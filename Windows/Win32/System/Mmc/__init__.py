from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.System.Com
import Windows.Win32.System.Mmc
import Windows.Win32.System.Variant
import Windows.Win32.UI.Controls
import Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
MMC_VER: UInt32 = 512
MMC_PROP_CHANGEAFFECTSUI: UInt32 = 1
MMC_PROP_MODIFIABLE: UInt32 = 2
MMC_PROP_REMOVABLE: UInt32 = 4
MMC_PROP_PERSIST: UInt32 = 8
MMCLV_AUTO: Int32 = -1
MMCLV_NOPARAM: Int32 = -2
MMCLV_NOICON: Int32 = -1
MMCLV_VIEWSTYLE_ICON: UInt32 = 0
MMCLV_VIEWSTYLE_SMALLICON: UInt32 = 2
MMCLV_VIEWSTYLE_LIST: UInt32 = 3
MMCLV_VIEWSTYLE_REPORT: UInt32 = 1
MMCLV_VIEWSTYLE_FILTERED: UInt32 = 4
MMCLV_NOPTR: UInt32 = 0
MMCLV_UPDATE_NOINVALIDATEALL: UInt32 = 1
MMCLV_UPDATE_NOSCROLL: UInt32 = 2
MMC_IMAGECALLBACK: Int32 = -1
RDI_STR: UInt32 = 2
RDI_IMAGE: UInt32 = 4
RDI_STATE: UInt32 = 8
RDI_PARAM: UInt32 = 16
RDI_INDEX: UInt32 = 32
RDI_INDENT: UInt32 = 64
MMC_VIEW_OPTIONS_NONE: UInt32 = 0
MMC_VIEW_OPTIONS_NOLISTVIEWS: UInt32 = 1
MMC_VIEW_OPTIONS_MULTISELECT: UInt32 = 2
MMC_VIEW_OPTIONS_OWNERDATALIST: UInt32 = 4
MMC_VIEW_OPTIONS_FILTERED: UInt32 = 8
MMC_VIEW_OPTIONS_CREATENEW: UInt32 = 16
MMC_VIEW_OPTIONS_USEFONTLINKING: UInt32 = 32
MMC_VIEW_OPTIONS_EXCLUDE_SCOPE_ITEMS_FROM_LIST: UInt32 = 64
MMC_VIEW_OPTIONS_LEXICAL_SORT: UInt32 = 128
MMC_PSO_NOAPPLYNOW: UInt32 = 1
MMC_PSO_HASHELP: UInt32 = 2
MMC_PSO_NEWWIZARDTYPE: UInt32 = 4
MMC_PSO_NO_PROPTITLE: UInt32 = 8
RFI_PARTIAL: UInt32 = 1
RFI_WRAP: UInt32 = 2
RSI_DESCENDING: UInt32 = 1
RSI_NOSORTICON: UInt32 = 2
SDI_STR: UInt32 = 2
SDI_IMAGE: UInt32 = 4
SDI_OPENIMAGE: UInt32 = 8
SDI_STATE: UInt32 = 16
SDI_PARAM: UInt32 = 32
SDI_CHILDREN: UInt32 = 64
SDI_PARENT: UInt32 = 0
SDI_PREVIOUS: UInt32 = 268435456
SDI_NEXT: UInt32 = 536870912
SDI_FIRST: UInt32 = 134217728
MMC_MULTI_SELECT_COOKIE: Int32 = -2
MMC_WINDOW_COOKIE: Int32 = -3
SPECIAL_COOKIE_MIN: Int32 = -10
SPECIAL_COOKIE_MAX: Int32 = -1
MMC_NW_OPTION_NONE: UInt32 = 0
MMC_NW_OPTION_NOSCOPEPANE: UInt32 = 1
MMC_NW_OPTION_NOTOOLBARS: UInt32 = 2
MMC_NW_OPTION_SHORTTITLE: UInt32 = 4
MMC_NW_OPTION_CUSTOMTITLE: UInt32 = 8
MMC_NW_OPTION_NOPERSIST: UInt32 = 16
MMC_NW_OPTION_NOACTIONPANE: UInt32 = 32
MMC_NODEID_SLOW_RETRIEVAL: UInt32 = 1
SPECIAL_DOBJ_MIN: Int32 = -10
SPECIAL_DOBJ_MAX: UInt32 = 0
AUTO_WIDTH: Int32 = -1
HIDE_COLUMN: Int32 = -4
ILSIF_LEAVE_LARGE_ICON: UInt32 = 1073741824
ILSIF_LEAVE_SMALL_ICON: UInt32 = 536870912
HDI_HIDDEN: UInt32 = 1
RDCI_ScopeItem: UInt32 = 2147483648
RVTI_MISC_OPTIONS_NOLISTVIEWS: UInt32 = 1
RVTI_LIST_OPTIONS_NONE: UInt32 = 0
RVTI_LIST_OPTIONS_OWNERDATALIST: UInt32 = 2
RVTI_LIST_OPTIONS_MULTISELECT: UInt32 = 4
RVTI_LIST_OPTIONS_FILTERED: UInt32 = 8
RVTI_LIST_OPTIONS_USEFONTLINKING: UInt32 = 32
RVTI_LIST_OPTIONS_EXCLUDE_SCOPE_ITEMS_FROM_LIST: UInt32 = 64
RVTI_LIST_OPTIONS_LEXICAL_SORT: UInt32 = 128
RVTI_LIST_OPTIONS_ALLOWPASTE: UInt32 = 256
RVTI_HTML_OPTIONS_NONE: UInt32 = 0
RVTI_HTML_OPTIONS_NOLISTVIEW: UInt32 = 1
RVTI_OCX_OPTIONS_NONE: UInt32 = 0
RVTI_OCX_OPTIONS_NOLISTVIEW: UInt32 = 1
RVTI_OCX_OPTIONS_CACHE_OCX: UInt32 = 2
MMC_DEFAULT_OPERATION_COPY: UInt32 = 1
MMC_ITEM_OVERLAY_STATE_MASK: UInt32 = 3840
MMC_ITEM_OVERLAY_STATE_SHIFT: UInt32 = 8
MMC_ITEM_STATE_MASK: UInt32 = 255
class AppEvents(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('fc7a4252-78ac-4532-8c-5a-56-3c-fe-13-88-63')
AppEventsDHTMLConnector = Guid('ade6444b-c91f-4e37-92-a4-5b-b4-30-a3-33-40')
Application = Guid('49b2791a-b1ae-4c90-9b-8e-e8-60-ba-07-f8-89')
CCM_COMMANDID_MASK_CONSTANTS = UInt32
CCM_COMMANDID_MASK_RESERVED: CCM_COMMANDID_MASK_CONSTANTS = 4294901760
CCM_INSERTIONALLOWED = Int32
CCM_INSERTIONALLOWED_TOP: CCM_INSERTIONALLOWED = 1
CCM_INSERTIONALLOWED_NEW: CCM_INSERTIONALLOWED = 2
CCM_INSERTIONALLOWED_TASK: CCM_INSERTIONALLOWED = 4
CCM_INSERTIONALLOWED_VIEW: CCM_INSERTIONALLOWED = 8
CCM_INSERTIONPOINTID = Int32
CCM_INSERTIONPOINTID_MASK_SPECIAL: CCM_INSERTIONPOINTID = -65536
CCM_INSERTIONPOINTID_MASK_SHARED: CCM_INSERTIONPOINTID = -2147483648
CCM_INSERTIONPOINTID_MASK_CREATE_PRIMARY: CCM_INSERTIONPOINTID = 1073741824
CCM_INSERTIONPOINTID_MASK_ADD_PRIMARY: CCM_INSERTIONPOINTID = 536870912
CCM_INSERTIONPOINTID_MASK_ADD_3RDPARTY: CCM_INSERTIONPOINTID = 268435456
CCM_INSERTIONPOINTID_MASK_RESERVED: CCM_INSERTIONPOINTID = 268369920
CCM_INSERTIONPOINTID_MASK_FLAGINDEX: CCM_INSERTIONPOINTID = 31
CCM_INSERTIONPOINTID_PRIMARY_TOP: CCM_INSERTIONPOINTID = -1610612736
CCM_INSERTIONPOINTID_PRIMARY_NEW: CCM_INSERTIONPOINTID = -1610612735
CCM_INSERTIONPOINTID_PRIMARY_TASK: CCM_INSERTIONPOINTID = -1610612734
CCM_INSERTIONPOINTID_PRIMARY_VIEW: CCM_INSERTIONPOINTID = -1610612733
CCM_INSERTIONPOINTID_PRIMARY_HELP: CCM_INSERTIONPOINTID = -1610612732
CCM_INSERTIONPOINTID_3RDPARTY_NEW: CCM_INSERTIONPOINTID = -1879048191
CCM_INSERTIONPOINTID_3RDPARTY_TASK: CCM_INSERTIONPOINTID = -1879048190
CCM_INSERTIONPOINTID_ROOT_MENU: CCM_INSERTIONPOINTID = -2147483648
CCM_SPECIAL = Int32
CCM_SPECIAL_SEPARATOR: CCM_SPECIAL = 1
CCM_SPECIAL_SUBMENU: CCM_SPECIAL = 2
CCM_SPECIAL_DEFAULT_ITEM: CCM_SPECIAL = 4
CCM_SPECIAL_INSERTION_POINT: CCM_SPECIAL = 8
CCM_SPECIAL_TESTONLY: CCM_SPECIAL = 16
class CONTEXTMENUITEM(EasyCastStructure):
    strName: Windows.Win32.Foundation.PWSTR
    strStatusBarText: Windows.Win32.Foundation.PWSTR
    lCommandID: Int32
    lInsertionPointID: Int32
    fFlags: Int32
    fSpecialFlags: Int32
class CONTEXTMENUITEM2(EasyCastStructure):
    strName: Windows.Win32.Foundation.PWSTR
    strStatusBarText: Windows.Win32.Foundation.PWSTR
    lCommandID: Int32
    lInsertionPointID: Int32
    fFlags: Int32
    fSpecialFlags: Int32
    strLanguageIndependentName: Windows.Win32.Foundation.PWSTR
class Column(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('fd1c5f63-2b16-4d06-9a-b3-f4-53-50-b9-40-ab')
    @commethod(7)
    def Name(self, Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Width(self, Width: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Width(self, Width: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DisplayPosition(self, DisplayPosition: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_DisplayPosition(self, Index: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Hidden(self, Hidden: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Hidden(self, Hidden: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetAsSortColumn(self, SortOrder: Windows.Win32.System.Mmc._ColumnSortOrder) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsSortColumn(self, IsSortColumn: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class Columns(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('383d4d97-fc44-478b-b1-39-63-23-dc-48-61-1c')
    @commethod(7)
    def Item(self, Index: Int32, Column: POINTER(Windows.Win32.System.Mmc.Column_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
ConsolePower = Guid('f0285374-dff1-11d3-b4-33-00-c0-4f-8e-cd-78')
class ContextMenu(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('dab39ce0-25e6-4e07-83-62-ba-9c-95-70-65-45')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, IndexOrPath: Windows.Win32.System.Variant.VARIANT, MenuItem: POINTER(Windows.Win32.System.Mmc.MenuItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
DATA_OBJECT_TYPES = Int32
CCT_SCOPE: DATA_OBJECT_TYPES = 32768
CCT_RESULT: DATA_OBJECT_TYPES = 32769
CCT_SNAPIN_MANAGER: DATA_OBJECT_TYPES = 32770
CCT_UNINITIALIZED: DATA_OBJECT_TYPES = 65535
class Document(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('225120d6-1e0f-40a3-93-fe-10-79-e6-a8-01-7b')
    @commethod(7)
    def Save(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SaveAs(self, Filename: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Close(self, SaveChanges: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Views(self, Views: POINTER(Windows.Win32.System.Mmc.Views_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SnapIns(self, SnapIns: POINTER(Windows.Win32.System.Mmc.SnapIns_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ActiveView(self, View: POINTER(Windows.Win32.System.Mmc.View_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Name(self, Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Name(self, Name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Location(self, Location: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_IsSaved(self, IsSaved: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Mode(self, Mode: POINTER(Windows.Win32.System.Mmc._DocumentMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Mode(self, Mode: Windows.Win32.System.Mmc._DocumentMode) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_RootNode(self, Node: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_ScopeNamespace(self, ScopeNamespace: POINTER(Windows.Win32.System.Mmc.ScopeNamespace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CreateProperties(self, Properties: POINTER(Windows.Win32.System.Mmc.Properties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_Application(self, Application: POINTER(Windows.Win32.System.Mmc._Application_head)) -> Windows.Win32.Foundation.HRESULT: ...
class Extension(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('ad4d6ca6-912f-409b-a2-6e-7f-d2-34-ae-f5-42')
    @commethod(7)
    def get_Name(self, Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Vendor(self, Vendor: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Version(self, Version: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Extensions(self, Extensions: POINTER(Windows.Win32.System.Mmc.Extensions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SnapinCLSID(self, SnapinCLSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnableAllExtensions(self, Enable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Enable(self, Enable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class Extensions(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('82dbea43-8ca4-44bc-a2-ca-d1-87-41-05-9e-c8')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Extension: POINTER(Windows.Win32.System.Mmc.Extension_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class Frame(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('e5e2d970-5bb3-4306-88-04-b0-96-8a-31-c8-e6')
    @commethod(7)
    def Maximize(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Minimize(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Restore(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Top(self, Top: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_Top(self, top: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Bottom(self, Bottom: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Bottom(self, bottom: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Left(self, Left: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Left(self, left: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Right(self, Right: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Right(self, right: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IColumnData(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('547c1354-024d-11d3-a7-07-00-c0-4f-8e-f4-cb')
    @commethod(3)
    def SetColumnConfigData(self, pColID: POINTER(Windows.Win32.System.Mmc.SColumnSetID_head), pColSetData: POINTER(Windows.Win32.System.Mmc.MMC_COLUMN_SET_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColumnConfigData(self, pColID: POINTER(Windows.Win32.System.Mmc.SColumnSetID_head), ppColSetData: POINTER(POINTER(Windows.Win32.System.Mmc.MMC_COLUMN_SET_DATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetColumnSortData(self, pColID: POINTER(Windows.Win32.System.Mmc.SColumnSetID_head), pColSortData: POINTER(Windows.Win32.System.Mmc.MMC_SORT_SET_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetColumnSortData(self, pColID: POINTER(Windows.Win32.System.Mmc.SColumnSetID_head), ppColSortData: POINTER(POINTER(Windows.Win32.System.Mmc.MMC_SORT_SET_DATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IComponent(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('43136eb2-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(3)
    def Initialize(self, lpConsole: Windows.Win32.System.Mmc.IConsole_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Notify(self, lpDataObject: Windows.Win32.System.Com.IDataObject_head, event: Windows.Win32.System.Mmc.MMC_NOTIFY_TYPE, arg: Windows.Win32.Foundation.LPARAM, param3: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Destroy(self, cookie: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryDataObject(self, cookie: IntPtr, type: Windows.Win32.System.Mmc.DATA_OBJECT_TYPES, ppDataObject: POINTER(Windows.Win32.System.Com.IDataObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResultViewType(self, cookie: IntPtr, ppViewType: POINTER(Windows.Win32.Foundation.PWSTR), pViewOptions: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDisplayInfo(self, pResultDataItem: POINTER(Windows.Win32.System.Mmc.RESULTDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CompareObjects(self, lpDataObjectA: Windows.Win32.System.Com.IDataObject_head, lpDataObjectB: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
class IComponent2(ComPtr):
    extends: Windows.Win32.System.Mmc.IComponent
    _iid_ = Guid('79a2d615-4a10-4ed4-8c-65-86-33-f9-33-50-95')
    @commethod(10)
    def QueryDispatch(self, cookie: IntPtr, type: Windows.Win32.System.Mmc.DATA_OBJECT_TYPES, ppDispatch: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetResultViewType2(self, cookie: IntPtr, pResultViewType: POINTER(Windows.Win32.System.Mmc.RESULT_VIEW_TYPE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RestoreResultView(self, cookie: IntPtr, pResultViewType: POINTER(Windows.Win32.System.Mmc.RESULT_VIEW_TYPE_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IComponentData(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('955ab28a-5218-11d0-a9-85-00-c0-4f-d8-d5-65')
    @commethod(3)
    def Initialize(self, pUnknown: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateComponent(self, ppComponent: POINTER(Windows.Win32.System.Mmc.IComponent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Notify(self, lpDataObject: Windows.Win32.System.Com.IDataObject_head, event: Windows.Win32.System.Mmc.MMC_NOTIFY_TYPE, arg: Windows.Win32.Foundation.LPARAM, param3: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Destroy(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def QueryDataObject(self, cookie: IntPtr, type: Windows.Win32.System.Mmc.DATA_OBJECT_TYPES, ppDataObject: POINTER(Windows.Win32.System.Com.IDataObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDisplayInfo(self, pScopeDataItem: POINTER(Windows.Win32.System.Mmc.SCOPEDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CompareObjects(self, lpDataObjectA: Windows.Win32.System.Com.IDataObject_head, lpDataObjectB: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
class IComponentData2(ComPtr):
    extends: Windows.Win32.System.Mmc.IComponentData
    _iid_ = Guid('cca0f2d2-82de-41b5-bf-47-3b-20-76-27-3d-5c')
    @commethod(10)
    def QueryDispatch(self, cookie: IntPtr, type: Windows.Win32.System.Mmc.DATA_OBJECT_TYPES, ppDispatch: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IConsole(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('43136eb1-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(3)
    def SetHeader(self, pHeader: Windows.Win32.System.Mmc.IHeaderCtrl_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetToolbar(self, pToolbar: Windows.Win32.System.Mmc.IToolbar_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryResultView(self, pUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryScopeImageList(self, ppImageList: POINTER(Windows.Win32.System.Mmc.IImageList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def QueryResultImageList(self, ppImageList: POINTER(Windows.Win32.System.Mmc.IImageList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UpdateAllViews(self, lpDataObject: Windows.Win32.System.Com.IDataObject_head, data: Windows.Win32.Foundation.LPARAM, hint: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def MessageBox(self, lpszText: Windows.Win32.Foundation.PWSTR, lpszTitle: Windows.Win32.Foundation.PWSTR, fuStyle: UInt32, piRetval: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def QueryConsoleVerb(self, ppConsoleVerb: POINTER(Windows.Win32.System.Mmc.IConsoleVerb_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SelectScopeItem(self, hScopeItem: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMainWindow(self, phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def NewWindow(self, hScopeItem: IntPtr, lOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IConsole2(ComPtr):
    extends: Windows.Win32.System.Mmc.IConsole
    _iid_ = Guid('103d842a-aa63-11d1-a7-e1-00-c0-4f-d8-d5-65')
    @commethod(14)
    def Expand(self, hItem: IntPtr, bExpand: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsTaskpadViewPreferred(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetStatusText(self, pszStatusText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IConsole3(ComPtr):
    extends: Windows.Win32.System.Mmc.IConsole2
    _iid_ = Guid('4f85efdb-d0e1-498c-8d-4a-d0-10-df-dd-40-4f')
    @commethod(17)
    def RenameScopeItem(self, hScopeItem: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IConsoleNameSpace(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('bedeb620-f24d-11cf-8a-fc-00-aa-00-3c-a9-f6')
    @commethod(3)
    def InsertItem(self, item: POINTER(Windows.Win32.System.Mmc.SCOPEDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteItem(self, hItem: IntPtr, fDeleteThis: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetItem(self, item: POINTER(Windows.Win32.System.Mmc.SCOPEDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetItem(self, item: POINTER(Windows.Win32.System.Mmc.SCOPEDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetChildItem(self, item: IntPtr, pItemChild: POINTER(IntPtr), pCookie: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNextItem(self, item: IntPtr, pItemNext: POINTER(IntPtr), pCookie: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetParentItem(self, item: IntPtr, pItemParent: POINTER(IntPtr), pCookie: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IConsoleNameSpace2(ComPtr):
    extends: Windows.Win32.System.Mmc.IConsoleNameSpace
    _iid_ = Guid('255f18cc-65db-11d1-a7-dc-00-c0-4f-d8-d5-65')
    @commethod(10)
    def Expand(self, hItem: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddExtension(self, hItem: IntPtr, lpClsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IConsolePower(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('1cfbdd0e-62ca-49ce-a3-af-db-b2-de-61-b0-68')
    @commethod(3)
    def SetExecutionState(self, dwAdd: UInt32, dwRemove: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ResetIdleTimer(self, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IConsolePowerSink(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('3333759f-fe4f-4975-b1-43-fe-c0-a5-dd-6d-65')
    @commethod(3)
    def OnPowerBroadcast(self, nEvent: UInt32, lParam: Windows.Win32.Foundation.LPARAM, plReturn: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class IConsoleVerb(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('e49f7a60-74af-11d0-a2-86-00-c0-4f-d8-fe-93')
    @commethod(3)
    def GetVerbState(self, eCmdID: Windows.Win32.System.Mmc.MMC_CONSOLE_VERB, nState: Windows.Win32.System.Mmc.MMC_BUTTON_STATE, pState: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetVerbState(self, eCmdID: Windows.Win32.System.Mmc.MMC_CONSOLE_VERB, nState: Windows.Win32.System.Mmc.MMC_BUTTON_STATE, bState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDefaultVerb(self, eCmdID: Windows.Win32.System.Mmc.MMC_CONSOLE_VERB) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDefaultVerb(self, peCmdID: POINTER(Windows.Win32.System.Mmc.MMC_CONSOLE_VERB)) -> Windows.Win32.Foundation.HRESULT: ...
class IContextMenuCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('43136eb7-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(3)
    def AddItem(self, pItem: POINTER(Windows.Win32.System.Mmc.CONTEXTMENUITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IContextMenuCallback2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('e178bc0e-2ed0-4b5e-80-97-42-c9-08-7e-8b-33')
    @commethod(3)
    def AddItem(self, pItem: POINTER(Windows.Win32.System.Mmc.CONTEXTMENUITEM2_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IContextMenuProvider(ComPtr):
    extends: Windows.Win32.System.Mmc.IContextMenuCallback
    _iid_ = Guid('43136eb6-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(4)
    def EmptyMenuList(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddPrimaryExtensionItems(self, piExtension: Windows.Win32.System.Com.IUnknown_head, piDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddThirdPartyExtensionItems(self, piDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowContextMenu(self, hwndParent: Windows.Win32.Foundation.HWND, xPos: Int32, yPos: Int32, plSelected: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IControlbar(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('69fb811e-6c1c-11d0-a2-cb-00-c0-4f-d9-09-dd')
    @commethod(3)
    def Create(self, nType: Windows.Win32.System.Mmc.MMC_CONTROL_TYPE, pExtendControlbar: Windows.Win32.System.Mmc.IExtendControlbar_head, ppUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Attach(self, nType: Windows.Win32.System.Mmc.MMC_CONTROL_TYPE, lpUnknown: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Detach(self, lpUnknown: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDisplayHelp(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('cc593830-b926-11d1-80-63-00-00-f8-75-a9-ce')
    @commethod(3)
    def ShowTopic(self, pszHelpTopic: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumTASK(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('338698b1-5a02-11d1-9f-ec-00-60-08-32-db-4a')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.System.Mmc.MMC_TASK_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.System.Mmc.IEnumTASK_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IExtendContextMenu(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('4f3b7a4f-cfac-11cf-b8-e3-00-c0-4f-d8-d5-b0')
    @commethod(3)
    def AddMenuItems(self, piDataObject: Windows.Win32.System.Com.IDataObject_head, piCallback: Windows.Win32.System.Mmc.IContextMenuCallback_head, pInsertionAllowed: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Command(self, lCommandID: Int32, piDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
class IExtendControlbar(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('49506520-6f40-11d0-a9-8b-00-c0-4f-d8-d5-65')
    @commethod(3)
    def SetControlbar(self, pControlbar: Windows.Win32.System.Mmc.IControlbar_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ControlbarNotify(self, event: Windows.Win32.System.Mmc.MMC_NOTIFY_TYPE, arg: Windows.Win32.Foundation.LPARAM, param2: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
class IExtendPropertySheet(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('85de64dc-ef21-11cf-a2-85-00-c0-4f-d8-db-e6')
    @commethod(3)
    def CreatePropertyPages(self, lpProvider: Windows.Win32.System.Mmc.IPropertySheetCallback_head, handle: IntPtr, lpIDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QueryPagesFor(self, lpDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
class IExtendPropertySheet2(ComPtr):
    extends: Windows.Win32.System.Mmc.IExtendPropertySheet
    _iid_ = Guid('b7a87232-4a51-11d1-a7-ea-00-c0-4f-d9-09-dd')
    @commethod(5)
    def GetWatermarks(self, lpIDataObject: Windows.Win32.System.Com.IDataObject_head, lphWatermark: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP), lphHeader: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP), lphPalette: POINTER(Windows.Win32.Graphics.Gdi.HPALETTE), bStretch: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IExtendTaskPad(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('8dee6511-554d-11d1-9f-ea-00-60-08-32-db-4a')
    @commethod(3)
    def TaskNotify(self, pdo: Windows.Win32.System.Com.IDataObject_head, arg: POINTER(Windows.Win32.System.Variant.VARIANT_head), param2: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumTasks(self, pdo: Windows.Win32.System.Com.IDataObject_head, szTaskGroup: Windows.Win32.Foundation.PWSTR, ppEnumTASK: POINTER(Windows.Win32.System.Mmc.IEnumTASK_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTitle(self, pszGroup: Windows.Win32.Foundation.PWSTR, pszTitle: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDescriptiveText(self, pszGroup: Windows.Win32.Foundation.PWSTR, pszDescriptiveText: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetBackground(self, pszGroup: Windows.Win32.Foundation.PWSTR, pTDO: POINTER(Windows.Win32.System.Mmc.MMC_TASK_DISPLAY_OBJECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetListPadInfo(self, pszGroup: Windows.Win32.Foundation.PWSTR, lpListPadInfo: POINTER(Windows.Win32.System.Mmc.MMC_LISTPAD_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IExtendView(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('89995cee-d2ed-4c0e-ae-5e-df-7e-76-f3-fa-53')
    @commethod(3)
    def GetViews(self, pDataObject: Windows.Win32.System.Com.IDataObject_head, pViewExtensionCallback: Windows.Win32.System.Mmc.IViewExtensionCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
class IHeaderCtrl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('43136eb3-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(3)
    def InsertColumn(self, nCol: Int32, title: Windows.Win32.Foundation.PWSTR, nFormat: Int32, nWidth: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteColumn(self, nCol: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetColumnText(self, nCol: Int32, title: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetColumnText(self, nCol: Int32, pText: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetColumnWidth(self, nCol: Int32, nWidth: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetColumnWidth(self, nCol: Int32, pWidth: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IHeaderCtrl2(ComPtr):
    extends: Windows.Win32.System.Mmc.IHeaderCtrl
    _iid_ = Guid('9757abb8-1b32-11d1-a7-ce-00-c0-4f-d8-d5-65')
    @commethod(9)
    def SetChangeTimeOut(self, uTimeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetColumnFilter(self, nColumn: UInt32, dwType: UInt32, pFilterData: POINTER(Windows.Win32.System.Mmc.MMC_FILTERDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetColumnFilter(self, nColumn: UInt32, pdwType: POINTER(UInt32), pFilterData: POINTER(Windows.Win32.System.Mmc.MMC_FILTERDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IImageList(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('43136eb8-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(3)
    def ImageListSetIcon(self, pIcon: POINTER(IntPtr), nLoc: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ImageListSetStrip(self, pBMapSm: POINTER(IntPtr), pBMapLg: POINTER(IntPtr), nStartLoc: Int32, cMask: Windows.Win32.Foundation.COLORREF) -> Windows.Win32.Foundation.HRESULT: ...
class IMMCVersionInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('a8d2c5fe-cdcb-4b9d-bd-e5-a2-73-43-ff-54-bc')
    @commethod(3)
    def GetMMCVersion(self, pVersionMajor: POINTER(Int32), pVersionMinor: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMenuButton(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('951ed750-d080-11d0-b1-97-00-00-00-00-00-00')
    @commethod(3)
    def AddButton(self, idCommand: Int32, lpButtonText: Windows.Win32.Foundation.PWSTR, lpTooltipText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetButton(self, idCommand: Int32, lpButtonText: Windows.Win32.Foundation.PWSTR, lpTooltipText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetButtonState(self, idCommand: Int32, nState: Windows.Win32.System.Mmc.MMC_BUTTON_STATE, bState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMessageView(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('80f94174-fccc-11d2-b9-91-00-c0-4f-8e-cd-78')
    @commethod(3)
    def SetTitleText(self, pszTitleText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBodyText(self, pszBodyText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetIcon(self, id: Windows.Win32.System.Mmc.IconIdentifier) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
class INodeProperties(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('15bc4d24-a522-4406-aa-55-07-49-53-7a-68-65')
    @commethod(3)
    def GetProperty(self, pDataObject: Windows.Win32.System.Com.IDataObject_head, szPropertyName: Windows.Win32.Foundation.BSTR, pbstrProperty: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertySheetCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('85de64dd-ef21-11cf-a2-85-00-c0-4f-d8-db-e6')
    @commethod(3)
    def AddPage(self, hPage: Windows.Win32.UI.Controls.HPROPSHEETPAGE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemovePage(self, hPage: Windows.Win32.UI.Controls.HPROPSHEETPAGE) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertySheetProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('85de64de-ef21-11cf-a2-85-00-c0-4f-d8-db-e6')
    @commethod(3)
    def CreatePropertySheet(self, title: Windows.Win32.Foundation.PWSTR, type: Byte, cookie: IntPtr, pIDataObjectm: Windows.Win32.System.Com.IDataObject_head, dwOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindPropertySheet(self, hItem: IntPtr, lpComponent: Windows.Win32.System.Mmc.IComponent_head, lpDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddPrimaryPages(self, lpUnknown: Windows.Win32.System.Com.IUnknown_head, bCreateHandle: Windows.Win32.Foundation.BOOL, hNotifyWindow: Windows.Win32.Foundation.HWND, bScopePane: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddExtensionPages(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Show(self, window: IntPtr, page: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IRequiredExtensions(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('72782d7a-a4a0-11d1-af-0f-00-c0-4f-b6-dd-2c')
    @commethod(3)
    def EnableAllExtensions(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFirstExtension(self, pExtCLSID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNextExtension(self, pExtCLSID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IResultData(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('31da5fa0-e0eb-11cf-9f-21-00-aa-00-3c-a9-f6')
    @commethod(3)
    def InsertItem(self, item: POINTER(Windows.Win32.System.Mmc.RESULTDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteItem(self, itemID: IntPtr, nCol: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindItemByLParam(self, lParam: Windows.Win32.Foundation.LPARAM, pItemID: POINTER(IntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteAllRsltItems(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetItem(self, item: POINTER(Windows.Win32.System.Mmc.RESULTDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetItem(self, item: POINTER(Windows.Win32.System.Mmc.RESULTDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNextItem(self, item: POINTER(Windows.Win32.System.Mmc.RESULTDATAITEM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ModifyItemState(self, nIndex: Int32, itemID: IntPtr, uAdd: UInt32, uRemove: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ModifyViewStyle(self, add: Windows.Win32.System.Mmc.MMC_RESULT_VIEW_STYLE, remove: Windows.Win32.System.Mmc.MMC_RESULT_VIEW_STYLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetViewMode(self, lViewMode: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetViewMode(self, lViewMode: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UpdateItem(self, itemID: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Sort(self, nColumn: Int32, dwSortOptions: UInt32, lUserParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetDescBarText(self, DescText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetItemCount(self, nItemCount: Int32, dwOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IResultData2(ComPtr):
    extends: Windows.Win32.System.Mmc.IResultData
    _iid_ = Guid('0f36e0eb-a7f1-4a81-be-5a-92-47-f7-de-4b-1b')
    @commethod(18)
    def RenameResultItem(self, itemID: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IResultDataCompare(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('e8315a52-7a1a-11d0-a2-d2-00-c0-4f-d9-09-dd')
    @commethod(3)
    def Compare(self, lUserParam: Windows.Win32.Foundation.LPARAM, cookieA: IntPtr, cookieB: IntPtr, pnResult: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IResultDataCompareEx(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('96933476-0251-11d3-ae-b0-00-c0-4f-8e-cd-78')
    @commethod(3)
    def Compare(self, prdc: POINTER(Windows.Win32.System.Mmc.RDCOMPARE_head), pnResult: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IResultOwnerData(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9cb396d8-ea83-11d0-ae-f1-00-c0-4f-b6-dd-2c')
    @commethod(3)
    def FindItem(self, pFindInfo: POINTER(Windows.Win32.System.Mmc.RESULTFINDINFO_head), pnFoundIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CacheHint(self, nStartIndex: Int32, nEndIndex: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SortItems(self, nColumn: Int32, dwSortOptions: UInt32, lUserParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
class ISnapinAbout(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('1245208c-a151-11d0-a7-d7-00-c0-4f-d9-09-dd')
    @commethod(3)
    def GetSnapinDescription(self, lpDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProvider(self, lpName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSnapinVersion(self, lpVersion: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSnapinImage(self, hAppIcon: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStaticFolderImage(self, hSmallImage: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP), hSmallImageOpen: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP), hLargeImage: POINTER(Windows.Win32.Graphics.Gdi.HBITMAP), cMask: POINTER(Windows.Win32.Foundation.COLORREF)) -> Windows.Win32.Foundation.HRESULT: ...
class ISnapinHelp(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('a6b15ace-df59-11d0-a7-dd-00-c0-4f-d9-09-dd')
    @commethod(3)
    def GetHelpTopic(self, lpCompiledHelpFile: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISnapinHelp2(ComPtr):
    extends: Windows.Win32.System.Mmc.ISnapinHelp
    _iid_ = Guid('4861a010-20f9-11d2-a5-10-00-c0-4f-b6-dd-2c')
    @commethod(4)
    def GetLinkedTopics(self, lpCompiledHelpFiles: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISnapinProperties(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('f7889da9-4a02-4837-bf-89-1a-6f-2a-02-10-10')
    @commethod(3)
    def Initialize(self, pProperties: Windows.Win32.System.Mmc.Properties_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QueryPropertyNames(self, pCallback: Windows.Win32.System.Mmc.ISnapinPropertiesCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PropertiesChanged(self, cProperties: Int32, pProperties: POINTER(Windows.Win32.System.Mmc.MMC_SNAPIN_PROPERTY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISnapinPropertiesCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('a50fa2e5-7e61-45eb-a8-d4-9a-07-b3-e8-51-a8')
    @commethod(3)
    def AddPropertyName(self, pszPropName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IStringTable(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('de40b7a4-0f65-11d2-8e-25-00-c0-4f-8e-cd-78')
    @commethod(3)
    def AddString(self, pszAdd: Windows.Win32.Foundation.PWSTR, pStringID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetString(self, StringID: UInt32, cchBuffer: UInt32, lpBuffer: Windows.Win32.Foundation.PWSTR, pcchOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStringLength(self, StringID: UInt32, pcchString: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteString(self, StringID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DeleteAllStrings(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindString(self, pszFind: Windows.Win32.Foundation.PWSTR, pStringID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Enumerate(self, ppEnum: POINTER(Windows.Win32.System.Com.IEnumString_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IToolbar(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('43136eb9-d36c-11cf-ad-bc-00-aa-00-a8-00-33')
    @commethod(3)
    def AddBitmap(self, nImages: Int32, hbmp: Windows.Win32.Graphics.Gdi.HBITMAP, cxSize: Int32, cySize: Int32, crMask: Windows.Win32.Foundation.COLORREF) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddButtons(self, nButtons: Int32, lpButtons: POINTER(Windows.Win32.System.Mmc.MMCBUTTON_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InsertButton(self, nIndex: Int32, lpButton: POINTER(Windows.Win32.System.Mmc.MMCBUTTON_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteButton(self, nIndex: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetButtonState(self, idCommand: Int32, nState: Windows.Win32.System.Mmc.MMC_BUTTON_STATE, pState: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetButtonState(self, idCommand: Int32, nState: Windows.Win32.System.Mmc.MMC_BUTTON_STATE, bState: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IViewExtensionCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('34dd928a-7599-41e5-9f-5e-d6-bc-30-62-c2-da')
    @commethod(3)
    def AddView(self, pExtViewData: POINTER(Windows.Win32.System.Mmc.MMC_EXT_VIEW_DATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
IconIdentifier = Int32
Icon_None: IconIdentifier = 0
Icon_Error: IconIdentifier = 32513
Icon_Question: IconIdentifier = 32514
Icon_Warning: IconIdentifier = 32515
Icon_Information: IconIdentifier = 32516
Icon_First: IconIdentifier = 32513
Icon_Last: IconIdentifier = 32516
class MENUBUTTONDATA(EasyCastStructure):
    idCommand: Int32
    x: Int32
    y: Int32
class MMCBUTTON(EasyCastStructure):
    nBitmap: Int32
    idCommand: Int32
    fsState: Byte
    fsType: Byte
    lpButtonText: Windows.Win32.Foundation.PWSTR
    lpTooltipText: Windows.Win32.Foundation.PWSTR
MMCVersionInfo = Guid('d6fedb1d-cf21-4bd9-af-3b-c5-46-8e-9c-66-84')
MMC_ACTION_TYPE = Int32
MMC_ACTION_UNINITIALIZED: MMC_ACTION_TYPE = -1
MMC_ACTION_ID: MMC_ACTION_TYPE = 0
MMC_ACTION_LINK: MMC_ACTION_TYPE = 1
MMC_ACTION_SCRIPT: MMC_ACTION_TYPE = 2
MMC_BUTTON_STATE = Int32
ENABLED: MMC_BUTTON_STATE = 1
CHECKED: MMC_BUTTON_STATE = 2
HIDDEN: MMC_BUTTON_STATE = 4
INDETERMINATE: MMC_BUTTON_STATE = 8
BUTTONPRESSED: MMC_BUTTON_STATE = 16
class MMC_COLUMN_DATA(EasyCastStructure):
    nColIndex: Int32
    dwFlags: UInt32
    nWidth: Int32
    ulReserved: UIntPtr
class MMC_COLUMN_SET_DATA(EasyCastStructure):
    cbSize: Int32
    nNumCols: Int32
    pColData: POINTER(Windows.Win32.System.Mmc.MMC_COLUMN_DATA_head)
MMC_CONSOLE_VERB = Int32
MMC_VERB_NONE: MMC_CONSOLE_VERB = 0
MMC_VERB_OPEN: MMC_CONSOLE_VERB = 32768
MMC_VERB_COPY: MMC_CONSOLE_VERB = 32769
MMC_VERB_PASTE: MMC_CONSOLE_VERB = 32770
MMC_VERB_DELETE: MMC_CONSOLE_VERB = 32771
MMC_VERB_PROPERTIES: MMC_CONSOLE_VERB = 32772
MMC_VERB_RENAME: MMC_CONSOLE_VERB = 32773
MMC_VERB_REFRESH: MMC_CONSOLE_VERB = 32774
MMC_VERB_PRINT: MMC_CONSOLE_VERB = 32775
MMC_VERB_CUT: MMC_CONSOLE_VERB = 32776
MMC_VERB_MAX: MMC_CONSOLE_VERB = 32777
MMC_VERB_FIRST: MMC_CONSOLE_VERB = 32768
MMC_VERB_LAST: MMC_CONSOLE_VERB = 32776
MMC_CONTROL_TYPE = Int32
TOOLBAR: MMC_CONTROL_TYPE = 0
MENUBUTTON: MMC_CONTROL_TYPE = 1
COMBOBOXBAR: MMC_CONTROL_TYPE = 2
class MMC_EXPANDSYNC_STRUCT(EasyCastStructure):
    bHandled: Windows.Win32.Foundation.BOOL
    bExpanding: Windows.Win32.Foundation.BOOL
    hItem: IntPtr
class MMC_EXT_VIEW_DATA(EasyCastStructure):
    viewID: Guid
    pszURL: Windows.Win32.Foundation.PWSTR
    pszViewTitle: Windows.Win32.Foundation.PWSTR
    pszTooltipText: Windows.Win32.Foundation.PWSTR
    bReplacesDefaultView: Windows.Win32.Foundation.BOOL
class MMC_FILTERDATA(EasyCastStructure):
    pszText: Windows.Win32.Foundation.PWSTR
    cchTextMax: Int32
    lValue: Int32
MMC_FILTER_CHANGE_CODE = Int32
MFCC_DISABLE: MMC_FILTER_CHANGE_CODE = 0
MFCC_ENABLE: MMC_FILTER_CHANGE_CODE = 1
MFCC_VALUE_CHANGE: MMC_FILTER_CHANGE_CODE = 2
MMC_FILTER_TYPE = Int32
MMC_STRING_FILTER: MMC_FILTER_TYPE = 0
MMC_INT_FILTER: MMC_FILTER_TYPE = 1
MMC_FILTER_NOVALUE: MMC_FILTER_TYPE = 32768
class MMC_LISTPAD_INFO(EasyCastStructure):
    szTitle: Windows.Win32.Foundation.PWSTR
    szButtonText: Windows.Win32.Foundation.PWSTR
    nCommandID: IntPtr
MMC_MENU_COMMAND_IDS = Int32
MMCC_STANDARD_VIEW_SELECT: MMC_MENU_COMMAND_IDS = -1
MMC_NOTIFY_TYPE = Int32
MMCN_ACTIVATE: MMC_NOTIFY_TYPE = 32769
MMCN_ADD_IMAGES: MMC_NOTIFY_TYPE = 32770
MMCN_BTN_CLICK: MMC_NOTIFY_TYPE = 32771
MMCN_CLICK: MMC_NOTIFY_TYPE = 32772
MMCN_COLUMN_CLICK: MMC_NOTIFY_TYPE = 32773
MMCN_CONTEXTMENU: MMC_NOTIFY_TYPE = 32774
MMCN_CUTORMOVE: MMC_NOTIFY_TYPE = 32775
MMCN_DBLCLICK: MMC_NOTIFY_TYPE = 32776
MMCN_DELETE: MMC_NOTIFY_TYPE = 32777
MMCN_DESELECT_ALL: MMC_NOTIFY_TYPE = 32778
MMCN_EXPAND: MMC_NOTIFY_TYPE = 32779
MMCN_HELP: MMC_NOTIFY_TYPE = 32780
MMCN_MENU_BTNCLICK: MMC_NOTIFY_TYPE = 32781
MMCN_MINIMIZED: MMC_NOTIFY_TYPE = 32782
MMCN_PASTE: MMC_NOTIFY_TYPE = 32783
MMCN_PROPERTY_CHANGE: MMC_NOTIFY_TYPE = 32784
MMCN_QUERY_PASTE: MMC_NOTIFY_TYPE = 32785
MMCN_REFRESH: MMC_NOTIFY_TYPE = 32786
MMCN_REMOVE_CHILDREN: MMC_NOTIFY_TYPE = 32787
MMCN_RENAME: MMC_NOTIFY_TYPE = 32788
MMCN_SELECT: MMC_NOTIFY_TYPE = 32789
MMCN_SHOW: MMC_NOTIFY_TYPE = 32790
MMCN_VIEW_CHANGE: MMC_NOTIFY_TYPE = 32791
MMCN_SNAPINHELP: MMC_NOTIFY_TYPE = 32792
MMCN_CONTEXTHELP: MMC_NOTIFY_TYPE = 32793
MMCN_INITOCX: MMC_NOTIFY_TYPE = 32794
MMCN_FILTER_CHANGE: MMC_NOTIFY_TYPE = 32795
MMCN_FILTERBTN_CLICK: MMC_NOTIFY_TYPE = 32796
MMCN_RESTORE_VIEW: MMC_NOTIFY_TYPE = 32797
MMCN_PRINT: MMC_NOTIFY_TYPE = 32798
MMCN_PRELOAD: MMC_NOTIFY_TYPE = 32799
MMCN_LISTPAD: MMC_NOTIFY_TYPE = 32800
MMCN_EXPANDSYNC: MMC_NOTIFY_TYPE = 32801
MMCN_COLUMNS_CHANGED: MMC_NOTIFY_TYPE = 32802
MMCN_CANPASTE_OUTOFPROC: MMC_NOTIFY_TYPE = 32803
MMC_PROPERTY_ACTION = Int32
MMC_PROPACT_DELETING: MMC_PROPERTY_ACTION = 1
MMC_PROPACT_CHANGING: MMC_PROPERTY_ACTION = 2
MMC_PROPACT_INITIALIZED: MMC_PROPERTY_ACTION = 3
class MMC_RESTORE_VIEW(EasyCastStructure):
    dwSize: UInt32
    cookie: IntPtr
    pViewType: Windows.Win32.Foundation.PWSTR
    lViewOptions: Int32
MMC_RESULT_VIEW_STYLE = Int32
MMC_SINGLESEL: MMC_RESULT_VIEW_STYLE = 1
MMC_SHOWSELALWAYS: MMC_RESULT_VIEW_STYLE = 2
MMC_NOSORTHEADER: MMC_RESULT_VIEW_STYLE = 4
MMC_ENSUREFOCUSVISIBLE: MMC_RESULT_VIEW_STYLE = 8
MMC_SCOPE_ITEM_STATE = Int32
MMC_SCOPE_ITEM_STATE_NORMAL: MMC_SCOPE_ITEM_STATE = 1
MMC_SCOPE_ITEM_STATE_BOLD: MMC_SCOPE_ITEM_STATE = 2
MMC_SCOPE_ITEM_STATE_EXPANDEDONCE: MMC_SCOPE_ITEM_STATE = 3
class MMC_SNAPIN_PROPERTY(EasyCastStructure):
    pszPropName: Windows.Win32.Foundation.PWSTR
    varValue: Windows.Win32.System.Variant.VARIANT
    eAction: Windows.Win32.System.Mmc.MMC_PROPERTY_ACTION
class MMC_SORT_DATA(EasyCastStructure):
    nColIndex: Int32
    dwSortOptions: UInt32
    ulReserved: UIntPtr
class MMC_SORT_SET_DATA(EasyCastStructure):
    cbSize: Int32
    nNumItems: Int32
    pSortData: POINTER(Windows.Win32.System.Mmc.MMC_SORT_DATA_head)
class MMC_TASK(EasyCastStructure):
    sDisplayObject: Windows.Win32.System.Mmc.MMC_TASK_DISPLAY_OBJECT
    szText: Windows.Win32.Foundation.PWSTR
    szHelpString: Windows.Win32.Foundation.PWSTR
    eActionType: Windows.Win32.System.Mmc.MMC_ACTION_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        nCommandID: IntPtr
        szActionURL: Windows.Win32.Foundation.PWSTR
        szScript: Windows.Win32.Foundation.PWSTR
class MMC_TASK_DISPLAY_BITMAP(EasyCastStructure):
    szMouseOverBitmap: Windows.Win32.Foundation.PWSTR
    szMouseOffBitmap: Windows.Win32.Foundation.PWSTR
class MMC_TASK_DISPLAY_OBJECT(EasyCastStructure):
    eDisplayType: Windows.Win32.System.Mmc.MMC_TASK_DISPLAY_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        uBitmap: Windows.Win32.System.Mmc.MMC_TASK_DISPLAY_BITMAP
        uSymbol: Windows.Win32.System.Mmc.MMC_TASK_DISPLAY_SYMBOL
class MMC_TASK_DISPLAY_SYMBOL(EasyCastStructure):
    szFontFamilyName: Windows.Win32.Foundation.PWSTR
    szURLtoEOT: Windows.Win32.Foundation.PWSTR
    szSymbolString: Windows.Win32.Foundation.PWSTR
MMC_TASK_DISPLAY_TYPE = Int32
MMC_TASK_DISPLAY_UNINITIALIZED: MMC_TASK_DISPLAY_TYPE = 0
MMC_TASK_DISPLAY_TYPE_SYMBOL: MMC_TASK_DISPLAY_TYPE = 1
MMC_TASK_DISPLAY_TYPE_VANILLA_GIF: MMC_TASK_DISPLAY_TYPE = 2
MMC_TASK_DISPLAY_TYPE_CHOCOLATE_GIF: MMC_TASK_DISPLAY_TYPE = 3
MMC_TASK_DISPLAY_TYPE_BITMAP: MMC_TASK_DISPLAY_TYPE = 4
MMC_VIEW_TYPE = Int32
MMC_VIEW_TYPE_LIST: MMC_VIEW_TYPE = 0
MMC_VIEW_TYPE_HTML: MMC_VIEW_TYPE = 1
MMC_VIEW_TYPE_OCX: MMC_VIEW_TYPE = 2
class MMC_VISIBLE_COLUMNS(EasyCastStructure):
    nVisibleColumns: Int32
    rgVisibleCols: Int32 * 1
class MenuItem(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('0178fad1-b361-4b27-96-ad-67-c5-7e-bf-2e-1d')
    @commethod(7)
    def get_DisplayName(self, DisplayName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LanguageIndependentName(self, LanguageIndependentName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Path(self, Path: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_LanguageIndependentPath(self, LanguageIndependentPath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Execute(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Enabled(self, Enabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class Node(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('f81ed800-7839-4447-94-5d-8e-15-da-59-ca-55')
    @commethod(7)
    def get_Name(self, Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Property(self, PropertyName: Windows.Win32.Foundation.BSTR, PropertyValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Bookmark(self, Bookmark: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsScopeNode(self, IsScopeNode: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Nodetype(self, Nodetype: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class Nodes(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('313b01df-b22f-4d42-b1-b8-48-3c-dc-f5-1d-35')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, Node: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class Properties(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('2886abc2-a425-42b2-91-c6-e2-5c-0e-04-58-1c')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Name: Windows.Win32.Foundation.BSTR, Property: POINTER(Windows.Win32.System.Mmc.Property_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Remove(self, Name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class Property(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('4600c3a5-e301-41d8-b6-d0-ef-2e-42-12-e0-ca')
    @commethod(7)
    def get_Value(self, Value: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(self, Value: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class RDCOMPARE(EasyCastStructure):
    cbSize: UInt32
    dwFlags: UInt32
    nColumn: Int32
    lUserParam: Windows.Win32.Foundation.LPARAM
    prdch1: POINTER(Windows.Win32.System.Mmc.RDITEMHDR_head)
    prdch2: POINTER(Windows.Win32.System.Mmc.RDITEMHDR_head)
class RDITEMHDR(EasyCastStructure):
    dwFlags: UInt32
    cookie: IntPtr
    lpReserved: Windows.Win32.Foundation.LPARAM
class RESULTDATAITEM(EasyCastStructure):
    mask: UInt32
    bScopeItem: Windows.Win32.Foundation.BOOL
    itemID: IntPtr
    nIndex: Int32
    nCol: Int32
    str: Windows.Win32.Foundation.PWSTR
    nImage: Int32
    nState: UInt32
    lParam: Windows.Win32.Foundation.LPARAM
    iIndent: Int32
class RESULTFINDINFO(EasyCastStructure):
    psz: Windows.Win32.Foundation.PWSTR
    nStart: Int32
    dwOptions: UInt32
class RESULT_VIEW_TYPE_INFO(EasyCastStructure):
    pstrPersistableViewDescription: Windows.Win32.Foundation.PWSTR
    eViewType: Windows.Win32.System.Mmc.MMC_VIEW_TYPE
    dwMiscOptions: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        dwListOptions: UInt32
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        class _Anonymous1_e__Struct(EasyCastStructure):
            dwHTMLOptions: UInt32
            pstrURL: Windows.Win32.Foundation.PWSTR
        class _Anonymous2_e__Struct(EasyCastStructure):
            dwOCXOptions: UInt32
            pUnkControl: Windows.Win32.System.Com.IUnknown_head
class SCOPEDATAITEM(EasyCastStructure):
    mask: UInt32
    displayname: Windows.Win32.Foundation.PWSTR
    nImage: Int32
    nOpenImage: Int32
    nState: UInt32
    cChildren: Int32
    lParam: Windows.Win32.Foundation.LPARAM
    relativeID: IntPtr
    ID: IntPtr
class SColumnSetID(EasyCastStructure):
    dwFlags: UInt32
    cBytes: UInt32
    id: Byte * 1
class SMMCDataObjects(EasyCastStructure):
    count: UInt32
    lpDataObject: Windows.Win32.System.Com.IDataObject_head * 1
class SMMCObjectTypes(EasyCastStructure):
    count: UInt32
    guid: Guid * 1
class SNodeID(EasyCastStructure):
    cBytes: UInt32
    id: Byte * 1
class SNodeID2(EasyCastStructure):
    dwFlags: UInt32
    cBytes: UInt32
    id: Byte * 1
class ScopeNamespace(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('ebbb48dc-1a3b-4d86-b7-86-c2-1b-28-38-90-12')
    @commethod(7)
    def GetParent(self, Node: Windows.Win32.System.Mmc.Node_head, Parent: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetChild(self, Node: Windows.Win32.System.Mmc.Node_head, Child: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetNext(self, Node: Windows.Win32.System.Mmc.Node_head, Next: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRoot(self, Root: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Expand(self, Node: Windows.Win32.System.Mmc.Node_head) -> Windows.Win32.Foundation.HRESULT: ...
class SnapIn(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('3be910f6-3459-49c6-a1-bb-41-e6-be-9d-f3-ea')
    @commethod(7)
    def get_Name(self, Name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Vendor(self, Vendor: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Version(self, Version: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Extensions(self, Extensions: POINTER(Windows.Win32.System.Mmc.Extensions_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SnapinCLSID(self, SnapinCLSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Properties(self, Properties: POINTER(Windows.Win32.System.Mmc.Properties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EnableAllExtensions(self, Enable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class SnapIns(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('2ef3de1d-b12a-49d1-92-c5-0b-00-79-87-68-f1')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, SnapIn: POINTER(Windows.Win32.System.Mmc.SnapIn_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, SnapinNameOrCLSID: Windows.Win32.Foundation.BSTR, ParentSnapin: Windows.Win32.System.Variant.VARIANT, Properties: Windows.Win32.System.Variant.VARIANT, SnapIn: POINTER(Windows.Win32.System.Mmc.SnapIn_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, SnapIn: Windows.Win32.System.Mmc.SnapIn_head) -> Windows.Win32.Foundation.HRESULT: ...
class View(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('6efc2da2-b38c-457e-9a-bb-ed-2d-18-9b-8c-38')
    @commethod(7)
    def get_ActiveScopeNode(self, Node: POINTER(Windows.Win32.System.Mmc.Node_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_ActiveScopeNode(self, Node: Windows.Win32.System.Mmc.Node_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Selection(self, Nodes: POINTER(Windows.Win32.System.Mmc.Nodes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ListItems(self, Nodes: POINTER(Windows.Win32.System.Mmc.Nodes_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SnapinScopeObject(self, ScopeNode: Windows.Win32.System.Variant.VARIANT, ScopeNodeObject: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SnapinSelectionObject(self, SelectionObject: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Is(self, View: Windows.Win32.System.Mmc.View_head, TheSame: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Document(self, Document: POINTER(Windows.Win32.System.Mmc.Document_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SelectAll(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Select(self, Node: Windows.Win32.System.Mmc.Node_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Deselect(self, Node: Windows.Win32.System.Mmc.Node_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def IsSelected(self, Node: Windows.Win32.System.Mmc.Node_head, IsSelected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def DisplayScopeNodePropertySheet(self, ScopeNode: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def DisplaySelectionPropertySheet(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CopyScopeNode(self, ScopeNode: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CopySelection(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def DeleteScopeNode(self, ScopeNode: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def DeleteSelection(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def RenameScopeNode(self, NewName: Windows.Win32.Foundation.BSTR, ScopeNode: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def RenameSelectedItem(self, NewName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_ScopeNodeContextMenu(self, ScopeNode: Windows.Win32.System.Variant.VARIANT, ContextMenu: POINTER(Windows.Win32.System.Mmc.ContextMenu_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_SelectionContextMenu(self, ContextMenu: POINTER(Windows.Win32.System.Mmc.ContextMenu_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def RefreshScopeNode(self, ScopeNode: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def RefreshSelection(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def ExecuteSelectionMenuItem(self, MenuItemPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def ExecuteScopeNodeMenuItem(self, MenuItemPath: Windows.Win32.Foundation.BSTR, ScopeNode: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def ExecuteShellCommand(self, Command: Windows.Win32.Foundation.BSTR, Directory: Windows.Win32.Foundation.BSTR, Parameters: Windows.Win32.Foundation.BSTR, WindowState: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_Frame(self, Frame: POINTER(Windows.Win32.System.Mmc.Frame_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_ScopeTreeVisible(self, Visible: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_ScopeTreeVisible(self, Visible: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def Back(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def Forward(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_StatusBarText(self, StatusBarText: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_Memento(self, Memento: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def ViewMemento(self, Memento: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_Columns(self, Columns: POINTER(Windows.Win32.System.Mmc.Columns_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_CellContents(self, Node: Windows.Win32.System.Mmc.Node_head, Column: Int32, CellContents: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def ExportList(self, File: Windows.Win32.Foundation.BSTR, exportoptions: Windows.Win32.System.Mmc._ExportListOptions) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_ListViewMode(self, Mode: POINTER(Windows.Win32.System.Mmc._ListViewMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_ListViewMode(self, mode: Windows.Win32.System.Mmc._ListViewMode) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_ControlObject(self, Control: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
class Views(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('d6b8c29d-a1ff-4d72-aa-b0-e3-81-e9-b9-33-8d')
    @commethod(7)
    def Item(self, Index: Int32, View: POINTER(Windows.Win32.System.Mmc.View_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Count(self, Count: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Add(self, Node: Windows.Win32.System.Mmc.Node_head, viewOptions: Windows.Win32.System.Mmc._ViewOptions) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get__NewEnum(self, retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class _AppEvents(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('de46cbdd-53f5-4635-af-54-4f-e7-1e-92-3d-3f')
    @commethod(7)
    def OnQuit(self, Application: Windows.Win32.System.Mmc._Application_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnDocumentOpen(self, Document: Windows.Win32.System.Mmc.Document_head, New: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnDocumentClose(self, Document: Windows.Win32.System.Mmc.Document_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnSnapInAdded(self, Document: Windows.Win32.System.Mmc.Document_head, SnapIn: Windows.Win32.System.Mmc.SnapIn_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnSnapInRemoved(self, Document: Windows.Win32.System.Mmc.Document_head, SnapIn: Windows.Win32.System.Mmc.SnapIn_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnNewView(self, View: Windows.Win32.System.Mmc.View_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnViewClose(self, View: Windows.Win32.System.Mmc.View_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnViewChange(self, View: Windows.Win32.System.Mmc.View_head, NewOwnerNode: Windows.Win32.System.Mmc.Node_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnSelectionChange(self, View: Windows.Win32.System.Mmc.View_head, NewNodes: Windows.Win32.System.Mmc.Nodes_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnContextMenuExecuted(self, MenuItem: Windows.Win32.System.Mmc.MenuItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OnToolbarButtonClicked(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def OnListUpdated(self, View: Windows.Win32.System.Mmc.View_head) -> Windows.Win32.Foundation.HRESULT: ...
class _Application(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('a3afb9cc-b653-4741-86-ab-f0-47-0e-c1-38-4c')
    @commethod(7)
    def Help(self) -> Void: ...
    @commethod(8)
    def Quit(self) -> Void: ...
    @commethod(9)
    def get_Document(self, Document: POINTER(Windows.Win32.System.Mmc.Document_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Load(self, Filename: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Frame(self, Frame: POINTER(Windows.Win32.System.Mmc.Frame_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Visible(self, Visible: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Show(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Hide(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_UserControl(self, UserControl: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_UserControl(self, UserControl: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_VersionMajor(self, VersionMajor: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_VersionMinor(self, VersionMinor: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
_ColumnSortOrder = Int32
SortOrder_Ascending: _ColumnSortOrder = 0
SortOrder_Descending: _ColumnSortOrder = 1
_DocumentMode = Int32
DocumentMode_Author: _DocumentMode = 0
DocumentMode_User: _DocumentMode = 1
DocumentMode_User_MDI: _DocumentMode = 2
DocumentMode_User_SDI: _DocumentMode = 3
class _EventConnector(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('c0bccd30-de44-4528-84-03-a0-5a-6a-1c-c8-ea')
    @commethod(7)
    def ConnectTo(self, Application: Windows.Win32.System.Mmc._Application_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Disconnect(self) -> Windows.Win32.Foundation.HRESULT: ...
_ExportListOptions = Int32
ExportListOptions_Default: _ExportListOptions = 0
ExportListOptions_Unicode: _ExportListOptions = 1
ExportListOptions_TabDelimited: _ExportListOptions = 2
ExportListOptions_SelectedItemsOnly: _ExportListOptions = 4
_ListViewMode = Int32
ListMode_Small_Icons: _ListViewMode = 0
ListMode_Large_Icons: _ListViewMode = 1
ListMode_List: _ListViewMode = 2
ListMode_Detail: _ListViewMode = 3
ListMode_Filtered: _ListViewMode = 4
_ViewOptions = Int32
ViewOption_Default: _ViewOptions = 0
ViewOption_ScopeTreeHidden: _ViewOptions = 1
ViewOption_NoToolBars: _ViewOptions = 2
ViewOption_NotPersistable: _ViewOptions = 4
ViewOption_ActionPaneHidden: _ViewOptions = 8
make_head(_module, 'AppEvents')
make_head(_module, 'CONTEXTMENUITEM')
make_head(_module, 'CONTEXTMENUITEM2')
make_head(_module, 'Column')
make_head(_module, 'Columns')
make_head(_module, 'ContextMenu')
make_head(_module, 'Document')
make_head(_module, 'Extension')
make_head(_module, 'Extensions')
make_head(_module, 'Frame')
make_head(_module, 'IColumnData')
make_head(_module, 'IComponent')
make_head(_module, 'IComponent2')
make_head(_module, 'IComponentData')
make_head(_module, 'IComponentData2')
make_head(_module, 'IConsole')
make_head(_module, 'IConsole2')
make_head(_module, 'IConsole3')
make_head(_module, 'IConsoleNameSpace')
make_head(_module, 'IConsoleNameSpace2')
make_head(_module, 'IConsolePower')
make_head(_module, 'IConsolePowerSink')
make_head(_module, 'IConsoleVerb')
make_head(_module, 'IContextMenuCallback')
make_head(_module, 'IContextMenuCallback2')
make_head(_module, 'IContextMenuProvider')
make_head(_module, 'IControlbar')
make_head(_module, 'IDisplayHelp')
make_head(_module, 'IEnumTASK')
make_head(_module, 'IExtendContextMenu')
make_head(_module, 'IExtendControlbar')
make_head(_module, 'IExtendPropertySheet')
make_head(_module, 'IExtendPropertySheet2')
make_head(_module, 'IExtendTaskPad')
make_head(_module, 'IExtendView')
make_head(_module, 'IHeaderCtrl')
make_head(_module, 'IHeaderCtrl2')
make_head(_module, 'IImageList')
make_head(_module, 'IMMCVersionInfo')
make_head(_module, 'IMenuButton')
make_head(_module, 'IMessageView')
make_head(_module, 'INodeProperties')
make_head(_module, 'IPropertySheetCallback')
make_head(_module, 'IPropertySheetProvider')
make_head(_module, 'IRequiredExtensions')
make_head(_module, 'IResultData')
make_head(_module, 'IResultData2')
make_head(_module, 'IResultDataCompare')
make_head(_module, 'IResultDataCompareEx')
make_head(_module, 'IResultOwnerData')
make_head(_module, 'ISnapinAbout')
make_head(_module, 'ISnapinHelp')
make_head(_module, 'ISnapinHelp2')
make_head(_module, 'ISnapinProperties')
make_head(_module, 'ISnapinPropertiesCallback')
make_head(_module, 'IStringTable')
make_head(_module, 'IToolbar')
make_head(_module, 'IViewExtensionCallback')
make_head(_module, 'MENUBUTTONDATA')
make_head(_module, 'MMCBUTTON')
make_head(_module, 'MMC_COLUMN_DATA')
make_head(_module, 'MMC_COLUMN_SET_DATA')
make_head(_module, 'MMC_EXPANDSYNC_STRUCT')
make_head(_module, 'MMC_EXT_VIEW_DATA')
make_head(_module, 'MMC_FILTERDATA')
make_head(_module, 'MMC_LISTPAD_INFO')
make_head(_module, 'MMC_RESTORE_VIEW')
make_head(_module, 'MMC_SNAPIN_PROPERTY')
make_head(_module, 'MMC_SORT_DATA')
make_head(_module, 'MMC_SORT_SET_DATA')
make_head(_module, 'MMC_TASK')
make_head(_module, 'MMC_TASK_DISPLAY_BITMAP')
make_head(_module, 'MMC_TASK_DISPLAY_OBJECT')
make_head(_module, 'MMC_TASK_DISPLAY_SYMBOL')
make_head(_module, 'MMC_VISIBLE_COLUMNS')
make_head(_module, 'MenuItem')
make_head(_module, 'Node')
make_head(_module, 'Nodes')
make_head(_module, 'Properties')
make_head(_module, 'Property')
make_head(_module, 'RDCOMPARE')
make_head(_module, 'RDITEMHDR')
make_head(_module, 'RESULTDATAITEM')
make_head(_module, 'RESULTFINDINFO')
make_head(_module, 'RESULT_VIEW_TYPE_INFO')
make_head(_module, 'SCOPEDATAITEM')
make_head(_module, 'SColumnSetID')
make_head(_module, 'SMMCDataObjects')
make_head(_module, 'SMMCObjectTypes')
make_head(_module, 'SNodeID')
make_head(_module, 'SNodeID2')
make_head(_module, 'ScopeNamespace')
make_head(_module, 'SnapIn')
make_head(_module, 'SnapIns')
make_head(_module, 'View')
make_head(_module, 'Views')
make_head(_module, '_AppEvents')
make_head(_module, '_Application')
make_head(_module, '_EventConnector')
