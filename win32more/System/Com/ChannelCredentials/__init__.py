from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.ChannelCredentials
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class IChannelCredentials(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('181b448c-c17c-4b17-ac-6d-06-69-9b-93-19-8f')
    @commethod(7)
    def SetWindowsCredential(domain: win32more.Foundation.BSTR, username: win32more.Foundation.BSTR, password: win32more.Foundation.BSTR, impersonationLevel: Int32, allowNtlm: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetUserNameCredential(username: win32more.Foundation.BSTR, password: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetClientCertificateFromStore(storeLocation: win32more.Foundation.BSTR, storeName: win32more.Foundation.BSTR, findYype: win32more.Foundation.BSTR, findValue: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetClientCertificateFromStoreByName(subjectName: win32more.Foundation.BSTR, storeLocation: win32more.Foundation.BSTR, storeName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetClientCertificateFromFile(filename: win32more.Foundation.BSTR, password: win32more.Foundation.BSTR, keystorageFlags: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetDefaultServiceCertificateFromStore(storeLocation: win32more.Foundation.BSTR, storeName: win32more.Foundation.BSTR, findType: win32more.Foundation.BSTR, findValue: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetDefaultServiceCertificateFromStoreByName(subjectName: win32more.Foundation.BSTR, storeLocation: win32more.Foundation.BSTR, storeName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetDefaultServiceCertificateFromFile(filename: win32more.Foundation.BSTR, password: win32more.Foundation.BSTR, keystorageFlags: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetServiceCertificateAuthentication(storeLocation: win32more.Foundation.BSTR, revocationMode: win32more.Foundation.BSTR, certificateValidationMode: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetIssuedToken(localIssuerAddres: win32more.Foundation.BSTR, localIssuerBindingType: win32more.Foundation.BSTR, localIssuerBinding: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IChannelCredentials')
__all__ = [
    "IChannelCredentials",
]
