from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Diagnostics.Debug
import win32more.System.ErrorReporting

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
WER_FAULT_REPORTING_NO_UI = 32
WER_FAULT_REPORTING_FLAG_NO_HEAP_ON_QUEUE = 64
WER_FAULT_REPORTING_DISABLE_SNAPSHOT_CRASH = 128
WER_FAULT_REPORTING_DISABLE_SNAPSHOT_HANG = 256
WER_FAULT_REPORTING_CRITICAL = 512
WER_FAULT_REPORTING_DURABLE = 1024
WER_MAX_TOTAL_PARAM_LENGTH = 1720
WER_MAX_PREFERRED_MODULES = 128
WER_MAX_PREFERRED_MODULES_BUFFER = 256
WER_P0 = 0
WER_P1 = 1
WER_P2 = 2
WER_P3 = 3
WER_P4 = 4
WER_P5 = 5
WER_P6 = 6
WER_P7 = 7
WER_P8 = 8
WER_P9 = 9
WER_FILE_COMPRESSED = 4
WER_SUBMIT_BYPASS_POWER_THROTTLING = 16384
WER_SUBMIT_BYPASS_NETWORK_COST_THROTTLING = 32768
WER_DUMP_MASK_START = 1
WER_DUMP_NOHEAP_ONQUEUE = 1
WER_DUMP_AUXILIARY = 2
WER_MAX_REGISTERED_ENTRIES = 512
WER_MAX_REGISTERED_METADATA = 8
WER_MAX_REGISTERED_DUMPCOLLECTION = 4
WER_METADATA_KEY_MAX_LENGTH = 64
WER_METADATA_VALUE_MAX_LENGTH = 128
WER_MAX_SIGNATURE_NAME_LENGTH = 128
WER_MAX_EVENT_NAME_LENGTH = 64
WER_MAX_PARAM_LENGTH = 260
WER_MAX_PARAM_COUNT = 10
WER_MAX_FRIENDLY_EVENT_NAME_LENGTH = 128
WER_MAX_APPLICATION_NAME_LENGTH = 128
WER_MAX_DESCRIPTION_LENGTH = 512
WER_MAX_BUCKET_ID_STRING_LENGTH = 260
WER_MAX_LOCAL_DUMP_SUBPATH_LENGTH = 64
WER_MAX_REGISTERED_RUNTIME_EXCEPTION_MODULES = 16
WER_FILE = UInt32
WER_FILE_ANONYMOUS_DATA = 2
WER_FILE_DELETE_WHEN_DONE = 1
WER_SUBMIT_FLAGS = UInt32
WER_SUBMIT_ADD_REGISTERED_DATA = 16
WER_SUBMIT_HONOR_RECOVERY = 1
WER_SUBMIT_HONOR_RESTART = 2
WER_SUBMIT_NO_ARCHIVE = 256
WER_SUBMIT_NO_CLOSE_UI = 64
WER_SUBMIT_NO_QUEUE = 128
WER_SUBMIT_OUTOFPROCESS = 32
WER_SUBMIT_OUTOFPROCESS_ASYNC = 1024
WER_SUBMIT_QUEUE = 4
WER_SUBMIT_SHOW_DEBUG = 8
WER_SUBMIT_START_MINIMIZED = 512
WER_SUBMIT_BYPASS_DATA_THROTTLING = 2048
WER_SUBMIT_ARCHIVE_PARAMETERS_ONLY = 4096
WER_SUBMIT_REPORT_MACHINE_ID = 8192
WER_FAULT_REPORTING = UInt32
WER_FAULT_REPORTING_FLAG_DISABLE_THREAD_SUSPENSION = 4
WER_FAULT_REPORTING_FLAG_NOHEAP = 1
WER_FAULT_REPORTING_FLAG_QUEUE = 2
WER_FAULT_REPORTING_FLAG_QUEUE_UPLOAD = 8
WER_FAULT_REPORTING_ALWAYS_SHOW_UI = 16
HREPORT = IntPtr
HREPORTSTORE = IntPtr
WER_REPORT_UI = Int32
WER_REPORT_UI_WerUIAdditionalDataDlgHeader = 1
WER_REPORT_UI_WerUIIconFilePath = 2
WER_REPORT_UI_WerUIConsentDlgHeader = 3
WER_REPORT_UI_WerUIConsentDlgBody = 4
WER_REPORT_UI_WerUIOnlineSolutionCheckText = 5
WER_REPORT_UI_WerUIOfflineSolutionCheckText = 6
WER_REPORT_UI_WerUICloseText = 7
WER_REPORT_UI_WerUICloseDlgHeader = 8
WER_REPORT_UI_WerUICloseDlgBody = 9
WER_REPORT_UI_WerUICloseDlgButtonText = 10
WER_REPORT_UI_WerUIMax = 11
WER_REGISTER_FILE_TYPE = Int32
WER_REGISTER_FILE_TYPE_WerRegFileTypeUserDocument = 1
WER_REGISTER_FILE_TYPE_WerRegFileTypeOther = 2
WER_REGISTER_FILE_TYPE_WerRegFileTypeMax = 3
WER_FILE_TYPE = Int32
WER_FILE_TYPE_WerFileTypeMicrodump = 1
WER_FILE_TYPE_WerFileTypeMinidump = 2
WER_FILE_TYPE_WerFileTypeHeapdump = 3
WER_FILE_TYPE_WerFileTypeUserDocument = 4
WER_FILE_TYPE_WerFileTypeOther = 5
WER_FILE_TYPE_WerFileTypeTriagedump = 6
WER_FILE_TYPE_WerFileTypeCustomDump = 7
WER_FILE_TYPE_WerFileTypeAuxiliaryDump = 8
WER_FILE_TYPE_WerFileTypeEtlTrace = 9
WER_FILE_TYPE_WerFileTypeMax = 10
WER_SUBMIT_RESULT = Int32
WER_SUBMIT_RESULT_WerReportQueued = 1
WER_SUBMIT_RESULT_WerReportUploaded = 2
WER_SUBMIT_RESULT_WerReportDebug = 3
WER_SUBMIT_RESULT_WerReportFailed = 4
WER_SUBMIT_RESULT_WerDisabled = 5
WER_SUBMIT_RESULT_WerReportCancelled = 6
WER_SUBMIT_RESULT_WerDisabledQueue = 7
WER_SUBMIT_RESULT_WerReportAsync = 8
WER_SUBMIT_RESULT_WerCustomAction = 9
WER_SUBMIT_RESULT_WerThrottled = 10
WER_SUBMIT_RESULT_WerReportUploadedCab = 11
WER_SUBMIT_RESULT_WerStorageLocationNotFound = 12
WER_SUBMIT_RESULT_WerSubmitResultMax = 13
WER_REPORT_TYPE = Int32
WER_REPORT_TYPE_WerReportNonCritical = 0
WER_REPORT_TYPE_WerReportCritical = 1
WER_REPORT_TYPE_WerReportApplicationCrash = 2
WER_REPORT_TYPE_WerReportApplicationHang = 3
WER_REPORT_TYPE_WerReportKernel = 4
WER_REPORT_TYPE_WerReportInvalid = 5
def _define_WER_REPORT_INFORMATION_head():
    class WER_REPORT_INFORMATION(Structure):
        pass
    return WER_REPORT_INFORMATION
def _define_WER_REPORT_INFORMATION():
    WER_REPORT_INFORMATION = win32more.System.ErrorReporting.WER_REPORT_INFORMATION_head
    WER_REPORT_INFORMATION._fields_ = [
        ("dwSize", UInt32),
        ("hProcess", win32more.Foundation.HANDLE),
        ("wzConsentKey", Char * 64),
        ("wzFriendlyEventName", Char * 128),
        ("wzApplicationName", Char * 128),
        ("wzApplicationPath", Char * 260),
        ("wzDescription", Char * 512),
        ("hwndParent", win32more.Foundation.HWND),
    ]
    return WER_REPORT_INFORMATION
def _define_WER_REPORT_INFORMATION_V3_head():
    class WER_REPORT_INFORMATION_V3(Structure):
        pass
    return WER_REPORT_INFORMATION_V3
def _define_WER_REPORT_INFORMATION_V3():
    WER_REPORT_INFORMATION_V3 = win32more.System.ErrorReporting.WER_REPORT_INFORMATION_V3_head
    WER_REPORT_INFORMATION_V3._fields_ = [
        ("dwSize", UInt32),
        ("hProcess", win32more.Foundation.HANDLE),
        ("wzConsentKey", Char * 64),
        ("wzFriendlyEventName", Char * 128),
        ("wzApplicationName", Char * 128),
        ("wzApplicationPath", Char * 260),
        ("wzDescription", Char * 512),
        ("hwndParent", win32more.Foundation.HWND),
        ("wzNamespacePartner", Char * 64),
        ("wzNamespaceGroup", Char * 64),
    ]
    return WER_REPORT_INFORMATION_V3
def _define_WER_DUMP_CUSTOM_OPTIONS_head():
    class WER_DUMP_CUSTOM_OPTIONS(Structure):
        pass
    return WER_DUMP_CUSTOM_OPTIONS
def _define_WER_DUMP_CUSTOM_OPTIONS():
    WER_DUMP_CUSTOM_OPTIONS = win32more.System.ErrorReporting.WER_DUMP_CUSTOM_OPTIONS_head
    WER_DUMP_CUSTOM_OPTIONS._fields_ = [
        ("dwSize", UInt32),
        ("dwMask", UInt32),
        ("dwDumpFlags", UInt32),
        ("bOnlyThisThread", win32more.Foundation.BOOL),
        ("dwExceptionThreadFlags", UInt32),
        ("dwOtherThreadFlags", UInt32),
        ("dwExceptionThreadExFlags", UInt32),
        ("dwOtherThreadExFlags", UInt32),
        ("dwPreferredModuleFlags", UInt32),
        ("dwOtherModuleFlags", UInt32),
        ("wzPreferredModuleList", Char * 256),
    ]
    return WER_DUMP_CUSTOM_OPTIONS
def _define_WER_DUMP_CUSTOM_OPTIONS_V2_head():
    class WER_DUMP_CUSTOM_OPTIONS_V2(Structure):
        pass
    return WER_DUMP_CUSTOM_OPTIONS_V2
def _define_WER_DUMP_CUSTOM_OPTIONS_V2():
    WER_DUMP_CUSTOM_OPTIONS_V2 = win32more.System.ErrorReporting.WER_DUMP_CUSTOM_OPTIONS_V2_head
    WER_DUMP_CUSTOM_OPTIONS_V2._fields_ = [
        ("dwSize", UInt32),
        ("dwMask", UInt32),
        ("dwDumpFlags", UInt32),
        ("bOnlyThisThread", win32more.Foundation.BOOL),
        ("dwExceptionThreadFlags", UInt32),
        ("dwOtherThreadFlags", UInt32),
        ("dwExceptionThreadExFlags", UInt32),
        ("dwOtherThreadExFlags", UInt32),
        ("dwPreferredModuleFlags", UInt32),
        ("dwOtherModuleFlags", UInt32),
        ("wzPreferredModuleList", Char * 256),
        ("dwPreferredModuleResetFlags", UInt32),
        ("dwOtherModuleResetFlags", UInt32),
    ]
    return WER_DUMP_CUSTOM_OPTIONS_V2
def _define_WER_REPORT_INFORMATION_V4_head():
    class WER_REPORT_INFORMATION_V4(Structure):
        pass
    return WER_REPORT_INFORMATION_V4
def _define_WER_REPORT_INFORMATION_V4():
    WER_REPORT_INFORMATION_V4 = win32more.System.ErrorReporting.WER_REPORT_INFORMATION_V4_head
    WER_REPORT_INFORMATION_V4._fields_ = [
        ("dwSize", UInt32),
        ("hProcess", win32more.Foundation.HANDLE),
        ("wzConsentKey", Char * 64),
        ("wzFriendlyEventName", Char * 128),
        ("wzApplicationName", Char * 128),
        ("wzApplicationPath", Char * 260),
        ("wzDescription", Char * 512),
        ("hwndParent", win32more.Foundation.HWND),
        ("wzNamespacePartner", Char * 64),
        ("wzNamespaceGroup", Char * 64),
        ("rgbApplicationIdentity", Byte * 16),
        ("hSnapshot", win32more.Foundation.HANDLE),
        ("hDeleteFilesImpersonationToken", win32more.Foundation.HANDLE),
    ]
    return WER_REPORT_INFORMATION_V4
def _define_WER_REPORT_INFORMATION_V5_head():
    class WER_REPORT_INFORMATION_V5(Structure):
        pass
    return WER_REPORT_INFORMATION_V5
def _define_WER_REPORT_INFORMATION_V5():
    WER_REPORT_INFORMATION_V5 = win32more.System.ErrorReporting.WER_REPORT_INFORMATION_V5_head
    WER_REPORT_INFORMATION_V5._fields_ = [
        ("dwSize", UInt32),
        ("hProcess", win32more.Foundation.HANDLE),
        ("wzConsentKey", Char * 64),
        ("wzFriendlyEventName", Char * 128),
        ("wzApplicationName", Char * 128),
        ("wzApplicationPath", Char * 260),
        ("wzDescription", Char * 512),
        ("hwndParent", win32more.Foundation.HWND),
        ("wzNamespacePartner", Char * 64),
        ("wzNamespaceGroup", Char * 64),
        ("rgbApplicationIdentity", Byte * 16),
        ("hSnapshot", win32more.Foundation.HANDLE),
        ("hDeleteFilesImpersonationToken", win32more.Foundation.HANDLE),
        ("submitResultMax", win32more.System.ErrorReporting.WER_SUBMIT_RESULT),
    ]
    return WER_REPORT_INFORMATION_V5
def _define_WER_DUMP_CUSTOM_OPTIONS_V3_head():
    class WER_DUMP_CUSTOM_OPTIONS_V3(Structure):
        pass
    return WER_DUMP_CUSTOM_OPTIONS_V3
def _define_WER_DUMP_CUSTOM_OPTIONS_V3():
    WER_DUMP_CUSTOM_OPTIONS_V3 = win32more.System.ErrorReporting.WER_DUMP_CUSTOM_OPTIONS_V3_head
    WER_DUMP_CUSTOM_OPTIONS_V3._fields_ = [
        ("dwSize", UInt32),
        ("dwMask", UInt32),
        ("dwDumpFlags", UInt32),
        ("bOnlyThisThread", win32more.Foundation.BOOL),
        ("dwExceptionThreadFlags", UInt32),
        ("dwOtherThreadFlags", UInt32),
        ("dwExceptionThreadExFlags", UInt32),
        ("dwOtherThreadExFlags", UInt32),
        ("dwPreferredModuleFlags", UInt32),
        ("dwOtherModuleFlags", UInt32),
        ("wzPreferredModuleList", Char * 256),
        ("dwPreferredModuleResetFlags", UInt32),
        ("dwOtherModuleResetFlags", UInt32),
        ("pvDumpKey", c_void_p),
        ("hSnapshot", win32more.Foundation.HANDLE),
        ("dwThreadID", UInt32),
    ]
    return WER_DUMP_CUSTOM_OPTIONS_V3
def _define_WER_EXCEPTION_INFORMATION_head():
    class WER_EXCEPTION_INFORMATION(Structure):
        pass
    return WER_EXCEPTION_INFORMATION
def _define_WER_EXCEPTION_INFORMATION():
    WER_EXCEPTION_INFORMATION = win32more.System.ErrorReporting.WER_EXCEPTION_INFORMATION_head
    WER_EXCEPTION_INFORMATION._fields_ = [
        ("pExceptionPointers", POINTER(win32more.System.Diagnostics.Debug.EXCEPTION_POINTERS_head)),
        ("bClientPointers", win32more.Foundation.BOOL),
    ]
    return WER_EXCEPTION_INFORMATION
WER_CONSENT = Int32
WER_CONSENT_WerConsentNotAsked = 1
WER_CONSENT_WerConsentApproved = 2
WER_CONSENT_WerConsentDenied = 3
WER_CONSENT_WerConsentAlwaysPrompt = 4
WER_CONSENT_WerConsentMax = 5
WER_DUMP_TYPE = Int32
WER_DUMP_TYPE_WerDumpTypeNone = 0
WER_DUMP_TYPE_WerDumpTypeMicroDump = 1
WER_DUMP_TYPE_WerDumpTypeMiniDump = 2
WER_DUMP_TYPE_WerDumpTypeHeapDump = 3
WER_DUMP_TYPE_WerDumpTypeTriageDump = 4
WER_DUMP_TYPE_WerDumpTypeMax = 5
def _define_WER_RUNTIME_EXCEPTION_INFORMATION_head():
    class WER_RUNTIME_EXCEPTION_INFORMATION(Structure):
        pass
    return WER_RUNTIME_EXCEPTION_INFORMATION
def _define_WER_RUNTIME_EXCEPTION_INFORMATION():
    WER_RUNTIME_EXCEPTION_INFORMATION = win32more.System.ErrorReporting.WER_RUNTIME_EXCEPTION_INFORMATION_head
    WER_RUNTIME_EXCEPTION_INFORMATION._fields_ = [
        ("dwSize", UInt32),
        ("hProcess", win32more.Foundation.HANDLE),
        ("hThread", win32more.Foundation.HANDLE),
        ("exceptionRecord", win32more.System.Diagnostics.Debug.EXCEPTION_RECORD),
        ("context", win32more.System.Diagnostics.Debug.CONTEXT),
        ("pwszReportId", win32more.Foundation.PWSTR),
        ("bIsFatal", win32more.Foundation.BOOL),
        ("dwReserved", UInt32),
    ]
    return WER_RUNTIME_EXCEPTION_INFORMATION
def _define_PFN_WER_RUNTIME_EXCEPTION_EVENT():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.System.ErrorReporting.WER_RUNTIME_EXCEPTION_INFORMATION_head),POINTER(win32more.Foundation.BOOL),POINTER(Char),POINTER(UInt32),POINTER(UInt32), use_last_error=False)
def _define_PFN_WER_RUNTIME_EXCEPTION_EVENT_SIGNATURE():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.System.ErrorReporting.WER_RUNTIME_EXCEPTION_INFORMATION_head),UInt32,POINTER(Char),POINTER(UInt32),POINTER(Char),POINTER(UInt32), use_last_error=False)
def _define_PFN_WER_RUNTIME_EXCEPTION_DEBUGGER_LAUNCH():
    return CFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.System.ErrorReporting.WER_RUNTIME_EXCEPTION_INFORMATION_head),POINTER(win32more.Foundation.BOOL),POINTER(Char),POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=False)
REPORT_STORE_TYPES = Int32
E_STORE_USER_ARCHIVE = 0
E_STORE_USER_QUEUE = 1
E_STORE_MACHINE_ARCHIVE = 2
E_STORE_MACHINE_QUEUE = 3
E_STORE_INVALID = 4
def _define_WER_REPORT_PARAMETER_head():
    class WER_REPORT_PARAMETER(Structure):
        pass
    return WER_REPORT_PARAMETER
def _define_WER_REPORT_PARAMETER():
    WER_REPORT_PARAMETER = win32more.System.ErrorReporting.WER_REPORT_PARAMETER_head
    WER_REPORT_PARAMETER._fields_ = [
        ("Name", Char * 129),
        ("Value", Char * 260),
    ]
    return WER_REPORT_PARAMETER
def _define_WER_REPORT_SIGNATURE_head():
    class WER_REPORT_SIGNATURE(Structure):
        pass
    return WER_REPORT_SIGNATURE
def _define_WER_REPORT_SIGNATURE():
    WER_REPORT_SIGNATURE = win32more.System.ErrorReporting.WER_REPORT_SIGNATURE_head
    WER_REPORT_SIGNATURE._fields_ = [
        ("EventName", Char * 65),
        ("Parameters", win32more.System.ErrorReporting.WER_REPORT_PARAMETER * 10),
    ]
    return WER_REPORT_SIGNATURE
def _define_WER_REPORT_METADATA_V2_head():
    class WER_REPORT_METADATA_V2(Structure):
        pass
    return WER_REPORT_METADATA_V2
def _define_WER_REPORT_METADATA_V2():
    WER_REPORT_METADATA_V2 = win32more.System.ErrorReporting.WER_REPORT_METADATA_V2_head
    WER_REPORT_METADATA_V2._fields_ = [
        ("Signature", win32more.System.ErrorReporting.WER_REPORT_SIGNATURE),
        ("BucketId", Guid),
        ("ReportId", Guid),
        ("CreationTime", win32more.Foundation.FILETIME),
        ("SizeInBytes", UInt64),
        ("CabId", Char * 260),
        ("ReportStatus", UInt32),
        ("ReportIntegratorId", Guid),
        ("NumberOfFiles", UInt32),
        ("SizeOfFileNames", UInt32),
        ("FileNames", win32more.Foundation.PWSTR),
    ]
    return WER_REPORT_METADATA_V2
def _define_WER_REPORT_METADATA_V3_head():
    class WER_REPORT_METADATA_V3(Structure):
        pass
    return WER_REPORT_METADATA_V3
def _define_WER_REPORT_METADATA_V3():
    WER_REPORT_METADATA_V3 = win32more.System.ErrorReporting.WER_REPORT_METADATA_V3_head
    WER_REPORT_METADATA_V3._fields_ = [
        ("Signature", win32more.System.ErrorReporting.WER_REPORT_SIGNATURE),
        ("BucketId", Guid),
        ("ReportId", Guid),
        ("CreationTime", win32more.Foundation.FILETIME),
        ("SizeInBytes", UInt64),
        ("CabId", Char * 260),
        ("ReportStatus", UInt32),
        ("ReportIntegratorId", Guid),
        ("NumberOfFiles", UInt32),
        ("SizeOfFileNames", UInt32),
        ("FileNames", win32more.Foundation.PWSTR),
        ("FriendlyEventName", Char * 128),
        ("ApplicationName", Char * 128),
        ("ApplicationPath", Char * 260),
        ("Description", Char * 512),
        ("BucketIdString", Char * 260),
        ("LegacyBucketId", UInt64),
    ]
    return WER_REPORT_METADATA_V3
def _define_WER_REPORT_METADATA_V1_head():
    class WER_REPORT_METADATA_V1(Structure):
        pass
    return WER_REPORT_METADATA_V1
def _define_WER_REPORT_METADATA_V1():
    WER_REPORT_METADATA_V1 = win32more.System.ErrorReporting.WER_REPORT_METADATA_V1_head
    WER_REPORT_METADATA_V1._fields_ = [
        ("Signature", win32more.System.ErrorReporting.WER_REPORT_SIGNATURE),
        ("BucketId", Guid),
        ("ReportId", Guid),
        ("CreationTime", win32more.Foundation.FILETIME),
        ("SizeInBytes", UInt64),
    ]
    return WER_REPORT_METADATA_V1
EFaultRepRetVal = Int32
EFaultRepRetVal_frrvOk = 0
EFaultRepRetVal_frrvOkManifest = 1
EFaultRepRetVal_frrvOkQueued = 2
EFaultRepRetVal_frrvErr = 3
EFaultRepRetVal_frrvErrNoDW = 4
EFaultRepRetVal_frrvErrTimeout = 5
EFaultRepRetVal_frrvLaunchDebugger = 6
EFaultRepRetVal_frrvOkHeadless = 7
EFaultRepRetVal_frrvErrAnotherInstance = 8
EFaultRepRetVal_frrvErrNoMemory = 9
EFaultRepRetVal_frrvErrDoubleFault = 10
def _define_pfn_REPORTFAULT():
    return CFUNCTYPE(win32more.System.ErrorReporting.EFaultRepRetVal,POINTER(win32more.System.Diagnostics.Debug.EXCEPTION_POINTERS_head),UInt32, use_last_error=False)
def _define_pfn_ADDEREXCLUDEDAPPLICATIONA():
    return CFUNCTYPE(win32more.System.ErrorReporting.EFaultRepRetVal,win32more.Foundation.PSTR, use_last_error=False)
def _define_pfn_ADDEREXCLUDEDAPPLICATIONW():
    return CFUNCTYPE(win32more.System.ErrorReporting.EFaultRepRetVal,win32more.Foundation.PWSTR, use_last_error=False)
def _define_WerReportCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.ErrorReporting.WER_REPORT_TYPE,POINTER(win32more.System.ErrorReporting.WER_REPORT_INFORMATION_head),POINTER(win32more.System.ErrorReporting.HREPORT), use_last_error=False)(("WerReportCreate", windll["wer"]), ((1, 'pwzEventType'),(1, 'repType'),(1, 'pReportInformation'),(1, 'phReportHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerReportSetParameter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORT,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("WerReportSetParameter", windll["wer"]), ((1, 'hReportHandle'),(1, 'dwparamID'),(1, 'pwzName'),(1, 'pwzValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerReportAddFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORT,win32more.Foundation.PWSTR,win32more.System.ErrorReporting.WER_FILE_TYPE,win32more.System.ErrorReporting.WER_FILE, use_last_error=False)(("WerReportAddFile", windll["wer"]), ((1, 'hReportHandle'),(1, 'pwzPath'),(1, 'repFileType'),(1, 'dwFileFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerReportSetUIOption():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORT,win32more.System.ErrorReporting.WER_REPORT_UI,win32more.Foundation.PWSTR, use_last_error=False)(("WerReportSetUIOption", windll["wer"]), ((1, 'hReportHandle'),(1, 'repUITypeID'),(1, 'pwzValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerReportSubmit():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORT,win32more.System.ErrorReporting.WER_CONSENT,win32more.System.ErrorReporting.WER_SUBMIT_FLAGS,POINTER(win32more.System.ErrorReporting.WER_SUBMIT_RESULT), use_last_error=False)(("WerReportSubmit", windll["wer"]), ((1, 'hReportHandle'),(1, 'consent'),(1, 'dwFlags'),(1, 'pSubmitResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerReportAddDump():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORT,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.System.ErrorReporting.WER_DUMP_TYPE,POINTER(win32more.System.ErrorReporting.WER_EXCEPTION_INFORMATION_head),POINTER(win32more.System.ErrorReporting.WER_DUMP_CUSTOM_OPTIONS_head),UInt32, use_last_error=False)(("WerReportAddDump", windll["wer"]), ((1, 'hReportHandle'),(1, 'hProcess'),(1, 'hThread'),(1, 'dumpType'),(1, 'pExceptionParam'),(1, 'pDumpCustomOptions'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerReportCloseHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORT, use_last_error=False)(("WerReportCloseHandle", windll["wer"]), ((1, 'hReportHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerRegisterFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.ErrorReporting.WER_REGISTER_FILE_TYPE,win32more.System.ErrorReporting.WER_FILE, use_last_error=False)(("WerRegisterFile", windll["KERNEL32"]), ((1, 'pwzFile'),(1, 'regFileType'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerUnregisterFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("WerUnregisterFile", windll["KERNEL32"]), ((1, 'pwzFilePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerRegisterMemoryBlock():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32, use_last_error=False)(("WerRegisterMemoryBlock", windll["KERNEL32"]), ((1, 'pvAddress'),(1, 'dwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerUnregisterMemoryBlock():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("WerUnregisterMemoryBlock", windll["KERNEL32"]), ((1, 'pvAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerRegisterExcludedMemoryBlock():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32, use_last_error=False)(("WerRegisterExcludedMemoryBlock", windll["KERNEL32"]), ((1, 'address'),(1, 'size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerUnregisterExcludedMemoryBlock():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("WerUnregisterExcludedMemoryBlock", windll["KERNEL32"]), ((1, 'address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerRegisterCustomMetadata():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("WerRegisterCustomMetadata", windll["KERNEL32"]), ((1, 'key'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerUnregisterCustomMetadata():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("WerUnregisterCustomMetadata", windll["KERNEL32"]), ((1, 'key'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerRegisterAdditionalProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(("WerRegisterAdditionalProcess", windll["KERNEL32"]), ((1, 'processId'),(1, 'captureExtraInfoForThreadId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerUnregisterAdditionalProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("WerUnregisterAdditionalProcess", windll["KERNEL32"]), ((1, 'processId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerRegisterAppLocalDump():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("WerRegisterAppLocalDump", windll["KERNEL32"]), ((1, 'localAppDataRelativePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerUnregisterAppLocalDump():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("WerUnregisterAppLocalDump", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerSetFlags():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.WER_FAULT_REPORTING, use_last_error=False)(("WerSetFlags", windll["KERNEL32"]), ((1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerGetFlags():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.System.ErrorReporting.WER_FAULT_REPORTING), use_last_error=False)(("WerGetFlags", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'pdwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerAddExcludedApplication():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("WerAddExcludedApplication", windll["wer"]), ((1, 'pwzExeName'),(1, 'bAllUsers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerRemoveExcludedApplication():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("WerRemoveExcludedApplication", windll["wer"]), ((1, 'pwzExeName'),(1, 'bAllUsers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerRegisterRuntimeExceptionModule():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,c_void_p, use_last_error=False)(("WerRegisterRuntimeExceptionModule", windll["KERNEL32"]), ((1, 'pwszOutOfProcessCallbackDll'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerUnregisterRuntimeExceptionModule():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,c_void_p, use_last_error=False)(("WerUnregisterRuntimeExceptionModule", windll["KERNEL32"]), ((1, 'pwszOutOfProcessCallbackDll'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerStoreOpen():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.REPORT_STORE_TYPES,POINTER(win32more.System.ErrorReporting.HREPORTSTORE), use_last_error=False)(("WerStoreOpen", windll["wer"]), ((1, 'repStoreType'),(1, 'phReportStore'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerStoreClose():
    try:
        return WINFUNCTYPE(Void,win32more.System.ErrorReporting.HREPORTSTORE, use_last_error=False)(("WerStoreClose", windll["wer"]), ((1, 'hReportStore'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerStoreGetFirstReportKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORTSTORE,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("WerStoreGetFirstReportKey", windll["wer"]), ((1, 'hReportStore'),(1, 'ppszReportKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerStoreGetNextReportKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORTSTORE,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("WerStoreGetNextReportKey", windll["wer"]), ((1, 'hReportStore'),(1, 'ppszReportKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerStoreQueryReportMetadataV2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORTSTORE,win32more.Foundation.PWSTR,POINTER(win32more.System.ErrorReporting.WER_REPORT_METADATA_V2_head), use_last_error=False)(("WerStoreQueryReportMetadataV2", windll["wer"]), ((1, 'hReportStore'),(1, 'pszReportKey'),(1, 'pReportMetadata'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerStoreQueryReportMetadataV3():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORTSTORE,win32more.Foundation.PWSTR,POINTER(win32more.System.ErrorReporting.WER_REPORT_METADATA_V3_head), use_last_error=False)(("WerStoreQueryReportMetadataV3", windll["wer"]), ((1, 'hReportStore'),(1, 'pszReportKey'),(1, 'pReportMetadata'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerFreeString():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.PWSTR, use_last_error=False)(("WerFreeString", windll["wer"]), ((1, 'pwszStr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerStorePurge():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("WerStorePurge", windll["wer"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerStoreGetReportCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORTSTORE,POINTER(UInt32), use_last_error=False)(("WerStoreGetReportCount", windll["wer"]), ((1, 'hReportStore'),(1, 'pdwReportCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerStoreGetSizeOnDisk():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORTSTORE,POINTER(UInt64), use_last_error=False)(("WerStoreGetSizeOnDisk", windll["wer"]), ((1, 'hReportStore'),(1, 'pqwSizeInBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerStoreQueryReportMetadataV1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORTSTORE,win32more.Foundation.PWSTR,POINTER(win32more.System.ErrorReporting.WER_REPORT_METADATA_V1_head), use_last_error=False)(("WerStoreQueryReportMetadataV1", windll["wer"]), ((1, 'hReportStore'),(1, 'pszReportKey'),(1, 'pReportMetadata'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WerStoreUploadReport():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.ErrorReporting.HREPORTSTORE,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.ErrorReporting.WER_SUBMIT_RESULT), use_last_error=False)(("WerStoreUploadReport", windll["wer"]), ((1, 'hReportStore'),(1, 'pszReportKey'),(1, 'dwFlags'),(1, 'pSubmitResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReportFault():
    try:
        return WINFUNCTYPE(win32more.System.ErrorReporting.EFaultRepRetVal,POINTER(win32more.System.Diagnostics.Debug.EXCEPTION_POINTERS_head),UInt32, use_last_error=False)(("ReportFault", windll["faultrep"]), ((1, 'pep'),(1, 'dwOpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddERExcludedApplicationA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR, use_last_error=True)(("AddERExcludedApplicationA", windll["faultrep"]), ((1, 'szApplication'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddERExcludedApplicationW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=True)(("AddERExcludedApplicationW", windll["faultrep"]), ((1, 'wszApplication'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddERExcludedApplication():
    return win32more.System.ErrorReporting.AddERExcludedApplicationW
def _define_WerReportHang():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR, use_last_error=False)(("WerReportHang", windll["faultrep"]), ((1, 'hwndHungApp'),(1, 'pwzHungApplicationName'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "WER_FAULT_REPORTING_NO_UI",
    "WER_FAULT_REPORTING_FLAG_NO_HEAP_ON_QUEUE",
    "WER_FAULT_REPORTING_DISABLE_SNAPSHOT_CRASH",
    "WER_FAULT_REPORTING_DISABLE_SNAPSHOT_HANG",
    "WER_FAULT_REPORTING_CRITICAL",
    "WER_FAULT_REPORTING_DURABLE",
    "WER_MAX_TOTAL_PARAM_LENGTH",
    "WER_MAX_PREFERRED_MODULES",
    "WER_MAX_PREFERRED_MODULES_BUFFER",
    "WER_P0",
    "WER_P1",
    "WER_P2",
    "WER_P3",
    "WER_P4",
    "WER_P5",
    "WER_P6",
    "WER_P7",
    "WER_P8",
    "WER_P9",
    "WER_FILE_COMPRESSED",
    "WER_SUBMIT_BYPASS_POWER_THROTTLING",
    "WER_SUBMIT_BYPASS_NETWORK_COST_THROTTLING",
    "WER_DUMP_MASK_START",
    "WER_DUMP_NOHEAP_ONQUEUE",
    "WER_DUMP_AUXILIARY",
    "WER_MAX_REGISTERED_ENTRIES",
    "WER_MAX_REGISTERED_METADATA",
    "WER_MAX_REGISTERED_DUMPCOLLECTION",
    "WER_METADATA_KEY_MAX_LENGTH",
    "WER_METADATA_VALUE_MAX_LENGTH",
    "WER_MAX_SIGNATURE_NAME_LENGTH",
    "WER_MAX_EVENT_NAME_LENGTH",
    "WER_MAX_PARAM_LENGTH",
    "WER_MAX_PARAM_COUNT",
    "WER_MAX_FRIENDLY_EVENT_NAME_LENGTH",
    "WER_MAX_APPLICATION_NAME_LENGTH",
    "WER_MAX_DESCRIPTION_LENGTH",
    "WER_MAX_BUCKET_ID_STRING_LENGTH",
    "WER_MAX_LOCAL_DUMP_SUBPATH_LENGTH",
    "WER_MAX_REGISTERED_RUNTIME_EXCEPTION_MODULES",
    "WER_FILE",
    "WER_FILE_ANONYMOUS_DATA",
    "WER_FILE_DELETE_WHEN_DONE",
    "WER_SUBMIT_FLAGS",
    "WER_SUBMIT_ADD_REGISTERED_DATA",
    "WER_SUBMIT_HONOR_RECOVERY",
    "WER_SUBMIT_HONOR_RESTART",
    "WER_SUBMIT_NO_ARCHIVE",
    "WER_SUBMIT_NO_CLOSE_UI",
    "WER_SUBMIT_NO_QUEUE",
    "WER_SUBMIT_OUTOFPROCESS",
    "WER_SUBMIT_OUTOFPROCESS_ASYNC",
    "WER_SUBMIT_QUEUE",
    "WER_SUBMIT_SHOW_DEBUG",
    "WER_SUBMIT_START_MINIMIZED",
    "WER_SUBMIT_BYPASS_DATA_THROTTLING",
    "WER_SUBMIT_ARCHIVE_PARAMETERS_ONLY",
    "WER_SUBMIT_REPORT_MACHINE_ID",
    "WER_FAULT_REPORTING",
    "WER_FAULT_REPORTING_FLAG_DISABLE_THREAD_SUSPENSION",
    "WER_FAULT_REPORTING_FLAG_NOHEAP",
    "WER_FAULT_REPORTING_FLAG_QUEUE",
    "WER_FAULT_REPORTING_FLAG_QUEUE_UPLOAD",
    "WER_FAULT_REPORTING_ALWAYS_SHOW_UI",
    "HREPORT",
    "HREPORTSTORE",
    "WER_REPORT_UI",
    "WER_REPORT_UI_WerUIAdditionalDataDlgHeader",
    "WER_REPORT_UI_WerUIIconFilePath",
    "WER_REPORT_UI_WerUIConsentDlgHeader",
    "WER_REPORT_UI_WerUIConsentDlgBody",
    "WER_REPORT_UI_WerUIOnlineSolutionCheckText",
    "WER_REPORT_UI_WerUIOfflineSolutionCheckText",
    "WER_REPORT_UI_WerUICloseText",
    "WER_REPORT_UI_WerUICloseDlgHeader",
    "WER_REPORT_UI_WerUICloseDlgBody",
    "WER_REPORT_UI_WerUICloseDlgButtonText",
    "WER_REPORT_UI_WerUIMax",
    "WER_REGISTER_FILE_TYPE",
    "WER_REGISTER_FILE_TYPE_WerRegFileTypeUserDocument",
    "WER_REGISTER_FILE_TYPE_WerRegFileTypeOther",
    "WER_REGISTER_FILE_TYPE_WerRegFileTypeMax",
    "WER_FILE_TYPE",
    "WER_FILE_TYPE_WerFileTypeMicrodump",
    "WER_FILE_TYPE_WerFileTypeMinidump",
    "WER_FILE_TYPE_WerFileTypeHeapdump",
    "WER_FILE_TYPE_WerFileTypeUserDocument",
    "WER_FILE_TYPE_WerFileTypeOther",
    "WER_FILE_TYPE_WerFileTypeTriagedump",
    "WER_FILE_TYPE_WerFileTypeCustomDump",
    "WER_FILE_TYPE_WerFileTypeAuxiliaryDump",
    "WER_FILE_TYPE_WerFileTypeEtlTrace",
    "WER_FILE_TYPE_WerFileTypeMax",
    "WER_SUBMIT_RESULT",
    "WER_SUBMIT_RESULT_WerReportQueued",
    "WER_SUBMIT_RESULT_WerReportUploaded",
    "WER_SUBMIT_RESULT_WerReportDebug",
    "WER_SUBMIT_RESULT_WerReportFailed",
    "WER_SUBMIT_RESULT_WerDisabled",
    "WER_SUBMIT_RESULT_WerReportCancelled",
    "WER_SUBMIT_RESULT_WerDisabledQueue",
    "WER_SUBMIT_RESULT_WerReportAsync",
    "WER_SUBMIT_RESULT_WerCustomAction",
    "WER_SUBMIT_RESULT_WerThrottled",
    "WER_SUBMIT_RESULT_WerReportUploadedCab",
    "WER_SUBMIT_RESULT_WerStorageLocationNotFound",
    "WER_SUBMIT_RESULT_WerSubmitResultMax",
    "WER_REPORT_TYPE",
    "WER_REPORT_TYPE_WerReportNonCritical",
    "WER_REPORT_TYPE_WerReportCritical",
    "WER_REPORT_TYPE_WerReportApplicationCrash",
    "WER_REPORT_TYPE_WerReportApplicationHang",
    "WER_REPORT_TYPE_WerReportKernel",
    "WER_REPORT_TYPE_WerReportInvalid",
    "WER_REPORT_INFORMATION",
    "WER_REPORT_INFORMATION_V3",
    "WER_DUMP_CUSTOM_OPTIONS",
    "WER_DUMP_CUSTOM_OPTIONS_V2",
    "WER_REPORT_INFORMATION_V4",
    "WER_REPORT_INFORMATION_V5",
    "WER_DUMP_CUSTOM_OPTIONS_V3",
    "WER_EXCEPTION_INFORMATION",
    "WER_CONSENT",
    "WER_CONSENT_WerConsentNotAsked",
    "WER_CONSENT_WerConsentApproved",
    "WER_CONSENT_WerConsentDenied",
    "WER_CONSENT_WerConsentAlwaysPrompt",
    "WER_CONSENT_WerConsentMax",
    "WER_DUMP_TYPE",
    "WER_DUMP_TYPE_WerDumpTypeNone",
    "WER_DUMP_TYPE_WerDumpTypeMicroDump",
    "WER_DUMP_TYPE_WerDumpTypeMiniDump",
    "WER_DUMP_TYPE_WerDumpTypeHeapDump",
    "WER_DUMP_TYPE_WerDumpTypeTriageDump",
    "WER_DUMP_TYPE_WerDumpTypeMax",
    "WER_RUNTIME_EXCEPTION_INFORMATION",
    "PFN_WER_RUNTIME_EXCEPTION_EVENT",
    "PFN_WER_RUNTIME_EXCEPTION_EVENT_SIGNATURE",
    "PFN_WER_RUNTIME_EXCEPTION_DEBUGGER_LAUNCH",
    "REPORT_STORE_TYPES",
    "E_STORE_USER_ARCHIVE",
    "E_STORE_USER_QUEUE",
    "E_STORE_MACHINE_ARCHIVE",
    "E_STORE_MACHINE_QUEUE",
    "E_STORE_INVALID",
    "WER_REPORT_PARAMETER",
    "WER_REPORT_SIGNATURE",
    "WER_REPORT_METADATA_V2",
    "WER_REPORT_METADATA_V3",
    "WER_REPORT_METADATA_V1",
    "EFaultRepRetVal",
    "EFaultRepRetVal_frrvOk",
    "EFaultRepRetVal_frrvOkManifest",
    "EFaultRepRetVal_frrvOkQueued",
    "EFaultRepRetVal_frrvErr",
    "EFaultRepRetVal_frrvErrNoDW",
    "EFaultRepRetVal_frrvErrTimeout",
    "EFaultRepRetVal_frrvLaunchDebugger",
    "EFaultRepRetVal_frrvOkHeadless",
    "EFaultRepRetVal_frrvErrAnotherInstance",
    "EFaultRepRetVal_frrvErrNoMemory",
    "EFaultRepRetVal_frrvErrDoubleFault",
    "pfn_REPORTFAULT",
    "pfn_ADDEREXCLUDEDAPPLICATIONA",
    "pfn_ADDEREXCLUDEDAPPLICATIONW",
    "WerReportCreate",
    "WerReportSetParameter",
    "WerReportAddFile",
    "WerReportSetUIOption",
    "WerReportSubmit",
    "WerReportAddDump",
    "WerReportCloseHandle",
    "WerRegisterFile",
    "WerUnregisterFile",
    "WerRegisterMemoryBlock",
    "WerUnregisterMemoryBlock",
    "WerRegisterExcludedMemoryBlock",
    "WerUnregisterExcludedMemoryBlock",
    "WerRegisterCustomMetadata",
    "WerUnregisterCustomMetadata",
    "WerRegisterAdditionalProcess",
    "WerUnregisterAdditionalProcess",
    "WerRegisterAppLocalDump",
    "WerUnregisterAppLocalDump",
    "WerSetFlags",
    "WerGetFlags",
    "WerAddExcludedApplication",
    "WerRemoveExcludedApplication",
    "WerRegisterRuntimeExceptionModule",
    "WerUnregisterRuntimeExceptionModule",
    "WerStoreOpen",
    "WerStoreClose",
    "WerStoreGetFirstReportKey",
    "WerStoreGetNextReportKey",
    "WerStoreQueryReportMetadataV2",
    "WerStoreQueryReportMetadataV3",
    "WerFreeString",
    "WerStorePurge",
    "WerStoreGetReportCount",
    "WerStoreGetSizeOnDisk",
    "WerStoreQueryReportMetadataV1",
    "WerStoreUploadReport",
    "ReportFault",
    "AddERExcludedApplicationA",
    "AddERExcludedApplicationW",
    "AddERExcludedApplication",
    "WerReportHang",
]
