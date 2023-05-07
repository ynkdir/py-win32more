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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IUserDataTask(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTask'
    _iid_ = Guid('{7c6585d1-e0d4-4f99-aee2-bc2d5ddadf4c}')
    @winrt_commethod(6)
    def get_Id(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ListId(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RemoteId(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_RemoteId(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_CompletedDate(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def put_CompletedDate(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(12)
    def get_Details(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_Details(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_DetailsKind(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskDetailsKind: ...
    @winrt_commethod(15)
    def put_DetailsKind(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskDetailsKind) -> Void: ...
    @winrt_commethod(16)
    def get_DueDate(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(17)
    def put_DueDate(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(18)
    def get_Kind(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskKind: ...
    @winrt_commethod(19)
    def get_Priority(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskPriority: ...
    @winrt_commethod(20)
    def put_Priority(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskPriority) -> Void: ...
    @winrt_commethod(21)
    def get_RecurrenceProperties(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceProperties: ...
    @winrt_commethod(22)
    def put_RecurrenceProperties(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceProperties) -> Void: ...
    @winrt_commethod(23)
    def get_RegenerationProperties(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationProperties: ...
    @winrt_commethod(24)
    def put_RegenerationProperties(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationProperties) -> Void: ...
    @winrt_commethod(25)
    def get_Reminder(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(26)
    def put_Reminder(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(27)
    def get_Sensitivity(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskSensitivity: ...
    @winrt_commethod(28)
    def put_Sensitivity(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskSensitivity) -> Void: ...
    @winrt_commethod(29)
    def get_Subject(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_commethod(30)
    def put_Subject(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: WinRT_String) -> Void: ...
    @winrt_commethod(31)
    def get_StartDate(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(32)
    def put_StartDate(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    Id = property(get_Id, None)
    ListId = property(get_ListId, None)
    RemoteId = property(get_RemoteId, put_RemoteId)
    CompletedDate = property(get_CompletedDate, put_CompletedDate)
    Details = property(get_Details, put_Details)
    DetailsKind = property(get_DetailsKind, put_DetailsKind)
    DueDate = property(get_DueDate, put_DueDate)
    Kind = property(get_Kind, None)
    Priority = property(get_Priority, put_Priority)
    RecurrenceProperties = property(get_RecurrenceProperties, put_RecurrenceProperties)
    RegenerationProperties = property(get_RegenerationProperties, put_RegenerationProperties)
    Reminder = property(get_Reminder, put_Reminder)
    Sensitivity = property(get_Sensitivity, put_Sensitivity)
    Subject = property(get_Subject, put_Subject)
    StartDate = property(get_StartDate, put_StartDate)
class IUserDataTaskBatch(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskBatch'
    _iid_ = Guid('{382da5fe-20b5-431c-8f42-a5d292ec930c}')
    @winrt_commethod(6)
    def get_Tasks(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskBatch) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.UserDataTasks.UserDataTask]: ...
    Tasks = property(get_Tasks, None)
class IUserDataTaskList(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskList'
    _iid_ = Guid('{49412e39-7c1d-4df1-bed3-314b7cbf5e4e}')
    @winrt_commethod(6)
    def get_Id(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UserDataAccountId(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DisplayName(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DisplayName(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_SourceDisplayName(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_OtherAppReadAccess(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppReadAccess: ...
    @winrt_commethod(12)
    def put_OtherAppReadAccess(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppReadAccess) -> Void: ...
    @winrt_commethod(13)
    def get_OtherAppWriteAccess(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppWriteAccess: ...
    @winrt_commethod(14)
    def put_OtherAppWriteAccess(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppWriteAccess) -> Void: ...
    @winrt_commethod(15)
    def get_LimitedWriteOperations(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskListLimitedWriteOperations: ...
    @winrt_commethod(16)
    def get_SyncManager(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncManager: ...
    @winrt_commethod(17)
    def RegisterSyncManagerAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def GetTaskReader(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskReader: ...
    @winrt_commethod(19)
    def GetTaskReaderWithOptions(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, options: Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryOptions) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskReader: ...
    @winrt_commethod(20)
    def GetTaskAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, userDataTask: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataTasks.UserDataTask]: ...
    @winrt_commethod(21)
    def SaveTaskAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, userDataTask: Windows.ApplicationModel.UserDataTasks.UserDataTask) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(22)
    def DeleteTaskAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, userDataTaskId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(23)
    def DeleteAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(24)
    def SaveAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.Foundation.IAsyncAction: ...
    Id = property(get_Id, None)
    UserDataAccountId = property(get_UserDataAccountId, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    SourceDisplayName = property(get_SourceDisplayName, None)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    OtherAppWriteAccess = property(get_OtherAppWriteAccess, put_OtherAppWriteAccess)
    LimitedWriteOperations = property(get_LimitedWriteOperations, None)
    SyncManager = property(get_SyncManager, None)
class IUserDataTaskListLimitedWriteOperations(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations'
    _iid_ = Guid('{7aa267f2-6078-4183-919e-4f29f19cfae9}')
    @winrt_commethod(6)
    def TryCompleteTaskAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations, userDataTaskId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def TryCreateOrUpdateTaskAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations, userDataTask: Windows.ApplicationModel.UserDataTasks.UserDataTask) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def TryDeleteTaskAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations, userDataTaskId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def TrySkipOccurrenceAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations, userDataTaskId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IUserDataTaskListSyncManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager'
    _iid_ = Guid('{8e591a95-1dcf-469f-93ec-ba48bb553c6b}')
    @winrt_commethod(6)
    def get_LastAttemptedSyncTime(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def put_LastAttemptedSyncTime(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(8)
    def get_LastSuccessfulSyncTime(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def put_LastSuccessfulSyncTime(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(10)
    def get_Status(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncStatus: ...
    @winrt_commethod(11)
    def put_Status(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncStatus) -> Void: ...
    @winrt_commethod(12)
    def SyncAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(13)
    def add_SyncStatusChanged(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncManager, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_SyncStatusChanged(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    LastAttemptedSyncTime = property(get_LastAttemptedSyncTime, put_LastAttemptedSyncTime)
    LastSuccessfulSyncTime = property(get_LastSuccessfulSyncTime, put_LastSuccessfulSyncTime)
    Status = property(get_Status, put_Status)
class IUserDataTaskManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskManager'
    _iid_ = Guid('{8451c914-e60b-48a9-9211-7fb8a56cb84c}')
    @winrt_commethod(6)
    def RequestStoreAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskManager, accessType: Windows.ApplicationModel.UserDataTasks.UserDataTaskStoreAccessType) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataTasks.UserDataTaskStore]: ...
    @winrt_commethod(7)
    def get_User(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskManager) -> Windows.System.User: ...
    User = property(get_User, None)
class IUserDataTaskManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskManagerStatics'
    _iid_ = Guid('{b35539f8-c502-47fc-a81e-100883719d55}')
    @winrt_commethod(6)
    def GetDefault(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskManagerStatics) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskManager: ...
    @winrt_commethod(7)
    def GetForUser(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskManagerStatics, user: Windows.System.User) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskManager: ...
class IUserDataTaskQueryOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions'
    _iid_ = Guid('{959f27ed-909a-4d30-8c1b-331d8fe667e2}')
    @winrt_commethod(6)
    def get_SortProperty(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskQuerySortProperty: ...
    @winrt_commethod(7)
    def put_SortProperty(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskQuerySortProperty) -> Void: ...
    @winrt_commethod(8)
    def get_Kind(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryKind: ...
    @winrt_commethod(9)
    def put_Kind(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryKind) -> Void: ...
    SortProperty = property(get_SortProperty, put_SortProperty)
    Kind = property(get_Kind, put_Kind)
class IUserDataTaskReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskReader'
    _iid_ = Guid('{03e688b1-4ccf-4500-883b-e76290cfed63}')
    @winrt_commethod(6)
    def ReadBatchAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskReader) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataTasks.UserDataTaskBatch]: ...
class IUserDataTaskRecurrenceProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties'
    _iid_ = Guid('{73df80b0-27c6-40ce-b149-9cd41485a69e}')
    @winrt_commethod(6)
    def get_Unit(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceUnit: ...
    @winrt_commethod(7)
    def put_Unit(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceUnit) -> Void: ...
    @winrt_commethod(8)
    def get_Occurrences(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def put_Occurrences(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(10)
    def get_Until(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def put_Until(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(12)
    def get_Interval(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Int32: ...
    @winrt_commethod(13)
    def put_Interval(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_DaysOfWeek(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.Foundation.IReference[Windows.ApplicationModel.UserDataTasks.UserDataTaskDaysOfWeek]: ...
    @winrt_commethod(15)
    def put_DaysOfWeek(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.Foundation.IReference[Windows.ApplicationModel.UserDataTasks.UserDataTaskDaysOfWeek]) -> Void: ...
    @winrt_commethod(16)
    def get_WeekOfMonth(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.Foundation.IReference[Windows.ApplicationModel.UserDataTasks.UserDataTaskWeekOfMonth]: ...
    @winrt_commethod(17)
    def put_WeekOfMonth(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.Foundation.IReference[Windows.ApplicationModel.UserDataTasks.UserDataTaskWeekOfMonth]) -> Void: ...
    @winrt_commethod(18)
    def get_Month(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(19)
    def put_Month(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(20)
    def get_Day(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(21)
    def put_Day(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    Unit = property(get_Unit, put_Unit)
    Occurrences = property(get_Occurrences, put_Occurrences)
    Until = property(get_Until, put_Until)
    Interval = property(get_Interval, put_Interval)
    DaysOfWeek = property(get_DaysOfWeek, put_DaysOfWeek)
    WeekOfMonth = property(get_WeekOfMonth, put_WeekOfMonth)
    Month = property(get_Month, put_Month)
    Day = property(get_Day, put_Day)
class IUserDataTaskRegenerationProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties'
    _iid_ = Guid('{92ab0007-090e-4704-bb5c-84fc0b0d9c31}')
    @winrt_commethod(6)
    def get_Unit(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationUnit: ...
    @winrt_commethod(7)
    def put_Unit(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationUnit) -> Void: ...
    @winrt_commethod(8)
    def get_Occurrences(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def put_Occurrences(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(10)
    def get_Until(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def put_Until(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(12)
    def get_Interval(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties) -> Int32: ...
    @winrt_commethod(13)
    def put_Interval(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties, value: Int32) -> Void: ...
    Unit = property(get_Unit, put_Unit)
    Occurrences = property(get_Occurrences, put_Occurrences)
    Until = property(get_Until, put_Until)
    Interval = property(get_Interval, put_Interval)
class IUserDataTaskStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore'
    _iid_ = Guid('{f06a9cb0-f1db-45ba-8a62-086004c0213d}')
    @winrt_commethod(6)
    def CreateListAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataTasks.UserDataTaskList]: ...
    @winrt_commethod(7)
    def CreateListInAccountAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore, name: WinRT_String, userDataAccountId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataTasks.UserDataTaskList]: ...
    @winrt_commethod(8)
    def FindListsAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.UserDataTasks.UserDataTaskList]]: ...
    @winrt_commethod(9)
    def GetListAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore, taskListId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataTasks.UserDataTaskList]: ...
class UserDataTask(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.IUserDataTask
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTask'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.UserDataTasks.UserDataTask: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ListId(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteId(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CompletedDate(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_CompletedDate(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Details(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Details(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DetailsKind(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskDetailsKind: ...
    @winrt_mixinmethod
    def put_DetailsKind(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskDetailsKind) -> Void: ...
    @winrt_mixinmethod
    def get_DueDate(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_DueDate(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskKind: ...
    @winrt_mixinmethod
    def get_Priority(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskPriority: ...
    @winrt_mixinmethod
    def put_Priority(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskPriority) -> Void: ...
    @winrt_mixinmethod
    def get_RecurrenceProperties(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceProperties: ...
    @winrt_mixinmethod
    def put_RecurrenceProperties(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceProperties) -> Void: ...
    @winrt_mixinmethod
    def get_RegenerationProperties(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationProperties: ...
    @winrt_mixinmethod
    def put_RegenerationProperties(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationProperties) -> Void: ...
    @winrt_mixinmethod
    def get_Reminder(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_Reminder(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Sensitivity(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskSensitivity: ...
    @winrt_mixinmethod
    def put_Sensitivity(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskSensitivity) -> Void: ...
    @winrt_mixinmethod
    def get_Subject(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subject(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_StartDate(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_StartDate(self: Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    Id = property(get_Id, None)
    ListId = property(get_ListId, None)
    RemoteId = property(get_RemoteId, put_RemoteId)
    CompletedDate = property(get_CompletedDate, put_CompletedDate)
    Details = property(get_Details, put_Details)
    DetailsKind = property(get_DetailsKind, put_DetailsKind)
    DueDate = property(get_DueDate, put_DueDate)
    Kind = property(get_Kind, None)
    Priority = property(get_Priority, put_Priority)
    RecurrenceProperties = property(get_RecurrenceProperties, put_RecurrenceProperties)
    RegenerationProperties = property(get_RegenerationProperties, put_RegenerationProperties)
    Reminder = property(get_Reminder, put_Reminder)
    Sensitivity = property(get_Sensitivity, put_Sensitivity)
    Subject = property(get_Subject, put_Subject)
    StartDate = property(get_StartDate, put_StartDate)
class UserDataTaskBatch(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.IUserDataTaskBatch
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskBatch'
    @winrt_mixinmethod
    def get_Tasks(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskBatch) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.UserDataTasks.UserDataTask]: ...
    Tasks = property(get_Tasks, None)
UserDataTaskDaysOfWeek = UInt32
UserDataTaskDaysOfWeek_None: UserDataTaskDaysOfWeek = 0
UserDataTaskDaysOfWeek_Sunday: UserDataTaskDaysOfWeek = 1
UserDataTaskDaysOfWeek_Monday: UserDataTaskDaysOfWeek = 2
UserDataTaskDaysOfWeek_Tuesday: UserDataTaskDaysOfWeek = 4
UserDataTaskDaysOfWeek_Wednesday: UserDataTaskDaysOfWeek = 8
UserDataTaskDaysOfWeek_Thursday: UserDataTaskDaysOfWeek = 16
UserDataTaskDaysOfWeek_Friday: UserDataTaskDaysOfWeek = 32
UserDataTaskDaysOfWeek_Saturday: UserDataTaskDaysOfWeek = 64
UserDataTaskDetailsKind = Int32
UserDataTaskDetailsKind_PlainText: UserDataTaskDetailsKind = 0
UserDataTaskDetailsKind_Html: UserDataTaskDetailsKind = 1
UserDataTaskKind = Int32
UserDataTaskKind_Single: UserDataTaskKind = 0
UserDataTaskKind_Recurring: UserDataTaskKind = 1
UserDataTaskKind_Regenerating: UserDataTaskKind = 2
class UserDataTaskList(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskList'
    @winrt_mixinmethod
    def get_Id(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserDataAccountId(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SourceDisplayName(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OtherAppReadAccess(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppReadAccess: ...
    @winrt_mixinmethod
    def put_OtherAppReadAccess(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppReadAccess) -> Void: ...
    @winrt_mixinmethod
    def get_OtherAppWriteAccess(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppWriteAccess: ...
    @winrt_mixinmethod
    def put_OtherAppWriteAccess(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppWriteAccess) -> Void: ...
    @winrt_mixinmethod
    def get_LimitedWriteOperations(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskListLimitedWriteOperations: ...
    @winrt_mixinmethod
    def get_SyncManager(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncManager: ...
    @winrt_mixinmethod
    def RegisterSyncManagerAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetTaskReader(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskReader: ...
    @winrt_mixinmethod
    def GetTaskReaderWithOptions(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, options: Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryOptions) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskReader: ...
    @winrt_mixinmethod
    def GetTaskAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, userDataTask: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataTasks.UserDataTask]: ...
    @winrt_mixinmethod
    def SaveTaskAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, userDataTask: Windows.ApplicationModel.UserDataTasks.UserDataTask) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteTaskAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, userDataTaskId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SaveAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> Windows.Foundation.IAsyncAction: ...
    Id = property(get_Id, None)
    UserDataAccountId = property(get_UserDataAccountId, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    SourceDisplayName = property(get_SourceDisplayName, None)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    OtherAppWriteAccess = property(get_OtherAppWriteAccess, put_OtherAppWriteAccess)
    LimitedWriteOperations = property(get_LimitedWriteOperations, None)
    SyncManager = property(get_SyncManager, None)
class UserDataTaskListLimitedWriteOperations(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskListLimitedWriteOperations'
    @winrt_mixinmethod
    def TryCompleteTaskAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations, userDataTaskId: WinRT_String) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def TryCreateOrUpdateTaskAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations, userDataTask: Windows.ApplicationModel.UserDataTasks.UserDataTask) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryDeleteTaskAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations, userDataTaskId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySkipOccurrenceAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations, userDataTaskId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
UserDataTaskListOtherAppReadAccess = Int32
UserDataTaskListOtherAppReadAccess_Full: UserDataTaskListOtherAppReadAccess = 0
UserDataTaskListOtherAppReadAccess_SystemOnly: UserDataTaskListOtherAppReadAccess = 1
UserDataTaskListOtherAppReadAccess_None: UserDataTaskListOtherAppReadAccess = 2
UserDataTaskListOtherAppWriteAccess = Int32
UserDataTaskListOtherAppWriteAccess_Limited: UserDataTaskListOtherAppWriteAccess = 0
UserDataTaskListOtherAppWriteAccess_None: UserDataTaskListOtherAppWriteAccess = 1
class UserDataTaskListSyncManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncManager'
    @winrt_mixinmethod
    def get_LastAttemptedSyncTime(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_LastAttemptedSyncTime(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_LastSuccessfulSyncTime(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_LastSuccessfulSyncTime(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, value: Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncStatus: ...
    @winrt_mixinmethod
    def put_Status(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncStatus) -> Void: ...
    @winrt_mixinmethod
    def SyncAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_SyncStatusChanged(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncManager, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SyncStatusChanged(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    LastAttemptedSyncTime = property(get_LastAttemptedSyncTime, put_LastAttemptedSyncTime)
    LastSuccessfulSyncTime = property(get_LastSuccessfulSyncTime, put_LastSuccessfulSyncTime)
    Status = property(get_Status, put_Status)
UserDataTaskListSyncStatus = Int32
UserDataTaskListSyncStatus_Idle: UserDataTaskListSyncStatus = 0
UserDataTaskListSyncStatus_Syncing: UserDataTaskListSyncStatus = 1
UserDataTaskListSyncStatus_UpToDate: UserDataTaskListSyncStatus = 2
UserDataTaskListSyncStatus_AuthenticationError: UserDataTaskListSyncStatus = 3
UserDataTaskListSyncStatus_PolicyError: UserDataTaskListSyncStatus = 4
UserDataTaskListSyncStatus_UnknownError: UserDataTaskListSyncStatus = 5
class UserDataTaskManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.IUserDataTaskManager
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskManager'
    @winrt_mixinmethod
    def RequestStoreAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskManager, accessType: Windows.ApplicationModel.UserDataTasks.UserDataTaskStoreAccessType) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataTasks.UserDataTaskStore]: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskManager) -> Windows.System.User: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.ApplicationModel.UserDataTasks.IUserDataTaskManagerStatics) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskManager: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.ApplicationModel.UserDataTasks.IUserDataTaskManagerStatics, user: Windows.System.User) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskManager: ...
    User = property(get_User, None)
UserDataTaskPriority = Int32
UserDataTaskPriority_Normal: UserDataTaskPriority = 0
UserDataTaskPriority_Low: UserDataTaskPriority = -1
UserDataTaskPriority_High: UserDataTaskPriority = 1
UserDataTaskQueryKind = Int32
UserDataTaskQueryKind_All: UserDataTaskQueryKind = 0
UserDataTaskQueryKind_Incomplete: UserDataTaskQueryKind = 1
UserDataTaskQueryKind_Complete: UserDataTaskQueryKind = 2
class UserDataTaskQueryOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryOptions: ...
    @winrt_mixinmethod
    def get_SortProperty(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskQuerySortProperty: ...
    @winrt_mixinmethod
    def put_SortProperty(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskQuerySortProperty) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryKind: ...
    @winrt_mixinmethod
    def put_Kind(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryKind) -> Void: ...
    SortProperty = property(get_SortProperty, put_SortProperty)
    Kind = property(get_Kind, put_Kind)
UserDataTaskQuerySortProperty = Int32
UserDataTaskQuerySortProperty_DueDate: UserDataTaskQuerySortProperty = 0
class UserDataTaskReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.IUserDataTaskReader
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskReader) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataTasks.UserDataTaskBatch]: ...
class UserDataTaskRecurrenceProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceProperties'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceProperties: ...
    @winrt_mixinmethod
    def get_Unit(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceUnit: ...
    @winrt_mixinmethod
    def put_Unit(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceUnit) -> Void: ...
    @winrt_mixinmethod
    def get_Occurrences(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_Occurrences(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_Until(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_Until(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Interval(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Int32: ...
    @winrt_mixinmethod
    def put_Interval(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_DaysOfWeek(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.Foundation.IReference[Windows.ApplicationModel.UserDataTasks.UserDataTaskDaysOfWeek]: ...
    @winrt_mixinmethod
    def put_DaysOfWeek(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.Foundation.IReference[Windows.ApplicationModel.UserDataTasks.UserDataTaskDaysOfWeek]) -> Void: ...
    @winrt_mixinmethod
    def get_WeekOfMonth(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.Foundation.IReference[Windows.ApplicationModel.UserDataTasks.UserDataTaskWeekOfMonth]: ...
    @winrt_mixinmethod
    def put_WeekOfMonth(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.Foundation.IReference[Windows.ApplicationModel.UserDataTasks.UserDataTaskWeekOfMonth]) -> Void: ...
    @winrt_mixinmethod
    def get_Month(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_Month(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_Day(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_Day(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    Unit = property(get_Unit, put_Unit)
    Occurrences = property(get_Occurrences, put_Occurrences)
    Until = property(get_Until, put_Until)
    Interval = property(get_Interval, put_Interval)
    DaysOfWeek = property(get_DaysOfWeek, put_DaysOfWeek)
    WeekOfMonth = property(get_WeekOfMonth, put_WeekOfMonth)
    Month = property(get_Month, put_Month)
    Day = property(get_Day, put_Day)
UserDataTaskRecurrenceUnit = Int32
UserDataTaskRecurrenceUnit_Daily: UserDataTaskRecurrenceUnit = 0
UserDataTaskRecurrenceUnit_Weekly: UserDataTaskRecurrenceUnit = 1
UserDataTaskRecurrenceUnit_Monthly: UserDataTaskRecurrenceUnit = 2
UserDataTaskRecurrenceUnit_MonthlyOnDay: UserDataTaskRecurrenceUnit = 3
UserDataTaskRecurrenceUnit_Yearly: UserDataTaskRecurrenceUnit = 4
UserDataTaskRecurrenceUnit_YearlyOnDay: UserDataTaskRecurrenceUnit = 5
class UserDataTaskRegenerationProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationProperties'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationProperties: ...
    @winrt_mixinmethod
    def get_Unit(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties) -> Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationUnit: ...
    @winrt_mixinmethod
    def put_Unit(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties, value: Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationUnit) -> Void: ...
    @winrt_mixinmethod
    def get_Occurrences(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties) -> Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_Occurrences(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties, value: Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_Until(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_Until(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Interval(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties) -> Int32: ...
    @winrt_mixinmethod
    def put_Interval(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties, value: Int32) -> Void: ...
    Unit = property(get_Unit, put_Unit)
    Occurrences = property(get_Occurrences, put_Occurrences)
    Until = property(get_Until, put_Until)
    Interval = property(get_Interval, put_Interval)
UserDataTaskRegenerationUnit = Int32
UserDataTaskRegenerationUnit_Daily: UserDataTaskRegenerationUnit = 0
UserDataTaskRegenerationUnit_Weekly: UserDataTaskRegenerationUnit = 1
UserDataTaskRegenerationUnit_Monthly: UserDataTaskRegenerationUnit = 2
UserDataTaskRegenerationUnit_Yearly: UserDataTaskRegenerationUnit = 4
UserDataTaskSensitivity = Int32
UserDataTaskSensitivity_Public: UserDataTaskSensitivity = 0
UserDataTaskSensitivity_Private: UserDataTaskSensitivity = 1
class UserDataTaskStore(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskStore'
    @winrt_mixinmethod
    def CreateListAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore, name: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataTasks.UserDataTaskList]: ...
    @winrt_mixinmethod
    def CreateListInAccountAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore, name: WinRT_String, userDataAccountId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataTasks.UserDataTaskList]: ...
    @winrt_mixinmethod
    def FindListsAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.UserDataTasks.UserDataTaskList]]: ...
    @winrt_mixinmethod
    def GetListAsync(self: Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore, taskListId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserDataTasks.UserDataTaskList]: ...
UserDataTaskStoreAccessType = Int32
UserDataTaskStoreAccessType_AppTasksReadWrite: UserDataTaskStoreAccessType = 0
UserDataTaskStoreAccessType_AllTasksLimitedReadWrite: UserDataTaskStoreAccessType = 1
UserDataTaskWeekOfMonth = Int32
UserDataTaskWeekOfMonth_First: UserDataTaskWeekOfMonth = 0
UserDataTaskWeekOfMonth_Second: UserDataTaskWeekOfMonth = 1
UserDataTaskWeekOfMonth_Third: UserDataTaskWeekOfMonth = 2
UserDataTaskWeekOfMonth_Fourth: UserDataTaskWeekOfMonth = 3
UserDataTaskWeekOfMonth_Last: UserDataTaskWeekOfMonth = 4
make_head(_module, 'IUserDataTask')
make_head(_module, 'IUserDataTaskBatch')
make_head(_module, 'IUserDataTaskList')
make_head(_module, 'IUserDataTaskListLimitedWriteOperations')
make_head(_module, 'IUserDataTaskListSyncManager')
make_head(_module, 'IUserDataTaskManager')
make_head(_module, 'IUserDataTaskManagerStatics')
make_head(_module, 'IUserDataTaskQueryOptions')
make_head(_module, 'IUserDataTaskReader')
make_head(_module, 'IUserDataTaskRecurrenceProperties')
make_head(_module, 'IUserDataTaskRegenerationProperties')
make_head(_module, 'IUserDataTaskStore')
make_head(_module, 'UserDataTask')
make_head(_module, 'UserDataTaskBatch')
make_head(_module, 'UserDataTaskList')
make_head(_module, 'UserDataTaskListLimitedWriteOperations')
make_head(_module, 'UserDataTaskListSyncManager')
make_head(_module, 'UserDataTaskManager')
make_head(_module, 'UserDataTaskQueryOptions')
make_head(_module, 'UserDataTaskReader')
make_head(_module, 'UserDataTaskRecurrenceProperties')
make_head(_module, 'UserDataTaskRegenerationProperties')
make_head(_module, 'UserDataTaskStore')
