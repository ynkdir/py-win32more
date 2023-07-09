from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Input.Inking.Preview
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPalmRejectionDelayZonePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Preview.IPalmRejectionDelayZonePreview'
    _iid_ = Guid('{62b496cb-539d-5343-a65f-41f5300ec70c}')
class IPalmRejectionDelayZonePreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Preview.IPalmRejectionDelayZonePreviewStatics'
    _iid_ = Guid('{cdef5ee0-93d0-53a9-8f0e-9a379f8f7530}')
    @winrt_commethod(6)
    def CreateForVisual(self, inputPanelVisual: win32more.Windows.UI.Composition.Visual, inputPanelRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview: ...
    @winrt_commethod(7)
    def CreateForVisualWithViewportClip(self, inputPanelVisual: win32more.Windows.UI.Composition.Visual, inputPanelRect: win32more.Windows.Foundation.Rect, viewportVisual: win32more.Windows.UI.Composition.Visual, viewportRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview: ...
class PalmRejectionDelayZonePreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Inking.Preview.IPalmRejectionDelayZonePreview
    _classid_ = 'Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview'
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateForVisual(cls: win32more.Windows.UI.Input.Inking.Preview.IPalmRejectionDelayZonePreviewStatics, inputPanelVisual: win32more.Windows.UI.Composition.Visual, inputPanelRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview: ...
    @winrt_classmethod
    def CreateForVisualWithViewportClip(cls: win32more.Windows.UI.Input.Inking.Preview.IPalmRejectionDelayZonePreviewStatics, inputPanelVisual: win32more.Windows.UI.Composition.Visual, inputPanelRect: win32more.Windows.Foundation.Rect, viewportVisual: win32more.Windows.UI.Composition.Visual, viewportRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview: ...
make_head(_module, 'IPalmRejectionDelayZonePreview')
make_head(_module, 'IPalmRejectionDelayZonePreviewStatics')
make_head(_module, 'PalmRejectionDelayZonePreview')
