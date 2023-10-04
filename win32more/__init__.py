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

MissingType = c_void_p

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
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        cls._hints_ = get_type_hints(cls)
        if cls._hints_["extends"] is not None:
            # Generic class have multiple base class (Generic[], ComPtr).
            cls.__bases__ = tuple(
                cls._hints_["extends"] if t is ComPtr else t
                for t in cls.__bases__
            )

    def __init__(self, value=None, own=False):
        super().__init__(value)
        self._own = own

    def __del__(self):
        if self and getattr(self, "_own", False):
            self.Release()


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


def _removesuffix(s, suffix):
    if sys.version_info < (3, 9):
        if s.endswith(suffix):
            return s[: -len(suffix)]
        else:
            return s
    return s.removesuffix(suffix)


class EasyCastStructure(Structure):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # FIXME: not work for Union.
        # if hasattr(cls, "_fields_"):
        if "_fields_" in dir(cls):
            return

        hints = {
            name: _patch_char_p(type_)
            for name, type_ in get_type_hints(cls).items()
        }
        anonymous = [
            name for name in hints.keys()
            if re.match(r"^Anonymous\d*$", name)
        ]
        if anonymous:
            cls._anonymous_ = anonymous

        cls._fields_ = list(hints.items())

        for name in anonymous:
            hints.update(hints[name]._hints_)
        cls._hints_ = hints

    def __setattr__(self, name, obj):
        if name in self._hints_:
            obj = easycast(obj, self._hints_[name])
        return super().__setattr__(name, obj)

    def __getattribute__(self, name):
        if name.endswith("_as_intptr"):
            rawname = _removesuffix(name, "_as_intptr")
            obj = super().__getattribute__(rawname)
            return cast(obj, c_void_p).value
        obj = super().__getattribute__(name)
        if type(obj) is c_char_p_no or type(obj) is c_wchar_p_no:
            if not obj:
                return None
            return obj.value
        return obj


class EasyCastUnion(Union):
    def __setattr__(self, name, obj):
        if name in self._hints_:
            obj = easycast(obj, self._hints_[name])
        return super().__setattr__(name, obj)

    def __getattribute__(self, name):
        if name.endswith("_as_intptr"):
            rawname = name.removesuffix("_as_intptr")
            obj = super().__getattribute__(rawname)
            return cast(obj, c_void_p).value
        obj = super().__getattribute__(name)
        if type(obj) is c_char_p_no or type(obj) is c_wchar_p_no:
            if not obj:
                return None
            return obj.value
        return obj


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


def easycast(obj, type_):
    for obj_type, type_hint, c_func in EASY_TYPES:
        if isinstance(obj, obj_type) and issubclass(type_, type_hint):
            if c_func is not None:
                obj = c_func(obj)
            return cast(obj, type_)
    if issubclass(type_, _CFuncPtr):
        if isinstance(type_, _CFuncPtr):
            return obj
        elif callable(obj):
            return type_(obj)
        elif obj is None:
            return type_()
    return obj


def get_type_hints(prototype, **kwargs):
    hints = _get_type_hints(prototype, localns=getattr(prototype, "__dict__", None), **kwargs)
    for name, type_ in hints.items():
        if type_ is None.__class__:
            hints[name] = None
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


def SUCCEEDED(hr):
    return hr >= 0


def FAILED(hr):
    return hr < 0


class ForeignFunction:
    def __init__(self, prototype, factory):
        hints = get_type_hints(prototype)
        restype = _patch_char_p(hints.pop("return"))
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
    def __init__(self, prototype, factory):
        hints = get_type_hints(prototype)
        restype = _patch_char_p(hints.pop("return"))
        argtypes = list(hints.values())
        types = [restype] + argtypes
        params = tuple((1, name) for name in hints.keys())
        self.hints = hints
        self.hints.update({i: v for i, v in enumerate(argtypes)})
        self.delegate = factory(prototype.__name__, types, params)

    def __call__(self, this, *args, **kwargs):
        _as_intptr = kwargs.pop("_as_intptr", False)
        cargs, ckwargs = self.make_args(args, kwargs)
        result = self.delegate(this, *cargs, **ckwargs)
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
    def factory(name, types, params):
        return WINFUNCTYPE(*types)(vtbl_index, name, params)

    def decorator(prototype):
        delegate = None

        def wrapper(*args, **kwargs):
            nonlocal delegate
            if delegate is None:
                delegate = ComMethod(prototype, factory)
            return delegate(*args, **kwargs)

        return wrapper

    return decorator



def cfunctype_pointer(prototype):
    types = list(get_type_hints(prototype).values())
    types = types[-1:] + types[:-1]
    return CFUNCTYPE(*types)


def winfunctype_pointer(prototype):
    types = list(get_type_hints(prototype).values())
    types = types[-1:] + types[:-1]
    return WINFUNCTYPE(*types)

