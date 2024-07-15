from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Gpio.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class GpioPinProviderValueChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Gpio.Provider.IGpioPinProviderValueChangedEventArgs
    _classid_ = 'Windows.Devices.Gpio.Provider.GpioPinProviderValueChangedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Gpio.Provider.GpioPinProviderValueChangedEventArgs.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Gpio.Provider.IGpioPinProviderValueChangedEventArgsFactory, edge: win32more.Windows.Devices.Gpio.Provider.ProviderGpioPinEdge) -> win32more.Windows.Devices.Gpio.Provider.GpioPinProviderValueChangedEventArgs: ...
    @winrt_mixinmethod
    def get_Edge(self: win32more.Windows.Devices.Gpio.Provider.IGpioPinProviderValueChangedEventArgs) -> win32more.Windows.Devices.Gpio.Provider.ProviderGpioPinEdge: ...
    Edge = property(get_Edge, None)
class IGpioControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.Provider.IGpioControllerProvider'
    _iid_ = Guid('{ad11cec7-19ea-4b21-874f-b91aed4a25db}')
    @winrt_commethod(6)
    def get_PinCount(self) -> Int32: ...
    @winrt_commethod(7)
    def OpenPinProvider(self, pin: Int32, sharingMode: win32more.Windows.Devices.Gpio.Provider.ProviderGpioSharingMode) -> win32more.Windows.Devices.Gpio.Provider.IGpioPinProvider: ...
    PinCount = property(get_PinCount, None)
class IGpioPinProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.Provider.IGpioPinProvider'
    _iid_ = Guid('{42344cb7-6abc-40ff-9ce7-73b85301b900}')
    @winrt_commethod(6)
    def add_ValueChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Gpio.Provider.IGpioPinProvider, win32more.Windows.Devices.Gpio.Provider.GpioPinProviderValueChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ValueChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_DebounceTimeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_DebounceTimeout(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_PinNumber(self) -> Int32: ...
    @winrt_commethod(11)
    def get_SharingMode(self) -> win32more.Windows.Devices.Gpio.Provider.ProviderGpioSharingMode: ...
    @winrt_commethod(12)
    def IsDriveModeSupported(self, driveMode: win32more.Windows.Devices.Gpio.Provider.ProviderGpioPinDriveMode) -> Boolean: ...
    @winrt_commethod(13)
    def GetDriveMode(self) -> win32more.Windows.Devices.Gpio.Provider.ProviderGpioPinDriveMode: ...
    @winrt_commethod(14)
    def SetDriveMode(self, value: win32more.Windows.Devices.Gpio.Provider.ProviderGpioPinDriveMode) -> Void: ...
    @winrt_commethod(15)
    def Write(self, value: win32more.Windows.Devices.Gpio.Provider.ProviderGpioPinValue) -> Void: ...
    @winrt_commethod(16)
    def Read(self) -> win32more.Windows.Devices.Gpio.Provider.ProviderGpioPinValue: ...
    DebounceTimeout = property(get_DebounceTimeout, put_DebounceTimeout)
    PinNumber = property(get_PinNumber, None)
    SharingMode = property(get_SharingMode, None)
    ValueChanged = event()
class IGpioPinProviderValueChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.Provider.IGpioPinProviderValueChangedEventArgs'
    _iid_ = Guid('{32a6d6f2-3d5b-44cd-8fbe-13a69f2edb24}')
    @winrt_commethod(6)
    def get_Edge(self) -> win32more.Windows.Devices.Gpio.Provider.ProviderGpioPinEdge: ...
    Edge = property(get_Edge, None)
class IGpioPinProviderValueChangedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.Provider.IGpioPinProviderValueChangedEventArgsFactory'
    _iid_ = Guid('{3ecb0b59-568c-4392-b24a-8a59a902b1f1}')
    @winrt_commethod(6)
    def Create(self, edge: win32more.Windows.Devices.Gpio.Provider.ProviderGpioPinEdge) -> win32more.Windows.Devices.Gpio.Provider.GpioPinProviderValueChangedEventArgs: ...
class IGpioProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.Provider.IGpioProvider'
    _iid_ = Guid('{44e82707-08ca-434a-afe0-d61580446f7e}')
    @winrt_commethod(6)
    def GetControllers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Gpio.Provider.IGpioControllerProvider]: ...
class ProviderGpioPinDriveMode(Enum, Int32):
    Input = 0
    Output = 1
    InputPullUp = 2
    InputPullDown = 3
    OutputOpenDrain = 4
    OutputOpenDrainPullUp = 5
    OutputOpenSource = 6
    OutputOpenSourcePullDown = 7
class ProviderGpioPinEdge(Enum, Int32):
    FallingEdge = 0
    RisingEdge = 1
class ProviderGpioPinValue(Enum, Int32):
    Low = 0
    High = 1
class ProviderGpioSharingMode(Enum, Int32):
    Exclusive = 0
    SharedReadOnly = 1


make_ready(__name__)
