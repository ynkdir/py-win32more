from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.UI
import win32more.Windows.UI.Notifications.Preview
class IToastOcclusionManagerPreviewStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Notifications.Preview.IToastOcclusionManagerPreviewStatics'
    _iid_ = Guid('{507e5c83-50f9-5412-8953-b65c18cfab12}')
    @winrt_commethod(6)
    def SetToastWindowMargin(self, appWindowId: win32more.Windows.UI.WindowId, margin: Double) -> Void: ...
class ToastOcclusionManagerPreview(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Notifications.Preview.ToastOcclusionManagerPreview'
    @winrt_classmethod
    def SetToastWindowMargin(cls: win32more.Windows.UI.Notifications.Preview.IToastOcclusionManagerPreviewStatics, appWindowId: win32more.Windows.UI.WindowId, margin: Double) -> Void: ...


make_ready(__name__)
