from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
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
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
CAccessiblityWinSAT = Guid('6e18f9c6-a3eb-495a-89-b7-95-64-82-e1-9f-7a')
CInitiateWinSAT = Guid('489331dc-f5e0-4528-9f-da-45-33-1b-f4-a5-71')
CProvideWinSATVisuals = Guid('9f377d7e-e551-44f8-9f-94-9d-b3-92-b0-3b-7b')
CQueryAllWinSAT = Guid('05df8d13-c355-47f4-a1-1e-85-1b-33-8c-ef-b8')
CQueryOEMWinSATCustomization = Guid('c47a41b7-b729-424f-9a-f9-5c-b3-93-4f-2d-fa')
CQueryWinSAT = Guid('f3bdfad3-f276-49e9-9b-17-c4-74-f4-8f-07-64')
class IAccessibleWinSAT(c_void_p):
    extends: win32more.UI.Accessibility.IAccessible
    Guid = Guid('30e6018a-94a8-4ff8-a6-9a-71-b6-74-13-f0-7b')
    @commethod(28)
    def SetAccessiblityData(wsName: win32more.Foundation.PWSTR, wsValue: win32more.Foundation.PWSTR, wsDesc: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IInitiateWinSATAssessment(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d983fc50-f5bf-49d5-b5-ed-cc-cb-18-aa-7f-c1')
    @commethod(3)
    def InitiateAssessment(cmdLine: win32more.Foundation.PWSTR, pCallbacks: win32more.System.AssessmentTool.IWinSATInitiateEvents_head, callerHwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def InitiateFormalAssessment(pCallbacks: win32more.System.AssessmentTool.IWinSATInitiateEvents_head, callerHwnd: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CancelAssessment() -> win32more.Foundation.HRESULT: ...
class IProvideWinSATAssessmentInfo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('0cd1c380-52d3-4678-ac-6f-e9-29-e4-80-be-9e')
    @commethod(7)
    def get_Score(score: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Title(title: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(description: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IProvideWinSATResultsInfo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('f8334d5d-568e-4075-87-5f-9d-f3-41-50-66-40')
    @commethod(7)
    def GetAssessmentInfo(assessment: win32more.System.AssessmentTool.WINSAT_ASSESSMENT_TYPE, ppinfo: POINTER(win32more.System.AssessmentTool.IProvideWinSATAssessmentInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_AssessmentState(state: POINTER(win32more.System.AssessmentTool.WINSAT_ASSESSMENT_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_AssessmentDateTime(fileTime: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_SystemRating(level: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_RatingStateDesc(description: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IProvideWinSATVisuals(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a9f4ade0-871a-42a3-b8-13-30-78-d2-51-62-c9')
    @commethod(3)
    def get_Bitmap(bitmapSize: win32more.System.AssessmentTool.WINSAT_BITMAP_SIZE, state: win32more.System.AssessmentTool.WINSAT_ASSESSMENT_STATE, rating: Single, pBitmap: POINTER(win32more.Graphics.Gdi.HBITMAP)) -> win32more.Foundation.HRESULT: ...
class IQueryAllWinSATAssessments(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('0b89ed1d-6398-4fea-87-fc-56-7d-8d-19-17-6f')
    @commethod(7)
    def get_AllXML(xPath: win32more.Foundation.BSTR, namespaces: win32more.Foundation.BSTR, ppDomNodeList: POINTER(win32more.Data.Xml.MsXml.IXMLDOMNodeList_head)) -> win32more.Foundation.HRESULT: ...
class IQueryOEMWinSATCustomization(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bc9a6a9f-ad4e-420e-99-53-b3-46-71-e9-df-22')
    @commethod(3)
    def GetOEMPrePopulationInfo(state: POINTER(win32more.System.AssessmentTool.WINSAT_OEM_CUSTOMIZATION_STATE)) -> win32more.Foundation.HRESULT: ...
class IQueryRecentWinSATAssessment(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('f8ad5d1f-3b47-4bdc-93-75-7c-6b-1d-a4-ec-a7')
    @commethod(7)
    def get_XML(xPath: win32more.Foundation.BSTR, namespaces: win32more.Foundation.BSTR, ppDomNodeList: POINTER(win32more.Data.Xml.MsXml.IXMLDOMNodeList_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Info(ppWinSATAssessmentInfo: POINTER(win32more.System.AssessmentTool.IProvideWinSATResultsInfo_head)) -> win32more.Foundation.HRESULT: ...
class IWinSATInitiateEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('262a1918-ba0d-41d5-92-c2-fa-b4-63-3e-e7-4f')
    @commethod(3)
    def WinSATComplete(hresult: win32more.Foundation.HRESULT, strDescription: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def WinSATUpdate(uCurrentTick: UInt32, uTickTotal: UInt32, strCurrentState: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
WINSAT_ASSESSMENT_STATE = Int32
WINSAT_ASSESSMENT_STATE_MIN: WINSAT_ASSESSMENT_STATE = 0
WINSAT_ASSESSMENT_STATE_UNKNOWN: WINSAT_ASSESSMENT_STATE = 0
WINSAT_ASSESSMENT_STATE_VALID: WINSAT_ASSESSMENT_STATE = 1
WINSAT_ASSESSMENT_STATE_INCOHERENT_WITH_HARDWARE: WINSAT_ASSESSMENT_STATE = 2
WINSAT_ASSESSMENT_STATE_NOT_AVAILABLE: WINSAT_ASSESSMENT_STATE = 3
WINSAT_ASSESSMENT_STATE_INVALID: WINSAT_ASSESSMENT_STATE = 4
WINSAT_ASSESSMENT_STATE_MAX: WINSAT_ASSESSMENT_STATE = 4
WINSAT_ASSESSMENT_TYPE = Int32
WINSAT_ASSESSMENT_MEMORY: WINSAT_ASSESSMENT_TYPE = 0
WINSAT_ASSESSMENT_CPU: WINSAT_ASSESSMENT_TYPE = 1
WINSAT_ASSESSMENT_DISK: WINSAT_ASSESSMENT_TYPE = 2
WINSAT_ASSESSMENT_D3D: WINSAT_ASSESSMENT_TYPE = 3
WINSAT_ASSESSMENT_GRAPHICS: WINSAT_ASSESSMENT_TYPE = 4
WINSAT_BITMAP_SIZE = Int32
WINSAT_BITMAP_SIZE_SMALL: WINSAT_BITMAP_SIZE = 0
WINSAT_BITMAP_SIZE_NORMAL: WINSAT_BITMAP_SIZE = 1
WINSAT_OEM_CUSTOMIZATION_STATE = Int32
WINSAT_OEM_DATA_VALID: WINSAT_OEM_CUSTOMIZATION_STATE = 0
WINSAT_OEM_DATA_NON_SYS_CONFIG_MATCH: WINSAT_OEM_CUSTOMIZATION_STATE = 1
WINSAT_OEM_DATA_INVALID: WINSAT_OEM_CUSTOMIZATION_STATE = 2
WINSAT_OEM_NO_DATA_SUPPLIED: WINSAT_OEM_CUSTOMIZATION_STATE = 3
make_head(_module, 'IAccessibleWinSAT')
make_head(_module, 'IInitiateWinSATAssessment')
make_head(_module, 'IProvideWinSATAssessmentInfo')
make_head(_module, 'IProvideWinSATResultsInfo')
make_head(_module, 'IProvideWinSATVisuals')
make_head(_module, 'IQueryAllWinSATAssessments')
make_head(_module, 'IQueryOEMWinSATCustomization')
make_head(_module, 'IQueryRecentWinSATAssessment')
make_head(_module, 'IWinSATInitiateEvents')
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
_arch_optional = [
]
