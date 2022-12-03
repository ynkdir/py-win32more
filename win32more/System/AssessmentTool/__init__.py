from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
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
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
CAccessiblityWinSAT = Guid('6e18f9c6-a3eb-495a-89-b7-95-64-82-e1-9f-7a')
CInitiateWinSAT = Guid('489331dc-f5e0-4528-9f-da-45-33-1b-f4-a5-71')
CProvideWinSATVisuals = Guid('9f377d7e-e551-44f8-9f-94-9d-b3-92-b0-3b-7b')
CQueryAllWinSAT = Guid('05df8d13-c355-47f4-a1-1e-85-1b-33-8c-ef-b8')
CQueryOEMWinSATCustomization = Guid('c47a41b7-b729-424f-9a-f9-5c-b3-93-4f-2d-fa')
CQueryWinSAT = Guid('f3bdfad3-f276-49e9-9b-17-c4-74-f4-8f-07-64')
def _define_IAccessibleWinSAT_head():
    class IAccessibleWinSAT(win32more.UI.Accessibility.IAccessible_head):
        Guid = Guid('30e6018a-94a8-4ff8-a6-9a-71-b6-74-13-f0-7b')
    return IAccessibleWinSAT
def _define_IAccessibleWinSAT():
    IAccessibleWinSAT = win32more.System.AssessmentTool.IAccessibleWinSAT_head
    IAccessibleWinSAT.SetAccessiblityData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(28, 'SetAccessiblityData', ((1, 'wsName'),(1, 'wsValue'),(1, 'wsDesc'),)))
    win32more.UI.Accessibility.IAccessible
    return IAccessibleWinSAT
def _define_IInitiateWinSATAssessment_head():
    class IInitiateWinSATAssessment(win32more.System.Com.IUnknown_head):
        Guid = Guid('d983fc50-f5bf-49d5-b5-ed-cc-cb-18-aa-7f-c1')
    return IInitiateWinSATAssessment
def _define_IInitiateWinSATAssessment():
    IInitiateWinSATAssessment = win32more.System.AssessmentTool.IInitiateWinSATAssessment_head
    IInitiateWinSATAssessment.InitiateAssessment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.AssessmentTool.IWinSATInitiateEvents_head,win32more.Foundation.HWND)(3, 'InitiateAssessment', ((1, 'cmdLine'),(1, 'pCallbacks'),(1, 'callerHwnd'),)))
    IInitiateWinSATAssessment.InitiateFormalAssessment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AssessmentTool.IWinSATInitiateEvents_head,win32more.Foundation.HWND)(4, 'InitiateFormalAssessment', ((1, 'pCallbacks'),(1, 'callerHwnd'),)))
    IInitiateWinSATAssessment.CancelAssessment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'CancelAssessment', ()))
    win32more.System.Com.IUnknown
    return IInitiateWinSATAssessment
def _define_IProvideWinSATAssessmentInfo_head():
    class IProvideWinSATAssessmentInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('0cd1c380-52d3-4678-ac-6f-e9-29-e4-80-be-9e')
    return IProvideWinSATAssessmentInfo
def _define_IProvideWinSATAssessmentInfo():
    IProvideWinSATAssessmentInfo = win32more.System.AssessmentTool.IProvideWinSATAssessmentInfo_head
    IProvideWinSATAssessmentInfo.get_Score = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(7, 'get_Score', ((1, 'score'),)))
    IProvideWinSATAssessmentInfo.get_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Title', ((1, 'title'),)))
    IProvideWinSATAssessmentInfo.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Description', ((1, 'description'),)))
    win32more.System.Com.IDispatch
    return IProvideWinSATAssessmentInfo
def _define_IProvideWinSATResultsInfo_head():
    class IProvideWinSATResultsInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('f8334d5d-568e-4075-87-5f-9d-f3-41-50-66-40')
    return IProvideWinSATResultsInfo
def _define_IProvideWinSATResultsInfo():
    IProvideWinSATResultsInfo = win32more.System.AssessmentTool.IProvideWinSATResultsInfo_head
    IProvideWinSATResultsInfo.GetAssessmentInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AssessmentTool.WINSAT_ASSESSMENT_TYPE,POINTER(win32more.System.AssessmentTool.IProvideWinSATAssessmentInfo_head))(7, 'GetAssessmentInfo', ((1, 'assessment'),(1, 'ppinfo'),)))
    IProvideWinSATResultsInfo.get_AssessmentState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AssessmentTool.WINSAT_ASSESSMENT_STATE))(8, 'get_AssessmentState', ((1, 'state'),)))
    IProvideWinSATResultsInfo.get_AssessmentDateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(9, 'get_AssessmentDateTime', ((1, 'fileTime'),)))
    IProvideWinSATResultsInfo.get_SystemRating = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(10, 'get_SystemRating', ((1, 'level'),)))
    IProvideWinSATResultsInfo.get_RatingStateDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_RatingStateDesc', ((1, 'description'),)))
    win32more.System.Com.IDispatch
    return IProvideWinSATResultsInfo
def _define_IProvideWinSATVisuals_head():
    class IProvideWinSATVisuals(win32more.System.Com.IUnknown_head):
        Guid = Guid('a9f4ade0-871a-42a3-b8-13-30-78-d2-51-62-c9')
    return IProvideWinSATVisuals
def _define_IProvideWinSATVisuals():
    IProvideWinSATVisuals = win32more.System.AssessmentTool.IProvideWinSATVisuals_head
    IProvideWinSATVisuals.get_Bitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.AssessmentTool.WINSAT_BITMAP_SIZE,win32more.System.AssessmentTool.WINSAT_ASSESSMENT_STATE,Single,POINTER(win32more.Graphics.Gdi.HBITMAP))(3, 'get_Bitmap', ((1, 'bitmapSize'),(1, 'state'),(1, 'rating'),(1, 'pBitmap'),)))
    win32more.System.Com.IUnknown
    return IProvideWinSATVisuals
def _define_IQueryAllWinSATAssessments_head():
    class IQueryAllWinSATAssessments(win32more.System.Com.IDispatch_head):
        Guid = Guid('0b89ed1d-6398-4fea-87-fc-56-7d-8d-19-17-6f')
    return IQueryAllWinSATAssessments
def _define_IQueryAllWinSATAssessments():
    IQueryAllWinSATAssessments = win32more.System.AssessmentTool.IQueryAllWinSATAssessments_head
    IQueryAllWinSATAssessments.get_AllXML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Data.Xml.MsXml.IXMLDOMNodeList_head))(7, 'get_AllXML', ((1, 'xPath'),(1, 'namespaces'),(1, 'ppDomNodeList'),)))
    win32more.System.Com.IDispatch
    return IQueryAllWinSATAssessments
def _define_IQueryOEMWinSATCustomization_head():
    class IQueryOEMWinSATCustomization(win32more.System.Com.IUnknown_head):
        Guid = Guid('bc9a6a9f-ad4e-420e-99-53-b3-46-71-e9-df-22')
    return IQueryOEMWinSATCustomization
def _define_IQueryOEMWinSATCustomization():
    IQueryOEMWinSATCustomization = win32more.System.AssessmentTool.IQueryOEMWinSATCustomization_head
    IQueryOEMWinSATCustomization.GetOEMPrePopulationInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AssessmentTool.WINSAT_OEM_CUSTOMIZATION_STATE))(3, 'GetOEMPrePopulationInfo', ((1, 'state'),)))
    win32more.System.Com.IUnknown
    return IQueryOEMWinSATCustomization
def _define_IQueryRecentWinSATAssessment_head():
    class IQueryRecentWinSATAssessment(win32more.System.Com.IDispatch_head):
        Guid = Guid('f8ad5d1f-3b47-4bdc-93-75-7c-6b-1d-a4-ec-a7')
    return IQueryRecentWinSATAssessment
def _define_IQueryRecentWinSATAssessment():
    IQueryRecentWinSATAssessment = win32more.System.AssessmentTool.IQueryRecentWinSATAssessment_head
    IQueryRecentWinSATAssessment.get_XML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Data.Xml.MsXml.IXMLDOMNodeList_head))(7, 'get_XML', ((1, 'xPath'),(1, 'namespaces'),(1, 'ppDomNodeList'),)))
    IQueryRecentWinSATAssessment.get_Info = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.AssessmentTool.IProvideWinSATResultsInfo_head))(8, 'get_Info', ((1, 'ppWinSATAssessmentInfo'),)))
    win32more.System.Com.IDispatch
    return IQueryRecentWinSATAssessment
def _define_IWinSATInitiateEvents_head():
    class IWinSATInitiateEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('262a1918-ba0d-41d5-92-c2-fa-b4-63-3e-e7-4f')
    return IWinSATInitiateEvents
def _define_IWinSATInitiateEvents():
    IWinSATInitiateEvents = win32more.System.AssessmentTool.IWinSATInitiateEvents_head
    IWinSATInitiateEvents.WinSATComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(3, 'WinSATComplete', ((1, 'hresult'),(1, 'strDescription'),)))
    IWinSATInitiateEvents.WinSATUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR)(4, 'WinSATUpdate', ((1, 'uCurrentTick'),(1, 'uTickTotal'),(1, 'strCurrentState'),)))
    win32more.System.Com.IUnknown
    return IWinSATInitiateEvents
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
WINSAT_OEM_CUSTOMIZATION_STATE = Int32
WINSAT_OEM_DATA_VALID = 0
WINSAT_OEM_DATA_NON_SYS_CONFIG_MATCH = 1
WINSAT_OEM_DATA_INVALID = 2
WINSAT_OEM_NO_DATA_SUPPLIED = 3
__all__ = [
    "CAccessiblityWinSAT",
    "CInitiateWinSAT",
    "CProvideWinSATVisuals",
    "CQueryAllWinSAT",
    "CQueryOEMWinSATCustomization",
    "CQueryWinSAT",
    "IAccessibleWinSAT",
    "IInitiateWinSATAssessment",
    "IProvideWinSATAssessmentInfo",
    "IProvideWinSATResultsInfo",
    "IProvideWinSATVisuals",
    "IQueryAllWinSATAssessments",
    "IQueryOEMWinSATCustomization",
    "IQueryRecentWinSATAssessment",
    "IWinSATInitiateEvents",
    "WINSAT_ASSESSMENT_CPU",
    "WINSAT_ASSESSMENT_D3D",
    "WINSAT_ASSESSMENT_DISK",
    "WINSAT_ASSESSMENT_GRAPHICS",
    "WINSAT_ASSESSMENT_MEMORY",
    "WINSAT_ASSESSMENT_STATE",
    "WINSAT_ASSESSMENT_STATE_INCOHERENT_WITH_HARDWARE",
    "WINSAT_ASSESSMENT_STATE_INVALID",
    "WINSAT_ASSESSMENT_STATE_MAX",
    "WINSAT_ASSESSMENT_STATE_MIN",
    "WINSAT_ASSESSMENT_STATE_NOT_AVAILABLE",
    "WINSAT_ASSESSMENT_STATE_UNKNOWN",
    "WINSAT_ASSESSMENT_STATE_VALID",
    "WINSAT_ASSESSMENT_TYPE",
    "WINSAT_BITMAP_SIZE",
    "WINSAT_BITMAP_SIZE_NORMAL",
    "WINSAT_BITMAP_SIZE_SMALL",
    "WINSAT_OEM_CUSTOMIZATION_STATE",
    "WINSAT_OEM_DATA_INVALID",
    "WINSAT_OEM_DATA_NON_SYS_CONFIG_MATCH",
    "WINSAT_OEM_DATA_VALID",
    "WINSAT_OEM_NO_DATA_SUPPLIED",
]
