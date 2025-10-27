from __future__ import annotations

import os
import sys
import webbrowser
from pathlib import Path

import win32more
from win32more import FAILED, Int32, String, UInt32, Void
from win32more._win32 import ARCH, winfunctype
from win32more.Windows.Win32.Foundation import (
    HRESULT,
    S_OK,
    STATEREPOSITORY_E_DEPENDENCY_NOT_RESOLVED,
)
from win32more.Windows.Win32.Storage.Packaging.Appx import (
    PACKAGE_DEPENDENCY_RANK_DEFAULT,
    PACKAGE_VERSION,
    PACKAGEDEPENDENCY_CONTEXT,
    AddPackageDependency,
    AddPackageDependencyOptions_None,
    CreatePackageDependencyOptions_None,
    PackageDependencyLifetimeKind_Process,
    PackageDependencyProcessorArchitectures_Arm64,
    PackageDependencyProcessorArchitectures_X64,
    PackageDependencyProcessorArchitectures_X86,
    TryCreatePackageDependency,
)
from win32more.Windows.Win32.UI.WindowsAndMessaging import IDYES, MB_ICONERROR, MB_YESNO, MessageBox

from . import WINDOWSAPPSDK_RUNTIME_VERSION_UINT64
from ._packaging import GetFrameworkPackageFamilyName, IsPackagedProcess

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
    if IsPackagedProcess():
        # FIXME: Mddbootstrap API doesn't support packaged process.
        # Since 1.6.5, WindowsAppSDK seems to work with Win11's package dependency API.
        # I'm not sure if it is offically supported.  It might have a problem.
        VERSION_1_6_5 = 0x1770019109300000
        if not _IsWin11() or WINDOWSAPPSDK_RUNTIME_VERSION_UINT64 < VERSION_1_6_5:
            raise RuntimeError("Packaged process is not supported before Windows 11")
        hr = _Initialize_Win11(GetFrameworkPackageFamilyName(major_minor_version, version_tag), min_version)
        if FAILED(hr):
            if hr == STATEREPOSITORY_E_DEPENDENCY_NOT_RESOLVED:
                if options & MddBootstrapInitializeOptions_OnNoMatch_ShowUI:
                    _OnNoMatch_ShowUI(major_minor_version, version_tag, min_version)
            return hr
        return S_OK
    else:
        return _MddBootstrapInitialize2(major_minor_version, version_tag, min_version, options)


def MddBootstrapShutdown() -> None:
    if IsPackagedProcess() and not _IsWin11():
        raise RuntimeError("Packaged process is not supported before Windows 11")
    elif _IsWin11():
        pass
    else:
        _MddBootstrapShutdown()


def _IsWin11() -> bool:
    return sys.getwindowsversion() >= (10, 0, 22000)


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

    package_dependency_context = PACKAGEDEPENDENCY_CONTEXT()
    hr = AddPackageDependency(
        package_dependency_id,
        PACKAGE_DEPENDENCY_RANK_DEFAULT,
        AddPackageDependencyOptions_None,
        package_dependency_context,
        None,
    )
    if FAILED(hr):
        return hr

    return S_OK


def _OnNoMatch_ShowUI(major_minor_version: int, version_tag: str, min_version: PACKAGE_VERSION) -> None:
    caption = f"{Path(sys.executable).name} - This application could not be started"
    text = f"""This application requires the Windows App Runtime
Version {major_minor_version >> 16}.{major_minor_version & 0xFFFF}
(MSIX package version >= {min_version.Major}.{min_version.Minor}.{min_version.Build}.{min_version.Revision})

Do you want to install a compatible Windows App Runtime now?"""
    r = MessageBox(0, text, caption, MB_YESNO | MB_ICONERROR)
    if r == IDYES:
        webbrowser.open("https://docs.microsoft.com/windows/apps/windows-app-sdk/downloads")
