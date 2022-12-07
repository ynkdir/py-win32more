from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Storage.Xps
import win32more.Storage.Xps.Printing
import win32more.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
ID_DOCUMENTPACKAGETARGET_MSXPS: Guid = Guid('9cae40a8-ded1-41c9-a9-fd-d7-35-ef-33-ae-da')
ID_DOCUMENTPACKAGETARGET_OPENXPS: Guid = Guid('0056bb72-8c9c-4612-bd-0f-93-01-2a-87-09-9d')
ID_DOCUMENTPACKAGETARGET_OPENXPS_WITH_3D: Guid = Guid('63dbd720-8b14-4577-b0-74-7b-b1-1b-59-6d-28')
@winfunctype('XPSPRINT.dll')
def StartXpsPrintJob(printerName: win32more.Foundation.PWSTR, jobName: win32more.Foundation.PWSTR, outputFileName: win32more.Foundation.PWSTR, progressEvent: win32more.Foundation.HANDLE, completionEvent: win32more.Foundation.HANDLE, printablePagesOn: c_char_p_no, printablePagesOnCount: UInt32, xpsPrintJob: POINTER(win32more.Storage.Xps.Printing.IXpsPrintJob_head), documentStream: POINTER(win32more.Storage.Xps.Printing.IXpsPrintJobStream_head), printTicketStream: POINTER(win32more.Storage.Xps.Printing.IXpsPrintJobStream_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('XPSPRINT.dll')
def StartXpsPrintJob1(printerName: win32more.Foundation.PWSTR, jobName: win32more.Foundation.PWSTR, outputFileName: win32more.Foundation.PWSTR, progressEvent: win32more.Foundation.HANDLE, completionEvent: win32more.Foundation.HANDLE, xpsPrintJob: POINTER(win32more.Storage.Xps.Printing.IXpsPrintJob_head), printContentReceiver: POINTER(win32more.Storage.Xps.IXpsOMPackageTarget_head)) -> win32more.Foundation.HRESULT: ...
class IPrintDocumentPackageStatusEvent(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('ed90c8ad-5c34-4d05-a1-ec-0e-8a-9b-3a-d7-af')
    @commethod(7)
    def PackageStatusUpdated(packageStatus: POINTER(win32more.Storage.Xps.Printing.PrintDocumentPackageStatus_head)) -> win32more.Foundation.HRESULT: ...
class IPrintDocumentPackageTarget(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1b8efec4-3019-4c27-96-4e-36-72-02-15-69-06')
    @commethod(3)
    def GetPackageTargetTypes(targetCount: POINTER(UInt32), targetTypes: POINTER(POINTER(Guid))) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPackageTarget(guidTargetType: POINTER(Guid), riid: POINTER(Guid), ppvTarget: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Cancel() -> win32more.Foundation.HRESULT: ...
class IPrintDocumentPackageTargetFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d2959bf7-b31b-4a3d-96-00-71-2e-b1-33-5b-a4')
    @commethod(3)
    def CreateDocumentPackageTargetForPrintJob(printerName: win32more.Foundation.PWSTR, jobName: win32more.Foundation.PWSTR, jobOutputStream: win32more.System.Com.IStream_head, jobPrintTicketStream: win32more.System.Com.IStream_head, docPackageTarget: POINTER(win32more.Storage.Xps.Printing.IPrintDocumentPackageTarget_head)) -> win32more.Foundation.HRESULT: ...
class IXpsPrintJob(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5ab89b06-8194-425f-ab-3b-d7-a9-6e-35-01-61')
    @commethod(3)
    def Cancel() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetJobStatus(jobStatus: POINTER(win32more.Storage.Xps.Printing.XPS_JOB_STATUS_head)) -> win32more.Foundation.HRESULT: ...
class IXpsPrintJobStream(c_void_p):
    extends: win32more.System.Com.ISequentialStream
    Guid = Guid('7a77dc5f-45d6-4dff-93-07-d8-cb-84-63-47-ca')
    @commethod(5)
    def Close() -> win32more.Foundation.HRESULT: ...
PrintDocumentPackageCompletion = Int32
PrintDocumentPackageCompletion_InProgress: PrintDocumentPackageCompletion = 0
PrintDocumentPackageCompletion_Completed: PrintDocumentPackageCompletion = 1
PrintDocumentPackageCompletion_Canceled: PrintDocumentPackageCompletion = 2
PrintDocumentPackageCompletion_Failed: PrintDocumentPackageCompletion = 3
class PrintDocumentPackageStatus(Structure):
    JobId: UInt32
    CurrentDocument: Int32
    CurrentPage: Int32
    CurrentPageTotal: Int32
    Completion: win32more.Storage.Xps.Printing.PrintDocumentPackageCompletion
    PackageStatus: win32more.Foundation.HRESULT
PrintDocumentPackageTarget = Guid('4842669e-9947-46ea-8b-a2-d8-cc-e4-32-c2-ca')
PrintDocumentPackageTargetFactory = Guid('348ef17d-6c81-4982-92-b4-ee-18-8a-43-86-7a')
XPS_JOB_COMPLETION = Int32
XPS_JOB_IN_PROGRESS: XPS_JOB_COMPLETION = 0
XPS_JOB_COMPLETED: XPS_JOB_COMPLETION = 1
XPS_JOB_CANCELLED: XPS_JOB_COMPLETION = 2
XPS_JOB_FAILED: XPS_JOB_COMPLETION = 3
class XPS_JOB_STATUS(Structure):
    jobId: UInt32
    currentDocument: Int32
    currentPage: Int32
    currentPageTotal: Int32
    completion: win32more.Storage.Xps.Printing.XPS_JOB_COMPLETION
    jobStatus: win32more.Foundation.HRESULT
make_head(_module, 'IPrintDocumentPackageStatusEvent')
make_head(_module, 'IPrintDocumentPackageTarget')
make_head(_module, 'IPrintDocumentPackageTargetFactory')
make_head(_module, 'IXpsPrintJob')
make_head(_module, 'IXpsPrintJobStream')
make_head(_module, 'PrintDocumentPackageStatus')
make_head(_module, 'XPS_JOB_STATUS')
__all__ = [
    "ID_DOCUMENTPACKAGETARGET_MSXPS",
    "ID_DOCUMENTPACKAGETARGET_OPENXPS",
    "ID_DOCUMENTPACKAGETARGET_OPENXPS_WITH_3D",
    "IPrintDocumentPackageStatusEvent",
    "IPrintDocumentPackageTarget",
    "IPrintDocumentPackageTargetFactory",
    "IXpsPrintJob",
    "IXpsPrintJobStream",
    "PrintDocumentPackageCompletion",
    "PrintDocumentPackageCompletion_Canceled",
    "PrintDocumentPackageCompletion_Completed",
    "PrintDocumentPackageCompletion_Failed",
    "PrintDocumentPackageCompletion_InProgress",
    "PrintDocumentPackageStatus",
    "PrintDocumentPackageTarget",
    "PrintDocumentPackageTargetFactory",
    "StartXpsPrintJob",
    "StartXpsPrintJob1",
    "XPS_JOB_CANCELLED",
    "XPS_JOB_COMPLETED",
    "XPS_JOB_COMPLETION",
    "XPS_JOB_FAILED",
    "XPS_JOB_IN_PROGRESS",
    "XPS_JOB_STATUS",
]
