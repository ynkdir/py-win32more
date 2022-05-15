from win32more import *
import win32more.System.RemoteAssistance
import win32more.Foundation
import win32more.System.Com

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.System.RemoteAssistance, name, globals()[f"_define_{name}"]())
    return getattr(win32more.System.RemoteAssistance, name)
def __dir__():
    return __all__
DISPID_EVENT_ON_STATE_CHANGED = 5
DISPID_EVENT_ON_TERMINATION = 6
DISPID_EVENT_ON_CONTEXT_DATA = 7
DISPID_EVENT_ON_SEND_ERROR = 8
RendezvousApplication = Guid('0b7e019a-b5de-47fa-8966-9082f82fb192')
RENDEZVOUS_SESSION_STATE = Int32
RSS_UNKNOWN = 0
RSS_READY = 1
RSS_INVITATION = 2
RSS_ACCEPTED = 3
RSS_CONNECTED = 4
RSS_CANCELLED = 5
RSS_DECLINED = 6
RSS_TERMINATED = 7
RENDEZVOUS_SESSION_FLAGS = Int32
RSF_NONE = 0
RSF_INVITER = 1
RSF_INVITEE = 2
RSF_ORIGINAL_INVITER = 4
RSF_REMOTE_LEGACYSESSION = 8
RSF_REMOTE_WIN7SESSION = 16
def _define_IRendezvousSession_head():
    class IRendezvousSession(win32more.System.Com.IUnknown_head):
        Guid = Guid('9ba4b1dd-8b0c-48b7-9e7c-2f25857c8df5')
    return IRendezvousSession
def _define_IRendezvousSession():
    IRendezvousSession = win32more.System.RemoteAssistance.IRendezvousSession_head
    IRendezvousSession.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.RemoteAssistance.RENDEZVOUS_SESSION_STATE), use_last_error=False)(3, 'get_State', ((1, 'pSessionState'),)))
    IRendezvousSession.get_RemoteUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_RemoteUser', ((1, 'bstrUserName'),)))
    IRendezvousSession.get_Flags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(5, 'get_Flags', ((1, 'pFlags'),)))
    IRendezvousSession.SendContextData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(6, 'SendContextData', ((1, 'bstrData'),)))
    IRendezvousSession.Terminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(7, 'Terminate', ((1, 'hr'),(1, 'bstrAppData'),)))
    return IRendezvousSession
def _define_DRendezvousSessionEvents_head():
    class DRendezvousSessionEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('3fa19cf8-64c4-4f53-ae60-635b3806eca6')
    return DRendezvousSessionEvents
def _define_DRendezvousSessionEvents():
    DRendezvousSessionEvents = win32more.System.RemoteAssistance.DRendezvousSessionEvents_head
    return DRendezvousSessionEvents
def _define_IRendezvousApplication_head():
    class IRendezvousApplication(win32more.System.Com.IUnknown_head):
        Guid = Guid('4f4d070b-a275-49fb-b10d-8ec26387b50d')
    return IRendezvousApplication
def _define_IRendezvousApplication():
    IRendezvousApplication = win32more.System.RemoteAssistance.IRendezvousApplication_head
    IRendezvousApplication.SetRendezvousSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'SetRendezvousSession', ((1, 'pRendezvousSession'),)))
    return IRendezvousApplication
__all__ = [
    "DISPID_EVENT_ON_STATE_CHANGED",
    "DISPID_EVENT_ON_TERMINATION",
    "DISPID_EVENT_ON_CONTEXT_DATA",
    "DISPID_EVENT_ON_SEND_ERROR",
    "RendezvousApplication",
    "RENDEZVOUS_SESSION_STATE",
    "RSS_UNKNOWN",
    "RSS_READY",
    "RSS_INVITATION",
    "RSS_ACCEPTED",
    "RSS_CONNECTED",
    "RSS_CANCELLED",
    "RSS_DECLINED",
    "RSS_TERMINATED",
    "RENDEZVOUS_SESSION_FLAGS",
    "RSF_NONE",
    "RSF_INVITER",
    "RSF_INVITEE",
    "RSF_ORIGINAL_INVITER",
    "RSF_REMOTE_LEGACYSESSION",
    "RSF_REMOTE_WIN7SESSION",
    "IRendezvousSession",
    "DRendezvousSessionEvents",
    "IRendezvousApplication",
]
