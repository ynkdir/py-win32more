from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.DeviceAccess
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
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
CLSID_DeviceIoControl: Guid = Guid('{12d3e372-874b-457d-9fdf-73977778686c}')
@winfunctype('deviceaccess.dll')
def CreateDeviceAccessInstance(deviceInterfacePath: win32more.Windows.Win32.Foundation.PWSTR, desiredAccess: UInt32, createAsync: POINTER(win32more.Windows.Win32.Devices.DeviceAccess.ICreateDeviceAccessAsync)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICreateDeviceAccessAsync(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3474628f-683d-42d2-abcb-db018c6503bc}')
    @commethod(3)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Wait(self, timeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetResult(self, riid: POINTER(Guid), deviceAccess: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDeviceIoControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9eefe161-23ab-4f18-9b49-991b586ae970}')
    @commethod(3)
    def DeviceIoControlSync(self, ioControlCode: UInt32, inputBuffer: POINTER(Byte), inputBufferSize: UInt32, outputBuffer: POINTER(Byte), outputBufferSize: UInt32, bytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeviceIoControlAsync(self, ioControlCode: UInt32, inputBuffer: POINTER(Byte), inputBufferSize: UInt32, outputBuffer: POINTER(Byte), outputBufferSize: UInt32, requestCompletionCallback: win32more.Windows.Win32.Devices.DeviceAccess.IDeviceRequestCompletionCallback, cancelContext: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CancelOperation(self, cancelContext: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDeviceRequestCompletionCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{999bad24-9acd-45bb-8669-2a2fc0288b04}')
    @commethod(3)
    def Invoke(self, requestResult: win32more.Windows.Win32.Foundation.HRESULT, bytesReturned: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
