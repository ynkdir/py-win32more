from ctypes import addressof
from pathlib import Path

from win32more._winrt import Vtbl
from win32more.Microsoft.UI.Xaml import Application, Window
from win32more.Microsoft.UI.Xaml.Controls import Button
from win32more.Microsoft.UI.Xaml.Markup import IComponentConnector
from win32more.Windows.Foundation import Uri
from win32more.Windows.Win32.Foundation import S_OK
from win32more.Windows.Win32.System.Com import IUnknown
from win32more.Windows.Win32.System.WinRT import IInspectable
from win32more.xaml import XamlApplication


# Visual Studio generates connection code from xaml like this.
class MainWindow(Window):
    _keep_reference_in_python_world_ = {}

    # FIXME: implementing constructor using __new__() causes error in this case.
    def __new__(cls):
        self = super().__new__(cls, own=True)
        self._component_connector_vtbl = Vtbl(self, IComponentConnector)
        self.value = addressof(self._component_connector_vtbl)
        self._refcount = 0
        self.AddRef()
        self._inner = IInspectable()
        Window.CreateInstance(self, self._inner)
        self.InitializeComponent()
        return self

    def InitializeComponent(self):
        # ms-appx:///foo.xaml is relative to python.exe.
        # Use absolute path.
        # mx-appx:///C:/Full/Path/To/My.xaml
        # NOTE: According to documentation, LoadComponent() takes relative location.
        xaml_path = Path(__file__).with_name("winui-component-connector.xaml").absolute().as_posix()
        resource_locator = Uri(f"ms-appx:///{xaml_path}")
        Application.LoadComponent(self, resource_locator)

    def QueryInterface(self, riid, ppvObject):
        if riid[0] == IUnknown._iid_:
            ppvObject[0] = addressof(self._component_connector_vtbl)
            self.AddRef()
            return S_OK
        elif riid[0] == IInspectable._iid_:
            ppvObject[0] = addressof(self._component_connector_vtbl)
            self.AddRef()
            return S_OK
        elif riid[0] == IComponentConnector._iid_:
            ppvObject[0] = addressof(self._component_connector_vtbl)
            self.AddRef()
            return S_OK
        else:
            return self._inner.QueryInterface(riid, ppvObject)

    def AddRef(self):
        self._refcount += 1
        if self._refcount == 1:
            self._keep_reference_in_python_world_[id(self)] = self
        return self._refcount

    def Release(self):
        self._refcount -= 1
        if self._refcount == 0:
            self._inner.Release()
            del self._keep_reference_in_python_world_[id(self)]
        return self._refcount

    def GetIids(self, iidCount, iids):
        return self._inner.GetIids(iidCount, iids)

    def GetRuntimeClassName(self, className):
        return self._inner.GetRuntimeClassName(className)

    def GetTrustLevel(self, trustLevel):
        return self._inner.GetTrustLevel(trustLevel)

    def Connect(self, connectionId, target):
        if connectionId == 1:
            self.Button1 = target.as_(Button)
            self.Button1.add_Click(self.Button1_OnClick)
        elif connectionId == 2:
            self.Button2 = target.as_(Button)
            self.Button2.add_Click(self.Button2_OnClick)

    def GetBindingConnector(self, connectionId, target):
        return None

    def Button1_OnClick(self, sender, e):
        text = self.Button1.Content.as_(str)
        self.Button1.Content = f"[{text}]"

    def Button2_OnClick(self, sender, e):
        text = self.Button2.Content.as_(str)
        self.Button2.Content = f"({text})"


class App(XamlApplication):
    def OnLaunched(self, args):
        self._window = MainWindow()
        self._window.Activate()


XamlApplication.Start(App)
