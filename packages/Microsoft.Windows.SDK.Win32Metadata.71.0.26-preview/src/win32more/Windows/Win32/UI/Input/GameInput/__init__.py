from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.Input.GameInput
FACILITY_GAMEINPUT: UInt32 = 906
GAMEINPUT_E_DEVICE_DISCONNECTED: win32more.Windows.Win32.Foundation.HRESULT = -2088108031
GAMEINPUT_E_DEVICE_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2088108030
GAMEINPUT_E_READING_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2088108029
GAMEINPUT_E_REFERENCE_READING_TOO_OLD: win32more.Windows.Win32.Foundation.HRESULT = -2088108028
GAMEINPUT_E_TIMESTAMP_OUT_OF_RANGE: win32more.Windows.Win32.Foundation.HRESULT = -2088108027
GAMEINPUT_E_INSUFFICIENT_FORCE_FEEDBACK_RESOURCES: win32more.Windows.Win32.Foundation.HRESULT = -2088108026
@winfunctype('GameInput.dll')
def GameInputCreate(gameInput: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInput)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
GameInputArcadeStickButtons = Int32
GameInputArcadeStickNone: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 0
GameInputArcadeStickMenu: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 1
GameInputArcadeStickView: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 2
GameInputArcadeStickUp: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 4
GameInputArcadeStickDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 8
GameInputArcadeStickLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 16
GameInputArcadeStickRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 32
GameInputArcadeStickAction1: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 64
GameInputArcadeStickAction2: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 128
GameInputArcadeStickAction3: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 256
GameInputArcadeStickAction4: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 512
GameInputArcadeStickAction5: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 1024
GameInputArcadeStickAction6: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 2048
GameInputArcadeStickSpecial1: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 4096
GameInputArcadeStickSpecial2: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons = 8192
class GameInputArcadeStickInfo(Structure):
    menuButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    viewButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    stickUpLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    stickDownLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    stickLeftLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    stickRightLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    actionButton1Label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    actionButton2Label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    actionButton3Label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    actionButton4Label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    actionButton5Label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    actionButton6Label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    specialButton1Label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    specialButton2Label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
class GameInputArcadeStickState(Structure):
    buttons: win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickButtons
class GameInputBatteryState(Structure):
    chargeRate: Single
    maxChargeRate: Single
    remainingCapacity: Single
    fullChargeCapacity: Single
    status: win32more.Windows.Win32.UI.Input.GameInput.GameInputBatteryStatus
GameInputBatteryStatus = Int32
GameInputBatteryUnknown: win32more.Windows.Win32.UI.Input.GameInput.GameInputBatteryStatus = -1
GameInputBatteryNotPresent: win32more.Windows.Win32.UI.Input.GameInput.GameInputBatteryStatus = 0
GameInputBatteryDischarging: win32more.Windows.Win32.UI.Input.GameInput.GameInputBatteryStatus = 1
GameInputBatteryIdle: win32more.Windows.Win32.UI.Input.GameInput.GameInputBatteryStatus = 2
GameInputBatteryCharging: win32more.Windows.Win32.UI.Input.GameInput.GameInputBatteryStatus = 3
class GameInputControllerAxisInfo(Structure):
    mappedInputKinds: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind
    label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    isContinuous: Byte
    isNonlinear: Byte
    isQuantized: Byte
    hasRestValue: Byte
    restValue: Single
    resolution: UInt64
    legacyDInputIndex: UInt16
    legacyHidIndex: UInt16
    rawReportIndex: UInt32
    inputReport: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportInfo)
    inputReportItem: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemInfo)
class GameInputControllerButtonInfo(Structure):
    mappedInputKinds: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind
    label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    legacyDInputIndex: UInt16
    legacyHidIndex: UInt16
    rawReportIndex: UInt32
    inputReport: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportInfo)
    inputReportItem: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemInfo)
class GameInputControllerSwitchInfo(Structure):
    mappedInputKinds: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind
    label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    positionLabels: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel * 9
    kind: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchKind
    legacyDInputIndex: UInt16
    legacyHidIndex: UInt16
    rawReportIndex: UInt32
    inputReport: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportInfo)
    inputReportItem: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemInfo)
@winfunctype_pointer
def GameInputDeviceCallback(callbackToken: UInt64, context: VoidPtr, device: win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice, timestamp: UInt64, currentStatus: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus, previousStatus: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus) -> Void: ...
GameInputDeviceCapabilities = Int32
GameInputDeviceCapabilityNone: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceCapabilities = 0
GameInputDeviceCapabilityAudio: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceCapabilities = 1
GameInputDeviceCapabilityPluginModule: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceCapabilities = 2
GameInputDeviceCapabilityPowerOff: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceCapabilities = 4
GameInputDeviceCapabilitySynchronization: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceCapabilities = 8
GameInputDeviceCapabilityWireless: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceCapabilities = 16
GameInputDeviceFamily = Int32
GameInputFamilyVirtual: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceFamily = -1
GameInputFamilyAggregate: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceFamily = 0
GameInputFamilyXboxOne: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceFamily = 1
GameInputFamilyXbox360: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceFamily = 2
GameInputFamilyHid: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceFamily = 3
GameInputFamilyI8042: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceFamily = 4
class GameInputDeviceInfo(Structure):
    infoSize: UInt32
    vendorId: UInt16
    productId: UInt16
    revisionNumber: UInt16
    interfaceNumber: Byte
    collectionNumber: Byte
    usage: win32more.Windows.Win32.UI.Input.GameInput.GameInputUsage
    hardwareVersion: win32more.Windows.Win32.UI.Input.GameInput.GameInputVersion
    firmwareVersion: win32more.Windows.Win32.UI.Input.GameInput.GameInputVersion
    deviceId: win32more.Windows.Win32.Foundation.APP_LOCAL_DEVICE_ID
    deviceRootId: win32more.Windows.Win32.Foundation.APP_LOCAL_DEVICE_ID
    deviceFamily: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceFamily
    capabilities: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceCapabilities
    supportedInput: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind
    supportedRumbleMotors: win32more.Windows.Win32.UI.Input.GameInput.GameInputRumbleMotors
    inputReportCount: UInt32
    outputReportCount: UInt32
    featureReportCount: UInt32
    controllerAxisCount: UInt32
    controllerButtonCount: UInt32
    controllerSwitchCount: UInt32
    touchPointCount: UInt32
    touchSensorCount: UInt32
    forceFeedbackMotorCount: UInt32
    hapticFeedbackMotorCount: UInt32
    deviceStringCount: UInt32
    deviceDescriptorSize: UInt32
    inputReportInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportInfo)
    outputReportInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportInfo)
    featureReportInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportInfo)
    controllerAxisInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputControllerAxisInfo)
    controllerButtonInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputControllerButtonInfo)
    controllerSwitchInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputControllerSwitchInfo)
    keyboardInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputKeyboardInfo)
    mouseInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputMouseInfo)
    touchSensorInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputTouchSensorInfo)
    motionInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputMotionInfo)
    arcadeStickInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickInfo)
    flightStickInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputFlightStickInfo)
    gamepadInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadInfo)
    racingWheelInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRacingWheelInfo)
    uiNavigationInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationInfo)
    forceFeedbackMotorInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackMotorInfo)
    hapticFeedbackMotorInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputHapticFeedbackMotorInfo)
    displayName: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputString)
    deviceStrings: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputString)
    deviceDescriptorData: VoidPtr
    supportedSystemButtons: win32more.Windows.Win32.UI.Input.GameInput.GameInputSystemButtons
GameInputDeviceStatus = Int32
GameInputDeviceNoStatus: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus = 0
GameInputDeviceConnected: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus = 1
GameInputDeviceInputEnabled: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus = 2
GameInputDeviceOutputEnabled: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus = 4
GameInputDeviceRawIoEnabled: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus = 8
GameInputDeviceAudioCapture: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus = 16
GameInputDeviceAudioRender: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus = 32
GameInputDeviceSynchronized: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus = 64
GameInputDeviceWireless: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus = 128
GameInputDeviceUserIdle: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus = 1048576
GameInputDeviceAnyStatus: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus = 16777215
GameInputEnumerationKind = Int32
GameInputNoEnumeration: win32more.Windows.Win32.UI.Input.GameInput.GameInputEnumerationKind = 0
GameInputAsyncEnumeration: win32more.Windows.Win32.UI.Input.GameInput.GameInputEnumerationKind = 1
GameInputBlockingEnumeration: win32more.Windows.Win32.UI.Input.GameInput.GameInputEnumerationKind = 2
GameInputFeedbackAxes = Int32
GameInputFeedbackAxisNone: win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackAxes = 0
GameInputFeedbackAxisLinearX: win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackAxes = 1
GameInputFeedbackAxisLinearY: win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackAxes = 2
GameInputFeedbackAxisLinearZ: win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackAxes = 4
GameInputFeedbackAxisAngularX: win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackAxes = 8
GameInputFeedbackAxisAngularY: win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackAxes = 16
GameInputFeedbackAxisAngularZ: win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackAxes = 32
GameInputFeedbackAxisNormal: win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackAxes = 64
GameInputFeedbackEffectState = Int32
GameInputFeedbackStopped: win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackEffectState = 0
GameInputFeedbackRunning: win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackEffectState = 1
GameInputFeedbackPaused: win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackEffectState = 2
GameInputFlightStickButtons = Int32
GameInputFlightStickNone: win32more.Windows.Win32.UI.Input.GameInput.GameInputFlightStickButtons = 0
GameInputFlightStickMenu: win32more.Windows.Win32.UI.Input.GameInput.GameInputFlightStickButtons = 1
GameInputFlightStickView: win32more.Windows.Win32.UI.Input.GameInput.GameInputFlightStickButtons = 2
GameInputFlightStickFirePrimary: win32more.Windows.Win32.UI.Input.GameInput.GameInputFlightStickButtons = 4
GameInputFlightStickFireSecondary: win32more.Windows.Win32.UI.Input.GameInput.GameInputFlightStickButtons = 8
class GameInputFlightStickInfo(Structure):
    menuButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    viewButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    firePrimaryButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    fireSecondaryButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    hatSwitchKind: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchKind
class GameInputFlightStickState(Structure):
    buttons: win32more.Windows.Win32.UI.Input.GameInput.GameInputFlightStickButtons
    hatSwitch: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchPosition
    roll: Single
    pitch: Single
    yaw: Single
    throttle: Single
GameInputFocusPolicy = Int32
GameInputDefaultFocusPolicy: win32more.Windows.Win32.UI.Input.GameInput.GameInputFocusPolicy = 0
GameInputDisableBackgroundInput: win32more.Windows.Win32.UI.Input.GameInput.GameInputFocusPolicy = 1
GameInputExclusiveForegroundInput: win32more.Windows.Win32.UI.Input.GameInput.GameInputFocusPolicy = 2
GameInputDisableBackgroundGuideButton: win32more.Windows.Win32.UI.Input.GameInput.GameInputFocusPolicy = 4
GameInputExclusiveForegroundGuideButton: win32more.Windows.Win32.UI.Input.GameInput.GameInputFocusPolicy = 8
GameInputDisableBackgroundShareButton: win32more.Windows.Win32.UI.Input.GameInput.GameInputFocusPolicy = 16
GameInputExclusiveForegroundShareButton: win32more.Windows.Win32.UI.Input.GameInput.GameInputFocusPolicy = 32
class GameInputForceFeedbackConditionParams(Structure):
    magnitude: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackMagnitude
    positiveCoefficient: Single
    negativeCoefficient: Single
    maxPositiveMagnitude: Single
    maxNegativeMagnitude: Single
    deadZone: Single
    bias: Single
class GameInputForceFeedbackConstantParams(Structure):
    envelope: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEnvelope
    magnitude: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackMagnitude
GameInputForceFeedbackEffectKind = Int32
GameInputForceFeedbackConstant: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEffectKind = 0
GameInputForceFeedbackRamp: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEffectKind = 1
GameInputForceFeedbackSineWave: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEffectKind = 2
GameInputForceFeedbackSquareWave: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEffectKind = 3
GameInputForceFeedbackTriangleWave: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEffectKind = 4
GameInputForceFeedbackSawtoothUpWave: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEffectKind = 5
GameInputForceFeedbackSawtoothDownWave: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEffectKind = 6
GameInputForceFeedbackSpring: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEffectKind = 7
GameInputForceFeedbackFriction: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEffectKind = 8
GameInputForceFeedbackDamper: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEffectKind = 9
GameInputForceFeedbackInertia: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEffectKind = 10
class GameInputForceFeedbackEnvelope(Structure):
    attackDuration: UInt64
    sustainDuration: UInt64
    releaseDuration: UInt64
    attackGain: Single
    sustainGain: Single
    releaseGain: Single
    playCount: UInt32
    repeatDelay: UInt64
class GameInputForceFeedbackMagnitude(Structure):
    linearX: Single
    linearY: Single
    linearZ: Single
    angularX: Single
    angularY: Single
    angularZ: Single
    normal: Single
class GameInputForceFeedbackMotorInfo(Structure):
    supportedAxes: win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackAxes
    location: win32more.Windows.Win32.UI.Input.GameInput.GameInputLocation
    locationId: UInt32
    maxSimultaneousEffects: UInt32
    isConstantEffectSupported: Byte
    isRampEffectSupported: Byte
    isSineWaveEffectSupported: Byte
    isSquareWaveEffectSupported: Byte
    isTriangleWaveEffectSupported: Byte
    isSawtoothUpWaveEffectSupported: Byte
    isSawtoothDownWaveEffectSupported: Byte
    isSpringEffectSupported: Byte
    isFrictionEffectSupported: Byte
    isDamperEffectSupported: Byte
    isInertiaEffectSupported: Byte
class GameInputForceFeedbackParams(Structure):
    kind: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEffectKind
    data: _data_e__Union
    class _data_e__Union(Union):
        constant: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackConstantParams
        ramp: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackRampParams
        sineWave: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackPeriodicParams
        squareWave: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackPeriodicParams
        triangleWave: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackPeriodicParams
        sawtoothUpWave: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackPeriodicParams
        sawtoothDownWave: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackPeriodicParams
        spring: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackConditionParams
        friction: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackConditionParams
        damper: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackConditionParams
        inertia: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackConditionParams
class GameInputForceFeedbackPeriodicParams(Structure):
    envelope: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEnvelope
    magnitude: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackMagnitude
    frequency: Single
    phase: Single
    bias: Single
class GameInputForceFeedbackRampParams(Structure):
    envelope: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackEnvelope
    startMagnitude: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackMagnitude
    endMagnitude: win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackMagnitude
GameInputGamepadButtons = Int32
GameInputGamepadNone: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 0
GameInputGamepadMenu: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 1
GameInputGamepadView: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 2
GameInputGamepadA: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 4
GameInputGamepadB: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 8
GameInputGamepadX: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 16
GameInputGamepadY: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 32
GameInputGamepadDPadUp: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 64
GameInputGamepadDPadDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 128
GameInputGamepadDPadLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 256
GameInputGamepadDPadRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 512
GameInputGamepadLeftShoulder: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 1024
GameInputGamepadRightShoulder: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 2048
GameInputGamepadLeftThumbstick: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 4096
GameInputGamepadRightThumbstick: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons = 8192
class GameInputGamepadInfo(Structure):
    menuButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    viewButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    aButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    bButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    xButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    yButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    dpadUpLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    dpadDownLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    dpadLeftLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    dpadRightLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    leftShoulderButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    rightShoulderButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    leftThumbstickButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    rightThumbstickButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
class GameInputGamepadState(Structure):
    buttons: win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadButtons
    leftTrigger: Single
    rightTrigger: Single
    leftThumbstickX: Single
    leftThumbstickY: Single
    rightThumbstickX: Single
    rightThumbstickY: Single
class GameInputHapticFeedbackMotorInfo(Structure):
    mappedRumbleMotors: win32more.Windows.Win32.UI.Input.GameInput.GameInputRumbleMotors
    location: win32more.Windows.Win32.UI.Input.GameInput.GameInputLocation
    locationId: UInt32
    waveformCount: UInt32
    waveformInfo: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputHapticWaveformInfo)
class GameInputHapticFeedbackParams(Structure):
    waveformIndex: UInt32
    duration: UInt64
    intensity: Single
    playCount: UInt32
    repeatDelay: UInt64
class GameInputHapticWaveformInfo(Structure):
    usage: win32more.Windows.Win32.UI.Input.GameInput.GameInputUsage
    isDurationSupported: Byte
    isIntensitySupported: Byte
    isRepeatSupported: Byte
    isRepeatDelaySupported: Byte
    defaultDuration: UInt64
class GameInputKeyState(Structure):
    scanCode: UInt32
    codePoint: UInt32
    virtualKey: Byte
    isDeadKey: Byte
class GameInputKeyboardInfo(Structure):
    kind: win32more.Windows.Win32.UI.Input.GameInput.GameInputKeyboardKind
    layout: UInt32
    keyCount: UInt32
    functionKeyCount: UInt32
    maxSimultaneousKeys: UInt32
    platformType: UInt32
    platformSubtype: UInt32
    nativeLanguage: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputString)
GameInputKeyboardKind = Int32
GameInputUnknownKeyboard: win32more.Windows.Win32.UI.Input.GameInput.GameInputKeyboardKind = -1
GameInputAnsiKeyboard: win32more.Windows.Win32.UI.Input.GameInput.GameInputKeyboardKind = 0
GameInputIsoKeyboard: win32more.Windows.Win32.UI.Input.GameInput.GameInputKeyboardKind = 1
GameInputKsKeyboard: win32more.Windows.Win32.UI.Input.GameInput.GameInputKeyboardKind = 2
GameInputAbntKeyboard: win32more.Windows.Win32.UI.Input.GameInput.GameInputKeyboardKind = 3
GameInputJisKeyboard: win32more.Windows.Win32.UI.Input.GameInput.GameInputKeyboardKind = 4
@winfunctype_pointer
def GameInputKeyboardLayoutCallback(callbackToken: UInt64, context: VoidPtr, device: win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice, timestamp: UInt64, currentLayout: UInt32, previousLayout: UInt32) -> Void: ...
GameInputKind = Int32
GameInputKindUnknown: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 0
GameInputKindRawDeviceReport: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 1
GameInputKindControllerAxis: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 2
GameInputKindControllerButton: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 4
GameInputKindControllerSwitch: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 8
GameInputKindController: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 14
GameInputKindKeyboard: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 16
GameInputKindMouse: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 32
GameInputKindTouch: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 256
GameInputKindMotion: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 4096
GameInputKindArcadeStick: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 65536
GameInputKindFlightStick: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 131072
GameInputKindGamepad: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 262144
GameInputKindRacingWheel: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 524288
GameInputKindUiNavigation: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind = 16777216
GameInputLabel = Int32
GameInputLabelUnknown: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = -1
GameInputLabelNone: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 0
GameInputLabelXboxGuide: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 1
GameInputLabelXboxBack: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 2
GameInputLabelXboxStart: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 3
GameInputLabelXboxMenu: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 4
GameInputLabelXboxView: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 5
GameInputLabelXboxA: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 7
GameInputLabelXboxB: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 8
GameInputLabelXboxX: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 9
GameInputLabelXboxY: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 10
GameInputLabelXboxDPadUp: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 11
GameInputLabelXboxDPadDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 12
GameInputLabelXboxDPadLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 13
GameInputLabelXboxDPadRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 14
GameInputLabelXboxLeftShoulder: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 15
GameInputLabelXboxLeftTrigger: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 16
GameInputLabelXboxLeftStickButton: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 17
GameInputLabelXboxRightShoulder: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 18
GameInputLabelXboxRightTrigger: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 19
GameInputLabelXboxRightStickButton: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 20
GameInputLabelXboxPaddle1: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 21
GameInputLabelXboxPaddle2: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 22
GameInputLabelXboxPaddle3: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 23
GameInputLabelXboxPaddle4: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 24
GameInputLabelLetterA: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 25
GameInputLabelLetterB: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 26
GameInputLabelLetterC: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 27
GameInputLabelLetterD: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 28
GameInputLabelLetterE: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 29
GameInputLabelLetterF: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 30
GameInputLabelLetterG: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 31
GameInputLabelLetterH: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 32
GameInputLabelLetterI: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 33
GameInputLabelLetterJ: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 34
GameInputLabelLetterK: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 35
GameInputLabelLetterL: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 36
GameInputLabelLetterM: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 37
GameInputLabelLetterN: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 38
GameInputLabelLetterO: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 39
GameInputLabelLetterP: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 40
GameInputLabelLetterQ: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 41
GameInputLabelLetterR: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 42
GameInputLabelLetterS: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 43
GameInputLabelLetterT: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 44
GameInputLabelLetterU: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 45
GameInputLabelLetterV: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 46
GameInputLabelLetterW: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 47
GameInputLabelLetterX: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 48
GameInputLabelLetterY: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 49
GameInputLabelLetterZ: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 50
GameInputLabelNumber0: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 51
GameInputLabelNumber1: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 52
GameInputLabelNumber2: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 53
GameInputLabelNumber3: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 54
GameInputLabelNumber4: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 55
GameInputLabelNumber5: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 56
GameInputLabelNumber6: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 57
GameInputLabelNumber7: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 58
GameInputLabelNumber8: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 59
GameInputLabelNumber9: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 60
GameInputLabelArrowUp: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 61
GameInputLabelArrowUpRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 62
GameInputLabelArrowRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 63
GameInputLabelArrowDownRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 64
GameInputLabelArrowDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 65
GameInputLabelArrowDownLLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 66
GameInputLabelArrowLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 67
GameInputLabelArrowUpLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 68
GameInputLabelArrowUpDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 69
GameInputLabelArrowLeftRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 70
GameInputLabelArrowUpDownLeftRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 71
GameInputLabelArrowClockwise: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 72
GameInputLabelArrowCounterClockwise: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 73
GameInputLabelArrowReturn: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 74
GameInputLabelIconBranding: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 75
GameInputLabelIconHome: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 76
GameInputLabelIconMenu: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 77
GameInputLabelIconCross: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 78
GameInputLabelIconCircle: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 79
GameInputLabelIconSquare: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 80
GameInputLabelIconTriangle: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 81
GameInputLabelIconStar: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 82
GameInputLabelIconDPadUp: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 83
GameInputLabelIconDPadDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 84
GameInputLabelIconDPadLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 85
GameInputLabelIconDPadRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 86
GameInputLabelIconDialClockwise: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 87
GameInputLabelIconDialCounterClockwise: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 88
GameInputLabelIconSliderLeftRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 89
GameInputLabelIconSliderUpDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 90
GameInputLabelIconWheelUpDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 91
GameInputLabelIconPlus: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 92
GameInputLabelIconMinus: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 93
GameInputLabelIconSuspension: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 94
GameInputLabelHome: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 95
GameInputLabelGuide: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 96
GameInputLabelMode: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 97
GameInputLabelSelect: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 98
GameInputLabelMenu: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 99
GameInputLabelView: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 100
GameInputLabelBack: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 101
GameInputLabelStart: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 102
GameInputLabelOptions: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 103
GameInputLabelShare: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 104
GameInputLabelUp: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 105
GameInputLabelDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 106
GameInputLabelLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 107
GameInputLabelRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 108
GameInputLabelLB: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 109
GameInputLabelLT: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 110
GameInputLabelLSB: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 111
GameInputLabelL1: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 112
GameInputLabelL2: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 113
GameInputLabelL3: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 114
GameInputLabelRB: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 115
GameInputLabelRT: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 116
GameInputLabelRSB: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 117
GameInputLabelR1: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 118
GameInputLabelR2: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 119
GameInputLabelR3: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 120
GameInputLabelP1: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 121
GameInputLabelP2: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 122
GameInputLabelP3: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 123
GameInputLabelP4: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel = 124
GameInputLocation = Int32
GameInputLocationUnknown: win32more.Windows.Win32.UI.Input.GameInput.GameInputLocation = -1
GameInputLocationChassis: win32more.Windows.Win32.UI.Input.GameInput.GameInputLocation = 0
GameInputLocationDisplay: win32more.Windows.Win32.UI.Input.GameInput.GameInputLocation = 1
GameInputLocationAxis: win32more.Windows.Win32.UI.Input.GameInput.GameInputLocation = 2
GameInputLocationButton: win32more.Windows.Win32.UI.Input.GameInput.GameInputLocation = 3
GameInputLocationSwitch: win32more.Windows.Win32.UI.Input.GameInput.GameInputLocation = 4
GameInputLocationKey: win32more.Windows.Win32.UI.Input.GameInput.GameInputLocation = 5
GameInputLocationTouchPad: win32more.Windows.Win32.UI.Input.GameInput.GameInputLocation = 6
GameInputMotionAccuracy = Int32
GameInputMotionAccuracyUnknown: win32more.Windows.Win32.UI.Input.GameInput.GameInputMotionAccuracy = -1
GameInputMotionUnavailable: win32more.Windows.Win32.UI.Input.GameInput.GameInputMotionAccuracy = 0
GameInputMotionUnreliable: win32more.Windows.Win32.UI.Input.GameInput.GameInputMotionAccuracy = 1
GameInputMotionApproximate: win32more.Windows.Win32.UI.Input.GameInput.GameInputMotionAccuracy = 2
GameInputMotionAccurate: win32more.Windows.Win32.UI.Input.GameInput.GameInputMotionAccuracy = 3
class GameInputMotionInfo(Structure):
    maxAcceleration: Single
    maxAngularVelocity: Single
    maxMagneticFieldStrength: Single
class GameInputMotionState(Structure):
    accelerationX: Single
    accelerationY: Single
    accelerationZ: Single
    angularVelocityX: Single
    angularVelocityY: Single
    angularVelocityZ: Single
    magneticFieldX: Single
    magneticFieldY: Single
    magneticFieldZ: Single
    orientationW: Single
    orientationX: Single
    orientationY: Single
    orientationZ: Single
    accelerometerAccuracy: win32more.Windows.Win32.UI.Input.GameInput.GameInputMotionAccuracy
    gyroscopeAccuracy: win32more.Windows.Win32.UI.Input.GameInput.GameInputMotionAccuracy
    magnetometerAccuracy: win32more.Windows.Win32.UI.Input.GameInput.GameInputMotionAccuracy
    orientationAccuracy: win32more.Windows.Win32.UI.Input.GameInput.GameInputMotionAccuracy
GameInputMouseButtons = Int32
GameInputMouseNone: win32more.Windows.Win32.UI.Input.GameInput.GameInputMouseButtons = 0
GameInputMouseLeftButton: win32more.Windows.Win32.UI.Input.GameInput.GameInputMouseButtons = 1
GameInputMouseRightButton: win32more.Windows.Win32.UI.Input.GameInput.GameInputMouseButtons = 2
GameInputMouseMiddleButton: win32more.Windows.Win32.UI.Input.GameInput.GameInputMouseButtons = 4
GameInputMouseButton4: win32more.Windows.Win32.UI.Input.GameInput.GameInputMouseButtons = 8
GameInputMouseButton5: win32more.Windows.Win32.UI.Input.GameInput.GameInputMouseButtons = 16
GameInputMouseWheelTiltLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputMouseButtons = 32
GameInputMouseWheelTiltRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputMouseButtons = 64
class GameInputMouseInfo(Structure):
    supportedButtons: win32more.Windows.Win32.UI.Input.GameInput.GameInputMouseButtons
    sampleRate: UInt32
    sensorDpi: UInt32
    hasWheelX: Byte
    hasWheelY: Byte
class GameInputMouseState(Structure):
    buttons: win32more.Windows.Win32.UI.Input.GameInput.GameInputMouseButtons
    positionX: Int64
    positionY: Int64
    wheelX: Int64
    wheelY: Int64
GameInputRacingWheelButtons = Int32
GameInputRacingWheelNone: win32more.Windows.Win32.UI.Input.GameInput.GameInputRacingWheelButtons = 0
GameInputRacingWheelMenu: win32more.Windows.Win32.UI.Input.GameInput.GameInputRacingWheelButtons = 1
GameInputRacingWheelView: win32more.Windows.Win32.UI.Input.GameInput.GameInputRacingWheelButtons = 2
GameInputRacingWheelPreviousGear: win32more.Windows.Win32.UI.Input.GameInput.GameInputRacingWheelButtons = 4
GameInputRacingWheelNextGear: win32more.Windows.Win32.UI.Input.GameInput.GameInputRacingWheelButtons = 8
GameInputRacingWheelDpadUp: win32more.Windows.Win32.UI.Input.GameInput.GameInputRacingWheelButtons = 16
GameInputRacingWheelDpadDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputRacingWheelButtons = 32
GameInputRacingWheelDpadLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputRacingWheelButtons = 64
GameInputRacingWheelDpadRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputRacingWheelButtons = 128
class GameInputRacingWheelInfo(Structure):
    menuButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    viewButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    previousGearButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    nextGearButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    dpadUpLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    dpadDownLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    dpadLeftLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    dpadRightLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    hasClutch: Byte
    hasHandbrake: Byte
    hasPatternShifter: Byte
    minPatternShifterGear: Int32
    maxPatternShifterGear: Int32
    maxWheelAngle: Single
class GameInputRacingWheelState(Structure):
    buttons: win32more.Windows.Win32.UI.Input.GameInput.GameInputRacingWheelButtons
    patternShifterGear: Int32
    wheel: Single
    throttle: Single
    brake: Single
    clutch: Single
    handbrake: Single
class GameInputRawDeviceItemCollectionInfo(Structure):
    kind: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionKind
    childCount: UInt32
    siblingCount: UInt32
    usageCount: UInt32
    usages: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputUsage)
    parent: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionInfo)
    firstSibling: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionInfo)
    previousSibling: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionInfo)
    nextSibling: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionInfo)
    lastSibling: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionInfo)
    firstChild: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionInfo)
    lastChild: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionInfo)
GameInputRawDeviceItemCollectionKind = Int32
GameInputUnknownItemCollection: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionKind = -1
GameInputPhysicalItemCollection: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionKind = 0
GameInputApplicationItemCollection: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionKind = 1
GameInputLogicalItemCollection: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionKind = 2
GameInputReportItemCollection: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionKind = 3
GameInputNamedArrayItemCollection: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionKind = 4
GameInputUsageSwitchItemCollection: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionKind = 5
GameInputUsageModifierItemCollection: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionKind = 6
GameInputRawDevicePhysicalUnitKind = Int32
GameInputPhysicalUnitUnknown: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = -1
GameInputPhysicalUnitNone: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 0
GameInputPhysicalUnitTime: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 1
GameInputPhysicalUnitFrequency: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 2
GameInputPhysicalUnitLength: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 3
GameInputPhysicalUnitVelocity: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 4
GameInputPhysicalUnitAcceleration: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 5
GameInputPhysicalUnitMass: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 6
GameInputPhysicalUnitMomentum: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 7
GameInputPhysicalUnitForce: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 8
GameInputPhysicalUnitPressure: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 9
GameInputPhysicalUnitAngle: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 10
GameInputPhysicalUnitAngularVelocity: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 11
GameInputPhysicalUnitAngularAcceleration: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 12
GameInputPhysicalUnitAngularMass: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 13
GameInputPhysicalUnitAngularMomentum: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 14
GameInputPhysicalUnitAngularTorque: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 15
GameInputPhysicalUnitElectricCurrent: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 16
GameInputPhysicalUnitElectricCharge: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 17
GameInputPhysicalUnitElectricPotential: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 18
GameInputPhysicalUnitEnergy: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 19
GameInputPhysicalUnitPower: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 20
GameInputPhysicalUnitTemperature: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 21
GameInputPhysicalUnitLuminousIntensity: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 22
GameInputPhysicalUnitLuminousFlux: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 23
GameInputPhysicalUnitIlluminance: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind = 24
class GameInputRawDeviceReportInfo(Structure):
    kind: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportKind
    id: UInt32
    size: UInt32
    itemCount: UInt32
    items: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemInfo)
GameInputRawDeviceReportItemFlags = Int32
GameInputDefaultItem: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemFlags = 0
GameInputConstantItem: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemFlags = 1
GameInputArrayItem: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemFlags = 2
GameInputRelativeItem: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemFlags = 4
GameInputWraparoundItem: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemFlags = 8
GameInputNonlinearItem: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemFlags = 16
GameInputStableItem: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemFlags = 32
GameInputNullableItem: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemFlags = 64
GameInputVolatileItem: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemFlags = 128
GameInputBufferedItem: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemFlags = 256
class GameInputRawDeviceReportItemInfo(Structure):
    bitOffset: UInt32
    bitSize: UInt32
    logicalMin: Int64
    logicalMax: Int64
    physicalMin: Double
    physicalMax: Double
    physicalUnits: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDevicePhysicalUnitKind
    rawPhysicalUnits: UInt32
    rawPhysicalUnitsExponent: Int32
    flags: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportItemFlags
    usageCount: UInt32
    usages: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputUsage)
    collection: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceItemCollectionInfo)
    itemString: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputString)
GameInputRawDeviceReportKind = Int32
GameInputRawInputReport: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportKind = 0
GameInputRawOutputReport: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportKind = 1
GameInputRawFeatureReport: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportKind = 2
@winfunctype_pointer
def GameInputReadingCallback(callbackToken: UInt64, context: VoidPtr, reading: win32more.Windows.Win32.UI.Input.GameInput.IGameInputReading, hasOverrunOccurred: Boolean) -> Void: ...
GameInputRumbleMotors = Int32
GameInputRumbleNone: win32more.Windows.Win32.UI.Input.GameInput.GameInputRumbleMotors = 0
GameInputRumbleLowFrequency: win32more.Windows.Win32.UI.Input.GameInput.GameInputRumbleMotors = 1
GameInputRumbleHighFrequency: win32more.Windows.Win32.UI.Input.GameInput.GameInputRumbleMotors = 2
GameInputRumbleLeftTrigger: win32more.Windows.Win32.UI.Input.GameInput.GameInputRumbleMotors = 4
GameInputRumbleRightTrigger: win32more.Windows.Win32.UI.Input.GameInput.GameInputRumbleMotors = 8
class GameInputRumbleParams(Structure):
    lowFrequency: Single
    highFrequency: Single
    leftTrigger: Single
    rightTrigger: Single
class GameInputString(Structure):
    sizeInBytes: UInt32
    codePointCount: UInt32
    data: win32more.Windows.Win32.Foundation.PSTR
GameInputSwitchKind = Int32
GameInputUnknownSwitchKind: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchKind = -1
GameInput2WaySwitch: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchKind = 0
GameInput4WaySwitch: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchKind = 1
GameInput8WaySwitch: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchKind = 2
GameInputSwitchPosition = Int32
GameInputSwitchCenter: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchPosition = 0
GameInputSwitchUp: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchPosition = 1
GameInputSwitchUpRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchPosition = 2
GameInputSwitchRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchPosition = 3
GameInputSwitchDownRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchPosition = 4
GameInputSwitchDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchPosition = 5
GameInputSwitchDownLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchPosition = 6
GameInputSwitchLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchPosition = 7
GameInputSwitchUpLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchPosition = 8
@winfunctype_pointer
def GameInputSystemButtonCallback(callbackToken: UInt64, context: VoidPtr, device: win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice, timestamp: UInt64, currentButtons: win32more.Windows.Win32.UI.Input.GameInput.GameInputSystemButtons, previousButtons: win32more.Windows.Win32.UI.Input.GameInput.GameInputSystemButtons) -> Void: ...
GameInputSystemButtons = Int32
GameInputSystemButtonNone: win32more.Windows.Win32.UI.Input.GameInput.GameInputSystemButtons = 0
GameInputSystemButtonGuide: win32more.Windows.Win32.UI.Input.GameInput.GameInputSystemButtons = 1
GameInputSystemButtonShare: win32more.Windows.Win32.UI.Input.GameInput.GameInputSystemButtons = 2
class GameInputTouchSensorInfo(Structure):
    mappedInputKinds: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind
    label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    location: win32more.Windows.Win32.UI.Input.GameInput.GameInputLocation
    locationId: UInt32
    resolutionX: UInt64
    resolutionY: UInt64
    shape: win32more.Windows.Win32.UI.Input.GameInput.GameInputTouchShape
    aspectRatio: Single
    orientation: Single
    physicalWidth: Single
    physicalHeight: Single
    maxPressure: Single
    maxProximity: Single
    maxTouchPoints: UInt32
GameInputTouchShape = Int32
GameInputTouchShapeUnknown: win32more.Windows.Win32.UI.Input.GameInput.GameInputTouchShape = -1
GameInputTouchShapePoint: win32more.Windows.Win32.UI.Input.GameInput.GameInputTouchShape = 0
GameInputTouchShape1DLinear: win32more.Windows.Win32.UI.Input.GameInput.GameInputTouchShape = 1
GameInputTouchShape1DRadial: win32more.Windows.Win32.UI.Input.GameInput.GameInputTouchShape = 2
GameInputTouchShape1DIrregular: win32more.Windows.Win32.UI.Input.GameInput.GameInputTouchShape = 3
GameInputTouchShape2DRectangular: win32more.Windows.Win32.UI.Input.GameInput.GameInputTouchShape = 4
GameInputTouchShape2DElliptical: win32more.Windows.Win32.UI.Input.GameInput.GameInputTouchShape = 5
GameInputTouchShape2DIrregular: win32more.Windows.Win32.UI.Input.GameInput.GameInputTouchShape = 6
class GameInputTouchState(Structure):
    touchId: UInt64
    sensorIndex: UInt32
    positionX: Single
    positionY: Single
    pressure: Single
    proximity: Single
    contactRectTop: Single
    contactRectLeft: Single
    contactRectRight: Single
    contactRectBottom: Single
GameInputUiNavigationButtons = Int32
GameInputUiNavigationNone: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 0
GameInputUiNavigationMenu: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 1
GameInputUiNavigationView: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 2
GameInputUiNavigationAccept: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 4
GameInputUiNavigationCancel: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 8
GameInputUiNavigationUp: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 16
GameInputUiNavigationDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 32
GameInputUiNavigationLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 64
GameInputUiNavigationRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 128
GameInputUiNavigationContext1: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 256
GameInputUiNavigationContext2: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 512
GameInputUiNavigationContext3: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 1024
GameInputUiNavigationContext4: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 2048
GameInputUiNavigationPageUp: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 4096
GameInputUiNavigationPageDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 8192
GameInputUiNavigationPageLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 16384
GameInputUiNavigationPageRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 32768
GameInputUiNavigationScrollUp: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 65536
GameInputUiNavigationScrollDown: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 131072
GameInputUiNavigationScrollLeft: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 262144
GameInputUiNavigationScrollRight: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons = 524288
class GameInputUiNavigationInfo(Structure):
    menuButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    viewButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    acceptButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    cancelButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    upButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    downButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    leftButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    rightButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    contextButton1Label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    contextButton2Label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    contextButton3Label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    contextButton4Label: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    pageUpButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    pageDownButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    pageLeftButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    pageRightButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    scrollUpButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    scrollDownButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    scrollLeftButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    scrollRightButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
    guideButtonLabel: win32more.Windows.Win32.UI.Input.GameInput.GameInputLabel
class GameInputUiNavigationState(Structure):
    buttons: win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationButtons
class GameInputUsage(Structure):
    page: UInt16
    id: UInt16
class GameInputVersion(Structure):
    major: UInt16
    minor: UInt16
    build: UInt16
    revision: UInt16
class IGameInput(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11be2a7e-4254-445a-9c09-ffc40f006918}')
    @commethod(3)
    def GetCurrentTimestamp(self) -> UInt64: ...
    @commethod(4)
    def GetCurrentReading(self, inputKind: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind, device: win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice, reading: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputReading)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNextReading(self, referenceReading: win32more.Windows.Win32.UI.Input.GameInput.IGameInputReading, inputKind: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind, device: win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice, reading: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputReading)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPreviousReading(self, referenceReading: win32more.Windows.Win32.UI.Input.GameInput.IGameInputReading, inputKind: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind, device: win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice, reading: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputReading)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTemporalReading(self, timestamp: UInt64, device: win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice, reading: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputReading)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterReadingCallback(self, device: win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice, inputKind: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind, analogThreshold: Single, context: VoidPtr, callbackFunc: win32more.Windows.Win32.UI.Input.GameInput.GameInputReadingCallback, callbackToken: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterDeviceCallback(self, device: win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice, inputKind: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind, statusFilter: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus, enumerationKind: win32more.Windows.Win32.UI.Input.GameInput.GameInputEnumerationKind, context: VoidPtr, callbackFunc: win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceCallback, callbackToken: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterSystemButtonCallback(self, device: win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice, buttonFilter: win32more.Windows.Win32.UI.Input.GameInput.GameInputSystemButtons, context: VoidPtr, callbackFunc: win32more.Windows.Win32.UI.Input.GameInput.GameInputSystemButtonCallback, callbackToken: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RegisterKeyboardLayoutCallback(self, device: win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice, context: VoidPtr, callbackFunc: win32more.Windows.Win32.UI.Input.GameInput.GameInputKeyboardLayoutCallback, callbackToken: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def StopCallback(self, callbackToken: UInt64) -> Void: ...
    @commethod(13)
    def UnregisterCallback(self, callbackToken: UInt64, timeoutInMicroseconds: UInt64) -> Boolean: ...
    @commethod(14)
    def CreateDispatcher(self, dispatcher: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputDispatcher)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateAggregateDevice(self, inputKind: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind, device: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def FindDeviceFromId(self, value: POINTER(win32more.Windows.Win32.Foundation.APP_LOCAL_DEVICE_ID), device: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def FindDeviceFromObject(self, value: win32more.Windows.Win32.System.Com.IUnknown, device: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def FindDeviceFromPlatformHandle(self, value: win32more.Windows.Win32.Foundation.HANDLE, device: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def FindDeviceFromPlatformString(self, value: win32more.Windows.Win32.Foundation.PWSTR, device: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def EnableOemDeviceSupport(self, vendorId: UInt16, productId: UInt16, interfaceNumber: Byte, collectionNumber: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetFocusPolicy(self, policy: win32more.Windows.Win32.UI.Input.GameInput.GameInputFocusPolicy) -> Void: ...
class IGameInputDevice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{31dd86fb-4c1b-408a-868f-439b3cd47125}')
    @commethod(3)
    def GetDeviceInfo(self) -> POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceInfo): ...
    @commethod(4)
    def GetDeviceStatus(self) -> win32more.Windows.Win32.UI.Input.GameInput.GameInputDeviceStatus: ...
    @commethod(5)
    def GetBatteryState(self, state: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputBatteryState)) -> Void: ...
    @commethod(6)
    def CreateForceFeedbackEffect(self, motorIndex: UInt32, params: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackParams), effect: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputForceFeedbackEffect)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsForceFeedbackMotorPoweredOn(self, motorIndex: UInt32) -> Boolean: ...
    @commethod(8)
    def SetForceFeedbackMotorGain(self, motorIndex: UInt32, masterGain: Single) -> Void: ...
    @commethod(9)
    def SetHapticMotorState(self, motorIndex: UInt32, params: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputHapticFeedbackParams)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetRumbleState(self, params: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRumbleParams)) -> Void: ...
    @commethod(11)
    def SetInputSynchronizationState(self, enabled: Byte) -> Void: ...
    @commethod(12)
    def SendInputSynchronizationHint(self) -> Void: ...
    @commethod(13)
    def PowerOff(self) -> Void: ...
    @commethod(14)
    def CreateRawDeviceReport(self, reportId: UInt32, reportKind: win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportKind, report: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputRawDeviceReport)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRawDeviceFeature(self, reportId: UInt32, report: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputRawDeviceReport)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetRawDeviceFeature(self, report: win32more.Windows.Win32.UI.Input.GameInput.IGameInputRawDeviceReport) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SendRawDeviceOutput(self, report: win32more.Windows.Win32.UI.Input.GameInput.IGameInputRawDeviceReport) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SendRawDeviceOutputWithResponse(self, requestReport: win32more.Windows.Win32.UI.Input.GameInput.IGameInputRawDeviceReport, responseReport: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputRawDeviceReport)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ExecuteRawDeviceIoControl(self, controlCode: UInt32, inputBufferSize: UIntPtr, inputBuffer: VoidPtr, outputBufferSize: UIntPtr, outputBuffer: VoidPtr, outputSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def AcquireExclusiveRawDeviceAccess(self, timeoutInMicroseconds: UInt64) -> Boolean: ...
    @commethod(21)
    def ReleaseExclusiveRawDeviceAccess(self) -> Void: ...
class IGameInputDispatcher(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{415eed2e-98cb-42c2-8f28-b94601074e31}')
    @commethod(3)
    def Dispatch(self, quotaInMicroseconds: UInt64) -> Boolean: ...
    @commethod(4)
    def OpenWaitHandle(self, waitHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGameInputForceFeedbackEffect(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{51bda05e-f742-45d9-b085-9444ae48381d}')
    @commethod(3)
    def GetDevice(self, device: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice)) -> Void: ...
    @commethod(4)
    def GetMotorIndex(self) -> UInt32: ...
    @commethod(5)
    def GetGain(self) -> Single: ...
    @commethod(6)
    def SetGain(self, gain: Single) -> Void: ...
    @commethod(7)
    def GetParams(self, params: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackParams)) -> Void: ...
    @commethod(8)
    def SetParams(self, params: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputForceFeedbackParams)) -> Boolean: ...
    @commethod(9)
    def GetState(self) -> win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackEffectState: ...
    @commethod(10)
    def SetState(self, state: win32more.Windows.Win32.UI.Input.GameInput.GameInputFeedbackEffectState) -> Void: ...
class IGameInputRawDeviceReport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{61f08cf1-1ffc-40ca-a2b8-e1ab8bc5b6dc}')
    @commethod(3)
    def GetDevice(self, device: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice)) -> Void: ...
    @commethod(4)
    def GetReportInfo(self) -> POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRawDeviceReportInfo): ...
    @commethod(5)
    def GetRawDataSize(self) -> UIntPtr: ...
    @commethod(6)
    def GetRawData(self, bufferSize: UIntPtr, buffer: VoidPtr) -> UIntPtr: ...
    @commethod(7)
    def SetRawData(self, bufferSize: UIntPtr, buffer: VoidPtr) -> Boolean: ...
    @commethod(8)
    def GetItemValue(self, itemIndex: UInt32, value: POINTER(Int64)) -> Boolean: ...
    @commethod(9)
    def SetItemValue(self, itemIndex: UInt32, value: Int64) -> Boolean: ...
    @commethod(10)
    def ResetItemValue(self, itemIndex: UInt32) -> Boolean: ...
    @commethod(11)
    def ResetAllItems(self) -> Boolean: ...
class IGameInputReading(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2156947a-e1fa-4de0-a30b-d812931dbd8d}')
    @commethod(3)
    def GetInputKind(self) -> win32more.Windows.Win32.UI.Input.GameInput.GameInputKind: ...
    @commethod(4)
    def GetSequenceNumber(self, inputKind: win32more.Windows.Win32.UI.Input.GameInput.GameInputKind) -> UInt64: ...
    @commethod(5)
    def GetTimestamp(self) -> UInt64: ...
    @commethod(6)
    def GetDevice(self, device: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputDevice)) -> Void: ...
    @commethod(7)
    def GetRawReport(self, report: POINTER(win32more.Windows.Win32.UI.Input.GameInput.IGameInputRawDeviceReport)) -> Boolean: ...
    @commethod(8)
    def GetControllerAxisCount(self) -> UInt32: ...
    @commethod(9)
    def GetControllerAxisState(self, stateArrayCount: UInt32, stateArray: POINTER(Single)) -> UInt32: ...
    @commethod(10)
    def GetControllerButtonCount(self) -> UInt32: ...
    @commethod(11)
    def GetControllerButtonState(self, stateArrayCount: UInt32, stateArray: POINTER(Boolean)) -> UInt32: ...
    @commethod(12)
    def GetControllerSwitchCount(self) -> UInt32: ...
    @commethod(13)
    def GetControllerSwitchState(self, stateArrayCount: UInt32, stateArray: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputSwitchPosition)) -> UInt32: ...
    @commethod(14)
    def GetKeyCount(self) -> UInt32: ...
    @commethod(15)
    def GetKeyState(self, stateArrayCount: UInt32, stateArray: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputKeyState)) -> UInt32: ...
    @commethod(16)
    def GetMouseState(self, state: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputMouseState)) -> Boolean: ...
    @commethod(17)
    def GetTouchCount(self) -> UInt32: ...
    @commethod(18)
    def GetTouchState(self, stateArrayCount: UInt32, stateArray: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputTouchState)) -> UInt32: ...
    @commethod(19)
    def GetMotionState(self, state: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputMotionState)) -> Boolean: ...
    @commethod(20)
    def GetArcadeStickState(self, state: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputArcadeStickState)) -> Boolean: ...
    @commethod(21)
    def GetFlightStickState(self, state: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputFlightStickState)) -> Boolean: ...
    @commethod(22)
    def GetGamepadState(self, state: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputGamepadState)) -> Boolean: ...
    @commethod(23)
    def GetRacingWheelState(self, state: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputRacingWheelState)) -> Boolean: ...
    @commethod(24)
    def GetUiNavigationState(self, state: POINTER(win32more.Windows.Win32.UI.Input.GameInput.GameInputUiNavigationState)) -> Boolean: ...


make_ready(__name__)
