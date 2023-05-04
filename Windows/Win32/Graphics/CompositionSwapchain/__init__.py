from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.CompositionSwapchain
import Windows.Win32.Graphics.Dxgi.Common
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('dcomp.dll')
def CreatePresentationFactory(d3dDevice: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), presentationFactory: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class CompositionFrameDisplayInstance(EasyCastStructure):
    displayAdapterLUID: Windows.Win32.Foundation.LUID
    displayVidPnSourceId: UInt32
    displayUniqueId: UInt32
    renderAdapterLUID: Windows.Win32.Foundation.LUID
    instanceKind: Windows.Win32.Graphics.CompositionSwapchain.CompositionFrameInstanceKind
    finalTransform: Windows.Win32.Graphics.CompositionSwapchain.PresentationTransform
    requiredCrossAdapterCopy: Byte
    colorSpace: Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE
CompositionFrameInstanceKind = Int32
CompositionFrameInstanceKind_ComposedOnScreen: CompositionFrameInstanceKind = 0
CompositionFrameInstanceKind_ScanoutOnScreen: CompositionFrameInstanceKind = 1
CompositionFrameInstanceKind_ComposedToIntermediate: CompositionFrameInstanceKind = 2
class ICompositionFramePresentStatistics(ComPtr):
    extends: Windows.Win32.Graphics.CompositionSwapchain.IPresentStatistics
    _iid_ = Guid('{ab41d127-c101-4c0a-911d-f9f2e9d08e64}')
    @commethod(5)
    def GetContentTag(self) -> UIntPtr: ...
    @commethod(6)
    def GetCompositionFrameId(self) -> UInt64: ...
    @commethod(7)
    def GetDisplayInstanceArray(self, displayInstanceArrayCount: POINTER(UInt32), displayInstanceArray: POINTER(POINTER(Windows.Win32.Graphics.CompositionSwapchain.CompositionFrameDisplayInstance_head))) -> Void: ...
class IIndependentFlipFramePresentStatistics(ComPtr):
    extends: Windows.Win32.Graphics.CompositionSwapchain.IPresentStatistics
    _iid_ = Guid('{8c93be27-ad94-4da0-8fd4-2413132d124e}')
    @commethod(5)
    def GetOutputAdapterLUID(self) -> Windows.Win32.Foundation.LUID: ...
    @commethod(6)
    def GetOutputVidPnSourceId(self) -> UInt32: ...
    @commethod(7)
    def GetContentTag(self) -> UIntPtr: ...
    @commethod(8)
    def GetDisplayedTime(self) -> Windows.Win32.Graphics.CompositionSwapchain.SystemInterruptTime: ...
    @commethod(9)
    def GetPresentDuration(self) -> Windows.Win32.Graphics.CompositionSwapchain.SystemInterruptTime: ...
class IPresentStatistics(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b44b8bda-7282-495d-9dd7-ceadd8b4bb86}')
    @commethod(3)
    def GetPresentId(self) -> UInt64: ...
    @commethod(4)
    def GetKind(self) -> Windows.Win32.Graphics.CompositionSwapchain.PresentStatisticsKind: ...
class IPresentStatusPresentStatistics(ComPtr):
    extends: Windows.Win32.Graphics.CompositionSwapchain.IPresentStatistics
    _iid_ = Guid('{c9ed2a41-79cb-435e-964e-c8553055420c}')
    @commethod(5)
    def GetCompositionFrameId(self) -> UInt64: ...
    @commethod(6)
    def GetPresentStatus(self) -> Windows.Win32.Graphics.CompositionSwapchain.PresentStatus: ...
class IPresentationBuffer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2e217d3a-5abb-4138-9a13-a775593c89ca}')
    @commethod(3)
    def GetAvailableEvent(self, availableEventHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsAvailable(self, isAvailable: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
class IPresentationContent(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5668bb79-3d8e-415c-b215-f38020f2d252}')
    @commethod(3)
    def SetTag(self, tag: UIntPtr) -> Void: ...
class IPresentationFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8fb37b58-1d74-4f64-a49c-1f97a80a2ec0}')
    @commethod(3)
    def IsPresentationSupported(self) -> Byte: ...
    @commethod(4)
    def IsPresentationSupportedWithIndependentFlip(self) -> Byte: ...
    @commethod(5)
    def CreatePresentationManager(self, ppPresentationManager: POINTER(Windows.Win32.Graphics.CompositionSwapchain.IPresentationManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPresentationManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fb562f82-6292-470a-88b1-843661e7f20c}')
    @commethod(3)
    def AddBufferFromResource(self, resource: Windows.Win32.System.Com.IUnknown_head, presentationBuffer: POINTER(Windows.Win32.Graphics.CompositionSwapchain.IPresentationBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePresentationSurface(self, compositionSurfaceHandle: Windows.Win32.Foundation.HANDLE, presentationSurface: POINTER(Windows.Win32.Graphics.CompositionSwapchain.IPresentationSurface_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNextPresentId(self) -> UInt64: ...
    @commethod(6)
    def SetTargetTime(self, targetTime: Windows.Win32.Graphics.CompositionSwapchain.SystemInterruptTime) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetPreferredPresentDuration(self, preferredDuration: Windows.Win32.Graphics.CompositionSwapchain.SystemInterruptTime, deviationTolerance: Windows.Win32.Graphics.CompositionSwapchain.SystemInterruptTime) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ForceVSyncInterrupt(self, forceVsyncInterrupt: Byte) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Present(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPresentRetiringFence(self, riid: POINTER(Guid), fence: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CancelPresentsFrom(self, presentIdToCancelFrom: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLostEvent(self, lostEventHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPresentStatisticsAvailableEvent(self, presentStatisticsAvailableEventHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnablePresentStatisticsKind(self, presentStatisticsKind: Windows.Win32.Graphics.CompositionSwapchain.PresentStatisticsKind, enabled: Byte) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetNextPresentStatistics(self, nextPresentStatistics: POINTER(Windows.Win32.Graphics.CompositionSwapchain.IPresentStatistics_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPresentationSurface(ComPtr):
    extends: Windows.Win32.Graphics.CompositionSwapchain.IPresentationContent
    _iid_ = Guid('{956710fb-ea40-4eba-a3eb-4375a0eb4edc}')
    @commethod(4)
    def SetBuffer(self, presentationBuffer: Windows.Win32.Graphics.CompositionSwapchain.IPresentationBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetColorSpace(self, colorSpace: Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAlphaMode(self, alphaMode: Windows.Win32.Graphics.Dxgi.Common.DXGI_ALPHA_MODE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetSourceRect(self, sourceRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetTransform(self, transform: POINTER(Windows.Win32.Graphics.CompositionSwapchain.PresentationTransform_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RestrictToOutput(self, output: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDisableReadback(self, value: Byte) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetLetterboxingMargins(self, leftLetterboxSize: Single, topLetterboxSize: Single, rightLetterboxSize: Single, bottomLetterboxSize: Single) -> Windows.Win32.Foundation.HRESULT: ...
PresentStatisticsKind = Int32
PresentStatisticsKind_PresentStatus: PresentStatisticsKind = 1
PresentStatisticsKind_CompositionFrame: PresentStatisticsKind = 2
PresentStatisticsKind_IndependentFlipFrame: PresentStatisticsKind = 3
PresentStatus = Int32
PresentStatus_Queued: PresentStatus = 0
PresentStatus_Skipped: PresentStatus = 1
PresentStatus_Canceled: PresentStatus = 2
class PresentationTransform(EasyCastStructure):
    M11: Single
    M12: Single
    M21: Single
    M22: Single
    M31: Single
    M32: Single
class SystemInterruptTime(EasyCastStructure):
    value: UInt64
make_head(_module, 'CompositionFrameDisplayInstance')
make_head(_module, 'ICompositionFramePresentStatistics')
make_head(_module, 'IIndependentFlipFramePresentStatistics')
make_head(_module, 'IPresentStatistics')
make_head(_module, 'IPresentStatusPresentStatistics')
make_head(_module, 'IPresentationBuffer')
make_head(_module, 'IPresentationContent')
make_head(_module, 'IPresentationFactory')
make_head(_module, 'IPresentationManager')
make_head(_module, 'IPresentationSurface')
make_head(_module, 'PresentationTransform')
make_head(_module, 'SystemInterruptTime')
