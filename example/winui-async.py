import asyncio

from win32more.asyncui import async_start_runner
from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Controls import Button
from win32more.Windows.Foundation import PropertyValue
from win32more.xaml import XamlApplication


class App(XamlApplication):
    def OnLaunched(self, args):
        win = Window()
        self.button = Button()
        self.button.Content = PropertyValue.CreateString("Count 10")
        self.button.add_Click(self.button_OnClick)
        win.Content = self.button
        win.Activate()

    async def button_OnClick(self, sender, e):
        for i in range(10):
            self.button.Content = PropertyValue.CreateString(f"Count {i + 1}")
            await asyncio.sleep(1.0)


def main():
    async_start_runner()
    XamlApplication.Start(App)


if __name__ == "__main__":
    main()
