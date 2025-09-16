import operator
from decimal import Decimal

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

        <TextBlock x:Name="TextBlock1" Grid.Column="0" Grid.Row="0" Grid.ColumnSpan="4" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" HorizontalTextAlignment="Right" FontFamily="Aptos-Mono" FontSize="42" Margin="0,0,20,0">0</TextBlock>

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

    def display(self, lhs, op="", rhs=""):
        self._textblock.Text = f"{lhs} {op} {rhs}".strip()

    def error(self, msg):
        self._textblock.Text = msg


class Calc:
    def __init__(self, view):
        self._view = view
        self._state = LhsState(self, view, Number("0"))
        self._view.display("0")

    def input(self, cmd):
        self._state.input(cmd)


class LhsState:
    def __init__(self, model, view, lhs):
        self._model = model
        self._view = view
        self._lhs = lhs

    def input(self, cmd):
        if cmd in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "+/-"}:
            self._lhs.input(cmd)
            self._view.display(self._lhs)
        elif cmd in {"+", "-", "*", "/", "%"}:
            op = Operator(cmd)
            self._model._state = OpState(self._model, self._view, self._lhs, op)
            self._view.display(self._lhs, op)
        elif cmd == "CE":
            self._lhs = Number("0")
            self._view.display(self._lhs)
        elif cmd == "C":
            self._lhs = Number("0")
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
        if cmd in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "+/-"}:
            if cmd == ".":
                rhs = Number("0.")
            elif cmd == "+/-":
                rhs = Number("-0")
            else:
                rhs = Number(cmd)
            self._model._state = RhsState(self._model, self._view, self._lhs, self._op, rhs)
            self._view.display(self._lhs, self._op, rhs)
        elif cmd in {"+", "-", "*", "/", "%"}:
            self._op = Operator(cmd)
            self._view.display(self._lhs, self._op)
        elif cmd == "CE":
            self._view.display(self._lhs, self._op)
        elif cmd == "C":
            lhs = Number("0")
            self._model._state = LhsState(self._model, self._view, lhs)
            self._view.display(lhs)
        elif cmd == "=":
            try:
                lhs = self._op(self._lhs, self._lhs)
            except ZeroDivisionError:
                self._model._state = LhsState(self._model, self._view, Number("0"))
                self._view.error("Cannot divide by zero")
            else:
                self._model._state = ResultState(self._model, self._view, lhs, self._op, self._lhs)
                self._view.display(lhs)


class RhsState:
    def __init__(self, model, view, lhs, op, rhs):
        self._model = model
        self._view = view
        self._lhs = lhs
        self._op = op
        self._rhs = rhs

    def input(self, cmd):
        if cmd in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "+/-"}:
            self._rhs.input(cmd)
            self._view.display(self._lhs, self._op, self._rhs)
        elif cmd in {"+", "-", "*", "/", "%"}:
            try:
                lhs = self._op(self._lhs, self._rhs)
            except ZeroDivisionError:
                self._model._state = LhsState(self._model, self._view, Number("0"))
                self._view.error("Cannot divide by zero")
            else:
                op = Operator(cmd)
                self._model._state = OpState(self._model, self._view, lhs, op)
                self._view.display(lhs, op)
        elif cmd == "CE":
            self._rhs = Number("0")
            self._view.display(self._lhs, self._op, self._rhs)
        elif cmd == "C":
            lhs = Number("0")
            self._model._state = LhsState(self._model, self._view, lhs)
            self._view.display(lhs)
        elif cmd == "=":
            try:
                lhs = self._op(self._lhs, self._rhs)
            except ZeroDivisionError:
                self._model._state = LhsState(self._model, self._view, Number("0"))
                self._view.error("Cannot divide by zero")
            else:
                self._model._state = ResultState(self._model, self._view, lhs, self._op, self._rhs)
                self._view.display(lhs)


class ResultState:
    def __init__(self, model, view, lhs, op, rhs):
        self._model = model
        self._view = view
        self._lhs = lhs
        self._op = op
        self._rhs = rhs

    def input(self, cmd):
        if cmd in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}:
            if cmd == ".":
                lhs = Number("0.")
            else:
                lhs = Number(cmd)
            self._model._state = LhsState(self._model, self._view, lhs)
            self._view.display(lhs)
        elif cmd == "+/-":
            self._lhs.input(cmd)
            self._view.display(self._lhs)
        elif cmd in {"+", "-", "*", "/", "%"}:
            op = Operator(cmd)
            self._model._state = OpState(self._model, self._view, self._lhs, op)
            self._view.display(self._lhs, op)
        elif cmd == "CE":
            lhs = Number("0")
            self._model._state = LhsState(self._model, self._view, lhs)
            self._view.display(lhs)
        elif cmd == "C":
            lhs = Number("0")
            self._model._state = LhsState(self._model, self._view, lhs)
            self._view.display(lhs)
        elif cmd == "=":
            try:
                self._lhs = self._op(self._lhs, self._rhs)
            except ZeroDivisionError:
                self._model._state = LhsState(self._model, self._view, Number("0"))
                self._view.error("Cannot divide by zero")
            else:
                self._view.display(self._lhs)


class Number:
    def __init__(self, num):
        self._num = num

    def input(self, cmd):
        if cmd in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            if self._num == "0":
                if cmd != "0":
                    self._num = cmd
            elif self._num == "-0":
                if cmd != "0":
                    self._num = "-" + cmd
            else:
                self._num += cmd
        elif cmd == ".":
            if "." not in self._num:
                self._num += "."
        elif cmd == "+/-":
            if self._num.startswith("-"):
                self._num = self._num[1:]
            else:
                self._num = "-" + self._num

    def __str__(self):
        return self._num

    def decimal(self):
        return Decimal(self._num)


class Operator:
    def __init__(self, op):
        self._op = op

    def __str__(self):
        return self._op

    def __call__(self, lhs, rhs):
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
            "%": operator.mod,
        }

        if self._op in {"/", "%"} and rhs.decimal().is_zero():
            raise ZeroDivisionError()

        result = operators[self._op](lhs.decimal(), rhs.decimal())
        if result.to_integral_value() == result:
            result = result.to_integral_value()

        return Number(str(result))


XamlApplication.Start(App)
