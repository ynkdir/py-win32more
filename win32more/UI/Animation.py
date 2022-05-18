from win32more import *
import win32more.Foundation
import win32more.Graphics.DirectComposition
import win32more.System.Com
import win32more.UI.Animation

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
UI_ANIMATION_SECONDS_EVENTUALLY = -1
UI_ANIMATION_REPEAT_INDEFINITELY = -1
UI_ANIMATION_REPEAT_INDEFINITELY_CONCLUDE_AT_END = -1
UI_ANIMATION_REPEAT_INDEFINITELY_CONCLUDE_AT_START = -2
UI_ANIMATION_SECONDS_INFINITE = -1
UI_ANIMATION_KEYFRAME = IntPtr
UIAnimationManager = Guid('4c1fc63a-695c-47e8-a339-1a194be3d0b8')
UIAnimationManager2 = Guid('d25d8842-8884-4a4a-b321-091314379bdd')
UIAnimationTransitionLibrary = Guid('1d6322ad-aa85-4ef5-a828-86d71067d145')
UIAnimationTransitionLibrary2 = Guid('812f944a-c5c8-4cd9-b0a6-b3da802f228d')
UIAnimationTransitionFactory = Guid('8a9b1cdd-fcd7-419c-8b44-42fd17db1887')
UIAnimationTransitionFactory2 = Guid('84302f97-7f7b-4040-b190-72ac9d18e420')
UIAnimationTimer = Guid('bfcd4a0c-06b6-4384-b768-0daa792c380e')
UI_ANIMATION_UPDATE_RESULT = Int32
UI_ANIMATION_UPDATE_NO_CHANGE = 0
UI_ANIMATION_UPDATE_VARIABLES_CHANGED = 1
UI_ANIMATION_MANAGER_STATUS = Int32
UI_ANIMATION_MANAGER_IDLE = 0
UI_ANIMATION_MANAGER_BUSY = 1
UI_ANIMATION_MODE = Int32
UI_ANIMATION_MODE_DISABLED = 0
UI_ANIMATION_MODE_SYSTEM_DEFAULT = 1
UI_ANIMATION_MODE_ENABLED = 2
UI_ANIMATION_REPEAT_MODE = Int32
UI_ANIMATION_REPEAT_MODE_NORMAL = 0
UI_ANIMATION_REPEAT_MODE_ALTERNATE = 1
def _define_IUIAnimationManager_head():
    class IUIAnimationManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('9169896c-ac8d-4e7d-94e5-67fa4dc2f2e8')
    return IUIAnimationManager
def _define_IUIAnimationManager():
    IUIAnimationManager = win32more.UI.Animation.IUIAnimationManager_head
    IUIAnimationManager.CreateAnimationVariable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.UI.Animation.IUIAnimationVariable_head), use_last_error=False)(3, 'CreateAnimationVariable', ((1, 'initialValue'),(1, 'variable'),)))
    IUIAnimationManager.ScheduleTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariable_head,win32more.UI.Animation.IUIAnimationTransition_head,Double, use_last_error=False)(4, 'ScheduleTransition', ((1, 'variable'),(1, 'transition'),(1, 'timeNow'),)))
    IUIAnimationManager.CreateStoryboard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Animation.IUIAnimationStoryboard_head), use_last_error=False)(5, 'CreateStoryboard', ((1, 'storyboard'),)))
    IUIAnimationManager.FinishAllStoryboards = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(6, 'FinishAllStoryboards', ((1, 'completionDeadline'),)))
    IUIAnimationManager.AbandonAllStoryboards = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'AbandonAllStoryboards', ()))
    IUIAnimationManager.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.UI.Animation.UI_ANIMATION_UPDATE_RESULT), use_last_error=False)(8, 'Update', ((1, 'timeNow'),(1, 'updateResult'),)))
    IUIAnimationManager.GetVariableFromTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(win32more.UI.Animation.IUIAnimationVariable_head), use_last_error=False)(9, 'GetVariableFromTag', ((1, 'object'),(1, 'id'),(1, 'variable'),)))
    IUIAnimationManager.GetStoryboardFromTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(win32more.UI.Animation.IUIAnimationStoryboard_head), use_last_error=False)(10, 'GetStoryboardFromTag', ((1, 'object'),(1, 'id'),(1, 'storyboard'),)))
    IUIAnimationManager.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Animation.UI_ANIMATION_MANAGER_STATUS), use_last_error=False)(11, 'GetStatus', ((1, 'status'),)))
    IUIAnimationManager.SetAnimationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.UI_ANIMATION_MODE, use_last_error=False)(12, 'SetAnimationMode', ((1, 'mode'),)))
    IUIAnimationManager.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'Pause', ()))
    IUIAnimationManager.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'Resume', ()))
    IUIAnimationManager.SetManagerEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationManagerEventHandler_head, use_last_error=False)(15, 'SetManagerEventHandler', ((1, 'handler'),)))
    IUIAnimationManager.SetCancelPriorityComparison = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationPriorityComparison_head, use_last_error=False)(16, 'SetCancelPriorityComparison', ((1, 'comparison'),)))
    IUIAnimationManager.SetTrimPriorityComparison = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationPriorityComparison_head, use_last_error=False)(17, 'SetTrimPriorityComparison', ((1, 'comparison'),)))
    IUIAnimationManager.SetCompressPriorityComparison = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationPriorityComparison_head, use_last_error=False)(18, 'SetCompressPriorityComparison', ((1, 'comparison'),)))
    IUIAnimationManager.SetConcludePriorityComparison = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationPriorityComparison_head, use_last_error=False)(19, 'SetConcludePriorityComparison', ((1, 'comparison'),)))
    IUIAnimationManager.SetDefaultLongestAcceptableDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(20, 'SetDefaultLongestAcceptableDelay', ((1, 'delay'),)))
    IUIAnimationManager.Shutdown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'Shutdown', ()))
    return IUIAnimationManager
UI_ANIMATION_ROUNDING_MODE = Int32
UI_ANIMATION_ROUNDING_NEAREST = 0
UI_ANIMATION_ROUNDING_FLOOR = 1
UI_ANIMATION_ROUNDING_CEILING = 2
def _define_IUIAnimationVariable_head():
    class IUIAnimationVariable(win32more.System.Com.IUnknown_head):
        Guid = Guid('8ceeb155-2849-4ce5-9448-91ff70e1e4d9')
    return IUIAnimationVariable
def _define_IUIAnimationVariable():
    IUIAnimationVariable = win32more.UI.Animation.IUIAnimationVariable_head
    IUIAnimationVariable.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(3, 'GetValue', ((1, 'value'),)))
    IUIAnimationVariable.GetFinalValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(4, 'GetFinalValue', ((1, 'finalValue'),)))
    IUIAnimationVariable.GetPreviousValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(5, 'GetPreviousValue', ((1, 'previousValue'),)))
    IUIAnimationVariable.GetIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(6, 'GetIntegerValue', ((1, 'value'),)))
    IUIAnimationVariable.GetFinalIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'GetFinalIntegerValue', ((1, 'finalValue'),)))
    IUIAnimationVariable.GetPreviousIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'GetPreviousIntegerValue', ((1, 'previousValue'),)))
    IUIAnimationVariable.GetCurrentStoryboard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Animation.IUIAnimationStoryboard_head), use_last_error=False)(9, 'GetCurrentStoryboard', ((1, 'storyboard'),)))
    IUIAnimationVariable.SetLowerBound = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(10, 'SetLowerBound', ((1, 'bound'),)))
    IUIAnimationVariable.SetUpperBound = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(11, 'SetUpperBound', ((1, 'bound'),)))
    IUIAnimationVariable.SetRoundingMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.UI_ANIMATION_ROUNDING_MODE, use_last_error=False)(12, 'SetRoundingMode', ((1, 'mode'),)))
    IUIAnimationVariable.SetTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32, use_last_error=False)(13, 'SetTag', ((1, 'object'),(1, 'id'),)))
    IUIAnimationVariable.GetTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head),POINTER(UInt32), use_last_error=False)(14, 'GetTag', ((1, 'object'),(1, 'id'),)))
    IUIAnimationVariable.SetVariableChangeHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariableChangeHandler_head, use_last_error=False)(15, 'SetVariableChangeHandler', ((1, 'handler'),)))
    IUIAnimationVariable.SetVariableIntegerChangeHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariableIntegerChangeHandler_head, use_last_error=False)(16, 'SetVariableIntegerChangeHandler', ((1, 'handler'),)))
    return IUIAnimationVariable
UI_ANIMATION_STORYBOARD_STATUS = Int32
UI_ANIMATION_STORYBOARD_BUILDING = 0
UI_ANIMATION_STORYBOARD_SCHEDULED = 1
UI_ANIMATION_STORYBOARD_CANCELLED = 2
UI_ANIMATION_STORYBOARD_PLAYING = 3
UI_ANIMATION_STORYBOARD_TRUNCATED = 4
UI_ANIMATION_STORYBOARD_FINISHED = 5
UI_ANIMATION_STORYBOARD_READY = 6
UI_ANIMATION_STORYBOARD_INSUFFICIENT_PRIORITY = 7
UI_ANIMATION_SCHEDULING_RESULT = Int32
UI_ANIMATION_SCHEDULING_UNEXPECTED_FAILURE = 0
UI_ANIMATION_SCHEDULING_INSUFFICIENT_PRIORITY = 1
UI_ANIMATION_SCHEDULING_ALREADY_SCHEDULED = 2
UI_ANIMATION_SCHEDULING_SUCCEEDED = 3
UI_ANIMATION_SCHEDULING_DEFERRED = 4
def _define_IUIAnimationStoryboard_head():
    class IUIAnimationStoryboard(win32more.System.Com.IUnknown_head):
        Guid = Guid('a8ff128f-9bf9-4af1-9e67-e5e410defb84')
    return IUIAnimationStoryboard
def _define_IUIAnimationStoryboard():
    IUIAnimationStoryboard = win32more.UI.Animation.IUIAnimationStoryboard_head
    IUIAnimationStoryboard.AddTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariable_head,win32more.UI.Animation.IUIAnimationTransition_head, use_last_error=False)(3, 'AddTransition', ((1, 'variable'),(1, 'transition'),)))
    IUIAnimationStoryboard.AddKeyframeAtOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.UI_ANIMATION_KEYFRAME,Double,POINTER(win32more.UI.Animation.UI_ANIMATION_KEYFRAME), use_last_error=False)(4, 'AddKeyframeAtOffset', ((1, 'existingKeyframe'),(1, 'offset'),(1, 'keyframe'),)))
    IUIAnimationStoryboard.AddKeyframeAfterTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationTransition_head,POINTER(win32more.UI.Animation.UI_ANIMATION_KEYFRAME), use_last_error=False)(5, 'AddKeyframeAfterTransition', ((1, 'transition'),(1, 'keyframe'),)))
    IUIAnimationStoryboard.AddTransitionAtKeyframe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariable_head,win32more.UI.Animation.IUIAnimationTransition_head,win32more.UI.Animation.UI_ANIMATION_KEYFRAME, use_last_error=False)(6, 'AddTransitionAtKeyframe', ((1, 'variable'),(1, 'transition'),(1, 'startKeyframe'),)))
    IUIAnimationStoryboard.AddTransitionBetweenKeyframes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariable_head,win32more.UI.Animation.IUIAnimationTransition_head,win32more.UI.Animation.UI_ANIMATION_KEYFRAME,win32more.UI.Animation.UI_ANIMATION_KEYFRAME, use_last_error=False)(7, 'AddTransitionBetweenKeyframes', ((1, 'variable'),(1, 'transition'),(1, 'startKeyframe'),(1, 'endKeyframe'),)))
    IUIAnimationStoryboard.RepeatBetweenKeyframes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.UI_ANIMATION_KEYFRAME,win32more.UI.Animation.UI_ANIMATION_KEYFRAME,Int32, use_last_error=False)(8, 'RepeatBetweenKeyframes', ((1, 'startKeyframe'),(1, 'endKeyframe'),(1, 'repetitionCount'),)))
    IUIAnimationStoryboard.HoldVariable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariable_head, use_last_error=False)(9, 'HoldVariable', ((1, 'variable'),)))
    IUIAnimationStoryboard.SetLongestAcceptableDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(10, 'SetLongestAcceptableDelay', ((1, 'delay'),)))
    IUIAnimationStoryboard.Schedule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.UI.Animation.UI_ANIMATION_SCHEDULING_RESULT), use_last_error=False)(11, 'Schedule', ((1, 'timeNow'),(1, 'schedulingResult'),)))
    IUIAnimationStoryboard.Conclude = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Conclude', ()))
    IUIAnimationStoryboard.Finish = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(13, 'Finish', ((1, 'completionDeadline'),)))
    IUIAnimationStoryboard.Abandon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'Abandon', ()))
    IUIAnimationStoryboard.SetTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32, use_last_error=False)(15, 'SetTag', ((1, 'object'),(1, 'id'),)))
    IUIAnimationStoryboard.GetTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head),POINTER(UInt32), use_last_error=False)(16, 'GetTag', ((1, 'object'),(1, 'id'),)))
    IUIAnimationStoryboard.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Animation.UI_ANIMATION_STORYBOARD_STATUS), use_last_error=False)(17, 'GetStatus', ((1, 'status'),)))
    IUIAnimationStoryboard.GetElapsedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(18, 'GetElapsedTime', ((1, 'elapsedTime'),)))
    IUIAnimationStoryboard.SetStoryboardEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationStoryboardEventHandler_head, use_last_error=False)(19, 'SetStoryboardEventHandler', ((1, 'handler'),)))
    return IUIAnimationStoryboard
def _define_IUIAnimationTransition_head():
    class IUIAnimationTransition(win32more.System.Com.IUnknown_head):
        Guid = Guid('dc6ce252-f731-41cf-b610-614b6ca049ad')
    return IUIAnimationTransition
def _define_IUIAnimationTransition():
    IUIAnimationTransition = win32more.UI.Animation.IUIAnimationTransition_head
    IUIAnimationTransition.SetInitialValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(3, 'SetInitialValue', ((1, 'value'),)))
    IUIAnimationTransition.SetInitialVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(4, 'SetInitialVelocity', ((1, 'velocity'),)))
    IUIAnimationTransition.IsDurationKnown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'IsDurationKnown', ()))
    IUIAnimationTransition.GetDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(6, 'GetDuration', ((1, 'duration'),)))
    return IUIAnimationTransition
def _define_IUIAnimationManagerEventHandler_head():
    class IUIAnimationManagerEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('783321ed-78a3-4366-b574-6af607a64788')
    return IUIAnimationManagerEventHandler
def _define_IUIAnimationManagerEventHandler():
    IUIAnimationManagerEventHandler = win32more.UI.Animation.IUIAnimationManagerEventHandler_head
    IUIAnimationManagerEventHandler.OnManagerStatusChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.UI_ANIMATION_MANAGER_STATUS,win32more.UI.Animation.UI_ANIMATION_MANAGER_STATUS, use_last_error=False)(3, 'OnManagerStatusChanged', ((1, 'newStatus'),(1, 'previousStatus'),)))
    return IUIAnimationManagerEventHandler
def _define_IUIAnimationVariableChangeHandler_head():
    class IUIAnimationVariableChangeHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('6358b7ba-87d2-42d5-bf71-82e919dd5862')
    return IUIAnimationVariableChangeHandler
def _define_IUIAnimationVariableChangeHandler():
    IUIAnimationVariableChangeHandler = win32more.UI.Animation.IUIAnimationVariableChangeHandler_head
    IUIAnimationVariableChangeHandler.OnValueChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationStoryboard_head,win32more.UI.Animation.IUIAnimationVariable_head,Double,Double, use_last_error=False)(3, 'OnValueChanged', ((1, 'storyboard'),(1, 'variable'),(1, 'newValue'),(1, 'previousValue'),)))
    return IUIAnimationVariableChangeHandler
def _define_IUIAnimationVariableIntegerChangeHandler_head():
    class IUIAnimationVariableIntegerChangeHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('bb3e1550-356e-44b0-99da-85ac6017865e')
    return IUIAnimationVariableIntegerChangeHandler
def _define_IUIAnimationVariableIntegerChangeHandler():
    IUIAnimationVariableIntegerChangeHandler = win32more.UI.Animation.IUIAnimationVariableIntegerChangeHandler_head
    IUIAnimationVariableIntegerChangeHandler.OnIntegerValueChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationStoryboard_head,win32more.UI.Animation.IUIAnimationVariable_head,Int32,Int32, use_last_error=False)(3, 'OnIntegerValueChanged', ((1, 'storyboard'),(1, 'variable'),(1, 'newValue'),(1, 'previousValue'),)))
    return IUIAnimationVariableIntegerChangeHandler
def _define_IUIAnimationStoryboardEventHandler_head():
    class IUIAnimationStoryboardEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('3d5c9008-ec7c-4364-9f8a-9af3c58cbae6')
    return IUIAnimationStoryboardEventHandler
def _define_IUIAnimationStoryboardEventHandler():
    IUIAnimationStoryboardEventHandler = win32more.UI.Animation.IUIAnimationStoryboardEventHandler_head
    IUIAnimationStoryboardEventHandler.OnStoryboardStatusChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationStoryboard_head,win32more.UI.Animation.UI_ANIMATION_STORYBOARD_STATUS,win32more.UI.Animation.UI_ANIMATION_STORYBOARD_STATUS, use_last_error=False)(3, 'OnStoryboardStatusChanged', ((1, 'storyboard'),(1, 'newStatus'),(1, 'previousStatus'),)))
    IUIAnimationStoryboardEventHandler.OnStoryboardUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationStoryboard_head, use_last_error=False)(4, 'OnStoryboardUpdated', ((1, 'storyboard'),)))
    return IUIAnimationStoryboardEventHandler
UI_ANIMATION_PRIORITY_EFFECT = Int32
UI_ANIMATION_PRIORITY_EFFECT_FAILURE = 0
UI_ANIMATION_PRIORITY_EFFECT_DELAY = 1
def _define_IUIAnimationPriorityComparison_head():
    class IUIAnimationPriorityComparison(win32more.System.Com.IUnknown_head):
        Guid = Guid('83fa9b74-5f86-4618-bc6a-a2fac19b3f44')
    return IUIAnimationPriorityComparison
def _define_IUIAnimationPriorityComparison():
    IUIAnimationPriorityComparison = win32more.UI.Animation.IUIAnimationPriorityComparison_head
    IUIAnimationPriorityComparison.HasPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationStoryboard_head,win32more.UI.Animation.IUIAnimationStoryboard_head,win32more.UI.Animation.UI_ANIMATION_PRIORITY_EFFECT, use_last_error=False)(3, 'HasPriority', ((1, 'scheduledStoryboard'),(1, 'newStoryboard'),(1, 'priorityEffect'),)))
    return IUIAnimationPriorityComparison
UI_ANIMATION_SLOPE = Int32
UI_ANIMATION_SLOPE_INCREASING = 0
UI_ANIMATION_SLOPE_DECREASING = 1
def _define_IUIAnimationTransitionLibrary_head():
    class IUIAnimationTransitionLibrary(win32more.System.Com.IUnknown_head):
        Guid = Guid('ca5a14b1-d24f-48b8-8fe4-c78169ba954e')
    return IUIAnimationTransitionLibrary
def _define_IUIAnimationTransitionLibrary():
    IUIAnimationTransitionLibrary = win32more.UI.Animation.IUIAnimationTransitionLibrary_head
    IUIAnimationTransitionLibrary.CreateInstantaneousTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition_head), use_last_error=False)(3, 'CreateInstantaneousTransition', ((1, 'finalValue'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary.CreateConstantTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition_head), use_last_error=False)(4, 'CreateConstantTransition', ((1, 'duration'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary.CreateDiscreteTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition_head), use_last_error=False)(5, 'CreateDiscreteTransition', ((1, 'delay'),(1, 'finalValue'),(1, 'hold'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary.CreateLinearTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition_head), use_last_error=False)(6, 'CreateLinearTransition', ((1, 'duration'),(1, 'finalValue'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary.CreateLinearTransitionFromSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition_head), use_last_error=False)(7, 'CreateLinearTransitionFromSpeed', ((1, 'speed'),(1, 'finalValue'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary.CreateSinusoidalTransitionFromVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition_head), use_last_error=False)(8, 'CreateSinusoidalTransitionFromVelocity', ((1, 'duration'),(1, 'period'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary.CreateSinusoidalTransitionFromRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,Double,Double,win32more.UI.Animation.UI_ANIMATION_SLOPE,POINTER(win32more.UI.Animation.IUIAnimationTransition_head), use_last_error=False)(9, 'CreateSinusoidalTransitionFromRange', ((1, 'duration'),(1, 'minimumValue'),(1, 'maximumValue'),(1, 'period'),(1, 'slope'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary.CreateAccelerateDecelerateTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition_head), use_last_error=False)(10, 'CreateAccelerateDecelerateTransition', ((1, 'duration'),(1, 'finalValue'),(1, 'accelerationRatio'),(1, 'decelerationRatio'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary.CreateReversalTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition_head), use_last_error=False)(11, 'CreateReversalTransition', ((1, 'duration'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary.CreateCubicTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition_head), use_last_error=False)(12, 'CreateCubicTransition', ((1, 'duration'),(1, 'finalValue'),(1, 'finalVelocity'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary.CreateSmoothStopTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition_head), use_last_error=False)(13, 'CreateSmoothStopTransition', ((1, 'maximumDuration'),(1, 'finalValue'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary.CreateParabolicTransitionFromAcceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition_head), use_last_error=False)(14, 'CreateParabolicTransitionFromAcceleration', ((1, 'finalValue'),(1, 'finalVelocity'),(1, 'acceleration'),(1, 'transition'),)))
    return IUIAnimationTransitionLibrary
UI_ANIMATION_DEPENDENCIES = UInt32
UI_ANIMATION_DEPENDENCY_NONE = 0
UI_ANIMATION_DEPENDENCY_INTERMEDIATE_VALUES = 1
UI_ANIMATION_DEPENDENCY_FINAL_VALUE = 2
UI_ANIMATION_DEPENDENCY_FINAL_VELOCITY = 4
UI_ANIMATION_DEPENDENCY_DURATION = 8
def _define_IUIAnimationInterpolator_head():
    class IUIAnimationInterpolator(win32more.System.Com.IUnknown_head):
        Guid = Guid('7815cbba-ddf7-478c-a46c-7b6c738b7978')
    return IUIAnimationInterpolator
def _define_IUIAnimationInterpolator():
    IUIAnimationInterpolator = win32more.UI.Animation.IUIAnimationInterpolator_head
    IUIAnimationInterpolator.SetInitialValueAndVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double, use_last_error=False)(3, 'SetInitialValueAndVelocity', ((1, 'initialValue'),(1, 'initialVelocity'),)))
    IUIAnimationInterpolator.SetDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(4, 'SetDuration', ((1, 'duration'),)))
    IUIAnimationInterpolator.GetDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(5, 'GetDuration', ((1, 'duration'),)))
    IUIAnimationInterpolator.GetFinalValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(6, 'GetFinalValue', ((1, 'value'),)))
    IUIAnimationInterpolator.InterpolateValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Double), use_last_error=False)(7, 'InterpolateValue', ((1, 'offset'),(1, 'value'),)))
    IUIAnimationInterpolator.InterpolateVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Double), use_last_error=False)(8, 'InterpolateVelocity', ((1, 'offset'),(1, 'velocity'),)))
    IUIAnimationInterpolator.GetDependencies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Animation.UI_ANIMATION_DEPENDENCIES),POINTER(win32more.UI.Animation.UI_ANIMATION_DEPENDENCIES),POINTER(win32more.UI.Animation.UI_ANIMATION_DEPENDENCIES), use_last_error=False)(9, 'GetDependencies', ((1, 'initialValueDependencies'),(1, 'initialVelocityDependencies'),(1, 'durationDependencies'),)))
    return IUIAnimationInterpolator
def _define_IUIAnimationTransitionFactory_head():
    class IUIAnimationTransitionFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('fcd91e03-3e3b-45ad-bbb1-6dfc8153743d')
    return IUIAnimationTransitionFactory
def _define_IUIAnimationTransitionFactory():
    IUIAnimationTransitionFactory = win32more.UI.Animation.IUIAnimationTransitionFactory_head
    IUIAnimationTransitionFactory.CreateTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationInterpolator_head,POINTER(win32more.UI.Animation.IUIAnimationTransition_head), use_last_error=False)(3, 'CreateTransition', ((1, 'interpolator'),(1, 'transition'),)))
    return IUIAnimationTransitionFactory
UI_ANIMATION_IDLE_BEHAVIOR = Int32
UI_ANIMATION_IDLE_BEHAVIOR_CONTINUE = 0
UI_ANIMATION_IDLE_BEHAVIOR_DISABLE = 1
def _define_IUIAnimationTimer_head():
    class IUIAnimationTimer(win32more.System.Com.IUnknown_head):
        Guid = Guid('6b0efad1-a053-41d6-9085-33a689144665')
    return IUIAnimationTimer
def _define_IUIAnimationTimer():
    IUIAnimationTimer = win32more.UI.Animation.IUIAnimationTimer_head
    IUIAnimationTimer.SetTimerUpdateHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationTimerUpdateHandler_head,win32more.UI.Animation.UI_ANIMATION_IDLE_BEHAVIOR, use_last_error=False)(3, 'SetTimerUpdateHandler', ((1, 'updateHandler'),(1, 'idleBehavior'),)))
    IUIAnimationTimer.SetTimerEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationTimerEventHandler_head, use_last_error=False)(4, 'SetTimerEventHandler', ((1, 'handler'),)))
    IUIAnimationTimer.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Enable', ()))
    IUIAnimationTimer.Disable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Disable', ()))
    IUIAnimationTimer.IsEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'IsEnabled', ()))
    IUIAnimationTimer.GetTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(8, 'GetTime', ((1, 'seconds'),)))
    IUIAnimationTimer.SetFrameRateThreshold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'SetFrameRateThreshold', ((1, 'framesPerSecond'),)))
    return IUIAnimationTimer
def _define_IUIAnimationTimerUpdateHandler_head():
    class IUIAnimationTimerUpdateHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('195509b7-5d5e-4e3e-b278-ee3759b367ad')
    return IUIAnimationTimerUpdateHandler
def _define_IUIAnimationTimerUpdateHandler():
    IUIAnimationTimerUpdateHandler = win32more.UI.Animation.IUIAnimationTimerUpdateHandler_head
    IUIAnimationTimerUpdateHandler.OnUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.UI.Animation.UI_ANIMATION_UPDATE_RESULT), use_last_error=False)(3, 'OnUpdate', ((1, 'timeNow'),(1, 'result'),)))
    IUIAnimationTimerUpdateHandler.SetTimerClientEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationTimerClientEventHandler_head, use_last_error=False)(4, 'SetTimerClientEventHandler', ((1, 'handler'),)))
    IUIAnimationTimerUpdateHandler.ClearTimerClientEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'ClearTimerClientEventHandler', ()))
    return IUIAnimationTimerUpdateHandler
UI_ANIMATION_TIMER_CLIENT_STATUS = Int32
UI_ANIMATION_TIMER_CLIENT_IDLE = 0
UI_ANIMATION_TIMER_CLIENT_BUSY = 1
def _define_IUIAnimationTimerClientEventHandler_head():
    class IUIAnimationTimerClientEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('bedb4db6-94fa-4bfb-a47f-ef2d9e408c25')
    return IUIAnimationTimerClientEventHandler
def _define_IUIAnimationTimerClientEventHandler():
    IUIAnimationTimerClientEventHandler = win32more.UI.Animation.IUIAnimationTimerClientEventHandler_head
    IUIAnimationTimerClientEventHandler.OnTimerClientStatusChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.UI_ANIMATION_TIMER_CLIENT_STATUS,win32more.UI.Animation.UI_ANIMATION_TIMER_CLIENT_STATUS, use_last_error=False)(3, 'OnTimerClientStatusChanged', ((1, 'newStatus'),(1, 'previousStatus'),)))
    return IUIAnimationTimerClientEventHandler
def _define_IUIAnimationTimerEventHandler_head():
    class IUIAnimationTimerEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('274a7dea-d771-4095-abbd-8df7abd23ce3')
    return IUIAnimationTimerEventHandler
def _define_IUIAnimationTimerEventHandler():
    IUIAnimationTimerEventHandler = win32more.UI.Animation.IUIAnimationTimerEventHandler_head
    IUIAnimationTimerEventHandler.OnPreUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnPreUpdate', ()))
    IUIAnimationTimerEventHandler.OnPostUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnPostUpdate', ()))
    IUIAnimationTimerEventHandler.OnRenderingTooSlow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'OnRenderingTooSlow', ((1, 'framesPerSecond'),)))
    return IUIAnimationTimerEventHandler
def _define_IUIAnimationManager2_head():
    class IUIAnimationManager2(win32more.System.Com.IUnknown_head):
        Guid = Guid('d8b6f7d4-4109-4d3f-acee-879926968cb1')
    return IUIAnimationManager2
def _define_IUIAnimationManager2():
    IUIAnimationManager2 = win32more.UI.Animation.IUIAnimationManager2_head
    IUIAnimationManager2.CreateAnimationVectorVariable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32,POINTER(win32more.UI.Animation.IUIAnimationVariable2_head), use_last_error=False)(3, 'CreateAnimationVectorVariable', ((1, 'initialValue'),(1, 'cDimension'),(1, 'variable'),)))
    IUIAnimationManager2.CreateAnimationVariable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.UI.Animation.IUIAnimationVariable2_head), use_last_error=False)(4, 'CreateAnimationVariable', ((1, 'initialValue'),(1, 'variable'),)))
    IUIAnimationManager2.ScheduleTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariable2_head,win32more.UI.Animation.IUIAnimationTransition2_head,Double, use_last_error=False)(5, 'ScheduleTransition', ((1, 'variable'),(1, 'transition'),(1, 'timeNow'),)))
    IUIAnimationManager2.CreateStoryboard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Animation.IUIAnimationStoryboard2_head), use_last_error=False)(6, 'CreateStoryboard', ((1, 'storyboard'),)))
    IUIAnimationManager2.FinishAllStoryboards = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(7, 'FinishAllStoryboards', ((1, 'completionDeadline'),)))
    IUIAnimationManager2.AbandonAllStoryboards = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'AbandonAllStoryboards', ()))
    IUIAnimationManager2.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.UI.Animation.UI_ANIMATION_UPDATE_RESULT), use_last_error=False)(9, 'Update', ((1, 'timeNow'),(1, 'updateResult'),)))
    IUIAnimationManager2.GetVariableFromTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(win32more.UI.Animation.IUIAnimationVariable2_head), use_last_error=False)(10, 'GetVariableFromTag', ((1, 'object'),(1, 'id'),(1, 'variable'),)))
    IUIAnimationManager2.GetStoryboardFromTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(win32more.UI.Animation.IUIAnimationStoryboard2_head), use_last_error=False)(11, 'GetStoryboardFromTag', ((1, 'object'),(1, 'id'),(1, 'storyboard'),)))
    IUIAnimationManager2.EstimateNextEventTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(12, 'EstimateNextEventTime', ((1, 'seconds'),)))
    IUIAnimationManager2.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Animation.UI_ANIMATION_MANAGER_STATUS), use_last_error=False)(13, 'GetStatus', ((1, 'status'),)))
    IUIAnimationManager2.SetAnimationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.UI_ANIMATION_MODE, use_last_error=False)(14, 'SetAnimationMode', ((1, 'mode'),)))
    IUIAnimationManager2.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'Pause', ()))
    IUIAnimationManager2.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Resume', ()))
    IUIAnimationManager2.SetManagerEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationManagerEventHandler2_head,win32more.Foundation.BOOL, use_last_error=False)(17, 'SetManagerEventHandler', ((1, 'handler'),(1, 'fRegisterForNextAnimationEvent'),)))
    IUIAnimationManager2.SetCancelPriorityComparison = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationPriorityComparison2_head, use_last_error=False)(18, 'SetCancelPriorityComparison', ((1, 'comparison'),)))
    IUIAnimationManager2.SetTrimPriorityComparison = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationPriorityComparison2_head, use_last_error=False)(19, 'SetTrimPriorityComparison', ((1, 'comparison'),)))
    IUIAnimationManager2.SetCompressPriorityComparison = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationPriorityComparison2_head, use_last_error=False)(20, 'SetCompressPriorityComparison', ((1, 'comparison'),)))
    IUIAnimationManager2.SetConcludePriorityComparison = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationPriorityComparison2_head, use_last_error=False)(21, 'SetConcludePriorityComparison', ((1, 'comparison'),)))
    IUIAnimationManager2.SetDefaultLongestAcceptableDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(22, 'SetDefaultLongestAcceptableDelay', ((1, 'delay'),)))
    IUIAnimationManager2.Shutdown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(23, 'Shutdown', ()))
    return IUIAnimationManager2
def _define_IUIAnimationVariable2_head():
    class IUIAnimationVariable2(win32more.System.Com.IUnknown_head):
        Guid = Guid('4914b304-96ab-44d9-9e77-d5109b7e7466')
    return IUIAnimationVariable2
def _define_IUIAnimationVariable2():
    IUIAnimationVariable2 = win32more.UI.Animation.IUIAnimationVariable2_head
    IUIAnimationVariable2.GetDimension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetDimension', ((1, 'dimension'),)))
    IUIAnimationVariable2.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(4, 'GetValue', ((1, 'value'),)))
    IUIAnimationVariable2.GetVectorValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32, use_last_error=False)(5, 'GetVectorValue', ((1, 'value'),(1, 'cDimension'),)))
    IUIAnimationVariable2.GetCurve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectComposition.IDCompositionAnimation_head, use_last_error=False)(6, 'GetCurve', ((1, 'animation'),)))
    IUIAnimationVariable2.GetVectorCurve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectComposition.IDCompositionAnimation_head),UInt32, use_last_error=False)(7, 'GetVectorCurve', ((1, 'animation'),(1, 'cDimension'),)))
    IUIAnimationVariable2.GetFinalValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(8, 'GetFinalValue', ((1, 'finalValue'),)))
    IUIAnimationVariable2.GetFinalVectorValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32, use_last_error=False)(9, 'GetFinalVectorValue', ((1, 'finalValue'),(1, 'cDimension'),)))
    IUIAnimationVariable2.GetPreviousValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(10, 'GetPreviousValue', ((1, 'previousValue'),)))
    IUIAnimationVariable2.GetPreviousVectorValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32, use_last_error=False)(11, 'GetPreviousVectorValue', ((1, 'previousValue'),(1, 'cDimension'),)))
    IUIAnimationVariable2.GetIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'GetIntegerValue', ((1, 'value'),)))
    IUIAnimationVariable2.GetIntegerVectorValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32, use_last_error=False)(13, 'GetIntegerVectorValue', ((1, 'value'),(1, 'cDimension'),)))
    IUIAnimationVariable2.GetFinalIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'GetFinalIntegerValue', ((1, 'finalValue'),)))
    IUIAnimationVariable2.GetFinalIntegerVectorValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32, use_last_error=False)(15, 'GetFinalIntegerVectorValue', ((1, 'finalValue'),(1, 'cDimension'),)))
    IUIAnimationVariable2.GetPreviousIntegerValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'GetPreviousIntegerValue', ((1, 'previousValue'),)))
    IUIAnimationVariable2.GetPreviousIntegerVectorValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32, use_last_error=False)(17, 'GetPreviousIntegerVectorValue', ((1, 'previousValue'),(1, 'cDimension'),)))
    IUIAnimationVariable2.GetCurrentStoryboard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Animation.IUIAnimationStoryboard2_head), use_last_error=False)(18, 'GetCurrentStoryboard', ((1, 'storyboard'),)))
    IUIAnimationVariable2.SetLowerBound = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(19, 'SetLowerBound', ((1, 'bound'),)))
    IUIAnimationVariable2.SetLowerBoundVector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32, use_last_error=False)(20, 'SetLowerBoundVector', ((1, 'bound'),(1, 'cDimension'),)))
    IUIAnimationVariable2.SetUpperBound = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(21, 'SetUpperBound', ((1, 'bound'),)))
    IUIAnimationVariable2.SetUpperBoundVector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32, use_last_error=False)(22, 'SetUpperBoundVector', ((1, 'bound'),(1, 'cDimension'),)))
    IUIAnimationVariable2.SetRoundingMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.UI_ANIMATION_ROUNDING_MODE, use_last_error=False)(23, 'SetRoundingMode', ((1, 'mode'),)))
    IUIAnimationVariable2.SetTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32, use_last_error=False)(24, 'SetTag', ((1, 'object'),(1, 'id'),)))
    IUIAnimationVariable2.GetTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head),POINTER(UInt32), use_last_error=False)(25, 'GetTag', ((1, 'object'),(1, 'id'),)))
    IUIAnimationVariable2.SetVariableChangeHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariableChangeHandler2_head,win32more.Foundation.BOOL, use_last_error=False)(26, 'SetVariableChangeHandler', ((1, 'handler'),(1, 'fRegisterForNextAnimationEvent'),)))
    IUIAnimationVariable2.SetVariableIntegerChangeHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariableIntegerChangeHandler2_head,win32more.Foundation.BOOL, use_last_error=False)(27, 'SetVariableIntegerChangeHandler', ((1, 'handler'),(1, 'fRegisterForNextAnimationEvent'),)))
    IUIAnimationVariable2.SetVariableCurveChangeHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariableCurveChangeHandler2_head, use_last_error=False)(28, 'SetVariableCurveChangeHandler', ((1, 'handler'),)))
    return IUIAnimationVariable2
def _define_IUIAnimationTransition2_head():
    class IUIAnimationTransition2(win32more.System.Com.IUnknown_head):
        Guid = Guid('62ff9123-a85a-4e9b-a218-435a93e268fd')
    return IUIAnimationTransition2
def _define_IUIAnimationTransition2():
    IUIAnimationTransition2 = win32more.UI.Animation.IUIAnimationTransition2_head
    IUIAnimationTransition2.GetDimension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetDimension', ((1, 'dimension'),)))
    IUIAnimationTransition2.SetInitialValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(4, 'SetInitialValue', ((1, 'value'),)))
    IUIAnimationTransition2.SetInitialVectorValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32, use_last_error=False)(5, 'SetInitialVectorValue', ((1, 'value'),(1, 'cDimension'),)))
    IUIAnimationTransition2.SetInitialVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(6, 'SetInitialVelocity', ((1, 'velocity'),)))
    IUIAnimationTransition2.SetInitialVectorVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32, use_last_error=False)(7, 'SetInitialVectorVelocity', ((1, 'velocity'),(1, 'cDimension'),)))
    IUIAnimationTransition2.IsDurationKnown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'IsDurationKnown', ()))
    IUIAnimationTransition2.GetDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(9, 'GetDuration', ((1, 'duration'),)))
    return IUIAnimationTransition2
def _define_IUIAnimationManagerEventHandler2_head():
    class IUIAnimationManagerEventHandler2(win32more.System.Com.IUnknown_head):
        Guid = Guid('f6e022ba-bff3-42ec-9033-e073f33e83c3')
    return IUIAnimationManagerEventHandler2
def _define_IUIAnimationManagerEventHandler2():
    IUIAnimationManagerEventHandler2 = win32more.UI.Animation.IUIAnimationManagerEventHandler2_head
    IUIAnimationManagerEventHandler2.OnManagerStatusChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.UI_ANIMATION_MANAGER_STATUS,win32more.UI.Animation.UI_ANIMATION_MANAGER_STATUS, use_last_error=False)(3, 'OnManagerStatusChanged', ((1, 'newStatus'),(1, 'previousStatus'),)))
    return IUIAnimationManagerEventHandler2
def _define_IUIAnimationVariableChangeHandler2_head():
    class IUIAnimationVariableChangeHandler2(win32more.System.Com.IUnknown_head):
        Guid = Guid('63acc8d2-6eae-4bb0-b879-586dd8cfbe42')
    return IUIAnimationVariableChangeHandler2
def _define_IUIAnimationVariableChangeHandler2():
    IUIAnimationVariableChangeHandler2 = win32more.UI.Animation.IUIAnimationVariableChangeHandler2_head
    IUIAnimationVariableChangeHandler2.OnValueChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationStoryboard2_head,win32more.UI.Animation.IUIAnimationVariable2_head,POINTER(Double),POINTER(Double),UInt32, use_last_error=False)(3, 'OnValueChanged', ((1, 'storyboard'),(1, 'variable'),(1, 'newValue'),(1, 'previousValue'),(1, 'cDimension'),)))
    return IUIAnimationVariableChangeHandler2
def _define_IUIAnimationVariableIntegerChangeHandler2_head():
    class IUIAnimationVariableIntegerChangeHandler2(win32more.System.Com.IUnknown_head):
        Guid = Guid('829b6cf1-4f3a-4412-ae09-b243eb4c6b58')
    return IUIAnimationVariableIntegerChangeHandler2
def _define_IUIAnimationVariableIntegerChangeHandler2():
    IUIAnimationVariableIntegerChangeHandler2 = win32more.UI.Animation.IUIAnimationVariableIntegerChangeHandler2_head
    IUIAnimationVariableIntegerChangeHandler2.OnIntegerValueChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationStoryboard2_head,win32more.UI.Animation.IUIAnimationVariable2_head,POINTER(Int32),POINTER(Int32),UInt32, use_last_error=False)(3, 'OnIntegerValueChanged', ((1, 'storyboard'),(1, 'variable'),(1, 'newValue'),(1, 'previousValue'),(1, 'cDimension'),)))
    return IUIAnimationVariableIntegerChangeHandler2
def _define_IUIAnimationVariableCurveChangeHandler2_head():
    class IUIAnimationVariableCurveChangeHandler2(win32more.System.Com.IUnknown_head):
        Guid = Guid('72895e91-0145-4c21-9192-5aab40eddf80')
    return IUIAnimationVariableCurveChangeHandler2
def _define_IUIAnimationVariableCurveChangeHandler2():
    IUIAnimationVariableCurveChangeHandler2 = win32more.UI.Animation.IUIAnimationVariableCurveChangeHandler2_head
    IUIAnimationVariableCurveChangeHandler2.OnCurveChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariable2_head, use_last_error=False)(3, 'OnCurveChanged', ((1, 'variable'),)))
    return IUIAnimationVariableCurveChangeHandler2
def _define_IUIAnimationStoryboardEventHandler2_head():
    class IUIAnimationStoryboardEventHandler2(win32more.System.Com.IUnknown_head):
        Guid = Guid('bac5f55a-ba7c-414c-b599-fbf850f553c6')
    return IUIAnimationStoryboardEventHandler2
def _define_IUIAnimationStoryboardEventHandler2():
    IUIAnimationStoryboardEventHandler2 = win32more.UI.Animation.IUIAnimationStoryboardEventHandler2_head
    IUIAnimationStoryboardEventHandler2.OnStoryboardStatusChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationStoryboard2_head,win32more.UI.Animation.UI_ANIMATION_STORYBOARD_STATUS,win32more.UI.Animation.UI_ANIMATION_STORYBOARD_STATUS, use_last_error=False)(3, 'OnStoryboardStatusChanged', ((1, 'storyboard'),(1, 'newStatus'),(1, 'previousStatus'),)))
    IUIAnimationStoryboardEventHandler2.OnStoryboardUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationStoryboard2_head, use_last_error=False)(4, 'OnStoryboardUpdated', ((1, 'storyboard'),)))
    return IUIAnimationStoryboardEventHandler2
def _define_IUIAnimationLoopIterationChangeHandler2_head():
    class IUIAnimationLoopIterationChangeHandler2(win32more.System.Com.IUnknown_head):
        Guid = Guid('2d3b15a4-4762-47ab-a030-b23221df3ae0')
    return IUIAnimationLoopIterationChangeHandler2
def _define_IUIAnimationLoopIterationChangeHandler2():
    IUIAnimationLoopIterationChangeHandler2 = win32more.UI.Animation.IUIAnimationLoopIterationChangeHandler2_head
    IUIAnimationLoopIterationChangeHandler2.OnLoopIterationChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationStoryboard2_head,UIntPtr,UInt32,UInt32, use_last_error=False)(3, 'OnLoopIterationChanged', ((1, 'storyboard'),(1, 'id'),(1, 'newIterationCount'),(1, 'oldIterationCount'),)))
    return IUIAnimationLoopIterationChangeHandler2
def _define_IUIAnimationPriorityComparison2_head():
    class IUIAnimationPriorityComparison2(win32more.System.Com.IUnknown_head):
        Guid = Guid('5b6d7a37-4621-467c-8b05-70131de62ddb')
    return IUIAnimationPriorityComparison2
def _define_IUIAnimationPriorityComparison2():
    IUIAnimationPriorityComparison2 = win32more.UI.Animation.IUIAnimationPriorityComparison2_head
    IUIAnimationPriorityComparison2.HasPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationStoryboard2_head,win32more.UI.Animation.IUIAnimationStoryboard2_head,win32more.UI.Animation.UI_ANIMATION_PRIORITY_EFFECT, use_last_error=False)(3, 'HasPriority', ((1, 'scheduledStoryboard'),(1, 'newStoryboard'),(1, 'priorityEffect'),)))
    return IUIAnimationPriorityComparison2
def _define_IUIAnimationTransitionLibrary2_head():
    class IUIAnimationTransitionLibrary2(win32more.System.Com.IUnknown_head):
        Guid = Guid('03cfae53-9580-4ee3-b363-2ece51b4af6a')
    return IUIAnimationTransitionLibrary2
def _define_IUIAnimationTransitionLibrary2():
    IUIAnimationTransitionLibrary2 = win32more.UI.Animation.IUIAnimationTransitionLibrary2_head
    IUIAnimationTransitionLibrary2.CreateInstantaneousTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(3, 'CreateInstantaneousTransition', ((1, 'finalValue'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateInstantaneousVectorTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(4, 'CreateInstantaneousVectorTransition', ((1, 'finalValue'),(1, 'cDimension'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateConstantTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(5, 'CreateConstantTransition', ((1, 'duration'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateDiscreteTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(6, 'CreateDiscreteTransition', ((1, 'delay'),(1, 'finalValue'),(1, 'hold'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateDiscreteVectorTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Double),UInt32,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(7, 'CreateDiscreteVectorTransition', ((1, 'delay'),(1, 'finalValue'),(1, 'cDimension'),(1, 'hold'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateLinearTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(8, 'CreateLinearTransition', ((1, 'duration'),(1, 'finalValue'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateLinearVectorTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Double),UInt32,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(9, 'CreateLinearVectorTransition', ((1, 'duration'),(1, 'finalValue'),(1, 'cDimension'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateLinearTransitionFromSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(10, 'CreateLinearTransitionFromSpeed', ((1, 'speed'),(1, 'finalValue'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateLinearVectorTransitionFromSpeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Double),UInt32,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(11, 'CreateLinearVectorTransitionFromSpeed', ((1, 'speed'),(1, 'finalValue'),(1, 'cDimension'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateSinusoidalTransitionFromVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(12, 'CreateSinusoidalTransitionFromVelocity', ((1, 'duration'),(1, 'period'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateSinusoidalTransitionFromRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,Double,Double,win32more.UI.Animation.UI_ANIMATION_SLOPE,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(13, 'CreateSinusoidalTransitionFromRange', ((1, 'duration'),(1, 'minimumValue'),(1, 'maximumValue'),(1, 'period'),(1, 'slope'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateAccelerateDecelerateTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(14, 'CreateAccelerateDecelerateTransition', ((1, 'duration'),(1, 'finalValue'),(1, 'accelerationRatio'),(1, 'decelerationRatio'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateReversalTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(15, 'CreateReversalTransition', ((1, 'duration'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateCubicTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(16, 'CreateCubicTransition', ((1, 'duration'),(1, 'finalValue'),(1, 'finalVelocity'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateCubicVectorTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Double),POINTER(Double),UInt32,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(17, 'CreateCubicVectorTransition', ((1, 'duration'),(1, 'finalValue'),(1, 'finalVelocity'),(1, 'cDimension'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateSmoothStopTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(18, 'CreateSmoothStopTransition', ((1, 'maximumDuration'),(1, 'finalValue'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateParabolicTransitionFromAcceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(19, 'CreateParabolicTransitionFromAcceleration', ((1, 'finalValue'),(1, 'finalVelocity'),(1, 'acceleration'),(1, 'transition'),)))
    IUIAnimationTransitionLibrary2.CreateCubicBezierLinearTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,Double,Double,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(20, 'CreateCubicBezierLinearTransition', ((1, 'duration'),(1, 'finalValue'),(1, 'x1'),(1, 'y1'),(1, 'x2'),(1, 'y2'),(1, 'ppTransition'),)))
    IUIAnimationTransitionLibrary2.CreateCubicBezierLinearVectorTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Double),UInt32,Double,Double,Double,Double,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(21, 'CreateCubicBezierLinearVectorTransition', ((1, 'duration'),(1, 'finalValue'),(1, 'cDimension'),(1, 'x1'),(1, 'y1'),(1, 'x2'),(1, 'y2'),(1, 'ppTransition'),)))
    return IUIAnimationTransitionLibrary2
def _define_IUIAnimationPrimitiveInterpolation_head():
    class IUIAnimationPrimitiveInterpolation(win32more.System.Com.IUnknown_head):
        Guid = Guid('bab20d63-4361-45da-a24f-ab8508846b5b')
    return IUIAnimationPrimitiveInterpolation
def _define_IUIAnimationPrimitiveInterpolation():
    IUIAnimationPrimitiveInterpolation = win32more.UI.Animation.IUIAnimationPrimitiveInterpolation_head
    IUIAnimationPrimitiveInterpolation.AddCubic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Double,Single,Single,Single,Single, use_last_error=False)(3, 'AddCubic', ((1, 'dimension'),(1, 'beginOffset'),(1, 'constantCoefficient'),(1, 'linearCoefficient'),(1, 'quadraticCoefficient'),(1, 'cubicCoefficient'),)))
    IUIAnimationPrimitiveInterpolation.AddSinusoidal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Double,Single,Single,Single,Single, use_last_error=False)(4, 'AddSinusoidal', ((1, 'dimension'),(1, 'beginOffset'),(1, 'bias'),(1, 'amplitude'),(1, 'frequency'),(1, 'phase'),)))
    return IUIAnimationPrimitiveInterpolation
def _define_IUIAnimationInterpolator2_head():
    class IUIAnimationInterpolator2(win32more.System.Com.IUnknown_head):
        Guid = Guid('ea76aff8-ea22-4a23-a0ef-a6a966703518')
    return IUIAnimationInterpolator2
def _define_IUIAnimationInterpolator2():
    IUIAnimationInterpolator2 = win32more.UI.Animation.IUIAnimationInterpolator2_head
    IUIAnimationInterpolator2.GetDimension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetDimension', ((1, 'dimension'),)))
    IUIAnimationInterpolator2.SetInitialValueAndVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),POINTER(Double),UInt32, use_last_error=False)(4, 'SetInitialValueAndVelocity', ((1, 'initialValue'),(1, 'initialVelocity'),(1, 'cDimension'),)))
    IUIAnimationInterpolator2.SetDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(5, 'SetDuration', ((1, 'duration'),)))
    IUIAnimationInterpolator2.GetDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(6, 'GetDuration', ((1, 'duration'),)))
    IUIAnimationInterpolator2.GetFinalValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32, use_last_error=False)(7, 'GetFinalValue', ((1, 'value'),(1, 'cDimension'),)))
    IUIAnimationInterpolator2.InterpolateValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Double),UInt32, use_last_error=False)(8, 'InterpolateValue', ((1, 'offset'),(1, 'value'),(1, 'cDimension'),)))
    IUIAnimationInterpolator2.InterpolateVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Double),UInt32, use_last_error=False)(9, 'InterpolateVelocity', ((1, 'offset'),(1, 'velocity'),(1, 'cDimension'),)))
    IUIAnimationInterpolator2.GetPrimitiveInterpolation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationPrimitiveInterpolation_head,UInt32, use_last_error=False)(10, 'GetPrimitiveInterpolation', ((1, 'interpolation'),(1, 'cDimension'),)))
    IUIAnimationInterpolator2.GetDependencies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Animation.UI_ANIMATION_DEPENDENCIES),POINTER(win32more.UI.Animation.UI_ANIMATION_DEPENDENCIES),POINTER(win32more.UI.Animation.UI_ANIMATION_DEPENDENCIES), use_last_error=False)(11, 'GetDependencies', ((1, 'initialValueDependencies'),(1, 'initialVelocityDependencies'),(1, 'durationDependencies'),)))
    return IUIAnimationInterpolator2
def _define_IUIAnimationTransitionFactory2_head():
    class IUIAnimationTransitionFactory2(win32more.System.Com.IUnknown_head):
        Guid = Guid('937d4916-c1a6-42d5-88d8-30344d6efe31')
    return IUIAnimationTransitionFactory2
def _define_IUIAnimationTransitionFactory2():
    IUIAnimationTransitionFactory2 = win32more.UI.Animation.IUIAnimationTransitionFactory2_head
    IUIAnimationTransitionFactory2.CreateTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationInterpolator2_head,POINTER(win32more.UI.Animation.IUIAnimationTransition2_head), use_last_error=False)(3, 'CreateTransition', ((1, 'interpolator'),(1, 'transition'),)))
    return IUIAnimationTransitionFactory2
def _define_IUIAnimationStoryboard2_head():
    class IUIAnimationStoryboard2(win32more.System.Com.IUnknown_head):
        Guid = Guid('ae289cd2-12d4-4945-9419-9e41be034df2')
    return IUIAnimationStoryboard2
def _define_IUIAnimationStoryboard2():
    IUIAnimationStoryboard2 = win32more.UI.Animation.IUIAnimationStoryboard2_head
    IUIAnimationStoryboard2.AddTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariable2_head,win32more.UI.Animation.IUIAnimationTransition2_head, use_last_error=False)(3, 'AddTransition', ((1, 'variable'),(1, 'transition'),)))
    IUIAnimationStoryboard2.AddKeyframeAtOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.UI_ANIMATION_KEYFRAME,Double,POINTER(win32more.UI.Animation.UI_ANIMATION_KEYFRAME), use_last_error=False)(4, 'AddKeyframeAtOffset', ((1, 'existingKeyframe'),(1, 'offset'),(1, 'keyframe'),)))
    IUIAnimationStoryboard2.AddKeyframeAfterTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationTransition2_head,POINTER(win32more.UI.Animation.UI_ANIMATION_KEYFRAME), use_last_error=False)(5, 'AddKeyframeAfterTransition', ((1, 'transition'),(1, 'keyframe'),)))
    IUIAnimationStoryboard2.AddTransitionAtKeyframe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariable2_head,win32more.UI.Animation.IUIAnimationTransition2_head,win32more.UI.Animation.UI_ANIMATION_KEYFRAME, use_last_error=False)(6, 'AddTransitionAtKeyframe', ((1, 'variable'),(1, 'transition'),(1, 'startKeyframe'),)))
    IUIAnimationStoryboard2.AddTransitionBetweenKeyframes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariable2_head,win32more.UI.Animation.IUIAnimationTransition2_head,win32more.UI.Animation.UI_ANIMATION_KEYFRAME,win32more.UI.Animation.UI_ANIMATION_KEYFRAME, use_last_error=False)(7, 'AddTransitionBetweenKeyframes', ((1, 'variable'),(1, 'transition'),(1, 'startKeyframe'),(1, 'endKeyframe'),)))
    IUIAnimationStoryboard2.RepeatBetweenKeyframes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.UI_ANIMATION_KEYFRAME,win32more.UI.Animation.UI_ANIMATION_KEYFRAME,Double,win32more.UI.Animation.UI_ANIMATION_REPEAT_MODE,win32more.UI.Animation.IUIAnimationLoopIterationChangeHandler2_head,UIntPtr,win32more.Foundation.BOOL, use_last_error=False)(8, 'RepeatBetweenKeyframes', ((1, 'startKeyframe'),(1, 'endKeyframe'),(1, 'cRepetition'),(1, 'repeatMode'),(1, 'pIterationChangeHandler'),(1, 'id'),(1, 'fRegisterForNextAnimationEvent'),)))
    IUIAnimationStoryboard2.HoldVariable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationVariable2_head, use_last_error=False)(9, 'HoldVariable', ((1, 'variable'),)))
    IUIAnimationStoryboard2.SetLongestAcceptableDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(10, 'SetLongestAcceptableDelay', ((1, 'delay'),)))
    IUIAnimationStoryboard2.SetSkipDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(11, 'SetSkipDuration', ((1, 'secondsDuration'),)))
    IUIAnimationStoryboard2.Schedule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.UI.Animation.UI_ANIMATION_SCHEDULING_RESULT), use_last_error=False)(12, 'Schedule', ((1, 'timeNow'),(1, 'schedulingResult'),)))
    IUIAnimationStoryboard2.Conclude = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'Conclude', ()))
    IUIAnimationStoryboard2.Finish = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(14, 'Finish', ((1, 'completionDeadline'),)))
    IUIAnimationStoryboard2.Abandon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'Abandon', ()))
    IUIAnimationStoryboard2.SetTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32, use_last_error=False)(16, 'SetTag', ((1, 'object'),(1, 'id'),)))
    IUIAnimationStoryboard2.GetTag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head),POINTER(UInt32), use_last_error=False)(17, 'GetTag', ((1, 'object'),(1, 'id'),)))
    IUIAnimationStoryboard2.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Animation.UI_ANIMATION_STORYBOARD_STATUS), use_last_error=False)(18, 'GetStatus', ((1, 'status'),)))
    IUIAnimationStoryboard2.GetElapsedTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(19, 'GetElapsedTime', ((1, 'elapsedTime'),)))
    IUIAnimationStoryboard2.SetStoryboardEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Animation.IUIAnimationStoryboardEventHandler2_head,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(20, 'SetStoryboardEventHandler', ((1, 'handler'),(1, 'fRegisterStatusChangeForNextAnimationEvent'),(1, 'fRegisterUpdateForNextAnimationEvent'),)))
    return IUIAnimationStoryboard2
__all__ = [
    "UI_ANIMATION_SECONDS_EVENTUALLY",
    "UI_ANIMATION_REPEAT_INDEFINITELY",
    "UI_ANIMATION_REPEAT_INDEFINITELY_CONCLUDE_AT_END",
    "UI_ANIMATION_REPEAT_INDEFINITELY_CONCLUDE_AT_START",
    "UI_ANIMATION_SECONDS_INFINITE",
    "UI_ANIMATION_KEYFRAME",
    "UIAnimationManager",
    "UIAnimationManager2",
    "UIAnimationTransitionLibrary",
    "UIAnimationTransitionLibrary2",
    "UIAnimationTransitionFactory",
    "UIAnimationTransitionFactory2",
    "UIAnimationTimer",
    "UI_ANIMATION_UPDATE_RESULT",
    "UI_ANIMATION_UPDATE_NO_CHANGE",
    "UI_ANIMATION_UPDATE_VARIABLES_CHANGED",
    "UI_ANIMATION_MANAGER_STATUS",
    "UI_ANIMATION_MANAGER_IDLE",
    "UI_ANIMATION_MANAGER_BUSY",
    "UI_ANIMATION_MODE",
    "UI_ANIMATION_MODE_DISABLED",
    "UI_ANIMATION_MODE_SYSTEM_DEFAULT",
    "UI_ANIMATION_MODE_ENABLED",
    "UI_ANIMATION_REPEAT_MODE",
    "UI_ANIMATION_REPEAT_MODE_NORMAL",
    "UI_ANIMATION_REPEAT_MODE_ALTERNATE",
    "IUIAnimationManager",
    "UI_ANIMATION_ROUNDING_MODE",
    "UI_ANIMATION_ROUNDING_NEAREST",
    "UI_ANIMATION_ROUNDING_FLOOR",
    "UI_ANIMATION_ROUNDING_CEILING",
    "IUIAnimationVariable",
    "UI_ANIMATION_STORYBOARD_STATUS",
    "UI_ANIMATION_STORYBOARD_BUILDING",
    "UI_ANIMATION_STORYBOARD_SCHEDULED",
    "UI_ANIMATION_STORYBOARD_CANCELLED",
    "UI_ANIMATION_STORYBOARD_PLAYING",
    "UI_ANIMATION_STORYBOARD_TRUNCATED",
    "UI_ANIMATION_STORYBOARD_FINISHED",
    "UI_ANIMATION_STORYBOARD_READY",
    "UI_ANIMATION_STORYBOARD_INSUFFICIENT_PRIORITY",
    "UI_ANIMATION_SCHEDULING_RESULT",
    "UI_ANIMATION_SCHEDULING_UNEXPECTED_FAILURE",
    "UI_ANIMATION_SCHEDULING_INSUFFICIENT_PRIORITY",
    "UI_ANIMATION_SCHEDULING_ALREADY_SCHEDULED",
    "UI_ANIMATION_SCHEDULING_SUCCEEDED",
    "UI_ANIMATION_SCHEDULING_DEFERRED",
    "IUIAnimationStoryboard",
    "IUIAnimationTransition",
    "IUIAnimationManagerEventHandler",
    "IUIAnimationVariableChangeHandler",
    "IUIAnimationVariableIntegerChangeHandler",
    "IUIAnimationStoryboardEventHandler",
    "UI_ANIMATION_PRIORITY_EFFECT",
    "UI_ANIMATION_PRIORITY_EFFECT_FAILURE",
    "UI_ANIMATION_PRIORITY_EFFECT_DELAY",
    "IUIAnimationPriorityComparison",
    "UI_ANIMATION_SLOPE",
    "UI_ANIMATION_SLOPE_INCREASING",
    "UI_ANIMATION_SLOPE_DECREASING",
    "IUIAnimationTransitionLibrary",
    "UI_ANIMATION_DEPENDENCIES",
    "UI_ANIMATION_DEPENDENCY_NONE",
    "UI_ANIMATION_DEPENDENCY_INTERMEDIATE_VALUES",
    "UI_ANIMATION_DEPENDENCY_FINAL_VALUE",
    "UI_ANIMATION_DEPENDENCY_FINAL_VELOCITY",
    "UI_ANIMATION_DEPENDENCY_DURATION",
    "IUIAnimationInterpolator",
    "IUIAnimationTransitionFactory",
    "UI_ANIMATION_IDLE_BEHAVIOR",
    "UI_ANIMATION_IDLE_BEHAVIOR_CONTINUE",
    "UI_ANIMATION_IDLE_BEHAVIOR_DISABLE",
    "IUIAnimationTimer",
    "IUIAnimationTimerUpdateHandler",
    "UI_ANIMATION_TIMER_CLIENT_STATUS",
    "UI_ANIMATION_TIMER_CLIENT_IDLE",
    "UI_ANIMATION_TIMER_CLIENT_BUSY",
    "IUIAnimationTimerClientEventHandler",
    "IUIAnimationTimerEventHandler",
    "IUIAnimationManager2",
    "IUIAnimationVariable2",
    "IUIAnimationTransition2",
    "IUIAnimationManagerEventHandler2",
    "IUIAnimationVariableChangeHandler2",
    "IUIAnimationVariableIntegerChangeHandler2",
    "IUIAnimationVariableCurveChangeHandler2",
    "IUIAnimationStoryboardEventHandler2",
    "IUIAnimationLoopIterationChangeHandler2",
    "IUIAnimationPriorityComparison2",
    "IUIAnimationTransitionLibrary2",
    "IUIAnimationPrimitiveInterpolation",
    "IUIAnimationInterpolator2",
    "IUIAnimationTransitionFactory2",
    "IUIAnimationStoryboard2",
]
