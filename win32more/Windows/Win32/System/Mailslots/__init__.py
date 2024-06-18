from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Mailslots
@winfunctype('KERNEL32.dll')
def CreateMailslotA(lpName: win32more.Windows.Win32.Foundation.PSTR, nMaxMessageSize: UInt32, lReadTimeout: UInt32, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateMailslotW(lpName: win32more.Windows.Win32.Foundation.PWSTR, nMaxMessageSize: UInt32, lReadTimeout: UInt32, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateMailslot = UnicodeAlias('CreateMailslotW')
@winfunctype('KERNEL32.dll')
def GetMailslotInfo(hMailslot: win32more.Windows.Win32.Foundation.HANDLE, lpMaxMessageSize: POINTER(UInt32), lpNextSize: POINTER(UInt32), lpMessageCount: POINTER(UInt32), lpReadTimeout: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetMailslotInfo(hMailslot: win32more.Windows.Win32.Foundation.HANDLE, lReadTimeout: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...


make_ready(__name__)
