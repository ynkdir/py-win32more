from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
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
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_IPrinting3DManagerInterop_head():
    class IPrinting3DManagerInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('9ca31010-1484-4587-b2-6b-dd-df-9f-9c-ae-cd')
    return IPrinting3DManagerInterop
def _define_IPrinting3DManagerInterop():
    IPrinting3DManagerInterop = win32more.System.WinRT.Printing.IPrinting3DManagerInterop_head
    IPrinting3DManagerInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'GetForWindow', ((1, 'appWindow'),(1, 'riid'),(1, 'printManager'),)))
    IPrinting3DManagerInterop.ShowPrintUIForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(7, 'ShowPrintUIForWindowAsync', ((1, 'appWindow'),(1, 'riid'),(1, 'asyncOperation'),)))
    win32more.System.WinRT.IInspectable
    return IPrinting3DManagerInterop
def _define_IPrintManagerInterop_head():
    class IPrintManagerInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('c5435a42-8d43-4e7b-a6-8a-ef-31-1e-39-20-87')
    return IPrintManagerInterop
def _define_IPrintManagerInterop():
    IPrintManagerInterop = win32more.System.WinRT.Printing.IPrintManagerInterop_head
    IPrintManagerInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'GetForWindow', ((1, 'appWindow'),(1, 'riid'),(1, 'printManager'),)))
    IPrintManagerInterop.ShowPrintUIForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(7, 'ShowPrintUIForWindowAsync', ((1, 'appWindow'),(1, 'riid'),(1, 'asyncOperation'),)))
    win32more.System.WinRT.IInspectable
    return IPrintManagerInterop
def _define_IPrintWorkflowConfigurationNative_head():
    class IPrintWorkflowConfigurationNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('c056be0a-9ee2-450a-98-23-96-4f-00-06-f2-bb')
    return IPrintWorkflowConfigurationNative
def _define_IPrintWorkflowConfigurationNative():
    IPrintWorkflowConfigurationNative = win32more.System.WinRT.Printing.IPrintWorkflowConfigurationNative_head
    IPrintWorkflowConfigurationNative.get_PrinterQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Printing.IPrinterQueue_head))(3, 'get_PrinterQueue', ((1, 'value'),)))
    IPrintWorkflowConfigurationNative.get_DriverProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Printing.IPrinterPropertyBag_head))(4, 'get_DriverProperties', ((1, 'value'),)))
    IPrintWorkflowConfigurationNative.get_UserProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Printing.IPrinterPropertyBag_head))(5, 'get_UserProperties', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IPrintWorkflowConfigurationNative
def _define_IPrintWorkflowObjectModelSourceFileContentNative_head():
    class IPrintWorkflowObjectModelSourceFileContentNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('68c9e477-993e-4052-8a-c6-45-4e-ff-58-db-9d')
    return IPrintWorkflowObjectModelSourceFileContentNative
def _define_IPrintWorkflowObjectModelSourceFileContentNative():
    IPrintWorkflowObjectModelSourceFileContentNative = win32more.System.WinRT.Printing.IPrintWorkflowObjectModelSourceFileContentNative_head
    IPrintWorkflowObjectModelSourceFileContentNative.StartXpsOMGeneration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.Printing.IPrintWorkflowXpsReceiver_head)(3, 'StartXpsOMGeneration', ((1, 'receiver'),)))
    IPrintWorkflowObjectModelSourceFileContentNative.get_ObjectFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMObjectFactory1_head))(4, 'get_ObjectFactory', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IPrintWorkflowObjectModelSourceFileContentNative
def _define_IPrintWorkflowXpsObjectModelTargetPackageNative_head():
    class IPrintWorkflowXpsObjectModelTargetPackageNative(win32more.System.Com.IUnknown_head):
        Guid = Guid('7d96bc74-9b54-4ca1-ad-3a-97-9c-3d-44-dd-ac')
    return IPrintWorkflowXpsObjectModelTargetPackageNative
def _define_IPrintWorkflowXpsObjectModelTargetPackageNative():
    IPrintWorkflowXpsObjectModelTargetPackageNative = win32more.System.WinRT.Printing.IPrintWorkflowXpsObjectModelTargetPackageNative_head
    IPrintWorkflowXpsObjectModelTargetPackageNative.get_DocumentPackageTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsDocumentPackageTarget_head))(3, 'get_DocumentPackageTarget', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IPrintWorkflowXpsObjectModelTargetPackageNative
def _define_IPrintWorkflowXpsReceiver_head():
    class IPrintWorkflowXpsReceiver(win32more.System.Com.IUnknown_head):
        Guid = Guid('04097374-77b8-47f6-81-67-aa-e2-9d-4c-f8-4b')
    return IPrintWorkflowXpsReceiver
def _define_IPrintWorkflowXpsReceiver():
    IPrintWorkflowXpsReceiver = win32more.System.WinRT.Printing.IPrintWorkflowXpsReceiver_head
    IPrintWorkflowXpsReceiver.SetDocumentSequencePrintTicket = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(3, 'SetDocumentSequencePrintTicket', ((1, 'documentSequencePrintTicket'),)))
    IPrintWorkflowXpsReceiver.SetDocumentSequenceUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(4, 'SetDocumentSequenceUri', ((1, 'documentSequenceUri'),)))
    IPrintWorkflowXpsReceiver.AddDocumentData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IStream_head,win32more.Foundation.PWSTR)(5, 'AddDocumentData', ((1, 'documentId'),(1, 'documentPrintTicket'),(1, 'documentUri'),)))
    IPrintWorkflowXpsReceiver.AddPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Storage.Xps.IXpsOMPageReference_head,win32more.Foundation.PWSTR)(6, 'AddPage', ((1, 'documentId'),(1, 'pageId'),(1, 'pageReference'),(1, 'pageUri'),)))
    IPrintWorkflowXpsReceiver.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Close', ()))
    win32more.System.Com.IUnknown
    return IPrintWorkflowXpsReceiver
def _define_IPrintWorkflowXpsReceiver2_head():
    class IPrintWorkflowXpsReceiver2(win32more.System.WinRT.Printing.IPrintWorkflowXpsReceiver_head):
        Guid = Guid('023bcc0c-dfab-4a61-b0-74-49-0c-69-95-58-0d')
    return IPrintWorkflowXpsReceiver2
def _define_IPrintWorkflowXpsReceiver2():
    IPrintWorkflowXpsReceiver2 = win32more.System.WinRT.Printing.IPrintWorkflowXpsReceiver2_head
    IPrintWorkflowXpsReceiver2.Failed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(8, 'Failed', ((1, 'XpsError'),)))
    win32more.System.WinRT.Printing.IPrintWorkflowXpsReceiver
    return IPrintWorkflowXpsReceiver2
__all__ = [
    "IPrintManagerInterop",
    "IPrintWorkflowConfigurationNative",
    "IPrintWorkflowObjectModelSourceFileContentNative",
    "IPrintWorkflowXpsObjectModelTargetPackageNative",
    "IPrintWorkflowXpsReceiver",
    "IPrintWorkflowXpsReceiver2",
    "IPrinting3DManagerInterop",
]
