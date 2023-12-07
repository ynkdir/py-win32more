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
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Media.Animation
import win32more.Microsoft.UI.Xaml.Navigation
import win32more.Windows.Foundation
import win32more.Windows.UI.Xaml.Interop
class FrameNavigationOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Navigation.IFrameNavigationOptions
    _classid_ = 'Microsoft.UI.Xaml.Navigation.FrameNavigationOptions'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Microsoft.UI.Xaml.Navigation.FrameNavigationOptions.CreateInstance(*args, None, None)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Navigation.IFrameNavigationOptionsFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Navigation.FrameNavigationOptions: ...
    @winrt_mixinmethod
    def get_IsNavigationStackEnabled(self: win32more.Microsoft.UI.Xaml.Navigation.IFrameNavigationOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsNavigationStackEnabled(self: win32more.Microsoft.UI.Xaml.Navigation.IFrameNavigationOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TransitionInfoOverride(self: win32more.Microsoft.UI.Xaml.Navigation.IFrameNavigationOptions) -> win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_mixinmethod
    def put_TransitionInfoOverride(self: win32more.Microsoft.UI.Xaml.Navigation.IFrameNavigationOptions, value: win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    IsNavigationStackEnabled = property(get_IsNavigationStackEnabled, put_IsNavigationStackEnabled)
    TransitionInfoOverride = property(get_TransitionInfoOverride, put_TransitionInfoOverride)
class IFrameNavigationOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Navigation.IFrameNavigationOptions'
    _iid_ = Guid('{390de593-14cf-5312-af99-6cd8d59ec5d5}')
    @winrt_commethod(6)
    def get_IsNavigationStackEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsNavigationStackEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_TransitionInfoOverride(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_commethod(9)
    def put_TransitionInfoOverride(self, value: win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    IsNavigationStackEnabled = property(get_IsNavigationStackEnabled, put_IsNavigationStackEnabled)
    TransitionInfoOverride = property(get_TransitionInfoOverride, put_TransitionInfoOverride)
class IFrameNavigationOptionsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Navigation.IFrameNavigationOptionsFactory'
    _iid_ = Guid('{ddf3f748-7127-5cee-9f79-ac281a234632}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Navigation.FrameNavigationOptions: ...
class INavigatingCancelEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Navigation.INavigatingCancelEventArgs'
    _iid_ = Guid('{172fde12-e06f-5df6-930e-5facf7b3fbe7}')
    @winrt_commethod(6)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_NavigationMode(self) -> win32more.Microsoft.UI.Xaml.Navigation.NavigationMode: ...
    @winrt_commethod(9)
    def get_SourcePageType(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(10)
    def get_Parameter(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(11)
    def get_NavigationTransitionInfo(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    Cancel = property(get_Cancel, put_Cancel)
    NavigationMode = property(get_NavigationMode, None)
    SourcePageType = property(get_SourcePageType, None)
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
class INavigationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Navigation.INavigationEventArgs'
    _iid_ = Guid('{876b70b4-2923-5785-9cea-2e44aa0761bd}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_Parameter(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(8)
    def get_NavigationTransitionInfo(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_commethod(9)
    def get_SourcePageType(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(10)
    def get_NavigationMode(self) -> win32more.Microsoft.UI.Xaml.Navigation.NavigationMode: ...
    @winrt_commethod(11)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def put_Uri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    Content = property(get_Content, None)
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
    SourcePageType = property(get_SourcePageType, None)
    NavigationMode = property(get_NavigationMode, None)
    Uri = property(get_Uri, put_Uri)
class INavigationFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Navigation.INavigationFailedEventArgs'
    _iid_ = Guid('{f808f9a0-130c-5974-87f8-4433271a35a9}')
    @winrt_commethod(6)
    def get_Exception(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_SourcePageType(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    Exception = property(get_Exception, None)
    Handled = property(get_Handled, put_Handled)
    SourcePageType = property(get_SourcePageType, None)
class IPageStackEntry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Navigation.IPageStackEntry'
    _iid_ = Guid('{d591f56e-4262-5c91-9d79-29165cd82100}')
    @winrt_commethod(6)
    def get_SourcePageType(self) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(7)
    def get_Parameter(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(8)
    def get_NavigationTransitionInfo(self) -> win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    SourcePageType = property(get_SourcePageType, None)
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
class IPageStackEntryFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Navigation.IPageStackEntryFactory'
    _iid_ = Guid('{7e5a9469-6108-5e92-a499-5ee9f065a68a}')
    @winrt_commethod(6)
    def CreateInstance(self, sourcePageType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, navigationTransitionInfo: win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> win32more.Microsoft.UI.Xaml.Navigation.PageStackEntry: ...
class IPageStackEntryStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Navigation.IPageStackEntryStatics'
    _iid_ = Guid('{2f1d4cb7-923b-59bb-bfc4-750933f28385}')
    @winrt_commethod(6)
    def get_SourcePageTypeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    SourcePageTypeProperty = property(get_SourcePageTypeProperty, None)
class NavigatedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8631b517-6d8e-58ee-82fe-d4034d1bd7c1}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Navigation.NavigationEventArgs) -> Void: ...
class NavigatingCancelEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Navigation.INavigatingCancelEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Navigation.NavigatingCancelEventArgs'
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Microsoft.UI.Xaml.Navigation.INavigatingCancelEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Microsoft.UI.Xaml.Navigation.INavigatingCancelEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NavigationMode(self: win32more.Microsoft.UI.Xaml.Navigation.INavigatingCancelEventArgs) -> win32more.Microsoft.UI.Xaml.Navigation.NavigationMode: ...
    @winrt_mixinmethod
    def get_SourcePageType(self: win32more.Microsoft.UI.Xaml.Navigation.INavigatingCancelEventArgs) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_mixinmethod
    def get_Parameter(self: win32more.Microsoft.UI.Xaml.Navigation.INavigatingCancelEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_NavigationTransitionInfo(self: win32more.Microsoft.UI.Xaml.Navigation.INavigatingCancelEventArgs) -> win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    Cancel = property(get_Cancel, put_Cancel)
    NavigationMode = property(get_NavigationMode, None)
    SourcePageType = property(get_SourcePageType, None)
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
class NavigatingCancelEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fcae1401-ec94-565f-9f48-7c4b6272b3b1}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Navigation.NavigatingCancelEventArgs) -> Void: ...
NavigationCacheMode = Int32
NavigationCacheMode_Disabled: NavigationCacheMode = 0
NavigationCacheMode_Required: NavigationCacheMode = 1
NavigationCacheMode_Enabled: NavigationCacheMode = 2
class NavigationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Navigation.INavigationEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Navigation.NavigationEventArgs'
    @winrt_mixinmethod
    def get_Content(self: win32more.Microsoft.UI.Xaml.Navigation.INavigationEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Parameter(self: win32more.Microsoft.UI.Xaml.Navigation.INavigationEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_NavigationTransitionInfo(self: win32more.Microsoft.UI.Xaml.Navigation.INavigationEventArgs) -> win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_mixinmethod
    def get_SourcePageType(self: win32more.Microsoft.UI.Xaml.Navigation.INavigationEventArgs) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_mixinmethod
    def get_NavigationMode(self: win32more.Microsoft.UI.Xaml.Navigation.INavigationEventArgs) -> win32more.Microsoft.UI.Xaml.Navigation.NavigationMode: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.UI.Xaml.Navigation.INavigationEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Microsoft.UI.Xaml.Navigation.INavigationEventArgs, value: win32more.Windows.Foundation.Uri) -> Void: ...
    Content = property(get_Content, None)
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
    SourcePageType = property(get_SourcePageType, None)
    NavigationMode = property(get_NavigationMode, None)
    Uri = property(get_Uri, put_Uri)
class NavigationFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Navigation.INavigationFailedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Navigation.NavigationFailedEventArgs'
    @winrt_mixinmethod
    def get_Exception(self: win32more.Microsoft.UI.Xaml.Navigation.INavigationFailedEventArgs) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Xaml.Navigation.INavigationFailedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Xaml.Navigation.INavigationFailedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SourcePageType(self: win32more.Microsoft.UI.Xaml.Navigation.INavigationFailedEventArgs) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    Exception = property(get_Exception, None)
    Handled = property(get_Handled, put_Handled)
    SourcePageType = property(get_SourcePageType, None)
class NavigationFailedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{97ca2b56-d6eb-5fd2-a675-a339640eedba}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Navigation.NavigationFailedEventArgs) -> Void: ...
NavigationMode = Int32
NavigationMode_New: NavigationMode = 0
NavigationMode_Back: NavigationMode = 1
NavigationMode_Forward: NavigationMode = 2
NavigationMode_Refresh: NavigationMode = 3
class NavigationStoppedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b9e796a6-7ffe-5a63-aef4-cbc331663b66}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Microsoft.UI.Xaml.Navigation.NavigationEventArgs) -> Void: ...
class _PageStackEntry_Meta_(ComPtr.__class__):
    pass
class PageStackEntry(ComPtr, metaclass=_PageStackEntry_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Navigation.IPageStackEntry
    _classid_ = 'Microsoft.UI.Xaml.Navigation.PageStackEntry'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 3:
            instance = win32more.Microsoft.UI.Xaml.Navigation.PageStackEntry.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Navigation.IPageStackEntryFactory, sourcePageType: win32more.Windows.UI.Xaml.Interop.TypeName, parameter: win32more.Windows.Win32.System.WinRT.IInspectable, navigationTransitionInfo: win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> win32more.Microsoft.UI.Xaml.Navigation.PageStackEntry: ...
    @winrt_mixinmethod
    def get_SourcePageType(self: win32more.Microsoft.UI.Xaml.Navigation.IPageStackEntry) -> win32more.Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_mixinmethod
    def get_Parameter(self: win32more.Microsoft.UI.Xaml.Navigation.IPageStackEntry) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_NavigationTransitionInfo(self: win32more.Microsoft.UI.Xaml.Navigation.IPageStackEntry) -> win32more.Microsoft.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_classmethod
    def get_SourcePageTypeProperty(cls: win32more.Microsoft.UI.Xaml.Navigation.IPageStackEntryStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    SourcePageType = property(get_SourcePageType, None)
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
    _PageStackEntry_Meta_.SourcePageTypeProperty = property(get_SourcePageTypeProperty.__wrapped__, None)
make_ready(__name__)
