import re
from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import ContentDialog
from win32more.Microsoft.Windows.Storage.Pickers import FileOpenPicker, FileSavePicker

from win32more.appsdk.xaml import XamlApplication, XamlLoader


class App(XamlApplication):
    def OnLaunched(self, args):
        self._window = XamlLoader.Load(
            self,
            """
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d"
    xmlns:muxc="using:Microsoft.UI.Xaml.Controls"
    Activated="_window_Activated">

    <Grid x:Name="_grid">
        <Grid.RowDefinitions>
            <RowDefinition Height="Auto" />
            <RowDefinition Height="*" />
        </Grid.RowDefinitions>
        <Grid.ColumnDefinitions>
            <ColumnDefinition Width="*" />
        </Grid.ColumnDefinitions>

        <muxc:MenuBar Grid.Row="0">
            <muxc:MenuBarItem Title="File">
                <muxc:MenuFlyoutItem x:Name="_menu_file_open" Text="Open" Click="_menu_file_open_Click" />
                <muxc:MenuFlyoutItem x:Name="_menu_file_save" Text="Save" Click="_menu_file_save_Click" />
                <muxc:MenuFlyoutItem x:Name="_menu_file_saveas" Text="Save As" Click="_menu_file_saveas_Click" />
                <muxc:MenuFlyoutItem x:Name="_menu_file_exit" Text="Exit" Click="_menu_file_exit_Click" />
            </muxc:MenuBarItem>
            <muxc:MenuBarItem Title="Edit">
                <!-- FIXME: How to use Binding? IsEnabled="{Binding ElementName=textbox, Path=CanUndo}" -->
                <muxc:MenuFlyoutItem x:Name="_menu_edit_undo" Text="Undo" IsEnabled="False" Click="_menu_edit_undo_Click" />
                <muxc:MenuFlyoutItem x:Name="_menu_edit_redo" Text="Redo" IsEnabled="False" Click="_menu_edit_redo_Click" />
                <muxc:MenuFlyoutItem x:Name="_menu_edit_cut" Text="Cut" IsEnabled="False" Click="_menu_edit_cut_Click" />
                <muxc:MenuFlyoutItem x:Name="_menu_edit_copy" Text="Copy" IsEnabled="False" Click="_menu_edit_copy_Click" />
                <muxc:MenuFlyoutItem x:Name="_menu_edit_paste" Text="Paste" IsEnabled="False" Click="_menu_edit_paste_Click" />
                <muxc:MenuFlyoutItem x:Name="_menu_edit_delete" Text="Delete" IsEnabled="False" Click="_menu_edit_delete_Click" />
            </muxc:MenuBarItem>
        </muxc:MenuBar>

        <TextBox x:Name="_textbox" Grid.Row="1" AcceptsReturn="True" TextWrapping="Wrap" ScrollViewer.VerticalScrollBarVisibility="Auto" TextChanged="_textbox_TextChanged" SelectionChanged="_textbox_SelectionChanged" />

    </Grid>
</Window>
""",
        )

        self._window.Title = "Text Editor"  # cannot set in xaml when using XamlReader
        self._window.Activate()
        self._current_file = None

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
        path = await self._file_open_dialog(".txt")
        if not path:
            return
        try:
            text = Path(path).read_text()
        except Exception as e:
            await self._message_box(str(e), "error")
            return
        self._textbox.Text = text
        self._current_file = path

    async def _menu_file_save_Click(self, sender, e):
        if not self._current_file:
            path = await self._file_save_dialog()
            if not path:
                return
            self._current_file = path
        # it seems textbox's newline is \r.
        text = re.sub(r"\r\n|\r|\n", "\r\n", self._textbox.Text)
        Path(self._current_file).write_text(text, newline="")

    async def _menu_file_saveas_Click(self, sender, e):
        path = await self._file_save_dialog()
        if not path:
            return
        self._current_file = path
        text = re.sub(r"\r\n|\r|\n", "\r\n", self._textbox.Text)
        Path(self._current_file).write_text(text, newline="")

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
        picker = FileOpenPicker(self._window.AppWindow.Id)
        picker.FileTypeFilter.Append(filter_)
        r = await picker.PickSingleFileAsync()
        if not r:
            return None
        return r.Path

    async def _file_save_dialog(self):
        picker = FileSavePicker(self._window.AppWindow.Id)
        picker.FileTypeChoices.Insert("Plain Text", [".txt"])
        r = await picker.PickSaveFileAsync()
        if not r:
            return None
        return r.Path

    async def _message_box(self, content, title):
        dialog = ContentDialog()
        dialog.XamlRoot = self._grid.XamlRoot
        dialog.Title = title
        dialog.Content = content
        dialog.CloseButtonText = "Ok"
        await dialog.ShowAsync()


if __name__ == "__main__":
    XamlApplication.Start(App)
