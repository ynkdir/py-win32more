from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Custom
import win32more.Windows.Foundation
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class CustomDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Custom.ICustomDevice
    _classid_ = 'Windows.Devices.Custom.CustomDevice'
    @winrt_mixinmethod
    def get_InputStream(self: win32more.Windows.Devices.Custom.ICustomDevice) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def get_OutputStream(self: win32more.Windows.Devices.Custom.ICustomDevice) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def SendIOControlAsync(self: win32more.Windows.Devices.Custom.ICustomDevice, ioControlCode: win32more.Windows.Devices.Custom.IIOControlCode, inputBuffer: win32more.Windows.Storage.Streams.IBuffer, outputBuffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def TrySendIOControlAsync(self: win32more.Windows.Devices.Custom.ICustomDevice, ioControlCode: win32more.Windows.Devices.Custom.IIOControlCode, inputBuffer: win32more.Windows.Storage.Streams.IBuffer, outputBuffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Custom.ICustomDeviceStatics, classGuid: Guid) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Custom.ICustomDeviceStatics, deviceId: WinRT_String, desiredAccess: win32more.Windows.Devices.Custom.DeviceAccessMode, sharingMode: win32more.Windows.Devices.Custom.DeviceSharingMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Custom.CustomDevice]: ...
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
CustomDeviceContract: UInt32 = 65536
class DeviceAccessMode(Enum, Int32):
    Read = 0
    Write = 1
    ReadWrite = 2
class DeviceSharingMode(Enum, Int32):
    Shared = 0
    Exclusive = 1
class ICustomDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Custom.ICustomDevice'
    _iid_ = Guid('{dd30251f-c48b-43bd-bcb1-dec88f15143e}')
    @winrt_commethod(6)
    def get_InputStream(self) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_commethod(7)
    def get_OutputStream(self) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_commethod(8)
    def SendIOControlAsync(self, ioControlCode: win32more.Windows.Devices.Custom.IIOControlCode, inputBuffer: win32more.Windows.Storage.Streams.IBuffer, outputBuffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(9)
    def TrySendIOControlAsync(self, ioControlCode: win32more.Windows.Devices.Custom.IIOControlCode, inputBuffer: win32more.Windows.Storage.Streams.IBuffer, outputBuffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    InputStream = property(get_InputStream, None)
    OutputStream = property(get_OutputStream, None)
class ICustomDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Custom.ICustomDeviceStatics'
    _iid_ = Guid('{c8220312-ef4c-46b1-a58e-eeb308dc8917}')
    @winrt_commethod(6)
    def GetDeviceSelector(self, classGuid: Guid) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String, desiredAccess: win32more.Windows.Devices.Custom.DeviceAccessMode, sharingMode: win32more.Windows.Devices.Custom.DeviceSharingMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Custom.CustomDevice]: ...
class IIOControlCode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Custom.IIOControlCode'
    _iid_ = Guid('{0e9559e7-60c8-4375-a761-7f8808066c60}')
    @winrt_commethod(6)
    def get_AccessMode(self) -> win32more.Windows.Devices.Custom.IOControlAccessMode: ...
    @winrt_commethod(7)
    def get_BufferingMethod(self) -> win32more.Windows.Devices.Custom.IOControlBufferingMethod: ...
    @winrt_commethod(8)
    def get_Function(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_DeviceType(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_ControlCode(self) -> UInt32: ...
    AccessMode = property(get_AccessMode, None)
    BufferingMethod = property(get_BufferingMethod, None)
    ControlCode = property(get_ControlCode, None)
    DeviceType = property(get_DeviceType, None)
    Function = property(get_Function, None)
class IIOControlCodeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Custom.IIOControlCodeFactory'
    _iid_ = Guid('{856a7cf0-4c11-44ae-afc6-b8d4a212788f}')
    @winrt_commethod(6)
    def CreateIOControlCode(self, deviceType: UInt16, function: UInt16, accessMode: win32more.Windows.Devices.Custom.IOControlAccessMode, bufferingMethod: win32more.Windows.Devices.Custom.IOControlBufferingMethod) -> win32more.Windows.Devices.Custom.IOControlCode: ...
class IKnownDeviceTypesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Custom.IKnownDeviceTypesStatics'
    _iid_ = Guid('{ee5479c2-5448-45da-ad1b-24948c239094}')
    @winrt_commethod(6)
    def get_Unknown(self) -> UInt16: ...
    Unknown = property(get_Unknown, None)
class IOControlAccessMode(Enum, Int32):
    Any = 0
    Read = 1
    Write = 2
    ReadWrite = 3
class IOControlBufferingMethod(Enum, Int32):
    Buffered = 0
    DirectInput = 1
    DirectOutput = 2
    Neither = 3
class IOControlCode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Custom.IIOControlCode
    _classid_ = 'Windows.Devices.Custom.IOControlCode'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Devices.Custom.IOControlCode.CreateIOControlCode(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateIOControlCode(cls: win32more.Windows.Devices.Custom.IIOControlCodeFactory, deviceType: UInt16, function: UInt16, accessMode: win32more.Windows.Devices.Custom.IOControlAccessMode, bufferingMethod: win32more.Windows.Devices.Custom.IOControlBufferingMethod) -> win32more.Windows.Devices.Custom.IOControlCode: ...
    @winrt_mixinmethod
    def get_AccessMode(self: win32more.Windows.Devices.Custom.IIOControlCode) -> win32more.Windows.Devices.Custom.IOControlAccessMode: ...
    @winrt_mixinmethod
    def get_BufferingMethod(self: win32more.Windows.Devices.Custom.IIOControlCode) -> win32more.Windows.Devices.Custom.IOControlBufferingMethod: ...
    @winrt_mixinmethod
    def get_Function(self: win32more.Windows.Devices.Custom.IIOControlCode) -> UInt16: ...
    @winrt_mixinmethod
    def get_DeviceType(self: win32more.Windows.Devices.Custom.IIOControlCode) -> UInt16: ...
    @winrt_mixinmethod
    def get_ControlCode(self: win32more.Windows.Devices.Custom.IIOControlCode) -> UInt32: ...
    AccessMode = property(get_AccessMode, None)
    BufferingMethod = property(get_BufferingMethod, None)
    ControlCode = property(get_ControlCode, None)
    DeviceType = property(get_DeviceType, None)
    Function = property(get_Function, None)
class _KnownDeviceTypes_Meta_(ComPtr.__class__):
    pass
class KnownDeviceTypes(ComPtr, metaclass=_KnownDeviceTypes_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Custom.KnownDeviceTypes'
    @winrt_classmethod
    def get_Unknown(cls: win32more.Windows.Devices.Custom.IKnownDeviceTypesStatics) -> UInt16: ...
    _KnownDeviceTypes_Meta_.Unknown = property(get_Unknown, None)


make_ready(__name__)
