from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
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
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
UI_ALL_COMMANDS: UInt32 = 0
UI_COLLECTION_INVALIDINDEX: UInt32 = 4294967295
LIBID_UIRibbon: Guid = Guid('942f35c2-e83b-45ef-b0-85-ac-29-5d-d6-3d-5b')
class IUIApplication(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d428903c-729a-491d-91-0d-68-2a-08-ff-25-22')
    @commethod(3)
    def OnViewChanged(viewId: UInt32, typeID: win32more.UI.Ribbon.UI_VIEWTYPE, view: win32more.System.Com.IUnknown_head, verb: win32more.UI.Ribbon.UI_VIEWVERB, uReasonCode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnCreateUICommand(commandId: UInt32, typeID: win32more.UI.Ribbon.UI_COMMANDTYPE, commandHandler: POINTER(win32more.UI.Ribbon.IUICommandHandler_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnDestroyUICommand(commandId: UInt32, typeID: win32more.UI.Ribbon.UI_COMMANDTYPE, commandHandler: win32more.UI.Ribbon.IUICommandHandler_head) -> win32more.Foundation.HRESULT: ...
class IUICollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('df4f45bf-6f9d-4dd7-9d-68-d8-f9-cd-18-c4-db')
    @commethod(3)
    def GetCount(count: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(index: UInt32, item: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Add(item: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Insert(index: UInt32, item: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAt(index: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Replace(indexReplaced: UInt32, itemReplaceWith: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Clear() -> win32more.Foundation.HRESULT: ...
class IUICollectionChangedEvent(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6502ae91-a14d-44b5-bb-d0-62-aa-cc-58-1d-52')
    @commethod(3)
    def OnChanged(action: win32more.UI.Ribbon.UI_COLLECTIONCHANGE, oldIndex: UInt32, oldItem: win32more.System.Com.IUnknown_head, newIndex: UInt32, newItem: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class IUICommandHandler(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('75ae0a2d-dc03-4c9f-88-83-06-96-60-d0-be-b6')
    @commethod(3)
    def Execute(commandId: UInt32, verb: win32more.UI.Ribbon.UI_EXECUTIONVERB, key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), currentValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), commandExecutionProperties: win32more.UI.Ribbon.IUISimplePropertySet_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateProperty(commandId: UInt32, key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), currentValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), newValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IUIContextualUI(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('eea11f37-7c46-437c-8e-55-b5-21-22-b2-92-93')
    @commethod(3)
    def ShowAtLocation(x: Int32, y: Int32) -> win32more.Foundation.HRESULT: ...
class IUIEventingManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3be6ea7f-9a9b-4198-93-68-9b-0f-92-3b-d5-34')
    @commethod(3)
    def SetEventLogger(eventLogger: win32more.UI.Ribbon.IUIEventLogger_head) -> win32more.Foundation.HRESULT: ...
class IUIEventLogger(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ec3e1034-dbf4-41a1-95-d5-03-e0-f1-02-6e-05')
    @commethod(3)
    def OnUIEvent(pEventParams: POINTER(win32more.UI.Ribbon.UI_EVENTPARAMS_head)) -> Void: ...
class IUIFramework(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f4f0385d-6872-43a8-ad-09-4c-33-9c-b3-f5-c5')
    @commethod(3)
    def Initialize(frameWnd: win32more.Foundation.HWND, application: win32more.UI.Ribbon.IUIApplication_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Destroy() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def LoadUI(instance: win32more.Foundation.HINSTANCE, resourceName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetView(viewId: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetUICommandProperty(commandId: UInt32, key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), value: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetUICommandProperty(commandId: UInt32, key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), value: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def InvalidateUICommand(commandId: UInt32, flags: win32more.UI.Ribbon.UI_INVALIDATIONS, key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def FlushPendingInvalidations() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetModes(iModes: Int32) -> win32more.Foundation.HRESULT: ...
class IUIImage(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('23c8c838-4de6-436b-ab-01-55-54-bb-7c-30-dd')
    @commethod(3)
    def GetBitmap(bitmap: POINTER(win32more.Graphics.Gdi.HBITMAP)) -> win32more.Foundation.HRESULT: ...
class IUIImageFromBitmap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('18aba7f3-4c1c-4ba2-bf-6c-f5-c3-32-6f-a8-16')
    @commethod(3)
    def CreateImage(bitmap: win32more.Graphics.Gdi.HBITMAP, options: win32more.UI.Ribbon.UI_OWNERSHIP, image: POINTER(win32more.UI.Ribbon.IUIImage_head)) -> win32more.Foundation.HRESULT: ...
class IUIRibbon(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('803982ab-370a-4f7e-a9-e7-87-84-03-6a-6e-26')
    @commethod(3)
    def GetHeight(cy: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def LoadSettingsFromStream(pStream: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SaveSettingsToStream(pStream: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
class IUISimplePropertySet(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c205bb48-5b1c-4219-a1-06-15-bd-0a-5f-24-e2')
    @commethod(3)
    def GetValue(key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), value: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
UI_COLLECTIONCHANGE = Int32
UI_COLLECTIONCHANGE_INSERT: UI_COLLECTIONCHANGE = 0
UI_COLLECTIONCHANGE_REMOVE: UI_COLLECTIONCHANGE = 1
UI_COLLECTIONCHANGE_REPLACE: UI_COLLECTIONCHANGE = 2
UI_COLLECTIONCHANGE_RESET: UI_COLLECTIONCHANGE = 3
UI_COMMANDTYPE = Int32
UI_COMMANDTYPE_UNKNOWN: UI_COMMANDTYPE = 0
UI_COMMANDTYPE_GROUP: UI_COMMANDTYPE = 1
UI_COMMANDTYPE_ACTION: UI_COMMANDTYPE = 2
UI_COMMANDTYPE_ANCHOR: UI_COMMANDTYPE = 3
UI_COMMANDTYPE_CONTEXT: UI_COMMANDTYPE = 4
UI_COMMANDTYPE_COLLECTION: UI_COMMANDTYPE = 5
UI_COMMANDTYPE_COMMANDCOLLECTION: UI_COMMANDTYPE = 6
UI_COMMANDTYPE_DECIMAL: UI_COMMANDTYPE = 7
UI_COMMANDTYPE_BOOLEAN: UI_COMMANDTYPE = 8
UI_COMMANDTYPE_FONT: UI_COMMANDTYPE = 9
UI_COMMANDTYPE_RECENTITEMS: UI_COMMANDTYPE = 10
UI_COMMANDTYPE_COLORANCHOR: UI_COMMANDTYPE = 11
UI_COMMANDTYPE_COLORCOLLECTION: UI_COMMANDTYPE = 12
UI_CONTEXTAVAILABILITY = Int32
UI_CONTEXTAVAILABILITY_NOTAVAILABLE: UI_CONTEXTAVAILABILITY = 0
UI_CONTEXTAVAILABILITY_AVAILABLE: UI_CONTEXTAVAILABILITY = 1
UI_CONTEXTAVAILABILITY_ACTIVE: UI_CONTEXTAVAILABILITY = 2
UI_CONTROLDOCK = Int32
UI_CONTROLDOCK_TOP: UI_CONTROLDOCK = 1
UI_CONTROLDOCK_BOTTOM: UI_CONTROLDOCK = 3
UI_EVENTLOCATION = Int32
UI_EVENTLOCATION_Ribbon: UI_EVENTLOCATION = 0
UI_EVENTLOCATION_QAT: UI_EVENTLOCATION = 1
UI_EVENTLOCATION_ApplicationMenu: UI_EVENTLOCATION = 2
UI_EVENTLOCATION_ContextPopup: UI_EVENTLOCATION = 3
class UI_EVENTPARAMS(Structure):
    EventType: win32more.UI.Ribbon.UI_EVENTTYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Modes: Int32
        Params: win32more.UI.Ribbon.UI_EVENTPARAMS_COMMAND
class UI_EVENTPARAMS_COMMAND(Structure):
    CommandID: UInt32
    CommandName: win32more.Foundation.PWSTR
    ParentCommandID: UInt32
    ParentCommandName: win32more.Foundation.PWSTR
    SelectionIndex: UInt32
    Location: win32more.UI.Ribbon.UI_EVENTLOCATION
UI_EVENTTYPE = Int32
UI_EVENTTYPE_ApplicationMenuOpened: UI_EVENTTYPE = 0
UI_EVENTTYPE_RibbonMinimized: UI_EVENTTYPE = 1
UI_EVENTTYPE_RibbonExpanded: UI_EVENTTYPE = 2
UI_EVENTTYPE_ApplicationModeSwitched: UI_EVENTTYPE = 3
UI_EVENTTYPE_TabActivated: UI_EVENTTYPE = 4
UI_EVENTTYPE_MenuOpened: UI_EVENTTYPE = 5
UI_EVENTTYPE_CommandExecuted: UI_EVENTTYPE = 6
UI_EVENTTYPE_TooltipShown: UI_EVENTTYPE = 7
UI_EXECUTIONVERB = Int32
UI_EXECUTIONVERB_EXECUTE: UI_EXECUTIONVERB = 0
UI_EXECUTIONVERB_PREVIEW: UI_EXECUTIONVERB = 1
UI_EXECUTIONVERB_CANCELPREVIEW: UI_EXECUTIONVERB = 2
UI_FONTDELTASIZE = Int32
UI_FONTDELTASIZE_GROW: UI_FONTDELTASIZE = 0
UI_FONTDELTASIZE_SHRINK: UI_FONTDELTASIZE = 1
UI_FONTPROPERTIES = Int32
UI_FONTPROPERTIES_NOTAVAILABLE: UI_FONTPROPERTIES = 0
UI_FONTPROPERTIES_NOTSET: UI_FONTPROPERTIES = 1
UI_FONTPROPERTIES_SET: UI_FONTPROPERTIES = 2
UI_FONTUNDERLINE = Int32
UI_FONTUNDERLINE_NOTAVAILABLE: UI_FONTUNDERLINE = 0
UI_FONTUNDERLINE_NOTSET: UI_FONTUNDERLINE = 1
UI_FONTUNDERLINE_SET: UI_FONTUNDERLINE = 2
UI_FONTVERTICALPOSITION = Int32
UI_FONTVERTICALPOSITION_NOTAVAILABLE: UI_FONTVERTICALPOSITION = 0
UI_FONTVERTICALPOSITION_NOTSET: UI_FONTVERTICALPOSITION = 1
UI_FONTVERTICALPOSITION_SUPERSCRIPT: UI_FONTVERTICALPOSITION = 2
UI_FONTVERTICALPOSITION_SUBSCRIPT: UI_FONTVERTICALPOSITION = 3
UI_INVALIDATIONS = Int32
UI_INVALIDATIONS_STATE: UI_INVALIDATIONS = 1
UI_INVALIDATIONS_VALUE: UI_INVALIDATIONS = 2
UI_INVALIDATIONS_PROPERTY: UI_INVALIDATIONS = 4
UI_INVALIDATIONS_ALLPROPERTIES: UI_INVALIDATIONS = 8
UI_OWNERSHIP = Int32
UI_OWNERSHIP_TRANSFER: UI_OWNERSHIP = 0
UI_OWNERSHIP_COPY: UI_OWNERSHIP = 1
UI_SWATCHCOLORMODE = Int32
UI_SWATCHCOLORMODE_NORMAL: UI_SWATCHCOLORMODE = 0
UI_SWATCHCOLORMODE_MONOCHROME: UI_SWATCHCOLORMODE = 1
UI_SWATCHCOLORTYPE = Int32
UI_SWATCHCOLORTYPE_NOCOLOR: UI_SWATCHCOLORTYPE = 0
UI_SWATCHCOLORTYPE_AUTOMATIC: UI_SWATCHCOLORTYPE = 1
UI_SWATCHCOLORTYPE_RGB: UI_SWATCHCOLORTYPE = 2
UI_VIEWTYPE = Int32
UI_VIEWTYPE_RIBBON: UI_VIEWTYPE = 1
UI_VIEWVERB = Int32
UI_VIEWVERB_CREATE: UI_VIEWVERB = 0
UI_VIEWVERB_DESTROY: UI_VIEWVERB = 1
UI_VIEWVERB_SIZE: UI_VIEWVERB = 2
UI_VIEWVERB_ERROR: UI_VIEWVERB = 3
UIRibbonFramework = Guid('926749fa-2615-4987-88-45-c3-3e-65-f2-b9-57')
UIRibbonImageFromBitmapFactory = Guid('0f7434b6-59b6-4250-99-9e-d1-68-d6-ae-42-93')
make_head(_module, 'IUIApplication')
make_head(_module, 'IUICollection')
make_head(_module, 'IUICollectionChangedEvent')
make_head(_module, 'IUICommandHandler')
make_head(_module, 'IUIContextualUI')
make_head(_module, 'IUIEventingManager')
make_head(_module, 'IUIEventLogger')
make_head(_module, 'IUIFramework')
make_head(_module, 'IUIImage')
make_head(_module, 'IUIImageFromBitmap')
make_head(_module, 'IUIRibbon')
make_head(_module, 'IUISimplePropertySet')
make_head(_module, 'UI_EVENTPARAMS')
make_head(_module, 'UI_EVENTPARAMS_COMMAND')
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
