from __future__ import annotations

import os
import sys
import webbrowser
from ctypes import pointer
from pathlib import Path

from win32more.Windows.Win32.Foundation import (
    APPMODEL_ERROR_NO_PACKAGE,
    ERROR_INSUFFICIENT_BUFFER,
    ERROR_SUCCESS,
    HRESULT,
    S_OK,
    STATEREPOSITORY_E_DEPENDENCY_NOT_RESOLVED,
)
from win32more.Windows.Win32.Storage.Packaging.Appx import (
    PACKAGE_FILTER_DYNAMIC,
    PACKAGE_FILTER_STATIC,
    PACKAGE_INFO,
    PACKAGE_VERSION,
    PACKAGEDEPENDENCY_CONTEXT,
    AddPackageDependency,
    AddPackageDependencyOptions_None,
    CreatePackageDependencyOptions_None,
    GetCurrentPackageFullName,
    GetCurrentPackageInfo,
    GetPackagePathByFullName,
    GetPackagesByPackageFamily,
    PackageDependencyLifetimeKind_Process,
    PackageDependencyProcessorArchitectures_Arm64,
    PackageDependencyProcessorArchitectures_X64,
    PackageDependencyProcessorArchitectures_X86,
    TryCreatePackageDependency,
)
from win32more.Windows.Win32.UI.WindowsAndMessaging import IDYES, MB_ICONERROR, MB_YESNO, MessageBox

import win32more
from win32more import FAILED, Byte, Char, ComError, Int32, String, UInt32, Void, WinError
from win32more._win32 import ARCH, winfunctype

# versioninfo.py will be installed by win32more-Microsoft.WindowsAppSDK
from .versioninfo import (  # noqa
    WINDOWSAPPSDK_RELEASE_MAJORMINOR,
    WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W,
    WINDOWSAPPSDK_RUNTIME_VERSION_UINT64,
)

if ARCH == "ARM64":
    PackageDependencyProcessorArchitectures_Current = PackageDependencyProcessorArchitectures_Arm64
    os.add_dll_directory(os.path.dirname(win32more.__file__) + "\\dll\\arm64")
elif ARCH == "X64":
    PackageDependencyProcessorArchitectures_Current = PackageDependencyProcessorArchitectures_X64
    os.add_dll_directory(os.path.dirname(win32more.__file__) + "\\dll\\x64")
elif ARCH == "X86":
    PackageDependencyProcessorArchitectures_Current = PackageDependencyProcessorArchitectures_X86
    os.add_dll_directory(os.path.dirname(win32more.__file__) + "\\dll\\x86")
else:
    assert False

MddBootstrapInitializeOptions = Int32
MddBootstrapInitializeOptions_None = 0
MddBootstrapInitializeOptions_OnError_DebugBreak = 1
MddBootstrapInitializeOptions_OnError_DebugBreak_IfDebuggerAttached = 2
MddBootstrapInitializeOptions_OnError_FailFast = 4
MddBootstrapInitializeOptions_OnNoMatch_ShowUI = 8
MddBootstrapInitializeOptions_OnPackageIdentity_NOOP = 16


@winfunctype("Microsoft.WindowsAppRuntime.Bootstrap.dll", entry_point="MddBootstrapInitialize")
def _MddBootstrapInitialize(majorMinorVersion: UInt32, versionTag: String, minVersion: PACKAGE_VERSION) -> HRESULT: ...


@winfunctype("Microsoft.WindowsAppRuntime.Bootstrap.dll", entry_point="MddBootstrapInitialize2")
def _MddBootstrapInitialize2(
    majorMinorVersion: UInt32, versionTag: String, minVersion: PACKAGE_VERSION, options: MddBootstrapInitializeOptions
) -> HRESULT: ...


@winfunctype("Microsoft.WindowsAppRuntime.Bootstrap.dll", entry_point="MddBootstrapShutdown")
def _MddBootstrapShutdown() -> Void: ...


def MddBootstrapInitialize(major_minor_version: int, version_tag: str, min_version: PACKAGE_VERSION) -> int:
    return MddBootstrapInitialize2(major_minor_version, version_tag, min_version, MddBootstrapInitializeOptions_None)


def MddBootstrapInitialize2(
    major_minor_version: int, version_tag: str, min_version: PACKAGE_VERSION, options: int
) -> int:
    if _IsPackagedProcess():
        # FIXME: Mddbootstrap API doesn't support packaged process.
        # Since 1.6.5, WindowsAppSDK seems to work with Win11's package dependency API.
        # I'm not sure if it is offically supported.  It might have a problem.
        VERSION_1_6_5 = 0x1770019109300000
        if not _IsWin11() or WINDOWSAPPSDK_RUNTIME_VERSION_UINT64 < VERSION_1_6_5:
            raise RuntimeError("Packaged process is not supported before Windows 11")
        hr = _Initialize_Win11(_GetFrameworkPackageFamilyName(major_minor_version, version_tag), min_version)
        if FAILED(hr):
            if hr == STATEREPOSITORY_E_DEPENDENCY_NOT_RESOLVED:
                if options & MddBootstrapInitializeOptions_OnNoMatch_ShowUI:
                    _OnNoMatch_ShowUI(major_minor_version, version_tag, min_version)
            return hr
        return S_OK
    else:
        return _MddBootstrapInitialize2(major_minor_version, version_tag, min_version, options)


def MddBootstrapShutdown() -> None:
    if _IsPackagedProcess() and not _IsWin11():
        raise RuntimeError("Packaged process is not supported before Windows 11")
    elif _IsWin11():
        pass
    else:
        _MddBootstrapShutdown()


def _IsWin11() -> bool:
    return sys.getwindowsversion() >= (10, 0, 22000)


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


def initialize() -> None:
    hr = MddBootstrapInitialize(
        WINDOWSAPPSDK_RELEASE_MAJORMINOR,
        WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W,
        PACKAGE_VERSION(Version=WINDOWSAPPSDK_RUNTIME_VERSION_UINT64),
    )

    if FAILED(hr):
        if hr == STATEREPOSITORY_E_DEPENDENCY_NOT_RESOLVED:
            raise RuntimeNotFound()
        raise ComError(hr)


def uninitialize() -> None:
    MddBootstrapShutdown()


class RuntimeNotFound(OSError):
    def __init__(self):
        major = WINDOWSAPPSDK_RELEASE_MAJORMINOR >> 16
        minor = WINDOWSAPPSDK_RELEASE_MAJORMINOR & 0xFFFF
        min_version = PACKAGE_VERSION(Version=WINDOWSAPPSDK_RUNTIME_VERSION_UINT64)
        msg = f"This application requires the Windows App Runtime Version {major}.{minor} (MSIX package version >= {min_version.Major}.{min_version.Minor}.{min_version.Build}.{min_version.Revision})"
        super().__init__(STATEREPOSITORY_E_DEPENDENCY_NOT_RESOLVED, msg)

    def show_dialog(self):
        _OnNoMatch_ShowUI(
            WINDOWSAPPSDK_RELEASE_MAJORMINOR,
            WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W,
            PACKAGE_VERSION(Version=WINDOWSAPPSDK_RUNTIME_VERSION_UINT64),
        )


def get_current_package_info(flags=PACKAGE_FILTER_DYNAMIC | PACKAGE_FILTER_STATIC):
    size = UInt32()
    r = GetCurrentPackageInfo(flags, size, None, None)
    if r != ERROR_INSUFFICIENT_BUFFER:
        raise WinError(r)

    buf = bytearray(size.value)
    pinfo = pointer(PACKAGE_INFO.from_buffer(buf))
    count = UInt32()
    r = GetCurrentPackageInfo(PACKAGE_FILTER_DYNAMIC | PACKAGE_FILTER_STATIC, size, Byte.from_buffer(buf), count)
    if FAILED(r):
        raise WinError(r)

    return pinfo[0 : count.value]


def get_loaded_appsdk_info():
    family_name = _GetFrameworkPackageFamilyName(
        WINDOWSAPPSDK_RELEASE_MAJORMINOR, WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W
    )
    for info in get_current_package_info():
        if info.packageFamilyName == family_name:
            return info
    raise LookupError(f"{family_name} is not loaded")
