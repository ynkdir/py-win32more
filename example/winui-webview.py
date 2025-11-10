# https://learn.microsoft.com/en-us/microsoft-edge/webview2/get-started/winui


from win32more.Windows.Foundation import Uri
from win32more.winui3 import XamlApplication, XamlLoader

xaml = """
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    xmlns:controls="using:Microsoft.UI.Xaml.Controls"
    mc:Ignorable="d">

    <Grid>
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto"/>
            <RowDefinition Height="*"/>
        </Grid.RowDefinitions>
        <Grid.ColumnDefinitions>
            <ColumnDefinition Width="*"/>
            <ColumnDefinition Width="Auto"/>
        </Grid.ColumnDefinitions>

        <TextBox x:Name="addressBar" Grid.Column="0"/>
        <Button x:Name="myButton" Grid.Column="1" Click="myButton_Click">Go</Button>

        <controls:WebView2 x:Name="MyWebView" Grid.Row="1" Grid.ColumnSpan="2"
            Source="https://www.microsoft.com" HorizontalAlignment="Stretch" VerticalAlignment="Stretch"/>
    </Grid>
</Window>
"""


class App(XamlApplication):
    def OnLaunched(self, args):
        self._window = XamlLoader.Load(self, xaml)
        self._window.Activate()

    def myButton_Click(self, sender, e):
        try:
            targetUri = Uri(self.addressBar.Text)
            self.MyWebView.Source = targetUri
        except Exception as e:
            print(e)


if __name__ == "__main__":
    XamlApplication.Start(App)
