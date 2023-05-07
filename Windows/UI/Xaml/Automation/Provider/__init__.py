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
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IAnnotationProvider'
    _iid_ = Guid('{95ba1417-4437-451b-9461-050a49b59d06}')
    @winrt_commethod(6)
    def get_AnnotationTypeId(self: Windows.UI.Xaml.Automation.Provider.IAnnotationProvider) -> Int32: ...
    @winrt_commethod(7)
    def get_AnnotationTypeName(self: Windows.UI.Xaml.Automation.Provider.IAnnotationProvider) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Author(self: Windows.UI.Xaml.Automation.Provider.IAnnotationProvider) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DateTime(self: Windows.UI.Xaml.Automation.Provider.IAnnotationProvider) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Target(self: Windows.UI.Xaml.Automation.Provider.IAnnotationProvider) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    AnnotationTypeId = property(get_AnnotationTypeId, None)
    AnnotationTypeName = property(get_AnnotationTypeName, None)
    Author = property(get_Author, None)
    DateTime = property(get_DateTime, None)
    Target = property(get_Target, None)
class ICustomNavigationProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ICustomNavigationProvider'
    _iid_ = Guid('{2bd8a6d0-2fa3-4717-b28c-4917ce54928d}')
    @winrt_commethod(6)
    def NavigateCustom(self: Windows.UI.Xaml.Automation.Provider.ICustomNavigationProvider, direction: Windows.UI.Xaml.Automation.Peers.AutomationNavigationDirection) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class IDockProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IDockProvider'
    _iid_ = Guid('{48c243f8-78b1-44a0-ac5f-750757bcde3c}')
    @winrt_commethod(6)
    def get_DockPosition(self: Windows.UI.Xaml.Automation.Provider.IDockProvider) -> Windows.UI.Xaml.Automation.DockPosition: ...
    @winrt_commethod(7)
    def SetDockPosition(self: Windows.UI.Xaml.Automation.Provider.IDockProvider, dockPosition: Windows.UI.Xaml.Automation.DockPosition) -> Void: ...
    DockPosition = property(get_DockPosition, None)
class IDragProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IDragProvider'
    _iid_ = Guid('{2e7786a9-7ffc-4f57-b965-1ef1f373f546}')
    @winrt_commethod(6)
    def get_IsGrabbed(self: Windows.UI.Xaml.Automation.Provider.IDragProvider) -> Boolean: ...
    @winrt_commethod(7)
    def get_DropEffect(self: Windows.UI.Xaml.Automation.Provider.IDragProvider) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DropEffects(self: Windows.UI.Xaml.Automation.Provider.IDragProvider) -> POINTER(WinRT_String): ...
    @winrt_commethod(9)
    def GetGrabbedItems(self: Windows.UI.Xaml.Automation.Provider.IDragProvider) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
    IsGrabbed = property(get_IsGrabbed, None)
    DropEffect = property(get_DropEffect, None)
    DropEffects = property(get_DropEffects, None)
class IDropTargetProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IDropTargetProvider'
    _iid_ = Guid('{7a245bdd-b458-4fe0-98c8-aac89df56d61}')
    @winrt_commethod(6)
    def get_DropEffect(self: Windows.UI.Xaml.Automation.Provider.IDropTargetProvider) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DropEffects(self: Windows.UI.Xaml.Automation.Provider.IDropTargetProvider) -> POINTER(WinRT_String): ...
    DropEffect = property(get_DropEffect, None)
    DropEffects = property(get_DropEffects, None)
class IExpandCollapseProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider'
    _iid_ = Guid('{49ac8399-d626-4543-94b9-a6d9a9593af6}')
    @winrt_commethod(6)
    def get_ExpandCollapseState(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Windows.UI.Xaml.Automation.ExpandCollapseState: ...
    @winrt_commethod(7)
    def Collapse(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    @winrt_commethod(8)
    def Expand(self: Windows.UI.Xaml.Automation.Provider.IExpandCollapseProvider) -> Void: ...
    ExpandCollapseState = property(get_ExpandCollapseState, None)
class IGridItemProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IGridItemProvider'
    _iid_ = Guid('{fff3683c-7407-45bb-a936-df3ed6d3837d}')
    @winrt_commethod(6)
    def get_Column(self: Windows.UI.Xaml.Automation.Provider.IGridItemProvider) -> Int32: ...
    @winrt_commethod(7)
    def get_ColumnSpan(self: Windows.UI.Xaml.Automation.Provider.IGridItemProvider) -> Int32: ...
    @winrt_commethod(8)
    def get_ContainingGrid(self: Windows.UI.Xaml.Automation.Provider.IGridItemProvider) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(9)
    def get_Row(self: Windows.UI.Xaml.Automation.Provider.IGridItemProvider) -> Int32: ...
    @winrt_commethod(10)
    def get_RowSpan(self: Windows.UI.Xaml.Automation.Provider.IGridItemProvider) -> Int32: ...
    Column = property(get_Column, None)
    ColumnSpan = property(get_ColumnSpan, None)
    ContainingGrid = property(get_ContainingGrid, None)
    Row = property(get_Row, None)
    RowSpan = property(get_RowSpan, None)
class IGridProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IGridProvider'
    _iid_ = Guid('{8b62b7a0-932c-4490-9a13-02fdb39a8f5b}')
    @winrt_commethod(6)
    def get_ColumnCount(self: Windows.UI.Xaml.Automation.Provider.IGridProvider) -> Int32: ...
    @winrt_commethod(7)
    def get_RowCount(self: Windows.UI.Xaml.Automation.Provider.IGridProvider) -> Int32: ...
    @winrt_commethod(8)
    def GetItem(self: Windows.UI.Xaml.Automation.Provider.IGridProvider, row: Int32, column: Int32) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    ColumnCount = property(get_ColumnCount, None)
    RowCount = property(get_RowCount, None)
class IIRawElementProviderSimple(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IIRawElementProviderSimple'
    _iid_ = Guid('{ec752224-9b77-4720-bb21-4ac89fdb1afd}')
class IInvokeProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IInvokeProvider'
    _iid_ = Guid('{f7d1a187-b13c-4540-b09e-6778e2dc9ba5}')
    @winrt_commethod(6)
    def Invoke(self: Windows.UI.Xaml.Automation.Provider.IInvokeProvider) -> Void: ...
class IItemContainerProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IItemContainerProvider'
    _iid_ = Guid('{ef5cd845-e1d4-40f4-bad5-c7fad44a703e}')
    @winrt_commethod(6)
    def FindItemByProperty(self: Windows.UI.Xaml.Automation.Provider.IItemContainerProvider, startAfter: Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple, automationProperty: Windows.UI.Xaml.Automation.AutomationProperty, value: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class IMultipleViewProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IMultipleViewProvider'
    _iid_ = Guid('{d014e196-0e50-4843-a5d2-c22897c8845a}')
    @winrt_commethod(6)
    def get_CurrentView(self: Windows.UI.Xaml.Automation.Provider.IMultipleViewProvider) -> Int32: ...
    @winrt_commethod(7)
    def GetSupportedViews(self: Windows.UI.Xaml.Automation.Provider.IMultipleViewProvider) -> POINTER(Int32): ...
    @winrt_commethod(8)
    def GetViewName(self: Windows.UI.Xaml.Automation.Provider.IMultipleViewProvider, viewId: Int32) -> WinRT_String: ...
    @winrt_commethod(9)
    def SetCurrentView(self: Windows.UI.Xaml.Automation.Provider.IMultipleViewProvider, viewId: Int32) -> Void: ...
    CurrentView = property(get_CurrentView, None)
class IObjectModelProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IObjectModelProvider'
    _iid_ = Guid('{c3ca36b9-0793-4ed0-bbf4-9ff4e0f98f80}')
    @winrt_commethod(6)
    def GetUnderlyingObjectModel(self: Windows.UI.Xaml.Automation.Provider.IObjectModelProvider) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class IRangeValueProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IRangeValueProvider'
    _iid_ = Guid('{838a34a8-7d5f-4079-af03-c3d015e93413}')
    @winrt_commethod(6)
    def get_IsReadOnly(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Boolean: ...
    @winrt_commethod(7)
    def get_LargeChange(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_commethod(8)
    def get_Maximum(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_commethod(9)
    def get_Minimum(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_commethod(10)
    def get_SmallChange(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_commethod(11)
    def get_Value(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider) -> Double: ...
    @winrt_commethod(12)
    def SetValue(self: Windows.UI.Xaml.Automation.Provider.IRangeValueProvider, value: Double) -> Void: ...
    IsReadOnly = property(get_IsReadOnly, None)
    LargeChange = property(get_LargeChange, None)
    Maximum = property(get_Maximum, None)
    Minimum = property(get_Minimum, None)
    SmallChange = property(get_SmallChange, None)
    Value = property(get_Value, None)
class IRawElementProviderSimple(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Automation.Provider.IIRawElementProviderSimple
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple'
class IScrollItemProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IScrollItemProvider'
    _iid_ = Guid('{9a3ec090-5d2c-4e42-9ee6-9d58db100b55}')
    @winrt_commethod(6)
    def ScrollIntoView(self: Windows.UI.Xaml.Automation.Provider.IScrollItemProvider) -> Void: ...
class IScrollProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IScrollProvider'
    _iid_ = Guid('{374bf581-7716-4bbc-82eb-d997006ea999}')
    @winrt_commethod(6)
    def get_HorizontallyScrollable(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_commethod(7)
    def get_HorizontalScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_commethod(8)
    def get_HorizontalViewSize(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_commethod(9)
    def get_VerticallyScrollable(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Boolean: ...
    @winrt_commethod(10)
    def get_VerticalScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_commethod(11)
    def get_VerticalViewSize(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider) -> Double: ...
    @winrt_commethod(12)
    def Scroll(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider, horizontalAmount: Windows.UI.Xaml.Automation.ScrollAmount, verticalAmount: Windows.UI.Xaml.Automation.ScrollAmount) -> Void: ...
    @winrt_commethod(13)
    def SetScrollPercent(self: Windows.UI.Xaml.Automation.Provider.IScrollProvider, horizontalPercent: Double, verticalPercent: Double) -> Void: ...
    HorizontallyScrollable = property(get_HorizontallyScrollable, None)
    HorizontalScrollPercent = property(get_HorizontalScrollPercent, None)
    HorizontalViewSize = property(get_HorizontalViewSize, None)
    VerticallyScrollable = property(get_VerticallyScrollable, None)
    VerticalScrollPercent = property(get_VerticalScrollPercent, None)
    VerticalViewSize = property(get_VerticalViewSize, None)
class ISelectionItemProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider'
    _iid_ = Guid('{6a4977c1-830d-42d2-bf62-042ebddecc19}')
    @winrt_commethod(6)
    def get_IsSelected(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Boolean: ...
    @winrt_commethod(7)
    def get_SelectionContainer(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(8)
    def AddToSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_commethod(9)
    def RemoveFromSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    @winrt_commethod(10)
    def Select(self: Windows.UI.Xaml.Automation.Provider.ISelectionItemProvider) -> Void: ...
    IsSelected = property(get_IsSelected, None)
    SelectionContainer = property(get_SelectionContainer, None)
class ISelectionProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ISelectionProvider'
    _iid_ = Guid('{1f018fca-b944-4395-8de1-88f674af51d3}')
    @winrt_commethod(6)
    def get_CanSelectMultiple(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsSelectionRequired(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> Boolean: ...
    @winrt_commethod(8)
    def GetSelection(self: Windows.UI.Xaml.Automation.Provider.ISelectionProvider) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
    CanSelectMultiple = property(get_CanSelectMultiple, None)
    IsSelectionRequired = property(get_IsSelectionRequired, None)
class ISpreadsheetItemProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ISpreadsheetItemProvider'
    _iid_ = Guid('{ebde8f92-6015-4826-b719-47521a81c67e}')
    @winrt_commethod(6)
    def get_Formula(self: Windows.UI.Xaml.Automation.Provider.ISpreadsheetItemProvider) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetAnnotationObjects(self: Windows.UI.Xaml.Automation.Provider.ISpreadsheetItemProvider) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
    @winrt_commethod(8)
    def GetAnnotationTypes(self: Windows.UI.Xaml.Automation.Provider.ISpreadsheetItemProvider) -> POINTER(Windows.UI.Xaml.Automation.AnnotationType): ...
    Formula = property(get_Formula, None)
class ISpreadsheetProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ISpreadsheetProvider'
    _iid_ = Guid('{15359093-bd99-4cfd-9f07-3b14b315e23d}')
    @winrt_commethod(6)
    def GetItemByName(self: Windows.UI.Xaml.Automation.Provider.ISpreadsheetProvider, name: WinRT_String) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
class IStylesProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IStylesProvider'
    _iid_ = Guid('{1a5b7a17-7c01-4bec-9cd4-2dfa7dc246cd}')
    @winrt_commethod(6)
    def get_ExtendedProperties(self: Windows.UI.Xaml.Automation.Provider.IStylesProvider) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FillColor(self: Windows.UI.Xaml.Automation.Provider.IStylesProvider) -> Windows.UI.Color: ...
    @winrt_commethod(8)
    def get_FillPatternColor(self: Windows.UI.Xaml.Automation.Provider.IStylesProvider) -> Windows.UI.Color: ...
    @winrt_commethod(9)
    def get_FillPatternStyle(self: Windows.UI.Xaml.Automation.Provider.IStylesProvider) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Shape(self: Windows.UI.Xaml.Automation.Provider.IStylesProvider) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_StyleId(self: Windows.UI.Xaml.Automation.Provider.IStylesProvider) -> Int32: ...
    @winrt_commethod(12)
    def get_StyleName(self: Windows.UI.Xaml.Automation.Provider.IStylesProvider) -> WinRT_String: ...
    ExtendedProperties = property(get_ExtendedProperties, None)
    FillColor = property(get_FillColor, None)
    FillPatternColor = property(get_FillPatternColor, None)
    FillPatternStyle = property(get_FillPatternStyle, None)
    Shape = property(get_Shape, None)
    StyleId = property(get_StyleId, None)
    StyleName = property(get_StyleName, None)
class ISynchronizedInputProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ISynchronizedInputProvider'
    _iid_ = Guid('{3d60cecb-da54-4aa3-b915-e3244427d4ac}')
    @winrt_commethod(6)
    def Cancel(self: Windows.UI.Xaml.Automation.Provider.ISynchronizedInputProvider) -> Void: ...
    @winrt_commethod(7)
    def StartListening(self: Windows.UI.Xaml.Automation.Provider.ISynchronizedInputProvider, inputType: Windows.UI.Xaml.Automation.SynchronizedInputType) -> Void: ...
class ITableItemProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITableItemProvider'
    _iid_ = Guid('{3b2c49cd-1de2-4ee2-a3e1-fb553559d15d}')
    @winrt_commethod(6)
    def GetColumnHeaderItems(self: Windows.UI.Xaml.Automation.Provider.ITableItemProvider) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
    @winrt_commethod(7)
    def GetRowHeaderItems(self: Windows.UI.Xaml.Automation.Provider.ITableItemProvider) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
class ITableProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITableProvider'
    _iid_ = Guid('{7a8ed399-6824-4595-bab3-464bc9a04417}')
    @winrt_commethod(6)
    def get_RowOrColumnMajor(self: Windows.UI.Xaml.Automation.Provider.ITableProvider) -> Windows.UI.Xaml.Automation.RowOrColumnMajor: ...
    @winrt_commethod(7)
    def GetColumnHeaders(self: Windows.UI.Xaml.Automation.Provider.ITableProvider) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
    @winrt_commethod(8)
    def GetRowHeaders(self: Windows.UI.Xaml.Automation.Provider.ITableProvider) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
    RowOrColumnMajor = property(get_RowOrColumnMajor, None)
class ITextChildProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITextChildProvider'
    _iid_ = Guid('{1133c336-a89b-4130-9be6-55e33334f557}')
    @winrt_commethod(6)
    def get_TextContainer(self: Windows.UI.Xaml.Automation.Provider.ITextChildProvider) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(7)
    def get_TextRange(self: Windows.UI.Xaml.Automation.Provider.ITextChildProvider) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    TextContainer = property(get_TextContainer, None)
    TextRange = property(get_TextRange, None)
class ITextEditProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITextEditProvider'
    _iid_ = Guid('{ea3605b4-3a05-400e-b5f9-4e91b40f6176}')
    @winrt_commethod(6)
    def GetActiveComposition(self: Windows.UI.Xaml.Automation.Provider.ITextEditProvider) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def GetConversionTarget(self: Windows.UI.Xaml.Automation.Provider.ITextEditProvider) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
class ITextProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITextProvider'
    _iid_ = Guid('{db5bbc9f-4807-4f2a-8678-1b13f3c60e22}')
    @winrt_commethod(6)
    def get_DocumentRange(self: Windows.UI.Xaml.Automation.Provider.ITextProvider) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def get_SupportedTextSelection(self: Windows.UI.Xaml.Automation.Provider.ITextProvider) -> Windows.UI.Xaml.Automation.SupportedTextSelection: ...
    @winrt_commethod(8)
    def GetSelection(self: Windows.UI.Xaml.Automation.Provider.ITextProvider) -> POINTER(Windows.UI.Xaml.Automation.Provider.ITextRangeProvider): ...
    @winrt_commethod(9)
    def GetVisibleRanges(self: Windows.UI.Xaml.Automation.Provider.ITextProvider) -> POINTER(Windows.UI.Xaml.Automation.Provider.ITextRangeProvider): ...
    @winrt_commethod(10)
    def RangeFromChild(self: Windows.UI.Xaml.Automation.Provider.ITextProvider, childElement: Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(11)
    def RangeFromPoint(self: Windows.UI.Xaml.Automation.Provider.ITextProvider, screenLocation: Windows.Foundation.Point) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    DocumentRange = property(get_DocumentRange, None)
    SupportedTextSelection = property(get_SupportedTextSelection, None)
class ITextProvider2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITextProvider2'
    _iid_ = Guid('{df1d48bc-0487-4e7f-9d5e-f09e77e41246}')
    @winrt_commethod(6)
    def RangeFromAnnotation(self: Windows.UI.Xaml.Automation.Provider.ITextProvider2, annotationElement: Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def GetCaretRange(self: Windows.UI.Xaml.Automation.Provider.ITextProvider2, isActive: POINTER(Boolean)) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
class ITextRangeProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITextRangeProvider'
    _iid_ = Guid('{0274688d-06e9-4f66-9446-28a5be98fbd0}')
    @winrt_commethod(6)
    def Clone(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(7)
    def Compare(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, textRangeProvider: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider) -> Boolean: ...
    @winrt_commethod(8)
    def CompareEndpoints(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, endpoint: Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint, textRangeProvider: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, targetEndpoint: Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint) -> Int32: ...
    @winrt_commethod(9)
    def ExpandToEnclosingUnit(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, unit: Windows.UI.Xaml.Automation.Text.TextUnit) -> Void: ...
    @winrt_commethod(10)
    def FindAttribute(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, attributeId: Int32, value: Windows.Win32.System.WinRT.IInspectable_head, backward: Boolean) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(11)
    def FindText(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, text: WinRT_String, backward: Boolean, ignoreCase: Boolean) -> Windows.UI.Xaml.Automation.Provider.ITextRangeProvider: ...
    @winrt_commethod(12)
    def GetAttributeValue(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, attributeId: Int32) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(13)
    def GetBoundingRectangles(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, returnValue: POINTER(POINTER(Double))) -> Void: ...
    @winrt_commethod(14)
    def GetEnclosingElement(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider) -> Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple: ...
    @winrt_commethod(15)
    def GetText(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, maxLength: Int32) -> WinRT_String: ...
    @winrt_commethod(16)
    def Move(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, unit: Windows.UI.Xaml.Automation.Text.TextUnit, count: Int32) -> Int32: ...
    @winrt_commethod(17)
    def MoveEndpointByUnit(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, endpoint: Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint, unit: Windows.UI.Xaml.Automation.Text.TextUnit, count: Int32) -> Int32: ...
    @winrt_commethod(18)
    def MoveEndpointByRange(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, endpoint: Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint, textRangeProvider: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, targetEndpoint: Windows.UI.Xaml.Automation.Text.TextPatternRangeEndpoint) -> Void: ...
    @winrt_commethod(19)
    def Select(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider) -> Void: ...
    @winrt_commethod(20)
    def AddToSelection(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider) -> Void: ...
    @winrt_commethod(21)
    def RemoveFromSelection(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider) -> Void: ...
    @winrt_commethod(22)
    def ScrollIntoView(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider, alignToTop: Boolean) -> Void: ...
    @winrt_commethod(23)
    def GetChildren(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider) -> POINTER(Windows.UI.Xaml.Automation.Provider.IRawElementProviderSimple): ...
class ITextRangeProvider2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITextRangeProvider2'
    _iid_ = Guid('{d3be3dfb-9f54-4642-a7a5-5c18d5ee2a3f}')
    @winrt_commethod(6)
    def ShowContextMenu(self: Windows.UI.Xaml.Automation.Provider.ITextRangeProvider2) -> Void: ...
class IToggleProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IToggleProvider'
    _iid_ = Guid('{93b88290-656f-44f7-aeaf-78b8f944d062}')
    @winrt_commethod(6)
    def get_ToggleState(self: Windows.UI.Xaml.Automation.Provider.IToggleProvider) -> Windows.UI.Xaml.Automation.ToggleState: ...
    @winrt_commethod(7)
    def Toggle(self: Windows.UI.Xaml.Automation.Provider.IToggleProvider) -> Void: ...
    ToggleState = property(get_ToggleState, None)
class ITransformProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITransformProvider'
    _iid_ = Guid('{79670fdd-f6a9-4a65-af17-861db799a2da}')
    @winrt_commethod(6)
    def get_CanMove(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider) -> Boolean: ...
    @winrt_commethod(7)
    def get_CanResize(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider) -> Boolean: ...
    @winrt_commethod(8)
    def get_CanRotate(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider) -> Boolean: ...
    @winrt_commethod(9)
    def Move(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider, x: Double, y: Double) -> Void: ...
    @winrt_commethod(10)
    def Resize(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider, width: Double, height: Double) -> Void: ...
    @winrt_commethod(11)
    def Rotate(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider, degrees: Double) -> Void: ...
    CanMove = property(get_CanMove, None)
    CanResize = property(get_CanResize, None)
    CanRotate = property(get_CanRotate, None)
class ITransformProvider2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.ITransformProvider2'
    _iid_ = Guid('{a8b11756-a39f-4e97-8c7d-c1ea8dd633c5}')
    @winrt_commethod(6)
    def get_CanZoom(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider2) -> Boolean: ...
    @winrt_commethod(7)
    def get_ZoomLevel(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider2) -> Double: ...
    @winrt_commethod(8)
    def get_MaxZoom(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider2) -> Double: ...
    @winrt_commethod(9)
    def get_MinZoom(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider2) -> Double: ...
    @winrt_commethod(10)
    def Zoom(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider2, zoom: Double) -> Void: ...
    @winrt_commethod(11)
    def ZoomByUnit(self: Windows.UI.Xaml.Automation.Provider.ITransformProvider2, zoomUnit: Windows.UI.Xaml.Automation.ZoomUnit) -> Void: ...
    CanZoom = property(get_CanZoom, None)
    ZoomLevel = property(get_ZoomLevel, None)
    MaxZoom = property(get_MaxZoom, None)
    MinZoom = property(get_MinZoom, None)
class IValueProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IValueProvider'
    _iid_ = Guid('{2086b7a7-ac0e-47d1-ab9b-2a64292afdf8}')
    @winrt_commethod(6)
    def get_IsReadOnly(self: Windows.UI.Xaml.Automation.Provider.IValueProvider) -> Boolean: ...
    @winrt_commethod(7)
    def get_Value(self: Windows.UI.Xaml.Automation.Provider.IValueProvider) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetValue(self: Windows.UI.Xaml.Automation.Provider.IValueProvider, value: WinRT_String) -> Void: ...
    IsReadOnly = property(get_IsReadOnly, None)
    Value = property(get_Value, None)
class IVirtualizedItemProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IVirtualizedItemProvider'
    _iid_ = Guid('{17d4a04b-d658-48e0-a574-5a516c58dfa7}')
    @winrt_commethod(6)
    def Realize(self: Windows.UI.Xaml.Automation.Provider.IVirtualizedItemProvider) -> Void: ...
class IWindowProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Automation.Provider.IWindowProvider'
    _iid_ = Guid('{1baa8b3d-38cf-415a-85d3-20e43a0ec1b1}')
    @winrt_commethod(6)
    def get_IsModal(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsTopmost(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_commethod(8)
    def get_Maximizable(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_commethod(9)
    def get_Minimizable(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Boolean: ...
    @winrt_commethod(10)
    def get_InteractionState(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Windows.UI.Xaml.Automation.WindowInteractionState: ...
    @winrt_commethod(11)
    def get_VisualState(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Windows.UI.Xaml.Automation.WindowVisualState: ...
    @winrt_commethod(12)
    def Close(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider) -> Void: ...
    @winrt_commethod(13)
    def SetVisualState(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider, state: Windows.UI.Xaml.Automation.WindowVisualState) -> Void: ...
    @winrt_commethod(14)
    def WaitForInputIdle(self: Windows.UI.Xaml.Automation.Provider.IWindowProvider, milliseconds: Int32) -> Boolean: ...
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
