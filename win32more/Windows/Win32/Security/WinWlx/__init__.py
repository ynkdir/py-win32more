from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Security.WinWlx
import win32more.Windows.Win32.System.StationsAndDesktops
import win32more.Windows.Win32.UI.WindowsAndMessaging
WLX_VERSION_1_0: UInt32 = 65536
WLX_VERSION_1_1: UInt32 = 65537
WLX_VERSION_1_2: UInt32 = 65538
WLX_VERSION_1_3: UInt32 = 65539
WLX_VERSION_1_4: UInt32 = 65540
WLX_CURRENT_VERSION: UInt32 = 65540
WLX_SAS_TYPE_TIMEOUT: UInt32 = 0
WLX_SAS_TYPE_CTRL_ALT_DEL: UInt32 = 1
WLX_SAS_TYPE_SCRNSVR_TIMEOUT: UInt32 = 2
WLX_SAS_TYPE_SCRNSVR_ACTIVITY: UInt32 = 3
WLX_SAS_TYPE_USER_LOGOFF: UInt32 = 4
WLX_SAS_TYPE_SC_INSERT: UInt32 = 5
WLX_SAS_TYPE_SC_REMOVE: UInt32 = 6
WLX_SAS_TYPE_AUTHENTICATED: UInt32 = 7
WLX_SAS_TYPE_SC_FIRST_READER_ARRIVED: UInt32 = 8
WLX_SAS_TYPE_SC_LAST_READER_REMOVED: UInt32 = 9
WLX_SAS_TYPE_SWITCHUSER: UInt32 = 10
WLX_SAS_TYPE_MAX_MSFT_VALUE: UInt32 = 127
WLX_LOGON_OPT_NO_PROFILE: UInt32 = 1
WLX_PROFILE_TYPE_V1_0: UInt32 = 1
WLX_PROFILE_TYPE_V2_0: UInt32 = 2
WLX_SAS_ACTION_LOGON: UInt32 = 1
WLX_SAS_ACTION_NONE: UInt32 = 2
WLX_SAS_ACTION_LOCK_WKSTA: UInt32 = 3
WLX_SAS_ACTION_LOGOFF: UInt32 = 4
WLX_SAS_ACTION_PWD_CHANGED: UInt32 = 6
WLX_SAS_ACTION_TASKLIST: UInt32 = 7
WLX_SAS_ACTION_UNLOCK_WKSTA: UInt32 = 8
WLX_SAS_ACTION_FORCE_LOGOFF: UInt32 = 9
WLX_SAS_ACTION_SHUTDOWN_SLEEP: UInt32 = 12
WLX_SAS_ACTION_SHUTDOWN_SLEEP2: UInt32 = 13
WLX_SAS_ACTION_SHUTDOWN_HIBERNATE: UInt32 = 14
WLX_SAS_ACTION_RECONNECTED: UInt32 = 15
WLX_SAS_ACTION_DELAYED_FORCE_LOGOFF: UInt32 = 16
WLX_SAS_ACTION_SWITCH_CONSOLE: UInt32 = 17
WLX_WM_SAS: UInt32 = 1625
WLX_DLG_SAS: UInt32 = 101
WLX_DLG_INPUT_TIMEOUT: UInt32 = 102
WLX_DLG_SCREEN_SAVER_TIMEOUT: UInt32 = 103
WLX_DLG_USER_LOGOFF: UInt32 = 104
WLX_DIRECTORY_LENGTH: UInt32 = 256
WLX_CREDENTIAL_TYPE_V1_0: UInt32 = 1
WLX_CREDENTIAL_TYPE_V2_0: UInt32 = 2
WLX_CONSOLESWITCHCREDENTIAL_TYPE_V1_0: UInt32 = 1
STATUSMSG_OPTION_NOANIMATION: UInt32 = 1
STATUSMSG_OPTION_SETFOREGROUND: UInt32 = 2
WLX_DESKTOP_NAME: UInt32 = 1
WLX_DESKTOP_HANDLE: UInt32 = 2
WLX_CREATE_INSTANCE_ONLY: UInt32 = 1
WLX_CREATE_USER: UInt32 = 2
WLX_OPTION_USE_CTRL_ALT_DEL: UInt32 = 1
WLX_OPTION_CONTEXT_POINTER: UInt32 = 2
WLX_OPTION_USE_SMART_CARD: UInt32 = 3
WLX_OPTION_FORCE_LOGOFF_TIME: UInt32 = 4
WLX_OPTION_IGNORE_AUTO_LOGON: UInt32 = 8
WLX_OPTION_NO_SWITCH_ON_SAS: UInt32 = 9
WLX_OPTION_SMART_CARD_PRESENT: UInt32 = 65537
WLX_OPTION_SMART_CARD_INFO: UInt32 = 65538
WLX_OPTION_DISPATCH_TABLE_SIZE: UInt32 = 65539
@winfunctype_pointer
def PFNMSGECALLBACK(bVerbose: win32more.Windows.Win32.Foundation.BOOL, lpMessage: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def PWLX_ASSIGN_SHELL_PROTECTION(hWlx: win32more.Windows.Win32.Foundation.HANDLE, hToken: win32more.Windows.Win32.Foundation.HANDLE, hProcess: win32more.Windows.Win32.Foundation.HANDLE, hThread: win32more.Windows.Win32.Foundation.HANDLE) -> Int32: ...
@winfunctype_pointer
def PWLX_CHANGE_PASSWORD_NOTIFY(hWlx: win32more.Windows.Win32.Foundation.HANDLE, pMprInfo: POINTER(win32more.Windows.Win32.Security.WinWlx.WLX_MPR_NOTIFY_INFO), dwChangeInfo: UInt32) -> Int32: ...
@winfunctype_pointer
def PWLX_CHANGE_PASSWORD_NOTIFY_EX(hWlx: win32more.Windows.Win32.Foundation.HANDLE, pMprInfo: POINTER(win32more.Windows.Win32.Security.WinWlx.WLX_MPR_NOTIFY_INFO), dwChangeInfo: UInt32, ProviderName: win32more.Windows.Win32.Foundation.PWSTR, Reserved: VoidPtr) -> Int32: ...
@winfunctype_pointer
def PWLX_CLOSE_USER_DESKTOP(hWlx: win32more.Windows.Win32.Foundation.HANDLE, pDesktop: POINTER(win32more.Windows.Win32.Security.WinWlx.WLX_DESKTOP), hToken: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_CREATE_USER_DESKTOP(hWlx: win32more.Windows.Win32.Foundation.HANDLE, hToken: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32, pszDesktopName: win32more.Windows.Win32.Foundation.PWSTR, ppDesktop: POINTER(POINTER(win32more.Windows.Win32.Security.WinWlx.WLX_DESKTOP))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_DIALOG_BOX(hWlx: win32more.Windows.Win32.Foundation.HANDLE, hInst: win32more.Windows.Win32.Foundation.HANDLE, lpszTemplate: win32more.Windows.Win32.Foundation.PWSTR, hwndOwner: win32more.Windows.Win32.Foundation.HWND, dlgprc: win32more.Windows.Win32.UI.WindowsAndMessaging.DLGPROC) -> Int32: ...
@winfunctype_pointer
def PWLX_DIALOG_BOX_INDIRECT(hWlx: win32more.Windows.Win32.Foundation.HANDLE, hInst: win32more.Windows.Win32.Foundation.HANDLE, hDialogTemplate: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.DLGTEMPLATE), hwndOwner: win32more.Windows.Win32.Foundation.HWND, dlgprc: win32more.Windows.Win32.UI.WindowsAndMessaging.DLGPROC) -> Int32: ...
@winfunctype_pointer
def PWLX_DIALOG_BOX_INDIRECT_PARAM(hWlx: win32more.Windows.Win32.Foundation.HANDLE, hInst: win32more.Windows.Win32.Foundation.HANDLE, hDialogTemplate: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.DLGTEMPLATE), hwndOwner: win32more.Windows.Win32.Foundation.HWND, dlgprc: win32more.Windows.Win32.UI.WindowsAndMessaging.DLGPROC, dwInitParam: win32more.Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype_pointer
def PWLX_DIALOG_BOX_PARAM(hWlx: win32more.Windows.Win32.Foundation.HANDLE, hInst: win32more.Windows.Win32.Foundation.HANDLE, lpszTemplate: win32more.Windows.Win32.Foundation.PWSTR, hwndOwner: win32more.Windows.Win32.Foundation.HWND, dlgprc: win32more.Windows.Win32.UI.WindowsAndMessaging.DLGPROC, dwInitParam: win32more.Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype_pointer
def PWLX_DISCONNECT() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_GET_OPTION(hWlx: win32more.Windows.Win32.Foundation.HANDLE, Option: UInt32, Value: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_GET_SOURCE_DESKTOP(hWlx: win32more.Windows.Win32.Foundation.HANDLE, ppDesktop: POINTER(POINTER(win32more.Windows.Win32.Security.WinWlx.WLX_DESKTOP))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_MESSAGE_BOX(hWlx: win32more.Windows.Win32.Foundation.HANDLE, hwndOwner: win32more.Windows.Win32.Foundation.HWND, lpszText: win32more.Windows.Win32.Foundation.PWSTR, lpszTitle: win32more.Windows.Win32.Foundation.PWSTR, fuStyle: UInt32) -> Int32: ...
@winfunctype_pointer
def PWLX_QUERY_CLIENT_CREDENTIALS(pCred: POINTER(win32more.Windows.Win32.Security.WinWlx.WLX_CLIENT_CREDENTIALS_INFO_V1_0)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_QUERY_CONSOLESWITCH_CREDENTIALS(pCred: POINTER(win32more.Windows.Win32.Security.WinWlx.WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0)) -> UInt32: ...
@winfunctype_pointer
def PWLX_QUERY_IC_CREDENTIALS(pCred: POINTER(win32more.Windows.Win32.Security.WinWlx.WLX_CLIENT_CREDENTIALS_INFO_V1_0)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_QUERY_TERMINAL_SERVICES_DATA(hWlx: win32more.Windows.Win32.Foundation.HANDLE, pTSData: POINTER(win32more.Windows.Win32.Security.WinWlx.WLX_TERMINAL_SERVICES_DATA), UserName: win32more.Windows.Win32.Foundation.PWSTR, Domain: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def PWLX_QUERY_TS_LOGON_CREDENTIALS(pCred: POINTER(win32more.Windows.Win32.Security.WinWlx.WLX_CLIENT_CREDENTIALS_INFO_V2_0)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_SAS_NOTIFY(hWlx: win32more.Windows.Win32.Foundation.HANDLE, dwSasType: UInt32) -> Void: ...
@winfunctype_pointer
def PWLX_SET_CONTEXT_POINTER(hWlx: win32more.Windows.Win32.Foundation.HANDLE, pWlxContext: VoidPtr) -> Void: ...
@winfunctype_pointer
def PWLX_SET_OPTION(hWlx: win32more.Windows.Win32.Foundation.HANDLE, Option: UInt32, Value: UIntPtr, OldValue: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_SET_RETURN_DESKTOP(hWlx: win32more.Windows.Win32.Foundation.HANDLE, pDesktop: POINTER(win32more.Windows.Win32.Security.WinWlx.WLX_DESKTOP)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_SET_TIMEOUT(hWlx: win32more.Windows.Win32.Foundation.HANDLE, Timeout: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_SWITCH_DESKTOP_TO_USER(hWlx: win32more.Windows.Win32.Foundation.HANDLE) -> Int32: ...
@winfunctype_pointer
def PWLX_SWITCH_DESKTOP_TO_WINLOGON(hWlx: win32more.Windows.Win32.Foundation.HANDLE) -> Int32: ...
@winfunctype_pointer
def PWLX_USE_CTRL_ALT_DEL(hWlx: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype_pointer
def PWLX_WIN31_MIGRATE(hWlx: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
class WLX_CLIENT_CREDENTIALS_INFO_V1_0(Structure):
    dwType: UInt32
    pszUserName: win32more.Windows.Win32.Foundation.PWSTR
    pszDomain: win32more.Windows.Win32.Foundation.PWSTR
    pszPassword: win32more.Windows.Win32.Foundation.PWSTR
    fPromptForPassword: win32more.Windows.Win32.Foundation.BOOL
class WLX_CLIENT_CREDENTIALS_INFO_V2_0(Structure):
    dwType: UInt32
    pszUserName: win32more.Windows.Win32.Foundation.PWSTR
    pszDomain: win32more.Windows.Win32.Foundation.PWSTR
    pszPassword: win32more.Windows.Win32.Foundation.PWSTR
    fPromptForPassword: win32more.Windows.Win32.Foundation.BOOL
    fDisconnectOnLogonFailure: win32more.Windows.Win32.Foundation.BOOL
class WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0(Structure):
    dwType: UInt32
    UserToken: win32more.Windows.Win32.Foundation.HANDLE
    LogonId: win32more.Windows.Win32.Foundation.LUID
    Quotas: win32more.Windows.Win32.Security.QUOTA_LIMITS
    UserName: win32more.Windows.Win32.Foundation.PWSTR
    Domain: win32more.Windows.Win32.Foundation.PWSTR
    LogonTime: Int64
    SmartCardLogon: win32more.Windows.Win32.Foundation.BOOL
    ProfileLength: UInt32
    MessageType: UInt32
    LogonCount: UInt16
    BadPasswordCount: UInt16
    ProfileLogonTime: Int64
    LogoffTime: Int64
    KickOffTime: Int64
    PasswordLastSet: Int64
    PasswordCanChange: Int64
    PasswordMustChange: Int64
    LogonScript: win32more.Windows.Win32.Foundation.PWSTR
    HomeDirectory: win32more.Windows.Win32.Foundation.PWSTR
    FullName: win32more.Windows.Win32.Foundation.PWSTR
    ProfilePath: win32more.Windows.Win32.Foundation.PWSTR
    HomeDirectoryDrive: win32more.Windows.Win32.Foundation.PWSTR
    LogonServer: win32more.Windows.Win32.Foundation.PWSTR
    UserFlags: UInt32
    PrivateDataLen: UInt32
    PrivateData: POINTER(Byte)
class WLX_DESKTOP(Structure):
    Size: UInt32
    Flags: UInt32
    hDesktop: win32more.Windows.Win32.System.StationsAndDesktops.HDESK
    pszDesktopName: win32more.Windows.Win32.Foundation.PWSTR
class WLX_DISPATCH_VERSION_1_0(Structure):
    WlxUseCtrlAltDel: win32more.Windows.Win32.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL
    WlxSetContextPointer: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_CONTEXT_POINTER
    WlxSasNotify: win32more.Windows.Win32.Security.WinWlx.PWLX_SAS_NOTIFY
    WlxSetTimeout: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_TIMEOUT
    WlxAssignShellProtection: win32more.Windows.Win32.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION
    WlxMessageBox: win32more.Windows.Win32.Security.WinWlx.PWLX_MESSAGE_BOX
    WlxDialogBox: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX
    WlxDialogBoxParam: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_PARAM
    WlxDialogBoxIndirect: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT
    WlxDialogBoxIndirectParam: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM
    WlxSwitchDesktopToUser: win32more.Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER
    WlxSwitchDesktopToWinlogon: win32more.Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON
    WlxChangePasswordNotify: win32more.Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY
class WLX_DISPATCH_VERSION_1_1(Structure):
    WlxUseCtrlAltDel: win32more.Windows.Win32.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL
    WlxSetContextPointer: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_CONTEXT_POINTER
    WlxSasNotify: win32more.Windows.Win32.Security.WinWlx.PWLX_SAS_NOTIFY
    WlxSetTimeout: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_TIMEOUT
    WlxAssignShellProtection: win32more.Windows.Win32.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION
    WlxMessageBox: win32more.Windows.Win32.Security.WinWlx.PWLX_MESSAGE_BOX
    WlxDialogBox: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX
    WlxDialogBoxParam: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_PARAM
    WlxDialogBoxIndirect: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT
    WlxDialogBoxIndirectParam: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM
    WlxSwitchDesktopToUser: win32more.Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER
    WlxSwitchDesktopToWinlogon: win32more.Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON
    WlxChangePasswordNotify: win32more.Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY
    WlxGetSourceDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_GET_SOURCE_DESKTOP
    WlxSetReturnDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_RETURN_DESKTOP
    WlxCreateUserDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_CREATE_USER_DESKTOP
    WlxChangePasswordNotifyEx: win32more.Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY_EX
class WLX_DISPATCH_VERSION_1_2(Structure):
    WlxUseCtrlAltDel: win32more.Windows.Win32.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL
    WlxSetContextPointer: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_CONTEXT_POINTER
    WlxSasNotify: win32more.Windows.Win32.Security.WinWlx.PWLX_SAS_NOTIFY
    WlxSetTimeout: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_TIMEOUT
    WlxAssignShellProtection: win32more.Windows.Win32.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION
    WlxMessageBox: win32more.Windows.Win32.Security.WinWlx.PWLX_MESSAGE_BOX
    WlxDialogBox: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX
    WlxDialogBoxParam: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_PARAM
    WlxDialogBoxIndirect: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT
    WlxDialogBoxIndirectParam: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM
    WlxSwitchDesktopToUser: win32more.Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER
    WlxSwitchDesktopToWinlogon: win32more.Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON
    WlxChangePasswordNotify: win32more.Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY
    WlxGetSourceDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_GET_SOURCE_DESKTOP
    WlxSetReturnDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_RETURN_DESKTOP
    WlxCreateUserDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_CREATE_USER_DESKTOP
    WlxChangePasswordNotifyEx: win32more.Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY_EX
    WlxCloseUserDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_CLOSE_USER_DESKTOP
class WLX_DISPATCH_VERSION_1_3(Structure):
    WlxUseCtrlAltDel: win32more.Windows.Win32.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL
    WlxSetContextPointer: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_CONTEXT_POINTER
    WlxSasNotify: win32more.Windows.Win32.Security.WinWlx.PWLX_SAS_NOTIFY
    WlxSetTimeout: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_TIMEOUT
    WlxAssignShellProtection: win32more.Windows.Win32.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION
    WlxMessageBox: win32more.Windows.Win32.Security.WinWlx.PWLX_MESSAGE_BOX
    WlxDialogBox: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX
    WlxDialogBoxParam: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_PARAM
    WlxDialogBoxIndirect: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT
    WlxDialogBoxIndirectParam: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM
    WlxSwitchDesktopToUser: win32more.Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER
    WlxSwitchDesktopToWinlogon: win32more.Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON
    WlxChangePasswordNotify: win32more.Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY
    WlxGetSourceDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_GET_SOURCE_DESKTOP
    WlxSetReturnDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_RETURN_DESKTOP
    WlxCreateUserDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_CREATE_USER_DESKTOP
    WlxChangePasswordNotifyEx: win32more.Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY_EX
    WlxCloseUserDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_CLOSE_USER_DESKTOP
    WlxSetOption: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_OPTION
    WlxGetOption: win32more.Windows.Win32.Security.WinWlx.PWLX_GET_OPTION
    WlxWin31Migrate: win32more.Windows.Win32.Security.WinWlx.PWLX_WIN31_MIGRATE
    WlxQueryClientCredentials: win32more.Windows.Win32.Security.WinWlx.PWLX_QUERY_CLIENT_CREDENTIALS
    WlxQueryInetConnectorCredentials: win32more.Windows.Win32.Security.WinWlx.PWLX_QUERY_IC_CREDENTIALS
    WlxDisconnect: win32more.Windows.Win32.Security.WinWlx.PWLX_DISCONNECT
    WlxQueryTerminalServicesData: win32more.Windows.Win32.Security.WinWlx.PWLX_QUERY_TERMINAL_SERVICES_DATA
class WLX_DISPATCH_VERSION_1_4(Structure):
    WlxUseCtrlAltDel: win32more.Windows.Win32.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL
    WlxSetContextPointer: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_CONTEXT_POINTER
    WlxSasNotify: win32more.Windows.Win32.Security.WinWlx.PWLX_SAS_NOTIFY
    WlxSetTimeout: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_TIMEOUT
    WlxAssignShellProtection: win32more.Windows.Win32.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION
    WlxMessageBox: win32more.Windows.Win32.Security.WinWlx.PWLX_MESSAGE_BOX
    WlxDialogBox: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX
    WlxDialogBoxParam: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_PARAM
    WlxDialogBoxIndirect: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT
    WlxDialogBoxIndirectParam: win32more.Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM
    WlxSwitchDesktopToUser: win32more.Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER
    WlxSwitchDesktopToWinlogon: win32more.Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON
    WlxChangePasswordNotify: win32more.Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY
    WlxGetSourceDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_GET_SOURCE_DESKTOP
    WlxSetReturnDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_RETURN_DESKTOP
    WlxCreateUserDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_CREATE_USER_DESKTOP
    WlxChangePasswordNotifyEx: win32more.Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY_EX
    WlxCloseUserDesktop: win32more.Windows.Win32.Security.WinWlx.PWLX_CLOSE_USER_DESKTOP
    WlxSetOption: win32more.Windows.Win32.Security.WinWlx.PWLX_SET_OPTION
    WlxGetOption: win32more.Windows.Win32.Security.WinWlx.PWLX_GET_OPTION
    WlxWin31Migrate: win32more.Windows.Win32.Security.WinWlx.PWLX_WIN31_MIGRATE
    WlxQueryClientCredentials: win32more.Windows.Win32.Security.WinWlx.PWLX_QUERY_CLIENT_CREDENTIALS
    WlxQueryInetConnectorCredentials: win32more.Windows.Win32.Security.WinWlx.PWLX_QUERY_IC_CREDENTIALS
    WlxDisconnect: win32more.Windows.Win32.Security.WinWlx.PWLX_DISCONNECT
    WlxQueryTerminalServicesData: win32more.Windows.Win32.Security.WinWlx.PWLX_QUERY_TERMINAL_SERVICES_DATA
    WlxQueryConsoleSwitchCredentials: win32more.Windows.Win32.Security.WinWlx.PWLX_QUERY_CONSOLESWITCH_CREDENTIALS
    WlxQueryTsLogonCredentials: win32more.Windows.Win32.Security.WinWlx.PWLX_QUERY_TS_LOGON_CREDENTIALS
class WLX_MPR_NOTIFY_INFO(Structure):
    pszUserName: win32more.Windows.Win32.Foundation.PWSTR
    pszDomain: win32more.Windows.Win32.Foundation.PWSTR
    pszPassword: win32more.Windows.Win32.Foundation.PWSTR
    pszOldPassword: win32more.Windows.Win32.Foundation.PWSTR
class WLX_NOTIFICATION_INFO(Structure):
    Size: UInt32
    Flags: UInt32
    UserName: win32more.Windows.Win32.Foundation.PWSTR
    Domain: win32more.Windows.Win32.Foundation.PWSTR
    WindowStation: win32more.Windows.Win32.Foundation.PWSTR
    hToken: win32more.Windows.Win32.Foundation.HANDLE
    hDesktop: win32more.Windows.Win32.System.StationsAndDesktops.HDESK
    pStatusCallback: win32more.Windows.Win32.Security.WinWlx.PFNMSGECALLBACK
class WLX_PROFILE_V1_0(Structure):
    dwType: UInt32
    pszProfile: win32more.Windows.Win32.Foundation.PWSTR
class WLX_PROFILE_V2_0(Structure):
    dwType: UInt32
    pszProfile: win32more.Windows.Win32.Foundation.PWSTR
    pszPolicy: win32more.Windows.Win32.Foundation.PWSTR
    pszNetworkDefaultUserProfile: win32more.Windows.Win32.Foundation.PWSTR
    pszServerName: win32more.Windows.Win32.Foundation.PWSTR
    pszEnvironment: win32more.Windows.Win32.Foundation.PWSTR
class WLX_SC_NOTIFICATION_INFO(Structure):
    pszCard: win32more.Windows.Win32.Foundation.PWSTR
    pszReader: win32more.Windows.Win32.Foundation.PWSTR
    pszContainer: win32more.Windows.Win32.Foundation.PWSTR
    pszCryptoProvider: win32more.Windows.Win32.Foundation.PWSTR
WLX_SHUTDOWN_TYPE = UInt32
WLX_SAS_ACTION_SHUTDOWN: win32more.Windows.Win32.Security.WinWlx.WLX_SHUTDOWN_TYPE = 5
WLX_SAS_ACTION_SHUTDOWN_REBOOT: win32more.Windows.Win32.Security.WinWlx.WLX_SHUTDOWN_TYPE = 11
WLX_SAS_ACTION_SHUTDOWN_POWER_OFF: win32more.Windows.Win32.Security.WinWlx.WLX_SHUTDOWN_TYPE = 10
class WLX_TERMINAL_SERVICES_DATA(Structure):
    ProfilePath: Char * 257
    HomeDir: Char * 257
    HomeDirDrive: Char * 4


make_ready(__name__)
