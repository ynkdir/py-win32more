from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.TaskScheduler
import win32more.UI.Controls
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
TASK_SUNDAY = 1
TASK_MONDAY = 2
TASK_TUESDAY = 4
TASK_WEDNESDAY = 8
TASK_THURSDAY = 16
TASK_FRIDAY = 32
TASK_SATURDAY = 64
TASK_FIRST_WEEK = 1
TASK_SECOND_WEEK = 2
TASK_THIRD_WEEK = 3
TASK_FOURTH_WEEK = 4
TASK_LAST_WEEK = 5
TASK_JANUARY = 1
TASK_FEBRUARY = 2
TASK_MARCH = 4
TASK_APRIL = 8
TASK_MAY = 16
TASK_JUNE = 32
TASK_JULY = 64
TASK_AUGUST = 128
TASK_SEPTEMBER = 256
TASK_OCTOBER = 512
TASK_NOVEMBER = 1024
TASK_DECEMBER = 2048
TASK_FLAG_INTERACTIVE = 1
TASK_FLAG_DELETE_WHEN_DONE = 2
TASK_FLAG_DISABLED = 4
TASK_FLAG_START_ONLY_IF_IDLE = 16
TASK_FLAG_KILL_ON_IDLE_END = 32
TASK_FLAG_DONT_START_IF_ON_BATTERIES = 64
TASK_FLAG_KILL_IF_GOING_ON_BATTERIES = 128
TASK_FLAG_RUN_ONLY_IF_DOCKED = 256
TASK_FLAG_HIDDEN = 512
TASK_FLAG_RUN_IF_CONNECTED_TO_INTERNET = 1024
TASK_FLAG_RESTART_ON_IDLE_RESUME = 2048
TASK_FLAG_SYSTEM_REQUIRED = 4096
TASK_FLAG_RUN_ONLY_IF_LOGGED_ON = 8192
TASK_TRIGGER_FLAG_HAS_END_DATE = 1
TASK_TRIGGER_FLAG_KILL_AT_DURATION_END = 2
TASK_TRIGGER_FLAG_DISABLED = 4
TASK_MAX_RUN_TIMES = 1440
def _define_CLSID_CTask():
    return Guid('148bd520-a2ab-11ce-b1-1f-00-aa-00-53-05-03')
def _define_CLSID_CTaskScheduler():
    return Guid('148bd52a-a2ab-11ce-b1-1f-00-aa-00-53-05-03')
def _define_DAILY_head():
    class DAILY(Structure):
        pass
    return DAILY
def _define_DAILY():
    DAILY = win32more.System.TaskScheduler.DAILY_head
    DAILY._fields_ = [
        ('DaysInterval', UInt16),
    ]
    return DAILY
def _define_IAction_head():
    class IAction(win32more.System.Com.IDispatch_head):
        Guid = Guid('bae54997-48b1-4cbe-99-65-d6-be-26-3e-be-a4')
    return IAction
def _define_IAction():
    IAction = win32more.System.TaskScheduler.IAction_head
    IAction.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Id', ((1, 'pId'),)))
    IAction.put_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_Id', ((1, 'Id'),)))
    IAction.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.TASK_ACTION_TYPE))(9, 'get_Type', ((1, 'pType'),)))
    win32more.System.Com.IDispatch
    return IAction
def _define_IActionCollection_head():
    class IActionCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('02820e19-7b98-4ed2-b2-e8-fd-cc-ce-ff-61-9b')
    return IActionCollection
def _define_IActionCollection():
    IActionCollection = win32more.System.TaskScheduler.IActionCollection_head
    IActionCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pCount'),)))
    IActionCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.TaskScheduler.IAction_head))(8, 'get_Item', ((1, 'index'),(1, 'ppAction'),)))
    IActionCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(9, 'get__NewEnum', ((1, 'ppEnum'),)))
    IActionCollection.get_XmlText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_XmlText', ((1, 'pText'),)))
    IActionCollection.put_XmlText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(11, 'put_XmlText', ((1, 'text'),)))
    IActionCollection.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.TASK_ACTION_TYPE,POINTER(win32more.System.TaskScheduler.IAction_head))(12, 'Create', ((1, 'type'),(1, 'ppAction'),)))
    IActionCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(13, 'Remove', ((1, 'index'),)))
    IActionCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'Clear', ()))
    IActionCollection.get_Context = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_Context', ((1, 'pContext'),)))
    IActionCollection.put_Context = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(16, 'put_Context', ((1, 'context'),)))
    win32more.System.Com.IDispatch
    return IActionCollection
def _define_IBootTrigger_head():
    class IBootTrigger(win32more.System.TaskScheduler.ITrigger_head):
        Guid = Guid('2a9c35da-d357-41f4-bb-c1-20-7a-c1-b1-f3-cb')
    return IBootTrigger
def _define_IBootTrigger():
    IBootTrigger = win32more.System.TaskScheduler.IBootTrigger_head
    IBootTrigger.get_Delay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_Delay', ((1, 'pDelay'),)))
    IBootTrigger.put_Delay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(21, 'put_Delay', ((1, 'delay'),)))
    win32more.System.TaskScheduler.ITrigger
    return IBootTrigger
def _define_IComHandlerAction_head():
    class IComHandlerAction(win32more.System.TaskScheduler.IAction_head):
        Guid = Guid('6d2fd252-75c5-4f66-90-ba-2a-7d-8c-c3-03-9f')
    return IComHandlerAction
def _define_IComHandlerAction():
    IComHandlerAction = win32more.System.TaskScheduler.IComHandlerAction_head
    IComHandlerAction.get_ClassId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_ClassId', ((1, 'pClsid'),)))
    IComHandlerAction.put_ClassId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(11, 'put_ClassId', ((1, 'clsid'),)))
    IComHandlerAction.get_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_Data', ((1, 'pData'),)))
    IComHandlerAction.put_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'put_Data', ((1, 'data'),)))
    win32more.System.TaskScheduler.IAction
    return IComHandlerAction
def _define_IDailyTrigger_head():
    class IDailyTrigger(win32more.System.TaskScheduler.ITrigger_head):
        Guid = Guid('126c5cd8-b288-41d5-8d-bf-e4-91-44-6a-dc-5c')
    return IDailyTrigger
def _define_IDailyTrigger():
    IDailyTrigger = win32more.System.TaskScheduler.IDailyTrigger_head
    IDailyTrigger.get_DaysInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16))(20, 'get_DaysInterval', ((1, 'pDays'),)))
    IDailyTrigger.put_DaysInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16)(21, 'put_DaysInterval', ((1, 'days'),)))
    IDailyTrigger.get_RandomDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_RandomDelay', ((1, 'pRandomDelay'),)))
    IDailyTrigger.put_RandomDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(23, 'put_RandomDelay', ((1, 'randomDelay'),)))
    win32more.System.TaskScheduler.ITrigger
    return IDailyTrigger
def _define_IEmailAction_head():
    class IEmailAction(win32more.System.TaskScheduler.IAction_head):
        Guid = Guid('10f62c64-7e16-4314-a0-c2-0c-36-83-f9-9d-40')
    return IEmailAction
def _define_IEmailAction():
    IEmailAction = win32more.System.TaskScheduler.IEmailAction_head
    IEmailAction.get_Server = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_Server', ((1, 'pServer'),)))
    IEmailAction.put_Server = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(11, 'put_Server', ((1, 'server'),)))
    IEmailAction.get_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_Subject', ((1, 'pSubject'),)))
    IEmailAction.put_Subject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'put_Subject', ((1, 'subject'),)))
    IEmailAction.get_To = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_To', ((1, 'pTo'),)))
    IEmailAction.put_To = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(15, 'put_To', ((1, 'to'),)))
    IEmailAction.get_Cc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(16, 'get_Cc', ((1, 'pCc'),)))
    IEmailAction.put_Cc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(17, 'put_Cc', ((1, 'cc'),)))
    IEmailAction.get_Bcc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'get_Bcc', ((1, 'pBcc'),)))
    IEmailAction.put_Bcc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(19, 'put_Bcc', ((1, 'bcc'),)))
    IEmailAction.get_ReplyTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_ReplyTo', ((1, 'pReplyTo'),)))
    IEmailAction.put_ReplyTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(21, 'put_ReplyTo', ((1, 'replyTo'),)))
    IEmailAction.get_From = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_From', ((1, 'pFrom'),)))
    IEmailAction.put_From = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(23, 'put_From', ((1, 'from'),)))
    IEmailAction.get_HeaderFields = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.ITaskNamedValueCollection_head))(24, 'get_HeaderFields', ((1, 'ppHeaderFields'),)))
    IEmailAction.put_HeaderFields = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.ITaskNamedValueCollection_head)(25, 'put_HeaderFields', ((1, 'pHeaderFields'),)))
    IEmailAction.get_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(26, 'get_Body', ((1, 'pBody'),)))
    IEmailAction.put_Body = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(27, 'put_Body', ((1, 'body'),)))
    IEmailAction.get_Attachments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(28, 'get_Attachments', ((1, 'pAttachements'),)))
    IEmailAction.put_Attachments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(29, 'put_Attachments', ((1, 'pAttachements'),)))
    win32more.System.TaskScheduler.IAction
    return IEmailAction
def _define_IEnumWorkItems_head():
    class IEnumWorkItems(win32more.System.Com.IUnknown_head):
        Guid = Guid('148bd528-a2ab-11ce-b1-1f-00-aa-00-53-05-03')
    return IEnumWorkItems
def _define_IEnumWorkItems():
    IEnumWorkItems = win32more.System.TaskScheduler.IEnumWorkItems_head
    IEnumWorkItems.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgpwszNames'),(1, 'pceltFetched'),)))
    IEnumWorkItems.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumWorkItems.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumWorkItems.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.IEnumWorkItems_head))(6, 'Clone', ((1, 'ppEnumWorkItems'),)))
    win32more.System.Com.IUnknown
    return IEnumWorkItems
def _define_IEventTrigger_head():
    class IEventTrigger(win32more.System.TaskScheduler.ITrigger_head):
        Guid = Guid('d45b0167-9653-4eef-b9-4f-07-32-ca-7a-f2-51')
    return IEventTrigger
def _define_IEventTrigger():
    IEventTrigger = win32more.System.TaskScheduler.IEventTrigger_head
    IEventTrigger.get_Subscription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_Subscription', ((1, 'pQuery'),)))
    IEventTrigger.put_Subscription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(21, 'put_Subscription', ((1, 'query'),)))
    IEventTrigger.get_Delay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_Delay', ((1, 'pDelay'),)))
    IEventTrigger.put_Delay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(23, 'put_Delay', ((1, 'delay'),)))
    IEventTrigger.get_ValueQueries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.ITaskNamedValueCollection_head))(24, 'get_ValueQueries', ((1, 'ppNamedXPaths'),)))
    IEventTrigger.put_ValueQueries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.ITaskNamedValueCollection_head)(25, 'put_ValueQueries', ((1, 'pNamedXPaths'),)))
    win32more.System.TaskScheduler.ITrigger
    return IEventTrigger
def _define_IExecAction_head():
    class IExecAction(win32more.System.TaskScheduler.IAction_head):
        Guid = Guid('4c3d624d-fd6b-49a3-b9-b7-09-cb-3c-d3-f0-47')
    return IExecAction
def _define_IExecAction():
    IExecAction = win32more.System.TaskScheduler.IExecAction_head
    IExecAction.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_Path', ((1, 'pPath'),)))
    IExecAction.put_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(11, 'put_Path', ((1, 'path'),)))
    IExecAction.get_Arguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_Arguments', ((1, 'pArgument'),)))
    IExecAction.put_Arguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'put_Arguments', ((1, 'argument'),)))
    IExecAction.get_WorkingDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_WorkingDirectory', ((1, 'pWorkingDirectory'),)))
    IExecAction.put_WorkingDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(15, 'put_WorkingDirectory', ((1, 'workingDirectory'),)))
    win32more.System.TaskScheduler.IAction
    return IExecAction
def _define_IExecAction2_head():
    class IExecAction2(win32more.System.TaskScheduler.IExecAction_head):
        Guid = Guid('f2a82542-bda5-4e6b-91-43-e2-bf-4f-89-87-b6')
    return IExecAction2
def _define_IExecAction2():
    IExecAction2 = win32more.System.TaskScheduler.IExecAction2_head
    IExecAction2.get_HideAppWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(16, 'get_HideAppWindow', ((1, 'pHideAppWindow'),)))
    IExecAction2.put_HideAppWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(17, 'put_HideAppWindow', ((1, 'hideAppWindow'),)))
    win32more.System.TaskScheduler.IExecAction
    return IExecAction2
def _define_IIdleSettings_head():
    class IIdleSettings(win32more.System.Com.IDispatch_head):
        Guid = Guid('84594461-0053-4342-a8-fd-08-8f-ab-f1-1f-32')
    return IIdleSettings
def _define_IIdleSettings():
    IIdleSettings = win32more.System.TaskScheduler.IIdleSettings_head
    IIdleSettings.get_IdleDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_IdleDuration', ((1, 'pDelay'),)))
    IIdleSettings.put_IdleDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_IdleDuration', ((1, 'delay'),)))
    IIdleSettings.get_WaitTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_WaitTimeout', ((1, 'pTimeout'),)))
    IIdleSettings.put_WaitTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_WaitTimeout', ((1, 'timeout'),)))
    IIdleSettings.get_StopOnIdleEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'get_StopOnIdleEnd', ((1, 'pStop'),)))
    IIdleSettings.put_StopOnIdleEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(12, 'put_StopOnIdleEnd', ((1, 'stop'),)))
    IIdleSettings.get_RestartOnIdle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(13, 'get_RestartOnIdle', ((1, 'pRestart'),)))
    IIdleSettings.put_RestartOnIdle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(14, 'put_RestartOnIdle', ((1, 'restart'),)))
    win32more.System.Com.IDispatch
    return IIdleSettings
def _define_IIdleTrigger_head():
    class IIdleTrigger(win32more.System.TaskScheduler.ITrigger_head):
        Guid = Guid('d537d2b0-9fb3-4d34-97-39-1f-f5-ce-7b-1e-f3')
    return IIdleTrigger
def _define_IIdleTrigger():
    IIdleTrigger = win32more.System.TaskScheduler.IIdleTrigger_head
    win32more.System.TaskScheduler.ITrigger
    return IIdleTrigger
def _define_ILogonTrigger_head():
    class ILogonTrigger(win32more.System.TaskScheduler.ITrigger_head):
        Guid = Guid('72dade38-fae4-4b3e-ba-f4-5d-00-9a-f0-2b-1c')
    return ILogonTrigger
def _define_ILogonTrigger():
    ILogonTrigger = win32more.System.TaskScheduler.ILogonTrigger_head
    ILogonTrigger.get_Delay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_Delay', ((1, 'pDelay'),)))
    ILogonTrigger.put_Delay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(21, 'put_Delay', ((1, 'delay'),)))
    ILogonTrigger.get_UserId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_UserId', ((1, 'pUser'),)))
    ILogonTrigger.put_UserId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(23, 'put_UserId', ((1, 'user'),)))
    win32more.System.TaskScheduler.ITrigger
    return ILogonTrigger
def _define_IMaintenanceSettings_head():
    class IMaintenanceSettings(win32more.System.Com.IDispatch_head):
        Guid = Guid('a6024fa8-9652-4adb-a6-bf-5c-fc-d8-77-a7-ba')
    return IMaintenanceSettings
def _define_IMaintenanceSettings():
    IMaintenanceSettings = win32more.System.TaskScheduler.IMaintenanceSettings_head
    IMaintenanceSettings.put_Period = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(7, 'put_Period', ((1, 'value'),)))
    IMaintenanceSettings.get_Period = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Period', ((1, 'target'),)))
    IMaintenanceSettings.put_Deadline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(9, 'put_Deadline', ((1, 'value'),)))
    IMaintenanceSettings.get_Deadline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_Deadline', ((1, 'target'),)))
    IMaintenanceSettings.put_Exclusive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(11, 'put_Exclusive', ((1, 'value'),)))
    IMaintenanceSettings.get_Exclusive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(12, 'get_Exclusive', ((1, 'target'),)))
    win32more.System.Com.IDispatch
    return IMaintenanceSettings
def _define_IMonthlyDOWTrigger_head():
    class IMonthlyDOWTrigger(win32more.System.TaskScheduler.ITrigger_head):
        Guid = Guid('77d025a3-90fa-43aa-b5-2e-cd-a5-49-9b-94-6a')
    return IMonthlyDOWTrigger
def _define_IMonthlyDOWTrigger():
    IMonthlyDOWTrigger = win32more.System.TaskScheduler.IMonthlyDOWTrigger_head
    IMonthlyDOWTrigger.get_DaysOfWeek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16))(20, 'get_DaysOfWeek', ((1, 'pDays'),)))
    IMonthlyDOWTrigger.put_DaysOfWeek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16)(21, 'put_DaysOfWeek', ((1, 'days'),)))
    IMonthlyDOWTrigger.get_WeeksOfMonth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16))(22, 'get_WeeksOfMonth', ((1, 'pWeeks'),)))
    IMonthlyDOWTrigger.put_WeeksOfMonth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16)(23, 'put_WeeksOfMonth', ((1, 'weeks'),)))
    IMonthlyDOWTrigger.get_MonthsOfYear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16))(24, 'get_MonthsOfYear', ((1, 'pMonths'),)))
    IMonthlyDOWTrigger.put_MonthsOfYear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16)(25, 'put_MonthsOfYear', ((1, 'months'),)))
    IMonthlyDOWTrigger.get_RunOnLastWeekOfMonth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(26, 'get_RunOnLastWeekOfMonth', ((1, 'pLastWeek'),)))
    IMonthlyDOWTrigger.put_RunOnLastWeekOfMonth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(27, 'put_RunOnLastWeekOfMonth', ((1, 'lastWeek'),)))
    IMonthlyDOWTrigger.get_RandomDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(28, 'get_RandomDelay', ((1, 'pRandomDelay'),)))
    IMonthlyDOWTrigger.put_RandomDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(29, 'put_RandomDelay', ((1, 'randomDelay'),)))
    win32more.System.TaskScheduler.ITrigger
    return IMonthlyDOWTrigger
def _define_IMonthlyTrigger_head():
    class IMonthlyTrigger(win32more.System.TaskScheduler.ITrigger_head):
        Guid = Guid('97c45ef1-6b02-4a1a-9c-0e-1e-bf-ba-15-00-ac')
    return IMonthlyTrigger
def _define_IMonthlyTrigger():
    IMonthlyTrigger = win32more.System.TaskScheduler.IMonthlyTrigger_head
    IMonthlyTrigger.get_DaysOfMonth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(20, 'get_DaysOfMonth', ((1, 'pDays'),)))
    IMonthlyTrigger.put_DaysOfMonth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(21, 'put_DaysOfMonth', ((1, 'days'),)))
    IMonthlyTrigger.get_MonthsOfYear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16))(22, 'get_MonthsOfYear', ((1, 'pMonths'),)))
    IMonthlyTrigger.put_MonthsOfYear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16)(23, 'put_MonthsOfYear', ((1, 'months'),)))
    IMonthlyTrigger.get_RunOnLastDayOfMonth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(24, 'get_RunOnLastDayOfMonth', ((1, 'pLastDay'),)))
    IMonthlyTrigger.put_RunOnLastDayOfMonth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(25, 'put_RunOnLastDayOfMonth', ((1, 'lastDay'),)))
    IMonthlyTrigger.get_RandomDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(26, 'get_RandomDelay', ((1, 'pRandomDelay'),)))
    IMonthlyTrigger.put_RandomDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(27, 'put_RandomDelay', ((1, 'randomDelay'),)))
    win32more.System.TaskScheduler.ITrigger
    return IMonthlyTrigger
def _define_INetworkSettings_head():
    class INetworkSettings(win32more.System.Com.IDispatch_head):
        Guid = Guid('9f7dea84-c30b-4245-80-b6-00-e9-f6-46-f1-b4')
    return INetworkSettings
def _define_INetworkSettings():
    INetworkSettings = win32more.System.TaskScheduler.INetworkSettings_head
    INetworkSettings.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'pName'),)))
    INetworkSettings.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_Name', ((1, 'name'),)))
    INetworkSettings.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Id', ((1, 'pId'),)))
    INetworkSettings.put_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_Id', ((1, 'id'),)))
    win32more.System.Com.IDispatch
    return INetworkSettings
def _define_IPrincipal_head():
    class IPrincipal(win32more.System.Com.IDispatch_head):
        Guid = Guid('d98d51e5-c9b4-496a-a9-c1-18-98-02-61-cf-0f')
    return IPrincipal
def _define_IPrincipal():
    IPrincipal = win32more.System.TaskScheduler.IPrincipal_head
    IPrincipal.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Id', ((1, 'pId'),)))
    IPrincipal.put_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_Id', ((1, 'Id'),)))
    IPrincipal.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_DisplayName', ((1, 'pName'),)))
    IPrincipal.put_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_DisplayName', ((1, 'name'),)))
    IPrincipal.get_UserId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_UserId', ((1, 'pUser'),)))
    IPrincipal.put_UserId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'put_UserId', ((1, 'user'),)))
    IPrincipal.get_LogonType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.TASK_LOGON_TYPE))(13, 'get_LogonType', ((1, 'pLogon'),)))
    IPrincipal.put_LogonType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.TASK_LOGON_TYPE)(14, 'put_LogonType', ((1, 'logon'),)))
    IPrincipal.get_GroupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_GroupId', ((1, 'pGroup'),)))
    IPrincipal.put_GroupId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(16, 'put_GroupId', ((1, 'group'),)))
    IPrincipal.get_RunLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.TASK_RUNLEVEL_TYPE))(17, 'get_RunLevel', ((1, 'pRunLevel'),)))
    IPrincipal.put_RunLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.TASK_RUNLEVEL_TYPE)(18, 'put_RunLevel', ((1, 'runLevel'),)))
    win32more.System.Com.IDispatch
    return IPrincipal
def _define_IPrincipal2_head():
    class IPrincipal2(win32more.System.Com.IDispatch_head):
        Guid = Guid('248919ae-e345-4a6d-8a-eb-e0-d3-16-5c-90-4e')
    return IPrincipal2
def _define_IPrincipal2():
    IPrincipal2 = win32more.System.TaskScheduler.IPrincipal2_head
    IPrincipal2.get_ProcessTokenSidType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.TASK_PROCESSTOKENSID_TYPE))(7, 'get_ProcessTokenSidType', ((1, 'pProcessTokenSidType'),)))
    IPrincipal2.put_ProcessTokenSidType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.TASK_PROCESSTOKENSID_TYPE)(8, 'put_ProcessTokenSidType', ((1, 'processTokenSidType'),)))
    IPrincipal2.get_RequiredPrivilegeCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_RequiredPrivilegeCount', ((1, 'pCount'),)))
    IPrincipal2.get_RequiredPrivilege = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR))(10, 'get_RequiredPrivilege', ((1, 'index'),(1, 'pPrivilege'),)))
    IPrincipal2.AddRequiredPrivilege = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(11, 'AddRequiredPrivilege', ((1, 'privilege'),)))
    win32more.System.Com.IDispatch
    return IPrincipal2
def _define_IProvideTaskPage_head():
    class IProvideTaskPage(win32more.System.Com.IUnknown_head):
        Guid = Guid('4086658a-cbbb-11cf-b6-04-00-c0-4f-d8-d5-65')
    return IProvideTaskPage
def _define_IProvideTaskPage():
    IProvideTaskPage = win32more.System.TaskScheduler.IProvideTaskPage_head
    IProvideTaskPage.GetPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.TASKPAGE,win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.HPROPSHEETPAGE))(3, 'GetPage', ((1, 'tpType'),(1, 'fPersistChanges'),(1, 'phPage'),)))
    win32more.System.Com.IUnknown
    return IProvideTaskPage
def _define_IRegisteredTask_head():
    class IRegisteredTask(win32more.System.Com.IDispatch_head):
        Guid = Guid('9c86f320-dee3-4dd1-b9-72-a3-03-f2-6b-06-1e')
    return IRegisteredTask
def _define_IRegisteredTask():
    IRegisteredTask = win32more.System.TaskScheduler.IRegisteredTask_head
    IRegisteredTask.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'pName'),)))
    IRegisteredTask.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Path', ((1, 'pPath'),)))
    IRegisteredTask.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.TASK_STATE))(9, 'get_State', ((1, 'pState'),)))
    IRegisteredTask.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(10, 'get_Enabled', ((1, 'pEnabled'),)))
    IRegisteredTask.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(11, 'put_Enabled', ((1, 'enabled'),)))
    IRegisteredTask.Run = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.TaskScheduler.IRunningTask_head))(12, 'Run', ((1, 'params'),(1, 'ppRunningTask'),)))
    IRegisteredTask.RunEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,Int32,Int32,win32more.Foundation.BSTR,POINTER(win32more.System.TaskScheduler.IRunningTask_head))(13, 'RunEx', ((1, 'params'),(1, 'flags'),(1, 'sessionID'),(1, 'user'),(1, 'ppRunningTask'),)))
    IRegisteredTask.GetInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.TaskScheduler.IRunningTaskCollection_head))(14, 'GetInstances', ((1, 'flags'),(1, 'ppRunningTasks'),)))
    IRegisteredTask.get_LastRunTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(15, 'get_LastRunTime', ((1, 'pLastRunTime'),)))
    IRegisteredTask.get_LastTaskResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_LastTaskResult', ((1, 'pLastTaskResult'),)))
    IRegisteredTask.get_NumberOfMissedRuns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(17, 'get_NumberOfMissedRuns', ((1, 'pNumberOfMissedRuns'),)))
    IRegisteredTask.get_NextRunTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(18, 'get_NextRunTime', ((1, 'pNextRunTime'),)))
    IRegisteredTask.get_Definition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.ITaskDefinition_head))(19, 'get_Definition', ((1, 'ppDefinition'),)))
    IRegisteredTask.get_Xml = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_Xml', ((1, 'pXml'),)))
    IRegisteredTask.GetSecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR))(21, 'GetSecurityDescriptor', ((1, 'securityInformation'),(1, 'pSddl'),)))
    IRegisteredTask.SetSecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32)(22, 'SetSecurityDescriptor', ((1, 'sddl'),(1, 'flags'),)))
    IRegisteredTask.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(23, 'Stop', ((1, 'flags'),)))
    IRegisteredTask.GetRunTimes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(UInt32),POINTER(POINTER(win32more.Foundation.SYSTEMTIME_head)))(24, 'GetRunTimes', ((1, 'pstStart'),(1, 'pstEnd'),(1, 'pCount'),(1, 'pRunTimes'),)))
    win32more.System.Com.IDispatch
    return IRegisteredTask
def _define_IRegisteredTaskCollection_head():
    class IRegisteredTaskCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('86627eb4-42a7-41e4-a4-d9-ac-33-a7-2f-2d-52')
    return IRegisteredTaskCollection
def _define_IRegisteredTaskCollection():
    IRegisteredTaskCollection = win32more.System.TaskScheduler.IRegisteredTaskCollection_head
    IRegisteredTaskCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pCount'),)))
    IRegisteredTaskCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.TaskScheduler.IRegisteredTask_head))(8, 'get_Item', ((1, 'index'),(1, 'ppRegisteredTask'),)))
    IRegisteredTaskCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(9, 'get__NewEnum', ((1, 'ppEnum'),)))
    win32more.System.Com.IDispatch
    return IRegisteredTaskCollection
def _define_IRegistrationInfo_head():
    class IRegistrationInfo(win32more.System.Com.IDispatch_head):
        Guid = Guid('416d8b73-cb41-4ea1-80-5c-9b-e9-a5-ac-4a-74')
    return IRegistrationInfo
def _define_IRegistrationInfo():
    IRegistrationInfo = win32more.System.TaskScheduler.IRegistrationInfo_head
    IRegistrationInfo.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Description', ((1, 'pDescription'),)))
    IRegistrationInfo.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_Description', ((1, 'description'),)))
    IRegistrationInfo.get_Author = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Author', ((1, 'pAuthor'),)))
    IRegistrationInfo.put_Author = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_Author', ((1, 'author'),)))
    IRegistrationInfo.get_Version = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_Version', ((1, 'pVersion'),)))
    IRegistrationInfo.put_Version = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'put_Version', ((1, 'version'),)))
    IRegistrationInfo.get_Date = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_Date', ((1, 'pDate'),)))
    IRegistrationInfo.put_Date = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(14, 'put_Date', ((1, 'date'),)))
    IRegistrationInfo.get_Documentation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_Documentation', ((1, 'pDocumentation'),)))
    IRegistrationInfo.put_Documentation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(16, 'put_Documentation', ((1, 'documentation'),)))
    IRegistrationInfo.get_XmlText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(17, 'get_XmlText', ((1, 'pText'),)))
    IRegistrationInfo.put_XmlText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(18, 'put_XmlText', ((1, 'text'),)))
    IRegistrationInfo.get_URI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(19, 'get_URI', ((1, 'pUri'),)))
    IRegistrationInfo.put_URI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(20, 'put_URI', ((1, 'uri'),)))
    IRegistrationInfo.get_SecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(21, 'get_SecurityDescriptor', ((1, 'pSddl'),)))
    IRegistrationInfo.put_SecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(22, 'put_SecurityDescriptor', ((1, 'sddl'),)))
    IRegistrationInfo.get_Source = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(23, 'get_Source', ((1, 'pSource'),)))
    IRegistrationInfo.put_Source = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(24, 'put_Source', ((1, 'source'),)))
    win32more.System.Com.IDispatch
    return IRegistrationInfo
def _define_IRegistrationTrigger_head():
    class IRegistrationTrigger(win32more.System.TaskScheduler.ITrigger_head):
        Guid = Guid('4c8fec3a-c218-4e0c-b2-3d-62-90-24-db-91-a2')
    return IRegistrationTrigger
def _define_IRegistrationTrigger():
    IRegistrationTrigger = win32more.System.TaskScheduler.IRegistrationTrigger_head
    IRegistrationTrigger.get_Delay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_Delay', ((1, 'pDelay'),)))
    IRegistrationTrigger.put_Delay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(21, 'put_Delay', ((1, 'delay'),)))
    win32more.System.TaskScheduler.ITrigger
    return IRegistrationTrigger
def _define_IRepetitionPattern_head():
    class IRepetitionPattern(win32more.System.Com.IDispatch_head):
        Guid = Guid('7fb9acf1-26be-400e-85-b5-29-4b-9c-75-df-d6')
    return IRepetitionPattern
def _define_IRepetitionPattern():
    IRepetitionPattern = win32more.System.TaskScheduler.IRepetitionPattern_head
    IRepetitionPattern.get_Interval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Interval', ((1, 'pInterval'),)))
    IRepetitionPattern.put_Interval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_Interval', ((1, 'interval'),)))
    IRepetitionPattern.get_Duration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Duration', ((1, 'pDuration'),)))
    IRepetitionPattern.put_Duration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_Duration', ((1, 'duration'),)))
    IRepetitionPattern.get_StopAtDurationEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'get_StopAtDurationEnd', ((1, 'pStop'),)))
    IRepetitionPattern.put_StopAtDurationEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(12, 'put_StopAtDurationEnd', ((1, 'stop'),)))
    win32more.System.Com.IDispatch
    return IRepetitionPattern
def _define_IRunningTask_head():
    class IRunningTask(win32more.System.Com.IDispatch_head):
        Guid = Guid('653758fb-7b9a-4f1e-a4-71-be-eb-8e-9b-83-4e')
    return IRunningTask
def _define_IRunningTask():
    IRunningTask = win32more.System.TaskScheduler.IRunningTask_head
    IRunningTask.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'pName'),)))
    IRunningTask.get_InstanceGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_InstanceGuid', ((1, 'pGuid'),)))
    IRunningTask.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Path', ((1, 'pPath'),)))
    IRunningTask.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.TASK_STATE))(10, 'get_State', ((1, 'pState'),)))
    IRunningTask.get_CurrentAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_CurrentAction', ((1, 'pName'),)))
    IRunningTask.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'Stop', ()))
    IRunningTask.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(13, 'Refresh', ()))
    IRunningTask.get_EnginePID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(14, 'get_EnginePID', ((1, 'pPID'),)))
    win32more.System.Com.IDispatch
    return IRunningTask
def _define_IRunningTaskCollection_head():
    class IRunningTaskCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('6a67614b-6828-4fec-aa-54-6d-52-e8-f1-f2-db')
    return IRunningTaskCollection
def _define_IRunningTaskCollection():
    IRunningTaskCollection = win32more.System.TaskScheduler.IRunningTaskCollection_head
    IRunningTaskCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pCount'),)))
    IRunningTaskCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.TaskScheduler.IRunningTask_head))(8, 'get_Item', ((1, 'index'),(1, 'ppRunningTask'),)))
    IRunningTaskCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(9, 'get__NewEnum', ((1, 'ppEnum'),)))
    win32more.System.Com.IDispatch
    return IRunningTaskCollection
def _define_IScheduledWorkItem_head():
    class IScheduledWorkItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('a6b952f0-a4b1-11d0-99-7d-00-aa-00-68-87-ec')
    return IScheduledWorkItem
def _define_IScheduledWorkItem():
    IScheduledWorkItem = win32more.System.TaskScheduler.IScheduledWorkItem_head
    IScheduledWorkItem.CreateTrigger = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(win32more.System.TaskScheduler.ITaskTrigger_head))(3, 'CreateTrigger', ((1, 'piNewTrigger'),(1, 'ppTrigger'),)))
    IScheduledWorkItem.DeleteTrigger = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16)(4, 'DeleteTrigger', ((1, 'iTrigger'),)))
    IScheduledWorkItem.GetTriggerCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16))(5, 'GetTriggerCount', ((1, 'pwCount'),)))
    IScheduledWorkItem.GetTrigger = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.System.TaskScheduler.ITaskTrigger_head))(6, 'GetTrigger', ((1, 'iTrigger'),(1, 'ppTrigger'),)))
    IScheduledWorkItem.GetTriggerString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.PWSTR))(7, 'GetTriggerString', ((1, 'iTrigger'),(1, 'ppwszTrigger'),)))
    IScheduledWorkItem.GetRunTimes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(UInt16),POINTER(POINTER(win32more.Foundation.SYSTEMTIME_head)))(8, 'GetRunTimes', ((1, 'pstBegin'),(1, 'pstEnd'),(1, 'pCount'),(1, 'rgstTaskTimes'),)))
    IScheduledWorkItem.GetNextRunTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head))(9, 'GetNextRunTime', ((1, 'pstNextRun'),)))
    IScheduledWorkItem.SetIdleWait = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt16)(10, 'SetIdleWait', ((1, 'wIdleMinutes'),(1, 'wDeadlineMinutes'),)))
    IScheduledWorkItem.GetIdleWait = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(UInt16))(11, 'GetIdleWait', ((1, 'pwIdleMinutes'),(1, 'pwDeadlineMinutes'),)))
    IScheduledWorkItem.Run = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'Run', ()))
    IScheduledWorkItem.Terminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(13, 'Terminate', ()))
    IScheduledWorkItem.EditWorkItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32)(14, 'EditWorkItem', ((1, 'hParent'),(1, 'dwReserved'),)))
    IScheduledWorkItem.GetMostRecentRunTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head))(15, 'GetMostRecentRunTime', ((1, 'pstLastRun'),)))
    IScheduledWorkItem.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT))(16, 'GetStatus', ((1, 'phrStatus'),)))
    IScheduledWorkItem.GetExitCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(17, 'GetExitCode', ((1, 'pdwExitCode'),)))
    IScheduledWorkItem.SetComment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(18, 'SetComment', ((1, 'pwszComment'),)))
    IScheduledWorkItem.GetComment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(19, 'GetComment', ((1, 'ppwszComment'),)))
    IScheduledWorkItem.SetCreator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(20, 'SetCreator', ((1, 'pwszCreator'),)))
    IScheduledWorkItem.GetCreator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(21, 'GetCreator', ((1, 'ppwszCreator'),)))
    IScheduledWorkItem.SetWorkItemData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,c_char_p_no)(22, 'SetWorkItemData', ((1, 'cbData'),(1, 'rgbData'),)))
    IScheduledWorkItem.GetWorkItemData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(c_char_p_no))(23, 'GetWorkItemData', ((1, 'pcbData'),(1, 'prgbData'),)))
    IScheduledWorkItem.SetErrorRetryCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16)(24, 'SetErrorRetryCount', ((1, 'wRetryCount'),)))
    IScheduledWorkItem.GetErrorRetryCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16))(25, 'GetErrorRetryCount', ((1, 'pwRetryCount'),)))
    IScheduledWorkItem.SetErrorRetryInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16)(26, 'SetErrorRetryInterval', ((1, 'wRetryInterval'),)))
    IScheduledWorkItem.GetErrorRetryInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16))(27, 'GetErrorRetryInterval', ((1, 'pwRetryInterval'),)))
    IScheduledWorkItem.SetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(28, 'SetFlags', ((1, 'dwFlags'),)))
    IScheduledWorkItem.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(29, 'GetFlags', ((1, 'pdwFlags'),)))
    IScheduledWorkItem.SetAccountInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(30, 'SetAccountInformation', ((1, 'pwszAccountName'),(1, 'pwszPassword'),)))
    IScheduledWorkItem.GetAccountInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(31, 'GetAccountInformation', ((1, 'ppwszAccountName'),)))
    win32more.System.Com.IUnknown
    return IScheduledWorkItem
def _define_ISessionStateChangeTrigger_head():
    class ISessionStateChangeTrigger(win32more.System.TaskScheduler.ITrigger_head):
        Guid = Guid('754da71b-4385-4475-9d-d9-59-82-94-fa-36-41')
    return ISessionStateChangeTrigger
def _define_ISessionStateChangeTrigger():
    ISessionStateChangeTrigger = win32more.System.TaskScheduler.ISessionStateChangeTrigger_head
    ISessionStateChangeTrigger.get_Delay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_Delay', ((1, 'pDelay'),)))
    ISessionStateChangeTrigger.put_Delay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(21, 'put_Delay', ((1, 'delay'),)))
    ISessionStateChangeTrigger.get_UserId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_UserId', ((1, 'pUser'),)))
    ISessionStateChangeTrigger.put_UserId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(23, 'put_UserId', ((1, 'user'),)))
    ISessionStateChangeTrigger.get_StateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.TASK_SESSION_STATE_CHANGE_TYPE))(24, 'get_StateChange', ((1, 'pType'),)))
    ISessionStateChangeTrigger.put_StateChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.TASK_SESSION_STATE_CHANGE_TYPE)(25, 'put_StateChange', ((1, 'type'),)))
    win32more.System.TaskScheduler.ITrigger
    return ISessionStateChangeTrigger
def _define_IShowMessageAction_head():
    class IShowMessageAction(win32more.System.TaskScheduler.IAction_head):
        Guid = Guid('505e9e68-af89-46b8-a3-0f-56-16-2a-83-d5-37')
    return IShowMessageAction
def _define_IShowMessageAction():
    IShowMessageAction = win32more.System.TaskScheduler.IShowMessageAction_head
    IShowMessageAction.get_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_Title', ((1, 'pTitle'),)))
    IShowMessageAction.put_Title = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(11, 'put_Title', ((1, 'title'),)))
    IShowMessageAction.get_MessageBody = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_MessageBody', ((1, 'pMessageBody'),)))
    IShowMessageAction.put_MessageBody = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'put_MessageBody', ((1, 'messageBody'),)))
    win32more.System.TaskScheduler.IAction
    return IShowMessageAction
def _define_ITask_head():
    class ITask(win32more.System.TaskScheduler.IScheduledWorkItem_head):
        Guid = Guid('148bd524-a2ab-11ce-b1-1f-00-aa-00-53-05-03')
    return ITask
def _define_ITask():
    ITask = win32more.System.TaskScheduler.ITask_head
    ITask.SetApplicationName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(32, 'SetApplicationName', ((1, 'pwszApplicationName'),)))
    ITask.GetApplicationName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(33, 'GetApplicationName', ((1, 'ppwszApplicationName'),)))
    ITask.SetParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(34, 'SetParameters', ((1, 'pwszParameters'),)))
    ITask.GetParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(35, 'GetParameters', ((1, 'ppwszParameters'),)))
    ITask.SetWorkingDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(36, 'SetWorkingDirectory', ((1, 'pwszWorkingDirectory'),)))
    ITask.GetWorkingDirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(37, 'GetWorkingDirectory', ((1, 'ppwszWorkingDirectory'),)))
    ITask.SetPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(38, 'SetPriority', ((1, 'dwPriority'),)))
    ITask.GetPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(39, 'GetPriority', ((1, 'pdwPriority'),)))
    ITask.SetTaskFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(40, 'SetTaskFlags', ((1, 'dwFlags'),)))
    ITask.GetTaskFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(41, 'GetTaskFlags', ((1, 'pdwFlags'),)))
    ITask.SetMaxRunTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(42, 'SetMaxRunTime', ((1, 'dwMaxRunTimeMS'),)))
    ITask.GetMaxRunTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(43, 'GetMaxRunTime', ((1, 'pdwMaxRunTimeMS'),)))
    win32more.System.TaskScheduler.IScheduledWorkItem
    return ITask
def _define_ITaskDefinition_head():
    class ITaskDefinition(win32more.System.Com.IDispatch_head):
        Guid = Guid('f5bc8fc5-536d-4f77-b8-52-fb-c1-35-6f-de-b6')
    return ITaskDefinition
def _define_ITaskDefinition():
    ITaskDefinition = win32more.System.TaskScheduler.ITaskDefinition_head
    ITaskDefinition.get_RegistrationInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.IRegistrationInfo_head))(7, 'get_RegistrationInfo', ((1, 'ppRegistrationInfo'),)))
    ITaskDefinition.put_RegistrationInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.IRegistrationInfo_head)(8, 'put_RegistrationInfo', ((1, 'pRegistrationInfo'),)))
    ITaskDefinition.get_Triggers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.ITriggerCollection_head))(9, 'get_Triggers', ((1, 'ppTriggers'),)))
    ITaskDefinition.put_Triggers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.ITriggerCollection_head)(10, 'put_Triggers', ((1, 'pTriggers'),)))
    ITaskDefinition.get_Settings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.ITaskSettings_head))(11, 'get_Settings', ((1, 'ppSettings'),)))
    ITaskDefinition.put_Settings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.ITaskSettings_head)(12, 'put_Settings', ((1, 'pSettings'),)))
    ITaskDefinition.get_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_Data', ((1, 'pData'),)))
    ITaskDefinition.put_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(14, 'put_Data', ((1, 'data'),)))
    ITaskDefinition.get_Principal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.IPrincipal_head))(15, 'get_Principal', ((1, 'ppPrincipal'),)))
    ITaskDefinition.put_Principal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.IPrincipal_head)(16, 'put_Principal', ((1, 'pPrincipal'),)))
    ITaskDefinition.get_Actions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.IActionCollection_head))(17, 'get_Actions', ((1, 'ppActions'),)))
    ITaskDefinition.put_Actions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.IActionCollection_head)(18, 'put_Actions', ((1, 'pActions'),)))
    ITaskDefinition.get_XmlText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(19, 'get_XmlText', ((1, 'pXml'),)))
    ITaskDefinition.put_XmlText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(20, 'put_XmlText', ((1, 'xml'),)))
    win32more.System.Com.IDispatch
    return ITaskDefinition
def _define_ITaskFolder_head():
    class ITaskFolder(win32more.System.Com.IDispatch_head):
        Guid = Guid('8cfac062-a080-4c15-9a-88-aa-7c-2a-f8-0d-fc')
    return ITaskFolder
def _define_ITaskFolder():
    ITaskFolder = win32more.System.TaskScheduler.ITaskFolder_head
    ITaskFolder.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'pName'),)))
    ITaskFolder.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Path', ((1, 'pPath'),)))
    ITaskFolder.GetFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.TaskScheduler.ITaskFolder_head))(9, 'GetFolder', ((1, 'path'),(1, 'ppFolder'),)))
    ITaskFolder.GetFolders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.TaskScheduler.ITaskFolderCollection_head))(10, 'GetFolders', ((1, 'flags'),(1, 'ppFolders'),)))
    ITaskFolder.CreateFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.System.TaskScheduler.ITaskFolder_head))(11, 'CreateFolder', ((1, 'subFolderName'),(1, 'sddl'),(1, 'ppFolder'),)))
    ITaskFolder.DeleteFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32)(12, 'DeleteFolder', ((1, 'subFolderName'),(1, 'flags'),)))
    ITaskFolder.GetTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.TaskScheduler.IRegisteredTask_head))(13, 'GetTask', ((1, 'path'),(1, 'ppTask'),)))
    ITaskFolder.GetTasks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.TaskScheduler.IRegisteredTaskCollection_head))(14, 'GetTasks', ((1, 'flags'),(1, 'ppTasks'),)))
    ITaskFolder.DeleteTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32)(15, 'DeleteTask', ((1, 'name'),(1, 'flags'),)))
    ITaskFolder.RegisterTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,win32more.System.TaskScheduler.TASK_LOGON_TYPE,win32more.System.Com.VARIANT,POINTER(win32more.System.TaskScheduler.IRegisteredTask_head))(16, 'RegisterTask', ((1, 'path'),(1, 'xmlText'),(1, 'flags'),(1, 'userId'),(1, 'password'),(1, 'logonType'),(1, 'sddl'),(1, 'ppTask'),)))
    ITaskFolder.RegisterTaskDefinition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.TaskScheduler.ITaskDefinition_head,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,win32more.System.TaskScheduler.TASK_LOGON_TYPE,win32more.System.Com.VARIANT,POINTER(win32more.System.TaskScheduler.IRegisteredTask_head))(17, 'RegisterTaskDefinition', ((1, 'path'),(1, 'pDefinition'),(1, 'flags'),(1, 'userId'),(1, 'password'),(1, 'logonType'),(1, 'sddl'),(1, 'ppTask'),)))
    ITaskFolder.GetSecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR))(18, 'GetSecurityDescriptor', ((1, 'securityInformation'),(1, 'pSddl'),)))
    ITaskFolder.SetSecurityDescriptor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32)(19, 'SetSecurityDescriptor', ((1, 'sddl'),(1, 'flags'),)))
    win32more.System.Com.IDispatch
    return ITaskFolder
def _define_ITaskFolderCollection_head():
    class ITaskFolderCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('79184a66-8664-423f-97-f1-63-73-56-a5-d8-12')
    return ITaskFolderCollection
def _define_ITaskFolderCollection():
    ITaskFolderCollection = win32more.System.TaskScheduler.ITaskFolderCollection_head
    ITaskFolderCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pCount'),)))
    ITaskFolderCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.TaskScheduler.ITaskFolder_head))(8, 'get_Item', ((1, 'index'),(1, 'ppFolder'),)))
    ITaskFolderCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(9, 'get__NewEnum', ((1, 'ppEnum'),)))
    win32more.System.Com.IDispatch
    return ITaskFolderCollection
def _define_ITaskHandler_head():
    class ITaskHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('839d7762-5121-4009-92-34-4f-0d-19-39-4f-04')
    return ITaskHandler
def _define_ITaskHandler():
    ITaskHandler = win32more.System.TaskScheduler.ITaskHandler_head
    ITaskHandler.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BSTR)(3, 'Start', ((1, 'pHandlerServices'),(1, 'data'),)))
    ITaskHandler.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT))(4, 'Stop', ((1, 'pRetCode'),)))
    ITaskHandler.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Pause', ()))
    ITaskHandler.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Resume', ()))
    win32more.System.Com.IUnknown
    return ITaskHandler
def _define_ITaskHandlerStatus_head():
    class ITaskHandlerStatus(win32more.System.Com.IUnknown_head):
        Guid = Guid('eaec7a8f-27a0-4ddc-86-75-14-72-6a-01-a3-8a')
    return ITaskHandlerStatus
def _define_ITaskHandlerStatus():
    ITaskHandlerStatus = win32more.System.TaskScheduler.ITaskHandlerStatus_head
    ITaskHandlerStatus.UpdateStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.Foundation.BSTR)(3, 'UpdateStatus', ((1, 'percentComplete'),(1, 'statusMessage'),)))
    ITaskHandlerStatus.TaskCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(4, 'TaskCompleted', ((1, 'taskErrCode'),)))
    win32more.System.Com.IUnknown
    return ITaskHandlerStatus
def _define_ITaskNamedValueCollection_head():
    class ITaskNamedValueCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('b4ef826b-63c3-46e4-a5-04-ef-69-e4-f7-ea-4d')
    return ITaskNamedValueCollection
def _define_ITaskNamedValueCollection():
    ITaskNamedValueCollection = win32more.System.TaskScheduler.ITaskNamedValueCollection_head
    ITaskNamedValueCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pCount'),)))
    ITaskNamedValueCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.TaskScheduler.ITaskNamedValuePair_head))(8, 'get_Item', ((1, 'index'),(1, 'ppPair'),)))
    ITaskNamedValueCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(9, 'get__NewEnum', ((1, 'ppEnum'),)))
    ITaskNamedValueCollection.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.TaskScheduler.ITaskNamedValuePair_head))(10, 'Create', ((1, 'name'),(1, 'value'),(1, 'ppPair'),)))
    ITaskNamedValueCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(11, 'Remove', ((1, 'index'),)))
    ITaskNamedValueCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'Clear', ()))
    win32more.System.Com.IDispatch
    return ITaskNamedValueCollection
def _define_ITaskNamedValuePair_head():
    class ITaskNamedValuePair(win32more.System.Com.IDispatch_head):
        Guid = Guid('39038068-2b46-4afd-86-62-7b-b6-f8-68-d2-21')
    return ITaskNamedValuePair
def _define_ITaskNamedValuePair():
    ITaskNamedValuePair = win32more.System.TaskScheduler.ITaskNamedValuePair_head
    ITaskNamedValuePair.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'pName'),)))
    ITaskNamedValuePair.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'put_Name', ((1, 'name'),)))
    ITaskNamedValuePair.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Value', ((1, 'pValue'),)))
    ITaskNamedValuePair.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_Value', ((1, 'value'),)))
    win32more.System.Com.IDispatch
    return ITaskNamedValuePair
def _define_ITaskScheduler_head():
    class ITaskScheduler(win32more.System.Com.IUnknown_head):
        Guid = Guid('148bd527-a2ab-11ce-b1-1f-00-aa-00-53-05-03')
    return ITaskScheduler
def _define_ITaskScheduler():
    ITaskScheduler = win32more.System.TaskScheduler.ITaskScheduler_head
    ITaskScheduler.SetTargetComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(3, 'SetTargetComputer', ((1, 'pwszComputer'),)))
    ITaskScheduler.GetTargetComputer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(4, 'GetTargetComputer', ((1, 'ppwszComputer'),)))
    ITaskScheduler.Enum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.IEnumWorkItems_head))(5, 'Enum', ((1, 'ppEnumWorkItems'),)))
    ITaskScheduler.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(6, 'Activate', ((1, 'pwszName'),(1, 'riid'),(1, 'ppUnk'),)))
    ITaskScheduler.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(7, 'Delete', ((1, 'pwszName'),)))
    ITaskScheduler.NewWorkItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(8, 'NewWorkItem', ((1, 'pwszTaskName'),(1, 'rclsid'),(1, 'riid'),(1, 'ppUnk'),)))
    ITaskScheduler.AddWorkItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.TaskScheduler.IScheduledWorkItem_head)(9, 'AddWorkItem', ((1, 'pwszTaskName'),(1, 'pWorkItem'),)))
    ITaskScheduler.IsOfType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid))(10, 'IsOfType', ((1, 'pwszName'),(1, 'riid'),)))
    win32more.System.Com.IUnknown
    return ITaskScheduler
def _define_ITaskService_head():
    class ITaskService(win32more.System.Com.IDispatch_head):
        Guid = Guid('2faba4c7-4da9-4013-96-97-20-cc-3f-d4-0f-85')
    return ITaskService
def _define_ITaskService():
    ITaskService = win32more.System.TaskScheduler.ITaskService_head
    ITaskService.GetFolder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.TaskScheduler.ITaskFolder_head))(7, 'GetFolder', ((1, 'path'),(1, 'ppFolder'),)))
    ITaskService.GetRunningTasks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.TaskScheduler.IRunningTaskCollection_head))(8, 'GetRunningTasks', ((1, 'flags'),(1, 'ppRunningTasks'),)))
    ITaskService.NewTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.TaskScheduler.ITaskDefinition_head))(9, 'NewTask', ((1, 'flags'),(1, 'ppDefinition'),)))
    ITaskService.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT)(10, 'Connect', ((1, 'serverName'),(1, 'user'),(1, 'domain'),(1, 'password'),)))
    ITaskService.get_Connected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'get_Connected', ((1, 'pConnected'),)))
    ITaskService.get_TargetServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_TargetServer', ((1, 'pServer'),)))
    ITaskService.get_ConnectedUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_ConnectedUser', ((1, 'pUser'),)))
    ITaskService.get_ConnectedDomain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_ConnectedDomain', ((1, 'pDomain'),)))
    ITaskService.get_HighestVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(15, 'get_HighestVersion', ((1, 'pVersion'),)))
    win32more.System.Com.IDispatch
    return ITaskService
def _define_ITaskSettings_head():
    class ITaskSettings(win32more.System.Com.IDispatch_head):
        Guid = Guid('8fd4711d-2d02-4c8c-87-e3-ef-f6-99-de-12-7e')
    return ITaskSettings
def _define_ITaskSettings():
    ITaskSettings = win32more.System.TaskScheduler.ITaskSettings_head
    ITaskSettings.get_AllowDemandStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_AllowDemandStart', ((1, 'pAllowDemandStart'),)))
    ITaskSettings.put_AllowDemandStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(8, 'put_AllowDemandStart', ((1, 'allowDemandStart'),)))
    ITaskSettings.get_RestartInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_RestartInterval', ((1, 'pRestartInterval'),)))
    ITaskSettings.put_RestartInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'put_RestartInterval', ((1, 'restartInterval'),)))
    ITaskSettings.get_RestartCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_RestartCount', ((1, 'pRestartCount'),)))
    ITaskSettings.put_RestartCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(12, 'put_RestartCount', ((1, 'restartCount'),)))
    ITaskSettings.get_MultipleInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.TASK_INSTANCES_POLICY))(13, 'get_MultipleInstances', ((1, 'pPolicy'),)))
    ITaskSettings.put_MultipleInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.TASK_INSTANCES_POLICY)(14, 'put_MultipleInstances', ((1, 'policy'),)))
    ITaskSettings.get_StopIfGoingOnBatteries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(15, 'get_StopIfGoingOnBatteries', ((1, 'pStopIfOnBatteries'),)))
    ITaskSettings.put_StopIfGoingOnBatteries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(16, 'put_StopIfGoingOnBatteries', ((1, 'stopIfOnBatteries'),)))
    ITaskSettings.get_DisallowStartIfOnBatteries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(17, 'get_DisallowStartIfOnBatteries', ((1, 'pDisallowStart'),)))
    ITaskSettings.put_DisallowStartIfOnBatteries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(18, 'put_DisallowStartIfOnBatteries', ((1, 'disallowStart'),)))
    ITaskSettings.get_AllowHardTerminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(19, 'get_AllowHardTerminate', ((1, 'pAllowHardTerminate'),)))
    ITaskSettings.put_AllowHardTerminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(20, 'put_AllowHardTerminate', ((1, 'allowHardTerminate'),)))
    ITaskSettings.get_StartWhenAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(21, 'get_StartWhenAvailable', ((1, 'pStartWhenAvailable'),)))
    ITaskSettings.put_StartWhenAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(22, 'put_StartWhenAvailable', ((1, 'startWhenAvailable'),)))
    ITaskSettings.get_XmlText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(23, 'get_XmlText', ((1, 'pText'),)))
    ITaskSettings.put_XmlText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(24, 'put_XmlText', ((1, 'text'),)))
    ITaskSettings.get_RunOnlyIfNetworkAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(25, 'get_RunOnlyIfNetworkAvailable', ((1, 'pRunOnlyIfNetworkAvailable'),)))
    ITaskSettings.put_RunOnlyIfNetworkAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(26, 'put_RunOnlyIfNetworkAvailable', ((1, 'runOnlyIfNetworkAvailable'),)))
    ITaskSettings.get_ExecutionTimeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(27, 'get_ExecutionTimeLimit', ((1, 'pExecutionTimeLimit'),)))
    ITaskSettings.put_ExecutionTimeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(28, 'put_ExecutionTimeLimit', ((1, 'executionTimeLimit'),)))
    ITaskSettings.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(29, 'get_Enabled', ((1, 'pEnabled'),)))
    ITaskSettings.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(30, 'put_Enabled', ((1, 'enabled'),)))
    ITaskSettings.get_DeleteExpiredTaskAfter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(31, 'get_DeleteExpiredTaskAfter', ((1, 'pExpirationDelay'),)))
    ITaskSettings.put_DeleteExpiredTaskAfter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(32, 'put_DeleteExpiredTaskAfter', ((1, 'expirationDelay'),)))
    ITaskSettings.get_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(33, 'get_Priority', ((1, 'pPriority'),)))
    ITaskSettings.put_Priority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(34, 'put_Priority', ((1, 'priority'),)))
    ITaskSettings.get_Compatibility = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.TASK_COMPATIBILITY))(35, 'get_Compatibility', ((1, 'pCompatLevel'),)))
    ITaskSettings.put_Compatibility = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.TASK_COMPATIBILITY)(36, 'put_Compatibility', ((1, 'compatLevel'),)))
    ITaskSettings.get_Hidden = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(37, 'get_Hidden', ((1, 'pHidden'),)))
    ITaskSettings.put_Hidden = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(38, 'put_Hidden', ((1, 'hidden'),)))
    ITaskSettings.get_IdleSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.IIdleSettings_head))(39, 'get_IdleSettings', ((1, 'ppIdleSettings'),)))
    ITaskSettings.put_IdleSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.IIdleSettings_head)(40, 'put_IdleSettings', ((1, 'pIdleSettings'),)))
    ITaskSettings.get_RunOnlyIfIdle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(41, 'get_RunOnlyIfIdle', ((1, 'pRunOnlyIfIdle'),)))
    ITaskSettings.put_RunOnlyIfIdle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(42, 'put_RunOnlyIfIdle', ((1, 'runOnlyIfIdle'),)))
    ITaskSettings.get_WakeToRun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(43, 'get_WakeToRun', ((1, 'pWake'),)))
    ITaskSettings.put_WakeToRun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(44, 'put_WakeToRun', ((1, 'wake'),)))
    ITaskSettings.get_NetworkSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.INetworkSettings_head))(45, 'get_NetworkSettings', ((1, 'ppNetworkSettings'),)))
    ITaskSettings.put_NetworkSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.INetworkSettings_head)(46, 'put_NetworkSettings', ((1, 'pNetworkSettings'),)))
    win32more.System.Com.IDispatch
    return ITaskSettings
def _define_ITaskSettings2_head():
    class ITaskSettings2(win32more.System.Com.IDispatch_head):
        Guid = Guid('2c05c3f0-6eed-4c05-a1-5f-ed-7d-7a-98-a3-69')
    return ITaskSettings2
def _define_ITaskSettings2():
    ITaskSettings2 = win32more.System.TaskScheduler.ITaskSettings2_head
    ITaskSettings2.get_DisallowStartOnRemoteAppSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_DisallowStartOnRemoteAppSession', ((1, 'pDisallowStart'),)))
    ITaskSettings2.put_DisallowStartOnRemoteAppSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(8, 'put_DisallowStartOnRemoteAppSession', ((1, 'disallowStart'),)))
    ITaskSettings2.get_UseUnifiedSchedulingEngine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_UseUnifiedSchedulingEngine', ((1, 'pUseUnifiedEngine'),)))
    ITaskSettings2.put_UseUnifiedSchedulingEngine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(10, 'put_UseUnifiedSchedulingEngine', ((1, 'useUnifiedEngine'),)))
    win32more.System.Com.IDispatch
    return ITaskSettings2
def _define_ITaskSettings3_head():
    class ITaskSettings3(win32more.System.TaskScheduler.ITaskSettings_head):
        Guid = Guid('0ad9d0d7-0c7f-4ebb-9a-5f-d1-c6-48-dc-a5-28')
    return ITaskSettings3
def _define_ITaskSettings3():
    ITaskSettings3 = win32more.System.TaskScheduler.ITaskSettings3_head
    ITaskSettings3.get_DisallowStartOnRemoteAppSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(47, 'get_DisallowStartOnRemoteAppSession', ((1, 'pDisallowStart'),)))
    ITaskSettings3.put_DisallowStartOnRemoteAppSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(48, 'put_DisallowStartOnRemoteAppSession', ((1, 'disallowStart'),)))
    ITaskSettings3.get_UseUnifiedSchedulingEngine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(49, 'get_UseUnifiedSchedulingEngine', ((1, 'pUseUnifiedEngine'),)))
    ITaskSettings3.put_UseUnifiedSchedulingEngine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(50, 'put_UseUnifiedSchedulingEngine', ((1, 'useUnifiedEngine'),)))
    ITaskSettings3.get_MaintenanceSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.IMaintenanceSettings_head))(51, 'get_MaintenanceSettings', ((1, 'ppMaintenanceSettings'),)))
    ITaskSettings3.put_MaintenanceSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.IMaintenanceSettings_head)(52, 'put_MaintenanceSettings', ((1, 'pMaintenanceSettings'),)))
    ITaskSettings3.CreateMaintenanceSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.IMaintenanceSettings_head))(53, 'CreateMaintenanceSettings', ((1, 'ppMaintenanceSettings'),)))
    ITaskSettings3.get_Volatile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(54, 'get_Volatile', ((1, 'pVolatile'),)))
    ITaskSettings3.put_Volatile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(55, 'put_Volatile', ((1, 'Volatile'),)))
    win32more.System.TaskScheduler.ITaskSettings
    return ITaskSettings3
def _define_ITaskTrigger_head():
    class ITaskTrigger(win32more.System.Com.IUnknown_head):
        Guid = Guid('148bd52b-a2ab-11ce-b1-1f-00-aa-00-53-05-03')
    return ITaskTrigger
def _define_ITaskTrigger():
    ITaskTrigger = win32more.System.TaskScheduler.ITaskTrigger_head
    ITaskTrigger.SetTrigger = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.TASK_TRIGGER_head))(3, 'SetTrigger', ((1, 'pTrigger'),)))
    ITaskTrigger.GetTrigger = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.TASK_TRIGGER_head))(4, 'GetTrigger', ((1, 'pTrigger'),)))
    ITaskTrigger.GetTriggerString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(5, 'GetTriggerString', ((1, 'ppwszTrigger'),)))
    win32more.System.Com.IUnknown
    return ITaskTrigger
def _define_ITaskVariables_head():
    class ITaskVariables(win32more.System.Com.IUnknown_head):
        Guid = Guid('3e4c9351-d966-4b8b-bb-87-ce-ba-68-bb-01-07')
    return ITaskVariables
def _define_ITaskVariables():
    ITaskVariables = win32more.System.TaskScheduler.ITaskVariables_head
    ITaskVariables.GetInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(3, 'GetInput', ((1, 'pInput'),)))
    ITaskVariables.SetOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(4, 'SetOutput', ((1, 'input'),)))
    ITaskVariables.GetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(5, 'GetContext', ((1, 'pContext'),)))
    win32more.System.Com.IUnknown
    return ITaskVariables
def _define_ITimeTrigger_head():
    class ITimeTrigger(win32more.System.TaskScheduler.ITrigger_head):
        Guid = Guid('b45747e0-eba7-4276-9f-29-85-c5-bb-30-00-06')
    return ITimeTrigger
def _define_ITimeTrigger():
    ITimeTrigger = win32more.System.TaskScheduler.ITimeTrigger_head
    ITimeTrigger.get_RandomDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_RandomDelay', ((1, 'pRandomDelay'),)))
    ITimeTrigger.put_RandomDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(21, 'put_RandomDelay', ((1, 'randomDelay'),)))
    win32more.System.TaskScheduler.ITrigger
    return ITimeTrigger
def _define_ITrigger_head():
    class ITrigger(win32more.System.Com.IDispatch_head):
        Guid = Guid('09941815-ea89-4b5b-89-e0-2a-77-38-01-fa-c3')
    return ITrigger
def _define_ITrigger():
    ITrigger = win32more.System.TaskScheduler.ITrigger_head
    ITrigger.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.TASK_TRIGGER_TYPE2))(7, 'get_Type', ((1, 'pType'),)))
    ITrigger.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Id', ((1, 'pId'),)))
    ITrigger.put_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(9, 'put_Id', ((1, 'id'),)))
    ITrigger.get_Repetition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.TaskScheduler.IRepetitionPattern_head))(10, 'get_Repetition', ((1, 'ppRepeat'),)))
    ITrigger.put_Repetition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.IRepetitionPattern_head)(11, 'put_Repetition', ((1, 'pRepeat'),)))
    ITrigger.get_ExecutionTimeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_ExecutionTimeLimit', ((1, 'pTimeLimit'),)))
    ITrigger.put_ExecutionTimeLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'put_ExecutionTimeLimit', ((1, 'timelimit'),)))
    ITrigger.get_StartBoundary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_StartBoundary', ((1, 'pStart'),)))
    ITrigger.put_StartBoundary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(15, 'put_StartBoundary', ((1, 'start'),)))
    ITrigger.get_EndBoundary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(16, 'get_EndBoundary', ((1, 'pEnd'),)))
    ITrigger.put_EndBoundary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(17, 'put_EndBoundary', ((1, 'end'),)))
    ITrigger.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(18, 'get_Enabled', ((1, 'pEnabled'),)))
    ITrigger.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(19, 'put_Enabled', ((1, 'enabled'),)))
    win32more.System.Com.IDispatch
    return ITrigger
def _define_ITriggerCollection_head():
    class ITriggerCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('85df5081-1b24-4f32-87-8a-d9-d1-4d-f4-cb-77')
    return ITriggerCollection
def _define_ITriggerCollection():
    ITriggerCollection = win32more.System.TaskScheduler.ITriggerCollection_head
    ITriggerCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'pCount'),)))
    ITriggerCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.TaskScheduler.ITrigger_head))(8, 'get_Item', ((1, 'index'),(1, 'ppTrigger'),)))
    ITriggerCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(9, 'get__NewEnum', ((1, 'ppEnum'),)))
    ITriggerCollection.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.TaskScheduler.TASK_TRIGGER_TYPE2,POINTER(win32more.System.TaskScheduler.ITrigger_head))(10, 'Create', ((1, 'type'),(1, 'ppTrigger'),)))
    ITriggerCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(11, 'Remove', ((1, 'index'),)))
    ITriggerCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'Clear', ()))
    win32more.System.Com.IDispatch
    return ITriggerCollection
def _define_IWeeklyTrigger_head():
    class IWeeklyTrigger(win32more.System.TaskScheduler.ITrigger_head):
        Guid = Guid('5038fc98-82ff-436d-87-28-a5-12-a5-7c-9d-c1')
    return IWeeklyTrigger
def _define_IWeeklyTrigger():
    IWeeklyTrigger = win32more.System.TaskScheduler.IWeeklyTrigger_head
    IWeeklyTrigger.get_DaysOfWeek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16))(20, 'get_DaysOfWeek', ((1, 'pDays'),)))
    IWeeklyTrigger.put_DaysOfWeek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16)(21, 'put_DaysOfWeek', ((1, 'days'),)))
    IWeeklyTrigger.get_WeeksInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16))(22, 'get_WeeksInterval', ((1, 'pWeeks'),)))
    IWeeklyTrigger.put_WeeksInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16)(23, 'put_WeeksInterval', ((1, 'weeks'),)))
    IWeeklyTrigger.get_RandomDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(24, 'get_RandomDelay', ((1, 'pRandomDelay'),)))
    IWeeklyTrigger.put_RandomDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(25, 'put_RandomDelay', ((1, 'randomDelay'),)))
    win32more.System.TaskScheduler.ITrigger
    return IWeeklyTrigger
def _define_MONTHLYDATE_head():
    class MONTHLYDATE(Structure):
        pass
    return MONTHLYDATE
def _define_MONTHLYDATE():
    MONTHLYDATE = win32more.System.TaskScheduler.MONTHLYDATE_head
    MONTHLYDATE._fields_ = [
        ('rgfDays', UInt32),
        ('rgfMonths', UInt16),
    ]
    return MONTHLYDATE
def _define_MONTHLYDOW_head():
    class MONTHLYDOW(Structure):
        pass
    return MONTHLYDOW
def _define_MONTHLYDOW():
    MONTHLYDOW = win32more.System.TaskScheduler.MONTHLYDOW_head
    MONTHLYDOW._fields_ = [
        ('wWhichWeek', UInt16),
        ('rgfDaysOfTheWeek', UInt16),
        ('rgfMonths', UInt16),
    ]
    return MONTHLYDOW
TASK_ACTION_TYPE = Int32
TASK_ACTION_EXEC = 0
TASK_ACTION_COM_HANDLER = 5
TASK_ACTION_SEND_EMAIL = 6
TASK_ACTION_SHOW_MESSAGE = 7
TASK_COMPATIBILITY = Int32
TASK_COMPATIBILITY_AT = 0
TASK_COMPATIBILITY_V1 = 1
TASK_COMPATIBILITY_V2 = 2
TASK_COMPATIBILITY_V2_1 = 3
TASK_COMPATIBILITY_V2_2 = 4
TASK_COMPATIBILITY_V2_3 = 5
TASK_COMPATIBILITY_V2_4 = 6
TASK_CREATION = Int32
TASK_VALIDATE_ONLY = 1
TASK_CREATE = 2
TASK_UPDATE = 4
TASK_CREATE_OR_UPDATE = 6
TASK_DISABLE = 8
TASK_DONT_ADD_PRINCIPAL_ACE = 16
TASK_IGNORE_REGISTRATION_TRIGGERS = 32
TASK_ENUM_FLAGS = Int32
TASK_ENUM_HIDDEN = 1
TASK_INSTANCES_POLICY = Int32
TASK_INSTANCES_PARALLEL = 0
TASK_INSTANCES_QUEUE = 1
TASK_INSTANCES_IGNORE_NEW = 2
TASK_INSTANCES_STOP_EXISTING = 3
TASK_LOGON_TYPE = Int32
TASK_LOGON_NONE = 0
TASK_LOGON_PASSWORD = 1
TASK_LOGON_S4U = 2
TASK_LOGON_INTERACTIVE_TOKEN = 3
TASK_LOGON_GROUP = 4
TASK_LOGON_SERVICE_ACCOUNT = 5
TASK_LOGON_INTERACTIVE_TOKEN_OR_PASSWORD = 6
TASK_PROCESSTOKENSID_TYPE = Int32
TASK_PROCESSTOKENSID_NONE = 0
TASK_PROCESSTOKENSID_UNRESTRICTED = 1
TASK_PROCESSTOKENSID_DEFAULT = 2
TASK_RUN_FLAGS = Int32
TASK_RUN_NO_FLAGS = 0
TASK_RUN_AS_SELF = 1
TASK_RUN_IGNORE_CONSTRAINTS = 2
TASK_RUN_USE_SESSION_ID = 4
TASK_RUN_USER_SID = 8
TASK_RUNLEVEL_TYPE = Int32
TASK_RUNLEVEL_LUA = 0
TASK_RUNLEVEL_HIGHEST = 1
TASK_SESSION_STATE_CHANGE_TYPE = Int32
TASK_CONSOLE_CONNECT = 1
TASK_CONSOLE_DISCONNECT = 2
TASK_REMOTE_CONNECT = 3
TASK_REMOTE_DISCONNECT = 4
TASK_SESSION_LOCK = 7
TASK_SESSION_UNLOCK = 8
TASK_STATE = Int32
TASK_STATE_UNKNOWN = 0
TASK_STATE_DISABLED = 1
TASK_STATE_QUEUED = 2
TASK_STATE_READY = 3
TASK_STATE_RUNNING = 4
def _define_TASK_TRIGGER_head():
    class TASK_TRIGGER(Structure):
        pass
    return TASK_TRIGGER
def _define_TASK_TRIGGER():
    TASK_TRIGGER = win32more.System.TaskScheduler.TASK_TRIGGER_head
    TASK_TRIGGER._fields_ = [
        ('cbTriggerSize', UInt16),
        ('Reserved1', UInt16),
        ('wBeginYear', UInt16),
        ('wBeginMonth', UInt16),
        ('wBeginDay', UInt16),
        ('wEndYear', UInt16),
        ('wEndMonth', UInt16),
        ('wEndDay', UInt16),
        ('wStartHour', UInt16),
        ('wStartMinute', UInt16),
        ('MinutesDuration', UInt32),
        ('MinutesInterval', UInt32),
        ('rgFlags', UInt32),
        ('TriggerType', win32more.System.TaskScheduler.TASK_TRIGGER_TYPE),
        ('Type', win32more.System.TaskScheduler.TRIGGER_TYPE_UNION),
        ('Reserved2', UInt16),
        ('wRandomMinutesInterval', UInt16),
    ]
    return TASK_TRIGGER
TASK_TRIGGER_TYPE = Int32
TASK_TIME_TRIGGER_ONCE = 0
TASK_TIME_TRIGGER_DAILY = 1
TASK_TIME_TRIGGER_WEEKLY = 2
TASK_TIME_TRIGGER_MONTHLYDATE = 3
TASK_TIME_TRIGGER_MONTHLYDOW = 4
TASK_EVENT_TRIGGER_ON_IDLE = 5
TASK_EVENT_TRIGGER_AT_SYSTEMSTART = 6
TASK_EVENT_TRIGGER_AT_LOGON = 7
TASK_TRIGGER_TYPE2 = Int32
TASK_TRIGGER_EVENT = 0
TASK_TRIGGER_TIME = 1
TASK_TRIGGER_DAILY = 2
TASK_TRIGGER_WEEKLY = 3
TASK_TRIGGER_MONTHLY = 4
TASK_TRIGGER_MONTHLYDOW = 5
TASK_TRIGGER_IDLE = 6
TASK_TRIGGER_REGISTRATION = 7
TASK_TRIGGER_BOOT = 8
TASK_TRIGGER_LOGON = 9
TASK_TRIGGER_SESSION_STATE_CHANGE = 11
TASK_TRIGGER_CUSTOM_TRIGGER_01 = 12
TaskHandlerPS = Guid('f2a69db7-da2c-4352-90-66-86-fe-e6-da-ca-c9')
TaskHandlerStatusPS = Guid('9f15266d-d7ba-48f0-93-c1-e6-89-5f-6f-e5-ac')
TASKPAGE = Int32
TASKPAGE_TASK = 0
TASKPAGE_SCHEDULE = 1
TASKPAGE_SETTINGS = 2
TaskScheduler = Guid('0f87369f-a4e5-4cfc-bd-3e-73-e6-15-45-72-dd')
def _define_TRIGGER_TYPE_UNION_head():
    class TRIGGER_TYPE_UNION(Union):
        pass
    return TRIGGER_TYPE_UNION
def _define_TRIGGER_TYPE_UNION():
    TRIGGER_TYPE_UNION = win32more.System.TaskScheduler.TRIGGER_TYPE_UNION_head
    TRIGGER_TYPE_UNION._fields_ = [
        ('Daily', win32more.System.TaskScheduler.DAILY),
        ('Weekly', win32more.System.TaskScheduler.WEEKLY),
        ('MonthlyDate', win32more.System.TaskScheduler.MONTHLYDATE),
        ('MonthlyDOW', win32more.System.TaskScheduler.MONTHLYDOW),
    ]
    return TRIGGER_TYPE_UNION
def _define_WEEKLY_head():
    class WEEKLY(Structure):
        pass
    return WEEKLY
def _define_WEEKLY():
    WEEKLY = win32more.System.TaskScheduler.WEEKLY_head
    WEEKLY._fields_ = [
        ('WeeksInterval', UInt16),
        ('rgfDaysOfTheWeek', UInt16),
    ]
    return WEEKLY
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
