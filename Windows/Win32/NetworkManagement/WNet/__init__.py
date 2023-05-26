from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.WNet
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
def WNetAddConnectionA(lpRemoteName: Windows.Win32.Foundation.PSTR, lpPassword: Windows.Win32.Foundation.PSTR, lpLocalName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnectionW(lpRemoteName: Windows.Win32.Foundation.PWSTR, lpPassword: Windows.Win32.Foundation.PWSTR, lpLocalName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnection2A(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEA_head), lpPassword: Windows.Win32.Foundation.PSTR, lpUserName: Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnection2W(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: Windows.Win32.Foundation.PWSTR, lpUserName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnection3A(hwndOwner: Windows.Win32.Foundation.HWND, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEA_head), lpPassword: Windows.Win32.Foundation.PSTR, lpUserName: Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnection3W(hwndOwner: Windows.Win32.Foundation.HWND, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: Windows.Win32.Foundation.PWSTR, lpUserName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnection4A(hwndOwner: Windows.Win32.Foundation.HWND, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEA_head), pAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: POINTER(Byte), cbUseOptions: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetAddConnection4W(hwndOwner: Windows.Win32.Foundation.HWND, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), pAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: POINTER(Byte), cbUseOptions: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetCancelConnectionA(lpName: Windows.Win32.Foundation.PSTR, fForce: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetCancelConnectionW(lpName: Windows.Win32.Foundation.PWSTR, fForce: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetCancelConnection2A(lpName: Windows.Win32.Foundation.PSTR, dwFlags: UInt32, fForce: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetCancelConnection2W(lpName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, fForce: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetConnectionA(lpLocalName: Windows.Win32.Foundation.PSTR, lpRemoteName: Windows.Win32.Foundation.PSTR, lpnLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetConnectionW(lpLocalName: Windows.Win32.Foundation.PWSTR, lpRemoteName: Windows.Win32.Foundation.PWSTR, lpnLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetUseConnectionA(hwndOwner: Windows.Win32.Foundation.HWND, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEA_head), lpPassword: Windows.Win32.Foundation.PSTR, lpUserId: Windows.Win32.Foundation.PSTR, dwFlags: Windows.Win32.NetworkManagement.WNet.NET_USE_CONNECT_FLAGS, lpAccessName: Windows.Win32.Foundation.PSTR, lpBufferSize: POINTER(UInt32), lpResult: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetUseConnectionW(hwndOwner: Windows.Win32.Foundation.HWND, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: Windows.Win32.Foundation.PWSTR, lpUserId: Windows.Win32.Foundation.PWSTR, dwFlags: Windows.Win32.NetworkManagement.WNet.NET_USE_CONNECT_FLAGS, lpAccessName: Windows.Win32.Foundation.PWSTR, lpBufferSize: POINTER(UInt32), lpResult: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetUseConnection4A(hwndOwner: Windows.Win32.Foundation.HWND, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEA_head), pAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: POINTER(Byte), cbUseOptions: UInt32, lpAccessName: Windows.Win32.Foundation.PSTR, lpBufferSize: POINTER(UInt32), lpResult: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetUseConnection4W(hwndOwner: Windows.Win32.Foundation.HWND, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), pAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: POINTER(Byte), cbUseOptions: UInt32, lpAccessName: Windows.Win32.Foundation.PWSTR, lpBufferSize: POINTER(UInt32), lpResult: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetConnectionDialog(hwnd: Windows.Win32.Foundation.HWND, dwType: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetDisconnectDialog(hwnd: Windows.Win32.Foundation.HWND, dwType: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetConnectionDialog1A(lpConnDlgStruct: POINTER(Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCTA_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetConnectionDialog1W(lpConnDlgStruct: POINTER(Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCTW_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetDisconnectDialog1A(lpConnDlgStruct: POINTER(Windows.Win32.NetworkManagement.WNet.DISCDLGSTRUCTA_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetDisconnectDialog1W(lpConnDlgStruct: POINTER(Windows.Win32.NetworkManagement.WNet.DISCDLGSTRUCTW_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetOpenEnumA(dwScope: Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_SCOPE, dwType: Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_TYPE, dwUsage: Windows.Win32.NetworkManagement.WNet.WNET_OPEN_ENUM_USAGE, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEA_head), lphEnum: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetOpenEnumW(dwScope: Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_SCOPE, dwType: Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_TYPE, dwUsage: Windows.Win32.NetworkManagement.WNet.WNET_OPEN_ENUM_USAGE, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lphEnum: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetEnumResourceA(hEnum: Windows.Win32.Foundation.HANDLE, lpcCount: POINTER(UInt32), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetEnumResourceW(hEnum: Windows.Win32.Foundation.HANDLE, lpcCount: POINTER(UInt32), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetCloseEnum(hEnum: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetResourceParentA(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEA_head), lpBuffer: VoidPtr, lpcbBuffer: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetResourceParentW(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: VoidPtr, lpcbBuffer: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetResourceInformationA(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEA_head), lpBuffer: VoidPtr, lpcbBuffer: POINTER(UInt32), lplpSystem: POINTER(Windows.Win32.Foundation.PSTR)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetResourceInformationW(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: VoidPtr, lpcbBuffer: POINTER(UInt32), lplpSystem: POINTER(Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetUniversalNameA(lpLocalPath: Windows.Win32.Foundation.PSTR, dwInfoLevel: Windows.Win32.NetworkManagement.WNet.UNC_INFO_LEVEL, lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetUniversalNameW(lpLocalPath: Windows.Win32.Foundation.PWSTR, dwInfoLevel: Windows.Win32.NetworkManagement.WNet.UNC_INFO_LEVEL, lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetUserA(lpName: Windows.Win32.Foundation.PSTR, lpUserName: Windows.Win32.Foundation.PSTR, lpnLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetUserW(lpName: Windows.Win32.Foundation.PWSTR, lpUserName: Windows.Win32.Foundation.PWSTR, lpnLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetProviderNameA(dwNetType: UInt32, lpProviderName: Windows.Win32.Foundation.PSTR, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetProviderNameW(dwNetType: UInt32, lpProviderName: Windows.Win32.Foundation.PWSTR, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetNetworkInformationA(lpProvider: Windows.Win32.Foundation.PSTR, lpNetInfoStruct: POINTER(Windows.Win32.NetworkManagement.WNet.NETINFOSTRUCT_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetNetworkInformationW(lpProvider: Windows.Win32.Foundation.PWSTR, lpNetInfoStruct: POINTER(Windows.Win32.NetworkManagement.WNet.NETINFOSTRUCT_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetLastErrorA(lpError: POINTER(UInt32), lpErrorBuf: Windows.Win32.Foundation.PSTR, nErrorBufSize: UInt32, lpNameBuf: Windows.Win32.Foundation.PSTR, nNameBufSize: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetGetLastErrorW(lpError: POINTER(UInt32), lpErrorBuf: Windows.Win32.Foundation.PWSTR, nErrorBufSize: UInt32, lpNameBuf: Windows.Win32.Foundation.PWSTR, nNameBufSize: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def MultinetGetConnectionPerformanceA(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEA_head), lpNetConnectInfoStruct: POINTER(Windows.Win32.NetworkManagement.WNet.NETCONNECTINFOSTRUCT_head)) -> UInt32: ...
@winfunctype('MPR.dll')
def MultinetGetConnectionPerformanceW(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpNetConnectInfoStruct: POINTER(Windows.Win32.NetworkManagement.WNet.NETCONNECTINFOSTRUCT_head)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPAddConnection(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: Windows.Win32.Foundation.PWSTR, lpUserName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPAddConnection3(hwndOwner: Windows.Win32.Foundation.HWND, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: Windows.Win32.Foundation.PWSTR, lpUserName: Windows.Win32.Foundation.PWSTR, dwFlags: Windows.Win32.NetworkManagement.WNet.NET_USE_CONNECT_FLAGS) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPAddConnection4(hwndOwner: Windows.Win32.Foundation.HWND, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: POINTER(Byte), cbUseOptions: UInt32) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPCancelConnection(lpName: Windows.Win32.Foundation.PWSTR, fForce: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPCancelConnection2(lpName: Windows.Win32.Foundation.PWSTR, fForce: Windows.Win32.Foundation.BOOL, dwFlags: UInt32) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetConnection(lpLocalName: Windows.Win32.Foundation.PWSTR, lpRemoteName: Windows.Win32.Foundation.PWSTR, lpnBufferLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPGetConnection3(lpLocalName: Windows.Win32.Foundation.PWSTR, dwLevel: UInt32, lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetUniversalName(lpLocalPath: Windows.Win32.Foundation.PWSTR, dwInfoLevel: Windows.Win32.NetworkManagement.WNet.UNC_INFO_LEVEL, lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPGetConnectionPerformance(lpRemoteName: Windows.Win32.Foundation.PWSTR, lpNetConnectInfo: POINTER(Windows.Win32.NetworkManagement.WNet.NETCONNECTINFOSTRUCT_head)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPOpenEnum(dwScope: UInt32, dwType: UInt32, dwUsage: UInt32, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lphEnum: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPEnumResource(hEnum: Windows.Win32.Foundation.HANDLE, lpcCount: POINTER(UInt32), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPCloseEnum(hEnum: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetCaps(ndex: UInt32) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetUser(lpName: Windows.Win32.Foundation.PWSTR, lpUserName: Windows.Win32.Foundation.PWSTR, lpnBufferLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPGetPersistentUseOptionsForConnection(lpRemotePath: Windows.Win32.Foundation.PWSTR, lpReadUseOptions: POINTER(Byte), cbReadUseOptions: UInt32, lpWriteUseOptions: POINTER(Byte), lpSizeWriteUseOptions: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetResourceParent(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetResourceInformation(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32), lplpSystem: POINTER(Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPFormatNetworkName(lpRemoteName: Windows.Win32.Foundation.PWSTR, lpFormattedName: Windows.Win32.Foundation.PWSTR, lpnLength: POINTER(UInt32), dwFlags: Windows.Win32.NetworkManagement.WNet.NETWORK_NAME_FORMAT_FLAGS, dwAveCharPerLine: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetSetLastErrorA(err: UInt32, lpError: Windows.Win32.Foundation.PSTR, lpProviders: Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('MPR.dll')
def WNetSetLastErrorW(err: UInt32, lpError: Windows.Win32.Foundation.PWSTR, lpProviders: Windows.Win32.Foundation.PWSTR) -> Void: ...
class CONNECTDLGSTRUCTA(EasyCastStructure):
    cbStructure: UInt32
    hwndOwner: Windows.Win32.Foundation.HWND
    lpConnRes: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEA_head)
    dwFlags: Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS
    dwDevNum: UInt32
class CONNECTDLGSTRUCTW(EasyCastStructure):
    cbStructure: UInt32
    hwndOwner: Windows.Win32.Foundation.HWND
    lpConnRes: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head)
    dwFlags: Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS
    dwDevNum: UInt32
CONNECTDLGSTRUCT_FLAGS = UInt32
CONNDLG_RO_PATH: CONNECTDLGSTRUCT_FLAGS = 1
CONNDLG_CONN_POINT: CONNECTDLGSTRUCT_FLAGS = 2
CONNDLG_USE_MRU: CONNECTDLGSTRUCT_FLAGS = 4
CONNDLG_HIDE_BOX: CONNECTDLGSTRUCT_FLAGS = 8
CONNDLG_PERSIST: CONNECTDLGSTRUCT_FLAGS = 16
CONNDLG_NOT_PERSIST: CONNECTDLGSTRUCT_FLAGS = 32
class DISCDLGSTRUCTA(EasyCastStructure):
    cbStructure: UInt32
    hwndOwner: Windows.Win32.Foundation.HWND
    lpLocalName: Windows.Win32.Foundation.PSTR
    lpRemoteName: Windows.Win32.Foundation.PSTR
    dwFlags: Windows.Win32.NetworkManagement.WNet.DISCDLGSTRUCT_FLAGS
class DISCDLGSTRUCTW(EasyCastStructure):
    cbStructure: UInt32
    hwndOwner: Windows.Win32.Foundation.HWND
    lpLocalName: Windows.Win32.Foundation.PWSTR
    lpRemoteName: Windows.Win32.Foundation.PWSTR
    dwFlags: Windows.Win32.NetworkManagement.WNet.DISCDLGSTRUCT_FLAGS
DISCDLGSTRUCT_FLAGS = UInt32
DISC_UPDATE_PROFILE: DISCDLGSTRUCT_FLAGS = 1
DISC_NO_FORCE: DISCDLGSTRUCT_FLAGS = 64
class NETCONNECTINFOSTRUCT(EasyCastStructure):
    cbStructure: UInt32
    dwFlags: UInt32
    dwSpeed: UInt32
    dwDelay: UInt32
    dwOptDataSize: UInt32
class NETINFOSTRUCT(EasyCastStructure):
    cbStructure: UInt32
    dwProviderVersion: UInt32
    dwStatus: Windows.Win32.Foundation.WIN32_ERROR
    dwCharacteristics: Windows.Win32.NetworkManagement.WNet.NETINFOSTRUCT_CHARACTERISTICS
    dwHandle: UIntPtr
    wNetType: UInt16
    dwPrinters: UInt32
    dwDrives: UInt32
NETINFOSTRUCT_CHARACTERISTICS = UInt32
NETINFO_DLL16: NETINFOSTRUCT_CHARACTERISTICS = 1
NETINFO_DISKRED: NETINFOSTRUCT_CHARACTERISTICS = 4
NETINFO_PRINTERRED: NETINFOSTRUCT_CHARACTERISTICS = 8
class NETRESOURCEA(EasyCastStructure):
    dwScope: Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_SCOPE
    dwType: Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_TYPE
    dwDisplayType: UInt32
    dwUsage: UInt32
    lpLocalName: Windows.Win32.Foundation.PSTR
    lpRemoteName: Windows.Win32.Foundation.PSTR
    lpComment: Windows.Win32.Foundation.PSTR
    lpProvider: Windows.Win32.Foundation.PSTR
class NETRESOURCEW(EasyCastStructure):
    dwScope: Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_SCOPE
    dwType: Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_TYPE
    dwDisplayType: UInt32
    dwUsage: UInt32
    lpLocalName: Windows.Win32.Foundation.PWSTR
    lpRemoteName: Windows.Win32.Foundation.PWSTR
    lpComment: Windows.Win32.Foundation.PWSTR
    lpProvider: Windows.Win32.Foundation.PWSTR
NETWORK_NAME_FORMAT_FLAGS = UInt32
WNFMT_MULTILINE: NETWORK_NAME_FORMAT_FLAGS = 1
WNFMT_ABBREVIATED: NETWORK_NAME_FORMAT_FLAGS = 2
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
class NOTIFYADD(EasyCastStructure):
    hwndOwner: Windows.Win32.Foundation.HWND
    NetResource: Windows.Win32.NetworkManagement.WNet.NETRESOURCEA
    dwAddFlags: Windows.Win32.NetworkManagement.WNet.NET_USE_CONNECT_FLAGS
class NOTIFYCANCEL(EasyCastStructure):
    lpName: Windows.Win32.Foundation.PWSTR
    lpProvider: Windows.Win32.Foundation.PWSTR
    dwFlags: UInt32
    fForce: Windows.Win32.Foundation.BOOL
class NOTIFYINFO(EasyCastStructure):
    dwNotifyStatus: UInt32
    dwOperationStatus: UInt32
    lpContext: VoidPtr
NPDIRECTORY_NOTIFY_OPERATION = UInt32
WNDN_MKDIR: NPDIRECTORY_NOTIFY_OPERATION = 1
WNDN_RMDIR: NPDIRECTORY_NOTIFY_OPERATION = 2
WNDN_MVDIR: NPDIRECTORY_NOTIFY_OPERATION = 3
NP_PROPERTY_DIALOG_SELECTION = UInt32
WNPS_FILE: NP_PROPERTY_DIALOG_SELECTION = 0
WNPS_DIR: NP_PROPERTY_DIALOG_SELECTION = 1
WNPS_MULT: NP_PROPERTY_DIALOG_SELECTION = 2
@winfunctype_pointer
def PF_AddConnectNotify(lpNotifyInfo: POINTER(Windows.Win32.NetworkManagement.WNet.NOTIFYINFO_head), lpAddInfo: POINTER(Windows.Win32.NetworkManagement.WNet.NOTIFYADD_head)) -> UInt32: ...
@winfunctype_pointer
def PF_CancelConnectNotify(lpNotifyInfo: POINTER(Windows.Win32.NetworkManagement.WNet.NOTIFYINFO_head), lpCancelInfo: POINTER(Windows.Win32.NetworkManagement.WNet.NOTIFYCANCEL_head)) -> UInt32: ...
@winfunctype_pointer
def PF_NPAddConnection(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: Windows.Win32.Foundation.PWSTR, lpUserName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def PF_NPAddConnection3(hwndOwner: Windows.Win32.Foundation.HWND, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpPassword: Windows.Win32.Foundation.PWSTR, lpUserName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPAddConnection4(hwndOwner: Windows.Win32.Foundation.HWND, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: POINTER(Byte), cbUseOptions: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPCancelConnection(lpName: Windows.Win32.Foundation.PWSTR, fForce: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype_pointer
def PF_NPCancelConnection2(lpName: Windows.Win32.Foundation.PWSTR, fForce: Windows.Win32.Foundation.BOOL, dwFlags: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPCloseEnum(hEnum: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype_pointer
def PF_NPDeviceMode(hParent: Windows.Win32.Foundation.HWND) -> UInt32: ...
@winfunctype_pointer
def PF_NPDirectoryNotify(hwnd: Windows.Win32.Foundation.HWND, lpDir: Windows.Win32.Foundation.PWSTR, dwOper: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPEnumResource(hEnum: Windows.Win32.Foundation.HANDLE, lpcCount: POINTER(UInt32), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPFMXEditPerm(lpDriveName: Windows.Win32.Foundation.PWSTR, hwndFMX: Windows.Win32.Foundation.HWND, nDialogType: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPFMXGetPermCaps(lpDriveName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def PF_NPFMXGetPermHelp(lpDriveName: Windows.Win32.Foundation.PWSTR, nDialogType: UInt32, fDirectory: Windows.Win32.Foundation.BOOL, lpFileNameBuffer: VoidPtr, lpBufferSize: POINTER(UInt32), lpnHelpContext: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPFormatNetworkName(lpRemoteName: Windows.Win32.Foundation.PWSTR, lpFormattedName: Windows.Win32.Foundation.PWSTR, lpnLength: POINTER(UInt32), dwFlags: UInt32, dwAveCharPerLine: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetCaps(ndex: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetConnection(lpLocalName: Windows.Win32.Foundation.PWSTR, lpRemoteName: Windows.Win32.Foundation.PWSTR, lpnBufferLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetConnection3(lpLocalName: Windows.Win32.Foundation.PWSTR, dwLevel: UInt32, lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetConnectionPerformance(lpRemoteName: Windows.Win32.Foundation.PWSTR, lpNetConnectInfo: POINTER(Windows.Win32.NetworkManagement.WNet.NETCONNECTINFOSTRUCT_head)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetDirectoryType(lpName: Windows.Win32.Foundation.PWSTR, lpType: POINTER(Int32), bFlushCache: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetPersistentUseOptionsForConnection(lpRemotePath: Windows.Win32.Foundation.PWSTR, lpReadUseOptions: POINTER(Byte), cbReadUseOptions: UInt32, lpWriteUseOptions: POINTER(Byte), lpSizeWriteUseOptions: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetPropertyText(iButton: UInt32, nPropSel: UInt32, lpName: Windows.Win32.Foundation.PWSTR, lpButtonName: Windows.Win32.Foundation.PWSTR, nButtonNameLen: UInt32, nType: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetResourceInformation(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32), lplpSystem: POINTER(Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetResourceParent(lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetUniversalName(lpLocalPath: Windows.Win32.Foundation.PWSTR, dwInfoLevel: UInt32, lpBuffer: VoidPtr, lpnBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetUser(lpName: Windows.Win32.Foundation.PWSTR, lpUserName: Windows.Win32.Foundation.PWSTR, lpnBufferLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPLogonNotify(lpLogonId: POINTER(Windows.Win32.Foundation.LUID_head), lpAuthentInfoType: Windows.Win32.Foundation.PWSTR, lpAuthentInfo: VoidPtr, lpPreviousAuthentInfoType: Windows.Win32.Foundation.PWSTR, lpPreviousAuthentInfo: VoidPtr, lpStationName: Windows.Win32.Foundation.PWSTR, StationHandle: VoidPtr, lpLogonScript: POINTER(Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype_pointer
def PF_NPOpenEnum(dwScope: UInt32, dwType: UInt32, dwUsage: UInt32, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lphEnum: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype_pointer
def PF_NPPasswordChangeNotify(lpAuthentInfoType: Windows.Win32.Foundation.PWSTR, lpAuthentInfo: VoidPtr, lpPreviousAuthentInfoType: Windows.Win32.Foundation.PWSTR, lpPreviousAuthentInfo: VoidPtr, lpStationName: Windows.Win32.Foundation.PWSTR, StationHandle: VoidPtr, dwChangeInfo: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPPropertyDialog(hwndParent: Windows.Win32.Foundation.HWND, iButtonDlg: UInt32, nPropSel: UInt32, lpFileName: Windows.Win32.Foundation.PWSTR, nType: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPSearchDialog(hwndParent: Windows.Win32.Foundation.HWND, lpNetResource: POINTER(Windows.Win32.NetworkManagement.WNet.NETRESOURCEW_head), lpBuffer: VoidPtr, cbBuffer: UInt32, lpnFlags: POINTER(UInt32)) -> UInt32: ...
class REMOTE_NAME_INFOA(EasyCastStructure):
    lpUniversalName: Windows.Win32.Foundation.PSTR
    lpConnectionName: Windows.Win32.Foundation.PSTR
    lpRemainingPath: Windows.Win32.Foundation.PSTR
class REMOTE_NAME_INFOW(EasyCastStructure):
    lpUniversalName: Windows.Win32.Foundation.PWSTR
    lpConnectionName: Windows.Win32.Foundation.PWSTR
    lpRemainingPath: Windows.Win32.Foundation.PWSTR
UNC_INFO_LEVEL = UInt32
UNIVERSAL_NAME_INFO_LEVEL: UNC_INFO_LEVEL = 1
REMOTE_NAME_INFO_LEVEL: UNC_INFO_LEVEL = 2
class UNIVERSAL_NAME_INFOA(EasyCastStructure):
    lpUniversalName: Windows.Win32.Foundation.PSTR
class UNIVERSAL_NAME_INFOW(EasyCastStructure):
    lpUniversalName: Windows.Win32.Foundation.PWSTR
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
