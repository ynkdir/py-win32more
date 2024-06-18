from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Media.MediaFoundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.System.WinRT.Media
CLSID_AudioFrameNativeFactory: Guid = Guid('{16a0a3b9-9f65-4102-9367-2cda3a4f372a}')
CLSID_VideoFrameNativeFactory: Guid = Guid('{d194386a-04e3-4814-8100-b2b0ae6d78c7}')
class IAudioFrameNative(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{20be1e2e-930f-4746-9335-3c332f255093}')
    @commethod(6)
    def GetData(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioFrameNativeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7bd67cf8-bf7d-43e6-af8d-b170ee0c0110}')
    @commethod(6)
    def CreateFromMFSample(self, data: win32more.Windows.Win32.Media.MediaFoundation.IMFSample, forceReadOnly: win32more.Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVideoFrameNative(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{26ba702b-314a-4620-aaf6-7a51aa58fa18}')
    @commethod(6)
    def GetData(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDevice(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVideoFrameNativeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{69e3693e-8e1e-4e63-ac4c-7fdc21d9731d}')
    @commethod(6)
    def CreateFromMFSample(self, data: win32more.Windows.Win32.Media.MediaFoundation.IMFSample, subtype: POINTER(Guid), width: UInt32, height: UInt32, forceReadOnly: win32more.Windows.Win32.Foundation.BOOL, minDisplayAperture: POINTER(win32more.Windows.Win32.Media.MediaFoundation.MFVideoArea), device: win32more.Windows.Win32.Media.MediaFoundation.IMFDXGIDeviceManager, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
