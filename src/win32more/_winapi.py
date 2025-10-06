import sys
from ctypes import POINTER, c_byte, c_uint32, c_void_p, c_wchar_p

if sys.platform == "cygwin":
    from ctypes import CFUNCTYPE as WINFUNCTYPE
    from ctypes import cdll as windll
else:
    from ctypes import WINFUNCTYPE, windll

# Windows.Win32.Foundation

GetLastError = WINFUNCTYPE(c_uint32)(("GetLastError", windll["kernel32.dll"]))
LocalFree = WINFUNCTYPE(c_void_p, c_void_p)(("LocalFree", windll["kernel32.dll"]))

# Windows.Win32.System.Diagnostics.Debug

FORMAT_MESSAGE_ALLOCATE_BUFFER = 256
FORMAT_MESSAGE_FROM_SYSTEM = 4096
FORMAT_MESSAGE_IGNORE_INSERTS = 512

FormatMessageW = WINFUNCTYPE(
    c_uint32, c_uint32, c_void_p, c_uint32, c_uint32, c_wchar_p, c_uint32, POINTER(POINTER(c_byte))
)(("FormatMessageW", windll["kernel32.dll"]))

# Windows.Win32.System.SystemServices

LANG_NEUTRAL = 0
SUBLANG_NEUTRAL = 0


def MAKELANGID(p, s):
    return (s << 10) | p
