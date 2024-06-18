from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.System.WinRT.Display
class IDisplayDeviceInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{64338358-366a-471b-bd56-dd8ef48e439b}')
    @commethod(3)
    def CreateSharedHandle(self, pObject: win32more.Windows.Win32.System.WinRT.IInspectable, pSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), Access: UInt32, Name: win32more.Windows.Win32.System.WinRT.HSTRING, pHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenSharedHandle(self, NTHandle: win32more.Windows.Win32.Foundation.HANDLE, riid: Guid, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDisplayPathInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a6ba4205-e59e-4e71-b25b-4e436d21ee3d}')
    @commethod(3)
    def CreateSourcePresentationHandle(self, pValue: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceId(self, pSourceId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
