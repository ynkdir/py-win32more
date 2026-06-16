# NOTE: This program add registry key
#
# [HKEY_CURRENT_USER\Software\Classes\AppUserModelId\win32more-example-appsdk-notification]
# "CustomActivator"="{CF597ACA-A2FB-4F02-BD03-FF7351D44055}"
# "DisplayName"="appsdk_notification.py"
# "IconUri"="...\icon1.png"
#
# [HKEY_CURRENT_USER\Software\Classes\CLSID\{CF597ACA-A2FB-4F02-BD03-FF7351D44055}\LocalServer32]
# @="\"C:\path\to\python.exe\" \"...\apsdk_notification.py\" ----AppNotificationActivated:"

import sys
import time
import winreg
from pathlib import Path

from win32more.Microsoft.Windows.AppNotifications import AppNotificationManager
from win32more.Microsoft.Windows.AppNotifications.Builder import AppNotificationBuilder
from win32more.Windows.Foundation import Uri
from win32more.Windows.Win32.UI.Shell import SetCurrentProcessExplicitAppUserModelID

AUMID = "win32more-example-appsdk-notification"
CUSTOM_ACTIVATOR = "{CF597ACA-A2FB-4F02-BD03-FF7351D44055}"
DISPLAY_NAME = "appsdk_notification.py"
KEY_APP_USER_MODEL_ID = "Software\\Classes\\AppUserModelId"
KEY_CLSID = "Software\\Classes\\CLSID"


# Setup AppUserModelId and CustomActivator registry, so that toast notification can run custom command line.
def setup_aumid():
    SetCurrentProcessExplicitAppUserModelID(AUMID)

    cmd = f'"{sys.executable}" "{__file__}" ----AppNotificationActivated:'

    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"{KEY_APP_USER_MODEL_ID}\\{AUMID}") as key:
        winreg.SetValueEx(key, "CustomActivator", 0, winreg.REG_SZ, CUSTOM_ACTIVATOR)

    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"{KEY_CLSID}\\{CUSTOM_ACTIVATOR}\\LocalServer32") as key:
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, cmd)


def notify():
    setup_aumid()

    notification_manager = AppNotificationManager.Default

    notification_manager.Register(DISPLAY_NAME, Uri(str(Path(__file__).with_name("icon1.png"))))

    notification = AppNotificationBuilder().AddText("title").AddText("message").BuildNotification()

    notification_manager.Show(notification)

    # Documentation says:
    #   "After calling Unregister, any subsequent calls to invoke the Notification by the user would launch a new process"
    # New process is executed as:
    #   /path/to/python.exe ----AppNotificationActivated: -Embedding
    notification_manager.Unregister()


def notification_activated():
    print(sys.argv)
    print("AppNotificationActivated!")
    for i in range(5, 1, -1):
        print(i)
        time.sleep(1)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "----AppNotificationActivated:":
        notification_activated()
    else:
        notify()


if __name__ == "__main__":
    main()
