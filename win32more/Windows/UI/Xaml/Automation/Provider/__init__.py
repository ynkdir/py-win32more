from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.UI
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Automation
import win32more.Windows.UI.Xaml.Automation.Peers
import win32more.Windows.UI.Xaml.Automation.Provider
import win32more.Windows.UI.Xaml.Automation.Text
import win32more.Windows.Win32.System.WinRT
class IAnnotationProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IAnnotationProvider'
    _iid_ = Guid('{95ba1417-4437-451b-9461-050a49b59d06}')
    @winrt_commethod(6)
    def get_AnnotationTypeId(self) -> Int32: ...
    @winrt_commethod(7)
    def get_AnnotationTypeName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Author(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DateTime(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Target(self) -> win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    AnnotationTypeId = property(get_AnnotationTypeId, None)
    AnnotationTypeName = property(get_AnnotationTypeName, None)
    Author = property(get_Author, None)
    DateTime = property(get_DateTime, None)
    Target = property(get_Target, None)
class ICustomNavigationProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ICustomNavigationProvider'
    _iid_ = Guid('{2bd8a6d0-2fa3-4717-b28c-4917ce54928d}')
    @winrt_commethod(6)
    def NavigateCustom(self, direction: win32more.Windows.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class IDockProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IDockProvider'
    _iid_ = Guid('{48c243f8-78b1-44a0-ac5f-750757bcde3c}')
    @winrt_commethod(6)
    def get_DockPosition(self) -> win32more.Windows.UI.Xaml.Automation.DockPosition: ...
    @winrt_commethod(7)
    def SetDockPosition(self, dockPosition: win32more.Windows.UI.Xaml.Automation.DockPosition) -> Void: ...
    DockPosition = property(get_DockPosition, None)
class IDragProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IDragProvider'
    _iid_ = Guid('{2e7786a9-7ffc-4f57-b965-1ef1f373f546}')
    @winrt_commethod(6)
    def get_IsGrabbed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_DropEffect(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DropEffects(self) -> ReceiveArray[WinRT_String]: ...
    @winrt_commethod(9)
    def GetGrabbedItems(self) -> ReceiveArray[win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    DropEffect = property(get_DropEffect, None)
    DropEffects = property(get_DropEffects, None)
    IsGrabbed = property(get_IsGrabbed, None)
class IDropTargetProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IDropTargetProvider'
    _iid_ = Guid('{7a245bdd-b458-4fe0-98c8-aac89df56d61}')
    @winrt_commethod(6)
    def get_DropEffect(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DropEffects(self) -> ReceiveArray[WinRT_String]: ...
    DropEffect = property(get_DropEffect, None)
    DropEffects = property(get_DropEffects, None)
class IExpandCollapseProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider'
    _iid_ = Guid('{49ac8399-d626-4543-94b9-a6d9a9593af6}')
    @winrt_commethod(6)
    def get_ExpandCollapseState(self) -> win32more.Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_commethod(7)
    def Collapse(self) -> Void: ...
    @winrt_commethod(8)
    def Expand(self) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class IGridItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IGridItemProvider'
    _iid_ = Guid('{fff3683c-7407-45bb-a936-df3ed6d3837d}')
    @winrt_commethod(6)
    def get_Column(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ColumnSpan(self) -> Int32: ...
    @winrt_commethod(8)
    def get_ContainingGrid(self) -> win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IGridProvider'
    _iid_ = Guid('{8b62b7a0-932c-4490-9a13-02fdb39a8f5b}')
    @winrt_commethod(6)
    def get_ColumnCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_RowCount(self) -> Int32: ...
    @winrt_commethod(8)
    def GetItem(self, row: Int32, column: Int32) -> win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    ColumnCount = property(get_ColumnCount, None)
    RowCount = property(get_RowCount, None)
class IIRawElementProviderSimple(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IIRawElementProviderSimple'
    _iid_ = Guid('{ec752224-9b77-4720-bb21-4ac89fdb1afd}')
class IInvokeProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IInvokeProvider'
    _iid_ = Guid('{f7d1a187-b13c-4540-b09e-6778e2dc9ba5}')
    @winrt_commethod(6)
    def Invoke(self) -> Void: ...
class IItemContainerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IItemContainerProvider'
    _iid_ = Guid('{ef5cd845-e1d4-40f4-bad5-c7fad44a703e}')
    @winrt_commethod(6)
    def FindItemByProperty(self, startAfter: win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple, automationProperty: win32more.Windows.UI.Xaml.Automation.AutomationProperty, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class IMultipleViewProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IMultipleViewProvider'
    _iid_ = Guid('{d014e196-0e50-4843-a5d2-c22897c8845a}')
    @winrt_commethod(6)
    def get_CurrentView(self) -> Int32: ...
    @winrt_commethod(7)
    def GetSupportedViews(self) -> ReceiveArray[Int32]: ...
    @winrt_commethod(8)
    def GetViewName(self, viewId: Int32) -> WinRT_String: ...
    @winrt_commethod(9)
    def SetCurrentView(self, viewId: Int32) -> Void: ...
    CurrentView = property(get_CurrentView, None)
class IObjectModelProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IObjectModelProvider'
    _iid_ = Guid('{c3ca36b9-0793-4ed0-bbf4-9ff4e0f98f80}')
    @winrt_commethod(6)
    def GetUnderlyingObjectModel(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class IRangeValueProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IRangeValueProvider'
    _iid_ = Guid('{838a34a8-7d5f-4079-af03-c3d015e93413}')
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
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Automation.Provider.IIRawElementProviderSimple
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple'
class IScrollItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IScrollItemProvider'
    _iid_ = Guid('{9a3ec090-5d2c-4e42-9ee6-9d58db100b55}')
    @winrt_commethod(6)
    def ScrollIntoView(self) -> Void: ...
class IScrollProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IScrollProvider'
    _iid_ = Guid('{374bf581-7716-4bbc-82eb-d997006ea999}')
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
    def Scroll(self, horizontalAmount: win32more.Windows.UI.Xaml.Automation.ScrollAmount, verticalAmount: win32more.Windows.UI.Xaml.Automation.ScrollAmount) -> Void: ...
    @winrt_commethod(13)
    def SetScrollPercent(self, horizontalPercent: Double, verticalPercent: Double) -> Void: ...
    HorizontalScrollPercent = property(get_HorizontalScrollPercent, None)
    HorizontalViewSize = property(get_HorizontalViewSize, None)
    HorizontallyScrollable = property(get_HorizontallyScrollable, None)
    VerticalScrollPercent = property(get_VerticalScrollPercent, None)
    VerticalViewSize = property(get_VerticalViewSize, None)
    VerticallyScrollable = property(get_VerticallyScrollable, None)
class ISelectionItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider'
    _iid_ = Guid('{6a4977c1-830d-42d2-bf62-042ebddecc19}')
    @winrt_commethod(6)
    def get_IsSelected(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SelectionContainer(self) -> win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(8)
    def AddToSelection(self) -> Void: ...
    @winrt_commethod(9)
    def RemoveFromSelection(self) -> Void: ...
    @winrt_commethod(10)
    def Select(self) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class ISelectionProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ISelectionProvider'
    _iid_ = Guid('{1f018fca-b944-4395-8de1-88f674af51d3}')
    @winrt_commethod(6)
    def get_CanSelectMultiple(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsSelectionRequired(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetSelection(self) -> ReceiveArray[win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    CanSelectMultiple = property(get_CanSelectMultiple, None)
    IsSelectionRequired = property(get_IsSelectionRequired, None)
class ISpreadsheetItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ISpreadsheetItemProvider'
    _iid_ = Guid('{ebde8f92-6015-4826-b719-47521a81c67e}')
    @winrt_commethod(6)
    def get_Formula(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetAnnotationObjects(self) -> ReceiveArray[win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    @winrt_commethod(8)
    def GetAnnotationTypes(self) -> ReceiveArray[win32more.Windows.UI.Xaml.Automation.AnnotationType]: ...
    Formula = property(get_Formula, None)
class ISpreadsheetProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ISpreadsheetProvider'
    _iid_ = Guid('{15359093-bd99-4cfd-9f07-3b14b315e23d}')
    @winrt_commethod(6)
    def GetItemByName(self, name: WinRT_String) -> win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class IStylesProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IStylesProvider'
    _iid_ = Guid('{1a5b7a17-7c01-4bec-9cd4-2dfa7dc246cd}')
    @winrt_commethod(6)
    def get_ExtendedProperties(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FillColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(8)
    def get_FillPatternColor(self) -> win32more.Windows.UI.Color: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ISynchronizedInputProvider'
    _iid_ = Guid('{3d60cecb-da54-4aa3-b915-e3244427d4ac}')
    @winrt_commethod(6)
    def Cancel(self) -> Void: ...
    @winrt_commethod(7)
    def StartListening(self, inputType: win32more.Windows.UI.Xaml.Automation.SynchronizedInputType) -> Void: ...
class ITableItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITableItemProvider'
    _iid_ = Guid('{3b2c49cd-1de2-4ee2-a3e1-fb553559d15d}')
    @winrt_commethod(6)
    def GetColumnHeaderItems(self) -> ReceiveArray[win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    @winrt_commethod(7)
    def GetRowHeaderItems(self) -> ReceiveArray[win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
class ITableProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITableProvider'
    _iid_ = Guid('{7a8ed399-6824-4595-bab3-464bc9a04417}')
    @winrt_commethod(6)
    def get_RowOrColumnMajor(self) -> win32more.Windows.UI.Xaml.Automation.RowOrColumnMajor: ...
    @winrt_commethod(7)
    def GetColumnHeaders(self) -> ReceiveArray[win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    @winrt_commethod(8)
    def GetRowHeaders(self) -> ReceiveArray[win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    RowOrColumnMajor = property(get_RowOrColumnMajor, None)
class ITextChildProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITextChildProvider'
    _iid_ = Guid('{1133c336-a89b-4130-9be6-55e33334f557}')
    @winrt_commethod(6)
    def get_TextContainer(self) -> win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(7)
    def get_TextRange(self) -> win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    TextContainer = property(get_TextContainer, None)
    TextRange = property(get_TextRange, None)
class ITextEditProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITextEditProvider'
    _iid_ = Guid('{ea3605b4-3a05-400e-b5f9-4e91b40f6176}')
    @winrt_commethod(6)
    def GetActiveComposition(self) -> win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def GetConversionTarget(self) -> win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
class ITextProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITextProvider'
    _iid_ = Guid('{db5bbc9f-4807-4f2a-8678-1b13f3c60e22}')
    @winrt_commethod(6)
    def get_DocumentRange(self) -> win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def get_SupportedTextSelection(self) -> win32more.Windows.UI.Xaml.Automation.SupportedTextSelection: ...
    @winrt_commethod(8)
    def GetSelection(self) -> ReceiveArray[win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider]: ...
    @winrt_commethod(9)
    def GetVisibleRanges(self) -> ReceiveArray[win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider]: ...
    @winrt_commethod(10)
    def RangeFromChild(self, childElement: win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(11)
    def RangeFromPoint(self, screenLocation: win32more.Windows.Foundation.Point) -> win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    DocumentRange = property(get_DocumentRange, None)
    SupportedTextSelection = property(get_SupportedTextSelection, None)
class ITextProvider2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITextProvider2'
    _iid_ = Guid('{df1d48bc-0487-4e7f-9d5e-f09e77e41246}')
    @winrt_commethod(6)
    def RangeFromAnnotation(self, annotationElement: win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def GetCaretRange(self, isActive: POINTER(Boolean)) -> win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
class ITextRangeProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITextRangeProvider'
    _iid_ = Guid('{0274688d-06e9-4f66-9446-28a5be98fbd0}')
    @winrt_commethod(6)
    def Clone(self) -> win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def Compare(self, textRangeProvider: win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider) -> Boolean: ...
    @winrt_commethod(8)
    def CompareEndpoints(self, endpoint: win32more.Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint, textRangeProvider: win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, targetEndpoint: win32more.Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint) -> Int32: ...
    @winrt_commethod(9)
    def ExpandToEnclosingUnit(self, unit: win32more.Windows.UI.Xaml.Automation.Text.TextUnit) -> Void: ...
    @winrt_commethod(10)
    def FindAttribute(self, attributeId: Int32, value: win32more.Windows.Win32.System.WinRT.IInspectable, backward: Boolean) -> win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(11)
    def FindText(self, text: WinRT_String, backward: Boolean, ignoreCase: Boolean) -> win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(12)
    def GetAttributeValue(self, attributeId: Int32) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(13)
    def GetBoundingRectangles(self, returnValue: ReceiveArray[Double]) -> Void: ...
    @winrt_commethod(14)
    def GetEnclosingElement(self) -> win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(15)
    def GetText(self, maxLength: Int32) -> WinRT_String: ...
    @winrt_commethod(16)
    def Move(self, unit: win32more.Windows.UI.Xaml.Automation.Text.TextUnit, count: Int32) -> Int32: ...
    @winrt_commethod(17)
    def MoveEndpointByUnit(self, endpoint: win32more.Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint, unit: win32more.Windows.UI.Xaml.Automation.Text.TextUnit, count: Int32) -> Int32: ...
    @winrt_commethod(18)
    def MoveEndpointByRange(self, endpoint: win32more.Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint, textRangeProvider: win32more.Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, targetEndpoint: win32more.Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint) -> Void: ...
    @winrt_commethod(19)
    def Select(self) -> Void: ...
    @winrt_commethod(20)
    def AddToSelection(self) -> Void: ...
    @winrt_commethod(21)
    def RemoveFromSelection(self) -> Void: ...
    @winrt_commethod(22)
    def ScrollIntoView(self, alignToTop: Boolean) -> Void: ...
    @winrt_commethod(23)
    def GetChildren(self) -> ReceiveArray[win32more.Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
class ITextRangeProvider2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITextRangeProvider2'
    _iid_ = Guid('{d3be3dfb-9f54-4642-a7a5-5c18d5ee2a3f}')
    @winrt_commethod(6)
    def ShowContextMenu(self) -> Void: ...
class IToggleProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IToggleProvider'
    _iid_ = Guid('{93b88290-656f-44f7-aeaf-78b8f944d062}')
    @winrt_commethod(6)
    def get_ToggleState(self) -> win32more.Windows.UI.Xaml.Automation.ToggleState: ...
    @winrt_commethod(7)
    def Toggle(self) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class ITransformProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITransformProvider'
    _iid_ = Guid('{79670fdd-f6a9-4a65-af17-861db799a2da}')
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITransformProvider2'
    _iid_ = Guid('{a8b11756-a39f-4e97-8c7d-c1ea8dd633c5}')
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
    def ZoomByUnit(self, zoomUnit: win32more.Windows.UI.Xaml.Automation.ZoomUnit) -> Void: ...
    CanZoom = property(get_CanZoom, None)
    MaxZoom = property(get_MaxZoom, None)
    MinZoom = property(get_MinZoom, None)
    ZoomLevel = property(get_ZoomLevel, None)
class IValueProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IValueProvider'
    _iid_ = Guid('{2086b7a7-ac0e-47d1-ab9b-2a64292afdf8}')
    @winrt_commethod(6)
    def get_IsReadOnly(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetValue(self, value: WinRT_String) -> Void: ...
    IsReadOnly = property(get_IsReadOnly, None)
    Value = property(get_Value, None)
class IVirtualizedItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IVirtualizedItemProvider'
    _iid_ = Guid('{17d4a04b-d658-48e0-a574-5a516c58dfa7}')
    @winrt_commethod(6)
    def Realize(self) -> Void: ...
class IWindowProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IWindowProvider'
    _iid_ = Guid('{1baa8b3d-38cf-415a-85d3-20e43a0ec1b1}')
    @winrt_commethod(6)
    def get_IsModal(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsTopmost(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Maximizable(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Minimizable(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_InteractionState(self) -> win32more.Windows.UI.Xaml.Automation.WindowInteractionState: ...
    @winrt_commethod(11)
    def get_VisualState(self) -> win32more.Windows.UI.Xaml.Automation.WindowVisualState: ...
    @winrt_commethod(12)
    def Close(self) -> Void: ...
    @winrt_commethod(13)
    def SetVisualState(self, state: win32more.Windows.UI.Xaml.Automation.WindowVisualState) -> Void: ...
    @winrt_commethod(14)
    def WaitForInputIdle(self, milliseconds: Int32) -> Boolean: ...
    InteractionState = property(get_InteractionState, None)
    IsModal = property(get_IsModal, None)
    IsTopmost = property(get_IsTopmost, None)
    Maximizable = property(get_Maximizable, None)
    Minimizable = property(get_Minimizable, None)
    VisualState = property(get_VisualState, None)


make_ready(__name__)
