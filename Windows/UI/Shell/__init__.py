from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.Core
import Windows.Foundation
import Windows.UI
import Windows.UI.Shell
import Windows.UI.StartScreen
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AdaptiveCardBuilder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.AdaptiveCardBuilder'
    @winrt_classmethod
    def CreateAdaptiveCardFromJson(cls: Windows.UI.Shell.IAdaptiveCardBuilderStatics, value: WinRT_String) -> Windows.UI.Shell.IAdaptiveCard: ...
class FocusSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Shell.IFocusSession
    _classid_ = 'Windows.UI.Shell.FocusSession'
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Shell.IFocusSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def End(self: Windows.UI.Shell.IFocusSession) -> Void: ...
    Id = property(get_Id, None)
class _FocusSessionManager_Meta_(ComPtr.__class__):
    pass
class FocusSessionManager(ComPtr, metaclass=_FocusSessionManager_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Shell.IFocusSessionManager
    _classid_ = 'Windows.UI.Shell.FocusSessionManager'
    @winrt_mixinmethod
    def get_IsFocusActive(self: Windows.UI.Shell.IFocusSessionManager) -> Boolean: ...
    @winrt_mixinmethod
    def GetSession(self: Windows.UI.Shell.IFocusSessionManager, id: WinRT_String) -> Windows.UI.Shell.FocusSession: ...
    @winrt_mixinmethod
    def TryStartFocusSession(self: Windows.UI.Shell.IFocusSessionManager) -> Windows.UI.Shell.FocusSession: ...
    @winrt_mixinmethod
    def TryStartFocusSession2(self: Windows.UI.Shell.IFocusSessionManager, endTime: Windows.Foundation.DateTime) -> Windows.UI.Shell.FocusSession: ...
    @winrt_mixinmethod
    def DeactivateFocus(self: Windows.UI.Shell.IFocusSessionManager) -> Void: ...
    @winrt_mixinmethod
    def add_IsFocusActiveChanged(self: Windows.UI.Shell.IFocusSessionManager, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Shell.FocusSessionManager, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsFocusActiveChanged(self: Windows.UI.Shell.IFocusSessionManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.UI.Shell.IFocusSessionManagerStatics) -> Windows.UI.Shell.FocusSessionManager: ...
    @winrt_classmethod
    def get_IsSupported(cls: Windows.UI.Shell.IFocusSessionManagerStatics) -> Boolean: ...
    IsFocusActive = property(get_IsFocusActive, None)
    _FocusSessionManager_Meta_.IsSupported = property(get_IsSupported.__wrapped__, None)
class IAdaptiveCard(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IAdaptiveCard'
    _iid_ = Guid('{72d0568c-a274-41cd-82a8-989d40b9b05e}')
    @winrt_commethod(6)
    def ToJson(self) -> WinRT_String: ...
class IAdaptiveCardBuilderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IAdaptiveCardBuilderStatics'
    _iid_ = Guid('{766d8f08-d3fe-4347-a0bc-b9ea9a6dc28e}')
    @winrt_commethod(6)
    def CreateAdaptiveCardFromJson(self, value: WinRT_String) -> Windows.UI.Shell.IAdaptiveCard: ...
class IFocusSession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IFocusSession'
    _iid_ = Guid('{069fbab8-0e84-5f2f-8614-9b6544326277}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def End(self) -> Void: ...
    Id = property(get_Id, None)
class IFocusSessionManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IFocusSessionManager'
    _iid_ = Guid('{e7ffbaa9-d8be-5dbf-bac6-49364842e37e}')
    @winrt_commethod(6)
    def get_IsFocusActive(self) -> Boolean: ...
    @winrt_commethod(7)
    def GetSession(self, id: WinRT_String) -> Windows.UI.Shell.FocusSession: ...
    @winrt_commethod(8)
    def TryStartFocusSession(self) -> Windows.UI.Shell.FocusSession: ...
    @winrt_commethod(9)
    def TryStartFocusSession2(self, endTime: Windows.Foundation.DateTime) -> Windows.UI.Shell.FocusSession: ...
    @winrt_commethod(10)
    def DeactivateFocus(self) -> Void: ...
    @winrt_commethod(11)
    def add_IsFocusActiveChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Shell.FocusSessionManager, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_IsFocusActiveChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsFocusActive = property(get_IsFocusActive, None)
class IFocusSessionManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IFocusSessionManagerStatics'
    _iid_ = Guid('{834df764-cb9a-5d0a-aa9f-73df4f249395}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.UI.Shell.FocusSessionManager: ...
    @winrt_commethod(7)
    def get_IsSupported(self) -> Boolean: ...
    IsSupported = property(get_IsSupported, None)
class ISecurityAppManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.ISecurityAppManager'
    _iid_ = Guid('{96ac500c-aed4-561d-bde8-953520343a2d}')
    @winrt_commethod(6)
    def Register(self, kind: Windows.UI.Shell.SecurityAppKind, displayName: WinRT_String, detailsUri: Windows.Foundation.Uri, registerPerUser: Boolean) -> Guid: ...
    @winrt_commethod(7)
    def Unregister(self, kind: Windows.UI.Shell.SecurityAppKind, guidRegistration: Guid) -> Void: ...
    @winrt_commethod(8)
    def UpdateState(self, kind: Windows.UI.Shell.SecurityAppKind, guidRegistration: Guid, state: Windows.UI.Shell.SecurityAppState, substatus: Windows.UI.Shell.SecurityAppSubstatus, detailsUri: Windows.Foundation.Uri) -> Void: ...
class IShareWindowCommandEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IShareWindowCommandEventArgs'
    _iid_ = Guid('{4578dc09-a523-5756-a995-e4feb991fff0}')
    @winrt_commethod(6)
    def get_WindowId(self) -> Windows.UI.WindowId: ...
    @winrt_commethod(7)
    def get_Command(self) -> Windows.UI.Shell.ShareWindowCommand: ...
    @winrt_commethod(8)
    def put_Command(self, value: Windows.UI.Shell.ShareWindowCommand) -> Void: ...
    WindowId = property(get_WindowId, None)
    Command = property(get_Command, put_Command)
class IShareWindowCommandSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IShareWindowCommandSource'
    _iid_ = Guid('{cb3b7ae3-6b9c-561e-bccc-61e68e0abfef}')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def Stop(self) -> Void: ...
    @winrt_commethod(8)
    def ReportCommandChanged(self) -> Void: ...
    @winrt_commethod(9)
    def add_CommandRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Shell.ShareWindowCommandSource, Windows.UI.Shell.ShareWindowCommandEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_CommandRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_CommandInvoked(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Shell.ShareWindowCommandSource, Windows.UI.Shell.ShareWindowCommandEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_CommandInvoked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IShareWindowCommandSourceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IShareWindowCommandSourceStatics'
    _iid_ = Guid('{b0eb6656-9cac-517c-b6c7-8ef715084295}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.Shell.ShareWindowCommandSource: ...
class ITaskbarManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.ITaskbarManager'
    _iid_ = Guid('{87490a19-1ad9-49f4-b2e8-86738dc5ac40}')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsPinningAllowed(self) -> Boolean: ...
    @winrt_commethod(8)
    def IsCurrentAppPinnedAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def IsAppListEntryPinnedAsync(self, appListEntry: Windows.ApplicationModel.Core.AppListEntry) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def RequestPinCurrentAppAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def RequestPinAppListEntryAsync(self, appListEntry: Windows.ApplicationModel.Core.AppListEntry) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    IsSupported = property(get_IsSupported, None)
    IsPinningAllowed = property(get_IsPinningAllowed, None)
class ITaskbarManager2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.ITaskbarManager2'
    _iid_ = Guid('{79f0a06e-7b02-4911-918c-dee0bbd20ba4}')
    @winrt_commethod(6)
    def IsSecondaryTilePinnedAsync(self, tileId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def RequestPinSecondaryTileAsync(self, secondaryTile: Windows.UI.StartScreen.SecondaryTile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def TryUnpinSecondaryTileAsync(self, tileId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class ITaskbarManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.ITaskbarManagerStatics'
    _iid_ = Guid('{db32ab74-de52-4fe6-b7b6-95ff9f8395df}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.UI.Shell.TaskbarManager: ...
SecurityAppKind = Int32
SecurityAppKind_WebProtection: SecurityAppKind = 0
class SecurityAppManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Shell.ISecurityAppManager
    _classid_ = 'Windows.UI.Shell.SecurityAppManager'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Shell.SecurityAppManager: ...
    @winrt_mixinmethod
    def Register(self: Windows.UI.Shell.ISecurityAppManager, kind: Windows.UI.Shell.SecurityAppKind, displayName: WinRT_String, detailsUri: Windows.Foundation.Uri, registerPerUser: Boolean) -> Guid: ...
    @winrt_mixinmethod
    def Unregister(self: Windows.UI.Shell.ISecurityAppManager, kind: Windows.UI.Shell.SecurityAppKind, guidRegistration: Guid) -> Void: ...
    @winrt_mixinmethod
    def UpdateState(self: Windows.UI.Shell.ISecurityAppManager, kind: Windows.UI.Shell.SecurityAppKind, guidRegistration: Guid, state: Windows.UI.Shell.SecurityAppState, substatus: Windows.UI.Shell.SecurityAppSubstatus, detailsUri: Windows.Foundation.Uri) -> Void: ...
SecurityAppManagerContract: UInt32 = 65536
SecurityAppState = Int32
SecurityAppState_Disabled: SecurityAppState = 0
SecurityAppState_Enabled: SecurityAppState = 1
SecurityAppSubstatus = Int32
SecurityAppSubstatus_Undetermined: SecurityAppSubstatus = 0
SecurityAppSubstatus_NoActionNeeded: SecurityAppSubstatus = 1
SecurityAppSubstatus_ActionRecommended: SecurityAppSubstatus = 2
SecurityAppSubstatus_ActionNeeded: SecurityAppSubstatus = 3
ShareWindowCommand = Int32
ShareWindowCommand_None: ShareWindowCommand = 0
ShareWindowCommand_StartSharing: ShareWindowCommand = 1
ShareWindowCommand_StopSharing: ShareWindowCommand = 2
class ShareWindowCommandEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Shell.IShareWindowCommandEventArgs
    _classid_ = 'Windows.UI.Shell.ShareWindowCommandEventArgs'
    @winrt_mixinmethod
    def get_WindowId(self: Windows.UI.Shell.IShareWindowCommandEventArgs) -> Windows.UI.WindowId: ...
    @winrt_mixinmethod
    def get_Command(self: Windows.UI.Shell.IShareWindowCommandEventArgs) -> Windows.UI.Shell.ShareWindowCommand: ...
    @winrt_mixinmethod
    def put_Command(self: Windows.UI.Shell.IShareWindowCommandEventArgs, value: Windows.UI.Shell.ShareWindowCommand) -> Void: ...
    WindowId = property(get_WindowId, None)
    Command = property(get_Command, put_Command)
class ShareWindowCommandSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Shell.IShareWindowCommandSource
    _classid_ = 'Windows.UI.Shell.ShareWindowCommandSource'
    @winrt_mixinmethod
    def Start(self: Windows.UI.Shell.IShareWindowCommandSource) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.UI.Shell.IShareWindowCommandSource) -> Void: ...
    @winrt_mixinmethod
    def ReportCommandChanged(self: Windows.UI.Shell.IShareWindowCommandSource) -> Void: ...
    @winrt_mixinmethod
    def add_CommandRequested(self: Windows.UI.Shell.IShareWindowCommandSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Shell.ShareWindowCommandSource, Windows.UI.Shell.ShareWindowCommandEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CommandRequested(self: Windows.UI.Shell.IShareWindowCommandSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CommandInvoked(self: Windows.UI.Shell.IShareWindowCommandSource, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Shell.ShareWindowCommandSource, Windows.UI.Shell.ShareWindowCommandEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CommandInvoked(self: Windows.UI.Shell.IShareWindowCommandSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.Shell.IShareWindowCommandSourceStatics) -> Windows.UI.Shell.ShareWindowCommandSource: ...
class TaskbarManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Shell.ITaskbarManager
    _classid_ = 'Windows.UI.Shell.TaskbarManager'
    @winrt_mixinmethod
    def get_IsSupported(self: Windows.UI.Shell.ITaskbarManager) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPinningAllowed(self: Windows.UI.Shell.ITaskbarManager) -> Boolean: ...
    @winrt_mixinmethod
    def IsCurrentAppPinnedAsync(self: Windows.UI.Shell.ITaskbarManager) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def IsAppListEntryPinnedAsync(self: Windows.UI.Shell.ITaskbarManager, appListEntry: Windows.ApplicationModel.Core.AppListEntry) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestPinCurrentAppAsync(self: Windows.UI.Shell.ITaskbarManager) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestPinAppListEntryAsync(self: Windows.UI.Shell.ITaskbarManager, appListEntry: Windows.ApplicationModel.Core.AppListEntry) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def IsSecondaryTilePinnedAsync(self: Windows.UI.Shell.ITaskbarManager2, tileId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestPinSecondaryTileAsync(self: Windows.UI.Shell.ITaskbarManager2, secondaryTile: Windows.UI.StartScreen.SecondaryTile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryUnpinSecondaryTileAsync(self: Windows.UI.Shell.ITaskbarManager2, tileId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.UI.Shell.ITaskbarManagerStatics) -> Windows.UI.Shell.TaskbarManager: ...
    IsSupported = property(get_IsSupported, None)
    IsPinningAllowed = property(get_IsPinningAllowed, None)
make_head(_module, 'AdaptiveCardBuilder')
make_head(_module, 'FocusSession')
make_head(_module, 'FocusSessionManager')
make_head(_module, 'IAdaptiveCard')
make_head(_module, 'IAdaptiveCardBuilderStatics')
make_head(_module, 'IFocusSession')
make_head(_module, 'IFocusSessionManager')
make_head(_module, 'IFocusSessionManagerStatics')
make_head(_module, 'ISecurityAppManager')
make_head(_module, 'IShareWindowCommandEventArgs')
make_head(_module, 'IShareWindowCommandSource')
make_head(_module, 'IShareWindowCommandSourceStatics')
make_head(_module, 'ITaskbarManager')
make_head(_module, 'ITaskbarManager2')
make_head(_module, 'ITaskbarManagerStatics')
make_head(_module, 'SecurityAppManager')
make_head(_module, 'ShareWindowCommandEventArgs')
make_head(_module, 'ShareWindowCommandSource')
make_head(_module, 'TaskbarManager')
