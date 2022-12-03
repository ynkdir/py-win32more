from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.Diagnostics.Debug
import win32more.System.Diagnostics.Debug.WebApp
import win32more.Web.MsHtml
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
def _define_IWebApplicationActivation_head():
    class IWebApplicationActivation(win32more.System.Com.IUnknown_head):
        Guid = Guid('bcdcd0de-330e-481b-b8-43-48-98-a6-a8-eb-ac')
    return IWebApplicationActivation
def _define_IWebApplicationActivation():
    IWebApplicationActivation = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationActivation_head
    IWebApplicationActivation.CancelPendingActivation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'CancelPendingActivation', ()))
    win32more.System.Com.IUnknown
    return IWebApplicationActivation
def _define_IWebApplicationAuthoringMode_head():
    class IWebApplicationAuthoringMode(win32more.System.Com.IServiceProvider_head):
        Guid = Guid('720aea93-1964-4db0-b0-05-29-eb-9e-2b-18-a9')
    return IWebApplicationAuthoringMode
def _define_IWebApplicationAuthoringMode():
    IWebApplicationAuthoringMode = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationAuthoringMode_head
    IWebApplicationAuthoringMode.get_AuthoringClientBinary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'get_AuthoringClientBinary', ((1, 'designModeDllPath'),)))
    win32more.System.Com.IServiceProvider
    return IWebApplicationAuthoringMode
def _define_IWebApplicationHost_head():
    class IWebApplicationHost(win32more.System.Com.IUnknown_head):
        Guid = Guid('cecbd2c3-a3a5-4749-96-81-20-e9-16-1c-67-94')
    return IWebApplicationHost
def _define_IWebApplicationHost():
    IWebApplicationHost = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationHost_head
    IWebApplicationHost.get_HWND = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND))(3, 'get_HWND', ((1, 'hwnd'),)))
    IWebApplicationHost.get_Document = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Web.MsHtml.IHTMLDocument2_head))(4, 'get_Document', ((1, 'htmlDocument'),)))
    IWebApplicationHost.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Refresh', ()))
    IWebApplicationHost.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(UInt32))(6, 'Advise', ((1, 'interfaceId'),(1, 'callback'),(1, 'cookie'),)))
    IWebApplicationHost.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'Unadvise', ((1, 'cookie'),)))
    win32more.System.Com.IUnknown
    return IWebApplicationHost
def _define_IWebApplicationNavigationEvents_head():
    class IWebApplicationNavigationEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('c22615d2-d318-4da2-84-22-1f-ca-f7-7b-10-e4')
    return IWebApplicationNavigationEvents
def _define_IWebApplicationNavigationEvents():
    IWebApplicationNavigationEvents = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationNavigationEvents_head
    IWebApplicationNavigationEvents.BeforeNavigate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Web.MsHtml.IHTMLWindow2_head,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR)(3, 'BeforeNavigate', ((1, 'htmlWindow'),(1, 'url'),(1, 'navigationFlags'),(1, 'targetFrameName'),)))
    IWebApplicationNavigationEvents.NavigateComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Web.MsHtml.IHTMLWindow2_head,win32more.Foundation.PWSTR)(4, 'NavigateComplete', ((1, 'htmlWindow'),(1, 'url'),)))
    IWebApplicationNavigationEvents.NavigateError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Web.MsHtml.IHTMLWindow2_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(5, 'NavigateError', ((1, 'htmlWindow'),(1, 'url'),(1, 'targetFrameName'),(1, 'statusCode'),)))
    IWebApplicationNavigationEvents.DocumentComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Web.MsHtml.IHTMLWindow2_head,win32more.Foundation.PWSTR)(6, 'DocumentComplete', ((1, 'htmlWindow'),(1, 'url'),)))
    IWebApplicationNavigationEvents.DownloadBegin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'DownloadBegin', ()))
    IWebApplicationNavigationEvents.DownloadComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'DownloadComplete', ()))
    win32more.System.Com.IUnknown
    return IWebApplicationNavigationEvents
def _define_IWebApplicationScriptEvents_head():
    class IWebApplicationScriptEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('7c3f6998-1567-4bba-b5-2b-48-d3-21-41-d6-13')
    return IWebApplicationScriptEvents
def _define_IWebApplicationScriptEvents():
    IWebApplicationScriptEvents = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationScriptEvents_head
    IWebApplicationScriptEvents.BeforeScriptExecute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Web.MsHtml.IHTMLWindow2_head)(3, 'BeforeScriptExecute', ((1, 'htmlWindow'),)))
    IWebApplicationScriptEvents.ScriptError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Web.MsHtml.IHTMLWindow2_head,win32more.System.Diagnostics.Debug.IActiveScriptError_head,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(4, 'ScriptError', ((1, 'htmlWindow'),(1, 'scriptError'),(1, 'url'),(1, 'errorHandled'),)))
    win32more.System.Com.IUnknown
    return IWebApplicationScriptEvents
def _define_IWebApplicationUIEvents_head():
    class IWebApplicationUIEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('5b2b3f99-328c-41d5-a6-f7-74-83-ed-8e-71-dd')
    return IWebApplicationUIEvents
def _define_IWebApplicationUIEvents():
    IWebApplicationUIEvents = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationUIEvents_head
    IWebApplicationUIEvents.SecurityProblem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.HRESULT))(3, 'SecurityProblem', ((1, 'securityProblem'),(1, 'result'),)))
    win32more.System.Com.IUnknown
    return IWebApplicationUIEvents
def _define_IWebApplicationUpdateEvents_head():
    class IWebApplicationUpdateEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('3e59e6b7-c652-4daf-ad-5e-16-fe-b3-50-cd-e3')
    return IWebApplicationUpdateEvents
def _define_IWebApplicationUpdateEvents():
    IWebApplicationUpdateEvents = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationUpdateEvents_head
    IWebApplicationUpdateEvents.OnPaint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'OnPaint', ()))
    IWebApplicationUpdateEvents.OnCssChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'OnCssChanged', ()))
    win32more.System.Com.IUnknown
    return IWebApplicationUpdateEvents
def _define_RegisterAuthoringClientFunctionType():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Diagnostics.Debug.WebApp.IWebApplicationAuthoringMode_head,win32more.System.Diagnostics.Debug.WebApp.IWebApplicationHost_head)
def _define_UnregisterAuthoringClientFunctionType():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Diagnostics.Debug.WebApp.IWebApplicationHost_head)
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
