from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.SubsystemForLinux
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslIsDistributionRegistered(distributionName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslRegisterDistribution(distributionName: win32more.Windows.Win32.Foundation.PWSTR, tarGzFilename: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslUnregisterDistribution(distributionName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslConfigureDistribution(distributionName: win32more.Windows.Win32.Foundation.PWSTR, defaultUID: UInt32, wslDistributionFlags: win32more.Windows.Win32.System.SubsystemForLinux.WSL_DISTRIBUTION_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslGetDistributionConfiguration(distributionName: win32more.Windows.Win32.Foundation.PWSTR, distributionVersion: POINTER(UInt32), defaultUID: POINTER(UInt32), wslDistributionFlags: POINTER(win32more.Windows.Win32.System.SubsystemForLinux.WSL_DISTRIBUTION_FLAGS), defaultEnvironmentVariables: POINTER(POINTER(win32more.Windows.Win32.Foundation.PSTR)), defaultEnvironmentVariableCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslLaunchInteractive(distributionName: win32more.Windows.Win32.Foundation.PWSTR, command: win32more.Windows.Win32.Foundation.PWSTR, useCurrentWorkingDirectory: win32more.Windows.Win32.Foundation.BOOL, exitCode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Api-ms-win-wsl-api-l1-1-0.dll')
def WslLaunch(distributionName: win32more.Windows.Win32.Foundation.PWSTR, command: win32more.Windows.Win32.Foundation.PWSTR, useCurrentWorkingDirectory: win32more.Windows.Win32.Foundation.BOOL, stdIn: win32more.Windows.Win32.Foundation.HANDLE, stdOut: win32more.Windows.Win32.Foundation.HANDLE, stdErr: win32more.Windows.Win32.Foundation.HANDLE, process: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
WSL_DISTRIBUTION_FLAGS = Int32
WSL_DISTRIBUTION_FLAGS_NONE: win32more.Windows.Win32.System.SubsystemForLinux.WSL_DISTRIBUTION_FLAGS = 0
WSL_DISTRIBUTION_FLAGS_ENABLE_INTEROP: win32more.Windows.Win32.System.SubsystemForLinux.WSL_DISTRIBUTION_FLAGS = 1
WSL_DISTRIBUTION_FLAGS_APPEND_NT_PATH: win32more.Windows.Win32.System.SubsystemForLinux.WSL_DISTRIBUTION_FLAGS = 2
WSL_DISTRIBUTION_FLAGS_ENABLE_DRIVE_MOUNTING: win32more.Windows.Win32.System.SubsystemForLinux.WSL_DISTRIBUTION_FLAGS = 4


make_ready(__name__)
