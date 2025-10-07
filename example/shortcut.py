from ctypes import WinError
from pathlib import Path

from win32more.Windows.Win32.System.Com import (
    CLSCTX_INPROC_SERVER,
    CoCreateInstance,
    CoInitialize,
    CoUninitialize,
    IPersistFile,
)
from win32more.Windows.Win32.UI.Shell import IShellLinkW, ShellLink

from win32more import FAILED

hr = CoInitialize(None)
if FAILED(hr):
    raise WinError(hr)

shell_link = IShellLinkW()
hr = CoCreateInstance(ShellLink, None, CLSCTX_INPROC_SERVER, IShellLinkW._iid_, shell_link)
if FAILED(hr):
    raise WinError(hr)

persist_file = IPersistFile()
hr = shell_link.QueryInterface(IPersistFile._iid_, persist_file)
if FAILED(hr):
    raise WinError(hr)

hr = shell_link.SetPath(str(Path("txttxt.txt").resolve()))
if FAILED(hr):
    raise WinError(hr)

hr = persist_file.Save(str(Path("lnklnk.lnk").resolve()), True)
if FAILED(hr):
    raise WinError(hr)

if Path("lnklnk.lnk").exists():
    print("lnklnk.lnk was created")

persist_file.Release()
shell_link.Release()
CoUninitialize()
