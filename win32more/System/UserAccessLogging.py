from win32more import *
import win32more.Foundation
import win32more.Networking.WinSock
import win32more.System.UserAccessLogging

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
def _define_UAL_DATA_BLOB_head():
    class UAL_DATA_BLOB(Structure):
        pass
    return UAL_DATA_BLOB
def _define_UAL_DATA_BLOB():
    UAL_DATA_BLOB = win32more.System.UserAccessLogging.UAL_DATA_BLOB_head
    UAL_DATA_BLOB._fields_ = [
        ("Size", UInt32),
        ("RoleGuid", Guid),
        ("TenantId", Guid),
        ("Address", win32more.Networking.WinSock.SOCKADDR_STORAGE),
        ("UserName", Char * 260),
    ]
    return UAL_DATA_BLOB
def _define_UalStart():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UserAccessLogging.UAL_DATA_BLOB_head), use_last_error=False)(("UalStart", windll["ualapi"]), ((1, 'Data'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UalStop():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UserAccessLogging.UAL_DATA_BLOB_head), use_last_error=False)(("UalStop", windll["ualapi"]), ((1, 'Data'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UalInstrument():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.UserAccessLogging.UAL_DATA_BLOB_head), use_last_error=False)(("UalInstrument", windll["ualapi"]), ((1, 'Data'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UalRegisterProduct():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("UalRegisterProduct", windll["ualapi"]), ((1, 'wszProductName'),(1, 'wszRoleName'),(1, 'wszGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "UAL_DATA_BLOB",
    "UalStart",
    "UalStop",
    "UalInstrument",
    "UalRegisterProduct",
]
