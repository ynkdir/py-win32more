from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.ChannelCredentials
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
def _define_IChannelCredentials_head():
    class IChannelCredentials(win32more.System.Com.IDispatch_head):
        Guid = Guid('181b448c-c17c-4b17-ac-6d-06-69-9b-93-19-8f')
    return IChannelCredentials
def _define_IChannelCredentials():
    IChannelCredentials = win32more.System.Com.ChannelCredentials.IChannelCredentials_head
    IChannelCredentials.SetWindowsCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.Foundation.BOOL)(7, 'SetWindowsCredential', ((1, 'domain'),(1, 'username'),(1, 'password'),(1, 'impersonationLevel'),(1, 'allowNtlm'),)))
    IChannelCredentials.SetUserNameCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(8, 'SetUserNameCredential', ((1, 'username'),(1, 'password'),)))
    IChannelCredentials.SetClientCertificateFromStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.Com.VARIANT)(9, 'SetClientCertificateFromStore', ((1, 'storeLocation'),(1, 'storeName'),(1, 'findYype'),(1, 'findValue'),)))
    IChannelCredentials.SetClientCertificateFromStoreByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(10, 'SetClientCertificateFromStoreByName', ((1, 'subjectName'),(1, 'storeLocation'),(1, 'storeName'),)))
    IChannelCredentials.SetClientCertificateFromFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(11, 'SetClientCertificateFromFile', ((1, 'filename'),(1, 'password'),(1, 'keystorageFlags'),)))
    IChannelCredentials.SetDefaultServiceCertificateFromStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.Com.VARIANT)(12, 'SetDefaultServiceCertificateFromStore', ((1, 'storeLocation'),(1, 'storeName'),(1, 'findType'),(1, 'findValue'),)))
    IChannelCredentials.SetDefaultServiceCertificateFromStoreByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(13, 'SetDefaultServiceCertificateFromStoreByName', ((1, 'subjectName'),(1, 'storeLocation'),(1, 'storeName'),)))
    IChannelCredentials.SetDefaultServiceCertificateFromFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(14, 'SetDefaultServiceCertificateFromFile', ((1, 'filename'),(1, 'password'),(1, 'keystorageFlags'),)))
    IChannelCredentials.SetServiceCertificateAuthentication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(15, 'SetServiceCertificateAuthentication', ((1, 'storeLocation'),(1, 'revocationMode'),(1, 'certificateValidationMode'),)))
    IChannelCredentials.SetIssuedToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(16, 'SetIssuedToken', ((1, 'localIssuerAddres'),(1, 'localIssuerBindingType'),(1, 'localIssuerBinding'),)))
    win32more.System.Com.IDispatch
    return IChannelCredentials
__all__ = [
    "IChannelCredentials",
]
