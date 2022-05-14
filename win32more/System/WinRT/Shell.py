from win32more import *
import win32more.System.WinRT.Shell
import win32more.Foundation
import win32more.System.Com
import win32more.UI.Shell

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.WinRT.Shell, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.WinRT.Shell, name)
CreateProcessMethod = Int32
CreateProcessMethod_CpCreateProcess = 0
CreateProcessMethod_CpCreateProcessAsUser = 1
CreateProcessMethod_CpAicLaunchAdminProcess = 2
def _define_IDDEInitializer_head():
    class IDDEInitializer(win32more.System.Com.IUnknown_head):
        Guid = Guid('30dc931f-33fc-4ffd-a168-942258cf3ca4')
    return IDDEInitializer
def _define_IDDEInitializer():
    IDDEInitializer = win32more.System.WinRT.Shell.IDDEInitializer_head
    IDDEInitializer.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.WinRT.Shell.CreateProcessMethod,win32more.Foundation.PWSTR,win32more.UI.Shell.IShellItem_head,win32more.System.Com.IUnknown_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'Initialize', ((1, 'fileExtensionOrProtocol'),(1, 'method'),(1, 'currentDirectory'),(1, 'execTarget'),(1, 'site'),(1, 'application'),(1, 'targetFile'),(1, 'arguments'),(1, 'verb'),)))
    return IDDEInitializer
__all__ = [
    "CreateProcessMethod",
    "CreateProcessMethod_CpCreateProcess",
    "CreateProcessMethod_CpCreateProcessAsUser",
    "CreateProcessMethod_CpAicLaunchAdminProcess",
    "IDDEInitializer",
]
