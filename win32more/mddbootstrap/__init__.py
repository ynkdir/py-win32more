from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.Packaging.Appx
import win32more.mddbootstrap

import os.path

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
