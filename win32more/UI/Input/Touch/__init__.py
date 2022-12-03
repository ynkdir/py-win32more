from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.UI.Input.Touch
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
def _define__IManipulationEvents_head():
    class _IManipulationEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('4f62c8da-9c53-4b22-93-df-92-7a-86-2b-bb-03')
    return _IManipulationEvents
def _define__IManipulationEvents():
    _IManipulationEvents = win32more.UI.Input.Touch._IManipulationEvents_head
    _IManipulationEvents.ManipulationStarted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single)(3, 'ManipulationStarted', ((1, 'x'),(1, 'y'),)))
    _IManipulationEvents.ManipulationDelta = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,Single,Single,Single,Single,Single,Single,Single,Single,Single)(4, 'ManipulationDelta', ((1, 'x'),(1, 'y'),(1, 'translationDeltaX'),(1, 'translationDeltaY'),(1, 'scaleDelta'),(1, 'expansionDelta'),(1, 'rotationDelta'),(1, 'cumulativeTranslationX'),(1, 'cumulativeTranslationY'),(1, 'cumulativeScale'),(1, 'cumulativeExpansion'),(1, 'cumulativeRotation'),)))
    _IManipulationEvents.ManipulationCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,Single,Single,Single,Single)(5, 'ManipulationCompleted', ((1, 'x'),(1, 'y'),(1, 'cumulativeTranslationX'),(1, 'cumulativeTranslationY'),(1, 'cumulativeScale'),(1, 'cumulativeExpansion'),(1, 'cumulativeRotation'),)))
    win32more.System.Com.IUnknown
    return _IManipulationEvents
def _define_GetTouchInputInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Input.Touch.HTOUCHINPUT,UInt32,POINTER(win32more.UI.Input.Touch.TOUCHINPUT_head),Int32)(('GetTouchInputInfo', windll['USER32.dll']), ((1, 'hTouchInput'),(1, 'cInputs'),(1, 'pInputs'),(1, 'cbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseTouchInputHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Input.Touch.HTOUCHINPUT)(('CloseTouchInputHandle', windll['USER32.dll']), ((1, 'hTouchInput'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterTouchWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.Input.Touch.REGISTER_TOUCH_WINDOW_FLAGS)(('RegisterTouchWindow', windll['USER32.dll']), ((1, 'hwnd'),(1, 'ulFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterTouchWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND)(('UnregisterTouchWindow', windll['USER32.dll']), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsTouchWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(UInt32))(('IsTouchWindow', windll['USER32.dll']), ((1, 'hwnd'),(1, 'pulFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGestureInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Input.Touch.HGESTUREINFO,POINTER(win32more.UI.Input.Touch.GESTUREINFO_head))(('GetGestureInfo', windll['USER32.dll']), ((1, 'hGestureInfo'),(1, 'pGestureInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGestureExtraArgs():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Input.Touch.HGESTUREINFO,UInt32,c_char_p_no)(('GetGestureExtraArgs', windll['USER32.dll']), ((1, 'hGestureInfo'),(1, 'cbExtraArgs'),(1, 'pExtraArgs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseGestureInfoHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Input.Touch.HGESTUREINFO)(('CloseGestureInfoHandle', windll['USER32.dll']), ((1, 'hGestureInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetGestureConfig():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,UInt32,UInt32,POINTER(win32more.UI.Input.Touch.GESTURECONFIG_head),UInt32)(('SetGestureConfig', windll['USER32.dll']), ((1, 'hwnd'),(1, 'dwReserved'),(1, 'cIDs'),(1, 'pGestureConfig'),(1, 'cbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGestureConfig():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,UInt32,UInt32,POINTER(UInt32),POINTER(win32more.UI.Input.Touch.GESTURECONFIG_head),UInt32)(('GetGestureConfig', windll['USER32.dll']), ((1, 'hwnd'),(1, 'dwReserved'),(1, 'dwFlags'),(1, 'pcIDs'),(1, 'pGestureConfig'),(1, 'cbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GESTURECONFIG_head():
    class GESTURECONFIG(Structure):
        pass
    return GESTURECONFIG
def _define_GESTURECONFIG():
    GESTURECONFIG = win32more.UI.Input.Touch.GESTURECONFIG_head
    GESTURECONFIG._fields_ = [
        ('dwID', win32more.UI.Input.Touch.GESTURECONFIG_ID),
        ('dwWant', UInt32),
        ('dwBlock', UInt32),
    ]
    return GESTURECONFIG
GESTURECONFIG_ID = UInt32
GID_BEGIN = 1
GID_END = 2
GID_ZOOM = 3
GID_PAN = 4
GID_ROTATE = 5
GID_TWOFINGERTAP = 6
GID_PRESSANDTAP = 7
GID_ROLLOVER = 7
def _define_GESTUREINFO_head():
    class GESTUREINFO(Structure):
        pass
    return GESTUREINFO
def _define_GESTUREINFO():
    GESTUREINFO = win32more.UI.Input.Touch.GESTUREINFO_head
    GESTUREINFO._fields_ = [
        ('cbSize', UInt32),
        ('dwFlags', UInt32),
        ('dwID', UInt32),
        ('hwndTarget', win32more.Foundation.HWND),
        ('ptsLocation', win32more.Foundation.POINTS),
        ('dwInstanceID', UInt32),
        ('dwSequenceID', UInt32),
        ('ullArguments', UInt64),
        ('cbExtraArgs', UInt32),
    ]
    return GESTUREINFO
def _define_GESTURENOTIFYSTRUCT_head():
    class GESTURENOTIFYSTRUCT(Structure):
        pass
    return GESTURENOTIFYSTRUCT
def _define_GESTURENOTIFYSTRUCT():
    GESTURENOTIFYSTRUCT = win32more.UI.Input.Touch.GESTURENOTIFYSTRUCT_head
    GESTURENOTIFYSTRUCT._fields_ = [
        ('cbSize', UInt32),
        ('dwFlags', UInt32),
        ('hwndTarget', win32more.Foundation.HWND),
        ('ptsLocation', win32more.Foundation.POINTS),
        ('dwInstanceID', UInt32),
    ]
    return GESTURENOTIFYSTRUCT
HGESTUREINFO = IntPtr
HTOUCHINPUT = IntPtr
def _define_IInertiaProcessor_head():
    class IInertiaProcessor(win32more.System.Com.IUnknown_head):
        Guid = Guid('18b00c6d-c5ee-41b1-90-a9-9d-4a-92-90-95-ad')
    return IInertiaProcessor
def _define_IInertiaProcessor():
    IInertiaProcessor = win32more.UI.Input.Touch.IInertiaProcessor_head
    IInertiaProcessor.get_InitialOriginX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(3, 'get_InitialOriginX', ((1, 'x'),)))
    IInertiaProcessor.put_InitialOriginX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(4, 'put_InitialOriginX', ((1, 'x'),)))
    IInertiaProcessor.get_InitialOriginY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(5, 'get_InitialOriginY', ((1, 'y'),)))
    IInertiaProcessor.put_InitialOriginY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(6, 'put_InitialOriginY', ((1, 'y'),)))
    IInertiaProcessor.get_InitialVelocityX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(7, 'get_InitialVelocityX', ((1, 'x'),)))
    IInertiaProcessor.put_InitialVelocityX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(8, 'put_InitialVelocityX', ((1, 'x'),)))
    IInertiaProcessor.get_InitialVelocityY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(9, 'get_InitialVelocityY', ((1, 'y'),)))
    IInertiaProcessor.put_InitialVelocityY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(10, 'put_InitialVelocityY', ((1, 'y'),)))
    IInertiaProcessor.get_InitialAngularVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(11, 'get_InitialAngularVelocity', ((1, 'velocity'),)))
    IInertiaProcessor.put_InitialAngularVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(12, 'put_InitialAngularVelocity', ((1, 'velocity'),)))
    IInertiaProcessor.get_InitialExpansionVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(13, 'get_InitialExpansionVelocity', ((1, 'velocity'),)))
    IInertiaProcessor.put_InitialExpansionVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(14, 'put_InitialExpansionVelocity', ((1, 'velocity'),)))
    IInertiaProcessor.get_InitialRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(15, 'get_InitialRadius', ((1, 'radius'),)))
    IInertiaProcessor.put_InitialRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(16, 'put_InitialRadius', ((1, 'radius'),)))
    IInertiaProcessor.get_BoundaryLeft = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(17, 'get_BoundaryLeft', ((1, 'left'),)))
    IInertiaProcessor.put_BoundaryLeft = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(18, 'put_BoundaryLeft', ((1, 'left'),)))
    IInertiaProcessor.get_BoundaryTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(19, 'get_BoundaryTop', ((1, 'top'),)))
    IInertiaProcessor.put_BoundaryTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(20, 'put_BoundaryTop', ((1, 'top'),)))
    IInertiaProcessor.get_BoundaryRight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(21, 'get_BoundaryRight', ((1, 'right'),)))
    IInertiaProcessor.put_BoundaryRight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(22, 'put_BoundaryRight', ((1, 'right'),)))
    IInertiaProcessor.get_BoundaryBottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(23, 'get_BoundaryBottom', ((1, 'bottom'),)))
    IInertiaProcessor.put_BoundaryBottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(24, 'put_BoundaryBottom', ((1, 'bottom'),)))
    IInertiaProcessor.get_ElasticMarginLeft = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(25, 'get_ElasticMarginLeft', ((1, 'left'),)))
    IInertiaProcessor.put_ElasticMarginLeft = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(26, 'put_ElasticMarginLeft', ((1, 'left'),)))
    IInertiaProcessor.get_ElasticMarginTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(27, 'get_ElasticMarginTop', ((1, 'top'),)))
    IInertiaProcessor.put_ElasticMarginTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(28, 'put_ElasticMarginTop', ((1, 'top'),)))
    IInertiaProcessor.get_ElasticMarginRight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(29, 'get_ElasticMarginRight', ((1, 'right'),)))
    IInertiaProcessor.put_ElasticMarginRight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(30, 'put_ElasticMarginRight', ((1, 'right'),)))
    IInertiaProcessor.get_ElasticMarginBottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(31, 'get_ElasticMarginBottom', ((1, 'bottom'),)))
    IInertiaProcessor.put_ElasticMarginBottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(32, 'put_ElasticMarginBottom', ((1, 'bottom'),)))
    IInertiaProcessor.get_DesiredDisplacement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(33, 'get_DesiredDisplacement', ((1, 'displacement'),)))
    IInertiaProcessor.put_DesiredDisplacement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(34, 'put_DesiredDisplacement', ((1, 'displacement'),)))
    IInertiaProcessor.get_DesiredRotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(35, 'get_DesiredRotation', ((1, 'rotation'),)))
    IInertiaProcessor.put_DesiredRotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(36, 'put_DesiredRotation', ((1, 'rotation'),)))
    IInertiaProcessor.get_DesiredExpansion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(37, 'get_DesiredExpansion', ((1, 'expansion'),)))
    IInertiaProcessor.put_DesiredExpansion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(38, 'put_DesiredExpansion', ((1, 'expansion'),)))
    IInertiaProcessor.get_DesiredDeceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(39, 'get_DesiredDeceleration', ((1, 'deceleration'),)))
    IInertiaProcessor.put_DesiredDeceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(40, 'put_DesiredDeceleration', ((1, 'deceleration'),)))
    IInertiaProcessor.get_DesiredAngularDeceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(41, 'get_DesiredAngularDeceleration', ((1, 'deceleration'),)))
    IInertiaProcessor.put_DesiredAngularDeceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(42, 'put_DesiredAngularDeceleration', ((1, 'deceleration'),)))
    IInertiaProcessor.get_DesiredExpansionDeceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(43, 'get_DesiredExpansionDeceleration', ((1, 'deceleration'),)))
    IInertiaProcessor.put_DesiredExpansionDeceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(44, 'put_DesiredExpansionDeceleration', ((1, 'deceleration'),)))
    IInertiaProcessor.get_InitialTimestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(45, 'get_InitialTimestamp', ((1, 'timestamp'),)))
    IInertiaProcessor.put_InitialTimestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(46, 'put_InitialTimestamp', ((1, 'timestamp'),)))
    IInertiaProcessor.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(47, 'Reset', ()))
    IInertiaProcessor.Process = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(48, 'Process', ((1, 'completed'),)))
    IInertiaProcessor.ProcessTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL))(49, 'ProcessTime', ((1, 'timestamp'),(1, 'completed'),)))
    IInertiaProcessor.Complete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(50, 'Complete', ()))
    IInertiaProcessor.CompleteTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(51, 'CompleteTime', ((1, 'timestamp'),)))
    win32more.System.Com.IUnknown
    return IInertiaProcessor
def _define_IManipulationProcessor_head():
    class IManipulationProcessor(win32more.System.Com.IUnknown_head):
        Guid = Guid('a22ac519-8300-48a0-be-f4-f1-be-87-37-db-a4')
    return IManipulationProcessor
def _define_IManipulationProcessor():
    IManipulationProcessor = win32more.UI.Input.Touch.IManipulationProcessor_head
    IManipulationProcessor.get_SupportedManipulations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Input.Touch.MANIPULATION_PROCESSOR_MANIPULATIONS))(3, 'get_SupportedManipulations', ((1, 'manipulations'),)))
    IManipulationProcessor.put_SupportedManipulations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Input.Touch.MANIPULATION_PROCESSOR_MANIPULATIONS)(4, 'put_SupportedManipulations', ((1, 'manipulations'),)))
    IManipulationProcessor.get_PivotPointX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(5, 'get_PivotPointX', ((1, 'pivotPointX'),)))
    IManipulationProcessor.put_PivotPointX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(6, 'put_PivotPointX', ((1, 'pivotPointX'),)))
    IManipulationProcessor.get_PivotPointY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(7, 'get_PivotPointY', ((1, 'pivotPointY'),)))
    IManipulationProcessor.put_PivotPointY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(8, 'put_PivotPointY', ((1, 'pivotPointY'),)))
    IManipulationProcessor.get_PivotRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(9, 'get_PivotRadius', ((1, 'pivotRadius'),)))
    IManipulationProcessor.put_PivotRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(10, 'put_PivotRadius', ((1, 'pivotRadius'),)))
    IManipulationProcessor.CompleteManipulation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'CompleteManipulation', ()))
    IManipulationProcessor.ProcessDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,Single)(12, 'ProcessDown', ((1, 'manipulatorId'),(1, 'x'),(1, 'y'),)))
    IManipulationProcessor.ProcessMove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,Single)(13, 'ProcessMove', ((1, 'manipulatorId'),(1, 'x'),(1, 'y'),)))
    IManipulationProcessor.ProcessUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,Single)(14, 'ProcessUp', ((1, 'manipulatorId'),(1, 'x'),(1, 'y'),)))
    IManipulationProcessor.ProcessDownWithTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,Single,UInt32)(15, 'ProcessDownWithTime', ((1, 'manipulatorId'),(1, 'x'),(1, 'y'),(1, 'timestamp'),)))
    IManipulationProcessor.ProcessMoveWithTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,Single,UInt32)(16, 'ProcessMoveWithTime', ((1, 'manipulatorId'),(1, 'x'),(1, 'y'),(1, 'timestamp'),)))
    IManipulationProcessor.ProcessUpWithTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,Single,UInt32)(17, 'ProcessUpWithTime', ((1, 'manipulatorId'),(1, 'x'),(1, 'y'),(1, 'timestamp'),)))
    IManipulationProcessor.GetVelocityX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(18, 'GetVelocityX', ((1, 'velocityX'),)))
    IManipulationProcessor.GetVelocityY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(19, 'GetVelocityY', ((1, 'velocityY'),)))
    IManipulationProcessor.GetExpansionVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(20, 'GetExpansionVelocity', ((1, 'expansionVelocity'),)))
    IManipulationProcessor.GetAngularVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(21, 'GetAngularVelocity', ((1, 'angularVelocity'),)))
    IManipulationProcessor.get_MinimumScaleRotateRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(22, 'get_MinimumScaleRotateRadius', ((1, 'minRadius'),)))
    IManipulationProcessor.put_MinimumScaleRotateRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(23, 'put_MinimumScaleRotateRadius', ((1, 'minRadius'),)))
    win32more.System.Com.IUnknown
    return IManipulationProcessor
InertiaProcessor = Guid('abb27087-4ce0-4e58-a0-cb-e2-4d-f9-68-14-be')
MANIPULATION_PROCESSOR_MANIPULATIONS = Int32
MANIPULATION_NONE = 0
MANIPULATION_TRANSLATE_X = 1
MANIPULATION_TRANSLATE_Y = 2
MANIPULATION_SCALE = 4
MANIPULATION_ROTATE = 8
MANIPULATION_ALL = 15
ManipulationProcessor = Guid('597d4fb0-47fd-4aff-89-b9-c6-cf-ae-8c-f0-8e')
REGISTER_TOUCH_WINDOW_FLAGS = UInt32
TWF_FINETOUCH = 1
TWF_WANTPALM = 2
TOUCHEVENTF_FLAGS = UInt32
TOUCHEVENTF_MOVE = 1
TOUCHEVENTF_DOWN = 2
TOUCHEVENTF_UP = 4
TOUCHEVENTF_INRANGE = 8
TOUCHEVENTF_PRIMARY = 16
TOUCHEVENTF_NOCOALESCE = 32
TOUCHEVENTF_PEN = 64
TOUCHEVENTF_PALM = 128
def _define_TOUCHINPUT_head():
    class TOUCHINPUT(Structure):
        pass
    return TOUCHINPUT
def _define_TOUCHINPUT():
    TOUCHINPUT = win32more.UI.Input.Touch.TOUCHINPUT_head
    TOUCHINPUT._fields_ = [
        ('x', Int32),
        ('y', Int32),
        ('hSource', win32more.Foundation.HANDLE),
        ('dwID', UInt32),
        ('dwFlags', win32more.UI.Input.Touch.TOUCHEVENTF_FLAGS),
        ('dwMask', win32more.UI.Input.Touch.TOUCHINPUTMASKF_MASK),
        ('dwTime', UInt32),
        ('dwExtraInfo', UIntPtr),
        ('cxContact', UInt32),
        ('cyContact', UInt32),
    ]
    return TOUCHINPUT
TOUCHINPUTMASKF_MASK = UInt32
TOUCHINPUTMASKF_TIMEFROMSYSTEM = 1
TOUCHINPUTMASKF_EXTRAINFO = 2
TOUCHINPUTMASKF_CONTACTAREA = 4
__all__ = [
    "CloseGestureInfoHandle",
    "CloseTouchInputHandle",
    "GESTURECONFIG",
    "GESTURECONFIG_ID",
    "GESTUREINFO",
    "GESTURENOTIFYSTRUCT",
    "GID_BEGIN",
    "GID_END",
    "GID_PAN",
    "GID_PRESSANDTAP",
    "GID_ROLLOVER",
    "GID_ROTATE",
    "GID_TWOFINGERTAP",
    "GID_ZOOM",
    "GetGestureConfig",
    "GetGestureExtraArgs",
    "GetGestureInfo",
    "GetTouchInputInfo",
    "HGESTUREINFO",
    "HTOUCHINPUT",
    "IInertiaProcessor",
    "IManipulationProcessor",
    "InertiaProcessor",
    "IsTouchWindow",
    "MANIPULATION_ALL",
    "MANIPULATION_NONE",
    "MANIPULATION_PROCESSOR_MANIPULATIONS",
    "MANIPULATION_ROTATE",
    "MANIPULATION_SCALE",
    "MANIPULATION_TRANSLATE_X",
    "MANIPULATION_TRANSLATE_Y",
    "ManipulationProcessor",
    "REGISTER_TOUCH_WINDOW_FLAGS",
    "RegisterTouchWindow",
    "SetGestureConfig",
    "TOUCHEVENTF_DOWN",
    "TOUCHEVENTF_FLAGS",
    "TOUCHEVENTF_INRANGE",
    "TOUCHEVENTF_MOVE",
    "TOUCHEVENTF_NOCOALESCE",
    "TOUCHEVENTF_PALM",
    "TOUCHEVENTF_PEN",
    "TOUCHEVENTF_PRIMARY",
    "TOUCHEVENTF_UP",
    "TOUCHINPUT",
    "TOUCHINPUTMASKF_CONTACTAREA",
    "TOUCHINPUTMASKF_EXTRAINFO",
    "TOUCHINPUTMASKF_MASK",
    "TOUCHINPUTMASKF_TIMEFROMSYSTEM",
    "TWF_FINETOUCH",
    "TWF_WANTPALM",
    "UnregisterTouchWindow",
    "_IManipulationEvents",
]
