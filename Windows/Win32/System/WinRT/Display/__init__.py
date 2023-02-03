from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT
import Windows.Win32.System.WinRT.Display
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
class IDisplayDeviceInterop(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('64338358-366a-471b-bd-56-dd-8e-f4-8e-43-9b')
    @commethod(3)
    def CreateSharedHandle(pObject: Windows.Win32.System.WinRT.IInspectable_head, pSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), Access: UInt32, Name: Windows.Win32.System.WinRT.HSTRING, pHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenSharedHandle(NTHandle: Windows.Win32.Foundation.HANDLE, riid: Guid, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDisplayPathInterop(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a6ba4205-e59e-4e71-b2-5b-4e-43-6d-21-ee-3d')
    @commethod(3)
    def CreateSourcePresentationHandle(pValue: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceId(pSourceId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IDisplayDeviceInterop')
make_head(_module, 'IDisplayPathInterop')
__all__ = [
    "IDisplayDeviceInterop",
    "IDisplayPathInterop",
]
_arch_optional = [
]
