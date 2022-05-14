from win32more import *
import win32more.Devices.SerialCommunication
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Devices.SerialCommunication, name, eval(f"_define_{name}()"))
    return getattr(win32more.Devices.SerialCommunication, name)
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
