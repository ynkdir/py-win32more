from ctypes import (
    WinError,
)

from win32more import FAILED
from win32more.mddbootstrap import MddBootstrapInitialize2, MddBootstrapShutdown, MddBootstrapInitializeOptions_OnNoMatch_ShowUI
from win32more.Microsoft.UI.Xaml import Application, HorizontalAlignment_Center, VerticalAlignment_Center, Window
from win32more.Microsoft.UI.Xaml.Controls import Button, StackPanel
from win32more.Windows.Foundation import PropertyValue
from win32more.Windows.Win32.Storage.Packaging.Appx import PACKAGE_VERSION


def box_str(s):
    return PropertyValue.CreateString(s)


# FIXME: How to implement OnLaunched()?
def init(params):
    app = Application.CreateInstance(None, None)

    win = Window.CreateInstance(None, None)
    win.Title = "WinUI3 Xaml Test"

    panel = StackPanel.CreateInstance(None, None)
    panel.HorizontalAlignment = HorizontalAlignment_Center
    panel.VerticalAlignment = VerticalAlignment_Center
    win.Content = panel

    button = Button.CreateInstance(None, None)

    button.Content = box_str("Click me!")
    button_count = 0

    @button.add_Click
    def on_click(sender, e):
        button_count += 1
        button.Content = box_str(f"{'[' * button_count}Click me!{']' * button_count}")

    panel.Children.Append(button)

    win.Activate()


def main() -> None:
    MddBootstrapInitialize2(0x00010004, "", PACKAGE_VERSION(Version=0x0FA0041900750000), MddBootstrapInitializeOptions_OnNoMatch_ShowUI)
    Application.Start(init)
    MddBootstrapShutdown()


if __name__ == "__main__":
    main()
