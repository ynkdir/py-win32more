from ctypes import (
    WinError,
)

from win32more import FAILED
from win32more.mddbootstrap import MddBootstrapInitialize2, MddBootstrapShutdown
from win32more.Microsoft.Windows.AppNotifications import AppNotificationManager
from win32more.Microsoft.Windows.AppNotifications.Builder import AppNotificationBuilder
from win32more.Windows.Win32.Storage.Packaging.Appx import PACKAGE_VERSION


def main() -> None:
    hr = MddBootstrapInitialize2(0x00010004, "", PACKAGE_VERSION(Revision=0, Build=0, Minor=4, Major=1), 0)
    if FAILED(hr):
        raise WinError(hr)

    notification_manager = AppNotificationManager.Default

    notification_manager.Register()

    # How to set title?
    notification = AppNotificationBuilder.CreateInstance().AddText("title").AddText("message").BuildNotification()

    notification_manager.Show(notification)

    # Documentation says:
    # "After calling Unregister, any subsequent calls to invoke the Notification by the user would launch a new process"
    notification_manager.Unregister()

    MddBootstrapShutdown()


if __name__ == "__main__":
    main()
