from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Devices.Pwm.Provider
import win32more.Windows.Foundation.Collections
class IPwmControllerProvider(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Pwm.Provider.IPwmControllerProvider'
    _iid_ = Guid('{1300593b-e2e3-40a4-b7d9-48dff0377a52}')
    @winrt_commethod(6)
    def get_PinCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ActualFrequency(self) -> Double: ...
    @winrt_commethod(8)
    def SetDesiredFrequency(self, frequency: Double) -> Double: ...
    @winrt_commethod(9)
    def get_MaxFrequency(self) -> Double: ...
    @winrt_commethod(10)
    def get_MinFrequency(self) -> Double: ...
    @winrt_commethod(11)
    def AcquirePin(self, pin: Int32) -> Void: ...
    @winrt_commethod(12)
    def ReleasePin(self, pin: Int32) -> Void: ...
    @winrt_commethod(13)
    def EnablePin(self, pin: Int32) -> Void: ...
    @winrt_commethod(14)
    def DisablePin(self, pin: Int32) -> Void: ...
    @winrt_commethod(15)
    def SetPulseParameters(self, pin: Int32, dutyCycle: Double, invertPolarity: Boolean) -> Void: ...
    ActualFrequency = property(get_ActualFrequency, None)
    MaxFrequency = property(get_MaxFrequency, None)
    MinFrequency = property(get_MinFrequency, None)
    PinCount = property(get_PinCount, None)
class IPwmProvider(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Pwm.Provider.IPwmProvider'
    _iid_ = Guid('{a3301228-52f1-47b0-9349-66ba43d25902}')
    @winrt_commethod(6)
    def GetControllers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Pwm.Provider.IPwmControllerProvider]: ...


make_ready(__name__)
