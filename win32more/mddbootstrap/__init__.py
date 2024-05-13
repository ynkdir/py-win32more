from __future__ import annotations

import os.path

import win32more.mddbootstrap
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.Packaging.Appx
from win32more import ARCH, FAILED, Int32, String, UInt32, Void, WinError, make_ready, winfunctype
from win32more.Windows.Win32.Foundation import APPMODEL_ERROR_NO_PACKAGE
from win32more.Windows.Win32.Storage.Packaging.Appx import (
    PACKAGEDEPENDENCY_CONTEXT,
    AddPackageDependency,
    AddPackageDependencyOptions_None,
    CreatePackageDependencyOptions_None,
    GetCurrentPackageFullName,
    PackageDependencyLifetimeKind_Process,
    PackageDependencyProcessorArchitectures_Arm64,
    PackageDependencyProcessorArchitectures_X64,
    PackageDependencyProcessorArchitectures_X86,
    TryCreatePackageDependency,
)

# TODO: keep sync with WindowsAppSDK-VersionInfo.h
# VERSION: 1.5.240428000
WINDOWSAPPSDK_RELEASE_MAJORMINOR = 0x00010005
WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W = ""
WINDOWSAPPSDK_RUNTIME_VERSION_UINT64 = 0x13890077009C0000

if ARCH == "ARM64":
    Microsoft_WindowsAppRuntime_Bootstrap_dll = (
        os.path.dirname(__file__) + "\\dll\\arm64\\Microsoft.WindowsAppRuntime.Bootstrap.dll"
    )
    PackageDependencyProcessorArchitectures_Current = PackageDependencyProcessorArchitectures_Arm64
elif ARCH == "X64":
    Microsoft_WindowsAppRuntime_Bootstrap_dll = (
        os.path.dirname(__file__) + "\\dll\\x64\\Microsoft.WindowsAppRuntime.Bootstrap.dll"
    )
    PackageDependencyProcessorArchitectures_Current = PackageDependencyProcessorArchitectures_X64
else:
    Microsoft_WindowsAppRuntime_Bootstrap_dll = (
        os.path.dirname(__file__) + "\\dll\\x86\\Microsoft.WindowsAppRuntime.Bootstrap.dll"
    )
    PackageDependencyProcessorArchitectures_Current = PackageDependencyProcessorArchitectures_X86

MddBootstrapInitializeOptions = Int32
MddBootstrapInitializeOptions_None: win32more.mddbootstrap.MddBootstrapInitializeOptions = 0
MddBootstrapInitializeOptions_OnError_DebugBreak: win32more.mddbootstrap.MddBootstrapInitializeOptions = 1
MddBootstrapInitializeOptions_OnError_DebugBreak_IfDebuggerAttached: win32more.mddbootstrap.MddBootstrapInitializeOptions = 2
MddBootstrapInitializeOptions_OnError_FailFast: win32more.mddbootstrap.MddBootstrapInitializeOptions = 4
MddBootstrapInitializeOptions_OnNoMatch_ShowUI: win32more.mddbootstrap.MddBootstrapInitializeOptions = 8
MddBootstrapInitializeOptions_OnPackageIdentity_NOOP: win32more.mddbootstrap.MddBootstrapInitializeOptions = 16


@winfunctype(Microsoft_WindowsAppRuntime_Bootstrap_dll)
def MddBootstrapInitialize(
    majorMinorVersion: UInt32,
    versionTag: String,
    minVersion: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VERSION,
) -> win32more.Windows.Win32.Foundation.HRESULT: ...


@winfunctype(Microsoft_WindowsAppRuntime_Bootstrap_dll)
def MddBootstrapInitialize2(
    majorMinorVersion: UInt32,
    versionTag: String,
    minVersion: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VERSION,
    options: win32more.mddbootstrap.MddBootstrapInitializeOptions,
) -> win32more.Windows.Win32.Foundation.HRESULT: ...


@winfunctype(Microsoft_WindowsAppRuntime_Bootstrap_dll)
def MddBootstrapShutdown() -> Void: ...


# WindowsAppSdk/dev/WindowsAppRuntime_BootstrapDLL/MddBootstrap.cpp
def FirstTimeInitialization(majorMinorVersion, versionTag, minVersion):
    packageFamilyName = GetFrameworkPackageFamilyName(majorMinorVersion, versionTag)
    packageDependencyId = String()
    hr = TryCreatePackageDependency(
        None,
        packageFamilyName,
        minVersion,
        PackageDependencyProcessorArchitectures_Current,
        PackageDependencyLifetimeKind_Process,
        None,
        CreatePackageDependencyOptions_None,
        packageDependencyId,
    )
    if FAILED(hr):
        raise WinError(hr)

    MDD_PACKAGE_DEPENDENCY_RANK_DEFAULT = 0
    packageDependencyContext = PACKAGEDEPENDENCY_CONTEXT()
    hr = AddPackageDependency(
        packageDependencyId,
        MDD_PACKAGE_DEPENDENCY_RANK_DEFAULT,
        AddPackageDependencyOptions_None,
        packageDependencyContext,
        None,
    )
    if FAILED(hr):
        raise WinError(hr)


def GetFrameworkPackageFamilyName(majorMinorVersion, versionTag):
    majorVersion = majorMinorVersion >> 16
    minorVersion = majorMinorVersion & 0xFFFF
    versionTagDelimiter = "" if versionTag == "" else "-"
    sep = "."  # FIXME: "-" is used in MddBootstrap.cpp
    return (
        f"Microsoft.WindowsAppRuntime{sep}{majorVersion}.{minorVersion}{versionTagDelimiter}{versionTag}_8wekyb3d8bbwe"
    )


def IsPacakgedProcess():
    return GetCurrentPackageFullName(UInt32(), None) != APPMODEL_ERROR_NO_PACKAGE


make_ready(__name__)
