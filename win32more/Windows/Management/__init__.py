from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Management
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IMdmAlert(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.IMdmAlert'
    _iid_ = Guid('{b0fbc327-28c1-4b52-a548-c5807caf70b6}')
    @winrt_commethod(6)
    def get_Data(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Data(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Format(self) -> win32more.Windows.Management.MdmAlertDataType: ...
    @winrt_commethod(9)
    def put_Format(self, value: win32more.Windows.Management.MdmAlertDataType) -> Void: ...
    @winrt_commethod(10)
    def get_Mark(self) -> win32more.Windows.Management.MdmAlertMark: ...
    @winrt_commethod(11)
    def put_Mark(self, value: win32more.Windows.Management.MdmAlertMark) -> Void: ...
    @winrt_commethod(12)
    def get_Source(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_Source(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_Status(self) -> UInt32: ...
    @winrt_commethod(15)
    def get_Target(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def put_Target(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def get_Type(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def put_Type(self, value: WinRT_String) -> Void: ...
    Data = property(get_Data, put_Data)
    Format = property(get_Format, put_Format)
    Mark = property(get_Mark, put_Mark)
    Source = property(get_Source, put_Source)
    Status = property(get_Status, None)
    Target = property(get_Target, put_Target)
    Type = property(get_Type, put_Type)
class IMdmSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.IMdmSession'
    _iid_ = Guid('{fe89314c-8f64-4797-a9d7-9d88f86ae166}')
    @winrt_commethod(6)
    def get_Alerts(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.MdmAlert]: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_State(self) -> win32more.Windows.Management.MdmSessionState: ...
    @winrt_commethod(10)
    def AttachAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def Delete(self) -> Void: ...
    @winrt_commethod(12)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def StartWithAlertsAsync(self, alerts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Management.MdmAlert]) -> win32more.Windows.Foundation.IAsyncAction: ...
    Alerts = property(get_Alerts, None)
    ExtendedError = property(get_ExtendedError, None)
    Id = property(get_Id, None)
    State = property(get_State, None)
class IMdmSessionManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.IMdmSessionManagerStatics'
    _iid_ = Guid('{cf4ad959-f745-4b79-9b5c-de0bf8efe44b}')
    @winrt_commethod(6)
    def get_SessionIds(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def TryCreateSession(self) -> win32more.Windows.Management.MdmSession: ...
    @winrt_commethod(8)
    def DeleteSessionById(self, sessionId: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def GetSessionById(self, sessionId: WinRT_String) -> win32more.Windows.Management.MdmSession: ...
    SessionIds = property(get_SessionIds, None)
class MdmAlert(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.IMdmAlert
    _classid_ = 'Windows.Management.MdmAlert'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Management.MdmAlert: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.Management.IMdmAlert) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Windows.Management.IMdmAlert, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Format(self: win32more.Windows.Management.IMdmAlert) -> win32more.Windows.Management.MdmAlertDataType: ...
    @winrt_mixinmethod
    def put_Format(self: win32more.Windows.Management.IMdmAlert, value: win32more.Windows.Management.MdmAlertDataType) -> Void: ...
    @winrt_mixinmethod
    def get_Mark(self: win32more.Windows.Management.IMdmAlert) -> win32more.Windows.Management.MdmAlertMark: ...
    @winrt_mixinmethod
    def put_Mark(self: win32more.Windows.Management.IMdmAlert, value: win32more.Windows.Management.MdmAlertMark) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Management.IMdmAlert) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Source(self: win32more.Windows.Management.IMdmAlert, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Management.IMdmAlert) -> UInt32: ...
    @winrt_mixinmethod
    def get_Target(self: win32more.Windows.Management.IMdmAlert) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Target(self: win32more.Windows.Management.IMdmAlert, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Management.IMdmAlert) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Type(self: win32more.Windows.Management.IMdmAlert, value: WinRT_String) -> Void: ...
    Data = property(get_Data, put_Data)
    Format = property(get_Format, put_Format)
    Mark = property(get_Mark, put_Mark)
    Source = property(get_Source, put_Source)
    Status = property(get_Status, None)
    Target = property(get_Target, put_Target)
    Type = property(get_Type, put_Type)
MdmAlertDataType = Int32
MdmAlertDataType_String: MdmAlertDataType = 0
MdmAlertDataType_Base64: MdmAlertDataType = 1
MdmAlertDataType_Boolean: MdmAlertDataType = 2
MdmAlertDataType_Integer: MdmAlertDataType = 3
MdmAlertMark = Int32
MdmAlertMark_None: MdmAlertMark = 0
MdmAlertMark_Fatal: MdmAlertMark = 1
MdmAlertMark_Critical: MdmAlertMark = 2
MdmAlertMark_Warning: MdmAlertMark = 3
MdmAlertMark_Informational: MdmAlertMark = 4
class MdmSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.IMdmSession
    _classid_ = 'Windows.Management.MdmSession'
    @winrt_mixinmethod
    def get_Alerts(self: win32more.Windows.Management.IMdmSession) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Management.MdmAlert]: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Management.IMdmSession) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Management.IMdmSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Management.IMdmSession) -> win32more.Windows.Management.MdmSessionState: ...
    @winrt_mixinmethod
    def AttachAsync(self: win32more.Windows.Management.IMdmSession) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Delete(self: win32more.Windows.Management.IMdmSession) -> Void: ...
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Management.IMdmSession) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartWithAlertsAsync(self: win32more.Windows.Management.IMdmSession, alerts: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Management.MdmAlert]) -> win32more.Windows.Foundation.IAsyncAction: ...
    Alerts = property(get_Alerts, None)
    ExtendedError = property(get_ExtendedError, None)
    Id = property(get_Id, None)
    State = property(get_State, None)
class _MdmSessionManager_Meta_(ComPtr.__class__):
    pass
class MdmSessionManager(ComPtr, metaclass=_MdmSessionManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.MdmSessionManager'
    @winrt_classmethod
    def get_SessionIds(cls: win32more.Windows.Management.IMdmSessionManagerStatics) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def TryCreateSession(cls: win32more.Windows.Management.IMdmSessionManagerStatics) -> win32more.Windows.Management.MdmSession: ...
    @winrt_classmethod
    def DeleteSessionById(cls: win32more.Windows.Management.IMdmSessionManagerStatics, sessionId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetSessionById(cls: win32more.Windows.Management.IMdmSessionManagerStatics, sessionId: WinRT_String) -> win32more.Windows.Management.MdmSession: ...
    _MdmSessionManager_Meta_.SessionIds = property(get_SessionIds.__wrapped__, None)
MdmSessionState = Int32
MdmSessionState_NotStarted: MdmSessionState = 0
MdmSessionState_Starting: MdmSessionState = 1
MdmSessionState_Connecting: MdmSessionState = 2
MdmSessionState_Communicating: MdmSessionState = 3
MdmSessionState_AlertStatusAvailable: MdmSessionState = 4
MdmSessionState_Retrying: MdmSessionState = 5
MdmSessionState_Completed: MdmSessionState = 6
make_head(_module, 'IMdmAlert')
make_head(_module, 'IMdmSession')
make_head(_module, 'IMdmSessionManagerStatics')
make_head(_module, 'MdmAlert')
make_head(_module, 'MdmSession')
make_head(_module, 'MdmSessionManager')
