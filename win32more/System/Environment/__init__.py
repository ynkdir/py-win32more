from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Environment
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
ENCLAVE_RUNTIME_POLICY_ALLOW_FULL_DEBUG = 1
ENCLAVE_RUNTIME_POLICY_ALLOW_DYNAMIC_DEBUG = 2
ENCLAVE_UNSEAL_FLAG_STALE_KEY = 1
ENCLAVE_FLAG_FULL_DEBUG_ENABLED = 1
ENCLAVE_FLAG_DYNAMIC_DEBUG_ENABLED = 2
ENCLAVE_FLAG_DYNAMIC_DEBUG_ACTIVE = 4
VBS_ENCLAVE_REPORT_PKG_HEADER_VERSION_CURRENT = 1
VBS_ENCLAVE_REPORT_SIGNATURE_SCHEME_SHA256_RSA_PSS_SHA256 = 1
VBS_ENCLAVE_REPORT_VERSION_CURRENT = 1
ENCLAVE_REPORT_DATA_LENGTH = 64
VBS_ENCLAVE_VARDATA_INVALID = 0
VBS_ENCLAVE_VARDATA_MODULE = 1
ENCLAVE_VBS_BASIC_KEY_FLAG_MEASUREMENT = 1
ENCLAVE_VBS_BASIC_KEY_FLAG_FAMILY_ID = 2
ENCLAVE_VBS_BASIC_KEY_FLAG_IMAGE_ID = 4
ENCLAVE_VBS_BASIC_KEY_FLAG_DEBUG_KEY = 8
def _define_SetEnvironmentStringsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('SetEnvironmentStringsW', windll['KERNEL32.dll']), ((1, 'NewEnvironment'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCommandLineA():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,)(('GetCommandLineA', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCommandLineW():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,)(('GetCommandLineW', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnvironmentStrings():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,)(('GetEnvironmentStrings', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnvironmentStringsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,)(('GetEnvironmentStringsW', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeEnvironmentStringsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('FreeEnvironmentStringsA', windll['KERNEL32.dll']), ((1, 'penv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeEnvironmentStringsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('FreeEnvironmentStringsW', windll['KERNEL32.dll']), ((1, 'penv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnvironmentVariableA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('GetEnvironmentVariableA', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnvironmentVariableW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('GetEnvironmentVariableW', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEnvironmentVariableA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('SetEnvironmentVariableA', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEnvironmentVariableW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('SetEnvironmentVariableW', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExpandEnvironmentStringsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('ExpandEnvironmentStringsA', windll['KERNEL32.dll']), ((1, 'lpSrc'),(1, 'lpDst'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExpandEnvironmentStringsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('ExpandEnvironmentStringsW', windll['KERNEL32.dll']), ((1, 'lpSrc'),(1, 'lpDst'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCurrentDirectoryA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('SetCurrentDirectoryA', windll['KERNEL32.dll']), ((1, 'lpPathName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCurrentDirectoryW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('SetCurrentDirectoryW', windll['KERNEL32.dll']), ((1, 'lpPathName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentDirectoryA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PSTR)(('GetCurrentDirectoryA', windll['KERNEL32.dll']), ((1, 'nBufferLength'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentDirectoryW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR)(('GetCurrentDirectoryW', windll['KERNEL32.dll']), ((1, 'nBufferLength'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NeedCurrentDirectoryForExePathA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('NeedCurrentDirectoryForExePathA', windll['KERNEL32.dll']), ((1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NeedCurrentDirectoryForExePathW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('NeedCurrentDirectoryForExePathW', windll['KERNEL32.dll']), ((1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateEnvironmentBlock():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(c_void_p),win32more.Foundation.HANDLE,win32more.Foundation.BOOL)(('CreateEnvironmentBlock', windll['USERENV.dll']), ((1, 'lpEnvironment'),(1, 'hToken'),(1, 'bInherit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DestroyEnvironmentBlock():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('DestroyEnvironmentBlock', windll['USERENV.dll']), ((1, 'lpEnvironment'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExpandEnvironmentStringsForUserA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('ExpandEnvironmentStringsForUserA', windll['USERENV.dll']), ((1, 'hToken'),(1, 'lpSrc'),(1, 'lpDest'),(1, 'dwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExpandEnvironmentStringsForUserW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('ExpandEnvironmentStringsForUserW', windll['USERENV.dll']), ((1, 'hToken'),(1, 'lpSrc'),(1, 'lpDest'),(1, 'dwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsEnclaveTypeSupported():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32)(('IsEnclaveTypeSupported', windll['KERNEL32.dll']), ((1, 'flEnclaveType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateEnclave():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,c_void_p,UIntPtr,UIntPtr,UInt32,c_void_p,UInt32,POINTER(UInt32))(('CreateEnclave', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'lpAddress'),(1, 'dwSize'),(1, 'dwInitialCommitment'),(1, 'flEnclaveType'),(1, 'lpEnclaveInformation'),(1, 'dwInfoLength'),(1, 'lpEnclaveError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadEnclaveData():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,c_void_p,UIntPtr,UInt32,c_void_p,UInt32,POINTER(UIntPtr),POINTER(UInt32))(('LoadEnclaveData', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'lpAddress'),(1, 'lpBuffer'),(1, 'nSize'),(1, 'flProtect'),(1, 'lpPageInformation'),(1, 'dwInfoLength'),(1, 'lpNumberOfBytesWritten'),(1, 'lpEnclaveError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitializeEnclave():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,c_void_p,UInt32,POINTER(UInt32))(('InitializeEnclave', windll['KERNEL32.dll']), ((1, 'hProcess'),(1, 'lpAddress'),(1, 'lpEnclaveInformation'),(1, 'dwInfoLength'),(1, 'lpEnclaveError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadEnclaveImageA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.Foundation.PSTR)(('LoadEnclaveImageA', windll['api-ms-win-core-enclave-l1-1-1.dll']), ((1, 'lpEnclaveAddress'),(1, 'lpImageName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadEnclaveImageW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.Foundation.PWSTR)(('LoadEnclaveImageW', windll['api-ms-win-core-enclave-l1-1-1.dll']), ((1, 'lpEnclaveAddress'),(1, 'lpImageName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CallEnclave():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,c_void_p,win32more.Foundation.BOOL,POINTER(c_void_p))(('CallEnclave', windll['vertdll.dll']), ((1, 'lpRoutine'),(1, 'lpParameter'),(1, 'fWaitForThread'),(1, 'lpReturnValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TerminateEnclave():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.Foundation.BOOL)(('TerminateEnclave', windll['vertdll.dll']), ((1, 'lpAddress'),(1, 'fWait'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteEnclave():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('DeleteEnclave', windll['api-ms-win-core-enclave-l1-1-1.dll']), ((1, 'lpAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnclaveGetAttestationReport():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,c_void_p,UInt32,POINTER(UInt32))(('EnclaveGetAttestationReport', windll['vertdll.dll']), ((1, 'EnclaveData'),(1, 'Report'),(1, 'BufferSize'),(1, 'OutputSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnclaveVerifyAttestationReport():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32)(('EnclaveVerifyAttestationReport', windll['vertdll.dll']), ((1, 'EnclaveType'),(1, 'Report'),(1, 'ReportSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnclaveSealData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.System.Environment.ENCLAVE_SEALING_IDENTITY_POLICY,UInt32,c_void_p,UInt32,POINTER(UInt32))(('EnclaveSealData', windll['vertdll.dll']), ((1, 'DataToEncrypt'),(1, 'DataToEncryptSize'),(1, 'IdentityPolicy'),(1, 'RuntimePolicy'),(1, 'ProtectedBlob'),(1, 'BufferSize'),(1, 'ProtectedBlobSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnclaveUnsealData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.System.Environment.ENCLAVE_IDENTITY_head),POINTER(UInt32))(('EnclaveUnsealData', windll['vertdll.dll']), ((1, 'ProtectedBlob'),(1, 'ProtectedBlobSize'),(1, 'DecryptedData'),(1, 'BufferSize'),(1, 'DecryptedDataSize'),(1, 'SealingIdentity'),(1, 'UnsealingFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnclaveGetEnclaveInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Environment.ENCLAVE_INFORMATION_head))(('EnclaveGetEnclaveInformation', windll['vertdll.dll']), ((1, 'InformationSize'),(1, 'EnclaveInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ENCLAVE_IDENTITY_head():
    class ENCLAVE_IDENTITY(Structure):
        pass
    return ENCLAVE_IDENTITY
def _define_ENCLAVE_IDENTITY():
    ENCLAVE_IDENTITY = win32more.System.Environment.ENCLAVE_IDENTITY_head
    ENCLAVE_IDENTITY._pack_ = 1
    ENCLAVE_IDENTITY._fields_ = [
        ('OwnerId', Byte * 32),
        ('UniqueId', Byte * 32),
        ('AuthorId', Byte * 32),
        ('FamilyId', Byte * 16),
        ('ImageId', Byte * 16),
        ('EnclaveSvn', UInt32),
        ('SecureKernelSvn', UInt32),
        ('PlatformSvn', UInt32),
        ('Flags', UInt32),
        ('SigningLevel', UInt32),
        ('EnclaveType', UInt32),
    ]
    return ENCLAVE_IDENTITY
def _define_ENCLAVE_INFORMATION_head():
    class ENCLAVE_INFORMATION(Structure):
        pass
    return ENCLAVE_INFORMATION
def _define_ENCLAVE_INFORMATION():
    ENCLAVE_INFORMATION = win32more.System.Environment.ENCLAVE_INFORMATION_head
    ENCLAVE_INFORMATION._fields_ = [
        ('EnclaveType', UInt32),
        ('Reserved', UInt32),
        ('BaseAddress', c_void_p),
        ('Size', UIntPtr),
        ('Identity', win32more.System.Environment.ENCLAVE_IDENTITY),
    ]
    return ENCLAVE_INFORMATION
ENCLAVE_SEALING_IDENTITY_POLICY = Int32
ENCLAVE_IDENTITY_POLICY_SEAL_INVALID = 0
ENCLAVE_IDENTITY_POLICY_SEAL_EXACT_CODE = 1
ENCLAVE_IDENTITY_POLICY_SEAL_SAME_PRIMARY_CODE = 2
ENCLAVE_IDENTITY_POLICY_SEAL_SAME_IMAGE = 3
ENCLAVE_IDENTITY_POLICY_SEAL_SAME_FAMILY = 4
ENCLAVE_IDENTITY_POLICY_SEAL_SAME_AUTHOR = 5
def _define_ENCLAVE_VBS_BASIC_KEY_REQUEST_head():
    class ENCLAVE_VBS_BASIC_KEY_REQUEST(Structure):
        pass
    return ENCLAVE_VBS_BASIC_KEY_REQUEST
def _define_ENCLAVE_VBS_BASIC_KEY_REQUEST():
    ENCLAVE_VBS_BASIC_KEY_REQUEST = win32more.System.Environment.ENCLAVE_VBS_BASIC_KEY_REQUEST_head
    ENCLAVE_VBS_BASIC_KEY_REQUEST._fields_ = [
        ('RequestSize', UInt32),
        ('Flags', UInt32),
        ('EnclaveSVN', UInt32),
        ('SystemKeyID', UInt32),
        ('CurrentSystemKeyID', UInt32),
    ]
    return ENCLAVE_VBS_BASIC_KEY_REQUEST
def _define_VBS_BASIC_ENCLAVE_BASIC_CALL_COMMIT_PAGES():
    return WINFUNCTYPE(Int32,c_void_p,UIntPtr,c_void_p,UInt32)
def _define_VBS_BASIC_ENCLAVE_BASIC_CALL_CREATE_THREAD():
    return WINFUNCTYPE(Int32,POINTER(win32more.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64_head))
def _define_VBS_BASIC_ENCLAVE_BASIC_CALL_DECOMMIT_PAGES():
    return WINFUNCTYPE(Int32,c_void_p,UIntPtr)
def _define_VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_KEY():
    return WINFUNCTYPE(Int32,POINTER(win32more.System.Environment.ENCLAVE_VBS_BASIC_KEY_REQUEST_head),UInt32,c_char_p_no)
def _define_VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_RANDOM_DATA():
    return WINFUNCTYPE(Int32,c_char_p_no,UInt32,POINTER(UInt64))
def _define_VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_REPORT():
    return WINFUNCTYPE(Int32,c_char_p_no,c_void_p,UInt32,POINTER(UInt32))
def _define_VBS_BASIC_ENCLAVE_BASIC_CALL_GET_ENCLAVE_INFORMATION():
    return WINFUNCTYPE(Int32,POINTER(win32more.System.Environment.ENCLAVE_INFORMATION_head))
def _define_VBS_BASIC_ENCLAVE_BASIC_CALL_INTERRUPT_THREAD():
    return WINFUNCTYPE(Int32,POINTER(win32more.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64_head))
def _define_VBS_BASIC_ENCLAVE_BASIC_CALL_PROTECT_PAGES():
    return WINFUNCTYPE(Int32,c_void_p,UIntPtr,UInt32)
def _define_VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_ENCLAVE():
    return WINFUNCTYPE(Void,UIntPtr)
def _define_VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_EXCEPTION():
    return WINFUNCTYPE(Int32,POINTER(win32more.System.Environment.VBS_BASIC_ENCLAVE_EXCEPTION_AMD64_head))
def _define_VBS_BASIC_ENCLAVE_BASIC_CALL_TERMINATE_THREAD():
    return WINFUNCTYPE(Int32,POINTER(win32more.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64_head))
def _define_VBS_BASIC_ENCLAVE_BASIC_CALL_VERIFY_REPORT():
    return WINFUNCTYPE(Int32,c_void_p,UInt32)
def _define_VBS_BASIC_ENCLAVE_EXCEPTION_AMD64_head():
    class VBS_BASIC_ENCLAVE_EXCEPTION_AMD64(Structure):
        pass
    return VBS_BASIC_ENCLAVE_EXCEPTION_AMD64
def _define_VBS_BASIC_ENCLAVE_EXCEPTION_AMD64():
    VBS_BASIC_ENCLAVE_EXCEPTION_AMD64 = win32more.System.Environment.VBS_BASIC_ENCLAVE_EXCEPTION_AMD64_head
    VBS_BASIC_ENCLAVE_EXCEPTION_AMD64._fields_ = [
        ('ExceptionCode', UInt32),
        ('NumberParameters', UInt32),
        ('ExceptionInformation', UIntPtr * 3),
        ('ExceptionRAX', UIntPtr),
        ('ExceptionRCX', UIntPtr),
        ('ExceptionRIP', UIntPtr),
        ('ExceptionRFLAGS', UIntPtr),
        ('ExceptionRSP', UIntPtr),
    ]
    return VBS_BASIC_ENCLAVE_EXCEPTION_AMD64
def _define_VBS_BASIC_ENCLAVE_SYSCALL_PAGE_head():
    class VBS_BASIC_ENCLAVE_SYSCALL_PAGE(Structure):
        pass
    return VBS_BASIC_ENCLAVE_SYSCALL_PAGE
def _define_VBS_BASIC_ENCLAVE_SYSCALL_PAGE():
    VBS_BASIC_ENCLAVE_SYSCALL_PAGE = win32more.System.Environment.VBS_BASIC_ENCLAVE_SYSCALL_PAGE_head
    VBS_BASIC_ENCLAVE_SYSCALL_PAGE._fields_ = [
        ('ReturnFromEnclave', win32more.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_ENCLAVE),
        ('ReturnFromException', win32more.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_EXCEPTION),
        ('TerminateThread', win32more.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_TERMINATE_THREAD),
        ('InterruptThread', win32more.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_INTERRUPT_THREAD),
        ('CommitPages', win32more.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_COMMIT_PAGES),
        ('DecommitPages', win32more.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_DECOMMIT_PAGES),
        ('ProtectPages', win32more.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_PROTECT_PAGES),
        ('CreateThread', win32more.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_CREATE_THREAD),
        ('GetEnclaveInformation', win32more.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_GET_ENCLAVE_INFORMATION),
        ('GenerateKey', win32more.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_KEY),
        ('GenerateReport', win32more.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_REPORT),
        ('VerifyReport', win32more.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_VERIFY_REPORT),
        ('GenerateRandomData', win32more.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_RANDOM_DATA),
    ]
    return VBS_BASIC_ENCLAVE_SYSCALL_PAGE
def _define_VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32_head():
    class VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32(Structure):
        pass
    return VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32
def _define_VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32():
    VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32 = win32more.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32_head
    VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32._fields_ = [
        ('ThreadContext', UInt32 * 4),
        ('EntryPoint', UInt32),
        ('StackPointer', UInt32),
        ('ExceptionEntryPoint', UInt32),
        ('ExceptionStack', UInt32),
        ('ExceptionActive', UInt32),
    ]
    return VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32
def _define_VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64_head():
    class VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64(Structure):
        pass
    return VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64
def _define_VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64():
    VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64 = win32more.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64_head
    VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64._fields_ = [
        ('ThreadContext', UInt64 * 4),
        ('EntryPoint', UInt64),
        ('StackPointer', UInt64),
        ('ExceptionEntryPoint', UInt64),
        ('ExceptionStack', UInt64),
        ('ExceptionActive', UInt32),
    ]
    return VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64
def _define_VBS_ENCLAVE_REPORT_head():
    class VBS_ENCLAVE_REPORT(Structure):
        pass
    return VBS_ENCLAVE_REPORT
def _define_VBS_ENCLAVE_REPORT():
    VBS_ENCLAVE_REPORT = win32more.System.Environment.VBS_ENCLAVE_REPORT_head
    VBS_ENCLAVE_REPORT._pack_ = 1
    VBS_ENCLAVE_REPORT._fields_ = [
        ('ReportSize', UInt32),
        ('ReportVersion', UInt32),
        ('EnclaveData', Byte * 64),
        ('EnclaveIdentity', win32more.System.Environment.ENCLAVE_IDENTITY),
    ]
    return VBS_ENCLAVE_REPORT
def _define_VBS_ENCLAVE_REPORT_MODULE_head():
    class VBS_ENCLAVE_REPORT_MODULE(Structure):
        pass
    return VBS_ENCLAVE_REPORT_MODULE
def _define_VBS_ENCLAVE_REPORT_MODULE():
    VBS_ENCLAVE_REPORT_MODULE = win32more.System.Environment.VBS_ENCLAVE_REPORT_MODULE_head
    VBS_ENCLAVE_REPORT_MODULE._pack_ = 1
    VBS_ENCLAVE_REPORT_MODULE._fields_ = [
        ('Header', win32more.System.Environment.VBS_ENCLAVE_REPORT_VARDATA_HEADER),
        ('UniqueId', Byte * 32),
        ('AuthorId', Byte * 32),
        ('FamilyId', Byte * 16),
        ('ImageId', Byte * 16),
        ('Svn', UInt32),
        ('ModuleName', Char * 1),
    ]
    return VBS_ENCLAVE_REPORT_MODULE
def _define_VBS_ENCLAVE_REPORT_PKG_HEADER_head():
    class VBS_ENCLAVE_REPORT_PKG_HEADER(Structure):
        pass
    return VBS_ENCLAVE_REPORT_PKG_HEADER
def _define_VBS_ENCLAVE_REPORT_PKG_HEADER():
    VBS_ENCLAVE_REPORT_PKG_HEADER = win32more.System.Environment.VBS_ENCLAVE_REPORT_PKG_HEADER_head
    VBS_ENCLAVE_REPORT_PKG_HEADER._pack_ = 1
    VBS_ENCLAVE_REPORT_PKG_HEADER._fields_ = [
        ('PackageSize', UInt32),
        ('Version', UInt32),
        ('SignatureScheme', UInt32),
        ('SignedStatementSize', UInt32),
        ('SignatureSize', UInt32),
        ('Reserved', UInt32),
    ]
    return VBS_ENCLAVE_REPORT_PKG_HEADER
def _define_VBS_ENCLAVE_REPORT_VARDATA_HEADER_head():
    class VBS_ENCLAVE_REPORT_VARDATA_HEADER(Structure):
        pass
    return VBS_ENCLAVE_REPORT_VARDATA_HEADER
def _define_VBS_ENCLAVE_REPORT_VARDATA_HEADER():
    VBS_ENCLAVE_REPORT_VARDATA_HEADER = win32more.System.Environment.VBS_ENCLAVE_REPORT_VARDATA_HEADER_head
    VBS_ENCLAVE_REPORT_VARDATA_HEADER._pack_ = 1
    VBS_ENCLAVE_REPORT_VARDATA_HEADER._fields_ = [
        ('DataType', UInt32),
        ('Size', UInt32),
    ]
    return VBS_ENCLAVE_REPORT_VARDATA_HEADER
__all__ = [
    "CallEnclave",
    "CreateEnclave",
    "CreateEnvironmentBlock",
    "DeleteEnclave",
    "DestroyEnvironmentBlock",
    "ENCLAVE_FLAG_DYNAMIC_DEBUG_ACTIVE",
    "ENCLAVE_FLAG_DYNAMIC_DEBUG_ENABLED",
    "ENCLAVE_FLAG_FULL_DEBUG_ENABLED",
    "ENCLAVE_IDENTITY",
    "ENCLAVE_IDENTITY_POLICY_SEAL_EXACT_CODE",
    "ENCLAVE_IDENTITY_POLICY_SEAL_INVALID",
    "ENCLAVE_IDENTITY_POLICY_SEAL_SAME_AUTHOR",
    "ENCLAVE_IDENTITY_POLICY_SEAL_SAME_FAMILY",
    "ENCLAVE_IDENTITY_POLICY_SEAL_SAME_IMAGE",
    "ENCLAVE_IDENTITY_POLICY_SEAL_SAME_PRIMARY_CODE",
    "ENCLAVE_INFORMATION",
    "ENCLAVE_REPORT_DATA_LENGTH",
    "ENCLAVE_RUNTIME_POLICY_ALLOW_DYNAMIC_DEBUG",
    "ENCLAVE_RUNTIME_POLICY_ALLOW_FULL_DEBUG",
    "ENCLAVE_SEALING_IDENTITY_POLICY",
    "ENCLAVE_UNSEAL_FLAG_STALE_KEY",
    "ENCLAVE_VBS_BASIC_KEY_FLAG_DEBUG_KEY",
    "ENCLAVE_VBS_BASIC_KEY_FLAG_FAMILY_ID",
    "ENCLAVE_VBS_BASIC_KEY_FLAG_IMAGE_ID",
    "ENCLAVE_VBS_BASIC_KEY_FLAG_MEASUREMENT",
    "ENCLAVE_VBS_BASIC_KEY_REQUEST",
    "EnclaveGetAttestationReport",
    "EnclaveGetEnclaveInformation",
    "EnclaveSealData",
    "EnclaveUnsealData",
    "EnclaveVerifyAttestationReport",
    "ExpandEnvironmentStringsA",
    "ExpandEnvironmentStringsForUserA",
    "ExpandEnvironmentStringsForUserW",
    "ExpandEnvironmentStringsW",
    "FreeEnvironmentStringsA",
    "FreeEnvironmentStringsW",
    "GetCommandLineA",
    "GetCommandLineW",
    "GetCurrentDirectoryA",
    "GetCurrentDirectoryW",
    "GetEnvironmentStrings",
    "GetEnvironmentStringsW",
    "GetEnvironmentVariableA",
    "GetEnvironmentVariableW",
    "InitializeEnclave",
    "IsEnclaveTypeSupported",
    "LoadEnclaveData",
    "LoadEnclaveImageA",
    "LoadEnclaveImageW",
    "NeedCurrentDirectoryForExePathA",
    "NeedCurrentDirectoryForExePathW",
    "SetCurrentDirectoryA",
    "SetCurrentDirectoryW",
    "SetEnvironmentStringsW",
    "SetEnvironmentVariableA",
    "SetEnvironmentVariableW",
    "TerminateEnclave",
    "VBS_BASIC_ENCLAVE_BASIC_CALL_COMMIT_PAGES",
    "VBS_BASIC_ENCLAVE_BASIC_CALL_CREATE_THREAD",
    "VBS_BASIC_ENCLAVE_BASIC_CALL_DECOMMIT_PAGES",
    "VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_KEY",
    "VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_RANDOM_DATA",
    "VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_REPORT",
    "VBS_BASIC_ENCLAVE_BASIC_CALL_GET_ENCLAVE_INFORMATION",
    "VBS_BASIC_ENCLAVE_BASIC_CALL_INTERRUPT_THREAD",
    "VBS_BASIC_ENCLAVE_BASIC_CALL_PROTECT_PAGES",
    "VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_ENCLAVE",
    "VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_EXCEPTION",
    "VBS_BASIC_ENCLAVE_BASIC_CALL_TERMINATE_THREAD",
    "VBS_BASIC_ENCLAVE_BASIC_CALL_VERIFY_REPORT",
    "VBS_BASIC_ENCLAVE_EXCEPTION_AMD64",
    "VBS_BASIC_ENCLAVE_SYSCALL_PAGE",
    "VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32",
    "VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64",
    "VBS_ENCLAVE_REPORT",
    "VBS_ENCLAVE_REPORT_MODULE",
    "VBS_ENCLAVE_REPORT_PKG_HEADER",
    "VBS_ENCLAVE_REPORT_PKG_HEADER_VERSION_CURRENT",
    "VBS_ENCLAVE_REPORT_SIGNATURE_SCHEME_SHA256_RSA_PSS_SHA256",
    "VBS_ENCLAVE_REPORT_VARDATA_HEADER",
    "VBS_ENCLAVE_REPORT_VERSION_CURRENT",
    "VBS_ENCLAVE_VARDATA_INVALID",
    "VBS_ENCLAVE_VARDATA_MODULE",
]
