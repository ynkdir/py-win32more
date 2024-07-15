from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Appointments
import win32more.Windows.ApplicationModel.Appointments.DataProvider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
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
    Comment = property(get_Comment, None)
    NotifyInvitees = property(get_NotifyInvitees, None)
    Subject = property(get_Subject, None)
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
    Appointment = property(get_Appointment, None)
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
    ChangedProperties = property(get_ChangedProperties, None)
    NotifyInvitees = property(get_NotifyInvitees, None)
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
    Comment = property(get_Comment, None)
    ForwardHeader = property(get_ForwardHeader, None)
    Invitees = property(get_Invitees, None)
    Subject = property(get_Subject, None)
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
    Comment = property(get_Comment, None)
    NewDuration = property(get_NewDuration, None)
    NewStartTime = property(get_NewStartTime, None)
    Subject = property(get_Subject, None)
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
    Comment = property(get_Comment, None)
    Response = property(get_Response, None)
    SendUpdate = property(get_SendUpdate, None)
    Subject = property(get_Subject, None)
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
    SyncRequested = event()
    CreateOrUpdateAppointmentRequested = event()
    CancelMeetingRequested = event()
    ForwardMeetingRequested = event()
    ProposeNewTimeForMeetingRequested = event()
    UpdateMeetingResponseRequested = event()
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
    Comment = property(get_Comment, None)
    NotifyInvitees = property(get_NotifyInvitees, None)
    Subject = property(get_Subject, None)
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
    Appointment = property(get_Appointment, None)
    AppointmentCalendarLocalId = property(get_AppointmentCalendarLocalId, None)
    ChangedProperties = property(get_ChangedProperties, None)
    NotifyInvitees = property(get_NotifyInvitees, None)
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
    Comment = property(get_Comment, None)
    ForwardHeader = property(get_ForwardHeader, None)
    Invitees = property(get_Invitees, None)
    Subject = property(get_Subject, None)
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
    Comment = property(get_Comment, None)
    NewDuration = property(get_NewDuration, None)
    NewStartTime = property(get_NewStartTime, None)
    Subject = property(get_Subject, None)
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
    Comment = property(get_Comment, None)
    Response = property(get_Response, None)
    SendUpdate = property(get_SendUpdate, None)
    Subject = property(get_Subject, None)
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
    SyncRequested = event()
    CreateOrUpdateAppointmentRequested = event()
    CancelMeetingRequested = event()
    ForwardMeetingRequested = event()
    ProposeNewTimeForMeetingRequested = event()
    UpdateMeetingResponseRequested = event()
class IAppointmentDataProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Appointments.DataProvider.IAppointmentDataProviderTriggerDetails'
    _iid_ = Guid('{b3283c01-7e12-4e5e-b1ef-74fb68ac6f2a}')
    @winrt_commethod(6)
    def get_Connection(self) -> win32more.Windows.ApplicationModel.Appointments.DataProvider.AppointmentDataProviderConnection: ...
    Connection = property(get_Connection, None)


make_ready(__name__)
