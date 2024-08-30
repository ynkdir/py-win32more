import importlib
import xml.etree.ElementTree as ET

from win32more import FAILED, WinError
from win32more._winrt import ComClass, WinRT_String, event_setter
from win32more.asyncui import async_start_runner
from win32more.mddbootstrap import (
    WINDOWSAPPSDK_RELEASE_MAJORMINOR,
    WINDOWSAPPSDK_RELEASE_VERSION_SHORTTAG_W,
    WINDOWSAPPSDK_RUNTIME_VERSION_UINT64,
    MddBootstrapInitialize2,
    MddBootstrapInitializeOptions_OnNoMatch_ShowUI,
    MddBootstrapShutdown,
)
from win32more.Microsoft.UI.Xaml import Application, FrameworkElement, IApplicationOverrides, Window
from win32more.Microsoft.UI.Xaml.Controls import XamlControlsResources
from win32more.Microsoft.UI.Xaml.Markup import IXamlMetadataProvider, XamlReader
from win32more.Microsoft.UI.Xaml.XamlTypeInfo import XamlControlsXamlMetaDataProvider
from win32more.Windows.Win32.Storage.Packaging.Appx import PACKAGE_VERSION
from win32more.Windows.Win32.System.Com import COINIT_APARTMENTTHREADED, CoInitializeEx, CoUninitialize
from win32more.Windows.Win32.UI.HiDpi import DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2, SetProcessDpiAwarenessContext


class XamlApplication(ComClass, Application, IApplicationOverrides, IXamlMetadataProvider):
    def __init__(self):
        XamlApplication.__current = self
        self._OnLaunched_wrapped = self.OnLaunched
        self.OnLaunched = self._OnLaunched_wrapper
        super().__init__(own=True)
        self._provider = XamlControlsXamlMetaDataProvider()

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

    __current = None

    @classmethod
    def Start(cls, init):
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

        async_start_runner()

        Application.Start(lambda params: init())

        # FIXME: force Release() to avoid exit with error code.
        if XamlApplication.__current is not None:
            XamlApplication.__current.Release()

        MddBootstrapShutdown()

        CoUninitialize()

    def LoadXamlAndSetEventHandler(self, xaml):
        uiroot = XamlReader.Load(xaml)
        XamlEventWiring().execute(self, uiroot, xaml)
        return uiroot


class XamlEventWiring:
    def execute(self, app, uiroot, xaml):
        uiroot = self.cast_to_runtime_class(uiroot)

        if isinstance(uiroot, Window):
            window = uiroot
            framework_element = uiroot.Content.as_(FrameworkElement)
        else:
            window = None
            framework_element = uiroot.as_(FrameworkElement)

        xmlroot = ET.fromstring(xaml)
        for xmlelement in xmlroot.iter():
            if xmlelement.tag == "{http://schemas.microsoft.com/winfx/2006/xaml/presentation}Window":
                if window is not None:
                    self.wire_event(app, window, xmlelement)
            else:
                try:
                    name = xmlelement.attrib["{http://schemas.microsoft.com/winfx/2006/xaml}Name"]
                except KeyError:
                    continue
                uielement = self.cast_to_runtime_class(framework_element.FindName(name))
                self.wire_event(app, uielement, xmlelement)

    def wire_event(self, app, uielement, xmlelement):
        for k, v in xmlelement.items():
            if isinstance(getattr(uielement, k, None), event_setter):
                setter = getattr(uielement, k)
                setter += getattr(app, v)

    def cast_to_runtime_class(self, uielement):
        return uielement.as_(self.get_runtime_class(uielement))

    def get_runtime_class(self, uielement):
        namespace, name = self.get_runtime_class_name(uielement).rsplit(".", 1)
        module = importlib.import_module(f"win32more.{namespace}")
        return getattr(module, name)

    def get_runtime_class_name(self, uielement):
        s = WinRT_String(own=True)
        hr = uielement.GetRuntimeClassName(s)
        if FAILED(hr):
            raise WinError(hr)
        return s.strvalue
