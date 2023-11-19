from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.mddbootstrap

import os

os.add_dll_directory(os.path.dirname(__file__))

class PACKAGE_VERSION(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        Version: UInt64
        class _Anonymous_e__Struct(EasyCastStructure):
            Revision: UInt16
            Build: UInt16
            Minor: UInt16
            Major: UInt16

MddBootstrapInitializeOptions = Int32
MddBootstrapInitializeOptions_None: win32more.mddbootstrap.MddBootstrapInitializeOptions = 0
MddBootstrapInitializeOptions_OnError_DebugBreak: win32more.mddbootstrap.MddBootstrapInitializeOptions = 1
MddBootstrapInitializeOptions_OnError_DebugBreak_IfDebuggerAttached: win32more.mddbootstrap.MddBootstrapInitializeOptions = 2
MddBootstrapInitializeOptions_OnError_FailFast: win32more.mddbootstrap.MddBootstrapInitializeOptions = 3
MddBootstrapInitializeOptions_OnNoMatch_ShowUI: win32more.mddbootstrap.MddBootstrapInitializeOptions = 4
MddBootstrapInitializeOptions_OnPackageIdentity_NOOP: win32more.mddbootstrap.MddBootstrapInitializeOptions = 5

@winfunctype('Microsoft.WindowsAppRuntime.Bootstrap.dll')
def MddBootstrapInitialize(majorMinorVersion: UInt32, versionTag: String, minVersion: win32more.mddbootstrap.PACKAGE_VERSION) -> win32more.Windows.Win32.Foundation.HRESULT: ...

@winfunctype('Microsoft.WindowsAppRuntime.Bootstrap.dll')
def MddBootstrapInitialize2(majorMinorVersion: UInt32, versionTag: String, minVersion: win32more.mddbootstrap.PACKAGE_VERSION, options: win32more.mddbootstrap.MddBootstrapInitializeOptions) -> win32more.Windows.Win32.Foundation.HRESULT: ...

@winfunctype('Microsoft.WindowsAppRuntime.Bootstrap.dll')
def MddBootstrapShutdown() -> Void: ...

make_ready(__name__)
