from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Environment
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
def SetEnvironmentStringsW(NewEnvironment: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetEnvironmentStrings = UnicodeAlias('SetEnvironmentStringsW')
@winfunctype('KERNEL32.dll')
def GetCommandLineA() -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('KERNEL32.dll')
def GetCommandLineW() -> win32more.Windows.Win32.Foundation.PWSTR: ...
GetCommandLine = UnicodeAlias('GetCommandLineW')
@winfunctype('KERNEL32.dll')
def GetEnvironmentStringsW() -> win32more.Windows.Win32.Foundation.PWSTR: ...
GetEnvironmentStrings = UnicodeAlias('GetEnvironmentStringsW')
@winfunctype('KERNEL32.dll')
def FreeEnvironmentStringsA(penv: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FreeEnvironmentStringsW(penv: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
FreeEnvironmentStrings = UnicodeAlias('FreeEnvironmentStringsW')
@winfunctype('KERNEL32.dll')
def GetEnvironmentVariableA(lpName: win32more.Windows.Win32.Foundation.PSTR, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetEnvironmentVariableW(lpName: win32more.Windows.Win32.Foundation.PWSTR, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
GetEnvironmentVariable = UnicodeAlias('GetEnvironmentVariableW')
@winfunctype('KERNEL32.dll')
def SetEnvironmentVariableA(lpName: win32more.Windows.Win32.Foundation.PSTR, lpValue: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetEnvironmentVariableW(lpName: win32more.Windows.Win32.Foundation.PWSTR, lpValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetEnvironmentVariable = UnicodeAlias('SetEnvironmentVariableW')
@winfunctype('KERNEL32.dll')
def ExpandEnvironmentStringsA(lpSrc: win32more.Windows.Win32.Foundation.PSTR, lpDst: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ExpandEnvironmentStringsW(lpSrc: win32more.Windows.Win32.Foundation.PWSTR, lpDst: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
ExpandEnvironmentStrings = UnicodeAlias('ExpandEnvironmentStringsW')
@winfunctype('KERNEL32.dll')
def SetCurrentDirectoryA(lpPathName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCurrentDirectoryW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetCurrentDirectory = UnicodeAlias('SetCurrentDirectoryW')
@winfunctype('KERNEL32.dll')
def GetCurrentDirectoryA(nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetCurrentDirectoryW(nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
GetCurrentDirectory = UnicodeAlias('GetCurrentDirectoryW')
@winfunctype('KERNEL32.dll')
def NeedCurrentDirectoryForExePathA(ExeName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def NeedCurrentDirectoryForExePathW(ExeName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
NeedCurrentDirectoryForExePath = UnicodeAlias('NeedCurrentDirectoryForExePathW')
@winfunctype('USERENV.dll')
def CreateEnvironmentBlock(lpEnvironment: POINTER(VoidPtr), hToken: win32more.Windows.Win32.Foundation.HANDLE, bInherit: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def DestroyEnvironmentBlock(lpEnvironment: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def ExpandEnvironmentStringsForUserA(hToken: win32more.Windows.Win32.Foundation.HANDLE, lpSrc: win32more.Windows.Win32.Foundation.PSTR, lpDest: win32more.Windows.Win32.Foundation.PSTR, dwSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def ExpandEnvironmentStringsForUserW(hToken: win32more.Windows.Win32.Foundation.HANDLE, lpSrc: win32more.Windows.Win32.Foundation.PWSTR, lpDest: win32more.Windows.Win32.Foundation.PWSTR, dwSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
ExpandEnvironmentStringsForUser = UnicodeAlias('ExpandEnvironmentStringsForUserW')
@winfunctype('KERNEL32.dll')
def IsEnclaveTypeSupported(flEnclaveType: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateEnclave(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpAddress: VoidPtr, dwSize: UIntPtr, dwInitialCommitment: UIntPtr, flEnclaveType: UInt32, lpEnclaveInformation: VoidPtr, dwInfoLength: UInt32, lpEnclaveError: POINTER(UInt32)) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def LoadEnclaveData(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpAddress: VoidPtr, lpBuffer: VoidPtr, nSize: UIntPtr, flProtect: UInt32, lpPageInformation: VoidPtr, dwInfoLength: UInt32, lpNumberOfBytesWritten: POINTER(UIntPtr), lpEnclaveError: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def InitializeEnclave(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpAddress: VoidPtr, lpEnclaveInformation: VoidPtr, dwInfoLength: UInt32, lpEnclaveError: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-enclave-l1-1-1.dll')
def LoadEnclaveImageA(lpEnclaveAddress: VoidPtr, lpImageName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-enclave-l1-1-1.dll')
def LoadEnclaveImageW(lpEnclaveAddress: VoidPtr, lpImageName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
LoadEnclaveImage = UnicodeAlias('LoadEnclaveImageW')
@winfunctype('vertdll.dll')
def CallEnclave(lpRoutine: IntPtr, lpParameter: VoidPtr, fWaitForThread: win32more.Windows.Win32.Foundation.BOOL, lpReturnValue: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('vertdll.dll')
def TerminateEnclave(lpAddress: VoidPtr, fWait: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-enclave-l1-1-1.dll')
def DeleteEnclave(lpAddress: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('vertdll.dll')
def EnclaveGetAttestationReport(EnclaveData: POINTER(Byte), Report: VoidPtr, BufferSize: UInt32, OutputSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vertdll.dll')
def EnclaveVerifyAttestationReport(EnclaveType: UInt32, Report: VoidPtr, ReportSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vertdll.dll')
def EnclaveSealData(DataToEncrypt: VoidPtr, DataToEncryptSize: UInt32, IdentityPolicy: win32more.Windows.Win32.System.Environment.ENCLAVE_SEALING_IDENTITY_POLICY, RuntimePolicy: UInt32, ProtectedBlob: VoidPtr, BufferSize: UInt32, ProtectedBlobSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vertdll.dll')
def EnclaveUnsealData(ProtectedBlob: VoidPtr, ProtectedBlobSize: UInt32, DecryptedData: VoidPtr, BufferSize: UInt32, DecryptedDataSize: POINTER(UInt32), SealingIdentity: POINTER(win32more.Windows.Win32.System.Environment.ENCLAVE_IDENTITY), UnsealingFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('vertdll.dll')
def EnclaveGetEnclaveInformation(InformationSize: UInt32, EnclaveInformation: POINTER(win32more.Windows.Win32.System.Environment.ENCLAVE_INFORMATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
    BaseAddress: VoidPtr
    Size: UIntPtr
    Identity: win32more.Windows.Win32.System.Environment.ENCLAVE_IDENTITY
ENCLAVE_SEALING_IDENTITY_POLICY = Int32
ENCLAVE_IDENTITY_POLICY_SEAL_INVALID: win32more.Windows.Win32.System.Environment.ENCLAVE_SEALING_IDENTITY_POLICY = 0
ENCLAVE_IDENTITY_POLICY_SEAL_EXACT_CODE: win32more.Windows.Win32.System.Environment.ENCLAVE_SEALING_IDENTITY_POLICY = 1
ENCLAVE_IDENTITY_POLICY_SEAL_SAME_PRIMARY_CODE: win32more.Windows.Win32.System.Environment.ENCLAVE_SEALING_IDENTITY_POLICY = 2
ENCLAVE_IDENTITY_POLICY_SEAL_SAME_IMAGE: win32more.Windows.Win32.System.Environment.ENCLAVE_SEALING_IDENTITY_POLICY = 3
ENCLAVE_IDENTITY_POLICY_SEAL_SAME_FAMILY: win32more.Windows.Win32.System.Environment.ENCLAVE_SEALING_IDENTITY_POLICY = 4
ENCLAVE_IDENTITY_POLICY_SEAL_SAME_AUTHOR: win32more.Windows.Win32.System.Environment.ENCLAVE_SEALING_IDENTITY_POLICY = 5
class ENCLAVE_VBS_BASIC_KEY_REQUEST(Structure):
    RequestSize: UInt32
    Flags: UInt32
    EnclaveSVN: UInt32
    SystemKeyID: UInt32
    CurrentSystemKeyID: UInt32
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_COMMIT_PAGES(EnclaveAddress: VoidPtr, NumberOfBytes: UIntPtr, SourceAddress: VoidPtr, PageProtection: UInt32) -> Int32: ...
if ARCH in 'X64,ARM64':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_CREATE_THREAD(ThreadDescriptor: POINTER(win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64)) -> Int32: ...
elif ARCH in 'X86':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_CREATE_THREAD(ThreadDescriptor: POINTER(win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32)) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_DECOMMIT_PAGES(EnclaveAddress: VoidPtr, NumberOfBytes: UIntPtr) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_KEY(KeyRequest: POINTER(win32more.Windows.Win32.System.Environment.ENCLAVE_VBS_BASIC_KEY_REQUEST), RequestedKeySize: UInt32, ReturnedKey: POINTER(Byte)) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_RANDOM_DATA(Buffer: POINTER(Byte), NumberOfBytes: UInt32, Generation: POINTER(UInt64)) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_REPORT(EnclaveData: POINTER(Byte), Report: VoidPtr, BufferSize: UInt32, OutputSize: POINTER(UInt32)) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_GET_ENCLAVE_INFORMATION(EnclaveInfo: POINTER(win32more.Windows.Win32.System.Environment.ENCLAVE_INFORMATION)) -> Int32: ...
if ARCH in 'X64,ARM64':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_INTERRUPT_THREAD(ThreadDescriptor: POINTER(win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64)) -> Int32: ...
elif ARCH in 'X86':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_INTERRUPT_THREAD(ThreadDescriptor: POINTER(win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32)) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_PROTECT_PAGES(EnclaveAddress: VoidPtr, NumberOfytes: UIntPtr, PageProtection: UInt32) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_ENCLAVE(ReturnValue: UIntPtr) -> Void: ...
if ARCH in 'X64':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_EXCEPTION(ExceptionRecord: POINTER(win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_EXCEPTION_AMD64)) -> Int32: ...
elif ARCH in 'X86,ARM64':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_EXCEPTION(ExceptionRecord: VoidPtr) -> Int32: ...
if ARCH in 'X64,ARM64':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_TERMINATE_THREAD(ThreadDescriptor: POINTER(win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR64)) -> Int32: ...
elif ARCH in 'X86':
    @winfunctype_pointer
    def VBS_BASIC_ENCLAVE_BASIC_CALL_TERMINATE_THREAD(ThreadDescriptor: POINTER(win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_THREAD_DESCRIPTOR32)) -> Int32: ...
@winfunctype_pointer
def VBS_BASIC_ENCLAVE_BASIC_CALL_VERIFY_REPORT(Report: VoidPtr, ReportSize: UInt32) -> Int32: ...
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
    ReturnFromEnclave: win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_ENCLAVE
    ReturnFromException: win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_RETURN_FROM_EXCEPTION
    TerminateThread: win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_TERMINATE_THREAD
    InterruptThread: win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_INTERRUPT_THREAD
    CommitPages: win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_COMMIT_PAGES
    DecommitPages: win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_DECOMMIT_PAGES
    ProtectPages: win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_PROTECT_PAGES
    CreateThread: win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_CREATE_THREAD
    GetEnclaveInformation: win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_GET_ENCLAVE_INFORMATION
    GenerateKey: win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_KEY
    GenerateReport: win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_REPORT
    VerifyReport: win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_VERIFY_REPORT
    GenerateRandomData: win32more.Windows.Win32.System.Environment.VBS_BASIC_ENCLAVE_BASIC_CALL_GENERATE_RANDOM_DATA
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
    EnclaveIdentity: win32more.Windows.Win32.System.Environment.ENCLAVE_IDENTITY
    _pack_ = 1
class VBS_ENCLAVE_REPORT_MODULE(Structure):
    Header: win32more.Windows.Win32.System.Environment.VBS_ENCLAVE_REPORT_VARDATA_HEADER
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


make_ready(__name__)
