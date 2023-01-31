from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
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
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class IPrintManagerInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('c5435a42-8d43-4e7b-a6-8a-ef-31-1e-39-20-87')
    @commethod(6)
    def GetForWindow(appWindow: win32more.Foundation.HWND, riid: POINTER(Guid), printManager: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ShowPrintUIForWindowAsync(appWindow: win32more.Foundation.HWND, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IPrintWorkflowConfigurationNative(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c056be0a-9ee2-450a-98-23-96-4f-00-06-f2-bb')
    @commethod(3)
    def get_PrinterQueue(value: POINTER(win32more.Graphics.Printing.IPrinterQueue_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_DriverProperties(value: POINTER(win32more.Graphics.Printing.IPrinterPropertyBag_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_UserProperties(value: POINTER(win32more.Graphics.Printing.IPrinterPropertyBag_head)) -> win32more.Foundation.HRESULT: ...
class IPrintWorkflowObjectModelSourceFileContentNative(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('68c9e477-993e-4052-8a-c6-45-4e-ff-58-db-9d')
    @commethod(3)
    def StartXpsOMGeneration(receiver: win32more.System.WinRT.Printing.IPrintWorkflowXpsReceiver_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_ObjectFactory(value: POINTER(win32more.Storage.Xps.IXpsOMObjectFactory1_head)) -> win32more.Foundation.HRESULT: ...
class IPrintWorkflowXpsObjectModelTargetPackageNative(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7d96bc74-9b54-4ca1-ad-3a-97-9c-3d-44-dd-ac')
    @commethod(3)
    def get_DocumentPackageTarget(value: POINTER(win32more.Storage.Xps.IXpsDocumentPackageTarget_head)) -> win32more.Foundation.HRESULT: ...
class IPrintWorkflowXpsReceiver(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('04097374-77b8-47f6-81-67-aa-e2-9d-4c-f8-4b')
    @commethod(3)
    def SetDocumentSequencePrintTicket(documentSequencePrintTicket: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetDocumentSequenceUri(documentSequenceUri: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddDocumentData(documentId: UInt32, documentPrintTicket: win32more.System.Com.IStream_head, documentUri: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def AddPage(documentId: UInt32, pageId: UInt32, pageReference: win32more.Storage.Xps.IXpsOMPageReference_head, pageUri: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Close() -> win32more.Foundation.HRESULT: ...
class IPrintWorkflowXpsReceiver2(c_void_p):
    extends: win32more.System.WinRT.Printing.IPrintWorkflowXpsReceiver
    Guid = Guid('023bcc0c-dfab-4a61-b0-74-49-0c-69-95-58-0d')
    @commethod(8)
    def Failed(XpsError: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
class IPrinting3DManagerInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('9ca31010-1484-4587-b2-6b-dd-df-9f-9c-ae-cd')
    @commethod(6)
    def GetForWindow(appWindow: win32more.Foundation.HWND, riid: POINTER(Guid), printManager: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ShowPrintUIForWindowAsync(appWindow: win32more.Foundation.HWND, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IPrintManagerInterop')
make_head(_module, 'IPrintWorkflowConfigurationNative')
make_head(_module, 'IPrintWorkflowObjectModelSourceFileContentNative')
make_head(_module, 'IPrintWorkflowXpsObjectModelTargetPackageNative')
make_head(_module, 'IPrintWorkflowXpsReceiver')
make_head(_module, 'IPrintWorkflowXpsReceiver2')
make_head(_module, 'IPrinting3DManagerInterop')
__all__ = [
    "IPrintManagerInterop",
    "IPrintWorkflowConfigurationNative",
    "IPrintWorkflowObjectModelSourceFileContentNative",
    "IPrintWorkflowXpsObjectModelTargetPackageNative",
    "IPrintWorkflowXpsReceiver",
    "IPrintWorkflowXpsReceiver2",
    "IPrinting3DManagerInterop",
]
_arch_optional = [
]
