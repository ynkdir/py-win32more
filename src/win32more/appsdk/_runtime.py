from __future__ import annotations

from win32more import FAILED, ComError, windll
from win32more.Windows.Win32.Foundation import STATEREPOSITORY_E_DEPENDENCY_NOT_RESOLVED
from win32more.Windows.Win32.Storage.Packaging.Appx import PACKAGE_INFO, PACKAGE_VERSION

from . import (
    WINDOWSAPPSDK_RELEASE_MAJORMINOR,
    WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W,
    WINDOWSAPPSDK_RUNTIME_VERSION_UINT64,
)
from ._packaging import GetCurrentPackageInfo, GetFrameworkPackageFamilyName
from .mddbootstrap import MddBootstrapInitialize, _OnNoMatch_ShowUI


class RuntimeNotFoundError(OSError):
    def __init__(self) -> None:
        major = WINDOWSAPPSDK_RELEASE_MAJORMINOR >> 16
        minor = WINDOWSAPPSDK_RELEASE_MAJORMINOR & 0xFFFF
        min_version = PACKAGE_VERSION(Version=WINDOWSAPPSDK_RUNTIME_VERSION_UINT64)
        msg = f"This application requires the Windows App Runtime Version {major}.{minor} (MSIX package version >= {min_version.Major}.{min_version.Minor}.{min_version.Build}.{min_version.Revision})"
        super().__init__(STATEREPOSITORY_E_DEPENDENCY_NOT_RESOLVED, msg)

    def show_dialog(self) -> None:
        _OnNoMatch_ShowUI(
            WINDOWSAPPSDK_RELEASE_MAJORMINOR,
            WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W,
            PACKAGE_VERSION(Version=WINDOWSAPPSDK_RUNTIME_VERSION_UINT64),
        )


def initialize() -> None:
    if is_self_contained():
        return

    hr = MddBootstrapInitialize(
        WINDOWSAPPSDK_RELEASE_MAJORMINOR,
        WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W,
        PACKAGE_VERSION(Version=WINDOWSAPPSDK_RUNTIME_VERSION_UINT64),
    )

    if FAILED(hr):
        if hr == STATEREPOSITORY_E_DEPENDENCY_NOT_RESOLVED:
            raise RuntimeNotFoundError()
        raise ComError(hr)


def get_loaded_appsdk_info() -> PACKAGE_INFO:
    family_name = GetFrameworkPackageFamilyName(
        WINDOWSAPPSDK_RELEASE_MAJORMINOR, WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W
    )
    for info in GetCurrentPackageInfo():
        if info.packageFamilyName == family_name:
            return info
    raise LookupError(f"{family_name} is not loaded")


def is_self_contained() -> bool:
    try:
        windll["Microsoft.WindowsAppRuntime.dll"]
    except AttributeError:
        return False
    return True
