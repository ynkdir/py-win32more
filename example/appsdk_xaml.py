from ctypes import (
    WinError,
)

from win32more import FAILED
from win32more.mddbootstrap import MddBootstrapInitialize2, MddBootstrapShutdown
from win32more.Microsoft.UI.Xaml import Application, HorizontalAlignment_Center, Window
from win32more.Microsoft.UI.Xaml.Controls import Button, StackPanel
from win32more.Windows.Foundation import PropertyValue
from win32more.Windows.Win32.Storage.Packaging.Appx import PACKAGE_VERSION


def box_str(s):
    return PropertyValue.CreateString(s)


# FIXME: How to implement OnLaunched()?
class App:
    def init(self, params):
        self.app = Application.CreateInstance(None, None)

        self.win = Window.CreateInstance(None, None)
        self.win.Title = "WinUI3 Xaml Test"

        self.panel = StackPanel.CreateInstance(None, None)
        self.win.Content = self.panel

        self.button = Button.CreateInstance(None, None)
        self.button.HorizontalAlignment = HorizontalAlignment_Center
        self.button.Content = box_str("Click me!")
        self.button_count = 0

        @self.button.add_Click
        def on_click(sender, e):
            self.button_count += 1
            self.button.Content = box_str(f"{'[' * self.button_count}Click me!{']' * self.button_count}")

        self.panel.Children.Append(self.button)

        self.win.Activate()


def main() -> None:
    hr = MddBootstrapInitialize2(0x00010004, "", PACKAGE_VERSION(Revision=0, Build=0, Minor=4, Major=1), 0)
    if FAILED(hr):
        raise WinError(hr)

    app = App()
    Application.Start(app.init)

    MddBootstrapShutdown()


if __name__ == "__main__":
    main()
