# https://learn.microsoft.com/en-us/windows/win32/learnwin32/example--the-open-dialog-box

import sys
import os
sys.path.append(os.path.dirname(__file__) + "/watch")

from ctypes import WinError
from raw_filedialog import *

hr = CoInitializeEx(None, COINIT_APARTMENTTHREADED | COINIT_DISABLE_OLE1DDE)
if hr >= 0:
    pFileOpen = IFileOpenDialog()
    hr = CoCreateInstance(FileOpenDialog, None, CLSCTX_ALL, IFileOpenDialog._iid_, pFileOpen)
    if hr >= 0:
        hr = pFileOpen.Show(0)
        if hr >= 0:
            pItem = IShellItem()
            hr = pFileOpen.GetResult(pItem)
            if hr >= 0:
                pszFilePath = PWSTR()
                hr = pItem.GetDisplayName(SIGDN_FILESYSPATH, pszFilePath)
                if hr >= 0:
                    MessageBoxW(0, pszFilePath, "File Path", MB_OK)
                    CoTaskMemFree(pszFilePath)
                pItem.Release()
        pFileOpen.Release()
    CoUninitialize()
if hr < 0:
    raise WinError(hr)
