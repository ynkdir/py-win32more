# Need Windows App SDK runtime
# https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/downloads

from ctypes import (
    WinError,
)

from win32more import FAILED
from win32more.appsdk.mddbootstrap import (
    WINDOWSAPPSDK_RELEASE_MAJORMINOR,
    WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W,
    WINDOWSAPPSDK_RUNTIME_VERSION_UINT64,
    MddBootstrapInitialize2,
    MddBootstrapInitializeOptions_OnNoMatch_ShowUI,
    MddBootstrapShutdown,
)
from win32more.Microsoft.UI.Windowing import AppWindow
from win32more.Windows.Win32.Storage.Packaging.Appx import PACKAGE_VERSION
from win32more.Windows.Win32.System.Com import COINIT_APARTMENTTHREADED, CoInitializeEx, CoUninitialize
from win32more.Windows.Win32.UI.WindowsAndMessaging import (
    MSG,
    DispatchMessageW,
    GetMessageW,
    TranslateMessage,
)

closed = False


def on_destroying(appwin, obj):
    global closed
    closed = True


def main() -> None:
    hr = CoInitializeEx(None, COINIT_APARTMENTTHREADED)
    if FAILED(hr):
        raise WinError(hr)

    hr = MddBootstrapInitialize2(
        WINDOWSAPPSDK_RELEASE_MAJORMINOR,
        WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W,
        PACKAGE_VERSION(Version=WINDOWSAPPSDK_RUNTIME_VERSION_UINT64),
        MddBootstrapInitializeOptions_OnNoMatch_ShowUI,
    )
    if FAILED(hr):
        raise WinError(hr)

    appwin = AppWindow.Create()
    appwin.add_Destroying(on_destroying)
    appwin.Show()

    msg = MSG()
    while GetMessageW(msg, 0, 0, 0) > 0:
        TranslateMessage(msg)
        DispatchMessageW(msg)
        if closed:
            break

    MddBootstrapShutdown()

    CoUninitialize()


if __name__ == "__main__":
    main()
