from __future__ import annotations
from win32more import Int32, String, UInt32, Void, make_ready, winfunctype
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.Packaging.Appx
import win32more.mddbootstrap

import os.path

# TODO: keep sync with WindowsAppSDK-VersionInfo.h
# VERSION: 1.4.23115000
WINDOWSAPPSDK_RELEASE_MAJORMINOR = 0x00010004
WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W = ""
WINDOWSAPPSDK_RUNTIME_VERSION_UINT64 = 0x0FA0041900750000

Microsoft_WindowsAppRuntime_Bootstrap_dll = os.path.dirname(__file__) + "\\Microsoft.WindowsAppRuntime.Bootstrap.dll"

MddBootstrapInitializeOptions = Int32
MddBootstrapInitializeOptions_None: win32more.mddbootstrap.MddBootstrapInitializeOptions = 0
MddBootstrapInitializeOptions_OnError_DebugBreak: win32more.mddbootstrap.MddBootstrapInitializeOptions = 1
MddBootstrapInitializeOptions_OnError_DebugBreak_IfDebuggerAttached: win32more.mddbootstrap.MddBootstrapInitializeOptions = 2
MddBootstrapInitializeOptions_OnError_FailFast: win32more.mddbootstrap.MddBootstrapInitializeOptions = 4
MddBootstrapInitializeOptions_OnNoMatch_ShowUI: win32more.mddbootstrap.MddBootstrapInitializeOptions = 8
MddBootstrapInitializeOptions_OnPackageIdentity_NOOP: win32more.mddbootstrap.MddBootstrapInitializeOptions = 16

@winfunctype(Microsoft_WindowsAppRuntime_Bootstrap_dll)
def MddBootstrapInitialize(majorMinorVersion: UInt32, versionTag: String, minVersion: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VERSION) -> win32more.Windows.Win32.Foundation.HRESULT: ...

@winfunctype(Microsoft_WindowsAppRuntime_Bootstrap_dll)
def MddBootstrapInitialize2(majorMinorVersion: UInt32, versionTag: String, minVersion: win32more.Windows.Win32.Storage.Packaging.Appx.PACKAGE_VERSION, options: win32more.mddbootstrap.MddBootstrapInitializeOptions) -> win32more.Windows.Win32.Foundation.HRESULT: ...

@winfunctype(Microsoft_WindowsAppRuntime_Bootstrap_dll)
def MddBootstrapShutdown() -> Void: ...

make_ready(__name__)
