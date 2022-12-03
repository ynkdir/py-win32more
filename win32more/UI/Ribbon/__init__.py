from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.UI.Ribbon
import win32more.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
UI_ALL_COMMANDS = 0
UI_COLLECTION_INVALIDINDEX = 4294967295
def _define_LIBID_UIRibbon():
    return Guid('942f35c2-e83b-45ef-b0-85-ac-29-5d-d6-3d-5b')
def _define_IUIApplication_head():
    class IUIApplication(win32more.System.Com.IUnknown_head):
        Guid = Guid('d428903c-729a-491d-91-0d-68-2a-08-ff-25-22')
    return IUIApplication
def _define_IUIApplication():
    IUIApplication = win32more.UI.Ribbon.IUIApplication_head
    IUIApplication.OnViewChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.Ribbon.UI_VIEWTYPE,win32more.System.Com.IUnknown_head,win32more.UI.Ribbon.UI_VIEWVERB,Int32)(3, 'OnViewChanged', ((1, 'viewId'),(1, 'typeID'),(1, 'view'),(1, 'verb'),(1, 'uReasonCode'),)))
    IUIApplication.OnCreateUICommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.Ribbon.UI_COMMANDTYPE,POINTER(win32more.UI.Ribbon.IUICommandHandler_head))(4, 'OnCreateUICommand', ((1, 'commandId'),(1, 'typeID'),(1, 'commandHandler'),)))
    IUIApplication.OnDestroyUICommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.Ribbon.UI_COMMANDTYPE,win32more.UI.Ribbon.IUICommandHandler_head)(5, 'OnDestroyUICommand', ((1, 'commandId'),(1, 'typeID'),(1, 'commandHandler'),)))
    win32more.System.Com.IUnknown
    return IUIApplication
def _define_IUICollection_head():
    class IUICollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('df4f45bf-6f9d-4dd7-9d-68-d8-f9-cd-18-c4-db')
    return IUICollection
def _define_IUICollection():
    IUICollection = win32more.UI.Ribbon.IUICollection_head
    IUICollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IUICollection.GetItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IUnknown_head))(4, 'GetItem', ((1, 'index'),(1, 'item'),)))
    IUICollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(5, 'Add', ((1, 'item'),)))
    IUICollection.Insert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IUnknown_head)(6, 'Insert', ((1, 'index'),(1, 'item'),)))
    IUICollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'RemoveAt', ((1, 'index'),)))
    IUICollection.Replace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IUnknown_head)(8, 'Replace', ((1, 'indexReplaced'),(1, 'itemReplaceWith'),)))
    IUICollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'Clear', ()))
    win32more.System.Com.IUnknown
    return IUICollection
def _define_IUICollectionChangedEvent_head():
    class IUICollectionChangedEvent(win32more.System.Com.IUnknown_head):
        Guid = Guid('6502ae91-a14d-44b5-bb-d0-62-aa-cc-58-1d-52')
    return IUICollectionChangedEvent
def _define_IUICollectionChangedEvent():
    IUICollectionChangedEvent = win32more.UI.Ribbon.IUICollectionChangedEvent_head
    IUICollectionChangedEvent.OnChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Ribbon.UI_COLLECTIONCHANGE,UInt32,win32more.System.Com.IUnknown_head,UInt32,win32more.System.Com.IUnknown_head)(3, 'OnChanged', ((1, 'action'),(1, 'oldIndex'),(1, 'oldItem'),(1, 'newIndex'),(1, 'newItem'),)))
    win32more.System.Com.IUnknown
    return IUICollectionChangedEvent
def _define_IUICommandHandler_head():
    class IUICommandHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('75ae0a2d-dc03-4c9f-88-83-06-96-60-d0-be-b6')
    return IUICommandHandler
def _define_IUICommandHandler():
    IUICommandHandler = win32more.UI.Ribbon.IUICommandHandler_head
    IUICommandHandler.Execute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.Ribbon.UI_EXECUTIONVERB,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),win32more.UI.Ribbon.IUISimplePropertySet_head)(3, 'Execute', ((1, 'commandId'),(1, 'verb'),(1, 'key'),(1, 'currentValue'),(1, 'commandExecutionProperties'),)))
    IUICommandHandler.UpdateProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(4, 'UpdateProperty', ((1, 'commandId'),(1, 'key'),(1, 'currentValue'),(1, 'newValue'),)))
    win32more.System.Com.IUnknown
    return IUICommandHandler
def _define_IUIContextualUI_head():
    class IUIContextualUI(win32more.System.Com.IUnknown_head):
        Guid = Guid('eea11f37-7c46-437c-8e-55-b5-21-22-b2-92-93')
    return IUIContextualUI
def _define_IUIContextualUI():
    IUIContextualUI = win32more.UI.Ribbon.IUIContextualUI_head
    IUIContextualUI.ShowAtLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32)(3, 'ShowAtLocation', ((1, 'x'),(1, 'y'),)))
    win32more.System.Com.IUnknown
    return IUIContextualUI
def _define_IUIEventingManager_head():
    class IUIEventingManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('3be6ea7f-9a9b-4198-93-68-9b-0f-92-3b-d5-34')
    return IUIEventingManager
def _define_IUIEventingManager():
    IUIEventingManager = win32more.UI.Ribbon.IUIEventingManager_head
    IUIEventingManager.SetEventLogger = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Ribbon.IUIEventLogger_head)(3, 'SetEventLogger', ((1, 'eventLogger'),)))
    win32more.System.Com.IUnknown
    return IUIEventingManager
def _define_IUIEventLogger_head():
    class IUIEventLogger(win32more.System.Com.IUnknown_head):
        Guid = Guid('ec3e1034-dbf4-41a1-95-d5-03-e0-f1-02-6e-05')
    return IUIEventLogger
def _define_IUIEventLogger():
    IUIEventLogger = win32more.UI.Ribbon.IUIEventLogger_head
    IUIEventLogger.OnUIEvent = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.UI.Ribbon.UI_EVENTPARAMS_head))(3, 'OnUIEvent', ((1, 'pEventParams'),)))
    win32more.System.Com.IUnknown
    return IUIEventLogger
def _define_IUIFramework_head():
    class IUIFramework(win32more.System.Com.IUnknown_head):
        Guid = Guid('f4f0385d-6872-43a8-ad-09-4c-33-9c-b3-f5-c5')
    return IUIFramework
def _define_IUIFramework():
    IUIFramework = win32more.UI.Ribbon.IUIFramework_head
    IUIFramework.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.UI.Ribbon.IUIApplication_head)(3, 'Initialize', ((1, 'frameWnd'),(1, 'application'),)))
    IUIFramework.Destroy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Destroy', ()))
    IUIFramework.LoadUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR)(5, 'LoadUI', ((1, 'instance'),(1, 'resourceName'),)))
    IUIFramework.GetView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p))(6, 'GetView', ((1, 'viewId'),(1, 'riid'),(1, 'ppv'),)))
    IUIFramework.GetUICommandProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(7, 'GetUICommandProperty', ((1, 'commandId'),(1, 'key'),(1, 'value'),)))
    IUIFramework.SetUICommandProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(8, 'SetUICommandProperty', ((1, 'commandId'),(1, 'key'),(1, 'value'),)))
    IUIFramework.InvalidateUICommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.Ribbon.UI_INVALIDATIONS,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(9, 'InvalidateUICommand', ((1, 'commandId'),(1, 'flags'),(1, 'key'),)))
    IUIFramework.FlushPendingInvalidations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'FlushPendingInvalidations', ()))
    IUIFramework.SetModes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(11, 'SetModes', ((1, 'iModes'),)))
    win32more.System.Com.IUnknown
    return IUIFramework
def _define_IUIImage_head():
    class IUIImage(win32more.System.Com.IUnknown_head):
        Guid = Guid('23c8c838-4de6-436b-ab-01-55-54-bb-7c-30-dd')
    return IUIImage
def _define_IUIImage():
    IUIImage = win32more.UI.Ribbon.IUIImage_head
    IUIImage.GetBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Gdi.HBITMAP))(3, 'GetBitmap', ((1, 'bitmap'),)))
    win32more.System.Com.IUnknown
    return IUIImage
def _define_IUIImageFromBitmap_head():
    class IUIImageFromBitmap(win32more.System.Com.IUnknown_head):
        Guid = Guid('18aba7f3-4c1c-4ba2-bf-6c-f5-c3-32-6f-a8-16')
    return IUIImageFromBitmap
def _define_IUIImageFromBitmap():
    IUIImageFromBitmap = win32more.UI.Ribbon.IUIImageFromBitmap_head
    IUIImageFromBitmap.CreateImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HBITMAP,win32more.UI.Ribbon.UI_OWNERSHIP,POINTER(win32more.UI.Ribbon.IUIImage_head))(3, 'CreateImage', ((1, 'bitmap'),(1, 'options'),(1, 'image'),)))
    win32more.System.Com.IUnknown
    return IUIImageFromBitmap
def _define_IUIRibbon_head():
    class IUIRibbon(win32more.System.Com.IUnknown_head):
        Guid = Guid('803982ab-370a-4f7e-a9-e7-87-84-03-6a-6e-26')
    return IUIRibbon
def _define_IUIRibbon():
    IUIRibbon = win32more.UI.Ribbon.IUIRibbon_head
    IUIRibbon.GetHeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetHeight', ((1, 'cy'),)))
    IUIRibbon.LoadSettingsFromStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(4, 'LoadSettingsFromStream', ((1, 'pStream'),)))
    IUIRibbon.SaveSettingsToStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(5, 'SaveSettingsToStream', ((1, 'pStream'),)))
    win32more.System.Com.IUnknown
    return IUIRibbon
def _define_IUISimplePropertySet_head():
    class IUISimplePropertySet(win32more.System.Com.IUnknown_head):
        Guid = Guid('c205bb48-5b1c-4219-a1-06-15-bd-0a-5f-24-e2')
    return IUISimplePropertySet
def _define_IUISimplePropertySet():
    IUISimplePropertySet = win32more.UI.Ribbon.IUISimplePropertySet_head
    IUISimplePropertySet.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(3, 'GetValue', ((1, 'key'),(1, 'value'),)))
    win32more.System.Com.IUnknown
    return IUISimplePropertySet
UI_COLLECTIONCHANGE = Int32
UI_COLLECTIONCHANGE_INSERT = 0
UI_COLLECTIONCHANGE_REMOVE = 1
UI_COLLECTIONCHANGE_REPLACE = 2
UI_COLLECTIONCHANGE_RESET = 3
UI_COMMANDTYPE = Int32
UI_COMMANDTYPE_UNKNOWN = 0
UI_COMMANDTYPE_GROUP = 1
UI_COMMANDTYPE_ACTION = 2
UI_COMMANDTYPE_ANCHOR = 3
UI_COMMANDTYPE_CONTEXT = 4
UI_COMMANDTYPE_COLLECTION = 5
UI_COMMANDTYPE_COMMANDCOLLECTION = 6
UI_COMMANDTYPE_DECIMAL = 7
UI_COMMANDTYPE_BOOLEAN = 8
UI_COMMANDTYPE_FONT = 9
UI_COMMANDTYPE_RECENTITEMS = 10
UI_COMMANDTYPE_COLORANCHOR = 11
UI_COMMANDTYPE_COLORCOLLECTION = 12
UI_CONTEXTAVAILABILITY = Int32
UI_CONTEXTAVAILABILITY_NOTAVAILABLE = 0
UI_CONTEXTAVAILABILITY_AVAILABLE = 1
UI_CONTEXTAVAILABILITY_ACTIVE = 2
UI_CONTROLDOCK = Int32
UI_CONTROLDOCK_TOP = 1
UI_CONTROLDOCK_BOTTOM = 3
UI_EVENTLOCATION = Int32
UI_EVENTLOCATION_Ribbon = 0
UI_EVENTLOCATION_QAT = 1
UI_EVENTLOCATION_ApplicationMenu = 2
UI_EVENTLOCATION_ContextPopup = 3
def _define_UI_EVENTPARAMS_head():
    class UI_EVENTPARAMS(Structure):
        pass
    return UI_EVENTPARAMS
def _define_UI_EVENTPARAMS():
    UI_EVENTPARAMS = win32more.UI.Ribbon.UI_EVENTPARAMS_head
    class UI_EVENTPARAMS__Anonymous_e__Union(Union):
        pass
    UI_EVENTPARAMS__Anonymous_e__Union._fields_ = [
        ('Modes', Int32),
        ('Params', win32more.UI.Ribbon.UI_EVENTPARAMS_COMMAND),
    ]
    UI_EVENTPARAMS._anonymous_ = [
        'Anonymous',
    ]
    UI_EVENTPARAMS._fields_ = [
        ('EventType', win32more.UI.Ribbon.UI_EVENTTYPE),
        ('Anonymous', UI_EVENTPARAMS__Anonymous_e__Union),
    ]
    return UI_EVENTPARAMS
def _define_UI_EVENTPARAMS_COMMAND_head():
    class UI_EVENTPARAMS_COMMAND(Structure):
        pass
    return UI_EVENTPARAMS_COMMAND
def _define_UI_EVENTPARAMS_COMMAND():
    UI_EVENTPARAMS_COMMAND = win32more.UI.Ribbon.UI_EVENTPARAMS_COMMAND_head
    UI_EVENTPARAMS_COMMAND._fields_ = [
        ('CommandID', UInt32),
        ('CommandName', win32more.Foundation.PWSTR),
        ('ParentCommandID', UInt32),
        ('ParentCommandName', win32more.Foundation.PWSTR),
        ('SelectionIndex', UInt32),
        ('Location', win32more.UI.Ribbon.UI_EVENTLOCATION),
    ]
    return UI_EVENTPARAMS_COMMAND
UI_EVENTTYPE = Int32
UI_EVENTTYPE_ApplicationMenuOpened = 0
UI_EVENTTYPE_RibbonMinimized = 1
UI_EVENTTYPE_RibbonExpanded = 2
UI_EVENTTYPE_ApplicationModeSwitched = 3
UI_EVENTTYPE_TabActivated = 4
UI_EVENTTYPE_MenuOpened = 5
UI_EVENTTYPE_CommandExecuted = 6
UI_EVENTTYPE_TooltipShown = 7
UI_EXECUTIONVERB = Int32
UI_EXECUTIONVERB_EXECUTE = 0
UI_EXECUTIONVERB_PREVIEW = 1
UI_EXECUTIONVERB_CANCELPREVIEW = 2
UI_FONTDELTASIZE = Int32
UI_FONTDELTASIZE_GROW = 0
UI_FONTDELTASIZE_SHRINK = 1
UI_FONTPROPERTIES = Int32
UI_FONTPROPERTIES_NOTAVAILABLE = 0
UI_FONTPROPERTIES_NOTSET = 1
UI_FONTPROPERTIES_SET = 2
UI_FONTUNDERLINE = Int32
UI_FONTUNDERLINE_NOTAVAILABLE = 0
UI_FONTUNDERLINE_NOTSET = 1
UI_FONTUNDERLINE_SET = 2
UI_FONTVERTICALPOSITION = Int32
UI_FONTVERTICALPOSITION_NOTAVAILABLE = 0
UI_FONTVERTICALPOSITION_NOTSET = 1
UI_FONTVERTICALPOSITION_SUPERSCRIPT = 2
UI_FONTVERTICALPOSITION_SUBSCRIPT = 3
UI_INVALIDATIONS = Int32
UI_INVALIDATIONS_STATE = 1
UI_INVALIDATIONS_VALUE = 2
UI_INVALIDATIONS_PROPERTY = 4
UI_INVALIDATIONS_ALLPROPERTIES = 8
UI_OWNERSHIP = Int32
UI_OWNERSHIP_TRANSFER = 0
UI_OWNERSHIP_COPY = 1
UI_SWATCHCOLORMODE = Int32
UI_SWATCHCOLORMODE_NORMAL = 0
UI_SWATCHCOLORMODE_MONOCHROME = 1
UI_SWATCHCOLORTYPE = Int32
UI_SWATCHCOLORTYPE_NOCOLOR = 0
UI_SWATCHCOLORTYPE_AUTOMATIC = 1
UI_SWATCHCOLORTYPE_RGB = 2
UI_VIEWTYPE = Int32
UI_VIEWTYPE_RIBBON = 1
UI_VIEWVERB = Int32
UI_VIEWVERB_CREATE = 0
UI_VIEWVERB_DESTROY = 1
UI_VIEWVERB_SIZE = 2
UI_VIEWVERB_ERROR = 3
UIRibbonFramework = Guid('926749fa-2615-4987-88-45-c3-3e-65-f2-b9-57')
UIRibbonImageFromBitmapFactory = Guid('0f7434b6-59b6-4250-99-9e-d1-68-d6-ae-42-93')
__all__ = [
    "IUIApplication",
    "IUICollection",
    "IUICollectionChangedEvent",
    "IUICommandHandler",
    "IUIContextualUI",
    "IUIEventLogger",
    "IUIEventingManager",
    "IUIFramework",
    "IUIImage",
    "IUIImageFromBitmap",
    "IUIRibbon",
    "IUISimplePropertySet",
    "LIBID_UIRibbon",
    "UIRibbonFramework",
    "UIRibbonImageFromBitmapFactory",
    "UI_ALL_COMMANDS",
    "UI_COLLECTIONCHANGE",
    "UI_COLLECTIONCHANGE_INSERT",
    "UI_COLLECTIONCHANGE_REMOVE",
    "UI_COLLECTIONCHANGE_REPLACE",
    "UI_COLLECTIONCHANGE_RESET",
    "UI_COLLECTION_INVALIDINDEX",
    "UI_COMMANDTYPE",
    "UI_COMMANDTYPE_ACTION",
    "UI_COMMANDTYPE_ANCHOR",
    "UI_COMMANDTYPE_BOOLEAN",
    "UI_COMMANDTYPE_COLLECTION",
    "UI_COMMANDTYPE_COLORANCHOR",
    "UI_COMMANDTYPE_COLORCOLLECTION",
    "UI_COMMANDTYPE_COMMANDCOLLECTION",
    "UI_COMMANDTYPE_CONTEXT",
    "UI_COMMANDTYPE_DECIMAL",
    "UI_COMMANDTYPE_FONT",
    "UI_COMMANDTYPE_GROUP",
    "UI_COMMANDTYPE_RECENTITEMS",
    "UI_COMMANDTYPE_UNKNOWN",
    "UI_CONTEXTAVAILABILITY",
    "UI_CONTEXTAVAILABILITY_ACTIVE",
    "UI_CONTEXTAVAILABILITY_AVAILABLE",
    "UI_CONTEXTAVAILABILITY_NOTAVAILABLE",
    "UI_CONTROLDOCK",
    "UI_CONTROLDOCK_BOTTOM",
    "UI_CONTROLDOCK_TOP",
    "UI_EVENTLOCATION",
    "UI_EVENTLOCATION_ApplicationMenu",
    "UI_EVENTLOCATION_ContextPopup",
    "UI_EVENTLOCATION_QAT",
    "UI_EVENTLOCATION_Ribbon",
    "UI_EVENTPARAMS",
    "UI_EVENTPARAMS_COMMAND",
    "UI_EVENTTYPE",
    "UI_EVENTTYPE_ApplicationMenuOpened",
    "UI_EVENTTYPE_ApplicationModeSwitched",
    "UI_EVENTTYPE_CommandExecuted",
    "UI_EVENTTYPE_MenuOpened",
    "UI_EVENTTYPE_RibbonExpanded",
    "UI_EVENTTYPE_RibbonMinimized",
    "UI_EVENTTYPE_TabActivated",
    "UI_EVENTTYPE_TooltipShown",
    "UI_EXECUTIONVERB",
    "UI_EXECUTIONVERB_CANCELPREVIEW",
    "UI_EXECUTIONVERB_EXECUTE",
    "UI_EXECUTIONVERB_PREVIEW",
    "UI_FONTDELTASIZE",
    "UI_FONTDELTASIZE_GROW",
    "UI_FONTDELTASIZE_SHRINK",
    "UI_FONTPROPERTIES",
    "UI_FONTPROPERTIES_NOTAVAILABLE",
    "UI_FONTPROPERTIES_NOTSET",
    "UI_FONTPROPERTIES_SET",
    "UI_FONTUNDERLINE",
    "UI_FONTUNDERLINE_NOTAVAILABLE",
    "UI_FONTUNDERLINE_NOTSET",
    "UI_FONTUNDERLINE_SET",
    "UI_FONTVERTICALPOSITION",
    "UI_FONTVERTICALPOSITION_NOTAVAILABLE",
    "UI_FONTVERTICALPOSITION_NOTSET",
    "UI_FONTVERTICALPOSITION_SUBSCRIPT",
    "UI_FONTVERTICALPOSITION_SUPERSCRIPT",
    "UI_INVALIDATIONS",
    "UI_INVALIDATIONS_ALLPROPERTIES",
    "UI_INVALIDATIONS_PROPERTY",
    "UI_INVALIDATIONS_STATE",
    "UI_INVALIDATIONS_VALUE",
    "UI_OWNERSHIP",
    "UI_OWNERSHIP_COPY",
    "UI_OWNERSHIP_TRANSFER",
    "UI_SWATCHCOLORMODE",
    "UI_SWATCHCOLORMODE_MONOCHROME",
    "UI_SWATCHCOLORMODE_NORMAL",
    "UI_SWATCHCOLORTYPE",
    "UI_SWATCHCOLORTYPE_AUTOMATIC",
    "UI_SWATCHCOLORTYPE_NOCOLOR",
    "UI_SWATCHCOLORTYPE_RGB",
    "UI_VIEWTYPE",
    "UI_VIEWTYPE_RIBBON",
    "UI_VIEWVERB",
    "UI_VIEWVERB_CREATE",
    "UI_VIEWVERB_DESTROY",
    "UI_VIEWVERB_ERROR",
    "UI_VIEWVERB_SIZE",
]
