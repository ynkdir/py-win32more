from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Controls import UserControl
from win32more.Windows.UI.Xaml.Interop import TypeKind

from win32more.appsdk.xaml import XamlApplication, XamlClass, XamlType


class App(XamlApplication):
    def OnLaunched(self, args):
        self._window = MainWindow()
        self._window.Activate()

    def GetXamlTypeByFullName(self, fullName):
        if fullName == "App.Counter":
            return XamlType("App.Counter", TypeKind.Custom, activate_instance=Counter)
        return super().GetXamlTypeByFullName(fullName)


class MainWindow(XamlClass, Window):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromString("""
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:local="using:App">

    <StackPanel>
        <Button x:Name="Button1" Content="Increment" Click="Button1_Click" />
        <local:Counter x:Name="Counter"/>
    </StackPanel>
</Window>
""")

    def Button1_Click(self, sender, e):
        self.Counter.increment()


class Counter(XamlClass, UserControl):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromString("""
<UserControl
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
    <TextBlock x:Name="TextBlock1" />
</UserControl>
""")
        self._counter = 0
        self.increment()

    def increment(self):
        self._counter += 1
        self.TextBlock1.Text = str(self._counter)


XamlApplication.Start(App)
