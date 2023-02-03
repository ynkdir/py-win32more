from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
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
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
MILBITMAPEFFECT_SDK_VERSION: UInt32 = 16777216
CLSID_MILBitmapEffectGroup: Guid = Guid('ac9c1a9a-7e18-4f64-ac-7e-47-cf-7f-05-1e-95')
CLSID_MILBitmapEffectBlur: Guid = Guid('a924df87-225d-4373-8f-5b-b9-0e-c8-5a-e3-de')
CLSID_MILBitmapEffectDropShadow: Guid = Guid('459a3fbe-d8ac-4692-87-4b-7a-26-57-15-aa-16')
CLSID_MILBitmapEffectOuterGlow: Guid = Guid('e2161bdd-7eb6-4725-9c-0b-8a-2a-1b-4f-06-67')
CLSID_MILBitmapEffectBevel: Guid = Guid('fd361dbe-6c9b-4de0-82-90-f6-40-0c-27-37-ed')
CLSID_MILBitmapEffectEmboss: Guid = Guid('cd299846-824f-47ec-a0-07-12-aa-76-7f-28-16')
class IMILBitmapEffect(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8a6ff321-c944-4a1b-99-44-99-54-af-30-12-58')
    @commethod(3)
    def GetOutput(uiIndex: UInt32, pContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head, ppBitmapSource: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetParentEffect(ppParentEffect: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetInputSource(uiIndex: UInt32, pBitmapSource: Windows.Win32.Graphics.Imaging.IWICBitmapSource_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectConnections(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c2b5d861-9b1a-4374-89-b0-de-c4-87-4d-6a-81')
    @commethod(3)
    def GetInputConnector(uiIndex: UInt32, ppConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOutputConnector(uiIndex: UInt32, ppConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectConnectionsInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('476b538a-c765-4237-ba-4a-d6-a8-80-ff-0c-fc')
    @commethod(3)
    def GetNumberInputs(puiNumInputs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumberOutputs(puiNumOutputs: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInputConnectorInfo(uiIndex: UInt32, ppConnectorInfo: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectConnectorInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOutputConnectorInfo(uiIndex: UInt32, ppConnectorInfo: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectConnectorInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectConnector(c_void_p):
    extends: Windows.Win32.UI.Wpf.IMILBitmapEffectConnectorInfo
    Guid = Guid('f59567b3-76c1-4d47-ba-1e-79-f9-55-e3-50-ef')
    @commethod(7)
    def IsConnected(pfConnected: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBitmapEffect(ppEffect: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffect_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectConnectorInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f66d2e4b-b46b-42fc-85-9e-3d-a0-ec-db-3c-43')
    @commethod(3)
    def GetIndex(puiIndex: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOptimalFormat(pFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNumberFormats(pulNumberFormats: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFormat(ulIndex: UInt32, pFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2e880dd8-f8ce-457b-81-99-d6-0b-b3-d7-ef-98')
    @commethod(3)
    def PropertyChange(pEffect: Windows.Win32.UI.Wpf.IMILBitmapEffect_head, bstrPropertyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DirtyRegion(pEffect: Windows.Win32.UI.Wpf.IMILBitmapEffect_head, pRect: POINTER(Windows.Win32.UI.Wpf.MilRectD_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('33a9df34-a403-4ec7-b0-7e-bc-06-82-37-08-45')
    @commethod(3)
    def CreateEffect(pguidEffect: POINTER(Guid), ppEffect: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateContext(ppContext: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateEffectOuter(ppEffect: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffect_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectGroup(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2f952360-698a-4ac6-81-a1-bc-fd-f0-8e-b8-e8')
    @commethod(3)
    def GetInteriorInputConnector(uiIndex: UInt32, ppConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInteriorOutputConnector(uiIndex: UInt32, ppConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(pEffect: Windows.Win32.UI.Wpf.IMILBitmapEffect_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectGroupImpl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('78fed518-1cfc-4807-8b-85-6b-6e-51-39-8f-62')
    @commethod(3)
    def Preprocess(pContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumberChildren(puiNumberChildren: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChildren(pChildren: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffects_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectImpl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cc2468f2-9936-47be-b4-af-06-b5-df-5d-bc-bb')
    @commethod(3)
    def IsInPlaceModificationAllowed(pOutputConnector: Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector_head, pfModifyInPlace: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetParentEffect(pParentEffect: Windows.Win32.UI.Wpf.IMILBitmapEffectGroup_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInputSource(uiIndex: UInt32, ppBitmapSource: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetInputSourceBounds(uiIndex: UInt32, pRect: POINTER(Windows.Win32.UI.Wpf.MilRectD_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetInputBitmapSource(uiIndex: UInt32, pRenderContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head, pfModifyInPlace: POINTER(Windows.Win32.Foundation.VARIANT_BOOL), ppBitmapSource: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetOutputBitmapSource(uiIndex: UInt32, pRenderContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head, pfModifyInPlace: POINTER(Windows.Win32.Foundation.VARIANT_BOOL), ppBitmapSource: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Initialize(pInner: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectInputConnector(c_void_p):
    extends: Windows.Win32.UI.Wpf.IMILBitmapEffectConnector
    Guid = Guid('a9b4ecaa-7a3c-45e7-85-73-f4-b8-1b-60-dd-6c')
    @commethod(9)
    def ConnectTo(pConnector: Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConnection(ppConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectInteriorInputConnector(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('20287e9e-86a2-4e15-95-3d-eb-14-38-a5-b8-42')
    @commethod(3)
    def GetInputConnector(pInputConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectInteriorOutputConnector(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00bbb6dc-acc9-4bfc-b3-44-8b-ee-38-3d-fe-fa')
    @commethod(3)
    def GetOutputConnector(pOutputConnector: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectOutputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectOutputConnector(c_void_p):
    extends: Windows.Win32.UI.Wpf.IMILBitmapEffectConnector
    Guid = Guid('92957aad-841b-4866-82-ec-87-52-46-8b-07-fd')
    @commethod(9)
    def GetNumberConnections(puiNumberConnections: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConnection(uiIndex: UInt32, ppConnection: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectOutputConnectorImpl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('21fae777-8b39-4bfa-9f-2d-f3-94-1e-d3-69-13')
    @commethod(3)
    def AddBackLink(pConnection: Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveBackLink(pConnection: Windows.Win32.UI.Wpf.IMILBitmapEffectInputConnector_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectPrimitive(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('67e31025-3091-4dfc-98-d6-dd-49-45-51-46-1d')
    @commethod(3)
    def GetOutput(uiIndex: UInt32, pContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head, pfModifyInPlace: POINTER(Windows.Win32.Foundation.VARIANT_BOOL), ppBitmapSource: POINTER(Windows.Win32.Graphics.Imaging.IWICBitmapSource_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TransformPoint(uiIndex: UInt32, p: POINTER(Windows.Win32.UI.Wpf.MilPoint2D_head), fForwardTransform: Windows.Win32.Foundation.VARIANT_BOOL, pContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head, pfPointTransformed: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TransformRect(uiIndex: UInt32, p: POINTER(Windows.Win32.UI.Wpf.MilRectD_head), fForwardTransform: Windows.Win32.Foundation.VARIANT_BOOL, pContext: Windows.Win32.UI.Wpf.IMILBitmapEffectRenderContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def HasAffineTransform(uiIndex: UInt32, pfAffine: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def HasInverseTransform(uiIndex: UInt32, pfHasInverse: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAffineMatrix(uiIndex: UInt32, pMatrix: POINTER(Windows.Win32.Graphics.Dwm.MilMatrix3x2D_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectPrimitiveImpl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ce41e00b-efa6-44e7-b0-07-dd-04-2e-3a-e1-26')
    @commethod(3)
    def IsDirty(uiOutputIndex: UInt32, pfDirty: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsVolatile(uiOutputIndex: UInt32, pfVolatile: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectRenderContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('12a2ec7e-2d33-44b2-b3-34-1a-bb-78-46-e3-90')
    @commethod(3)
    def SetOutputPixelFormat(format: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOutputPixelFormat(pFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetUseSoftwareRenderer(fSoftware: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetInitialTransform(pMatrix: POINTER(Windows.Win32.UI.Wpf.MILMatrixF_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFinalTransform(pMatrix: POINTER(Windows.Win32.UI.Wpf.MILMatrixF_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetOutputDPI(dblDpiX: Double, dblDpiY: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetOutputDPI(pdblDpiX: POINTER(Double), pdblDpiY: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetRegionOfInterest(pRect: POINTER(Windows.Win32.UI.Wpf.MilRectD_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffectRenderContextImpl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4d25accb-797d-4fd2-b1-28-df-fe-ff-84-fc-c3')
    @commethod(3)
    def GetUseSoftwareRenderer(pfSoftware: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTransform(pMatrix: POINTER(Windows.Win32.UI.Wpf.MILMatrixF_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateTransform(pMatrix: POINTER(Windows.Win32.UI.Wpf.MILMatrixF_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOutputBounds(pRect: POINTER(Windows.Win32.UI.Wpf.MilRectD_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UpdateOutputBounds(pRect: POINTER(Windows.Win32.UI.Wpf.MilRectD_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMILBitmapEffects(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('51ac3dce-67c5-448b-91-80-ad-3e-ab-dd-d5-dd')
    @commethod(3)
    def _NewEnum(ppiuReturn: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Parent(ppEffect: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffectGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Item(uindex: UInt32, ppEffect: POINTER(Windows.Win32.UI.Wpf.IMILBitmapEffect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Count(puiCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
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
__all__ = [
    "CLSID_MILBitmapEffectBevel",
    "CLSID_MILBitmapEffectBlur",
    "CLSID_MILBitmapEffectDropShadow",
    "CLSID_MILBitmapEffectEmboss",
    "CLSID_MILBitmapEffectGroup",
    "CLSID_MILBitmapEffectOuterGlow",
    "IMILBitmapEffect",
    "IMILBitmapEffectConnections",
    "IMILBitmapEffectConnectionsInfo",
    "IMILBitmapEffectConnector",
    "IMILBitmapEffectConnectorInfo",
    "IMILBitmapEffectEvents",
    "IMILBitmapEffectFactory",
    "IMILBitmapEffectGroup",
    "IMILBitmapEffectGroupImpl",
    "IMILBitmapEffectImpl",
    "IMILBitmapEffectInputConnector",
    "IMILBitmapEffectInteriorInputConnector",
    "IMILBitmapEffectInteriorOutputConnector",
    "IMILBitmapEffectOutputConnector",
    "IMILBitmapEffectOutputConnectorImpl",
    "IMILBitmapEffectPrimitive",
    "IMILBitmapEffectPrimitiveImpl",
    "IMILBitmapEffectRenderContext",
    "IMILBitmapEffectRenderContextImpl",
    "IMILBitmapEffects",
    "MILBITMAPEFFECT_SDK_VERSION",
    "MILMatrixF",
    "MilPoint2D",
    "MilRectD",
]
_arch_optional = [
]
