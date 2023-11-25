import logging
from ctypes import (
    POINTER,
    WINFUNCTYPE,
    Structure,
    WinError,
    addressof,
    c_void_p,
    cast,
    py_object,
)

from win32more import FAILED, Guid, UInt32
from win32more.mddbootstrap import MddBootstrapInitialize2, MddBootstrapShutdown
from win32more.Microsoft.UI.Xaml import (
    Application,
    HorizontalAlignment_Center,
    IApplicationOverrides,
    LaunchActivatedEventArgs,
    Window,
)
from win32more.Microsoft.UI.Xaml.Controls import Button, StackPanel
from win32more.Windows.Foundation import PropertyValue
from win32more.Windows.Win32.Foundation import HRESULT, S_OK
from win32more.Windows.Win32.Storage.Packaging.Appx import PACKAGE_VERSION
from win32more.Windows.Win32.System.WinRT import HSTRING, IInspectable, TrustLevel

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def box_str(s):
    return PropertyValue.CreateString(s)


class AppImpl(Structure):
    _fields_ = [("lpvtbl", POINTER(c_void_p)), ("comptr", py_object)]

    def __init__(self, comptr):
        self.lpvtbl = (c_void_p * 7)()
        self.lpvtbl[0] = cast(self.QueryInterface, c_void_p)
        self.lpvtbl[1] = cast(self.AddRef, c_void_p)
        self.lpvtbl[2] = cast(self.Release, c_void_p)
        self.lpvtbl[3] = cast(self.GetIids, c_void_p)
        self.lpvtbl[4] = cast(self.GetRuntimeClassName, c_void_p)
        self.lpvtbl[5] = cast(self.GetTrustLevel, c_void_p)
        self.lpvtbl[6] = cast(self.OnLaunched, c_void_p)
        self.comptr = py_object(comptr)

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(Guid), POINTER(c_void_p))
    def QueryInterface(this, riid, ppvObject):
        self = cast(this, POINTER(AppImpl)).contents
        return self.comptr.QueryInterface(riid, ppvObject)

    @WINFUNCTYPE(UInt32, c_void_p)
    def AddRef(this):
        self = cast(this, POINTER(AppImpl)).contents
        return self.comptr.AddRef()

    @WINFUNCTYPE(UInt32, c_void_p)
    def Release(this):
        self = cast(this, POINTER(AppImpl)).contents
        return self.comptr.Release()

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(UInt32), POINTER(POINTER(Guid)))
    def GetIids(this, iidCount, iids):
        self = cast(this, POINTER(AppImpl)).contents
        return self.comptr.GetIids(iidCount, iids)

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(HSTRING))
    def GetRuntimeClassName(this, className):
        self = cast(this, POINTER(AppImpl)).contents
        return self.comptr.GetRuntimeClassName(className)

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(TrustLevel))
    def GetTrustLevel(this, trustLevel):
        self = cast(this, POINTER(AppImpl)).contents
        return self.comptr.GetTrustLevel(trustLevel)

    @WINFUNCTYPE(HRESULT, c_void_p, LaunchActivatedEventArgs)
    def OnLaunched(this, args):
        self = cast(this, POINTER(AppImpl)).contents
        self.comptr.OnLaunched(args)
        return S_OK


class App(IApplicationOverrides):
    _keep_reference_in_python_world_ = {}

    def __init__(self):
        self._comobj = AppImpl(self)
        self.value = addressof(self._comobj)
        self._refcount = 0
        self.AddRef()
        self._inner_interface = IInspectable()
        Application.CreateInstance(self, self._inner_interface)

    def QueryInterface(self, riid, ppvObject):
        logger.debug(f"QueryInterface: {riid.contents}, {ppvObject}")
        if str(riid.contents) == str(IApplicationOverrides._iid_):
            ppvObject.contents.value = self.value
            self.AddRef()
            return S_OK
        else:
            return self._inner_interface.QueryInterface(riid, ppvObject)

    def AddRef(self):
        logger.debug(f"AddRef: {self._refcount}")
        self._refcount += 1
        if self._refcount == 1:
            self._keep_reference_in_python_world_[id(self)] = self
        return self._refcount

    def Release(self):
        logger.debug(f"Release: {self._refcount}")
        self._refcount -= 1
        if self._refcount == 0:
            self._comobj.comptr = None
            del self._keep_reference_in_python_world_[id(self)]
        return self._refcount

    def GetIids(self, iidCount, iids):
        logger.debug(f"GetIids: {iidCount} {iids}")
        return self._inner_interface.GetIids(iidCount, iids)

    def GetRuntimeClassName(self, className):
        logger.debug(f"GetRuntimeClassName: {className}")
        return self._inner_interface.GetRuntimeClassName(className)

    def GetTrustLevel(self, trustLevel):
        logger.debug(f"GetTrustLevel: {trustLevel}")
        return self._inner_interface.GetTrustLevel(trustLevel)

    def OnLaunched(self, args):
        logger.debug(f"OnLaunched: {args}")

        self.win = Window.CreateInstance(None, None)
        self.win.Title = "WinUI3 Xaml Test"

        self.panel = StackPanel.CreateInstance(None, None)
        self.win.Content = self.panel

        self.button = Button.CreateInstance(None, None)
        self.button.HorizontalAlignment = HorizontalAlignment_Center
        self.button.Content = box_str("Click me!")
        self.button_count = 0

        @self.button.add_Click
        def on_click(sender, e):
            self.button_count += 1
            self.button.Content = box_str(f"{'[' * self.button_count}Click me!{']' * self.button_count}")

        self.panel.Children.Append(self.button)

        self.win.Activate()


def main() -> None:
    hr = MddBootstrapInitialize2(0x00010004, "", PACKAGE_VERSION(Revision=0, Build=0, Minor=4, Major=1), 0)
    if FAILED(hr):
        raise WinError(hr)

    Application.Start(lambda params: App() and None)

    MddBootstrapShutdown()


if __name__ == "__main__":
    main()
