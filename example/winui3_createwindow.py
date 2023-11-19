# Need Windows App SDK runtime
# https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/downloads

from ctypes import (
    WinError,
)

from win32more import FAILED
from win32more.mddbootstrap import PACKAGE_VERSION, MddBootstrapInitialize2, MddBootstrapShutdown
from win32more.Microsoft.UI.Windowing import AppWindow
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
    hr = MddBootstrapInitialize2(0x00010004, "", PACKAGE_VERSION(Revision=0, Build=0, Minor=4, Major=1), 0)
    if FAILED(hr):
        raise WinError(hr)

    appwin = AppWindow.Create()
    appwin.Show()

    appwin.add_Destroying(on_destroying)

    msg = MSG()
    while GetMessageW(msg, 0, 0, 0) > 0:
        TranslateMessage(msg)
        DispatchMessageW(msg)
        if closed:
            break

    MddBootstrapShutdown()


if __name__ == "__main__":
    main()
