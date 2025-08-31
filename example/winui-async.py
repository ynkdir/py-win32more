import asyncio

from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Controls import Button
from win32more.appsdk.xaml import XamlApplication


class App(XamlApplication):
    def OnLaunched(self, args):
        win = Window()
        self.button = Button()
        self.button.Content = "Count 10"
        self.button.add_Click(self.button_OnClick)
        win.Content = self.button
        win.Activate()

    async def button_OnClick(self, sender, e):
        for i in range(10):
            self.button.Content = f"Count {i + 1}"
            await asyncio.sleep(1.0)


def main():
    XamlApplication.Start(App)


if __name__ == "__main__":
    main()
