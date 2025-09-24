from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.ApplicationModel.Preview.InkWorkspace
import win32more.Windows.Foundation
import win32more.Windows.Graphics.Imaging
class IInkWorkspaceHostedAppManager(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManager'
    _iid_ = Guid('{fe0a7990-5e59-4bb7-8a63-7d218cd96300}')
    @winrt_commethod(6)
    def SetThumbnailAsync(self, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncAction: ...
class IInkWorkspaceHostedAppManagerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManagerStatics'
    _iid_ = Guid('{cbfd8cc5-a162-4bc4-84ee-e8716d5233c5}')
    @winrt_commethod(6)
    def GetForCurrentApp(self) -> win32more.Windows.ApplicationModel.Preview.InkWorkspace.InkWorkspaceHostedAppManager: ...
class InkWorkspaceHostedAppManager(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManager
    _classid_ = 'Windows.ApplicationModel.Preview.InkWorkspace.InkWorkspaceHostedAppManager'
    @winrt_mixinmethod
    def SetThumbnailAsync(self: win32more.Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManager, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetForCurrentApp(cls: win32more.Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManagerStatics) -> win32more.Windows.ApplicationModel.Preview.InkWorkspace.InkWorkspaceHostedAppManager: ...
PreviewInkWorkspaceContract: UInt32 = 65536


make_ready(__name__)
