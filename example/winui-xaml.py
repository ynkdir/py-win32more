from pathlib import Path

from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Markup import XamlReader
from win32more.Microsoft.UI.Xaml.Media import MicaBackdrop

from win32more.winui3 import XamlApplication


class App(XamlApplication):
    def OnLaunched(self, args):
        win = Window()
        win.SystemBackdrop = MicaBackdrop()
        win.Content = XamlReader.Load((Path(__file__).parent / "page.xaml").read_text())
        win.Activate()


XamlApplication.Start(App)
