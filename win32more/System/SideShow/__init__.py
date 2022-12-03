from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
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
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_SIDESHOW_ENDPOINT_SIMPLE_CONTENT_FORMAT():
    return Guid('a9a5353f-2d4b-47ce-93-ee-75-9f-3a-7d-da-4f')
def _define_SIDESHOW_ENDPOINT_ICAL():
    return Guid('4dff36b5-9dde-4f76-9a-2a-96-43-50-47-06-3d')
def _define_SIDESHOW_CAPABILITY_DEVICE_PROPERTIES():
    return Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99')
def _define_SIDESHOW_CAPABILITY_DEVICE_ID():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=1)
def _define_SIDESHOW_CAPABILITY_SCREEN_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=2)
def _define_SIDESHOW_CAPABILITY_SCREEN_WIDTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=3)
def _define_SIDESHOW_CAPABILITY_SCREEN_HEIGHT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=4)
def _define_SIDESHOW_CAPABILITY_COLOR_DEPTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=5)
def _define_SIDESHOW_CAPABILITY_COLOR_TYPE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=6)
def _define_SIDESHOW_CAPABILITY_DATA_CACHE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=7)
def _define_SIDESHOW_CAPABILITY_SUPPORTED_LANGUAGES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=8)
def _define_SIDESHOW_CAPABILITY_CURRENT_LANGUAGE():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=9)
def _define_SIDESHOW_CAPABILITY_SUPPORTED_THEMES():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=10)
def _define_SIDESHOW_CAPABILITY_SUPPORTED_IMAGE_FORMATS():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=14)
def _define_SIDESHOW_CAPABILITY_CLIENT_AREA_WIDTH():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=15)
def _define_SIDESHOW_CAPABILITY_CLIENT_AREA_HEIGHT():
    return win32more.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('8abc88a8-857b-4ad7-a3-5a-b5-94-2f-49-2b-99'), pid=16)
def _define_GUID_DEVINTERFACE_SIDESHOW():
    return Guid('152e5811-feb9-4b00-90-f4-d3-29-47-ae-16-81')
def _define_SIDESHOW_CONTENT_MISSING_EVENT():
    return Guid('5007fba8-d313-439f-be-a2-a5-02-01-d3-e9-a8')
def _define_SIDESHOW_APPLICATION_EVENT():
    return Guid('4cb572fa-1d3b-49b3-a1-7a-2e-6b-ff-05-28-54')
def _define_SIDESHOW_USER_CHANGE_REQUEST_EVENT():
    return Guid('5009673c-3f7d-4c7e-99-71-ea-a2-e9-1f-15-75')
def _define_SIDESHOW_NEW_EVENT_DATA_AVAILABLE():
    return Guid('57813854-2fc1-411c-a5-9f-f2-49-27-60-88-04')
CONTENT_ID_GLANCE = 0
SIDESHOW_EVENTID_APPLICATION_ENTER = 4294901760
SIDESHOW_EVENTID_APPLICATION_EXIT = 4294901761
CONTENT_ID_HOME = 1
VERSION_1_WINDOWS_7 = 0
def _define_APPLICATION_EVENT_DATA_head():
    class APPLICATION_EVENT_DATA(Structure):
        pass
    return APPLICATION_EVENT_DATA
def _define_APPLICATION_EVENT_DATA():
    APPLICATION_EVENT_DATA = win32more.System.SideShow.APPLICATION_EVENT_DATA_head
    APPLICATION_EVENT_DATA._pack_ = 1
    APPLICATION_EVENT_DATA._fields_ = [
        ('cbApplicationEventData', UInt32),
        ('ApplicationId', Guid),
        ('EndpointId', Guid),
        ('dwEventId', UInt32),
        ('cbEventData', UInt32),
        ('bEventData', Byte * 1),
    ]
    return APPLICATION_EVENT_DATA
def _define_CONTENT_MISSING_EVENT_DATA_head():
    class CONTENT_MISSING_EVENT_DATA(Structure):
        pass
    return CONTENT_MISSING_EVENT_DATA
def _define_CONTENT_MISSING_EVENT_DATA():
    CONTENT_MISSING_EVENT_DATA = win32more.System.SideShow.CONTENT_MISSING_EVENT_DATA_head
    CONTENT_MISSING_EVENT_DATA._pack_ = 1
    CONTENT_MISSING_EVENT_DATA._fields_ = [
        ('cbContentMissingEventData', UInt32),
        ('ApplicationId', Guid),
        ('EndpointId', Guid),
        ('ContentId', UInt32),
    ]
    return CONTENT_MISSING_EVENT_DATA
def _define_DEVICE_USER_CHANGE_EVENT_DATA_head():
    class DEVICE_USER_CHANGE_EVENT_DATA(Structure):
        pass
    return DEVICE_USER_CHANGE_EVENT_DATA
def _define_DEVICE_USER_CHANGE_EVENT_DATA():
    DEVICE_USER_CHANGE_EVENT_DATA = win32more.System.SideShow.DEVICE_USER_CHANGE_EVENT_DATA_head
    DEVICE_USER_CHANGE_EVENT_DATA._pack_ = 1
    DEVICE_USER_CHANGE_EVENT_DATA._fields_ = [
        ('cbDeviceUserChangeEventData', UInt32),
        ('wszUser', Char),
    ]
    return DEVICE_USER_CHANGE_EVENT_DATA
def _define_EVENT_DATA_HEADER_head():
    class EVENT_DATA_HEADER(Structure):
        pass
    return EVENT_DATA_HEADER
def _define_EVENT_DATA_HEADER():
    EVENT_DATA_HEADER = win32more.System.SideShow.EVENT_DATA_HEADER_head
    EVENT_DATA_HEADER._pack_ = 1
    EVENT_DATA_HEADER._fields_ = [
        ('cbEventDataHeader', UInt32),
        ('guidEventType', Guid),
        ('dwVersion', UInt32),
        ('cbEventDataSid', UInt32),
    ]
    return EVENT_DATA_HEADER
def _define_ISideShowBulkCapabilities_head():
    class ISideShowBulkCapabilities(win32more.System.SideShow.ISideShowCapabilities_head):
        Guid = Guid('3a2b7fbc-3ad5-48bd-bb-f1-0e-6c-fb-d1-08-07')
    return ISideShowBulkCapabilities
def _define_ISideShowBulkCapabilities():
    ISideShowBulkCapabilities = win32more.System.SideShow.ISideShowBulkCapabilities_head
    ISideShowBulkCapabilities.GetCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SideShow.ISideShowKeyCollection_head,POINTER(win32more.System.SideShow.ISideShowPropVariantCollection_head))(4, 'GetCapabilities', ((1, 'in_keyCollection'),(1, 'inout_pValues'),)))
    win32more.System.SideShow.ISideShowCapabilities
    return ISideShowBulkCapabilities
def _define_ISideShowCapabilities_head():
    class ISideShowCapabilities(win32more.System.Com.IUnknown_head):
        Guid = Guid('535e1379-c09e-4a54-a5-11-59-7b-ab-3a-72-b8')
    return ISideShowCapabilities
def _define_ISideShowCapabilities():
    ISideShowCapabilities = win32more.System.SideShow.ISideShowCapabilities_head
    ISideShowCapabilities.GetCapability = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(3, 'GetCapability', ((1, 'in_keyCapability'),(1, 'inout_pValue'),)))
    win32more.System.Com.IUnknown
    return ISideShowCapabilities
def _define_ISideShowCapabilitiesCollection_head():
    class ISideShowCapabilitiesCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('50305597-5e0d-4ff7-b3-af-33-d0-d9-bd-52-dd')
    return ISideShowCapabilitiesCollection
def _define_ISideShowCapabilitiesCollection():
    ISideShowCapabilitiesCollection = win32more.System.SideShow.ISideShowCapabilitiesCollection_head
    ISideShowCapabilitiesCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'out_pdwCount'),)))
    ISideShowCapabilitiesCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.SideShow.ISideShowCapabilities_head))(4, 'GetAt', ((1, 'in_dwIndex'),(1, 'out_ppCapabilities'),)))
    win32more.System.Com.IUnknown
    return ISideShowCapabilitiesCollection
def _define_ISideShowContent_head():
    class ISideShowContent(win32more.System.Com.IUnknown_head):
        Guid = Guid('c18552ed-74ff-4fec-be-07-4c-fe-d2-9d-48-87')
    return ISideShowContent
def _define_ISideShowContent():
    ISideShowContent = win32more.System.SideShow.ISideShowContent_head
    ISideShowContent.GetContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SideShow.ISideShowCapabilities_head,POINTER(UInt32),POINTER(c_char_p_no))(3, 'GetContent', ((1, 'in_pICapabilities'),(1, 'out_pdwSize'),(1, 'out_ppbData'),)))
    ISideShowContent.get_ContentId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'get_ContentId', ((1, 'out_pcontentId'),)))
    ISideShowContent.get_DifferentiateContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(5, 'get_DifferentiateContent', ((1, 'out_pfDifferentiateContent'),)))
    win32more.System.Com.IUnknown
    return ISideShowContent
def _define_ISideShowContentManager_head():
    class ISideShowContentManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('a5d5b66b-eef9-41db-8d-7e-e1-7c-33-ab-10-b0')
    return ISideShowContentManager
def _define_ISideShowContentManager():
    ISideShowContentManager = win32more.System.SideShow.ISideShowContentManager_head
    ISideShowContentManager.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SideShow.ISideShowContent_head)(3, 'Add', ((1, 'in_pIContent'),)))
    ISideShowContentManager.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Remove', ((1, 'in_contentId'),)))
    ISideShowContentManager.RemoveAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'RemoveAll', ()))
    ISideShowContentManager.SetEventSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SideShow.ISideShowEvents_head)(6, 'SetEventSink', ((1, 'in_pIEvents'),)))
    ISideShowContentManager.GetDeviceCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.SideShow.ISideShowCapabilitiesCollection_head))(7, 'GetDeviceCapabilities', ((1, 'out_ppCollection'),)))
    win32more.System.Com.IUnknown
    return ISideShowContentManager
def _define_ISideShowEvents_head():
    class ISideShowEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('61feca4c-deb4-4a7e-8d-75-51-f1-13-2d-61-5b')
    return ISideShowEvents
def _define_ISideShowEvents():
    ISideShowEvents = win32more.System.SideShow.ISideShowEvents_head
    ISideShowEvents.ContentMissing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.SideShow.ISideShowContent_head))(3, 'ContentMissing', ((1, 'in_contentId'),(1, 'out_ppIContent'),)))
    ISideShowEvents.ApplicationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SideShow.ISideShowCapabilities_head,UInt32,UInt32,c_char_p_no)(4, 'ApplicationEvent', ((1, 'in_pICapabilities'),(1, 'in_dwEventId'),(1, 'in_dwEventSize'),(1, 'in_pbEventData'),)))
    ISideShowEvents.DeviceAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SideShow.ISideShowCapabilities_head)(5, 'DeviceAdded', ((1, 'in_pIDevice'),)))
    ISideShowEvents.DeviceRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SideShow.ISideShowCapabilities_head)(6, 'DeviceRemoved', ((1, 'in_pIDevice'),)))
    win32more.System.Com.IUnknown
    return ISideShowEvents
def _define_ISideShowKeyCollection_head():
    class ISideShowKeyCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('045473bc-a37b-4957-b1-44-68-10-54-11-ed-8e')
    return ISideShowKeyCollection
def _define_ISideShowKeyCollection():
    ISideShowKeyCollection = win32more.System.SideShow.ISideShowKeyCollection_head
    ISideShowKeyCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(3, 'Add', ((1, 'Key'),)))
    ISideShowKeyCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Clear', ()))
    ISideShowKeyCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head))(5, 'GetAt', ((1, 'dwIndex'),(1, 'pKey'),)))
    ISideShowKeyCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(6, 'GetCount', ((1, 'pcElems'),)))
    ISideShowKeyCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'RemoveAt', ((1, 'dwIndex'),)))
    win32more.System.Com.IUnknown
    return ISideShowKeyCollection
def _define_ISideShowNotification_head():
    class ISideShowNotification(win32more.System.Com.IUnknown_head):
        Guid = Guid('03c93300-8ab2-41c5-9b-79-46-12-7a-30-e1-48')
    return ISideShowNotification
def _define_ISideShowNotification():
    ISideShowNotification = win32more.System.SideShow.ISideShowNotification_head
    ISideShowNotification.get_NotificationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'get_NotificationId', ((1, 'out_pNotificationId'),)))
    ISideShowNotification.put_NotificationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'put_NotificationId', ((1, 'in_notificationId'),)))
    ISideShowNotification.get_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(5, 'get_Title', ((1, 'out_ppwszTitle'),)))
    ISideShowNotification.put_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(6, 'put_Title', ((1, 'in_pwszTitle'),)))
    ISideShowNotification.get_Message = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(7, 'get_Message', ((1, 'out_ppwszMessage'),)))
    ISideShowNotification.put_Message = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(8, 'put_Message', ((1, 'in_pwszMessage'),)))
    ISideShowNotification.get_Image = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.HICON))(9, 'get_Image', ((1, 'out_phIcon'),)))
    ISideShowNotification.put_Image = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HICON)(10, 'put_Image', ((1, 'in_hIcon'),)))
    ISideShowNotification.get_ExpirationTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head))(11, 'get_ExpirationTime', ((1, 'out_pTime'),)))
    ISideShowNotification.put_ExpirationTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head))(12, 'put_ExpirationTime', ((1, 'in_pTime'),)))
    win32more.System.Com.IUnknown
    return ISideShowNotification
def _define_ISideShowNotificationManager_head():
    class ISideShowNotificationManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('63cea909-f2b9-4302-b5-e1-c6-8e-6d-9a-b8-33')
    return ISideShowNotificationManager
def _define_ISideShowNotificationManager():
    ISideShowNotificationManager = win32more.System.SideShow.ISideShowNotificationManager_head
    ISideShowNotificationManager.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.SideShow.ISideShowNotification_head)(3, 'Show', ((1, 'in_pINotification'),)))
    ISideShowNotificationManager.Revoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Revoke', ((1, 'in_notificationId'),)))
    ISideShowNotificationManager.RevokeAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'RevokeAll', ()))
    win32more.System.Com.IUnknown
    return ISideShowNotificationManager
def _define_ISideShowPropVariantCollection_head():
    class ISideShowPropVariantCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('2ea7a549-7bff-4aae-ba-b0-22-d4-31-11-de-49')
    return ISideShowPropVariantCollection
def _define_ISideShowPropVariantCollection():
    ISideShowPropVariantCollection = win32more.System.SideShow.ISideShowPropVariantCollection_head
    ISideShowPropVariantCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(3, 'Add', ((1, 'pValue'),)))
    ISideShowPropVariantCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Clear', ()))
    ISideShowPropVariantCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head))(5, 'GetAt', ((1, 'dwIndex'),(1, 'pValue'),)))
    ISideShowPropVariantCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(6, 'GetCount', ((1, 'pcElems'),)))
    ISideShowPropVariantCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'RemoveAt', ((1, 'dwIndex'),)))
    win32more.System.Com.IUnknown
    return ISideShowPropVariantCollection
def _define_ISideShowSession_head():
    class ISideShowSession(win32more.System.Com.IUnknown_head):
        Guid = Guid('e22331ee-9e7d-4922-9f-c2-ab-7a-a4-1c-e4-91')
    return ISideShowSession
def _define_ISideShowSession():
    ISideShowSession = win32more.System.SideShow.ISideShowSession_head
    ISideShowSession.RegisterContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.SideShow.ISideShowContentManager_head))(3, 'RegisterContent', ((1, 'in_applicationId'),(1, 'in_endpointId'),(1, 'out_ppIContent'),)))
    ISideShowSession.RegisterNotifications = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.SideShow.ISideShowNotificationManager_head))(4, 'RegisterNotifications', ((1, 'in_applicationId'),(1, 'out_ppINotification'),)))
    win32more.System.Com.IUnknown
    return ISideShowSession
def _define_NEW_EVENT_DATA_AVAILABLE_head():
    class NEW_EVENT_DATA_AVAILABLE(Structure):
        pass
    return NEW_EVENT_DATA_AVAILABLE
def _define_NEW_EVENT_DATA_AVAILABLE():
    NEW_EVENT_DATA_AVAILABLE = win32more.System.SideShow.NEW_EVENT_DATA_AVAILABLE_head
    NEW_EVENT_DATA_AVAILABLE._pack_ = 1
    NEW_EVENT_DATA_AVAILABLE._fields_ = [
        ('cbNewEventDataAvailable', UInt32),
        ('dwVersion', UInt32),
    ]
    return NEW_EVENT_DATA_AVAILABLE
SCF_BUTTON_IDS = Int32
SCF_BUTTON_MENU = 1
SCF_BUTTON_SELECT = 2
SCF_BUTTON_UP = 3
SCF_BUTTON_DOWN = 4
SCF_BUTTON_LEFT = 5
SCF_BUTTON_RIGHT = 6
SCF_BUTTON_PLAY = 7
SCF_BUTTON_PAUSE = 8
SCF_BUTTON_FASTFORWARD = 9
SCF_BUTTON_REWIND = 10
SCF_BUTTON_STOP = 11
SCF_BUTTON_BACK = 65280
def _define_SCF_CONTEXTMENU_EVENT_head():
    class SCF_CONTEXTMENU_EVENT(Structure):
        pass
    return SCF_CONTEXTMENU_EVENT
def _define_SCF_CONTEXTMENU_EVENT():
    SCF_CONTEXTMENU_EVENT = win32more.System.SideShow.SCF_CONTEXTMENU_EVENT_head
    SCF_CONTEXTMENU_EVENT._fields_ = [
        ('PreviousPage', UInt32),
        ('TargetPage', UInt32),
        ('PreviousItemId', UInt32),
        ('MenuPage', UInt32),
        ('MenuItemId', UInt32),
    ]
    return SCF_CONTEXTMENU_EVENT
def _define_SCF_EVENT_HEADER_head():
    class SCF_EVENT_HEADER(Structure):
        pass
    return SCF_EVENT_HEADER
def _define_SCF_EVENT_HEADER():
    SCF_EVENT_HEADER = win32more.System.SideShow.SCF_EVENT_HEADER_head
    SCF_EVENT_HEADER._fields_ = [
        ('PreviousPage', UInt32),
        ('TargetPage', UInt32),
    ]
    return SCF_EVENT_HEADER
SCF_EVENT_IDS = Int32
SCF_EVENT_NAVIGATION = 1
SCF_EVENT_MENUACTION = 2
SCF_EVENT_CONTEXTMENU = 3
def _define_SCF_MENUACTION_EVENT_head():
    class SCF_MENUACTION_EVENT(Structure):
        pass
    return SCF_MENUACTION_EVENT
def _define_SCF_MENUACTION_EVENT():
    SCF_MENUACTION_EVENT = win32more.System.SideShow.SCF_MENUACTION_EVENT_head
    SCF_MENUACTION_EVENT._fields_ = [
        ('PreviousPage', UInt32),
        ('TargetPage', UInt32),
        ('Button', UInt32),
        ('ItemId', UInt32),
    ]
    return SCF_MENUACTION_EVENT
def _define_SCF_NAVIGATION_EVENT_head():
    class SCF_NAVIGATION_EVENT(Structure):
        pass
    return SCF_NAVIGATION_EVENT
def _define_SCF_NAVIGATION_EVENT():
    SCF_NAVIGATION_EVENT = win32more.System.SideShow.SCF_NAVIGATION_EVENT_head
    SCF_NAVIGATION_EVENT._fields_ = [
        ('PreviousPage', UInt32),
        ('TargetPage', UInt32),
        ('Button', UInt32),
    ]
    return SCF_NAVIGATION_EVENT
SIDESHOW_COLOR_TYPE = Int32
SIDESHOW_COLOR_TYPE_COLOR = 0
SIDESHOW_COLOR_TYPE_GREYSCALE = 1
SIDESHOW_COLOR_TYPE_BLACK_AND_WHITE = 2
SIDESHOW_SCREEN_TYPE = Int32
SIDESHOW_SCREEN_TYPE_BITMAP = 0
SIDESHOW_SCREEN_TYPE_TEXT = 1
SideShowKeyCollection = Guid('dfbbdbf8-18de-49b8-83-dc-eb-c7-27-c6-2d-94')
SideShowNotification = Guid('0ce3e86f-d5cd-4525-a7-66-1a-ba-b1-a7-52-f5')
SideShowPropVariantCollection = Guid('e640f415-539e-4923-96-cd-5f-09-3b-c2-50-cd')
SideShowSession = Guid('e20543b9-f785-4ea2-98-1e-c4-ff-a7-6b-bc-7c')
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
