from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Diagnostics.Debug.ActiveScript
import Windows.Win32.System.Diagnostics.Debug.WebApp
import Windows.Win32.Web.MsHtml
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IWebApplicationActivation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bcdcd0de-330e-481b-b843-4898a6a8ebac}')
    @commethod(3)
    def CancelPendingActivation(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWebApplicationAuthoringMode(ComPtr):
    extends: Windows.Win32.System.Com.IServiceProvider
    _iid_ = Guid('{720aea93-1964-4db0-b005-29eb9e2b18a9}')
    @commethod(4)
    def get_AuthoringClientBinary(self, designModeDllPath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IWebApplicationHost(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cecbd2c3-a3a5-4749-9681-20e9161c6794}')
    @commethod(3)
    def get_HWND(self, hwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Document(self, htmlDocument: POINTER(Windows.Win32.Web.MsHtml.IHTMLDocument2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Advise(self, interfaceId: POINTER(Guid), callback: Windows.Win32.System.Com.IUnknown_head, cookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Unadvise(self, cookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWebApplicationNavigationEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c22615d2-d318-4da2-8422-1fcaf77b10e4}')
    @commethod(3)
    def BeforeNavigate(self, htmlWindow: Windows.Win32.Web.MsHtml.IHTMLWindow2_head, url: Windows.Win32.Foundation.PWSTR, navigationFlags: UInt32, targetFrameName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NavigateComplete(self, htmlWindow: Windows.Win32.Web.MsHtml.IHTMLWindow2_head, url: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NavigateError(self, htmlWindow: Windows.Win32.Web.MsHtml.IHTMLWindow2_head, url: Windows.Win32.Foundation.PWSTR, targetFrameName: Windows.Win32.Foundation.PWSTR, statusCode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DocumentComplete(self, htmlWindow: Windows.Win32.Web.MsHtml.IHTMLWindow2_head, url: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DownloadBegin(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DownloadComplete(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWebApplicationScriptEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7c3f6998-1567-4bba-b52b-48d32141d613}')
    @commethod(3)
    def BeforeScriptExecute(self, htmlWindow: Windows.Win32.Web.MsHtml.IHTMLWindow2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ScriptError(self, htmlWindow: Windows.Win32.Web.MsHtml.IHTMLWindow2_head, scriptError: Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptError_head, url: Windows.Win32.Foundation.PWSTR, errorHandled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IWebApplicationUIEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b2b3f99-328c-41d5-a6f7-7483ed8e71dd}')
    @commethod(3)
    def SecurityProblem(self, securityProblem: UInt32, result: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class IWebApplicationUpdateEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3e59e6b7-c652-4daf-ad5e-16feb350cde3}')
    @commethod(3)
    def OnPaint(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnCssChanged(self) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def RegisterAuthoringClientFunctionType(authoringModeObject: Windows.Win32.System.Diagnostics.Debug.WebApp.IWebApplicationAuthoringMode_head, host: Windows.Win32.System.Diagnostics.Debug.WebApp.IWebApplicationHost_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def UnregisterAuthoringClientFunctionType(host: Windows.Win32.System.Diagnostics.Debug.WebApp.IWebApplicationHost_head) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IWebApplicationActivation')
make_head(_module, 'IWebApplicationAuthoringMode')
make_head(_module, 'IWebApplicationHost')
make_head(_module, 'IWebApplicationNavigationEvents')
make_head(_module, 'IWebApplicationScriptEvents')
make_head(_module, 'IWebApplicationUIEvents')
make_head(_module, 'IWebApplicationUpdateEvents')
make_head(_module, 'RegisterAuthoringClientFunctionType')
make_head(_module, 'UnregisterAuthoringClientFunctionType')
