from __future__ import annotations
from win32more.win32.prelude import *
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.DeveloperLicensing
@winfunctype('WSClient.dll')
def CheckDeveloperLicense(pExpiration: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSClient.dll')
def AcquireDeveloperLicense(hwndParent: win32more.Windows.Win32.Foundation.HWND, pExpiration: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WSClient.dll')
def RemoveDeveloperLicense(hwndParent: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
