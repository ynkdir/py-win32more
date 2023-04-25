from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
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
class AdaptiveCardBuilder(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Shell.AdaptiveCardBuilder'
    @winrt_classmethod
    def CreateAdaptiveCardFromJson(cls: Windows.UI.Shell.IAdaptiveCardBuilderStatics, value: WinRT_String) -> Windows.UI.Shell.IAdaptiveCard: ...
class FocusSession(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Shell.FocusSession'
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Shell.IFocusSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def End(self: Windows.UI.Shell.IFocusSession) -> Void: ...
    Id = property(get_Id, None)
class FocusSessionManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Shell.FocusSessionManager'
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
    IsSupported = property(get_IsSupported, None)
class IAdaptiveCard(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('72d0568c-a274-41cd-82-a8-98-9d-40-b9-b0-5e')
    @winrt_commethod(6)
    def ToJson(self) -> WinRT_String: ...
class IAdaptiveCardBuilderStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('766d8f08-d3fe-4347-a0-bc-b9-ea-9a-6d-c2-8e')
    @winrt_commethod(6)
    def CreateAdaptiveCardFromJson(self, value: WinRT_String) -> Windows.UI.Shell.IAdaptiveCard: ...
class IFocusSession(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('069fbab8-0e84-5f2f-86-14-9b-65-44-32-62-77')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def End(self) -> Void: ...
    Id = property(get_Id, None)
class IFocusSessionManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e7ffbaa9-d8be-5dbf-ba-c6-49-36-48-42-e3-7e')
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
class IFocusSessionManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('834df764-cb9a-5d0a-aa-9f-73-df-4f-24-93-95')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.UI.Shell.FocusSessionManager: ...
    @winrt_commethod(7)
    def get_IsSupported(self) -> Boolean: ...
    IsSupported = property(get_IsSupported, None)
class IShareWindowCommandEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4578dc09-a523-5756-a9-95-e4-fe-b9-91-ff-f0')
    @winrt_commethod(6)
    def get_WindowId(self) -> Windows.UI.WindowId: ...
    @winrt_commethod(7)
    def get_Command(self) -> Windows.UI.Shell.ShareWindowCommand: ...
    @winrt_commethod(8)
    def put_Command(self, value: Windows.UI.Shell.ShareWindowCommand) -> Void: ...
    WindowId = property(get_WindowId, None)
    Command = property(get_Command, put_Command)
class IShareWindowCommandSource(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cb3b7ae3-6b9c-561e-bc-cc-61-e6-8e-0a-bf-ef')
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
class IShareWindowCommandSourceStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b0eb6656-9cac-517c-b6-c7-8e-f7-15-08-42-95')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.Shell.ShareWindowCommandSource: ...
class ITaskbarManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('87490a19-1ad9-49f4-b2-e8-86-73-8d-c5-ac-40')
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
class ITaskbarManager2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('79f0a06e-7b02-4911-91-8c-de-e0-bb-d2-0b-a4')
    @winrt_commethod(6)
    def IsSecondaryTilePinnedAsync(self, tileId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def RequestPinSecondaryTileAsync(self, secondaryTile: Windows.UI.StartScreen.SecondaryTile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def TryUnpinSecondaryTileAsync(self, tileId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class ITaskbarManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('db32ab74-de52-4fe6-b7-b6-95-ff-9f-83-95-df')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.UI.Shell.TaskbarManager: ...
ShareWindowCommand = Int32
ShareWindowCommand_None: ShareWindowCommand = 0
ShareWindowCommand_StartSharing: ShareWindowCommand = 1
ShareWindowCommand_StopSharing: ShareWindowCommand = 2
class ShareWindowCommandEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Shell.ShareWindowCommandEventArgs'
    @winrt_mixinmethod
    def get_WindowId(self: Windows.UI.Shell.IShareWindowCommandEventArgs) -> Windows.UI.WindowId: ...
    @winrt_mixinmethod
    def get_Command(self: Windows.UI.Shell.IShareWindowCommandEventArgs) -> Windows.UI.Shell.ShareWindowCommand: ...
    @winrt_mixinmethod
    def put_Command(self: Windows.UI.Shell.IShareWindowCommandEventArgs, value: Windows.UI.Shell.ShareWindowCommand) -> Void: ...
    WindowId = property(get_WindowId, None)
    Command = property(get_Command, put_Command)
class ShareWindowCommandSource(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Shell.ShareWindowCommandSource'
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
class TaskbarManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Shell.TaskbarManager'
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
make_head(_module, 'IShareWindowCommandEventArgs')
make_head(_module, 'IShareWindowCommandSource')
make_head(_module, 'IShareWindowCommandSourceStatics')
make_head(_module, 'ITaskbarManager')
make_head(_module, 'ITaskbarManager2')
make_head(_module, 'ITaskbarManagerStatics')
make_head(_module, 'ShareWindowCommandEventArgs')
make_head(_module, 'ShareWindowCommandSource')
make_head(_module, 'TaskbarManager')
