import operator
from decimal import Decimal

from win32more.Microsoft.UI.Xaml.Controls import Button

from win32more.winui3 import XamlApplication, XamlLoader


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

        <Button x:Name="BPercent" Grid.Column="0" Grid.Row="1" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="%">
        </Button>
        <Button x:Name="BCE" Grid.Column="1" Grid.Row="1" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="CE">
        </Button>
        <Button x:Name="BC" Grid.Column="2" Grid.Row="1" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="C">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="Escape" /></Button.KeyboardAccelerators>
        </Button>
        <Button x:Name="BDevide" Grid.Column="3" Grid.Row="1" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="/">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="Divide" /></Button.KeyboardAccelerators>
        </Button>

        <Button x:Name="B7" Grid.Column="0" Grid.Row="2" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="7">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="NumberPad7" /></Button.KeyboardAccelerators>
        </Button>
        <Button x:Name="B8" Grid.Column="1" Grid.Row="2" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="8">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="NumberPad8" /></Button.KeyboardAccelerators>
        </Button>
        <Button x:Name="B9" Grid.Column="2" Grid.Row="2" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="9">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="NumberPad9" /></Button.KeyboardAccelerators>
        </Button>
        <Button x:Name="BMultiply" Grid.Column="3" Grid.Row="2" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="*">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="Multiply" /></Button.KeyboardAccelerators>
        </Button>

        <Button x:Name="B4" Grid.Column="0" Grid.Row="3" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="4">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="NumberPad4" /></Button.KeyboardAccelerators>
        </Button>
        <Button x:Name="B5" Grid.Column="1" Grid.Row="3" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="5">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="NumberPad5" /></Button.KeyboardAccelerators>
        </Button>
        <Button x:Name="B6" Grid.Column="2" Grid.Row="3" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="6">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="NumberPad6" /></Button.KeyboardAccelerators>
        </Button>
        <Button x:Name="BMinus" Grid.Column="3" Grid.Row="3" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="-">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="Subtract" /></Button.KeyboardAccelerators>
        </Button>

        <Button x:Name="B1" Grid.Column="0" Grid.Row="4" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="1">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="Numberpad1" /></Button.KeyboardAccelerators>
        </Button>
        <Button x:Name="B2" Grid.Column="1" Grid.Row="4" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="2">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="Numberpad2" /></Button.KeyboardAccelerators>
        </Button>
        <Button x:Name="B3" Grid.Column="2" Grid.Row="4" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="3">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="Numberpad3" /></Button.KeyboardAccelerators>
        </Button>
        <Button x:Name="BPlus" Grid.Column="3" Grid.Row="4" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="+">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="Add" /></Button.KeyboardAccelerators>
        </Button>

        <Button x:Name="BPM" Grid.Column="0" Grid.Row="5" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="+/-">
        </Button>
        <Button x:Name="B0" Grid.Column="1" Grid.Row="5" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="0">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="Numberpad0" /></Button.KeyboardAccelerators>
        </Button>
        <Button x:Name="BPeriod" Grid.Column="2" Grid.Row="5" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content=".">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="Decimal" /></Button.KeyboardAccelerators>
        </Button>
        <Button x:Name="BEqual" Grid.Column="3" Grid.Row="5" HorizontalAlignment="Stretch" VerticalAlignment="Stretch" Click="_on_button_click" Content="=">
            <Button.KeyboardAccelerators><KeyboardAccelerator Key="Enter" /></Button.KeyboardAccelerators>
        </Button>

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

    def display(self, txt):
        self._textblock.Text = txt


class Calc:
    def __init__(self, view):
        self._view = view
        self._state = LhsState(Number("0"))
        self._view.display(str(self._state))

    def input(self, cmd):
        self._state = self._state.input(cmd)
        self._view.display(str(self._state))


class LhsState:
    def __init__(self, lhs):
        self._lhs = lhs

    def input(self, cmd):
        if cmd in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "+/-"}:
            return LhsState(self._lhs.input(cmd))
        elif cmd in {"+", "-", "*", "/", "%"}:
            return OpState(self._lhs, Operator(cmd))
        elif cmd == "CE":
            return LhsState(Number("0"))
        elif cmd == "C":
            return LhsState(Number("0"))
        elif cmd == "=":
            return self
        raise RuntimeError("never happen")

    def __str__(self):
        return f"{self._lhs}"


class OpState:
    def __init__(self, lhs, op):
        self._lhs = lhs
        self._op = op

    def input(self, cmd):
        if cmd in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            return RhsState(self._lhs, self._op, Number(cmd))
        elif cmd == ".":
            return RhsState(self._lhs, self._op, Number("0."))
        elif cmd == "+/-":
            return RhsState(self._lhs, self._op, Number("-0"))
        elif cmd in {"+", "-", "*", "/", "%"}:
            return OpState(self._lhs, Operator(cmd))
        elif cmd == "CE":
            return self
        elif cmd == "C":
            return LhsState(Number("0"))
        elif cmd == "=":
            try:
                lhs = self._op(self._lhs, self._lhs)
            except ZeroDivisionError:
                return ErrorState("Cannot divide by zero")
            else:
                return ResultState(lhs, self._op, self._lhs)
        raise RuntimeError("never happen")

    def __str__(self):
        return f"{self._lhs} {self._op}"


class RhsState:
    def __init__(self, lhs, op, rhs):
        self._lhs = lhs
        self._op = op
        self._rhs = rhs

    def input(self, cmd):
        if cmd in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "+/-"}:
            return RhsState(self._lhs, self._op, self._rhs.input(cmd))
        elif cmd in {"+", "-", "*", "/", "%"}:
            try:
                lhs = self._op(self._lhs, self._rhs)
            except ZeroDivisionError:
                return ErrorState("Cannot divide by zero")
            else:
                return OpState(lhs, Operator(cmd))
        elif cmd == "CE":
            return RhsState(self._lhs, self._op, Number("0"))
        elif cmd == "C":
            return LhsState(Number("0"))
        elif cmd == "=":
            try:
                lhs = self._op(self._lhs, self._rhs)
            except ZeroDivisionError:
                return ErrorState("Cannot divide by zero")
            else:
                return ResultState(lhs, self._op, self._rhs)
        raise RuntimeError("never happen")

    def __str__(self):
        return f"{self._lhs} {self._op} {self._rhs}"


class ResultState:
    def __init__(self, lhs, op, rhs):
        self._lhs = lhs
        self._op = op
        self._rhs = rhs

    def input(self, cmd):
        if cmd in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            return LhsState(Number(cmd))
        elif cmd == ".":
            return LhsState(Number("0."))
        elif cmd == "+/-":
            return ResultState(self._lhs.input(cmd), self._op, self._rhs)
        elif cmd in {"+", "-", "*", "/", "%"}:
            return OpState(self._lhs, Operator(cmd))
        elif cmd == "CE":
            return LhsState(Number("0"))
        elif cmd == "C":
            return LhsState(Number("0"))
        elif cmd == "=":
            try:
                lhs = self._op(self._lhs, self._rhs)
            except ZeroDivisionError:
                return ErrorState("Cannot divide by zero")
            else:
                return ResultState(lhs, self._op, self._rhs)
        raise RuntimeError("never happen")

    def __str__(self):
        return f"{self._lhs}"


class ErrorState:
    def __init__(self, msg):
        self._msg = msg

    def input(self, cmd):
        if cmd in {"CE", "C"}:
            return LhsState(Number("0"))
        return self

    def __str__(self):
        return self._msg


class Number:
    def __init__(self, num):
        self._num = num

    def input(self, cmd):
        if cmd in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            if self._num == "0":
                return Number(cmd)
            elif self._num == "-0":
                return Number("-" + cmd)
            return Number(self._num + cmd)
        elif cmd == ".":
            if "." in self._num:
                return self
            return Number(self._num + ".")
        elif cmd == "+/-":
            if self._num.startswith("-"):
                return Number(self._num[1:])
            return Number("-" + self._num)
        raise RuntimeError("never happen")

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
