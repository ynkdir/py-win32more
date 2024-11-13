from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.SideShow
import win32more.Windows.Win32.UI.WindowsAndMessaging
class APPLICATION_EVENT_DATA(Structure):
    cbApplicationEventData: UInt32
    ApplicationId: Guid
    EndpointId: Guid
    dwEventId: UInt32
    cbEventData: UInt32
    bEventData: Byte * 1
    _pack_ = 1
SIDESHOW_ENDPOINT_SIMPLE_CONTENT_FORMAT: Guid = Guid('{a9a5353f-2d4b-47ce-93ee-759f3a7dda4f}')
SIDESHOW_ENDPOINT_ICAL: Guid = Guid('{4dff36b5-9dde-4f76-9a2a-96435047063d}')
SIDESHOW_CAPABILITY_DEVICE_PROPERTIES: Guid = Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}')
SIDESHOW_CAPABILITY_DEVICE_ID: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=1)
SIDESHOW_CAPABILITY_SCREEN_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=2)
SIDESHOW_CAPABILITY_SCREEN_WIDTH: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=3)
SIDESHOW_CAPABILITY_SCREEN_HEIGHT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=4)
SIDESHOW_CAPABILITY_COLOR_DEPTH: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=5)
SIDESHOW_CAPABILITY_COLOR_TYPE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=6)
SIDESHOW_CAPABILITY_DATA_CACHE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=7)
SIDESHOW_CAPABILITY_SUPPORTED_LANGUAGES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=8)
SIDESHOW_CAPABILITY_CURRENT_LANGUAGE: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=9)
SIDESHOW_CAPABILITY_SUPPORTED_THEMES: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=10)
SIDESHOW_CAPABILITY_SUPPORTED_IMAGE_FORMATS: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=14)
SIDESHOW_CAPABILITY_CLIENT_AREA_WIDTH: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=15)
SIDESHOW_CAPABILITY_CLIENT_AREA_HEIGHT: win32more.Windows.Win32.Foundation.PROPERTYKEY = ConstantLazyLoader(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=16)
GUID_DEVINTERFACE_SIDESHOW: Guid = Guid('{152e5811-feb9-4b00-90f4-d32947ae1681}')
SIDESHOW_CONTENT_MISSING_EVENT: Guid = Guid('{5007fba8-d313-439f-bea2-a50201d3e9a8}')
SIDESHOW_APPLICATION_EVENT: Guid = Guid('{4cb572fa-1d3b-49b3-a17a-2e6bff052854}')
SIDESHOW_USER_CHANGE_REQUEST_EVENT: Guid = Guid('{5009673c-3f7d-4c7e-9971-eaa2e91f1575}')
SIDESHOW_NEW_EVENT_DATA_AVAILABLE: Guid = Guid('{57813854-2fc1-411c-a59f-f24927608804}')
CONTENT_ID_GLANCE: UInt32 = 0
SIDESHOW_EVENTID_APPLICATION_ENTER: UInt32 = 4294901760
SIDESHOW_EVENTID_APPLICATION_EXIT: UInt32 = 4294901761
CONTENT_ID_HOME: UInt32 = 1
VERSION_1_WINDOWS_7: UInt32 = 0
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
class ISideShowBulkCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.SideShow.ISideShowCapabilities
    _iid_ = Guid('{3a2b7fbc-3ad5-48bd-bbf1-0e6cfbd10807}')
    @commethod(4)
    def GetCapabilities(self, in_keyCollection: win32more.Windows.Win32.System.SideShow.ISideShowKeyCollection, inout_pValues: POINTER(win32more.Windows.Win32.System.SideShow.ISideShowPropVariantCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISideShowCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{535e1379-c09e-4a54-a511-597bab3a72b8}')
    @commethod(3)
    def GetCapability(self, in_keyCapability: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), inout_pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISideShowCapabilitiesCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{50305597-5e0d-4ff7-b3af-33d0d9bd52dd}')
    @commethod(3)
    def GetCount(self, out_pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, in_dwIndex: UInt32, out_ppCapabilities: POINTER(win32more.Windows.Win32.System.SideShow.ISideShowCapabilities)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISideShowContent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c18552ed-74ff-4fec-be07-4cfed29d4887}')
    @commethod(3)
    def GetContent(self, in_pICapabilities: win32more.Windows.Win32.System.SideShow.ISideShowCapabilities, out_pdwSize: POINTER(UInt32), out_ppbData: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ContentId(self, out_pcontentId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_DifferentiateContent(self, out_pfDifferentiateContent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISideShowContentManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a5d5b66b-eef9-41db-8d7e-e17c33ab10b0}')
    @commethod(3)
    def Add(self, in_pIContent: win32more.Windows.Win32.System.SideShow.ISideShowContent) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(self, in_contentId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetEventSink(self, in_pIEvents: win32more.Windows.Win32.System.SideShow.ISideShowEvents) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDeviceCapabilities(self, out_ppCollection: POINTER(win32more.Windows.Win32.System.SideShow.ISideShowCapabilitiesCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISideShowEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{61feca4c-deb4-4a7e-8d75-51f1132d615b}')
    @commethod(3)
    def ContentMissing(self, in_contentId: UInt32, out_ppIContent: POINTER(win32more.Windows.Win32.System.SideShow.ISideShowContent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ApplicationEvent(self, in_pICapabilities: win32more.Windows.Win32.System.SideShow.ISideShowCapabilities, in_dwEventId: UInt32, in_dwEventSize: UInt32, in_pbEventData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeviceAdded(self, in_pIDevice: win32more.Windows.Win32.System.SideShow.ISideShowCapabilities) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeviceRemoved(self, in_pIDevice: win32more.Windows.Win32.System.SideShow.ISideShowCapabilities) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISideShowKeyCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{045473bc-a37b-4957-b144-68105411ed8e}')
    @commethod(3)
    def Add(self, Key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAt(self, dwIndex: UInt32, pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCount(self, pcElems: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAt(self, dwIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISideShowNotification(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{03c93300-8ab2-41c5-9b79-46127a30e148}')
    @commethod(3)
    def get_NotificationId(self, out_pNotificationId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_NotificationId(self, in_notificationId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Title(self, out_ppwszTitle: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_Title(self, in_pwszTitle: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Message(self, out_ppwszMessage: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Message(self, in_pwszMessage: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Image(self, out_phIcon: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Image(self, in_hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ExpirationTime(self, out_pTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ExpirationTime(self, in_pTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISideShowNotificationManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{63cea909-f2b9-4302-b5e1-c68e6d9ab833}')
    @commethod(3)
    def Show(self, in_pINotification: win32more.Windows.Win32.System.SideShow.ISideShowNotification) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Revoke(self, in_notificationId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RevokeAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISideShowPropVariantCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2ea7a549-7bff-4aae-bab0-22d43111de49}')
    @commethod(3)
    def Add(self, pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAt(self, dwIndex: UInt32, pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCount(self, pcElems: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAt(self, dwIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISideShowSession(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e22331ee-9e7d-4922-9fc2-ab7aa41ce491}')
    @commethod(3)
    def RegisterContent(self, in_applicationId: POINTER(Guid), in_endpointId: POINTER(Guid), out_ppIContent: POINTER(win32more.Windows.Win32.System.SideShow.ISideShowContentManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterNotifications(self, in_applicationId: POINTER(Guid), out_ppINotification: POINTER(win32more.Windows.Win32.System.SideShow.ISideShowNotificationManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class NEW_EVENT_DATA_AVAILABLE(Structure):
    cbNewEventDataAvailable: UInt32
    dwVersion: UInt32
    _pack_ = 1
SCF_BUTTON_IDS = Int32
SCF_BUTTON_MENU: win32more.Windows.Win32.System.SideShow.SCF_BUTTON_IDS = 1
SCF_BUTTON_SELECT: win32more.Windows.Win32.System.SideShow.SCF_BUTTON_IDS = 2
SCF_BUTTON_UP: win32more.Windows.Win32.System.SideShow.SCF_BUTTON_IDS = 3
SCF_BUTTON_DOWN: win32more.Windows.Win32.System.SideShow.SCF_BUTTON_IDS = 4
SCF_BUTTON_LEFT: win32more.Windows.Win32.System.SideShow.SCF_BUTTON_IDS = 5
SCF_BUTTON_RIGHT: win32more.Windows.Win32.System.SideShow.SCF_BUTTON_IDS = 6
SCF_BUTTON_PLAY: win32more.Windows.Win32.System.SideShow.SCF_BUTTON_IDS = 7
SCF_BUTTON_PAUSE: win32more.Windows.Win32.System.SideShow.SCF_BUTTON_IDS = 8
SCF_BUTTON_FASTFORWARD: win32more.Windows.Win32.System.SideShow.SCF_BUTTON_IDS = 9
SCF_BUTTON_REWIND: win32more.Windows.Win32.System.SideShow.SCF_BUTTON_IDS = 10
SCF_BUTTON_STOP: win32more.Windows.Win32.System.SideShow.SCF_BUTTON_IDS = 11
SCF_BUTTON_BACK: win32more.Windows.Win32.System.SideShow.SCF_BUTTON_IDS = 65280
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
SCF_EVENT_NAVIGATION: win32more.Windows.Win32.System.SideShow.SCF_EVENT_IDS = 1
SCF_EVENT_MENUACTION: win32more.Windows.Win32.System.SideShow.SCF_EVENT_IDS = 2
SCF_EVENT_CONTEXTMENU: win32more.Windows.Win32.System.SideShow.SCF_EVENT_IDS = 3
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
SIDESHOW_COLOR_TYPE_COLOR: win32more.Windows.Win32.System.SideShow.SIDESHOW_COLOR_TYPE = 0
SIDESHOW_COLOR_TYPE_GREYSCALE: win32more.Windows.Win32.System.SideShow.SIDESHOW_COLOR_TYPE = 1
SIDESHOW_COLOR_TYPE_BLACK_AND_WHITE: win32more.Windows.Win32.System.SideShow.SIDESHOW_COLOR_TYPE = 2
SIDESHOW_SCREEN_TYPE = Int32
SIDESHOW_SCREEN_TYPE_BITMAP: win32more.Windows.Win32.System.SideShow.SIDESHOW_SCREEN_TYPE = 0
SIDESHOW_SCREEN_TYPE_TEXT: win32more.Windows.Win32.System.SideShow.SIDESHOW_SCREEN_TYPE = 1
SideShowKeyCollection = Guid('{dfbbdbf8-18de-49b8-83dc-ebc727c62d94}')
SideShowNotification = Guid('{0ce3e86f-d5cd-4525-a766-1abab1a752f5}')
SideShowPropVariantCollection = Guid('{e640f415-539e-4923-96cd-5f093bc250cd}')
SideShowSession = Guid('{e20543b9-f785-4ea2-981e-c4ffa76bbc7c}')


make_ready(__name__)
