from win32more.base import *
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.ChannelCredentials

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_IChannelCredentials_head():
    class IChannelCredentials(win32more.System.Com.IDispatch_head):
        Guid = Guid('181b448c-c17c-4b17-ac6d-06699b93198f')
    return IChannelCredentials
def _define_IChannelCredentials():
    IChannelCredentials = win32more.System.Com.ChannelCredentials.IChannelCredentials_head
    IChannelCredentials.SetWindowsCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.Foundation.BOOL, use_last_error=False)(7, 'SetWindowsCredential', ((1, 'domain'),(1, 'username'),(1, 'password'),(1, 'impersonationLevel'),(1, 'allowNtlm'),)))
    IChannelCredentials.SetUserNameCredential = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(8, 'SetUserNameCredential', ((1, 'username'),(1, 'password'),)))
    IChannelCredentials.SetClientCertificateFromStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(9, 'SetClientCertificateFromStore', ((1, 'storeLocation'),(1, 'storeName'),(1, 'findYype'),(1, 'findValue'),)))
    IChannelCredentials.SetClientCertificateFromStoreByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(10, 'SetClientCertificateFromStoreByName', ((1, 'subjectName'),(1, 'storeLocation'),(1, 'storeName'),)))
    IChannelCredentials.SetClientCertificateFromFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(11, 'SetClientCertificateFromFile', ((1, 'filename'),(1, 'password'),(1, 'keystorageFlags'),)))
    IChannelCredentials.SetDefaultServiceCertificateFromStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(12, 'SetDefaultServiceCertificateFromStore', ((1, 'storeLocation'),(1, 'storeName'),(1, 'findType'),(1, 'findValue'),)))
    IChannelCredentials.SetDefaultServiceCertificateFromStoreByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(13, 'SetDefaultServiceCertificateFromStoreByName', ((1, 'subjectName'),(1, 'storeLocation'),(1, 'storeName'),)))
    IChannelCredentials.SetDefaultServiceCertificateFromFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(14, 'SetDefaultServiceCertificateFromFile', ((1, 'filename'),(1, 'password'),(1, 'keystorageFlags'),)))
    IChannelCredentials.SetServiceCertificateAuthentication = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(15, 'SetServiceCertificateAuthentication', ((1, 'storeLocation'),(1, 'revocationMode'),(1, 'certificateValidationMode'),)))
    IChannelCredentials.SetIssuedToken = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(16, 'SetIssuedToken', ((1, 'localIssuerAddres'),(1, 'localIssuerBindingType'),(1, 'localIssuerBinding'),)))
    win32more.System.Com.IDispatch
    return IChannelCredentials
__all__ = [
    "IChannelCredentials",
]
