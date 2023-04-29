from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Storage.Xps
import Windows.Win32.Storage.Xps.Printing
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ID_DOCUMENTPACKAGETARGET_MSXPS: Guid = Guid('9cae40a8-ded1-41c9-a9-fd-d7-35-ef-33-ae-da')
ID_DOCUMENTPACKAGETARGET_OPENXPS: Guid = Guid('0056bb72-8c9c-4612-bd-0f-93-01-2a-87-09-9d')
ID_DOCUMENTPACKAGETARGET_OPENXPS_WITH_3D: Guid = Guid('63dbd720-8b14-4577-b0-74-7b-b1-1b-59-6d-28')
@winfunctype('XPSPRINT.dll')
def StartXpsPrintJob(printerName: Windows.Win32.Foundation.PWSTR, jobName: Windows.Win32.Foundation.PWSTR, outputFileName: Windows.Win32.Foundation.PWSTR, progressEvent: Windows.Win32.Foundation.HANDLE, completionEvent: Windows.Win32.Foundation.HANDLE, printablePagesOn: POINTER(Byte), printablePagesOnCount: UInt32, xpsPrintJob: POINTER(Windows.Win32.Storage.Xps.Printing.IXpsPrintJob_head), documentStream: POINTER(Windows.Win32.Storage.Xps.Printing.IXpsPrintJobStream_head), printTicketStream: POINTER(Windows.Win32.Storage.Xps.Printing.IXpsPrintJobStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('XPSPRINT.dll')
def StartXpsPrintJob1(printerName: Windows.Win32.Foundation.PWSTR, jobName: Windows.Win32.Foundation.PWSTR, outputFileName: Windows.Win32.Foundation.PWSTR, progressEvent: Windows.Win32.Foundation.HANDLE, completionEvent: Windows.Win32.Foundation.HANDLE, xpsPrintJob: POINTER(Windows.Win32.Storage.Xps.Printing.IXpsPrintJob_head), printContentReceiver: POINTER(Windows.Win32.Storage.Xps.IXpsOMPackageTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintDocumentPackageStatusEvent(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('ed90c8ad-5c34-4d05-a1-ec-0e-8a-9b-3a-d7-af')
    @commethod(7)
    def PackageStatusUpdated(self, packageStatus: POINTER(Windows.Win32.Storage.Xps.Printing.PrintDocumentPackageStatus_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintDocumentPackageTarget(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('1b8efec4-3019-4c27-96-4e-36-72-02-15-69-06')
    @commethod(3)
    def GetPackageTargetTypes(self, targetCount: POINTER(UInt32), targetTypes: POINTER(POINTER(Guid))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPackageTarget(self, guidTargetType: POINTER(Guid), riid: POINTER(Guid), ppvTarget: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintDocumentPackageTarget2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('c560298a-535c-48f9-86-6a-63-25-40-66-0c-b4')
    @commethod(3)
    def GetIsTargetIppPrinter(self, isIppPrinter: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTargetIppPrintDevice(self, riid: POINTER(Guid), ppvTarget: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintDocumentPackageTargetFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('d2959bf7-b31b-4a3d-96-00-71-2e-b1-33-5b-a4')
    @commethod(3)
    def CreateDocumentPackageTargetForPrintJob(self, printerName: Windows.Win32.Foundation.PWSTR, jobName: Windows.Win32.Foundation.PWSTR, jobOutputStream: Windows.Win32.System.Com.IStream_head, jobPrintTicketStream: Windows.Win32.System.Com.IStream_head, docPackageTarget: POINTER(Windows.Win32.Storage.Xps.Printing.IPrintDocumentPackageTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsPrintJob(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('5ab89b06-8194-425f-ab-3b-d7-a9-6e-35-01-61')
    @commethod(3)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetJobStatus(self, jobStatus: POINTER(Windows.Win32.Storage.Xps.Printing.XPS_JOB_STATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IXpsPrintJobStream(ComPtr):
    extends: Windows.Win32.System.Com.ISequentialStream
    _iid_ = Guid('7a77dc5f-45d6-4dff-93-07-d8-cb-84-63-47-ca')
    @commethod(5)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
PrintDocumentPackageCompletion = Int32
PrintDocumentPackageCompletion_InProgress: PrintDocumentPackageCompletion = 0
PrintDocumentPackageCompletion_Completed: PrintDocumentPackageCompletion = 1
PrintDocumentPackageCompletion_Canceled: PrintDocumentPackageCompletion = 2
PrintDocumentPackageCompletion_Failed: PrintDocumentPackageCompletion = 3
class PrintDocumentPackageStatus(EasyCastStructure):
    JobId: UInt32
    CurrentDocument: Int32
    CurrentPage: Int32
    CurrentPageTotal: Int32
    Completion: Windows.Win32.Storage.Xps.Printing.PrintDocumentPackageCompletion
    PackageStatus: Windows.Win32.Foundation.HRESULT
PrintDocumentPackageTarget = Guid('4842669e-9947-46ea-8b-a2-d8-cc-e4-32-c2-ca')
PrintDocumentPackageTargetFactory = Guid('348ef17d-6c81-4982-92-b4-ee-18-8a-43-86-7a')
XPS_JOB_COMPLETION = Int32
XPS_JOB_IN_PROGRESS: XPS_JOB_COMPLETION = 0
XPS_JOB_COMPLETED: XPS_JOB_COMPLETION = 1
XPS_JOB_CANCELLED: XPS_JOB_COMPLETION = 2
XPS_JOB_FAILED: XPS_JOB_COMPLETION = 3
class XPS_JOB_STATUS(EasyCastStructure):
    jobId: UInt32
    currentDocument: Int32
    currentPage: Int32
    currentPageTotal: Int32
    completion: Windows.Win32.Storage.Xps.Printing.XPS_JOB_COMPLETION
    jobStatus: Windows.Win32.Foundation.HRESULT
make_head(_module, 'IPrintDocumentPackageStatusEvent')
make_head(_module, 'IPrintDocumentPackageTarget')
make_head(_module, 'IPrintDocumentPackageTarget2')
make_head(_module, 'IPrintDocumentPackageTargetFactory')
make_head(_module, 'IXpsPrintJob')
make_head(_module, 'IXpsPrintJobStream')
make_head(_module, 'PrintDocumentPackageStatus')
make_head(_module, 'XPS_JOB_STATUS')
