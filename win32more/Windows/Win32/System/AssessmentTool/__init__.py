from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Data.Xml.MsXml
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.System.AssessmentTool
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.UI.Accessibility
CAccessiblityWinSAT = Guid('{6e18f9c6-a3eb-495a-89b7-956482e19f7a}')
CInitiateWinSAT = Guid('{489331dc-f5e0-4528-9fda-45331bf4a571}')
CProvideWinSATVisuals = Guid('{9f377d7e-e551-44f8-9f94-9db392b03b7b}')
CQueryAllWinSAT = Guid('{05df8d13-c355-47f4-a11e-851b338cefb8}')
CQueryOEMWinSATCustomization = Guid('{c47a41b7-b729-424f-9af9-5cb3934f2dfa}')
CQueryWinSAT = Guid('{f3bdfad3-f276-49e9-9b17-c474f48f0764}')
class IAccessibleWinSAT(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IAccessible
    _iid_ = Guid('{30e6018a-94a8-4ff8-a69a-71b67413f07b}')
    @commethod(28)
    def SetAccessiblityData(self, wsName: win32more.Windows.Win32.Foundation.PWSTR, wsValue: win32more.Windows.Win32.Foundation.PWSTR, wsDesc: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInitiateWinSATAssessment(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d983fc50-f5bf-49d5-b5ed-cccb18aa7fc1}')
    @commethod(3)
    def InitiateAssessment(self, cmdLine: win32more.Windows.Win32.Foundation.PWSTR, pCallbacks: win32more.Windows.Win32.System.AssessmentTool.IWinSATInitiateEvents, callerHwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InitiateFormalAssessment(self, pCallbacks: win32more.Windows.Win32.System.AssessmentTool.IWinSATInitiateEvents, callerHwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CancelAssessment(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProvideWinSATAssessmentInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0cd1c380-52d3-4678-ac6f-e929e480be9e}')
    @commethod(7)
    def get_Score(self, score: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Title(self, title: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, description: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProvideWinSATResultsInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f8334d5d-568e-4075-875f-9df341506640}')
    @commethod(7)
    def GetAssessmentInfo(self, assessment: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_TYPE, ppinfo: POINTER(win32more.Windows.Win32.System.AssessmentTool.IProvideWinSATAssessmentInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AssessmentState(self, state: POINTER(win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_AssessmentDateTime(self, fileTime: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_SystemRating(self, level: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_RatingStateDesc(self, description: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProvideWinSATVisuals(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9f4ade0-871a-42a3-b813-3078d25162c9}')
    @commethod(3)
    def get_Bitmap(self, bitmapSize: win32more.Windows.Win32.System.AssessmentTool.WINSAT_BITMAP_SIZE, state: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_STATE, rating: Single, pBitmap: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQueryAllWinSATAssessments(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0b89ed1d-6398-4fea-87fc-567d8d19176f}')
    @commethod(7)
    def get_AllXML(self, xPath: win32more.Windows.Win32.Foundation.BSTR, namespaces: win32more.Windows.Win32.Foundation.BSTR, ppDomNodeList: POINTER(win32more.Windows.Win32.Data.Xml.MsXml.IXMLDOMNodeList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQueryOEMWinSATCustomization(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bc9a6a9f-ad4e-420e-9953-b34671e9df22}')
    @commethod(3)
    def GetOEMPrePopulationInfo(self, state: POINTER(win32more.Windows.Win32.System.AssessmentTool.WINSAT_OEM_CUSTOMIZATION_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQueryRecentWinSATAssessment(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f8ad5d1f-3b47-4bdc-9375-7c6b1da4eca7}')
    @commethod(7)
    def get_XML(self, xPath: win32more.Windows.Win32.Foundation.BSTR, namespaces: win32more.Windows.Win32.Foundation.BSTR, ppDomNodeList: POINTER(win32more.Windows.Win32.Data.Xml.MsXml.IXMLDOMNodeList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Info(self, ppWinSATAssessmentInfo: POINTER(win32more.Windows.Win32.System.AssessmentTool.IProvideWinSATResultsInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWinSATInitiateEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{262a1918-ba0d-41d5-92c2-fab4633ee74f}')
    @commethod(3)
    def WinSATComplete(self, hresult: win32more.Windows.Win32.Foundation.HRESULT, strDescription: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WinSATUpdate(self, uCurrentTick: UInt32, uTickTotal: UInt32, strCurrentState: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WINSAT_ASSESSMENT_STATE = Int32
WINSAT_ASSESSMENT_STATE_MIN: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_STATE = 0
WINSAT_ASSESSMENT_STATE_UNKNOWN: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_STATE = 0
WINSAT_ASSESSMENT_STATE_VALID: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_STATE = 1
WINSAT_ASSESSMENT_STATE_INCOHERENT_WITH_HARDWARE: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_STATE = 2
WINSAT_ASSESSMENT_STATE_NOT_AVAILABLE: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_STATE = 3
WINSAT_ASSESSMENT_STATE_INVALID: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_STATE = 4
WINSAT_ASSESSMENT_STATE_MAX: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_STATE = 4
WINSAT_ASSESSMENT_TYPE = Int32
WINSAT_ASSESSMENT_MEMORY: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_TYPE = 0
WINSAT_ASSESSMENT_CPU: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_TYPE = 1
WINSAT_ASSESSMENT_DISK: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_TYPE = 2
WINSAT_ASSESSMENT_D3D: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_TYPE = 3
WINSAT_ASSESSMENT_GRAPHICS: win32more.Windows.Win32.System.AssessmentTool.WINSAT_ASSESSMENT_TYPE = 4
WINSAT_BITMAP_SIZE = Int32
WINSAT_BITMAP_SIZE_SMALL: win32more.Windows.Win32.System.AssessmentTool.WINSAT_BITMAP_SIZE = 0
WINSAT_BITMAP_SIZE_NORMAL: win32more.Windows.Win32.System.AssessmentTool.WINSAT_BITMAP_SIZE = 1
WINSAT_OEM_CUSTOMIZATION_STATE = Int32
WINSAT_OEM_DATA_VALID: win32more.Windows.Win32.System.AssessmentTool.WINSAT_OEM_CUSTOMIZATION_STATE = 0
WINSAT_OEM_DATA_NON_SYS_CONFIG_MATCH: win32more.Windows.Win32.System.AssessmentTool.WINSAT_OEM_CUSTOMIZATION_STATE = 1
WINSAT_OEM_DATA_INVALID: win32more.Windows.Win32.System.AssessmentTool.WINSAT_OEM_CUSTOMIZATION_STATE = 2
WINSAT_OEM_NO_DATA_SUPPLIED: win32more.Windows.Win32.System.AssessmentTool.WINSAT_OEM_CUSTOMIZATION_STATE = 3


make_ready(__name__)
