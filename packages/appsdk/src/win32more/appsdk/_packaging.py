from __future__ import annotations

from ctypes import pointer

from win32more import FAILED, Byte, Char, String, UInt32, WinError
from win32more._win32 import ARCH
from win32more.Windows.Win32.Foundation import (
    APPMODEL_ERROR_NO_PACKAGE,
    ERROR_INSUFFICIENT_BUFFER,
    ERROR_SUCCESS,
)
from win32more.Windows.Win32.Storage.Packaging.Appx import (
    PACKAGE_FILTER_DYNAMIC,
    PACKAGE_FILTER_STATIC,
    PACKAGE_INFO,
    PACKAGE_VERSION,
    GetCurrentPackageFullName,
)
from win32more.Windows.Win32.Storage.Packaging.Appx import GetCurrentPackageInfo as _GetCurrentPackageInfo
from win32more.Windows.Win32.Storage.Packaging.Appx import GetPackagePathByFullName as _GetPackagePathByFullName
from win32more.Windows.Win32.Storage.Packaging.Appx import GetPackagesByPackageFamily as _GetPackagesByPackageFamily


def IsPackagedProcess() -> bool:
    return GetCurrentPackageFullName(UInt32(), None) != APPMODEL_ERROR_NO_PACKAGE


# https://learn.microsoft.com/en-us/windows/apps/desktop/modernize/package-identity-overview
def GetFrameworkPackageFamilyName(major_minor_version: int, version_tag: PACKAGE_VERSION) -> str:
    major_version = major_minor_version >> 16
    minor_version = major_minor_version & 0xFFFF
    version_tag_delimiter = "" if version_tag == "" else "-"
    name = f"Microsoft.WindowsAppRuntime.{major_version}.{minor_version}{version_tag_delimiter}{version_tag}"
    publisher_id = "8wekyb3d8bbwe"
    return f"{name}_{publisher_id}"


def GetFrameworkPackageDirectory(
    major_minor_version: int, version_tag: str, min_version: PACKAGE_VERSION
) -> str | None:
    family_name = GetFrameworkPackageFamilyName(major_minor_version, version_tag)
    full_name = ResolvePackageDependency(family_name, min_version, ARCH)
    if full_name is None:
        return None
    return GetPackagePathByFullName(full_name)


def ResolvePackageDependency(family_name: str, min_version: PACKAGE_VERSION, arch: str) -> str | None:
    bestfit = None
    latest_version = None

    for full_name in GetPackagesByPackageFamily(family_name):
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


def GetPackagesByPackageFamily(family_name: str) -> list[str]:
    count = UInt32()
    buffer_length = UInt32()
    r = _GetPackagesByPackageFamily(family_name, count, None, buffer_length, None)
    if r == ERROR_SUCCESS:
        return []  # not found
    elif r != ERROR_INSUFFICIENT_BUFFER:
        raise WinError(r)

    full_names = (String * count.value)()
    buffer = (Char * buffer_length.value)()
    r = _GetPackagesByPackageFamily(family_name, count, full_names, buffer_length, buffer)
    if r != ERROR_SUCCESS:
        raise WinError(r)

    return full_names[: count.value]


def GetPackagePathByFullName(full_name: str) -> str:
    path_length = UInt32()
    r = _GetPackagePathByFullName(full_name, path_length, None)
    if r != ERROR_INSUFFICIENT_BUFFER:
        raise WinError(r)

    path = (Char * path_length.value)()
    r = _GetPackagePathByFullName(full_name, path_length, path)
    if r != ERROR_SUCCESS:
        raise WinError(r)

    return path.value


def GetCurrentPackageInfo(flags=PACKAGE_FILTER_DYNAMIC | PACKAGE_FILTER_STATIC) -> list[PACKAGE_INFO]:
    size = UInt32()
    r = _GetCurrentPackageInfo(flags, size, None, None)
    if r != ERROR_INSUFFICIENT_BUFFER:
        raise WinError(r)

    buf = bytearray(size.value)
    pinfo = pointer(PACKAGE_INFO.from_buffer(buf))
    count = UInt32()
    r = _GetCurrentPackageInfo(flags, size, Byte.from_buffer(buf), count)
    if FAILED(r):
        raise WinError(r)

    return pinfo[0 : count.value]
