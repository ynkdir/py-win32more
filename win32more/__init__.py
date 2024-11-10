import re
import sys
import types
import uuid
from ctypes import (
    CFUNCTYPE,
    POINTER,
    Array,
    _CFuncPtr,
    c_bool,
    c_byte,
    c_char_p,
    c_double,
    c_float,
    c_int16,
    c_int32,
    c_int64,
    c_size_t,
    c_ssize_t,
    c_ubyte,
    c_uint16,
    c_uint32,
    c_uint64,
    c_void_p,
    c_wchar,
    c_wchar_p,
    cast,
    cdll,
    pointer,
)
from ctypes import Structure as _Structure
from ctypes import Union as _Union
from itertools import zip_longest

if sys.version_info < (3, 9):
    from typing_extensions import Annotated, get_args, get_origin
    from typing_extensions import get_type_hints as _get_type_hints
else:
    from typing import Annotated, get_args, get_origin
    from typing import get_type_hints as _get_type_hints

if "(arm64)" in sys.version.lower():
    ARCH = "ARM64"
elif "(amd64)" in sys.version.lower():
    ARCH = "X64"
else:
    ARCH = "X86"

if sys.platform == "cygwin":
    from ._cygwin import ARCH, WINFUNCTYPE, WinError, windll  # noqa: F401
else:
    from ctypes import WINFUNCTYPE, WinError, windll

Byte = c_ubyte
SByte = c_byte
Char = c_wchar
Int16 = c_int16
UInt16 = c_uint16
Int32 = c_int32
UInt32 = c_uint32
Int64 = c_int64
UInt64 = c_uint64
IntPtr = c_ssize_t
UIntPtr = c_size_t
Single = c_float
Double = c_double
Bytes = c_char_p
String = c_wchar_p
Boolean = c_bool
VoidPtr = c_void_p
Void = None


class Enum:
    pass


# FIXME: How to manage com reference count?  ContextManager style?
class ComPtr(c_void_p):
    def __init__(self, value=None, own=False, move=None):
        super().__init__()
        if move is not None:
            self.value = move.value
            self._own = getattr(move, "_own", False)
            move.value = None
            move._own = False
        else:
            self.value = value
            self._own = own

    def __del__(self):
        if self and getattr(self, "_own", False):
            self.Release()

    # overwritten in _winrt.py
    @classmethod
    def __commit__(cls):
        cls._hints_ = get_type_hints(cls)
        if cls._hints_["extends"] is None:
            return cls
        cls.__bases__ = (cls._hints_["extends"],)
        return cls

    # overwritten in _winrt.py
    def as_(self, cls):
        iid = cls._iid_
        instance = cls(own=True)
        hr = self.QueryInterface(pointer(iid), pointer(instance))
        if FAILED(hr):
            raise WinError(hr)
        return instance

    def __eq__(self, other):
        return isinstance(other, ComPtr) and self.value == other.value


def _struct_union_commit(cls, start=True):
    if start:
        # First, register cls for circular reference.
        module = sys.modules[cls.__module__]
        setattr(module, cls.__name__, cls)

    hints = get_type_hints(cls)

    ireference_types = {}

    for name, type_ in hints.items():
        if getattr(type_, "_classid_", None) == "Windows.Foundation.IReference":
            ireference_types[name] = type_
            hints[name] = get_origin(type_)

    for type_ in hints.values():
        if issubclass(type_, (Structure, Union)) and "_fields_" not in type_.__dict__:
            # nested struct or circular reference
            _struct_union_commit(type_, False)

    # FIXME: hasattr(cls, "_fields_") not work for Union.
    if "_fields_" in cls.__dict__:
        raise CircularReferenceResolved()

    bitfields = {}
    for name, type_ in get_type_hints(cls, include_extras=True).items():
        if get_origin(type_) is Annotated:
            _, width = get_args(type_)
            bitfields[name] = width

    anonymous = [name for name in hints.keys() if re.match(r"^Anonymous\d*$", name) and name not in bitfields]
    if anonymous:
        cls._anonymous_ = anonymous

    fields = []
    for name, type_ in hints.items():
        if name in bitfields:
            fields.append((name, type_, bitfields[name]))
        else:
            fields.append((name, type_))

    cls._fields_ = fields

    for name, type_ in hints.items():
        # use __dict__[name] to avoid calling descriptor.__get__().
        setattr(cls, name, EasyCastDescriptor(cls.__dict__[name], type_))

    for name, type_ in hints.items():
        if issubclass(type_, (c_char_p, c_wchar_p)):
            setattr(cls, f"{name}_as_intptr", AsIntPtrDescriptor(cls.__dict__[name]))

    for name, type_ in ireference_types.items():
        setattr(cls, name, IReferenceDescriptor(cls.__dict__[name], type_))

    for name in anonymous:
        hints.update(hints[name]._hints_)

    cls._hints_ = hints

    return cls


class Structure(_Structure):
    __commit__ = classmethod(_struct_union_commit)


class Union(_Union):
    __commit__ = classmethod(_struct_union_commit)


class EasyCastDescriptor:
    def __init__(self, original_descriptor, type_):
        self._original_descriptor = original_descriptor
        self._type = type_

    def __get__(self, instance, owner=None):
        if instance is None:
            # _ctypes/stgdict.c:MakeFields() raises TypeError for non _ctypes.CField type.
            return self._original_descriptor.__get__(instance, owner)
        return self._original_descriptor.__get__(instance, owner)

    def __set__(self, instance, value):
        self._original_descriptor.__set__(instance, easycast(value, self._type))

    @property
    def offset(self):
        return self._original_descriptor.offset


class AsIntPtrDescriptor:
    def __init__(self, original_descriptor):
        self._original_descriptor = original_descriptor

    def __get__(self, instance, owner=None):
        if instance is None:
            return self._original_descriptor.__get__(instance, owner)
        return UIntPtr.from_buffer(instance, self._original_descriptor.offset).value

    def __set__(self, instance, value):
        self._original_descriptor.__set__(instance, value)


class IReferenceDescriptor:
    def __init__(self, original_descriptor, type_):
        self._original_descriptor = original_descriptor
        self._type = type_

    def __get__(self, instance, owner=None):
        if instance is None:
            return self._original_descriptor.__get__(instance, owner)
        return self._type(move=self._original_descriptor.__get__(instance, owner))

    def __set__(self, instance, value):
        self._original_descriptor.__set__(instance, value)

    @property
    def offset(self):
        return self._original_descriptor.offset


easycast_keep_reference = []


def easycast(obj, type_):
    if issubclass(type_, (POINTER(Int16), POINTER(UInt16))):
        if isinstance(obj, str):
            return cast(c_wchar_p(obj), type_)
        elif isinstance(obj, c_wchar_p):
            return cast(obj, type_)
    elif issubclass(type_, (POINTER(POINTER(Int16)), POINTER(POINTER(UInt16)))):
        if isinstance(obj, c_wchar_p):
            return cast(pointer(obj), type_)
    elif issubclass(type_, (c_char_p, c_wchar_p)):
        if isinstance(obj, int):
            # function doesn't support this conversion, though struct does it.
            return type_(obj)
    elif issubclass(type_, ComPtr):
        if isinstance(obj, (str, bytes)):
            # disable default conversion
            raise TypeError(f"cannot convert from {type(obj)} to ComPtr")
    elif issubclass(type_, c_void_p):
        if isinstance(obj, Array):
            # struct doesn't support this conversion, though function does it.
            return cast(obj, c_void_p)
    elif issubclass(type_, _CFuncPtr):
        if isinstance(obj, type_):
            return obj
        elif callable(obj):
            r = type_(obj)
            easycast_keep_reference.append(r)
            return r
        elif obj is None:
            return type_()
    return obj


def get_type_hints(prototype, include_extras=False):
    if sys.version_info < (3, 10) and isinstance(prototype, type) and issubclass(prototype, (Structure, Union)):
        hints = _get_type_hints(prototype, localns=vars(prototype), include_extras=include_extras)
    else:
        hints = _get_type_hints(prototype, include_extras=include_extras)
    for name, type_ in hints.items():
        if not isinstance(type_, type):
            # generic
            pass
        elif type_ is type(None):
            hints[name] = None
        elif issubclass(type_, Enum):
            # Ctype's fundamental types are converted to python type transparently.
            # It is not applied to subclass.  Avoid it for Enum.
            hints[name] = type_.__bases__[1]
    return hints


def parse_arguments(funcname: str, params: list, args: tuple, kwargs: dict, variadic: bool) -> list:
    for k in params[: len(args)]:
        if k in kwargs:
            raise TypeError(f"{funcname}() got multiple values for argument '{k}'")
    for k in kwargs:
        if k not in params:
            raise TypeError(f"{funcname}() got an unexpected keyword argument '{k}'")
    nargs = len(args) + len(kwargs)
    if nargs < len(params):
        missing_count = len(params) - nargs
        missing_keys = ", ".join(f"'{k}'" for k in params[-missing_count:])
        raise TypeError(f"{funcname}() missing {missing_count} required positional arguments: {missing_keys}")
    if nargs > len(params) and not variadic:
        raise TypeError(f"{funcname}() takes {len(params)} positional arguments but {nargs} were given")
    return list(args) + list(kwargs[k] for k in params[len(args) :])


class Guid(Structure):
    _fields_ = [
        ("Data1", UInt32),
        ("Data2", UInt16),
        ("Data3", UInt16),
        ("Data4", Byte * 8),
    ]
    _hints_ = {
        "Data1": UInt32,
        "Data2": UInt16,
        "Data3": UInt16,
        "Data4": Byte * 8,
    }

    def __init__(self, val=None):
        if val is None:
            pass
        elif isinstance(val, self.__class__):
            self.Data1 = val.Data1
            self.Data2 = val.Data2
            self.Data3 = val.Data3
            self.Data4 = val.Data4
        elif isinstance(val, str):
            u = uuid.UUID(val)
            self.Data1 = u.time_low
            self.Data2 = u.time_mid
            self.Data3 = u.time_hi_version
            for i in range(8):
                self.Data4[i] = u.bytes[8 + i]
        elif isinstance(val, uuid.UUID):
            u = val
            self.Data1 = u.time_low
            self.Data2 = u.time_mid
            self.Data3 = u.time_hi_version
            for i in range(8):
                self.Data4[i] = u.bytes[8 + i]
        else:
            raise ValueError()

    def __str__(self):
        return f"{{{self.Data1:08x}-{self.Data2:04x}-{self.Data3:04x}-{self.Data4[0]:02x}{self.Data4[1]:02x}-{self.Data4[2]:02x}{self.Data4[3]:02x}{self.Data4[4]:02x}{self.Data4[5]:02x}{self.Data4[6]:02x}{self.Data4[7]:02x}}}"

    def __eq__(self, other):
        if not isinstance(other, Guid):
            raise ValueError(f"cannot compare with {type(other)}")
        return (
            self.Data1 == other.Data1
            and self.Data2 == other.Data2
            and self.Data3 == other.Data3
            and self.Data4[0] == other.Data4[0]
            and self.Data4[1] == other.Data4[1]
            and self.Data4[2] == other.Data4[2]
            and self.Data4[3] == other.Data4[3]
            and self.Data4[4] == other.Data4[4]
            and self.Data4[5] == other.Data4[5]
            and self.Data4[6] == other.Data4[6]
            and self.Data4[7] == other.Data4[7]
        )


def SUCCEEDED(hr):
    return hr >= 0


def FAILED(hr):
    return hr < 0


class ForeignFunction:
    def __init__(self, prototype, library, entry_point, variadic, dlltype, functype):
        self._prototype = prototype
        self._library = library
        self._entry_point = entry_point
        self._variadic = variadic
        self._dlltype = dlltype
        self._functype = functype
        self._delegate = None

    def _create_foreign_function_call(self):
        if self._entry_point is None:
            entry_point = self._prototype.__name__
        else:
            entry_point = self._entry_point
        if self._variadic:
            # Disable keyword argument for variadic function.
            params = None
        else:
            params = tuple((1, name) for name in self._prototype.__annotations__.keys() if name != "return")
        return ForeignFunctionCall(
            self._prototype, self._functype, [(entry_point, self._dlltype[self._library]), params], self._variadic
        )

    def __call__(self, *args, **kwargs):
        if self._delegate is None:
            self._delegate = self._create_foreign_function_call()
        return self._delegate(*args, **kwargs)


class ForeignFunctionCall:
    def __init__(self, prototype, functype, spec, variadic):
        hints = get_type_hints(prototype)
        self._restype = restype = hints.pop("return")
        if self._restype is c_char_p or self._restype is c_wchar_p:
            restype = UIntPtr
        self._prototype = prototype
        self._hints = hints
        self._variadic = variadic
        self._delegate = functype(restype, *self._hints.values())(*spec)

    def __call__(self, *args, **kwargs):
        _as_intptr = kwargs.pop("_as_intptr", False)
        cargs = self.make_args(args, kwargs)
        result = self._delegate(*cargs)
        return self.make_result(result, _as_intptr)

    def make_args(self, args, kwargs):
        pargs = parse_arguments(self._prototype.__qualname__, list(self._hints), args, kwargs, self._variadic)
        return [easycast(v, t) if t else v for v, t in zip_longest(pargs, self._hints.values())]

    def make_result(self, result, _as_intptr):
        if _as_intptr:
            if result is None:
                return 0
            return result
        if self._restype is c_char_p or self._restype is c_wchar_p:
            return self._restype(result).value
        return result


class ComMethod:
    def __init__(self, prototype, vtbl_index):
        self._prototype = prototype
        self._vtbl_index = vtbl_index
        self._delegate = None

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return types.MethodType(self.__call__, instance)

    def __call__(self, this, *args, **kwargs):
        if self._delegate is None:
            self._delegate = ComMethodCall(self._prototype, self._vtbl_index)
        return self._delegate(this, *args, **kwargs)


class ComMethodCall:
    def __init__(self, prototype, vtbl_index):
        hints = get_type_hints(prototype)
        self._restype = restype = hints.pop("return")
        if self._restype is c_char_p or self._restype is c_wchar_p:
            restype = UIntPtr
        params = tuple((1, name) for name in hints.keys())
        self._prototype = prototype
        self._hints = hints
        self._delegate = WINFUNCTYPE(restype, *self._hints.values())(vtbl_index, prototype.__name__, params)

    def __call__(self, this, *args, **kwargs):
        _as_intptr = kwargs.pop("_as_intptr", False)
        cargs = self.make_args(args, kwargs)
        result = self._delegate(this, *cargs)
        return self.make_result(result, _as_intptr)

    def make_args(self, args, kwargs):
        pargs = parse_arguments(self._prototype.__qualname__, list(self._hints), args, kwargs, False)
        return [easycast(v, t) for v, t in zip(pargs, self._hints.values())]  # >=3.10 strict=True

    def make_result(self, result, _as_intptr):
        if _as_intptr:
            if result is None:
                return 0
            return result
        if self._restype is c_char_p or self._restype is c_wchar_p:
            return self._restype(result).value
        return result


def cfunctype(library, entry_point=None, variadic=False):
    def decorator(prototype):
        return ForeignFunction(prototype, library, entry_point, variadic, cdll, CFUNCTYPE)

    return decorator


def winfunctype(library, entry_point=None):
    def decorator(prototype):
        return ForeignFunction(prototype, library, entry_point, False, windll, WINFUNCTYPE)

    return decorator


def commethod(vtbl_index):
    def decorator(prototype):
        return ComMethod(prototype, vtbl_index)

    return decorator


class ForeignFunctionPointer:
    def __init__(self, prototype, functype):
        self.__module__ = prototype.__module__  # referred by make_ready()
        self._prototype = prototype
        self._functype = functype

    def __commit__(self):
        hints = get_type_hints(self._prototype)

        if self._prototype.__name__ in sys.modules[self.__module__].__dict__:
            raise CircularReferenceResolved()

        restype = hints.pop("return")
        argtypes = list(hints.values())
        return self._functype(restype, *argtypes)


def cfunctype_pointer(prototype):
    return ForeignFunctionPointer(prototype, CFUNCTYPE)


def winfunctype_pointer(prototype):
    return ForeignFunctionPointer(prototype, WINFUNCTYPE)


class LazyLoader:
    def __init__(self, module):
        self._module = module
        self._lazyload = {}

    def register(self, name, prototype):
        self._lazyload[name] = prototype

    def setup(self):
        for name in self._lazyload:
            delattr(self._module, name)

    def __call__(self, name):
        try:
            prototype = self._lazyload[name]
        except KeyError:
            raise AttributeError(f"module '{self._module.__name__}' has no attribute '{name}'") from None
        try:
            setattr(self._module, name, prototype.__commit__())
            del self._lazyload[name]
        except CircularReferenceResolved:
            pass
        except AttributeError as e:
            # AttributeError will be ignored in __getattr__().
            raise RuntimeError("Unexpected error") from e
        return getattr(self._module, name)


class CircularReferenceResolved(Exception):
    pass


class ConstantLazyLoader:
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self.__annotations__ = {}

    def __set_name__(self, owner, name):
        # get_type_hints() referes __globals__.
        self.__globals__ = owner.__dict__
        self.__annotations__["self"] = owner.__annotations__[name]

    def __commit__(self):
        cls = get_type_hints(self)["self"]
        return cls(*self._args, **self._kwargs)


class UnicodeAlias:
    def __init__(self, unicode_name):
        self._unicode_name = unicode_name
        self._owner = None

    def __set_name__(self, owner, name):
        self._owner = owner

    def __commit__(self):
        return getattr(self._owner, self._unicode_name)


def make_ready(module_name: str) -> None:
    module = sys.modules[module_name]

    module.__getattr__ = lazy_loader = LazyLoader(module)

    for name, value in vars(module).items():
        if isinstance(value, ConstantLazyLoader):
            value.__set_name__(module, name)
            lazy_loader.register(name, value)
        elif isinstance(value, UnicodeAlias):
            value.__set_name__(module, name)
            lazy_loader.register(name, value)
        elif hasattr(value, "__commit__") and value.__module__ == module_name:
            lazy_loader.register(name, value)

    lazy_loader.setup()
