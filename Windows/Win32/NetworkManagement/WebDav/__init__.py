from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.WebDav
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AUTHNEXTSTEP = Int32
AUTHNEXTSTEP_DefaultBehavior: AUTHNEXTSTEP = 0
AUTHNEXTSTEP_RetryRequest: AUTHNEXTSTEP = 1
AUTHNEXTSTEP_CancelRequest: AUTHNEXTSTEP = 2
DAV_AUTHN_SCHEME_BASIC: UInt32 = 1
DAV_AUTHN_SCHEME_NTLM: UInt32 = 2
DAV_AUTHN_SCHEME_PASSPORT: UInt32 = 4
DAV_AUTHN_SCHEME_DIGEST: UInt32 = 8
DAV_AUTHN_SCHEME_NEGOTIATE: UInt32 = 16
DAV_AUTHN_SCHEME_CERT: UInt32 = 65536
DAV_AUTHN_SCHEME_FBA: UInt32 = 1048576
@winfunctype('NETAPI32.dll')
def DavAddConnection(ConnectionHandle: POINTER(Windows.Win32.Foundation.HANDLE), RemoteName: Windows.Win32.Foundation.PWSTR, UserName: Windows.Win32.Foundation.PWSTR, Password: Windows.Win32.Foundation.PWSTR, ClientCert: POINTER(Byte), CertSize: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavDeleteConnection(ConnectionHandle: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavGetUNCFromHTTPPath(Url: Windows.Win32.Foundation.PWSTR, UncPath: Windows.Win32.Foundation.PWSTR, lpSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavGetHTTPFromUNCPath(UncPath: Windows.Win32.Foundation.PWSTR, Url: Windows.Win32.Foundation.PWSTR, lpSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavGetTheLockOwnerOfTheFile(FileName: Windows.Win32.Foundation.PWSTR, LockOwnerName: Windows.Win32.Foundation.PWSTR, LockOwnerNameLengthInBytes: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavGetExtendedError(hFile: Windows.Win32.Foundation.HANDLE, ExtError: POINTER(UInt32), ExtErrorString: Windows.Win32.Foundation.PWSTR, cChSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavFlushFile(hFile: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavInvalidateCache(URLName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavCancelConnectionsToServer(lpName: Windows.Win32.Foundation.PWSTR, fForce: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavRegisterAuthCallback(CallBack: Windows.Win32.NetworkManagement.WebDav.PFNDAVAUTHCALLBACK, Version: UInt32) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavUnregisterAuthCallback(hCallback: UInt32) -> Void: ...
class DAV_CALLBACK_AUTH_BLOB(EasyCastStructure):
    pBuffer: c_void_p
    ulSize: UInt32
    ulType: UInt32
class DAV_CALLBACK_AUTH_UNP(EasyCastStructure):
    pszUserName: Windows.Win32.Foundation.PWSTR
    ulUserNameLength: UInt32
    pszPassword: Windows.Win32.Foundation.PWSTR
    ulPasswordLength: UInt32
class DAV_CALLBACK_CRED(EasyCastStructure):
    AuthBlob: Windows.Win32.NetworkManagement.WebDav.DAV_CALLBACK_AUTH_BLOB
    UNPBlob: Windows.Win32.NetworkManagement.WebDav.DAV_CALLBACK_AUTH_UNP
    bAuthBlobValid: Windows.Win32.Foundation.BOOL
    bSave: Windows.Win32.Foundation.BOOL
@winfunctype_pointer
def PFNDAVAUTHCALLBACK(lpwzServerName: Windows.Win32.Foundation.PWSTR, lpwzRemoteName: Windows.Win32.Foundation.PWSTR, dwAuthScheme: UInt32, dwFlags: UInt32, pCallbackCred: POINTER(Windows.Win32.NetworkManagement.WebDav.DAV_CALLBACK_CRED_head), NextStep: POINTER(Windows.Win32.NetworkManagement.WebDav.AUTHNEXTSTEP), pFreeCred: POINTER(Windows.Win32.NetworkManagement.WebDav.PFNDAVAUTHCALLBACK_FREECRED)) -> UInt32: ...
@winfunctype_pointer
def PFNDAVAUTHCALLBACK_FREECRED(pbuffer: c_void_p) -> UInt32: ...
make_head(_module, 'DAV_CALLBACK_AUTH_BLOB')
make_head(_module, 'DAV_CALLBACK_AUTH_UNP')
make_head(_module, 'DAV_CALLBACK_CRED')
make_head(_module, 'PFNDAVAUTHCALLBACK')
make_head(_module, 'PFNDAVAUTHCALLBACK_FREECRED')
