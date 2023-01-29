from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.Diagnostics.Debug
import win32more.System.Diagnostics.Debug.WebApp
import win32more.Web.MsHtml
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
class IWebApplicationActivation(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bcdcd0de-330e-481b-b8-43-48-98-a6-a8-eb-ac')
    @commethod(3)
    def CancelPendingActivation() -> win32more.Foundation.HRESULT: ...
class IWebApplicationAuthoringMode(c_void_p):
    extends: win32more.System.Com.IServiceProvider
    Guid = Guid('720aea93-1964-4db0-b0-05-29-eb-9e-2b-18-a9')
    @commethod(4)
    def get_AuthoringClientBinary(designModeDllPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IWebApplicationHost(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('cecbd2c3-a3a5-4749-96-81-20-e9-16-1c-67-94')
    @commethod(3)
    def get_HWND(hwnd: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_Document(htmlDocument: POINTER(win32more.Web.MsHtml.IHTMLDocument2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Refresh() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Advise(interfaceId: POINTER(Guid), callback: win32more.System.Com.IUnknown_head, cookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Unadvise(cookie: UInt32) -> win32more.Foundation.HRESULT: ...
class IWebApplicationNavigationEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c22615d2-d318-4da2-84-22-1f-ca-f7-7b-10-e4')
    @commethod(3)
    def BeforeNavigate(htmlWindow: win32more.Web.MsHtml.IHTMLWindow2_head, url: win32more.Foundation.PWSTR, navigationFlags: UInt32, targetFrameName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def NavigateComplete(htmlWindow: win32more.Web.MsHtml.IHTMLWindow2_head, url: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def NavigateError(htmlWindow: win32more.Web.MsHtml.IHTMLWindow2_head, url: win32more.Foundation.PWSTR, targetFrameName: win32more.Foundation.PWSTR, statusCode: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def DocumentComplete(htmlWindow: win32more.Web.MsHtml.IHTMLWindow2_head, url: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def DownloadBegin() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def DownloadComplete() -> win32more.Foundation.HRESULT: ...
class IWebApplicationScriptEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7c3f6998-1567-4bba-b5-2b-48-d3-21-41-d6-13')
    @commethod(3)
    def BeforeScriptExecute(htmlWindow: win32more.Web.MsHtml.IHTMLWindow2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ScriptError(htmlWindow: win32more.Web.MsHtml.IHTMLWindow2_head, scriptError: win32more.System.Diagnostics.Debug.IActiveScriptError_head, url: win32more.Foundation.PWSTR, errorHandled: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IWebApplicationUIEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5b2b3f99-328c-41d5-a6-f7-74-83-ed-8e-71-dd')
    @commethod(3)
    def SecurityProblem(securityProblem: UInt32, result: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
class IWebApplicationUpdateEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3e59e6b7-c652-4daf-ad-5e-16-fe-b3-50-cd-e3')
    @commethod(3)
    def OnPaint() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnCssChanged() -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def RegisterAuthoringClientFunctionType(authoringModeObject: win32more.System.Diagnostics.Debug.WebApp.IWebApplicationAuthoringMode_head, host: win32more.System.Diagnostics.Debug.WebApp.IWebApplicationHost_head) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def UnregisterAuthoringClientFunctionType(host: win32more.System.Diagnostics.Debug.WebApp.IWebApplicationHost_head) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IWebApplicationActivation')
make_head(_module, 'IWebApplicationAuthoringMode')
make_head(_module, 'IWebApplicationHost')
make_head(_module, 'IWebApplicationNavigationEvents')
make_head(_module, 'IWebApplicationScriptEvents')
make_head(_module, 'IWebApplicationUIEvents')
make_head(_module, 'IWebApplicationUpdateEvents')
make_head(_module, 'RegisterAuthoringClientFunctionType')
make_head(_module, 'UnregisterAuthoringClientFunctionType')
__all__ = [
    "IWebApplicationActivation",
    "IWebApplicationAuthoringMode",
    "IWebApplicationHost",
    "IWebApplicationNavigationEvents",
    "IWebApplicationScriptEvents",
    "IWebApplicationUIEvents",
    "IWebApplicationUpdateEvents",
    "RegisterAuthoringClientFunctionType",
    "UnregisterAuthoringClientFunctionType",
]
_arch_optional = [
]
