from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.UI.Xaml
import Windows.UI.Xaml.Automation
import Windows.UI.Xaml.Automation.Peers
import Windows.UI.Xaml.Automation.Provider
import Windows.UI.Xaml.Controls
import Windows.UI.Xaml.Controls.Primitives
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AccessibilityView = Int32
AccessibilityView_Raw: AccessibilityView = 0
AccessibilityView_Control: AccessibilityView = 1
AccessibilityView_Content: AccessibilityView = 2
class AppBarAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IAppBarAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.AppBarAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IAppBarAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.AppBar, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.AppBarAutomationPeer: ...
    @winrt_mixinmethod
    def get_ToggleState(self: Windows.UI.Xaml.Automation.Provider.IToggleProvider) -> Windows.UI.Xaml.Automation.ToggleState: ...
    @winrt_mixinmethod
    def Toggle(self: Windows.UI.Xaml.Automation.Provider.IToggleProvider) -> Void: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def get_IsModal(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTopmost(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_Maximizable(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_Minimizable(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_InteractionState(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Windows.UI.Xaml.Automation.WindowInteractionState: ...
    @winrt_mixinmethod
    def get_VisualState(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Windows.UI.Xaml.Automation.WindowVisualState: ...
    @winrt_mixinmethod
    def Close(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Void: ...
    @winrt_mixinmethod
    def SetVisualState(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider, state: Windows.UI.Xaml.Automation.WindowVisualState) -> Void: ...
    @winrt_mixinmethod
    def WaitForInputIdle(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider, milliseconds: Int32) -> Boolean: ...
    ToggleState = property(get_ToggleState, None)
    ExpandCollapseState = property(get_ExpandCollapseState, None)
    IsModal = property(get_IsModal, None)
    IsTopmost = property(get_IsTopmost, None)
    Maximizable = property(get_Maximizable, None)
    Minimizable = property(get_Minimizable, None)
    InteractionState = property(get_InteractionState, None)
    VisualState = property(get_VisualState, None)
class AppBarButtonAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ButtonAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IAppBarButtonAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.AppBarButtonAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IAppBarButtonAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.AppBarButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.AppBarButtonAutomationPeer: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class AppBarToggleButtonAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IAppBarToggleButtonAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.AppBarToggleButtonAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IAppBarToggleButtonAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.AppBarToggleButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.AppBarToggleButtonAutomationPeer: ...
class AutoSuggestBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IAutoSuggestBoxAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.AutoSuggestBoxAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IAutoSuggestBoxAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.AutoSuggestBox) -> Windows.UI.Xaml.Automation.Peers.AutoSuggestBoxAutomationPeer: ...
    @winrt_mixinmethod
    def Invoke(self: Windows.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
AutomationControlType = Int32
AutomationControlType_Button: AutomationControlType = 0
AutomationControlType_Calendar: AutomationControlType = 1
AutomationControlType_CheckBox: AutomationControlType = 2
AutomationControlType_ComboBox: AutomationControlType = 3
AutomationControlType_Edit: AutomationControlType = 4
AutomationControlType_Hyperlink: AutomationControlType = 5
AutomationControlType_Image: AutomationControlType = 6
AutomationControlType_ListItem: AutomationControlType = 7
AutomationControlType_List: AutomationControlType = 8
AutomationControlType_Menu: AutomationControlType = 9
AutomationControlType_MenuBar: AutomationControlType = 10
AutomationControlType_MenuItem: AutomationControlType = 11
AutomationControlType_ProgressBar: AutomationControlType = 12
AutomationControlType_RadioButton: AutomationControlType = 13
AutomationControlType_ScrollBar: AutomationControlType = 14
AutomationControlType_Slider: AutomationControlType = 15
AutomationControlType_Spinner: AutomationControlType = 16
AutomationControlType_StatusBar: AutomationControlType = 17
AutomationControlType_Tab: AutomationControlType = 18
AutomationControlType_TabItem: AutomationControlType = 19
AutomationControlType_Text: AutomationControlType = 20
AutomationControlType_ToolBar: AutomationControlType = 21
AutomationControlType_ToolTip: AutomationControlType = 22
AutomationControlType_Tree: AutomationControlType = 23
AutomationControlType_TreeItem: AutomationControlType = 24
AutomationControlType_Custom: AutomationControlType = 25
AutomationControlType_Group: AutomationControlType = 26
AutomationControlType_Thumb: AutomationControlType = 27
AutomationControlType_DataGrid: AutomationControlType = 28
AutomationControlType_DataItem: AutomationControlType = 29
AutomationControlType_Document: AutomationControlType = 30
AutomationControlType_SplitButton: AutomationControlType = 31
AutomationControlType_Window: AutomationControlType = 32
AutomationControlType_Pane: AutomationControlType = 33
AutomationControlType_Header: AutomationControlType = 34
AutomationControlType_HeaderItem: AutomationControlType = 35
AutomationControlType_Table: AutomationControlType = 36
AutomationControlType_TitleBar: AutomationControlType = 37
AutomationControlType_Separator: AutomationControlType = 38
AutomationControlType_SemanticZoom: AutomationControlType = 39
AutomationControlType_AppBar: AutomationControlType = 40
AutomationEvents = Int32
AutomationEvents_ToolTipOpened: AutomationEvents = 0
AutomationEvents_ToolTipClosed: AutomationEvents = 1
AutomationEvents_MenuOpened: AutomationEvents = 2
AutomationEvents_MenuClosed: AutomationEvents = 3
AutomationEvents_AutomationFocusChanged: AutomationEvents = 4
AutomationEvents_InvokePatternOnInvoked: AutomationEvents = 5
AutomationEvents_SelectionItemPatternOnElementAddedToSelection: AutomationEvents = 6
AutomationEvents_SelectionItemPatternOnElementRemovedFromSelection: AutomationEvents = 7
AutomationEvents_SelectionItemPatternOnElementSelected: AutomationEvents = 8
AutomationEvents_SelectionPatternOnInvalidated: AutomationEvents = 9
AutomationEvents_TextPatternOnTextSelectionChanged: AutomationEvents = 10
AutomationEvents_TextPatternOnTextChanged: AutomationEvents = 11
AutomationEvents_AsyncContentLoaded: AutomationEvents = 12
AutomationEvents_PropertyChanged: AutomationEvents = 13
AutomationEvents_StructureChanged: AutomationEvents = 14
AutomationEvents_DragStart: AutomationEvents = 15
AutomationEvents_DragCancel: AutomationEvents = 16
AutomationEvents_DragComplete: AutomationEvents = 17
AutomationEvents_DragEnter: AutomationEvents = 18
AutomationEvents_DragLeave: AutomationEvents = 19
AutomationEvents_Dropped: AutomationEvents = 20
AutomationEvents_LiveRegionChanged: AutomationEvents = 21
AutomationEvents_InputReachedTarget: AutomationEvents = 22
AutomationEvents_InputReachedOtherElement: AutomationEvents = 23
AutomationEvents_InputDiscarded: AutomationEvents = 24
AutomationEvents_WindowClosed: AutomationEvents = 25
AutomationEvents_WindowOpened: AutomationEvents = 26
AutomationEvents_ConversionTargetChanged: AutomationEvents = 27
AutomationEvents_TextEditTextChanged: AutomationEvents = 28
AutomationEvents_LayoutInvalidated: AutomationEvents = 29
AutomationHeadingLevel = Int32
AutomationHeadingLevel_None: AutomationHeadingLevel = 0
AutomationHeadingLevel_Level1: AutomationHeadingLevel = 1
AutomationHeadingLevel_Level2: AutomationHeadingLevel = 2
AutomationHeadingLevel_Level3: AutomationHeadingLevel = 3
AutomationHeadingLevel_Level4: AutomationHeadingLevel = 4
AutomationHeadingLevel_Level5: AutomationHeadingLevel = 5
AutomationHeadingLevel_Level6: AutomationHeadingLevel = 6
AutomationHeadingLevel_Level7: AutomationHeadingLevel = 7
AutomationHeadingLevel_Level8: AutomationHeadingLevel = 8
AutomationHeadingLevel_Level9: AutomationHeadingLevel = 9
AutomationLandmarkType = Int32
AutomationLandmarkType_None: AutomationLandmarkType = 0
AutomationLandmarkType_Custom: AutomationLandmarkType = 1
AutomationLandmarkType_Form: AutomationLandmarkType = 2
AutomationLandmarkType_Main: AutomationLandmarkType = 3
AutomationLandmarkType_Navigation: AutomationLandmarkType = 4
AutomationLandmarkType_Search: AutomationLandmarkType = 5
AutomationLiveSetting = Int32
AutomationLiveSetting_Off: AutomationLiveSetting = 0
AutomationLiveSetting_Polite: AutomationLiveSetting = 1
AutomationLiveSetting_Assertive: AutomationLiveSetting = 2
AutomationNavigationDirection = Int32
AutomationNavigationDirection_Parent: AutomationNavigationDirection = 0
AutomationNavigationDirection_NextSibling: AutomationNavigationDirection = 1
AutomationNavigationDirection_PreviousSibling: AutomationNavigationDirection = 2
AutomationNavigationDirection_FirstChild: AutomationNavigationDirection = 3
AutomationNavigationDirection_LastChild: AutomationNavigationDirection = 4
AutomationNotificationKind = Int32
AutomationNotificationKind_ItemAdded: AutomationNotificationKind = 0
AutomationNotificationKind_ItemRemoved: AutomationNotificationKind = 1
AutomationNotificationKind_ActionCompleted: AutomationNotificationKind = 2
AutomationNotificationKind_ActionAborted: AutomationNotificationKind = 3
AutomationNotificationKind_Other: AutomationNotificationKind = 4
AutomationNotificationProcessing = Int32
AutomationNotificationProcessing_ImportantAll: AutomationNotificationProcessing = 0
AutomationNotificationProcessing_ImportantMostRecent: AutomationNotificationProcessing = 1
AutomationNotificationProcessing_All: AutomationNotificationProcessing = 2
AutomationNotificationProcessing_MostRecent: AutomationNotificationProcessing = 3
AutomationNotificationProcessing_CurrentThenMostRecent: AutomationNotificationProcessing = 4
AutomationOrientation = Int32
AutomationOrientation_None: AutomationOrientation = 0
AutomationOrientation_Horizontal: AutomationOrientation = 1
AutomationOrientation_Vertical: AutomationOrientation = 2
class AutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Automation.Peers.IAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.AutomationPeer'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Automation.Peers.IAutomationPeerFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def get_EventsSource(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def put_EventsSource(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer, value: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_mixinmethod
    def GetPattern(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer, patternInterface: Windows.UI.Xaml.Automation.Peers.PatternInterface) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def RaiseAutomationEvent(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer, eventId: Windows.UI.Xaml.Automation.Peers.AutomationEvents) -> Void: ...
    @winrt_mixinmethod
    def RaisePropertyChangedEvent(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer, automationProperty: Windows.UI.Xaml.Automation.AutomationProperty, oldValue: Windows.Win32.System.WinRT.IInspectable_head, newValue: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def GetAcceleratorKey(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetAccessKey(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetAutomationControlType(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Windows.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_mixinmethod
    def GetAutomationId(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetBoundingRectangle(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def GetChildren(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def GetClassName(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetClickablePoint(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def GetHelpText(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetItemStatus(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetItemType(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLabeledBy(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def GetLocalizedControlType(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetName(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetOrientation(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Windows.UI.Xaml.Automation.Peers.AutomationOrientation: ...
    @winrt_mixinmethod
    def HasKeyboardFocus(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsContentElement(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsControlElement(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsEnabled(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsKeyboardFocusable(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsOffscreen(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsPassword(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def IsRequiredForForm(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Boolean: ...
    @winrt_mixinmethod
    def SetFocus(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Void: ...
    @winrt_mixinmethod
    def GetParent(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def InvalidatePeer(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Void: ...
    @winrt_mixinmethod
    def GetPeerFromPoint(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer, point: Windows.Foundation.Point) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def GetLiveSetting(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer) -> Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_mixinmethod
    def Navigate(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer3, direction: Windows.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def GetElementFromPoint(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer3, pointInWindowCoordinates: Windows.Foundation.Point) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def GetFocusedElement(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer3) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def ShowContextMenu(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer3) -> Void: ...
    @winrt_mixinmethod
    def GetControlledPeers(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer3) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def GetAnnotations(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer3) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation]: ...
    @winrt_mixinmethod
    def SetParent(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer3, peer: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_mixinmethod
    def RaiseTextEditTextChangedEvent(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer3, automationTextEditChangeType: Windows.UI.Xaml.Automation.AutomationTextEditChangeType, changedData: Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_mixinmethod
    def GetPositionInSet(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer3) -> Int32: ...
    @winrt_mixinmethod
    def GetSizeOfSet(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer3) -> Int32: ...
    @winrt_mixinmethod
    def GetLevel(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer3) -> Int32: ...
    @winrt_mixinmethod
    def RaiseStructureChangedEvent(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer3, structureChangeType: Windows.UI.Xaml.Automation.Peers.AutomationStructureChangeType, child: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_mixinmethod
    def GetLandmarkType(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer4) -> Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_mixinmethod
    def GetLocalizedLandmarkType(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer4) -> WinRT_String: ...
    @winrt_mixinmethod
    def IsPeripheral(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer5) -> Boolean: ...
    @winrt_mixinmethod
    def IsDataValidForForm(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer5) -> Boolean: ...
    @winrt_mixinmethod
    def GetFullDescription(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer5) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetCulture(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer6) -> Int32: ...
    @winrt_mixinmethod
    def RaiseNotificationEvent(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer7, notificationKind: Windows.UI.Xaml.Automation.Peers.AutomationNotificationKind, notificationProcessing: Windows.UI.Xaml.Automation.Peers.AutomationNotificationProcessing, displayString: WinRT_String, activityId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def GetHeadingLevel(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer8) -> Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_mixinmethod
    def IsDialog(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeer9) -> Boolean: ...
    @winrt_mixinmethod
    def PeerFromProvider(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerProtected, provider: Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def ProviderFromPeer(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerProtected, peer: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_mixinmethod
    def GetPatternCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides, patternInterface: Windows.UI.Xaml.Automation.Peers.PatternInterface) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def GetAcceleratorKeyCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetAccessKeyCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetAutomationControlTypeCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Windows.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_mixinmethod
    def GetAutomationIdCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetBoundingRectangleCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def GetChildrenCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def GetClassNameCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetClickablePointCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def GetHelpTextCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetItemStatusCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetItemTypeCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetLabeledByCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def GetLocalizedControlTypeCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetNameCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetOrientationCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Windows.UI.Xaml.Automation.Peers.AutomationOrientation: ...
    @winrt_mixinmethod
    def HasKeyboardFocusCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsContentElementCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsControlElementCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsEnabledCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsKeyboardFocusableCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsOffscreenCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsPasswordCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def IsRequiredForFormCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Boolean: ...
    @winrt_mixinmethod
    def SetFocusCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Void: ...
    @winrt_mixinmethod
    def GetPeerFromPointCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides, point: Windows.Foundation.Point) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def GetLiveSettingCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides) -> Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_mixinmethod
    def ShowContextMenuCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides2) -> Void: ...
    @winrt_mixinmethod
    def GetControlledPeersCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides2) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def NavigateCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides3, direction: Windows.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def GetElementFromPointCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides3, pointInWindowCoordinates: Windows.Foundation.Point) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def GetFocusedElementCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides3) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def GetAnnotationsCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides3) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation]: ...
    @winrt_mixinmethod
    def GetPositionInSetCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides3) -> Int32: ...
    @winrt_mixinmethod
    def GetSizeOfSetCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides3) -> Int32: ...
    @winrt_mixinmethod
    def GetLevelCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides3) -> Int32: ...
    @winrt_mixinmethod
    def GetLandmarkTypeCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides4) -> Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_mixinmethod
    def GetLocalizedLandmarkTypeCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides4) -> WinRT_String: ...
    @winrt_mixinmethod
    def IsPeripheralCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides5) -> Boolean: ...
    @winrt_mixinmethod
    def IsDataValidForFormCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides5) -> Boolean: ...
    @winrt_mixinmethod
    def GetFullDescriptionCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides5) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetDescribedByCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides5) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def GetFlowsToCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides5) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def GetFlowsFromCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides5) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_mixinmethod
    def GetCultureCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides6) -> Int32: ...
    @winrt_mixinmethod
    def GetHeadingLevelCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides8) -> Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_mixinmethod
    def IsDialogCore(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides9) -> Boolean: ...
    @winrt_classmethod
    def GenerateRawElementProviderRuntimeId(cls: Windows.UI.Xaml.Automation.Peers.IAutomationPeerStatics3) -> Windows.UI.Xaml.Automation.Peers.RawElementProviderRuntimeId: ...
    @winrt_classmethod
    def ListenerExists(cls: Windows.UI.Xaml.Automation.Peers.IAutomationPeerStatics, eventId: Windows.UI.Xaml.Automation.Peers.AutomationEvents) -> Boolean: ...
    EventsSource = property(get_EventsSource, put_EventsSource)
class _AutomationPeerAnnotation_Meta_(ComPtr.__class__):
    pass
class AutomationPeerAnnotation(ComPtr, metaclass=_AutomationPeerAnnotation_Meta_):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Automation.Peers.IAutomationPeerAnnotation
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation: ...
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Automation.Peers.IAutomationPeerAnnotationFactory, type: Windows.UI.Xaml.Automation.AnnotationType) -> Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation: ...
    @winrt_factorymethod
    def CreateWithPeerParameter(cls: Windows.UI.Xaml.Automation.Peers.IAutomationPeerAnnotationFactory, type: Windows.UI.Xaml.Automation.AnnotationType, peer: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerAnnotation) -> Windows.UI.Xaml.Automation.AnnotationType: ...
    @winrt_mixinmethod
    def put_Type(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerAnnotation, value: Windows.UI.Xaml.Automation.AnnotationType) -> Void: ...
    @winrt_mixinmethod
    def get_Peer(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerAnnotation) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_mixinmethod
    def put_Peer(self: Windows.UI.Xaml.Automation.Peers.IAutomationPeerAnnotation, value: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_classmethod
    def get_TypeProperty(cls: Windows.UI.Xaml.Automation.Peers.IAutomationPeerAnnotationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PeerProperty(cls: Windows.UI.Xaml.Automation.Peers.IAutomationPeerAnnotationStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Type = property(get_Type, put_Type)
    Peer = property(get_Peer, put_Peer)
    _AutomationPeerAnnotation_Meta_.TypeProperty = property(get_TypeProperty.__wrapped__, None)
    _AutomationPeerAnnotation_Meta_.PeerProperty = property(get_PeerProperty.__wrapped__, None)
AutomationStructureChangeType = Int32
AutomationStructureChangeType_ChildAdded: AutomationStructureChangeType = 0
AutomationStructureChangeType_ChildRemoved: AutomationStructureChangeType = 1
AutomationStructureChangeType_ChildrenInvalidated: AutomationStructureChangeType = 2
AutomationStructureChangeType_ChildrenBulkAdded: AutomationStructureChangeType = 3
AutomationStructureChangeType_ChildrenBulkRemoved: AutomationStructureChangeType = 4
AutomationStructureChangeType_ChildrenReordered: AutomationStructureChangeType = 5
class ButtonAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IButtonAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ButtonAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IButtonAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Button, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ButtonAutomationPeer: ...
    @winrt_mixinmethod
    def Invoke(self: Windows.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
class ButtonBaseAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IButtonBaseAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IButtonBaseAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Primitives.ButtonBase, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer: ...
class CalendarDatePickerAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ICalendarDatePickerAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.CalendarDatePickerAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.ICalendarDatePickerAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.CalendarDatePicker, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.CalendarDatePickerAutomationPeer: ...
    @winrt_mixinmethod
    def Invoke(self: Windows.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: Windows.UI.Xaml.Automation.Provider.IValueProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.UI.Xaml.Automation.Provider.IValueProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetValue(self: Windows.UI.Xaml.Automation.Provider.IValueProvider, value: WinRT_String) -> Void: ...
    IsReadOnly = property(get_IsReadOnly, None)
    Value = property(get_Value, None)
class CaptureElementAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ICaptureElementAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.CaptureElementAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.ICaptureElementAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.CaptureElement, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.CaptureElementAutomationPeer: ...
class CheckBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ICheckBoxAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.CheckBoxAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.ICheckBoxAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.CheckBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.CheckBoxAutomationPeer: ...
class ColorPickerSliderAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SliderAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IColorPickerSliderAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ColorPickerSliderAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IColorPickerSliderAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Primitives.ColorPickerSlider, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ColorPickerSliderAutomationPeer: ...
class ColorSpectrumAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IColorSpectrumAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ColorSpectrumAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IColorSpectrumAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Primitives.ColorSpectrum, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ColorSpectrumAutomationPeer: ...
class ComboBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IComboBoxAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ComboBoxAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IComboBoxAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ComboBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ComboBoxAutomationPeer: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: Windows.UI.Xaml.Automation.Provider.IValueProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.UI.Xaml.Automation.Provider.IValueProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetValue(self: Windows.UI.Xaml.Automation.Provider.IValueProvider, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def get_IsModal(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTopmost(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_Maximizable(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_Minimizable(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_InteractionState(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Windows.UI.Xaml.Automation.WindowInteractionState: ...
    @winrt_mixinmethod
    def get_VisualState(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Windows.UI.Xaml.Automation.WindowVisualState: ...
    @winrt_mixinmethod
    def Close(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Void: ...
    @winrt_mixinmethod
    def SetVisualState(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider, state: Windows.UI.Xaml.Automation.WindowVisualState) -> Void: ...
    @winrt_mixinmethod
    def WaitForInputIdle(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider, milliseconds: Int32) -> Boolean: ...
    IsReadOnly = property(get_IsReadOnly, None)
    Value = property(get_Value, None)
    ExpandCollapseState = property(get_ExpandCollapseState, None)
    IsModal = property(get_IsModal, None)
    IsTopmost = property(get_IsTopmost, None)
    Maximizable = property(get_Maximizable, None)
    Minimizable = property(get_Minimizable, None)
    InteractionState = property(get_InteractionState, None)
    VisualState = property(get_VisualState, None)
class ComboBoxItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IComboBoxItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ComboBoxItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IComboBoxItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ComboBoxItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ComboBoxItemAutomationPeer: ...
class ComboBoxItemDataAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IComboBoxItemDataAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ComboBoxItemDataAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: Windows.UI.Xaml.Automation.Peers.IComboBoxItemDataAutomationPeerFactory, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.ComboBoxAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ComboBoxItemDataAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: Windows.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
class DatePickerAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IDatePickerAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.DatePickerAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IDatePickerAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.DatePicker, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.DatePickerAutomationPeer: ...
class DatePickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IDatePickerFlyoutPresenterAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.DatePickerFlyoutPresenterAutomationPeer'
class FlipViewAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IFlipViewAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.FlipViewAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IFlipViewAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.FlipView, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FlipViewAutomationPeer: ...
class FlipViewItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IFlipViewItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.FlipViewItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IFlipViewItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.FlipViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FlipViewItemAutomationPeer: ...
class FlipViewItemDataAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IFlipViewItemDataAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.FlipViewItemDataAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: Windows.UI.Xaml.Automation.Peers.IFlipViewItemDataAutomationPeerFactory, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.FlipViewAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FlipViewItemDataAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: Windows.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
class FlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IFlyoutPresenterAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.FlyoutPresenterAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IFlyoutPresenterAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.FlyoutPresenter, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FlyoutPresenterAutomationPeer: ...
class FrameworkElementAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.AutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeerFactory, owner: Windows.UI.Xaml.FrameworkElement, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer: ...
    @winrt_mixinmethod
    def get_Owner(self: Windows.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeer) -> Windows.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def FromElement(cls: Windows.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeerStatics, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_classmethod
    def CreatePeerForElement(cls: Windows.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeerStatics, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    Owner = property(get_Owner, None)
class GridViewAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IGridViewAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.GridViewAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IGridViewAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.GridView, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GridViewAutomationPeer: ...
class GridViewHeaderItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IGridViewHeaderItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.GridViewHeaderItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IGridViewHeaderItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.GridViewHeaderItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GridViewHeaderItemAutomationPeer: ...
class GridViewItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IGridViewItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.GridViewItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IGridViewItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.GridViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GridViewItemAutomationPeer: ...
class GridViewItemDataAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IGridViewItemDataAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.GridViewItemDataAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: Windows.UI.Xaml.Automation.Peers.IGridViewItemDataAutomationPeerFactory, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.GridViewAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GridViewItemDataAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: Windows.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
class GroupItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IGroupItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.GroupItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IGroupItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.GroupItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GroupItemAutomationPeer: ...
class HubAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IHubAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.HubAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IHubAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Hub, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.HubAutomationPeer: ...
class HubSectionAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IHubSectionAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.HubSectionAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IHubSectionAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.HubSection, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.HubSectionAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: Windows.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
class HyperlinkButtonAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IHyperlinkButtonAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.HyperlinkButtonAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IHyperlinkButtonAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.HyperlinkButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.HyperlinkButtonAutomationPeer: ...
    @winrt_mixinmethod
    def Invoke(self: Windows.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
class IAppBarAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAppBarAutomationPeer'
    _iid_ = Guid('{8b4acfeb-89fa-4f13-84be-35ca5b7c9590}')
class IAppBarAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAppBarAutomationPeerFactory'
    _iid_ = Guid('{8360f4e2-e396-4517-af5d-f4cf34c54edf}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.AppBar, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.AppBarAutomationPeer: ...
class IAppBarButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAppBarButtonAutomationPeer'
    _iid_ = Guid('{443262b2-4f6d-4b76-9d2e-3eff777e8864}')
class IAppBarButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAppBarButtonAutomationPeerFactory'
    _iid_ = Guid('{aef0342a-acb7-42dc-97e3-847071865fd6}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.AppBarButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.AppBarButtonAutomationPeer: ...
class IAppBarToggleButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAppBarToggleButtonAutomationPeer'
    _iid_ = Guid('{8464efad-9655-4aff-9550-63ae9ec8fe9c}')
class IAppBarToggleButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAppBarToggleButtonAutomationPeerFactory'
    _iid_ = Guid('{d6f9139d-02c1-4221-9591-7d4efeb74701}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.AppBarToggleButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.AppBarToggleButtonAutomationPeer: ...
class IAutoSuggestBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutoSuggestBoxAutomationPeer'
    _iid_ = Guid('{2f32c302-f99b-491d-9726-a5e181643efa}')
class IAutoSuggestBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutoSuggestBoxAutomationPeerFactory'
    _iid_ = Guid('{80046849-18e7-4475-b362-4bbd53d24562}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.AutoSuggestBox) -> Windows.UI.Xaml.Automation.Peers.AutoSuggestBoxAutomationPeer: ...
class IAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeer'
    _iid_ = Guid('{35aac87a-62ee-4d3e-a24c-2bc8432d68b7}')
    @winrt_commethod(6)
    def get_EventsSource(self) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(7)
    def put_EventsSource(self, value: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_commethod(8)
    def GetPattern(self, patternInterface: Windows.UI.Xaml.Automation.Peers.PatternInterface) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(9)
    def RaiseAutomationEvent(self, eventId: Windows.UI.Xaml.Automation.Peers.AutomationEvents) -> Void: ...
    @winrt_commethod(10)
    def RaisePropertyChangedEvent(self, automationProperty: Windows.UI.Xaml.Automation.AutomationProperty, oldValue: Windows.Win32.System.WinRT.IInspectable_head, newValue: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(11)
    def GetAcceleratorKey(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def GetAccessKey(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def GetAutomationControlType(self) -> Windows.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_commethod(14)
    def GetAutomationId(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def GetBoundingRectangle(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(16)
    def GetChildren(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(17)
    def GetClassName(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def GetClickablePoint(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(19)
    def GetHelpText(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def GetItemStatus(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def GetItemType(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def GetLabeledBy(self) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(23)
    def GetLocalizedControlType(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def GetName(self) -> WinRT_String: ...
    @winrt_commethod(25)
    def GetOrientation(self) -> Windows.UI.Xaml.Automation.Peers.AutomationOrientation: ...
    @winrt_commethod(26)
    def HasKeyboardFocus(self) -> Boolean: ...
    @winrt_commethod(27)
    def IsContentElement(self) -> Boolean: ...
    @winrt_commethod(28)
    def IsControlElement(self) -> Boolean: ...
    @winrt_commethod(29)
    def IsEnabled(self) -> Boolean: ...
    @winrt_commethod(30)
    def IsKeyboardFocusable(self) -> Boolean: ...
    @winrt_commethod(31)
    def IsOffscreen(self) -> Boolean: ...
    @winrt_commethod(32)
    def IsPassword(self) -> Boolean: ...
    @winrt_commethod(33)
    def IsRequiredForForm(self) -> Boolean: ...
    @winrt_commethod(34)
    def SetFocus(self) -> Void: ...
    @winrt_commethod(35)
    def GetParent(self) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(36)
    def InvalidatePeer(self) -> Void: ...
    @winrt_commethod(37)
    def GetPeerFromPoint(self, point: Windows.Foundation.Point) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(38)
    def GetLiveSetting(self) -> Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    EventsSource = property(get_EventsSource, put_EventsSource)
class IAutomationPeer2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeer2'
    _iid_ = Guid('{ea1f89c7-ebf5-4ab8-88f7-680d821dac61}')
class IAutomationPeer3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeer3'
    _iid_ = Guid('{d3cfb977-0084-41d7-a221-28158d3bc32c}')
    @winrt_commethod(6)
    def Navigate(self, direction: Windows.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def GetElementFromPoint(self, pointInWindowCoordinates: Windows.Foundation.Point) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(8)
    def GetFocusedElement(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(9)
    def ShowContextMenu(self) -> Void: ...
    @winrt_commethod(10)
    def GetControlledPeers(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(11)
    def GetAnnotations(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation]: ...
    @winrt_commethod(12)
    def SetParent(self, peer: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_commethod(13)
    def RaiseTextEditTextChangedEvent(self, automationTextEditChangeType: Windows.UI.Xaml.Automation.AutomationTextEditChangeType, changedData: Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_commethod(14)
    def GetPositionInSet(self) -> Int32: ...
    @winrt_commethod(15)
    def GetSizeOfSet(self) -> Int32: ...
    @winrt_commethod(16)
    def GetLevel(self) -> Int32: ...
    @winrt_commethod(17)
    def RaiseStructureChangedEvent(self, structureChangeType: Windows.UI.Xaml.Automation.Peers.AutomationStructureChangeType, child: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
class IAutomationPeer4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeer4'
    _iid_ = Guid('{761ce752-73c1-4f44-be75-43c49ec0d4d5}')
    @winrt_commethod(6)
    def GetLandmarkType(self) -> Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_commethod(7)
    def GetLocalizedLandmarkType(self) -> WinRT_String: ...
class IAutomationPeer5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeer5'
    _iid_ = Guid('{f632e1c6-0a3f-4574-9fef-cdc151765674}')
    @winrt_commethod(6)
    def IsPeripheral(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsDataValidForForm(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetFullDescription(self) -> WinRT_String: ...
class IAutomationPeer6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeer6'
    _iid_ = Guid('{caf8608f-13ff-42fb-866d-22206434cc6b}')
    @winrt_commethod(6)
    def GetCulture(self) -> Int32: ...
class IAutomationPeer7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeer7'
    _iid_ = Guid('{796b3287-e642-48ab-b223-5208b41da9d6}')
    @winrt_commethod(6)
    def RaiseNotificationEvent(self, notificationKind: Windows.UI.Xaml.Automation.Peers.AutomationNotificationKind, notificationProcessing: Windows.UI.Xaml.Automation.Peers.AutomationNotificationProcessing, displayString: WinRT_String, activityId: WinRT_String) -> Void: ...
class IAutomationPeer8(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeer8'
    _iid_ = Guid('{5c6a1fe6-9a55-4d7f-9498-cfe429e92da8}')
    @winrt_commethod(6)
    def GetHeadingLevel(self) -> Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
class IAutomationPeer9(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeer9'
    _iid_ = Guid('{df2e0265-1d74-57fa-8094-f81c2f626b8c}')
    @winrt_commethod(6)
    def IsDialog(self) -> Boolean: ...
class IAutomationPeerAnnotation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerAnnotation'
    _iid_ = Guid('{0c456061-52cf-43fa-82f8-07f137351e5a}')
    @winrt_commethod(6)
    def get_Type(self) -> Windows.UI.Xaml.Automation.AnnotationType: ...
    @winrt_commethod(7)
    def put_Type(self, value: Windows.UI.Xaml.Automation.AnnotationType) -> Void: ...
    @winrt_commethod(8)
    def get_Peer(self) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(9)
    def put_Peer(self, value: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    Type = property(get_Type, put_Type)
    Peer = property(get_Peer, put_Peer)
class IAutomationPeerAnnotationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerAnnotationFactory'
    _iid_ = Guid('{f59c439e-c65b-43cd-9009-03fc023363a7}')
    @winrt_commethod(6)
    def CreateInstance(self, type: Windows.UI.Xaml.Automation.AnnotationType) -> Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation: ...
    @winrt_commethod(7)
    def CreateWithPeerParameter(self, type: Windows.UI.Xaml.Automation.AnnotationType, peer: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation: ...
class IAutomationPeerAnnotationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerAnnotationStatics'
    _iid_ = Guid('{8809a87d-09b2-4d45-b78b-1d3b3b09f661}')
    @winrt_commethod(6)
    def get_TypeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PeerProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TypeProperty = property(get_TypeProperty, None)
    PeerProperty = property(get_PeerProperty, None)
class IAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerFactory'
    _iid_ = Guid('{20c27545-a88b-43c8-bc24-cea9dafd04a3}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
class IAutomationPeerOverrides(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides'
    _iid_ = Guid('{bea93e67-dbee-4f7b-af0d-a79aae5333bf}')
    @winrt_commethod(6)
    def GetPatternCore(self, patternInterface: Windows.UI.Xaml.Automation.Peers.PatternInterface) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def GetAcceleratorKeyCore(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetAccessKeyCore(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetAutomationControlTypeCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_commethod(10)
    def GetAutomationIdCore(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def GetBoundingRectangleCore(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(12)
    def GetChildrenCore(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(13)
    def GetClassNameCore(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def GetClickablePointCore(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(15)
    def GetHelpTextCore(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def GetItemStatusCore(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def GetItemTypeCore(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def GetLabeledByCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(19)
    def GetLocalizedControlTypeCore(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def GetNameCore(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def GetOrientationCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationOrientation: ...
    @winrt_commethod(22)
    def HasKeyboardFocusCore(self) -> Boolean: ...
    @winrt_commethod(23)
    def IsContentElementCore(self) -> Boolean: ...
    @winrt_commethod(24)
    def IsControlElementCore(self) -> Boolean: ...
    @winrt_commethod(25)
    def IsEnabledCore(self) -> Boolean: ...
    @winrt_commethod(26)
    def IsKeyboardFocusableCore(self) -> Boolean: ...
    @winrt_commethod(27)
    def IsOffscreenCore(self) -> Boolean: ...
    @winrt_commethod(28)
    def IsPasswordCore(self) -> Boolean: ...
    @winrt_commethod(29)
    def IsRequiredForFormCore(self) -> Boolean: ...
    @winrt_commethod(30)
    def SetFocusCore(self) -> Void: ...
    @winrt_commethod(31)
    def GetPeerFromPointCore(self, point: Windows.Foundation.Point) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(32)
    def GetLiveSettingCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
class IAutomationPeerOverrides2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides2'
    _iid_ = Guid('{2603682a-9da6-4023-b496-496e5ef228d2}')
    @winrt_commethod(6)
    def ShowContextMenuCore(self) -> Void: ...
    @winrt_commethod(7)
    def GetControlledPeersCore(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
class IAutomationPeerOverrides3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides3'
    _iid_ = Guid('{b6f0c4ad-4d39-49e6-bb91-d924eefd8538}')
    @winrt_commethod(6)
    def NavigateCore(self, direction: Windows.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def GetElementFromPointCore(self, pointInWindowCoordinates: Windows.Foundation.Point) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(8)
    def GetFocusedElementCore(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(9)
    def GetAnnotationsCore(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation]: ...
    @winrt_commethod(10)
    def GetPositionInSetCore(self) -> Int32: ...
    @winrt_commethod(11)
    def GetSizeOfSetCore(self) -> Int32: ...
    @winrt_commethod(12)
    def GetLevelCore(self) -> Int32: ...
class IAutomationPeerOverrides4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides4'
    _iid_ = Guid('{b186cda2-5d46-4bcd-a811-269ad15b3aee}')
    @winrt_commethod(6)
    def GetLandmarkTypeCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_commethod(7)
    def GetLocalizedLandmarkTypeCore(self) -> WinRT_String: ...
class IAutomationPeerOverrides5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides5'
    _iid_ = Guid('{2c847c85-781e-49f7-9fef-b9e14d014707}')
    @winrt_commethod(6)
    def IsPeripheralCore(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsDataValidForFormCore(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetFullDescriptionCore(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDescribedByCore(self) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(10)
    def GetFlowsToCore(self) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(11)
    def GetFlowsFromCore(self) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
class IAutomationPeerOverrides6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides6'
    _iid_ = Guid('{e98babe7-f6ff-444c-9c0d-277eaf0ad9c0}')
    @winrt_commethod(6)
    def GetCultureCore(self) -> Int32: ...
class IAutomationPeerOverrides8(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides8'
    _iid_ = Guid('{0e1ebbd4-a003-4936-8175-f5457c07f0c6}')
    @winrt_commethod(6)
    def GetHeadingLevelCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
class IAutomationPeerOverrides9(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerOverrides9'
    _iid_ = Guid('{f3709e8b-091a-5db5-b896-ff78f01990c9}')
    @winrt_commethod(6)
    def IsDialogCore(self) -> Boolean: ...
class IAutomationPeerProtected(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerProtected'
    _iid_ = Guid('{f4b40e52-642f-4629-a54a-ea5d2349c448}')
    @winrt_commethod(6)
    def PeerFromProvider(self, provider: Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(7)
    def ProviderFromPeer(self, peer: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class IAutomationPeerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerStatics'
    _iid_ = Guid('{562f7fb0-a331-4a9c-9dec-bfb7586fffff}')
    @winrt_commethod(6)
    def ListenerExists(self, eventId: Windows.UI.Xaml.Automation.Peers.AutomationEvents) -> Boolean: ...
class IAutomationPeerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IAutomationPeerStatics3'
    _iid_ = Guid('{572c5714-7f87-4271-819f-6cf4c4d022d0}')
    @winrt_commethod(6)
    def GenerateRawElementProviderRuntimeId(self) -> Windows.UI.Xaml.Automation.Peers.RawElementProviderRuntimeId: ...
class IButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IButtonAutomationPeer'
    _iid_ = Guid('{fb77efbe-39ec-4508-8ac3-51a1424027d7}')
class IButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IButtonAutomationPeerFactory'
    _iid_ = Guid('{3fdb9f49-f4ab-4780-8644-03376299a175}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Button, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ButtonAutomationPeer: ...
class IButtonBaseAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IButtonBaseAutomationPeer'
    _iid_ = Guid('{a4f3b5b6-7585-4e0b-96d2-08cf6f28befa}')
class IButtonBaseAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IButtonBaseAutomationPeerFactory'
    _iid_ = Guid('{8a04091e-e6b2-4c60-a759-c13ca45165ed}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.ButtonBase, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer: ...
class ICalendarDatePickerAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ICalendarDatePickerAutomationPeer'
    _iid_ = Guid('{40d8938e-db5e-4b03-beba-d10f62419787}')
class ICalendarDatePickerAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ICalendarDatePickerAutomationPeerFactory'
    _iid_ = Guid('{ab705dd2-d293-45bf-9f19-26f7603a5e9b}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.CalendarDatePicker, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.CalendarDatePickerAutomationPeer: ...
class ICaptureElementAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ICaptureElementAutomationPeer'
    _iid_ = Guid('{dcc44ee0-fa45-45c6-8bb7-320d808f5958}')
class ICaptureElementAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ICaptureElementAutomationPeerFactory'
    _iid_ = Guid('{9b92ef48-85e9-4869-b175-8f7cf45a6d9f}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.CaptureElement, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.CaptureElementAutomationPeer: ...
class ICheckBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ICheckBoxAutomationPeer'
    _iid_ = Guid('{eb15bc42-c0a9-46c6-ac24-b83de429c733}')
class ICheckBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ICheckBoxAutomationPeerFactory'
    _iid_ = Guid('{b75c775d-eb8f-44ef-a27c-e26ac7de8333}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.CheckBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.CheckBoxAutomationPeer: ...
class IColorPickerSliderAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IColorPickerSliderAutomationPeer'
    _iid_ = Guid('{a514215a-7293-4577-924c-47d4e0bf9b90}')
class IColorPickerSliderAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IColorPickerSliderAutomationPeerFactory'
    _iid_ = Guid('{1a55c77e-9dd6-45a3-9042-b40200fea1a9}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.ColorPickerSlider, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ColorPickerSliderAutomationPeer: ...
class IColorSpectrumAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IColorSpectrumAutomationPeer'
    _iid_ = Guid('{15d5ba03-010d-4ff7-9087-f4dd09f831b7}')
class IColorSpectrumAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IColorSpectrumAutomationPeerFactory'
    _iid_ = Guid('{0ac400e1-b743-4496-837a-8889e6ac6497}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.ColorSpectrum, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ColorSpectrumAutomationPeer: ...
class IComboBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IComboBoxAutomationPeer'
    _iid_ = Guid('{7eb40d0b-75c5-4263-ba6a-d4a54fb0f239}')
class IComboBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IComboBoxAutomationPeerFactory'
    _iid_ = Guid('{098e5b0d-1b90-40b9-9be3-b23267eb13cf}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ComboBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ComboBoxAutomationPeer: ...
class IComboBoxItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IComboBoxItemAutomationPeer'
    _iid_ = Guid('{12ddc76e-9552-446a-82ee-938cc371800f}')
class IComboBoxItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IComboBoxItemAutomationPeerFactory'
    _iid_ = Guid('{134ac7fc-397a-403f-a6ec-1ce8beda15e5}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ComboBoxItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ComboBoxItemAutomationPeer: ...
class IComboBoxItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IComboBoxItemDataAutomationPeer'
    _iid_ = Guid('{4fef6df2-289c-4c04-831b-5a668c6d7104}')
class IComboBoxItemDataAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IComboBoxItemDataAutomationPeerFactory'
    _iid_ = Guid('{14a8d4f6-469a-41ba-9d93-44a1a55da872}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.ComboBoxAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ComboBoxItemDataAutomationPeer: ...
class IDatePickerAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IDatePickerAutomationPeer'
    _iid_ = Guid('{d07d357f-a0b9-45dc-991a-76c505e7d0f5}')
class IDatePickerAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IDatePickerAutomationPeerFactory'
    _iid_ = Guid('{e5667d19-9157-4436-9f4d-7fb99174b48e}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.DatePicker, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.DatePickerAutomationPeer: ...
class IDatePickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IDatePickerFlyoutPresenterAutomationPeer'
    _iid_ = Guid('{752aed38-c2bf-4880-82b2-a6c05e90c135}')
class IFlipViewAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IFlipViewAutomationPeer'
    _iid_ = Guid('{8ec0353a-4284-4b00-aef8-a2688ea5e3c4}')
class IFlipViewAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IFlipViewAutomationPeerFactory'
    _iid_ = Guid('{4395ab0d-8d83-483c-88eb-e2617b0d293f}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.FlipView, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FlipViewAutomationPeer: ...
class IFlipViewItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IFlipViewItemAutomationPeer'
    _iid_ = Guid('{c83034de-fa08-4bd3-aeb2-d2e5bfa04df9}')
class IFlipViewItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IFlipViewItemAutomationPeerFactory'
    _iid_ = Guid('{69109356-d0e5-4c10-a09c-ad0bf1b0cb01}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.FlipViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FlipViewItemAutomationPeer: ...
class IFlipViewItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IFlipViewItemDataAutomationPeer'
    _iid_ = Guid('{b0986175-00bc-4118-8a6f-16ee9c15d968}')
class IFlipViewItemDataAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IFlipViewItemDataAutomationPeerFactory'
    _iid_ = Guid('{3c864393-0aea-4e78-bc11-b775cac4114c}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.FlipViewAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FlipViewItemDataAutomationPeer: ...
class IFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IFlyoutPresenterAutomationPeer'
    _iid_ = Guid('{a01840b4-5fca-456f-98ea-300eb40b585e}')
class IFlyoutPresenterAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IFlyoutPresenterAutomationPeerFactory'
    _iid_ = Guid('{f350155f-8924-44c0-ba44-653fe79f1efb}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.FlyoutPresenter, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FlyoutPresenterAutomationPeer: ...
class IFrameworkElementAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeer'
    _iid_ = Guid('{b90ad781-bfeb-4451-bd47-9f3a63ebd24a}')
    @winrt_commethod(6)
    def get_Owner(self) -> Windows.UI.Xaml.UIElement: ...
    Owner = property(get_Owner, None)
class IFrameworkElementAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeerFactory'
    _iid_ = Guid('{0db9b8bc-b812-48e3-af1f-dbc57600c325}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.FrameworkElement, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer: ...
class IFrameworkElementAutomationPeerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeerStatics'
    _iid_ = Guid('{b9c0b997-2820-44a1-a5a8-9b801edc269e}')
    @winrt_commethod(6)
    def FromElement(self, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(7)
    def CreatePeerForElement(self, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
class IGridViewAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IGridViewAutomationPeer'
    _iid_ = Guid('{1c4401a4-d951-49ca-8f82-c7f3c60681b0}')
class IGridViewAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IGridViewAutomationPeerFactory'
    _iid_ = Guid('{8aca59dd-22a7-4800-894b-c1f485f38953}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.GridView, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GridViewAutomationPeer: ...
class IGridViewHeaderItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IGridViewHeaderItemAutomationPeer'
    _iid_ = Guid('{e3dcef3a-e08a-48e7-b23a-2be5b66e474e}')
class IGridViewHeaderItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IGridViewHeaderItemAutomationPeerFactory'
    _iid_ = Guid('{2c80b4d2-ffc2-4157-88dd-59cd92e39715}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.GridViewHeaderItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GridViewHeaderItemAutomationPeer: ...
class IGridViewItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IGridViewItemAutomationPeer'
    _iid_ = Guid('{93ef2d07-346c-4166-a4ba-bc6a181e7f33}')
class IGridViewItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IGridViewItemAutomationPeerFactory'
    _iid_ = Guid('{fafec376-f22e-466d-913c-ae24ccdb160f}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.GridViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GridViewItemAutomationPeer: ...
class IGridViewItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IGridViewItemDataAutomationPeer'
    _iid_ = Guid('{f3f4868f-29d4-4094-8c54-ea61a88294a4}')
class IGridViewItemDataAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IGridViewItemDataAutomationPeerFactory'
    _iid_ = Guid('{a65e7a88-770d-402c-996f-67506af2a4af}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.GridViewAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GridViewItemDataAutomationPeer: ...
class IGroupItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IGroupItemAutomationPeer'
    _iid_ = Guid('{1914fe6d-0740-4236-9ee1-38cf19c1c388}')
class IGroupItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IGroupItemAutomationPeerFactory'
    _iid_ = Guid('{56a64567-f21c-4c90-b379-15a27c7f8409}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.GroupItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GroupItemAutomationPeer: ...
class IHubAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IHubAutomationPeer'
    _iid_ = Guid('{4ddee056-4ebc-4620-a05d-903e3c9a4ead}')
class IHubAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IHubAutomationPeerFactory'
    _iid_ = Guid('{c762d43f-79dd-43ee-8777-8d08b39aa065}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Hub, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.HubAutomationPeer: ...
class IHubSectionAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IHubSectionAutomationPeer'
    _iid_ = Guid('{16d91ff7-7431-4d82-83ce-cfa3192b0f18}')
class IHubSectionAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IHubSectionAutomationPeerFactory'
    _iid_ = Guid('{c68e27e8-17ec-4329-91ae-2d0b2339d498}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.HubSection, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.HubSectionAutomationPeer: ...
class IHyperlinkButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IHyperlinkButtonAutomationPeer'
    _iid_ = Guid('{aa7afcb1-0edf-46d9-aa9e-0eb21d140097}')
class IHyperlinkButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IHyperlinkButtonAutomationPeerFactory'
    _iid_ = Guid('{59bc1661-c182-49af-9526-44b88e628455}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.HyperlinkButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.HyperlinkButtonAutomationPeer: ...
class IImageAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IImageAutomationPeer'
    _iid_ = Guid('{9b0bbf8c-60a2-48bf-ab2c-1a52a451d2d4}')
class IImageAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IImageAutomationPeerFactory'
    _iid_ = Guid('{90304003-687d-47bf-b3a2-4babcad8ef50}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Image, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ImageAutomationPeer: ...
class IInkToolbarAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IInkToolbarAutomationPeer'
    _iid_ = Guid('{123baaa4-f2e8-4bcb-9382-5dfdd11fe45f}')
class IItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IItemAutomationPeer'
    _iid_ = Guid('{953c34f6-3b31-47a7-b3bf-25d3ae99c317}')
    @winrt_commethod(6)
    def get_Item(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_ItemsControlAutomationPeer(self) -> Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer: ...
    Item = property(get_Item, None)
    ItemsControlAutomationPeer = property(get_ItemsControlAutomationPeer, None)
class IItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IItemAutomationPeerFactory'
    _iid_ = Guid('{29065073-de3d-4d3f-97b4-4d6f9d53444d}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
class IItemsControlAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IItemsControlAutomationPeer'
    _iid_ = Guid('{96e76bf1-37f7-4088-925d-65268e83e34d}')
class IItemsControlAutomationPeer2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IItemsControlAutomationPeer2'
    _iid_ = Guid('{c48d8917-95a8-47b8-a517-bf891a6c039b}')
    @winrt_commethod(6)
    def CreateItemAutomationPeer(self, item: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
class IItemsControlAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IItemsControlAutomationPeerFactory'
    _iid_ = Guid('{4038a259-2e1a-49ca-a533-c64f181577e6}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ItemsControl, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer: ...
class IItemsControlAutomationPeerOverrides2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IItemsControlAutomationPeerOverrides2'
    _iid_ = Guid('{361dc0e8-b56f-45e9-80fe-10a0fb0fe177}')
    @winrt_commethod(6)
    def OnCreateItemAutomationPeer(self, item: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
class IListBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListBoxAutomationPeer'
    _iid_ = Guid('{8cd0d608-b402-4a6e-bd9a-343f8845eb32}')
class IListBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListBoxAutomationPeerFactory'
    _iid_ = Guid('{e2362185-7df6-49f7-8abc-4c33f1a3d46e}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListBoxAutomationPeer: ...
class IListBoxItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListBoxItemAutomationPeer'
    _iid_ = Guid('{1bc6e1c6-2997-42df-99eb-92bc1dd149fb}')
class IListBoxItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListBoxItemAutomationPeerFactory'
    _iid_ = Guid('{509f9dd8-b0aa-443f-a110-41209af44f1c}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListBoxItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListBoxItemAutomationPeer: ...
class IListBoxItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListBoxItemDataAutomationPeer'
    _iid_ = Guid('{fd7d5fee-fde0-482a-8084-dcebba5b9806}')
class IListBoxItemDataAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListBoxItemDataAutomationPeerFactory'
    _iid_ = Guid('{d7924e16-bd8d-4662-a995-20ff9a056093}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.ListBoxAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListBoxItemDataAutomationPeer: ...
class IListPickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListPickerFlyoutPresenterAutomationPeer'
    _iid_ = Guid('{56dfdc58-2395-4060-8047-8ea463698a24}')
class IListViewAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListViewAutomationPeer'
    _iid_ = Guid('{73cecc87-c0dc-4260-9148-75e9864a7230}')
class IListViewAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListViewAutomationPeerFactory'
    _iid_ = Guid('{65f39174-eaa2-4e44-8be6-4cca28cd0288}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListView, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewAutomationPeer: ...
class IListViewBaseAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListViewBaseAutomationPeer'
    _iid_ = Guid('{87ec7649-b83d-4e55-9afd-bd835e748f5c}')
class IListViewBaseAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListViewBaseAutomationPeerFactory'
    _iid_ = Guid('{70d3c2be-8950-4647-9362-fd002f8ff82e}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListViewBase, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer: ...
class IListViewBaseHeaderItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListViewBaseHeaderItemAutomationPeer'
    _iid_ = Guid('{7cb8b732-c1f0-4a3c-bc14-85dd48dedb85}')
class IListViewBaseHeaderItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListViewBaseHeaderItemAutomationPeerFactory'
    _iid_ = Guid('{40ec995f-d631-4004-832e-6d8643e51561}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListViewBaseHeaderItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer: ...
class IListViewHeaderItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListViewHeaderItemAutomationPeer'
    _iid_ = Guid('{67ab1e4b-ad61-4c88-ba45-0f3a8d061f8f}')
class IListViewHeaderItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListViewHeaderItemAutomationPeerFactory'
    _iid_ = Guid('{07668694-2ca5-4be4-a8b9-592d48f76087}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListViewHeaderItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewHeaderItemAutomationPeer: ...
class IListViewItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListViewItemAutomationPeer'
    _iid_ = Guid('{ca114e70-a16d-4d09-a1cf-1856ef98a9ec}')
class IListViewItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListViewItemAutomationPeerFactory'
    _iid_ = Guid('{c47dfbc0-facc-4024-a73b-17ec4e662654}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer: ...
class IListViewItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListViewItemDataAutomationPeer'
    _iid_ = Guid('{15a8d7fd-d7a5-4a6c-963c-6f7ce464671a}')
class IListViewItemDataAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IListViewItemDataAutomationPeerFactory'
    _iid_ = Guid('{d0db12bb-d715-4523-acc0-1e1072d8e32b}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewItemDataAutomationPeer: ...
class ILoopingSelectorAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ILoopingSelectorAutomationPeer'
    _iid_ = Guid('{50b406ca-bae9-4816-8a3a-0cb4f96478a2}')
class ILoopingSelectorItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ILoopingSelectorItemAutomationPeer'
    _iid_ = Guid('{d3fa68bf-04cf-4f4c-8d3e-4780a19d4788}')
class ILoopingSelectorItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ILoopingSelectorItemDataAutomationPeer'
    _iid_ = Guid('{ef567e32-7cd2-4d32-9590-1f588d5ef38d}')
class IMapControlAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMapControlAutomationPeer'
    _iid_ = Guid('{425beee4-f2e8-4bcb-9382-5dfdd11fe45f}')
class IMediaElementAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMediaElementAutomationPeer'
    _iid_ = Guid('{ba0b9fc2-a6e2-41a5-b17a-d1594613efba}')
class IMediaElementAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMediaElementAutomationPeerFactory'
    _iid_ = Guid('{b2ad3b28-7575-4173-9bc7-80367a164ed2}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.MediaElement, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MediaElementAutomationPeer: ...
class IMediaPlayerElementAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMediaPlayerElementAutomationPeer'
    _iid_ = Guid('{02bed209-3f65-4fdd-b5ca-c4750d4e6ea4}')
class IMediaPlayerElementAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMediaPlayerElementAutomationPeerFactory'
    _iid_ = Guid('{08848077-82af-4d19-b170-282a9e0e7f37}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.MediaPlayerElement, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MediaPlayerElementAutomationPeer: ...
class IMediaTransportControlsAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMediaTransportControlsAutomationPeer'
    _iid_ = Guid('{a3ad8d93-79f8-4958-a3c8-980defb83d15}')
class IMediaTransportControlsAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMediaTransportControlsAutomationPeerFactory'
    _iid_ = Guid('{f41cb003-e103-4ab0-812a-a08fbdb570ce}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.MediaTransportControls, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MediaTransportControlsAutomationPeer: ...
class IMenuBarAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMenuBarAutomationPeer'
    _iid_ = Guid('{4b6adcf1-f274-5592-85a8-7b099e99b320}')
class IMenuBarAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMenuBarAutomationPeerFactory'
    _iid_ = Guid('{2a094871-4a9b-5a0b-9fda-7bc3ae957c53}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: Windows.UI.Xaml.Controls.MenuBar, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MenuBarAutomationPeer: ...
class IMenuBarItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMenuBarItemAutomationPeer'
    _iid_ = Guid('{0fce49b4-cff5-5c4b-98ee-e75fdddf799a}')
class IMenuBarItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMenuBarItemAutomationPeerFactory'
    _iid_ = Guid('{c9c77746-130f-5b19-83a6-61db584613aa}')
    @winrt_commethod(6)
    def CreateInstance(self, owner: Windows.UI.Xaml.Controls.MenuBarItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MenuBarItemAutomationPeer: ...
class IMenuFlyoutItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMenuFlyoutItemAutomationPeer'
    _iid_ = Guid('{1fc19462-21df-456e-aa11-8fac6b4b2af6}')
class IMenuFlyoutItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMenuFlyoutItemAutomationPeerFactory'
    _iid_ = Guid('{d08bfcb8-20d1-45d8-a2c2-2f130df714e0}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.MenuFlyoutItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MenuFlyoutItemAutomationPeer: ...
class IMenuFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMenuFlyoutPresenterAutomationPeer'
    _iid_ = Guid('{e244a871-fcbb-48fc-8a93-41ea134b53ce}')
class IMenuFlyoutPresenterAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IMenuFlyoutPresenterAutomationPeerFactory'
    _iid_ = Guid('{07b5172d-761d-452b-9e6d-fa2a8be0ad26}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.MenuFlyoutPresenter, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MenuFlyoutPresenterAutomationPeer: ...
class INavigationViewItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.INavigationViewItemAutomationPeer'
    _iid_ = Guid('{309847a5-9971-4d8d-a81c-085c7086a1b9}')
class INavigationViewItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.INavigationViewItemAutomationPeerFactory'
    _iid_ = Guid('{0bc2835d-aa38-4f97-9664-e6fc821d81ed}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.NavigationViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.NavigationViewItemAutomationPeer: ...
class IPasswordBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IPasswordBoxAutomationPeer'
    _iid_ = Guid('{684f065e-3df3-4b9f-82ad-8819db3b218a}')
class IPasswordBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IPasswordBoxAutomationPeerFactory'
    _iid_ = Guid('{ac3d7ede-dca4-481c-b520-4a9b3f3b179c}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.PasswordBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.PasswordBoxAutomationPeer: ...
class IPersonPictureAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IPersonPictureAutomationPeer'
    _iid_ = Guid('{27156d4c-a66f-4aaf-8286-4f796d30628c}')
class IPersonPictureAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IPersonPictureAutomationPeerFactory'
    _iid_ = Guid('{a95f1f6d-2524-44a4-97fd-1181130100ad}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.PersonPicture, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.PersonPictureAutomationPeer: ...
class IPickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IPickerFlyoutPresenterAutomationPeer'
    _iid_ = Guid('{28414bf7-8382-4eae-93c1-d6f035aa8155}')
class IPivotAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IPivotAutomationPeer'
    _iid_ = Guid('{e715a8f8-3b9d-402c-81e2-6e912ef58981}')
class IPivotAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IPivotAutomationPeerFactory'
    _iid_ = Guid('{3efe0f94-0c91-4341-b9ac-1b56b4e6b84f}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Pivot) -> Windows.UI.Xaml.Automation.Peers.PivotAutomationPeer: ...
class IPivotItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IPivotItemAutomationPeer'
    _iid_ = Guid('{1a4241ad-5d55-4d27-b40f-2d37506fbe78}')
class IPivotItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IPivotItemAutomationPeerFactory'
    _iid_ = Guid('{f2810471-183f-416b-b41a-1e5a958a91f4}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.PivotItem) -> Windows.UI.Xaml.Automation.Peers.PivotItemAutomationPeer: ...
class IPivotItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IPivotItemDataAutomationPeer'
    _iid_ = Guid('{a2a3b788-ea1d-48b7-88ee-f08b6aa07fee}')
class IPivotItemDataAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IPivotItemDataAutomationPeerFactory'
    _iid_ = Guid('{517a2480-d3b6-412e-82b6-94a0a84c13b0}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.PivotAutomationPeer) -> Windows.UI.Xaml.Automation.Peers.PivotItemDataAutomationPeer: ...
class IProgressBarAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IProgressBarAutomationPeer'
    _iid_ = Guid('{93f48f86-d840-4fb6-ac2f-5f779b854b0d}')
class IProgressBarAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IProgressBarAutomationPeerFactory'
    _iid_ = Guid('{364679ab-b80f-41b4-8eea-2f5251bc739c}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ProgressBar, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ProgressBarAutomationPeer: ...
class IProgressRingAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IProgressRingAutomationPeer'
    _iid_ = Guid('{bc305eee-39d3-4eeb-ac33-2394de123e2e}')
class IProgressRingAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IProgressRingAutomationPeerFactory'
    _iid_ = Guid('{f3db204b-157e-40bc-9593-55bc5c71a4f6}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ProgressRing, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ProgressRingAutomationPeer: ...
class IRadioButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRadioButtonAutomationPeer'
    _iid_ = Guid('{7e6a5ed8-0b30-4743-b102-dcdf548e3131}')
class IRadioButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRadioButtonAutomationPeerFactory'
    _iid_ = Guid('{4940c4fd-3d88-49ca-8f31-924187af0bfe}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.RadioButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RadioButtonAutomationPeer: ...
class IRangeBaseAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRangeBaseAutomationPeer'
    _iid_ = Guid('{e454b549-4b2c-42ad-b04b-d35947d1ee50}')
class IRangeBaseAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRangeBaseAutomationPeerFactory'
    _iid_ = Guid('{827c7601-3078-4479-95ea-91374ca06207}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.RangeBase, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer: ...
class IRatingControlAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRatingControlAutomationPeer'
    _iid_ = Guid('{3d14349a-9963-4a47-823c-f457cb3209d5}')
class IRatingControlAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRatingControlAutomationPeerFactory'
    _iid_ = Guid('{f179f272-9846-4632-8b9c-be6fa8d3c9bb}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.RatingControl, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RatingControlAutomationPeer: ...
class IRepeatButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRepeatButtonAutomationPeer'
    _iid_ = Guid('{29e41ad5-a8ac-4e8a-83d8-09e37e054257}')
class IRepeatButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRepeatButtonAutomationPeerFactory'
    _iid_ = Guid('{6a6ff9d4-575e-4e60-bdd6-ec14419b4ff6}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.RepeatButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RepeatButtonAutomationPeer: ...
class IRichEditBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRichEditBoxAutomationPeer'
    _iid_ = Guid('{c69f5c04-16ee-467a-a833-c3da8458ad64}')
class IRichEditBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRichEditBoxAutomationPeerFactory'
    _iid_ = Guid('{752c8399-d296-4d87-9020-a4750e885b3c}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.RichEditBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RichEditBoxAutomationPeer: ...
class IRichTextBlockAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRichTextBlockAutomationPeer'
    _iid_ = Guid('{93a01a9c-9609-41fa-82f3-909c09f49a72}')
class IRichTextBlockAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRichTextBlockAutomationPeerFactory'
    _iid_ = Guid('{2038ae61-1389-467a-aed6-37334da9622b}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.RichTextBlock, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RichTextBlockAutomationPeer: ...
class IRichTextBlockOverflowAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRichTextBlockOverflowAutomationPeer'
    _iid_ = Guid('{8c9a409a-2736-437b-ab36-a16a202f105d}')
class IRichTextBlockOverflowAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IRichTextBlockOverflowAutomationPeerFactory'
    _iid_ = Guid('{bd5eb663-2c14-4665-adef-f2b033947beb}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.RichTextBlockOverflow, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RichTextBlockOverflowAutomationPeer: ...
class IScrollBarAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IScrollBarAutomationPeer'
    _iid_ = Guid('{69e0c369-bbe7-41f2-87ca-aad813fe550e}')
class IScrollBarAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IScrollBarAutomationPeerFactory'
    _iid_ = Guid('{e1302110-afeb-4595-8e3d-edc0844a2b21}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.ScrollBar, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ScrollBarAutomationPeer: ...
class IScrollViewerAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IScrollViewerAutomationPeer'
    _iid_ = Guid('{d985f259-1b09-4e88-88fd-421750dc6b45}')
class IScrollViewerAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IScrollViewerAutomationPeerFactory'
    _iid_ = Guid('{270dff7d-d96d-48f9-a36a-c252aa9c4670}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ScrollViewer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ScrollViewerAutomationPeer: ...
class ISearchBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ISearchBoxAutomationPeer'
    _iid_ = Guid('{854011a4-18a6-4f30-939b-8871afa3f5e9}')
class ISearchBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ISearchBoxAutomationPeerFactory'
    _iid_ = Guid('{b3c01430-7faa-41bb-8e91-7c761c5267f1}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.SearchBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SearchBoxAutomationPeer: ...
class ISelectorAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ISelectorAutomationPeer'
    _iid_ = Guid('{162ac829-7115-43ec-b383-a7b71644069d}')
class ISelectorAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ISelectorAutomationPeerFactory'
    _iid_ = Guid('{7b525646-829b-4dcc-bd52-5a8d0399387a}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.Selector, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer: ...
class ISelectorItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ISelectorItemAutomationPeer'
    _iid_ = Guid('{ae8b3477-860a-45bb-bf7c-e1b27419d1dd}')
class ISelectorItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ISelectorItemAutomationPeerFactory'
    _iid_ = Guid('{66d7edfb-786d-4362-a964-ebfb21776c30}')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer: ...
class ISemanticZoomAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ISemanticZoomAutomationPeer'
    _iid_ = Guid('{3c2fac6c-a977-47fc-b44e-2754c0b2bea9}')
class ISemanticZoomAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ISemanticZoomAutomationPeerFactory'
    _iid_ = Guid('{f518d44d-a493-4496-b077-9674c7f4c5fa}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.SemanticZoom, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SemanticZoomAutomationPeer: ...
class ISettingsFlyoutAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ISettingsFlyoutAutomationPeer'
    _iid_ = Guid('{d0de0cdb-30cf-47a6-a5eb-9c77f0b0d6dd}')
class ISettingsFlyoutAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ISettingsFlyoutAutomationPeerFactory'
    _iid_ = Guid('{f94762bd-8a14-40e4-94a7-3f33c922e945}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.SettingsFlyout, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SettingsFlyoutAutomationPeer: ...
class ISliderAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ISliderAutomationPeer'
    _iid_ = Guid('{ec30015a-d611-46d0-ae4f-6ecf27dfbaa5}')
class ISliderAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ISliderAutomationPeerFactory'
    _iid_ = Guid('{971b8056-9a7a-4df9-95fa-6f5c04c91cac}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Slider, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SliderAutomationPeer: ...
class ITextBlockAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ITextBlockAutomationPeer'
    _iid_ = Guid('{be2057f5-6715-4e69-a050-92bd0ce232a9}')
class ITextBlockAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ITextBlockAutomationPeerFactory'
    _iid_ = Guid('{76bf924b-7ca0-4b01-bc5c-a8cf4d3691de}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.TextBlock, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TextBlockAutomationPeer: ...
class ITextBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ITextBoxAutomationPeer'
    _iid_ = Guid('{3a4f1ca0-5e5d-4d26-9067-e740bf657a9f}')
class ITextBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ITextBoxAutomationPeerFactory'
    _iid_ = Guid('{01f0c067-966b-4130-b872-469e42bd4a7f}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.TextBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TextBoxAutomationPeer: ...
class IThumbAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IThumbAutomationPeer'
    _iid_ = Guid('{dc2949b5-b45e-4d6d-892f-d9422c950efb}')
class IThumbAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IThumbAutomationPeerFactory'
    _iid_ = Guid('{970743ff-af41-4600-b55d-26d43df860e1}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.Thumb, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ThumbAutomationPeer: ...
class ITimePickerAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ITimePickerAutomationPeer'
    _iid_ = Guid('{a43d44ef-3285-4df7-b4a4-e4cdf36a3a17}')
class ITimePickerAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ITimePickerAutomationPeerFactory'
    _iid_ = Guid('{978f6671-47f8-40a7-9e21-68128b16b4fd}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.TimePicker, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TimePickerAutomationPeer: ...
class ITimePickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ITimePickerFlyoutPresenterAutomationPeer'
    _iid_ = Guid('{da93ee27-82f1-4701-8706-be297bf06043}')
class IToggleButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IToggleButtonAutomationPeer'
    _iid_ = Guid('{62dbe6c5-bc0a-45bb-bf77-ea0f1502891f}')
class IToggleButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IToggleButtonAutomationPeerFactory'
    _iid_ = Guid('{c9218cc4-ad4b-4d03-a6a4-7d59e6360004}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.ToggleButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer: ...
class IToggleMenuFlyoutItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IToggleMenuFlyoutItemAutomationPeer'
    _iid_ = Guid('{6b57eafe-6af1-4903-8373-3437bf352345}')
class IToggleMenuFlyoutItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IToggleMenuFlyoutItemAutomationPeerFactory'
    _iid_ = Guid('{94364b77-8f6c-4837-aae3-94d010d8d162}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ToggleMenuFlyoutItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ToggleMenuFlyoutItemAutomationPeer: ...
class IToggleSwitchAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IToggleSwitchAutomationPeer'
    _iid_ = Guid('{c011f174-e89e-4790-bf9a-78ebb5f59e9f}')
class IToggleSwitchAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.IToggleSwitchAutomationPeerFactory'
    _iid_ = Guid('{31f933e3-fef8-4419-9df5-d9ef7196ea34}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ToggleSwitch, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ToggleSwitchAutomationPeer: ...
class ITreeViewItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ITreeViewItemAutomationPeer'
    _iid_ = Guid('{2331d648-b617-437f-920c-71d450503e65}')
class ITreeViewItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ITreeViewItemAutomationPeerFactory'
    _iid_ = Guid('{73d388bf-1d01-4159-82c0-2b2996dbfdce}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.TreeViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TreeViewItemAutomationPeer: ...
class ITreeViewListAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ITreeViewListAutomationPeer'
    _iid_ = Guid('{71c1b5bc-bb29-4479-a8a8-606be6b823ae}')
class ITreeViewListAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ITreeViewListAutomationPeerFactory'
    _iid_ = Guid('{00f597e2-f811-475a-bfe6-290fe707fa88}')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.TreeViewList, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TreeViewListAutomationPeer: ...
class ImageAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IImageAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ImageAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IImageAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Image, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ImageAutomationPeer: ...
class InkToolbarAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IInkToolbarAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.InkToolbarAutomationPeer'
class ItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.AutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: Windows.UI.Xaml.Automation.Peers.IItemAutomationPeerFactory, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
    @winrt_mixinmethod
    def get_Item(self: Windows.UI.Xaml.Automation.Peers.IItemAutomationPeer) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_ItemsControlAutomationPeer(self: Windows.UI.Xaml.Automation.Peers.IItemAutomationPeer) -> Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer: ...
    @winrt_mixinmethod
    def Realize(self: Windows.UI.Xaml.Automation.Provider.IVirtualizedItemProvider) -> Void: ...
    Item = property(get_Item, None)
    ItemsControlAutomationPeer = property(get_ItemsControlAutomationPeer, None)
class ItemsControlAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IItemsControlAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IItemsControlAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ItemsControl, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer: ...
    @winrt_mixinmethod
    def CreateItemAutomationPeer(self: Windows.UI.Xaml.Automation.Peers.IItemsControlAutomationPeer2, item: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
    @winrt_mixinmethod
    def OnCreateItemAutomationPeer(self: Windows.UI.Xaml.Automation.Peers.IItemsControlAutomationPeerOverrides2, item: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
    @winrt_mixinmethod
    def FindItemByProperty(self: Windows.UI.Xaml.Automation.Provider.IItemContainerProvider, startAfter: Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple, automationProperty: Windows.UI.Xaml.Automation.AutomationProperty, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class ListBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IListBoxAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ListBoxAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IListBoxAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ListBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListBoxAutomationPeer: ...
class ListBoxItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IListBoxItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ListBoxItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IListBoxItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ListBoxItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListBoxItemAutomationPeer: ...
class ListBoxItemDataAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IListBoxItemDataAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ListBoxItemDataAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: Windows.UI.Xaml.Automation.Peers.IListBoxItemDataAutomationPeerFactory, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.ListBoxAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListBoxItemDataAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: Windows.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
class ListPickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IListPickerFlyoutPresenterAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ListPickerFlyoutPresenterAutomationPeer'
class ListViewAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IListViewAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ListViewAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IListViewAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ListView, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewAutomationPeer: ...
class ListViewBaseAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IListViewBaseAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IListViewBaseAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ListViewBase, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer: ...
    @winrt_mixinmethod
    def get_DropEffect(self: Windows.UI.Xaml.Automation.Provider.IDropTargetProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DropEffects(self: Windows.UI.Xaml.Automation.Provider.IDropTargetProvider) -> SZArray[WinRT_String]: ...
    DropEffect = property(get_DropEffect, None)
    DropEffects = property(get_DropEffects, None)
class ListViewBaseHeaderItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IListViewBaseHeaderItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IListViewBaseHeaderItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ListViewBaseHeaderItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer: ...
class ListViewHeaderItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IListViewHeaderItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ListViewHeaderItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IListViewHeaderItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ListViewHeaderItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewHeaderItemAutomationPeer: ...
class ListViewItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IListViewItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IListViewItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ListViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer: ...
class ListViewItemDataAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IListViewItemDataAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ListViewItemDataAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: Windows.UI.Xaml.Automation.Peers.IListViewItemDataAutomationPeerFactory, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewItemDataAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: Windows.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
class LoopingSelectorAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ILoopingSelectorAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.LoopingSelectorAutomationPeer'
    @winrt_mixinmethod
    def get_CanSelectMultiple(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSelectionRequired(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def GetSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> SZArray[Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    @winrt_mixinmethod
    def FindItemByProperty(self: Windows.UI.Xaml.Automation.Provider.IItemContainerProvider, startAfter: Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple, automationProperty: Windows.UI.Xaml.Automation.AutomationProperty, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def get_HorizontallyScrollable(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_HorizontalScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_HorizontalViewSize(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticallyScrollable(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_VerticalScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalViewSize(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def Scroll(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider, horizontalAmount: Windows.UI.Xaml.Automation.ScrollAmount, verticalAmount: Windows.UI.Xaml.Automation.ScrollAmount) -> Void: ...
    @winrt_mixinmethod
    def SetScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider, horizontalPercent: Double, verticalPercent: Double) -> Void: ...
    CanSelectMultiple = property(get_CanSelectMultiple, None)
    IsSelectionRequired = property(get_IsSelectionRequired, None)
    ExpandCollapseState = property(get_ExpandCollapseState, None)
    HorizontallyScrollable = property(get_HorizontallyScrollable, None)
    HorizontalScrollPercent = property(get_HorizontalScrollPercent, None)
    HorizontalViewSize = property(get_HorizontalViewSize, None)
    VerticallyScrollable = property(get_VerticallyScrollable, None)
    VerticalScrollPercent = property(get_VerticalScrollPercent, None)
    VerticalViewSize = property(get_VerticalViewSize, None)
class LoopingSelectorItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ILoopingSelectorItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.LoopingSelectorItemAutomationPeer'
    @winrt_mixinmethod
    def ScrollIntoView(self: Windows.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
    @winrt_mixinmethod
    def get_IsSelected(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_SelectionContainer(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_mixinmethod
    def AddToSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def Select(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class LoopingSelectorItemDataAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.AutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ILoopingSelectorItemDataAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.LoopingSelectorItemDataAutomationPeer'
    @winrt_mixinmethod
    def Realize(self: Windows.UI.Xaml.Automation.Provider.IVirtualizedItemProvider) -> Void: ...
class MapControlAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IMapControlAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.MapControlAutomationPeer'
    @winrt_mixinmethod
    def get_HorizontallyScrollable(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_HorizontalScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_HorizontalViewSize(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticallyScrollable(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_VerticalScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalViewSize(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def Scroll(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider, horizontalAmount: Windows.UI.Xaml.Automation.ScrollAmount, verticalAmount: Windows.UI.Xaml.Automation.ScrollAmount) -> Void: ...
    @winrt_mixinmethod
    def SetScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider, horizontalPercent: Double, verticalPercent: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CanZoom(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider2) -> Boolean: ...
    @winrt_mixinmethod
    def get_ZoomLevel(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider2) -> Double: ...
    @winrt_mixinmethod
    def get_MaxZoom(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider2) -> Double: ...
    @winrt_mixinmethod
    def get_MinZoom(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider2) -> Double: ...
    @winrt_mixinmethod
    def Zoom(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider2, zoom: Double) -> Void: ...
    @winrt_mixinmethod
    def ZoomByUnit(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider2, zoomUnit: Windows.UI.Xaml.Automation.ZoomUnit) -> Void: ...
    @winrt_mixinmethod
    def get_CanMove(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanResize(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanRotate(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider) -> Boolean: ...
    @winrt_mixinmethod
    def Move(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider, x: Double, y: Double) -> Void: ...
    @winrt_mixinmethod
    def Resize(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider, width: Double, height: Double) -> Void: ...
    @winrt_mixinmethod
    def Rotate(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider, degrees: Double) -> Void: ...
    HorizontallyScrollable = property(get_HorizontallyScrollable, None)
    HorizontalScrollPercent = property(get_HorizontalScrollPercent, None)
    HorizontalViewSize = property(get_HorizontalViewSize, None)
    VerticallyScrollable = property(get_VerticallyScrollable, None)
    VerticalScrollPercent = property(get_VerticalScrollPercent, None)
    VerticalViewSize = property(get_VerticalViewSize, None)
    CanZoom = property(get_CanZoom, None)
    ZoomLevel = property(get_ZoomLevel, None)
    MaxZoom = property(get_MaxZoom, None)
    MinZoom = property(get_MinZoom, None)
    CanMove = property(get_CanMove, None)
    CanResize = property(get_CanResize, None)
    CanRotate = property(get_CanRotate, None)
class MediaElementAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IMediaElementAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.MediaElementAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IMediaElementAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.MediaElement, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MediaElementAutomationPeer: ...
class MediaPlayerElementAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IMediaPlayerElementAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.MediaPlayerElementAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IMediaPlayerElementAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.MediaPlayerElement, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MediaPlayerElementAutomationPeer: ...
class MediaTransportControlsAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IMediaTransportControlsAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.MediaTransportControlsAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IMediaTransportControlsAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.MediaTransportControls, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MediaTransportControlsAutomationPeer: ...
class MenuBarAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IMenuBarAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.MenuBarAutomationPeer'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Automation.Peers.IMenuBarAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.MenuBar, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MenuBarAutomationPeer: ...
class MenuBarItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IMenuBarItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.MenuBarItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Automation.Peers.IMenuBarItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.MenuBarItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MenuBarItemAutomationPeer: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Invoke(self: Windows.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class MenuFlyoutItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IMenuFlyoutItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.MenuFlyoutItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IMenuFlyoutItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.MenuFlyoutItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MenuFlyoutItemAutomationPeer: ...
    @winrt_mixinmethod
    def Invoke(self: Windows.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
class MenuFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IMenuFlyoutPresenterAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.MenuFlyoutPresenterAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IMenuFlyoutPresenterAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.MenuFlyoutPresenter, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MenuFlyoutPresenterAutomationPeer: ...
class NavigationViewItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.INavigationViewItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.NavigationViewItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.INavigationViewItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.NavigationViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.NavigationViewItemAutomationPeer: ...
class PasswordBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IPasswordBoxAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.PasswordBoxAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IPasswordBoxAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.PasswordBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.PasswordBoxAutomationPeer: ...
PatternInterface = Int32
PatternInterface_Invoke: PatternInterface = 0
PatternInterface_Selection: PatternInterface = 1
PatternInterface_Value: PatternInterface = 2
PatternInterface_RangeValue: PatternInterface = 3
PatternInterface_Scroll: PatternInterface = 4
PatternInterface_ScrollItem: PatternInterface = 5
PatternInterface_ExpandCollapse: PatternInterface = 6
PatternInterface_Grid: PatternInterface = 7
PatternInterface_GridItem: PatternInterface = 8
PatternInterface_MultipleView: PatternInterface = 9
PatternInterface_Window: PatternInterface = 10
PatternInterface_SelectionItem: PatternInterface = 11
PatternInterface_Dock: PatternInterface = 12
PatternInterface_Table: PatternInterface = 13
PatternInterface_TableItem: PatternInterface = 14
PatternInterface_Toggle: PatternInterface = 15
PatternInterface_Transform: PatternInterface = 16
PatternInterface_Text: PatternInterface = 17
PatternInterface_ItemContainer: PatternInterface = 18
PatternInterface_VirtualizedItem: PatternInterface = 19
PatternInterface_Text2: PatternInterface = 20
PatternInterface_TextChild: PatternInterface = 21
PatternInterface_TextRange: PatternInterface = 22
PatternInterface_Annotation: PatternInterface = 23
PatternInterface_Drag: PatternInterface = 24
PatternInterface_DropTarget: PatternInterface = 25
PatternInterface_ObjectModel: PatternInterface = 26
PatternInterface_Spreadsheet: PatternInterface = 27
PatternInterface_SpreadsheetItem: PatternInterface = 28
PatternInterface_Styles: PatternInterface = 29
PatternInterface_Transform2: PatternInterface = 30
PatternInterface_SynchronizedInput: PatternInterface = 31
PatternInterface_TextEdit: PatternInterface = 32
PatternInterface_CustomNavigation: PatternInterface = 33
class PersonPictureAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IPersonPictureAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.PersonPictureAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IPersonPictureAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.PersonPicture, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.PersonPictureAutomationPeer: ...
class PickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IPickerFlyoutPresenterAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.PickerFlyoutPresenterAutomationPeer'
class PivotAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IPivotAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.PivotAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IPivotAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Pivot) -> Windows.UI.Xaml.Automation.Peers.PivotAutomationPeer: ...
    @winrt_mixinmethod
    def get_CanSelectMultiple(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSelectionRequired(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def GetSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> SZArray[Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    @winrt_mixinmethod
    def get_HorizontallyScrollable(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_HorizontalScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_HorizontalViewSize(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticallyScrollable(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_VerticalScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalViewSize(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def Scroll(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider, horizontalAmount: Windows.UI.Xaml.Automation.ScrollAmount, verticalAmount: Windows.UI.Xaml.Automation.ScrollAmount) -> Void: ...
    @winrt_mixinmethod
    def SetScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider, horizontalPercent: Double, verticalPercent: Double) -> Void: ...
    CanSelectMultiple = property(get_CanSelectMultiple, None)
    IsSelectionRequired = property(get_IsSelectionRequired, None)
    HorizontallyScrollable = property(get_HorizontallyScrollable, None)
    HorizontalScrollPercent = property(get_HorizontalScrollPercent, None)
    HorizontalViewSize = property(get_HorizontalViewSize, None)
    VerticallyScrollable = property(get_VerticallyScrollable, None)
    VerticalScrollPercent = property(get_VerticalScrollPercent, None)
    VerticalViewSize = property(get_VerticalViewSize, None)
class PivotItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IPivotItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.PivotItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IPivotItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.PivotItem) -> Windows.UI.Xaml.Automation.Peers.PivotItemAutomationPeer: ...
class PivotItemDataAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IPivotItemDataAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.PivotItemDataAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: Windows.UI.Xaml.Automation.Peers.IPivotItemDataAutomationPeerFactory, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.PivotAutomationPeer) -> Windows.UI.Xaml.Automation.Peers.PivotItemDataAutomationPeer: ...
    @winrt_mixinmethod
    def ScrollIntoView(self: Windows.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
    @winrt_mixinmethod
    def get_IsSelected(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_SelectionContainer(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_mixinmethod
    def AddToSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def Select(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def Realize(self: Windows.UI.Xaml.Automation.Provider.IVirtualizedItemProvider) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class ProgressBarAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IProgressBarAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ProgressBarAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IProgressBarAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ProgressBar, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ProgressBarAutomationPeer: ...
class ProgressRingAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IProgressRingAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ProgressRingAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IProgressRingAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ProgressRing, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ProgressRingAutomationPeer: ...
class RadioButtonAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IRadioButtonAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.RadioButtonAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IRadioButtonAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.RadioButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RadioButtonAutomationPeer: ...
    @winrt_mixinmethod
    def get_IsSelected(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_SelectionContainer(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_mixinmethod
    def AddToSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def Select(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class RangeBaseAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IRangeBaseAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IRangeBaseAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Primitives.RangeBase, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_LargeChange(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def get_Maximum(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def get_Minimum(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def get_SmallChange(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_mixinmethod
    def SetValue(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider, value: Double) -> Void: ...
    IsReadOnly = property(get_IsReadOnly, None)
    LargeChange = property(get_LargeChange, None)
    Maximum = property(get_Maximum, None)
    Minimum = property(get_Minimum, None)
    SmallChange = property(get_SmallChange, None)
    Value = property(get_Value, None)
class RatingControlAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IRatingControlAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.RatingControlAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IRatingControlAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.RatingControl, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RatingControlAutomationPeer: ...
class RawElementProviderRuntimeId(EasyCastStructure):
    Part1: UInt32
    Part2: UInt32
class RepeatButtonAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IRepeatButtonAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.RepeatButtonAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IRepeatButtonAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Primitives.RepeatButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RepeatButtonAutomationPeer: ...
    @winrt_mixinmethod
    def Invoke(self: Windows.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
class RichEditBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IRichEditBoxAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.RichEditBoxAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IRichEditBoxAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.RichEditBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RichEditBoxAutomationPeer: ...
class RichTextBlockAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IRichTextBlockAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.RichTextBlockAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IRichTextBlockAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.RichTextBlock, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RichTextBlockAutomationPeer: ...
class RichTextBlockOverflowAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IRichTextBlockOverflowAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.RichTextBlockOverflowAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IRichTextBlockOverflowAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.RichTextBlockOverflow, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RichTextBlockOverflowAutomationPeer: ...
class ScrollBarAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IScrollBarAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ScrollBarAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IScrollBarAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Primitives.ScrollBar, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ScrollBarAutomationPeer: ...
class ScrollViewerAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IScrollViewerAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ScrollViewerAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IScrollViewerAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ScrollViewer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ScrollViewerAutomationPeer: ...
    @winrt_mixinmethod
    def get_HorizontallyScrollable(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_HorizontalScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_HorizontalViewSize(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticallyScrollable(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_VerticalScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def get_VerticalViewSize(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_mixinmethod
    def Scroll(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider, horizontalAmount: Windows.UI.Xaml.Automation.ScrollAmount, verticalAmount: Windows.UI.Xaml.Automation.ScrollAmount) -> Void: ...
    @winrt_mixinmethod
    def SetScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider, horizontalPercent: Double, verticalPercent: Double) -> Void: ...
    HorizontallyScrollable = property(get_HorizontallyScrollable, None)
    HorizontalScrollPercent = property(get_HorizontalScrollPercent, None)
    HorizontalViewSize = property(get_HorizontalViewSize, None)
    VerticallyScrollable = property(get_VerticallyScrollable, None)
    VerticalScrollPercent = property(get_VerticalScrollPercent, None)
    VerticalViewSize = property(get_VerticalViewSize, None)
class SearchBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ISearchBoxAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.SearchBoxAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.ISearchBoxAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.SearchBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SearchBoxAutomationPeer: ...
class SelectorAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ISelectorAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.ISelectorAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Primitives.Selector, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer: ...
    @winrt_mixinmethod
    def get_CanSelectMultiple(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSelectionRequired(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def GetSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> SZArray[Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    CanSelectMultiple = property(get_CanSelectMultiple, None)
    IsSelectionRequired = property(get_IsSelectionRequired, None)
class SelectorItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ISelectorItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithParentAndItem(cls: Windows.UI.Xaml.Automation.Peers.ISelectorItemAutomationPeerFactory, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer: ...
    @winrt_mixinmethod
    def get_IsSelected(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_SelectionContainer(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_mixinmethod
    def AddToSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_mixinmethod
    def Select(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class SemanticZoomAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ISemanticZoomAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.SemanticZoomAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.ISemanticZoomAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.SemanticZoom, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SemanticZoomAutomationPeer: ...
    @winrt_mixinmethod
    def get_ToggleState(self: Windows.UI.Xaml.Automation.Provider.IToggleProvider) -> Windows.UI.Xaml.Automation.ToggleState: ...
    @winrt_mixinmethod
    def Toggle(self: Windows.UI.Xaml.Automation.Provider.IToggleProvider) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class SettingsFlyoutAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ISettingsFlyoutAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.SettingsFlyoutAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.ISettingsFlyoutAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.SettingsFlyout, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SettingsFlyoutAutomationPeer: ...
class SliderAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ISliderAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.SliderAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.ISliderAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Slider, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SliderAutomationPeer: ...
class TextBlockAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ITextBlockAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.TextBlockAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.ITextBlockAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.TextBlock, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TextBlockAutomationPeer: ...
class TextBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ITextBoxAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.TextBoxAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.ITextBoxAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.TextBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TextBoxAutomationPeer: ...
class ThumbAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IThumbAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ThumbAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IThumbAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Primitives.Thumb, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ThumbAutomationPeer: ...
class TimePickerAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ITimePickerAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.TimePickerAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.ITimePickerAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.TimePicker, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TimePickerAutomationPeer: ...
class TimePickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ITimePickerFlyoutPresenterAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.TimePickerFlyoutPresenterAutomationPeer'
class ToggleButtonAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IToggleButtonAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IToggleButtonAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Primitives.ToggleButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer: ...
    @winrt_mixinmethod
    def get_ToggleState(self: Windows.UI.Xaml.Automation.Provider.IToggleProvider) -> Windows.UI.Xaml.Automation.ToggleState: ...
    @winrt_mixinmethod
    def Toggle(self: Windows.UI.Xaml.Automation.Provider.IToggleProvider) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class ToggleMenuFlyoutItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IToggleMenuFlyoutItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ToggleMenuFlyoutItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IToggleMenuFlyoutItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ToggleMenuFlyoutItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ToggleMenuFlyoutItemAutomationPeer: ...
    @winrt_mixinmethod
    def get_ToggleState(self: Windows.UI.Xaml.Automation.Provider.IToggleProvider) -> Windows.UI.Xaml.Automation.ToggleState: ...
    @winrt_mixinmethod
    def Toggle(self: Windows.UI.Xaml.Automation.Provider.IToggleProvider) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class ToggleSwitchAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.IToggleSwitchAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.ToggleSwitchAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IToggleSwitchAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.ToggleSwitch, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ToggleSwitchAutomationPeer: ...
    @winrt_mixinmethod
    def get_ToggleState(self: Windows.UI.Xaml.Automation.Provider.IToggleProvider) -> Windows.UI.Xaml.Automation.ToggleState: ...
    @winrt_mixinmethod
    def Toggle(self: Windows.UI.Xaml.Automation.Provider.IToggleProvider) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class TreeViewItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ITreeViewItemAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.TreeViewItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.ITreeViewItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.TreeViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TreeViewItemAutomationPeer: ...
    @winrt_mixinmethod
    def get_ExpandCollapseState(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_mixinmethod
    def Collapse(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_mixinmethod
    def Expand(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class TreeViewListAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer
    default_interface: Windows.UI.Xaml.Automation.Peers.ITreeViewListAutomationPeer
    _classid_ = 'Windows.UI.Xaml.Automation.Peers.TreeViewListAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.ITreeViewListAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.TreeViewList, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TreeViewListAutomationPeer: ...
make_head(_module, 'AppBarAutomationPeer')
make_head(_module, 'AppBarButtonAutomationPeer')
make_head(_module, 'AppBarToggleButtonAutomationPeer')
make_head(_module, 'AutoSuggestBoxAutomationPeer')
make_head(_module, 'AutomationPeer')
make_head(_module, 'AutomationPeerAnnotation')
make_head(_module, 'ButtonAutomationPeer')
make_head(_module, 'ButtonBaseAutomationPeer')
make_head(_module, 'CalendarDatePickerAutomationPeer')
make_head(_module, 'CaptureElementAutomationPeer')
make_head(_module, 'CheckBoxAutomationPeer')
make_head(_module, 'ColorPickerSliderAutomationPeer')
make_head(_module, 'ColorSpectrumAutomationPeer')
make_head(_module, 'ComboBoxAutomationPeer')
make_head(_module, 'ComboBoxItemAutomationPeer')
make_head(_module, 'ComboBoxItemDataAutomationPeer')
make_head(_module, 'DatePickerAutomationPeer')
make_head(_module, 'DatePickerFlyoutPresenterAutomationPeer')
make_head(_module, 'FlipViewAutomationPeer')
make_head(_module, 'FlipViewItemAutomationPeer')
make_head(_module, 'FlipViewItemDataAutomationPeer')
make_head(_module, 'FlyoutPresenterAutomationPeer')
make_head(_module, 'FrameworkElementAutomationPeer')
make_head(_module, 'GridViewAutomationPeer')
make_head(_module, 'GridViewHeaderItemAutomationPeer')
make_head(_module, 'GridViewItemAutomationPeer')
make_head(_module, 'GridViewItemDataAutomationPeer')
make_head(_module, 'GroupItemAutomationPeer')
make_head(_module, 'HubAutomationPeer')
make_head(_module, 'HubSectionAutomationPeer')
make_head(_module, 'HyperlinkButtonAutomationPeer')
make_head(_module, 'IAppBarAutomationPeer')
make_head(_module, 'IAppBarAutomationPeerFactory')
make_head(_module, 'IAppBarButtonAutomationPeer')
make_head(_module, 'IAppBarButtonAutomationPeerFactory')
make_head(_module, 'IAppBarToggleButtonAutomationPeer')
make_head(_module, 'IAppBarToggleButtonAutomationPeerFactory')
make_head(_module, 'IAutoSuggestBoxAutomationPeer')
make_head(_module, 'IAutoSuggestBoxAutomationPeerFactory')
make_head(_module, 'IAutomationPeer')
make_head(_module, 'IAutomationPeer2')
make_head(_module, 'IAutomationPeer3')
make_head(_module, 'IAutomationPeer4')
make_head(_module, 'IAutomationPeer5')
make_head(_module, 'IAutomationPeer6')
make_head(_module, 'IAutomationPeer7')
make_head(_module, 'IAutomationPeer8')
make_head(_module, 'IAutomationPeer9')
make_head(_module, 'IAutomationPeerAnnotation')
make_head(_module, 'IAutomationPeerAnnotationFactory')
make_head(_module, 'IAutomationPeerAnnotationStatics')
make_head(_module, 'IAutomationPeerFactory')
make_head(_module, 'IAutomationPeerOverrides')
make_head(_module, 'IAutomationPeerOverrides2')
make_head(_module, 'IAutomationPeerOverrides3')
make_head(_module, 'IAutomationPeerOverrides4')
make_head(_module, 'IAutomationPeerOverrides5')
make_head(_module, 'IAutomationPeerOverrides6')
make_head(_module, 'IAutomationPeerOverrides8')
make_head(_module, 'IAutomationPeerOverrides9')
make_head(_module, 'IAutomationPeerProtected')
make_head(_module, 'IAutomationPeerStatics')
make_head(_module, 'IAutomationPeerStatics3')
make_head(_module, 'IButtonAutomationPeer')
make_head(_module, 'IButtonAutomationPeerFactory')
make_head(_module, 'IButtonBaseAutomationPeer')
make_head(_module, 'IButtonBaseAutomationPeerFactory')
make_head(_module, 'ICalendarDatePickerAutomationPeer')
make_head(_module, 'ICalendarDatePickerAutomationPeerFactory')
make_head(_module, 'ICaptureElementAutomationPeer')
make_head(_module, 'ICaptureElementAutomationPeerFactory')
make_head(_module, 'ICheckBoxAutomationPeer')
make_head(_module, 'ICheckBoxAutomationPeerFactory')
make_head(_module, 'IColorPickerSliderAutomationPeer')
make_head(_module, 'IColorPickerSliderAutomationPeerFactory')
make_head(_module, 'IColorSpectrumAutomationPeer')
make_head(_module, 'IColorSpectrumAutomationPeerFactory')
make_head(_module, 'IComboBoxAutomationPeer')
make_head(_module, 'IComboBoxAutomationPeerFactory')
make_head(_module, 'IComboBoxItemAutomationPeer')
make_head(_module, 'IComboBoxItemAutomationPeerFactory')
make_head(_module, 'IComboBoxItemDataAutomationPeer')
make_head(_module, 'IComboBoxItemDataAutomationPeerFactory')
make_head(_module, 'IDatePickerAutomationPeer')
make_head(_module, 'IDatePickerAutomationPeerFactory')
make_head(_module, 'IDatePickerFlyoutPresenterAutomationPeer')
make_head(_module, 'IFlipViewAutomationPeer')
make_head(_module, 'IFlipViewAutomationPeerFactory')
make_head(_module, 'IFlipViewItemAutomationPeer')
make_head(_module, 'IFlipViewItemAutomationPeerFactory')
make_head(_module, 'IFlipViewItemDataAutomationPeer')
make_head(_module, 'IFlipViewItemDataAutomationPeerFactory')
make_head(_module, 'IFlyoutPresenterAutomationPeer')
make_head(_module, 'IFlyoutPresenterAutomationPeerFactory')
make_head(_module, 'IFrameworkElementAutomationPeer')
make_head(_module, 'IFrameworkElementAutomationPeerFactory')
make_head(_module, 'IFrameworkElementAutomationPeerStatics')
make_head(_module, 'IGridViewAutomationPeer')
make_head(_module, 'IGridViewAutomationPeerFactory')
make_head(_module, 'IGridViewHeaderItemAutomationPeer')
make_head(_module, 'IGridViewHeaderItemAutomationPeerFactory')
make_head(_module, 'IGridViewItemAutomationPeer')
make_head(_module, 'IGridViewItemAutomationPeerFactory')
make_head(_module, 'IGridViewItemDataAutomationPeer')
make_head(_module, 'IGridViewItemDataAutomationPeerFactory')
make_head(_module, 'IGroupItemAutomationPeer')
make_head(_module, 'IGroupItemAutomationPeerFactory')
make_head(_module, 'IHubAutomationPeer')
make_head(_module, 'IHubAutomationPeerFactory')
make_head(_module, 'IHubSectionAutomationPeer')
make_head(_module, 'IHubSectionAutomationPeerFactory')
make_head(_module, 'IHyperlinkButtonAutomationPeer')
make_head(_module, 'IHyperlinkButtonAutomationPeerFactory')
make_head(_module, 'IImageAutomationPeer')
make_head(_module, 'IImageAutomationPeerFactory')
make_head(_module, 'IInkToolbarAutomationPeer')
make_head(_module, 'IItemAutomationPeer')
make_head(_module, 'IItemAutomationPeerFactory')
make_head(_module, 'IItemsControlAutomationPeer')
make_head(_module, 'IItemsControlAutomationPeer2')
make_head(_module, 'IItemsControlAutomationPeerFactory')
make_head(_module, 'IItemsControlAutomationPeerOverrides2')
make_head(_module, 'IListBoxAutomationPeer')
make_head(_module, 'IListBoxAutomationPeerFactory')
make_head(_module, 'IListBoxItemAutomationPeer')
make_head(_module, 'IListBoxItemAutomationPeerFactory')
make_head(_module, 'IListBoxItemDataAutomationPeer')
make_head(_module, 'IListBoxItemDataAutomationPeerFactory')
make_head(_module, 'IListPickerFlyoutPresenterAutomationPeer')
make_head(_module, 'IListViewAutomationPeer')
make_head(_module, 'IListViewAutomationPeerFactory')
make_head(_module, 'IListViewBaseAutomationPeer')
make_head(_module, 'IListViewBaseAutomationPeerFactory')
make_head(_module, 'IListViewBaseHeaderItemAutomationPeer')
make_head(_module, 'IListViewBaseHeaderItemAutomationPeerFactory')
make_head(_module, 'IListViewHeaderItemAutomationPeer')
make_head(_module, 'IListViewHeaderItemAutomationPeerFactory')
make_head(_module, 'IListViewItemAutomationPeer')
make_head(_module, 'IListViewItemAutomationPeerFactory')
make_head(_module, 'IListViewItemDataAutomationPeer')
make_head(_module, 'IListViewItemDataAutomationPeerFactory')
make_head(_module, 'ILoopingSelectorAutomationPeer')
make_head(_module, 'ILoopingSelectorItemAutomationPeer')
make_head(_module, 'ILoopingSelectorItemDataAutomationPeer')
make_head(_module, 'IMapControlAutomationPeer')
make_head(_module, 'IMediaElementAutomationPeer')
make_head(_module, 'IMediaElementAutomationPeerFactory')
make_head(_module, 'IMediaPlayerElementAutomationPeer')
make_head(_module, 'IMediaPlayerElementAutomationPeerFactory')
make_head(_module, 'IMediaTransportControlsAutomationPeer')
make_head(_module, 'IMediaTransportControlsAutomationPeerFactory')
make_head(_module, 'IMenuBarAutomationPeer')
make_head(_module, 'IMenuBarAutomationPeerFactory')
make_head(_module, 'IMenuBarItemAutomationPeer')
make_head(_module, 'IMenuBarItemAutomationPeerFactory')
make_head(_module, 'IMenuFlyoutItemAutomationPeer')
make_head(_module, 'IMenuFlyoutItemAutomationPeerFactory')
make_head(_module, 'IMenuFlyoutPresenterAutomationPeer')
make_head(_module, 'IMenuFlyoutPresenterAutomationPeerFactory')
make_head(_module, 'INavigationViewItemAutomationPeer')
make_head(_module, 'INavigationViewItemAutomationPeerFactory')
make_head(_module, 'IPasswordBoxAutomationPeer')
make_head(_module, 'IPasswordBoxAutomationPeerFactory')
make_head(_module, 'IPersonPictureAutomationPeer')
make_head(_module, 'IPersonPictureAutomationPeerFactory')
make_head(_module, 'IPickerFlyoutPresenterAutomationPeer')
make_head(_module, 'IPivotAutomationPeer')
make_head(_module, 'IPivotAutomationPeerFactory')
make_head(_module, 'IPivotItemAutomationPeer')
make_head(_module, 'IPivotItemAutomationPeerFactory')
make_head(_module, 'IPivotItemDataAutomationPeer')
make_head(_module, 'IPivotItemDataAutomationPeerFactory')
make_head(_module, 'IProgressBarAutomationPeer')
make_head(_module, 'IProgressBarAutomationPeerFactory')
make_head(_module, 'IProgressRingAutomationPeer')
make_head(_module, 'IProgressRingAutomationPeerFactory')
make_head(_module, 'IRadioButtonAutomationPeer')
make_head(_module, 'IRadioButtonAutomationPeerFactory')
make_head(_module, 'IRangeBaseAutomationPeer')
make_head(_module, 'IRangeBaseAutomationPeerFactory')
make_head(_module, 'IRatingControlAutomationPeer')
make_head(_module, 'IRatingControlAutomationPeerFactory')
make_head(_module, 'IRepeatButtonAutomationPeer')
make_head(_module, 'IRepeatButtonAutomationPeerFactory')
make_head(_module, 'IRichEditBoxAutomationPeer')
make_head(_module, 'IRichEditBoxAutomationPeerFactory')
make_head(_module, 'IRichTextBlockAutomationPeer')
make_head(_module, 'IRichTextBlockAutomationPeerFactory')
make_head(_module, 'IRichTextBlockOverflowAutomationPeer')
make_head(_module, 'IRichTextBlockOverflowAutomationPeerFactory')
make_head(_module, 'IScrollBarAutomationPeer')
make_head(_module, 'IScrollBarAutomationPeerFactory')
make_head(_module, 'IScrollViewerAutomationPeer')
make_head(_module, 'IScrollViewerAutomationPeerFactory')
make_head(_module, 'ISearchBoxAutomationPeer')
make_head(_module, 'ISearchBoxAutomationPeerFactory')
make_head(_module, 'ISelectorAutomationPeer')
make_head(_module, 'ISelectorAutomationPeerFactory')
make_head(_module, 'ISelectorItemAutomationPeer')
make_head(_module, 'ISelectorItemAutomationPeerFactory')
make_head(_module, 'ISemanticZoomAutomationPeer')
make_head(_module, 'ISemanticZoomAutomationPeerFactory')
make_head(_module, 'ISettingsFlyoutAutomationPeer')
make_head(_module, 'ISettingsFlyoutAutomationPeerFactory')
make_head(_module, 'ISliderAutomationPeer')
make_head(_module, 'ISliderAutomationPeerFactory')
make_head(_module, 'ITextBlockAutomationPeer')
make_head(_module, 'ITextBlockAutomationPeerFactory')
make_head(_module, 'ITextBoxAutomationPeer')
make_head(_module, 'ITextBoxAutomationPeerFactory')
make_head(_module, 'IThumbAutomationPeer')
make_head(_module, 'IThumbAutomationPeerFactory')
make_head(_module, 'ITimePickerAutomationPeer')
make_head(_module, 'ITimePickerAutomationPeerFactory')
make_head(_module, 'ITimePickerFlyoutPresenterAutomationPeer')
make_head(_module, 'IToggleButtonAutomationPeer')
make_head(_module, 'IToggleButtonAutomationPeerFactory')
make_head(_module, 'IToggleMenuFlyoutItemAutomationPeer')
make_head(_module, 'IToggleMenuFlyoutItemAutomationPeerFactory')
make_head(_module, 'IToggleSwitchAutomationPeer')
make_head(_module, 'IToggleSwitchAutomationPeerFactory')
make_head(_module, 'ITreeViewItemAutomationPeer')
make_head(_module, 'ITreeViewItemAutomationPeerFactory')
make_head(_module, 'ITreeViewListAutomationPeer')
make_head(_module, 'ITreeViewListAutomationPeerFactory')
make_head(_module, 'ImageAutomationPeer')
make_head(_module, 'InkToolbarAutomationPeer')
make_head(_module, 'ItemAutomationPeer')
make_head(_module, 'ItemsControlAutomationPeer')
make_head(_module, 'ListBoxAutomationPeer')
make_head(_module, 'ListBoxItemAutomationPeer')
make_head(_module, 'ListBoxItemDataAutomationPeer')
make_head(_module, 'ListPickerFlyoutPresenterAutomationPeer')
make_head(_module, 'ListViewAutomationPeer')
make_head(_module, 'ListViewBaseAutomationPeer')
make_head(_module, 'ListViewBaseHeaderItemAutomationPeer')
make_head(_module, 'ListViewHeaderItemAutomationPeer')
make_head(_module, 'ListViewItemAutomationPeer')
make_head(_module, 'ListViewItemDataAutomationPeer')
make_head(_module, 'LoopingSelectorAutomationPeer')
make_head(_module, 'LoopingSelectorItemAutomationPeer')
make_head(_module, 'LoopingSelectorItemDataAutomationPeer')
make_head(_module, 'MapControlAutomationPeer')
make_head(_module, 'MediaElementAutomationPeer')
make_head(_module, 'MediaPlayerElementAutomationPeer')
make_head(_module, 'MediaTransportControlsAutomationPeer')
make_head(_module, 'MenuBarAutomationPeer')
make_head(_module, 'MenuBarItemAutomationPeer')
make_head(_module, 'MenuFlyoutItemAutomationPeer')
make_head(_module, 'MenuFlyoutPresenterAutomationPeer')
make_head(_module, 'NavigationViewItemAutomationPeer')
make_head(_module, 'PasswordBoxAutomationPeer')
make_head(_module, 'PersonPictureAutomationPeer')
make_head(_module, 'PickerFlyoutPresenterAutomationPeer')
make_head(_module, 'PivotAutomationPeer')
make_head(_module, 'PivotItemAutomationPeer')
make_head(_module, 'PivotItemDataAutomationPeer')
make_head(_module, 'ProgressBarAutomationPeer')
make_head(_module, 'ProgressRingAutomationPeer')
make_head(_module, 'RadioButtonAutomationPeer')
make_head(_module, 'RangeBaseAutomationPeer')
make_head(_module, 'RatingControlAutomationPeer')
make_head(_module, 'RawElementProviderRuntimeId')
make_head(_module, 'RepeatButtonAutomationPeer')
make_head(_module, 'RichEditBoxAutomationPeer')
make_head(_module, 'RichTextBlockAutomationPeer')
make_head(_module, 'RichTextBlockOverflowAutomationPeer')
make_head(_module, 'ScrollBarAutomationPeer')
make_head(_module, 'ScrollViewerAutomationPeer')
make_head(_module, 'SearchBoxAutomationPeer')
make_head(_module, 'SelectorAutomationPeer')
make_head(_module, 'SelectorItemAutomationPeer')
make_head(_module, 'SemanticZoomAutomationPeer')
make_head(_module, 'SettingsFlyoutAutomationPeer')
make_head(_module, 'SliderAutomationPeer')
make_head(_module, 'TextBlockAutomationPeer')
make_head(_module, 'TextBoxAutomationPeer')
make_head(_module, 'ThumbAutomationPeer')
make_head(_module, 'TimePickerAutomationPeer')
make_head(_module, 'TimePickerFlyoutPresenterAutomationPeer')
make_head(_module, 'ToggleButtonAutomationPeer')
make_head(_module, 'ToggleMenuFlyoutItemAutomationPeer')
make_head(_module, 'ToggleSwitchAutomationPeer')
make_head(_module, 'TreeViewItemAutomationPeer')
make_head(_module, 'TreeViewListAutomationPeer')
