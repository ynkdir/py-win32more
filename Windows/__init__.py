import types
import typing
import re
import sys
import uuid
from ctypes import c_byte, c_ubyte, c_short, c_ushort, c_int, c_uint, c_longlong, c_ulonglong, c_float, c_double, c_bool, c_wchar, c_char_p, c_wchar_p, c_void_p, Structure, Union, cdll, windll, CFUNCTYPE, WINFUNCTYPE, sizeof, POINTER, cast, pointer, Array

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
Int16 = c_short
UInt16 = c_ushort
Int32 = c_int
UInt32 = c_uint
Int64 = c_longlong
UInt64 = c_ulonglong
if sizeof(c_void_p) == sizeof(Int64):
    IntPtr = Int64
    UIntPtr = UInt64
elif sizeof(c_void_p) == sizeof(Int32):
    IntPtr = Int32
    UIntPtr = UInt32
else:
    raise NotImplementedError()
Single = c_float
Double = c_double
String = c_wchar_p
Boolean = c_bool
Void = None

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

class EasyCastStructure(Structure):
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

EASY_TYPES = [ #obj_type, type_hint, c_func
    # python objects:
    (str, (POINTER(Int16), POINTER(UInt16)), c_wchar_p),
    (int, (c_char_p, c_wchar_p), c_void_p),  # for function for consistency with struct.member assignment
    # ctypes objects:
    (c_wchar_p, (POINTER(Int16), POINTER(UInt16)), None),
    (c_wchar_p, (POINTER(POINTER(Int16)), POINTER(POINTER(UInt16))), pointer),
    (c_char_p, (c_char_p_no,), None),
    (c_wchar_p, (c_wchar_p_no,), None),
]

def easycast(obj, type_):
    for obj_type, type_hint, c_func in EASY_TYPES:
        if isinstance(obj, obj_type) and issubclass(type_, type_hint):
            if c_func is not None: obj = c_func(obj)
            return cast(obj, type_)
    return obj

class Guid(EasyCastStructure):
    _fields_ = [("Data1", UInt32),
                ("Data2", UInt16),
                ("Data3", UInt16),
                ("Data4", Byte * 8)]
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

def get_type_hints(prototype):
    hints = typing.get_type_hints(prototype, localns=getattr(prototype, '__dict__', None))
    for name, type_ in hints.items():
        if type_ is None.__class__:
            hints[name] = None
    return hints

class ForeignFunction:
    def __init__(self, prototype, factory):
        self.hints = get_type_hints(prototype)
        self.restype = _patch_char_p(self.hints.pop("return"))
        self.argtypes = list(self.hints.values())
        types = [self.restype] + self.argtypes
        params = tuple((1, name) for name in self.hints.keys())
        varnames = prototype.__code__.co_varnames
        if varnames and varnames[-1] == "__arglist":
            # Disable keyword argument for variable length arguments.
            params = None
        self.is_com = (varnames and varnames[0] == "self" and "self" not in self.hints)
        self.delegate = factory(prototype.__name__, types, params)

    def __call__(self, *args, **kwargs):
        _as_intptr = kwargs.pop("_as_intptr", False)
        if self.is_com:
            cargs, ckwargs = self.make_args(args[1:], kwargs)
            cargs.insert(0, args[0])
        else:
            cargs, ckwargs = self.make_args(args, kwargs)
        cargs, ckwargs = self.make_args(args, kwargs)
        result = self.delegate(*cargs, **ckwargs)
        if _as_intptr:
            return cast(result, c_void_p).value
        elif type(result) is c_char_p_no or type(result) is c_wchar_p_no:
            return result.value
        return result

    def make_args(self, args, kwargs):
        cargs = []
        for i, v in enumerate(args):
            if i < len(self.argtypes):
                cargs.append(easycast(v, self.argtypes[i]))
            else:
                cargs.append(v)
        ckwargs = {}
        for k, v in kwargs.items():
            if k in self.hints:
                ckwargs[k] = easycast(v, self.hints[k])
            else:
                ckwargs[k] = v
        return cargs, ckwargs

def commonfunctype(factory):
    def decorator(prototype):
        delegate = None
        def wrapper(*args, **kwargs):
            nonlocal delegate
            if delegate is None:
                delegate = ForeignFunction(prototype, factory)
            return delegate(*args, **kwargs)
        return wrapper
    return decorator

def cfunctype(library, entry_point=None):
    def factory(name, types, params):
        if entry_point is not None:
            name = entry_point
        return CFUNCTYPE(*types)((name, cdll[library]), params)
    return commonfunctype(factory)

def winfunctype(library, entry_point=None):
    def factory(name, types, params):
        if entry_point is not None:
            name = entry_point
        return WINFUNCTYPE(*types)((name, windll[library]), params)
    return commonfunctype(factory)

def commethod(vtbl_index):
    def factory(name, types, params):
        return WINFUNCTYPE(*types)(vtbl_index, name, params)
    return commonfunctype(factory)

def commonfunctype_pointer(prototype, functype):
    def press_functype_pointer():
        hints = get_type_hints(prototype)
        types = list(hints.values())
        types = types[-1:] + types[:-1]
        return functype(*types)
    return press_functype_pointer

def cfunctype_pointer(prototype):
    return commonfunctype_pointer(prototype, CFUNCTYPE)

def winfunctype_pointer(prototype):
    return commonfunctype_pointer(prototype, WINFUNCTYPE)

def press(prototype):
    if isinstance(prototype, types.FunctionType):
        # constant or function_pointer
        return prototype()
    elif issubclass(prototype, (Structure, Union)):
        return press_struct(prototype)
    elif issubclass(prototype, c_void_p):
        return press_interface(prototype)
    else:
        raise NotImplementedError()

def press_struct(prototype):
    # FIXME: not work for Union.
    #if hasattr(prototype, "_fields_"):
    if "_fields_" in dir(prototype):
        return prototype
    hints = {name: _patch_char_p(type_) for name, type_ in get_type_hints(prototype).items()}
    anonymous = [name  for name in hints.keys() if re.match(r"^Anonymous\d*$", name)]
    if anonymous:
        prototype._anonymous_ = anonymous
    for type_ in hints.values():
        if type_ is not prototype and issubclass(type_, (Structure, Union)):
            press_struct(type_)
    prototype._fields_ = list(hints.items())
    for name in anonymous:
        hints.update(hints[name]._hints_)
    prototype._hints_ = hints
    return prototype

def press_interface(prototype):
    hints = get_type_hints(prototype)
    if hints["extends"] is None:
        return prototype
    prototype.__bases__ = (hints["extends"],)
    return prototype

def make_head(module, name):
    setattr(module, f"{name}_head", getattr(module, name))
    delattr(module, name)

