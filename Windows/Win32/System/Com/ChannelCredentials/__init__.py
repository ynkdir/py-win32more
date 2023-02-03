from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.ChannelCredentials
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
class IChannelCredentials(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('181b448c-c17c-4b17-ac-6d-06-69-9b-93-19-8f')
    @commethod(7)
    def SetWindowsCredential(domain: Windows.Win32.Foundation.BSTR, username: Windows.Win32.Foundation.BSTR, password: Windows.Win32.Foundation.BSTR, impersonationLevel: Int32, allowNtlm: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetUserNameCredential(username: Windows.Win32.Foundation.BSTR, password: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetClientCertificateFromStore(storeLocation: Windows.Win32.Foundation.BSTR, storeName: Windows.Win32.Foundation.BSTR, findYype: Windows.Win32.Foundation.BSTR, findValue: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetClientCertificateFromStoreByName(subjectName: Windows.Win32.Foundation.BSTR, storeLocation: Windows.Win32.Foundation.BSTR, storeName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetClientCertificateFromFile(filename: Windows.Win32.Foundation.BSTR, password: Windows.Win32.Foundation.BSTR, keystorageFlags: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetDefaultServiceCertificateFromStore(storeLocation: Windows.Win32.Foundation.BSTR, storeName: Windows.Win32.Foundation.BSTR, findType: Windows.Win32.Foundation.BSTR, findValue: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetDefaultServiceCertificateFromStoreByName(subjectName: Windows.Win32.Foundation.BSTR, storeLocation: Windows.Win32.Foundation.BSTR, storeName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetDefaultServiceCertificateFromFile(filename: Windows.Win32.Foundation.BSTR, password: Windows.Win32.Foundation.BSTR, keystorageFlags: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetServiceCertificateAuthentication(storeLocation: Windows.Win32.Foundation.BSTR, revocationMode: Windows.Win32.Foundation.BSTR, certificateValidationMode: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetIssuedToken(localIssuerAddres: Windows.Win32.Foundation.BSTR, localIssuerBindingType: Windows.Win32.Foundation.BSTR, localIssuerBinding: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IChannelCredentials')
__all__ = [
    "IChannelCredentials",
]
_arch_optional = [
]
