from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.UserDataTasks
import Windows.ApplicationModel.UserDataTasks.DataProvider
import Windows.Foundation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IUserDataTaskDataProviderConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection'
    _iid_ = Guid('{9ff39d1d-a447-428b-afe9-e5402bdeb041}')
    @winrt_commethod(6)
    def add_CreateOrUpdateTaskRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CreateOrUpdateTaskRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SyncRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SyncRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SkipOccurrenceRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SkipOccurrenceRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_CompleteTaskRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_CompleteTaskRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_DeleteTaskRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_DeleteTaskRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def Start(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection) -> Void: ...
class IUserDataTaskDataProviderTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderTriggerDetails'
    _iid_ = Guid('{ae273202-b1c9-453e-afc5-b30af3bd217d}')
    @winrt_commethod(6)
    def get_Connection(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderTriggerDetails) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection: ...
    Connection = property(get_Connection, None)
class IUserDataTaskListCompleteTaskRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest'
    _iid_ = Guid('{f65e14a3-1a42-49da-8552-2873e52c55eb}')
    @winrt_commethod(6)
    def get_TaskListId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TaskId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest, completedTaskId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
    TaskId = property(get_TaskId, None)
class IUserDataTaskListCompleteTaskRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequestEventArgs'
    _iid_ = Guid('{d77c393d-4cf2-48ad-87fd-963f0eaa7a95}')
    @winrt_commethod(6)
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserDataTaskListCreateOrUpdateTaskRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest'
    _iid_ = Guid('{2133772c-55c2-4300-8279-04326e07cce4}')
    @winrt_commethod(6)
    def get_TaskListId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Task(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest) -> Windows.ApplicationModel.UserDataTasks.UserDataTask: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest, createdOrUpdatedUserDataTask: Windows.ApplicationModel.UserDataTasks.UserDataTask) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
    Task = property(get_Task, None)
class IUserDataTaskListCreateOrUpdateTaskRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequestEventArgs'
    _iid_ = Guid('{12c55a52-e378-419b-ae38-a5e9e604476e}')
    @winrt_commethod(6)
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserDataTaskListDeleteTaskRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest'
    _iid_ = Guid('{4b863c68-7657-4f3d-b074-d47ec8df07e7}')
    @winrt_commethod(6)
    def get_TaskListId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TaskId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
    TaskId = property(get_TaskId, None)
class IUserDataTaskListDeleteTaskRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequestEventArgs'
    _iid_ = Guid('{6063dad9-f562-4145-8efe-d50078c92b7f}')
    @winrt_commethod(6)
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserDataTaskListSkipOccurrenceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest'
    _iid_ = Guid('{ab87e34d-1cd3-431c-9f58-089aa4338d85}')
    @winrt_commethod(6)
    def get_TaskListId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TaskId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
    TaskId = property(get_TaskId, None)
class IUserDataTaskListSkipOccurrenceRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequestEventArgs'
    _iid_ = Guid('{7a3b924a-cc2f-4e7b-aacd-a5b9d29cfa4e}')
    @winrt_commethod(6)
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserDataTaskListSyncManagerSyncRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest'
    _iid_ = Guid('{40a73807-7590-4149-ae19-b211431a9f48}')
    @winrt_commethod(6)
    def get_TaskListId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportCompletedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ReportFailedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
class IUserDataTaskListSyncManagerSyncRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequestEventArgs'
    _iid_ = Guid('{8ead1c12-768e-43bd-8385-5cdc351ffdea}')
    @winrt_commethod(6)
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskDataProviderConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection'
    @winrt_mixinmethod
    def add_CreateOrUpdateTaskRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CreateOrUpdateTaskRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SyncRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SyncRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SkipOccurrenceRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SkipOccurrenceRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CompleteTaskRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CompleteTaskRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DeleteTaskRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DeleteTaskRequested(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderConnection) -> Void: ...
class UserDataTaskDataProviderTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderTriggerDetails
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderTriggerDetails'
    @winrt_mixinmethod
    def get_Connection(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderTriggerDetails) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection: ...
    Connection = property(get_Connection, None)
class UserDataTaskListCompleteTaskRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequest'
    @winrt_mixinmethod
    def get_TaskListId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TaskId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest, completedTaskId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequest) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
    TaskId = property(get_TaskId, None)
class UserDataTaskListCompleteTaskRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskListCreateOrUpdateTaskRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequest'
    @winrt_mixinmethod
    def get_TaskListId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Task(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest) -> Windows.ApplicationModel.UserDataTasks.UserDataTask: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest, createdOrUpdatedUserDataTask: Windows.ApplicationModel.UserDataTasks.UserDataTask) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequest) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
    Task = property(get_Task, None)
class UserDataTaskListCreateOrUpdateTaskRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskListDeleteTaskRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequest'
    @winrt_mixinmethod
    def get_TaskListId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TaskId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequest) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
    TaskId = property(get_TaskId, None)
class UserDataTaskListDeleteTaskRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskListSkipOccurrenceRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequest'
    @winrt_mixinmethod
    def get_TaskListId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TaskId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequest) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
    TaskId = property(get_TaskId, None)
class UserDataTaskListSkipOccurrenceRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskListSyncManagerSyncRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequest'
    @winrt_mixinmethod
    def get_TaskListId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
class UserDataTaskListSyncManagerSyncRequestEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequestEventArgs
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
make_head(_module, 'IUserDataTaskDataProviderConnection')
make_head(_module, 'IUserDataTaskDataProviderTriggerDetails')
make_head(_module, 'IUserDataTaskListCompleteTaskRequest')
make_head(_module, 'IUserDataTaskListCompleteTaskRequestEventArgs')
make_head(_module, 'IUserDataTaskListCreateOrUpdateTaskRequest')
make_head(_module, 'IUserDataTaskListCreateOrUpdateTaskRequestEventArgs')
make_head(_module, 'IUserDataTaskListDeleteTaskRequest')
make_head(_module, 'IUserDataTaskListDeleteTaskRequestEventArgs')
make_head(_module, 'IUserDataTaskListSkipOccurrenceRequest')
make_head(_module, 'IUserDataTaskListSkipOccurrenceRequestEventArgs')
make_head(_module, 'IUserDataTaskListSyncManagerSyncRequest')
make_head(_module, 'IUserDataTaskListSyncManagerSyncRequestEventArgs')
make_head(_module, 'UserDataTaskDataProviderConnection')
make_head(_module, 'UserDataTaskDataProviderTriggerDetails')
make_head(_module, 'UserDataTaskListCompleteTaskRequest')
make_head(_module, 'UserDataTaskListCompleteTaskRequestEventArgs')
make_head(_module, 'UserDataTaskListCreateOrUpdateTaskRequest')
make_head(_module, 'UserDataTaskListCreateOrUpdateTaskRequestEventArgs')
make_head(_module, 'UserDataTaskListDeleteTaskRequest')
make_head(_module, 'UserDataTaskListDeleteTaskRequestEventArgs')
make_head(_module, 'UserDataTaskListSkipOccurrenceRequest')
make_head(_module, 'UserDataTaskListSkipOccurrenceRequestEventArgs')
make_head(_module, 'UserDataTaskListSyncManagerSyncRequest')
make_head(_module, 'UserDataTaskListSyncManagerSyncRequestEventArgs')
