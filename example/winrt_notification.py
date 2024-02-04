from ctypes import WinError

from win32more import FAILED
from win32more.Windows.Data.Xml.Dom import XmlDocument
from win32more.Windows.UI.Notifications import ToastNotification, ToastNotificationManager
from win32more.Windows.Win32.System.WinRT import (
    RO_INIT_SINGLETHREADED,
    RoInitialize,
    RoUninitialize,
)


def main2() -> None:
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

    toast_notifier = ToastNotificationManager.CreateToastNotifierWithId(
        r"{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe"
    )

    toast_notifier.Show(toast_notification)


def main() -> None:
    hr = RoInitialize(RO_INIT_SINGLETHREADED)
    if FAILED(hr):
        raise WinError(hr)

    main2()

    RoUninitialize()


if __name__ == "__main__":
    main()
