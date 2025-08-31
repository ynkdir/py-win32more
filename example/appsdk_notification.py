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
from win32more.Microsoft.Windows.AppNotifications import AppNotificationManager
from win32more.Microsoft.Windows.AppNotifications.Builder import AppNotificationBuilder
from win32more.Windows.Win32.Storage.Packaging.Appx import PACKAGE_VERSION
from win32more.Windows.Win32.System.Com import COINIT_APARTMENTTHREADED, CoInitializeEx, CoUninitialize


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

    notification_manager = AppNotificationManager.Default

    notification_manager.Register()

    # How to set title?
    notification = AppNotificationBuilder().AddText("title").AddText("message").BuildNotification()

    notification_manager.Show(notification)

    # Documentation says:
    # "After calling Unregister, any subsequent calls to invoke the Notification by the user would launch a new process"
    notification_manager.Unregister()

    MddBootstrapShutdown()

    CoUninitialize()


if __name__ == "__main__":
    main()
