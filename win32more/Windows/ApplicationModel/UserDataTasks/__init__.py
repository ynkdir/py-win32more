from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.UserDataTasks
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
class IUserDataTask(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTask'
    _iid_ = Guid('{7c6585d1-e0d4-4f99-aee2-bc2d5ddadf4c}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ListId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_CompletedDate(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def put_CompletedDate(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(12)
    def get_Details(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def put_Details(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(14)
    def get_DetailsKind(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskDetailsKind: ...
    @winrt_commethod(15)
    def put_DetailsKind(self, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskDetailsKind) -> Void: ...
    @winrt_commethod(16)
    def get_DueDate(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(17)
    def put_DueDate(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(18)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskKind: ...
    @winrt_commethod(19)
    def get_Priority(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskPriority: ...
    @winrt_commethod(20)
    def put_Priority(self, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskPriority) -> Void: ...
    @winrt_commethod(21)
    def get_RecurrenceProperties(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceProperties: ...
    @winrt_commethod(22)
    def put_RecurrenceProperties(self, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceProperties) -> Void: ...
    @winrt_commethod(23)
    def get_RegenerationProperties(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationProperties: ...
    @winrt_commethod(24)
    def put_RegenerationProperties(self, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationProperties) -> Void: ...
    @winrt_commethod(25)
    def get_Reminder(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(26)
    def put_Reminder(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(27)
    def get_Sensitivity(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskSensitivity: ...
    @winrt_commethod(28)
    def put_Sensitivity(self, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskSensitivity) -> Void: ...
    @winrt_commethod(29)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(30)
    def put_Subject(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(31)
    def get_StartDate(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(32)
    def put_StartDate(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    CompletedDate = property(get_CompletedDate, put_CompletedDate)
    Details = property(get_Details, put_Details)
    DetailsKind = property(get_DetailsKind, put_DetailsKind)
    DueDate = property(get_DueDate, put_DueDate)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    ListId = property(get_ListId, None)
    Priority = property(get_Priority, put_Priority)
    RecurrenceProperties = property(get_RecurrenceProperties, put_RecurrenceProperties)
    RegenerationProperties = property(get_RegenerationProperties, put_RegenerationProperties)
    Reminder = property(get_Reminder, put_Reminder)
    RemoteId = property(get_RemoteId, put_RemoteId)
    Sensitivity = property(get_Sensitivity, put_Sensitivity)
    StartDate = property(get_StartDate, put_StartDate)
    Subject = property(get_Subject, put_Subject)
class IUserDataTaskBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskBatch'
    _iid_ = Guid('{382da5fe-20b5-431c-8f42-a5d292ec930c}')
    @winrt_commethod(6)
    def get_Tasks(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask]: ...
    Tasks = property(get_Tasks, None)
class IUserDataTaskList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskList'
    _iid_ = Guid('{49412e39-7c1d-4df1-bed3-314b7cbf5e4e}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UserDataAccountId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_SourceDisplayName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_OtherAppReadAccess(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppReadAccess: ...
    @winrt_commethod(12)
    def put_OtherAppReadAccess(self, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppReadAccess) -> Void: ...
    @winrt_commethod(13)
    def get_OtherAppWriteAccess(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppWriteAccess: ...
    @winrt_commethod(14)
    def put_OtherAppWriteAccess(self, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppWriteAccess) -> Void: ...
    @winrt_commethod(15)
    def get_LimitedWriteOperations(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListLimitedWriteOperations: ...
    @winrt_commethod(16)
    def get_SyncManager(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncManager: ...
    @winrt_commethod(17)
    def RegisterSyncManagerAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def GetTaskReader(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskReader: ...
    @winrt_commethod(19)
    def GetTaskReaderWithOptions(self, options: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryOptions) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskReader: ...
    @winrt_commethod(20)
    def GetTaskAsync(self, userDataTask: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask]: ...
    @winrt_commethod(21)
    def SaveTaskAsync(self, userDataTask: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(22)
    def DeleteTaskAsync(self, userDataTaskId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(23)
    def DeleteAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(24)
    def SaveAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    Id = property(get_Id, None)
    LimitedWriteOperations = property(get_LimitedWriteOperations, None)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    OtherAppWriteAccess = property(get_OtherAppWriteAccess, put_OtherAppWriteAccess)
    SourceDisplayName = property(get_SourceDisplayName, None)
    SyncManager = property(get_SyncManager, None)
    UserDataAccountId = property(get_UserDataAccountId, None)
class IUserDataTaskListLimitedWriteOperations(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations'
    _iid_ = Guid('{7aa267f2-6078-4183-919e-4f29f19cfae9}')
    @winrt_commethod(6)
    def TryCompleteTaskAsync(self, userDataTaskId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def TryCreateOrUpdateTaskAsync(self, userDataTask: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def TryDeleteTaskAsync(self, userDataTaskId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(9)
    def TrySkipOccurrenceAsync(self, userDataTaskId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IUserDataTaskListSyncManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager'
    _iid_ = Guid('{8e591a95-1dcf-469f-93ec-ba48bb553c6b}')
    @winrt_commethod(6)
    def get_LastAttemptedSyncTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def put_LastAttemptedSyncTime(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(8)
    def get_LastSuccessfulSyncTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def put_LastSuccessfulSyncTime(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(10)
    def get_Status(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncStatus: ...
    @winrt_commethod(11)
    def put_Status(self, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncStatus) -> Void: ...
    @winrt_commethod(12)
    def SyncAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(13)
    def add_SyncStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_SyncStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    LastAttemptedSyncTime = property(get_LastAttemptedSyncTime, put_LastAttemptedSyncTime)
    LastSuccessfulSyncTime = property(get_LastSuccessfulSyncTime, put_LastSuccessfulSyncTime)
    Status = property(get_Status, put_Status)
    SyncStatusChanged = event()
class IUserDataTaskManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskManager'
    _iid_ = Guid('{8451c914-e60b-48a9-9211-7fb8a56cb84c}')
    @winrt_commethod(6)
    def RequestStoreAsync(self, accessType: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskStore]: ...
    @winrt_commethod(7)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IUserDataTaskManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskManagerStatics'
    _iid_ = Guid('{b35539f8-c502-47fc-a81e-100883719d55}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskManager: ...
    @winrt_commethod(7)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskManager: ...
class IUserDataTaskQueryOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions'
    _iid_ = Guid('{959f27ed-909a-4d30-8c1b-331d8fe667e2}')
    @winrt_commethod(6)
    def get_SortProperty(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskQuerySortProperty: ...
    @winrt_commethod(7)
    def put_SortProperty(self, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskQuerySortProperty) -> Void: ...
    @winrt_commethod(8)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryKind: ...
    @winrt_commethod(9)
    def put_Kind(self, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryKind) -> Void: ...
    Kind = property(get_Kind, put_Kind)
    SortProperty = property(get_SortProperty, put_SortProperty)
class IUserDataTaskReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskReader'
    _iid_ = Guid('{03e688b1-4ccf-4500-883b-e76290cfed63}')
    @winrt_commethod(6)
    def ReadBatchAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskBatch]: ...
class IUserDataTaskRecurrenceProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties'
    _iid_ = Guid('{73df80b0-27c6-40ce-b149-9cd41485a69e}')
    @winrt_commethod(6)
    def get_Unit(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceUnit: ...
    @winrt_commethod(7)
    def put_Unit(self, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceUnit) -> Void: ...
    @winrt_commethod(8)
    def get_Occurrences(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def put_Occurrences(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(10)
    def get_Until(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def put_Until(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(12)
    def get_Interval(self) -> Int32: ...
    @winrt_commethod(13)
    def put_Interval(self, value: Int32) -> Void: ...
    @winrt_commethod(14)
    def get_DaysOfWeek(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskDaysOfWeek]: ...
    @winrt_commethod(15)
    def put_DaysOfWeek(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskDaysOfWeek]) -> Void: ...
    @winrt_commethod(16)
    def get_WeekOfMonth(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskWeekOfMonth]: ...
    @winrt_commethod(17)
    def put_WeekOfMonth(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskWeekOfMonth]) -> Void: ...
    @winrt_commethod(18)
    def get_Month(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(19)
    def put_Month(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(20)
    def get_Day(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(21)
    def put_Day(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    Day = property(get_Day, put_Day)
    DaysOfWeek = property(get_DaysOfWeek, put_DaysOfWeek)
    Interval = property(get_Interval, put_Interval)
    Month = property(get_Month, put_Month)
    Occurrences = property(get_Occurrences, put_Occurrences)
    Unit = property(get_Unit, put_Unit)
    Until = property(get_Until, put_Until)
    WeekOfMonth = property(get_WeekOfMonth, put_WeekOfMonth)
class IUserDataTaskRegenerationProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties'
    _iid_ = Guid('{92ab0007-090e-4704-bb5c-84fc0b0d9c31}')
    @winrt_commethod(6)
    def get_Unit(self) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationUnit: ...
    @winrt_commethod(7)
    def put_Unit(self, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationUnit) -> Void: ...
    @winrt_commethod(8)
    def get_Occurrences(self) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_commethod(9)
    def put_Occurrences(self, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_commethod(10)
    def get_Until(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(11)
    def put_Until(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(12)
    def get_Interval(self) -> Int32: ...
    @winrt_commethod(13)
    def put_Interval(self, value: Int32) -> Void: ...
    Interval = property(get_Interval, put_Interval)
    Occurrences = property(get_Occurrences, put_Occurrences)
    Unit = property(get_Unit, put_Unit)
    Until = property(get_Until, put_Until)
class IUserDataTaskStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore'
    _iid_ = Guid('{f06a9cb0-f1db-45ba-8a62-086004c0213d}')
    @winrt_commethod(6)
    def CreateListAsync(self, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskList]: ...
    @winrt_commethod(7)
    def CreateListInAccountAsync(self, name: WinRT_String, userDataAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskList]: ...
    @winrt_commethod(8)
    def FindListsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskList]]: ...
    @winrt_commethod(9)
    def GetListAsync(self, taskListId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskList]: ...
class UserDataTask(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTask'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ListId(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RemoteId(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CompletedDate(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_CompletedDate(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Details(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Details(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DetailsKind(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskDetailsKind: ...
    @winrt_mixinmethod
    def put_DetailsKind(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskDetailsKind) -> Void: ...
    @winrt_mixinmethod
    def get_DueDate(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_DueDate(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskKind: ...
    @winrt_mixinmethod
    def get_Priority(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskPriority: ...
    @winrt_mixinmethod
    def put_Priority(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskPriority) -> Void: ...
    @winrt_mixinmethod
    def get_RecurrenceProperties(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceProperties: ...
    @winrt_mixinmethod
    def put_RecurrenceProperties(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceProperties) -> Void: ...
    @winrt_mixinmethod
    def get_RegenerationProperties(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationProperties: ...
    @winrt_mixinmethod
    def put_RegenerationProperties(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationProperties) -> Void: ...
    @winrt_mixinmethod
    def get_Reminder(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_Reminder(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Sensitivity(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskSensitivity: ...
    @winrt_mixinmethod
    def put_Sensitivity(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskSensitivity) -> Void: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subject(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_StartDate(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_StartDate(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTask, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    CompletedDate = property(get_CompletedDate, put_CompletedDate)
    Details = property(get_Details, put_Details)
    DetailsKind = property(get_DetailsKind, put_DetailsKind)
    DueDate = property(get_DueDate, put_DueDate)
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    ListId = property(get_ListId, None)
    Priority = property(get_Priority, put_Priority)
    RecurrenceProperties = property(get_RecurrenceProperties, put_RecurrenceProperties)
    RegenerationProperties = property(get_RegenerationProperties, put_RegenerationProperties)
    Reminder = property(get_Reminder, put_Reminder)
    RemoteId = property(get_RemoteId, put_RemoteId)
    Sensitivity = property(get_Sensitivity, put_Sensitivity)
    StartDate = property(get_StartDate, put_StartDate)
    Subject = property(get_Subject, put_Subject)
class UserDataTaskBatch(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskBatch
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskBatch'
    @winrt_mixinmethod
    def get_Tasks(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskBatch) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask]: ...
    Tasks = property(get_Tasks, None)
class UserDataTaskDaysOfWeek(Enum, UInt32):
    None_ = 0
    Sunday = 1
    Monday = 2
    Tuesday = 4
    Wednesday = 8
    Thursday = 16
    Friday = 32
    Saturday = 64
class UserDataTaskDetailsKind(Enum, Int32):
    PlainText = 0
    Html = 1
class UserDataTaskKind(Enum, Int32):
    Single = 0
    Recurring = 1
    Regenerating = 2
class UserDataTaskList(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskList'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserDataAccountId(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_SourceDisplayName(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OtherAppReadAccess(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppReadAccess: ...
    @winrt_mixinmethod
    def put_OtherAppReadAccess(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppReadAccess) -> Void: ...
    @winrt_mixinmethod
    def get_OtherAppWriteAccess(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppWriteAccess: ...
    @winrt_mixinmethod
    def put_OtherAppWriteAccess(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListOtherAppWriteAccess) -> Void: ...
    @winrt_mixinmethod
    def get_LimitedWriteOperations(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListLimitedWriteOperations: ...
    @winrt_mixinmethod
    def get_SyncManager(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncManager: ...
    @winrt_mixinmethod
    def RegisterSyncManagerAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetTaskReader(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskReader: ...
    @winrt_mixinmethod
    def GetTaskReaderWithOptions(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, options: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryOptions) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskReader: ...
    @winrt_mixinmethod
    def GetTaskAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, userDataTask: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask]: ...
    @winrt_mixinmethod
    def SaveTaskAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, userDataTask: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteTaskAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList, userDataTaskId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskList) -> win32more.Windows.Foundation.IAsyncAction: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    Id = property(get_Id, None)
    LimitedWriteOperations = property(get_LimitedWriteOperations, None)
    OtherAppReadAccess = property(get_OtherAppReadAccess, put_OtherAppReadAccess)
    OtherAppWriteAccess = property(get_OtherAppWriteAccess, put_OtherAppWriteAccess)
    SourceDisplayName = property(get_SourceDisplayName, None)
    SyncManager = property(get_SyncManager, None)
    UserDataAccountId = property(get_UserDataAccountId, None)
class UserDataTaskListLimitedWriteOperations(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskListLimitedWriteOperations'
    @winrt_mixinmethod
    def TryCompleteTaskAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations, userDataTaskId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def TryCreateOrUpdateTaskAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations, userDataTask: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTask) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryDeleteTaskAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations, userDataTaskId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySkipOccurrenceAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListLimitedWriteOperations, userDataTaskId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class UserDataTaskListOtherAppReadAccess(Enum, Int32):
    Full = 0
    SystemOnly = 1
    None_ = 2
class UserDataTaskListOtherAppWriteAccess(Enum, Int32):
    Limited = 0
    None_ = 1
class UserDataTaskListSyncManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncManager'
    @winrt_mixinmethod
    def get_LastAttemptedSyncTime(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_LastAttemptedSyncTime(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_LastSuccessfulSyncTime(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_LastSuccessfulSyncTime(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncStatus: ...
    @winrt_mixinmethod
    def put_Status(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncStatus) -> Void: ...
    @winrt_mixinmethod
    def SyncAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_SyncStatusChanged(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskListSyncManager, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SyncStatusChanged(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskListSyncManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    LastAttemptedSyncTime = property(get_LastAttemptedSyncTime, put_LastAttemptedSyncTime)
    LastSuccessfulSyncTime = property(get_LastSuccessfulSyncTime, put_LastSuccessfulSyncTime)
    Status = property(get_Status, put_Status)
    SyncStatusChanged = event()
class UserDataTaskListSyncStatus(Enum, Int32):
    Idle = 0
    Syncing = 1
    UpToDate = 2
    AuthenticationError = 3
    PolicyError = 4
    UnknownError = 5
class UserDataTaskManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskManager
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskManager'
    @winrt_mixinmethod
    def RequestStoreAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskManager, accessType: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskStoreAccessType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskStore]: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskManager) -> win32more.Windows.System.User: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskManagerStatics) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskManager: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskManagerStatics, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskManager: ...
    User = property(get_User, None)
class UserDataTaskPriority(Enum, Int32):
    Normal = 0
    Low = -1
    High = 1
class UserDataTaskQueryKind(Enum, Int32):
    All = 0
    Incomplete = 1
    Complete = 2
class UserDataTaskQueryOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryOptions: ...
    @winrt_mixinmethod
    def get_SortProperty(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskQuerySortProperty: ...
    @winrt_mixinmethod
    def put_SortProperty(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskQuerySortProperty) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskQueryOptions, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskQueryKind) -> Void: ...
    Kind = property(get_Kind, put_Kind)
    SortProperty = property(get_SortProperty, put_SortProperty)
class UserDataTaskQuerySortProperty(Enum, Int32):
    DueDate = 0
class UserDataTaskReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskReader
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskReader'
    @winrt_mixinmethod
    def ReadBatchAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskBatch]: ...
class UserDataTaskRecurrenceProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceProperties'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceProperties.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceProperties: ...
    @winrt_mixinmethod
    def get_Unit(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceUnit: ...
    @winrt_mixinmethod
    def put_Unit(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRecurrenceUnit) -> Void: ...
    @winrt_mixinmethod
    def get_Occurrences(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_Occurrences(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_Until(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_Until(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Interval(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> Int32: ...
    @winrt_mixinmethod
    def put_Interval(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_DaysOfWeek(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskDaysOfWeek]: ...
    @winrt_mixinmethod
    def put_DaysOfWeek(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskDaysOfWeek]) -> Void: ...
    @winrt_mixinmethod
    def get_WeekOfMonth(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskWeekOfMonth]: ...
    @winrt_mixinmethod
    def put_WeekOfMonth(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: win32more.Windows.Foundation.IReference[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskWeekOfMonth]) -> Void: ...
    @winrt_mixinmethod
    def get_Month(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_Month(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_Day(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_Day(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRecurrenceProperties, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    Day = property(get_Day, put_Day)
    DaysOfWeek = property(get_DaysOfWeek, put_DaysOfWeek)
    Interval = property(get_Interval, put_Interval)
    Month = property(get_Month, put_Month)
    Occurrences = property(get_Occurrences, put_Occurrences)
    Unit = property(get_Unit, put_Unit)
    Until = property(get_Until, put_Until)
    WeekOfMonth = property(get_WeekOfMonth, put_WeekOfMonth)
class UserDataTaskRecurrenceUnit(Enum, Int32):
    Daily = 0
    Weekly = 1
    Monthly = 2
    MonthlyOnDay = 3
    Yearly = 4
    YearlyOnDay = 5
class UserDataTaskRegenerationProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationProperties'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationProperties.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationProperties: ...
    @winrt_mixinmethod
    def get_Unit(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties) -> win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationUnit: ...
    @winrt_mixinmethod
    def put_Unit(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties, value: win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskRegenerationUnit) -> Void: ...
    @winrt_mixinmethod
    def get_Occurrences(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties) -> win32more.Windows.Foundation.IReference[Int32]: ...
    @winrt_mixinmethod
    def put_Occurrences(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties, value: win32more.Windows.Foundation.IReference[Int32]) -> Void: ...
    @winrt_mixinmethod
    def get_Until(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_Until(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Interval(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties) -> Int32: ...
    @winrt_mixinmethod
    def put_Interval(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskRegenerationProperties, value: Int32) -> Void: ...
    Interval = property(get_Interval, put_Interval)
    Occurrences = property(get_Occurrences, put_Occurrences)
    Unit = property(get_Unit, put_Unit)
    Until = property(get_Until, put_Until)
class UserDataTaskRegenerationUnit(Enum, Int32):
    Daily = 0
    Weekly = 1
    Monthly = 2
    Yearly = 4
class UserDataTaskSensitivity(Enum, Int32):
    Public = 0
    Private = 1
class UserDataTaskStore(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore
    _classid_ = 'Windows.ApplicationModel.UserDataTasks.UserDataTaskStore'
    @winrt_mixinmethod
    def CreateListAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore, name: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskList]: ...
    @winrt_mixinmethod
    def CreateListInAccountAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore, name: WinRT_String, userDataAccountId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskList]: ...
    @winrt_mixinmethod
    def FindListsAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskList]]: ...
    @winrt_mixinmethod
    def GetListAsync(self: win32more.Windows.ApplicationModel.UserDataTasks.IUserDataTaskStore, taskListId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserDataTasks.UserDataTaskList]: ...
class UserDataTaskStoreAccessType(Enum, Int32):
    AppTasksReadWrite = 0
    AllTasksLimitedReadWrite = 1
class UserDataTaskWeekOfMonth(Enum, Int32):
    First = 0
    Second = 1
    Third = 2
    Fourth = 3
    Last = 4


make_ready(__name__)
