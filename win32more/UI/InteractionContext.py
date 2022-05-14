from win32more import *
import win32more.UI.InteractionContext
import win32more.Foundation
import win32more.UI.Input.Pointer
import win32more.UI.WindowsAndMessaging

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.UI.InteractionContext, name, eval(f"_define_{name}()"))
    return getattr(win32more.UI.InteractionContext, name)
HINTERACTIONCONTEXT = IntPtr
INTERACTION_ID = Int32
INTERACTION_ID_NONE = 0
INTERACTION_ID_MANIPULATION = 1
INTERACTION_ID_TAP = 2
INTERACTION_ID_SECONDARY_TAP = 3
INTERACTION_ID_HOLD = 4
INTERACTION_ID_DRAG = 5
INTERACTION_ID_CROSS_SLIDE = 6
INTERACTION_ID_MAX = -1
INTERACTION_FLAGS = UInt32
INTERACTION_FLAG_NONE = 0
INTERACTION_FLAG_BEGIN = 1
INTERACTION_FLAG_END = 2
INTERACTION_FLAG_CANCEL = 4
INTERACTION_FLAG_INERTIA = 8
INTERACTION_FLAG_MAX = 4294967295
INTERACTION_CONFIGURATION_FLAGS = UInt32
INTERACTION_CONFIGURATION_FLAG_NONE = 0
INTERACTION_CONFIGURATION_FLAG_MANIPULATION = 1
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_TRANSLATION_X = 2
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_TRANSLATION_Y = 4
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_ROTATION = 8
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_SCALING = 16
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_TRANSLATION_INERTIA = 32
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_ROTATION_INERTIA = 64
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_SCALING_INERTIA = 128
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_RAILS_X = 256
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_RAILS_Y = 512
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_EXACT = 1024
INTERACTION_CONFIGURATION_FLAG_MANIPULATION_MULTIPLE_FINGER_PANNING = 2048
INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE = 1
INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_HORIZONTAL = 2
INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_SELECT = 4
INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_SPEED_BUMP = 8
INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_REARRANGE = 16
INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_EXACT = 32
INTERACTION_CONFIGURATION_FLAG_TAP = 1
INTERACTION_CONFIGURATION_FLAG_TAP_DOUBLE = 2
INTERACTION_CONFIGURATION_FLAG_TAP_MULTIPLE_FINGER = 4
INTERACTION_CONFIGURATION_FLAG_SECONDARY_TAP = 1
INTERACTION_CONFIGURATION_FLAG_HOLD = 1
INTERACTION_CONFIGURATION_FLAG_HOLD_MOUSE = 2
INTERACTION_CONFIGURATION_FLAG_HOLD_MULTIPLE_FINGER = 4
INTERACTION_CONFIGURATION_FLAG_DRAG = 1
INTERACTION_CONFIGURATION_FLAG_MAX = 4294967295
INERTIA_PARAMETER = Int32
INERTIA_PARAMETER_TRANSLATION_DECELERATION = 1
INERTIA_PARAMETER_TRANSLATION_DISPLACEMENT = 2
INERTIA_PARAMETER_ROTATION_DECELERATION = 3
INERTIA_PARAMETER_ROTATION_ANGLE = 4
INERTIA_PARAMETER_EXPANSION_DECELERATION = 5
INERTIA_PARAMETER_EXPANSION_EXPANSION = 6
INERTIA_PARAMETER_MAX = -1
INTERACTION_STATE = Int32
INTERACTION_STATE_IDLE = 0
INTERACTION_STATE_IN_INTERACTION = 1
INTERACTION_STATE_POSSIBLE_DOUBLE_TAP = 2
INTERACTION_STATE_MAX = -1
INTERACTION_CONTEXT_PROPERTY = Int32
INTERACTION_CONTEXT_PROPERTY_MEASUREMENT_UNITS = 1
INTERACTION_CONTEXT_PROPERTY_INTERACTION_UI_FEEDBACK = 2
INTERACTION_CONTEXT_PROPERTY_FILTER_POINTERS = 3
INTERACTION_CONTEXT_PROPERTY_MAX = -1
CROSS_SLIDE_THRESHOLD = Int32
CROSS_SLIDE_THRESHOLD_SELECT_START = 0
CROSS_SLIDE_THRESHOLD_SPEED_BUMP_START = 1
CROSS_SLIDE_THRESHOLD_SPEED_BUMP_END = 2
CROSS_SLIDE_THRESHOLD_REARRANGE_START = 3
CROSS_SLIDE_THRESHOLD_COUNT = 4
CROSS_SLIDE_THRESHOLD_MAX = -1
CROSS_SLIDE_FLAGS = UInt32
CROSS_SLIDE_FLAGS_NONE = 0
CROSS_SLIDE_FLAGS_SELECT = 1
CROSS_SLIDE_FLAGS_SPEED_BUMP = 2
CROSS_SLIDE_FLAGS_REARRANGE = 4
CROSS_SLIDE_FLAGS_MAX = 4294967295
MOUSE_WHEEL_PARAMETER = Int32
MOUSE_WHEEL_PARAMETER_CHAR_TRANSLATION_X = 1
MOUSE_WHEEL_PARAMETER_CHAR_TRANSLATION_Y = 2
MOUSE_WHEEL_PARAMETER_DELTA_SCALE = 3
MOUSE_WHEEL_PARAMETER_DELTA_ROTATION = 4
MOUSE_WHEEL_PARAMETER_PAGE_TRANSLATION_X = 5
MOUSE_WHEEL_PARAMETER_PAGE_TRANSLATION_Y = 6
MOUSE_WHEEL_PARAMETER_MAX = -1
TAP_PARAMETER = Int32
TAP_PARAMETER_MIN_CONTACT_COUNT = 0
TAP_PARAMETER_MAX_CONTACT_COUNT = 1
TAP_PARAMETER_MAX = -1
HOLD_PARAMETER = Int32
HOLD_PARAMETER_MIN_CONTACT_COUNT = 0
HOLD_PARAMETER_MAX_CONTACT_COUNT = 1
HOLD_PARAMETER_THRESHOLD_RADIUS = 2
HOLD_PARAMETER_THRESHOLD_START_DELAY = 3
HOLD_PARAMETER_MAX = -1
TRANSLATION_PARAMETER = Int32
TRANSLATION_PARAMETER_MIN_CONTACT_COUNT = 0
TRANSLATION_PARAMETER_MAX_CONTACT_COUNT = 1
TRANSLATION_PARAMETER_MAX = -1
MANIPULATION_RAILS_STATE = Int32
MANIPULATION_RAILS_STATE_UNDECIDED = 0
MANIPULATION_RAILS_STATE_FREE = 1
MANIPULATION_RAILS_STATE_RAILED = 2
MANIPULATION_RAILS_STATE_MAX = -1
def _define_MANIPULATION_TRANSFORM_head():
    class MANIPULATION_TRANSFORM(Structure):
        pass
    return MANIPULATION_TRANSFORM
def _define_MANIPULATION_TRANSFORM():
    MANIPULATION_TRANSFORM = win32more.UI.InteractionContext.MANIPULATION_TRANSFORM_head
    MANIPULATION_TRANSFORM._fields_ = [
        ("translationX", Single),
        ("translationY", Single),
        ("scale", Single),
        ("expansion", Single),
        ("rotation", Single),
    ]
    return MANIPULATION_TRANSFORM
def _define_MANIPULATION_VELOCITY_head():
    class MANIPULATION_VELOCITY(Structure):
        pass
    return MANIPULATION_VELOCITY
def _define_MANIPULATION_VELOCITY():
    MANIPULATION_VELOCITY = win32more.UI.InteractionContext.MANIPULATION_VELOCITY_head
    MANIPULATION_VELOCITY._fields_ = [
        ("velocityX", Single),
        ("velocityY", Single),
        ("velocityExpansion", Single),
        ("velocityAngular", Single),
    ]
    return MANIPULATION_VELOCITY
def _define_INTERACTION_ARGUMENTS_MANIPULATION_head():
    class INTERACTION_ARGUMENTS_MANIPULATION(Structure):
        pass
    return INTERACTION_ARGUMENTS_MANIPULATION
def _define_INTERACTION_ARGUMENTS_MANIPULATION():
    INTERACTION_ARGUMENTS_MANIPULATION = win32more.UI.InteractionContext.INTERACTION_ARGUMENTS_MANIPULATION_head
    INTERACTION_ARGUMENTS_MANIPULATION._fields_ = [
        ("delta", win32more.UI.InteractionContext.MANIPULATION_TRANSFORM),
        ("cumulative", win32more.UI.InteractionContext.MANIPULATION_TRANSFORM),
        ("velocity", win32more.UI.InteractionContext.MANIPULATION_VELOCITY),
        ("railsState", win32more.UI.InteractionContext.MANIPULATION_RAILS_STATE),
    ]
    return INTERACTION_ARGUMENTS_MANIPULATION
def _define_INTERACTION_ARGUMENTS_TAP_head():
    class INTERACTION_ARGUMENTS_TAP(Structure):
        pass
    return INTERACTION_ARGUMENTS_TAP
def _define_INTERACTION_ARGUMENTS_TAP():
    INTERACTION_ARGUMENTS_TAP = win32more.UI.InteractionContext.INTERACTION_ARGUMENTS_TAP_head
    INTERACTION_ARGUMENTS_TAP._fields_ = [
        ("count", UInt32),
    ]
    return INTERACTION_ARGUMENTS_TAP
def _define_INTERACTION_ARGUMENTS_CROSS_SLIDE_head():
    class INTERACTION_ARGUMENTS_CROSS_SLIDE(Structure):
        pass
    return INTERACTION_ARGUMENTS_CROSS_SLIDE
def _define_INTERACTION_ARGUMENTS_CROSS_SLIDE():
    INTERACTION_ARGUMENTS_CROSS_SLIDE = win32more.UI.InteractionContext.INTERACTION_ARGUMENTS_CROSS_SLIDE_head
    INTERACTION_ARGUMENTS_CROSS_SLIDE._fields_ = [
        ("flags", win32more.UI.InteractionContext.CROSS_SLIDE_FLAGS),
    ]
    return INTERACTION_ARGUMENTS_CROSS_SLIDE
def _define_INTERACTION_CONTEXT_OUTPUT_head():
    class INTERACTION_CONTEXT_OUTPUT(Structure):
        pass
    return INTERACTION_CONTEXT_OUTPUT
def _define_INTERACTION_CONTEXT_OUTPUT():
    INTERACTION_CONTEXT_OUTPUT = win32more.UI.InteractionContext.INTERACTION_CONTEXT_OUTPUT_head
    class INTERACTION_CONTEXT_OUTPUT__arguments_e__Union(Union):
        pass
    INTERACTION_CONTEXT_OUTPUT__arguments_e__Union._fields_ = [
        ("manipulation", win32more.UI.InteractionContext.INTERACTION_ARGUMENTS_MANIPULATION),
        ("tap", win32more.UI.InteractionContext.INTERACTION_ARGUMENTS_TAP),
        ("crossSlide", win32more.UI.InteractionContext.INTERACTION_ARGUMENTS_CROSS_SLIDE),
    ]
    INTERACTION_CONTEXT_OUTPUT._fields_ = [
        ("interactionId", win32more.UI.InteractionContext.INTERACTION_ID),
        ("interactionFlags", win32more.UI.InteractionContext.INTERACTION_FLAGS),
        ("inputType", win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE),
        ("x", Single),
        ("y", Single),
        ("arguments", INTERACTION_CONTEXT_OUTPUT__arguments_e__Union),
    ]
    return INTERACTION_CONTEXT_OUTPUT
def _define_INTERACTION_CONTEXT_OUTPUT2_head():
    class INTERACTION_CONTEXT_OUTPUT2(Structure):
        pass
    return INTERACTION_CONTEXT_OUTPUT2
def _define_INTERACTION_CONTEXT_OUTPUT2():
    INTERACTION_CONTEXT_OUTPUT2 = win32more.UI.InteractionContext.INTERACTION_CONTEXT_OUTPUT2_head
    class INTERACTION_CONTEXT_OUTPUT2__arguments_e__Union(Union):
        pass
    INTERACTION_CONTEXT_OUTPUT2__arguments_e__Union._fields_ = [
        ("manipulation", win32more.UI.InteractionContext.INTERACTION_ARGUMENTS_MANIPULATION),
        ("tap", win32more.UI.InteractionContext.INTERACTION_ARGUMENTS_TAP),
        ("crossSlide", win32more.UI.InteractionContext.INTERACTION_ARGUMENTS_CROSS_SLIDE),
    ]
    INTERACTION_CONTEXT_OUTPUT2._fields_ = [
        ("interactionId", win32more.UI.InteractionContext.INTERACTION_ID),
        ("interactionFlags", win32more.UI.InteractionContext.INTERACTION_FLAGS),
        ("inputType", win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE),
        ("contactCount", UInt32),
        ("currentContactCount", UInt32),
        ("x", Single),
        ("y", Single),
        ("arguments", INTERACTION_CONTEXT_OUTPUT2__arguments_e__Union),
    ]
    return INTERACTION_CONTEXT_OUTPUT2
def _define_INTERACTION_CONTEXT_CONFIGURATION_head():
    class INTERACTION_CONTEXT_CONFIGURATION(Structure):
        pass
    return INTERACTION_CONTEXT_CONFIGURATION
def _define_INTERACTION_CONTEXT_CONFIGURATION():
    INTERACTION_CONTEXT_CONFIGURATION = win32more.UI.InteractionContext.INTERACTION_CONTEXT_CONFIGURATION_head
    INTERACTION_CONTEXT_CONFIGURATION._fields_ = [
        ("interactionId", win32more.UI.InteractionContext.INTERACTION_ID),
        ("enable", win32more.UI.InteractionContext.INTERACTION_CONFIGURATION_FLAGS),
    ]
    return INTERACTION_CONTEXT_CONFIGURATION
def _define_CROSS_SLIDE_PARAMETER_head():
    class CROSS_SLIDE_PARAMETER(Structure):
        pass
    return CROSS_SLIDE_PARAMETER
def _define_CROSS_SLIDE_PARAMETER():
    CROSS_SLIDE_PARAMETER = win32more.UI.InteractionContext.CROSS_SLIDE_PARAMETER_head
    CROSS_SLIDE_PARAMETER._fields_ = [
        ("threshold", win32more.UI.InteractionContext.CROSS_SLIDE_THRESHOLD),
        ("distance", Single),
    ]
    return CROSS_SLIDE_PARAMETER
def _define_INTERACTION_CONTEXT_OUTPUT_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.UI.InteractionContext.INTERACTION_CONTEXT_OUTPUT_head), use_last_error=False)
def _define_INTERACTION_CONTEXT_OUTPUT_CALLBACK2():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.UI.InteractionContext.INTERACTION_CONTEXT_OUTPUT2_head), use_last_error=False)
def _define_CreateInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.InteractionContext.HINTERACTIONCONTEXT), use_last_error=False)(("CreateInteractionContext", windll["NInput"]), ((1, 'interactionContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DestroyInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT, use_last_error=False)(("DestroyInteractionContext", windll["NInput"]), ((1, 'interactionContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterOutputCallbackInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.INTERACTION_CONTEXT_OUTPUT_CALLBACK,c_void_p, use_last_error=False)(("RegisterOutputCallbackInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'outputCallback'),(1, 'clientData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterOutputCallbackInteractionContext2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.INTERACTION_CONTEXT_OUTPUT_CALLBACK2,c_void_p, use_last_error=False)(("RegisterOutputCallbackInteractionContext2", windll["NInput"]), ((1, 'interactionContext'),(1, 'outputCallback'),(1, 'clientData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetInteractionConfigurationInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,UInt32,POINTER(win32more.UI.InteractionContext.INTERACTION_CONTEXT_CONFIGURATION), use_last_error=False)(("SetInteractionConfigurationInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'configurationCount'),(1, 'configuration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetInteractionConfigurationInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,UInt32,POINTER(win32more.UI.InteractionContext.INTERACTION_CONTEXT_CONFIGURATION), use_last_error=False)(("GetInteractionConfigurationInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'configurationCount'),(1, 'configuration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPropertyInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.INTERACTION_CONTEXT_PROPERTY,UInt32, use_last_error=False)(("SetPropertyInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'contextProperty'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPropertyInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.INTERACTION_CONTEXT_PROPERTY,POINTER(UInt32), use_last_error=False)(("GetPropertyInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'contextProperty'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetInertiaParameterInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.INERTIA_PARAMETER,Single, use_last_error=False)(("SetInertiaParameterInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'inertiaParameter'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetInertiaParameterInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.INERTIA_PARAMETER,POINTER(Single), use_last_error=False)(("GetInertiaParameterInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'inertiaParameter'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCrossSlideParametersInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,UInt32,POINTER(win32more.UI.InteractionContext.CROSS_SLIDE_PARAMETER), use_last_error=False)(("SetCrossSlideParametersInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'parameterCount'),(1, 'crossSlideParameters'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCrossSlideParameterInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.CROSS_SLIDE_THRESHOLD,POINTER(Single), use_last_error=False)(("GetCrossSlideParameterInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'threshold'),(1, 'distance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTapParameterInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.TAP_PARAMETER,Single, use_last_error=False)(("SetTapParameterInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'parameter'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTapParameterInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.TAP_PARAMETER,POINTER(Single), use_last_error=False)(("GetTapParameterInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'parameter'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetHoldParameterInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.HOLD_PARAMETER,Single, use_last_error=False)(("SetHoldParameterInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'parameter'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetHoldParameterInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.HOLD_PARAMETER,POINTER(Single), use_last_error=False)(("GetHoldParameterInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'parameter'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTranslationParameterInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.TRANSLATION_PARAMETER,Single, use_last_error=False)(("SetTranslationParameterInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'parameter'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTranslationParameterInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.TRANSLATION_PARAMETER,POINTER(Single), use_last_error=False)(("GetTranslationParameterInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'parameter'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMouseWheelParameterInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.MOUSE_WHEEL_PARAMETER,Single, use_last_error=False)(("SetMouseWheelParameterInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'parameter'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMouseWheelParameterInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,win32more.UI.InteractionContext.MOUSE_WHEEL_PARAMETER,POINTER(Single), use_last_error=False)(("GetMouseWheelParameterInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'parameter'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResetInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT, use_last_error=False)(("ResetInteractionContext", windll["NInput"]), ((1, 'interactionContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStateInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,POINTER(win32more.UI.Input.Pointer.POINTER_INFO_head),POINTER(win32more.UI.InteractionContext.INTERACTION_STATE), use_last_error=False)(("GetStateInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'pointerInfo'),(1, 'state'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddPointerInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,UInt32, use_last_error=False)(("AddPointerInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'pointerId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemovePointerInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,UInt32, use_last_error=False)(("RemovePointerInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'pointerId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ProcessPointerFramesInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,UInt32,UInt32,POINTER(win32more.UI.Input.Pointer.POINTER_INFO_head), use_last_error=False)(("ProcessPointerFramesInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'entriesCount'),(1, 'pointerCount'),(1, 'pointerInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BufferPointerPacketsInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,UInt32,POINTER(win32more.UI.Input.Pointer.POINTER_INFO), use_last_error=False)(("BufferPointerPacketsInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'entriesCount'),(1, 'pointerInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ProcessBufferedPacketsInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT, use_last_error=False)(("ProcessBufferedPacketsInteractionContext", windll["NInput"]), ((1, 'interactionContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ProcessInertiaInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT, use_last_error=False)(("ProcessInertiaInteractionContext", windll["NInput"]), ((1, 'interactionContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StopInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT, use_last_error=False)(("StopInteractionContext", windll["NInput"]), ((1, 'interactionContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPivotInteractionContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.InteractionContext.HINTERACTIONCONTEXT,Single,Single,Single, use_last_error=False)(("SetPivotInteractionContext", windll["NInput"]), ((1, 'interactionContext'),(1, 'x'),(1, 'y'),(1, 'radius'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "HINTERACTIONCONTEXT",
    "INTERACTION_ID",
    "INTERACTION_ID_NONE",
    "INTERACTION_ID_MANIPULATION",
    "INTERACTION_ID_TAP",
    "INTERACTION_ID_SECONDARY_TAP",
    "INTERACTION_ID_HOLD",
    "INTERACTION_ID_DRAG",
    "INTERACTION_ID_CROSS_SLIDE",
    "INTERACTION_ID_MAX",
    "INTERACTION_FLAGS",
    "INTERACTION_FLAG_NONE",
    "INTERACTION_FLAG_BEGIN",
    "INTERACTION_FLAG_END",
    "INTERACTION_FLAG_CANCEL",
    "INTERACTION_FLAG_INERTIA",
    "INTERACTION_FLAG_MAX",
    "INTERACTION_CONFIGURATION_FLAGS",
    "INTERACTION_CONFIGURATION_FLAG_NONE",
    "INTERACTION_CONFIGURATION_FLAG_MANIPULATION",
    "INTERACTION_CONFIGURATION_FLAG_MANIPULATION_TRANSLATION_X",
    "INTERACTION_CONFIGURATION_FLAG_MANIPULATION_TRANSLATION_Y",
    "INTERACTION_CONFIGURATION_FLAG_MANIPULATION_ROTATION",
    "INTERACTION_CONFIGURATION_FLAG_MANIPULATION_SCALING",
    "INTERACTION_CONFIGURATION_FLAG_MANIPULATION_TRANSLATION_INERTIA",
    "INTERACTION_CONFIGURATION_FLAG_MANIPULATION_ROTATION_INERTIA",
    "INTERACTION_CONFIGURATION_FLAG_MANIPULATION_SCALING_INERTIA",
    "INTERACTION_CONFIGURATION_FLAG_MANIPULATION_RAILS_X",
    "INTERACTION_CONFIGURATION_FLAG_MANIPULATION_RAILS_Y",
    "INTERACTION_CONFIGURATION_FLAG_MANIPULATION_EXACT",
    "INTERACTION_CONFIGURATION_FLAG_MANIPULATION_MULTIPLE_FINGER_PANNING",
    "INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE",
    "INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_HORIZONTAL",
    "INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_SELECT",
    "INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_SPEED_BUMP",
    "INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_REARRANGE",
    "INTERACTION_CONFIGURATION_FLAG_CROSS_SLIDE_EXACT",
    "INTERACTION_CONFIGURATION_FLAG_TAP",
    "INTERACTION_CONFIGURATION_FLAG_TAP_DOUBLE",
    "INTERACTION_CONFIGURATION_FLAG_TAP_MULTIPLE_FINGER",
    "INTERACTION_CONFIGURATION_FLAG_SECONDARY_TAP",
    "INTERACTION_CONFIGURATION_FLAG_HOLD",
    "INTERACTION_CONFIGURATION_FLAG_HOLD_MOUSE",
    "INTERACTION_CONFIGURATION_FLAG_HOLD_MULTIPLE_FINGER",
    "INTERACTION_CONFIGURATION_FLAG_DRAG",
    "INTERACTION_CONFIGURATION_FLAG_MAX",
    "INERTIA_PARAMETER",
    "INERTIA_PARAMETER_TRANSLATION_DECELERATION",
    "INERTIA_PARAMETER_TRANSLATION_DISPLACEMENT",
    "INERTIA_PARAMETER_ROTATION_DECELERATION",
    "INERTIA_PARAMETER_ROTATION_ANGLE",
    "INERTIA_PARAMETER_EXPANSION_DECELERATION",
    "INERTIA_PARAMETER_EXPANSION_EXPANSION",
    "INERTIA_PARAMETER_MAX",
    "INTERACTION_STATE",
    "INTERACTION_STATE_IDLE",
    "INTERACTION_STATE_IN_INTERACTION",
    "INTERACTION_STATE_POSSIBLE_DOUBLE_TAP",
    "INTERACTION_STATE_MAX",
    "INTERACTION_CONTEXT_PROPERTY",
    "INTERACTION_CONTEXT_PROPERTY_MEASUREMENT_UNITS",
    "INTERACTION_CONTEXT_PROPERTY_INTERACTION_UI_FEEDBACK",
    "INTERACTION_CONTEXT_PROPERTY_FILTER_POINTERS",
    "INTERACTION_CONTEXT_PROPERTY_MAX",
    "CROSS_SLIDE_THRESHOLD",
    "CROSS_SLIDE_THRESHOLD_SELECT_START",
    "CROSS_SLIDE_THRESHOLD_SPEED_BUMP_START",
    "CROSS_SLIDE_THRESHOLD_SPEED_BUMP_END",
    "CROSS_SLIDE_THRESHOLD_REARRANGE_START",
    "CROSS_SLIDE_THRESHOLD_COUNT",
    "CROSS_SLIDE_THRESHOLD_MAX",
    "CROSS_SLIDE_FLAGS",
    "CROSS_SLIDE_FLAGS_NONE",
    "CROSS_SLIDE_FLAGS_SELECT",
    "CROSS_SLIDE_FLAGS_SPEED_BUMP",
    "CROSS_SLIDE_FLAGS_REARRANGE",
    "CROSS_SLIDE_FLAGS_MAX",
    "MOUSE_WHEEL_PARAMETER",
    "MOUSE_WHEEL_PARAMETER_CHAR_TRANSLATION_X",
    "MOUSE_WHEEL_PARAMETER_CHAR_TRANSLATION_Y",
    "MOUSE_WHEEL_PARAMETER_DELTA_SCALE",
    "MOUSE_WHEEL_PARAMETER_DELTA_ROTATION",
    "MOUSE_WHEEL_PARAMETER_PAGE_TRANSLATION_X",
    "MOUSE_WHEEL_PARAMETER_PAGE_TRANSLATION_Y",
    "MOUSE_WHEEL_PARAMETER_MAX",
    "TAP_PARAMETER",
    "TAP_PARAMETER_MIN_CONTACT_COUNT",
    "TAP_PARAMETER_MAX_CONTACT_COUNT",
    "TAP_PARAMETER_MAX",
    "HOLD_PARAMETER",
    "HOLD_PARAMETER_MIN_CONTACT_COUNT",
    "HOLD_PARAMETER_MAX_CONTACT_COUNT",
    "HOLD_PARAMETER_THRESHOLD_RADIUS",
    "HOLD_PARAMETER_THRESHOLD_START_DELAY",
    "HOLD_PARAMETER_MAX",
    "TRANSLATION_PARAMETER",
    "TRANSLATION_PARAMETER_MIN_CONTACT_COUNT",
    "TRANSLATION_PARAMETER_MAX_CONTACT_COUNT",
    "TRANSLATION_PARAMETER_MAX",
    "MANIPULATION_RAILS_STATE",
    "MANIPULATION_RAILS_STATE_UNDECIDED",
    "MANIPULATION_RAILS_STATE_FREE",
    "MANIPULATION_RAILS_STATE_RAILED",
    "MANIPULATION_RAILS_STATE_MAX",
    "MANIPULATION_TRANSFORM",
    "MANIPULATION_VELOCITY",
    "INTERACTION_ARGUMENTS_MANIPULATION",
    "INTERACTION_ARGUMENTS_TAP",
    "INTERACTION_ARGUMENTS_CROSS_SLIDE",
    "INTERACTION_CONTEXT_OUTPUT",
    "INTERACTION_CONTEXT_OUTPUT2",
    "INTERACTION_CONTEXT_CONFIGURATION",
    "CROSS_SLIDE_PARAMETER",
    "INTERACTION_CONTEXT_OUTPUT_CALLBACK",
    "INTERACTION_CONTEXT_OUTPUT_CALLBACK2",
    "CreateInteractionContext",
    "DestroyInteractionContext",
    "RegisterOutputCallbackInteractionContext",
    "RegisterOutputCallbackInteractionContext2",
    "SetInteractionConfigurationInteractionContext",
    "GetInteractionConfigurationInteractionContext",
    "SetPropertyInteractionContext",
    "GetPropertyInteractionContext",
    "SetInertiaParameterInteractionContext",
    "GetInertiaParameterInteractionContext",
    "SetCrossSlideParametersInteractionContext",
    "GetCrossSlideParameterInteractionContext",
    "SetTapParameterInteractionContext",
    "GetTapParameterInteractionContext",
    "SetHoldParameterInteractionContext",
    "GetHoldParameterInteractionContext",
    "SetTranslationParameterInteractionContext",
    "GetTranslationParameterInteractionContext",
    "SetMouseWheelParameterInteractionContext",
    "GetMouseWheelParameterInteractionContext",
    "ResetInteractionContext",
    "GetStateInteractionContext",
    "AddPointerInteractionContext",
    "RemovePointerInteractionContext",
    "ProcessPointerFramesInteractionContext",
    "BufferPointerPacketsInteractionContext",
    "ProcessBufferedPacketsInteractionContext",
    "ProcessInertiaInteractionContext",
    "StopInteractionContext",
    "SetPivotInteractionContext",
]
