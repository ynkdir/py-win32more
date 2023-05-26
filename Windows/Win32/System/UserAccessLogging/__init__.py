from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Networking.WinSock
import Windows.Win32.System.UserAccessLogging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('ualapi.dll')
def UalStart(Data: POINTER(Windows.Win32.System.UserAccessLogging.UAL_DATA_BLOB_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ualapi.dll')
def UalStop(Data: POINTER(Windows.Win32.System.UserAccessLogging.UAL_DATA_BLOB_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ualapi.dll')
def UalInstrument(Data: POINTER(Windows.Win32.System.UserAccessLogging.UAL_DATA_BLOB_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ualapi.dll')
def UalRegisterProduct(wszProductName: Windows.Win32.Foundation.PWSTR, wszRoleName: Windows.Win32.Foundation.PWSTR, wszGuid: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class UAL_DATA_BLOB(EasyCastStructure):
    Size: UInt32
    RoleGuid: Guid
    TenantId: Guid
    Address: Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE
    UserName: Char * 260
make_head(_module, 'UAL_DATA_BLOB')
