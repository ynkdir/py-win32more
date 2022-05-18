from win32more import *
import win32more.Foundation
import win32more.Storage.Xps
import win32more.Storage.Xps.Printing
import win32more.System.Com

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
ID_DOCUMENTPACKAGETARGET_MSXPS = '9cae40a8-ded1-41c9-a9fd-d735ef33aeda'
ID_DOCUMENTPACKAGETARGET_OPENXPS = '0056bb72-8c9c-4612-bd0f-93012a87099d'
ID_DOCUMENTPACKAGETARGET_OPENXPS_WITH_3D = '63dbd720-8b14-4577-b074-7bb11b596d28'
XPS_JOB_COMPLETION = Int32
XPS_JOB_IN_PROGRESS = 0
XPS_JOB_COMPLETED = 1
XPS_JOB_CANCELLED = 2
XPS_JOB_FAILED = 3
def _define_XPS_JOB_STATUS_head():
    class XPS_JOB_STATUS(Structure):
        pass
    return XPS_JOB_STATUS
def _define_XPS_JOB_STATUS():
    XPS_JOB_STATUS = win32more.Storage.Xps.Printing.XPS_JOB_STATUS_head
    XPS_JOB_STATUS._fields_ = [
        ("jobId", UInt32),
        ("currentDocument", Int32),
        ("currentPage", Int32),
        ("currentPageTotal", Int32),
        ("completion", win32more.Storage.Xps.Printing.XPS_JOB_COMPLETION),
        ("jobStatus", win32more.Foundation.HRESULT),
    ]
    return XPS_JOB_STATUS
def _define_IXpsPrintJobStream_head():
    class IXpsPrintJobStream(win32more.System.Com.ISequentialStream_head):
        Guid = Guid('7a77dc5f-45d6-4dff-9307-d8cb846347ca')
    return IXpsPrintJobStream
def _define_IXpsPrintJobStream():
    IXpsPrintJobStream = win32more.Storage.Xps.Printing.IXpsPrintJobStream_head
    IXpsPrintJobStream.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Close', ()))
    return IXpsPrintJobStream
def _define_IXpsPrintJob_head():
    class IXpsPrintJob(win32more.System.Com.IUnknown_head):
        Guid = Guid('5ab89b06-8194-425f-ab3b-d7a96e350161')
    return IXpsPrintJob
def _define_IXpsPrintJob():
    IXpsPrintJob = win32more.Storage.Xps.Printing.IXpsPrintJob_head
    IXpsPrintJob.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Cancel', ()))
    IXpsPrintJob.GetJobStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.Printing.XPS_JOB_STATUS_head), use_last_error=False)(4, 'GetJobStatus', ((1, 'jobStatus'),)))
    return IXpsPrintJob
PrintDocumentPackageTarget = Guid('4842669e-9947-46ea-8ba2-d8cce432c2ca')
PrintDocumentPackageTargetFactory = Guid('348ef17d-6c81-4982-92b4-ee188a43867a')
def _define_IPrintDocumentPackageTarget_head():
    class IPrintDocumentPackageTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('1b8efec4-3019-4c27-964e-367202156906')
    return IPrintDocumentPackageTarget
def _define_IPrintDocumentPackageTarget():
    IPrintDocumentPackageTarget = win32more.Storage.Xps.Printing.IPrintDocumentPackageTarget_head
    IPrintDocumentPackageTarget.GetPackageTargetTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(Guid)), use_last_error=False)(3, 'GetPackageTargetTypes', ((1, 'targetCount'),(1, 'targetTypes'),)))
    IPrintDocumentPackageTarget.GetPackageTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'GetPackageTarget', ((1, 'guidTargetType'),(1, 'riid'),(1, 'ppvTarget'),)))
    IPrintDocumentPackageTarget.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Cancel', ()))
    return IPrintDocumentPackageTarget
PrintDocumentPackageCompletion = Int32
PrintDocumentPackageCompletion_InProgress = 0
PrintDocumentPackageCompletion_Completed = 1
PrintDocumentPackageCompletion_Canceled = 2
PrintDocumentPackageCompletion_Failed = 3
def _define_PrintDocumentPackageStatus_head():
    class PrintDocumentPackageStatus(Structure):
        pass
    return PrintDocumentPackageStatus
def _define_PrintDocumentPackageStatus():
    PrintDocumentPackageStatus = win32more.Storage.Xps.Printing.PrintDocumentPackageStatus_head
    PrintDocumentPackageStatus._fields_ = [
        ("JobId", UInt32),
        ("CurrentDocument", Int32),
        ("CurrentPage", Int32),
        ("CurrentPageTotal", Int32),
        ("Completion", win32more.Storage.Xps.Printing.PrintDocumentPackageCompletion),
        ("PackageStatus", win32more.Foundation.HRESULT),
    ]
    return PrintDocumentPackageStatus
def _define_IPrintDocumentPackageStatusEvent_head():
    class IPrintDocumentPackageStatusEvent(win32more.System.Com.IDispatch_head):
        Guid = Guid('ed90c8ad-5c34-4d05-a1ec-0e8a9b3ad7af')
    return IPrintDocumentPackageStatusEvent
def _define_IPrintDocumentPackageStatusEvent():
    IPrintDocumentPackageStatusEvent = win32more.Storage.Xps.Printing.IPrintDocumentPackageStatusEvent_head
    IPrintDocumentPackageStatusEvent.PackageStatusUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.Printing.PrintDocumentPackageStatus_head), use_last_error=False)(7, 'PackageStatusUpdated', ((1, 'packageStatus'),)))
    return IPrintDocumentPackageStatusEvent
def _define_IPrintDocumentPackageTargetFactory_head():
    class IPrintDocumentPackageTargetFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('d2959bf7-b31b-4a3d-9600-712eb1335ba4')
    return IPrintDocumentPackageTargetFactory
def _define_IPrintDocumentPackageTargetFactory():
    IPrintDocumentPackageTargetFactory = win32more.Storage.Xps.Printing.IPrintDocumentPackageTargetFactory_head
    IPrintDocumentPackageTargetFactory.CreateDocumentPackageTargetForPrintJob = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.Com.IStream_head,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Xps.Printing.IPrintDocumentPackageTarget_head), use_last_error=False)(3, 'CreateDocumentPackageTargetForPrintJob', ((1, 'printerName'),(1, 'jobName'),(1, 'jobOutputStream'),(1, 'jobPrintTicketStream'),(1, 'docPackageTarget'),)))
    return IPrintDocumentPackageTargetFactory
def _define_StartXpsPrintJob():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(Byte),UInt32,POINTER(win32more.Storage.Xps.Printing.IXpsPrintJob_head),POINTER(win32more.Storage.Xps.Printing.IXpsPrintJobStream_head),POINTER(win32more.Storage.Xps.Printing.IXpsPrintJobStream_head), use_last_error=False)(("StartXpsPrintJob", windll["XPSPRINT"]), ((1, 'printerName'),(1, 'jobName'),(1, 'outputFileName'),(1, 'progressEvent'),(1, 'completionEvent'),(1, 'printablePagesOn'),(1, 'printablePagesOnCount'),(1, 'xpsPrintJob'),(1, 'documentStream'),(1, 'printTicketStream'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StartXpsPrintJob1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Storage.Xps.Printing.IXpsPrintJob_head),POINTER(win32more.Storage.Xps.IXpsOMPackageTarget_head), use_last_error=False)(("StartXpsPrintJob1", windll["XPSPRINT"]), ((1, 'printerName'),(1, 'jobName'),(1, 'outputFileName'),(1, 'progressEvent'),(1, 'completionEvent'),(1, 'xpsPrintJob'),(1, 'printContentReceiver'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "ID_DOCUMENTPACKAGETARGET_MSXPS",
    "ID_DOCUMENTPACKAGETARGET_OPENXPS",
    "ID_DOCUMENTPACKAGETARGET_OPENXPS_WITH_3D",
    "XPS_JOB_COMPLETION",
    "XPS_JOB_IN_PROGRESS",
    "XPS_JOB_COMPLETED",
    "XPS_JOB_CANCELLED",
    "XPS_JOB_FAILED",
    "XPS_JOB_STATUS",
    "IXpsPrintJobStream",
    "IXpsPrintJob",
    "PrintDocumentPackageTarget",
    "PrintDocumentPackageTargetFactory",
    "IPrintDocumentPackageTarget",
    "PrintDocumentPackageCompletion",
    "PrintDocumentPackageCompletion_InProgress",
    "PrintDocumentPackageCompletion_Completed",
    "PrintDocumentPackageCompletion_Canceled",
    "PrintDocumentPackageCompletion_Failed",
    "PrintDocumentPackageStatus",
    "IPrintDocumentPackageStatusEvent",
    "IPrintDocumentPackageTargetFactory",
    "StartXpsPrintJob",
    "StartXpsPrintJob1",
]
