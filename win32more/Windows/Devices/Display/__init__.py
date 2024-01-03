from __future__ import annotations
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
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Display
import win32more.Windows.Foundation
import win32more.Windows.Graphics
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
    def GetDescriptor(self: win32more.Windows.Devices.Display.IDisplayMonitor, descriptorKind: win32more.Windows.Devices.Display.DisplayMonitorDescriptorKind) -> SZArray[Byte]: ...
    @winrt_mixinmethod
    def get_IsDolbyVisionSupportedInHdrMode(self: win32more.Windows.Devices.Display.IDisplayMonitor2) -> Boolean: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Display.IDisplayMonitorStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Display.IDisplayMonitorStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Display.DisplayMonitor]: ...
    @winrt_classmethod
    def FromInterfaceIdAsync(cls: win32more.Windows.Devices.Display.IDisplayMonitorStatics, deviceInterfaceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Display.DisplayMonitor]: ...
    DeviceId = property(get_DeviceId, None)
    DisplayName = property(get_DisplayName, None)
    ConnectionKind = property(get_ConnectionKind, None)
    PhysicalConnector = property(get_PhysicalConnector, None)
    DisplayAdapterDeviceId = property(get_DisplayAdapterDeviceId, None)
    DisplayAdapterId = property(get_DisplayAdapterId, None)
    DisplayAdapterTargetId = property(get_DisplayAdapterTargetId, None)
    UsageKind = property(get_UsageKind, None)
    NativeResolutionInRawPixels = property(get_NativeResolutionInRawPixels, None)
    PhysicalSizeInInches = property(get_PhysicalSizeInInches, None)
    RawDpiX = property(get_RawDpiX, None)
    RawDpiY = property(get_RawDpiY, None)
    RedPrimary = property(get_RedPrimary, None)
    GreenPrimary = property(get_GreenPrimary, None)
    BluePrimary = property(get_BluePrimary, None)
    WhitePoint = property(get_WhitePoint, None)
    MaxLuminanceInNits = property(get_MaxLuminanceInNits, None)
    MinLuminanceInNits = property(get_MinLuminanceInNits, None)
    MaxAverageFullFrameLuminanceInNits = property(get_MaxAverageFullFrameLuminanceInNits, None)
    IsDolbyVisionSupportedInHdrMode = property(get_IsDolbyVisionSupportedInHdrMode, None)
DisplayMonitorConnectionKind = Int32
DisplayMonitorConnectionKind_Internal: DisplayMonitorConnectionKind = 0
DisplayMonitorConnectionKind_Wired: DisplayMonitorConnectionKind = 1
DisplayMonitorConnectionKind_Wireless: DisplayMonitorConnectionKind = 2
DisplayMonitorConnectionKind_Virtual: DisplayMonitorConnectionKind = 3
DisplayMonitorDescriptorKind = Int32
DisplayMonitorDescriptorKind_Edid: DisplayMonitorDescriptorKind = 0
DisplayMonitorDescriptorKind_DisplayId: DisplayMonitorDescriptorKind = 1
DisplayMonitorPhysicalConnectorKind = Int32
DisplayMonitorPhysicalConnectorKind_Unknown: DisplayMonitorPhysicalConnectorKind = 0
DisplayMonitorPhysicalConnectorKind_HD15: DisplayMonitorPhysicalConnectorKind = 1
DisplayMonitorPhysicalConnectorKind_AnalogTV: DisplayMonitorPhysicalConnectorKind = 2
DisplayMonitorPhysicalConnectorKind_Dvi: DisplayMonitorPhysicalConnectorKind = 3
DisplayMonitorPhysicalConnectorKind_Hdmi: DisplayMonitorPhysicalConnectorKind = 4
DisplayMonitorPhysicalConnectorKind_Lvds: DisplayMonitorPhysicalConnectorKind = 5
DisplayMonitorPhysicalConnectorKind_Sdi: DisplayMonitorPhysicalConnectorKind = 6
DisplayMonitorPhysicalConnectorKind_DisplayPort: DisplayMonitorPhysicalConnectorKind = 7
DisplayMonitorUsageKind = Int32
DisplayMonitorUsageKind_Standard: DisplayMonitorUsageKind = 0
DisplayMonitorUsageKind_HeadMounted: DisplayMonitorUsageKind = 1
DisplayMonitorUsageKind_SpecialPurpose: DisplayMonitorUsageKind = 2
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
    def GetDescriptor(self, descriptorKind: win32more.Windows.Devices.Display.DisplayMonitorDescriptorKind) -> SZArray[Byte]: ...
    DeviceId = property(get_DeviceId, None)
    DisplayName = property(get_DisplayName, None)
    ConnectionKind = property(get_ConnectionKind, None)
    PhysicalConnector = property(get_PhysicalConnector, None)
    DisplayAdapterDeviceId = property(get_DisplayAdapterDeviceId, None)
    DisplayAdapterId = property(get_DisplayAdapterId, None)
    DisplayAdapterTargetId = property(get_DisplayAdapterTargetId, None)
    UsageKind = property(get_UsageKind, None)
    NativeResolutionInRawPixels = property(get_NativeResolutionInRawPixels, None)
    PhysicalSizeInInches = property(get_PhysicalSizeInInches, None)
    RawDpiX = property(get_RawDpiX, None)
    RawDpiY = property(get_RawDpiY, None)
    RedPrimary = property(get_RedPrimary, None)
    GreenPrimary = property(get_GreenPrimary, None)
    BluePrimary = property(get_BluePrimary, None)
    WhitePoint = property(get_WhitePoint, None)
    MaxLuminanceInNits = property(get_MaxLuminanceInNits, None)
    MinLuminanceInNits = property(get_MinLuminanceInNits, None)
    MaxAverageFullFrameLuminanceInNits = property(get_MaxAverageFullFrameLuminanceInNits, None)
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
