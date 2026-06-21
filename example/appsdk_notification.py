# NOTE: This program add registry key
#
# [HKEY_CURRENT_USER\Software\Classes\AppUserModelId\win32more-example-appsdk-notification]
# "CustomActivator"="{CF597ACA-A2FB-4F02-BD03-FF7351D44055}"
# "DisplayName"="appsdk_notification.py"
# "IconUri"="...\icon1.png"
#
# [HKEY_CURRENT_USER\Software\Classes\CLSID\{CF597ACA-A2FB-4F02-BD03-FF7351D44055}\LocalServer32]
# @="\"C:\path\to\python.exe\" \"...\appsdk_notification.py\" ----AppNotificationActivated:"

import sys
import time
import winreg
from pathlib import Path

from win32more.Microsoft.Windows.AppLifecycle import AppInstance, ExtendedActivationKind
from win32more.Microsoft.Windows.AppNotifications import AppNotificationManager, IAppNotificationActivatedEventArgs
from win32more.Microsoft.Windows.AppNotifications.Builder import AppNotificationBuilder, AppNotificationButton
from win32more.Windows.Foundation import Uri
from win32more.Windows.Win32.UI.Shell import SetCurrentProcessExplicitAppUserModelID

AUMID = "win32more-example-appsdk-notification"
CUSTOM_ACTIVATOR = "{CF597ACA-A2FB-4F02-BD03-FF7351D44055}"
DISPLAY_NAME = "appsdk_notification.py"
ICON_URI = Uri(str(Path(__file__).with_name("icon1.png")))
KEY_APP_USER_MODEL_ID = "Software\\Classes\\AppUserModelId"
KEY_CLSID = "Software\\Classes\\CLSID"


# Setup AppUserModelId and CustomActivator registry, so that toast notification can run custom command line.
# Normally WASDK do this setup.
# By default, WASDK set LocalServer32 as "{GetModuleFileName()} ----AppNotificationActivated:" and it doesn't work for python.
def setup_aumid():
    SetCurrentProcessExplicitAppUserModelID(AUMID)

    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"{KEY_APP_USER_MODEL_ID}\\{AUMID}") as key:
        winreg.SetValueEx(key, "CustomActivator", 0, winreg.REG_SZ, CUSTOM_ACTIVATOR)
        # DisplayName and IconUri are set by WASDK.

    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"{KEY_CLSID}\\{CUSTOM_ACTIVATOR}\\LocalServer32") as key:
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, f'"{sys.executable}" "{__file__}" ----AppNotificationActivated:')


def notify(notification_manager):
    notification = (
        AppNotificationBuilder()
        .AddText("title")
        .AddText("message")
        .AddTextBox2("input1", "some input", "input1")
        .AddButton(AppNotificationButton("Ok").AddArgument("action", "Ok"))
        .AddButton(AppNotificationButton("Cancel").AddArgument("action", "Cancel"))
        .BuildNotification()
    )
    notification_manager.Show(notification)


def notification_activated(args):
    print(sys.argv)
    print("AppNotificationActivated!")
    print("    Argument=", args.Argument)
    print("    UserInput=", dict(args.UserInput))
    for i in range(5, 1, -1):
        print(i)
        time.sleep(1)


def main():
    setup_aumid()

    notification_manager = AppNotificationManager.Default

    notification_manager.Register(DISPLAY_NAME, ICON_URI)

    args = AppInstance.GetCurrent().GetActivatedEventArgs()

    if args.Kind == ExtendedActivationKind.Launch:
        notify(notification_manager)
    elif args.Kind == ExtendedActivationKind.AppNotification:
        notification_activated(args.Data.as_(IAppNotificationActivatedEventArgs))
    else:
        raise RuntimeError("Unexpected kind:", args.Kind)

    # Documentation says:
    #   "After calling Unregister, any subsequent calls to invoke the Notification by the user would launch a new process"
    # New process is executed as:
    #   /path/to/python.exe ----AppNotificationActivated: -Embedding
    notification_manager.Unregister()


if __name__ == "__main__":
    main()
