from win32more.xaml import XamlApplication
from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Media import MicaBackdrop
from win32more.Microsoft.UI.Xaml.Markup import XamlReader

class App(XamlApplication):
    def OnLaunched(self, args):
        win = Window.CreateInstance(None, None)
        win.SystemBackdrop = MicaBackdrop.CreateInstance(None, None)
        with open("page.xaml", "r") as file:
            win.Content = XamlReader.Load(file.read())
        win.Activate()

XamlApplication.Start(App)
