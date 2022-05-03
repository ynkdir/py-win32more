from ctypes import *
from ctypes.wintypes import *
import uuid

# to avoid auto conversion to str
class c_char_p_no(c_char_p):
    pass

class c_wchar_p_no(c_wchar_p):
    pass

Byte = c_ubyte
SByte = c_byte
Char = c_wchar
Int16 = c_short
UInt16 = c_ushort
Int32 = c_int
UInt32 = c_uint
Int64 = c_longlong
UInt64 = c_ulonglong
IntPtr = c_longlong
UIntPtr = c_ulonglong
Single = c_float
Double = c_double
String = c_wchar_p_no
Boolean = c_bool
Void = None

class Guid(Structure):
    _fields_ = [("Data1", UInt32),
                ("Data2", UInt16),
                ("Data3", UInt16),
                ("Data4", Byte * 8)]

    def __init__(self, val=None):
        if isinstance(val, self.__class__):
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

    def __str__(self):
        return f"{self.Data1:08x}-{self.Data2:04x}-{self.Data3:04x}-{self.Data4[0]:02x}{self.Data4[1]:02x}-{self.Data4[2]:02x}{self.Data4[3]:02x}{self.Data4[4]:02x}{self.Data4[5]:02x}{self.Data4[6]:02x}{self.Data4[7]:02x}"

def COMMETHOD(f):
    def wrap(*args, **kwargs):
        return f(*args, **kwargs)
    return wrap

def SUCCEEDED(hr):
    return hr >= 0

def FAILED(hr):
    return hr < 0

