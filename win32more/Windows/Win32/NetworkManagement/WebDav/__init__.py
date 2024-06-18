from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.WebDav
AUTHNEXTSTEP = Int32
DefaultBehavior: win32more.Windows.Win32.NetworkManagement.WebDav.AUTHNEXTSTEP = 0
RetryRequest: win32more.Windows.Win32.NetworkManagement.WebDav.AUTHNEXTSTEP = 1
CancelRequest: win32more.Windows.Win32.NetworkManagement.WebDav.AUTHNEXTSTEP = 2
DAV_AUTHN_SCHEME_BASIC: UInt32 = 1
DAV_AUTHN_SCHEME_NTLM: UInt32 = 2
DAV_AUTHN_SCHEME_PASSPORT: UInt32 = 4
DAV_AUTHN_SCHEME_DIGEST: UInt32 = 8
DAV_AUTHN_SCHEME_NEGOTIATE: UInt32 = 16
DAV_AUTHN_SCHEME_CERT: UInt32 = 65536
DAV_AUTHN_SCHEME_FBA: UInt32 = 1048576
@winfunctype('NETAPI32.dll')
def DavAddConnection(ConnectionHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), RemoteName: win32more.Windows.Win32.Foundation.PWSTR, UserName: win32more.Windows.Win32.Foundation.PWSTR, Password: win32more.Windows.Win32.Foundation.PWSTR, ClientCert: POINTER(Byte), CertSize: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavDeleteConnection(ConnectionHandle: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavGetUNCFromHTTPPath(Url: win32more.Windows.Win32.Foundation.PWSTR, UncPath: win32more.Windows.Win32.Foundation.PWSTR, lpSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavGetHTTPFromUNCPath(UncPath: win32more.Windows.Win32.Foundation.PWSTR, Url: win32more.Windows.Win32.Foundation.PWSTR, lpSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavGetTheLockOwnerOfTheFile(FileName: win32more.Windows.Win32.Foundation.PWSTR, LockOwnerName: win32more.Windows.Win32.Foundation.PWSTR, LockOwnerNameLengthInBytes: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavGetExtendedError(hFile: win32more.Windows.Win32.Foundation.HANDLE, ExtError: POINTER(UInt32), ExtErrorString: win32more.Windows.Win32.Foundation.PWSTR, cChSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavFlushFile(hFile: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavInvalidateCache(URLName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavCancelConnectionsToServer(lpName: win32more.Windows.Win32.Foundation.PWSTR, fForce: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavRegisterAuthCallback(CallBack: win32more.Windows.Win32.NetworkManagement.WebDav.PFNDAVAUTHCALLBACK, Version: UInt32) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavUnregisterAuthCallback(hCallback: UInt32) -> Void: ...
class DAV_CALLBACK_AUTH_BLOB(Structure):
    pBuffer: VoidPtr
    ulSize: UInt32
    ulType: UInt32
class DAV_CALLBACK_AUTH_UNP(Structure):
    pszUserName: win32more.Windows.Win32.Foundation.PWSTR
    ulUserNameLength: UInt32
    pszPassword: win32more.Windows.Win32.Foundation.PWSTR
    ulPasswordLength: UInt32
class DAV_CALLBACK_CRED(Structure):
    AuthBlob: win32more.Windows.Win32.NetworkManagement.WebDav.DAV_CALLBACK_AUTH_BLOB
    UNPBlob: win32more.Windows.Win32.NetworkManagement.WebDav.DAV_CALLBACK_AUTH_UNP
    bAuthBlobValid: win32more.Windows.Win32.Foundation.BOOL
    bSave: win32more.Windows.Win32.Foundation.BOOL
@winfunctype_pointer
def PFNDAVAUTHCALLBACK(lpwzServerName: win32more.Windows.Win32.Foundation.PWSTR, lpwzRemoteName: win32more.Windows.Win32.Foundation.PWSTR, dwAuthScheme: UInt32, dwFlags: UInt32, pCallbackCred: POINTER(win32more.Windows.Win32.NetworkManagement.WebDav.DAV_CALLBACK_CRED), NextStep: POINTER(win32more.Windows.Win32.NetworkManagement.WebDav.AUTHNEXTSTEP), pFreeCred: POINTER(win32more.Windows.Win32.NetworkManagement.WebDav.PFNDAVAUTHCALLBACK_FREECRED)) -> UInt32: ...
@winfunctype_pointer
def PFNDAVAUTHCALLBACK_FREECRED(pbuffer: VoidPtr) -> UInt32: ...


make_ready(__name__)
