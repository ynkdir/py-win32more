from typing import override

from win32more.Microsoft.UI.Xaml import FrameworkElement, Window
from win32more.Microsoft.UI.Xaml.Controls import Frame, NavigationView, NavigationViewItem, Page
from win32more.Microsoft.UI.Xaml.Markup import XamlReader
from win32more.Windows.UI.Xaml.Interop import TypeKind

from win32more.winui3 import XamlApplication, XamlType, xaml_typename

xaml_window = """
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d">

    <Window.SystemBackdrop>
        <MicaBackdrop Kind="BaseAlt" />
    </Window.SystemBackdrop>

    <NavigationView x:Name="NavView" IsBackButtonVisible="Collapsed">
        <NavigationView.MenuItems>
            <NavigationViewItem Tag="App.Home" Content="Home" Icon="Home" />
            <NavigationViewItem Tag="App.Page2" Content="Page2" Icon="Audio" />
        </NavigationView.MenuItems>
        <Frame x:Name="ContentFrame" />
    </NavigationView>

</Window>
"""

xaml_home = """
<Page
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d">

    <StackPanel HorizontalAlignment="Center" VerticalAlignment="Center">
        <TextBlock Text="NavigationView Example" FontSize="40" Padding="10" HorizontalAlignment="Center" />
        <HyperlinkButton Content="NavigationView Class" NavigateUri="https://learn.microsoft.com/en-us/windows/winui/api/microsoft.ui.xaml.controls.navigationview"/>
        <HyperlinkButton Content="NavigationView" NavigateUri="https://learn.microsoft.com/en-us/windows/apps/design/controls/navigationview"/>
        <HyperlinkButton Content="Navigation design basics for Windows apps" NavigateUri="https://learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics"/>
    </StackPanel>

</Page>
"""

xaml_page2 = """
<Page
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d">

    <StackPanel HorizontalAlignment="Center" VerticalAlignment="Center">
        <TextBlock Text="Page2" FontSize="40" Padding="10" HorizontalAlignment="Center" />
    </StackPanel>

</Page>
"""

xaml_settings = """
<Page
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d">

    <StackPanel HorizontalAlignment="Center" VerticalAlignment="Center">
        <TextBlock Text="Settings" FontSize="40" Padding="10" HorizontalAlignment="Center" />
    </StackPanel>

</Page>
"""


class App(XamlApplication):
    @override
    def OnLaunched(self, args):
        win = XamlReader.Load(xaml_window).as_(Window)

        self.ContentFrame = win.Content.as_(FrameworkElement).FindName("ContentFrame").as_(Frame)

        self.NavView = win.Content.as_(FrameworkElement).FindName("NavView").as_(NavigationView)

        # Setup event handler
        self.NavView.SelectionChanged += self.NavView_SelectionChanged

        # Select first item
        self.NavView.SelectedItem = self.NavView.MenuItems[0]

        win.Activate()

    # Return XamlType for navigation.
    @override
    def GetXamlTypeByFullName(self, typename):
        if typename == "App.Home":
            return XamlType("App.Home", TypeKind.Custom, activate_instance=Home)
        elif typename == "App.Page2":
            return XamlType("App.Page2", TypeKind.Custom, activate_instance=lambda: XamlReader.Load(xaml_page2))
        elif typename == "Settings":
            return XamlType("Settings", TypeKind.Custom, activate_instance=lambda: XamlReader.Load(xaml_settings))
        return super().GetXamlTypeByFullName(typename)

    def NavView_SelectionChanged(self, navigation_view, args):
        item = args.SelectedItem.as_(NavigationViewItem)
        typename = item.Tag.as_(str)

        # Navigate() implies GetXamlTypeByFullName() querying.
        self.ContentFrame.Navigate(xaml_typename(typename, TypeKind.Custom))


class Home(Page):
    def __init__(self):
        # Application.LoadComponent() should probably be used.
        super().__init__(move=XamlReader.Load(xaml_home))


XamlApplication.Start(App)
