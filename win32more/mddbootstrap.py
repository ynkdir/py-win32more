from __future__ import annotations

import os
import sys
import webbrowser
from pathlib import Path

import win32more.mddbootstrap
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.Packaging.Appx
from win32more import ARCH, FAILED, Char, Int32, String, UInt32, Void, WinError, make_ready, winfunctype
from win32more.Windows.Win32.Foundation import (
    APPMODEL_ERROR_NO_PACKAGE,
    ERROR_INSUFFICIENT_BUFFER,
    ERROR_SUCCESS,
    S_OK,
    STATEREPOSITORY_E_DEPENDENCY_NOT_RESOLVED,
)
from win32more.Windows.Win32.Storage.Packaging.Appx import (
    PACKAGE_VERSION,
    PACKAGEDEPENDENCY_CONTEXT,
    AddPackageDependency,
    AddPackageDependencyOptions_None,
    CreatePackageDependencyOptions_None,
    GetCurrentPackageFullName,
    GetPackagePathByFullName,
    GetPackagesByPackageFamily,
    PackageDependencyLifetimeKind_Process,
    PackageDependencyProcessorArchitectures_Arm64,
    PackageDependencyProcessorArchitectures_X64,
    PackageDependencyProcessorArchitectures_X86,
    TryCreatePackageDependency,
)
from win32more.Windows.Win32.UI.WindowsAndMessaging import IDYES, MB_ICONERROR, MB_YESNO, MessageBox

_module = sys.modules[__name__]

# TODO: keep sync with WindowsAppSDK-VersionInfo.h
# VERSION: 1.7.250310001
WINDOWSAPPSDK_RELEASE_MAJORMINOR = 0x00010007
WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W = ""
WINDOWSAPPSDK_RUNTIME_VERSION_UINT64 = 0x1B5801B3009A0000

if ARCH == "ARM64":
    PackageDependencyProcessorArchitectures_Current = PackageDependencyProcessorArchitectures_Arm64
    os.add_dll_directory(os.path.dirname(__file__) + "\\dll\\arm64")
elif ARCH == "X64":
    PackageDependencyProcessorArchitectures_Current = PackageDependencyProcessorArchitectures_X64
    os.add_dll_directory(os.path.dirname(__file__) + "\\dll\\x64")
elif ARCH == "X86":
    PackageDependencyProcessorArchitectures_Current = PackageDependencyProcessorArchitectures_X86
    os.add_dll_directory(os.path.dirname(__file__) + "\\dll\\x86")
else:
    assert False

MddBootstrapInitializeOptions = Int32
MddBootstrapInitializeOptions_None: win32more.mddbootstrap.MddBootstrapInitializeOptions = 0
MddBootstrapInitializeOptions_OnError_DebugBreak: win32more.mddbootstrap.MddBootstrapInitializeOptions = 1
MddBootstrapInitializeOptions_OnError_DebugBreak_IfDebuggerAttached: win32more.mddbootstrap.MddBootstrapInitializeOptions = 2
MddBootstrapInitializeOptions_OnError_FailFast: win32more.mddbootstrap.MddBootstrapInitializeOptions = 4
MddBootstrapInitializeOptions_OnNoMatch_ShowUI: win32more.mddbootstrap.MddBootstrapInitializeOptions = 8
MddBootstrapInitializeOptions_OnPackageIdentity_NOOP: win32more.mddbootstrap.MddBootstrapInitializeOptions = 16


@winfunctype("Microsoft.WindowsAppRuntime.Bootstrap.dll", entry_point="MddBootstrapInitialize")
def _MddBootstrapInitialize(
    majorMinorVersion: UInt32,
    versionTag: String,
    minVersion: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VERSION,
) -> win32more.Windows.Win32.Foundation.HRESULT: ...


@winfunctype("Microsoft.WindowsAppRuntime.Bootstrap.dll", entry_point="MddBootstrapInitialize2")
def _MddBootstrapInitialize2(
    majorMinorVersion: UInt32,
    versionTag: String,
    minVersion: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VERSION,
    options: win32more.mddbootstrap.MddBootstrapInitializeOptions,
) -> win32more.Windows.Win32.Foundation.HRESULT: ...


@winfunctype("Microsoft.WindowsAppRuntime.Bootstrap.dll", entry_point="MddBootstrapShutdown")
def _MddBootstrapShutdown() -> Void: ...


def MddBootstrapInitialize(major_minor_version: int, version_tag: str, min_version: PACKAGE_VERSION) -> int:
    return MddBootstrapInitialize2(major_minor_version, version_tag, min_version, MddBootstrapInitializeOptions_None)


def MddBootstrapInitialize2(
    major_minor_version: int, version_tag: str, min_version: PACKAGE_VERSION, options: int
) -> int:
    if _IsPackagedProcess() and not _IsWin11():
        raise RuntimeError("Packaged process is not supported before Windows 11")
    elif _IsWin11():
        hr = _Initialize_Win11(_GetFrameworkPackageFamilyName(major_minor_version, version_tag), min_version)
        if FAILED(hr):
            if hr == STATEREPOSITORY_E_DEPENDENCY_NOT_RESOLVED:
                if options & MddBootstrapInitializeOptions_OnNoMatch_ShowUI:
                    _OnNoMatch_ShowUI(major_minor_version, version_tag, min_version)
            return hr
        return S_OK
    else:
        return _module._MddBootstrapInitialize2(major_minor_version, version_tag, min_version, options)


def MddBootstrapShutdown() -> None:
    if _IsPackagedProcess() and not _IsWin11():
        raise RuntimeError("Packaged process is not supported before Windows 11")
    elif _IsWin11():
        pass
    else:
        return _module._MddBootstrapShutdown()


def _IsWin11() -> bool:
    # FIXME: RoActivateInstance() failes
    return False
    # return sys.getwindowsversion() >= (10, 0, 22000)


def _IsPackagedProcess() -> bool:
    return GetCurrentPackageFullName(UInt32(), None) != APPMODEL_ERROR_NO_PACKAGE


def _Initialize_Win11(family_name: str, min_version: PACKAGE_VERSION) -> int:
    package_dependency_id = String()
    hr = TryCreatePackageDependency(
        None,
        family_name,
        min_version,
        PackageDependencyProcessorArchitectures_Current,
        PackageDependencyLifetimeKind_Process,
        None,
        CreatePackageDependencyOptions_None,
        package_dependency_id,
    )
    if FAILED(hr):
        return hr

    MDD_PACKAGE_DEPENDENCY_RANK_DEFAULT = 0
    package_dependency_context = PACKAGEDEPENDENCY_CONTEXT()
    hr = AddPackageDependency(
        package_dependency_id,
        MDD_PACKAGE_DEPENDENCY_RANK_DEFAULT,
        AddPackageDependencyOptions_None,
        package_dependency_context,
        None,
    )
    if FAILED(hr):
        return hr

    return S_OK


# https://learn.microsoft.com/en-us/windows/apps/desktop/modernize/package-identity-overview
def _GetFrameworkPackageFamilyName(major_minor_version: int, version_tag: PACKAGE_VERSION) -> str:
    major_version = major_minor_version >> 16
    minor_version = major_minor_version & 0xFFFF
    version_tag_delimiter = "" if version_tag == "" else "-"
    name = f"Microsoft.WindowsAppRuntime.{major_version}.{minor_version}{version_tag_delimiter}{version_tag}"
    publisher_id = "8wekyb3d8bbwe"
    return f"{name}_{publisher_id}"


def _GetFrameworkPackageDirectory(
    major_minor_version: int, version_tag: str, min_version: PACKAGE_VERSION
) -> str | None:
    family_name = _GetFrameworkPackageFamilyName(major_minor_version, version_tag)
    full_name = _ResolvePackageDependency(family_name, min_version, ARCH)
    if full_name is None:
        return None
    return _GetPackagePathByFullName(full_name)


def _ResolvePackageDependency(family_name: str, min_version: PACKAGE_VERSION, arch: str) -> str | None:
    bestfit = None
    latest_version = None

    for full_name in _GetPackagesByPackageFamily(family_name):
        name, version, architecture, resource_id, publisher_id = full_name.split("_")
        major, minor, build, revision = [int(x) for x in version.split(".")]
        if architecture.upper() != arch:
            continue
        if (major, minor, build, revision) < (
            min_version.Major,
            min_version.Minor,
            min_version.Build,
            min_version.Revision,
        ):
            continue
        if latest_version is None or latest_version < (major, minor, build, revision):
            bestfit = full_name
            latest_version = (major, minor, build, revision)

    return bestfit


def _OnNoMatch_ShowUI(major_minor_version: int, version_tag: str, min_version: PACKAGE_VERSION) -> None:
    caption = f"{Path(sys.executable).name} - This application could not be started"
    text = f"""This application requires the Windows App Runtime
Version {major_minor_version >> 16}.{major_minor_version & 0xFFFF}
(MSIX package version >= {min_version.Major}.{min_version.Minor}.{min_version.Build}.{min_version.Revision})

Do you want to install a compatible Windows App Runtime now?"""
    r = MessageBox(0, text, caption, MB_YESNO | MB_ICONERROR)
    if r == IDYES:
        webbrowser.open("https://docs.microsoft.com/windows/apps/windows-app-sdk/downloads")


def _GetPackagesByPackageFamily(family_name: str) -> list[str]:
    count = UInt32()
    buffer_length = UInt32()
    r = GetPackagesByPackageFamily(family_name, count, None, buffer_length, None)
    if r == ERROR_SUCCESS:
        return []  # not found
    elif r != ERROR_INSUFFICIENT_BUFFER:
        raise WinError(r)

    full_names = (String * count.value)()
    buffer = (Char * buffer_length.value)()
    r = GetPackagesByPackageFamily(family_name, count, full_names, buffer_length, buffer)
    if r != ERROR_SUCCESS:
        raise WinError(r)

    return full_names[: count.value]


def _GetPackagePathByFullName(full_name: str) -> str:
    path_length = UInt32()
    r = GetPackagePathByFullName(full_name, path_length, None)
    if r != ERROR_INSUFFICIENT_BUFFER:
        raise WinError(r)

    path = (Char * path_length.value)()
    r = GetPackagePathByFullName(full_name, path_length, path)
    if r != ERROR_SUCCESS:
        raise WinError(r)

    return path.value


make_ready(__name__)
