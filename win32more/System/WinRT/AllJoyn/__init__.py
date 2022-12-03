from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.WinRT
import win32more.System.WinRT.AllJoyn
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
def _define_IWindowsDevicesAllJoynBusAttachmentFactoryInterop_head():
    class IWindowsDevicesAllJoynBusAttachmentFactoryInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('4b8f7505-b239-4e7b-88-af-f6-68-25-75-d8-61')
    return IWindowsDevicesAllJoynBusAttachmentFactoryInterop
def _define_IWindowsDevicesAllJoynBusAttachmentFactoryInterop():
    IWindowsDevicesAllJoynBusAttachmentFactoryInterop = win32more.System.WinRT.AllJoyn.IWindowsDevicesAllJoynBusAttachmentFactoryInterop_head
    IWindowsDevicesAllJoynBusAttachmentFactoryInterop.CreateFromWin32Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,Byte,POINTER(Guid),POINTER(c_void_p))(6, 'CreateFromWin32Handle', ((1, 'win32handle'),(1, 'enableAboutData'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return IWindowsDevicesAllJoynBusAttachmentFactoryInterop
def _define_IWindowsDevicesAllJoynBusAttachmentInterop_head():
    class IWindowsDevicesAllJoynBusAttachmentInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('fd89c65b-b50e-4a19-9d-0c-b4-2b-78-32-81-cd')
    return IWindowsDevicesAllJoynBusAttachmentInterop
def _define_IWindowsDevicesAllJoynBusAttachmentInterop():
    IWindowsDevicesAllJoynBusAttachmentInterop = win32more.System.WinRT.AllJoyn.IWindowsDevicesAllJoynBusAttachmentInterop_head
    IWindowsDevicesAllJoynBusAttachmentInterop.get_Win32Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64))(6, 'get_Win32Handle', ((1, 'value'),)))
    win32more.System.WinRT.IInspectable
    return IWindowsDevicesAllJoynBusAttachmentInterop
def _define_IWindowsDevicesAllJoynBusObjectFactoryInterop_head():
    class IWindowsDevicesAllJoynBusObjectFactoryInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('6174e506-8b95-4e36-95-c0-b8-8f-ed-34-93-8c')
    return IWindowsDevicesAllJoynBusObjectFactoryInterop
def _define_IWindowsDevicesAllJoynBusObjectFactoryInterop():
    IWindowsDevicesAllJoynBusObjectFactoryInterop = win32more.System.WinRT.AllJoyn.IWindowsDevicesAllJoynBusObjectFactoryInterop_head
    IWindowsDevicesAllJoynBusObjectFactoryInterop.CreateFromWin32Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(Guid),POINTER(c_void_p))(6, 'CreateFromWin32Handle', ((1, 'win32handle'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return IWindowsDevicesAllJoynBusObjectFactoryInterop
def _define_IWindowsDevicesAllJoynBusObjectInterop_head():
    class IWindowsDevicesAllJoynBusObjectInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('d78aa3d5-5054-428f-99-f2-ec-3a-5d-e3-c3-bc')
    return IWindowsDevicesAllJoynBusObjectInterop
def _define_IWindowsDevicesAllJoynBusObjectInterop():
    IWindowsDevicesAllJoynBusObjectInterop = win32more.System.WinRT.AllJoyn.IWindowsDevicesAllJoynBusObjectInterop_head
    IWindowsDevicesAllJoynBusObjectInterop.AddPropertyGetHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.WinRT.HSTRING,IntPtr)(6, 'AddPropertyGetHandler', ((1, 'context'),(1, 'interfaceName'),(1, 'callback'),)))
    IWindowsDevicesAllJoynBusObjectInterop.AddPropertySetHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.WinRT.HSTRING,IntPtr)(7, 'AddPropertySetHandler', ((1, 'context'),(1, 'interfaceName'),(1, 'callback'),)))
    IWindowsDevicesAllJoynBusObjectInterop.get_Win32Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64))(8, 'get_Win32Handle', ((1, 'value'),)))
    win32more.System.WinRT.IInspectable
    return IWindowsDevicesAllJoynBusObjectInterop
__all__ = [
    "IWindowsDevicesAllJoynBusAttachmentFactoryInterop",
    "IWindowsDevicesAllJoynBusAttachmentInterop",
    "IWindowsDevicesAllJoynBusObjectFactoryInterop",
    "IWindowsDevicesAllJoynBusObjectInterop",
]
