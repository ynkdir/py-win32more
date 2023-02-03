import Windows.all as win32
from pathlib import Path

win32.CoInitialize(None)

shell_link = win32.IShellLinkW()
if win32.FAILED(hr := win32.CoCreateInstance(win32.ShellLink, None, win32.CLSCTX_INPROC_SERVER, win32.IShellLinkW.Guid, shell_link)):
    raise win32.WinError(hr)

persist_file = win32.IPersistFile()
if win32.FAILED(hr := shell_link.QueryInterface(win32.IPersistFile.Guid, persist_file)):
    raise win32.WinError(hr)

if win32.FAILED(hr := shell_link.SetPath(str(Path("txttxt.txt").resolve()))):
    raise win32.WinError(hr)

if win32.FAILED(hr := persist_file.Save(str(Path("lnklnk.lnk").resolve()), True)):
    raise win32.WinError(hr)

if Path("lnklnk.lnk").exists():
    print("lnklnk.lnk was created")

win32.CoUninitialize()
