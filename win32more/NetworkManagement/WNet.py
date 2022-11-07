from win32more.base import *
import win32more.Foundation
import win32more.NetworkManagement.WNet

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
WNGETCON_CONNECTED = 0
WNGETCON_DISCONNECTED = 1
WNNC_SPEC_VERSION = 1
WNNC_SPEC_VERSION51 = 327681
WNNC_NET_TYPE = 2
WNNC_NET_NONE = 0
WNNC_DRIVER_VERSION = 3
WNNC_USER = 4
WNNC_USR_GETUSER = 1
WNNC_CONNECTION = 6
WNNC_CON_ADDCONNECTION = 1
WNNC_CON_CANCELCONNECTION = 2
WNNC_CON_GETCONNECTIONS = 4
WNNC_CON_ADDCONNECTION3 = 8
WNNC_CON_ADDCONNECTION4 = 16
WNNC_CON_CANCELCONNECTION2 = 32
WNNC_CON_GETPERFORMANCE = 64
WNNC_CON_DEFER = 128
WNNC_DIALOG = 8
WNNC_DLG_DEVICEMODE = 1
WNNC_DLG_PROPERTYDIALOG = 32
WNNC_DLG_SEARCHDIALOG = 64
WNNC_DLG_FORMATNETWORKNAME = 128
WNNC_DLG_PERMISSIONEDITOR = 256
WNNC_DLG_GETRESOURCEPARENT = 512
WNNC_DLG_GETRESOURCEINFORMATION = 2048
WNNC_ADMIN = 9
WNNC_ADM_GETDIRECTORYTYPE = 1
WNNC_ADM_DIRECTORYNOTIFY = 2
WNNC_ENUMERATION = 11
WNNC_ENUM_GLOBAL = 1
WNNC_ENUM_LOCAL = 2
WNNC_ENUM_CONTEXT = 4
WNNC_ENUM_SHAREABLE = 8
WNNC_START = 12
WNNC_WAIT_FOR_START = 1
WNNC_CONNECTION_FLAGS = 13
WNTYPE_DRIVE = 1
WNTYPE_FILE = 2
WNTYPE_PRINTER = 3
WNTYPE_COMM = 4
WNSRCH_REFRESH_FIRST_LEVEL = 1
WNDT_NORMAL = 0
WNDT_NETWORK = 1
WN_NETWORK_CLASS = 1
WN_CREDENTIAL_CLASS = 2
WN_PRIMARY_AUTHENT_CLASS = 4
WN_SERVICE_CLASS = 8
WN_VALID_LOGON_ACCOUNT = 1
WN_NT_PASSWORD_CHANGED = 2
NOTIFY_PRE = 1
NOTIFY_POST = 2
WNPERMC_PERM = 1
WNPERMC_AUDIT = 2
WNPERMC_OWNER = 4
RESOURCE_RECENT = 4
RESOURCETYPE_RESERVED = 8
RESOURCETYPE_UNKNOWN = 4294967295
RESOURCEUSAGE_NOLOCALDEVICE = 4
RESOURCEUSAGE_SIBLING = 8
RESOURCEUSAGE_RESERVED = 2147483648
RESOURCEDISPLAYTYPE_NETWORK = 6
RESOURCEDISPLAYTYPE_ROOT = 7
RESOURCEDISPLAYTYPE_SHAREADMIN = 8
RESOURCEDISPLAYTYPE_DIRECTORY = 9
RESOURCEDISPLAYTYPE_NDSCONTAINER = 11
NETPROPERTY_PERSISTENT = 1
CONNECT_NEED_DRIVE = 32
CONNECT_REFCOUNT = 64
CONNECT_LOCALDRIVE = 256
CONNECT_CURRENT_MEDIA = 512
CONNECT_RESERVED = 4278190080
CONNECT_CRED_RESET = 8192
CONNECT_REQUIRE_INTEGRITY = 16384
CONNECT_REQUIRE_PRIVACY = 32768
CONNECT_WRITE_THROUGH_SEMANTICS = 65536
CONNECT_GLOBAL_MAPPING = 262144
WNFMT_INENUM = 16
WNFMT_CONNECTION = 32
WNCON_FORNETCARD = 1
WNCON_NOTROUTED = 2
WNCON_SLOWLINK = 4
WNCON_DYNAMIC = 8
UNC_INFO_LEVEL = UInt32
UNIVERSAL_NAME_INFO_LEVEL = 1
REMOTE_NAME_INFO_LEVEL = 2
WNPERM_DLG = UInt32
WNPERM_DLG_PERM = 0
WNPERM_DLG_AUDIT = 1
WNPERM_DLG_OWNER = 2
WNET_OPEN_ENUM_USAGE = UInt32
RESOURCEUSAGE_NONE = 0
RESOURCEUSAGE_CONNECTABLE = 1
RESOURCEUSAGE_CONTAINER = 2
RESOURCEUSAGE_ATTACHED = 16
RESOURCEUSAGE_ALL = 19
NET_USE_CONNECT_FLAGS = UInt32
CONNECT_INTERACTIVE = 8
CONNECT_PROMPT = 16
CONNECT_REDIRECT = 128
CONNECT_UPDATE_PROFILE = 1
CONNECT_COMMANDLINE = 2048
CONNECT_CMD_SAVECRED = 4096
CONNECT_TEMPORARY = 4
CONNECT_DEFERRED = 1024
CONNECT_UPDATE_RECENT = 2
NP_PROPERTY_DIALOG_SELECTION = UInt32
WNPS_FILE = 0
WNPS_DIR = 1
WNPS_MULT = 2
NPDIRECTORY_NOTIFY_OPERATION = UInt32
WNDN_MKDIR = 1
WNDN_RMDIR = 2
WNDN_MVDIR = 3
NET_RESOURCE_TYPE = UInt32
RESOURCETYPE_ANY = 0
RESOURCETYPE_DISK = 1
RESOURCETYPE_PRINT = 2
NETWORK_NAME_FORMAT_FLAGS = UInt32
WNFMT_MULTILINE = 1
WNFMT_ABBREVIATED = 2
NET_RESOURCE_SCOPE = UInt32
RESOURCE_CONNECTED = 1
RESOURCE_CONTEXT = 5
RESOURCE_GLOBALNET = 2
RESOURCE_REMEMBERED = 3
NETINFOSTRUCT_CHARACTERISTICS = UInt32
NETINFO_DLL16 = 1
NETINFO_DISKRED = 4
NETINFO_PRINTERRED = 8
CONNECTDLGSTRUCT_FLAGS = UInt32
CONNDLG_RO_PATH = 1
CONNDLG_CONN_POINT = 2
CONNDLG_USE_MRU = 4
CONNDLG_HIDE_BOX = 8
CONNDLG_PERSIST = 16
CONNDLG_NOT_PERSIST = 32
DISCDLGSTRUCT_FLAGS = UInt32
DISC_UPDATE_PROFILE = 1
DISC_NO_FORCE = 64
NetEnumHandle = IntPtr
def _define_NETRESOURCEA_head():
    class NETRESOURCEA(Structure):
        pass
    return NETRESOURCEA
def _define_NETRESOURCEA():
    NETRESOURCEA = win32more.NetworkManagement.WNet.NETRESOURCEA_head
    NETRESOURCEA._fields_ = [
        ("dwScope", win32more.NetworkManagement.WNet.NET_RESOURCE_SCOPE),
        ("dwType", win32more.NetworkManagement.WNet.NET_RESOURCE_TYPE),
        ("dwDisplayType", UInt32),
        ("dwUsage", UInt32),
        ("lpLocalName", win32more.Foundation.PSTR),
        ("lpRemoteName", win32more.Foundation.PSTR),
        ("lpComment", win32more.Foundation.PSTR),
        ("lpProvider", win32more.Foundation.PSTR),
    ]
    return NETRESOURCEA
def _define_NETRESOURCEW_head():
    class NETRESOURCEW(Structure):
        pass
    return NETRESOURCEW
def _define_NETRESOURCEW():
    NETRESOURCEW = win32more.NetworkManagement.WNet.NETRESOURCEW_head
    NETRESOURCEW._fields_ = [
        ("dwScope", win32more.NetworkManagement.WNet.NET_RESOURCE_SCOPE),
        ("dwType", win32more.NetworkManagement.WNet.NET_RESOURCE_TYPE),
        ("dwDisplayType", UInt32),
        ("dwUsage", UInt32),
        ("lpLocalName", win32more.Foundation.PWSTR),
        ("lpRemoteName", win32more.Foundation.PWSTR),
        ("lpComment", win32more.Foundation.PWSTR),
        ("lpProvider", win32more.Foundation.PWSTR),
    ]
    return NETRESOURCEW
def _define_CONNECTDLGSTRUCTA_head():
    class CONNECTDLGSTRUCTA(Structure):
        pass
    return CONNECTDLGSTRUCTA
def _define_CONNECTDLGSTRUCTA():
    CONNECTDLGSTRUCTA = win32more.NetworkManagement.WNet.CONNECTDLGSTRUCTA_head
    CONNECTDLGSTRUCTA._fields_ = [
        ("cbStructure", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("lpConnRes", POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head)),
        ("dwFlags", win32more.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS),
        ("dwDevNum", UInt32),
    ]
    return CONNECTDLGSTRUCTA
def _define_CONNECTDLGSTRUCTW_head():
    class CONNECTDLGSTRUCTW(Structure):
        pass
    return CONNECTDLGSTRUCTW
def _define_CONNECTDLGSTRUCTW():
    CONNECTDLGSTRUCTW = win32more.NetworkManagement.WNet.CONNECTDLGSTRUCTW_head
    CONNECTDLGSTRUCTW._fields_ = [
        ("cbStructure", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("lpConnRes", POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head)),
        ("dwFlags", win32more.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS),
        ("dwDevNum", UInt32),
    ]
    return CONNECTDLGSTRUCTW
def _define_DISCDLGSTRUCTA_head():
    class DISCDLGSTRUCTA(Structure):
        pass
    return DISCDLGSTRUCTA
def _define_DISCDLGSTRUCTA():
    DISCDLGSTRUCTA = win32more.NetworkManagement.WNet.DISCDLGSTRUCTA_head
    DISCDLGSTRUCTA._fields_ = [
        ("cbStructure", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("lpLocalName", win32more.Foundation.PSTR),
        ("lpRemoteName", win32more.Foundation.PSTR),
        ("dwFlags", win32more.NetworkManagement.WNet.DISCDLGSTRUCT_FLAGS),
    ]
    return DISCDLGSTRUCTA
def _define_DISCDLGSTRUCTW_head():
    class DISCDLGSTRUCTW(Structure):
        pass
    return DISCDLGSTRUCTW
def _define_DISCDLGSTRUCTW():
    DISCDLGSTRUCTW = win32more.NetworkManagement.WNet.DISCDLGSTRUCTW_head
    DISCDLGSTRUCTW._fields_ = [
        ("cbStructure", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("lpLocalName", win32more.Foundation.PWSTR),
        ("lpRemoteName", win32more.Foundation.PWSTR),
        ("dwFlags", win32more.NetworkManagement.WNet.DISCDLGSTRUCT_FLAGS),
    ]
    return DISCDLGSTRUCTW
def _define_UNIVERSAL_NAME_INFOA_head():
    class UNIVERSAL_NAME_INFOA(Structure):
        pass
    return UNIVERSAL_NAME_INFOA
def _define_UNIVERSAL_NAME_INFOA():
    UNIVERSAL_NAME_INFOA = win32more.NetworkManagement.WNet.UNIVERSAL_NAME_INFOA_head
    UNIVERSAL_NAME_INFOA._fields_ = [
        ("lpUniversalName", win32more.Foundation.PSTR),
    ]
    return UNIVERSAL_NAME_INFOA
def _define_UNIVERSAL_NAME_INFOW_head():
    class UNIVERSAL_NAME_INFOW(Structure):
        pass
    return UNIVERSAL_NAME_INFOW
def _define_UNIVERSAL_NAME_INFOW():
    UNIVERSAL_NAME_INFOW = win32more.NetworkManagement.WNet.UNIVERSAL_NAME_INFOW_head
    UNIVERSAL_NAME_INFOW._fields_ = [
        ("lpUniversalName", win32more.Foundation.PWSTR),
    ]
    return UNIVERSAL_NAME_INFOW
def _define_REMOTE_NAME_INFOA_head():
    class REMOTE_NAME_INFOA(Structure):
        pass
    return REMOTE_NAME_INFOA
def _define_REMOTE_NAME_INFOA():
    REMOTE_NAME_INFOA = win32more.NetworkManagement.WNet.REMOTE_NAME_INFOA_head
    REMOTE_NAME_INFOA._fields_ = [
        ("lpUniversalName", win32more.Foundation.PSTR),
        ("lpConnectionName", win32more.Foundation.PSTR),
        ("lpRemainingPath", win32more.Foundation.PSTR),
    ]
    return REMOTE_NAME_INFOA
def _define_REMOTE_NAME_INFOW_head():
    class REMOTE_NAME_INFOW(Structure):
        pass
    return REMOTE_NAME_INFOW
def _define_REMOTE_NAME_INFOW():
    REMOTE_NAME_INFOW = win32more.NetworkManagement.WNet.REMOTE_NAME_INFOW_head
    REMOTE_NAME_INFOW._fields_ = [
        ("lpUniversalName", win32more.Foundation.PWSTR),
        ("lpConnectionName", win32more.Foundation.PWSTR),
        ("lpRemainingPath", win32more.Foundation.PWSTR),
    ]
    return REMOTE_NAME_INFOW
def _define_NETINFOSTRUCT_head():
    class NETINFOSTRUCT(Structure):
        pass
    return NETINFOSTRUCT
def _define_NETINFOSTRUCT():
    NETINFOSTRUCT = win32more.NetworkManagement.WNet.NETINFOSTRUCT_head
    NETINFOSTRUCT._fields_ = [
        ("cbStructure", UInt32),
        ("dwProviderVersion", UInt32),
        ("dwStatus", win32more.Foundation.WIN32_ERROR),
        ("dwCharacteristics", win32more.NetworkManagement.WNet.NETINFOSTRUCT_CHARACTERISTICS),
        ("dwHandle", UIntPtr),
        ("wNetType", UInt16),
        ("dwPrinters", UInt32),
        ("dwDrives", UInt32),
    ]
    return NETINFOSTRUCT
def _define_NETCONNECTINFOSTRUCT_head():
    class NETCONNECTINFOSTRUCT(Structure):
        pass
    return NETCONNECTINFOSTRUCT
def _define_NETCONNECTINFOSTRUCT():
    NETCONNECTINFOSTRUCT = win32more.NetworkManagement.WNet.NETCONNECTINFOSTRUCT_head
    NETCONNECTINFOSTRUCT._fields_ = [
        ("cbStructure", UInt32),
        ("dwFlags", UInt32),
        ("dwSpeed", UInt32),
        ("dwDelay", UInt32),
        ("dwOptDataSize", UInt32),
    ]
    return NETCONNECTINFOSTRUCT
def _define_PF_NPAddConnection():
    return CFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)
def _define_PF_NPAddConnection3():
    return CFUNCTYPE(UInt32,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)
def _define_PF_NPAddConnection4():
    return CFUNCTYPE(UInt32,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),c_void_p,UInt32,UInt32,c_char_p_no,UInt32, use_last_error=False)
def _define_PF_NPCancelConnection():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)
def _define_PF_NPCancelConnection2():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,UInt32, use_last_error=False)
def _define_PF_NPGetConnection():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32), use_last_error=False)
def _define_PF_NPGetConnection3():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_void_p,POINTER(UInt32), use_last_error=False)
def _define_PF_NPGetUniversalName():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_void_p,POINTER(UInt32), use_last_error=False)
def _define_PF_NPGetConnectionPerformance():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.WNet.NETCONNECTINFOSTRUCT_head), use_last_error=False)
def _define_PF_NPOpenEnum():
    return CFUNCTYPE(UInt32,UInt32,UInt32,UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),POINTER(win32more.Foundation.HANDLE), use_last_error=False)
def _define_PF_NPEnumResource():
    return CFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32),c_void_p,POINTER(UInt32), use_last_error=False)
def _define_PF_NPCloseEnum():
    return CFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)
def _define_PF_NPGetCaps():
    return CFUNCTYPE(UInt32,UInt32, use_last_error=False)
def _define_PF_NPGetUser():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32), use_last_error=False)
def _define_PF_NPGetPersistentUseOptionsForConnection():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,c_char_p_no,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)
def _define_PF_NPDeviceMode():
    return CFUNCTYPE(UInt32,win32more.Foundation.HWND, use_last_error=False)
def _define_PF_NPSearchDialog():
    return CFUNCTYPE(UInt32,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),POINTER(Void),UInt32,POINTER(UInt32), use_last_error=False)
def _define_PF_NPGetResourceParent():
    return CFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),c_void_p,POINTER(UInt32), use_last_error=False)
def _define_PF_NPGetResourceInformation():
    return CFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),c_void_p,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR), use_last_error=False)
def _define_PF_NPFormatNetworkName():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32),UInt32,UInt32, use_last_error=False)
def _define_PF_NPGetPropertyText():
    return CFUNCTYPE(UInt32,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(Char),UInt32,UInt32, use_last_error=False)
def _define_PF_NPPropertyDialog():
    return CFUNCTYPE(UInt32,win32more.Foundation.HWND,UInt32,UInt32,win32more.Foundation.PWSTR,UInt32, use_last_error=False)
def _define_PF_NPGetDirectoryType():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Int32),win32more.Foundation.BOOL, use_last_error=False)
def _define_PF_NPDirectoryNotify():
    return CFUNCTYPE(UInt32,win32more.Foundation.HWND,win32more.Foundation.PWSTR,UInt32, use_last_error=False)
def _define_PF_NPLogonNotify():
    return CFUNCTYPE(UInt32,POINTER(win32more.Foundation.LUID_head),win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.PWSTR,c_void_p,POINTER(win32more.Foundation.PWSTR), use_last_error=False)
def _define_PF_NPPasswordChangeNotify():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.PWSTR,c_void_p,win32more.Foundation.PWSTR,c_void_p,UInt32, use_last_error=False)
def _define_NOTIFYINFO_head():
    class NOTIFYINFO(Structure):
        pass
    return NOTIFYINFO
def _define_NOTIFYINFO():
    NOTIFYINFO = win32more.NetworkManagement.WNet.NOTIFYINFO_head
    NOTIFYINFO._fields_ = [
        ("dwNotifyStatus", UInt32),
        ("dwOperationStatus", UInt32),
        ("lpContext", c_void_p),
    ]
    return NOTIFYINFO
def _define_NOTIFYADD_head():
    class NOTIFYADD(Structure):
        pass
    return NOTIFYADD
def _define_NOTIFYADD():
    NOTIFYADD = win32more.NetworkManagement.WNet.NOTIFYADD_head
    NOTIFYADD._fields_ = [
        ("hwndOwner", win32more.Foundation.HWND),
        ("NetResource", win32more.NetworkManagement.WNet.NETRESOURCEA),
        ("dwAddFlags", win32more.NetworkManagement.WNet.NET_USE_CONNECT_FLAGS),
    ]
    return NOTIFYADD
def _define_NOTIFYCANCEL_head():
    class NOTIFYCANCEL(Structure):
        pass
    return NOTIFYCANCEL
def _define_NOTIFYCANCEL():
    NOTIFYCANCEL = win32more.NetworkManagement.WNet.NOTIFYCANCEL_head
    NOTIFYCANCEL._fields_ = [
        ("lpName", win32more.Foundation.PWSTR),
        ("lpProvider", win32more.Foundation.PWSTR),
        ("dwFlags", UInt32),
        ("fForce", win32more.Foundation.BOOL),
    ]
    return NOTIFYCANCEL
def _define_PF_AddConnectNotify():
    return CFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NOTIFYINFO_head),POINTER(win32more.NetworkManagement.WNet.NOTIFYADD_head), use_last_error=False)
def _define_PF_CancelConnectNotify():
    return CFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NOTIFYINFO_head),POINTER(win32more.NetworkManagement.WNet.NOTIFYCANCEL_head), use_last_error=False)
def _define_PF_NPFMXGetPermCaps():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)
def _define_PF_NPFMXEditPerm():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.HWND,UInt32, use_last_error=False)
def _define_PF_NPFMXGetPermHelp():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.BOOL,POINTER(Void),POINTER(UInt32),POINTER(UInt32), use_last_error=False)
def _define_WNetAddConnectionA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("WNetAddConnectionA", windll["MPR"]), ((1, 'lpRemoteName'),(1, 'lpPassword'),(1, 'lpLocalName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetAddConnectionW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("WNetAddConnectionW", windll["MPR"]), ((1, 'lpRemoteName'),(1, 'lpPassword'),(1, 'lpLocalName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetAddConnection():
    return win32more.NetworkManagement.WNet.WNetAddConnectionW
def _define_WNetAddConnection2A():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("WNetAddConnection2A", windll["MPR"]), ((1, 'lpNetResource'),(1, 'lpPassword'),(1, 'lpUserName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetAddConnection2W():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("WNetAddConnection2W", windll["MPR"]), ((1, 'lpNetResource'),(1, 'lpPassword'),(1, 'lpUserName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetAddConnection2():
    return win32more.NetworkManagement.WNet.WNetAddConnection2W
def _define_WNetAddConnection3A():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("WNetAddConnection3A", windll["MPR"]), ((1, 'hwndOwner'),(1, 'lpNetResource'),(1, 'lpPassword'),(1, 'lpUserName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetAddConnection3W():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("WNetAddConnection3W", windll["MPR"]), ((1, 'hwndOwner'),(1, 'lpNetResource'),(1, 'lpPassword'),(1, 'lpUserName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetAddConnection3():
    return win32more.NetworkManagement.WNet.WNetAddConnection3W
def _define_WNetAddConnection4A():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head),c_void_p,UInt32,UInt32,c_char_p_no,UInt32, use_last_error=False)(("WNetAddConnection4A", windll["MPR"]), ((1, 'hwndOwner'),(1, 'lpNetResource'),(1, 'pAuthBuffer'),(1, 'cbAuthBuffer'),(1, 'dwFlags'),(1, 'lpUseOptions'),(1, 'cbUseOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetAddConnection4W():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),c_void_p,UInt32,UInt32,c_char_p_no,UInt32, use_last_error=False)(("WNetAddConnection4W", windll["MPR"]), ((1, 'hwndOwner'),(1, 'lpNetResource'),(1, 'pAuthBuffer'),(1, 'cbAuthBuffer'),(1, 'dwFlags'),(1, 'lpUseOptions'),(1, 'cbUseOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetAddConnection4():
    return win32more.NetworkManagement.WNet.WNetAddConnection4W
def _define_WNetCancelConnectionA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.BOOL, use_last_error=False)(("WNetCancelConnectionA", windll["MPR"]), ((1, 'lpName'),(1, 'fForce'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetCancelConnectionW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("WNetCancelConnectionW", windll["MPR"]), ((1, 'lpName'),(1, 'fForce'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetCancelConnection():
    return win32more.NetworkManagement.WNet.WNetCancelConnectionW
def _define_WNetCancelConnection2A():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.BOOL, use_last_error=False)(("WNetCancelConnection2A", windll["MPR"]), ((1, 'lpName'),(1, 'dwFlags'),(1, 'fForce'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetCancelConnection2W():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.BOOL, use_last_error=False)(("WNetCancelConnection2W", windll["MPR"]), ((1, 'lpName'),(1, 'dwFlags'),(1, 'fForce'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetCancelConnection2():
    return win32more.NetworkManagement.WNet.WNetCancelConnection2W
def _define_WNetGetConnectionA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(Byte),POINTER(UInt32), use_last_error=False)(("WNetGetConnectionA", windll["MPR"]), ((1, 'lpLocalName'),(1, 'lpRemoteName'),(1, 'lpnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetConnectionW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32), use_last_error=False)(("WNetGetConnectionW", windll["MPR"]), ((1, 'lpLocalName'),(1, 'lpRemoteName'),(1, 'lpnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetConnection():
    return win32more.NetworkManagement.WNet.WNetGetConnectionW
def _define_WNetUseConnectionA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.NetworkManagement.WNet.NET_USE_CONNECT_FLAGS,POINTER(Byte),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("WNetUseConnectionA", windll["MPR"]), ((1, 'hwndOwner'),(1, 'lpNetResource'),(1, 'lpPassword'),(1, 'lpUserId'),(1, 'dwFlags'),(1, 'lpAccessName'),(1, 'lpBufferSize'),(1, 'lpResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetUseConnectionW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.NetworkManagement.WNet.NET_USE_CONNECT_FLAGS,POINTER(Char),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("WNetUseConnectionW", windll["MPR"]), ((1, 'hwndOwner'),(1, 'lpNetResource'),(1, 'lpPassword'),(1, 'lpUserId'),(1, 'dwFlags'),(1, 'lpAccessName'),(1, 'lpBufferSize'),(1, 'lpResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetUseConnection():
    return win32more.NetworkManagement.WNet.WNetUseConnectionW
def _define_WNetUseConnection4A():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head),c_void_p,UInt32,UInt32,c_char_p_no,UInt32,POINTER(Byte),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("WNetUseConnection4A", windll["MPR"]), ((1, 'hwndOwner'),(1, 'lpNetResource'),(1, 'pAuthBuffer'),(1, 'cbAuthBuffer'),(1, 'dwFlags'),(1, 'lpUseOptions'),(1, 'cbUseOptions'),(1, 'lpAccessName'),(1, 'lpBufferSize'),(1, 'lpResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetUseConnection4W():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),c_void_p,UInt32,UInt32,c_char_p_no,UInt32,POINTER(Char),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("WNetUseConnection4W", windll["MPR"]), ((1, 'hwndOwner'),(1, 'lpNetResource'),(1, 'pAuthBuffer'),(1, 'cbAuthBuffer'),(1, 'dwFlags'),(1, 'lpUseOptions'),(1, 'cbUseOptions'),(1, 'lpAccessName'),(1, 'lpBufferSize'),(1, 'lpResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetUseConnection4():
    return win32more.NetworkManagement.WNet.WNetUseConnection4W
def _define_WNetConnectionDialog():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,UInt32, use_last_error=False)(("WNetConnectionDialog", windll["MPR"]), ((1, 'hwnd'),(1, 'dwType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetDisconnectDialog():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,UInt32, use_last_error=False)(("WNetDisconnectDialog", windll["MPR"]), ((1, 'hwnd'),(1, 'dwType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetConnectionDialog1A():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.CONNECTDLGSTRUCTA_head), use_last_error=False)(("WNetConnectionDialog1A", windll["MPR"]), ((1, 'lpConnDlgStruct'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetConnectionDialog1W():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.CONNECTDLGSTRUCTW_head), use_last_error=False)(("WNetConnectionDialog1W", windll["MPR"]), ((1, 'lpConnDlgStruct'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetConnectionDialog1():
    return win32more.NetworkManagement.WNet.WNetConnectionDialog1W
def _define_WNetDisconnectDialog1A():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.DISCDLGSTRUCTA_head), use_last_error=False)(("WNetDisconnectDialog1A", windll["MPR"]), ((1, 'lpConnDlgStruct'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetDisconnectDialog1W():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.DISCDLGSTRUCTW_head), use_last_error=False)(("WNetDisconnectDialog1W", windll["MPR"]), ((1, 'lpConnDlgStruct'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetDisconnectDialog1():
    return win32more.NetworkManagement.WNet.WNetDisconnectDialog1W
def _define_WNetOpenEnumA():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.WNet.NET_RESOURCE_SCOPE,win32more.NetworkManagement.WNet.NET_RESOURCE_TYPE,win32more.NetworkManagement.WNet.WNET_OPEN_ENUM_USAGE,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head),POINTER(win32more.NetworkManagement.WNet.NetEnumHandle), use_last_error=False)(("WNetOpenEnumA", windll["MPR"]), ((1, 'dwScope'),(1, 'dwType'),(1, 'dwUsage'),(1, 'lpNetResource'),(1, 'lphEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetOpenEnumW():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.WNet.NET_RESOURCE_SCOPE,win32more.NetworkManagement.WNet.NET_RESOURCE_TYPE,win32more.NetworkManagement.WNet.WNET_OPEN_ENUM_USAGE,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),POINTER(win32more.NetworkManagement.WNet.NetEnumHandle), use_last_error=False)(("WNetOpenEnumW", windll["MPR"]), ((1, 'dwScope'),(1, 'dwType'),(1, 'dwUsage'),(1, 'lpNetResource'),(1, 'lphEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetOpenEnum():
    return win32more.NetworkManagement.WNet.WNetOpenEnumW
def _define_WNetEnumResourceA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32),c_void_p,POINTER(UInt32), use_last_error=False)(("WNetEnumResourceA", windll["MPR"]), ((1, 'hEnum'),(1, 'lpcCount'),(1, 'lpBuffer'),(1, 'lpBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetEnumResourceW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32),c_void_p,POINTER(UInt32), use_last_error=False)(("WNetEnumResourceW", windll["MPR"]), ((1, 'hEnum'),(1, 'lpcCount'),(1, 'lpBuffer'),(1, 'lpBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetEnumResource():
    return win32more.NetworkManagement.WNet.WNetEnumResourceW
def _define_WNetCloseEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("WNetCloseEnum", windll["MPR"]), ((1, 'hEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetResourceParentA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head),c_void_p,POINTER(UInt32), use_last_error=False)(("WNetGetResourceParentA", windll["MPR"]), ((1, 'lpNetResource'),(1, 'lpBuffer'),(1, 'lpcbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetResourceParentW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),c_void_p,POINTER(UInt32), use_last_error=False)(("WNetGetResourceParentW", windll["MPR"]), ((1, 'lpNetResource'),(1, 'lpBuffer'),(1, 'lpcbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetResourceParent():
    return win32more.NetworkManagement.WNet.WNetGetResourceParentW
def _define_WNetGetResourceInformationA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head),c_void_p,POINTER(UInt32),POINTER(win32more.Foundation.PSTR), use_last_error=False)(("WNetGetResourceInformationA", windll["MPR"]), ((1, 'lpNetResource'),(1, 'lpBuffer'),(1, 'lpcbBuffer'),(1, 'lplpSystem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetResourceInformationW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),c_void_p,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("WNetGetResourceInformationW", windll["MPR"]), ((1, 'lpNetResource'),(1, 'lpBuffer'),(1, 'lpcbBuffer'),(1, 'lplpSystem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetResourceInformation():
    return win32more.NetworkManagement.WNet.WNetGetResourceInformationW
def _define_WNetGetUniversalNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.NetworkManagement.WNet.UNC_INFO_LEVEL,c_void_p,POINTER(UInt32), use_last_error=False)(("WNetGetUniversalNameA", windll["MPR"]), ((1, 'lpLocalPath'),(1, 'dwInfoLevel'),(1, 'lpBuffer'),(1, 'lpBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetUniversalNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.WNet.UNC_INFO_LEVEL,c_void_p,POINTER(UInt32), use_last_error=False)(("WNetGetUniversalNameW", windll["MPR"]), ((1, 'lpLocalPath'),(1, 'dwInfoLevel'),(1, 'lpBuffer'),(1, 'lpBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetUniversalName():
    return win32more.NetworkManagement.WNet.WNetGetUniversalNameW
def _define_WNetGetUserA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(Byte),POINTER(UInt32), use_last_error=False)(("WNetGetUserA", windll["MPR"]), ((1, 'lpName'),(1, 'lpUserName'),(1, 'lpnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetUserW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32), use_last_error=False)(("WNetGetUserW", windll["MPR"]), ((1, 'lpName'),(1, 'lpUserName'),(1, 'lpnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetUser():
    return win32more.NetworkManagement.WNet.WNetGetUserW
def _define_WNetGetProviderNameA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(("WNetGetProviderNameA", windll["MPR"]), ((1, 'dwNetType'),(1, 'lpProviderName'),(1, 'lpBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetProviderNameW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(("WNetGetProviderNameW", windll["MPR"]), ((1, 'dwNetType'),(1, 'lpProviderName'),(1, 'lpBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetProviderName():
    return win32more.NetworkManagement.WNet.WNetGetProviderNameW
def _define_WNetGetNetworkInformationA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.WNet.NETINFOSTRUCT_head), use_last_error=False)(("WNetGetNetworkInformationA", windll["MPR"]), ((1, 'lpProvider'),(1, 'lpNetInfoStruct'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetNetworkInformationW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.WNet.NETINFOSTRUCT_head), use_last_error=False)(("WNetGetNetworkInformationW", windll["MPR"]), ((1, 'lpProvider'),(1, 'lpNetInfoStruct'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetNetworkInformation():
    return win32more.NetworkManagement.WNet.WNetGetNetworkInformationW
def _define_WNetGetLastErrorA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(Byte),UInt32,POINTER(Byte),UInt32, use_last_error=True)(("WNetGetLastErrorA", windll["MPR"]), ((1, 'lpError'),(1, 'lpErrorBuf'),(1, 'nErrorBufSize'),(1, 'lpNameBuf'),(1, 'nNameBufSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetLastErrorW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(Char),UInt32,POINTER(Char),UInt32, use_last_error=True)(("WNetGetLastErrorW", windll["MPR"]), ((1, 'lpError'),(1, 'lpErrorBuf'),(1, 'nErrorBufSize'),(1, 'lpNameBuf'),(1, 'nNameBufSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetGetLastError():
    return win32more.NetworkManagement.WNet.WNetGetLastErrorW
def _define_MultinetGetConnectionPerformanceA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head),POINTER(win32more.NetworkManagement.WNet.NETCONNECTINFOSTRUCT_head), use_last_error=False)(("MultinetGetConnectionPerformanceA", windll["MPR"]), ((1, 'lpNetResource'),(1, 'lpNetConnectInfoStruct'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MultinetGetConnectionPerformanceW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),POINTER(win32more.NetworkManagement.WNet.NETCONNECTINFOSTRUCT_head), use_last_error=False)(("MultinetGetConnectionPerformanceW", windll["MPR"]), ((1, 'lpNetResource'),(1, 'lpNetConnectInfoStruct'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MultinetGetConnectionPerformance():
    return win32more.NetworkManagement.WNet.MultinetGetConnectionPerformanceW
def _define_NPAddConnection():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("NPAddConnection", windll["davclnt"]), ((1, 'lpNetResource'),(1, 'lpPassword'),(1, 'lpUserName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPAddConnection3():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.NetworkManagement.WNet.NET_USE_CONNECT_FLAGS, use_last_error=False)(("NPAddConnection3", windll["davclnt"]), ((1, 'hwndOwner'),(1, 'lpNetResource'),(1, 'lpPassword'),(1, 'lpUserName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPAddConnection4():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),c_void_p,UInt32,UInt32,c_char_p_no,UInt32, use_last_error=False)(("NPAddConnection4", windll["NTLANMAN"]), ((1, 'hwndOwner'),(1, 'lpNetResource'),(1, 'lpAuthBuffer'),(1, 'cbAuthBuffer'),(1, 'dwFlags'),(1, 'lpUseOptions'),(1, 'cbUseOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPCancelConnection():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("NPCancelConnection", windll["davclnt"]), ((1, 'lpName'),(1, 'fForce'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPCancelConnection2():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,UInt32, use_last_error=False)(("NPCancelConnection2", windll["NTLANMAN"]), ((1, 'lpName'),(1, 'fForce'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPGetConnection():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32), use_last_error=False)(("NPGetConnection", windll["davclnt"]), ((1, 'lpLocalName'),(1, 'lpRemoteName'),(1, 'lpnBufferLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPGetConnection3():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_void_p,POINTER(UInt32), use_last_error=False)(("NPGetConnection3", windll["NTLANMAN"]), ((1, 'lpLocalName'),(1, 'dwLevel'),(1, 'lpBuffer'),(1, 'lpBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPGetUniversalName():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.NetworkManagement.WNet.UNC_INFO_LEVEL,c_void_p,POINTER(UInt32), use_last_error=False)(("NPGetUniversalName", windll["davclnt"]), ((1, 'lpLocalPath'),(1, 'dwInfoLevel'),(1, 'lpBuffer'),(1, 'lpBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPGetConnectionPerformance():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.NetworkManagement.WNet.NETCONNECTINFOSTRUCT_head), use_last_error=False)(("NPGetConnectionPerformance", windll["NTLANMAN"]), ((1, 'lpRemoteName'),(1, 'lpNetConnectInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPOpenEnum():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("NPOpenEnum", windll["davclnt"]), ((1, 'dwScope'),(1, 'dwType'),(1, 'dwUsage'),(1, 'lpNetResource'),(1, 'lphEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPEnumResource():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32),c_void_p,POINTER(UInt32), use_last_error=False)(("NPEnumResource", windll["davclnt"]), ((1, 'hEnum'),(1, 'lpcCount'),(1, 'lpBuffer'),(1, 'lpBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPCloseEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("NPCloseEnum", windll["davclnt"]), ((1, 'hEnum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPGetCaps():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("NPGetCaps", windll["davclnt"]), ((1, 'ndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPGetUser():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32), use_last_error=False)(("NPGetUser", windll["davclnt"]), ((1, 'lpName'),(1, 'lpUserName'),(1, 'lpnBufferLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPGetPersistentUseOptionsForConnection():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,c_char_p_no,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(("NPGetPersistentUseOptionsForConnection", windll["NTLANMAN"]), ((1, 'lpRemotePath'),(1, 'lpReadUseOptions'),(1, 'cbReadUseOptions'),(1, 'lpWriteUseOptions'),(1, 'lpSizeWriteUseOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPGetResourceParent():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),c_void_p,POINTER(UInt32), use_last_error=False)(("NPGetResourceParent", windll["davclnt"]), ((1, 'lpNetResource'),(1, 'lpBuffer'),(1, 'lpBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPGetResourceInformation():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head),c_void_p,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("NPGetResourceInformation", windll["davclnt"]), ((1, 'lpNetResource'),(1, 'lpBuffer'),(1, 'lpBufferSize'),(1, 'lplpSystem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NPFormatNetworkName():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Char),POINTER(UInt32),win32more.NetworkManagement.WNet.NETWORK_NAME_FORMAT_FLAGS,UInt32, use_last_error=False)(("NPFormatNetworkName", windll["davclnt"]), ((1, 'lpRemoteName'),(1, 'lpFormattedName'),(1, 'lpnLength'),(1, 'dwFlags'),(1, 'dwAveCharPerLine'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetSetLastErrorA():
    try:
        return WINFUNCTYPE(Void,UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("WNetSetLastErrorA", windll["MPR"]), ((1, 'err'),(1, 'lpError'),(1, 'lpProviders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetSetLastErrorW():
    try:
        return WINFUNCTYPE(Void,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("WNetSetLastErrorW", windll["MPR"]), ((1, 'err'),(1, 'lpError'),(1, 'lpProviders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WNetSetLastError():
    return win32more.NetworkManagement.WNet.WNetSetLastErrorW
__all__ = [
    "WNGETCON_CONNECTED",
    "WNGETCON_DISCONNECTED",
    "WNNC_SPEC_VERSION",
    "WNNC_SPEC_VERSION51",
    "WNNC_NET_TYPE",
    "WNNC_NET_NONE",
    "WNNC_DRIVER_VERSION",
    "WNNC_USER",
    "WNNC_USR_GETUSER",
    "WNNC_CONNECTION",
    "WNNC_CON_ADDCONNECTION",
    "WNNC_CON_CANCELCONNECTION",
    "WNNC_CON_GETCONNECTIONS",
    "WNNC_CON_ADDCONNECTION3",
    "WNNC_CON_ADDCONNECTION4",
    "WNNC_CON_CANCELCONNECTION2",
    "WNNC_CON_GETPERFORMANCE",
    "WNNC_CON_DEFER",
    "WNNC_DIALOG",
    "WNNC_DLG_DEVICEMODE",
    "WNNC_DLG_PROPERTYDIALOG",
    "WNNC_DLG_SEARCHDIALOG",
    "WNNC_DLG_FORMATNETWORKNAME",
    "WNNC_DLG_PERMISSIONEDITOR",
    "WNNC_DLG_GETRESOURCEPARENT",
    "WNNC_DLG_GETRESOURCEINFORMATION",
    "WNNC_ADMIN",
    "WNNC_ADM_GETDIRECTORYTYPE",
    "WNNC_ADM_DIRECTORYNOTIFY",
    "WNNC_ENUMERATION",
    "WNNC_ENUM_GLOBAL",
    "WNNC_ENUM_LOCAL",
    "WNNC_ENUM_CONTEXT",
    "WNNC_ENUM_SHAREABLE",
    "WNNC_START",
    "WNNC_WAIT_FOR_START",
    "WNNC_CONNECTION_FLAGS",
    "WNTYPE_DRIVE",
    "WNTYPE_FILE",
    "WNTYPE_PRINTER",
    "WNTYPE_COMM",
    "WNSRCH_REFRESH_FIRST_LEVEL",
    "WNDT_NORMAL",
    "WNDT_NETWORK",
    "WN_NETWORK_CLASS",
    "WN_CREDENTIAL_CLASS",
    "WN_PRIMARY_AUTHENT_CLASS",
    "WN_SERVICE_CLASS",
    "WN_VALID_LOGON_ACCOUNT",
    "WN_NT_PASSWORD_CHANGED",
    "NOTIFY_PRE",
    "NOTIFY_POST",
    "WNPERMC_PERM",
    "WNPERMC_AUDIT",
    "WNPERMC_OWNER",
    "RESOURCE_RECENT",
    "RESOURCETYPE_RESERVED",
    "RESOURCETYPE_UNKNOWN",
    "RESOURCEUSAGE_NOLOCALDEVICE",
    "RESOURCEUSAGE_SIBLING",
    "RESOURCEUSAGE_RESERVED",
    "RESOURCEDISPLAYTYPE_NETWORK",
    "RESOURCEDISPLAYTYPE_ROOT",
    "RESOURCEDISPLAYTYPE_SHAREADMIN",
    "RESOURCEDISPLAYTYPE_DIRECTORY",
    "RESOURCEDISPLAYTYPE_NDSCONTAINER",
    "NETPROPERTY_PERSISTENT",
    "CONNECT_NEED_DRIVE",
    "CONNECT_REFCOUNT",
    "CONNECT_LOCALDRIVE",
    "CONNECT_CURRENT_MEDIA",
    "CONNECT_RESERVED",
    "CONNECT_CRED_RESET",
    "CONNECT_REQUIRE_INTEGRITY",
    "CONNECT_REQUIRE_PRIVACY",
    "CONNECT_WRITE_THROUGH_SEMANTICS",
    "CONNECT_GLOBAL_MAPPING",
    "WNFMT_INENUM",
    "WNFMT_CONNECTION",
    "WNCON_FORNETCARD",
    "WNCON_NOTROUTED",
    "WNCON_SLOWLINK",
    "WNCON_DYNAMIC",
    "UNC_INFO_LEVEL",
    "UNIVERSAL_NAME_INFO_LEVEL",
    "REMOTE_NAME_INFO_LEVEL",
    "WNPERM_DLG",
    "WNPERM_DLG_PERM",
    "WNPERM_DLG_AUDIT",
    "WNPERM_DLG_OWNER",
    "WNET_OPEN_ENUM_USAGE",
    "RESOURCEUSAGE_NONE",
    "RESOURCEUSAGE_CONNECTABLE",
    "RESOURCEUSAGE_CONTAINER",
    "RESOURCEUSAGE_ATTACHED",
    "RESOURCEUSAGE_ALL",
    "NET_USE_CONNECT_FLAGS",
    "CONNECT_INTERACTIVE",
    "CONNECT_PROMPT",
    "CONNECT_REDIRECT",
    "CONNECT_UPDATE_PROFILE",
    "CONNECT_COMMANDLINE",
    "CONNECT_CMD_SAVECRED",
    "CONNECT_TEMPORARY",
    "CONNECT_DEFERRED",
    "CONNECT_UPDATE_RECENT",
    "NP_PROPERTY_DIALOG_SELECTION",
    "WNPS_FILE",
    "WNPS_DIR",
    "WNPS_MULT",
    "NPDIRECTORY_NOTIFY_OPERATION",
    "WNDN_MKDIR",
    "WNDN_RMDIR",
    "WNDN_MVDIR",
    "NET_RESOURCE_TYPE",
    "RESOURCETYPE_ANY",
    "RESOURCETYPE_DISK",
    "RESOURCETYPE_PRINT",
    "NETWORK_NAME_FORMAT_FLAGS",
    "WNFMT_MULTILINE",
    "WNFMT_ABBREVIATED",
    "NET_RESOURCE_SCOPE",
    "RESOURCE_CONNECTED",
    "RESOURCE_CONTEXT",
    "RESOURCE_GLOBALNET",
    "RESOURCE_REMEMBERED",
    "NETINFOSTRUCT_CHARACTERISTICS",
    "NETINFO_DLL16",
    "NETINFO_DISKRED",
    "NETINFO_PRINTERRED",
    "CONNECTDLGSTRUCT_FLAGS",
    "CONNDLG_RO_PATH",
    "CONNDLG_CONN_POINT",
    "CONNDLG_USE_MRU",
    "CONNDLG_HIDE_BOX",
    "CONNDLG_PERSIST",
    "CONNDLG_NOT_PERSIST",
    "DISCDLGSTRUCT_FLAGS",
    "DISC_UPDATE_PROFILE",
    "DISC_NO_FORCE",
    "NetEnumHandle",
    "NETRESOURCEA",
    "NETRESOURCEW",
    "CONNECTDLGSTRUCTA",
    "CONNECTDLGSTRUCTW",
    "DISCDLGSTRUCTA",
    "DISCDLGSTRUCTW",
    "UNIVERSAL_NAME_INFOA",
    "UNIVERSAL_NAME_INFOW",
    "REMOTE_NAME_INFOA",
    "REMOTE_NAME_INFOW",
    "NETINFOSTRUCT",
    "NETCONNECTINFOSTRUCT",
    "PF_NPAddConnection",
    "PF_NPAddConnection3",
    "PF_NPAddConnection4",
    "PF_NPCancelConnection",
    "PF_NPCancelConnection2",
    "PF_NPGetConnection",
    "PF_NPGetConnection3",
    "PF_NPGetUniversalName",
    "PF_NPGetConnectionPerformance",
    "PF_NPOpenEnum",
    "PF_NPEnumResource",
    "PF_NPCloseEnum",
    "PF_NPGetCaps",
    "PF_NPGetUser",
    "PF_NPGetPersistentUseOptionsForConnection",
    "PF_NPDeviceMode",
    "PF_NPSearchDialog",
    "PF_NPGetResourceParent",
    "PF_NPGetResourceInformation",
    "PF_NPFormatNetworkName",
    "PF_NPGetPropertyText",
    "PF_NPPropertyDialog",
    "PF_NPGetDirectoryType",
    "PF_NPDirectoryNotify",
    "PF_NPLogonNotify",
    "PF_NPPasswordChangeNotify",
    "NOTIFYINFO",
    "NOTIFYADD",
    "NOTIFYCANCEL",
    "PF_AddConnectNotify",
    "PF_CancelConnectNotify",
    "PF_NPFMXGetPermCaps",
    "PF_NPFMXEditPerm",
    "PF_NPFMXGetPermHelp",
    "WNetAddConnectionA",
    "WNetAddConnectionW",
    "WNetAddConnection",
    "WNetAddConnection2A",
    "WNetAddConnection2W",
    "WNetAddConnection2",
    "WNetAddConnection3A",
    "WNetAddConnection3W",
    "WNetAddConnection3",
    "WNetAddConnection4A",
    "WNetAddConnection4W",
    "WNetAddConnection4",
    "WNetCancelConnectionA",
    "WNetCancelConnectionW",
    "WNetCancelConnection",
    "WNetCancelConnection2A",
    "WNetCancelConnection2W",
    "WNetCancelConnection2",
    "WNetGetConnectionA",
    "WNetGetConnectionW",
    "WNetGetConnection",
    "WNetUseConnectionA",
    "WNetUseConnectionW",
    "WNetUseConnection",
    "WNetUseConnection4A",
    "WNetUseConnection4W",
    "WNetUseConnection4",
    "WNetConnectionDialog",
    "WNetDisconnectDialog",
    "WNetConnectionDialog1A",
    "WNetConnectionDialog1W",
    "WNetConnectionDialog1",
    "WNetDisconnectDialog1A",
    "WNetDisconnectDialog1W",
    "WNetDisconnectDialog1",
    "WNetOpenEnumA",
    "WNetOpenEnumW",
    "WNetOpenEnum",
    "WNetEnumResourceA",
    "WNetEnumResourceW",
    "WNetEnumResource",
    "WNetCloseEnum",
    "WNetGetResourceParentA",
    "WNetGetResourceParentW",
    "WNetGetResourceParent",
    "WNetGetResourceInformationA",
    "WNetGetResourceInformationW",
    "WNetGetResourceInformation",
    "WNetGetUniversalNameA",
    "WNetGetUniversalNameW",
    "WNetGetUniversalName",
    "WNetGetUserA",
    "WNetGetUserW",
    "WNetGetUser",
    "WNetGetProviderNameA",
    "WNetGetProviderNameW",
    "WNetGetProviderName",
    "WNetGetNetworkInformationA",
    "WNetGetNetworkInformationW",
    "WNetGetNetworkInformation",
    "WNetGetLastErrorA",
    "WNetGetLastErrorW",
    "WNetGetLastError",
    "MultinetGetConnectionPerformanceA",
    "MultinetGetConnectionPerformanceW",
    "MultinetGetConnectionPerformance",
    "NPAddConnection",
    "NPAddConnection3",
    "NPAddConnection4",
    "NPCancelConnection",
    "NPCancelConnection2",
    "NPGetConnection",
    "NPGetConnection3",
    "NPGetUniversalName",
    "NPGetConnectionPerformance",
    "NPOpenEnum",
    "NPEnumResource",
    "NPCloseEnum",
    "NPGetCaps",
    "NPGetUser",
    "NPGetPersistentUseOptionsForConnection",
    "NPGetResourceParent",
    "NPGetResourceInformation",
    "NPFormatNetworkName",
    "WNetSetLastErrorA",
    "WNetSetLastErrorW",
    "WNetSetLastError",
]
