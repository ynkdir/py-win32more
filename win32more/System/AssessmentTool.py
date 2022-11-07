from win32more import *
import win32more.Data.Xml.MsXml
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.AssessmentTool
import win32more.System.Com
import win32more.UI.Accessibility

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
CInitiateWinSAT = Guid('489331dc-f5e0-4528-9fda-45331bf4a571')
CQueryWinSAT = Guid('f3bdfad3-f276-49e9-9b17-c474f48f0764')
CQueryAllWinSAT = Guid('05df8d13-c355-47f4-a11e-851b338cefb8')
CProvideWinSATVisuals = Guid('9f377d7e-e551-44f8-9f94-9db392b03b7b')
CAccessiblityWinSAT = Guid('6e18f9c6-a3eb-495a-89b7-956482e19f7a')
CQueryOEMWinSATCustomization = Guid('c47a41b7-b729-424f-9af9-5cb3934f2dfa')
WINSAT_OEM_DATA_TYPE = Int32
WINSAT_OEM_DATA_VALID = 0
WINSAT_OEM_DATA_NON_SYS_CONFIG_MATCH = 1
WINSAT_OEM_DATA_INVALID = 2
WINSAT_OEM_NO_DATA_SUPPLIED = 3
WINSAT_ASSESSMENT_STATE = Int32
WINSAT_ASSESSMENT_STATE_MIN = 0
WINSAT_ASSESSMENT_STATE_UNKNOWN = 0
WINSAT_ASSESSMENT_STATE_VALID = 1
WINSAT_ASSESSMENT_STATE_INCOHERENT_WITH_HARDWARE = 2
WINSAT_ASSESSMENT_STATE_NOT_AVAILABLE = 3
WINSAT_ASSESSMENT_STATE_INVALID = 4
WINSAT_ASSESSMENT_STATE_MAX = 4
WINSAT_ASSESSMENT_TYPE = Int32
WINSAT_ASSESSMENT_MEMORY = 0
WINSAT_ASSESSMENT_CPU = 1
WINSAT_ASSESSMENT_DISK = 2
WINSAT_ASSESSMENT_D3D = 3
WINSAT_ASSESSMENT_GRAPHICS = 4
WINSAT_BITMAP_SIZE = Int32
WINSAT_BITMAP_SIZE_SMALL = 0
WINSAT_BITMAP_SIZE_NORMAL = 1
def _define_IProvideWinSATAssessmentInfo_head():
    class IProvideWinSATAssessmentInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('0cd1c380-52d3-4678-ac6f-e929e480be9e')
    return IProvideWinSATAssessmentInfo
def _define_IProvideWinSATAssessmentInfo():
    IProvideWinSATAssessmentInfo = win32more.System.AssessmentTool.IProvideWinSATAssessmentInfo_head
    IProvideWinSATAssessmentInfo.get_Score = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(7, 'get_Score', ((1, 'score'),)))
    IProvideWinSATAssessmentInfo.get_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Title', ((1, 'title'),)))
    IProvideWinSATAssessmentInfo.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Description', ((1, 'description'),)))
    win32more.System.Com.IDispatch
    return IProvideWinSATAssessmentInfo
def _define_IProvideWinSATResultsInfo_head():
    class IProvideWinSATResultsInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('f8334d5d-568e-4075-875f-9df341506640')
    return IProvideWinSATResultsInfo
def _define_IProvideWinSATResultsInfo():
    IProvideWinSATResultsInfo = win32more.System.AssessmentTool.IProvideWinSATResultsInfo_head
    IProvideWinSATResultsInfo.GetAssessmentInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AssessmentTool.WINSAT_ASSESSMENT_TYPE,POINTER(win32more.System.AssessmentTool.IProvideWinSATAssessmentInfo_head), use_last_error=False)(7, 'GetAssessmentInfo', ((1, 'assessment'),(1, 'ppinfo'),)))
    IProvideWinSATResultsInfo.get_AssessmentState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AssessmentTool.WINSAT_ASSESSMENT_STATE), use_last_error=False)(8, 'get_AssessmentState', ((1, 'state'),)))
    IProvideWinSATResultsInfo.get_AssessmentDateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'get_AssessmentDateTime', ((1, 'fileTime'),)))
    IProvideWinSATResultsInfo.get_SystemRating = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(10, 'get_SystemRating', ((1, 'level'),)))
    IProvideWinSATResultsInfo.get_RatingStateDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_RatingStateDesc', ((1, 'description'),)))
    win32more.System.Com.IDispatch
    return IProvideWinSATResultsInfo
def _define_IQueryRecentWinSATAssessment_head():
    class IQueryRecentWinSATAssessment(win32more.System.Com.IDispatch_head):
        Guid = Guid('f8ad5d1f-3b47-4bdc-9375-7c6b1da4eca7')
    return IQueryRecentWinSATAssessment
def _define_IQueryRecentWinSATAssessment():
    IQueryRecentWinSATAssessment = win32more.System.AssessmentTool.IQueryRecentWinSATAssessment_head
    IQueryRecentWinSATAssessment.get_XML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Data.Xml.MsXml.IXMLDOMNodeList_head), use_last_error=False)(7, 'get_XML', ((1, 'xPath'),(1, 'namespaces'),(1, 'ppDomNodeList'),)))
    IQueryRecentWinSATAssessment.get_Info = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AssessmentTool.IProvideWinSATResultsInfo_head), use_last_error=False)(8, 'get_Info', ((1, 'ppWinSATAssessmentInfo'),)))
    win32more.System.Com.IDispatch
    return IQueryRecentWinSATAssessment
def _define_IProvideWinSATVisuals_head():
    class IProvideWinSATVisuals(win32more.System.Com.IUnknown_head):
        Guid = Guid('a9f4ade0-871a-42a3-b813-3078d25162c9')
    return IProvideWinSATVisuals
def _define_IProvideWinSATVisuals():
    IProvideWinSATVisuals = win32more.System.AssessmentTool.IProvideWinSATVisuals_head
    IProvideWinSATVisuals.get_Bitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AssessmentTool.WINSAT_BITMAP_SIZE,win32more.System.AssessmentTool.WINSAT_ASSESSMENT_STATE,Single,POINTER(win32more.Graphics.Gdi.HBITMAP), use_last_error=False)(3, 'get_Bitmap', ((1, 'bitmapSize'),(1, 'state'),(1, 'rating'),(1, 'pBitmap'),)))
    win32more.System.Com.IUnknown
    return IProvideWinSATVisuals
def _define_IQueryAllWinSATAssessments_head():
    class IQueryAllWinSATAssessments(win32more.System.Com.IDispatch_head):
        Guid = Guid('0b89ed1d-6398-4fea-87fc-567d8d19176f')
    return IQueryAllWinSATAssessments
def _define_IQueryAllWinSATAssessments():
    IQueryAllWinSATAssessments = win32more.System.AssessmentTool.IQueryAllWinSATAssessments_head
    IQueryAllWinSATAssessments.get_AllXML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Data.Xml.MsXml.IXMLDOMNodeList_head), use_last_error=False)(7, 'get_AllXML', ((1, 'xPath'),(1, 'namespaces'),(1, 'ppDomNodeList'),)))
    win32more.System.Com.IDispatch
    return IQueryAllWinSATAssessments
def _define_IWinSATInitiateEvents_head():
    class IWinSATInitiateEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('262a1918-ba0d-41d5-92c2-fab4633ee74f')
    return IWinSATInitiateEvents
def _define_IWinSATInitiateEvents():
    IWinSATInitiateEvents = win32more.System.AssessmentTool.IWinSATInitiateEvents_head
    IWinSATInitiateEvents.WinSATComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'WinSATComplete', ((1, 'hresult'),(1, 'strDescription'),)))
    IWinSATInitiateEvents.WinSATUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(4, 'WinSATUpdate', ((1, 'uCurrentTick'),(1, 'uTickTotal'),(1, 'strCurrentState'),)))
    win32more.System.Com.IUnknown
    return IWinSATInitiateEvents
def _define_IInitiateWinSATAssessment_head():
    class IInitiateWinSATAssessment(win32more.System.Com.IUnknown_head):
        Guid = Guid('d983fc50-f5bf-49d5-b5ed-cccb18aa7fc1')
    return IInitiateWinSATAssessment
def _define_IInitiateWinSATAssessment():
    IInitiateWinSATAssessment = win32more.System.AssessmentTool.IInitiateWinSATAssessment_head
    IInitiateWinSATAssessment.InitiateAssessment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.AssessmentTool.IWinSATInitiateEvents_head,win32more.Foundation.HWND, use_last_error=False)(3, 'InitiateAssessment', ((1, 'cmdLine'),(1, 'pCallbacks'),(1, 'callerHwnd'),)))
    IInitiateWinSATAssessment.InitiateFormalAssessment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AssessmentTool.IWinSATInitiateEvents_head,win32more.Foundation.HWND, use_last_error=False)(4, 'InitiateFormalAssessment', ((1, 'pCallbacks'),(1, 'callerHwnd'),)))
    IInitiateWinSATAssessment.CancelAssessment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'CancelAssessment', ()))
    win32more.System.Com.IUnknown
    return IInitiateWinSATAssessment
def _define_IAccessibleWinSAT_head():
    class IAccessibleWinSAT(win32more.UI.Accessibility.IAccessible_head):
        Guid = Guid('30e6018a-94a8-4ff8-a69a-71b67413f07b')
    return IAccessibleWinSAT
def _define_IAccessibleWinSAT():
    IAccessibleWinSAT = win32more.System.AssessmentTool.IAccessibleWinSAT_head
    IAccessibleWinSAT.SetAccessiblityData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(28, 'SetAccessiblityData', ((1, 'wsName'),(1, 'wsValue'),(1, 'wsDesc'),)))
    win32more.UI.Accessibility.IAccessible
    return IAccessibleWinSAT
def _define_IQueryOEMWinSATCustomization_head():
    class IQueryOEMWinSATCustomization(win32more.System.Com.IUnknown_head):
        Guid = Guid('bc9a6a9f-ad4e-420e-9953-b34671e9df22')
    return IQueryOEMWinSATCustomization
def _define_IQueryOEMWinSATCustomization():
    IQueryOEMWinSATCustomization = win32more.System.AssessmentTool.IQueryOEMWinSATCustomization_head
    IQueryOEMWinSATCustomization.GetOEMPrePopulationInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AssessmentTool.WINSAT_OEM_DATA_TYPE), use_last_error=False)(3, 'GetOEMPrePopulationInfo', ((1, 'state'),)))
    win32more.System.Com.IUnknown
    return IQueryOEMWinSATCustomization
__all__ = [
    "CInitiateWinSAT",
    "CQueryWinSAT",
    "CQueryAllWinSAT",
    "CProvideWinSATVisuals",
    "CAccessiblityWinSAT",
    "CQueryOEMWinSATCustomization",
    "WINSAT_OEM_DATA_TYPE",
    "WINSAT_OEM_DATA_VALID",
    "WINSAT_OEM_DATA_NON_SYS_CONFIG_MATCH",
    "WINSAT_OEM_DATA_INVALID",
    "WINSAT_OEM_NO_DATA_SUPPLIED",
    "WINSAT_ASSESSMENT_STATE",
    "WINSAT_ASSESSMENT_STATE_MIN",
    "WINSAT_ASSESSMENT_STATE_UNKNOWN",
    "WINSAT_ASSESSMENT_STATE_VALID",
    "WINSAT_ASSESSMENT_STATE_INCOHERENT_WITH_HARDWARE",
    "WINSAT_ASSESSMENT_STATE_NOT_AVAILABLE",
    "WINSAT_ASSESSMENT_STATE_INVALID",
    "WINSAT_ASSESSMENT_STATE_MAX",
    "WINSAT_ASSESSMENT_TYPE",
    "WINSAT_ASSESSMENT_MEMORY",
    "WINSAT_ASSESSMENT_CPU",
    "WINSAT_ASSESSMENT_DISK",
    "WINSAT_ASSESSMENT_D3D",
    "WINSAT_ASSESSMENT_GRAPHICS",
    "WINSAT_BITMAP_SIZE",
    "WINSAT_BITMAP_SIZE_SMALL",
    "WINSAT_BITMAP_SIZE_NORMAL",
    "IProvideWinSATAssessmentInfo",
    "IProvideWinSATResultsInfo",
    "IQueryRecentWinSATAssessment",
    "IProvideWinSATVisuals",
    "IQueryAllWinSATAssessments",
    "IWinSATInitiateEvents",
    "IInitiateWinSATAssessment",
    "IAccessibleWinSAT",
    "IQueryOEMWinSATCustomization",
]
