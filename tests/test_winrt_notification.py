from contextlib import ExitStack
from ctypes import WinError
from typing import TypeVar

from Windows import FAILED, Guid
from Windows.Data.Xml.Dom import IXmlDocumentIO, XmlDocument
from Windows.UI.Notifications import (
    IToastNotificationFactory,
    ToastNotification,
    ToastNotificationManager,
    ToastNotifier,
)
from Windows.Win32.System.WinRT import (
    HSTRING,
    RO_INIT_SINGLETHREADED,
    IInspectable,
    RoActivateInstance,
    RoGetActivationFactory,
    RoInitialize,
    RoUninitialize,
    WindowsCreateString,
    WindowsDeleteString,
)

T = TypeVar("T")


def create_string(s: str) -> HSTRING:
    hs = HSTRING()
    hr = WindowsCreateString(s, len(s), hs)
    if FAILED(hr):
        raise WinError(hr)
    return hs


def activate_instance(classid: str, cls: type[T]) -> T:
    with ExitStack() as defer:
        hs = create_string(classid)
        defer.callback(WindowsDeleteString, hs)
        ii = cls()
        hr = RoActivateInstance(hs, ii)
        if FAILED(hr):
            raise WinError(hr)
        return ii


def get_activation_factory(classid: str, factory_cls: type[T]) -> T:
    with ExitStack() as defer:
        hs = create_string(classid)
        defer.callback(WindowsDeleteString, hs)
        factory = factory_cls()
        hr = RoGetActivationFactory(hs, factory_cls.Guid, factory)
        if FAILED(hr):
            raise WinError(hr)
        return factory


def create_xml_document(s: str) -> XmlDocument:
    with ExitStack() as defer:
        xml = activate_instance("Windows.Data.Xml.Dom.XmlDocument", XmlDocument)
        src = create_string(s)
        defer.callback(WindowsDeleteString, src)
        hr = xml.LoadXml(src)
        if FAILED(hr):
            xml.Release()
            raise WinError(hr)
        return xml


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

        xml = create_xml_document(template)
        defer.callback(xml.Release)

        appid = create_string(
            r"{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe"
        )
        defer.callback(WindowsDeleteString, appid)

        toast_notifier = ToastNotifier()
        hr = ToastNotificationManager.CreateToastNotifierWithId(appid, toast_notifier)
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(toast_notifier.Release)

        toast_notification_factory = get_activation_factory(
            "Windows.UI.Notifications.ToastNotification", IToastNotificationFactory
        )
        defer.callback(toast_notification_factory.Release)

        toast_notification = ToastNotification()
        hr = toast_notification_factory.CreateToastNotification(xml, toast_notification)
        if FAILED(hr):
            raise WinError(hr)
        defer.callback(toast_notification.Release)

        hr = toast_notifier.Show(toast_notification)
        if FAILED(hr):
            raise WinError(hr)


if __name__ == "__main__":
    main()
