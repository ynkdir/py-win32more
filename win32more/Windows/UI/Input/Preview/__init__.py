from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.UI.Input
import win32more.Windows.UI.Input.Preview
import win32more.Windows.UI.WindowManagement
class IInputActivationListenerPreviewStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.IInputActivationListenerPreviewStatics'
    _iid_ = Guid('{f0551ce5-0de6-5be0-a589-f737201a4582}')
    @winrt_commethod(6)
    def CreateForApplicationWindow(self, window: win32more.Windows.UI.WindowManagement.AppWindow) -> win32more.Windows.UI.Input.InputActivationListener: ...
class InputActivationListenerPreview(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Preview.InputActivationListenerPreview'
    @winrt_classmethod
    def CreateForApplicationWindow(cls: win32more.Windows.UI.Input.Preview.IInputActivationListenerPreviewStatics, window: win32more.Windows.UI.WindowManagement.AppWindow) -> win32more.Windows.UI.Input.InputActivationListener: ...


make_ready(__name__)
