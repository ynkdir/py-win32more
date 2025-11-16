import unittest
from multiprocessing import Pool

try:
    import win32more.Microsoft  # noqa
except:  # noqa
    appsdk_available = False
else:
    appsdk_available = True


def _test_create_window_main():
    from win32more.Microsoft.UI.Xaml import Window
    from win32more.winui3 import XamlApplication

    class App(XamlApplication):
        def OnLaunched(self, args):
            self._window = Window()
            self._window.Activated += self.Window_Activated
            self._window.Activate()

        def Window_Activated(self, sender, e):
            nonlocal activated
            activated = True
            self.Exit()

    activated = False

    XamlApplication.Start(App)

    return activated


def _test_create_window_xaml_loader_main():
    from win32more.winui3 import XamlApplication, XamlLoader

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
    xmlns:controls="using:Microsoft.UI.Xaml.Controls"
    mc:Ignorable="d">

    <StackPanel>
        <Button Content="Button1" />
    </StackPanel>
</Window>
""",
            )

            self._window.Activated += self.Window_Activated
            self._window.Activate()

        def Window_Activated(self, sender, e):
            nonlocal activated
            activated = True
            self.Exit()

    activated = False

    XamlApplication.Start(App)

    return activated


def _test_create_window_xaml_class_main():
    from win32more.Microsoft.UI.Xaml import Window
    from win32more.winui3 import XamlApplication, XamlClass

    class App(XamlApplication):
        def OnLaunched(self, args):
            self._window = MainWindow()
            self._window.Activated += self.Window_Activated
            self._window.Activate()

        def Window_Activated(self, sender, e):
            nonlocal activated
            activated = True
            self.Exit()

    class MainWindow(XamlClass, Window):
        def __init__(self):
            super().__init__()
            self.LoadComponentFromString("""
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    xmlns:controls="using:Microsoft.UI.Xaml.Controls"
    mc:Ignorable="d">

    <StackPanel>
        <Button Content="Button1" />
    </StackPanel>
</Window>
""")

    activated = False

    XamlApplication.Start(App)

    return activated


@unittest.skipUnless(appsdk_available, "WindowsAppSDK is not available")
class TestWinui3(unittest.TestCase):
    def _mp(self, target):
        with Pool() as pool:
            return pool.apply_async(target).get()

    def test_create_window(self):
        activated = self._mp(_test_create_window_main)
        self.assertTrue(activated)

    def test_create_window_xaml_loader(self):
        activated = self._mp(_test_create_window_xaml_loader_main)
        self.assertTrue(activated)

    def test_create_window_xaml_class(self):
        activated = self._mp(_test_create_window_xaml_class_main)
        self.assertTrue(activated)


if __name__ == "__main__":
    unittest.main()
