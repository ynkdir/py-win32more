from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.WNet
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
WNFMT_INENUM: UInt32 = 16
WNFMT_CONNECTION: UInt32 = 32
WNCON_FORNETCARD: UInt32 = 1
WNCON_NOTROUTED: UInt32 = 2
WNCON_SLOWLINK: UInt32 = 4
WNCON_DYNAMIC: UInt32 = 8
@winfunctype('MPR.dll')
def WNetAddConnectionA(lpRemoteName: win32more.Windows.Win32.Foundation.PSTR, lpPassword: win32more.Windows.Win32.Foundation.PSTR, lpLocalName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetAddConnectionW(lpRemoteName: win32more.Windows.Win32.Foundation.PWSTR, lpPassword: win32more.Windows.Win32.Foundation.PWSTR, lpLocalName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetAddConnection = UnicodeAlias('WNetAddConnectionW')
@winfunctype('MPR.dll')
def WNetAddConnection2A(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEA), lpPassword: win32more.Windows.Win32.Foundation.PSTR, lpUserName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetAddConnection2W(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpPassword: win32more.Windows.Win32.Foundation.PWSTR, lpUserName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetAddConnection2 = UnicodeAlias('WNetAddConnection2W')
@winfunctype('MPR.dll')
def WNetAddConnection3A(hwndOwner: win32more.Windows.Win32.Foundation.HWND, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEA), lpPassword: win32more.Windows.Win32.Foundation.PSTR, lpUserName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetAddConnection3W(hwndOwner: win32more.Windows.Win32.Foundation.HWND, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpPassword: win32more.Windows.Win32.Foundation.PWSTR, lpUserName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetAddConnection3 = UnicodeAlias('WNetAddConnection3W')
@winfunctype('MPR.dll')
def WNetAddConnection4A(hwndOwner: win32more.Windows.Win32.Foundation.HWND, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEA), pAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS, lpUseOptions: POINTER(Byte), cbUseOptions: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetAddConnection4W(hwndOwner: win32more.Windows.Win32.Foundation.HWND, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), pAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS, lpUseOptions: POINTER(Byte), cbUseOptions: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetAddConnection4 = UnicodeAlias('WNetAddConnection4W')
@winfunctype('MPR.dll')
def WNetCancelConnectionA(lpName: win32more.Windows.Win32.Foundation.PSTR, fForce: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetCancelConnectionW(lpName: win32more.Windows.Win32.Foundation.PWSTR, fForce: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetCancelConnection = UnicodeAlias('WNetCancelConnectionW')
@winfunctype('MPR.dll')
def WNetCancelConnection2A(lpName: win32more.Windows.Win32.Foundation.PSTR, dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS, fForce: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetCancelConnection2W(lpName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS, fForce: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetCancelConnection2 = UnicodeAlias('WNetCancelConnection2W')
@winfunctype('MPR.dll')
def WNetGetConnectionA(lpLocalName: win32more.Windows.Win32.Foundation.PSTR, lpRemoteName: win32more.Windows.Win32.Foundation.PSTR, lpnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetGetConnectionW(lpLocalName: win32more.Windows.Win32.Foundation.PWSTR, lpRemoteName: win32more.Windows.Win32.Foundation.PWSTR, lpnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetGetConnection = UnicodeAlias('WNetGetConnectionW')
@winfunctype('MPR.dll')
def WNetUseConnectionA(hwndOwner: win32more.Windows.Win32.Foundation.HWND, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEA), lpPassword: win32more.Windows.Win32.Foundation.PSTR, lpUserId: win32more.Windows.Win32.Foundation.PSTR, dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS, lpAccessName: win32more.Windows.Win32.Foundation.PSTR, lpBufferSize: POINTER(UInt32), lpResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetUseConnectionW(hwndOwner: win32more.Windows.Win32.Foundation.HWND, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpPassword: win32more.Windows.Win32.Foundation.PWSTR, lpUserId: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS, lpAccessName: win32more.Windows.Win32.Foundation.PWSTR, lpBufferSize: POINTER(UInt32), lpResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetUseConnection = UnicodeAlias('WNetUseConnectionW')
@winfunctype('MPR.dll')
def WNetUseConnection4A(hwndOwner: win32more.Windows.Win32.Foundation.HWND, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEA), pAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: POINTER(Byte), cbUseOptions: UInt32, lpAccessName: win32more.Windows.Win32.Foundation.PSTR, lpBufferSize: POINTER(UInt32), lpResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetUseConnection4W(hwndOwner: win32more.Windows.Win32.Foundation.HWND, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), pAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: POINTER(Byte), cbUseOptions: UInt32, lpAccessName: win32more.Windows.Win32.Foundation.PWSTR, lpBufferSize: POINTER(UInt32), lpResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetUseConnection4 = UnicodeAlias('WNetUseConnection4W')
@winfunctype('MPR.dll')
def WNetConnectionDialog(hwnd: win32more.Windows.Win32.Foundation.HWND, dwType: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetDisconnectDialog(hwnd: win32more.Windows.Win32.Foundation.HWND, dwType: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetConnectionDialog1A(lpConnDlgStruct: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCTA)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetConnectionDialog1W(lpConnDlgStruct: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCTW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetConnectionDialog1 = UnicodeAlias('WNetConnectionDialog1W')
@winfunctype('MPR.dll')
def WNetDisconnectDialog1A(lpConnDlgStruct: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.DISCDLGSTRUCTA)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetDisconnectDialog1W(lpConnDlgStruct: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.DISCDLGSTRUCTW)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetDisconnectDialog1 = UnicodeAlias('WNetDisconnectDialog1W')
@winfunctype('MPR.dll')
def WNetOpenEnumA(dwScope: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_SCOPE, dwType: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_TYPE, dwUsage: win32more.Windows.Win32.NetworkManagement.WNet.WNET_OPEN_ENUM_USAGE, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEA), lphEnum: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetOpenEnumW(dwScope: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_SCOPE, dwType: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_TYPE, dwUsage: win32more.Windows.Win32.NetworkManagement.WNet.WNET_OPEN_ENUM_USAGE, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lphEnum: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetOpenEnum = UnicodeAlias('WNetOpenEnumW')
@winfunctype('MPR.dll')
def WNetEnumResourceA(hEnum: win32more.Windows.Win32.Foundation.HANDLE, lpcCount: POINTER(UInt32), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetEnumResourceW(hEnum: win32more.Windows.Win32.Foundation.HANDLE, lpcCount: POINTER(UInt32), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetEnumResource = UnicodeAlias('WNetEnumResourceW')
@winfunctype('MPR.dll')
def WNetCloseEnum(hEnum: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetGetResourceParentA(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEA), lpBuffer: VoidPtr, lpcbBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetGetResourceParentW(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpBuffer: VoidPtr, lpcbBuffer: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetGetResourceParent = UnicodeAlias('WNetGetResourceParentW')
@winfunctype('MPR.dll')
def WNetGetResourceInformationA(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEA), lpBuffer: VoidPtr, lpcbBuffer: POINTER(UInt32), lplpSystem: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetGetResourceInformationW(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpBuffer: VoidPtr, lpcbBuffer: POINTER(UInt32), lplpSystem: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetGetResourceInformation = UnicodeAlias('WNetGetResourceInformationW')
@winfunctype('MPR.dll')
def WNetGetUniversalNameA(lpLocalPath: win32more.Windows.Win32.Foundation.PSTR, dwInfoLevel: win32more.Windows.Win32.NetworkManagement.WNet.UNC_INFO_LEVEL, lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetGetUniversalNameW(lpLocalPath: win32more.Windows.Win32.Foundation.PWSTR, dwInfoLevel: win32more.Windows.Win32.NetworkManagement.WNet.UNC_INFO_LEVEL, lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetGetUniversalName = UnicodeAlias('WNetGetUniversalNameW')
@winfunctype('MPR.dll')
def WNetGetUserA(lpName: win32more.Windows.Win32.Foundation.PSTR, lpUserName: win32more.Windows.Win32.Foundation.PSTR, lpnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetGetUserW(lpName: win32more.Windows.Win32.Foundation.PWSTR, lpUserName: win32more.Windows.Win32.Foundation.PWSTR, lpnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetGetUser = UnicodeAlias('WNetGetUserW')
@winfunctype('MPR.dll')
def WNetGetProviderNameA(dwNetType: UInt32, lpProviderName: win32more.Windows.Win32.Foundation.PSTR, lpBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetGetProviderNameW(dwNetType: UInt32, lpProviderName: win32more.Windows.Win32.Foundation.PWSTR, lpBufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetGetProviderName = UnicodeAlias('WNetGetProviderNameW')
@winfunctype('MPR.dll')
def WNetGetNetworkInformationA(lpProvider: win32more.Windows.Win32.Foundation.PSTR, lpNetInfoStruct: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETINFOSTRUCT)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetGetNetworkInformationW(lpProvider: win32more.Windows.Win32.Foundation.PWSTR, lpNetInfoStruct: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETINFOSTRUCT)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetGetNetworkInformation = UnicodeAlias('WNetGetNetworkInformationW')
@winfunctype('MPR.dll')
def WNetGetLastErrorA(lpError: POINTER(UInt32), lpErrorBuf: win32more.Windows.Win32.Foundation.PSTR, nErrorBufSize: UInt32, lpNameBuf: win32more.Windows.Win32.Foundation.PSTR, nNameBufSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('MPR.dll')
def WNetGetLastErrorW(lpError: POINTER(UInt32), lpErrorBuf: win32more.Windows.Win32.Foundation.PWSTR, nErrorBufSize: UInt32, lpNameBuf: win32more.Windows.Win32.Foundation.PWSTR, nNameBufSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
WNetGetLastError = UnicodeAlias('WNetGetLastErrorW')
@winfunctype('MPR.dll')
def MultinetGetConnectionPerformanceA(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEA), lpNetConnectInfoStruct: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETCONNECTINFOSTRUCT)) -> UInt32: ...
@winfunctype('MPR.dll')
def MultinetGetConnectionPerformanceW(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpNetConnectInfoStruct: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETCONNECTINFOSTRUCT)) -> UInt32: ...
MultinetGetConnectionPerformance = UnicodeAlias('MultinetGetConnectionPerformanceW')
@winfunctype('davclnt.dll')
def NPAddConnection(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpPassword: win32more.Windows.Win32.Foundation.PWSTR, lpUserName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPAddConnection3(hwndOwner: win32more.Windows.Win32.Foundation.HWND, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpPassword: win32more.Windows.Win32.Foundation.PWSTR, lpUserName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPAddConnection4(hwndOwner: win32more.Windows.Win32.Foundation.HWND, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: POINTER(Byte), cbUseOptions: UInt32) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPCancelConnection(lpName: win32more.Windows.Win32.Foundation.PWSTR, fForce: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPCancelConnection2(lpName: win32more.Windows.Win32.Foundation.PWSTR, fForce: win32more.Windows.Win32.Foundation.BOOL, dwFlags: UInt32) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetConnection(lpLocalName: win32more.Windows.Win32.Foundation.PWSTR, lpRemoteName: win32more.Windows.Win32.Foundation.PWSTR, lpnBufferLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPGetConnection3(lpLocalName: win32more.Windows.Win32.Foundation.PWSTR, dwLevel: UInt32, lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetUniversalName(lpLocalPath: win32more.Windows.Win32.Foundation.PWSTR, dwInfoLevel: win32more.Windows.Win32.NetworkManagement.WNet.UNC_INFO_LEVEL, lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPGetConnectionPerformance(lpRemoteName: win32more.Windows.Win32.Foundation.PWSTR, lpNetConnectInfo: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETCONNECTINFOSTRUCT)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPOpenEnum(dwScope: UInt32, dwType: UInt32, dwUsage: UInt32, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lphEnum: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPEnumResource(hEnum: win32more.Windows.Win32.Foundation.HANDLE, lpcCount: POINTER(UInt32), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPCloseEnum(hEnum: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetCaps(ndex: UInt32) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetUser(lpName: win32more.Windows.Win32.Foundation.PWSTR, lpUserName: win32more.Windows.Win32.Foundation.PWSTR, lpnBufferLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NTLANMAN.dll')
def NPGetPersistentUseOptionsForConnection(lpRemotePath: win32more.Windows.Win32.Foundation.PWSTR, lpReadUseOptions: POINTER(Byte), cbReadUseOptions: UInt32, lpWriteUseOptions: POINTER(Byte), lpSizeWriteUseOptions: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetResourceParent(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPGetResourceInformation(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32), lplpSystem: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('davclnt.dll')
def NPFormatNetworkName(lpRemoteName: win32more.Windows.Win32.Foundation.PWSTR, lpFormattedName: win32more.Windows.Win32.Foundation.PWSTR, lpnLength: POINTER(UInt32), dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.NETWORK_NAME_FORMAT_FLAGS, dwAveCharPerLine: UInt32) -> UInt32: ...
@winfunctype('MPR.dll')
def WNetSetLastErrorA(err: UInt32, lpError: win32more.Windows.Win32.Foundation.PSTR, lpProviders: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('MPR.dll')
def WNetSetLastErrorW(err: UInt32, lpError: win32more.Windows.Win32.Foundation.PWSTR, lpProviders: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
WNetSetLastError = UnicodeAlias('WNetSetLastErrorW')
class CONNECTDLGSTRUCTA(Structure):
    cbStructure: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    lpConnRes: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEA)
    dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS
    dwDevNum: UInt32
class CONNECTDLGSTRUCTW(Structure):
    cbStructure: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    lpConnRes: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW)
    dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS
    dwDevNum: UInt32
CONNECTDLGSTRUCT = UnicodeAlias('CONNECTDLGSTRUCTW')
CONNECTDLGSTRUCT_FLAGS = UInt32
CONNDLG_RO_PATH: win32more.Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS = 1
CONNDLG_CONN_POINT: win32more.Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS = 2
CONNDLG_USE_MRU: win32more.Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS = 4
CONNDLG_HIDE_BOX: win32more.Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS = 8
CONNDLG_PERSIST: win32more.Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS = 16
CONNDLG_NOT_PERSIST: win32more.Windows.Win32.NetworkManagement.WNet.CONNECTDLGSTRUCT_FLAGS = 32
class DISCDLGSTRUCTA(Structure):
    cbStructure: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    lpLocalName: win32more.Windows.Win32.Foundation.PSTR
    lpRemoteName: win32more.Windows.Win32.Foundation.PSTR
    dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.DISCDLGSTRUCT_FLAGS
class DISCDLGSTRUCTW(Structure):
    cbStructure: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    lpLocalName: win32more.Windows.Win32.Foundation.PWSTR
    lpRemoteName: win32more.Windows.Win32.Foundation.PWSTR
    dwFlags: win32more.Windows.Win32.NetworkManagement.WNet.DISCDLGSTRUCT_FLAGS
DISCDLGSTRUCT = UnicodeAlias('DISCDLGSTRUCTW')
DISCDLGSTRUCT_FLAGS = UInt32
DISC_UPDATE_PROFILE: win32more.Windows.Win32.NetworkManagement.WNet.DISCDLGSTRUCT_FLAGS = 1
DISC_NO_FORCE: win32more.Windows.Win32.NetworkManagement.WNet.DISCDLGSTRUCT_FLAGS = 64
class NETCONNECTINFOSTRUCT(Structure):
    cbStructure: UInt32
    dwFlags: UInt32
    dwSpeed: UInt32
    dwDelay: UInt32
    dwOptDataSize: UInt32
class NETINFOSTRUCT(Structure):
    cbStructure: UInt32
    dwProviderVersion: UInt32
    dwStatus: win32more.Windows.Win32.Foundation.WIN32_ERROR
    dwCharacteristics: win32more.Windows.Win32.NetworkManagement.WNet.NETINFOSTRUCT_CHARACTERISTICS
    dwHandle: UIntPtr
    wNetType: UInt16
    dwPrinters: UInt32
    dwDrives: UInt32
NETINFOSTRUCT_CHARACTERISTICS = UInt32
NETINFO_DLL16: win32more.Windows.Win32.NetworkManagement.WNet.NETINFOSTRUCT_CHARACTERISTICS = 1
NETINFO_DISKRED: win32more.Windows.Win32.NetworkManagement.WNet.NETINFOSTRUCT_CHARACTERISTICS = 4
NETINFO_PRINTERRED: win32more.Windows.Win32.NetworkManagement.WNet.NETINFOSTRUCT_CHARACTERISTICS = 8
class NETRESOURCEA(Structure):
    dwScope: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_SCOPE
    dwType: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_TYPE
    dwDisplayType: UInt32
    dwUsage: UInt32
    lpLocalName: win32more.Windows.Win32.Foundation.PSTR
    lpRemoteName: win32more.Windows.Win32.Foundation.PSTR
    lpComment: win32more.Windows.Win32.Foundation.PSTR
    lpProvider: win32more.Windows.Win32.Foundation.PSTR
class NETRESOURCEW(Structure):
    dwScope: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_SCOPE
    dwType: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_TYPE
    dwDisplayType: UInt32
    dwUsage: UInt32
    lpLocalName: win32more.Windows.Win32.Foundation.PWSTR
    lpRemoteName: win32more.Windows.Win32.Foundation.PWSTR
    lpComment: win32more.Windows.Win32.Foundation.PWSTR
    lpProvider: win32more.Windows.Win32.Foundation.PWSTR
NETRESOURCE = UnicodeAlias('NETRESOURCEW')
NETWORK_NAME_FORMAT_FLAGS = UInt32
WNFMT_MULTILINE: win32more.Windows.Win32.NetworkManagement.WNet.NETWORK_NAME_FORMAT_FLAGS = 1
WNFMT_ABBREVIATED: win32more.Windows.Win32.NetworkManagement.WNet.NETWORK_NAME_FORMAT_FLAGS = 2
NET_CONNECT_FLAGS = UInt32
CONNECT_UPDATE_PROFILE: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 1
CONNECT_UPDATE_RECENT: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 2
CONNECT_TEMPORARY: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 4
CONNECT_INTERACTIVE: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 8
CONNECT_PROMPT: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 16
CONNECT_NEED_DRIVE: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 32
CONNECT_REFCOUNT: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 64
CONNECT_REDIRECT: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 128
CONNECT_LOCALDRIVE: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 256
CONNECT_CURRENT_MEDIA: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 512
CONNECT_DEFERRED: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 1024
CONNECT_RESERVED: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 4278190080
CONNECT_COMMANDLINE: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 2048
CONNECT_CMD_SAVECRED: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 4096
CONNECT_CRED_RESET: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 8192
CONNECT_REQUIRE_INTEGRITY: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 16384
CONNECT_REQUIRE_PRIVACY: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 32768
CONNECT_WRITE_THROUGH_SEMANTICS: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 65536
CONNECT_GLOBAL_MAPPING: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS = 262144
NET_RESOURCE_SCOPE = UInt32
RESOURCE_CONNECTED: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_SCOPE = 1
RESOURCE_CONTEXT: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_SCOPE = 5
RESOURCE_GLOBALNET: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_SCOPE = 2
RESOURCE_REMEMBERED: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_SCOPE = 3
NET_RESOURCE_TYPE = UInt32
RESOURCETYPE_ANY: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_TYPE = 0
RESOURCETYPE_DISK: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_TYPE = 1
RESOURCETYPE_PRINT: win32more.Windows.Win32.NetworkManagement.WNet.NET_RESOURCE_TYPE = 2
class NOTIFYADD(Structure):
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    NetResource: win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEA
    dwAddFlags: win32more.Windows.Win32.NetworkManagement.WNet.NET_CONNECT_FLAGS
class NOTIFYCANCEL(Structure):
    lpName: win32more.Windows.Win32.Foundation.PWSTR
    lpProvider: win32more.Windows.Win32.Foundation.PWSTR
    dwFlags: UInt32
    fForce: win32more.Windows.Win32.Foundation.BOOL
class NOTIFYINFO(Structure):
    dwNotifyStatus: UInt32
    dwOperationStatus: UInt32
    lpContext: VoidPtr
NPDIRECTORY_NOTIFY_OPERATION = UInt32
WNDN_MKDIR: win32more.Windows.Win32.NetworkManagement.WNet.NPDIRECTORY_NOTIFY_OPERATION = 1
WNDN_RMDIR: win32more.Windows.Win32.NetworkManagement.WNet.NPDIRECTORY_NOTIFY_OPERATION = 2
WNDN_MVDIR: win32more.Windows.Win32.NetworkManagement.WNet.NPDIRECTORY_NOTIFY_OPERATION = 3
NP_PROPERTY_DIALOG_SELECTION = UInt32
WNPS_FILE: win32more.Windows.Win32.NetworkManagement.WNet.NP_PROPERTY_DIALOG_SELECTION = 0
WNPS_DIR: win32more.Windows.Win32.NetworkManagement.WNet.NP_PROPERTY_DIALOG_SELECTION = 1
WNPS_MULT: win32more.Windows.Win32.NetworkManagement.WNet.NP_PROPERTY_DIALOG_SELECTION = 2
@winfunctype_pointer
def PF_AddConnectNotify(lpNotifyInfo: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NOTIFYINFO), lpAddInfo: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NOTIFYADD)) -> UInt32: ...
@winfunctype_pointer
def PF_CancelConnectNotify(lpNotifyInfo: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NOTIFYINFO), lpCancelInfo: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NOTIFYCANCEL)) -> UInt32: ...
@winfunctype_pointer
def PF_NPAddConnection(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpPassword: win32more.Windows.Win32.Foundation.PWSTR, lpUserName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def PF_NPAddConnection3(hwndOwner: win32more.Windows.Win32.Foundation.HWND, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpPassword: win32more.Windows.Win32.Foundation.PWSTR, lpUserName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPAddConnection4(hwndOwner: win32more.Windows.Win32.Foundation.HWND, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpAuthBuffer: VoidPtr, cbAuthBuffer: UInt32, dwFlags: UInt32, lpUseOptions: POINTER(Byte), cbUseOptions: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPCancelConnection(lpName: win32more.Windows.Win32.Foundation.PWSTR, fForce: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype_pointer
def PF_NPCancelConnection2(lpName: win32more.Windows.Win32.Foundation.PWSTR, fForce: win32more.Windows.Win32.Foundation.BOOL, dwFlags: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPCloseEnum(hEnum: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype_pointer
def PF_NPDeviceMode(hParent: win32more.Windows.Win32.Foundation.HWND) -> UInt32: ...
@winfunctype_pointer
def PF_NPDirectoryNotify(hwnd: win32more.Windows.Win32.Foundation.HWND, lpDir: win32more.Windows.Win32.Foundation.PWSTR, dwOper: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPEnumResource(hEnum: win32more.Windows.Win32.Foundation.HANDLE, lpcCount: POINTER(UInt32), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPFMXEditPerm(lpDriveName: win32more.Windows.Win32.Foundation.PWSTR, hwndFMX: win32more.Windows.Win32.Foundation.HWND, nDialogType: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPFMXGetPermCaps(lpDriveName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def PF_NPFMXGetPermHelp(lpDriveName: win32more.Windows.Win32.Foundation.PWSTR, nDialogType: UInt32, fDirectory: win32more.Windows.Win32.Foundation.BOOL, lpFileNameBuffer: VoidPtr, lpBufferSize: POINTER(UInt32), lpnHelpContext: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPFormatNetworkName(lpRemoteName: win32more.Windows.Win32.Foundation.PWSTR, lpFormattedName: win32more.Windows.Win32.Foundation.PWSTR, lpnLength: POINTER(UInt32), dwFlags: UInt32, dwAveCharPerLine: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetCaps(ndex: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetConnection(lpLocalName: win32more.Windows.Win32.Foundation.PWSTR, lpRemoteName: win32more.Windows.Win32.Foundation.PWSTR, lpnBufferLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetConnection3(lpLocalName: win32more.Windows.Win32.Foundation.PWSTR, dwLevel: UInt32, lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetConnectionPerformance(lpRemoteName: win32more.Windows.Win32.Foundation.PWSTR, lpNetConnectInfo: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETCONNECTINFOSTRUCT)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetDirectoryType(lpName: win32more.Windows.Win32.Foundation.PWSTR, lpType: POINTER(Int32), bFlushCache: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetPersistentUseOptionsForConnection(lpRemotePath: win32more.Windows.Win32.Foundation.PWSTR, lpReadUseOptions: POINTER(Byte), cbReadUseOptions: UInt32, lpWriteUseOptions: POINTER(Byte), lpSizeWriteUseOptions: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetPropertyText(iButton: UInt32, nPropSel: UInt32, lpName: win32more.Windows.Win32.Foundation.PWSTR, lpButtonName: win32more.Windows.Win32.Foundation.PWSTR, nButtonNameLen: UInt32, nType: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetResourceInformation(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32), lplpSystem: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetResourceParent(lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpBuffer: VoidPtr, lpBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetUniversalName(lpLocalPath: win32more.Windows.Win32.Foundation.PWSTR, dwInfoLevel: UInt32, lpBuffer: VoidPtr, lpnBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPGetUser(lpName: win32more.Windows.Win32.Foundation.PWSTR, lpUserName: win32more.Windows.Win32.Foundation.PWSTR, lpnBufferLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PF_NPLogonNotify(lpLogonId: POINTER(win32more.Windows.Win32.Foundation.LUID), lpAuthentInfoType: win32more.Windows.Win32.Foundation.PWSTR, lpAuthentInfo: VoidPtr, lpPreviousAuthentInfoType: win32more.Windows.Win32.Foundation.PWSTR, lpPreviousAuthentInfo: VoidPtr, lpStationName: win32more.Windows.Win32.Foundation.PWSTR, StationHandle: VoidPtr, lpLogonScript: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype_pointer
def PF_NPOpenEnum(dwScope: UInt32, dwType: UInt32, dwUsage: UInt32, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lphEnum: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype_pointer
def PF_NPPasswordChangeNotify(lpAuthentInfoType: win32more.Windows.Win32.Foundation.PWSTR, lpAuthentInfo: VoidPtr, lpPreviousAuthentInfoType: win32more.Windows.Win32.Foundation.PWSTR, lpPreviousAuthentInfo: VoidPtr, lpStationName: win32more.Windows.Win32.Foundation.PWSTR, StationHandle: VoidPtr, dwChangeInfo: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPPropertyDialog(hwndParent: win32more.Windows.Win32.Foundation.HWND, iButtonDlg: UInt32, nPropSel: UInt32, lpFileName: win32more.Windows.Win32.Foundation.PWSTR, nType: UInt32) -> UInt32: ...
@winfunctype_pointer
def PF_NPSearchDialog(hwndParent: win32more.Windows.Win32.Foundation.HWND, lpNetResource: POINTER(win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEW), lpBuffer: VoidPtr, cbBuffer: UInt32, lpnFlags: POINTER(UInt32)) -> UInt32: ...
class REMOTE_NAME_INFOA(Structure):
    lpUniversalName: win32more.Windows.Win32.Foundation.PSTR
    lpConnectionName: win32more.Windows.Win32.Foundation.PSTR
    lpRemainingPath: win32more.Windows.Win32.Foundation.PSTR
class REMOTE_NAME_INFOW(Structure):
    lpUniversalName: win32more.Windows.Win32.Foundation.PWSTR
    lpConnectionName: win32more.Windows.Win32.Foundation.PWSTR
    lpRemainingPath: win32more.Windows.Win32.Foundation.PWSTR
REMOTE_NAME_INFO = UnicodeAlias('REMOTE_NAME_INFOW')
UNC_INFO_LEVEL = UInt32
UNIVERSAL_NAME_INFO_LEVEL: win32more.Windows.Win32.NetworkManagement.WNet.UNC_INFO_LEVEL = 1
REMOTE_NAME_INFO_LEVEL: win32more.Windows.Win32.NetworkManagement.WNet.UNC_INFO_LEVEL = 2
class UNIVERSAL_NAME_INFOA(Structure):
    lpUniversalName: win32more.Windows.Win32.Foundation.PSTR
class UNIVERSAL_NAME_INFOW(Structure):
    lpUniversalName: win32more.Windows.Win32.Foundation.PWSTR
UNIVERSAL_NAME_INFO = UnicodeAlias('UNIVERSAL_NAME_INFOW')
WNET_OPEN_ENUM_USAGE = UInt32
RESOURCEUSAGE_NONE: win32more.Windows.Win32.NetworkManagement.WNet.WNET_OPEN_ENUM_USAGE = 0
RESOURCEUSAGE_CONNECTABLE: win32more.Windows.Win32.NetworkManagement.WNet.WNET_OPEN_ENUM_USAGE = 1
RESOURCEUSAGE_CONTAINER: win32more.Windows.Win32.NetworkManagement.WNet.WNET_OPEN_ENUM_USAGE = 2
RESOURCEUSAGE_ATTACHED: win32more.Windows.Win32.NetworkManagement.WNet.WNET_OPEN_ENUM_USAGE = 16
RESOURCEUSAGE_ALL: win32more.Windows.Win32.NetworkManagement.WNet.WNET_OPEN_ENUM_USAGE = 19
WNPERM_DLG = UInt32
WNPERM_DLG_PERM: win32more.Windows.Win32.NetworkManagement.WNet.WNPERM_DLG = 0
WNPERM_DLG_AUDIT: win32more.Windows.Win32.NetworkManagement.WNet.WNPERM_DLG = 1
WNPERM_DLG_OWNER: win32more.Windows.Win32.NetworkManagement.WNet.WNPERM_DLG = 2


make_ready(__name__)
