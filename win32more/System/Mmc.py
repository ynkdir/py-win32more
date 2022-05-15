from win32more import *
import win32more.System.Mmc
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.UI.Controls
import win32more.UI.WindowsAndMessaging

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.System.Mmc, name, globals()[f"_define_{name}"]())
    return getattr(win32more.System.Mmc, name)
def __dir__():
    return __all__
MMC_VER = 512
MMC_PROP_CHANGEAFFECTSUI = 1
MMC_PROP_MODIFIABLE = 2
MMC_PROP_REMOVABLE = 4
MMC_PROP_PERSIST = 8
MMCLV_AUTO = -1
MMCLV_NOPARAM = -2
MMCLV_NOICON = -1
MMCLV_VIEWSTYLE_ICON = 0
MMCLV_VIEWSTYLE_SMALLICON = 2
MMCLV_VIEWSTYLE_LIST = 3
MMCLV_VIEWSTYLE_REPORT = 1
MMCLV_VIEWSTYLE_FILTERED = 4
MMCLV_NOPTR = 0
MMCLV_UPDATE_NOINVALIDATEALL = 1
MMCLV_UPDATE_NOSCROLL = 2
MMC_IMAGECALLBACK = -1
RDI_STR = 2
RDI_IMAGE = 4
RDI_STATE = 8
RDI_PARAM = 16
RDI_INDEX = 32
RDI_INDENT = 64
MMC_VIEW_OPTIONS_NONE = 0
MMC_VIEW_OPTIONS_NOLISTVIEWS = 1
MMC_VIEW_OPTIONS_MULTISELECT = 2
MMC_VIEW_OPTIONS_OWNERDATALIST = 4
MMC_VIEW_OPTIONS_FILTERED = 8
MMC_VIEW_OPTIONS_CREATENEW = 16
MMC_VIEW_OPTIONS_USEFONTLINKING = 32
MMC_VIEW_OPTIONS_EXCLUDE_SCOPE_ITEMS_FROM_LIST = 64
MMC_VIEW_OPTIONS_LEXICAL_SORT = 128
MMC_PSO_NOAPPLYNOW = 1
MMC_PSO_HASHELP = 2
MMC_PSO_NEWWIZARDTYPE = 4
MMC_PSO_NO_PROPTITLE = 8
RFI_PARTIAL = 1
RFI_WRAP = 2
RSI_DESCENDING = 1
RSI_NOSORTICON = 2
SDI_STR = 2
SDI_IMAGE = 4
SDI_OPENIMAGE = 8
SDI_STATE = 16
SDI_PARAM = 32
SDI_CHILDREN = 64
SDI_PARENT = 0
SDI_PREVIOUS = 268435456
SDI_NEXT = 536870912
SDI_FIRST = 134217728
MMC_MULTI_SELECT_COOKIE = -2
MMC_WINDOW_COOKIE = -3
SPECIAL_COOKIE_MIN = -10
SPECIAL_COOKIE_MAX = -1
MMC_NW_OPTION_NONE = 0
MMC_NW_OPTION_NOSCOPEPANE = 1
MMC_NW_OPTION_NOTOOLBARS = 2
MMC_NW_OPTION_SHORTTITLE = 4
MMC_NW_OPTION_CUSTOMTITLE = 8
MMC_NW_OPTION_NOPERSIST = 16
MMC_NW_OPTION_NOACTIONPANE = 32
MMC_NODEID_SLOW_RETRIEVAL = 1
SPECIAL_DOBJ_MIN = -10
SPECIAL_DOBJ_MAX = 0
AUTO_WIDTH = -1
HIDE_COLUMN = -4
ILSIF_LEAVE_LARGE_ICON = 1073741824
ILSIF_LEAVE_SMALL_ICON = 536870912
HDI_HIDDEN = 1
RDCI_ScopeItem = 2147483648
RVTI_MISC_OPTIONS_NOLISTVIEWS = 1
RVTI_LIST_OPTIONS_NONE = 0
RVTI_LIST_OPTIONS_OWNERDATALIST = 2
RVTI_LIST_OPTIONS_MULTISELECT = 4
RVTI_LIST_OPTIONS_FILTERED = 8
RVTI_LIST_OPTIONS_USEFONTLINKING = 32
RVTI_LIST_OPTIONS_EXCLUDE_SCOPE_ITEMS_FROM_LIST = 64
RVTI_LIST_OPTIONS_LEXICAL_SORT = 128
RVTI_LIST_OPTIONS_ALLOWPASTE = 256
RVTI_HTML_OPTIONS_NONE = 0
RVTI_HTML_OPTIONS_NOLISTVIEW = 1
RVTI_OCX_OPTIONS_NONE = 0
RVTI_OCX_OPTIONS_NOLISTVIEW = 1
RVTI_OCX_OPTIONS_CACHE_OCX = 2
MMC_DEFAULT_OPERATION_COPY = 1
MMC_ITEM_OVERLAY_STATE_MASK = 3840
MMC_ITEM_OVERLAY_STATE_SHIFT = 8
MMC_ITEM_STATE_MASK = 255
Application = Guid('49b2791a-b1ae-4c90-9b8e-e860ba07f889')
AppEventsDHTMLConnector = Guid('ade6444b-c91f-4e37-92a4-5bb430a33340')
MMC_PROPERTY_ACTION = Int32
MMC_PROPACT_DELETING = 1
MMC_PROPACT_CHANGING = 2
MMC_PROPACT_INITIALIZED = 3
def _define_MMC_SNAPIN_PROPERTY_head():
    class MMC_SNAPIN_PROPERTY(Structure):
        pass
    return MMC_SNAPIN_PROPERTY
def _define_MMC_SNAPIN_PROPERTY():
    MMC_SNAPIN_PROPERTY = win32more.System.Mmc.MMC_SNAPIN_PROPERTY_head
    MMC_SNAPIN_PROPERTY._fields_ = [
        ("pszPropName", win32more.Foundation.PWSTR),
        ("varValue", win32more.System.Com.VARIANT),
        ("eAction", win32more.System.Mmc.MMC_PROPERTY_ACTION),
    ]
    return MMC_SNAPIN_PROPERTY
def _define_ISnapinProperties_head():
    class ISnapinProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('f7889da9-4a02-4837-bf89-1a6f2a021010')
    return ISnapinProperties
def _define_ISnapinProperties():
    ISnapinProperties = win32more.System.Mmc.ISnapinProperties_head
    ISnapinProperties.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Properties_head, use_last_error=False)(3, 'Initialize', ((1, 'pProperties'),)))
    ISnapinProperties.QueryPropertyNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.ISnapinPropertiesCallback_head, use_last_error=False)(4, 'QueryPropertyNames', ((1, 'pCallback'),)))
    ISnapinProperties.PropertiesChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Mmc.MMC_SNAPIN_PROPERTY), use_last_error=False)(5, 'PropertiesChanged', ((1, 'cProperties'),(1, 'pProperties'),)))
    return ISnapinProperties
def _define_ISnapinPropertiesCallback_head():
    class ISnapinPropertiesCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('a50fa2e5-7e61-45eb-a8d4-9a07b3e851a8')
    return ISnapinPropertiesCallback
def _define_ISnapinPropertiesCallback():
    ISnapinPropertiesCallback = win32more.System.Mmc.ISnapinPropertiesCallback_head
    ISnapinPropertiesCallback.AddPropertyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(3, 'AddPropertyName', ((1, 'pszPropName'),(1, 'dwFlags'),)))
    return ISnapinPropertiesCallback
_DocumentMode = Int32
DocumentMode_Author = 0
DocumentMode_User = 1
DocumentMode_User_MDI = 2
DocumentMode_User_SDI = 3
_ListViewMode = Int32
ListMode_Small_Icons = 0
ListMode_Large_Icons = 1
ListMode_List = 2
ListMode_Detail = 3
ListMode_Filtered = 4
_ViewOptions = Int32
ViewOption_Default = 0
ViewOption_ScopeTreeHidden = 1
ViewOption_NoToolBars = 2
ViewOption_NotPersistable = 4
ViewOption_ActionPaneHidden = 8
_ExportListOptions = Int32
ExportListOptions_Default = 0
ExportListOptions_Unicode = 1
ExportListOptions_TabDelimited = 2
ExportListOptions_SelectedItemsOnly = 4
def _define__Application_head():
    class _Application(win32more.System.Com.IDispatch_head):
        Guid = Guid('a3afb9cc-b653-4741-86ab-f0470ec1384c')
    return _Application
def _define__Application():
    _Application = win32more.System.Mmc._Application_head
    _Application.Help = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(7, 'Help', ()))
    _Application.Quit = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(8, 'Quit', ()))
    _Application.get_Document = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Document_head), use_last_error=False)(9, 'get_Document', ((1, 'Document'),)))
    _Application.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'Load', ((1, 'Filename'),)))
    _Application.get_Frame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Frame_head), use_last_error=False)(11, 'get_Frame', ((1, 'Frame'),)))
    _Application.get_Visible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'get_Visible', ((1, 'Visible'),)))
    _Application.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'Show', ()))
    _Application.Hide = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'Hide', ()))
    _Application.get_UserControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(15, 'get_UserControl', ((1, 'UserControl'),)))
    _Application.put_UserControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(16, 'put_UserControl', ((1, 'UserControl'),)))
    _Application.get_VersionMajor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_VersionMajor', ((1, 'VersionMajor'),)))
    _Application.get_VersionMinor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(18, 'get_VersionMinor', ((1, 'VersionMinor'),)))
    return _Application
def _define__AppEvents_head():
    class _AppEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('de46cbdd-53f5-4635-af54-4fe71e923d3f')
    return _AppEvents
def _define__AppEvents():
    _AppEvents = win32more.System.Mmc._AppEvents_head
    _AppEvents.OnQuit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc._Application_head, use_last_error=False)(7, 'OnQuit', ((1, 'Application'),)))
    _AppEvents.OnDocumentOpen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Document_head,win32more.Foundation.BOOL, use_last_error=False)(8, 'OnDocumentOpen', ((1, 'Document'),(1, 'New'),)))
    _AppEvents.OnDocumentClose = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Document_head, use_last_error=False)(9, 'OnDocumentClose', ((1, 'Document'),)))
    _AppEvents.OnSnapInAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Document_head,win32more.System.Mmc.SnapIn_head, use_last_error=False)(10, 'OnSnapInAdded', ((1, 'Document'),(1, 'SnapIn'),)))
    _AppEvents.OnSnapInRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Document_head,win32more.System.Mmc.SnapIn_head, use_last_error=False)(11, 'OnSnapInRemoved', ((1, 'Document'),(1, 'SnapIn'),)))
    _AppEvents.OnNewView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.View_head, use_last_error=False)(12, 'OnNewView', ((1, 'View'),)))
    _AppEvents.OnViewClose = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.View_head, use_last_error=False)(13, 'OnViewClose', ((1, 'View'),)))
    _AppEvents.OnViewChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.View_head,win32more.System.Mmc.Node_head, use_last_error=False)(14, 'OnViewChange', ((1, 'View'),(1, 'NewOwnerNode'),)))
    _AppEvents.OnSelectionChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.View_head,win32more.System.Mmc.Nodes_head, use_last_error=False)(15, 'OnSelectionChange', ((1, 'View'),(1, 'NewNodes'),)))
    _AppEvents.OnContextMenuExecuted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.MenuItem_head, use_last_error=False)(16, 'OnContextMenuExecuted', ((1, 'MenuItem'),)))
    _AppEvents.OnToolbarButtonClicked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'OnToolbarButtonClicked', ()))
    _AppEvents.OnListUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.View_head, use_last_error=False)(18, 'OnListUpdated', ((1, 'View'),)))
    return _AppEvents
def _define_AppEvents_head():
    class AppEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('fc7a4252-78ac-4532-8c5a-563cfe138863')
    return AppEvents
def _define_AppEvents():
    AppEvents = win32more.System.Mmc.AppEvents_head
    return AppEvents
def _define__EventConnector_head():
    class _EventConnector(win32more.System.Com.IDispatch_head):
        Guid = Guid('c0bccd30-de44-4528-8403-a05a6a1cc8ea')
    return _EventConnector
def _define__EventConnector():
    _EventConnector = win32more.System.Mmc._EventConnector_head
    _EventConnector.ConnectTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc._Application_head, use_last_error=False)(7, 'ConnectTo', ((1, 'Application'),)))
    _EventConnector.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Disconnect', ()))
    return _EventConnector
def _define_Frame_head():
    class Frame(win32more.System.Com.IDispatch_head):
        Guid = Guid('e5e2d970-5bb3-4306-8804-b0968a31c8e6')
    return Frame
def _define_Frame():
    Frame = win32more.System.Mmc.Frame_head
    Frame.Maximize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Maximize', ()))
    Frame.Minimize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Minimize', ()))
    Frame.Restore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Restore', ()))
    Frame.get_Top = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_Top', ((1, 'Top'),)))
    Frame.put_Top = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'put_Top', ((1, 'top'),)))
    Frame.get_Bottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_Bottom', ((1, 'Bottom'),)))
    Frame.put_Bottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'put_Bottom', ((1, 'bottom'),)))
    Frame.get_Left = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'get_Left', ((1, 'Left'),)))
    Frame.put_Left = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(15, 'put_Left', ((1, 'left'),)))
    Frame.get_Right = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'get_Right', ((1, 'Right'),)))
    Frame.put_Right = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(17, 'put_Right', ((1, 'right'),)))
    return Frame
def _define_Node_head():
    class Node(win32more.System.Com.IDispatch_head):
        Guid = Guid('f81ed800-7839-4447-945d-8e15da59ca55')
    return Node
def _define_Node():
    Node = win32more.System.Mmc.Node_head
    Node.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(7, 'get_Name', ((1, 'Name'),)))
    Node.get_Property = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(POINTER(UInt16)), use_last_error=False)(8, 'get_Property', ((1, 'PropertyName'),(1, 'PropertyValue'),)))
    Node.get_Bookmark = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(9, 'get_Bookmark', ((1, 'Bookmark'),)))
    Node.IsScopeNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(10, 'IsScopeNode', ((1, 'IsScopeNode'),)))
    Node.get_Nodetype = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(11, 'get_Nodetype', ((1, 'Nodetype'),)))
    return Node
def _define_ScopeNamespace_head():
    class ScopeNamespace(win32more.System.Com.IDispatch_head):
        Guid = Guid('ebbb48dc-1a3b-4d86-b786-c21b28389012')
    return ScopeNamespace
def _define_ScopeNamespace():
    ScopeNamespace = win32more.System.Mmc.ScopeNamespace_head
    ScopeNamespace.GetParent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Node_head,POINTER(win32more.System.Mmc.Node_head), use_last_error=False)(7, 'GetParent', ((1, 'Node'),(1, 'Parent'),)))
    ScopeNamespace.GetChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Node_head,POINTER(win32more.System.Mmc.Node_head), use_last_error=False)(8, 'GetChild', ((1, 'Node'),(1, 'Child'),)))
    ScopeNamespace.GetNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Node_head,POINTER(win32more.System.Mmc.Node_head), use_last_error=False)(9, 'GetNext', ((1, 'Node'),(1, 'Next'),)))
    ScopeNamespace.GetRoot = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Node_head), use_last_error=False)(10, 'GetRoot', ((1, 'Root'),)))
    ScopeNamespace.Expand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Node_head, use_last_error=False)(11, 'Expand', ((1, 'Node'),)))
    return ScopeNamespace
def _define_Document_head():
    class Document(win32more.System.Com.IDispatch_head):
        Guid = Guid('225120d6-1e0f-40a3-93fe-1079e6a8017b')
    return Document
def _define_Document():
    Document = win32more.System.Mmc.Document_head
    Document.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Save', ()))
    Document.SaveAs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'SaveAs', ((1, 'Filename'),)))
    Document.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(9, 'Close', ((1, 'SaveChanges'),)))
    Document.get_Views = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Views_head), use_last_error=False)(10, 'get_Views', ((1, 'Views'),)))
    Document.get_SnapIns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.SnapIns_head), use_last_error=False)(11, 'get_SnapIns', ((1, 'SnapIns'),)))
    Document.get_ActiveView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.View_head), use_last_error=False)(12, 'get_ActiveView', ((1, 'View'),)))
    Document.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(13, 'get_Name', ((1, 'Name'),)))
    Document.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'put_Name', ((1, 'Name'),)))
    Document.get_Location = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(15, 'get_Location', ((1, 'Location'),)))
    Document.get_IsSaved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(16, 'get_IsSaved', ((1, 'IsSaved'),)))
    Document.get_Mode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc._DocumentMode), use_last_error=False)(17, 'get_Mode', ((1, 'Mode'),)))
    Document.put_Mode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc._DocumentMode, use_last_error=False)(18, 'put_Mode', ((1, 'Mode'),)))
    Document.get_RootNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Node_head), use_last_error=False)(19, 'get_RootNode', ((1, 'Node'),)))
    Document.get_ScopeNamespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.ScopeNamespace_head), use_last_error=False)(20, 'get_ScopeNamespace', ((1, 'ScopeNamespace'),)))
    Document.CreateProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Properties_head), use_last_error=False)(21, 'CreateProperties', ((1, 'Properties'),)))
    Document.get_Application = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc._Application_head), use_last_error=False)(22, 'get_Application', ((1, 'Application'),)))
    return Document
def _define_SnapIn_head():
    class SnapIn(win32more.System.Com.IDispatch_head):
        Guid = Guid('3be910f6-3459-49c6-a1bb-41e6be9df3ea')
    return SnapIn
def _define_SnapIn():
    SnapIn = win32more.System.Mmc.SnapIn_head
    SnapIn.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(7, 'get_Name', ((1, 'Name'),)))
    SnapIn.get_Vendor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(8, 'get_Vendor', ((1, 'Vendor'),)))
    SnapIn.get_Version = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(9, 'get_Version', ((1, 'Version'),)))
    SnapIn.get_Extensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Extensions_head), use_last_error=False)(10, 'get_Extensions', ((1, 'Extensions'),)))
    SnapIn.get_SnapinCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(11, 'get_SnapinCLSID', ((1, 'SnapinCLSID'),)))
    SnapIn.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Properties_head), use_last_error=False)(12, 'get_Properties', ((1, 'Properties'),)))
    SnapIn.EnableAllExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(13, 'EnableAllExtensions', ((1, 'Enable'),)))
    return SnapIn
def _define_SnapIns_head():
    class SnapIns(win32more.System.Com.IDispatch_head):
        Guid = Guid('2ef3de1d-b12a-49d1-92c5-0b00798768f1')
    return SnapIns
def _define_SnapIns():
    SnapIns = win32more.System.Mmc.SnapIns_head
    SnapIns.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'retval'),)))
    SnapIns.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Mmc.SnapIn_head), use_last_error=False)(8, 'Item', ((1, 'Index'),(1, 'SnapIn'),)))
    SnapIns.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'Count'),)))
    SnapIns.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,POINTER(win32more.System.Mmc.SnapIn_head), use_last_error=False)(10, 'Add', ((1, 'SnapinNameOrCLSID'),(1, 'ParentSnapin'),(1, 'Properties'),(1, 'SnapIn'),)))
    SnapIns.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.SnapIn_head, use_last_error=False)(11, 'Remove', ((1, 'SnapIn'),)))
    return SnapIns
def _define_Extension_head():
    class Extension(win32more.System.Com.IDispatch_head):
        Guid = Guid('ad4d6ca6-912f-409b-a26e-7fd234aef542')
    return Extension
def _define_Extension():
    Extension = win32more.System.Mmc.Extension_head
    Extension.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(7, 'get_Name', ((1, 'Name'),)))
    Extension.get_Vendor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(8, 'get_Vendor', ((1, 'Vendor'),)))
    Extension.get_Version = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(9, 'get_Version', ((1, 'Version'),)))
    Extension.get_Extensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Extensions_head), use_last_error=False)(10, 'get_Extensions', ((1, 'Extensions'),)))
    Extension.get_SnapinCLSID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(11, 'get_SnapinCLSID', ((1, 'SnapinCLSID'),)))
    Extension.EnableAllExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(12, 'EnableAllExtensions', ((1, 'Enable'),)))
    Extension.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(13, 'Enable', ((1, 'Enable'),)))
    return Extension
def _define_Extensions_head():
    class Extensions(win32more.System.Com.IDispatch_head):
        Guid = Guid('82dbea43-8ca4-44bc-a2ca-d18741059ec8')
    return Extensions
def _define_Extensions():
    Extensions = win32more.System.Mmc.Extensions_head
    Extensions.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'retval'),)))
    Extensions.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Mmc.Extension_head), use_last_error=False)(8, 'Item', ((1, 'Index'),(1, 'Extension'),)))
    Extensions.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'Count'),)))
    return Extensions
def _define_Columns_head():
    class Columns(win32more.System.Com.IDispatch_head):
        Guid = Guid('383d4d97-fc44-478b-b139-6323dc48611c')
    return Columns
def _define_Columns():
    Columns = win32more.System.Mmc.Columns_head
    Columns.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Mmc.Column_head), use_last_error=False)(7, 'Item', ((1, 'Index'),(1, 'Column'),)))
    Columns.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'Count'),)))
    Columns.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'retval'),)))
    return Columns
_ColumnSortOrder = Int32
SortOrder_Ascending = 0
SortOrder_Descending = 1
def _define_Column_head():
    class Column(win32more.System.Com.IDispatch_head):
        Guid = Guid('fd1c5f63-2b16-4d06-9ab3-f45350b940ab')
    return Column
def _define_Column():
    Column = win32more.System.Mmc.Column_head
    Column.Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'Name', ((1, 'Name'),)))
    Column.get_Width = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Width', ((1, 'Width'),)))
    Column.put_Width = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(9, 'put_Width', ((1, 'Width'),)))
    Column.get_DisplayPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_DisplayPosition', ((1, 'DisplayPosition'),)))
    Column.put_DisplayPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'put_DisplayPosition', ((1, 'Index'),)))
    Column.get_Hidden = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'get_Hidden', ((1, 'Hidden'),)))
    Column.put_Hidden = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(13, 'put_Hidden', ((1, 'Hidden'),)))
    Column.SetAsSortColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc._ColumnSortOrder, use_last_error=False)(14, 'SetAsSortColumn', ((1, 'SortOrder'),)))
    Column.IsSortColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(15, 'IsSortColumn', ((1, 'IsSortColumn'),)))
    return Column
def _define_Views_head():
    class Views(win32more.System.Com.IDispatch_head):
        Guid = Guid('d6b8c29d-a1ff-4d72-aab0-e381e9b9338d')
    return Views
def _define_Views():
    Views = win32more.System.Mmc.Views_head
    Views.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Mmc.View_head), use_last_error=False)(7, 'Item', ((1, 'Index'),(1, 'View'),)))
    Views.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_Count', ((1, 'Count'),)))
    Views.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Node_head,win32more.System.Mmc._ViewOptions, use_last_error=False)(9, 'Add', ((1, 'Node'),(1, 'viewOptions'),)))
    Views.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(10, 'get__NewEnum', ((1, 'retval'),)))
    return Views
def _define_View_head():
    class View(win32more.System.Com.IDispatch_head):
        Guid = Guid('6efc2da2-b38c-457e-9abb-ed2d189b8c38')
    return View
def _define_View():
    View = win32more.System.Mmc.View_head
    View.get_ActiveScopeNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Node_head), use_last_error=False)(7, 'get_ActiveScopeNode', ((1, 'Node'),)))
    View.put_ActiveScopeNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Node_head, use_last_error=False)(8, 'put_ActiveScopeNode', ((1, 'Node'),)))
    View.get_Selection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Nodes_head), use_last_error=False)(9, 'get_Selection', ((1, 'Nodes'),)))
    View.get_ListItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Nodes_head), use_last_error=False)(10, 'get_ListItems', ((1, 'Nodes'),)))
    View.SnapinScopeObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(11, 'SnapinScopeObject', ((1, 'ScopeNode'),(1, 'ScopeNodeObject'),)))
    View.SnapinSelectionObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(12, 'SnapinSelectionObject', ((1, 'SelectionObject'),)))
    View.Is = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.View_head,POINTER(Int16), use_last_error=False)(13, 'Is', ((1, 'View'),(1, 'TheSame'),)))
    View.get_Document = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Document_head), use_last_error=False)(14, 'get_Document', ((1, 'Document'),)))
    View.SelectAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'SelectAll', ()))
    View.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Node_head, use_last_error=False)(16, 'Select', ((1, 'Node'),)))
    View.Deselect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Node_head, use_last_error=False)(17, 'Deselect', ((1, 'Node'),)))
    View.IsSelected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Node_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(18, 'IsSelected', ((1, 'Node'),(1, 'IsSelected'),)))
    View.DisplayScopeNodePropertySheet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(19, 'DisplayScopeNodePropertySheet', ((1, 'ScopeNode'),)))
    View.DisplaySelectionPropertySheet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(20, 'DisplaySelectionPropertySheet', ()))
    View.CopyScopeNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(21, 'CopyScopeNode', ((1, 'ScopeNode'),)))
    View.CopySelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(22, 'CopySelection', ()))
    View.DeleteScopeNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(23, 'DeleteScopeNode', ((1, 'ScopeNode'),)))
    View.DeleteSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(24, 'DeleteSelection', ()))
    View.RenameScopeNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(25, 'RenameScopeNode', ((1, 'NewName'),(1, 'ScopeNode'),)))
    View.RenameSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(26, 'RenameSelectedItem', ((1, 'NewName'),)))
    View.get_ScopeNodeContextMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Mmc.ContextMenu_head), use_last_error=False)(27, 'get_ScopeNodeContextMenu', ((1, 'ScopeNode'),(1, 'ContextMenu'),)))
    View.get_SelectionContextMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.ContextMenu_head), use_last_error=False)(28, 'get_SelectionContextMenu', ((1, 'ContextMenu'),)))
    View.RefreshScopeNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(29, 'RefreshScopeNode', ((1, 'ScopeNode'),)))
    View.RefreshSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(30, 'RefreshSelection', ()))
    View.ExecuteSelectionMenuItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(31, 'ExecuteSelectionMenuItem', ((1, 'MenuItemPath'),)))
    View.ExecuteScopeNodeMenuItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT, use_last_error=False)(32, 'ExecuteScopeNodeMenuItem', ((1, 'MenuItemPath'),(1, 'ScopeNode'),)))
    View.ExecuteShellCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(33, 'ExecuteShellCommand', ((1, 'Command'),(1, 'Directory'),(1, 'Parameters'),(1, 'WindowState'),)))
    View.get_Frame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Frame_head), use_last_error=False)(34, 'get_Frame', ((1, 'Frame'),)))
    View.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(35, 'Close', ()))
    View.get_ScopeTreeVisible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(36, 'get_ScopeTreeVisible', ((1, 'Visible'),)))
    View.put_ScopeTreeVisible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(37, 'put_ScopeTreeVisible', ((1, 'Visible'),)))
    View.Back = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(38, 'Back', ()))
    View.Forward = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(39, 'Forward', ()))
    View.put_StatusBarText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(40, 'put_StatusBarText', ((1, 'StatusBarText'),)))
    View.get_Memento = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(41, 'get_Memento', ((1, 'Memento'),)))
    View.ViewMemento = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(42, 'ViewMemento', ((1, 'Memento'),)))
    View.get_Columns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.Columns_head), use_last_error=False)(43, 'get_Columns', ((1, 'Columns'),)))
    View.get_CellContents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.Node_head,Int32,POINTER(POINTER(UInt16)), use_last_error=False)(44, 'get_CellContents', ((1, 'Node'),(1, 'Column'),(1, 'CellContents'),)))
    View.ExportList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Mmc._ExportListOptions, use_last_error=False)(45, 'ExportList', ((1, 'File'),(1, 'exportoptions'),)))
    View.get_ListViewMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc._ListViewMode), use_last_error=False)(46, 'get_ListViewMode', ((1, 'Mode'),)))
    View.put_ListViewMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc._ListViewMode, use_last_error=False)(47, 'put_ListViewMode', ((1, 'mode'),)))
    View.get_ControlObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(48, 'get_ControlObject', ((1, 'Control'),)))
    return View
def _define_Nodes_head():
    class Nodes(win32more.System.Com.IDispatch_head):
        Guid = Guid('313b01df-b22f-4d42-b1b8-483cdcf51d35')
    return Nodes
def _define_Nodes():
    Nodes = win32more.System.Mmc.Nodes_head
    Nodes.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'retval'),)))
    Nodes.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Mmc.Node_head), use_last_error=False)(8, 'Item', ((1, 'Index'),(1, 'Node'),)))
    Nodes.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'Count'),)))
    return Nodes
def _define_ContextMenu_head():
    class ContextMenu(win32more.System.Com.IDispatch_head):
        Guid = Guid('dab39ce0-25e6-4e07-8362-ba9c95706545')
    return ContextMenu
def _define_ContextMenu():
    ContextMenu = win32more.System.Mmc.ContextMenu_head
    ContextMenu.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'retval'),)))
    ContextMenu.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Mmc.MenuItem_head), use_last_error=False)(8, 'get_Item', ((1, 'IndexOrPath'),(1, 'MenuItem'),)))
    ContextMenu.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'Count'),)))
    return ContextMenu
def _define_MenuItem_head():
    class MenuItem(win32more.System.Com.IDispatch_head):
        Guid = Guid('0178fad1-b361-4b27-96ad-67c57ebf2e1d')
    return MenuItem
def _define_MenuItem():
    MenuItem = win32more.System.Mmc.MenuItem_head
    MenuItem.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(7, 'get_DisplayName', ((1, 'DisplayName'),)))
    MenuItem.get_LanguageIndependentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(8, 'get_LanguageIndependentName', ((1, 'LanguageIndependentName'),)))
    MenuItem.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(9, 'get_Path', ((1, 'Path'),)))
    MenuItem.get_LanguageIndependentPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(10, 'get_LanguageIndependentPath', ((1, 'LanguageIndependentPath'),)))
    MenuItem.Execute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Execute', ()))
    MenuItem.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'get_Enabled', ((1, 'Enabled'),)))
    return MenuItem
def _define_Properties_head():
    class Properties(win32more.System.Com.IDispatch_head):
        Guid = Guid('2886abc2-a425-42b2-91c6-e25c0e04581c')
    return Properties
def _define_Properties():
    Properties = win32more.System.Mmc.Properties_head
    Properties.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'retval'),)))
    Properties.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Mmc.Property_head), use_last_error=False)(8, 'Item', ((1, 'Name'),(1, 'Property'),)))
    Properties.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'Count'),)))
    Properties.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'Remove', ((1, 'Name'),)))
    return Properties
def _define_Property_head():
    class Property(win32more.System.Com.IDispatch_head):
        Guid = Guid('4600c3a5-e301-41d8-b6d0-ef2e4212e0ca')
    return Property
def _define_Property():
    Property = win32more.System.Mmc.Property_head
    Property.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Value', ((1, 'Value'),)))
    Property.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(8, 'put_Value', ((1, 'Value'),)))
    Property.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)), use_last_error=False)(9, 'get_Name', ((1, 'Name'),)))
    return Property
MMCVersionInfo = Guid('d6fedb1d-cf21-4bd9-af3b-c5468e9c6684')
ConsolePower = Guid('f0285374-dff1-11d3-b433-00c04f8ecd78')
MMC_RESULT_VIEW_STYLE = Int32
MMC_SINGLESEL = 1
MMC_SHOWSELALWAYS = 2
MMC_NOSORTHEADER = 4
MMC_ENSUREFOCUSVISIBLE = 8
MMC_CONTROL_TYPE = Int32
TOOLBAR = 0
MENUBUTTON = 1
COMBOBOXBAR = 2
MMC_CONSOLE_VERB = Int32
MMC_VERB_NONE = 0
MMC_VERB_OPEN = 32768
MMC_VERB_COPY = 32769
MMC_VERB_PASTE = 32770
MMC_VERB_DELETE = 32771
MMC_VERB_PROPERTIES = 32772
MMC_VERB_RENAME = 32773
MMC_VERB_REFRESH = 32774
MMC_VERB_PRINT = 32775
MMC_VERB_CUT = 32776
MMC_VERB_MAX = 32777
MMC_VERB_FIRST = 32768
MMC_VERB_LAST = 32776
def _define_MMCBUTTON_head():
    class MMCBUTTON(Structure):
        pass
    return MMCBUTTON
def _define_MMCBUTTON():
    MMCBUTTON = win32more.System.Mmc.MMCBUTTON_head
    MMCBUTTON._fields_ = [
        ("nBitmap", Int32),
        ("idCommand", Int32),
        ("fsState", Byte),
        ("fsType", Byte),
        ("lpButtonText", win32more.Foundation.PWSTR),
        ("lpTooltipText", win32more.Foundation.PWSTR),
    ]
    return MMCBUTTON
MMC_BUTTON_STATE = Int32
ENABLED = 1
CHECKED = 2
HIDDEN = 4
INDETERMINATE = 8
BUTTONPRESSED = 16
def _define_RESULTDATAITEM_head():
    class RESULTDATAITEM(Structure):
        pass
    return RESULTDATAITEM
def _define_RESULTDATAITEM():
    RESULTDATAITEM = win32more.System.Mmc.RESULTDATAITEM_head
    RESULTDATAITEM._fields_ = [
        ("mask", UInt32),
        ("bScopeItem", win32more.Foundation.BOOL),
        ("itemID", IntPtr),
        ("nIndex", Int32),
        ("nCol", Int32),
        ("str", win32more.Foundation.PWSTR),
        ("nImage", Int32),
        ("nState", UInt32),
        ("lParam", win32more.Foundation.LPARAM),
        ("iIndent", Int32),
    ]
    return RESULTDATAITEM
def _define_RESULTFINDINFO_head():
    class RESULTFINDINFO(Structure):
        pass
    return RESULTFINDINFO
def _define_RESULTFINDINFO():
    RESULTFINDINFO = win32more.System.Mmc.RESULTFINDINFO_head
    RESULTFINDINFO._fields_ = [
        ("psz", win32more.Foundation.PWSTR),
        ("nStart", Int32),
        ("dwOptions", UInt32),
    ]
    return RESULTFINDINFO
def _define_SCOPEDATAITEM_head():
    class SCOPEDATAITEM(Structure):
        pass
    return SCOPEDATAITEM
def _define_SCOPEDATAITEM():
    SCOPEDATAITEM = win32more.System.Mmc.SCOPEDATAITEM_head
    SCOPEDATAITEM._fields_ = [
        ("mask", UInt32),
        ("displayname", win32more.Foundation.PWSTR),
        ("nImage", Int32),
        ("nOpenImage", Int32),
        ("nState", UInt32),
        ("cChildren", Int32),
        ("lParam", win32more.Foundation.LPARAM),
        ("relativeID", IntPtr),
        ("ID", IntPtr),
    ]
    return SCOPEDATAITEM
MMC_SCOPE_ITEM_STATE = Int32
MMC_SCOPE_ITEM_STATE_NORMAL = 1
MMC_SCOPE_ITEM_STATE_BOLD = 2
MMC_SCOPE_ITEM_STATE_EXPANDEDONCE = 3
def _define_CONTEXTMENUITEM_head():
    class CONTEXTMENUITEM(Structure):
        pass
    return CONTEXTMENUITEM
def _define_CONTEXTMENUITEM():
    CONTEXTMENUITEM = win32more.System.Mmc.CONTEXTMENUITEM_head
    CONTEXTMENUITEM._fields_ = [
        ("strName", win32more.Foundation.PWSTR),
        ("strStatusBarText", win32more.Foundation.PWSTR),
        ("lCommandID", Int32),
        ("lInsertionPointID", Int32),
        ("fFlags", Int32),
        ("fSpecialFlags", Int32),
    ]
    return CONTEXTMENUITEM
MMC_MENU_COMMAND_IDS = Int32
MMCC_STANDARD_VIEW_SELECT = -1
def _define_MENUBUTTONDATA_head():
    class MENUBUTTONDATA(Structure):
        pass
    return MENUBUTTONDATA
def _define_MENUBUTTONDATA():
    MENUBUTTONDATA = win32more.System.Mmc.MENUBUTTONDATA_head
    MENUBUTTONDATA._fields_ = [
        ("idCommand", Int32),
        ("x", Int32),
        ("y", Int32),
    ]
    return MENUBUTTONDATA
MMC_FILTER_TYPE = Int32
MMC_STRING_FILTER = 0
MMC_INT_FILTER = 1
MMC_FILTER_NOVALUE = 32768
def _define_MMC_FILTERDATA_head():
    class MMC_FILTERDATA(Structure):
        pass
    return MMC_FILTERDATA
def _define_MMC_FILTERDATA():
    MMC_FILTERDATA = win32more.System.Mmc.MMC_FILTERDATA_head
    MMC_FILTERDATA._fields_ = [
        ("pszText", win32more.Foundation.PWSTR),
        ("cchTextMax", Int32),
        ("lValue", Int32),
    ]
    return MMC_FILTERDATA
MMC_FILTER_CHANGE_CODE = Int32
MFCC_DISABLE = 0
MFCC_ENABLE = 1
MFCC_VALUE_CHANGE = 2
def _define_MMC_RESTORE_VIEW_head():
    class MMC_RESTORE_VIEW(Structure):
        pass
    return MMC_RESTORE_VIEW
def _define_MMC_RESTORE_VIEW():
    MMC_RESTORE_VIEW = win32more.System.Mmc.MMC_RESTORE_VIEW_head
    MMC_RESTORE_VIEW._fields_ = [
        ("dwSize", UInt32),
        ("cookie", IntPtr),
        ("pViewType", win32more.Foundation.PWSTR),
        ("lViewOptions", Int32),
    ]
    return MMC_RESTORE_VIEW
def _define_MMC_EXPANDSYNC_STRUCT_head():
    class MMC_EXPANDSYNC_STRUCT(Structure):
        pass
    return MMC_EXPANDSYNC_STRUCT
def _define_MMC_EXPANDSYNC_STRUCT():
    MMC_EXPANDSYNC_STRUCT = win32more.System.Mmc.MMC_EXPANDSYNC_STRUCT_head
    MMC_EXPANDSYNC_STRUCT._fields_ = [
        ("bHandled", win32more.Foundation.BOOL),
        ("bExpanding", win32more.Foundation.BOOL),
        ("hItem", IntPtr),
    ]
    return MMC_EXPANDSYNC_STRUCT
def _define_MMC_VISIBLE_COLUMNS_head():
    class MMC_VISIBLE_COLUMNS(Structure):
        pass
    return MMC_VISIBLE_COLUMNS
def _define_MMC_VISIBLE_COLUMNS():
    MMC_VISIBLE_COLUMNS = win32more.System.Mmc.MMC_VISIBLE_COLUMNS_head
    MMC_VISIBLE_COLUMNS._fields_ = [
        ("nVisibleColumns", Int32),
        ("rgVisibleCols", Int32 * 0),
    ]
    return MMC_VISIBLE_COLUMNS
MMC_NOTIFY_TYPE = Int32
MMCN_ACTIVATE = 32769
MMCN_ADD_IMAGES = 32770
MMCN_BTN_CLICK = 32771
MMCN_CLICK = 32772
MMCN_COLUMN_CLICK = 32773
MMCN_CONTEXTMENU = 32774
MMCN_CUTORMOVE = 32775
MMCN_DBLCLICK = 32776
MMCN_DELETE = 32777
MMCN_DESELECT_ALL = 32778
MMCN_EXPAND = 32779
MMCN_HELP = 32780
MMCN_MENU_BTNCLICK = 32781
MMCN_MINIMIZED = 32782
MMCN_PASTE = 32783
MMCN_PROPERTY_CHANGE = 32784
MMCN_QUERY_PASTE = 32785
MMCN_REFRESH = 32786
MMCN_REMOVE_CHILDREN = 32787
MMCN_RENAME = 32788
MMCN_SELECT = 32789
MMCN_SHOW = 32790
MMCN_VIEW_CHANGE = 32791
MMCN_SNAPINHELP = 32792
MMCN_CONTEXTHELP = 32793
MMCN_INITOCX = 32794
MMCN_FILTER_CHANGE = 32795
MMCN_FILTERBTN_CLICK = 32796
MMCN_RESTORE_VIEW = 32797
MMCN_PRINT = 32798
MMCN_PRELOAD = 32799
MMCN_LISTPAD = 32800
MMCN_EXPANDSYNC = 32801
MMCN_COLUMNS_CHANGED = 32802
MMCN_CANPASTE_OUTOFPROC = 32803
DATA_OBJECT_TYPES = Int32
CCT_SCOPE = 32768
CCT_RESULT = 32769
CCT_SNAPIN_MANAGER = 32770
CCT_UNINITIALIZED = 65535
def _define_SMMCDataObjects_head():
    class SMMCDataObjects(Structure):
        pass
    return SMMCDataObjects
def _define_SMMCDataObjects():
    SMMCDataObjects = win32more.System.Mmc.SMMCDataObjects_head
    SMMCDataObjects._fields_ = [
        ("count", UInt32),
        ("lpDataObject", win32more.System.Com.IDataObject_head * 0),
    ]
    return SMMCDataObjects
def _define_SMMCObjectTypes_head():
    class SMMCObjectTypes(Structure):
        pass
    return SMMCObjectTypes
def _define_SMMCObjectTypes():
    SMMCObjectTypes = win32more.System.Mmc.SMMCObjectTypes_head
    SMMCObjectTypes._fields_ = [
        ("count", UInt32),
        ("guid", Guid * 0),
    ]
    return SMMCObjectTypes
def _define_SNodeID_head():
    class SNodeID(Structure):
        pass
    return SNodeID
def _define_SNodeID():
    SNodeID = win32more.System.Mmc.SNodeID_head
    SNodeID._fields_ = [
        ("cBytes", UInt32),
        ("id", Byte * 0),
    ]
    return SNodeID
def _define_SNodeID2_head():
    class SNodeID2(Structure):
        pass
    return SNodeID2
def _define_SNodeID2():
    SNodeID2 = win32more.System.Mmc.SNodeID2_head
    SNodeID2._fields_ = [
        ("dwFlags", UInt32),
        ("cBytes", UInt32),
        ("id", Byte * 0),
    ]
    return SNodeID2
def _define_SColumnSetID_head():
    class SColumnSetID(Structure):
        pass
    return SColumnSetID
def _define_SColumnSetID():
    SColumnSetID = win32more.System.Mmc.SColumnSetID_head
    SColumnSetID._fields_ = [
        ("dwFlags", UInt32),
        ("cBytes", UInt32),
        ("id", Byte * 0),
    ]
    return SColumnSetID
def _define_IComponentData_head():
    class IComponentData(win32more.System.Com.IUnknown_head):
        Guid = Guid('955ab28a-5218-11d0-a985-00c04fd8d565')
    return IComponentData
def _define_IComponentData():
    IComponentData = win32more.System.Mmc.IComponentData_head
    IComponentData.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'Initialize', ((1, 'pUnknown'),)))
    IComponentData.CreateComponent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.IComponent_head), use_last_error=False)(4, 'CreateComponent', ((1, 'ppComponent'),)))
    IComponentData.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,win32more.System.Mmc.MMC_NOTIFY_TYPE,win32more.Foundation.LPARAM,win32more.Foundation.LPARAM, use_last_error=False)(5, 'Notify', ((1, 'lpDataObject'),(1, 'event'),(1, 'arg'),(1, 'param3'),)))
    IComponentData.Destroy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Destroy', ()))
    IComponentData.QueryDataObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,win32more.System.Mmc.DATA_OBJECT_TYPES,POINTER(win32more.System.Com.IDataObject_head), use_last_error=False)(7, 'QueryDataObject', ((1, 'cookie'),(1, 'type'),(1, 'ppDataObject'),)))
    IComponentData.GetDisplayInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.SCOPEDATAITEM_head), use_last_error=False)(8, 'GetDisplayInfo', ((1, 'pScopeDataItem'),)))
    IComponentData.CompareObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,win32more.System.Com.IDataObject_head, use_last_error=False)(9, 'CompareObjects', ((1, 'lpDataObjectA'),(1, 'lpDataObjectB'),)))
    return IComponentData
def _define_IComponent_head():
    class IComponent(win32more.System.Com.IUnknown_head):
        Guid = Guid('43136eb2-d36c-11cf-adbc-00aa00a80033')
    return IComponent
def _define_IComponent():
    IComponent = win32more.System.Mmc.IComponent_head
    IComponent.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.IConsole_head, use_last_error=False)(3, 'Initialize', ((1, 'lpConsole'),)))
    IComponent.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,win32more.System.Mmc.MMC_NOTIFY_TYPE,win32more.Foundation.LPARAM,win32more.Foundation.LPARAM, use_last_error=False)(4, 'Notify', ((1, 'lpDataObject'),(1, 'event'),(1, 'arg'),(1, 'param3'),)))
    IComponent.Destroy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(5, 'Destroy', ((1, 'cookie'),)))
    IComponent.QueryDataObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,win32more.System.Mmc.DATA_OBJECT_TYPES,POINTER(win32more.System.Com.IDataObject_head), use_last_error=False)(6, 'QueryDataObject', ((1, 'cookie'),(1, 'type'),(1, 'ppDataObject'),)))
    IComponent.GetResultViewType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(win32more.Foundation.PWSTR),POINTER(Int32), use_last_error=False)(7, 'GetResultViewType', ((1, 'cookie'),(1, 'ppViewType'),(1, 'pViewOptions'),)))
    IComponent.GetDisplayInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.RESULTDATAITEM_head), use_last_error=False)(8, 'GetDisplayInfo', ((1, 'pResultDataItem'),)))
    IComponent.CompareObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,win32more.System.Com.IDataObject_head, use_last_error=False)(9, 'CompareObjects', ((1, 'lpDataObjectA'),(1, 'lpDataObjectB'),)))
    return IComponent
def _define_IResultDataCompare_head():
    class IResultDataCompare(win32more.System.Com.IUnknown_head):
        Guid = Guid('e8315a52-7a1a-11d0-a2d2-00c04fd909dd')
    return IResultDataCompare
def _define_IResultDataCompare():
    IResultDataCompare = win32more.System.Mmc.IResultDataCompare_head
    IResultDataCompare.Compare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LPARAM,IntPtr,IntPtr,POINTER(Int32), use_last_error=False)(3, 'Compare', ((1, 'lUserParam'),(1, 'cookieA'),(1, 'cookieB'),(1, 'pnResult'),)))
    return IResultDataCompare
def _define_IResultOwnerData_head():
    class IResultOwnerData(win32more.System.Com.IUnknown_head):
        Guid = Guid('9cb396d8-ea83-11d0-aef1-00c04fb6dd2c')
    return IResultOwnerData
def _define_IResultOwnerData():
    IResultOwnerData = win32more.System.Mmc.IResultOwnerData_head
    IResultOwnerData.FindItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.RESULTFINDINFO_head),POINTER(Int32), use_last_error=False)(3, 'FindItem', ((1, 'pFindInfo'),(1, 'pnFoundIndex'),)))
    IResultOwnerData.CacheHint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(4, 'CacheHint', ((1, 'nStartIndex'),(1, 'nEndIndex'),)))
    IResultOwnerData.SortItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,win32more.Foundation.LPARAM, use_last_error=False)(5, 'SortItems', ((1, 'nColumn'),(1, 'dwSortOptions'),(1, 'lUserParam'),)))
    return IResultOwnerData
def _define_IConsole_head():
    class IConsole(win32more.System.Com.IUnknown_head):
        Guid = Guid('43136eb1-d36c-11cf-adbc-00aa00a80033')
    return IConsole
def _define_IConsole():
    IConsole = win32more.System.Mmc.IConsole_head
    IConsole.SetHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.IHeaderCtrl_head, use_last_error=False)(3, 'SetHeader', ((1, 'pHeader'),)))
    IConsole.SetToolbar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.IToolbar_head, use_last_error=False)(4, 'SetToolbar', ((1, 'pToolbar'),)))
    IConsole.QueryResultView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(5, 'QueryResultView', ((1, 'pUnknown'),)))
    IConsole.QueryScopeImageList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.IImageList_head), use_last_error=False)(6, 'QueryScopeImageList', ((1, 'ppImageList'),)))
    IConsole.QueryResultImageList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.IImageList_head), use_last_error=False)(7, 'QueryResultImageList', ((1, 'ppImageList'),)))
    IConsole.UpdateAllViews = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,win32more.Foundation.LPARAM,IntPtr, use_last_error=False)(8, 'UpdateAllViews', ((1, 'lpDataObject'),(1, 'data'),(1, 'hint'),)))
    IConsole.MessageBox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(Int32), use_last_error=False)(9, 'MessageBox', ((1, 'lpszText'),(1, 'lpszTitle'),(1, 'fuStyle'),(1, 'piRetval'),)))
    IConsole.QueryConsoleVerb = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.IConsoleVerb_head), use_last_error=False)(10, 'QueryConsoleVerb', ((1, 'ppConsoleVerb'),)))
    IConsole.SelectScopeItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(11, 'SelectScopeItem', ((1, 'hScopeItem'),)))
    IConsole.GetMainWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND), use_last_error=False)(12, 'GetMainWindow', ((1, 'phwnd'),)))
    IConsole.NewWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,UInt32, use_last_error=False)(13, 'NewWindow', ((1, 'hScopeItem'),(1, 'lOptions'),)))
    return IConsole
def _define_IHeaderCtrl_head():
    class IHeaderCtrl(win32more.System.Com.IUnknown_head):
        Guid = Guid('43136eb3-d36c-11cf-adbc-00aa00a80033')
    return IHeaderCtrl
def _define_IHeaderCtrl():
    IHeaderCtrl = win32more.System.Mmc.IHeaderCtrl_head
    IHeaderCtrl.InsertColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.PWSTR,Int32,Int32, use_last_error=False)(3, 'InsertColumn', ((1, 'nCol'),(1, 'title'),(1, 'nFormat'),(1, 'nWidth'),)))
    IHeaderCtrl.DeleteColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(4, 'DeleteColumn', ((1, 'nCol'),)))
    IHeaderCtrl.SetColumnText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SetColumnText', ((1, 'nCol'),(1, 'title'),)))
    IHeaderCtrl.GetColumnText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetColumnText', ((1, 'nCol'),(1, 'pText'),)))
    IHeaderCtrl.SetColumnWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(7, 'SetColumnWidth', ((1, 'nCol'),(1, 'nWidth'),)))
    IHeaderCtrl.GetColumnWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(8, 'GetColumnWidth', ((1, 'nCol'),(1, 'pWidth'),)))
    return IHeaderCtrl
CCM_INSERTIONPOINTID = Int32
CCM_INSERTIONPOINTID_MASK_SPECIAL = -65536
CCM_INSERTIONPOINTID_MASK_SHARED = -2147483648
CCM_INSERTIONPOINTID_MASK_CREATE_PRIMARY = 1073741824
CCM_INSERTIONPOINTID_MASK_ADD_PRIMARY = 536870912
CCM_INSERTIONPOINTID_MASK_ADD_3RDPARTY = 268435456
CCM_INSERTIONPOINTID_MASK_RESERVED = 268369920
CCM_INSERTIONPOINTID_MASK_FLAGINDEX = 31
CCM_INSERTIONPOINTID_PRIMARY_TOP = -1610612736
CCM_INSERTIONPOINTID_PRIMARY_NEW = -1610612735
CCM_INSERTIONPOINTID_PRIMARY_TASK = -1610612734
CCM_INSERTIONPOINTID_PRIMARY_VIEW = -1610612733
CCM_INSERTIONPOINTID_PRIMARY_HELP = -1610612732
CCM_INSERTIONPOINTID_3RDPARTY_NEW = -1879048191
CCM_INSERTIONPOINTID_3RDPARTY_TASK = -1879048190
CCM_INSERTIONPOINTID_ROOT_MENU = -2147483648
CCM_INSERTIONALLOWED = Int32
CCM_INSERTIONALLOWED_TOP = 1
CCM_INSERTIONALLOWED_NEW = 2
CCM_INSERTIONALLOWED_TASK = 4
CCM_INSERTIONALLOWED_VIEW = 8
CCM_COMMANDID_MASK_CONSTANTS = UInt32
CCM_COMMANDID_MASK_RESERVED = 4294901760
CCM_SPECIAL = Int32
CCM_SPECIAL_SEPARATOR = 1
CCM_SPECIAL_SUBMENU = 2
CCM_SPECIAL_DEFAULT_ITEM = 4
CCM_SPECIAL_INSERTION_POINT = 8
CCM_SPECIAL_TESTONLY = 16
def _define_IContextMenuCallback_head():
    class IContextMenuCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('43136eb7-d36c-11cf-adbc-00aa00a80033')
    return IContextMenuCallback
def _define_IContextMenuCallback():
    IContextMenuCallback = win32more.System.Mmc.IContextMenuCallback_head
    IContextMenuCallback.AddItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.CONTEXTMENUITEM_head), use_last_error=False)(3, 'AddItem', ((1, 'pItem'),)))
    return IContextMenuCallback
def _define_IContextMenuProvider_head():
    class IContextMenuProvider(win32more.System.Mmc.IContextMenuCallback_head):
        Guid = Guid('43136eb6-d36c-11cf-adbc-00aa00a80033')
    return IContextMenuProvider
def _define_IContextMenuProvider():
    IContextMenuProvider = win32more.System.Mmc.IContextMenuProvider_head
    IContextMenuProvider.EmptyMenuList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'EmptyMenuList', ()))
    IContextMenuProvider.AddPrimaryExtensionItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IDataObject_head, use_last_error=False)(5, 'AddPrimaryExtensionItems', ((1, 'piExtension'),(1, 'piDataObject'),)))
    IContextMenuProvider.AddThirdPartyExtensionItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head, use_last_error=False)(6, 'AddThirdPartyExtensionItems', ((1, 'piDataObject'),)))
    IContextMenuProvider.ShowContextMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,Int32,Int32,POINTER(Int32), use_last_error=False)(7, 'ShowContextMenu', ((1, 'hwndParent'),(1, 'xPos'),(1, 'yPos'),(1, 'plSelected'),)))
    return IContextMenuProvider
def _define_IExtendContextMenu_head():
    class IExtendContextMenu(win32more.System.Com.IUnknown_head):
        Guid = Guid('4f3b7a4f-cfac-11cf-b8e3-00c04fd8d5b0')
    return IExtendContextMenu
def _define_IExtendContextMenu():
    IExtendContextMenu = win32more.System.Mmc.IExtendContextMenu_head
    IExtendContextMenu.AddMenuItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,win32more.System.Mmc.IContextMenuCallback_head,POINTER(Int32), use_last_error=False)(3, 'AddMenuItems', ((1, 'piDataObject'),(1, 'piCallback'),(1, 'pInsertionAllowed'),)))
    IExtendContextMenu.Command = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.IDataObject_head, use_last_error=False)(4, 'Command', ((1, 'lCommandID'),(1, 'piDataObject'),)))
    return IExtendContextMenu
def _define_IImageList_head():
    class IImageList(win32more.System.Com.IUnknown_head):
        Guid = Guid('43136eb8-d36c-11cf-adbc-00aa00a80033')
    return IImageList
def _define_IImageList():
    IImageList = win32more.System.Mmc.IImageList_head
    IImageList.ImageListSetIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(IntPtr),Int32, use_last_error=False)(3, 'ImageListSetIcon', ((1, 'pIcon'),(1, 'nLoc'),)))
    IImageList.ImageListSetStrip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(IntPtr),POINTER(IntPtr),Int32,UInt32, use_last_error=False)(4, 'ImageListSetStrip', ((1, 'pBMapSm'),(1, 'pBMapLg'),(1, 'nStartLoc'),(1, 'cMask'),)))
    return IImageList
def _define_IResultData_head():
    class IResultData(win32more.System.Com.IUnknown_head):
        Guid = Guid('31da5fa0-e0eb-11cf-9f21-00aa003ca9f6')
    return IResultData
def _define_IResultData():
    IResultData = win32more.System.Mmc.IResultData_head
    IResultData.InsertItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.RESULTDATAITEM_head), use_last_error=False)(3, 'InsertItem', ((1, 'item'),)))
    IResultData.DeleteItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,Int32, use_last_error=False)(4, 'DeleteItem', ((1, 'itemID'),(1, 'nCol'),)))
    IResultData.FindItemByLParam = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LPARAM,POINTER(IntPtr), use_last_error=False)(5, 'FindItemByLParam', ((1, 'lParam'),(1, 'pItemID'),)))
    IResultData.DeleteAllRsltItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'DeleteAllRsltItems', ()))
    IResultData.SetItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.RESULTDATAITEM_head), use_last_error=False)(7, 'SetItem', ((1, 'item'),)))
    IResultData.GetItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.RESULTDATAITEM_head), use_last_error=False)(8, 'GetItem', ((1, 'item'),)))
    IResultData.GetNextItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.RESULTDATAITEM_head), use_last_error=False)(9, 'GetNextItem', ((1, 'item'),)))
    IResultData.ModifyItemState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,IntPtr,UInt32,UInt32, use_last_error=False)(10, 'ModifyItemState', ((1, 'nIndex'),(1, 'itemID'),(1, 'uAdd'),(1, 'uRemove'),)))
    IResultData.ModifyViewStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.MMC_RESULT_VIEW_STYLE,win32more.System.Mmc.MMC_RESULT_VIEW_STYLE, use_last_error=False)(11, 'ModifyViewStyle', ((1, 'add'),(1, 'remove'),)))
    IResultData.SetViewMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'SetViewMode', ((1, 'lViewMode'),)))
    IResultData.GetViewMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'GetViewMode', ((1, 'lViewMode'),)))
    IResultData.UpdateItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(14, 'UpdateItem', ((1, 'itemID'),)))
    IResultData.Sort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,win32more.Foundation.LPARAM, use_last_error=False)(15, 'Sort', ((1, 'nColumn'),(1, 'dwSortOptions'),(1, 'lUserParam'),)))
    IResultData.SetDescBarText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(16, 'SetDescBarText', ((1, 'DescText'),)))
    IResultData.SetItemCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32, use_last_error=False)(17, 'SetItemCount', ((1, 'nItemCount'),(1, 'dwOptions'),)))
    return IResultData
def _define_IConsoleNameSpace_head():
    class IConsoleNameSpace(win32more.System.Com.IUnknown_head):
        Guid = Guid('bedeb620-f24d-11cf-8afc-00aa003ca9f6')
    return IConsoleNameSpace
def _define_IConsoleNameSpace():
    IConsoleNameSpace = win32more.System.Mmc.IConsoleNameSpace_head
    IConsoleNameSpace.InsertItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.SCOPEDATAITEM_head), use_last_error=False)(3, 'InsertItem', ((1, 'item'),)))
    IConsoleNameSpace.DeleteItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,Int32, use_last_error=False)(4, 'DeleteItem', ((1, 'hItem'),(1, 'fDeleteThis'),)))
    IConsoleNameSpace.SetItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.SCOPEDATAITEM_head), use_last_error=False)(5, 'SetItem', ((1, 'item'),)))
    IConsoleNameSpace.GetItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.SCOPEDATAITEM_head), use_last_error=False)(6, 'GetItem', ((1, 'item'),)))
    IConsoleNameSpace.GetChildItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(IntPtr),POINTER(IntPtr), use_last_error=False)(7, 'GetChildItem', ((1, 'item'),(1, 'pItemChild'),(1, 'pCookie'),)))
    IConsoleNameSpace.GetNextItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(IntPtr),POINTER(IntPtr), use_last_error=False)(8, 'GetNextItem', ((1, 'item'),(1, 'pItemNext'),(1, 'pCookie'),)))
    IConsoleNameSpace.GetParentItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(IntPtr),POINTER(IntPtr), use_last_error=False)(9, 'GetParentItem', ((1, 'item'),(1, 'pItemParent'),(1, 'pCookie'),)))
    return IConsoleNameSpace
def _define_IConsoleNameSpace2_head():
    class IConsoleNameSpace2(win32more.System.Mmc.IConsoleNameSpace_head):
        Guid = Guid('255f18cc-65db-11d1-a7dc-00c04fd8d565')
    return IConsoleNameSpace2
def _define_IConsoleNameSpace2():
    IConsoleNameSpace2 = win32more.System.Mmc.IConsoleNameSpace2_head
    IConsoleNameSpace2.Expand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(10, 'Expand', ((1, 'hItem'),)))
    IConsoleNameSpace2.AddExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(Guid), use_last_error=False)(11, 'AddExtension', ((1, 'hItem'),(1, 'lpClsid'),)))
    return IConsoleNameSpace2
def _define_IPropertySheetCallback_head():
    class IPropertySheetCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('85de64dd-ef21-11cf-a285-00c04fd8dbe6')
    return IPropertySheetCallback
def _define_IPropertySheetCallback():
    IPropertySheetCallback = win32more.System.Mmc.IPropertySheetCallback_head
    IPropertySheetCallback.AddPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.HPROPSHEETPAGE, use_last_error=False)(3, 'AddPage', ((1, 'hPage'),)))
    IPropertySheetCallback.RemovePage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.HPROPSHEETPAGE, use_last_error=False)(4, 'RemovePage', ((1, 'hPage'),)))
    return IPropertySheetCallback
def _define_IPropertySheetProvider_head():
    class IPropertySheetProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('85de64de-ef21-11cf-a285-00c04fd8dbe6')
    return IPropertySheetProvider
def _define_IPropertySheetProvider():
    IPropertySheetProvider = win32more.System.Mmc.IPropertySheetProvider_head
    IPropertySheetProvider.CreatePropertySheet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Byte,IntPtr,win32more.System.Com.IDataObject_head,UInt32, use_last_error=False)(3, 'CreatePropertySheet', ((1, 'title'),(1, 'type'),(1, 'cookie'),(1, 'pIDataObjectm'),(1, 'dwOptions'),)))
    IPropertySheetProvider.FindPropertySheet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,win32more.System.Mmc.IComponent_head,win32more.System.Com.IDataObject_head, use_last_error=False)(4, 'FindPropertySheet', ((1, 'hItem'),(1, 'lpComponent'),(1, 'lpDataObject'),)))
    IPropertySheetProvider.AddPrimaryPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.BOOL, use_last_error=False)(5, 'AddPrimaryPages', ((1, 'lpUnknown'),(1, 'bCreateHandle'),(1, 'hNotifyWindow'),(1, 'bScopePane'),)))
    IPropertySheetProvider.AddExtensionPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'AddExtensionPages', ()))
    IPropertySheetProvider.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,Int32, use_last_error=False)(7, 'Show', ((1, 'window'),(1, 'page'),)))
    return IPropertySheetProvider
def _define_IExtendPropertySheet_head():
    class IExtendPropertySheet(win32more.System.Com.IUnknown_head):
        Guid = Guid('85de64dc-ef21-11cf-a285-00c04fd8dbe6')
    return IExtendPropertySheet
def _define_IExtendPropertySheet():
    IExtendPropertySheet = win32more.System.Mmc.IExtendPropertySheet_head
    IExtendPropertySheet.CreatePropertyPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.IPropertySheetCallback_head,IntPtr,win32more.System.Com.IDataObject_head, use_last_error=False)(3, 'CreatePropertyPages', ((1, 'lpProvider'),(1, 'handle'),(1, 'lpIDataObject'),)))
    IExtendPropertySheet.QueryPagesFor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head, use_last_error=False)(4, 'QueryPagesFor', ((1, 'lpDataObject'),)))
    return IExtendPropertySheet
def _define_IControlbar_head():
    class IControlbar(win32more.System.Com.IUnknown_head):
        Guid = Guid('69fb811e-6c1c-11d0-a2cb-00c04fd909dd')
    return IControlbar
def _define_IControlbar():
    IControlbar = win32more.System.Mmc.IControlbar_head
    IControlbar.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.MMC_CONTROL_TYPE,win32more.System.Mmc.IExtendControlbar_head,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(3, 'Create', ((1, 'nType'),(1, 'pExtendControlbar'),(1, 'ppUnknown'),)))
    IControlbar.Attach = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.MMC_CONTROL_TYPE,win32more.System.Com.IUnknown_head, use_last_error=False)(4, 'Attach', ((1, 'nType'),(1, 'lpUnknown'),)))
    IControlbar.Detach = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(5, 'Detach', ((1, 'lpUnknown'),)))
    return IControlbar
def _define_IExtendControlbar_head():
    class IExtendControlbar(win32more.System.Com.IUnknown_head):
        Guid = Guid('49506520-6f40-11d0-a98b-00c04fd8d565')
    return IExtendControlbar
def _define_IExtendControlbar():
    IExtendControlbar = win32more.System.Mmc.IExtendControlbar_head
    IExtendControlbar.SetControlbar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.IControlbar_head, use_last_error=False)(3, 'SetControlbar', ((1, 'pControlbar'),)))
    IExtendControlbar.ControlbarNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.MMC_NOTIFY_TYPE,win32more.Foundation.LPARAM,win32more.Foundation.LPARAM, use_last_error=False)(4, 'ControlbarNotify', ((1, 'event'),(1, 'arg'),(1, 'param2'),)))
    return IExtendControlbar
def _define_IToolbar_head():
    class IToolbar(win32more.System.Com.IUnknown_head):
        Guid = Guid('43136eb9-d36c-11cf-adbc-00aa00a80033')
    return IToolbar
def _define_IToolbar():
    IToolbar = win32more.System.Mmc.IToolbar_head
    IToolbar.AddBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Graphics.Gdi.HBITMAP,Int32,Int32,UInt32, use_last_error=False)(3, 'AddBitmap', ((1, 'nImages'),(1, 'hbmp'),(1, 'cxSize'),(1, 'cySize'),(1, 'crMask'),)))
    IToolbar.AddButtons = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Mmc.MMCBUTTON_head), use_last_error=False)(4, 'AddButtons', ((1, 'nButtons'),(1, 'lpButtons'),)))
    IToolbar.InsertButton = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Mmc.MMCBUTTON_head), use_last_error=False)(5, 'InsertButton', ((1, 'nIndex'),(1, 'lpButton'),)))
    IToolbar.DeleteButton = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(6, 'DeleteButton', ((1, 'nIndex'),)))
    IToolbar.GetButtonState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Mmc.MMC_BUTTON_STATE,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'GetButtonState', ((1, 'idCommand'),(1, 'nState'),(1, 'pState'),)))
    IToolbar.SetButtonState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Mmc.MMC_BUTTON_STATE,win32more.Foundation.BOOL, use_last_error=False)(8, 'SetButtonState', ((1, 'idCommand'),(1, 'nState'),(1, 'bState'),)))
    return IToolbar
def _define_IConsoleVerb_head():
    class IConsoleVerb(win32more.System.Com.IUnknown_head):
        Guid = Guid('e49f7a60-74af-11d0-a286-00c04fd8fe93')
    return IConsoleVerb
def _define_IConsoleVerb():
    IConsoleVerb = win32more.System.Mmc.IConsoleVerb_head
    IConsoleVerb.GetVerbState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.MMC_CONSOLE_VERB,win32more.System.Mmc.MMC_BUTTON_STATE,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'GetVerbState', ((1, 'eCmdID'),(1, 'nState'),(1, 'pState'),)))
    IConsoleVerb.SetVerbState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.MMC_CONSOLE_VERB,win32more.System.Mmc.MMC_BUTTON_STATE,win32more.Foundation.BOOL, use_last_error=False)(4, 'SetVerbState', ((1, 'eCmdID'),(1, 'nState'),(1, 'bState'),)))
    IConsoleVerb.SetDefaultVerb = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.MMC_CONSOLE_VERB, use_last_error=False)(5, 'SetDefaultVerb', ((1, 'eCmdID'),)))
    IConsoleVerb.GetDefaultVerb = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.MMC_CONSOLE_VERB), use_last_error=False)(6, 'GetDefaultVerb', ((1, 'peCmdID'),)))
    return IConsoleVerb
def _define_ISnapinAbout_head():
    class ISnapinAbout(win32more.System.Com.IUnknown_head):
        Guid = Guid('1245208c-a151-11d0-a7d7-00c04fd909dd')
    return ISnapinAbout
def _define_ISnapinAbout():
    ISnapinAbout = win32more.System.Mmc.ISnapinAbout_head
    ISnapinAbout.GetSnapinDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetSnapinDescription', ((1, 'lpDescription'),)))
    ISnapinAbout.GetProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetProvider', ((1, 'lpName'),)))
    ISnapinAbout.GetSnapinVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetSnapinVersion', ((1, 'lpVersion'),)))
    ISnapinAbout.GetSnapinImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.HICON), use_last_error=False)(6, 'GetSnapinImage', ((1, 'hAppIcon'),)))
    ISnapinAbout.GetStaticFolderImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Gdi.HBITMAP),POINTER(win32more.Graphics.Gdi.HBITMAP),POINTER(win32more.Graphics.Gdi.HBITMAP),POINTER(UInt32), use_last_error=False)(7, 'GetStaticFolderImage', ((1, 'hSmallImage'),(1, 'hSmallImageOpen'),(1, 'hLargeImage'),(1, 'cMask'),)))
    return ISnapinAbout
def _define_IMenuButton_head():
    class IMenuButton(win32more.System.Com.IUnknown_head):
        Guid = Guid('951ed750-d080-11d0-b197-000000000000')
    return IMenuButton
def _define_IMenuButton():
    IMenuButton = win32more.System.Mmc.IMenuButton_head
    IMenuButton.AddButton = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'AddButton', ((1, 'idCommand'),(1, 'lpButtonText'),(1, 'lpTooltipText'),)))
    IMenuButton.SetButton = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(4, 'SetButton', ((1, 'idCommand'),(1, 'lpButtonText'),(1, 'lpTooltipText'),)))
    IMenuButton.SetButtonState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Mmc.MMC_BUTTON_STATE,win32more.Foundation.BOOL, use_last_error=False)(5, 'SetButtonState', ((1, 'idCommand'),(1, 'nState'),(1, 'bState'),)))
    return IMenuButton
def _define_ISnapinHelp_head():
    class ISnapinHelp(win32more.System.Com.IUnknown_head):
        Guid = Guid('a6b15ace-df59-11d0-a7dd-00c04fd909dd')
    return ISnapinHelp
def _define_ISnapinHelp():
    ISnapinHelp = win32more.System.Mmc.ISnapinHelp_head
    ISnapinHelp.GetHelpTopic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetHelpTopic', ((1, 'lpCompiledHelpFile'),)))
    return ISnapinHelp
def _define_IExtendPropertySheet2_head():
    class IExtendPropertySheet2(win32more.System.Mmc.IExtendPropertySheet_head):
        Guid = Guid('b7a87232-4a51-11d1-a7ea-00c04fd909dd')
    return IExtendPropertySheet2
def _define_IExtendPropertySheet2():
    IExtendPropertySheet2 = win32more.System.Mmc.IExtendPropertySheet2_head
    IExtendPropertySheet2.GetWatermarks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,POINTER(win32more.Graphics.Gdi.HBITMAP),POINTER(win32more.Graphics.Gdi.HBITMAP),POINTER(win32more.Graphics.Gdi.HPALETTE),POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'GetWatermarks', ((1, 'lpIDataObject'),(1, 'lphWatermark'),(1, 'lphHeader'),(1, 'lphPalette'),(1, 'bStretch'),)))
    return IExtendPropertySheet2
def _define_IHeaderCtrl2_head():
    class IHeaderCtrl2(win32more.System.Mmc.IHeaderCtrl_head):
        Guid = Guid('9757abb8-1b32-11d1-a7ce-00c04fd8d565')
    return IHeaderCtrl2
def _define_IHeaderCtrl2():
    IHeaderCtrl2 = win32more.System.Mmc.IHeaderCtrl2_head
    IHeaderCtrl2.SetChangeTimeOut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'SetChangeTimeOut', ((1, 'uTimeout'),)))
    IHeaderCtrl2.SetColumnFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.Mmc.MMC_FILTERDATA_head), use_last_error=False)(10, 'SetColumnFilter', ((1, 'nColumn'),(1, 'dwType'),(1, 'pFilterData'),)))
    IHeaderCtrl2.GetColumnFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(win32more.System.Mmc.MMC_FILTERDATA_head), use_last_error=False)(11, 'GetColumnFilter', ((1, 'nColumn'),(1, 'pdwType'),(1, 'pFilterData'),)))
    return IHeaderCtrl2
def _define_ISnapinHelp2_head():
    class ISnapinHelp2(win32more.System.Mmc.ISnapinHelp_head):
        Guid = Guid('4861a010-20f9-11d2-a510-00c04fb6dd2c')
    return ISnapinHelp2
def _define_ISnapinHelp2():
    ISnapinHelp2 = win32more.System.Mmc.ISnapinHelp2_head
    ISnapinHelp2.GetLinkedTopics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'GetLinkedTopics', ((1, 'lpCompiledHelpFiles'),)))
    return ISnapinHelp2
MMC_TASK_DISPLAY_TYPE = Int32
MMC_TASK_DISPLAY_UNINITIALIZED = 0
MMC_TASK_DISPLAY_TYPE_SYMBOL = 1
MMC_TASK_DISPLAY_TYPE_VANILLA_GIF = 2
MMC_TASK_DISPLAY_TYPE_CHOCOLATE_GIF = 3
MMC_TASK_DISPLAY_TYPE_BITMAP = 4
def _define_MMC_TASK_DISPLAY_SYMBOL_head():
    class MMC_TASK_DISPLAY_SYMBOL(Structure):
        pass
    return MMC_TASK_DISPLAY_SYMBOL
def _define_MMC_TASK_DISPLAY_SYMBOL():
    MMC_TASK_DISPLAY_SYMBOL = win32more.System.Mmc.MMC_TASK_DISPLAY_SYMBOL_head
    MMC_TASK_DISPLAY_SYMBOL._fields_ = [
        ("szFontFamilyName", win32more.Foundation.PWSTR),
        ("szURLtoEOT", win32more.Foundation.PWSTR),
        ("szSymbolString", win32more.Foundation.PWSTR),
    ]
    return MMC_TASK_DISPLAY_SYMBOL
def _define_MMC_TASK_DISPLAY_BITMAP_head():
    class MMC_TASK_DISPLAY_BITMAP(Structure):
        pass
    return MMC_TASK_DISPLAY_BITMAP
def _define_MMC_TASK_DISPLAY_BITMAP():
    MMC_TASK_DISPLAY_BITMAP = win32more.System.Mmc.MMC_TASK_DISPLAY_BITMAP_head
    MMC_TASK_DISPLAY_BITMAP._fields_ = [
        ("szMouseOverBitmap", win32more.Foundation.PWSTR),
        ("szMouseOffBitmap", win32more.Foundation.PWSTR),
    ]
    return MMC_TASK_DISPLAY_BITMAP
def _define_MMC_TASK_DISPLAY_OBJECT_head():
    class MMC_TASK_DISPLAY_OBJECT(Structure):
        pass
    return MMC_TASK_DISPLAY_OBJECT
def _define_MMC_TASK_DISPLAY_OBJECT():
    MMC_TASK_DISPLAY_OBJECT = win32more.System.Mmc.MMC_TASK_DISPLAY_OBJECT_head
    class MMC_TASK_DISPLAY_OBJECT__Anonymous_e__Union(Union):
        pass
    MMC_TASK_DISPLAY_OBJECT__Anonymous_e__Union._fields_ = [
        ("uBitmap", win32more.System.Mmc.MMC_TASK_DISPLAY_BITMAP),
        ("uSymbol", win32more.System.Mmc.MMC_TASK_DISPLAY_SYMBOL),
    ]
    MMC_TASK_DISPLAY_OBJECT._anonymous_ = [
        'Anonymous',
    ]
    MMC_TASK_DISPLAY_OBJECT._fields_ = [
        ("eDisplayType", win32more.System.Mmc.MMC_TASK_DISPLAY_TYPE),
        ("Anonymous", MMC_TASK_DISPLAY_OBJECT__Anonymous_e__Union),
    ]
    return MMC_TASK_DISPLAY_OBJECT
MMC_ACTION_TYPE = Int32
MMC_ACTION_UNINITIALIZED = -1
MMC_ACTION_ID = 0
MMC_ACTION_LINK = 1
MMC_ACTION_SCRIPT = 2
def _define_MMC_TASK_head():
    class MMC_TASK(Structure):
        pass
    return MMC_TASK
def _define_MMC_TASK():
    MMC_TASK = win32more.System.Mmc.MMC_TASK_head
    class MMC_TASK__Anonymous_e__Union(Union):
        pass
    MMC_TASK__Anonymous_e__Union._fields_ = [
        ("nCommandID", IntPtr),
        ("szActionURL", win32more.Foundation.PWSTR),
        ("szScript", win32more.Foundation.PWSTR),
    ]
    MMC_TASK._anonymous_ = [
        'Anonymous',
    ]
    MMC_TASK._fields_ = [
        ("sDisplayObject", win32more.System.Mmc.MMC_TASK_DISPLAY_OBJECT),
        ("szText", win32more.Foundation.PWSTR),
        ("szHelpString", win32more.Foundation.PWSTR),
        ("eActionType", win32more.System.Mmc.MMC_ACTION_TYPE),
        ("Anonymous", MMC_TASK__Anonymous_e__Union),
    ]
    return MMC_TASK
def _define_MMC_LISTPAD_INFO_head():
    class MMC_LISTPAD_INFO(Structure):
        pass
    return MMC_LISTPAD_INFO
def _define_MMC_LISTPAD_INFO():
    MMC_LISTPAD_INFO = win32more.System.Mmc.MMC_LISTPAD_INFO_head
    MMC_LISTPAD_INFO._fields_ = [
        ("szTitle", win32more.Foundation.PWSTR),
        ("szButtonText", win32more.Foundation.PWSTR),
        ("nCommandID", IntPtr),
    ]
    return MMC_LISTPAD_INFO
def _define_IEnumTASK_head():
    class IEnumTASK(win32more.System.Com.IUnknown_head):
        Guid = Guid('338698b1-5a02-11d1-9fec-00600832db4a')
    return IEnumTASK
def _define_IEnumTASK():
    IEnumTASK = win32more.System.Mmc.IEnumTASK_head
    IEnumTASK.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Mmc.MMC_TASK),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumTASK.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumTASK.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTASK.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.IEnumTASK_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    return IEnumTASK
def _define_IExtendTaskPad_head():
    class IExtendTaskPad(win32more.System.Com.IUnknown_head):
        Guid = Guid('8dee6511-554d-11d1-9fea-00600832db4a')
    return IExtendTaskPad
def _define_IExtendTaskPad():
    IExtendTaskPad = win32more.System.Mmc.IExtendTaskPad_head
    IExtendTaskPad.TaskNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(3, 'TaskNotify', ((1, 'pdo'),(1, 'arg'),(1, 'param2'),)))
    IExtendTaskPad.EnumTasks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,win32more.Foundation.PWSTR,POINTER(win32more.System.Mmc.IEnumTASK_head), use_last_error=False)(4, 'EnumTasks', ((1, 'pdo'),(1, 'szTaskGroup'),(1, 'ppEnumTASK'),)))
    IExtendTaskPad.GetTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(5, 'GetTitle', ((1, 'pszGroup'),(1, 'pszTitle'),)))
    IExtendTaskPad.GetDescriptiveText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetDescriptiveText', ((1, 'pszGroup'),(1, 'pszDescriptiveText'),)))
    IExtendTaskPad.GetBackground = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Mmc.MMC_TASK_DISPLAY_OBJECT_head), use_last_error=False)(7, 'GetBackground', ((1, 'pszGroup'),(1, 'pTDO'),)))
    IExtendTaskPad.GetListPadInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Mmc.MMC_LISTPAD_INFO_head), use_last_error=False)(8, 'GetListPadInfo', ((1, 'pszGroup'),(1, 'lpListPadInfo'),)))
    return IExtendTaskPad
def _define_IConsole2_head():
    class IConsole2(win32more.System.Mmc.IConsole_head):
        Guid = Guid('103d842a-aa63-11d1-a7e1-00c04fd8d565')
    return IConsole2
def _define_IConsole2():
    IConsole2 = win32more.System.Mmc.IConsole2_head
    IConsole2.Expand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,win32more.Foundation.BOOL, use_last_error=False)(14, 'Expand', ((1, 'hItem'),(1, 'bExpand'),)))
    IConsole2.IsTaskpadViewPreferred = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'IsTaskpadViewPreferred', ()))
    IConsole2.SetStatusText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(16, 'SetStatusText', ((1, 'pszStatusText'),)))
    return IConsole2
def _define_IDisplayHelp_head():
    class IDisplayHelp(win32more.System.Com.IUnknown_head):
        Guid = Guid('cc593830-b926-11d1-8063-0000f875a9ce')
    return IDisplayHelp
def _define_IDisplayHelp():
    IDisplayHelp = win32more.System.Mmc.IDisplayHelp_head
    IDisplayHelp.ShowTopic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'ShowTopic', ((1, 'pszHelpTopic'),)))
    return IDisplayHelp
def _define_IRequiredExtensions_head():
    class IRequiredExtensions(win32more.System.Com.IUnknown_head):
        Guid = Guid('72782d7a-a4a0-11d1-af0f-00c04fb6dd2c')
    return IRequiredExtensions
def _define_IRequiredExtensions():
    IRequiredExtensions = win32more.System.Mmc.IRequiredExtensions_head
    IRequiredExtensions.EnableAllExtensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'EnableAllExtensions', ()))
    IRequiredExtensions.GetFirstExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'GetFirstExtension', ((1, 'pExtCLSID'),)))
    IRequiredExtensions.GetNextExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(5, 'GetNextExtension', ((1, 'pExtCLSID'),)))
    return IRequiredExtensions
def _define_IStringTable_head():
    class IStringTable(win32more.System.Com.IUnknown_head):
        Guid = Guid('de40b7a4-0f65-11d2-8e25-00c04f8ecd78')
    return IStringTable
def _define_IStringTable():
    IStringTable = win32more.System.Mmc.IStringTable_head
    IStringTable.AddString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(3, 'AddString', ((1, 'pszAdd'),(1, 'pStringID'),)))
    IStringTable.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Char),POINTER(UInt32), use_last_error=False)(4, 'GetString', ((1, 'StringID'),(1, 'cchBuffer'),(1, 'lpBuffer'),(1, 'pcchOut'),)))
    IStringTable.GetStringLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetStringLength', ((1, 'StringID'),(1, 'pcchString'),)))
    IStringTable.DeleteString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'DeleteString', ((1, 'StringID'),)))
    IStringTable.DeleteAllStrings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'DeleteAllStrings', ()))
    IStringTable.FindString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(8, 'FindString', ((1, 'pszFind'),(1, 'pStringID'),)))
    IStringTable.Enumerate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumString_head), use_last_error=False)(9, 'Enumerate', ((1, 'ppEnum'),)))
    return IStringTable
def _define_MMC_COLUMN_DATA_head():
    class MMC_COLUMN_DATA(Structure):
        pass
    return MMC_COLUMN_DATA
def _define_MMC_COLUMN_DATA():
    MMC_COLUMN_DATA = win32more.System.Mmc.MMC_COLUMN_DATA_head
    MMC_COLUMN_DATA._fields_ = [
        ("nColIndex", Int32),
        ("dwFlags", UInt32),
        ("nWidth", Int32),
        ("ulReserved", UIntPtr),
    ]
    return MMC_COLUMN_DATA
def _define_MMC_COLUMN_SET_DATA_head():
    class MMC_COLUMN_SET_DATA(Structure):
        pass
    return MMC_COLUMN_SET_DATA
def _define_MMC_COLUMN_SET_DATA():
    MMC_COLUMN_SET_DATA = win32more.System.Mmc.MMC_COLUMN_SET_DATA_head
    MMC_COLUMN_SET_DATA._fields_ = [
        ("cbSize", Int32),
        ("nNumCols", Int32),
        ("pColData", POINTER(win32more.System.Mmc.MMC_COLUMN_DATA_head)),
    ]
    return MMC_COLUMN_SET_DATA
def _define_MMC_SORT_DATA_head():
    class MMC_SORT_DATA(Structure):
        pass
    return MMC_SORT_DATA
def _define_MMC_SORT_DATA():
    MMC_SORT_DATA = win32more.System.Mmc.MMC_SORT_DATA_head
    MMC_SORT_DATA._fields_ = [
        ("nColIndex", Int32),
        ("dwSortOptions", UInt32),
        ("ulReserved", UIntPtr),
    ]
    return MMC_SORT_DATA
def _define_MMC_SORT_SET_DATA_head():
    class MMC_SORT_SET_DATA(Structure):
        pass
    return MMC_SORT_SET_DATA
def _define_MMC_SORT_SET_DATA():
    MMC_SORT_SET_DATA = win32more.System.Mmc.MMC_SORT_SET_DATA_head
    MMC_SORT_SET_DATA._fields_ = [
        ("cbSize", Int32),
        ("nNumItems", Int32),
        ("pSortData", POINTER(win32more.System.Mmc.MMC_SORT_DATA_head)),
    ]
    return MMC_SORT_SET_DATA
def _define_IColumnData_head():
    class IColumnData(win32more.System.Com.IUnknown_head):
        Guid = Guid('547c1354-024d-11d3-a707-00c04f8ef4cb')
    return IColumnData
def _define_IColumnData():
    IColumnData = win32more.System.Mmc.IColumnData_head
    IColumnData.SetColumnConfigData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.SColumnSetID_head),POINTER(win32more.System.Mmc.MMC_COLUMN_SET_DATA_head), use_last_error=False)(3, 'SetColumnConfigData', ((1, 'pColID'),(1, 'pColSetData'),)))
    IColumnData.GetColumnConfigData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.SColumnSetID_head),POINTER(POINTER(win32more.System.Mmc.MMC_COLUMN_SET_DATA_head)), use_last_error=False)(4, 'GetColumnConfigData', ((1, 'pColID'),(1, 'ppColSetData'),)))
    IColumnData.SetColumnSortData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.SColumnSetID_head),POINTER(win32more.System.Mmc.MMC_SORT_SET_DATA_head), use_last_error=False)(5, 'SetColumnSortData', ((1, 'pColID'),(1, 'pColSortData'),)))
    IColumnData.GetColumnSortData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.SColumnSetID_head),POINTER(POINTER(win32more.System.Mmc.MMC_SORT_SET_DATA_head)), use_last_error=False)(6, 'GetColumnSortData', ((1, 'pColID'),(1, 'ppColSortData'),)))
    return IColumnData
IconIdentifier = Int32
Icon_None = 0
Icon_Error = 32513
Icon_Question = 32514
Icon_Warning = 32515
Icon_Information = 32516
Icon_First = 32513
Icon_Last = 32516
def _define_IMessageView_head():
    class IMessageView(win32more.System.Com.IUnknown_head):
        Guid = Guid('80f94174-fccc-11d2-b991-00c04f8ecd78')
    return IMessageView
def _define_IMessageView():
    IMessageView = win32more.System.Mmc.IMessageView_head
    IMessageView.SetTitleText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'SetTitleText', ((1, 'pszTitleText'),)))
    IMessageView.SetBodyText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'SetBodyText', ((1, 'pszBodyText'),)))
    IMessageView.SetIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Mmc.IconIdentifier, use_last_error=False)(5, 'SetIcon', ((1, 'id'),)))
    IMessageView.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Clear', ()))
    return IMessageView
def _define_RDITEMHDR_head():
    class RDITEMHDR(Structure):
        pass
    return RDITEMHDR
def _define_RDITEMHDR():
    RDITEMHDR = win32more.System.Mmc.RDITEMHDR_head
    RDITEMHDR._fields_ = [
        ("dwFlags", UInt32),
        ("cookie", IntPtr),
        ("lpReserved", win32more.Foundation.LPARAM),
    ]
    return RDITEMHDR
def _define_RDCOMPARE_head():
    class RDCOMPARE(Structure):
        pass
    return RDCOMPARE
def _define_RDCOMPARE():
    RDCOMPARE = win32more.System.Mmc.RDCOMPARE_head
    RDCOMPARE._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", UInt32),
        ("nColumn", Int32),
        ("lUserParam", win32more.Foundation.LPARAM),
        ("prdch1", POINTER(win32more.System.Mmc.RDITEMHDR_head)),
        ("prdch2", POINTER(win32more.System.Mmc.RDITEMHDR_head)),
    ]
    return RDCOMPARE
def _define_IResultDataCompareEx_head():
    class IResultDataCompareEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('96933476-0251-11d3-aeb0-00c04f8ecd78')
    return IResultDataCompareEx
def _define_IResultDataCompareEx():
    IResultDataCompareEx = win32more.System.Mmc.IResultDataCompareEx_head
    IResultDataCompareEx.Compare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.RDCOMPARE_head),POINTER(Int32), use_last_error=False)(3, 'Compare', ((1, 'prdc'),(1, 'pnResult'),)))
    return IResultDataCompareEx
MMC_VIEW_TYPE = Int32
MMC_VIEW_TYPE_LIST = 0
MMC_VIEW_TYPE_HTML = 1
MMC_VIEW_TYPE_OCX = 2
def _define_RESULT_VIEW_TYPE_INFO_head():
    class RESULT_VIEW_TYPE_INFO(Structure):
        pass
    return RESULT_VIEW_TYPE_INFO
def _define_RESULT_VIEW_TYPE_INFO():
    RESULT_VIEW_TYPE_INFO = win32more.System.Mmc.RESULT_VIEW_TYPE_INFO_head
    class RESULT_VIEW_TYPE_INFO__Anonymous_e__Union(Union):
        pass
    class RESULT_VIEW_TYPE_INFO__Anonymous_e__Union__Anonymous2_e__Struct(Structure):
        pass
    RESULT_VIEW_TYPE_INFO__Anonymous_e__Union__Anonymous2_e__Struct._fields_ = [
        ("dwOCXOptions", UInt32),
        ("pUnkControl", win32more.System.Com.IUnknown_head),
    ]
    class RESULT_VIEW_TYPE_INFO__Anonymous_e__Union__Anonymous1_e__Struct(Structure):
        pass
    RESULT_VIEW_TYPE_INFO__Anonymous_e__Union__Anonymous1_e__Struct._fields_ = [
        ("dwHTMLOptions", UInt32),
        ("pstrURL", win32more.Foundation.PWSTR),
    ]
    RESULT_VIEW_TYPE_INFO__Anonymous_e__Union._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    RESULT_VIEW_TYPE_INFO__Anonymous_e__Union._fields_ = [
        ("dwListOptions", UInt32),
        ("Anonymous1", RESULT_VIEW_TYPE_INFO__Anonymous_e__Union__Anonymous1_e__Struct),
        ("Anonymous2", RESULT_VIEW_TYPE_INFO__Anonymous_e__Union__Anonymous2_e__Struct),
    ]
    RESULT_VIEW_TYPE_INFO._anonymous_ = [
        'Anonymous',
    ]
    RESULT_VIEW_TYPE_INFO._fields_ = [
        ("pstrPersistableViewDescription", win32more.Foundation.PWSTR),
        ("eViewType", win32more.System.Mmc.MMC_VIEW_TYPE),
        ("dwMiscOptions", UInt32),
        ("Anonymous", RESULT_VIEW_TYPE_INFO__Anonymous_e__Union),
    ]
    return RESULT_VIEW_TYPE_INFO
def _define_CONTEXTMENUITEM2_head():
    class CONTEXTMENUITEM2(Structure):
        pass
    return CONTEXTMENUITEM2
def _define_CONTEXTMENUITEM2():
    CONTEXTMENUITEM2 = win32more.System.Mmc.CONTEXTMENUITEM2_head
    CONTEXTMENUITEM2._fields_ = [
        ("strName", win32more.Foundation.PWSTR),
        ("strStatusBarText", win32more.Foundation.PWSTR),
        ("lCommandID", Int32),
        ("lInsertionPointID", Int32),
        ("fFlags", Int32),
        ("fSpecialFlags", Int32),
        ("strLanguageIndependentName", win32more.Foundation.PWSTR),
    ]
    return CONTEXTMENUITEM2
def _define_MMC_EXT_VIEW_DATA_head():
    class MMC_EXT_VIEW_DATA(Structure):
        pass
    return MMC_EXT_VIEW_DATA
def _define_MMC_EXT_VIEW_DATA():
    MMC_EXT_VIEW_DATA = win32more.System.Mmc.MMC_EXT_VIEW_DATA_head
    MMC_EXT_VIEW_DATA._fields_ = [
        ("viewID", Guid),
        ("pszURL", win32more.Foundation.PWSTR),
        ("pszViewTitle", win32more.Foundation.PWSTR),
        ("pszTooltipText", win32more.Foundation.PWSTR),
        ("bReplacesDefaultView", win32more.Foundation.BOOL),
    ]
    return MMC_EXT_VIEW_DATA
def _define_IComponentData2_head():
    class IComponentData2(win32more.System.Mmc.IComponentData_head):
        Guid = Guid('cca0f2d2-82de-41b5-bf47-3b2076273d5c')
    return IComponentData2
def _define_IComponentData2():
    IComponentData2 = win32more.System.Mmc.IComponentData2_head
    IComponentData2.QueryDispatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,win32more.System.Mmc.DATA_OBJECT_TYPES,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(10, 'QueryDispatch', ((1, 'cookie'),(1, 'type'),(1, 'ppDispatch'),)))
    return IComponentData2
def _define_IComponent2_head():
    class IComponent2(win32more.System.Mmc.IComponent_head):
        Guid = Guid('79a2d615-4a10-4ed4-8c65-8633f9335095')
    return IComponent2
def _define_IComponent2():
    IComponent2 = win32more.System.Mmc.IComponent2_head
    IComponent2.QueryDispatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,win32more.System.Mmc.DATA_OBJECT_TYPES,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(10, 'QueryDispatch', ((1, 'cookie'),(1, 'type'),(1, 'ppDispatch'),)))
    IComponent2.GetResultViewType2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(win32more.System.Mmc.RESULT_VIEW_TYPE_INFO_head), use_last_error=False)(11, 'GetResultViewType2', ((1, 'cookie'),(1, 'pResultViewType'),)))
    IComponent2.RestoreResultView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(win32more.System.Mmc.RESULT_VIEW_TYPE_INFO_head), use_last_error=False)(12, 'RestoreResultView', ((1, 'cookie'),(1, 'pResultViewType'),)))
    return IComponent2
def _define_IContextMenuCallback2_head():
    class IContextMenuCallback2(win32more.System.Com.IUnknown_head):
        Guid = Guid('e178bc0e-2ed0-4b5e-8097-42c9087e8b33')
    return IContextMenuCallback2
def _define_IContextMenuCallback2():
    IContextMenuCallback2 = win32more.System.Mmc.IContextMenuCallback2_head
    IContextMenuCallback2.AddItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.CONTEXTMENUITEM2_head), use_last_error=False)(3, 'AddItem', ((1, 'pItem'),)))
    return IContextMenuCallback2
def _define_IMMCVersionInfo_head():
    class IMMCVersionInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('a8d2c5fe-cdcb-4b9d-bde5-a27343ff54bc')
    return IMMCVersionInfo
def _define_IMMCVersionInfo():
    IMMCVersionInfo = win32more.System.Mmc.IMMCVersionInfo_head
    IMMCVersionInfo.GetMMCVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32), use_last_error=False)(3, 'GetMMCVersion', ((1, 'pVersionMajor'),(1, 'pVersionMinor'),)))
    return IMMCVersionInfo
def _define_IExtendView_head():
    class IExtendView(win32more.System.Com.IUnknown_head):
        Guid = Guid('89995cee-d2ed-4c0e-ae5e-df7e76f3fa53')
    return IExtendView
def _define_IExtendView():
    IExtendView = win32more.System.Mmc.IExtendView_head
    IExtendView.GetViews = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,win32more.System.Mmc.IViewExtensionCallback_head, use_last_error=False)(3, 'GetViews', ((1, 'pDataObject'),(1, 'pViewExtensionCallback'),)))
    return IExtendView
def _define_IViewExtensionCallback_head():
    class IViewExtensionCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('34dd928a-7599-41e5-9f5e-d6bc3062c2da')
    return IViewExtensionCallback
def _define_IViewExtensionCallback():
    IViewExtensionCallback = win32more.System.Mmc.IViewExtensionCallback_head
    IViewExtensionCallback.AddView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Mmc.MMC_EXT_VIEW_DATA_head), use_last_error=False)(3, 'AddView', ((1, 'pExtViewData'),)))
    return IViewExtensionCallback
def _define_IConsolePower_head():
    class IConsolePower(win32more.System.Com.IUnknown_head):
        Guid = Guid('1cfbdd0e-62ca-49ce-a3af-dbb2de61b068')
    return IConsolePower
def _define_IConsolePower():
    IConsolePower = win32more.System.Mmc.IConsolePower_head
    IConsolePower.SetExecutionState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(3, 'SetExecutionState', ((1, 'dwAdd'),(1, 'dwRemove'),)))
    IConsolePower.ResetIdleTimer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'ResetIdleTimer', ((1, 'dwFlags'),)))
    return IConsolePower
def _define_IConsolePowerSink_head():
    class IConsolePowerSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('3333759f-fe4f-4975-b143-fec0a5dd6d65')
    return IConsolePowerSink
def _define_IConsolePowerSink():
    IConsolePowerSink = win32more.System.Mmc.IConsolePowerSink_head
    IConsolePowerSink.OnPowerBroadcast = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(3, 'OnPowerBroadcast', ((1, 'nEvent'),(1, 'lParam'),(1, 'plReturn'),)))
    return IConsolePowerSink
def _define_INodeProperties_head():
    class INodeProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('15bc4d24-a522-4406-aa55-0749537a6865')
    return INodeProperties
def _define_INodeProperties():
    INodeProperties = win32more.System.Mmc.INodeProperties_head
    INodeProperties.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,win32more.Foundation.BSTR,POINTER(POINTER(UInt16)), use_last_error=False)(3, 'GetProperty', ((1, 'pDataObject'),(1, 'szPropertyName'),(1, 'pbstrProperty'),)))
    return INodeProperties
def _define_IConsole3_head():
    class IConsole3(win32more.System.Mmc.IConsole2_head):
        Guid = Guid('4f85efdb-d0e1-498c-8d4a-d010dfdd404f')
    return IConsole3
def _define_IConsole3():
    IConsole3 = win32more.System.Mmc.IConsole3_head
    IConsole3.RenameScopeItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(17, 'RenameScopeItem', ((1, 'hScopeItem'),)))
    return IConsole3
def _define_IResultData2_head():
    class IResultData2(win32more.System.Mmc.IResultData_head):
        Guid = Guid('0f36e0eb-a7f1-4a81-be5a-9247f7de4b1b')
    return IResultData2
def _define_IResultData2():
    IResultData2 = win32more.System.Mmc.IResultData2_head
    IResultData2.RenameResultItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(18, 'RenameResultItem', ((1, 'itemID'),)))
    return IResultData2
__all__ = [
    "MMC_VER",
    "MMC_PROP_CHANGEAFFECTSUI",
    "MMC_PROP_MODIFIABLE",
    "MMC_PROP_REMOVABLE",
    "MMC_PROP_PERSIST",
    "MMCLV_AUTO",
    "MMCLV_NOPARAM",
    "MMCLV_NOICON",
    "MMCLV_VIEWSTYLE_ICON",
    "MMCLV_VIEWSTYLE_SMALLICON",
    "MMCLV_VIEWSTYLE_LIST",
    "MMCLV_VIEWSTYLE_REPORT",
    "MMCLV_VIEWSTYLE_FILTERED",
    "MMCLV_NOPTR",
    "MMCLV_UPDATE_NOINVALIDATEALL",
    "MMCLV_UPDATE_NOSCROLL",
    "MMC_IMAGECALLBACK",
    "RDI_STR",
    "RDI_IMAGE",
    "RDI_STATE",
    "RDI_PARAM",
    "RDI_INDEX",
    "RDI_INDENT",
    "MMC_VIEW_OPTIONS_NONE",
    "MMC_VIEW_OPTIONS_NOLISTVIEWS",
    "MMC_VIEW_OPTIONS_MULTISELECT",
    "MMC_VIEW_OPTIONS_OWNERDATALIST",
    "MMC_VIEW_OPTIONS_FILTERED",
    "MMC_VIEW_OPTIONS_CREATENEW",
    "MMC_VIEW_OPTIONS_USEFONTLINKING",
    "MMC_VIEW_OPTIONS_EXCLUDE_SCOPE_ITEMS_FROM_LIST",
    "MMC_VIEW_OPTIONS_LEXICAL_SORT",
    "MMC_PSO_NOAPPLYNOW",
    "MMC_PSO_HASHELP",
    "MMC_PSO_NEWWIZARDTYPE",
    "MMC_PSO_NO_PROPTITLE",
    "RFI_PARTIAL",
    "RFI_WRAP",
    "RSI_DESCENDING",
    "RSI_NOSORTICON",
    "SDI_STR",
    "SDI_IMAGE",
    "SDI_OPENIMAGE",
    "SDI_STATE",
    "SDI_PARAM",
    "SDI_CHILDREN",
    "SDI_PARENT",
    "SDI_PREVIOUS",
    "SDI_NEXT",
    "SDI_FIRST",
    "MMC_MULTI_SELECT_COOKIE",
    "MMC_WINDOW_COOKIE",
    "SPECIAL_COOKIE_MIN",
    "SPECIAL_COOKIE_MAX",
    "MMC_NW_OPTION_NONE",
    "MMC_NW_OPTION_NOSCOPEPANE",
    "MMC_NW_OPTION_NOTOOLBARS",
    "MMC_NW_OPTION_SHORTTITLE",
    "MMC_NW_OPTION_CUSTOMTITLE",
    "MMC_NW_OPTION_NOPERSIST",
    "MMC_NW_OPTION_NOACTIONPANE",
    "MMC_NODEID_SLOW_RETRIEVAL",
    "SPECIAL_DOBJ_MIN",
    "SPECIAL_DOBJ_MAX",
    "AUTO_WIDTH",
    "HIDE_COLUMN",
    "ILSIF_LEAVE_LARGE_ICON",
    "ILSIF_LEAVE_SMALL_ICON",
    "HDI_HIDDEN",
    "RDCI_ScopeItem",
    "RVTI_MISC_OPTIONS_NOLISTVIEWS",
    "RVTI_LIST_OPTIONS_NONE",
    "RVTI_LIST_OPTIONS_OWNERDATALIST",
    "RVTI_LIST_OPTIONS_MULTISELECT",
    "RVTI_LIST_OPTIONS_FILTERED",
    "RVTI_LIST_OPTIONS_USEFONTLINKING",
    "RVTI_LIST_OPTIONS_EXCLUDE_SCOPE_ITEMS_FROM_LIST",
    "RVTI_LIST_OPTIONS_LEXICAL_SORT",
    "RVTI_LIST_OPTIONS_ALLOWPASTE",
    "RVTI_HTML_OPTIONS_NONE",
    "RVTI_HTML_OPTIONS_NOLISTVIEW",
    "RVTI_OCX_OPTIONS_NONE",
    "RVTI_OCX_OPTIONS_NOLISTVIEW",
    "RVTI_OCX_OPTIONS_CACHE_OCX",
    "MMC_DEFAULT_OPERATION_COPY",
    "MMC_ITEM_OVERLAY_STATE_MASK",
    "MMC_ITEM_OVERLAY_STATE_SHIFT",
    "MMC_ITEM_STATE_MASK",
    "Application",
    "AppEventsDHTMLConnector",
    "MMC_PROPERTY_ACTION",
    "MMC_PROPACT_DELETING",
    "MMC_PROPACT_CHANGING",
    "MMC_PROPACT_INITIALIZED",
    "MMC_SNAPIN_PROPERTY",
    "ISnapinProperties",
    "ISnapinPropertiesCallback",
    "_DocumentMode",
    "DocumentMode_Author",
    "DocumentMode_User",
    "DocumentMode_User_MDI",
    "DocumentMode_User_SDI",
    "_ListViewMode",
    "ListMode_Small_Icons",
    "ListMode_Large_Icons",
    "ListMode_List",
    "ListMode_Detail",
    "ListMode_Filtered",
    "_ViewOptions",
    "ViewOption_Default",
    "ViewOption_ScopeTreeHidden",
    "ViewOption_NoToolBars",
    "ViewOption_NotPersistable",
    "ViewOption_ActionPaneHidden",
    "_ExportListOptions",
    "ExportListOptions_Default",
    "ExportListOptions_Unicode",
    "ExportListOptions_TabDelimited",
    "ExportListOptions_SelectedItemsOnly",
    "_Application",
    "_AppEvents",
    "AppEvents",
    "_EventConnector",
    "Frame",
    "Node",
    "ScopeNamespace",
    "Document",
    "SnapIn",
    "SnapIns",
    "Extension",
    "Extensions",
    "Columns",
    "_ColumnSortOrder",
    "SortOrder_Ascending",
    "SortOrder_Descending",
    "Column",
    "Views",
    "View",
    "Nodes",
    "ContextMenu",
    "MenuItem",
    "Properties",
    "Property",
    "MMCVersionInfo",
    "ConsolePower",
    "MMC_RESULT_VIEW_STYLE",
    "MMC_SINGLESEL",
    "MMC_SHOWSELALWAYS",
    "MMC_NOSORTHEADER",
    "MMC_ENSUREFOCUSVISIBLE",
    "MMC_CONTROL_TYPE",
    "TOOLBAR",
    "MENUBUTTON",
    "COMBOBOXBAR",
    "MMC_CONSOLE_VERB",
    "MMC_VERB_NONE",
    "MMC_VERB_OPEN",
    "MMC_VERB_COPY",
    "MMC_VERB_PASTE",
    "MMC_VERB_DELETE",
    "MMC_VERB_PROPERTIES",
    "MMC_VERB_RENAME",
    "MMC_VERB_REFRESH",
    "MMC_VERB_PRINT",
    "MMC_VERB_CUT",
    "MMC_VERB_MAX",
    "MMC_VERB_FIRST",
    "MMC_VERB_LAST",
    "MMCBUTTON",
    "MMC_BUTTON_STATE",
    "ENABLED",
    "CHECKED",
    "HIDDEN",
    "INDETERMINATE",
    "BUTTONPRESSED",
    "RESULTDATAITEM",
    "RESULTFINDINFO",
    "SCOPEDATAITEM",
    "MMC_SCOPE_ITEM_STATE",
    "MMC_SCOPE_ITEM_STATE_NORMAL",
    "MMC_SCOPE_ITEM_STATE_BOLD",
    "MMC_SCOPE_ITEM_STATE_EXPANDEDONCE",
    "CONTEXTMENUITEM",
    "MMC_MENU_COMMAND_IDS",
    "MMCC_STANDARD_VIEW_SELECT",
    "MENUBUTTONDATA",
    "MMC_FILTER_TYPE",
    "MMC_STRING_FILTER",
    "MMC_INT_FILTER",
    "MMC_FILTER_NOVALUE",
    "MMC_FILTERDATA",
    "MMC_FILTER_CHANGE_CODE",
    "MFCC_DISABLE",
    "MFCC_ENABLE",
    "MFCC_VALUE_CHANGE",
    "MMC_RESTORE_VIEW",
    "MMC_EXPANDSYNC_STRUCT",
    "MMC_VISIBLE_COLUMNS",
    "MMC_NOTIFY_TYPE",
    "MMCN_ACTIVATE",
    "MMCN_ADD_IMAGES",
    "MMCN_BTN_CLICK",
    "MMCN_CLICK",
    "MMCN_COLUMN_CLICK",
    "MMCN_CONTEXTMENU",
    "MMCN_CUTORMOVE",
    "MMCN_DBLCLICK",
    "MMCN_DELETE",
    "MMCN_DESELECT_ALL",
    "MMCN_EXPAND",
    "MMCN_HELP",
    "MMCN_MENU_BTNCLICK",
    "MMCN_MINIMIZED",
    "MMCN_PASTE",
    "MMCN_PROPERTY_CHANGE",
    "MMCN_QUERY_PASTE",
    "MMCN_REFRESH",
    "MMCN_REMOVE_CHILDREN",
    "MMCN_RENAME",
    "MMCN_SELECT",
    "MMCN_SHOW",
    "MMCN_VIEW_CHANGE",
    "MMCN_SNAPINHELP",
    "MMCN_CONTEXTHELP",
    "MMCN_INITOCX",
    "MMCN_FILTER_CHANGE",
    "MMCN_FILTERBTN_CLICK",
    "MMCN_RESTORE_VIEW",
    "MMCN_PRINT",
    "MMCN_PRELOAD",
    "MMCN_LISTPAD",
    "MMCN_EXPANDSYNC",
    "MMCN_COLUMNS_CHANGED",
    "MMCN_CANPASTE_OUTOFPROC",
    "DATA_OBJECT_TYPES",
    "CCT_SCOPE",
    "CCT_RESULT",
    "CCT_SNAPIN_MANAGER",
    "CCT_UNINITIALIZED",
    "SMMCDataObjects",
    "SMMCObjectTypes",
    "SNodeID",
    "SNodeID2",
    "SColumnSetID",
    "IComponentData",
    "IComponent",
    "IResultDataCompare",
    "IResultOwnerData",
    "IConsole",
    "IHeaderCtrl",
    "CCM_INSERTIONPOINTID",
    "CCM_INSERTIONPOINTID_MASK_SPECIAL",
    "CCM_INSERTIONPOINTID_MASK_SHARED",
    "CCM_INSERTIONPOINTID_MASK_CREATE_PRIMARY",
    "CCM_INSERTIONPOINTID_MASK_ADD_PRIMARY",
    "CCM_INSERTIONPOINTID_MASK_ADD_3RDPARTY",
    "CCM_INSERTIONPOINTID_MASK_RESERVED",
    "CCM_INSERTIONPOINTID_MASK_FLAGINDEX",
    "CCM_INSERTIONPOINTID_PRIMARY_TOP",
    "CCM_INSERTIONPOINTID_PRIMARY_NEW",
    "CCM_INSERTIONPOINTID_PRIMARY_TASK",
    "CCM_INSERTIONPOINTID_PRIMARY_VIEW",
    "CCM_INSERTIONPOINTID_PRIMARY_HELP",
    "CCM_INSERTIONPOINTID_3RDPARTY_NEW",
    "CCM_INSERTIONPOINTID_3RDPARTY_TASK",
    "CCM_INSERTIONPOINTID_ROOT_MENU",
    "CCM_INSERTIONALLOWED",
    "CCM_INSERTIONALLOWED_TOP",
    "CCM_INSERTIONALLOWED_NEW",
    "CCM_INSERTIONALLOWED_TASK",
    "CCM_INSERTIONALLOWED_VIEW",
    "CCM_COMMANDID_MASK_CONSTANTS",
    "CCM_COMMANDID_MASK_RESERVED",
    "CCM_SPECIAL",
    "CCM_SPECIAL_SEPARATOR",
    "CCM_SPECIAL_SUBMENU",
    "CCM_SPECIAL_DEFAULT_ITEM",
    "CCM_SPECIAL_INSERTION_POINT",
    "CCM_SPECIAL_TESTONLY",
    "IContextMenuCallback",
    "IContextMenuProvider",
    "IExtendContextMenu",
    "IImageList",
    "IResultData",
    "IConsoleNameSpace",
    "IConsoleNameSpace2",
    "IPropertySheetCallback",
    "IPropertySheetProvider",
    "IExtendPropertySheet",
    "IControlbar",
    "IExtendControlbar",
    "IToolbar",
    "IConsoleVerb",
    "ISnapinAbout",
    "IMenuButton",
    "ISnapinHelp",
    "IExtendPropertySheet2",
    "IHeaderCtrl2",
    "ISnapinHelp2",
    "MMC_TASK_DISPLAY_TYPE",
    "MMC_TASK_DISPLAY_UNINITIALIZED",
    "MMC_TASK_DISPLAY_TYPE_SYMBOL",
    "MMC_TASK_DISPLAY_TYPE_VANILLA_GIF",
    "MMC_TASK_DISPLAY_TYPE_CHOCOLATE_GIF",
    "MMC_TASK_DISPLAY_TYPE_BITMAP",
    "MMC_TASK_DISPLAY_SYMBOL",
    "MMC_TASK_DISPLAY_BITMAP",
    "MMC_TASK_DISPLAY_OBJECT",
    "MMC_ACTION_TYPE",
    "MMC_ACTION_UNINITIALIZED",
    "MMC_ACTION_ID",
    "MMC_ACTION_LINK",
    "MMC_ACTION_SCRIPT",
    "MMC_TASK",
    "MMC_LISTPAD_INFO",
    "IEnumTASK",
    "IExtendTaskPad",
    "IConsole2",
    "IDisplayHelp",
    "IRequiredExtensions",
    "IStringTable",
    "MMC_COLUMN_DATA",
    "MMC_COLUMN_SET_DATA",
    "MMC_SORT_DATA",
    "MMC_SORT_SET_DATA",
    "IColumnData",
    "IconIdentifier",
    "Icon_None",
    "Icon_Error",
    "Icon_Question",
    "Icon_Warning",
    "Icon_Information",
    "Icon_First",
    "Icon_Last",
    "IMessageView",
    "RDITEMHDR",
    "RDCOMPARE",
    "IResultDataCompareEx",
    "MMC_VIEW_TYPE",
    "MMC_VIEW_TYPE_LIST",
    "MMC_VIEW_TYPE_HTML",
    "MMC_VIEW_TYPE_OCX",
    "RESULT_VIEW_TYPE_INFO",
    "CONTEXTMENUITEM2",
    "MMC_EXT_VIEW_DATA",
    "IComponentData2",
    "IComponent2",
    "IContextMenuCallback2",
    "IMMCVersionInfo",
    "IExtendView",
    "IViewExtensionCallback",
    "IConsolePower",
    "IConsolePowerSink",
    "INodeProperties",
    "IConsole3",
    "IResultData2",
]
