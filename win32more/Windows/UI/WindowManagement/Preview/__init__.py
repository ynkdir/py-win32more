from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Foundation
import win32more.Windows.UI.WindowManagement
import win32more.Windows.UI.WindowManagement.Preview
class IWindowManagementPreview(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.WindowManagement.Preview.IWindowManagementPreview'
    _iid_ = Guid('{4ef55b0d-561d-513c-a67c-2c02b69cef41}')
class IWindowManagementPreviewStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.WindowManagement.Preview.IWindowManagementPreviewStatics'
    _iid_ = Guid('{0f9725c6-c004-5a23-8fd2-8d092ce2704a}')
    @winrt_commethod(6)
    def SetPreferredMinSize(self, window: win32more.Windows.UI.WindowManagement.AppWindow, preferredFrameMinSize: win32more.Windows.Foundation.Size) -> Void: ...
class WindowManagementPreview(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.WindowManagement.Preview.IWindowManagementPreview
    _classid_ = 'Windows.UI.WindowManagement.Preview.WindowManagementPreview'
    @winrt_classmethod
    def SetPreferredMinSize(cls: win32more.Windows.UI.WindowManagement.Preview.IWindowManagementPreviewStatics, window: win32more.Windows.UI.WindowManagement.AppWindow, preferredFrameMinSize: win32more.Windows.Foundation.Size) -> Void: ...


make_ready(__name__)
