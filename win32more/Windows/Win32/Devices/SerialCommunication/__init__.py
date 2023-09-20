from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.Properties
import win32more.Windows.Win32.Devices.SerialCommunication
import win32more.Windows.Win32.Foundation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def DEVPKEY_DeviceInterface_Serial_UsbVendorId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4c6bf15c-4c03-4aac-91f5-64c0f852bcf4}'), pid=2)
def DEVPKEY_DeviceInterface_Serial_UsbProductId():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4c6bf15c-4c03-4aac-91f5-64c0f852bcf4}'), pid=3)
def DEVPKEY_DeviceInterface_Serial_PortName():
    return Windows.Win32.Devices.Properties.DEVPROPKEY(fmtid=Guid('{4c6bf15c-4c03-4aac-91f5-64c0f852bcf4}'), pid=4)
IOCTL_SERIAL_SET_BAUD_RATE: UInt32 = 1769476
IOCTL_SERIAL_SET_QUEUE_SIZE: UInt32 = 1769480
IOCTL_SERIAL_SET_LINE_CONTROL: UInt32 = 1769484
IOCTL_SERIAL_SET_BREAK_ON: UInt32 = 1769488
IOCTL_SERIAL_SET_BREAK_OFF: UInt32 = 1769492
IOCTL_SERIAL_IMMEDIATE_CHAR: UInt32 = 1769496
IOCTL_SERIAL_SET_TIMEOUTS: UInt32 = 1769500
IOCTL_SERIAL_GET_TIMEOUTS: UInt32 = 1769504
IOCTL_SERIAL_SET_DTR: UInt32 = 1769508
IOCTL_SERIAL_CLR_DTR: UInt32 = 1769512
IOCTL_SERIAL_RESET_DEVICE: UInt32 = 1769516
IOCTL_SERIAL_SET_RTS: UInt32 = 1769520
IOCTL_SERIAL_CLR_RTS: UInt32 = 1769524
IOCTL_SERIAL_SET_XOFF: UInt32 = 1769528
IOCTL_SERIAL_SET_XON: UInt32 = 1769532
IOCTL_SERIAL_GET_WAIT_MASK: UInt32 = 1769536
IOCTL_SERIAL_SET_WAIT_MASK: UInt32 = 1769540
IOCTL_SERIAL_WAIT_ON_MASK: UInt32 = 1769544
IOCTL_SERIAL_PURGE: UInt32 = 1769548
IOCTL_SERIAL_GET_BAUD_RATE: UInt32 = 1769552
IOCTL_SERIAL_GET_LINE_CONTROL: UInt32 = 1769556
IOCTL_SERIAL_GET_CHARS: UInt32 = 1769560
IOCTL_SERIAL_SET_CHARS: UInt32 = 1769564
IOCTL_SERIAL_GET_HANDFLOW: UInt32 = 1769568
IOCTL_SERIAL_SET_HANDFLOW: UInt32 = 1769572
IOCTL_SERIAL_GET_MODEMSTATUS: UInt32 = 1769576
IOCTL_SERIAL_GET_COMMSTATUS: UInt32 = 1769580
IOCTL_SERIAL_XOFF_COUNTER: UInt32 = 1769584
IOCTL_SERIAL_GET_PROPERTIES: UInt32 = 1769588
IOCTL_SERIAL_GET_DTRRTS: UInt32 = 1769592
IOCTL_SERIAL_CONFIG_SIZE: UInt32 = 1769600
IOCTL_SERIAL_GET_COMMCONFIG: UInt32 = 1769604
IOCTL_SERIAL_SET_COMMCONFIG: UInt32 = 1769608
IOCTL_SERIAL_GET_STATS: UInt32 = 1769612
IOCTL_SERIAL_CLEAR_STATS: UInt32 = 1769616
IOCTL_SERIAL_GET_MODEM_CONTROL: UInt32 = 1769620
IOCTL_SERIAL_SET_MODEM_CONTROL: UInt32 = 1769624
IOCTL_SERIAL_SET_FIFO_CONTROL: UInt32 = 1769628
IOCTL_SERIAL_APPLY_DEFAULT_CONFIGURATION: UInt32 = 1769632
IOCTL_SERIAL_SET_INTERVAL_TIMER_RESOLUTION: UInt32 = 1769636
IOCTL_SERIAL_INTERNAL_DO_WAIT_WAKE: UInt32 = 1769476
IOCTL_SERIAL_INTERNAL_CANCEL_WAIT_WAKE: UInt32 = 1769480
IOCTL_SERIAL_INTERNAL_BASIC_SETTINGS: UInt32 = 1769484
IOCTL_SERIAL_INTERNAL_RESTORE_SETTINGS: UInt32 = 1769488
SERIAL_EV_RXCHAR: UInt32 = 1
SERIAL_EV_RXFLAG: UInt32 = 2
SERIAL_EV_TXEMPTY: UInt32 = 4
SERIAL_EV_CTS: UInt32 = 8
SERIAL_EV_DSR: UInt32 = 16
SERIAL_EV_RLSD: UInt32 = 32
SERIAL_EV_BREAK: UInt32 = 64
SERIAL_EV_ERR: UInt32 = 128
SERIAL_EV_RING: UInt32 = 256
SERIAL_EV_PERR: UInt32 = 512
SERIAL_EV_RX80FULL: UInt32 = 1024
SERIAL_EV_EVENT1: UInt32 = 2048
SERIAL_EV_EVENT2: UInt32 = 4096
SERIAL_PURGE_TXABORT: UInt32 = 1
SERIAL_PURGE_RXABORT: UInt32 = 2
SERIAL_PURGE_TXCLEAR: UInt32 = 4
SERIAL_PURGE_RXCLEAR: UInt32 = 8
STOP_BIT_1: UInt32 = 0
STOP_BITS_1_5: UInt32 = 1
STOP_BITS_2: UInt32 = 2
NO_PARITY: UInt32 = 0
ODD_PARITY: UInt32 = 1
EVEN_PARITY: UInt32 = 2
MARK_PARITY: UInt32 = 3
SPACE_PARITY: UInt32 = 4
SERIAL_LSRMST_ESCAPE: UInt16 = 0
SERIAL_LSRMST_LSR_DATA: UInt16 = 1
SERIAL_LSRMST_LSR_NODATA: UInt16 = 2
SERIAL_LSRMST_MST: UInt16 = 3
IOCTL_INTERNAL_SERENUM_REMOVE_SELF: UInt32 = 3604999
COMDB_MIN_PORTS_ARBITRATED: UInt32 = 256
COMDB_MAX_PORTS_ARBITRATED: UInt32 = 4096
CDB_REPORT_BITS: UInt32 = 0
CDB_REPORT_BYTES: UInt32 = 1
@winfunctype('MSPORTS.dll')
def ComDBOpen(PHComDB: POINTER(win32more.Windows.Win32.Devices.SerialCommunication.HCOMDB)) -> Int32: ...
@winfunctype('MSPORTS.dll')
def ComDBClose(HComDB: win32more.Windows.Win32.Devices.SerialCommunication.HCOMDB) -> Int32: ...
@winfunctype('MSPORTS.dll')
def ComDBGetCurrentPortUsage(HComDB: win32more.Windows.Win32.Devices.SerialCommunication.HCOMDB, Buffer: POINTER(Byte), BufferSize: UInt32, ReportType: UInt32, MaxPortsReported: POINTER(UInt32)) -> Int32: ...
@winfunctype('MSPORTS.dll')
def ComDBClaimNextFreePort(HComDB: win32more.Windows.Win32.Devices.SerialCommunication.HCOMDB, ComNumber: POINTER(UInt32)) -> Int32: ...
@winfunctype('MSPORTS.dll')
def ComDBClaimPort(HComDB: win32more.Windows.Win32.Devices.SerialCommunication.HCOMDB, ComNumber: UInt32, ForceClaim: win32more.Windows.Win32.Foundation.BOOL, Forced: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> Int32: ...
@winfunctype('MSPORTS.dll')
def ComDBReleasePort(HComDB: win32more.Windows.Win32.Devices.SerialCommunication.HCOMDB, ComNumber: UInt32) -> Int32: ...
@winfunctype('MSPORTS.dll')
def ComDBResizeDatabase(HComDB: win32more.Windows.Win32.Devices.SerialCommunication.HCOMDB, NewSize: UInt32) -> Int32: ...
HCOMDB = IntPtr
@winfunctype_pointer
def PSERENUM_READPORT(SerPortAddress: VoidPtr) -> Byte: ...
@winfunctype_pointer
def PSERENUM_WRITEPORT(SerPortAddress: VoidPtr, Value: Byte) -> Void: ...
SERENUM_PORTION = Int32
SERENUM_PORTION_SerenumFirstHalf: SERENUM_PORTION = 0
SERENUM_PORTION_SerenumSecondHalf: SERENUM_PORTION = 1
SERENUM_PORTION_SerenumWhole: SERENUM_PORTION = 2
class SERENUM_PORT_DESC(EasyCastStructure):
    Size: UInt32
    PortHandle: VoidPtr
    PortAddress: Int64
    Reserved: UInt16 * 1
class SERENUM_PORT_PARAMETERS(EasyCastStructure):
    Size: UInt32
    ReadAccessor: win32more.Windows.Win32.Devices.SerialCommunication.PSERENUM_READPORT
    WriteAccessor: win32more.Windows.Win32.Devices.SerialCommunication.PSERENUM_WRITEPORT
    SerPortAddress: VoidPtr
    HardwareHandle: VoidPtr
    Portion: win32more.Windows.Win32.Devices.SerialCommunication.SERENUM_PORTION
    NumberAxis: UInt16
    Reserved: UInt16 * 3
class SERIALCONFIG(EasyCastStructure):
    Size: UInt32
    Version: UInt16
    SubType: UInt32
    ProvOffset: UInt32
    ProviderSize: UInt32
    ProviderData: Char * 1
class SERIALPERF_STATS(EasyCastStructure):
    ReceivedCount: UInt32
    TransmittedCount: UInt32
    FrameErrorCount: UInt32
    SerialOverrunErrorCount: UInt32
    BufferOverrunErrorCount: UInt32
    ParityErrorCount: UInt32
class SERIAL_BASIC_SETTINGS(EasyCastStructure):
    Timeouts: win32more.Windows.Win32.Devices.SerialCommunication.SERIAL_TIMEOUTS
    HandFlow: win32more.Windows.Win32.Devices.SerialCommunication.SERIAL_HANDFLOW
    RxFifo: UInt32
    TxFifo: UInt32
class SERIAL_BAUD_RATE(EasyCastStructure):
    BaudRate: UInt32
class SERIAL_CHARS(EasyCastStructure):
    EofChar: Byte
    ErrorChar: Byte
    BreakChar: Byte
    EventChar: Byte
    XonChar: Byte
    XoffChar: Byte
class SERIAL_COMMPROP(EasyCastStructure):
    PacketLength: UInt16
    PacketVersion: UInt16
    ServiceMask: UInt32
    Reserved1: UInt32
    MaxTxQueue: UInt32
    MaxRxQueue: UInt32
    MaxBaud: UInt32
    ProvSubType: UInt32
    ProvCapabilities: UInt32
    SettableParams: UInt32
    SettableBaud: UInt32
    SettableData: UInt16
    SettableStopParity: UInt16
    CurrentTxQueue: UInt32
    CurrentRxQueue: UInt32
    ProvSpec1: UInt32
    ProvSpec2: UInt32
    ProvChar: Char * 1
class SERIAL_HANDFLOW(EasyCastStructure):
    ControlHandShake: UInt32
    FlowReplace: UInt32
    XonLimit: Int32
    XoffLimit: Int32
class SERIAL_LINE_CONTROL(EasyCastStructure):
    StopBits: Byte
    Parity: Byte
    WordLength: Byte
class SERIAL_QUEUE_SIZE(EasyCastStructure):
    InSize: UInt32
    OutSize: UInt32
class SERIAL_STATUS(EasyCastStructure):
    Errors: UInt32
    HoldReasons: UInt32
    AmountInInQueue: UInt32
    AmountInOutQueue: UInt32
    EofReceived: win32more.Windows.Win32.Foundation.BOOLEAN
    WaitForImmediate: win32more.Windows.Win32.Foundation.BOOLEAN
class SERIAL_TIMEOUTS(EasyCastStructure):
    ReadIntervalTimeout: UInt32
    ReadTotalTimeoutMultiplier: UInt32
    ReadTotalTimeoutConstant: UInt32
    WriteTotalTimeoutMultiplier: UInt32
    WriteTotalTimeoutConstant: UInt32
class SERIAL_XOFF_COUNTER(EasyCastStructure):
    Timeout: UInt32
    Counter: Int32
    XoffChar: Byte
make_head(_module, 'DEVPKEY_DeviceInterface_Serial_UsbVendorId')
make_head(_module, 'DEVPKEY_DeviceInterface_Serial_UsbProductId')
make_head(_module, 'DEVPKEY_DeviceInterface_Serial_PortName')
make_head(_module, 'PSERENUM_READPORT')
make_head(_module, 'PSERENUM_WRITEPORT')
make_head(_module, 'SERENUM_PORT_DESC')
make_head(_module, 'SERENUM_PORT_PARAMETERS')
make_head(_module, 'SERIALCONFIG')
make_head(_module, 'SERIALPERF_STATS')
make_head(_module, 'SERIAL_BASIC_SETTINGS')
make_head(_module, 'SERIAL_BAUD_RATE')
make_head(_module, 'SERIAL_CHARS')
make_head(_module, 'SERIAL_COMMPROP')
make_head(_module, 'SERIAL_HANDFLOW')
make_head(_module, 'SERIAL_LINE_CONTROL')
make_head(_module, 'SERIAL_QUEUE_SIZE')
make_head(_module, 'SERIAL_STATUS')
make_head(_module, 'SERIAL_TIMEOUTS')
make_head(_module, 'SERIAL_XOFF_COUNTER')
