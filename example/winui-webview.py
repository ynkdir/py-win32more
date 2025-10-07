# https://learn.microsoft.com/en-us/microsoft-edge/webview2/get-started/winui

from pathlib import Path

from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Controls import Button, Grid, TextBox, WebView2
from win32more.Microsoft.UI.Xaml.Markup import XamlReader
from win32more.Windows.Foundation import Uri

from win32more.appsdk.xaml import XamlApplication


class App(XamlApplication):
    def OnLaunched(self, args):
        win = XamlReader.Load((Path(__file__).parent / "winui-webview.xaml").read_text()).as_(Window)

        grid = win.Content.as_(Grid)

        self.addressBar = grid.FindName("addressBar").as_(TextBox)

        self.myButton = grid.FindName("myButton").as_(Button)
        self.myButton.add_Click(self.myButton_Click)

        self.MyWebView = grid.FindName("MyWebView").as_(WebView2)

        win.Activate()

    def myButton_Click(self, sender, e):
        try:
            targetUri = Uri(self.addressBar.Text)
            self.MyWebView.Source = targetUri
        except Exception as e:
            print(e)


XamlApplication.Start(App)
