from ctypes import WinError
from pathlib import Path

from Windows.Win32.System.Com import (CLSCTX_INPROC_SERVER, CoCreateInstance,
                                      CoInitialize, CoUninitialize,
                                      IPersistFile)
from Windows.Win32.UI.Shell import IShellLinkW, ShellLink

CoInitialize(None)

shell_link = IShellLinkW()
CoCreateInstance(ShellLink, None, CLSCTX_INPROC_SERVER, IShellLinkW.Guid, shell_link)

persist_file = IPersistFile()
shell_link.QueryInterface(IPersistFile.Guid, persist_file)

shell_link.SetPath(str(Path("txttxt.txt").resolve()))

persist_file.Save(str(Path("lnklnk.lnk").resolve()), True)

if Path("lnklnk.lnk").exists():
    print("lnklnk.lnk was created")

CoUninitialize()
