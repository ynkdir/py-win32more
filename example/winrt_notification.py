# NOTE: This program add registry key
#
# [HKEY_CURRENT_USER\Software\Classes\AppUserModelId\win32more-example-winrt-notification]
# "CustomActivator"="{CF597ACA-A2FB-4F02-BD03-FF7351D44055}"
# "DisplayName"="winrt_notification.py"
# "IconUri"="...\icon1.png"
#
# [HKEY_CURRENT_USER\Software\Classes\CLSID\{EECF8B95-96C7-4738-B802-FC02D16CB000}\LocalServer32]
# @="\"C:\path\to\python.exe\" \"...\winrt_notification.py\""

import sys
import time
import winreg
from pathlib import Path

from win32more.Windows.Data.Xml.Dom import XmlDocument
from win32more.Windows.UI.Notifications import ToastNotification, ToastNotificationManager
from win32more.Windows.Win32.UI.Shell import SetCurrentProcessExplicitAppUserModelID

AUMID = "win32more-example-winrt-notification"
CUSTOM_ACTIVATOR = "{EECF8B95-96C7-4738-B802-FC02D16CB000}"
DISPLAY_NAME = "winrt_notification.py"
KEY_APP_USER_MODEL_ID = "Software\\Classes\\AppUserModelId"
KEY_CLSID = "Software\\Classes\\CLSID"


# Setup AppUserModelId and CustomActivator registry, so that toast notification can run custom command line.
def setup_aumid():
    SetCurrentProcessExplicitAppUserModelID(AUMID)

    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"{KEY_APP_USER_MODEL_ID}\\{AUMID}") as key:
        winreg.SetValueEx(key, "CustomActivator", 0, winreg.REG_SZ, CUSTOM_ACTIVATOR)
        winreg.SetValueEx(key, "DisplayName", 0, winreg.REG_SZ, DISPLAY_NAME)
        winreg.SetValueEx(key, "IconUri", 0, winreg.REG_SZ, str(Path(__file__).with_name("icon1.png")))

    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"{KEY_CLSID}\\{CUSTOM_ACTIVATOR}\\LocalServer32") as key:
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, f'"{sys.executable}" "{__file__}"')


def notify():
    setup_aumid()

    template = """
    <toast>
        <visual>
            <binding template='ToastGeneric'>
                <text>this is title</text>
                <text>hello, world</text>
            </binding>
        </visual>
    </toast>
    """

    xml = XmlDocument.CreateInstance()

    xml.LoadXml(template)

    toast_notification = ToastNotification.CreateToastNotification(xml)

    toast_notifier = ToastNotificationManager.CreateToastNotifierWithId(AUMID)

    toast_notifier.Show(toast_notification)


def notification_activated():
    print(sys.argv)
    print("WinrtNotificationActivated!")
    for i in range(5, 1, -1):
        print(i)
        time.sleep(1)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-Embedding":
        # notification run custom activator with -Embedding
        notification_activated()
    else:
        notify()


if __name__ == "__main__":
    main()
