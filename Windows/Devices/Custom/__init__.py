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
import Windows.Devices.Custom
import Windows.Foundation
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
class CustomDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Custom.CustomDevice'
    @winrt_mixinmethod
    def get_InputStream(self: Windows.Devices.Custom.ICustomDevice) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_OutputStream(self: Windows.Devices.Custom.ICustomDevice) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def SendIOControlAsync(self: Windows.Devices.Custom.ICustomDevice, ioControlCode: Windows.Devices.Custom.IIOControlCode, inputBuffer: Windows.Storage.Streams.IBuffer, outputBuffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def TrySendIOControlAsync(self: Windows.Devices.Custom.ICustomDevice, ioControlCode: Windows.Devices.Custom.IIOControlCode, inputBuffer: Windows.Storage.Streams.IBuffer, outputBuffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Custom.ICustomDeviceStatics, classGuid: Guid) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Custom.ICustomDeviceStatics, deviceId: WinRT_String, desiredAccess: Windows.Devices.Custom.DeviceAccessMode, sharingMode: Windows.Devices.Custom.DeviceSharingMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Custom.CustomDevice]: ...
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
CustomDeviceContract: UInt32 = 65536
DeviceAccessMode = Int32
DeviceAccessMode_Read: DeviceAccessMode = 0
DeviceAccessMode_Write: DeviceAccessMode = 1
DeviceAccessMode_ReadWrite: DeviceAccessMode = 2
DeviceSharingMode = Int32
DeviceSharingMode_Shared: DeviceSharingMode = 0
DeviceSharingMode_Exclusive: DeviceSharingMode = 1
class ICustomDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('dd30251f-c48b-43bd-bc-b1-de-c8-8f-15-14-3e')
    @winrt_commethod(6)
    def get_InputStream(self) -> Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(7)
    def get_OutputStream(self) -> Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(8)
    def SendIOControlAsync(self, ioControlCode: Windows.Devices.Custom.IIOControlCode, inputBuffer: Windows.Storage.Streams.IBuffer, outputBuffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(9)
    def TrySendIOControlAsync(self, ioControlCode: Windows.Devices.Custom.IIOControlCode, inputBuffer: Windows.Storage.Streams.IBuffer, outputBuffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class ICustomDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c8220312-ef4c-46b1-a5-8e-ee-b3-08-dc-89-17')
    @winrt_commethod(6)
    def GetDeviceSelector(self, classGuid: Guid) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String, desiredAccess: Windows.Devices.Custom.DeviceAccessMode, sharingMode: Windows.Devices.Custom.DeviceSharingMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Custom.CustomDevice]: ...
class IIOControlCode(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0e9559e7-60c8-4375-a7-61-7f-88-08-06-6c-60')
    @winrt_commethod(6)
    def get_AccessMode(self) -> Windows.Devices.Custom.IOControlAccessMode: ...
    @winrt_commethod(7)
    def get_BufferingMethod(self) -> Windows.Devices.Custom.IOControlBufferingMethod: ...
    @winrt_commethod(8)
    def get_Function(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_DeviceType(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_ControlCode(self) -> UInt32: ...
    AccessMode = property(get_AccessMode, None)
    BufferingMethod = property(get_BufferingMethod, None)
    Function = property(get_Function, None)
    DeviceType = property(get_DeviceType, None)
    ControlCode = property(get_ControlCode, None)
class IIOControlCodeFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('856a7cf0-4c11-44ae-af-c6-b8-d4-a2-12-78-8f')
    @winrt_commethod(6)
    def CreateIOControlCode(self, deviceType: UInt16, function: UInt16, accessMode: Windows.Devices.Custom.IOControlAccessMode, bufferingMethod: Windows.Devices.Custom.IOControlBufferingMethod) -> Windows.Devices.Custom.IOControlCode: ...
class IKnownDeviceTypesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ee5479c2-5448-45da-ad-1b-24-94-8c-23-90-94')
    @winrt_commethod(6)
    def get_Unknown(self) -> UInt16: ...
    Unknown = property(get_Unknown, None)
IOControlAccessMode = Int32
IOControlAccessMode_Any: IOControlAccessMode = 0
IOControlAccessMode_Read: IOControlAccessMode = 1
IOControlAccessMode_Write: IOControlAccessMode = 2
IOControlAccessMode_ReadWrite: IOControlAccessMode = 3
IOControlBufferingMethod = Int32
IOControlBufferingMethod_Buffered: IOControlBufferingMethod = 0
IOControlBufferingMethod_DirectInput: IOControlBufferingMethod = 1
IOControlBufferingMethod_DirectOutput: IOControlBufferingMethod = 2
IOControlBufferingMethod_Neither: IOControlBufferingMethod = 3
class IOControlCode(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Custom.IOControlCode'
    @winrt_factorymethod
    def CreateIOControlCode(cls: Windows.Devices.Custom.IIOControlCodeFactory, deviceType: UInt16, function: UInt16, accessMode: Windows.Devices.Custom.IOControlAccessMode, bufferingMethod: Windows.Devices.Custom.IOControlBufferingMethod) -> Windows.Devices.Custom.IOControlCode: ...
    @winrt_mixinmethod
    def get_AccessMode(self: Windows.Devices.Custom.IIOControlCode) -> Windows.Devices.Custom.IOControlAccessMode: ...
    @winrt_mixinmethod
    def get_BufferingMethod(self: Windows.Devices.Custom.IIOControlCode) -> Windows.Devices.Custom.IOControlBufferingMethod: ...
    @winrt_mixinmethod
    def get_Function(self: Windows.Devices.Custom.IIOControlCode) -> UInt16: ...
    @winrt_mixinmethod
    def get_DeviceType(self: Windows.Devices.Custom.IIOControlCode) -> UInt16: ...
    @winrt_mixinmethod
    def get_ControlCode(self: Windows.Devices.Custom.IIOControlCode) -> UInt32: ...
    AccessMode = property(get_AccessMode, None)
    BufferingMethod = property(get_BufferingMethod, None)
    Function = property(get_Function, None)
    DeviceType = property(get_DeviceType, None)
    ControlCode = property(get_ControlCode, None)
class KnownDeviceTypes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Custom.KnownDeviceTypes'
    @winrt_classmethod
    def get_Unknown(cls: Windows.Devices.Custom.IKnownDeviceTypesStatics) -> UInt16: ...
    Unknown = property(get_Unknown, None)
make_head(_module, 'CustomDevice')
make_head(_module, 'ICustomDevice')
make_head(_module, 'ICustomDeviceStatics')
make_head(_module, 'IIOControlCode')
make_head(_module, 'IIOControlCodeFactory')
make_head(_module, 'IKnownDeviceTypesStatics')
make_head(_module, 'IOControlCode')
make_head(_module, 'KnownDeviceTypes')
