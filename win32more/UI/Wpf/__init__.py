from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Dwm
import win32more.Graphics.Imaging
import win32more.System.Com
import win32more.UI.Wpf
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
MILBITMAPEFFECT_SDK_VERSION = 16777216
def _define_CLSID_MILBitmapEffectGroup():
    return Guid('ac9c1a9a-7e18-4f64-ac-7e-47-cf-7f-05-1e-95')
def _define_CLSID_MILBitmapEffectBlur():
    return Guid('a924df87-225d-4373-8f-5b-b9-0e-c8-5a-e3-de')
def _define_CLSID_MILBitmapEffectDropShadow():
    return Guid('459a3fbe-d8ac-4692-87-4b-7a-26-57-15-aa-16')
def _define_CLSID_MILBitmapEffectOuterGlow():
    return Guid('e2161bdd-7eb6-4725-9c-0b-8a-2a-1b-4f-06-67')
def _define_CLSID_MILBitmapEffectBevel():
    return Guid('fd361dbe-6c9b-4de0-82-90-f6-40-0c-27-37-ed')
def _define_CLSID_MILBitmapEffectEmboss():
    return Guid('cd299846-824f-47ec-a0-07-12-aa-76-7f-28-16')
def _define_IMILBitmapEffect_head():
    class IMILBitmapEffect(win32more.System.Com.IUnknown_head):
        Guid = Guid('8a6ff321-c944-4a1b-99-44-99-54-af-30-12-58')
    return IMILBitmapEffect
def _define_IMILBitmapEffect():
    IMILBitmapEffect = win32more.UI.Wpf.IMILBitmapEffect_head
    IMILBitmapEffect.GetOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.Wpf.IMILBitmapEffectRenderContext_head,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head))(3, 'GetOutput', ((1, 'uiIndex'),(1, 'pContext'),(1, 'ppBitmapSource'),)))
    IMILBitmapEffect.GetParentEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.IMILBitmapEffectGroup_head))(4, 'GetParentEffect', ((1, 'ppParentEffect'),)))
    IMILBitmapEffect.SetInputSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Imaging.IWICBitmapSource_head)(5, 'SetInputSource', ((1, 'uiIndex'),(1, 'pBitmapSource'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffect
def _define_IMILBitmapEffectConnections_head():
    class IMILBitmapEffectConnections(win32more.System.Com.IUnknown_head):
        Guid = Guid('c2b5d861-9b1a-4374-89-b0-de-c4-87-4d-6a-81')
    return IMILBitmapEffectConnections
def _define_IMILBitmapEffectConnections():
    IMILBitmapEffectConnections = win32more.UI.Wpf.IMILBitmapEffectConnections_head
    IMILBitmapEffectConnections.GetInputConnector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Wpf.IMILBitmapEffectInputConnector_head))(3, 'GetInputConnector', ((1, 'uiIndex'),(1, 'ppConnector'),)))
    IMILBitmapEffectConnections.GetOutputConnector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Wpf.IMILBitmapEffectOutputConnector_head))(4, 'GetOutputConnector', ((1, 'uiIndex'),(1, 'ppConnector'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectConnections
def _define_IMILBitmapEffectConnectionsInfo_head():
    class IMILBitmapEffectConnectionsInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('476b538a-c765-4237-ba-4a-d6-a8-80-ff-0c-fc')
    return IMILBitmapEffectConnectionsInfo
def _define_IMILBitmapEffectConnectionsInfo():
    IMILBitmapEffectConnectionsInfo = win32more.UI.Wpf.IMILBitmapEffectConnectionsInfo_head
    IMILBitmapEffectConnectionsInfo.GetNumberInputs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetNumberInputs', ((1, 'puiNumInputs'),)))
    IMILBitmapEffectConnectionsInfo.GetNumberOutputs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetNumberOutputs', ((1, 'puiNumOutputs'),)))
    IMILBitmapEffectConnectionsInfo.GetInputConnectorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Wpf.IMILBitmapEffectConnectorInfo_head))(5, 'GetInputConnectorInfo', ((1, 'uiIndex'),(1, 'ppConnectorInfo'),)))
    IMILBitmapEffectConnectionsInfo.GetOutputConnectorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Wpf.IMILBitmapEffectConnectorInfo_head))(6, 'GetOutputConnectorInfo', ((1, 'uiIndex'),(1, 'ppConnectorInfo'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectConnectionsInfo
def _define_IMILBitmapEffectConnector_head():
    class IMILBitmapEffectConnector(win32more.UI.Wpf.IMILBitmapEffectConnectorInfo_head):
        Guid = Guid('f59567b3-76c1-4d47-ba-1e-79-f9-55-e3-50-ef')
    return IMILBitmapEffectConnector
def _define_IMILBitmapEffectConnector():
    IMILBitmapEffectConnector = win32more.UI.Wpf.IMILBitmapEffectConnector_head
    IMILBitmapEffectConnector.IsConnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'IsConnected', ((1, 'pfConnected'),)))
    IMILBitmapEffectConnector.GetBitmapEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.IMILBitmapEffect_head))(8, 'GetBitmapEffect', ((1, 'ppEffect'),)))
    win32more.UI.Wpf.IMILBitmapEffectConnectorInfo
    return IMILBitmapEffectConnector
def _define_IMILBitmapEffectConnectorInfo_head():
    class IMILBitmapEffectConnectorInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('f66d2e4b-b46b-42fc-85-9e-3d-a0-ec-db-3c-43')
    return IMILBitmapEffectConnectorInfo
def _define_IMILBitmapEffectConnectorInfo():
    IMILBitmapEffectConnectorInfo = win32more.UI.Wpf.IMILBitmapEffectConnectorInfo_head
    IMILBitmapEffectConnectorInfo.GetIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetIndex', ((1, 'puiIndex'),)))
    IMILBitmapEffectConnectorInfo.GetOptimalFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(4, 'GetOptimalFormat', ((1, 'pFormat'),)))
    IMILBitmapEffectConnectorInfo.GetNumberFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(5, 'GetNumberFormats', ((1, 'pulNumberFormats'),)))
    IMILBitmapEffectConnectorInfo.GetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid))(6, 'GetFormat', ((1, 'ulIndex'),(1, 'pFormat'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectConnectorInfo
def _define_IMILBitmapEffectEvents_head():
    class IMILBitmapEffectEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('2e880dd8-f8ce-457b-81-99-d6-0b-b3-d7-ef-98')
    return IMILBitmapEffectEvents
def _define_IMILBitmapEffectEvents():
    IMILBitmapEffectEvents = win32more.UI.Wpf.IMILBitmapEffectEvents_head
    IMILBitmapEffectEvents.PropertyChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Wpf.IMILBitmapEffect_head,win32more.Foundation.BSTR)(3, 'PropertyChange', ((1, 'pEffect'),(1, 'bstrPropertyName'),)))
    IMILBitmapEffectEvents.DirtyRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Wpf.IMILBitmapEffect_head,POINTER(win32more.UI.Wpf.MilRectD_head))(4, 'DirtyRegion', ((1, 'pEffect'),(1, 'pRect'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectEvents
def _define_IMILBitmapEffectFactory_head():
    class IMILBitmapEffectFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('33a9df34-a403-4ec7-b0-7e-bc-06-82-37-08-45')
    return IMILBitmapEffectFactory
def _define_IMILBitmapEffectFactory():
    IMILBitmapEffectFactory = win32more.UI.Wpf.IMILBitmapEffectFactory_head
    IMILBitmapEffectFactory.CreateEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.Wpf.IMILBitmapEffect_head))(3, 'CreateEffect', ((1, 'pguidEffect'),(1, 'ppEffect'),)))
    IMILBitmapEffectFactory.CreateContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.IMILBitmapEffectRenderContext_head))(4, 'CreateContext', ((1, 'ppContext'),)))
    IMILBitmapEffectFactory.CreateEffectOuter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.IMILBitmapEffect_head))(5, 'CreateEffectOuter', ((1, 'ppEffect'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectFactory
def _define_IMILBitmapEffectGroup_head():
    class IMILBitmapEffectGroup(win32more.System.Com.IUnknown_head):
        Guid = Guid('2f952360-698a-4ac6-81-a1-bc-fd-f0-8e-b8-e8')
    return IMILBitmapEffectGroup
def _define_IMILBitmapEffectGroup():
    IMILBitmapEffectGroup = win32more.UI.Wpf.IMILBitmapEffectGroup_head
    IMILBitmapEffectGroup.GetInteriorInputConnector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Wpf.IMILBitmapEffectOutputConnector_head))(3, 'GetInteriorInputConnector', ((1, 'uiIndex'),(1, 'ppConnector'),)))
    IMILBitmapEffectGroup.GetInteriorOutputConnector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Wpf.IMILBitmapEffectInputConnector_head))(4, 'GetInteriorOutputConnector', ((1, 'uiIndex'),(1, 'ppConnector'),)))
    IMILBitmapEffectGroup.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Wpf.IMILBitmapEffect_head)(5, 'Add', ((1, 'pEffect'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectGroup
def _define_IMILBitmapEffectGroupImpl_head():
    class IMILBitmapEffectGroupImpl(win32more.System.Com.IUnknown_head):
        Guid = Guid('78fed518-1cfc-4807-8b-85-6b-6e-51-39-8f-62')
    return IMILBitmapEffectGroupImpl
def _define_IMILBitmapEffectGroupImpl():
    IMILBitmapEffectGroupImpl = win32more.UI.Wpf.IMILBitmapEffectGroupImpl_head
    IMILBitmapEffectGroupImpl.Preprocess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Wpf.IMILBitmapEffectRenderContext_head)(3, 'Preprocess', ((1, 'pContext'),)))
    IMILBitmapEffectGroupImpl.GetNumberChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetNumberChildren', ((1, 'puiNumberChildren'),)))
    IMILBitmapEffectGroupImpl.GetChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.IMILBitmapEffects_head))(5, 'GetChildren', ((1, 'pChildren'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectGroupImpl
def _define_IMILBitmapEffectImpl_head():
    class IMILBitmapEffectImpl(win32more.System.Com.IUnknown_head):
        Guid = Guid('cc2468f2-9936-47be-b4-af-06-b5-df-5d-bc-bb')
    return IMILBitmapEffectImpl
def _define_IMILBitmapEffectImpl():
    IMILBitmapEffectImpl = win32more.UI.Wpf.IMILBitmapEffectImpl_head
    IMILBitmapEffectImpl.IsInPlaceModificationAllowed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Wpf.IMILBitmapEffectOutputConnector_head,POINTER(win32more.Foundation.VARIANT_BOOL))(3, 'IsInPlaceModificationAllowed', ((1, 'pOutputConnector'),(1, 'pfModifyInPlace'),)))
    IMILBitmapEffectImpl.SetParentEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Wpf.IMILBitmapEffectGroup_head)(4, 'SetParentEffect', ((1, 'pParentEffect'),)))
    IMILBitmapEffectImpl.GetInputSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head))(5, 'GetInputSource', ((1, 'uiIndex'),(1, 'ppBitmapSource'),)))
    IMILBitmapEffectImpl.GetInputSourceBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Wpf.MilRectD_head))(6, 'GetInputSourceBounds', ((1, 'uiIndex'),(1, 'pRect'),)))
    IMILBitmapEffectImpl.GetInputBitmapSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.Wpf.IMILBitmapEffectRenderContext_head,POINTER(win32more.Foundation.VARIANT_BOOL),POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head))(7, 'GetInputBitmapSource', ((1, 'uiIndex'),(1, 'pRenderContext'),(1, 'pfModifyInPlace'),(1, 'ppBitmapSource'),)))
    IMILBitmapEffectImpl.GetOutputBitmapSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.Wpf.IMILBitmapEffectRenderContext_head,POINTER(win32more.Foundation.VARIANT_BOOL),POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head))(8, 'GetOutputBitmapSource', ((1, 'uiIndex'),(1, 'pRenderContext'),(1, 'pfModifyInPlace'),(1, 'ppBitmapSource'),)))
    IMILBitmapEffectImpl.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(9, 'Initialize', ((1, 'pInner'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectImpl
def _define_IMILBitmapEffectInputConnector_head():
    class IMILBitmapEffectInputConnector(win32more.UI.Wpf.IMILBitmapEffectConnector_head):
        Guid = Guid('a9b4ecaa-7a3c-45e7-85-73-f4-b8-1b-60-dd-6c')
    return IMILBitmapEffectInputConnector
def _define_IMILBitmapEffectInputConnector():
    IMILBitmapEffectInputConnector = win32more.UI.Wpf.IMILBitmapEffectInputConnector_head
    IMILBitmapEffectInputConnector.ConnectTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Wpf.IMILBitmapEffectOutputConnector_head)(9, 'ConnectTo', ((1, 'pConnector'),)))
    IMILBitmapEffectInputConnector.GetConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.IMILBitmapEffectOutputConnector_head))(10, 'GetConnection', ((1, 'ppConnector'),)))
    win32more.UI.Wpf.IMILBitmapEffectConnector
    return IMILBitmapEffectInputConnector
def _define_IMILBitmapEffectInteriorInputConnector_head():
    class IMILBitmapEffectInteriorInputConnector(win32more.System.Com.IUnknown_head):
        Guid = Guid('20287e9e-86a2-4e15-95-3d-eb-14-38-a5-b8-42')
    return IMILBitmapEffectInteriorInputConnector
def _define_IMILBitmapEffectInteriorInputConnector():
    IMILBitmapEffectInteriorInputConnector = win32more.UI.Wpf.IMILBitmapEffectInteriorInputConnector_head
    IMILBitmapEffectInteriorInputConnector.GetInputConnector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.IMILBitmapEffectInputConnector_head))(3, 'GetInputConnector', ((1, 'pInputConnector'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectInteriorInputConnector
def _define_IMILBitmapEffectInteriorOutputConnector_head():
    class IMILBitmapEffectInteriorOutputConnector(win32more.System.Com.IUnknown_head):
        Guid = Guid('00bbb6dc-acc9-4bfc-b3-44-8b-ee-38-3d-fe-fa')
    return IMILBitmapEffectInteriorOutputConnector
def _define_IMILBitmapEffectInteriorOutputConnector():
    IMILBitmapEffectInteriorOutputConnector = win32more.UI.Wpf.IMILBitmapEffectInteriorOutputConnector_head
    IMILBitmapEffectInteriorOutputConnector.GetOutputConnector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.IMILBitmapEffectOutputConnector_head))(3, 'GetOutputConnector', ((1, 'pOutputConnector'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectInteriorOutputConnector
def _define_IMILBitmapEffectOutputConnector_head():
    class IMILBitmapEffectOutputConnector(win32more.UI.Wpf.IMILBitmapEffectConnector_head):
        Guid = Guid('92957aad-841b-4866-82-ec-87-52-46-8b-07-fd')
    return IMILBitmapEffectOutputConnector
def _define_IMILBitmapEffectOutputConnector():
    IMILBitmapEffectOutputConnector = win32more.UI.Wpf.IMILBitmapEffectOutputConnector_head
    IMILBitmapEffectOutputConnector.GetNumberConnections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'GetNumberConnections', ((1, 'puiNumberConnections'),)))
    IMILBitmapEffectOutputConnector.GetConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Wpf.IMILBitmapEffectInputConnector_head))(10, 'GetConnection', ((1, 'uiIndex'),(1, 'ppConnection'),)))
    win32more.UI.Wpf.IMILBitmapEffectConnector
    return IMILBitmapEffectOutputConnector
def _define_IMILBitmapEffectOutputConnectorImpl_head():
    class IMILBitmapEffectOutputConnectorImpl(win32more.System.Com.IUnknown_head):
        Guid = Guid('21fae777-8b39-4bfa-9f-2d-f3-94-1e-d3-69-13')
    return IMILBitmapEffectOutputConnectorImpl
def _define_IMILBitmapEffectOutputConnectorImpl():
    IMILBitmapEffectOutputConnectorImpl = win32more.UI.Wpf.IMILBitmapEffectOutputConnectorImpl_head
    IMILBitmapEffectOutputConnectorImpl.AddBackLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Wpf.IMILBitmapEffectInputConnector_head)(3, 'AddBackLink', ((1, 'pConnection'),)))
    IMILBitmapEffectOutputConnectorImpl.RemoveBackLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Wpf.IMILBitmapEffectInputConnector_head)(4, 'RemoveBackLink', ((1, 'pConnection'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectOutputConnectorImpl
def _define_IMILBitmapEffectPrimitive_head():
    class IMILBitmapEffectPrimitive(win32more.System.Com.IUnknown_head):
        Guid = Guid('67e31025-3091-4dfc-98-d6-dd-49-45-51-46-1d')
    return IMILBitmapEffectPrimitive
def _define_IMILBitmapEffectPrimitive():
    IMILBitmapEffectPrimitive = win32more.UI.Wpf.IMILBitmapEffectPrimitive_head
    IMILBitmapEffectPrimitive.GetOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.Wpf.IMILBitmapEffectRenderContext_head,POINTER(win32more.Foundation.VARIANT_BOOL),POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head))(3, 'GetOutput', ((1, 'uiIndex'),(1, 'pContext'),(1, 'pfModifyInPlace'),(1, 'ppBitmapSource'),)))
    IMILBitmapEffectPrimitive.TransformPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Wpf.MilPoint2D_head),win32more.Foundation.VARIANT_BOOL,win32more.UI.Wpf.IMILBitmapEffectRenderContext_head,POINTER(win32more.Foundation.VARIANT_BOOL))(4, 'TransformPoint', ((1, 'uiIndex'),(1, 'p'),(1, 'fForwardTransform'),(1, 'pContext'),(1, 'pfPointTransformed'),)))
    IMILBitmapEffectPrimitive.TransformRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Wpf.MilRectD_head),win32more.Foundation.VARIANT_BOOL,win32more.UI.Wpf.IMILBitmapEffectRenderContext_head)(5, 'TransformRect', ((1, 'uiIndex'),(1, 'p'),(1, 'fForwardTransform'),(1, 'pContext'),)))
    IMILBitmapEffectPrimitive.HasAffineTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.VARIANT_BOOL))(6, 'HasAffineTransform', ((1, 'uiIndex'),(1, 'pfAffine'),)))
    IMILBitmapEffectPrimitive.HasInverseTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'HasInverseTransform', ((1, 'uiIndex'),(1, 'pfHasInverse'),)))
    IMILBitmapEffectPrimitive.GetAffineMatrix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Dwm.MilMatrix3x2D_head))(8, 'GetAffineMatrix', ((1, 'uiIndex'),(1, 'pMatrix'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectPrimitive
def _define_IMILBitmapEffectPrimitiveImpl_head():
    class IMILBitmapEffectPrimitiveImpl(win32more.System.Com.IUnknown_head):
        Guid = Guid('ce41e00b-efa6-44e7-b0-07-dd-04-2e-3a-e1-26')
    return IMILBitmapEffectPrimitiveImpl
def _define_IMILBitmapEffectPrimitiveImpl():
    IMILBitmapEffectPrimitiveImpl = win32more.UI.Wpf.IMILBitmapEffectPrimitiveImpl_head
    IMILBitmapEffectPrimitiveImpl.IsDirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.VARIANT_BOOL))(3, 'IsDirty', ((1, 'uiOutputIndex'),(1, 'pfDirty'),)))
    IMILBitmapEffectPrimitiveImpl.IsVolatile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.VARIANT_BOOL))(4, 'IsVolatile', ((1, 'uiOutputIndex'),(1, 'pfVolatile'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectPrimitiveImpl
def _define_IMILBitmapEffectRenderContext_head():
    class IMILBitmapEffectRenderContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('12a2ec7e-2d33-44b2-b3-34-1a-bb-78-46-e3-90')
    return IMILBitmapEffectRenderContext
def _define_IMILBitmapEffectRenderContext():
    IMILBitmapEffectRenderContext = win32more.UI.Wpf.IMILBitmapEffectRenderContext_head
    IMILBitmapEffectRenderContext.SetOutputPixelFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'SetOutputPixelFormat', ((1, 'format'),)))
    IMILBitmapEffectRenderContext.GetOutputPixelFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(4, 'GetOutputPixelFormat', ((1, 'pFormat'),)))
    IMILBitmapEffectRenderContext.SetUseSoftwareRenderer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(5, 'SetUseSoftwareRenderer', ((1, 'fSoftware'),)))
    IMILBitmapEffectRenderContext.SetInitialTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.MILMatrixF_head))(6, 'SetInitialTransform', ((1, 'pMatrix'),)))
    IMILBitmapEffectRenderContext.GetFinalTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.MILMatrixF_head))(7, 'GetFinalTransform', ((1, 'pMatrix'),)))
    IMILBitmapEffectRenderContext.SetOutputDPI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double)(8, 'SetOutputDPI', ((1, 'dblDpiX'),(1, 'dblDpiY'),)))
    IMILBitmapEffectRenderContext.GetOutputDPI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),POINTER(Double))(9, 'GetOutputDPI', ((1, 'pdblDpiX'),(1, 'pdblDpiY'),)))
    IMILBitmapEffectRenderContext.SetRegionOfInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.MilRectD_head))(10, 'SetRegionOfInterest', ((1, 'pRect'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectRenderContext
def _define_IMILBitmapEffectRenderContextImpl_head():
    class IMILBitmapEffectRenderContextImpl(win32more.System.Com.IUnknown_head):
        Guid = Guid('4d25accb-797d-4fd2-b1-28-df-fe-ff-84-fc-c3')
    return IMILBitmapEffectRenderContextImpl
def _define_IMILBitmapEffectRenderContextImpl():
    IMILBitmapEffectRenderContextImpl = win32more.UI.Wpf.IMILBitmapEffectRenderContextImpl_head
    IMILBitmapEffectRenderContextImpl.GetUseSoftwareRenderer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(3, 'GetUseSoftwareRenderer', ((1, 'pfSoftware'),)))
    IMILBitmapEffectRenderContextImpl.GetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.MILMatrixF_head))(4, 'GetTransform', ((1, 'pMatrix'),)))
    IMILBitmapEffectRenderContextImpl.UpdateTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.MILMatrixF_head))(5, 'UpdateTransform', ((1, 'pMatrix'),)))
    IMILBitmapEffectRenderContextImpl.GetOutputBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.MilRectD_head))(6, 'GetOutputBounds', ((1, 'pRect'),)))
    IMILBitmapEffectRenderContextImpl.UpdateOutputBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.MilRectD_head))(7, 'UpdateOutputBounds', ((1, 'pRect'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffectRenderContextImpl
def _define_IMILBitmapEffects_head():
    class IMILBitmapEffects(win32more.System.Com.IUnknown_head):
        Guid = Guid('51ac3dce-67c5-448b-91-80-ad-3e-ab-dd-d5-dd')
    return IMILBitmapEffects
def _define_IMILBitmapEffects():
    IMILBitmapEffects = win32more.UI.Wpf.IMILBitmapEffects_head
    IMILBitmapEffects._NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(3, '_NewEnum', ((1, 'ppiuReturn'),)))
    IMILBitmapEffects.get_Parent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Wpf.IMILBitmapEffectGroup_head))(4, 'get_Parent', ((1, 'ppEffect'),)))
    IMILBitmapEffects.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Wpf.IMILBitmapEffect_head))(5, 'Item', ((1, 'uindex'),(1, 'ppEffect'),)))
    IMILBitmapEffects.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(6, 'get_Count', ((1, 'puiCount'),)))
    win32more.System.Com.IUnknown
    return IMILBitmapEffects
def _define_MILMatrixF_head():
    class MILMatrixF(Structure):
        pass
    return MILMatrixF
def _define_MILMatrixF():
    MILMatrixF = win32more.UI.Wpf.MILMatrixF_head
    MILMatrixF._fields_ = [
        ('_11', Double),
        ('_12', Double),
        ('_13', Double),
        ('_14', Double),
        ('_21', Double),
        ('_22', Double),
        ('_23', Double),
        ('_24', Double),
        ('_31', Double),
        ('_32', Double),
        ('_33', Double),
        ('_34', Double),
        ('_41', Double),
        ('_42', Double),
        ('_43', Double),
        ('_44', Double),
    ]
    return MILMatrixF
def _define_MilPoint2D_head():
    class MilPoint2D(Structure):
        pass
    return MilPoint2D
def _define_MilPoint2D():
    MilPoint2D = win32more.UI.Wpf.MilPoint2D_head
    MilPoint2D._fields_ = [
        ('X', Double),
        ('Y', Double),
    ]
    return MilPoint2D
def _define_MilRectD_head():
    class MilRectD(Structure):
        pass
    return MilRectD
def _define_MilRectD():
    MilRectD = win32more.UI.Wpf.MilRectD_head
    MilRectD._fields_ = [
        ('left', Double),
        ('top', Double),
        ('right', Double),
        ('bottom', Double),
    ]
    return MilRectD
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
