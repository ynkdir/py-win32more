from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.ApplicationModel.Core
import win32more.Windows.System
import win32more.Windows.UI.Core
import win32more.Windows.UI.Input
import win32more.Windows.UI.Input.Core
class IRadialControllerIndependentInputSource(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Core.IRadialControllerIndependentInputSource'
    _iid_ = Guid('{3d577ef6-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def get_Controller(self) -> win32more.Windows.UI.Input.RadialController: ...
    @winrt_commethod(7)
    def get_Dispatcher(self) -> win32more.Windows.UI.Core.CoreDispatcher: ...
    Controller = property(get_Controller, None)
    Dispatcher = property(get_Dispatcher, None)
class IRadialControllerIndependentInputSource2(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Core.IRadialControllerIndependentInputSource2'
    _iid_ = Guid('{7073aad8-35f3-4eeb-8751-be4d0a66faf4}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> win32more.Windows.System.DispatcherQueue: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class IRadialControllerIndependentInputSourceStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Input.Core.IRadialControllerIndependentInputSourceStatics'
    _iid_ = Guid('{3d577ef5-4cee-11e6-b535-001bdc06ab3b}')
    @winrt_commethod(6)
    def CreateForView(self, view: win32more.Windows.ApplicationModel.Core.CoreApplicationView) -> win32more.Windows.UI.Input.Core.RadialControllerIndependentInputSource: ...
class RadialControllerIndependentInputSource(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Input.Core.IRadialControllerIndependentInputSource
    _classid_ = 'Windows.UI.Input.Core.RadialControllerIndependentInputSource'
    @winrt_mixinmethod
    def get_Controller(self: win32more.Windows.UI.Input.Core.IRadialControllerIndependentInputSource) -> win32more.Windows.UI.Input.RadialController: ...
    @winrt_mixinmethod
    def get_Dispatcher(self: win32more.Windows.UI.Input.Core.IRadialControllerIndependentInputSource) -> win32more.Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: win32more.Windows.UI.Input.Core.IRadialControllerIndependentInputSource2) -> win32more.Windows.System.DispatcherQueue: ...
    @winrt_classmethod
    def CreateForView(cls: win32more.Windows.UI.Input.Core.IRadialControllerIndependentInputSourceStatics, view: win32more.Windows.ApplicationModel.Core.CoreApplicationView) -> win32more.Windows.UI.Input.Core.RadialControllerIndependentInputSource: ...
    Controller = property(get_Controller, None)
    Dispatcher = property(get_Dispatcher, None)
    DispatcherQueue = property(get_DispatcherQueue, None)


make_ready(__name__)
