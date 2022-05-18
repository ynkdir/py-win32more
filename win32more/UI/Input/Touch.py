from win32more import *
import win32more.Foundation
import win32more.System.Com
import win32more.UI.Input.Touch

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
GESTURECONFIG_ID = UInt32
GID_BEGIN = 1
GID_END = 2
GID_ZOOM = 3
GID_PAN = 4
GID_ROTATE = 5
GID_TWOFINGERTAP = 6
GID_PRESSANDTAP = 7
GID_ROLLOVER = 7
TOUCHEVENTF_FLAGS = UInt32
TOUCHEVENTF_MOVE = 1
TOUCHEVENTF_DOWN = 2
TOUCHEVENTF_UP = 4
TOUCHEVENTF_INRANGE = 8
TOUCHEVENTF_PRIMARY = 16
TOUCHEVENTF_NOCOALESCE = 32
TOUCHEVENTF_PEN = 64
TOUCHEVENTF_PALM = 128
TOUCHINPUTMASKF_MASK = UInt32
TOUCHINPUTMASKF_TIMEFROMSYSTEM = 1
TOUCHINPUTMASKF_EXTRAINFO = 2
TOUCHINPUTMASKF_CONTACTAREA = 4
REGISTER_TOUCH_WINDOW_FLAGS = UInt32
TWF_FINETOUCH = 1
TWF_WANTPALM = 2
HGESTUREINFO = IntPtr
HTOUCHINPUT = IntPtr
InertiaProcessor = Guid('abb27087-4ce0-4e58-a0cb-e24df96814be')
ManipulationProcessor = Guid('597d4fb0-47fd-4aff-89b9-c6cfae8cf08e')
MANIPULATION_PROCESSOR_MANIPULATIONS = Int32
MANIPULATION_NONE = 0
MANIPULATION_TRANSLATE_X = 1
MANIPULATION_TRANSLATE_Y = 2
MANIPULATION_SCALE = 4
MANIPULATION_ROTATE = 8
MANIPULATION_ALL = 15
def _define__IManipulationEvents_head():
    class _IManipulationEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('4f62c8da-9c53-4b22-93df-927a862bbb03')
    return _IManipulationEvents
def _define__IManipulationEvents():
    _IManipulationEvents = win32more.UI.Input.Touch._IManipulationEvents_head
    _IManipulationEvents.ManipulationStarted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single, use_last_error=False)(3, 'ManipulationStarted', ((1, 'x'),(1, 'y'),)))
    _IManipulationEvents.ManipulationDelta = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,Single,Single,Single,Single,Single,Single,Single,Single,Single, use_last_error=False)(4, 'ManipulationDelta', ((1, 'x'),(1, 'y'),(1, 'translationDeltaX'),(1, 'translationDeltaY'),(1, 'scaleDelta'),(1, 'expansionDelta'),(1, 'rotationDelta'),(1, 'cumulativeTranslationX'),(1, 'cumulativeTranslationY'),(1, 'cumulativeScale'),(1, 'cumulativeExpansion'),(1, 'cumulativeRotation'),)))
    _IManipulationEvents.ManipulationCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,Single,Single,Single,Single, use_last_error=False)(5, 'ManipulationCompleted', ((1, 'x'),(1, 'y'),(1, 'cumulativeTranslationX'),(1, 'cumulativeTranslationY'),(1, 'cumulativeScale'),(1, 'cumulativeExpansion'),(1, 'cumulativeRotation'),)))
    return _IManipulationEvents
def _define_IInertiaProcessor_head():
    class IInertiaProcessor(win32more.System.Com.IUnknown_head):
        Guid = Guid('18b00c6d-c5ee-41b1-90a9-9d4a929095ad')
    return IInertiaProcessor
def _define_IInertiaProcessor():
    IInertiaProcessor = win32more.UI.Input.Touch.IInertiaProcessor_head
    IInertiaProcessor.get_InitialOriginX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(3, 'get_InitialOriginX', ((1, 'x'),)))
    IInertiaProcessor.put_InitialOriginX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(4, 'put_InitialOriginX', ((1, 'x'),)))
    IInertiaProcessor.get_InitialOriginY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(5, 'get_InitialOriginY', ((1, 'y'),)))
    IInertiaProcessor.put_InitialOriginY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(6, 'put_InitialOriginY', ((1, 'y'),)))
    IInertiaProcessor.get_InitialVelocityX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(7, 'get_InitialVelocityX', ((1, 'x'),)))
    IInertiaProcessor.put_InitialVelocityX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(8, 'put_InitialVelocityX', ((1, 'x'),)))
    IInertiaProcessor.get_InitialVelocityY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(9, 'get_InitialVelocityY', ((1, 'y'),)))
    IInertiaProcessor.put_InitialVelocityY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(10, 'put_InitialVelocityY', ((1, 'y'),)))
    IInertiaProcessor.get_InitialAngularVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(11, 'get_InitialAngularVelocity', ((1, 'velocity'),)))
    IInertiaProcessor.put_InitialAngularVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(12, 'put_InitialAngularVelocity', ((1, 'velocity'),)))
    IInertiaProcessor.get_InitialExpansionVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(13, 'get_InitialExpansionVelocity', ((1, 'velocity'),)))
    IInertiaProcessor.put_InitialExpansionVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(14, 'put_InitialExpansionVelocity', ((1, 'velocity'),)))
    IInertiaProcessor.get_InitialRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(15, 'get_InitialRadius', ((1, 'radius'),)))
    IInertiaProcessor.put_InitialRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(16, 'put_InitialRadius', ((1, 'radius'),)))
    IInertiaProcessor.get_BoundaryLeft = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(17, 'get_BoundaryLeft', ((1, 'left'),)))
    IInertiaProcessor.put_BoundaryLeft = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(18, 'put_BoundaryLeft', ((1, 'left'),)))
    IInertiaProcessor.get_BoundaryTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(19, 'get_BoundaryTop', ((1, 'top'),)))
    IInertiaProcessor.put_BoundaryTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(20, 'put_BoundaryTop', ((1, 'top'),)))
    IInertiaProcessor.get_BoundaryRight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(21, 'get_BoundaryRight', ((1, 'right'),)))
    IInertiaProcessor.put_BoundaryRight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(22, 'put_BoundaryRight', ((1, 'right'),)))
    IInertiaProcessor.get_BoundaryBottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(23, 'get_BoundaryBottom', ((1, 'bottom'),)))
    IInertiaProcessor.put_BoundaryBottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(24, 'put_BoundaryBottom', ((1, 'bottom'),)))
    IInertiaProcessor.get_ElasticMarginLeft = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(25, 'get_ElasticMarginLeft', ((1, 'left'),)))
    IInertiaProcessor.put_ElasticMarginLeft = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(26, 'put_ElasticMarginLeft', ((1, 'left'),)))
    IInertiaProcessor.get_ElasticMarginTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(27, 'get_ElasticMarginTop', ((1, 'top'),)))
    IInertiaProcessor.put_ElasticMarginTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(28, 'put_ElasticMarginTop', ((1, 'top'),)))
    IInertiaProcessor.get_ElasticMarginRight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(29, 'get_ElasticMarginRight', ((1, 'right'),)))
    IInertiaProcessor.put_ElasticMarginRight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(30, 'put_ElasticMarginRight', ((1, 'right'),)))
    IInertiaProcessor.get_ElasticMarginBottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(31, 'get_ElasticMarginBottom', ((1, 'bottom'),)))
    IInertiaProcessor.put_ElasticMarginBottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(32, 'put_ElasticMarginBottom', ((1, 'bottom'),)))
    IInertiaProcessor.get_DesiredDisplacement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(33, 'get_DesiredDisplacement', ((1, 'displacement'),)))
    IInertiaProcessor.put_DesiredDisplacement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(34, 'put_DesiredDisplacement', ((1, 'displacement'),)))
    IInertiaProcessor.get_DesiredRotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(35, 'get_DesiredRotation', ((1, 'rotation'),)))
    IInertiaProcessor.put_DesiredRotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(36, 'put_DesiredRotation', ((1, 'rotation'),)))
    IInertiaProcessor.get_DesiredExpansion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(37, 'get_DesiredExpansion', ((1, 'expansion'),)))
    IInertiaProcessor.put_DesiredExpansion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(38, 'put_DesiredExpansion', ((1, 'expansion'),)))
    IInertiaProcessor.get_DesiredDeceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(39, 'get_DesiredDeceleration', ((1, 'deceleration'),)))
    IInertiaProcessor.put_DesiredDeceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(40, 'put_DesiredDeceleration', ((1, 'deceleration'),)))
    IInertiaProcessor.get_DesiredAngularDeceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(41, 'get_DesiredAngularDeceleration', ((1, 'deceleration'),)))
    IInertiaProcessor.put_DesiredAngularDeceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(42, 'put_DesiredAngularDeceleration', ((1, 'deceleration'),)))
    IInertiaProcessor.get_DesiredExpansionDeceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(43, 'get_DesiredExpansionDeceleration', ((1, 'deceleration'),)))
    IInertiaProcessor.put_DesiredExpansionDeceleration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(44, 'put_DesiredExpansionDeceleration', ((1, 'deceleration'),)))
    IInertiaProcessor.get_InitialTimestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(45, 'get_InitialTimestamp', ((1, 'timestamp'),)))
    IInertiaProcessor.put_InitialTimestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(46, 'put_InitialTimestamp', ((1, 'timestamp'),)))
    IInertiaProcessor.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(47, 'Reset', ()))
    IInertiaProcessor.Process = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(48, 'Process', ((1, 'completed'),)))
    IInertiaProcessor.ProcessTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(49, 'ProcessTime', ((1, 'timestamp'),(1, 'completed'),)))
    IInertiaProcessor.Complete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(50, 'Complete', ()))
    IInertiaProcessor.CompleteTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(51, 'CompleteTime', ((1, 'timestamp'),)))
    return IInertiaProcessor
def _define_IManipulationProcessor_head():
    class IManipulationProcessor(win32more.System.Com.IUnknown_head):
        Guid = Guid('a22ac519-8300-48a0-bef4-f1be8737dba4')
    return IManipulationProcessor
def _define_IManipulationProcessor():
    IManipulationProcessor = win32more.UI.Input.Touch.IManipulationProcessor_head
    IManipulationProcessor.get_SupportedManipulations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Input.Touch.MANIPULATION_PROCESSOR_MANIPULATIONS), use_last_error=False)(3, 'get_SupportedManipulations', ((1, 'manipulations'),)))
    IManipulationProcessor.put_SupportedManipulations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Input.Touch.MANIPULATION_PROCESSOR_MANIPULATIONS, use_last_error=False)(4, 'put_SupportedManipulations', ((1, 'manipulations'),)))
    IManipulationProcessor.get_PivotPointX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(5, 'get_PivotPointX', ((1, 'pivotPointX'),)))
    IManipulationProcessor.put_PivotPointX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(6, 'put_PivotPointX', ((1, 'pivotPointX'),)))
    IManipulationProcessor.get_PivotPointY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(7, 'get_PivotPointY', ((1, 'pivotPointY'),)))
    IManipulationProcessor.put_PivotPointY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(8, 'put_PivotPointY', ((1, 'pivotPointY'),)))
    IManipulationProcessor.get_PivotRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(9, 'get_PivotRadius', ((1, 'pivotRadius'),)))
    IManipulationProcessor.put_PivotRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(10, 'put_PivotRadius', ((1, 'pivotRadius'),)))
    IManipulationProcessor.CompleteManipulation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'CompleteManipulation', ()))
    IManipulationProcessor.ProcessDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,Single, use_last_error=False)(12, 'ProcessDown', ((1, 'manipulatorId'),(1, 'x'),(1, 'y'),)))
    IManipulationProcessor.ProcessMove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,Single, use_last_error=False)(13, 'ProcessMove', ((1, 'manipulatorId'),(1, 'x'),(1, 'y'),)))
    IManipulationProcessor.ProcessUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,Single, use_last_error=False)(14, 'ProcessUp', ((1, 'manipulatorId'),(1, 'x'),(1, 'y'),)))
    IManipulationProcessor.ProcessDownWithTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,Single,UInt32, use_last_error=False)(15, 'ProcessDownWithTime', ((1, 'manipulatorId'),(1, 'x'),(1, 'y'),(1, 'timestamp'),)))
    IManipulationProcessor.ProcessMoveWithTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,Single,UInt32, use_last_error=False)(16, 'ProcessMoveWithTime', ((1, 'manipulatorId'),(1, 'x'),(1, 'y'),(1, 'timestamp'),)))
    IManipulationProcessor.ProcessUpWithTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Single,Single,UInt32, use_last_error=False)(17, 'ProcessUpWithTime', ((1, 'manipulatorId'),(1, 'x'),(1, 'y'),(1, 'timestamp'),)))
    IManipulationProcessor.GetVelocityX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(18, 'GetVelocityX', ((1, 'velocityX'),)))
    IManipulationProcessor.GetVelocityY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(19, 'GetVelocityY', ((1, 'velocityY'),)))
    IManipulationProcessor.GetExpansionVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(20, 'GetExpansionVelocity', ((1, 'expansionVelocity'),)))
    IManipulationProcessor.GetAngularVelocity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(21, 'GetAngularVelocity', ((1, 'angularVelocity'),)))
    IManipulationProcessor.get_MinimumScaleRotateRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(22, 'get_MinimumScaleRotateRadius', ((1, 'minRadius'),)))
    IManipulationProcessor.put_MinimumScaleRotateRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(23, 'put_MinimumScaleRotateRadius', ((1, 'minRadius'),)))
    return IManipulationProcessor
def _define_TOUCHINPUT_head():
    class TOUCHINPUT(Structure):
        pass
    return TOUCHINPUT
def _define_TOUCHINPUT():
    TOUCHINPUT = win32more.UI.Input.Touch.TOUCHINPUT_head
    TOUCHINPUT._fields_ = [
        ("x", Int32),
        ("y", Int32),
        ("hSource", win32more.Foundation.HANDLE),
        ("dwID", UInt32),
        ("dwFlags", win32more.UI.Input.Touch.TOUCHEVENTF_FLAGS),
        ("dwMask", win32more.UI.Input.Touch.TOUCHINPUTMASKF_MASK),
        ("dwTime", UInt32),
        ("dwExtraInfo", UIntPtr),
        ("cxContact", UInt32),
        ("cyContact", UInt32),
    ]
    return TOUCHINPUT
def _define_GESTUREINFO_head():
    class GESTUREINFO(Structure):
        pass
    return GESTUREINFO
def _define_GESTUREINFO():
    GESTUREINFO = win32more.UI.Input.Touch.GESTUREINFO_head
    GESTUREINFO._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", UInt32),
        ("dwID", UInt32),
        ("hwndTarget", win32more.Foundation.HWND),
        ("ptsLocation", win32more.Foundation.POINTS),
        ("dwInstanceID", UInt32),
        ("dwSequenceID", UInt32),
        ("ullArguments", UInt64),
        ("cbExtraArgs", UInt32),
    ]
    return GESTUREINFO
def _define_GESTURENOTIFYSTRUCT_head():
    class GESTURENOTIFYSTRUCT(Structure):
        pass
    return GESTURENOTIFYSTRUCT
def _define_GESTURENOTIFYSTRUCT():
    GESTURENOTIFYSTRUCT = win32more.UI.Input.Touch.GESTURENOTIFYSTRUCT_head
    GESTURENOTIFYSTRUCT._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", UInt32),
        ("hwndTarget", win32more.Foundation.HWND),
        ("ptsLocation", win32more.Foundation.POINTS),
        ("dwInstanceID", UInt32),
    ]
    return GESTURENOTIFYSTRUCT
def _define_GESTURECONFIG_head():
    class GESTURECONFIG(Structure):
        pass
    return GESTURECONFIG
def _define_GESTURECONFIG():
    GESTURECONFIG = win32more.UI.Input.Touch.GESTURECONFIG_head
    GESTURECONFIG._fields_ = [
        ("dwID", win32more.UI.Input.Touch.GESTURECONFIG_ID),
        ("dwWant", UInt32),
        ("dwBlock", UInt32),
    ]
    return GESTURECONFIG
def _define_GetTouchInputInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Input.Touch.HTOUCHINPUT,UInt32,POINTER(win32more.UI.Input.Touch.TOUCHINPUT),Int32, use_last_error=True)(("GetTouchInputInfo", windll["USER32"]), ((1, 'hTouchInput'),(1, 'cInputs'),(1, 'pInputs'),(1, 'cbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseTouchInputHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Input.Touch.HTOUCHINPUT, use_last_error=True)(("CloseTouchInputHandle", windll["USER32"]), ((1, 'hTouchInput'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterTouchWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.Input.Touch.REGISTER_TOUCH_WINDOW_FLAGS, use_last_error=True)(("RegisterTouchWindow", windll["USER32"]), ((1, 'hwnd'),(1, 'ulFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterTouchWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND, use_last_error=True)(("UnregisterTouchWindow", windll["USER32"]), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsTouchWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(UInt32), use_last_error=False)(("IsTouchWindow", windll["USER32"]), ((1, 'hwnd'),(1, 'pulFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGestureInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Input.Touch.HGESTUREINFO,POINTER(win32more.UI.Input.Touch.GESTUREINFO_head), use_last_error=True)(("GetGestureInfo", windll["USER32"]), ((1, 'hGestureInfo'),(1, 'pGestureInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGestureExtraArgs():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Input.Touch.HGESTUREINFO,UInt32,c_char_p_no, use_last_error=True)(("GetGestureExtraArgs", windll["USER32"]), ((1, 'hGestureInfo'),(1, 'cbExtraArgs'),(1, 'pExtraArgs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseGestureInfoHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Input.Touch.HGESTUREINFO, use_last_error=True)(("CloseGestureInfoHandle", windll["USER32"]), ((1, 'hGestureInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetGestureConfig():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,UInt32,UInt32,POINTER(win32more.UI.Input.Touch.GESTURECONFIG),UInt32, use_last_error=True)(("SetGestureConfig", windll["USER32"]), ((1, 'hwnd'),(1, 'dwReserved'),(1, 'cIDs'),(1, 'pGestureConfig'),(1, 'cbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGestureConfig():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,UInt32,UInt32,POINTER(UInt32),POINTER(win32more.UI.Input.Touch.GESTURECONFIG),UInt32, use_last_error=True)(("GetGestureConfig", windll["USER32"]), ((1, 'hwnd'),(1, 'dwReserved'),(1, 'dwFlags'),(1, 'pcIDs'),(1, 'pGestureConfig'),(1, 'cbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "GESTURECONFIG_ID",
    "GID_BEGIN",
    "GID_END",
    "GID_ZOOM",
    "GID_PAN",
    "GID_ROTATE",
    "GID_TWOFINGERTAP",
    "GID_PRESSANDTAP",
    "GID_ROLLOVER",
    "TOUCHEVENTF_FLAGS",
    "TOUCHEVENTF_MOVE",
    "TOUCHEVENTF_DOWN",
    "TOUCHEVENTF_UP",
    "TOUCHEVENTF_INRANGE",
    "TOUCHEVENTF_PRIMARY",
    "TOUCHEVENTF_NOCOALESCE",
    "TOUCHEVENTF_PEN",
    "TOUCHEVENTF_PALM",
    "TOUCHINPUTMASKF_MASK",
    "TOUCHINPUTMASKF_TIMEFROMSYSTEM",
    "TOUCHINPUTMASKF_EXTRAINFO",
    "TOUCHINPUTMASKF_CONTACTAREA",
    "REGISTER_TOUCH_WINDOW_FLAGS",
    "TWF_FINETOUCH",
    "TWF_WANTPALM",
    "HGESTUREINFO",
    "HTOUCHINPUT",
    "InertiaProcessor",
    "ManipulationProcessor",
    "MANIPULATION_PROCESSOR_MANIPULATIONS",
    "MANIPULATION_NONE",
    "MANIPULATION_TRANSLATE_X",
    "MANIPULATION_TRANSLATE_Y",
    "MANIPULATION_SCALE",
    "MANIPULATION_ROTATE",
    "MANIPULATION_ALL",
    "_IManipulationEvents",
    "IInertiaProcessor",
    "IManipulationProcessor",
    "TOUCHINPUT",
    "GESTUREINFO",
    "GESTURENOTIFYSTRUCT",
    "GESTURECONFIG",
    "GetTouchInputInfo",
    "CloseTouchInputHandle",
    "RegisterTouchWindow",
    "UnregisterTouchWindow",
    "IsTouchWindow",
    "GetGestureInfo",
    "GetGestureExtraArgs",
    "CloseGestureInfoHandle",
    "SetGestureConfig",
    "GetGestureConfig",
]
