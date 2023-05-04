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
import Windows.Devices.Display
import Windows.Foundation
import Windows.Graphics
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class DisplayMonitor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.IDisplayMonitor
    _classid_ = 'Windows.Devices.Display.DisplayMonitor'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Display.IDisplayMonitor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Devices.Display.IDisplayMonitor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ConnectionKind(self: Windows.Devices.Display.IDisplayMonitor) -> Windows.Devices.Display.DisplayMonitorConnectionKind: ...
    @winrt_mixinmethod
    def get_PhysicalConnector(self: Windows.Devices.Display.IDisplayMonitor) -> Windows.Devices.Display.DisplayMonitorPhysicalConnectorKind: ...
    @winrt_mixinmethod
    def get_DisplayAdapterDeviceId(self: Windows.Devices.Display.IDisplayMonitor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayAdapterId(self: Windows.Devices.Display.IDisplayMonitor) -> Windows.Graphics.DisplayAdapterId: ...
    @winrt_mixinmethod
    def get_DisplayAdapterTargetId(self: Windows.Devices.Display.IDisplayMonitor) -> UInt32: ...
    @winrt_mixinmethod
    def get_UsageKind(self: Windows.Devices.Display.IDisplayMonitor) -> Windows.Devices.Display.DisplayMonitorUsageKind: ...
    @winrt_mixinmethod
    def get_NativeResolutionInRawPixels(self: Windows.Devices.Display.IDisplayMonitor) -> Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def get_PhysicalSizeInInches(self: Windows.Devices.Display.IDisplayMonitor) -> Windows.Foundation.IReference[Windows.Foundation.Size]: ...
    @winrt_mixinmethod
    def get_RawDpiX(self: Windows.Devices.Display.IDisplayMonitor) -> Single: ...
    @winrt_mixinmethod
    def get_RawDpiY(self: Windows.Devices.Display.IDisplayMonitor) -> Single: ...
    @winrt_mixinmethod
    def get_RedPrimary(self: Windows.Devices.Display.IDisplayMonitor) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_GreenPrimary(self: Windows.Devices.Display.IDisplayMonitor) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_BluePrimary(self: Windows.Devices.Display.IDisplayMonitor) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_WhitePoint(self: Windows.Devices.Display.IDisplayMonitor) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_MaxLuminanceInNits(self: Windows.Devices.Display.IDisplayMonitor) -> Single: ...
    @winrt_mixinmethod
    def get_MinLuminanceInNits(self: Windows.Devices.Display.IDisplayMonitor) -> Single: ...
    @winrt_mixinmethod
    def get_MaxAverageFullFrameLuminanceInNits(self: Windows.Devices.Display.IDisplayMonitor) -> Single: ...
    @winrt_mixinmethod
    def GetDescriptor(self: Windows.Devices.Display.IDisplayMonitor, descriptorKind: Windows.Devices.Display.DisplayMonitorDescriptorKind) -> c_char_p_no: ...
    @winrt_mixinmethod
    def get_IsDolbyVisionSupportedInHdrMode(self: Windows.Devices.Display.IDisplayMonitor2) -> Boolean: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Display.IDisplayMonitorStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Display.IDisplayMonitorStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Display.DisplayMonitor]: ...
    @winrt_classmethod
    def FromInterfaceIdAsync(cls: Windows.Devices.Display.IDisplayMonitorStatics, deviceInterfaceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Display.DisplayMonitor]: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1f6b15d4-1d01-4c51-87e2-6f954a772b59}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ConnectionKind(self) -> Windows.Devices.Display.DisplayMonitorConnectionKind: ...
    @winrt_commethod(9)
    def get_PhysicalConnector(self) -> Windows.Devices.Display.DisplayMonitorPhysicalConnectorKind: ...
    @winrt_commethod(10)
    def get_DisplayAdapterDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_DisplayAdapterId(self) -> Windows.Graphics.DisplayAdapterId: ...
    @winrt_commethod(12)
    def get_DisplayAdapterTargetId(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_UsageKind(self) -> Windows.Devices.Display.DisplayMonitorUsageKind: ...
    @winrt_commethod(14)
    def get_NativeResolutionInRawPixels(self) -> Windows.Graphics.SizeInt32: ...
    @winrt_commethod(15)
    def get_PhysicalSizeInInches(self) -> Windows.Foundation.IReference[Windows.Foundation.Size]: ...
    @winrt_commethod(16)
    def get_RawDpiX(self) -> Single: ...
    @winrt_commethod(17)
    def get_RawDpiY(self) -> Single: ...
    @winrt_commethod(18)
    def get_RedPrimary(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(19)
    def get_GreenPrimary(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(20)
    def get_BluePrimary(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(21)
    def get_WhitePoint(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(22)
    def get_MaxLuminanceInNits(self) -> Single: ...
    @winrt_commethod(23)
    def get_MinLuminanceInNits(self) -> Single: ...
    @winrt_commethod(24)
    def get_MaxAverageFullFrameLuminanceInNits(self) -> Single: ...
    @winrt_commethod(25)
    def GetDescriptor(self, descriptorKind: Windows.Devices.Display.DisplayMonitorDescriptorKind) -> c_char_p_no: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{023018e6-cb23-5830-96df-a7bf6e602577}')
    @winrt_commethod(6)
    def get_IsDolbyVisionSupportedInHdrMode(self) -> Boolean: ...
    IsDolbyVisionSupportedInHdrMode = property(get_IsDolbyVisionSupportedInHdrMode, None)
class IDisplayMonitorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6eae698f-a228-4c05-821d-b695d667de8e}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Display.DisplayMonitor]: ...
    @winrt_commethod(8)
    def FromInterfaceIdAsync(self, deviceInterfaceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Display.DisplayMonitor]: ...
make_head(_module, 'DisplayMonitor')
make_head(_module, 'IDisplayMonitor')
make_head(_module, 'IDisplayMonitor2')
make_head(_module, 'IDisplayMonitorStatics')
