# NOTE: This program add registry key
#
# [HKEY_CURRENT_USER\Software\Classes\AppUserModelId\win32more-example-winrt-notification]
# "CustomActivator"="{EECF8B95-96C7-4738-B802-FC02D16CB000}"
# "DisplayName"="winrt_notification.py"
# "IconUri"="...\icon1.png"
#
# [HKEY_CURRENT_USER\Software\Classes\CLSID\{EECF8B95-96C7-4738-B802-FC02D16CB000}\LocalServer32]
# @="\"C:\path\to\python.exe\" \"...\winrt_notification.py\""

import sys
import threading
import winreg
from ctypes import POINTER
from pathlib import Path

from win32more import FAILED, ComClass, Guid, UInt32, VoidPtr, WinError
from win32more.Windows.Data.Xml.Dom import XmlDocument
from win32more.Windows.UI.Notifications import ToastNotification, ToastNotificationManager
from win32more.Windows.Win32.Foundation import BOOL, HRESULT, PWSTR, S_OK
from win32more.Windows.Win32.System.Com import (
    CLSCTX_LOCAL_SERVER,
    REGCLS_MULTIPLEUSE,
    CoRegisterClassObject,
    CoRevokeClassObject,
    IClassFactory,
    IUnknown,
)
from win32more.Windows.Win32.UI.Notifications import (
    NOTIFICATION_USER_INPUT_DATA,
    INotificationActivationCallback,
)
from win32more.Windows.Win32.UI.Shell import SetCurrentProcessExplicitAppUserModelID

AUMID = "win32more-example-winrt-notification"
CUSTOM_ACTIVATOR = "{EECF8B95-96C7-4738-B802-FC02D16CB000}"
DISPLAY_NAME = "winrt_notification.py"
KEY_APP_USER_MODEL_ID = "Software\\Classes\\AppUserModelId"
KEY_CLSID = "Software\\Classes\\CLSID"


notification_activated_event = threading.Event()
notification_activated_args = {}


# Setup AppUserModelId and CustomActivator registry, so that toast notification can run custom command line.
def setup_aumid():
    SetCurrentProcessExplicitAppUserModelID(AUMID)

    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"{KEY_APP_USER_MODEL_ID}\\{AUMID}") as key:
        winreg.SetValueEx(key, "CustomActivator", 0, winreg.REG_SZ, CUSTOM_ACTIVATOR)
        winreg.SetValueEx(key, "DisplayName", 0, winreg.REG_SZ, DISPLAY_NAME)
        winreg.SetValueEx(key, "IconUri", 0, winreg.REG_SZ, str(Path(__file__).with_name("icon1.png")))

    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, f"{KEY_CLSID}\\{CUSTOM_ACTIVATOR}\\LocalServer32") as key:
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, f'"{sys.executable}" "{__file__}"')


# Windows activates a clicked toast by calling
# CoCreateInstance(CUSTOM_ACTIVATOR, ..., CLSCTX_LOCAL_SERVER, IID_INotificationActivationCallback)
# and then Activate().  COM starts LocalServer32 and waits for it to register this
# class object.  Without the registration the click is never acknowledged, so the
# notification is not dismissed and the invoked arguments are lost.
class NotificationActivator(ComClass, INotificationActivationCallback):
    def Activate(
        self,
        appUserModelId: PWSTR,
        invokedArgs: PWSTR,
        data: POINTER(NOTIFICATION_USER_INPUT_DATA),
        count: UInt32,
    ) -> HRESULT:
        # Called on an RPC thread while Windows waits.  Hand the work over to the
        # main thread and return immediately.
        notification_activated_args["app_user_model_id"] = appUserModelId
        notification_activated_args["invoked_args"] = invokedArgs
        notification_activated_args["user_input"] = {data[i].Key: data[i].Value for i in range(count)}
        notification_activated_event.set()
        return S_OK


class NotificationActivatorFactory(ComClass, IClassFactory):
    def __init__(self) -> None:
        super().__init__()
        self._activator = NotificationActivator()

    def CreateInstance(self, pUnkOuter: IUnknown, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> HRESULT:
        return self._activator.QueryInterface(riid, ppvObject)

    def LockServer(self, fLock: BOOL) -> HRESULT:
        return S_OK


def notify():
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
    print("    InvokedArgs=", notification_activated_args["invoked_args"])
    print("    UserInput=", notification_activated_args["user_input"])


def main():
    setup_aumid()

    factory = NotificationActivatorFactory()
    cookie = UInt32()
    hr = CoRegisterClassObject(Guid(CUSTOM_ACTIVATOR), factory, CLSCTX_LOCAL_SERVER, REGCLS_MULTIPLEUSE, cookie)
    if FAILED(hr):
        raise WinError(hr)

    activated = False

    try:
        if len(sys.argv) > 1 and sys.argv[1] == "-Embedding":
            # notification run custom activator with -Embedding
            activated = True
        else:
            notify()

        print("Press CTRL-C to exit (or timeout in 10 seconds)")
        try:
            for _ in range(10):
                if notification_activated_event.wait(1):
                    notification_activated()
                    if activated:
                        # keep message
                        notification_activated_event.clear()
                        continue
                    break
                print(".", end="", flush=True)
        except KeyboardInterrupt:
            pass
    finally:
        CoRevokeClassObject(cookie.value)


if __name__ == "__main__":
    main()
