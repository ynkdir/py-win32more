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
import Windows.UI.Composition
import Windows.UI.WindowManagement
import Windows.UI.Xaml
import Windows.UI.Xaml.Controls
import Windows.UI.Xaml.Hosting
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ElementCompositionPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Xaml.Hosting.ElementCompositionPreview'
    @winrt_classmethod
    def SetAppWindowContent(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics3, appWindow: Windows.UI.WindowManagement.AppWindow, xamlContent: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def GetAppWindowContent(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics3, appWindow: Windows.UI.WindowManagement.AppWindow) -> Windows.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def SetImplicitShowAnimation(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2, element: Windows.UI.Xaml.UIElement, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_classmethod
    def SetImplicitHideAnimation(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2, element: Windows.UI.Xaml.UIElement, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_classmethod
    def SetIsTranslationEnabled(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_classmethod
    def GetPointerPositionPropertySet(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics2, targetElement: Windows.UI.Xaml.UIElement) -> Windows.UI.Composition.CompositionPropertySet: ...
    @winrt_classmethod
    def GetElementVisual(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Composition.Visual: ...
    @winrt_classmethod
    def GetElementChildVisual(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Composition.Visual: ...
    @winrt_classmethod
    def SetElementChildVisual(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics, element: Windows.UI.Xaml.UIElement, visual: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_classmethod
    def GetScrollViewerManipulationPropertySet(cls: Windows.UI.Xaml.Hosting.IElementCompositionPreviewStatics, scrollViewer: Windows.UI.Xaml.Controls.ScrollViewer) -> Windows.UI.Composition.CompositionPropertySet: ...
class IElementCompositionPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b6f1a676-cfe6-46ac-ac-f6-c4-68-7b-b6-5e-60')
class IElementCompositionPreviewStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('08c92b38-ec99-4c55-bc-85-a1-c1-80-b2-76-46')
    @winrt_commethod(6)
    def GetElementVisual(self, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(7)
    def GetElementChildVisual(self, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Composition.Visual: ...
    @winrt_commethod(8)
    def SetElementChildVisual(self, element: Windows.UI.Xaml.UIElement, visual: Windows.UI.Composition.Visual) -> Void: ...
    @winrt_commethod(9)
    def GetScrollViewerManipulationPropertySet(self, scrollViewer: Windows.UI.Xaml.Controls.ScrollViewer) -> Windows.UI.Composition.CompositionPropertySet: ...
class IElementCompositionPreviewStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('24148fbb-23d6-4f37-ba-0c-07-33-e7-99-72-2d')
    @winrt_commethod(6)
    def SetImplicitShowAnimation(self, element: Windows.UI.Xaml.UIElement, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_commethod(7)
    def SetImplicitHideAnimation(self, element: Windows.UI.Xaml.UIElement, animation: Windows.UI.Composition.ICompositionAnimationBase) -> Void: ...
    @winrt_commethod(8)
    def SetIsTranslationEnabled(self, element: Windows.UI.Xaml.UIElement, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def GetPointerPositionPropertySet(self, targetElement: Windows.UI.Xaml.UIElement) -> Windows.UI.Composition.CompositionPropertySet: ...
class IElementCompositionPreviewStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('843bc4c3-c105-59fe-a3-d1-37-3c-1d-3e-6f-bc')
    @winrt_commethod(6)
    def SetAppWindowContent(self, appWindow: Windows.UI.WindowManagement.AppWindow, xamlContent: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(7)
    def GetAppWindowContent(self, appWindow: Windows.UI.WindowManagement.AppWindow) -> Windows.UI.Xaml.UIElement: ...
make_head(_module, 'ElementCompositionPreview')
make_head(_module, 'IElementCompositionPreview')
make_head(_module, 'IElementCompositionPreviewStatics')
make_head(_module, 'IElementCompositionPreviewStatics2')
make_head(_module, 'IElementCompositionPreviewStatics3')
