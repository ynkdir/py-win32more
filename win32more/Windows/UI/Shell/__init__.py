from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Core
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.UI.Shell
import win32more.Windows.UI.StartScreen
import win32more.Windows.Win32.System.WinRT
class AdaptiveCardBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.AdaptiveCardBuilder'
    @winrt_classmethod
    def CreateAdaptiveCardFromJson(cls: win32more.Windows.UI.Shell.IAdaptiveCardBuilderStatics, value: WinRT_String) -> win32more.Windows.UI.Shell.IAdaptiveCard: ...
class FocusSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.IFocusSession
    _classid_ = 'Windows.UI.Shell.FocusSession'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Shell.IFocusSession) -> WinRT_String: ...
    @winrt_mixinmethod
    def End(self: win32more.Windows.UI.Shell.IFocusSession) -> Void: ...
    Id = property(get_Id, None)
class _FocusSessionManager_Meta_(ComPtr.__class__):
    pass
class FocusSessionManager(ComPtr, metaclass=_FocusSessionManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.IFocusSessionManager
    _classid_ = 'Windows.UI.Shell.FocusSessionManager'
    @winrt_mixinmethod
    def get_IsFocusActive(self: win32more.Windows.UI.Shell.IFocusSessionManager) -> Boolean: ...
    @winrt_mixinmethod
    def GetSession(self: win32more.Windows.UI.Shell.IFocusSessionManager, id: WinRT_String) -> win32more.Windows.UI.Shell.FocusSession: ...
    @winrt_mixinmethod
    def TryStartFocusSession(self: win32more.Windows.UI.Shell.IFocusSessionManager) -> win32more.Windows.UI.Shell.FocusSession: ...
    @winrt_mixinmethod
    def TryStartFocusSession2(self: win32more.Windows.UI.Shell.IFocusSessionManager, endTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.UI.Shell.FocusSession: ...
    @winrt_mixinmethod
    def DeactivateFocus(self: win32more.Windows.UI.Shell.IFocusSessionManager) -> Void: ...
    @winrt_mixinmethod
    def add_IsFocusActiveChanged(self: win32more.Windows.UI.Shell.IFocusSessionManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.FocusSessionManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsFocusActiveChanged(self: win32more.Windows.UI.Shell.IFocusSessionManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.UI.Shell.IFocusSessionManagerStatics) -> win32more.Windows.UI.Shell.FocusSessionManager: ...
    @winrt_classmethod
    def get_IsSupported(cls: win32more.Windows.UI.Shell.IFocusSessionManagerStatics) -> Boolean: ...
    IsFocusActive = property(get_IsFocusActive, None)
    _FocusSessionManager_Meta_.IsSupported = property(get_IsSupported, None)
    IsFocusActiveChanged = event()
class IAdaptiveCard(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IAdaptiveCard'
    _iid_ = Guid('{72d0568c-a274-41cd-82a8-989d40b9b05e}')
    @winrt_commethod(6)
    def ToJson(self) -> WinRT_String: ...
class IAdaptiveCardBuilderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IAdaptiveCardBuilderStatics'
    _iid_ = Guid('{766d8f08-d3fe-4347-a0bc-b9ea9a6dc28e}')
    @winrt_commethod(6)
    def CreateAdaptiveCardFromJson(self, value: WinRT_String) -> win32more.Windows.UI.Shell.IAdaptiveCard: ...
class IFocusSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IFocusSession'
    _iid_ = Guid('{069fbab8-0e84-5f2f-8614-9b6544326277}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def End(self) -> Void: ...
    Id = property(get_Id, None)
class IFocusSessionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IFocusSessionManager'
    _iid_ = Guid('{e7ffbaa9-d8be-5dbf-bac6-49364842e37e}')
    @winrt_commethod(6)
    def get_IsFocusActive(self) -> Boolean: ...
    @winrt_commethod(7)
    def GetSession(self, id: WinRT_String) -> win32more.Windows.UI.Shell.FocusSession: ...
    @winrt_commethod(8)
    def TryStartFocusSession(self) -> win32more.Windows.UI.Shell.FocusSession: ...
    @winrt_commethod(9)
    def TryStartFocusSession2(self, endTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.UI.Shell.FocusSession: ...
    @winrt_commethod(10)
    def DeactivateFocus(self) -> Void: ...
    @winrt_commethod(11)
    def add_IsFocusActiveChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.FocusSessionManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_IsFocusActiveChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsFocusActive = property(get_IsFocusActive, None)
    IsFocusActiveChanged = event()
class IFocusSessionManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IFocusSessionManagerStatics'
    _iid_ = Guid('{834df764-cb9a-5d0a-aa9f-73df4f249395}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.UI.Shell.FocusSessionManager: ...
    @winrt_commethod(7)
    def get_IsSupported(self) -> Boolean: ...
    IsSupported = property(get_IsSupported, None)
class ISecurityAppManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.ISecurityAppManager'
    _iid_ = Guid('{96ac500c-aed4-561d-bde8-953520343a2d}')
    @winrt_commethod(6)
    def Register(self, kind: win32more.Windows.UI.Shell.SecurityAppKind, displayName: WinRT_String, detailsUri: win32more.Windows.Foundation.Uri, registerPerUser: Boolean) -> Guid: ...
    @winrt_commethod(7)
    def Unregister(self, kind: win32more.Windows.UI.Shell.SecurityAppKind, guidRegistration: Guid) -> Void: ...
    @winrt_commethod(8)
    def UpdateState(self, kind: win32more.Windows.UI.Shell.SecurityAppKind, guidRegistration: Guid, state: win32more.Windows.UI.Shell.SecurityAppState, substatus: win32more.Windows.UI.Shell.SecurityAppSubstatus, detailsUri: win32more.Windows.Foundation.Uri) -> Void: ...
class IShareWindowCommandEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IShareWindowCommandEventArgs'
    _iid_ = Guid('{4578dc09-a523-5756-a995-e4feb991fff0}')
    @winrt_commethod(6)
    def get_WindowId(self) -> win32more.Windows.UI.WindowId: ...
    @winrt_commethod(7)
    def get_Command(self) -> win32more.Windows.UI.Shell.ShareWindowCommand: ...
    @winrt_commethod(8)
    def put_Command(self, value: win32more.Windows.UI.Shell.ShareWindowCommand) -> Void: ...
    Command = property(get_Command, put_Command)
    WindowId = property(get_WindowId, None)
class IShareWindowCommandSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IShareWindowCommandSource'
    _iid_ = Guid('{cb3b7ae3-6b9c-561e-bccc-61e68e0abfef}')
    @winrt_commethod(6)
    def Start(self) -> Void: ...
    @winrt_commethod(7)
    def Stop(self) -> Void: ...
    @winrt_commethod(8)
    def ReportCommandChanged(self) -> Void: ...
    @winrt_commethod(9)
    def add_CommandRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.ShareWindowCommandSource, win32more.Windows.UI.Shell.ShareWindowCommandEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_CommandRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_CommandInvoked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.ShareWindowCommandSource, win32more.Windows.UI.Shell.ShareWindowCommandEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_CommandInvoked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CommandRequested = event()
    CommandInvoked = event()
class IShareWindowCommandSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IShareWindowCommandSourceStatics'
    _iid_ = Guid('{b0eb6656-9cac-517c-b6c7-8ef715084295}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.Shell.ShareWindowCommandSource: ...
class ITaskbarManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.ITaskbarManager'
    _iid_ = Guid('{87490a19-1ad9-49f4-b2e8-86738dc5ac40}')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsPinningAllowed(self) -> Boolean: ...
    @winrt_commethod(8)
    def IsCurrentAppPinnedAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def IsAppListEntryPinnedAsync(self, appListEntry: win32more.Windows.ApplicationModel.Core.AppListEntry) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def RequestPinCurrentAppAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def RequestPinAppListEntryAsync(self, appListEntry: win32more.Windows.ApplicationModel.Core.AppListEntry) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    IsPinningAllowed = property(get_IsPinningAllowed, None)
    IsSupported = property(get_IsSupported, None)
class ITaskbarManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.ITaskbarManager2'
    _iid_ = Guid('{79f0a06e-7b02-4911-918c-dee0bbd20ba4}')
    @winrt_commethod(6)
    def IsSecondaryTilePinnedAsync(self, tileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def RequestPinSecondaryTileAsync(self, secondaryTile: win32more.Windows.UI.StartScreen.SecondaryTile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def TryUnpinSecondaryTileAsync(self, tileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class ITaskbarManagerDesktopAppSupportStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.ITaskbarManagerDesktopAppSupportStatics'
    _iid_ = Guid('{cdfefd63-e879-4134-b9a7-8283f05f9480}')
class ITaskbarManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.ITaskbarManagerStatics'
    _iid_ = Guid('{db32ab74-de52-4fe6-b7b6-95ff9f8395df}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.UI.Shell.TaskbarManager: ...
class IWindowTab(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IWindowTab'
    _iid_ = Guid('{551e776a-7928-4d60-bdd9-672b5a5758eb}')
    @winrt_commethod(6)
    def get_Tag(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def put_Tag(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(8)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Icon(self) -> win32more.Windows.UI.Shell.WindowTabIcon: ...
    @winrt_commethod(11)
    def put_Icon(self, value: win32more.Windows.UI.Shell.WindowTabIcon) -> Void: ...
    @winrt_commethod(12)
    def get_TreatAsSecondaryTileId(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_TreatAsSecondaryTileId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_Group(self) -> win32more.Windows.UI.Shell.WindowTabGroup: ...
    @winrt_commethod(15)
    def put_Group(self, value: win32more.Windows.UI.Shell.WindowTabGroup) -> Void: ...
    @winrt_commethod(16)
    def ReportThumbnailAvailable(self) -> Void: ...
    Group = property(get_Group, put_Group)
    Icon = property(get_Icon, put_Icon)
    Tag = property(get_Tag, put_Tag)
    Title = property(get_Title, put_Title)
    TreatAsSecondaryTileId = property(get_TreatAsSecondaryTileId, put_TreatAsSecondaryTileId)
class IWindowTabCloseRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IWindowTabCloseRequestedEventArgs'
    _iid_ = Guid('{477282e9-eec4-5882-9889-2dd64d0f9fb6}')
    @winrt_commethod(6)
    def get_Tab(self) -> win32more.Windows.UI.Shell.WindowTab: ...
    Tab = property(get_Tab, None)
class IWindowTabCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IWindowTabCollection'
    _iid_ = Guid('{accd0d6c-ed07-519a-8c33-17e02e7e9b0f}')
    @winrt_commethod(6)
    def MoveTab(self, tab: win32more.Windows.UI.Shell.WindowTab, index: UInt32) -> Void: ...
class IWindowTabGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IWindowTabGroup'
    _iid_ = Guid('{a9c2c4fe-6cfe-449c-8b57-5756771abe56}')
    @winrt_commethod(6)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Icon(self) -> win32more.Windows.UI.Shell.WindowTabIcon: ...
    @winrt_commethod(9)
    def put_Icon(self, value: win32more.Windows.UI.Shell.WindowTabIcon) -> Void: ...
    Icon = property(get_Icon, put_Icon)
    Title = property(get_Title, put_Title)
class IWindowTabIcon(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IWindowTabIcon'
    _iid_ = Guid('{f92f398f-3669-4d0c-a183-14ddae6f6538}')
class IWindowTabIconStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IWindowTabIconStatics'
    _iid_ = Guid('{2e18d95e-2cbb-4084-af0c-36ee1c2d54b1}')
    @winrt_commethod(6)
    def CreateFromFontGlyph(self, glyph: WinRT_String, fontFamily: WinRT_String) -> win32more.Windows.UI.Shell.WindowTabIcon: ...
    @winrt_commethod(7)
    def CreateFromFontGlyphWithUri(self, glyph: WinRT_String, fontFamily: WinRT_String, fontUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Shell.WindowTabIcon: ...
    @winrt_commethod(8)
    def CreateFromImage(self, image: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.UI.Shell.WindowTabIcon: ...
class IWindowTabManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IWindowTabManager'
    _iid_ = Guid('{97b3c697-f43a-43e7-b3a2-e889a9835599}')
    @winrt_commethod(6)
    def get_Tabs(self) -> win32more.Windows.UI.Shell.WindowTabCollection: ...
    @winrt_commethod(7)
    def SetActiveTab(self, tab: win32more.Windows.UI.Shell.WindowTab) -> Void: ...
    @winrt_commethod(8)
    def add_TabSwitchRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.WindowTabManager, win32more.Windows.UI.Shell.WindowTabSwitchRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_TabSwitchRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_TabCloseRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.WindowTabManager, win32more.Windows.UI.Shell.WindowTabCloseRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_TabCloseRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_TabTearOutRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.WindowTabManager, win32more.Windows.UI.Shell.WindowTabTearOutRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_TabTearOutRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_TabThumbnailRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.WindowTabManager, win32more.Windows.UI.Shell.WindowTabThumbnailRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_TabThumbnailRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Tabs = property(get_Tabs, None)
    TabSwitchRequested = event()
    TabCloseRequested = event()
    TabTearOutRequested = event()
    TabThumbnailRequested = event()
class IWindowTabManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IWindowTabManagerStatics'
    _iid_ = Guid('{76755668-45f0-4e0b-8172-4e6d9d0f87bd}')
    @winrt_commethod(6)
    def GetForWindow(self, id: win32more.Windows.UI.WindowId) -> win32more.Windows.UI.Shell.WindowTabManager: ...
    @winrt_commethod(7)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def IsTabTearOutSupported(self) -> Boolean: ...
class IWindowTabSwitchRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IWindowTabSwitchRequestedEventArgs'
    _iid_ = Guid('{7cbc421a-58a4-568b-a351-f8a947a5aad8}')
    @winrt_commethod(6)
    def get_Tab(self) -> win32more.Windows.UI.Shell.WindowTab: ...
    Tab = property(get_Tab, None)
class IWindowTabTearOutRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IWindowTabTearOutRequestedEventArgs'
    _iid_ = Guid('{17d66659-5005-5ece-99af-566306e73642}')
    @winrt_commethod(6)
    def get_Tab(self) -> win32more.Windows.UI.Shell.WindowTab: ...
    @winrt_commethod(7)
    def get_WindowId(self) -> UInt64: ...
    @winrt_commethod(8)
    def put_WindowId(self, value: UInt64) -> Void: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Tab = property(get_Tab, None)
    WindowId = property(get_WindowId, put_WindowId)
class IWindowTabThumbnailRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Shell.IWindowTabThumbnailRequestedEventArgs'
    _iid_ = Guid('{2d558e54-9c4e-5abc-ab72-3350fb4937a0}')
    @winrt_commethod(6)
    def get_Tab(self) -> win32more.Windows.UI.Shell.WindowTab: ...
    @winrt_commethod(7)
    def get_RequestedSize(self) -> win32more.Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_commethod(8)
    def get_Image(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(9)
    def put_Image(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_commethod(11)
    def get_IsCompositedOnWindow(self) -> Boolean: ...
    Image = property(get_Image, put_Image)
    IsCompositedOnWindow = property(get_IsCompositedOnWindow, None)
    RequestedSize = property(get_RequestedSize, None)
    Tab = property(get_Tab, None)
class SecurityAppKind(Enum, Int32):
    WebProtection = 0
class SecurityAppManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.ISecurityAppManager
    _classid_ = 'Windows.UI.Shell.SecurityAppManager'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Shell.SecurityAppManager.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Shell.SecurityAppManager: ...
    @winrt_mixinmethod
    def Register(self: win32more.Windows.UI.Shell.ISecurityAppManager, kind: win32more.Windows.UI.Shell.SecurityAppKind, displayName: WinRT_String, detailsUri: win32more.Windows.Foundation.Uri, registerPerUser: Boolean) -> Guid: ...
    @winrt_mixinmethod
    def Unregister(self: win32more.Windows.UI.Shell.ISecurityAppManager, kind: win32more.Windows.UI.Shell.SecurityAppKind, guidRegistration: Guid) -> Void: ...
    @winrt_mixinmethod
    def UpdateState(self: win32more.Windows.UI.Shell.ISecurityAppManager, kind: win32more.Windows.UI.Shell.SecurityAppKind, guidRegistration: Guid, state: win32more.Windows.UI.Shell.SecurityAppState, substatus: win32more.Windows.UI.Shell.SecurityAppSubstatus, detailsUri: win32more.Windows.Foundation.Uri) -> Void: ...
SecurityAppManagerContract: UInt32 = 65536
class SecurityAppState(Enum, Int32):
    Disabled = 0
    Enabled = 1
class SecurityAppSubstatus(Enum, Int32):
    Undetermined = 0
    NoActionNeeded = 1
    ActionRecommended = 2
    ActionNeeded = 3
class ShareWindowCommand(Enum, Int32):
    None_ = 0
    StartSharing = 1
    StopSharing = 2
class ShareWindowCommandEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.IShareWindowCommandEventArgs
    _classid_ = 'Windows.UI.Shell.ShareWindowCommandEventArgs'
    @winrt_mixinmethod
    def get_WindowId(self: win32more.Windows.UI.Shell.IShareWindowCommandEventArgs) -> win32more.Windows.UI.WindowId: ...
    @winrt_mixinmethod
    def get_Command(self: win32more.Windows.UI.Shell.IShareWindowCommandEventArgs) -> win32more.Windows.UI.Shell.ShareWindowCommand: ...
    @winrt_mixinmethod
    def put_Command(self: win32more.Windows.UI.Shell.IShareWindowCommandEventArgs, value: win32more.Windows.UI.Shell.ShareWindowCommand) -> Void: ...
    Command = property(get_Command, put_Command)
    WindowId = property(get_WindowId, None)
class ShareWindowCommandSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.IShareWindowCommandSource
    _classid_ = 'Windows.UI.Shell.ShareWindowCommandSource'
    @winrt_mixinmethod
    def Start(self: win32more.Windows.UI.Shell.IShareWindowCommandSource) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.UI.Shell.IShareWindowCommandSource) -> Void: ...
    @winrt_mixinmethod
    def ReportCommandChanged(self: win32more.Windows.UI.Shell.IShareWindowCommandSource) -> Void: ...
    @winrt_mixinmethod
    def add_CommandRequested(self: win32more.Windows.UI.Shell.IShareWindowCommandSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.ShareWindowCommandSource, win32more.Windows.UI.Shell.ShareWindowCommandEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CommandRequested(self: win32more.Windows.UI.Shell.IShareWindowCommandSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CommandInvoked(self: win32more.Windows.UI.Shell.IShareWindowCommandSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.ShareWindowCommandSource, win32more.Windows.UI.Shell.ShareWindowCommandEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CommandInvoked(self: win32more.Windows.UI.Shell.IShareWindowCommandSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.Shell.IShareWindowCommandSourceStatics) -> win32more.Windows.UI.Shell.ShareWindowCommandSource: ...
    CommandRequested = event()
    CommandInvoked = event()
class TaskbarManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.ITaskbarManager
    _classid_ = 'Windows.UI.Shell.TaskbarManager'
    @winrt_mixinmethod
    def get_IsSupported(self: win32more.Windows.UI.Shell.ITaskbarManager) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPinningAllowed(self: win32more.Windows.UI.Shell.ITaskbarManager) -> Boolean: ...
    @winrt_mixinmethod
    def IsCurrentAppPinnedAsync(self: win32more.Windows.UI.Shell.ITaskbarManager) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def IsAppListEntryPinnedAsync(self: win32more.Windows.UI.Shell.ITaskbarManager, appListEntry: win32more.Windows.ApplicationModel.Core.AppListEntry) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestPinCurrentAppAsync(self: win32more.Windows.UI.Shell.ITaskbarManager) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestPinAppListEntryAsync(self: win32more.Windows.UI.Shell.ITaskbarManager, appListEntry: win32more.Windows.ApplicationModel.Core.AppListEntry) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def IsSecondaryTilePinnedAsync(self: win32more.Windows.UI.Shell.ITaskbarManager2, tileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestPinSecondaryTileAsync(self: win32more.Windows.UI.Shell.ITaskbarManager2, secondaryTile: win32more.Windows.UI.StartScreen.SecondaryTile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryUnpinSecondaryTileAsync(self: win32more.Windows.UI.Shell.ITaskbarManager2, tileId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.UI.Shell.ITaskbarManagerStatics) -> win32more.Windows.UI.Shell.TaskbarManager: ...
    IsPinningAllowed = property(get_IsPinningAllowed, None)
    IsSupported = property(get_IsSupported, None)
class WindowTab(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.IWindowTab
    _classid_ = 'Windows.UI.Shell.WindowTab'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Shell.WindowTab.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Shell.WindowTab: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.UI.Shell.IWindowTab) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.UI.Shell.IWindowTab, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.UI.Shell.IWindowTab) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.UI.Shell.IWindowTab, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Icon(self: win32more.Windows.UI.Shell.IWindowTab) -> win32more.Windows.UI.Shell.WindowTabIcon: ...
    @winrt_mixinmethod
    def put_Icon(self: win32more.Windows.UI.Shell.IWindowTab, value: win32more.Windows.UI.Shell.WindowTabIcon) -> Void: ...
    @winrt_mixinmethod
    def get_TreatAsSecondaryTileId(self: win32more.Windows.UI.Shell.IWindowTab) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TreatAsSecondaryTileId(self: win32more.Windows.UI.Shell.IWindowTab, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Group(self: win32more.Windows.UI.Shell.IWindowTab) -> win32more.Windows.UI.Shell.WindowTabGroup: ...
    @winrt_mixinmethod
    def put_Group(self: win32more.Windows.UI.Shell.IWindowTab, value: win32more.Windows.UI.Shell.WindowTabGroup) -> Void: ...
    @winrt_mixinmethod
    def ReportThumbnailAvailable(self: win32more.Windows.UI.Shell.IWindowTab) -> Void: ...
    Group = property(get_Group, put_Group)
    Icon = property(get_Icon, put_Icon)
    Tag = property(get_Tag, put_Tag)
    Title = property(get_Title, put_Title)
    TreatAsSecondaryTileId = property(get_TreatAsSecondaryTileId, put_TreatAsSecondaryTileId)
class WindowTabCloseRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.IWindowTabCloseRequestedEventArgs
    _classid_ = 'Windows.UI.Shell.WindowTabCloseRequestedEventArgs'
    @winrt_mixinmethod
    def get_Tab(self: win32more.Windows.UI.Shell.IWindowTabCloseRequestedEventArgs) -> win32more.Windows.UI.Shell.WindowTab: ...
    Tab = property(get_Tab, None)
class WindowTabCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Shell.WindowTab]]
    default_interface: win32more.Windows.UI.Shell.IWindowTabCollection
    _classid_ = 'Windows.UI.Shell.WindowTabCollection'
    @winrt_mixinmethod
    def MoveTab(self: win32more.Windows.UI.Shell.IWindowTabCollection, tab: win32more.Windows.UI.Shell.WindowTab, index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Shell.WindowTab], index: UInt32) -> win32more.Windows.UI.Shell.WindowTab: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Shell.WindowTab]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Shell.WindowTab]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Shell.WindowTab]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Shell.WindowTab], value: win32more.Windows.UI.Shell.WindowTab, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Shell.WindowTab], index: UInt32, value: win32more.Windows.UI.Shell.WindowTab) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Shell.WindowTab], index: UInt32, value: win32more.Windows.UI.Shell.WindowTab) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Shell.WindowTab], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Shell.WindowTab], value: win32more.Windows.UI.Shell.WindowTab) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Shell.WindowTab]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Shell.WindowTab]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Shell.WindowTab], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Shell.WindowTab]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Shell.WindowTab], items: PassArray[win32more.Windows.UI.Shell.WindowTab]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Shell.WindowTab]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Shell.WindowTab]: ...
    Size = property(get_Size, None)
class WindowTabGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.IWindowTabGroup
    _classid_ = 'Windows.UI.Shell.WindowTabGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Shell.WindowTabGroup.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Shell.WindowTabGroup: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.UI.Shell.IWindowTabGroup) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.UI.Shell.IWindowTabGroup, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Icon(self: win32more.Windows.UI.Shell.IWindowTabGroup) -> win32more.Windows.UI.Shell.WindowTabIcon: ...
    @winrt_mixinmethod
    def put_Icon(self: win32more.Windows.UI.Shell.IWindowTabGroup, value: win32more.Windows.UI.Shell.WindowTabIcon) -> Void: ...
    Icon = property(get_Icon, put_Icon)
    Title = property(get_Title, put_Title)
class WindowTabIcon(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.IWindowTabIcon
    _classid_ = 'Windows.UI.Shell.WindowTabIcon'
    @winrt_classmethod
    def CreateFromFontGlyph(cls: win32more.Windows.UI.Shell.IWindowTabIconStatics, glyph: WinRT_String, fontFamily: WinRT_String) -> win32more.Windows.UI.Shell.WindowTabIcon: ...
    @winrt_classmethod
    def CreateFromFontGlyphWithUri(cls: win32more.Windows.UI.Shell.IWindowTabIconStatics, glyph: WinRT_String, fontFamily: WinRT_String, fontUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Shell.WindowTabIcon: ...
    @winrt_classmethod
    def CreateFromImage(cls: win32more.Windows.UI.Shell.IWindowTabIconStatics, image: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.UI.Shell.WindowTabIcon: ...
class WindowTabManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.IWindowTabManager
    _classid_ = 'Windows.UI.Shell.WindowTabManager'
    @winrt_mixinmethod
    def get_Tabs(self: win32more.Windows.UI.Shell.IWindowTabManager) -> win32more.Windows.UI.Shell.WindowTabCollection: ...
    @winrt_mixinmethod
    def SetActiveTab(self: win32more.Windows.UI.Shell.IWindowTabManager, tab: win32more.Windows.UI.Shell.WindowTab) -> Void: ...
    @winrt_mixinmethod
    def add_TabSwitchRequested(self: win32more.Windows.UI.Shell.IWindowTabManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.WindowTabManager, win32more.Windows.UI.Shell.WindowTabSwitchRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TabSwitchRequested(self: win32more.Windows.UI.Shell.IWindowTabManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TabCloseRequested(self: win32more.Windows.UI.Shell.IWindowTabManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.WindowTabManager, win32more.Windows.UI.Shell.WindowTabCloseRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TabCloseRequested(self: win32more.Windows.UI.Shell.IWindowTabManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TabTearOutRequested(self: win32more.Windows.UI.Shell.IWindowTabManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.WindowTabManager, win32more.Windows.UI.Shell.WindowTabTearOutRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TabTearOutRequested(self: win32more.Windows.UI.Shell.IWindowTabManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TabThumbnailRequested(self: win32more.Windows.UI.Shell.IWindowTabManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Shell.WindowTabManager, win32more.Windows.UI.Shell.WindowTabThumbnailRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TabThumbnailRequested(self: win32more.Windows.UI.Shell.IWindowTabManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForWindow(cls: win32more.Windows.UI.Shell.IWindowTabManagerStatics, id: win32more.Windows.UI.WindowId) -> win32more.Windows.UI.Shell.WindowTabManager: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.UI.Shell.IWindowTabManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def IsTabTearOutSupported(cls: win32more.Windows.UI.Shell.IWindowTabManagerStatics) -> Boolean: ...
    Tabs = property(get_Tabs, None)
    TabSwitchRequested = event()
    TabCloseRequested = event()
    TabTearOutRequested = event()
    TabThumbnailRequested = event()
WindowTabManagerContract: UInt32 = 65536
class WindowTabSwitchRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.IWindowTabSwitchRequestedEventArgs
    _classid_ = 'Windows.UI.Shell.WindowTabSwitchRequestedEventArgs'
    @winrt_mixinmethod
    def get_Tab(self: win32more.Windows.UI.Shell.IWindowTabSwitchRequestedEventArgs) -> win32more.Windows.UI.Shell.WindowTab: ...
    Tab = property(get_Tab, None)
class WindowTabTearOutRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.IWindowTabTearOutRequestedEventArgs
    _classid_ = 'Windows.UI.Shell.WindowTabTearOutRequestedEventArgs'
    @winrt_mixinmethod
    def get_Tab(self: win32more.Windows.UI.Shell.IWindowTabTearOutRequestedEventArgs) -> win32more.Windows.UI.Shell.WindowTab: ...
    @winrt_mixinmethod
    def get_WindowId(self: win32more.Windows.UI.Shell.IWindowTabTearOutRequestedEventArgs) -> UInt64: ...
    @winrt_mixinmethod
    def put_WindowId(self: win32more.Windows.UI.Shell.IWindowTabTearOutRequestedEventArgs, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Shell.IWindowTabTearOutRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Tab = property(get_Tab, None)
    WindowId = property(get_WindowId, put_WindowId)
class WindowTabThumbnailRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Shell.IWindowTabThumbnailRequestedEventArgs
    _classid_ = 'Windows.UI.Shell.WindowTabThumbnailRequestedEventArgs'
    @winrt_mixinmethod
    def get_Tab(self: win32more.Windows.UI.Shell.IWindowTabThumbnailRequestedEventArgs) -> win32more.Windows.UI.Shell.WindowTab: ...
    @winrt_mixinmethod
    def get_RequestedSize(self: win32more.Windows.UI.Shell.IWindowTabThumbnailRequestedEventArgs) -> win32more.Windows.Graphics.Imaging.BitmapSize: ...
    @winrt_mixinmethod
    def get_Image(self: win32more.Windows.UI.Shell.IWindowTabThumbnailRequestedEventArgs) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Image(self: win32more.Windows.UI.Shell.IWindowTabThumbnailRequestedEventArgs, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Shell.IWindowTabThumbnailRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def get_IsCompositedOnWindow(self: win32more.Windows.UI.Shell.IWindowTabThumbnailRequestedEventArgs) -> Boolean: ...
    Image = property(get_Image, put_Image)
    IsCompositedOnWindow = property(get_IsCompositedOnWindow, None)
    RequestedSize = property(get_RequestedSize, None)
    Tab = property(get_Tab, None)


make_ready(__name__)
