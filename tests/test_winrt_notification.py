from contextlib import ExitStack
from ctypes import WinError

from Windows import FAILED
from Windows.Data.Xml.Dom import XmlDocument
from Windows.UI.Notifications import ToastNotification, ToastNotificationManager
from Windows.Win32.System.WinRT import (
    RO_INIT_SINGLETHREADED,
    RoInitialize,
    RoUninitialize,
)


def main() -> None:
    with ExitStack() as defer:
        hr = RoInitialize(RO_INIT_SINGLETHREADED)
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(RoUninitialize)

        template = f"""
        <toast>
            <visual>
                <binding template='ToastGeneric'>
                    <text>this is title</text>
                    <text>hello, world</text>
                </binding>
            </visual>
        </toast>
        """

        xml = XmlDocument.New()
        defer.callback(xml.Release)

        xml.LoadXml(template)

        toast_notification = ToastNotification.CreateToastNotification(xml)
        defer.callback(toast_notification.Release)

        toast_notifier = ToastNotificationManager.CreateToastNotifierWithId(
            r"{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe"
        )
        defer.callback(toast_notifier.Release)

        toast_notifier.Show(toast_notification)


if __name__ == "__main__":
    main()
