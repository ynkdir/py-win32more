from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.Communication
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.IO
MDM_COMPRESSION: UInt32 = 1
MDM_ERROR_CONTROL: UInt32 = 2
MDM_FORCED_EC: UInt32 = 4
MDM_CELLULAR: UInt32 = 8
MDM_FLOWCONTROL_HARD: UInt32 = 16
MDM_FLOWCONTROL_SOFT: UInt32 = 32
MDM_CCITT_OVERRIDE: UInt32 = 64
MDM_SPEED_ADJUST: UInt32 = 128
MDM_TONE_DIAL: UInt32 = 256
MDM_BLIND_DIAL: UInt32 = 512
MDM_V23_OVERRIDE: UInt32 = 1024
MDM_DIAGNOSTICS: UInt32 = 2048
MDM_MASK_BEARERMODE: UInt32 = 61440
MDM_SHIFT_BEARERMODE: UInt32 = 12
MDM_MASK_PROTOCOLID: UInt32 = 983040
MDM_SHIFT_PROTOCOLID: UInt32 = 16
MDM_MASK_PROTOCOLDATA: UInt32 = 267386880
MDM_SHIFT_PROTOCOLDATA: UInt32 = 20
MDM_SHIFT_PROTOCOLINFO: UInt32 = 16
MDM_SHIFT_EXTENDEDINFO: UInt32 = 12
MDM_BEARERMODE_ANALOG: UInt32 = 0
MDM_BEARERMODE_ISDN: UInt32 = 1
MDM_BEARERMODE_GSM: UInt32 = 2
MDM_PROTOCOLID_DEFAULT: UInt32 = 0
MDM_PROTOCOLID_HDLCPPP: UInt32 = 1
MDM_PROTOCOLID_V128: UInt32 = 2
MDM_PROTOCOLID_X75: UInt32 = 3
MDM_PROTOCOLID_V110: UInt32 = 4
MDM_PROTOCOLID_V120: UInt32 = 5
MDM_PROTOCOLID_AUTO: UInt32 = 6
MDM_PROTOCOLID_ANALOG: UInt32 = 7
MDM_PROTOCOLID_GPRS: UInt32 = 8
MDM_PROTOCOLID_PIAFS: UInt32 = 9
MDM_SHIFT_HDLCPPP_SPEED: UInt32 = 0
MDM_MASK_HDLCPPP_SPEED: UInt32 = 7
MDM_HDLCPPP_SPEED_DEFAULT: UInt32 = 0
MDM_HDLCPPP_SPEED_64K: UInt32 = 1
MDM_HDLCPPP_SPEED_56K: UInt32 = 2
MDM_SHIFT_HDLCPPP_AUTH: UInt32 = 3
MDM_HDLCPPP_AUTH_DEFAULT: UInt32 = 0
MDM_HDLCPPP_AUTH_NONE: UInt32 = 1
MDM_HDLCPPP_AUTH_PAP: UInt32 = 2
MDM_HDLCPPP_AUTH_CHAP: UInt32 = 3
MDM_HDLCPPP_AUTH_MSCHAP: UInt32 = 4
MDM_SHIFT_HDLCPPP_ML: UInt32 = 6
MDM_HDLCPPP_ML_DEFAULT: UInt32 = 0
MDM_HDLCPPP_ML_NONE: UInt32 = 1
MDM_HDLCPPP_ML_2: UInt32 = 2
MDM_SHIFT_V120_SPEED: UInt32 = 0
MDM_MASK_V120_SPEED: UInt32 = 7
MDM_V120_SPEED_DEFAULT: UInt32 = 0
MDM_V120_SPEED_64K: UInt32 = 1
MDM_V120_SPEED_56K: UInt32 = 2
MDM_SHIFT_V120_ML: UInt32 = 6
MDM_V120_ML_DEFAULT: UInt32 = 0
MDM_V120_ML_NONE: UInt32 = 1
MDM_V120_ML_2: UInt32 = 2
MDM_SHIFT_X75_DATA: UInt32 = 0
MDM_MASK_X75_DATA: UInt32 = 7
MDM_X75_DATA_DEFAULT: UInt32 = 0
MDM_X75_DATA_64K: UInt32 = 1
MDM_X75_DATA_128K: UInt32 = 2
MDM_X75_DATA_T_70: UInt32 = 3
MDM_X75_DATA_BTX: UInt32 = 4
MDM_SHIFT_V110_SPEED: UInt32 = 0
MDM_MASK_V110_SPEED: UInt32 = 15
MDM_V110_SPEED_DEFAULT: UInt32 = 0
MDM_V110_SPEED_1DOT2K: UInt32 = 1
MDM_V110_SPEED_2DOT4K: UInt32 = 2
MDM_V110_SPEED_4DOT8K: UInt32 = 3
MDM_V110_SPEED_9DOT6K: UInt32 = 4
MDM_V110_SPEED_12DOT0K: UInt32 = 5
MDM_V110_SPEED_14DOT4K: UInt32 = 6
MDM_V110_SPEED_19DOT2K: UInt32 = 7
MDM_V110_SPEED_28DOT8K: UInt32 = 8
MDM_V110_SPEED_38DOT4K: UInt32 = 9
MDM_V110_SPEED_57DOT6K: UInt32 = 10
MDM_SHIFT_AUTO_SPEED: UInt32 = 0
MDM_MASK_AUTO_SPEED: UInt32 = 7
MDM_AUTO_SPEED_DEFAULT: UInt32 = 0
MDM_SHIFT_AUTO_ML: UInt32 = 6
MDM_AUTO_ML_DEFAULT: UInt32 = 0
MDM_AUTO_ML_NONE: UInt32 = 1
MDM_AUTO_ML_2: UInt32 = 2
MDM_ANALOG_RLP_ON: UInt32 = 0
MDM_ANALOG_RLP_OFF: UInt32 = 1
MDM_ANALOG_V34: UInt32 = 2
MDM_PIAFS_INCOMING: UInt32 = 0
MDM_PIAFS_OUTGOING: UInt32 = 1
SID_3GPP_SUPSVCMODEL: Guid = Guid('{d7d08e07-d767-4478-b14a-eecc87ea12f7}')
MAXLENGTH_NAI: UInt32 = 72
MAXLENGTH_UICCDATASTORE: UInt32 = 10
@winfunctype('KERNEL32.dll')
def ClearCommBreak(hFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ClearCommError(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpErrors: POINTER(win32more.Windows.Win32.Devices.Communication.CLEAR_COMM_ERROR_FLAGS), lpStat: POINTER(win32more.Windows.Win32.Devices.Communication.COMSTAT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetupComm(hFile: win32more.Windows.Win32.Foundation.HANDLE, dwInQueue: UInt32, dwOutQueue: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EscapeCommFunction(hFile: win32more.Windows.Win32.Foundation.HANDLE, dwFunc: win32more.Windows.Win32.Devices.Communication.ESCAPE_COMM_FUNCTION) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCommConfig(hCommDev: win32more.Windows.Win32.Foundation.HANDLE, lpCC: POINTER(win32more.Windows.Win32.Devices.Communication.COMMCONFIG), lpdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCommMask(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpEvtMask: POINTER(win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCommProperties(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpCommProp: POINTER(win32more.Windows.Win32.Devices.Communication.COMMPROP)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCommModemStatus(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpModemStat: POINTER(win32more.Windows.Win32.Devices.Communication.MODEM_STATUS_FLAGS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCommState(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpDCB: POINTER(win32more.Windows.Win32.Devices.Communication.DCB)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCommTimeouts(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpCommTimeouts: POINTER(win32more.Windows.Win32.Devices.Communication.COMMTIMEOUTS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PurgeComm(hFile: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.Devices.Communication.PURGE_COMM_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCommBreak(hFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCommConfig(hCommDev: win32more.Windows.Win32.Foundation.HANDLE, lpCC: POINTER(win32more.Windows.Win32.Devices.Communication.COMMCONFIG), dwSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCommMask(hFile: win32more.Windows.Win32.Foundation.HANDLE, dwEvtMask: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCommState(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpDCB: POINTER(win32more.Windows.Win32.Devices.Communication.DCB)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCommTimeouts(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpCommTimeouts: POINTER(win32more.Windows.Win32.Devices.Communication.COMMTIMEOUTS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def TransmitCommChar(hFile: win32more.Windows.Win32.Foundation.HANDLE, cChar: win32more.Windows.Win32.Foundation.CHAR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WaitCommEvent(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpEvtMask: POINTER(win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-comm-l1-1-1.dll')
def OpenCommPort(uPortNumber: UInt32, dwDesiredAccess: UInt32, dwFlagsAndAttributes: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-comm-l1-1-2.dll')
def GetCommPorts(lpPortNumbers: POINTER(UInt32), uPortNumbersCount: UInt32, puPortNumbersFound: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def BuildCommDCBA(lpDef: win32more.Windows.Win32.Foundation.PSTR, lpDCB: POINTER(win32more.Windows.Win32.Devices.Communication.DCB)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BuildCommDCBW(lpDef: win32more.Windows.Win32.Foundation.PWSTR, lpDCB: POINTER(win32more.Windows.Win32.Devices.Communication.DCB)) -> win32more.Windows.Win32.Foundation.BOOL: ...
BuildCommDCB = UnicodeAlias('BuildCommDCBW')
@winfunctype('KERNEL32.dll')
def BuildCommDCBAndTimeoutsA(lpDef: win32more.Windows.Win32.Foundation.PSTR, lpDCB: POINTER(win32more.Windows.Win32.Devices.Communication.DCB), lpCommTimeouts: POINTER(win32more.Windows.Win32.Devices.Communication.COMMTIMEOUTS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BuildCommDCBAndTimeoutsW(lpDef: win32more.Windows.Win32.Foundation.PWSTR, lpDCB: POINTER(win32more.Windows.Win32.Devices.Communication.DCB), lpCommTimeouts: POINTER(win32more.Windows.Win32.Devices.Communication.COMMTIMEOUTS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
BuildCommDCBAndTimeouts = UnicodeAlias('BuildCommDCBAndTimeoutsW')
@winfunctype('KERNEL32.dll')
def CommConfigDialogA(lpszName: win32more.Windows.Win32.Foundation.PSTR, hWnd: win32more.Windows.Win32.Foundation.HWND, lpCC: POINTER(win32more.Windows.Win32.Devices.Communication.COMMCONFIG)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CommConfigDialogW(lpszName: win32more.Windows.Win32.Foundation.PWSTR, hWnd: win32more.Windows.Win32.Foundation.HWND, lpCC: POINTER(win32more.Windows.Win32.Devices.Communication.COMMCONFIG)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CommConfigDialog = UnicodeAlias('CommConfigDialogW')
@winfunctype('KERNEL32.dll')
def GetDefaultCommConfigA(lpszName: win32more.Windows.Win32.Foundation.PSTR, lpCC: POINTER(win32more.Windows.Win32.Devices.Communication.COMMCONFIG), lpdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDefaultCommConfigW(lpszName: win32more.Windows.Win32.Foundation.PWSTR, lpCC: POINTER(win32more.Windows.Win32.Devices.Communication.COMMCONFIG), lpdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetDefaultCommConfig = UnicodeAlias('GetDefaultCommConfigW')
@winfunctype('KERNEL32.dll')
def SetDefaultCommConfigA(lpszName: win32more.Windows.Win32.Foundation.PSTR, lpCC: POINTER(win32more.Windows.Win32.Devices.Communication.COMMCONFIG), dwSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDefaultCommConfigW(lpszName: win32more.Windows.Win32.Foundation.PWSTR, lpCC: POINTER(win32more.Windows.Win32.Devices.Communication.COMMCONFIG), dwSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetDefaultCommConfig = UnicodeAlias('SetDefaultCommConfigW')
CLEAR_COMM_ERROR_FLAGS = UInt32
CE_BREAK: win32more.Windows.Win32.Devices.Communication.CLEAR_COMM_ERROR_FLAGS = 16
CE_FRAME: win32more.Windows.Win32.Devices.Communication.CLEAR_COMM_ERROR_FLAGS = 8
CE_OVERRUN: win32more.Windows.Win32.Devices.Communication.CLEAR_COMM_ERROR_FLAGS = 2
CE_RXOVER: win32more.Windows.Win32.Devices.Communication.CLEAR_COMM_ERROR_FLAGS = 1
CE_RXPARITY: win32more.Windows.Win32.Devices.Communication.CLEAR_COMM_ERROR_FLAGS = 4
class COMMCONFIG(Structure):
    dwSize: UInt32
    wVersion: UInt16
    wReserved: UInt16
    dcb: win32more.Windows.Win32.Devices.Communication.DCB
    dwProviderSubType: UInt32
    dwProviderOffset: UInt32
    dwProviderSize: UInt32
    wcProviderData: Char * 1
class COMMPROP(Structure):
    wPacketLength: UInt16
    wPacketVersion: UInt16
    dwServiceMask: UInt32
    dwReserved1: UInt32
    dwMaxTxQueue: UInt32
    dwMaxRxQueue: UInt32
    dwMaxBaud: UInt32
    dwProvSubType: UInt32
    dwProvCapabilities: UInt32
    dwSettableParams: UInt32
    dwSettableBaud: UInt32
    wSettableData: UInt16
    wSettableStopParity: win32more.Windows.Win32.Devices.Communication.COMMPROP_STOP_PARITY
    dwCurrentTxQueue: UInt32
    dwCurrentRxQueue: UInt32
    dwProvSpec1: UInt32
    dwProvSpec2: UInt32
    wcProvChar: Char * 1
COMMPROP_STOP_PARITY = UInt16
STOPBITS_10: win32more.Windows.Win32.Devices.Communication.COMMPROP_STOP_PARITY = 1
STOPBITS_15: win32more.Windows.Win32.Devices.Communication.COMMPROP_STOP_PARITY = 2
STOPBITS_20: win32more.Windows.Win32.Devices.Communication.COMMPROP_STOP_PARITY = 4
PARITY_NONE: win32more.Windows.Win32.Devices.Communication.COMMPROP_STOP_PARITY = 256
PARITY_ODD: win32more.Windows.Win32.Devices.Communication.COMMPROP_STOP_PARITY = 512
PARITY_EVEN: win32more.Windows.Win32.Devices.Communication.COMMPROP_STOP_PARITY = 1024
PARITY_MARK: win32more.Windows.Win32.Devices.Communication.COMMPROP_STOP_PARITY = 2048
PARITY_SPACE: win32more.Windows.Win32.Devices.Communication.COMMPROP_STOP_PARITY = 4096
class COMMTIMEOUTS(Structure):
    ReadIntervalTimeout: UInt32
    ReadTotalTimeoutMultiplier: UInt32
    ReadTotalTimeoutConstant: UInt32
    WriteTotalTimeoutMultiplier: UInt32
    WriteTotalTimeoutConstant: UInt32
COMM_EVENT_MASK = UInt32
EV_BREAK: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK = 64
EV_CTS: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK = 8
EV_DSR: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK = 16
EV_ERR: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK = 128
EV_EVENT1: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK = 2048
EV_EVENT2: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK = 4096
EV_PERR: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK = 512
EV_RING: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK = 256
EV_RLSD: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK = 32
EV_RX80FULL: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK = 1024
EV_RXCHAR: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK = 1
EV_RXFLAG: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK = 2
EV_TXEMPTY: win32more.Windows.Win32.Devices.Communication.COMM_EVENT_MASK = 4
class COMSTAT(Structure):
    fCtsHold: Annotated[UInt32, 1]
    fDsrHold: Annotated[UInt32, 1]
    fRlsdHold: Annotated[UInt32, 1]
    fXoffHold: Annotated[UInt32, 1]
    fXoffSent: Annotated[UInt32, 1]
    fEof: Annotated[UInt32, 1]
    fTxim: Annotated[UInt32, 1]
    fReserved: Annotated[UInt32, 25]
    cbInQue: UInt32
    cbOutQue: UInt32
class DCB(Structure):
    DCBlength: UInt32
    BaudRate: UInt32
    fBinary: Annotated[UInt32, 1]
    fParity: Annotated[UInt32, 1]
    fOutxCtsFlow: Annotated[UInt32, 1]
    fOutxDsrFlow: Annotated[UInt32, 1]
    fDtrControl: Annotated[UInt32, 2]
    fDsrSensitivity: Annotated[UInt32, 1]
    fTXContinueOnXoff: Annotated[UInt32, 1]
    fOutX: Annotated[UInt32, 1]
    fInX: Annotated[UInt32, 1]
    fErrorChar: Annotated[UInt32, 1]
    fNull: Annotated[UInt32, 1]
    fRtsControl: Annotated[UInt32, 2]
    fAbortOnError: Annotated[UInt32, 1]
    fDummy2: Annotated[UInt32, 17]
    wReserved: UInt16
    XonLim: UInt16
    XoffLim: UInt16
    ByteSize: Byte
    Parity: win32more.Windows.Win32.Devices.Communication.DCB_PARITY
    StopBits: win32more.Windows.Win32.Devices.Communication.DCB_STOP_BITS
    XonChar: win32more.Windows.Win32.Foundation.CHAR
    XoffChar: win32more.Windows.Win32.Foundation.CHAR
    ErrorChar: win32more.Windows.Win32.Foundation.CHAR
    EofChar: win32more.Windows.Win32.Foundation.CHAR
    EvtChar: win32more.Windows.Win32.Foundation.CHAR
    wReserved1: UInt16
DCB_PARITY = Byte
EVENPARITY: win32more.Windows.Win32.Devices.Communication.DCB_PARITY = 2
MARKPARITY: win32more.Windows.Win32.Devices.Communication.DCB_PARITY = 3
NOPARITY: win32more.Windows.Win32.Devices.Communication.DCB_PARITY = 0
ODDPARITY: win32more.Windows.Win32.Devices.Communication.DCB_PARITY = 1
SPACEPARITY: win32more.Windows.Win32.Devices.Communication.DCB_PARITY = 4
DCB_STOP_BITS = Byte
ONESTOPBIT: win32more.Windows.Win32.Devices.Communication.DCB_STOP_BITS = 0
ONE5STOPBITS: win32more.Windows.Win32.Devices.Communication.DCB_STOP_BITS = 1
TWOSTOPBITS: win32more.Windows.Win32.Devices.Communication.DCB_STOP_BITS = 2
ESCAPE_COMM_FUNCTION = UInt32
CLRBREAK: win32more.Windows.Win32.Devices.Communication.ESCAPE_COMM_FUNCTION = 9
CLRDTR: win32more.Windows.Win32.Devices.Communication.ESCAPE_COMM_FUNCTION = 6
CLRRTS: win32more.Windows.Win32.Devices.Communication.ESCAPE_COMM_FUNCTION = 4
SETBREAK: win32more.Windows.Win32.Devices.Communication.ESCAPE_COMM_FUNCTION = 8
SETDTR: win32more.Windows.Win32.Devices.Communication.ESCAPE_COMM_FUNCTION = 5
SETRTS: win32more.Windows.Win32.Devices.Communication.ESCAPE_COMM_FUNCTION = 3
SETXOFF: win32more.Windows.Win32.Devices.Communication.ESCAPE_COMM_FUNCTION = 1
SETXON: win32more.Windows.Win32.Devices.Communication.ESCAPE_COMM_FUNCTION = 2
class MODEMDEVCAPS(Structure):
    dwActualSize: UInt32
    dwRequiredSize: UInt32
    dwDevSpecificOffset: UInt32
    dwDevSpecificSize: UInt32
    dwModemProviderVersion: UInt32
    dwModemManufacturerOffset: UInt32
    dwModemManufacturerSize: UInt32
    dwModemModelOffset: UInt32
    dwModemModelSize: UInt32
    dwModemVersionOffset: UInt32
    dwModemVersionSize: UInt32
    dwDialOptions: win32more.Windows.Win32.Devices.Communication.MODEMDEVCAPS_DIAL_OPTIONS
    dwCallSetupFailTimer: UInt32
    dwInactivityTimeout: UInt32
    dwSpeakerVolume: win32more.Windows.Win32.Devices.Communication.MODEMDEVCAPS_SPEAKER_VOLUME
    dwSpeakerMode: win32more.Windows.Win32.Devices.Communication.MODEMDEVCAPS_SPEAKER_MODE
    dwModemOptions: UInt32
    dwMaxDTERate: UInt32
    dwMaxDCERate: UInt32
    abVariablePortion: Byte * 1
MODEMDEVCAPS_DIAL_OPTIONS = UInt32
DIALOPTION_BILLING: win32more.Windows.Win32.Devices.Communication.MODEMDEVCAPS_DIAL_OPTIONS = 64
DIALOPTION_DIALTONE: win32more.Windows.Win32.Devices.Communication.MODEMDEVCAPS_DIAL_OPTIONS = 256
DIALOPTION_QUIET: win32more.Windows.Win32.Devices.Communication.MODEMDEVCAPS_DIAL_OPTIONS = 128
MODEMDEVCAPS_SPEAKER_MODE = UInt32
MDMSPKRFLAG_CALLSETUP: win32more.Windows.Win32.Devices.Communication.MODEMDEVCAPS_SPEAKER_MODE = 8
MDMSPKRFLAG_DIAL: win32more.Windows.Win32.Devices.Communication.MODEMDEVCAPS_SPEAKER_MODE = 2
MDMSPKRFLAG_OFF: win32more.Windows.Win32.Devices.Communication.MODEMDEVCAPS_SPEAKER_MODE = 1
MDMSPKRFLAG_ON: win32more.Windows.Win32.Devices.Communication.MODEMDEVCAPS_SPEAKER_MODE = 4
MODEMDEVCAPS_SPEAKER_VOLUME = UInt32
MDMVOLFLAG_HIGH: win32more.Windows.Win32.Devices.Communication.MODEMDEVCAPS_SPEAKER_VOLUME = 4
MDMVOLFLAG_LOW: win32more.Windows.Win32.Devices.Communication.MODEMDEVCAPS_SPEAKER_VOLUME = 1
MDMVOLFLAG_MEDIUM: win32more.Windows.Win32.Devices.Communication.MODEMDEVCAPS_SPEAKER_VOLUME = 2
class MODEMSETTINGS(Structure):
    dwActualSize: UInt32
    dwRequiredSize: UInt32
    dwDevSpecificOffset: UInt32
    dwDevSpecificSize: UInt32
    dwCallSetupFailTimer: UInt32
    dwInactivityTimeout: UInt32
    dwSpeakerVolume: win32more.Windows.Win32.Devices.Communication.MODEM_SPEAKER_VOLUME
    dwSpeakerMode: win32more.Windows.Win32.Devices.Communication.MODEMSETTINGS_SPEAKER_MODE
    dwPreferredModemOptions: UInt32
    dwNegotiatedModemOptions: UInt32
    dwNegotiatedDCERate: UInt32
    abVariablePortion: Byte * 1
MODEMSETTINGS_SPEAKER_MODE = UInt32
MDMSPKR_CALLSETUP: win32more.Windows.Win32.Devices.Communication.MODEMSETTINGS_SPEAKER_MODE = 8
MDMSPKR_DIAL: win32more.Windows.Win32.Devices.Communication.MODEMSETTINGS_SPEAKER_MODE = 2
MDMSPKR_OFF: win32more.Windows.Win32.Devices.Communication.MODEMSETTINGS_SPEAKER_MODE = 1
MDMSPKR_ON: win32more.Windows.Win32.Devices.Communication.MODEMSETTINGS_SPEAKER_MODE = 4
MODEM_SPEAKER_VOLUME = UInt32
MDMVOL_HIGH: win32more.Windows.Win32.Devices.Communication.MODEM_SPEAKER_VOLUME = 2
MDMVOL_LOW: win32more.Windows.Win32.Devices.Communication.MODEM_SPEAKER_VOLUME = 0
MDMVOL_MEDIUM: win32more.Windows.Win32.Devices.Communication.MODEM_SPEAKER_VOLUME = 1
MODEM_STATUS_FLAGS = UInt32
MS_CTS_ON: win32more.Windows.Win32.Devices.Communication.MODEM_STATUS_FLAGS = 16
MS_DSR_ON: win32more.Windows.Win32.Devices.Communication.MODEM_STATUS_FLAGS = 32
MS_RING_ON: win32more.Windows.Win32.Devices.Communication.MODEM_STATUS_FLAGS = 64
MS_RLSD_ON: win32more.Windows.Win32.Devices.Communication.MODEM_STATUS_FLAGS = 128
PURGE_COMM_FLAGS = UInt32
PURGE_RXABORT: win32more.Windows.Win32.Devices.Communication.PURGE_COMM_FLAGS = 2
PURGE_RXCLEAR: win32more.Windows.Win32.Devices.Communication.PURGE_COMM_FLAGS = 8
PURGE_TXABORT: win32more.Windows.Win32.Devices.Communication.PURGE_COMM_FLAGS = 1
PURGE_TXCLEAR: win32more.Windows.Win32.Devices.Communication.PURGE_COMM_FLAGS = 4


make_ready(__name__)
