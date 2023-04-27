from ctypes import WinError
from pathlib import Path

from Windows import FAILED
from Windows.Win32.System.Com import (CLSCTX_INPROC_SERVER, CoCreateInstance,
                                      CoInitialize, CoUninitialize,
                                      IPersistFile)
from Windows.Win32.UI.Shell import IShellLinkW, ShellLink

CoInitialize(None)

shell_link = IShellLinkW()
if FAILED(hr := CoCreateInstance(ShellLink, None, CLSCTX_INPROC_SERVER, IShellLinkW.Guid, shell_link)):
    raise WinError(hr)

persist_file = IPersistFile()
if FAILED(hr := shell_link.QueryInterface(IPersistFile.Guid, persist_file)):
    raise WinError(hr)

if FAILED(hr := shell_link.SetPath(str(Path("txttxt.txt").resolve()))):
    raise WinError(hr)

if FAILED(hr := persist_file.Save(str(Path("lnklnk.lnk").resolve()), True)):
    raise WinError(hr)

if Path("lnklnk.lnk").exists():
    print("lnklnk.lnk was created")

CoUninitialize()
