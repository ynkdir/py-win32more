from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.Security.WinWlx
import win32more.System.StationsAndDesktops
import win32more.UI.WindowsAndMessaging

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
WLX_VERSION_1_0 = 65536
WLX_VERSION_1_1 = 65537
WLX_VERSION_1_2 = 65538
WLX_VERSION_1_3 = 65539
WLX_VERSION_1_4 = 65540
WLX_CURRENT_VERSION = 65540
WLX_SAS_TYPE_TIMEOUT = 0
WLX_SAS_TYPE_CTRL_ALT_DEL = 1
WLX_SAS_TYPE_SCRNSVR_TIMEOUT = 2
WLX_SAS_TYPE_SCRNSVR_ACTIVITY = 3
WLX_SAS_TYPE_USER_LOGOFF = 4
WLX_SAS_TYPE_SC_INSERT = 5
WLX_SAS_TYPE_SC_REMOVE = 6
WLX_SAS_TYPE_AUTHENTICATED = 7
WLX_SAS_TYPE_SC_FIRST_READER_ARRIVED = 8
WLX_SAS_TYPE_SC_LAST_READER_REMOVED = 9
WLX_SAS_TYPE_SWITCHUSER = 10
WLX_SAS_TYPE_MAX_MSFT_VALUE = 127
WLX_LOGON_OPT_NO_PROFILE = 1
WLX_PROFILE_TYPE_V1_0 = 1
WLX_PROFILE_TYPE_V2_0 = 2
WLX_SAS_ACTION_LOGON = 1
WLX_SAS_ACTION_NONE = 2
WLX_SAS_ACTION_LOCK_WKSTA = 3
WLX_SAS_ACTION_LOGOFF = 4
WLX_SAS_ACTION_PWD_CHANGED = 6
WLX_SAS_ACTION_TASKLIST = 7
WLX_SAS_ACTION_UNLOCK_WKSTA = 8
WLX_SAS_ACTION_FORCE_LOGOFF = 9
WLX_SAS_ACTION_SHUTDOWN_SLEEP = 12
WLX_SAS_ACTION_SHUTDOWN_SLEEP2 = 13
WLX_SAS_ACTION_SHUTDOWN_HIBERNATE = 14
WLX_SAS_ACTION_RECONNECTED = 15
WLX_SAS_ACTION_DELAYED_FORCE_LOGOFF = 16
WLX_SAS_ACTION_SWITCH_CONSOLE = 17
WLX_WM_SAS = 1625
WLX_DLG_SAS = 101
WLX_DLG_INPUT_TIMEOUT = 102
WLX_DLG_SCREEN_SAVER_TIMEOUT = 103
WLX_DLG_USER_LOGOFF = 104
WLX_DIRECTORY_LENGTH = 256
WLX_CREDENTIAL_TYPE_V1_0 = 1
WLX_CREDENTIAL_TYPE_V2_0 = 2
WLX_CONSOLESWITCHCREDENTIAL_TYPE_V1_0 = 1
STATUSMSG_OPTION_NOANIMATION = 1
STATUSMSG_OPTION_SETFOREGROUND = 2
WLX_DESKTOP_NAME = 1
WLX_DESKTOP_HANDLE = 2
WLX_CREATE_INSTANCE_ONLY = 1
WLX_CREATE_USER = 2
WLX_OPTION_USE_CTRL_ALT_DEL = 1
WLX_OPTION_CONTEXT_POINTER = 2
WLX_OPTION_USE_SMART_CARD = 3
WLX_OPTION_FORCE_LOGOFF_TIME = 4
WLX_OPTION_IGNORE_AUTO_LOGON = 8
WLX_OPTION_NO_SWITCH_ON_SAS = 9
WLX_OPTION_SMART_CARD_PRESENT = 65537
WLX_OPTION_SMART_CARD_INFO = 65538
WLX_OPTION_DISPATCH_TABLE_SIZE = 65539
WLX_SHUTDOWN_TYPE = UInt32
WLX_SAS_ACTION_SHUTDOWN = 5
WLX_SAS_ACTION_SHUTDOWN_REBOOT = 11
WLX_SAS_ACTION_SHUTDOWN_POWER_OFF = 10
def _define_WLX_SC_NOTIFICATION_INFO_head():
    class WLX_SC_NOTIFICATION_INFO(Structure):
        pass
    return WLX_SC_NOTIFICATION_INFO
def _define_WLX_SC_NOTIFICATION_INFO():
    WLX_SC_NOTIFICATION_INFO = win32more.Security.WinWlx.WLX_SC_NOTIFICATION_INFO_head
    WLX_SC_NOTIFICATION_INFO._fields_ = [
        ("pszCard", win32more.Foundation.PWSTR),
        ("pszReader", win32more.Foundation.PWSTR),
        ("pszContainer", win32more.Foundation.PWSTR),
        ("pszCryptoProvider", win32more.Foundation.PWSTR),
    ]
    return WLX_SC_NOTIFICATION_INFO
def _define_WLX_PROFILE_V1_0_head():
    class WLX_PROFILE_V1_0(Structure):
        pass
    return WLX_PROFILE_V1_0
def _define_WLX_PROFILE_V1_0():
    WLX_PROFILE_V1_0 = win32more.Security.WinWlx.WLX_PROFILE_V1_0_head
    WLX_PROFILE_V1_0._fields_ = [
        ("dwType", UInt32),
        ("pszProfile", win32more.Foundation.PWSTR),
    ]
    return WLX_PROFILE_V1_0
def _define_WLX_PROFILE_V2_0_head():
    class WLX_PROFILE_V2_0(Structure):
        pass
    return WLX_PROFILE_V2_0
def _define_WLX_PROFILE_V2_0():
    WLX_PROFILE_V2_0 = win32more.Security.WinWlx.WLX_PROFILE_V2_0_head
    WLX_PROFILE_V2_0._fields_ = [
        ("dwType", UInt32),
        ("pszProfile", win32more.Foundation.PWSTR),
        ("pszPolicy", win32more.Foundation.PWSTR),
        ("pszNetworkDefaultUserProfile", win32more.Foundation.PWSTR),
        ("pszServerName", win32more.Foundation.PWSTR),
        ("pszEnvironment", win32more.Foundation.PWSTR),
    ]
    return WLX_PROFILE_V2_0
def _define_WLX_MPR_NOTIFY_INFO_head():
    class WLX_MPR_NOTIFY_INFO(Structure):
        pass
    return WLX_MPR_NOTIFY_INFO
def _define_WLX_MPR_NOTIFY_INFO():
    WLX_MPR_NOTIFY_INFO = win32more.Security.WinWlx.WLX_MPR_NOTIFY_INFO_head
    WLX_MPR_NOTIFY_INFO._fields_ = [
        ("pszUserName", win32more.Foundation.PWSTR),
        ("pszDomain", win32more.Foundation.PWSTR),
        ("pszPassword", win32more.Foundation.PWSTR),
        ("pszOldPassword", win32more.Foundation.PWSTR),
    ]
    return WLX_MPR_NOTIFY_INFO
def _define_WLX_TERMINAL_SERVICES_DATA_head():
    class WLX_TERMINAL_SERVICES_DATA(Structure):
        pass
    return WLX_TERMINAL_SERVICES_DATA
def _define_WLX_TERMINAL_SERVICES_DATA():
    WLX_TERMINAL_SERVICES_DATA = win32more.Security.WinWlx.WLX_TERMINAL_SERVICES_DATA_head
    WLX_TERMINAL_SERVICES_DATA._fields_ = [
        ("ProfilePath", Char * 257),
        ("HomeDir", Char * 257),
        ("HomeDirDrive", Char * 4),
    ]
    return WLX_TERMINAL_SERVICES_DATA
def _define_WLX_CLIENT_CREDENTIALS_INFO_V1_0_head():
    class WLX_CLIENT_CREDENTIALS_INFO_V1_0(Structure):
        pass
    return WLX_CLIENT_CREDENTIALS_INFO_V1_0
def _define_WLX_CLIENT_CREDENTIALS_INFO_V1_0():
    WLX_CLIENT_CREDENTIALS_INFO_V1_0 = win32more.Security.WinWlx.WLX_CLIENT_CREDENTIALS_INFO_V1_0_head
    WLX_CLIENT_CREDENTIALS_INFO_V1_0._fields_ = [
        ("dwType", UInt32),
        ("pszUserName", win32more.Foundation.PWSTR),
        ("pszDomain", win32more.Foundation.PWSTR),
        ("pszPassword", win32more.Foundation.PWSTR),
        ("fPromptForPassword", win32more.Foundation.BOOL),
    ]
    return WLX_CLIENT_CREDENTIALS_INFO_V1_0
def _define_WLX_CLIENT_CREDENTIALS_INFO_V2_0_head():
    class WLX_CLIENT_CREDENTIALS_INFO_V2_0(Structure):
        pass
    return WLX_CLIENT_CREDENTIALS_INFO_V2_0
def _define_WLX_CLIENT_CREDENTIALS_INFO_V2_0():
    WLX_CLIENT_CREDENTIALS_INFO_V2_0 = win32more.Security.WinWlx.WLX_CLIENT_CREDENTIALS_INFO_V2_0_head
    WLX_CLIENT_CREDENTIALS_INFO_V2_0._fields_ = [
        ("dwType", UInt32),
        ("pszUserName", win32more.Foundation.PWSTR),
        ("pszDomain", win32more.Foundation.PWSTR),
        ("pszPassword", win32more.Foundation.PWSTR),
        ("fPromptForPassword", win32more.Foundation.BOOL),
        ("fDisconnectOnLogonFailure", win32more.Foundation.BOOL),
    ]
    return WLX_CLIENT_CREDENTIALS_INFO_V2_0
def _define_WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0_head():
    class WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0(Structure):
        pass
    return WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0
def _define_WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0():
    WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0 = win32more.Security.WinWlx.WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0_head
    WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0._fields_ = [
        ("dwType", UInt32),
        ("UserToken", win32more.Foundation.HANDLE),
        ("LogonId", win32more.Foundation.LUID),
        ("Quotas", win32more.Security.QUOTA_LIMITS),
        ("UserName", win32more.Foundation.PWSTR),
        ("Domain", win32more.Foundation.PWSTR),
        ("LogonTime", win32more.Foundation.LARGE_INTEGER),
        ("SmartCardLogon", win32more.Foundation.BOOL),
        ("ProfileLength", UInt32),
        ("MessageType", UInt32),
        ("LogonCount", UInt16),
        ("BadPasswordCount", UInt16),
        ("ProfileLogonTime", win32more.Foundation.LARGE_INTEGER),
        ("LogoffTime", win32more.Foundation.LARGE_INTEGER),
        ("KickOffTime", win32more.Foundation.LARGE_INTEGER),
        ("PasswordLastSet", win32more.Foundation.LARGE_INTEGER),
        ("PasswordCanChange", win32more.Foundation.LARGE_INTEGER),
        ("PasswordMustChange", win32more.Foundation.LARGE_INTEGER),
        ("LogonScript", win32more.Foundation.PWSTR),
        ("HomeDirectory", win32more.Foundation.PWSTR),
        ("FullName", win32more.Foundation.PWSTR),
        ("ProfilePath", win32more.Foundation.PWSTR),
        ("HomeDirectoryDrive", win32more.Foundation.PWSTR),
        ("LogonServer", win32more.Foundation.PWSTR),
        ("UserFlags", UInt32),
        ("PrivateDataLen", UInt32),
        ("PrivateData", c_char_p_no),
    ]
    return WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0
def _define_WLX_DESKTOP_head():
    class WLX_DESKTOP(Structure):
        pass
    return WLX_DESKTOP
def _define_WLX_DESKTOP():
    WLX_DESKTOP = win32more.Security.WinWlx.WLX_DESKTOP_head
    WLX_DESKTOP._fields_ = [
        ("Size", UInt32),
        ("Flags", UInt32),
        ("hDesktop", win32more.System.StationsAndDesktops.HDESK),
        ("pszDesktopName", win32more.Foundation.PWSTR),
    ]
    return WLX_DESKTOP
def _define_PWLX_USE_CTRL_ALT_DEL():
    return CFUNCTYPE(Void,win32more.Foundation.HANDLE, use_last_error=False)
def _define_PWLX_SET_CONTEXT_POINTER():
    return CFUNCTYPE(Void,win32more.Foundation.HANDLE,c_void_p, use_last_error=False)
def _define_PWLX_SAS_NOTIFY():
    return CFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32, use_last_error=False)
def _define_PWLX_SET_TIMEOUT():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32, use_last_error=False)
def _define_PWLX_ASSIGN_SHELL_PROTECTION():
    return CFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE, use_last_error=False)
def _define_PWLX_MESSAGE_BOX():
    return CFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)
def _define_PWLX_DIALOG_BOX():
    return CFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.HWND,win32more.UI.WindowsAndMessaging.DLGPROC, use_last_error=False)
def _define_PWLX_DIALOG_BOX_INDIRECT():
    return CFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.UI.WindowsAndMessaging.DLGTEMPLATE_head),win32more.Foundation.HWND,win32more.UI.WindowsAndMessaging.DLGPROC, use_last_error=False)
def _define_PWLX_DIALOG_BOX_PARAM():
    return CFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.HWND,win32more.UI.WindowsAndMessaging.DLGPROC,win32more.Foundation.LPARAM, use_last_error=False)
def _define_PWLX_DIALOG_BOX_INDIRECT_PARAM():
    return CFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.UI.WindowsAndMessaging.DLGTEMPLATE_head),win32more.Foundation.HWND,win32more.UI.WindowsAndMessaging.DLGPROC,win32more.Foundation.LPARAM, use_last_error=False)
def _define_PWLX_SWITCH_DESKTOP_TO_USER():
    return CFUNCTYPE(Int32,win32more.Foundation.HANDLE, use_last_error=False)
def _define_PWLX_SWITCH_DESKTOP_TO_WINLOGON():
    return CFUNCTYPE(Int32,win32more.Foundation.HANDLE, use_last_error=False)
def _define_PWLX_CHANGE_PASSWORD_NOTIFY():
    return CFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(win32more.Security.WinWlx.WLX_MPR_NOTIFY_INFO_head),UInt32, use_last_error=False)
def _define_PWLX_GET_SOURCE_DESKTOP():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(POINTER(win32more.Security.WinWlx.WLX_DESKTOP_head)), use_last_error=False)
def _define_PWLX_SET_RETURN_DESKTOP():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Security.WinWlx.WLX_DESKTOP_head), use_last_error=False)
def _define_PWLX_CREATE_USER_DESKTOP():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Security.WinWlx.WLX_DESKTOP_head)), use_last_error=False)
def _define_PWLX_CHANGE_PASSWORD_NOTIFY_EX():
    return CFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(win32more.Security.WinWlx.WLX_MPR_NOTIFY_INFO_head),UInt32,win32more.Foundation.PWSTR,c_void_p, use_last_error=False)
def _define_PWLX_CLOSE_USER_DESKTOP():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Security.WinWlx.WLX_DESKTOP_head),win32more.Foundation.HANDLE, use_last_error=False)
def _define_PWLX_SET_OPTION():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UIntPtr,POINTER(UIntPtr), use_last_error=False)
def _define_PWLX_GET_OPTION():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(UIntPtr), use_last_error=False)
def _define_PWLX_WIN31_MIGRATE():
    return CFUNCTYPE(Void,win32more.Foundation.HANDLE, use_last_error=False)
def _define_PWLX_QUERY_CLIENT_CREDENTIALS():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.WinWlx.WLX_CLIENT_CREDENTIALS_INFO_V1_0_head), use_last_error=False)
def _define_PWLX_QUERY_IC_CREDENTIALS():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.WinWlx.WLX_CLIENT_CREDENTIALS_INFO_V1_0_head), use_last_error=False)
def _define_PWLX_QUERY_TS_LOGON_CREDENTIALS():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Security.WinWlx.WLX_CLIENT_CREDENTIALS_INFO_V2_0_head), use_last_error=False)
def _define_PWLX_DISCONNECT():
    return CFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)
def _define_PWLX_QUERY_TERMINAL_SERVICES_DATA():
    return CFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Security.WinWlx.WLX_TERMINAL_SERVICES_DATA_head),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)
def _define_PWLX_QUERY_CONSOLESWITCH_CREDENTIALS():
    return CFUNCTYPE(UInt32,POINTER(win32more.Security.WinWlx.WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0_head), use_last_error=False)
def _define_WLX_DISPATCH_VERSION_1_0_head():
    class WLX_DISPATCH_VERSION_1_0(Structure):
        pass
    return WLX_DISPATCH_VERSION_1_0
def _define_WLX_DISPATCH_VERSION_1_0():
    WLX_DISPATCH_VERSION_1_0 = win32more.Security.WinWlx.WLX_DISPATCH_VERSION_1_0_head
    WLX_DISPATCH_VERSION_1_0._fields_ = [
        ("WlxUseCtrlAltDel", win32more.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL),
        ("WlxSetContextPointer", win32more.Security.WinWlx.PWLX_SET_CONTEXT_POINTER),
        ("WlxSasNotify", win32more.Security.WinWlx.PWLX_SAS_NOTIFY),
        ("WlxSetTimeout", win32more.Security.WinWlx.PWLX_SET_TIMEOUT),
        ("WlxAssignShellProtection", win32more.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION),
        ("WlxMessageBox", win32more.Security.WinWlx.PWLX_MESSAGE_BOX),
        ("WlxDialogBox", win32more.Security.WinWlx.PWLX_DIALOG_BOX),
        ("WlxDialogBoxParam", win32more.Security.WinWlx.PWLX_DIALOG_BOX_PARAM),
        ("WlxDialogBoxIndirect", win32more.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT),
        ("WlxDialogBoxIndirectParam", win32more.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM),
        ("WlxSwitchDesktopToUser", win32more.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER),
        ("WlxSwitchDesktopToWinlogon", win32more.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON),
        ("WlxChangePasswordNotify", win32more.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY),
    ]
    return WLX_DISPATCH_VERSION_1_0
def _define_WLX_DISPATCH_VERSION_1_1_head():
    class WLX_DISPATCH_VERSION_1_1(Structure):
        pass
    return WLX_DISPATCH_VERSION_1_1
def _define_WLX_DISPATCH_VERSION_1_1():
    WLX_DISPATCH_VERSION_1_1 = win32more.Security.WinWlx.WLX_DISPATCH_VERSION_1_1_head
    WLX_DISPATCH_VERSION_1_1._fields_ = [
        ("WlxUseCtrlAltDel", win32more.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL),
        ("WlxSetContextPointer", win32more.Security.WinWlx.PWLX_SET_CONTEXT_POINTER),
        ("WlxSasNotify", win32more.Security.WinWlx.PWLX_SAS_NOTIFY),
        ("WlxSetTimeout", win32more.Security.WinWlx.PWLX_SET_TIMEOUT),
        ("WlxAssignShellProtection", win32more.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION),
        ("WlxMessageBox", win32more.Security.WinWlx.PWLX_MESSAGE_BOX),
        ("WlxDialogBox", win32more.Security.WinWlx.PWLX_DIALOG_BOX),
        ("WlxDialogBoxParam", win32more.Security.WinWlx.PWLX_DIALOG_BOX_PARAM),
        ("WlxDialogBoxIndirect", win32more.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT),
        ("WlxDialogBoxIndirectParam", win32more.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM),
        ("WlxSwitchDesktopToUser", win32more.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER),
        ("WlxSwitchDesktopToWinlogon", win32more.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON),
        ("WlxChangePasswordNotify", win32more.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY),
        ("WlxGetSourceDesktop", win32more.Security.WinWlx.PWLX_GET_SOURCE_DESKTOP),
        ("WlxSetReturnDesktop", win32more.Security.WinWlx.PWLX_SET_RETURN_DESKTOP),
        ("WlxCreateUserDesktop", win32more.Security.WinWlx.PWLX_CREATE_USER_DESKTOP),
        ("WlxChangePasswordNotifyEx", win32more.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY_EX),
    ]
    return WLX_DISPATCH_VERSION_1_1
def _define_WLX_DISPATCH_VERSION_1_2_head():
    class WLX_DISPATCH_VERSION_1_2(Structure):
        pass
    return WLX_DISPATCH_VERSION_1_2
def _define_WLX_DISPATCH_VERSION_1_2():
    WLX_DISPATCH_VERSION_1_2 = win32more.Security.WinWlx.WLX_DISPATCH_VERSION_1_2_head
    WLX_DISPATCH_VERSION_1_2._fields_ = [
        ("WlxUseCtrlAltDel", win32more.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL),
        ("WlxSetContextPointer", win32more.Security.WinWlx.PWLX_SET_CONTEXT_POINTER),
        ("WlxSasNotify", win32more.Security.WinWlx.PWLX_SAS_NOTIFY),
        ("WlxSetTimeout", win32more.Security.WinWlx.PWLX_SET_TIMEOUT),
        ("WlxAssignShellProtection", win32more.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION),
        ("WlxMessageBox", win32more.Security.WinWlx.PWLX_MESSAGE_BOX),
        ("WlxDialogBox", win32more.Security.WinWlx.PWLX_DIALOG_BOX),
        ("WlxDialogBoxParam", win32more.Security.WinWlx.PWLX_DIALOG_BOX_PARAM),
        ("WlxDialogBoxIndirect", win32more.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT),
        ("WlxDialogBoxIndirectParam", win32more.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM),
        ("WlxSwitchDesktopToUser", win32more.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER),
        ("WlxSwitchDesktopToWinlogon", win32more.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON),
        ("WlxChangePasswordNotify", win32more.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY),
        ("WlxGetSourceDesktop", win32more.Security.WinWlx.PWLX_GET_SOURCE_DESKTOP),
        ("WlxSetReturnDesktop", win32more.Security.WinWlx.PWLX_SET_RETURN_DESKTOP),
        ("WlxCreateUserDesktop", win32more.Security.WinWlx.PWLX_CREATE_USER_DESKTOP),
        ("WlxChangePasswordNotifyEx", win32more.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY_EX),
        ("WlxCloseUserDesktop", win32more.Security.WinWlx.PWLX_CLOSE_USER_DESKTOP),
    ]
    return WLX_DISPATCH_VERSION_1_2
def _define_WLX_DISPATCH_VERSION_1_3_head():
    class WLX_DISPATCH_VERSION_1_3(Structure):
        pass
    return WLX_DISPATCH_VERSION_1_3
def _define_WLX_DISPATCH_VERSION_1_3():
    WLX_DISPATCH_VERSION_1_3 = win32more.Security.WinWlx.WLX_DISPATCH_VERSION_1_3_head
    WLX_DISPATCH_VERSION_1_3._fields_ = [
        ("WlxUseCtrlAltDel", win32more.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL),
        ("WlxSetContextPointer", win32more.Security.WinWlx.PWLX_SET_CONTEXT_POINTER),
        ("WlxSasNotify", win32more.Security.WinWlx.PWLX_SAS_NOTIFY),
        ("WlxSetTimeout", win32more.Security.WinWlx.PWLX_SET_TIMEOUT),
        ("WlxAssignShellProtection", win32more.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION),
        ("WlxMessageBox", win32more.Security.WinWlx.PWLX_MESSAGE_BOX),
        ("WlxDialogBox", win32more.Security.WinWlx.PWLX_DIALOG_BOX),
        ("WlxDialogBoxParam", win32more.Security.WinWlx.PWLX_DIALOG_BOX_PARAM),
        ("WlxDialogBoxIndirect", win32more.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT),
        ("WlxDialogBoxIndirectParam", win32more.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM),
        ("WlxSwitchDesktopToUser", win32more.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER),
        ("WlxSwitchDesktopToWinlogon", win32more.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON),
        ("WlxChangePasswordNotify", win32more.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY),
        ("WlxGetSourceDesktop", win32more.Security.WinWlx.PWLX_GET_SOURCE_DESKTOP),
        ("WlxSetReturnDesktop", win32more.Security.WinWlx.PWLX_SET_RETURN_DESKTOP),
        ("WlxCreateUserDesktop", win32more.Security.WinWlx.PWLX_CREATE_USER_DESKTOP),
        ("WlxChangePasswordNotifyEx", win32more.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY_EX),
        ("WlxCloseUserDesktop", win32more.Security.WinWlx.PWLX_CLOSE_USER_DESKTOP),
        ("WlxSetOption", win32more.Security.WinWlx.PWLX_SET_OPTION),
        ("WlxGetOption", win32more.Security.WinWlx.PWLX_GET_OPTION),
        ("WlxWin31Migrate", win32more.Security.WinWlx.PWLX_WIN31_MIGRATE),
        ("WlxQueryClientCredentials", win32more.Security.WinWlx.PWLX_QUERY_CLIENT_CREDENTIALS),
        ("WlxQueryInetConnectorCredentials", win32more.Security.WinWlx.PWLX_QUERY_IC_CREDENTIALS),
        ("WlxDisconnect", win32more.Security.WinWlx.PWLX_DISCONNECT),
        ("WlxQueryTerminalServicesData", win32more.Security.WinWlx.PWLX_QUERY_TERMINAL_SERVICES_DATA),
    ]
    return WLX_DISPATCH_VERSION_1_3
def _define_WLX_DISPATCH_VERSION_1_4_head():
    class WLX_DISPATCH_VERSION_1_4(Structure):
        pass
    return WLX_DISPATCH_VERSION_1_4
def _define_WLX_DISPATCH_VERSION_1_4():
    WLX_DISPATCH_VERSION_1_4 = win32more.Security.WinWlx.WLX_DISPATCH_VERSION_1_4_head
    WLX_DISPATCH_VERSION_1_4._fields_ = [
        ("WlxUseCtrlAltDel", win32more.Security.WinWlx.PWLX_USE_CTRL_ALT_DEL),
        ("WlxSetContextPointer", win32more.Security.WinWlx.PWLX_SET_CONTEXT_POINTER),
        ("WlxSasNotify", win32more.Security.WinWlx.PWLX_SAS_NOTIFY),
        ("WlxSetTimeout", win32more.Security.WinWlx.PWLX_SET_TIMEOUT),
        ("WlxAssignShellProtection", win32more.Security.WinWlx.PWLX_ASSIGN_SHELL_PROTECTION),
        ("WlxMessageBox", win32more.Security.WinWlx.PWLX_MESSAGE_BOX),
        ("WlxDialogBox", win32more.Security.WinWlx.PWLX_DIALOG_BOX),
        ("WlxDialogBoxParam", win32more.Security.WinWlx.PWLX_DIALOG_BOX_PARAM),
        ("WlxDialogBoxIndirect", win32more.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT),
        ("WlxDialogBoxIndirectParam", win32more.Security.WinWlx.PWLX_DIALOG_BOX_INDIRECT_PARAM),
        ("WlxSwitchDesktopToUser", win32more.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_USER),
        ("WlxSwitchDesktopToWinlogon", win32more.Security.WinWlx.PWLX_SWITCH_DESKTOP_TO_WINLOGON),
        ("WlxChangePasswordNotify", win32more.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY),
        ("WlxGetSourceDesktop", win32more.Security.WinWlx.PWLX_GET_SOURCE_DESKTOP),
        ("WlxSetReturnDesktop", win32more.Security.WinWlx.PWLX_SET_RETURN_DESKTOP),
        ("WlxCreateUserDesktop", win32more.Security.WinWlx.PWLX_CREATE_USER_DESKTOP),
        ("WlxChangePasswordNotifyEx", win32more.Security.WinWlx.PWLX_CHANGE_PASSWORD_NOTIFY_EX),
        ("WlxCloseUserDesktop", win32more.Security.WinWlx.PWLX_CLOSE_USER_DESKTOP),
        ("WlxSetOption", win32more.Security.WinWlx.PWLX_SET_OPTION),
        ("WlxGetOption", win32more.Security.WinWlx.PWLX_GET_OPTION),
        ("WlxWin31Migrate", win32more.Security.WinWlx.PWLX_WIN31_MIGRATE),
        ("WlxQueryClientCredentials", win32more.Security.WinWlx.PWLX_QUERY_CLIENT_CREDENTIALS),
        ("WlxQueryInetConnectorCredentials", win32more.Security.WinWlx.PWLX_QUERY_IC_CREDENTIALS),
        ("WlxDisconnect", win32more.Security.WinWlx.PWLX_DISCONNECT),
        ("WlxQueryTerminalServicesData", win32more.Security.WinWlx.PWLX_QUERY_TERMINAL_SERVICES_DATA),
        ("WlxQueryConsoleSwitchCredentials", win32more.Security.WinWlx.PWLX_QUERY_CONSOLESWITCH_CREDENTIALS),
        ("WlxQueryTsLogonCredentials", win32more.Security.WinWlx.PWLX_QUERY_TS_LOGON_CREDENTIALS),
    ]
    return WLX_DISPATCH_VERSION_1_4
def _define_PFNMSGECALLBACK():
    return CFUNCTYPE(UInt32,win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=False)
def _define_WLX_NOTIFICATION_INFO_head():
    class WLX_NOTIFICATION_INFO(Structure):
        pass
    return WLX_NOTIFICATION_INFO
def _define_WLX_NOTIFICATION_INFO():
    WLX_NOTIFICATION_INFO = win32more.Security.WinWlx.WLX_NOTIFICATION_INFO_head
    WLX_NOTIFICATION_INFO._fields_ = [
        ("Size", UInt32),
        ("Flags", UInt32),
        ("UserName", win32more.Foundation.PWSTR),
        ("Domain", win32more.Foundation.PWSTR),
        ("WindowStation", win32more.Foundation.PWSTR),
        ("hToken", win32more.Foundation.HANDLE),
        ("hDesktop", win32more.System.StationsAndDesktops.HDESK),
        ("pStatusCallback", win32more.Security.WinWlx.PFNMSGECALLBACK),
    ]
    return WLX_NOTIFICATION_INFO
__all__ = [
    "WLX_VERSION_1_0",
    "WLX_VERSION_1_1",
    "WLX_VERSION_1_2",
    "WLX_VERSION_1_3",
    "WLX_VERSION_1_4",
    "WLX_CURRENT_VERSION",
    "WLX_SAS_TYPE_TIMEOUT",
    "WLX_SAS_TYPE_CTRL_ALT_DEL",
    "WLX_SAS_TYPE_SCRNSVR_TIMEOUT",
    "WLX_SAS_TYPE_SCRNSVR_ACTIVITY",
    "WLX_SAS_TYPE_USER_LOGOFF",
    "WLX_SAS_TYPE_SC_INSERT",
    "WLX_SAS_TYPE_SC_REMOVE",
    "WLX_SAS_TYPE_AUTHENTICATED",
    "WLX_SAS_TYPE_SC_FIRST_READER_ARRIVED",
    "WLX_SAS_TYPE_SC_LAST_READER_REMOVED",
    "WLX_SAS_TYPE_SWITCHUSER",
    "WLX_SAS_TYPE_MAX_MSFT_VALUE",
    "WLX_LOGON_OPT_NO_PROFILE",
    "WLX_PROFILE_TYPE_V1_0",
    "WLX_PROFILE_TYPE_V2_0",
    "WLX_SAS_ACTION_LOGON",
    "WLX_SAS_ACTION_NONE",
    "WLX_SAS_ACTION_LOCK_WKSTA",
    "WLX_SAS_ACTION_LOGOFF",
    "WLX_SAS_ACTION_PWD_CHANGED",
    "WLX_SAS_ACTION_TASKLIST",
    "WLX_SAS_ACTION_UNLOCK_WKSTA",
    "WLX_SAS_ACTION_FORCE_LOGOFF",
    "WLX_SAS_ACTION_SHUTDOWN_SLEEP",
    "WLX_SAS_ACTION_SHUTDOWN_SLEEP2",
    "WLX_SAS_ACTION_SHUTDOWN_HIBERNATE",
    "WLX_SAS_ACTION_RECONNECTED",
    "WLX_SAS_ACTION_DELAYED_FORCE_LOGOFF",
    "WLX_SAS_ACTION_SWITCH_CONSOLE",
    "WLX_WM_SAS",
    "WLX_DLG_SAS",
    "WLX_DLG_INPUT_TIMEOUT",
    "WLX_DLG_SCREEN_SAVER_TIMEOUT",
    "WLX_DLG_USER_LOGOFF",
    "WLX_DIRECTORY_LENGTH",
    "WLX_CREDENTIAL_TYPE_V1_0",
    "WLX_CREDENTIAL_TYPE_V2_0",
    "WLX_CONSOLESWITCHCREDENTIAL_TYPE_V1_0",
    "STATUSMSG_OPTION_NOANIMATION",
    "STATUSMSG_OPTION_SETFOREGROUND",
    "WLX_DESKTOP_NAME",
    "WLX_DESKTOP_HANDLE",
    "WLX_CREATE_INSTANCE_ONLY",
    "WLX_CREATE_USER",
    "WLX_OPTION_USE_CTRL_ALT_DEL",
    "WLX_OPTION_CONTEXT_POINTER",
    "WLX_OPTION_USE_SMART_CARD",
    "WLX_OPTION_FORCE_LOGOFF_TIME",
    "WLX_OPTION_IGNORE_AUTO_LOGON",
    "WLX_OPTION_NO_SWITCH_ON_SAS",
    "WLX_OPTION_SMART_CARD_PRESENT",
    "WLX_OPTION_SMART_CARD_INFO",
    "WLX_OPTION_DISPATCH_TABLE_SIZE",
    "WLX_SHUTDOWN_TYPE",
    "WLX_SAS_ACTION_SHUTDOWN",
    "WLX_SAS_ACTION_SHUTDOWN_REBOOT",
    "WLX_SAS_ACTION_SHUTDOWN_POWER_OFF",
    "WLX_SC_NOTIFICATION_INFO",
    "WLX_PROFILE_V1_0",
    "WLX_PROFILE_V2_0",
    "WLX_MPR_NOTIFY_INFO",
    "WLX_TERMINAL_SERVICES_DATA",
    "WLX_CLIENT_CREDENTIALS_INFO_V1_0",
    "WLX_CLIENT_CREDENTIALS_INFO_V2_0",
    "WLX_CONSOLESWITCH_CREDENTIALS_INFO_V1_0",
    "WLX_DESKTOP",
    "PWLX_USE_CTRL_ALT_DEL",
    "PWLX_SET_CONTEXT_POINTER",
    "PWLX_SAS_NOTIFY",
    "PWLX_SET_TIMEOUT",
    "PWLX_ASSIGN_SHELL_PROTECTION",
    "PWLX_MESSAGE_BOX",
    "PWLX_DIALOG_BOX",
    "PWLX_DIALOG_BOX_INDIRECT",
    "PWLX_DIALOG_BOX_PARAM",
    "PWLX_DIALOG_BOX_INDIRECT_PARAM",
    "PWLX_SWITCH_DESKTOP_TO_USER",
    "PWLX_SWITCH_DESKTOP_TO_WINLOGON",
    "PWLX_CHANGE_PASSWORD_NOTIFY",
    "PWLX_GET_SOURCE_DESKTOP",
    "PWLX_SET_RETURN_DESKTOP",
    "PWLX_CREATE_USER_DESKTOP",
    "PWLX_CHANGE_PASSWORD_NOTIFY_EX",
    "PWLX_CLOSE_USER_DESKTOP",
    "PWLX_SET_OPTION",
    "PWLX_GET_OPTION",
    "PWLX_WIN31_MIGRATE",
    "PWLX_QUERY_CLIENT_CREDENTIALS",
    "PWLX_QUERY_IC_CREDENTIALS",
    "PWLX_QUERY_TS_LOGON_CREDENTIALS",
    "PWLX_DISCONNECT",
    "PWLX_QUERY_TERMINAL_SERVICES_DATA",
    "PWLX_QUERY_CONSOLESWITCH_CREDENTIALS",
    "WLX_DISPATCH_VERSION_1_0",
    "WLX_DISPATCH_VERSION_1_1",
    "WLX_DISPATCH_VERSION_1_2",
    "WLX_DISPATCH_VERSION_1_3",
    "WLX_DISPATCH_VERSION_1_4",
    "PFNMSGECALLBACK",
    "WLX_NOTIFICATION_INFO",
]
