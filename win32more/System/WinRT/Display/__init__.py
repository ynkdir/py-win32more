from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security
import win32more.System.Com
import win32more.System.WinRT
import win32more.System.WinRT.Display
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
def _define_IDisplayDeviceInterop_head():
    class IDisplayDeviceInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('64338358-366a-471b-bd-56-dd-8e-f4-8e-43-9b')
    return IDisplayDeviceInterop
def _define_IDisplayDeviceInterop():
    IDisplayDeviceInterop = win32more.System.WinRT.Display.IDisplayDeviceInterop_head
    IDisplayDeviceInterop.CreateSharedHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IInspectable_head,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,win32more.System.WinRT.HSTRING,POINTER(win32more.Foundation.HANDLE))(3, 'CreateSharedHandle', ((1, 'pObject'),(1, 'pSecurityAttributes'),(1, 'Access'),(1, 'Name'),(1, 'pHandle'),)))
    IDisplayDeviceInterop.OpenSharedHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,Guid,POINTER(c_void_p))(4, 'OpenSharedHandle', ((1, 'NTHandle'),(1, 'riid'),(1, 'ppvObj'),)))
    win32more.System.Com.IUnknown
    return IDisplayDeviceInterop
def _define_IDisplayPathInterop_head():
    class IDisplayPathInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('a6ba4205-e59e-4e71-b2-5b-4e-43-6d-21-ee-3d')
    return IDisplayPathInterop
def _define_IDisplayPathInterop():
    IDisplayPathInterop = win32more.System.WinRT.Display.IDisplayPathInterop_head
    IDisplayPathInterop.CreateSourcePresentationHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE))(3, 'CreateSourcePresentationHandle', ((1, 'pValue'),)))
    IDisplayPathInterop.GetSourceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetSourceId', ((1, 'pSourceId'),)))
    win32more.System.Com.IUnknown
    return IDisplayPathInterop
__all__ = [
    "IDisplayDeviceInterop",
    "IDisplayPathInterop",
]
