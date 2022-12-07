from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.SideShow
import win32more.UI.Shell.PropertiesSystem
import win32more.UI.WindowsAndMessaging
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
SIDESHOW_ENDPOINT_SIMPLE_CONTENT_FORMAT: Guid = Guid('a9a5353f-2d4b-47ce-93-ee-75-9f-3a-7d-da-4f')
SIDESHOW_ENDPOINT_ICAL: Guid = Guid('4dff36b5-9dde-4f76-9a-2a-96-43-50-47-06-3d')
SIDESHOW_CAPABILITY_DEVICE_PROPERTIES: Guid = Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99')
def SIDESHOW_CAPABILITY_DEVICE_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=1)
def SIDESHOW_CAPABILITY_SCREEN_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=2)
def SIDESHOW_CAPABILITY_SCREEN_WIDTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=3)
def SIDESHOW_CAPABILITY_SCREEN_HEIGHT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=4)
def SIDESHOW_CAPABILITY_COLOR_DEPTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=5)
def SIDESHOW_CAPABILITY_COLOR_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=6)
def SIDESHOW_CAPABILITY_DATA_CACHE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=7)
def SIDESHOW_CAPABILITY_SUPPORTED_LANGUAGES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=8)
def SIDESHOW_CAPABILITY_CURRENT_LANGUAGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=9)
def SIDESHOW_CAPABILITY_SUPPORTED_THEMES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=10)
def SIDESHOW_CAPABILITY_SUPPORTED_IMAGE_FORMATS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=14)
def SIDESHOW_CAPABILITY_CLIENT_AREA_WIDTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=15)
def SIDESHOW_CAPABILITY_CLIENT_AREA_HEIGHT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=16)
GUID_DEVINTERFACE_SIDESHOW: Guid = Guid('152e5811-feb9-4b00-90-f4-d3-29-47-ae-16-81')
SIDESHOW_CONTENT_MISSING_EVENT: Guid = Guid('5007fba8-d313-439f-be-a2-a5-02-01-d3-e9-a8')
SIDESHOW_APPLICATION_EVENT: Guid = Guid('4cb572fa-1d3b-49b3-a1-7a-2e-6b-ff-05-28-54')
SIDESHOW_USER_CHANGE_REQUEST_EVENT: Guid = Guid('5009673c-3f7d-4c7e-99-71-ea-a2-e9-1f-15-75')
SIDESHOW_NEW_EVENT_DATA_AVAILABLE: Guid = Guid('57813854-2fc1-411c-a5-9f-f2-49-27-60-88-04')
CONTENT_ID_GLANCE: UInt32 = 0
SIDESHOW_EVENTID_APPLICATION_ENTER: UInt32 = 4294901760
SIDESHOW_EVENTID_APPLICATION_EXIT: UInt32 = 4294901761
CONTENT_ID_HOME: UInt32 = 1
VERSION_1_WINDOWS_7: UInt32 = 0
class APPLICATION_EVENT_DATA(Structure):
    cbApplicationEventData: UInt32
    ApplicationId: Guid
    EndpointId: Guid
    dwEventId: UInt32
    cbEventData: UInt32
    bEventData: Byte * 1
    _pack_ = 1
class CONTENT_MISSING_EVENT_DATA(Structure):
    cbContentMissingEventData: UInt32
    ApplicationId: Guid
    EndpointId: Guid
    ContentId: UInt32
    _pack_ = 1
class DEVICE_USER_CHANGE_EVENT_DATA(Structure):
    cbDeviceUserChangeEventData: UInt32
    wszUser: Char
    _pack_ = 1
class EVENT_DATA_HEADER(Structure):
    cbEventDataHeader: UInt32
    guidEventType: Guid
    dwVersion: UInt32
    cbEventDataSid: UInt32
    _pack_ = 1
class ISideShowBulkCapabilities(c_void_p):
    extends: win32more.System.SideShow.ISideShowCapabilities
    Guid = Guid('3a2b7fbc-3ad5-48bd-bb-f1-0e-6c-fb-d1-08-07')
    @commethod(4)
    def GetCapabilities(in_keyCollection: win32more.System.SideShow.ISideShowKeyCollection_head, inout_pValues: POINTER(win32more.System.SideShow.ISideShowPropVariantCollection_head)) -> win32more.Foundation.HRESULT: ...
class ISideShowCapabilities(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('535e1379-c09e-4a54-a5-11-59-7b-ab-3a-72-b8')
    @commethod(3)
    def GetCapability(in_keyCapability: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head), inout_pValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
class ISideShowCapabilitiesCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('50305597-5e0d-4ff7-b3-af-33-d0-d9-bd-52-dd')
    @commethod(3)
    def GetCount(out_pdwCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(in_dwIndex: UInt32, out_ppCapabilities: POINTER(win32more.System.SideShow.ISideShowCapabilities_head)) -> win32more.Foundation.HRESULT: ...
class ISideShowContent(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c18552ed-74ff-4fec-be-07-4c-fe-d2-9d-48-87')
    @commethod(3)
    def GetContent(in_pICapabilities: win32more.System.SideShow.ISideShowCapabilities_head, out_pdwSize: POINTER(UInt32), out_ppbData: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_ContentId(out_pcontentId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_DifferentiateContent(out_pfDifferentiateContent: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ISideShowContentManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a5d5b66b-eef9-41db-8d-7e-e1-7c-33-ab-10-b0')
    @commethod(3)
    def Add(in_pIContent: win32more.System.SideShow.ISideShowContent_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(in_contentId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAll() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetEventSink(in_pIEvents: win32more.System.SideShow.ISideShowEvents_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetDeviceCapabilities(out_ppCollection: POINTER(win32more.System.SideShow.ISideShowCapabilitiesCollection_head)) -> win32more.Foundation.HRESULT: ...
class ISideShowEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('61feca4c-deb4-4a7e-8d-75-51-f1-13-2d-61-5b')
    @commethod(3)
    def ContentMissing(in_contentId: UInt32, out_ppIContent: POINTER(win32more.System.SideShow.ISideShowContent_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ApplicationEvent(in_pICapabilities: win32more.System.SideShow.ISideShowCapabilities_head, in_dwEventId: UInt32, in_dwEventSize: UInt32, in_pbEventData: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def DeviceAdded(in_pIDevice: win32more.System.SideShow.ISideShowCapabilities_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def DeviceRemoved(in_pIDevice: win32more.System.SideShow.ISideShowCapabilities_head) -> win32more.Foundation.HRESULT: ...
class ISideShowKeyCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('045473bc-a37b-4957-b1-44-68-10-54-11-ed-8e')
    @commethod(3)
    def Add(Key: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Clear() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetAt(dwIndex: UInt32, pKey: POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCount(pcElems: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAt(dwIndex: UInt32) -> win32more.Foundation.HRESULT: ...
class ISideShowNotification(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('03c93300-8ab2-41c5-9b-79-46-12-7a-30-e1-48')
    @commethod(3)
    def get_NotificationId(out_pNotificationId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_NotificationId(in_notificationId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_Title(out_ppwszTitle: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_Title(in_pwszTitle: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_Message(out_ppwszMessage: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Message(in_pwszMessage: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Image(out_phIcon: POINTER(win32more.UI.WindowsAndMessaging.HICON)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Image(in_hIcon: win32more.UI.WindowsAndMessaging.HICON) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_ExpirationTime(out_pTime: POINTER(win32more.Foundation.SYSTEMTIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_ExpirationTime(in_pTime: POINTER(win32more.Foundation.SYSTEMTIME_head)) -> win32more.Foundation.HRESULT: ...
class ISideShowNotificationManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('63cea909-f2b9-4302-b5-e1-c6-8e-6d-9a-b8-33')
    @commethod(3)
    def Show(in_pINotification: win32more.System.SideShow.ISideShowNotification_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Revoke(in_notificationId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RevokeAll() -> win32more.Foundation.HRESULT: ...
class ISideShowPropVariantCollection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2ea7a549-7bff-4aae-ba-b0-22-d4-31-11-de-49')
    @commethod(3)
    def Add(pValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Clear() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetAt(dwIndex: UInt32, pValue: POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCount(pcElems: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAt(dwIndex: UInt32) -> win32more.Foundation.HRESULT: ...
class ISideShowSession(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e22331ee-9e7d-4922-9f-c2-ab-7a-a4-1c-e4-91')
    @commethod(3)
    def RegisterContent(in_applicationId: POINTER(Guid), in_endpointId: POINTER(Guid), out_ppIContent: POINTER(win32more.System.SideShow.ISideShowContentManager_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterNotifications(in_applicationId: POINTER(Guid), out_ppINotification: POINTER(win32more.System.SideShow.ISideShowNotificationManager_head)) -> win32more.Foundation.HRESULT: ...
class NEW_EVENT_DATA_AVAILABLE(Structure):
    cbNewEventDataAvailable: UInt32
    dwVersion: UInt32
    _pack_ = 1
SCF_BUTTON_IDS = Int32
SCF_BUTTON_MENU: SCF_BUTTON_IDS = 1
SCF_BUTTON_SELECT: SCF_BUTTON_IDS = 2
SCF_BUTTON_UP: SCF_BUTTON_IDS = 3
SCF_BUTTON_DOWN: SCF_BUTTON_IDS = 4
SCF_BUTTON_LEFT: SCF_BUTTON_IDS = 5
SCF_BUTTON_RIGHT: SCF_BUTTON_IDS = 6
SCF_BUTTON_PLAY: SCF_BUTTON_IDS = 7
SCF_BUTTON_PAUSE: SCF_BUTTON_IDS = 8
SCF_BUTTON_FASTFORWARD: SCF_BUTTON_IDS = 9
SCF_BUTTON_REWIND: SCF_BUTTON_IDS = 10
SCF_BUTTON_STOP: SCF_BUTTON_IDS = 11
SCF_BUTTON_BACK: SCF_BUTTON_IDS = 65280
class SCF_CONTEXTMENU_EVENT(Structure):
    PreviousPage: UInt32
    TargetPage: UInt32
    PreviousItemId: UInt32
    MenuPage: UInt32
    MenuItemId: UInt32
class SCF_EVENT_HEADER(Structure):
    PreviousPage: UInt32
    TargetPage: UInt32
SCF_EVENT_IDS = Int32
SCF_EVENT_NAVIGATION: SCF_EVENT_IDS = 1
SCF_EVENT_MENUACTION: SCF_EVENT_IDS = 2
SCF_EVENT_CONTEXTMENU: SCF_EVENT_IDS = 3
class SCF_MENUACTION_EVENT(Structure):
    PreviousPage: UInt32
    TargetPage: UInt32
    Button: UInt32
    ItemId: UInt32
class SCF_NAVIGATION_EVENT(Structure):
    PreviousPage: UInt32
    TargetPage: UInt32
    Button: UInt32
SIDESHOW_COLOR_TYPE = Int32
SIDESHOW_COLOR_TYPE_COLOR: SIDESHOW_COLOR_TYPE = 0
SIDESHOW_COLOR_TYPE_GREYSCALE: SIDESHOW_COLOR_TYPE = 1
SIDESHOW_COLOR_TYPE_BLACK_AND_WHITE: SIDESHOW_COLOR_TYPE = 2
SIDESHOW_SCREEN_TYPE = Int32
SIDESHOW_SCREEN_TYPE_BITMAP: SIDESHOW_SCREEN_TYPE = 0
SIDESHOW_SCREEN_TYPE_TEXT: SIDESHOW_SCREEN_TYPE = 1
SideShowKeyCollection = Guid('dfbbdbf8-18de-49b8-83-dc-eb-c7-27-c6-2d-94')
SideShowNotification = Guid('0ce3e86f-d5cd-4525-a7-66-1a-ba-b1-a7-52-f5')
SideShowPropVariantCollection = Guid('e640f415-539e-4923-96-cd-5f-09-3b-c2-50-cd')
SideShowSession = Guid('e20543b9-f785-4ea2-98-1e-c4-ff-a7-6b-bc-7c')
make_head(_module, 'SIDESHOW_CAPABILITY_DEVICE_ID')
make_head(_module, 'SIDESHOW_CAPABILITY_SCREEN_TYPE')
make_head(_module, 'SIDESHOW_CAPABILITY_SCREEN_WIDTH')
make_head(_module, 'SIDESHOW_CAPABILITY_SCREEN_HEIGHT')
make_head(_module, 'SIDESHOW_CAPABILITY_COLOR_DEPTH')
make_head(_module, 'SIDESHOW_CAPABILITY_COLOR_TYPE')
make_head(_module, 'SIDESHOW_CAPABILITY_DATA_CACHE')
make_head(_module, 'SIDESHOW_CAPABILITY_SUPPORTED_LANGUAGES')
make_head(_module, 'SIDESHOW_CAPABILITY_CURRENT_LANGUAGE')
make_head(_module, 'SIDESHOW_CAPABILITY_SUPPORTED_THEMES')
make_head(_module, 'SIDESHOW_CAPABILITY_SUPPORTED_IMAGE_FORMATS')
make_head(_module, 'SIDESHOW_CAPABILITY_CLIENT_AREA_WIDTH')
make_head(_module, 'SIDESHOW_CAPABILITY_CLIENT_AREA_HEIGHT')
make_head(_module, 'APPLICATION_EVENT_DATA')
make_head(_module, 'CONTENT_MISSING_EVENT_DATA')
make_head(_module, 'DEVICE_USER_CHANGE_EVENT_DATA')
make_head(_module, 'EVENT_DATA_HEADER')
make_head(_module, 'ISideShowBulkCapabilities')
make_head(_module, 'ISideShowCapabilities')
make_head(_module, 'ISideShowCapabilitiesCollection')
make_head(_module, 'ISideShowContent')
make_head(_module, 'ISideShowContentManager')
make_head(_module, 'ISideShowEvents')
make_head(_module, 'ISideShowKeyCollection')
make_head(_module, 'ISideShowNotification')
make_head(_module, 'ISideShowNotificationManager')
make_head(_module, 'ISideShowPropVariantCollection')
make_head(_module, 'ISideShowSession')
make_head(_module, 'NEW_EVENT_DATA_AVAILABLE')
make_head(_module, 'SCF_CONTEXTMENU_EVENT')
make_head(_module, 'SCF_EVENT_HEADER')
make_head(_module, 'SCF_MENUACTION_EVENT')
make_head(_module, 'SCF_NAVIGATION_EVENT')
__all__ = [
    "APPLICATION_EVENT_DATA",
    "CONTENT_ID_GLANCE",
    "CONTENT_ID_HOME",
    "CONTENT_MISSING_EVENT_DATA",
    "DEVICE_USER_CHANGE_EVENT_DATA",
    "EVENT_DATA_HEADER",
    "GUID_DEVINTERFACE_SIDESHOW",
    "ISideShowBulkCapabilities",
    "ISideShowCapabilities",
    "ISideShowCapabilitiesCollection",
    "ISideShowContent",
    "ISideShowContentManager",
    "ISideShowEvents",
    "ISideShowKeyCollection",
    "ISideShowNotification",
    "ISideShowNotificationManager",
    "ISideShowPropVariantCollection",
    "ISideShowSession",
    "NEW_EVENT_DATA_AVAILABLE",
    "SCF_BUTTON_BACK",
    "SCF_BUTTON_DOWN",
    "SCF_BUTTON_FASTFORWARD",
    "SCF_BUTTON_IDS",
    "SCF_BUTTON_LEFT",
    "SCF_BUTTON_MENU",
    "SCF_BUTTON_PAUSE",
    "SCF_BUTTON_PLAY",
    "SCF_BUTTON_REWIND",
    "SCF_BUTTON_RIGHT",
    "SCF_BUTTON_SELECT",
    "SCF_BUTTON_STOP",
    "SCF_BUTTON_UP",
    "SCF_CONTEXTMENU_EVENT",
    "SCF_EVENT_CONTEXTMENU",
    "SCF_EVENT_HEADER",
    "SCF_EVENT_IDS",
    "SCF_EVENT_MENUACTION",
    "SCF_EVENT_NAVIGATION",
    "SCF_MENUACTION_EVENT",
    "SCF_NAVIGATION_EVENT",
    "SIDESHOW_APPLICATION_EVENT",
    "SIDESHOW_CAPABILITY_CLIENT_AREA_HEIGHT",
    "SIDESHOW_CAPABILITY_CLIENT_AREA_WIDTH",
    "SIDESHOW_CAPABILITY_COLOR_DEPTH",
    "SIDESHOW_CAPABILITY_COLOR_TYPE",
    "SIDESHOW_CAPABILITY_CURRENT_LANGUAGE",
    "SIDESHOW_CAPABILITY_DATA_CACHE",
    "SIDESHOW_CAPABILITY_DEVICE_ID",
    "SIDESHOW_CAPABILITY_DEVICE_PROPERTIES",
    "SIDESHOW_CAPABILITY_SCREEN_HEIGHT",
    "SIDESHOW_CAPABILITY_SCREEN_TYPE",
    "SIDESHOW_CAPABILITY_SCREEN_WIDTH",
    "SIDESHOW_CAPABILITY_SUPPORTED_IMAGE_FORMATS",
    "SIDESHOW_CAPABILITY_SUPPORTED_LANGUAGES",
    "SIDESHOW_CAPABILITY_SUPPORTED_THEMES",
    "SIDESHOW_COLOR_TYPE",
    "SIDESHOW_COLOR_TYPE_BLACK_AND_WHITE",
    "SIDESHOW_COLOR_TYPE_COLOR",
    "SIDESHOW_COLOR_TYPE_GREYSCALE",
    "SIDESHOW_CONTENT_MISSING_EVENT",
    "SIDESHOW_ENDPOINT_ICAL",
    "SIDESHOW_ENDPOINT_SIMPLE_CONTENT_FORMAT",
    "SIDESHOW_EVENTID_APPLICATION_ENTER",
    "SIDESHOW_EVENTID_APPLICATION_EXIT",
    "SIDESHOW_NEW_EVENT_DATA_AVAILABLE",
    "SIDESHOW_SCREEN_TYPE",
    "SIDESHOW_SCREEN_TYPE_BITMAP",
    "SIDESHOW_SCREEN_TYPE_TEXT",
    "SIDESHOW_USER_CHANGE_REQUEST_EVENT",
    "SideShowKeyCollection",
    "SideShowNotification",
    "SideShowPropVariantCollection",
    "SideShowSession",
    "VERSION_1_WINDOWS_7",
]
