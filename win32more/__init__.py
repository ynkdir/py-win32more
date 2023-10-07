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
from collections import defaultdict

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
    def __init__(self, value=None, own=False):
        super().__init__(value)
        self._own = own

    def __del__(self):
        if self and getattr(self, "_own", False):
            self.Release()

    @classmethod
    def __commit__(struct):
        if struct.__annotations__["extends"] == 'None':
            return

        struct._hints_ = get_hints(struct)

        # Generic class have multiple base class (Generic[], ComPtr).
        struct.__bases__ = tuple(
            struct._hints_["extends"] if t is ComPtr else t
            for t in struct.__bases__
        )


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


class EasyCastBase:
    @classmethod
    def __commit__(struct):
        # FIXME: not work for Union.
        # if hasattr(cls, "_fields_"):
        if "_fields_" in dir(struct):
            return

        hints = get_hints(struct)

        anonymous = [
            hint for hint in hints.keys()
            if re.match(r"^Anonymous\d*$", hint)
        ]
        if anonymous:
            struct._anonymous_ = anonymous

        struct._fields_ = list(hints.items())

        for hint in anonymous:
            hints.update(hints[hint]._hints_)
        struct._hints_ = hints


class EasyCastStructure(EasyCastBase, Structure):
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


class EasyCastUnion(EasyCastBase, Union):
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


def get_hints(struct, patch_return=False):
    hints = {}
    for hint, type_ in get_type_hints(struct).items():
        if type_ is None or hasattr(type_, '__done_ctypes__'):
            hints[hint] = type_
            continue

        if not patch_return or hint == 'return':
            type_ = _patch_char_p(type_)

        if isinstance(type_, BaseFuncType):
            if not hasattr(type_, '__done_ctypes__'):
                type_.__done_ctypes__ = True
                BaseFuncType.commit(type_)
            type_ = type_._fn
        elif issubclass(type_, (EasyCastStructure, EasyCastUnion, ComPtr)):
            type_.__commit__()
        hints[hint] = type_
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
        hints = get_hints(prototype, patch_return=True)
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
    def __init__(self, prototype, factory):
        hints = get_hints(prototype, patch_return=True)
        restype = hints.pop("return")
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


class BaseFuncType:
    def __init__(self, fn, kind):
        self._fn = fn
        self._kind = kind

    def __call__(self, *args, **kwargs):
        if not hasattr(self, '__done_ctypes__'):
            self.__done_ctypes__ = True
            BaseFuncType.commit(self)
        return self._fn(*args, **kwargs)

    @classmethod
    def commit(cls, instance):
        types = list(get_hints(instance._fn).values())
        types = types[-1:] + types[:-1]
        instance._fn = instance._kind(*types)


def cfunctype_pointer(prototype):
    return BaseFuncType(prototype, CFUNCTYPE)


def winfunctype_pointer(prototype):
    return BaseFuncType(prototype, WINFUNCTYPE)

class GetAttr:
    def __init__(self, mod):
        self._mod = mod
        self._obj = sys.modules[mod]

    def __call__(self, name):
        try:
            prototype = self._obj.__dict__[f'_unused_{name}']
        except KeyError:
            raise AttributeError(
                f"module '{self._mod}' has no attribute '{name}'"
            ) from None

        prottype.__done_ctypes__ = True
        if issubclass(type_, (EasyCastStructure, EasyCastUnion, ComPtr)):
            type_.__commit__()

        setattr(self._obj, name, prototype)
        delattr(self._obj, f'_unused_{name}')
        return prototype


def make_ready(mod: str) -> None:
    obj = sys.modules[mod]

    for name in dir(obj):
        prototype = getattr(obj, name)
        if (
            isinstance(prototype, type)
            and issubclass(prototype, (EasyCastStructure, EasyCastUnion, ComPtr))
            and not hasattr(prototype, '__done_ctypes__')
        ):
            setattr(obj, f'_unused_{name}', prototype)
            delattr(obj, name)

    obj.__getattr__ = GetAttr(mod)
