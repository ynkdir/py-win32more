from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.CompositionSwapchain
import win32more.Windows.Win32.Graphics.Dxgi.Common
import win32more.Windows.Win32.System.Com
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
def CreatePresentationFactory(d3dDevice: win32more.Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), presentationFactory: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class CompositionFrameDisplayInstance(EasyCastStructure):
    displayAdapterLUID: win32more.Windows.Win32.Foundation.LUID
    displayVidPnSourceId: UInt32
    displayUniqueId: UInt32
    renderAdapterLUID: win32more.Windows.Win32.Foundation.LUID
    instanceKind: win32more.Windows.Win32.Graphics.CompositionSwapchain.CompositionFrameInstanceKind
    finalTransform: win32more.Windows.Win32.Graphics.CompositionSwapchain.PresentationTransform
    requiredCrossAdapterCopy: Byte
    colorSpace: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE
CompositionFrameInstanceKind = Int32
CompositionFrameInstanceKind_ComposedOnScreen: CompositionFrameInstanceKind = 0
CompositionFrameInstanceKind_ScanoutOnScreen: CompositionFrameInstanceKind = 1
CompositionFrameInstanceKind_ComposedToIntermediate: CompositionFrameInstanceKind = 2
class ICompositionFramePresentStatistics(ComPtr):
    extends: win32more.Windows.Win32.Graphics.CompositionSwapchain.IPresentStatistics
    _iid_ = Guid('{ab41d127-c101-4c0a-911d-f9f2e9d08e64}')
    @commethod(5)
    def GetContentTag(self) -> UIntPtr: ...
    @commethod(6)
    def GetCompositionFrameId(self) -> UInt64: ...
    @commethod(7)
    def GetDisplayInstanceArray(self, displayInstanceArrayCount: POINTER(UInt32), displayInstanceArray: POINTER(POINTER(win32more.Windows.Win32.Graphics.CompositionSwapchain.CompositionFrameDisplayInstance_head))) -> Void: ...
class IIndependentFlipFramePresentStatistics(ComPtr):
    extends: win32more.Windows.Win32.Graphics.CompositionSwapchain.IPresentStatistics
    _iid_ = Guid('{8c93be27-ad94-4da0-8fd4-2413132d124e}')
    @commethod(5)
    def GetOutputAdapterLUID(self) -> win32more.Windows.Win32.Foundation.LUID: ...
    @commethod(6)
    def GetOutputVidPnSourceId(self) -> UInt32: ...
    @commethod(7)
    def GetContentTag(self) -> UIntPtr: ...
    @commethod(8)
    def GetDisplayedTime(self) -> win32more.Windows.Win32.Graphics.CompositionSwapchain.SystemInterruptTime: ...
    @commethod(9)
    def GetPresentDuration(self) -> win32more.Windows.Win32.Graphics.CompositionSwapchain.SystemInterruptTime: ...
class IPresentStatistics(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b44b8bda-7282-495d-9dd7-ceadd8b4bb86}')
    @commethod(3)
    def GetPresentId(self) -> UInt64: ...
    @commethod(4)
    def GetKind(self) -> win32more.Windows.Win32.Graphics.CompositionSwapchain.PresentStatisticsKind: ...
class IPresentStatusPresentStatistics(ComPtr):
    extends: win32more.Windows.Win32.Graphics.CompositionSwapchain.IPresentStatistics
    _iid_ = Guid('{c9ed2a41-79cb-435e-964e-c8553055420c}')
    @commethod(5)
    def GetCompositionFrameId(self) -> UInt64: ...
    @commethod(6)
    def GetPresentStatus(self) -> win32more.Windows.Win32.Graphics.CompositionSwapchain.PresentStatus: ...
class IPresentationBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2e217d3a-5abb-4138-9a13-a775593c89ca}')
    @commethod(3)
    def GetAvailableEvent(self, availableEventHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsAvailable(self, isAvailable: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPresentationContent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5668bb79-3d8e-415c-b215-f38020f2d252}')
    @commethod(3)
    def SetTag(self, tag: UIntPtr) -> Void: ...
class IPresentationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8fb37b58-1d74-4f64-a49c-1f97a80a2ec0}')
    @commethod(3)
    def IsPresentationSupported(self) -> Byte: ...
    @commethod(4)
    def IsPresentationSupportedWithIndependentFlip(self) -> Byte: ...
    @commethod(5)
    def CreatePresentationManager(self, ppPresentationManager: POINTER(win32more.Windows.Win32.Graphics.CompositionSwapchain.IPresentationManager_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPresentationManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fb562f82-6292-470a-88b1-843661e7f20c}')
    @commethod(3)
    def AddBufferFromResource(self, resource: win32more.Windows.Win32.System.Com.IUnknown_head, presentationBuffer: POINTER(win32more.Windows.Win32.Graphics.CompositionSwapchain.IPresentationBuffer_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePresentationSurface(self, compositionSurfaceHandle: win32more.Windows.Win32.Foundation.HANDLE, presentationSurface: POINTER(win32more.Windows.Win32.Graphics.CompositionSwapchain.IPresentationSurface_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNextPresentId(self) -> UInt64: ...
    @commethod(6)
    def SetTargetTime(self, targetTime: win32more.Windows.Win32.Graphics.CompositionSwapchain.SystemInterruptTime) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetPreferredPresentDuration(self, preferredDuration: win32more.Windows.Win32.Graphics.CompositionSwapchain.SystemInterruptTime, deviationTolerance: win32more.Windows.Win32.Graphics.CompositionSwapchain.SystemInterruptTime) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ForceVSyncInterrupt(self, forceVsyncInterrupt: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Present(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPresentRetiringFence(self, riid: POINTER(Guid), fence: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CancelPresentsFrom(self, presentIdToCancelFrom: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLostEvent(self, lostEventHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPresentStatisticsAvailableEvent(self, presentStatisticsAvailableEventHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnablePresentStatisticsKind(self, presentStatisticsKind: win32more.Windows.Win32.Graphics.CompositionSwapchain.PresentStatisticsKind, enabled: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetNextPresentStatistics(self, nextPresentStatistics: POINTER(win32more.Windows.Win32.Graphics.CompositionSwapchain.IPresentStatistics_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPresentationSurface(ComPtr):
    extends: win32more.Windows.Win32.Graphics.CompositionSwapchain.IPresentationContent
    _iid_ = Guid('{956710fb-ea40-4eba-a3eb-4375a0eb4edc}')
    @commethod(4)
    def SetBuffer(self, presentationBuffer: win32more.Windows.Win32.Graphics.CompositionSwapchain.IPresentationBuffer_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetColorSpace(self, colorSpace: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAlphaMode(self, alphaMode: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_ALPHA_MODE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetSourceRect(self, sourceRect: POINTER(win32more.Windows.Win32.Foundation.RECT_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetTransform(self, transform: POINTER(win32more.Windows.Win32.Graphics.CompositionSwapchain.PresentationTransform_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RestrictToOutput(self, output: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDisableReadback(self, value: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetLetterboxingMargins(self, leftLetterboxSize: Single, topLetterboxSize: Single, rightLetterboxSize: Single, bottomLetterboxSize: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
