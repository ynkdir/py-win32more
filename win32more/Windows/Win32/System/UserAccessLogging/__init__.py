from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.WinSock
import win32more.Windows.Win32.System.UserAccessLogging
@winfunctype('ualapi.dll')
def UalStart(Data: POINTER(win32more.Windows.Win32.System.UserAccessLogging.UAL_DATA_BLOB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ualapi.dll')
def UalStop(Data: POINTER(win32more.Windows.Win32.System.UserAccessLogging.UAL_DATA_BLOB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ualapi.dll')
def UalInstrument(Data: POINTER(win32more.Windows.Win32.System.UserAccessLogging.UAL_DATA_BLOB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ualapi.dll')
def UalRegisterProduct(wszProductName: win32more.Windows.Win32.Foundation.PWSTR, wszRoleName: win32more.Windows.Win32.Foundation.PWSTR, wszGuid: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class UAL_DATA_BLOB(Structure):
    Size: UInt32
    RoleGuid: Guid
    TenantId: Guid
    Address: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE
    UserName: Char * 260


make_ready(__name__)
