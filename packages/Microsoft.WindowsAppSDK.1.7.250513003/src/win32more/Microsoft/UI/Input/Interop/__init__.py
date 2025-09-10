from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.UI.Input
import win32more.Microsoft.UI.Input.Interop
import win32more.Windows.Devices.Input
class IPenDeviceInteropStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Input.Interop.IPenDeviceInteropStatics'
    _iid_ = Guid('{c2a59f2a-e077-5d30-a1bd-cf84dd09ee39}')
    @winrt_commethod(6)
    def FromPointerPoint(self, pointerPoint: win32more.Microsoft.UI.Input.PointerPoint) -> win32more.Windows.Devices.Input.PenDevice: ...
class PenDeviceInterop(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Input.Interop.PenDeviceInterop'
    @winrt_classmethod
    def FromPointerPoint(cls: win32more.Microsoft.UI.Input.Interop.IPenDeviceInteropStatics, pointerPoint: win32more.Microsoft.UI.Input.PointerPoint) -> win32more.Windows.Devices.Input.PenDevice: ...


make_ready(__name__)
