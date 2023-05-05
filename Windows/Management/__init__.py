from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Management
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.IMdmAlert'
    _iid_ = Guid('{b0fbc327-28c1-4b52-a548-c5807caf70b6}')
    @winrt_commethod(6)
    def get_Data(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Data(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Format(self) -> Windows.Management.MdmAlertDataType: ...
    @winrt_commethod(9)
    def put_Format(self, value: Windows.Management.MdmAlertDataType) -> Void: ...
    @winrt_commethod(10)
    def get_Mark(self) -> Windows.Management.MdmAlertMark: ...
    @winrt_commethod(11)
    def put_Mark(self, value: Windows.Management.MdmAlertMark) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.IMdmSession'
    _iid_ = Guid('{fe89314c-8f64-4797-a9d7-9d88f86ae166}')
    @winrt_commethod(6)
    def get_Alerts(self) -> Windows.Foundation.Collections.IVectorView[Windows.Management.MdmAlert]: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_State(self) -> Windows.Management.MdmSessionState: ...
    @winrt_commethod(10)
    def AttachAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def Delete(self) -> Void: ...
    @winrt_commethod(12)
    def StartAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def StartWithAlertsAsync(self, alerts: Windows.Foundation.Collections.IIterable[Windows.Management.MdmAlert]) -> Windows.Foundation.IAsyncAction: ...
    Alerts = property(get_Alerts, None)
    ExtendedError = property(get_ExtendedError, None)
    Id = property(get_Id, None)
    State = property(get_State, None)
class IMdmSessionManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.IMdmSessionManagerStatics'
    _iid_ = Guid('{cf4ad959-f745-4b79-9b5c-de0bf8efe44b}')
    @winrt_commethod(6)
    def get_SessionIds(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def TryCreateSession(self) -> Windows.Management.MdmSession: ...
    @winrt_commethod(8)
    def DeleteSessionById(self, sessionId: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def GetSessionById(self, sessionId: WinRT_String) -> Windows.Management.MdmSession: ...
    SessionIds = property(get_SessionIds, None)
class MdmAlert(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Management.IMdmAlert
    _classid_ = 'Windows.Management.MdmAlert'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Management.MdmAlert: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.Management.IMdmAlert) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Data(self: Windows.Management.IMdmAlert, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Format(self: Windows.Management.IMdmAlert) -> Windows.Management.MdmAlertDataType: ...
    @winrt_mixinmethod
    def put_Format(self: Windows.Management.IMdmAlert, value: Windows.Management.MdmAlertDataType) -> Void: ...
    @winrt_mixinmethod
    def get_Mark(self: Windows.Management.IMdmAlert) -> Windows.Management.MdmAlertMark: ...
    @winrt_mixinmethod
    def put_Mark(self: Windows.Management.IMdmAlert, value: Windows.Management.MdmAlertMark) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.Management.IMdmAlert) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Source(self: Windows.Management.IMdmAlert, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Management.IMdmAlert) -> UInt32: ...
    @winrt_mixinmethod
    def get_Target(self: Windows.Management.IMdmAlert) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Target(self: Windows.Management.IMdmAlert, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.Management.IMdmAlert) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Type(self: Windows.Management.IMdmAlert, value: WinRT_String) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Management.IMdmSession
    _classid_ = 'Windows.Management.MdmSession'
    @winrt_mixinmethod
    def get_Alerts(self: Windows.Management.IMdmSession) -> Windows.Foundation.Collections.IVectorView[Windows.Management.MdmAlert]: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Management.IMdmSession) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.Management.IMdmSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Management.IMdmSession) -> Windows.Management.MdmSessionState: ...
    @winrt_mixinmethod
    def AttachAsync(self: Windows.Management.IMdmSession) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Delete(self: Windows.Management.IMdmSession) -> Void: ...
    @winrt_mixinmethod
    def StartAsync(self: Windows.Management.IMdmSession) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StartWithAlertsAsync(self: Windows.Management.IMdmSession, alerts: Windows.Foundation.Collections.IIterable[Windows.Management.MdmAlert]) -> Windows.Foundation.IAsyncAction: ...
    Alerts = property(get_Alerts, None)
    ExtendedError = property(get_ExtendedError, None)
    Id = property(get_Id, None)
    State = property(get_State, None)
class MdmSessionManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.MdmSessionManager'
    @winrt_classmethod
    def get_SessionIds(cls: Windows.Management.IMdmSessionManagerStatics) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def TryCreateSession(cls: Windows.Management.IMdmSessionManagerStatics) -> Windows.Management.MdmSession: ...
    @winrt_classmethod
    def DeleteSessionById(cls: Windows.Management.IMdmSessionManagerStatics, sessionId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetSessionById(cls: Windows.Management.IMdmSessionManagerStatics, sessionId: WinRT_String) -> Windows.Management.MdmSession: ...
    SessionIds = property(get_SessionIds, None)
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
