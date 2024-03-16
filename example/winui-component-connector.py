from ctypes import POINTER, WINFUNCTYPE, Structure, addressof, c_void_p, cast, py_object
from pathlib import Path

from win32more import Guid, Int32, UInt32
from win32more.Microsoft.UI.Xaml import Application, Window
from win32more.Microsoft.UI.Xaml.Controls import Button
from win32more.Microsoft.UI.Xaml.Markup import IComponentConnector
from win32more.Windows.Foundation import IPropertyValue, PropertyValue, Uri
from win32more.Windows.Win32.Foundation import HRESULT, S_OK
from win32more.Windows.Win32.System.Com import IUnknown
from win32more.Windows.Win32.System.WinRT import HSTRING, IInspectable, TrustLevel
from win32more.xaml import XamlApplication


class IComponentConnectorImpl(Structure):
    _fields_ = [("lpvtbl", POINTER(c_void_p)), ("comptr", py_object)]

    def __init__(self, comptr):
        self.lpvtbl = (c_void_p * 8)()
        self.lpvtbl[0] = cast(self.QueryInterface, c_void_p)
        self.lpvtbl[1] = cast(self.AddRef, c_void_p)
        self.lpvtbl[2] = cast(self.Release, c_void_p)
        self.lpvtbl[3] = cast(self.GetIids, c_void_p)
        self.lpvtbl[4] = cast(self.GetRuntimeClassName, c_void_p)
        self.lpvtbl[5] = cast(self.GetTrustLevel, c_void_p)
        self.lpvtbl[6] = cast(self.Connect, c_void_p)
        self.lpvtbl[7] = cast(self.GetBindingConnector, c_void_p)
        self.comptr = py_object(comptr)

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(Guid), POINTER(c_void_p))
    def QueryInterface(this, riid, ppvObject):
        self = cast(this, POINTER(IComponentConnectorImpl)).contents
        return self.comptr.QueryInterface(riid, ppvObject)

    @WINFUNCTYPE(UInt32, c_void_p)
    def AddRef(this):
        self = cast(this, POINTER(IComponentConnectorImpl)).contents
        return self.comptr.AddRef()

    @WINFUNCTYPE(UInt32, c_void_p)
    def Release(this):
        self = cast(this, POINTER(IComponentConnectorImpl)).contents
        return self.comptr.Release()

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(UInt32), POINTER(POINTER(Guid)))
    def GetIids(this, iidCount, iids):
        self = cast(this, POINTER(IComponentConnectorImpl)).contents
        return self.comptr.GetIids(iidCount, iids)

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(HSTRING))
    def GetRuntimeClassName(this, className):
        self = cast(this, POINTER(IComponentConnectorImpl)).contents
        return self.comptr.GetRuntimeClassName(className)

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(TrustLevel))
    def GetTrustLevel(this, trustLevel):
        self = cast(this, POINTER(IComponentConnectorImpl)).contents
        return self.comptr.GetTrustLevel(trustLevel)

    @WINFUNCTYPE(HRESULT, c_void_p, Int32, IInspectable)
    def Connect(this, connectionId, target):
        self = cast(this, POINTER(IComponentConnectorImpl)).contents
        return self.comptr.Connect(connectionId, target)

    @WINFUNCTYPE(HRESULT, c_void_p, Int32, IInspectable, POINTER(IComponentConnector))
    def GetBindingConnector(this, connectionId, target, result):
        self = cast(this, POINTER(IComponentConnectorImpl)).contents
        return self.comptr.Connect(connectionId, target, result)


class ComponentConnector(IComponentConnector):
    _keep_reference_in_python_world_ = {}

    # FIXME: implementing constructor using __new__() causes error in this case.
    def __new__(cls, delegate, **kwargs):
        return super().__new__(cls, **kwargs)

    def __init__(self, delegate):
        self._delegate = delegate
        self._comobj = IComponentConnectorImpl(self)
        self.value = addressof(self._comobj)
        self._refcount = 0
        self.AddRef()

    def QueryInterface(self, riid, ppvObject):
        if riid.contents == IUnknown._iid_:
            ppvObject.contents.value = self.value
            self.AddRef()
            return S_OK
        elif riid.contents == IInspectable._iid_:
            ppvObject.contents.value = self.value
            self.AddRef()
            return S_OK
        elif riid.contents == IComponentConnector._iid_:
            ppvObject.contents.value = self.value
            self.AddRef()
            return S_OK
        else:
            return self._delegate._inner.QueryInterface(riid, ppvObject)

    def AddRef(self):
        self._refcount += 1
        if self._refcount == 1:
            self._keep_reference_in_python_world_[id(self)] = self
        return self._refcount

    def Release(self):
        self._refcount -= 1
        if self._refcount == 0:
            self._comobj.comptr = None
            self._delegate._inner.Release()
            del self._keep_reference_in_python_world_[id(self)]
        return self._refcount

    def GetIids(self, iidCount, iids):
        return self._delegate._inner.GetIids(iidCount, iids)

    def GetRuntimeClassName(self, className):
        return self._delegate._inner.GetRuntimeClassName(className)

    def GetTrustLevel(self, trustLevel):
        return self._delegate._inner.GetTrustLevel(trustLevel)

    def Connect(self, connectionId, target):
        return self._delegate.Connect(connectionId, target)

    def GetBindingConnector(self, connectionId, target, result):
        return self._delegate.GetBindingConnector(connectionId, target, result)


# Visual Studio generates connection code from xaml like this.
class MainWindow(Window, IComponentConnector):
    def __new__(cls):
        self = super().__new__(cls, own=True)
        self._component_connector = ComponentConnector(self)
        self.value = self._component_connector.value
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

    def Connect(self, connectionId, target):
        if connectionId == 1:
            self.Button1 = target.as_(Button)
            self.Button1.add_Click(self.Button1_OnClick)
        elif connectionId == 2:
            self.Button2 = target.as_(Button)
            self.Button2.add_Click(self.Button2_OnClick)
        return S_OK

    def GetBindingConnector(self, connectionId, target, result):
        return S_OK

    def Button1_OnClick(self, sender, e):
        text = self.Button1.Content.as_(IPropertyValue).GetString()
        self.Button1.Content = PropertyValue.CreateString(f"[{text}]")

    def Button2_OnClick(self, sender, e):
        text = self.Button2.Content.as_(IPropertyValue).GetString()
        self.Button2.Content = PropertyValue.CreateString(f"({text})")


class App(XamlApplication):
    def OnLaunched(self, args):
        self._window = MainWindow()
        self._window.Activate()


XamlApplication.Start(App)
