from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.UI
import Windows.UI.ViewManagement.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CoreFrameworkInputView(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ViewManagement.Core.CoreFrameworkInputView'
    @winrt_mixinmethod
    def add_PrimaryViewAnimationStarting(self: Windows.UI.ViewManagement.Core.ICoreFrameworkInputView, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreFrameworkInputView, Windows.UI.ViewManagement.Core.CoreFrameworkInputViewAnimationStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrimaryViewAnimationStarting(self: Windows.UI.ViewManagement.Core.ICoreFrameworkInputView, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_OcclusionsChanged(self: Windows.UI.ViewManagement.Core.ICoreFrameworkInputView, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreFrameworkInputView, Windows.UI.ViewManagement.Core.CoreFrameworkInputViewOcclusionsChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OcclusionsChanged(self: Windows.UI.ViewManagement.Core.ICoreFrameworkInputView, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForUIContext(cls: Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewStatics, context: Windows.UI.UIContext) -> Windows.UI.ViewManagement.Core.CoreFrameworkInputView: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewStatics) -> Windows.UI.ViewManagement.Core.CoreFrameworkInputView: ...
class CoreFrameworkInputViewAnimationStartingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ViewManagement.Core.CoreFrameworkInputViewAnimationStartingEventArgs'
    @winrt_mixinmethod
    def get_Occlusions(self: Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewAnimationStartingEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_mixinmethod
    def get_FrameworkAnimationRecommended(self: Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewAnimationStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_AnimationDuration(self: Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewAnimationStartingEventArgs) -> Windows.Foundation.TimeSpan: ...
    Occlusions = property(get_Occlusions, None)
    FrameworkAnimationRecommended = property(get_FrameworkAnimationRecommended, None)
    AnimationDuration = property(get_AnimationDuration, None)
class CoreFrameworkInputViewOcclusionsChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ViewManagement.Core.CoreFrameworkInputViewOcclusionsChangedEventArgs'
    @winrt_mixinmethod
    def get_Occlusions(self: Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewOcclusionsChangedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.ViewManagement.Core.ICoreFrameworkInputViewOcclusionsChangedEventArgs) -> Boolean: ...
    Occlusions = property(get_Occlusions, None)
    Handled = property(get_Handled, None)
class CoreInputView(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ViewManagement.Core.CoreInputView'
    @winrt_mixinmethod
    def add_OcclusionsChanged(self: Windows.UI.ViewManagement.Core.ICoreInputView, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.UI.ViewManagement.Core.CoreInputViewOcclusionsChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OcclusionsChanged(self: Windows.UI.ViewManagement.Core.ICoreInputView, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetCoreInputViewOcclusions(self: Windows.UI.ViewManagement.Core.ICoreInputView) -> Windows.Foundation.Collections.IVectorView[Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_mixinmethod
    def TryShowPrimaryView(self: Windows.UI.ViewManagement.Core.ICoreInputView) -> Boolean: ...
    @winrt_mixinmethod
    def TryHidePrimaryView(self: Windows.UI.ViewManagement.Core.ICoreInputView) -> Boolean: ...
    @winrt_mixinmethod
    def add_XYFocusTransferringFromPrimaryView(self: Windows.UI.ViewManagement.Core.ICoreInputView2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.UI.ViewManagement.Core.CoreInputViewTransferringXYFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_XYFocusTransferringFromPrimaryView(self: Windows.UI.ViewManagement.Core.ICoreInputView2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_XYFocusTransferredToPrimaryView(self: Windows.UI.ViewManagement.Core.ICoreInputView2, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_XYFocusTransferredToPrimaryView(self: Windows.UI.ViewManagement.Core.ICoreInputView2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def TryTransferXYFocusToPrimaryView(self: Windows.UI.ViewManagement.Core.ICoreInputView2, origin: Windows.Foundation.Rect, direction: Windows.UI.ViewManagement.Core.CoreInputViewXYFocusTransferDirection) -> Boolean: ...
    @winrt_mixinmethod
    def TryShow(self: Windows.UI.ViewManagement.Core.ICoreInputView3) -> Boolean: ...
    @winrt_mixinmethod
    def TryShowWithKind(self: Windows.UI.ViewManagement.Core.ICoreInputView3, type: Windows.UI.ViewManagement.Core.CoreInputViewKind) -> Boolean: ...
    @winrt_mixinmethod
    def TryHide(self: Windows.UI.ViewManagement.Core.ICoreInputView3) -> Boolean: ...
    @winrt_mixinmethod
    def add_PrimaryViewShowing(self: Windows.UI.ViewManagement.Core.ICoreInputView4, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.UI.ViewManagement.Core.CoreInputViewShowingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrimaryViewShowing(self: Windows.UI.ViewManagement.Core.ICoreInputView4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PrimaryViewHiding(self: Windows.UI.ViewManagement.Core.ICoreInputView4, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.UI.ViewManagement.Core.CoreInputViewHidingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrimaryViewHiding(self: Windows.UI.ViewManagement.Core.ICoreInputView4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def IsKindSupported(self: Windows.UI.ViewManagement.Core.ICoreInputView5, type: Windows.UI.ViewManagement.Core.CoreInputViewKind) -> Boolean: ...
    @winrt_mixinmethod
    def add_SupportedKindsChanged(self: Windows.UI.ViewManagement.Core.ICoreInputView5, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SupportedKindsChanged(self: Windows.UI.ViewManagement.Core.ICoreInputView5, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PrimaryViewAnimationStarting(self: Windows.UI.ViewManagement.Core.ICoreInputView5, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.UI.ViewManagement.Core.CoreInputViewAnimationStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PrimaryViewAnimationStarting(self: Windows.UI.ViewManagement.Core.ICoreInputView5, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForUIContext(cls: Windows.UI.ViewManagement.Core.ICoreInputViewStatics2, context: Windows.UI.UIContext) -> Windows.UI.ViewManagement.Core.CoreInputView: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.ViewManagement.Core.ICoreInputViewStatics) -> Windows.UI.ViewManagement.Core.CoreInputView: ...
class CoreInputViewAnimationStartingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ViewManagement.Core.CoreInputViewAnimationStartingEventArgs'
    @winrt_mixinmethod
    def get_Occlusions(self: Windows.UI.ViewManagement.Core.ICoreInputViewAnimationStartingEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.ViewManagement.Core.ICoreInputViewAnimationStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.ViewManagement.Core.ICoreInputViewAnimationStartingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AnimationDuration(self: Windows.UI.ViewManagement.Core.ICoreInputViewAnimationStartingEventArgs) -> Windows.Foundation.TimeSpan: ...
    Occlusions = property(get_Occlusions, None)
    Handled = property(get_Handled, put_Handled)
    AnimationDuration = property(get_AnimationDuration, None)
class CoreInputViewHidingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ViewManagement.Core.CoreInputViewHidingEventArgs'
    @winrt_mixinmethod
    def TryCancel(self: Windows.UI.ViewManagement.Core.ICoreInputViewHidingEventArgs) -> Boolean: ...
CoreInputViewKind = Int32
CoreInputViewKind_Default: CoreInputViewKind = 0
CoreInputViewKind_Keyboard: CoreInputViewKind = 1
CoreInputViewKind_Handwriting: CoreInputViewKind = 2
CoreInputViewKind_Emoji: CoreInputViewKind = 3
CoreInputViewKind_Symbols: CoreInputViewKind = 4
CoreInputViewKind_Clipboard: CoreInputViewKind = 5
CoreInputViewKind_Dictation: CoreInputViewKind = 6
class CoreInputViewOcclusion(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ViewManagement.Core.CoreInputViewOcclusion'
    @winrt_mixinmethod
    def get_OccludingRect(self: Windows.UI.ViewManagement.Core.ICoreInputViewOcclusion) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_OcclusionKind(self: Windows.UI.ViewManagement.Core.ICoreInputViewOcclusion) -> Windows.UI.ViewManagement.Core.CoreInputViewOcclusionKind: ...
    OccludingRect = property(get_OccludingRect, None)
    OcclusionKind = property(get_OcclusionKind, None)
CoreInputViewOcclusionKind = Int32
CoreInputViewOcclusionKind_Docked: CoreInputViewOcclusionKind = 0
CoreInputViewOcclusionKind_Floating: CoreInputViewOcclusionKind = 1
CoreInputViewOcclusionKind_Overlay: CoreInputViewOcclusionKind = 2
class CoreInputViewOcclusionsChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ViewManagement.Core.CoreInputViewOcclusionsChangedEventArgs'
    @winrt_mixinmethod
    def get_Occlusions(self: Windows.UI.ViewManagement.Core.ICoreInputViewOcclusionsChangedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.ViewManagement.Core.ICoreInputViewOcclusionsChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.ViewManagement.Core.ICoreInputViewOcclusionsChangedEventArgs, value: Boolean) -> Void: ...
    Occlusions = property(get_Occlusions, None)
    Handled = property(get_Handled, put_Handled)
class CoreInputViewShowingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ViewManagement.Core.CoreInputViewShowingEventArgs'
    @winrt_mixinmethod
    def TryCancel(self: Windows.UI.ViewManagement.Core.ICoreInputViewShowingEventArgs) -> Boolean: ...
class CoreInputViewTransferringXYFocusEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ViewManagement.Core.CoreInputViewTransferringXYFocusEventArgs'
    @winrt_mixinmethod
    def get_Origin(self: Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_Direction(self: Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs) -> Windows.UI.ViewManagement.Core.CoreInputViewXYFocusTransferDirection: ...
    @winrt_mixinmethod
    def put_TransferHandled(self: Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TransferHandled(self: Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_KeepPrimaryViewVisible(self: Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeepPrimaryViewVisible(self: Windows.UI.ViewManagement.Core.ICoreInputViewTransferringXYFocusEventArgs) -> Boolean: ...
    Origin = property(get_Origin, None)
    Direction = property(get_Direction, None)
    TransferHandled = property(get_TransferHandled, put_TransferHandled)
    KeepPrimaryViewVisible = property(get_KeepPrimaryViewVisible, put_KeepPrimaryViewVisible)
CoreInputViewXYFocusTransferDirection = Int32
CoreInputViewXYFocusTransferDirection_Up: CoreInputViewXYFocusTransferDirection = 0
CoreInputViewXYFocusTransferDirection_Right: CoreInputViewXYFocusTransferDirection = 1
CoreInputViewXYFocusTransferDirection_Down: CoreInputViewXYFocusTransferDirection = 2
CoreInputViewXYFocusTransferDirection_Left: CoreInputViewXYFocusTransferDirection = 3
class ICoreFrameworkInputView(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d77c94ae-46b8-5d4a-94-89-8d-de-c3-d6-39-a6')
    @winrt_commethod(6)
    def add_PrimaryViewAnimationStarting(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreFrameworkInputView, Windows.UI.ViewManagement.Core.CoreFrameworkInputViewAnimationStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PrimaryViewAnimationStarting(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_OcclusionsChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreFrameworkInputView, Windows.UI.ViewManagement.Core.CoreFrameworkInputViewOcclusionsChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_OcclusionsChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreFrameworkInputViewAnimationStartingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c0ec901c-bba4-501b-ae-8b-65-c9-e7-56-a7-19')
    @winrt_commethod(6)
    def get_Occlusions(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_commethod(7)
    def get_FrameworkAnimationRecommended(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_AnimationDuration(self) -> Windows.Foundation.TimeSpan: ...
    Occlusions = property(get_Occlusions, None)
    FrameworkAnimationRecommended = property(get_FrameworkAnimationRecommended, None)
    AnimationDuration = property(get_AnimationDuration, None)
class ICoreFrameworkInputViewOcclusionsChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f36f4949-c82c-53d1-a7-5d-2b-2b-af-0d-9b-0d')
    @winrt_commethod(6)
    def get_Occlusions(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    Occlusions = property(get_Occlusions, None)
    Handled = property(get_Handled, None)
class ICoreFrameworkInputViewStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6eebd9b6-eac2-5f8b-97-5f-77-2e-e3-e4-2e-eb')
    @winrt_commethod(6)
    def GetForUIContext(self, context: Windows.UI.UIContext) -> Windows.UI.ViewManagement.Core.CoreFrameworkInputView: ...
    @winrt_commethod(7)
    def GetForCurrentView(self) -> Windows.UI.ViewManagement.Core.CoreFrameworkInputView: ...
class ICoreInputView(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c770cd7a-7001-4c32-bf-94-25-c1-f5-54-cb-f1')
    @winrt_commethod(6)
    def add_OcclusionsChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.UI.ViewManagement.Core.CoreInputViewOcclusionsChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_OcclusionsChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def GetCoreInputViewOcclusions(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_commethod(9)
    def TryShowPrimaryView(self) -> Boolean: ...
    @winrt_commethod(10)
    def TryHidePrimaryView(self) -> Boolean: ...
class ICoreInputView2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0ed726c1-e09a-4ae8-ae-df-df-a4-85-7d-1a-01')
    @winrt_commethod(6)
    def add_XYFocusTransferringFromPrimaryView(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.UI.ViewManagement.Core.CoreInputViewTransferringXYFocusEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_XYFocusTransferringFromPrimaryView(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_XYFocusTransferredToPrimaryView(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_XYFocusTransferredToPrimaryView(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def TryTransferXYFocusToPrimaryView(self, origin: Windows.Foundation.Rect, direction: Windows.UI.ViewManagement.Core.CoreInputViewXYFocusTransferDirection) -> Boolean: ...
class ICoreInputView3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bc941653-3ab9-4849-8f-58-46-e7-f0-35-3c-fc')
    @winrt_commethod(6)
    def TryShow(self) -> Boolean: ...
    @winrt_commethod(7)
    def TryShowWithKind(self, type: Windows.UI.ViewManagement.Core.CoreInputViewKind) -> Boolean: ...
    @winrt_commethod(8)
    def TryHide(self) -> Boolean: ...
class ICoreInputView4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('002863d6-d9ef-57eb-8c-ef-77-f6-ce-1b-7e-e7')
    @winrt_commethod(6)
    def add_PrimaryViewShowing(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.UI.ViewManagement.Core.CoreInputViewShowingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PrimaryViewShowing(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_PrimaryViewHiding(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.UI.ViewManagement.Core.CoreInputViewHidingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_PrimaryViewHiding(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreInputView5(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('136316e0-c6d5-5c57-81-1e-1a-d8-a9-9b-a6-ab')
    @winrt_commethod(6)
    def IsKindSupported(self, type: Windows.UI.ViewManagement.Core.CoreInputViewKind) -> Boolean: ...
    @winrt_commethod(7)
    def add_SupportedKindsChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_SupportedKindsChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_PrimaryViewAnimationStarting(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.ViewManagement.Core.CoreInputView, Windows.UI.ViewManagement.Core.CoreInputViewAnimationStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PrimaryViewAnimationStarting(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreInputViewAnimationStartingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a9144af2-b55c-5ea1-b8-ab-53-40-f3-e9-48-97')
    @winrt_commethod(6)
    def get_Occlusions(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_AnimationDuration(self) -> Windows.Foundation.TimeSpan: ...
    Occlusions = property(get_Occlusions, None)
    Handled = property(get_Handled, put_Handled)
    AnimationDuration = property(get_AnimationDuration, None)
class ICoreInputViewHidingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eada47bd-bac5-5336-84-8d-41-08-35-84-da-ad')
    @winrt_commethod(6)
    def TryCancel(self) -> Boolean: ...
class ICoreInputViewOcclusion(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cc36ce06-3865-4177-b5-f5-8b-65-e0-b9-ce-84')
    @winrt_commethod(6)
    def get_OccludingRect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_OcclusionKind(self) -> Windows.UI.ViewManagement.Core.CoreInputViewOcclusionKind: ...
    OccludingRect = property(get_OccludingRect, None)
    OcclusionKind = property(get_OcclusionKind, None)
class ICoreInputViewOcclusionsChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('be1027e8-b3ee-4df7-95-54-89-cd-c6-60-82-c2')
    @winrt_commethod(6)
    def get_Occlusions(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.ViewManagement.Core.CoreInputViewOcclusion]: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    Occlusions = property(get_Occlusions, None)
    Handled = property(get_Handled, put_Handled)
class ICoreInputViewShowingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ca52261b-fb9e-5daf-a9-8c-26-2b-8b-76-af-50')
    @winrt_commethod(6)
    def TryCancel(self) -> Boolean: ...
class ICoreInputViewStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7d9b97cd-edbe-49cf-a5-4f-33-7d-e0-52-90-7f')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.ViewManagement.Core.CoreInputView: ...
class ICoreInputViewStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7ebc0862-d049-4e52-87-b0-1e-90-e9-8c-49-ed')
    @winrt_commethod(6)
    def GetForUIContext(self, context: Windows.UI.UIContext) -> Windows.UI.ViewManagement.Core.CoreInputView: ...
class ICoreInputViewTransferringXYFocusEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('04de169f-ba02-4850-8b-55-d8-2d-03-ba-6d-7f')
    @winrt_commethod(6)
    def get_Origin(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_Direction(self) -> Windows.UI.ViewManagement.Core.CoreInputViewXYFocusTransferDirection: ...
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
class IUISettingsController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('78a51ac4-15c0-5a1b-a7-5b-ac-bf-9c-b8-bb-9e')
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
class IUISettingsControllerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eb3c68cc-c220-578c-81-19-7d-b3-24-ed-26-a6')
    @winrt_commethod(6)
    def RequestDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.UI.ViewManagement.Core.UISettingsController]: ...
class UISettingsController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.ViewManagement.Core.UISettingsController'
    @winrt_mixinmethod
    def SetAdvancedEffectsEnabled(self: Windows.UI.ViewManagement.Core.IUISettingsController, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetAnimationsEnabled(self: Windows.UI.ViewManagement.Core.IUISettingsController, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetAutoHideScrollBars(self: Windows.UI.ViewManagement.Core.IUISettingsController, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetMessageDuration(self: Windows.UI.ViewManagement.Core.IUISettingsController, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def SetTextScaleFactor(self: Windows.UI.ViewManagement.Core.IUISettingsController, value: Double) -> Void: ...
    @winrt_classmethod
    def RequestDefaultAsync(cls: Windows.UI.ViewManagement.Core.IUISettingsControllerStatics) -> Windows.Foundation.IAsyncOperation[Windows.UI.ViewManagement.Core.UISettingsController]: ...
make_head(_module, 'CoreFrameworkInputView')
make_head(_module, 'CoreFrameworkInputViewAnimationStartingEventArgs')
make_head(_module, 'CoreFrameworkInputViewOcclusionsChangedEventArgs')
make_head(_module, 'CoreInputView')
make_head(_module, 'CoreInputViewAnimationStartingEventArgs')
make_head(_module, 'CoreInputViewHidingEventArgs')
make_head(_module, 'CoreInputViewOcclusion')
make_head(_module, 'CoreInputViewOcclusionsChangedEventArgs')
make_head(_module, 'CoreInputViewShowingEventArgs')
make_head(_module, 'CoreInputViewTransferringXYFocusEventArgs')
make_head(_module, 'ICoreFrameworkInputView')
make_head(_module, 'ICoreFrameworkInputViewAnimationStartingEventArgs')
make_head(_module, 'ICoreFrameworkInputViewOcclusionsChangedEventArgs')
make_head(_module, 'ICoreFrameworkInputViewStatics')
make_head(_module, 'ICoreInputView')
make_head(_module, 'ICoreInputView2')
make_head(_module, 'ICoreInputView3')
make_head(_module, 'ICoreInputView4')
make_head(_module, 'ICoreInputView5')
make_head(_module, 'ICoreInputViewAnimationStartingEventArgs')
make_head(_module, 'ICoreInputViewHidingEventArgs')
make_head(_module, 'ICoreInputViewOcclusion')
make_head(_module, 'ICoreInputViewOcclusionsChangedEventArgs')
make_head(_module, 'ICoreInputViewShowingEventArgs')
make_head(_module, 'ICoreInputViewStatics')
make_head(_module, 'ICoreInputViewStatics2')
make_head(_module, 'ICoreInputViewTransferringXYFocusEventArgs')
make_head(_module, 'IUISettingsController')
make_head(_module, 'IUISettingsControllerStatics')
make_head(_module, 'UISettingsController')
