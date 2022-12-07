from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.WinRT
import win32more.System.WinRT.AllJoyn
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
class IWindowsDevicesAllJoynBusAttachmentFactoryInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('4b8f7505-b239-4e7b-88-af-f6-68-25-75-d8-61')
    @commethod(6)
    def CreateFromWin32Handle(win32handle: UInt64, enableAboutData: Byte, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IWindowsDevicesAllJoynBusAttachmentInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('fd89c65b-b50e-4a19-9d-0c-b4-2b-78-32-81-cd')
    @commethod(6)
    def get_Win32Handle(value: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
class IWindowsDevicesAllJoynBusObjectFactoryInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('6174e506-8b95-4e36-95-c0-b8-8f-ed-34-93-8c')
    @commethod(6)
    def CreateFromWin32Handle(win32handle: UInt64, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IWindowsDevicesAllJoynBusObjectInterop(c_void_p):
    extends: win32more.System.WinRT.IInspectable
    Guid = Guid('d78aa3d5-5054-428f-99-f2-ec-3a-5d-e3-c3-bc')
    @commethod(6)
    def AddPropertyGetHandler(context: c_void_p, interfaceName: win32more.System.WinRT.HSTRING, callback: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def AddPropertySetHandler(context: c_void_p, interfaceName: win32more.System.WinRT.HSTRING, callback: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Win32Handle(value: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'IWindowsDevicesAllJoynBusAttachmentFactoryInterop')
make_head(_module, 'IWindowsDevicesAllJoynBusAttachmentInterop')
make_head(_module, 'IWindowsDevicesAllJoynBusObjectFactoryInterop')
make_head(_module, 'IWindowsDevicesAllJoynBusObjectInterop')
__all__ = [
    "IWindowsDevicesAllJoynBusAttachmentFactoryInterop",
    "IWindowsDevicesAllJoynBusAttachmentInterop",
    "IWindowsDevicesAllJoynBusObjectFactoryInterop",
    "IWindowsDevicesAllJoynBusObjectInterop",
]
