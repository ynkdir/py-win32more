from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Display
import win32more.Windows.Foundation
import win32more.Windows.Graphics
import win32more.Windows.Win32.System.WinRT
class DisplayMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Display.IDisplayMonitor
    _classid_ = 'Windows.Devices.Display.DisplayMonitor'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConnectionKind(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> win32more.Windows.Devices.Display.DisplayMonitorConnectionKind: ...
    @winrt_mixinmethod
    def get_PhysicalConnector(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> win32more.Windows.Devices.Display.DisplayMonitorPhysicalConnectorKind: ...
    @winrt_mixinmethod
    def get_DisplayAdapterDeviceId(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayAdapterId(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> win32more.Windows.Graphics.DisplayAdapterId: ...
    @winrt_mixinmethod
    def get_DisplayAdapterTargetId(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> UInt32: ...
    @winrt_mixinmethod
    def get_UsageKind(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> win32more.Windows.Devices.Display.DisplayMonitorUsageKind: ...
    @winrt_mixinmethod
    def get_NativeResolutionInRawPixels(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def get_PhysicalSizeInInches(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Size]: ...
    @winrt_mixinmethod
    def get_RawDpiX(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> Single: ...
    @winrt_mixinmethod
    def get_RawDpiY(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> Single: ...
    @winrt_mixinmethod
    def get_RedPrimary(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_GreenPrimary(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_BluePrimary(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_WhitePoint(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_MaxLuminanceInNits(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> Single: ...
    @winrt_mixinmethod
    def get_MinLuminanceInNits(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> Single: ...
    @winrt_mixinmethod
    def get_MaxAverageFullFrameLuminanceInNits(self: win32more.Windows.Devices.Display.IDisplayMonitor) -> Single: ...
    @winrt_mixinmethod
    def GetDescriptor(self: win32more.Windows.Devices.Display.IDisplayMonitor, descriptorKind: win32more.Windows.Devices.Display.DisplayMonitorDescriptorKind) -> ReceiveArray[Byte]: ...
    @winrt_mixinmethod
    def get_IsDolbyVisionSupportedInHdrMode(self: win32more.Windows.Devices.Display.IDisplayMonitor2) -> Boolean: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Display.IDisplayMonitorStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Display.IDisplayMonitorStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Display.DisplayMonitor]: ...
    @winrt_classmethod
    def FromInterfaceIdAsync(cls: win32more.Windows.Devices.Display.IDisplayMonitorStatics, deviceInterfaceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Display.DisplayMonitor]: ...
    BluePrimary = property(get_BluePrimary, None)
    ConnectionKind = property(get_ConnectionKind, None)
    DeviceId = property(get_DeviceId, None)
    DisplayAdapterDeviceId = property(get_DisplayAdapterDeviceId, None)
    DisplayAdapterId = property(get_DisplayAdapterId, None)
    DisplayAdapterTargetId = property(get_DisplayAdapterTargetId, None)
    DisplayName = property(get_DisplayName, None)
    GreenPrimary = property(get_GreenPrimary, None)
    IsDolbyVisionSupportedInHdrMode = property(get_IsDolbyVisionSupportedInHdrMode, None)
    MaxAverageFullFrameLuminanceInNits = property(get_MaxAverageFullFrameLuminanceInNits, None)
    MaxLuminanceInNits = property(get_MaxLuminanceInNits, None)
    MinLuminanceInNits = property(get_MinLuminanceInNits, None)
    NativeResolutionInRawPixels = property(get_NativeResolutionInRawPixels, None)
    PhysicalConnector = property(get_PhysicalConnector, None)
    PhysicalSizeInInches = property(get_PhysicalSizeInInches, None)
    RawDpiX = property(get_RawDpiX, None)
    RawDpiY = property(get_RawDpiY, None)
    RedPrimary = property(get_RedPrimary, None)
    UsageKind = property(get_UsageKind, None)
    WhitePoint = property(get_WhitePoint, None)
class DisplayMonitorConnectionKind(Enum, Int32):
    Internal = 0
    Wired = 1
    Wireless = 2
    Virtual = 3
class DisplayMonitorDescriptorKind(Enum, Int32):
    Edid = 0
    DisplayId = 1
class DisplayMonitorPhysicalConnectorKind(Enum, Int32):
    Unknown = 0
    HD15 = 1
    AnalogTV = 2
    Dvi = 3
    Hdmi = 4
    Lvds = 5
    Sdi = 6
    DisplayPort = 7
class DisplayMonitorUsageKind(Enum, Int32):
    Standard = 0
    HeadMounted = 1
    SpecialPurpose = 2
class IDisplayMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.IDisplayMonitor'
    _iid_ = Guid('{1f6b15d4-1d01-4c51-87e2-6f954a772b59}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ConnectionKind(self) -> win32more.Windows.Devices.Display.DisplayMonitorConnectionKind: ...
    @winrt_commethod(9)
    def get_PhysicalConnector(self) -> win32more.Windows.Devices.Display.DisplayMonitorPhysicalConnectorKind: ...
    @winrt_commethod(10)
    def get_DisplayAdapterDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_DisplayAdapterId(self) -> win32more.Windows.Graphics.DisplayAdapterId: ...
    @winrt_commethod(12)
    def get_DisplayAdapterTargetId(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_UsageKind(self) -> win32more.Windows.Devices.Display.DisplayMonitorUsageKind: ...
    @winrt_commethod(14)
    def get_NativeResolutionInRawPixels(self) -> win32more.Windows.Graphics.SizeInt32: ...
    @winrt_commethod(15)
    def get_PhysicalSizeInInches(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Size]: ...
    @winrt_commethod(16)
    def get_RawDpiX(self) -> Single: ...
    @winrt_commethod(17)
    def get_RawDpiY(self) -> Single: ...
    @winrt_commethod(18)
    def get_RedPrimary(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(19)
    def get_GreenPrimary(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(20)
    def get_BluePrimary(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(21)
    def get_WhitePoint(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(22)
    def get_MaxLuminanceInNits(self) -> Single: ...
    @winrt_commethod(23)
    def get_MinLuminanceInNits(self) -> Single: ...
    @winrt_commethod(24)
    def get_MaxAverageFullFrameLuminanceInNits(self) -> Single: ...
    @winrt_commethod(25)
    def GetDescriptor(self, descriptorKind: win32more.Windows.Devices.Display.DisplayMonitorDescriptorKind) -> ReceiveArray[Byte]: ...
    BluePrimary = property(get_BluePrimary, None)
    ConnectionKind = property(get_ConnectionKind, None)
    DeviceId = property(get_DeviceId, None)
    DisplayAdapterDeviceId = property(get_DisplayAdapterDeviceId, None)
    DisplayAdapterId = property(get_DisplayAdapterId, None)
    DisplayAdapterTargetId = property(get_DisplayAdapterTargetId, None)
    DisplayName = property(get_DisplayName, None)
    GreenPrimary = property(get_GreenPrimary, None)
    MaxAverageFullFrameLuminanceInNits = property(get_MaxAverageFullFrameLuminanceInNits, None)
    MaxLuminanceInNits = property(get_MaxLuminanceInNits, None)
    MinLuminanceInNits = property(get_MinLuminanceInNits, None)
    NativeResolutionInRawPixels = property(get_NativeResolutionInRawPixels, None)
    PhysicalConnector = property(get_PhysicalConnector, None)
    PhysicalSizeInInches = property(get_PhysicalSizeInInches, None)
    RawDpiX = property(get_RawDpiX, None)
    RawDpiY = property(get_RawDpiY, None)
    RedPrimary = property(get_RedPrimary, None)
    UsageKind = property(get_UsageKind, None)
    WhitePoint = property(get_WhitePoint, None)
class IDisplayMonitor2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.IDisplayMonitor2'
    _iid_ = Guid('{023018e6-cb23-5830-96df-a7bf6e602577}')
    @winrt_commethod(6)
    def get_IsDolbyVisionSupportedInHdrMode(self) -> Boolean: ...
    IsDolbyVisionSupportedInHdrMode = property(get_IsDolbyVisionSupportedInHdrMode, None)
class IDisplayMonitorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.IDisplayMonitorStatics'
    _iid_ = Guid('{6eae698f-a228-4c05-821d-b695d667de8e}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Display.DisplayMonitor]: ...
    @winrt_commethod(8)
    def FromInterfaceIdAsync(self, deviceInterfaceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Display.DisplayMonitor]: ...


make_ready(__name__)
