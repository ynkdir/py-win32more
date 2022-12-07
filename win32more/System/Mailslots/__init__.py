from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security
import win32more.System.Mailslots
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
@winfunctype('KERNEL32.dll')
def CreateMailslotA(lpName: win32more.Foundation.PSTR, nMaxMessageSize: UInt32, lReadTimeout: UInt32, lpSecurityAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head)) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateMailslotW(lpName: win32more.Foundation.PWSTR, nMaxMessageSize: UInt32, lReadTimeout: UInt32, lpSecurityAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head)) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def GetMailslotInfo(hMailslot: win32more.Foundation.HANDLE, lpMaxMessageSize: POINTER(UInt32), lpNextSize: POINTER(UInt32), lpMessageCount: POINTER(UInt32), lpReadTimeout: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetMailslotInfo(hMailslot: win32more.Foundation.HANDLE, lReadTimeout: UInt32) -> win32more.Foundation.BOOL: ...
__all__ = [
    "CreateMailslotA",
    "CreateMailslotW",
    "GetMailslotInfo",
    "SetMailslotInfo",
]
