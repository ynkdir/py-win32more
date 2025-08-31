from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Foundation
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Input.Inking.Preview
class IPalmRejectionDelayZonePreview(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Preview.IPalmRejectionDelayZonePreview'
    _iid_ = Guid('{62b496cb-539d-5343-a65f-41f5300ec70c}')
class IPalmRejectionDelayZonePreviewStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Inking.Preview.IPalmRejectionDelayZonePreviewStatics'
    _iid_ = Guid('{cdef5ee0-93d0-53a9-8f0e-9a379f8f7530}')
    @winrt_commethod(6)
    def CreateForVisual(self, inputPanelVisual: win32more.Windows.UI.Composition.Visual, inputPanelRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview: ...
    @winrt_commethod(7)
    def CreateForVisualWithViewportClip(self, inputPanelVisual: win32more.Windows.UI.Composition.Visual, inputPanelRect: win32more.Windows.Foundation.Rect, viewportVisual: win32more.Windows.UI.Composition.Visual, viewportRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview: ...
class PalmRejectionDelayZonePreview(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.UI.Input.Inking.Preview.IPalmRejectionDelayZonePreview
    _classid_ = 'Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview'
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateForVisual(cls: win32more.Windows.UI.Input.Inking.Preview.IPalmRejectionDelayZonePreviewStatics, inputPanelVisual: win32more.Windows.UI.Composition.Visual, inputPanelRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview: ...
    @winrt_classmethod
    def CreateForVisualWithViewportClip(cls: win32more.Windows.UI.Input.Inking.Preview.IPalmRejectionDelayZonePreviewStatics, inputPanelVisual: win32more.Windows.UI.Composition.Visual, inputPanelRect: win32more.Windows.Foundation.Rect, viewportVisual: win32more.Windows.UI.Composition.Visual, viewportRect: win32more.Windows.Foundation.Rect) -> win32more.Windows.UI.Input.Inking.Preview.PalmRejectionDelayZonePreview: ...


make_ready(__name__)
