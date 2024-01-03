from __future__ import annotations
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
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Input.Inking.Preview
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


make_ready(__name__)
