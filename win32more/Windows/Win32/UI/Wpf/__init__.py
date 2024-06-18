from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Dwm
import win32more.Windows.Win32.Graphics.Imaging
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.Wpf
MILBITMAPEFFECT_SDK_VERSION: UInt32 = 16777216
CLSID_MILBitmapEffectGroup: Guid = Guid('{ac9c1a9a-7e18-4f64-ac7e-47cf7f051e95}')
CLSID_MILBitmapEffectBlur: Guid = Guid('{a924df87-225d-4373-8f5b-b90ec85ae3de}')
CLSID_MILBitmapEffectDropShadow: Guid = Guid('{459a3fbe-d8ac-4692-874b-7a265715aa16}')
CLSID_MILBitmapEffectOuterGlow: Guid = Guid('{e2161bdd-7eb6-4725-9c0b-8a2a1b4f0667}')
CLSID_MILBitmapEffectBevel: Guid = Guid('{fd361dbe-6c9b-4de0-8290-f6400c2737ed}')
CLSID_MILBitmapEffectEmboss: Guid = Guid('{cd299846-824f-47ec-a007-12aa767f2816}')
class IMILBitmapEffect(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8a6ff321-c944-4a1b-9944-9954af301258}')
    @commethod(3)
    def GetOutput(self, uiIndex: UInt32, pContext: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext, ppBitmapSource: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetParentEffect(self, ppParentEffect: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetInputSource(self, uiIndex: UInt32, pBitmapSource: win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectConnections(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c2b5d861-9b1a-4374-89b0-dec4874d6a81}')
    @commethod(3)
    def GetInputConnector(self, uiIndex: UInt32, ppConnector: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOutputConnector(self, uiIndex: UInt32, ppConnector: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectConnectionsInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{476b538a-c765-4237-ba4a-d6a880ff0cfc}')
    @commethod(3)
    def GetNumberInputs(self, puiNumInputs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumberOutputs(self, puiNumOutputs: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInputConnectorInfo(self, uiIndex: UInt32, ppConnectorInfo: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectConnectorInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOutputConnectorInfo(self, uiIndex: UInt32, ppConnectorInfo: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectConnectorInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectConnector(ComPtr):
    extends: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectConnectorInfo
    _iid_ = Guid('{f59567b3-76c1-4d47-ba1e-79f955e350ef}')
    @commethod(7)
    def IsConnected(self, pfConnected: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBitmapEffect(self, ppEffect: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffect)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectConnectorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f66d2e4b-b46b-42fc-859e-3da0ecdb3c43}')
    @commethod(3)
    def GetIndex(self, puiIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOptimalFormat(self, pFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNumberFormats(self, pulNumberFormats: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFormat(self, ulIndex: UInt32, pFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2e880dd8-f8ce-457b-8199-d60bb3d7ef98}')
    @commethod(3)
    def PropertyChange(self, pEffect: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffect, bstrPropertyName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DirtyRegion(self, pEffect: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffect, pRect: POINTER(win32more.Windows.Win32.UI.Wpf.MilRectD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{33a9df34-a403-4ec7-b07e-bc0682370845}')
    @commethod(3)
    def CreateEffect(self, pguidEffect: POINTER(Guid), ppEffect: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffect)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateContext(self, ppContext: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateEffectOuter(self, ppEffect: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffect)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectGroup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2f952360-698a-4ac6-81a1-bcfdf08eb8e8}')
    @commethod(3)
    def GetInteriorInputConnector(self, uiIndex: UInt32, ppConnector: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInteriorOutputConnector(self, uiIndex: UInt32, ppConnector: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, pEffect: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffect) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectGroupImpl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{78fed518-1cfc-4807-8b85-6b6e51398f62}')
    @commethod(3)
    def Preprocess(self, pContext: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumberChildren(self, puiNumberChildren: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChildren(self, pChildren: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffects)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectImpl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cc2468f2-9936-47be-b4af-06b5df5dbcbb}')
    @commethod(3)
    def IsInPlaceModificationAllowed(self, pOutputConnector: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector, pfModifyInPlace: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetParentEffect(self, pParentEffect: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectGroup) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInputSource(self, uiIndex: UInt32, ppBitmapSource: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetInputSourceBounds(self, uiIndex: UInt32, pRect: POINTER(win32more.Windows.Win32.UI.Wpf.MilRectD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetInputBitmapSource(self, uiIndex: UInt32, pRenderContext: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext, pfModifyInPlace: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL), ppBitmapSource: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputBitmapSource(self, uiIndex: UInt32, pRenderContext: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext, pfModifyInPlace: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL), ppBitmapSource: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Initialize(self, pInner: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectInputConnector(ComPtr):
    extends: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectConnector
    _iid_ = Guid('{a9b4ecaa-7a3c-45e7-8573-f4b81b60dd6c}')
    @commethod(9)
    def ConnectTo(self, pConnector: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConnection(self, ppConnector: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectInteriorInputConnector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{20287e9e-86a2-4e15-953d-eb1438a5b842}')
    @commethod(3)
    def GetInputConnector(self, pInputConnector: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectInteriorOutputConnector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00bbb6dc-acc9-4bfc-b344-8bee383dfefa}')
    @commethod(3)
    def GetOutputConnector(self, pOutputConnector: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectOutputConnector(ComPtr):
    extends: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectConnector
    _iid_ = Guid('{92957aad-841b-4866-82ec-8752468b07fd}')
    @commethod(9)
    def GetNumberConnections(self, puiNumberConnections: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConnection(self, uiIndex: UInt32, ppConnection: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectOutputConnectorImpl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{21fae777-8b39-4bfa-9f2d-f3941ed36913}')
    @commethod(3)
    def AddBackLink(self, pConnection: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveBackLink(self, pConnection: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectPrimitive(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{67e31025-3091-4dfc-98d6-dd494551461d}')
    @commethod(3)
    def GetOutput(self, uiIndex: UInt32, pContext: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext, pfModifyInPlace: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL), ppBitmapSource: POINTER(win32more.Windows.Win32.Graphics.Imaging.IWICBitmapSource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TransformPoint(self, uiIndex: UInt32, p: POINTER(win32more.Windows.Win32.UI.Wpf.MilPoint2D), fForwardTransform: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pContext: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext, pfPointTransformed: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TransformRect(self, uiIndex: UInt32, p: POINTER(win32more.Windows.Win32.UI.Wpf.MilRectD), fForwardTransform: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pContext: win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def HasAffineTransform(self, uiIndex: UInt32, pfAffine: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def HasInverseTransform(self, uiIndex: UInt32, pfHasInverse: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAffineMatrix(self, uiIndex: UInt32, pMatrix: POINTER(win32more.Windows.Win32.Graphics.Dwm.MilMatrix3x2D)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectPrimitiveImpl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ce41e00b-efa6-44e7-b007-dd042e3ae126}')
    @commethod(3)
    def IsDirty(self, uiOutputIndex: UInt32, pfDirty: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsVolatile(self, uiOutputIndex: UInt32, pfVolatile: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectRenderContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{12a2ec7e-2d33-44b2-b334-1abb7846e390}')
    @commethod(3)
    def SetOutputPixelFormat(self, format: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOutputPixelFormat(self, pFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetUseSoftwareRenderer(self, fSoftware: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetInitialTransform(self, pMatrix: POINTER(win32more.Windows.Win32.UI.Wpf.MILMatrixF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFinalTransform(self, pMatrix: POINTER(win32more.Windows.Win32.UI.Wpf.MILMatrixF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetOutputDPI(self, dblDpiX: Double, dblDpiY: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetOutputDPI(self, pdblDpiX: POINTER(Double), pdblDpiY: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetRegionOfInterest(self, pRect: POINTER(win32more.Windows.Win32.UI.Wpf.MilRectD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectRenderContextImpl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4d25accb-797d-4fd2-b128-dffeff84fcc3}')
    @commethod(3)
    def GetUseSoftwareRenderer(self, pfSoftware: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransform(self, pMatrix: POINTER(win32more.Windows.Win32.UI.Wpf.MILMatrixF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateTransform(self, pMatrix: POINTER(win32more.Windows.Win32.UI.Wpf.MILMatrixF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOutputBounds(self, pRect: POINTER(win32more.Windows.Win32.UI.Wpf.MilRectD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UpdateOutputBounds(self, pRect: POINTER(win32more.Windows.Win32.UI.Wpf.MilRectD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffects(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51ac3dce-67c5-448b-9180-ad3eabddd5dd}')
    @commethod(3)
    def _NewEnum(self, ppiuReturn: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Parent(self, ppEffect: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffectGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Item(self, uindex: UInt32, ppEffect: POINTER(win32more.Windows.Win32.UI.Wpf.IMILBitmapEffect)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(self, puiCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class MILMatrixF(Structure):
    _11: Double
    _12: Double
    _13: Double
    _14: Double
    _21: Double
    _22: Double
    _23: Double
    _24: Double
    _31: Double
    _32: Double
    _33: Double
    _34: Double
    _41: Double
    _42: Double
    _43: Double
    _44: Double
class MilPoint2D(Structure):
    X: Double
    Y: Double
class MilRectD(Structure):
    left: Double
    top: Double
    right: Double
    bottom: Double


make_ready(__name__)
