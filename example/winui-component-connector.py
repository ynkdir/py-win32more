from pathlib import Path

from win32more.Microsoft.UI.Xaml import Application, Window
from win32more.Microsoft.UI.Xaml.Controls import Button
from win32more.Microsoft.UI.Xaml.Markup import IComponentConnector
from win32more.Windows.Foundation import Uri

from win32more import ComClass
from win32more.appsdk.xaml import XamlApplication


# Visual Studio generates connection code from xaml like this.
class MainWindow(ComClass, Window, IComponentConnector):
    def __init__(self):
        super().__init__(own=True)
        self.InitializeComponent()

    def InitializeComponent(self):
        # ms-appx:///foo.xaml is relative to python.exe.
        # Use absolute path.
        # mx-appx:///C:/Full/Path/To/My.xaml
        # NOTE: According to documentation, LoadComponent() takes relative location.
        xaml_path = Path(__file__).with_name("winui-component-connector.xaml").absolute().as_posix()
        resource_locator = Uri(f"ms-appx:///{xaml_path}")
        Application.LoadComponent(self, resource_locator)

    def Connect(self, connectionId, target):
        if connectionId == 1:
            self.Button1 = target.as_(Button)
            self.Button1.Click += self.Button1_Click
        elif connectionId == 2:
            self.Button2 = target.as_(Button)
            self.Button2.Click += self.Button2_Click

    def GetBindingConnector(self, connectionId, target):
        return None

    def Button1_Click(self, sender, e):
        text = self.Button1.Content.as_(str)
        self.Button1.Content = f"[{text}]"

    def Button2_Click(self, sender, e):
        text = self.Button2.Content.as_(str)
        self.Button2.Content = f"({text})"


class App(XamlApplication):
    def OnLaunched(self, args):
        self._window = MainWindow()
        self._window.Activate()


XamlApplication.Start(App)
