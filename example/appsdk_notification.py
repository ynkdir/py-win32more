# NOTE: This program add registry key
#
# [HKEY_CURRENT_USER\Software\Classes\AppUserModelId\win32more-example-appsdk-notification]
# "CustomActivator"="{CF597ACA-A2FB-4F02-BD03-FF7351D44055}"
# "DisplayName"="appsdk_notification.py"
# "IconUri"="...\icon1.png"
#
# [HKEY_CURRENT_USER\Software\Classes\CLSID\{CF597ACA-A2FB-4F02-BD03-FF7351D44055}\LocalServer32]
# @="\"C:\path\to\python.exe\" \"...\appsdk_notification.py\" ----AppNotificationActivated:"

import msvcrt
import sys
import threading
import winreg
from pathlib import Path

from win32more.Microsoft.Windows.AppLifecycle import AppInstance, ExtendedActivationKind
from win32more.Microsoft.Windows.AppNotifications import AppNotificationActivatedEventArgs, AppNotificationManager
from win32more.Microsoft.Windows.AppNotifications.Builder import AppNotificationBuilder, AppNotificationButton
from win32more.Windows.Foundation import Uri
from win32more.Windows.Win32.UI.Shell import SetCurrentProcessExplicitAppUserModelID

AUMID = "win32more-example-appsdk-notification"
CUSTOM_ACTIVATOR = "{CF597ACA-A2FB-4F02-BD03-FF7351D44055}"
DISPLAY_NAME = "appsdk_notification.py"
ICON_URI = Uri(str(Path(__file__).with_name("icon1.png")))
KEY_APP_USER_MODEL_ID = "Software\\Classes\\AppUserModelId"
KEY_CLSID = "Software\\Classes\\CLSID"


handled = threading.Event()


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


def notification_invoked(sender, args):
    print("NotificationInvoked!")
    print("    Arguments=", dict(args.Arguments))
    print("    UserInput=", dict(args.UserInput))
    handled.set()


def notification_activated(sender, args):
    print(sys.argv)
    print("AppNotificationActivated!")
    print("    Arguments=", dict(args.Arguments))
    print("    UserInput=", dict(args.UserInput))


def main():
    setup_aumid()

    notification_manager = AppNotificationManager.Default

    notification_manager.NotificationInvoked += notification_invoked

    notification_manager.Register(DISPLAY_NAME, ICON_URI)

    args = AppInstance.GetCurrent().GetActivatedEventArgs()

    if args.Kind == ExtendedActivationKind.Launch:
        notify(notification_manager)
    elif args.Kind == ExtendedActivationKind.AppNotification:
        notification_activated(notification_manager, args.Data.as_(AppNotificationActivatedEventArgs))
    else:
        raise RuntimeError("Unexpected kind:", args.Kind)

    print("Hit any key to exit")
    while True:
        if msvcrt.kbhit():
            msvcrt.getch()
            break
        if handled.wait(0.1):
            break

    # Documentation says:
    #   "After calling Unregister, any subsequent calls to invoke the Notification by the user would launch a new process"
    # New process is executed as:
    #   /path/to/python.exe ----AppNotificationActivated: -Embedding
    notification_manager.Unregister()


if __name__ == "__main__":
    main()
