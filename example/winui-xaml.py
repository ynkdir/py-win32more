from pathlib import Path
from win32more.xaml import XamlApplication
from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Media import MicaBackdrop
from win32more.Microsoft.UI.Xaml.Markup import XamlReader

class App(XamlApplication):
    def OnLaunched(self, args):
        win = Window()
        win.SystemBackdrop = MicaBackdrop()
        win.Content = XamlReader.Load((Path(__file__).parent / "page.xaml").read_text())
        win.Activate()

XamlApplication.Start(App)
