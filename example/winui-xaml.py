from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Markup import XamlReader
from win32more.Microsoft.UI.Xaml.Media import MicaBackdrop
from win32more.winui3 import XamlApplication

xaml = """
<Page xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation">
    <NavigationView IsBackButtonVisible="Collapsed">
        <NavigationView.MenuItems>
            <NavigationViewItem Content="Home" Icon="Home" />
        </NavigationView.MenuItems>
        <Frame>
            <StackPanel HorizontalAlignment="Center" VerticalAlignment="Center">
                <TextBlock Text="WinUI 3 with Python!" FontSize="40" Padding="10" HorizontalAlignment="Center" />
                <HyperlinkButton Content="GitHub repository" NavigateUri="https://github.com/ynkdir/py-win32more" HorizontalAlignment="Center" />
            </StackPanel>
        </Frame>
    </NavigationView>
</Page>
"""


class App(XamlApplication):
    def OnLaunched(self, args):
        win = Window()
        win.SystemBackdrop = MicaBackdrop()
        win.Content = XamlReader.Load(xaml)
        win.Activate()


XamlApplication.Start(App)
