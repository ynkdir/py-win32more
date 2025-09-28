from win32more.Microsoft.Windows.AppNotifications import AppNotificationManager
from win32more.Microsoft.Windows.AppNotifications.Builder import AppNotificationBuilder


def main() -> None:
    notification_manager = AppNotificationManager.Default

    notification_manager.Register()

    # How to set title?
    notification = AppNotificationBuilder().AddText("title").AddText("message").BuildNotification()

    notification_manager.Show(notification)

    # Documentation says:
    #   "After calling Unregister, any subsequent calls to invoke the Notification by the user would launch a new process"
    # New process is executed as:
    #   /path/to/python.exe ----AppNotificationActivated: -Embedding
    # where python.exe is real executable, not venv/Scripts/python.exe even if you are using venv.
    # (because venv/Scripts/python.exe fork system installed python.exe)
    # And python.exe is immediately exit with "unknown option" error.
    notification_manager.Unregister()


if __name__ == "__main__":
    main()
