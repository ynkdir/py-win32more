from ctypes import WinError, addressof

from win32more import FAILED
from win32more._winrt import Vtbl
from win32more.mddbootstrap import (
    WINDOWSAPPSDK_RELEASE_MAJORMINOR,
    WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W,
    WINDOWSAPPSDK_RUNTIME_VERSION_UINT64,
    MddBootstrapInitialize2,
    MddBootstrapInitializeOptions_OnNoMatch_ShowUI,
    MddBootstrapShutdown,
)
from win32more.Microsoft.UI.Xaml import Application, IApplicationOverrides
from win32more.Microsoft.UI.Xaml.Controls import XamlControlsResources
from win32more.Microsoft.UI.Xaml.Markup import IXamlMetadataProvider
from win32more.Microsoft.UI.Xaml.XamlTypeInfo import XamlControlsXamlMetaDataProvider
from win32more.Windows.Win32.Foundation import S_OK
from win32more.Windows.Win32.Storage.Packaging.Appx import PACKAGE_VERSION
from win32more.Windows.Win32.System.Com import COINIT_APARTMENTTHREADED, CoInitializeEx, CoUninitialize, IUnknown
from win32more.Windows.Win32.System.WinRT import IInspectable
from win32more.Windows.Win32.UI.HiDpi import DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2, SetProcessDpiAwarenessContext


class XamlApplication(Application):
    _keep_reference_in_python_world_ = {}

    def __init__(self):
        super().__init__(own=True)
        self._OnLaunched_wrapped = self.OnLaunched
        self.OnLaunched = self._OnLaunched_wrapper
        self._application_overrides_vtbl = Vtbl(self, IApplicationOverrides)
        self._xaml_metadata_provider_vtbl = Vtbl(self, IXamlMetadataProvider)
        self.value = addressof(self._application_overrides_vtbl)
        self._refcount = 0
        self.AddRef()
        self._provider = XamlControlsXamlMetaDataProvider()
        self._inner_interface = IInspectable()
        Application.CreateInstance(self, self._inner_interface)

    def QueryInterface(self, riid, ppvObject):
        if riid[0] == IUnknown._iid_:
            ppvObject[0] = addressof(self._application_overrides_vtbl)
            self.AddRef()
            return S_OK
        elif riid[0] == IInspectable._iid_:
            ppvObject[0] = addressof(self._application_overrides_vtbl)
            self.AddRef()
            return S_OK
        elif riid[0] == IApplicationOverrides._iid_:
            ppvObject[0] = addressof(self._application_overrides_vtbl)
            self.AddRef()
            return S_OK
        elif riid[0] == IXamlMetadataProvider._iid_:
            ppvObject[0] = addressof(self._xaml_metadata_provider_vtbl)
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
            self._inner_interface.Release()
            del self._keep_reference_in_python_world_[id(self)]
        return self._refcount

    def GetIids(self, iidCount, iids):
        return self._inner_interface.GetIids(iidCount, iids)

    def GetRuntimeClassName(self, className):
        return self._inner_interface.GetRuntimeClassName(className)

    def GetTrustLevel(self, trustLevel):
        return self._inner_interface.GetTrustLevel(trustLevel)

    def _OnLaunched_wrapper(self, args):
        self.Resources.MergedDictionaries.Append(XamlControlsResources())
        self._OnLaunched_wrapped(args)

    def OnLaunched(self, args):
        # You should override this in your devired class
        ...

    def GetXamlType(self, type):
        return self._provider.GetXamlType(type)

    def GetXamlTypeByFullName(self, fullName):
        return self._provider.GetXamlTypeByFullName(fullName)

    def GetXmlnsDefinitions(self):
        return self._provider.GetXmlnsDefinitions()

    @classmethod
    def Start(cls, appcls):
        r = SetProcessDpiAwarenessContext(DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2)
        if FAILED(r):
            raise WinError(r)

        hr = CoInitializeEx(None, COINIT_APARTMENTTHREADED)
        if FAILED(hr):
            raise WinError(hr)

        hr = MddBootstrapInitialize2(
            WINDOWSAPPSDK_RELEASE_MAJORMINOR,
            WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W,
            PACKAGE_VERSION(Version=WINDOWSAPPSDK_RUNTIME_VERSION_UINT64),
            MddBootstrapInitializeOptions_OnNoMatch_ShowUI,
        )
        if FAILED(hr):
            raise WinError(hr)

        app = None

        def init(params):
            nonlocal app
            app = appcls()

        Application.Start(init)

        app.Release()

        MddBootstrapShutdown()

        CoUninitialize()
