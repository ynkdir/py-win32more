from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
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
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPrintManagerInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c5435a42-8d43-4e7b-a68a-ef311e392087}')
    @commethod(6)
    def GetForWindow(self, appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), printManager: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowPrintUIForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowConfigurationNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c056be0a-9ee2-450a-9823-964f0006f2bb}')
    @commethod(3)
    def get_PrinterQueue(self, value: POINTER(Windows.Win32.Graphics.Printing.IPrinterQueue_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_DriverProperties(self, value: POINTER(Windows.Win32.Graphics.Printing.IPrinterPropertyBag_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_UserProperties(self, value: POINTER(Windows.Win32.Graphics.Printing.IPrinterPropertyBag_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowObjectModelSourceFileContentNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{68c9e477-993e-4052-8ac6-454eff58db9d}')
    @commethod(3)
    def StartXpsOMGeneration(self, receiver: Windows.Win32.System.WinRT.Printing.IPrintWorkflowXpsReceiver_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ObjectFactory(self, value: POINTER(Windows.Win32.Storage.Xps.IXpsOMObjectFactory1_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowXpsObjectModelTargetPackageNative(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d96bc74-9b54-4ca1-ad3a-979c3d44ddac}')
    @commethod(3)
    def get_DocumentPackageTarget(self, value: POINTER(Windows.Win32.Storage.Xps.IXpsDocumentPackageTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowXpsReceiver(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{04097374-77b8-47f6-8167-aae29d4cf84b}')
    @commethod(3)
    def SetDocumentSequencePrintTicket(self, documentSequencePrintTicket: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDocumentSequenceUri(self, documentSequenceUri: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddDocumentData(self, documentId: UInt32, documentPrintTicket: Windows.Win32.System.Com.IStream_head, documentUri: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddPage(self, documentId: UInt32, pageId: UInt32, pageReference: Windows.Win32.Storage.Xps.IXpsOMPageReference_head, pageUri: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowXpsReceiver2(ComPtr):
    extends: Windows.Win32.System.WinRT.Printing.IPrintWorkflowXpsReceiver
    _iid_ = Guid('{023bcc0c-dfab-4a61-b074-490c6995580d}')
    @commethod(8)
    def Failed(self, XpsError: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IPrinting3DManagerInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9ca31010-1484-4587-b26b-dddf9f9caecd}')
    @commethod(6)
    def GetForWindow(self, appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), printManager: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowPrintUIForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IPrintManagerInterop')
make_head(_module, 'IPrintWorkflowConfigurationNative')
make_head(_module, 'IPrintWorkflowObjectModelSourceFileContentNative')
make_head(_module, 'IPrintWorkflowXpsObjectModelTargetPackageNative')
make_head(_module, 'IPrintWorkflowXpsReceiver')
make_head(_module, 'IPrintWorkflowXpsReceiver2')
make_head(_module, 'IPrinting3DManagerInterop')
