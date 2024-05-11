from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.ChannelCredentials
import win32more.Windows.Win32.System.Variant
class IChannelCredentials(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{181b448c-c17c-4b17-ac6d-06699b93198f}')
    @commethod(7)
    def SetWindowsCredential(self, domain: win32more.Windows.Win32.Foundation.BSTR, username: win32more.Windows.Win32.Foundation.BSTR, password: win32more.Windows.Win32.Foundation.BSTR, impersonationLevel: Int32, allowNtlm: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetUserNameCredential(self, username: win32more.Windows.Win32.Foundation.BSTR, password: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetClientCertificateFromStore(self, storeLocation: win32more.Windows.Win32.Foundation.BSTR, storeName: win32more.Windows.Win32.Foundation.BSTR, findYype: win32more.Windows.Win32.Foundation.BSTR, findValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetClientCertificateFromStoreByName(self, subjectName: win32more.Windows.Win32.Foundation.BSTR, storeLocation: win32more.Windows.Win32.Foundation.BSTR, storeName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetClientCertificateFromFile(self, filename: win32more.Windows.Win32.Foundation.BSTR, password: win32more.Windows.Win32.Foundation.BSTR, keystorageFlags: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetDefaultServiceCertificateFromStore(self, storeLocation: win32more.Windows.Win32.Foundation.BSTR, storeName: win32more.Windows.Win32.Foundation.BSTR, findType: win32more.Windows.Win32.Foundation.BSTR, findValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetDefaultServiceCertificateFromStoreByName(self, subjectName: win32more.Windows.Win32.Foundation.BSTR, storeLocation: win32more.Windows.Win32.Foundation.BSTR, storeName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetDefaultServiceCertificateFromFile(self, filename: win32more.Windows.Win32.Foundation.BSTR, password: win32more.Windows.Win32.Foundation.BSTR, keystorageFlags: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetServiceCertificateAuthentication(self, storeLocation: win32more.Windows.Win32.Foundation.BSTR, revocationMode: win32more.Windows.Win32.Foundation.BSTR, certificateValidationMode: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetIssuedToken(self, localIssuerAddres: win32more.Windows.Win32.Foundation.BSTR, localIssuerBindingType: win32more.Windows.Win32.Foundation.BSTR, localIssuerBinding: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
