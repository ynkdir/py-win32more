from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.ChannelCredentials
import Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IChannelCredentials(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{181b448c-c17c-4b17-ac6d-06699b93198f}')
    @commethod(7)
    def SetWindowsCredential(self, domain: Windows.Win32.Foundation.BSTR, username: Windows.Win32.Foundation.BSTR, password: Windows.Win32.Foundation.BSTR, impersonationLevel: Int32, allowNtlm: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetUserNameCredential(self, username: Windows.Win32.Foundation.BSTR, password: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetClientCertificateFromStore(self, storeLocation: Windows.Win32.Foundation.BSTR, storeName: Windows.Win32.Foundation.BSTR, findYype: Windows.Win32.Foundation.BSTR, findValue: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetClientCertificateFromStoreByName(self, subjectName: Windows.Win32.Foundation.BSTR, storeLocation: Windows.Win32.Foundation.BSTR, storeName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetClientCertificateFromFile(self, filename: Windows.Win32.Foundation.BSTR, password: Windows.Win32.Foundation.BSTR, keystorageFlags: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetDefaultServiceCertificateFromStore(self, storeLocation: Windows.Win32.Foundation.BSTR, storeName: Windows.Win32.Foundation.BSTR, findType: Windows.Win32.Foundation.BSTR, findValue: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetDefaultServiceCertificateFromStoreByName(self, subjectName: Windows.Win32.Foundation.BSTR, storeLocation: Windows.Win32.Foundation.BSTR, storeName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetDefaultServiceCertificateFromFile(self, filename: Windows.Win32.Foundation.BSTR, password: Windows.Win32.Foundation.BSTR, keystorageFlags: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetServiceCertificateAuthentication(self, storeLocation: Windows.Win32.Foundation.BSTR, revocationMode: Windows.Win32.Foundation.BSTR, certificateValidationMode: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetIssuedToken(self, localIssuerAddres: Windows.Win32.Foundation.BSTR, localIssuerBindingType: Windows.Win32.Foundation.BSTR, localIssuerBinding: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IChannelCredentials')
