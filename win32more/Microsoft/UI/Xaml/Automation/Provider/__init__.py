from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Automation
import win32more.Microsoft.UI.Xaml.Automation.Peers
import win32more.Microsoft.UI.Xaml.Automation.Provider
import win32more.Microsoft.UI.Xaml.Automation.Text
import win32more.Windows.Foundation
import win32more.Windows.UI
import win32more.Windows.Win32.System.WinRT
class IAnnotationProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IAnnotationProvider'
    _iid_ = Guid('{546ab18e-986d-5deb-8f2a-2d9303a43006}')
    @winrt_commethod(6)
    def get_AnnotationTypeId(self) -> Int32: ...
    @winrt_commethod(7)
    def get_AnnotationTypeName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Author(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DateTime(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Target(self) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    AnnotationTypeId = property(get_AnnotationTypeId, None)
    AnnotationTypeName = property(get_AnnotationTypeName, None)
    Author = property(get_Author, None)
    DateTime = property(get_DateTime, None)
    Target = property(get_Target, None)
class ICustomNavigationProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ICustomNavigationProvider'
    _iid_ = Guid('{cad51322-faa9-5a2b-90f0-b762c46178b3}')
    @winrt_commethod(6)
    def NavigateCustom(self, direction: win32more.Microsoft.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class IDockProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IDockProvider'
    _iid_ = Guid('{9882b971-70ea-5c6d-a818-7a7ab68c6f3b}')
    @winrt_commethod(6)
    def get_DockPosition(self) -> win32more.Microsoft.UI.Xaml.Automation.DockPosition: ...
    @winrt_commethod(7)
    def SetDockPosition(self, dockPosition: win32more.Microsoft.UI.Xaml.Automation.DockPosition) -> Void: ...
    DockPosition = property(get_DockPosition, None)
class IDragProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IDragProvider'
    _iid_ = Guid('{c60bb643-a356-5132-a258-ffba6c7480f2}')
    @winrt_commethod(6)
    def get_IsGrabbed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_DropEffect(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DropEffects(self) -> ReceiveArray[WinRT_String]: ...
    @winrt_commethod(9)
    def GetGrabbedItems(self) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    DropEffect = property(get_DropEffect, None)
    DropEffects = property(get_DropEffects, None)
    IsGrabbed = property(get_IsGrabbed, None)
class IDropTargetProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IDropTargetProvider'
    _iid_ = Guid('{9b2a9f3d-bbb1-510d-99e8-0e0ae14a6e3b}')
    @winrt_commethod(6)
    def get_DropEffect(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DropEffects(self) -> ReceiveArray[WinRT_String]: ...
    DropEffect = property(get_DropEffect, None)
    DropEffects = property(get_DropEffects, None)
class IExpandCollapseProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IExpandCollapseProvider'
    _iid_ = Guid('{6cef349c-b181-5d0b-b297-c3b0166120c3}')
    @winrt_commethod(6)
    def get_ExpandCollapseState(self) -> win32more.Microsoft.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_commethod(7)
    def Collapse(self) -> Void: ...
    @winrt_commethod(8)
    def Expand(self) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class IGridItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IGridItemProvider'
    _iid_ = Guid('{d2557a0e-6909-5170-a680-60728df339b4}')
    @winrt_commethod(6)
    def get_Column(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ColumnSpan(self) -> Int32: ...
    @winrt_commethod(8)
    def get_ContainingGrid(self) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IGridProvider'
    _iid_ = Guid('{50992d5e-d225-56e9-a25a-78c372e81955}')
    @winrt_commethod(6)
    def get_ColumnCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_RowCount(self) -> Int32: ...
    @winrt_commethod(8)
    def GetItem(self, row: Int32, column: Int32) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    ColumnCount = property(get_ColumnCount, None)
    RowCount = property(get_RowCount, None)
class IIRawElementProviderSimple(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IIRawElementProviderSimple'
    _iid_ = Guid('{f90bc239-ade2-55c9-a838-a3b0579763c5}')
class IInvokeProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IInvokeProvider'
    _iid_ = Guid('{02481105-3378-544d-b4e1-a1b368afbc02}')
    @winrt_commethod(6)
    def Invoke(self) -> Void: ...
class IItemContainerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IItemContainerProvider'
    _iid_ = Guid('{ad297363-694e-5885-997d-a2d6dff415a7}')
    @winrt_commethod(6)
    def FindItemByProperty(self, startAfter: win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple, automationProperty: win32more.Microsoft.UI.Xaml.Automation.AutomationProperty, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class IMultipleViewProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IMultipleViewProvider'
    _iid_ = Guid('{60be5484-3d8f-51fd-beab-423422ee1e03}')
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
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IObjectModelProvider'
    _iid_ = Guid('{92953ed0-4bd8-5624-8e3d-78d45fde9cf2}')
    @winrt_commethod(6)
    def GetUnderlyingObjectModel(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class IRangeValueProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IRangeValueProvider'
    _iid_ = Guid('{729ae414-1e8f-5020-82bb-bb574d145fd8}')
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
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Automation.Provider.IIRawElementProviderSimple
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple'
class IScrollItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IScrollItemProvider'
    _iid_ = Guid('{8a6fb8eb-e5f1-58eb-8e72-8b95f236fc47}')
    @winrt_commethod(6)
    def ScrollIntoView(self) -> Void: ...
class IScrollProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IScrollProvider'
    _iid_ = Guid('{7e2e5af3-ff50-5365-bcfe-ef424b2fd590}')
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
    def Scroll(self, horizontalAmount: win32more.Microsoft.UI.Xaml.Automation.ScrollAmount, verticalAmount: win32more.Microsoft.UI.Xaml.Automation.ScrollAmount) -> Void: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ISelectionItemProvider'
    _iid_ = Guid('{c9dfdd81-d4ac-5d31-be7f-24fab16060e4}')
    @winrt_commethod(6)
    def get_IsSelected(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_SelectionContainer(self) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
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
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ISelectionProvider'
    _iid_ = Guid('{80d56d4e-0052-541f-9411-9d1778b3bfca}')
    @winrt_commethod(6)
    def get_CanSelectMultiple(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsSelectionRequired(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetSelection(self) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    CanSelectMultiple = property(get_CanSelectMultiple, None)
    IsSelectionRequired = property(get_IsSelectionRequired, None)
class ISpreadsheetItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ISpreadsheetItemProvider'
    _iid_ = Guid('{51c1ce89-b21f-592c-8768-0accdefd5738}')
    @winrt_commethod(6)
    def get_Formula(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetAnnotationObjects(self) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    @winrt_commethod(8)
    def GetAnnotationTypes(self) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.AnnotationType]: ...
    Formula = property(get_Formula, None)
class ISpreadsheetProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ISpreadsheetProvider'
    _iid_ = Guid('{1ff41bac-d9e3-5e48-b5f8-9eab0fb2d9d8}')
    @winrt_commethod(6)
    def GetItemByName(self, name: WinRT_String) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class IStylesProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IStylesProvider'
    _iid_ = Guid('{d8895839-0048-54de-9c1f-152de6665e80}')
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
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ISynchronizedInputProvider'
    _iid_ = Guid('{c5615613-936d-5289-a190-e82057e0ff5a}')
    @winrt_commethod(6)
    def Cancel(self) -> Void: ...
    @winrt_commethod(7)
    def StartListening(self, inputType: win32more.Microsoft.UI.Xaml.Automation.SynchronizedInputType) -> Void: ...
class ITableItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ITableItemProvider'
    _iid_ = Guid('{6ce6f038-54d4-5553-a4ad-03cbcf358197}')
    @winrt_commethod(6)
    def GetColumnHeaderItems(self) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    @winrt_commethod(7)
    def GetRowHeaderItems(self) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
class ITableProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ITableProvider'
    _iid_ = Guid('{9aba6724-b22d-5db8-8abb-81f911f18af2}')
    @winrt_commethod(6)
    def get_RowOrColumnMajor(self) -> win32more.Microsoft.UI.Xaml.Automation.RowOrColumnMajor: ...
    @winrt_commethod(7)
    def GetColumnHeaders(self) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    @winrt_commethod(8)
    def GetRowHeaders(self) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
    RowOrColumnMajor = property(get_RowOrColumnMajor, None)
class ITextChildProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ITextChildProvider'
    _iid_ = Guid('{7c72e55f-f75d-5522-aeb5-c1f82c32933b}')
    @winrt_commethod(6)
    def get_TextContainer(self) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(7)
    def get_TextRange(self) -> win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    TextContainer = property(get_TextContainer, None)
    TextRange = property(get_TextRange, None)
class ITextEditProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ITextEditProvider'
    _iid_ = Guid('{7f09bbe8-bea7-5dd3-ba6b-28dbb402fad4}')
    @winrt_commethod(6)
    def GetActiveComposition(self) -> win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def GetConversionTarget(self) -> win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
class ITextProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ITextProvider'
    _iid_ = Guid('{37e7dce6-fe7a-56a7-a47a-9462872c67ef}')
    @winrt_commethod(6)
    def get_DocumentRange(self) -> win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def get_SupportedTextSelection(self) -> win32more.Microsoft.UI.Xaml.Automation.SupportedTextSelection: ...
    @winrt_commethod(8)
    def GetSelection(self) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider]: ...
    @winrt_commethod(9)
    def GetVisibleRanges(self) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider]: ...
    @winrt_commethod(10)
    def RangeFromChild(self, childElement: win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(11)
    def RangeFromPoint(self, screenLocation: win32more.Windows.Foundation.Point) -> win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    DocumentRange = property(get_DocumentRange, None)
    SupportedTextSelection = property(get_SupportedTextSelection, None)
class ITextProvider2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ITextProvider2'
    _iid_ = Guid('{6844f012-c7e6-5763-ba04-5b6db910cd34}')
    @winrt_commethod(6)
    def RangeFromAnnotation(self, annotationElement: win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def GetCaretRange(self, isActive: POINTER(Boolean)) -> win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
class ITextRangeProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider'
    _iid_ = Guid('{84210361-6ce2-5084-bf3b-28afa6e9851f}')
    @winrt_commethod(6)
    def Clone(self) -> win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def Compare(self, textRangeProvider: win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider) -> Boolean: ...
    @winrt_commethod(8)
    def CompareEndpoints(self, endpoint: win32more.Microsoft.UI.Xaml.Automation.Text.TextPatternRangeEndpoint, textRangeProvider: win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider, targetEndpoint: win32more.Microsoft.UI.Xaml.Automation.Text.TextPatternRangeEndpoint) -> Int32: ...
    @winrt_commethod(9)
    def ExpandToEnclosingUnit(self, unit: win32more.Microsoft.UI.Xaml.Automation.Text.TextUnit) -> Void: ...
    @winrt_commethod(10)
    def FindAttribute(self, attributeId: Int32, value: win32more.Windows.Win32.System.WinRT.IInspectable, backward: Boolean) -> win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(11)
    def FindText(self, text: WinRT_String, backward: Boolean, ignoreCase: Boolean) -> win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(12)
    def GetAttributeValue(self, attributeId: Int32) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(13)
    def GetBoundingRectangles(self, returnValue: ReceiveArray[Double]) -> Void: ...
    @winrt_commethod(14)
    def GetEnclosingElement(self) -> win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(15)
    def GetText(self, maxLength: Int32) -> WinRT_String: ...
    @winrt_commethod(16)
    def Move(self, unit: win32more.Microsoft.UI.Xaml.Automation.Text.TextUnit, count: Int32) -> Int32: ...
    @winrt_commethod(17)
    def MoveEndpointByUnit(self, endpoint: win32more.Microsoft.UI.Xaml.Automation.Text.TextPatternRangeEndpoint, unit: win32more.Microsoft.UI.Xaml.Automation.Text.TextUnit, count: Int32) -> Int32: ...
    @winrt_commethod(18)
    def MoveEndpointByRange(self, endpoint: win32more.Microsoft.UI.Xaml.Automation.Text.TextPatternRangeEndpoint, textRangeProvider: win32more.Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider, targetEndpoint: win32more.Microsoft.UI.Xaml.Automation.Text.TextPatternRangeEndpoint) -> Void: ...
    @winrt_commethod(19)
    def Select(self) -> Void: ...
    @winrt_commethod(20)
    def AddToSelection(self) -> Void: ...
    @winrt_commethod(21)
    def RemoveFromSelection(self) -> Void: ...
    @winrt_commethod(22)
    def ScrollIntoView(self, alignToTop: Boolean) -> Void: ...
    @winrt_commethod(23)
    def GetChildren(self) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Automation.Provider.IRawElementProviderSimple]: ...
class ITextRangeProvider2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ITextRangeProvider2'
    _iid_ = Guid('{34d4a80e-36bb-5362-a53b-490428a8b367}')
    @winrt_commethod(6)
    def ShowContextMenu(self) -> Void: ...
class IToggleProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IToggleProvider'
    _iid_ = Guid('{021080c2-30a9-52ef-bc32-2b79847b6ba7}')
    @winrt_commethod(6)
    def get_ToggleState(self) -> win32more.Microsoft.UI.Xaml.Automation.ToggleState: ...
    @winrt_commethod(7)
    def Toggle(self) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class ITransformProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ITransformProvider'
    _iid_ = Guid('{6fd76988-8f52-5ef2-a826-9c8c4951c911}')
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
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.ITransformProvider2'
    _iid_ = Guid('{7d91d02d-8401-5cf8-bbc4-47391a524215}')
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
    def ZoomByUnit(self, zoomUnit: win32more.Microsoft.UI.Xaml.Automation.ZoomUnit) -> Void: ...
    CanZoom = property(get_CanZoom, None)
    MaxZoom = property(get_MaxZoom, None)
    MinZoom = property(get_MinZoom, None)
    ZoomLevel = property(get_ZoomLevel, None)
class IValueProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IValueProvider'
    _iid_ = Guid('{984f11cf-4611-588e-b52e-b96a12322c71}')
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
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IVirtualizedItemProvider'
    _iid_ = Guid('{098f858a-2e63-5985-ab87-f8ebdb1c5740}')
    @winrt_commethod(6)
    def Realize(self) -> Void: ...
class IWindowProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Automation.Provider.IWindowProvider'
    _iid_ = Guid('{83f1df99-9ddf-575e-a651-2ee657fd16e0}')
    @winrt_commethod(6)
    def get_IsModal(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsTopmost(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Maximizable(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Minimizable(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_InteractionState(self) -> win32more.Microsoft.UI.Xaml.Automation.WindowInteractionState: ...
    @winrt_commethod(11)
    def get_VisualState(self) -> win32more.Microsoft.UI.Xaml.Automation.WindowVisualState: ...
    @winrt_commethod(12)
    def Close(self) -> Void: ...
    @winrt_commethod(13)
    def SetVisualState(self, state: win32more.Microsoft.UI.Xaml.Automation.WindowVisualState) -> Void: ...
    @winrt_commethod(14)
    def WaitForInputIdle(self, milliseconds: Int32) -> Boolean: ...
    InteractionState = property(get_InteractionState, None)
    IsModal = property(get_IsModal, None)
    IsTopmost = property(get_IsTopmost, None)
    Maximizable = property(get_Maximizable, None)
    Minimizable = property(get_Minimizable, None)
    VisualState = property(get_VisualState, None)


make_ready(__name__)
