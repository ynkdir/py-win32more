from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Devices.Communication
import Windows.Win32.Foundation
import Windows.Win32.System.IO
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
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
SID_3GPP_SUPSVCMODEL: Guid = Guid('d7d08e07-d767-4478-b1-4a-ee-cc-87-ea-12-f7')
MAXLENGTH_NAI: UInt32 = 72
MAXLENGTH_UICCDATASTORE: UInt32 = 10
@winfunctype('KERNEL32.dll')
def ClearCommBreak(hFile: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ClearCommError(hFile: Windows.Win32.Foundation.HANDLE, lpErrors: POINTER(Windows.Win32.Devices.Communication.CLEAR_COMM_ERROR_FLAGS), lpStat: POINTER(Windows.Win32.Devices.Communication.COMSTAT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetupComm(hFile: Windows.Win32.Foundation.HANDLE, dwInQueue: UInt32, dwOutQueue: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EscapeCommFunction(hFile: Windows.Win32.Foundation.HANDLE, dwFunc: Windows.Win32.Devices.Communication.ESCAPE_COMM_FUNCTION) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCommConfig(hCommDev: Windows.Win32.Foundation.HANDLE, lpCC: POINTER(Windows.Win32.Devices.Communication.COMMCONFIG_head), lpdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCommMask(hFile: Windows.Win32.Foundation.HANDLE, lpEvtMask: POINTER(Windows.Win32.Devices.Communication.COMM_EVENT_MASK)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCommProperties(hFile: Windows.Win32.Foundation.HANDLE, lpCommProp: POINTER(Windows.Win32.Devices.Communication.COMMPROP_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCommModemStatus(hFile: Windows.Win32.Foundation.HANDLE, lpModemStat: POINTER(Windows.Win32.Devices.Communication.MODEM_STATUS_FLAGS)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCommState(hFile: Windows.Win32.Foundation.HANDLE, lpDCB: POINTER(Windows.Win32.Devices.Communication.DCB_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCommTimeouts(hFile: Windows.Win32.Foundation.HANDLE, lpCommTimeouts: POINTER(Windows.Win32.Devices.Communication.COMMTIMEOUTS_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PurgeComm(hFile: Windows.Win32.Foundation.HANDLE, dwFlags: Windows.Win32.Devices.Communication.PURGE_COMM_FLAGS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCommBreak(hFile: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCommConfig(hCommDev: Windows.Win32.Foundation.HANDLE, lpCC: POINTER(Windows.Win32.Devices.Communication.COMMCONFIG_head), dwSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCommMask(hFile: Windows.Win32.Foundation.HANDLE, dwEvtMask: Windows.Win32.Devices.Communication.COMM_EVENT_MASK) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCommState(hFile: Windows.Win32.Foundation.HANDLE, lpDCB: POINTER(Windows.Win32.Devices.Communication.DCB_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCommTimeouts(hFile: Windows.Win32.Foundation.HANDLE, lpCommTimeouts: POINTER(Windows.Win32.Devices.Communication.COMMTIMEOUTS_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def TransmitCommChar(hFile: Windows.Win32.Foundation.HANDLE, cChar: Windows.Win32.Foundation.CHAR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WaitCommEvent(hFile: Windows.Win32.Foundation.HANDLE, lpEvtMask: POINTER(Windows.Win32.Devices.Communication.COMM_EVENT_MASK), lpOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-comm-l1-1-1.dll')
def OpenCommPort(uPortNumber: UInt32, dwDesiredAccess: UInt32, dwFlagsAndAttributes: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-comm-l1-1-2.dll')
def GetCommPorts(lpPortNumbers: POINTER(UInt32), uPortNumbersCount: UInt32, puPortNumbersFound: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def BuildCommDCBA(lpDef: Windows.Win32.Foundation.PSTR, lpDCB: POINTER(Windows.Win32.Devices.Communication.DCB_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BuildCommDCBW(lpDef: Windows.Win32.Foundation.PWSTR, lpDCB: POINTER(Windows.Win32.Devices.Communication.DCB_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BuildCommDCBAndTimeoutsA(lpDef: Windows.Win32.Foundation.PSTR, lpDCB: POINTER(Windows.Win32.Devices.Communication.DCB_head), lpCommTimeouts: POINTER(Windows.Win32.Devices.Communication.COMMTIMEOUTS_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BuildCommDCBAndTimeoutsW(lpDef: Windows.Win32.Foundation.PWSTR, lpDCB: POINTER(Windows.Win32.Devices.Communication.DCB_head), lpCommTimeouts: POINTER(Windows.Win32.Devices.Communication.COMMTIMEOUTS_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CommConfigDialogA(lpszName: Windows.Win32.Foundation.PSTR, hWnd: Windows.Win32.Foundation.HWND, lpCC: POINTER(Windows.Win32.Devices.Communication.COMMCONFIG_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CommConfigDialogW(lpszName: Windows.Win32.Foundation.PWSTR, hWnd: Windows.Win32.Foundation.HWND, lpCC: POINTER(Windows.Win32.Devices.Communication.COMMCONFIG_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDefaultCommConfigA(lpszName: Windows.Win32.Foundation.PSTR, lpCC: POINTER(Windows.Win32.Devices.Communication.COMMCONFIG_head), lpdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDefaultCommConfigW(lpszName: Windows.Win32.Foundation.PWSTR, lpCC: POINTER(Windows.Win32.Devices.Communication.COMMCONFIG_head), lpdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDefaultCommConfigA(lpszName: Windows.Win32.Foundation.PSTR, lpCC: POINTER(Windows.Win32.Devices.Communication.COMMCONFIG_head), dwSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDefaultCommConfigW(lpszName: Windows.Win32.Foundation.PWSTR, lpCC: POINTER(Windows.Win32.Devices.Communication.COMMCONFIG_head), dwSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
CLEAR_COMM_ERROR_FLAGS = UInt32
CE_BREAK: CLEAR_COMM_ERROR_FLAGS = 16
CE_FRAME: CLEAR_COMM_ERROR_FLAGS = 8
CE_OVERRUN: CLEAR_COMM_ERROR_FLAGS = 2
CE_RXOVER: CLEAR_COMM_ERROR_FLAGS = 1
CE_RXPARITY: CLEAR_COMM_ERROR_FLAGS = 4
class COMMCONFIG(Structure):
    dwSize: UInt32
    wVersion: UInt16
    wReserved: UInt16
    dcb: Windows.Win32.Devices.Communication.DCB
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
    wSettableStopParity: Windows.Win32.Devices.Communication.COMMPROP_STOP_PARITY
    dwCurrentTxQueue: UInt32
    dwCurrentRxQueue: UInt32
    dwProvSpec1: UInt32
    dwProvSpec2: UInt32
    wcProvChar: Char * 1
COMMPROP_STOP_PARITY = UInt16
STOPBITS_10: COMMPROP_STOP_PARITY = 1
STOPBITS_15: COMMPROP_STOP_PARITY = 2
STOPBITS_20: COMMPROP_STOP_PARITY = 4
PARITY_NONE: COMMPROP_STOP_PARITY = 256
PARITY_ODD: COMMPROP_STOP_PARITY = 512
PARITY_EVEN: COMMPROP_STOP_PARITY = 1024
PARITY_MARK: COMMPROP_STOP_PARITY = 2048
PARITY_SPACE: COMMPROP_STOP_PARITY = 4096
class COMMTIMEOUTS(Structure):
    ReadIntervalTimeout: UInt32
    ReadTotalTimeoutMultiplier: UInt32
    ReadTotalTimeoutConstant: UInt32
    WriteTotalTimeoutMultiplier: UInt32
    WriteTotalTimeoutConstant: UInt32
COMM_EVENT_MASK = UInt32
EV_BREAK: COMM_EVENT_MASK = 64
EV_CTS: COMM_EVENT_MASK = 8
EV_DSR: COMM_EVENT_MASK = 16
EV_ERR: COMM_EVENT_MASK = 128
EV_EVENT1: COMM_EVENT_MASK = 2048
EV_EVENT2: COMM_EVENT_MASK = 4096
EV_PERR: COMM_EVENT_MASK = 512
EV_RING: COMM_EVENT_MASK = 256
EV_RLSD: COMM_EVENT_MASK = 32
EV_RX80FULL: COMM_EVENT_MASK = 1024
EV_RXCHAR: COMM_EVENT_MASK = 1
EV_RXFLAG: COMM_EVENT_MASK = 2
EV_TXEMPTY: COMM_EVENT_MASK = 4
class COMSTAT(Structure):
    _bitfield: UInt32
    cbInQue: UInt32
    cbOutQue: UInt32
class DCB(Structure):
    DCBlength: UInt32
    BaudRate: UInt32
    _bitfield: UInt32
    wReserved: UInt16
    XonLim: UInt16
    XoffLim: UInt16
    ByteSize: Byte
    Parity: Windows.Win32.Devices.Communication.DCB_PARITY
    StopBits: Windows.Win32.Devices.Communication.DCB_STOP_BITS
    XonChar: Windows.Win32.Foundation.CHAR
    XoffChar: Windows.Win32.Foundation.CHAR
    ErrorChar: Windows.Win32.Foundation.CHAR
    EofChar: Windows.Win32.Foundation.CHAR
    EvtChar: Windows.Win32.Foundation.CHAR
    wReserved1: UInt16
DCB_PARITY = Byte
EVENPARITY: DCB_PARITY = 2
MARKPARITY: DCB_PARITY = 3
NOPARITY: DCB_PARITY = 0
ODDPARITY: DCB_PARITY = 1
SPACEPARITY: DCB_PARITY = 4
DCB_STOP_BITS = Byte
ONESTOPBIT: DCB_STOP_BITS = 0
ONE5STOPBITS: DCB_STOP_BITS = 1
TWOSTOPBITS: DCB_STOP_BITS = 2
ESCAPE_COMM_FUNCTION = UInt32
CLRBREAK: ESCAPE_COMM_FUNCTION = 9
CLRDTR: ESCAPE_COMM_FUNCTION = 6
CLRRTS: ESCAPE_COMM_FUNCTION = 4
SETBREAK: ESCAPE_COMM_FUNCTION = 8
SETDTR: ESCAPE_COMM_FUNCTION = 5
SETRTS: ESCAPE_COMM_FUNCTION = 3
SETXOFF: ESCAPE_COMM_FUNCTION = 1
SETXON: ESCAPE_COMM_FUNCTION = 2
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
    dwDialOptions: Windows.Win32.Devices.Communication.MODEMDEVCAPS_DIAL_OPTIONS
    dwCallSetupFailTimer: UInt32
    dwInactivityTimeout: UInt32
    dwSpeakerVolume: Windows.Win32.Devices.Communication.MODEMDEVCAPS_SPEAKER_VOLUME
    dwSpeakerMode: Windows.Win32.Devices.Communication.MODEMDEVCAPS_SPEAKER_MODE
    dwModemOptions: UInt32
    dwMaxDTERate: UInt32
    dwMaxDCERate: UInt32
    abVariablePortion: Byte * 1
MODEMDEVCAPS_DIAL_OPTIONS = UInt32
DIALOPTION_BILLING: MODEMDEVCAPS_DIAL_OPTIONS = 64
DIALOPTION_DIALTONE: MODEMDEVCAPS_DIAL_OPTIONS = 256
DIALOPTION_QUIET: MODEMDEVCAPS_DIAL_OPTIONS = 128
MODEMDEVCAPS_SPEAKER_MODE = UInt32
MDMSPKRFLAG_CALLSETUP: MODEMDEVCAPS_SPEAKER_MODE = 8
MDMSPKRFLAG_DIAL: MODEMDEVCAPS_SPEAKER_MODE = 2
MDMSPKRFLAG_OFF: MODEMDEVCAPS_SPEAKER_MODE = 1
MDMSPKRFLAG_ON: MODEMDEVCAPS_SPEAKER_MODE = 4
MODEMDEVCAPS_SPEAKER_VOLUME = UInt32
MDMVOLFLAG_HIGH: MODEMDEVCAPS_SPEAKER_VOLUME = 4
MDMVOLFLAG_LOW: MODEMDEVCAPS_SPEAKER_VOLUME = 1
MDMVOLFLAG_MEDIUM: MODEMDEVCAPS_SPEAKER_VOLUME = 2
class MODEMSETTINGS(Structure):
    dwActualSize: UInt32
    dwRequiredSize: UInt32
    dwDevSpecificOffset: UInt32
    dwDevSpecificSize: UInt32
    dwCallSetupFailTimer: UInt32
    dwInactivityTimeout: UInt32
    dwSpeakerVolume: Windows.Win32.Devices.Communication.MODEM_SPEAKER_VOLUME
    dwSpeakerMode: Windows.Win32.Devices.Communication.MODEMSETTINGS_SPEAKER_MODE
    dwPreferredModemOptions: UInt32
    dwNegotiatedModemOptions: UInt32
    dwNegotiatedDCERate: UInt32
    abVariablePortion: Byte * 1
MODEMSETTINGS_SPEAKER_MODE = UInt32
MDMSPKR_CALLSETUP: MODEMSETTINGS_SPEAKER_MODE = 8
MDMSPKR_DIAL: MODEMSETTINGS_SPEAKER_MODE = 2
MDMSPKR_OFF: MODEMSETTINGS_SPEAKER_MODE = 1
MDMSPKR_ON: MODEMSETTINGS_SPEAKER_MODE = 4
MODEM_SPEAKER_VOLUME = UInt32
MDMVOL_HIGH: MODEM_SPEAKER_VOLUME = 2
MDMVOL_LOW: MODEM_SPEAKER_VOLUME = 0
MDMVOL_MEDIUM: MODEM_SPEAKER_VOLUME = 1
MODEM_STATUS_FLAGS = UInt32
MS_CTS_ON: MODEM_STATUS_FLAGS = 16
MS_DSR_ON: MODEM_STATUS_FLAGS = 32
MS_RING_ON: MODEM_STATUS_FLAGS = 64
MS_RLSD_ON: MODEM_STATUS_FLAGS = 128
PURGE_COMM_FLAGS = UInt32
PURGE_RXABORT: PURGE_COMM_FLAGS = 2
PURGE_RXCLEAR: PURGE_COMM_FLAGS = 8
PURGE_TXABORT: PURGE_COMM_FLAGS = 1
PURGE_TXCLEAR: PURGE_COMM_FLAGS = 4
make_head(_module, 'COMMCONFIG')
make_head(_module, 'COMMPROP')
make_head(_module, 'COMMTIMEOUTS')
make_head(_module, 'COMSTAT')
make_head(_module, 'DCB')
make_head(_module, 'MODEMDEVCAPS')
make_head(_module, 'MODEMSETTINGS')
__all__ = [
    "BuildCommDCBA",
    "BuildCommDCBAndTimeoutsA",
    "BuildCommDCBAndTimeoutsW",
    "BuildCommDCBW",
    "CE_BREAK",
    "CE_FRAME",
    "CE_OVERRUN",
    "CE_RXOVER",
    "CE_RXPARITY",
    "CLEAR_COMM_ERROR_FLAGS",
    "CLRBREAK",
    "CLRDTR",
    "CLRRTS",
    "COMMCONFIG",
    "COMMPROP",
    "COMMPROP_STOP_PARITY",
    "COMMTIMEOUTS",
    "COMM_EVENT_MASK",
    "COMSTAT",
    "ClearCommBreak",
    "ClearCommError",
    "CommConfigDialogA",
    "CommConfigDialogW",
    "DCB",
    "DCB_PARITY",
    "DCB_STOP_BITS",
    "DIALOPTION_BILLING",
    "DIALOPTION_DIALTONE",
    "DIALOPTION_QUIET",
    "ESCAPE_COMM_FUNCTION",
    "EVENPARITY",
    "EV_BREAK",
    "EV_CTS",
    "EV_DSR",
    "EV_ERR",
    "EV_EVENT1",
    "EV_EVENT2",
    "EV_PERR",
    "EV_RING",
    "EV_RLSD",
    "EV_RX80FULL",
    "EV_RXCHAR",
    "EV_RXFLAG",
    "EV_TXEMPTY",
    "EscapeCommFunction",
    "GetCommConfig",
    "GetCommMask",
    "GetCommModemStatus",
    "GetCommPorts",
    "GetCommProperties",
    "GetCommState",
    "GetCommTimeouts",
    "GetDefaultCommConfigA",
    "GetDefaultCommConfigW",
    "MARKPARITY",
    "MAXLENGTH_NAI",
    "MAXLENGTH_UICCDATASTORE",
    "MDMSPKRFLAG_CALLSETUP",
    "MDMSPKRFLAG_DIAL",
    "MDMSPKRFLAG_OFF",
    "MDMSPKRFLAG_ON",
    "MDMSPKR_CALLSETUP",
    "MDMSPKR_DIAL",
    "MDMSPKR_OFF",
    "MDMSPKR_ON",
    "MDMVOLFLAG_HIGH",
    "MDMVOLFLAG_LOW",
    "MDMVOLFLAG_MEDIUM",
    "MDMVOL_HIGH",
    "MDMVOL_LOW",
    "MDMVOL_MEDIUM",
    "MDM_ANALOG_RLP_OFF",
    "MDM_ANALOG_RLP_ON",
    "MDM_ANALOG_V34",
    "MDM_AUTO_ML_2",
    "MDM_AUTO_ML_DEFAULT",
    "MDM_AUTO_ML_NONE",
    "MDM_AUTO_SPEED_DEFAULT",
    "MDM_BEARERMODE_ANALOG",
    "MDM_BEARERMODE_GSM",
    "MDM_BEARERMODE_ISDN",
    "MDM_BLIND_DIAL",
    "MDM_CCITT_OVERRIDE",
    "MDM_CELLULAR",
    "MDM_COMPRESSION",
    "MDM_DIAGNOSTICS",
    "MDM_ERROR_CONTROL",
    "MDM_FLOWCONTROL_HARD",
    "MDM_FLOWCONTROL_SOFT",
    "MDM_FORCED_EC",
    "MDM_HDLCPPP_AUTH_CHAP",
    "MDM_HDLCPPP_AUTH_DEFAULT",
    "MDM_HDLCPPP_AUTH_MSCHAP",
    "MDM_HDLCPPP_AUTH_NONE",
    "MDM_HDLCPPP_AUTH_PAP",
    "MDM_HDLCPPP_ML_2",
    "MDM_HDLCPPP_ML_DEFAULT",
    "MDM_HDLCPPP_ML_NONE",
    "MDM_HDLCPPP_SPEED_56K",
    "MDM_HDLCPPP_SPEED_64K",
    "MDM_HDLCPPP_SPEED_DEFAULT",
    "MDM_MASK_AUTO_SPEED",
    "MDM_MASK_BEARERMODE",
    "MDM_MASK_HDLCPPP_SPEED",
    "MDM_MASK_PROTOCOLDATA",
    "MDM_MASK_PROTOCOLID",
    "MDM_MASK_V110_SPEED",
    "MDM_MASK_V120_SPEED",
    "MDM_MASK_X75_DATA",
    "MDM_PIAFS_INCOMING",
    "MDM_PIAFS_OUTGOING",
    "MDM_PROTOCOLID_ANALOG",
    "MDM_PROTOCOLID_AUTO",
    "MDM_PROTOCOLID_DEFAULT",
    "MDM_PROTOCOLID_GPRS",
    "MDM_PROTOCOLID_HDLCPPP",
    "MDM_PROTOCOLID_PIAFS",
    "MDM_PROTOCOLID_V110",
    "MDM_PROTOCOLID_V120",
    "MDM_PROTOCOLID_V128",
    "MDM_PROTOCOLID_X75",
    "MDM_SHIFT_AUTO_ML",
    "MDM_SHIFT_AUTO_SPEED",
    "MDM_SHIFT_BEARERMODE",
    "MDM_SHIFT_EXTENDEDINFO",
    "MDM_SHIFT_HDLCPPP_AUTH",
    "MDM_SHIFT_HDLCPPP_ML",
    "MDM_SHIFT_HDLCPPP_SPEED",
    "MDM_SHIFT_PROTOCOLDATA",
    "MDM_SHIFT_PROTOCOLID",
    "MDM_SHIFT_PROTOCOLINFO",
    "MDM_SHIFT_V110_SPEED",
    "MDM_SHIFT_V120_ML",
    "MDM_SHIFT_V120_SPEED",
    "MDM_SHIFT_X75_DATA",
    "MDM_SPEED_ADJUST",
    "MDM_TONE_DIAL",
    "MDM_V110_SPEED_12DOT0K",
    "MDM_V110_SPEED_14DOT4K",
    "MDM_V110_SPEED_19DOT2K",
    "MDM_V110_SPEED_1DOT2K",
    "MDM_V110_SPEED_28DOT8K",
    "MDM_V110_SPEED_2DOT4K",
    "MDM_V110_SPEED_38DOT4K",
    "MDM_V110_SPEED_4DOT8K",
    "MDM_V110_SPEED_57DOT6K",
    "MDM_V110_SPEED_9DOT6K",
    "MDM_V110_SPEED_DEFAULT",
    "MDM_V120_ML_2",
    "MDM_V120_ML_DEFAULT",
    "MDM_V120_ML_NONE",
    "MDM_V120_SPEED_56K",
    "MDM_V120_SPEED_64K",
    "MDM_V120_SPEED_DEFAULT",
    "MDM_V23_OVERRIDE",
    "MDM_X75_DATA_128K",
    "MDM_X75_DATA_64K",
    "MDM_X75_DATA_BTX",
    "MDM_X75_DATA_DEFAULT",
    "MDM_X75_DATA_T_70",
    "MODEMDEVCAPS",
    "MODEMDEVCAPS_DIAL_OPTIONS",
    "MODEMDEVCAPS_SPEAKER_MODE",
    "MODEMDEVCAPS_SPEAKER_VOLUME",
    "MODEMSETTINGS",
    "MODEMSETTINGS_SPEAKER_MODE",
    "MODEM_SPEAKER_VOLUME",
    "MODEM_STATUS_FLAGS",
    "MS_CTS_ON",
    "MS_DSR_ON",
    "MS_RING_ON",
    "MS_RLSD_ON",
    "NOPARITY",
    "ODDPARITY",
    "ONE5STOPBITS",
    "ONESTOPBIT",
    "OpenCommPort",
    "PARITY_EVEN",
    "PARITY_MARK",
    "PARITY_NONE",
    "PARITY_ODD",
    "PARITY_SPACE",
    "PURGE_COMM_FLAGS",
    "PURGE_RXABORT",
    "PURGE_RXCLEAR",
    "PURGE_TXABORT",
    "PURGE_TXCLEAR",
    "PurgeComm",
    "SETBREAK",
    "SETDTR",
    "SETRTS",
    "SETXOFF",
    "SETXON",
    "SID_3GPP_SUPSVCMODEL",
    "SPACEPARITY",
    "STOPBITS_10",
    "STOPBITS_15",
    "STOPBITS_20",
    "SetCommBreak",
    "SetCommConfig",
    "SetCommMask",
    "SetCommState",
    "SetCommTimeouts",
    "SetDefaultCommConfigA",
    "SetDefaultCommConfigW",
    "SetupComm",
    "TWOSTOPBITS",
    "TransmitCommChar",
    "WaitCommEvent",
]
_arch_optional = [
]
