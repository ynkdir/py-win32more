from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT.Shell
import win32more.Windows.Win32.UI.Shell
CreateProcessMethod = Int32
CpCreateProcess: win32more.Windows.Win32.System.WinRT.Shell.CreateProcessMethod = 0
CpCreateProcessAsUser: win32more.Windows.Win32.System.WinRT.Shell.CreateProcessMethod = 1
CpAicLaunchAdminProcess: win32more.Windows.Win32.System.WinRT.Shell.CreateProcessMethod = 2
class IDDEInitializer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30dc931f-33fc-4ffd-a168-942258cf3ca4}')
    @commethod(3)
    def Initialize(self, fileExtensionOrProtocol: win32more.Windows.Win32.Foundation.PWSTR, method: win32more.Windows.Win32.System.WinRT.Shell.CreateProcessMethod, currentDirectory: win32more.Windows.Win32.Foundation.PWSTR, execTarget: win32more.Windows.Win32.UI.Shell.IShellItem, site: win32more.Windows.Win32.System.Com.IUnknown, application: win32more.Windows.Win32.Foundation.PWSTR, targetFile: win32more.Windows.Win32.Foundation.PWSTR, arguments: win32more.Windows.Win32.Foundation.PWSTR, verb: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
