from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.SubsystemForLinux

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
WSL_DISTRIBUTION_FLAGS = UInt32
WSL_DISTRIBUTION_FLAGS_NONE = 0
WSL_DISTRIBUTION_FLAGS_ENABLE_INTEROP = 1
WSL_DISTRIBUTION_FLAGS_APPEND_NT_PATH = 2
WSL_DISTRIBUTION_FLAGS_ENABLE_DRIVE_MOUNTING = 4
def _define_WslIsDistributionRegistered():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=False)(("WslIsDistributionRegistered", windll["Api-ms-win-wsl-api-l1-1-0"]), ((1, 'distributionName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WslRegisterDistribution():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("WslRegisterDistribution", windll["Api-ms-win-wsl-api-l1-1-0"]), ((1, 'distributionName'),(1, 'tarGzFilename'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WslUnregisterDistribution():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(("WslUnregisterDistribution", windll["Api-ms-win-wsl-api-l1-1-0"]), ((1, 'distributionName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WslConfigureDistribution():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.System.SubsystemForLinux.WSL_DISTRIBUTION_FLAGS, use_last_error=False)(("WslConfigureDistribution", windll["Api-ms-win-wsl-api-l1-1-0"]), ((1, 'distributionName'),(1, 'defaultUID'),(1, 'wslDistributionFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WslGetDistributionConfiguration():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.System.SubsystemForLinux.WSL_DISTRIBUTION_FLAGS),POINTER(POINTER(win32more.Foundation.PSTR)),POINTER(UInt32), use_last_error=False)(("WslGetDistributionConfiguration", windll["Api-ms-win-wsl-api-l1-1-0"]), ((1, 'distributionName'),(1, 'distributionVersion'),(1, 'defaultUID'),(1, 'wslDistributionFlags'),(1, 'defaultEnvironmentVariables'),(1, 'defaultEnvironmentVariableCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WslLaunchInteractive():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,POINTER(UInt32), use_last_error=False)(("WslLaunchInteractive", windll["Api-ms-win-wsl-api-l1-1-0"]), ((1, 'distributionName'),(1, 'command'),(1, 'useCurrentWorkingDirectory'),(1, 'exitCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WslLaunch():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("WslLaunch", windll["Api-ms-win-wsl-api-l1-1-0"]), ((1, 'distributionName'),(1, 'command'),(1, 'useCurrentWorkingDirectory'),(1, 'stdIn'),(1, 'stdOut'),(1, 'stdErr'),(1, 'process'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "WSL_DISTRIBUTION_FLAGS",
    "WSL_DISTRIBUTION_FLAGS_NONE",
    "WSL_DISTRIBUTION_FLAGS_ENABLE_INTEROP",
    "WSL_DISTRIBUTION_FLAGS_APPEND_NT_PATH",
    "WSL_DISTRIBUTION_FLAGS_ENABLE_DRIVE_MOUNTING",
    "WslIsDistributionRegistered",
    "WslRegisterDistribution",
    "WslUnregisterDistribution",
    "WslConfigureDistribution",
    "WslGetDistributionConfiguration",
    "WslLaunchInteractive",
    "WslLaunch",
]
