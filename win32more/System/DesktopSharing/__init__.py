from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.DesktopSharing
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
def _define___ReferenceRemainingTypes___head():
    class __ReferenceRemainingTypes__(Structure):
        pass
    return __ReferenceRemainingTypes__
def _define___ReferenceRemainingTypes__():
    __ReferenceRemainingTypes__ = win32more.System.DesktopSharing.__ReferenceRemainingTypes___head
    __ReferenceRemainingTypes__._fields_ = [
        ('__ctrlLevel__', win32more.System.DesktopSharing.CTRL_LEVEL),
        ('__attendeeDisconnectReason__', win32more.System.DesktopSharing.ATTENDEE_DISCONNECT_REASON),
        ('__channelPriority__', win32more.System.DesktopSharing.CHANNEL_PRIORITY),
        ('__channelFlags__', win32more.System.DesktopSharing.CHANNEL_FLAGS),
        ('__channelAccessEnum__', win32more.System.DesktopSharing.CHANNEL_ACCESS_ENUM),
        ('__rdpencomapiAttendeeFlags__', win32more.System.DesktopSharing.RDPENCOMAPI_ATTENDEE_FLAGS),
        ('__rdpsrapiWndFlags__', win32more.System.DesktopSharing.RDPSRAPI_WND_FLAGS),
        ('__rdpsrapiAppFlags__', win32more.System.DesktopSharing.RDPSRAPI_APP_FLAGS),
    ]
    return __ReferenceRemainingTypes__
def _define__IRDPSessionEvents_head():
    class _IRDPSessionEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('98a97042-6698-40e9-8e-fd-b3-20-09-90-00-4b')
    return _IRDPSessionEvents
def _define__IRDPSessionEvents():
    _IRDPSessionEvents = win32more.System.DesktopSharing._IRDPSessionEvents_head
    win32more.System.Com.IDispatch
    return _IRDPSessionEvents
DISPID_RDPSRAPI_METHOD_OPEN = 100
DISPID_RDPSRAPI_METHOD_CLOSE = 101
DISPID_RDPSRAPI_METHOD_SETSHAREDRECT = 102
DISPID_RDPSRAPI_METHOD_GETSHAREDRECT = 103
DISPID_RDPSRAPI_METHOD_VIEWERCONNECT = 104
DISPID_RDPSRAPI_METHOD_VIEWERDISCONNECT = 105
DISPID_RDPSRAPI_METHOD_TERMINATE_CONNECTION = 106
DISPID_RDPSRAPI_METHOD_CREATE_INVITATION = 107
DISPID_RDPSRAPI_METHOD_REQUEST_CONTROL = 108
DISPID_RDPSRAPI_METHOD_VIRTUAL_CHANNEL_CREATE = 109
DISPID_RDPSRAPI_METHOD_VIRTUAL_CHANNEL_SEND_DATA = 110
DISPID_RDPSRAPI_METHOD_VIRTUAL_CHANNEL_SET_ACCESS = 111
DISPID_RDPSRAPI_METHOD_PAUSE = 112
DISPID_RDPSRAPI_METHOD_RESUME = 113
DISPID_RDPSRAPI_METHOD_SHOW_WINDOW = 114
DISPID_RDPSRAPI_METHOD_REQUEST_COLOR_DEPTH_CHANGE = 115
DISPID_RDPSRAPI_METHOD_STARTREVCONNECTLISTENER = 116
DISPID_RDPSRAPI_METHOD_CONNECTTOCLIENT = 117
DISPID_RDPSRAPI_METHOD_SET_RENDERING_SURFACE = 118
DISPID_RDPSRAPI_METHOD_SEND_MOUSE_BUTTON_EVENT = 119
DISPID_RDPSRAPI_METHOD_SEND_MOUSE_MOVE_EVENT = 120
DISPID_RDPSRAPI_METHOD_SEND_MOUSE_WHEEL_EVENT = 121
DISPID_RDPSRAPI_METHOD_SEND_KEYBOARD_EVENT = 122
DISPID_RDPSRAPI_METHOD_SEND_SYNC_EVENT = 123
DISPID_RDPSRAPI_METHOD_BEGIN_TOUCH_FRAME = 124
DISPID_RDPSRAPI_METHOD_ADD_TOUCH_INPUT = 125
DISPID_RDPSRAPI_METHOD_END_TOUCH_FRAME = 126
DISPID_RDPSRAPI_METHOD_CONNECTUSINGTRANSPORTSTREAM = 127
DISPID_RDPSRAPI_METHOD_SENDCONTROLLEVELCHANGERESPONSE = 148
DISPID_RDPSRAPI_METHOD_GETFRAMEBUFFERBITS = 149
DISPID_RDPSRAPI_PROP_DISPIDVALUE = 200
DISPID_RDPSRAPI_PROP_ID = 201
DISPID_RDPSRAPI_PROP_SESSION_PROPERTIES = 202
DISPID_RDPSRAPI_PROP_ATTENDEES = 203
DISPID_RDPSRAPI_PROP_INVITATIONS = 204
DISPID_RDPSRAPI_PROP_INVITATION = 205
DISPID_RDPSRAPI_PROP_CHANNELMANAGER = 206
DISPID_RDPSRAPI_PROP_VIRTUAL_CHANNEL_GETNAME = 207
DISPID_RDPSRAPI_PROP_VIRTUAL_CHANNEL_GETFLAGS = 208
DISPID_RDPSRAPI_PROP_VIRTUAL_CHANNEL_GETPRIORITY = 209
DISPID_RDPSRAPI_PROP_WINDOWID = 210
DISPID_RDPSRAPI_PROP_APPLICATION = 211
DISPID_RDPSRAPI_PROP_WINDOWSHARED = 212
DISPID_RDPSRAPI_PROP_WINDOWNAME = 213
DISPID_RDPSRAPI_PROP_APPNAME = 214
DISPID_RDPSRAPI_PROP_APPLICATION_FILTER = 215
DISPID_RDPSRAPI_PROP_WINDOW_LIST = 216
DISPID_RDPSRAPI_PROP_APPLICATION_LIST = 217
DISPID_RDPSRAPI_PROP_APPFILTER_ENABLED = 218
DISPID_RDPSRAPI_PROP_APPFILTERENABLED = 219
DISPID_RDPSRAPI_PROP_SHARED = 220
DISPID_RDPSRAPI_PROP_INVITATIONITEM = 221
DISPID_RDPSRAPI_PROP_DBG_CLX_CMDLINE = 222
DISPID_RDPSRAPI_PROP_APPFLAGS = 223
DISPID_RDPSRAPI_PROP_WNDFLAGS = 224
DISPID_RDPSRAPI_PROP_PROTOCOL_TYPE = 225
DISPID_RDPSRAPI_PROP_LOCAL_PORT = 226
DISPID_RDPSRAPI_PROP_LOCAL_IP = 227
DISPID_RDPSRAPI_PROP_PEER_PORT = 228
DISPID_RDPSRAPI_PROP_PEER_IP = 229
DISPID_RDPSRAPI_PROP_ATTENDEE_FLAGS = 230
DISPID_RDPSRAPI_PROP_CONINFO = 231
DISPID_RDPSRAPI_PROP_CONNECTION_STRING = 232
DISPID_RDPSRAPI_PROP_GROUP_NAME = 233
DISPID_RDPSRAPI_PROP_PASSWORD = 234
DISPID_RDPSRAPI_PROP_ATTENDEELIMIT = 235
DISPID_RDPSRAPI_PROP_REVOKED = 236
DISPID_RDPSRAPI_PROP_DISCONNECTED_STRING = 237
DISPID_RDPSRAPI_PROP_USESMARTSIZING = 238
DISPID_RDPSRAPI_PROP_SESSION_COLORDEPTH = 239
DISPID_RDPSRAPI_PROP_REASON = 240
DISPID_RDPSRAPI_PROP_CODE = 241
DISPID_RDPSRAPI_PROP_CTRL_LEVEL = 242
DISPID_RDPSRAPI_PROP_REMOTENAME = 243
DISPID_RDPSRAPI_PROP_COUNT = 244
DISPID_RDPSRAPI_PROP_FRAMEBUFFER_HEIGHT = 251
DISPID_RDPSRAPI_PROP_FRAMEBUFFER_WIDTH = 252
DISPID_RDPSRAPI_PROP_FRAMEBUFFER_BPP = 253
DISPID_RDPSRAPI_PROP_FRAMEBUFFER = 254
DISPID_RDPSRAPI_EVENT_ON_ATTENDEE_CONNECTED = 301
DISPID_RDPSRAPI_EVENT_ON_ATTENDEE_DISCONNECTED = 302
DISPID_RDPSRAPI_EVENT_ON_ATTENDEE_UPDATE = 303
DISPID_RDPSRAPI_EVENT_ON_ERROR = 304
DISPID_RDPSRAPI_EVENT_ON_VIEWER_CONNECTED = 305
DISPID_RDPSRAPI_EVENT_ON_VIEWER_DISCONNECTED = 306
DISPID_RDPSRAPI_EVENT_ON_VIEWER_AUTHENTICATED = 307
DISPID_RDPSRAPI_EVENT_ON_VIEWER_CONNECTFAILED = 308
DISPID_RDPSRAPI_EVENT_ON_CTRLLEVEL_CHANGE_REQUEST = 309
DISPID_RDPSRAPI_EVENT_ON_GRAPHICS_STREAM_PAUSED = 310
DISPID_RDPSRAPI_EVENT_ON_GRAPHICS_STREAM_RESUMED = 311
DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_JOIN = 312
DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_LEAVE = 313
DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_DATARECEIVED = 314
DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_SENDCOMPLETED = 315
DISPID_RDPSRAPI_EVENT_ON_APPLICATION_OPEN = 316
DISPID_RDPSRAPI_EVENT_ON_APPLICATION_CLOSE = 317
DISPID_RDPSRAPI_EVENT_ON_APPLICATION_UPDATE = 318
DISPID_RDPSRAPI_EVENT_ON_WINDOW_OPEN = 319
DISPID_RDPSRAPI_EVENT_ON_WINDOW_CLOSE = 320
DISPID_RDPSRAPI_EVENT_ON_WINDOW_UPDATE = 321
DISPID_RDPSRAPI_EVENT_ON_APPFILTER_UPDATE = 322
DISPID_RDPSRAPI_EVENT_ON_SHARED_RECT_CHANGED = 323
DISPID_RDPSRAPI_EVENT_ON_FOCUSRELEASED = 324
DISPID_RDPSRAPI_EVENT_ON_SHARED_DESKTOP_SETTINGS_CHANGED = 325
DISPID_RDPSRAPI_EVENT_ON_CTRLLEVEL_CHANGE_RESPONSE = 338
DISPID_RDPAPI_EVENT_ON_BOUNDING_RECT_CHANGED = 340
DISPID_RDPSRAPI_METHOD_STREAM_ALLOCBUFFER = 421
DISPID_RDPSRAPI_METHOD_STREAM_FREEBUFFER = 422
DISPID_RDPSRAPI_METHOD_STREAMSENDDATA = 423
DISPID_RDPSRAPI_METHOD_STREAMREADDATA = 424
DISPID_RDPSRAPI_METHOD_STREAMOPEN = 425
DISPID_RDPSRAPI_METHOD_STREAMCLOSE = 426
DISPID_RDPSRAPI_PROP_STREAMBUFFER_STORAGE = 555
DISPID_RDPSRAPI_PROP_STREAMBUFFER_PAYLOADSIZE = 558
DISPID_RDPSRAPI_PROP_STREAMBUFFER_PAYLOADOFFSET = 559
DISPID_RDPSRAPI_PROP_STREAMBUFFER_CONTEXT = 560
DISPID_RDPSRAPI_PROP_STREAMBUFFER_FLAGS = 561
DISPID_RDPSRAPI_PROP_STREAMBUFFER_STORESIZE = 562
DISPID_RDPSRAPI_EVENT_ON_STREAM_SENDCOMPLETED = 632
DISPID_RDPSRAPI_EVENT_ON_STREAM_DATARECEIVED = 633
DISPID_RDPSRAPI_EVENT_ON_STREAM_CLOSED = 634
DISPID_RDPSRAPI_EVENT_VIEW_MOUSE_BUTTON_RECEIVED = 700
DISPID_RDPSRAPI_EVENT_VIEW_MOUSE_MOVE_RECEIVED = 701
DISPID_RDPSRAPI_EVENT_VIEW_MOUSE_WHEEL_RECEIVED = 702
ATTENDEE_DISCONNECT_REASON = Int32
ATTENDEE_DISCONNECT_REASON_MIN = 0
ATTENDEE_DISCONNECT_REASON_APP = 0
ATTENDEE_DISCONNECT_REASON_ERR = 1
ATTENDEE_DISCONNECT_REASON_CLI = 2
ATTENDEE_DISCONNECT_REASON_MAX = 2
CHANNEL_ACCESS_ENUM = Int32
CHANNEL_ACCESS_ENUM_NONE = 0
CHANNEL_ACCESS_ENUM_SENDRECEIVE = 1
CHANNEL_FLAGS = Int32
CHANNEL_FLAGS_LEGACY = 1
CHANNEL_FLAGS_UNCOMPRESSED = 2
CHANNEL_FLAGS_DYNAMIC = 4
CHANNEL_PRIORITY = Int32
CHANNEL_PRIORITY_LO = 0
CHANNEL_PRIORITY_MED = 1
CHANNEL_PRIORITY_HI = 2
CTRL_LEVEL = Int32
CTRL_LEVEL_MIN = 0
CTRL_LEVEL_INVALID = 0
CTRL_LEVEL_NONE = 1
CTRL_LEVEL_VIEW = 2
CTRL_LEVEL_INTERACTIVE = 3
CTRL_LEVEL_REQCTRL_VIEW = 4
CTRL_LEVEL_REQCTRL_INTERACTIVE = 5
CTRL_LEVEL_MAX = 5
def _define_IRDPSRAPIApplication_head():
    class IRDPSRAPIApplication(win32more.System.Com.IDispatch_head):
        Guid = Guid('41e7a09d-eb7a-436e-93-5d-78-0c-a2-62-83-24')
    return IRDPSRAPIApplication
def _define_IRDPSRAPIApplication():
    IRDPSRAPIApplication = win32more.System.DesktopSharing.IRDPSRAPIApplication_head
    IRDPSRAPIApplication.get_Windows = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIWindowList_head))(7, 'get_Windows', ((1, 'pWindowList'),)))
    IRDPSRAPIApplication.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_Id', ((1, 'pRetVal'),)))
    IRDPSRAPIApplication.get_Shared = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_Shared', ((1, 'pRetVal'),)))
    IRDPSRAPIApplication.put_Shared = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(10, 'put_Shared', ((1, 'NewVal'),)))
    IRDPSRAPIApplication.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_Name', ((1, 'pRetVal'),)))
    IRDPSRAPIApplication.get_Flags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'get_Flags', ((1, 'pdwFlags'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIApplication
def _define_IRDPSRAPIApplicationFilter_head():
    class IRDPSRAPIApplicationFilter(win32more.System.Com.IDispatch_head):
        Guid = Guid('d20f10ca-6637-4f06-b1-d5-27-7e-a7-e5-16-0d')
    return IRDPSRAPIApplicationFilter
def _define_IRDPSRAPIApplicationFilter():
    IRDPSRAPIApplicationFilter = win32more.System.DesktopSharing.IRDPSRAPIApplicationFilter_head
    IRDPSRAPIApplicationFilter.get_Applications = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIApplicationList_head))(7, 'get_Applications', ((1, 'pApplications'),)))
    IRDPSRAPIApplicationFilter.get_Windows = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIWindowList_head))(8, 'get_Windows', ((1, 'pWindows'),)))
    IRDPSRAPIApplicationFilter.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_Enabled', ((1, 'pRetVal'),)))
    IRDPSRAPIApplicationFilter.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(10, 'put_Enabled', ((1, 'NewVal'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIApplicationFilter
def _define_IRDPSRAPIApplicationList_head():
    class IRDPSRAPIApplicationList(win32more.System.Com.IDispatch_head):
        Guid = Guid('d4b4aeb3-22dc-4837-b3-b6-42-ea-25-17-84-9a')
    return IRDPSRAPIApplicationList
def _define_IRDPSRAPIApplicationList():
    IRDPSRAPIApplicationList = win32more.System.DesktopSharing.IRDPSRAPIApplicationList_head
    IRDPSRAPIApplicationList.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'retval'),)))
    IRDPSRAPIApplicationList.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.DesktopSharing.IRDPSRAPIApplication_head))(8, 'get_Item', ((1, 'item'),(1, 'pApplication'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIApplicationList
def _define_IRDPSRAPIAttendee_head():
    class IRDPSRAPIAttendee(win32more.System.Com.IDispatch_head):
        Guid = Guid('ec0671b3-1b78-4b80-a4-64-91-32-24-75-43-e3')
    return IRDPSRAPIAttendee
def _define_IRDPSRAPIAttendee():
    IRDPSRAPIAttendee = win32more.System.DesktopSharing.IRDPSRAPIAttendee_head
    IRDPSRAPIAttendee.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Id', ((1, 'pId'),)))
    IRDPSRAPIAttendee.get_RemoteName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_RemoteName', ((1, 'pVal'),)))
    IRDPSRAPIAttendee.get_ControlLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.CTRL_LEVEL))(9, 'get_ControlLevel', ((1, 'pVal'),)))
    IRDPSRAPIAttendee.put_ControlLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DesktopSharing.CTRL_LEVEL)(10, 'put_ControlLevel', ((1, 'pNewVal'),)))
    IRDPSRAPIAttendee.get_Invitation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIInvitation_head))(11, 'get_Invitation', ((1, 'ppVal'),)))
    IRDPSRAPIAttendee.TerminateConnection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'TerminateConnection', ()))
    IRDPSRAPIAttendee.get_Flags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_Flags', ((1, 'plFlags'),)))
    IRDPSRAPIAttendee.get_ConnectivityInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(14, 'get_ConnectivityInfo', ((1, 'ppVal'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIAttendee
def _define_IRDPSRAPIAttendeeDisconnectInfo_head():
    class IRDPSRAPIAttendeeDisconnectInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('c187689f-447c-44a1-9c-14-ff-fb-b3-b7-ec-17')
    return IRDPSRAPIAttendeeDisconnectInfo
def _define_IRDPSRAPIAttendeeDisconnectInfo():
    IRDPSRAPIAttendeeDisconnectInfo = win32more.System.DesktopSharing.IRDPSRAPIAttendeeDisconnectInfo_head
    IRDPSRAPIAttendeeDisconnectInfo.get_Attendee = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIAttendee_head))(7, 'get_Attendee', ((1, 'retval'),)))
    IRDPSRAPIAttendeeDisconnectInfo.get_Reason = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.ATTENDEE_DISCONNECT_REASON))(8, 'get_Reason', ((1, 'pReason'),)))
    IRDPSRAPIAttendeeDisconnectInfo.get_Code = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Code', ((1, 'pVal'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIAttendeeDisconnectInfo
def _define_IRDPSRAPIAttendeeManager_head():
    class IRDPSRAPIAttendeeManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('ba3a37e8-33da-4749-8d-a0-07-fa-34-da-79-44')
    return IRDPSRAPIAttendeeManager
def _define_IRDPSRAPIAttendeeManager():
    IRDPSRAPIAttendeeManager = win32more.System.DesktopSharing.IRDPSRAPIAttendeeManager_head
    IRDPSRAPIAttendeeManager.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'retval'),)))
    IRDPSRAPIAttendeeManager.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.DesktopSharing.IRDPSRAPIAttendee_head))(8, 'get_Item', ((1, 'id'),(1, 'ppItem'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIAttendeeManager
def _define_IRDPSRAPIAudioStream_head():
    class IRDPSRAPIAudioStream(win32more.System.Com.IUnknown_head):
        Guid = Guid('e3e30ef9-89c6-4541-ba-3b-19-33-6a-c6-d3-1c')
    return IRDPSRAPIAudioStream
def _define_IRDPSRAPIAudioStream():
    IRDPSRAPIAudioStream = win32more.System.DesktopSharing.IRDPSRAPIAudioStream_head
    IRDPSRAPIAudioStream.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64))(3, 'Initialize', ((1, 'pnPeriodInHundredNsIntervals'),)))
    IRDPSRAPIAudioStream.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Start', ()))
    IRDPSRAPIAudioStream.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Stop', ()))
    IRDPSRAPIAudioStream.GetBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32),POINTER(UInt64))(6, 'GetBuffer', ((1, 'ppbData'),(1, 'pcbData'),(1, 'pTimestamp'),)))
    IRDPSRAPIAudioStream.FreeBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'FreeBuffer', ()))
    win32more.System.Com.IUnknown
    return IRDPSRAPIAudioStream
def _define_IRDPSRAPIClipboardUseEvents_head():
    class IRDPSRAPIClipboardUseEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('d559f59a-7a27-4138-87-63-24-7c-e5-f6-59-a8')
    return IRDPSRAPIClipboardUseEvents
def _define_IRDPSRAPIClipboardUseEvents():
    IRDPSRAPIClipboardUseEvents = win32more.System.DesktopSharing.IRDPSRAPIClipboardUseEvents_head
    IRDPSRAPIClipboardUseEvents.OnPasteFromClipboard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IDispatch_head,POINTER(win32more.Foundation.VARIANT_BOOL))(3, 'OnPasteFromClipboard', ((1, 'clipboardFormat'),(1, 'pAttendee'),(1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRDPSRAPIClipboardUseEvents
def _define_IRDPSRAPIDebug_head():
    class IRDPSRAPIDebug(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa1e42b5-496d-4ca4-a6-90-34-8d-cb-2e-c4-ad')
    return IRDPSRAPIDebug
def _define_IRDPSRAPIDebug():
    IRDPSRAPIDebug = win32more.System.DesktopSharing.IRDPSRAPIDebug_head
    IRDPSRAPIDebug.put_CLXCmdLine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(3, 'put_CLXCmdLine', ((1, 'CLXCmdLine'),)))
    IRDPSRAPIDebug.get_CLXCmdLine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'get_CLXCmdLine', ((1, 'pCLXCmdLine'),)))
    win32more.System.Com.IUnknown
    return IRDPSRAPIDebug
def _define_IRDPSRAPIFrameBuffer_head():
    class IRDPSRAPIFrameBuffer(win32more.System.Com.IDispatch_head):
        Guid = Guid('3d67e7d2-b27b-448e-81-b3-c6-11-0e-d8-b4-be')
    return IRDPSRAPIFrameBuffer
def _define_IRDPSRAPIFrameBuffer():
    IRDPSRAPIFrameBuffer = win32more.System.DesktopSharing.IRDPSRAPIFrameBuffer_head
    IRDPSRAPIFrameBuffer.get_Width = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Width', ((1, 'plWidth'),)))
    IRDPSRAPIFrameBuffer.get_Height = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_Height', ((1, 'plHeight'),)))
    IRDPSRAPIFrameBuffer.get_Bpp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Bpp', ((1, 'plBpp'),)))
    IRDPSRAPIFrameBuffer.GetFrameBufferBits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,Int32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(10, 'GetFrameBufferBits', ((1, 'x'),(1, 'y'),(1, 'Width'),(1, 'Heigth'),(1, 'ppBits'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIFrameBuffer
def _define_IRDPSRAPIInvitation_head():
    class IRDPSRAPIInvitation(win32more.System.Com.IDispatch_head):
        Guid = Guid('4fac1d43-fc51-45bb-b1-b4-2b-53-aa-56-2f-a3')
    return IRDPSRAPIInvitation
def _define_IRDPSRAPIInvitation():
    IRDPSRAPIInvitation = win32more.System.DesktopSharing.IRDPSRAPIInvitation_head
    IRDPSRAPIInvitation.get_ConnectionString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_ConnectionString', ((1, 'pbstrVal'),)))
    IRDPSRAPIInvitation.get_GroupName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_GroupName', ((1, 'pbstrVal'),)))
    IRDPSRAPIInvitation.get_Password = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Password', ((1, 'pbstrVal'),)))
    IRDPSRAPIInvitation.get_AttendeeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_AttendeeLimit', ((1, 'pRetVal'),)))
    IRDPSRAPIInvitation.put_AttendeeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(11, 'put_AttendeeLimit', ((1, 'NewVal'),)))
    IRDPSRAPIInvitation.get_Revoked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(12, 'get_Revoked', ((1, 'pRetVal'),)))
    IRDPSRAPIInvitation.put_Revoked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(13, 'put_Revoked', ((1, 'NewVal'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIInvitation
def _define_IRDPSRAPIInvitationManager_head():
    class IRDPSRAPIInvitationManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('4722b049-92c3-4c2d-8a-65-f7-34-8f-64-4d-cf')
    return IRDPSRAPIInvitationManager
def _define_IRDPSRAPIInvitationManager():
    IRDPSRAPIInvitationManager = win32more.System.DesktopSharing.IRDPSRAPIInvitationManager_head
    IRDPSRAPIInvitationManager.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'retval'),)))
    IRDPSRAPIInvitationManager.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIInvitation_head))(8, 'get_Item', ((1, 'item'),(1, 'ppInvitation'),)))
    IRDPSRAPIInvitationManager.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Count', ((1, 'pRetVal'),)))
    IRDPSRAPIInvitationManager.CreateInvitation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.DesktopSharing.IRDPSRAPIInvitation_head))(10, 'CreateInvitation', ((1, 'bstrAuthString'),(1, 'bstrGroupName'),(1, 'bstrPassword'),(1, 'AttendeeLimit'),(1, 'ppInvitation'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIInvitationManager
def _define_IRDPSRAPIPerfCounterLogger_head():
    class IRDPSRAPIPerfCounterLogger(win32more.System.Com.IUnknown_head):
        Guid = Guid('071c2533-0fa4-4e8f-ae-83-9c-10-b4-30-5a-b5')
    return IRDPSRAPIPerfCounterLogger
def _define_IRDPSRAPIPerfCounterLogger():
    IRDPSRAPIPerfCounterLogger = win32more.System.DesktopSharing.IRDPSRAPIPerfCounterLogger_head
    IRDPSRAPIPerfCounterLogger.LogValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64)(3, 'LogValue', ((1, 'lValue'),)))
    win32more.System.Com.IUnknown
    return IRDPSRAPIPerfCounterLogger
def _define_IRDPSRAPIPerfCounterLoggingManager_head():
    class IRDPSRAPIPerfCounterLoggingManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('9a512c86-ac6e-4a8e-b1-a4-fc-ef-36-3f-6e-64')
    return IRDPSRAPIPerfCounterLoggingManager
def _define_IRDPSRAPIPerfCounterLoggingManager():
    IRDPSRAPIPerfCounterLoggingManager = win32more.System.DesktopSharing.IRDPSRAPIPerfCounterLoggingManager_head
    IRDPSRAPIPerfCounterLoggingManager.CreateLogger = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.DesktopSharing.IRDPSRAPIPerfCounterLogger_head))(3, 'CreateLogger', ((1, 'bstrCounterName'),(1, 'ppLogger'),)))
    win32more.System.Com.IUnknown
    return IRDPSRAPIPerfCounterLoggingManager
def _define_IRDPSRAPISessionProperties_head():
    class IRDPSRAPISessionProperties(win32more.System.Com.IDispatch_head):
        Guid = Guid('339b24f2-9bc0-4f16-9a-ac-f1-65-43-3d-13-d4')
    return IRDPSRAPISessionProperties
def _define_IRDPSRAPISessionProperties():
    IRDPSRAPISessionProperties = win32more.System.DesktopSharing.IRDPSRAPISessionProperties_head
    IRDPSRAPISessionProperties.get_Property = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head))(7, 'get_Property', ((1, 'PropertyName'),(1, 'pVal'),)))
    IRDPSRAPISessionProperties.put_Property = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT)(8, 'put_Property', ((1, 'PropertyName'),(1, 'newVal'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPISessionProperties
def _define_IRDPSRAPISharingSession_head():
    class IRDPSRAPISharingSession(win32more.System.Com.IDispatch_head):
        Guid = Guid('eeb20886-e470-4cf6-84-2b-27-39-c0-ec-5c-fb')
    return IRDPSRAPISharingSession
def _define_IRDPSRAPISharingSession():
    IRDPSRAPISharingSession = win32more.System.DesktopSharing.IRDPSRAPISharingSession_head
    IRDPSRAPISharingSession.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Open', ()))
    IRDPSRAPISharingSession.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Close', ()))
    IRDPSRAPISharingSession.put_ColorDepth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(9, 'put_ColorDepth', ((1, 'colorDepth'),)))
    IRDPSRAPISharingSession.get_ColorDepth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_ColorDepth', ((1, 'pColorDepth'),)))
    IRDPSRAPISharingSession.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPISessionProperties_head))(11, 'get_Properties', ((1, 'ppVal'),)))
    IRDPSRAPISharingSession.get_Attendees = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIAttendeeManager_head))(12, 'get_Attendees', ((1, 'ppVal'),)))
    IRDPSRAPISharingSession.get_Invitations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIInvitationManager_head))(13, 'get_Invitations', ((1, 'ppVal'),)))
    IRDPSRAPISharingSession.get_ApplicationFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIApplicationFilter_head))(14, 'get_ApplicationFilter', ((1, 'ppVal'),)))
    IRDPSRAPISharingSession.get_VirtualChannelManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIVirtualChannelManager_head))(15, 'get_VirtualChannelManager', ((1, 'ppVal'),)))
    IRDPSRAPISharingSession.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'Pause', ()))
    IRDPSRAPISharingSession.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(17, 'Resume', ()))
    IRDPSRAPISharingSession.ConnectToClient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(18, 'ConnectToClient', ((1, 'bstrConnectionString'),)))
    IRDPSRAPISharingSession.SetDesktopSharedRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,Int32)(19, 'SetDesktopSharedRect', ((1, 'left'),(1, 'top'),(1, 'right'),(1, 'bottom'),)))
    IRDPSRAPISharingSession.GetDesktopSharedRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32))(20, 'GetDesktopSharedRect', ((1, 'pleft'),(1, 'ptop'),(1, 'pright'),(1, 'pbottom'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPISharingSession
def _define_IRDPSRAPISharingSession2_head():
    class IRDPSRAPISharingSession2(win32more.System.DesktopSharing.IRDPSRAPISharingSession_head):
        Guid = Guid('fee4ee57-e3e8-4205-8f-b0-8f-d1-d0-67-5c-21')
    return IRDPSRAPISharingSession2
def _define_IRDPSRAPISharingSession2():
    IRDPSRAPISharingSession2 = win32more.System.DesktopSharing.IRDPSRAPISharingSession2_head
    IRDPSRAPISharingSession2.ConnectUsingTransportStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DesktopSharing.IRDPSRAPITransportStream_head,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(21, 'ConnectUsingTransportStream', ((1, 'pStream'),(1, 'bstrGroup'),(1, 'bstrAuthenticatedAttendeeName'),)))
    IRDPSRAPISharingSession2.get_FrameBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIFrameBuffer_head))(22, 'get_FrameBuffer', ((1, 'ppVal'),)))
    IRDPSRAPISharingSession2.SendControlLevelChangeResponse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DesktopSharing.IRDPSRAPIAttendee_head,win32more.System.DesktopSharing.CTRL_LEVEL,Int32)(23, 'SendControlLevelChangeResponse', ((1, 'pAttendee'),(1, 'RequestedLevel'),(1, 'ReasonCode'),)))
    win32more.System.DesktopSharing.IRDPSRAPISharingSession
    return IRDPSRAPISharingSession2
def _define_IRDPSRAPITcpConnectionInfo_head():
    class IRDPSRAPITcpConnectionInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('f74049a4-3d06-4028-81-93-0a-8c-29-bc-24-52')
    return IRDPSRAPITcpConnectionInfo
def _define_IRDPSRAPITcpConnectionInfo():
    IRDPSRAPITcpConnectionInfo = win32more.System.DesktopSharing.IRDPSRAPITcpConnectionInfo_head
    IRDPSRAPITcpConnectionInfo.get_Protocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Protocol', ((1, 'plProtocol'),)))
    IRDPSRAPITcpConnectionInfo.get_LocalPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_LocalPort', ((1, 'plPort'),)))
    IRDPSRAPITcpConnectionInfo.get_LocalIP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_LocalIP', ((1, 'pbsrLocalIP'),)))
    IRDPSRAPITcpConnectionInfo.get_PeerPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_PeerPort', ((1, 'plPort'),)))
    IRDPSRAPITcpConnectionInfo.get_PeerIP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_PeerIP', ((1, 'pbstrIP'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPITcpConnectionInfo
def _define_IRDPSRAPITransportStream_head():
    class IRDPSRAPITransportStream(win32more.System.Com.IUnknown_head):
        Guid = Guid('36cfa065-43bb-4ef7-ae-d7-9b-88-a5-05-30-36')
    return IRDPSRAPITransportStream
def _define_IRDPSRAPITransportStream():
    IRDPSRAPITransportStream = win32more.System.DesktopSharing.IRDPSRAPITransportStream_head
    IRDPSRAPITransportStream.AllocBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.DesktopSharing.IRDPSRAPITransportStreamBuffer_head))(3, 'AllocBuffer', ((1, 'maxPayload'),(1, 'ppBuffer'),)))
    IRDPSRAPITransportStream.FreeBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DesktopSharing.IRDPSRAPITransportStreamBuffer_head)(4, 'FreeBuffer', ((1, 'pBuffer'),)))
    IRDPSRAPITransportStream.WriteBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DesktopSharing.IRDPSRAPITransportStreamBuffer_head)(5, 'WriteBuffer', ((1, 'pBuffer'),)))
    IRDPSRAPITransportStream.ReadBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DesktopSharing.IRDPSRAPITransportStreamBuffer_head)(6, 'ReadBuffer', ((1, 'pBuffer'),)))
    IRDPSRAPITransportStream.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DesktopSharing.IRDPSRAPITransportStreamEvents_head)(7, 'Open', ((1, 'pCallbacks'),)))
    IRDPSRAPITransportStream.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Close', ()))
    win32more.System.Com.IUnknown
    return IRDPSRAPITransportStream
def _define_IRDPSRAPITransportStreamBuffer_head():
    class IRDPSRAPITransportStreamBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('81c80290-5085-44b0-b4-60-f8-65-c3-9c-b4-a9')
    return IRDPSRAPITransportStreamBuffer
def _define_IRDPSRAPITransportStreamBuffer():
    IRDPSRAPITransportStreamBuffer = win32more.System.DesktopSharing.IRDPSRAPITransportStreamBuffer_head
    IRDPSRAPITransportStreamBuffer.get_Storage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no))(3, 'get_Storage', ((1, 'ppbStorage'),)))
    IRDPSRAPITransportStreamBuffer.get_StorageSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(4, 'get_StorageSize', ((1, 'plMaxStore'),)))
    IRDPSRAPITransportStreamBuffer.get_PayloadSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(5, 'get_PayloadSize', ((1, 'plRetVal'),)))
    IRDPSRAPITransportStreamBuffer.put_PayloadSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(6, 'put_PayloadSize', ((1, 'lVal'),)))
    IRDPSRAPITransportStreamBuffer.get_PayloadOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_PayloadOffset', ((1, 'plRetVal'),)))
    IRDPSRAPITransportStreamBuffer.put_PayloadOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(8, 'put_PayloadOffset', ((1, 'lRetVal'),)))
    IRDPSRAPITransportStreamBuffer.get_Flags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Flags', ((1, 'plFlags'),)))
    IRDPSRAPITransportStreamBuffer.put_Flags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(10, 'put_Flags', ((1, 'lFlags'),)))
    IRDPSRAPITransportStreamBuffer.get_Context = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(11, 'get_Context', ((1, 'ppContext'),)))
    IRDPSRAPITransportStreamBuffer.put_Context = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(12, 'put_Context', ((1, 'pContext'),)))
    win32more.System.Com.IUnknown
    return IRDPSRAPITransportStreamBuffer
def _define_IRDPSRAPITransportStreamEvents_head():
    class IRDPSRAPITransportStreamEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('ea81c254-f5af-4e40-98-2e-3e-63-bb-59-52-76')
    return IRDPSRAPITransportStreamEvents
def _define_IRDPSRAPITransportStreamEvents():
    IRDPSRAPITransportStreamEvents = win32more.System.DesktopSharing.IRDPSRAPITransportStreamEvents_head
    IRDPSRAPITransportStreamEvents.OnWriteCompleted = COMMETHOD(WINFUNCTYPE(Void,win32more.System.DesktopSharing.IRDPSRAPITransportStreamBuffer_head)(3, 'OnWriteCompleted', ((1, 'pBuffer'),)))
    IRDPSRAPITransportStreamEvents.OnReadCompleted = COMMETHOD(WINFUNCTYPE(Void,win32more.System.DesktopSharing.IRDPSRAPITransportStreamBuffer_head)(4, 'OnReadCompleted', ((1, 'pBuffer'),)))
    IRDPSRAPITransportStreamEvents.OnStreamClosed = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.HRESULT)(5, 'OnStreamClosed', ((1, 'hrReason'),)))
    win32more.System.Com.IUnknown
    return IRDPSRAPITransportStreamEvents
def _define_IRDPSRAPIViewer_head():
    class IRDPSRAPIViewer(win32more.System.Com.IDispatch_head):
        Guid = Guid('c6bfcd38-8ce9-404d-8a-e8-f3-1d-00-c6-5c-b5')
    return IRDPSRAPIViewer
def _define_IRDPSRAPIViewer():
    IRDPSRAPIViewer = win32more.System.DesktopSharing.IRDPSRAPIViewer_head
    IRDPSRAPIViewer.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(7, 'Connect', ((1, 'bstrConnectionString'),(1, 'bstrName'),(1, 'bstrPassword'),)))
    IRDPSRAPIViewer.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Disconnect', ()))
    IRDPSRAPIViewer.get_Attendees = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIAttendeeManager_head))(9, 'get_Attendees', ((1, 'ppVal'),)))
    IRDPSRAPIViewer.get_Invitations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIInvitationManager_head))(10, 'get_Invitations', ((1, 'ppVal'),)))
    IRDPSRAPIViewer.get_ApplicationFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIApplicationFilter_head))(11, 'get_ApplicationFilter', ((1, 'ppVal'),)))
    IRDPSRAPIViewer.get_VirtualChannelManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIVirtualChannelManager_head))(12, 'get_VirtualChannelManager', ((1, 'ppVal'),)))
    IRDPSRAPIViewer.put_SmartSizing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(13, 'put_SmartSizing', ((1, 'vbSmartSizing'),)))
    IRDPSRAPIViewer.get_SmartSizing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(14, 'get_SmartSizing', ((1, 'pvbSmartSizing'),)))
    IRDPSRAPIViewer.RequestControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DesktopSharing.CTRL_LEVEL)(15, 'RequestControl', ((1, 'CtrlLevel'),)))
    IRDPSRAPIViewer.put_DisconnectedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(16, 'put_DisconnectedText', ((1, 'bstrDisconnectedText'),)))
    IRDPSRAPIViewer.get_DisconnectedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(17, 'get_DisconnectedText', ((1, 'pbstrDisconnectedText'),)))
    IRDPSRAPIViewer.RequestColorDepthChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(18, 'RequestColorDepthChange', ((1, 'Bpp'),)))
    IRDPSRAPIViewer.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPISessionProperties_head))(19, 'get_Properties', ((1, 'ppVal'),)))
    IRDPSRAPIViewer.StartReverseConnectListener = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR))(20, 'StartReverseConnectListener', ((1, 'bstrConnectionString'),(1, 'bstrUserName'),(1, 'bstrPassword'),(1, 'pbstrReverseConnectString'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIViewer
def _define_IRDPSRAPIVirtualChannel_head():
    class IRDPSRAPIVirtualChannel(win32more.System.Com.IDispatch_head):
        Guid = Guid('05e12f95-28b3-4c9a-87-80-d0-24-85-74-a1-e0')
    return IRDPSRAPIVirtualChannel
def _define_IRDPSRAPIVirtualChannel():
    IRDPSRAPIVirtualChannel = win32more.System.DesktopSharing.IRDPSRAPIVirtualChannel_head
    IRDPSRAPIVirtualChannel.SendData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,UInt32)(7, 'SendData', ((1, 'bstrData'),(1, 'lAttendeeId'),(1, 'ChannelSendFlags'),)))
    IRDPSRAPIVirtualChannel.SetAccess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.DesktopSharing.CHANNEL_ACCESS_ENUM)(8, 'SetAccess', ((1, 'lAttendeeId'),(1, 'AccessType'),)))
    IRDPSRAPIVirtualChannel.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Name', ((1, 'pbstrName'),)))
    IRDPSRAPIVirtualChannel.get_Flags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_Flags', ((1, 'plFlags'),)))
    IRDPSRAPIVirtualChannel.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.CHANNEL_PRIORITY))(11, 'get_Priority', ((1, 'pPriority'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIVirtualChannel
def _define_IRDPSRAPIVirtualChannelManager_head():
    class IRDPSRAPIVirtualChannelManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('0d11c661-5d0d-4ee4-89-df-21-66-ae-1f-df-ed')
    return IRDPSRAPIVirtualChannelManager
def _define_IRDPSRAPIVirtualChannelManager():
    IRDPSRAPIVirtualChannelManager = win32more.System.DesktopSharing.IRDPSRAPIVirtualChannelManager_head
    IRDPSRAPIVirtualChannelManager.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'retval'),)))
    IRDPSRAPIVirtualChannelManager.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIVirtualChannel_head))(8, 'get_Item', ((1, 'item'),(1, 'pChannel'),)))
    IRDPSRAPIVirtualChannelManager.CreateVirtualChannel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.DesktopSharing.CHANNEL_PRIORITY,UInt32,POINTER(win32more.System.DesktopSharing.IRDPSRAPIVirtualChannel_head))(9, 'CreateVirtualChannel', ((1, 'bstrChannelName'),(1, 'Priority'),(1, 'ChannelFlags'),(1, 'ppChannel'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIVirtualChannelManager
def _define_IRDPSRAPIWindow_head():
    class IRDPSRAPIWindow(win32more.System.Com.IDispatch_head):
        Guid = Guid('beafe0f9-c77b-4933-ba-9f-a2-4c-dd-cc-27-cf')
    return IRDPSRAPIWindow
def _define_IRDPSRAPIWindow():
    IRDPSRAPIWindow = win32more.System.DesktopSharing.IRDPSRAPIWindow_head
    IRDPSRAPIWindow.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Id', ((1, 'pRetVal'),)))
    IRDPSRAPIWindow.get_Application = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.DesktopSharing.IRDPSRAPIApplication_head))(8, 'get_Application', ((1, 'pApplication'),)))
    IRDPSRAPIWindow.get_Shared = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_Shared', ((1, 'pRetVal'),)))
    IRDPSRAPIWindow.put_Shared = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(10, 'put_Shared', ((1, 'NewVal'),)))
    IRDPSRAPIWindow.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_Name', ((1, 'pRetVal'),)))
    IRDPSRAPIWindow.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'Show', ()))
    IRDPSRAPIWindow.get_Flags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(13, 'get_Flags', ((1, 'pdwFlags'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIWindow
def _define_IRDPSRAPIWindowList_head():
    class IRDPSRAPIWindowList(win32more.System.Com.IDispatch_head):
        Guid = Guid('8a05ce44-715a-4116-a1-89-a1-18-f3-0a-07-bd')
    return IRDPSRAPIWindowList
def _define_IRDPSRAPIWindowList():
    IRDPSRAPIWindowList = win32more.System.DesktopSharing.IRDPSRAPIWindowList_head
    IRDPSRAPIWindowList.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get__NewEnum', ((1, 'retval'),)))
    IRDPSRAPIWindowList.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.DesktopSharing.IRDPSRAPIWindow_head))(8, 'get_Item', ((1, 'item'),(1, 'pWindow'),)))
    win32more.System.Com.IDispatch
    return IRDPSRAPIWindowList
def _define_IRDPViewerInputSink_head():
    class IRDPViewerInputSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('bb590853-a6c5-4a7b-8d-d4-76-b6-9e-ea-12-d5')
    return IRDPViewerInputSink
def _define_IRDPViewerInputSink():
    IRDPViewerInputSink = win32more.System.DesktopSharing.IRDPViewerInputSink_head
    IRDPViewerInputSink.SendMouseButtonEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DesktopSharing.RDPSRAPI_MOUSE_BUTTON_TYPE,win32more.Foundation.VARIANT_BOOL,UInt32,UInt32)(3, 'SendMouseButtonEvent', ((1, 'buttonType'),(1, 'vbButtonDown'),(1, 'xPos'),(1, 'yPos'),)))
    IRDPViewerInputSink.SendMouseMoveEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32)(4, 'SendMouseMoveEvent', ((1, 'xPos'),(1, 'yPos'),)))
    IRDPViewerInputSink.SendMouseWheelEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16)(5, 'SendMouseWheelEvent', ((1, 'wheelRotation'),)))
    IRDPViewerInputSink.SendKeyboardEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.DesktopSharing.RDPSRAPI_KBD_CODE_TYPE,UInt16,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.VARIANT_BOOL)(6, 'SendKeyboardEvent', ((1, 'codeType'),(1, 'keycode'),(1, 'vbKeyUp'),(1, 'vbRepeat'),(1, 'vbExtended'),)))
    IRDPViewerInputSink.SendSyncEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'SendSyncEvent', ((1, 'syncFlags'),)))
    IRDPViewerInputSink.BeginTouchFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'BeginTouchFrame', ()))
    IRDPViewerInputSink.AddTouchInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,Int32,Int32)(9, 'AddTouchInput', ((1, 'contactId'),(1, 'event'),(1, 'x'),(1, 'y'),)))
    IRDPViewerInputSink.EndTouchFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'EndTouchFrame', ()))
    win32more.System.Com.IUnknown
    return IRDPViewerInputSink
RDPENCOMAPI_ATTENDEE_FLAGS = Int32
ATTENDEE_FLAGS_LOCAL = 1
RDPENCOMAPI_CONSTANTS = Int32
CONST_MAX_CHANNEL_MESSAGE_SIZE = 1024
CONST_MAX_CHANNEL_NAME_LEN = 8
CONST_MAX_LEGACY_CHANNEL_MESSAGE_SIZE = 409600
CONST_ATTENDEE_ID_EVERYONE = -1
CONST_ATTENDEE_ID_HOST = 0
CONST_CONN_INTERVAL = 50
CONST_ATTENDEE_ID_DEFAULT = -1
RDPSession = Guid('9b78f0e6-3e05-4a5b-b2-e8-e7-43-a8-95-6b-65')
RDPSRAPI_APP_FLAGS = Int32
APP_FLAG_PRIVILEGED = 1
RDPSRAPI_KBD_CODE_TYPE = Int32
RDPSRAPI_KBD_CODE_SCANCODE = 0
RDPSRAPI_KBD_CODE_UNICODE = 1
RDPSRAPI_KBD_SYNC_FLAG = Int32
RDPSRAPI_KBD_SYNC_FLAG_SCROLL_LOCK = 1
RDPSRAPI_KBD_SYNC_FLAG_NUM_LOCK = 2
RDPSRAPI_KBD_SYNC_FLAG_CAPS_LOCK = 4
RDPSRAPI_KBD_SYNC_FLAG_KANA_LOCK = 8
RDPSRAPI_MOUSE_BUTTON_TYPE = Int32
RDPSRAPI_MOUSE_BUTTON_BUTTON1 = 0
RDPSRAPI_MOUSE_BUTTON_BUTTON2 = 1
RDPSRAPI_MOUSE_BUTTON_BUTTON3 = 2
RDPSRAPI_MOUSE_BUTTON_XBUTTON1 = 3
RDPSRAPI_MOUSE_BUTTON_XBUTTON2 = 4
RDPSRAPI_MOUSE_BUTTON_XBUTTON3 = 5
RDPSRAPI_WND_FLAGS = Int32
WND_FLAG_PRIVILEGED = 1
RDPSRAPIApplication = Guid('c116a484-4b25-4b9f-8a-54-b9-34-b0-6e-57-fa')
RDPSRAPIApplicationFilter = Guid('e35ace89-c7e8-427e-a4-f9-b9-da-07-28-26-bd')
RDPSRAPIApplicationList = Guid('9e31c815-7433-4876-97-fb-ed-59-fe-2b-aa-22')
RDPSRAPIAttendee = Guid('74f93bb5-755f-488e-8a-29-23-90-10-8a-ef-55')
RDPSRAPIAttendeeDisconnectInfo = Guid('b47d7250-5bdb-405d-b4-87-ca-ad-9c-56-f4-f8')
RDPSRAPIAttendeeManager = Guid('d7b13a01-f7d4-42a6-85-95-12-fc-8c-24-e8-51')
RDPSRAPIFrameBuffer = Guid('a4f66bcc-538e-4101-95-1d-30-84-7a-db-51-01')
RDPSRAPIInvitation = Guid('49174dc6-0731-4b5e-8e-e1-83-a6-3d-38-68-fa')
RDPSRAPIInvitationManager = Guid('53d9c9db-75ab-4271-94-8a-4c-4e-b3-6a-8f-2b')
RDPSRAPISessionProperties = Guid('dd7594ff-ea2a-4c06-8f-df-13-2d-e4-8b-65-10')
RDPSRAPITcpConnectionInfo = Guid('be49db3f-ebb6-4278-8c-e0-d5-45-58-33-ea-ee')
RDPSRAPIWindow = Guid('03cf46db-ce45-4d36-86-ed-ed-28-b7-43-98-bf')
RDPSRAPIWindowList = Guid('9c21e2b8-5dd4-42cc-81-ba-1c-09-98-52-e6-fa')
RDPTransportStreamBuffer = Guid('8d4a1c69-f17f-4549-a6-99-76-1c-6e-6b-5c-0a')
RDPTransportStreamEvents = Guid('31e3ab20-5350-483f-9d-c6-67-48-66-5e-fd-eb')
RDPViewer = Guid('32be5ed2-5c86-480f-a9-14-0f-f8-88-5a-1b-3f')
__all__ = [
    "APP_FLAG_PRIVILEGED",
    "ATTENDEE_DISCONNECT_REASON",
    "ATTENDEE_DISCONNECT_REASON_APP",
    "ATTENDEE_DISCONNECT_REASON_CLI",
    "ATTENDEE_DISCONNECT_REASON_ERR",
    "ATTENDEE_DISCONNECT_REASON_MAX",
    "ATTENDEE_DISCONNECT_REASON_MIN",
    "ATTENDEE_FLAGS_LOCAL",
    "CHANNEL_ACCESS_ENUM",
    "CHANNEL_ACCESS_ENUM_NONE",
    "CHANNEL_ACCESS_ENUM_SENDRECEIVE",
    "CHANNEL_FLAGS",
    "CHANNEL_FLAGS_DYNAMIC",
    "CHANNEL_FLAGS_LEGACY",
    "CHANNEL_FLAGS_UNCOMPRESSED",
    "CHANNEL_PRIORITY",
    "CHANNEL_PRIORITY_HI",
    "CHANNEL_PRIORITY_LO",
    "CHANNEL_PRIORITY_MED",
    "CONST_ATTENDEE_ID_DEFAULT",
    "CONST_ATTENDEE_ID_EVERYONE",
    "CONST_ATTENDEE_ID_HOST",
    "CONST_CONN_INTERVAL",
    "CONST_MAX_CHANNEL_MESSAGE_SIZE",
    "CONST_MAX_CHANNEL_NAME_LEN",
    "CONST_MAX_LEGACY_CHANNEL_MESSAGE_SIZE",
    "CTRL_LEVEL",
    "CTRL_LEVEL_INTERACTIVE",
    "CTRL_LEVEL_INVALID",
    "CTRL_LEVEL_MAX",
    "CTRL_LEVEL_MIN",
    "CTRL_LEVEL_NONE",
    "CTRL_LEVEL_REQCTRL_INTERACTIVE",
    "CTRL_LEVEL_REQCTRL_VIEW",
    "CTRL_LEVEL_VIEW",
    "DISPID_RDPAPI_EVENT_ON_BOUNDING_RECT_CHANGED",
    "DISPID_RDPSRAPI_EVENT_ON_APPFILTER_UPDATE",
    "DISPID_RDPSRAPI_EVENT_ON_APPLICATION_CLOSE",
    "DISPID_RDPSRAPI_EVENT_ON_APPLICATION_OPEN",
    "DISPID_RDPSRAPI_EVENT_ON_APPLICATION_UPDATE",
    "DISPID_RDPSRAPI_EVENT_ON_ATTENDEE_CONNECTED",
    "DISPID_RDPSRAPI_EVENT_ON_ATTENDEE_DISCONNECTED",
    "DISPID_RDPSRAPI_EVENT_ON_ATTENDEE_UPDATE",
    "DISPID_RDPSRAPI_EVENT_ON_CTRLLEVEL_CHANGE_REQUEST",
    "DISPID_RDPSRAPI_EVENT_ON_CTRLLEVEL_CHANGE_RESPONSE",
    "DISPID_RDPSRAPI_EVENT_ON_ERROR",
    "DISPID_RDPSRAPI_EVENT_ON_FOCUSRELEASED",
    "DISPID_RDPSRAPI_EVENT_ON_GRAPHICS_STREAM_PAUSED",
    "DISPID_RDPSRAPI_EVENT_ON_GRAPHICS_STREAM_RESUMED",
    "DISPID_RDPSRAPI_EVENT_ON_SHARED_DESKTOP_SETTINGS_CHANGED",
    "DISPID_RDPSRAPI_EVENT_ON_SHARED_RECT_CHANGED",
    "DISPID_RDPSRAPI_EVENT_ON_STREAM_CLOSED",
    "DISPID_RDPSRAPI_EVENT_ON_STREAM_DATARECEIVED",
    "DISPID_RDPSRAPI_EVENT_ON_STREAM_SENDCOMPLETED",
    "DISPID_RDPSRAPI_EVENT_ON_VIEWER_AUTHENTICATED",
    "DISPID_RDPSRAPI_EVENT_ON_VIEWER_CONNECTED",
    "DISPID_RDPSRAPI_EVENT_ON_VIEWER_CONNECTFAILED",
    "DISPID_RDPSRAPI_EVENT_ON_VIEWER_DISCONNECTED",
    "DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_DATARECEIVED",
    "DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_JOIN",
    "DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_LEAVE",
    "DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_SENDCOMPLETED",
    "DISPID_RDPSRAPI_EVENT_ON_WINDOW_CLOSE",
    "DISPID_RDPSRAPI_EVENT_ON_WINDOW_OPEN",
    "DISPID_RDPSRAPI_EVENT_ON_WINDOW_UPDATE",
    "DISPID_RDPSRAPI_EVENT_VIEW_MOUSE_BUTTON_RECEIVED",
    "DISPID_RDPSRAPI_EVENT_VIEW_MOUSE_MOVE_RECEIVED",
    "DISPID_RDPSRAPI_EVENT_VIEW_MOUSE_WHEEL_RECEIVED",
    "DISPID_RDPSRAPI_METHOD_ADD_TOUCH_INPUT",
    "DISPID_RDPSRAPI_METHOD_BEGIN_TOUCH_FRAME",
    "DISPID_RDPSRAPI_METHOD_CLOSE",
    "DISPID_RDPSRAPI_METHOD_CONNECTTOCLIENT",
    "DISPID_RDPSRAPI_METHOD_CONNECTUSINGTRANSPORTSTREAM",
    "DISPID_RDPSRAPI_METHOD_CREATE_INVITATION",
    "DISPID_RDPSRAPI_METHOD_END_TOUCH_FRAME",
    "DISPID_RDPSRAPI_METHOD_GETFRAMEBUFFERBITS",
    "DISPID_RDPSRAPI_METHOD_GETSHAREDRECT",
    "DISPID_RDPSRAPI_METHOD_OPEN",
    "DISPID_RDPSRAPI_METHOD_PAUSE",
    "DISPID_RDPSRAPI_METHOD_REQUEST_COLOR_DEPTH_CHANGE",
    "DISPID_RDPSRAPI_METHOD_REQUEST_CONTROL",
    "DISPID_RDPSRAPI_METHOD_RESUME",
    "DISPID_RDPSRAPI_METHOD_SENDCONTROLLEVELCHANGERESPONSE",
    "DISPID_RDPSRAPI_METHOD_SEND_KEYBOARD_EVENT",
    "DISPID_RDPSRAPI_METHOD_SEND_MOUSE_BUTTON_EVENT",
    "DISPID_RDPSRAPI_METHOD_SEND_MOUSE_MOVE_EVENT",
    "DISPID_RDPSRAPI_METHOD_SEND_MOUSE_WHEEL_EVENT",
    "DISPID_RDPSRAPI_METHOD_SEND_SYNC_EVENT",
    "DISPID_RDPSRAPI_METHOD_SETSHAREDRECT",
    "DISPID_RDPSRAPI_METHOD_SET_RENDERING_SURFACE",
    "DISPID_RDPSRAPI_METHOD_SHOW_WINDOW",
    "DISPID_RDPSRAPI_METHOD_STARTREVCONNECTLISTENER",
    "DISPID_RDPSRAPI_METHOD_STREAMCLOSE",
    "DISPID_RDPSRAPI_METHOD_STREAMOPEN",
    "DISPID_RDPSRAPI_METHOD_STREAMREADDATA",
    "DISPID_RDPSRAPI_METHOD_STREAMSENDDATA",
    "DISPID_RDPSRAPI_METHOD_STREAM_ALLOCBUFFER",
    "DISPID_RDPSRAPI_METHOD_STREAM_FREEBUFFER",
    "DISPID_RDPSRAPI_METHOD_TERMINATE_CONNECTION",
    "DISPID_RDPSRAPI_METHOD_VIEWERCONNECT",
    "DISPID_RDPSRAPI_METHOD_VIEWERDISCONNECT",
    "DISPID_RDPSRAPI_METHOD_VIRTUAL_CHANNEL_CREATE",
    "DISPID_RDPSRAPI_METHOD_VIRTUAL_CHANNEL_SEND_DATA",
    "DISPID_RDPSRAPI_METHOD_VIRTUAL_CHANNEL_SET_ACCESS",
    "DISPID_RDPSRAPI_PROP_APPFILTERENABLED",
    "DISPID_RDPSRAPI_PROP_APPFILTER_ENABLED",
    "DISPID_RDPSRAPI_PROP_APPFLAGS",
    "DISPID_RDPSRAPI_PROP_APPLICATION",
    "DISPID_RDPSRAPI_PROP_APPLICATION_FILTER",
    "DISPID_RDPSRAPI_PROP_APPLICATION_LIST",
    "DISPID_RDPSRAPI_PROP_APPNAME",
    "DISPID_RDPSRAPI_PROP_ATTENDEELIMIT",
    "DISPID_RDPSRAPI_PROP_ATTENDEES",
    "DISPID_RDPSRAPI_PROP_ATTENDEE_FLAGS",
    "DISPID_RDPSRAPI_PROP_CHANNELMANAGER",
    "DISPID_RDPSRAPI_PROP_CODE",
    "DISPID_RDPSRAPI_PROP_CONINFO",
    "DISPID_RDPSRAPI_PROP_CONNECTION_STRING",
    "DISPID_RDPSRAPI_PROP_COUNT",
    "DISPID_RDPSRAPI_PROP_CTRL_LEVEL",
    "DISPID_RDPSRAPI_PROP_DBG_CLX_CMDLINE",
    "DISPID_RDPSRAPI_PROP_DISCONNECTED_STRING",
    "DISPID_RDPSRAPI_PROP_DISPIDVALUE",
    "DISPID_RDPSRAPI_PROP_FRAMEBUFFER",
    "DISPID_RDPSRAPI_PROP_FRAMEBUFFER_BPP",
    "DISPID_RDPSRAPI_PROP_FRAMEBUFFER_HEIGHT",
    "DISPID_RDPSRAPI_PROP_FRAMEBUFFER_WIDTH",
    "DISPID_RDPSRAPI_PROP_GROUP_NAME",
    "DISPID_RDPSRAPI_PROP_ID",
    "DISPID_RDPSRAPI_PROP_INVITATION",
    "DISPID_RDPSRAPI_PROP_INVITATIONITEM",
    "DISPID_RDPSRAPI_PROP_INVITATIONS",
    "DISPID_RDPSRAPI_PROP_LOCAL_IP",
    "DISPID_RDPSRAPI_PROP_LOCAL_PORT",
    "DISPID_RDPSRAPI_PROP_PASSWORD",
    "DISPID_RDPSRAPI_PROP_PEER_IP",
    "DISPID_RDPSRAPI_PROP_PEER_PORT",
    "DISPID_RDPSRAPI_PROP_PROTOCOL_TYPE",
    "DISPID_RDPSRAPI_PROP_REASON",
    "DISPID_RDPSRAPI_PROP_REMOTENAME",
    "DISPID_RDPSRAPI_PROP_REVOKED",
    "DISPID_RDPSRAPI_PROP_SESSION_COLORDEPTH",
    "DISPID_RDPSRAPI_PROP_SESSION_PROPERTIES",
    "DISPID_RDPSRAPI_PROP_SHARED",
    "DISPID_RDPSRAPI_PROP_STREAMBUFFER_CONTEXT",
    "DISPID_RDPSRAPI_PROP_STREAMBUFFER_FLAGS",
    "DISPID_RDPSRAPI_PROP_STREAMBUFFER_PAYLOADOFFSET",
    "DISPID_RDPSRAPI_PROP_STREAMBUFFER_PAYLOADSIZE",
    "DISPID_RDPSRAPI_PROP_STREAMBUFFER_STORAGE",
    "DISPID_RDPSRAPI_PROP_STREAMBUFFER_STORESIZE",
    "DISPID_RDPSRAPI_PROP_USESMARTSIZING",
    "DISPID_RDPSRAPI_PROP_VIRTUAL_CHANNEL_GETFLAGS",
    "DISPID_RDPSRAPI_PROP_VIRTUAL_CHANNEL_GETNAME",
    "DISPID_RDPSRAPI_PROP_VIRTUAL_CHANNEL_GETPRIORITY",
    "DISPID_RDPSRAPI_PROP_WINDOWID",
    "DISPID_RDPSRAPI_PROP_WINDOWNAME",
    "DISPID_RDPSRAPI_PROP_WINDOWSHARED",
    "DISPID_RDPSRAPI_PROP_WINDOW_LIST",
    "DISPID_RDPSRAPI_PROP_WNDFLAGS",
    "IRDPSRAPIApplication",
    "IRDPSRAPIApplicationFilter",
    "IRDPSRAPIApplicationList",
    "IRDPSRAPIAttendee",
    "IRDPSRAPIAttendeeDisconnectInfo",
    "IRDPSRAPIAttendeeManager",
    "IRDPSRAPIAudioStream",
    "IRDPSRAPIClipboardUseEvents",
    "IRDPSRAPIDebug",
    "IRDPSRAPIFrameBuffer",
    "IRDPSRAPIInvitation",
    "IRDPSRAPIInvitationManager",
    "IRDPSRAPIPerfCounterLogger",
    "IRDPSRAPIPerfCounterLoggingManager",
    "IRDPSRAPISessionProperties",
    "IRDPSRAPISharingSession",
    "IRDPSRAPISharingSession2",
    "IRDPSRAPITcpConnectionInfo",
    "IRDPSRAPITransportStream",
    "IRDPSRAPITransportStreamBuffer",
    "IRDPSRAPITransportStreamEvents",
    "IRDPSRAPIViewer",
    "IRDPSRAPIVirtualChannel",
    "IRDPSRAPIVirtualChannelManager",
    "IRDPSRAPIWindow",
    "IRDPSRAPIWindowList",
    "IRDPViewerInputSink",
    "RDPENCOMAPI_ATTENDEE_FLAGS",
    "RDPENCOMAPI_CONSTANTS",
    "RDPSRAPIApplication",
    "RDPSRAPIApplicationFilter",
    "RDPSRAPIApplicationList",
    "RDPSRAPIAttendee",
    "RDPSRAPIAttendeeDisconnectInfo",
    "RDPSRAPIAttendeeManager",
    "RDPSRAPIFrameBuffer",
    "RDPSRAPIInvitation",
    "RDPSRAPIInvitationManager",
    "RDPSRAPISessionProperties",
    "RDPSRAPITcpConnectionInfo",
    "RDPSRAPIWindow",
    "RDPSRAPIWindowList",
    "RDPSRAPI_APP_FLAGS",
    "RDPSRAPI_KBD_CODE_SCANCODE",
    "RDPSRAPI_KBD_CODE_TYPE",
    "RDPSRAPI_KBD_CODE_UNICODE",
    "RDPSRAPI_KBD_SYNC_FLAG",
    "RDPSRAPI_KBD_SYNC_FLAG_CAPS_LOCK",
    "RDPSRAPI_KBD_SYNC_FLAG_KANA_LOCK",
    "RDPSRAPI_KBD_SYNC_FLAG_NUM_LOCK",
    "RDPSRAPI_KBD_SYNC_FLAG_SCROLL_LOCK",
    "RDPSRAPI_MOUSE_BUTTON_BUTTON1",
    "RDPSRAPI_MOUSE_BUTTON_BUTTON2",
    "RDPSRAPI_MOUSE_BUTTON_BUTTON3",
    "RDPSRAPI_MOUSE_BUTTON_TYPE",
    "RDPSRAPI_MOUSE_BUTTON_XBUTTON1",
    "RDPSRAPI_MOUSE_BUTTON_XBUTTON2",
    "RDPSRAPI_MOUSE_BUTTON_XBUTTON3",
    "RDPSRAPI_WND_FLAGS",
    "RDPSession",
    "RDPTransportStreamBuffer",
    "RDPTransportStreamEvents",
    "RDPViewer",
    "WND_FLAG_PRIVILEGED",
    "_IRDPSessionEvents",
    "__ReferenceRemainingTypes__",
]
