import sys
import uuid
from ctypes import (
    POINTER,
    Structure,
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
)

if sys.platform == "cygwin":
    from ctypes import CFUNCTYPE as WINFUNCTYPE
    from ctypes import cdll as windll
else:
    from ctypes import WINFUNCTYPE, windll

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


class Guid(Structure):
    _fields_ = [
        ("Data1", UInt32),
        ("Data2", UInt16),
        ("Data3", UInt16),
        ("Data4", Byte * 8),
    ]

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


def MAKELANGID(p, s):
    return (s << 10) | p


# Windows.Win32.Foundation

BSTR = String
BSTR_AS_VOIDPTR = VoidPtr
HLOCAL = VoidPtr
HRESULT = Int32
PWSTR = String
WIN32_ERROR = UInt32

S_OK = 0
E_FAIL = -2147467259
E_NOINTERFACE = -2147467262

GetLastError = WINFUNCTYPE(WIN32_ERROR)(("GetLastError", windll["kernel32.dll"]))
LocalFree = WINFUNCTYPE(HLOCAL, HLOCAL)(("LocalFree", windll["kernel32.dll"]))
SysAllocString = WINFUNCTYPE(BSTR_AS_VOIDPTR, PWSTR)(("SysAllocString", windll["oleaut32.dll"]))
SysFreeString = WINFUNCTYPE(None, BSTR_AS_VOIDPTR)(("SysFreeString", windll["oleaut32.dll"]))
SysStringLen = WINFUNCTYPE(UInt32, BSTR_AS_VOIDPTR)(("SysStringLen", windll["oleaut32.dll"]))

# Windows.Win32.System.Com

IErrorInfo = c_void_p

CoTaskMemAlloc = WINFUNCTYPE(VoidPtr, UIntPtr)(("CoTaskMemAlloc", windll["ole32.dll"]))
CoTaskMemFree = WINFUNCTYPE(None, VoidPtr)(("CoTaskMemFree", windll["ole32.dll"]))
SetErrorInfo = WINFUNCTYPE(HRESULT, UInt32, IErrorInfo)(("SetErrorInfo", windll["oleaut32.dll"]))
GetErrorInfo = WINFUNCTYPE(HRESULT, UInt32, POINTER(IErrorInfo))(("GetErrorInfo", windll["oleaut32.dll"]))

# Windows.Win32.System.Ole

ICreateErrorInfo = c_void_p

CreateErrorInfo = WINFUNCTYPE(HRESULT, POINTER(ICreateErrorInfo))(("CreateErrorInfo", windll["oleaut32.dll"]))

# Windows.Win32.System.WinRT

BaseTrust = 0

TrustLevel = Int32
HSTRING = VoidPtr
IActivationFactory = VoidPtr

PFNGETACTIVATIONFACTORY = WINFUNCTYPE(HRESULT, HSTRING, POINTER(IActivationFactory))

RoGetActivationFactory = WINFUNCTYPE(HRESULT, HSTRING, POINTER(Guid), POINTER(c_void_p))(
    ("RoGetActivationFactory", windll["api-ms-win-core-winrt-l1-1-0.dll"])
)
RoOriginateError = WINFUNCTYPE(Boolean, HRESULT, HSTRING)(
    ("RoOriginateError", windll["api-ms-win-core-winrt-error-l1-1-0.dll"])
)
WindowsCreateString = WINFUNCTYPE(HRESULT, PWSTR, UInt32, POINTER(HSTRING))(
    ("WindowsCreateString", windll["api-ms-win-core-winrt-string-l1-1-0.dll"])
)
WindowsDeleteString = WINFUNCTYPE(HRESULT, HSTRING)(
    ("WindowsDeleteString", windll["api-ms-win-core-winrt-string-l1-1-0.dll"])
)
WindowsGetStringRawBuffer = WINFUNCTYPE(PWSTR, HSTRING, POINTER(UInt32))(
    ("WindowsGetStringRawBuffer", windll["api-ms-win-core-winrt-string-l1-1-0.dll"])
)


# Windows.Win32.System.Diagnostics.Debug

FORMAT_MESSAGE_OPTIONS = UInt32

FORMAT_MESSAGE_ALLOCATE_BUFFER = 256
FORMAT_MESSAGE_FROM_SYSTEM = 4096
FORMAT_MESSAGE_IGNORE_INSERTS = 512

FormatMessageW = WINFUNCTYPE(
    UInt32, FORMAT_MESSAGE_OPTIONS, VoidPtr, UInt32, UInt32, PWSTR, UInt32, POINTER(POINTER(SByte))
)(("FormatMessageW", windll["kernel32.dll"]))

# Windows.Win32.System.SystemServices

LANG_NEUTRAL = 0
SUBLANG_NEUTRAL = 0
