from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System.Update
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
    State = property(get_State, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    Id = property(get_Id, None)
    Revision = property(get_Revision, None)
    DownloadProgress = property(get_DownloadProgress, None)
    InstallProgress = property(get_InstallProgress, None)
    ExtendedError = property(get_ExtendedError, None)
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
    State = property(get_State, None)
    ExtendedError = property(get_ExtendedError, None)
    IsInteractive = property(get_IsInteractive, None)
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
    State = property(get_State, None)
    DownloadProgress = property(get_DownloadProgress, None)
    InstallProgress = property(get_InstallProgress, None)
    UserActiveHoursStart = property(get_UserActiveHoursStart, None)
    UserActiveHoursEnd = property(get_UserActiveHoursEnd, None)
    UserActiveHoursMax = property(get_UserActiveHoursMax, None)
    LastUpdateCheckTime = property(get_LastUpdateCheckTime, None)
    LastUpdateInstallTime = property(get_LastUpdateInstallTime, None)
    LastErrorInfo = property(get_LastErrorInfo, None)
    ExtendedError = property(get_ExtendedError, None)
    AttentionRequiredReason = property(get_AttentionRequiredReason, None)
SystemUpdateAttentionRequiredReason = Int32
SystemUpdateAttentionRequiredReason_None: SystemUpdateAttentionRequiredReason = 0
SystemUpdateAttentionRequiredReason_NetworkRequired: SystemUpdateAttentionRequiredReason = 1
SystemUpdateAttentionRequiredReason_InsufficientDiskSpace: SystemUpdateAttentionRequiredReason = 2
SystemUpdateAttentionRequiredReason_InsufficientBattery: SystemUpdateAttentionRequiredReason = 3
SystemUpdateAttentionRequiredReason_UpdateBlocked: SystemUpdateAttentionRequiredReason = 4
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
    State = property(get_State, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    Id = property(get_Id, None)
    Revision = property(get_Revision, None)
    DownloadProgress = property(get_DownloadProgress, None)
    InstallProgress = property(get_InstallProgress, None)
    ExtendedError = property(get_ExtendedError, None)
SystemUpdateItemState = Int32
SystemUpdateItemState_NotStarted: SystemUpdateItemState = 0
SystemUpdateItemState_Initializing: SystemUpdateItemState = 1
SystemUpdateItemState_Preparing: SystemUpdateItemState = 2
SystemUpdateItemState_Calculating: SystemUpdateItemState = 3
SystemUpdateItemState_Downloading: SystemUpdateItemState = 4
SystemUpdateItemState_Installing: SystemUpdateItemState = 5
SystemUpdateItemState_Completed: SystemUpdateItemState = 6
SystemUpdateItemState_RebootRequired: SystemUpdateItemState = 7
SystemUpdateItemState_Error: SystemUpdateItemState = 8
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
    State = property(get_State, None)
    ExtendedError = property(get_ExtendedError, None)
    IsInteractive = property(get_IsInteractive, None)
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
    _SystemUpdateManager_Meta_.State = property(get_State.__wrapped__, None)
    _SystemUpdateManager_Meta_.DownloadProgress = property(get_DownloadProgress.__wrapped__, None)
    _SystemUpdateManager_Meta_.InstallProgress = property(get_InstallProgress.__wrapped__, None)
    _SystemUpdateManager_Meta_.UserActiveHoursStart = property(get_UserActiveHoursStart.__wrapped__, None)
    _SystemUpdateManager_Meta_.UserActiveHoursEnd = property(get_UserActiveHoursEnd.__wrapped__, None)
    _SystemUpdateManager_Meta_.UserActiveHoursMax = property(get_UserActiveHoursMax.__wrapped__, None)
    _SystemUpdateManager_Meta_.LastUpdateCheckTime = property(get_LastUpdateCheckTime.__wrapped__, None)
    _SystemUpdateManager_Meta_.LastUpdateInstallTime = property(get_LastUpdateInstallTime.__wrapped__, None)
    _SystemUpdateManager_Meta_.LastErrorInfo = property(get_LastErrorInfo.__wrapped__, None)
    _SystemUpdateManager_Meta_.ExtendedError = property(get_ExtendedError.__wrapped__, None)
    _SystemUpdateManager_Meta_.AttentionRequiredReason = property(get_AttentionRequiredReason.__wrapped__, None)
SystemUpdateManagerState = Int32
SystemUpdateManagerState_Idle: SystemUpdateManagerState = 0
SystemUpdateManagerState_Detecting: SystemUpdateManagerState = 1
SystemUpdateManagerState_ReadyToDownload: SystemUpdateManagerState = 2
SystemUpdateManagerState_Downloading: SystemUpdateManagerState = 3
SystemUpdateManagerState_ReadyToInstall: SystemUpdateManagerState = 4
SystemUpdateManagerState_Installing: SystemUpdateManagerState = 5
SystemUpdateManagerState_RebootRequired: SystemUpdateManagerState = 6
SystemUpdateManagerState_ReadyToFinalize: SystemUpdateManagerState = 7
SystemUpdateManagerState_Finalizing: SystemUpdateManagerState = 8
SystemUpdateManagerState_Completed: SystemUpdateManagerState = 9
SystemUpdateManagerState_AttentionRequired: SystemUpdateManagerState = 10
SystemUpdateManagerState_Error: SystemUpdateManagerState = 11
SystemUpdateStartInstallAction = Int32
SystemUpdateStartInstallAction_UpToReboot: SystemUpdateStartInstallAction = 0
SystemUpdateStartInstallAction_AllowReboot: SystemUpdateStartInstallAction = 1
make_ready(__name__)
