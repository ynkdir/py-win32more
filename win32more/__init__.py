import re
import sys
import types
import uuid
from ctypes import (
    CFUNCTYPE,
    POINTER,
    WINFUNCTYPE,
    Array,
    Structure,
    Union,
    WinError,
    _CFuncPtr,
    addressof,
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
    windll,
)

if sys.version_info < (3, 9):
    from typing_extensions import get_type_hints as _get_type_hints
else:
    from typing import get_type_hints as _get_type_hints

if "(arm64)" in sys.version.lower():
    ARCH = "ARM64"
elif "(amd64)" in sys.version.lower():
    ARCH = "X64"
else:
    ARCH = "X86"

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


# FIXME: How to manage com reference count?  ContextManager style?
class ComPtr(c_void_p):
    def __new__(cls, value=None, own=False):
        self = super().__new__(cls)
        self.value = value
        self._own = own
        return self

    def __init__(self, *args, **kwargs):
        # Do not pass subclass's args to c_void_p.__init__().
        pass

    def __del__(self):
        if self and getattr(self, "_own", False):
            self.Release()

    @classmethod
    def __commit__(struct):
        struct._hints_ = get_type_hints_with_patch(struct)
        if struct._hints_["extends"] is None:
            return struct
        # Generic class have multiple base class (Generic[], ComPtr).
        struct.__bases__ = tuple(struct._hints_["extends"] if t is ComPtr else t for t in struct.__bases__)
        return struct

    def as_(self, cls):
        is_generic_alias = not isinstance(cls, type)
        if is_generic_alias:
            from win32more._winrt import _ro_get_parameterized_type_instance_iid

            iid = _ro_get_parameterized_type_instance_iid(cls)
        elif "_iid_" in cls.__dict__:
            iid = cls._iid_
        elif "default_interface" in cls._hints_:
            iid = cls._hints_["default_interface"]._iid_
        else:
            raise RuntimeError("no _iid_ found")
        instance = cls(own=True)
        hr = self.QueryInterface(pointer(iid), pointer(instance))
        if FAILED(hr):
            raise WinError(hr)
        return instance


# to avoid auto conversion to str when struct.member access and function() result.
class c_char_p_no(c_char_p):
    pass


class c_wchar_p_no(c_wchar_p):
    pass


def _patch_char_p(type_):
    if type_ is c_char_p:
        return c_char_p_no
    elif type_ is c_wchar_p:
        return c_wchar_p_no
    else:
        return type_


class EasyCastBase:
    @classmethod
    def __commit__(struct):
        # FIXME: not work for Union.
        # if hasattr(cls, "_fields_"):
        if "_fields_" in struct.__dict__:
            return struct

        hints = get_type_hints(struct)

        anonymous = [hint for hint in hints.keys() if re.match(r"^Anonymous\d*$", hint)]
        if anonymous:
            struct._anonymous_ = anonymous

        for type_ in hints.values():
            if type_ is not struct and issubclass(type_, (Structure, Union)):
                type_.__commit__()

        struct._fields_ = list(hints.items())

        for name, type_ in hints.items():
            # use __dict__[name] to avoid calling descriptor.__get__().
            setattr(struct, name, EasyCastDescriptor(struct.__dict__[name], type_))

        for name, type_ in hints.items():
            if issubclass(type_, (c_char_p, c_wchar_p)):
                setattr(struct, f"{name}_as_intptr", AsIntPtrDescriptor(struct.__dict__[name]))

        for hint in anonymous:
            hints.update(hints[hint]._hints_)

        struct._hints_ = hints

        return struct


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
        address = addressof(instance) + self._original_descriptor.offset
        return c_void_p.from_address(address).value

    def __set__(self, instance, value):
        self._original_descriptor.__set__(instance, value)


class EasyCastStructure(EasyCastBase, Structure):
    pass


class EasyCastUnion(EasyCastBase, Union):
    pass


EASY_TYPES = [  # obj_type, type_hint, c_func
    # python objects:
    (str, (POINTER(Int16), POINTER(UInt16)), c_wchar_p),
    # for function call for consistency with struct.member assignment.
    (int, (c_char_p, c_wchar_p), c_void_p),
    # for struct.member assignment for consistency with function call.
    (Array, (c_void_p,), None),
    # ctypes objects:
    (c_wchar_p, (POINTER(Int16), POINTER(UInt16)), None),
    (c_wchar_p, (POINTER(POINTER(Int16)), POINTER(POINTER(UInt16))), pointer),
    (c_char_p, (c_char_p_no,), None),
    (c_wchar_p, (c_wchar_p_no,), None),
]

easycast_keep_reference = []


def easycast(obj, type_):
    for obj_type, type_hint, c_func in EASY_TYPES:
        if isinstance(obj, obj_type) and issubclass(type_, type_hint):
            if c_func is not None:
                obj = c_func(obj)
            return cast(obj, type_)
    if issubclass(type_, _CFuncPtr):
        if isinstance(obj, type_):
            return obj
        elif callable(obj):
            r = type_(obj)
            easycast_keep_reference.append(r)
            return r
        elif obj is None:
            return type_()
    return obj


def get_type_hints(prototype):
    if sys.version_info < (3, 10) and isinstance(prototype, type) and issubclass(prototype, EasyCastBase):
        hints = _get_type_hints(prototype, localns=vars(prototype))
    else:
        hints = _get_type_hints(prototype)
    for name, type_ in hints.items():
        if type_ is type(None):
            hints[name] = None
    return hints


def get_type_hints_with_patch(prototype):
    hints = get_type_hints(prototype)
    for name, type_ in hints.items():
        hints[name] = _patch_char_p(type_)
    return hints


def get_type_hints_with_patch_return_only(prototype):
    hints = get_type_hints(prototype)
    for name, type_ in hints.items():
        if name == "return":
            hints[name] = _patch_char_p(type_)
    return hints


class Guid(EasyCastStructure):
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
    def __init__(self, prototype, factory):
        hints = get_type_hints_with_patch_return_only(prototype)
        restype = hints.pop("return")
        argtypes = list(hints.values())
        types = [restype] + argtypes
        params = tuple((1, name) for name in hints.keys())
        self.hints = hints
        self.hints.update({i: v for i, v in enumerate(argtypes)})
        self.delegate = factory(prototype.__name__, types, params)

    def __call__(self, *args, **kwargs):
        _as_intptr = kwargs.pop("_as_intptr", False)
        cargs, ckwargs = self.make_args(args, kwargs)
        result = self.delegate(*cargs, **ckwargs)
        return self.make_result(result, _as_intptr)

    def make_args(self, args, kwargs):
        cargs = [easycast(v, self.hints[i]) if i in self.hints else v for i, v in enumerate(args)]
        ckwargs = {k: easycast(v, self.hints[k]) if k in self.hints else v for k, v in kwargs.items()}
        return cargs, ckwargs

    def make_result(self, result, _as_intptr):
        if _as_intptr:
            return cast(result, c_void_p).value
        elif type(result) is c_char_p_no or type(result) is c_wchar_p_no:
            return result.value
        return result


class ComMethod:
    def __init__(self, vtbl_index, prototype):
        self._vtbl_index = vtbl_index
        self._prototype = prototype
        self._delegate = None

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return types.MethodType(self.__call__, instance)

    def __call__(self, this, *args, **kwargs):
        if self._delegate is None:
            self._delegate = ComMethodCaller(self._vtbl_index, self._prototype)
        return self._delegate(this, *args, **kwargs)


class ComMethodCaller:
    def __init__(self, vtbl_index, prototype):
        hints = get_type_hints_with_patch_return_only(prototype)
        restype = hints.pop("return")
        argtypes = list(hints.values())
        params = tuple((1, name) for name in hints.keys())
        hints.update({i: v for i, v in enumerate(argtypes)})
        self._hints = hints
        self._delegate = WINFUNCTYPE(restype, *argtypes)(vtbl_index, prototype.__name__, params)

    def __call__(self, this, *args, **kwargs):
        _as_intptr = kwargs.pop("_as_intptr", False)
        cargs, ckwargs = self.make_args(args, kwargs)
        result = self._delegate(this, *cargs, **ckwargs)
        return self.make_result(result, _as_intptr)

    def make_args(self, args, kwargs):
        cargs = [easycast(v, self._hints[i]) if i in self._hints else v for i, v in enumerate(args)]
        ckwargs = {k: easycast(v, self._hints[k]) if k in self._hints else v for k, v in kwargs.items()}
        return cargs, ckwargs

    def make_result(self, result, _as_intptr):
        if _as_intptr:
            return cast(result, c_void_p).value
        elif type(result) is c_char_p_no or type(result) is c_wchar_p_no:
            return result.value
        return result


def cfunctype(library, entry_point=None, variadic=False):
    def factory(name, types, params):
        if entry_point is not None:
            name = entry_point
        if variadic:
            # Disable keyword argument for variadic function.
            params = None
        return CFUNCTYPE(*types)((name, cdll[library]), params)

    def decorator(prototype):
        delegate = None

        def wrapper(*args, **kwargs):
            nonlocal delegate
            if delegate is None:
                delegate = ForeignFunction(prototype, factory)
            return delegate(*args, **kwargs)

        return wrapper

    return decorator


def winfunctype(library, entry_point=None):
    def factory(name, types, params):
        if entry_point is not None:
            name = entry_point
        return WINFUNCTYPE(*types)((name, windll[library]), params)

    def decorator(prototype):
        delegate = None

        def wrapper(*args, **kwargs):
            nonlocal delegate
            if delegate is None:
                delegate = ForeignFunction(prototype, factory)
            return delegate(*args, **kwargs)

        return wrapper

    return decorator


def commethod(vtbl_index):
    def decorator(prototype):
        return ComMethod(vtbl_index, prototype)

    return decorator


class BaseFuncType:
    def __init__(self, fn, kind):
        self.__module__ = fn.__module__  # referred by make_ready()
        self._fn = fn
        self._kind = kind

    def __commit__(self):
        types = list(get_type_hints_with_patch(self._fn).values())
        types = types[-1:] + types[:-1]
        return self._kind(*types)


def cfunctype_pointer(prototype):
    return BaseFuncType(prototype, CFUNCTYPE)


def winfunctype_pointer(prototype):
    return BaseFuncType(prototype, WINFUNCTYPE)


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
            prototype = self._lazyload.pop(name)
        except KeyError:
            raise AttributeError(f"module '{self._module.__name__}' has no attribute '{name}'") from None
        setattr(self._module, name, prototype)
        setattr(self._module, name, prototype.__commit__())
        return getattr(self._module, name)


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


def make_ready(module_name: str) -> None:
    module = sys.modules[module_name]

    module.__getattr__ = lazy_loader = LazyLoader(module)

    for name, value in vars(module).items():
        if isinstance(value, ConstantLazyLoader):
            value.__set_name__(module, name)
            lazy_loader.register(name, value)
        elif hasattr(value, "__commit__") and value.__module__ == module_name:
            lazy_loader.register(name, value)

    lazy_loader.setup()
