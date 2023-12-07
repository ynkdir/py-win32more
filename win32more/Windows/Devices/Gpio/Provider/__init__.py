from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Gpio.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
class GpioPinProviderValueChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Gpio.Provider.IGpioPinProviderValueChangedEventArgs
    _classid_ = 'Windows.Devices.Gpio.Provider.GpioPinProviderValueChangedEventArgs'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.Devices.Gpio.Provider.GpioPinProviderValueChangedEventArgs.Create(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
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
ProviderGpioPinDriveMode = Int32
ProviderGpioPinDriveMode_Input: ProviderGpioPinDriveMode = 0
ProviderGpioPinDriveMode_Output: ProviderGpioPinDriveMode = 1
ProviderGpioPinDriveMode_InputPullUp: ProviderGpioPinDriveMode = 2
ProviderGpioPinDriveMode_InputPullDown: ProviderGpioPinDriveMode = 3
ProviderGpioPinDriveMode_OutputOpenDrain: ProviderGpioPinDriveMode = 4
ProviderGpioPinDriveMode_OutputOpenDrainPullUp: ProviderGpioPinDriveMode = 5
ProviderGpioPinDriveMode_OutputOpenSource: ProviderGpioPinDriveMode = 6
ProviderGpioPinDriveMode_OutputOpenSourcePullDown: ProviderGpioPinDriveMode = 7
ProviderGpioPinEdge = Int32
ProviderGpioPinEdge_FallingEdge: ProviderGpioPinEdge = 0
ProviderGpioPinEdge_RisingEdge: ProviderGpioPinEdge = 1
ProviderGpioPinValue = Int32
ProviderGpioPinValue_Low: ProviderGpioPinValue = 0
ProviderGpioPinValue_High: ProviderGpioPinValue = 1
ProviderGpioSharingMode = Int32
ProviderGpioSharingMode_Exclusive: ProviderGpioSharingMode = 0
ProviderGpioSharingMode_SharedReadOnly: ProviderGpioSharingMode = 1
make_ready(__name__)
