import re

from win32more.Microsoft.UI.Xaml import FrameworkElement, Window
from win32more.Microsoft.UI.Xaml.Controls import ContentDialog, MenuFlyoutItem, TextBox
from win32more.Microsoft.UI.Xaml.Markup import XamlReader
from win32more.Windows.Storage import FileIO
from win32more.Windows.Storage.Pickers import FileOpenPicker, FileSavePicker
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
            <muxc:MenuBarItem Title="Edit">
                <!-- FIXME: How to use Binding? IsEnabled="{Binding ElementName=textbox, Path=CanUndo}" -->
                <muxc:MenuFlyoutItem x:Name="menu_edit_undo" Text="Undo" IsEnabled="False" />
                <muxc:MenuFlyoutItem x:Name="menu_edit_redo" Text="Redo" IsEnabled="False" />
                <muxc:MenuFlyoutItem x:Name="menu_edit_cut" Text="Cut" IsEnabled="False" />
                <muxc:MenuFlyoutItem x:Name="menu_edit_copy" Text="Copy" IsEnabled="False" />
                <muxc:MenuFlyoutItem x:Name="menu_edit_paste" Text="Paste" IsEnabled="False" />
                <muxc:MenuFlyoutItem x:Name="menu_edit_delete" Text="Delete" IsEnabled="False" />
            </muxc:MenuBarItem>
        </muxc:MenuBar>

        <TextBox Grid.Row="1" x:Name="textbox" AcceptsReturn="True" TextWrapping="Wrap" ScrollViewer.VerticalScrollBarVisibility="Auto" />

    </Grid>
</Window>
""").as_(Window)

        self._window.Title = "Text Editor"
        self._window.Activated += self._window_Activated

        framework_element = self._window.Content.as_(FrameworkElement)

        self._textbox = framework_element.FindName("textbox").as_(TextBox)
        self._textbox.TextChanged += self._textbox_TextChanged
        self._textbox.SelectionChanged += self._textbox_SelectionChanged

        framework_element.FindName("menu_file_open").as_(MenuFlyoutItem).Click += self._menu_file_open_Click

        framework_element.FindName("menu_file_save").as_(MenuFlyoutItem).Click += self._menu_file_save_Click

        framework_element.FindName("menu_file_saveas").as_(MenuFlyoutItem).Click += self._menu_file_saveas_Click

        framework_element.FindName("menu_file_exit").as_(MenuFlyoutItem).Click += self._menu_file_exit_Click

        self._menu_edit_undo = framework_element.FindName("menu_edit_undo").as_(MenuFlyoutItem)
        self._menu_edit_undo.Click += self._menu_edit_undo_Click

        self._menu_edit_redo = framework_element.FindName("menu_edit_redo").as_(MenuFlyoutItem)
        self._menu_edit_redo.Click += self._menu_edit_redo_Click

        self._menu_edit_cut = framework_element.FindName("menu_edit_cut").as_(MenuFlyoutItem)
        self._menu_edit_cut.Click += self._menu_edit_cut_Click

        self._menu_edit_copy = framework_element.FindName("menu_edit_copy").as_(MenuFlyoutItem)
        self._menu_edit_copy.Click += self._menu_edit_copy_Click

        self._menu_edit_paste = framework_element.FindName("menu_edit_paste").as_(MenuFlyoutItem)
        self._menu_edit_paste.Click += self._menu_edit_paste_Click

        self._menu_edit_delete = framework_element.FindName("menu_edit_delete").as_(MenuFlyoutItem)
        self._menu_edit_delete.Click += self._menu_edit_delete_Click

        self._window.Activate()

        self._storage_file = None

    def _window_Activated(self, sender, e):
        self._menu_edit_paste.IsEnabled = self._textbox.CanPasteClipboardContent

    def _textbox_TextChanged(self, sender, e):
        self._menu_edit_undo.IsEnabled = self._textbox.CanUndo
        self._menu_edit_redo.IsEnabled = self._textbox.CanRedo

    def _textbox_SelectionChanged(self, sender, e):
        if self._textbox.SelectionLength == 0:
            self._menu_edit_cut.IsEnabled = False
            self._menu_edit_copy.IsEnabled = False
            self._menu_edit_delete.IsEnabled = False
        else:
            self._menu_edit_cut.IsEnabled = True
            self._menu_edit_copy.IsEnabled = True
            self._menu_edit_delete.IsEnabled = True

    async def _menu_file_open_Click(self, sender, e):
        storage_file = await self._file_open_dialog(".txt")
        if not storage_file:
            return
        try:
            text = await FileIO.ReadTextAsync(storage_file)
        except Exception as e:
            await self._message_box(str(e), "error")
            return
        self._textbox.Text = text
        self._storage_file = storage_file

    async def _menu_file_save_Click(self, sender, e):
        if not self._storage_file:
            storage_file = await self._file_save_dialog()
            if not storage_file:
                return
            self._storage_file = storage_file
        # it seems textbox's newline is \r.
        text = re.sub(r"\r\n|\r|\n", "\r\n", self._textbox.Text)
        await FileIO.WriteTextAsync(self._storage_file, text)

    async def _menu_file_saveas_Click(self, sender, e):
        storage_file = await self._file_save_dialog()
        if not storage_file:
            return
        self._storage_file = storage_file
        text = re.sub(r"\r\n|\r|\n", "\r\n", self._textbox.Text)
        await FileIO.WriteTextAsync(self._storage_file, text)

    def _menu_file_exit_Click(self, sender, e):
        self.Exit()

    def _menu_edit_undo_Click(self, sender, e):
        self._textbox.Undo()

    def _menu_edit_redo_Click(self, sender, e):
        self._textbox.Redo()

    def _menu_edit_cut_Click(self, sender, e):
        self._textbox.CutSelectionToClipboard()
        self._menu_edit_paste.IsEnabled = True

    def _menu_edit_copy_Click(self, sender, e):
        self._textbox.CopySelectionToClipboard()
        self._menu_edit_paste.IsEnabled = True

    def _menu_edit_paste_Click(self, sender, e):
        self._textbox.PasteFromClipboard()

    def _menu_edit_delete_Click(self, sender, e):
        self._textbox.SelectedText = ""

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
        dialog = ContentDialog()
        dialog.XamlRoot = self._window.Content.as_(FrameworkElement).XamlRoot
        dialog.Title = title
        dialog.Content = content
        dialog.CloseButtonText = "Ok"
        await dialog.ShowAsync()


if __name__ == "__main__":
    XamlApplication.Start(App)
