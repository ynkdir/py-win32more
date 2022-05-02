from win32more.all import *
from pathlib import Path

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
