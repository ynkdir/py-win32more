from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Pwm
import win32more.Windows.Devices.Pwm.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class IPwmController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.IPwmController'
    _iid_ = Guid('{c45f5c85-d2e8-42cf-9bd6-cf5ed029e6a7}')
    @winrt_commethod(6)
    def get_PinCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ActualFrequency(self) -> Double: ...
    @winrt_commethod(8)
    def SetDesiredFrequency(self, desiredFrequency: Double) -> Double: ...
    @winrt_commethod(9)
    def get_MinFrequency(self) -> Double: ...
    @winrt_commethod(10)
    def get_MaxFrequency(self) -> Double: ...
    @winrt_commethod(11)
    def OpenPin(self, pinNumber: Int32) -> win32more.Windows.Devices.Pwm.PwmPin: ...
    ActualFrequency = property(get_ActualFrequency, None)
    MaxFrequency = property(get_MaxFrequency, None)
    MinFrequency = property(get_MinFrequency, None)
    PinCount = property(get_PinCount, None)
class IPwmControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.IPwmControllerStatics'
    _iid_ = Guid('{4263bda1-8946-4404-bd48-81dd124af4d9}')
    @winrt_commethod(6)
    def GetControllersAsync(self, provider: win32more.Windows.Devices.Pwm.Provider.IPwmProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Pwm.PwmController]]: ...
class IPwmControllerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.IPwmControllerStatics2'
    _iid_ = Guid('{44fc5b1f-f119-4bdd-97ad-f76ef986736d}')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Pwm.PwmController]: ...
class IPwmControllerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.IPwmControllerStatics3'
    _iid_ = Guid('{b2581871-0229-4344-ae3f-9b7cd0e66b94}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromFriendlyName(self, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Pwm.PwmController]: ...
class IPwmPin(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Pwm.IPwmPin'
    _iid_ = Guid('{22972dc8-c6cf-4821-b7f9-c6454fb6af79}')
    @winrt_commethod(6)
    def get_Controller(self) -> win32more.Windows.Devices.Pwm.PwmController: ...
    @winrt_commethod(7)
    def GetActiveDutyCyclePercentage(self) -> Double: ...
    @winrt_commethod(8)
    def SetActiveDutyCyclePercentage(self, dutyCyclePercentage: Double) -> Void: ...
    @winrt_commethod(9)
    def get_Polarity(self) -> win32more.Windows.Devices.Pwm.PwmPulsePolarity: ...
    @winrt_commethod(10)
    def put_Polarity(self, value: win32more.Windows.Devices.Pwm.PwmPulsePolarity) -> Void: ...
    @winrt_commethod(11)
    def Start(self) -> Void: ...
    @winrt_commethod(12)
    def Stop(self) -> Void: ...
    @winrt_commethod(13)
    def get_IsStarted(self) -> Boolean: ...
    Controller = property(get_Controller, None)
    IsStarted = property(get_IsStarted, None)
    Polarity = property(get_Polarity, put_Polarity)
class PwmController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Pwm.IPwmController
    _classid_ = 'Windows.Devices.Pwm.PwmController'
    @winrt_mixinmethod
    def get_PinCount(self: win32more.Windows.Devices.Pwm.IPwmController) -> Int32: ...
    @winrt_mixinmethod
    def get_ActualFrequency(self: win32more.Windows.Devices.Pwm.IPwmController) -> Double: ...
    @winrt_mixinmethod
    def SetDesiredFrequency(self: win32more.Windows.Devices.Pwm.IPwmController, desiredFrequency: Double) -> Double: ...
    @winrt_mixinmethod
    def get_MinFrequency(self: win32more.Windows.Devices.Pwm.IPwmController) -> Double: ...
    @winrt_mixinmethod
    def get_MaxFrequency(self: win32more.Windows.Devices.Pwm.IPwmController) -> Double: ...
    @winrt_mixinmethod
    def OpenPin(self: win32more.Windows.Devices.Pwm.IPwmController, pinNumber: Int32) -> win32more.Windows.Devices.Pwm.PwmPin: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Pwm.IPwmControllerStatics3) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromFriendlyName(cls: win32more.Windows.Devices.Pwm.IPwmControllerStatics3, friendlyName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Pwm.IPwmControllerStatics3, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Pwm.PwmController]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: win32more.Windows.Devices.Pwm.IPwmControllerStatics2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Pwm.PwmController]: ...
    @winrt_classmethod
    def GetControllersAsync(cls: win32more.Windows.Devices.Pwm.IPwmControllerStatics, provider: win32more.Windows.Devices.Pwm.Provider.IPwmProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Pwm.PwmController]]: ...
    ActualFrequency = property(get_ActualFrequency, None)
    MaxFrequency = property(get_MaxFrequency, None)
    MinFrequency = property(get_MinFrequency, None)
    PinCount = property(get_PinCount, None)
class PwmPin(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Pwm.IPwmPin
    _classid_ = 'Windows.Devices.Pwm.PwmPin'
    @winrt_mixinmethod
    def get_Controller(self: win32more.Windows.Devices.Pwm.IPwmPin) -> win32more.Windows.Devices.Pwm.PwmController: ...
    @winrt_mixinmethod
    def GetActiveDutyCyclePercentage(self: win32more.Windows.Devices.Pwm.IPwmPin) -> Double: ...
    @winrt_mixinmethod
    def SetActiveDutyCyclePercentage(self: win32more.Windows.Devices.Pwm.IPwmPin, dutyCyclePercentage: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Polarity(self: win32more.Windows.Devices.Pwm.IPwmPin) -> win32more.Windows.Devices.Pwm.PwmPulsePolarity: ...
    @winrt_mixinmethod
    def put_Polarity(self: win32more.Windows.Devices.Pwm.IPwmPin, value: win32more.Windows.Devices.Pwm.PwmPulsePolarity) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Pwm.IPwmPin) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Pwm.IPwmPin) -> Void: ...
    @winrt_mixinmethod
    def get_IsStarted(self: win32more.Windows.Devices.Pwm.IPwmPin) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Controller = property(get_Controller, None)
    IsStarted = property(get_IsStarted, None)
    Polarity = property(get_Polarity, put_Polarity)
class PwmPulsePolarity(Enum, Int32):
    ActiveHigh = 0
    ActiveLow = 1


make_ready(__name__)
