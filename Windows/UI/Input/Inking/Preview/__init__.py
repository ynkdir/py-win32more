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
import Windows.UI.Composition
import Windows.UI.Input.Inking.Preview
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPalmRejectionDelayZonePreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('62b496cb-539d-5343-a6-5f-41-f5-30-0e-c7-0c')
class IPalmRejectionDelayZonePreviewStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cdef5ee0-93d0-53a9-8f-0e-9a-37-9f-8f-75-30')
    @winrt_commethod(6)
    def CreateForVisual(self, inputPanelVisual: Windows.UI.Composition.Visual, inputPanelRect: Windows.Foundation.Rect) -> Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview: ...
    @winrt_commethod(7)
    def CreateForVisualWithViewportClip(self, inputPanelVisual: Windows.UI.Composition.Visual, inputPanelRect: Windows.Foundation.Rect, viewportVisual: Windows.UI.Composition.Visual, viewportRect: Windows.Foundation.Rect) -> Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview: ...
class PalmRejectionDelayZonePreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview'
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateForVisual(cls: Windows.UI.Input.Inking.Preview.IPalmRejectionDelayZonePreviewStatics, inputPanelVisual: Windows.UI.Composition.Visual, inputPanelRect: Windows.Foundation.Rect) -> Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview: ...
    @winrt_classmethod
    def CreateForVisualWithViewportClip(cls: Windows.UI.Input.Inking.Preview.IPalmRejectionDelayZonePreviewStatics, inputPanelVisual: Windows.UI.Composition.Visual, inputPanelRect: Windows.Foundation.Rect, viewportVisual: Windows.UI.Composition.Visual, viewportRect: Windows.Foundation.Rect) -> Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview: ...
make_head(_module, 'IPalmRejectionDelayZonePreview')
make_head(_module, 'IPalmRejectionDelayZonePreviewStatics')
make_head(_module, 'PalmRejectionDelayZonePreview')
