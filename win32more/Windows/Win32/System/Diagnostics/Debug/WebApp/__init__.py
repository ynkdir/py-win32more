from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript
import win32more.Windows.Win32.System.Diagnostics.Debug.WebApp
import win32more.Windows.Win32.Web.MsHtml
class IWebApplicationActivation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bcdcd0de-330e-481b-b843-4898a6a8ebac}')
    @commethod(3)
    def CancelPendingActivation(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebApplicationAuthoringMode(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IServiceProvider
    _iid_ = Guid('{720aea93-1964-4db0-b005-29eb9e2b18a9}')
    @commethod(4)
    def get_AuthoringClientBinary(self, designModeDllPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebApplicationHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cecbd2c3-a3a5-4749-9681-20e9161c6794}')
    @commethod(3)
    def get_HWND(self, hwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Document(self, htmlDocument: POINTER(win32more.Windows.Win32.Web.MsHtml.IHTMLDocument2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Advise(self, interfaceId: POINTER(Guid), callback: win32more.Windows.Win32.System.Com.IUnknown, cookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Unadvise(self, cookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebApplicationNavigationEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c22615d2-d318-4da2-8422-1fcaf77b10e4}')
    @commethod(3)
    def BeforeNavigate(self, htmlWindow: win32more.Windows.Win32.Web.MsHtml.IHTMLWindow2, url: win32more.Windows.Win32.Foundation.PWSTR, navigationFlags: UInt32, targetFrameName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def NavigateComplete(self, htmlWindow: win32more.Windows.Win32.Web.MsHtml.IHTMLWindow2, url: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NavigateError(self, htmlWindow: win32more.Windows.Win32.Web.MsHtml.IHTMLWindow2, url: win32more.Windows.Win32.Foundation.PWSTR, targetFrameName: win32more.Windows.Win32.Foundation.PWSTR, statusCode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DocumentComplete(self, htmlWindow: win32more.Windows.Win32.Web.MsHtml.IHTMLWindow2, url: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DownloadBegin(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DownloadComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebApplicationScriptEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7c3f6998-1567-4bba-b52b-48d32141d613}')
    @commethod(3)
    def BeforeScriptExecute(self, htmlWindow: win32more.Windows.Win32.Web.MsHtml.IHTMLWindow2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ScriptError(self, htmlWindow: win32more.Windows.Win32.Web.MsHtml.IHTMLWindow2, scriptError: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptError, url: win32more.Windows.Win32.Foundation.PWSTR, errorHandled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebApplicationUIEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b2b3f99-328c-41d5-a6f7-7483ed8e71dd}')
    @commethod(3)
    def SecurityProblem(self, securityProblem: UInt32, result: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebApplicationUpdateEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3e59e6b7-c652-4daf-ad5e-16feb350cde3}')
    @commethod(3)
    def OnPaint(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnCssChanged(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def RegisterAuthoringClientFunctionType(authoringModeObject: win32more.Windows.Win32.System.Diagnostics.Debug.WebApp.IWebApplicationAuthoringMode, host: win32more.Windows.Win32.System.Diagnostics.Debug.WebApp.IWebApplicationHost) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def UnregisterAuthoringClientFunctionType(host: win32more.Windows.Win32.System.Diagnostics.Debug.WebApp.IWebApplicationHost) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
