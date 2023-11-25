from ctypes import Structure, POINTER, py_object, c_void_p, cast, WINFUNCTYPE, HRESULT, addressof, byref, WinError

from win32more import ComPtr, Guid, UInt32, FAILED
from win32more._winrt import WinRT_String
from win32more.mddbootstrap import MddBootstrapInitialize2, MddBootstrapShutdown, MddBootstrapInitializeOptions_OnNoMatch_ShowUI
from win32more.Windows.Win32.Foundation import S_OK, E_NOINTERFACE
from win32more.Windows.Win32.System.Com import IUnknown
from win32more.Windows.Win32.System.WinRT import IInspectable, HSTRING, TrustLevel, TrustLevel_BaseTrust
from win32more.Windows.Win32.Storage.Packaging.Appx import PACKAGE_VERSION
from win32more.Microsoft.UI.Xaml import IApplicationOverrides, ILaunchActivatedEventArgs, LaunchActivatedEventArgs, Application, Window


class XamlApplicationImpl(Structure):

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
        self = cast(this, POINTER(XamlApplicationImpl)).contents
        return self.comptr.QueryInterface(riid, ppvObject)

    @WINFUNCTYPE(UInt32, c_void_p)
    def AddRef(this):
        self = cast(this, POINTER(XamlApplicationImpl)).contents
        return self.comptr.AddRef()

    @WINFUNCTYPE(UInt32, c_void_p)
    def Release(this):
        self = cast(this, POINTER(XamlApplicationImpl)).contents
        return self.comptr.Release()

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(UInt32), POINTER(POINTER(Guid)))
    def GetIids(this, iidCount, iids):
        self = cast(this, POINTER(XamlApplicationImpl)).contents
        return self.comptr.GetIids(iidCount, iids)

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(HSTRING))
    def GetRuntimeClassName(this, className):
        self = cast(this, POINTER(XamlApplicationImpl)).contents
        return self.comptr.GetIids(className)

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(TrustLevel))
    def GetTrustLevel(this, trustLevel):
        self = cast(this, POINTER(XamlApplicationImpl)).contents
        return self.comptr.GetIids(trustLevel)

    @WINFUNCTYPE(HRESULT, c_void_p, c_void_p)
    def OnLaunched(this, args):
        self = cast(this, POINTER(XamlApplicationImpl)).contents
        # TODO: Convert ILaunchActivatedEventArgs into LaunchActivatedEventArgs
        return self.comptr.OnLaunched(args)


class XamlApplication(ComPtr):
    
    extends: IInspectable
    _keep_reference_in_python_world_ = {}

    def __init__(self):
        self._comobj = XamlApplicationImpl(self)
        self.value = addressof(self._comobj)
        self._refcount = 0
        self.AddRef()
        self.base = IInspectable()
        self.base.value = addressof(self._comobj)
        self.app = IInspectable()
        Application.CreateInstance(self.base, byref(self.app))

    def QueryInterface(self, riid, ppvObject):
        if str(riid.contents) == str(IUnknown._iid_):
            # ppvObject.contents.value can be access by ppvObject[0]
            ppvObject.contents.value = self.value
            self.AddRef()
            return S_OK
        elif str(riid.contents) == str(IInspectable._iid_):
            ppvObject.contents.value = self.value
            self.AddRef()
            return S_OK
        elif str(riid.contents) == str(IApplicationOverrides._iid_):
            ppvObject.contents.value = self.value
            self.AddRef()
            return S_OK
        else:
            return E_NOINTERFACE

    def AddRef(self):
        self._refcount += 1
        if self._refcount == 1:
            self._keep_reference_in_python_world_[id(self)] = self
        return self._refcount

    def Release(self):
        self._refcount -= 1
        if self._refcount == 0:
            self._comobj.comptr = None
            del self._keep_reference_in_python_world_[id(self)]
        return self._refcount

    def GetIids(self, iidCount, iids):
        iidCount.contents.value = 1
        iids.contents.value = (Guid * 1)(IApplicationOverrides._iid_)

    def GetRuntimeClassName(this, className):
        className.contents.value = WinRT_String("Microsoft.UI.Xaml.IApplicationOverrides")

    def GetTrustLevel(self, trustLevel):
        trustLevel.contesnts.value = TrustLevel_BaseTrust

    def OnLaunched(self, args: ILaunchActivatedEventArgs):
        # TODO: Convert ILaunchActivatedEventArgs into LaunchActivatedEventArgs in C implementation
        self.window = Window()
        self.window.Activate()
        print("test")


def init(params):
    XamlApplication()

hr = MddBootstrapInitialize2(0x00010004, "", PACKAGE_VERSION(Version=0x0FA0041900750000), MddBootstrapInitializeOptions_OnNoMatch_ShowUI)
if FAILED(hr):
    raise WinError(hr)
Application.Start(init)
MddBootstrapShutdown()