from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Devices.Gpio
import Windows.Devices.Gpio.Provider
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class GpioChangeCount(EasyCastStructure):
    Count: UInt64
    RelativeTime: Windows.Foundation.TimeSpan
class GpioChangeCounter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.GpioChangeCounter'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Gpio.IGpioChangeCounterFactory, pin: Windows.Devices.Gpio.GpioPin) -> Windows.Devices.Gpio.GpioChangeCounter: ...
    @winrt_mixinmethod
    def put_Polarity(self: Windows.Devices.Gpio.IGpioChangeCounter, value: Windows.Devices.Gpio.GpioChangePolarity) -> Void: ...
    @winrt_mixinmethod
    def get_Polarity(self: Windows.Devices.Gpio.IGpioChangeCounter) -> Windows.Devices.Gpio.GpioChangePolarity: ...
    @winrt_mixinmethod
    def get_IsStarted(self: Windows.Devices.Gpio.IGpioChangeCounter) -> Boolean: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Gpio.IGpioChangeCounter) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Gpio.IGpioChangeCounter) -> Void: ...
    @winrt_mixinmethod
    def Read(self: Windows.Devices.Gpio.IGpioChangeCounter) -> Windows.Devices.Gpio.GpioChangeCount: ...
    @winrt_mixinmethod
    def Reset(self: Windows.Devices.Gpio.IGpioChangeCounter) -> Windows.Devices.Gpio.GpioChangeCount: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Polarity = property(get_Polarity, put_Polarity)
    IsStarted = property(get_IsStarted, None)
GpioChangePolarity = Int32
GpioChangePolarity_Falling: GpioChangePolarity = 0
GpioChangePolarity_Rising: GpioChangePolarity = 1
GpioChangePolarity_Both: GpioChangePolarity = 2
class GpioChangeReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.GpioChangeReader'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Gpio.IGpioChangeReaderFactory, pin: Windows.Devices.Gpio.GpioPin) -> Windows.Devices.Gpio.GpioChangeReader: ...
    @winrt_factorymethod
    def CreateWithCapacity(cls: Windows.Devices.Gpio.IGpioChangeReaderFactory, pin: Windows.Devices.Gpio.GpioPin, minCapacity: Int32) -> Windows.Devices.Gpio.GpioChangeReader: ...
    @winrt_mixinmethod
    def get_Capacity(self: Windows.Devices.Gpio.IGpioChangeReader) -> Int32: ...
    @winrt_mixinmethod
    def get_Length(self: Windows.Devices.Gpio.IGpioChangeReader) -> Int32: ...
    @winrt_mixinmethod
    def get_IsEmpty(self: Windows.Devices.Gpio.IGpioChangeReader) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsOverflowed(self: Windows.Devices.Gpio.IGpioChangeReader) -> Boolean: ...
    @winrt_mixinmethod
    def put_Polarity(self: Windows.Devices.Gpio.IGpioChangeReader, value: Windows.Devices.Gpio.GpioChangePolarity) -> Void: ...
    @winrt_mixinmethod
    def get_Polarity(self: Windows.Devices.Gpio.IGpioChangeReader) -> Windows.Devices.Gpio.GpioChangePolarity: ...
    @winrt_mixinmethod
    def get_IsStarted(self: Windows.Devices.Gpio.IGpioChangeReader) -> Boolean: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Gpio.IGpioChangeReader) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Gpio.IGpioChangeReader) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Devices.Gpio.IGpioChangeReader) -> Void: ...
    @winrt_mixinmethod
    def GetNextItem(self: Windows.Devices.Gpio.IGpioChangeReader) -> Windows.Devices.Gpio.GpioChangeRecord: ...
    @winrt_mixinmethod
    def PeekNextItem(self: Windows.Devices.Gpio.IGpioChangeReader) -> Windows.Devices.Gpio.GpioChangeRecord: ...
    @winrt_mixinmethod
    def GetAllItems(self: Windows.Devices.Gpio.IGpioChangeReader) -> Windows.Foundation.Collections.IVector[Windows.Devices.Gpio.GpioChangeRecord]: ...
    @winrt_mixinmethod
    def WaitForItemsAsync(self: Windows.Devices.Gpio.IGpioChangeReader, count: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Capacity = property(get_Capacity, None)
    Length = property(get_Length, None)
    IsEmpty = property(get_IsEmpty, None)
    IsOverflowed = property(get_IsOverflowed, None)
    Polarity = property(get_Polarity, put_Polarity)
    IsStarted = property(get_IsStarted, None)
class GpioChangeRecord(EasyCastStructure):
    RelativeTime: Windows.Foundation.TimeSpan
    Edge: Windows.Devices.Gpio.GpioPinEdge
class GpioController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.GpioController'
    @winrt_mixinmethod
    def get_PinCount(self: Windows.Devices.Gpio.IGpioController) -> Int32: ...
    @winrt_mixinmethod
    def OpenPin(self: Windows.Devices.Gpio.IGpioController, pinNumber: Int32) -> Windows.Devices.Gpio.GpioPin: ...
    @winrt_mixinmethod
    def OpenPinWithSharingMode(self: Windows.Devices.Gpio.IGpioController, pinNumber: Int32, sharingMode: Windows.Devices.Gpio.GpioSharingMode) -> Windows.Devices.Gpio.GpioPin: ...
    @winrt_mixinmethod
    def TryOpenPin(self: Windows.Devices.Gpio.IGpioController, pinNumber: Int32, sharingMode: Windows.Devices.Gpio.GpioSharingMode, pin: POINTER(Windows.Devices.Gpio.GpioPin), openStatus: POINTER(Windows.Devices.Gpio.GpioOpenStatus)) -> Boolean: ...
    @winrt_classmethod
    def GetControllersAsync(cls: Windows.Devices.Gpio.IGpioControllerStatics2, provider: Windows.Devices.Gpio.Provider.IGpioProvider) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Gpio.GpioController]]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.Gpio.IGpioControllerStatics2) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Gpio.GpioController]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Gpio.IGpioControllerStatics) -> Windows.Devices.Gpio.GpioController: ...
    PinCount = property(get_PinCount, None)
GpioOpenStatus = Int32
GpioOpenStatus_PinOpened: GpioOpenStatus = 0
GpioOpenStatus_PinUnavailable: GpioOpenStatus = 1
GpioOpenStatus_SharingViolation: GpioOpenStatus = 2
GpioOpenStatus_MuxingConflict: GpioOpenStatus = 3
GpioOpenStatus_UnknownError: GpioOpenStatus = 4
class GpioPin(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.GpioPin'
    @winrt_mixinmethod
    def add_ValueChanged(self: Windows.Devices.Gpio.IGpioPin, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Gpio.GpioPin, Windows.Devices.Gpio.GpioPinValueChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ValueChanged(self: Windows.Devices.Gpio.IGpioPin, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DebounceTimeout(self: Windows.Devices.Gpio.IGpioPin) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_DebounceTimeout(self: Windows.Devices.Gpio.IGpioPin, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_PinNumber(self: Windows.Devices.Gpio.IGpioPin) -> Int32: ...
    @winrt_mixinmethod
    def get_SharingMode(self: Windows.Devices.Gpio.IGpioPin) -> Windows.Devices.Gpio.GpioSharingMode: ...
    @winrt_mixinmethod
    def IsDriveModeSupported(self: Windows.Devices.Gpio.IGpioPin, driveMode: Windows.Devices.Gpio.GpioPinDriveMode) -> Boolean: ...
    @winrt_mixinmethod
    def GetDriveMode(self: Windows.Devices.Gpio.IGpioPin) -> Windows.Devices.Gpio.GpioPinDriveMode: ...
    @winrt_mixinmethod
    def SetDriveMode(self: Windows.Devices.Gpio.IGpioPin, value: Windows.Devices.Gpio.GpioPinDriveMode) -> Void: ...
    @winrt_mixinmethod
    def Write(self: Windows.Devices.Gpio.IGpioPin, value: Windows.Devices.Gpio.GpioPinValue) -> Void: ...
    @winrt_mixinmethod
    def Read(self: Windows.Devices.Gpio.IGpioPin) -> Windows.Devices.Gpio.GpioPinValue: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Gpio.GpioPinValueChangedEventArgs'
    @winrt_mixinmethod
    def get_Edge(self: Windows.Devices.Gpio.IGpioPinValueChangedEventArgs) -> Windows.Devices.Gpio.GpioPinEdge: ...
    Edge = property(get_Edge, None)
GpioSharingMode = Int32
GpioSharingMode_Exclusive: GpioSharingMode = 0
GpioSharingMode_SharedReadOnly: GpioSharingMode = 1
class IGpioChangeCounter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cb5ec0de-6801-43ff-80-3d-45-76-62-8a-8b-26')
    @winrt_commethod(6)
    def put_Polarity(self, value: Windows.Devices.Gpio.GpioChangePolarity) -> Void: ...
    @winrt_commethod(7)
    def get_Polarity(self) -> Windows.Devices.Gpio.GpioChangePolarity: ...
    @winrt_commethod(8)
    def get_IsStarted(self) -> Boolean: ...
    @winrt_commethod(9)
    def Start(self) -> Void: ...
    @winrt_commethod(10)
    def Stop(self) -> Void: ...
    @winrt_commethod(11)
    def Read(self) -> Windows.Devices.Gpio.GpioChangeCount: ...
    @winrt_commethod(12)
    def Reset(self) -> Windows.Devices.Gpio.GpioChangeCount: ...
    Polarity = property(get_Polarity, put_Polarity)
    IsStarted = property(get_IsStarted, None)
class IGpioChangeCounterFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('147d94b6-0a9e-410c-b4-fa-f8-9f-40-52-08-4d')
    @winrt_commethod(6)
    def Create(self, pin: Windows.Devices.Gpio.GpioPin) -> Windows.Devices.Gpio.GpioChangeCounter: ...
class IGpioChangeReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0abc885f-e031-48e8-85-90-70-de-78-36-3c-6d')
    @winrt_commethod(6)
    def get_Capacity(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Length(self) -> Int32: ...
    @winrt_commethod(8)
    def get_IsEmpty(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsOverflowed(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_Polarity(self, value: Windows.Devices.Gpio.GpioChangePolarity) -> Void: ...
    @winrt_commethod(11)
    def get_Polarity(self) -> Windows.Devices.Gpio.GpioChangePolarity: ...
    @winrt_commethod(12)
    def get_IsStarted(self) -> Boolean: ...
    @winrt_commethod(13)
    def Start(self) -> Void: ...
    @winrt_commethod(14)
    def Stop(self) -> Void: ...
    @winrt_commethod(15)
    def Clear(self) -> Void: ...
    @winrt_commethod(16)
    def GetNextItem(self) -> Windows.Devices.Gpio.GpioChangeRecord: ...
    @winrt_commethod(17)
    def PeekNextItem(self) -> Windows.Devices.Gpio.GpioChangeRecord: ...
    @winrt_commethod(18)
    def GetAllItems(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Gpio.GpioChangeRecord]: ...
    @winrt_commethod(19)
    def WaitForItemsAsync(self, count: Int32) -> Windows.Foundation.IAsyncAction: ...
    Capacity = property(get_Capacity, None)
    Length = property(get_Length, None)
    IsEmpty = property(get_IsEmpty, None)
    IsOverflowed = property(get_IsOverflowed, None)
    Polarity = property(get_Polarity, put_Polarity)
    IsStarted = property(get_IsStarted, None)
class IGpioChangeReaderFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a9598ef3-390e-441a-9d-1c-e8-de-0b-2d-f0-df')
    @winrt_commethod(6)
    def Create(self, pin: Windows.Devices.Gpio.GpioPin) -> Windows.Devices.Gpio.GpioChangeReader: ...
    @winrt_commethod(7)
    def CreateWithCapacity(self, pin: Windows.Devices.Gpio.GpioPin, minCapacity: Int32) -> Windows.Devices.Gpio.GpioChangeReader: ...
class IGpioController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('284012e3-7461-469c-a8-bc-61-d6-9d-08-a5-3c')
    @winrt_commethod(6)
    def get_PinCount(self) -> Int32: ...
    @winrt_commethod(7)
    def OpenPin(self, pinNumber: Int32) -> Windows.Devices.Gpio.GpioPin: ...
    @winrt_commethod(8)
    def OpenPinWithSharingMode(self, pinNumber: Int32, sharingMode: Windows.Devices.Gpio.GpioSharingMode) -> Windows.Devices.Gpio.GpioPin: ...
    @winrt_commethod(9)
    def TryOpenPin(self, pinNumber: Int32, sharingMode: Windows.Devices.Gpio.GpioSharingMode, pin: POINTER(Windows.Devices.Gpio.GpioPin), openStatus: POINTER(Windows.Devices.Gpio.GpioOpenStatus)) -> Boolean: ...
    PinCount = property(get_PinCount, None)
class IGpioControllerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2ed6f42e-7af7-4116-95-33-c4-3d-99-a1-fb-64')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Gpio.GpioController: ...
class IGpioControllerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('912b7d20-6ca4-4106-a3-73-ff-fd-34-6b-0e-5b')
    @winrt_commethod(6)
    def GetControllersAsync(self, provider: Windows.Devices.Gpio.Provider.IGpioProvider) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Gpio.GpioController]]: ...
    @winrt_commethod(7)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Gpio.GpioController]: ...
class IGpioPin(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('11d9b087-afae-4790-9e-e9-e0-ea-c9-42-d2-01')
    @winrt_commethod(6)
    def add_ValueChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Gpio.GpioPin, Windows.Devices.Gpio.GpioPinValueChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ValueChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_DebounceTimeout(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_DebounceTimeout(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_PinNumber(self) -> Int32: ...
    @winrt_commethod(11)
    def get_SharingMode(self) -> Windows.Devices.Gpio.GpioSharingMode: ...
    @winrt_commethod(12)
    def IsDriveModeSupported(self, driveMode: Windows.Devices.Gpio.GpioPinDriveMode) -> Boolean: ...
    @winrt_commethod(13)
    def GetDriveMode(self) -> Windows.Devices.Gpio.GpioPinDriveMode: ...
    @winrt_commethod(14)
    def SetDriveMode(self, value: Windows.Devices.Gpio.GpioPinDriveMode) -> Void: ...
    @winrt_commethod(15)
    def Write(self, value: Windows.Devices.Gpio.GpioPinValue) -> Void: ...
    @winrt_commethod(16)
    def Read(self) -> Windows.Devices.Gpio.GpioPinValue: ...
    DebounceTimeout = property(get_DebounceTimeout, put_DebounceTimeout)
    PinNumber = property(get_PinNumber, None)
    SharingMode = property(get_SharingMode, None)
class IGpioPinValueChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3137aae1-703d-4059-bd-24-b5-b2-5d-ff-b8-4e')
    @winrt_commethod(6)
    def get_Edge(self) -> Windows.Devices.Gpio.GpioPinEdge: ...
    Edge = property(get_Edge, None)
make_head(_module, 'GpioChangeCount')
make_head(_module, 'GpioChangeCounter')
make_head(_module, 'GpioChangeReader')
make_head(_module, 'GpioChangeRecord')
make_head(_module, 'GpioController')
make_head(_module, 'GpioPin')
make_head(_module, 'GpioPinValueChangedEventArgs')
make_head(_module, 'IGpioChangeCounter')
make_head(_module, 'IGpioChangeCounterFactory')
make_head(_module, 'IGpioChangeReader')
make_head(_module, 'IGpioChangeReaderFactory')
make_head(_module, 'IGpioController')
make_head(_module, 'IGpioControllerStatics')
make_head(_module, 'IGpioControllerStatics2')
make_head(_module, 'IGpioPin')
make_head(_module, 'IGpioPinValueChangedEventArgs')
