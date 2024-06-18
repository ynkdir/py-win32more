from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Printing
import win32more.Windows.Win32.Storage.Xps
import win32more.Windows.Win32.Storage.Xps.Printing
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.System.WinRT.Printing
class IPrintDocumentPageSource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a96bb1db-172e-4667-82b5-ad97a252318f}')
    @commethod(3)
    def GetPreviewPageCollection(self, docPackageTarget: win32more.Windows.Win32.Storage.Xps.Printing.IPrintDocumentPackageTarget, docPageCollection: POINTER(win32more.Windows.Win32.System.WinRT.Printing.IPrintPreviewPageCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MakeDocument(self, printTaskOptions: win32more.Windows.Win32.System.WinRT.IInspectable, docPackageTarget: win32more.Windows.Win32.Storage.Xps.Printing.IPrintDocumentPackageTarget) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintManagerInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c5435a42-8d43-4e7b-a68a-ef311e392087}')
    @commethod(6)
    def GetForWindow(self, appWindow: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), printManager: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowPrintUIForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintPreviewPageCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0b31cc62-d7ec-4747-9d6e-f2537d870f2b}')
    @commethod(3)
    def Paginate(self, currentJobPage: UInt32, printTaskOptions: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MakePage(self, desiredJobPage: UInt32, width: Single, height: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowConfigurationNative(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c056be0a-9ee2-450a-9823-964f0006f2bb}')
    @commethod(3)
    def get_PrinterQueue(self, value: POINTER(win32more.Windows.Win32.Graphics.Printing.IPrinterQueue)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_DriverProperties(self, value: POINTER(win32more.Windows.Win32.Graphics.Printing.IPrinterPropertyBag)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_UserProperties(self, value: POINTER(win32more.Windows.Win32.Graphics.Printing.IPrinterPropertyBag)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowObjectModelSourceFileContentNative(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{68c9e477-993e-4052-8ac6-454eff58db9d}')
    @commethod(3)
    def StartXpsOMGeneration(self, receiver: win32more.Windows.Win32.System.WinRT.Printing.IPrintWorkflowXpsReceiver) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ObjectFactory(self, value: POINTER(win32more.Windows.Win32.Storage.Xps.IXpsOMObjectFactory1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowXpsObjectModelTargetPackageNative(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d96bc74-9b54-4ca1-ad3a-979c3d44ddac}')
    @commethod(3)
    def get_DocumentPackageTarget(self, value: POINTER(win32more.Windows.Win32.Storage.Xps.IXpsDocumentPackageTarget)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowXpsReceiver(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{04097374-77b8-47f6-8167-aae29d4cf84b}')
    @commethod(3)
    def SetDocumentSequencePrintTicket(self, documentSequencePrintTicket: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDocumentSequenceUri(self, documentSequenceUri: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddDocumentData(self, documentId: UInt32, documentPrintTicket: win32more.Windows.Win32.System.Com.IStream, documentUri: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddPage(self, documentId: UInt32, pageId: UInt32, pageReference: win32more.Windows.Win32.Storage.Xps.IXpsOMPageReference, pageUri: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintWorkflowXpsReceiver2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.Printing.IPrintWorkflowXpsReceiver
    _iid_ = Guid('{023bcc0c-dfab-4a61-b074-490c6995580d}')
    @commethod(8)
    def Failed(self, XpsError: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrinting3DManagerInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9ca31010-1484-4587-b26b-dddf9f9caecd}')
    @commethod(6)
    def GetForWindow(self, appWindow: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), printManager: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowPrintUIForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
