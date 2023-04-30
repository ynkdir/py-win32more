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
import Windows.System.Update
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ISystemUpdateItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('779740eb-5624-519e-a8-e2-09-e9-17-3b-3f-b7')
    @winrt_commethod(6)
    def get_State(self) -> Windows.System.Update.SystemUpdateItemState: ...
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
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    State = property(get_State, None)
    Title = property(get_Title, None)
    Description = property(get_Description, None)
    Id = property(get_Id, None)
    Revision = property(get_Revision, None)
    DownloadProgress = property(get_DownloadProgress, None)
    InstallProgress = property(get_InstallProgress, None)
    ExtendedError = property(get_ExtendedError, None)
class ISystemUpdateLastErrorInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7ee887f7-8a44-5b6e-bd-07-7a-ec-e4-11-6e-a9')
    @winrt_commethod(6)
    def get_State(self) -> Windows.System.Update.SystemUpdateManagerState: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_IsInteractive(self) -> Boolean: ...
    State = property(get_State, None)
    ExtendedError = property(get_ExtendedError, None)
    IsInteractive = property(get_IsInteractive, None)
class ISystemUpdateManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b2d3fcef-2971-51be-b4-1a-8b-d7-03-bb-70-1a')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_State(self) -> Windows.System.Update.SystemUpdateManagerState: ...
    @winrt_commethod(8)
    def add_StateChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_StateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_DownloadProgress(self) -> Double: ...
    @winrt_commethod(11)
    def get_InstallProgress(self) -> Double: ...
    @winrt_commethod(12)
    def get_UserActiveHoursStart(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(13)
    def get_UserActiveHoursEnd(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(14)
    def get_UserActiveHoursMax(self) -> Int32: ...
    @winrt_commethod(15)
    def TrySetUserActiveHours(self, start: Windows.Foundation.TimeSpan, end: Windows.Foundation.TimeSpan) -> Boolean: ...
    @winrt_commethod(16)
    def get_LastUpdateCheckTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(17)
    def get_LastUpdateInstallTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(18)
    def get_LastErrorInfo(self) -> Windows.System.Update.SystemUpdateLastErrorInfo: ...
    @winrt_commethod(19)
    def GetAutomaticRebootBlockIds(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(20)
    def BlockAutomaticRebootAsync(self, lockId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(21)
    def UnblockAutomaticRebootAsync(self, lockId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(22)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(23)
    def GetUpdateItems(self) -> Windows.Foundation.Collections.IVectorView[Windows.System.Update.SystemUpdateItem]: ...
    @winrt_commethod(24)
    def get_AttentionRequiredReason(self) -> Windows.System.Update.SystemUpdateAttentionRequiredReason: ...
    @winrt_commethod(25)
    def SetFlightRing(self, flightRing: WinRT_String) -> Boolean: ...
    @winrt_commethod(26)
    def GetFlightRing(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def StartInstall(self, action: Windows.System.Update.SystemUpdateStartInstallAction) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Update.SystemUpdateItem'
    @winrt_mixinmethod
    def get_State(self: Windows.System.Update.ISystemUpdateItem) -> Windows.System.Update.SystemUpdateItemState: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.System.Update.ISystemUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.System.Update.ISystemUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.System.Update.ISystemUpdateItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Revision(self: Windows.System.Update.ISystemUpdateItem) -> UInt32: ...
    @winrt_mixinmethod
    def get_DownloadProgress(self: Windows.System.Update.ISystemUpdateItem) -> Double: ...
    @winrt_mixinmethod
    def get_InstallProgress(self: Windows.System.Update.ISystemUpdateItem) -> Double: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.System.Update.ISystemUpdateItem) -> Windows.Foundation.HResult: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Update.SystemUpdateLastErrorInfo'
    @winrt_mixinmethod
    def get_State(self: Windows.System.Update.ISystemUpdateLastErrorInfo) -> Windows.System.Update.SystemUpdateManagerState: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.System.Update.ISystemUpdateLastErrorInfo) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_IsInteractive(self: Windows.System.Update.ISystemUpdateLastErrorInfo) -> Boolean: ...
    State = property(get_State, None)
    ExtendedError = property(get_ExtendedError, None)
    IsInteractive = property(get_IsInteractive, None)
class SystemUpdateManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Update.SystemUpdateManager'
    @winrt_classmethod
    def IsSupported(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def get_State(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Windows.System.Update.SystemUpdateManagerState: ...
    @winrt_classmethod
    def add_StateChanged(cls: Windows.System.Update.ISystemUpdateManagerStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_StateChanged(cls: Windows.System.Update.ISystemUpdateManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_DownloadProgress(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Double: ...
    @winrt_classmethod
    def get_InstallProgress(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Double: ...
    @winrt_classmethod
    def get_UserActiveHoursStart(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Windows.Foundation.TimeSpan: ...
    @winrt_classmethod
    def get_UserActiveHoursEnd(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Windows.Foundation.TimeSpan: ...
    @winrt_classmethod
    def get_UserActiveHoursMax(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Int32: ...
    @winrt_classmethod
    def TrySetUserActiveHours(cls: Windows.System.Update.ISystemUpdateManagerStatics, start: Windows.Foundation.TimeSpan, end: Windows.Foundation.TimeSpan) -> Boolean: ...
    @winrt_classmethod
    def get_LastUpdateCheckTime(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Windows.Foundation.DateTime: ...
    @winrt_classmethod
    def get_LastUpdateInstallTime(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Windows.Foundation.DateTime: ...
    @winrt_classmethod
    def get_LastErrorInfo(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Windows.System.Update.SystemUpdateLastErrorInfo: ...
    @winrt_classmethod
    def GetAutomaticRebootBlockIds(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def BlockAutomaticRebootAsync(cls: Windows.System.Update.ISystemUpdateManagerStatics, lockId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def UnblockAutomaticRebootAsync(cls: Windows.System.Update.ISystemUpdateManagerStatics, lockId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_ExtendedError(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Windows.Foundation.HResult: ...
    @winrt_classmethod
    def GetUpdateItems(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Windows.Foundation.Collections.IVectorView[Windows.System.Update.SystemUpdateItem]: ...
    @winrt_classmethod
    def get_AttentionRequiredReason(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Windows.System.Update.SystemUpdateAttentionRequiredReason: ...
    @winrt_classmethod
    def SetFlightRing(cls: Windows.System.Update.ISystemUpdateManagerStatics, flightRing: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def GetFlightRing(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> WinRT_String: ...
    @winrt_classmethod
    def StartInstall(cls: Windows.System.Update.ISystemUpdateManagerStatics, action: Windows.System.Update.SystemUpdateStartInstallAction) -> Void: ...
    @winrt_classmethod
    def RebootToCompleteInstall(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Void: ...
    @winrt_classmethod
    def StartCancelUpdates(cls: Windows.System.Update.ISystemUpdateManagerStatics) -> Void: ...
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
make_head(_module, 'ISystemUpdateItem')
make_head(_module, 'ISystemUpdateLastErrorInfo')
make_head(_module, 'ISystemUpdateManagerStatics')
make_head(_module, 'SystemUpdateItem')
make_head(_module, 'SystemUpdateLastErrorInfo')
make_head(_module, 'SystemUpdateManager')
