from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.NetworkManagement.WebDav
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
DAV_AUTHN_SCHEME_BASIC: UInt32 = 1
DAV_AUTHN_SCHEME_NTLM: UInt32 = 2
DAV_AUTHN_SCHEME_PASSPORT: UInt32 = 4
DAV_AUTHN_SCHEME_DIGEST: UInt32 = 8
DAV_AUTHN_SCHEME_NEGOTIATE: UInt32 = 16
DAV_AUTHN_SCHEME_CERT: UInt32 = 65536
DAV_AUTHN_SCHEME_FBA: UInt32 = 1048576
@winfunctype('NETAPI32.dll')
def DavAddConnection(ConnectionHandle: POINTER(win32more.Foundation.HANDLE), RemoteName: win32more.Foundation.PWSTR, UserName: win32more.Foundation.PWSTR, Password: win32more.Foundation.PWSTR, ClientCert: c_char_p_no, CertSize: UInt32) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavDeleteConnection(ConnectionHandle: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavGetUNCFromHTTPPath(Url: win32more.Foundation.PWSTR, UncPath: win32more.Foundation.PWSTR, lpSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavGetHTTPFromUNCPath(UncPath: win32more.Foundation.PWSTR, Url: win32more.Foundation.PWSTR, lpSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavGetTheLockOwnerOfTheFile(FileName: win32more.Foundation.PWSTR, LockOwnerName: win32more.Foundation.PWSTR, LockOwnerNameLengthInBytes: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavGetExtendedError(hFile: win32more.Foundation.HANDLE, ExtError: POINTER(UInt32), ExtErrorString: win32more.Foundation.PWSTR, cChSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETAPI32.dll')
def DavFlushFile(hFile: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavInvalidateCache(URLName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavCancelConnectionsToServer(lpName: win32more.Foundation.PWSTR, fForce: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavRegisterAuthCallback(CallBack: win32more.NetworkManagement.WebDav.PFNDAVAUTHCALLBACK, Version: UInt32) -> UInt32: ...
@winfunctype('davclnt.dll')
def DavUnregisterAuthCallback(hCallback: UInt32) -> Void: ...
AUTHNEXTSTEP = Int32
AUTHNEXTSTEP_DefaultBehavior: AUTHNEXTSTEP = 0
AUTHNEXTSTEP_RetryRequest: AUTHNEXTSTEP = 1
AUTHNEXTSTEP_CancelRequest: AUTHNEXTSTEP = 2
class DAV_CALLBACK_AUTH_BLOB(Structure):
    pBuffer: c_void_p
    ulSize: UInt32
    ulType: UInt32
class DAV_CALLBACK_AUTH_UNP(Structure):
    pszUserName: win32more.Foundation.PWSTR
    ulUserNameLength: UInt32
    pszPassword: win32more.Foundation.PWSTR
    ulPasswordLength: UInt32
class DAV_CALLBACK_CRED(Structure):
    AuthBlob: win32more.NetworkManagement.WebDav.DAV_CALLBACK_AUTH_BLOB
    UNPBlob: win32more.NetworkManagement.WebDav.DAV_CALLBACK_AUTH_UNP
    bAuthBlobValid: win32more.Foundation.BOOL
    bSave: win32more.Foundation.BOOL
@winfunctype_pointer
def PFNDAVAUTHCALLBACK(lpwzServerName: win32more.Foundation.PWSTR, lpwzRemoteName: win32more.Foundation.PWSTR, dwAuthScheme: UInt32, dwFlags: UInt32, pCallbackCred: POINTER(win32more.NetworkManagement.WebDav.DAV_CALLBACK_CRED_head), NextStep: POINTER(win32more.NetworkManagement.WebDav.AUTHNEXTSTEP), pFreeCred: POINTER(win32more.NetworkManagement.WebDav.PFNDAVAUTHCALLBACK_FREECRED)) -> UInt32: ...
@winfunctype_pointer
def PFNDAVAUTHCALLBACK_FREECRED(pbuffer: c_void_p) -> UInt32: ...
make_head(_module, 'DAV_CALLBACK_AUTH_BLOB')
make_head(_module, 'DAV_CALLBACK_AUTH_UNP')
make_head(_module, 'DAV_CALLBACK_CRED')
make_head(_module, 'PFNDAVAUTHCALLBACK')
make_head(_module, 'PFNDAVAUTHCALLBACK_FREECRED')
__all__ = [
    "AUTHNEXTSTEP",
    "AUTHNEXTSTEP_CancelRequest",
    "AUTHNEXTSTEP_DefaultBehavior",
    "AUTHNEXTSTEP_RetryRequest",
    "DAV_AUTHN_SCHEME_BASIC",
    "DAV_AUTHN_SCHEME_CERT",
    "DAV_AUTHN_SCHEME_DIGEST",
    "DAV_AUTHN_SCHEME_FBA",
    "DAV_AUTHN_SCHEME_NEGOTIATE",
    "DAV_AUTHN_SCHEME_NTLM",
    "DAV_AUTHN_SCHEME_PASSPORT",
    "DAV_CALLBACK_AUTH_BLOB",
    "DAV_CALLBACK_AUTH_UNP",
    "DAV_CALLBACK_CRED",
    "DavAddConnection",
    "DavCancelConnectionsToServer",
    "DavDeleteConnection",
    "DavFlushFile",
    "DavGetExtendedError",
    "DavGetHTTPFromUNCPath",
    "DavGetTheLockOwnerOfTheFile",
    "DavGetUNCFromHTTPPath",
    "DavInvalidateCache",
    "DavRegisterAuthCallback",
    "DavUnregisterAuthCallback",
    "PFNDAVAUTHCALLBACK",
    "PFNDAVAUTHCALLBACK_FREECRED",
]
_arch_optional = [
]
