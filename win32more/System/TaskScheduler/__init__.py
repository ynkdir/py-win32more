from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.TaskScheduler
import win32more.UI.Controls
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
TASK_SUNDAY: UInt32 = 1
TASK_MONDAY: UInt32 = 2
TASK_TUESDAY: UInt32 = 4
TASK_WEDNESDAY: UInt32 = 8
TASK_THURSDAY: UInt32 = 16
TASK_FRIDAY: UInt32 = 32
TASK_SATURDAY: UInt32 = 64
TASK_FIRST_WEEK: UInt32 = 1
TASK_SECOND_WEEK: UInt32 = 2
TASK_THIRD_WEEK: UInt32 = 3
TASK_FOURTH_WEEK: UInt32 = 4
TASK_LAST_WEEK: UInt32 = 5
TASK_JANUARY: UInt32 = 1
TASK_FEBRUARY: UInt32 = 2
TASK_MARCH: UInt32 = 4
TASK_APRIL: UInt32 = 8
TASK_MAY: UInt32 = 16
TASK_JUNE: UInt32 = 32
TASK_JULY: UInt32 = 64
TASK_AUGUST: UInt32 = 128
TASK_SEPTEMBER: UInt32 = 256
TASK_OCTOBER: UInt32 = 512
TASK_NOVEMBER: UInt32 = 1024
TASK_DECEMBER: UInt32 = 2048
TASK_FLAG_INTERACTIVE: UInt32 = 1
TASK_FLAG_DELETE_WHEN_DONE: UInt32 = 2
TASK_FLAG_DISABLED: UInt32 = 4
TASK_FLAG_START_ONLY_IF_IDLE: UInt32 = 16
TASK_FLAG_KILL_ON_IDLE_END: UInt32 = 32
TASK_FLAG_DONT_START_IF_ON_BATTERIES: UInt32 = 64
TASK_FLAG_KILL_IF_GOING_ON_BATTERIES: UInt32 = 128
TASK_FLAG_RUN_ONLY_IF_DOCKED: UInt32 = 256
TASK_FLAG_HIDDEN: UInt32 = 512
TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET: UInt32 = 1024
TASK_FLAG_RESTART_ON_IDLE_RESUME: UInt32 = 2048
TASK_FLAG_SYSTEM_REQUIRED: UInt32 = 4096
TASK_FLAG_RUN_ONLY_IF_LOGGED_ON: UInt32 = 8192
TASK_TRIGGER_FLAG_HAS_END_DATE: UInt32 = 1
TASK_TRIGGER_FLAG_KILL_AT_DURATION_END: UInt32 = 2
TASK_TRIGGER_FLAG_DISABLED: UInt32 = 4
TASK_MAX_RUN_TIMES: UInt32 = 1440
CLSID_CTask: Guid = Guid('148bd520-a2ab-11ce-b1-1f-00-aa-00-53-05-03')
CLSID_CTaskScheduler: Guid = Guid('148bd52a-a2ab-11ce-b1-1f-00-aa-00-53-05-03')
class DAILY(Structure):
    DaysInterval: UInt16
class IAction(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('bae54997-48b1-4cbe-99-65-d6-be-26-3e-be-a4')
    @commethod(7)
    def get_Id(pId: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Id(Id: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Type(pType: POINTER(win32more.System.TaskScheduler.TASK_ACTION_TYPE)) -> win32more.Foundation.HRESULT: ...
class IActionCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('02820e19-7b98-4ed2-b2-e8-fd-cc-ce-ff-61-9b')
    @commethod(7)
    def get_Count(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: Int32, ppAction: POINTER(win32more.System.TaskScheduler.IAction_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ppEnum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_XmlText(pText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_XmlText(text: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Create(type: win32more.System.TaskScheduler.TASK_ACTION_TYPE, ppAction: POINTER(win32more.System.TaskScheduler.IAction_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Remove(index: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Clear() -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Context(pContext: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_Context(context: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IBootTrigger(c_void_p):
    extends: win32more.System.TaskScheduler.ITrigger
    Guid = Guid('2a9c35da-d357-41f4-bb-c1-20-7a-c1-b1-f3-cb')
    @commethod(20)
    def get_Delay(pDelay: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_Delay(delay: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IComHandlerAction(c_void_p):
    extends: win32more.System.TaskScheduler.IAction
    Guid = Guid('6d2fd252-75c5-4f66-90-ba-2a-7d-8c-c3-03-9f')
    @commethod(10)
    def get_ClassId(pClsid: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_ClassId(clsid: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Data(pData: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Data(data: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IDailyTrigger(c_void_p):
    extends: win32more.System.TaskScheduler.ITrigger
    Guid = Guid('126c5cd8-b288-41d5-8d-bf-e4-91-44-6a-dc-5c')
    @commethod(20)
    def get_DaysInterval(pDays: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_DaysInterval(days: Int16) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_RandomDelay(pRandomDelay: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_RandomDelay(randomDelay: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IEmailAction(c_void_p):
    extends: win32more.System.TaskScheduler.IAction
    Guid = Guid('10f62c64-7e16-4314-a0-c2-0c-36-83-f9-9d-40')
    @commethod(10)
    def get_Server(pServer: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Server(server: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Subject(pSubject: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Subject(subject: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_To(pTo: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_To(to: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_Cc(pCc: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_Cc(cc: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_Bcc(pBcc: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_Bcc(bcc: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_ReplyTo(pReplyTo: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_ReplyTo(replyTo: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_From(pFrom: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_From(from_: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_HeaderFields(ppHeaderFields: POINTER(win32more.System.TaskScheduler.ITaskNamedValueCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_HeaderFields(pHeaderFields: win32more.System.TaskScheduler.ITaskNamedValueCollection_head) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_Body(pBody: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_Body(body: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_Attachments(pAttachements: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_Attachments(pAttachements: POINTER(win32more.System.Com.SAFEARRAY_head)) -> win32more.Foundation.HRESULT: ...
class IEnumWorkItems(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('148bd528-a2ab-11ce-b1-1f-00-aa-00-53-05-03')
    @commethod(3)
    def Next(celt: UInt32, rgpwszNames: POINTER(POINTER(win32more.Foundation.PWSTR)), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnumWorkItems: POINTER(win32more.System.TaskScheduler.IEnumWorkItems_head)) -> win32more.Foundation.HRESULT: ...
class IEventTrigger(c_void_p):
    extends: win32more.System.TaskScheduler.ITrigger
    Guid = Guid('d45b0167-9653-4eef-b9-4f-07-32-ca-7a-f2-51')
    @commethod(20)
    def get_Subscription(pQuery: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_Subscription(query: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_Delay(pDelay: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_Delay(delay: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_ValueQueries(ppNamedXPaths: POINTER(win32more.System.TaskScheduler.ITaskNamedValueCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_ValueQueries(pNamedXPaths: win32more.System.TaskScheduler.ITaskNamedValueCollection_head) -> win32more.Foundation.HRESULT: ...
class IExecAction(c_void_p):
    extends: win32more.System.TaskScheduler.IAction
    Guid = Guid('4c3d624d-fd6b-49a3-b9-b7-09-cb-3c-d3-f0-47')
    @commethod(10)
    def get_Path(pPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Path(path: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Arguments(pArgument: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_Arguments(argument: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_WorkingDirectory(pWorkingDirectory: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_WorkingDirectory(workingDirectory: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IExecAction2(c_void_p):
    extends: win32more.System.TaskScheduler.IExecAction
    Guid = Guid('f2a82542-bda5-4e6b-91-43-e2-bf-4f-89-87-b6')
    @commethod(16)
    def get_HideAppWindow(pHideAppWindow: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_HideAppWindow(hideAppWindow: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IIdleSettings(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('84594461-0053-4342-a8-fd-08-8f-ab-f1-1f-32')
    @commethod(7)
    def get_IdleDuration(pDelay: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_IdleDuration(delay: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_WaitTimeout(pTimeout: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_WaitTimeout(timeout: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_StopOnIdleEnd(pStop: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_StopOnIdleEnd(stop: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_RestartOnIdle(pRestart: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_RestartOnIdle(restart: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IIdleTrigger(c_void_p):
    extends: win32more.System.TaskScheduler.ITrigger
    Guid = Guid('d537d2b0-9fb3-4d34-97-39-1f-f5-ce-7b-1e-f3')
class ILogonTrigger(c_void_p):
    extends: win32more.System.TaskScheduler.ITrigger
    Guid = Guid('72dade38-fae4-4b3e-ba-f4-5d-00-9a-f0-2b-1c')
    @commethod(20)
    def get_Delay(pDelay: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_Delay(delay: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_UserId(pUser: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_UserId(user: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IMaintenanceSettings(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('a6024fa8-9652-4adb-a6-bf-5c-fc-d8-77-a7-ba')
    @commethod(7)
    def put_Period(value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Period(target: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_Deadline(value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Deadline(target: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Exclusive(value: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_Exclusive(target: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class IMonthlyDOWTrigger(c_void_p):
    extends: win32more.System.TaskScheduler.ITrigger
    Guid = Guid('77d025a3-90fa-43aa-b5-2e-cd-a5-49-9b-94-6a')
    @commethod(20)
    def get_DaysOfWeek(pDays: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_DaysOfWeek(days: Int16) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_WeeksOfMonth(pWeeks: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_WeeksOfMonth(weeks: Int16) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_MonthsOfYear(pMonths: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_MonthsOfYear(months: Int16) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_RunOnLastWeekOfMonth(pLastWeek: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_RunOnLastWeekOfMonth(lastWeek: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_RandomDelay(pRandomDelay: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_RandomDelay(randomDelay: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IMonthlyTrigger(c_void_p):
    extends: win32more.System.TaskScheduler.ITrigger
    Guid = Guid('97c45ef1-6b02-4a1a-9c-0e-1e-bf-ba-15-00-ac')
    @commethod(20)
    def get_DaysOfMonth(pDays: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_DaysOfMonth(days: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_MonthsOfYear(pMonths: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_MonthsOfYear(months: Int16) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_RunOnLastDayOfMonth(pLastDay: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_RunOnLastDayOfMonth(lastDay: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_RandomDelay(pRandomDelay: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_RandomDelay(randomDelay: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class INetworkSettings(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('9f7dea84-c30b-4245-80-b6-00-e9-f6-46-f1-b4')
    @commethod(7)
    def get_Name(pName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Id(pId: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Id(id: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IPrincipal(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d98d51e5-c9b4-496a-a9-c1-18-98-02-61-cf-0f')
    @commethod(7)
    def get_Id(pId: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Id(Id: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_DisplayName(pName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_DisplayName(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_UserId(pUser: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_UserId(user: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_LogonType(pLogon: POINTER(win32more.System.TaskScheduler.TASK_LOGON_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_LogonType(logon: win32more.System.TaskScheduler.TASK_LOGON_TYPE) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_GroupId(pGroup: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_GroupId(group: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_RunLevel(pRunLevel: POINTER(win32more.System.TaskScheduler.TASK_RUNLEVEL_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_RunLevel(runLevel: win32more.System.TaskScheduler.TASK_RUNLEVEL_TYPE) -> win32more.Foundation.HRESULT: ...
class IPrincipal2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('248919ae-e345-4a6d-8a-eb-e0-d3-16-5c-90-4e')
    @commethod(7)
    def get_ProcessTokenSidType(pProcessTokenSidType: POINTER(win32more.System.TaskScheduler.TASK_PROCESSTOKENSID_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_ProcessTokenSidType(processTokenSidType: win32more.System.TaskScheduler.TASK_PROCESSTOKENSID_TYPE) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_RequiredPrivilegeCount(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_RequiredPrivilege(index: Int32, pPrivilege: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def AddRequiredPrivilege(privilege: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IProvideTaskPage(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4086658a-cbbb-11cf-b6-04-00-c0-4f-d8-d5-65')
    @commethod(3)
    def GetPage(tpType: win32more.System.TaskScheduler.TASKPAGE, fPersistChanges: win32more.Foundation.BOOL, phPage: POINTER(win32more.UI.Controls.HPROPSHEETPAGE)) -> win32more.Foundation.HRESULT: ...
class IRegisteredTask(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('9c86f320-dee3-4dd1-b9-72-a3-03-f2-6b-06-1e')
    @commethod(7)
    def get_Name(pName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Path(pPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_State(pState: POINTER(win32more.System.TaskScheduler.TASK_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Enabled(pEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Enabled(enabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Run(params: win32more.System.Com.VARIANT, ppRunningTask: POINTER(win32more.System.TaskScheduler.IRunningTask_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def RunEx(params: win32more.System.Com.VARIANT, flags: Int32, sessionID: Int32, user: win32more.Foundation.BSTR, ppRunningTask: POINTER(win32more.System.TaskScheduler.IRunningTask_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetInstances(flags: Int32, ppRunningTasks: POINTER(win32more.System.TaskScheduler.IRunningTaskCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_LastRunTime(pLastRunTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_LastTaskResult(pLastTaskResult: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_NumberOfMissedRuns(pNumberOfMissedRuns: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_NextRunTime(pNextRunTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_Definition(ppDefinition: POINTER(win32more.System.TaskScheduler.ITaskDefinition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_Xml(pXml: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetSecurityDescriptor(securityInformation: Int32, pSddl: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SetSecurityDescriptor(sddl: win32more.Foundation.BSTR, flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def Stop(flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetRunTimes(pstStart: POINTER(win32more.Foundation.SYSTEMTIME_head), pstEnd: POINTER(win32more.Foundation.SYSTEMTIME_head), pCount: POINTER(UInt32), pRunTimes: POINTER(POINTER(win32more.Foundation.SYSTEMTIME_head))) -> win32more.Foundation.HRESULT: ...
class IRegisteredTaskCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('86627eb4-42a7-41e4-a4-d9-ac-33-a7-2f-2d-52')
    @commethod(7)
    def get_Count(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: win32more.System.Com.VARIANT, ppRegisteredTask: POINTER(win32more.System.TaskScheduler.IRegisteredTask_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ppEnum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IRegistrationInfo(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('416d8b73-cb41-4ea1-80-5c-9b-e9-a5-ac-4a-74')
    @commethod(7)
    def get_Description(pDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Description(description: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Author(pAuthor: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Author(author: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Version(pVersion: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_Version(version: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Date(pDate: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Date(date: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Documentation(pDocumentation: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_Documentation(documentation: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_XmlText(pText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_XmlText(text: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_URI(pUri: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_URI(uri: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_SecurityDescriptor(pSddl: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_SecurityDescriptor(sddl: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_Source(pSource: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_Source(source: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IRegistrationTrigger(c_void_p):
    extends: win32more.System.TaskScheduler.ITrigger
    Guid = Guid('4c8fec3a-c218-4e0c-b2-3d-62-90-24-db-91-a2')
    @commethod(20)
    def get_Delay(pDelay: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_Delay(delay: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class IRepetitionPattern(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('7fb9acf1-26be-400e-85-b5-29-4b-9c-75-df-d6')
    @commethod(7)
    def get_Interval(pInterval: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Interval(interval: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Duration(pDuration: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Duration(duration: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_StopAtDurationEnd(pStop: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_StopAtDurationEnd(stop: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class IRunningTask(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('653758fb-7b9a-4f1e-a4-71-be-eb-8e-9b-83-4e')
    @commethod(7)
    def get_Name(pName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_InstanceGuid(pGuid: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Path(pPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_State(pState: POINTER(win32more.System.TaskScheduler.TASK_STATE)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_CurrentAction(pName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Stop() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Refresh() -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_EnginePID(pPID: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IRunningTaskCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('6a67614b-6828-4fec-aa-54-6d-52-e8-f1-f2-db')
    @commethod(7)
    def get_Count(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: win32more.System.Com.VARIANT, ppRunningTask: POINTER(win32more.System.TaskScheduler.IRunningTask_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ppEnum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IScheduledWorkItem(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a6b952f0-a4b1-11d0-99-7d-00-aa-00-68-87-ec')
    @commethod(3)
    def CreateTrigger(piNewTrigger: POINTER(UInt16), ppTrigger: POINTER(win32more.System.TaskScheduler.ITaskTrigger_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteTrigger(iTrigger: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTriggerCount(pwCount: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTrigger(iTrigger: UInt16, ppTrigger: POINTER(win32more.System.TaskScheduler.ITaskTrigger_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetTriggerString(iTrigger: UInt16, ppwszTrigger: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRunTimes(pstBegin: POINTER(win32more.Foundation.SYSTEMTIME_head), pstEnd: POINTER(win32more.Foundation.SYSTEMTIME_head), pCount: POINTER(UInt16), rgstTaskTimes: POINTER(POINTER(win32more.Foundation.SYSTEMTIME_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetNextRunTime(pstNextRun: POINTER(win32more.Foundation.SYSTEMTIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetIdleWait(wIdleMinutes: UInt16, wDeadlineMinutes: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetIdleWait(pwIdleMinutes: POINTER(UInt16), pwDeadlineMinutes: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Run() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Terminate() -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def EditWorkItem(hParent: win32more.Foundation.HWND, dwReserved: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetMostRecentRunTime(pstLastRun: POINTER(win32more.Foundation.SYSTEMTIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetStatus(phrStatus: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetExitCode(pdwExitCode: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetComment(pwszComment: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetComment(ppwszComment: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetCreator(pwszCreator: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetCreator(ppwszCreator: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SetWorkItemData(cbData: UInt16, rgbData: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetWorkItemData(pcbData: POINTER(UInt16), prgbData: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def SetErrorRetryCount(wRetryCount: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetErrorRetryCount(pwRetryCount: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def SetErrorRetryInterval(wRetryInterval: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def GetErrorRetryInterval(pwRetryInterval: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def SetFlags(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def GetFlags(pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def SetAccountInformation(pwszAccountName: win32more.Foundation.PWSTR, pwszPassword: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetAccountInformation(ppwszAccountName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class ISessionStateChangeTrigger(c_void_p):
    extends: win32more.System.TaskScheduler.ITrigger
    Guid = Guid('754da71b-4385-4475-9d-d9-59-82-94-fa-36-41')
    @commethod(20)
    def get_Delay(pDelay: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_Delay(delay: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_UserId(pUser: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_UserId(user: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_StateChange(pType: POINTER(win32more.System.TaskScheduler.TASK_SESSION_STATE_CHANGE_TYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_StateChange(type: win32more.System.TaskScheduler.TASK_SESSION_STATE_CHANGE_TYPE) -> win32more.Foundation.HRESULT: ...
class IShowMessageAction(c_void_p):
    extends: win32more.System.TaskScheduler.IAction
    Guid = Guid('505e9e68-af89-46b8-a3-0f-56-16-2a-83-d5-37')
    @commethod(10)
    def get_Title(pTitle: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Title(title: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_MessageBody(pMessageBody: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_MessageBody(messageBody: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class ITask(c_void_p):
    extends: win32more.System.TaskScheduler.IScheduledWorkItem
    Guid = Guid('148bd524-a2ab-11ce-b1-1f-00-aa-00-53-05-03')
    @commethod(32)
    def SetApplicationName(pwszApplicationName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def GetApplicationName(ppwszApplicationName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def SetParameters(pwszParameters: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def GetParameters(ppwszParameters: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def SetWorkingDirectory(pwszWorkingDirectory: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def GetWorkingDirectory(ppwszWorkingDirectory: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def SetPriority(dwPriority: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def GetPriority(pdwPriority: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def SetTaskFlags(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def GetTaskFlags(pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def SetMaxRunTime(dwMaxRunTimeMS: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def GetMaxRunTime(pdwMaxRunTimeMS: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITaskDefinition(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('f5bc8fc5-536d-4f77-b8-52-fb-c1-35-6f-de-b6')
    @commethod(7)
    def get_RegistrationInfo(ppRegistrationInfo: POINTER(win32more.System.TaskScheduler.IRegistrationInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_RegistrationInfo(pRegistrationInfo: win32more.System.TaskScheduler.IRegistrationInfo_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Triggers(ppTriggers: POINTER(win32more.System.TaskScheduler.ITriggerCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Triggers(pTriggers: win32more.System.TaskScheduler.ITriggerCollection_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Settings(ppSettings: POINTER(win32more.System.TaskScheduler.ITaskSettings_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_Settings(pSettings: win32more.System.TaskScheduler.ITaskSettings_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Data(pData: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Data(data: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_Principal(ppPrincipal: POINTER(win32more.System.TaskScheduler.IPrincipal_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_Principal(pPrincipal: win32more.System.TaskScheduler.IPrincipal_head) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_Actions(ppActions: POINTER(win32more.System.TaskScheduler.IActionCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_Actions(pActions: win32more.System.TaskScheduler.IActionCollection_head) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_XmlText(pXml: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_XmlText(xml: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class ITaskFolder(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('8cfac062-a080-4c15-9a-88-aa-7c-2a-f8-0d-fc')
    @commethod(7)
    def get_Name(pName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Path(pPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetFolder(path: win32more.Foundation.BSTR, ppFolder: POINTER(win32more.System.TaskScheduler.ITaskFolder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetFolders(flags: Int32, ppFolders: POINTER(win32more.System.TaskScheduler.ITaskFolderCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CreateFolder(subFolderName: win32more.Foundation.BSTR, sddl: win32more.System.Com.VARIANT, ppFolder: POINTER(win32more.System.TaskScheduler.ITaskFolder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def DeleteFolder(subFolderName: win32more.Foundation.BSTR, flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetTask(path: win32more.Foundation.BSTR, ppTask: POINTER(win32more.System.TaskScheduler.IRegisteredTask_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetTasks(flags: Int32, ppTasks: POINTER(win32more.System.TaskScheduler.IRegisteredTaskCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def DeleteTask(name: win32more.Foundation.BSTR, flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def RegisterTask(path: win32more.Foundation.BSTR, xmlText: win32more.Foundation.BSTR, flags: Int32, userId: win32more.System.Com.VARIANT, password: win32more.System.Com.VARIANT, logonType: win32more.System.TaskScheduler.TASK_LOGON_TYPE, sddl: win32more.System.Com.VARIANT, ppTask: POINTER(win32more.System.TaskScheduler.IRegisteredTask_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def RegisterTaskDefinition(path: win32more.Foundation.BSTR, pDefinition: win32more.System.TaskScheduler.ITaskDefinition_head, flags: Int32, userId: win32more.System.Com.VARIANT, password: win32more.System.Com.VARIANT, logonType: win32more.System.TaskScheduler.TASK_LOGON_TYPE, sddl: win32more.System.Com.VARIANT, ppTask: POINTER(win32more.System.TaskScheduler.IRegisteredTask_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetSecurityDescriptor(securityInformation: Int32, pSddl: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetSecurityDescriptor(sddl: win32more.Foundation.BSTR, flags: Int32) -> win32more.Foundation.HRESULT: ...
class ITaskFolderCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('79184a66-8664-423f-97-f1-63-73-56-a5-d8-12')
    @commethod(7)
    def get_Count(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: win32more.System.Com.VARIANT, ppFolder: POINTER(win32more.System.TaskScheduler.ITaskFolder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ppEnum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ITaskHandler(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('839d7762-5121-4009-92-34-4f-0d-19-39-4f-04')
    @commethod(3)
    def Start(pHandlerServices: win32more.System.Com.IUnknown_head, data: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(pRetCode: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Pause() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Resume() -> win32more.Foundation.HRESULT: ...
class ITaskHandlerStatus(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('eaec7a8f-27a0-4ddc-86-75-14-72-6a-01-a3-8a')
    @commethod(3)
    def UpdateStatus(percentComplete: Int16, statusMessage: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def TaskCompleted(taskErrCode: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
class ITaskNamedValueCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('b4ef826b-63c3-46e4-a5-04-ef-69-e4-f7-ea-4d')
    @commethod(7)
    def get_Count(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: Int32, ppPair: POINTER(win32more.System.TaskScheduler.ITaskNamedValuePair_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ppEnum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Create(name: win32more.Foundation.BSTR, value: win32more.Foundation.BSTR, ppPair: POINTER(win32more.System.TaskScheduler.ITaskNamedValuePair_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(index: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Clear() -> win32more.Foundation.HRESULT: ...
class ITaskNamedValuePair(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('39038068-2b46-4afd-86-62-7b-b6-f8-68-d2-21')
    @commethod(7)
    def get_Name(pName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(name: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Value(pValue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Value(value: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class ITaskScheduler(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('148bd527-a2ab-11ce-b1-1f-00-aa-00-53-05-03')
    @commethod(3)
    def SetTargetComputer(pwszComputer: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTargetComputer(ppwszComputer: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Enum(ppEnumWorkItems: POINTER(win32more.System.TaskScheduler.IEnumWorkItems_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Activate(pwszName: win32more.Foundation.PWSTR, riid: POINTER(Guid), ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Delete(pwszName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def NewWorkItem(pwszTaskName: win32more.Foundation.PWSTR, rclsid: POINTER(Guid), riid: POINTER(Guid), ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AddWorkItem(pwszTaskName: win32more.Foundation.PWSTR, pWorkItem: win32more.System.TaskScheduler.IScheduledWorkItem_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def IsOfType(pwszName: win32more.Foundation.PWSTR, riid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class ITaskService(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2faba4c7-4da9-4013-96-97-20-cc-3f-d4-0f-85')
    @commethod(7)
    def GetFolder(path: win32more.Foundation.BSTR, ppFolder: POINTER(win32more.System.TaskScheduler.ITaskFolder_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRunningTasks(flags: Int32, ppRunningTasks: POINTER(win32more.System.TaskScheduler.IRunningTaskCollection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def NewTask(flags: UInt32, ppDefinition: POINTER(win32more.System.TaskScheduler.ITaskDefinition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Connect(serverName: win32more.System.Com.VARIANT, user: win32more.System.Com.VARIANT, domain: win32more.System.Com.VARIANT, password: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Connected(pConnected: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_TargetServer(pServer: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_ConnectedUser(pUser: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_ConnectedDomain(pDomain: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_HighestVersion(pVersion: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITaskSettings(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('8fd4711d-2d02-4c8c-87-e3-ef-f6-99-de-12-7e')
    @commethod(7)
    def get_AllowDemandStart(pAllowDemandStart: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_AllowDemandStart(allowDemandStart: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_RestartInterval(pRestartInterval: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_RestartInterval(restartInterval: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_RestartCount(pRestartCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_RestartCount(restartCount: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_MultipleInstances(pPolicy: POINTER(win32more.System.TaskScheduler.TASK_INSTANCES_POLICY)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_MultipleInstances(policy: win32more.System.TaskScheduler.TASK_INSTANCES_POLICY) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_StopIfGoingOnBatteries(pStopIfOnBatteries: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_StopIfGoingOnBatteries(stopIfOnBatteries: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_DisallowStartIfOnBatteries(pDisallowStart: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_DisallowStartIfOnBatteries(disallowStart: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_AllowHardTerminate(pAllowHardTerminate: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_AllowHardTerminate(allowHardTerminate: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_StartWhenAvailable(pStartWhenAvailable: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_StartWhenAvailable(startWhenAvailable: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_XmlText(pText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_XmlText(text: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_RunOnlyIfNetworkAvailable(pRunOnlyIfNetworkAvailable: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def put_RunOnlyIfNetworkAvailable(runOnlyIfNetworkAvailable: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_ExecutionTimeLimit(pExecutionTimeLimit: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_ExecutionTimeLimit(executionTimeLimit: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_Enabled(pEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_Enabled(enabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_DeleteExpiredTaskAfter(pExpirationDelay: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def put_DeleteExpiredTaskAfter(expirationDelay: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_Priority(pPriority: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def put_Priority(priority: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_Compatibility(pCompatLevel: POINTER(win32more.System.TaskScheduler.TASK_COMPATIBILITY)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def put_Compatibility(compatLevel: win32more.System.TaskScheduler.TASK_COMPATIBILITY) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def get_Hidden(pHidden: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def put_Hidden(hidden: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def get_IdleSettings(ppIdleSettings: POINTER(win32more.System.TaskScheduler.IIdleSettings_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def put_IdleSettings(pIdleSettings: win32more.System.TaskScheduler.IIdleSettings_head) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def get_RunOnlyIfIdle(pRunOnlyIfIdle: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def put_RunOnlyIfIdle(runOnlyIfIdle: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def get_WakeToRun(pWake: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def put_WakeToRun(wake: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def get_NetworkSettings(ppNetworkSettings: POINTER(win32more.System.TaskScheduler.INetworkSettings_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def put_NetworkSettings(pNetworkSettings: win32more.System.TaskScheduler.INetworkSettings_head) -> win32more.Foundation.HRESULT: ...
class ITaskSettings2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('2c05c3f0-6eed-4c05-a1-5f-ed-7d-7a-98-a3-69')
    @commethod(7)
    def get_DisallowStartOnRemoteAppSession(pDisallowStart: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_DisallowStartOnRemoteAppSession(disallowStart: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_UseUnifiedSchedulingEngine(pUseUnifiedEngine: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_UseUnifiedSchedulingEngine(useUnifiedEngine: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class ITaskSettings3(c_void_p):
    extends: win32more.System.TaskScheduler.ITaskSettings
    Guid = Guid('0ad9d0d7-0c7f-4ebb-9a-5f-d1-c6-48-dc-a5-28')
    @commethod(47)
    def get_DisallowStartOnRemoteAppSession(pDisallowStart: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def put_DisallowStartOnRemoteAppSession(disallowStart: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def get_UseUnifiedSchedulingEngine(pUseUnifiedEngine: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def put_UseUnifiedSchedulingEngine(useUnifiedEngine: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def get_MaintenanceSettings(ppMaintenanceSettings: POINTER(win32more.System.TaskScheduler.IMaintenanceSettings_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def put_MaintenanceSettings(pMaintenanceSettings: win32more.System.TaskScheduler.IMaintenanceSettings_head) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def CreateMaintenanceSettings(ppMaintenanceSettings: POINTER(win32more.System.TaskScheduler.IMaintenanceSettings_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def get_Volatile(pVolatile: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def put_Volatile(Volatile: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class ITaskTrigger(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('148bd52b-a2ab-11ce-b1-1f-00-aa-00-53-05-03')
    @commethod(3)
    def SetTrigger(pTrigger: POINTER(win32more.System.TaskScheduler.TASK_TRIGGER_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTrigger(pTrigger: POINTER(win32more.System.TaskScheduler.TASK_TRIGGER_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTriggerString(ppwszTrigger: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class ITaskVariables(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3e4c9351-d966-4b8b-bb-87-ce-ba-68-bb-01-07')
    @commethod(3)
    def GetInput(pInput: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetOutput(input: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetContext(pContext: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ITimeTrigger(c_void_p):
    extends: win32more.System.TaskScheduler.ITrigger
    Guid = Guid('b45747e0-eba7-4276-9f-29-85-c5-bb-30-00-06')
    @commethod(20)
    def get_RandomDelay(pRandomDelay: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_RandomDelay(randomDelay: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class ITrigger(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('09941815-ea89-4b5b-89-e0-2a-77-38-01-fa-c3')
    @commethod(7)
    def get_Type(pType: POINTER(win32more.System.TaskScheduler.TASK_TRIGGER_TYPE2)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(pId: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def put_Id(id: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Repetition(ppRepeat: POINTER(win32more.System.TaskScheduler.IRepetitionPattern_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def put_Repetition(pRepeat: win32more.System.TaskScheduler.IRepetitionPattern_head) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_ExecutionTimeLimit(pTimeLimit: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def put_ExecutionTimeLimit(timelimit: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_StartBoundary(pStart: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_StartBoundary(start: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_EndBoundary(pEnd: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_EndBoundary(end: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_Enabled(pEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_Enabled(enabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class ITriggerCollection(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('85df5081-1b24-4f32-87-8a-d9-d1-4d-f4-cb-77')
    @commethod(7)
    def get_Count(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(index: Int32, ppTrigger: POINTER(win32more.System.TaskScheduler.ITrigger_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(ppEnum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Create(type: win32more.System.TaskScheduler.TASK_TRIGGER_TYPE2, ppTrigger: POINTER(win32more.System.TaskScheduler.ITrigger_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(index: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Clear() -> win32more.Foundation.HRESULT: ...
class IWeeklyTrigger(c_void_p):
    extends: win32more.System.TaskScheduler.ITrigger
    Guid = Guid('5038fc98-82ff-436d-87-28-a5-12-a5-7c-9d-c1')
    @commethod(20)
    def get_DaysOfWeek(pDays: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def put_DaysOfWeek(days: Int16) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_WeeksInterval(pWeeks: POINTER(Int16)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_WeeksInterval(weeks: Int16) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_RandomDelay(pRandomDelay: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def put_RandomDelay(randomDelay: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class MONTHLYDATE(Structure):
    rgfDays: UInt32
    rgfMonths: UInt16
class MONTHLYDOW(Structure):
    wWhichWeek: UInt16
    rgfDaysOfTheWeek: UInt16
    rgfMonths: UInt16
TASK_ACTION_TYPE = Int32
TASK_ACTION_EXEC: TASK_ACTION_TYPE = 0
TASK_ACTION_COM_HANDLER: TASK_ACTION_TYPE = 5
TASK_ACTION_SEND_EMAIL: TASK_ACTION_TYPE = 6
TASK_ACTION_SHOW_MESSAGE: TASK_ACTION_TYPE = 7
TASK_COMPATIBILITY = Int32
TASK_COMPATIBILITY_AT: TASK_COMPATIBILITY = 0
TASK_COMPATIBILITY_V1: TASK_COMPATIBILITY = 1
TASK_COMPATIBILITY_V2: TASK_COMPATIBILITY = 2
TASK_COMPATIBILITY_V2_1: TASK_COMPATIBILITY = 3
TASK_COMPATIBILITY_V2_2: TASK_COMPATIBILITY = 4
TASK_COMPATIBILITY_V2_3: TASK_COMPATIBILITY = 5
TASK_COMPATIBILITY_V2_4: TASK_COMPATIBILITY = 6
TASK_CREATION = Int32
TASK_VALIDATE_ONLY: TASK_CREATION = 1
TASK_CREATE: TASK_CREATION = 2
TASK_UPDATE: TASK_CREATION = 4
TASK_CREATE_OR_UPDATE: TASK_CREATION = 6
TASK_DISABLE: TASK_CREATION = 8
TASK_DONT_ADD_PRINCIPAL_ACE: TASK_CREATION = 16
TASK_IGNORE_REGISTRATION_TRIGGERS: TASK_CREATION = 32
TASK_ENUM_FLAGS = Int32
TASK_ENUM_HIDDEN: TASK_ENUM_FLAGS = 1
TASK_INSTANCES_POLICY = Int32
TASK_INSTANCES_PARALLEL: TASK_INSTANCES_POLICY = 0
TASK_INSTANCES_QUEUE: TASK_INSTANCES_POLICY = 1
TASK_INSTANCES_IGNORE_NEW: TASK_INSTANCES_POLICY = 2
TASK_INSTANCES_STOP_EXISTING: TASK_INSTANCES_POLICY = 3
TASK_LOGON_TYPE = Int32
TASK_LOGON_NONE: TASK_LOGON_TYPE = 0
TASK_LOGON_PASSWORD: TASK_LOGON_TYPE = 1
TASK_LOGON_S4U: TASK_LOGON_TYPE = 2
TASK_LOGON_INTERACTIVE_TOKEN: TASK_LOGON_TYPE = 3
TASK_LOGON_GROUP: TASK_LOGON_TYPE = 4
TASK_LOGON_SERVICE_ACCOUNT: TASK_LOGON_TYPE = 5
TASK_LOGON_INTERACTIVE_TOKEN_OR_PASSWORD: TASK_LOGON_TYPE = 6
TASK_PROCESSTOKENSID_TYPE = Int32
TASK_PROCESSTOKENSID_NONE: TASK_PROCESSTOKENSID_TYPE = 0
TASK_PROCESSTOKENSID_UNRESTRICTED: TASK_PROCESSTOKENSID_TYPE = 1
TASK_PROCESSTOKENSID_DEFAULT: TASK_PROCESSTOKENSID_TYPE = 2
TASK_RUN_FLAGS = Int32
TASK_RUN_NO_FLAGS: TASK_RUN_FLAGS = 0
TASK_RUN_AS_SELF: TASK_RUN_FLAGS = 1
TASK_RUN_IGNORE_CONSTRAINTS: TASK_RUN_FLAGS = 2
TASK_RUN_USE_SESSION_ID: TASK_RUN_FLAGS = 4
TASK_RUN_USER_SID: TASK_RUN_FLAGS = 8
TASK_RUNLEVEL_TYPE = Int32
TASK_RUNLEVEL_LUA: TASK_RUNLEVEL_TYPE = 0
TASK_RUNLEVEL_HIGHEST: TASK_RUNLEVEL_TYPE = 1
TASK_SESSION_STATE_CHANGE_TYPE = Int32
TASK_CONSOLE_CONNECT: TASK_SESSION_STATE_CHANGE_TYPE = 1
TASK_CONSOLE_DISCONNECT: TASK_SESSION_STATE_CHANGE_TYPE = 2
TASK_REMOTE_CONNECT: TASK_SESSION_STATE_CHANGE_TYPE = 3
TASK_REMOTE_DISCONNECT: TASK_SESSION_STATE_CHANGE_TYPE = 4
TASK_SESSION_LOCK: TASK_SESSION_STATE_CHANGE_TYPE = 7
TASK_SESSION_UNLOCK: TASK_SESSION_STATE_CHANGE_TYPE = 8
TASK_STATE = Int32
TASK_STATE_UNKNOWN: TASK_STATE = 0
TASK_STATE_DISABLED: TASK_STATE = 1
TASK_STATE_QUEUED: TASK_STATE = 2
TASK_STATE_READY: TASK_STATE = 3
TASK_STATE_RUNNING: TASK_STATE = 4
class TASK_TRIGGER(Structure):
    cbTriggerSize: UInt16
    Reserved1: UInt16
    wBeginYear: UInt16
    wBeginMonth: UInt16
    wBeginDay: UInt16
    wEndYear: UInt16
    wEndMonth: UInt16
    wEndDay: UInt16
    wStartHour: UInt16
    wStartMinute: UInt16
    MinutesDuration: UInt32
    MinutesInterval: UInt32
    rgFlags: UInt32
    TriggerType: win32more.System.TaskScheduler.TASK_TRIGGER_TYPE
    Type: win32more.System.TaskScheduler.TRIGGER_TYPE_UNION
    Reserved2: UInt16
    wRandomMinutesInterval: UInt16
TASK_TRIGGER_TYPE = Int32
TASK_TIME_TRIGGER_ONCE: TASK_TRIGGER_TYPE = 0
TASK_TIME_TRIGGER_DAILY: TASK_TRIGGER_TYPE = 1
TASK_TIME_TRIGGER_WEEKLY: TASK_TRIGGER_TYPE = 2
TASK_TIME_TRIGGER_MONTHLYDATE: TASK_TRIGGER_TYPE = 3
TASK_TIME_TRIGGER_MONTHLYDOW: TASK_TRIGGER_TYPE = 4
TASK_EVENT_TRIGGER_ON_IDLE: TASK_TRIGGER_TYPE = 5
TASK_EVENT_TRIGGER_AT_SYSTEMSTART: TASK_TRIGGER_TYPE = 6
TASK_EVENT_TRIGGER_AT_LOGON: TASK_TRIGGER_TYPE = 7
TASK_TRIGGER_TYPE2 = Int32
TASK_TRIGGER_EVENT: TASK_TRIGGER_TYPE2 = 0
TASK_TRIGGER_TIME: TASK_TRIGGER_TYPE2 = 1
TASK_TRIGGER_DAILY: TASK_TRIGGER_TYPE2 = 2
TASK_TRIGGER_WEEKLY: TASK_TRIGGER_TYPE2 = 3
TASK_TRIGGER_MONTHLY: TASK_TRIGGER_TYPE2 = 4
TASK_TRIGGER_MONTHLYDOW: TASK_TRIGGER_TYPE2 = 5
TASK_TRIGGER_IDLE: TASK_TRIGGER_TYPE2 = 6
TASK_TRIGGER_REGISTRATION: TASK_TRIGGER_TYPE2 = 7
TASK_TRIGGER_BOOT: TASK_TRIGGER_TYPE2 = 8
TASK_TRIGGER_LOGON: TASK_TRIGGER_TYPE2 = 9
TASK_TRIGGER_SESSION_STATE_CHANGE: TASK_TRIGGER_TYPE2 = 11
TASK_TRIGGER_CUSTOM_TRIGGER_01: TASK_TRIGGER_TYPE2 = 12
TaskHandlerPS = Guid('f2a69db7-da2c-4352-90-66-86-fe-e6-da-ca-c9')
TaskHandlerStatusPS = Guid('9f15266d-d7ba-48f0-93-c1-e6-89-5f-6f-e5-ac')
TASKPAGE = Int32
TASKPAGE_TASK: TASKPAGE = 0
TASKPAGE_SCHEDULE: TASKPAGE = 1
TASKPAGE_SETTINGS: TASKPAGE = 2
TaskScheduler = Guid('0f87369f-a4e5-4cfc-bd-3e-73-e6-15-45-72-dd')
class TRIGGER_TYPE_UNION(Union):
    Daily: win32more.System.TaskScheduler.DAILY
    Weekly: win32more.System.TaskScheduler.WEEKLY
    MonthlyDate: win32more.System.TaskScheduler.MONTHLYDATE
    MonthlyDOW: win32more.System.TaskScheduler.MONTHLYDOW
class WEEKLY(Structure):
    WeeksInterval: UInt16
    rgfDaysOfTheWeek: UInt16
make_head(_module, 'DAILY')
make_head(_module, 'IAction')
make_head(_module, 'IActionCollection')
make_head(_module, 'IBootTrigger')
make_head(_module, 'IComHandlerAction')
make_head(_module, 'IDailyTrigger')
make_head(_module, 'IEmailAction')
make_head(_module, 'IEnumWorkItems')
make_head(_module, 'IEventTrigger')
make_head(_module, 'IExecAction')
make_head(_module, 'IExecAction2')
make_head(_module, 'IIdleSettings')
make_head(_module, 'IIdleTrigger')
make_head(_module, 'ILogonTrigger')
make_head(_module, 'IMaintenanceSettings')
make_head(_module, 'IMonthlyDOWTrigger')
make_head(_module, 'IMonthlyTrigger')
make_head(_module, 'INetworkSettings')
make_head(_module, 'IPrincipal')
make_head(_module, 'IPrincipal2')
make_head(_module, 'IProvideTaskPage')
make_head(_module, 'IRegisteredTask')
make_head(_module, 'IRegisteredTaskCollection')
make_head(_module, 'IRegistrationInfo')
make_head(_module, 'IRegistrationTrigger')
make_head(_module, 'IRepetitionPattern')
make_head(_module, 'IRunningTask')
make_head(_module, 'IRunningTaskCollection')
make_head(_module, 'IScheduledWorkItem')
make_head(_module, 'ISessionStateChangeTrigger')
make_head(_module, 'IShowMessageAction')
make_head(_module, 'ITask')
make_head(_module, 'ITaskDefinition')
make_head(_module, 'ITaskFolder')
make_head(_module, 'ITaskFolderCollection')
make_head(_module, 'ITaskHandler')
make_head(_module, 'ITaskHandlerStatus')
make_head(_module, 'ITaskNamedValueCollection')
make_head(_module, 'ITaskNamedValuePair')
make_head(_module, 'ITaskScheduler')
make_head(_module, 'ITaskService')
make_head(_module, 'ITaskSettings')
make_head(_module, 'ITaskSettings2')
make_head(_module, 'ITaskSettings3')
make_head(_module, 'ITaskTrigger')
make_head(_module, 'ITaskVariables')
make_head(_module, 'ITimeTrigger')
make_head(_module, 'ITrigger')
make_head(_module, 'ITriggerCollection')
make_head(_module, 'IWeeklyTrigger')
make_head(_module, 'MONTHLYDATE')
make_head(_module, 'MONTHLYDOW')
make_head(_module, 'TASK_TRIGGER')
make_head(_module, 'TRIGGER_TYPE_UNION')
make_head(_module, 'WEEKLY')
__all__ = [
    "CLSID_CTask",
    "CLSID_CTaskScheduler",
    "DAILY",
    "IAction",
    "IActionCollection",
    "IBootTrigger",
    "IComHandlerAction",
    "IDailyTrigger",
    "IEmailAction",
    "IEnumWorkItems",
    "IEventTrigger",
    "IExecAction",
    "IExecAction2",
    "IIdleSettings",
    "IIdleTrigger",
    "ILogonTrigger",
    "IMaintenanceSettings",
    "IMonthlyDOWTrigger",
    "IMonthlyTrigger",
    "INetworkSettings",
    "IPrincipal",
    "IPrincipal2",
    "IProvideTaskPage",
    "IRegisteredTask",
    "IRegisteredTaskCollection",
    "IRegistrationInfo",
    "IRegistrationTrigger",
    "IRepetitionPattern",
    "IRunningTask",
    "IRunningTaskCollection",
    "IScheduledWorkItem",
    "ISessionStateChangeTrigger",
    "IShowMessageAction",
    "ITask",
    "ITaskDefinition",
    "ITaskFolder",
    "ITaskFolderCollection",
    "ITaskHandler",
    "ITaskHandlerStatus",
    "ITaskNamedValueCollection",
    "ITaskNamedValuePair",
    "ITaskScheduler",
    "ITaskService",
    "ITaskSettings",
    "ITaskSettings2",
    "ITaskSettings3",
    "ITaskTrigger",
    "ITaskVariables",
    "ITimeTrigger",
    "ITrigger",
    "ITriggerCollection",
    "IWeeklyTrigger",
    "MONTHLYDATE",
    "MONTHLYDOW",
    "TASKPAGE",
    "TASKPAGE_SCHEDULE",
    "TASKPAGE_SETTINGS",
    "TASKPAGE_TASK",
    "TASK_ACTION_COM_HANDLER",
    "TASK_ACTION_EXEC",
    "TASK_ACTION_SEND_EMAIL",
    "TASK_ACTION_SHOW_MESSAGE",
    "TASK_ACTION_TYPE",
    "TASK_APRIL",
    "TASK_AUGUST",
    "TASK_COMPATIBILITY",
    "TASK_COMPATIBILITY_AT",
    "TASK_COMPATIBILITY_V1",
    "TASK_COMPATIBILITY_V2",
    "TASK_COMPATIBILITY_V2_1",
    "TASK_COMPATIBILITY_V2_2",
    "TASK_COMPATIBILITY_V2_3",
    "TASK_COMPATIBILITY_V2_4",
    "TASK_CONSOLE_CONNECT",
    "TASK_CONSOLE_DISCONNECT",
    "TASK_CREATE",
    "TASK_CREATE_OR_UPDATE",
    "TASK_CREATION",
    "TASK_DECEMBER",
    "TASK_DISABLE",
    "TASK_DONT_ADD_PRINCIPAL_ACE",
    "TASK_ENUM_FLAGS",
    "TASK_ENUM_HIDDEN",
    "TASK_EVENT_TRIGGER_AT_LOGON",
    "TASK_EVENT_TRIGGER_AT_SYSTEMSTART",
    "TASK_EVENT_TRIGGER_ON_IDLE",
    "TASK_FEBRUARY",
    "TASK_FIRST_WEEK",
    "TASK_FLAG_DELETE_WHEN_DONE",
    "TASK_FLAG_DISABLED",
    "TASK_FLAG_DONT_START_IF_ON_BATTERIES",
    "TASK_FLAG_HIDDEN",
    "TASK_FLAG_INTERACTIVE",
    "TASK_FLAG_KILL_IF_GOING_ON_BATTERIES",
    "TASK_FLAG_KILL_ON_IDLE_END",
    "TASK_FLAG_RESTART_ON_IDLE_RESUME",
    "TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET",
    "TASK_FLAG_RUN_ONLY_IF_DOCKED",
    "TASK_FLAG_RUN_ONLY_IF_LOGGED_ON",
    "TASK_FLAG_START_ONLY_IF_IDLE",
    "TASK_FLAG_SYSTEM_REQUIRED",
    "TASK_FOURTH_WEEK",
    "TASK_FRIDAY",
    "TASK_IGNORE_REGISTRATION_TRIGGERS",
    "TASK_INSTANCES_IGNORE_NEW",
    "TASK_INSTANCES_PARALLEL",
    "TASK_INSTANCES_POLICY",
    "TASK_INSTANCES_QUEUE",
    "TASK_INSTANCES_STOP_EXISTING",
    "TASK_JANUARY",
    "TASK_JULY",
    "TASK_JUNE",
    "TASK_LAST_WEEK",
    "TASK_LOGON_GROUP",
    "TASK_LOGON_INTERACTIVE_TOKEN",
    "TASK_LOGON_INTERACTIVE_TOKEN_OR_PASSWORD",
    "TASK_LOGON_NONE",
    "TASK_LOGON_PASSWORD",
    "TASK_LOGON_S4U",
    "TASK_LOGON_SERVICE_ACCOUNT",
    "TASK_LOGON_TYPE",
    "TASK_MARCH",
    "TASK_MAX_RUN_TIMES",
    "TASK_MAY",
    "TASK_MONDAY",
    "TASK_NOVEMBER",
    "TASK_OCTOBER",
    "TASK_PROCESSTOKENSID_DEFAULT",
    "TASK_PROCESSTOKENSID_NONE",
    "TASK_PROCESSTOKENSID_TYPE",
    "TASK_PROCESSTOKENSID_UNRESTRICTED",
    "TASK_REMOTE_CONNECT",
    "TASK_REMOTE_DISCONNECT",
    "TASK_RUNLEVEL_HIGHEST",
    "TASK_RUNLEVEL_LUA",
    "TASK_RUNLEVEL_TYPE",
    "TASK_RUN_AS_SELF",
    "TASK_RUN_FLAGS",
    "TASK_RUN_IGNORE_CONSTRAINTS",
    "TASK_RUN_NO_FLAGS",
    "TASK_RUN_USER_SID",
    "TASK_RUN_USE_SESSION_ID",
    "TASK_SATURDAY",
    "TASK_SECOND_WEEK",
    "TASK_SEPTEMBER",
    "TASK_SESSION_LOCK",
    "TASK_SESSION_STATE_CHANGE_TYPE",
    "TASK_SESSION_UNLOCK",
    "TASK_STATE",
    "TASK_STATE_DISABLED",
    "TASK_STATE_QUEUED",
    "TASK_STATE_READY",
    "TASK_STATE_RUNNING",
    "TASK_STATE_UNKNOWN",
    "TASK_SUNDAY",
    "TASK_THIRD_WEEK",
    "TASK_THURSDAY",
    "TASK_TIME_TRIGGER_DAILY",
    "TASK_TIME_TRIGGER_MONTHLYDATE",
    "TASK_TIME_TRIGGER_MONTHLYDOW",
    "TASK_TIME_TRIGGER_ONCE",
    "TASK_TIME_TRIGGER_WEEKLY",
    "TASK_TRIGGER",
    "TASK_TRIGGER_BOOT",
    "TASK_TRIGGER_CUSTOM_TRIGGER_01",
    "TASK_TRIGGER_DAILY",
    "TASK_TRIGGER_EVENT",
    "TASK_TRIGGER_FLAG_DISABLED",
    "TASK_TRIGGER_FLAG_HAS_END_DATE",
    "TASK_TRIGGER_FLAG_KILL_AT_DURATION_END",
    "TASK_TRIGGER_IDLE",
    "TASK_TRIGGER_LOGON",
    "TASK_TRIGGER_MONTHLY",
    "TASK_TRIGGER_MONTHLYDOW",
    "TASK_TRIGGER_REGISTRATION",
    "TASK_TRIGGER_SESSION_STATE_CHANGE",
    "TASK_TRIGGER_TIME",
    "TASK_TRIGGER_TYPE",
    "TASK_TRIGGER_TYPE2",
    "TASK_TRIGGER_WEEKLY",
    "TASK_TUESDAY",
    "TASK_UPDATE",
    "TASK_VALIDATE_ONLY",
    "TASK_WEDNESDAY",
    "TRIGGER_TYPE_UNION",
    "TaskHandlerPS",
    "TaskHandlerStatusPS",
    "TaskScheduler",
    "WEEKLY",
]
_arch_optional = [
]
