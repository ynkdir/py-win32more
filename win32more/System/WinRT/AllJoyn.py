from win32more.base import *
import win32more.Foundation
import win32more.System.WinRT
import win32more.System.WinRT.AllJoyn

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
def _define_IWindowsDevicesAllJoynBusAttachmentInterop_head():
    class IWindowsDevicesAllJoynBusAttachmentInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('fd89c65b-b50e-4a19-9d0c-b42b783281cd')
    return IWindowsDevicesAllJoynBusAttachmentInterop
def _define_IWindowsDevicesAllJoynBusAttachmentInterop():
    IWindowsDevicesAllJoynBusAttachmentInterop = win32more.System.WinRT.AllJoyn.IWindowsDevicesAllJoynBusAttachmentInterop_head
    IWindowsDevicesAllJoynBusAttachmentInterop.get_Win32Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(6, 'get_Win32Handle', ((1, 'value'),)))
    win32more.System.WinRT.IInspectable
    return IWindowsDevicesAllJoynBusAttachmentInterop
def _define_IWindowsDevicesAllJoynBusAttachmentFactoryInterop_head():
    class IWindowsDevicesAllJoynBusAttachmentFactoryInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('4b8f7505-b239-4e7b-88af-f6682575d861')
    return IWindowsDevicesAllJoynBusAttachmentFactoryInterop
def _define_IWindowsDevicesAllJoynBusAttachmentFactoryInterop():
    IWindowsDevicesAllJoynBusAttachmentFactoryInterop = win32more.System.WinRT.AllJoyn.IWindowsDevicesAllJoynBusAttachmentFactoryInterop_head
    IWindowsDevicesAllJoynBusAttachmentFactoryInterop.CreateFromWin32Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,Byte,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'CreateFromWin32Handle', ((1, 'win32handle'),(1, 'enableAboutData'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return IWindowsDevicesAllJoynBusAttachmentFactoryInterop
def _define_IWindowsDevicesAllJoynBusObjectInterop_head():
    class IWindowsDevicesAllJoynBusObjectInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('d78aa3d5-5054-428f-99f2-ec3a5de3c3bc')
    return IWindowsDevicesAllJoynBusObjectInterop
def _define_IWindowsDevicesAllJoynBusObjectInterop():
    IWindowsDevicesAllJoynBusObjectInterop = win32more.System.WinRT.AllJoyn.IWindowsDevicesAllJoynBusObjectInterop_head
    IWindowsDevicesAllJoynBusObjectInterop.AddPropertyGetHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.WinRT.HSTRING,IntPtr, use_last_error=False)(6, 'AddPropertyGetHandler', ((1, 'context'),(1, 'interfaceName'),(1, 'callback'),)))
    IWindowsDevicesAllJoynBusObjectInterop.AddPropertySetHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.WinRT.HSTRING,IntPtr, use_last_error=False)(7, 'AddPropertySetHandler', ((1, 'context'),(1, 'interfaceName'),(1, 'callback'),)))
    IWindowsDevicesAllJoynBusObjectInterop.get_Win32Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(8, 'get_Win32Handle', ((1, 'value'),)))
    win32more.System.WinRT.IInspectable
    return IWindowsDevicesAllJoynBusObjectInterop
def _define_IWindowsDevicesAllJoynBusObjectFactoryInterop_head():
    class IWindowsDevicesAllJoynBusObjectFactoryInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('6174e506-8b95-4e36-95c0-b88fed34938c')
    return IWindowsDevicesAllJoynBusObjectFactoryInterop
def _define_IWindowsDevicesAllJoynBusObjectFactoryInterop():
    IWindowsDevicesAllJoynBusObjectFactoryInterop = win32more.System.WinRT.AllJoyn.IWindowsDevicesAllJoynBusObjectFactoryInterop_head
    IWindowsDevicesAllJoynBusObjectFactoryInterop.CreateFromWin32Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'CreateFromWin32Handle', ((1, 'win32handle'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return IWindowsDevicesAllJoynBusObjectFactoryInterop
__all__ = [
    "IWindowsDevicesAllJoynBusAttachmentInterop",
    "IWindowsDevicesAllJoynBusAttachmentFactoryInterop",
    "IWindowsDevicesAllJoynBusObjectInterop",
    "IWindowsDevicesAllJoynBusObjectFactoryInterop",
]
