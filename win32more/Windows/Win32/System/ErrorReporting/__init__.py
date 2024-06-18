from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Diagnostics.Debug
import win32more.Windows.Win32.System.ErrorReporting
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
def WerReportCreate(pwzEventType: win32more.Windows.Win32.Foundation.PWSTR, repType: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_TYPE, pReportInformation: POINTER(win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_INFORMATION), phReportHandle: POINTER(win32more.Windows.Win32.System.ErrorReporting.HREPORT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerReportSetParameter(hReportHandle: win32more.Windows.Win32.System.ErrorReporting.HREPORT, dwparamID: UInt32, pwzName: win32more.Windows.Win32.Foundation.PWSTR, pwzValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerReportAddFile(hReportHandle: win32more.Windows.Win32.System.ErrorReporting.HREPORT, pwzPath: win32more.Windows.Win32.Foundation.PWSTR, repFileType: win32more.Windows.Win32.System.ErrorReporting.WER_FILE_TYPE, dwFileFlags: win32more.Windows.Win32.System.ErrorReporting.WER_FILE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerReportSetUIOption(hReportHandle: win32more.Windows.Win32.System.ErrorReporting.HREPORT, repUITypeID: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_UI, pwzValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerReportSubmit(hReportHandle: win32more.Windows.Win32.System.ErrorReporting.HREPORT, consent: win32more.Windows.Win32.System.ErrorReporting.WER_CONSENT, dwFlags: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS, pSubmitResult: POINTER(win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerReportAddDump(hReportHandle: win32more.Windows.Win32.System.ErrorReporting.HREPORT, hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE, dumpType: win32more.Windows.Win32.System.ErrorReporting.WER_DUMP_TYPE, pExceptionParam: POINTER(win32more.Windows.Win32.System.ErrorReporting.WER_EXCEPTION_INFORMATION), pDumpCustomOptions: POINTER(win32more.Windows.Win32.System.ErrorReporting.WER_DUMP_CUSTOM_OPTIONS), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerReportCloseHandle(hReportHandle: win32more.Windows.Win32.System.ErrorReporting.HREPORT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterFile(pwzFile: win32more.Windows.Win32.Foundation.PWSTR, regFileType: win32more.Windows.Win32.System.ErrorReporting.WER_REGISTER_FILE_TYPE, dwFlags: win32more.Windows.Win32.System.ErrorReporting.WER_FILE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterFile(pwzFilePath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterMemoryBlock(pvAddress: VoidPtr, dwSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterMemoryBlock(pvAddress: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterExcludedMemoryBlock(address: VoidPtr, size: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterExcludedMemoryBlock(address: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterCustomMetadata(key: win32more.Windows.Win32.Foundation.PWSTR, value: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterCustomMetadata(key: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterAdditionalProcess(processId: UInt32, captureExtraInfoForThreadId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterAdditionalProcess(processId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterAppLocalDump(localAppDataRelativePath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterAppLocalDump() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerSetFlags(dwFlags: win32more.Windows.Win32.System.ErrorReporting.WER_FAULT_REPORTING) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerGetFlags(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pdwFlags: POINTER(win32more.Windows.Win32.System.ErrorReporting.WER_FAULT_REPORTING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerAddExcludedApplication(pwzExeName: win32more.Windows.Win32.Foundation.PWSTR, bAllUsers: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerRemoveExcludedApplication(pwzExeName: win32more.Windows.Win32.Foundation.PWSTR, bAllUsers: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerRegisterRuntimeExceptionModule(pwszOutOfProcessCallbackDll: win32more.Windows.Win32.Foundation.PWSTR, pContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def WerUnregisterRuntimeExceptionModule(pwszOutOfProcessCallbackDll: win32more.Windows.Win32.Foundation.PWSTR, pContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreOpen(repStoreType: win32more.Windows.Win32.System.ErrorReporting.REPORT_STORE_TYPES, phReportStore: POINTER(win32more.Windows.Win32.System.ErrorReporting.HREPORTSTORE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreClose(hReportStore: win32more.Windows.Win32.System.ErrorReporting.HREPORTSTORE) -> Void: ...
@winfunctype('wer.dll')
def WerStoreGetFirstReportKey(hReportStore: win32more.Windows.Win32.System.ErrorReporting.HREPORTSTORE, ppszReportKey: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreGetNextReportKey(hReportStore: win32more.Windows.Win32.System.ErrorReporting.HREPORTSTORE, ppszReportKey: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreQueryReportMetadataV2(hReportStore: win32more.Windows.Win32.System.ErrorReporting.HREPORTSTORE, pszReportKey: win32more.Windows.Win32.Foundation.PWSTR, pReportMetadata: POINTER(win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_METADATA_V2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreQueryReportMetadataV3(hReportStore: win32more.Windows.Win32.System.ErrorReporting.HREPORTSTORE, pszReportKey: win32more.Windows.Win32.Foundation.PWSTR, pReportMetadata: POINTER(win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_METADATA_V3)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerFreeString(pwszStr: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('wer.dll')
def WerStorePurge() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreGetReportCount(hReportStore: win32more.Windows.Win32.System.ErrorReporting.HREPORTSTORE, pdwReportCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreGetSizeOnDisk(hReportStore: win32more.Windows.Win32.System.ErrorReporting.HREPORTSTORE, pqwSizeInBytes: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreQueryReportMetadataV1(hReportStore: win32more.Windows.Win32.System.ErrorReporting.HREPORTSTORE, pszReportKey: win32more.Windows.Win32.Foundation.PWSTR, pReportMetadata: POINTER(win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_METADATA_V1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('wer.dll')
def WerStoreUploadReport(hReportStore: win32more.Windows.Win32.System.ErrorReporting.HREPORTSTORE, pszReportKey: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, pSubmitResult: POINTER(win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('faultrep.dll')
def ReportFault(pep: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS), dwOpt: UInt32) -> win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal: ...
@winfunctype('faultrep.dll')
def AddERExcludedApplicationA(szApplication: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('faultrep.dll')
def AddERExcludedApplicationW(wszApplication: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
AddERExcludedApplication = UnicodeAlias('AddERExcludedApplicationW')
@winfunctype('faultrep.dll')
def WerReportHang(hwndHungApp: win32more.Windows.Win32.Foundation.HWND, pwzHungApplicationName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
EFaultRepRetVal = Int32
frrvOk: win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal = 0
frrvOkManifest: win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal = 1
frrvOkQueued: win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal = 2
frrvErr: win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal = 3
frrvErrNoDW: win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal = 4
frrvErrTimeout: win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal = 5
frrvLaunchDebugger: win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal = 6
frrvOkHeadless: win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal = 7
frrvErrAnotherInstance: win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal = 8
frrvErrNoMemory: win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal = 9
frrvErrDoubleFault: win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal = 10
HREPORT = VoidPtr
HREPORTSTORE = VoidPtr
@winfunctype_pointer
def PFN_WER_RUNTIME_EXCEPTION_DEBUGGER_LAUNCH(pContext: VoidPtr, pExceptionInformation: POINTER(win32more.Windows.Win32.System.ErrorReporting.WER_RUNTIME_EXCEPTION_INFORMATION), pbIsCustomDebugger: POINTER(win32more.Windows.Win32.Foundation.BOOL), pwszDebuggerLaunch: win32more.Windows.Win32.Foundation.PWSTR, pchDebuggerLaunch: POINTER(UInt32), pbIsDebuggerAutolaunch: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_WER_RUNTIME_EXCEPTION_EVENT(pContext: VoidPtr, pExceptionInformation: POINTER(win32more.Windows.Win32.System.ErrorReporting.WER_RUNTIME_EXCEPTION_INFORMATION), pbOwnershipClaimed: POINTER(win32more.Windows.Win32.Foundation.BOOL), pwszEventName: win32more.Windows.Win32.Foundation.PWSTR, pchSize: POINTER(UInt32), pdwSignatureCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFN_WER_RUNTIME_EXCEPTION_EVENT_SIGNATURE(pContext: VoidPtr, pExceptionInformation: POINTER(win32more.Windows.Win32.System.ErrorReporting.WER_RUNTIME_EXCEPTION_INFORMATION), dwIndex: UInt32, pwszName: win32more.Windows.Win32.Foundation.PWSTR, pchName: POINTER(UInt32), pwszValue: win32more.Windows.Win32.Foundation.PWSTR, pchValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
REPORT_STORE_TYPES = Int32
E_STORE_USER_ARCHIVE: win32more.Windows.Win32.System.ErrorReporting.REPORT_STORE_TYPES = 0
E_STORE_USER_QUEUE: win32more.Windows.Win32.System.ErrorReporting.REPORT_STORE_TYPES = 1
E_STORE_MACHINE_ARCHIVE: win32more.Windows.Win32.System.ErrorReporting.REPORT_STORE_TYPES = 2
E_STORE_MACHINE_QUEUE: win32more.Windows.Win32.System.ErrorReporting.REPORT_STORE_TYPES = 3
E_STORE_INVALID: win32more.Windows.Win32.System.ErrorReporting.REPORT_STORE_TYPES = 4
WER_CONSENT = Int32
WerConsentNotAsked: win32more.Windows.Win32.System.ErrorReporting.WER_CONSENT = 1
WerConsentApproved: win32more.Windows.Win32.System.ErrorReporting.WER_CONSENT = 2
WerConsentDenied: win32more.Windows.Win32.System.ErrorReporting.WER_CONSENT = 3
WerConsentAlwaysPrompt: win32more.Windows.Win32.System.ErrorReporting.WER_CONSENT = 4
WerConsentMax: win32more.Windows.Win32.System.ErrorReporting.WER_CONSENT = 5
class WER_DUMP_CUSTOM_OPTIONS(Structure):
    dwSize: UInt32
    dwMask: UInt32
    dwDumpFlags: UInt32
    bOnlyThisThread: win32more.Windows.Win32.Foundation.BOOL
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
    bOnlyThisThread: win32more.Windows.Win32.Foundation.BOOL
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
    bOnlyThisThread: win32more.Windows.Win32.Foundation.BOOL
    dwExceptionThreadFlags: UInt32
    dwOtherThreadFlags: UInt32
    dwExceptionThreadExFlags: UInt32
    dwOtherThreadExFlags: UInt32
    dwPreferredModuleFlags: UInt32
    dwOtherModuleFlags: UInt32
    wzPreferredModuleList: Char * 256
    dwPreferredModuleResetFlags: UInt32
    dwOtherModuleResetFlags: UInt32
    pvDumpKey: VoidPtr
    hSnapshot: win32more.Windows.Win32.Foundation.HANDLE
    dwThreadID: UInt32
WER_DUMP_TYPE = Int32
WerDumpTypeNone: win32more.Windows.Win32.System.ErrorReporting.WER_DUMP_TYPE = 0
WerDumpTypeMicroDump: win32more.Windows.Win32.System.ErrorReporting.WER_DUMP_TYPE = 1
WerDumpTypeMiniDump: win32more.Windows.Win32.System.ErrorReporting.WER_DUMP_TYPE = 2
WerDumpTypeHeapDump: win32more.Windows.Win32.System.ErrorReporting.WER_DUMP_TYPE = 3
WerDumpTypeTriageDump: win32more.Windows.Win32.System.ErrorReporting.WER_DUMP_TYPE = 4
WerDumpTypeMax: win32more.Windows.Win32.System.ErrorReporting.WER_DUMP_TYPE = 5
class WER_EXCEPTION_INFORMATION(Structure):
    pExceptionPointers: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS)
    bClientPointers: win32more.Windows.Win32.Foundation.BOOL
WER_FAULT_REPORTING = UInt32
WER_FAULT_REPORTING_FLAG_DISABLE_THREAD_SUSPENSION: win32more.Windows.Win32.System.ErrorReporting.WER_FAULT_REPORTING = 4
WER_FAULT_REPORTING_FLAG_NOHEAP: win32more.Windows.Win32.System.ErrorReporting.WER_FAULT_REPORTING = 1
WER_FAULT_REPORTING_FLAG_QUEUE: win32more.Windows.Win32.System.ErrorReporting.WER_FAULT_REPORTING = 2
WER_FAULT_REPORTING_FLAG_QUEUE_UPLOAD: win32more.Windows.Win32.System.ErrorReporting.WER_FAULT_REPORTING = 8
WER_FAULT_REPORTING_ALWAYS_SHOW_UI: win32more.Windows.Win32.System.ErrorReporting.WER_FAULT_REPORTING = 16
WER_FILE = UInt32
WER_FILE_ANONYMOUS_DATA: win32more.Windows.Win32.System.ErrorReporting.WER_FILE = 2
WER_FILE_DELETE_WHEN_DONE: win32more.Windows.Win32.System.ErrorReporting.WER_FILE = 1
WER_FILE_TYPE = Int32
WerFileTypeMicrodump: win32more.Windows.Win32.System.ErrorReporting.WER_FILE_TYPE = 1
WerFileTypeMinidump: win32more.Windows.Win32.System.ErrorReporting.WER_FILE_TYPE = 2
WerFileTypeHeapdump: win32more.Windows.Win32.System.ErrorReporting.WER_FILE_TYPE = 3
WerFileTypeUserDocument: win32more.Windows.Win32.System.ErrorReporting.WER_FILE_TYPE = 4
WerFileTypeOther: win32more.Windows.Win32.System.ErrorReporting.WER_FILE_TYPE = 5
WerFileTypeTriagedump: win32more.Windows.Win32.System.ErrorReporting.WER_FILE_TYPE = 6
WerFileTypeCustomDump: win32more.Windows.Win32.System.ErrorReporting.WER_FILE_TYPE = 7
WerFileTypeAuxiliaryDump: win32more.Windows.Win32.System.ErrorReporting.WER_FILE_TYPE = 8
WerFileTypeEtlTrace: win32more.Windows.Win32.System.ErrorReporting.WER_FILE_TYPE = 9
WerFileTypeMax: win32more.Windows.Win32.System.ErrorReporting.WER_FILE_TYPE = 10
WER_REGISTER_FILE_TYPE = Int32
WerRegFileTypeUserDocument: win32more.Windows.Win32.System.ErrorReporting.WER_REGISTER_FILE_TYPE = 1
WerRegFileTypeOther: win32more.Windows.Win32.System.ErrorReporting.WER_REGISTER_FILE_TYPE = 2
WerRegFileTypeMax: win32more.Windows.Win32.System.ErrorReporting.WER_REGISTER_FILE_TYPE = 3
class WER_REPORT_INFORMATION(Structure):
    dwSize: UInt32
    hProcess: win32more.Windows.Win32.Foundation.HANDLE
    wzConsentKey: Char * 64
    wzFriendlyEventName: Char * 128
    wzApplicationName: Char * 128
    wzApplicationPath: Char * 260
    wzDescription: Char * 512
    hwndParent: win32more.Windows.Win32.Foundation.HWND
class WER_REPORT_INFORMATION_V3(Structure):
    dwSize: UInt32
    hProcess: win32more.Windows.Win32.Foundation.HANDLE
    wzConsentKey: Char * 64
    wzFriendlyEventName: Char * 128
    wzApplicationName: Char * 128
    wzApplicationPath: Char * 260
    wzDescription: Char * 512
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    wzNamespacePartner: Char * 64
    wzNamespaceGroup: Char * 64
class WER_REPORT_INFORMATION_V4(Structure):
    dwSize: UInt32
    hProcess: win32more.Windows.Win32.Foundation.HANDLE
    wzConsentKey: Char * 64
    wzFriendlyEventName: Char * 128
    wzApplicationName: Char * 128
    wzApplicationPath: Char * 260
    wzDescription: Char * 512
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    wzNamespacePartner: Char * 64
    wzNamespaceGroup: Char * 64
    rgbApplicationIdentity: Byte * 16
    hSnapshot: win32more.Windows.Win32.Foundation.HANDLE
    hDeleteFilesImpersonationToken: win32more.Windows.Win32.Foundation.HANDLE
class WER_REPORT_INFORMATION_V5(Structure):
    dwSize: UInt32
    hProcess: win32more.Windows.Win32.Foundation.HANDLE
    wzConsentKey: Char * 64
    wzFriendlyEventName: Char * 128
    wzApplicationName: Char * 128
    wzApplicationPath: Char * 260
    wzDescription: Char * 512
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    wzNamespacePartner: Char * 64
    wzNamespaceGroup: Char * 64
    rgbApplicationIdentity: Byte * 16
    hSnapshot: win32more.Windows.Win32.Foundation.HANDLE
    hDeleteFilesImpersonationToken: win32more.Windows.Win32.Foundation.HANDLE
    submitResultMax: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT
class WER_REPORT_METADATA_V1(Structure):
    Signature: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_SIGNATURE
    BucketId: Guid
    ReportId: Guid
    CreationTime: win32more.Windows.Win32.Foundation.FILETIME
    SizeInBytes: UInt64
class WER_REPORT_METADATA_V2(Structure):
    Signature: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_SIGNATURE
    BucketId: Guid
    ReportId: Guid
    CreationTime: win32more.Windows.Win32.Foundation.FILETIME
    SizeInBytes: UInt64
    CabId: Char * 260
    ReportStatus: UInt32
    ReportIntegratorId: Guid
    NumberOfFiles: UInt32
    SizeOfFileNames: UInt32
    FileNames: win32more.Windows.Win32.Foundation.PWSTR
class WER_REPORT_METADATA_V3(Structure):
    Signature: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_SIGNATURE
    BucketId: Guid
    ReportId: Guid
    CreationTime: win32more.Windows.Win32.Foundation.FILETIME
    SizeInBytes: UInt64
    CabId: Char * 260
    ReportStatus: UInt32
    ReportIntegratorId: Guid
    NumberOfFiles: UInt32
    SizeOfFileNames: UInt32
    FileNames: win32more.Windows.Win32.Foundation.PWSTR
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
    Parameters: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_PARAMETER * 10
WER_REPORT_TYPE = Int32
WerReportNonCritical: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_TYPE = 0
WerReportCritical: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_TYPE = 1
WerReportApplicationCrash: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_TYPE = 2
WerReportApplicationHang: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_TYPE = 3
WerReportKernel: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_TYPE = 4
WerReportInvalid: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_TYPE = 5
WER_REPORT_UI = Int32
WerUIAdditionalDataDlgHeader: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_UI = 1
WerUIIconFilePath: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_UI = 2
WerUIConsentDlgHeader: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_UI = 3
WerUIConsentDlgBody: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_UI = 4
WerUIOnlineSolutionCheckText: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_UI = 5
WerUIOfflineSolutionCheckText: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_UI = 6
WerUICloseText: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_UI = 7
WerUICloseDlgHeader: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_UI = 8
WerUICloseDlgBody: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_UI = 9
WerUICloseDlgButtonText: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_UI = 10
WerUIMax: win32more.Windows.Win32.System.ErrorReporting.WER_REPORT_UI = 11
class WER_RUNTIME_EXCEPTION_INFORMATION(Structure):
    dwSize: UInt32
    hProcess: win32more.Windows.Win32.Foundation.HANDLE
    hThread: win32more.Windows.Win32.Foundation.HANDLE
    exceptionRecord: win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD
    context: win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT
    pwszReportId: win32more.Windows.Win32.Foundation.PWSTR
    bIsFatal: win32more.Windows.Win32.Foundation.BOOL
    dwReserved: UInt32
WER_SUBMIT_FLAGS = UInt32
WER_SUBMIT_ADD_REGISTERED_DATA: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 16
WER_SUBMIT_HONOR_RECOVERY: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 1
WER_SUBMIT_HONOR_RESTART: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 2
WER_SUBMIT_NO_ARCHIVE: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 256
WER_SUBMIT_NO_CLOSE_UI: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 64
WER_SUBMIT_NO_QUEUE: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 128
WER_SUBMIT_OUTOFPROCESS: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 32
WER_SUBMIT_OUTOFPROCESS_ASYNC: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 1024
WER_SUBMIT_QUEUE: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 4
WER_SUBMIT_SHOW_DEBUG: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 8
WER_SUBMIT_START_MINIMIZED: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 512
WER_SUBMIT_BYPASS_DATA_THROTTLING: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 2048
WER_SUBMIT_ARCHIVE_PARAMETERS_ONLY: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 4096
WER_SUBMIT_REPORT_MACHINE_ID: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_FLAGS = 8192
WER_SUBMIT_RESULT = Int32
WerReportQueued: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT = 1
WerReportUploaded: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT = 2
WerReportDebug: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT = 3
WerReportFailed: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT = 4
WerDisabled: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT = 5
WerReportCancelled: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT = 6
WerDisabledQueue: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT = 7
WerReportAsync: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT = 8
WerCustomAction: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT = 9
WerThrottled: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT = 10
WerReportUploadedCab: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT = 11
WerStorageLocationNotFound: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT = 12
WerSubmitResultMax: win32more.Windows.Win32.System.ErrorReporting.WER_SUBMIT_RESULT = 13
@winfunctype_pointer
def pfn_ADDEREXCLUDEDAPPLICATIONA(param0: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal: ...
@winfunctype_pointer
def pfn_ADDEREXCLUDEDAPPLICATIONW(param0: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal: ...
pfn_ADDEREXCLUDEDAPPLICATION = UnicodeAlias('pfn_ADDEREXCLUDEDAPPLICATIONW')
@winfunctype_pointer
def pfn_REPORTFAULT(param0: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_POINTERS), param1: UInt32) -> win32more.Windows.Win32.System.ErrorReporting.EFaultRepRetVal: ...


make_ready(__name__)
