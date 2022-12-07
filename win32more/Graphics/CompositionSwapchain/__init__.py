from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.CompositionSwapchain
import win32more.Graphics.Dxgi.Common
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
@winfunctype('dcomp.dll')
def CreatePresentationFactory(d3dDevice: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), presentationFactory: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class CompositionFrameDisplayInstance(Structure):
    displayAdapterLUID: win32more.Foundation.LUID
    displayVidPnSourceId: UInt32
    displayUniqueId: UInt32
    renderAdapterLUID: win32more.Foundation.LUID
    instanceKind: win32more.Graphics.CompositionSwapchain.CompositionFrameInstanceKind
    finalTransform: win32more.Graphics.CompositionSwapchain.PresentationTransform
    requiredCrossAdapterCopy: Byte
    colorSpace: win32more.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE
CompositionFrameInstanceKind = Int32
CompositionFrameInstanceKind_ComposedOnScreen: CompositionFrameInstanceKind = 0
CompositionFrameInstanceKind_ScanoutOnScreen: CompositionFrameInstanceKind = 1
CompositionFrameInstanceKind_ComposedToIntermediate: CompositionFrameInstanceKind = 2
class ICompositionFramePresentStatistics(c_void_p):
    extends: win32more.Graphics.CompositionSwapchain.IPresentStatistics
    Guid = Guid('ab41d127-c101-4c0a-91-1d-f9-f2-e9-d0-8e-64')
    @commethod(5)
    def GetContentTag() -> UIntPtr: ...
    @commethod(6)
    def GetCompositionFrameId() -> UInt64: ...
    @commethod(7)
    def GetDisplayInstanceArray(displayInstanceArrayCount: POINTER(UInt32), displayInstanceArray: POINTER(POINTER(win32more.Graphics.CompositionSwapchain.CompositionFrameDisplayInstance_head))) -> Void: ...
class IIndependentFlipFramePresentStatistics(c_void_p):
    extends: win32more.Graphics.CompositionSwapchain.IPresentStatistics
    Guid = Guid('8c93be27-ad94-4da0-8f-d4-24-13-13-2d-12-4e')
    @commethod(5)
    def GetOutputAdapterLUID() -> win32more.Foundation.LUID: ...
    @commethod(6)
    def GetOutputVidPnSourceId() -> UInt32: ...
    @commethod(7)
    def GetContentTag() -> UIntPtr: ...
    @commethod(8)
    def GetDisplayedTime() -> win32more.Graphics.CompositionSwapchain.SystemInterruptTime: ...
    @commethod(9)
    def GetPresentDuration() -> win32more.Graphics.CompositionSwapchain.SystemInterruptTime: ...
class IPresentationBuffer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2e217d3a-5abb-4138-9a-13-a7-75-59-3c-89-ca')
    @commethod(3)
    def GetAvailableEvent(availableEventHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def IsAvailable(isAvailable: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IPresentationContent(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5668bb79-3d8e-415c-b2-15-f3-80-20-f2-d2-52')
    @commethod(3)
    def SetTag(tag: UIntPtr) -> Void: ...
class IPresentationFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8fb37b58-1d74-4f64-a4-9c-1f-97-a8-0a-2e-c0')
    @commethod(3)
    def IsPresentationSupported() -> Byte: ...
    @commethod(4)
    def IsPresentationSupportedWithIndependentFlip() -> Byte: ...
    @commethod(5)
    def CreatePresentationManager(ppPresentationManager: POINTER(win32more.Graphics.CompositionSwapchain.IPresentationManager_head)) -> win32more.Foundation.HRESULT: ...
class IPresentationManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fb562f82-6292-470a-88-b1-84-36-61-e7-f2-0c')
    @commethod(3)
    def AddBufferFromResource(resource: win32more.System.Com.IUnknown_head, presentationBuffer: POINTER(win32more.Graphics.CompositionSwapchain.IPresentationBuffer_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePresentationSurface(compositionSurfaceHandle: win32more.Foundation.HANDLE, presentationSurface: POINTER(win32more.Graphics.CompositionSwapchain.IPresentationSurface_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetNextPresentId() -> UInt64: ...
    @commethod(6)
    def SetTargetTime(targetTime: win32more.Graphics.CompositionSwapchain.SystemInterruptTime) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetPreferredPresentDuration(preferredDuration: win32more.Graphics.CompositionSwapchain.SystemInterruptTime, deviationTolerance: win32more.Graphics.CompositionSwapchain.SystemInterruptTime) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ForceVSyncInterrupt(forceVsyncInterrupt: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Present() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetPresentRetiringFence(riid: POINTER(Guid), fence: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CancelPresentsFrom(presentIdToCancelFrom: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetLostEvent(lostEventHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetPresentStatisticsAvailableEvent(presentStatisticsAvailableEventHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def EnablePresentStatisticsKind(presentStatisticsKind: win32more.Graphics.CompositionSwapchain.PresentStatisticsKind, enabled: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetNextPresentStatistics(nextPresentStatistics: POINTER(win32more.Graphics.CompositionSwapchain.IPresentStatistics_head)) -> win32more.Foundation.HRESULT: ...
class IPresentationSurface(c_void_p):
    extends: win32more.Graphics.CompositionSwapchain.IPresentationContent
    Guid = Guid('956710fb-ea40-4eba-a3-eb-43-75-a0-eb-4e-dc')
    @commethod(4)
    def SetBuffer(presentationBuffer: win32more.Graphics.CompositionSwapchain.IPresentationBuffer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetColorSpace(colorSpace: win32more.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetAlphaMode(alphaMode: win32more.Graphics.Dxgi.Common.DXGI_ALPHA_MODE) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetSourceRect(sourceRect: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetTransform(transform: POINTER(win32more.Graphics.CompositionSwapchain.PresentationTransform_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def RestrictToOutput(output: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetDisableReadback(value: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetLetterboxingMargins(leftLetterboxSize: Single, topLetterboxSize: Single, rightLetterboxSize: Single, bottomLetterboxSize: Single) -> win32more.Foundation.HRESULT: ...
class IPresentStatistics(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b44b8bda-7282-495d-9d-d7-ce-ad-d8-b4-bb-86')
    @commethod(3)
    def GetPresentId() -> UInt64: ...
    @commethod(4)
    def GetKind() -> win32more.Graphics.CompositionSwapchain.PresentStatisticsKind: ...
class IPresentStatusPresentStatistics(c_void_p):
    extends: win32more.Graphics.CompositionSwapchain.IPresentStatistics
    Guid = Guid('c9ed2a41-79cb-435e-96-4e-c8-55-30-55-42-0c')
    @commethod(5)
    def GetCompositionFrameId() -> UInt64: ...
    @commethod(6)
    def GetPresentStatus() -> win32more.Graphics.CompositionSwapchain.PresentStatus: ...
class PresentationTransform(Structure):
    M11: Single
    M12: Single
    M21: Single
    M22: Single
    M31: Single
    M32: Single
PresentStatisticsKind = Int32
PresentStatisticsKind_PresentStatus: PresentStatisticsKind = 1
PresentStatisticsKind_CompositionFrame: PresentStatisticsKind = 2
PresentStatisticsKind_IndependentFlipFrame: PresentStatisticsKind = 3
PresentStatus = Int32
PresentStatus_Queued: PresentStatus = 0
PresentStatus_Skipped: PresentStatus = 1
PresentStatus_Canceled: PresentStatus = 2
class SystemInterruptTime(Structure):
    value: UInt64
make_head(_module, 'CompositionFrameDisplayInstance')
make_head(_module, 'ICompositionFramePresentStatistics')
make_head(_module, 'IIndependentFlipFramePresentStatistics')
make_head(_module, 'IPresentationBuffer')
make_head(_module, 'IPresentationContent')
make_head(_module, 'IPresentationFactory')
make_head(_module, 'IPresentationManager')
make_head(_module, 'IPresentationSurface')
make_head(_module, 'IPresentStatistics')
make_head(_module, 'IPresentStatusPresentStatistics')
make_head(_module, 'PresentationTransform')
make_head(_module, 'SystemInterruptTime')
__all__ = [
    "CompositionFrameDisplayInstance",
    "CompositionFrameInstanceKind",
    "CompositionFrameInstanceKind_ComposedOnScreen",
    "CompositionFrameInstanceKind_ComposedToIntermediate",
    "CompositionFrameInstanceKind_ScanoutOnScreen",
    "CreatePresentationFactory",
    "ICompositionFramePresentStatistics",
    "IIndependentFlipFramePresentStatistics",
    "IPresentStatistics",
    "IPresentStatusPresentStatistics",
    "IPresentationBuffer",
    "IPresentationContent",
    "IPresentationFactory",
    "IPresentationManager",
    "IPresentationSurface",
    "PresentStatisticsKind",
    "PresentStatisticsKind_CompositionFrame",
    "PresentStatisticsKind_IndependentFlipFrame",
    "PresentStatisticsKind_PresentStatus",
    "PresentStatus",
    "PresentStatus_Canceled",
    "PresentStatus_Queued",
    "PresentStatus_Skipped",
    "PresentationTransform",
    "SystemInterruptTime",
]
