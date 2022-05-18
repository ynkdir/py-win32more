from win32more import *
import win32more.Foundation
import win32more.System.Com
import win32more.System.Diagnostics.Debug
import win32more.System.Diagnostics.Debug.WebApp
import win32more.Web.MsHtml

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
def _define_IWebApplicationScriptEvents_head():
    class IWebApplicationScriptEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('7c3f6998-1567-4bba-b52b-48d32141d613')
    return IWebApplicationScriptEvents
def _define_IWebApplicationScriptEvents():
    IWebApplicationScriptEvents = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationScriptEvents_head
    IWebApplicationScriptEvents.BeforeScriptExecute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Web.MsHtml.IHTMLWindow2_head, use_last_error=False)(3, 'BeforeScriptExecute', ((1, 'htmlWindow'),)))
    IWebApplicationScriptEvents.ScriptError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Web.MsHtml.IHTMLWindow2_head,win32more.System.Diagnostics.Debug.IActiveScriptError_head,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(4, 'ScriptError', ((1, 'htmlWindow'),(1, 'scriptError'),(1, 'url'),(1, 'errorHandled'),)))
    return IWebApplicationScriptEvents
def _define_IWebApplicationNavigationEvents_head():
    class IWebApplicationNavigationEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('c22615d2-d318-4da2-8422-1fcaf77b10e4')
    return IWebApplicationNavigationEvents
def _define_IWebApplicationNavigationEvents():
    IWebApplicationNavigationEvents = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationNavigationEvents_head
    IWebApplicationNavigationEvents.BeforeNavigate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Web.MsHtml.IHTMLWindow2_head,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(3, 'BeforeNavigate', ((1, 'htmlWindow'),(1, 'url'),(1, 'navigationFlags'),(1, 'targetFrameName'),)))
    IWebApplicationNavigationEvents.NavigateComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Web.MsHtml.IHTMLWindow2_head,win32more.Foundation.PWSTR, use_last_error=False)(4, 'NavigateComplete', ((1, 'htmlWindow'),(1, 'url'),)))
    IWebApplicationNavigationEvents.NavigateError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Web.MsHtml.IHTMLWindow2_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(5, 'NavigateError', ((1, 'htmlWindow'),(1, 'url'),(1, 'targetFrameName'),(1, 'statusCode'),)))
    IWebApplicationNavigationEvents.DocumentComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Web.MsHtml.IHTMLWindow2_head,win32more.Foundation.PWSTR, use_last_error=False)(6, 'DocumentComplete', ((1, 'htmlWindow'),(1, 'url'),)))
    IWebApplicationNavigationEvents.DownloadBegin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'DownloadBegin', ()))
    IWebApplicationNavigationEvents.DownloadComplete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'DownloadComplete', ()))
    return IWebApplicationNavigationEvents
def _define_IWebApplicationUIEvents_head():
    class IWebApplicationUIEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('5b2b3f99-328c-41d5-a6f7-7483ed8e71dd')
    return IWebApplicationUIEvents
def _define_IWebApplicationUIEvents():
    IWebApplicationUIEvents = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationUIEvents_head
    IWebApplicationUIEvents.SecurityProblem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(3, 'SecurityProblem', ((1, 'securityProblem'),(1, 'result'),)))
    return IWebApplicationUIEvents
def _define_IWebApplicationUpdateEvents_head():
    class IWebApplicationUpdateEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('3e59e6b7-c652-4daf-ad5e-16feb350cde3')
    return IWebApplicationUpdateEvents
def _define_IWebApplicationUpdateEvents():
    IWebApplicationUpdateEvents = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationUpdateEvents_head
    IWebApplicationUpdateEvents.OnPaint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnPaint', ()))
    IWebApplicationUpdateEvents.OnCssChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnCssChanged', ()))
    return IWebApplicationUpdateEvents
def _define_IWebApplicationHost_head():
    class IWebApplicationHost(win32more.System.Com.IUnknown_head):
        Guid = Guid('cecbd2c3-a3a5-4749-9681-20e9161c6794')
    return IWebApplicationHost
def _define_IWebApplicationHost():
    IWebApplicationHost = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationHost_head
    IWebApplicationHost.get_HWND = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND), use_last_error=False)(3, 'get_HWND', ((1, 'hwnd'),)))
    IWebApplicationHost.get_Document = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Web.MsHtml.IHTMLDocument2_head), use_last_error=False)(4, 'get_Document', ((1, 'htmlDocument'),)))
    IWebApplicationHost.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Refresh', ()))
    IWebApplicationHost.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(UInt32), use_last_error=False)(6, 'Advise', ((1, 'interfaceId'),(1, 'callback'),(1, 'cookie'),)))
    IWebApplicationHost.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(7, 'Unadvise', ((1, 'cookie'),)))
    return IWebApplicationHost
def _define_IWebApplicationActivation_head():
    class IWebApplicationActivation(win32more.System.Com.IUnknown_head):
        Guid = Guid('bcdcd0de-330e-481b-b843-4898a6a8ebac')
    return IWebApplicationActivation
def _define_IWebApplicationActivation():
    IWebApplicationActivation = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationActivation_head
    IWebApplicationActivation.CancelPendingActivation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'CancelPendingActivation', ()))
    return IWebApplicationActivation
def _define_IWebApplicationAuthoringMode_head():
    class IWebApplicationAuthoringMode(win32more.System.Com.IServiceProvider_head):
        Guid = Guid('720aea93-1964-4db0-b005-29eb9e2b18a9')
    return IWebApplicationAuthoringMode
def _define_IWebApplicationAuthoringMode():
    IWebApplicationAuthoringMode = win32more.System.Diagnostics.Debug.WebApp.IWebApplicationAuthoringMode_head
    IWebApplicationAuthoringMode.get_AuthoringClientBinary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_AuthoringClientBinary', ((1, 'designModeDllPath'),)))
    return IWebApplicationAuthoringMode
def _define_RegisterAuthoringClientFunctionType():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Diagnostics.Debug.WebApp.IWebApplicationAuthoringMode_head,win32more.System.Diagnostics.Debug.WebApp.IWebApplicationHost_head, use_last_error=False)
def _define_UnregisterAuthoringClientFunctionType():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Diagnostics.Debug.WebApp.IWebApplicationHost_head, use_last_error=False)
__all__ = [
    "IWebApplicationScriptEvents",
    "IWebApplicationNavigationEvents",
    "IWebApplicationUIEvents",
    "IWebApplicationUpdateEvents",
    "IWebApplicationHost",
    "IWebApplicationActivation",
    "IWebApplicationAuthoringMode",
    "RegisterAuthoringClientFunctionType",
    "UnregisterAuthoringClientFunctionType",
]
