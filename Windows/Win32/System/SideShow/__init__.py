from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.System.SideShow
import Windows.Win32.UI.Shell.PropertiesSystem
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
class APPLICATION_EVENT_DATA(EasyCastStructure):
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
def SIDESHOW_CAPABILITY_DEVICE_ID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=1)
def SIDESHOW_CAPABILITY_SCREEN_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=2)
def SIDESHOW_CAPABILITY_SCREEN_WIDTH():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=3)
def SIDESHOW_CAPABILITY_SCREEN_HEIGHT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=4)
def SIDESHOW_CAPABILITY_COLOR_DEPTH():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=5)
def SIDESHOW_CAPABILITY_COLOR_TYPE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=6)
def SIDESHOW_CAPABILITY_DATA_CACHE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=7)
def SIDESHOW_CAPABILITY_SUPPORTED_LANGUAGES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=8)
def SIDESHOW_CAPABILITY_CURRENT_LANGUAGE():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=9)
def SIDESHOW_CAPABILITY_SUPPORTED_THEMES():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=10)
def SIDESHOW_CAPABILITY_SUPPORTED_IMAGE_FORMATS():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=14)
def SIDESHOW_CAPABILITY_CLIENT_AREA_WIDTH():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=15)
def SIDESHOW_CAPABILITY_CLIENT_AREA_HEIGHT():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('{8abc88a8-857b-4ad7-a35a-b5942f492b99}'), pid=16)
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
class CONTENT_MISSING_EVENT_DATA(EasyCastStructure):
    cbContentMissingEventData: UInt32
    ApplicationId: Guid
    EndpointId: Guid
    ContentId: UInt32
    _pack_ = 1
class DEVICE_USER_CHANGE_EVENT_DATA(EasyCastStructure):
    cbDeviceUserChangeEventData: UInt32
    wszUser: Char
    _pack_ = 1
class EVENT_DATA_HEADER(EasyCastStructure):
    cbEventDataHeader: UInt32
    guidEventType: Guid
    dwVersion: UInt32
    cbEventDataSid: UInt32
    _pack_ = 1
class ISideShowBulkCapabilities(ComPtr):
    extends: Windows.Win32.System.SideShow.ISideShowCapabilities
    _iid_ = Guid('{3a2b7fbc-3ad5-48bd-bbf1-0e6cfbd10807}')
    @commethod(4)
    def GetCapabilities(self, in_keyCollection: Windows.Win32.System.SideShow.ISideShowKeyCollection_head, inout_pValues: POINTER(Windows.Win32.System.SideShow.ISideShowPropVariantCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISideShowCapabilities(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{535e1379-c09e-4a54-a511-597bab3a72b8}')
    @commethod(3)
    def GetCapability(self, in_keyCapability: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), inout_pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISideShowCapabilitiesCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{50305597-5e0d-4ff7-b3af-33d0d9bd52dd}')
    @commethod(3)
    def GetCount(self, out_pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, in_dwIndex: UInt32, out_ppCapabilities: POINTER(Windows.Win32.System.SideShow.ISideShowCapabilities_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISideShowContent(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c18552ed-74ff-4fec-be07-4cfed29d4887}')
    @commethod(3)
    def GetContent(self, in_pICapabilities: Windows.Win32.System.SideShow.ISideShowCapabilities_head, out_pdwSize: POINTER(UInt32), out_ppbData: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ContentId(self, out_pcontentId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_DifferentiateContent(self, out_pfDifferentiateContent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ISideShowContentManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a5d5b66b-eef9-41db-8d7e-e17c33ab10b0}')
    @commethod(3)
    def Add(self, in_pIContent: Windows.Win32.System.SideShow.ISideShowContent_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(self, in_contentId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAll(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetEventSink(self, in_pIEvents: Windows.Win32.System.SideShow.ISideShowEvents_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDeviceCapabilities(self, out_ppCollection: POINTER(Windows.Win32.System.SideShow.ISideShowCapabilitiesCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISideShowEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{61feca4c-deb4-4a7e-8d75-51f1132d615b}')
    @commethod(3)
    def ContentMissing(self, in_contentId: UInt32, out_ppIContent: POINTER(Windows.Win32.System.SideShow.ISideShowContent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ApplicationEvent(self, in_pICapabilities: Windows.Win32.System.SideShow.ISideShowCapabilities_head, in_dwEventId: UInt32, in_dwEventSize: UInt32, in_pbEventData: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeviceAdded(self, in_pIDevice: Windows.Win32.System.SideShow.ISideShowCapabilities_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeviceRemoved(self, in_pIDevice: Windows.Win32.System.SideShow.ISideShowCapabilities_head) -> Windows.Win32.Foundation.HRESULT: ...
class ISideShowKeyCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{045473bc-a37b-4957-b144-68105411ed8e}')
    @commethod(3)
    def Add(self, Key: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAt(self, dwIndex: UInt32, pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCount(self, pcElems: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAt(self, dwIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISideShowNotification(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{03c93300-8ab2-41c5-9b79-46127a30e148}')
    @commethod(3)
    def get_NotificationId(self, out_pNotificationId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_NotificationId(self, in_notificationId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Title(self, out_ppwszTitle: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_Title(self, in_pwszTitle: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Message(self, out_ppwszMessage: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Message(self, in_pwszMessage: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Image(self, out_phIcon: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Image(self, in_hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ExpirationTime(self, out_pTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_ExpirationTime(self, in_pTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISideShowNotificationManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{63cea909-f2b9-4302-b5e1-c68e6d9ab833}')
    @commethod(3)
    def Show(self, in_pINotification: Windows.Win32.System.SideShow.ISideShowNotification_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Revoke(self, in_notificationId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RevokeAll(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISideShowPropVariantCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2ea7a549-7bff-4aae-bab0-22d43111de49}')
    @commethod(3)
    def Add(self, pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAt(self, dwIndex: UInt32, pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCount(self, pcElems: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAt(self, dwIndex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISideShowSession(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e22331ee-9e7d-4922-9fc2-ab7aa41ce491}')
    @commethod(3)
    def RegisterContent(self, in_applicationId: POINTER(Guid), in_endpointId: POINTER(Guid), out_ppIContent: POINTER(Windows.Win32.System.SideShow.ISideShowContentManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterNotifications(self, in_applicationId: POINTER(Guid), out_ppINotification: POINTER(Windows.Win32.System.SideShow.ISideShowNotificationManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
class NEW_EVENT_DATA_AVAILABLE(EasyCastStructure):
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
class SCF_CONTEXTMENU_EVENT(EasyCastStructure):
    PreviousPage: UInt32
    TargetPage: UInt32
    PreviousItemId: UInt32
    MenuPage: UInt32
    MenuItemId: UInt32
class SCF_EVENT_HEADER(EasyCastStructure):
    PreviousPage: UInt32
    TargetPage: UInt32
SCF_EVENT_IDS = Int32
SCF_EVENT_NAVIGATION: SCF_EVENT_IDS = 1
SCF_EVENT_MENUACTION: SCF_EVENT_IDS = 2
SCF_EVENT_CONTEXTMENU: SCF_EVENT_IDS = 3
class SCF_MENUACTION_EVENT(EasyCastStructure):
    PreviousPage: UInt32
    TargetPage: UInt32
    Button: UInt32
    ItemId: UInt32
class SCF_NAVIGATION_EVENT(EasyCastStructure):
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
SideShowKeyCollection = Guid('{dfbbdbf8-18de-49b8-83dc-ebc727c62d94}')
SideShowNotification = Guid('{0ce3e86f-d5cd-4525-a766-1abab1a752f5}')
SideShowPropVariantCollection = Guid('{e640f415-539e-4923-96cd-5f093bc250cd}')
SideShowSession = Guid('{e20543b9-f785-4ea2-981e-c4ffa76bbc7c}')
make_head(_module, 'APPLICATION_EVENT_DATA')
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
