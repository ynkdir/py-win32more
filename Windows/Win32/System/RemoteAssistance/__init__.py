from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.RemoteAssistance
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
DISPID_EVENT_ON_STATE_CHANGED: UInt32 = 5
DISPID_EVENT_ON_TERMINATION: UInt32 = 6
DISPID_EVENT_ON_CONTEXT_DATA: UInt32 = 7
DISPID_EVENT_ON_SEND_ERROR: UInt32 = 8
class DRendezvousSessionEvents(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('3fa19cf8-64c4-4f53-ae-60-63-5b-38-06-ec-a6')
class IRendezvousApplication(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('4f4d070b-a275-49fb-b1-0d-8e-c2-63-87-b5-0d')
    @commethod(3)
    def SetRendezvousSession(self, pRendezvousSession: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IRendezvousSession(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9ba4b1dd-8b0c-48b7-9e-7c-2f-25-85-7c-8d-f5')
    @commethod(3)
    def get_State(self, pSessionState: POINTER(Windows.Win32.System.RemoteAssistance.RENDEZVOUS_SESSION_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_RemoteUser(self, bstrUserName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Flags(self, pFlags: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SendContextData(self, bstrData: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Terminate(self, hr: Windows.Win32.Foundation.HRESULT, bstrAppData: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
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
