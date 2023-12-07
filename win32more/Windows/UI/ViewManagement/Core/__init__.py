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
import win32more.Windows.UI
import win32more.Windows.UI.ViewManagement.Core
class CoreFrameworkInputView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputView
    _classid_ = 'Windows.UI.ViewManagement.Core.CoreFrameworkInputView'
    @winrt_mixinmethod
    def add_PrimaryViewAnimationStarting(self: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputView, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreFrameworkInputView, win32more.Windows.UI.ViewManagement.Core.CoreFrameworkInputViewAnimationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrimaryViewAnimationStarting(self: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputView, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_OcclusionsChanged(self: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputView, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreFrameworkInputView, win32more.Windows.UI.ViewManagement.Core.CoreFrameworkInputViewOcclusionsChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OcclusionsChanged(self: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputView, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForUIContext(cls: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewStatics, context: win32more.Windows.UI.UIContext) -> win32more.Windows.UI.ViewManagement.Core.CoreFrameworkInputView: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewStatics) -> win32more.Windows.UI.ViewManagement.Core.CoreFrameworkInputView: ...
class CoreFrameworkInputViewAnimationStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewAnimationStartingEventArgs
    _classid_ = 'Windows.UI.ViewManagement.Core.CoreFrameworkInputViewAnimationStartingEventArgs'
    @winrt_mixinmethod
    def get_Occlusions(self: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewAnimationStartingEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_mixinmethod
    def get_FrameworkAnimationRecommended(self: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewAnimationStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_AnimationDuration(self: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewAnimationStartingEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    Occlusions = property(get_Occlusions, None)
    FrameworkAnimationRecommended = property(get_FrameworkAnimationRecommended, None)
    AnimationDuration = property(get_AnimationDuration, None)
class CoreFrameworkInputViewOcclusionsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewOcclusionsChangedEventArgs
    _classid_ = 'Windows.UI.ViewManagement.Core.CoreFrameworkInputViewOcclusionsChangedEventArgs'
    @winrt_mixinmethod
    def get_Occlusions(self: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewOcclusionsChangedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewOcclusionsChangedEventArgs) -> Boolean: ...
    Occlusions = property(get_Occlusions, None)
    Handled = property(get_Handled, None)
class CoreInputView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.Core.ICoreInputView
    _classid_ = 'Windows.UI.ViewManagement.Core.CoreInputView'
    @winrt_mixinmethod
    def add_OcclusionsChanged(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusionsChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OcclusionsChanged(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetCoreInputViewOcclusions(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_mixinmethod
    def TryShowPrimaryView(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView) -> Boolean: ...
    @winrt_mixinmethod
    def TryHidePrimaryView(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView) -> Boolean: ...
    @winrt_mixinmethod
    def add_XYFocusTransferringFromPrimaryView(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.UI.ViewManagement.Core.CoreInputViewTransferringXYFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_XYFocusTransferringFromPrimaryView(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_XYFocusTransferredToPrimaryView(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_XYFocusTransferredToPrimaryView(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryTransferXYFocusToPrimaryView(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView2, origin: win32more.Windows.Foundation.Rect, direction: win32more.Windows.UI.ViewManagement.Core.CoreInputViewXYFocusTransferDirection) -> Boolean: ...
    @winrt_mixinmethod
    def TryShow(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView3) -> Boolean: ...
    @winrt_mixinmethod
    def TryShowWithKind(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView3, type: win32more.Windows.UI.ViewManagement.Core.CoreInputViewKind) -> Boolean: ...
    @winrt_mixinmethod
    def TryHide(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView3) -> Boolean: ...
    @winrt_mixinmethod
    def add_PrimaryViewShowing(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.UI.ViewManagement.Core.CoreInputViewShowingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrimaryViewShowing(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PrimaryViewHiding(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.UI.ViewManagement.Core.CoreInputViewHidingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrimaryViewHiding(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def IsKindSupported(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView5, type: win32more.Windows.UI.ViewManagement.Core.CoreInputViewKind) -> Boolean: ...
    @winrt_mixinmethod
    def add_SupportedKindsChanged(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView5, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SupportedKindsChanged(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView5, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PrimaryViewAnimationStarting(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView5, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.UI.ViewManagement.Core.CoreInputViewAnimationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrimaryViewAnimationStarting(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputView5, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForUIContext(cls: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewStatics2, context: win32more.Windows.UI.UIContext) -> win32more.Windows.UI.ViewManagement.Core.CoreInputView: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewStatics) -> win32more.Windows.UI.ViewManagement.Core.CoreInputView: ...
class CoreInputViewAnimationStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewAnimationStartingEventArgs
    _classid_ = 'Windows.UI.ViewManagement.Core.CoreInputViewAnimationStartingEventArgs'
    @winrt_mixinmethod
    def get_Occlusions(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewAnimationStartingEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewAnimationStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewAnimationStartingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AnimationDuration(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewAnimationStartingEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    Occlusions = property(get_Occlusions, None)
    Handled = property(get_Handled, put_Handled)
    AnimationDuration = property(get_AnimationDuration, None)
class CoreInputViewHidingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewHidingEventArgs
    _classid_ = 'Windows.UI.ViewManagement.Core.CoreInputViewHidingEventArgs'
    @winrt_mixinmethod
    def TryCancel(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewHidingEventArgs) -> Boolean: ...
CoreInputViewKind = Int32
CoreInputViewKind_Default: CoreInputViewKind = 0
CoreInputViewKind_Keyboard: CoreInputViewKind = 1
CoreInputViewKind_Handwriting: CoreInputViewKind = 2
CoreInputViewKind_Emoji: CoreInputViewKind = 3
CoreInputViewKind_Symbols: CoreInputViewKind = 4
CoreInputViewKind_Clipboard: CoreInputViewKind = 5
CoreInputViewKind_Dictation: CoreInputViewKind = 6
class CoreInputViewOcclusion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewOcclusion
    _classid_ = 'Windows.UI.ViewManagement.Core.CoreInputViewOcclusion'
    @winrt_mixinmethod
    def get_OccludingRect(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewOcclusion) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_OcclusionKind(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewOcclusion) -> win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusionKind: ...
    OccludingRect = property(get_OccludingRect, None)
    OcclusionKind = property(get_OcclusionKind, None)
CoreInputViewOcclusionKind = Int32
CoreInputViewOcclusionKind_Docked: CoreInputViewOcclusionKind = 0
CoreInputViewOcclusionKind_Floating: CoreInputViewOcclusionKind = 1
CoreInputViewOcclusionKind_Overlay: CoreInputViewOcclusionKind = 2
class CoreInputViewOcclusionsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewOcclusionsChangedEventArgs
    _classid_ = 'Windows.UI.ViewManagement.Core.CoreInputViewOcclusionsChangedEventArgs'
    @winrt_mixinmethod
    def get_Occlusions(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewOcclusionsChangedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewOcclusionsChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewOcclusionsChangedEventArgs, value: Boolean) -> Void: ...
    Occlusions = property(get_Occlusions, None)
    Handled = property(get_Handled, put_Handled)
class CoreInputViewShowingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewShowingEventArgs
    _classid_ = 'Windows.UI.ViewManagement.Core.CoreInputViewShowingEventArgs'
    @winrt_mixinmethod
    def TryCancel(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewShowingEventArgs) -> Boolean: ...
class CoreInputViewTransferringXYFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs
    _classid_ = 'Windows.UI.ViewManagement.Core.CoreInputViewTransferringXYFocusEventArgs'
    @winrt_mixinmethod
    def get_Origin(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs) -> win32more.Windows.UI.ViewManagement.Core.CoreInputViewXYFocusTransferDirection: ...
    @winrt_mixinmethod
    def put_TransferHandled(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TransferHandled(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeepPrimaryViewVisible(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeepPrimaryViewVisible(self: win32more.Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs) -> Boolean: ...
    Origin = property(get_Origin, None)
    Direction = property(get_Direction, None)
    TransferHandled = property(get_TransferHandled, put_TransferHandled)
    KeepPrimaryViewVisible = property(get_KeepPrimaryViewVisible, put_KeepPrimaryViewVisible)
CoreInputViewXYFocusTransferDirection = Int32
CoreInputViewXYFocusTransferDirection_Up: CoreInputViewXYFocusTransferDirection = 0
CoreInputViewXYFocusTransferDirection_Right: CoreInputViewXYFocusTransferDirection = 1
CoreInputViewXYFocusTransferDirection_Down: CoreInputViewXYFocusTransferDirection = 2
CoreInputViewXYFocusTransferDirection_Left: CoreInputViewXYFocusTransferDirection = 3
class ICoreFrameworkInputView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreFrameworkInputView'
    _iid_ = Guid('{d77c94ae-46b8-5d4a-9489-8ddec3d639a6}')
    @winrt_commethod(6)
    def add_PrimaryViewAnimationStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreFrameworkInputView, win32more.Windows.UI.ViewManagement.Core.CoreFrameworkInputViewAnimationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PrimaryViewAnimationStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_OcclusionsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreFrameworkInputView, win32more.Windows.UI.ViewManagement.Core.CoreFrameworkInputViewOcclusionsChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_OcclusionsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreFrameworkInputViewAnimationStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewAnimationStartingEventArgs'
    _iid_ = Guid('{c0ec901c-bba4-501b-ae8b-65c9e756a719}')
    @winrt_commethod(6)
    def get_Occlusions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_commethod(7)
    def get_FrameworkAnimationRecommended(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_AnimationDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    Occlusions = property(get_Occlusions, None)
    FrameworkAnimationRecommended = property(get_FrameworkAnimationRecommended, None)
    AnimationDuration = property(get_AnimationDuration, None)
class ICoreFrameworkInputViewOcclusionsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewOcclusionsChangedEventArgs'
    _iid_ = Guid('{f36f4949-c82c-53d1-a75d-2b2baf0d9b0d}')
    @winrt_commethod(6)
    def get_Occlusions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    Occlusions = property(get_Occlusions, None)
    Handled = property(get_Handled, None)
class ICoreFrameworkInputViewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewStatics'
    _iid_ = Guid('{6eebd9b6-eac2-5f8b-975f-772ee3e42eeb}')
    @winrt_commethod(6)
    def GetForUIContext(self, context: win32more.Windows.UI.UIContext) -> win32more.Windows.UI.ViewManagement.Core.CoreFrameworkInputView: ...
    @winrt_commethod(7)
    def GetForCurrentView(self) -> win32more.Windows.UI.ViewManagement.Core.CoreFrameworkInputView: ...
class ICoreInputView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreInputView'
    _iid_ = Guid('{c770cd7a-7001-4c32-bf94-25c1f554cbf1}')
    @winrt_commethod(6)
    def add_OcclusionsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusionsChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_OcclusionsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def GetCoreInputViewOcclusions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_commethod(9)
    def TryShowPrimaryView(self) -> Boolean: ...
    @winrt_commethod(10)
    def TryHidePrimaryView(self) -> Boolean: ...
class ICoreInputView2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreInputView2'
    _iid_ = Guid('{0ed726c1-e09a-4ae8-aedf-dfa4857d1a01}')
    @winrt_commethod(6)
    def add_XYFocusTransferringFromPrimaryView(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.UI.ViewManagement.Core.CoreInputViewTransferringXYFocusEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_XYFocusTransferringFromPrimaryView(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_XYFocusTransferredToPrimaryView(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_XYFocusTransferredToPrimaryView(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def TryTransferXYFocusToPrimaryView(self, origin: win32more.Windows.Foundation.Rect, direction: win32more.Windows.UI.ViewManagement.Core.CoreInputViewXYFocusTransferDirection) -> Boolean: ...
class ICoreInputView3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreInputView3'
    _iid_ = Guid('{bc941653-3ab9-4849-8f58-46e7f0353cfc}')
    @winrt_commethod(6)
    def TryShow(self) -> Boolean: ...
    @winrt_commethod(7)
    def TryShowWithKind(self, type: win32more.Windows.UI.ViewManagement.Core.CoreInputViewKind) -> Boolean: ...
    @winrt_commethod(8)
    def TryHide(self) -> Boolean: ...
class ICoreInputView4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreInputView4'
    _iid_ = Guid('{002863d6-d9ef-57eb-8cef-77f6ce1b7ee7}')
    @winrt_commethod(6)
    def add_PrimaryViewShowing(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.UI.ViewManagement.Core.CoreInputViewShowingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PrimaryViewShowing(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_PrimaryViewHiding(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.UI.ViewManagement.Core.CoreInputViewHidingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_PrimaryViewHiding(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreInputView5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreInputView5'
    _iid_ = Guid('{136316e0-c6d5-5c57-811e-1ad8a99ba6ab}')
    @winrt_commethod(6)
    def IsKindSupported(self, type: win32more.Windows.UI.ViewManagement.Core.CoreInputViewKind) -> Boolean: ...
    @winrt_commethod(7)
    def add_SupportedKindsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_SupportedKindsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_PrimaryViewAnimationStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.ViewManagement.Core.CoreInputView, win32more.Windows.UI.ViewManagement.Core.CoreInputViewAnimationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PrimaryViewAnimationStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreInputViewAnimationStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreInputViewAnimationStartingEventArgs'
    _iid_ = Guid('{a9144af2-b55c-5ea1-b8ab-5340f3e94897}')
    @winrt_commethod(6)
    def get_Occlusions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_AnimationDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    Occlusions = property(get_Occlusions, None)
    Handled = property(get_Handled, put_Handled)
    AnimationDuration = property(get_AnimationDuration, None)
class ICoreInputViewHidingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreInputViewHidingEventArgs'
    _iid_ = Guid('{eada47bd-bac5-5336-848d-41083584daad}')
    @winrt_commethod(6)
    def TryCancel(self) -> Boolean: ...
class ICoreInputViewOcclusion(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreInputViewOcclusion'
    _iid_ = Guid('{cc36ce06-3865-4177-b5f5-8b65e0b9ce84}')
    @winrt_commethod(6)
    def get_OccludingRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_OcclusionKind(self) -> win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusionKind: ...
    OccludingRect = property(get_OccludingRect, None)
    OcclusionKind = property(get_OcclusionKind, None)
class ICoreInputViewOcclusionsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreInputViewOcclusionsChangedEventArgs'
    _iid_ = Guid('{be1027e8-b3ee-4df7-9554-89cdc66082c2}')
    @winrt_commethod(6)
    def get_Occlusions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    Occlusions = property(get_Occlusions, None)
    Handled = property(get_Handled, put_Handled)
class ICoreInputViewShowingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreInputViewShowingEventArgs'
    _iid_ = Guid('{ca52261b-fb9e-5daf-a98c-262b8b76af50}')
    @winrt_commethod(6)
    def TryCancel(self) -> Boolean: ...
class ICoreInputViewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreInputViewStatics'
    _iid_ = Guid('{7d9b97cd-edbe-49cf-a54f-337de052907f}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.ViewManagement.Core.CoreInputView: ...
class ICoreInputViewStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreInputViewStatics2'
    _iid_ = Guid('{7ebc0862-d049-4e52-87b0-1e90e98c49ed}')
    @winrt_commethod(6)
    def GetForUIContext(self, context: win32more.Windows.UI.UIContext) -> win32more.Windows.UI.ViewManagement.Core.CoreInputView: ...
class ICoreInputViewTransferringXYFocusEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs'
    _iid_ = Guid('{04de169f-ba02-4850-8b55-d82d03ba6d7f}')
    @winrt_commethod(6)
    def get_Origin(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_Direction(self) -> win32more.Windows.UI.ViewManagement.Core.CoreInputViewXYFocusTransferDirection: ...
    @winrt_commethod(8)
    def put_TransferHandled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_TransferHandled(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_KeepPrimaryViewVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_KeepPrimaryViewVisible(self) -> Boolean: ...
    Origin = property(get_Origin, None)
    Direction = property(get_Direction, None)
    TransferHandled = property(get_TransferHandled, put_TransferHandled)
    KeepPrimaryViewVisible = property(get_KeepPrimaryViewVisible, put_KeepPrimaryViewVisible)
class IUISettingsController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.IUISettingsController'
    _iid_ = Guid('{78a51ac4-15c0-5a1b-a75b-acbf9cb8bb9e}')
    @winrt_commethod(6)
    def SetAdvancedEffectsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def SetAnimationsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def SetAutoHideScrollBars(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def SetMessageDuration(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def SetTextScaleFactor(self, value: Double) -> Void: ...
class IUISettingsControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.ViewManagement.Core.IUISettingsControllerStatics'
    _iid_ = Guid('{eb3c68cc-c220-578c-8119-7db324ed26a6}')
    @winrt_commethod(6)
    def RequestDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.ViewManagement.Core.UISettingsController]: ...
class UISettingsController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.ViewManagement.Core.IUISettingsController
    _classid_ = 'Windows.UI.ViewManagement.Core.UISettingsController'
    @winrt_mixinmethod
    def SetAdvancedEffectsEnabled(self: win32more.Windows.UI.ViewManagement.Core.IUISettingsController, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetAnimationsEnabled(self: win32more.Windows.UI.ViewManagement.Core.IUISettingsController, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetAutoHideScrollBars(self: win32more.Windows.UI.ViewManagement.Core.IUISettingsController, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetMessageDuration(self: win32more.Windows.UI.ViewManagement.Core.IUISettingsController, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def SetTextScaleFactor(self: win32more.Windows.UI.ViewManagement.Core.IUISettingsController, value: Double) -> Void: ...
    @winrt_classmethod
    def RequestDefaultAsync(cls: win32more.Windows.UI.ViewManagement.Core.IUISettingsControllerStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.ViewManagement.Core.UISettingsController]: ...
make_ready(__name__)
