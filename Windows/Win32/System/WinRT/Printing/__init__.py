from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Printing
import Windows.Win32.Storage.Xps
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT
import Windows.Win32.System.WinRT.Printing
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
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c5435a42-8d43-4e7b-a6-8a-ef-31-1e-39-20-87')
    @commethod(6)
    def GetForWindow(appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), printManager: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowPrintUIForWindowAsync(appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowConfigurationNative(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c056be0a-9ee2-450a-98-23-96-4f-00-06-f2-bb')
    @commethod(3)
    def get_PrinterQueue(value: POINTER(Windows.Win32.Graphics.Printing.IPrinterQueue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_DriverProperties(value: POINTER(Windows.Win32.Graphics.Printing.IPrinterPropertyBag_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_UserProperties(value: POINTER(Windows.Win32.Graphics.Printing.IPrinterPropertyBag_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowObjectModelSourceFileContentNative(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('68c9e477-993e-4052-8a-c6-45-4e-ff-58-db-9d')
    @commethod(3)
    def StartXpsOMGeneration(receiver: Windows.Win32.System.WinRT.Printing.IPrintWorkflowXpsReceiver_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ObjectFactory(value: POINTER(Windows.Win32.Storage.Xps.IXpsOMObjectFactory1_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowXpsObjectModelTargetPackageNative(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7d96bc74-9b54-4ca1-ad-3a-97-9c-3d-44-dd-ac')
    @commethod(3)
    def get_DocumentPackageTarget(value: POINTER(Windows.Win32.Storage.Xps.IXpsDocumentPackageTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowXpsReceiver(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('04097374-77b8-47f6-81-67-aa-e2-9d-4c-f8-4b')
    @commethod(3)
    def SetDocumentSequencePrintTicket(documentSequencePrintTicket: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDocumentSequenceUri(documentSequenceUri: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddDocumentData(documentId: UInt32, documentPrintTicket: Windows.Win32.System.Com.IStream_head, documentUri: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddPage(documentId: UInt32, pageId: UInt32, pageReference: Windows.Win32.Storage.Xps.IXpsOMPageReference_head, pageUri: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowXpsReceiver2(c_void_p):
    extends: Windows.Win32.System.WinRT.Printing.IPrintWorkflowXpsReceiver
    Guid = Guid('023bcc0c-dfab-4a61-b0-74-49-0c-69-95-58-0d')
    @commethod(8)
    def Failed(XpsError: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IPrinting3DManagerInterop(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9ca31010-1484-4587-b2-6b-dd-df-9f-9c-ae-cd')
    @commethod(6)
    def GetForWindow(appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), printManager: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowPrintUIForWindowAsync(appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
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
