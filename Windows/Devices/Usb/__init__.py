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
import Windows.Devices.Usb
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IUsbBulkInEndpointDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbBulkInEndpointDescriptor'
    _iid_ = Guid('{3c6e4846-06cf-42a9-9dc2-971c1b14b6e3}')
    @winrt_commethod(6)
    def get_MaxPacketSize(self: Windows.Devices.Usb.IUsbBulkInEndpointDescriptor) -> UInt32: ...
    @winrt_commethod(7)
    def get_EndpointNumber(self: Windows.Devices.Usb.IUsbBulkInEndpointDescriptor) -> Byte: ...
    @winrt_commethod(8)
    def get_Pipe(self: Windows.Devices.Usb.IUsbBulkInEndpointDescriptor) -> Windows.Devices.Usb.UsbBulkInPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Pipe = property(get_Pipe, None)
class IUsbBulkInPipe(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbBulkInPipe'
    _iid_ = Guid('{f01d2d3b-4548-4d50-b326-d82cdabe1220}')
    @winrt_commethod(6)
    def get_MaxTransferSizeBytes(self: Windows.Devices.Usb.IUsbBulkInPipe) -> UInt32: ...
    @winrt_commethod(7)
    def get_EndpointDescriptor(self: Windows.Devices.Usb.IUsbBulkInPipe) -> Windows.Devices.Usb.UsbBulkInEndpointDescriptor: ...
    @winrt_commethod(8)
    def ClearStallAsync(self: Windows.Devices.Usb.IUsbBulkInPipe) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def put_ReadOptions(self: Windows.Devices.Usb.IUsbBulkInPipe, value: Windows.Devices.Usb.UsbReadOptions) -> Void: ...
    @winrt_commethod(10)
    def get_ReadOptions(self: Windows.Devices.Usb.IUsbBulkInPipe) -> Windows.Devices.Usb.UsbReadOptions: ...
    @winrt_commethod(11)
    def FlushBuffer(self: Windows.Devices.Usb.IUsbBulkInPipe) -> Void: ...
    @winrt_commethod(12)
    def get_InputStream(self: Windows.Devices.Usb.IUsbBulkInPipe) -> Windows.Storage.Streams.IInputStream: ...
    MaxTransferSizeBytes = property(get_MaxTransferSizeBytes, None)
    EndpointDescriptor = property(get_EndpointDescriptor, None)
    ReadOptions = property(get_ReadOptions, put_ReadOptions)
    InputStream = property(get_InputStream, None)
class IUsbBulkOutEndpointDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbBulkOutEndpointDescriptor'
    _iid_ = Guid('{2820847a-ffee-4f60-9be1-956cac3ecb65}')
    @winrt_commethod(6)
    def get_MaxPacketSize(self: Windows.Devices.Usb.IUsbBulkOutEndpointDescriptor) -> UInt32: ...
    @winrt_commethod(7)
    def get_EndpointNumber(self: Windows.Devices.Usb.IUsbBulkOutEndpointDescriptor) -> Byte: ...
    @winrt_commethod(8)
    def get_Pipe(self: Windows.Devices.Usb.IUsbBulkOutEndpointDescriptor) -> Windows.Devices.Usb.UsbBulkOutPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Pipe = property(get_Pipe, None)
class IUsbBulkOutPipe(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbBulkOutPipe'
    _iid_ = Guid('{a8e9ee6e-0115-45aa-8b21-37b225bccee7}')
    @winrt_commethod(6)
    def get_EndpointDescriptor(self: Windows.Devices.Usb.IUsbBulkOutPipe) -> Windows.Devices.Usb.UsbBulkOutEndpointDescriptor: ...
    @winrt_commethod(7)
    def ClearStallAsync(self: Windows.Devices.Usb.IUsbBulkOutPipe) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def put_WriteOptions(self: Windows.Devices.Usb.IUsbBulkOutPipe, value: Windows.Devices.Usb.UsbWriteOptions) -> Void: ...
    @winrt_commethod(9)
    def get_WriteOptions(self: Windows.Devices.Usb.IUsbBulkOutPipe) -> Windows.Devices.Usb.UsbWriteOptions: ...
    @winrt_commethod(10)
    def get_OutputStream(self: Windows.Devices.Usb.IUsbBulkOutPipe) -> Windows.Storage.Streams.IOutputStream: ...
    EndpointDescriptor = property(get_EndpointDescriptor, None)
    WriteOptions = property(get_WriteOptions, put_WriteOptions)
    OutputStream = property(get_OutputStream, None)
class IUsbConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbConfiguration'
    _iid_ = Guid('{68177429-36a9-46d7-b873-fc689251ec30}')
    @winrt_commethod(6)
    def get_UsbInterfaces(self: Windows.Devices.Usb.IUsbConfiguration) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbInterface]: ...
    @winrt_commethod(7)
    def get_ConfigurationDescriptor(self: Windows.Devices.Usb.IUsbConfiguration) -> Windows.Devices.Usb.UsbConfigurationDescriptor: ...
    @winrt_commethod(8)
    def get_Descriptors(self: Windows.Devices.Usb.IUsbConfiguration) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbDescriptor]: ...
    UsbInterfaces = property(get_UsbInterfaces, None)
    ConfigurationDescriptor = property(get_ConfigurationDescriptor, None)
    Descriptors = property(get_Descriptors, None)
class IUsbConfigurationDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbConfigurationDescriptor'
    _iid_ = Guid('{f2176d92-b442-407a-8207-7d646c0385f3}')
    @winrt_commethod(6)
    def get_ConfigurationValue(self: Windows.Devices.Usb.IUsbConfigurationDescriptor) -> Byte: ...
    @winrt_commethod(7)
    def get_MaxPowerMilliamps(self: Windows.Devices.Usb.IUsbConfigurationDescriptor) -> UInt32: ...
    @winrt_commethod(8)
    def get_SelfPowered(self: Windows.Devices.Usb.IUsbConfigurationDescriptor) -> Boolean: ...
    @winrt_commethod(9)
    def get_RemoteWakeup(self: Windows.Devices.Usb.IUsbConfigurationDescriptor) -> Boolean: ...
    ConfigurationValue = property(get_ConfigurationValue, None)
    MaxPowerMilliamps = property(get_MaxPowerMilliamps, None)
    SelfPowered = property(get_SelfPowered, None)
    RemoteWakeup = property(get_RemoteWakeup, None)
class IUsbConfigurationDescriptorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbConfigurationDescriptorStatics'
    _iid_ = Guid('{424ced93-e740-40a1-92bd-da120ea04914}')
    @winrt_commethod(6)
    def TryParse(self: Windows.Devices.Usb.IUsbConfigurationDescriptorStatics, descriptor: Windows.Devices.Usb.UsbDescriptor, parsed: POINTER(Windows.Devices.Usb.UsbConfigurationDescriptor)) -> Boolean: ...
    @winrt_commethod(7)
    def Parse(self: Windows.Devices.Usb.IUsbConfigurationDescriptorStatics, descriptor: Windows.Devices.Usb.UsbDescriptor) -> Windows.Devices.Usb.UsbConfigurationDescriptor: ...
class IUsbControlRequestType(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbControlRequestType'
    _iid_ = Guid('{8e9465a6-d73d-46de-94be-aae7f07c0f5c}')
    @winrt_commethod(6)
    def get_Direction(self: Windows.Devices.Usb.IUsbControlRequestType) -> Windows.Devices.Usb.UsbTransferDirection: ...
    @winrt_commethod(7)
    def put_Direction(self: Windows.Devices.Usb.IUsbControlRequestType, value: Windows.Devices.Usb.UsbTransferDirection) -> Void: ...
    @winrt_commethod(8)
    def get_ControlTransferType(self: Windows.Devices.Usb.IUsbControlRequestType) -> Windows.Devices.Usb.UsbControlTransferType: ...
    @winrt_commethod(9)
    def put_ControlTransferType(self: Windows.Devices.Usb.IUsbControlRequestType, value: Windows.Devices.Usb.UsbControlTransferType) -> Void: ...
    @winrt_commethod(10)
    def get_Recipient(self: Windows.Devices.Usb.IUsbControlRequestType) -> Windows.Devices.Usb.UsbControlRecipient: ...
    @winrt_commethod(11)
    def put_Recipient(self: Windows.Devices.Usb.IUsbControlRequestType, value: Windows.Devices.Usb.UsbControlRecipient) -> Void: ...
    @winrt_commethod(12)
    def get_AsByte(self: Windows.Devices.Usb.IUsbControlRequestType) -> Byte: ...
    @winrt_commethod(13)
    def put_AsByte(self: Windows.Devices.Usb.IUsbControlRequestType, value: Byte) -> Void: ...
    Direction = property(get_Direction, put_Direction)
    ControlTransferType = property(get_ControlTransferType, put_ControlTransferType)
    Recipient = property(get_Recipient, put_Recipient)
    AsByte = property(get_AsByte, put_AsByte)
class IUsbDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDescriptor'
    _iid_ = Guid('{0a89f216-5f9d-4874-8904-da9ad3f5528f}')
    @winrt_commethod(6)
    def get_Length(self: Windows.Devices.Usb.IUsbDescriptor) -> Byte: ...
    @winrt_commethod(7)
    def get_DescriptorType(self: Windows.Devices.Usb.IUsbDescriptor) -> Byte: ...
    @winrt_commethod(8)
    def ReadDescriptorBuffer(self: Windows.Devices.Usb.IUsbDescriptor, buffer: Windows.Storage.Streams.IBuffer) -> Void: ...
    Length = property(get_Length, None)
    DescriptorType = property(get_DescriptorType, None)
class IUsbDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDevice'
    _iid_ = Guid('{5249b992-c456-44d5-ad5e-24f5a089f63b}')
    @winrt_commethod(6)
    def SendControlOutTransferAsync(self: Windows.Devices.Usb.IUsbDevice, setupPacket: Windows.Devices.Usb.UsbSetupPacket, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(7)
    def SendControlOutTransferAsyncNoBuffer(self: Windows.Devices.Usb.IUsbDevice, setupPacket: Windows.Devices.Usb.UsbSetupPacket) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(8)
    def SendControlInTransferAsync(self: Windows.Devices.Usb.IUsbDevice, setupPacket: Windows.Devices.Usb.UsbSetupPacket, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(9)
    def SendControlInTransferAsyncNoBuffer(self: Windows.Devices.Usb.IUsbDevice, setupPacket: Windows.Devices.Usb.UsbSetupPacket) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(10)
    def get_DefaultInterface(self: Windows.Devices.Usb.IUsbDevice) -> Windows.Devices.Usb.UsbInterface: ...
    @winrt_commethod(11)
    def get_DeviceDescriptor(self: Windows.Devices.Usb.IUsbDevice) -> Windows.Devices.Usb.UsbDeviceDescriptor: ...
    @winrt_commethod(12)
    def get_Configuration(self: Windows.Devices.Usb.IUsbDevice) -> Windows.Devices.Usb.UsbConfiguration: ...
    DefaultInterface = property(get_DefaultInterface, None)
    DeviceDescriptor = property(get_DeviceDescriptor, None)
    Configuration = property(get_Configuration, None)
class IUsbDeviceClass(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDeviceClass'
    _iid_ = Guid('{051942f9-845e-47eb-b12a-38f2f617afe7}')
    @winrt_commethod(6)
    def get_ClassCode(self: Windows.Devices.Usb.IUsbDeviceClass) -> Byte: ...
    @winrt_commethod(7)
    def put_ClassCode(self: Windows.Devices.Usb.IUsbDeviceClass, value: Byte) -> Void: ...
    @winrt_commethod(8)
    def get_SubclassCode(self: Windows.Devices.Usb.IUsbDeviceClass) -> Windows.Foundation.IReference[Byte]: ...
    @winrt_commethod(9)
    def put_SubclassCode(self: Windows.Devices.Usb.IUsbDeviceClass, value: Windows.Foundation.IReference[Byte]) -> Void: ...
    @winrt_commethod(10)
    def get_ProtocolCode(self: Windows.Devices.Usb.IUsbDeviceClass) -> Windows.Foundation.IReference[Byte]: ...
    @winrt_commethod(11)
    def put_ProtocolCode(self: Windows.Devices.Usb.IUsbDeviceClass, value: Windows.Foundation.IReference[Byte]) -> Void: ...
    ClassCode = property(get_ClassCode, put_ClassCode)
    SubclassCode = property(get_SubclassCode, put_SubclassCode)
    ProtocolCode = property(get_ProtocolCode, put_ProtocolCode)
class IUsbDeviceClasses(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDeviceClasses'
    _iid_ = Guid('{686f955d-9b92-4b30-9781-c22c55ac35cb}')
class IUsbDeviceClassesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDeviceClassesStatics'
    _iid_ = Guid('{b20b0527-c580-4599-a165-981b4fd03230}')
    @winrt_commethod(6)
    def get_CdcControl(self: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(7)
    def get_Physical(self: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(8)
    def get_PersonalHealthcare(self: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(9)
    def get_ActiveSync(self: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(10)
    def get_PalmSync(self: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(11)
    def get_DeviceFirmwareUpdate(self: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(12)
    def get_Irda(self: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(13)
    def get_Measurement(self: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_commethod(14)
    def get_VendorSpecific(self: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    CdcControl = property(get_CdcControl, None)
    Physical = property(get_Physical, None)
    PersonalHealthcare = property(get_PersonalHealthcare, None)
    ActiveSync = property(get_ActiveSync, None)
    PalmSync = property(get_PalmSync, None)
    DeviceFirmwareUpdate = property(get_DeviceFirmwareUpdate, None)
    Irda = property(get_Irda, None)
    Measurement = property(get_Measurement, None)
    VendorSpecific = property(get_VendorSpecific, None)
class IUsbDeviceDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDeviceDescriptor'
    _iid_ = Guid('{1f48d1f6-ba97-4322-b92c-b5b189216588}')
    @winrt_commethod(6)
    def get_BcdUsb(self: Windows.Devices.Usb.IUsbDeviceDescriptor) -> UInt32: ...
    @winrt_commethod(7)
    def get_MaxPacketSize0(self: Windows.Devices.Usb.IUsbDeviceDescriptor) -> Byte: ...
    @winrt_commethod(8)
    def get_VendorId(self: Windows.Devices.Usb.IUsbDeviceDescriptor) -> UInt32: ...
    @winrt_commethod(9)
    def get_ProductId(self: Windows.Devices.Usb.IUsbDeviceDescriptor) -> UInt32: ...
    @winrt_commethod(10)
    def get_BcdDeviceRevision(self: Windows.Devices.Usb.IUsbDeviceDescriptor) -> UInt32: ...
    @winrt_commethod(11)
    def get_NumberOfConfigurations(self: Windows.Devices.Usb.IUsbDeviceDescriptor) -> Byte: ...
    BcdUsb = property(get_BcdUsb, None)
    MaxPacketSize0 = property(get_MaxPacketSize0, None)
    VendorId = property(get_VendorId, None)
    ProductId = property(get_ProductId, None)
    BcdDeviceRevision = property(get_BcdDeviceRevision, None)
    NumberOfConfigurations = property(get_NumberOfConfigurations, None)
class IUsbDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbDeviceStatics'
    _iid_ = Guid('{066b85a2-09b7-4446-8502-6fe6dcaa7309}')
    @winrt_commethod(6)
    def GetDeviceSelector(self: Windows.Devices.Usb.IUsbDeviceStatics, vendorId: UInt32, productId: UInt32, winUsbInterfaceClass: Guid) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorGuidOnly(self: Windows.Devices.Usb.IUsbDeviceStatics, winUsbInterfaceClass: Guid) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorVidPidOnly(self: Windows.Devices.Usb.IUsbDeviceStatics, vendorId: UInt32, productId: UInt32) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDeviceClassSelector(self: Windows.Devices.Usb.IUsbDeviceStatics, usbClass: Windows.Devices.Usb.UsbDeviceClass) -> WinRT_String: ...
    @winrt_commethod(10)
    def FromIdAsync(self: Windows.Devices.Usb.IUsbDeviceStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Usb.UsbDevice]: ...
class IUsbEndpointDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbEndpointDescriptor'
    _iid_ = Guid('{6b4862d9-8df7-4b40-ac83-578f139f0575}')
    @winrt_commethod(6)
    def get_EndpointNumber(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Byte: ...
    @winrt_commethod(7)
    def get_Direction(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Windows.Devices.Usb.UsbTransferDirection: ...
    @winrt_commethod(8)
    def get_EndpointType(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Windows.Devices.Usb.UsbEndpointType: ...
    @winrt_commethod(9)
    def get_AsBulkInEndpointDescriptor(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Windows.Devices.Usb.UsbBulkInEndpointDescriptor: ...
    @winrt_commethod(10)
    def get_AsInterruptInEndpointDescriptor(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Windows.Devices.Usb.UsbInterruptInEndpointDescriptor: ...
    @winrt_commethod(11)
    def get_AsBulkOutEndpointDescriptor(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Windows.Devices.Usb.UsbBulkOutEndpointDescriptor: ...
    @winrt_commethod(12)
    def get_AsInterruptOutEndpointDescriptor(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor: ...
    EndpointNumber = property(get_EndpointNumber, None)
    Direction = property(get_Direction, None)
    EndpointType = property(get_EndpointType, None)
    AsBulkInEndpointDescriptor = property(get_AsBulkInEndpointDescriptor, None)
    AsInterruptInEndpointDescriptor = property(get_AsInterruptInEndpointDescriptor, None)
    AsBulkOutEndpointDescriptor = property(get_AsBulkOutEndpointDescriptor, None)
    AsInterruptOutEndpointDescriptor = property(get_AsInterruptOutEndpointDescriptor, None)
class IUsbEndpointDescriptorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbEndpointDescriptorStatics'
    _iid_ = Guid('{c890b201-9a6a-495e-a82c-295b9e708106}')
    @winrt_commethod(6)
    def TryParse(self: Windows.Devices.Usb.IUsbEndpointDescriptorStatics, descriptor: Windows.Devices.Usb.UsbDescriptor, parsed: POINTER(Windows.Devices.Usb.UsbEndpointDescriptor)) -> Boolean: ...
    @winrt_commethod(7)
    def Parse(self: Windows.Devices.Usb.IUsbEndpointDescriptorStatics, descriptor: Windows.Devices.Usb.UsbDescriptor) -> Windows.Devices.Usb.UsbEndpointDescriptor: ...
class IUsbInterface(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterface'
    _iid_ = Guid('{a0322b95-7f47-48ab-a727-678c25be2112}')
    @winrt_commethod(6)
    def get_BulkInPipes(self: Windows.Devices.Usb.IUsbInterface) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbBulkInPipe]: ...
    @winrt_commethod(7)
    def get_InterruptInPipes(self: Windows.Devices.Usb.IUsbInterface) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbInterruptInPipe]: ...
    @winrt_commethod(8)
    def get_BulkOutPipes(self: Windows.Devices.Usb.IUsbInterface) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbBulkOutPipe]: ...
    @winrt_commethod(9)
    def get_InterruptOutPipes(self: Windows.Devices.Usb.IUsbInterface) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbInterruptOutPipe]: ...
    @winrt_commethod(10)
    def get_InterfaceSettings(self: Windows.Devices.Usb.IUsbInterface) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbInterfaceSetting]: ...
    @winrt_commethod(11)
    def get_InterfaceNumber(self: Windows.Devices.Usb.IUsbInterface) -> Byte: ...
    @winrt_commethod(12)
    def get_Descriptors(self: Windows.Devices.Usb.IUsbInterface) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbDescriptor]: ...
    BulkInPipes = property(get_BulkInPipes, None)
    InterruptInPipes = property(get_InterruptInPipes, None)
    BulkOutPipes = property(get_BulkOutPipes, None)
    InterruptOutPipes = property(get_InterruptOutPipes, None)
    InterfaceSettings = property(get_InterfaceSettings, None)
    InterfaceNumber = property(get_InterfaceNumber, None)
    Descriptors = property(get_Descriptors, None)
class IUsbInterfaceDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterfaceDescriptor'
    _iid_ = Guid('{199670c7-b7ee-4f90-8cd5-94a2e257598a}')
    @winrt_commethod(6)
    def get_ClassCode(self: Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_commethod(7)
    def get_SubclassCode(self: Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_commethod(8)
    def get_ProtocolCode(self: Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_commethod(9)
    def get_AlternateSettingNumber(self: Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_commethod(10)
    def get_InterfaceNumber(self: Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    ClassCode = property(get_ClassCode, None)
    SubclassCode = property(get_SubclassCode, None)
    ProtocolCode = property(get_ProtocolCode, None)
    AlternateSettingNumber = property(get_AlternateSettingNumber, None)
    InterfaceNumber = property(get_InterfaceNumber, None)
class IUsbInterfaceDescriptorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterfaceDescriptorStatics'
    _iid_ = Guid('{e34a9ff5-77d6-48b6-b0be-16c6422316fe}')
    @winrt_commethod(6)
    def TryParse(self: Windows.Devices.Usb.IUsbInterfaceDescriptorStatics, descriptor: Windows.Devices.Usb.UsbDescriptor, parsed: POINTER(Windows.Devices.Usb.UsbInterfaceDescriptor)) -> Boolean: ...
    @winrt_commethod(7)
    def Parse(self: Windows.Devices.Usb.IUsbInterfaceDescriptorStatics, descriptor: Windows.Devices.Usb.UsbDescriptor) -> Windows.Devices.Usb.UsbInterfaceDescriptor: ...
class IUsbInterfaceSetting(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterfaceSetting'
    _iid_ = Guid('{1827bba7-8da7-4af7-8f4c-7f3032e781f5}')
    @winrt_commethod(6)
    def get_BulkInEndpoints(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbBulkInEndpointDescriptor]: ...
    @winrt_commethod(7)
    def get_InterruptInEndpoints(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbInterruptInEndpointDescriptor]: ...
    @winrt_commethod(8)
    def get_BulkOutEndpoints(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbBulkOutEndpointDescriptor]: ...
    @winrt_commethod(9)
    def get_InterruptOutEndpoints(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor]: ...
    @winrt_commethod(10)
    def get_Selected(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Boolean: ...
    @winrt_commethod(11)
    def SelectSettingAsync(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def get_InterfaceDescriptor(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Devices.Usb.UsbInterfaceDescriptor: ...
    @winrt_commethod(13)
    def get_Descriptors(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbDescriptor]: ...
    BulkInEndpoints = property(get_BulkInEndpoints, None)
    InterruptInEndpoints = property(get_InterruptInEndpoints, None)
    BulkOutEndpoints = property(get_BulkOutEndpoints, None)
    InterruptOutEndpoints = property(get_InterruptOutEndpoints, None)
    Selected = property(get_Selected, None)
    InterfaceDescriptor = property(get_InterfaceDescriptor, None)
    Descriptors = property(get_Descriptors, None)
class IUsbInterruptInEndpointDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor'
    _iid_ = Guid('{c0528967-c911-4c3a-86b2-419c2da89039}')
    @winrt_commethod(6)
    def get_MaxPacketSize(self: Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor) -> UInt32: ...
    @winrt_commethod(7)
    def get_EndpointNumber(self: Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor) -> Byte: ...
    @winrt_commethod(8)
    def get_Interval(self: Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_Pipe(self: Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor) -> Windows.Devices.Usb.UsbInterruptInPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Interval = property(get_Interval, None)
    Pipe = property(get_Pipe, None)
class IUsbInterruptInEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterruptInEventArgs'
    _iid_ = Guid('{b7b04092-1418-4936-8209-299cf5605583}')
    @winrt_commethod(6)
    def get_InterruptData(self: Windows.Devices.Usb.IUsbInterruptInEventArgs) -> Windows.Storage.Streams.IBuffer: ...
    InterruptData = property(get_InterruptData, None)
class IUsbInterruptInPipe(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterruptInPipe'
    _iid_ = Guid('{fa007116-84d7-48c7-8a3f-4c0b235f2ea6}')
    @winrt_commethod(6)
    def get_EndpointDescriptor(self: Windows.Devices.Usb.IUsbInterruptInPipe) -> Windows.Devices.Usb.UsbInterruptInEndpointDescriptor: ...
    @winrt_commethod(7)
    def ClearStallAsync(self: Windows.Devices.Usb.IUsbInterruptInPipe) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def add_DataReceived(self: Windows.Devices.Usb.IUsbInterruptInPipe, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Usb.UsbInterruptInPipe, Windows.Devices.Usb.UsbInterruptInEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DataReceived(self: Windows.Devices.Usb.IUsbInterruptInPipe, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    EndpointDescriptor = property(get_EndpointDescriptor, None)
class IUsbInterruptOutEndpointDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor'
    _iid_ = Guid('{cc9fed81-10ca-4533-952d-9e278341e80f}')
    @winrt_commethod(6)
    def get_MaxPacketSize(self: Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor) -> UInt32: ...
    @winrt_commethod(7)
    def get_EndpointNumber(self: Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor) -> Byte: ...
    @winrt_commethod(8)
    def get_Interval(self: Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_Pipe(self: Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor) -> Windows.Devices.Usb.UsbInterruptOutPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Interval = property(get_Interval, None)
    Pipe = property(get_Pipe, None)
class IUsbInterruptOutPipe(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbInterruptOutPipe'
    _iid_ = Guid('{e984c8a9-aaf9-49d0-b96c-f661ab4a7f95}')
    @winrt_commethod(6)
    def get_EndpointDescriptor(self: Windows.Devices.Usb.IUsbInterruptOutPipe) -> Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor: ...
    @winrt_commethod(7)
    def ClearStallAsync(self: Windows.Devices.Usb.IUsbInterruptOutPipe) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def put_WriteOptions(self: Windows.Devices.Usb.IUsbInterruptOutPipe, value: Windows.Devices.Usb.UsbWriteOptions) -> Void: ...
    @winrt_commethod(9)
    def get_WriteOptions(self: Windows.Devices.Usb.IUsbInterruptOutPipe) -> Windows.Devices.Usb.UsbWriteOptions: ...
    @winrt_commethod(10)
    def get_OutputStream(self: Windows.Devices.Usb.IUsbInterruptOutPipe) -> Windows.Storage.Streams.IOutputStream: ...
    EndpointDescriptor = property(get_EndpointDescriptor, None)
    WriteOptions = property(get_WriteOptions, put_WriteOptions)
    OutputStream = property(get_OutputStream, None)
class IUsbSetupPacket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbSetupPacket'
    _iid_ = Guid('{104ba132-c78f-4c51-b654-e49d02f2cb03}')
    @winrt_commethod(6)
    def get_RequestType(self: Windows.Devices.Usb.IUsbSetupPacket) -> Windows.Devices.Usb.UsbControlRequestType: ...
    @winrt_commethod(7)
    def put_RequestType(self: Windows.Devices.Usb.IUsbSetupPacket, value: Windows.Devices.Usb.UsbControlRequestType) -> Void: ...
    @winrt_commethod(8)
    def get_Request(self: Windows.Devices.Usb.IUsbSetupPacket) -> Byte: ...
    @winrt_commethod(9)
    def put_Request(self: Windows.Devices.Usb.IUsbSetupPacket, value: Byte) -> Void: ...
    @winrt_commethod(10)
    def get_Value(self: Windows.Devices.Usb.IUsbSetupPacket) -> UInt32: ...
    @winrt_commethod(11)
    def put_Value(self: Windows.Devices.Usb.IUsbSetupPacket, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_Index(self: Windows.Devices.Usb.IUsbSetupPacket) -> UInt32: ...
    @winrt_commethod(13)
    def put_Index(self: Windows.Devices.Usb.IUsbSetupPacket, value: UInt32) -> Void: ...
    @winrt_commethod(14)
    def get_Length(self: Windows.Devices.Usb.IUsbSetupPacket) -> UInt32: ...
    @winrt_commethod(15)
    def put_Length(self: Windows.Devices.Usb.IUsbSetupPacket, value: UInt32) -> Void: ...
    RequestType = property(get_RequestType, put_RequestType)
    Request = property(get_Request, put_Request)
    Value = property(get_Value, put_Value)
    Index = property(get_Index, put_Index)
    Length = property(get_Length, put_Length)
class IUsbSetupPacketFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Usb.IUsbSetupPacketFactory'
    _iid_ = Guid('{c9257d50-1b2e-4a41-a2a7-338f0cef3c14}')
    @winrt_commethod(6)
    def CreateWithEightByteBuffer(self: Windows.Devices.Usb.IUsbSetupPacketFactory, eightByteBuffer: Windows.Storage.Streams.IBuffer) -> Windows.Devices.Usb.UsbSetupPacket: ...
class UsbBulkInEndpointDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbBulkInEndpointDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbBulkInEndpointDescriptor'
    @winrt_mixinmethod
    def get_MaxPacketSize(self: Windows.Devices.Usb.IUsbBulkInEndpointDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_EndpointNumber(self: Windows.Devices.Usb.IUsbBulkInEndpointDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_Pipe(self: Windows.Devices.Usb.IUsbBulkInEndpointDescriptor) -> Windows.Devices.Usb.UsbBulkInPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Pipe = property(get_Pipe, None)
class UsbBulkInPipe(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbBulkInPipe
    _classid_ = 'Windows.Devices.Usb.UsbBulkInPipe'
    @winrt_mixinmethod
    def get_MaxTransferSizeBytes(self: Windows.Devices.Usb.IUsbBulkInPipe) -> UInt32: ...
    @winrt_mixinmethod
    def get_EndpointDescriptor(self: Windows.Devices.Usb.IUsbBulkInPipe) -> Windows.Devices.Usb.UsbBulkInEndpointDescriptor: ...
    @winrt_mixinmethod
    def ClearStallAsync(self: Windows.Devices.Usb.IUsbBulkInPipe) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def put_ReadOptions(self: Windows.Devices.Usb.IUsbBulkInPipe, value: Windows.Devices.Usb.UsbReadOptions) -> Void: ...
    @winrt_mixinmethod
    def get_ReadOptions(self: Windows.Devices.Usb.IUsbBulkInPipe) -> Windows.Devices.Usb.UsbReadOptions: ...
    @winrt_mixinmethod
    def FlushBuffer(self: Windows.Devices.Usb.IUsbBulkInPipe) -> Void: ...
    @winrt_mixinmethod
    def get_InputStream(self: Windows.Devices.Usb.IUsbBulkInPipe) -> Windows.Storage.Streams.IInputStream: ...
    MaxTransferSizeBytes = property(get_MaxTransferSizeBytes, None)
    EndpointDescriptor = property(get_EndpointDescriptor, None)
    ReadOptions = property(get_ReadOptions, put_ReadOptions)
    InputStream = property(get_InputStream, None)
class UsbBulkOutEndpointDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbBulkOutEndpointDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbBulkOutEndpointDescriptor'
    @winrt_mixinmethod
    def get_MaxPacketSize(self: Windows.Devices.Usb.IUsbBulkOutEndpointDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_EndpointNumber(self: Windows.Devices.Usb.IUsbBulkOutEndpointDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_Pipe(self: Windows.Devices.Usb.IUsbBulkOutEndpointDescriptor) -> Windows.Devices.Usb.UsbBulkOutPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Pipe = property(get_Pipe, None)
class UsbBulkOutPipe(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbBulkOutPipe
    _classid_ = 'Windows.Devices.Usb.UsbBulkOutPipe'
    @winrt_mixinmethod
    def get_EndpointDescriptor(self: Windows.Devices.Usb.IUsbBulkOutPipe) -> Windows.Devices.Usb.UsbBulkOutEndpointDescriptor: ...
    @winrt_mixinmethod
    def ClearStallAsync(self: Windows.Devices.Usb.IUsbBulkOutPipe) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def put_WriteOptions(self: Windows.Devices.Usb.IUsbBulkOutPipe, value: Windows.Devices.Usb.UsbWriteOptions) -> Void: ...
    @winrt_mixinmethod
    def get_WriteOptions(self: Windows.Devices.Usb.IUsbBulkOutPipe) -> Windows.Devices.Usb.UsbWriteOptions: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Devices.Usb.IUsbBulkOutPipe) -> Windows.Storage.Streams.IOutputStream: ...
    EndpointDescriptor = property(get_EndpointDescriptor, None)
    WriteOptions = property(get_WriteOptions, put_WriteOptions)
    OutputStream = property(get_OutputStream, None)
class UsbConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbConfiguration
    _classid_ = 'Windows.Devices.Usb.UsbConfiguration'
    @winrt_mixinmethod
    def get_UsbInterfaces(self: Windows.Devices.Usb.IUsbConfiguration) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbInterface]: ...
    @winrt_mixinmethod
    def get_ConfigurationDescriptor(self: Windows.Devices.Usb.IUsbConfiguration) -> Windows.Devices.Usb.UsbConfigurationDescriptor: ...
    @winrt_mixinmethod
    def get_Descriptors(self: Windows.Devices.Usb.IUsbConfiguration) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbDescriptor]: ...
    UsbInterfaces = property(get_UsbInterfaces, None)
    ConfigurationDescriptor = property(get_ConfigurationDescriptor, None)
    Descriptors = property(get_Descriptors, None)
class UsbConfigurationDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbConfigurationDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbConfigurationDescriptor'
    @winrt_mixinmethod
    def get_ConfigurationValue(self: Windows.Devices.Usb.IUsbConfigurationDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_MaxPowerMilliamps(self: Windows.Devices.Usb.IUsbConfigurationDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_SelfPowered(self: Windows.Devices.Usb.IUsbConfigurationDescriptor) -> Boolean: ...
    @winrt_mixinmethod
    def get_RemoteWakeup(self: Windows.Devices.Usb.IUsbConfigurationDescriptor) -> Boolean: ...
    @winrt_classmethod
    def TryParse(cls: Windows.Devices.Usb.IUsbConfigurationDescriptorStatics, descriptor: Windows.Devices.Usb.UsbDescriptor, parsed: POINTER(Windows.Devices.Usb.UsbConfigurationDescriptor)) -> Boolean: ...
    @winrt_classmethod
    def Parse(cls: Windows.Devices.Usb.IUsbConfigurationDescriptorStatics, descriptor: Windows.Devices.Usb.UsbDescriptor) -> Windows.Devices.Usb.UsbConfigurationDescriptor: ...
    ConfigurationValue = property(get_ConfigurationValue, None)
    MaxPowerMilliamps = property(get_MaxPowerMilliamps, None)
    SelfPowered = property(get_SelfPowered, None)
    RemoteWakeup = property(get_RemoteWakeup, None)
UsbControlRecipient = Int32
UsbControlRecipient_Device: UsbControlRecipient = 0
UsbControlRecipient_SpecifiedInterface: UsbControlRecipient = 1
UsbControlRecipient_Endpoint: UsbControlRecipient = 2
UsbControlRecipient_Other: UsbControlRecipient = 3
UsbControlRecipient_DefaultInterface: UsbControlRecipient = 4
class UsbControlRequestType(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbControlRequestType
    _classid_ = 'Windows.Devices.Usb.UsbControlRequestType'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Devices.Usb.UsbControlRequestType: ...
    @winrt_mixinmethod
    def get_Direction(self: Windows.Devices.Usb.IUsbControlRequestType) -> Windows.Devices.Usb.UsbTransferDirection: ...
    @winrt_mixinmethod
    def put_Direction(self: Windows.Devices.Usb.IUsbControlRequestType, value: Windows.Devices.Usb.UsbTransferDirection) -> Void: ...
    @winrt_mixinmethod
    def get_ControlTransferType(self: Windows.Devices.Usb.IUsbControlRequestType) -> Windows.Devices.Usb.UsbControlTransferType: ...
    @winrt_mixinmethod
    def put_ControlTransferType(self: Windows.Devices.Usb.IUsbControlRequestType, value: Windows.Devices.Usb.UsbControlTransferType) -> Void: ...
    @winrt_mixinmethod
    def get_Recipient(self: Windows.Devices.Usb.IUsbControlRequestType) -> Windows.Devices.Usb.UsbControlRecipient: ...
    @winrt_mixinmethod
    def put_Recipient(self: Windows.Devices.Usb.IUsbControlRequestType, value: Windows.Devices.Usb.UsbControlRecipient) -> Void: ...
    @winrt_mixinmethod
    def get_AsByte(self: Windows.Devices.Usb.IUsbControlRequestType) -> Byte: ...
    @winrt_mixinmethod
    def put_AsByte(self: Windows.Devices.Usb.IUsbControlRequestType, value: Byte) -> Void: ...
    Direction = property(get_Direction, put_Direction)
    ControlTransferType = property(get_ControlTransferType, put_ControlTransferType)
    Recipient = property(get_Recipient, put_Recipient)
    AsByte = property(get_AsByte, put_AsByte)
UsbControlTransferType = Int32
UsbControlTransferType_Standard: UsbControlTransferType = 0
UsbControlTransferType_Class: UsbControlTransferType = 1
UsbControlTransferType_Vendor: UsbControlTransferType = 2
class UsbDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbDescriptor'
    @winrt_mixinmethod
    def get_Length(self: Windows.Devices.Usb.IUsbDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_DescriptorType(self: Windows.Devices.Usb.IUsbDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def ReadDescriptorBuffer(self: Windows.Devices.Usb.IUsbDescriptor, buffer: Windows.Storage.Streams.IBuffer) -> Void: ...
    Length = property(get_Length, None)
    DescriptorType = property(get_DescriptorType, None)
class UsbDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbDevice
    _classid_ = 'Windows.Devices.Usb.UsbDevice'
    @winrt_mixinmethod
    def SendControlOutTransferAsync(self: Windows.Devices.Usb.IUsbDevice, setupPacket: Windows.Devices.Usb.UsbSetupPacket, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def SendControlOutTransferAsyncNoBuffer(self: Windows.Devices.Usb.IUsbDevice, setupPacket: Windows.Devices.Usb.UsbSetupPacket) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def SendControlInTransferAsync(self: Windows.Devices.Usb.IUsbDevice, setupPacket: Windows.Devices.Usb.UsbSetupPacket, buffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def SendControlInTransferAsyncNoBuffer(self: Windows.Devices.Usb.IUsbDevice, setupPacket: Windows.Devices.Usb.UsbSetupPacket) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def get_DefaultInterface(self: Windows.Devices.Usb.IUsbDevice) -> Windows.Devices.Usb.UsbInterface: ...
    @winrt_mixinmethod
    def get_DeviceDescriptor(self: Windows.Devices.Usb.IUsbDevice) -> Windows.Devices.Usb.UsbDeviceDescriptor: ...
    @winrt_mixinmethod
    def get_Configuration(self: Windows.Devices.Usb.IUsbDevice) -> Windows.Devices.Usb.UsbConfiguration: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Usb.IUsbDeviceStatics, vendorId: UInt32, productId: UInt32, winUsbInterfaceClass: Guid) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorGuidOnly(cls: Windows.Devices.Usb.IUsbDeviceStatics, winUsbInterfaceClass: Guid) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorVidPidOnly(cls: Windows.Devices.Usb.IUsbDeviceStatics, vendorId: UInt32, productId: UInt32) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceClassSelector(cls: Windows.Devices.Usb.IUsbDeviceStatics, usbClass: Windows.Devices.Usb.UsbDeviceClass) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Usb.IUsbDeviceStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Usb.UsbDevice]: ...
    DefaultInterface = property(get_DefaultInterface, None)
    DeviceDescriptor = property(get_DeviceDescriptor, None)
    Configuration = property(get_Configuration, None)
class UsbDeviceClass(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbDeviceClass
    _classid_ = 'Windows.Devices.Usb.UsbDeviceClass'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_mixinmethod
    def get_ClassCode(self: Windows.Devices.Usb.IUsbDeviceClass) -> Byte: ...
    @winrt_mixinmethod
    def put_ClassCode(self: Windows.Devices.Usb.IUsbDeviceClass, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_SubclassCode(self: Windows.Devices.Usb.IUsbDeviceClass) -> Windows.Foundation.IReference[Byte]: ...
    @winrt_mixinmethod
    def put_SubclassCode(self: Windows.Devices.Usb.IUsbDeviceClass, value: Windows.Foundation.IReference[Byte]) -> Void: ...
    @winrt_mixinmethod
    def get_ProtocolCode(self: Windows.Devices.Usb.IUsbDeviceClass) -> Windows.Foundation.IReference[Byte]: ...
    @winrt_mixinmethod
    def put_ProtocolCode(self: Windows.Devices.Usb.IUsbDeviceClass, value: Windows.Foundation.IReference[Byte]) -> Void: ...
    ClassCode = property(get_ClassCode, put_ClassCode)
    SubclassCode = property(get_SubclassCode, put_SubclassCode)
    ProtocolCode = property(get_ProtocolCode, put_ProtocolCode)
class _UsbDeviceClasses_Meta_(ComPtr.__class__):
    pass
class UsbDeviceClasses(ComPtr, metaclass=_UsbDeviceClasses_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbDeviceClasses
    _classid_ = 'Windows.Devices.Usb.UsbDeviceClasses'
    @winrt_classmethod
    def get_CdcControl(cls: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_Physical(cls: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_PersonalHealthcare(cls: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_ActiveSync(cls: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_PalmSync(cls: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_DeviceFirmwareUpdate(cls: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_Irda(cls: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_Measurement(cls: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    @winrt_classmethod
    def get_VendorSpecific(cls: Windows.Devices.Usb.IUsbDeviceClassesStatics) -> Windows.Devices.Usb.UsbDeviceClass: ...
    _UsbDeviceClasses_Meta_.CdcControl = property(get_CdcControl.__wrapped__, None)
    _UsbDeviceClasses_Meta_.Physical = property(get_Physical.__wrapped__, None)
    _UsbDeviceClasses_Meta_.PersonalHealthcare = property(get_PersonalHealthcare.__wrapped__, None)
    _UsbDeviceClasses_Meta_.ActiveSync = property(get_ActiveSync.__wrapped__, None)
    _UsbDeviceClasses_Meta_.PalmSync = property(get_PalmSync.__wrapped__, None)
    _UsbDeviceClasses_Meta_.DeviceFirmwareUpdate = property(get_DeviceFirmwareUpdate.__wrapped__, None)
    _UsbDeviceClasses_Meta_.Irda = property(get_Irda.__wrapped__, None)
    _UsbDeviceClasses_Meta_.Measurement = property(get_Measurement.__wrapped__, None)
    _UsbDeviceClasses_Meta_.VendorSpecific = property(get_VendorSpecific.__wrapped__, None)
class UsbDeviceDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbDeviceDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbDeviceDescriptor'
    @winrt_mixinmethod
    def get_BcdUsb(self: Windows.Devices.Usb.IUsbDeviceDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxPacketSize0(self: Windows.Devices.Usb.IUsbDeviceDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_VendorId(self: Windows.Devices.Usb.IUsbDeviceDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_ProductId(self: Windows.Devices.Usb.IUsbDeviceDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_BcdDeviceRevision(self: Windows.Devices.Usb.IUsbDeviceDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_NumberOfConfigurations(self: Windows.Devices.Usb.IUsbDeviceDescriptor) -> Byte: ...
    BcdUsb = property(get_BcdUsb, None)
    MaxPacketSize0 = property(get_MaxPacketSize0, None)
    VendorId = property(get_VendorId, None)
    ProductId = property(get_ProductId, None)
    BcdDeviceRevision = property(get_BcdDeviceRevision, None)
    NumberOfConfigurations = property(get_NumberOfConfigurations, None)
class UsbEndpointDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbEndpointDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbEndpointDescriptor'
    @winrt_mixinmethod
    def get_EndpointNumber(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_Direction(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Windows.Devices.Usb.UsbTransferDirection: ...
    @winrt_mixinmethod
    def get_EndpointType(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Windows.Devices.Usb.UsbEndpointType: ...
    @winrt_mixinmethod
    def get_AsBulkInEndpointDescriptor(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Windows.Devices.Usb.UsbBulkInEndpointDescriptor: ...
    @winrt_mixinmethod
    def get_AsInterruptInEndpointDescriptor(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Windows.Devices.Usb.UsbInterruptInEndpointDescriptor: ...
    @winrt_mixinmethod
    def get_AsBulkOutEndpointDescriptor(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Windows.Devices.Usb.UsbBulkOutEndpointDescriptor: ...
    @winrt_mixinmethod
    def get_AsInterruptOutEndpointDescriptor(self: Windows.Devices.Usb.IUsbEndpointDescriptor) -> Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor: ...
    @winrt_classmethod
    def TryParse(cls: Windows.Devices.Usb.IUsbEndpointDescriptorStatics, descriptor: Windows.Devices.Usb.UsbDescriptor, parsed: POINTER(Windows.Devices.Usb.UsbEndpointDescriptor)) -> Boolean: ...
    @winrt_classmethod
    def Parse(cls: Windows.Devices.Usb.IUsbEndpointDescriptorStatics, descriptor: Windows.Devices.Usb.UsbDescriptor) -> Windows.Devices.Usb.UsbEndpointDescriptor: ...
    EndpointNumber = property(get_EndpointNumber, None)
    Direction = property(get_Direction, None)
    EndpointType = property(get_EndpointType, None)
    AsBulkInEndpointDescriptor = property(get_AsBulkInEndpointDescriptor, None)
    AsInterruptInEndpointDescriptor = property(get_AsInterruptInEndpointDescriptor, None)
    AsBulkOutEndpointDescriptor = property(get_AsBulkOutEndpointDescriptor, None)
    AsInterruptOutEndpointDescriptor = property(get_AsInterruptOutEndpointDescriptor, None)
UsbEndpointType = Int32
UsbEndpointType_Control: UsbEndpointType = 0
UsbEndpointType_Isochronous: UsbEndpointType = 1
UsbEndpointType_Bulk: UsbEndpointType = 2
UsbEndpointType_Interrupt: UsbEndpointType = 3
class UsbInterface(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbInterface
    _classid_ = 'Windows.Devices.Usb.UsbInterface'
    @winrt_mixinmethod
    def get_BulkInPipes(self: Windows.Devices.Usb.IUsbInterface) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbBulkInPipe]: ...
    @winrt_mixinmethod
    def get_InterruptInPipes(self: Windows.Devices.Usb.IUsbInterface) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbInterruptInPipe]: ...
    @winrt_mixinmethod
    def get_BulkOutPipes(self: Windows.Devices.Usb.IUsbInterface) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbBulkOutPipe]: ...
    @winrt_mixinmethod
    def get_InterruptOutPipes(self: Windows.Devices.Usb.IUsbInterface) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbInterruptOutPipe]: ...
    @winrt_mixinmethod
    def get_InterfaceSettings(self: Windows.Devices.Usb.IUsbInterface) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbInterfaceSetting]: ...
    @winrt_mixinmethod
    def get_InterfaceNumber(self: Windows.Devices.Usb.IUsbInterface) -> Byte: ...
    @winrt_mixinmethod
    def get_Descriptors(self: Windows.Devices.Usb.IUsbInterface) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbDescriptor]: ...
    BulkInPipes = property(get_BulkInPipes, None)
    InterruptInPipes = property(get_InterruptInPipes, None)
    BulkOutPipes = property(get_BulkOutPipes, None)
    InterruptOutPipes = property(get_InterruptOutPipes, None)
    InterfaceSettings = property(get_InterfaceSettings, None)
    InterfaceNumber = property(get_InterfaceNumber, None)
    Descriptors = property(get_Descriptors, None)
class UsbInterfaceDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbInterfaceDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbInterfaceDescriptor'
    @winrt_mixinmethod
    def get_ClassCode(self: Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_SubclassCode(self: Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_ProtocolCode(self: Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_AlternateSettingNumber(self: Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_InterfaceNumber(self: Windows.Devices.Usb.IUsbInterfaceDescriptor) -> Byte: ...
    @winrt_classmethod
    def TryParse(cls: Windows.Devices.Usb.IUsbInterfaceDescriptorStatics, descriptor: Windows.Devices.Usb.UsbDescriptor, parsed: POINTER(Windows.Devices.Usb.UsbInterfaceDescriptor)) -> Boolean: ...
    @winrt_classmethod
    def Parse(cls: Windows.Devices.Usb.IUsbInterfaceDescriptorStatics, descriptor: Windows.Devices.Usb.UsbDescriptor) -> Windows.Devices.Usb.UsbInterfaceDescriptor: ...
    ClassCode = property(get_ClassCode, None)
    SubclassCode = property(get_SubclassCode, None)
    ProtocolCode = property(get_ProtocolCode, None)
    AlternateSettingNumber = property(get_AlternateSettingNumber, None)
    InterfaceNumber = property(get_InterfaceNumber, None)
class UsbInterfaceSetting(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbInterfaceSetting
    _classid_ = 'Windows.Devices.Usb.UsbInterfaceSetting'
    @winrt_mixinmethod
    def get_BulkInEndpoints(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbBulkInEndpointDescriptor]: ...
    @winrt_mixinmethod
    def get_InterruptInEndpoints(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbInterruptInEndpointDescriptor]: ...
    @winrt_mixinmethod
    def get_BulkOutEndpoints(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbBulkOutEndpointDescriptor]: ...
    @winrt_mixinmethod
    def get_InterruptOutEndpoints(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor]: ...
    @winrt_mixinmethod
    def get_Selected(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Boolean: ...
    @winrt_mixinmethod
    def SelectSettingAsync(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_InterfaceDescriptor(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Devices.Usb.UsbInterfaceDescriptor: ...
    @winrt_mixinmethod
    def get_Descriptors(self: Windows.Devices.Usb.IUsbInterfaceSetting) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Usb.UsbDescriptor]: ...
    BulkInEndpoints = property(get_BulkInEndpoints, None)
    InterruptInEndpoints = property(get_InterruptInEndpoints, None)
    BulkOutEndpoints = property(get_BulkOutEndpoints, None)
    InterruptOutEndpoints = property(get_InterruptOutEndpoints, None)
    Selected = property(get_Selected, None)
    InterfaceDescriptor = property(get_InterfaceDescriptor, None)
    Descriptors = property(get_Descriptors, None)
class UsbInterruptInEndpointDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbInterruptInEndpointDescriptor'
    @winrt_mixinmethod
    def get_MaxPacketSize(self: Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_EndpointNumber(self: Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_Interval(self: Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Pipe(self: Windows.Devices.Usb.IUsbInterruptInEndpointDescriptor) -> Windows.Devices.Usb.UsbInterruptInPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Interval = property(get_Interval, None)
    Pipe = property(get_Pipe, None)
class UsbInterruptInEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbInterruptInEventArgs
    _classid_ = 'Windows.Devices.Usb.UsbInterruptInEventArgs'
    @winrt_mixinmethod
    def get_InterruptData(self: Windows.Devices.Usb.IUsbInterruptInEventArgs) -> Windows.Storage.Streams.IBuffer: ...
    InterruptData = property(get_InterruptData, None)
class UsbInterruptInPipe(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbInterruptInPipe
    _classid_ = 'Windows.Devices.Usb.UsbInterruptInPipe'
    @winrt_mixinmethod
    def get_EndpointDescriptor(self: Windows.Devices.Usb.IUsbInterruptInPipe) -> Windows.Devices.Usb.UsbInterruptInEndpointDescriptor: ...
    @winrt_mixinmethod
    def ClearStallAsync(self: Windows.Devices.Usb.IUsbInterruptInPipe) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_DataReceived(self: Windows.Devices.Usb.IUsbInterruptInPipe, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Usb.UsbInterruptInPipe, Windows.Devices.Usb.UsbInterruptInEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DataReceived(self: Windows.Devices.Usb.IUsbInterruptInPipe, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    EndpointDescriptor = property(get_EndpointDescriptor, None)
class UsbInterruptOutEndpointDescriptor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor
    _classid_ = 'Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor'
    @winrt_mixinmethod
    def get_MaxPacketSize(self: Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor) -> UInt32: ...
    @winrt_mixinmethod
    def get_EndpointNumber(self: Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor) -> Byte: ...
    @winrt_mixinmethod
    def get_Interval(self: Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Pipe(self: Windows.Devices.Usb.IUsbInterruptOutEndpointDescriptor) -> Windows.Devices.Usb.UsbInterruptOutPipe: ...
    MaxPacketSize = property(get_MaxPacketSize, None)
    EndpointNumber = property(get_EndpointNumber, None)
    Interval = property(get_Interval, None)
    Pipe = property(get_Pipe, None)
class UsbInterruptOutPipe(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbInterruptOutPipe
    _classid_ = 'Windows.Devices.Usb.UsbInterruptOutPipe'
    @winrt_mixinmethod
    def get_EndpointDescriptor(self: Windows.Devices.Usb.IUsbInterruptOutPipe) -> Windows.Devices.Usb.UsbInterruptOutEndpointDescriptor: ...
    @winrt_mixinmethod
    def ClearStallAsync(self: Windows.Devices.Usb.IUsbInterruptOutPipe) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def put_WriteOptions(self: Windows.Devices.Usb.IUsbInterruptOutPipe, value: Windows.Devices.Usb.UsbWriteOptions) -> Void: ...
    @winrt_mixinmethod
    def get_WriteOptions(self: Windows.Devices.Usb.IUsbInterruptOutPipe) -> Windows.Devices.Usb.UsbWriteOptions: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Devices.Usb.IUsbInterruptOutPipe) -> Windows.Storage.Streams.IOutputStream: ...
    EndpointDescriptor = property(get_EndpointDescriptor, None)
    WriteOptions = property(get_WriteOptions, put_WriteOptions)
    OutputStream = property(get_OutputStream, None)
UsbReadOptions = UInt32
UsbReadOptions_None: UsbReadOptions = 0
UsbReadOptions_AutoClearStall: UsbReadOptions = 1
UsbReadOptions_OverrideAutomaticBufferManagement: UsbReadOptions = 2
UsbReadOptions_IgnoreShortPacket: UsbReadOptions = 4
UsbReadOptions_AllowPartialReads: UsbReadOptions = 8
class UsbSetupPacket(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Usb.IUsbSetupPacket
    _classid_ = 'Windows.Devices.Usb.UsbSetupPacket'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Devices.Usb.UsbSetupPacket: ...
    @winrt_factorymethod
    def CreateWithEightByteBuffer(cls: Windows.Devices.Usb.IUsbSetupPacketFactory, eightByteBuffer: Windows.Storage.Streams.IBuffer) -> Windows.Devices.Usb.UsbSetupPacket: ...
    @winrt_mixinmethod
    def get_RequestType(self: Windows.Devices.Usb.IUsbSetupPacket) -> Windows.Devices.Usb.UsbControlRequestType: ...
    @winrt_mixinmethod
    def put_RequestType(self: Windows.Devices.Usb.IUsbSetupPacket, value: Windows.Devices.Usb.UsbControlRequestType) -> Void: ...
    @winrt_mixinmethod
    def get_Request(self: Windows.Devices.Usb.IUsbSetupPacket) -> Byte: ...
    @winrt_mixinmethod
    def put_Request(self: Windows.Devices.Usb.IUsbSetupPacket, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Devices.Usb.IUsbSetupPacket) -> UInt32: ...
    @winrt_mixinmethod
    def put_Value(self: Windows.Devices.Usb.IUsbSetupPacket, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Index(self: Windows.Devices.Usb.IUsbSetupPacket) -> UInt32: ...
    @winrt_mixinmethod
    def put_Index(self: Windows.Devices.Usb.IUsbSetupPacket, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Length(self: Windows.Devices.Usb.IUsbSetupPacket) -> UInt32: ...
    @winrt_mixinmethod
    def put_Length(self: Windows.Devices.Usb.IUsbSetupPacket, value: UInt32) -> Void: ...
    RequestType = property(get_RequestType, put_RequestType)
    Request = property(get_Request, put_Request)
    Value = property(get_Value, put_Value)
    Index = property(get_Index, put_Index)
    Length = property(get_Length, put_Length)
UsbTransferDirection = Int32
UsbTransferDirection_Out: UsbTransferDirection = 0
UsbTransferDirection_In: UsbTransferDirection = 1
UsbWriteOptions = UInt32
UsbWriteOptions_None: UsbWriteOptions = 0
UsbWriteOptions_AutoClearStall: UsbWriteOptions = 1
UsbWriteOptions_ShortPacketTerminate: UsbWriteOptions = 2
make_head(_module, 'IUsbBulkInEndpointDescriptor')
make_head(_module, 'IUsbBulkInPipe')
make_head(_module, 'IUsbBulkOutEndpointDescriptor')
make_head(_module, 'IUsbBulkOutPipe')
make_head(_module, 'IUsbConfiguration')
make_head(_module, 'IUsbConfigurationDescriptor')
make_head(_module, 'IUsbConfigurationDescriptorStatics')
make_head(_module, 'IUsbControlRequestType')
make_head(_module, 'IUsbDescriptor')
make_head(_module, 'IUsbDevice')
make_head(_module, 'IUsbDeviceClass')
make_head(_module, 'IUsbDeviceClasses')
make_head(_module, 'IUsbDeviceClassesStatics')
make_head(_module, 'IUsbDeviceDescriptor')
make_head(_module, 'IUsbDeviceStatics')
make_head(_module, 'IUsbEndpointDescriptor')
make_head(_module, 'IUsbEndpointDescriptorStatics')
make_head(_module, 'IUsbInterface')
make_head(_module, 'IUsbInterfaceDescriptor')
make_head(_module, 'IUsbInterfaceDescriptorStatics')
make_head(_module, 'IUsbInterfaceSetting')
make_head(_module, 'IUsbInterruptInEndpointDescriptor')
make_head(_module, 'IUsbInterruptInEventArgs')
make_head(_module, 'IUsbInterruptInPipe')
make_head(_module, 'IUsbInterruptOutEndpointDescriptor')
make_head(_module, 'IUsbInterruptOutPipe')
make_head(_module, 'IUsbSetupPacket')
make_head(_module, 'IUsbSetupPacketFactory')
make_head(_module, 'UsbBulkInEndpointDescriptor')
make_head(_module, 'UsbBulkInPipe')
make_head(_module, 'UsbBulkOutEndpointDescriptor')
make_head(_module, 'UsbBulkOutPipe')
make_head(_module, 'UsbConfiguration')
make_head(_module, 'UsbConfigurationDescriptor')
make_head(_module, 'UsbControlRequestType')
make_head(_module, 'UsbDescriptor')
make_head(_module, 'UsbDevice')
make_head(_module, 'UsbDeviceClass')
make_head(_module, 'UsbDeviceClasses')
make_head(_module, 'UsbDeviceDescriptor')
make_head(_module, 'UsbEndpointDescriptor')
make_head(_module, 'UsbInterface')
make_head(_module, 'UsbInterfaceDescriptor')
make_head(_module, 'UsbInterfaceSetting')
make_head(_module, 'UsbInterruptInEndpointDescriptor')
make_head(_module, 'UsbInterruptInEventArgs')
make_head(_module, 'UsbInterruptInPipe')
make_head(_module, 'UsbInterruptOutEndpointDescriptor')
make_head(_module, 'UsbInterruptOutPipe')
make_head(_module, 'UsbSetupPacket')
