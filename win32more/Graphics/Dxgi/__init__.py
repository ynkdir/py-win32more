from win32more import *
import win32more.Graphics.Dxgi
import win32more.Foundation
import win32more.Graphics.Dxgi.Common
import win32more.Graphics.Gdi
import win32more.Security
import win32more.System.Com

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Graphics.Dxgi, name, eval(f"_define_{name}()"))
    return getattr(win32more.Graphics.Dxgi, name)
DXGI_USAGE_SHADER_INPUT = 16
DXGI_USAGE_RENDER_TARGET_OUTPUT = 32
DXGI_USAGE_BACK_BUFFER = 64
DXGI_USAGE_SHARED = 128
DXGI_USAGE_READ_ONLY = 256
DXGI_USAGE_DISCARD_ON_PRESENT = 512
DXGI_USAGE_UNORDERED_ACCESS = 1024
DXGI_MAP_READ = 1
DXGI_MAP_WRITE = 2
DXGI_MAP_DISCARD = 4
DXGI_ENUM_MODES_INTERLACED = 1
DXGI_ENUM_MODES_SCALING = 2
DXGI_MAX_SWAP_CHAIN_BUFFERS = 16
DXGI_PRESENT_TEST = 1
DXGI_PRESENT_DO_NOT_SEQUENCE = 2
DXGI_PRESENT_RESTART = 4
DXGI_PRESENT_DO_NOT_WAIT = 8
DXGI_PRESENT_STEREO_PREFER_RIGHT = 16
DXGI_PRESENT_STEREO_TEMPORARY_MONO = 32
DXGI_PRESENT_RESTRICT_TO_OUTPUT = 64
DXGI_PRESENT_USE_DURATION = 256
DXGI_PRESENT_ALLOW_TEARING = 512
DXGI_MWA_NO_WINDOW_CHANGES = 1
DXGI_MWA_NO_ALT_ENTER = 2
DXGI_MWA_NO_PRINT_SCREEN = 4
DXGI_MWA_VALID = 7
DXGI_ENUM_MODES_STEREO = 4
DXGI_ENUM_MODES_DISABLED_STEREO = 8
DXGI_SHARED_RESOURCE_READ = 2147483648
DXGI_SHARED_RESOURCE_WRITE = 1
DXGI_DEBUG_BINARY_VERSION = 1
DXGI_DEBUG_ALL = 'e48ae283-da80-490b-87e6-43e9a9cfda08'
DXGI_DEBUG_DX = '35cdd7fc-13b2-421d-a5d7-7e4451287d64'
DXGI_DEBUG_DXGI = '25cddaa4-b1c6-47e1-ac3e-98875b5a2e2a'
DXGI_DEBUG_APP = '06cd6e01-4219-4ebd-8709-27ed23360c62'
DXGI_INFO_QUEUE_MESSAGE_ID_STRING_FROM_APPLICATION = 0
DXGI_INFO_QUEUE_DEFAULT_MESSAGE_COUNT_LIMIT = 1024
DXGI_CREATE_FACTORY_DEBUG = 1
DXGI_ERROR_INVALID_CALL = -2005270527
DXGI_ERROR_NOT_FOUND = -2005270526
DXGI_ERROR_MORE_DATA = -2005270525
DXGI_ERROR_UNSUPPORTED = -2005270524
DXGI_ERROR_DEVICE_REMOVED = -2005270523
DXGI_ERROR_DEVICE_HUNG = -2005270522
DXGI_ERROR_DEVICE_RESET = -2005270521
DXGI_ERROR_WAS_STILL_DRAWING = -2005270518
DXGI_ERROR_FRAME_STATISTICS_DISJOINT = -2005270517
DXGI_ERROR_GRAPHICS_VIDPN_SOURCE_IN_USE = -2005270516
DXGI_ERROR_DRIVER_INTERNAL_ERROR = -2005270496
DXGI_ERROR_NONEXCLUSIVE = -2005270495
DXGI_ERROR_NOT_CURRENTLY_AVAILABLE = -2005270494
DXGI_ERROR_REMOTE_CLIENT_DISCONNECTED = -2005270493
DXGI_ERROR_REMOTE_OUTOFMEMORY = -2005270492
DXGI_ERROR_ACCESS_LOST = -2005270490
DXGI_ERROR_WAIT_TIMEOUT = -2005270489
DXGI_ERROR_SESSION_DISCONNECTED = -2005270488
DXGI_ERROR_RESTRICT_TO_OUTPUT_STALE = -2005270487
DXGI_ERROR_CANNOT_PROTECT_CONTENT = -2005270486
DXGI_ERROR_ACCESS_DENIED = -2005270485
DXGI_ERROR_NAME_ALREADY_EXISTS = -2005270484
DXGI_ERROR_SDK_COMPONENT_MISSING = -2005270483
DXGI_ERROR_NOT_CURRENT = -2005270482
DXGI_ERROR_HW_PROTECTION_OUTOFMEMORY = -2005270480
DXGI_ERROR_DYNAMIC_CODE_POLICY_VIOLATION = -2005270479
DXGI_ERROR_NON_COMPOSITED_UI = -2005270478
DXGI_ERROR_MODE_CHANGE_IN_PROGRESS = -2005270491
DXGI_ERROR_CACHE_CORRUPT = -2005270477
DXGI_ERROR_CACHE_FULL = -2005270476
DXGI_ERROR_CACHE_HASH_COLLISION = -2005270475
DXGI_ERROR_ALREADY_EXISTS = -2005270474
def _define_DXGI_RGBA_head():
    class DXGI_RGBA(Structure):
        pass
    return DXGI_RGBA
def _define_DXGI_RGBA():
    DXGI_RGBA = win32more.Graphics.Dxgi.DXGI_RGBA_head
    DXGI_RGBA._fields_ = [
        ("r", Single),
        ("g", Single),
        ("b", Single),
        ("a", Single),
    ]
    return DXGI_RGBA
DXGI_RESOURCE_PRIORITY = UInt32
DXGI_RESOURCE_PRIORITY_MINIMUM = 671088640
DXGI_RESOURCE_PRIORITY_LOW = 1342177280
DXGI_RESOURCE_PRIORITY_NORMAL = 2013265920
DXGI_RESOURCE_PRIORITY_HIGH = 2684354560
DXGI_RESOURCE_PRIORITY_MAXIMUM = 3355443200
def _define_DXGI_FRAME_STATISTICS_head():
    class DXGI_FRAME_STATISTICS(Structure):
        pass
    return DXGI_FRAME_STATISTICS
def _define_DXGI_FRAME_STATISTICS():
    DXGI_FRAME_STATISTICS = win32more.Graphics.Dxgi.DXGI_FRAME_STATISTICS_head
    DXGI_FRAME_STATISTICS._fields_ = [
        ("PresentCount", UInt32),
        ("PresentRefreshCount", UInt32),
        ("SyncRefreshCount", UInt32),
        ("SyncQPCTime", win32more.Foundation.LARGE_INTEGER),
        ("SyncGPUTime", win32more.Foundation.LARGE_INTEGER),
    ]
    return DXGI_FRAME_STATISTICS
def _define_DXGI_MAPPED_RECT_head():
    class DXGI_MAPPED_RECT(Structure):
        pass
    return DXGI_MAPPED_RECT
def _define_DXGI_MAPPED_RECT():
    DXGI_MAPPED_RECT = win32more.Graphics.Dxgi.DXGI_MAPPED_RECT_head
    DXGI_MAPPED_RECT._fields_ = [
        ("Pitch", Int32),
        ("pBits", c_char_p_no),
    ]
    return DXGI_MAPPED_RECT
def _define_DXGI_ADAPTER_DESC_head():
    class DXGI_ADAPTER_DESC(Structure):
        pass
    return DXGI_ADAPTER_DESC
def _define_DXGI_ADAPTER_DESC():
    DXGI_ADAPTER_DESC = win32more.Graphics.Dxgi.DXGI_ADAPTER_DESC_head
    DXGI_ADAPTER_DESC._fields_ = [
        ("Description", Char * 128),
        ("VendorId", UInt32),
        ("DeviceId", UInt32),
        ("SubSysId", UInt32),
        ("Revision", UInt32),
        ("DedicatedVideoMemory", UIntPtr),
        ("DedicatedSystemMemory", UIntPtr),
        ("SharedSystemMemory", UIntPtr),
        ("AdapterLuid", win32more.Foundation.LUID),
    ]
    return DXGI_ADAPTER_DESC
def _define_DXGI_OUTPUT_DESC_head():
    class DXGI_OUTPUT_DESC(Structure):
        pass
    return DXGI_OUTPUT_DESC
def _define_DXGI_OUTPUT_DESC():
    DXGI_OUTPUT_DESC = win32more.Graphics.Dxgi.DXGI_OUTPUT_DESC_head
    DXGI_OUTPUT_DESC._fields_ = [
        ("DeviceName", Char * 32),
        ("DesktopCoordinates", win32more.Foundation.RECT),
        ("AttachedToDesktop", win32more.Foundation.BOOL),
        ("Rotation", win32more.Graphics.Dxgi.Common.DXGI_MODE_ROTATION),
        ("Monitor", win32more.Graphics.Gdi.HMONITOR),
    ]
    return DXGI_OUTPUT_DESC
def _define_DXGI_SHARED_RESOURCE_head():
    class DXGI_SHARED_RESOURCE(Structure):
        pass
    return DXGI_SHARED_RESOURCE
def _define_DXGI_SHARED_RESOURCE():
    DXGI_SHARED_RESOURCE = win32more.Graphics.Dxgi.DXGI_SHARED_RESOURCE_head
    DXGI_SHARED_RESOURCE._fields_ = [
        ("Handle", win32more.Foundation.HANDLE),
    ]
    return DXGI_SHARED_RESOURCE
DXGI_RESIDENCY = Int32
DXGI_RESIDENCY_FULLY_RESIDENT = 1
DXGI_RESIDENCY_RESIDENT_IN_SHARED_MEMORY = 2
DXGI_RESIDENCY_EVICTED_TO_DISK = 3
def _define_DXGI_SURFACE_DESC_head():
    class DXGI_SURFACE_DESC(Structure):
        pass
    return DXGI_SURFACE_DESC
def _define_DXGI_SURFACE_DESC():
    DXGI_SURFACE_DESC = win32more.Graphics.Dxgi.DXGI_SURFACE_DESC_head
    DXGI_SURFACE_DESC._fields_ = [
        ("Width", UInt32),
        ("Height", UInt32),
        ("Format", win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ("SampleDesc", win32more.Graphics.Dxgi.Common.DXGI_SAMPLE_DESC),
    ]
    return DXGI_SURFACE_DESC
DXGI_SWAP_EFFECT = Int32
DXGI_SWAP_EFFECT_DISCARD = 0
DXGI_SWAP_EFFECT_SEQUENTIAL = 1
DXGI_SWAP_EFFECT_FLIP_SEQUENTIAL = 3
DXGI_SWAP_EFFECT_FLIP_DISCARD = 4
DXGI_SWAP_CHAIN_FLAG = Int32
DXGI_SWAP_CHAIN_FLAG_NONPREROTATED = 1
DXGI_SWAP_CHAIN_FLAG_ALLOW_MODE_SWITCH = 2
DXGI_SWAP_CHAIN_FLAG_GDI_COMPATIBLE = 4
DXGI_SWAP_CHAIN_FLAG_RESTRICTED_CONTENT = 8
DXGI_SWAP_CHAIN_FLAG_RESTRICT_SHARED_RESOURCE_DRIVER = 16
DXGI_SWAP_CHAIN_FLAG_DISPLAY_ONLY = 32
DXGI_SWAP_CHAIN_FLAG_FRAME_LATENCY_WAITABLE_OBJECT = 64
DXGI_SWAP_CHAIN_FLAG_FOREGROUND_LAYER = 128
DXGI_SWAP_CHAIN_FLAG_FULLSCREEN_VIDEO = 256
DXGI_SWAP_CHAIN_FLAG_YUV_VIDEO = 512
DXGI_SWAP_CHAIN_FLAG_HW_PROTECTED = 1024
DXGI_SWAP_CHAIN_FLAG_ALLOW_TEARING = 2048
DXGI_SWAP_CHAIN_FLAG_RESTRICTED_TO_ALL_HOLOGRAPHIC_DISPLAYS = 4096
def _define_DXGI_SWAP_CHAIN_DESC_head():
    class DXGI_SWAP_CHAIN_DESC(Structure):
        pass
    return DXGI_SWAP_CHAIN_DESC
def _define_DXGI_SWAP_CHAIN_DESC():
    DXGI_SWAP_CHAIN_DESC = win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC_head
    DXGI_SWAP_CHAIN_DESC._fields_ = [
        ("BufferDesc", win32more.Graphics.Dxgi.Common.DXGI_MODE_DESC),
        ("SampleDesc", win32more.Graphics.Dxgi.Common.DXGI_SAMPLE_DESC),
        ("BufferUsage", UInt32),
        ("BufferCount", UInt32),
        ("OutputWindow", win32more.Foundation.HWND),
        ("Windowed", win32more.Foundation.BOOL),
        ("SwapEffect", win32more.Graphics.Dxgi.DXGI_SWAP_EFFECT),
        ("Flags", UInt32),
    ]
    return DXGI_SWAP_CHAIN_DESC
def _define_IDXGIObject_head():
    class IDXGIObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('aec22fb8-76f3-4639-9be0-28eb43a67a2e')
    return IDXGIObject
def _define_IDXGIObject():
    IDXGIObject = win32more.Graphics.Dxgi.IDXGIObject_head
    IDXGIObject.SetPrivateData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,c_void_p, use_last_error=False)(3, 'SetPrivateData', ((1, 'Name'),(1, 'DataSize'),(1, 'pData'),)))
    IDXGIObject.SetPrivateDataInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head, use_last_error=False)(4, 'SetPrivateDataInterface', ((1, 'Name'),(1, 'pUnknown'),)))
    IDXGIObject.GetPrivateData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32),c_void_p, use_last_error=False)(5, 'GetPrivateData', ((1, 'Name'),(1, 'pDataSize'),(1, 'pData'),)))
    IDXGIObject.GetParent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetParent', ((1, 'riid'),(1, 'ppParent'),)))
    return IDXGIObject
def _define_IDXGIDeviceSubObject_head():
    class IDXGIDeviceSubObject(win32more.Graphics.Dxgi.IDXGIObject_head):
        Guid = Guid('3d3e0379-f9de-4d58-bb6c-18d62992f1a6')
    return IDXGIDeviceSubObject
def _define_IDXGIDeviceSubObject():
    IDXGIDeviceSubObject = win32more.Graphics.Dxgi.IDXGIDeviceSubObject_head
    IDXGIDeviceSubObject.GetDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(7, 'GetDevice', ((1, 'riid'),(1, 'ppDevice'),)))
    return IDXGIDeviceSubObject
def _define_IDXGIResource_head():
    class IDXGIResource(win32more.Graphics.Dxgi.IDXGIDeviceSubObject_head):
        Guid = Guid('035f3ab4-482e-4e50-b41f-8a7f8bd8960b')
    return IDXGIResource
def _define_IDXGIResource():
    IDXGIResource = win32more.Graphics.Dxgi.IDXGIResource_head
    IDXGIResource.GetSharedHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(8, 'GetSharedHandle', ((1, 'pSharedHandle'),)))
    IDXGIResource.GetUsage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetUsage', ((1, 'pUsage'),)))
    IDXGIResource.SetEvictionPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.DXGI_RESOURCE_PRIORITY, use_last_error=False)(10, 'SetEvictionPriority', ((1, 'EvictionPriority'),)))
    IDXGIResource.GetEvictionPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'GetEvictionPriority', ((1, 'pEvictionPriority'),)))
    return IDXGIResource
def _define_IDXGIKeyedMutex_head():
    class IDXGIKeyedMutex(win32more.Graphics.Dxgi.IDXGIDeviceSubObject_head):
        Guid = Guid('9d8e1289-d7b3-465f-8126-250e349af85d')
    return IDXGIKeyedMutex
def _define_IDXGIKeyedMutex():
    IDXGIKeyedMutex = win32more.Graphics.Dxgi.IDXGIKeyedMutex_head
    IDXGIKeyedMutex.AcquireSync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt32, use_last_error=False)(8, 'AcquireSync', ((1, 'Key'),(1, 'dwMilliseconds'),)))
    IDXGIKeyedMutex.ReleaseSync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(9, 'ReleaseSync', ((1, 'Key'),)))
    return IDXGIKeyedMutex
def _define_IDXGISurface_head():
    class IDXGISurface(win32more.Graphics.Dxgi.IDXGIDeviceSubObject_head):
        Guid = Guid('cafcb56c-6ac3-4889-bf47-9e23bbd260ec')
    return IDXGISurface
def _define_IDXGISurface():
    IDXGISurface = win32more.Graphics.Dxgi.IDXGISurface_head
    IDXGISurface.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_SURFACE_DESC_head), use_last_error=False)(8, 'GetDesc', ((1, 'pDesc'),)))
    IDXGISurface.Map = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_MAPPED_RECT_head),UInt32, use_last_error=False)(9, 'Map', ((1, 'pLockedRect'),(1, 'MapFlags'),)))
    IDXGISurface.Unmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'Unmap', ()))
    return IDXGISurface
def _define_IDXGISurface1_head():
    class IDXGISurface1(win32more.Graphics.Dxgi.IDXGISurface_head):
        Guid = Guid('4ae63092-6327-4c1b-80ae-bfe12ea32b86')
    return IDXGISurface1
def _define_IDXGISurface1():
    IDXGISurface1 = win32more.Graphics.Dxgi.IDXGISurface1_head
    IDXGISurface1.GetDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(win32more.Graphics.Gdi.HDC), use_last_error=False)(11, 'GetDC', ((1, 'Discard'),(1, 'phdc'),)))
    IDXGISurface1.ReleaseDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(12, 'ReleaseDC', ((1, 'pDirtyRect'),)))
    return IDXGISurface1
def _define_IDXGIAdapter_head():
    class IDXGIAdapter(win32more.Graphics.Dxgi.IDXGIObject_head):
        Guid = Guid('2411e7e1-12ac-4ccf-bd14-9798e8534dc0')
    return IDXGIAdapter
def _define_IDXGIAdapter():
    IDXGIAdapter = win32more.Graphics.Dxgi.IDXGIAdapter_head
    IDXGIAdapter.EnumOutputs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Dxgi.IDXGIOutput_head), use_last_error=False)(7, 'EnumOutputs', ((1, 'Output'),(1, 'ppOutput'),)))
    IDXGIAdapter.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_ADAPTER_DESC_head), use_last_error=False)(8, 'GetDesc', ((1, 'pDesc'),)))
    IDXGIAdapter.CheckInterfaceSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.LARGE_INTEGER_head), use_last_error=False)(9, 'CheckInterfaceSupport', ((1, 'InterfaceName'),(1, 'pUMDVersion'),)))
    return IDXGIAdapter
def _define_IDXGIOutput_head():
    class IDXGIOutput(win32more.Graphics.Dxgi.IDXGIObject_head):
        Guid = Guid('ae02eedb-c735-4690-8d52-5a8dc20213aa')
    return IDXGIOutput
def _define_IDXGIOutput():
    IDXGIOutput = win32more.Graphics.Dxgi.IDXGIOutput_head
    IDXGIOutput.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_OUTPUT_DESC_head), use_last_error=False)(7, 'GetDesc', ((1, 'pDesc'),)))
    IDXGIOutput.GetDisplayModeList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,UInt32,POINTER(UInt32),POINTER(win32more.Graphics.Dxgi.Common.DXGI_MODE_DESC), use_last_error=False)(8, 'GetDisplayModeList', ((1, 'EnumFormat'),(1, 'Flags'),(1, 'pNumModes'),(1, 'pDesc'),)))
    IDXGIOutput.FindClosestMatchingMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.Common.DXGI_MODE_DESC_head),POINTER(win32more.Graphics.Dxgi.Common.DXGI_MODE_DESC_head),win32more.System.Com.IUnknown_head, use_last_error=False)(9, 'FindClosestMatchingMode', ((1, 'pModeToMatch'),(1, 'pClosestMatch'),(1, 'pConcernedDevice'),)))
    IDXGIOutput.WaitForVBlank = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'WaitForVBlank', ()))
    IDXGIOutput.TakeOwnership = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL, use_last_error=False)(11, 'TakeOwnership', ((1, 'pDevice'),(1, 'Exclusive'),)))
    IDXGIOutput.ReleaseOwnership = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(12, 'ReleaseOwnership', ()))
    IDXGIOutput.GetGammaControlCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.Common.DXGI_GAMMA_CONTROL_CAPABILITIES_head), use_last_error=False)(13, 'GetGammaControlCapabilities', ((1, 'pGammaCaps'),)))
    IDXGIOutput.SetGammaControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.Common.DXGI_GAMMA_CONTROL_head), use_last_error=False)(14, 'SetGammaControl', ((1, 'pArray'),)))
    IDXGIOutput.GetGammaControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.Common.DXGI_GAMMA_CONTROL_head), use_last_error=False)(15, 'GetGammaControl', ((1, 'pArray'),)))
    IDXGIOutput.SetDisplaySurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGISurface_head, use_last_error=False)(16, 'SetDisplaySurface', ((1, 'pScanoutSurface'),)))
    IDXGIOutput.GetDisplaySurfaceData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGISurface_head, use_last_error=False)(17, 'GetDisplaySurfaceData', ((1, 'pDestination'),)))
    IDXGIOutput.GetFrameStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_FRAME_STATISTICS_head), use_last_error=False)(18, 'GetFrameStatistics', ((1, 'pStats'),)))
    return IDXGIOutput
def _define_IDXGISwapChain_head():
    class IDXGISwapChain(win32more.Graphics.Dxgi.IDXGIDeviceSubObject_head):
        Guid = Guid('310d36a0-d2e7-4c0a-aa04-6a9d23b8886a')
    return IDXGISwapChain
def _define_IDXGISwapChain():
    IDXGISwapChain = win32more.Graphics.Dxgi.IDXGISwapChain_head
    IDXGISwapChain.Present = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(8, 'Present', ((1, 'SyncInterval'),(1, 'Flags'),)))
    IDXGISwapChain.GetBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(9, 'GetBuffer', ((1, 'Buffer'),(1, 'riid'),(1, 'ppSurface'),)))
    IDXGISwapChain.SetFullscreenState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Graphics.Dxgi.IDXGIOutput_head, use_last_error=False)(10, 'SetFullscreenState', ((1, 'Fullscreen'),(1, 'pTarget'),)))
    IDXGISwapChain.GetFullscreenState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Graphics.Dxgi.IDXGIOutput_head), use_last_error=False)(11, 'GetFullscreenState', ((1, 'pFullscreen'),(1, 'ppTarget'),)))
    IDXGISwapChain.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC_head), use_last_error=False)(12, 'GetDesc', ((1, 'pDesc'),)))
    IDXGISwapChain.ResizeBuffers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,UInt32, use_last_error=False)(13, 'ResizeBuffers', ((1, 'BufferCount'),(1, 'Width'),(1, 'Height'),(1, 'NewFormat'),(1, 'SwapChainFlags'),)))
    IDXGISwapChain.ResizeTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.Common.DXGI_MODE_DESC_head), use_last_error=False)(14, 'ResizeTarget', ((1, 'pNewTargetParameters'),)))
    IDXGISwapChain.GetContainingOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.IDXGIOutput_head), use_last_error=False)(15, 'GetContainingOutput', ((1, 'ppOutput'),)))
    IDXGISwapChain.GetFrameStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_FRAME_STATISTICS_head), use_last_error=False)(16, 'GetFrameStatistics', ((1, 'pStats'),)))
    IDXGISwapChain.GetLastPresentCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(17, 'GetLastPresentCount', ((1, 'pLastPresentCount'),)))
    return IDXGISwapChain
def _define_IDXGIFactory_head():
    class IDXGIFactory(win32more.Graphics.Dxgi.IDXGIObject_head):
        Guid = Guid('7b7166ec-21c7-44ae-b21a-c9ae321ae369')
    return IDXGIFactory
def _define_IDXGIFactory():
    IDXGIFactory = win32more.Graphics.Dxgi.IDXGIFactory_head
    IDXGIFactory.EnumAdapters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Dxgi.IDXGIAdapter_head), use_last_error=False)(7, 'EnumAdapters', ((1, 'Adapter'),(1, 'ppAdapter'),)))
    IDXGIFactory.MakeWindowAssociation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32, use_last_error=False)(8, 'MakeWindowAssociation', ((1, 'WindowHandle'),(1, 'Flags'),)))
    IDXGIFactory.GetWindowAssociation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND), use_last_error=False)(9, 'GetWindowAssociation', ((1, 'pWindowHandle'),)))
    IDXGIFactory.CreateSwapChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC_head),POINTER(win32more.Graphics.Dxgi.IDXGISwapChain_head), use_last_error=False)(10, 'CreateSwapChain', ((1, 'pDevice'),(1, 'pDesc'),(1, 'ppSwapChain'),)))
    IDXGIFactory.CreateSoftwareAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,POINTER(win32more.Graphics.Dxgi.IDXGIAdapter_head), use_last_error=False)(11, 'CreateSoftwareAdapter', ((1, 'Module'),(1, 'ppAdapter'),)))
    return IDXGIFactory
def _define_IDXGIDevice_head():
    class IDXGIDevice(win32more.Graphics.Dxgi.IDXGIObject_head):
        Guid = Guid('54ec77fa-1377-44e6-8c32-88fd5f44c84c')
    return IDXGIDevice
def _define_IDXGIDevice():
    IDXGIDevice = win32more.Graphics.Dxgi.IDXGIDevice_head
    IDXGIDevice.GetAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.IDXGIAdapter_head), use_last_error=False)(7, 'GetAdapter', ((1, 'pAdapter'),)))
    IDXGIDevice.CreateSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_SURFACE_DESC_head),UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.DXGI_SHARED_RESOURCE_head),POINTER(win32more.Graphics.Dxgi.IDXGISurface_head), use_last_error=False)(8, 'CreateSurface', ((1, 'pDesc'),(1, 'NumSurfaces'),(1, 'Usage'),(1, 'pSharedResource'),(1, 'ppSurface'),)))
    IDXGIDevice.QueryResourceResidency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head),POINTER(win32more.Graphics.Dxgi.DXGI_RESIDENCY),UInt32, use_last_error=False)(9, 'QueryResourceResidency', ((1, 'ppResources'),(1, 'pResidencyStatus'),(1, 'NumResources'),)))
    IDXGIDevice.SetGPUThreadPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'SetGPUThreadPriority', ((1, 'Priority'),)))
    IDXGIDevice.GetGPUThreadPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'GetGPUThreadPriority', ((1, 'pPriority'),)))
    return IDXGIDevice
DXGI_ADAPTER_FLAG = UInt32
DXGI_ADAPTER_FLAG_NONE = 0
DXGI_ADAPTER_FLAG_REMOTE = 1
DXGI_ADAPTER_FLAG_SOFTWARE = 2
def _define_DXGI_ADAPTER_DESC1_head():
    class DXGI_ADAPTER_DESC1(Structure):
        pass
    return DXGI_ADAPTER_DESC1
def _define_DXGI_ADAPTER_DESC1():
    DXGI_ADAPTER_DESC1 = win32more.Graphics.Dxgi.DXGI_ADAPTER_DESC1_head
    DXGI_ADAPTER_DESC1._fields_ = [
        ("Description", Char * 128),
        ("VendorId", UInt32),
        ("DeviceId", UInt32),
        ("SubSysId", UInt32),
        ("Revision", UInt32),
        ("DedicatedVideoMemory", UIntPtr),
        ("DedicatedSystemMemory", UIntPtr),
        ("SharedSystemMemory", UIntPtr),
        ("AdapterLuid", win32more.Foundation.LUID),
        ("Flags", UInt32),
    ]
    return DXGI_ADAPTER_DESC1
def _define_DXGI_DISPLAY_COLOR_SPACE_head():
    class DXGI_DISPLAY_COLOR_SPACE(Structure):
        pass
    return DXGI_DISPLAY_COLOR_SPACE
def _define_DXGI_DISPLAY_COLOR_SPACE():
    DXGI_DISPLAY_COLOR_SPACE = win32more.Graphics.Dxgi.DXGI_DISPLAY_COLOR_SPACE_head
    DXGI_DISPLAY_COLOR_SPACE._fields_ = [
        ("PrimaryCoordinates", Single * 16),
        ("WhitePoints", Single * 32),
    ]
    return DXGI_DISPLAY_COLOR_SPACE
def _define_IDXGIFactory1_head():
    class IDXGIFactory1(win32more.Graphics.Dxgi.IDXGIFactory_head):
        Guid = Guid('770aae78-f26f-4dba-a829-253c83d1b387')
    return IDXGIFactory1
def _define_IDXGIFactory1():
    IDXGIFactory1 = win32more.Graphics.Dxgi.IDXGIFactory1_head
    IDXGIFactory1.EnumAdapters1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Dxgi.IDXGIAdapter1_head), use_last_error=False)(12, 'EnumAdapters1', ((1, 'Adapter'),(1, 'ppAdapter'),)))
    IDXGIFactory1.IsCurrent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(13, 'IsCurrent', ()))
    return IDXGIFactory1
def _define_IDXGIAdapter1_head():
    class IDXGIAdapter1(win32more.Graphics.Dxgi.IDXGIAdapter_head):
        Guid = Guid('29038f61-3839-4626-91fd-086879011a05')
    return IDXGIAdapter1
def _define_IDXGIAdapter1():
    IDXGIAdapter1 = win32more.Graphics.Dxgi.IDXGIAdapter1_head
    IDXGIAdapter1.GetDesc1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_ADAPTER_DESC1_head), use_last_error=False)(10, 'GetDesc1', ((1, 'pDesc'),)))
    return IDXGIAdapter1
def _define_IDXGIDevice1_head():
    class IDXGIDevice1(win32more.Graphics.Dxgi.IDXGIDevice_head):
        Guid = Guid('77db970f-6276-48ba-ba28-070143b4392c')
    return IDXGIDevice1
def _define_IDXGIDevice1():
    IDXGIDevice1 = win32more.Graphics.Dxgi.IDXGIDevice1_head
    IDXGIDevice1.SetMaximumFrameLatency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(12, 'SetMaximumFrameLatency', ((1, 'MaxLatency'),)))
    IDXGIDevice1.GetMaximumFrameLatency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(13, 'GetMaximumFrameLatency', ((1, 'pMaxLatency'),)))
    return IDXGIDevice1
def _define_IDXGIDisplayControl_head():
    class IDXGIDisplayControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('ea9dbf1a-c88e-4486-854a-98aa0138f30c')
    return IDXGIDisplayControl
def _define_IDXGIDisplayControl():
    IDXGIDisplayControl = win32more.Graphics.Dxgi.IDXGIDisplayControl_head
    IDXGIDisplayControl.IsStereoEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(3, 'IsStereoEnabled', ()))
    IDXGIDisplayControl.SetStereoEnabled = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.BOOL, use_last_error=False)(4, 'SetStereoEnabled', ((1, 'enabled'),)))
    return IDXGIDisplayControl
def _define_DXGI_OUTDUPL_MOVE_RECT_head():
    class DXGI_OUTDUPL_MOVE_RECT(Structure):
        pass
    return DXGI_OUTDUPL_MOVE_RECT
def _define_DXGI_OUTDUPL_MOVE_RECT():
    DXGI_OUTDUPL_MOVE_RECT = win32more.Graphics.Dxgi.DXGI_OUTDUPL_MOVE_RECT_head
    DXGI_OUTDUPL_MOVE_RECT._fields_ = [
        ("SourcePoint", win32more.Foundation.POINT),
        ("DestinationRect", win32more.Foundation.RECT),
    ]
    return DXGI_OUTDUPL_MOVE_RECT
def _define_DXGI_OUTDUPL_DESC_head():
    class DXGI_OUTDUPL_DESC(Structure):
        pass
    return DXGI_OUTDUPL_DESC
def _define_DXGI_OUTDUPL_DESC():
    DXGI_OUTDUPL_DESC = win32more.Graphics.Dxgi.DXGI_OUTDUPL_DESC_head
    DXGI_OUTDUPL_DESC._fields_ = [
        ("ModeDesc", win32more.Graphics.Dxgi.Common.DXGI_MODE_DESC),
        ("Rotation", win32more.Graphics.Dxgi.Common.DXGI_MODE_ROTATION),
        ("DesktopImageInSystemMemory", win32more.Foundation.BOOL),
    ]
    return DXGI_OUTDUPL_DESC
def _define_DXGI_OUTDUPL_POINTER_POSITION_head():
    class DXGI_OUTDUPL_POINTER_POSITION(Structure):
        pass
    return DXGI_OUTDUPL_POINTER_POSITION
def _define_DXGI_OUTDUPL_POINTER_POSITION():
    DXGI_OUTDUPL_POINTER_POSITION = win32more.Graphics.Dxgi.DXGI_OUTDUPL_POINTER_POSITION_head
    DXGI_OUTDUPL_POINTER_POSITION._fields_ = [
        ("Position", win32more.Foundation.POINT),
        ("Visible", win32more.Foundation.BOOL),
    ]
    return DXGI_OUTDUPL_POINTER_POSITION
DXGI_OUTDUPL_POINTER_SHAPE_TYPE = Int32
DXGI_OUTDUPL_POINTER_SHAPE_TYPE_MONOCHROME = 1
DXGI_OUTDUPL_POINTER_SHAPE_TYPE_COLOR = 2
DXGI_OUTDUPL_POINTER_SHAPE_TYPE_MASKED_COLOR = 4
def _define_DXGI_OUTDUPL_POINTER_SHAPE_INFO_head():
    class DXGI_OUTDUPL_POINTER_SHAPE_INFO(Structure):
        pass
    return DXGI_OUTDUPL_POINTER_SHAPE_INFO
def _define_DXGI_OUTDUPL_POINTER_SHAPE_INFO():
    DXGI_OUTDUPL_POINTER_SHAPE_INFO = win32more.Graphics.Dxgi.DXGI_OUTDUPL_POINTER_SHAPE_INFO_head
    DXGI_OUTDUPL_POINTER_SHAPE_INFO._fields_ = [
        ("Type", UInt32),
        ("Width", UInt32),
        ("Height", UInt32),
        ("Pitch", UInt32),
        ("HotSpot", win32more.Foundation.POINT),
    ]
    return DXGI_OUTDUPL_POINTER_SHAPE_INFO
def _define_DXGI_OUTDUPL_FRAME_INFO_head():
    class DXGI_OUTDUPL_FRAME_INFO(Structure):
        pass
    return DXGI_OUTDUPL_FRAME_INFO
def _define_DXGI_OUTDUPL_FRAME_INFO():
    DXGI_OUTDUPL_FRAME_INFO = win32more.Graphics.Dxgi.DXGI_OUTDUPL_FRAME_INFO_head
    DXGI_OUTDUPL_FRAME_INFO._fields_ = [
        ("LastPresentTime", win32more.Foundation.LARGE_INTEGER),
        ("LastMouseUpdateTime", win32more.Foundation.LARGE_INTEGER),
        ("AccumulatedFrames", UInt32),
        ("RectsCoalesced", win32more.Foundation.BOOL),
        ("ProtectedContentMaskedOut", win32more.Foundation.BOOL),
        ("PointerPosition", win32more.Graphics.Dxgi.DXGI_OUTDUPL_POINTER_POSITION),
        ("TotalMetadataBufferSize", UInt32),
        ("PointerShapeBufferSize", UInt32),
    ]
    return DXGI_OUTDUPL_FRAME_INFO
def _define_IDXGIOutputDuplication_head():
    class IDXGIOutputDuplication(win32more.Graphics.Dxgi.IDXGIObject_head):
        Guid = Guid('191cfac3-a341-470d-b26e-a864f428319c')
    return IDXGIOutputDuplication
def _define_IDXGIOutputDuplication():
    IDXGIOutputDuplication = win32more.Graphics.Dxgi.IDXGIOutputDuplication_head
    IDXGIOutputDuplication.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Dxgi.DXGI_OUTDUPL_DESC_head), use_last_error=False)(7, 'GetDesc', ((1, 'pDesc'),)))
    IDXGIOutputDuplication.AcquireNextFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Dxgi.DXGI_OUTDUPL_FRAME_INFO_head),POINTER(win32more.Graphics.Dxgi.IDXGIResource_head), use_last_error=False)(8, 'AcquireNextFrame', ((1, 'TimeoutInMilliseconds'),(1, 'pFrameInfo'),(1, 'ppDesktopResource'),)))
    IDXGIOutputDuplication.GetFrameDirtyRects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.RECT_head),POINTER(UInt32), use_last_error=False)(9, 'GetFrameDirtyRects', ((1, 'DirtyRectsBufferSize'),(1, 'pDirtyRectsBuffer'),(1, 'pDirtyRectsBufferSizeRequired'),)))
    IDXGIOutputDuplication.GetFrameMoveRects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Dxgi.DXGI_OUTDUPL_MOVE_RECT_head),POINTER(UInt32), use_last_error=False)(10, 'GetFrameMoveRects', ((1, 'MoveRectsBufferSize'),(1, 'pMoveRectBuffer'),(1, 'pMoveRectsBufferSizeRequired'),)))
    IDXGIOutputDuplication.GetFramePointerShape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,POINTER(UInt32),POINTER(win32more.Graphics.Dxgi.DXGI_OUTDUPL_POINTER_SHAPE_INFO_head), use_last_error=False)(11, 'GetFramePointerShape', ((1, 'PointerShapeBufferSize'),(1, 'pPointerShapeBuffer'),(1, 'pPointerShapeBufferSizeRequired'),(1, 'pPointerShapeInfo'),)))
    IDXGIOutputDuplication.MapDesktopSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_MAPPED_RECT_head), use_last_error=False)(12, 'MapDesktopSurface', ((1, 'pLockedRect'),)))
    IDXGIOutputDuplication.UnMapDesktopSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'UnMapDesktopSurface', ()))
    IDXGIOutputDuplication.ReleaseFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'ReleaseFrame', ()))
    return IDXGIOutputDuplication
def _define_IDXGISurface2_head():
    class IDXGISurface2(win32more.Graphics.Dxgi.IDXGISurface1_head):
        Guid = Guid('aba496dd-b617-4cb8-a866-bc44d7eb1fa2')
    return IDXGISurface2
def _define_IDXGISurface2():
    IDXGISurface2 = win32more.Graphics.Dxgi.IDXGISurface2_head
    IDXGISurface2.GetResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),POINTER(UInt32), use_last_error=False)(13, 'GetResource', ((1, 'riid'),(1, 'ppParentResource'),(1, 'pSubresourceIndex'),)))
    return IDXGISurface2
def _define_IDXGIResource1_head():
    class IDXGIResource1(win32more.Graphics.Dxgi.IDXGIResource_head):
        Guid = Guid('30961379-4609-4a41-998e-54fe567ee0c1')
    return IDXGIResource1
def _define_IDXGIResource1():
    IDXGIResource1 = win32more.Graphics.Dxgi.IDXGIResource1_head
    IDXGIResource1.CreateSubresourceSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Dxgi.IDXGISurface2_head), use_last_error=False)(12, 'CreateSubresourceSurface', ((1, 'index'),(1, 'ppSurface'),)))
    IDXGIResource1.CreateSharedHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(13, 'CreateSharedHandle', ((1, 'pAttributes'),(1, 'dwAccess'),(1, 'lpName'),(1, 'pHandle'),)))
    return IDXGIResource1
DXGI_OFFER_RESOURCE_PRIORITY = Int32
DXGI_OFFER_RESOURCE_PRIORITY_LOW = 1
DXGI_OFFER_RESOURCE_PRIORITY_NORMAL = 2
DXGI_OFFER_RESOURCE_PRIORITY_HIGH = 3
def _define_IDXGIDevice2_head():
    class IDXGIDevice2(win32more.Graphics.Dxgi.IDXGIDevice1_head):
        Guid = Guid('05008617-fbfd-4051-a790-144884b4f6a9')
    return IDXGIDevice2
def _define_IDXGIDevice2():
    IDXGIDevice2 = win32more.Graphics.Dxgi.IDXGIDevice2_head
    IDXGIDevice2.OfferResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Dxgi.IDXGIResource_head),win32more.Graphics.Dxgi.DXGI_OFFER_RESOURCE_PRIORITY, use_last_error=False)(14, 'OfferResources', ((1, 'NumResources'),(1, 'ppResources'),(1, 'Priority'),)))
    IDXGIDevice2.ReclaimResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Dxgi.IDXGIResource_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(15, 'ReclaimResources', ((1, 'NumResources'),(1, 'ppResources'),(1, 'pDiscarded'),)))
    IDXGIDevice2.EnqueueSetEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE, use_last_error=False)(16, 'EnqueueSetEvent', ((1, 'hEvent'),)))
    return IDXGIDevice2
def _define_DXGI_MODE_DESC1_head():
    class DXGI_MODE_DESC1(Structure):
        pass
    return DXGI_MODE_DESC1
def _define_DXGI_MODE_DESC1():
    DXGI_MODE_DESC1 = win32more.Graphics.Dxgi.DXGI_MODE_DESC1_head
    DXGI_MODE_DESC1._fields_ = [
        ("Width", UInt32),
        ("Height", UInt32),
        ("RefreshRate", win32more.Graphics.Dxgi.Common.DXGI_RATIONAL),
        ("Format", win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ("ScanlineOrdering", win32more.Graphics.Dxgi.Common.DXGI_MODE_SCANLINE_ORDER),
        ("Scaling", win32more.Graphics.Dxgi.Common.DXGI_MODE_SCALING),
        ("Stereo", win32more.Foundation.BOOL),
    ]
    return DXGI_MODE_DESC1
DXGI_SCALING = Int32
DXGI_SCALING_STRETCH = 0
DXGI_SCALING_NONE = 1
DXGI_SCALING_ASPECT_RATIO_STRETCH = 2
def _define_DXGI_SWAP_CHAIN_DESC1_head():
    class DXGI_SWAP_CHAIN_DESC1(Structure):
        pass
    return DXGI_SWAP_CHAIN_DESC1
def _define_DXGI_SWAP_CHAIN_DESC1():
    DXGI_SWAP_CHAIN_DESC1 = win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC1_head
    DXGI_SWAP_CHAIN_DESC1._fields_ = [
        ("Width", UInt32),
        ("Height", UInt32),
        ("Format", win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ("Stereo", win32more.Foundation.BOOL),
        ("SampleDesc", win32more.Graphics.Dxgi.Common.DXGI_SAMPLE_DESC),
        ("BufferUsage", UInt32),
        ("BufferCount", UInt32),
        ("Scaling", win32more.Graphics.Dxgi.DXGI_SCALING),
        ("SwapEffect", win32more.Graphics.Dxgi.DXGI_SWAP_EFFECT),
        ("AlphaMode", win32more.Graphics.Dxgi.Common.DXGI_ALPHA_MODE),
        ("Flags", UInt32),
    ]
    return DXGI_SWAP_CHAIN_DESC1
def _define_DXGI_SWAP_CHAIN_FULLSCREEN_DESC_head():
    class DXGI_SWAP_CHAIN_FULLSCREEN_DESC(Structure):
        pass
    return DXGI_SWAP_CHAIN_FULLSCREEN_DESC
def _define_DXGI_SWAP_CHAIN_FULLSCREEN_DESC():
    DXGI_SWAP_CHAIN_FULLSCREEN_DESC = win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_FULLSCREEN_DESC_head
    DXGI_SWAP_CHAIN_FULLSCREEN_DESC._fields_ = [
        ("RefreshRate", win32more.Graphics.Dxgi.Common.DXGI_RATIONAL),
        ("ScanlineOrdering", win32more.Graphics.Dxgi.Common.DXGI_MODE_SCANLINE_ORDER),
        ("Scaling", win32more.Graphics.Dxgi.Common.DXGI_MODE_SCALING),
        ("Windowed", win32more.Foundation.BOOL),
    ]
    return DXGI_SWAP_CHAIN_FULLSCREEN_DESC
def _define_DXGI_PRESENT_PARAMETERS_head():
    class DXGI_PRESENT_PARAMETERS(Structure):
        pass
    return DXGI_PRESENT_PARAMETERS
def _define_DXGI_PRESENT_PARAMETERS():
    DXGI_PRESENT_PARAMETERS = win32more.Graphics.Dxgi.DXGI_PRESENT_PARAMETERS_head
    DXGI_PRESENT_PARAMETERS._fields_ = [
        ("DirtyRectsCount", UInt32),
        ("pDirtyRects", POINTER(win32more.Foundation.RECT_head)),
        ("pScrollRect", POINTER(win32more.Foundation.RECT_head)),
        ("pScrollOffset", POINTER(win32more.Foundation.POINT_head)),
    ]
    return DXGI_PRESENT_PARAMETERS
def _define_IDXGISwapChain1_head():
    class IDXGISwapChain1(win32more.Graphics.Dxgi.IDXGISwapChain_head):
        Guid = Guid('790a45f7-0d42-4876-983a-0a55cfe6f4aa')
    return IDXGISwapChain1
def _define_IDXGISwapChain1():
    IDXGISwapChain1 = win32more.Graphics.Dxgi.IDXGISwapChain1_head
    IDXGISwapChain1.GetDesc1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC1_head), use_last_error=False)(18, 'GetDesc1', ((1, 'pDesc'),)))
    IDXGISwapChain1.GetFullscreenDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_FULLSCREEN_DESC_head), use_last_error=False)(19, 'GetFullscreenDesc', ((1, 'pDesc'),)))
    IDXGISwapChain1.GetHwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND), use_last_error=False)(20, 'GetHwnd', ((1, 'pHwnd'),)))
    IDXGISwapChain1.GetCoreWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(21, 'GetCoreWindow', ((1, 'refiid'),(1, 'ppUnk'),)))
    IDXGISwapChain1.Present1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.DXGI_PRESENT_PARAMETERS_head), use_last_error=False)(22, 'Present1', ((1, 'SyncInterval'),(1, 'PresentFlags'),(1, 'pPresentParameters'),)))
    IDXGISwapChain1.IsTemporaryMonoSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(23, 'IsTemporaryMonoSupported', ()))
    IDXGISwapChain1.GetRestrictToOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.IDXGIOutput_head), use_last_error=False)(24, 'GetRestrictToOutput', ((1, 'ppRestrictToOutput'),)))
    IDXGISwapChain1.SetBackgroundColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_RGBA_head), use_last_error=False)(25, 'SetBackgroundColor', ((1, 'pColor'),)))
    IDXGISwapChain1.GetBackgroundColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_RGBA_head), use_last_error=False)(26, 'GetBackgroundColor', ((1, 'pColor'),)))
    IDXGISwapChain1.SetRotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.Common.DXGI_MODE_ROTATION, use_last_error=False)(27, 'SetRotation', ((1, 'Rotation'),)))
    IDXGISwapChain1.GetRotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.Common.DXGI_MODE_ROTATION), use_last_error=False)(28, 'GetRotation', ((1, 'pRotation'),)))
    return IDXGISwapChain1
def _define_IDXGIFactory2_head():
    class IDXGIFactory2(win32more.Graphics.Dxgi.IDXGIFactory1_head):
        Guid = Guid('50c83a1c-e072-4c48-87b0-3630fa36a6d0')
    return IDXGIFactory2
def _define_IDXGIFactory2():
    IDXGIFactory2 = win32more.Graphics.Dxgi.IDXGIFactory2_head
    IDXGIFactory2.IsWindowedStereoEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(14, 'IsWindowedStereoEnabled', ()))
    IDXGIFactory2.CreateSwapChainForHwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.HWND,POINTER(win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC1_head),POINTER(win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_FULLSCREEN_DESC_head),win32more.Graphics.Dxgi.IDXGIOutput_head,POINTER(win32more.Graphics.Dxgi.IDXGISwapChain1_head), use_last_error=False)(15, 'CreateSwapChainForHwnd', ((1, 'pDevice'),(1, 'hWnd'),(1, 'pDesc'),(1, 'pFullscreenDesc'),(1, 'pRestrictToOutput'),(1, 'ppSwapChain'),)))
    IDXGIFactory2.CreateSwapChainForCoreWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head,POINTER(win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC1_head),win32more.Graphics.Dxgi.IDXGIOutput_head,POINTER(win32more.Graphics.Dxgi.IDXGISwapChain1_head), use_last_error=False)(16, 'CreateSwapChainForCoreWindow', ((1, 'pDevice'),(1, 'pWindow'),(1, 'pDesc'),(1, 'pRestrictToOutput'),(1, 'ppSwapChain'),)))
    IDXGIFactory2.GetSharedResourceAdapterLuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LUID_head), use_last_error=False)(17, 'GetSharedResourceAdapterLuid', ((1, 'hResource'),(1, 'pLuid'),)))
    IDXGIFactory2.RegisterStereoStatusWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,POINTER(UInt32), use_last_error=False)(18, 'RegisterStereoStatusWindow', ((1, 'WindowHandle'),(1, 'wMsg'),(1, 'pdwCookie'),)))
    IDXGIFactory2.RegisterStereoStatusEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(UInt32), use_last_error=False)(19, 'RegisterStereoStatusEvent', ((1, 'hEvent'),(1, 'pdwCookie'),)))
    IDXGIFactory2.UnregisterStereoStatus = COMMETHOD(WINFUNCTYPE(Void,UInt32, use_last_error=False)(20, 'UnregisterStereoStatus', ((1, 'dwCookie'),)))
    IDXGIFactory2.RegisterOcclusionStatusWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,POINTER(UInt32), use_last_error=False)(21, 'RegisterOcclusionStatusWindow', ((1, 'WindowHandle'),(1, 'wMsg'),(1, 'pdwCookie'),)))
    IDXGIFactory2.RegisterOcclusionStatusEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(UInt32), use_last_error=False)(22, 'RegisterOcclusionStatusEvent', ((1, 'hEvent'),(1, 'pdwCookie'),)))
    IDXGIFactory2.UnregisterOcclusionStatus = COMMETHOD(WINFUNCTYPE(Void,UInt32, use_last_error=False)(23, 'UnregisterOcclusionStatus', ((1, 'dwCookie'),)))
    IDXGIFactory2.CreateSwapChainForComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC1_head),win32more.Graphics.Dxgi.IDXGIOutput_head,POINTER(win32more.Graphics.Dxgi.IDXGISwapChain1_head), use_last_error=False)(24, 'CreateSwapChainForComposition', ((1, 'pDevice'),(1, 'pDesc'),(1, 'pRestrictToOutput'),(1, 'ppSwapChain'),)))
    return IDXGIFactory2
DXGI_GRAPHICS_PREEMPTION_GRANULARITY = Int32
DXGI_GRAPHICS_PREEMPTION_DMA_BUFFER_BOUNDARY = 0
DXGI_GRAPHICS_PREEMPTION_PRIMITIVE_BOUNDARY = 1
DXGI_GRAPHICS_PREEMPTION_TRIANGLE_BOUNDARY = 2
DXGI_GRAPHICS_PREEMPTION_PIXEL_BOUNDARY = 3
DXGI_GRAPHICS_PREEMPTION_INSTRUCTION_BOUNDARY = 4
DXGI_COMPUTE_PREEMPTION_GRANULARITY = Int32
DXGI_COMPUTE_PREEMPTION_DMA_BUFFER_BOUNDARY = 0
DXGI_COMPUTE_PREEMPTION_DISPATCH_BOUNDARY = 1
DXGI_COMPUTE_PREEMPTION_THREAD_GROUP_BOUNDARY = 2
DXGI_COMPUTE_PREEMPTION_THREAD_BOUNDARY = 3
DXGI_COMPUTE_PREEMPTION_INSTRUCTION_BOUNDARY = 4
def _define_DXGI_ADAPTER_DESC2_head():
    class DXGI_ADAPTER_DESC2(Structure):
        pass
    return DXGI_ADAPTER_DESC2
def _define_DXGI_ADAPTER_DESC2():
    DXGI_ADAPTER_DESC2 = win32more.Graphics.Dxgi.DXGI_ADAPTER_DESC2_head
    DXGI_ADAPTER_DESC2._fields_ = [
        ("Description", Char * 128),
        ("VendorId", UInt32),
        ("DeviceId", UInt32),
        ("SubSysId", UInt32),
        ("Revision", UInt32),
        ("DedicatedVideoMemory", UIntPtr),
        ("DedicatedSystemMemory", UIntPtr),
        ("SharedSystemMemory", UIntPtr),
        ("AdapterLuid", win32more.Foundation.LUID),
        ("Flags", UInt32),
        ("GraphicsPreemptionGranularity", win32more.Graphics.Dxgi.DXGI_GRAPHICS_PREEMPTION_GRANULARITY),
        ("ComputePreemptionGranularity", win32more.Graphics.Dxgi.DXGI_COMPUTE_PREEMPTION_GRANULARITY),
    ]
    return DXGI_ADAPTER_DESC2
def _define_IDXGIAdapter2_head():
    class IDXGIAdapter2(win32more.Graphics.Dxgi.IDXGIAdapter1_head):
        Guid = Guid('0aa1ae0a-fa0e-4b84-8644-e05ff8e5acb5')
    return IDXGIAdapter2
def _define_IDXGIAdapter2():
    IDXGIAdapter2 = win32more.Graphics.Dxgi.IDXGIAdapter2_head
    IDXGIAdapter2.GetDesc2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_ADAPTER_DESC2_head), use_last_error=False)(11, 'GetDesc2', ((1, 'pDesc'),)))
    return IDXGIAdapter2
def _define_IDXGIOutput1_head():
    class IDXGIOutput1(win32more.Graphics.Dxgi.IDXGIOutput_head):
        Guid = Guid('00cddea8-939b-4b83-a340-a685226666cc')
    return IDXGIOutput1
def _define_IDXGIOutput1():
    IDXGIOutput1 = win32more.Graphics.Dxgi.IDXGIOutput1_head
    IDXGIOutput1.GetDisplayModeList1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,UInt32,POINTER(UInt32),POINTER(win32more.Graphics.Dxgi.DXGI_MODE_DESC1), use_last_error=False)(19, 'GetDisplayModeList1', ((1, 'EnumFormat'),(1, 'Flags'),(1, 'pNumModes'),(1, 'pDesc'),)))
    IDXGIOutput1.FindClosestMatchingMode1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_MODE_DESC1_head),POINTER(win32more.Graphics.Dxgi.DXGI_MODE_DESC1_head),win32more.System.Com.IUnknown_head, use_last_error=False)(20, 'FindClosestMatchingMode1', ((1, 'pModeToMatch'),(1, 'pClosestMatch'),(1, 'pConcernedDevice'),)))
    IDXGIOutput1.GetDisplaySurfaceData1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIResource_head, use_last_error=False)(21, 'GetDisplaySurfaceData1', ((1, 'pDestination'),)))
    IDXGIOutput1.DuplicateOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.Graphics.Dxgi.IDXGIOutputDuplication_head), use_last_error=False)(22, 'DuplicateOutput', ((1, 'pDevice'),(1, 'ppOutputDuplication'),)))
    return IDXGIOutput1
def _define_IDXGIDevice3_head():
    class IDXGIDevice3(win32more.Graphics.Dxgi.IDXGIDevice2_head):
        Guid = Guid('6007896c-3244-4afd-bf18-a6d3beda5023')
    return IDXGIDevice3
def _define_IDXGIDevice3():
    IDXGIDevice3 = win32more.Graphics.Dxgi.IDXGIDevice3_head
    IDXGIDevice3.Trim = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(17, 'Trim', ()))
    return IDXGIDevice3
def _define_DXGI_MATRIX_3X2_F_head():
    class DXGI_MATRIX_3X2_F(Structure):
        pass
    return DXGI_MATRIX_3X2_F
def _define_DXGI_MATRIX_3X2_F():
    DXGI_MATRIX_3X2_F = win32more.Graphics.Dxgi.DXGI_MATRIX_3X2_F_head
    DXGI_MATRIX_3X2_F._fields_ = [
        ("_11", Single),
        ("_12", Single),
        ("_21", Single),
        ("_22", Single),
        ("_31", Single),
        ("_32", Single),
    ]
    return DXGI_MATRIX_3X2_F
def _define_IDXGISwapChain2_head():
    class IDXGISwapChain2(win32more.Graphics.Dxgi.IDXGISwapChain1_head):
        Guid = Guid('a8be2ac4-199f-4946-b331-79599fb98de7')
    return IDXGISwapChain2
def _define_IDXGISwapChain2():
    IDXGISwapChain2 = win32more.Graphics.Dxgi.IDXGISwapChain2_head
    IDXGISwapChain2.SetSourceSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(29, 'SetSourceSize', ((1, 'Width'),(1, 'Height'),)))
    IDXGISwapChain2.GetSourceSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(30, 'GetSourceSize', ((1, 'pWidth'),(1, 'pHeight'),)))
    IDXGISwapChain2.SetMaximumFrameLatency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(31, 'SetMaximumFrameLatency', ((1, 'MaxLatency'),)))
    IDXGISwapChain2.GetMaximumFrameLatency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(32, 'GetMaximumFrameLatency', ((1, 'pMaxLatency'),)))
    IDXGISwapChain2.GetFrameLatencyWaitableObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HANDLE, use_last_error=False)(33, 'GetFrameLatencyWaitableObject', ()))
    IDXGISwapChain2.SetMatrixTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_MATRIX_3X2_F_head), use_last_error=False)(34, 'SetMatrixTransform', ((1, 'pMatrix'),)))
    IDXGISwapChain2.GetMatrixTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_MATRIX_3X2_F_head), use_last_error=False)(35, 'GetMatrixTransform', ((1, 'pMatrix'),)))
    return IDXGISwapChain2
def _define_IDXGIOutput2_head():
    class IDXGIOutput2(win32more.Graphics.Dxgi.IDXGIOutput1_head):
        Guid = Guid('595e39d1-2724-4663-99b1-da969de28364')
    return IDXGIOutput2
def _define_IDXGIOutput2():
    IDXGIOutput2 = win32more.Graphics.Dxgi.IDXGIOutput2_head
    IDXGIOutput2.SupportsOverlays = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(23, 'SupportsOverlays', ()))
    return IDXGIOutput2
def _define_IDXGIFactory3_head():
    class IDXGIFactory3(win32more.Graphics.Dxgi.IDXGIFactory2_head):
        Guid = Guid('25483823-cd46-4c7d-86ca-47aa95b837bd')
    return IDXGIFactory3
def _define_IDXGIFactory3():
    IDXGIFactory3 = win32more.Graphics.Dxgi.IDXGIFactory3_head
    IDXGIFactory3.GetCreationFlags = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(25, 'GetCreationFlags', ()))
    return IDXGIFactory3
def _define_DXGI_DECODE_SWAP_CHAIN_DESC_head():
    class DXGI_DECODE_SWAP_CHAIN_DESC(Structure):
        pass
    return DXGI_DECODE_SWAP_CHAIN_DESC
def _define_DXGI_DECODE_SWAP_CHAIN_DESC():
    DXGI_DECODE_SWAP_CHAIN_DESC = win32more.Graphics.Dxgi.DXGI_DECODE_SWAP_CHAIN_DESC_head
    DXGI_DECODE_SWAP_CHAIN_DESC._fields_ = [
        ("Flags", UInt32),
    ]
    return DXGI_DECODE_SWAP_CHAIN_DESC
DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS = Int32
DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE = 1
DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709 = 2
DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC = 4
def _define_IDXGIDecodeSwapChain_head():
    class IDXGIDecodeSwapChain(win32more.System.Com.IUnknown_head):
        Guid = Guid('2633066b-4514-4c7a-8fd8-12ea98059d18')
    return IDXGIDecodeSwapChain
def _define_IDXGIDecodeSwapChain():
    IDXGIDecodeSwapChain = win32more.Graphics.Dxgi.IDXGIDecodeSwapChain_head
    IDXGIDecodeSwapChain.PresentBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32, use_last_error=False)(3, 'PresentBuffer', ((1, 'BufferToPresent'),(1, 'SyncInterval'),(1, 'Flags'),)))
    IDXGIDecodeSwapChain.SetSourceRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(4, 'SetSourceRect', ((1, 'pRect'),)))
    IDXGIDecodeSwapChain.SetTargetRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(5, 'SetTargetRect', ((1, 'pRect'),)))
    IDXGIDecodeSwapChain.SetDestSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(6, 'SetDestSize', ((1, 'Width'),(1, 'Height'),)))
    IDXGIDecodeSwapChain.GetSourceRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(7, 'GetSourceRect', ((1, 'pRect'),)))
    IDXGIDecodeSwapChain.GetTargetRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(8, 'GetTargetRect', ((1, 'pRect'),)))
    IDXGIDecodeSwapChain.GetDestSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(9, 'GetDestSize', ((1, 'pWidth'),(1, 'pHeight'),)))
    IDXGIDecodeSwapChain.SetColorSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS, use_last_error=False)(10, 'SetColorSpace', ((1, 'ColorSpace'),)))
    IDXGIDecodeSwapChain.GetColorSpace = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Dxgi.DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS, use_last_error=False)(11, 'GetColorSpace', ()))
    return IDXGIDecodeSwapChain
def _define_IDXGIFactoryMedia_head():
    class IDXGIFactoryMedia(win32more.System.Com.IUnknown_head):
        Guid = Guid('41e7d1f2-a591-4f7b-a2e5-fa9c843e1c12')
    return IDXGIFactoryMedia
def _define_IDXGIFactoryMedia():
    IDXGIFactoryMedia = win32more.Graphics.Dxgi.IDXGIFactoryMedia_head
    IDXGIFactoryMedia.CreateSwapChainForCompositionSurfaceHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.HANDLE,POINTER(win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC1_head),win32more.Graphics.Dxgi.IDXGIOutput_head,POINTER(win32more.Graphics.Dxgi.IDXGISwapChain1_head), use_last_error=False)(3, 'CreateSwapChainForCompositionSurfaceHandle', ((1, 'pDevice'),(1, 'hSurface'),(1, 'pDesc'),(1, 'pRestrictToOutput'),(1, 'ppSwapChain'),)))
    IDXGIFactoryMedia.CreateDecodeSwapChainForCompositionSurfaceHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.HANDLE,POINTER(win32more.Graphics.Dxgi.DXGI_DECODE_SWAP_CHAIN_DESC_head),win32more.Graphics.Dxgi.IDXGIResource_head,win32more.Graphics.Dxgi.IDXGIOutput_head,POINTER(win32more.Graphics.Dxgi.IDXGIDecodeSwapChain_head), use_last_error=False)(4, 'CreateDecodeSwapChainForCompositionSurfaceHandle', ((1, 'pDevice'),(1, 'hSurface'),(1, 'pDesc'),(1, 'pYuvDecodeBuffers'),(1, 'pRestrictToOutput'),(1, 'ppSwapChain'),)))
    return IDXGIFactoryMedia
DXGI_FRAME_PRESENTATION_MODE = Int32
DXGI_FRAME_PRESENTATION_MODE_COMPOSED = 0
DXGI_FRAME_PRESENTATION_MODE_OVERLAY = 1
DXGI_FRAME_PRESENTATION_MODE_NONE = 2
DXGI_FRAME_PRESENTATION_MODE_COMPOSITION_FAILURE = 3
def _define_DXGI_FRAME_STATISTICS_MEDIA_head():
    class DXGI_FRAME_STATISTICS_MEDIA(Structure):
        pass
    return DXGI_FRAME_STATISTICS_MEDIA
def _define_DXGI_FRAME_STATISTICS_MEDIA():
    DXGI_FRAME_STATISTICS_MEDIA = win32more.Graphics.Dxgi.DXGI_FRAME_STATISTICS_MEDIA_head
    DXGI_FRAME_STATISTICS_MEDIA._fields_ = [
        ("PresentCount", UInt32),
        ("PresentRefreshCount", UInt32),
        ("SyncRefreshCount", UInt32),
        ("SyncQPCTime", win32more.Foundation.LARGE_INTEGER),
        ("SyncGPUTime", win32more.Foundation.LARGE_INTEGER),
        ("CompositionMode", win32more.Graphics.Dxgi.DXGI_FRAME_PRESENTATION_MODE),
        ("ApprovedPresentDuration", UInt32),
    ]
    return DXGI_FRAME_STATISTICS_MEDIA
def _define_IDXGISwapChainMedia_head():
    class IDXGISwapChainMedia(win32more.System.Com.IUnknown_head):
        Guid = Guid('dd95b90b-f05f-4f6a-bd65-25bfb264bd84')
    return IDXGISwapChainMedia
def _define_IDXGISwapChainMedia():
    IDXGISwapChainMedia = win32more.Graphics.Dxgi.IDXGISwapChainMedia_head
    IDXGISwapChainMedia.GetFrameStatisticsMedia = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_FRAME_STATISTICS_MEDIA_head), use_last_error=False)(3, 'GetFrameStatisticsMedia', ((1, 'pStats'),)))
    IDXGISwapChainMedia.SetPresentDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SetPresentDuration', ((1, 'Duration'),)))
    IDXGISwapChainMedia.CheckPresentDurationSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(5, 'CheckPresentDurationSupport', ((1, 'DesiredPresentDuration'),(1, 'pClosestSmallerPresentDuration'),(1, 'pClosestLargerPresentDuration'),)))
    return IDXGISwapChainMedia
DXGI_OVERLAY_SUPPORT_FLAG = Int32
DXGI_OVERLAY_SUPPORT_FLAG_DIRECT = 1
DXGI_OVERLAY_SUPPORT_FLAG_SCALING = 2
def _define_IDXGIOutput3_head():
    class IDXGIOutput3(win32more.Graphics.Dxgi.IDXGIOutput2_head):
        Guid = Guid('8a6bb301-7e7e-41f4-a8e0-5b32f7f99b18')
    return IDXGIOutput3
def _define_IDXGIOutput3():
    IDXGIOutput3 = win32more.Graphics.Dxgi.IDXGIOutput3_head
    IDXGIOutput3.CheckOverlaySupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,win32more.System.Com.IUnknown_head,POINTER(UInt32), use_last_error=False)(24, 'CheckOverlaySupport', ((1, 'EnumFormat'),(1, 'pConcernedDevice'),(1, 'pFlags'),)))
    return IDXGIOutput3
DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG = Int32
DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG_PRESENT = 1
DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG_OVERLAY_PRESENT = 2
def _define_IDXGISwapChain3_head():
    class IDXGISwapChain3(win32more.Graphics.Dxgi.IDXGISwapChain2_head):
        Guid = Guid('94d99bdb-f1f8-4ab0-b236-7da0170edab1')
    return IDXGISwapChain3
def _define_IDXGISwapChain3():
    IDXGISwapChain3 = win32more.Graphics.Dxgi.IDXGISwapChain3_head
    IDXGISwapChain3.GetCurrentBackBufferIndex = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(36, 'GetCurrentBackBufferIndex', ()))
    IDXGISwapChain3.CheckColorSpaceSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE,POINTER(UInt32), use_last_error=False)(37, 'CheckColorSpaceSupport', ((1, 'ColorSpace'),(1, 'pColorSpaceSupport'),)))
    IDXGISwapChain3.SetColorSpace1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE, use_last_error=False)(38, 'SetColorSpace1', ((1, 'ColorSpace'),)))
    IDXGISwapChain3.ResizeBuffers1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,UInt32,POINTER(UInt32),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(39, 'ResizeBuffers1', ((1, 'BufferCount'),(1, 'Width'),(1, 'Height'),(1, 'Format'),(1, 'SwapChainFlags'),(1, 'pCreationNodeMask'),(1, 'ppPresentQueue'),)))
    return IDXGISwapChain3
DXGI_OVERLAY_COLOR_SPACE_SUPPORT_FLAG = Int32
DXGI_OVERLAY_COLOR_SPACE_SUPPORT_FLAG_PRESENT = 1
def _define_IDXGIOutput4_head():
    class IDXGIOutput4(win32more.Graphics.Dxgi.IDXGIOutput3_head):
        Guid = Guid('dc7dca35-2196-414d-9f53-617884032a60')
    return IDXGIOutput4
def _define_IDXGIOutput4():
    IDXGIOutput4 = win32more.Graphics.Dxgi.IDXGIOutput4_head
    IDXGIOutput4.CheckOverlayColorSpaceSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,win32more.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE,win32more.System.Com.IUnknown_head,POINTER(UInt32), use_last_error=False)(25, 'CheckOverlayColorSpaceSupport', ((1, 'Format'),(1, 'ColorSpace'),(1, 'pConcernedDevice'),(1, 'pFlags'),)))
    return IDXGIOutput4
def _define_IDXGIFactory4_head():
    class IDXGIFactory4(win32more.Graphics.Dxgi.IDXGIFactory3_head):
        Guid = Guid('1bc6ea02-ef36-464f-bf0c-21ca39e5168a')
    return IDXGIFactory4
def _define_IDXGIFactory4():
    IDXGIFactory4 = win32more.Graphics.Dxgi.IDXGIFactory4_head
    IDXGIFactory4.EnumAdapterByLuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LUID,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(26, 'EnumAdapterByLuid', ((1, 'AdapterLuid'),(1, 'riid'),(1, 'ppvAdapter'),)))
    IDXGIFactory4.EnumWarpAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(27, 'EnumWarpAdapter', ((1, 'riid'),(1, 'ppvAdapter'),)))
    return IDXGIFactory4
DXGI_MEMORY_SEGMENT_GROUP = Int32
DXGI_MEMORY_SEGMENT_GROUP_LOCAL = 0
DXGI_MEMORY_SEGMENT_GROUP_NON_LOCAL = 1
def _define_DXGI_QUERY_VIDEO_MEMORY_INFO_head():
    class DXGI_QUERY_VIDEO_MEMORY_INFO(Structure):
        pass
    return DXGI_QUERY_VIDEO_MEMORY_INFO
def _define_DXGI_QUERY_VIDEO_MEMORY_INFO():
    DXGI_QUERY_VIDEO_MEMORY_INFO = win32more.Graphics.Dxgi.DXGI_QUERY_VIDEO_MEMORY_INFO_head
    DXGI_QUERY_VIDEO_MEMORY_INFO._fields_ = [
        ("Budget", UInt64),
        ("CurrentUsage", UInt64),
        ("AvailableForReservation", UInt64),
        ("CurrentReservation", UInt64),
    ]
    return DXGI_QUERY_VIDEO_MEMORY_INFO
def _define_IDXGIAdapter3_head():
    class IDXGIAdapter3(win32more.Graphics.Dxgi.IDXGIAdapter2_head):
        Guid = Guid('645967a4-1392-4310-a798-8053ce3e93fd')
    return IDXGIAdapter3
def _define_IDXGIAdapter3():
    IDXGIAdapter3 = win32more.Graphics.Dxgi.IDXGIAdapter3_head
    IDXGIAdapter3.RegisterHardwareContentProtectionTeardownStatusEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(UInt32), use_last_error=False)(12, 'RegisterHardwareContentProtectionTeardownStatusEvent', ((1, 'hEvent'),(1, 'pdwCookie'),)))
    IDXGIAdapter3.UnregisterHardwareContentProtectionTeardownStatus = COMMETHOD(WINFUNCTYPE(Void,UInt32, use_last_error=False)(13, 'UnregisterHardwareContentProtectionTeardownStatus', ((1, 'dwCookie'),)))
    IDXGIAdapter3.QueryVideoMemoryInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Dxgi.DXGI_MEMORY_SEGMENT_GROUP,POINTER(win32more.Graphics.Dxgi.DXGI_QUERY_VIDEO_MEMORY_INFO_head), use_last_error=False)(14, 'QueryVideoMemoryInfo', ((1, 'NodeIndex'),(1, 'MemorySegmentGroup'),(1, 'pVideoMemoryInfo'),)))
    IDXGIAdapter3.SetVideoMemoryReservation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Dxgi.DXGI_MEMORY_SEGMENT_GROUP,UInt64, use_last_error=False)(15, 'SetVideoMemoryReservation', ((1, 'NodeIndex'),(1, 'MemorySegmentGroup'),(1, 'Reservation'),)))
    IDXGIAdapter3.RegisterVideoMemoryBudgetChangeNotificationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(UInt32), use_last_error=False)(16, 'RegisterVideoMemoryBudgetChangeNotificationEvent', ((1, 'hEvent'),(1, 'pdwCookie'),)))
    IDXGIAdapter3.UnregisterVideoMemoryBudgetChangeNotification = COMMETHOD(WINFUNCTYPE(Void,UInt32, use_last_error=False)(17, 'UnregisterVideoMemoryBudgetChangeNotification', ((1, 'dwCookie'),)))
    return IDXGIAdapter3
DXGI_OUTDUPL_FLAG = Int32
DXGI_OUTDUPL_COMPOSITED_UI_CAPTURE_ONLY = 1
def _define_IDXGIOutput5_head():
    class IDXGIOutput5(win32more.Graphics.Dxgi.IDXGIOutput4_head):
        Guid = Guid('80a07424-ab52-42eb-833c-0c42fd282d98')
    return IDXGIOutput5
def _define_IDXGIOutput5():
    IDXGIOutput5 = win32more.Graphics.Dxgi.IDXGIOutput5_head
    IDXGIOutput5.DuplicateOutput1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.Common.DXGI_FORMAT),POINTER(win32more.Graphics.Dxgi.IDXGIOutputDuplication_head), use_last_error=False)(26, 'DuplicateOutput1', ((1, 'pDevice'),(1, 'Flags'),(1, 'SupportedFormatsCount'),(1, 'pSupportedFormats'),(1, 'ppOutputDuplication'),)))
    return IDXGIOutput5
DXGI_HDR_METADATA_TYPE = Int32
DXGI_HDR_METADATA_TYPE_NONE = 0
DXGI_HDR_METADATA_TYPE_HDR10 = 1
DXGI_HDR_METADATA_TYPE_HDR10PLUS = 2
def _define_DXGI_HDR_METADATA_HDR10_head():
    class DXGI_HDR_METADATA_HDR10(Structure):
        pass
    return DXGI_HDR_METADATA_HDR10
def _define_DXGI_HDR_METADATA_HDR10():
    DXGI_HDR_METADATA_HDR10 = win32more.Graphics.Dxgi.DXGI_HDR_METADATA_HDR10_head
    DXGI_HDR_METADATA_HDR10._fields_ = [
        ("RedPrimary", UInt16 * 2),
        ("GreenPrimary", UInt16 * 2),
        ("BluePrimary", UInt16 * 2),
        ("WhitePoint", UInt16 * 2),
        ("MaxMasteringLuminance", UInt32),
        ("MinMasteringLuminance", UInt32),
        ("MaxContentLightLevel", UInt16),
        ("MaxFrameAverageLightLevel", UInt16),
    ]
    return DXGI_HDR_METADATA_HDR10
def _define_DXGI_HDR_METADATA_HDR10PLUS_head():
    class DXGI_HDR_METADATA_HDR10PLUS(Structure):
        pass
    return DXGI_HDR_METADATA_HDR10PLUS
def _define_DXGI_HDR_METADATA_HDR10PLUS():
    DXGI_HDR_METADATA_HDR10PLUS = win32more.Graphics.Dxgi.DXGI_HDR_METADATA_HDR10PLUS_head
    DXGI_HDR_METADATA_HDR10PLUS._fields_ = [
        ("Data", Byte * 72),
    ]
    return DXGI_HDR_METADATA_HDR10PLUS
def _define_IDXGISwapChain4_head():
    class IDXGISwapChain4(win32more.Graphics.Dxgi.IDXGISwapChain3_head):
        Guid = Guid('3d585d5a-bd4a-489e-b1f4-3dbcb6452ffb')
    return IDXGISwapChain4
def _define_IDXGISwapChain4():
    IDXGISwapChain4 = win32more.Graphics.Dxgi.IDXGISwapChain4_head
    IDXGISwapChain4.SetHDRMetaData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.DXGI_HDR_METADATA_TYPE,UInt32,POINTER(Void), use_last_error=False)(40, 'SetHDRMetaData', ((1, 'Type'),(1, 'Size'),(1, 'pMetaData'),)))
    return IDXGISwapChain4
DXGI_OFFER_RESOURCE_FLAGS = Int32
DXGI_OFFER_RESOURCE_FLAG_ALLOW_DECOMMIT = 1
DXGI_RECLAIM_RESOURCE_RESULTS = Int32
DXGI_RECLAIM_RESOURCE_RESULT_OK = 0
DXGI_RECLAIM_RESOURCE_RESULT_DISCARDED = 1
DXGI_RECLAIM_RESOURCE_RESULT_NOT_COMMITTED = 2
def _define_IDXGIDevice4_head():
    class IDXGIDevice4(win32more.Graphics.Dxgi.IDXGIDevice3_head):
        Guid = Guid('95b4f95f-d8da-4ca4-9ee6-3b76d5968a10')
    return IDXGIDevice4
def _define_IDXGIDevice4():
    IDXGIDevice4 = win32more.Graphics.Dxgi.IDXGIDevice4_head
    IDXGIDevice4.OfferResources1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Dxgi.IDXGIResource_head),win32more.Graphics.Dxgi.DXGI_OFFER_RESOURCE_PRIORITY,UInt32, use_last_error=False)(18, 'OfferResources1', ((1, 'NumResources'),(1, 'ppResources'),(1, 'Priority'),(1, 'Flags'),)))
    IDXGIDevice4.ReclaimResources1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Dxgi.IDXGIResource_head),POINTER(win32more.Graphics.Dxgi.DXGI_RECLAIM_RESOURCE_RESULTS), use_last_error=False)(19, 'ReclaimResources1', ((1, 'NumResources'),(1, 'ppResources'),(1, 'pResults'),)))
    return IDXGIDevice4
DXGI_FEATURE = Int32
DXGI_FEATURE_PRESENT_ALLOW_TEARING = 0
def _define_IDXGIFactory5_head():
    class IDXGIFactory5(win32more.Graphics.Dxgi.IDXGIFactory4_head):
        Guid = Guid('7632e1f5-ee65-4dca-87fd-84cd75f8838d')
    return IDXGIFactory5
def _define_IDXGIFactory5():
    IDXGIFactory5 = win32more.Graphics.Dxgi.IDXGIFactory5_head
    IDXGIFactory5.CheckFeatureSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.DXGI_FEATURE,c_void_p,UInt32, use_last_error=False)(28, 'CheckFeatureSupport', ((1, 'Feature'),(1, 'pFeatureSupportData'),(1, 'FeatureSupportDataSize'),)))
    return IDXGIFactory5
DXGI_ADAPTER_FLAG3 = UInt32
DXGI_ADAPTER_FLAG3_NONE = 0
DXGI_ADAPTER_FLAG3_REMOTE = 1
DXGI_ADAPTER_FLAG3_SOFTWARE = 2
DXGI_ADAPTER_FLAG3_ACG_COMPATIBLE = 4
DXGI_ADAPTER_FLAG3_SUPPORT_MONITORED_FENCES = 8
DXGI_ADAPTER_FLAG3_SUPPORT_NON_MONITORED_FENCES = 16
DXGI_ADAPTER_FLAG3_KEYED_MUTEX_CONFORMANCE = 32
DXGI_ADAPTER_FLAG3_FORCE_DWORD = 4294967295
def _define_DXGI_ADAPTER_DESC3_head():
    class DXGI_ADAPTER_DESC3(Structure):
        pass
    return DXGI_ADAPTER_DESC3
def _define_DXGI_ADAPTER_DESC3():
    DXGI_ADAPTER_DESC3 = win32more.Graphics.Dxgi.DXGI_ADAPTER_DESC3_head
    DXGI_ADAPTER_DESC3._fields_ = [
        ("Description", Char * 128),
        ("VendorId", UInt32),
        ("DeviceId", UInt32),
        ("SubSysId", UInt32),
        ("Revision", UInt32),
        ("DedicatedVideoMemory", UIntPtr),
        ("DedicatedSystemMemory", UIntPtr),
        ("SharedSystemMemory", UIntPtr),
        ("AdapterLuid", win32more.Foundation.LUID),
        ("Flags", win32more.Graphics.Dxgi.DXGI_ADAPTER_FLAG3),
        ("GraphicsPreemptionGranularity", win32more.Graphics.Dxgi.DXGI_GRAPHICS_PREEMPTION_GRANULARITY),
        ("ComputePreemptionGranularity", win32more.Graphics.Dxgi.DXGI_COMPUTE_PREEMPTION_GRANULARITY),
    ]
    return DXGI_ADAPTER_DESC3
def _define_IDXGIAdapter4_head():
    class IDXGIAdapter4(win32more.Graphics.Dxgi.IDXGIAdapter3_head):
        Guid = Guid('3c8d99d1-4fbf-4181-a82c-af66bf7bd24e')
    return IDXGIAdapter4
def _define_IDXGIAdapter4():
    IDXGIAdapter4 = win32more.Graphics.Dxgi.IDXGIAdapter4_head
    IDXGIAdapter4.GetDesc3 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_ADAPTER_DESC3_head), use_last_error=False)(18, 'GetDesc3', ((1, 'pDesc'),)))
    return IDXGIAdapter4
def _define_DXGI_OUTPUT_DESC1_head():
    class DXGI_OUTPUT_DESC1(Structure):
        pass
    return DXGI_OUTPUT_DESC1
def _define_DXGI_OUTPUT_DESC1():
    DXGI_OUTPUT_DESC1 = win32more.Graphics.Dxgi.DXGI_OUTPUT_DESC1_head
    DXGI_OUTPUT_DESC1._fields_ = [
        ("DeviceName", Char * 32),
        ("DesktopCoordinates", win32more.Foundation.RECT),
        ("AttachedToDesktop", win32more.Foundation.BOOL),
        ("Rotation", win32more.Graphics.Dxgi.Common.DXGI_MODE_ROTATION),
        ("Monitor", win32more.Graphics.Gdi.HMONITOR),
        ("BitsPerColor", UInt32),
        ("ColorSpace", win32more.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE),
        ("RedPrimary", Single * 2),
        ("GreenPrimary", Single * 2),
        ("BluePrimary", Single * 2),
        ("WhitePoint", Single * 2),
        ("MinLuminance", Single),
        ("MaxLuminance", Single),
        ("MaxFullFrameLuminance", Single),
    ]
    return DXGI_OUTPUT_DESC1
DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAGS = UInt32
DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAG_FULLSCREEN = 1
DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAG_WINDOWED = 2
DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAG_CURSOR_STRETCHED = 4
def _define_IDXGIOutput6_head():
    class IDXGIOutput6(win32more.Graphics.Dxgi.IDXGIOutput5_head):
        Guid = Guid('068346e8-aaec-4b84-add7-137f513f77a1')
    return IDXGIOutput6
def _define_IDXGIOutput6():
    IDXGIOutput6 = win32more.Graphics.Dxgi.IDXGIOutput6_head
    IDXGIOutput6.GetDesc1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.DXGI_OUTPUT_DESC1_head), use_last_error=False)(27, 'GetDesc1', ((1, 'pDesc'),)))
    IDXGIOutput6.CheckHardwareCompositionSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(28, 'CheckHardwareCompositionSupport', ((1, 'pFlags'),)))
    return IDXGIOutput6
DXGI_GPU_PREFERENCE = Int32
DXGI_GPU_PREFERENCE_UNSPECIFIED = 0
DXGI_GPU_PREFERENCE_MINIMUM_POWER = 1
DXGI_GPU_PREFERENCE_HIGH_PERFORMANCE = 2
def _define_IDXGIFactory6_head():
    class IDXGIFactory6(win32more.Graphics.Dxgi.IDXGIFactory5_head):
        Guid = Guid('c1b6694f-ff09-44a9-b03c-77900a0a1d17')
    return IDXGIFactory6
def _define_IDXGIFactory6():
    IDXGIFactory6 = win32more.Graphics.Dxgi.IDXGIFactory6_head
    IDXGIFactory6.EnumAdapterByGpuPreference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Dxgi.DXGI_GPU_PREFERENCE,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(29, 'EnumAdapterByGpuPreference', ((1, 'Adapter'),(1, 'GpuPreference'),(1, 'riid'),(1, 'ppvAdapter'),)))
    return IDXGIFactory6
def _define_IDXGIFactory7_head():
    class IDXGIFactory7(win32more.Graphics.Dxgi.IDXGIFactory6_head):
        Guid = Guid('a4966eed-76db-44da-84c1-ee9a7afb20a8')
    return IDXGIFactory7
def _define_IDXGIFactory7():
    IDXGIFactory7 = win32more.Graphics.Dxgi.IDXGIFactory7_head
    IDXGIFactory7.RegisterAdaptersChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(UInt32), use_last_error=False)(30, 'RegisterAdaptersChangedEvent', ((1, 'hEvent'),(1, 'pdwCookie'),)))
    IDXGIFactory7.UnregisterAdaptersChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(31, 'UnregisterAdaptersChangedEvent', ((1, 'dwCookie'),)))
    return IDXGIFactory7
DXGI_DEBUG_RLO_FLAGS = UInt32
DXGI_DEBUG_RLO_SUMMARY = 1
DXGI_DEBUG_RLO_DETAIL = 2
DXGI_DEBUG_RLO_IGNORE_INTERNAL = 4
DXGI_DEBUG_RLO_ALL = 7
DXGI_INFO_QUEUE_MESSAGE_CATEGORY = Int32
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_UNKNOWN = 0
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_MISCELLANEOUS = 1
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_INITIALIZATION = 2
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_CLEANUP = 3
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_COMPILATION = 4
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_STATE_CREATION = 5
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_STATE_SETTING = 6
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_STATE_GETTING = 7
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_RESOURCE_MANIPULATION = 8
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_EXECUTION = 9
DXGI_INFO_QUEUE_MESSAGE_CATEGORY_SHADER = 10
DXGI_INFO_QUEUE_MESSAGE_SEVERITY = Int32
DXGI_INFO_QUEUE_MESSAGE_SEVERITY_CORRUPTION = 0
DXGI_INFO_QUEUE_MESSAGE_SEVERITY_ERROR = 1
DXGI_INFO_QUEUE_MESSAGE_SEVERITY_WARNING = 2
DXGI_INFO_QUEUE_MESSAGE_SEVERITY_INFO = 3
DXGI_INFO_QUEUE_MESSAGE_SEVERITY_MESSAGE = 4
def _define_DXGI_INFO_QUEUE_MESSAGE_head():
    class DXGI_INFO_QUEUE_MESSAGE(Structure):
        pass
    return DXGI_INFO_QUEUE_MESSAGE
def _define_DXGI_INFO_QUEUE_MESSAGE():
    DXGI_INFO_QUEUE_MESSAGE = win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_head
    DXGI_INFO_QUEUE_MESSAGE._fields_ = [
        ("Producer", Guid),
        ("Category", win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY),
        ("Severity", win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY),
        ("ID", Int32),
        ("pDescription", c_char_p_no),
        ("DescriptionByteLength", UIntPtr),
    ]
    return DXGI_INFO_QUEUE_MESSAGE
def _define_DXGI_INFO_QUEUE_FILTER_DESC_head():
    class DXGI_INFO_QUEUE_FILTER_DESC(Structure):
        pass
    return DXGI_INFO_QUEUE_FILTER_DESC
def _define_DXGI_INFO_QUEUE_FILTER_DESC():
    DXGI_INFO_QUEUE_FILTER_DESC = win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER_DESC_head
    DXGI_INFO_QUEUE_FILTER_DESC._fields_ = [
        ("NumCategories", UInt32),
        ("pCategoryList", POINTER(win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY)),
        ("NumSeverities", UInt32),
        ("pSeverityList", POINTER(win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY)),
        ("NumIDs", UInt32),
        ("pIDList", POINTER(Int32)),
    ]
    return DXGI_INFO_QUEUE_FILTER_DESC
def _define_DXGI_INFO_QUEUE_FILTER_head():
    class DXGI_INFO_QUEUE_FILTER(Structure):
        pass
    return DXGI_INFO_QUEUE_FILTER
def _define_DXGI_INFO_QUEUE_FILTER():
    DXGI_INFO_QUEUE_FILTER = win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER_head
    DXGI_INFO_QUEUE_FILTER._fields_ = [
        ("AllowList", win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER_DESC),
        ("DenyList", win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER_DESC),
    ]
    return DXGI_INFO_QUEUE_FILTER
def _define_IDXGIInfoQueue_head():
    class IDXGIInfoQueue(win32more.System.Com.IUnknown_head):
        Guid = Guid('d67441c7-672a-476f-9e82-cd55b44949ce')
    return IDXGIInfoQueue
def _define_IDXGIInfoQueue():
    IDXGIInfoQueue = win32more.Graphics.Dxgi.IDXGIInfoQueue_head
    IDXGIInfoQueue.SetMessageCountLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt64, use_last_error=False)(3, 'SetMessageCountLimit', ((1, 'Producer'),(1, 'MessageCountLimit'),)))
    IDXGIInfoQueue.ClearStoredMessages = COMMETHOD(WINFUNCTYPE(Void,Guid, use_last_error=False)(4, 'ClearStoredMessages', ((1, 'Producer'),)))
    IDXGIInfoQueue.GetMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt64,POINTER(win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_head),POINTER(UIntPtr), use_last_error=False)(5, 'GetMessage', ((1, 'Producer'),(1, 'MessageIndex'),(1, 'pMessage'),(1, 'pMessageByteLength'),)))
    IDXGIInfoQueue.GetNumStoredMessagesAllowedByRetrievalFilters = COMMETHOD(WINFUNCTYPE(UInt64,Guid, use_last_error=False)(6, 'GetNumStoredMessagesAllowedByRetrievalFilters', ((1, 'Producer'),)))
    IDXGIInfoQueue.GetNumStoredMessages = COMMETHOD(WINFUNCTYPE(UInt64,Guid, use_last_error=False)(7, 'GetNumStoredMessages', ((1, 'Producer'),)))
    IDXGIInfoQueue.GetNumMessagesDiscardedByMessageCountLimit = COMMETHOD(WINFUNCTYPE(UInt64,Guid, use_last_error=False)(8, 'GetNumMessagesDiscardedByMessageCountLimit', ((1, 'Producer'),)))
    IDXGIInfoQueue.GetMessageCountLimit = COMMETHOD(WINFUNCTYPE(UInt64,Guid, use_last_error=False)(9, 'GetMessageCountLimit', ((1, 'Producer'),)))
    IDXGIInfoQueue.GetNumMessagesAllowedByStorageFilter = COMMETHOD(WINFUNCTYPE(UInt64,Guid, use_last_error=False)(10, 'GetNumMessagesAllowedByStorageFilter', ((1, 'Producer'),)))
    IDXGIInfoQueue.GetNumMessagesDeniedByStorageFilter = COMMETHOD(WINFUNCTYPE(UInt64,Guid, use_last_error=False)(11, 'GetNumMessagesDeniedByStorageFilter', ((1, 'Producer'),)))
    IDXGIInfoQueue.AddStorageFilterEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER_head), use_last_error=False)(12, 'AddStorageFilterEntries', ((1, 'Producer'),(1, 'pFilter'),)))
    IDXGIInfoQueue.GetStorageFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER_head),POINTER(UIntPtr), use_last_error=False)(13, 'GetStorageFilter', ((1, 'Producer'),(1, 'pFilter'),(1, 'pFilterByteLength'),)))
    IDXGIInfoQueue.ClearStorageFilter = COMMETHOD(WINFUNCTYPE(Void,Guid, use_last_error=False)(14, 'ClearStorageFilter', ((1, 'Producer'),)))
    IDXGIInfoQueue.PushEmptyStorageFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(15, 'PushEmptyStorageFilter', ((1, 'Producer'),)))
    IDXGIInfoQueue.PushDenyAllStorageFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(16, 'PushDenyAllStorageFilter', ((1, 'Producer'),)))
    IDXGIInfoQueue.PushCopyOfStorageFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(17, 'PushCopyOfStorageFilter', ((1, 'Producer'),)))
    IDXGIInfoQueue.PushStorageFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER_head), use_last_error=False)(18, 'PushStorageFilter', ((1, 'Producer'),(1, 'pFilter'),)))
    IDXGIInfoQueue.PopStorageFilter = COMMETHOD(WINFUNCTYPE(Void,Guid, use_last_error=False)(19, 'PopStorageFilter', ((1, 'Producer'),)))
    IDXGIInfoQueue.GetStorageFilterStackSize = COMMETHOD(WINFUNCTYPE(UInt32,Guid, use_last_error=False)(20, 'GetStorageFilterStackSize', ((1, 'Producer'),)))
    IDXGIInfoQueue.AddRetrievalFilterEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER_head), use_last_error=False)(21, 'AddRetrievalFilterEntries', ((1, 'Producer'),(1, 'pFilter'),)))
    IDXGIInfoQueue.GetRetrievalFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER_head),POINTER(UIntPtr), use_last_error=False)(22, 'GetRetrievalFilter', ((1, 'Producer'),(1, 'pFilter'),(1, 'pFilterByteLength'),)))
    IDXGIInfoQueue.ClearRetrievalFilter = COMMETHOD(WINFUNCTYPE(Void,Guid, use_last_error=False)(23, 'ClearRetrievalFilter', ((1, 'Producer'),)))
    IDXGIInfoQueue.PushEmptyRetrievalFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(24, 'PushEmptyRetrievalFilter', ((1, 'Producer'),)))
    IDXGIInfoQueue.PushDenyAllRetrievalFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(25, 'PushDenyAllRetrievalFilter', ((1, 'Producer'),)))
    IDXGIInfoQueue.PushCopyOfRetrievalFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(26, 'PushCopyOfRetrievalFilter', ((1, 'Producer'),)))
    IDXGIInfoQueue.PushRetrievalFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_FILTER_head), use_last_error=False)(27, 'PushRetrievalFilter', ((1, 'Producer'),(1, 'pFilter'),)))
    IDXGIInfoQueue.PopRetrievalFilter = COMMETHOD(WINFUNCTYPE(Void,Guid, use_last_error=False)(28, 'PopRetrievalFilter', ((1, 'Producer'),)))
    IDXGIInfoQueue.GetRetrievalFilterStackSize = COMMETHOD(WINFUNCTYPE(UInt32,Guid, use_last_error=False)(29, 'GetRetrievalFilterStackSize', ((1, 'Producer'),)))
    IDXGIInfoQueue.AddMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY,win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY,Int32,win32more.Foundation.PSTR, use_last_error=False)(30, 'AddMessage', ((1, 'Producer'),(1, 'Category'),(1, 'Severity'),(1, 'ID'),(1, 'pDescription'),)))
    IDXGIInfoQueue.AddApplicationMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY,win32more.Foundation.PSTR, use_last_error=False)(31, 'AddApplicationMessage', ((1, 'Severity'),(1, 'pDescription'),)))
    IDXGIInfoQueue.SetBreakOnCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY,win32more.Foundation.BOOL, use_last_error=False)(32, 'SetBreakOnCategory', ((1, 'Producer'),(1, 'Category'),(1, 'bEnable'),)))
    IDXGIInfoQueue.SetBreakOnSeverity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY,win32more.Foundation.BOOL, use_last_error=False)(33, 'SetBreakOnSeverity', ((1, 'Producer'),(1, 'Severity'),(1, 'bEnable'),)))
    IDXGIInfoQueue.SetBreakOnID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Int32,win32more.Foundation.BOOL, use_last_error=False)(34, 'SetBreakOnID', ((1, 'Producer'),(1, 'ID'),(1, 'bEnable'),)))
    IDXGIInfoQueue.GetBreakOnCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,Guid,win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_CATEGORY, use_last_error=False)(35, 'GetBreakOnCategory', ((1, 'Producer'),(1, 'Category'),)))
    IDXGIInfoQueue.GetBreakOnSeverity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,Guid,win32more.Graphics.Dxgi.DXGI_INFO_QUEUE_MESSAGE_SEVERITY, use_last_error=False)(36, 'GetBreakOnSeverity', ((1, 'Producer'),(1, 'Severity'),)))
    IDXGIInfoQueue.GetBreakOnID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,Guid,Int32, use_last_error=False)(37, 'GetBreakOnID', ((1, 'Producer'),(1, 'ID'),)))
    IDXGIInfoQueue.SetMuteDebugOutput = COMMETHOD(WINFUNCTYPE(Void,Guid,win32more.Foundation.BOOL, use_last_error=False)(38, 'SetMuteDebugOutput', ((1, 'Producer'),(1, 'bMute'),)))
    IDXGIInfoQueue.GetMuteDebugOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,Guid, use_last_error=False)(39, 'GetMuteDebugOutput', ((1, 'Producer'),)))
    return IDXGIInfoQueue
def _define_IDXGIDebug_head():
    class IDXGIDebug(win32more.System.Com.IUnknown_head):
        Guid = Guid('119e7452-de9e-40fe-8806-88f90c12b441')
    return IDXGIDebug
def _define_IDXGIDebug():
    IDXGIDebug = win32more.Graphics.Dxgi.IDXGIDebug_head
    IDXGIDebug.ReportLiveObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Graphics.Dxgi.DXGI_DEBUG_RLO_FLAGS, use_last_error=False)(3, 'ReportLiveObjects', ((1, 'apiid'),(1, 'flags'),)))
    return IDXGIDebug
def _define_IDXGIDebug1_head():
    class IDXGIDebug1(win32more.Graphics.Dxgi.IDXGIDebug_head):
        Guid = Guid('c5a05f0c-16f2-4adf-9f4d-a8c4d58ac550')
    return IDXGIDebug1
def _define_IDXGIDebug1():
    IDXGIDebug1 = win32more.Graphics.Dxgi.IDXGIDebug1_head
    IDXGIDebug1.EnableLeakTrackingForThread = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(4, 'EnableLeakTrackingForThread', ()))
    IDXGIDebug1.DisableLeakTrackingForThread = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(5, 'DisableLeakTrackingForThread', ()))
    IDXGIDebug1.IsLeakTrackingEnabledForThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(6, 'IsLeakTrackingEnabledForThread', ()))
    return IDXGIDebug1
DXGI_Message_Id = Int32
DXGI_MSG_IDXGISwapChain_CreationOrResizeBuffers_InvalidOutputWindow = 0
DXGI_MSG_IDXGISwapChain_CreationOrResizeBuffers_BufferWidthInferred = 1
DXGI_MSG_IDXGISwapChain_CreationOrResizeBuffers_BufferHeightInferred = 2
DXGI_MSG_IDXGISwapChain_CreationOrResizeBuffers_NoScanoutFlagChanged = 3
DXGI_MSG_IDXGISwapChain_Creation_MaxBufferCountExceeded = 4
DXGI_MSG_IDXGISwapChain_Creation_TooFewBuffers = 5
DXGI_MSG_IDXGISwapChain_Creation_NoOutputWindow = 6
DXGI_MSG_IDXGISwapChain_Destruction_OtherMethodsCalled = 7
DXGI_MSG_IDXGISwapChain_GetDesc_pDescIsNULL = 8
DXGI_MSG_IDXGISwapChain_GetBuffer_ppSurfaceIsNULL = 9
DXGI_MSG_IDXGISwapChain_GetBuffer_NoAllocatedBuffers = 10
DXGI_MSG_IDXGISwapChain_GetBuffer_iBufferMustBeZero = 11
DXGI_MSG_IDXGISwapChain_GetBuffer_iBufferOOB = 12
DXGI_MSG_IDXGISwapChain_GetContainingOutput_ppOutputIsNULL = 13
DXGI_MSG_IDXGISwapChain_Present_SyncIntervalOOB = 14
DXGI_MSG_IDXGISwapChain_Present_InvalidNonPreRotatedFlag = 15
DXGI_MSG_IDXGISwapChain_Present_NoAllocatedBuffers = 16
DXGI_MSG_IDXGISwapChain_Present_GetDXGIAdapterFailed = 17
DXGI_MSG_IDXGISwapChain_ResizeBuffers_BufferCountOOB = 18
DXGI_MSG_IDXGISwapChain_ResizeBuffers_UnreleasedReferences = 19
DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidSwapChainFlag = 20
DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidNonPreRotatedFlag = 21
DXGI_MSG_IDXGISwapChain_ResizeTarget_RefreshRateDivideByZero = 22
DXGI_MSG_IDXGISwapChain_SetFullscreenState_InvalidTarget = 23
DXGI_MSG_IDXGISwapChain_GetFrameStatistics_pStatsIsNULL = 24
DXGI_MSG_IDXGISwapChain_GetLastPresentCount_pLastPresentCountIsNULL = 25
DXGI_MSG_IDXGISwapChain_SetFullscreenState_RemoteNotSupported = 26
DXGI_MSG_IDXGIOutput_TakeOwnership_FailedToAcquireFullscreenMutex = 27
DXGI_MSG_IDXGIFactory_CreateSoftwareAdapter_ppAdapterInterfaceIsNULL = 28
DXGI_MSG_IDXGIFactory_EnumAdapters_ppAdapterInterfaceIsNULL = 29
DXGI_MSG_IDXGIFactory_CreateSwapChain_ppSwapChainIsNULL = 30
DXGI_MSG_IDXGIFactory_CreateSwapChain_pDescIsNULL = 31
DXGI_MSG_IDXGIFactory_CreateSwapChain_UnknownSwapEffect = 32
DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidFlags = 33
DXGI_MSG_IDXGIFactory_CreateSwapChain_NonPreRotatedFlagAndWindowed = 34
DXGI_MSG_IDXGIFactory_CreateSwapChain_NullDeviceInterface = 35
DXGI_MSG_IDXGIFactory_GetWindowAssociation_phWndIsNULL = 36
DXGI_MSG_IDXGIFactory_MakeWindowAssociation_InvalidFlags = 37
DXGI_MSG_IDXGISurface_Map_InvalidSurface = 38
DXGI_MSG_IDXGISurface_Map_FlagsSetToZero = 39
DXGI_MSG_IDXGISurface_Map_DiscardAndReadFlagSet = 40
DXGI_MSG_IDXGISurface_Map_DiscardButNotWriteFlagSet = 41
DXGI_MSG_IDXGISurface_Map_NoCPUAccess = 42
DXGI_MSG_IDXGISurface_Map_ReadFlagSetButCPUAccessIsDynamic = 43
DXGI_MSG_IDXGISurface_Map_DiscardFlagSetButCPUAccessIsNotDynamic = 44
DXGI_MSG_IDXGIOutput_GetDisplayModeList_pNumModesIsNULL = 45
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_ModeHasInvalidWidthOrHeight = 46
DXGI_MSG_IDXGIOutput_GetCammaControlCapabilities_NoOwnerDevice = 47
DXGI_MSG_IDXGIOutput_TakeOwnership_pDeviceIsNULL = 48
DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_NoOwnerDevice = 49
DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_pDestinationIsNULL = 50
DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_MapOfDestinationFailed = 51
DXGI_MSG_IDXGIOutput_GetFrameStatistics_NoOwnerDevice = 52
DXGI_MSG_IDXGIOutput_GetFrameStatistics_pStatsIsNULL = 53
DXGI_MSG_IDXGIOutput_SetGammaControl_NoOwnerDevice = 54
DXGI_MSG_IDXGIOutput_GetGammaControl_NoOwnerDevice = 55
DXGI_MSG_IDXGIOutput_GetGammaControl_NoGammaControls = 56
DXGI_MSG_IDXGIOutput_SetDisplaySurface_IDXGIResourceNotSupportedBypPrimary = 57
DXGI_MSG_IDXGIOutput_SetDisplaySurface_pPrimaryIsInvalid = 58
DXGI_MSG_IDXGIOutput_SetDisplaySurface_NoOwnerDevice = 59
DXGI_MSG_IDXGIOutput_TakeOwnership_RemoteDeviceNotSupported = 60
DXGI_MSG_IDXGIOutput_GetDisplayModeList_RemoteDeviceNotSupported = 61
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_RemoteDeviceNotSupported = 62
DXGI_MSG_IDXGIDevice_CreateSurface_InvalidParametersWithpSharedResource = 63
DXGI_MSG_IDXGIObject_GetPrivateData_puiDataSizeIsNULL = 64
DXGI_MSG_IDXGISwapChain_Creation_InvalidOutputWindow = 65
DXGI_MSG_IDXGISwapChain_Release_SwapChainIsFullscreen = 66
DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_InvalidTargetSurfaceFormat = 67
DXGI_MSG_IDXGIFactory_CreateSoftwareAdapter_ModuleIsNULL = 68
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_IDXGIDeviceNotSupportedBypConcernedDevice = 69
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_pModeToMatchOrpClosestMatchIsNULL = 70
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_ModeHasRefreshRateDenominatorZero = 71
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_UnknownFormatIsInvalidForConfiguration = 72
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_InvalidDisplayModeScanlineOrdering = 73
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_InvalidDisplayModeScaling = 74
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_InvalidDisplayModeFormatAndDeviceCombination = 75
DXGI_MSG_IDXGIFactory_Creation_CalledFromDllMain = 76
DXGI_MSG_IDXGISwapChain_SetFullscreenState_OutputNotOwnedBySwapChainDevice = 77
DXGI_MSG_IDXGISwapChain_Creation_InvalidWindowStyle = 78
DXGI_MSG_IDXGISwapChain_GetFrameStatistics_UnsupportedStatistics = 79
DXGI_MSG_IDXGISwapChain_GetContainingOutput_SwapchainAdapterDoesNotControlOutput = 80
DXGI_MSG_IDXGIOutput_SetOrGetGammaControl_pArrayIsNULL = 81
DXGI_MSG_IDXGISwapChain_SetFullscreenState_FullscreenInvalidForChildWindows = 82
DXGI_MSG_IDXGIFactory_Release_CalledFromDllMain = 83
DXGI_MSG_IDXGISwapChain_Present_UnreleasedHDC = 84
DXGI_MSG_IDXGISwapChain_ResizeBuffers_NonPreRotatedAndGDICompatibleFlags = 85
DXGI_MSG_IDXGIFactory_CreateSwapChain_NonPreRotatedAndGDICompatibleFlags = 86
DXGI_MSG_IDXGISurface1_GetDC_pHdcIsNULL = 87
DXGI_MSG_IDXGISurface1_GetDC_SurfaceNotTexture2D = 88
DXGI_MSG_IDXGISurface1_GetDC_GDICompatibleFlagNotSet = 89
DXGI_MSG_IDXGISurface1_GetDC_UnreleasedHDC = 90
DXGI_MSG_IDXGISurface_Map_NoCPUAccess2 = 91
DXGI_MSG_IDXGISurface1_ReleaseDC_GetDCNotCalled = 92
DXGI_MSG_IDXGISurface1_ReleaseDC_InvalidRectangleDimensions = 93
DXGI_MSG_IDXGIOutput_TakeOwnership_RemoteOutputNotSupported = 94
DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_RemoteOutputNotSupported = 95
DXGI_MSG_IDXGIOutput_GetDisplayModeList_RemoteOutputNotSupported = 96
DXGI_MSG_IDXGIFactory_CreateSwapChain_pDeviceHasMismatchedDXGIFactory = 97
DXGI_MSG_IDXGISwapChain_Present_NonOptimalFSConfiguration = 98
DXGI_MSG_IDXGIFactory_CreateSwapChain_FlipSequentialNotSupportedOnD3D10 = 99
DXGI_MSG_IDXGIFactory_CreateSwapChain_BufferCountOOBForFlipSequential = 100
DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidFormatForFlipSequential = 101
DXGI_MSG_IDXGIFactory_CreateSwapChain_MultiSamplingNotSupportedForFlipSequential = 102
DXGI_MSG_IDXGISwapChain_ResizeBuffers_BufferCountOOBForFlipSequential = 103
DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidFormatForFlipSequential = 104
DXGI_MSG_IDXGISwapChain_Present_PartialPresentationBeforeStandardPresentation = 105
DXGI_MSG_IDXGISwapChain_Present_FullscreenPartialPresentIsInvalid = 106
DXGI_MSG_IDXGISwapChain_Present_InvalidPresentTestOrDoNotSequenceFlag = 107
DXGI_MSG_IDXGISwapChain_Present_ScrollInfoWithNoDirtyRectsSpecified = 108
DXGI_MSG_IDXGISwapChain_Present_EmptyScrollRect = 109
DXGI_MSG_IDXGISwapChain_Present_ScrollRectOutOfBackbufferBounds = 110
DXGI_MSG_IDXGISwapChain_Present_ScrollRectOutOfBackbufferBoundsWithOffset = 111
DXGI_MSG_IDXGISwapChain_Present_EmptyDirtyRect = 112
DXGI_MSG_IDXGISwapChain_Present_DirtyRectOutOfBackbufferBounds = 113
DXGI_MSG_IDXGIFactory_CreateSwapChain_UnsupportedBufferUsageFlags = 114
DXGI_MSG_IDXGISwapChain_Present_DoNotSequenceFlagSetButPreviousBufferIsUndefined = 115
DXGI_MSG_IDXGISwapChain_Present_UnsupportedFlags = 116
DXGI_MSG_IDXGISwapChain_Present_FlipModelChainMustResizeOrCreateOnFSTransition = 117
DXGI_MSG_IDXGIFactory_CreateSwapChain_pRestrictToOutputFromOtherIDXGIFactory = 118
DXGI_MSG_IDXGIFactory_CreateSwapChain_RestrictOutputNotSupportedOnAdapter = 119
DXGI_MSG_IDXGISwapChain_Present_RestrictToOutputFlagSetButInvalidpRestrictToOutput = 120
DXGI_MSG_IDXGISwapChain_Present_RestrictToOutputFlagdWithFullscreen = 121
DXGI_MSG_IDXGISwapChain_Present_RestrictOutputFlagWithStaleSwapChain = 122
DXGI_MSG_IDXGISwapChain_Present_OtherFlagsCausingInvalidPresentTestFlag = 123
DXGI_MSG_IDXGIFactory_CreateSwapChain_UnavailableInSession0 = 124
DXGI_MSG_IDXGIFactory_MakeWindowAssociation_UnavailableInSession0 = 125
DXGI_MSG_IDXGIFactory_GetWindowAssociation_UnavailableInSession0 = 126
DXGI_MSG_IDXGIAdapter_EnumOutputs_UnavailableInSession0 = 127
DXGI_MSG_IDXGISwapChain_CreationOrSetFullscreenState_StereoDisabled = 128
DXGI_MSG_IDXGIFactory2_UnregisterStatus_CookieNotFound = 129
DXGI_MSG_IDXGISwapChain_Present_ProtectedContentInWindowedModeWithoutFSOrOverlay = 130
DXGI_MSG_IDXGISwapChain_Present_ProtectedContentInWindowedModeWithoutFlipSequential = 131
DXGI_MSG_IDXGISwapChain_Present_ProtectedContentWithRDPDriver = 132
DXGI_MSG_IDXGISwapChain_Present_ProtectedContentInWindowedModeWithDWMOffOrInvalidDisplayAffinity = 133
DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_WidthOrHeightIsZero = 134
DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_OnlyFlipSequentialSupported = 135
DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_UnsupportedOnAdapter = 136
DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_UnsupportedOnWindows7 = 137
DXGI_MSG_IDXGISwapChain_SetFullscreenState_FSTransitionWithCompositionSwapChain = 138
DXGI_MSG_IDXGISwapChain_ResizeTarget_InvalidWithCompositionSwapChain = 139
DXGI_MSG_IDXGISwapChain_ResizeBuffers_WidthOrHeightIsZero = 140
DXGI_MSG_IDXGIFactory_CreateSwapChain_ScalingNoneIsFlipModelOnly = 141
DXGI_MSG_IDXGIFactory_CreateSwapChain_ScalingUnrecognized = 142
DXGI_MSG_IDXGIFactory_CreateSwapChain_DisplayOnlyFullscreenUnsupported = 143
DXGI_MSG_IDXGIFactory_CreateSwapChain_DisplayOnlyUnsupported = 144
DXGI_MSG_IDXGISwapChain_Present_RestartIsFullscreenOnly = 145
DXGI_MSG_IDXGISwapChain_Present_ProtectedWindowlessPresentationRequiresDisplayOnly = 146
DXGI_MSG_IDXGISwapChain_SetFullscreenState_DisplayOnlyUnsupported = 147
DXGI_MSG_IDXGISwapChain1_SetBackgroundColor_OutOfRange = 148
DXGI_MSG_IDXGISwapChain_ResizeBuffers_DisplayOnlyFullscreenUnsupported = 149
DXGI_MSG_IDXGISwapChain_ResizeBuffers_DisplayOnlyUnsupported = 150
DXGI_MSG_IDXGISwapchain_Present_ScrollUnsupported = 151
DXGI_MSG_IDXGISwapChain1_SetRotation_UnsupportedOS = 152
DXGI_MSG_IDXGISwapChain1_GetRotation_UnsupportedOS = 153
DXGI_MSG_IDXGISwapchain_Present_FullscreenRotation = 154
DXGI_MSG_IDXGISwapChain_Present_PartialPresentationWithMSAABuffers = 155
DXGI_MSG_IDXGISwapChain1_SetRotation_FlipSequentialRequired = 156
DXGI_MSG_IDXGISwapChain1_SetRotation_InvalidRotation = 157
DXGI_MSG_IDXGISwapChain1_GetRotation_FlipSequentialRequired = 158
DXGI_MSG_IDXGISwapChain_GetHwnd_WrongType = 159
DXGI_MSG_IDXGISwapChain_GetCompositionSurface_WrongType = 160
DXGI_MSG_IDXGISwapChain_GetCoreWindow_WrongType = 161
DXGI_MSG_IDXGISwapChain_GetFullscreenDesc_NonHwnd = 162
DXGI_MSG_IDXGISwapChain_SetFullscreenState_CoreWindow = 163
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_UnsupportedOnWindows7 = 164
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_pWindowIsNULL = 165
DXGI_MSG_IDXGIFactory_CreateSwapChain_FSUnsupportedForModernApps = 166
DXGI_MSG_IDXGIFactory_MakeWindowAssociation_ModernApp = 167
DXGI_MSG_IDXGISwapChain_ResizeTarget_ModernApp = 168
DXGI_MSG_IDXGISwapChain_ResizeTarget_pNewTargetParametersIsNULL = 169
DXGI_MSG_IDXGIOutput_SetDisplaySurface_ModernApp = 170
DXGI_MSG_IDXGIOutput_TakeOwnership_ModernApp = 171
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_pWindowIsInvalid = 172
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCompositionSurface_InvalidHandle = 173
DXGI_MSG_IDXGISurface1_GetDC_ModernApp = 174
DXGI_MSG_IDXGIFactory_CreateSwapChain_ScalingNoneRequiresWindows8OrNewer = 175
DXGI_MSG_IDXGISwapChain_Present_TemporaryMonoAndPreferRight = 176
DXGI_MSG_IDXGISwapChain_Present_TemporaryMonoOrPreferRightWithDoNotSequence = 177
DXGI_MSG_IDXGISwapChain_Present_TemporaryMonoOrPreferRightWithoutStereo = 178
DXGI_MSG_IDXGISwapChain_Present_TemporaryMonoUnsupported = 179
DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_ArraySizeMismatch = 180
DXGI_MSG_IDXGISwapChain_Present_PartialPresentationWithSwapEffectDiscard = 181
DXGI_MSG_IDXGIFactory_CreateSwapChain_AlphaUnrecognized = 182
DXGI_MSG_IDXGIFactory_CreateSwapChain_AlphaIsWindowlessOnly = 183
DXGI_MSG_IDXGIFactory_CreateSwapChain_AlphaIsFlipModelOnly = 184
DXGI_MSG_IDXGIFactory_CreateSwapChain_RestrictToOutputAdapterMismatch = 185
DXGI_MSG_IDXGIFactory_CreateSwapChain_DisplayOnlyOnLegacy = 186
DXGI_MSG_IDXGISwapChain_ResizeBuffers_DisplayOnlyOnLegacy = 187
DXGI_MSG_IDXGIResource1_CreateSubresourceSurface_InvalidIndex = 188
DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_InvalidScaling = 189
DXGI_MSG_IDXGIFactory_CreateSwapChainForCoreWindow_InvalidSwapEffect = 190
DXGI_MSG_IDXGIResource1_CreateSharedHandle_UnsupportedOS = 191
DXGI_MSG_IDXGIFactory2_RegisterOcclusionStatusWindow_UnsupportedOS = 192
DXGI_MSG_IDXGIFactory2_RegisterOcclusionStatusEvent_UnsupportedOS = 193
DXGI_MSG_IDXGIOutput1_DuplicateOutput_UnsupportedOS = 194
DXGI_MSG_IDXGIDisplayControl_IsStereoEnabled_UnsupportedOS = 195
DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_InvalidAlphaMode = 196
DXGI_MSG_IDXGIFactory_GetSharedResourceAdapterLuid_InvalidResource = 197
DXGI_MSG_IDXGIFactory_GetSharedResourceAdapterLuid_InvalidLUID = 198
DXGI_MSG_IDXGIFactory_GetSharedResourceAdapterLuid_UnsupportedOS = 199
DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_2DOnly = 200
DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_StagingOnly = 201
DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_NeedCPUAccessWrite = 202
DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_NoShared = 203
DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_OnlyMipLevels1 = 204
DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_MappedOrOfferedResource = 205
DXGI_MSG_IDXGISwapChain_SetFullscreenState_FSUnsupportedForModernApps = 206
DXGI_MSG_IDXGIFactory_CreateSwapChain_FailedToGoFSButNonPreRotated = 207
DXGI_MSG_IDXGIFactory_CreateSwapChainOrRegisterOcclusionStatus_BlitModelUsedWhileRegisteredForOcclusionStatusEvents = 208
DXGI_MSG_IDXGISwapChain_Present_BlitModelUsedWhileRegisteredForOcclusionStatusEvents = 209
DXGI_MSG_IDXGIFactory_CreateSwapChain_WaitableSwapChainsAreFlipModelOnly = 210
DXGI_MSG_IDXGIFactory_CreateSwapChain_WaitableSwapChainsAreNotFullscreen = 211
DXGI_MSG_IDXGISwapChain_SetFullscreenState_Waitable = 212
DXGI_MSG_IDXGISwapChain_ResizeBuffers_CannotAddOrRemoveWaitableFlag = 213
DXGI_MSG_IDXGISwapChain_GetFrameLatencyWaitableObject_OnlyWaitable = 214
DXGI_MSG_IDXGISwapChain_GetMaximumFrameLatency_OnlyWaitable = 215
DXGI_MSG_IDXGISwapChain_GetMaximumFrameLatency_pMaxLatencyIsNULL = 216
DXGI_MSG_IDXGISwapChain_SetMaximumFrameLatency_OnlyWaitable = 217
DXGI_MSG_IDXGISwapChain_SetMaximumFrameLatency_MaxLatencyIsOutOfBounds = 218
DXGI_MSG_IDXGIFactory_CreateSwapChain_ForegroundIsCoreWindowOnly = 219
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_ForegroundUnsupportedOnAdapter = 220
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_InvalidScaling = 221
DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_InvalidAlphaMode = 222
DXGI_MSG_IDXGISwapChain_ResizeBuffers_CannotAddOrRemoveForegroundFlag = 223
DXGI_MSG_IDXGISwapChain_SetMatrixTransform_MatrixPointerCannotBeNull = 224
DXGI_MSG_IDXGISwapChain_SetMatrixTransform_RequiresCompositionSwapChain = 225
DXGI_MSG_IDXGISwapChain_SetMatrixTransform_MatrixMustBeFinite = 226
DXGI_MSG_IDXGISwapChain_SetMatrixTransform_MatrixMustBeTranslateAndOrScale = 227
DXGI_MSG_IDXGISwapChain_GetMatrixTransform_MatrixPointerCannotBeNull = 228
DXGI_MSG_IDXGISwapChain_GetMatrixTransform_RequiresCompositionSwapChain = 229
DXGI_MSG_DXGIGetDebugInterface1_NULL_ppDebug = 230
DXGI_MSG_DXGIGetDebugInterface1_InvalidFlags = 231
DXGI_MSG_IDXGISwapChain_Present_Decode = 232
DXGI_MSG_IDXGISwapChain_ResizeBuffers_Decode = 233
DXGI_MSG_IDXGISwapChain_SetSourceSize_FlipModel = 234
DXGI_MSG_IDXGISwapChain_SetSourceSize_Decode = 235
DXGI_MSG_IDXGISwapChain_SetSourceSize_WidthHeight = 236
DXGI_MSG_IDXGISwapChain_GetSourceSize_NullPointers = 237
DXGI_MSG_IDXGISwapChain_GetSourceSize_Decode = 238
DXGI_MSG_IDXGIDecodeSwapChain_SetColorSpace_InvalidFlags = 239
DXGI_MSG_IDXGIDecodeSwapChain_SetSourceRect_InvalidRect = 240
DXGI_MSG_IDXGIDecodeSwapChain_SetTargetRect_InvalidRect = 241
DXGI_MSG_IDXGIDecodeSwapChain_SetDestSize_InvalidSize = 242
DXGI_MSG_IDXGIDecodeSwapChain_GetSourceRect_InvalidPointer = 243
DXGI_MSG_IDXGIDecodeSwapChain_GetTargetRect_InvalidPointer = 244
DXGI_MSG_IDXGIDecodeSwapChain_GetDestSize_InvalidPointer = 245
DXGI_MSG_IDXGISwapChain_PresentBuffer_YUV = 246
DXGI_MSG_IDXGISwapChain_SetSourceSize_YUV = 247
DXGI_MSG_IDXGISwapChain_GetSourceSize_YUV = 248
DXGI_MSG_IDXGISwapChain_SetMatrixTransform_YUV = 249
DXGI_MSG_IDXGISwapChain_GetMatrixTransform_YUV = 250
DXGI_MSG_IDXGISwapChain_Present_PartialPresentation_YUV = 251
DXGI_MSG_IDXGISwapChain_ResizeBuffers_CannotAddOrRemoveFlag_YUV = 252
DXGI_MSG_IDXGISwapChain_ResizeBuffers_Alignment_YUV = 253
DXGI_MSG_IDXGIFactory_CreateSwapChain_ShaderInputUnsupported_YUV = 254
DXGI_MSG_IDXGIOutput3_CheckOverlaySupport_NullPointers = 255
DXGI_MSG_IDXGIOutput3_CheckOverlaySupport_IDXGIDeviceNotSupportedBypConcernedDevice = 256
DXGI_MSG_IDXGIAdapter_EnumOutputs2_InvalidEnumOutputs2Flag = 257
DXGI_MSG_IDXGISwapChain_CreationOrSetFullscreenState_FSUnsupportedForFlipDiscard = 258
DXGI_MSG_IDXGIOutput4_CheckOverlayColorSpaceSupport_NullPointers = 259
DXGI_MSG_IDXGIOutput4_CheckOverlayColorSpaceSupport_IDXGIDeviceNotSupportedBypConcernedDevice = 260
DXGI_MSG_IDXGISwapChain3_CheckColorSpaceSupport_NullPointers = 261
DXGI_MSG_IDXGISwapChain3_SetColorSpace1_InvalidColorSpace = 262
DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidHwProtect = 263
DXGI_MSG_IDXGIFactory_CreateSwapChain_HwProtectUnsupported = 264
DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidHwProtect = 265
DXGI_MSG_IDXGISwapChain_ResizeBuffers_HwProtectUnsupported = 266
DXGI_MSG_IDXGISwapChain_ResizeBuffers1_D3D12Only = 267
DXGI_MSG_IDXGISwapChain_ResizeBuffers1_FlipModel = 268
DXGI_MSG_IDXGISwapChain_ResizeBuffers1_NodeMaskAndQueueRequired = 269
DXGI_MSG_IDXGISwapChain_CreateSwapChain_InvalidHwProtectGdiFlag = 270
DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidHwProtectGdiFlag = 271
DXGI_MSG_IDXGIFactory_CreateSwapChain_10BitFormatNotSupported = 272
DXGI_MSG_IDXGIFactory_CreateSwapChain_FlipSwapEffectRequired = 273
DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidDevice = 274
DXGI_MSG_IDXGIOutput_TakeOwnership_Unsupported = 275
DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidQueue = 276
DXGI_MSG_IDXGISwapChain3_ResizeBuffers1_InvalidQueue = 277
DXGI_MSG_IDXGIFactory_CreateSwapChainForHwnd_InvalidScaling = 278
DXGI_MSG_IDXGISwapChain3_SetHDRMetaData_InvalidSize = 279
DXGI_MSG_IDXGISwapChain3_SetHDRMetaData_InvalidPointer = 280
DXGI_MSG_IDXGISwapChain3_SetHDRMetaData_InvalidType = 281
DXGI_MSG_IDXGISwapChain_Present_FullscreenAllowTearingIsInvalid = 282
DXGI_MSG_IDXGISwapChain_Present_AllowTearingRequiresPresentIntervalZero = 283
DXGI_MSG_IDXGISwapChain_Present_AllowTearingRequiresCreationFlag = 284
DXGI_MSG_IDXGISwapChain_ResizeBuffers_CannotAddOrRemoveAllowTearingFlag = 285
DXGI_MSG_IDXGIFactory_CreateSwapChain_AllowTearingFlagIsFlipModelOnly = 286
DXGI_MSG_IDXGIFactory_CheckFeatureSupport_InvalidFeature = 287
DXGI_MSG_IDXGIFactory_CheckFeatureSupport_InvalidSize = 288
DXGI_MSG_IDXGIOutput6_CheckHardwareCompositionSupport_NullPointer = 289
DXGI_MSG_IDXGISwapChain_SetFullscreenState_PerMonitorDpiShimApplied = 290
DXGI_MSG_IDXGIOutput_DuplicateOutput_PerMonitorDpiShimApplied = 291
DXGI_MSG_IDXGIOutput_DuplicateOutput1_PerMonitorDpiRequired = 292
DXGI_MSG_IDXGIFactory7_UnregisterAdaptersChangedEvent_CookieNotFound = 293
DXGI_MSG_IDXGIFactory_CreateSwapChain_LegacyBltModelSwapEffect = 294
DXGI_MSG_IDXGISwapChain4_SetHDRMetaData_MetadataUnchanged = 295
DXGI_MSG_IDXGISwapChain_Present_11On12_Released_Resource = 296
DXGI_MSG_IDXGIFactory_CreateSwapChain_MultipleSwapchainRefToSurface_DeferredDtr = 297
DXGI_MSG_IDXGIFactory_MakeWindowAssociation_NoOpBehavior = 298
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_NotForegroundWindow = 1000
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_DISCARD_BufferCount = 1001
DXGI_MSG_Phone_IDXGISwapChain_SetFullscreenState_NotAvailable = 1002
DXGI_MSG_Phone_IDXGISwapChain_ResizeBuffers_NotAvailable = 1003
DXGI_MSG_Phone_IDXGISwapChain_ResizeTarget_NotAvailable = 1004
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidLayerIndex = 1005
DXGI_MSG_Phone_IDXGISwapChain_Present_MultipleLayerIndex = 1006
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidLayerFlag = 1007
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidRotation = 1008
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidBlend = 1009
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidResource = 1010
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidMultiPlaneOverlayResource = 1011
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidIndexForPrimary = 1012
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidIndexForOverlay = 1013
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidSubResourceIndex = 1014
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidSourceRect = 1015
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidDestinationRect = 1016
DXGI_MSG_Phone_IDXGISwapChain_Present_MultipleResource = 1017
DXGI_MSG_Phone_IDXGISwapChain_Present_NotSharedResource = 1018
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidFlag = 1019
DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidInterval = 1020
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_MSAA_NotSupported = 1021
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_ScalingAspectRatioStretch_Supported_ModernApp = 1022
DXGI_MSG_Phone_IDXGISwapChain_GetFrameStatistics_NotAvailable_ModernApp = 1023
DXGI_MSG_Phone_IDXGISwapChain_Present_ReplaceInterval0With1 = 1024
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_FailedRegisterWithCompositor = 1025
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_NotForegroundWindow_AtRendering = 1026
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_FLIP_SEQUENTIAL_BufferCount = 1027
DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_FLIP_Modern_CoreWindow_Only = 1028
DXGI_MSG_Phone_IDXGISwapChain_Present1_RequiresOverlays = 1029
DXGI_MSG_Phone_IDXGISwapChain_SetBackgroundColor_FlipSequentialRequired = 1030
DXGI_MSG_Phone_IDXGISwapChain_GetBackgroundColor_FlipSequentialRequired = 1031
def _define_IDXGraphicsAnalysis_head():
    class IDXGraphicsAnalysis(win32more.System.Com.IUnknown_head):
        Guid = Guid('9f251514-9d4d-4902-9d60-18988ab7d4b5')
    return IDXGraphicsAnalysis
def _define_IDXGraphicsAnalysis():
    IDXGraphicsAnalysis = win32more.Graphics.Dxgi.IDXGraphicsAnalysis_head
    IDXGraphicsAnalysis.BeginCapture = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(3, 'BeginCapture', ()))
    IDXGraphicsAnalysis.EndCapture = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(4, 'EndCapture', ()))
    return IDXGraphicsAnalysis
def _define_CreateDXGIFactory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("CreateDXGIFactory", windll["dxgi"]), ((1, 'riid'),(1, 'ppFactory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDXGIFactory1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("CreateDXGIFactory1", windll["dxgi"]), ((1, 'riid'),(1, 'ppFactory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDXGIFactory2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("CreateDXGIFactory2", windll["dxgi"]), ((1, 'Flags'),(1, 'riid'),(1, 'ppFactory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DXGIGetDebugInterface1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("DXGIGetDebugInterface1", windll["dxgi"]), ((1, 'Flags'),(1, 'riid'),(1, 'pDebug'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DXGIDeclareAdapterRemovalSupport():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("DXGIDeclareAdapterRemovalSupport", windll["dxgi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "DXGI_USAGE_SHADER_INPUT",
    "DXGI_USAGE_RENDER_TARGET_OUTPUT",
    "DXGI_USAGE_BACK_BUFFER",
    "DXGI_USAGE_SHARED",
    "DXGI_USAGE_READ_ONLY",
    "DXGI_USAGE_DISCARD_ON_PRESENT",
    "DXGI_USAGE_UNORDERED_ACCESS",
    "DXGI_MAP_READ",
    "DXGI_MAP_WRITE",
    "DXGI_MAP_DISCARD",
    "DXGI_ENUM_MODES_INTERLACED",
    "DXGI_ENUM_MODES_SCALING",
    "DXGI_MAX_SWAP_CHAIN_BUFFERS",
    "DXGI_PRESENT_TEST",
    "DXGI_PRESENT_DO_NOT_SEQUENCE",
    "DXGI_PRESENT_RESTART",
    "DXGI_PRESENT_DO_NOT_WAIT",
    "DXGI_PRESENT_STEREO_PREFER_RIGHT",
    "DXGI_PRESENT_STEREO_TEMPORARY_MONO",
    "DXGI_PRESENT_RESTRICT_TO_OUTPUT",
    "DXGI_PRESENT_USE_DURATION",
    "DXGI_PRESENT_ALLOW_TEARING",
    "DXGI_MWA_NO_WINDOW_CHANGES",
    "DXGI_MWA_NO_ALT_ENTER",
    "DXGI_MWA_NO_PRINT_SCREEN",
    "DXGI_MWA_VALID",
    "DXGI_ENUM_MODES_STEREO",
    "DXGI_ENUM_MODES_DISABLED_STEREO",
    "DXGI_SHARED_RESOURCE_READ",
    "DXGI_SHARED_RESOURCE_WRITE",
    "DXGI_DEBUG_BINARY_VERSION",
    "DXGI_DEBUG_ALL",
    "DXGI_DEBUG_DX",
    "DXGI_DEBUG_DXGI",
    "DXGI_DEBUG_APP",
    "DXGI_INFO_QUEUE_MESSAGE_ID_STRING_FROM_APPLICATION",
    "DXGI_INFO_QUEUE_DEFAULT_MESSAGE_COUNT_LIMIT",
    "DXGI_CREATE_FACTORY_DEBUG",
    "DXGI_ERROR_INVALID_CALL",
    "DXGI_ERROR_NOT_FOUND",
    "DXGI_ERROR_MORE_DATA",
    "DXGI_ERROR_UNSUPPORTED",
    "DXGI_ERROR_DEVICE_REMOVED",
    "DXGI_ERROR_DEVICE_HUNG",
    "DXGI_ERROR_DEVICE_RESET",
    "DXGI_ERROR_WAS_STILL_DRAWING",
    "DXGI_ERROR_FRAME_STATISTICS_DISJOINT",
    "DXGI_ERROR_GRAPHICS_VIDPN_SOURCE_IN_USE",
    "DXGI_ERROR_DRIVER_INTERNAL_ERROR",
    "DXGI_ERROR_NONEXCLUSIVE",
    "DXGI_ERROR_NOT_CURRENTLY_AVAILABLE",
    "DXGI_ERROR_REMOTE_CLIENT_DISCONNECTED",
    "DXGI_ERROR_REMOTE_OUTOFMEMORY",
    "DXGI_ERROR_ACCESS_LOST",
    "DXGI_ERROR_WAIT_TIMEOUT",
    "DXGI_ERROR_SESSION_DISCONNECTED",
    "DXGI_ERROR_RESTRICT_TO_OUTPUT_STALE",
    "DXGI_ERROR_CANNOT_PROTECT_CONTENT",
    "DXGI_ERROR_ACCESS_DENIED",
    "DXGI_ERROR_NAME_ALREADY_EXISTS",
    "DXGI_ERROR_SDK_COMPONENT_MISSING",
    "DXGI_ERROR_NOT_CURRENT",
    "DXGI_ERROR_HW_PROTECTION_OUTOFMEMORY",
    "DXGI_ERROR_DYNAMIC_CODE_POLICY_VIOLATION",
    "DXGI_ERROR_NON_COMPOSITED_UI",
    "DXGI_ERROR_MODE_CHANGE_IN_PROGRESS",
    "DXGI_ERROR_CACHE_CORRUPT",
    "DXGI_ERROR_CACHE_FULL",
    "DXGI_ERROR_CACHE_HASH_COLLISION",
    "DXGI_ERROR_ALREADY_EXISTS",
    "DXGI_RGBA",
    "DXGI_RESOURCE_PRIORITY",
    "DXGI_RESOURCE_PRIORITY_MINIMUM",
    "DXGI_RESOURCE_PRIORITY_LOW",
    "DXGI_RESOURCE_PRIORITY_NORMAL",
    "DXGI_RESOURCE_PRIORITY_HIGH",
    "DXGI_RESOURCE_PRIORITY_MAXIMUM",
    "DXGI_FRAME_STATISTICS",
    "DXGI_MAPPED_RECT",
    "DXGI_ADAPTER_DESC",
    "DXGI_OUTPUT_DESC",
    "DXGI_SHARED_RESOURCE",
    "DXGI_RESIDENCY",
    "DXGI_RESIDENCY_FULLY_RESIDENT",
    "DXGI_RESIDENCY_RESIDENT_IN_SHARED_MEMORY",
    "DXGI_RESIDENCY_EVICTED_TO_DISK",
    "DXGI_SURFACE_DESC",
    "DXGI_SWAP_EFFECT",
    "DXGI_SWAP_EFFECT_DISCARD",
    "DXGI_SWAP_EFFECT_SEQUENTIAL",
    "DXGI_SWAP_EFFECT_FLIP_SEQUENTIAL",
    "DXGI_SWAP_EFFECT_FLIP_DISCARD",
    "DXGI_SWAP_CHAIN_FLAG",
    "DXGI_SWAP_CHAIN_FLAG_NONPREROTATED",
    "DXGI_SWAP_CHAIN_FLAG_ALLOW_MODE_SWITCH",
    "DXGI_SWAP_CHAIN_FLAG_GDI_COMPATIBLE",
    "DXGI_SWAP_CHAIN_FLAG_RESTRICTED_CONTENT",
    "DXGI_SWAP_CHAIN_FLAG_RESTRICT_SHARED_RESOURCE_DRIVER",
    "DXGI_SWAP_CHAIN_FLAG_DISPLAY_ONLY",
    "DXGI_SWAP_CHAIN_FLAG_FRAME_LATENCY_WAITABLE_OBJECT",
    "DXGI_SWAP_CHAIN_FLAG_FOREGROUND_LAYER",
    "DXGI_SWAP_CHAIN_FLAG_FULLSCREEN_VIDEO",
    "DXGI_SWAP_CHAIN_FLAG_YUV_VIDEO",
    "DXGI_SWAP_CHAIN_FLAG_HW_PROTECTED",
    "DXGI_SWAP_CHAIN_FLAG_ALLOW_TEARING",
    "DXGI_SWAP_CHAIN_FLAG_RESTRICTED_TO_ALL_HOLOGRAPHIC_DISPLAYS",
    "DXGI_SWAP_CHAIN_DESC",
    "IDXGIObject",
    "IDXGIDeviceSubObject",
    "IDXGIResource",
    "IDXGIKeyedMutex",
    "IDXGISurface",
    "IDXGISurface1",
    "IDXGIAdapter",
    "IDXGIOutput",
    "IDXGISwapChain",
    "IDXGIFactory",
    "IDXGIDevice",
    "DXGI_ADAPTER_FLAG",
    "DXGI_ADAPTER_FLAG_NONE",
    "DXGI_ADAPTER_FLAG_REMOTE",
    "DXGI_ADAPTER_FLAG_SOFTWARE",
    "DXGI_ADAPTER_DESC1",
    "DXGI_DISPLAY_COLOR_SPACE",
    "IDXGIFactory1",
    "IDXGIAdapter1",
    "IDXGIDevice1",
    "IDXGIDisplayControl",
    "DXGI_OUTDUPL_MOVE_RECT",
    "DXGI_OUTDUPL_DESC",
    "DXGI_OUTDUPL_POINTER_POSITION",
    "DXGI_OUTDUPL_POINTER_SHAPE_TYPE",
    "DXGI_OUTDUPL_POINTER_SHAPE_TYPE_MONOCHROME",
    "DXGI_OUTDUPL_POINTER_SHAPE_TYPE_COLOR",
    "DXGI_OUTDUPL_POINTER_SHAPE_TYPE_MASKED_COLOR",
    "DXGI_OUTDUPL_POINTER_SHAPE_INFO",
    "DXGI_OUTDUPL_FRAME_INFO",
    "IDXGIOutputDuplication",
    "IDXGISurface2",
    "IDXGIResource1",
    "DXGI_OFFER_RESOURCE_PRIORITY",
    "DXGI_OFFER_RESOURCE_PRIORITY_LOW",
    "DXGI_OFFER_RESOURCE_PRIORITY_NORMAL",
    "DXGI_OFFER_RESOURCE_PRIORITY_HIGH",
    "IDXGIDevice2",
    "DXGI_MODE_DESC1",
    "DXGI_SCALING",
    "DXGI_SCALING_STRETCH",
    "DXGI_SCALING_NONE",
    "DXGI_SCALING_ASPECT_RATIO_STRETCH",
    "DXGI_SWAP_CHAIN_DESC1",
    "DXGI_SWAP_CHAIN_FULLSCREEN_DESC",
    "DXGI_PRESENT_PARAMETERS",
    "IDXGISwapChain1",
    "IDXGIFactory2",
    "DXGI_GRAPHICS_PREEMPTION_GRANULARITY",
    "DXGI_GRAPHICS_PREEMPTION_DMA_BUFFER_BOUNDARY",
    "DXGI_GRAPHICS_PREEMPTION_PRIMITIVE_BOUNDARY",
    "DXGI_GRAPHICS_PREEMPTION_TRIANGLE_BOUNDARY",
    "DXGI_GRAPHICS_PREEMPTION_PIXEL_BOUNDARY",
    "DXGI_GRAPHICS_PREEMPTION_INSTRUCTION_BOUNDARY",
    "DXGI_COMPUTE_PREEMPTION_GRANULARITY",
    "DXGI_COMPUTE_PREEMPTION_DMA_BUFFER_BOUNDARY",
    "DXGI_COMPUTE_PREEMPTION_DISPATCH_BOUNDARY",
    "DXGI_COMPUTE_PREEMPTION_THREAD_GROUP_BOUNDARY",
    "DXGI_COMPUTE_PREEMPTION_THREAD_BOUNDARY",
    "DXGI_COMPUTE_PREEMPTION_INSTRUCTION_BOUNDARY",
    "DXGI_ADAPTER_DESC2",
    "IDXGIAdapter2",
    "IDXGIOutput1",
    "IDXGIDevice3",
    "DXGI_MATRIX_3X2_F",
    "IDXGISwapChain2",
    "IDXGIOutput2",
    "IDXGIFactory3",
    "DXGI_DECODE_SWAP_CHAIN_DESC",
    "DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAGS",
    "DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAG_NOMINAL_RANGE",
    "DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAG_BT709",
    "DXGI_MULTIPLANE_OVERLAY_YCbCr_FLAG_xvYCC",
    "IDXGIDecodeSwapChain",
    "IDXGIFactoryMedia",
    "DXGI_FRAME_PRESENTATION_MODE",
    "DXGI_FRAME_PRESENTATION_MODE_COMPOSED",
    "DXGI_FRAME_PRESENTATION_MODE_OVERLAY",
    "DXGI_FRAME_PRESENTATION_MODE_NONE",
    "DXGI_FRAME_PRESENTATION_MODE_COMPOSITION_FAILURE",
    "DXGI_FRAME_STATISTICS_MEDIA",
    "IDXGISwapChainMedia",
    "DXGI_OVERLAY_SUPPORT_FLAG",
    "DXGI_OVERLAY_SUPPORT_FLAG_DIRECT",
    "DXGI_OVERLAY_SUPPORT_FLAG_SCALING",
    "IDXGIOutput3",
    "DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG",
    "DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG_PRESENT",
    "DXGI_SWAP_CHAIN_COLOR_SPACE_SUPPORT_FLAG_OVERLAY_PRESENT",
    "IDXGISwapChain3",
    "DXGI_OVERLAY_COLOR_SPACE_SUPPORT_FLAG",
    "DXGI_OVERLAY_COLOR_SPACE_SUPPORT_FLAG_PRESENT",
    "IDXGIOutput4",
    "IDXGIFactory4",
    "DXGI_MEMORY_SEGMENT_GROUP",
    "DXGI_MEMORY_SEGMENT_GROUP_LOCAL",
    "DXGI_MEMORY_SEGMENT_GROUP_NON_LOCAL",
    "DXGI_QUERY_VIDEO_MEMORY_INFO",
    "IDXGIAdapter3",
    "DXGI_OUTDUPL_FLAG",
    "DXGI_OUTDUPL_COMPOSITED_UI_CAPTURE_ONLY",
    "IDXGIOutput5",
    "DXGI_HDR_METADATA_TYPE",
    "DXGI_HDR_METADATA_TYPE_NONE",
    "DXGI_HDR_METADATA_TYPE_HDR10",
    "DXGI_HDR_METADATA_TYPE_HDR10PLUS",
    "DXGI_HDR_METADATA_HDR10",
    "DXGI_HDR_METADATA_HDR10PLUS",
    "IDXGISwapChain4",
    "DXGI_OFFER_RESOURCE_FLAGS",
    "DXGI_OFFER_RESOURCE_FLAG_ALLOW_DECOMMIT",
    "DXGI_RECLAIM_RESOURCE_RESULTS",
    "DXGI_RECLAIM_RESOURCE_RESULT_OK",
    "DXGI_RECLAIM_RESOURCE_RESULT_DISCARDED",
    "DXGI_RECLAIM_RESOURCE_RESULT_NOT_COMMITTED",
    "IDXGIDevice4",
    "DXGI_FEATURE",
    "DXGI_FEATURE_PRESENT_ALLOW_TEARING",
    "IDXGIFactory5",
    "DXGI_ADAPTER_FLAG3",
    "DXGI_ADAPTER_FLAG3_NONE",
    "DXGI_ADAPTER_FLAG3_REMOTE",
    "DXGI_ADAPTER_FLAG3_SOFTWARE",
    "DXGI_ADAPTER_FLAG3_ACG_COMPATIBLE",
    "DXGI_ADAPTER_FLAG3_SUPPORT_MONITORED_FENCES",
    "DXGI_ADAPTER_FLAG3_SUPPORT_NON_MONITORED_FENCES",
    "DXGI_ADAPTER_FLAG3_KEYED_MUTEX_CONFORMANCE",
    "DXGI_ADAPTER_FLAG3_FORCE_DWORD",
    "DXGI_ADAPTER_DESC3",
    "IDXGIAdapter4",
    "DXGI_OUTPUT_DESC1",
    "DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAGS",
    "DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAG_FULLSCREEN",
    "DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAG_WINDOWED",
    "DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAG_CURSOR_STRETCHED",
    "IDXGIOutput6",
    "DXGI_GPU_PREFERENCE",
    "DXGI_GPU_PREFERENCE_UNSPECIFIED",
    "DXGI_GPU_PREFERENCE_MINIMUM_POWER",
    "DXGI_GPU_PREFERENCE_HIGH_PERFORMANCE",
    "IDXGIFactory6",
    "IDXGIFactory7",
    "DXGI_DEBUG_RLO_FLAGS",
    "DXGI_DEBUG_RLO_SUMMARY",
    "DXGI_DEBUG_RLO_DETAIL",
    "DXGI_DEBUG_RLO_IGNORE_INTERNAL",
    "DXGI_DEBUG_RLO_ALL",
    "DXGI_INFO_QUEUE_MESSAGE_CATEGORY",
    "DXGI_INFO_QUEUE_MESSAGE_CATEGORY_UNKNOWN",
    "DXGI_INFO_QUEUE_MESSAGE_CATEGORY_MISCELLANEOUS",
    "DXGI_INFO_QUEUE_MESSAGE_CATEGORY_INITIALIZATION",
    "DXGI_INFO_QUEUE_MESSAGE_CATEGORY_CLEANUP",
    "DXGI_INFO_QUEUE_MESSAGE_CATEGORY_COMPILATION",
    "DXGI_INFO_QUEUE_MESSAGE_CATEGORY_STATE_CREATION",
    "DXGI_INFO_QUEUE_MESSAGE_CATEGORY_STATE_SETTING",
    "DXGI_INFO_QUEUE_MESSAGE_CATEGORY_STATE_GETTING",
    "DXGI_INFO_QUEUE_MESSAGE_CATEGORY_RESOURCE_MANIPULATION",
    "DXGI_INFO_QUEUE_MESSAGE_CATEGORY_EXECUTION",
    "DXGI_INFO_QUEUE_MESSAGE_CATEGORY_SHADER",
    "DXGI_INFO_QUEUE_MESSAGE_SEVERITY",
    "DXGI_INFO_QUEUE_MESSAGE_SEVERITY_CORRUPTION",
    "DXGI_INFO_QUEUE_MESSAGE_SEVERITY_ERROR",
    "DXGI_INFO_QUEUE_MESSAGE_SEVERITY_WARNING",
    "DXGI_INFO_QUEUE_MESSAGE_SEVERITY_INFO",
    "DXGI_INFO_QUEUE_MESSAGE_SEVERITY_MESSAGE",
    "DXGI_INFO_QUEUE_MESSAGE",
    "DXGI_INFO_QUEUE_FILTER_DESC",
    "DXGI_INFO_QUEUE_FILTER",
    "IDXGIInfoQueue",
    "IDXGIDebug",
    "IDXGIDebug1",
    "DXGI_Message_Id",
    "DXGI_MSG_IDXGISwapChain_CreationOrResizeBuffers_InvalidOutputWindow",
    "DXGI_MSG_IDXGISwapChain_CreationOrResizeBuffers_BufferWidthInferred",
    "DXGI_MSG_IDXGISwapChain_CreationOrResizeBuffers_BufferHeightInferred",
    "DXGI_MSG_IDXGISwapChain_CreationOrResizeBuffers_NoScanoutFlagChanged",
    "DXGI_MSG_IDXGISwapChain_Creation_MaxBufferCountExceeded",
    "DXGI_MSG_IDXGISwapChain_Creation_TooFewBuffers",
    "DXGI_MSG_IDXGISwapChain_Creation_NoOutputWindow",
    "DXGI_MSG_IDXGISwapChain_Destruction_OtherMethodsCalled",
    "DXGI_MSG_IDXGISwapChain_GetDesc_pDescIsNULL",
    "DXGI_MSG_IDXGISwapChain_GetBuffer_ppSurfaceIsNULL",
    "DXGI_MSG_IDXGISwapChain_GetBuffer_NoAllocatedBuffers",
    "DXGI_MSG_IDXGISwapChain_GetBuffer_iBufferMustBeZero",
    "DXGI_MSG_IDXGISwapChain_GetBuffer_iBufferOOB",
    "DXGI_MSG_IDXGISwapChain_GetContainingOutput_ppOutputIsNULL",
    "DXGI_MSG_IDXGISwapChain_Present_SyncIntervalOOB",
    "DXGI_MSG_IDXGISwapChain_Present_InvalidNonPreRotatedFlag",
    "DXGI_MSG_IDXGISwapChain_Present_NoAllocatedBuffers",
    "DXGI_MSG_IDXGISwapChain_Present_GetDXGIAdapterFailed",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_BufferCountOOB",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_UnreleasedReferences",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidSwapChainFlag",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidNonPreRotatedFlag",
    "DXGI_MSG_IDXGISwapChain_ResizeTarget_RefreshRateDivideByZero",
    "DXGI_MSG_IDXGISwapChain_SetFullscreenState_InvalidTarget",
    "DXGI_MSG_IDXGISwapChain_GetFrameStatistics_pStatsIsNULL",
    "DXGI_MSG_IDXGISwapChain_GetLastPresentCount_pLastPresentCountIsNULL",
    "DXGI_MSG_IDXGISwapChain_SetFullscreenState_RemoteNotSupported",
    "DXGI_MSG_IDXGIOutput_TakeOwnership_FailedToAcquireFullscreenMutex",
    "DXGI_MSG_IDXGIFactory_CreateSoftwareAdapter_ppAdapterInterfaceIsNULL",
    "DXGI_MSG_IDXGIFactory_EnumAdapters_ppAdapterInterfaceIsNULL",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_ppSwapChainIsNULL",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_pDescIsNULL",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_UnknownSwapEffect",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidFlags",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_NonPreRotatedFlagAndWindowed",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_NullDeviceInterface",
    "DXGI_MSG_IDXGIFactory_GetWindowAssociation_phWndIsNULL",
    "DXGI_MSG_IDXGIFactory_MakeWindowAssociation_InvalidFlags",
    "DXGI_MSG_IDXGISurface_Map_InvalidSurface",
    "DXGI_MSG_IDXGISurface_Map_FlagsSetToZero",
    "DXGI_MSG_IDXGISurface_Map_DiscardAndReadFlagSet",
    "DXGI_MSG_IDXGISurface_Map_DiscardButNotWriteFlagSet",
    "DXGI_MSG_IDXGISurface_Map_NoCPUAccess",
    "DXGI_MSG_IDXGISurface_Map_ReadFlagSetButCPUAccessIsDynamic",
    "DXGI_MSG_IDXGISurface_Map_DiscardFlagSetButCPUAccessIsNotDynamic",
    "DXGI_MSG_IDXGIOutput_GetDisplayModeList_pNumModesIsNULL",
    "DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_ModeHasInvalidWidthOrHeight",
    "DXGI_MSG_IDXGIOutput_GetCammaControlCapabilities_NoOwnerDevice",
    "DXGI_MSG_IDXGIOutput_TakeOwnership_pDeviceIsNULL",
    "DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_NoOwnerDevice",
    "DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_pDestinationIsNULL",
    "DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_MapOfDestinationFailed",
    "DXGI_MSG_IDXGIOutput_GetFrameStatistics_NoOwnerDevice",
    "DXGI_MSG_IDXGIOutput_GetFrameStatistics_pStatsIsNULL",
    "DXGI_MSG_IDXGIOutput_SetGammaControl_NoOwnerDevice",
    "DXGI_MSG_IDXGIOutput_GetGammaControl_NoOwnerDevice",
    "DXGI_MSG_IDXGIOutput_GetGammaControl_NoGammaControls",
    "DXGI_MSG_IDXGIOutput_SetDisplaySurface_IDXGIResourceNotSupportedBypPrimary",
    "DXGI_MSG_IDXGIOutput_SetDisplaySurface_pPrimaryIsInvalid",
    "DXGI_MSG_IDXGIOutput_SetDisplaySurface_NoOwnerDevice",
    "DXGI_MSG_IDXGIOutput_TakeOwnership_RemoteDeviceNotSupported",
    "DXGI_MSG_IDXGIOutput_GetDisplayModeList_RemoteDeviceNotSupported",
    "DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_RemoteDeviceNotSupported",
    "DXGI_MSG_IDXGIDevice_CreateSurface_InvalidParametersWithpSharedResource",
    "DXGI_MSG_IDXGIObject_GetPrivateData_puiDataSizeIsNULL",
    "DXGI_MSG_IDXGISwapChain_Creation_InvalidOutputWindow",
    "DXGI_MSG_IDXGISwapChain_Release_SwapChainIsFullscreen",
    "DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_InvalidTargetSurfaceFormat",
    "DXGI_MSG_IDXGIFactory_CreateSoftwareAdapter_ModuleIsNULL",
    "DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_IDXGIDeviceNotSupportedBypConcernedDevice",
    "DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_pModeToMatchOrpClosestMatchIsNULL",
    "DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_ModeHasRefreshRateDenominatorZero",
    "DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_UnknownFormatIsInvalidForConfiguration",
    "DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_InvalidDisplayModeScanlineOrdering",
    "DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_InvalidDisplayModeScaling",
    "DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_InvalidDisplayModeFormatAndDeviceCombination",
    "DXGI_MSG_IDXGIFactory_Creation_CalledFromDllMain",
    "DXGI_MSG_IDXGISwapChain_SetFullscreenState_OutputNotOwnedBySwapChainDevice",
    "DXGI_MSG_IDXGISwapChain_Creation_InvalidWindowStyle",
    "DXGI_MSG_IDXGISwapChain_GetFrameStatistics_UnsupportedStatistics",
    "DXGI_MSG_IDXGISwapChain_GetContainingOutput_SwapchainAdapterDoesNotControlOutput",
    "DXGI_MSG_IDXGIOutput_SetOrGetGammaControl_pArrayIsNULL",
    "DXGI_MSG_IDXGISwapChain_SetFullscreenState_FullscreenInvalidForChildWindows",
    "DXGI_MSG_IDXGIFactory_Release_CalledFromDllMain",
    "DXGI_MSG_IDXGISwapChain_Present_UnreleasedHDC",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_NonPreRotatedAndGDICompatibleFlags",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_NonPreRotatedAndGDICompatibleFlags",
    "DXGI_MSG_IDXGISurface1_GetDC_pHdcIsNULL",
    "DXGI_MSG_IDXGISurface1_GetDC_SurfaceNotTexture2D",
    "DXGI_MSG_IDXGISurface1_GetDC_GDICompatibleFlagNotSet",
    "DXGI_MSG_IDXGISurface1_GetDC_UnreleasedHDC",
    "DXGI_MSG_IDXGISurface_Map_NoCPUAccess2",
    "DXGI_MSG_IDXGISurface1_ReleaseDC_GetDCNotCalled",
    "DXGI_MSG_IDXGISurface1_ReleaseDC_InvalidRectangleDimensions",
    "DXGI_MSG_IDXGIOutput_TakeOwnership_RemoteOutputNotSupported",
    "DXGI_MSG_IDXGIOutput_FindClosestMatchingMode_RemoteOutputNotSupported",
    "DXGI_MSG_IDXGIOutput_GetDisplayModeList_RemoteOutputNotSupported",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_pDeviceHasMismatchedDXGIFactory",
    "DXGI_MSG_IDXGISwapChain_Present_NonOptimalFSConfiguration",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_FlipSequentialNotSupportedOnD3D10",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_BufferCountOOBForFlipSequential",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidFormatForFlipSequential",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_MultiSamplingNotSupportedForFlipSequential",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_BufferCountOOBForFlipSequential",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidFormatForFlipSequential",
    "DXGI_MSG_IDXGISwapChain_Present_PartialPresentationBeforeStandardPresentation",
    "DXGI_MSG_IDXGISwapChain_Present_FullscreenPartialPresentIsInvalid",
    "DXGI_MSG_IDXGISwapChain_Present_InvalidPresentTestOrDoNotSequenceFlag",
    "DXGI_MSG_IDXGISwapChain_Present_ScrollInfoWithNoDirtyRectsSpecified",
    "DXGI_MSG_IDXGISwapChain_Present_EmptyScrollRect",
    "DXGI_MSG_IDXGISwapChain_Present_ScrollRectOutOfBackbufferBounds",
    "DXGI_MSG_IDXGISwapChain_Present_ScrollRectOutOfBackbufferBoundsWithOffset",
    "DXGI_MSG_IDXGISwapChain_Present_EmptyDirtyRect",
    "DXGI_MSG_IDXGISwapChain_Present_DirtyRectOutOfBackbufferBounds",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_UnsupportedBufferUsageFlags",
    "DXGI_MSG_IDXGISwapChain_Present_DoNotSequenceFlagSetButPreviousBufferIsUndefined",
    "DXGI_MSG_IDXGISwapChain_Present_UnsupportedFlags",
    "DXGI_MSG_IDXGISwapChain_Present_FlipModelChainMustResizeOrCreateOnFSTransition",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_pRestrictToOutputFromOtherIDXGIFactory",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_RestrictOutputNotSupportedOnAdapter",
    "DXGI_MSG_IDXGISwapChain_Present_RestrictToOutputFlagSetButInvalidpRestrictToOutput",
    "DXGI_MSG_IDXGISwapChain_Present_RestrictToOutputFlagdWithFullscreen",
    "DXGI_MSG_IDXGISwapChain_Present_RestrictOutputFlagWithStaleSwapChain",
    "DXGI_MSG_IDXGISwapChain_Present_OtherFlagsCausingInvalidPresentTestFlag",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_UnavailableInSession0",
    "DXGI_MSG_IDXGIFactory_MakeWindowAssociation_UnavailableInSession0",
    "DXGI_MSG_IDXGIFactory_GetWindowAssociation_UnavailableInSession0",
    "DXGI_MSG_IDXGIAdapter_EnumOutputs_UnavailableInSession0",
    "DXGI_MSG_IDXGISwapChain_CreationOrSetFullscreenState_StereoDisabled",
    "DXGI_MSG_IDXGIFactory2_UnregisterStatus_CookieNotFound",
    "DXGI_MSG_IDXGISwapChain_Present_ProtectedContentInWindowedModeWithoutFSOrOverlay",
    "DXGI_MSG_IDXGISwapChain_Present_ProtectedContentInWindowedModeWithoutFlipSequential",
    "DXGI_MSG_IDXGISwapChain_Present_ProtectedContentWithRDPDriver",
    "DXGI_MSG_IDXGISwapChain_Present_ProtectedContentInWindowedModeWithDWMOffOrInvalidDisplayAffinity",
    "DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_WidthOrHeightIsZero",
    "DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_OnlyFlipSequentialSupported",
    "DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_UnsupportedOnAdapter",
    "DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_UnsupportedOnWindows7",
    "DXGI_MSG_IDXGISwapChain_SetFullscreenState_FSTransitionWithCompositionSwapChain",
    "DXGI_MSG_IDXGISwapChain_ResizeTarget_InvalidWithCompositionSwapChain",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_WidthOrHeightIsZero",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_ScalingNoneIsFlipModelOnly",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_ScalingUnrecognized",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_DisplayOnlyFullscreenUnsupported",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_DisplayOnlyUnsupported",
    "DXGI_MSG_IDXGISwapChain_Present_RestartIsFullscreenOnly",
    "DXGI_MSG_IDXGISwapChain_Present_ProtectedWindowlessPresentationRequiresDisplayOnly",
    "DXGI_MSG_IDXGISwapChain_SetFullscreenState_DisplayOnlyUnsupported",
    "DXGI_MSG_IDXGISwapChain1_SetBackgroundColor_OutOfRange",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_DisplayOnlyFullscreenUnsupported",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_DisplayOnlyUnsupported",
    "DXGI_MSG_IDXGISwapchain_Present_ScrollUnsupported",
    "DXGI_MSG_IDXGISwapChain1_SetRotation_UnsupportedOS",
    "DXGI_MSG_IDXGISwapChain1_GetRotation_UnsupportedOS",
    "DXGI_MSG_IDXGISwapchain_Present_FullscreenRotation",
    "DXGI_MSG_IDXGISwapChain_Present_PartialPresentationWithMSAABuffers",
    "DXGI_MSG_IDXGISwapChain1_SetRotation_FlipSequentialRequired",
    "DXGI_MSG_IDXGISwapChain1_SetRotation_InvalidRotation",
    "DXGI_MSG_IDXGISwapChain1_GetRotation_FlipSequentialRequired",
    "DXGI_MSG_IDXGISwapChain_GetHwnd_WrongType",
    "DXGI_MSG_IDXGISwapChain_GetCompositionSurface_WrongType",
    "DXGI_MSG_IDXGISwapChain_GetCoreWindow_WrongType",
    "DXGI_MSG_IDXGISwapChain_GetFullscreenDesc_NonHwnd",
    "DXGI_MSG_IDXGISwapChain_SetFullscreenState_CoreWindow",
    "DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_UnsupportedOnWindows7",
    "DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_pWindowIsNULL",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_FSUnsupportedForModernApps",
    "DXGI_MSG_IDXGIFactory_MakeWindowAssociation_ModernApp",
    "DXGI_MSG_IDXGISwapChain_ResizeTarget_ModernApp",
    "DXGI_MSG_IDXGISwapChain_ResizeTarget_pNewTargetParametersIsNULL",
    "DXGI_MSG_IDXGIOutput_SetDisplaySurface_ModernApp",
    "DXGI_MSG_IDXGIOutput_TakeOwnership_ModernApp",
    "DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_pWindowIsInvalid",
    "DXGI_MSG_IDXGIFactory2_CreateSwapChainForCompositionSurface_InvalidHandle",
    "DXGI_MSG_IDXGISurface1_GetDC_ModernApp",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_ScalingNoneRequiresWindows8OrNewer",
    "DXGI_MSG_IDXGISwapChain_Present_TemporaryMonoAndPreferRight",
    "DXGI_MSG_IDXGISwapChain_Present_TemporaryMonoOrPreferRightWithDoNotSequence",
    "DXGI_MSG_IDXGISwapChain_Present_TemporaryMonoOrPreferRightWithoutStereo",
    "DXGI_MSG_IDXGISwapChain_Present_TemporaryMonoUnsupported",
    "DXGI_MSG_IDXGIOutput_GetDisplaySurfaceData_ArraySizeMismatch",
    "DXGI_MSG_IDXGISwapChain_Present_PartialPresentationWithSwapEffectDiscard",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_AlphaUnrecognized",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_AlphaIsWindowlessOnly",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_AlphaIsFlipModelOnly",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_RestrictToOutputAdapterMismatch",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_DisplayOnlyOnLegacy",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_DisplayOnlyOnLegacy",
    "DXGI_MSG_IDXGIResource1_CreateSubresourceSurface_InvalidIndex",
    "DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_InvalidScaling",
    "DXGI_MSG_IDXGIFactory_CreateSwapChainForCoreWindow_InvalidSwapEffect",
    "DXGI_MSG_IDXGIResource1_CreateSharedHandle_UnsupportedOS",
    "DXGI_MSG_IDXGIFactory2_RegisterOcclusionStatusWindow_UnsupportedOS",
    "DXGI_MSG_IDXGIFactory2_RegisterOcclusionStatusEvent_UnsupportedOS",
    "DXGI_MSG_IDXGIOutput1_DuplicateOutput_UnsupportedOS",
    "DXGI_MSG_IDXGIDisplayControl_IsStereoEnabled_UnsupportedOS",
    "DXGI_MSG_IDXGIFactory_CreateSwapChainForComposition_InvalidAlphaMode",
    "DXGI_MSG_IDXGIFactory_GetSharedResourceAdapterLuid_InvalidResource",
    "DXGI_MSG_IDXGIFactory_GetSharedResourceAdapterLuid_InvalidLUID",
    "DXGI_MSG_IDXGIFactory_GetSharedResourceAdapterLuid_UnsupportedOS",
    "DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_2DOnly",
    "DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_StagingOnly",
    "DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_NeedCPUAccessWrite",
    "DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_NoShared",
    "DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_OnlyMipLevels1",
    "DXGI_MSG_IDXGIOutput1_GetDisplaySurfaceData1_MappedOrOfferedResource",
    "DXGI_MSG_IDXGISwapChain_SetFullscreenState_FSUnsupportedForModernApps",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_FailedToGoFSButNonPreRotated",
    "DXGI_MSG_IDXGIFactory_CreateSwapChainOrRegisterOcclusionStatus_BlitModelUsedWhileRegisteredForOcclusionStatusEvents",
    "DXGI_MSG_IDXGISwapChain_Present_BlitModelUsedWhileRegisteredForOcclusionStatusEvents",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_WaitableSwapChainsAreFlipModelOnly",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_WaitableSwapChainsAreNotFullscreen",
    "DXGI_MSG_IDXGISwapChain_SetFullscreenState_Waitable",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_CannotAddOrRemoveWaitableFlag",
    "DXGI_MSG_IDXGISwapChain_GetFrameLatencyWaitableObject_OnlyWaitable",
    "DXGI_MSG_IDXGISwapChain_GetMaximumFrameLatency_OnlyWaitable",
    "DXGI_MSG_IDXGISwapChain_GetMaximumFrameLatency_pMaxLatencyIsNULL",
    "DXGI_MSG_IDXGISwapChain_SetMaximumFrameLatency_OnlyWaitable",
    "DXGI_MSG_IDXGISwapChain_SetMaximumFrameLatency_MaxLatencyIsOutOfBounds",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_ForegroundIsCoreWindowOnly",
    "DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_ForegroundUnsupportedOnAdapter",
    "DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_InvalidScaling",
    "DXGI_MSG_IDXGIFactory2_CreateSwapChainForCoreWindow_InvalidAlphaMode",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_CannotAddOrRemoveForegroundFlag",
    "DXGI_MSG_IDXGISwapChain_SetMatrixTransform_MatrixPointerCannotBeNull",
    "DXGI_MSG_IDXGISwapChain_SetMatrixTransform_RequiresCompositionSwapChain",
    "DXGI_MSG_IDXGISwapChain_SetMatrixTransform_MatrixMustBeFinite",
    "DXGI_MSG_IDXGISwapChain_SetMatrixTransform_MatrixMustBeTranslateAndOrScale",
    "DXGI_MSG_IDXGISwapChain_GetMatrixTransform_MatrixPointerCannotBeNull",
    "DXGI_MSG_IDXGISwapChain_GetMatrixTransform_RequiresCompositionSwapChain",
    "DXGI_MSG_DXGIGetDebugInterface1_NULL_ppDebug",
    "DXGI_MSG_DXGIGetDebugInterface1_InvalidFlags",
    "DXGI_MSG_IDXGISwapChain_Present_Decode",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_Decode",
    "DXGI_MSG_IDXGISwapChain_SetSourceSize_FlipModel",
    "DXGI_MSG_IDXGISwapChain_SetSourceSize_Decode",
    "DXGI_MSG_IDXGISwapChain_SetSourceSize_WidthHeight",
    "DXGI_MSG_IDXGISwapChain_GetSourceSize_NullPointers",
    "DXGI_MSG_IDXGISwapChain_GetSourceSize_Decode",
    "DXGI_MSG_IDXGIDecodeSwapChain_SetColorSpace_InvalidFlags",
    "DXGI_MSG_IDXGIDecodeSwapChain_SetSourceRect_InvalidRect",
    "DXGI_MSG_IDXGIDecodeSwapChain_SetTargetRect_InvalidRect",
    "DXGI_MSG_IDXGIDecodeSwapChain_SetDestSize_InvalidSize",
    "DXGI_MSG_IDXGIDecodeSwapChain_GetSourceRect_InvalidPointer",
    "DXGI_MSG_IDXGIDecodeSwapChain_GetTargetRect_InvalidPointer",
    "DXGI_MSG_IDXGIDecodeSwapChain_GetDestSize_InvalidPointer",
    "DXGI_MSG_IDXGISwapChain_PresentBuffer_YUV",
    "DXGI_MSG_IDXGISwapChain_SetSourceSize_YUV",
    "DXGI_MSG_IDXGISwapChain_GetSourceSize_YUV",
    "DXGI_MSG_IDXGISwapChain_SetMatrixTransform_YUV",
    "DXGI_MSG_IDXGISwapChain_GetMatrixTransform_YUV",
    "DXGI_MSG_IDXGISwapChain_Present_PartialPresentation_YUV",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_CannotAddOrRemoveFlag_YUV",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_Alignment_YUV",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_ShaderInputUnsupported_YUV",
    "DXGI_MSG_IDXGIOutput3_CheckOverlaySupport_NullPointers",
    "DXGI_MSG_IDXGIOutput3_CheckOverlaySupport_IDXGIDeviceNotSupportedBypConcernedDevice",
    "DXGI_MSG_IDXGIAdapter_EnumOutputs2_InvalidEnumOutputs2Flag",
    "DXGI_MSG_IDXGISwapChain_CreationOrSetFullscreenState_FSUnsupportedForFlipDiscard",
    "DXGI_MSG_IDXGIOutput4_CheckOverlayColorSpaceSupport_NullPointers",
    "DXGI_MSG_IDXGIOutput4_CheckOverlayColorSpaceSupport_IDXGIDeviceNotSupportedBypConcernedDevice",
    "DXGI_MSG_IDXGISwapChain3_CheckColorSpaceSupport_NullPointers",
    "DXGI_MSG_IDXGISwapChain3_SetColorSpace1_InvalidColorSpace",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidHwProtect",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_HwProtectUnsupported",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidHwProtect",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_HwProtectUnsupported",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers1_D3D12Only",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers1_FlipModel",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers1_NodeMaskAndQueueRequired",
    "DXGI_MSG_IDXGISwapChain_CreateSwapChain_InvalidHwProtectGdiFlag",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_InvalidHwProtectGdiFlag",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_10BitFormatNotSupported",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_FlipSwapEffectRequired",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidDevice",
    "DXGI_MSG_IDXGIOutput_TakeOwnership_Unsupported",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_InvalidQueue",
    "DXGI_MSG_IDXGISwapChain3_ResizeBuffers1_InvalidQueue",
    "DXGI_MSG_IDXGIFactory_CreateSwapChainForHwnd_InvalidScaling",
    "DXGI_MSG_IDXGISwapChain3_SetHDRMetaData_InvalidSize",
    "DXGI_MSG_IDXGISwapChain3_SetHDRMetaData_InvalidPointer",
    "DXGI_MSG_IDXGISwapChain3_SetHDRMetaData_InvalidType",
    "DXGI_MSG_IDXGISwapChain_Present_FullscreenAllowTearingIsInvalid",
    "DXGI_MSG_IDXGISwapChain_Present_AllowTearingRequiresPresentIntervalZero",
    "DXGI_MSG_IDXGISwapChain_Present_AllowTearingRequiresCreationFlag",
    "DXGI_MSG_IDXGISwapChain_ResizeBuffers_CannotAddOrRemoveAllowTearingFlag",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_AllowTearingFlagIsFlipModelOnly",
    "DXGI_MSG_IDXGIFactory_CheckFeatureSupport_InvalidFeature",
    "DXGI_MSG_IDXGIFactory_CheckFeatureSupport_InvalidSize",
    "DXGI_MSG_IDXGIOutput6_CheckHardwareCompositionSupport_NullPointer",
    "DXGI_MSG_IDXGISwapChain_SetFullscreenState_PerMonitorDpiShimApplied",
    "DXGI_MSG_IDXGIOutput_DuplicateOutput_PerMonitorDpiShimApplied",
    "DXGI_MSG_IDXGIOutput_DuplicateOutput1_PerMonitorDpiRequired",
    "DXGI_MSG_IDXGIFactory7_UnregisterAdaptersChangedEvent_CookieNotFound",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_LegacyBltModelSwapEffect",
    "DXGI_MSG_IDXGISwapChain4_SetHDRMetaData_MetadataUnchanged",
    "DXGI_MSG_IDXGISwapChain_Present_11On12_Released_Resource",
    "DXGI_MSG_IDXGIFactory_CreateSwapChain_MultipleSwapchainRefToSurface_DeferredDtr",
    "DXGI_MSG_IDXGIFactory_MakeWindowAssociation_NoOpBehavior",
    "DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_NotForegroundWindow",
    "DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_DISCARD_BufferCount",
    "DXGI_MSG_Phone_IDXGISwapChain_SetFullscreenState_NotAvailable",
    "DXGI_MSG_Phone_IDXGISwapChain_ResizeBuffers_NotAvailable",
    "DXGI_MSG_Phone_IDXGISwapChain_ResizeTarget_NotAvailable",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidLayerIndex",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_MultipleLayerIndex",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidLayerFlag",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidRotation",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidBlend",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidResource",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidMultiPlaneOverlayResource",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidIndexForPrimary",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidIndexForOverlay",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidSubResourceIndex",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidSourceRect",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidDestinationRect",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_MultipleResource",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_NotSharedResource",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidFlag",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_InvalidInterval",
    "DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_MSAA_NotSupported",
    "DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_ScalingAspectRatioStretch_Supported_ModernApp",
    "DXGI_MSG_Phone_IDXGISwapChain_GetFrameStatistics_NotAvailable_ModernApp",
    "DXGI_MSG_Phone_IDXGISwapChain_Present_ReplaceInterval0With1",
    "DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_FailedRegisterWithCompositor",
    "DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_NotForegroundWindow_AtRendering",
    "DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_FLIP_SEQUENTIAL_BufferCount",
    "DXGI_MSG_Phone_IDXGIFactory_CreateSwapChain_FLIP_Modern_CoreWindow_Only",
    "DXGI_MSG_Phone_IDXGISwapChain_Present1_RequiresOverlays",
    "DXGI_MSG_Phone_IDXGISwapChain_SetBackgroundColor_FlipSequentialRequired",
    "DXGI_MSG_Phone_IDXGISwapChain_GetBackgroundColor_FlipSequentialRequired",
    "IDXGraphicsAnalysis",
    "CreateDXGIFactory",
    "CreateDXGIFactory1",
    "CreateDXGIFactory2",
    "DXGIGetDebugInterface1",
    "DXGIDeclareAdapterRemovalSupport",
]
