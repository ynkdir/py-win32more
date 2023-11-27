from ctypes import (
    POINTER,
    WINFUNCTYPE,
    Structure,
    WinError,
    addressof,
    c_void_p,
    cast,
    py_object,
    sizeof
)

from win32more import FAILED, Guid, UInt32
from win32more._winrt import WinRT_String, SZArray
from win32more.mddbootstrap import MddBootstrapInitialize2, MddBootstrapShutdown, MddBootstrapInitializeOptions_OnNoMatch_ShowUI
from win32more.Windows.Win32.Foundation import HRESULT, S_OK
from win32more.Windows.Win32.Storage.Packaging.Appx import PACKAGE_VERSION
from win32more.Windows.Win32.System.WinRT import HSTRING, IInspectable, TrustLevel
from win32more.Windows.Win32.UI.HiDpi import SetProcessDpiAwarenessContext, DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2
from win32more.Windows.UI.Xaml.Interop import TypeName
from win32more.Microsoft.UI.Xaml import Application, IApplicationOverrides, LaunchActivatedEventArgs
from win32more.Microsoft.UI.Xaml.Controls import XamlControlsResources
from win32more.Microsoft.UI.Xaml.Markup import IXamlType, XmlnsDefinition, IXamlMetadataProvider
from win32more.Microsoft.UI.Xaml.XamlTypeInfo import XamlControlsXamlMetaDataProvider

class XamlApplicationImpl(Structure):
    _fields_ = [("lpvtbl", POINTER(c_void_p)), ("lpvtbl2", POINTER(c_void_p)), ("comptr", py_object)]

    def __init__(self, comptr):
        self.lpvtbl = (c_void_p * 7)()
        self.lpvtbl[0] = cast(self.QueryInterface, c_void_p)
        self.lpvtbl[1] = cast(self.AddRef, c_void_p)
        self.lpvtbl[2] = cast(self.Release, c_void_p)
        self.lpvtbl[3] = cast(self.GetIids, c_void_p)
        self.lpvtbl[4] = cast(self.GetRuntimeClassName, c_void_p)
        self.lpvtbl[5] = cast(self.GetTrustLevel, c_void_p)
        self.lpvtbl[6] = cast(self.OnLaunched, c_void_p)
        self.lpvtbl2 = (c_void_p * 9)()
        self.lpvtbl2[0] = cast(self.QueryInterface2, c_void_p)
        self.lpvtbl2[1] = cast(self.AddRef2, c_void_p)
        self.lpvtbl2[2] = cast(self.Release2, c_void_p)
        self.lpvtbl2[3] = cast(self.GetIids2, c_void_p)
        self.lpvtbl2[4] = cast(self.GetRuntimeClassName2, c_void_p)
        self.lpvtbl2[5] = cast(self.GetTrustLevel2, c_void_p)
        self.lpvtbl2[6] = cast(self.GetXamlType, c_void_p)
        self.lpvtbl2[7] = cast(self.GetXamlTypeByFullName, c_void_p)
        self.lpvtbl2[8] = cast(self.GetXmlnsDefinitions, c_void_p)
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
        return self.comptr.GetRuntimeClassName(className)

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(TrustLevel))
    def GetTrustLevel(this, trustLevel):
        self = cast(this, POINTER(XamlApplicationImpl)).contents
        return self.comptr.GetTrustLevel(trustLevel)

    @WINFUNCTYPE(HRESULT, c_void_p, LaunchActivatedEventArgs)
    def OnLaunched(this, args):
        self = cast(this, POINTER(XamlApplicationImpl)).contents
        self.comptr._OnLaunched(args)
        return S_OK

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(Guid), POINTER(c_void_p))
    def QueryInterface2(this, riid, ppvObject):
        self = cast(this-sizeof(c_void_p), POINTER(XamlApplicationImpl)).contents
        return self.comptr.QueryInterface(riid, ppvObject)

    @WINFUNCTYPE(UInt32, c_void_p)
    def AddRef2(this):
        self = cast(this-sizeof(c_void_p), POINTER(XamlApplicationImpl)).contents
        return self.comptr.AddRef()

    @WINFUNCTYPE(UInt32, c_void_p)
    def Release2(this):
        self = cast(this-sizeof(c_void_p), POINTER(XamlApplicationImpl)).contents
        return self.comptr.Release()

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(UInt32), POINTER(POINTER(Guid)))
    def GetIids2(this, iidCount, iids):
        self = cast(this-sizeof(c_void_p), POINTER(XamlApplicationImpl)).contents
        return self.comptr.GetIids(iidCount, iids)

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(HSTRING))
    def GetRuntimeClassName2(this, className):
        self = cast(this-sizeof(c_void_p), POINTER(XamlApplicationImpl)).contents
        return self.comptr.GetRuntimeClassName(className)

    @WINFUNCTYPE(HRESULT, c_void_p, POINTER(TrustLevel))
    def GetTrustLevel2(this, trustLevel):
        self = cast(this-sizeof(c_void_p), POINTER(XamlApplicationImpl)).contents
        return self.comptr.GetTrustLevel(trustLevel)

    @WINFUNCTYPE(HRESULT, c_void_p, TypeName, POINTER(IXamlType))
    def GetXamlType(this, type, value):
        self = cast(this-sizeof(c_void_p), POINTER(XamlApplicationImpl)).contents
        return self.comptr.GetXamlType(type, value)

    @WINFUNCTYPE(HRESULT, c_void_p, WinRT_String, POINTER(IXamlType))
    def GetXamlTypeByFullName(this, fullName, value):
        self = cast(this-sizeof(c_void_p), POINTER(XamlApplicationImpl)).contents
        return self.comptr.GetXamlTypeByFullName(fullName, value)

    @WINFUNCTYPE(HRESULT, c_void_p, c_void_p)
    def GetXmlnsDefinitions(this, value):
        self = cast(this-sizeof(c_void_p), POINTER(XamlApplicationImpl)).contents
        return self.comptr.GetXmlnsDefinitions(value)


class XamlApplication(IApplicationOverrides):
    _keep_reference_in_python_world_ = {}

    def __init__(self):
        self._comobj = XamlApplicationImpl(self)
        self.value = addressof(self._comobj)
        self.value2 = addressof(self._comobj.lpvtbl2)
        self._refcount = 0
        self.AddRef()
        self._provider = XamlControlsXamlMetaDataProvider.CreateInstance()
        self._inner_interface = IInspectable()
        Application.CreateInstance(self, self._inner_interface)

    def QueryInterface(self, riid, ppvObject):
        if str(riid.contents) == str(IApplicationOverrides._iid_):
            ppvObject.contents.value = self.value
            self.AddRef()
            return S_OK
        elif str(riid.contents) == str(IXamlMetadataProvider._iid_):
            ppvObject.contents.value = self.value2
            self.AddRef()
            return S_OK
        else:
            return self._inner_interface.QueryInterface(riid, ppvObject)

    def AddRef(self):
        self._refcount += 1
        if self._refcount == 1:
            self._keep_reference_in_python_world_[id(self)] = self
        return self._refcount

    def Release(self):
        self._refcount -= 1
        if self._refcount == 0:
            self._comobj.comptr = None
            self._inner_interface.Release()
            del self._keep_reference_in_python_world_[id(self)]
        return self._refcount

    def GetIids(self, iidCount, iids):
        return self._inner_interface.GetIids(iidCount, iids)

    def GetRuntimeClassName(self, className):
        return self._inner_interface.GetRuntimeClassName(className)

    def GetTrustLevel(self, trustLevel):
        return self._inner_interface.GetTrustLevel(trustLevel)

    def _OnLaunched(self, args):
        Application.Current.Resources.MergedDictionaries.Append(XamlControlsResources.CreateInstance())
        self.OnLaunched(args)

    def OnLaunched(self, args):
        # You should override this in your devired class
        ...

    def GetXamlType(self, type, value):
        value.contents.value = self._provider.GetXamlType(type).value
        return S_OK

    def GetXamlTypeByFullName(self, fullName, value):
        value.contents.value =  self._provider.GetXamlTypeByFullName(fullName).value
        return S_OK

    def GetXmlnsDefinitions(self, value):
        value.contents.value = self._provider.GetXmlnsDefinitions().value
        return S_OK

    @classmethod
    def Start(cls, appcls):
        r = SetProcessDpiAwarenessContext(DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2)
        if FAILED(r):
            raise WinError(r)

        hr = MddBootstrapInitialize2(0x00010004, "", PACKAGE_VERSION(Version=0x0FA0041900750000), MddBootstrapInitializeOptions_OnNoMatch_ShowUI)
        if FAILED(hr):
            raise WinError(hr)

        app = None

        def init(params):
            nonlocal app
            app = appcls()

        Application.Start(init)

        app.Release()

        MddBootstrapShutdown()
