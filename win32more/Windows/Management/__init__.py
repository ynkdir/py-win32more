from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Management
import win32more.Windows.Win32.System.WinRT
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
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Management.MdmAlert.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
class MdmAlertDataType(Enum, Int32):
    String = 0
    Base64 = 1
    Boolean = 2
    Integer = 3
class MdmAlertMark(Enum, Int32):
    None_ = 0
    Fatal = 1
    Critical = 2
    Warning = 3
    Informational = 4
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
    _MdmSessionManager_Meta_.SessionIds = property(get_SessionIds, None)
class MdmSessionState(Enum, Int32):
    NotStarted = 0
    Starting = 1
    Connecting = 2
    Communicating = 3
    AlertStatusAvailable = 4
    Retrying = 5
    Completed = 6


make_ready(__name__)
