from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.NetworkManagement.WNet
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
WNGETCON_CONNECTED: UInt32 = 0
WNGETCON_DISCONNECTED: UInt32 = 1
WNNC_SPEC_VERSION: UInt32 = 1
WNNC_SPEC_VERSION51: UInt32 = 327681
WNNC_NET_TYPE: UInt32 = 2
WNNC_NET_NONE: UInt32 = 0
WNNC_DRIVER_VERSION: UInt32 = 3
WNNC_USER: UInt32 = 4
WNNC_USR_GETUSER: UInt32 = 1
WNNC_CONNECTION: UInt32 = 6
WNNC_CON_ADDCONNECTION: UInt32 = 1
WNNC_CON_CANCELCONNECTION: UInt32 = 2
WNNC_CON_GETCONNECTIONS: UInt32 = 4
WNNC_CON_ADDCONNECTION3: UInt32 = 8
WNNC_CON_ADDCONNECTION4: UInt32 = 16
WNNC_CON_CANCELCONNECTION2: UInt32 = 32
WNNC_CON_GETPERFORMANCE: UInt32 = 64
WNNC_CON_DEFER: UInt32 = 128
WNNC_DIALOG: UInt32 = 8
WNNC_DLG_DEVICEMODE: UInt32 = 1
WNNC_DLG_PROPERTYDIALOG: UInt32 = 32
WNNC_DLG_SEARCHDIALOG: UInt32 = 64
WNNC_DLG_FORMATNETWORKNAME: UInt32 = 128
WNNC_DLG_PERMISSIONEDITOR: UInt32 = 256
WNNC_DLG_GETRESOURCEPARENT: UInt32 = 512
WNNC_DLG_GETRESOURCEINFORMATION: UInt32 = 2048
WNNC_ADMIN: UInt32 = 9
WNNC_ADM_GETDIRECTORYTYPE: UInt32 = 1
WNNC_ADM_DIRECTORYNOTIFY: UInt32 = 2
WNNC_ENUMERATION: UInt32 = 11
WNNC_ENUM_GLOBAL: UInt32 = 1
WNNC_ENUM_LOCAL: UInt32 = 2
WNNC_ENUM_CONTEXT: UInt32 = 4
WNNC_ENUM_SHAREABLE: UInt32 = 8
WNNC_START: UInt32 = 12
WNNC_WAIT_FOR_START: UInt32 = 1
WNNC_CONNECTION_FLAGS: UInt32 = 13
WNTYPE_DRIVE: UInt32 = 1
WNTYPE_FILE: UInt32 = 2
WNTYPE_PRINTER: UInt32 = 3
WNTYPE_COMM: UInt32 = 4
WNSRCH_REFRESH_FIRST_LEVEL: UInt32 = 1
WNDT_NORMAL: UInt32 = 0
WNDT_NETWORK: UInt32 = 1
WN_NETWORK_CLASS: UInt32 = 1
WN_CREDENTIAL_CLASS: UInt32 = 2
WN_PRIMARY_AUTHENT_CLASS: UInt32 = 4
WN_SERVICE_CLASS: UInt32 = 8
WN_VALID_LOGON_ACCOUNT: UInt32 = 1
WN_NT_PASSWORD_CHANGED: UInt32 = 2
NOTIFY_PRE: UInt32 = 1
NOTIFY_POST: UInt32 = 2
WNPERMC_PERM: UInt32 = 1
WNPERMC_AUDIT: UInt32 = 2
WNPERMC_OWNER: UInt32 = 4
RESOURCE_RECENT: UInt32 = 4
RESOURCETYPE_RESERVED: UInt32 = 8
RESOURCETYPE_UNKNOWN: UInt32 = 4294967295
RESOURCEUSAGE_NOLOCALDEVICE: UInt32 = 4
RESOURCEUSAGE_SIBLING: UInt32 = 8
RESOURCEUSAGE_RESERVED: UInt32 = 2147483648
RESOURCEDISPLAYTYPE_NETWORK: UInt32 = 6
RESOURCEDISPLAYTYPE_ROOT: UInt32 = 7
RESOURCEDISPLAYTYPE_SHAREADMIN: UInt32 = 8
RESOURCEDISPLAYTYPE_DIRECTORY: UInt32 = 9
RESOURCEDISPLAYTYPE_NDSCONTAINER: UInt32 = 11
NETPROPERTY_PERSISTENT: UInt32 = 1
CONNECT_NEED_DRIVE: UInt32 = 32
CONNECT_REFCOUNT: UInt32 = 64
CONNECT_LOCALDRIVE: UInt32 = 256
CONNECT_CURRENT_MEDIA: UInt32 = 512
CONNECT_RESERVED: UInt32 = 4278190080
CONNECT_CRED_RESET: UInt32 = 8192
CONNECT_REQUIRE_INTEGRITY: UInt32 = 16384
CONNECT_REQUIRE_PRIVACY: UInt32 = 32768
CONNECT_WRITE_THROUGH_SEMANTICS: UInt32 = 65536
CONNECT_GLOBAL_MAPPING: UInt32 = 262144
WNFMT_INENUM: UInt32 = 16
WNFMT_CONNECTION: UInt32 = 32
WNCON_FORNETCARD: UInt32 = 1
WNCON_NOTROUTED: UInt32 = 2
WNCON_SLOWLINK: UInt32 = 4
WNCON_DYNAMIC: UInt32 = 8
@winfunctype('MPR.dll')
def WNetAddConnectionA(lpRemoteName: win32more.Foundation.PSTR, lpPassword: win32more.Foundation.PSTR, lpLocalName: win32more.Foundation.PSTR) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnectionW(lpRemoteName: win32more.Foundation.PWSTR, lpPassword: win32more.Foundation.PWSTR, lpLocalName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnection2A(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head), lpPassword: win32more.Foundation.PSTR, lpUserName: win32more.Foundation.PSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnection2W(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: win32more.Foundation.PWSTR, lpUserName: win32more.Foundation.PWSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnection3A(hwndOwner: win32more.Foundation.HWND, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head), lpPassword: win32more.Foundation.PSTR, lpUserName: win32more.Foundation.PSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnection3W(hwndOwner: win32more.Foundation.HWND, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: win32more.Foundation.PWSTR, lpUserName: win32more.Foundation.PWSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnection4A(hwndOwner: win32more.Foundation.HWND, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head), pAuthBuffer: c_void_p, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: c_char_p_no, cbUseOptions: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnection4W(hwndOwner: win32more.Foundation.HWND, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), pAuthBuffer: c_void_p, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: c_char_p_no, cbUseOptions: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetCancelConnectionA(lpName: win32more.Foundation.PSTR, fForce: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetCancelConnectionW(lpName: win32more.Foundation.PWSTR, fForce: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetCancelConnection2A(lpName: win32more.Foundation.PSTR, dwFlags: UInt32, fForce: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetCancelConnection2W(lpName: win32more.Foundation.PWSTR, dwFlags: UInt32, fForce: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetConnectionA(lpLocalName: win32more.Foundation.PSTR, lpRemoteName: win32more.Foundation.PSTR, lpnLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetConnectionW(lpLocalName: win32more.Foundation.PWSTR, lpRemoteName: win32more.Foundation.PWSTR, lpnLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetUseConnectionA(hwndOwner: win32more.Foundation.HWND, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head), lpPassword: win32more.Foundation.PSTR, lpUserId: win32more.Foundation.PSTR, dwFlags: win32more.NetworkManagement.WNet.NET_USE_CONNECT_FLAGS, lpAccessName: win32more.Foundation.PSTR, lpBufferSize: POINTER(UInt32), lpResult: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetUseConnectionW(hwndOwner: win32more.Foundation.HWND, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: win32more.Foundation.PWSTR, lpUserId: win32more.Foundation.PWSTR, dwFlags: win32more.NetworkManagement.WNet.NET_USE_CONNECT_FLAGS, lpAccessName: win32more.Foundation.PWSTR, lpBufferSize: POINTER(UInt32), lpResult: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetUseConnection4A(hwndOwner: win32more.Foundation.HWND, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head), pAuthBuffer: c_void_p, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: c_char_p_no, cbUseOptions: UInt32, lpAccessName: win32more.Foundation.PSTR, lpBufferSize: POINTER(UInt32), lpResult: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetUseConnection4W(hwndOwner: win32more.Foundation.HWND, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), pAuthBuffer: c_void_p, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: c_char_p_no, cbUseOptions: UInt32, lpAccessName: win32more.Foundation.PWSTR, lpBufferSize: POINTER(UInt32), lpResult: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetConnectionDialog(hwnd: win32more.Foundation.HWND, dwType: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetDisconnectDialog(hwnd: win32more.Foundation.HWND, dwType: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetConnectionDialog1A(lpConnDlgStruct: POINTER(win32more.NetworkManagement.WNet.CONNECTDLGSTRUCTA_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetConnectionDialog1W(lpConnDlgStruct: POINTER(win32more.NetworkManagement.WNet.CONNECTDLGSTRUCTW_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetDisconnectDialog1A(lpConnDlgStruct: POINTER(win32more.NetworkManagement.WNet.DISCDLGSTRUCTA_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetDisconnectDialog1W(lpConnDlgStruct: POINTER(win32more.NetworkManagement.WNet.DISCDLGSTRUCTW_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetOpenEnumA(dwScope: win32more.NetworkManagement.WNet.NET_RESOURCE_SCOPE, dwType: win32more.NetworkManagement.WNet.NET_RESOURCE_TYPE, dwUsage: win32more.NetworkManagement.WNet.WNET_OPEN_ENUM_USAGE, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head), lphEnum: POINTER(win32more.NetworkManagement.WNet.NetEnumHandle)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetOpenEnumW(dwScope: win32more.NetworkManagement.WNet.NET_RESOURCE_SCOPE, dwType: win32more.NetworkManagement.WNet.NET_RESOURCE_TYPE, dwUsage: win32more.NetworkManagement.WNet.WNET_OPEN_ENUM_USAGE, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lphEnum: POINTER(win32more.NetworkManagement.WNet.NetEnumHandle)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetEnumResourceA(hEnum: win32more.Foundation.HANDLE, lpcCount: POINTER(UInt32), lpBuffer: c_void_p, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetEnumResourceW(hEnum: win32more.Foundation.HANDLE, lpcCount: POINTER(UInt32), lpBuffer: c_void_p, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetCloseEnum(hEnum: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetResourceParentA(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head), lpBuffer: c_void_p, lpcbBuffer: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetResourceParentW(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: c_void_p, lpcbBuffer: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetResourceInformationA(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head), lpBuffer: c_void_p, lpcbBuffer: POINTER(UInt32), lplpSystem: POINTER(win32more.Foundation.PSTR)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetResourceInformationW(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: c_void_p, lpcbBuffer: POINTER(UInt32), lplpSystem: POINTER(win32more.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetUniversalNameA(lpLocalPath: win32more.Foundation.PSTR, dwInfoLevel: win32more.NetworkManagement.WNet.UNC_INFO_LEVEL, lpBuffer: c_void_p, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetUniversalNameW(lpLocalPath: win32more.Foundation.PWSTR, dwInfoLevel: win32more.NetworkManagement.WNet.UNC_INFO_LEVEL, lpBuffer: c_void_p, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetUserA(lpName: win32more.Foundation.PSTR, lpUserName: win32more.Foundation.PSTR, lpnLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetUserW(lpName: win32more.Foundation.PWSTR, lpUserName: win32more.Foundation.PWSTR, lpnLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetProviderNameA(dwNetType: UInt32, lpProviderName: win32more.Foundation.PSTR, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetProviderNameW(dwNetType: UInt32, lpProviderName: win32more.Foundation.PWSTR, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetNetworkInformationA(lpProvider: win32more.Foundation.PSTR, lpNetInfoStruct: POINTER(win32more.NetworkManagement.WNet.NETINFOSTRUCT_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetNetworkInformationW(lpProvider: win32more.Foundation.PWSTR, lpNetInfoStruct: POINTER(win32more.NetworkManagement.WNet.NETINFOSTRUCT_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetLastErrorA(lpError: POINTER(UInt32), lpErrorBuf: win32more.Foundation.PSTR, nErrorBufSize: UInt32, lpNameBuf: win32more.Foundation.PSTR, nNameBufSize: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetLastErrorW(lpError: POINTER(UInt32), lpErrorBuf: win32more.Foundation.PWSTR, nErrorBufSize: UInt32, lpNameBuf: win32more.Foundation.PWSTR, nNameBufSize: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def MultinetGetConnectionPerformanceA(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head), lpNetConnectInfoStruct: POINTER(win32more.NetworkManagement.WNet.NETCONNECTINFOSTRUCT_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def MultinetGetConnectionPerformanceW(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpNetConnectInfoStruct: POINTER(win32more.NetworkManagement.WNet.NETCONNECTINFOSTRUCT_head)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPAddConnection(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: win32more.Foundation.PWSTR, lpUserName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPAddConnection3(hwndOwner: win32more.Foundation.HWND, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: win32more.Foundation.PWSTR, lpUserName: win32more.Foundation.PWSTR, dwFlags: win32more.NetworkManagement.WNet.NET_USE_CONNECT_FLAGS) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPAddConnection4(hwndOwner: win32more.Foundation.HWND, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpAuthBuffer: c_void_p, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: c_char_p_no, cbUseOptions: UInt32) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPCancelConnection(lpName: win32more.Foundation.PWSTR, fForce: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPCancelConnection2(lpName: win32more.Foundation.PWSTR, fForce: win32more.Foundation.BOOL, dwFlags: UInt32) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetConnection(lpLocalName: win32more.Foundation.PWSTR, lpRemoteName: win32more.Foundation.PWSTR, lpnBufferLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPGetConnection3(lpLocalName: win32more.Foundation.PWSTR, dwLevel: UInt32, lpBuffer: c_void_p, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetUniversalName(lpLocalPath: win32more.Foundation.PWSTR, dwInfoLevel: win32more.NetworkManagement.WNet.UNC_INFO_LEVEL, lpBuffer: c_void_p, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPGetConnectionPerformance(lpRemoteName: win32more.Foundation.PWSTR, lpNetConnectInfo: POINTER(win32more.NetworkManagement.WNet.NETCONNECTINFOSTRUCT_head)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPOpenEnum(dwScope: UInt32, dwType: UInt32, dwUsage: UInt32, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lphEnum: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPEnumResource(hEnum: win32more.Foundation.HANDLE, lpcCount: POINTER(UInt32), lpBuffer: c_void_p, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPCloseEnum(hEnum: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetCaps(ndex: UInt32) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetUser(lpName: win32more.Foundation.PWSTR, lpUserName: win32more.Foundation.PWSTR, lpnBufferLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPGetPersistentUseOptionsForConnection(lpRemotePath: win32more.Foundation.PWSTR, lpReadUseOptions: c_char_p_no, cbReadUseOptions: UInt32, lpWriteUseOptions: c_char_p_no, lpSizeWriteUseOptions: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetResourceParent(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: c_void_p, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetResourceInformation(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: c_void_p, lpBufferSize: POINTER(UInt32), lplpSystem: POINTER(win32more.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPFormatNetworkName(lpRemoteName: win32more.Foundation.PWSTR, lpFormattedName: win32more.Foundation.PWSTR, lpnLength: POINTER(UInt32), dwFlags: win32more.NetworkManagement.WNet.NETWORK_NAME_FORMAT_FLAGS, dwAveCharPerLine: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetSetLastErrorA(err: UInt32, lpError: win32more.Foundation.PSTR, lpProviders: win32more.Foundation.PSTR) -> Void: ...
@winfunctype('MPR.dll')
def WNetSetLastErrorW(err: UInt32, lpError: win32more.Foundation.PWSTR, lpProviders: win32more.Foundation.PWSTR) -> Void: ...
CONNECTDLGSTRUCT_FLAGS = UInt32
CONNDLG_RO_PATH: CONNECTDLGSTRUCT_FLAGS = 1
CONNDLG_CONN_POINT: CONNECTDLGSTRUCT_FLAGS = 2
CONNDLG_USE_MRU: CONNECTDLGSTRUCT_FLAGS = 4
CONNDLG_HIDE_BOX: CONNECTDLGSTRUCT_FLAGS = 8
CONNDLG_PERSIST: CONNECTDLGSTRUCT_FLAGS = 16
CONNDLG_NOT_PERSIST: CONNECTDLGSTRUCT_FLAGS = 32
class CONNECTDLGSTRUCTA(Structure):
    cbStructure: UInt32
    hwndOwner: win32more.Foundation.HWND
    lpConnRes: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEA_head)
    dwFlags: win32more.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS
    dwDevNum: UInt32
class CONNECTDLGSTRUCTW(Structure):
    cbStructure: UInt32
    hwndOwner: win32more.Foundation.HWND
    lpConnRes: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head)
    dwFlags: win32more.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS
    dwDevNum: UInt32
DISCDLGSTRUCT_FLAGS = UInt32
DISC_UPDATE_PROFILE: DISCDLGSTRUCT_FLAGS = 1
DISC_NO_FORCE: DISCDLGSTRUCT_FLAGS = 64
class DISCDLGSTRUCTA(Structure):
    cbStructure: UInt32
    hwndOwner: win32more.Foundation.HWND
    lpLocalName: win32more.Foundation.PSTR
    lpRemoteName: win32more.Foundation.PSTR
    dwFlags: win32more.NetworkManagement.WNet.DISCDLGSTRUCT_FLAGS
class DISCDLGSTRUCTW(Structure):
    cbStructure: UInt32
    hwndOwner: win32more.Foundation.HWND
    lpLocalName: win32more.Foundation.PWSTR
    lpRemoteName: win32more.Foundation.PWSTR
    dwFlags: win32more.NetworkManagement.WNet.DISCDLGSTRUCT_FLAGS
NET_RESOURCE_SCOPE = UInt32
RESOURCE_CONNECTED: NET_RESOURCE_SCOPE = 1
RESOURCE_CONTEXT: NET_RESOURCE_SCOPE = 5
RESOURCE_GLOBALNET: NET_RESOURCE_SCOPE = 2
RESOURCE_REMEMBERED: NET_RESOURCE_SCOPE = 3
NET_RESOURCE_TYPE = UInt32
RESOURCETYPE_ANY: NET_RESOURCE_TYPE = 0
RESOURCETYPE_DISK: NET_RESOURCE_TYPE = 1
RESOURCETYPE_PRINT: NET_RESOURCE_TYPE = 2
NET_USE_CONNECT_FLAGS = UInt32
CONNECT_INTERACTIVE: NET_USE_CONNECT_FLAGS = 8
CONNECT_PROMPT: NET_USE_CONNECT_FLAGS = 16
CONNECT_REDIRECT: NET_USE_CONNECT_FLAGS = 128
CONNECT_UPDATE_PROFILE: NET_USE_CONNECT_FLAGS = 1
CONNECT_COMMANDLINE: NET_USE_CONNECT_FLAGS = 2048
CONNECT_CMD_SAVECRED: NET_USE_CONNECT_FLAGS = 4096
CONNECT_TEMPORARY: NET_USE_CONNECT_FLAGS = 4
CONNECT_DEFERRED: NET_USE_CONNECT_FLAGS = 1024
CONNECT_UPDATE_RECENT: NET_USE_CONNECT_FLAGS = 2
class NETCONNECTINFOSTRUCT(Structure):
    cbStructure: UInt32
    dwFlags: UInt32
    dwSpeed: UInt32
    dwDelay: UInt32
    dwOptDataSize: UInt32
NetEnumHandle = IntPtr
class NETINFOSTRUCT(Structure):
    cbStructure: UInt32
    dwProviderVersion: UInt32
    dwStatus: win32more.Foundation.WIN32_ERROR
    dwCharacteristics: win32more.NetworkManagement.WNet.NETINFOSTRUCT_CHARACTERISTICS
    dwHandle: UIntPtr
    wNetType: UInt16
    dwPrinters: UInt32
    dwDrives: UInt32
NETINFOSTRUCT_CHARACTERISTICS = UInt32
NETINFO_DLL16: NETINFOSTRUCT_CHARACTERISTICS = 1
NETINFO_DISKRED: NETINFOSTRUCT_CHARACTERISTICS = 4
NETINFO_PRINTERRED: NETINFOSTRUCT_CHARACTERISTICS = 8
class NETRESOURCEA(Structure):
    dwScope: win32more.NetworkManagement.WNet.NET_RESOURCE_SCOPE
    dwType: win32more.NetworkManagement.WNet.NET_RESOURCE_TYPE
    dwDisplayType: UInt32
    dwUsage: UInt32
    lpLocalName: win32more.Foundation.PSTR
    lpRemoteName: win32more.Foundation.PSTR
    lpComment: win32more.Foundation.PSTR
    lpProvider: win32more.Foundation.PSTR
class NETRESOURCEW(Structure):
    dwScope: win32more.NetworkManagement.WNet.NET_RESOURCE_SCOPE
    dwType: win32more.NetworkManagement.WNet.NET_RESOURCE_TYPE
    dwDisplayType: UInt32
    dwUsage: UInt32
    lpLocalName: win32more.Foundation.PWSTR
    lpRemoteName: win32more.Foundation.PWSTR
    lpComment: win32more.Foundation.PWSTR
    lpProvider: win32more.Foundation.PWSTR
NETWORK_NAME_FORMAT_FLAGS = UInt32
WNFMT_MULTILINE: NETWORK_NAME_FORMAT_FLAGS = 1
WNFMT_ABBREVIATED: NETWORK_NAME_FORMAT_FLAGS = 2
class NOTIFYADD(Structure):
    hwndOwner: win32more.Foundation.HWND
    NetResource: win32more.NetworkManagement.WNet.NETRESOURCEA
    dwAddFlags: win32more.NetworkManagement.WNet.NET_USE_CONNECT_FLAGS
class NOTIFYCANCEL(Structure):
    lpName: win32more.Foundation.PWSTR
    lpProvider: win32more.Foundation.PWSTR
    dwFlags: UInt32
    fForce: win32more.Foundation.BOOL
class NOTIFYINFO(Structure):
    dwNotifyStatus: UInt32
    dwOperationStatus: UInt32
    lpContext: c_void_p
NP_PROPERTY_DIALOG_SELECTION = UInt32
WNPS_FILE: NP_PROPERTY_DIALOG_SELECTION = 0
WNPS_DIR: NP_PROPERTY_DIALOG_SELECTION = 1
WNPS_MULT: NP_PROPERTY_DIALOG_SELECTION = 2
NPDIRECTORY_NOTIFY_OPERATION = UInt32
WNDN_MKDIR: NPDIRECTORY_NOTIFY_OPERATION = 1
WNDN_RMDIR: NPDIRECTORY_NOTIFY_OPERATION = 2
WNDN_MVDIR: NPDIRECTORY_NOTIFY_OPERATION = 3
@winfunctype_pointer
def PF_AddConnectNotify(lpNotifyInfo: POINTER(win32more.NetworkManagement.WNet.NOTIFYINFO_head), lpAddInfo: POINTER(win32more.NetworkManagement.WNet.NOTIFYADD_head)) -> UInt32: ...
@winfunctype_pointer
def PF_CancelConnectNotify(lpNotifyInfo: POINTER(win32more.NetworkManagement.WNet.NOTIFYINFO_head), lpCancelInfo: POINTER(win32more.NetworkManagement.WNet.NOTIFYCANCEL_head)) -> UInt32: ...
@winfunctype_pointer
def PF_NPAddConnection(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: win32more.Foundation.PWSTR, lpUserName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def PF_NPAddConnection3(hwndOwner: win32more.Foundation.HWND, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: win32more.Foundation.PWSTR, lpUserName: win32more.Foundation.PWSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPAddConnection4(hwndOwner: win32more.Foundation.HWND, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpAuthBuffer: c_void_p, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: c_char_p_no, cbUseOptions: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPCancelConnection(lpName: win32more.Foundation.PWSTR, fForce: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype_pointer
def PF_NPCancelConnection2(lpName: win32more.Foundation.PWSTR, fForce: win32more.Foundation.BOOL, dwFlags: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPCloseEnum(hEnum: win32more.Foundation.HANDLE) -> UInt32: ...
@winfunctype_pointer
def PF_NPDeviceMode(hParent: win32more.Foundation.HWND) -> UInt32: ...
@winfunctype_pointer
def PF_NPDirectoryNotify(hwnd: win32more.Foundation.HWND, lpDir: win32more.Foundation.PWSTR, dwOper: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPEnumResource(hEnum: win32more.Foundation.HANDLE, lpcCount: POINTER(UInt32), lpBuffer: c_void_p, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPFMXEditPerm(lpDriveName: win32more.Foundation.PWSTR, hwndFMX: win32more.Foundation.HWND, nDialogType: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPFMXGetPermCaps(lpDriveName: win32more.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def PF_NPFMXGetPermHelp(lpDriveName: win32more.Foundation.PWSTR, nDialogType: UInt32, fDirectory: win32more.Foundation.BOOL, lpFileNameBuffer: c_void_p, lpBufferSize: POINTER(UInt32), lpnHelpContext: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPFormatNetworkName(lpRemoteName: win32more.Foundation.PWSTR, lpFormattedName: win32more.Foundation.PWSTR, lpnLength: POINTER(UInt32), dwFlags: UInt32, dwAveCharPerLine: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetCaps(ndex: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetConnection(lpLocalName: win32more.Foundation.PWSTR, lpRemoteName: win32more.Foundation.PWSTR, lpnBufferLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetConnection3(lpLocalName: win32more.Foundation.PWSTR, dwLevel: UInt32, lpBuffer: c_void_p, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetConnectionPerformance(lpRemoteName: win32more.Foundation.PWSTR, lpNetConnectInfo: POINTER(win32more.NetworkManagement.WNet.NETCONNECTINFOSTRUCT_head)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetDirectoryType(lpName: win32more.Foundation.PWSTR, lpType: POINTER(Int32), bFlushCache: win32more.Foundation.BOOL) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetPersistentUseOptionsForConnection(lpRemotePath: win32more.Foundation.PWSTR, lpReadUseOptions: c_char_p_no, cbReadUseOptions: UInt32, lpWriteUseOptions: c_char_p_no, lpSizeWriteUseOptions: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetPropertyText(iButton: UInt32, nPropSel: UInt32, lpName: win32more.Foundation.PWSTR, lpButtonName: win32more.Foundation.PWSTR, nButtonNameLen: UInt32, nType: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetResourceInformation(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: c_void_p, lpBufferSize: POINTER(UInt32), lplpSystem: POINTER(win32more.Foundation.PWSTR)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetResourceParent(lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: c_void_p, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetUniversalName(lpLocalPath: win32more.Foundation.PWSTR, dwInfoLevel: UInt32, lpBuffer: c_void_p, lpnBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetUser(lpName: win32more.Foundation.PWSTR, lpUserName: win32more.Foundation.PWSTR, lpnBufferLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPLogonNotify(lpLogonId: POINTER(win32more.Foundation.LUID_head), lpAuthentInfoType: win32more.Foundation.PWSTR, lpAuthentInfo: c_void_p, lpPreviousAuthentInfoType: win32more.Foundation.PWSTR, lpPreviousAuthentInfo: c_void_p, lpStationName: win32more.Foundation.PWSTR, StationHandle: c_void_p, lpLogonScript: POINTER(win32more.Foundation.PWSTR)) -> UInt32: ...
@winfunctype_pointer
def PF_NPOpenEnum(dwScope: UInt32, dwType: UInt32, dwUsage: UInt32, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lphEnum: POINTER(win32more.Foundation.HANDLE)) -> UInt32: ...
@winfunctype_pointer
def PF_NPPasswordChangeNotify(lpAuthentInfoType: win32more.Foundation.PWSTR, lpAuthentInfo: c_void_p, lpPreviousAuthentInfoType: win32more.Foundation.PWSTR, lpPreviousAuthentInfo: c_void_p, lpStationName: win32more.Foundation.PWSTR, StationHandle: c_void_p, dwChangeInfo: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPPropertyDialog(hwndParent: win32more.Foundation.HWND, iButtonDlg: UInt32, nPropSel: UInt32, lpFileName: win32more.Foundation.PWSTR, nType: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPSearchDialog(hwndParent: win32more.Foundation.HWND, lpNetResource: POINTER(win32more.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: c_void_p, cbBuffer: UInt32, lpnFlags: POINTER(UInt32)) -> UInt32: ...
class REMOTE_NAME_INFOA(Structure):
    lpUniversalName: win32more.Foundation.PSTR
    lpConnectionName: win32more.Foundation.PSTR
    lpRemainingPath: win32more.Foundation.PSTR
class REMOTE_NAME_INFOW(Structure):
    lpUniversalName: win32more.Foundation.PWSTR
    lpConnectionName: win32more.Foundation.PWSTR
    lpRemainingPath: win32more.Foundation.PWSTR
UNC_INFO_LEVEL = UInt32
UNIVERSAL_NAME_INFO_LEVEL: UNC_INFO_LEVEL = 1
REMOTE_NAME_INFO_LEVEL: UNC_INFO_LEVEL = 2
class UNIVERSAL_NAME_INFOA(Structure):
    lpUniversalName: win32more.Foundation.PSTR
class UNIVERSAL_NAME_INFOW(Structure):
    lpUniversalName: win32more.Foundation.PWSTR
WNET_OPEN_ENUM_USAGE = UInt32
RESOURCEUSAGE_NONE: WNET_OPEN_ENUM_USAGE = 0
RESOURCEUSAGE_CONNECTABLE: WNET_OPEN_ENUM_USAGE = 1
RESOURCEUSAGE_CONTAINER: WNET_OPEN_ENUM_USAGE = 2
RESOURCEUSAGE_ATTACHED: WNET_OPEN_ENUM_USAGE = 16
RESOURCEUSAGE_ALL: WNET_OPEN_ENUM_USAGE = 19
WNPERM_DLG = UInt32
WNPERM_DLG_PERM: WNPERM_DLG = 0
WNPERM_DLG_AUDIT: WNPERM_DLG = 1
WNPERM_DLG_OWNER: WNPERM_DLG = 2
make_head(_module, 'CONNECTDLGSTRUCTA')
make_head(_module, 'CONNECTDLGSTRUCTW')
make_head(_module, 'DISCDLGSTRUCTA')
make_head(_module, 'DISCDLGSTRUCTW')
make_head(_module, 'NETCONNECTINFOSTRUCT')
make_head(_module, 'NETINFOSTRUCT')
make_head(_module, 'NETRESOURCEA')
make_head(_module, 'NETRESOURCEW')
make_head(_module, 'NOTIFYADD')
make_head(_module, 'NOTIFYCANCEL')
make_head(_module, 'NOTIFYINFO')
make_head(_module, 'PF_AddConnectNotify')
make_head(_module, 'PF_CancelConnectNotify')
make_head(_module, 'PF_NPAddConnection')
make_head(_module, 'PF_NPAddConnection3')
make_head(_module, 'PF_NPAddConnection4')
make_head(_module, 'PF_NPCancelConnection')
make_head(_module, 'PF_NPCancelConnection2')
make_head(_module, 'PF_NPCloseEnum')
make_head(_module, 'PF_NPDeviceMode')
make_head(_module, 'PF_NPDirectoryNotify')
make_head(_module, 'PF_NPEnumResource')
make_head(_module, 'PF_NPFMXEditPerm')
make_head(_module, 'PF_NPFMXGetPermCaps')
make_head(_module, 'PF_NPFMXGetPermHelp')
make_head(_module, 'PF_NPFormatNetworkName')
make_head(_module, 'PF_NPGetCaps')
make_head(_module, 'PF_NPGetConnection')
make_head(_module, 'PF_NPGetConnection3')
make_head(_module, 'PF_NPGetConnectionPerformance')
make_head(_module, 'PF_NPGetDirectoryType')
make_head(_module, 'PF_NPGetPersistentUseOptionsForConnection')
make_head(_module, 'PF_NPGetPropertyText')
make_head(_module, 'PF_NPGetResourceInformation')
make_head(_module, 'PF_NPGetResourceParent')
make_head(_module, 'PF_NPGetUniversalName')
make_head(_module, 'PF_NPGetUser')
make_head(_module, 'PF_NPLogonNotify')
make_head(_module, 'PF_NPOpenEnum')
make_head(_module, 'PF_NPPasswordChangeNotify')
make_head(_module, 'PF_NPPropertyDialog')
make_head(_module, 'PF_NPSearchDialog')
make_head(_module, 'REMOTE_NAME_INFOA')
make_head(_module, 'REMOTE_NAME_INFOW')
make_head(_module, 'UNIVERSAL_NAME_INFOA')
make_head(_module, 'UNIVERSAL_NAME_INFOW')
__all__ = [
    "CONNDLG_CONN_POINT",
    "CONNDLG_HIDE_BOX",
    "CONNDLG_NOT_PERSIST",
    "CONNDLG_PERSIST",
    "CONNDLG_RO_PATH",
    "CONNDLG_USE_MRU",
    "CONNECTDLGSTRUCTA",
    "CONNECTDLGSTRUCTW",
    "CONNECTDLGSTRUCT_FLAGS",
    "CONNECT_CMD_SAVECRED",
    "CONNECT_COMMANDLINE",
    "CONNECT_CRED_RESET",
    "CONNECT_CURRENT_MEDIA",
    "CONNECT_DEFERRED",
    "CONNECT_GLOBAL_MAPPING",
    "CONNECT_INTERACTIVE",
    "CONNECT_LOCALDRIVE",
    "CONNECT_NEED_DRIVE",
    "CONNECT_PROMPT",
    "CONNECT_REDIRECT",
    "CONNECT_REFCOUNT",
    "CONNECT_REQUIRE_INTEGRITY",
    "CONNECT_REQUIRE_PRIVACY",
    "CONNECT_RESERVED",
    "CONNECT_TEMPORARY",
    "CONNECT_UPDATE_PROFILE",
    "CONNECT_UPDATE_RECENT",
    "CONNECT_WRITE_THROUGH_SEMANTICS",
    "DISCDLGSTRUCTA",
    "DISCDLGSTRUCTW",
    "DISCDLGSTRUCT_FLAGS",
    "DISC_NO_FORCE",
    "DISC_UPDATE_PROFILE",
    "MultinetGetConnectionPerformanceA",
    "MultinetGetConnectionPerformanceW",
    "NETCONNECTINFOSTRUCT",
    "NETINFOSTRUCT",
    "NETINFOSTRUCT_CHARACTERISTICS",
    "NETINFO_DISKRED",
    "NETINFO_DLL16",
    "NETINFO_PRINTERRED",
    "NETPROPERTY_PERSISTENT",
    "NETRESOURCEA",
    "NETRESOURCEW",
    "NETWORK_NAME_FORMAT_FLAGS",
    "NET_RESOURCE_SCOPE",
    "NET_RESOURCE_TYPE",
    "NET_USE_CONNECT_FLAGS",
    "NOTIFYADD",
    "NOTIFYCANCEL",
    "NOTIFYINFO",
    "NOTIFY_POST",
    "NOTIFY_PRE",
    "NPAddConnection",
    "NPAddConnection3",
    "NPAddConnection4",
    "NPCancelConnection",
    "NPCancelConnection2",
    "NPCloseEnum",
    "NPDIRECTORY_NOTIFY_OPERATION",
    "NPEnumResource",
    "NPFormatNetworkName",
    "NPGetCaps",
    "NPGetConnection",
    "NPGetConnection3",
    "NPGetConnectionPerformance",
    "NPGetPersistentUseOptionsForConnection",
    "NPGetResourceInformation",
    "NPGetResourceParent",
    "NPGetUniversalName",
    "NPGetUser",
    "NPOpenEnum",
    "NP_PROPERTY_DIALOG_SELECTION",
    "NetEnumHandle",
    "PF_AddConnectNotify",
    "PF_CancelConnectNotify",
    "PF_NPAddConnection",
    "PF_NPAddConnection3",
    "PF_NPAddConnection4",
    "PF_NPCancelConnection",
    "PF_NPCancelConnection2",
    "PF_NPCloseEnum",
    "PF_NPDeviceMode",
    "PF_NPDirectoryNotify",
    "PF_NPEnumResource",
    "PF_NPFMXEditPerm",
    "PF_NPFMXGetPermCaps",
    "PF_NPFMXGetPermHelp",
    "PF_NPFormatNetworkName",
    "PF_NPGetCaps",
    "PF_NPGetConnection",
    "PF_NPGetConnection3",
    "PF_NPGetConnectionPerformance",
    "PF_NPGetDirectoryType",
    "PF_NPGetPersistentUseOptionsForConnection",
    "PF_NPGetPropertyText",
    "PF_NPGetResourceInformation",
    "PF_NPGetResourceParent",
    "PF_NPGetUniversalName",
    "PF_NPGetUser",
    "PF_NPLogonNotify",
    "PF_NPOpenEnum",
    "PF_NPPasswordChangeNotify",
    "PF_NPPropertyDialog",
    "PF_NPSearchDialog",
    "REMOTE_NAME_INFOA",
    "REMOTE_NAME_INFOW",
    "REMOTE_NAME_INFO_LEVEL",
    "RESOURCEDISPLAYTYPE_DIRECTORY",
    "RESOURCEDISPLAYTYPE_NDSCONTAINER",
    "RESOURCEDISPLAYTYPE_NETWORK",
    "RESOURCEDISPLAYTYPE_ROOT",
    "RESOURCEDISPLAYTYPE_SHAREADMIN",
    "RESOURCETYPE_ANY",
    "RESOURCETYPE_DISK",
    "RESOURCETYPE_PRINT",
    "RESOURCETYPE_RESERVED",
    "RESOURCETYPE_UNKNOWN",
    "RESOURCEUSAGE_ALL",
    "RESOURCEUSAGE_ATTACHED",
    "RESOURCEUSAGE_CONNECTABLE",
    "RESOURCEUSAGE_CONTAINER",
    "RESOURCEUSAGE_NOLOCALDEVICE",
    "RESOURCEUSAGE_NONE",
    "RESOURCEUSAGE_RESERVED",
    "RESOURCEUSAGE_SIBLING",
    "RESOURCE_CONNECTED",
    "RESOURCE_CONTEXT",
    "RESOURCE_GLOBALNET",
    "RESOURCE_RECENT",
    "RESOURCE_REMEMBERED",
    "UNC_INFO_LEVEL",
    "UNIVERSAL_NAME_INFOA",
    "UNIVERSAL_NAME_INFOW",
    "UNIVERSAL_NAME_INFO_LEVEL",
    "WNCON_DYNAMIC",
    "WNCON_FORNETCARD",
    "WNCON_NOTROUTED",
    "WNCON_SLOWLINK",
    "WNDN_MKDIR",
    "WNDN_MVDIR",
    "WNDN_RMDIR",
    "WNDT_NETWORK",
    "WNDT_NORMAL",
    "WNET_OPEN_ENUM_USAGE",
    "WNFMT_ABBREVIATED",
    "WNFMT_CONNECTION",
    "WNFMT_INENUM",
    "WNFMT_MULTILINE",
    "WNGETCON_CONNECTED",
    "WNGETCON_DISCONNECTED",
    "WNNC_ADMIN",
    "WNNC_ADM_DIRECTORYNOTIFY",
    "WNNC_ADM_GETDIRECTORYTYPE",
    "WNNC_CONNECTION",
    "WNNC_CONNECTION_FLAGS",
    "WNNC_CON_ADDCONNECTION",
    "WNNC_CON_ADDCONNECTION3",
    "WNNC_CON_ADDCONNECTION4",
    "WNNC_CON_CANCELCONNECTION",
    "WNNC_CON_CANCELCONNECTION2",
    "WNNC_CON_DEFER",
    "WNNC_CON_GETCONNECTIONS",
    "WNNC_CON_GETPERFORMANCE",
    "WNNC_DIALOG",
    "WNNC_DLG_DEVICEMODE",
    "WNNC_DLG_FORMATNETWORKNAME",
    "WNNC_DLG_GETRESOURCEINFORMATION",
    "WNNC_DLG_GETRESOURCEPARENT",
    "WNNC_DLG_PERMISSIONEDITOR",
    "WNNC_DLG_PROPERTYDIALOG",
    "WNNC_DLG_SEARCHDIALOG",
    "WNNC_DRIVER_VERSION",
    "WNNC_ENUMERATION",
    "WNNC_ENUM_CONTEXT",
    "WNNC_ENUM_GLOBAL",
    "WNNC_ENUM_LOCAL",
    "WNNC_ENUM_SHAREABLE",
    "WNNC_NET_NONE",
    "WNNC_NET_TYPE",
    "WNNC_SPEC_VERSION",
    "WNNC_SPEC_VERSION51",
    "WNNC_START",
    "WNNC_USER",
    "WNNC_USR_GETUSER",
    "WNNC_WAIT_FOR_START",
    "WNPERMC_AUDIT",
    "WNPERMC_OWNER",
    "WNPERMC_PERM",
    "WNPERM_DLG",
    "WNPERM_DLG_AUDIT",
    "WNPERM_DLG_OWNER",
    "WNPERM_DLG_PERM",
    "WNPS_DIR",
    "WNPS_FILE",
    "WNPS_MULT",
    "WNSRCH_REFRESH_FIRST_LEVEL",
    "WNTYPE_COMM",
    "WNTYPE_DRIVE",
    "WNTYPE_FILE",
    "WNTYPE_PRINTER",
    "WN_CREDENTIAL_CLASS",
    "WN_NETWORK_CLASS",
    "WN_NT_PASSWORD_CHANGED",
    "WN_PRIMARY_AUTHENT_CLASS",
    "WN_SERVICE_CLASS",
    "WN_VALID_LOGON_ACCOUNT",
    "WNetAddConnection2A",
    "WNetAddConnection2W",
    "WNetAddConnection3A",
    "WNetAddConnection3W",
    "WNetAddConnection4A",
    "WNetAddConnection4W",
    "WNetAddConnectionA",
    "WNetAddConnectionW",
    "WNetCancelConnection2A",
    "WNetCancelConnection2W",
    "WNetCancelConnectionA",
    "WNetCancelConnectionW",
    "WNetCloseEnum",
    "WNetConnectionDialog",
    "WNetConnectionDialog1A",
    "WNetConnectionDialog1W",
    "WNetDisconnectDialog",
    "WNetDisconnectDialog1A",
    "WNetDisconnectDialog1W",
    "WNetEnumResourceA",
    "WNetEnumResourceW",
    "WNetGetConnectionA",
    "WNetGetConnectionW",
    "WNetGetLastErrorA",
    "WNetGetLastErrorW",
    "WNetGetNetworkInformationA",
    "WNetGetNetworkInformationW",
    "WNetGetProviderNameA",
    "WNetGetProviderNameW",
    "WNetGetResourceInformationA",
    "WNetGetResourceInformationW",
    "WNetGetResourceParentA",
    "WNetGetResourceParentW",
    "WNetGetUniversalNameA",
    "WNetGetUniversalNameW",
    "WNetGetUserA",
    "WNetGetUserW",
    "WNetOpenEnumA",
    "WNetOpenEnumW",
    "WNetSetLastErrorA",
    "WNetSetLastErrorW",
    "WNetUseConnection4A",
    "WNetUseConnection4W",
    "WNetUseConnectionA",
    "WNetUseConnectionW",
]
_arch_optional = [
]
