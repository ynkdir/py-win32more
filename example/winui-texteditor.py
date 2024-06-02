import re

from win32more.asyncui import async_start_runner
from win32more.Microsoft.UI.Xaml import FrameworkElement, Window
from win32more.Microsoft.UI.Xaml.Controls import MenuFlyoutItem, TextBox
from win32more.Microsoft.UI.Xaml.Markup import XamlReader
from win32more.Windows.Storage import FileIO
from win32more.Windows.Storage.Pickers import FileOpenPicker, FileSavePicker
from win32more.Windows.UI.Popups import MessageDialog
from win32more.Windows.Win32.UI.Shell import IInitializeWithWindow
from win32more.xaml import XamlApplication


class App(XamlApplication):
    def OnLaunched(self, args):
        self._window = XamlReader.Load("""
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    xmlns:muxc="using:Microsoft.UI.Xaml.Controls">

    <Grid>
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto" />
            <RowDefinition Height="*" />
        </Grid.RowDefinitions>
        <Grid.ColumnDefinitions>
            <ColumnDefinition Width="*" />
        </Grid.ColumnDefinitions>

        <muxc:MenuBar Grid.Row="0">
            <muxc:MenuBarItem Title="File">
                <muxc:MenuFlyoutItem x:Name="menu_file_open" Text="Open" />
                <muxc:MenuFlyoutItem x:Name="menu_file_save" Text="Save" />
                <muxc:MenuFlyoutItem x:Name="menu_file_saveas" Text="Save As" />
                <muxc:MenuFlyoutItem x:Name="menu_file_exit" Text="Exit" />
            </muxc:MenuBarItem>
        </muxc:MenuBar>

        <TextBox Grid.Row="1" x:Name="textbox" AcceptsReturn="True" TextWrapping="Wrap" ScrollViewer.VerticalScrollBarVisibility="Auto" />

    </Grid>
</Window>
""").as_(Window)

        self._window.Title = "Text Editor"

        framework_element = self._window.Content.as_(FrameworkElement)

        self._textbox = framework_element.FindName("textbox").as_(TextBox)

        framework_element.FindName("menu_file_open").as_(MenuFlyoutItem).Click += self._on_menu_file_open
        framework_element.FindName("menu_file_save").as_(MenuFlyoutItem).Click += self._on_menu_file_save
        framework_element.FindName("menu_file_saveas").as_(MenuFlyoutItem).Click += self._on_menu_file_saveas
        framework_element.FindName("menu_file_exit").as_(MenuFlyoutItem).Click += self._on_menu_file_exit

        self._window.Activate()

        self._storage_file = None

    async def _on_menu_file_open(self, sender, e):
        storage_file = await self._file_open_dialog(".txt")
        if not storage_file.value:
            return
        try:
            text = await FileIO.ReadTextAsync(storage_file)
        except Exception as e:
            await self._message_box(str(e), "error")
            return
        self._textbox.Text = text
        self._storage_file = storage_file

    async def _on_menu_file_save(self, sender, e):
        if not self._storage_file:
            storage_file = await self._file_save_dialog()
            if not storage_file:
                return
            self._storage_file = storage_file
        # it seems textbox's newline is \r.
        text = re.sub(r"\r\n|\r|\n", "\r\n", self._textbox.Text)
        await FileIO.WriteTextAsync(self._storage_file, text)

    async def _on_menu_file_saveas(self, sender, e):
        storage_file = await self._file_save_dialog()
        if not storage_file:
            return
        self._storage_file = storage_file
        text = re.sub(r"\r\n|\r|\n", "\r\n", self._textbox.Text)
        await FileIO.WriteTextAsync(self._storage_file, text)

    def _on_menu_file_exit(self, sender, e):
        self.Exit()

    async def _file_open_dialog(self, filter_):
        hwnd = self._window.AppWindow.Id.Value
        picker = FileOpenPicker()
        picker.as_(IInitializeWithWindow).Initialize(hwnd)
        picker.FileTypeFilter.Append(filter_)
        return await picker.PickSingleFileAsync()

    async def _file_save_dialog(self):
        hwnd = self._window.AppWindow.Id.Value
        picker = FileSavePicker()
        picker.as_(IInitializeWithWindow).Initialize(hwnd)
        picker.FileTypeChoices.Insert("Plain Text", [".txt"])
        return await picker.PickSaveFileAsync()

    async def _message_box(self, content, title):
        hwnd = self._window.AppWindow.Id.Value
        dialog = MessageDialog(content, title)
        dialog.as_(IInitializeWithWindow).Initialize(hwnd)
        await dialog.ShowAsync()


if __name__ == "__main__":
    async_start_runner()
    XamlApplication.Start(App)
