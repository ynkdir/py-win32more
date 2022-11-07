from win32more import *
import win32more.Foundation
import win32more.Graphics.Printing
import win32more.Storage.Xps
import win32more.System.Com
import win32more.System.WinRT
import win32more.System.WinRT.Printing

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
def _define_IPrinting3DManagerInterop_head():
    class IPrinting3DManagerInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('9ca31010-1484-4587-b26b-dddf9f9caecd')
    return IPrinting3DManagerInterop
def _define_IPrinting3DManagerInterop():
    IPrinting3DManagerInterop = win32more.System.WinRT.Printing.IPrinting3DManagerInterop_head
    IPrinting3DManagerInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetForWindow', ((1, 'appWindow'),(1, 'riid'),(1, 'printManager'),)))
    IPrinting3DManagerInterop.ShowPrintUIForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(7, 'ShowPrintUIForWindowAsync', ((1, 'appWindow'),(1, 'riid'),(1, 'asyncOperation'),)))
    win32more.System.WinRT.IInspectable
    return IPrinting3DManagerInterop
def _define_IPrintManagerInterop_head():
    class IPrintManagerInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('c5435a42-8d43-4e7b-a68a-ef311e392087')
    return IPrintManagerInterop
def _define_IPrintManagerInterop():
    IPrintManagerInterop = win32more.System.WinRT.Printing.IPrintManagerInterop_head
    IPrintManagerInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetForWindow', ((1, 'appWindow'),(1, 'riid'),(1, 'printManager'),)))
    IPrintManagerInterop.ShowPrintUIForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(7, 'ShowPrintUIForWindowAsync', ((1, 'appWindow'),(1, 'riid'),(1, 'asyncOperation'),)))
    win32more.System.WinRT.IInspectable
    return IPrintManagerInterop
def _define_IPrintWorkflowXpsReceiver_head():
    class IPrintWorkflowXpsReceiver(win32more.System.Com.IUnknown_head):
        Guid = Guid('04097374-77b8-47f6-8167-aae29d4cf84b')
    return IPrintWorkflowXpsReceiver
def _define_IPrintWorkflowXpsReceiver():
    IPrintWorkflowXpsReceiver = win32more.System.WinRT.Printing.IPrintWorkflowXpsReceiver_head
    IPrintWorkflowXpsReceiver.SetDocumentSequencePrintTicket = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head, use_last_error=False)(3, 'SetDocumentSequencePrintTicket', ((1, 'documentSequencePrintTicket'),)))
    IPrintWorkflowXpsReceiver.SetDocumentSequenceUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'SetDocumentSequenceUri', ((1, 'documentSequenceUri'),)))
    IPrintWorkflowXpsReceiver.AddDocumentData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IStream_head,win32more.Foundation.PWSTR, use_last_error=False)(5, 'AddDocumentData', ((1, 'documentId'),(1, 'documentPrintTicket'),(1, 'documentUri'),)))
    IPrintWorkflowXpsReceiver.AddPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Storage.Xps.IXpsOMPageReference_head,win32more.Foundation.PWSTR, use_last_error=False)(6, 'AddPage', ((1, 'documentId'),(1, 'pageId'),(1, 'pageReference'),(1, 'pageUri'),)))
    IPrintWorkflowXpsReceiver.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Close', ()))
    win32more.System.Com.IUnknown
    return IPrintWorkflowXpsReceiver
def _define_IPrintWorkflowXpsReceiver2_head():
    class IPrintWorkflowXpsReceiver2(win32more.System.WinRT.Printing.IPrintWorkflowXpsReceiver_head):
        Guid = Guid('023bcc0c-dfab-4a61-b074-490c6995580d')
    return IPrintWorkflowXpsReceiver2
def _define_IPrintWorkflowXpsReceiver2():
    IPrintWorkflowXpsReceiver2 = win32more.System.WinRT.Printing.IPrintWorkflowXpsReceiver2_head
    IPrintWorkflowXpsReceiver2.Failed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT, use_last_error=False)(8, 'Failed', ((1, 'XpsError'),)))
    win32more.System.WinRT.Printing.IPrintWorkflowXpsReceiver
    return IPrintWorkflowXpsReceiver2
def _define_IPrintWorkflowObjectModelSourceFileContentNative_head():
    class IPrintWorkflowObjectModelSourceFileContentNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('68c9e477-993e-4052-8ac6-454eff58db9d')
    return IPrintWorkflowObjectModelSourceFileContentNative
def _define_IPrintWorkflowObjectModelSourceFileContentNative():
    IPrintWorkflowObjectModelSourceFileContentNative = win32more.System.WinRT.Printing.IPrintWorkflowObjectModelSourceFileContentNative_head
    IPrintWorkflowObjectModelSourceFileContentNative.StartXpsOMGeneration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Printing.IPrintWorkflowXpsReceiver_head, use_last_error=False)(3, 'StartXpsOMGeneration', ((1, 'receiver'),)))
    IPrintWorkflowObjectModelSourceFileContentNative.get_ObjectFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMObjectFactory1_head), use_last_error=False)(4, 'get_ObjectFactory', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IPrintWorkflowObjectModelSourceFileContentNative
def _define_IPrintWorkflowXpsObjectModelTargetPackageNative_head():
    class IPrintWorkflowXpsObjectModelTargetPackageNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('7d96bc74-9b54-4ca1-ad3a-979c3d44ddac')
    return IPrintWorkflowXpsObjectModelTargetPackageNative
def _define_IPrintWorkflowXpsObjectModelTargetPackageNative():
    IPrintWorkflowXpsObjectModelTargetPackageNative = win32more.System.WinRT.Printing.IPrintWorkflowXpsObjectModelTargetPackageNative_head
    IPrintWorkflowXpsObjectModelTargetPackageNative.get_DocumentPackageTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsDocumentPackageTarget_head), use_last_error=False)(3, 'get_DocumentPackageTarget', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IPrintWorkflowXpsObjectModelTargetPackageNative
def _define_IPrintWorkflowConfigurationNative_head():
    class IPrintWorkflowConfigurationNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('c056be0a-9ee2-450a-9823-964f0006f2bb')
    return IPrintWorkflowConfigurationNative
def _define_IPrintWorkflowConfigurationNative():
    IPrintWorkflowConfigurationNative = win32more.System.WinRT.Printing.IPrintWorkflowConfigurationNative_head
    IPrintWorkflowConfigurationNative.get_PrinterQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Printing.IPrinterQueue_head), use_last_error=False)(3, 'get_PrinterQueue', ((1, 'value'),)))
    IPrintWorkflowConfigurationNative.get_DriverProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Printing.IPrinterPropertyBag_head), use_last_error=False)(4, 'get_DriverProperties', ((1, 'value'),)))
    IPrintWorkflowConfigurationNative.get_UserProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Printing.IPrinterPropertyBag_head), use_last_error=False)(5, 'get_UserProperties', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IPrintWorkflowConfigurationNative
__all__ = [
    "IPrinting3DManagerInterop",
    "IPrintManagerInterop",
    "IPrintWorkflowXpsReceiver",
    "IPrintWorkflowXpsReceiver2",
    "IPrintWorkflowObjectModelSourceFileContentNative",
    "IPrintWorkflowXpsObjectModelTargetPackageNative",
    "IPrintWorkflowConfigurationNative",
]
