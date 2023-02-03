from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.Security.WinWlx
import Windows.Win32.System.StationsAndDesktops
import Windows.Win32.UI.WindowsAndMessaging
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
def PFNMSGECALLBACK(bVerbose: Windows.Win32.Foundation.BOOL, lpMessage: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def PWLX_ASSIGN_SHELL_PROTECTION(hWlx: Windows.Win32.Foundation.HANDLE, hToken: Windows.Win32.Foundation.HANDLE, hProcess: Windows.Win32.Foundation.HANDLE, hThread: Windows.Win32.Foundation.HANDLE) -> Int32: ...
@winfunctype_pointer
def PWLX_CHANGE_PASSWORD_NOTIFY(hWlx: Windows.Win32.Foundation.HANDLE, pMprInfo: POINTER(Windows.Win32.Security.WinWlx.WLX_MPR_NOTIFY_INFO_head), dwChangeInfo: UInt32) -> Int32: ...
@winfunctype_pointer
def PWLX_CHANGE_PASSWORD_NOTIFY_EX(hWlx: Windows.Win32.Foundation.HANDLE, pMprInfo: POINTER(Windows.Win32.Security.WinWlx.WLX_MPR_NOTIFY_INFO_head), dwChangeInfo: UInt32, ProviderName: Windows.Win32.Foundation.PWSTR, Reserved: c_void_p) -> Int32: ...
@winfunctype_pointer
def PWLX_CLOSE_USER_DESKTOP(hWlx: Windows.Win32.Foundation.HANDLE, pDesktop: POINTER(Windows.Win32.Security.WinWlx.WLX_DESKTOP_head), hToken: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_CREATE_USER_DESKTOP(hWlx: Windows.Win32.Foundation.HANDLE, hToken: Windows.Win32.Foundation.HANDLE, Flags: UInt32, pszDesktopName: Windows.Win32.Foundation.PWSTR, ppDesktop: POINTER(POINTER(Windows.Win32.Security.WinWlx.WLX_DESKTOP_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_DIALOG_BOX(hWlx: Windows.Win32.Foundation.HANDLE, hInst: Windows.Win32.Foundation.HANDLE, lpszTemplate: Windows.Win32.Foundation.PWSTR, hwndOwner: Windows.Win32.Foundation.HWND, dlgprc: Windows.Win32.UI.WindowsAndMessaging.DLGPROC) -> Int32: ...
@winfunctype_pointer
def PWLX_DIALOG_BOX_INDIRECT(hWlx: Windows.Win32.Foundation.HANDLE, hInst: Windows.Win32.Foundation.HANDLE, hDialogTemplate: POINTER(Windows.Win32.UI.WindowsAndMessaging.DLGTEMPLATE_head), hwndOwner: Windows.Win32.Foundation.HWND, dlgprc: Windows.Win32.UI.WindowsAndMessaging.DLGPROC) -> Int32: ...
@winfunctype_pointer
def PWLX_DIALOG_BOX_INDIRECT_PARAM(hWlx: Windows.Win32.Foundation.HANDLE, hInst: Windows.Win32.Foundation.HANDLE, hDialogTemplate: POINTER(Windows.Win32.UI.WindowsAndMessaging.DLGTEMPLATE_head), hwndOwner: Windows.Win32.Foundation.HWND, dlgprc: Windows.Win32.UI.WindowsAndMessaging.DLGPROC, dwInitParam: Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype_pointer
def PWLX_DIALOG_BOX_PARAM(hWlx: Windows.Win32.Foundation.HANDLE, hInst: Windows.Win32.Foundation.HANDLE, lpszTemplate: Windows.Win32.Foundation.PWSTR, hwndOwner: Windows.Win32.Foundation.HWND, dlgprc: Windows.Win32.UI.WindowsAndMessaging.DLGPROC, dwInitParam: Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype_pointer
def PWLX_DISCONNECT() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_GET_OPTION(hWlx: Windows.Win32.Foundation.HANDLE, Option: UInt32, Value: POINTER(UIntPtr)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_GET_SOURCE_DESKTOP(hWlx: Windows.Win32.Foundation.HANDLE, ppDesktop: POINTER(POINTER(Windows.Win32.Security.WinWlx.WLX_DESKTOP_head))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_MESSAGE_BOX(hWlx: Windows.Win32.Foundation.HANDLE, hwndOwner: Windows.Win32.Foundation.HWND, lpszText: Windows.Win32.Foundation.PWSTR, lpszTitle: Windows.Win32.Foundation.PWSTR, fuStyle: UInt32) -> Int32: ...
@winfunctype_pointer
def PWLX_QUERY_CLIENT_CREDENTIALS(pCred: POINTER(Windows.Win32.Security.WinWlx.WLX_CLIENT_CREDENTIALS_INFO_V1_0_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_QUERY_CONSOLESWITCH_CREDENTIALS(pCred: POINTER(Windows.Win32.Security.WinWlx.WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0_head)) -> UInt32: ...
@winfunctype_pointer
def PWLX_QUERY_IC_CREDENTIALS(pCred: POINTER(Windows.Win32.Security.WinWlx.WLX_CLIENT_CREDENTIALS_INFO_V1_0_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_QUERY_TERMINAL_SERVICES_DATA(hWlx: Windows.Win32.Foundation.HANDLE, pTSData: POINTER(Windows.Win32.Security.WinWlx.WLX_TERMINAL_SERVICES_DATA_head), UserName: Windows.Win32.Foundation.PWSTR, Domain: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def PWLX_QUERY_TS_LOGON_CREDENTIALS(pCred: POINTER(Windows.Win32.Security.WinWlx.WLX_CLIENT_CREDENTIALS_INFO_V2_0_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_SAS_NOTIFY(hWlx: Windows.Win32.Foundation.HANDLE, dwSasType: UInt32) -> Void: ...
@winfunctype_pointer
def PWLX_SET_CONTEXT_POINTER(hWlx: Windows.Win32.Foundation.HANDLE, pWlxContext: c_void_p) -> Void: ...
@winfunctype_pointer
def PWLX_SET_OPTION(hWlx: Windows.Win32.Foundation.HANDLE, Option: UInt32, Value: UIntPtr, OldValue: POINTER(UIntPtr)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_SET_RETURN_DESKTOP(hWlx: Windows.Win32.Foundation.HANDLE, pDesktop: POINTER(Windows.Win32.Security.WinWlx.WLX_DESKTOP_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_SET_TIMEOUT(hWlx: Windows.Win32.Foundation.HANDLE, Timeout: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PWLX_SWITCH_DESKTOP_TO_USER(hWlx: Windows.Win32.Foundation.HANDLE) -> Int32: ...
@winfunctype_pointer
def PWLX_SWITCH_DESKTOP_TO_WINLOGON(hWlx: Windows.Win32.Foundation.HANDLE) -> Int32: ...
@winfunctype_pointer
def PWLX_USE_CTRL_ALT_DEL(hWlx: Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype_pointer
def PWLX_WIN31_MIGRATE(hWlx: Windows.Win32.Foundation.HANDLE) -> Void: ...
class WLX_CLIENT_CREDENTIALS_INFO_V1_0(Structure):
    dwType: UInt32
    pszUserName: Windows.Win32.Foundation.PWSTR
    pszDomain: Windows.Win32.Foundation.PWSTR
    pszPassword: Windows.Win32.Foundation.PWSTR
    fPromptForPassword: Windows.Win32.Foundation.BOOL
class WLX_CLIENT_CREDENTIALS_INFO_V2_0(Structure):
    dwType: UInt32
    pszUserName: Windows.Win32.Foundation.PWSTR
    pszDomain: Windows.Win32.Foundation.PWSTR
    pszPassword: Windows.Win32.Foundation.PWSTR
    fPromptForPassword: Windows.Win32.Foundation.BOOL
    fDisconnectOnLogonFailure: Windows.Win32.Foundation.BOOL
class WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0(Structure):
    dwType: UInt32
    UserToken: Windows.Win32.Foundation.HANDLE
    LogonId: Windows.Win32.Foundation.LUID
    Quotas: Windows.Win32.Security.QUOTA_LIMITS
    UserName: Windows.Win32.Foundation.PWSTR
    Domain: Windows.Win32.Foundation.PWSTR
    LogonTime: Windows.Win32.Foundation.LARGE_INTEGER
    SmartCardLogon: Windows.Win32.Foundation.BOOL
    ProfileLength: UInt32
    MessageType: UInt32
    LogonCount: UInt16
    BadPasswordCount: UInt16
    ProfileLogonTime: Windows.Win32.Foundation.LARGE_INTEGER
    LogoffTime: Windows.Win32.Foundation.LARGE_INTEGER
    KickOffTime: Windows.Win32.Foundation.LARGE_INTEGER
    PasswordLastSet: Windows.Win32.Foundation.LARGE_INTEGER
    PasswordCanChange: Windows.Win32.Foundation.LARGE_INTEGER
    PasswordMustChange: Windows.Win32.Foundation.LARGE_INTEGER
    LogonScript: Windows.Win32.Foundation.PWSTR
    HomeDirectory: Windows.Win32.Foundation.PWSTR
    FullName: Windows.Win32.Foundation.PWSTR
    ProfilePath: Windows.Win32.Foundation.PWSTR
    HomeDirectoryDrive: Windows.Win32.Foundation.PWSTR
    LogonServer: Windows.Win32.Foundation.PWSTR
    UserFlags: UInt32
    PrivateDataLen: UInt32
    PrivateData: c_char_p_no
class WLX_DESKTOP(Structure):
    Size: UInt32
    Flags: UInt32
    hDesktop: Windows.Win32.System.StationsAndDesktops.HDESK
    pszDesktopName: Windows.Win32.Foundation.PWSTR
class WLX_DISPATCH_VERSION_1_0(Structure):
    WlxUseCtrlAltDel: Windows.Win32.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL
    WlxSetContextPointer: Windows.Win32.Security.WinWlx.PWLX_SET_CONTEXT_POINTER
    WlxSasNotify: Windows.Win32.Security.WinWlx.PWLX_SAS_NOTIFY
    WlxSetTimeout: Windows.Win32.Security.WinWlx.PWLX_SET_TIMEOUT
    WlxAssignShellProtection: Windows.Win32.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION
    WlxMessageBox: Windows.Win32.Security.WinWlx.PWLX_MESSAGE_BOX
    WlxDialogBox: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX
    WlxDialogBoxParam: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_PARAM
    WlxDialogBoxIndirect: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT
    WlxDialogBoxIndirectParam: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM
    WlxSwitchDesktopToUser: Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER
    WlxSwitchDesktopToWinlogon: Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON
    WlxChangePasswordNotify: Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY
class WLX_DISPATCH_VERSION_1_1(Structure):
    WlxUseCtrlAltDel: Windows.Win32.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL
    WlxSetContextPointer: Windows.Win32.Security.WinWlx.PWLX_SET_CONTEXT_POINTER
    WlxSasNotify: Windows.Win32.Security.WinWlx.PWLX_SAS_NOTIFY
    WlxSetTimeout: Windows.Win32.Security.WinWlx.PWLX_SET_TIMEOUT
    WlxAssignShellProtection: Windows.Win32.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION
    WlxMessageBox: Windows.Win32.Security.WinWlx.PWLX_MESSAGE_BOX
    WlxDialogBox: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX
    WlxDialogBoxParam: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_PARAM
    WlxDialogBoxIndirect: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT
    WlxDialogBoxIndirectParam: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM
    WlxSwitchDesktopToUser: Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER
    WlxSwitchDesktopToWinlogon: Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON
    WlxChangePasswordNotify: Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY
    WlxGetSourceDesktop: Windows.Win32.Security.WinWlx.PWLX_GET_SOURCE_DESKTOP
    WlxSetReturnDesktop: Windows.Win32.Security.WinWlx.PWLX_SET_RETURN_DESKTOP
    WlxCreateUserDesktop: Windows.Win32.Security.WinWlx.PWLX_CREATE_USER_DESKTOP
    WlxChangePasswordNotifyEx: Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY_EX
class WLX_DISPATCH_VERSION_1_2(Structure):
    WlxUseCtrlAltDel: Windows.Win32.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL
    WlxSetContextPointer: Windows.Win32.Security.WinWlx.PWLX_SET_CONTEXT_POINTER
    WlxSasNotify: Windows.Win32.Security.WinWlx.PWLX_SAS_NOTIFY
    WlxSetTimeout: Windows.Win32.Security.WinWlx.PWLX_SET_TIMEOUT
    WlxAssignShellProtection: Windows.Win32.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION
    WlxMessageBox: Windows.Win32.Security.WinWlx.PWLX_MESSAGE_BOX
    WlxDialogBox: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX
    WlxDialogBoxParam: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_PARAM
    WlxDialogBoxIndirect: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT
    WlxDialogBoxIndirectParam: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM
    WlxSwitchDesktopToUser: Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER
    WlxSwitchDesktopToWinlogon: Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON
    WlxChangePasswordNotify: Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY
    WlxGetSourceDesktop: Windows.Win32.Security.WinWlx.PWLX_GET_SOURCE_DESKTOP
    WlxSetReturnDesktop: Windows.Win32.Security.WinWlx.PWLX_SET_RETURN_DESKTOP
    WlxCreateUserDesktop: Windows.Win32.Security.WinWlx.PWLX_CREATE_USER_DESKTOP
    WlxChangePasswordNotifyEx: Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY_EX
    WlxCloseUserDesktop: Windows.Win32.Security.WinWlx.PWLX_CLOSE_USER_DESKTOP
class WLX_DISPATCH_VERSION_1_3(Structure):
    WlxUseCtrlAltDel: Windows.Win32.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL
    WlxSetContextPointer: Windows.Win32.Security.WinWlx.PWLX_SET_CONTEXT_POINTER
    WlxSasNotify: Windows.Win32.Security.WinWlx.PWLX_SAS_NOTIFY
    WlxSetTimeout: Windows.Win32.Security.WinWlx.PWLX_SET_TIMEOUT
    WlxAssignShellProtection: Windows.Win32.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION
    WlxMessageBox: Windows.Win32.Security.WinWlx.PWLX_MESSAGE_BOX
    WlxDialogBox: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX
    WlxDialogBoxParam: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_PARAM
    WlxDialogBoxIndirect: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT
    WlxDialogBoxIndirectParam: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM
    WlxSwitchDesktopToUser: Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER
    WlxSwitchDesktopToWinlogon: Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON
    WlxChangePasswordNotify: Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY
    WlxGetSourceDesktop: Windows.Win32.Security.WinWlx.PWLX_GET_SOURCE_DESKTOP
    WlxSetReturnDesktop: Windows.Win32.Security.WinWlx.PWLX_SET_RETURN_DESKTOP
    WlxCreateUserDesktop: Windows.Win32.Security.WinWlx.PWLX_CREATE_USER_DESKTOP
    WlxChangePasswordNotifyEx: Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY_EX
    WlxCloseUserDesktop: Windows.Win32.Security.WinWlx.PWLX_CLOSE_USER_DESKTOP
    WlxSetOption: Windows.Win32.Security.WinWlx.PWLX_SET_OPTION
    WlxGetOption: Windows.Win32.Security.WinWlx.PWLX_GET_OPTION
    WlxWin31Migrate: Windows.Win32.Security.WinWlx.PWLX_WIN31_MIGRATE
    WlxQueryClientCredentials: Windows.Win32.Security.WinWlx.PWLX_QUERY_CLIENT_CREDENTIALS
    WlxQueryInetConnectorCredentials: Windows.Win32.Security.WinWlx.PWLX_QUERY_IC_CREDENTIALS
    WlxDisconnect: Windows.Win32.Security.WinWlx.PWLX_DISCONNECT
    WlxQueryTerminalServicesData: Windows.Win32.Security.WinWlx.PWLX_QUERY_TERMINAL_SERVICES_DATA
class WLX_DISPATCH_VERSION_1_4(Structure):
    WlxUseCtrlAltDel: Windows.Win32.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL
    WlxSetContextPointer: Windows.Win32.Security.WinWlx.PWLX_SET_CONTEXT_POINTER
    WlxSasNotify: Windows.Win32.Security.WinWlx.PWLX_SAS_NOTIFY
    WlxSetTimeout: Windows.Win32.Security.WinWlx.PWLX_SET_TIMEOUT
    WlxAssignShellProtection: Windows.Win32.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION
    WlxMessageBox: Windows.Win32.Security.WinWlx.PWLX_MESSAGE_BOX
    WlxDialogBox: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX
    WlxDialogBoxParam: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_PARAM
    WlxDialogBoxIndirect: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT
    WlxDialogBoxIndirectParam: Windows.Win32.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM
    WlxSwitchDesktopToUser: Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER
    WlxSwitchDesktopToWinlogon: Windows.Win32.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON
    WlxChangePasswordNotify: Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY
    WlxGetSourceDesktop: Windows.Win32.Security.WinWlx.PWLX_GET_SOURCE_DESKTOP
    WlxSetReturnDesktop: Windows.Win32.Security.WinWlx.PWLX_SET_RETURN_DESKTOP
    WlxCreateUserDesktop: Windows.Win32.Security.WinWlx.PWLX_CREATE_USER_DESKTOP
    WlxChangePasswordNotifyEx: Windows.Win32.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY_EX
    WlxCloseUserDesktop: Windows.Win32.Security.WinWlx.PWLX_CLOSE_USER_DESKTOP
    WlxSetOption: Windows.Win32.Security.WinWlx.PWLX_SET_OPTION
    WlxGetOption: Windows.Win32.Security.WinWlx.PWLX_GET_OPTION
    WlxWin31Migrate: Windows.Win32.Security.WinWlx.PWLX_WIN31_MIGRATE
    WlxQueryClientCredentials: Windows.Win32.Security.WinWlx.PWLX_QUERY_CLIENT_CREDENTIALS
    WlxQueryInetConnectorCredentials: Windows.Win32.Security.WinWlx.PWLX_QUERY_IC_CREDENTIALS
    WlxDisconnect: Windows.Win32.Security.WinWlx.PWLX_DISCONNECT
    WlxQueryTerminalServicesData: Windows.Win32.Security.WinWlx.PWLX_QUERY_TERMINAL_SERVICES_DATA
    WlxQueryConsoleSwitchCredentials: Windows.Win32.Security.WinWlx.PWLX_QUERY_CONSOLESWITCH_CREDENTIALS
    WlxQueryTsLogonCredentials: Windows.Win32.Security.WinWlx.PWLX_QUERY_TS_LOGON_CREDENTIALS
class WLX_MPR_NOTIFY_INFO(Structure):
    pszUserName: Windows.Win32.Foundation.PWSTR
    pszDomain: Windows.Win32.Foundation.PWSTR
    pszPassword: Windows.Win32.Foundation.PWSTR
    pszOldPassword: Windows.Win32.Foundation.PWSTR
class WLX_NOTIFICATION_INFO(Structure):
    Size: UInt32
    Flags: UInt32
    UserName: Windows.Win32.Foundation.PWSTR
    Domain: Windows.Win32.Foundation.PWSTR
    WindowStation: Windows.Win32.Foundation.PWSTR
    hToken: Windows.Win32.Foundation.HANDLE
    hDesktop: Windows.Win32.System.StationsAndDesktops.HDESK
    pStatusCallback: Windows.Win32.Security.WinWlx.PFNMSGECALLBACK
class WLX_PROFILE_V1_0(Structure):
    dwType: UInt32
    pszProfile: Windows.Win32.Foundation.PWSTR
class WLX_PROFILE_V2_0(Structure):
    dwType: UInt32
    pszProfile: Windows.Win32.Foundation.PWSTR
    pszPolicy: Windows.Win32.Foundation.PWSTR
    pszNetworkDefaultUserProfile: Windows.Win32.Foundation.PWSTR
    pszServerName: Windows.Win32.Foundation.PWSTR
    pszEnvironment: Windows.Win32.Foundation.PWSTR
class WLX_SC_NOTIFICATION_INFO(Structure):
    pszCard: Windows.Win32.Foundation.PWSTR
    pszReader: Windows.Win32.Foundation.PWSTR
    pszContainer: Windows.Win32.Foundation.PWSTR
    pszCryptoProvider: Windows.Win32.Foundation.PWSTR
WLX_SHUTDOWN_TYPE = UInt32
WLX_SAS_ACTION_SHUTDOWN: WLX_SHUTDOWN_TYPE = 5
WLX_SAS_ACTION_SHUTDOWN_REBOOT: WLX_SHUTDOWN_TYPE = 11
WLX_SAS_ACTION_SHUTDOWN_POWER_OFF: WLX_SHUTDOWN_TYPE = 10
class WLX_TERMINAL_SERVICES_DATA(Structure):
    ProfilePath: Char * 257
    HomeDir: Char * 257
    HomeDirDrive: Char * 4
make_head(_module, 'PFNMSGECALLBACK')
make_head(_module, 'PWLX_ASSIGN_SHELL_PROTECTION')
make_head(_module, 'PWLX_CHANGE_PASSWORD_NOTIFY')
make_head(_module, 'PWLX_CHANGE_PASSWORD_NOTIFY_EX')
make_head(_module, 'PWLX_CLOSE_USER_DESKTOP')
make_head(_module, 'PWLX_CREATE_USER_DESKTOP')
make_head(_module, 'PWLX_DIALOG_BOX')
make_head(_module, 'PWLX_DIALOG_BOX_INDIRECT')
make_head(_module, 'PWLX_DIALOG_BOX_INDIRECT_PARAM')
make_head(_module, 'PWLX_DIALOG_BOX_PARAM')
make_head(_module, 'PWLX_DISCONNECT')
make_head(_module, 'PWLX_GET_OPTION')
make_head(_module, 'PWLX_GET_SOURCE_DESKTOP')
make_head(_module, 'PWLX_MESSAGE_BOX')
make_head(_module, 'PWLX_QUERY_CLIENT_CREDENTIALS')
make_head(_module, 'PWLX_QUERY_CONSOLESWITCH_CREDENTIALS')
make_head(_module, 'PWLX_QUERY_IC_CREDENTIALS')
make_head(_module, 'PWLX_QUERY_TERMINAL_SERVICES_DATA')
make_head(_module, 'PWLX_QUERY_TS_LOGON_CREDENTIALS')
make_head(_module, 'PWLX_SAS_NOTIFY')
make_head(_module, 'PWLX_SET_CONTEXT_POINTER')
make_head(_module, 'PWLX_SET_OPTION')
make_head(_module, 'PWLX_SET_RETURN_DESKTOP')
make_head(_module, 'PWLX_SET_TIMEOUT')
make_head(_module, 'PWLX_SWITCH_DESKTOP_TO_USER')
make_head(_module, 'PWLX_SWITCH_DESKTOP_TO_WINLOGON')
make_head(_module, 'PWLX_USE_CTRL_ALT_DEL')
make_head(_module, 'PWLX_WIN31_MIGRATE')
make_head(_module, 'WLX_CLIENT_CREDENTIALS_INFO_V1_0')
make_head(_module, 'WLX_CLIENT_CREDENTIALS_INFO_V2_0')
make_head(_module, 'WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0')
make_head(_module, 'WLX_DESKTOP')
make_head(_module, 'WLX_DISPATCH_VERSION_1_0')
make_head(_module, 'WLX_DISPATCH_VERSION_1_1')
make_head(_module, 'WLX_DISPATCH_VERSION_1_2')
make_head(_module, 'WLX_DISPATCH_VERSION_1_3')
make_head(_module, 'WLX_DISPATCH_VERSION_1_4')
make_head(_module, 'WLX_MPR_NOTIFY_INFO')
make_head(_module, 'WLX_NOTIFICATION_INFO')
make_head(_module, 'WLX_PROFILE_V1_0')
make_head(_module, 'WLX_PROFILE_V2_0')
make_head(_module, 'WLX_SC_NOTIFICATION_INFO')
make_head(_module, 'WLX_TERMINAL_SERVICES_DATA')
__all__ = [
    "PFNMSGECALLBACK",
    "PWLX_ASSIGN_SHELL_PROTECTION",
    "PWLX_CHANGE_PASSWORD_NOTIFY",
    "PWLX_CHANGE_PASSWORD_NOTIFY_EX",
    "PWLX_CLOSE_USER_DESKTOP",
    "PWLX_CREATE_USER_DESKTOP",
    "PWLX_DIALOG_BOX",
    "PWLX_DIALOG_BOX_INDIRECT",
    "PWLX_DIALOG_BOX_INDIRECT_PARAM",
    "PWLX_DIALOG_BOX_PARAM",
    "PWLX_DISCONNECT",
    "PWLX_GET_OPTION",
    "PWLX_GET_SOURCE_DESKTOP",
    "PWLX_MESSAGE_BOX",
    "PWLX_QUERY_CLIENT_CREDENTIALS",
    "PWLX_QUERY_CONSOLESWITCH_CREDENTIALS",
    "PWLX_QUERY_IC_CREDENTIALS",
    "PWLX_QUERY_TERMINAL_SERVICES_DATA",
    "PWLX_QUERY_TS_LOGON_CREDENTIALS",
    "PWLX_SAS_NOTIFY",
    "PWLX_SET_CONTEXT_POINTER",
    "PWLX_SET_OPTION",
    "PWLX_SET_RETURN_DESKTOP",
    "PWLX_SET_TIMEOUT",
    "PWLX_SWITCH_DESKTOP_TO_USER",
    "PWLX_SWITCH_DESKTOP_TO_WINLOGON",
    "PWLX_USE_CTRL_ALT_DEL",
    "PWLX_WIN31_MIGRATE",
    "STATUSMSG_OPTION_NOANIMATION",
    "STATUSMSG_OPTION_SETFOREGROUND",
    "WLX_CLIENT_CREDENTIALS_INFO_V1_0",
    "WLX_CLIENT_CREDENTIALS_INFO_V2_0",
    "WLX_CONSOLESWITCHCREDENTIAL_TYPE_V1_0",
    "WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0",
    "WLX_CREATE_INSTANCE_ONLY",
    "WLX_CREATE_USER",
    "WLX_CREDENTIAL_TYPE_V1_0",
    "WLX_CREDENTIAL_TYPE_V2_0",
    "WLX_CURRENT_VERSION",
    "WLX_DESKTOP",
    "WLX_DESKTOP_HANDLE",
    "WLX_DESKTOP_NAME",
    "WLX_DIRECTORY_LENGTH",
    "WLX_DISPATCH_VERSION_1_0",
    "WLX_DISPATCH_VERSION_1_1",
    "WLX_DISPATCH_VERSION_1_2",
    "WLX_DISPATCH_VERSION_1_3",
    "WLX_DISPATCH_VERSION_1_4",
    "WLX_DLG_INPUT_TIMEOUT",
    "WLX_DLG_SAS",
    "WLX_DLG_SCREEN_SAVER_TIMEOUT",
    "WLX_DLG_USER_LOGOFF",
    "WLX_LOGON_OPT_NO_PROFILE",
    "WLX_MPR_NOTIFY_INFO",
    "WLX_NOTIFICATION_INFO",
    "WLX_OPTION_CONTEXT_POINTER",
    "WLX_OPTION_DISPATCH_TABLE_SIZE",
    "WLX_OPTION_FORCE_LOGOFF_TIME",
    "WLX_OPTION_IGNORE_AUTO_LOGON",
    "WLX_OPTION_NO_SWITCH_ON_SAS",
    "WLX_OPTION_SMART_CARD_INFO",
    "WLX_OPTION_SMART_CARD_PRESENT",
    "WLX_OPTION_USE_CTRL_ALT_DEL",
    "WLX_OPTION_USE_SMART_CARD",
    "WLX_PROFILE_TYPE_V1_0",
    "WLX_PROFILE_TYPE_V2_0",
    "WLX_PROFILE_V1_0",
    "WLX_PROFILE_V2_0",
    "WLX_SAS_ACTION_DELAYED_FORCE_LOGOFF",
    "WLX_SAS_ACTION_FORCE_LOGOFF",
    "WLX_SAS_ACTION_LOCK_WKSTA",
    "WLX_SAS_ACTION_LOGOFF",
    "WLX_SAS_ACTION_LOGON",
    "WLX_SAS_ACTION_NONE",
    "WLX_SAS_ACTION_PWD_CHANGED",
    "WLX_SAS_ACTION_RECONNECTED",
    "WLX_SAS_ACTION_SHUTDOWN",
    "WLX_SAS_ACTION_SHUTDOWN_HIBERNATE",
    "WLX_SAS_ACTION_SHUTDOWN_POWER_OFF",
    "WLX_SAS_ACTION_SHUTDOWN_REBOOT",
    "WLX_SAS_ACTION_SHUTDOWN_SLEEP",
    "WLX_SAS_ACTION_SHUTDOWN_SLEEP2",
    "WLX_SAS_ACTION_SWITCH_CONSOLE",
    "WLX_SAS_ACTION_TASKLIST",
    "WLX_SAS_ACTION_UNLOCK_WKSTA",
    "WLX_SAS_TYPE_AUTHENTICATED",
    "WLX_SAS_TYPE_CTRL_ALT_DEL",
    "WLX_SAS_TYPE_MAX_MSFT_VALUE",
    "WLX_SAS_TYPE_SCRNSVR_ACTIVITY",
    "WLX_SAS_TYPE_SCRNSVR_TIMEOUT",
    "WLX_SAS_TYPE_SC_FIRST_READER_ARRIVED",
    "WLX_SAS_TYPE_SC_INSERT",
    "WLX_SAS_TYPE_SC_LAST_READER_REMOVED",
    "WLX_SAS_TYPE_SC_REMOVE",
    "WLX_SAS_TYPE_SWITCHUSER",
    "WLX_SAS_TYPE_TIMEOUT",
    "WLX_SAS_TYPE_USER_LOGOFF",
    "WLX_SC_NOTIFICATION_INFO",
    "WLX_SHUTDOWN_TYPE",
    "WLX_TERMINAL_SERVICES_DATA",
    "WLX_VERSION_1_0",
    "WLX_VERSION_1_1",
    "WLX_VERSION_1_2",
    "WLX_VERSION_1_3",
    "WLX_VERSION_1_4",
    "WLX_WM_SAS",
]
_arch_optional = [
]
