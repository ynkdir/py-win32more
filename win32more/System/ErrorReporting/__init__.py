from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Diagnostics.Debug
import win32more.System.ErrorReporting
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
WER_FAULT_REPORTING_NO_UI: UInt32 = 32
WER_FAULT_REPORTING_FLAG_NO_HEAP_ON_QUEUE: UInt32 = 64
WER_FAULT_REPORTING_DISABLE_SNAPSHOT_CRASH: UInt32 = 128
WER_FAULT_REPORTING_DISABLE_SNAPSHOT_HANG: UInt32 = 256
WER_FAULT_REPORTING_CRITICAL: UInt32 = 512
WER_FAULT_REPORTING_DURABLE: UInt32 = 1024
WER_MAX_TOTAL_PARAM_LENGTH: UInt32 = 1720
WER_MAX_PREFERRED_MODULES: UInt32 = 128
WER_MAX_PREFERRED_MODULES_BUFFER: UInt32 = 256
APPCRASH_EVENT: String = 'APPCRASH'
PACKAGED_APPCRASH_EVENT: String = 'MoAppCrash'
WER_P0: UInt32 = 0
WER_P1: UInt32 = 1
WER_P2: UInt32 = 2
WER_P3: UInt32 = 3
WER_P4: UInt32 = 4
WER_P5: UInt32 = 5
WER_P6: UInt32 = 6
WER_P7: UInt32 = 7
WER_P8: UInt32 = 8
WER_P9: UInt32 = 9
WER_FILE_COMPRESSED: UInt32 = 4
WER_SUBMIT_BYPASS_POWER_THROTTLING: UInt32 = 16384
WER_SUBMIT_BYPASS_NETWORK_COST_THROTTLING: UInt32 = 32768
WER_DUMP_MASK_START: UInt32 = 1
WER_DUMP_NOHEAP_ONQUEUE: UInt32 = 1
WER_DUMP_AUXILIARY: UInt32 = 2
WER_MAX_REGISTERED_ENTRIES: UInt32 = 512
WER_MAX_REGISTERED_METADATA: UInt32 = 8
WER_MAX_REGISTERED_DUMPCOLLECTION: UInt32 = 4
WER_METADATA_KEY_MAX_LENGTH: UInt32 = 64
WER_METADATA_VALUE_MAX_LENGTH: UInt32 = 128
WER_MAX_SIGNATURE_NAME_LENGTH: UInt32 = 128
WER_MAX_EVENT_NAME_LENGTH: UInt32 = 64
WER_MAX_PARAM_LENGTH: UInt32 = 260
WER_MAX_PARAM_COUNT: UInt32 = 10
WER_MAX_FRIENDLY_EVENT_NAME_LENGTH: UInt32 = 128
WER_MAX_APPLICATION_NAME_LENGTH: UInt32 = 128
WER_MAX_DESCRIPTION_LENGTH: UInt32 = 512
WER_MAX_BUCKET_ID_STRING_LENGTH: UInt32 = 260
WER_MAX_LOCAL_DUMP_SUBPATH_LENGTH: UInt32 = 64
WER_MAX_REGISTERED_RUNTIME_EXCEPTION_MODULES: UInt32 = 16
WER_RUNTIME_EXCEPTION_EVENT_FUNCTION: String = 'OutOfProcessExceptionEventCallback'
WER_RUNTIME_EXCEPTION_EVENT_SIGNATURE_FUNCTION: String = 'OutOfProcessExceptionEventSignatureCallback'
WER_RUNTIME_EXCEPTION_DEBUGGER_LAUNCH: String = 'OutOfProcessExceptionEventDebuggerLaunchCallback'
@winfunctype('wer.dll')
def WerReportCreate(pwzEventType: win32more.Foundation.PWSTR, repType: win32more.System.ErrorReporting.WER_REPORT_TYPE, pReportInformation: POINTER(win32more.System.ErrorReporting.WER_REPORT_INFORMATION_head), phReportHandle: POINTER(win32more.System.ErrorReporting.HREPORT)) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerReportSetParameter(hReportHandle: win32more.System.ErrorReporting.HREPORT, dwparamID: UInt32, pwzName: win32more.Foundation.PWSTR, pwzValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerReportAddFile(hReportHandle: win32more.System.ErrorReporting.HREPORT, pwzPath: win32more.Foundation.PWSTR, repFileType: win32more.System.ErrorReporting.WER_FILE_TYPE, dwFileFlags: win32more.System.ErrorReporting.WER_FILE) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerReportSetUIOption(hReportHandle: win32more.System.ErrorReporting.HREPORT, repUITypeID: win32more.System.ErrorReporting.WER_REPORT_UI, pwzValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerReportSubmit(hReportHandle: win32more.System.ErrorReporting.HREPORT, consent: win32more.System.ErrorReporting.WER_CONSENT, dwFlags: win32more.System.ErrorReporting.WER_SUBMIT_FLAGS, pSubmitResult: POINTER(win32more.System.ErrorReporting.WER_SUBMIT_RESULT)) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerReportAddDump(hReportHandle: win32more.System.ErrorReporting.HREPORT, hProcess: win32more.Foundation.HANDLE, hThread: win32more.Foundation.HANDLE, dumpType: win32more.System.ErrorReporting.WER_DUMP_TYPE, pExceptionParam: POINTER(win32more.System.ErrorReporting.WER_EXCEPTION_INFORMATION_head), pDumpCustomOptions: POINTER(win32more.System.ErrorReporting.WER_DUMP_CUSTOM_OPTIONS_head), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerReportCloseHandle(hReportHandle: win32more.System.ErrorReporting.HREPORT) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterFile(pwzFile: win32more.Foundation.PWSTR, regFileType: win32more.System.ErrorReporting.WER_REGISTER_FILE_TYPE, dwFlags: win32more.System.ErrorReporting.WER_FILE) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterFile(pwzFilePath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterMemoryBlock(pvAddress: c_void_p, dwSize: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterMemoryBlock(pvAddress: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterExcludedMemoryBlock(address: c_void_p, size: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterExcludedMemoryBlock(address: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterCustomMetadata(key: win32more.Foundation.PWSTR, value: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterCustomMetadata(key: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterAdditionalProcess(processId: UInt32, captureExtraInfoForThreadId: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterAdditionalProcess(processId: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterAppLocalDump(localAppDataRelativePath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterAppLocalDump() -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerSetFlags(dwFlags: win32more.System.ErrorReporting.WER_FAULT_REPORTING) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerGetFlags(hProcess: win32more.Foundation.HANDLE, pdwFlags: POINTER(win32more.System.ErrorReporting.WER_FAULT_REPORTING)) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerAddExcludedApplication(pwzExeName: win32more.Foundation.PWSTR, bAllUsers: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerRemoveExcludedApplication(pwzExeName: win32more.Foundation.PWSTR, bAllUsers: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterRuntimeExceptionModule(pwszOutOfProcessCallbackDll: win32more.Foundation.PWSTR, pContext: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterRuntimeExceptionModule(pwszOutOfProcessCallbackDll: win32more.Foundation.PWSTR, pContext: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreOpen(repStoreType: win32more.System.ErrorReporting.REPORT_STORE_TYPES, phReportStore: POINTER(win32more.System.ErrorReporting.HREPORTSTORE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreClose(hReportStore: win32more.System.ErrorReporting.HREPORTSTORE) -> Void: ...
@winfunctype('wer.dll')
def WerStoreGetFirstReportKey(hReportStore: win32more.System.ErrorReporting.HREPORTSTORE, ppszReportKey: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreGetNextReportKey(hReportStore: win32more.System.ErrorReporting.HREPORTSTORE, ppszReportKey: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreQueryReportMetadataV2(hReportStore: win32more.System.ErrorReporting.HREPORTSTORE, pszReportKey: win32more.Foundation.PWSTR, pReportMetadata: POINTER(win32more.System.ErrorReporting.WER_REPORT_METADATA_V2_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreQueryReportMetadataV3(hReportStore: win32more.System.ErrorReporting.HREPORTSTORE, pszReportKey: win32more.Foundation.PWSTR, pReportMetadata: POINTER(win32more.System.ErrorReporting.WER_REPORT_METADATA_V3_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerFreeString(pwszStr: win32more.Foundation.PWSTR) -> Void: ...
@winfunctype('wer.dll')
def WerStorePurge() -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreGetReportCount(hReportStore: win32more.System.ErrorReporting.HREPORTSTORE, pdwReportCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreGetSizeOnDisk(hReportStore: win32more.System.ErrorReporting.HREPORTSTORE, pqwSizeInBytes: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreQueryReportMetadataV1(hReportStore: win32more.System.ErrorReporting.HREPORTSTORE, pszReportKey: win32more.Foundation.PWSTR, pReportMetadata: POINTER(win32more.System.ErrorReporting.WER_REPORT_METADATA_V1_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreUploadReport(hReportStore: win32more.System.ErrorReporting.HREPORTSTORE, pszReportKey: win32more.Foundation.PWSTR, dwFlags: UInt32, pSubmitResult: POINTER(win32more.System.ErrorReporting.WER_SUBMIT_RESULT)) -> win32more.Foundation.HRESULT: ...
@winfunctype('faultrep.dll')
def ReportFault(pep: POINTER(win32more.System.Diagnostics.Debug.EXCEPTION_POINTERS_head), dwOpt: UInt32) -> win32more.System.ErrorReporting.EFaultRepRetVal: ...
@winfunctype('faultrep.dll')
def AddERExcludedApplicationA(szApplication: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('faultrep.dll')
def AddERExcludedApplicationW(wszApplication: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('faultrep.dll')
def WerReportHang(hwndHungApp: win32more.Foundation.HWND, pwzHungApplicationName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
EFaultRepRetVal = Int32
EFaultRepRetVal_frrvOk: EFaultRepRetVal = 0
EFaultRepRetVal_frrvOkManifest: EFaultRepRetVal = 1
EFaultRepRetVal_frrvOkQueued: EFaultRepRetVal = 2
EFaultRepRetVal_frrvErr: EFaultRepRetVal = 3
EFaultRepRetVal_frrvErrNoDW: EFaultRepRetVal = 4
EFaultRepRetVal_frrvErrTimeout: EFaultRepRetVal = 5
EFaultRepRetVal_frrvLaunchDebugger: EFaultRepRetVal = 6
EFaultRepRetVal_frrvOkHeadless: EFaultRepRetVal = 7
EFaultRepRetVal_frrvErrAnotherInstance: EFaultRepRetVal = 8
EFaultRepRetVal_frrvErrNoMemory: EFaultRepRetVal = 9
EFaultRepRetVal_frrvErrDoubleFault: EFaultRepRetVal = 10
HREPORT = IntPtr
HREPORTSTORE = IntPtr
@winfunctype_pointer
def PFN_WER_RUNTIME_EXCEPTION_DEBUGGER_LAUNCH(pContext: c_void_p, pExceptionInformation: POINTER(win32more.System.ErrorReporting.WER_RUNTIME_EXCEPTION_INFORMATION_head), pbIsCustomDebugger: POINTER(win32more.Foundation.BOOL), pwszDebuggerLaunch: win32more.Foundation.PWSTR, pchDebuggerLaunch: POINTER(UInt32), pbIsDebuggerAutolaunch: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_WER_RUNTIME_EXCEPTION_EVENT(pContext: c_void_p, pExceptionInformation: POINTER(win32more.System.ErrorReporting.WER_RUNTIME_EXCEPTION_INFORMATION_head), pbOwnershipClaimed: POINTER(win32more.Foundation.BOOL), pwszEventName: win32more.Foundation.PWSTR, pchSize: POINTER(UInt32), pdwSignatureCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_WER_RUNTIME_EXCEPTION_EVENT_SIGNATURE(pContext: c_void_p, pExceptionInformation: POINTER(win32more.System.ErrorReporting.WER_RUNTIME_EXCEPTION_INFORMATION_head), dwIndex: UInt32, pwszName: win32more.Foundation.PWSTR, pchName: POINTER(UInt32), pwszValue: win32more.Foundation.PWSTR, pchValue: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
REPORT_STORE_TYPES = Int32
E_STORE_USER_ARCHIVE: REPORT_STORE_TYPES = 0
E_STORE_USER_QUEUE: REPORT_STORE_TYPES = 1
E_STORE_MACHINE_ARCHIVE: REPORT_STORE_TYPES = 2
E_STORE_MACHINE_QUEUE: REPORT_STORE_TYPES = 3
E_STORE_INVALID: REPORT_STORE_TYPES = 4
WER_CONSENT = Int32
WER_CONSENT_WerConsentNotAsked: WER_CONSENT = 1
WER_CONSENT_WerConsentApproved: WER_CONSENT = 2
WER_CONSENT_WerConsentDenied: WER_CONSENT = 3
WER_CONSENT_WerConsentAlwaysPrompt: WER_CONSENT = 4
WER_CONSENT_WerConsentMax: WER_CONSENT = 5
class WER_DUMP_CUSTOM_OPTIONS(Structure):
    dwSize: UInt32
    dwMask: UInt32
    dwDumpFlags: UInt32
    bOnlyThisThread: win32more.Foundation.BOOL
    dwExceptionThreadFlags: UInt32
    dwOtherThreadFlags: UInt32
    dwExceptionThreadExFlags: UInt32
    dwOtherThreadExFlags: UInt32
    dwPreferredModuleFlags: UInt32
    dwOtherModuleFlags: UInt32
    wzPreferredModuleList: Char * 256
class WER_DUMP_CUSTOM_OPTIONS_V2(Structure):
    dwSize: UInt32
    dwMask: UInt32
    dwDumpFlags: UInt32
    bOnlyThisThread: win32more.Foundation.BOOL
    dwExceptionThreadFlags: UInt32
    dwOtherThreadFlags: UInt32
    dwExceptionThreadExFlags: UInt32
    dwOtherThreadExFlags: UInt32
    dwPreferredModuleFlags: UInt32
    dwOtherModuleFlags: UInt32
    wzPreferredModuleList: Char * 256
    dwPreferredModuleResetFlags: UInt32
    dwOtherModuleResetFlags: UInt32
class WER_DUMP_CUSTOM_OPTIONS_V3(Structure):
    dwSize: UInt32
    dwMask: UInt32
    dwDumpFlags: UInt32
    bOnlyThisThread: win32more.Foundation.BOOL
    dwExceptionThreadFlags: UInt32
    dwOtherThreadFlags: UInt32
    dwExceptionThreadExFlags: UInt32
    dwOtherThreadExFlags: UInt32
    dwPreferredModuleFlags: UInt32
    dwOtherModuleFlags: UInt32
    wzPreferredModuleList: Char * 256
    dwPreferredModuleResetFlags: UInt32
    dwOtherModuleResetFlags: UInt32
    pvDumpKey: c_void_p
    hSnapshot: win32more.Foundation.HANDLE
    dwThreadID: UInt32
WER_DUMP_TYPE = Int32
WER_DUMP_TYPE_WerDumpTypeNone: WER_DUMP_TYPE = 0
WER_DUMP_TYPE_WerDumpTypeMicroDump: WER_DUMP_TYPE = 1
WER_DUMP_TYPE_WerDumpTypeMiniDump: WER_DUMP_TYPE = 2
WER_DUMP_TYPE_WerDumpTypeHeapDump: WER_DUMP_TYPE = 3
WER_DUMP_TYPE_WerDumpTypeTriageDump: WER_DUMP_TYPE = 4
WER_DUMP_TYPE_WerDumpTypeMax: WER_DUMP_TYPE = 5
class WER_EXCEPTION_INFORMATION(Structure):
    pExceptionPointers: POINTER(win32more.System.Diagnostics.Debug.EXCEPTION_POINTERS_head)
    bClientPointers: win32more.Foundation.BOOL
WER_FAULT_REPORTING = UInt32
WER_FAULT_REPORTING_FLAG_DISABLE_THREAD_SUSPENSION: WER_FAULT_REPORTING = 4
WER_FAULT_REPORTING_FLAG_NOHEAP: WER_FAULT_REPORTING = 1
WER_FAULT_REPORTING_FLAG_QUEUE: WER_FAULT_REPORTING = 2
WER_FAULT_REPORTING_FLAG_QUEUE_UPLOAD: WER_FAULT_REPORTING = 8
WER_FAULT_REPORTING_ALWAYS_SHOW_UI: WER_FAULT_REPORTING = 16
WER_FILE = UInt32
WER_FILE_ANONYMOUS_DATA: WER_FILE = 2
WER_FILE_DELETE_WHEN_DONE: WER_FILE = 1
WER_FILE_TYPE = Int32
WER_FILE_TYPE_WerFileTypeMicrodump: WER_FILE_TYPE = 1
WER_FILE_TYPE_WerFileTypeMinidump: WER_FILE_TYPE = 2
WER_FILE_TYPE_WerFileTypeHeapdump: WER_FILE_TYPE = 3
WER_FILE_TYPE_WerFileTypeUserDocument: WER_FILE_TYPE = 4
WER_FILE_TYPE_WerFileTypeOther: WER_FILE_TYPE = 5
WER_FILE_TYPE_WerFileTypeTriagedump: WER_FILE_TYPE = 6
WER_FILE_TYPE_WerFileTypeCustomDump: WER_FILE_TYPE = 7
WER_FILE_TYPE_WerFileTypeAuxiliaryDump: WER_FILE_TYPE = 8
WER_FILE_TYPE_WerFileTypeEtlTrace: WER_FILE_TYPE = 9
WER_FILE_TYPE_WerFileTypeMax: WER_FILE_TYPE = 10
WER_REGISTER_FILE_TYPE = Int32
WER_REGISTER_FILE_TYPE_WerRegFileTypeUserDocument: WER_REGISTER_FILE_TYPE = 1
WER_REGISTER_FILE_TYPE_WerRegFileTypeOther: WER_REGISTER_FILE_TYPE = 2
WER_REGISTER_FILE_TYPE_WerRegFileTypeMax: WER_REGISTER_FILE_TYPE = 3
class WER_REPORT_INFORMATION(Structure):
    dwSize: UInt32
    hProcess: win32more.Foundation.HANDLE
    wzConsentKey: Char * 64
    wzFriendlyEventName: Char * 128
    wzApplicationName: Char * 128
    wzApplicationPath: Char * 260
    wzDescription: Char * 512
    hwndParent: win32more.Foundation.HWND
class WER_REPORT_INFORMATION_V3(Structure):
    dwSize: UInt32
    hProcess: win32more.Foundation.HANDLE
    wzConsentKey: Char * 64
    wzFriendlyEventName: Char * 128
    wzApplicationName: Char * 128
    wzApplicationPath: Char * 260
    wzDescription: Char * 512
    hwndParent: win32more.Foundation.HWND
    wzNamespacePartner: Char * 64
    wzNamespaceGroup: Char * 64
class WER_REPORT_INFORMATION_V4(Structure):
    dwSize: UInt32
    hProcess: win32more.Foundation.HANDLE
    wzConsentKey: Char * 64
    wzFriendlyEventName: Char * 128
    wzApplicationName: Char * 128
    wzApplicationPath: Char * 260
    wzDescription: Char * 512
    hwndParent: win32more.Foundation.HWND
    wzNamespacePartner: Char * 64
    wzNamespaceGroup: Char * 64
    rgbApplicationIdentity: Byte * 16
    hSnapshot: win32more.Foundation.HANDLE
    hDeleteFilesImpersonationToken: win32more.Foundation.HANDLE
class WER_REPORT_INFORMATION_V5(Structure):
    dwSize: UInt32
    hProcess: win32more.Foundation.HANDLE
    wzConsentKey: Char * 64
    wzFriendlyEventName: Char * 128
    wzApplicationName: Char * 128
    wzApplicationPath: Char * 260
    wzDescription: Char * 512
    hwndParent: win32more.Foundation.HWND
    wzNamespacePartner: Char * 64
    wzNamespaceGroup: Char * 64
    rgbApplicationIdentity: Byte * 16
    hSnapshot: win32more.Foundation.HANDLE
    hDeleteFilesImpersonationToken: win32more.Foundation.HANDLE
    submitResultMax: win32more.System.ErrorReporting.WER_SUBMIT_RESULT
class WER_REPORT_METADATA_V1(Structure):
    Signature: win32more.System.ErrorReporting.WER_REPORT_SIGNATURE
    BucketId: Guid
    ReportId: Guid
    CreationTime: win32more.Foundation.FILETIME
    SizeInBytes: UInt64
class WER_REPORT_METADATA_V2(Structure):
    Signature: win32more.System.ErrorReporting.WER_REPORT_SIGNATURE
    BucketId: Guid
    ReportId: Guid
    CreationTime: win32more.Foundation.FILETIME
    SizeInBytes: UInt64
    CabId: Char * 260
    ReportStatus: UInt32
    ReportIntegratorId: Guid
    NumberOfFiles: UInt32
    SizeOfFileNames: UInt32
    FileNames: win32more.Foundation.PWSTR
class WER_REPORT_METADATA_V3(Structure):
    Signature: win32more.System.ErrorReporting.WER_REPORT_SIGNATURE
    BucketId: Guid
    ReportId: Guid
    CreationTime: win32more.Foundation.FILETIME
    SizeInBytes: UInt64
    CabId: Char * 260
    ReportStatus: UInt32
    ReportIntegratorId: Guid
    NumberOfFiles: UInt32
    SizeOfFileNames: UInt32
    FileNames: win32more.Foundation.PWSTR
    FriendlyEventName: Char * 128
    ApplicationName: Char * 128
    ApplicationPath: Char * 260
    Description: Char * 512
    BucketIdString: Char * 260
    LegacyBucketId: UInt64
class WER_REPORT_PARAMETER(Structure):
    Name: Char * 129
    Value: Char * 260
class WER_REPORT_SIGNATURE(Structure):
    EventName: Char * 65
    Parameters: win32more.System.ErrorReporting.WER_REPORT_PARAMETER * 10
WER_REPORT_TYPE = Int32
WER_REPORT_TYPE_WerReportNonCritical: WER_REPORT_TYPE = 0
WER_REPORT_TYPE_WerReportCritical: WER_REPORT_TYPE = 1
WER_REPORT_TYPE_WerReportApplicationCrash: WER_REPORT_TYPE = 2
WER_REPORT_TYPE_WerReportApplicationHang: WER_REPORT_TYPE = 3
WER_REPORT_TYPE_WerReportKernel: WER_REPORT_TYPE = 4
WER_REPORT_TYPE_WerReportInvalid: WER_REPORT_TYPE = 5
WER_REPORT_UI = Int32
WER_REPORT_UI_WerUIAdditionalDataDlgHeader: WER_REPORT_UI = 1
WER_REPORT_UI_WerUIIconFilePath: WER_REPORT_UI = 2
WER_REPORT_UI_WerUIConsentDlgHeader: WER_REPORT_UI = 3
WER_REPORT_UI_WerUIConsentDlgBody: WER_REPORT_UI = 4
WER_REPORT_UI_WerUIOnlineSolutionCheckText: WER_REPORT_UI = 5
WER_REPORT_UI_WerUIOfflineSolutionCheckText: WER_REPORT_UI = 6
WER_REPORT_UI_WerUICloseText: WER_REPORT_UI = 7
WER_REPORT_UI_WerUICloseDlgHeader: WER_REPORT_UI = 8
WER_REPORT_UI_WerUICloseDlgBody: WER_REPORT_UI = 9
WER_REPORT_UI_WerUICloseDlgButtonText: WER_REPORT_UI = 10
WER_REPORT_UI_WerUIMax: WER_REPORT_UI = 11
class WER_RUNTIME_EXCEPTION_INFORMATION(Structure):
    dwSize: UInt32
    hProcess: win32more.Foundation.HANDLE
    hThread: win32more.Foundation.HANDLE
    exceptionRecord: win32more.System.Diagnostics.Debug.EXCEPTION_RECORD
    context: win32more.System.Diagnostics.Debug.CONTEXT
    pwszReportId: win32more.Foundation.PWSTR
    bIsFatal: win32more.Foundation.BOOL
    dwReserved: UInt32
WER_SUBMIT_FLAGS = UInt32
WER_SUBMIT_ADD_REGISTERED_DATA: WER_SUBMIT_FLAGS = 16
WER_SUBMIT_HONOR_RECOVERY: WER_SUBMIT_FLAGS = 1
WER_SUBMIT_HONOR_RESTART: WER_SUBMIT_FLAGS = 2
WER_SUBMIT_NO_ARCHIVE: WER_SUBMIT_FLAGS = 256
WER_SUBMIT_NO_CLOSE_UI: WER_SUBMIT_FLAGS = 64
WER_SUBMIT_NO_QUEUE: WER_SUBMIT_FLAGS = 128
WER_SUBMIT_OUTOFPROCESS: WER_SUBMIT_FLAGS = 32
WER_SUBMIT_OUTOFPROCESS_ASYNC: WER_SUBMIT_FLAGS = 1024
WER_SUBMIT_QUEUE: WER_SUBMIT_FLAGS = 4
WER_SUBMIT_SHOW_DEBUG: WER_SUBMIT_FLAGS = 8
WER_SUBMIT_START_MINIMIZED: WER_SUBMIT_FLAGS = 512
WER_SUBMIT_BYPASS_DATA_THROTTLING: WER_SUBMIT_FLAGS = 2048
WER_SUBMIT_ARCHIVE_PARAMETERS_ONLY: WER_SUBMIT_FLAGS = 4096
WER_SUBMIT_REPORT_MACHINE_ID: WER_SUBMIT_FLAGS = 8192
WER_SUBMIT_RESULT = Int32
WER_SUBMIT_RESULT_WerReportQueued: WER_SUBMIT_RESULT = 1
WER_SUBMIT_RESULT_WerReportUploaded: WER_SUBMIT_RESULT = 2
WER_SUBMIT_RESULT_WerReportDebug: WER_SUBMIT_RESULT = 3
WER_SUBMIT_RESULT_WerReportFailed: WER_SUBMIT_RESULT = 4
WER_SUBMIT_RESULT_WerDisabled: WER_SUBMIT_RESULT = 5
WER_SUBMIT_RESULT_WerReportCancelled: WER_SUBMIT_RESULT = 6
WER_SUBMIT_RESULT_WerDisabledQueue: WER_SUBMIT_RESULT = 7
WER_SUBMIT_RESULT_WerReportAsync: WER_SUBMIT_RESULT = 8
WER_SUBMIT_RESULT_WerCustomAction: WER_SUBMIT_RESULT = 9
WER_SUBMIT_RESULT_WerThrottled: WER_SUBMIT_RESULT = 10
WER_SUBMIT_RESULT_WerReportUploadedCab: WER_SUBMIT_RESULT = 11
WER_SUBMIT_RESULT_WerStorageLocationNotFound: WER_SUBMIT_RESULT = 12
WER_SUBMIT_RESULT_WerSubmitResultMax: WER_SUBMIT_RESULT = 13
@winfunctype_pointer
def pfn_ADDEREXCLUDEDAPPLICATIONA(param0: win32more.Foundation.PSTR) -> win32more.System.ErrorReporting.EFaultRepRetVal: ...
@winfunctype_pointer
def pfn_ADDEREXCLUDEDAPPLICATIONW(param0: win32more.Foundation.PWSTR) -> win32more.System.ErrorReporting.EFaultRepRetVal: ...
@winfunctype_pointer
def pfn_REPORTFAULT(param0: POINTER(win32more.System.Diagnostics.Debug.EXCEPTION_POINTERS_head), param1: UInt32) -> win32more.System.ErrorReporting.EFaultRepRetVal: ...
make_head(_module, 'PFN_WER_RUNTIME_EXCEPTION_DEBUGGER_LAUNCH')
make_head(_module, 'PFN_WER_RUNTIME_EXCEPTION_EVENT')
make_head(_module, 'PFN_WER_RUNTIME_EXCEPTION_EVENT_SIGNATURE')
make_head(_module, 'WER_DUMP_CUSTOM_OPTIONS')
make_head(_module, 'WER_DUMP_CUSTOM_OPTIONS_V2')
make_head(_module, 'WER_DUMP_CUSTOM_OPTIONS_V3')
make_head(_module, 'WER_EXCEPTION_INFORMATION')
make_head(_module, 'WER_REPORT_INFORMATION')
make_head(_module, 'WER_REPORT_INFORMATION_V3')
make_head(_module, 'WER_REPORT_INFORMATION_V4')
make_head(_module, 'WER_REPORT_INFORMATION_V5')
make_head(_module, 'WER_REPORT_METADATA_V1')
make_head(_module, 'WER_REPORT_METADATA_V2')
make_head(_module, 'WER_REPORT_METADATA_V3')
make_head(_module, 'WER_REPORT_PARAMETER')
make_head(_module, 'WER_REPORT_SIGNATURE')
make_head(_module, 'WER_RUNTIME_EXCEPTION_INFORMATION')
make_head(_module, 'pfn_ADDEREXCLUDEDAPPLICATIONA')
make_head(_module, 'pfn_ADDEREXCLUDEDAPPLICATIONW')
make_head(_module, 'pfn_REPORTFAULT')
__all__ = [
    "APPCRASH_EVENT",
    "AddERExcludedApplicationA",
    "AddERExcludedApplicationW",
    "EFaultRepRetVal",
    "EFaultRepRetVal_frrvErr",
    "EFaultRepRetVal_frrvErrAnotherInstance",
    "EFaultRepRetVal_frrvErrDoubleFault",
    "EFaultRepRetVal_frrvErrNoDW",
    "EFaultRepRetVal_frrvErrNoMemory",
    "EFaultRepRetVal_frrvErrTimeout",
    "EFaultRepRetVal_frrvLaunchDebugger",
    "EFaultRepRetVal_frrvOk",
    "EFaultRepRetVal_frrvOkHeadless",
    "EFaultRepRetVal_frrvOkManifest",
    "EFaultRepRetVal_frrvOkQueued",
    "E_STORE_INVALID",
    "E_STORE_MACHINE_ARCHIVE",
    "E_STORE_MACHINE_QUEUE",
    "E_STORE_USER_ARCHIVE",
    "E_STORE_USER_QUEUE",
    "HREPORT",
    "HREPORTSTORE",
    "PACKAGED_APPCRASH_EVENT",
    "PFN_WER_RUNTIME_EXCEPTION_DEBUGGER_LAUNCH",
    "PFN_WER_RUNTIME_EXCEPTION_EVENT",
    "PFN_WER_RUNTIME_EXCEPTION_EVENT_SIGNATURE",
    "REPORT_STORE_TYPES",
    "ReportFault",
    "WER_CONSENT",
    "WER_CONSENT_WerConsentAlwaysPrompt",
    "WER_CONSENT_WerConsentApproved",
    "WER_CONSENT_WerConsentDenied",
    "WER_CONSENT_WerConsentMax",
    "WER_CONSENT_WerConsentNotAsked",
    "WER_DUMP_AUXILIARY",
    "WER_DUMP_CUSTOM_OPTIONS",
    "WER_DUMP_CUSTOM_OPTIONS_V2",
    "WER_DUMP_CUSTOM_OPTIONS_V3",
    "WER_DUMP_MASK_START",
    "WER_DUMP_NOHEAP_ONQUEUE",
    "WER_DUMP_TYPE",
    "WER_DUMP_TYPE_WerDumpTypeHeapDump",
    "WER_DUMP_TYPE_WerDumpTypeMax",
    "WER_DUMP_TYPE_WerDumpTypeMicroDump",
    "WER_DUMP_TYPE_WerDumpTypeMiniDump",
    "WER_DUMP_TYPE_WerDumpTypeNone",
    "WER_DUMP_TYPE_WerDumpTypeTriageDump",
    "WER_EXCEPTION_INFORMATION",
    "WER_FAULT_REPORTING",
    "WER_FAULT_REPORTING_ALWAYS_SHOW_UI",
    "WER_FAULT_REPORTING_CRITICAL",
    "WER_FAULT_REPORTING_DISABLE_SNAPSHOT_CRASH",
    "WER_FAULT_REPORTING_DISABLE_SNAPSHOT_HANG",
    "WER_FAULT_REPORTING_DURABLE",
    "WER_FAULT_REPORTING_FLAG_DISABLE_THREAD_SUSPENSION",
    "WER_FAULT_REPORTING_FLAG_NOHEAP",
    "WER_FAULT_REPORTING_FLAG_NO_HEAP_ON_QUEUE",
    "WER_FAULT_REPORTING_FLAG_QUEUE",
    "WER_FAULT_REPORTING_FLAG_QUEUE_UPLOAD",
    "WER_FAULT_REPORTING_NO_UI",
    "WER_FILE",
    "WER_FILE_ANONYMOUS_DATA",
    "WER_FILE_COMPRESSED",
    "WER_FILE_DELETE_WHEN_DONE",
    "WER_FILE_TYPE",
    "WER_FILE_TYPE_WerFileTypeAuxiliaryDump",
    "WER_FILE_TYPE_WerFileTypeCustomDump",
    "WER_FILE_TYPE_WerFileTypeEtlTrace",
    "WER_FILE_TYPE_WerFileTypeHeapdump",
    "WER_FILE_TYPE_WerFileTypeMax",
    "WER_FILE_TYPE_WerFileTypeMicrodump",
    "WER_FILE_TYPE_WerFileTypeMinidump",
    "WER_FILE_TYPE_WerFileTypeOther",
    "WER_FILE_TYPE_WerFileTypeTriagedump",
    "WER_FILE_TYPE_WerFileTypeUserDocument",
    "WER_MAX_APPLICATION_NAME_LENGTH",
    "WER_MAX_BUCKET_ID_STRING_LENGTH",
    "WER_MAX_DESCRIPTION_LENGTH",
    "WER_MAX_EVENT_NAME_LENGTH",
    "WER_MAX_FRIENDLY_EVENT_NAME_LENGTH",
    "WER_MAX_LOCAL_DUMP_SUBPATH_LENGTH",
    "WER_MAX_PARAM_COUNT",
    "WER_MAX_PARAM_LENGTH",
    "WER_MAX_PREFERRED_MODULES",
    "WER_MAX_PREFERRED_MODULES_BUFFER",
    "WER_MAX_REGISTERED_DUMPCOLLECTION",
    "WER_MAX_REGISTERED_ENTRIES",
    "WER_MAX_REGISTERED_METADATA",
    "WER_MAX_REGISTERED_RUNTIME_EXCEPTION_MODULES",
    "WER_MAX_SIGNATURE_NAME_LENGTH",
    "WER_MAX_TOTAL_PARAM_LENGTH",
    "WER_METADATA_KEY_MAX_LENGTH",
    "WER_METADATA_VALUE_MAX_LENGTH",
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
    "WER_REGISTER_FILE_TYPE",
    "WER_REGISTER_FILE_TYPE_WerRegFileTypeMax",
    "WER_REGISTER_FILE_TYPE_WerRegFileTypeOther",
    "WER_REGISTER_FILE_TYPE_WerRegFileTypeUserDocument",
    "WER_REPORT_INFORMATION",
    "WER_REPORT_INFORMATION_V3",
    "WER_REPORT_INFORMATION_V4",
    "WER_REPORT_INFORMATION_V5",
    "WER_REPORT_METADATA_V1",
    "WER_REPORT_METADATA_V2",
    "WER_REPORT_METADATA_V3",
    "WER_REPORT_PARAMETER",
    "WER_REPORT_SIGNATURE",
    "WER_REPORT_TYPE",
    "WER_REPORT_TYPE_WerReportApplicationCrash",
    "WER_REPORT_TYPE_WerReportApplicationHang",
    "WER_REPORT_TYPE_WerReportCritical",
    "WER_REPORT_TYPE_WerReportInvalid",
    "WER_REPORT_TYPE_WerReportKernel",
    "WER_REPORT_TYPE_WerReportNonCritical",
    "WER_REPORT_UI",
    "WER_REPORT_UI_WerUIAdditionalDataDlgHeader",
    "WER_REPORT_UI_WerUICloseDlgBody",
    "WER_REPORT_UI_WerUICloseDlgButtonText",
    "WER_REPORT_UI_WerUICloseDlgHeader",
    "WER_REPORT_UI_WerUICloseText",
    "WER_REPORT_UI_WerUIConsentDlgBody",
    "WER_REPORT_UI_WerUIConsentDlgHeader",
    "WER_REPORT_UI_WerUIIconFilePath",
    "WER_REPORT_UI_WerUIMax",
    "WER_REPORT_UI_WerUIOfflineSolutionCheckText",
    "WER_REPORT_UI_WerUIOnlineSolutionCheckText",
    "WER_RUNTIME_EXCEPTION_DEBUGGER_LAUNCH",
    "WER_RUNTIME_EXCEPTION_EVENT_FUNCTION",
    "WER_RUNTIME_EXCEPTION_EVENT_SIGNATURE_FUNCTION",
    "WER_RUNTIME_EXCEPTION_INFORMATION",
    "WER_SUBMIT_ADD_REGISTERED_DATA",
    "WER_SUBMIT_ARCHIVE_PARAMETERS_ONLY",
    "WER_SUBMIT_BYPASS_DATA_THROTTLING",
    "WER_SUBMIT_BYPASS_NETWORK_COST_THROTTLING",
    "WER_SUBMIT_BYPASS_POWER_THROTTLING",
    "WER_SUBMIT_FLAGS",
    "WER_SUBMIT_HONOR_RECOVERY",
    "WER_SUBMIT_HONOR_RESTART",
    "WER_SUBMIT_NO_ARCHIVE",
    "WER_SUBMIT_NO_CLOSE_UI",
    "WER_SUBMIT_NO_QUEUE",
    "WER_SUBMIT_OUTOFPROCESS",
    "WER_SUBMIT_OUTOFPROCESS_ASYNC",
    "WER_SUBMIT_QUEUE",
    "WER_SUBMIT_REPORT_MACHINE_ID",
    "WER_SUBMIT_RESULT",
    "WER_SUBMIT_RESULT_WerCustomAction",
    "WER_SUBMIT_RESULT_WerDisabled",
    "WER_SUBMIT_RESULT_WerDisabledQueue",
    "WER_SUBMIT_RESULT_WerReportAsync",
    "WER_SUBMIT_RESULT_WerReportCancelled",
    "WER_SUBMIT_RESULT_WerReportDebug",
    "WER_SUBMIT_RESULT_WerReportFailed",
    "WER_SUBMIT_RESULT_WerReportQueued",
    "WER_SUBMIT_RESULT_WerReportUploaded",
    "WER_SUBMIT_RESULT_WerReportUploadedCab",
    "WER_SUBMIT_RESULT_WerStorageLocationNotFound",
    "WER_SUBMIT_RESULT_WerSubmitResultMax",
    "WER_SUBMIT_RESULT_WerThrottled",
    "WER_SUBMIT_SHOW_DEBUG",
    "WER_SUBMIT_START_MINIMIZED",
    "WerAddExcludedApplication",
    "WerFreeString",
    "WerGetFlags",
    "WerRegisterAdditionalProcess",
    "WerRegisterAppLocalDump",
    "WerRegisterCustomMetadata",
    "WerRegisterExcludedMemoryBlock",
    "WerRegisterFile",
    "WerRegisterMemoryBlock",
    "WerRegisterRuntimeExceptionModule",
    "WerRemoveExcludedApplication",
    "WerReportAddDump",
    "WerReportAddFile",
    "WerReportCloseHandle",
    "WerReportCreate",
    "WerReportHang",
    "WerReportSetParameter",
    "WerReportSetUIOption",
    "WerReportSubmit",
    "WerSetFlags",
    "WerStoreClose",
    "WerStoreGetFirstReportKey",
    "WerStoreGetNextReportKey",
    "WerStoreGetReportCount",
    "WerStoreGetSizeOnDisk",
    "WerStoreOpen",
    "WerStorePurge",
    "WerStoreQueryReportMetadataV1",
    "WerStoreQueryReportMetadataV2",
    "WerStoreQueryReportMetadataV3",
    "WerStoreUploadReport",
    "WerUnregisterAdditionalProcess",
    "WerUnregisterAppLocalDump",
    "WerUnregisterCustomMetadata",
    "WerUnregisterExcludedMemoryBlock",
    "WerUnregisterFile",
    "WerUnregisterMemoryBlock",
    "WerUnregisterRuntimeExceptionModule",
    "pfn_ADDEREXCLUDEDAPPLICATIONA",
    "pfn_ADDEREXCLUDEDAPPLICATIONW",
    "pfn_REPORTFAULT",
]
_arch_optional = [
]
