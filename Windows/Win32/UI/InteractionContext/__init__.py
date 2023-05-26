from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.UI.Input.Pointer
import Windows.Win32.UI.InteractionContext
import Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
@winfunctype('NInput.dll')
def CreateInteractionContext(interactionContext: POINTER(Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def DestroyInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def RegisterOutputCallbackInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, outputCallback: Windows.Win32.UI.InteractionContext.INTERACTION_CONTEXT_OUTPUT_CALLBACK, clientData: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def RegisterOutputCallbackInteractionContext2(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, outputCallback: Windows.Win32.UI.InteractionContext.INTERACTION_CONTEXT_OUTPUT_CALLBACK2, clientData: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def SetInteractionConfigurationInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, configurationCount: UInt32, configuration: POINTER(Windows.Win32.UI.InteractionContext.INTERACTION_CONTEXT_CONFIGURATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def GetInteractionConfigurationInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, configurationCount: UInt32, configuration: POINTER(Windows.Win32.UI.InteractionContext.INTERACTION_CONTEXT_CONFIGURATION_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def SetPropertyInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, contextProperty: Windows.Win32.UI.InteractionContext.INTERACTION_CONTEXT_PROPERTY, value: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def GetPropertyInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, contextProperty: Windows.Win32.UI.InteractionContext.INTERACTION_CONTEXT_PROPERTY, value: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def SetInertiaParameterInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, inertiaParameter: Windows.Win32.UI.InteractionContext.INERTIA_PARAMETER, value: Single) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def GetInertiaParameterInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, inertiaParameter: Windows.Win32.UI.InteractionContext.INERTIA_PARAMETER, value: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def SetCrossSlideParametersInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, parameterCount: UInt32, crossSlideParameters: POINTER(Windows.Win32.UI.InteractionContext.CROSS_SLIDE_PARAMETER_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def GetCrossSlideParameterInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, threshold: Windows.Win32.UI.InteractionContext.CROSS_SLIDE_THRESHOLD, distance: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def SetTapParameterInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, parameter: Windows.Win32.UI.InteractionContext.TAP_PARAMETER, value: Single) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def GetTapParameterInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, parameter: Windows.Win32.UI.InteractionContext.TAP_PARAMETER, value: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def SetHoldParameterInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, parameter: Windows.Win32.UI.InteractionContext.HOLD_PARAMETER, value: Single) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def GetHoldParameterInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, parameter: Windows.Win32.UI.InteractionContext.HOLD_PARAMETER, value: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def SetTranslationParameterInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, parameter: Windows.Win32.UI.InteractionContext.TRANSLATION_PARAMETER, value: Single) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def GetTranslationParameterInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, parameter: Windows.Win32.UI.InteractionContext.TRANSLATION_PARAMETER, value: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def SetMouseWheelParameterInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, parameter: Windows.Win32.UI.InteractionContext.MOUSE_WHEEL_PARAMETER, value: Single) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def GetMouseWheelParameterInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, parameter: Windows.Win32.UI.InteractionContext.MOUSE_WHEEL_PARAMETER, value: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def ResetInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def GetStateInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, pointerInfo: POINTER(Windows.Win32.UI.Input.Pointer.POINTER_INFO_head), state: POINTER(Windows.Win32.UI.InteractionContext.INTERACTION_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def AddPointerInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, pointerId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def RemovePointerInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, pointerId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def ProcessPointerFramesInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, entriesCount: UInt32, pointerCount: UInt32, pointerInfo: POINTER(Windows.Win32.UI.Input.Pointer.POINTER_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def BufferPointerPacketsInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, entriesCount: UInt32, pointerInfo: POINTER(Windows.Win32.UI.Input.Pointer.POINTER_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def ProcessBufferedPacketsInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def ProcessInertiaInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def StopInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('NInput.dll')
def SetPivotInteractionContext(interactionContext: Windows.Win32.UI.InteractionContext.HINTERACTIONCONTEXT, x: Single, y: Single, radius: Single) -> Windows.Win32.Foundation.HRESULT: ...
CROSS_SLIDE_FLAGS = UInt32
CROSS_SLIDE_FLAGS_NONE: CROSS_SLIDE_FLAGS = 0
CROSS_SLIDE_FLAGS_SELECT: CROSS_SLIDE_FLAGS = 1
CROSS_SLIDE_FLAGS_SPEED_BUMP: CROSS_SLIDE_FLAGS = 2
CROSS_SLIDE_FLAGS_REARRANGE: CROSS_SLIDE_FLAGS = 4
CROSS_SLIDE_FLAGS_MAX: CROSS_SLIDE_FLAGS = 4294967295
class CROSS_SLIDE_PARAMETER(EasyCastStructure):
    threshold: Windows.Win32.UI.InteractionContext.CROSS_SLIDE_THRESHOLD
    distance: Single
CROSS_SLIDE_THRESHOLD = Int32
CROSS_SLIDE_THRESHOLD_SELECT_START: CROSS_SLIDE_THRESHOLD = 0
CROSS_SLIDE_THRESHOLD_SPEED_BUMP_START: CROSS_SLIDE_THRESHOLD = 1
CROSS_SLIDE_THRESHOLD_SPEED_BUMP_END: CROSS_SLIDE_THRESHOLD = 2
CROSS_SLIDE_THRESHOLD_REARRANGE_START: CROSS_SLIDE_THRESHOLD = 3
CROSS_SLIDE_THRESHOLD_COUNT: CROSS_SLIDE_THRESHOLD = 4
CROSS_SLIDE_THRESHOLD_MAX: CROSS_SLIDE_THRESHOLD = -1
HINTERACTIONCONTEXT = IntPtr
HOLD_PARAMETER = Int32
HOLD_PARAMETER_MIN_CONTACT_COUNT: HOLD_PARAMETER = 0
HOLD_PARAMETER_MAX_CONTACT_COUNT: HOLD_PARAMETER = 1
HOLD_PARAMETER_THRESHOLD_RADIUS: HOLD_PARAMETER = 2
HOLD_PARAMETER_THRESHOLD_START_DELAY: HOLD_PARAMETER = 3
HOLD_PARAMETER_MAX: HOLD_PARAMETER = -1
INERTIA_PARAMETER = Int32
INERTIA_PARAMETER_TRANSLATION_DECELERATION: INERTIA_PARAMETER = 1
INERTIA_PARAMETER_TRANSLATION_DISPLACEMENT: INERTIA_PARAMETER = 2
INERTIA_PARAMETER_ROTATION_DECELERATION: INERTIA_PARAMETER = 3
INERTIA_PARAMETER_ROTATION_ANGLE: INERTIA_PARAMETER = 4
INERTIA_PARAMETER_EXPANSION_DECELERATION: INERTIA_PARAMETER = 5
INERTIA_PARAMETER_EXPANSION_EXPANSION: INERTIA_PARAMETER = 6
INERTIA_PARAMETER_MAX: INERTIA_PARAMETER = -1
class INTERACTION_ARGUMENTS_CROSS_SLIDE(EasyCastStructure):
    flags: Windows.Win32.UI.InteractionContext.CROSS_SLIDE_FLAGS
class INTERACTION_ARGUMENTS_MANIPULATION(EasyCastStructure):
    delta: Windows.Win32.UI.InteractionContext.MANIPULATION_TRANSFORM
    cumulative: Windows.Win32.UI.InteractionContext.MANIPULATION_TRANSFORM
    velocity: Windows.Win32.UI.InteractionContext.MANIPULATION_VELOCITY
    railsState: Windows.Win32.UI.InteractionContext.MANIPULATION_RAILS_STATE
class INTERACTION_ARGUMENTS_TAP(EasyCastStructure):
    count: UInt32
INTERACTION_CONFIGURATION_FLAGS = UInt32
INTERACTION_CONFIGURATION_FLAG_NONE: INTERACTION_CONFIGURATION_FLAGS = 0
INTERACTION_CONFIGURATION_FLAG_MANIPULATION: INTERACTION_CONFIGURATION_FLAGS = 1
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_TRANSLATION_X: INTERACTION_CONFIGURATION_FLAGS = 2
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_TRANSLATION_Y: INTERACTION_CONFIGURATION_FLAGS = 4
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_ROTATION: INTERACTION_CONFIGURATION_FLAGS = 8
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_SCALING: INTERACTION_CONFIGURATION_FLAGS = 16
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_TRANSLATION_INERTIA: INTERACTION_CONFIGURATION_FLAGS = 32
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_ROTATION_INERTIA: INTERACTION_CONFIGURATION_FLAGS = 64
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_SCALING_INERTIA: INTERACTION_CONFIGURATION_FLAGS = 128
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_RAILS_X: INTERACTION_CONFIGURATION_FLAGS = 256
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_RAILS_Y: INTERACTION_CONFIGURATION_FLAGS = 512
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_EXACT: INTERACTION_CONFIGURATION_FLAGS = 1024
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_MULTIPLE_FINGER_PANNING: INTERACTION_CONFIGURATION_FLAGS = 2048
INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE: INTERACTION_CONFIGURATION_FLAGS = 1
INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_HORIZONTAL: INTERACTION_CONFIGURATION_FLAGS = 2
INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_SELECT: INTERACTION_CONFIGURATION_FLAGS = 4
INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_SPEED_BUMP: INTERACTION_CONFIGURATION_FLAGS = 8
INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_REARRANGE: INTERACTION_CONFIGURATION_FLAGS = 16
INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_EXACT: INTERACTION_CONFIGURATION_FLAGS = 32
INTERACTION_CONFIGURATION_FLAG_TAP: INTERACTION_CONFIGURATION_FLAGS = 1
INTERACTION_CONFIGURATION_FLAG_TAP_DOUBLE: INTERACTION_CONFIGURATION_FLAGS = 2
INTERACTION_CONFIGURATION_FLAG_TAP_MULTIPLE_FINGER: INTERACTION_CONFIGURATION_FLAGS = 4
INTERACTION_CONFIGURATION_FLAG_SECONDARY_TAP: INTERACTION_CONFIGURATION_FLAGS = 1
INTERACTION_CONFIGURATION_FLAG_HOLD: INTERACTION_CONFIGURATION_FLAGS = 1
INTERACTION_CONFIGURATION_FLAG_HOLD_MOUSE: INTERACTION_CONFIGURATION_FLAGS = 2
INTERACTION_CONFIGURATION_FLAG_HOLD_MULTIPLE_FINGER: INTERACTION_CONFIGURATION_FLAGS = 4
INTERACTION_CONFIGURATION_FLAG_DRAG: INTERACTION_CONFIGURATION_FLAGS = 1
INTERACTION_CONFIGURATION_FLAG_MAX: INTERACTION_CONFIGURATION_FLAGS = 4294967295
class INTERACTION_CONTEXT_CONFIGURATION(EasyCastStructure):
    interactionId: Windows.Win32.UI.InteractionContext.INTERACTION_ID
    enable: Windows.Win32.UI.InteractionContext.INTERACTION_CONFIGURATION_FLAGS
class INTERACTION_CONTEXT_OUTPUT(EasyCastStructure):
    interactionId: Windows.Win32.UI.InteractionContext.INTERACTION_ID
    interactionFlags: Windows.Win32.UI.InteractionContext.INTERACTION_FLAGS
    inputType: Windows.Win32.UI.WindowsAndMessaging.POINTER_INPUT_TYPE
    x: Single
    y: Single
    arguments: _arguments_e__Union
    class _arguments_e__Union(EasyCastUnion):
        manipulation: Windows.Win32.UI.InteractionContext.INTERACTION_ARGUMENTS_MANIPULATION
        tap: Windows.Win32.UI.InteractionContext.INTERACTION_ARGUMENTS_TAP
        crossSlide: Windows.Win32.UI.InteractionContext.INTERACTION_ARGUMENTS_CROSS_SLIDE
class INTERACTION_CONTEXT_OUTPUT2(EasyCastStructure):
    interactionId: Windows.Win32.UI.InteractionContext.INTERACTION_ID
    interactionFlags: Windows.Win32.UI.InteractionContext.INTERACTION_FLAGS
    inputType: Windows.Win32.UI.WindowsAndMessaging.POINTER_INPUT_TYPE
    contactCount: UInt32
    currentContactCount: UInt32
    x: Single
    y: Single
    arguments: _arguments_e__Union
    class _arguments_e__Union(EasyCastUnion):
        manipulation: Windows.Win32.UI.InteractionContext.INTERACTION_ARGUMENTS_MANIPULATION
        tap: Windows.Win32.UI.InteractionContext.INTERACTION_ARGUMENTS_TAP
        crossSlide: Windows.Win32.UI.InteractionContext.INTERACTION_ARGUMENTS_CROSS_SLIDE
@winfunctype_pointer
def INTERACTION_CONTEXT_OUTPUT_CALLBACK(clientData: VoidPtr, output: POINTER(Windows.Win32.UI.InteractionContext.INTERACTION_CONTEXT_OUTPUT_head)) -> Void: ...
@winfunctype_pointer
def INTERACTION_CONTEXT_OUTPUT_CALLBACK2(clientData: VoidPtr, output: POINTER(Windows.Win32.UI.InteractionContext.INTERACTION_CONTEXT_OUTPUT2_head)) -> Void: ...
INTERACTION_CONTEXT_PROPERTY = Int32
INTERACTION_CONTEXT_PROPERTY_MEASUREMENT_UNITS: INTERACTION_CONTEXT_PROPERTY = 1
INTERACTION_CONTEXT_PROPERTY_INTERACTION_UI_FEEDBACK: INTERACTION_CONTEXT_PROPERTY = 2
INTERACTION_CONTEXT_PROPERTY_FILTER_POINTERS: INTERACTION_CONTEXT_PROPERTY = 3
INTERACTION_CONTEXT_PROPERTY_MAX: INTERACTION_CONTEXT_PROPERTY = -1
INTERACTION_FLAGS = UInt32
INTERACTION_FLAG_NONE: INTERACTION_FLAGS = 0
INTERACTION_FLAG_BEGIN: INTERACTION_FLAGS = 1
INTERACTION_FLAG_END: INTERACTION_FLAGS = 2
INTERACTION_FLAG_CANCEL: INTERACTION_FLAGS = 4
INTERACTION_FLAG_INERTIA: INTERACTION_FLAGS = 8
INTERACTION_FLAG_MAX: INTERACTION_FLAGS = 4294967295
INTERACTION_ID = Int32
INTERACTION_ID_NONE: INTERACTION_ID = 0
INTERACTION_ID_MANIPULATION: INTERACTION_ID = 1
INTERACTION_ID_TAP: INTERACTION_ID = 2
INTERACTION_ID_SECONDARY_TAP: INTERACTION_ID = 3
INTERACTION_ID_HOLD: INTERACTION_ID = 4
INTERACTION_ID_DRAG: INTERACTION_ID = 5
INTERACTION_ID_CROSS_SLIDE: INTERACTION_ID = 6
INTERACTION_ID_MAX: INTERACTION_ID = -1
INTERACTION_STATE = Int32
INTERACTION_STATE_IDLE: INTERACTION_STATE = 0
INTERACTION_STATE_IN_INTERACTION: INTERACTION_STATE = 1
INTERACTION_STATE_POSSIBLE_DOUBLE_TAP: INTERACTION_STATE = 2
INTERACTION_STATE_MAX: INTERACTION_STATE = -1
MANIPULATION_RAILS_STATE = Int32
MANIPULATION_RAILS_STATE_UNDECIDED: MANIPULATION_RAILS_STATE = 0
MANIPULATION_RAILS_STATE_FREE: MANIPULATION_RAILS_STATE = 1
MANIPULATION_RAILS_STATE_RAILED: MANIPULATION_RAILS_STATE = 2
MANIPULATION_RAILS_STATE_MAX: MANIPULATION_RAILS_STATE = -1
class MANIPULATION_TRANSFORM(EasyCastStructure):
    translationX: Single
    translationY: Single
    scale: Single
    expansion: Single
    rotation: Single
class MANIPULATION_VELOCITY(EasyCastStructure):
    velocityX: Single
    velocityY: Single
    velocityExpansion: Single
    velocityAngular: Single
MOUSE_WHEEL_PARAMETER = Int32
MOUSE_WHEEL_PARAMETER_CHAR_TRANSLATION_X: MOUSE_WHEEL_PARAMETER = 1
MOUSE_WHEEL_PARAMETER_CHAR_TRANSLATION_Y: MOUSE_WHEEL_PARAMETER = 2
MOUSE_WHEEL_PARAMETER_DELTA_SCALE: MOUSE_WHEEL_PARAMETER = 3
MOUSE_WHEEL_PARAMETER_DELTA_ROTATION: MOUSE_WHEEL_PARAMETER = 4
MOUSE_WHEEL_PARAMETER_PAGE_TRANSLATION_X: MOUSE_WHEEL_PARAMETER = 5
MOUSE_WHEEL_PARAMETER_PAGE_TRANSLATION_Y: MOUSE_WHEEL_PARAMETER = 6
MOUSE_WHEEL_PARAMETER_MAX: MOUSE_WHEEL_PARAMETER = -1
TAP_PARAMETER = Int32
TAP_PARAMETER_MIN_CONTACT_COUNT: TAP_PARAMETER = 0
TAP_PARAMETER_MAX_CONTACT_COUNT: TAP_PARAMETER = 1
TAP_PARAMETER_MAX: TAP_PARAMETER = -1
TRANSLATION_PARAMETER = Int32
TRANSLATION_PARAMETER_MIN_CONTACT_COUNT: TRANSLATION_PARAMETER = 0
TRANSLATION_PARAMETER_MAX_CONTACT_COUNT: TRANSLATION_PARAMETER = 1
TRANSLATION_PARAMETER_MAX: TRANSLATION_PARAMETER = -1
make_head(_module, 'CROSS_SLIDE_PARAMETER')
make_head(_module, 'INTERACTION_ARGUMENTS_CROSS_SLIDE')
make_head(_module, 'INTERACTION_ARGUMENTS_MANIPULATION')
make_head(_module, 'INTERACTION_ARGUMENTS_TAP')
make_head(_module, 'INTERACTION_CONTEXT_CONFIGURATION')
make_head(_module, 'INTERACTION_CONTEXT_OUTPUT')
make_head(_module, 'INTERACTION_CONTEXT_OUTPUT2')
make_head(_module, 'INTERACTION_CONTEXT_OUTPUT_CALLBACK')
make_head(_module, 'INTERACTION_CONTEXT_OUTPUT_CALLBACK2')
make_head(_module, 'MANIPULATION_TRANSFORM')
make_head(_module, 'MANIPULATION_VELOCITY')
