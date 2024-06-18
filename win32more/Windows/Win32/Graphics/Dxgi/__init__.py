from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Dxgi
import win32more.Windows.Win32.Graphics.Dxgi.Common
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Com
DXGI_MAX_SWAP_CHAIN_BUFFERS: UInt32 = 16
DXGI_DEBUG_BINARY_VERSION: UInt32 = 1
DXGI_DEBUG_ALL: Guid = Guid('{e48ae283-da80-490b-87e6-43e9a9cfda08}')
DXGI_DEBUG_DX: Guid = Guid('{35cdd7fc-13b2-421d-a5d7-7e4451287d64}')
DXGI_DEBUG_DXGI: Guid = Guid('{25cddaa4-b1c6-47e1-ac3e-98875b5a2e2a}')
DXGI_DEBUG_APP: Guid = Guid('{06cd6e01-4219-4ebd-8709-27ed23360c62}')
DXGI_INFO_QUEUE_MESSAGE_ID_STRING_FROM_APPLICATION: UInt32 = 0
DXGI_INFO_QUEUE_DEFAULT_MESSAGE_COUNT_LIMIT: UInt32 = 1024
DXGI_ERROR_INVALID_CALL: win32more.Windows.Win32.Foundation.HRESULT = -2005270527
DXGI_ERROR_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2005270526
DXGI_ERROR_MORE_DATA: win32more.Windows.Win32.Foundation.HRESULT = -2005270525
DXGI_ERROR_UNSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2005270524
DXGI_ERROR_DEVICE_REMOVED: win32more.Windows.Win32.Foundation.HRESULT = -2005270523
DXGI_ERROR_DEVICE_HUNG: win32more.Windows.Win32.Foundation.HRESULT = -2005270522
DXGI_ERROR_DEVICE_RESET: win32more.Windows.Win32.Foundation.HRESULT = -2005270521
DXGI_ERROR_WAS_STILL_DRAWING: win32more.Windows.Win32.Foundation.HRESULT = -2005270518
DXGI_ERROR_FRAME_STATISTICS_DISJOINT: win32more.Windows.Win32.Foundation.HRESULT = -2005270517
DXGI_ERROR_GRAPHICS_VIDPN_SOURCE_IN_USE: win32more.Windows.Win32.Foundation.HRESULT = -2005270516
DXGI_ERROR_DRIVER_INTERNAL_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2005270496
DXGI_ERROR_NONEXCLUSIVE: win32more.Windows.Win32.Foundation.HRESULT = -2005270495
DXGI_ERROR_NOT_CURRENTLY_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2005270494
DXGI_ERROR_REMOTE_CLIENT_DISCONNECTED: win32more.Windows.Win32.Foundation.HRESULT = -2005270493
DXGI_ERROR_REMOTE_OUTOFMEMORY: win32more.Windows.Win32.Foundation.HRESULT = -2005270492
DXGI_ERROR_ACCESS_LOST: win32more.Windows.Win32.Foundation.HRESULT = -2005270490
DXGI_ERROR_WAIT_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2005270489
DXGI_ERROR_SESSION_DISCONNECTED: win32more.Windows.Win32.Foundation.HRESULT = -2005270488
DXGI_ERROR_RESTRICT_TO_OUTPUT_STALE: win32more.Windows.Win32.Foundation.HRESULT = -2005270487
DXGI_ERROR_CANNOT_PROTECT_CONTENT: win32more.Windows.Win32.Foundation.HRESULT = -2005270486
DXGI_ERROR_ACCESS_DENIED: win32more.Windows.Win32.Foundation.HRESULT = -2005270485
DXGI_ERROR_NAME_ALREADY_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2005270484
DXGI_ERROR_SDK_COMPONENT_MISSING: win32more.Windows.Win32.Foundation.HRESULT = -2005270483
DXGI_ERROR_NOT_CURRENT: win32more.Windows.Win32.Foundation.HRESULT = -2005270482
DXGI_ERROR_HW_PROTECTION_OUTOFMEMORY: win32more.Windows.Win32.Foundation.HRESULT = -2005270480
DXGI_ERROR_DYNAMIC_CODE_POLICY_VIOLATION: win32more.Windows.Win32.Foundation.HRESULT = -2005270479
DXGI_ERROR_NON_COMPOSITED_UI: win32more.Windows.Win32.Foundation.HRESULT = -2005270478
DXGI_ERROR_MODE_CHANGE_IN_PROGRESS: win32more.Windows.Win32.Foundation.HRESULT = -2005270491
DXGI_ERROR_CACHE_CORRUPT: win32more.Windows.Win32.Foundation.HRESULT = -2005270477
DXGI_ERROR_CACHE_FULL: win32more.Windows.Win32.Foundation.HRESULT = -2005270476
DXGI_ERROR_CACHE_HASH_COLLISION: win32more.Windows.Win32.Foundation.HRESULT = -2005270475
DXGI_ERROR_ALREADY_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2005270474
DXGI_ERROR_MPO_UNPINNED: win32more.Windows.Win32.Foundation.HRESULT = -2005270428
@winfunctype('dxgi.dll')
def CreateDXGIFactory(riid: POINTER(Guid), ppFactory: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dxgi.dll')
def CreateDXGIFactory1(riid: POINTER(Guid), ppFactory: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dxgi.dll')
def CreateDXGIFactory2(Flags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_CREATE_FACTORY_FLAGS, riid: POINTER(Guid), ppFactory: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dxgi.dll')
def DXGIGetDebugInterface1(Flags: UInt32, riid: POINTER(Guid), pDebug: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dxgi.dll')
def DXGIDeclareAdapterRemovalSupport() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dxgi.dll')
def DXGIDisableVBlankVirtualization() -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DXGI_ADAPTER_DESC(Structure):
    Description: Char * 128
    VendorId: UInt32
    DeviceId: UInt32
    SubSysId: UInt32
    Revision: UInt32
    DedicatedVideoMemory: UIntPtr
    DedicatedSystemMemory: UIntPtr
    SharedSystemMemory: UIntPtr
    AdapterLuid: win32more.Windows.Win32.Foundation.LUID
class DXGI_ADAPTER_DESC1(Structure):
    Description: Char * 128
    VendorId: UInt32
    DeviceId: UInt32
    SubSysId: UInt32
    Revision: UInt32
    DedicatedVideoMemory: UIntPtr
    DedicatedSystemMemory: UIntPtr
    SharedSystemMemory: UIntPtr
    AdapterLuid: win32more.Windows.Win32.Foundation.LUID
    Flags: UInt32
class DXGI_ADAPTER_DESC2(Structure):
    Description: Char * 128
    VendorId: UInt32
    DeviceId: UInt32
    SubSysId: UInt32
    Revision: UInt32
    DedicatedVideoMemory: UIntPtr
    DedicatedSystemMemory: UIntPtr
    SharedSystemMemory: UIntPtr
    AdapterLuid: win32more.Windows.Win32.Foundation.LUID
    Flags: UInt32
    GraphicsPreemptionGranularity: win32more.Windows.Win32.Graphics.Dxgi.DXGI_GRAPHICS_PREEMPTION_GRANULARITY
    ComputePreemptionGranularity: win32more.Windows.Win32.Graphics.Dxgi.DXGI_COMPUTE_PREEMPTION_GRANULARITY
class DXGI_ADAPTER_DESC3(Structure):
    Description: Char * 128
    VendorId: UInt32
    DeviceId: UInt32
    SubSysId: UInt32
    Revision: UInt32
    DedicatedVideoMemory: UIntPtr
    DedicatedSystemMemory: UIntPtr
    SharedSystemMemory: UIntPtr
    AdapterLuid: win32more.Windows.Win32.Foundation.LUID
    Flags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_FLAG3
    GraphicsPreemptionGranularity: win32more.Windows.Win32.Graphics.Dxgi.DXGI_GRAPHICS_PREEMPTION_GRANULARITY
    ComputePreemptionGranularity: win32more.Windows.Win32.Graphics.Dxgi.DXGI_COMPUTE_PREEMPTION_GRANULARITY
DXGI_ADAPTER_FLAG = Int32
DXGI_ADAPTER_FLAG_NONE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_FLAG = 0
DXGI_ADAPTER_FLAG_REMOTE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_FLAG = 1
DXGI_ADAPTER_FLAG_SOFTWARE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_FLAG = 2
DXGI_ADAPTER_FLAG3 = Int32
DXGI_ADAPTER_FLAG3_NONE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_FLAG3 = 0
DXGI_ADAPTER_FLAG3_REMOTE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_FLAG3 = 1
DXGI_ADAPTER_FLAG3_SOFTWARE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_FLAG3 = 2
DXGI_ADAPTER_FLAG3_ACG_COMPATIBLE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_FLAG3 = 4
DXGI_ADAPTER_FLAG3_SUPPORT_MONITORED_FENCES: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_FLAG3 = 8
DXGI_ADAPTER_FLAG3_SUPPORT_NON_MONITORED_FENCES: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_FLAG3 = 16
DXGI_ADAPTER_FLAG3_KEYED_MUTEX_CONFORMANCE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_FLAG3 = 32
DXGI_COMPUTE_PREEMPTION_GRANULARITY = Int32
DXGI_COMPUTE_PREEMPTION_DMA_BUFFER_BOUNDARY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_COMPUTE_PREEMPTION_GRANULARITY = 0
DXGI_COMPUTE_PREEMPTION_DISPATCH_BOUNDARY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_COMPUTE_PREEMPTION_GRANULARITY = 1
DXGI_COMPUTE_PREEMPTION_THREAD_GROUP_BOUNDARY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_COMPUTE_PREEMPTION_GRANULARITY = 2
DXGI_COMPUTE_PREEMPTION_THREAD_BOUNDARY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_COMPUTE_PREEMPTION_GRANULARITY = 3
DXGI_COMPUTE_PREEMPTION_INSTRUCTION_BOUNDARY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_COMPUTE_PREEMPTION_GRANULARITY = 4
DXGI_CREATE_FACTORY_FLAGS = UInt32
DXGI_CREATE_FACTORY_DEBUG: win32more.Windows.Win32.Graphics.Dxgi.DXGI_CREATE_FACTORY_FLAGS = 1
DXGI_DEBUG_RLO_FLAGS = Int32
DXGI_DEBUG_RLO_SUMMARY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_DEBUG_RLO_FLAGS = 1
DXGI_DEBUG_RLO_DETAIL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_DEBUG_RLO_FLAGS = 2
DXGI_DEBUG_RLO_IGNORE_INTERNAL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_DEBUG_RLO_FLAGS = 4
DXGI_DEBUG_RLO_ALL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_DEBUG_RLO_FLAGS = 7
class DXGI_DECODE_SWAP_CHAIN_DESC(Structure):
    Flags: UInt32
class DXGI_DISPLAY_COLOR_SPACE(Structure):
    PrimaryCoordinates: Single * 16
    WhitePoints: Single * 32
DXGI_ENUM_MODES = UInt32
DXGI_ENUM_MODES_INTERLACED: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ENUM_MODES = 1
DXGI_ENUM_MODES_SCALING: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ENUM_MODES = 2
DXGI_ENUM_MODES_STEREO: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ENUM_MODES = 4
DXGI_ENUM_MODES_DISABLED_STEREO: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ENUM_MODES = 8
DXGI_FEATURE = Int32
DXGI_FEATURE_PRESENT_ALLOW_TEARING: win32more.Windows.Win32.Graphics.Dxgi.DXGI_FEATURE = 0
DXGI_FRAME_PRESENTATION_MODE = Int32
DXGI_FRAME_PRESENTATION_MODE_COMPOSED: win32more.Windows.Win32.Graphics.Dxgi.DXGI_FRAME_PRESENTATION_MODE = 0
DXGI_FRAME_PRESENTATION_MODE_OVERLAY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_FRAME_PRESENTATION_MODE = 1
DXGI_FRAME_PRESENTATION_MODE_NONE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_FRAME_PRESENTATION_MODE = 2
DXGI_FRAME_PRESENTATION_MODE_COMPOSITION_FAILURE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_FRAME_PRESENTATION_MODE = 3
class DXGI_FRAME_STATISTICS(Structure):
    PresentCount: UInt32
    PresentRefreshCount: UInt32
    SyncRefreshCount: UInt32
    SyncQPCTime: Int64
    SyncGPUTime: Int64
class DXGI_FRAME_STATISTICS_MEDIA(Structure):
    PresentCount: UInt32
    PresentRefreshCount: UInt32
    SyncRefreshCount: UInt32
    SyncQPCTime: Int64
    SyncGPUTime: Int64
    CompositionMode: win32more.Windows.Win32.Graphics.Dxgi.DXGI_FRAME_PRESENTATION_MODE
    ApprovedPresentDuration: UInt32
DXGI_GPU_PREFERENCE = Int32
DXGI_GPU_PREFERENCE_UNSPECIFIED: win32more.Windows.Win32.Graphics.Dxgi.DXGI_GPU_PREFERENCE = 0
DXGI_GPU_PREFERENCE_MINIMUM_POWER: win32more.Windows.Win32.Graphics.Dxgi.DXGI_GPU_PREFERENCE = 1
DXGI_GPU_PREFERENCE_HIGH_PERFORMANCE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_GPU_PREFERENCE = 2
DXGI_GRAPHICS_PREEMPTION_GRANULARITY = Int32
DXGI_GRAPHICS_PREEMPTION_DMA_BUFFER_BOUNDARY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_GRAPHICS_PREEMPTION_GRANULARITY = 0
DXGI_GRAPHICS_PREEMPTION_PRIMITIVE_BOUNDARY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_GRAPHICS_PREEMPTION_GRANULARITY = 1
DXGI_GRAPHICS_PREEMPTION_TRIANGLE_BOUNDARY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_GRAPHICS_PREEMPTION_GRANULARITY = 2
DXGI_GRAPHICS_PREEMPTION_PIXEL_BOUNDARY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_GRAPHICS_PREEMPTION_GRANULARITY = 3
DXGI_GRAPHICS_PREEMPTION_INSTRUCTION_BOUNDARY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_GRAPHICS_PREEMPTION_GRANULARITY = 4
DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAGS = Int32
DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAG_FULLSCREEN: win32more.Windows.Win32.Graphics.Dxgi.DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAGS = 1
DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAG_WINDOWED: win32more.Windows.Win32.Graphics.Dxgi.DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAGS = 2
DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAG_CURSOR_STRETCHED: win32more.Windows.Win32.Graphics.Dxgi.DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAGS = 4
class DXGI_HDR_METADATA_HDR10(Structure):
    RedPrimary: UInt16 * 2
    GreenPrimary: UInt16 * 2
    BluePrimary: UInt16 * 2
    WhitePoint: UInt16 * 2
    MaxMasteringLuminance: UInt32
    MinMasteringLuminance: UInt32
    MaxContentLightLevel: UInt16
    MaxFrameAverageLightLevel: UInt16
class DXGI_HDR_METADATA_HDR10PLUS(Structure):
    Data: Byte * 72
DXGI_HDR_METADATA_TYPE = Int32
DXGI_HDR_METADATA_TYPE_NONE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_HDR_METADATA_TYPE = 0
DXGI_HDR_METADATA_TYPE_HDR10: win32more.Windows.Win32.Graphics.Dxgi.DXGI_HDR_METADATA_TYPE = 1
DXGI_HDR_METADATA_TYPE_HDR10PLUS: win32more.Windows.Win32.Graphics.Dxgi.DXGI_HDR_METADATA_TYPE = 2
class DXGI_INFO_QUEUE_FILTER(Structure):
    AllowList: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER_DESC
    DenyList: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER_DESC
class DXGI_INFO_QUEUE_FILTER_DESC(Structure):
    NumCategories: UInt32
    pCategoryList: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY)
    NumSeverities: UInt32
    pSeverityList: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY)
    NumIDs: UInt32
    pIDList: POINTER(Int32)
class DXGI_INFO_QUEUE_MESSAGE(Structure):
    Producer: Guid
    Category: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY
    Severity: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY
    ID: Int32
    pDescription: POINTER(Byte)
    DescriptionByteLength: UIntPtr
DXGI_INFO_QUEUE_MESSAGE_CATEGORY = Int32
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_UNKNOWN: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY = 0
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_MISCELLANEOUS: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY = 1
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_INITIALIZATION: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY = 2
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_CLEANUP: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY = 3
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_COMPILATION: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY = 4
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_STATE_CREATION: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY = 5
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_STATE_SETTING: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY = 6
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_STATE_GETTING: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY = 7
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_RESOURCE_MANIPULATION: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY = 8
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_EXECUTION: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY = 9
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_SHADER: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY = 10
DXGI_INFO_QUEUE_MESSAGE_SEVERITY = Int32
DXGI_INFO_QUEUE_MESSAGE_SEVERITY_CORRUPTION: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY = 0
DXGI_INFO_QUEUE_MESSAGE_SEVERITY_ERROR: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY = 1
DXGI_INFO_QUEUE_MESSAGE_SEVERITY_WARNING: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY = 2
DXGI_INFO_QUEUE_MESSAGE_SEVERITY_INFO: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY = 3
DXGI_INFO_QUEUE_MESSAGE_SEVERITY_MESSAGE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY = 4
class DXGI_MAPPED_RECT(Structure):
    Pitch: Int32
    pBits: POINTER(Byte)
DXGI_MAP_FLAGS = UInt32
DXGI_MAP_READ: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MAP_FLAGS = 1
DXGI_MAP_WRITE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MAP_FLAGS = 2
DXGI_MAP_DISCARD: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MAP_FLAGS = 4
class DXGI_MATRIX_3X2_F(Structure):
    _11: Single
    _12: Single
    _21: Single
    _22: Single
    _31: Single
    _32: Single
DXGI_MEMORY_SEGMENT_GROUP = Int32
DXGI_MEMORY_SEGMENT_GROUP_LOCAL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MEMORY_SEGMENT_GROUP = 0
DXGI_MEMORY_SEGMENT_GROUP_NON_LOCAL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MEMORY_SEGMENT_GROUP = 1
class DXGI_MODE_DESC1(Structure):
    Width: UInt32
    Height: UInt32
    RefreshRate: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    Format: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    ScanlineOrdering: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_SCANLINE_ORDER
    Scaling: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_SCALING
    Stereo: win32more.Windows.Win32.Foundation.BOOL
DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS = Int32
DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS = 1
DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS = 2
DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS = 4
DXGI_MWA_FLAGS = UInt32
DXGI_MWA_NO_WINDOW_CHANGES: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MWA_FLAGS = 1
DXGI_MWA_NO_ALT_ENTER: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MWA_FLAGS = 2
DXGI_MWA_NO_PRINT_SCREEN: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MWA_FLAGS = 4
DXGI_MWA_VALID: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MWA_FLAGS = 7
DXGI_Message_Id = Int32
DXGI_MSG_IDXGISwapChain_CreationOrResizeBuffers_InvalidOutputWindow: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 0
DXGI_MSG_IDXGISwapChain_CreationOrResizeBuffers_BufferWidthInferred: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1
DXGI_MSG_IDXGISwapChain_CreationOrResizeBuffers_BufferHeightInferred: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 2
DXGI_MSG_IDXGISwapChain_CreationOrResizeBuffers_NoScanoutFlagChanged: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 3
DXGI_MSG_IDXGISwapChain_Creation_MaxBufferCountExceeded: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 4
DXGI_MSG_IDXGISwapChain_Creation_TooFewBuffers: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 5
DXGI_MSG_IDXGISwapChain_Creation_NoOutputWindow: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 6
DXGI_MSG_IDXGISwapChain_Destruction_OtherMethodsCalled: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 7
DXGI_MSG_IDXGISwapChain_GetDesc_pDescIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 8
DXGI_MSG_IDXGISwapChain_GetBuffer_ppSurfaceIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 9
DXGI_MSG_IDXGISwapChain_GetBuffer_NoAllocatedBuffers: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 10
DXGI_MSG_IDXGISwapChain_GetBuffer_iBufferMustBeZero: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 11
DXGI_MSG_IDXGISwapChain_GetBuffer_iBufferOOB: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 12
DXGI_MSG_IDXGISwapChain_GetContainingOutput_ppOutputIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 13
DXGI_MSG_IDXGISwapChain_Present_SyncIntervalOOB: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 14
DXGI_MSG_IDXGISwapChain_Present_InvalidNonPreRotatedFlag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 15
DXGI_MSG_IDXGISwapChain_Present_NoAllocatedBuffers: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 16
DXGI_MSG_IDXGISwapChain_Present_GetDXGIAdapterFailed: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 17
DXGI_MSG_IDXGISwapChain_ResizeBuffers_BufferCountOOB: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 18
DXGI_MSG_IDXGISwapChain_ResizeBuffers_UnreleasedReferences: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 19
DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidSwapChainFlag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 20
DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidNonPreRotatedFlag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 21
DXGI_MSG_IDXGISwapChain_ResizeTarget_RefreshRateDivideByZero: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 22
DXGI_MSG_IDXGISwapChain_SetFullscreenState_InvalidTarget: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 23
DXGI_MSG_IDXGISwapChain_GetFrameStatistics_pStatsIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 24
DXGI_MSG_IDXGISwapChain_GetLastPresentCount_pLastPresentCountIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 25
DXGI_MSG_IDXGISwapChain_SetFullscreenState_RemoteNotSupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 26
DXGI_MSG_IDXGIOutput_TakeOwnership_FailedToAcquireFullscreenMutex: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 27
DXGI_MSG_IDXGIFactory_CreateSoftwareAdapter_ppAdapterInterfaceIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 28
DXGI_MSG_IDXGIFactory_EnumAdapters_ppAdapterInterfaceIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 29
DXGI_MSG_IDXGIFactory_CreateSwapChain_ppSwapChainIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 30
DXGI_MSG_IDXGIFactory_CreateSwapChain_pDescIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 31
DXGI_MSG_IDXGIFactory_CreateSwapChain_UnknownSwapEffect: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 32
DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidFlags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 33
DXGI_MSG_IDXGIFactory_CreateSwapChain_NonPreRotatedFlagAndWindowed: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 34
DXGI_MSG_IDXGIFactory_CreateSwapChain_NullDeviceInterface: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 35
DXGI_MSG_IDXGIFactory_GetWindowAssociation_phWndIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 36
DXGI_MSG_IDXGIFactory_MakeWindowAssociation_InvalidFlags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 37
DXGI_MSG_IDXGISurface_Map_InvalidSurface: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 38
DXGI_MSG_IDXGISurface_Map_FlagsSetToZero: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 39
DXGI_MSG_IDXGISurface_Map_DiscardAndReadFlagSet: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 40
DXGI_MSG_IDXGISurface_Map_DiscardButNotWriteFlagSet: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 41
DXGI_MSG_IDXGISurface_Map_NoCPUAccess: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 42
DXGI_MSG_IDXGISurface_Map_ReadFlagSetButCPUAccessIsDynamic: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 43
DXGI_MSG_IDXGISurface_Map_DiscardFlagSetButCPUAccessIsNotDynamic: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 44
DXGI_MSG_IDXGIOutput_GetDisplayModeList_pNumModesIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 45
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_ModeHasInvalidWidthOrHeight: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 46
DXGI_MSG_IDXGIOutput_GetCammaControlCapabilities_NoOwnerDevice: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 47
DXGI_MSG_IDXGIOutput_TakeOwnership_pDeviceIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 48
DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_NoOwnerDevice: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 49
DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_pDestinationIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 50
DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_MapOfDestinationFailed: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 51
DXGI_MSG_IDXGIOutput_GetFrameStatistics_NoOwnerDevice: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 52
DXGI_MSG_IDXGIOutput_GetFrameStatistics_pStatsIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 53
DXGI_MSG_IDXGIOutput_SetGammaControl_NoOwnerDevice: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 54
DXGI_MSG_IDXGIOutput_GetGammaControl_NoOwnerDevice: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 55
DXGI_MSG_IDXGIOutput_GetGammaControl_NoGammaControls: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 56
DXGI_MSG_IDXGIOutput_SetDisplaySurface_IDXGIResourceNotSupportedBypPrimary: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 57
DXGI_MSG_IDXGIOutput_SetDisplaySurface_pPrimaryIsInvalid: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 58
DXGI_MSG_IDXGIOutput_SetDisplaySurface_NoOwnerDevice: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 59
DXGI_MSG_IDXGIOutput_TakeOwnership_RemoteDeviceNotSupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 60
DXGI_MSG_IDXGIOutput_GetDisplayModeList_RemoteDeviceNotSupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 61
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_RemoteDeviceNotSupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 62
DXGI_MSG_IDXGIDevice_CreateSurface_InvalidParametersWithpSharedResource: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 63
DXGI_MSG_IDXGIObject_GetPrivateData_puiDataSizeIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 64
DXGI_MSG_IDXGISwapChain_Creation_InvalidOutputWindow: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 65
DXGI_MSG_IDXGISwapChain_Release_SwapChainIsFullscreen: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 66
DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_InvalidTargetSurfaceFormat: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 67
DXGI_MSG_IDXGIFactory_CreateSoftwareAdapter_ModuleIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 68
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_IDXGIDeviceNotSupportedBypConcernedDevice: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 69
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_pModeToMatchOrpClosestMatchIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 70
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_ModeHasRefreshRateDenominatorZero: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 71
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_UnknownFormatIsInvalidForConfiguration: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 72
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_InvalidDisplayModeScanlineOrdering: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 73
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_InvalidDisplayModeScaling: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 74
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_InvalidDisplayModeFormatAndDeviceCombination: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 75
DXGI_MSG_IDXGIFactory_Creation_CalledFromDllMain: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 76
DXGI_MSG_IDXGISwapChain_SetFullscreenState_OutputNotOwnedBySwapChainDevice: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 77
DXGI_MSG_IDXGISwapChain_Creation_InvalidWindowStyle: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 78
DXGI_MSG_IDXGISwapChain_GetFrameStatistics_UnsupportedStatistics: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 79
DXGI_MSG_IDXGISwapChain_GetContainingOutput_SwapchainAdapterDoesNotControlOutput: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 80
DXGI_MSG_IDXGIOutput_SetOrGetGammaControl_pArrayIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 81
DXGI_MSG_IDXGISwapChain_SetFullscreenState_FullscreenInvalidForChildWindows: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 82
DXGI_MSG_IDXGIFactory_Release_CalledFromDllMain: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 83
DXGI_MSG_IDXGISwapChain_Present_UnreleasedHDC: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 84
DXGI_MSG_IDXGISwapChain_ResizeBuffers_NonPreRotatedAndGDICompatibleFlags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 85
DXGI_MSG_IDXGIFactory_CreateSwapChain_NonPreRotatedAndGDICompatibleFlags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 86
DXGI_MSG_IDXGISurface1_GetDC_pHdcIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 87
DXGI_MSG_IDXGISurface1_GetDC_SurfaceNotTexture2D: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 88
DXGI_MSG_IDXGISurface1_GetDC_GDICompatibleFlagNotSet: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 89
DXGI_MSG_IDXGISurface1_GetDC_UnreleasedHDC: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 90
DXGI_MSG_IDXGISurface_Map_NoCPUAccess2: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 91
DXGI_MSG_IDXGISurface1_ReleaseDC_GetDCNotCalled: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 92
DXGI_MSG_IDXGISurface1_ReleaseDC_InvalidRectangleDimensions: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 93
DXGI_MSG_IDXGIOutput_TakeOwnership_RemoteOutputNotSupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 94
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_RemoteOutputNotSupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 95
DXGI_MSG_IDXGIOutput_GetDisplayModeList_RemoteOutputNotSupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 96
DXGI_MSG_IDXGIFactory_CreateSwapChain_pDeviceHasMismatchedDXGIFactory: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 97
DXGI_MSG_IDXGISwapChain_Present_NonOptimalFSConfiguration: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 98
DXGI_MSG_IDXGIFactory_CreateSwapChain_FlipSequentialNotSupportedOnD3D10: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 99
DXGI_MSG_IDXGIFactory_CreateSwapChain_BufferCountOOBForFlipSequential: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 100
DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidFormatForFlipSequential: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 101
DXGI_MSG_IDXGIFactory_CreateSwapChain_MultiSamplingNotSupportedForFlipSequential: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 102
DXGI_MSG_IDXGISwapChain_ResizeBuffers_BufferCountOOBForFlipSequential: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 103
DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidFormatForFlipSequential: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 104
DXGI_MSG_IDXGISwapChain_Present_PartialPresentationBeforeStandardPresentation: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 105
DXGI_MSG_IDXGISwapChain_Present_FullscreenPartialPresentIsInvalid: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 106
DXGI_MSG_IDXGISwapChain_Present_InvalidPresentTestOrDoNotSequenceFlag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 107
DXGI_MSG_IDXGISwapChain_Present_ScrollInfoWithNoDirtyRectsSpecified: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 108
DXGI_MSG_IDXGISwapChain_Present_EmptyScrollRect: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 109
DXGI_MSG_IDXGISwapChain_Present_ScrollRectOutOfBackbufferBounds: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 110
DXGI_MSG_IDXGISwapChain_Present_ScrollRectOutOfBackbufferBoundsWithOffset: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 111
DXGI_MSG_IDXGISwapChain_Present_EmptyDirtyRect: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 112
DXGI_MSG_IDXGISwapChain_Present_DirtyRectOutOfBackbufferBounds: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 113
DXGI_MSG_IDXGIFactory_CreateSwapChain_UnsupportedBufferUsageFlags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 114
DXGI_MSG_IDXGISwapChain_Present_DoNotSequenceFlagSetButPreviousBufferIsUndefined: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 115
DXGI_MSG_IDXGISwapChain_Present_UnsupportedFlags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 116
DXGI_MSG_IDXGISwapChain_Present_FlipModelChainMustResizeOrCreateOnFSTransition: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 117
DXGI_MSG_IDXGIFactory_CreateSwapChain_pRestrictToOutputFromOtherIDXGIFactory: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 118
DXGI_MSG_IDXGIFactory_CreateSwapChain_RestrictOutputNotSupportedOnAdapter: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 119
DXGI_MSG_IDXGISwapChain_Present_RestrictToOutputFlagSetButInvalidpRestrictToOutput: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 120
DXGI_MSG_IDXGISwapChain_Present_RestrictToOutputFlagdWithFullscreen: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 121
DXGI_MSG_IDXGISwapChain_Present_RestrictOutputFlagWithStaleSwapChain: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 122
DXGI_MSG_IDXGISwapChain_Present_OtherFlagsCausingInvalidPresentTestFlag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 123
DXGI_MSG_IDXGIFactory_CreateSwapChain_UnavailableInSession0: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 124
DXGI_MSG_IDXGIFactory_MakeWindowAssociation_UnavailableInSession0: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 125
DXGI_MSG_IDXGIFactory_GetWindowAssociation_UnavailableInSession0: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 126
DXGI_MSG_IDXGIAdapter_EnumOutputs_UnavailableInSession0: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 127
DXGI_MSG_IDXGISwapChain_CreationOrSetFullscreenState_StereoDisabled: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 128
DXGI_MSG_IDXGIFactory2_UnregisterStatus_CookieNotFound: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 129
DXGI_MSG_IDXGISwapChain_Present_ProtectedContentInWindowedModeWithoutFSOrOverlay: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 130
DXGI_MSG_IDXGISwapChain_Present_ProtectedContentInWindowedModeWithoutFlipSequential: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 131
DXGI_MSG_IDXGISwapChain_Present_ProtectedContentWithRDPDriver: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 132
DXGI_MSG_IDXGISwapChain_Present_ProtectedContentInWindowedModeWithDWMOffOrInvalidDisplayAffinity: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 133
DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_WidthOrHeightIsZero: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 134
DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_OnlyFlipSequentialSupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 135
DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_UnsupportedOnAdapter: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 136
DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_UnsupportedOnWindows7: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 137
DXGI_MSG_IDXGISwapChain_SetFullscreenState_FSTransitionWithCompositionSwapChain: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 138
DXGI_MSG_IDXGISwapChain_ResizeTarget_InvalidWithCompositionSwapChain: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 139
DXGI_MSG_IDXGISwapChain_ResizeBuffers_WidthOrHeightIsZero: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 140
DXGI_MSG_IDXGIFactory_CreateSwapChain_ScalingNoneIsFlipModelOnly: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 141
DXGI_MSG_IDXGIFactory_CreateSwapChain_ScalingUnrecognized: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 142
DXGI_MSG_IDXGIFactory_CreateSwapChain_DisplayOnlyFullscreenUnsupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 143
DXGI_MSG_IDXGIFactory_CreateSwapChain_DisplayOnlyUnsupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 144
DXGI_MSG_IDXGISwapChain_Present_RestartIsFullscreenOnly: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 145
DXGI_MSG_IDXGISwapChain_Present_ProtectedWindowlessPresentationRequiresDisplayOnly: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 146
DXGI_MSG_IDXGISwapChain_SetFullscreenState_DisplayOnlyUnsupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 147
DXGI_MSG_IDXGISwapChain1_SetBackgroundColor_OutOfRange: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 148
DXGI_MSG_IDXGISwapChain_ResizeBuffers_DisplayOnlyFullscreenUnsupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 149
DXGI_MSG_IDXGISwapChain_ResizeBuffers_DisplayOnlyUnsupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 150
DXGI_MSG_IDXGISwapchain_Present_ScrollUnsupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 151
DXGI_MSG_IDXGISwapChain1_SetRotation_UnsupportedOS: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 152
DXGI_MSG_IDXGISwapChain1_GetRotation_UnsupportedOS: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 153
DXGI_MSG_IDXGISwapchain_Present_FullscreenRotation: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 154
DXGI_MSG_IDXGISwapChain_Present_PartialPresentationWithMSAABuffers: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 155
DXGI_MSG_IDXGISwapChain1_SetRotation_FlipSequentialRequired: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 156
DXGI_MSG_IDXGISwapChain1_SetRotation_InvalidRotation: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 157
DXGI_MSG_IDXGISwapChain1_GetRotation_FlipSequentialRequired: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 158
DXGI_MSG_IDXGISwapChain_GetHwnd_WrongType: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 159
DXGI_MSG_IDXGISwapChain_GetCompositionSurface_WrongType: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 160
DXGI_MSG_IDXGISwapChain_GetCoreWindow_WrongType: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 161
DXGI_MSG_IDXGISwapChain_GetFullscreenDesc_NonHwnd: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 162
DXGI_MSG_IDXGISwapChain_SetFullscreenState_CoreWindow: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 163
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_UnsupportedOnWindows7: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 164
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_pWindowIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 165
DXGI_MSG_IDXGIFactory_CreateSwapChain_FSUnsupportedForModernApps: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 166
DXGI_MSG_IDXGIFactory_MakeWindowAssociation_ModernApp: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 167
DXGI_MSG_IDXGISwapChain_ResizeTarget_ModernApp: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 168
DXGI_MSG_IDXGISwapChain_ResizeTarget_pNewTargetParametersIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 169
DXGI_MSG_IDXGIOutput_SetDisplaySurface_ModernApp: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 170
DXGI_MSG_IDXGIOutput_TakeOwnership_ModernApp: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 171
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_pWindowIsInvalid: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 172
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCompositionSurface_InvalidHandle: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 173
DXGI_MSG_IDXGISurface1_GetDC_ModernApp: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 174
DXGI_MSG_IDXGIFactory_CreateSwapChain_ScalingNoneRequiresWindows8OrNewer: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 175
DXGI_MSG_IDXGISwapChain_Present_TemporaryMonoAndPreferRight: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 176
DXGI_MSG_IDXGISwapChain_Present_TemporaryMonoOrPreferRightWithDoNotSequence: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 177
DXGI_MSG_IDXGISwapChain_Present_TemporaryMonoOrPreferRightWithoutStereo: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 178
DXGI_MSG_IDXGISwapChain_Present_TemporaryMonoUnsupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 179
DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_ArraySizeMismatch: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 180
DXGI_MSG_IDXGISwapChain_Present_PartialPresentationWithSwapEffectDiscard: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 181
DXGI_MSG_IDXGIFactory_CreateSwapChain_AlphaUnrecognized: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 182
DXGI_MSG_IDXGIFactory_CreateSwapChain_AlphaIsWindowlessOnly: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 183
DXGI_MSG_IDXGIFactory_CreateSwapChain_AlphaIsFlipModelOnly: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 184
DXGI_MSG_IDXGIFactory_CreateSwapChain_RestrictToOutputAdapterMismatch: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 185
DXGI_MSG_IDXGIFactory_CreateSwapChain_DisplayOnlyOnLegacy: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 186
DXGI_MSG_IDXGISwapChain_ResizeBuffers_DisplayOnlyOnLegacy: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 187
DXGI_MSG_IDXGIResource1_CreateSubresourceSurface_InvalidIndex: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 188
DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_InvalidScaling: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 189
DXGI_MSG_IDXGIFactory_CreateSwapChainForCoreWindow_InvalidSwapEffect: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 190
DXGI_MSG_IDXGIResource1_CreateSharedHandle_UnsupportedOS: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 191
DXGI_MSG_IDXGIFactory2_RegisterOcclusionStatusWindow_UnsupportedOS: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 192
DXGI_MSG_IDXGIFactory2_RegisterOcclusionStatusEvent_UnsupportedOS: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 193
DXGI_MSG_IDXGIOutput1_DuplicateOutput_UnsupportedOS: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 194
DXGI_MSG_IDXGIDisplayControl_IsStereoEnabled_UnsupportedOS: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 195
DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_InvalidAlphaMode: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 196
DXGI_MSG_IDXGIFactory_GetSharedResourceAdapterLuid_InvalidResource: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 197
DXGI_MSG_IDXGIFactory_GetSharedResourceAdapterLuid_InvalidLUID: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 198
DXGI_MSG_IDXGIFactory_GetSharedResourceAdapterLuid_UnsupportedOS: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 199
DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_2DOnly: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 200
DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_StagingOnly: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 201
DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_NeedCPUAccessWrite: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 202
DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_NoShared: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 203
DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_OnlyMipLevels1: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 204
DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_MappedOrOfferedResource: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 205
DXGI_MSG_IDXGISwapChain_SetFullscreenState_FSUnsupportedForModernApps: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 206
DXGI_MSG_IDXGIFactory_CreateSwapChain_FailedToGoFSButNonPreRotated: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 207
DXGI_MSG_IDXGIFactory_CreateSwapChainOrRegisterOcclusionStatus_BlitModelUsedWhileRegisteredForOcclusionStatusEvents: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 208
DXGI_MSG_IDXGISwapChain_Present_BlitModelUsedWhileRegisteredForOcclusionStatusEvents: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 209
DXGI_MSG_IDXGIFactory_CreateSwapChain_WaitableSwapChainsAreFlipModelOnly: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 210
DXGI_MSG_IDXGIFactory_CreateSwapChain_WaitableSwapChainsAreNotFullscreen: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 211
DXGI_MSG_IDXGISwapChain_SetFullscreenState_Waitable: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 212
DXGI_MSG_IDXGISwapChain_ResizeBuffers_CannotAddOrRemoveWaitableFlag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 213
DXGI_MSG_IDXGISwapChain_GetFrameLatencyWaitableObject_OnlyWaitable: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 214
DXGI_MSG_IDXGISwapChain_GetMaximumFrameLatency_OnlyWaitable: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 215
DXGI_MSG_IDXGISwapChain_GetMaximumFrameLatency_pMaxLatencyIsNULL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 216
DXGI_MSG_IDXGISwapChain_SetMaximumFrameLatency_OnlyWaitable: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 217
DXGI_MSG_IDXGISwapChain_SetMaximumFrameLatency_MaxLatencyIsOutOfBounds: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 218
DXGI_MSG_IDXGIFactory_CreateSwapChain_ForegroundIsCoreWindowOnly: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 219
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_ForegroundUnsupportedOnAdapter: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 220
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_InvalidScaling: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 221
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_InvalidAlphaMode: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 222
DXGI_MSG_IDXGISwapChain_ResizeBuffers_CannotAddOrRemoveForegroundFlag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 223
DXGI_MSG_IDXGISwapChain_SetMatrixTransform_MatrixPointerCannotBeNull: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 224
DXGI_MSG_IDXGISwapChain_SetMatrixTransform_RequiresCompositionSwapChain: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 225
DXGI_MSG_IDXGISwapChain_SetMatrixTransform_MatrixMustBeFinite: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 226
DXGI_MSG_IDXGISwapChain_SetMatrixTransform_MatrixMustBeTranslateAndOrScale: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 227
DXGI_MSG_IDXGISwapChain_GetMatrixTransform_MatrixPointerCannotBeNull: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 228
DXGI_MSG_IDXGISwapChain_GetMatrixTransform_RequiresCompositionSwapChain: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 229
DXGI_MSG_DXGIGetDebugInterface1_NULL_ppDebug: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 230
DXGI_MSG_DXGIGetDebugInterface1_InvalidFlags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 231
DXGI_MSG_IDXGISwapChain_Present_Decode: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 232
DXGI_MSG_IDXGISwapChain_ResizeBuffers_Decode: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 233
DXGI_MSG_IDXGISwapChain_SetSourceSize_FlipModel: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 234
DXGI_MSG_IDXGISwapChain_SetSourceSize_Decode: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 235
DXGI_MSG_IDXGISwapChain_SetSourceSize_WidthHeight: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 236
DXGI_MSG_IDXGISwapChain_GetSourceSize_NullPointers: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 237
DXGI_MSG_IDXGISwapChain_GetSourceSize_Decode: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 238
DXGI_MSG_IDXGIDecodeSwapChain_SetColorSpace_InvalidFlags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 239
DXGI_MSG_IDXGIDecodeSwapChain_SetSourceRect_InvalidRect: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 240
DXGI_MSG_IDXGIDecodeSwapChain_SetTargetRect_InvalidRect: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 241
DXGI_MSG_IDXGIDecodeSwapChain_SetDestSize_InvalidSize: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 242
DXGI_MSG_IDXGIDecodeSwapChain_GetSourceRect_InvalidPointer: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 243
DXGI_MSG_IDXGIDecodeSwapChain_GetTargetRect_InvalidPointer: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 244
DXGI_MSG_IDXGIDecodeSwapChain_GetDestSize_InvalidPointer: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 245
DXGI_MSG_IDXGISwapChain_PresentBuffer_YUV: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 246
DXGI_MSG_IDXGISwapChain_SetSourceSize_YUV: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 247
DXGI_MSG_IDXGISwapChain_GetSourceSize_YUV: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 248
DXGI_MSG_IDXGISwapChain_SetMatrixTransform_YUV: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 249
DXGI_MSG_IDXGISwapChain_GetMatrixTransform_YUV: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 250
DXGI_MSG_IDXGISwapChain_Present_PartialPresentation_YUV: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 251
DXGI_MSG_IDXGISwapChain_ResizeBuffers_CannotAddOrRemoveFlag_YUV: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 252
DXGI_MSG_IDXGISwapChain_ResizeBuffers_Alignment_YUV: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 253
DXGI_MSG_IDXGIFactory_CreateSwapChain_ShaderInputUnsupported_YUV: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 254
DXGI_MSG_IDXGIOutput3_CheckOverlaySupport_NullPointers: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 255
DXGI_MSG_IDXGIOutput3_CheckOverlaySupport_IDXGIDeviceNotSupportedBypConcernedDevice: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 256
DXGI_MSG_IDXGIAdapter_EnumOutputs2_InvalidEnumOutputs2Flag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 257
DXGI_MSG_IDXGISwapChain_CreationOrSetFullscreenState_FSUnsupportedForFlipDiscard: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 258
DXGI_MSG_IDXGIOutput4_CheckOverlayColorSpaceSupport_NullPointers: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 259
DXGI_MSG_IDXGIOutput4_CheckOverlayColorSpaceSupport_IDXGIDeviceNotSupportedBypConcernedDevice: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 260
DXGI_MSG_IDXGISwapChain3_CheckColorSpaceSupport_NullPointers: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 261
DXGI_MSG_IDXGISwapChain3_SetColorSpace1_InvalidColorSpace: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 262
DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidHwProtect: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 263
DXGI_MSG_IDXGIFactory_CreateSwapChain_HwProtectUnsupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 264
DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidHwProtect: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 265
DXGI_MSG_IDXGISwapChain_ResizeBuffers_HwProtectUnsupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 266
DXGI_MSG_IDXGISwapChain_ResizeBuffers1_D3D12Only: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 267
DXGI_MSG_IDXGISwapChain_ResizeBuffers1_FlipModel: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 268
DXGI_MSG_IDXGISwapChain_ResizeBuffers1_NodeMaskAndQueueRequired: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 269
DXGI_MSG_IDXGISwapChain_CreateSwapChain_InvalidHwProtectGdiFlag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 270
DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidHwProtectGdiFlag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 271
DXGI_MSG_IDXGIFactory_CreateSwapChain_10BitFormatNotSupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 272
DXGI_MSG_IDXGIFactory_CreateSwapChain_FlipSwapEffectRequired: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 273
DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidDevice: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 274
DXGI_MSG_IDXGIOutput_TakeOwnership_Unsupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 275
DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidQueue: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 276
DXGI_MSG_IDXGISwapChain3_ResizeBuffers1_InvalidQueue: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 277
DXGI_MSG_IDXGIFactory_CreateSwapChainForHwnd_InvalidScaling: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 278
DXGI_MSG_IDXGISwapChain3_SetHDRMetaData_InvalidSize: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 279
DXGI_MSG_IDXGISwapChain3_SetHDRMetaData_InvalidPointer: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 280
DXGI_MSG_IDXGISwapChain3_SetHDRMetaData_InvalidType: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 281
DXGI_MSG_IDXGISwapChain_Present_FullscreenAllowTearingIsInvalid: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 282
DXGI_MSG_IDXGISwapChain_Present_AllowTearingRequiresPresentIntervalZero: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 283
DXGI_MSG_IDXGISwapChain_Present_AllowTearingRequiresCreationFlag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 284
DXGI_MSG_IDXGISwapChain_ResizeBuffers_CannotAddOrRemoveAllowTearingFlag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 285
DXGI_MSG_IDXGIFactory_CreateSwapChain_AllowTearingFlagIsFlipModelOnly: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 286
DXGI_MSG_IDXGIFactory_CheckFeatureSupport_InvalidFeature: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 287
DXGI_MSG_IDXGIFactory_CheckFeatureSupport_InvalidSize: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 288
DXGI_MSG_IDXGIOutput6_CheckHardwareCompositionSupport_NullPointer: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 289
DXGI_MSG_IDXGISwapChain_SetFullscreenState_PerMonitorDpiShimApplied: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 290
DXGI_MSG_IDXGIOutput_DuplicateOutput_PerMonitorDpiShimApplied: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 291
DXGI_MSG_IDXGIOutput_DuplicateOutput1_PerMonitorDpiRequired: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 292
DXGI_MSG_IDXGIFactory7_UnregisterAdaptersChangedEvent_CookieNotFound: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 293
DXGI_MSG_IDXGIFactory_CreateSwapChain_LegacyBltModelSwapEffect: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 294
DXGI_MSG_IDXGISwapChain4_SetHDRMetaData_MetadataUnchanged: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 295
DXGI_MSG_IDXGISwapChain_Present_11On12_Released_Resource: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 296
DXGI_MSG_IDXGIFactory_CreateSwapChain_MultipleSwapchainRefToSurface_DeferredDtr: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 297
DXGI_MSG_IDXGIFactory_MakeWindowAssociation_NoOpBehavior: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 298
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_NotForegroundWindow: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1000
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_DISCARD_BufferCount: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1001
DXGI_MSG_Phone_IDXGISwapChain_SetFullscreenState_NotAvailable: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1002
DXGI_MSG_Phone_IDXGISwapChain_ResizeBuffers_NotAvailable: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1003
DXGI_MSG_Phone_IDXGISwapChain_ResizeTarget_NotAvailable: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1004
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidLayerIndex: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1005
DXGI_MSG_Phone_IDXGISwapChain_Present_MultipleLayerIndex: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1006
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidLayerFlag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1007
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidRotation: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1008
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidBlend: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1009
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidResource: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1010
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidMultiPlaneOverlayResource: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1011
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidIndexForPrimary: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1012
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidIndexForOverlay: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1013
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidSubResourceIndex: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1014
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidSourceRect: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1015
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidDestinationRect: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1016
DXGI_MSG_Phone_IDXGISwapChain_Present_MultipleResource: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1017
DXGI_MSG_Phone_IDXGISwapChain_Present_NotSharedResource: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1018
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidFlag: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1019
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidInterval: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1020
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_MSAA_NotSupported: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1021
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_ScalingAspectRatioStretch_Supported_ModernApp: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1022
DXGI_MSG_Phone_IDXGISwapChain_GetFrameStatistics_NotAvailable_ModernApp: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1023
DXGI_MSG_Phone_IDXGISwapChain_Present_ReplaceInterval0With1: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1024
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_FailedRegisterWithCompositor: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1025
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_NotForegroundWindow_AtRendering: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1026
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_FLIP_SEQUENTIAL_BufferCount: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1027
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_FLIP_Modern_CoreWindow_Only: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1028
DXGI_MSG_Phone_IDXGISwapChain_Present1_RequiresOverlays: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1029
DXGI_MSG_Phone_IDXGISwapChain_SetBackgroundColor_FlipSequentialRequired: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1030
DXGI_MSG_Phone_IDXGISwapChain_GetBackgroundColor_FlipSequentialRequired: win32more.Windows.Win32.Graphics.Dxgi.DXGI_Message_Id = 1031
DXGI_OFFER_RESOURCE_FLAGS = Int32
DXGI_OFFER_RESOURCE_FLAG_ALLOW_DECOMMIT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OFFER_RESOURCE_FLAGS = 1
DXGI_OFFER_RESOURCE_PRIORITY = Int32
DXGI_OFFER_RESOURCE_PRIORITY_LOW: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OFFER_RESOURCE_PRIORITY = 1
DXGI_OFFER_RESOURCE_PRIORITY_NORMAL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OFFER_RESOURCE_PRIORITY = 2
DXGI_OFFER_RESOURCE_PRIORITY_HIGH: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OFFER_RESOURCE_PRIORITY = 3
class DXGI_OUTDUPL_DESC(Structure):
    ModeDesc: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_DESC
    Rotation: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION
    DesktopImageInSystemMemory: win32more.Windows.Win32.Foundation.BOOL
DXGI_OUTDUPL_FLAG = Int32
DXGI_OUTDUPL_COMPOSITED_UI_CAPTURE_ONLY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OUTDUPL_FLAG = 1
class DXGI_OUTDUPL_FRAME_INFO(Structure):
    LastPresentTime: Int64
    LastMouseUpdateTime: Int64
    AccumulatedFrames: UInt32
    RectsCoalesced: win32more.Windows.Win32.Foundation.BOOL
    ProtectedContentMaskedOut: win32more.Windows.Win32.Foundation.BOOL
    PointerPosition: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OUTDUPL_POINTER_POSITION
    TotalMetadataBufferSize: UInt32
    PointerShapeBufferSize: UInt32
class DXGI_OUTDUPL_MOVE_RECT(Structure):
    SourcePoint: win32more.Windows.Win32.Foundation.POINT
    DestinationRect: win32more.Windows.Win32.Foundation.RECT
class DXGI_OUTDUPL_POINTER_POSITION(Structure):
    Position: win32more.Windows.Win32.Foundation.POINT
    Visible: win32more.Windows.Win32.Foundation.BOOL
class DXGI_OUTDUPL_POINTER_SHAPE_INFO(Structure):
    Type: UInt32
    Width: UInt32
    Height: UInt32
    Pitch: UInt32
    HotSpot: win32more.Windows.Win32.Foundation.POINT
DXGI_OUTDUPL_POINTER_SHAPE_TYPE = Int32
DXGI_OUTDUPL_POINTER_SHAPE_TYPE_MONOCHROME: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OUTDUPL_POINTER_SHAPE_TYPE = 1
DXGI_OUTDUPL_POINTER_SHAPE_TYPE_COLOR: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OUTDUPL_POINTER_SHAPE_TYPE = 2
DXGI_OUTDUPL_POINTER_SHAPE_TYPE_MASKED_COLOR: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OUTDUPL_POINTER_SHAPE_TYPE = 4
class DXGI_OUTPUT_DESC(Structure):
    DeviceName: Char * 32
    DesktopCoordinates: win32more.Windows.Win32.Foundation.RECT
    AttachedToDesktop: win32more.Windows.Win32.Foundation.BOOL
    Rotation: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION
    Monitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR
class DXGI_OUTPUT_DESC1(Structure):
    DeviceName: Char * 32
    DesktopCoordinates: win32more.Windows.Win32.Foundation.RECT
    AttachedToDesktop: win32more.Windows.Win32.Foundation.BOOL
    Rotation: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION
    Monitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR
    BitsPerColor: UInt32
    ColorSpace: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE
    RedPrimary: Single * 2
    GreenPrimary: Single * 2
    BluePrimary: Single * 2
    WhitePoint: Single * 2
    MinLuminance: Single
    MaxLuminance: Single
    MaxFullFrameLuminance: Single
DXGI_OVERLAY_COLOR_SPACE_SUPPORT_FLAG = Int32
DXGI_OVERLAY_COLOR_SPACE_SUPPORT_FLAG_PRESENT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OVERLAY_COLOR_SPACE_SUPPORT_FLAG = 1
DXGI_OVERLAY_SUPPORT_FLAG = Int32
DXGI_OVERLAY_SUPPORT_FLAG_DIRECT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OVERLAY_SUPPORT_FLAG = 1
DXGI_OVERLAY_SUPPORT_FLAG_SCALING: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OVERLAY_SUPPORT_FLAG = 2
DXGI_PRESENT = UInt32
DXGI_PRESENT_TEST: win32more.Windows.Win32.Graphics.Dxgi.DXGI_PRESENT = 1
DXGI_PRESENT_DO_NOT_SEQUENCE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_PRESENT = 2
DXGI_PRESENT_RESTART: win32more.Windows.Win32.Graphics.Dxgi.DXGI_PRESENT = 4
DXGI_PRESENT_DO_NOT_WAIT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_PRESENT = 8
DXGI_PRESENT_STEREO_PREFER_RIGHT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_PRESENT = 16
DXGI_PRESENT_STEREO_TEMPORARY_MONO: win32more.Windows.Win32.Graphics.Dxgi.DXGI_PRESENT = 32
DXGI_PRESENT_RESTRICT_TO_OUTPUT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_PRESENT = 64
DXGI_PRESENT_USE_DURATION: win32more.Windows.Win32.Graphics.Dxgi.DXGI_PRESENT = 256
DXGI_PRESENT_ALLOW_TEARING: win32more.Windows.Win32.Graphics.Dxgi.DXGI_PRESENT = 512
class DXGI_PRESENT_PARAMETERS(Structure):
    DirtyRectsCount: UInt32
    pDirtyRects: POINTER(win32more.Windows.Win32.Foundation.RECT)
    pScrollRect: POINTER(win32more.Windows.Win32.Foundation.RECT)
    pScrollOffset: POINTER(win32more.Windows.Win32.Foundation.POINT)
class DXGI_QUERY_VIDEO_MEMORY_INFO(Structure):
    Budget: UInt64
    CurrentUsage: UInt64
    AvailableForReservation: UInt64
    CurrentReservation: UInt64
DXGI_RECLAIM_RESOURCE_RESULTS = Int32
DXGI_RECLAIM_RESOURCE_RESULT_OK: win32more.Windows.Win32.Graphics.Dxgi.DXGI_RECLAIM_RESOURCE_RESULTS = 0
DXGI_RECLAIM_RESOURCE_RESULT_DISCARDED: win32more.Windows.Win32.Graphics.Dxgi.DXGI_RECLAIM_RESOURCE_RESULTS = 1
DXGI_RECLAIM_RESOURCE_RESULT_NOT_COMMITTED: win32more.Windows.Win32.Graphics.Dxgi.DXGI_RECLAIM_RESOURCE_RESULTS = 2
DXGI_RESIDENCY = Int32
DXGI_RESIDENCY_FULLY_RESIDENT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_RESIDENCY = 1
DXGI_RESIDENCY_RESIDENT_IN_SHARED_MEMORY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_RESIDENCY = 2
DXGI_RESIDENCY_EVICTED_TO_DISK: win32more.Windows.Win32.Graphics.Dxgi.DXGI_RESIDENCY = 3
DXGI_RESOURCE_PRIORITY = UInt32
DXGI_RESOURCE_PRIORITY_MINIMUM: win32more.Windows.Win32.Graphics.Dxgi.DXGI_RESOURCE_PRIORITY = 671088640
DXGI_RESOURCE_PRIORITY_LOW: win32more.Windows.Win32.Graphics.Dxgi.DXGI_RESOURCE_PRIORITY = 1342177280
DXGI_RESOURCE_PRIORITY_NORMAL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_RESOURCE_PRIORITY = 2013265920
DXGI_RESOURCE_PRIORITY_HIGH: win32more.Windows.Win32.Graphics.Dxgi.DXGI_RESOURCE_PRIORITY = 2684354560
DXGI_RESOURCE_PRIORITY_MAXIMUM: win32more.Windows.Win32.Graphics.Dxgi.DXGI_RESOURCE_PRIORITY = 3355443200
class DXGI_RGBA(Structure):
    r: Single
    g: Single
    b: Single
    a: Single
DXGI_SCALING = Int32
DXGI_SCALING_STRETCH: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SCALING = 0
DXGI_SCALING_NONE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SCALING = 1
DXGI_SCALING_ASPECT_RATIO_STRETCH: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SCALING = 2
class DXGI_SHARED_RESOURCE(Structure):
    Handle: win32more.Windows.Win32.Foundation.HANDLE
DXGI_SHARED_RESOURCE_RW = UInt32
DXGI_SHARED_RESOURCE_READ: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SHARED_RESOURCE_RW = 2147483648
DXGI_SHARED_RESOURCE_WRITE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SHARED_RESOURCE_RW = 1
class DXGI_SURFACE_DESC(Structure):
    Width: UInt32
    Height: UInt32
    Format: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    SampleDesc: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_SAMPLE_DESC
DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG = Int32
DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG_PRESENT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG = 1
DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG_OVERLAY_PRESENT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG = 2
class DXGI_SWAP_CHAIN_DESC(Structure):
    BufferDesc: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_DESC
    SampleDesc: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_SAMPLE_DESC
    BufferUsage: win32more.Windows.Win32.Graphics.Dxgi.DXGI_USAGE
    BufferCount: UInt32
    OutputWindow: win32more.Windows.Win32.Foundation.HWND
    Windowed: win32more.Windows.Win32.Foundation.BOOL
    SwapEffect: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_EFFECT
    Flags: UInt32
class DXGI_SWAP_CHAIN_DESC1(Structure):
    Width: UInt32
    Height: UInt32
    Format: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    Stereo: win32more.Windows.Win32.Foundation.BOOL
    SampleDesc: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_SAMPLE_DESC
    BufferUsage: win32more.Windows.Win32.Graphics.Dxgi.DXGI_USAGE
    BufferCount: UInt32
    Scaling: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SCALING
    SwapEffect: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_EFFECT
    AlphaMode: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_ALPHA_MODE
    Flags: UInt32
DXGI_SWAP_CHAIN_FLAG = Int32
DXGI_SWAP_CHAIN_FLAG_NONPREROTATED: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FLAG = 1
DXGI_SWAP_CHAIN_FLAG_ALLOW_MODE_SWITCH: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FLAG = 2
DXGI_SWAP_CHAIN_FLAG_GDI_COMPATIBLE: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FLAG = 4
DXGI_SWAP_CHAIN_FLAG_RESTRICTED_CONTENT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FLAG = 8
DXGI_SWAP_CHAIN_FLAG_RESTRICT_SHARED_RESOURCE_DRIVER: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FLAG = 16
DXGI_SWAP_CHAIN_FLAG_DISPLAY_ONLY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FLAG = 32
DXGI_SWAP_CHAIN_FLAG_FRAME_LATENCY_WAITABLE_OBJECT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FLAG = 64
DXGI_SWAP_CHAIN_FLAG_FOREGROUND_LAYER: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FLAG = 128
DXGI_SWAP_CHAIN_FLAG_FULLSCREEN_VIDEO: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FLAG = 256
DXGI_SWAP_CHAIN_FLAG_YUV_VIDEO: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FLAG = 512
DXGI_SWAP_CHAIN_FLAG_HW_PROTECTED: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FLAG = 1024
DXGI_SWAP_CHAIN_FLAG_ALLOW_TEARING: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FLAG = 2048
DXGI_SWAP_CHAIN_FLAG_RESTRICTED_TO_ALL_HOLOGRAPHIC_DISPLAYS: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FLAG = 4096
class DXGI_SWAP_CHAIN_FULLSCREEN_DESC(Structure):
    RefreshRate: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_RATIONAL
    ScanlineOrdering: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_SCANLINE_ORDER
    Scaling: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_SCALING
    Windowed: win32more.Windows.Win32.Foundation.BOOL
DXGI_SWAP_EFFECT = Int32
DXGI_SWAP_EFFECT_DISCARD: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_EFFECT = 0
DXGI_SWAP_EFFECT_SEQUENTIAL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_EFFECT = 1
DXGI_SWAP_EFFECT_FLIP_SEQUENTIAL: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_EFFECT = 3
DXGI_SWAP_EFFECT_FLIP_DISCARD: win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_EFFECT = 4
DXGI_USAGE = UInt32
DXGI_USAGE_SHADER_INPUT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_USAGE = 16
DXGI_USAGE_RENDER_TARGET_OUTPUT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_USAGE = 32
DXGI_USAGE_BACK_BUFFER: win32more.Windows.Win32.Graphics.Dxgi.DXGI_USAGE = 64
DXGI_USAGE_SHARED: win32more.Windows.Win32.Graphics.Dxgi.DXGI_USAGE = 128
DXGI_USAGE_READ_ONLY: win32more.Windows.Win32.Graphics.Dxgi.DXGI_USAGE = 256
DXGI_USAGE_DISCARD_ON_PRESENT: win32more.Windows.Win32.Graphics.Dxgi.DXGI_USAGE = 512
DXGI_USAGE_UNORDERED_ACCESS: win32more.Windows.Win32.Graphics.Dxgi.DXGI_USAGE = 1024
class IDXGIAdapter(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIObject
    _iid_ = Guid('{2411e7e1-12ac-4ccf-bd14-9798e8534dc0}')
    @commethod(7)
    def EnumOutputs(self, Output: UInt32, ppOutput: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDesc(self, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_DESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CheckInterfaceSupport(self, InterfaceName: POINTER(Guid), pUMDVersion: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIAdapter1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIAdapter
    _iid_ = Guid('{29038f61-3839-4626-91fd-086879011a05}')
    @commethod(10)
    def GetDesc1(self, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_DESC1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIAdapter2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIAdapter1
    _iid_ = Guid('{0aa1ae0a-fa0e-4b84-8644-e05ff8e5acb5}')
    @commethod(11)
    def GetDesc2(self, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_DESC2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIAdapter3(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIAdapter2
    _iid_ = Guid('{645967a4-1392-4310-a798-8053ce3e93fd}')
    @commethod(12)
    def RegisterHardwareContentProtectionTeardownStatusEvent(self, hEvent: win32more.Windows.Win32.Foundation.HANDLE, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def UnregisterHardwareContentProtectionTeardownStatus(self, dwCookie: UInt32) -> Void: ...
    @commethod(14)
    def QueryVideoMemoryInfo(self, NodeIndex: UInt32, MemorySegmentGroup: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MEMORY_SEGMENT_GROUP, pVideoMemoryInfo: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_QUERY_VIDEO_MEMORY_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetVideoMemoryReservation(self, NodeIndex: UInt32, MemorySegmentGroup: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MEMORY_SEGMENT_GROUP, Reservation: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RegisterVideoMemoryBudgetChangeNotificationEvent(self, hEvent: win32more.Windows.Win32.Foundation.HANDLE, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def UnregisterVideoMemoryBudgetChangeNotification(self, dwCookie: UInt32) -> Void: ...
class IDXGIAdapter4(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIAdapter3
    _iid_ = Guid('{3c8d99d1-4fbf-4181-a82c-af66bf7bd24e}')
    @commethod(18)
    def GetDesc3(self, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_ADAPTER_DESC3)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIDebug(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{119e7452-de9e-40fe-8806-88f90c12b441}')
    @commethod(3)
    def ReportLiveObjects(self, apiid: Guid, flags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_DEBUG_RLO_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIDebug1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDebug
    _iid_ = Guid('{c5a05f0c-16f2-4adf-9f4d-a8c4d58ac550}')
    @commethod(4)
    def EnableLeakTrackingForThread(self) -> Void: ...
    @commethod(5)
    def DisableLeakTrackingForThread(self) -> Void: ...
    @commethod(6)
    def IsLeakTrackingEnabledForThread(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IDXGIDecodeSwapChain(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2633066b-4514-4c7a-8fd8-12ea98059d18}')
    @commethod(3)
    def PresentBuffer(self, BufferToPresent: UInt32, SyncInterval: UInt32, Flags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_PRESENT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSourceRect(self, pRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetTargetRect(self, pRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetDestSize(self, Width: UInt32, Height: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSourceRect(self, pRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTargetRect(self, pRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDestSize(self, pWidth: POINTER(UInt32), pHeight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetColorSpace(self, ColorSpace: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetColorSpace(self) -> win32more.Windows.Win32.Graphics.Dxgi.DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS: ...
class IDXGIDevice(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIObject
    _iid_ = Guid('{54ec77fa-1377-44e6-8c32-88fd5f44c84c}')
    @commethod(7)
    def GetAdapter(self, pAdapter: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIAdapter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateSurface(self, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_SURFACE_DESC), NumSurfaces: UInt32, Usage: win32more.Windows.Win32.Graphics.Dxgi.DXGI_USAGE, pSharedResource: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_SHARED_RESOURCE), ppSurface: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGISurface)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def QueryResourceResidency(self, ppResources: POINTER(win32more.Windows.Win32.System.Com.IUnknown), pResidencyStatus: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_RESIDENCY), NumResources: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetGPUThreadPriority(self, Priority: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetGPUThreadPriority(self, pPriority: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIDevice1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDevice
    _iid_ = Guid('{77db970f-6276-48ba-ba28-070143b4392c}')
    @commethod(12)
    def SetMaximumFrameLatency(self, MaxLatency: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetMaximumFrameLatency(self, pMaxLatency: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIDevice2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDevice1
    _iid_ = Guid('{05008617-fbfd-4051-a790-144884b4f6a9}')
    @commethod(14)
    def OfferResources(self, NumResources: UInt32, ppResources: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIResource), Priority: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OFFER_RESOURCE_PRIORITY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ReclaimResources(self, NumResources: UInt32, ppResources: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIResource), pDiscarded: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EnqueueSetEvent(self, hEvent: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIDevice3(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDevice2
    _iid_ = Guid('{6007896c-3244-4afd-bf18-a6d3beda5023}')
    @commethod(17)
    def Trim(self) -> Void: ...
class IDXGIDevice4(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDevice3
    _iid_ = Guid('{95b4f95f-d8da-4ca4-9ee6-3b76d5968a10}')
    @commethod(18)
    def OfferResources1(self, NumResources: UInt32, ppResources: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIResource), Priority: win32more.Windows.Win32.Graphics.Dxgi.DXGI_OFFER_RESOURCE_PRIORITY, Flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ReclaimResources1(self, NumResources: UInt32, ppResources: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIResource), pResults: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_RECLAIM_RESOURCE_RESULTS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIDeviceSubObject(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIObject
    _iid_ = Guid('{3d3e0379-f9de-4d58-bb6c-18d62992f1a6}')
    @commethod(7)
    def GetDevice(self, riid: POINTER(Guid), ppDevice: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIDisplayControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ea9dbf1a-c88e-4486-854a-98aa0138f30c}')
    @commethod(3)
    def IsStereoEnabled(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(4)
    def SetStereoEnabled(self, enabled: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
class IDXGIFactory(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIObject
    _iid_ = Guid('{7b7166ec-21c7-44ae-b21a-c9ae321ae369}')
    @commethod(7)
    def EnumAdapters(self, Adapter: UInt32, ppAdapter: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIAdapter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MakeWindowAssociation(self, WindowHandle: win32more.Windows.Win32.Foundation.HWND, Flags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MWA_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetWindowAssociation(self, pWindowHandle: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateSwapChain(self, pDevice: win32more.Windows.Win32.System.Com.IUnknown, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC), ppSwapChain: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGISwapChain)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateSoftwareAdapter(self, Module: win32more.Windows.Win32.Foundation.HMODULE, ppAdapter: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIAdapter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIFactory1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIFactory
    _iid_ = Guid('{770aae78-f26f-4dba-a829-253c83d1b387}')
    @commethod(12)
    def EnumAdapters1(self, Adapter: UInt32, ppAdapter: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIAdapter1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsCurrent(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IDXGIFactory2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIFactory1
    _iid_ = Guid('{50c83a1c-e072-4c48-87b0-3630fa36a6d0}')
    @commethod(14)
    def IsWindowedStereoEnabled(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(15)
    def CreateSwapChainForHwnd(self, pDevice: win32more.Windows.Win32.System.Com.IUnknown, hWnd: win32more.Windows.Win32.Foundation.HWND, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC1), pFullscreenDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FULLSCREEN_DESC), pRestrictToOutput: win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput, ppSwapChain: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGISwapChain1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CreateSwapChainForCoreWindow(self, pDevice: win32more.Windows.Win32.System.Com.IUnknown, pWindow: win32more.Windows.Win32.System.Com.IUnknown, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC1), pRestrictToOutput: win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput, ppSwapChain: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGISwapChain1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetSharedResourceAdapterLuid(self, hResource: win32more.Windows.Win32.Foundation.HANDLE, pLuid: POINTER(win32more.Windows.Win32.Foundation.LUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RegisterStereoStatusWindow(self, WindowHandle: win32more.Windows.Win32.Foundation.HWND, wMsg: UInt32, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def RegisterStereoStatusEvent(self, hEvent: win32more.Windows.Win32.Foundation.HANDLE, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def UnregisterStereoStatus(self, dwCookie: UInt32) -> Void: ...
    @commethod(21)
    def RegisterOcclusionStatusWindow(self, WindowHandle: win32more.Windows.Win32.Foundation.HWND, wMsg: UInt32, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def RegisterOcclusionStatusEvent(self, hEvent: win32more.Windows.Win32.Foundation.HANDLE, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def UnregisterOcclusionStatus(self, dwCookie: UInt32) -> Void: ...
    @commethod(24)
    def CreateSwapChainForComposition(self, pDevice: win32more.Windows.Win32.System.Com.IUnknown, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC1), pRestrictToOutput: win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput, ppSwapChain: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGISwapChain1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIFactory3(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIFactory2
    _iid_ = Guid('{25483823-cd46-4c7d-86ca-47aa95b837bd}')
    @commethod(25)
    def GetCreationFlags(self) -> win32more.Windows.Win32.Graphics.Dxgi.DXGI_CREATE_FACTORY_FLAGS: ...
class IDXGIFactory4(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIFactory3
    _iid_ = Guid('{1bc6ea02-ef36-464f-bf0c-21ca39e5168a}')
    @commethod(26)
    def EnumAdapterByLuid(self, AdapterLuid: win32more.Windows.Win32.Foundation.LUID, riid: POINTER(Guid), ppvAdapter: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def EnumWarpAdapter(self, riid: POINTER(Guid), ppvAdapter: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIFactory5(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIFactory4
    _iid_ = Guid('{7632e1f5-ee65-4dca-87fd-84cd75f8838d}')
    @commethod(28)
    def CheckFeatureSupport(self, Feature: win32more.Windows.Win32.Graphics.Dxgi.DXGI_FEATURE, pFeatureSupportData: VoidPtr, FeatureSupportDataSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIFactory6(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIFactory5
    _iid_ = Guid('{c1b6694f-ff09-44a9-b03c-77900a0a1d17}')
    @commethod(29)
    def EnumAdapterByGpuPreference(self, Adapter: UInt32, GpuPreference: win32more.Windows.Win32.Graphics.Dxgi.DXGI_GPU_PREFERENCE, riid: POINTER(Guid), ppvAdapter: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIFactory7(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIFactory6
    _iid_ = Guid('{a4966eed-76db-44da-84c1-ee9a7afb20a8}')
    @commethod(30)
    def RegisterAdaptersChangedEvent(self, hEvent: win32more.Windows.Win32.Foundation.HANDLE, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def UnregisterAdaptersChangedEvent(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIFactoryMedia(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{41e7d1f2-a591-4f7b-a2e5-fa9c843e1c12}')
    @commethod(3)
    def CreateSwapChainForCompositionSurfaceHandle(self, pDevice: win32more.Windows.Win32.System.Com.IUnknown, hSurface: win32more.Windows.Win32.Foundation.HANDLE, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC1), pRestrictToOutput: win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput, ppSwapChain: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGISwapChain1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateDecodeSwapChainForCompositionSurfaceHandle(self, pDevice: win32more.Windows.Win32.System.Com.IUnknown, hSurface: win32more.Windows.Win32.Foundation.HANDLE, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_DECODE_SWAP_CHAIN_DESC), pYuvDecodeBuffers: win32more.Windows.Win32.Graphics.Dxgi.IDXGIResource, pRestrictToOutput: win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput, ppSwapChain: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIDecodeSwapChain)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIInfoQueue(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d67441c7-672a-476f-9e82-cd55b44949ce}')
    @commethod(3)
    def SetMessageCountLimit(self, Producer: Guid, MessageCountLimit: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ClearStoredMessages(self, Producer: Guid) -> Void: ...
    @commethod(5)
    def GetMessage(self, Producer: Guid, MessageIndex: UInt64, pMessage: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE), pMessageByteLength: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNumStoredMessagesAllowedByRetrievalFilters(self, Producer: Guid) -> UInt64: ...
    @commethod(7)
    def GetNumStoredMessages(self, Producer: Guid) -> UInt64: ...
    @commethod(8)
    def GetNumMessagesDiscardedByMessageCountLimit(self, Producer: Guid) -> UInt64: ...
    @commethod(9)
    def GetMessageCountLimit(self, Producer: Guid) -> UInt64: ...
    @commethod(10)
    def GetNumMessagesAllowedByStorageFilter(self, Producer: Guid) -> UInt64: ...
    @commethod(11)
    def GetNumMessagesDeniedByStorageFilter(self, Producer: Guid) -> UInt64: ...
    @commethod(12)
    def AddStorageFilterEntries(self, Producer: Guid, pFilter: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetStorageFilter(self, Producer: Guid, pFilter: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER), pFilterByteLength: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ClearStorageFilter(self, Producer: Guid) -> Void: ...
    @commethod(15)
    def PushEmptyStorageFilter(self, Producer: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def PushDenyAllStorageFilter(self, Producer: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def PushCopyOfStorageFilter(self, Producer: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def PushStorageFilter(self, Producer: Guid, pFilter: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def PopStorageFilter(self, Producer: Guid) -> Void: ...
    @commethod(20)
    def GetStorageFilterStackSize(self, Producer: Guid) -> UInt32: ...
    @commethod(21)
    def AddRetrievalFilterEntries(self, Producer: Guid, pFilter: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetRetrievalFilter(self, Producer: Guid, pFilter: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER), pFilterByteLength: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def ClearRetrievalFilter(self, Producer: Guid) -> Void: ...
    @commethod(24)
    def PushEmptyRetrievalFilter(self, Producer: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def PushDenyAllRetrievalFilter(self, Producer: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def PushCopyOfRetrievalFilter(self, Producer: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def PushRetrievalFilter(self, Producer: Guid, pFilter: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def PopRetrievalFilter(self, Producer: Guid) -> Void: ...
    @commethod(29)
    def GetRetrievalFilterStackSize(self, Producer: Guid) -> UInt32: ...
    @commethod(30)
    def AddMessage(self, Producer: Guid, Category: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY, Severity: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY, ID: Int32, pDescription: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def AddApplicationMessage(self, Severity: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY, pDescription: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetBreakOnCategory(self, Producer: Guid, Category: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY, bEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetBreakOnSeverity(self, Producer: Guid, Severity: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY, bEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def SetBreakOnID(self, Producer: Guid, ID: Int32, bEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetBreakOnCategory(self, Producer: Guid, Category: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(36)
    def GetBreakOnSeverity(self, Producer: Guid, Severity: win32more.Windows.Win32.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(37)
    def GetBreakOnID(self, Producer: Guid, ID: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(38)
    def SetMuteDebugOutput(self, Producer: Guid, bMute: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
    @commethod(39)
    def GetMuteDebugOutput(self, Producer: Guid) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IDXGIKeyedMutex(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDeviceSubObject
    _iid_ = Guid('{9d8e1289-d7b3-465f-8126-250e349af85d}')
    @commethod(8)
    def AcquireSync(self, Key: UInt64, dwMilliseconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ReleaseSync(self, Key: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aec22fb8-76f3-4639-9be0-28eb43a67a2e}')
    @commethod(3)
    def SetPrivateData(self, Name: POINTER(Guid), DataSize: UInt32, pData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPrivateDataInterface(self, Name: POINTER(Guid), pUnknown: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPrivateData(self, Name: POINTER(Guid), pDataSize: POINTER(UInt32), pData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetParent(self, riid: POINTER(Guid), ppParent: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIOutput(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIObject
    _iid_ = Guid('{ae02eedb-c735-4690-8d52-5a8dc20213aa}')
    @commethod(7)
    def GetDesc(self, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_OUTPUT_DESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDisplayModeList(self, EnumFormat: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT, Flags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ENUM_MODES, pNumModes: POINTER(UInt32), pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_DESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def FindClosestMatchingMode(self, pModeToMatch: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_DESC), pClosestMatch: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_DESC), pConcernedDevice: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def WaitForVBlank(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def TakeOwnership(self, pDevice: win32more.Windows.Win32.System.Com.IUnknown, Exclusive: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ReleaseOwnership(self) -> Void: ...
    @commethod(13)
    def GetGammaControlCapabilities(self, pGammaCaps: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_GAMMA_CONTROL_CAPABILITIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetGammaControl(self, pArray: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_GAMMA_CONTROL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetGammaControl(self, pArray: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_GAMMA_CONTROL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetDisplaySurface(self, pScanoutSurface: win32more.Windows.Win32.Graphics.Dxgi.IDXGISurface) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDisplaySurfaceData(self, pDestination: win32more.Windows.Win32.Graphics.Dxgi.IDXGISurface) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetFrameStatistics(self, pStats: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_FRAME_STATISTICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIOutput1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput
    _iid_ = Guid('{00cddea8-939b-4b83-a340-a685226666cc}')
    @commethod(19)
    def GetDisplayModeList1(self, EnumFormat: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT, Flags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_ENUM_MODES, pNumModes: POINTER(UInt32), pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_MODE_DESC1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def FindClosestMatchingMode1(self, pModeToMatch: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_MODE_DESC1), pClosestMatch: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_MODE_DESC1), pConcernedDevice: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetDisplaySurfaceData1(self, pDestination: win32more.Windows.Win32.Graphics.Dxgi.IDXGIResource) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def DuplicateOutput(self, pDevice: win32more.Windows.Win32.System.Com.IUnknown, ppOutputDuplication: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutputDuplication)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIOutput2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput1
    _iid_ = Guid('{595e39d1-2724-4663-99b1-da969de28364}')
    @commethod(23)
    def SupportsOverlays(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IDXGIOutput3(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput2
    _iid_ = Guid('{8a6bb301-7e7e-41f4-a8e0-5b32f7f99b18}')
    @commethod(24)
    def CheckOverlaySupport(self, EnumFormat: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT, pConcernedDevice: win32more.Windows.Win32.System.Com.IUnknown, pFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIOutput4(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput3
    _iid_ = Guid('{dc7dca35-2196-414d-9f53-617884032a60}')
    @commethod(25)
    def CheckOverlayColorSpaceSupport(self, Format: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT, ColorSpace: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE, pConcernedDevice: win32more.Windows.Win32.System.Com.IUnknown, pFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIOutput5(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput4
    _iid_ = Guid('{80a07424-ab52-42eb-833c-0c42fd282d98}')
    @commethod(26)
    def DuplicateOutput1(self, pDevice: win32more.Windows.Win32.System.Com.IUnknown, Flags: UInt32, SupportedFormatsCount: UInt32, pSupportedFormats: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT), ppOutputDuplication: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutputDuplication)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIOutput6(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput5
    _iid_ = Guid('{068346e8-aaec-4b84-add7-137f513f77a1}')
    @commethod(27)
    def GetDesc1(self, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_OUTPUT_DESC1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def CheckHardwareCompositionSupport(self, pFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIOutputDuplication(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIObject
    _iid_ = Guid('{191cfac3-a341-470d-b26e-a864f428319c}')
    @commethod(7)
    def GetDesc(self, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_OUTDUPL_DESC)) -> Void: ...
    @commethod(8)
    def AcquireNextFrame(self, TimeoutInMilliseconds: UInt32, pFrameInfo: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_OUTDUPL_FRAME_INFO), ppDesktopResource: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIResource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFrameDirtyRects(self, DirtyRectsBufferSize: UInt32, pDirtyRectsBuffer: POINTER(win32more.Windows.Win32.Foundation.RECT), pDirtyRectsBufferSizeRequired: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFrameMoveRects(self, MoveRectsBufferSize: UInt32, pMoveRectBuffer: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_OUTDUPL_MOVE_RECT), pMoveRectsBufferSizeRequired: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFramePointerShape(self, PointerShapeBufferSize: UInt32, pPointerShapeBuffer: VoidPtr, pPointerShapeBufferSizeRequired: POINTER(UInt32), pPointerShapeInfo: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_OUTDUPL_POINTER_SHAPE_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MapDesktopSurface(self, pLockedRect: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_MAPPED_RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def UnMapDesktopSurface(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ReleaseFrame(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIResource(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDeviceSubObject
    _iid_ = Guid('{035f3ab4-482e-4e50-b41f-8a7f8bd8960b}')
    @commethod(8)
    def GetSharedHandle(self, pSharedHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetUsage(self, pUsage: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_USAGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetEvictionPriority(self, EvictionPriority: win32more.Windows.Win32.Graphics.Dxgi.DXGI_RESOURCE_PRIORITY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetEvictionPriority(self, pEvictionPriority: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_RESOURCE_PRIORITY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGIResource1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIResource
    _iid_ = Guid('{30961379-4609-4a41-998e-54fe567ee0c1}')
    @commethod(12)
    def CreateSubresourceSurface(self, index: UInt32, ppSurface: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGISurface2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateSharedHandle(self, pAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), dwAccess: UInt32, lpName: win32more.Windows.Win32.Foundation.PWSTR, pHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGISurface(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDeviceSubObject
    _iid_ = Guid('{cafcb56c-6ac3-4889-bf47-9e23bbd260ec}')
    @commethod(8)
    def GetDesc(self, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_SURFACE_DESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Map(self, pLockedRect: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_MAPPED_RECT), MapFlags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_MAP_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Unmap(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGISurface1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGISurface
    _iid_ = Guid('{4ae63092-6327-4c1b-80ae-bfe12ea32b86}')
    @commethod(11)
    def GetDC(self, Discard: win32more.Windows.Win32.Foundation.BOOL, phdc: POINTER(win32more.Windows.Win32.Graphics.Gdi.HDC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ReleaseDC(self, pDirtyRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGISurface2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGISurface1
    _iid_ = Guid('{aba496dd-b617-4cb8-a866-bc44d7eb1fa2}')
    @commethod(13)
    def GetResource(self, riid: POINTER(Guid), ppParentResource: POINTER(VoidPtr), pSubresourceIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGISwapChain(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGIDeviceSubObject
    _iid_ = Guid('{310d36a0-d2e7-4c0a-aa04-6a9d23b8886a}')
    @commethod(8)
    def Present(self, SyncInterval: UInt32, Flags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_PRESENT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetBuffer(self, Buffer: UInt32, riid: POINTER(Guid), ppSurface: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetFullscreenState(self, Fullscreen: win32more.Windows.Win32.Foundation.BOOL, pTarget: win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFullscreenState(self, pFullscreen: POINTER(win32more.Windows.Win32.Foundation.BOOL), ppTarget: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDesc(self, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ResizeBuffers(self, BufferCount: UInt32, Width: UInt32, Height: UInt32, NewFormat: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT, SwapChainFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ResizeTarget(self, pNewTargetParameters: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_DESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetContainingOutput(self, ppOutput: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetFrameStatistics(self, pStats: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_FRAME_STATISTICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetLastPresentCount(self, pLastPresentCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGISwapChain1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGISwapChain
    _iid_ = Guid('{790a45f7-0d42-4876-983a-0a55cfe6f4aa}')
    @commethod(18)
    def GetDesc1(self, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetFullscreenDesc(self, pDesc: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_SWAP_CHAIN_FULLSCREEN_DESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetHwnd(self, pHwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetCoreWindow(self, refiid: POINTER(Guid), ppUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Present1(self, SyncInterval: UInt32, PresentFlags: win32more.Windows.Win32.Graphics.Dxgi.DXGI_PRESENT, pPresentParameters: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_PRESENT_PARAMETERS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def IsTemporaryMonoSupported(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(24)
    def GetRestrictToOutput(self, ppRestrictToOutput: POINTER(win32more.Windows.Win32.Graphics.Dxgi.IDXGIOutput)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetBackgroundColor(self, pColor: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_RGBA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetBackgroundColor(self, pColor: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_RGBA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetRotation(self, Rotation: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetRotation(self, pRotation: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGISwapChain2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGISwapChain1
    _iid_ = Guid('{a8be2ac4-199f-4946-b331-79599fb98de7}')
    @commethod(29)
    def SetSourceSize(self, Width: UInt32, Height: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetSourceSize(self, pWidth: POINTER(UInt32), pHeight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetMaximumFrameLatency(self, MaxLatency: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetMaximumFrameLatency(self, pMaxLatency: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetFrameLatencyWaitableObject(self) -> win32more.Windows.Win32.Foundation.HANDLE: ...
    @commethod(34)
    def SetMatrixTransform(self, pMatrix: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_MATRIX_3X2_F)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetMatrixTransform(self, pMatrix: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_MATRIX_3X2_F)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGISwapChain3(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGISwapChain2
    _iid_ = Guid('{94d99bdb-f1f8-4ab0-b236-7da0170edab1}')
    @commethod(36)
    def GetCurrentBackBufferIndex(self) -> UInt32: ...
    @commethod(37)
    def CheckColorSpaceSupport(self, ColorSpace: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE, pColorSpaceSupport: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SetColorSpace1(self, ColorSpace: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def ResizeBuffers1(self, BufferCount: UInt32, Width: UInt32, Height: UInt32, Format: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT, SwapChainFlags: UInt32, pCreationNodeMask: POINTER(UInt32), ppPresentQueue: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGISwapChain4(ComPtr):
    extends: win32more.Windows.Win32.Graphics.Dxgi.IDXGISwapChain3
    _iid_ = Guid('{3d585d5a-bd4a-489e-b1f4-3dbcb6452ffb}')
    @commethod(40)
    def SetHDRMetaData(self, Type: win32more.Windows.Win32.Graphics.Dxgi.DXGI_HDR_METADATA_TYPE, Size: UInt32, pMetaData: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGISwapChainMedia(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dd95b90b-f05f-4f6a-bd65-25bfb264bd84}')
    @commethod(3)
    def GetFrameStatisticsMedia(self, pStats: POINTER(win32more.Windows.Win32.Graphics.Dxgi.DXGI_FRAME_STATISTICS_MEDIA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPresentDuration(self, Duration: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CheckPresentDurationSupport(self, DesiredPresentDuration: UInt32, pClosestSmallerPresentDuration: POINTER(UInt32), pClosestLargerPresentDuration: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDXGraphicsAnalysis(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f251514-9d4d-4902-9d60-18988ab7d4b5}')
    @commethod(3)
    def BeginCapture(self) -> Void: ...
    @commethod(4)
    def EndCapture(self) -> Void: ...


make_ready(__name__)
