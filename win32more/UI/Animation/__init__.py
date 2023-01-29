from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.DirectComposition
import win32more.System.Com
import win32more.UI.Animation
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
UI_ANIMATION_SECONDS_EVENTUALLY: Int32 = -1
UI_ANIMATION_REPEAT_INDEFINITELY: Int32 = -1
UI_ANIMATION_REPEAT_INDEFINITELY_CONCLUDE_AT_END: Int32 = -1
UI_ANIMATION_REPEAT_INDEFINITELY_CONCLUDE_AT_START: Int32 = -2
UI_ANIMATION_SECONDS_INFINITE: Int32 = -1
class IUIAnimationInterpolator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7815cbba-ddf7-478c-a4-6c-7b-6c-73-8b-79-78')
    @commethod(3)
    def SetInitialValueAndVelocity(initialValue: Double, initialVelocity: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetDuration(duration: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDuration(duration: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetFinalValue(value: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def InterpolateValue(offset: Double, value: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def InterpolateVelocity(offset: Double, velocity: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDependencies(initialValueDependencies: POINTER(win32more.UI.Animation.UI_ANIMATION_DEPENDENCIES), initialVelocityDependencies: POINTER(win32more.UI.Animation.UI_ANIMATION_DEPENDENCIES), durationDependencies: POINTER(win32more.UI.Animation.UI_ANIMATION_DEPENDENCIES)) -> win32more.Foundation.HRESULT: ...
class IUIAnimationInterpolator2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ea76aff8-ea22-4a23-a0-ef-a6-a9-66-70-35-18')
    @commethod(3)
    def GetDimension(dimension: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetInitialValueAndVelocity(initialValue: POINTER(Double), initialVelocity: POINTER(Double), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetDuration(duration: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDuration(duration: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetFinalValue(value: POINTER(Double), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def InterpolateValue(offset: Double, value: POINTER(Double), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def InterpolateVelocity(offset: Double, velocity: POINTER(Double), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetPrimitiveInterpolation(interpolation: win32more.UI.Animation.IUIAnimationPrimitiveInterpolation_head, cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetDependencies(initialValueDependencies: POINTER(win32more.UI.Animation.UI_ANIMATION_DEPENDENCIES), initialVelocityDependencies: POINTER(win32more.UI.Animation.UI_ANIMATION_DEPENDENCIES), durationDependencies: POINTER(win32more.UI.Animation.UI_ANIMATION_DEPENDENCIES)) -> win32more.Foundation.HRESULT: ...
class IUIAnimationLoopIterationChangeHandler2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2d3b15a4-4762-47ab-a0-30-b2-32-21-df-3a-e0')
    @commethod(3)
    def OnLoopIterationChanged(storyboard: win32more.UI.Animation.IUIAnimationStoryboard2_head, id: UIntPtr, newIterationCount: UInt32, oldIterationCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IUIAnimationManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9169896c-ac8d-4e7d-94-e5-67-fa-4d-c2-f2-e8')
    @commethod(3)
    def CreateAnimationVariable(initialValue: Double, variable: POINTER(win32more.UI.Animation.IUIAnimationVariable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ScheduleTransition(variable: win32more.UI.Animation.IUIAnimationVariable_head, transition: win32more.UI.Animation.IUIAnimationTransition_head, timeNow: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateStoryboard(storyboard: POINTER(win32more.UI.Animation.IUIAnimationStoryboard_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def FinishAllStoryboards(completionDeadline: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def AbandonAllStoryboards() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Update(timeNow: Double, updateResult: POINTER(win32more.UI.Animation.UI_ANIMATION_UPDATE_RESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetVariableFromTag(object: win32more.System.Com.IUnknown_head, id: UInt32, variable: POINTER(win32more.UI.Animation.IUIAnimationVariable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetStoryboardFromTag(object: win32more.System.Com.IUnknown_head, id: UInt32, storyboard: POINTER(win32more.UI.Animation.IUIAnimationStoryboard_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetStatus(status: POINTER(win32more.UI.Animation.UI_ANIMATION_MANAGER_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetAnimationMode(mode: win32more.UI.Animation.UI_ANIMATION_MODE) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Pause() -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Resume() -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetManagerEventHandler(handler: win32more.UI.Animation.IUIAnimationManagerEventHandler_head) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetCancelPriorityComparison(comparison: win32more.UI.Animation.IUIAnimationPriorityComparison_head) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetTrimPriorityComparison(comparison: win32more.UI.Animation.IUIAnimationPriorityComparison_head) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetCompressPriorityComparison(comparison: win32more.UI.Animation.IUIAnimationPriorityComparison_head) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetConcludePriorityComparison(comparison: win32more.UI.Animation.IUIAnimationPriorityComparison_head) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetDefaultLongestAcceptableDelay(delay: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def Shutdown() -> win32more.Foundation.HRESULT: ...
class IUIAnimationManager2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d8b6f7d4-4109-4d3f-ac-ee-87-99-26-96-8c-b1')
    @commethod(3)
    def CreateAnimationVectorVariable(initialValue: POINTER(Double), cDimension: UInt32, variable: POINTER(win32more.UI.Animation.IUIAnimationVariable2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateAnimationVariable(initialValue: Double, variable: POINTER(win32more.UI.Animation.IUIAnimationVariable2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ScheduleTransition(variable: win32more.UI.Animation.IUIAnimationVariable2_head, transition: win32more.UI.Animation.IUIAnimationTransition2_head, timeNow: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CreateStoryboard(storyboard: POINTER(win32more.UI.Animation.IUIAnimationStoryboard2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def FinishAllStoryboards(completionDeadline: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def AbandonAllStoryboards() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Update(timeNow: Double, updateResult: POINTER(win32more.UI.Animation.UI_ANIMATION_UPDATE_RESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetVariableFromTag(object: win32more.System.Com.IUnknown_head, id: UInt32, variable: POINTER(win32more.UI.Animation.IUIAnimationVariable2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetStoryboardFromTag(object: win32more.System.Com.IUnknown_head, id: UInt32, storyboard: POINTER(win32more.UI.Animation.IUIAnimationStoryboard2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def EstimateNextEventTime(seconds: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetStatus(status: POINTER(win32more.UI.Animation.UI_ANIMATION_MANAGER_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetAnimationMode(mode: win32more.UI.Animation.UI_ANIMATION_MODE) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Pause() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Resume() -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetManagerEventHandler(handler: win32more.UI.Animation.IUIAnimationManagerEventHandler2_head, fRegisterForNextAnimationEvent: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetCancelPriorityComparison(comparison: win32more.UI.Animation.IUIAnimationPriorityComparison2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetTrimPriorityComparison(comparison: win32more.UI.Animation.IUIAnimationPriorityComparison2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetCompressPriorityComparison(comparison: win32more.UI.Animation.IUIAnimationPriorityComparison2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetConcludePriorityComparison(comparison: win32more.UI.Animation.IUIAnimationPriorityComparison2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SetDefaultLongestAcceptableDelay(delay: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def Shutdown() -> win32more.Foundation.HRESULT: ...
class IUIAnimationManagerEventHandler(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('783321ed-78a3-4366-b5-74-6a-f6-07-a6-47-88')
    @commethod(3)
    def OnManagerStatusChanged(newStatus: win32more.UI.Animation.UI_ANIMATION_MANAGER_STATUS, previousStatus: win32more.UI.Animation.UI_ANIMATION_MANAGER_STATUS) -> win32more.Foundation.HRESULT: ...
class IUIAnimationManagerEventHandler2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f6e022ba-bff3-42ec-90-33-e0-73-f3-3e-83-c3')
    @commethod(3)
    def OnManagerStatusChanged(newStatus: win32more.UI.Animation.UI_ANIMATION_MANAGER_STATUS, previousStatus: win32more.UI.Animation.UI_ANIMATION_MANAGER_STATUS) -> win32more.Foundation.HRESULT: ...
class IUIAnimationPrimitiveInterpolation(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bab20d63-4361-45da-a2-4f-ab-85-08-84-6b-5b')
    @commethod(3)
    def AddCubic(dimension: UInt32, beginOffset: Double, constantCoefficient: Single, linearCoefficient: Single, quadraticCoefficient: Single, cubicCoefficient: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AddSinusoidal(dimension: UInt32, beginOffset: Double, bias: Single, amplitude: Single, frequency: Single, phase: Single) -> win32more.Foundation.HRESULT: ...
class IUIAnimationPriorityComparison(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('83fa9b74-5f86-4618-bc-6a-a2-fa-c1-9b-3f-44')
    @commethod(3)
    def HasPriority(scheduledStoryboard: win32more.UI.Animation.IUIAnimationStoryboard_head, newStoryboard: win32more.UI.Animation.IUIAnimationStoryboard_head, priorityEffect: win32more.UI.Animation.UI_ANIMATION_PRIORITY_EFFECT) -> win32more.Foundation.HRESULT: ...
class IUIAnimationPriorityComparison2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5b6d7a37-4621-467c-8b-05-70-13-1d-e6-2d-db')
    @commethod(3)
    def HasPriority(scheduledStoryboard: win32more.UI.Animation.IUIAnimationStoryboard2_head, newStoryboard: win32more.UI.Animation.IUIAnimationStoryboard2_head, priorityEffect: win32more.UI.Animation.UI_ANIMATION_PRIORITY_EFFECT) -> win32more.Foundation.HRESULT: ...
class IUIAnimationStoryboard(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a8ff128f-9bf9-4af1-9e-67-e5-e4-10-de-fb-84')
    @commethod(3)
    def AddTransition(variable: win32more.UI.Animation.IUIAnimationVariable_head, transition: win32more.UI.Animation.IUIAnimationTransition_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AddKeyframeAtOffset(existingKeyframe: win32more.UI.Animation.UI_ANIMATION_KEYFRAME, offset: Double, keyframe: POINTER(win32more.UI.Animation.UI_ANIMATION_KEYFRAME)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddKeyframeAfterTransition(transition: win32more.UI.Animation.IUIAnimationTransition_head, keyframe: POINTER(win32more.UI.Animation.UI_ANIMATION_KEYFRAME)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def AddTransitionAtKeyframe(variable: win32more.UI.Animation.IUIAnimationVariable_head, transition: win32more.UI.Animation.IUIAnimationTransition_head, startKeyframe: win32more.UI.Animation.UI_ANIMATION_KEYFRAME) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def AddTransitionBetweenKeyframes(variable: win32more.UI.Animation.IUIAnimationVariable_head, transition: win32more.UI.Animation.IUIAnimationTransition_head, startKeyframe: win32more.UI.Animation.UI_ANIMATION_KEYFRAME, endKeyframe: win32more.UI.Animation.UI_ANIMATION_KEYFRAME) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RepeatBetweenKeyframes(startKeyframe: win32more.UI.Animation.UI_ANIMATION_KEYFRAME, endKeyframe: win32more.UI.Animation.UI_ANIMATION_KEYFRAME, repetitionCount: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def HoldVariable(variable: win32more.UI.Animation.IUIAnimationVariable_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetLongestAcceptableDelay(delay: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Schedule(timeNow: Double, schedulingResult: POINTER(win32more.UI.Animation.UI_ANIMATION_SCHEDULING_RESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Conclude() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Finish(completionDeadline: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Abandon() -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetTag(object: win32more.System.Com.IUnknown_head, id: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetTag(object: POINTER(win32more.System.Com.IUnknown_head), id: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetStatus(status: POINTER(win32more.UI.Animation.UI_ANIMATION_STORYBOARD_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetElapsedTime(elapsedTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetStoryboardEventHandler(handler: win32more.UI.Animation.IUIAnimationStoryboardEventHandler_head) -> win32more.Foundation.HRESULT: ...
class IUIAnimationStoryboard2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ae289cd2-12d4-4945-94-19-9e-41-be-03-4d-f2')
    @commethod(3)
    def AddTransition(variable: win32more.UI.Animation.IUIAnimationVariable2_head, transition: win32more.UI.Animation.IUIAnimationTransition2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AddKeyframeAtOffset(existingKeyframe: win32more.UI.Animation.UI_ANIMATION_KEYFRAME, offset: Double, keyframe: POINTER(win32more.UI.Animation.UI_ANIMATION_KEYFRAME)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddKeyframeAfterTransition(transition: win32more.UI.Animation.IUIAnimationTransition2_head, keyframe: POINTER(win32more.UI.Animation.UI_ANIMATION_KEYFRAME)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def AddTransitionAtKeyframe(variable: win32more.UI.Animation.IUIAnimationVariable2_head, transition: win32more.UI.Animation.IUIAnimationTransition2_head, startKeyframe: win32more.UI.Animation.UI_ANIMATION_KEYFRAME) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def AddTransitionBetweenKeyframes(variable: win32more.UI.Animation.IUIAnimationVariable2_head, transition: win32more.UI.Animation.IUIAnimationTransition2_head, startKeyframe: win32more.UI.Animation.UI_ANIMATION_KEYFRAME, endKeyframe: win32more.UI.Animation.UI_ANIMATION_KEYFRAME) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RepeatBetweenKeyframes(startKeyframe: win32more.UI.Animation.UI_ANIMATION_KEYFRAME, endKeyframe: win32more.UI.Animation.UI_ANIMATION_KEYFRAME, cRepetition: Double, repeatMode: win32more.UI.Animation.UI_ANIMATION_REPEAT_MODE, pIterationChangeHandler: win32more.UI.Animation.IUIAnimationLoopIterationChangeHandler2_head, id: UIntPtr, fRegisterForNextAnimationEvent: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def HoldVariable(variable: win32more.UI.Animation.IUIAnimationVariable2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetLongestAcceptableDelay(delay: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetSkipDuration(secondsDuration: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Schedule(timeNow: Double, schedulingResult: POINTER(win32more.UI.Animation.UI_ANIMATION_SCHEDULING_RESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Conclude() -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Finish(completionDeadline: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Abandon() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetTag(object: win32more.System.Com.IUnknown_head, id: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetTag(object: POINTER(win32more.System.Com.IUnknown_head), id: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetStatus(status: POINTER(win32more.UI.Animation.UI_ANIMATION_STORYBOARD_STATUS)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetElapsedTime(elapsedTime: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetStoryboardEventHandler(handler: win32more.UI.Animation.IUIAnimationStoryboardEventHandler2_head, fRegisterStatusChangeForNextAnimationEvent: win32more.Foundation.BOOL, fRegisterUpdateForNextAnimationEvent: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IUIAnimationStoryboardEventHandler(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3d5c9008-ec7c-4364-9f-8a-9a-f3-c5-8c-ba-e6')
    @commethod(3)
    def OnStoryboardStatusChanged(storyboard: win32more.UI.Animation.IUIAnimationStoryboard_head, newStatus: win32more.UI.Animation.UI_ANIMATION_STORYBOARD_STATUS, previousStatus: win32more.UI.Animation.UI_ANIMATION_STORYBOARD_STATUS) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnStoryboardUpdated(storyboard: win32more.UI.Animation.IUIAnimationStoryboard_head) -> win32more.Foundation.HRESULT: ...
class IUIAnimationStoryboardEventHandler2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bac5f55a-ba7c-414c-b5-99-fb-f8-50-f5-53-c6')
    @commethod(3)
    def OnStoryboardStatusChanged(storyboard: win32more.UI.Animation.IUIAnimationStoryboard2_head, newStatus: win32more.UI.Animation.UI_ANIMATION_STORYBOARD_STATUS, previousStatus: win32more.UI.Animation.UI_ANIMATION_STORYBOARD_STATUS) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnStoryboardUpdated(storyboard: win32more.UI.Animation.IUIAnimationStoryboard2_head) -> win32more.Foundation.HRESULT: ...
class IUIAnimationTimer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6b0efad1-a053-41d6-90-85-33-a6-89-14-46-65')
    @commethod(3)
    def SetTimerUpdateHandler(updateHandler: win32more.UI.Animation.IUIAnimationTimerUpdateHandler_head, idleBehavior: win32more.UI.Animation.UI_ANIMATION_IDLE_BEHAVIOR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetTimerEventHandler(handler: win32more.UI.Animation.IUIAnimationTimerEventHandler_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Enable() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Disable() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def IsEnabled() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTime(seconds: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetFrameRateThreshold(framesPerSecond: UInt32) -> win32more.Foundation.HRESULT: ...
class IUIAnimationTimerClientEventHandler(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bedb4db6-94fa-4bfb-a4-7f-ef-2d-9e-40-8c-25')
    @commethod(3)
    def OnTimerClientStatusChanged(newStatus: win32more.UI.Animation.UI_ANIMATION_TIMER_CLIENT_STATUS, previousStatus: win32more.UI.Animation.UI_ANIMATION_TIMER_CLIENT_STATUS) -> win32more.Foundation.HRESULT: ...
class IUIAnimationTimerEventHandler(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('274a7dea-d771-4095-ab-bd-8d-f7-ab-d2-3c-e3')
    @commethod(3)
    def OnPreUpdate() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnPostUpdate() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnRenderingTooSlow(framesPerSecond: UInt32) -> win32more.Foundation.HRESULT: ...
class IUIAnimationTimerUpdateHandler(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('195509b7-5d5e-4e3e-b2-78-ee-37-59-b3-67-ad')
    @commethod(3)
    def OnUpdate(timeNow: Double, result: POINTER(win32more.UI.Animation.UI_ANIMATION_UPDATE_RESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetTimerClientEventHandler(handler: win32more.UI.Animation.IUIAnimationTimerClientEventHandler_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ClearTimerClientEventHandler() -> win32more.Foundation.HRESULT: ...
class IUIAnimationTransition(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dc6ce252-f731-41cf-b6-10-61-4b-6c-a0-49-ad')
    @commethod(3)
    def SetInitialValue(value: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetInitialVelocity(velocity: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def IsDurationKnown() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDuration(duration: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
class IUIAnimationTransition2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('62ff9123-a85a-4e9b-a2-18-43-5a-93-e2-68-fd')
    @commethod(3)
    def GetDimension(dimension: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetInitialValue(value: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetInitialVectorValue(value: POINTER(Double), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetInitialVelocity(velocity: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetInitialVectorVelocity(velocity: POINTER(Double), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def IsDurationKnown() -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDuration(duration: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
class IUIAnimationTransitionFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fcd91e03-3e3b-45ad-bb-b1-6d-fc-81-53-74-3d')
    @commethod(3)
    def CreateTransition(interpolator: win32more.UI.Animation.IUIAnimationInterpolator_head, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition_head)) -> win32more.Foundation.HRESULT: ...
class IUIAnimationTransitionFactory2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('937d4916-c1a6-42d5-88-d8-30-34-4d-6e-fe-31')
    @commethod(3)
    def CreateTransition(interpolator: win32more.UI.Animation.IUIAnimationInterpolator2_head, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
class IUIAnimationTransitionLibrary(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ca5a14b1-d24f-48b8-8f-e4-c7-81-69-ba-95-4e')
    @commethod(3)
    def CreateInstantaneousTransition(finalValue: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateConstantTransition(duration: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateDiscreteTransition(delay: Double, finalValue: Double, hold: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CreateLinearTransition(duration: Double, finalValue: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CreateLinearTransitionFromSpeed(speed: Double, finalValue: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CreateSinusoidalTransitionFromVelocity(duration: Double, period: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CreateSinusoidalTransitionFromRange(duration: Double, minimumValue: Double, maximumValue: Double, period: Double, slope: win32more.UI.Animation.UI_ANIMATION_SLOPE, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CreateAccelerateDecelerateTransition(duration: Double, finalValue: Double, accelerationRatio: Double, decelerationRatio: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CreateReversalTransition(duration: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def CreateCubicTransition(duration: Double, finalValue: Double, finalVelocity: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def CreateSmoothStopTransition(maximumDuration: Double, finalValue: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def CreateParabolicTransitionFromAcceleration(finalValue: Double, finalVelocity: Double, acceleration: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition_head)) -> win32more.Foundation.HRESULT: ...
class IUIAnimationTransitionLibrary2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('03cfae53-9580-4ee3-b3-63-2e-ce-51-b4-af-6a')
    @commethod(3)
    def CreateInstantaneousTransition(finalValue: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateInstantaneousVectorTransition(finalValue: POINTER(Double), cDimension: UInt32, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateConstantTransition(duration: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CreateDiscreteTransition(delay: Double, finalValue: Double, hold: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CreateDiscreteVectorTransition(delay: Double, finalValue: POINTER(Double), cDimension: UInt32, hold: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def CreateLinearTransition(duration: Double, finalValue: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CreateLinearVectorTransition(duration: Double, finalValue: POINTER(Double), cDimension: UInt32, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def CreateLinearTransitionFromSpeed(speed: Double, finalValue: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CreateLinearVectorTransitionFromSpeed(speed: Double, finalValue: POINTER(Double), cDimension: UInt32, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def CreateSinusoidalTransitionFromVelocity(duration: Double, period: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def CreateSinusoidalTransitionFromRange(duration: Double, minimumValue: Double, maximumValue: Double, period: Double, slope: win32more.UI.Animation.UI_ANIMATION_SLOPE, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def CreateAccelerateDecelerateTransition(duration: Double, finalValue: Double, accelerationRatio: Double, decelerationRatio: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def CreateReversalTransition(duration: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def CreateCubicTransition(duration: Double, finalValue: Double, finalVelocity: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def CreateCubicVectorTransition(duration: Double, finalValue: POINTER(Double), finalVelocity: POINTER(Double), cDimension: UInt32, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def CreateSmoothStopTransition(maximumDuration: Double, finalValue: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def CreateParabolicTransitionFromAcceleration(finalValue: Double, finalVelocity: Double, acceleration: Double, transition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def CreateCubicBezierLinearTransition(duration: Double, finalValue: Double, x1: Double, y1: Double, x2: Double, y2: Double, ppTransition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def CreateCubicBezierLinearVectorTransition(duration: Double, finalValue: POINTER(Double), cDimension: UInt32, x1: Double, y1: Double, x2: Double, y2: Double, ppTransition: POINTER(win32more.UI.Animation.IUIAnimationTransition2_head)) -> win32more.Foundation.HRESULT: ...
class IUIAnimationVariable(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8ceeb155-2849-4ce5-94-48-91-ff-70-e1-e4-d9')
    @commethod(3)
    def GetValue(value: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetFinalValue(finalValue: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetPreviousValue(previousValue: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetIntegerValue(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetFinalIntegerValue(finalValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetPreviousIntegerValue(previousValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentStoryboard(storyboard: POINTER(win32more.UI.Animation.IUIAnimationStoryboard_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetLowerBound(bound: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetUpperBound(bound: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetRoundingMode(mode: win32more.UI.Animation.UI_ANIMATION_ROUNDING_MODE) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetTag(object: win32more.System.Com.IUnknown_head, id: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetTag(object: POINTER(win32more.System.Com.IUnknown_head), id: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetVariableChangeHandler(handler: win32more.UI.Animation.IUIAnimationVariableChangeHandler_head) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetVariableIntegerChangeHandler(handler: win32more.UI.Animation.IUIAnimationVariableIntegerChangeHandler_head) -> win32more.Foundation.HRESULT: ...
class IUIAnimationVariable2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4914b304-96ab-44d9-9e-77-d5-10-9b-7e-74-66')
    @commethod(3)
    def GetDimension(dimension: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(value: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetVectorValue(value: POINTER(Double), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurve(animation: win32more.Graphics.DirectComposition.IDCompositionAnimation_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetVectorCurve(animation: POINTER(win32more.Graphics.DirectComposition.IDCompositionAnimation_head), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetFinalValue(finalValue: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetFinalVectorValue(finalValue: POINTER(Double), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetPreviousValue(previousValue: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetPreviousVectorValue(previousValue: POINTER(Double), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetIntegerValue(value: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetIntegerVectorValue(value: POINTER(Int32), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetFinalIntegerValue(finalValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetFinalIntegerVectorValue(finalValue: POINTER(Int32), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetPreviousIntegerValue(previousValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetPreviousIntegerVectorValue(previousValue: POINTER(Int32), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetCurrentStoryboard(storyboard: POINTER(win32more.UI.Animation.IUIAnimationStoryboard2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetLowerBound(bound: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetLowerBoundVector(bound: POINTER(Double), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetUpperBound(bound: Double) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SetUpperBoundVector(bound: POINTER(Double), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SetRoundingMode(mode: win32more.UI.Animation.UI_ANIMATION_ROUNDING_MODE) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def SetTag(object: win32more.System.Com.IUnknown_head, id: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetTag(object: POINTER(win32more.System.Com.IUnknown_head), id: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def SetVariableChangeHandler(handler: win32more.UI.Animation.IUIAnimationVariableChangeHandler2_head, fRegisterForNextAnimationEvent: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SetVariableIntegerChangeHandler(handler: win32more.UI.Animation.IUIAnimationVariableIntegerChangeHandler2_head, fRegisterForNextAnimationEvent: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def SetVariableCurveChangeHandler(handler: win32more.UI.Animation.IUIAnimationVariableCurveChangeHandler2_head) -> win32more.Foundation.HRESULT: ...
class IUIAnimationVariableChangeHandler(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6358b7ba-87d2-42d5-bf-71-82-e9-19-dd-58-62')
    @commethod(3)
    def OnValueChanged(storyboard: win32more.UI.Animation.IUIAnimationStoryboard_head, variable: win32more.UI.Animation.IUIAnimationVariable_head, newValue: Double, previousValue: Double) -> win32more.Foundation.HRESULT: ...
class IUIAnimationVariableChangeHandler2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('63acc8d2-6eae-4bb0-b8-79-58-6d-d8-cf-be-42')
    @commethod(3)
    def OnValueChanged(storyboard: win32more.UI.Animation.IUIAnimationStoryboard2_head, variable: win32more.UI.Animation.IUIAnimationVariable2_head, newValue: POINTER(Double), previousValue: POINTER(Double), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
class IUIAnimationVariableCurveChangeHandler2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('72895e91-0145-4c21-91-92-5a-ab-40-ed-df-80')
    @commethod(3)
    def OnCurveChanged(variable: win32more.UI.Animation.IUIAnimationVariable2_head) -> win32more.Foundation.HRESULT: ...
class IUIAnimationVariableIntegerChangeHandler(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bb3e1550-356e-44b0-99-da-85-ac-60-17-86-5e')
    @commethod(3)
    def OnIntegerValueChanged(storyboard: win32more.UI.Animation.IUIAnimationStoryboard_head, variable: win32more.UI.Animation.IUIAnimationVariable_head, newValue: Int32, previousValue: Int32) -> win32more.Foundation.HRESULT: ...
class IUIAnimationVariableIntegerChangeHandler2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('829b6cf1-4f3a-4412-ae-09-b2-43-eb-4c-6b-58')
    @commethod(3)
    def OnIntegerValueChanged(storyboard: win32more.UI.Animation.IUIAnimationStoryboard2_head, variable: win32more.UI.Animation.IUIAnimationVariable2_head, newValue: POINTER(Int32), previousValue: POINTER(Int32), cDimension: UInt32) -> win32more.Foundation.HRESULT: ...
UI_ANIMATION_DEPENDENCIES = UInt32
UI_ANIMATION_DEPENDENCY_NONE: UI_ANIMATION_DEPENDENCIES = 0
UI_ANIMATION_DEPENDENCY_INTERMEDIATE_VALUES: UI_ANIMATION_DEPENDENCIES = 1
UI_ANIMATION_DEPENDENCY_FINAL_VALUE: UI_ANIMATION_DEPENDENCIES = 2
UI_ANIMATION_DEPENDENCY_FINAL_VELOCITY: UI_ANIMATION_DEPENDENCIES = 4
UI_ANIMATION_DEPENDENCY_DURATION: UI_ANIMATION_DEPENDENCIES = 8
UI_ANIMATION_IDLE_BEHAVIOR = Int32
UI_ANIMATION_IDLE_BEHAVIOR_CONTINUE: UI_ANIMATION_IDLE_BEHAVIOR = 0
UI_ANIMATION_IDLE_BEHAVIOR_DISABLE: UI_ANIMATION_IDLE_BEHAVIOR = 1
UI_ANIMATION_KEYFRAME = IntPtr
UI_ANIMATION_MANAGER_STATUS = Int32
UI_ANIMATION_MANAGER_IDLE: UI_ANIMATION_MANAGER_STATUS = 0
UI_ANIMATION_MANAGER_BUSY: UI_ANIMATION_MANAGER_STATUS = 1
UI_ANIMATION_MODE = Int32
UI_ANIMATION_MODE_DISABLED: UI_ANIMATION_MODE = 0
UI_ANIMATION_MODE_SYSTEM_DEFAULT: UI_ANIMATION_MODE = 1
UI_ANIMATION_MODE_ENABLED: UI_ANIMATION_MODE = 2
UI_ANIMATION_PRIORITY_EFFECT = Int32
UI_ANIMATION_PRIORITY_EFFECT_FAILURE: UI_ANIMATION_PRIORITY_EFFECT = 0
UI_ANIMATION_PRIORITY_EFFECT_DELAY: UI_ANIMATION_PRIORITY_EFFECT = 1
UI_ANIMATION_REPEAT_MODE = Int32
UI_ANIMATION_REPEAT_MODE_NORMAL: UI_ANIMATION_REPEAT_MODE = 0
UI_ANIMATION_REPEAT_MODE_ALTERNATE: UI_ANIMATION_REPEAT_MODE = 1
UI_ANIMATION_ROUNDING_MODE = Int32
UI_ANIMATION_ROUNDING_NEAREST: UI_ANIMATION_ROUNDING_MODE = 0
UI_ANIMATION_ROUNDING_FLOOR: UI_ANIMATION_ROUNDING_MODE = 1
UI_ANIMATION_ROUNDING_CEILING: UI_ANIMATION_ROUNDING_MODE = 2
UI_ANIMATION_SCHEDULING_RESULT = Int32
UI_ANIMATION_SCHEDULING_UNEXPECTED_FAILURE: UI_ANIMATION_SCHEDULING_RESULT = 0
UI_ANIMATION_SCHEDULING_INSUFFICIENT_PRIORITY: UI_ANIMATION_SCHEDULING_RESULT = 1
UI_ANIMATION_SCHEDULING_ALREADY_SCHEDULED: UI_ANIMATION_SCHEDULING_RESULT = 2
UI_ANIMATION_SCHEDULING_SUCCEEDED: UI_ANIMATION_SCHEDULING_RESULT = 3
UI_ANIMATION_SCHEDULING_DEFERRED: UI_ANIMATION_SCHEDULING_RESULT = 4
UI_ANIMATION_SLOPE = Int32
UI_ANIMATION_SLOPE_INCREASING: UI_ANIMATION_SLOPE = 0
UI_ANIMATION_SLOPE_DECREASING: UI_ANIMATION_SLOPE = 1
UI_ANIMATION_STORYBOARD_STATUS = Int32
UI_ANIMATION_STORYBOARD_BUILDING: UI_ANIMATION_STORYBOARD_STATUS = 0
UI_ANIMATION_STORYBOARD_SCHEDULED: UI_ANIMATION_STORYBOARD_STATUS = 1
UI_ANIMATION_STORYBOARD_CANCELLED: UI_ANIMATION_STORYBOARD_STATUS = 2
UI_ANIMATION_STORYBOARD_PLAYING: UI_ANIMATION_STORYBOARD_STATUS = 3
UI_ANIMATION_STORYBOARD_TRUNCATED: UI_ANIMATION_STORYBOARD_STATUS = 4
UI_ANIMATION_STORYBOARD_FINISHED: UI_ANIMATION_STORYBOARD_STATUS = 5
UI_ANIMATION_STORYBOARD_READY: UI_ANIMATION_STORYBOARD_STATUS = 6
UI_ANIMATION_STORYBOARD_INSUFFICIENT_PRIORITY: UI_ANIMATION_STORYBOARD_STATUS = 7
UI_ANIMATION_TIMER_CLIENT_STATUS = Int32
UI_ANIMATION_TIMER_CLIENT_IDLE: UI_ANIMATION_TIMER_CLIENT_STATUS = 0
UI_ANIMATION_TIMER_CLIENT_BUSY: UI_ANIMATION_TIMER_CLIENT_STATUS = 1
UI_ANIMATION_UPDATE_RESULT = Int32
UI_ANIMATION_UPDATE_NO_CHANGE: UI_ANIMATION_UPDATE_RESULT = 0
UI_ANIMATION_UPDATE_VARIABLES_CHANGED: UI_ANIMATION_UPDATE_RESULT = 1
UIAnimationManager = Guid('4c1fc63a-695c-47e8-a3-39-1a-19-4b-e3-d0-b8')
UIAnimationManager2 = Guid('d25d8842-8884-4a4a-b3-21-09-13-14-37-9b-dd')
UIAnimationTimer = Guid('bfcd4a0c-06b6-4384-b7-68-0d-aa-79-2c-38-0e')
UIAnimationTransitionFactory = Guid('8a9b1cdd-fcd7-419c-8b-44-42-fd-17-db-18-87')
UIAnimationTransitionFactory2 = Guid('84302f97-7f7b-4040-b1-90-72-ac-9d-18-e4-20')
UIAnimationTransitionLibrary = Guid('1d6322ad-aa85-4ef5-a8-28-86-d7-10-67-d1-45')
UIAnimationTransitionLibrary2 = Guid('812f944a-c5c8-4cd9-b0-a6-b3-da-80-2f-22-8d')
make_head(_module, 'IUIAnimationInterpolator')
make_head(_module, 'IUIAnimationInterpolator2')
make_head(_module, 'IUIAnimationLoopIterationChangeHandler2')
make_head(_module, 'IUIAnimationManager')
make_head(_module, 'IUIAnimationManager2')
make_head(_module, 'IUIAnimationManagerEventHandler')
make_head(_module, 'IUIAnimationManagerEventHandler2')
make_head(_module, 'IUIAnimationPrimitiveInterpolation')
make_head(_module, 'IUIAnimationPriorityComparison')
make_head(_module, 'IUIAnimationPriorityComparison2')
make_head(_module, 'IUIAnimationStoryboard')
make_head(_module, 'IUIAnimationStoryboard2')
make_head(_module, 'IUIAnimationStoryboardEventHandler')
make_head(_module, 'IUIAnimationStoryboardEventHandler2')
make_head(_module, 'IUIAnimationTimer')
make_head(_module, 'IUIAnimationTimerClientEventHandler')
make_head(_module, 'IUIAnimationTimerEventHandler')
make_head(_module, 'IUIAnimationTimerUpdateHandler')
make_head(_module, 'IUIAnimationTransition')
make_head(_module, 'IUIAnimationTransition2')
make_head(_module, 'IUIAnimationTransitionFactory')
make_head(_module, 'IUIAnimationTransitionFactory2')
make_head(_module, 'IUIAnimationTransitionLibrary')
make_head(_module, 'IUIAnimationTransitionLibrary2')
make_head(_module, 'IUIAnimationVariable')
make_head(_module, 'IUIAnimationVariable2')
make_head(_module, 'IUIAnimationVariableChangeHandler')
make_head(_module, 'IUIAnimationVariableChangeHandler2')
make_head(_module, 'IUIAnimationVariableCurveChangeHandler2')
make_head(_module, 'IUIAnimationVariableIntegerChangeHandler')
make_head(_module, 'IUIAnimationVariableIntegerChangeHandler2')
__all__ = [
    "IUIAnimationInterpolator",
    "IUIAnimationInterpolator2",
    "IUIAnimationLoopIterationChangeHandler2",
    "IUIAnimationManager",
    "IUIAnimationManager2",
    "IUIAnimationManagerEventHandler",
    "IUIAnimationManagerEventHandler2",
    "IUIAnimationPrimitiveInterpolation",
    "IUIAnimationPriorityComparison",
    "IUIAnimationPriorityComparison2",
    "IUIAnimationStoryboard",
    "IUIAnimationStoryboard2",
    "IUIAnimationStoryboardEventHandler",
    "IUIAnimationStoryboardEventHandler2",
    "IUIAnimationTimer",
    "IUIAnimationTimerClientEventHandler",
    "IUIAnimationTimerEventHandler",
    "IUIAnimationTimerUpdateHandler",
    "IUIAnimationTransition",
    "IUIAnimationTransition2",
    "IUIAnimationTransitionFactory",
    "IUIAnimationTransitionFactory2",
    "IUIAnimationTransitionLibrary",
    "IUIAnimationTransitionLibrary2",
    "IUIAnimationVariable",
    "IUIAnimationVariable2",
    "IUIAnimationVariableChangeHandler",
    "IUIAnimationVariableChangeHandler2",
    "IUIAnimationVariableCurveChangeHandler2",
    "IUIAnimationVariableIntegerChangeHandler",
    "IUIAnimationVariableIntegerChangeHandler2",
    "UIAnimationManager",
    "UIAnimationManager2",
    "UIAnimationTimer",
    "UIAnimationTransitionFactory",
    "UIAnimationTransitionFactory2",
    "UIAnimationTransitionLibrary",
    "UIAnimationTransitionLibrary2",
    "UI_ANIMATION_DEPENDENCIES",
    "UI_ANIMATION_DEPENDENCY_DURATION",
    "UI_ANIMATION_DEPENDENCY_FINAL_VALUE",
    "UI_ANIMATION_DEPENDENCY_FINAL_VELOCITY",
    "UI_ANIMATION_DEPENDENCY_INTERMEDIATE_VALUES",
    "UI_ANIMATION_DEPENDENCY_NONE",
    "UI_ANIMATION_IDLE_BEHAVIOR",
    "UI_ANIMATION_IDLE_BEHAVIOR_CONTINUE",
    "UI_ANIMATION_IDLE_BEHAVIOR_DISABLE",
    "UI_ANIMATION_KEYFRAME",
    "UI_ANIMATION_MANAGER_BUSY",
    "UI_ANIMATION_MANAGER_IDLE",
    "UI_ANIMATION_MANAGER_STATUS",
    "UI_ANIMATION_MODE",
    "UI_ANIMATION_MODE_DISABLED",
    "UI_ANIMATION_MODE_ENABLED",
    "UI_ANIMATION_MODE_SYSTEM_DEFAULT",
    "UI_ANIMATION_PRIORITY_EFFECT",
    "UI_ANIMATION_PRIORITY_EFFECT_DELAY",
    "UI_ANIMATION_PRIORITY_EFFECT_FAILURE",
    "UI_ANIMATION_REPEAT_INDEFINITELY",
    "UI_ANIMATION_REPEAT_INDEFINITELY_CONCLUDE_AT_END",
    "UI_ANIMATION_REPEAT_INDEFINITELY_CONCLUDE_AT_START",
    "UI_ANIMATION_REPEAT_MODE",
    "UI_ANIMATION_REPEAT_MODE_ALTERNATE",
    "UI_ANIMATION_REPEAT_MODE_NORMAL",
    "UI_ANIMATION_ROUNDING_CEILING",
    "UI_ANIMATION_ROUNDING_FLOOR",
    "UI_ANIMATION_ROUNDING_MODE",
    "UI_ANIMATION_ROUNDING_NEAREST",
    "UI_ANIMATION_SCHEDULING_ALREADY_SCHEDULED",
    "UI_ANIMATION_SCHEDULING_DEFERRED",
    "UI_ANIMATION_SCHEDULING_INSUFFICIENT_PRIORITY",
    "UI_ANIMATION_SCHEDULING_RESULT",
    "UI_ANIMATION_SCHEDULING_SUCCEEDED",
    "UI_ANIMATION_SCHEDULING_UNEXPECTED_FAILURE",
    "UI_ANIMATION_SECONDS_EVENTUALLY",
    "UI_ANIMATION_SECONDS_INFINITE",
    "UI_ANIMATION_SLOPE",
    "UI_ANIMATION_SLOPE_DECREASING",
    "UI_ANIMATION_SLOPE_INCREASING",
    "UI_ANIMATION_STORYBOARD_BUILDING",
    "UI_ANIMATION_STORYBOARD_CANCELLED",
    "UI_ANIMATION_STORYBOARD_FINISHED",
    "UI_ANIMATION_STORYBOARD_INSUFFICIENT_PRIORITY",
    "UI_ANIMATION_STORYBOARD_PLAYING",
    "UI_ANIMATION_STORYBOARD_READY",
    "UI_ANIMATION_STORYBOARD_SCHEDULED",
    "UI_ANIMATION_STORYBOARD_STATUS",
    "UI_ANIMATION_STORYBOARD_TRUNCATED",
    "UI_ANIMATION_TIMER_CLIENT_BUSY",
    "UI_ANIMATION_TIMER_CLIENT_IDLE",
    "UI_ANIMATION_TIMER_CLIENT_STATUS",
    "UI_ANIMATION_UPDATE_NO_CHANGE",
    "UI_ANIMATION_UPDATE_RESULT",
    "UI_ANIMATION_UPDATE_VARIABLES_CHANGED",
]
_arch_optional = [
]
