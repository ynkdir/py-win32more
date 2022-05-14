from win32more import *
import win32more.UI.Notifications
import win32more.Foundation
import win32more.System.Com

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.UI.Notifications, name, eval(f"_define_{name}()"))
    return getattr(win32more.UI.Notifications, name)
def _define_NOTIFICATION_USER_INPUT_DATA_head():
    class NOTIFICATION_USER_INPUT_DATA(Structure):
        pass
    return NOTIFICATION_USER_INPUT_DATA
def _define_NOTIFICATION_USER_INPUT_DATA():
    NOTIFICATION_USER_INPUT_DATA = win32more.UI.Notifications.NOTIFICATION_USER_INPUT_DATA_head
    NOTIFICATION_USER_INPUT_DATA._fields_ = [
        ("Key", win32more.Foundation.PWSTR),
        ("Value", win32more.Foundation.PWSTR),
    ]
    return NOTIFICATION_USER_INPUT_DATA
def _define_INotificationActivationCallback_head():
    class INotificationActivationCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('53e31837-6600-4a81-9395-75cffe746f94')
    return INotificationActivationCallback
def _define_INotificationActivationCallback():
    INotificationActivationCallback = win32more.UI.Notifications.INotificationActivationCallback_head
    INotificationActivationCallback.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.UI.Notifications.NOTIFICATION_USER_INPUT_DATA),UInt32, use_last_error=False)(3, 'Activate', ((1, 'appUserModelId'),(1, 'invokedArgs'),(1, 'data'),(1, 'count'),)))
    return INotificationActivationCallback
__all__ = [
    "NOTIFICATION_USER_INPUT_DATA",
    "INotificationActivationCallback",
]
