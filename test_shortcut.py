from win32more.all import *
from pathlib import Path

CoInitialize(None)

shell_link = IShellLinkW()
if FAILED(CoCreateInstance(ShellLink, None, CLSCTX_CLSCTX_INPROC_SERVER, IShellLinkW.Guid, shell_link)):
    raise RuntimeException("CoCreateInstance")

persist_file = IPersistFile()
if FAILED(shell_link.QueryInterface(IPersistFile.Guid, persist_file)):
    raise RuntimeException("QueryInterface")

if FAILED(shell_link.SetPath(str(Path("txttxt.txt").resolve()))):
    raise RuntimeException("IShellLinkW.SetPath")

if FAILED(persist_file.Save(str(Path("lnklnk.lnk").resolve()), True)):
    raise RuntimeException("IPersistFile.Save")

if Path("lnklnk.lnk").exists():
    print("lnklnk.lnk was created")

CoUninitialize()
