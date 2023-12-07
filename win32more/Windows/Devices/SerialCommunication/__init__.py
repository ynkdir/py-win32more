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
import win32more.Windows.Devices.SerialCommunication
import win32more.Windows.Foundation
import win32more.Windows.Storage.Streams
class ErrorReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SerialCommunication.IErrorReceivedEventArgs
    _classid_ = 'Windows.Devices.SerialCommunication.ErrorReceivedEventArgs'
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.SerialCommunication.IErrorReceivedEventArgs) -> win32more.Windows.Devices.SerialCommunication.SerialError: ...
    Error = property(get_Error, None)
class IErrorReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SerialCommunication.IErrorReceivedEventArgs'
    _iid_ = Guid('{fcc6bf59-1283-4d8a-bfdf-566b33ddb28f}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Devices.SerialCommunication.SerialError: ...
    Error = property(get_Error, None)
class IPinChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SerialCommunication.IPinChangedEventArgs'
    _iid_ = Guid('{a2bf1db0-fc9c-4607-93d0-fa5e8343ee22}')
    @winrt_commethod(6)
    def get_PinChange(self) -> win32more.Windows.Devices.SerialCommunication.SerialPinChange: ...
    PinChange = property(get_PinChange, None)
class ISerialDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SerialCommunication.ISerialDevice'
    _iid_ = Guid('{e187ccc6-2210-414f-b65a-f5553a03372a}')
    @winrt_commethod(6)
    def get_BaudRate(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_BaudRate(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_BreakSignalState(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_BreakSignalState(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_BytesReceived(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_CarrierDetectState(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_ClearToSendState(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_DataBits(self) -> UInt16: ...
    @winrt_commethod(14)
    def put_DataBits(self, value: UInt16) -> Void: ...
    @winrt_commethod(15)
    def get_DataSetReadyState(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_Handshake(self) -> win32more.Windows.Devices.SerialCommunication.SerialHandshake: ...
    @winrt_commethod(17)
    def put_Handshake(self, value: win32more.Windows.Devices.SerialCommunication.SerialHandshake) -> Void: ...
    @winrt_commethod(18)
    def get_IsDataTerminalReadyEnabled(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_IsDataTerminalReadyEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_IsRequestToSendEnabled(self) -> Boolean: ...
    @winrt_commethod(21)
    def put_IsRequestToSendEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(22)
    def get_Parity(self) -> win32more.Windows.Devices.SerialCommunication.SerialParity: ...
    @winrt_commethod(23)
    def put_Parity(self, value: win32more.Windows.Devices.SerialCommunication.SerialParity) -> Void: ...
    @winrt_commethod(24)
    def get_PortName(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def get_ReadTimeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(26)
    def put_ReadTimeout(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(27)
    def get_StopBits(self) -> win32more.Windows.Devices.SerialCommunication.SerialStopBitCount: ...
    @winrt_commethod(28)
    def put_StopBits(self, value: win32more.Windows.Devices.SerialCommunication.SerialStopBitCount) -> Void: ...
    @winrt_commethod(29)
    def get_UsbVendorId(self) -> UInt16: ...
    @winrt_commethod(30)
    def get_UsbProductId(self) -> UInt16: ...
    @winrt_commethod(31)
    def get_WriteTimeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(32)
    def put_WriteTimeout(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(33)
    def get_InputStream(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(34)
    def get_OutputStream(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(35)
    def add_ErrorReceived(self, reportHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.SerialCommunication.SerialDevice, win32more.Windows.Devices.SerialCommunication.ErrorReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(36)
    def remove_ErrorReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(37)
    def add_PinChanged(self, reportHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.SerialCommunication.SerialDevice, win32more.Windows.Devices.SerialCommunication.PinChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(38)
    def remove_PinChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BaudRate = property(get_BaudRate, put_BaudRate)
    BreakSignalState = property(get_BreakSignalState, put_BreakSignalState)
    BytesReceived = property(get_BytesReceived, None)
    CarrierDetectState = property(get_CarrierDetectState, None)
    ClearToSendState = property(get_ClearToSendState, None)
    DataBits = property(get_DataBits, put_DataBits)
    DataSetReadyState = property(get_DataSetReadyState, None)
    Handshake = property(get_Handshake, put_Handshake)
    IsDataTerminalReadyEnabled = property(get_IsDataTerminalReadyEnabled, put_IsDataTerminalReadyEnabled)
    IsRequestToSendEnabled = property(get_IsRequestToSendEnabled, put_IsRequestToSendEnabled)
    Parity = property(get_Parity, put_Parity)
    PortName = property(get_PortName, None)
    ReadTimeout = property(get_ReadTimeout, put_ReadTimeout)
    StopBits = property(get_StopBits, put_StopBits)
    UsbVendorId = property(get_UsbVendorId, None)
    UsbProductId = property(get_UsbProductId, None)
    WriteTimeout = property(get_WriteTimeout, put_WriteTimeout)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class ISerialDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.SerialCommunication.ISerialDeviceStatics'
    _iid_ = Guid('{058c4a70-0836-4993-ae1a-b61ae3be056b}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromPortName(self, portName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorFromUsbVidPid(self, vendorId: UInt16, productId: UInt16) -> WinRT_String: ...
    @winrt_commethod(9)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SerialCommunication.SerialDevice]: ...
class PinChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SerialCommunication.IPinChangedEventArgs
    _classid_ = 'Windows.Devices.SerialCommunication.PinChangedEventArgs'
    @winrt_mixinmethod
    def get_PinChange(self: win32more.Windows.Devices.SerialCommunication.IPinChangedEventArgs) -> win32more.Windows.Devices.SerialCommunication.SerialPinChange: ...
    PinChange = property(get_PinChange, None)
class SerialDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.SerialCommunication.ISerialDevice
    _classid_ = 'Windows.Devices.SerialCommunication.SerialDevice'
    @winrt_mixinmethod
    def get_BaudRate(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> UInt32: ...
    @winrt_mixinmethod
    def put_BaudRate(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_BreakSignalState(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> Boolean: ...
    @winrt_mixinmethod
    def put_BreakSignalState(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BytesReceived(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> UInt32: ...
    @winrt_mixinmethod
    def get_CarrierDetectState(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> Boolean: ...
    @winrt_mixinmethod
    def get_ClearToSendState(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> Boolean: ...
    @winrt_mixinmethod
    def get_DataBits(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> UInt16: ...
    @winrt_mixinmethod
    def put_DataBits(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, value: UInt16) -> Void: ...
    @winrt_mixinmethod
    def get_DataSetReadyState(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> Boolean: ...
    @winrt_mixinmethod
    def get_Handshake(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> win32more.Windows.Devices.SerialCommunication.SerialHandshake: ...
    @winrt_mixinmethod
    def put_Handshake(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, value: win32more.Windows.Devices.SerialCommunication.SerialHandshake) -> Void: ...
    @winrt_mixinmethod
    def get_IsDataTerminalReadyEnabled(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDataTerminalReadyEnabled(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsRequestToSendEnabled(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRequestToSendEnabled(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Parity(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> win32more.Windows.Devices.SerialCommunication.SerialParity: ...
    @winrt_mixinmethod
    def put_Parity(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, value: win32more.Windows.Devices.SerialCommunication.SerialParity) -> Void: ...
    @winrt_mixinmethod
    def get_PortName(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ReadTimeout(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_ReadTimeout(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_StopBits(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> win32more.Windows.Devices.SerialCommunication.SerialStopBitCount: ...
    @winrt_mixinmethod
    def put_StopBits(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, value: win32more.Windows.Devices.SerialCommunication.SerialStopBitCount) -> Void: ...
    @winrt_mixinmethod
    def get_UsbVendorId(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsbProductId(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> UInt16: ...
    @winrt_mixinmethod
    def get_WriteTimeout(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_WriteTimeout(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_InputStream(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_OutputStream(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def add_ErrorReceived(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, reportHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.SerialCommunication.SerialDevice, win32more.Windows.Devices.SerialCommunication.ErrorReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ErrorReceived(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PinChanged(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, reportHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.SerialCommunication.SerialDevice, win32more.Windows.Devices.SerialCommunication.PinChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PinChanged(self: win32more.Windows.Devices.SerialCommunication.ISerialDevice, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.SerialCommunication.ISerialDeviceStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromPortName(cls: win32more.Windows.Devices.SerialCommunication.ISerialDeviceStatics, portName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromUsbVidPid(cls: win32more.Windows.Devices.SerialCommunication.ISerialDeviceStatics, vendorId: UInt16, productId: UInt16) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.SerialCommunication.ISerialDeviceStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.SerialCommunication.SerialDevice]: ...
    BaudRate = property(get_BaudRate, put_BaudRate)
    BreakSignalState = property(get_BreakSignalState, put_BreakSignalState)
    BytesReceived = property(get_BytesReceived, None)
    CarrierDetectState = property(get_CarrierDetectState, None)
    ClearToSendState = property(get_ClearToSendState, None)
    DataBits = property(get_DataBits, put_DataBits)
    DataSetReadyState = property(get_DataSetReadyState, None)
    Handshake = property(get_Handshake, put_Handshake)
    IsDataTerminalReadyEnabled = property(get_IsDataTerminalReadyEnabled, put_IsDataTerminalReadyEnabled)
    IsRequestToSendEnabled = property(get_IsRequestToSendEnabled, put_IsRequestToSendEnabled)
    Parity = property(get_Parity, put_Parity)
    PortName = property(get_PortName, None)
    ReadTimeout = property(get_ReadTimeout, put_ReadTimeout)
    StopBits = property(get_StopBits, put_StopBits)
    UsbVendorId = property(get_UsbVendorId, None)
    UsbProductId = property(get_UsbProductId, None)
    WriteTimeout = property(get_WriteTimeout, put_WriteTimeout)
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
SerialError = Int32
SerialError_Frame: SerialError = 0
SerialError_BufferOverrun: SerialError = 1
SerialError_ReceiveFull: SerialError = 2
SerialError_ReceiveParity: SerialError = 3
SerialError_TransmitFull: SerialError = 4
SerialHandshake = Int32
SerialHandshake_None: SerialHandshake = 0
SerialHandshake_RequestToSend: SerialHandshake = 1
SerialHandshake_XOnXOff: SerialHandshake = 2
SerialHandshake_RequestToSendXOnXOff: SerialHandshake = 3
SerialParity = Int32
SerialParity_None: SerialParity = 0
SerialParity_Odd: SerialParity = 1
SerialParity_Even: SerialParity = 2
SerialParity_Mark: SerialParity = 3
SerialParity_Space: SerialParity = 4
SerialPinChange = Int32
SerialPinChange_BreakSignal: SerialPinChange = 0
SerialPinChange_CarrierDetect: SerialPinChange = 1
SerialPinChange_ClearToSend: SerialPinChange = 2
SerialPinChange_DataSetReady: SerialPinChange = 3
SerialPinChange_RingIndicator: SerialPinChange = 4
SerialStopBitCount = Int32
SerialStopBitCount_One: SerialStopBitCount = 0
SerialStopBitCount_OnePointFive: SerialStopBitCount = 1
SerialStopBitCount_Two: SerialStopBitCount = 2
make_ready(__name__)
