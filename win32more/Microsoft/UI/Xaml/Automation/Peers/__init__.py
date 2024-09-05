from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Automation
import win32more.Microsoft.UI.Xaml.Automation.Peers
import win32more.Microsoft.UI.Xaml.Automation.Provider
import win32more.Microsoft.UI.Xaml.Controls
import win32more.Microsoft.UI.Xaml.Controls.Primitives
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class AccessibilityView(Enum, Int32):
    Raw = 0
    Control = 1
    Content = 2
class AnimatedVisualPlayerAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IAnimatedVisualPlayerAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.AnimatedVisualPlayerAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.AnimatedVisualPlayerAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IAnimatedVisualPlayerAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.AnimatedVisualPlayer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AnimatedVisualPlayerAutomationPeer: ...
class AppBarAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IAppBarAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.AppBarAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.AppBarAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IAppBarAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.AppBar, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AppBarAutomationPeer: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> win32more.Microsoft.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IToggleProvider) -> win32more.Microsoft.UI.Xaml.Automation.ToggleState: ...
    @winrt_mixinmethod
    def Toggle(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IToggleProvider) -> Void: ...
    @winrt_mixinmethod
    def get_IsModal(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTopmost(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_Maximizable(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_Minimizable(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_InteractionState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> win32more.Microsoft.UI.Xaml.Automation.WindowInteractionState: ...
    @winrt_mixinmethod
    def get_VisualState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> win32more.Microsoft.UI.Xaml.Automation.WindowVisualState: ...
    @winrt_mixinmethod
    def Close(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> Void: ...
    @winrt_mixinmethod
    def SetVisualState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider, state: win32more.Microsoft.UI.Xaml.Automation.WindowVisualState) -> Void: ...
    @winrt_mixinmethod
    def WaitForInputIdle(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider, milliseconds: Int32) -> Boolean: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
    InteractionState = property(get_InteractionState, None)
    IsModal = property(get_IsModal, None)
    IsTopmost = property(get_IsTopmost, None)
    Maximizable = property(get_Maximizable, None)
    Minimizable = property(get_Minimizable, None)
    ToggleState = property(get_ToggleState, None)
    VisualState = property(get_VisualState, None)
class AppBarButtonAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ButtonAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IAppBarButtonAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.AppBarButtonAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.AppBarButtonAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IAppBarButtonAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.AppBarButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AppBarButtonAutomationPeer: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> win32more.Microsoft.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class AppBarToggleButtonAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IAppBarToggleButtonAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.AppBarToggleButtonAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.AppBarToggleButtonAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IAppBarToggleButtonAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.AppBarToggleButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AppBarToggleButtonAutomationPeer: ...
class AutoSuggestBoxAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutoSuggestBoxAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.AutoSuggestBoxAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.AutoSuggestBoxAutomationPeer.CreateInstanceWithOwner(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutoSuggestBoxAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.AutoSuggestBox) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutoSuggestBoxAutomationPeer: ...
    @winrt_mixinmethod
    def Invoke(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
class AutomationControlType(Enum, Int32):
    Button = 0
    Calendar = 1
    CheckBox = 2
    ComboBox = 3
    Edit = 4
    Hyperlink = 5
    Image = 6
    ListItem = 7
    List = 8
    Menu = 9
    MenuBar = 10
    MenuItem = 11
    ProgressBar = 12
    RadioButton = 13
    ScrollBar = 14
    Slider = 15
    Spinner = 16
    StatusBar = 17
    Tab = 18
    TabItem = 19
    Text = 20
    ToolBar = 21
    ToolTip = 22
    Tree = 23
    TreeItem = 24
    Custom = 25
    Group = 26
    Thumb = 27
    DataGrid = 28
    DataItem = 29
    Document = 30
    SplitButton = 31
    Window = 32
    Pane = 33
    Header = 34
    HeaderItem = 35
    Table = 36
    TitleBar = 37
    Separator = 38
    SemanticZoom = 39
    AppBar = 40
    FlipView = 41
class AutomationEvents(Enum, Int32):
    ToolTipOpened = 0
    ToolTipClosed = 1
    MenuOpened = 2
    MenuClosed = 3
    AutomationFocusChanged = 4
    InvokePatternOnInvoked = 5
    SelectionItemPatternOnElementAddedToSelection = 6
    SelectionItemPatternOnElementRemovedFromSelection = 7
    SelectionItemPatternOnElementSelected = 8
    SelectionPatternOnInvalidated = 9
    TextPatternOnTextSelectionChanged = 10
    TextPatternOnTextChanged = 11
    AsyncContentLoaded = 12
    PropertyChanged = 13
    StructureChanged = 14
    DragStart = 15
    DragCancel = 16
    DragComplete = 17
    DragEnter = 18
    DragLeave = 19
    Dropped = 20
    LiveRegionChanged = 21
    InputReachedTarget = 22
    InputReachedOtherElement = 23
    InputDiscarded = 24
    WindowClosed = 25
    WindowOpened = 26
    ConversionTargetChanged = 27
    TextEditTextChanged = 28
    LayoutInvalidated = 29
class AutomationHeadingLevel(Enum, Int32):
    None_ = 0
    Level1 = 1
    Level2 = 2
    Level3 = 3
    Level4 = 4
    Level5 = 5
    Level6 = 6
    Level7 = 7
    Level8 = 8
    Level9 = 9
class AutomationLandmarkType(Enum, Int32):
    None_ = 0
    Custom = 1
    Form = 2
    Main = 3
    Navigation = 4
    Search = 5
class AutomationLiveSetting(Enum, Int32):
    Off = 0
    Polite = 1
    Assertive = 2
class AutomationNavigationDirection(Enum, Int32):
    Parent = 0
    NextSibling = 1
    PreviousSibling = 2
    FirstChild = 3
    LastChild = 4
class AutomationNotificationKind(Enum, Int32):
    ItemAdded = 0
    ItemRemoved = 1
    ActionCompleted = 2
    ActionAborted = 3
    Other = 4
class AutomationNotificationProcessing(Enum, Int32):
    ImportantAll = 0
    ImportantMostRecent = 1
    All = 2
    MostRecent = 3
    CurrentThenMostRecent = 4
class AutomationOrientation(Enum, Int32):
    None_ = 0
    Horizontal = 1
    Vertical = 2
class AutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.AutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def get_EventsSource(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def put_EventsSource(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_mixinmethod
    def GetPattern(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer, patternInterface: win32more.Microsoft.UI.Xaml.Automation.Peers.PatternInterface) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def RaiseAutomationEvent(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer, eventId: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationEvents) -> Void: ...
    @winrt_mixinmethod
    def RaisePropertyChangedEvent(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer, automationProperty: win32more.Microsoft.UI.Xaml.Automation.AutomationProperty, oldValue: win32more.Windows.Win32.System.WinRT.IInspectable, newValue: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def GetAcceleratorKey(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetAccessKey(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetAutomationControlType(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_mixinmethod
    def GetAutomationId(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetBoundingRectangle(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def GetChildren(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def Navigate(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer, direction: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def GetClassName(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetClickablePoint(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def GetHelpText(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetItemStatus(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetItemType(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLabeledBy(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def GetLocalizedControlType(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetName(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetOrientation(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationOrientation: ...
    @winrt_mixinmethod
    def HasKeyboardFocus(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsContentElement(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsControlElement(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsEnabled(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsKeyboardFocusable(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsOffscreen(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsPassword(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsRequiredForForm(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def SetFocus(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Void: ...
    @winrt_mixinmethod
    def GetParent(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def InvalidatePeer(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Void: ...
    @winrt_mixinmethod
    def GetPeerFromPoint(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer, point: win32more.Windows.Foundation.Point) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def GetElementFromPoint(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer, pointInWindowCoordinates: win32more.Windows.Foundation.Point) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def GetFocusedElement(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def GetLiveSetting(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_mixinmethod
    def ShowContextMenu(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Void: ...
    @winrt_mixinmethod
    def GetControlledPeers(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def GetAnnotations(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeerAnnotation]: ...
    @winrt_mixinmethod
    def SetParent(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer, peer: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_mixinmethod
    def RaiseTextEditTextChangedEvent(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer, automationTextEditChangeType: win32more.Microsoft.UI.Xaml.Automation.AutomationTextEditChangeType, changedData: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def GetPositionInSet(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Int32: ...
    @winrt_mixinmethod
    def GetSizeOfSet(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Int32: ...
    @winrt_mixinmethod
    def GetLevel(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Int32: ...
    @winrt_mixinmethod
    def RaiseStructureChangedEvent(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer, structureChangeType: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationStructureChangeType, child: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_mixinmethod
    def GetLandmarkType(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_mixinmethod
    def GetLocalizedLandmarkType(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def IsPeripheral(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsDataValidForForm(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def GetFullDescription(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetCulture(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Int32: ...
    @winrt_mixinmethod
    def RaiseNotificationEvent(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer, notificationKind: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationNotificationKind, notificationProcessing: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationNotificationProcessing, displayString: WinRT_String, activityId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetHeadingLevel(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_mixinmethod
    def IsDialog(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def PeerFromProvider(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerProtected, provider: win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def ProviderFromPeer(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerProtected, peer: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_mixinmethod
    def GetPatternCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides, patternInterface: win32more.Microsoft.UI.Xaml.Automation.Peers.PatternInterface) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def GetAcceleratorKeyCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetAccessKeyCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetAutomationControlTypeCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_mixinmethod
    def GetAutomationIdCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetBoundingRectangleCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def GetChildrenCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def NavigateCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides, direction: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def GetClassNameCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetClickablePointCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def GetHelpTextCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetItemStatusCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetItemTypeCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLabeledByCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def GetLocalizedControlTypeCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNameCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetOrientationCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationOrientation: ...
    @winrt_mixinmethod
    def HasKeyboardFocusCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsContentElementCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsControlElementCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsEnabledCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsKeyboardFocusableCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsOffscreenCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsPasswordCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsRequiredForFormCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def SetFocusCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Void: ...
    @winrt_mixinmethod
    def GetPeerFromPointCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides, point: win32more.Windows.Foundation.Point) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def GetElementFromPointCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides, pointInWindowCoordinates: win32more.Windows.Foundation.Point) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def GetFocusedElementCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def GetLiveSettingCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_mixinmethod
    def ShowContextMenuCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Void: ...
    @winrt_mixinmethod
    def GetControlledPeersCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def GetAnnotationsCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeerAnnotation]: ...
    @winrt_mixinmethod
    def GetPositionInSetCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Int32: ...
    @winrt_mixinmethod
    def GetSizeOfSetCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Int32: ...
    @winrt_mixinmethod
    def GetLevelCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Int32: ...
    @winrt_mixinmethod
    def GetLandmarkTypeCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_mixinmethod
    def GetLocalizedLandmarkTypeCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def IsPeripheralCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsDataValidForFormCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def GetFullDescriptionCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetDescribedByCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def GetFlowsToCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def GetFlowsFromCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def GetCultureCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Int32: ...
    @winrt_mixinmethod
    def GetHeadingLevelCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_mixinmethod
    def IsDialogCore(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_classmethod
    def ListenerExists(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerStatics, eventId: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationEvents) -> Boolean: ...
    @winrt_classmethod
    def GenerateRawElementProviderRuntimeId(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerStatics) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RawElementProviderRuntimeId: ...
    EventsSource = property(get_EventsSource, put_EventsSource)
class _AutomationPeerAnnotation_Meta_(ComPtr.__class__):
    pass
class AutomationPeerAnnotation(ComPtr, metaclass=_AutomationPeerAnnotation_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerAnnotation
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.AutomationPeerAnnotation'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeerAnnotation.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeerAnnotation.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeerAnnotation.CreateWithPeerParameter(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeerAnnotation: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerAnnotationFactory, type: win32more.Microsoft.UI.Xaml.Automation.AnnotationType) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeerAnnotation: ...
    @winrt_factorymethod
    def CreateWithPeerParameter(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerAnnotationFactory, type: win32more.Microsoft.UI.Xaml.Automation.AnnotationType, peer: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeerAnnotation: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerAnnotation) -> win32more.Microsoft.UI.Xaml.Automation.AnnotationType: ...
    @winrt_mixinmethod
    def put_Type(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerAnnotation, value: win32more.Microsoft.UI.Xaml.Automation.AnnotationType) -> Void: ...
    @winrt_mixinmethod
    def get_Peer(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerAnnotation) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def put_Peer(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerAnnotation, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_classmethod
    def get_TypeProperty(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerAnnotationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PeerProperty(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerAnnotationStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Peer = property(get_Peer, put_Peer)
    Type = property(get_Type, put_Type)
    _AutomationPeerAnnotation_Meta_.PeerProperty = property(get_PeerProperty, None)
    _AutomationPeerAnnotation_Meta_.TypeProperty = property(get_TypeProperty, None)
class AutomationStructureChangeType(Enum, Int32):
    ChildAdded = 0
    ChildRemoved = 1
    ChildrenInvalidated = 2
    ChildrenBulkAdded = 3
    ChildrenBulkRemoved = 4
    ChildrenReordered = 5
class BreadcrumbBarItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IBreadcrumbBarItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.BreadcrumbBarItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.BreadcrumbBarItemAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IBreadcrumbBarItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.BreadcrumbBarItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.BreadcrumbBarItemAutomationPeer: ...
    @winrt_mixinmethod
    def Invoke(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
class ButtonAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IButtonAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ButtonAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ButtonAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IButtonAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Button, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ButtonAutomationPeer: ...
    @winrt_mixinmethod
    def Invoke(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
class ButtonBaseAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IButtonBaseAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IButtonBaseAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.ButtonBase, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer: ...
class CalendarDatePickerAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ICalendarDatePickerAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.CalendarDatePickerAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.CalendarDatePickerAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ICalendarDatePickerAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.CalendarDatePicker, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.CalendarDatePickerAutomationPeer: ...
    @winrt_mixinmethod
    def Invoke(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IValueProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IValueProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetValue(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IValueProvider, value: WinRT_String) -> Void: ...
    IsReadOnly = property(get_IsReadOnly, None)
    Value = property(get_Value, None)
class CheckBoxAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ICheckBoxAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.CheckBoxAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.CheckBoxAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ICheckBoxAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.CheckBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.CheckBoxAutomationPeer: ...
class ColorPickerSliderAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.SliderAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IColorPickerSliderAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ColorPickerSliderAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ColorPickerSliderAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IColorPickerSliderAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.ColorPickerSlider, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ColorPickerSliderAutomationPeer: ...
class ColorSpectrumAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IColorSpectrumAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ColorSpectrumAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ColorSpectrumAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IColorSpectrumAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.ColorSpectrum, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ColorSpectrumAutomationPeer: ...
class ComboBoxAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IComboBoxAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ComboBoxAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ComboBoxAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IComboBoxAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ComboBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ComboBoxAutomationPeer: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IValueProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IValueProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetValue(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IValueProvider, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> win32more.Microsoft.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def get_IsModal(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTopmost(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_Maximizable(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_Minimizable(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_InteractionState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> win32more.Microsoft.UI.Xaml.Automation.WindowInteractionState: ...
    @winrt_mixinmethod
    def get_VisualState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> win32more.Microsoft.UI.Xaml.Automation.WindowVisualState: ...
    @winrt_mixinmethod
    def Close(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider) -> Void: ...
    @winrt_mixinmethod
    def SetVisualState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider, state: win32more.Microsoft.UI.Xaml.Automation.WindowVisualState) -> Void: ...
    @winrt_mixinmethod
    def WaitForInputIdle(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IWindowProvider, milliseconds: Int32) -> Boolean: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
    InteractionState = property(get_InteractionState, None)
    IsModal = property(get_IsModal, None)
    IsReadOnly = property(get_IsReadOnly, None)
    IsTopmost = property(get_IsTopmost, None)
    Maximizable = property(get_Maximizable, None)
    Minimizable = property(get_Minimizable, None)
    Value = property(get_Value, None)
    VisualState = property(get_VisualState, None)
class ComboBoxItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IComboBoxItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ComboBoxItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ComboBoxItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IComboBoxItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ComboBoxItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ComboBoxItemAutomationPeer: ...
class ComboBoxItemDataAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IComboBoxItemDataAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ComboBoxItemDataAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ComboBoxItemDataAutomationPeer.CreateInstanceWithParentAndItem(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IComboBoxItemDataAutomationPeerFactory, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.ComboBoxAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ComboBoxItemDataAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
class DatePickerAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IDatePickerAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.DatePickerAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.DatePickerAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IDatePickerAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.DatePicker, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.DatePickerAutomationPeer: ...
class DatePickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IDatePickerFlyoutPresenterAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.DatePickerFlyoutPresenterAutomationPeer'
class DropDownButtonAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ButtonAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IDropDownButtonAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.DropDownButtonAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.DropDownButtonAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IDropDownButtonAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.DropDownButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.DropDownButtonAutomationPeer: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> win32more.Microsoft.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class ExpanderAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IExpanderAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ExpanderAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ExpanderAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IExpanderAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Expander, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ExpanderAutomationPeer: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> win32more.Microsoft.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class FlipViewAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IFlipViewAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.FlipViewAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.FlipViewAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IFlipViewAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.FlipView, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.FlipViewAutomationPeer: ...
class FlipViewItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IFlipViewItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.FlipViewItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.FlipViewItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IFlipViewItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.FlipViewItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.FlipViewItemAutomationPeer: ...
class FlipViewItemDataAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IFlipViewItemDataAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.FlipViewItemDataAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.FlipViewItemDataAutomationPeer.CreateInstanceWithParentAndItem(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IFlipViewItemDataAutomationPeerFactory, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.FlipViewAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.FlipViewItemDataAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
class FlyoutPresenterAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IFlyoutPresenterAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.FlyoutPresenterAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.FlyoutPresenterAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IFlyoutPresenterAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.FlyoutPresenter, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.FlyoutPresenterAutomationPeer: ...
class FrameworkElementAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.FrameworkElement, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer: ...
    @winrt_mixinmethod
    def get_Owner(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeer) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def FromElement(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeerStatics, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_classmethod
    def CreatePeerForElement(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeerStatics, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    Owner = property(get_Owner, None)
class GridViewAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IGridViewAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.GridViewAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IGridViewAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.GridView, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewAutomationPeer: ...
class GridViewHeaderItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IGridViewHeaderItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.GridViewHeaderItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewHeaderItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IGridViewHeaderItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.GridViewHeaderItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewHeaderItemAutomationPeer: ...
class GridViewItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IGridViewItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.GridViewItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IGridViewItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.GridViewItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewItemAutomationPeer: ...
class GridViewItemDataAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IGridViewItemDataAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.GridViewItemDataAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewItemDataAutomationPeer.CreateInstanceWithParentAndItem(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IGridViewItemDataAutomationPeerFactory, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewItemDataAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
class GroupItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IGroupItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.GroupItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.GroupItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IGroupItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.GroupItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.GroupItemAutomationPeer: ...
class HubAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IHubAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.HubAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.HubAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IHubAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Hub, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.HubAutomationPeer: ...
class HubSectionAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IHubSectionAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.HubSectionAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.HubSectionAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IHubSectionAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.HubSection, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.HubSectionAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
class HyperlinkButtonAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IHyperlinkButtonAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.HyperlinkButtonAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.HyperlinkButtonAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IHyperlinkButtonAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.HyperlinkButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.HyperlinkButtonAutomationPeer: ...
    @winrt_mixinmethod
    def Invoke(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
class IAnimatedVisualPlayerAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAnimatedVisualPlayerAutomationPeer'
    _iid_ = Guid('{f949eeb6-b3ea-58ad-b62b-b7255bcc04df}')
class IAnimatedVisualPlayerAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAnimatedVisualPlayerAutomationPeerFactory'
    _iid_ = Guid('{d2a49198-80bb-51d6-b495-3dc5aab59589}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.AnimatedVisualPlayer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AnimatedVisualPlayerAutomationPeer: ...
class IAppBarAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAppBarAutomationPeer'
    _iid_ = Guid('{883a52e2-1810-5f1a-a9fd-1db0f9c62b02}')
class IAppBarAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAppBarAutomationPeerFactory'
    _iid_ = Guid('{64f68ce4-ad2d-5c18-abc0-d0157cc63088}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.AppBar, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AppBarAutomationPeer: ...
class IAppBarButtonAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAppBarButtonAutomationPeer'
    _iid_ = Guid('{439efdb4-141b-5fff-8723-03e6e69f6b36}')
class IAppBarButtonAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAppBarButtonAutomationPeerFactory'
    _iid_ = Guid('{6f611433-7e50-5e2e-b192-d6a285962c74}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.AppBarButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AppBarButtonAutomationPeer: ...
class IAppBarToggleButtonAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAppBarToggleButtonAutomationPeer'
    _iid_ = Guid('{17d28eb5-4635-5e2d-af01-8dcd23a608c4}')
class IAppBarToggleButtonAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAppBarToggleButtonAutomationPeerFactory'
    _iid_ = Guid('{3cb5ef43-ae92-5452-92e9-cd0ccca26891}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.AppBarToggleButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AppBarToggleButtonAutomationPeer: ...
class IAutoSuggestBoxAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAutoSuggestBoxAutomationPeer'
    _iid_ = Guid('{695236fc-0021-5936-bdf9-ed5991db0d52}')
class IAutoSuggestBoxAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAutoSuggestBoxAutomationPeerFactory'
    _iid_ = Guid('{c30950c9-b682-56df-9cb2-de6786fb8f90}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.AutoSuggestBox) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutoSuggestBoxAutomationPeer: ...
class IAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAutomationPeer'
    _iid_ = Guid('{e51d3e4e-34f0-568c-999f-6277e2afe6d7}')
    @winrt_commethod(6)
    def get_EventsSource(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(7)
    def put_EventsSource(self, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_commethod(8)
    def GetPattern(self, patternInterface: win32more.Microsoft.UI.Xaml.Automation.Peers.PatternInterface) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(9)
    def RaiseAutomationEvent(self, eventId: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationEvents) -> Void: ...
    @winrt_commethod(10)
    def RaisePropertyChangedEvent(self, automationProperty: win32more.Microsoft.UI.Xaml.Automation.AutomationProperty, oldValue: win32more.Windows.Win32.System.WinRT.IInspectable, newValue: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(11)
    def GetAcceleratorKey(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def GetAccessKey(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def GetAutomationControlType(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_commethod(14)
    def GetAutomationId(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def GetBoundingRectangle(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(16)
    def GetChildren(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(17)
    def Navigate(self, direction: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(18)
    def GetClassName(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def GetClickablePoint(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(20)
    def GetHelpText(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def GetItemStatus(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def GetItemType(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def GetLabeledBy(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(24)
    def GetLocalizedControlType(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def GetName(self) -> WinRT_String: ...
    @winrt_commethod(26)
    def GetOrientation(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationOrientation: ...
    @winrt_commethod(27)
    def HasKeyboardFocus(self) -> Boolean: ...
    @winrt_commethod(28)
    def IsContentElement(self) -> Boolean: ...
    @winrt_commethod(29)
    def IsControlElement(self) -> Boolean: ...
    @winrt_commethod(30)
    def IsEnabled(self) -> Boolean: ...
    @winrt_commethod(31)
    def IsKeyboardFocusable(self) -> Boolean: ...
    @winrt_commethod(32)
    def IsOffscreen(self) -> Boolean: ...
    @winrt_commethod(33)
    def IsPassword(self) -> Boolean: ...
    @winrt_commethod(34)
    def IsRequiredForForm(self) -> Boolean: ...
    @winrt_commethod(35)
    def SetFocus(self) -> Void: ...
    @winrt_commethod(36)
    def GetParent(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(37)
    def InvalidatePeer(self) -> Void: ...
    @winrt_commethod(38)
    def GetPeerFromPoint(self, point: win32more.Windows.Foundation.Point) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(39)
    def GetElementFromPoint(self, pointInWindowCoordinates: win32more.Windows.Foundation.Point) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(40)
    def GetFocusedElement(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(41)
    def GetLiveSetting(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_commethod(42)
    def ShowContextMenu(self) -> Void: ...
    @winrt_commethod(43)
    def GetControlledPeers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(44)
    def GetAnnotations(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeerAnnotation]: ...
    @winrt_commethod(45)
    def SetParent(self, peer: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_commethod(46)
    def RaiseTextEditTextChangedEvent(self, automationTextEditChangeType: win32more.Microsoft.UI.Xaml.Automation.AutomationTextEditChangeType, changedData: win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_commethod(47)
    def GetPositionInSet(self) -> Int32: ...
    @winrt_commethod(48)
    def GetSizeOfSet(self) -> Int32: ...
    @winrt_commethod(49)
    def GetLevel(self) -> Int32: ...
    @winrt_commethod(50)
    def RaiseStructureChangedEvent(self, structureChangeType: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationStructureChangeType, child: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_commethod(51)
    def GetLandmarkType(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_commethod(52)
    def GetLocalizedLandmarkType(self) -> WinRT_String: ...
    @winrt_commethod(53)
    def IsPeripheral(self) -> Boolean: ...
    @winrt_commethod(54)
    def IsDataValidForForm(self) -> Boolean: ...
    @winrt_commethod(55)
    def GetFullDescription(self) -> WinRT_String: ...
    @winrt_commethod(56)
    def GetCulture(self) -> Int32: ...
    @winrt_commethod(57)
    def RaiseNotificationEvent(self, notificationKind: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationNotificationKind, notificationProcessing: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationNotificationProcessing, displayString: WinRT_String, activityId: WinRT_String) -> Void: ...
    @winrt_commethod(58)
    def GetHeadingLevel(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_commethod(59)
    def IsDialog(self) -> Boolean: ...
    EventsSource = property(get_EventsSource, put_EventsSource)
class IAutomationPeerAnnotation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerAnnotation'
    _iid_ = Guid('{2738b92a-2528-5b63-973d-d29eb0593647}')
    @winrt_commethod(6)
    def get_Type(self) -> win32more.Microsoft.UI.Xaml.Automation.AnnotationType: ...
    @winrt_commethod(7)
    def put_Type(self, value: win32more.Microsoft.UI.Xaml.Automation.AnnotationType) -> Void: ...
    @winrt_commethod(8)
    def get_Peer(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(9)
    def put_Peer(self, value: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    Peer = property(get_Peer, put_Peer)
    Type = property(get_Type, put_Type)
class IAutomationPeerAnnotationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerAnnotationFactory'
    _iid_ = Guid('{25a1a202-bd68-5d41-a311-f84af9c8c440}')
    @winrt_commethod(6)
    def CreateInstance(self, type: win32more.Microsoft.UI.Xaml.Automation.AnnotationType) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeerAnnotation: ...
    @winrt_commethod(7)
    def CreateWithPeerParameter(self, type: win32more.Microsoft.UI.Xaml.Automation.AnnotationType, peer: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeerAnnotation: ...
class IAutomationPeerAnnotationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerAnnotationStatics'
    _iid_ = Guid('{c46105d7-8ca3-50e3-a1bc-b6bb2f9ce1cd}')
    @winrt_commethod(6)
    def get_TypeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PeerProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    PeerProperty = property(get_PeerProperty, None)
    TypeProperty = property(get_TypeProperty, None)
class IAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerFactory'
    _iid_ = Guid('{a1af86a0-6ec6-5be2-858f-72808be6fddd}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
class IAutomationPeerOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerOverrides'
    _iid_ = Guid('{44f8f6df-1b60-512d-a295-dd8c276c4618}')
    @winrt_commethod(6)
    def GetPatternCore(self, patternInterface: win32more.Microsoft.UI.Xaml.Automation.Peers.PatternInterface) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def GetAcceleratorKeyCore(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetAccessKeyCore(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetAutomationControlTypeCore(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_commethod(10)
    def GetAutomationIdCore(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def GetBoundingRectangleCore(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(12)
    def GetChildrenCore(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(13)
    def NavigateCore(self, direction: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(14)
    def GetClassNameCore(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def GetClickablePointCore(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(16)
    def GetHelpTextCore(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def GetItemStatusCore(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def GetItemTypeCore(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def GetLabeledByCore(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(20)
    def GetLocalizedControlTypeCore(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def GetNameCore(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def GetOrientationCore(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationOrientation: ...
    @winrt_commethod(23)
    def HasKeyboardFocusCore(self) -> Boolean: ...
    @winrt_commethod(24)
    def IsContentElementCore(self) -> Boolean: ...
    @winrt_commethod(25)
    def IsControlElementCore(self) -> Boolean: ...
    @winrt_commethod(26)
    def IsEnabledCore(self) -> Boolean: ...
    @winrt_commethod(27)
    def IsKeyboardFocusableCore(self) -> Boolean: ...
    @winrt_commethod(28)
    def IsOffscreenCore(self) -> Boolean: ...
    @winrt_commethod(29)
    def IsPasswordCore(self) -> Boolean: ...
    @winrt_commethod(30)
    def IsRequiredForFormCore(self) -> Boolean: ...
    @winrt_commethod(31)
    def SetFocusCore(self) -> Void: ...
    @winrt_commethod(32)
    def GetPeerFromPointCore(self, point: win32more.Windows.Foundation.Point) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(33)
    def GetElementFromPointCore(self, pointInWindowCoordinates: win32more.Windows.Foundation.Point) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(34)
    def GetFocusedElementCore(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(35)
    def GetLiveSettingCore(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_commethod(36)
    def ShowContextMenuCore(self) -> Void: ...
    @winrt_commethod(37)
    def GetControlledPeersCore(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(38)
    def GetAnnotationsCore(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeerAnnotation]: ...
    @winrt_commethod(39)
    def GetPositionInSetCore(self) -> Int32: ...
    @winrt_commethod(40)
    def GetSizeOfSetCore(self) -> Int32: ...
    @winrt_commethod(41)
    def GetLevelCore(self) -> Int32: ...
    @winrt_commethod(42)
    def GetLandmarkTypeCore(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_commethod(43)
    def GetLocalizedLandmarkTypeCore(self) -> WinRT_String: ...
    @winrt_commethod(44)
    def IsPeripheralCore(self) -> Boolean: ...
    @winrt_commethod(45)
    def IsDataValidForFormCore(self) -> Boolean: ...
    @winrt_commethod(46)
    def GetFullDescriptionCore(self) -> WinRT_String: ...
    @winrt_commethod(47)
    def GetDescribedByCore(self) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(48)
    def GetFlowsToCore(self) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(49)
    def GetFlowsFromCore(self) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(50)
    def GetCultureCore(self) -> Int32: ...
    @winrt_commethod(51)
    def GetHeadingLevelCore(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_commethod(52)
    def IsDialogCore(self) -> Boolean: ...
class IAutomationPeerProtected(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerProtected'
    _iid_ = Guid('{9663b2c3-8c1f-56d4-abd9-268082a9e8bc}')
    @winrt_commethod(6)
    def PeerFromProvider(self, provider: win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(7)
    def ProviderFromPeer(self, peer: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class IAutomationPeerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IAutomationPeerStatics'
    _iid_ = Guid('{90b157ff-18d5-5623-850c-612ceae576bd}')
    @winrt_commethod(6)
    def ListenerExists(self, eventId: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationEvents) -> Boolean: ...
    @winrt_commethod(7)
    def GenerateRawElementProviderRuntimeId(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RawElementProviderRuntimeId: ...
class IBreadcrumbBarItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IBreadcrumbBarItemAutomationPeer'
    _iid_ = Guid('{48e81612-7de0-5065-b881-04ebfff90497}')
class IBreadcrumbBarItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IBreadcrumbBarItemAutomationPeerFactory'
    _iid_ = Guid('{dfb02146-405f-52ed-a873-0ed4942850be}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.BreadcrumbBarItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.BreadcrumbBarItemAutomationPeer: ...
class IButtonAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IButtonAutomationPeer'
    _iid_ = Guid('{a3a2e96b-8a2d-50bf-9b3d-dfbc4653f5a6}')
class IButtonAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IButtonAutomationPeerFactory'
    _iid_ = Guid('{1c2f87b7-fbc1-56b0-a654-550d61c423d1}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Button, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ButtonAutomationPeer: ...
class IButtonBaseAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IButtonBaseAutomationPeer'
    _iid_ = Guid('{7a88a2d8-f8dd-5526-8a40-e2e3888193bf}')
class IButtonBaseAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IButtonBaseAutomationPeerFactory'
    _iid_ = Guid('{d6e707bb-7299-5f7a-9c03-7fa10f939771}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.ButtonBase, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer: ...
class ICalendarDatePickerAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ICalendarDatePickerAutomationPeer'
    _iid_ = Guid('{246d63e3-812f-5f28-8d18-af79409a4f95}')
class ICalendarDatePickerAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ICalendarDatePickerAutomationPeerFactory'
    _iid_ = Guid('{6d272c12-68a3-586e-879b-571e606803b4}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.CalendarDatePicker, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.CalendarDatePickerAutomationPeer: ...
class ICheckBoxAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ICheckBoxAutomationPeer'
    _iid_ = Guid('{9b449814-2c1a-5bdc-9524-1df91c06e992}')
class ICheckBoxAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ICheckBoxAutomationPeerFactory'
    _iid_ = Guid('{0f5b9e3c-6de5-588e-835f-3228be930fea}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.CheckBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.CheckBoxAutomationPeer: ...
class IColorPickerSliderAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IColorPickerSliderAutomationPeer'
    _iid_ = Guid('{793d35d4-4152-50fa-b5f4-f6c045c1339d}')
class IColorPickerSliderAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IColorPickerSliderAutomationPeerFactory'
    _iid_ = Guid('{e5f9093f-5e2c-5148-b5d1-1cda4eb86913}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.ColorPickerSlider, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ColorPickerSliderAutomationPeer: ...
class IColorSpectrumAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IColorSpectrumAutomationPeer'
    _iid_ = Guid('{005ac3d1-b031-58ab-918d-030fabaeaf87}')
class IColorSpectrumAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IColorSpectrumAutomationPeerFactory'
    _iid_ = Guid('{cfccae7e-fe0f-5c9c-9d1a-69e20e0232cf}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.ColorSpectrum, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ColorSpectrumAutomationPeer: ...
class IComboBoxAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IComboBoxAutomationPeer'
    _iid_ = Guid('{459d2245-1fd2-5dda-822c-bed13df6776b}')
class IComboBoxAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IComboBoxAutomationPeerFactory'
    _iid_ = Guid('{d094829f-2a6f-5b1f-a0ce-0f682cc56c0f}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.ComboBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ComboBoxAutomationPeer: ...
class IComboBoxItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IComboBoxItemAutomationPeer'
    _iid_ = Guid('{3d4195bc-b579-5cda-b56f-1e7399e14122}')
class IComboBoxItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IComboBoxItemAutomationPeerFactory'
    _iid_ = Guid('{ead9d22d-112b-550e-8cac-760614f979aa}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.ComboBoxItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ComboBoxItemAutomationPeer: ...
class IComboBoxItemDataAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IComboBoxItemDataAutomationPeer'
    _iid_ = Guid('{65b69b50-cbc3-5ae7-bf9c-2794fe56c6b3}')
class IComboBoxItemDataAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IComboBoxItemDataAutomationPeerFactory'
    _iid_ = Guid('{66778718-8757-56d5-bd3a-f2ff40e83a78}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.ComboBoxAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ComboBoxItemDataAutomationPeer: ...
class IDatePickerAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IDatePickerAutomationPeer'
    _iid_ = Guid('{f3d7c3e5-c817-58a5-bb47-d9eb228f3ba0}')
class IDatePickerAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IDatePickerAutomationPeerFactory'
    _iid_ = Guid('{480f7825-b4a7-5c56-9f8a-fed84b9348ae}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.DatePicker, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.DatePickerAutomationPeer: ...
class IDatePickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IDatePickerFlyoutPresenterAutomationPeer'
    _iid_ = Guid('{600b7162-0529-5fd1-b6e4-41dc37eda513}')
class IDropDownButtonAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IDropDownButtonAutomationPeer'
    _iid_ = Guid('{7dc37dec-0a0a-5c98-8a6f-9e47dbab2f82}')
class IDropDownButtonAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IDropDownButtonAutomationPeerFactory'
    _iid_ = Guid('{68c4bffa-1685-5936-b219-517e87fd591f}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.DropDownButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.DropDownButtonAutomationPeer: ...
class IExpanderAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IExpanderAutomationPeer'
    _iid_ = Guid('{f7527408-cc89-5b65-bbde-eae6d66dc3e5}')
class IExpanderAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IExpanderAutomationPeerFactory'
    _iid_ = Guid('{2024523b-4a40-5976-aaab-0f05664f7494}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.Expander, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ExpanderAutomationPeer: ...
class IFlipViewAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IFlipViewAutomationPeer'
    _iid_ = Guid('{9f2901ea-23cb-5cac-87d4-7fa9c7ffbc60}')
class IFlipViewAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IFlipViewAutomationPeerFactory'
    _iid_ = Guid('{e73c7f75-ed47-522a-8a27-45feda1031f0}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.FlipView, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.FlipViewAutomationPeer: ...
class IFlipViewItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IFlipViewItemAutomationPeer'
    _iid_ = Guid('{3569b1bb-7601-56de-812a-171455d8ad32}')
class IFlipViewItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IFlipViewItemAutomationPeerFactory'
    _iid_ = Guid('{aa3b880f-62cb-5878-8f0b-7b3548c65080}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.FlipViewItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.FlipViewItemAutomationPeer: ...
class IFlipViewItemDataAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IFlipViewItemDataAutomationPeer'
    _iid_ = Guid('{3bb31a93-e737-501d-b9a6-a11461c9bcf5}')
class IFlipViewItemDataAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IFlipViewItemDataAutomationPeerFactory'
    _iid_ = Guid('{6f892ace-4467-587c-953c-c1c13b632e5f}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.FlipViewAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.FlipViewItemDataAutomationPeer: ...
class IFlyoutPresenterAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IFlyoutPresenterAutomationPeer'
    _iid_ = Guid('{e589b818-4a64-58c5-9c0b-5cea0f867e9b}')
class IFlyoutPresenterAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IFlyoutPresenterAutomationPeerFactory'
    _iid_ = Guid('{e529e586-7aa3-50a6-b17e-678b54fee127}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.FlyoutPresenter, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.FlyoutPresenterAutomationPeer: ...
class IFrameworkElementAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeer'
    _iid_ = Guid('{7dab4f24-605c-51cb-87db-3eed1b9fb37b}')
    @winrt_commethod(6)
    def get_Owner(self) -> win32more.Microsoft.UI.Xaml.UIElement: ...
    Owner = property(get_Owner, None)
class IFrameworkElementAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeerFactory'
    _iid_ = Guid('{1682c3f8-238d-5c7e-a5a5-08cc3c10ac7c}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.FrameworkElement, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer: ...
class IFrameworkElementAutomationPeerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeerStatics'
    _iid_ = Guid('{081f6fbe-6500-528a-a506-f5a4d41ddf6c}')
    @winrt_commethod(6)
    def FromElement(self, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(7)
    def CreatePeerForElement(self, element: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer: ...
class IGridViewAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IGridViewAutomationPeer'
    _iid_ = Guid('{7870992f-3328-53c2-b412-2914438975b4}')
class IGridViewAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IGridViewAutomationPeerFactory'
    _iid_ = Guid('{71b829e1-7d57-580b-b1a6-d780ed992248}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.GridView, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewAutomationPeer: ...
class IGridViewHeaderItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IGridViewHeaderItemAutomationPeer'
    _iid_ = Guid('{c38af4b0-2757-569b-bdc7-a5b7b74ffdba}')
class IGridViewHeaderItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IGridViewHeaderItemAutomationPeerFactory'
    _iid_ = Guid('{6161999a-e042-5d9b-aa38-9fe1296bfb01}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.GridViewHeaderItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewHeaderItemAutomationPeer: ...
class IGridViewItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IGridViewItemAutomationPeer'
    _iid_ = Guid('{de249c2e-5419-5798-b625-cd2c05307572}')
class IGridViewItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IGridViewItemAutomationPeerFactory'
    _iid_ = Guid('{04735951-0f91-53f5-984b-75bf0ed41540}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.GridViewItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewItemAutomationPeer: ...
class IGridViewItemDataAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IGridViewItemDataAutomationPeer'
    _iid_ = Guid('{0372c2a0-5094-5811-96ba-0dbe77187435}')
class IGridViewItemDataAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IGridViewItemDataAutomationPeerFactory'
    _iid_ = Guid('{44137b3e-c6f3-53ce-915d-fc8e60ccee74}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.GridViewItemDataAutomationPeer: ...
class IGroupItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IGroupItemAutomationPeer'
    _iid_ = Guid('{2ff50701-4164-511d-bb23-d21eb88d5eb9}')
class IGroupItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IGroupItemAutomationPeerFactory'
    _iid_ = Guid('{cdb10ed9-d1d3-5faa-8772-70014da666b3}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.GroupItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.GroupItemAutomationPeer: ...
class IHubAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IHubAutomationPeer'
    _iid_ = Guid('{8fa20cb6-42c1-531e-b54f-fcaf33c943a9}')
class IHubAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IHubAutomationPeerFactory'
    _iid_ = Guid('{c1b1f1cf-3926-56c9-b690-530c8bc78806}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Hub, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.HubAutomationPeer: ...
class IHubSectionAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IHubSectionAutomationPeer'
    _iid_ = Guid('{174e94ab-c033-534a-895c-eaaf1dcc4352}')
class IHubSectionAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IHubSectionAutomationPeerFactory'
    _iid_ = Guid('{dc56cf08-2031-56b6-9ad5-7f8d7475d35d}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.HubSection, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.HubSectionAutomationPeer: ...
class IHyperlinkButtonAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IHyperlinkButtonAutomationPeer'
    _iid_ = Guid('{6a770ab2-02d0-59ba-a28e-3dfba1f10dd8}')
class IHyperlinkButtonAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IHyperlinkButtonAutomationPeerFactory'
    _iid_ = Guid('{2476e661-abce-5d35-b38b-6cee2c4148f4}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.HyperlinkButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.HyperlinkButtonAutomationPeer: ...
class IImageAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IImageAutomationPeer'
    _iid_ = Guid('{1f6eb184-8765-5455-bd1d-93c251c17f9b}')
class IImageAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IImageAutomationPeerFactory'
    _iid_ = Guid('{1b26001b-49a6-5ff4-b1b1-2d504d2ef133}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Image, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ImageAutomationPeer: ...
class IInfoBarAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IInfoBarAutomationPeer'
    _iid_ = Guid('{aa2c40eb-df80-5050-92c5-5fda5abfdef2}')
class IInfoBarAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IInfoBarAutomationPeerFactory'
    _iid_ = Guid('{5fd3e590-68b9-5c9c-a572-0bc10167ce46}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.InfoBar, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.InfoBarAutomationPeer: ...
class IItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IItemAutomationPeer'
    _iid_ = Guid('{be8a71bb-3e36-54d2-920e-60722f1c62ff}')
    @winrt_commethod(6)
    def get_Item(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_ItemsControlAutomationPeer(self) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer: ...
    Item = property(get_Item, None)
    ItemsControlAutomationPeer = property(get_ItemsControlAutomationPeer, None)
class IItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IItemAutomationPeerFactory'
    _iid_ = Guid('{ffe08885-14ac-5859-b031-5f3a4c504e6d}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
class IItemContainerAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IItemContainerAutomationPeer'
    _iid_ = Guid('{f915a1fb-754e-58c7-ad2a-b99528701793}')
class IItemContainerAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IItemContainerAutomationPeerFactory'
    _iid_ = Guid('{4600cfb3-72e1-5181-95ec-653f30b01c78}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.ItemContainer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemContainerAutomationPeer: ...
class IItemsControlAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IItemsControlAutomationPeer'
    _iid_ = Guid('{0ae7bb7e-1407-5947-985f-9d542f433ab1}')
    @winrt_commethod(6)
    def CreateItemAutomationPeer(self, item: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
class IItemsControlAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IItemsControlAutomationPeerFactory'
    _iid_ = Guid('{9de524cc-5e66-51a0-a7e0-a1742d28334b}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.ItemsControl, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer: ...
class IItemsControlAutomationPeerOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IItemsControlAutomationPeerOverrides'
    _iid_ = Guid('{d751b35b-236e-5859-a834-52fa369cd3bd}')
    @winrt_commethod(6)
    def OnCreateItemAutomationPeer(self, item: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
class IItemsViewAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IItemsViewAutomationPeer'
    _iid_ = Guid('{d456ad6d-18d5-51ae-a44e-95671f848184}')
class IItemsViewAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IItemsViewAutomationPeerFactory'
    _iid_ = Guid('{8fd329c7-ea9c-56a3-a79e-bfff5ca74323}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.ItemsView, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemsViewAutomationPeer: ...
class IListBoxAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListBoxAutomationPeer'
    _iid_ = Guid('{2bc1ca3f-3617-53a8-94b9-bec91d573525}')
class IListBoxAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListBoxAutomationPeerFactory'
    _iid_ = Guid('{004aaf6f-a12c-5fa4-a1f7-e3b0fbe45ddd}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.ListBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListBoxAutomationPeer: ...
class IListBoxItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListBoxItemAutomationPeer'
    _iid_ = Guid('{19a8c4b4-e63a-5b2e-8e2f-c834e6a08204}')
class IListBoxItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListBoxItemAutomationPeerFactory'
    _iid_ = Guid('{936e36ef-0fae-58a2-8fb2-313999793263}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.ListBoxItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListBoxItemAutomationPeer: ...
class IListBoxItemDataAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListBoxItemDataAutomationPeer'
    _iid_ = Guid('{2b81660f-46dc-5765-b10a-2269d12eba42}')
class IListBoxItemDataAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListBoxItemDataAutomationPeerFactory'
    _iid_ = Guid('{2ce97068-5280-5bec-8ba5-785c58986dcf}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.ListBoxAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListBoxItemDataAutomationPeer: ...
class IListPickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListPickerFlyoutPresenterAutomationPeer'
    _iid_ = Guid('{16574767-e8ca-551a-a9e9-e5394de33469}')
class IListViewAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListViewAutomationPeer'
    _iid_ = Guid('{8f2a3373-e305-55f3-923e-d9eee8d1a6ee}')
class IListViewAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListViewAutomationPeerFactory'
    _iid_ = Guid('{3c6d8fc2-57ea-584e-9a89-504c65251d0f}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.ListView, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewAutomationPeer: ...
class IListViewBaseAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListViewBaseAutomationPeer'
    _iid_ = Guid('{ad9a395c-5a96-5331-9636-ee4c53184986}')
class IListViewBaseAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListViewBaseAutomationPeerFactory'
    _iid_ = Guid('{361ed030-7c93-5967-97cb-4a9693e34050}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.ListViewBase, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer: ...
class IListViewBaseHeaderItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListViewBaseHeaderItemAutomationPeer'
    _iid_ = Guid('{623314d2-c7f1-5003-9560-07d420a33a2a}')
class IListViewBaseHeaderItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListViewBaseHeaderItemAutomationPeerFactory'
    _iid_ = Guid('{e6041212-904b-5d22-b856-d3ef53d16aa6}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.ListViewBaseHeaderItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer: ...
class IListViewHeaderItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListViewHeaderItemAutomationPeer'
    _iid_ = Guid('{0293eaca-f7de-5a0d-9beb-79dc1ac4a7de}')
class IListViewHeaderItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListViewHeaderItemAutomationPeerFactory'
    _iid_ = Guid('{f7b3480b-bfff-5c1c-b9d5-8eee544aebf8}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.ListViewHeaderItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewHeaderItemAutomationPeer: ...
class IListViewItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListViewItemAutomationPeer'
    _iid_ = Guid('{de487f2c-5a61-599e-b9ff-0fd7675d7af3}')
class IListViewItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListViewItemAutomationPeerFactory'
    _iid_ = Guid('{d6625ba7-1ae3-58b1-af12-e5cd5afc17ff}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.ListViewItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer: ...
class IListViewItemDataAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListViewItemDataAutomationPeer'
    _iid_ = Guid('{88bb28d3-45ed-5415-825f-dd2da536c968}')
class IListViewItemDataAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IListViewItemDataAutomationPeerFactory'
    _iid_ = Guid('{9b22e7ea-6f7a-5c05-8072-5bddf54f9bda}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewItemDataAutomationPeer: ...
class ILoopingSelectorAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ILoopingSelectorAutomationPeer'
    _iid_ = Guid('{00b612f4-8faf-5c0c-92e4-4396e0f7b8d8}')
class ILoopingSelectorItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ILoopingSelectorItemAutomationPeer'
    _iid_ = Guid('{9c108861-895f-5e92-84c1-ff12072e7ec0}')
class ILoopingSelectorItemDataAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ILoopingSelectorItemDataAutomationPeer'
    _iid_ = Guid('{1f8362eb-a069-5121-a56b-619365b4515c}')
class IMediaPlayerElementAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IMediaPlayerElementAutomationPeer'
    _iid_ = Guid('{f68b8ca2-4428-5c35-b6a8-1b2ea062c22c}')
class IMediaPlayerElementAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IMediaPlayerElementAutomationPeerFactory'
    _iid_ = Guid('{2ae1aa11-7a7c-5580-a7d7-f7597859bdc2}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.MediaPlayerElement, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.MediaPlayerElementAutomationPeer: ...
class IMediaTransportControlsAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IMediaTransportControlsAutomationPeer'
    _iid_ = Guid('{da850d4e-8715-5ae7-81a9-abd10d17c1ed}')
class IMediaTransportControlsAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IMediaTransportControlsAutomationPeerFactory'
    _iid_ = Guid('{77f281e1-cb51-5360-b74e-6fe4f8ee5028}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.MediaTransportControls, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.MediaTransportControlsAutomationPeer: ...
class IMenuBarAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IMenuBarAutomationPeer'
    _iid_ = Guid('{ae96e710-b9d3-59dd-973e-1bbc86cf0afc}')
class IMenuBarAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IMenuBarAutomationPeerFactory'
    _iid_ = Guid('{d3e1ca3f-1702-5bd3-8adb-e6f6cb9e7531}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.MenuBar, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.MenuBarAutomationPeer: ...
class IMenuBarItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IMenuBarItemAutomationPeer'
    _iid_ = Guid('{2da890cd-0aae-53b9-8c12-81003f60ed14}')
class IMenuBarItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IMenuBarItemAutomationPeerFactory'
    _iid_ = Guid('{603b63c4-a626-50e6-9c1a-649699ca7ad6}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.MenuBarItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.MenuBarItemAutomationPeer: ...
class IMenuFlyoutItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IMenuFlyoutItemAutomationPeer'
    _iid_ = Guid('{fdb57952-2a4f-5ed4-8ada-320def75ea71}')
class IMenuFlyoutItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IMenuFlyoutItemAutomationPeerFactory'
    _iid_ = Guid('{fe125e46-7c1c-5a7c-98e0-c7aa3a00a6cd}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.MenuFlyoutItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.MenuFlyoutItemAutomationPeer: ...
class IMenuFlyoutPresenterAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IMenuFlyoutPresenterAutomationPeer'
    _iid_ = Guid('{74d3ff77-1e92-5f96-99a1-697d74283ba7}')
class IMenuFlyoutPresenterAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IMenuFlyoutPresenterAutomationPeerFactory'
    _iid_ = Guid('{beadfdfc-1035-5ffd-bae6-03f754b05dcc}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.MenuFlyoutPresenter, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.MenuFlyoutPresenterAutomationPeer: ...
class INavigationViewAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.INavigationViewAutomationPeer'
    _iid_ = Guid('{72013eae-b015-550d-ba8d-a05112b62731}')
class INavigationViewAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.INavigationViewAutomationPeerFactory'
    _iid_ = Guid('{75075b03-a2f7-5869-b23c-63cbe5acc43a}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.NavigationView, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.NavigationViewAutomationPeer: ...
class INavigationViewItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.INavigationViewItemAutomationPeer'
    _iid_ = Guid('{c7924c7a-739f-5251-9b86-df6486eb08a7}')
class INavigationViewItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.INavigationViewItemAutomationPeerFactory'
    _iid_ = Guid('{890516d0-5a62-528b-8873-4f7140b40489}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.NavigationViewItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.NavigationViewItemAutomationPeer: ...
class INumberBoxAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.INumberBoxAutomationPeer'
    _iid_ = Guid('{235befeb-6c98-5d35-a2e7-001eae342509}')
class INumberBoxAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.INumberBoxAutomationPeerFactory'
    _iid_ = Guid('{659719ac-4405-58f4-bde2-ef61dfe64c21}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.NumberBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.NumberBoxAutomationPeer: ...
class IPasswordBoxAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IPasswordBoxAutomationPeer'
    _iid_ = Guid('{49b18dba-fa3b-5106-a1e8-1aaa3d24d5e1}')
class IPasswordBoxAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IPasswordBoxAutomationPeerFactory'
    _iid_ = Guid('{7b0d5cba-c5b3-553e-989a-a10ee04144af}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.PasswordBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.PasswordBoxAutomationPeer: ...
class IPersonPictureAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IPersonPictureAutomationPeer'
    _iid_ = Guid('{2e71779b-aca4-52c2-8a25-bc5f1ee3b0ae}')
class IPersonPictureAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IPersonPictureAutomationPeerFactory'
    _iid_ = Guid('{bd1709e5-1940-56fc-b5c3-85e4570951cc}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.PersonPicture, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.PersonPictureAutomationPeer: ...
class IPickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IPickerFlyoutPresenterAutomationPeer'
    _iid_ = Guid('{b29f6d28-154b-5c1d-a5e8-98604bb5cdf6}')
class IPipsPagerAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IPipsPagerAutomationPeer'
    _iid_ = Guid('{93de1bc2-cf84-5b5f-91be-a7c781b2021a}')
class IPipsPagerAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IPipsPagerAutomationPeerFactory'
    _iid_ = Guid('{fb5248ef-e835-5997-bc36-d4e5db4a1b5a}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.PipsPager, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.PipsPagerAutomationPeer: ...
class IPivotAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IPivotAutomationPeer'
    _iid_ = Guid('{84225540-a6a3-5e65-a3dc-b31b81ab14c1}')
class IPivotAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IPivotAutomationPeerFactory'
    _iid_ = Guid('{b1dd0229-c14c-5ac0-8331-be24fa2007f0}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Pivot) -> win32more.Microsoft.UI.Xaml.Automation.Peers.PivotAutomationPeer: ...
class IPivotItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IPivotItemAutomationPeer'
    _iid_ = Guid('{bfe7fb7b-2d88-56e4-b50f-0a40de6f52a1}')
class IPivotItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IPivotItemAutomationPeerFactory'
    _iid_ = Guid('{14966ee7-afaf-5fcc-9346-f0e7192c220a}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.PivotItem) -> win32more.Microsoft.UI.Xaml.Automation.Peers.PivotItemAutomationPeer: ...
class IPivotItemDataAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IPivotItemDataAutomationPeer'
    _iid_ = Guid('{6758ebee-b3e0-5feb-aaba-b7f6c59fe49f}')
class IPivotItemDataAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IPivotItemDataAutomationPeerFactory'
    _iid_ = Guid('{26d7a6e9-ce6b-5690-9024-75ce5770b0d6}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.PivotAutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Peers.PivotItemDataAutomationPeer: ...
class IProgressBarAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IProgressBarAutomationPeer'
    _iid_ = Guid('{8565ead9-b877-52c7-a147-6fe1fee767af}')
class IProgressBarAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IProgressBarAutomationPeerFactory'
    _iid_ = Guid('{cea28c0d-c4b3-5d18-aef6-958031395878}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.ProgressBar, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ProgressBarAutomationPeer: ...
class IProgressRingAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IProgressRingAutomationPeer'
    _iid_ = Guid('{3b6952da-9e44-52b0-91df-39da9dc1d8b0}')
class IProgressRingAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IProgressRingAutomationPeerFactory'
    _iid_ = Guid('{650f375c-3b29-5376-a7f7-c78082b82d13}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.ProgressRing, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ProgressRingAutomationPeer: ...
class IRadioButtonAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRadioButtonAutomationPeer'
    _iid_ = Guid('{cce147b7-574a-53b6-a5b2-ca2622a79b2c}')
class IRadioButtonAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRadioButtonAutomationPeerFactory'
    _iid_ = Guid('{ca07c7ee-502a-509e-bc44-682e6828d1f8}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.RadioButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RadioButtonAutomationPeer: ...
class IRadioButtonsAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRadioButtonsAutomationPeer'
    _iid_ = Guid('{fff86275-0cdd-54db-9d88-9c0e5f9bcb4d}')
class IRadioButtonsAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRadioButtonsAutomationPeerFactory'
    _iid_ = Guid('{f13521d0-056e-598c-ad23-a7150049d80a}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.RadioButtons, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RadioButtonsAutomationPeer: ...
class IRangeBaseAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRangeBaseAutomationPeer'
    _iid_ = Guid('{b5d50512-70a9-5b27-82fe-16f6ba67bac5}')
class IRangeBaseAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRangeBaseAutomationPeerFactory'
    _iid_ = Guid('{8c8f25e9-5194-54a9-b787-ce0293fd6721}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.RangeBase, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer: ...
class IRatingControlAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRatingControlAutomationPeer'
    _iid_ = Guid('{55493ec4-926b-595a-97a3-a7fa604188a4}')
class IRatingControlAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRatingControlAutomationPeerFactory'
    _iid_ = Guid('{f87dacb6-e87e-59b3-8a40-331ea7aa747d}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.RatingControl, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RatingControlAutomationPeer: ...
class IRepeatButtonAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRepeatButtonAutomationPeer'
    _iid_ = Guid('{e42a7cc2-ace8-56eb-9967-9b7fd157c37f}')
class IRepeatButtonAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRepeatButtonAutomationPeerFactory'
    _iid_ = Guid('{0fad55a4-1c62-595e-a189-bb43a219c699}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.RepeatButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RepeatButtonAutomationPeer: ...
class IRepeaterAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRepeaterAutomationPeer'
    _iid_ = Guid('{03f2c315-fb55-54b2-9aad-9723aaf5e2cf}')
class IRepeaterAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRepeaterAutomationPeerFactory'
    _iid_ = Guid('{04526bc7-fa3e-55fe-a314-986e2f196a2f}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.ItemsRepeater, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RepeaterAutomationPeer: ...
class IRichEditBoxAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRichEditBoxAutomationPeer'
    _iid_ = Guid('{193a43f1-129d-57e1-bcf9-ba966bcadacb}')
class IRichEditBoxAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRichEditBoxAutomationPeerFactory'
    _iid_ = Guid('{84f0d84f-54ca-58f2-ac50-d379aab75463}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.RichEditBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RichEditBoxAutomationPeer: ...
class IRichTextBlockAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRichTextBlockAutomationPeer'
    _iid_ = Guid('{7080ff80-b3b8-5d3c-89b5-d989d561192f}')
class IRichTextBlockAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRichTextBlockAutomationPeerFactory'
    _iid_ = Guid('{f8a4485b-2895-5886-8ff6-497e4f1a6e3d}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.RichTextBlock, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RichTextBlockAutomationPeer: ...
class IRichTextBlockOverflowAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRichTextBlockOverflowAutomationPeer'
    _iid_ = Guid('{d0bf83c0-8cfb-5770-b26c-0706e51a9a3b}')
class IRichTextBlockOverflowAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IRichTextBlockOverflowAutomationPeerFactory'
    _iid_ = Guid('{3e7b3ced-bd1f-5851-97a4-1c318f60d641}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.RichTextBlockOverflow, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RichTextBlockOverflowAutomationPeer: ...
class IScrollBarAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IScrollBarAutomationPeer'
    _iid_ = Guid('{028a26c4-05f7-58b2-a81e-a7ac032f756f}')
class IScrollBarAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IScrollBarAutomationPeerFactory'
    _iid_ = Guid('{fc67a9cc-e914-532a-8717-0b383e2157f3}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollBar, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ScrollBarAutomationPeer: ...
class IScrollPresenterAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IScrollPresenterAutomationPeer'
    _iid_ = Guid('{995a6964-607f-5d95-bdf9-1870a5e82a0c}')
class IScrollPresenterAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IScrollPresenterAutomationPeerFactory'
    _iid_ = Guid('{47e29168-5e30-5abc-b844-7d89b5c3eec0}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ScrollPresenterAutomationPeer: ...
class IScrollViewerAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IScrollViewerAutomationPeer'
    _iid_ = Guid('{25394bad-6ca2-5e04-95fa-95412c1f80ac}')
class IScrollViewerAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IScrollViewerAutomationPeerFactory'
    _iid_ = Guid('{3f1578f9-60ec-5f7c-8d11-10c535a75a12}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.ScrollViewer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ScrollViewerAutomationPeer: ...
class ISelectorAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ISelectorAutomationPeer'
    _iid_ = Guid('{4bac62ba-fb33-5f8b-995e-0dd93431294f}')
class ISelectorAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ISelectorAutomationPeerFactory'
    _iid_ = Guid('{d84fe7b9-f5f5-5122-b41c-5575a799d581}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.Selector, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorAutomationPeer: ...
class ISelectorBarItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ISelectorBarItemAutomationPeer'
    _iid_ = Guid('{cdb1078e-1350-56fb-8728-8537b0f35c20}')
class ISelectorBarItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ISelectorBarItemAutomationPeerFactory'
    _iid_ = Guid('{4aab3752-0ddb-5e2d-a614-0b5f7d4efe9d}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.SelectorBarItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorBarItemAutomationPeer: ...
class ISelectorItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ISelectorItemAutomationPeer'
    _iid_ = Guid('{70b85e53-e684-5068-91b7-2d84fea8e9d7}')
class ISelectorItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ISelectorItemAutomationPeerFactory'
    _iid_ = Guid('{2691e85b-dc9c-5ce6-aec9-21c8da9a4ad1}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer: ...
class ISemanticZoomAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ISemanticZoomAutomationPeer'
    _iid_ = Guid('{7d7fbd09-112f-50fd-9654-0474ce760b5d}')
class ISemanticZoomAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ISemanticZoomAutomationPeerFactory'
    _iid_ = Guid('{0572c3c2-87df-55d6-8fcc-032330108cd8}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.SemanticZoom, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.SemanticZoomAutomationPeer: ...
class ISliderAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ISliderAutomationPeer'
    _iid_ = Guid('{c321c95f-c917-5714-9d16-ad706e38926a}')
class ISliderAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ISliderAutomationPeerFactory'
    _iid_ = Guid('{81459943-902a-5fe3-9c75-0f8b11f42658}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Slider, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.SliderAutomationPeer: ...
class ISplitButtonAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ISplitButtonAutomationPeer'
    _iid_ = Guid('{0182661c-0df3-5c7d-8752-547804c4fa44}')
class ISplitButtonAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ISplitButtonAutomationPeerFactory'
    _iid_ = Guid('{e82ddc93-780e-5000-981e-9be10eedeb1f}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.SplitButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.SplitButtonAutomationPeer: ...
class ITabViewAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITabViewAutomationPeer'
    _iid_ = Guid('{efb3f05b-2a25-5266-a1cb-5a0aa451ca32}')
class ITabViewAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITabViewAutomationPeerFactory'
    _iid_ = Guid('{f8d8c7cb-47cc-5da5-bd1a-e2e1ba0fd24d}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.TabView, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TabViewAutomationPeer: ...
class ITabViewItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITabViewItemAutomationPeer'
    _iid_ = Guid('{58afb1c3-a3fd-54a1-be39-328dd8a6f8ec}')
class ITabViewItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITabViewItemAutomationPeerFactory'
    _iid_ = Guid('{00218040-9c0d-5c52-b578-593b809047b3}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.TabViewItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TabViewItemAutomationPeer: ...
class ITeachingTipAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITeachingTipAutomationPeer'
    _iid_ = Guid('{607994ec-a995-5b07-b535-8c913f0bc26c}')
class ITeachingTipAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITeachingTipAutomationPeerFactory'
    _iid_ = Guid('{71a061c1-3d71-5548-98fd-62167f246085}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.TeachingTip, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TeachingTipAutomationPeer: ...
class ITextBlockAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITextBlockAutomationPeer'
    _iid_ = Guid('{29521960-2ef2-5d15-bf6a-cf585ef8a571}')
class ITextBlockAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITextBlockAutomationPeerFactory'
    _iid_ = Guid('{2a04c7bb-6d48-5f8e-9622-54dccdf0a5ca}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.TextBlock, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TextBlockAutomationPeer: ...
class ITextBoxAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITextBoxAutomationPeer'
    _iid_ = Guid('{9e26139a-0618-56fa-9916-8d5edf564735}')
class ITextBoxAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITextBoxAutomationPeerFactory'
    _iid_ = Guid('{1e84ac8f-9974-5be1-b6ea-84f309c8b2b8}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.TextBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TextBoxAutomationPeer: ...
class IThumbAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IThumbAutomationPeer'
    _iid_ = Guid('{b05d6e5b-3586-5157-a497-4f15b87d89eb}')
class IThumbAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IThumbAutomationPeerFactory'
    _iid_ = Guid('{311b414a-7cc8-56d9-b581-149c8bf9d76d}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.Thumb, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ThumbAutomationPeer: ...
class ITimePickerAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITimePickerAutomationPeer'
    _iid_ = Guid('{6309d3bb-3387-5965-acf5-47bfa9b92ed4}')
class ITimePickerAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITimePickerAutomationPeerFactory'
    _iid_ = Guid('{7cdf2f82-7453-5d86-8ee3-60daaf345f47}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.TimePicker, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TimePickerAutomationPeer: ...
class ITimePickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITimePickerFlyoutPresenterAutomationPeer'
    _iid_ = Guid('{2438268a-62e8-5d61-95d0-d36f6b42e652}')
class IToggleButtonAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IToggleButtonAutomationPeer'
    _iid_ = Guid('{637d9b99-bcc2-5e26-b43f-ba6c26af72c3}')
class IToggleButtonAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IToggleButtonAutomationPeerFactory'
    _iid_ = Guid('{2c272096-21e0-5714-9164-1f6a1e0b2181}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.ToggleButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer: ...
class IToggleMenuFlyoutItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IToggleMenuFlyoutItemAutomationPeer'
    _iid_ = Guid('{ea4e4c7e-1f12-56c0-a2a5-b59e9c25b06d}')
class IToggleMenuFlyoutItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IToggleMenuFlyoutItemAutomationPeerFactory'
    _iid_ = Guid('{7789f700-d565-5dc7-8bcc-d459a4c08fd6}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.ToggleMenuFlyoutItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleMenuFlyoutItemAutomationPeer: ...
class IToggleSplitButtonAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IToggleSplitButtonAutomationPeer'
    _iid_ = Guid('{21356952-4c74-5273-b82d-e5ce1bbcd369}')
class IToggleSplitButtonAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IToggleSplitButtonAutomationPeerFactory'
    _iid_ = Guid('{61c214a5-605b-5e98-b85d-e3121d23edaa}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.ToggleSplitButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleSplitButtonAutomationPeer: ...
class IToggleSwitchAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IToggleSwitchAutomationPeer'
    _iid_ = Guid('{927d6091-5070-574f-9833-0ef89a9cbb4b}')
class IToggleSwitchAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IToggleSwitchAutomationPeerFactory'
    _iid_ = Guid('{03f5e3e4-4b61-5dcf-afdc-fd23041a0374}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.ToggleSwitch, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleSwitchAutomationPeer: ...
class ITreeViewItemAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITreeViewItemAutomationPeer'
    _iid_ = Guid('{25b38166-b905-5480-8439-e459a5b77b8c}')
class ITreeViewItemAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITreeViewItemAutomationPeerFactory'
    _iid_ = Guid('{0c993c78-981f-5dcf-93d3-a217ad9acab6}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.TreeViewItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TreeViewItemAutomationPeer: ...
class ITreeViewItemDataAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITreeViewItemDataAutomationPeer'
    _iid_ = Guid('{20f74f77-edfa-5c71-9deb-530dcaf9c11d}')
class ITreeViewItemDataAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITreeViewItemDataAutomationPeerFactory'
    _iid_ = Guid('{07fc8e59-55a2-58ab-8921-91e57ddf119f}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.TreeViewListAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TreeViewItemDataAutomationPeer: ...
class ITreeViewListAutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITreeViewListAutomationPeer'
    _iid_ = Guid('{1ebf0f7f-6111-50a5-8398-89c4fdd0dedb}')
class ITreeViewListAutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ITreeViewListAutomationPeerFactory'
    _iid_ = Guid('{51332d86-c414-5e7d-b57b-e479983c9e5d}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: win32more.Microsoft.UI.Xaml.Controls.TreeViewList, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TreeViewListAutomationPeer: ...
class IWebView2AutomationPeer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IWebView2AutomationPeer'
    _iid_ = Guid('{8e556eca-b000-5e51-810f-7b7d80c39d56}')
class IWebView2AutomationPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.IWebView2AutomationPeerFactory'
    _iid_ = Guid('{68512210-e61e-5b56-a6af-c4fb14677155}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: win32more.Microsoft.UI.Xaml.Controls.WebView2, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.WebView2AutomationPeer: ...
class ImageAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IImageAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ImageAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ImageAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IImageAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Image, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ImageAutomationPeer: ...
class InfoBarAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IInfoBarAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.InfoBarAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.InfoBarAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IInfoBarAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.InfoBar, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.InfoBarAutomationPeer: ...
class ItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ItemAutomationPeer.CreateInstanceWithParentAndItem(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IItemAutomationPeerFactory, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
    @winrt_mixinmethod
    def get_Item(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IItemAutomationPeer) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_ItemsControlAutomationPeer(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IItemAutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer: ...
    @winrt_mixinmethod
    def Realize(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IVirtualizedItemProvider) -> Void: ...
    Item = property(get_Item, None)
    ItemsControlAutomationPeer = property(get_ItemsControlAutomationPeer, None)
class ItemContainerAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IItemContainerAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ItemContainerAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ItemContainerAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IItemContainerAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ItemContainer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemContainerAutomationPeer: ...
    @winrt_mixinmethod
    def get_IsSelected(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_SelectionContainer(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_mixinmethod
    def AddToSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def Select(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def Invoke(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class ItemsControlAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IItemsControlAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IItemsControlAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ItemsControl, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer: ...
    @winrt_mixinmethod
    def CreateItemAutomationPeer(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IItemsControlAutomationPeer, item: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
    @winrt_mixinmethod
    def OnCreateItemAutomationPeer(self: win32more.Microsoft.UI.Xaml.Automation.Peers.IItemsControlAutomationPeerOverrides, item: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
    @winrt_mixinmethod
    def FindItemByProperty(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IItemContainerProvider, startAfter: win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple, automationProperty: win32more.Microsoft.UI.Xaml.Automation.AutomationProperty, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class ItemsViewAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IItemsViewAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ItemsViewAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ItemsViewAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IItemsViewAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ItemsView, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ItemsViewAutomationPeer: ...
    @winrt_mixinmethod
    def get_CanSelectMultiple(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSelectionRequired(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def GetSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionProvider) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    CanSelectMultiple = property(get_CanSelectMultiple, None)
    IsSelectionRequired = property(get_IsSelectionRequired, None)
class ListBoxAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IListBoxAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ListBoxAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ListBoxAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IListBoxAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ListBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListBoxAutomationPeer: ...
class ListBoxItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IListBoxItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ListBoxItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ListBoxItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IListBoxItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ListBoxItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListBoxItemAutomationPeer: ...
class ListBoxItemDataAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IListBoxItemDataAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ListBoxItemDataAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ListBoxItemDataAutomationPeer.CreateInstanceWithParentAndItem(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IListBoxItemDataAutomationPeerFactory, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.ListBoxAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListBoxItemDataAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
class ListPickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IListPickerFlyoutPresenterAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ListPickerFlyoutPresenterAutomationPeer'
class ListViewAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IListViewAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ListViewAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IListViewAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ListView, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewAutomationPeer: ...
class ListViewBaseAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IListViewBaseAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IListViewBaseAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ListViewBase, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer: ...
    @winrt_mixinmethod
    def get_DropEffect(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IDropTargetProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DropEffects(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IDropTargetProvider) -> ReceiveArray[WinRT_String]: ...
    DropEffect = property(get_DropEffect, None)
    DropEffects = property(get_DropEffects, None)
class ListViewBaseHeaderItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IListViewBaseHeaderItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IListViewBaseHeaderItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ListViewBaseHeaderItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer: ...
class ListViewHeaderItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IListViewHeaderItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ListViewHeaderItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewHeaderItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IListViewHeaderItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ListViewHeaderItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewHeaderItemAutomationPeer: ...
class ListViewItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IListViewItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IListViewItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ListViewItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer: ...
class ListViewItemDataAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IListViewItemDataAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ListViewItemDataAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewItemDataAutomationPeer.CreateInstanceWithParentAndItem(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IListViewItemDataAutomationPeerFactory, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewItemDataAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
class LoopingSelectorAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ILoopingSelectorAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.LoopingSelectorAutomationPeer'
    @winrt_mixinmethod
    def get_CanSelectMultiple(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSelectionRequired(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def GetSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionProvider) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    @winrt_mixinmethod
    def FindItemByProperty(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IItemContainerProvider, startAfter: win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple, automationProperty: win32more.Microsoft.UI.Xaml.Automation.AutomationProperty, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_mixinmethod
    def get_HorizontallyScrollable(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_HorizontalScrollPercent(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_HorizontalViewSize(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticallyScrollable(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_VerticalScrollPercent(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalViewSize(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def Scroll(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider, horizontalAmount: win32more.Microsoft.UI.Xaml.Automation.ScrollAmount, verticalAmount: win32more.Microsoft.UI.Xaml.Automation.ScrollAmount) -> Void: ...
    @winrt_mixinmethod
    def SetScrollPercent(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider, horizontalPercent: Double, verticalPercent: Double) -> Void: ...
    CanSelectMultiple = property(get_CanSelectMultiple, None)
    HorizontalScrollPercent = property(get_HorizontalScrollPercent, None)
    HorizontalViewSize = property(get_HorizontalViewSize, None)
    HorizontallyScrollable = property(get_HorizontallyScrollable, None)
    IsSelectionRequired = property(get_IsSelectionRequired, None)
    VerticalScrollPercent = property(get_VerticalScrollPercent, None)
    VerticalViewSize = property(get_VerticalViewSize, None)
    VerticallyScrollable = property(get_VerticallyScrollable, None)
class LoopingSelectorItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ILoopingSelectorItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.LoopingSelectorItemAutomationPeer'
    @winrt_mixinmethod
    def ScrollIntoView(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
    @winrt_mixinmethod
    def get_IsSelected(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_SelectionContainer(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_mixinmethod
    def AddToSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def Select(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class LoopingSelectorItemDataAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ILoopingSelectorItemDataAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.LoopingSelectorItemDataAutomationPeer'
    @winrt_mixinmethod
    def Realize(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IVirtualizedItemProvider) -> Void: ...
class MediaPlayerElementAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IMediaPlayerElementAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.MediaPlayerElementAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.MediaPlayerElementAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IMediaPlayerElementAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.MediaPlayerElement, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.MediaPlayerElementAutomationPeer: ...
class MediaTransportControlsAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IMediaTransportControlsAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.MediaTransportControlsAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.MediaTransportControlsAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IMediaTransportControlsAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.MediaTransportControls, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.MediaTransportControlsAutomationPeer: ...
class MenuBarAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IMenuBarAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.MenuBarAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.MenuBarAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IMenuBarAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.MenuBar, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.MenuBarAutomationPeer: ...
class MenuBarItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IMenuBarItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.MenuBarItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.MenuBarItemAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IMenuBarItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.MenuBarItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.MenuBarItemAutomationPeer: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> win32more.Microsoft.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Invoke(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class MenuFlyoutItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IMenuFlyoutItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.MenuFlyoutItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.MenuFlyoutItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IMenuFlyoutItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.MenuFlyoutItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.MenuFlyoutItemAutomationPeer: ...
    @winrt_mixinmethod
    def Invoke(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
class MenuFlyoutPresenterAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IMenuFlyoutPresenterAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.MenuFlyoutPresenterAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.MenuFlyoutPresenterAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IMenuFlyoutPresenterAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.MenuFlyoutPresenter, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.MenuFlyoutPresenterAutomationPeer: ...
class NavigationViewAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.INavigationViewAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.NavigationViewAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.NavigationViewAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.INavigationViewAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.NavigationView, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.NavigationViewAutomationPeer: ...
class NavigationViewItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.INavigationViewItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.NavigationViewItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.NavigationViewItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.INavigationViewItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.NavigationViewItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.NavigationViewItemAutomationPeer: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> win32more.Microsoft.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class NumberBoxAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.INumberBoxAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.NumberBoxAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.NumberBoxAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.INumberBoxAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.NumberBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.NumberBoxAutomationPeer: ...
class PasswordBoxAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IPasswordBoxAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.PasswordBoxAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.PasswordBoxAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IPasswordBoxAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.PasswordBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.PasswordBoxAutomationPeer: ...
class PatternInterface(Enum, Int32):
    Invoke = 0
    Selection = 1
    Value = 2
    RangeValue = 3
    Scroll = 4
    ScrollItem = 5
    ExpandCollapse = 6
    Grid = 7
    GridItem = 8
    MultipleView = 9
    Window = 10
    SelectionItem = 11
    Dock = 12
    Table = 13
    TableItem = 14
    Toggle = 15
    Transform = 16
    Text = 17
    ItemContainer = 18
    VirtualizedItem = 19
    Text2 = 20
    TextChild = 21
    TextRange = 22
    Annotation = 23
    Drag = 24
    DropTarget = 25
    ObjectModel = 26
    Spreadsheet = 27
    SpreadsheetItem = 28
    Styles = 29
    Transform2 = 30
    SynchronizedInput = 31
    TextEdit = 32
    CustomNavigation = 33
class PersonPictureAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IPersonPictureAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.PersonPictureAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.PersonPictureAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IPersonPictureAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.PersonPicture, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.PersonPictureAutomationPeer: ...
class PickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IPickerFlyoutPresenterAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.PickerFlyoutPresenterAutomationPeer'
class PipsPagerAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IPipsPagerAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.PipsPagerAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.PipsPagerAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IPipsPagerAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.PipsPager, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.PipsPagerAutomationPeer: ...
class PivotAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IPivotAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.PivotAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.PivotAutomationPeer.CreateInstanceWithOwner(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IPivotAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Pivot) -> win32more.Microsoft.UI.Xaml.Automation.Peers.PivotAutomationPeer: ...
    @winrt_mixinmethod
    def get_CanSelectMultiple(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSelectionRequired(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def GetSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionProvider) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    @winrt_mixinmethod
    def get_HorizontallyScrollable(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_HorizontalScrollPercent(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_HorizontalViewSize(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticallyScrollable(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_VerticalScrollPercent(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalViewSize(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def Scroll(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider, horizontalAmount: win32more.Microsoft.UI.Xaml.Automation.ScrollAmount, verticalAmount: win32more.Microsoft.UI.Xaml.Automation.ScrollAmount) -> Void: ...
    @winrt_mixinmethod
    def SetScrollPercent(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider, horizontalPercent: Double, verticalPercent: Double) -> Void: ...
    CanSelectMultiple = property(get_CanSelectMultiple, None)
    HorizontalScrollPercent = property(get_HorizontalScrollPercent, None)
    HorizontalViewSize = property(get_HorizontalViewSize, None)
    HorizontallyScrollable = property(get_HorizontallyScrollable, None)
    IsSelectionRequired = property(get_IsSelectionRequired, None)
    VerticalScrollPercent = property(get_VerticalScrollPercent, None)
    VerticalViewSize = property(get_VerticalViewSize, None)
    VerticallyScrollable = property(get_VerticallyScrollable, None)
class PivotItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IPivotItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.PivotItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.PivotItemAutomationPeer.CreateInstanceWithOwner(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IPivotItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.PivotItem) -> win32more.Microsoft.UI.Xaml.Automation.Peers.PivotItemAutomationPeer: ...
class PivotItemDataAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ItemAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IPivotItemDataAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.PivotItemDataAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.PivotItemDataAutomationPeer.CreateInstanceWithParentAndItem(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IPivotItemDataAutomationPeerFactory, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.PivotAutomationPeer) -> win32more.Microsoft.UI.Xaml.Automation.Peers.PivotItemDataAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
    @winrt_mixinmethod
    def get_IsSelected(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_SelectionContainer(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_mixinmethod
    def AddToSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def Select(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def Realize(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IVirtualizedItemProvider) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class ProgressBarAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IProgressBarAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ProgressBarAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ProgressBarAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IProgressBarAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ProgressBar, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ProgressBarAutomationPeer: ...
class ProgressRingAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IProgressRingAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ProgressRingAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ProgressRingAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IProgressRingAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ProgressRing, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ProgressRingAutomationPeer: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_LargeChange(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def get_Maximum(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def get_Minimum(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def get_SmallChange(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def SetValue(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider, value: Double) -> Void: ...
    IsReadOnly = property(get_IsReadOnly, None)
    LargeChange = property(get_LargeChange, None)
    Maximum = property(get_Maximum, None)
    Minimum = property(get_Minimum, None)
    SmallChange = property(get_SmallChange, None)
    Value = property(get_Value, None)
class RadioButtonAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IRadioButtonAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.RadioButtonAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.RadioButtonAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IRadioButtonAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.RadioButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RadioButtonAutomationPeer: ...
    @winrt_mixinmethod
    def get_IsSelected(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_SelectionContainer(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_mixinmethod
    def AddToSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def Select(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class RadioButtonsAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IRadioButtonsAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.RadioButtonsAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.RadioButtonsAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IRadioButtonsAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.RadioButtons, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RadioButtonsAutomationPeer: ...
class RangeBaseAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IRangeBaseAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IRangeBaseAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.RangeBase, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_LargeChange(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def get_Maximum(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def get_Minimum(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def get_SmallChange(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def SetValue(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider, value: Double) -> Void: ...
    IsReadOnly = property(get_IsReadOnly, None)
    LargeChange = property(get_LargeChange, None)
    Maximum = property(get_Maximum, None)
    Minimum = property(get_Minimum, None)
    SmallChange = property(get_SmallChange, None)
    Value = property(get_Value, None)
class RatingControlAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IRatingControlAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.RatingControlAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.RatingControlAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IRatingControlAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.RatingControl, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RatingControlAutomationPeer: ...
class RawElementProviderRuntimeId(Structure):
    Part1: UInt32
    Part2: UInt32
class RepeatButtonAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IRepeatButtonAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.RepeatButtonAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.RepeatButtonAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IRepeatButtonAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.RepeatButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RepeatButtonAutomationPeer: ...
    @winrt_mixinmethod
    def Invoke(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
class RepeaterAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IRepeaterAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.RepeaterAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.RepeaterAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IRepeaterAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ItemsRepeater, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RepeaterAutomationPeer: ...
class RichEditBoxAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IRichEditBoxAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.RichEditBoxAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.RichEditBoxAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IRichEditBoxAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.RichEditBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RichEditBoxAutomationPeer: ...
class RichTextBlockAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IRichTextBlockAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.RichTextBlockAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.RichTextBlockAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IRichTextBlockAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.RichTextBlock, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RichTextBlockAutomationPeer: ...
class RichTextBlockOverflowAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IRichTextBlockOverflowAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.RichTextBlockOverflowAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.RichTextBlockOverflowAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IRichTextBlockOverflowAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.RichTextBlockOverflow, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.RichTextBlockOverflowAutomationPeer: ...
class ScrollBarAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IScrollBarAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ScrollBarAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ScrollBarAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IScrollBarAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollBar, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ScrollBarAutomationPeer: ...
class ScrollPresenterAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IScrollPresenterAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ScrollPresenterAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ScrollPresenterAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IScrollPresenterAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.ScrollPresenter, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ScrollPresenterAutomationPeer: ...
class ScrollViewerAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IScrollViewerAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ScrollViewerAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ScrollViewerAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IScrollViewerAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ScrollViewer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ScrollViewerAutomationPeer: ...
    @winrt_mixinmethod
    def get_HorizontallyScrollable(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_HorizontalScrollPercent(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_HorizontalViewSize(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticallyScrollable(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_VerticalScrollPercent(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalViewSize(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def Scroll(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider, horizontalAmount: win32more.Microsoft.UI.Xaml.Automation.ScrollAmount, verticalAmount: win32more.Microsoft.UI.Xaml.Automation.ScrollAmount) -> Void: ...
    @winrt_mixinmethod
    def SetScrollPercent(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IScrollProvider, horizontalPercent: Double, verticalPercent: Double) -> Void: ...
    HorizontalScrollPercent = property(get_HorizontalScrollPercent, None)
    HorizontalViewSize = property(get_HorizontalViewSize, None)
    HorizontallyScrollable = property(get_HorizontallyScrollable, None)
    VerticalScrollPercent = property(get_VerticalScrollPercent, None)
    VerticalViewSize = property(get_VerticalViewSize, None)
    VerticallyScrollable = property(get_VerticallyScrollable, None)
class SelectorAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ISelectorAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.SelectorAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ISelectorAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.Selector, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorAutomationPeer: ...
    @winrt_mixinmethod
    def get_CanSelectMultiple(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSelectionRequired(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def GetSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionProvider) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    CanSelectMultiple = property(get_CanSelectMultiple, None)
    IsSelectionRequired = property(get_IsSelectionRequired, None)
class SelectorBarItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ItemContainerAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ISelectorBarItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.SelectorBarItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorBarItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ISelectorBarItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.SelectorBarItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorBarItemAutomationPeer: ...
class SelectorItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ItemAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ISelectorItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer.CreateInstanceWithParentAndItem(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ISelectorItemAutomationPeerFactory, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer: ...
    @winrt_mixinmethod
    def get_IsSelected(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_SelectionContainer(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_mixinmethod
    def AddToSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromSelection(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def Select(self: win32more.Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class SemanticZoomAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ISemanticZoomAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.SemanticZoomAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.SemanticZoomAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ISemanticZoomAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.SemanticZoom, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.SemanticZoomAutomationPeer: ...
    @winrt_mixinmethod
    def get_ToggleState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IToggleProvider) -> win32more.Microsoft.UI.Xaml.Automation.ToggleState: ...
    @winrt_mixinmethod
    def Toggle(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IToggleProvider) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class SliderAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ISliderAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.SliderAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.SliderAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ISliderAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Slider, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.SliderAutomationPeer: ...
class SplitButtonAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ISplitButtonAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.SplitButtonAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.SplitButtonAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ISplitButtonAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.SplitButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.SplitButtonAutomationPeer: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> win32more.Microsoft.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Invoke(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class TabViewAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ITabViewAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.TabViewAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.TabViewAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ITabViewAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.TabView, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TabViewAutomationPeer: ...
class TabViewItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ITabViewItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.TabViewItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.TabViewItemAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ITabViewItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.TabViewItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TabViewItemAutomationPeer: ...
class TeachingTipAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ITeachingTipAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.TeachingTipAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.TeachingTipAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ITeachingTipAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.TeachingTip, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TeachingTipAutomationPeer: ...
class TextBlockAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ITextBlockAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.TextBlockAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.TextBlockAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ITextBlockAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.TextBlock, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TextBlockAutomationPeer: ...
class TextBoxAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ITextBoxAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.TextBoxAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.TextBoxAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ITextBoxAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.TextBox, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TextBoxAutomationPeer: ...
class ThumbAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IThumbAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ThumbAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ThumbAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IThumbAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.Thumb, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ThumbAutomationPeer: ...
class TimePickerAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ITimePickerAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.TimePickerAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.TimePickerAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ITimePickerAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.TimePicker, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TimePickerAutomationPeer: ...
class TimePickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ITimePickerFlyoutPresenterAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.TimePickerFlyoutPresenterAutomationPeer'
class ToggleButtonAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IToggleButtonAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IToggleButtonAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.Primitives.ToggleButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer: ...
    @winrt_mixinmethod
    def get_ToggleState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IToggleProvider) -> win32more.Microsoft.UI.Xaml.Automation.ToggleState: ...
    @winrt_mixinmethod
    def Toggle(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IToggleProvider) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class ToggleMenuFlyoutItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IToggleMenuFlyoutItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ToggleMenuFlyoutItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleMenuFlyoutItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IToggleMenuFlyoutItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ToggleMenuFlyoutItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleMenuFlyoutItemAutomationPeer: ...
    @winrt_mixinmethod
    def get_ToggleState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IToggleProvider) -> win32more.Microsoft.UI.Xaml.Automation.ToggleState: ...
    @winrt_mixinmethod
    def Toggle(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IToggleProvider) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class ToggleSplitButtonAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IToggleSplitButtonAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ToggleSplitButtonAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleSplitButtonAutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IToggleSplitButtonAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ToggleSplitButton, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleSplitButtonAutomationPeer: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> win32more.Microsoft.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def get_ToggleState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IToggleProvider) -> win32more.Microsoft.UI.Xaml.Automation.ToggleState: ...
    @winrt_mixinmethod
    def Toggle(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IToggleProvider) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
    ToggleState = property(get_ToggleState, None)
class ToggleSwitchAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IToggleSwitchAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.ToggleSwitchAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleSwitchAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IToggleSwitchAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.ToggleSwitch, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.ToggleSwitchAutomationPeer: ...
    @winrt_mixinmethod
    def get_ToggleState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IToggleProvider) -> win32more.Microsoft.UI.Xaml.Automation.ToggleState: ...
    @winrt_mixinmethod
    def Toggle(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IToggleProvider) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class TreeViewItemAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ITreeViewItemAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.TreeViewItemAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.TreeViewItemAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ITreeViewItemAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.TreeViewItem, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TreeViewItemAutomationPeer: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> win32more.Microsoft.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class TreeViewItemDataAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ItemAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ITreeViewItemDataAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.TreeViewItemDataAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.TreeViewItemDataAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ITreeViewItemDataAutomationPeerFactory, item: win32more.Windows.Win32.System.WinRT.IInspectable, parent: win32more.Microsoft.UI.Xaml.Automation.Peers.TreeViewListAutomationPeer, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TreeViewItemDataAutomationPeer: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> win32more.Microsoft.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: win32more.Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class TreeViewListAutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.ListViewAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.ITreeViewListAutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.TreeViewListAutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.TreeViewListAutomationPeer.CreateInstanceWithOwner(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.ITreeViewListAutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.TreeViewList, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.TreeViewListAutomationPeer: ...
class WebView2AutomationPeer(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Peers.IWebView2AutomationPeer
    _classid_ = 'Microsoft.UI.Xaml.Automation.Peers.WebView2AutomationPeer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Automation.Peers.WebView2AutomationPeer.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Automation.Peers.IWebView2AutomationPeerFactory, owner: win32more.Microsoft.UI.Xaml.Controls.WebView2, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Automation.Peers.WebView2AutomationPeer: ...


make_ready(__name__)
