import importlib
import weakref
import xml.etree.ElementTree as ET

from win32more import FAILED, WinError, asyncui
from win32more._winrt import ComClass, WinRT_String, event_setter
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
from win32more.Microsoft.UI.Xaml.Markup import IXamlMetadataProvider, IXamlType, XamlReader
from win32more.Microsoft.UI.Xaml.XamlTypeInfo import XamlControlsXamlMetaDataProvider
from win32more.Windows.UI.Xaml.Interop import TypeName
from win32more.Windows.Win32.Storage.Packaging.Appx import PACKAGE_VERSION
from win32more.Windows.Win32.System.Com import COINIT_APARTMENTTHREADED, CoInitializeEx, CoUninitialize
from win32more.Windows.Win32.UI.HiDpi import DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2, SetProcessDpiAwarenessContext
from win32more.Windows.Win32.UI.WindowsAndMessaging import SetTimer


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
        # You should override this in your derived class
        ...

    def GetXamlType(self, type):
        xaml_type = self.GetXamlTypeByFullName(type.Name.strvalue)
        if xaml_type:
            return xaml_type
        return self._provider.GetXamlType(type)

    # TODO: Is it needed to provide information for primitive or winui type?
    def GetXamlTypeByFullName(self, fullName):
        return self._provider.GetXamlTypeByFullName(fullName)

    def GetXmlnsDefinitions(self):
        return self._provider.GetXmlnsDefinitions()

    __current = None

    @classmethod
    def Start(cls, init):
        r = SetProcessDpiAwarenessContext(DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2)
        if not r:
            raise WinError()

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

        with asyncui.HandCrankRunner() as runner:
            SetTimer(0, 0, 100, lambda *_: runner.update())
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


class XamlType(ComClass, IXamlType):
    def __init__(
        self,
        full_name,
        type_kind,
        *,
        base_type=None,
        boxed_type=None,
        content_property=None,
        is_array=False,
        is_bindable=False,
        is_collection=False,
        is_dictionary=False,
        is_markup_extension=False,
        item_type=None,
        key_type=None,
        activate_instance=None,
        add_to_map=None,
        add_to_vector=None,
        create_from_string=None,
    ):
        super().__init__(own=True)
        self._full_name = full_name
        self._type_kind = type_kind
        self._base_type = base_type
        self._boxed_type = boxed_type
        self._content_property = content_property
        self._is_array = is_array
        self._is_bindable = is_bindable
        self._is_collection = is_collection
        self._is_constructible = bool(activate_instance)
        self._is_dictionary = is_dictionary
        self._is_markup_extension = is_markup_extension
        self._item_type = item_type
        self._key_type = key_type
        self._activate_instance = activate_instance
        self._add_to_map = add_to_map
        self._add_to_vector = add_to_vector
        self._create_from_string = create_from_string

    def get_BaseType(self):
        return self._base_type

    def get_BoxedType(self):
        return self._boxed_type

    def get_ContentProperty(self):
        return self._content_property

    def get_FullName(self):
        return self._full_name

    def get_IsArray(self):
        return self._is_array

    def get_IsBindable(self):
        return self._is_bindable

    def get_IsCollection(self):
        return self._is_collection

    def get_IsConstructible(self):
        return self._is_constructible

    def get_IsDictionary(self):
        return self._is_dictionary

    def get_IsMarkupExtension(self):
        return self._is_markup_extension

    def get_ItemType(self):
        return self._item_type

    def get_KeyType(self):
        return self._key_type

    def get_UnderlyingType(self):
        return TypeName(WinRT_String(self._full_name), self._type_kind)

    def ActivateInstance(self):
        if self._activate_instance is None:
            raise NotImplementedError()
        return self._activate_instance()

    def AddToMap(self, instance, key, value):
        if self._add_to_map is None:
            raise NotImplementedError()
        self._add_to_map(instance, key, value)

    def AddToVector(self, instance, value):
        if self._add_to_vector is None:
            raise NotImplementedError()
        self._add_to_vector(instance, value)

    def CreateFromString(self, value):
        if self._boxed_type is not None:
            return self._boxed_type.CreateFromString(value)
        if self._create_from_string is not None:
            return self._create_from_string(value)
        # TODO:
        # return fromStringConverter()
        raise NotImplementedError()

    def GetMember(self, name):
        # TODO:
        raise NotImplementedError()

    def RunInitializer(self):
        pass


def xaml_typename(name, kind):
    hs = WinRT_String(name)
    tn = TypeName(hs, kind)
    weakref.finalize(tn, hs.clear)
    return tn
