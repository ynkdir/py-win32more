from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.DesktopSharing
import win32more.Windows.Win32.System.Variant
ATTENDEE_DISCONNECT_REASON = Int32
ATTENDEE_DISCONNECT_REASON_MIN: win32more.Windows.Win32.System.DesktopSharing.ATTENDEE_DISCONNECT_REASON = 0
ATTENDEE_DISCONNECT_REASON_APP: win32more.Windows.Win32.System.DesktopSharing.ATTENDEE_DISCONNECT_REASON = 0
ATTENDEE_DISCONNECT_REASON_ERR: win32more.Windows.Win32.System.DesktopSharing.ATTENDEE_DISCONNECT_REASON = 1
ATTENDEE_DISCONNECT_REASON_CLI: win32more.Windows.Win32.System.DesktopSharing.ATTENDEE_DISCONNECT_REASON = 2
ATTENDEE_DISCONNECT_REASON_MAX: win32more.Windows.Win32.System.DesktopSharing.ATTENDEE_DISCONNECT_REASON = 2
DISPID_RDPSRAPI_METHOD_OPEN: UInt32 = 100
DISPID_RDPSRAPI_METHOD_CLOSE: UInt32 = 101
DISPID_RDPSRAPI_METHOD_SETSHAREDRECT: UInt32 = 102
DISPID_RDPSRAPI_METHOD_GETSHAREDRECT: UInt32 = 103
DISPID_RDPSRAPI_METHOD_VIEWERCONNECT: UInt32 = 104
DISPID_RDPSRAPI_METHOD_VIEWERDISCONNECT: UInt32 = 105
DISPID_RDPSRAPI_METHOD_TERMINATE_CONNECTION: UInt32 = 106
DISPID_RDPSRAPI_METHOD_CREATE_INVITATION: UInt32 = 107
DISPID_RDPSRAPI_METHOD_REQUEST_CONTROL: UInt32 = 108
DISPID_RDPSRAPI_METHOD_VIRTUAL_CHANNEL_CREATE: UInt32 = 109
DISPID_RDPSRAPI_METHOD_VIRTUAL_CHANNEL_SEND_DATA: UInt32 = 110
DISPID_RDPSRAPI_METHOD_VIRTUAL_CHANNEL_SET_ACCESS: UInt32 = 111
DISPID_RDPSRAPI_METHOD_PAUSE: UInt32 = 112
DISPID_RDPSRAPI_METHOD_RESUME: UInt32 = 113
DISPID_RDPSRAPI_METHOD_SHOW_WINDOW: UInt32 = 114
DISPID_RDPSRAPI_METHOD_REQUEST_COLOR_DEPTH_CHANGE: UInt32 = 115
DISPID_RDPSRAPI_METHOD_STARTREVCONNECTLISTENER: UInt32 = 116
DISPID_RDPSRAPI_METHOD_CONNECTTOCLIENT: UInt32 = 117
DISPID_RDPSRAPI_METHOD_SET_RENDERING_SURFACE: UInt32 = 118
DISPID_RDPSRAPI_METHOD_SEND_MOUSE_BUTTON_EVENT: UInt32 = 119
DISPID_RDPSRAPI_METHOD_SEND_MOUSE_MOVE_EVENT: UInt32 = 120
DISPID_RDPSRAPI_METHOD_SEND_MOUSE_WHEEL_EVENT: UInt32 = 121
DISPID_RDPSRAPI_METHOD_SEND_KEYBOARD_EVENT: UInt32 = 122
DISPID_RDPSRAPI_METHOD_SEND_SYNC_EVENT: UInt32 = 123
DISPID_RDPSRAPI_METHOD_BEGIN_TOUCH_FRAME: UInt32 = 124
DISPID_RDPSRAPI_METHOD_ADD_TOUCH_INPUT: UInt32 = 125
DISPID_RDPSRAPI_METHOD_END_TOUCH_FRAME: UInt32 = 126
DISPID_RDPSRAPI_METHOD_CONNECTUSINGTRANSPORTSTREAM: UInt32 = 127
DISPID_RDPSRAPI_METHOD_SENDCONTROLLEVELCHANGERESPONSE: UInt32 = 148
DISPID_RDPSRAPI_METHOD_GETFRAMEBUFFERBITS: UInt32 = 149
DISPID_RDPSRAPI_PROP_DISPIDVALUE: UInt32 = 200
DISPID_RDPSRAPI_PROP_ID: UInt32 = 201
DISPID_RDPSRAPI_PROP_SESSION_PROPERTIES: UInt32 = 202
DISPID_RDPSRAPI_PROP_ATTENDEES: UInt32 = 203
DISPID_RDPSRAPI_PROP_INVITATIONS: UInt32 = 204
DISPID_RDPSRAPI_PROP_INVITATION: UInt32 = 205
DISPID_RDPSRAPI_PROP_CHANNELMANAGER: UInt32 = 206
DISPID_RDPSRAPI_PROP_VIRTUAL_CHANNEL_GETNAME: UInt32 = 207
DISPID_RDPSRAPI_PROP_VIRTUAL_CHANNEL_GETFLAGS: UInt32 = 208
DISPID_RDPSRAPI_PROP_VIRTUAL_CHANNEL_GETPRIORITY: UInt32 = 209
DISPID_RDPSRAPI_PROP_WINDOWID: UInt32 = 210
DISPID_RDPSRAPI_PROP_APPLICATION: UInt32 = 211
DISPID_RDPSRAPI_PROP_WINDOWSHARED: UInt32 = 212
DISPID_RDPSRAPI_PROP_WINDOWNAME: UInt32 = 213
DISPID_RDPSRAPI_PROP_APPNAME: UInt32 = 214
DISPID_RDPSRAPI_PROP_APPLICATION_FILTER: UInt32 = 215
DISPID_RDPSRAPI_PROP_WINDOW_LIST: UInt32 = 216
DISPID_RDPSRAPI_PROP_APPLICATION_LIST: UInt32 = 217
DISPID_RDPSRAPI_PROP_APPFILTER_ENABLED: UInt32 = 218
DISPID_RDPSRAPI_PROP_APPFILTERENABLED: UInt32 = 219
DISPID_RDPSRAPI_PROP_SHARED: UInt32 = 220
DISPID_RDPSRAPI_PROP_INVITATIONITEM: UInt32 = 221
DISPID_RDPSRAPI_PROP_DBG_CLX_CMDLINE: UInt32 = 222
DISPID_RDPSRAPI_PROP_APPFLAGS: UInt32 = 223
DISPID_RDPSRAPI_PROP_WNDFLAGS: UInt32 = 224
DISPID_RDPSRAPI_PROP_PROTOCOL_TYPE: UInt32 = 225
DISPID_RDPSRAPI_PROP_LOCAL_PORT: UInt32 = 226
DISPID_RDPSRAPI_PROP_LOCAL_IP: UInt32 = 227
DISPID_RDPSRAPI_PROP_PEER_PORT: UInt32 = 228
DISPID_RDPSRAPI_PROP_PEER_IP: UInt32 = 229
DISPID_RDPSRAPI_PROP_ATTENDEE_FLAGS: UInt32 = 230
DISPID_RDPSRAPI_PROP_CONINFO: UInt32 = 231
DISPID_RDPSRAPI_PROP_CONNECTION_STRING: UInt32 = 232
DISPID_RDPSRAPI_PROP_GROUP_NAME: UInt32 = 233
DISPID_RDPSRAPI_PROP_PASSWORD: UInt32 = 234
DISPID_RDPSRAPI_PROP_ATTENDEELIMIT: UInt32 = 235
DISPID_RDPSRAPI_PROP_REVOKED: UInt32 = 236
DISPID_RDPSRAPI_PROP_DISCONNECTED_STRING: UInt32 = 237
DISPID_RDPSRAPI_PROP_USESMARTSIZING: UInt32 = 238
DISPID_RDPSRAPI_PROP_SESSION_COLORDEPTH: UInt32 = 239
DISPID_RDPSRAPI_PROP_REASON: UInt32 = 240
DISPID_RDPSRAPI_PROP_CODE: UInt32 = 241
DISPID_RDPSRAPI_PROP_CTRL_LEVEL: UInt32 = 242
DISPID_RDPSRAPI_PROP_REMOTENAME: UInt32 = 243
DISPID_RDPSRAPI_PROP_COUNT: UInt32 = 244
DISPID_RDPSRAPI_PROP_FRAMEBUFFER_HEIGHT: UInt32 = 251
DISPID_RDPSRAPI_PROP_FRAMEBUFFER_WIDTH: UInt32 = 252
DISPID_RDPSRAPI_PROP_FRAMEBUFFER_BPP: UInt32 = 253
DISPID_RDPSRAPI_PROP_FRAMEBUFFER: UInt32 = 254
DISPID_RDPSRAPI_EVENT_ON_ATTENDEE_CONNECTED: UInt32 = 301
DISPID_RDPSRAPI_EVENT_ON_ATTENDEE_DISCONNECTED: UInt32 = 302
DISPID_RDPSRAPI_EVENT_ON_ATTENDEE_UPDATE: UInt32 = 303
DISPID_RDPSRAPI_EVENT_ON_ERROR: UInt32 = 304
DISPID_RDPSRAPI_EVENT_ON_VIEWER_CONNECTED: UInt32 = 305
DISPID_RDPSRAPI_EVENT_ON_VIEWER_DISCONNECTED: UInt32 = 306
DISPID_RDPSRAPI_EVENT_ON_VIEWER_AUTHENTICATED: UInt32 = 307
DISPID_RDPSRAPI_EVENT_ON_VIEWER_CONNECTFAILED: UInt32 = 308
DISPID_RDPSRAPI_EVENT_ON_CTRLLEVEL_CHANGE_REQUEST: UInt32 = 309
DISPID_RDPSRAPI_EVENT_ON_GRAPHICS_STREAM_PAUSED: UInt32 = 310
DISPID_RDPSRAPI_EVENT_ON_GRAPHICS_STREAM_RESUMED: UInt32 = 311
DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_JOIN: UInt32 = 312
DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_LEAVE: UInt32 = 313
DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_DATARECEIVED: UInt32 = 314
DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_SENDCOMPLETED: UInt32 = 315
DISPID_RDPSRAPI_EVENT_ON_APPLICATION_OPEN: UInt32 = 316
DISPID_RDPSRAPI_EVENT_ON_APPLICATION_CLOSE: UInt32 = 317
DISPID_RDPSRAPI_EVENT_ON_APPLICATION_UPDATE: UInt32 = 318
DISPID_RDPSRAPI_EVENT_ON_WINDOW_OPEN: UInt32 = 319
DISPID_RDPSRAPI_EVENT_ON_WINDOW_CLOSE: UInt32 = 320
DISPID_RDPSRAPI_EVENT_ON_WINDOW_UPDATE: UInt32 = 321
DISPID_RDPSRAPI_EVENT_ON_APPFILTER_UPDATE: UInt32 = 322
DISPID_RDPSRAPI_EVENT_ON_SHARED_RECT_CHANGED: UInt32 = 323
DISPID_RDPSRAPI_EVENT_ON_FOCUSRELEASED: UInt32 = 324
DISPID_RDPSRAPI_EVENT_ON_SHARED_DESKTOP_SETTINGS_CHANGED: UInt32 = 325
DISPID_RDPSRAPI_EVENT_ON_CTRLLEVEL_CHANGE_RESPONSE: UInt32 = 338
DISPID_RDPAPI_EVENT_ON_BOUNDING_RECT_CHANGED: UInt32 = 340
DISPID_RDPSRAPI_METHOD_STREAM_ALLOCBUFFER: UInt32 = 421
DISPID_RDPSRAPI_METHOD_STREAM_FREEBUFFER: UInt32 = 422
DISPID_RDPSRAPI_METHOD_STREAMSENDDATA: UInt32 = 423
DISPID_RDPSRAPI_METHOD_STREAMREADDATA: UInt32 = 424
DISPID_RDPSRAPI_METHOD_STREAMOPEN: UInt32 = 425
DISPID_RDPSRAPI_METHOD_STREAMCLOSE: UInt32 = 426
DISPID_RDPSRAPI_PROP_STREAMBUFFER_STORAGE: UInt32 = 555
DISPID_RDPSRAPI_PROP_STREAMBUFFER_PAYLOADSIZE: UInt32 = 558
DISPID_RDPSRAPI_PROP_STREAMBUFFER_PAYLOADOFFSET: UInt32 = 559
DISPID_RDPSRAPI_PROP_STREAMBUFFER_CONTEXT: UInt32 = 560
DISPID_RDPSRAPI_PROP_STREAMBUFFER_FLAGS: UInt32 = 561
DISPID_RDPSRAPI_PROP_STREAMBUFFER_STORESIZE: UInt32 = 562
DISPID_RDPSRAPI_EVENT_ON_STREAM_SENDCOMPLETED: UInt32 = 632
DISPID_RDPSRAPI_EVENT_ON_STREAM_DATARECEIVED: UInt32 = 633
DISPID_RDPSRAPI_EVENT_ON_STREAM_CLOSED: UInt32 = 634
DISPID_RDPSRAPI_EVENT_VIEW_MOUSE_BUTTON_RECEIVED: UInt32 = 700
DISPID_RDPSRAPI_EVENT_VIEW_MOUSE_MOVE_RECEIVED: UInt32 = 701
DISPID_RDPSRAPI_EVENT_VIEW_MOUSE_WHEEL_RECEIVED: UInt32 = 702
CHANNEL_ACCESS_ENUM = Int32
CHANNEL_ACCESS_ENUM_NONE: win32more.Windows.Win32.System.DesktopSharing.CHANNEL_ACCESS_ENUM = 0
CHANNEL_ACCESS_ENUM_SENDRECEIVE: win32more.Windows.Win32.System.DesktopSharing.CHANNEL_ACCESS_ENUM = 1
CHANNEL_FLAGS = Int32
CHANNEL_FLAGS_LEGACY: win32more.Windows.Win32.System.DesktopSharing.CHANNEL_FLAGS = 1
CHANNEL_FLAGS_UNCOMPRESSED: win32more.Windows.Win32.System.DesktopSharing.CHANNEL_FLAGS = 2
CHANNEL_FLAGS_DYNAMIC: win32more.Windows.Win32.System.DesktopSharing.CHANNEL_FLAGS = 4
CHANNEL_PRIORITY = Int32
CHANNEL_PRIORITY_LO: win32more.Windows.Win32.System.DesktopSharing.CHANNEL_PRIORITY = 0
CHANNEL_PRIORITY_MED: win32more.Windows.Win32.System.DesktopSharing.CHANNEL_PRIORITY = 1
CHANNEL_PRIORITY_HI: win32more.Windows.Win32.System.DesktopSharing.CHANNEL_PRIORITY = 2
CTRL_LEVEL = Int32
CTRL_LEVEL_MIN: win32more.Windows.Win32.System.DesktopSharing.CTRL_LEVEL = 0
CTRL_LEVEL_INVALID: win32more.Windows.Win32.System.DesktopSharing.CTRL_LEVEL = 0
CTRL_LEVEL_NONE: win32more.Windows.Win32.System.DesktopSharing.CTRL_LEVEL = 1
CTRL_LEVEL_VIEW: win32more.Windows.Win32.System.DesktopSharing.CTRL_LEVEL = 2
CTRL_LEVEL_INTERACTIVE: win32more.Windows.Win32.System.DesktopSharing.CTRL_LEVEL = 3
CTRL_LEVEL_REQCTRL_VIEW: win32more.Windows.Win32.System.DesktopSharing.CTRL_LEVEL = 4
CTRL_LEVEL_REQCTRL_INTERACTIVE: win32more.Windows.Win32.System.DesktopSharing.CTRL_LEVEL = 5
CTRL_LEVEL_MAX: win32more.Windows.Win32.System.DesktopSharing.CTRL_LEVEL = 5
class IRDPSRAPIApplication(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{41e7a09d-eb7a-436e-935d-780ca2628324}')
    @commethod(7)
    def get_Windows(self, pWindowList: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIWindowList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Shared(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Shared(self, NewVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Name(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Flags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIApplicationFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d20f10ca-6637-4f06-b1d5-277ea7e5160d}')
    @commethod(7)
    def get_Applications(self, pApplications: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIApplicationList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Windows(self, pWindows: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIWindowList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Enabled(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Enabled(self, NewVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIApplicationList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d4b4aeb3-22dc-4837-b3b6-42ea2517849a}')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, item: Int32, pApplication: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIApplication)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIAttendee(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ec0671b3-1b78-4b80-a464-9132247543e3}')
    @commethod(7)
    def get_Id(self, pId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RemoteName(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ControlLevel(self, pVal: POINTER(win32more.Windows.Win32.System.DesktopSharing.CTRL_LEVEL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ControlLevel(self, pNewVal: win32more.Windows.Win32.System.DesktopSharing.CTRL_LEVEL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Invitation(self, ppVal: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIInvitation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def TerminateConnection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Flags(self, plFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ConnectivityInfo(self, ppVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIAttendeeDisconnectInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c187689f-447c-44a1-9c14-fffbb3b7ec17}')
    @commethod(7)
    def get_Attendee(self, retval: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIAttendee)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Reason(self, pReason: POINTER(win32more.Windows.Win32.System.DesktopSharing.ATTENDEE_DISCONNECT_REASON)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Code(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIAttendeeManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ba3a37e8-33da-4749-8da0-07fa34da7944}')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, id: Int32, ppItem: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIAttendee)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIAudioStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e3e30ef9-89c6-4541-ba3b-19336ac6d31c}')
    @commethod(3)
    def Initialize(self, pnPeriodInHundredNsIntervals: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Start(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBuffer(self, ppbData: POINTER(POINTER(Byte)), pcbData: POINTER(UInt32), pTimestamp: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FreeBuffer(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIClipboardUseEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d559f59a-7a27-4138-8763-247ce5f659a8}')
    @commethod(3)
    def OnPasteFromClipboard(self, clipboardFormat: UInt32, pAttendee: win32more.Windows.Win32.System.Com.IDispatch, pRetVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIDebug(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa1e42b5-496d-4ca4-a690-348dcb2ec4ad}')
    @commethod(3)
    def put_CLXCmdLine(self, CLXCmdLine: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CLXCmdLine(self, pCLXCmdLine: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIFrameBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3d67e7d2-b27b-448e-81b3-c6110ed8b4be}')
    @commethod(7)
    def get_Width(self, plWidth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Height(self, plHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Bpp(self, plBpp: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFrameBufferBits(self, x: Int32, y: Int32, Width: Int32, Heigth: Int32, ppBits: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIInvitation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4fac1d43-fc51-45bb-b1b4-2b53aa562fa3}')
    @commethod(7)
    def get_ConnectionString(self, pbstrVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_GroupName(self, pbstrVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Password(self, pbstrVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AttendeeLimit(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_AttendeeLimit(self, NewVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Revoked(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Revoked(self, NewVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIInvitationManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4722b049-92c3-4c2d-8a65-f7348f644dcf}')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, item: win32more.Windows.Win32.System.Variant.VARIANT, ppInvitation: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIInvitation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateInvitation(self, bstrAuthString: win32more.Windows.Win32.Foundation.BSTR, bstrGroupName: win32more.Windows.Win32.Foundation.BSTR, bstrPassword: win32more.Windows.Win32.Foundation.BSTR, AttendeeLimit: Int32, ppInvitation: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIInvitation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIPerfCounterLogger(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{071c2533-0fa4-4e8f-ae83-9c10b4305ab5}')
    @commethod(3)
    def LogValue(self, lValue: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIPerfCounterLoggingManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9a512c86-ac6e-4a8e-b1a4-fcef363f6e64}')
    @commethod(3)
    def CreateLogger(self, bstrCounterName: win32more.Windows.Win32.Foundation.BSTR, ppLogger: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIPerfCounterLogger)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPISessionProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{339b24f2-9bc0-4f16-9aac-f165433d13d4}')
    @commethod(7)
    def get_Property(self, PropertyName: win32more.Windows.Win32.Foundation.BSTR, pVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Property(self, PropertyName: win32more.Windows.Win32.Foundation.BSTR, newVal: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPISharingSession(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{eeb20886-e470-4cf6-842b-2739c0ec5cfb}')
    @commethod(7)
    def Open(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_ColorDepth(self, colorDepth: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ColorDepth(self, pColorDepth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Properties(self, ppVal: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPISessionProperties)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Attendees(self, ppVal: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIAttendeeManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Invitations(self, ppVal: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIInvitationManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ApplicationFilter(self, ppVal: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIApplicationFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_VirtualChannelManager(self, ppVal: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIVirtualChannelManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ConnectToClient(self, bstrConnectionString: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetDesktopSharedRect(self, left: Int32, top: Int32, right: Int32, bottom: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDesktopSharedRect(self, pleft: POINTER(Int32), ptop: POINTER(Int32), pright: POINTER(Int32), pbottom: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPISharingSession2(ComPtr):
    extends: win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPISharingSession
    _iid_ = Guid('{fee4ee57-e3e8-4205-8fb0-8fd1d0675c21}')
    @commethod(21)
    def ConnectUsingTransportStream(self, pStream: win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStream, bstrGroup: win32more.Windows.Win32.Foundation.BSTR, bstrAuthenticatedAttendeeName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_FrameBuffer(self, ppVal: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIFrameBuffer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SendControlLevelChangeResponse(self, pAttendee: win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIAttendee, RequestedLevel: win32more.Windows.Win32.System.DesktopSharing.CTRL_LEVEL, ReasonCode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPITcpConnectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f74049a4-3d06-4028-8193-0a8c29bc2452}')
    @commethod(7)
    def get_Protocol(self, plProtocol: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LocalPort(self, plPort: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LocalIP(self, pbsrLocalIP: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PeerPort(self, plPort: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PeerIP(self, pbstrIP: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPITransportStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{36cfa065-43bb-4ef7-aed7-9b88a5053036}')
    @commethod(3)
    def AllocBuffer(self, maxPayload: Int32, ppBuffer: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamBuffer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FreeBuffer(self, pBuffer: win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WriteBuffer(self, pBuffer: win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReadBuffer(self, pBuffer: win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Open(self, pCallbacks: win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamEvents) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPITransportStreamBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{81c80290-5085-44b0-b460-f865c39cb4a9}')
    @commethod(3)
    def get_Storage(self, ppbStorage: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_StorageSize(self, plMaxStore: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_PayloadSize(self, plRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_PayloadSize(self, lVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_PayloadOffset(self, plRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_PayloadOffset(self, lRetVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Flags(self, plFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Flags(self, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Context(self, ppContext: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Context(self, pContext: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPITransportStreamEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ea81c254-f5af-4e40-982e-3e63bb595276}')
    @commethod(3)
    def OnWriteCompleted(self, pBuffer: win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamBuffer) -> Void: ...
    @commethod(4)
    def OnReadCompleted(self, pBuffer: win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamBuffer) -> Void: ...
    @commethod(5)
    def OnStreamClosed(self, hrReason: win32more.Windows.Win32.Foundation.HRESULT) -> Void: ...
class IRDPSRAPIViewer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c6bfcd38-8ce9-404d-8ae8-f31d00c65cb5}')
    @commethod(7)
    def Connect(self, bstrConnectionString: win32more.Windows.Win32.Foundation.BSTR, bstrName: win32more.Windows.Win32.Foundation.BSTR, bstrPassword: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Disconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Attendees(self, ppVal: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIAttendeeManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Invitations(self, ppVal: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIInvitationManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationFilter(self, ppVal: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIApplicationFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_VirtualChannelManager(self, ppVal: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIVirtualChannelManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_SmartSizing(self, vbSmartSizing: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_SmartSizing(self, pvbSmartSizing: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RequestControl(self, CtrlLevel: win32more.Windows.Win32.System.DesktopSharing.CTRL_LEVEL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_DisconnectedText(self, bstrDisconnectedText: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_DisconnectedText(self, pbstrDisconnectedText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RequestColorDepthChange(self, Bpp: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Properties(self, ppVal: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPISessionProperties)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def StartReverseConnectListener(self, bstrConnectionString: win32more.Windows.Win32.Foundation.BSTR, bstrUserName: win32more.Windows.Win32.Foundation.BSTR, bstrPassword: win32more.Windows.Win32.Foundation.BSTR, pbstrReverseConnectString: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIVirtualChannel(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{05e12f95-28b3-4c9a-8780-d0248574a1e0}')
    @commethod(7)
    def SendData(self, bstrData: win32more.Windows.Win32.Foundation.BSTR, lAttendeeId: Int32, ChannelSendFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetAccess(self, lAttendeeId: Int32, AccessType: win32more.Windows.Win32.System.DesktopSharing.CHANNEL_ACCESS_ENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Flags(self, plFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Priority(self, pPriority: POINTER(win32more.Windows.Win32.System.DesktopSharing.CHANNEL_PRIORITY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIVirtualChannelManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0d11c661-5d0d-4ee4-89df-2166ae1fdfed}')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, item: win32more.Windows.Win32.System.Variant.VARIANT, pChannel: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIVirtualChannel)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateVirtualChannel(self, bstrChannelName: win32more.Windows.Win32.Foundation.BSTR, Priority: win32more.Windows.Win32.System.DesktopSharing.CHANNEL_PRIORITY, ChannelFlags: UInt32, ppChannel: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIVirtualChannel)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIWindow(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{beafe0f9-c77b-4933-ba9f-a24cddcc27cf}')
    @commethod(7)
    def get_Id(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Application(self, pApplication: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIApplication)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Shared(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Shared(self, NewVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Name(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Show(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Flags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIWindowList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8a05ce44-715a-4116-a189-a118f30a07bd}')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, item: Int32, pWindow: POINTER(win32more.Windows.Win32.System.DesktopSharing.IRDPSRAPIWindow)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRDPViewerInputSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb590853-a6c5-4a7b-8dd4-76b69eea12d5}')
    @commethod(3)
    def SendMouseButtonEvent(self, buttonType: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_MOUSE_BUTTON_TYPE, vbButtonDown: win32more.Windows.Win32.Foundation.VARIANT_BOOL, xPos: UInt32, yPos: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendMouseMoveEvent(self, xPos: UInt32, yPos: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SendMouseWheelEvent(self, wheelRotation: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SendKeyboardEvent(self, codeType: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_KBD_CODE_TYPE, keycode: UInt16, vbKeyUp: win32more.Windows.Win32.Foundation.VARIANT_BOOL, vbRepeat: win32more.Windows.Win32.Foundation.VARIANT_BOOL, vbExtended: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SendSyncEvent(self, syncFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def BeginTouchFrame(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddTouchInput(self, contactId: UInt32, event: UInt32, x: Int32, y: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EndTouchFrame(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
RDPENCOMAPI_ATTENDEE_FLAGS = Int32
ATTENDEE_FLAGS_LOCAL: win32more.Windows.Win32.System.DesktopSharing.RDPENCOMAPI_ATTENDEE_FLAGS = 1
RDPENCOMAPI_CONSTANTS = Int32
CONST_MAX_CHANNEL_MESSAGE_SIZE: win32more.Windows.Win32.System.DesktopSharing.RDPENCOMAPI_CONSTANTS = 1024
CONST_MAX_CHANNEL_NAME_LEN: win32more.Windows.Win32.System.DesktopSharing.RDPENCOMAPI_CONSTANTS = 8
CONST_MAX_LEGACY_CHANNEL_MESSAGE_SIZE: win32more.Windows.Win32.System.DesktopSharing.RDPENCOMAPI_CONSTANTS = 409600
CONST_ATTENDEE_ID_EVERYONE: win32more.Windows.Win32.System.DesktopSharing.RDPENCOMAPI_CONSTANTS = -1
CONST_ATTENDEE_ID_HOST: win32more.Windows.Win32.System.DesktopSharing.RDPENCOMAPI_CONSTANTS = 0
CONST_CONN_INTERVAL: win32more.Windows.Win32.System.DesktopSharing.RDPENCOMAPI_CONSTANTS = 50
CONST_ATTENDEE_ID_DEFAULT: win32more.Windows.Win32.System.DesktopSharing.RDPENCOMAPI_CONSTANTS = -1
RDPSRAPIApplication = Guid('{c116a484-4b25-4b9f-8a54-b934b06e57fa}')
RDPSRAPIApplicationFilter = Guid('{e35ace89-c7e8-427e-a4f9-b9da072826bd}')
RDPSRAPIApplicationList = Guid('{9e31c815-7433-4876-97fb-ed59fe2baa22}')
RDPSRAPIAttendee = Guid('{74f93bb5-755f-488e-8a29-2390108aef55}')
RDPSRAPIAttendeeDisconnectInfo = Guid('{b47d7250-5bdb-405d-b487-caad9c56f4f8}')
RDPSRAPIAttendeeManager = Guid('{d7b13a01-f7d4-42a6-8595-12fc8c24e851}')
RDPSRAPIFrameBuffer = Guid('{a4f66bcc-538e-4101-951d-30847adb5101}')
RDPSRAPIInvitation = Guid('{49174dc6-0731-4b5e-8ee1-83a63d3868fa}')
RDPSRAPIInvitationManager = Guid('{53d9c9db-75ab-4271-948a-4c4eb36a8f2b}')
RDPSRAPISessionProperties = Guid('{dd7594ff-ea2a-4c06-8fdf-132de48b6510}')
RDPSRAPITcpConnectionInfo = Guid('{be49db3f-ebb6-4278-8ce0-d5455833eaee}')
RDPSRAPIWindow = Guid('{03cf46db-ce45-4d36-86ed-ed28b74398bf}')
RDPSRAPIWindowList = Guid('{9c21e2b8-5dd4-42cc-81ba-1c099852e6fa}')
RDPSRAPI_APP_FLAGS = Int32
APP_FLAG_PRIVILEGED: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_APP_FLAGS = 1
RDPSRAPI_KBD_CODE_TYPE = Int32
RDPSRAPI_KBD_CODE_SCANCODE: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_KBD_CODE_TYPE = 0
RDPSRAPI_KBD_CODE_UNICODE: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_KBD_CODE_TYPE = 1
RDPSRAPI_KBD_SYNC_FLAG = Int32
RDPSRAPI_KBD_SYNC_FLAG_SCROLL_LOCK: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_KBD_SYNC_FLAG = 1
RDPSRAPI_KBD_SYNC_FLAG_NUM_LOCK: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_KBD_SYNC_FLAG = 2
RDPSRAPI_KBD_SYNC_FLAG_CAPS_LOCK: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_KBD_SYNC_FLAG = 4
RDPSRAPI_KBD_SYNC_FLAG_KANA_LOCK: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_KBD_SYNC_FLAG = 8
RDPSRAPI_MOUSE_BUTTON_TYPE = Int32
RDPSRAPI_MOUSE_BUTTON_BUTTON1: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_MOUSE_BUTTON_TYPE = 0
RDPSRAPI_MOUSE_BUTTON_BUTTON2: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_MOUSE_BUTTON_TYPE = 1
RDPSRAPI_MOUSE_BUTTON_BUTTON3: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_MOUSE_BUTTON_TYPE = 2
RDPSRAPI_MOUSE_BUTTON_XBUTTON1: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_MOUSE_BUTTON_TYPE = 3
RDPSRAPI_MOUSE_BUTTON_XBUTTON2: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_MOUSE_BUTTON_TYPE = 4
RDPSRAPI_MOUSE_BUTTON_XBUTTON3: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_MOUSE_BUTTON_TYPE = 5
RDPSRAPI_WND_FLAGS = Int32
WND_FLAG_PRIVILEGED: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_WND_FLAGS = 1
RDPSession = Guid('{9b78f0e6-3e05-4a5b-b2e8-e743a8956b65}')
RDPTransportStreamBuffer = Guid('{8d4a1c69-f17f-4549-a699-761c6e6b5c0a}')
RDPTransportStreamEvents = Guid('{31e3ab20-5350-483f-9dc6-6748665efdeb}')
RDPViewer = Guid('{32be5ed2-5c86-480f-a914-0ff8885a1b3f}')
class _IRDPSessionEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{98a97042-6698-40e9-8efd-b3200990004b}')
class __ReferenceRemainingTypes__(Structure):
    __ctrlLevel__: win32more.Windows.Win32.System.DesktopSharing.CTRL_LEVEL
    __attendeeDisconnectReason__: win32more.Windows.Win32.System.DesktopSharing.ATTENDEE_DISCONNECT_REASON
    __channelPriority__: win32more.Windows.Win32.System.DesktopSharing.CHANNEL_PRIORITY
    __channelFlags__: win32more.Windows.Win32.System.DesktopSharing.CHANNEL_FLAGS
    __channelAccessEnum__: win32more.Windows.Win32.System.DesktopSharing.CHANNEL_ACCESS_ENUM
    __rdpencomapiAttendeeFlags__: win32more.Windows.Win32.System.DesktopSharing.RDPENCOMAPI_ATTENDEE_FLAGS
    __rdpsrapiWndFlags__: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_WND_FLAGS
    __rdpsrapiAppFlags__: win32more.Windows.Win32.System.DesktopSharing.RDPSRAPI_APP_FLAGS


make_ready(__name__)
