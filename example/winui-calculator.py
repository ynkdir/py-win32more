from win32more.Microsoft.UI.Xaml.Controls import Button
from win32more.xaml import XamlApplication, XamlLoader


class App(XamlApplication):
    def OnLaunched(self, args):
        self.window = XamlLoader.Load(
            self,
            """
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    mc:Ignorable="d">

    <Grid>
        <Grid.RowDefinitions>
            <RowDefinition />
            <RowDefinition />
            <RowDefinition />
            <RowDefinition />
            <RowDefinition />
            <RowDefinition />
        </Grid.RowDefinitions>
        <Grid.ColumnDefinitions>
            <ColumnDefinition />
            <ColumnDefinition />
            <ColumnDefinition />
            <ColumnDefinition />
        </Grid.ColumnDefinitions>

        <TextBlock x:Name="DisplayBox" Grid.Column="0" Grid.Row="0" Grid.ColumnSpan="4" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" HorizontalTextAlignment="Right" FontSize="42" Margin="0,0,20,0">0</TextBlock>

        <Button x:Name="BPercent" Grid.Column="0" Grid.Row="1" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">%</Button>
        <Button x:Name="BCE" Grid.Column="1" Grid.Row="1" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">CE</Button>
        <Button x:Name="BC" Grid.Column="2" Grid.Row="1" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">C</Button>
        <Button x:Name="BDevide" Grid.Column="3" Grid.Row="1" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">/</Button>

        <Button x:Name="B7" Grid.Column="0" Grid.Row="2" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">7</Button>
        <Button x:Name="B8" Grid.Column="1" Grid.Row="2" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">8</Button>
        <Button x:Name="B9" Grid.Column="2" Grid.Row="2" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">9</Button>
        <Button x:Name="BMultiply" Grid.Column="3" Grid.Row="2" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">*</Button>

        <Button x:Name="B4" Grid.Column="0" Grid.Row="3" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">4</Button>
        <Button x:Name="B5" Grid.Column="1" Grid.Row="3" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">5</Button>
        <Button x:Name="B6" Grid.Column="2" Grid.Row="3" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">6</Button>
        <Button x:Name="BMinus" Grid.Column="3" Grid.Row="3" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">-</Button>

        <Button x:Name="B1" Grid.Column="0" Grid.Row="4" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">1</Button>
        <Button x:Name="B2" Grid.Column="1" Grid.Row="4" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">2</Button>
        <Button x:Name="B3" Grid.Column="2" Grid.Row="4" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">3</Button>
        <Button x:Name="BPlus" Grid.Column="3" Grid.Row="4" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">+</Button>

        <Button x:Name="BPM" Grid.Column="0" Grid.Row="5" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">+/-</Button>
        <Button x:Name="B0" Grid.Column="1" Grid.Row="5" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">0</Button>
        <Button x:Name="BPeriod" Grid.Column="2" Grid.Row="5" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">.</Button>
        <Button x:Name="BEqual" Grid.Column="3" Grid.Row="5" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click">=</Button>

    </Grid>
</Window>
""",
        )

        self.window.Activate()

        self._lhs = "0"
        self._rhs = ""
        self._op = ""
        self._state = "lhs"

    def _on_button_click(self, sender, e):
        cmd = sender.as_(Button).Content.as_(str)

        if self._state == "lhs":
            if cmd in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if self._lhs == "0":
                    if cmd != "0":
                        self._lhs = cmd
                elif self._lhs == "-0":
                    if cmd != "0":
                        self._lhs = "-" + cmd
                else:
                    self._lhs += cmd
                display = self._lhs
            elif cmd in ["+", "-", "*", "/", "%"]:
                self._state = "op"
                self._op = cmd
                display = self._lhs + " " + self._op
            elif cmd == ".":
                if "." not in self._lhs:
                    self._lhs += "."
                display = self._lhs
            elif cmd == "+/-":
                if self._lhs.startswith("-"):
                    self._lhs = self._lhs[1:]
                else:
                    self._lhs = "-" + self._lhs
                display = self._lhs
            elif cmd == "CE":
                self._lhs = "0"
                display = self._lhs
            elif cmd == "C":
                self._state = "lhs"
                self._lhs = "0"
                display = self._lhs
            elif cmd == "=":
                display = self._lhs
                self._lhs = "0"
        elif self._state == "op":
            if cmd in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                self._state = "rhs"
                self._rhs = cmd
                display = self._lhs + " " + self._op + " " + self._rhs
            elif cmd in ["+", "-", "*", "/", "%"]:
                self._op = cmd
                display = self._lhs + " " + self._op
            elif cmd == ".":
                self._state = "rhs"
                self._rhs = "0."
                display = self._lhs + " " + self._op + " " + self._rhs
            elif cmd == "+/-":
                self._state = "rhs"
                self._rhs = "-0"
                display = self._lhs + " " + self._op + " " + self._rhs
            elif cmd == "CE":
                display = self._lhs + " " + self._op
            elif cmd == "C":
                self._state = "lhs"
                self._lhs = "0"
                self._rhs = ""
                self._op = ""
                display = "0"
            elif cmd == "=":
                try:
                    display = str(eval(self._lhs + self._op + self._lhs))
                except Exception as e:
                    display = str(e)
                self._state = "lhs"
                self._lhs = "0"
                self._rhs = ""
                self._op = ""
        elif self._state == "rhs":
            if cmd in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if self._rhs == "0":
                    if cmd != "0":
                        self._rhs = cmd
                elif self._rhs == "-0":
                    if cmd != "0":
                        self._rhs = "-" + cmd
                else:
                    self._rhs += cmd
                display = self._lhs + " " + self._op + " " + self._rhs
            elif cmd in ["+", "-", "*", "/", "%"]:
                display = self._lhs + " " + self._op + " " + self._rhs
            elif cmd == ".":
                if "." not in self._rhs:
                    self._rhs += "."
                display = self._lhs + " " + self._op + " " + self._rhs
            elif cmd == "+/-":
                if self._rhs.startswith("-"):
                    self._rhs = self._rhs[1:]
                else:
                    self._rhs = "-" + self._rhs
                display = self._lhs + " " + self._op + " " + self._rhs
            elif cmd == "CE":
                self._rhs = "0"
                display = self._lhs + " " + self._op + " " + self._rhs
            elif cmd == "C":
                self._state = "lhs"
                self._lhs = "0"
                self._rhs = ""
                self._op = ""
                display = "0"
            elif cmd == "=":
                try:
                    display = str(eval(self._lhs + self._op + self._rhs))
                except Exception as e:
                    display = str(e)
                self._state = "lhs"
                self._lhs = "0"
                self._rhs = ""
                self._op = ""
        else:
            assert False

        self.DisplayBox.Text = display


XamlApplication.Start(App)
