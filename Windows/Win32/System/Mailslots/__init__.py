from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.System.Mailslots
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
@winfunctype('KERNEL32.dll')
def CreateMailslotA(lpName: Windows.Win32.Foundation.PSTR, nMaxMessageSize: UInt32, lReadTimeout: UInt32, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateMailslotW(lpName: Windows.Win32.Foundation.PWSTR, nMaxMessageSize: UInt32, lReadTimeout: UInt32, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetMailslotInfo(hMailslot: Windows.Win32.Foundation.HANDLE, lpMaxMessageSize: POINTER(UInt32), lpNextSize: POINTER(UInt32), lpMessageCount: POINTER(UInt32), lpReadTimeout: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetMailslotInfo(hMailslot: Windows.Win32.Foundation.HANDLE, lReadTimeout: UInt32) -> Windows.Win32.Foundation.BOOL: ...
__all__ = [
    "CreateMailslotA",
    "CreateMailslotW",
    "GetMailslotInfo",
    "SetMailslotInfo",
]
_arch_optional = [
]