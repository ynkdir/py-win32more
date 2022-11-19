from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Devices.SerialCommunication
import win32more.Foundation

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
COMDB_MIN_PORTS_ARBITRATED = 256
COMDB_MAX_PORTS_ARBITRATED = 4096
CDB_REPORT_BITS = 0
CDB_REPORT_BYTES = 1
HCOMDB = IntPtr
def _define_ComDBOpen():
    try:
        return WINFUNCTYPE(Int32,POINTER(IntPtr), use_last_error=False)(("ComDBOpen", windll["MSPORTS"]), ((1, 'PHComDB'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ComDBClose():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.SerialCommunication.HCOMDB, use_last_error=False)(("ComDBClose", windll["MSPORTS"]), ((1, 'HComDB'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ComDBGetCurrentPortUsage():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.SerialCommunication.HCOMDB,c_char_p_no,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(("ComDBGetCurrentPortUsage", windll["MSPORTS"]), ((1, 'HComDB'),(1, 'Buffer'),(1, 'BufferSize'),(1, 'ReportType'),(1, 'MaxPortsReported'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ComDBClaimNextFreePort():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.SerialCommunication.HCOMDB,POINTER(UInt32), use_last_error=False)(("ComDBClaimNextFreePort", windll["MSPORTS"]), ((1, 'HComDB'),(1, 'ComNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ComDBClaimPort():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.SerialCommunication.HCOMDB,UInt32,win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("ComDBClaimPort", windll["MSPORTS"]), ((1, 'HComDB'),(1, 'ComNumber'),(1, 'ForceClaim'),(1, 'Forced'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ComDBReleasePort():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.SerialCommunication.HCOMDB,UInt32, use_last_error=False)(("ComDBReleasePort", windll["MSPORTS"]), ((1, 'HComDB'),(1, 'ComNumber'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ComDBResizeDatabase():
    try:
        return WINFUNCTYPE(Int32,win32more.Devices.SerialCommunication.HCOMDB,UInt32, use_last_error=False)(("ComDBResizeDatabase", windll["MSPORTS"]), ((1, 'HComDB'),(1, 'NewSize'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "COMDB_MIN_PORTS_ARBITRATED",
    "COMDB_MAX_PORTS_ARBITRATED",
    "CDB_REPORT_BITS",
    "CDB_REPORT_BYTES",
    "HCOMDB",
    "ComDBOpen",
    "ComDBClose",
    "ComDBGetCurrentPortUsage",
    "ComDBClaimNextFreePort",
    "ComDBClaimPort",
    "ComDBReleasePort",
    "ComDBResizeDatabase",
]
