from win32more.base import *
import win32more.Devices.DeviceAccess
import win32more.Foundation
import win32more.System.Com

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
ED_BASE = 4096
DEV_PORT_SIM = 1
DEV_PORT_COM1 = 2
DEV_PORT_COM2 = 3
DEV_PORT_COM3 = 4
DEV_PORT_COM4 = 5
DEV_PORT_DIAQ = 6
DEV_PORT_ARTI = 7
DEV_PORT_1394 = 8
DEV_PORT_USB = 9
DEV_PORT_MIN = 1
DEV_PORT_MAX = 9
ED_TOP = 1
ED_MIDDLE = 2
ED_BOTTOM = 4
ED_LEFT = 256
ED_CENTER = 512
ED_RIGHT = 1024
ED_AUDIO_ALL = 268435456
ED_AUDIO_1 = 1
ED_AUDIO_2 = 2
ED_AUDIO_3 = 4
ED_AUDIO_4 = 8
ED_AUDIO_5 = 16
ED_AUDIO_6 = 32
ED_AUDIO_7 = 64
ED_AUDIO_8 = 128
ED_AUDIO_9 = 256
ED_AUDIO_10 = 512
ED_AUDIO_11 = 1024
ED_AUDIO_12 = 2048
ED_AUDIO_13 = 4096
ED_AUDIO_14 = 8192
ED_AUDIO_15 = 16384
ED_AUDIO_16 = 32768
ED_AUDIO_17 = 65536
ED_AUDIO_18 = 131072
ED_AUDIO_19 = 262144
ED_AUDIO_20 = 524288
ED_AUDIO_21 = 1048576
ED_AUDIO_22 = 2097152
ED_AUDIO_23 = 4194304
ED_AUDIO_24 = 8388608
ED_VIDEO = 33554432
CLSID_DeviceIoControl = '12d3e372-874b-457d-9fdf-73977778686c'
def _define_IDeviceRequestCompletionCallback_head():
    class IDeviceRequestCompletionCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('999bad24-9acd-45bb-8669-2a2fc0288b04')
    return IDeviceRequestCompletionCallback
def _define_IDeviceRequestCompletionCallback():
    IDeviceRequestCompletionCallback = win32more.Devices.DeviceAccess.IDeviceRequestCompletionCallback_head
    IDeviceRequestCompletionCallback.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'Invoke', ((1, 'requestResult'),(1, 'bytesReturned'),)))
    win32more.System.Com.IUnknown
    return IDeviceRequestCompletionCallback
def _define_IDeviceIoControl_head():
    class IDeviceIoControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('9eefe161-23ab-4f18-9b49-991b586ae970')
    return IDeviceIoControl
def _define_IDeviceIoControl():
    IDeviceIoControl = win32more.Devices.DeviceAccess.IDeviceIoControl_head
    IDeviceIoControl.DeviceIoControlSync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,POINTER(UInt32), use_last_error=False)(3, 'DeviceIoControlSync', ((1, 'ioControlCode'),(1, 'inputBuffer'),(1, 'inputBufferSize'),(1, 'outputBuffer'),(1, 'outputBufferSize'),(1, 'bytesReturned'),)))
    IDeviceIoControl.DeviceIoControlAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),UInt32,POINTER(Byte),UInt32,win32more.Devices.DeviceAccess.IDeviceRequestCompletionCallback_head,POINTER(UIntPtr), use_last_error=False)(4, 'DeviceIoControlAsync', ((1, 'ioControlCode'),(1, 'inputBuffer'),(1, 'inputBufferSize'),(1, 'outputBuffer'),(1, 'outputBufferSize'),(1, 'requestCompletionCallback'),(1, 'cancelContext'),)))
    IDeviceIoControl.CancelOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr, use_last_error=False)(5, 'CancelOperation', ((1, 'cancelContext'),)))
    win32more.System.Com.IUnknown
    return IDeviceIoControl
def _define_ICreateDeviceAccessAsync_head():
    class ICreateDeviceAccessAsync(win32more.System.Com.IUnknown_head):
        Guid = Guid('3474628f-683d-42d2-abcb-db018c6503bc')
    return ICreateDeviceAccessAsync
def _define_ICreateDeviceAccessAsync():
    ICreateDeviceAccessAsync = win32more.Devices.DeviceAccess.ICreateDeviceAccessAsync_head
    ICreateDeviceAccessAsync.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Cancel', ()))
    ICreateDeviceAccessAsync.Wait = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Wait', ((1, 'timeout'),)))
    ICreateDeviceAccessAsync.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Close', ()))
    ICreateDeviceAccessAsync.GetResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetResult', ((1, 'riid'),(1, 'deviceAccess'),)))
    win32more.System.Com.IUnknown
    return ICreateDeviceAccessAsync
def _define_CreateDeviceAccessInstance():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Devices.DeviceAccess.ICreateDeviceAccessAsync_head), use_last_error=False)(("CreateDeviceAccessInstance", windll["deviceaccess"]), ((1, 'deviceInterfacePath'),(1, 'desiredAccess'),(1, 'createAsync'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "ED_BASE",
    "DEV_PORT_SIM",
    "DEV_PORT_COM1",
    "DEV_PORT_COM2",
    "DEV_PORT_COM3",
    "DEV_PORT_COM4",
    "DEV_PORT_DIAQ",
    "DEV_PORT_ARTI",
    "DEV_PORT_1394",
    "DEV_PORT_USB",
    "DEV_PORT_MIN",
    "DEV_PORT_MAX",
    "ED_TOP",
    "ED_MIDDLE",
    "ED_BOTTOM",
    "ED_LEFT",
    "ED_CENTER",
    "ED_RIGHT",
    "ED_AUDIO_ALL",
    "ED_AUDIO_1",
    "ED_AUDIO_2",
    "ED_AUDIO_3",
    "ED_AUDIO_4",
    "ED_AUDIO_5",
    "ED_AUDIO_6",
    "ED_AUDIO_7",
    "ED_AUDIO_8",
    "ED_AUDIO_9",
    "ED_AUDIO_10",
    "ED_AUDIO_11",
    "ED_AUDIO_12",
    "ED_AUDIO_13",
    "ED_AUDIO_14",
    "ED_AUDIO_15",
    "ED_AUDIO_16",
    "ED_AUDIO_17",
    "ED_AUDIO_18",
    "ED_AUDIO_19",
    "ED_AUDIO_20",
    "ED_AUDIO_21",
    "ED_AUDIO_22",
    "ED_AUDIO_23",
    "ED_AUDIO_24",
    "ED_VIDEO",
    "CLSID_DeviceIoControl",
    "IDeviceRequestCompletionCallback",
    "IDeviceIoControl",
    "ICreateDeviceAccessAsync",
    "CreateDeviceAccessInstance",
]
