from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
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
class IUserDataTaskDataProviderConnection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9ff39d1d-a447-428b-af-e9-e5-40-2b-de-b0-41')
    @winrt_commethod(6)
    def add_CreateOrUpdateTaskRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CreateOrUpdateTaskRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SyncRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SyncRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SkipOccurrenceRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SkipOccurrenceRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_CompleteTaskRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_CompleteTaskRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_DeleteTaskRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection, Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_DeleteTaskRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def Start(self) -> Void: ...
class IUserDataTaskDataProviderTriggerDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ae273202-b1c9-453e-af-c5-b3-0a-f3-bd-21-7d')
    @winrt_commethod(6)
    def get_Connection(self) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection: ...
    Connection = property(get_Connection, None)
class IUserDataTaskListCompleteTaskRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f65e14a3-1a42-49da-85-52-28-73-e5-2c-55-eb')
    @winrt_commethod(6)
    def get_TaskListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TaskId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self, completedTaskId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
    TaskId = property(get_TaskId, None)
class IUserDataTaskListCompleteTaskRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d77c393d-4cf2-48ad-87-fd-96-3f-0e-aa-7a-95')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserDataTaskListCreateOrUpdateTaskRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2133772c-55c2-4300-82-79-04-32-6e-07-cc-e4')
    @winrt_commethod(6)
    def get_TaskListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Task(self) -> Windows.ApplicationModel.UserDataTasks.UserDataTask: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self, createdOrUpdatedUserDataTask: Windows.ApplicationModel.UserDataTasks.UserDataTask) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
    Task = property(get_Task, None)
class IUserDataTaskListCreateOrUpdateTaskRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('12c55a52-e378-419b-ae-38-a5-e9-e6-04-47-6e')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserDataTaskListDeleteTaskRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4b863c68-7657-4f3d-b0-74-d4-7e-c8-df-07-e7')
    @winrt_commethod(6)
    def get_TaskListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TaskId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
    TaskId = property(get_TaskId, None)
class IUserDataTaskListDeleteTaskRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6063dad9-f562-4145-8e-fe-d5-00-78-c9-2b-7f')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserDataTaskListSkipOccurrenceRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ab87e34d-1cd3-431c-9f-58-08-9a-a4-33-8d-85')
    @winrt_commethod(6)
    def get_TaskListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TaskId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
    TaskId = property(get_TaskId, None)
class IUserDataTaskListSkipOccurrenceRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7a3b924a-cc2f-4e7b-aa-cd-a5-b9-d2-9c-fa-4e')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserDataTaskListSyncManagerSyncRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('40a73807-7590-4149-ae-19-b2-11-43-1a-9f-48')
    @winrt_commethod(6)
    def get_TaskListId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
class IUserDataTaskListSyncManagerSyncRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8ead1c12-768e-43bd-83-85-5c-dc-35-1f-fd-ea')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskDataProviderConnection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection'
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
class UserDataTaskDataProviderTriggerDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderTriggerDetails'
    @winrt_mixinmethod
    def get_Connection(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskDataProviderTriggerDetails) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskDataProviderConnection: ...
    Connection = property(get_Connection, None)
class UserDataTaskListCompleteTaskRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequest'
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
class UserDataTaskListCompleteTaskRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCompleteTaskRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCompleteTaskRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskListCreateOrUpdateTaskRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequest'
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
class UserDataTaskListCreateOrUpdateTaskRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListCreateOrUpdateTaskRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListCreateOrUpdateTaskRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskListDeleteTaskRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequest'
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
class UserDataTaskListDeleteTaskRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListDeleteTaskRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListDeleteTaskRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskListSkipOccurrenceRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequest'
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
class UserDataTaskListSkipOccurrenceRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequestEventArgs) -> Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSkipOccurrenceRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSkipOccurrenceRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserDataTaskListSyncManagerSyncRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequest'
    @winrt_mixinmethod
    def get_TaskListId(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.ApplicationModel.UserDataTasks.DataProvider.IUserDataTaskListSyncManagerSyncRequest) -> Windows.Foundation.IAsyncAction: ...
    TaskListId = property(get_TaskListId, None)
class UserDataTaskListSyncManagerSyncRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserDataTasks.DataProvider.UserDataTaskListSyncManagerSyncRequestEventArgs'
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
