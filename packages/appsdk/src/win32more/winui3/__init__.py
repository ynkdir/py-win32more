from __future__ import annotations

import importlib
import inspect
import weakref
import xml.etree.ElementTree as ET
from functools import partial
from pathlib import Path
from tempfile import NamedTemporaryFile

from win32more import FAILED, Char, ComClass, WinError, asyncui
from win32more._winrt import ISelf, hstr
from win32more.Microsoft.UI.Xaml import Application, FrameworkElement, IApplicationOverrides
from win32more.Microsoft.UI.Xaml.Markup import IComponentConnector, IXamlMetadataProvider, IXamlType, XamlReader
from win32more.Microsoft.UI.Xaml.XamlTypeInfo import XamlControlsXamlMetaDataProvider
from win32more.Microsoft.Windows.ApplicationModel.Resources import (
    ResourceCandidate,
    ResourceCandidateKind,
    ResourceManager,
)
from win32more.Windows.Foundation import Uri
from win32more.Windows.UI.Xaml.Interop import TypeName
from win32more.Windows.Win32.System.Com import COINIT_APARTMENTTHREADED, CoInitializeEx, CoUninitialize
from win32more.Windows.Win32.System.LibraryLoader import GetModuleFileName
from win32more.Windows.Win32.UI.HiDpi import DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2, SetProcessDpiAwarenessContext
from win32more.Windows.Win32.UI.WindowsAndMessaging import SetTimer

XMLNS_XAML = "http://schemas.microsoft.com/winfx/2006/xaml"
XMLNS_XAML_PRESENTATION = "http://schemas.microsoft.com/winfx/2006/xaml/presentation"

# FIXME: register_namespace() is global.
# This is required to prevent "ns0:" prefix for default namespace.
ET.register_namespace("", XMLNS_XAML_PRESENTATION)


class XamlApplication(ComClass, Application, IApplicationOverrides, IXamlMetadataProvider):
    def __init__(self):
        XamlApplication.__current = self
        self._provider = None
        super().__init__(own=True)
        self.InitializeComponent()
        self.ResourceManagerRequested += self.OnResourceManagerRequested

    def InitializeComponent(self):
        xaml_path = Path(__file__).with_name("app.xaml").as_posix()
        resource_locator = Uri(f"ms-appx:///{xaml_path}")
        Application.LoadComponent(self, resource_locator)

    def OnLaunched(self, args):
        # You should override this in your derived class
        ...

    def GetXamlType(self, type):
        return self.AppProvider().GetXamlType(type)

    # TODO: Is it needed to provide information for primitive or winui type?
    def GetXamlTypeByFullName(self, fullName):
        return self.AppProvider().GetXamlTypeByFullName(fullName)

    def GetXmlnsDefinitions(self):
        return self.AppProvider().GetXmlnsDefinitions()

    def AppProvider(self):
        if self._provider is None:
            self._provider = XamlControlsXamlMetaDataProvider()
        return self._provider

    # FIXME: When executing app execution alias, sys.executable points alias.
    #   sys.executable => $LOCALAPPDATA\Microsoft\WindowsApps\python.exe
    # We need resolved path instead.
    def AppExecutable(self) -> Path:
        buf = (Char * 1024)()
        r = GetModuleFileName(None, buf, 1024)
        if r == 0:
            raise WinError()
        return Path(buf.value)

    # Application root path.  This is used to convert "ms-appx:///" path.  See OnResourceNotFound().
    # This does not affect to WindowsAppSDK and may not work in specific situation.
    # Appsdk's default is directory of python.exe file.
    def AppRoot(self) -> Path:
        # return self.AppExecutable().parent
        return Path(inspect.getfile(type(self))).parent

    def OnResourceManagerRequested(self, sender, e):
        # Workaround to avoid FileNotFoundError with default constructor (file does not need to exist).
        # https://github.com/microsoft/WindowsAppSDK/issues/5814
        manager = ResourceManager("resources.pri")
        manager.ResourceNotFound += self.OnResourceNotFound
        e.CustomResourceManager = manager

    def OnResourceNotFound(self, sender, e):
        name = e.Name
        if name.startswith("Files/file:///"):
            # ignore absolute path
            pass
        elif e.Name.startswith("Files/"):
            # convert relative path from ms-appx:///path/to/file to AppRoot()/path/to/file
            name = name.removeprefix("Files/")
            filepath = self.__tmp_resource_file.pop(name, self.AppRoot() / name)
            if filepath.exists():
                resource_candidate = ResourceCandidate(ResourceCandidateKind.FilePath, str(filepath))
                e.SetResolvedCandidate(resource_candidate)

    __tmp_resource_file = {}

    __current = None

    @classmethod
    def Start(cls, init):
        r = SetProcessDpiAwarenessContext(DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2)
        if not r:
            raise WinError()

        hr = CoInitializeEx(None, COINIT_APARTMENTTHREADED)
        if FAILED(hr):
            raise WinError(hr)

        with asyncui.HandCrankRunner() as runner:
            SetTimer(0, 0, 100, lambda *_: runner.update())
            Application.Start(lambda params: init())

        # FIXME: force Release() to avoid exit with error code.
        if XamlApplication.__current is not None:
            XamlApplication.__current.Release()

        CoUninitialize()


class XamlClass(ComClass, IComponentConnector):
    def __init__(self, *args, own=True, **kwargs):
        super().__init__(*args, own=own, **kwargs)
        self.__component_connector = None

    def Connect(self, connectionId, target):
        self.__component_connector.Connect(connectionId, target)

    def GetBindingConnector(self, connectionId, target):
        return self.__component_connector.GetBindingConnector(connectionId, target)

    def LoadComponentFromFile(self, xaml_path: str | Path, encoding: str | None = None) -> None:
        self.LoadComponentFromString(Path(xaml_path).read_text(encoding=encoding), xaml_path)

    def LoadComponentFromString(self, xaml_str: str, xaml_path: str | Path | None = None) -> None:
        self.__component_connector = XamlComponentConnector()
        self.__component_connector.Load(self, xaml_str, xaml_path)


class XamlComponentConnector:
    def __init__(self):
        self._connectors = {}

    def Connect(self, connectionId, target):
        for connect in self._connectors[connectionId]:
            connect(target)

    def GetBindingConnector(self, connectionId, target):
        return None

    def Load(self, component: XamlClass, xaml_str: str, xaml_path: str | Path | None) -> None:
        if xaml_path is not None:
            xaml_path = Path(xaml_path).absolute()

        xaml_preprocessed = self._preprocess(component, xaml_str)

        with NamedTemporaryFile(delete=False) as f:
            f.write(xaml_preprocessed.encode("utf-8"))
            f.close()

            approot = XamlApplication._XamlApplication__current.AppRoot()
            if xaml_path is not None and xaml_path.is_relative_to(approot):
                apppath = xaml_path.relative_to(approot).as_posix() + ".tmp"
                XamlApplication._XamlApplication__tmp_resource_file[apppath] = Path(f.name)
                resource_locator = Uri(f"ms-appx:///{apppath}")
            else:
                tmp_xaml_path = Path(f.name).as_posix()
                resource_locator = Uri(f"ms-appx:///{tmp_xaml_path}")

            Application.LoadComponent(component, resource_locator)

            Path(f.name).unlink()

    def _preprocess(self, component: XamlClass, xaml_str: str) -> str:
        root = ET.fromstring(xaml_str)
        for i, e in enumerate(root.iter()):
            self._connectors[i] = []
            for k, v in list(e.attrib.items()):
                if k == f"{{{XMLNS_XAML}}}Name":
                    self._connectors[i].append(partial(self._connect_name, component, v))
                elif k in _known_events:
                    if e == root:
                        self._connectors[i].append(partial(self._connect_event_root, component, k, v))
                    else:
                        self._connectors[i].append(partial(self._connect_event, component, k, v))
                    del e.attrib[k]
            if self._connectors[i]:
                e.attrib[f"{{{XMLNS_XAML}}}ConnectionId"] = str(i)
        return ET.tostring(root, encoding="unicode")

    def _connect_name(self, component, bind_name, target):
        setattr(component, bind_name, as_runtime_class(target))

    def _connect_event(self, component, event_name, method_name, target):
        event_setter = getattr(as_runtime_class(target), event_name)
        event_setter += getattr(component, method_name)

    def _connect_event_root(self, component, event_name, method_name, target):
        event_setter = getattr(component, event_name)
        event_setter += getattr(component, method_name)


# Load xaml and connect element and event handler to view object.
#
# <Button x:Name="Button1" Click="Button1_Click" />
#
# to be
#
# view.Button1 = Button()
# view.Button1.Click += view.Button1_Click
class XamlLoader:
    @classmethod
    def Load(cls, view: object, xaml_str: str) -> object:
        return cls().execute(view, xaml_str)

    def __init__(self):
        self._connectors = {}

    def execute(self, view, xaml_str):
        xaml_preprocessed = self._preprocess(view, xaml_str)
        uiroot = as_runtime_class(XamlReader.Load(xaml_preprocessed))
        self._connect(uiroot)
        return uiroot

    def _preprocess(self, view, xaml_str):
        root = ET.fromstring(xaml_str)
        for i, e in enumerate(root.iter()):
            if e is root:
                name = ""
            elif f"{{{XMLNS_XAML}}}Name" in e.attrib:
                name = e.attrib[f"{{{XMLNS_XAML}}}Name"]
            else:
                name = f"__dummy{i}"
            self._connectors[name] = []
            for k, v in list(e.attrib.items()):
                if k == f"{{{XMLNS_XAML}}}Name" and e is not root:
                    self._connectors[name].append(partial(self._connect_name, view, name))
                elif k in _known_events:
                    self._connectors[name].append(partial(self._connect_event, view, k, v))
                    del e.attrib[k]
            if self._connectors[name] and f"{{{XMLNS_XAML}}}Name" not in e.attrib and e is not root:
                e.attrib[f"{{{XMLNS_XAML}}}Name"] = name
        return ET.tostring(root, encoding="unicode")

    def _connect(self, uiroot):
        try:
            framework_element = uiroot.as_(FrameworkElement)
        except OSError:
            framework_element = uiroot.Content.as_(FrameworkElement)

        for name, connectors in self._connectors.items():
            for connect in connectors:
                if name == "":
                    target = uiroot
                else:
                    target = framework_element.FindName(name)
                connect(target)

    def _connect_name(self, view, bind_name, target):
        setattr(view, bind_name, as_runtime_class(target))

    def _connect_event(self, view, event_name, method_name, target):
        event_setter = getattr(as_runtime_class(target), event_name)
        event_setter += getattr(view, method_name)


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
        return TypeName(hstr(self._full_name), self._type_kind)

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
    hs = hstr(name)
    tn = TypeName(hs, kind)
    weakref.finalize(tn, hs.clear)
    return tn


def as_runtime_class(uielement):
    try:
        return uielement.as_(ISelf).GetSelf()
    except OSError:
        return uielement.as_(_get_runtime_class(uielement))


def _get_runtime_class(uielement):
    namespace, name = _get_runtime_class_name(uielement).rsplit(".", 1)
    module = importlib.import_module(f"win32more.{namespace}")
    return getattr(module, name)


def _get_runtime_class_name(uielement):
    hs = hstr(own=True)
    hr = uielement.GetRuntimeClassName(hs)
    if FAILED(hr):
        raise WinError(hr)
    return str(hs)


_known_events = {
    "AccessKeyDisplayDismissed",
    "AccessKeyDisplayRequested",
    "AccessKeyInvoked",
    "ActionButtonClick",
    "Activated",
    "ActualPlacementChanged",
    "ActualThemeChanged",
    "AddPages",
    "AddScrollVelocityRequested",
    "AddTabButtonClick",
    "AnchorRequested",
    "AnimatedVisualInvalidated",
    "ArrangeInvalidated",
    "BackRequested",
    "BeforeTextChanging",
    "BindingFailed",
    "BringIntoViewRequested",
    "BringingIntoView",
    "CalendarViewDayItemChanging",
    "CanExecuteChanged",
    "CanExecuteRequested",
    "CanScrollChanged",
    "CandidateWindowBoundsChanged",
    "Changed",
    "CharacterReceived",
    "Checked",
    "ChoosingGroupHeaderContainer",
    "ChoosingItemContainer",
    "CleanUpVirtualizedItemEvent",
    "Click",
    "CloseButtonClick",
    "CloseRequested",
    "Closed",
    "Closing",
    "Collapsed",
    "CollectionChanged",
    "ColorChanged",
    "Completed",
    "CompositionScaleChanged",
    "Confirmed",
    "ContainerContentChanging",
    "ContextCanceled",
    "ContextMenuOpening",
    "ContextRequested",
    "CopyingToClipboard",
    "CoreProcessFailed",
    "CoreWebView2Initialized",
    "CurrentChanged",
    "CurrentChanging",
    "CurrentStateChanged",
    "CurrentStateChanging",
    "CuttingToClipboard",
    "DataContextChanged",
    "DateChanged",
    "DatePicked",
    "DetailLabelRequested",
    "DirectManipulationCompleted",
    "DirectManipulationStarted",
    "DisplayModeChanged",
    "DoubleTapped",
    "DownloadProgress",
    "DragCompleted",
    "DragDelta",
    "DragEnter",
    "DragItemsCompleted",
    "DragItemsStarting",
    "DragLeave",
    "DragOver",
    "DragStarted",
    "DragStarting",
    "Drop",
    "DropCompleted",
    "DropDownClosed",
    "DropDownOpened",
    "DynamicOverflowItemsChanging",
    "EffectiveViewportChanged",
    "ElementClearing",
    "ElementIndexChanged",
    "ElementPrepared",
    "ErrorsChanged",
    "ExecuteRequested",
    "Expanding",
    "ExtentChanged",
    "ExternalTornOutTabsDropped",
    "ExternalTornOutTabsDropping",
    "FocusDisengaged",
    "FocusEngaged",
    "GetPreviewPage",
    "GettingFocus",
    "GotFocus",
    "Holding",
    "HorizontalSnapPointsChanged",
    "ImageFailed",
    "ImageOpened",
    "Indeterminate",
    "Invoked",
    "IsCheckedChanged",
    "IsDisplayModeEnabledChanged",
    "IsEnabledChanged",
    "IsScrollingWithMouseChanged",
    "IsTextTrimmedChanged",
    "ItemClick",
    "ItemClicked",
    "ItemInvoked",
    "ItemsChanged",
    "ItemsInfoRequested",
    "ItemsPicked",
    "ItemsUnlocked",
    "KeyDown",
    "KeyUp",
    "LayoutUpdated",
    "LoadCompleted",
    "Loaded",
    "Loading",
    "LosingFocus",
    "LostFocus",
    "ManipulationCompleted",
    "ManipulationDelta",
    "ManipulationInertiaStarting",
    "ManipulationStarted",
    "ManipulationStarting",
    "MapElementClick",
    "MapServiceErrorOccurred",
    "MeasureInvalidated",
    "ModeChanged",
    "Navigated",
    "Navigating",
    "NavigationCompleted",
    "NavigationFailed",
    "NavigationStarting",
    "NavigationStopped",
    "NoFocusCandidateFound",
    "OpenFailed",
    "Opened",
    "Opening",
    "Paginate",
    "PanRequested",
    "PaneClosed",
    "PaneClosing",
    "PaneOpened",
    "PaneOpening",
    "PaneToggleRequested",
    "PasswordChanged",
    "PasswordChanging",
    "Paste",
    "PivotItemLoaded",
    "PivotItemLoading",
    "PivotItemUnloaded",
    "PivotItemUnloading",
    "PointerCanceled",
    "PointerCaptureLost",
    "PointerEntered",
    "PointerExited",
    "PointerMoved",
    "PointerPressed",
    "PointerReleased",
    "PointerWheelChanged",
    "PreviewKeyDown",
    "PreviewKeyUp",
    "PrimaryButtonClick",
    "ProcessKeyboardAccelerators",
    "PropertyChanged",
    "QuerySubmitted",
    "RefreshRequested",
    "RefreshStateChanged",
    "Rendered",
    "Rendering",
    "ResourceManagerRequested",
    "RightTapped",
    "Scroll",
    "ScrollAnimationStarting",
    "ScrollByRequested",
    "ScrollCompleted",
    "ScrollToRequested",
    "Scrolling",
    "SecondaryButtonClick",
    "SectionHeaderClick",
    "SectionsInViewChanged",
    "SelectedDateChanged",
    "SelectedDatesChanged",
    "SelectedIndexChanged",
    "SelectedTimeChanged",
    "SelectionChanged",
    "SelectionChanging",
    "SizeChanged",
    "StateChanged",
    "SuggestionChosen",
    "SurfaceContentsLost",
    "TabCloseRequested",
    "TabDragCompleted",
    "TabDragStarting",
    "TabDroppedOutside",
    "TabItemsChanged",
    "TabStripDragOver",
    "TabStripDrop",
    "TabTearOutRequested",
    "TabTearOutWindowRequested",
    "TakeFocusRequested",
    "Tapped",
    "TextChanged",
    "TextChanging",
    "TextCompositionChanged",
    "TextCompositionEnded",
    "TextCompositionStarted",
    "TextSubmitted",
    "ThumbnailRequested",
    "Tick",
    "TimeChanged",
    "TimePicked",
    "Toggled",
    "TransitionCompleted",
    "Unchecked",
    "UnhandledException",
    "Unloaded",
    "ValueChanged",
    "VectorChanged",
    "VerticalSnapPointsChanged",
    "ViewChangeCompleted",
    "ViewChangeStarted",
    "ViewChanged",
    "ViewChanging",
    "VisibilityChanged",
    "WebMessageReceived",
    "XamlResourceReferenceFailed",
    "XamlShutdownCompletedOnThread",
    "ZoomAnimationStarting",
    "ZoomCompleted",
}
