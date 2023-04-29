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
import Windows.UI.Xaml
import Windows.UI.Xaml.Interop
import Windows.UI.Xaml.Media.Animation
import Windows.UI.Xaml.Navigation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class FrameNavigationOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_commethod(6)
    def get_IsNavigationStackEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsNavigationStackEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_TransitionInfoOverride(self) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_commethod(9)
    def put_TransitionInfoOverride(self, value: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    IsNavigationStackEnabled = property(get_IsNavigationStackEnabled, put_IsNavigationStackEnabled)
    TransitionInfoOverride = property(get_TransitionInfoOverride, put_TransitionInfoOverride)
class IFrameNavigationOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b539ad2a-9fb7-520a-8f-41-57-a5-0c-59-cf-92')
    @winrt_commethod(6)
    def get_IsNavigationStackEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsNavigationStackEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_TransitionInfoOverride(self) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_commethod(9)
    def put_TransitionInfoOverride(self, value: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Void: ...
    IsNavigationStackEnabled = property(get_IsNavigationStackEnabled, put_IsNavigationStackEnabled)
    TransitionInfoOverride = property(get_TransitionInfoOverride, put_TransitionInfoOverride)
class IFrameNavigationOptionsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d4681e41-7e6d-5c7c-ac-a0-47-86-81-cc-6f-ce')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Navigation.FrameNavigationOptions: ...
class INavigatingCancelEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fd1d67ae-eafb-4079-be-80-6d-c9-2a-03-ae-df')
    @winrt_commethod(6)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_NavigationMode(self) -> Windows.UI.Xaml.Navigation.NavigationMode: ...
    @winrt_commethod(9)
    def get_SourcePageType(self) -> Windows.UI.Xaml.Interop.TypeName: ...
    Cancel = property(get_Cancel, put_Cancel)
    NavigationMode = property(get_NavigationMode, None)
    SourcePageType = property(get_SourcePageType, None)
class INavigatingCancelEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5407b704-8147-4343-83-8f-dd-1e-e9-08-c1-37')
    @winrt_commethod(6)
    def get_Parameter(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_NavigationTransitionInfo(self) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
class INavigationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b6aa9834-6691-44d1-bd-f7-58-82-0c-27-b0-d0')
    @winrt_commethod(6)
    def get_Content(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_Parameter(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(8)
    def get_SourcePageType(self) -> Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(9)
    def get_NavigationMode(self) -> Windows.UI.Xaml.Navigation.NavigationMode: ...
    @winrt_commethod(10)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def put_Uri(self, value: Windows.Foundation.Uri) -> Void: ...
    Content = property(get_Content, None)
    Parameter = property(get_Parameter, None)
    SourcePageType = property(get_SourcePageType, None)
    NavigationMode = property(get_NavigationMode, None)
    Uri = property(get_Uri, put_Uri)
class INavigationEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('dbff71d9-979a-4b2e-a4-9b-3b-b1-7f-de-f5-74')
    @winrt_commethod(6)
    def get_NavigationTransitionInfo(self) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
class INavigationFailedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('11c1dff7-36c2-4102-b2-ef-02-17-a9-72-89-b3')
    @winrt_commethod(6)
    def get_Exception(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_SourcePageType(self) -> Windows.UI.Xaml.Interop.TypeName: ...
    Exception = property(get_Exception, None)
    Handled = property(get_Handled, put_Handled)
    SourcePageType = property(get_SourcePageType, None)
class IPageStackEntry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ef8814a6-9388-4aca-85-72-40-51-94-06-90-80')
    @winrt_commethod(6)
    def get_SourcePageType(self) -> Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_commethod(7)
    def get_Parameter(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(8)
    def get_NavigationTransitionInfo(self) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    SourcePageType = property(get_SourcePageType, None)
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
class IPageStackEntryFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4454048a-a8b9-4f78-9b-84-1f-51-f5-88-51-ff')
    @winrt_commethod(6)
    def CreateInstance(self, sourcePageType: Windows.UI.Xaml.Interop.TypeName, parameter: Windows.Win32.System.WinRT.IInspectable_head, navigationTransitionInfo: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Windows.UI.Xaml.Navigation.PageStackEntry: ...
class IPageStackEntryStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('aceff8e3-246c-4033-9f-01-01-cb-0d-a5-25-4e')
    @winrt_commethod(6)
    def get_SourcePageTypeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    SourcePageTypeProperty = property(get_SourcePageTypeProperty, None)
class LoadCompletedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('aebaf785-43fc-4e2c-95-c3-97-ae-84-ea-bc-8e')
    ClassId = 'Windows.UI.Xaml.Navigation.LoadCompletedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Navigation.NavigationEventArgs) -> Void: ...
class NavigatedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('7bd1cf54-23cf-4cce-b2-f5-4c-e7-8d-96-89-6e')
    ClassId = 'Windows.UI.Xaml.Navigation.NavigatedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Navigation.NavigationEventArgs) -> Void: ...
class NavigatingCancelEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Navigation.NavigatingCancelEventArgs'
    @winrt_mixinmethod
    def get_Cancel(self: Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NavigationMode(self: Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs) -> Windows.UI.Xaml.Navigation.NavigationMode: ...
    @winrt_mixinmethod
    def get_SourcePageType(self: Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs) -> Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_mixinmethod
    def get_Parameter(self: Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs2) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_NavigationTransitionInfo(self: Windows.UI.Xaml.Navigation.INavigatingCancelEventArgs2) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    Cancel = property(get_Cancel, put_Cancel)
    NavigationMode = property(get_NavigationMode, None)
    SourcePageType = property(get_SourcePageType, None)
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
class NavigatingCancelEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('75d6a78f-a302-4489-98-98-24-ea-49-18-29-10')
    ClassId = 'Windows.UI.Xaml.Navigation.NavigatingCancelEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Navigation.NavigatingCancelEventArgs) -> Void: ...
NavigationCacheMode = Int32
NavigationCacheMode_Disabled: NavigationCacheMode = 0
NavigationCacheMode_Required: NavigationCacheMode = 1
NavigationCacheMode_Enabled: NavigationCacheMode = 2
class NavigationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Navigation.NavigationEventArgs'
    @winrt_mixinmethod
    def get_Content(self: Windows.UI.Xaml.Navigation.INavigationEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Parameter(self: Windows.UI.Xaml.Navigation.INavigationEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_SourcePageType(self: Windows.UI.Xaml.Navigation.INavigationEventArgs) -> Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_mixinmethod
    def get_NavigationMode(self: Windows.UI.Xaml.Navigation.INavigationEventArgs) -> Windows.UI.Xaml.Navigation.NavigationMode: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.UI.Xaml.Navigation.INavigationEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Uri(self: Windows.UI.Xaml.Navigation.INavigationEventArgs, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_NavigationTransitionInfo(self: Windows.UI.Xaml.Navigation.INavigationEventArgs2) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    Content = property(get_Content, None)
    Parameter = property(get_Parameter, None)
    SourcePageType = property(get_SourcePageType, None)
    NavigationMode = property(get_NavigationMode, None)
    Uri = property(get_Uri, put_Uri)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
class NavigationFailedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Navigation.NavigationFailedEventArgs'
    @winrt_mixinmethod
    def get_Exception(self: Windows.UI.Xaml.Navigation.INavigationFailedEventArgs) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Xaml.Navigation.INavigationFailedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Xaml.Navigation.INavigationFailedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SourcePageType(self: Windows.UI.Xaml.Navigation.INavigationFailedEventArgs) -> Windows.UI.Xaml.Interop.TypeName: ...
    Exception = property(get_Exception, None)
    Handled = property(get_Handled, put_Handled)
    SourcePageType = property(get_SourcePageType, None)
class NavigationFailedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('4dab4671-12b2-43c7-b8-92-9b-e2-dc-d3-e8-8d')
    ClassId = 'Windows.UI.Xaml.Navigation.NavigationFailedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Navigation.NavigationFailedEventArgs) -> Void: ...
NavigationMode = Int32
NavigationMode_New: NavigationMode = 0
NavigationMode_Back: NavigationMode = 1
NavigationMode_Forward: NavigationMode = 2
NavigationMode_Refresh: NavigationMode = 3
class NavigationStoppedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('f0117ddb-12fa-4d8d-8b-26-b3-83-d0-9c-2b-3c')
    ClassId = 'Windows.UI.Xaml.Navigation.NavigationStoppedEventHandler'
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Navigation.NavigationEventArgs) -> Void: ...
class PageStackEntry(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    ClassId = 'Windows.UI.Xaml.Navigation.PageStackEntry'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Navigation.IPageStackEntryFactory, sourcePageType: Windows.UI.Xaml.Interop.TypeName, parameter: Windows.Win32.System.WinRT.IInspectable_head, navigationTransitionInfo: Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo) -> Windows.UI.Xaml.Navigation.PageStackEntry: ...
    @winrt_mixinmethod
    def get_SourcePageType(self: Windows.UI.Xaml.Navigation.IPageStackEntry) -> Windows.UI.Xaml.Interop.TypeName: ...
    @winrt_mixinmethod
    def get_Parameter(self: Windows.UI.Xaml.Navigation.IPageStackEntry) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_NavigationTransitionInfo(self: Windows.UI.Xaml.Navigation.IPageStackEntry) -> Windows.UI.Xaml.Media.Animation.NavigationTransitionInfo: ...
    @winrt_classmethod
    def get_SourcePageTypeProperty(cls: Windows.UI.Xaml.Navigation.IPageStackEntryStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    SourcePageType = property(get_SourcePageType, None)
    Parameter = property(get_Parameter, None)
    NavigationTransitionInfo = property(get_NavigationTransitionInfo, None)
    SourcePageTypeProperty = property(get_SourcePageTypeProperty, None)
make_head(_module, 'FrameNavigationOptions')
make_head(_module, 'IFrameNavigationOptions')
make_head(_module, 'IFrameNavigationOptionsFactory')
make_head(_module, 'INavigatingCancelEventArgs')
make_head(_module, 'INavigatingCancelEventArgs2')
make_head(_module, 'INavigationEventArgs')
make_head(_module, 'INavigationEventArgs2')
make_head(_module, 'INavigationFailedEventArgs')
make_head(_module, 'IPageStackEntry')
make_head(_module, 'IPageStackEntryFactory')
make_head(_module, 'IPageStackEntryStatics')
make_head(_module, 'LoadCompletedEventHandler')
make_head(_module, 'NavigatedEventHandler')
make_head(_module, 'NavigatingCancelEventArgs')
make_head(_module, 'NavigatingCancelEventHandler')
make_head(_module, 'NavigationEventArgs')
make_head(_module, 'NavigationFailedEventArgs')
make_head(_module, 'NavigationFailedEventHandler')
make_head(_module, 'NavigationStoppedEventHandler')
make_head(_module, 'PageStackEntry')
