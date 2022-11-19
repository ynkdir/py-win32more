from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.CompositionSwapchain
import win32more.Graphics.Dxgi.Common
import win32more.System.Com

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_SystemInterruptTime_head():
    class SystemInterruptTime(Structure):
        pass
    return SystemInterruptTime
def _define_SystemInterruptTime():
    SystemInterruptTime = win32more.Graphics.CompositionSwapchain.SystemInterruptTime_head
    SystemInterruptTime._fields_ = [
        ("value", UInt64),
    ]
    return SystemInterruptTime
def _define_PresentationTransform_head():
    class PresentationTransform(Structure):
        pass
    return PresentationTransform
def _define_PresentationTransform():
    PresentationTransform = win32more.Graphics.CompositionSwapchain.PresentationTransform_head
    PresentationTransform._fields_ = [
        ("M11", Single),
        ("M12", Single),
        ("M21", Single),
        ("M22", Single),
        ("M31", Single),
        ("M32", Single),
    ]
    return PresentationTransform
PresentStatisticsKind = Int32
PresentStatisticsKind_PresentStatus = 1
PresentStatisticsKind_CompositionFrame = 2
PresentStatisticsKind_IndependentFlipFrame = 3
def _define_IPresentationBuffer_head():
    class IPresentationBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('2e217d3a-5abb-4138-9a13-a775593c89ca')
    return IPresentationBuffer
def _define_IPresentationBuffer():
    IPresentationBuffer = win32more.Graphics.CompositionSwapchain.IPresentationBuffer_head
    IPresentationBuffer.GetAvailableEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(3, 'GetAvailableEvent', ((1, 'availableEventHandle'),)))
    IPresentationBuffer.IsAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no, use_last_error=False)(4, 'IsAvailable', ((1, 'isAvailable'),)))
    win32more.System.Com.IUnknown
    return IPresentationBuffer
def _define_IPresentationContent_head():
    class IPresentationContent(win32more.System.Com.IUnknown_head):
        Guid = Guid('5668bb79-3d8e-415c-b215-f38020f2d252')
    return IPresentationContent
def _define_IPresentationContent():
    IPresentationContent = win32more.Graphics.CompositionSwapchain.IPresentationContent_head
    IPresentationContent.SetTag = COMMETHOD(WINFUNCTYPE(Void,UIntPtr, use_last_error=False)(3, 'SetTag', ((1, 'tag'),)))
    win32more.System.Com.IUnknown
    return IPresentationContent
def _define_IPresentationSurface_head():
    class IPresentationSurface(win32more.Graphics.CompositionSwapchain.IPresentationContent_head):
        Guid = Guid('956710fb-ea40-4eba-a3eb-4375a0eb4edc')
    return IPresentationSurface
def _define_IPresentationSurface():
    IPresentationSurface = win32more.Graphics.CompositionSwapchain.IPresentationSurface_head
    IPresentationSurface.SetBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.CompositionSwapchain.IPresentationBuffer_head, use_last_error=False)(4, 'SetBuffer', ((1, 'presentationBuffer'),)))
    IPresentationSurface.SetColorSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE, use_last_error=False)(5, 'SetColorSpace', ((1, 'colorSpace'),)))
    IPresentationSurface.SetAlphaMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.Common.DXGI_ALPHA_MODE, use_last_error=False)(6, 'SetAlphaMode', ((1, 'alphaMode'),)))
    IPresentationSurface.SetSourceRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(7, 'SetSourceRect', ((1, 'sourceRect'),)))
    IPresentationSurface.SetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.CompositionSwapchain.PresentationTransform_head), use_last_error=False)(8, 'SetTransform', ((1, 'transform'),)))
    IPresentationSurface.RestrictToOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(9, 'RestrictToOutput', ((1, 'output'),)))
    IPresentationSurface.SetDisableReadback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Byte, use_last_error=False)(10, 'SetDisableReadback', ((1, 'value'),)))
    IPresentationSurface.SetLetterboxingMargins = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,Single, use_last_error=False)(11, 'SetLetterboxingMargins', ((1, 'leftLetterboxSize'),(1, 'topLetterboxSize'),(1, 'rightLetterboxSize'),(1, 'bottomLetterboxSize'),)))
    win32more.Graphics.CompositionSwapchain.IPresentationContent
    return IPresentationSurface
def _define_IPresentStatistics_head():
    class IPresentStatistics(win32more.System.Com.IUnknown_head):
        Guid = Guid('b44b8bda-7282-495d-9dd7-ceadd8b4bb86')
    return IPresentStatistics
def _define_IPresentStatistics():
    IPresentStatistics = win32more.Graphics.CompositionSwapchain.IPresentStatistics_head
    IPresentStatistics.GetPresentId = COMMETHOD(WINFUNCTYPE(UInt64, use_last_error=False)(3, 'GetPresentId', ()))
    IPresentStatistics.GetKind = COMMETHOD(WINFUNCTYPE(win32more.Graphics.CompositionSwapchain.PresentStatisticsKind, use_last_error=False)(4, 'GetKind', ()))
    win32more.System.Com.IUnknown
    return IPresentStatistics
def _define_IPresentationManager_head():
    class IPresentationManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('fb562f82-6292-470a-88b1-843661e7f20c')
    return IPresentationManager
def _define_IPresentationManager():
    IPresentationManager = win32more.Graphics.CompositionSwapchain.IPresentationManager_head
    IPresentationManager.AddBufferFromResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.Graphics.CompositionSwapchain.IPresentationBuffer_head), use_last_error=False)(3, 'AddBufferFromResource', ((1, 'resource'),(1, 'presentationBuffer'),)))
    IPresentationManager.CreatePresentationSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Graphics.CompositionSwapchain.IPresentationSurface_head), use_last_error=False)(4, 'CreatePresentationSurface', ((1, 'compositionSurfaceHandle'),(1, 'presentationSurface'),)))
    IPresentationManager.GetNextPresentId = COMMETHOD(WINFUNCTYPE(UInt64, use_last_error=False)(5, 'GetNextPresentId', ()))
    IPresentationManager.SetTargetTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.CompositionSwapchain.SystemInterruptTime, use_last_error=False)(6, 'SetTargetTime', ((1, 'targetTime'),)))
    IPresentationManager.SetPreferredPresentDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.CompositionSwapchain.SystemInterruptTime,win32more.Graphics.CompositionSwapchain.SystemInterruptTime, use_last_error=False)(7, 'SetPreferredPresentDuration', ((1, 'preferredDuration'),(1, 'deviationTolerance'),)))
    IPresentationManager.ForceVSyncInterrupt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Byte, use_last_error=False)(8, 'ForceVSyncInterrupt', ((1, 'forceVsyncInterrupt'),)))
    IPresentationManager.Present = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Present', ()))
    IPresentationManager.GetPresentRetiringFence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(10, 'GetPresentRetiringFence', ((1, 'riid'),(1, 'fence'),)))
    IPresentationManager.CancelPresentsFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(11, 'CancelPresentsFrom', ((1, 'presentIdToCancelFrom'),)))
    IPresentationManager.GetLostEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(12, 'GetLostEvent', ((1, 'lostEventHandle'),)))
    IPresentationManager.GetPresentStatisticsAvailableEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(13, 'GetPresentStatisticsAvailableEvent', ((1, 'presentStatisticsAvailableEventHandle'),)))
    IPresentationManager.EnablePresentStatisticsKind = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.CompositionSwapchain.PresentStatisticsKind,Byte, use_last_error=False)(14, 'EnablePresentStatisticsKind', ((1, 'presentStatisticsKind'),(1, 'enabled'),)))
    IPresentationManager.GetNextPresentStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.CompositionSwapchain.IPresentStatistics_head), use_last_error=False)(15, 'GetNextPresentStatistics', ((1, 'nextPresentStatistics'),)))
    win32more.System.Com.IUnknown
    return IPresentationManager
def _define_IPresentationFactory_head():
    class IPresentationFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('8fb37b58-1d74-4f64-a49c-1f97a80a2ec0')
    return IPresentationFactory
def _define_IPresentationFactory():
    IPresentationFactory = win32more.Graphics.CompositionSwapchain.IPresentationFactory_head
    IPresentationFactory.IsPresentationSupported = COMMETHOD(WINFUNCTYPE(Byte, use_last_error=False)(3, 'IsPresentationSupported', ()))
    IPresentationFactory.IsPresentationSupportedWithIndependentFlip = COMMETHOD(WINFUNCTYPE(Byte, use_last_error=False)(4, 'IsPresentationSupportedWithIndependentFlip', ()))
    IPresentationFactory.CreatePresentationManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.CompositionSwapchain.IPresentationManager_head), use_last_error=False)(5, 'CreatePresentationManager', ((1, 'ppPresentationManager'),)))
    win32more.System.Com.IUnknown
    return IPresentationFactory
PresentStatus = Int32
PresentStatus_Queued = 0
PresentStatus_Skipped = 1
PresentStatus_Canceled = 2
def _define_IPresentStatusPresentStatistics_head():
    class IPresentStatusPresentStatistics(win32more.Graphics.CompositionSwapchain.IPresentStatistics_head):
        Guid = Guid('c9ed2a41-79cb-435e-964e-c8553055420c')
    return IPresentStatusPresentStatistics
def _define_IPresentStatusPresentStatistics():
    IPresentStatusPresentStatistics = win32more.Graphics.CompositionSwapchain.IPresentStatusPresentStatistics_head
    IPresentStatusPresentStatistics.GetCompositionFrameId = COMMETHOD(WINFUNCTYPE(UInt64, use_last_error=False)(5, 'GetCompositionFrameId', ()))
    IPresentStatusPresentStatistics.GetPresentStatus = COMMETHOD(WINFUNCTYPE(win32more.Graphics.CompositionSwapchain.PresentStatus, use_last_error=False)(6, 'GetPresentStatus', ()))
    win32more.Graphics.CompositionSwapchain.IPresentStatistics
    return IPresentStatusPresentStatistics
CompositionFrameInstanceKind = Int32
CompositionFrameInstanceKind_ComposedOnScreen = 0
CompositionFrameInstanceKind_ScanoutOnScreen = 1
CompositionFrameInstanceKind_ComposedToIntermediate = 2
def _define_CompositionFrameDisplayInstance_head():
    class CompositionFrameDisplayInstance(Structure):
        pass
    return CompositionFrameDisplayInstance
def _define_CompositionFrameDisplayInstance():
    CompositionFrameDisplayInstance = win32more.Graphics.CompositionSwapchain.CompositionFrameDisplayInstance_head
    CompositionFrameDisplayInstance._fields_ = [
        ("displayAdapterLUID", win32more.Foundation.LUID),
        ("displayVidPnSourceId", UInt32),
        ("displayUniqueId", UInt32),
        ("renderAdapterLUID", win32more.Foundation.LUID),
        ("instanceKind", win32more.Graphics.CompositionSwapchain.CompositionFrameInstanceKind),
        ("finalTransform", win32more.Graphics.CompositionSwapchain.PresentationTransform),
        ("requiredCrossAdapterCopy", Byte),
        ("colorSpace", win32more.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE),
    ]
    return CompositionFrameDisplayInstance
def _define_ICompositionFramePresentStatistics_head():
    class ICompositionFramePresentStatistics(win32more.Graphics.CompositionSwapchain.IPresentStatistics_head):
        Guid = Guid('ab41d127-c101-4c0a-911d-f9f2e9d08e64')
    return ICompositionFramePresentStatistics
def _define_ICompositionFramePresentStatistics():
    ICompositionFramePresentStatistics = win32more.Graphics.CompositionSwapchain.ICompositionFramePresentStatistics_head
    ICompositionFramePresentStatistics.GetContentTag = COMMETHOD(WINFUNCTYPE(UIntPtr, use_last_error=False)(5, 'GetContentTag', ()))
    ICompositionFramePresentStatistics.GetCompositionFrameId = COMMETHOD(WINFUNCTYPE(UInt64, use_last_error=False)(6, 'GetCompositionFrameId', ()))
    ICompositionFramePresentStatistics.GetDisplayInstanceArray = COMMETHOD(WINFUNCTYPE(Void,POINTER(UInt32),POINTER(POINTER(win32more.Graphics.CompositionSwapchain.CompositionFrameDisplayInstance_head)), use_last_error=False)(7, 'GetDisplayInstanceArray', ((1, 'displayInstanceArrayCount'),(1, 'displayInstanceArray'),)))
    win32more.Graphics.CompositionSwapchain.IPresentStatistics
    return ICompositionFramePresentStatistics
def _define_IIndependentFlipFramePresentStatistics_head():
    class IIndependentFlipFramePresentStatistics(win32more.Graphics.CompositionSwapchain.IPresentStatistics_head):
        Guid = Guid('8c93be27-ad94-4da0-8fd4-2413132d124e')
    return IIndependentFlipFramePresentStatistics
def _define_IIndependentFlipFramePresentStatistics():
    IIndependentFlipFramePresentStatistics = win32more.Graphics.CompositionSwapchain.IIndependentFlipFramePresentStatistics_head
    IIndependentFlipFramePresentStatistics.GetOutputAdapterLUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.LUID, use_last_error=False)(5, 'GetOutputAdapterLUID', ()))
    IIndependentFlipFramePresentStatistics.GetOutputVidPnSourceId = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(6, 'GetOutputVidPnSourceId', ()))
    IIndependentFlipFramePresentStatistics.GetContentTag = COMMETHOD(WINFUNCTYPE(UIntPtr, use_last_error=False)(7, 'GetContentTag', ()))
    IIndependentFlipFramePresentStatistics.GetDisplayedTime = COMMETHOD(WINFUNCTYPE(win32more.Graphics.CompositionSwapchain.SystemInterruptTime, use_last_error=False)(8, 'GetDisplayedTime', ()))
    IIndependentFlipFramePresentStatistics.GetPresentDuration = COMMETHOD(WINFUNCTYPE(win32more.Graphics.CompositionSwapchain.SystemInterruptTime, use_last_error=False)(9, 'GetPresentDuration', ()))
    win32more.Graphics.CompositionSwapchain.IPresentStatistics
    return IIndependentFlipFramePresentStatistics
def _define_CreatePresentationFactory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("CreatePresentationFactory", windll["dcomp"]), ((1, 'd3dDevice'),(1, 'riid'),(1, 'presentationFactory'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "SystemInterruptTime",
    "PresentationTransform",
    "PresentStatisticsKind",
    "PresentStatisticsKind_PresentStatus",
    "PresentStatisticsKind_CompositionFrame",
    "PresentStatisticsKind_IndependentFlipFrame",
    "IPresentationBuffer",
    "IPresentationContent",
    "IPresentationSurface",
    "IPresentStatistics",
    "IPresentationManager",
    "IPresentationFactory",
    "PresentStatus",
    "PresentStatus_Queued",
    "PresentStatus_Skipped",
    "PresentStatus_Canceled",
    "IPresentStatusPresentStatistics",
    "CompositionFrameInstanceKind",
    "CompositionFrameInstanceKind_ComposedOnScreen",
    "CompositionFrameInstanceKind_ScanoutOnScreen",
    "CompositionFrameInstanceKind_ComposedToIntermediate",
    "CompositionFrameDisplayInstance",
    "ICompositionFramePresentStatistics",
    "IIndependentFlipFramePresentStatistics",
    "CreatePresentationFactory",
]
