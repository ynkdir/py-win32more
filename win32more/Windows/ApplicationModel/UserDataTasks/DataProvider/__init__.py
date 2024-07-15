from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.UserDataTasks
import win32more.Windows.ApplicationModel.UserDataTasks.DataProvider
import win32more.Windows.Foundation
import win32more.Windows.Win32.System.WinRT
class IUserDataTaskDataProviderConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection'
    _iid_ = Guid('{9ff39d1d-a447-428b-afe9-e5402bdeb041}')
    @winrt_commethod(6)
    def add_CreateOrUpdateTaskRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CreateOrUpdateTaskRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SyncRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SyncRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SkipOccurrenceRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SkipOccurrenceRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_CompleteTaskRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_CompleteTaskRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_DeleteTaskRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_DeleteTaskRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def Start(self) -> Void: ...
    CreateOrUpdateTaskRequested = event()
    SyncRequested = event()
    SkipOccurrenceRequested = event()
    CompleteTaskRequested = event()
    DeleteTaskRequested = event()
class IUserDataTaskDataProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderTriggerDetails'
    _iid_ = Guid('{ae273202-b1c9-453e-afc5-b30af3bd217d}')
    @winrt_commethod(6)
    def get_Connection(self) -> win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection: ...
    Connection = property(get_Connection, None)
class IUserDataTaskListCompleteTaskRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest'
    _iid_ = Guid('{f65e14a3-1a42-49da-8552-2873e52c55eb}')
    @winrt_commethod(6)
    def get_TaskListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TaskId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self, completedTaskId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    TaskId = property(get_TaskId, None)
    TaskListId = property(get_TaskListId, None)
class IUserDataTaskListCompleteTaskRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequestEventArgs'
    _iid_ = Guid('{d77c393d-4cf2-48ad-87fd-963f0eaa7a95}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserDataTaskListCreateOrUpdateTaskRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest'
    _iid_ = Guid('{2133772c-55c2-4300-8279-04326e07cce4}')
    @winrt_commethod(6)
    def get_TaskListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Task(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self, createdOrUpdatedUserDataTask: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Task = property(get_Task, None)
    TaskListId = property(get_TaskListId, None)
class IUserDataTaskListCreateOrUpdateTaskRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequestEventArgs'
    _iid_ = Guid('{12c55a52-e378-419b-ae38-a5e9e604476e}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserDataTaskListDeleteTaskRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest'
    _iid_ = Guid('{4b863c68-7657-4f3d-b074-d47ec8df07e7}')
    @winrt_commethod(6)
    def get_TaskListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TaskId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    TaskId = property(get_TaskId, None)
    TaskListId = property(get_TaskListId, None)
class IUserDataTaskListDeleteTaskRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequestEventArgs'
    _iid_ = Guid('{6063dad9-f562-4145-8efe-d50078c92b7f}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserDataTaskListSkipOccurrenceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest'
    _iid_ = Guid('{ab87e34d-1cd3-431c-9f58-089aa4338d85}')
    @winrt_commethod(6)
    def get_TaskListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TaskId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    TaskId = property(get_TaskId, None)
    TaskListId = property(get_TaskListId, None)
class IUserDataTaskListSkipOccurrenceRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequestEventArgs'
    _iid_ = Guid('{7a3b924a-cc2f-4e7b-aacd-a5b9d29cfa4e}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserDataTaskListSyncManagerSyncRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest'
    _iid_ = Guid('{40a73807-7590-4149-ae19-b211431a9f48}')
    @winrt_commethod(6)
    def get_TaskListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
class IUserDataTaskListSyncManagerSyncRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequestEventArgs'
    _iid_ = Guid('{8ead1c12-768e-43bd-8385-5cdc351ffdea}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskDataProviderConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection'
    @winrt_mixinmethod
    def add_CreateOrUpdateTaskRequested(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CreateOrUpdateTaskRequested(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SyncRequested(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SyncRequested(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SkipOccurrenceRequested(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SkipOccurrenceRequested(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CompleteTaskRequested(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CompleteTaskRequested(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DeleteTaskRequested(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DeleteTaskRequested(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection) -> Void: ...
    CreateOrUpdateTaskRequested = event()
    SyncRequested = event()
    SkipOccurrenceRequested = event()
    CompleteTaskRequested = event()
    DeleteTaskRequested = event()
class UserDataTaskDataProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderTriggerDetails
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderTriggerDetails'
    @winrt_mixinmethod
    def get_Connection(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderTriggerDetails) -> win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection: ...
    Connection = property(get_Connection, None)
class UserDataTaskListCompleteTaskRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequest'
    @winrt_mixinmethod
    def get_TaskListId(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TaskId(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest, completedTaskId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    TaskId = property(get_TaskId, None)
    TaskListId = property(get_TaskListId, None)
class UserDataTaskListCompleteTaskRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequestEventArgs) -> win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskListCreateOrUpdateTaskRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequest'
    @winrt_mixinmethod
    def get_TaskListId(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Task(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest, createdOrUpdatedUserDataTask: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    Task = property(get_Task, None)
    TaskListId = property(get_TaskListId, None)
class UserDataTaskListCreateOrUpdateTaskRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequestEventArgs) -> win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskListDeleteTaskRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequest'
    @winrt_mixinmethod
    def get_TaskListId(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TaskId(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    TaskId = property(get_TaskId, None)
    TaskListId = property(get_TaskListId, None)
class UserDataTaskListDeleteTaskRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequestEventArgs) -> win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskListSkipOccurrenceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequest'
    @winrt_mixinmethod
    def get_TaskListId(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TaskId(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    TaskId = property(get_TaskId, None)
    TaskListId = property(get_TaskListId, None)
class UserDataTaskListSkipOccurrenceRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequestEventArgs) -> win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskListSyncManagerSyncRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequest'
    @winrt_mixinmethod
    def get_TaskListId(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
class UserDataTaskListSyncManagerSyncRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequestEventArgs) -> win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)


make_ready(__name__)
