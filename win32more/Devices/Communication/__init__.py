from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Devices.Communication
import win32more.Foundation
import win32more.System.IO

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
MDM_COMPRESSION = 1
MDM_ERROR_CONTROL = 2
MDM_FORCED_EC = 4
MDM_CELLULAR = 8
MDM_FLOWCONTROL_HARD = 16
MDM_FLOWCONTROL_SOFT = 32
MDM_CCITT_OVERRIDE = 64
MDM_SPEED_ADJUST = 128
MDM_TONE_DIAL = 256
MDM_BLIND_DIAL = 512
MDM_V23_OVERRIDE = 1024
MDM_DIAGNOSTICS = 2048
MDM_MASK_BEARERMODE = 61440
MDM_SHIFT_BEARERMODE = 12
MDM_MASK_PROTOCOLID = 983040
MDM_SHIFT_PROTOCOLID = 16
MDM_MASK_PROTOCOLDATA = 267386880
MDM_SHIFT_PROTOCOLDATA = 20
MDM_SHIFT_PROTOCOLINFO = 16
MDM_SHIFT_EXTENDEDINFO = 12
MDM_BEARERMODE_ANALOG = 0
MDM_BEARERMODE_ISDN = 1
MDM_BEARERMODE_GSM = 2
MDM_PROTOCOLID_DEFAULT = 0
MDM_PROTOCOLID_HDLCPPP = 1
MDM_PROTOCOLID_V128 = 2
MDM_PROTOCOLID_X75 = 3
MDM_PROTOCOLID_V110 = 4
MDM_PROTOCOLID_V120 = 5
MDM_PROTOCOLID_AUTO = 6
MDM_PROTOCOLID_ANALOG = 7
MDM_PROTOCOLID_GPRS = 8
MDM_PROTOCOLID_PIAFS = 9
MDM_SHIFT_HDLCPPP_SPEED = 0
MDM_MASK_HDLCPPP_SPEED = 7
MDM_HDLCPPP_SPEED_DEFAULT = 0
MDM_HDLCPPP_SPEED_64K = 1
MDM_HDLCPPP_SPEED_56K = 2
MDM_SHIFT_HDLCPPP_AUTH = 3
MDM_HDLCPPP_AUTH_DEFAULT = 0
MDM_HDLCPPP_AUTH_NONE = 1
MDM_HDLCPPP_AUTH_PAP = 2
MDM_HDLCPPP_AUTH_CHAP = 3
MDM_HDLCPPP_AUTH_MSCHAP = 4
MDM_SHIFT_HDLCPPP_ML = 6
MDM_HDLCPPP_ML_DEFAULT = 0
MDM_HDLCPPP_ML_NONE = 1
MDM_HDLCPPP_ML_2 = 2
MDM_SHIFT_V120_SPEED = 0
MDM_MASK_V120_SPEED = 7
MDM_V120_SPEED_DEFAULT = 0
MDM_V120_SPEED_64K = 1
MDM_V120_SPEED_56K = 2
MDM_SHIFT_V120_ML = 6
MDM_V120_ML_DEFAULT = 0
MDM_V120_ML_NONE = 1
MDM_V120_ML_2 = 2
MDM_SHIFT_X75_DATA = 0
MDM_MASK_X75_DATA = 7
MDM_X75_DATA_DEFAULT = 0
MDM_X75_DATA_64K = 1
MDM_X75_DATA_128K = 2
MDM_X75_DATA_T_70 = 3
MDM_X75_DATA_BTX = 4
MDM_SHIFT_V110_SPEED = 0
MDM_MASK_V110_SPEED = 15
MDM_V110_SPEED_DEFAULT = 0
MDM_V110_SPEED_1DOT2K = 1
MDM_V110_SPEED_2DOT4K = 2
MDM_V110_SPEED_4DOT8K = 3
MDM_V110_SPEED_9DOT6K = 4
MDM_V110_SPEED_12DOT0K = 5
MDM_V110_SPEED_14DOT4K = 6
MDM_V110_SPEED_19DOT2K = 7
MDM_V110_SPEED_28DOT8K = 8
MDM_V110_SPEED_38DOT4K = 9
MDM_V110_SPEED_57DOT6K = 10
MDM_SHIFT_AUTO_SPEED = 0
MDM_MASK_AUTO_SPEED = 7
MDM_AUTO_SPEED_DEFAULT = 0
MDM_SHIFT_AUTO_ML = 6
MDM_AUTO_ML_DEFAULT = 0
MDM_AUTO_ML_NONE = 1
MDM_AUTO_ML_2 = 2
MDM_ANALOG_RLP_ON = 0
MDM_ANALOG_RLP_OFF = 1
MDM_ANALOG_V34 = 2
MDM_PIAFS_INCOMING = 0
MDM_PIAFS_OUTGOING = 1
SID_3GPP_SUPSVCMODEL = 'd7d08e07-d767-4478-b14a-eecc87ea12f7'
MAXLENGTH_NAI = 72
MAXLENGTH_UICCDATASTORE = 10
MODEM_STATUS_FLAGS = UInt32
MS_CTS_ON = 16
MS_DSR_ON = 32
MS_RING_ON = 64
MS_RLSD_ON = 128
CLEAR_COMM_ERROR_FLAGS = UInt32
CE_BREAK = 16
CE_FRAME = 8
CE_OVERRUN = 2
CE_RXOVER = 1
CE_RXPARITY = 4
PURGE_COMM_FLAGS = UInt32
PURGE_RXABORT = 2
PURGE_RXCLEAR = 8
PURGE_TXABORT = 1
PURGE_TXCLEAR = 4
COMM_EVENT_MASK = UInt32
EV_BREAK = 64
EV_CTS = 8
EV_DSR = 16
EV_ERR = 128
EV_EVENT1 = 2048
EV_EVENT2 = 4096
EV_PERR = 512
EV_RING = 256
EV_RLSD = 32
EV_RX80FULL = 1024
EV_RXCHAR = 1
EV_RXFLAG = 2
EV_TXEMPTY = 4
ESCAPE_COMM_FUNCTION = UInt32
CLRBREAK = 9
CLRDTR = 6
CLRRTS = 4
SETBREAK = 8
SETDTR = 5
SETRTS = 3
SETXOFF = 1
SETXON = 2
MODEMDEVCAPS_DIAL_OPTIONS = UInt32
DIALOPTION_BILLING = 64
DIALOPTION_DIALTONE = 256
DIALOPTION_QUIET = 128
MODEMSETTINGS_SPEAKER_MODE = UInt32
MDMSPKR_CALLSETUP = 8
MDMSPKR_DIAL = 2
MDMSPKR_OFF = 1
MDMSPKR_ON = 4
COMMPROP_STOP_PARITY = UInt16
STOPBITS_10 = 1
STOPBITS_15 = 2
STOPBITS_20 = 4
PARITY_NONE = 256
PARITY_ODD = 512
PARITY_EVEN = 1024
PARITY_MARK = 2048
PARITY_SPACE = 4096
MODEM_SPEAKER_VOLUME = UInt32
MDMVOL_HIGH = 2
MDMVOL_LOW = 0
MDMVOL_MEDIUM = 1
MODEMDEVCAPS_SPEAKER_VOLUME = UInt32
MDMVOLFLAG_HIGH = 4
MDMVOLFLAG_LOW = 1
MDMVOLFLAG_MEDIUM = 2
MODEMDEVCAPS_SPEAKER_MODE = UInt32
MDMSPKRFLAG_CALLSETUP = 8
MDMSPKRFLAG_DIAL = 2
MDMSPKRFLAG_OFF = 1
MDMSPKRFLAG_ON = 4
def _define_MODEMDEVCAPS_head():
    class MODEMDEVCAPS(Structure):
        pass
    return MODEMDEVCAPS
def _define_MODEMDEVCAPS():
    MODEMDEVCAPS = win32more.Devices.Communication.MODEMDEVCAPS_head
    MODEMDEVCAPS._fields_ = [
        ("dwActualSize", UInt32),
        ("dwRequiredSize", UInt32),
        ("dwDevSpecificOffset", UInt32),
        ("dwDevSpecificSize", UInt32),
        ("dwModemProviderVersion", UInt32),
        ("dwModemManufacturerOffset", UInt32),
        ("dwModemManufacturerSize", UInt32),
        ("dwModemModelOffset", UInt32),
        ("dwModemModelSize", UInt32),
        ("dwModemVersionOffset", UInt32),
        ("dwModemVersionSize", UInt32),
        ("dwDialOptions", win32more.Devices.Communication.MODEMDEVCAPS_DIAL_OPTIONS),
        ("dwCallSetupFailTimer", UInt32),
        ("dwInactivityTimeout", UInt32),
        ("dwSpeakerVolume", win32more.Devices.Communication.MODEMDEVCAPS_SPEAKER_VOLUME),
        ("dwSpeakerMode", win32more.Devices.Communication.MODEMDEVCAPS_SPEAKER_MODE),
        ("dwModemOptions", UInt32),
        ("dwMaxDTERate", UInt32),
        ("dwMaxDCERate", UInt32),
        ("abVariablePortion", Byte * 0),
    ]
    return MODEMDEVCAPS
def _define_MODEMSETTINGS_head():
    class MODEMSETTINGS(Structure):
        pass
    return MODEMSETTINGS
def _define_MODEMSETTINGS():
    MODEMSETTINGS = win32more.Devices.Communication.MODEMSETTINGS_head
    MODEMSETTINGS._fields_ = [
        ("dwActualSize", UInt32),
        ("dwRequiredSize", UInt32),
        ("dwDevSpecificOffset", UInt32),
        ("dwDevSpecificSize", UInt32),
        ("dwCallSetupFailTimer", UInt32),
        ("dwInactivityTimeout", UInt32),
        ("dwSpeakerVolume", win32more.Devices.Communication.MODEM_SPEAKER_VOLUME),
        ("dwSpeakerMode", win32more.Devices.Communication.MODEMSETTINGS_SPEAKER_MODE),
        ("dwPreferredModemOptions", UInt32),
        ("dwNegotiatedModemOptions", UInt32),
        ("dwNegotiatedDCERate", UInt32),
        ("abVariablePortion", Byte * 0),
    ]
    return MODEMSETTINGS
def _define_COMMPROP_head():
    class COMMPROP(Structure):
        pass
    return COMMPROP
def _define_COMMPROP():
    COMMPROP = win32more.Devices.Communication.COMMPROP_head
    COMMPROP._fields_ = [
        ("wPacketLength", UInt16),
        ("wPacketVersion", UInt16),
        ("dwServiceMask", UInt32),
        ("dwReserved1", UInt32),
        ("dwMaxTxQueue", UInt32),
        ("dwMaxRxQueue", UInt32),
        ("dwMaxBaud", UInt32),
        ("dwProvSubType", UInt32),
        ("dwProvCapabilities", UInt32),
        ("dwSettableParams", UInt32),
        ("dwSettableBaud", UInt32),
        ("wSettableData", UInt16),
        ("wSettableStopParity", win32more.Devices.Communication.COMMPROP_STOP_PARITY),
        ("dwCurrentTxQueue", UInt32),
        ("dwCurrentRxQueue", UInt32),
        ("dwProvSpec1", UInt32),
        ("dwProvSpec2", UInt32),
        ("wcProvChar", Char * 0),
    ]
    return COMMPROP
def _define_COMSTAT_head():
    class COMSTAT(Structure):
        pass
    return COMSTAT
def _define_COMSTAT():
    COMSTAT = win32more.Devices.Communication.COMSTAT_head
    COMSTAT._fields_ = [
        ("_bitfield", UInt32),
        ("cbInQue", UInt32),
        ("cbOutQue", UInt32),
    ]
    return COMSTAT
def _define_DCB_head():
    class DCB(Structure):
        pass
    return DCB
def _define_DCB():
    DCB = win32more.Devices.Communication.DCB_head
    DCB._fields_ = [
        ("DCBlength", UInt32),
        ("BaudRate", UInt32),
        ("_bitfield", UInt32),
        ("wReserved", UInt16),
        ("XonLim", UInt16),
        ("XoffLim", UInt16),
        ("ByteSize", Byte),
        ("Parity", Byte),
        ("StopBits", Byte),
        ("XonChar", win32more.Foundation.CHAR),
        ("XoffChar", win32more.Foundation.CHAR),
        ("ErrorChar", win32more.Foundation.CHAR),
        ("EofChar", win32more.Foundation.CHAR),
        ("EvtChar", win32more.Foundation.CHAR),
        ("wReserved1", UInt16),
    ]
    return DCB
def _define_COMMTIMEOUTS_head():
    class COMMTIMEOUTS(Structure):
        pass
    return COMMTIMEOUTS
def _define_COMMTIMEOUTS():
    COMMTIMEOUTS = win32more.Devices.Communication.COMMTIMEOUTS_head
    COMMTIMEOUTS._fields_ = [
        ("ReadIntervalTimeout", UInt32),
        ("ReadTotalTimeoutMultiplier", UInt32),
        ("ReadTotalTimeoutConstant", UInt32),
        ("WriteTotalTimeoutMultiplier", UInt32),
        ("WriteTotalTimeoutConstant", UInt32),
    ]
    return COMMTIMEOUTS
def _define_COMMCONFIG_head():
    class COMMCONFIG(Structure):
        pass
    return COMMCONFIG
def _define_COMMCONFIG():
    COMMCONFIG = win32more.Devices.Communication.COMMCONFIG_head
    COMMCONFIG._fields_ = [
        ("dwSize", UInt32),
        ("wVersion", UInt16),
        ("wReserved", UInt16),
        ("dcb", win32more.Devices.Communication.DCB),
        ("dwProviderSubType", UInt32),
        ("dwProviderOffset", UInt32),
        ("dwProviderSize", UInt32),
        ("wcProviderData", Char * 0),
    ]
    return COMMCONFIG
def _define_ClearCommBreak():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=True)(("ClearCommBreak", windll["KERNEL32"]), ((1, 'hFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ClearCommError():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Communication.CLEAR_COMM_ERROR_FLAGS),POINTER(win32more.Devices.Communication.COMSTAT_head), use_last_error=True)(("ClearCommError", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpErrors'),(1, 'lpStat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetupComm():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32, use_last_error=True)(("SetupComm", windll["KERNEL32"]), ((1, 'hFile'),(1, 'dwInQueue'),(1, 'dwOutQueue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EscapeCommFunction():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Devices.Communication.ESCAPE_COMM_FUNCTION, use_last_error=True)(("EscapeCommFunction", windll["KERNEL32"]), ((1, 'hFile'),(1, 'dwFunc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCommConfig():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Communication.COMMCONFIG_head),POINTER(UInt32), use_last_error=True)(("GetCommConfig", windll["KERNEL32"]), ((1, 'hCommDev'),(1, 'lpCC'),(1, 'lpdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCommMask():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Communication.COMM_EVENT_MASK), use_last_error=True)(("GetCommMask", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpEvtMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCommProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Communication.COMMPROP_head), use_last_error=True)(("GetCommProperties", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpCommProp'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCommModemStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Communication.MODEM_STATUS_FLAGS), use_last_error=True)(("GetCommModemStatus", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpModemStat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCommState():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Communication.DCB_head), use_last_error=True)(("GetCommState", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpDCB'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCommTimeouts():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Communication.COMMTIMEOUTS_head), use_last_error=True)(("GetCommTimeouts", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpCommTimeouts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PurgeComm():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Devices.Communication.PURGE_COMM_FLAGS, use_last_error=True)(("PurgeComm", windll["KERNEL32"]), ((1, 'hFile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCommBreak():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=True)(("SetCommBreak", windll["KERNEL32"]), ((1, 'hFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCommConfig():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Communication.COMMCONFIG_head),UInt32, use_last_error=True)(("SetCommConfig", windll["KERNEL32"]), ((1, 'hCommDev'),(1, 'lpCC'),(1, 'dwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCommMask():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Devices.Communication.COMM_EVENT_MASK, use_last_error=True)(("SetCommMask", windll["KERNEL32"]), ((1, 'hFile'),(1, 'dwEvtMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCommState():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Communication.DCB_head), use_last_error=True)(("SetCommState", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpDCB'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCommTimeouts():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Communication.COMMTIMEOUTS_head), use_last_error=True)(("SetCommTimeouts", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpCommTimeouts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TransmitCommChar():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.CHAR, use_last_error=True)(("TransmitCommChar", windll["KERNEL32"]), ((1, 'hFile'),(1, 'cChar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WaitCommEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Communication.COMM_EVENT_MASK),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=True)(("WaitCommEvent", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpEvtMask'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenCommPort():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,UInt32,UInt32, use_last_error=False)(("OpenCommPort", windll["api-ms-win-core-comm-l1-1-1"]), ((1, 'uPortNumber'),(1, 'dwDesiredAccess'),(1, 'dwFlagsAndAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCommPorts():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(UInt32), use_last_error=False)(("GetCommPorts", windll["api-ms-win-core-comm-l1-1-2"]), ((1, 'lpPortNumbers'),(1, 'uPortNumbersCount'),(1, 'puPortNumbersFound'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildCommDCBA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Devices.Communication.DCB_head), use_last_error=True)(("BuildCommDCBA", windll["KERNEL32"]), ((1, 'lpDef'),(1, 'lpDCB'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildCommDCBW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Communication.DCB_head), use_last_error=True)(("BuildCommDCBW", windll["KERNEL32"]), ((1, 'lpDef'),(1, 'lpDCB'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildCommDCB():
    return win32more.Devices.Communication.BuildCommDCBW
def _define_BuildCommDCBAndTimeoutsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Devices.Communication.DCB_head),POINTER(win32more.Devices.Communication.COMMTIMEOUTS_head), use_last_error=True)(("BuildCommDCBAndTimeoutsA", windll["KERNEL32"]), ((1, 'lpDef'),(1, 'lpDCB'),(1, 'lpCommTimeouts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildCommDCBAndTimeoutsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Communication.DCB_head),POINTER(win32more.Devices.Communication.COMMTIMEOUTS_head), use_last_error=True)(("BuildCommDCBAndTimeoutsW", windll["KERNEL32"]), ((1, 'lpDef'),(1, 'lpDCB'),(1, 'lpCommTimeouts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildCommDCBAndTimeouts():
    return win32more.Devices.Communication.BuildCommDCBAndTimeoutsW
def _define_CommConfigDialogA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.HWND,POINTER(win32more.Devices.Communication.COMMCONFIG_head), use_last_error=True)(("CommConfigDialogA", windll["KERNEL32"]), ((1, 'lpszName'),(1, 'hWnd'),(1, 'lpCC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CommConfigDialogW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.HWND,POINTER(win32more.Devices.Communication.COMMCONFIG_head), use_last_error=True)(("CommConfigDialogW", windll["KERNEL32"]), ((1, 'lpszName'),(1, 'hWnd'),(1, 'lpCC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CommConfigDialog():
    return win32more.Devices.Communication.CommConfigDialogW
def _define_GetDefaultCommConfigA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Devices.Communication.COMMCONFIG_head),POINTER(UInt32), use_last_error=True)(("GetDefaultCommConfigA", windll["KERNEL32"]), ((1, 'lpszName'),(1, 'lpCC'),(1, 'lpdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDefaultCommConfigW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Communication.COMMCONFIG_head),POINTER(UInt32), use_last_error=True)(("GetDefaultCommConfigW", windll["KERNEL32"]), ((1, 'lpszName'),(1, 'lpCC'),(1, 'lpdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDefaultCommConfig():
    return win32more.Devices.Communication.GetDefaultCommConfigW
def _define_SetDefaultCommConfigA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Devices.Communication.COMMCONFIG_head),UInt32, use_last_error=True)(("SetDefaultCommConfigA", windll["KERNEL32"]), ((1, 'lpszName'),(1, 'lpCC'),(1, 'dwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDefaultCommConfigW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Devices.Communication.COMMCONFIG_head),UInt32, use_last_error=True)(("SetDefaultCommConfigW", windll["KERNEL32"]), ((1, 'lpszName'),(1, 'lpCC'),(1, 'dwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDefaultCommConfig():
    return win32more.Devices.Communication.SetDefaultCommConfigW
__all__ = [
    "MDM_COMPRESSION",
    "MDM_ERROR_CONTROL",
    "MDM_FORCED_EC",
    "MDM_CELLULAR",
    "MDM_FLOWCONTROL_HARD",
    "MDM_FLOWCONTROL_SOFT",
    "MDM_CCITT_OVERRIDE",
    "MDM_SPEED_ADJUST",
    "MDM_TONE_DIAL",
    "MDM_BLIND_DIAL",
    "MDM_V23_OVERRIDE",
    "MDM_DIAGNOSTICS",
    "MDM_MASK_BEARERMODE",
    "MDM_SHIFT_BEARERMODE",
    "MDM_MASK_PROTOCOLID",
    "MDM_SHIFT_PROTOCOLID",
    "MDM_MASK_PROTOCOLDATA",
    "MDM_SHIFT_PROTOCOLDATA",
    "MDM_SHIFT_PROTOCOLINFO",
    "MDM_SHIFT_EXTENDEDINFO",
    "MDM_BEARERMODE_ANALOG",
    "MDM_BEARERMODE_ISDN",
    "MDM_BEARERMODE_GSM",
    "MDM_PROTOCOLID_DEFAULT",
    "MDM_PROTOCOLID_HDLCPPP",
    "MDM_PROTOCOLID_V128",
    "MDM_PROTOCOLID_X75",
    "MDM_PROTOCOLID_V110",
    "MDM_PROTOCOLID_V120",
    "MDM_PROTOCOLID_AUTO",
    "MDM_PROTOCOLID_ANALOG",
    "MDM_PROTOCOLID_GPRS",
    "MDM_PROTOCOLID_PIAFS",
    "MDM_SHIFT_HDLCPPP_SPEED",
    "MDM_MASK_HDLCPPP_SPEED",
    "MDM_HDLCPPP_SPEED_DEFAULT",
    "MDM_HDLCPPP_SPEED_64K",
    "MDM_HDLCPPP_SPEED_56K",
    "MDM_SHIFT_HDLCPPP_AUTH",
    "MDM_HDLCPPP_AUTH_DEFAULT",
    "MDM_HDLCPPP_AUTH_NONE",
    "MDM_HDLCPPP_AUTH_PAP",
    "MDM_HDLCPPP_AUTH_CHAP",
    "MDM_HDLCPPP_AUTH_MSCHAP",
    "MDM_SHIFT_HDLCPPP_ML",
    "MDM_HDLCPPP_ML_DEFAULT",
    "MDM_HDLCPPP_ML_NONE",
    "MDM_HDLCPPP_ML_2",
    "MDM_SHIFT_V120_SPEED",
    "MDM_MASK_V120_SPEED",
    "MDM_V120_SPEED_DEFAULT",
    "MDM_V120_SPEED_64K",
    "MDM_V120_SPEED_56K",
    "MDM_SHIFT_V120_ML",
    "MDM_V120_ML_DEFAULT",
    "MDM_V120_ML_NONE",
    "MDM_V120_ML_2",
    "MDM_SHIFT_X75_DATA",
    "MDM_MASK_X75_DATA",
    "MDM_X75_DATA_DEFAULT",
    "MDM_X75_DATA_64K",
    "MDM_X75_DATA_128K",
    "MDM_X75_DATA_T_70",
    "MDM_X75_DATA_BTX",
    "MDM_SHIFT_V110_SPEED",
    "MDM_MASK_V110_SPEED",
    "MDM_V110_SPEED_DEFAULT",
    "MDM_V110_SPEED_1DOT2K",
    "MDM_V110_SPEED_2DOT4K",
    "MDM_V110_SPEED_4DOT8K",
    "MDM_V110_SPEED_9DOT6K",
    "MDM_V110_SPEED_12DOT0K",
    "MDM_V110_SPEED_14DOT4K",
    "MDM_V110_SPEED_19DOT2K",
    "MDM_V110_SPEED_28DOT8K",
    "MDM_V110_SPEED_38DOT4K",
    "MDM_V110_SPEED_57DOT6K",
    "MDM_SHIFT_AUTO_SPEED",
    "MDM_MASK_AUTO_SPEED",
    "MDM_AUTO_SPEED_DEFAULT",
    "MDM_SHIFT_AUTO_ML",
    "MDM_AUTO_ML_DEFAULT",
    "MDM_AUTO_ML_NONE",
    "MDM_AUTO_ML_2",
    "MDM_ANALOG_RLP_ON",
    "MDM_ANALOG_RLP_OFF",
    "MDM_ANALOG_V34",
    "MDM_PIAFS_INCOMING",
    "MDM_PIAFS_OUTGOING",
    "SID_3GPP_SUPSVCMODEL",
    "MAXLENGTH_NAI",
    "MAXLENGTH_UICCDATASTORE",
    "MODEM_STATUS_FLAGS",
    "MS_CTS_ON",
    "MS_DSR_ON",
    "MS_RING_ON",
    "MS_RLSD_ON",
    "CLEAR_COMM_ERROR_FLAGS",
    "CE_BREAK",
    "CE_FRAME",
    "CE_OVERRUN",
    "CE_RXOVER",
    "CE_RXPARITY",
    "PURGE_COMM_FLAGS",
    "PURGE_RXABORT",
    "PURGE_RXCLEAR",
    "PURGE_TXABORT",
    "PURGE_TXCLEAR",
    "COMM_EVENT_MASK",
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
    "ESCAPE_COMM_FUNCTION",
    "CLRBREAK",
    "CLRDTR",
    "CLRRTS",
    "SETBREAK",
    "SETDTR",
    "SETRTS",
    "SETXOFF",
    "SETXON",
    "MODEMDEVCAPS_DIAL_OPTIONS",
    "DIALOPTION_BILLING",
    "DIALOPTION_DIALTONE",
    "DIALOPTION_QUIET",
    "MODEMSETTINGS_SPEAKER_MODE",
    "MDMSPKR_CALLSETUP",
    "MDMSPKR_DIAL",
    "MDMSPKR_OFF",
    "MDMSPKR_ON",
    "COMMPROP_STOP_PARITY",
    "STOPBITS_10",
    "STOPBITS_15",
    "STOPBITS_20",
    "PARITY_NONE",
    "PARITY_ODD",
    "PARITY_EVEN",
    "PARITY_MARK",
    "PARITY_SPACE",
    "MODEM_SPEAKER_VOLUME",
    "MDMVOL_HIGH",
    "MDMVOL_LOW",
    "MDMVOL_MEDIUM",
    "MODEMDEVCAPS_SPEAKER_VOLUME",
    "MDMVOLFLAG_HIGH",
    "MDMVOLFLAG_LOW",
    "MDMVOLFLAG_MEDIUM",
    "MODEMDEVCAPS_SPEAKER_MODE",
    "MDMSPKRFLAG_CALLSETUP",
    "MDMSPKRFLAG_DIAL",
    "MDMSPKRFLAG_OFF",
    "MDMSPKRFLAG_ON",
    "MODEMDEVCAPS",
    "MODEMSETTINGS",
    "COMMPROP",
    "COMSTAT",
    "DCB",
    "COMMTIMEOUTS",
    "COMMCONFIG",
    "ClearCommBreak",
    "ClearCommError",
    "SetupComm",
    "EscapeCommFunction",
    "GetCommConfig",
    "GetCommMask",
    "GetCommProperties",
    "GetCommModemStatus",
    "GetCommState",
    "GetCommTimeouts",
    "PurgeComm",
    "SetCommBreak",
    "SetCommConfig",
    "SetCommMask",
    "SetCommState",
    "SetCommTimeouts",
    "TransmitCommChar",
    "WaitCommEvent",
    "OpenCommPort",
    "GetCommPorts",
    "BuildCommDCBA",
    "BuildCommDCBW",
    "BuildCommDCB",
    "BuildCommDCBAndTimeoutsA",
    "BuildCommDCBAndTimeoutsW",
    "BuildCommDCBAndTimeouts",
    "CommConfigDialogA",
    "CommConfigDialogW",
    "CommConfigDialog",
    "GetDefaultCommConfigA",
    "GetDefaultCommConfigW",
    "GetDefaultCommConfig",
    "SetDefaultCommConfigA",
    "SetDefaultCommConfigW",
    "SetDefaultCommConfig",
]
