from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import Annotated, Generic, K, MulticastDelegate, SZArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Gpio
import win32more.Windows.Devices.Gpio.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class GpioChangeCount(EasyCastStructure):
    Count: UInt64
    RelativeTime: win32more.Windows.Foundation.TimeSpan
class GpioChangeCounter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Gpio.IGpioChangeCounter
    _classid_ = 'Windows.Devices.Gpio.GpioChangeCounter'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.Devices.Gpio.GpioChangeCounter.Create(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Gpio.IGpioChangeCounterFactory, pin: win32more.Windows.Devices.Gpio.GpioPin) -> win32more.Windows.Devices.Gpio.GpioChangeCounter: ...
    @winrt_mixinmethod
    def put_Polarity(self: win32more.Windows.Devices.Gpio.IGpioChangeCounter, value: win32more.Windows.Devices.Gpio.GpioChangePolarity) -> Void: ...
    @winrt_mixinmethod
    def get_Polarity(self: win32more.Windows.Devices.Gpio.IGpioChangeCounter) -> win32more.Windows.Devices.Gpio.GpioChangePolarity: ...
    @winrt_mixinmethod
    def get_IsStarted(self: win32more.Windows.Devices.Gpio.IGpioChangeCounter) -> Boolean: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Gpio.IGpioChangeCounter) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Gpio.IGpioChangeCounter) -> Void: ...
    @winrt_mixinmethod
    def Read(self: win32more.Windows.Devices.Gpio.IGpioChangeCounter) -> win32more.Windows.Devices.Gpio.GpioChangeCount: ...
    @winrt_mixinmethod
    def Reset(self: win32more.Windows.Devices.Gpio.IGpioChangeCounter) -> win32more.Windows.Devices.Gpio.GpioChangeCount: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Polarity = property(get_Polarity, put_Polarity)
    IsStarted = property(get_IsStarted, None)
GpioChangePolarity = Int32
GpioChangePolarity_Falling: GpioChangePolarity = 0
GpioChangePolarity_Rising: GpioChangePolarity = 1
GpioChangePolarity_Both: GpioChangePolarity = 2
class GpioChangeReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Gpio.IGpioChangeReader
    _classid_ = 'Windows.Devices.Gpio.GpioChangeReader'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 1:
            return win32more.Windows.Devices.Gpio.GpioChangeReader.Create(*args)
        elif len(args) == 2:
            return win32more.Windows.Devices.Gpio.GpioChangeReader.CreateWithCapacity(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Gpio.IGpioChangeReaderFactory, pin: win32more.Windows.Devices.Gpio.GpioPin) -> win32more.Windows.Devices.Gpio.GpioChangeReader: ...
    @winrt_factorymethod
    def CreateWithCapacity(cls: win32more.Windows.Devices.Gpio.IGpioChangeReaderFactory, pin: win32more.Windows.Devices.Gpio.GpioPin, minCapacity: Int32) -> win32more.Windows.Devices.Gpio.GpioChangeReader: ...
    @winrt_mixinmethod
    def get_Capacity(self: win32more.Windows.Devices.Gpio.IGpioChangeReader) -> Int32: ...
    @winrt_mixinmethod
    def get_Length(self: win32more.Windows.Devices.Gpio.IGpioChangeReader) -> Int32: ...
    @winrt_mixinmethod
    def get_IsEmpty(self: win32more.Windows.Devices.Gpio.IGpioChangeReader) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsOverflowed(self: win32more.Windows.Devices.Gpio.IGpioChangeReader) -> Boolean: ...
    @winrt_mixinmethod
    def put_Polarity(self: win32more.Windows.Devices.Gpio.IGpioChangeReader, value: win32more.Windows.Devices.Gpio.GpioChangePolarity) -> Void: ...
    @winrt_mixinmethod
    def get_Polarity(self: win32more.Windows.Devices.Gpio.IGpioChangeReader) -> win32more.Windows.Devices.Gpio.GpioChangePolarity: ...
    @winrt_mixinmethod
    def get_IsStarted(self: win32more.Windows.Devices.Gpio.IGpioChangeReader) -> Boolean: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Gpio.IGpioChangeReader) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Gpio.IGpioChangeReader) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Devices.Gpio.IGpioChangeReader) -> Void: ...
    @winrt_mixinmethod
    def GetNextItem(self: win32more.Windows.Devices.Gpio.IGpioChangeReader) -> win32more.Windows.Devices.Gpio.GpioChangeRecord: ...
    @winrt_mixinmethod
    def PeekNextItem(self: win32more.Windows.Devices.Gpio.IGpioChangeReader) -> win32more.Windows.Devices.Gpio.GpioChangeRecord: ...
    @winrt_mixinmethod
    def GetAllItems(self: win32more.Windows.Devices.Gpio.IGpioChangeReader) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Gpio.GpioChangeRecord]: ...
    @winrt_mixinmethod
    def WaitForItemsAsync(self: win32more.Windows.Devices.Gpio.IGpioChangeReader, count: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Capacity = property(get_Capacity, None)
    Length = property(get_Length, None)
    IsEmpty = property(get_IsEmpty, None)
    IsOverflowed = property(get_IsOverflowed, None)
    Polarity = property(get_Polarity, put_Polarity)
    IsStarted = property(get_IsStarted, None)
class GpioChangeRecord(EasyCastStructure):
    RelativeTime: win32more.Windows.Foundation.TimeSpan
    Edge: win32more.Windows.Devices.Gpio.GpioPinEdge
class GpioController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Gpio.IGpioController
    _classid_ = 'Windows.Devices.Gpio.GpioController'
    @winrt_mixinmethod
    def get_PinCount(self: win32more.Windows.Devices.Gpio.IGpioController) -> Int32: ...
    @winrt_mixinmethod
    def OpenPin(self: win32more.Windows.Devices.Gpio.IGpioController, pinNumber: Int32) -> win32more.Windows.Devices.Gpio.GpioPin: ...
    @winrt_mixinmethod
    def OpenPinWithSharingMode(self: win32more.Windows.Devices.Gpio.IGpioController, pinNumber: Int32, sharingMode: win32more.Windows.Devices.Gpio.GpioSharingMode) -> win32more.Windows.Devices.Gpio.GpioPin: ...
    @winrt_mixinmethod
    def TryOpenPin(self: win32more.Windows.Devices.Gpio.IGpioController, pinNumber: Int32, sharingMode: win32more.Windows.Devices.Gpio.GpioSharingMode, pin: POINTER(win32more.Windows.Devices.Gpio.GpioPin), openStatus: POINTER(win32more.Windows.Devices.Gpio.GpioOpenStatus)) -> Boolean: ...
    @winrt_classmethod
    def GetControllersAsync(cls: win32more.Windows.Devices.Gpio.IGpioControllerStatics2, provider: win32more.Windows.Devices.Gpio.Provider.IGpioProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Gpio.GpioController]]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: win32more.Windows.Devices.Gpio.IGpioControllerStatics2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Gpio.GpioController]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Devices.Gpio.IGpioControllerStatics) -> win32more.Windows.Devices.Gpio.GpioController: ...
    PinCount = property(get_PinCount, None)
GpioOpenStatus = Int32
GpioOpenStatus_PinOpened: GpioOpenStatus = 0
GpioOpenStatus_PinUnavailable: GpioOpenStatus = 1
GpioOpenStatus_SharingViolation: GpioOpenStatus = 2
GpioOpenStatus_MuxingConflict: GpioOpenStatus = 3
GpioOpenStatus_UnknownError: GpioOpenStatus = 4
class GpioPin(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Gpio.IGpioPin
    _classid_ = 'Windows.Devices.Gpio.GpioPin'
    @winrt_mixinmethod
    def add_ValueChanged(self: win32more.Windows.Devices.Gpio.IGpioPin, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Gpio.GpioPin, win32more.Windows.Devices.Gpio.GpioPinValueChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ValueChanged(self: win32more.Windows.Devices.Gpio.IGpioPin, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DebounceTimeout(self: win32more.Windows.Devices.Gpio.IGpioPin) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DebounceTimeout(self: win32more.Windows.Devices.Gpio.IGpioPin, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_PinNumber(self: win32more.Windows.Devices.Gpio.IGpioPin) -> Int32: ...
    @winrt_mixinmethod
    def get_SharingMode(self: win32more.Windows.Devices.Gpio.IGpioPin) -> win32more.Windows.Devices.Gpio.GpioSharingMode: ...
    @winrt_mixinmethod
    def IsDriveModeSupported(self: win32more.Windows.Devices.Gpio.IGpioPin, driveMode: win32more.Windows.Devices.Gpio.GpioPinDriveMode) -> Boolean: ...
    @winrt_mixinmethod
    def GetDriveMode(self: win32more.Windows.Devices.Gpio.IGpioPin) -> win32more.Windows.Devices.Gpio.GpioPinDriveMode: ...
    @winrt_mixinmethod
    def SetDriveMode(self: win32more.Windows.Devices.Gpio.IGpioPin, value: win32more.Windows.Devices.Gpio.GpioPinDriveMode) -> Void: ...
    @winrt_mixinmethod
    def Write(self: win32more.Windows.Devices.Gpio.IGpioPin, value: win32more.Windows.Devices.Gpio.GpioPinValue) -> Void: ...
    @winrt_mixinmethod
    def Read(self: win32more.Windows.Devices.Gpio.IGpioPin) -> win32more.Windows.Devices.Gpio.GpioPinValue: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    DebounceTimeout = property(get_DebounceTimeout, put_DebounceTimeout)
    PinNumber = property(get_PinNumber, None)
    SharingMode = property(get_SharingMode, None)
GpioPinDriveMode = Int32
GpioPinDriveMode_Input: GpioPinDriveMode = 0
GpioPinDriveMode_Output: GpioPinDriveMode = 1
GpioPinDriveMode_InputPullUp: GpioPinDriveMode = 2
GpioPinDriveMode_InputPullDown: GpioPinDriveMode = 3
GpioPinDriveMode_OutputOpenDrain: GpioPinDriveMode = 4
GpioPinDriveMode_OutputOpenDrainPullUp: GpioPinDriveMode = 5
GpioPinDriveMode_OutputOpenSource: GpioPinDriveMode = 6
GpioPinDriveMode_OutputOpenSourcePullDown: GpioPinDriveMode = 7
GpioPinEdge = Int32
GpioPinEdge_FallingEdge: GpioPinEdge = 0
GpioPinEdge_RisingEdge: GpioPinEdge = 1
GpioPinValue = Int32
GpioPinValue_Low: GpioPinValue = 0
GpioPinValue_High: GpioPinValue = 1
class GpioPinValueChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Gpio.IGpioPinValueChangedEventArgs
    _classid_ = 'Windows.Devices.Gpio.GpioPinValueChangedEventArgs'
    @winrt_mixinmethod
    def get_Edge(self: win32more.Windows.Devices.Gpio.IGpioPinValueChangedEventArgs) -> win32more.Windows.Devices.Gpio.GpioPinEdge: ...
    Edge = property(get_Edge, None)
GpioSharingMode = Int32
GpioSharingMode_Exclusive: GpioSharingMode = 0
GpioSharingMode_SharedReadOnly: GpioSharingMode = 1
class IGpioChangeCounter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.IGpioChangeCounter'
    _iid_ = Guid('{cb5ec0de-6801-43ff-803d-4576628a8b26}')
    @winrt_commethod(6)
    def put_Polarity(self, value: win32more.Windows.Devices.Gpio.GpioChangePolarity) -> Void: ...
    @winrt_commethod(7)
    def get_Polarity(self) -> win32more.Windows.Devices.Gpio.GpioChangePolarity: ...
    @winrt_commethod(8)
    def get_IsStarted(self) -> Boolean: ...
    @winrt_commethod(9)
    def Start(self) -> Void: ...
    @winrt_commethod(10)
    def Stop(self) -> Void: ...
    @winrt_commethod(11)
    def Read(self) -> win32more.Windows.Devices.Gpio.GpioChangeCount: ...
    @winrt_commethod(12)
    def Reset(self) -> win32more.Windows.Devices.Gpio.GpioChangeCount: ...
    Polarity = property(get_Polarity, put_Polarity)
    IsStarted = property(get_IsStarted, None)
class IGpioChangeCounterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.IGpioChangeCounterFactory'
    _iid_ = Guid('{147d94b6-0a9e-410c-b4fa-f89f4052084d}')
    @winrt_commethod(6)
    def Create(self, pin: win32more.Windows.Devices.Gpio.GpioPin) -> win32more.Windows.Devices.Gpio.GpioChangeCounter: ...
class IGpioChangeReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.IGpioChangeReader'
    _iid_ = Guid('{0abc885f-e031-48e8-8590-70de78363c6d}')
    @winrt_commethod(6)
    def get_Capacity(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Length(self) -> Int32: ...
    @winrt_commethod(8)
    def get_IsEmpty(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsOverflowed(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_Polarity(self, value: win32more.Windows.Devices.Gpio.GpioChangePolarity) -> Void: ...
    @winrt_commethod(11)
    def get_Polarity(self) -> win32more.Windows.Devices.Gpio.GpioChangePolarity: ...
    @winrt_commethod(12)
    def get_IsStarted(self) -> Boolean: ...
    @winrt_commethod(13)
    def Start(self) -> Void: ...
    @winrt_commethod(14)
    def Stop(self) -> Void: ...
    @winrt_commethod(15)
    def Clear(self) -> Void: ...
    @winrt_commethod(16)
    def GetNextItem(self) -> win32more.Windows.Devices.Gpio.GpioChangeRecord: ...
    @winrt_commethod(17)
    def PeekNextItem(self) -> win32more.Windows.Devices.Gpio.GpioChangeRecord: ...
    @winrt_commethod(18)
    def GetAllItems(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Gpio.GpioChangeRecord]: ...
    @winrt_commethod(19)
    def WaitForItemsAsync(self, count: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    Capacity = property(get_Capacity, None)
    Length = property(get_Length, None)
    IsEmpty = property(get_IsEmpty, None)
    IsOverflowed = property(get_IsOverflowed, None)
    Polarity = property(get_Polarity, put_Polarity)
    IsStarted = property(get_IsStarted, None)
class IGpioChangeReaderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.IGpioChangeReaderFactory'
    _iid_ = Guid('{a9598ef3-390e-441a-9d1c-e8de0b2df0df}')
    @winrt_commethod(6)
    def Create(self, pin: win32more.Windows.Devices.Gpio.GpioPin) -> win32more.Windows.Devices.Gpio.GpioChangeReader: ...
    @winrt_commethod(7)
    def CreateWithCapacity(self, pin: win32more.Windows.Devices.Gpio.GpioPin, minCapacity: Int32) -> win32more.Windows.Devices.Gpio.GpioChangeReader: ...
class IGpioController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.IGpioController'
    _iid_ = Guid('{284012e3-7461-469c-a8bc-61d69d08a53c}')
    @winrt_commethod(6)
    def get_PinCount(self) -> Int32: ...
    @winrt_commethod(7)
    def OpenPin(self, pinNumber: Int32) -> win32more.Windows.Devices.Gpio.GpioPin: ...
    @winrt_commethod(8)
    def OpenPinWithSharingMode(self, pinNumber: Int32, sharingMode: win32more.Windows.Devices.Gpio.GpioSharingMode) -> win32more.Windows.Devices.Gpio.GpioPin: ...
    @winrt_commethod(9)
    def TryOpenPin(self, pinNumber: Int32, sharingMode: win32more.Windows.Devices.Gpio.GpioSharingMode, pin: POINTER(win32more.Windows.Devices.Gpio.GpioPin), openStatus: POINTER(win32more.Windows.Devices.Gpio.GpioOpenStatus)) -> Boolean: ...
    PinCount = property(get_PinCount, None)
class IGpioControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.IGpioControllerStatics'
    _iid_ = Guid('{2ed6f42e-7af7-4116-9533-c43d99a1fb64}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Devices.Gpio.GpioController: ...
class IGpioControllerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.IGpioControllerStatics2'
    _iid_ = Guid('{912b7d20-6ca4-4106-a373-fffd346b0e5b}')
    @winrt_commethod(6)
    def GetControllersAsync(self, provider: win32more.Windows.Devices.Gpio.Provider.IGpioProvider) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Gpio.GpioController]]: ...
    @winrt_commethod(7)
    def GetDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Gpio.GpioController]: ...
class IGpioPin(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.IGpioPin'
    _iid_ = Guid('{11d9b087-afae-4790-9ee9-e0eac942d201}')
    @winrt_commethod(6)
    def add_ValueChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Gpio.GpioPin, win32more.Windows.Devices.Gpio.GpioPinValueChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ValueChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_DebounceTimeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_DebounceTimeout(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_PinNumber(self) -> Int32: ...
    @winrt_commethod(11)
    def get_SharingMode(self) -> win32more.Windows.Devices.Gpio.GpioSharingMode: ...
    @winrt_commethod(12)
    def IsDriveModeSupported(self, driveMode: win32more.Windows.Devices.Gpio.GpioPinDriveMode) -> Boolean: ...
    @winrt_commethod(13)
    def GetDriveMode(self) -> win32more.Windows.Devices.Gpio.GpioPinDriveMode: ...
    @winrt_commethod(14)
    def SetDriveMode(self, value: win32more.Windows.Devices.Gpio.GpioPinDriveMode) -> Void: ...
    @winrt_commethod(15)
    def Write(self, value: win32more.Windows.Devices.Gpio.GpioPinValue) -> Void: ...
    @winrt_commethod(16)
    def Read(self) -> win32more.Windows.Devices.Gpio.GpioPinValue: ...
    DebounceTimeout = property(get_DebounceTimeout, put_DebounceTimeout)
    PinNumber = property(get_PinNumber, None)
    SharingMode = property(get_SharingMode, None)
class IGpioPinValueChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.IGpioPinValueChangedEventArgs'
    _iid_ = Guid('{3137aae1-703d-4059-bd24-b5b25dffb84e}')
    @winrt_commethod(6)
    def get_Edge(self) -> win32more.Windows.Devices.Gpio.GpioPinEdge: ...
    Edge = property(get_Edge, None)


make_ready(__name__)
