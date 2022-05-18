from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.System.Com
import win32more.System.WinRT

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
def _define_IDisplayDeviceInterop_head():
    class IDisplayDeviceInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('64338358-366a-471b-bd56-dd8ef48e439b')
    return IDisplayDeviceInterop
def _define_IDisplayDeviceInterop():
    IDisplayDeviceInterop = win32more.System.WinRT.Display.IDisplayDeviceInterop_head
    IDisplayDeviceInterop.CreateSharedHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,win32more.System.WinRT.HSTRING,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(3, 'CreateSharedHandle', ((1, 'pObject'),(1, 'pSecurityAttributes'),(1, 'Access'),(1, 'Name'),(1, 'pHandle'),)))
    IDisplayDeviceInterop.OpenSharedHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,Guid,POINTER(c_void_p), use_last_error=False)(4, 'OpenSharedHandle', ((1, 'NTHandle'),(1, 'riid'),(1, 'ppvObj'),)))
    return IDisplayDeviceInterop
def _define_IDisplayPathInterop_head():
    class IDisplayPathInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('a6ba4205-e59e-4e71-b25b-4e436d21ee3d')
    return IDisplayPathInterop
def _define_IDisplayPathInterop():
    IDisplayPathInterop = win32more.System.WinRT.Display.IDisplayPathInterop_head
    IDisplayPathInterop.CreateSourcePresentationHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(3, 'CreateSourcePresentationHandle', ((1, 'pValue'),)))
    IDisplayPathInterop.GetSourceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetSourceId', ((1, 'pSourceId'),)))
    return IDisplayPathInterop
__all__ = [
    "IDisplayDeviceInterop",
    "IDisplayPathInterop",
]
