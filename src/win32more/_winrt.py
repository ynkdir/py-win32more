from __future__ import annotations

import asyncio
import inspect
import logging
import types
from collections.abc import MutableSequence, Sequence
from contextlib import ExitStack
from ctypes import (
    POINTER,
    _SimpleCData,
    cast,
    pointer,
    sizeof,
)
from functools import partial
from typing import (
    Any,
    Generic,
    Tuple,  # noqa: F401
    TypeVar,
    get_args,
    get_origin,
)

from . import asyncui
from ._boxing import box_value, unbox_value
from ._comclass import ComClass, ISelf, is_com_class, is_com_instance
from ._comerror import ComError
from ._generic import (
    GenericSpecializer,
    generic_get_type_hints,
    get_origin_or_itself,
    get_original_class,
    is_generic_alias,
    is_generic_instance,
)
from ._hstr import hstr
from ._ro import ro_activate_instance, ro_get_activation_factory
from ._win32 import (
    FAILED,
    WINFUNCTYPE,
    Enum,
    UInt32,
    Void,
    WinError,
    easycast,
    get_type_hints,
)
from ._win32api import (
    HRESULT,
    CoTaskMemAlloc,
    CoTaskMemFree,
    IAgileObject,
    IInspectable,
    IUnknown,
)

# TODO: For backword compatibility.  Remove later.
WinRT_String = hstr

K = TypeVar("K")
T = TypeVar("T")
V = TypeVar("V")
TProgress = TypeVar("TProgress")
TResult = TypeVar("TResult")
TSender = TypeVar("TSender")

logger = logging.getLogger(__name__)


class event:
    def __init__(self):
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return event_setter(instance, self._name)


class event_setter:
    def __init__(self, instance, name):
        self._instance = instance
        self._name = name

    def __iadd__(self, callback):
        getattr(self._instance, f"add_{self._name}")(callback)


def winrt_easycast(obj, type_):
    from win32more._vector import Vector
    from win32more.Windows.Foundation import IReference
    from win32more.Windows.Foundation.Collections import IVector

    if type_ is IInspectable:
        if isinstance(obj, str):
            return box_value(obj)
    elif issubclass(get_origin_or_itself(type_), IVector):
        if isinstance(obj, list):
            return Vector[get_args(type_)[0]](obj)
    elif issubclass(get_origin_or_itself(type_), IReference):
        # FIXME: Should I check obj is T of IReference[T]?
        if obj is None:
            return IReference(None)
        return box_value(obj).as_(type_)
    elif is_generic_alias(type_):
        # Do not propagate generic type
        return obj
    return easycast(obj, type_)


# Dummy type for list[T]
class PassArray(Generic[T]):
    def __init__(self, type_, seq, cargs):
        self._type = type_

        if isinstance(seq, Sequence):
            if self._type is hstr:
                self._seq = [hstr(s, own=True) for s in seq]
            else:
                self._seq = seq
            cargs.append(len(self._seq))
            cargs.append((self._type * len(self._seq))(*self._seq))
        else:
            raise TypeError(f"cannot convert {type(seq)} to PassArray[{type_.__name__}]")

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class PassArrayCallback:
    def __init__(self, type_, size, ptr, pyargs):
        self._type = type_
        self._size = size
        self._ptr = ptr
        self._lst = []
        for i in range(size):
            if type_ is hstr:
                self._lst.append(str(ptr[i]))
            elif not is_simple_cdata(type_):
                self._lst.append(type_.from_buffer_copy(ptr[i]))
            else:
                self._lst.append(ptr[i])
        pyargs.append(self._lst)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass


# Dummy type for list[T]
class FillArray(Generic[T]):
    def __init__(self, type_, seq, cargs):
        self._type = type_

        if isinstance(seq, MutableSequence):
            self._seq = seq
            self._ptr = (type_ * len(seq))()
            cargs.append(len(self._seq))
            cargs.append(self._ptr)
        else:
            raise TypeError(f"cannot convert {type(seq)} to FillArray[{type_.__name__}]")

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            return

        if self._type is hstr:
            self._seq[:] = [str(s) for s in self._ptr[:]]
            for s in self._ptr[:]:
                s.clear()
        elif is_com_class(self._type):
            self._seq[:] = self._ptr[:]
            for p in self.seq:
                p._own = True
        else:
            self._seq[:] = self._ptr[:]


class FillArrayCallback:
    def __init__(self, type_, size, ptr, pyargs):
        self._type = type_
        self._size = size
        self._ptr = ptr
        self._lst = [None] * size
        pyargs.append(self._lst)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            return

        for i, v in enumerate(self._lst):
            if self._type is hstr:
                self._ptr[i] = hstr(v)
            elif is_com_class(self._type):
                if v:
                    v.AddRef()
                self._ptr[i] = v
            else:
                self._ptr[i] = v


# Dummy type for list[T]
class ReceiveArray(Generic[T]):
    def __init__(self, type_, seq, cargs):
        self._type = type_

        if isinstance(seq, MutableSequence):
            self._seq = seq
            self._size = UInt32()
            self._ptr = POINTER(type_)()
            cargs.append(pointer(self._size))
            cargs.append(pointer(self._ptr))
        else:
            raise TypeError(f"cannot convert {type(seq)} to ReceiveArray[{type_.__name__}]")

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            return

        if self._type is hstr:
            self._seq[:] = [str(s) for s in self._ptr[: self._size.value]]
            for s in self._ptr[: self._size.value]:
                s.clear()
        elif is_com_class(self._type):
            self._seq[:] = [self._type.from_buffer_copy(p) for p in self._ptr[: self._size.value]]
            for p in self._seq:
                p._own = True
        elif not is_simple_cdata(self._type):
            self._seq[:] = [self._type.from_buffer_copy(p) for p in self._ptr[: self._size.value]]
        else:
            self._seq[:] = self._ptr[: self._size.value]
        CoTaskMemFree(self._ptr)


class ReceiveArrayCallback:
    def __init__(self, type_, psize, pptr, pyargs):
        self._type = type_
        self._psize = psize
        self._pptr = pptr
        self._lst = []
        pyargs.append(self._lst)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            return
        self.handle_result(self._type, self._psize, self._pptr, self._lst)

    @staticmethod
    def handle_result(type_, psize, pptr, seq):
        if not isinstance(seq, Sequence):
            raise ValueError(f"Sequence is expected: {seq}")

        psize[0] = len(seq)
        ptr = CoTaskMemAlloc(len(seq) * sizeof(type_))
        if not ptr:
            raise WinError()
        pptr[0] = cast(ptr, POINTER(type_))
        for i, v in enumerate(seq):
            if type_ is hstr:
                pptr[0][i] = hstr(v)
            elif is_com_class(type_):
                if v:
                    v.AddRef()
                pptr[0][i] = v
            else:
                pptr[0][i] = v


class WinrtMethod:
    def __init__(self, prototype, vtbl_index):
        self._prototype = prototype
        self._vtbl_index = vtbl_index
        self._generic_delegate = {}

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return types.MethodType(self.__call__, instance)

    def __call__(self, this, *args, **kwargs):
        cls = get_original_class(this)
        generic_args = get_args(cls)
        if generic_args not in self._generic_delegate:
            self._generic_delegate[generic_args] = WinrtMethodCall(self._prototype, self._vtbl_index, cls)
        return self._generic_delegate[generic_args](this, *args, **kwargs)


class WinrtMethodCall:
    def __init__(self, prototype, vtbl_index, cls):
        hints = generic_get_type_hints(prototype, cls)
        restype = hints.pop("return")
        argtypes = []
        params = []
        for name, type_ in hints.items():
            self._add_parameter(argtypes, params, name, type_)
        self._add_restype(argtypes, params, restype)
        self.delegate = WINFUNCTYPE(HRESULT, *argtypes)(vtbl_index, prototype.__name__, tuple(params))
        self.restype = restype
        self._prototype = prototype
        self.hints = hints
        self._signature = inspect.signature(prototype)

    def __call__(self, this, *args, **kwargs):
        with ExitStack() as exitstack:
            cargs = []
            pargs = self._signature.bind(None, *args, **kwargs).args[1:]
            for value, type_ in zip(pargs, self.hints.values()):  # >=3.10 strict=True
                self._add_argument(cargs, value, type_, exitstack)
            result = self._add_result(cargs, self.restype, exitstack)
            hr = self.delegate(this, *cargs)
            if FAILED(hr):
                # FIXME: Is restricted error obtained here always associated with this hr?
                raise ComError(hr)
        return self._handle_result(result)

    def _add_parameter(self, argtypes: list[type], params: list[tuple[int, str]], name: str, type_: type) -> None:
        if is_passarray_class(type_):
            argtypes.append(UInt32)
            argtypes.append(POINTER(get_args(type_)[0]))
            params.append((1, f"{name}_length"))
            params.append((1, name))
        elif is_fillarray_class(type_):
            argtypes.append(UInt32)
            argtypes.append(POINTER(get_args(type_)[0]))
            params.append((1, f"{name}_length"))
            params.append((1, name))
        elif is_receivearray_class(type_):
            argtypes.append(POINTER(UInt32))
            argtypes.append(POINTER(POINTER(get_args(type_)[0])))
            params.append((1, f"{name}_length"))
            params.append((1, name))
        elif is_delegate_class(type_):
            argtypes.append(MulticastDelegateImpl)
            params.append((1, name))
        elif is_generic_alias(type_):
            argtypes.append(get_origin(type_))
            params.append((1, name))
        else:
            argtypes.append(type_)
            params.append((1, name))

    def _add_restype(self, argtypes: list[type], params: list[tuple[int, str]], restype: type) -> None:
        if restype is Void:
            pass
        elif is_receivearray_class(restype):
            argtypes.append(POINTER(UInt32))
            argtypes.append(POINTER(POINTER(get_args(restype)[0])))
            params.append((1, "return_length"))
            params.append((1, "return"))
        elif is_generic_alias(restype):
            argtypes.append(POINTER(get_origin(restype)))
            params.append((1, "return"))
        else:
            argtypes.append(POINTER(restype))
            params.append((1, "return"))

    def _add_argument(self, cargs: list[Any], value: Any, type_: type, exitstack: ExitStack) -> None:
        if is_passarray_class(type_):
            exitstack.enter_context(PassArray(get_args(type_)[0], value, cargs))
        elif is_fillarray_class(type_):
            exitstack.enter_context(FillArray(get_args(type_)[0], value, cargs))
        elif is_receivearray_class(type_):
            exitstack.enter_context(ReceiveArray(get_args(type_)[0], value, cargs))
        elif is_delegate_class(type_):
            cargs.append(MulticastDelegateImpl(type_, value))
        elif is_com_instance(value) and is_com_class(type_):
            cargs.append(value.as_(type_))
        else:
            cargs.append(winrt_easycast(value, type_))

    def _add_result(self, cargs: list[Any], restype: type, exitstack) -> None:
        if self.restype is Void:
            result = None
        elif is_receivearray_class(self.restype):
            result = []
            exitstack.enter_context(ReceiveArray(get_args(self.restype)[0], result, cargs))
        elif is_com_class(self.restype):
            result = self.restype(own=True)
            cargs.append(pointer(result))
        elif self.restype is hstr:
            result = self.restype(own=True)
            cargs.append(pointer(result))
        else:
            result = self.restype()
            cargs.append(pointer(result))
        return result

    def _handle_result(self, result: Any) -> Any:
        from win32more.Windows.Foundation import IReference

        if self.restype is Void:
            return None
        elif issubclass(get_origin_or_itself(self.restype), IReference):
            if not result:
                return None
            return unbox_value(result)
        elif issubclass(get_origin_or_itself(self.restype), Enum):
            return result.value
        elif is_com_class(self.restype):
            if not result:
                return None
            return result
        elif self.restype is hstr:
            return str(result)
        elif is_simple_cdata(get_origin_or_itself(self.restype)):
            return result.value
        return result


def winrt_commethod(vtbl_index):
    def decorator(prototype):
        return WinrtMethod(prototype, vtbl_index)

    return decorator


class winrt_mixinmethod:
    def __init__(self, prototype):
        self._prototype = prototype

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return types.MethodType(self.__call__, instance)

    def __call__(self, instance, *args, **kwargs):
        hints = get_type_hints(self._prototype)
        interface_instance = instance.as_(hints["self"])
        return getattr(interface_instance, self._prototype.__name__)(*args, **kwargs)

    def argcount(self):
        return len(self._prototype.__annotations__) - 2


def is_delegate_class(cls):
    return issubclass(get_origin_or_itself(cls), MulticastDelegate)


def is_passarray_class(cls):
    return issubclass(get_origin_or_itself(cls), PassArray)


def is_fillarray_class(cls):
    return issubclass(get_origin_or_itself(cls), FillArray)


def is_receivearray_class(cls):
    return issubclass(get_origin_or_itself(cls), ReceiveArray)


# check if ptr[0] returns python primitive?
def is_simple_cdata(cls):
    return cls.__base__ is _SimpleCData


class winrt_classmethod:
    def __init__(self, prototype):
        self._prototype = prototype

    def __get__(self, instance, owner=None):
        return types.MethodType(self.__call__, owner)

    def __call__(self, cls, *args, **kwargs):
        hints = get_type_hints(self._prototype)
        factory_class = hints["cls"]
        factory = ro_get_activation_factory(cls._classid_).as_(factory_class)
        return getattr(factory, self._prototype.__name__)(*args, **kwargs)

    def argcount(self):
        return len(self._prototype.__annotations__) - 2


def winrt_factorymethod(prototype):
    return winrt_classmethod(prototype)


class winrt_activatemethod:
    def __init__(self, prototype):
        self._prototype = prototype

    def __get__(self, instance, owner=None):
        return types.MethodType(self.__call__, owner)

    def __call__(self, cls):
        return ro_activate_instance(cls._classid_).as_(cls)

    def argcount(self):
        return 0


class winrt_overload:
    def __init__(self, func: winrt_mixinmethod | winrt_classmethod | winrt_activatemethod) -> None:
        self.funcs = [func]

    def register(self, func: winrt_mixinmethod | winrt_classmethod | winrt_activatemethod):
        self.funcs.append(func)
        return self

    def __get__(self, instance, owner=None):
        if instance is None:
            return types.MethodType(self._call_classmethod, owner)
        else:
            return types.MethodType(self._call_method, instance)

    def _call_classmethod(self, cls, *args, **kwargs):
        for func in self.funcs:
            if isinstance(func, (winrt_classmethod, winrt_activatemethod)) and len(args) == func.argcount():
                return func(cls, *args, **kwargs)
        raise ValueError("no matched method")

    def _call_method(self, instance, *args, **kwargs):
        for func in self.funcs:
            if isinstance(func, winrt_mixinmethod) and len(args) == func.argcount():
                return func(instance, *args, **kwargs)
        raise ValueError("no matched method")


class MulticastDelegate(IUnknown):
    pass


class MulticastDelegateImpl(ComClass):
    def __init__(self, interface, callback):
        if not callable(callback):
            raise TypeError(f"cannot convert {type(callback)} to MulticastDelegate")
        self._interface = interface
        self._callback = callback
        super().__init__(own=True)

    def _implemented_interfaces(self):
        return [self._interface, IUnknown, IAgileObject, ISelf]

    def Invoke(self, *args):
        if inspect.iscoroutinefunction(self._callback):
            self._addref(args)
            future = asyncui.create_task(self._callback(*args))
            future.add_done_callback(lambda _: self._release(args))
            return None
        return self._callback(*args)

    def _addref(self, args):
        for obj in args:
            if isinstance(obj, IUnknown) and obj.value:
                obj.AddRef()

    def _release(self, args):
        for obj in args:
            if isinstance(obj, IUnknown) and obj.value:
                obj.Release()


class AwaitableProtocol:
    def __await__(self):
        future = asyncio.get_running_loop().create_future()
        self.Completed = partial(self.__on_completed, future)
        return future.__await__()

    def __on_completed(self, future, asyncInfo, asyncStatus):
        from win32more.Windows.Foundation import AsyncStatus, IAsyncInfo

        if asyncStatus == AsyncStatus.Completed:
            future.get_loop().call_soon_threadsafe(future.set_result, asyncInfo.GetResults())
        elif asyncStatus == AsyncStatus.Error:
            # It seems that restricted error info is built by invoking IAsyncInfo.ErrorCode.
            error = ComError(asyncInfo.as_(IAsyncInfo).ErrorCode.Value)
            future.get_loop().call_soon_threadsafe(future.set_exception, error)
        elif asyncStatus == AsyncStatus.Canceled:
            future.get_loop().call_soon_threadsafe(future.cancel)
        else:
            assert False, "unreachable"


class IterableProtocol:
    def __class_getitem__(cls, key):
        return cls

    def __iter__(self):
        iterator = self.First()
        while iterator.HasCurrent:
            yield iterator.Current
            iterator.MoveNext()


class SequenceProtocol:
    def __class_getitem__(cls, key):
        return cls

    def __len__(self):
        return self.Size

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self[i] for i in range(*index.indices(len(self)))]
        elif isinstance(index, int):
            if index < 0:
                index += len(self)
            if index < 0 or len(self) <= index:
                raise IndexError("list index out of range")
            return self.GetAt(index)
        else:
            raise TypeError(f"list indices must be integers or slices, not {type(index).__name__}")


class MappingProtocol:
    def __class_getitem__(cls, key):
        classdict = dict(cls.__dict__)
        classdict["_MappingProtocol__parameters"] = key
        return type("MappingProtocol", (), classdict)

    def __args(self):
        if not is_generic_instance(self):
            return self.__parameters
        gs = GenericSpecializer.from_generic_alias(get_original_class(self))
        return gs.specialize_parameters(self.__parameters)

    def __iterator(self):
        from win32more.Windows.Foundation.Collections import IIterable, IKeyValuePair

        args = self.__args()
        iterable = self.as_(IIterable[IKeyValuePair[args[0], args[1]]])
        for pair in iterable:
            yield pair.Key, pair.Value

    def __iter__(self):
        yield from self.keys()

    def __len__(self):
        return self.Size

    def __getitem__(self, key):
        if not self.HasKey(key):
            raise KeyError(key)
        return self.Lookup(key)

    def __contains__(self, key):
        return self.HasKey(key)

    def items(self):
        for k, v in self.__iterator():
            yield k, v

    def keys(self):
        for k, v in self.__iterator():
            yield k

    def values(self):
        for k, v in self.__iterator():
            yield v

    def get(self, key, default=None):
        if not self.HasKey(key):
            return default
        return self.Lookup(key)

    def __eq__(self, other):
        return dict(self.items()) == dict(other.items())


# IClosable
class ContextManagerProtocol:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        from win32more.Windows.Foundation import IClosable

        self.as_(IClosable).Close()
