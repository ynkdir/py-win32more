from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Controls import ColorPicker

from win32more.appsdk.xaml import XamlApplication


class App(XamlApplication):
    def OnLaunched(self, args):
        win = Window()
        clr = ColorPicker()
        win.Content = clr
        win.Activate()


XamlApplication.Start(App)
