from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System.Update
import win32more.Windows.Win32.System.WinRT
class ISystemUpdateItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Update.ISystemUpdateItem'
    _iid_ = Guid('{779740eb-5624-519e-a8e2-09e9173b3fb7}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.System.Update.SystemUpdateItemState: ...
    @winrt_commethod(7)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Revision(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_DownloadProgress(self) -> Double: ...
    @winrt_commethod(12)
    def get_InstallProgress(self) -> Double: ...
    @winrt_commethod(13)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    Description = property(get_Description, None)
    DownloadProgress = property(get_DownloadProgress, None)
    ExtendedError = property(get_ExtendedError, None)
    Id = property(get_Id, None)
    InstallProgress = property(get_InstallProgress, None)
    Revision = property(get_Revision, None)
    State = property(get_State, None)
    Title = property(get_Title, None)
class ISystemUpdateLastErrorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Update.ISystemUpdateLastErrorInfo'
    _iid_ = Guid('{7ee887f7-8a44-5b6e-bd07-7aece4116ea9}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.System.Update.SystemUpdateManagerState: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_IsInteractive(self) -> Boolean: ...
    ExtendedError = property(get_ExtendedError, None)
    IsInteractive = property(get_IsInteractive, None)
    State = property(get_State, None)
class ISystemUpdateManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Update.ISystemUpdateManagerStatics'
    _iid_ = Guid('{b2d3fcef-2971-51be-b41a-8bd703bb701a}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_State(self) -> win32more.Windows.System.Update.SystemUpdateManagerState: ...
    @winrt_commethod(8)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_DownloadProgress(self) -> Double: ...
    @winrt_commethod(11)
    def get_InstallProgress(self) -> Double: ...
    @winrt_commethod(12)
    def get_UserActiveHoursStart(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(13)
    def get_UserActiveHoursEnd(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(14)
    def get_UserActiveHoursMax(self) -> Int32: ...
    @winrt_commethod(15)
    def TrySetUserActiveHours(self, start: win32more.Windows.Foundation.TimeSpan, end: win32more.Windows.Foundation.TimeSpan) -> Boolean: ...
    @winrt_commethod(16)
    def get_LastUpdateCheckTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(17)
    def get_LastUpdateInstallTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(18)
    def get_LastErrorInfo(self) -> win32more.Windows.System.Update.SystemUpdateLastErrorInfo: ...
    @winrt_commethod(19)
    def GetAutomaticRebootBlockIds(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(20)
    def BlockAutomaticRebootAsync(self, lockId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(21)
    def UnblockAutomaticRebootAsync(self, lockId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(22)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(23)
    def GetUpdateItems(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.Update.SystemUpdateItem]: ...
    @winrt_commethod(24)
    def get_AttentionRequiredReason(self) -> win32more.Windows.System.Update.SystemUpdateAttentionRequiredReason: ...
    @winrt_commethod(25)
    def SetFlightRing(self, flightRing: WinRT_String) -> Boolean: ...
    @winrt_commethod(26)
    def GetFlightRing(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def StartInstall(self, action: win32more.Windows.System.Update.SystemUpdateStartInstallAction) -> Void: ...
    @winrt_commethod(28)
    def RebootToCompleteInstall(self) -> Void: ...
    @winrt_commethod(29)
    def StartCancelUpdates(self) -> Void: ...
    AttentionRequiredReason = property(get_AttentionRequiredReason, None)
    DownloadProgress = property(get_DownloadProgress, None)
    ExtendedError = property(get_ExtendedError, None)
    InstallProgress = property(get_InstallProgress, None)
    LastErrorInfo = property(get_LastErrorInfo, None)
    LastUpdateCheckTime = property(get_LastUpdateCheckTime, None)
    LastUpdateInstallTime = property(get_LastUpdateInstallTime, None)
    State = property(get_State, None)
    UserActiveHoursEnd = property(get_UserActiveHoursEnd, None)
    UserActiveHoursMax = property(get_UserActiveHoursMax, None)
    UserActiveHoursStart = property(get_UserActiveHoursStart, None)
    StateChanged = event()
class SystemUpdateAttentionRequiredReason(Enum, Int32):
    None_ = 0
    NetworkRequired = 1
    InsufficientDiskSpace = 2
    InsufficientBattery = 3
    UpdateBlocked = 4
class SystemUpdateItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Update.ISystemUpdateItem
    _classid_ = 'Windows.System.Update.SystemUpdateItem'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.System.Update.ISystemUpdateItem) -> win32more.Windows.System.Update.SystemUpdateItemState: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.System.Update.ISystemUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.System.Update.ISystemUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.System.Update.ISystemUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Revision(self: win32more.Windows.System.Update.ISystemUpdateItem) -> UInt32: ...
    @winrt_mixinmethod
    def get_DownloadProgress(self: win32more.Windows.System.Update.ISystemUpdateItem) -> Double: ...
    @winrt_mixinmethod
    def get_InstallProgress(self: win32more.Windows.System.Update.ISystemUpdateItem) -> Double: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.System.Update.ISystemUpdateItem) -> win32more.Windows.Foundation.HResult: ...
    Description = property(get_Description, None)
    DownloadProgress = property(get_DownloadProgress, None)
    ExtendedError = property(get_ExtendedError, None)
    Id = property(get_Id, None)
    InstallProgress = property(get_InstallProgress, None)
    Revision = property(get_Revision, None)
    State = property(get_State, None)
    Title = property(get_Title, None)
class SystemUpdateItemState(Enum, Int32):
    NotStarted = 0
    Initializing = 1
    Preparing = 2
    Calculating = 3
    Downloading = 4
    Installing = 5
    Completed = 6
    RebootRequired = 7
    Error = 8
class SystemUpdateLastErrorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Update.ISystemUpdateLastErrorInfo
    _classid_ = 'Windows.System.Update.SystemUpdateLastErrorInfo'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.System.Update.ISystemUpdateLastErrorInfo) -> win32more.Windows.System.Update.SystemUpdateManagerState: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.System.Update.ISystemUpdateLastErrorInfo) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_IsInteractive(self: win32more.Windows.System.Update.ISystemUpdateLastErrorInfo) -> Boolean: ...
    ExtendedError = property(get_ExtendedError, None)
    IsInteractive = property(get_IsInteractive, None)
    State = property(get_State, None)
class _SystemUpdateManager_Meta_(ComPtr.__class__):
    pass
class SystemUpdateManager(ComPtr, metaclass=_SystemUpdateManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Update.SystemUpdateManager'
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def get_State(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> win32more.Windows.System.Update.SystemUpdateManagerState: ...
    @winrt_classmethod
    def add_StateChanged(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_StateChanged(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_DownloadProgress(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> Double: ...
    @winrt_classmethod
    def get_InstallProgress(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> Double: ...
    @winrt_classmethod
    def get_UserActiveHoursStart(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_classmethod
    def get_UserActiveHoursEnd(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_classmethod
    def get_UserActiveHoursMax(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> Int32: ...
    @winrt_classmethod
    def TrySetUserActiveHours(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics, start: win32more.Windows.Foundation.TimeSpan, end: win32more.Windows.Foundation.TimeSpan) -> Boolean: ...
    @winrt_classmethod
    def get_LastUpdateCheckTime(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_classmethod
    def get_LastUpdateInstallTime(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_classmethod
    def get_LastErrorInfo(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> win32more.Windows.System.Update.SystemUpdateLastErrorInfo: ...
    @winrt_classmethod
    def GetAutomaticRebootBlockIds(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def BlockAutomaticRebootAsync(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics, lockId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def UnblockAutomaticRebootAsync(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics, lockId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_ExtendedError(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> win32more.Windows.Foundation.HResult: ...
    @winrt_classmethod
    def GetUpdateItems(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.System.Update.SystemUpdateItem]: ...
    @winrt_classmethod
    def get_AttentionRequiredReason(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> win32more.Windows.System.Update.SystemUpdateAttentionRequiredReason: ...
    @winrt_classmethod
    def SetFlightRing(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics, flightRing: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def GetFlightRing(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> WinRT_String: ...
    @winrt_classmethod
    def StartInstall(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics, action: win32more.Windows.System.Update.SystemUpdateStartInstallAction) -> Void: ...
    @winrt_classmethod
    def RebootToCompleteInstall(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> Void: ...
    @winrt_classmethod
    def StartCancelUpdates(cls: win32more.Windows.System.Update.ISystemUpdateManagerStatics) -> Void: ...
    _SystemUpdateManager_Meta_.AttentionRequiredReason = property(get_AttentionRequiredReason, None)
    _SystemUpdateManager_Meta_.DownloadProgress = property(get_DownloadProgress, None)
    _SystemUpdateManager_Meta_.ExtendedError = property(get_ExtendedError, None)
    _SystemUpdateManager_Meta_.InstallProgress = property(get_InstallProgress, None)
    _SystemUpdateManager_Meta_.LastErrorInfo = property(get_LastErrorInfo, None)
    _SystemUpdateManager_Meta_.LastUpdateCheckTime = property(get_LastUpdateCheckTime, None)
    _SystemUpdateManager_Meta_.LastUpdateInstallTime = property(get_LastUpdateInstallTime, None)
    _SystemUpdateManager_Meta_.State = property(get_State, None)
    _SystemUpdateManager_Meta_.UserActiveHoursEnd = property(get_UserActiveHoursEnd, None)
    _SystemUpdateManager_Meta_.UserActiveHoursMax = property(get_UserActiveHoursMax, None)
    _SystemUpdateManager_Meta_.UserActiveHoursStart = property(get_UserActiveHoursStart, None)
class SystemUpdateManagerState(Enum, Int32):
    Idle = 0
    Detecting = 1
    ReadyToDownload = 2
    Downloading = 3
    ReadyToInstall = 4
    Installing = 5
    RebootRequired = 6
    ReadyToFinalize = 7
    Finalizing = 8
    Completed = 9
    AttentionRequired = 10
    Error = 11
class SystemUpdateStartInstallAction(Enum, Int32):
    UpToReboot = 0
    AllowReboot = 1


make_ready(__name__)
