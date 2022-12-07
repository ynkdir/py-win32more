from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security
import win32more.System.Com
import win32more.System.WinRT
import win32more.System.WinRT.Display
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
class IDisplayDeviceInterop(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('64338358-366a-471b-bd-56-dd-8e-f4-8e-43-9b')
    @commethod(3)
    def CreateSharedHandle(pObject: win32more.System.WinRT.IInspectable_head, pSecurityAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), Access: UInt32, Name: win32more.System.WinRT.HSTRING, pHandle: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OpenSharedHandle(NTHandle: win32more.Foundation.HANDLE, riid: Guid, ppvObj: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IDisplayPathInterop(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a6ba4205-e59e-4e71-b2-5b-4e-43-6d-21-ee-3d')
    @commethod(3)
    def CreateSourcePresentationHandle(pValue: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceId(pSourceId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IDisplayDeviceInterop')
make_head(_module, 'IDisplayPathInterop')
__all__ = [
    "IDisplayDeviceInterop",
    "IDisplayPathInterop",
]
