from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.Xps
import win32more.Windows.Win32.Storage.Xps.Printing
import win32more.Windows.Win32.System.Com
ID_DOCUMENTPACKAGETARGET_MSXPS: Guid = Guid('{9cae40a8-ded1-41c9-a9fd-d735ef33aeda}')
ID_DOCUMENTPACKAGETARGET_OPENXPS: Guid = Guid('{0056bb72-8c9c-4612-bd0f-93012a87099d}')
ID_DOCUMENTPACKAGETARGET_OPENXPS_WITH_3D: Guid = Guid('{63dbd720-8b14-4577-b074-7bb11b596d28}')
@winfunctype('XPSPRINT.dll')
def StartXpsPrintJob(printerName: win32more.Windows.Win32.Foundation.PWSTR, jobName: win32more.Windows.Win32.Foundation.PWSTR, outputFileName: win32more.Windows.Win32.Foundation.PWSTR, progressEvent: win32more.Windows.Win32.Foundation.HANDLE, completionEvent: win32more.Windows.Win32.Foundation.HANDLE, printablePagesOn: POINTER(Byte), printablePagesOnCount: UInt32, xpsPrintJob: POINTER(win32more.Windows.Win32.Storage.Xps.Printing.IXpsPrintJob), documentStream: POINTER(win32more.Windows.Win32.Storage.Xps.Printing.IXpsPrintJobStream), printTicketStream: POINTER(win32more.Windows.Win32.Storage.Xps.Printing.IXpsPrintJobStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XPSPRINT.dll')
def StartXpsPrintJob1(printerName: win32more.Windows.Win32.Foundation.PWSTR, jobName: win32more.Windows.Win32.Foundation.PWSTR, outputFileName: win32more.Windows.Win32.Foundation.PWSTR, progressEvent: win32more.Windows.Win32.Foundation.HANDLE, completionEvent: win32more.Windows.Win32.Foundation.HANDLE, xpsPrintJob: POINTER(win32more.Windows.Win32.Storage.Xps.Printing.IXpsPrintJob), printContentReceiver: POINTER(win32more.Windows.Win32.Storage.Xps.IXpsOMPackageTarget)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintDocumentPackageStatusEvent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ed90c8ad-5c34-4d05-a1ec-0e8a9b3ad7af}')
    @commethod(7)
    def PackageStatusUpdated(self, packageStatus: POINTER(win32more.Windows.Win32.Storage.Xps.Printing.PrintDocumentPackageStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintDocumentPackageTarget(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1b8efec4-3019-4c27-964e-367202156906}')
    @commethod(3)
    def GetPackageTargetTypes(self, targetCount: POINTER(UInt32), targetTypes: POINTER(POINTER(Guid))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPackageTarget(self, guidTargetType: POINTER(Guid), riid: POINTER(Guid), ppvTarget: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintDocumentPackageTarget2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c560298a-535c-48f9-866a-632540660cb4}')
    @commethod(3)
    def GetIsTargetIppPrinter(self, isIppPrinter: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTargetIppPrintDevice(self, riid: POINTER(Guid), ppvTarget: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintDocumentPackageTargetFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2959bf7-b31b-4a3d-9600-712eb1335ba4}')
    @commethod(3)
    def CreateDocumentPackageTargetForPrintJob(self, printerName: win32more.Windows.Win32.Foundation.PWSTR, jobName: win32more.Windows.Win32.Foundation.PWSTR, jobOutputStream: win32more.Windows.Win32.System.Com.IStream, jobPrintTicketStream: win32more.Windows.Win32.System.Com.IStream, docPackageTarget: POINTER(win32more.Windows.Win32.Storage.Xps.Printing.IPrintDocumentPackageTarget)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXpsPrintJob(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5ab89b06-8194-425f-ab3b-d7a96e350161}')
    @commethod(3)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetJobStatus(self, jobStatus: POINTER(win32more.Windows.Win32.Storage.Xps.Printing.XPS_JOB_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IXpsPrintJobStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.ISequentialStream
    _iid_ = Guid('{7a77dc5f-45d6-4dff-9307-d8cb846347ca}')
    @commethod(5)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PrintDocumentPackageCompletion = Int32
PrintDocumentPackageCompletion_InProgress: win32more.Windows.Win32.Storage.Xps.Printing.PrintDocumentPackageCompletion = 0
PrintDocumentPackageCompletion_Completed: win32more.Windows.Win32.Storage.Xps.Printing.PrintDocumentPackageCompletion = 1
PrintDocumentPackageCompletion_Canceled: win32more.Windows.Win32.Storage.Xps.Printing.PrintDocumentPackageCompletion = 2
PrintDocumentPackageCompletion_Failed: win32more.Windows.Win32.Storage.Xps.Printing.PrintDocumentPackageCompletion = 3
class PrintDocumentPackageStatus(Structure):
    JobId: UInt32
    CurrentDocument: Int32
    CurrentPage: Int32
    CurrentPageTotal: Int32
    Completion: win32more.Windows.Win32.Storage.Xps.Printing.PrintDocumentPackageCompletion
    PackageStatus: win32more.Windows.Win32.Foundation.HRESULT
PrintDocumentPackageTarget = Guid('{4842669e-9947-46ea-8ba2-d8cce432c2ca}')
PrintDocumentPackageTargetFactory = Guid('{348ef17d-6c81-4982-92b4-ee188a43867a}')
XPS_JOB_COMPLETION = Int32
XPS_JOB_IN_PROGRESS: win32more.Windows.Win32.Storage.Xps.Printing.XPS_JOB_COMPLETION = 0
XPS_JOB_COMPLETED: win32more.Windows.Win32.Storage.Xps.Printing.XPS_JOB_COMPLETION = 1
XPS_JOB_CANCELLED: win32more.Windows.Win32.Storage.Xps.Printing.XPS_JOB_COMPLETION = 2
XPS_JOB_FAILED: win32more.Windows.Win32.Storage.Xps.Printing.XPS_JOB_COMPLETION = 3
class XPS_JOB_STATUS(Structure):
    jobId: UInt32
    currentDocument: Int32
    currentPage: Int32
    currentPageTotal: Int32
    completion: win32more.Windows.Win32.Storage.Xps.Printing.XPS_JOB_COMPLETION
    jobStatus: win32more.Windows.Win32.Foundation.HRESULT


make_ready(__name__)
