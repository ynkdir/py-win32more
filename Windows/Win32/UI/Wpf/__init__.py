from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Dwm
import Windows.Win32.Graphics.Imaging
import Windows.Win32.System.Com
import Windows.Win32.UI.Wpf
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
MILBITMAPEFFECT_SDK_VERSION: UInt32 = 16777216
CLSID_MILBitmapEffectGroup: Guid = Guid('ac9c1a9a-7e18-4f64-ac-7e-47-cf-7f-05-1e-95')
CLSID_MILBitmapEffectBlur: Guid = Guid('a924df87-225d-4373-8f-5b-b9-0e-c8-5a-e3-de')
CLSID_MILBitmapEffectDropShadow: Guid = Guid('459a3fbe-d8ac-4692-87-4b-7a-26-57-15-aa-16')
CLSID_MILBitmapEffectOuterGlow: Guid = Guid('e2161bdd-7eb6-4725-9c-0b-8a-2a-1b-4f-06-67')
CLSID_MILBitmapEffectBevel: Guid = Guid('fd361dbe-6c9b-4de0-82-90-f6-40-0c-27-37-ed')
CLSID_MILBitmapEffectEmboss: Guid = Guid('cd299846-824f-47ec-a0-07-12-aa-76-7f-28-16')
class IMILBitmapEffect(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8a6ff321-c944-4a1b-99-44-99-54-af-30-12-58')
    @commethod(3)
    def GetOutput(self, uiIndex: UInt32, pContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head, ppBitmapSource: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetParentEffect(self, ppParentEffect: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetInputSource(self, uiIndex: UInt32, pBitmapSource: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectConnections(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c2b5d861-9b1a-4374-89-b0-de-c4-87-4d-6a-81')
    @commethod(3)
    def GetInputConnector(self, uiIndex: UInt32, ppConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOutputConnector(self, uiIndex: UInt32, ppConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectConnectionsInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('476b538a-c765-4237-ba-4a-d6-a8-80-ff-0c-fc')
    @commethod(3)
    def GetNumberInputs(self, puiNumInputs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumberOutputs(self, puiNumOutputs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInputConnectorInfo(self, uiIndex: UInt32, ppConnectorInfo: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectConnectorInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOutputConnectorInfo(self, uiIndex: UInt32, ppConnectorInfo: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectConnectorInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectConnector(ComPtr):
    extends: Windows.Win32.UI.Wpf.IMILBitmapEffectConnectorInfo
    Guid = Guid('f59567b3-76c1-4d47-ba-1e-79-f9-55-e3-50-ef')
    @commethod(7)
    def IsConnected(self, pfConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBitmapEffect(self, ppEffect: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffect_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectConnectorInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f66d2e4b-b46b-42fc-85-9e-3d-a0-ec-db-3c-43')
    @commethod(3)
    def GetIndex(self, puiIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOptimalFormat(self, pFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNumberFormats(self, pulNumberFormats: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFormat(self, ulIndex: UInt32, pFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2e880dd8-f8ce-457b-81-99-d6-0b-b3-d7-ef-98')
    @commethod(3)
    def PropertyChange(self, pEffect: Windows.Win32.UI.Wpf.IMILBitmapEffect_head, bstrPropertyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DirtyRegion(self, pEffect: Windows.Win32.UI.Wpf.IMILBitmapEffect_head, pRect: POINTER(Windows.Win32.UI.Wpf.MilRectD_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('33a9df34-a403-4ec7-b0-7e-bc-06-82-37-08-45')
    @commethod(3)
    def CreateEffect(self, pguidEffect: POINTER(Guid), ppEffect: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateContext(self, ppContext: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateEffectOuter(self, ppEffect: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffect_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectGroup(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2f952360-698a-4ac6-81-a1-bc-fd-f0-8e-b8-e8')
    @commethod(3)
    def GetInteriorInputConnector(self, uiIndex: UInt32, ppConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInteriorOutputConnector(self, uiIndex: UInt32, ppConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, pEffect: Windows.Win32.UI.Wpf.IMILBitmapEffect_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectGroupImpl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('78fed518-1cfc-4807-8b-85-6b-6e-51-39-8f-62')
    @commethod(3)
    def Preprocess(self, pContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumberChildren(self, puiNumberChildren: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChildren(self, pChildren: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffects_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectImpl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cc2468f2-9936-47be-b4-af-06-b5-df-5d-bc-bb')
    @commethod(3)
    def IsInPlaceModificationAllowed(self, pOutputConnector: Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector_head, pfModifyInPlace: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetParentEffect(self, pParentEffect: Windows.Win32.UI.Wpf.IMILBitmapEffectGroup_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInputSource(self, uiIndex: UInt32, ppBitmapSource: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetInputSourceBounds(self, uiIndex: UInt32, pRect: POINTER(Windows.Win32.UI.Wpf.MilRectD_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetInputBitmapSource(self, uiIndex: UInt32, pRenderContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head, pfModifyInPlace: POINTER(Windows.Win32.Foundation.VARIANT_BOOL), ppBitmapSource: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputBitmapSource(self, uiIndex: UInt32, pRenderContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head, pfModifyInPlace: POINTER(Windows.Win32.Foundation.VARIANT_BOOL), ppBitmapSource: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Initialize(self, pInner: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectInputConnector(ComPtr):
    extends: Windows.Win32.UI.Wpf.IMILBitmapEffectConnector
    Guid = Guid('a9b4ecaa-7a3c-45e7-85-73-f4-b8-1b-60-dd-6c')
    @commethod(9)
    def ConnectTo(self, pConnector: Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConnection(self, ppConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectInteriorInputConnector(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('20287e9e-86a2-4e15-95-3d-eb-14-38-a5-b8-42')
    @commethod(3)
    def GetInputConnector(self, pInputConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectInteriorOutputConnector(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00bbb6dc-acc9-4bfc-b3-44-8b-ee-38-3d-fe-fa')
    @commethod(3)
    def GetOutputConnector(self, pOutputConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectOutputConnector(ComPtr):
    extends: Windows.Win32.UI.Wpf.IMILBitmapEffectConnector
    Guid = Guid('92957aad-841b-4866-82-ec-87-52-46-8b-07-fd')
    @commethod(9)
    def GetNumberConnections(self, puiNumberConnections: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConnection(self, uiIndex: UInt32, ppConnection: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectOutputConnectorImpl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('21fae777-8b39-4bfa-9f-2d-f3-94-1e-d3-69-13')
    @commethod(3)
    def AddBackLink(self, pConnection: Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveBackLink(self, pConnection: Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectPrimitive(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('67e31025-3091-4dfc-98-d6-dd-49-45-51-46-1d')
    @commethod(3)
    def GetOutput(self, uiIndex: UInt32, pContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head, pfModifyInPlace: POINTER(Windows.Win32.Foundation.VARIANT_BOOL), ppBitmapSource: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TransformPoint(self, uiIndex: UInt32, p: POINTER(Windows.Win32.UI.Wpf.MilPoint2D_head), fForwardTransform: Windows.Win32.Foundation.VARIANT_BOOL, pContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head, pfPointTransformed: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TransformRect(self, uiIndex: UInt32, p: POINTER(Windows.Win32.UI.Wpf.MilRectD_head), fForwardTransform: Windows.Win32.Foundation.VARIANT_BOOL, pContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def HasAffineTransform(self, uiIndex: UInt32, pfAffine: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def HasInverseTransform(self, uiIndex: UInt32, pfHasInverse: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAffineMatrix(self, uiIndex: UInt32, pMatrix: POINTER(Windows.Win32.Graphics.Dwm.MilMatrix3x2D_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectPrimitiveImpl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ce41e00b-efa6-44e7-b0-07-dd-04-2e-3a-e1-26')
    @commethod(3)
    def IsDirty(self, uiOutputIndex: UInt32, pfDirty: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsVolatile(self, uiOutputIndex: UInt32, pfVolatile: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectRenderContext(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('12a2ec7e-2d33-44b2-b3-34-1a-bb-78-46-e3-90')
    @commethod(3)
    def SetOutputPixelFormat(self, format: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOutputPixelFormat(self, pFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetUseSoftwareRenderer(self, fSoftware: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetInitialTransform(self, pMatrix: POINTER(Windows.Win32.UI.Wpf.MILMatrixF_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFinalTransform(self, pMatrix: POINTER(Windows.Win32.UI.Wpf.MILMatrixF_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetOutputDPI(self, dblDpiX: Double, dblDpiY: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetOutputDPI(self, pdblDpiX: POINTER(Double), pdblDpiY: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetRegionOfInterest(self, pRect: POINTER(Windows.Win32.UI.Wpf.MilRectD_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectRenderContextImpl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4d25accb-797d-4fd2-b1-28-df-fe-ff-84-fc-c3')
    @commethod(3)
    def GetUseSoftwareRenderer(self, pfSoftware: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransform(self, pMatrix: POINTER(Windows.Win32.UI.Wpf.MILMatrixF_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateTransform(self, pMatrix: POINTER(Windows.Win32.UI.Wpf.MILMatrixF_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOutputBounds(self, pRect: POINTER(Windows.Win32.UI.Wpf.MilRectD_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UpdateOutputBounds(self, pRect: POINTER(Windows.Win32.UI.Wpf.MilRectD_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffects(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('51ac3dce-67c5-448b-91-80-ad-3e-ab-dd-d5-dd')
    @commethod(3)
    def _NewEnum(self, ppiuReturn: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Parent(self, ppEffect: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Item(self, uindex: UInt32, ppEffect: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(self, puiCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class MILMatrixF(EasyCastStructure):
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
class MilPoint2D(EasyCastStructure):
    X: Double
    Y: Double
class MilRectD(EasyCastStructure):
    left: Double
    top: Double
    right: Double
    bottom: Double
make_head(_module, 'IMILBitmapEffect')
make_head(_module, 'IMILBitmapEffectConnections')
make_head(_module, 'IMILBitmapEffectConnectionsInfo')
make_head(_module, 'IMILBitmapEffectConnector')
make_head(_module, 'IMILBitmapEffectConnectorInfo')
make_head(_module, 'IMILBitmapEffectEvents')
make_head(_module, 'IMILBitmapEffectFactory')
make_head(_module, 'IMILBitmapEffectGroup')
make_head(_module, 'IMILBitmapEffectGroupImpl')
make_head(_module, 'IMILBitmapEffectImpl')
make_head(_module, 'IMILBitmapEffectInputConnector')
make_head(_module, 'IMILBitmapEffectInteriorInputConnector')
make_head(_module, 'IMILBitmapEffectInteriorOutputConnector')
make_head(_module, 'IMILBitmapEffectOutputConnector')
make_head(_module, 'IMILBitmapEffectOutputConnectorImpl')
make_head(_module, 'IMILBitmapEffectPrimitive')
make_head(_module, 'IMILBitmapEffectPrimitiveImpl')
make_head(_module, 'IMILBitmapEffectRenderContext')
make_head(_module, 'IMILBitmapEffectRenderContextImpl')
make_head(_module, 'IMILBitmapEffects')
make_head(_module, 'MILMatrixF')
make_head(_module, 'MilPoint2D')
make_head(_module, 'MilRectD')
