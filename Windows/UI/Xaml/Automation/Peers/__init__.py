from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
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
    @winrt_commethod(131)
    def get_ToggleState(self) -> Windows.UI.Xaml.Automation.ToggleState: ...
    @winrt_commethod(132)
    def Toggle(self) -> Void: ...
    @winrt_commethod(133)
    def get_ExpandCollapseState(self) -> Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_commethod(134)
    def Collapse(self) -> Void: ...
    @winrt_commethod(135)
    def Expand(self) -> Void: ...
    @winrt_commethod(136)
    def get_IsModal(self) -> Boolean: ...
    @winrt_commethod(137)
    def get_IsTopmost(self) -> Boolean: ...
    @winrt_commethod(138)
    def get_Maximizable(self) -> Boolean: ...
    @winrt_commethod(139)
    def get_Minimizable(self) -> Boolean: ...
    @winrt_commethod(140)
    def get_InteractionState(self) -> Windows.UI.Xaml.Automation.WindowInteractionState: ...
    @winrt_commethod(141)
    def get_VisualState(self) -> Windows.UI.Xaml.Automation.WindowVisualState: ...
    @winrt_commethod(142)
    def Close(self) -> Void: ...
    @winrt_commethod(143)
    def SetVisualState(self, state: Windows.UI.Xaml.Automation.WindowVisualState) -> Void: ...
    @winrt_commethod(144)
    def WaitForInputIdle(self, milliseconds: Int32) -> Boolean: ...
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
    @winrt_commethod(123)
    def get_ExpandCollapseState(self) -> Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_commethod(124)
    def Collapse(self) -> Void: ...
    @winrt_commethod(125)
    def Expand(self) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class AppBarToggleButtonAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer
class AutoSuggestBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    ClassId = 'Windows.UI.Xaml.Automation.Peers.AutoSuggestBoxAutomationPeer'
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
    @winrt_commethod(112)
    def get_EventsSource(self) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(113)
    def put_EventsSource(self, value: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_commethod(114)
    def GetPattern(self, patternInterface: Windows.UI.Xaml.Automation.Peers.PatternInterface) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(115)
    def RaiseAutomationEvent(self, eventId: Windows.UI.Xaml.Automation.Peers.AutomationEvents) -> Void: ...
    @winrt_commethod(116)
    def RaisePropertyChangedEvent(self, automationProperty: Windows.UI.Xaml.Automation.AutomationProperty, oldValue: Windows.Win32.System.WinRT.IInspectable_head, newValue: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(117)
    def GetAcceleratorKey(self) -> WinRT_String: ...
    @winrt_commethod(118)
    def GetAccessKey(self) -> WinRT_String: ...
    @winrt_commethod(119)
    def GetAutomationControlType(self) -> Windows.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_commethod(120)
    def GetAutomationId(self) -> WinRT_String: ...
    @winrt_commethod(121)
    def GetBoundingRectangle(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(122)
    def GetChildren(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(123)
    def GetClassName(self) -> WinRT_String: ...
    @winrt_commethod(124)
    def GetClickablePoint(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(125)
    def GetHelpText(self) -> WinRT_String: ...
    @winrt_commethod(126)
    def GetItemStatus(self) -> WinRT_String: ...
    @winrt_commethod(127)
    def GetItemType(self) -> WinRT_String: ...
    @winrt_commethod(128)
    def GetLabeledBy(self) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(129)
    def GetLocalizedControlType(self) -> WinRT_String: ...
    @winrt_commethod(130)
    def GetName(self) -> WinRT_String: ...
    @winrt_commethod(131)
    def GetOrientation(self) -> Windows.UI.Xaml.Automation.Peers.AutomationOrientation: ...
    @winrt_commethod(132)
    def HasKeyboardFocus(self) -> Boolean: ...
    @winrt_commethod(133)
    def IsContentElement(self) -> Boolean: ...
    @winrt_commethod(134)
    def IsControlElement(self) -> Boolean: ...
    @winrt_commethod(135)
    def IsEnabled(self) -> Boolean: ...
    @winrt_commethod(136)
    def IsKeyboardFocusable(self) -> Boolean: ...
    @winrt_commethod(137)
    def IsOffscreen(self) -> Boolean: ...
    @winrt_commethod(138)
    def IsPassword(self) -> Boolean: ...
    @winrt_commethod(139)
    def IsRequiredForForm(self) -> Boolean: ...
    @winrt_commethod(140)
    def SetFocus(self) -> Void: ...
    @winrt_commethod(141)
    def GetParent(self) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(142)
    def InvalidatePeer(self) -> Void: ...
    @winrt_commethod(143)
    def GetPeerFromPoint(self, point: Windows.Foundation.Point) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(144)
    def GetLiveSetting(self) -> Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_commethod(145)
    def Navigate(self, direction: Windows.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(146)
    def GetElementFromPoint(self, pointInWindowCoordinates: Windows.Foundation.Point) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(147)
    def GetFocusedElement(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(148)
    def ShowContextMenu(self) -> Void: ...
    @winrt_commethod(149)
    def GetControlledPeers(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(150)
    def GetAnnotations(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation]: ...
    @winrt_commethod(151)
    def SetParent(self, peer: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_commethod(152)
    def RaiseTextEditTextChangedEvent(self, automationTextEditChangeType: Windows.UI.Xaml.Automation.AutomationTextEditChangeType, changedData: Windows.Foundation.Collections.IVectorView[WinRT_String]) -> Void: ...
    @winrt_commethod(153)
    def GetPositionInSet(self) -> Int32: ...
    @winrt_commethod(154)
    def GetSizeOfSet(self) -> Int32: ...
    @winrt_commethod(155)
    def GetLevel(self) -> Int32: ...
    @winrt_commethod(156)
    def RaiseStructureChangedEvent(self, structureChangeType: Windows.UI.Xaml.Automation.Peers.AutomationStructureChangeType, child: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Void: ...
    @winrt_commethod(157)
    def GetLandmarkType(self) -> Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_commethod(158)
    def GetLocalizedLandmarkType(self) -> WinRT_String: ...
    @winrt_commethod(159)
    def IsPeripheral(self) -> Boolean: ...
    @winrt_commethod(160)
    def IsDataValidForForm(self) -> Boolean: ...
    @winrt_commethod(161)
    def GetFullDescription(self) -> WinRT_String: ...
    @winrt_commethod(162)
    def GetCulture(self) -> Int32: ...
    @winrt_commethod(163)
    def RaiseNotificationEvent(self, notificationKind: Windows.UI.Xaml.Automation.Peers.AutomationNotificationKind, notificationProcessing: Windows.UI.Xaml.Automation.Peers.AutomationNotificationProcessing, displayString: WinRT_String, activityId: WinRT_String) -> Void: ...
    @winrt_commethod(164)
    def GetHeadingLevel(self) -> Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_commethod(165)
    def IsDialog(self) -> Boolean: ...
    @winrt_commethod(166)
    def PeerFromProvider(self, provider: Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(167)
    def ProviderFromPeer(self, peer: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(168)
    def GetPatternCore(self, patternInterface: Windows.UI.Xaml.Automation.Peers.PatternInterface) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(169)
    def GetAcceleratorKeyCore(self) -> WinRT_String: ...
    @winrt_commethod(170)
    def GetAccessKeyCore(self) -> WinRT_String: ...
    @winrt_commethod(171)
    def GetAutomationControlTypeCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationControlType: ...
    @winrt_commethod(172)
    def GetAutomationIdCore(self) -> WinRT_String: ...
    @winrt_commethod(173)
    def GetBoundingRectangleCore(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(174)
    def GetChildrenCore(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(175)
    def GetClassNameCore(self) -> WinRT_String: ...
    @winrt_commethod(176)
    def GetClickablePointCore(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(177)
    def GetHelpTextCore(self) -> WinRT_String: ...
    @winrt_commethod(178)
    def GetItemStatusCore(self) -> WinRT_String: ...
    @winrt_commethod(179)
    def GetItemTypeCore(self) -> WinRT_String: ...
    @winrt_commethod(180)
    def GetLabeledByCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(181)
    def GetLocalizedControlTypeCore(self) -> WinRT_String: ...
    @winrt_commethod(182)
    def GetNameCore(self) -> WinRT_String: ...
    @winrt_commethod(183)
    def GetOrientationCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationOrientation: ...
    @winrt_commethod(184)
    def HasKeyboardFocusCore(self) -> Boolean: ...
    @winrt_commethod(185)
    def IsContentElementCore(self) -> Boolean: ...
    @winrt_commethod(186)
    def IsControlElementCore(self) -> Boolean: ...
    @winrt_commethod(187)
    def IsEnabledCore(self) -> Boolean: ...
    @winrt_commethod(188)
    def IsKeyboardFocusableCore(self) -> Boolean: ...
    @winrt_commethod(189)
    def IsOffscreenCore(self) -> Boolean: ...
    @winrt_commethod(190)
    def IsPasswordCore(self) -> Boolean: ...
    @winrt_commethod(191)
    def IsRequiredForFormCore(self) -> Boolean: ...
    @winrt_commethod(192)
    def SetFocusCore(self) -> Void: ...
    @winrt_commethod(193)
    def GetPeerFromPointCore(self, point: Windows.Foundation.Point) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(194)
    def GetLiveSettingCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationLiveSetting: ...
    @winrt_commethod(195)
    def ShowContextMenuCore(self) -> Void: ...
    @winrt_commethod(196)
    def GetControlledPeersCore(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(197)
    def NavigateCore(self, direction: Windows.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(198)
    def GetElementFromPointCore(self, pointInWindowCoordinates: Windows.Foundation.Point) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(199)
    def GetFocusedElementCore(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(200)
    def GetAnnotationsCore(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation]: ...
    @winrt_commethod(201)
    def GetPositionInSetCore(self) -> Int32: ...
    @winrt_commethod(202)
    def GetSizeOfSetCore(self) -> Int32: ...
    @winrt_commethod(203)
    def GetLevelCore(self) -> Int32: ...
    @winrt_commethod(204)
    def GetLandmarkTypeCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_commethod(205)
    def GetLocalizedLandmarkTypeCore(self) -> WinRT_String: ...
    @winrt_commethod(206)
    def IsPeripheralCore(self) -> Boolean: ...
    @winrt_commethod(207)
    def IsDataValidForFormCore(self) -> Boolean: ...
    @winrt_commethod(208)
    def GetFullDescriptionCore(self) -> WinRT_String: ...
    @winrt_commethod(209)
    def GetDescribedByCore(self) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(210)
    def GetFlowsToCore(self) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(211)
    def GetFlowsFromCore(self) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
    @winrt_commethod(212)
    def GetCultureCore(self) -> Int32: ...
    @winrt_commethod(213)
    def GetHeadingLevelCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
    @winrt_commethod(214)
    def IsDialogCore(self) -> Boolean: ...
    @winrt_classmethod
    def GenerateRawElementProviderRuntimeId(cls: Windows.UI.Xaml.Automation.Peers.IAutomationPeerStatics3) -> Windows.UI.Xaml.Automation.Peers.RawElementProviderRuntimeId: ...
    @winrt_classmethod
    def ListenerExists(cls: Windows.UI.Xaml.Automation.Peers.IAutomationPeerStatics, eventId: Windows.UI.Xaml.Automation.Peers.AutomationEvents) -> Boolean: ...
    EventsSource = property(get_EventsSource, put_EventsSource)
class AutomationPeerAnnotation(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    ClassId = 'Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation: ...
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
    TypeProperty = property(get_TypeProperty, None)
    PeerProperty = property(get_PeerProperty, None)
AutomationStructureChangeType = Int32
AutomationStructureChangeType_ChildAdded: AutomationStructureChangeType = 0
AutomationStructureChangeType_ChildRemoved: AutomationStructureChangeType = 1
AutomationStructureChangeType_ChildrenInvalidated: AutomationStructureChangeType = 2
AutomationStructureChangeType_ChildrenBulkAdded: AutomationStructureChangeType = 3
AutomationStructureChangeType_ChildrenBulkRemoved: AutomationStructureChangeType = 4
AutomationStructureChangeType_ChildrenReordered: AutomationStructureChangeType = 5
class ButtonAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer
    @winrt_commethod(119)
    def Invoke(self) -> Void: ...
class ButtonBaseAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class CalendarDatePickerAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    @winrt_commethod(121)
    def Invoke(self) -> Void: ...
    @winrt_commethod(122)
    def get_IsReadOnly(self) -> Boolean: ...
    @winrt_commethod(123)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(124)
    def SetValue(self, value: WinRT_String) -> Void: ...
    IsReadOnly = property(get_IsReadOnly, None)
    Value = property(get_Value, None)
class CaptureElementAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class CheckBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer
class ColorPickerSliderAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SliderAutomationPeer
class ColorSpectrumAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class ComboBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer
    @winrt_commethod(140)
    def get_IsReadOnly(self) -> Boolean: ...
    @winrt_commethod(141)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(142)
    def SetValue(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(143)
    def get_ExpandCollapseState(self) -> Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_commethod(144)
    def Collapse(self) -> Void: ...
    @winrt_commethod(145)
    def Expand(self) -> Void: ...
    @winrt_commethod(146)
    def get_IsModal(self) -> Boolean: ...
    @winrt_commethod(147)
    def get_IsTopmost(self) -> Boolean: ...
    @winrt_commethod(148)
    def get_Maximizable(self) -> Boolean: ...
    @winrt_commethod(149)
    def get_Minimizable(self) -> Boolean: ...
    @winrt_commethod(150)
    def get_InteractionState(self) -> Windows.UI.Xaml.Automation.WindowInteractionState: ...
    @winrt_commethod(151)
    def get_VisualState(self) -> Windows.UI.Xaml.Automation.WindowVisualState: ...
    @winrt_commethod(152)
    def Close(self) -> Void: ...
    @winrt_commethod(153)
    def SetVisualState(self, state: Windows.UI.Xaml.Automation.WindowVisualState) -> Void: ...
    @winrt_commethod(154)
    def WaitForInputIdle(self, milliseconds: Int32) -> Boolean: ...
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
class ComboBoxItemDataAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    @winrt_commethod(124)
    def ScrollIntoView(self) -> Void: ...
class DatePickerAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class DatePickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    ClassId = 'Windows.UI.Xaml.Automation.Peers.DatePickerFlyoutPresenterAutomationPeer'
class FlipViewAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer
class FlipViewItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class FlipViewItemDataAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    @winrt_commethod(124)
    def ScrollIntoView(self) -> Void: ...
class FlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class FrameworkElementAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.AutomationPeer
    @winrt_commethod(116)
    def get_Owner(self) -> Windows.UI.Xaml.UIElement: ...
    @winrt_classmethod
    def FromElement(cls: Windows.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeerStatics, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_classmethod
    def CreatePeerForElement(cls: Windows.UI.Xaml.Automation.Peers.IFrameworkElementAutomationPeerStatics, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    Owner = property(get_Owner, None)
class GridViewAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer
class GridViewHeaderItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer
class GridViewItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class GridViewItemDataAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    @winrt_commethod(124)
    def ScrollIntoView(self) -> Void: ...
class GroupItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class HubAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class HubSectionAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    @winrt_commethod(118)
    def ScrollIntoView(self) -> Void: ...
class HyperlinkButtonAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer
    @winrt_commethod(119)
    def Invoke(self) -> Void: ...
class IAppBarAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8b4acfeb-89fa-4f13-84-be-35-ca-5b-7c-95-90')
class IAppBarAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8360f4e2-e396-4517-af-5d-f4-cf-34-c5-4e-df')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.AppBar, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.AppBarAutomationPeer: ...
class IAppBarButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('443262b2-4f6d-4b76-9d-2e-3e-ff-77-7e-88-64')
class IAppBarButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('aef0342a-acb7-42dc-97-e3-84-70-71-86-5f-d6')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.AppBarButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.AppBarButtonAutomationPeer: ...
class IAppBarToggleButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8464efad-9655-4aff-95-50-63-ae-9e-c8-fe-9c')
class IAppBarToggleButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d6f9139d-02c1-4221-95-91-7d-4e-fe-b7-47-01')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.AppBarToggleButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.AppBarToggleButtonAutomationPeer: ...
class IAutoSuggestBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2f32c302-f99b-491d-97-26-a5-e1-81-64-3e-fa')
class IAutoSuggestBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('80046849-18e7-4475-b3-62-4b-bd-53-d2-45-62')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.AutoSuggestBox) -> Windows.UI.Xaml.Automation.Peers.AutoSuggestBoxAutomationPeer: ...
class IAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('35aac87a-62ee-4d3e-a2-4c-2b-c8-43-2d-68-b7')
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
    Guid = Guid('ea1f89c7-ebf5-4ab8-88-f7-68-0d-82-1d-ac-61')
class IAutomationPeer3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d3cfb977-0084-41d7-a2-21-28-15-8d-3b-c3-2c')
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
    Guid = Guid('761ce752-73c1-4f44-be-75-43-c4-9e-c0-d4-d5')
    @winrt_commethod(6)
    def GetLandmarkType(self) -> Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_commethod(7)
    def GetLocalizedLandmarkType(self) -> WinRT_String: ...
class IAutomationPeer5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f632e1c6-0a3f-4574-9f-ef-cd-c1-51-76-56-74')
    @winrt_commethod(6)
    def IsPeripheral(self) -> Boolean: ...
    @winrt_commethod(7)
    def IsDataValidForForm(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetFullDescription(self) -> WinRT_String: ...
class IAutomationPeer6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('caf8608f-13ff-42fb-86-6d-22-20-64-34-cc-6b')
    @winrt_commethod(6)
    def GetCulture(self) -> Int32: ...
class IAutomationPeer7(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('796b3287-e642-48ab-b2-23-52-08-b4-1d-a9-d6')
    @winrt_commethod(6)
    def RaiseNotificationEvent(self, notificationKind: Windows.UI.Xaml.Automation.Peers.AutomationNotificationKind, notificationProcessing: Windows.UI.Xaml.Automation.Peers.AutomationNotificationProcessing, displayString: WinRT_String, activityId: WinRT_String) -> Void: ...
class IAutomationPeer8(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5c6a1fe6-9a55-4d7f-94-98-cf-e4-29-e9-2d-a8')
    @winrt_commethod(6)
    def GetHeadingLevel(self) -> Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
class IAutomationPeer9(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('df2e0265-1d74-57fa-80-94-f8-1c-2f-62-6b-8c')
    @winrt_commethod(6)
    def IsDialog(self) -> Boolean: ...
class IAutomationPeerAnnotation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0c456061-52cf-43fa-82-f8-07-f1-37-35-1e-5a')
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
    Guid = Guid('f59c439e-c65b-43cd-90-09-03-fc-02-33-63-a7')
    @winrt_commethod(6)
    def CreateInstance(self, type: Windows.UI.Xaml.Automation.AnnotationType) -> Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation: ...
    @winrt_commethod(7)
    def CreateWithPeerParameter(self, type: Windows.UI.Xaml.Automation.AnnotationType, peer: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Windows.UI.Xaml.Automation.Peers.AutomationPeerAnnotation: ...
class IAutomationPeerAnnotationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8809a87d-09b2-4d45-b7-8b-1d-3b-3b-09-f6-61')
    @winrt_commethod(6)
    def get_TypeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PeerProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TypeProperty = property(get_TypeProperty, None)
    PeerProperty = property(get_PeerProperty, None)
class IAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('20c27545-a88b-43c8-bc-24-ce-a9-da-fd-04-a3')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
class IAutomationPeerOverrides(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bea93e67-dbee-4f7b-af-0d-a7-9a-ae-53-33-bf')
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
    Guid = Guid('2603682a-9da6-4023-b4-96-49-6e-5e-f2-28-d2')
    @winrt_commethod(6)
    def ShowContextMenuCore(self) -> Void: ...
    @winrt_commethod(7)
    def GetControlledPeersCore(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Automation.Peers.AutomationPeer]: ...
class IAutomationPeerOverrides3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b6f0c4ad-4d39-49e6-bb-91-d9-24-ee-fd-85-38')
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
    Guid = Guid('b186cda2-5d46-4bcd-a8-11-26-9a-d1-5b-3a-ee')
    @winrt_commethod(6)
    def GetLandmarkTypeCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationLandmarkType: ...
    @winrt_commethod(7)
    def GetLocalizedLandmarkTypeCore(self) -> WinRT_String: ...
class IAutomationPeerOverrides5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2c847c85-781e-49f7-9f-ef-b9-e1-4d-01-47-07')
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
    Guid = Guid('e98babe7-f6ff-444c-9c-0d-27-7e-af-0a-d9-c0')
    @winrt_commethod(6)
    def GetCultureCore(self) -> Int32: ...
class IAutomationPeerOverrides8(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0e1ebbd4-a003-4936-81-75-f5-45-7c-07-f0-c6')
    @winrt_commethod(6)
    def GetHeadingLevelCore(self) -> Windows.UI.Xaml.Automation.Peers.AutomationHeadingLevel: ...
class IAutomationPeerOverrides9(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f3709e8b-091a-5db5-b8-96-ff-78-f0-19-90-c9')
    @winrt_commethod(6)
    def IsDialogCore(self) -> Boolean: ...
class IAutomationPeerProtected(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f4b40e52-642f-4629-a5-4a-ea-5d-23-49-c4-48')
    @winrt_commethod(6)
    def PeerFromProvider(self, provider: Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(7)
    def ProviderFromPeer(self, peer: Windows.UI.Xaml.Automation.Peers.AutomationPeer) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class IAutomationPeerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('562f7fb0-a331-4a9c-9d-ec-bf-b7-58-6f-ff-ff')
    @winrt_commethod(6)
    def ListenerExists(self, eventId: Windows.UI.Xaml.Automation.Peers.AutomationEvents) -> Boolean: ...
class IAutomationPeerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('572c5714-7f87-4271-81-9f-6c-f4-c4-d0-22-d0')
    @winrt_commethod(6)
    def GenerateRawElementProviderRuntimeId(self) -> Windows.UI.Xaml.Automation.Peers.RawElementProviderRuntimeId: ...
class IButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fb77efbe-39ec-4508-8a-c3-51-a1-42-40-27-d7')
class IButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3fdb9f49-f4ab-4780-86-44-03-37-62-99-a1-75')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Button, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ButtonAutomationPeer: ...
class IButtonBaseAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a4f3b5b6-7585-4e0b-96-d2-08-cf-6f-28-be-fa')
class IButtonBaseAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8a04091e-e6b2-4c60-a7-59-c1-3c-a4-51-65-ed')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.ButtonBase, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer: ...
class ICalendarDatePickerAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('40d8938e-db5e-4b03-be-ba-d1-0f-62-41-97-87')
class ICalendarDatePickerAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ab705dd2-d293-45bf-9f-19-26-f7-60-3a-5e-9b')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.CalendarDatePicker, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.CalendarDatePickerAutomationPeer: ...
class ICaptureElementAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dcc44ee0-fa45-45c6-8b-b7-32-0d-80-8f-59-58')
class ICaptureElementAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9b92ef48-85e9-4869-b1-75-8f-7c-f4-5a-6d-9f')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.CaptureElement, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.CaptureElementAutomationPeer: ...
class ICheckBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eb15bc42-c0a9-46c6-ac-24-b8-3d-e4-29-c7-33')
class ICheckBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b75c775d-eb8f-44ef-a2-7c-e2-6a-c7-de-83-33')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.CheckBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.CheckBoxAutomationPeer: ...
class IColorPickerSliderAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a514215a-7293-4577-92-4c-47-d4-e0-bf-9b-90')
class IColorPickerSliderAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1a55c77e-9dd6-45a3-90-42-b4-02-00-fe-a1-a9')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.ColorPickerSlider, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ColorPickerSliderAutomationPeer: ...
class IColorSpectrumAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('15d5ba03-010d-4ff7-90-87-f4-dd-09-f8-31-b7')
class IColorSpectrumAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0ac400e1-b743-4496-83-7a-88-89-e6-ac-64-97')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.ColorSpectrum, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ColorSpectrumAutomationPeer: ...
class IComboBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7eb40d0b-75c5-4263-ba-6a-d4-a5-4f-b0-f2-39')
class IComboBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('098e5b0d-1b90-40b9-9b-e3-b2-32-67-eb-13-cf')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ComboBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ComboBoxAutomationPeer: ...
class IComboBoxItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('12ddc76e-9552-446a-82-ee-93-8c-c3-71-80-0f')
class IComboBoxItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('134ac7fc-397a-403f-a6-ec-1c-e8-be-da-15-e5')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ComboBoxItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ComboBoxItemAutomationPeer: ...
class IComboBoxItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4fef6df2-289c-4c04-83-1b-5a-66-8c-6d-71-04')
class IComboBoxItemDataAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('14a8d4f6-469a-41ba-9d-93-44-a1-a5-5d-a8-72')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.ComboBoxAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ComboBoxItemDataAutomationPeer: ...
class IDatePickerAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d07d357f-a0b9-45dc-99-1a-76-c5-05-e7-d0-f5')
class IDatePickerAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e5667d19-9157-4436-9f-4d-7f-b9-91-74-b4-8e')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.DatePicker, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.DatePickerAutomationPeer: ...
class IDatePickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('752aed38-c2bf-4880-82-b2-a6-c0-5e-90-c1-35')
class IFlipViewAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8ec0353a-4284-4b00-ae-f8-a2-68-8e-a5-e3-c4')
class IFlipViewAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4395ab0d-8d83-483c-88-eb-e2-61-7b-0d-29-3f')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.FlipView, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FlipViewAutomationPeer: ...
class IFlipViewItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c83034de-fa08-4bd3-ae-b2-d2-e5-bf-a0-4d-f9')
class IFlipViewItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('69109356-d0e5-4c10-a0-9c-ad-0b-f1-b0-cb-01')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.FlipViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FlipViewItemAutomationPeer: ...
class IFlipViewItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b0986175-00bc-4118-8a-6f-16-ee-9c-15-d9-68')
class IFlipViewItemDataAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3c864393-0aea-4e78-bc-11-b7-75-ca-c4-11-4c')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.FlipViewAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FlipViewItemDataAutomationPeer: ...
class IFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a01840b4-5fca-456f-98-ea-30-0e-b4-0b-58-5e')
class IFlyoutPresenterAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f350155f-8924-44c0-ba-44-65-3f-e7-9f-1e-fb')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.FlyoutPresenter, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FlyoutPresenterAutomationPeer: ...
class IFrameworkElementAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b90ad781-bfeb-4451-bd-47-9f-3a-63-eb-d2-4a')
    @winrt_commethod(6)
    def get_Owner(self) -> Windows.UI.Xaml.UIElement: ...
    Owner = property(get_Owner, None)
class IFrameworkElementAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0db9b8bc-b812-48e3-af-1f-db-c5-76-00-c3-25')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.FrameworkElement, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer: ...
class IFrameworkElementAutomationPeerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b9c0b997-2820-44a1-a5-a8-9b-80-1e-dc-26-9e')
    @winrt_commethod(6)
    def FromElement(self, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
    @winrt_commethod(7)
    def CreatePeerForElement(self, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Automation.Peers.AutomationPeer: ...
class IGridViewAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1c4401a4-d951-49ca-8f-82-c7-f3-c6-06-81-b0')
class IGridViewAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8aca59dd-22a7-4800-89-4b-c1-f4-85-f3-89-53')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.GridView, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GridViewAutomationPeer: ...
class IGridViewHeaderItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e3dcef3a-e08a-48e7-b2-3a-2b-e5-b6-6e-47-4e')
class IGridViewHeaderItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2c80b4d2-ffc2-4157-88-dd-59-cd-92-e3-97-15')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.GridViewHeaderItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GridViewHeaderItemAutomationPeer: ...
class IGridViewItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('93ef2d07-346c-4166-a4-ba-bc-6a-18-1e-7f-33')
class IGridViewItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fafec376-f22e-466d-91-3c-ae-24-cc-db-16-0f')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.GridViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GridViewItemAutomationPeer: ...
class IGridViewItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f3f4868f-29d4-4094-8c-54-ea-61-a8-82-94-a4')
class IGridViewItemDataAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a65e7a88-770d-402c-99-6f-67-50-6a-f2-a4-af')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.GridViewAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GridViewItemDataAutomationPeer: ...
class IGroupItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1914fe6d-0740-4236-9e-e1-38-cf-19-c1-c3-88')
class IGroupItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('56a64567-f21c-4c90-b3-79-15-a2-7c-7f-84-09')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.GroupItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.GroupItemAutomationPeer: ...
class IHubAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4ddee056-4ebc-4620-a0-5d-90-3e-3c-9a-4e-ad')
class IHubAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c762d43f-79dd-43ee-87-77-8d-08-b3-9a-a0-65')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Hub, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.HubAutomationPeer: ...
class IHubSectionAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('16d91ff7-7431-4d82-83-ce-cf-a3-19-2b-0f-18')
class IHubSectionAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c68e27e8-17ec-4329-91-ae-2d-0b-23-39-d4-98')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.HubSection, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.HubSectionAutomationPeer: ...
class IHyperlinkButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('aa7afcb1-0edf-46d9-aa-9e-0e-b2-1d-14-00-97')
class IHyperlinkButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('59bc1661-c182-49af-95-26-44-b8-8e-62-84-55')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.HyperlinkButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.HyperlinkButtonAutomationPeer: ...
class IImageAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9b0bbf8c-60a2-48bf-ab-2c-1a-52-a4-51-d2-d4')
class IImageAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('90304003-687d-47bf-b3-a2-4b-ab-ca-d8-ef-50')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Image, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ImageAutomationPeer: ...
class IInkToolbarAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('123baaa4-f2e8-4bcb-93-82-5d-fd-d1-1f-e4-5f')
class IItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('953c34f6-3b31-47a7-b3-bf-25-d3-ae-99-c3-17')
    @winrt_commethod(6)
    def get_Item(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_ItemsControlAutomationPeer(self) -> Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer: ...
    Item = property(get_Item, None)
    ItemsControlAutomationPeer = property(get_ItemsControlAutomationPeer, None)
class IItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('29065073-de3d-4d3f-97-b4-4d-6f-9d-53-44-4d')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
class IItemsControlAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('96e76bf1-37f7-4088-92-5d-65-26-8e-83-e3-4d')
class IItemsControlAutomationPeer2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c48d8917-95a8-47b8-a5-17-bf-89-1a-6c-03-9b')
    @winrt_commethod(6)
    def CreateItemAutomationPeer(self, item: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
class IItemsControlAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4038a259-2e1a-49ca-a5-33-c6-4f-18-15-77-e6')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ItemsControl, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer: ...
class IItemsControlAutomationPeerOverrides2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('361dc0e8-b56f-45e9-80-fe-10-a0-fb-0f-e1-77')
    @winrt_commethod(6)
    def OnCreateItemAutomationPeer(self, item: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
class IListBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8cd0d608-b402-4a6e-bd-9a-34-3f-88-45-eb-32')
class IListBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e2362185-7df6-49f7-8a-bc-4c-33-f1-a3-d4-6e')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListBoxAutomationPeer: ...
class IListBoxItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1bc6e1c6-2997-42df-99-eb-92-bc-1d-d1-49-fb')
class IListBoxItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('509f9dd8-b0aa-443f-a1-10-41-20-9a-f4-4f-1c')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListBoxItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListBoxItemAutomationPeer: ...
class IListBoxItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fd7d5fee-fde0-482a-80-84-dc-eb-ba-5b-98-06')
class IListBoxItemDataAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d7924e16-bd8d-4662-a9-95-20-ff-9a-05-60-93')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.ListBoxAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListBoxItemDataAutomationPeer: ...
class IListPickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('56dfdc58-2395-4060-80-47-8e-a4-63-69-8a-24')
class IListViewAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('73cecc87-c0dc-4260-91-48-75-e9-86-4a-72-30')
class IListViewAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('65f39174-eaa2-4e44-8b-e6-4c-ca-28-cd-02-88')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListView, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewAutomationPeer: ...
class IListViewBaseAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('87ec7649-b83d-4e55-9a-fd-bd-83-5e-74-8f-5c')
class IListViewBaseAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('70d3c2be-8950-4647-93-62-fd-00-2f-8f-f8-2e')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListViewBase, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer: ...
class IListViewBaseHeaderItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7cb8b732-c1f0-4a3c-bc-14-85-dd-48-de-db-85')
class IListViewBaseHeaderItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('40ec995f-d631-4004-83-2e-6d-86-43-e5-15-61')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListViewBaseHeaderItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer: ...
class IListViewHeaderItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('67ab1e4b-ad61-4c88-ba-45-0f-3a-8d-06-1f-8f')
class IListViewHeaderItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('07668694-2ca5-4be4-a8-b9-59-2d-48-f7-60-87')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListViewHeaderItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewHeaderItemAutomationPeer: ...
class IListViewItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ca114e70-a16d-4d09-a1-cf-18-56-ef-98-a9-ec')
class IListViewItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c47dfbc0-facc-4024-a7-3b-17-ec-4e-66-26-54')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ListViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer: ...
class IListViewItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('15a8d7fd-d7a5-4a6c-96-3c-6f-7c-e4-64-67-1a')
class IListViewItemDataAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d0db12bb-d715-4523-ac-c0-1e-10-72-d8-e3-2b')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ListViewItemDataAutomationPeer: ...
class ILoopingSelectorAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('50b406ca-bae9-4816-8a-3a-0c-b4-f9-64-78-a2')
class ILoopingSelectorItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d3fa68bf-04cf-4f4c-8d-3e-47-80-a1-9d-47-88')
class ILoopingSelectorItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ef567e32-7cd2-4d32-95-90-1f-58-8d-5e-f3-8d')
class IMapControlAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('425beee4-f2e8-4bcb-93-82-5d-fd-d1-1f-e4-5f')
class IMediaElementAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ba0b9fc2-a6e2-41a5-b1-7a-d1-59-46-13-ef-ba')
class IMediaElementAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b2ad3b28-7575-4173-9b-c7-80-36-7a-16-4e-d2')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.MediaElement, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MediaElementAutomationPeer: ...
class IMediaPlayerElementAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('02bed209-3f65-4fdd-b5-ca-c4-75-0d-4e-6e-a4')
class IMediaPlayerElementAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('08848077-82af-4d19-b1-70-28-2a-9e-0e-7f-37')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.MediaPlayerElement, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MediaPlayerElementAutomationPeer: ...
class IMediaTransportControlsAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a3ad8d93-79f8-4958-a3-c8-98-0d-ef-b8-3d-15')
class IMediaTransportControlsAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f41cb003-e103-4ab0-81-2a-a0-8f-bd-b5-70-ce')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.MediaTransportControls, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MediaTransportControlsAutomationPeer: ...
class IMenuBarAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4b6adcf1-f274-5592-85-a8-7b-09-9e-99-b3-20')
class IMenuBarAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2a094871-4a9b-5a0b-9f-da-7b-c3-ae-95-7c-53')
    @winrt_commethod(6)
    def CreateInstance(self, owner: Windows.UI.Xaml.Controls.MenuBar, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MenuBarAutomationPeer: ...
class IMenuBarItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0fce49b4-cff5-5c4b-98-ee-e7-5f-dd-df-79-9a')
class IMenuBarItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c9c77746-130f-5b19-83-a6-61-db-58-46-13-aa')
    @winrt_commethod(6)
    def CreateInstance(self, owner: Windows.UI.Xaml.Controls.MenuBarItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MenuBarItemAutomationPeer: ...
class IMenuFlyoutItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1fc19462-21df-456e-aa-11-8f-ac-6b-4b-2a-f6')
class IMenuFlyoutItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d08bfcb8-20d1-45d8-a2-c2-2f-13-0d-f7-14-e0')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.MenuFlyoutItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MenuFlyoutItemAutomationPeer: ...
class IMenuFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e244a871-fcbb-48fc-8a-93-41-ea-13-4b-53-ce')
class IMenuFlyoutPresenterAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('07b5172d-761d-452b-9e-6d-fa-2a-8b-e0-ad-26')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.MenuFlyoutPresenter, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.MenuFlyoutPresenterAutomationPeer: ...
class INavigationViewItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('309847a5-9971-4d8d-a8-1c-08-5c-70-86-a1-b9')
class INavigationViewItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0bc2835d-aa38-4f97-96-64-e6-fc-82-1d-81-ed')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.NavigationViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.NavigationViewItemAutomationPeer: ...
class IPasswordBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('684f065e-3df3-4b9f-82-ad-88-19-db-3b-21-8a')
class IPasswordBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ac3d7ede-dca4-481c-b5-20-4a-9b-3f-3b-17-9c')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.PasswordBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.PasswordBoxAutomationPeer: ...
class IPersonPictureAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('27156d4c-a66f-4aaf-82-86-4f-79-6d-30-62-8c')
class IPersonPictureAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a95f1f6d-2524-44a4-97-fd-11-81-13-01-00-ad')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.PersonPicture, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.PersonPictureAutomationPeer: ...
class IPickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('28414bf7-8382-4eae-93-c1-d6-f0-35-aa-81-55')
class IPivotAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e715a8f8-3b9d-402c-81-e2-6e-91-2e-f5-89-81')
class IPivotAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3efe0f94-0c91-4341-b9-ac-1b-56-b4-e6-b8-4f')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Pivot) -> Windows.UI.Xaml.Automation.Peers.PivotAutomationPeer: ...
class IPivotItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1a4241ad-5d55-4d27-b4-0f-2d-37-50-6f-be-78')
class IPivotItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f2810471-183f-416b-b4-1a-1e-5a-95-8a-91-f4')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.PivotItem) -> Windows.UI.Xaml.Automation.Peers.PivotItemAutomationPeer: ...
class IPivotItemDataAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a2a3b788-ea1d-48b7-88-ee-f0-8b-6a-a0-7f-ee')
class IPivotItemDataAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('517a2480-d3b6-412e-82-b6-94-a0-a8-4c-13-b0')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.PivotAutomationPeer) -> Windows.UI.Xaml.Automation.Peers.PivotItemDataAutomationPeer: ...
class IProgressBarAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('93f48f86-d840-4fb6-ac-2f-5f-77-9b-85-4b-0d')
class IProgressBarAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('364679ab-b80f-41b4-8e-ea-2f-52-51-bc-73-9c')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ProgressBar, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ProgressBarAutomationPeer: ...
class IProgressRingAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bc305eee-39d3-4eeb-ac-33-23-94-de-12-3e-2e')
class IProgressRingAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f3db204b-157e-40bc-95-93-55-bc-5c-71-a4-f6')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ProgressRing, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ProgressRingAutomationPeer: ...
class IRadioButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7e6a5ed8-0b30-4743-b1-02-dc-df-54-8e-31-31')
class IRadioButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4940c4fd-3d88-49ca-8f-31-92-41-87-af-0b-fe')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.RadioButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RadioButtonAutomationPeer: ...
class IRangeBaseAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e454b549-4b2c-42ad-b0-4b-d3-59-47-d1-ee-50')
class IRangeBaseAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('827c7601-3078-4479-95-ea-91-37-4c-a0-62-07')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.RangeBase, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer: ...
class IRatingControlAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d14349a-9963-4a47-82-3c-f4-57-cb-32-09-d5')
class IRatingControlAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f179f272-9846-4632-8b-9c-be-6f-a8-d3-c9-bb')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.RatingControl, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RatingControlAutomationPeer: ...
class IRepeatButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('29e41ad5-a8ac-4e8a-83-d8-09-e3-7e-05-42-57')
class IRepeatButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6a6ff9d4-575e-4e60-bd-d6-ec-14-41-9b-4f-f6')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.RepeatButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RepeatButtonAutomationPeer: ...
class IRichEditBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c69f5c04-16ee-467a-a8-33-c3-da-84-58-ad-64')
class IRichEditBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('752c8399-d296-4d87-90-20-a4-75-0e-88-5b-3c')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.RichEditBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RichEditBoxAutomationPeer: ...
class IRichTextBlockAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('93a01a9c-9609-41fa-82-f3-90-9c-09-f4-9a-72')
class IRichTextBlockAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2038ae61-1389-467a-ae-d6-37-33-4d-a9-62-2b')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.RichTextBlock, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RichTextBlockAutomationPeer: ...
class IRichTextBlockOverflowAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8c9a409a-2736-437b-ab-36-a1-6a-20-2f-10-5d')
class IRichTextBlockOverflowAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bd5eb663-2c14-4665-ad-ef-f2-b0-33-94-7b-eb')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.RichTextBlockOverflow, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.RichTextBlockOverflowAutomationPeer: ...
class IScrollBarAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('69e0c369-bbe7-41f2-87-ca-aa-d8-13-fe-55-0e')
class IScrollBarAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e1302110-afeb-4595-8e-3d-ed-c0-84-4a-2b-21')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.ScrollBar, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ScrollBarAutomationPeer: ...
class IScrollViewerAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d985f259-1b09-4e88-88-fd-42-17-50-dc-6b-45')
class IScrollViewerAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('270dff7d-d96d-48f9-a3-6a-c2-52-aa-9c-46-70')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ScrollViewer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ScrollViewerAutomationPeer: ...
class ISearchBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('854011a4-18a6-4f30-93-9b-88-71-af-a3-f5-e9')
class ISearchBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b3c01430-7faa-41bb-8e-91-7c-76-1c-52-67-f1')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.SearchBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SearchBoxAutomationPeer: ...
class ISelectorAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('162ac829-7115-43ec-b3-83-a7-b7-16-44-06-9d')
class ISelectorAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7b525646-829b-4dcc-bd-52-5a-8d-03-99-38-7a')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.Selector, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer: ...
class ISelectorItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ae8b3477-860a-45bb-bf-7c-e1-b2-74-19-d1-dd')
class ISelectorItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('66d7edfb-786d-4362-a9-64-eb-fb-21-77-6c-30')
    @winrt_commethod(6)
    def CreateInstanceWithParentAndItem(self, item: Windows.Win32.System.WinRT.IInspectable_head, parent: Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer: ...
class ISemanticZoomAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3c2fac6c-a977-47fc-b4-4e-27-54-c0-b2-be-a9')
class ISemanticZoomAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f518d44d-a493-4496-b0-77-96-74-c7-f4-c5-fa')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.SemanticZoom, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SemanticZoomAutomationPeer: ...
class ISettingsFlyoutAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d0de0cdb-30cf-47a6-a5-eb-9c-77-f0-b0-d6-dd')
class ISettingsFlyoutAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f94762bd-8a14-40e4-94-a7-3f-33-c9-22-e9-45')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.SettingsFlyout, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SettingsFlyoutAutomationPeer: ...
class ISliderAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ec30015a-d611-46d0-ae-4f-6e-cf-27-df-ba-a5')
class ISliderAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('971b8056-9a7a-4df9-95-fa-6f-5c-04-c9-1c-ac')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Slider, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.SliderAutomationPeer: ...
class ITextBlockAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('be2057f5-6715-4e69-a0-50-92-bd-0c-e2-32-a9')
class ITextBlockAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('76bf924b-7ca0-4b01-bc-5c-a8-cf-4d-36-91-de')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.TextBlock, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TextBlockAutomationPeer: ...
class ITextBoxAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3a4f1ca0-5e5d-4d26-90-67-e7-40-bf-65-7a-9f')
class ITextBoxAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('01f0c067-966b-4130-b8-72-46-9e-42-bd-4a-7f')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.TextBox, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TextBoxAutomationPeer: ...
class IThumbAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dc2949b5-b45e-4d6d-89-2f-d9-42-2c-95-0e-fb')
class IThumbAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('970743ff-af41-4600-b5-5d-26-d4-3d-f8-60-e1')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.Thumb, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ThumbAutomationPeer: ...
class ITimePickerAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a43d44ef-3285-4df7-b4-a4-e4-cd-f3-6a-3a-17')
class ITimePickerAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('978f6671-47f8-40a7-9e-21-68-12-8b-16-b4-fd')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.TimePicker, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TimePickerAutomationPeer: ...
class ITimePickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('da93ee27-82f1-4701-87-06-be-29-7b-f0-60-43')
class IToggleButtonAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('62dbe6c5-bc0a-45bb-bf-77-ea-0f-15-02-89-1f')
class IToggleButtonAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c9218cc4-ad4b-4d03-a6-a4-7d-59-e6-36-00-04')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.Primitives.ToggleButton, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer: ...
class IToggleMenuFlyoutItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6b57eafe-6af1-4903-83-73-34-37-bf-35-23-45')
class IToggleMenuFlyoutItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('94364b77-8f6c-4837-aa-e3-94-d0-10-d8-d1-62')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ToggleMenuFlyoutItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ToggleMenuFlyoutItemAutomationPeer: ...
class IToggleSwitchAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c011f174-e89e-4790-bf-9a-78-eb-b5-f5-9e-9f')
class IToggleSwitchAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('31f933e3-fef8-4419-9d-f5-d9-ef-71-96-ea-34')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.ToggleSwitch, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.ToggleSwitchAutomationPeer: ...
class ITreeViewItemAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2331d648-b617-437f-92-0c-71-d4-50-50-3e-65')
class ITreeViewItemAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('73d388bf-1d01-4159-82-c0-2b-29-96-db-fd-ce')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.TreeViewItem, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TreeViewItemAutomationPeer: ...
class ITreeViewListAutomationPeer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('71c1b5bc-bb29-4479-a8-a8-60-6b-e6-b8-23-ae')
class ITreeViewListAutomationPeerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('00f597e2-f811-475a-bf-e6-29-0f-e7-07-fa-88')
    @winrt_commethod(6)
    def CreateInstanceWithOwner(self, owner: Windows.UI.Xaml.Controls.TreeViewList, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Automation.Peers.TreeViewListAutomationPeer: ...
class ImageAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class InkToolbarAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    ClassId = 'Windows.UI.Xaml.Automation.Peers.InkToolbarAutomationPeer'
class ItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.AutomationPeer
    @winrt_commethod(116)
    def get_Item(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(117)
    def get_ItemsControlAutomationPeer(self) -> Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer: ...
    @winrt_commethod(118)
    def Realize(self) -> Void: ...
    Item = property(get_Item, None)
    ItemsControlAutomationPeer = property(get_ItemsControlAutomationPeer, None)
class ItemsControlAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    @winrt_commethod(120)
    def CreateItemAutomationPeer(self, item: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
    @winrt_commethod(121)
    def OnCreateItemAutomationPeer(self, item: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer: ...
    @winrt_commethod(122)
    def FindItemByProperty(self, startAfter: Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple, automationProperty: Windows.UI.Xaml.Automation.AutomationProperty, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class ListBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer
class ListBoxItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class ListBoxItemDataAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    @winrt_commethod(124)
    def ScrollIntoView(self) -> Void: ...
class ListPickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    ClassId = 'Windows.UI.Xaml.Automation.Peers.ListPickerFlyoutPresenterAutomationPeer'
class ListViewAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ListViewBaseAutomationPeer
class ListViewBaseAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer
    @winrt_commethod(127)
    def get_DropEffect(self) -> WinRT_String: ...
    @winrt_commethod(128)
    def get_DropEffects(self) -> POINTER(WinRT_String): ...
    DropEffect = property(get_DropEffect, None)
    DropEffects = property(get_DropEffects, None)
class ListViewBaseHeaderItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class ListViewHeaderItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ListViewBaseHeaderItemAutomationPeer
class ListViewItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class ListViewItemDataAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorItemAutomationPeer
    @winrt_commethod(124)
    def ScrollIntoView(self) -> Void: ...
class LoopingSelectorAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    ClassId = 'Windows.UI.Xaml.Automation.Peers.LoopingSelectorAutomationPeer'
    @winrt_mixinmethod
    def get_CanSelectMultiple(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSelectionRequired(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def GetSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
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
    ClassId = 'Windows.UI.Xaml.Automation.Peers.LoopingSelectorItemAutomationPeer'
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
    ClassId = 'Windows.UI.Xaml.Automation.Peers.LoopingSelectorItemDataAutomationPeer'
    @winrt_mixinmethod
    def Realize(self: Windows.UI.Xaml.Automation.Provider.IVirtualizedItemProvider) -> Void: ...
class MapControlAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    ClassId = 'Windows.UI.Xaml.Automation.Peers.MapControlAutomationPeer'
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
class MediaPlayerElementAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class MediaTransportControlsAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class MenuBarAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class MenuBarItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    @winrt_commethod(121)
    def get_ExpandCollapseState(self) -> Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_commethod(122)
    def Collapse(self) -> Void: ...
    @winrt_commethod(123)
    def Expand(self) -> Void: ...
    @winrt_commethod(124)
    def Invoke(self) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class MenuFlyoutItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    @winrt_commethod(118)
    def Invoke(self) -> Void: ...
class MenuFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer
class NavigationViewItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer
class PasswordBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
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
class PickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    ClassId = 'Windows.UI.Xaml.Automation.Peers.PickerFlyoutPresenterAutomationPeer'
class PivotAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer
    ClassId = 'Windows.UI.Xaml.Automation.Peers.PivotAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IPivotAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.Pivot) -> Windows.UI.Xaml.Automation.Peers.PivotAutomationPeer: ...
    @winrt_mixinmethod
    def get_CanSelectMultiple(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSelectionRequired(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_mixinmethod
    def GetSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
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
    ClassId = 'Windows.UI.Xaml.Automation.Peers.PivotItemAutomationPeer'
    @winrt_factorymethod
    def CreateInstanceWithOwner(cls: Windows.UI.Xaml.Automation.Peers.IPivotItemAutomationPeerFactory, owner: Windows.UI.Xaml.Controls.PivotItem) -> Windows.UI.Xaml.Automation.Peers.PivotItemAutomationPeer: ...
class PivotItemDataAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer
    ClassId = 'Windows.UI.Xaml.Automation.Peers.PivotItemDataAutomationPeer'
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
class ProgressRingAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class RadioButtonAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ToggleButtonAutomationPeer
    @winrt_commethod(126)
    def get_IsSelected(self) -> Boolean: ...
    @winrt_commethod(127)
    def get_SelectionContainer(self) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(128)
    def AddToSelection(self) -> Void: ...
    @winrt_commethod(129)
    def RemoveFromSelection(self) -> Void: ...
    @winrt_commethod(130)
    def Select(self) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class RangeBaseAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    @winrt_commethod(124)
    def get_IsReadOnly(self) -> Boolean: ...
    @winrt_commethod(125)
    def get_LargeChange(self) -> Double: ...
    @winrt_commethod(126)
    def get_Maximum(self) -> Double: ...
    @winrt_commethod(127)
    def get_Minimum(self) -> Double: ...
    @winrt_commethod(128)
    def get_SmallChange(self) -> Double: ...
    @winrt_commethod(129)
    def get_Value(self) -> Double: ...
    @winrt_commethod(130)
    def SetValue(self, value: Double) -> Void: ...
    IsReadOnly = property(get_IsReadOnly, None)
    LargeChange = property(get_LargeChange, None)
    Maximum = property(get_Maximum, None)
    Minimum = property(get_Minimum, None)
    SmallChange = property(get_SmallChange, None)
    Value = property(get_Value, None)
class RatingControlAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class RawElementProviderRuntimeId(EasyCastStructure):
    Part1: UInt32
    Part2: UInt32
class RepeatButtonAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer
    @winrt_commethod(119)
    def Invoke(self) -> Void: ...
class RichEditBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class RichTextBlockAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class RichTextBlockOverflowAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class ScrollBarAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer
class ScrollViewerAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    @winrt_commethod(125)
    def get_HorizontallyScrollable(self) -> Boolean: ...
    @winrt_commethod(126)
    def get_HorizontalScrollPercent(self) -> Double: ...
    @winrt_commethod(127)
    def get_HorizontalViewSize(self) -> Double: ...
    @winrt_commethod(128)
    def get_VerticallyScrollable(self) -> Boolean: ...
    @winrt_commethod(129)
    def get_VerticalScrollPercent(self) -> Double: ...
    @winrt_commethod(130)
    def get_VerticalViewSize(self) -> Double: ...
    @winrt_commethod(131)
    def Scroll(self, horizontalAmount: Windows.UI.Xaml.Automation.ScrollAmount, verticalAmount: Windows.UI.Xaml.Automation.ScrollAmount) -> Void: ...
    @winrt_commethod(132)
    def SetScrollPercent(self, horizontalPercent: Double, verticalPercent: Double) -> Void: ...
    HorizontallyScrollable = property(get_HorizontallyScrollable, None)
    HorizontalScrollPercent = property(get_HorizontalScrollPercent, None)
    HorizontalViewSize = property(get_HorizontalViewSize, None)
    VerticallyScrollable = property(get_VerticallyScrollable, None)
    VerticalScrollPercent = property(get_VerticalScrollPercent, None)
    VerticalViewSize = property(get_VerticalViewSize, None)
class SearchBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class SelectorAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ItemsControlAutomationPeer
    @winrt_commethod(124)
    def get_CanSelectMultiple(self) -> Boolean: ...
    @winrt_commethod(125)
    def get_IsSelectionRequired(self) -> Boolean: ...
    @winrt_commethod(126)
    def GetSelection(self) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
    CanSelectMultiple = property(get_CanSelectMultiple, None)
    IsSelectionRequired = property(get_IsSelectionRequired, None)
class SelectorItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ItemAutomationPeer
    @winrt_commethod(122)
    def get_IsSelected(self) -> Boolean: ...
    @winrt_commethod(123)
    def get_SelectionContainer(self) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(124)
    def AddToSelection(self) -> Void: ...
    @winrt_commethod(125)
    def RemoveFromSelection(self) -> Void: ...
    @winrt_commethod(126)
    def Select(self) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class SemanticZoomAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    @winrt_commethod(119)
    def get_ToggleState(self) -> Windows.UI.Xaml.Automation.ToggleState: ...
    @winrt_commethod(120)
    def Toggle(self) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class SettingsFlyoutAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class SliderAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.RangeBaseAutomationPeer
class TextBlockAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class TextBoxAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class ThumbAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class TimePickerAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
class TimePickerFlyoutPresenterAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    ClassId = 'Windows.UI.Xaml.Automation.Peers.TimePickerFlyoutPresenterAutomationPeer'
class ToggleButtonAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ButtonBaseAutomationPeer
    @winrt_commethod(120)
    def get_ToggleState(self) -> Windows.UI.Xaml.Automation.ToggleState: ...
    @winrt_commethod(121)
    def Toggle(self) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class ToggleMenuFlyoutItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    @winrt_commethod(119)
    def get_ToggleState(self) -> Windows.UI.Xaml.Automation.ToggleState: ...
    @winrt_commethod(120)
    def Toggle(self) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class ToggleSwitchAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.FrameworkElementAutomationPeer
    @winrt_commethod(119)
    def get_ToggleState(self) -> Windows.UI.Xaml.Automation.ToggleState: ...
    @winrt_commethod(120)
    def Toggle(self) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class TreeViewItemAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.ListViewItemAutomationPeer
    @winrt_commethod(121)
    def get_ExpandCollapseState(self) -> Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_commethod(122)
    def Collapse(self) -> Void: ...
    @winrt_commethod(123)
    def Expand(self) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class TreeViewListAutomationPeer(ComPtr):
    extends: Windows.UI.Xaml.Automation.Peers.SelectorAutomationPeer
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
