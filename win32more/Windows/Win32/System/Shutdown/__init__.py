from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Shutdown
MAX_REASON_NAME_LEN: UInt32 = 64
MAX_REASON_DESC_LEN: UInt32 = 256
MAX_REASON_BUGID_LEN: UInt32 = 32
MAX_REASON_COMMENT_LEN: UInt32 = 512
SHUTDOWN_TYPE_LEN: UInt32 = 32
POLICY_SHOWREASONUI_NEVER: UInt32 = 0
POLICY_SHOWREASONUI_ALWAYS: UInt32 = 1
POLICY_SHOWREASONUI_WORKSTATIONONLY: UInt32 = 2
POLICY_SHOWREASONUI_SERVERONLY: UInt32 = 3
SNAPSHOT_POLICY_NEVER: UInt32 = 0
SNAPSHOT_POLICY_ALWAYS: UInt32 = 1
SNAPSHOT_POLICY_UNPLANNED: UInt32 = 2
MAX_NUM_REASONS: UInt32 = 256
@winfunctype('ADVAPI32.dll')
def InitiateSystemShutdownA(lpMachineName: win32more.Windows.Win32.Foundation.PSTR, lpMessage: win32more.Windows.Win32.Foundation.PSTR, dwTimeout: UInt32, bForceAppsClosed: win32more.Windows.Win32.Foundation.BOOL, bRebootAfterShutdown: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def InitiateSystemShutdownW(lpMachineName: win32more.Windows.Win32.Foundation.PWSTR, lpMessage: win32more.Windows.Win32.Foundation.PWSTR, dwTimeout: UInt32, bForceAppsClosed: win32more.Windows.Win32.Foundation.BOOL, bRebootAfterShutdown: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
InitiateSystemShutdown = UnicodeAlias('InitiateSystemShutdownW')
@winfunctype('ADVAPI32.dll')
def AbortSystemShutdownA(lpMachineName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AbortSystemShutdownW(lpMachineName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
AbortSystemShutdown = UnicodeAlias('AbortSystemShutdownW')
@winfunctype('ADVAPI32.dll')
def InitiateSystemShutdownExA(lpMachineName: win32more.Windows.Win32.Foundation.PSTR, lpMessage: win32more.Windows.Win32.Foundation.PSTR, dwTimeout: UInt32, bForceAppsClosed: win32more.Windows.Win32.Foundation.BOOL, bRebootAfterShutdown: win32more.Windows.Win32.Foundation.BOOL, dwReason: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def InitiateSystemShutdownExW(lpMachineName: win32more.Windows.Win32.Foundation.PWSTR, lpMessage: win32more.Windows.Win32.Foundation.PWSTR, dwTimeout: UInt32, bForceAppsClosed: win32more.Windows.Win32.Foundation.BOOL, bRebootAfterShutdown: win32more.Windows.Win32.Foundation.BOOL, dwReason: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON) -> win32more.Windows.Win32.Foundation.BOOL: ...
InitiateSystemShutdownEx = UnicodeAlias('InitiateSystemShutdownExW')
@winfunctype('ADVAPI32.dll')
def InitiateShutdownA(lpMachineName: win32more.Windows.Win32.Foundation.PSTR, lpMessage: win32more.Windows.Win32.Foundation.PSTR, dwGracePeriod: UInt32, dwShutdownFlags: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS, dwReason: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def InitiateShutdownW(lpMachineName: win32more.Windows.Win32.Foundation.PWSTR, lpMessage: win32more.Windows.Win32.Foundation.PWSTR, dwGracePeriod: UInt32, dwShutdownFlags: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS, dwReason: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON) -> UInt32: ...
InitiateShutdown = UnicodeAlias('InitiateShutdownW')
@winfunctype('ADVAPI32.dll')
def CheckForHiberboot(pHiberboot: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN), bClearFlag: win32more.Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
@winfunctype('USER32.dll')
def ExitWindowsEx(uFlags: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS, dwReason: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def LockWorkStation() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def ShutdownBlockReasonCreate(hWnd: win32more.Windows.Win32.Foundation.HWND, pwszReason: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def ShutdownBlockReasonQuery(hWnd: win32more.Windows.Win32.Foundation.HWND, pwszBuff: win32more.Windows.Win32.Foundation.PWSTR, pcchBuff: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def ShutdownBlockReasonDestroy(hWnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
EXIT_WINDOWS_FLAGS = UInt32
EWX_LOGOFF: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS = 0
EWX_SHUTDOWN: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS = 1
EWX_REBOOT: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS = 2
EWX_FORCE: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS = 4
EWX_POWEROFF: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS = 8
EWX_FORCEIFHUNG: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS = 16
EWX_QUICKRESOLVE: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS = 32
EWX_RESTARTAPPS: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS = 64
EWX_HYBRID_SHUTDOWN: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS = 4194304
EWX_BOOTOPTIONS: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS = 16777216
EWX_ARSO: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS = 67108864
EWX_CHECK_SAFE_FOR_SERVER: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS = 134217728
EWX_SYSTEM_INITIATED: win32more.Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS = 268435456
SHUTDOWN_FLAGS = UInt32
SHUTDOWN_FORCE_OTHERS: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 1
SHUTDOWN_FORCE_SELF: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 2
SHUTDOWN_RESTART: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 4
SHUTDOWN_POWEROFF: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 8
SHUTDOWN_NOREBOOT: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 16
SHUTDOWN_GRACE_OVERRIDE: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 32
SHUTDOWN_INSTALL_UPDATES: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 64
SHUTDOWN_RESTARTAPPS: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 128
SHUTDOWN_SKIP_SVC_PRESHUTDOWN: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 256
SHUTDOWN_HYBRID: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 512
SHUTDOWN_RESTART_BOOTOPTIONS: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 1024
SHUTDOWN_SOFT_REBOOT: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 2048
SHUTDOWN_MOBILE_UI: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 4096
SHUTDOWN_ARSO: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 8192
SHUTDOWN_CHECK_SAFE_FOR_SERVER: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 16384
SHUTDOWN_VAIL_CONTAINER: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 32768
SHUTDOWN_SYSTEM_INITIATED: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS = 65536
SHUTDOWN_REASON = UInt32
SHTDN_REASON_NONE: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 0
SHTDN_REASON_FLAG_COMMENT_REQUIRED: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 16777216
SHTDN_REASON_FLAG_DIRTY_PROBLEM_ID_REQUIRED: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 33554432
SHTDN_REASON_FLAG_CLEAN_UI: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 67108864
SHTDN_REASON_FLAG_DIRTY_UI: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 134217728
SHTDN_REASON_FLAG_MOBILE_UI_RESERVED: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 268435456
SHTDN_REASON_FLAG_USER_DEFINED: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 1073741824
SHTDN_REASON_FLAG_PLANNED: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 2147483648
SHTDN_REASON_MAJOR_OTHER: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 0
SHTDN_REASON_MAJOR_NONE: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 0
SHTDN_REASON_MAJOR_HARDWARE: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 65536
SHTDN_REASON_MAJOR_OPERATINGSYSTEM: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 131072
SHTDN_REASON_MAJOR_SOFTWARE: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 196608
SHTDN_REASON_MAJOR_APPLICATION: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 262144
SHTDN_REASON_MAJOR_SYSTEM: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 327680
SHTDN_REASON_MAJOR_POWER: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 393216
SHTDN_REASON_MAJOR_LEGACY_API: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 458752
SHTDN_REASON_MINOR_OTHER: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 0
SHTDN_REASON_MINOR_NONE: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 255
SHTDN_REASON_MINOR_MAINTENANCE: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 1
SHTDN_REASON_MINOR_INSTALLATION: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 2
SHTDN_REASON_MINOR_UPGRADE: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 3
SHTDN_REASON_MINOR_RECONFIG: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 4
SHTDN_REASON_MINOR_HUNG: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 5
SHTDN_REASON_MINOR_UNSTABLE: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 6
SHTDN_REASON_MINOR_DISK: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 7
SHTDN_REASON_MINOR_PROCESSOR: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 8
SHTDN_REASON_MINOR_NETWORKCARD: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 9
SHTDN_REASON_MINOR_POWER_SUPPLY: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 10
SHTDN_REASON_MINOR_CORDUNPLUGGED: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 11
SHTDN_REASON_MINOR_ENVIRONMENT: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 12
SHTDN_REASON_MINOR_HARDWARE_DRIVER: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 13
SHTDN_REASON_MINOR_OTHERDRIVER: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 14
SHTDN_REASON_MINOR_BLUESCREEN: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 15
SHTDN_REASON_MINOR_SERVICEPACK: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 16
SHTDN_REASON_MINOR_HOTFIX: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 17
SHTDN_REASON_MINOR_SECURITYFIX: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 18
SHTDN_REASON_MINOR_SECURITY: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 19
SHTDN_REASON_MINOR_NETWORK_CONNECTIVITY: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 20
SHTDN_REASON_MINOR_WMI: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 21
SHTDN_REASON_MINOR_SERVICEPACK_UNINSTALL: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 22
SHTDN_REASON_MINOR_HOTFIX_UNINSTALL: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 23
SHTDN_REASON_MINOR_SECURITYFIX_UNINSTALL: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 24
SHTDN_REASON_MINOR_MMC: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 25
SHTDN_REASON_MINOR_SYSTEMRESTORE: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 26
SHTDN_REASON_MINOR_TERMSRV: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 32
SHTDN_REASON_MINOR_DC_PROMOTION: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 33
SHTDN_REASON_MINOR_DC_DEMOTION: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 34
SHTDN_REASON_UNKNOWN: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 255
SHTDN_REASON_LEGACY_API: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 2147942400
SHTDN_REASON_VALID_BIT_MASK: win32more.Windows.Win32.System.Shutdown.SHUTDOWN_REASON = 3238002687


make_ready(__name__)
