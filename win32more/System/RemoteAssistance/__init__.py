from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.RemoteAssistance
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
DISPID_EVENT_ON_STATE_CHANGED: UInt32 = 5
DISPID_EVENT_ON_TERMINATION: UInt32 = 6
DISPID_EVENT_ON_CONTEXT_DATA: UInt32 = 7
DISPID_EVENT_ON_SEND_ERROR: UInt32 = 8
class DRendezvousSessionEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('3fa19cf8-64c4-4f53-ae-60-63-5b-38-06-ec-a6')
class IRendezvousApplication(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4f4d070b-a275-49fb-b1-0d-8e-c2-63-87-b5-0d')
    @commethod(3)
    def SetRendezvousSession(pRendezvousSession: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class IRendezvousSession(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9ba4b1dd-8b0c-48b7-9e-7c-2f-25-85-7c-8d-f5')
    @commethod(3)
    def get_State(pSessionState: POINTER(win32more.System.RemoteAssistance.RENDEZVOUS_SESSION_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def get_RemoteUser(bstrUserName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_Flags(pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SendContextData(bstrData: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Terminate(hr: win32more.Foundation.HRESULT, bstrAppData: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
RENDEZVOUS_SESSION_FLAGS = Int32
RSF_NONE: RENDEZVOUS_SESSION_FLAGS = 0
RSF_INVITER: RENDEZVOUS_SESSION_FLAGS = 1
RSF_INVITEE: RENDEZVOUS_SESSION_FLAGS = 2
RSF_ORIGINAL_INVITER: RENDEZVOUS_SESSION_FLAGS = 4
RSF_REMOTE_LEGACYSESSION: RENDEZVOUS_SESSION_FLAGS = 8
RSF_REMOTE_WIN7SESSION: RENDEZVOUS_SESSION_FLAGS = 16
RENDEZVOUS_SESSION_STATE = Int32
RSS_UNKNOWN: RENDEZVOUS_SESSION_STATE = 0
RSS_READY: RENDEZVOUS_SESSION_STATE = 1
RSS_INVITATION: RENDEZVOUS_SESSION_STATE = 2
RSS_ACCEPTED: RENDEZVOUS_SESSION_STATE = 3
RSS_CONNECTED: RENDEZVOUS_SESSION_STATE = 4
RSS_CANCELLED: RENDEZVOUS_SESSION_STATE = 5
RSS_DECLINED: RENDEZVOUS_SESSION_STATE = 6
RSS_TERMINATED: RENDEZVOUS_SESSION_STATE = 7
RendezvousApplication = Guid('0b7e019a-b5de-47fa-89-66-90-82-f8-2f-b1-92')
make_head(_module, 'DRendezvousSessionEvents')
make_head(_module, 'IRendezvousApplication')
make_head(_module, 'IRendezvousSession')
__all__ = [
    "DISPID_EVENT_ON_CONTEXT_DATA",
    "DISPID_EVENT_ON_SEND_ERROR",
    "DISPID_EVENT_ON_STATE_CHANGED",
    "DISPID_EVENT_ON_TERMINATION",
    "DRendezvousSessionEvents",
    "IRendezvousApplication",
    "IRendezvousSession",
    "RENDEZVOUS_SESSION_FLAGS",
    "RENDEZVOUS_SESSION_STATE",
    "RSF_INVITEE",
    "RSF_INVITER",
    "RSF_NONE",
    "RSF_ORIGINAL_INVITER",
    "RSF_REMOTE_LEGACYSESSION",
    "RSF_REMOTE_WIN7SESSION",
    "RSS_ACCEPTED",
    "RSS_CANCELLED",
    "RSS_CONNECTED",
    "RSS_DECLINED",
    "RSS_INVITATION",
    "RSS_READY",
    "RSS_TERMINATED",
    "RSS_UNKNOWN",
    "RendezvousApplication",
]
