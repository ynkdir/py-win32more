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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Devices.Display
import Windows.Devices.Display.Core
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Foundation.Numerics
import Windows.Graphics
import Windows.Graphics.DirectX
import Windows.Graphics.DirectX.Direct3D11
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
class DisplayAdapter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayAdapter
    _classid_ = 'Windows.Devices.Display.Core.DisplayAdapter'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Display.Core.IDisplayAdapter) -> Windows.Graphics.DisplayAdapterId: ...
    @winrt_mixinmethod
    def get_DeviceInterfacePath(self: Windows.Devices.Display.Core.IDisplayAdapter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SourceCount(self: Windows.Devices.Display.Core.IDisplayAdapter) -> UInt32: ...
    @winrt_mixinmethod
    def get_PciVendorId(self: Windows.Devices.Display.Core.IDisplayAdapter) -> UInt32: ...
    @winrt_mixinmethod
    def get_PciDeviceId(self: Windows.Devices.Display.Core.IDisplayAdapter) -> UInt32: ...
    @winrt_mixinmethod
    def get_PciSubSystemId(self: Windows.Devices.Display.Core.IDisplayAdapter) -> UInt32: ...
    @winrt_mixinmethod
    def get_PciRevision(self: Windows.Devices.Display.Core.IDisplayAdapter) -> UInt32: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Display.Core.IDisplayAdapter) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_classmethod
    def FromId(cls: Windows.Devices.Display.Core.IDisplayAdapterStatics, id: Windows.Graphics.DisplayAdapterId) -> Windows.Devices.Display.Core.DisplayAdapter: ...
    Id = property(get_Id, None)
    DeviceInterfacePath = property(get_DeviceInterfacePath, None)
    SourceCount = property(get_SourceCount, None)
    PciVendorId = property(get_PciVendorId, None)
    PciDeviceId = property(get_PciDeviceId, None)
    PciSubSystemId = property(get_PciSubSystemId, None)
    PciRevision = property(get_PciRevision, None)
    Properties = property(get_Properties, None)
DisplayBitsPerChannel = UInt32
DisplayBitsPerChannel_None: DisplayBitsPerChannel = 0
DisplayBitsPerChannel_Bpc6: DisplayBitsPerChannel = 1
DisplayBitsPerChannel_Bpc8: DisplayBitsPerChannel = 2
DisplayBitsPerChannel_Bpc10: DisplayBitsPerChannel = 4
DisplayBitsPerChannel_Bpc12: DisplayBitsPerChannel = 8
DisplayBitsPerChannel_Bpc14: DisplayBitsPerChannel = 16
DisplayBitsPerChannel_Bpc16: DisplayBitsPerChannel = 32
class DisplayDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayDevice
    _classid_ = 'Windows.Devices.Display.Core.DisplayDevice'
    @winrt_mixinmethod
    def CreateScanoutSource(self: Windows.Devices.Display.Core.IDisplayDevice, target: Windows.Devices.Display.Core.DisplayTarget) -> Windows.Devices.Display.Core.DisplaySource: ...
    @winrt_mixinmethod
    def CreatePrimary(self: Windows.Devices.Display.Core.IDisplayDevice, target: Windows.Devices.Display.Core.DisplayTarget, desc: Windows.Devices.Display.Core.DisplayPrimaryDescription) -> Windows.Devices.Display.Core.DisplaySurface: ...
    @winrt_mixinmethod
    def CreateTaskPool(self: Windows.Devices.Display.Core.IDisplayDevice) -> Windows.Devices.Display.Core.DisplayTaskPool: ...
    @winrt_mixinmethod
    def CreatePeriodicFence(self: Windows.Devices.Display.Core.IDisplayDevice, target: Windows.Devices.Display.Core.DisplayTarget, offsetFromVBlank: Windows.Foundation.TimeSpan) -> Windows.Devices.Display.Core.DisplayFence: ...
    @winrt_mixinmethod
    def WaitForVBlank(self: Windows.Devices.Display.Core.IDisplayDevice, source: Windows.Devices.Display.Core.DisplaySource) -> Void: ...
    @winrt_mixinmethod
    def CreateSimpleScanout(self: Windows.Devices.Display.Core.IDisplayDevice, pSource: Windows.Devices.Display.Core.DisplaySource, pSurface: Windows.Devices.Display.Core.DisplaySurface, SubResourceIndex: UInt32, SyncInterval: UInt32) -> Windows.Devices.Display.Core.DisplayScanout: ...
    @winrt_mixinmethod
    def IsCapabilitySupported(self: Windows.Devices.Display.Core.IDisplayDevice, capability: Windows.Devices.Display.Core.DisplayDeviceCapability) -> Boolean: ...
    @winrt_mixinmethod
    def CreateSimpleScanoutWithDirtyRectsAndOptions(self: Windows.Devices.Display.Core.IDisplayDevice2, source: Windows.Devices.Display.Core.DisplaySource, surface: Windows.Devices.Display.Core.DisplaySurface, subresourceIndex: UInt32, syncInterval: UInt32, dirtyRects: Windows.Foundation.Collections.IIterable[Windows.Graphics.RectInt32], options: Windows.Devices.Display.Core.DisplayScanoutOptions) -> Windows.Devices.Display.Core.DisplayScanout: ...
DisplayDeviceCapability = Int32
DisplayDeviceCapability_FlipOverride: DisplayDeviceCapability = 0
class DisplayFence(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayFence
    _classid_ = 'Windows.Devices.Display.Core.DisplayFence'
class DisplayManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayManager
    _classid_ = 'Windows.Devices.Display.Core.DisplayManager'
    @winrt_mixinmethod
    def GetCurrentTargets(self: Windows.Devices.Display.Core.IDisplayManager) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Display.Core.DisplayTarget]: ...
    @winrt_mixinmethod
    def GetCurrentAdapters(self: Windows.Devices.Display.Core.IDisplayManager) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Display.Core.DisplayAdapter]: ...
    @winrt_mixinmethod
    def TryAcquireTarget(self: Windows.Devices.Display.Core.IDisplayManager, target: Windows.Devices.Display.Core.DisplayTarget) -> Windows.Devices.Display.Core.DisplayManagerResult: ...
    @winrt_mixinmethod
    def ReleaseTarget(self: Windows.Devices.Display.Core.IDisplayManager, target: Windows.Devices.Display.Core.DisplayTarget) -> Void: ...
    @winrt_mixinmethod
    def TryReadCurrentStateForAllTargets(self: Windows.Devices.Display.Core.IDisplayManager) -> Windows.Devices.Display.Core.DisplayManagerResultWithState: ...
    @winrt_mixinmethod
    def TryAcquireTargetsAndReadCurrentState(self: Windows.Devices.Display.Core.IDisplayManager, targets: Windows.Foundation.Collections.IIterable[Windows.Devices.Display.Core.DisplayTarget]) -> Windows.Devices.Display.Core.DisplayManagerResultWithState: ...
    @winrt_mixinmethod
    def TryAcquireTargetsAndCreateEmptyState(self: Windows.Devices.Display.Core.IDisplayManager, targets: Windows.Foundation.Collections.IIterable[Windows.Devices.Display.Core.DisplayTarget]) -> Windows.Devices.Display.Core.DisplayManagerResultWithState: ...
    @winrt_mixinmethod
    def TryAcquireTargetsAndCreateSubstate(self: Windows.Devices.Display.Core.IDisplayManager, existingState: Windows.Devices.Display.Core.DisplayState, targets: Windows.Foundation.Collections.IIterable[Windows.Devices.Display.Core.DisplayTarget]) -> Windows.Devices.Display.Core.DisplayManagerResultWithState: ...
    @winrt_mixinmethod
    def CreateDisplayDevice(self: Windows.Devices.Display.Core.IDisplayManager, adapter: Windows.Devices.Display.Core.DisplayAdapter) -> Windows.Devices.Display.Core.DisplayDevice: ...
    @winrt_mixinmethod
    def add_Enabled(self: Windows.Devices.Display.Core.IDisplayManager, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Display.Core.DisplayManager, Windows.Devices.Display.Core.DisplayManagerEnabledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Enabled(self: Windows.Devices.Display.Core.IDisplayManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Disabled(self: Windows.Devices.Display.Core.IDisplayManager, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Display.Core.DisplayManager, Windows.Devices.Display.Core.DisplayManagerDisabledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Disabled(self: Windows.Devices.Display.Core.IDisplayManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Changed(self: Windows.Devices.Display.Core.IDisplayManager, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Display.Core.DisplayManager, Windows.Devices.Display.Core.DisplayManagerChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: Windows.Devices.Display.Core.IDisplayManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PathsFailedOrInvalidated(self: Windows.Devices.Display.Core.IDisplayManager, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Display.Core.DisplayManager, Windows.Devices.Display.Core.DisplayManagerPathsFailedOrInvalidatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PathsFailedOrInvalidated(self: Windows.Devices.Display.Core.IDisplayManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Display.Core.IDisplayManager) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Display.Core.IDisplayManager) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def Create(cls: Windows.Devices.Display.Core.IDisplayManagerStatics, options: Windows.Devices.Display.Core.DisplayManagerOptions) -> Windows.Devices.Display.Core.DisplayManager: ...
class DisplayManagerChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayManagerChangedEventArgs
    _classid_ = 'Windows.Devices.Display.Core.DisplayManagerChangedEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: Windows.Devices.Display.Core.IDisplayManagerChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.Devices.Display.Core.IDisplayManagerChangedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.Display.Core.IDisplayManagerChangedEventArgs) -> Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
class DisplayManagerDisabledEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayManagerDisabledEventArgs
    _classid_ = 'Windows.Devices.Display.Core.DisplayManagerDisabledEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: Windows.Devices.Display.Core.IDisplayManagerDisabledEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.Devices.Display.Core.IDisplayManagerDisabledEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.Display.Core.IDisplayManagerDisabledEventArgs) -> Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
class DisplayManagerEnabledEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayManagerEnabledEventArgs
    _classid_ = 'Windows.Devices.Display.Core.DisplayManagerEnabledEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: Windows.Devices.Display.Core.IDisplayManagerEnabledEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.Devices.Display.Core.IDisplayManagerEnabledEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.Display.Core.IDisplayManagerEnabledEventArgs) -> Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
DisplayManagerOptions = UInt32
DisplayManagerOptions_None: DisplayManagerOptions = 0
DisplayManagerOptions_EnforceSourceOwnership: DisplayManagerOptions = 1
DisplayManagerOptions_VirtualRefreshRateAware: DisplayManagerOptions = 2
class DisplayManagerPathsFailedOrInvalidatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayManagerPathsFailedOrInvalidatedEventArgs
    _classid_ = 'Windows.Devices.Display.Core.DisplayManagerPathsFailedOrInvalidatedEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: Windows.Devices.Display.Core.IDisplayManagerPathsFailedOrInvalidatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.Devices.Display.Core.IDisplayManagerPathsFailedOrInvalidatedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.Display.Core.IDisplayManagerPathsFailedOrInvalidatedEventArgs) -> Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
DisplayManagerResult = Int32
DisplayManagerResult_Success: DisplayManagerResult = 0
DisplayManagerResult_UnknownFailure: DisplayManagerResult = 1
DisplayManagerResult_TargetAccessDenied: DisplayManagerResult = 2
DisplayManagerResult_TargetStale: DisplayManagerResult = 3
DisplayManagerResult_RemoteSessionNotSupported: DisplayManagerResult = 4
class DisplayManagerResultWithState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayManagerResultWithState
    _classid_ = 'Windows.Devices.Display.Core.DisplayManagerResultWithState'
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.Devices.Display.Core.IDisplayManagerResultWithState) -> Windows.Devices.Display.Core.DisplayManagerResult: ...
    @winrt_mixinmethod
    def get_ExtendedErrorCode(self: Windows.Devices.Display.Core.IDisplayManagerResultWithState) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Devices.Display.Core.IDisplayManagerResultWithState) -> Windows.Devices.Display.Core.DisplayState: ...
    ErrorCode = property(get_ErrorCode, None)
    ExtendedErrorCode = property(get_ExtendedErrorCode, None)
    State = property(get_State, None)
class DisplayModeInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayModeInfo
    _classid_ = 'Windows.Devices.Display.Core.DisplayModeInfo'
    @winrt_mixinmethod
    def get_SourceResolution(self: Windows.Devices.Display.Core.IDisplayModeInfo) -> Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def get_IsStereo(self: Windows.Devices.Display.Core.IDisplayModeInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_SourcePixelFormat(self: Windows.Devices.Display.Core.IDisplayModeInfo) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def get_TargetResolution(self: Windows.Devices.Display.Core.IDisplayModeInfo) -> Windows.Graphics.SizeInt32: ...
    @winrt_mixinmethod
    def get_PresentationRate(self: Windows.Devices.Display.Core.IDisplayModeInfo) -> Windows.Devices.Display.Core.DisplayPresentationRate: ...
    @winrt_mixinmethod
    def get_IsInterlaced(self: Windows.Devices.Display.Core.IDisplayModeInfo) -> Boolean: ...
    @winrt_mixinmethod
    def GetWireFormatSupportedBitsPerChannel(self: Windows.Devices.Display.Core.IDisplayModeInfo, encoding: Windows.Devices.Display.Core.DisplayWireFormatPixelEncoding) -> Windows.Devices.Display.Core.DisplayBitsPerChannel: ...
    @winrt_mixinmethod
    def IsWireFormatSupported(self: Windows.Devices.Display.Core.IDisplayModeInfo, wireFormat: Windows.Devices.Display.Core.DisplayWireFormat) -> Boolean: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Display.Core.IDisplayModeInfo) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_PhysicalPresentationRate(self: Windows.Devices.Display.Core.IDisplayModeInfo2) -> Windows.Devices.Display.Core.DisplayPresentationRate: ...
    SourceResolution = property(get_SourceResolution, None)
    IsStereo = property(get_IsStereo, None)
    SourcePixelFormat = property(get_SourcePixelFormat, None)
    TargetResolution = property(get_TargetResolution, None)
    PresentationRate = property(get_PresentationRate, None)
    IsInterlaced = property(get_IsInterlaced, None)
    Properties = property(get_Properties, None)
    PhysicalPresentationRate = property(get_PhysicalPresentationRate, None)
DisplayModeQueryOptions = UInt32
DisplayModeQueryOptions_None: DisplayModeQueryOptions = 0
DisplayModeQueryOptions_OnlyPreferredResolution: DisplayModeQueryOptions = 1
class DisplayPath(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayPath
    _classid_ = 'Windows.Devices.Display.Core.DisplayPath'
    @winrt_mixinmethod
    def get_View(self: Windows.Devices.Display.Core.IDisplayPath) -> Windows.Devices.Display.Core.DisplayView: ...
    @winrt_mixinmethod
    def get_Target(self: Windows.Devices.Display.Core.IDisplayPath) -> Windows.Devices.Display.Core.DisplayTarget: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Display.Core.IDisplayPath) -> Windows.Devices.Display.Core.DisplayPathStatus: ...
    @winrt_mixinmethod
    def get_SourceResolution(self: Windows.Devices.Display.Core.IDisplayPath) -> Windows.Foundation.IReference[Windows.Graphics.SizeInt32]: ...
    @winrt_mixinmethod
    def put_SourceResolution(self: Windows.Devices.Display.Core.IDisplayPath, value: Windows.Foundation.IReference[Windows.Graphics.SizeInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_SourcePixelFormat(self: Windows.Devices.Display.Core.IDisplayPath) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def put_SourcePixelFormat(self: Windows.Devices.Display.Core.IDisplayPath, value: Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_mixinmethod
    def get_IsStereo(self: Windows.Devices.Display.Core.IDisplayPath) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStereo(self: Windows.Devices.Display.Core.IDisplayPath, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TargetResolution(self: Windows.Devices.Display.Core.IDisplayPath) -> Windows.Foundation.IReference[Windows.Graphics.SizeInt32]: ...
    @winrt_mixinmethod
    def put_TargetResolution(self: Windows.Devices.Display.Core.IDisplayPath, value: Windows.Foundation.IReference[Windows.Graphics.SizeInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_PresentationRate(self: Windows.Devices.Display.Core.IDisplayPath) -> Windows.Foundation.IReference[Windows.Devices.Display.Core.DisplayPresentationRate]: ...
    @winrt_mixinmethod
    def put_PresentationRate(self: Windows.Devices.Display.Core.IDisplayPath, value: Windows.Foundation.IReference[Windows.Devices.Display.Core.DisplayPresentationRate]) -> Void: ...
    @winrt_mixinmethod
    def get_IsInterlaced(self: Windows.Devices.Display.Core.IDisplayPath) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_mixinmethod
    def put_IsInterlaced(self: Windows.Devices.Display.Core.IDisplayPath, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_mixinmethod
    def get_WireFormat(self: Windows.Devices.Display.Core.IDisplayPath) -> Windows.Devices.Display.Core.DisplayWireFormat: ...
    @winrt_mixinmethod
    def put_WireFormat(self: Windows.Devices.Display.Core.IDisplayPath, value: Windows.Devices.Display.Core.DisplayWireFormat) -> Void: ...
    @winrt_mixinmethod
    def get_Rotation(self: Windows.Devices.Display.Core.IDisplayPath) -> Windows.Devices.Display.Core.DisplayRotation: ...
    @winrt_mixinmethod
    def put_Rotation(self: Windows.Devices.Display.Core.IDisplayPath, value: Windows.Devices.Display.Core.DisplayRotation) -> Void: ...
    @winrt_mixinmethod
    def get_Scaling(self: Windows.Devices.Display.Core.IDisplayPath) -> Windows.Devices.Display.Core.DisplayPathScaling: ...
    @winrt_mixinmethod
    def put_Scaling(self: Windows.Devices.Display.Core.IDisplayPath, value: Windows.Devices.Display.Core.DisplayPathScaling) -> Void: ...
    @winrt_mixinmethod
    def FindModes(self: Windows.Devices.Display.Core.IDisplayPath, flags: Windows.Devices.Display.Core.DisplayModeQueryOptions) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Display.Core.DisplayModeInfo]: ...
    @winrt_mixinmethod
    def ApplyPropertiesFromMode(self: Windows.Devices.Display.Core.IDisplayPath, modeResult: Windows.Devices.Display.Core.DisplayModeInfo) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Display.Core.IDisplayPath) -> Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_PhysicalPresentationRate(self: Windows.Devices.Display.Core.IDisplayPath2) -> Windows.Foundation.IReference[Windows.Devices.Display.Core.DisplayPresentationRate]: ...
    @winrt_mixinmethod
    def put_PhysicalPresentationRate(self: Windows.Devices.Display.Core.IDisplayPath2, value: Windows.Foundation.IReference[Windows.Devices.Display.Core.DisplayPresentationRate]) -> Void: ...
    View = property(get_View, None)
    Target = property(get_Target, None)
    Status = property(get_Status, None)
    SourceResolution = property(get_SourceResolution, put_SourceResolution)
    SourcePixelFormat = property(get_SourcePixelFormat, put_SourcePixelFormat)
    IsStereo = property(get_IsStereo, put_IsStereo)
    TargetResolution = property(get_TargetResolution, put_TargetResolution)
    PresentationRate = property(get_PresentationRate, put_PresentationRate)
    IsInterlaced = property(get_IsInterlaced, put_IsInterlaced)
    WireFormat = property(get_WireFormat, put_WireFormat)
    Rotation = property(get_Rotation, put_Rotation)
    Scaling = property(get_Scaling, put_Scaling)
    Properties = property(get_Properties, None)
    PhysicalPresentationRate = property(get_PhysicalPresentationRate, put_PhysicalPresentationRate)
DisplayPathScaling = Int32
DisplayPathScaling_Identity: DisplayPathScaling = 0
DisplayPathScaling_Centered: DisplayPathScaling = 1
DisplayPathScaling_Stretched: DisplayPathScaling = 2
DisplayPathScaling_AspectRatioStretched: DisplayPathScaling = 3
DisplayPathScaling_Custom: DisplayPathScaling = 4
DisplayPathScaling_DriverPreferred: DisplayPathScaling = 5
DisplayPathStatus = Int32
DisplayPathStatus_Unknown: DisplayPathStatus = 0
DisplayPathStatus_Succeeded: DisplayPathStatus = 1
DisplayPathStatus_Pending: DisplayPathStatus = 2
DisplayPathStatus_Failed: DisplayPathStatus = 3
DisplayPathStatus_FailedAsync: DisplayPathStatus = 4
DisplayPathStatus_InvalidatedAsync: DisplayPathStatus = 5
DisplayPresentStatus = Int32
DisplayPresentStatus_Success: DisplayPresentStatus = 0
DisplayPresentStatus_SourceStatusPreventedPresent: DisplayPresentStatus = 1
DisplayPresentStatus_ScanoutInvalid: DisplayPresentStatus = 2
DisplayPresentStatus_SourceInvalid: DisplayPresentStatus = 3
DisplayPresentStatus_DeviceInvalid: DisplayPresentStatus = 4
DisplayPresentStatus_UnknownFailure: DisplayPresentStatus = 5
class DisplayPresentationRate(EasyCastStructure):
    VerticalSyncRate: Windows.Foundation.Numerics.Rational
    VerticalSyncsPerPresentation: Int32
class DisplayPrimaryDescription(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayPrimaryDescription
    _classid_ = 'Windows.Devices.Display.Core.DisplayPrimaryDescription'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Devices.Display.Core.IDisplayPrimaryDescriptionFactory, width: UInt32, height: UInt32, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, colorSpace: Windows.Graphics.DirectX.DirectXColorSpace, isStereo: Boolean, multisampleDescription: Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription) -> Windows.Devices.Display.Core.DisplayPrimaryDescription: ...
    @winrt_mixinmethod
    def get_Width(self: Windows.Devices.Display.Core.IDisplayPrimaryDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.Devices.Display.Core.IDisplayPrimaryDescription) -> UInt32: ...
    @winrt_mixinmethod
    def get_Format(self: Windows.Devices.Display.Core.IDisplayPrimaryDescription) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_mixinmethod
    def get_ColorSpace(self: Windows.Devices.Display.Core.IDisplayPrimaryDescription) -> Windows.Graphics.DirectX.DirectXColorSpace: ...
    @winrt_mixinmethod
    def get_IsStereo(self: Windows.Devices.Display.Core.IDisplayPrimaryDescription) -> Boolean: ...
    @winrt_mixinmethod
    def get_MultisampleDescription(self: Windows.Devices.Display.Core.IDisplayPrimaryDescription) -> Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Display.Core.IDisplayPrimaryDescription) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_classmethod
    def CreateWithProperties(cls: Windows.Devices.Display.Core.IDisplayPrimaryDescriptionStatics, extraProperties: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[Guid, Windows.Win32.System.WinRT.IInspectable_head]], width: UInt32, height: UInt32, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, colorSpace: Windows.Graphics.DirectX.DirectXColorSpace, isStereo: Boolean, multisampleDescription: Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription) -> Windows.Devices.Display.Core.DisplayPrimaryDescription: ...
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Format = property(get_Format, None)
    ColorSpace = property(get_ColorSpace, None)
    IsStereo = property(get_IsStereo, None)
    MultisampleDescription = property(get_MultisampleDescription, None)
    Properties = property(get_Properties, None)
DisplayRotation = Int32
DisplayRotation_None: DisplayRotation = 0
DisplayRotation_Clockwise90Degrees: DisplayRotation = 1
DisplayRotation_Clockwise180Degrees: DisplayRotation = 2
DisplayRotation_Clockwise270Degrees: DisplayRotation = 3
class DisplayScanout(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayScanout
    _classid_ = 'Windows.Devices.Display.Core.DisplayScanout'
DisplayScanoutOptions = UInt32
DisplayScanoutOptions_None: DisplayScanoutOptions = 0
DisplayScanoutOptions_AllowTearing: DisplayScanoutOptions = 2
class DisplaySource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplaySource
    _classid_ = 'Windows.Devices.Display.Core.DisplaySource'
    @winrt_mixinmethod
    def get_AdapterId(self: Windows.Devices.Display.Core.IDisplaySource) -> Windows.Graphics.DisplayAdapterId: ...
    @winrt_mixinmethod
    def get_SourceId(self: Windows.Devices.Display.Core.IDisplaySource) -> UInt32: ...
    @winrt_mixinmethod
    def GetMetadata(self: Windows.Devices.Display.Core.IDisplaySource, Key: Guid) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Display.Core.IDisplaySource2) -> Windows.Devices.Display.Core.DisplaySourceStatus: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: Windows.Devices.Display.Core.IDisplaySource2, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Display.Core.DisplaySource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: Windows.Devices.Display.Core.IDisplaySource2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    AdapterId = property(get_AdapterId, None)
    SourceId = property(get_SourceId, None)
    Status = property(get_Status, None)
DisplaySourceStatus = Int32
DisplaySourceStatus_Active: DisplaySourceStatus = 0
DisplaySourceStatus_PoweredOff: DisplaySourceStatus = 1
DisplaySourceStatus_Invalid: DisplaySourceStatus = 2
DisplaySourceStatus_OwnedByAnotherDevice: DisplaySourceStatus = 3
DisplaySourceStatus_Unowned: DisplaySourceStatus = 4
class DisplayState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayState
    _classid_ = 'Windows.Devices.Display.Core.DisplayState'
    @winrt_mixinmethod
    def get_IsReadOnly(self: Windows.Devices.Display.Core.IDisplayState) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStale(self: Windows.Devices.Display.Core.IDisplayState) -> Boolean: ...
    @winrt_mixinmethod
    def get_Targets(self: Windows.Devices.Display.Core.IDisplayState) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Display.Core.DisplayTarget]: ...
    @winrt_mixinmethod
    def get_Views(self: Windows.Devices.Display.Core.IDisplayState) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Display.Core.DisplayView]: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Display.Core.IDisplayState) -> Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def ConnectTarget(self: Windows.Devices.Display.Core.IDisplayState, target: Windows.Devices.Display.Core.DisplayTarget) -> Windows.Devices.Display.Core.DisplayPath: ...
    @winrt_mixinmethod
    def ConnectTargetToView(self: Windows.Devices.Display.Core.IDisplayState, target: Windows.Devices.Display.Core.DisplayTarget, view: Windows.Devices.Display.Core.DisplayView) -> Windows.Devices.Display.Core.DisplayPath: ...
    @winrt_mixinmethod
    def CanConnectTargetToView(self: Windows.Devices.Display.Core.IDisplayState, target: Windows.Devices.Display.Core.DisplayTarget, view: Windows.Devices.Display.Core.DisplayView) -> Boolean: ...
    @winrt_mixinmethod
    def GetViewForTarget(self: Windows.Devices.Display.Core.IDisplayState, target: Windows.Devices.Display.Core.DisplayTarget) -> Windows.Devices.Display.Core.DisplayView: ...
    @winrt_mixinmethod
    def GetPathForTarget(self: Windows.Devices.Display.Core.IDisplayState, target: Windows.Devices.Display.Core.DisplayTarget) -> Windows.Devices.Display.Core.DisplayPath: ...
    @winrt_mixinmethod
    def DisconnectTarget(self: Windows.Devices.Display.Core.IDisplayState, target: Windows.Devices.Display.Core.DisplayTarget) -> Void: ...
    @winrt_mixinmethod
    def TryFunctionalize(self: Windows.Devices.Display.Core.IDisplayState, options: Windows.Devices.Display.Core.DisplayStateFunctionalizeOptions) -> Windows.Devices.Display.Core.DisplayStateOperationResult: ...
    @winrt_mixinmethod
    def TryApply(self: Windows.Devices.Display.Core.IDisplayState, options: Windows.Devices.Display.Core.DisplayStateApplyOptions) -> Windows.Devices.Display.Core.DisplayStateOperationResult: ...
    @winrt_mixinmethod
    def Clone(self: Windows.Devices.Display.Core.IDisplayState) -> Windows.Devices.Display.Core.DisplayState: ...
    IsReadOnly = property(get_IsReadOnly, None)
    IsStale = property(get_IsStale, None)
    Targets = property(get_Targets, None)
    Views = property(get_Views, None)
    Properties = property(get_Properties, None)
DisplayStateApplyOptions = UInt32
DisplayStateApplyOptions_None: DisplayStateApplyOptions = 0
DisplayStateApplyOptions_FailIfStateChanged: DisplayStateApplyOptions = 1
DisplayStateApplyOptions_ForceReapply: DisplayStateApplyOptions = 2
DisplayStateApplyOptions_ForceModeEnumeration: DisplayStateApplyOptions = 4
DisplayStateFunctionalizeOptions = UInt32
DisplayStateFunctionalizeOptions_None: DisplayStateFunctionalizeOptions = 0
DisplayStateFunctionalizeOptions_FailIfStateChanged: DisplayStateFunctionalizeOptions = 1
DisplayStateFunctionalizeOptions_ValidateTopologyOnly: DisplayStateFunctionalizeOptions = 2
class DisplayStateOperationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayStateOperationResult
    _classid_ = 'Windows.Devices.Display.Core.DisplayStateOperationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Display.Core.IDisplayStateOperationResult) -> Windows.Devices.Display.Core.DisplayStateOperationStatus: ...
    @winrt_mixinmethod
    def get_ExtendedErrorCode(self: Windows.Devices.Display.Core.IDisplayStateOperationResult) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedErrorCode = property(get_ExtendedErrorCode, None)
DisplayStateOperationStatus = Int32
DisplayStateOperationStatus_Success: DisplayStateOperationStatus = 0
DisplayStateOperationStatus_PartialFailure: DisplayStateOperationStatus = 1
DisplayStateOperationStatus_UnknownFailure: DisplayStateOperationStatus = 2
DisplayStateOperationStatus_TargetOwnershipLost: DisplayStateOperationStatus = 3
DisplayStateOperationStatus_SystemStateChanged: DisplayStateOperationStatus = 4
DisplayStateOperationStatus_TooManyPathsForAdapter: DisplayStateOperationStatus = 5
DisplayStateOperationStatus_ModesNotSupported: DisplayStateOperationStatus = 6
DisplayStateOperationStatus_RemoteSessionNotSupported: DisplayStateOperationStatus = 7
class DisplaySurface(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplaySurface
    _classid_ = 'Windows.Devices.Display.Core.DisplaySurface'
class DisplayTarget(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayTarget
    _classid_ = 'Windows.Devices.Display.Core.DisplayTarget'
    @winrt_mixinmethod
    def get_Adapter(self: Windows.Devices.Display.Core.IDisplayTarget) -> Windows.Devices.Display.Core.DisplayAdapter: ...
    @winrt_mixinmethod
    def get_DeviceInterfacePath(self: Windows.Devices.Display.Core.IDisplayTarget) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AdapterRelativeId(self: Windows.Devices.Display.Core.IDisplayTarget) -> UInt32: ...
    @winrt_mixinmethod
    def get_IsConnected(self: Windows.Devices.Display.Core.IDisplayTarget) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsVirtualModeEnabled(self: Windows.Devices.Display.Core.IDisplayTarget) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsVirtualTopologyEnabled(self: Windows.Devices.Display.Core.IDisplayTarget) -> Boolean: ...
    @winrt_mixinmethod
    def get_UsageKind(self: Windows.Devices.Display.Core.IDisplayTarget) -> Windows.Devices.Display.DisplayMonitorUsageKind: ...
    @winrt_mixinmethod
    def get_MonitorPersistence(self: Windows.Devices.Display.Core.IDisplayTarget) -> Windows.Devices.Display.Core.DisplayTargetPersistence: ...
    @winrt_mixinmethod
    def get_StableMonitorId(self: Windows.Devices.Display.Core.IDisplayTarget) -> WinRT_String: ...
    @winrt_mixinmethod
    def TryGetMonitor(self: Windows.Devices.Display.Core.IDisplayTarget) -> Windows.Devices.Display.DisplayMonitor: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Display.Core.IDisplayTarget) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_IsStale(self: Windows.Devices.Display.Core.IDisplayTarget) -> Boolean: ...
    @winrt_mixinmethod
    def IsSame(self: Windows.Devices.Display.Core.IDisplayTarget, otherTarget: Windows.Devices.Display.Core.DisplayTarget) -> Boolean: ...
    @winrt_mixinmethod
    def IsEqual(self: Windows.Devices.Display.Core.IDisplayTarget, otherTarget: Windows.Devices.Display.Core.DisplayTarget) -> Boolean: ...
    Adapter = property(get_Adapter, None)
    DeviceInterfacePath = property(get_DeviceInterfacePath, None)
    AdapterRelativeId = property(get_AdapterRelativeId, None)
    IsConnected = property(get_IsConnected, None)
    IsVirtualModeEnabled = property(get_IsVirtualModeEnabled, None)
    IsVirtualTopologyEnabled = property(get_IsVirtualTopologyEnabled, None)
    UsageKind = property(get_UsageKind, None)
    MonitorPersistence = property(get_MonitorPersistence, None)
    StableMonitorId = property(get_StableMonitorId, None)
    Properties = property(get_Properties, None)
    IsStale = property(get_IsStale, None)
DisplayTargetPersistence = Int32
DisplayTargetPersistence_None: DisplayTargetPersistence = 0
DisplayTargetPersistence_BootPersisted: DisplayTargetPersistence = 1
DisplayTargetPersistence_TemporaryPersisted: DisplayTargetPersistence = 2
DisplayTargetPersistence_PathPersisted: DisplayTargetPersistence = 3
class DisplayTask(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayTask
    _classid_ = 'Windows.Devices.Display.Core.DisplayTask'
    @winrt_mixinmethod
    def SetScanout(self: Windows.Devices.Display.Core.IDisplayTask, scanout: Windows.Devices.Display.Core.DisplayScanout) -> Void: ...
    @winrt_mixinmethod
    def SetWait(self: Windows.Devices.Display.Core.IDisplayTask, readyFence: Windows.Devices.Display.Core.DisplayFence, readyFenceValue: UInt64) -> Void: ...
    @winrt_mixinmethod
    def SetSignal(self: Windows.Devices.Display.Core.IDisplayTask2, signalKind: Windows.Devices.Display.Core.DisplayTaskSignalKind, fence: Windows.Devices.Display.Core.DisplayFence) -> Void: ...
class DisplayTaskPool(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayTaskPool
    _classid_ = 'Windows.Devices.Display.Core.DisplayTaskPool'
    @winrt_mixinmethod
    def CreateTask(self: Windows.Devices.Display.Core.IDisplayTaskPool) -> Windows.Devices.Display.Core.DisplayTask: ...
    @winrt_mixinmethod
    def ExecuteTask(self: Windows.Devices.Display.Core.IDisplayTaskPool, task: Windows.Devices.Display.Core.DisplayTask) -> Void: ...
    @winrt_mixinmethod
    def TryExecuteTask(self: Windows.Devices.Display.Core.IDisplayTaskPool2, task: Windows.Devices.Display.Core.DisplayTask) -> Windows.Devices.Display.Core.DisplayTaskResult: ...
class DisplayTaskResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayTaskResult
    _classid_ = 'Windows.Devices.Display.Core.DisplayTaskResult'
    @winrt_mixinmethod
    def get_PresentStatus(self: Windows.Devices.Display.Core.IDisplayTaskResult) -> Windows.Devices.Display.Core.DisplayPresentStatus: ...
    @winrt_mixinmethod
    def get_PresentId(self: Windows.Devices.Display.Core.IDisplayTaskResult) -> UInt64: ...
    @winrt_mixinmethod
    def get_SourceStatus(self: Windows.Devices.Display.Core.IDisplayTaskResult) -> Windows.Devices.Display.Core.DisplaySourceStatus: ...
    PresentStatus = property(get_PresentStatus, None)
    PresentId = property(get_PresentId, None)
    SourceStatus = property(get_SourceStatus, None)
DisplayTaskSignalKind = Int32
DisplayTaskSignalKind_OnPresentFlipAway: DisplayTaskSignalKind = 0
DisplayTaskSignalKind_OnPresentFlipTo: DisplayTaskSignalKind = 1
class DisplayView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayView
    _classid_ = 'Windows.Devices.Display.Core.DisplayView'
    @winrt_mixinmethod
    def get_Paths(self: Windows.Devices.Display.Core.IDisplayView) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Display.Core.DisplayPath]: ...
    @winrt_mixinmethod
    def get_ContentResolution(self: Windows.Devices.Display.Core.IDisplayView) -> Windows.Foundation.IReference[Windows.Graphics.SizeInt32]: ...
    @winrt_mixinmethod
    def put_ContentResolution(self: Windows.Devices.Display.Core.IDisplayView, value: Windows.Foundation.IReference[Windows.Graphics.SizeInt32]) -> Void: ...
    @winrt_mixinmethod
    def SetPrimaryPath(self: Windows.Devices.Display.Core.IDisplayView, path: Windows.Devices.Display.Core.DisplayPath) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Display.Core.IDisplayView) -> Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Paths = property(get_Paths, None)
    ContentResolution = property(get_ContentResolution, put_ContentResolution)
    Properties = property(get_Properties, None)
class DisplayWireFormat(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Display.Core.IDisplayWireFormat
    _classid_ = 'Windows.Devices.Display.Core.DisplayWireFormat'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Devices.Display.Core.IDisplayWireFormatFactory, pixelEncoding: Windows.Devices.Display.Core.DisplayWireFormatPixelEncoding, bitsPerChannel: Int32, colorSpace: Windows.Devices.Display.Core.DisplayWireFormatColorSpace, eotf: Windows.Devices.Display.Core.DisplayWireFormatEotf, hdrMetadata: Windows.Devices.Display.Core.DisplayWireFormatHdrMetadata) -> Windows.Devices.Display.Core.DisplayWireFormat: ...
    @winrt_mixinmethod
    def get_PixelEncoding(self: Windows.Devices.Display.Core.IDisplayWireFormat) -> Windows.Devices.Display.Core.DisplayWireFormatPixelEncoding: ...
    @winrt_mixinmethod
    def get_BitsPerChannel(self: Windows.Devices.Display.Core.IDisplayWireFormat) -> Int32: ...
    @winrt_mixinmethod
    def get_ColorSpace(self: Windows.Devices.Display.Core.IDisplayWireFormat) -> Windows.Devices.Display.Core.DisplayWireFormatColorSpace: ...
    @winrt_mixinmethod
    def get_Eotf(self: Windows.Devices.Display.Core.IDisplayWireFormat) -> Windows.Devices.Display.Core.DisplayWireFormatEotf: ...
    @winrt_mixinmethod
    def get_HdrMetadata(self: Windows.Devices.Display.Core.IDisplayWireFormat) -> Windows.Devices.Display.Core.DisplayWireFormatHdrMetadata: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Display.Core.IDisplayWireFormat) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_classmethod
    def CreateWithProperties(cls: Windows.Devices.Display.Core.IDisplayWireFormatStatics, extraProperties: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[Guid, Windows.Win32.System.WinRT.IInspectable_head]], pixelEncoding: Windows.Devices.Display.Core.DisplayWireFormatPixelEncoding, bitsPerChannel: Int32, colorSpace: Windows.Devices.Display.Core.DisplayWireFormatColorSpace, eotf: Windows.Devices.Display.Core.DisplayWireFormatEotf, hdrMetadata: Windows.Devices.Display.Core.DisplayWireFormatHdrMetadata) -> Windows.Devices.Display.Core.DisplayWireFormat: ...
    PixelEncoding = property(get_PixelEncoding, None)
    BitsPerChannel = property(get_BitsPerChannel, None)
    ColorSpace = property(get_ColorSpace, None)
    Eotf = property(get_Eotf, None)
    HdrMetadata = property(get_HdrMetadata, None)
    Properties = property(get_Properties, None)
DisplayWireFormatColorSpace = Int32
DisplayWireFormatColorSpace_BT709: DisplayWireFormatColorSpace = 0
DisplayWireFormatColorSpace_BT2020: DisplayWireFormatColorSpace = 1
DisplayWireFormatColorSpace_ProfileDefinedWideColorGamut: DisplayWireFormatColorSpace = 2
DisplayWireFormatEotf = Int32
DisplayWireFormatEotf_Sdr: DisplayWireFormatEotf = 0
DisplayWireFormatEotf_HdrSmpte2084: DisplayWireFormatEotf = 1
DisplayWireFormatHdrMetadata = Int32
DisplayWireFormatHdrMetadata_None: DisplayWireFormatHdrMetadata = 0
DisplayWireFormatHdrMetadata_Hdr10: DisplayWireFormatHdrMetadata = 1
DisplayWireFormatHdrMetadata_Hdr10Plus: DisplayWireFormatHdrMetadata = 2
DisplayWireFormatHdrMetadata_DolbyVisionLowLatency: DisplayWireFormatHdrMetadata = 3
DisplayWireFormatPixelEncoding = Int32
DisplayWireFormatPixelEncoding_Rgb444: DisplayWireFormatPixelEncoding = 0
DisplayWireFormatPixelEncoding_Ycc444: DisplayWireFormatPixelEncoding = 1
DisplayWireFormatPixelEncoding_Ycc422: DisplayWireFormatPixelEncoding = 2
DisplayWireFormatPixelEncoding_Ycc420: DisplayWireFormatPixelEncoding = 3
DisplayWireFormatPixelEncoding_Intensity: DisplayWireFormatPixelEncoding = 4
class IDisplayAdapter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayAdapter'
    _iid_ = Guid('{a56f5287-f000-5f2e-b5ac-3783a2b69af5}')
    @winrt_commethod(6)
    def get_Id(self) -> Windows.Graphics.DisplayAdapterId: ...
    @winrt_commethod(7)
    def get_DeviceInterfacePath(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SourceCount(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_PciVendorId(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_PciDeviceId(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_PciSubSystemId(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_PciRevision(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Id = property(get_Id, None)
    DeviceInterfacePath = property(get_DeviceInterfacePath, None)
    SourceCount = property(get_SourceCount, None)
    PciVendorId = property(get_PciVendorId, None)
    PciDeviceId = property(get_PciDeviceId, None)
    PciSubSystemId = property(get_PciSubSystemId, None)
    PciRevision = property(get_PciRevision, None)
    Properties = property(get_Properties, None)
class IDisplayAdapterStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayAdapterStatics'
    _iid_ = Guid('{1dac3cda-481f-5469-8470-82c4ba680a28}')
    @winrt_commethod(6)
    def FromId(self, id: Windows.Graphics.DisplayAdapterId) -> Windows.Devices.Display.Core.DisplayAdapter: ...
class IDisplayDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayDevice'
    _iid_ = Guid('{a4c9b62c-335f-5731-8cb4-c1ccd4731070}')
    @winrt_commethod(6)
    def CreateScanoutSource(self, target: Windows.Devices.Display.Core.DisplayTarget) -> Windows.Devices.Display.Core.DisplaySource: ...
    @winrt_commethod(7)
    def CreatePrimary(self, target: Windows.Devices.Display.Core.DisplayTarget, desc: Windows.Devices.Display.Core.DisplayPrimaryDescription) -> Windows.Devices.Display.Core.DisplaySurface: ...
    @winrt_commethod(8)
    def CreateTaskPool(self) -> Windows.Devices.Display.Core.DisplayTaskPool: ...
    @winrt_commethod(9)
    def CreatePeriodicFence(self, target: Windows.Devices.Display.Core.DisplayTarget, offsetFromVBlank: Windows.Foundation.TimeSpan) -> Windows.Devices.Display.Core.DisplayFence: ...
    @winrt_commethod(10)
    def WaitForVBlank(self, source: Windows.Devices.Display.Core.DisplaySource) -> Void: ...
    @winrt_commethod(11)
    def CreateSimpleScanout(self, pSource: Windows.Devices.Display.Core.DisplaySource, pSurface: Windows.Devices.Display.Core.DisplaySurface, SubResourceIndex: UInt32, SyncInterval: UInt32) -> Windows.Devices.Display.Core.DisplayScanout: ...
    @winrt_commethod(12)
    def IsCapabilitySupported(self, capability: Windows.Devices.Display.Core.DisplayDeviceCapability) -> Boolean: ...
class IDisplayDevice2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayDevice2'
    _iid_ = Guid('{3fefe50c-0940-54bd-a02f-f9c7a536ad60}')
    @winrt_commethod(6)
    def CreateSimpleScanoutWithDirtyRectsAndOptions(self, source: Windows.Devices.Display.Core.DisplaySource, surface: Windows.Devices.Display.Core.DisplaySurface, subresourceIndex: UInt32, syncInterval: UInt32, dirtyRects: Windows.Foundation.Collections.IIterable[Windows.Graphics.RectInt32], options: Windows.Devices.Display.Core.DisplayScanoutOptions) -> Windows.Devices.Display.Core.DisplayScanout: ...
class IDisplayFence(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayFence'
    _iid_ = Guid('{04dcf9ef-3406-5700-8fec-77eba4c5a74b}')
class IDisplayManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayManager'
    _iid_ = Guid('{4ed9245b-15ec-56e2-9072-7fe5084a31a7}')
    @winrt_commethod(6)
    def GetCurrentTargets(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Display.Core.DisplayTarget]: ...
    @winrt_commethod(7)
    def GetCurrentAdapters(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Display.Core.DisplayAdapter]: ...
    @winrt_commethod(8)
    def TryAcquireTarget(self, target: Windows.Devices.Display.Core.DisplayTarget) -> Windows.Devices.Display.Core.DisplayManagerResult: ...
    @winrt_commethod(9)
    def ReleaseTarget(self, target: Windows.Devices.Display.Core.DisplayTarget) -> Void: ...
    @winrt_commethod(10)
    def TryReadCurrentStateForAllTargets(self) -> Windows.Devices.Display.Core.DisplayManagerResultWithState: ...
    @winrt_commethod(11)
    def TryAcquireTargetsAndReadCurrentState(self, targets: Windows.Foundation.Collections.IIterable[Windows.Devices.Display.Core.DisplayTarget]) -> Windows.Devices.Display.Core.DisplayManagerResultWithState: ...
    @winrt_commethod(12)
    def TryAcquireTargetsAndCreateEmptyState(self, targets: Windows.Foundation.Collections.IIterable[Windows.Devices.Display.Core.DisplayTarget]) -> Windows.Devices.Display.Core.DisplayManagerResultWithState: ...
    @winrt_commethod(13)
    def TryAcquireTargetsAndCreateSubstate(self, existingState: Windows.Devices.Display.Core.DisplayState, targets: Windows.Foundation.Collections.IIterable[Windows.Devices.Display.Core.DisplayTarget]) -> Windows.Devices.Display.Core.DisplayManagerResultWithState: ...
    @winrt_commethod(14)
    def CreateDisplayDevice(self, adapter: Windows.Devices.Display.Core.DisplayAdapter) -> Windows.Devices.Display.Core.DisplayDevice: ...
    @winrt_commethod(15)
    def add_Enabled(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Display.Core.DisplayManager, Windows.Devices.Display.Core.DisplayManagerEnabledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_Enabled(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_Disabled(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Display.Core.DisplayManager, Windows.Devices.Display.Core.DisplayManagerDisabledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_Disabled(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_Changed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Display.Core.DisplayManager, Windows.Devices.Display.Core.DisplayManagerChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_Changed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_PathsFailedOrInvalidated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Display.Core.DisplayManager, Windows.Devices.Display.Core.DisplayManagerPathsFailedOrInvalidatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_PathsFailedOrInvalidated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def Start(self) -> Void: ...
    @winrt_commethod(24)
    def Stop(self) -> Void: ...
class IDisplayManagerChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayManagerChangedEventArgs'
    _iid_ = Guid('{6abfa285-6cca-5731-bcdc-42e5d2f5c50f}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
class IDisplayManagerDisabledEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayManagerDisabledEventArgs'
    _iid_ = Guid('{8726dde4-6793-5973-a11f-5ffbc93fdb90}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
class IDisplayManagerEnabledEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayManagerEnabledEventArgs'
    _iid_ = Guid('{f0cf3f6f-42fa-59a2-b297-26e1713de848}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
class IDisplayManagerPathsFailedOrInvalidatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayManagerPathsFailedOrInvalidatedEventArgs'
    _iid_ = Guid('{03a65659-1dec-5c15-b2a2-8fe9129869fe}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
class IDisplayManagerResultWithState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayManagerResultWithState'
    _iid_ = Guid('{8e656aa6-6614-54be-bfef-4994547f7be1}')
    @winrt_commethod(6)
    def get_ErrorCode(self) -> Windows.Devices.Display.Core.DisplayManagerResult: ...
    @winrt_commethod(7)
    def get_ExtendedErrorCode(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_State(self) -> Windows.Devices.Display.Core.DisplayState: ...
    ErrorCode = property(get_ErrorCode, None)
    ExtendedErrorCode = property(get_ExtendedErrorCode, None)
    State = property(get_State, None)
class IDisplayManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayManagerStatics'
    _iid_ = Guid('{2b6b9446-b999-5535-9d69-53f092c780a1}')
    @winrt_commethod(6)
    def Create(self, options: Windows.Devices.Display.Core.DisplayManagerOptions) -> Windows.Devices.Display.Core.DisplayManager: ...
class IDisplayModeInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayModeInfo'
    _iid_ = Guid('{48d513a0-f79b-5a74-a05e-da821f470868}')
    @winrt_commethod(6)
    def get_SourceResolution(self) -> Windows.Graphics.SizeInt32: ...
    @winrt_commethod(7)
    def get_IsStereo(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_SourcePixelFormat(self) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(9)
    def get_TargetResolution(self) -> Windows.Graphics.SizeInt32: ...
    @winrt_commethod(10)
    def get_PresentationRate(self) -> Windows.Devices.Display.Core.DisplayPresentationRate: ...
    @winrt_commethod(11)
    def get_IsInterlaced(self) -> Boolean: ...
    @winrt_commethod(12)
    def GetWireFormatSupportedBitsPerChannel(self, encoding: Windows.Devices.Display.Core.DisplayWireFormatPixelEncoding) -> Windows.Devices.Display.Core.DisplayBitsPerChannel: ...
    @winrt_commethod(13)
    def IsWireFormatSupported(self, wireFormat: Windows.Devices.Display.Core.DisplayWireFormat) -> Boolean: ...
    @winrt_commethod(14)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    SourceResolution = property(get_SourceResolution, None)
    IsStereo = property(get_IsStereo, None)
    SourcePixelFormat = property(get_SourcePixelFormat, None)
    TargetResolution = property(get_TargetResolution, None)
    PresentationRate = property(get_PresentationRate, None)
    IsInterlaced = property(get_IsInterlaced, None)
    Properties = property(get_Properties, None)
class IDisplayModeInfo2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayModeInfo2'
    _iid_ = Guid('{c86fa386-0ddb-5473-bfb0-4b7807b5f909}')
    @winrt_commethod(6)
    def get_PhysicalPresentationRate(self) -> Windows.Devices.Display.Core.DisplayPresentationRate: ...
    PhysicalPresentationRate = property(get_PhysicalPresentationRate, None)
class IDisplayPath(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayPath'
    _iid_ = Guid('{b3dfd64a-7460-5cde-811b-d5ae9f3d9f84}')
    @winrt_commethod(6)
    def get_View(self) -> Windows.Devices.Display.Core.DisplayView: ...
    @winrt_commethod(7)
    def get_Target(self) -> Windows.Devices.Display.Core.DisplayTarget: ...
    @winrt_commethod(8)
    def get_Status(self) -> Windows.Devices.Display.Core.DisplayPathStatus: ...
    @winrt_commethod(9)
    def get_SourceResolution(self) -> Windows.Foundation.IReference[Windows.Graphics.SizeInt32]: ...
    @winrt_commethod(10)
    def put_SourceResolution(self, value: Windows.Foundation.IReference[Windows.Graphics.SizeInt32]) -> Void: ...
    @winrt_commethod(11)
    def get_SourcePixelFormat(self) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(12)
    def put_SourcePixelFormat(self, value: Windows.Graphics.DirectX.DirectXPixelFormat) -> Void: ...
    @winrt_commethod(13)
    def get_IsStereo(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_IsStereo(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_TargetResolution(self) -> Windows.Foundation.IReference[Windows.Graphics.SizeInt32]: ...
    @winrt_commethod(16)
    def put_TargetResolution(self, value: Windows.Foundation.IReference[Windows.Graphics.SizeInt32]) -> Void: ...
    @winrt_commethod(17)
    def get_PresentationRate(self) -> Windows.Foundation.IReference[Windows.Devices.Display.Core.DisplayPresentationRate]: ...
    @winrt_commethod(18)
    def put_PresentationRate(self, value: Windows.Foundation.IReference[Windows.Devices.Display.Core.DisplayPresentationRate]) -> Void: ...
    @winrt_commethod(19)
    def get_IsInterlaced(self) -> Windows.Foundation.IReference[Boolean]: ...
    @winrt_commethod(20)
    def put_IsInterlaced(self, value: Windows.Foundation.IReference[Boolean]) -> Void: ...
    @winrt_commethod(21)
    def get_WireFormat(self) -> Windows.Devices.Display.Core.DisplayWireFormat: ...
    @winrt_commethod(22)
    def put_WireFormat(self, value: Windows.Devices.Display.Core.DisplayWireFormat) -> Void: ...
    @winrt_commethod(23)
    def get_Rotation(self) -> Windows.Devices.Display.Core.DisplayRotation: ...
    @winrt_commethod(24)
    def put_Rotation(self, value: Windows.Devices.Display.Core.DisplayRotation) -> Void: ...
    @winrt_commethod(25)
    def get_Scaling(self) -> Windows.Devices.Display.Core.DisplayPathScaling: ...
    @winrt_commethod(26)
    def put_Scaling(self, value: Windows.Devices.Display.Core.DisplayPathScaling) -> Void: ...
    @winrt_commethod(27)
    def FindModes(self, flags: Windows.Devices.Display.Core.DisplayModeQueryOptions) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Display.Core.DisplayModeInfo]: ...
    @winrt_commethod(28)
    def ApplyPropertiesFromMode(self, modeResult: Windows.Devices.Display.Core.DisplayModeInfo) -> Void: ...
    @winrt_commethod(29)
    def get_Properties(self) -> Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    View = property(get_View, None)
    Target = property(get_Target, None)
    Status = property(get_Status, None)
    SourceResolution = property(get_SourceResolution, put_SourceResolution)
    SourcePixelFormat = property(get_SourcePixelFormat, put_SourcePixelFormat)
    IsStereo = property(get_IsStereo, put_IsStereo)
    TargetResolution = property(get_TargetResolution, put_TargetResolution)
    PresentationRate = property(get_PresentationRate, put_PresentationRate)
    IsInterlaced = property(get_IsInterlaced, put_IsInterlaced)
    WireFormat = property(get_WireFormat, put_WireFormat)
    Rotation = property(get_Rotation, put_Rotation)
    Scaling = property(get_Scaling, put_Scaling)
    Properties = property(get_Properties, None)
class IDisplayPath2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayPath2'
    _iid_ = Guid('{f32459c5-e994-570b-9ec8-ef42c35a8547}')
    @winrt_commethod(6)
    def get_PhysicalPresentationRate(self) -> Windows.Foundation.IReference[Windows.Devices.Display.Core.DisplayPresentationRate]: ...
    @winrt_commethod(7)
    def put_PhysicalPresentationRate(self, value: Windows.Foundation.IReference[Windows.Devices.Display.Core.DisplayPresentationRate]) -> Void: ...
    PhysicalPresentationRate = property(get_PhysicalPresentationRate, put_PhysicalPresentationRate)
class IDisplayPrimaryDescription(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayPrimaryDescription'
    _iid_ = Guid('{872591d2-d533-50ff-a85e-06696194b77c}')
    @winrt_commethod(6)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Format(self) -> Windows.Graphics.DirectX.DirectXPixelFormat: ...
    @winrt_commethod(9)
    def get_ColorSpace(self) -> Windows.Graphics.DirectX.DirectXColorSpace: ...
    @winrt_commethod(10)
    def get_IsStereo(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_MultisampleDescription(self) -> Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription: ...
    @winrt_commethod(12)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Format = property(get_Format, None)
    ColorSpace = property(get_ColorSpace, None)
    IsStereo = property(get_IsStereo, None)
    MultisampleDescription = property(get_MultisampleDescription, None)
    Properties = property(get_Properties, None)
class IDisplayPrimaryDescriptionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayPrimaryDescriptionFactory'
    _iid_ = Guid('{1a6aff7b-3637-5c46-b479-76d576216e65}')
    @winrt_commethod(6)
    def CreateInstance(self, width: UInt32, height: UInt32, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, colorSpace: Windows.Graphics.DirectX.DirectXColorSpace, isStereo: Boolean, multisampleDescription: Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription) -> Windows.Devices.Display.Core.DisplayPrimaryDescription: ...
class IDisplayPrimaryDescriptionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayPrimaryDescriptionStatics'
    _iid_ = Guid('{e60e4cfb-36c9-56dd-8fa1-6ff8c4e0ff07}')
    @winrt_commethod(6)
    def CreateWithProperties(self, extraProperties: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[Guid, Windows.Win32.System.WinRT.IInspectable_head]], width: UInt32, height: UInt32, pixelFormat: Windows.Graphics.DirectX.DirectXPixelFormat, colorSpace: Windows.Graphics.DirectX.DirectXColorSpace, isStereo: Boolean, multisampleDescription: Windows.Graphics.DirectX.Direct3D11.Direct3DMultisampleDescription) -> Windows.Devices.Display.Core.DisplayPrimaryDescription: ...
class IDisplayScanout(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayScanout'
    _iid_ = Guid('{e3051828-1ba5-50e7-8a39-bb1fd2f4f8b9}')
class IDisplaySource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplaySource'
    _iid_ = Guid('{ecd15fc1-eadc-51bc-971d-3bc628db2dd4}')
    @winrt_commethod(6)
    def get_AdapterId(self) -> Windows.Graphics.DisplayAdapterId: ...
    @winrt_commethod(7)
    def get_SourceId(self) -> UInt32: ...
    @winrt_commethod(8)
    def GetMetadata(self, Key: Guid) -> Windows.Storage.Streams.IBuffer: ...
    AdapterId = property(get_AdapterId, None)
    SourceId = property(get_SourceId, None)
class IDisplaySource2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplaySource2'
    _iid_ = Guid('{71e18952-b321-5af4-bfe8-03fbea31e40d}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Display.Core.DisplaySourceStatus: ...
    @winrt_commethod(7)
    def add_StatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Display.Core.DisplaySource, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_StatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
class IDisplayState(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayState'
    _iid_ = Guid('{08129321-11b5-5cb2-99f8-e90b479a8a1d}')
    @winrt_commethod(6)
    def get_IsReadOnly(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsStale(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Targets(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Display.Core.DisplayTarget]: ...
    @winrt_commethod(9)
    def get_Views(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Display.Core.DisplayView]: ...
    @winrt_commethod(10)
    def get_Properties(self) -> Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(11)
    def ConnectTarget(self, target: Windows.Devices.Display.Core.DisplayTarget) -> Windows.Devices.Display.Core.DisplayPath: ...
    @winrt_commethod(12)
    def ConnectTargetToView(self, target: Windows.Devices.Display.Core.DisplayTarget, view: Windows.Devices.Display.Core.DisplayView) -> Windows.Devices.Display.Core.DisplayPath: ...
    @winrt_commethod(13)
    def CanConnectTargetToView(self, target: Windows.Devices.Display.Core.DisplayTarget, view: Windows.Devices.Display.Core.DisplayView) -> Boolean: ...
    @winrt_commethod(14)
    def GetViewForTarget(self, target: Windows.Devices.Display.Core.DisplayTarget) -> Windows.Devices.Display.Core.DisplayView: ...
    @winrt_commethod(15)
    def GetPathForTarget(self, target: Windows.Devices.Display.Core.DisplayTarget) -> Windows.Devices.Display.Core.DisplayPath: ...
    @winrt_commethod(16)
    def DisconnectTarget(self, target: Windows.Devices.Display.Core.DisplayTarget) -> Void: ...
    @winrt_commethod(17)
    def TryFunctionalize(self, options: Windows.Devices.Display.Core.DisplayStateFunctionalizeOptions) -> Windows.Devices.Display.Core.DisplayStateOperationResult: ...
    @winrt_commethod(18)
    def TryApply(self, options: Windows.Devices.Display.Core.DisplayStateApplyOptions) -> Windows.Devices.Display.Core.DisplayStateOperationResult: ...
    @winrt_commethod(19)
    def Clone(self) -> Windows.Devices.Display.Core.DisplayState: ...
    IsReadOnly = property(get_IsReadOnly, None)
    IsStale = property(get_IsStale, None)
    Targets = property(get_Targets, None)
    Views = property(get_Views, None)
    Properties = property(get_Properties, None)
class IDisplayStateOperationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayStateOperationResult'
    _iid_ = Guid('{fcadbfdf-dc27-5638-b7f2-ebdfa4f7ea93}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Display.Core.DisplayStateOperationStatus: ...
    @winrt_commethod(7)
    def get_ExtendedErrorCode(self) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedErrorCode = property(get_ExtendedErrorCode, None)
class IDisplaySurface(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplaySurface'
    _iid_ = Guid('{594f6cc6-139a-56d6-a4b1-15fe2cb76adb}')
class IDisplayTarget(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayTarget'
    _iid_ = Guid('{aec57c6f-47b4-546b-987c-e73fa791fe3a}')
    @winrt_commethod(6)
    def get_Adapter(self) -> Windows.Devices.Display.Core.DisplayAdapter: ...
    @winrt_commethod(7)
    def get_DeviceInterfacePath(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AdapterRelativeId(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_IsConnected(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsVirtualModeEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsVirtualTopologyEnabled(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_UsageKind(self) -> Windows.Devices.Display.DisplayMonitorUsageKind: ...
    @winrt_commethod(13)
    def get_MonitorPersistence(self) -> Windows.Devices.Display.Core.DisplayTargetPersistence: ...
    @winrt_commethod(14)
    def get_StableMonitorId(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def TryGetMonitor(self) -> Windows.Devices.Display.DisplayMonitor: ...
    @winrt_commethod(16)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_commethod(17)
    def get_IsStale(self) -> Boolean: ...
    @winrt_commethod(18)
    def IsSame(self, otherTarget: Windows.Devices.Display.Core.DisplayTarget) -> Boolean: ...
    @winrt_commethod(19)
    def IsEqual(self, otherTarget: Windows.Devices.Display.Core.DisplayTarget) -> Boolean: ...
    Adapter = property(get_Adapter, None)
    DeviceInterfacePath = property(get_DeviceInterfacePath, None)
    AdapterRelativeId = property(get_AdapterRelativeId, None)
    IsConnected = property(get_IsConnected, None)
    IsVirtualModeEnabled = property(get_IsVirtualModeEnabled, None)
    IsVirtualTopologyEnabled = property(get_IsVirtualTopologyEnabled, None)
    UsageKind = property(get_UsageKind, None)
    MonitorPersistence = property(get_MonitorPersistence, None)
    StableMonitorId = property(get_StableMonitorId, None)
    Properties = property(get_Properties, None)
    IsStale = property(get_IsStale, None)
class IDisplayTask(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayTask'
    _iid_ = Guid('{5e087448-135b-5bb0-bf63-637f84227c7a}')
    @winrt_commethod(6)
    def SetScanout(self, scanout: Windows.Devices.Display.Core.DisplayScanout) -> Void: ...
    @winrt_commethod(7)
    def SetWait(self, readyFence: Windows.Devices.Display.Core.DisplayFence, readyFenceValue: UInt64) -> Void: ...
class IDisplayTask2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayTask2'
    _iid_ = Guid('{0957ea19-bd55-55de-9267-c97b61e71c37}')
    @winrt_commethod(6)
    def SetSignal(self, signalKind: Windows.Devices.Display.Core.DisplayTaskSignalKind, fence: Windows.Devices.Display.Core.DisplayFence) -> Void: ...
class IDisplayTaskPool(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayTaskPool'
    _iid_ = Guid('{c676253d-237d-5548-aafa-3e517fefef1c}')
    @winrt_commethod(6)
    def CreateTask(self) -> Windows.Devices.Display.Core.DisplayTask: ...
    @winrt_commethod(7)
    def ExecuteTask(self, task: Windows.Devices.Display.Core.DisplayTask) -> Void: ...
class IDisplayTaskPool2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayTaskPool2'
    _iid_ = Guid('{46b879b6-5d17-5955-a872-eb38003db586}')
    @winrt_commethod(6)
    def TryExecuteTask(self, task: Windows.Devices.Display.Core.DisplayTask) -> Windows.Devices.Display.Core.DisplayTaskResult: ...
class IDisplayTaskResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayTaskResult'
    _iid_ = Guid('{6fbc7d67-f9b1-55e0-9d88-d3a5197a3f59}')
    @winrt_commethod(6)
    def get_PresentStatus(self) -> Windows.Devices.Display.Core.DisplayPresentStatus: ...
    @winrt_commethod(7)
    def get_PresentId(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_SourceStatus(self) -> Windows.Devices.Display.Core.DisplaySourceStatus: ...
    PresentStatus = property(get_PresentStatus, None)
    PresentId = property(get_PresentId, None)
    SourceStatus = property(get_SourceStatus, None)
class IDisplayView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayView'
    _iid_ = Guid('{b0c98ca1-b759-5b59-b1ad-f0786aa9e53d}')
    @winrt_commethod(6)
    def get_Paths(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Display.Core.DisplayPath]: ...
    @winrt_commethod(7)
    def get_ContentResolution(self) -> Windows.Foundation.IReference[Windows.Graphics.SizeInt32]: ...
    @winrt_commethod(8)
    def put_ContentResolution(self, value: Windows.Foundation.IReference[Windows.Graphics.SizeInt32]) -> Void: ...
    @winrt_commethod(9)
    def SetPrimaryPath(self, path: Windows.Devices.Display.Core.DisplayPath) -> Void: ...
    @winrt_commethod(10)
    def get_Properties(self) -> Windows.Foundation.Collections.IMap[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Paths = property(get_Paths, None)
    ContentResolution = property(get_ContentResolution, put_ContentResolution)
    Properties = property(get_Properties, None)
class IDisplayWireFormat(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayWireFormat'
    _iid_ = Guid('{1acc967d-872c-5a38-bbb9-1d4872b76255}')
    @winrt_commethod(6)
    def get_PixelEncoding(self) -> Windows.Devices.Display.Core.DisplayWireFormatPixelEncoding: ...
    @winrt_commethod(7)
    def get_BitsPerChannel(self) -> Int32: ...
    @winrt_commethod(8)
    def get_ColorSpace(self) -> Windows.Devices.Display.Core.DisplayWireFormatColorSpace: ...
    @winrt_commethod(9)
    def get_Eotf(self) -> Windows.Devices.Display.Core.DisplayWireFormatEotf: ...
    @winrt_commethod(10)
    def get_HdrMetadata(self) -> Windows.Devices.Display.Core.DisplayWireFormatHdrMetadata: ...
    @winrt_commethod(11)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[Guid, Windows.Win32.System.WinRT.IInspectable_head]: ...
    PixelEncoding = property(get_PixelEncoding, None)
    BitsPerChannel = property(get_BitsPerChannel, None)
    ColorSpace = property(get_ColorSpace, None)
    Eotf = property(get_Eotf, None)
    HdrMetadata = property(get_HdrMetadata, None)
    Properties = property(get_Properties, None)
class IDisplayWireFormatFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayWireFormatFactory'
    _iid_ = Guid('{b2efc8d5-09d6-55e6-ad22-9014b3d25229}')
    @winrt_commethod(6)
    def CreateInstance(self, pixelEncoding: Windows.Devices.Display.Core.DisplayWireFormatPixelEncoding, bitsPerChannel: Int32, colorSpace: Windows.Devices.Display.Core.DisplayWireFormatColorSpace, eotf: Windows.Devices.Display.Core.DisplayWireFormatEotf, hdrMetadata: Windows.Devices.Display.Core.DisplayWireFormatHdrMetadata) -> Windows.Devices.Display.Core.DisplayWireFormat: ...
class IDisplayWireFormatStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Display.Core.IDisplayWireFormatStatics'
    _iid_ = Guid('{c575a22d-c3e6-5f7a-bdfb-87c6ab8661d5}')
    @winrt_commethod(6)
    def CreateWithProperties(self, extraProperties: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[Guid, Windows.Win32.System.WinRT.IInspectable_head]], pixelEncoding: Windows.Devices.Display.Core.DisplayWireFormatPixelEncoding, bitsPerChannel: Int32, colorSpace: Windows.Devices.Display.Core.DisplayWireFormatColorSpace, eotf: Windows.Devices.Display.Core.DisplayWireFormatEotf, hdrMetadata: Windows.Devices.Display.Core.DisplayWireFormatHdrMetadata) -> Windows.Devices.Display.Core.DisplayWireFormat: ...
make_head(_module, 'DisplayAdapter')
make_head(_module, 'DisplayDevice')
make_head(_module, 'DisplayFence')
make_head(_module, 'DisplayManager')
make_head(_module, 'DisplayManagerChangedEventArgs')
make_head(_module, 'DisplayManagerDisabledEventArgs')
make_head(_module, 'DisplayManagerEnabledEventArgs')
make_head(_module, 'DisplayManagerPathsFailedOrInvalidatedEventArgs')
make_head(_module, 'DisplayManagerResultWithState')
make_head(_module, 'DisplayModeInfo')
make_head(_module, 'DisplayPath')
make_head(_module, 'DisplayPresentationRate')
make_head(_module, 'DisplayPrimaryDescription')
make_head(_module, 'DisplayScanout')
make_head(_module, 'DisplaySource')
make_head(_module, 'DisplayState')
make_head(_module, 'DisplayStateOperationResult')
make_head(_module, 'DisplaySurface')
make_head(_module, 'DisplayTarget')
make_head(_module, 'DisplayTask')
make_head(_module, 'DisplayTaskPool')
make_head(_module, 'DisplayTaskResult')
make_head(_module, 'DisplayView')
make_head(_module, 'DisplayWireFormat')
make_head(_module, 'IDisplayAdapter')
make_head(_module, 'IDisplayAdapterStatics')
make_head(_module, 'IDisplayDevice')
make_head(_module, 'IDisplayDevice2')
make_head(_module, 'IDisplayFence')
make_head(_module, 'IDisplayManager')
make_head(_module, 'IDisplayManagerChangedEventArgs')
make_head(_module, 'IDisplayManagerDisabledEventArgs')
make_head(_module, 'IDisplayManagerEnabledEventArgs')
make_head(_module, 'IDisplayManagerPathsFailedOrInvalidatedEventArgs')
make_head(_module, 'IDisplayManagerResultWithState')
make_head(_module, 'IDisplayManagerStatics')
make_head(_module, 'IDisplayModeInfo')
make_head(_module, 'IDisplayModeInfo2')
make_head(_module, 'IDisplayPath')
make_head(_module, 'IDisplayPath2')
make_head(_module, 'IDisplayPrimaryDescription')
make_head(_module, 'IDisplayPrimaryDescriptionFactory')
make_head(_module, 'IDisplayPrimaryDescriptionStatics')
make_head(_module, 'IDisplayScanout')
make_head(_module, 'IDisplaySource')
make_head(_module, 'IDisplaySource2')
make_head(_module, 'IDisplayState')
make_head(_module, 'IDisplayStateOperationResult')
make_head(_module, 'IDisplaySurface')
make_head(_module, 'IDisplayTarget')
make_head(_module, 'IDisplayTask')
make_head(_module, 'IDisplayTask2')
make_head(_module, 'IDisplayTaskPool')
make_head(_module, 'IDisplayTaskPool2')
make_head(_module, 'IDisplayTaskResult')
make_head(_module, 'IDisplayView')
make_head(_module, 'IDisplayWireFormat')
make_head(_module, 'IDisplayWireFormatFactory')
make_head(_module, 'IDisplayWireFormatStatics')
