import unittest
from concurrent.futures import ProcessPoolExecutor

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
            # NOTE: activated may be called twice.
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
    Activated="Window_Activated">

    <StackPanel>
        <Button Content="Button1" />
    </StackPanel>
</Window>
""",
            )
            self._window.Activate()

        def Window_Activated(self, sender, e):
            nonlocal activated
            activated = True
            self.Exit()

    activated = False

    XamlApplication.Start(App)

    return activated


def _test_xaml_loader_connect_name_main():
    from win32more.winui3 import XamlApplication, XamlLoader

    class App(XamlApplication):
        def OnLaunched(self, args):
            nonlocal button_content

            self._window = XamlLoader.Load(
                self,
                """
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">

    <StackPanel>
        <Button x:Name="Button1" Content="Button1" />
    </StackPanel>
</Window>
""",
            )
            button_content = self.Button1.Content.as_(str)
            self.Exit()

    button_content = None

    XamlApplication.Start(App)

    return button_content


def _test_create_window_xaml_class_main():
    from win32more.Microsoft.UI.Xaml import Window
    from win32more.winui3 import XamlApplication, XamlClass

    class App(XamlApplication):
        def OnLaunched(self, args):
            self._window = MainWindow()
            self._window.Activate()

    class MainWindow(XamlClass, Window):
        def __init__(self):
            super().__init__()
            self.LoadComponentFromString("""
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    Activated="_Activated">

    <StackPanel>
        <Button Content="Button1" />
    </StackPanel>
</Window>
""")

        def _Activated(self, sender, e):
            nonlocal activated
            activated = True
            self.Close()

    activated = False

    XamlApplication.Start(App)

    return activated


def _test_xaml_class_connect_name_main():
    from win32more.Microsoft.UI.Xaml import Window
    from win32more.winui3 import XamlApplication, XamlClass

    class App(XamlApplication):
        def OnLaunched(self, args):
            nonlocal button_content

            self._window = MainWindow()
            button_content = self._window.Button1.Content.as_(str)
            self.Exit()

    class MainWindow(XamlClass, Window):
        def __init__(self):
            super().__init__()
            self.LoadComponentFromString("""
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">

    <StackPanel>
        <Button x:Name="Button1" Content="Button1" />
    </StackPanel>
</Window>
""")

    button_content = None

    XamlApplication.Start(App)

    return button_content


def _test_ms_appx_absolute_path():
    from pathlib import Path

    from win32more.winui3 import _ms_appx_absolute_path

    approot = Path("C:\\myapp")
    xaml_root = Path("C:\\myapp\\src")

    return [
        ("ms-appx:///C:/myapp/foo.txt", _ms_appx_absolute_path("ms-appx:///foo.txt", xaml_root, approot)),
        ("ms-appx:///C:/foo.txt", _ms_appx_absolute_path("ms-appx:///C:/foo.txt", xaml_root, approot)),
        ("ms-appx:///C:/myapp/src/foo.txt", _ms_appx_absolute_path("foo.txt", xaml_root, approot)),
        ("/foo.txt", _ms_appx_absolute_path("/foo.txt", xaml_root, approot)),
        ("ms-appx:///C:/myapp/src/foo.txt", _ms_appx_absolute_path("./foo.txt", xaml_root, approot)),
        ("C:/path/to/foo.txt", _ms_appx_absolute_path("C:/path/to/foo.txt", xaml_root, approot)),
        ("http://example.com/foo.txt", _ms_appx_absolute_path("http://example.com/foo.txt", xaml_root, approot)),
    ]


@unittest.skipUnless(appsdk_available, "WindowsAppSDK is not available")
class TestWinui3(unittest.TestCase):
    def _mp(self, target):
        with ProcessPoolExecutor(max_workers=1) as executor:
            return executor.submit(target).result()

    def test_create_window(self):
        activated = self._mp(_test_create_window_main)
        self.assertTrue(activated)

    def test_create_window_xaml_loader(self):
        activated = self._mp(_test_create_window_xaml_loader_main)
        self.assertTrue(activated)

    def test_xaml_loader_connect_name(self):
        button_content = self._mp(_test_xaml_loader_connect_name_main)
        self.assertEqual(button_content, "Button1")

    def test_create_window_xaml_class(self):
        activated = self._mp(_test_create_window_xaml_class_main)
        self.assertTrue(activated)

    def test_xaml_class_connect_name(self):
        button_content = self._mp(_test_xaml_class_connect_name_main)
        self.assertEqual(button_content, "Button1")

    def test_ms_appx_absolute_path(self):
        results = self._mp(_test_ms_appx_absolute_path)
        for expected, result in results:
            self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
