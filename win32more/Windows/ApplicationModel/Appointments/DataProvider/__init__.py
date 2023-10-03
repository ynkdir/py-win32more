from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.Appointments
import win32more.Windows.ApplicationModel.Appointments.DataProvider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AppointmentCalendarCancelMeetingRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequest
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarCancelMeetingRequest'
    @winrt_mixinmethod
    def get_AppointmentCalendarLocalId(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppointmentLocalId(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppointmentOriginalStartTime(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequest) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Comment(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NotifyInvitees(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequest) -> Boolean: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
    AppointmentLocalId = property(get_AppointmentLocalId, None)
    AppointmentOriginalStartTime = property(get_AppointmentOriginalStartTime, None)
    Subject = property(get_Subject, None)
    Comment = property(get_Comment, None)
    NotifyInvitees = property(get_NotifyInvitees, None)
class AppointmentCalendarCancelMeetingRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarCancelMeetingRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequestEventArgs) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarCancelMeetingRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class AppointmentCalendarCreateOrUpdateAppointmentRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCreateOrUpdateAppointmentRequest
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarCreateOrUpdateAppointmentRequest'
    @winrt_mixinmethod
    def get_AppointmentCalendarLocalId(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCreateOrUpdateAppointmentRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Appointment(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCreateOrUpdateAppointmentRequest) -> win32more.Windows.ApplicationModel.Appointments.Appointment: ...
    @winrt_mixinmethod
    def get_NotifyInvitees(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCreateOrUpdateAppointmentRequest) -> Boolean: ...
    @winrt_mixinmethod
    def get_ChangedProperties(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCreateOrUpdateAppointmentRequest) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCreateOrUpdateAppointmentRequest, createdOrUpdatedAppointment: win32more.Windows.ApplicationModel.Appointments.Appointment) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCreateOrUpdateAppointmentRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
    Appointment = property(get_Appointment, None)
    NotifyInvitees = property(get_NotifyInvitees, None)
    ChangedProperties = property(get_ChangedProperties, None)
class AppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarCreateOrUpdateAppointmentRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class AppointmentCalendarForwardMeetingRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequest
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarForwardMeetingRequest'
    @winrt_mixinmethod
    def get_AppointmentCalendarLocalId(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppointmentLocalId(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppointmentOriginalStartTime(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequest) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_Invitees(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequest) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Appointments.AppointmentInvitee]: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ForwardHeader(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Comment(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
    AppointmentLocalId = property(get_AppointmentLocalId, None)
    AppointmentOriginalStartTime = property(get_AppointmentOriginalStartTime, None)
    Invitees = property(get_Invitees, None)
    Subject = property(get_Subject, None)
    ForwardHeader = property(get_ForwardHeader, None)
    Comment = property(get_Comment, None)
class AppointmentCalendarForwardMeetingRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarForwardMeetingRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequestEventArgs) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarForwardMeetingRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class AppointmentCalendarProposeNewTimeForMeetingRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequest
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarProposeNewTimeForMeetingRequest'
    @winrt_mixinmethod
    def get_AppointmentCalendarLocalId(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppointmentLocalId(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppointmentOriginalStartTime(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequest) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_NewStartTime(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequest) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_NewDuration(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequest) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Comment(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
    AppointmentLocalId = property(get_AppointmentLocalId, None)
    AppointmentOriginalStartTime = property(get_AppointmentOriginalStartTime, None)
    NewStartTime = property(get_NewStartTime, None)
    NewDuration = property(get_NewDuration, None)
    Subject = property(get_Subject, None)
    Comment = property(get_Comment, None)
class AppointmentCalendarProposeNewTimeForMeetingRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarProposeNewTimeForMeetingRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequestEventArgs) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarProposeNewTimeForMeetingRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class AppointmentCalendarSyncManagerSyncRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarSyncManagerSyncRequest
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarSyncManagerSyncRequest'
    @winrt_mixinmethod
    def get_AppointmentCalendarLocalId(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarSyncManagerSyncRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarSyncManagerSyncRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarSyncManagerSyncRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
class AppointmentCalendarSyncManagerSyncRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarSyncManagerSyncRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarSyncManagerSyncRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarSyncManagerSyncRequestEventArgs) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarSyncManagerSyncRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarSyncManagerSyncRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class AppointmentCalendarUpdateMeetingResponseRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequest
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarUpdateMeetingResponseRequest'
    @winrt_mixinmethod
    def get_AppointmentCalendarLocalId(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppointmentLocalId(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AppointmentOriginalStartTime(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequest) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_Response(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequest) -> win32more.Windows.ApplicationModel.Appointments.AppointmentParticipantResponse: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Comment(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SendUpdate(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequest) -> Boolean: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
    AppointmentLocalId = property(get_AppointmentLocalId, None)
    AppointmentOriginalStartTime = property(get_AppointmentOriginalStartTime, None)
    Response = property(get_Response, None)
    Subject = property(get_Subject, None)
    Comment = property(get_Comment, None)
    SendUpdate = property(get_SendUpdate, None)
class AppointmentCalendarUpdateMeetingResponseRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarUpdateMeetingResponseRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequestEventArgs) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarUpdateMeetingResponseRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class AppointmentDataProviderConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection'
    @winrt_mixinmethod
    def add_SyncRequested(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection, win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarSyncManagerSyncRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SyncRequested(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CreateOrUpdateAppointmentRequested(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection, win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CreateOrUpdateAppointmentRequested(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CancelMeetingRequested(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection, win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarCancelMeetingRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CancelMeetingRequested(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ForwardMeetingRequested(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection, win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarForwardMeetingRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ForwardMeetingRequested(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ProposeNewTimeForMeetingRequested(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection, win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarProposeNewTimeForMeetingRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProposeNewTimeForMeetingRequested(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UpdateMeetingResponseRequested(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection, win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarUpdateMeetingResponseRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UpdateMeetingResponseRequested(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection) -> Void: ...
class AppointmentDataProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderTriggerDetails
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderTriggerDetails'
    @winrt_mixinmethod
    def get_Connection(self: win32more.Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderTriggerDetails) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection: ...
    Connection = property(get_Connection, None)
class IAppointmentCalendarCancelMeetingRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequest'
    _iid_ = Guid('{49460f8d-6434-40d7-ad46-6297419314d1}')
    @winrt_commethod(6)
    def get_AppointmentCalendarLocalId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AppointmentLocalId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AppointmentOriginalStartTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_NotifyInvitees(self) -> Boolean: ...
    @winrt_commethod(12)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
    AppointmentLocalId = property(get_AppointmentLocalId, None)
    AppointmentOriginalStartTime = property(get_AppointmentOriginalStartTime, None)
    Subject = property(get_Subject, None)
    Comment = property(get_Comment, None)
    NotifyInvitees = property(get_NotifyInvitees, None)
class IAppointmentCalendarCancelMeetingRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCancelMeetingRequestEventArgs'
    _iid_ = Guid('{1a79be16-7f30-4e35-beef-9d2c7b6dcae1}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarCancelMeetingRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IAppointmentCalendarCreateOrUpdateAppointmentRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCreateOrUpdateAppointmentRequest'
    _iid_ = Guid('{2e62f2b2-ca96-48ac-9124-406b19fefa70}')
    @winrt_commethod(6)
    def get_AppointmentCalendarLocalId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Appointment(self) -> win32more.Windows.ApplicationModel.Appointments.Appointment: ...
    @winrt_commethod(8)
    def get_NotifyInvitees(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ChangedProperties(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def ReportCompletedAsync(self, createdOrUpdatedAppointment: win32more.Windows.ApplicationModel.Appointments.Appointment) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
    Appointment = property(get_Appointment, None)
    NotifyInvitees = property(get_NotifyInvitees, None)
    ChangedProperties = property(get_ChangedProperties, None)
class IAppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs'
    _iid_ = Guid('{cf8ded28-002e-4bf7-8e9d-5e20d49aa3ba}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarCreateOrUpdateAppointmentRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IAppointmentCalendarForwardMeetingRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequest'
    _iid_ = Guid('{82e5ee56-26b6-4253-8a8f-6cf5f2ff7884}')
    @winrt_commethod(6)
    def get_AppointmentCalendarLocalId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AppointmentLocalId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AppointmentOriginalStartTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def get_Invitees(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.Appointments.AppointmentInvitee]: ...
    @winrt_commethod(10)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_ForwardHeader(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
    AppointmentLocalId = property(get_AppointmentLocalId, None)
    AppointmentOriginalStartTime = property(get_AppointmentOriginalStartTime, None)
    Invitees = property(get_Invitees, None)
    Subject = property(get_Subject, None)
    ForwardHeader = property(get_ForwardHeader, None)
    Comment = property(get_Comment, None)
class IAppointmentCalendarForwardMeetingRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarForwardMeetingRequestEventArgs'
    _iid_ = Guid('{3109151a-23a2-42fd-9c82-c9a60d59f8a8}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarForwardMeetingRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IAppointmentCalendarProposeNewTimeForMeetingRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequest'
    _iid_ = Guid('{ce1c63f5-edf6-43c3-82b7-be6b368c6900}')
    @winrt_commethod(6)
    def get_AppointmentCalendarLocalId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AppointmentLocalId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AppointmentOriginalStartTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def get_NewStartTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_NewDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
    AppointmentLocalId = property(get_AppointmentLocalId, None)
    AppointmentOriginalStartTime = property(get_AppointmentOriginalStartTime, None)
    NewStartTime = property(get_NewStartTime, None)
    NewDuration = property(get_NewDuration, None)
    Subject = property(get_Subject, None)
    Comment = property(get_Comment, None)
class IAppointmentCalendarProposeNewTimeForMeetingRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarProposeNewTimeForMeetingRequestEventArgs'
    _iid_ = Guid('{d2d777d8-fed1-4280-a3ba-2e1f47609aa2}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarProposeNewTimeForMeetingRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IAppointmentCalendarSyncManagerSyncRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarSyncManagerSyncRequest'
    _iid_ = Guid('{12ab382b-7163-4a56-9a4e-7223a84adf46}')
    @winrt_commethod(6)
    def get_AppointmentCalendarLocalId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
class IAppointmentCalendarSyncManagerSyncRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarSyncManagerSyncRequestEventArgs'
    _iid_ = Guid('{ca17c6f7-0284-4edd-87ba-4d8f69dcf5c0}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarSyncManagerSyncRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IAppointmentCalendarUpdateMeetingResponseRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequest'
    _iid_ = Guid('{a36d608c-c29d-4b94-b086-7e9ff7bd84a0}')
    @winrt_commethod(6)
    def get_AppointmentCalendarLocalId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AppointmentLocalId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AppointmentOriginalStartTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def get_Response(self) -> win32more.Windows.ApplicationModel.Appointments.AppointmentParticipantResponse: ...
    @winrt_commethod(10)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_SendUpdate(self) -> Boolean: ...
    @winrt_commethod(13)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
    AppointmentLocalId = property(get_AppointmentLocalId, None)
    AppointmentOriginalStartTime = property(get_AppointmentOriginalStartTime, None)
    Response = property(get_Response, None)
    Subject = property(get_Subject, None)
    Comment = property(get_Comment, None)
    SendUpdate = property(get_SendUpdate, None)
class IAppointmentCalendarUpdateMeetingResponseRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentCalendarUpdateMeetingResponseRequestEventArgs'
    _iid_ = Guid('{88759883-97bf-479d-aed5-0be8ce567d1e}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarUpdateMeetingResponseRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IAppointmentDataProviderConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderConnection'
    _iid_ = Guid('{f3dd9d83-3254-465f-abdb-928046552cf4}')
    @winrt_commethod(6)
    def add_SyncRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection, win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarSyncManagerSyncRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SyncRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_CreateOrUpdateAppointmentRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection, win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CreateOrUpdateAppointmentRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_CancelMeetingRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection, win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarCancelMeetingRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_CancelMeetingRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_ForwardMeetingRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection, win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarForwardMeetingRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_ForwardMeetingRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_ProposeNewTimeForMeetingRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection, win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarProposeNewTimeForMeetingRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_ProposeNewTimeForMeetingRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_UpdateMeetingResponseRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection, win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentCalendarUpdateMeetingResponseRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_UpdateMeetingResponseRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def Start(self) -> Void: ...
class IAppointmentDataProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderTriggerDetails'
    _iid_ = Guid('{b3283c01-7e12-4e5e-b1ef-74fb68ac6f2a}')
    @winrt_commethod(6)
    def get_Connection(self) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection: ...
    Connection = property(get_Connection, None)
make_head(_module, 'AppointmentCalendarCancelMeetingRequest')
make_head(_module, 'AppointmentCalendarCancelMeetingRequestEventArgs')
make_head(_module, 'AppointmentCalendarCreateOrUpdateAppointmentRequest')
make_head(_module, 'AppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs')
make_head(_module, 'AppointmentCalendarForwardMeetingRequest')
make_head(_module, 'AppointmentCalendarForwardMeetingRequestEventArgs')
make_head(_module, 'AppointmentCalendarProposeNewTimeForMeetingRequest')
make_head(_module, 'AppointmentCalendarProposeNewTimeForMeetingRequestEventArgs')
make_head(_module, 'AppointmentCalendarSyncManagerSyncRequest')
make_head(_module, 'AppointmentCalendarSyncManagerSyncRequestEventArgs')
make_head(_module, 'AppointmentCalendarUpdateMeetingResponseRequest')
make_head(_module, 'AppointmentCalendarUpdateMeetingResponseRequestEventArgs')
make_head(_module, 'AppointmentDataProviderConnection')
make_head(_module, 'AppointmentDataProviderTriggerDetails')
make_head(_module, 'IAppointmentCalendarCancelMeetingRequest')
make_head(_module, 'IAppointmentCalendarCancelMeetingRequestEventArgs')
make_head(_module, 'IAppointmentCalendarCreateOrUpdateAppointmentRequest')
make_head(_module, 'IAppointmentCalendarCreateOrUpdateAppointmentRequestEventArgs')
make_head(_module, 'IAppointmentCalendarForwardMeetingRequest')
make_head(_module, 'IAppointmentCalendarForwardMeetingRequestEventArgs')
make_head(_module, 'IAppointmentCalendarProposeNewTimeForMeetingRequest')
make_head(_module, 'IAppointmentCalendarProposeNewTimeForMeetingRequestEventArgs')
make_head(_module, 'IAppointmentCalendarSyncManagerSyncRequest')
make_head(_module, 'IAppointmentCalendarSyncManagerSyncRequestEventArgs')
make_head(_module, 'IAppointmentCalendarUpdateMeetingResponseRequest')
make_head(_module, 'IAppointmentCalendarUpdateMeetingResponseRequestEventArgs')
make_head(_module, 'IAppointmentDataProviderConnection')
make_head(_module, 'IAppointmentDataProviderTriggerDetails')