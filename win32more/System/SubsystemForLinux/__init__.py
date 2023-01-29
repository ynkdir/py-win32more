from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.SubsystemForLinux
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
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslIsDistributionRegistered(distributionName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslRegisterDistribution(distributionName: win32more.Foundation.PWSTR, tarGzFilename: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslUnregisterDistribution(distributionName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslConfigureDistribution(distributionName: win32more.Foundation.PWSTR, defaultUID: UInt32, wslDistributionFlags: win32more.System.SubsystemForLinux.WSL_DISTRIBUTION_FLAGS) -> win32more.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslGetDistributionConfiguration(distributionName: win32more.Foundation.PWSTR, distributionVersion: POINTER(UInt32), defaultUID: POINTER(UInt32), wslDistributionFlags: POINTER(win32more.System.SubsystemForLinux.WSL_DISTRIBUTION_FLAGS), defaultEnvironmentVariables: POINTER(POINTER(win32more.Foundation.PSTR)), defaultEnvironmentVariableCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslLaunchInteractive(distributionName: win32more.Foundation.PWSTR, command: win32more.Foundation.PWSTR, useCurrentWorkingDirectory: win32more.Foundation.BOOL, exitCode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslLaunch(distributionName: win32more.Foundation.PWSTR, command: win32more.Foundation.PWSTR, useCurrentWorkingDirectory: win32more.Foundation.BOOL, stdIn: win32more.Foundation.HANDLE, stdOut: win32more.Foundation.HANDLE, stdErr: win32more.Foundation.HANDLE, process: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
WSL_DISTRIBUTION_FLAGS = UInt32
WSL_DISTRIBUTION_FLAGS_NONE: WSL_DISTRIBUTION_FLAGS = 0
WSL_DISTRIBUTION_FLAGS_ENABLE_INTEROP: WSL_DISTRIBUTION_FLAGS = 1
WSL_DISTRIBUTION_FLAGS_APPEND_NT_PATH: WSL_DISTRIBUTION_FLAGS = 2
WSL_DISTRIBUTION_FLAGS_ENABLE_DRIVE_MOUNTING: WSL_DISTRIBUTION_FLAGS = 4
__all__ = [
    "WSL_DISTRIBUTION_FLAGS",
    "WSL_DISTRIBUTION_FLAGS_APPEND_NT_PATH",
    "WSL_DISTRIBUTION_FLAGS_ENABLE_DRIVE_MOUNTING",
    "WSL_DISTRIBUTION_FLAGS_ENABLE_INTEROP",
    "WSL_DISTRIBUTION_FLAGS_NONE",
    "WslConfigureDistribution",
    "WslGetDistributionConfiguration",
    "WslIsDistributionRegistered",
    "WslLaunch",
    "WslLaunchInteractive",
    "WslRegisterDistribution",
    "WslUnregisterDistribution",
]
_arch_optional = [
]
