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
import Windows.UI
import Windows.UI.Xaml.Automation
import Windows.UI.Xaml.Automation.Peers
import Windows.UI.Xaml.Automation.Provider
import Windows.UI.Xaml.Automation.Text
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IAnnotationProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('95ba1417-4437-451b-94-61-05-0a-49-b5-9d-06')
    @winrt_commethod(6)
    def get_AnnotationTypeId(self) -> Int32: ...
    @winrt_commethod(7)
    def get_AnnotationTypeName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Author(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DateTime(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Target(self) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    AnnotationTypeId = property(get_AnnotationTypeId, None)
    AnnotationTypeName = property(get_AnnotationTypeName, None)
    Author = property(get_Author, None)
    DateTime = property(get_DateTime, None)
    Target = property(get_Target, None)
class ICustomNavigationProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2bd8a6d0-2fa3-4717-b2-8c-49-17-ce-54-92-8d')
    @winrt_commethod(6)
    def NavigateCustom(self, direction: Windows.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class IDockProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('48c243f8-78b1-44a0-ac-5f-75-07-57-bc-de-3c')
    @winrt_commethod(6)
    def get_DockPosition(self) -> Windows.UI.Xaml.Automation.DockPosition: ...
    @winrt_commethod(7)
    def SetDockPosition(self, dockPosition: Windows.UI.Xaml.Automation.DockPosition) -> Void: ...
    DockPosition = property(get_DockPosition, None)
class IDragProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2e7786a9-7ffc-4f57-b9-65-1e-f1-f3-73-f5-46')
    @winrt_commethod(6)
    def get_IsGrabbed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_DropEffect(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DropEffects(self) -> POINTER(WinRT_String): ...
    @winrt_commethod(9)
    def GetGrabbedItems(self) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
    IsGrabbed = property(get_IsGrabbed, None)
    DropEffect = property(get_DropEffect, None)
    DropEffects = property(get_DropEffects, None)
class IDropTargetProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7a245bdd-b458-4fe0-98-c8-aa-c8-9d-f5-6d-61')
    @winrt_commethod(6)
    def get_DropEffect(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DropEffects(self) -> POINTER(WinRT_String): ...
    DropEffect = property(get_DropEffect, None)
    DropEffects = property(get_DropEffects, None)
class IExpandCollapseProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('49ac8399-d626-4543-94-b9-a6-d9-a9-59-3a-f6')
    @winrt_commethod(6)
    def get_ExpandCollapseState(self) -> Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_commethod(7)
    def Collapse(self) -> Void: ...
    @winrt_commethod(8)
    def Expand(self) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class IGridItemProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fff3683c-7407-45bb-a9-36-df-3e-d6-d3-83-7d')
    @winrt_commethod(6)
    def get_Column(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ColumnSpan(self) -> Int32: ...
    @winrt_commethod(8)
    def get_ContainingGrid(self) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(9)
    def get_Row(self) -> Int32: ...
    @winrt_commethod(10)
    def get_RowSpan(self) -> Int32: ...
    Column = property(get_Column, None)
    ColumnSpan = property(get_ColumnSpan, None)
    ContainingGrid = property(get_ContainingGrid, None)
    Row = property(get_Row, None)
    RowSpan = property(get_RowSpan, None)
class IGridProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8b62b7a0-932c-4490-9a-13-02-fd-b3-9a-8f-5b')
    @winrt_commethod(6)
    def get_ColumnCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_RowCount(self) -> Int32: ...
    @winrt_commethod(8)
    def GetItem(self, row: Int32, column: Int32) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    ColumnCount = property(get_ColumnCount, None)
    RowCount = property(get_RowCount, None)
class IIRawElementProviderSimple(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ec752224-9b77-4720-bb-21-4a-c8-9f-db-1a-fd')
class IInvokeProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f7d1a187-b13c-4540-b0-9e-67-78-e2-dc-9b-a5')
    @winrt_commethod(6)
    def Invoke(self) -> Void: ...
class IItemContainerProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ef5cd845-e1d4-40f4-ba-d5-c7-fa-d4-4a-70-3e')
    @winrt_commethod(6)
    def FindItemByProperty(self, startAfter: Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple, automationProperty: Windows.UI.Xaml.Automation.AutomationProperty, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class IMultipleViewProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d014e196-0e50-4843-a5-d2-c2-28-97-c8-84-5a')
    @winrt_commethod(6)
    def get_CurrentView(self) -> Int32: ...
    @winrt_commethod(7)
    def GetSupportedViews(self) -> POINTER(Int32): ...
    @winrt_commethod(8)
    def GetViewName(self, viewId: Int32) -> WinRT_String: ...
    @winrt_commethod(9)
    def SetCurrentView(self, viewId: Int32) -> Void: ...
    CurrentView = property(get_CurrentView, None)
class IObjectModelProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c3ca36b9-0793-4ed0-bb-f4-9f-f4-e0-f9-8f-80')
    @winrt_commethod(6)
    def GetUnderlyingObjectModel(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class IRangeValueProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('838a34a8-7d5f-4079-af-03-c3-d0-15-e9-34-13')
    @winrt_commethod(6)
    def get_IsReadOnly(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_LargeChange(self) -> Double: ...
    @winrt_commethod(8)
    def get_Maximum(self) -> Double: ...
    @winrt_commethod(9)
    def get_Minimum(self) -> Double: ...
    @winrt_commethod(10)
    def get_SmallChange(self) -> Double: ...
    @winrt_commethod(11)
    def get_Value(self) -> Double: ...
    @winrt_commethod(12)
    def SetValue(self, value: Double) -> Void: ...
    IsReadOnly = property(get_IsReadOnly, None)
    LargeChange = property(get_LargeChange, None)
    Maximum = property(get_Maximum, None)
    Minimum = property(get_Minimum, None)
    SmallChange = property(get_SmallChange, None)
    Value = property(get_Value, None)
class IRawElementProviderSimple(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    ClassId = 'Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple'
class IScrollItemProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9a3ec090-5d2c-4e42-9e-e6-9d-58-db-10-0b-55')
    @winrt_commethod(6)
    def ScrollIntoView(self) -> Void: ...
class IScrollProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('374bf581-7716-4bbc-82-eb-d9-97-00-6e-a9-99')
    @winrt_commethod(6)
    def get_HorizontallyScrollable(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_HorizontalScrollPercent(self) -> Double: ...
    @winrt_commethod(8)
    def get_HorizontalViewSize(self) -> Double: ...
    @winrt_commethod(9)
    def get_VerticallyScrollable(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_VerticalScrollPercent(self) -> Double: ...
    @winrt_commethod(11)
    def get_VerticalViewSize(self) -> Double: ...
    @winrt_commethod(12)
    def Scroll(self, horizontalAmount: Windows.UI.Xaml.Automation.ScrollAmount, verticalAmount: Windows.UI.Xaml.Automation.ScrollAmount) -> Void: ...
    @winrt_commethod(13)
    def SetScrollPercent(self, horizontalPercent: Double, verticalPercent: Double) -> Void: ...
    HorizontallyScrollable = property(get_HorizontallyScrollable, None)
    HorizontalScrollPercent = property(get_HorizontalScrollPercent, None)
    HorizontalViewSize = property(get_HorizontalViewSize, None)
    VerticallyScrollable = property(get_VerticallyScrollable, None)
    VerticalScrollPercent = property(get_VerticalScrollPercent, None)
    VerticalViewSize = property(get_VerticalViewSize, None)
class ISelectionItemProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6a4977c1-830d-42d2-bf-62-04-2e-bd-de-cc-19')
    @winrt_commethod(6)
    def get_IsSelected(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SelectionContainer(self) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(8)
    def AddToSelection(self) -> Void: ...
    @winrt_commethod(9)
    def RemoveFromSelection(self) -> Void: ...
    @winrt_commethod(10)
    def Select(self) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class ISelectionProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1f018fca-b944-4395-8d-e1-88-f6-74-af-51-d3')
    @winrt_commethod(6)
    def get_CanSelectMultiple(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsSelectionRequired(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetSelection(self) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
    CanSelectMultiple = property(get_CanSelectMultiple, None)
    IsSelectionRequired = property(get_IsSelectionRequired, None)
class ISpreadsheetItemProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ebde8f92-6015-4826-b7-19-47-52-1a-81-c6-7e')
    @winrt_commethod(6)
    def get_Formula(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetAnnotationObjects(self) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
    @winrt_commethod(8)
    def GetAnnotationTypes(self) -> POINTER(Windows.UI.Xaml.Automation.AnnotationType): ...
    Formula = property(get_Formula, None)
class ISpreadsheetProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('15359093-bd99-4cfd-9f-07-3b-14-b3-15-e2-3d')
    @winrt_commethod(6)
    def GetItemByName(self, name: WinRT_String) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class IStylesProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1a5b7a17-7c01-4bec-9c-d4-2d-fa-7d-c2-46-cd')
    @winrt_commethod(6)
    def get_ExtendedProperties(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FillColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(8)
    def get_FillPatternColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(9)
    def get_FillPatternStyle(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Shape(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_StyleId(self) -> Int32: ...
    @winrt_commethod(12)
    def get_StyleName(self) -> WinRT_String: ...
    ExtendedProperties = property(get_ExtendedProperties, None)
    FillColor = property(get_FillColor, None)
    FillPatternColor = property(get_FillPatternColor, None)
    FillPatternStyle = property(get_FillPatternStyle, None)
    Shape = property(get_Shape, None)
    StyleId = property(get_StyleId, None)
    StyleName = property(get_StyleName, None)
class ISynchronizedInputProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3d60cecb-da54-4aa3-b9-15-e3-24-44-27-d4-ac')
    @winrt_commethod(6)
    def Cancel(self) -> Void: ...
    @winrt_commethod(7)
    def StartListening(self, inputType: Windows.UI.Xaml.Automation.SynchronizedInputType) -> Void: ...
class ITableItemProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3b2c49cd-1de2-4ee2-a3-e1-fb-55-35-59-d1-5d')
    @winrt_commethod(6)
    def GetColumnHeaderItems(self) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
    @winrt_commethod(7)
    def GetRowHeaderItems(self) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
class ITableProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7a8ed399-6824-4595-ba-b3-46-4b-c9-a0-44-17')
    @winrt_commethod(6)
    def get_RowOrColumnMajor(self) -> Windows.UI.Xaml.Automation.RowOrColumnMajor: ...
    @winrt_commethod(7)
    def GetColumnHeaders(self) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
    @winrt_commethod(8)
    def GetRowHeaders(self) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
    RowOrColumnMajor = property(get_RowOrColumnMajor, None)
class ITextChildProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1133c336-a89b-4130-9b-e6-55-e3-33-34-f5-57')
    @winrt_commethod(6)
    def get_TextContainer(self) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(7)
    def get_TextRange(self) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    TextContainer = property(get_TextContainer, None)
    TextRange = property(get_TextRange, None)
class ITextEditProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ea3605b4-3a05-400e-b5-f9-4e-91-b4-0f-61-76')
    @winrt_commethod(6)
    def GetActiveComposition(self) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def GetConversionTarget(self) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
class ITextProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('db5bbc9f-4807-4f2a-86-78-1b-13-f3-c6-0e-22')
    @winrt_commethod(6)
    def get_DocumentRange(self) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def get_SupportedTextSelection(self) -> Windows.UI.Xaml.Automation.SupportedTextSelection: ...
    @winrt_commethod(8)
    def GetSelection(self) -> POINTER(Windows.UI.Xaml.Automation.Provider.ITextRangeProvider): ...
    @winrt_commethod(9)
    def GetVisibleRanges(self) -> POINTER(Windows.UI.Xaml.Automation.Provider.ITextRangeProvider): ...
    @winrt_commethod(10)
    def RangeFromChild(self, childElement: Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(11)
    def RangeFromPoint(self, screenLocation: Windows.Foundation.Point) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    DocumentRange = property(get_DocumentRange, None)
    SupportedTextSelection = property(get_SupportedTextSelection, None)
class ITextProvider2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('df1d48bc-0487-4e7f-9d-5e-f0-9e-77-e4-12-46')
    @winrt_commethod(6)
    def RangeFromAnnotation(self, annotationElement: Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def GetCaretRange(self, isActive: POINTER(Boolean)) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
class ITextRangeProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0274688d-06e9-4f66-94-46-28-a5-be-98-fb-d0')
    @winrt_commethod(6)
    def Clone(self) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def Compare(self, textRangeProvider: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider) -> Boolean: ...
    @winrt_commethod(8)
    def CompareEndpoints(self, endpoint: Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint, textRangeProvider: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, targetEndpoint: Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint) -> Int32: ...
    @winrt_commethod(9)
    def ExpandToEnclosingUnit(self, unit: Windows.UI.Xaml.Automation.Text.TextUnit) -> Void: ...
    @winrt_commethod(10)
    def FindAttribute(self, attributeId: Int32, value: Windows.Win32.System.WinRT.IInspectable_head, backward: Boolean) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(11)
    def FindText(self, text: WinRT_String, backward: Boolean, ignoreCase: Boolean) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(12)
    def GetAttributeValue(self, attributeId: Int32) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(13)
    def GetBoundingRectangles(self, returnValue: POINTER(POINTER(Double))) -> Void: ...
    @winrt_commethod(14)
    def GetEnclosingElement(self) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(15)
    def GetText(self, maxLength: Int32) -> WinRT_String: ...
    @winrt_commethod(16)
    def Move(self, unit: Windows.UI.Xaml.Automation.Text.TextUnit, count: Int32) -> Int32: ...
    @winrt_commethod(17)
    def MoveEndpointByUnit(self, endpoint: Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint, unit: Windows.UI.Xaml.Automation.Text.TextUnit, count: Int32) -> Int32: ...
    @winrt_commethod(18)
    def MoveEndpointByRange(self, endpoint: Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint, textRangeProvider: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, targetEndpoint: Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint) -> Void: ...
    @winrt_commethod(19)
    def Select(self) -> Void: ...
    @winrt_commethod(20)
    def AddToSelection(self) -> Void: ...
    @winrt_commethod(21)
    def RemoveFromSelection(self) -> Void: ...
    @winrt_commethod(22)
    def ScrollIntoView(self, alignToTop: Boolean) -> Void: ...
    @winrt_commethod(23)
    def GetChildren(self) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
class ITextRangeProvider2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d3be3dfb-9f54-4642-a7-a5-5c-18-d5-ee-2a-3f')
    @winrt_commethod(6)
    def ShowContextMenu(self) -> Void: ...
class IToggleProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('93b88290-656f-44f7-ae-af-78-b8-f9-44-d0-62')
    @winrt_commethod(6)
    def get_ToggleState(self) -> Windows.UI.Xaml.Automation.ToggleState: ...
    @winrt_commethod(7)
    def Toggle(self) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class ITransformProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('79670fdd-f6a9-4a65-af-17-86-1d-b7-99-a2-da')
    @winrt_commethod(6)
    def get_CanMove(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CanResize(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_CanRotate(self) -> Boolean: ...
    @winrt_commethod(9)
    def Move(self, x: Double, y: Double) -> Void: ...
    @winrt_commethod(10)
    def Resize(self, width: Double, height: Double) -> Void: ...
    @winrt_commethod(11)
    def Rotate(self, degrees: Double) -> Void: ...
    CanMove = property(get_CanMove, None)
    CanResize = property(get_CanResize, None)
    CanRotate = property(get_CanRotate, None)
class ITransformProvider2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a8b11756-a39f-4e97-8c-7d-c1-ea-8d-d6-33-c5')
    @winrt_commethod(6)
    def get_CanZoom(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ZoomLevel(self) -> Double: ...
    @winrt_commethod(8)
    def get_MaxZoom(self) -> Double: ...
    @winrt_commethod(9)
    def get_MinZoom(self) -> Double: ...
    @winrt_commethod(10)
    def Zoom(self, zoom: Double) -> Void: ...
    @winrt_commethod(11)
    def ZoomByUnit(self, zoomUnit: Windows.UI.Xaml.Automation.ZoomUnit) -> Void: ...
    CanZoom = property(get_CanZoom, None)
    ZoomLevel = property(get_ZoomLevel, None)
    MaxZoom = property(get_MaxZoom, None)
    MinZoom = property(get_MinZoom, None)
class IValueProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2086b7a7-ac0e-47d1-ab-9b-2a-64-29-2a-fd-f8')
    @winrt_commethod(6)
    def get_IsReadOnly(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetValue(self, value: WinRT_String) -> Void: ...
    IsReadOnly = property(get_IsReadOnly, None)
    Value = property(get_Value, None)
class IVirtualizedItemProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('17d4a04b-d658-48e0-a5-74-5a-51-6c-58-df-a7')
    @winrt_commethod(6)
    def Realize(self) -> Void: ...
class IWindowProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1baa8b3d-38cf-415a-85-d3-20-e4-3a-0e-c1-b1')
    @winrt_commethod(6)
    def get_IsModal(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsTopmost(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Maximizable(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Minimizable(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_InteractionState(self) -> Windows.UI.Xaml.Automation.WindowInteractionState: ...
    @winrt_commethod(11)
    def get_VisualState(self) -> Windows.UI.Xaml.Automation.WindowVisualState: ...
    @winrt_commethod(12)
    def Close(self) -> Void: ...
    @winrt_commethod(13)
    def SetVisualState(self, state: Windows.UI.Xaml.Automation.WindowVisualState) -> Void: ...
    @winrt_commethod(14)
    def WaitForInputIdle(self, milliseconds: Int32) -> Boolean: ...
    IsModal = property(get_IsModal, None)
    IsTopmost = property(get_IsTopmost, None)
    Maximizable = property(get_Maximizable, None)
    Minimizable = property(get_Minimizable, None)
    InteractionState = property(get_InteractionState, None)
    VisualState = property(get_VisualState, None)
make_head(_module, 'IAnnotationProvider')
make_head(_module, 'ICustomNavigationProvider')
make_head(_module, 'IDockProvider')
make_head(_module, 'IDragProvider')
make_head(_module, 'IDropTargetProvider')
make_head(_module, 'IExpandCollapseProvider')
make_head(_module, 'IGridItemProvider')
make_head(_module, 'IGridProvider')
make_head(_module, 'IIRawElementProviderSimple')
make_head(_module, 'IInvokeProvider')
make_head(_module, 'IItemContainerProvider')
make_head(_module, 'IMultipleViewProvider')
make_head(_module, 'IObjectModelProvider')
make_head(_module, 'IRangeValueProvider')
make_head(_module, 'IRawElementProviderSimple')
make_head(_module, 'IScrollItemProvider')
make_head(_module, 'IScrollProvider')
make_head(_module, 'ISelectionItemProvider')
make_head(_module, 'ISelectionProvider')
make_head(_module, 'ISpreadsheetItemProvider')
make_head(_module, 'ISpreadsheetProvider')
make_head(_module, 'IStylesProvider')
make_head(_module, 'ISynchronizedInputProvider')
make_head(_module, 'ITableItemProvider')
make_head(_module, 'ITableProvider')
make_head(_module, 'ITextChildProvider')
make_head(_module, 'ITextEditProvider')
make_head(_module, 'ITextProvider')
make_head(_module, 'ITextProvider2')
make_head(_module, 'ITextRangeProvider')
make_head(_module, 'ITextRangeProvider2')
make_head(_module, 'IToggleProvider')
make_head(_module, 'ITransformProvider')
make_head(_module, 'ITransformProvider2')
make_head(_module, 'IValueProvider')
make_head(_module, 'IVirtualizedItemProvider')
make_head(_module, 'IWindowProvider')
