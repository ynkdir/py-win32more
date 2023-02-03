from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Environment
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
ENCLAVE_RUNTIME_POLICY_ALLOW_FULL_DEBUG: UInt32 = 1
ENCLAVE_RUNTIME_POLICY_ALLOW_DYNAMIC_DEBUG: UInt32 = 2
ENCLAVE_UNSEAL_FLAG_STALE_KEY: UInt32 = 1
ENCLAVE_FLAG_FULL_DEBUG_ENABLED: UInt32 = 1
ENCLAVE_FLAG_DYNAMIC_DEBUG_ENABLED: UInt32 = 2
ENCLAVE_FLAG_DYNAMIC_DEBUG_ACTIVE: UInt32 = 4
VBS_ENCLAVE_REPORT_PKG_HEADER_VERSION_CURRENT: UInt32 = 1
VBS_ENCLAVE_REPORT_SIGNATURE_SCHEME_SHA256_RSA_PSS_SHA256: UInt32 = 1
VBS_ENCLAVE_REPORT_VERSION_CURRENT: UInt32 = 1
ENCLAVE_REPORT_DATA_LENGTH: UInt32 = 64
VBS_ENCLAVE_VARDATA_INVALID: UInt32 = 0
VBS_ENCLAVE_VARDATA_MODULE: UInt32 = 1
ENCLAVE_VBS_BASIC_KEY_FLAG_MEASUREMENT: UInt32 = 1
ENCLAVE_VBS_BASIC_KEY_FLAG_FAMILY_ID: UInt32 = 2
ENCLAVE_VBS_BASIC_KEY_FLAG_IMAGE_ID: UInt32 = 4
ENCLAVE_VBS_BASIC_KEY_FLAG_DEBUG_KEY: UInt32 = 8
@winfunctype('KERNEL32.dll')
def SetEnvironmentStringsW(NewEnvironment: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCommandLineA() -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('KERNEL32.dll')
def GetCommandLineW() -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('KERNEL32.dll')
def GetEnvironmentStrings() -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('KERNEL32.dll')
def GetEnvironmentStringsW() -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('KERNEL32.dll')
def FreeEnvironmentStringsA(penv: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FreeEnvironmentStringsW(penv: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetEnvironmentVariableA(lpName: Windows.Win32.Foundation.PSTR, lpBuffer: Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetEnvironmentVariableW(lpName: Windows.Win32.Foundation.PWSTR, lpBuffer: Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetEnvironmentVariableA(lpName: Windows.Win32.Foundation.PSTR, lpValue: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetEnvironmentVariableW(lpName: Windows.Win32.Foundation.PWSTR, lpValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ExpandEnvironmentStringsA(lpSrc: Windows.Win32.Foundation.PSTR, lpDst: Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ExpandEnvironmentStringsW(lpSrc: Windows.Win32.Foundation.PWSTR, lpDst: Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetCurrentDirectoryA(lpPathName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCurrentDirectoryW(lpPathName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCurrentDirectoryA(nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetCurrentDirectoryW(nBufferLength: UInt32, lpBuffer: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def NeedCurrentDirectoryForExePathA(ExeName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def NeedCurrentDirectoryForExePathW(ExeName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def CreateEnvironmentBlock(lpEnvironment: POINTER(c_void_p), hToken: Windows.Win32.Foundation.HANDLE, bInherit: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def DestroyEnvironmentBlock(lpEnvironment: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def ExpandEnvironmentStringsForUserA(hToken: Windows.Win32.Foundation.HANDLE, lpSrc: Windows.Win32.Foundation.PSTR, lpDest: Windows.Win32.Foundation.PSTR, dwSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def ExpandEnvironmentStringsForUserW(hToken: Windows.Win32.Foundation.HANDLE, lpSrc: Windows.Win32.Foundation.PWSTR, lpDest: Windows.Win32.Foundation.PWSTR, dwSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsEnclaveTypeSupported(flEnclaveType: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateEnclave(hProcess: Windows.Win32.Foundation.HANDLE, lpAddress: c_void_p, dwSize: UIntPtr, dwInitialCommitment: UIntPtr, flEnclaveType: UInt32, lpEnclaveInformation: c_void_p, dwInfoLength: UInt32, lpEnclaveError: POINTER(UInt32)) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def LoadEnclaveData(hProcess: Windows.Win32.Foundation.HANDLE, lpAddress: c_void_p, lpBuffer: c_void_p, nSize: UIntPtr, flProtect: UInt32, lpPageInformation: c_void_p, dwInfoLength: UInt32, lpNumberOfBytesWritten: POINTER(UIntPtr), lpEnclaveError: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeEnclave(hProcess: Windows.Win32.Foundation.HANDLE, lpAddress: c_void_p, lpEnclaveInformation: c_void_p, dwInfoLength: UInt32, lpEnclaveError: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-enclave-l1-1-1.dll')
def LoadEnclaveImageA(lpEnclaveAddress: c_void_p, lpImageName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-enclave-l1-1-1.dll')
def LoadEnclaveImageW(lpEnclaveAddress: c_void_p, lpImageName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('vertdll.dll')
def CallEnclave(lpRoutine: IntPtr, lpParameter: c_void_p, fWaitForThread: Windows.Win32.Foundation.BOOL, lpReturnValue: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('vertdll.dll')
def TerminateEnclave(lpAddress: c_void_p, fWait: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-enclave-l1-1-1.dll')
def DeleteEnclave(lpAddress: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('vertdll.dll')
def EnclaveGetAttestationReport(EnclaveData: c_char_p_no, Report: c_void_p, BufferSize: UInt32, OutputSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vertdll.dll')
def EnclaveVerifyAttestationReport(EnclaveType: UInt32, Report: c_void_p, ReportSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vertdll.dll')
def EnclaveSealData(DataToEncrypt: c_void_p, DataToEncryptSize: UInt32, IdentityPolicy: Windows.Win32.System.Environment.ENCLAVE_SEALING_IDENTITY_POLICY, RuntimePolicy: UInt32, ProtectedBlob: c_void_p, BufferSize: UInt32, ProtectedBlobSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vertdll.dll')
def EnclaveUnsealData(ProtectedBlob: c_void_p, ProtectedBlobSize: UInt32, DecryptedData: c_void_p, BufferSize: UInt32, DecryptedDataSize: POINTER(UInt32), SealingIdentity: POINTER(Windows.Win32.System.Environment.ENCLAVE_IDENTITY_head), UnsealingFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vertdll.dll')
def EnclaveGetEnclaveInformation(InformationSize: UInt32, EnclaveInformation: POINTER(Windows.Win32.System.Environment.ENCLAVE_INFORMATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ENCLAVE_IDENTITY(Structure):
    OwnerId: Byte * 32
    UniqueId: Byte * 32
    AuthorId: Byte * 32
    FamilyId: Byte * 16
    ImageId: Byte * 16
    EnclaveSvn: UInt32
    SecureKernelSvn: UInt32
    PlatformSvn: UInt32
    Flags: UInt32
    SigningLevel: UInt32
    EnclaveType: UInt32
    _pack_ = 1
class ENCLAVE_INFORMATION(Structure):
    EnclaveType: UInt32
    Reserved: UInt32
    BaseAddress: c_void_p
    Size: UIntPtr
    Identity: Windows.Win32.System.Environment.ENCLAVE_IDENTITY
ENCLAVE_SEALING_IDENTITY_POLICY = Int32
ENCLAVE_IDENTITY_POLICY_SEAL_INVALID: ENCLAVE_SEALING_IDENTITY_POLICY = 0
ENCLAVE_IDENTITY_POLICY_SEAL_EXACT_CODE: ENCLAVE_SEALING_IDENTITY_POLICY = 1
ENCLAVE_IDENTITY_POLICY_SEAL_SAME_PRIMARY_CODE: ENCLAVE_SEALING_IDENTITY_POLICY = 2
ENCLAVE_IDENTITY_POLICY_SEAL_SAME_IMAGE: ENCLAVE_SEALING_IDENTITY_POLICY = 3
ENCLAVE_IDENTITY_POLICY_SEAL_SAME_FAMILY: ENCLAVE_SEALING_IDENTITY_POLICY = 4
ENCLAVE_IDENTITY_POLICY_SEAL_SAME_AUTHOR: ENCLAVE_SEALING_IDENTITY_POLICY = 5
class ENCLAVE_VBS_BASIC_KEY_REQUEST(Structure):
    RequestSize: UInt32
    Flags: UInt32
    EnclaveSVN: UInt32
    SystemKeyID: UInt32
    CurrentSystemKeyID: UInt32
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_COMMIT_PAGES(EnclaveAddress: c_void_p, NumberOfBytes: UIntPtr, SourceAddress: c_void_p, PageProtection: UInt32) -> Int32: ...
if ARCH in 'X64,ARM64':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_CREATE_THREAD(ThreadDescriptor: POINTER(Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64_head)) -> Int32: ...
if ARCH in 'X86':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_CREATE_THREAD(ThreadDescriptor: POINTER(Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32_head)) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_DECOMMIT_PAGES(EnclaveAddress: c_void_p, NumberOfBytes: UIntPtr) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_KEY(KeyRequest: POINTER(Windows.Win32.System.Environment.ENCLAVE_VBS_BASIC_KEY_REQUEST_head), RequestedKeySize: UInt32, ReturnedKey: c_char_p_no) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_RANDOM_DATA(Buffer: c_char_p_no, NumberOfBytes: UInt32, Generation: POINTER(UInt64)) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_REPORT(EnclaveData: c_char_p_no, Report: c_void_p, BufferSize: UInt32, OutputSize: POINTER(UInt32)) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_GET_ENCLAVE_INFORMATION(EnclaveInfo: POINTER(Windows.Win32.System.Environment.ENCLAVE_INFORMATION_head)) -> Int32: ...
if ARCH in 'X64,ARM64':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_INTERRUPT_THREAD(ThreadDescriptor: POINTER(Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64_head)) -> Int32: ...
if ARCH in 'X86':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_INTERRUPT_THREAD(ThreadDescriptor: POINTER(Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32_head)) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_PROTECT_PAGES(EnclaveAddress: c_void_p, NumberOfytes: UIntPtr, PageProtection: UInt32) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_ENCLAVE(ReturnValue: UIntPtr) -> Void: ...
if ARCH in 'X64':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_EXCEPTION(ExceptionRecord: POINTER(Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_EXCEPTION_AMD64_head)) -> Int32: ...
if ARCH in 'X86,ARM64':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_EXCEPTION(ExceptionRecord: c_void_p) -> Int32: ...
if ARCH in 'X64,ARM64':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_TERMINATE_THREAD(ThreadDescriptor: POINTER(Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64_head)) -> Int32: ...
if ARCH in 'X86':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_TERMINATE_THREAD(ThreadDescriptor: POINTER(Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32_head)) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_VERIFY_REPORT(Report: c_void_p, ReportSize: UInt32) -> Int32: ...
class VBS_BASIC_ENCLAVE_EXCEPTION_AMD64(Structure):
    ExceptionCode: UInt32
    NumberParameters: UInt32
    ExceptionInformation: UIntPtr * 3
    ExceptionRAX: UIntPtr
    ExceptionRCX: UIntPtr
    ExceptionRIP: UIntPtr
    ExceptionRFLAGS: UIntPtr
    ExceptionRSP: UIntPtr
class VBS_BASIC_ENCLAVE_SYSCALL_PAGE(Structure):
    ReturnFromEnclave: Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_ENCLAVE
    ReturnFromException: Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_EXCEPTION
    TerminateThread: Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_TERMINATE_THREAD
    InterruptThread: Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_INTERRUPT_THREAD
    CommitPages: Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_COMMIT_PAGES
    DecommitPages: Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_DECOMMIT_PAGES
    ProtectPages: Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_PROTECT_PAGES
    CreateThread: Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_CREATE_THREAD
    GetEnclaveInformation: Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_GET_ENCLAVE_INFORMATION
    GenerateKey: Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_KEY
    GenerateReport: Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_REPORT
    VerifyReport: Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_VERIFY_REPORT
    GenerateRandomData: Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_RANDOM_DATA
class VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32(Structure):
    ThreadContext: UInt32 * 4
    EntryPoint: UInt32
    StackPointer: UInt32
    ExceptionEntryPoint: UInt32
    ExceptionStack: UInt32
    ExceptionActive: UInt32
class VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64(Structure):
    ThreadContext: UInt64 * 4
    EntryPoint: UInt64
    StackPointer: UInt64
    ExceptionEntryPoint: UInt64
    ExceptionStack: UInt64
    ExceptionActive: UInt32
class VBS_ENCLAVE_REPORT(Structure):
    ReportSize: UInt32
    ReportVersion: UInt32
    EnclaveData: Byte * 64
    EnclaveIdentity: Windows.Win32.System.Environment.ENCLAVE_IDENTITY
    _pack_ = 1
class VBS_ENCLAVE_REPORT_MODULE(Structure):
    Header: Windows.Win32.System.Environment.VBS_ENCLAVE_REPORT_VARDATA_HEADER
    UniqueId: Byte * 32
    AuthorId: Byte * 32
    FamilyId: Byte * 16
    ImageId: Byte * 16
    Svn: UInt32
    ModuleName: Char * 1
    _pack_ = 1
class VBS_ENCLAVE_REPORT_PKG_HEADER(Structure):
    PackageSize: UInt32
    Version: UInt32
    SignatureScheme: UInt32
    SignedStatementSize: UInt32
    SignatureSize: UInt32
    Reserved: UInt32
    _pack_ = 1
class VBS_ENCLAVE_REPORT_VARDATA_HEADER(Structure):
    DataType: UInt32
    Size: UInt32
    _pack_ = 1
make_head(_module, 'ENCLAVE_IDENTITY')
make_head(_module, 'ENCLAVE_INFORMATION')
make_head(_module, 'ENCLAVE_VBS_BASIC_KEY_REQUEST')
make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_COMMIT_PAGES')
if ARCH in 'X64,ARM64':
    make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_CREATE_THREAD')
if ARCH in 'X86':
    make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_CREATE_THREAD')
make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_DECOMMIT_PAGES')
make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_KEY')
make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_RANDOM_DATA')
make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_REPORT')
make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_GET_ENCLAVE_INFORMATION')
if ARCH in 'X64,ARM64':
    make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_INTERRUPT_THREAD')
if ARCH in 'X86':
    make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_INTERRUPT_THREAD')
make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_PROTECT_PAGES')
make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_ENCLAVE')
if ARCH in 'X64':
    make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_EXCEPTION')
if ARCH in 'X86,ARM64':
    make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_EXCEPTION')
if ARCH in 'X64,ARM64':
    make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_TERMINATE_THREAD')
if ARCH in 'X86':
    make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_TERMINATE_THREAD')
make_head(_module, 'VBS_BASIC_ENCLAVE_BASIC_CALL_VERIFY_REPORT')
make_head(_module, 'VBS_BASIC_ENCLAVE_EXCEPTION_AMD64')
make_head(_module, 'VBS_BASIC_ENCLAVE_SYSCALL_PAGE')
make_head(_module, 'VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32')
make_head(_module, 'VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64')
make_head(_module, 'VBS_ENCLAVE_REPORT')
make_head(_module, 'VBS_ENCLAVE_REPORT_MODULE')
make_head(_module, 'VBS_ENCLAVE_REPORT_PKG_HEADER')
make_head(_module, 'VBS_ENCLAVE_REPORT_VARDATA_HEADER')
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
_arch_optional = [
]
