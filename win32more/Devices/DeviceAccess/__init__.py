from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Devices.DeviceAccess
import win32more.Foundation
import win32more.System.Com
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
ED_BASE: Int32 = 4096
DEV_PORT_SIM: UInt32 = 1
DEV_PORT_COM1: UInt32 = 2
DEV_PORT_COM2: UInt32 = 3
DEV_PORT_COM3: UInt32 = 4
DEV_PORT_COM4: UInt32 = 5
DEV_PORT_DIAQ: UInt32 = 6
DEV_PORT_ARTI: UInt32 = 7
DEV_PORT_1394: UInt32 = 8
DEV_PORT_USB: UInt32 = 9
DEV_PORT_MIN: UInt32 = 1
DEV_PORT_MAX: UInt32 = 9
ED_TOP: UInt32 = 1
ED_MIDDLE: UInt32 = 2
ED_BOTTOM: UInt32 = 4
ED_LEFT: UInt32 = 256
ED_CENTER: UInt32 = 512
ED_RIGHT: UInt32 = 1024
ED_AUDIO_ALL: UInt32 = 268435456
ED_AUDIO_1: Int32 = 1
ED_AUDIO_2: Int32 = 2
ED_AUDIO_3: Int32 = 4
ED_AUDIO_4: Int32 = 8
ED_AUDIO_5: Int32 = 16
ED_AUDIO_6: Int32 = 32
ED_AUDIO_7: Int32 = 64
ED_AUDIO_8: Int32 = 128
ED_AUDIO_9: Int32 = 256
ED_AUDIO_10: Int32 = 512
ED_AUDIO_11: Int32 = 1024
ED_AUDIO_12: Int32 = 2048
ED_AUDIO_13: Int32 = 4096
ED_AUDIO_14: Int32 = 8192
ED_AUDIO_15: Int32 = 16384
ED_AUDIO_16: Int32 = 32768
ED_AUDIO_17: Int32 = 65536
ED_AUDIO_18: Int32 = 131072
ED_AUDIO_19: Int32 = 262144
ED_AUDIO_20: Int32 = 524288
ED_AUDIO_21: Int32 = 1048576
ED_AUDIO_22: Int32 = 2097152
ED_AUDIO_23: Int32 = 4194304
ED_AUDIO_24: Int32 = 8388608
ED_VIDEO: Int32 = 33554432
CLSID_DeviceIoControl: Guid = Guid('12d3e372-874b-457d-9f-df-73-97-77-78-68-6c')
@winfunctype('deviceaccess.dll')
def CreateDeviceAccessInstance(deviceInterfacePath: win32more.Foundation.PWSTR, desiredAccess: UInt32, createAsync: POINTER(win32more.Devices.DeviceAccess.ICreateDeviceAccessAsync_head)) -> win32more.Foundation.HRESULT: ...
class ICreateDeviceAccessAsync(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3474628f-683d-42d2-ab-cb-db-01-8c-65-03-bc')
    @commethod(3)
    def Cancel() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Wait(timeout: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Close() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetResult(riid: POINTER(Guid), deviceAccess: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IDeviceIoControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9eefe161-23ab-4f18-9b-49-99-1b-58-6a-e9-70')
    @commethod(3)
    def DeviceIoControlSync(ioControlCode: UInt32, inputBuffer: c_char_p_no, inputBufferSize: UInt32, outputBuffer: c_char_p_no, outputBufferSize: UInt32, bytesReturned: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def DeviceIoControlAsync(ioControlCode: UInt32, inputBuffer: c_char_p_no, inputBufferSize: UInt32, outputBuffer: c_char_p_no, outputBufferSize: UInt32, requestCompletionCallback: win32more.Devices.DeviceAccess.IDeviceRequestCompletionCallback_head, cancelContext: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CancelOperation(cancelContext: UIntPtr) -> win32more.Foundation.HRESULT: ...
class IDeviceRequestCompletionCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('999bad24-9acd-45bb-86-69-2a-2f-c0-28-8b-04')
    @commethod(3)
    def Invoke(requestResult: win32more.Foundation.HRESULT, bytesReturned: UInt32) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'ICreateDeviceAccessAsync')
make_head(_module, 'IDeviceIoControl')
make_head(_module, 'IDeviceRequestCompletionCallback')
__all__ = [
    "CLSID_DeviceIoControl",
    "CreateDeviceAccessInstance",
    "DEV_PORT_1394",
    "DEV_PORT_ARTI",
    "DEV_PORT_COM1",
    "DEV_PORT_COM2",
    "DEV_PORT_COM3",
    "DEV_PORT_COM4",
    "DEV_PORT_DIAQ",
    "DEV_PORT_MAX",
    "DEV_PORT_MIN",
    "DEV_PORT_SIM",
    "DEV_PORT_USB",
    "ED_AUDIO_1",
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
    "ED_AUDIO_2",
    "ED_AUDIO_20",
    "ED_AUDIO_21",
    "ED_AUDIO_22",
    "ED_AUDIO_23",
    "ED_AUDIO_24",
    "ED_AUDIO_3",
    "ED_AUDIO_4",
    "ED_AUDIO_5",
    "ED_AUDIO_6",
    "ED_AUDIO_7",
    "ED_AUDIO_8",
    "ED_AUDIO_9",
    "ED_AUDIO_ALL",
    "ED_BASE",
    "ED_BOTTOM",
    "ED_CENTER",
    "ED_LEFT",
    "ED_MIDDLE",
    "ED_RIGHT",
    "ED_TOP",
    "ED_VIDEO",
    "ICreateDeviceAccessAsync",
    "IDeviceIoControl",
    "IDeviceRequestCompletionCallback",
]
