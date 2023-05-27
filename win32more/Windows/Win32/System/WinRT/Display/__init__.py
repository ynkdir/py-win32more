from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.System.WinRT.Display
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IDisplayDeviceInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{64338358-366a-471b-bd56-dd8ef48e439b}')
    @commethod(3)
    def CreateSharedHandle(self, pObject: win32more.Windows.Win32.System.WinRT.IInspectable_head, pSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES_head), Access: UInt32, Name: win32more.Windows.Win32.System.WinRT.HSTRING, pHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenSharedHandle(self, NTHandle: win32more.Windows.Win32.Foundation.HANDLE, riid: Guid, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDisplayPathInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a6ba4205-e59e-4e71-b25b-4e436d21ee3d}')
    @commethod(3)
    def CreateSourcePresentationHandle(self, pValue: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceId(self, pSourceId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IDisplayDeviceInterop')
make_head(_module, 'IDisplayPathInterop')
