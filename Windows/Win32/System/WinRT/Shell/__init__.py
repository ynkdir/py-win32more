from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT.Shell
import Windows.Win32.UI.Shell
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
CreateProcessMethod = Int32
CreateProcessMethod_CpCreateProcess: CreateProcessMethod = 0
CreateProcessMethod_CpCreateProcessAsUser: CreateProcessMethod = 1
CreateProcessMethod_CpAicLaunchAdminProcess: CreateProcessMethod = 2
class IDDEInitializer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30dc931f-33fc-4ffd-a168-942258cf3ca4}')
    @commethod(3)
    def Initialize(self, fileExtensionOrProtocol: Windows.Win32.Foundation.PWSTR, method: Windows.Win32.System.WinRT.Shell.CreateProcessMethod, currentDirectory: Windows.Win32.Foundation.PWSTR, execTarget: Windows.Win32.UI.Shell.IShellItem_head, site: Windows.Win32.System.Com.IUnknown_head, application: Windows.Win32.Foundation.PWSTR, targetFile: Windows.Win32.Foundation.PWSTR, arguments: Windows.Win32.Foundation.PWSTR, verb: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'IDDEInitializer')
