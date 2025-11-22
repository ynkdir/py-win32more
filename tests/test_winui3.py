import sys
import unittest
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import parent_process

try:
    import win32more.Microsoft  # noqa
except:  # noqa
    appsdk_available = False
else:
    appsdk_available = True


assertion_error = None


def process(testfunc):
    def wrapper(self):
        if parent_process() is not None:
            testfunc(self)
            if assertion_error is not None:
                raise assertion_error.with_traceback(assertion_error.__traceback__)
        else:
            with ProcessPoolExecutor() as executor:
                was_successful = executor.submit(run, testfunc.__qualname__).result()
            if not was_successful:
                self.fail("test in subprocess failed")

    return wrapper


def run(name):
    suite = unittest.TestLoader().loadTestsFromName(name, sys.modules[__name__])
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result.wasSuccessful()


def exitonerror(func):
    def wrapper(*args):
        global assertion_error
        try:
            return func(*args)
        except AssertionError as e:
            from win32more.Microsoft.UI.Xaml import Application

            assertion_error = e
            Application.Current.Exit()

    return wrapper


@unittest.skipUnless(appsdk_available, "WindowsAppSDK is not available")
class TestWinui3(unittest.TestCase):
    @process
    def test_create_window(testcase):
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

        testcase.assertTrue(activated)

    @process
    def test_create_window_xaml_loader(testcase):
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

        testcase.assertTrue(activated)

    @process
    def test_xaml_loader_connect_name(testcase):
        from win32more.winui3 import XamlApplication, XamlLoader

        class App(XamlApplication):
            @exitonerror
            def OnLaunched(self, args):
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
                testcase.assertEqual(self.Button1.Content.as_(str), "Button1")
                self.Exit()

        XamlApplication.Start(App)

    @process
    def test_create_window_xaml_class(testcase):
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

        testcase.assertTrue(activated)

    @process
    def test_xaml_class_connect_name(testcase):
        from win32more.Microsoft.UI.Xaml import Window
        from win32more.winui3 import XamlApplication, XamlClass

        class App(XamlApplication):
            @exitonerror
            def OnLaunched(self, args):
                self._window = MainWindow()
                testcase.assertEqual(self._window.Button1.Content.as_(str), "Button1")
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

        XamlApplication.Start(App)

    @process
    def test_ms_appx_absolute_path(testcase):
        from pathlib import Path

        from win32more.winui3 import _ms_appx_absolute_path

        approot = Path("C:\\myapp")
        xaml_root = Path("C:\\myapp\\src")

        testcase.assertEqual(
            "ms-appx:///C:/myapp/foo.txt", _ms_appx_absolute_path("ms-appx:///foo.txt", xaml_root, approot)
        )
        testcase.assertEqual(
            "ms-appx:///C:/foo.txt", _ms_appx_absolute_path("ms-appx:///C:/foo.txt", xaml_root, approot)
        )
        testcase.assertEqual("ms-appx:///C:/myapp/src/foo.txt", _ms_appx_absolute_path("foo.txt", xaml_root, approot))
        testcase.assertEqual("/foo.txt", _ms_appx_absolute_path("/foo.txt", xaml_root, approot))
        testcase.assertEqual("ms-appx:///C:/myapp/src/foo.txt", _ms_appx_absolute_path("./foo.txt", xaml_root, approot))
        testcase.assertEqual("C:/path/to/foo.txt", _ms_appx_absolute_path("C:/path/to/foo.txt", xaml_root, approot))
        testcase.assertEqual(
            "http://example.com/foo.txt", _ms_appx_absolute_path("http://example.com/foo.txt", xaml_root, approot)
        )


if __name__ == "__main__":
    unittest.main()
