from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.UI.Input.Touch
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
@winfunctype('USER32.dll')
def GetTouchInputInfo(hTouchInput: win32more.UI.Input.Touch.HTOUCHINPUT, cInputs: UInt32, pInputs: POINTER(win32more.UI.Input.Touch.TOUCHINPUT_head), cbSize: Int32) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def CloseTouchInputHandle(hTouchInput: win32more.UI.Input.Touch.HTOUCHINPUT) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def RegisterTouchWindow(hwnd: win32more.Foundation.HWND, ulFlags: win32more.UI.Input.Touch.REGISTER_TOUCH_WINDOW_FLAGS) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def UnregisterTouchWindow(hwnd: win32more.Foundation.HWND) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IsTouchWindow(hwnd: win32more.Foundation.HWND, pulFlags: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetGestureInfo(hGestureInfo: win32more.UI.Input.Touch.HGESTUREINFO, pGestureInfo: POINTER(win32more.UI.Input.Touch.GESTUREINFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetGestureExtraArgs(hGestureInfo: win32more.UI.Input.Touch.HGESTUREINFO, cbExtraArgs: UInt32, pExtraArgs: c_char_p_no) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def CloseGestureInfoHandle(hGestureInfo: win32more.UI.Input.Touch.HGESTUREINFO) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetGestureConfig(hwnd: win32more.Foundation.HWND, dwReserved: UInt32, cIDs: UInt32, pGestureConfig: POINTER(win32more.UI.Input.Touch.GESTURECONFIG_head), cbSize: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetGestureConfig(hwnd: win32more.Foundation.HWND, dwReserved: UInt32, dwFlags: UInt32, pcIDs: POINTER(UInt32), pGestureConfig: POINTER(win32more.UI.Input.Touch.GESTURECONFIG_head), cbSize: UInt32) -> win32more.Foundation.BOOL: ...
class GESTURECONFIG(Structure):
    dwID: win32more.UI.Input.Touch.GESTURECONFIG_ID
    dwWant: UInt32
    dwBlock: UInt32
GESTURECONFIG_ID = UInt32
GID_BEGIN: GESTURECONFIG_ID = 1
GID_END: GESTURECONFIG_ID = 2
GID_ZOOM: GESTURECONFIG_ID = 3
GID_PAN: GESTURECONFIG_ID = 4
GID_ROTATE: GESTURECONFIG_ID = 5
GID_TWOFINGERTAP: GESTURECONFIG_ID = 6
GID_PRESSANDTAP: GESTURECONFIG_ID = 7
GID_ROLLOVER: GESTURECONFIG_ID = 7
class GESTUREINFO(Structure):
    cbSize: UInt32
    dwFlags: UInt32
    dwID: UInt32
    hwndTarget: win32more.Foundation.HWND
    ptsLocation: win32more.Foundation.POINTS
    dwInstanceID: UInt32
    dwSequenceID: UInt32
    ullArguments: UInt64
    cbExtraArgs: UInt32
class GESTURENOTIFYSTRUCT(Structure):
    cbSize: UInt32
    dwFlags: UInt32
    hwndTarget: win32more.Foundation.HWND
    ptsLocation: win32more.Foundation.POINTS
    dwInstanceID: UInt32
HGESTUREINFO = IntPtr
HTOUCHINPUT = IntPtr
class IInertiaProcessor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('18b00c6d-c5ee-41b1-90-a9-9d-4a-92-90-95-ad')
    @commethod(3)
    def get_InitialOriginX(x: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_InitialOriginX(x: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_InitialOriginY(y: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_InitialOriginY(y: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_InitialVelocityX(x: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_InitialVelocityX(x: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_InitialVelocityY(y: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_InitialVelocityY(y: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_InitialAngularVelocity(velocity: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_InitialAngularVelocity(velocity: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_InitialExpansionVelocity(velocity: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_InitialExpansionVelocity(velocity: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_InitialRadius(radius: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_InitialRadius(radius: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_BoundaryLeft(left: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_BoundaryLeft(left: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_BoundaryTop(top: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_BoundaryTop(top: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_BoundaryRight(right: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_BoundaryRight(right: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_BoundaryBottom(bottom: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_BoundaryBottom(bottom: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_ElasticMarginLeft(left: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def put_ElasticMarginLeft(left: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_ElasticMarginTop(top: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_ElasticMarginTop(top: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_ElasticMarginRight(right: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_ElasticMarginRight(right: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_ElasticMarginBottom(bottom: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def put_ElasticMarginBottom(bottom: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_DesiredDisplacement(displacement: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def put_DesiredDisplacement(displacement: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_DesiredRotation(rotation: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def put_DesiredRotation(rotation: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def get_DesiredExpansion(expansion: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def put_DesiredExpansion(expansion: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def get_DesiredDeceleration(deceleration: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def put_DesiredDeceleration(deceleration: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def get_DesiredAngularDeceleration(deceleration: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def put_DesiredAngularDeceleration(deceleration: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def get_DesiredExpansionDeceleration(deceleration: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def put_DesiredExpansionDeceleration(deceleration: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def get_InitialTimestamp(timestamp: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def put_InitialTimestamp(timestamp: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def Process(completed: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def ProcessTime(timestamp: UInt32, completed: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def Complete() -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def CompleteTime(timestamp: UInt32) -> win32more.Foundation.HRESULT: ...
class IManipulationProcessor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a22ac519-8300-48a0-be-f4-f1-be-87-37-db-a4')
    @commethod(3)
    def get_SupportedManipulations(manipulations: POINTER(win32more.UI.Input.Touch.MANIPULATION_PROCESSOR_MANIPULATIONS)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def put_SupportedManipulations(manipulations: win32more.UI.Input.Touch.MANIPULATION_PROCESSOR_MANIPULATIONS) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def get_PivotPointX(pivotPointX: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def put_PivotPointX(pivotPointX: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def get_PivotPointY(pivotPointY: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_PivotPointY(pivotPointY: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_PivotRadius(pivotRadius: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_PivotRadius(pivotRadius: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def CompleteManipulation() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def ProcessDown(manipulatorId: UInt32, x: Single, y: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def ProcessMove(manipulatorId: UInt32, x: Single, y: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def ProcessUp(manipulatorId: UInt32, x: Single, y: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def ProcessDownWithTime(manipulatorId: UInt32, x: Single, y: Single, timestamp: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def ProcessMoveWithTime(manipulatorId: UInt32, x: Single, y: Single, timestamp: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def ProcessUpWithTime(manipulatorId: UInt32, x: Single, y: Single, timestamp: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetVelocityX(velocityX: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetVelocityY(velocityY: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetExpansionVelocity(expansionVelocity: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetAngularVelocity(angularVelocity: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_MinimumScaleRotateRadius(minRadius: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def put_MinimumScaleRotateRadius(minRadius: Single) -> win32more.Foundation.HRESULT: ...
InertiaProcessor = Guid('abb27087-4ce0-4e58-a0-cb-e2-4d-f9-68-14-be')
MANIPULATION_PROCESSOR_MANIPULATIONS = Int32
MANIPULATION_NONE: MANIPULATION_PROCESSOR_MANIPULATIONS = 0
MANIPULATION_TRANSLATE_X: MANIPULATION_PROCESSOR_MANIPULATIONS = 1
MANIPULATION_TRANSLATE_Y: MANIPULATION_PROCESSOR_MANIPULATIONS = 2
MANIPULATION_SCALE: MANIPULATION_PROCESSOR_MANIPULATIONS = 4
MANIPULATION_ROTATE: MANIPULATION_PROCESSOR_MANIPULATIONS = 8
MANIPULATION_ALL: MANIPULATION_PROCESSOR_MANIPULATIONS = 15
ManipulationProcessor = Guid('597d4fb0-47fd-4aff-89-b9-c6-cf-ae-8c-f0-8e')
REGISTER_TOUCH_WINDOW_FLAGS = UInt32
TWF_FINETOUCH: REGISTER_TOUCH_WINDOW_FLAGS = 1
TWF_WANTPALM: REGISTER_TOUCH_WINDOW_FLAGS = 2
TOUCHEVENTF_FLAGS = UInt32
TOUCHEVENTF_MOVE: TOUCHEVENTF_FLAGS = 1
TOUCHEVENTF_DOWN: TOUCHEVENTF_FLAGS = 2
TOUCHEVENTF_UP: TOUCHEVENTF_FLAGS = 4
TOUCHEVENTF_INRANGE: TOUCHEVENTF_FLAGS = 8
TOUCHEVENTF_PRIMARY: TOUCHEVENTF_FLAGS = 16
TOUCHEVENTF_NOCOALESCE: TOUCHEVENTF_FLAGS = 32
TOUCHEVENTF_PEN: TOUCHEVENTF_FLAGS = 64
TOUCHEVENTF_PALM: TOUCHEVENTF_FLAGS = 128
class TOUCHINPUT(Structure):
    x: Int32
    y: Int32
    hSource: win32more.Foundation.HANDLE
    dwID: UInt32
    dwFlags: win32more.UI.Input.Touch.TOUCHEVENTF_FLAGS
    dwMask: win32more.UI.Input.Touch.TOUCHINPUTMASKF_MASK
    dwTime: UInt32
    dwExtraInfo: UIntPtr
    cxContact: UInt32
    cyContact: UInt32
TOUCHINPUTMASKF_MASK = UInt32
TOUCHINPUTMASKF_TIMEFROMSYSTEM: TOUCHINPUTMASKF_MASK = 1
TOUCHINPUTMASKF_EXTRAINFO: TOUCHINPUTMASKF_MASK = 2
TOUCHINPUTMASKF_CONTACTAREA: TOUCHINPUTMASKF_MASK = 4
class _IManipulationEvents(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4f62c8da-9c53-4b22-93-df-92-7a-86-2b-bb-03')
    @commethod(3)
    def ManipulationStarted(x: Single, y: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ManipulationDelta(x: Single, y: Single, translationDeltaX: Single, translationDeltaY: Single, scaleDelta: Single, expansionDelta: Single, rotationDelta: Single, cumulativeTranslationX: Single, cumulativeTranslationY: Single, cumulativeScale: Single, cumulativeExpansion: Single, cumulativeRotation: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ManipulationCompleted(x: Single, y: Single, cumulativeTranslationX: Single, cumulativeTranslationY: Single, cumulativeScale: Single, cumulativeExpansion: Single, cumulativeRotation: Single) -> win32more.Foundation.HRESULT: ...
make_head(_module, 'GESTURECONFIG')
make_head(_module, 'GESTUREINFO')
make_head(_module, 'GESTURENOTIFYSTRUCT')
make_head(_module, 'IInertiaProcessor')
make_head(_module, 'IManipulationProcessor')
make_head(_module, 'TOUCHINPUT')
make_head(_module, '_IManipulationEvents')
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
_arch_optional = [
]
