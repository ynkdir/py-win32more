import operator

from win32more.Microsoft.UI.Xaml.Controls import Button

from win32more.appsdk.xaml import XamlApplication, XamlLoader


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

        <TextBlock x:Name="TextBlock1" Grid.Column="0" Grid.Row="0" Grid.ColumnSpan="4" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" HorizontalTextAlignment="Right" FontSize="42" Margin="0,0,20,0">0</TextBlock>

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

        self._model = Calc(View(self.TextBlock1))

    def _on_button_click(self, sender, e):
        cmd = sender.as_(Button).Content.as_(str)
        self._model.input(cmd)


class View:
    def __init__(self, textblock):
        self._textblock = textblock

    def display(self, text):
        self._textblock.Text = text


class Calc:
    def __init__(self, view):
        self._view = view
        self._state = LhsState(self, view, "0")
        self._view.display("0")

    def input(self, cmd):
        self._state.input(cmd)

    def eval(self, lhs, op, rhs):
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "%": operator.mod,
        }

        result = operators[op](float(lhs), float(rhs))
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        return str(result)


class LhsState:
    def __init__(self, model, view, lhs):
        self._model = model
        self._view = view
        self._lhs = lhs

    def input(self, cmd):
        if cmd in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            if self._lhs == "0":
                if cmd != "0":
                    self._lhs = cmd
            elif self._lhs == "-0":
                if cmd != "0":
                    self._lhs = "-" + cmd
            else:
                self._lhs += cmd
            self._view.display(self._lhs)
        elif cmd in {"+", "-", "*", "/", "%"}:
            self._model._state = OpState(self._model, self._view, self._lhs, cmd)
            self._view.display(self._lhs + " " + cmd)
        elif cmd == ".":
            if "." not in self._lhs:
                self._lhs += "."
            self._view.display(self._lhs)
        elif cmd == "+/-":
            if self._lhs.startswith("-"):
                self._lhs = self._lhs[1:]
            else:
                self._lhs = "-" + self._lhs
            self._view.display(self._lhs)
        elif cmd == "CE":
            self._lhs = "0"
            self._view.display(self._lhs)
        elif cmd == "C":
            self._lhs = "0"
            self._view.display(self._lhs)
        elif cmd == "=":
            self._view.display(self._lhs)


class OpState:
    def __init__(self, model, view, lhs, op):
        self._model = model
        self._view = view
        self._lhs = lhs
        self._op = op

    def input(self, cmd):
        if cmd in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            self._model._state = RhsState(self._model, self._view, self._lhs, self._op, cmd)
            self._view.display(self._lhs + " " + self._op + " " + cmd)
        elif cmd in {"+", "-", "*", "/", "%"}:
            self._op = cmd
            self._view.display(self._lhs + " " + self._op)
        elif cmd == ".":
            self._model._state = RhsState(self._model, self._view, self._lhs, self._op, "0.")
            self._view.display(self._lhs + " " + self._op + " 0.")
        elif cmd == "+/-":
            self._model._state = RhsState(self._model, self._view, self._lhs, self._op, "-0")
            self._view.display(self._lhs + " " + self._op + " -0")
        elif cmd == "CE":
            self._view.display(self._lhs + " " + self._op)
        elif cmd == "C":
            self._model._state = LhsState(self._model, self._view, "0")
            self._view.display("0")
        elif cmd == "=":
            try:
                result = self._model.eval(self._lhs, self._op, self._lhs)
            except ZeroDivisionError as e:
                self._model._state = LhsState(self._model, self._view, "0")
                self._view.display(str(e))
            else:
                self._model._state = LhsState(self._model, self._view, result)
                self._view.display(result)


class RhsState:
    def __init__(self, model, view, lhs, op, rhs):
        self._model = model
        self._view = view
        self._lhs = lhs
        self._op = op
        self._rhs = rhs

    def input(self, cmd):
        if cmd in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            if self._rhs == "0":
                if cmd != "0":
                    self._rhs = cmd
            elif self._rhs == "-0":
                if cmd != "0":
                    self._rhs = "-" + cmd
            else:
                self._rhs += cmd
            self._view.display(self._lhs + " " + self._op + " " + self._rhs)
        elif cmd in {"+", "-", "*", "/", "%"}:
            try:
                result = self._model.eval(self._lhs, self._op, self._rhs)
            except ZeroDivisionError as e:
                self._model._state = LhsState(self._model, self._view, "0")
                self._view.display(str(e))
            else:
                self._model._state = OpState(self._model, self._view, result, cmd)
                self._view.display(result + " " + cmd)
        elif cmd == ".":
            if "." not in self._rhs:
                self._rhs += "."
            self._view.display(self._lhs + " " + self._op + " " + self._rhs)
        elif cmd == "+/-":
            if self._rhs.startswith("-"):
                self._rhs = self._rhs[1:]
            else:
                self._rhs = "-" + self._rhs
            self._view.display(self._lhs + " " + self._op + " " + self._rhs)
        elif cmd == "CE":
            self._rhs = "0"
            self._view.display(self._lhs + " " + self._op + " " + self._rhs)
        elif cmd == "C":
            self._model._state = LhsState(self._model, self._view, "0")
            self._view.display("0")
        elif cmd == "=":
            try:
                result = self._model.eval(self._lhs, self._op, self._rhs)
            except ZeroDivisionError as e:
                self._model._state = LhsState(self._model, self._view, "0")
                self._view.display(str(e))
            else:
                self._model._state = LhsState(self._model, self._view, result)
                self._view.display(result)


XamlApplication.Start(App)
