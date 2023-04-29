from ctypes import c_wchar, sizeof, wstring_at

from Windows import IntPtr
from Windows.Win32.System.Environment import FreeEnvironmentStringsW, GetEnvironmentStringsW


# Unsafe case for c_wchar_p to python str auto-conversion.
# GetEnvironmentStringsW() returns NUL terminated list of NUL terminated string.
# name1=value1\0name2=value2\0\0
# Return value should be freed by FreeEnvironmentStringsW().
def GetEnvironmentStrings():
    ptr: IntPtr = GetEnvironmentStringsW(_as_intptr=True)
    p = ptr
    while (s := wstring_at(p)) != "":
        yield s.split("=", maxsplit=1)
        p += (len(s) + 1) * sizeof(c_wchar)
    FreeEnvironmentStringsW(ptr)


for name, value in GetEnvironmentStrings():
    print(f"{name} = {value}")
