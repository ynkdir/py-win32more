from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.UI.Accessibility
import Windows.Win32.UI.WindowsAndMessaging
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
class ACCESSTIMEOUT(Structure):
    cbSize: UInt32
    dwFlags: UInt32
    iTimeOutMSec: UInt32
ACC_UTILITY_STATE_FLAGS = UInt32
ANRUS_ON_SCREEN_KEYBOARD_ACTIVE: ACC_UTILITY_STATE_FLAGS = 1
ANRUS_TOUCH_MODIFICATION_ACTIVE: ACC_UTILITY_STATE_FLAGS = 2
ANRUS_PRIORITY_AUDIO_ACTIVE: ACC_UTILITY_STATE_FLAGS = 4
ANRUS_PRIORITY_AUDIO_ACTIVE_NODUCK: ACC_UTILITY_STATE_FLAGS = 8
ActiveEnd = Int32
ActiveEnd_None: ActiveEnd = 0
ActiveEnd_Start: ActiveEnd = 1
ActiveEnd_End: ActiveEnd = 2
AnimationStyle = Int32
AnimationStyle_None: AnimationStyle = 0
AnimationStyle_LasVegasLights: AnimationStyle = 1
AnimationStyle_BlinkingBackground: AnimationStyle = 2
AnimationStyle_SparkleText: AnimationStyle = 3
AnimationStyle_MarchingBlackAnts: AnimationStyle = 4
AnimationStyle_MarchingRedAnts: AnimationStyle = 5
AnimationStyle_Shimmer: AnimationStyle = 6
AnimationStyle_Other: AnimationStyle = -1
AnnoScope = Int32
ANNO_THIS: AnnoScope = 0
ANNO_CONTAINER: AnnoScope = 1
LIBID_Accessibility: Guid = Guid('1ea4dbf0-3c3b-11cf-81-0c-00-aa-00-38-9b-71')
CLSID_AccPropServices: Guid = Guid('b5f8350b-0548-48b1-a6-ee-88-bd-00-b4-a5-e7')
IIS_IsOleaccProxy: Guid = Guid('902697fa-80e4-4560-80-2a-a1-3f-22-a6-47-09')
IIS_ControlAccessible: Guid = Guid('38c682a6-9731-43f2-9f-ae-e9-01-e6-41-b1-01')
ANRUS_PRIORITY_AUDIO_DYNAMIC_DUCK: UInt32 = 16
MSAA_MENU_SIG: Int32 = -1441927155
PROPID_ACC_NAME: Guid = Guid('608d3df8-8128-4aa7-a4-28-f5-5e-49-26-72-91')
PROPID_ACC_VALUE: Guid = Guid('123fe443-211a-4615-95-27-c4-5a-7e-93-71-7a')
PROPID_ACC_DESCRIPTION: Guid = Guid('4d48dfe4-bd3f-491f-a6-48-49-2d-6f-20-c5-88')
PROPID_ACC_ROLE: Guid = Guid('cb905ff2-7bd1-4c05-b3-c8-e6-c2-41-36-4d-70')
PROPID_ACC_STATE: Guid = Guid('a8d4d5b0-0a21-42d0-a5-c0-51-4e-98-4f-45-7b')
PROPID_ACC_HELP: Guid = Guid('c831e11f-44db-4a99-97-68-cb-8f-97-8b-72-31')
PROPID_ACC_KEYBOARDSHORTCUT: Guid = Guid('7d9bceee-7d1e-4979-93-82-51-80-f4-17-2c-34')
PROPID_ACC_DEFAULTACTION: Guid = Guid('180c072b-c27f-43c7-99-22-f6-35-62-a4-63-2b')
PROPID_ACC_HELPTOPIC: Guid = Guid('787d1379-8ede-440b-8a-ec-11-f7-bf-90-30-b3')
PROPID_ACC_FOCUS: Guid = Guid('6eb335df-1c29-4127-b1-2c-de-e9-fd-15-7f-2b')
PROPID_ACC_SELECTION: Guid = Guid('b99d073c-d731-405b-90-61-d9-5e-8f-84-29-84')
PROPID_ACC_PARENT: Guid = Guid('474c22b6-ffc2-467a-b1-b5-e9-58-b4-65-73-30')
PROPID_ACC_NAV_UP: Guid = Guid('016e1a2b-1a4e-4767-86-12-33-86-f6-69-35-ec')
PROPID_ACC_NAV_DOWN: Guid = Guid('031670ed-3cdf-48d2-96-13-13-8f-2d-d8-a6-68')
PROPID_ACC_NAV_LEFT: Guid = Guid('228086cb-82f1-4a39-87-05-dc-dc-0f-ff-92-f5')
PROPID_ACC_NAV_RIGHT: Guid = Guid('cd211d9f-e1cb-4fe5-a7-7c-92-0b-88-4d-09-5b')
PROPID_ACC_NAV_PREV: Guid = Guid('776d3891-c73b-4480-b3-f6-07-6a-16-a1-5a-f6')
PROPID_ACC_NAV_NEXT: Guid = Guid('1cdc5455-8cd9-4c92-a3-71-39-39-a2-fe-3e-ee')
PROPID_ACC_NAV_FIRSTCHILD: Guid = Guid('cfd02558-557b-4c67-84-f9-2a-09-fc-e4-07-49')
PROPID_ACC_NAV_LASTCHILD: Guid = Guid('302ecaa5-48d5-4f8d-b6-71-1a-8d-20-a7-78-32')
PROPID_ACC_ROLEMAP: Guid = Guid('f79acda2-140d-4fe6-89-14-20-84-76-32-82-69')
PROPID_ACC_VALUEMAP: Guid = Guid('da1c3d79-fc5c-420e-b3-99-9d-15-33-54-9e-75')
PROPID_ACC_STATEMAP: Guid = Guid('43946c5e-0ac0-4042-b5-25-07-bb-db-e1-7f-a7')
PROPID_ACC_DESCRIPTIONMAP: Guid = Guid('1ff1435f-8a14-477b-b2-26-a0-ab-e2-79-97-5d')
PROPID_ACC_DODEFAULTACTION: Guid = Guid('1ba09523-2e3b-49a6-a0-59-59-68-2a-3c-48-fd')
DISPID_ACC_PARENT: Int32 = -5000
DISPID_ACC_CHILDCOUNT: Int32 = -5001
DISPID_ACC_CHILD: Int32 = -5002
DISPID_ACC_NAME: Int32 = -5003
DISPID_ACC_VALUE: Int32 = -5004
DISPID_ACC_DESCRIPTION: Int32 = -5005
DISPID_ACC_ROLE: Int32 = -5006
DISPID_ACC_STATE: Int32 = -5007
DISPID_ACC_HELP: Int32 = -5008
DISPID_ACC_HELPTOPIC: Int32 = -5009
DISPID_ACC_KEYBOARDSHORTCUT: Int32 = -5010
DISPID_ACC_FOCUS: Int32 = -5011
DISPID_ACC_SELECTION: Int32 = -5012
DISPID_ACC_DEFAULTACTION: Int32 = -5013
DISPID_ACC_SELECT: Int32 = -5014
DISPID_ACC_LOCATION: Int32 = -5015
DISPID_ACC_NAVIGATE: Int32 = -5016
DISPID_ACC_HITTEST: Int32 = -5017
DISPID_ACC_DODEFAULTACTION: Int32 = -5018
NAVDIR_MIN: UInt32 = 0
NAVDIR_UP: UInt32 = 1
NAVDIR_DOWN: UInt32 = 2
NAVDIR_LEFT: UInt32 = 3
NAVDIR_RIGHT: UInt32 = 4
NAVDIR_NEXT: UInt32 = 5
NAVDIR_PREVIOUS: UInt32 = 6
NAVDIR_FIRSTCHILD: UInt32 = 7
NAVDIR_LASTCHILD: UInt32 = 8
NAVDIR_MAX: UInt32 = 9
SELFLAG_NONE: UInt32 = 0
SELFLAG_TAKEFOCUS: UInt32 = 1
SELFLAG_TAKESELECTION: UInt32 = 2
SELFLAG_EXTENDSELECTION: UInt32 = 4
SELFLAG_ADDSELECTION: UInt32 = 8
SELFLAG_REMOVESELECTION: UInt32 = 16
SELFLAG_VALID: UInt32 = 31
STATE_SYSTEM_NORMAL: UInt32 = 0
STATE_SYSTEM_HASPOPUP: UInt32 = 1073741824
ROLE_SYSTEM_TITLEBAR: UInt32 = 1
ROLE_SYSTEM_MENUBAR: UInt32 = 2
ROLE_SYSTEM_SCROLLBAR: UInt32 = 3
ROLE_SYSTEM_GRIP: UInt32 = 4
ROLE_SYSTEM_SOUND: UInt32 = 5
ROLE_SYSTEM_CURSOR: UInt32 = 6
ROLE_SYSTEM_CARET: UInt32 = 7
ROLE_SYSTEM_ALERT: UInt32 = 8
ROLE_SYSTEM_WINDOW: UInt32 = 9
ROLE_SYSTEM_CLIENT: UInt32 = 10
ROLE_SYSTEM_MENUPOPUP: UInt32 = 11
ROLE_SYSTEM_MENUITEM: UInt32 = 12
ROLE_SYSTEM_TOOLTIP: UInt32 = 13
ROLE_SYSTEM_APPLICATION: UInt32 = 14
ROLE_SYSTEM_DOCUMENT: UInt32 = 15
ROLE_SYSTEM_PANE: UInt32 = 16
ROLE_SYSTEM_CHART: UInt32 = 17
ROLE_SYSTEM_DIALOG: UInt32 = 18
ROLE_SYSTEM_BORDER: UInt32 = 19
ROLE_SYSTEM_GROUPING: UInt32 = 20
ROLE_SYSTEM_SEPARATOR: UInt32 = 21
ROLE_SYSTEM_TOOLBAR: UInt32 = 22
ROLE_SYSTEM_STATUSBAR: UInt32 = 23
ROLE_SYSTEM_TABLE: UInt32 = 24
ROLE_SYSTEM_COLUMNHEADER: UInt32 = 25
ROLE_SYSTEM_ROWHEADER: UInt32 = 26
ROLE_SYSTEM_COLUMN: UInt32 = 27
ROLE_SYSTEM_ROW: UInt32 = 28
ROLE_SYSTEM_CELL: UInt32 = 29
ROLE_SYSTEM_LINK: UInt32 = 30
ROLE_SYSTEM_HELPBALLOON: UInt32 = 31
ROLE_SYSTEM_CHARACTER: UInt32 = 32
ROLE_SYSTEM_LIST: UInt32 = 33
ROLE_SYSTEM_LISTITEM: UInt32 = 34
ROLE_SYSTEM_OUTLINE: UInt32 = 35
ROLE_SYSTEM_OUTLINEITEM: UInt32 = 36
ROLE_SYSTEM_PAGETAB: UInt32 = 37
ROLE_SYSTEM_PROPERTYPAGE: UInt32 = 38
ROLE_SYSTEM_INDICATOR: UInt32 = 39
ROLE_SYSTEM_GRAPHIC: UInt32 = 40
ROLE_SYSTEM_STATICTEXT: UInt32 = 41
ROLE_SYSTEM_TEXT: UInt32 = 42
ROLE_SYSTEM_PUSHBUTTON: UInt32 = 43
ROLE_SYSTEM_CHECKBUTTON: UInt32 = 44
ROLE_SYSTEM_RADIOBUTTON: UInt32 = 45
ROLE_SYSTEM_COMBOBOX: UInt32 = 46
ROLE_SYSTEM_DROPLIST: UInt32 = 47
ROLE_SYSTEM_PROGRESSBAR: UInt32 = 48
ROLE_SYSTEM_DIAL: UInt32 = 49
ROLE_SYSTEM_HOTKEYFIELD: UInt32 = 50
ROLE_SYSTEM_SLIDER: UInt32 = 51
ROLE_SYSTEM_SPINBUTTON: UInt32 = 52
ROLE_SYSTEM_DIAGRAM: UInt32 = 53
ROLE_SYSTEM_ANIMATION: UInt32 = 54
ROLE_SYSTEM_EQUATION: UInt32 = 55
ROLE_SYSTEM_BUTTONDROPDOWN: UInt32 = 56
ROLE_SYSTEM_BUTTONMENU: UInt32 = 57
ROLE_SYSTEM_BUTTONDROPDOWNGRID: UInt32 = 58
ROLE_SYSTEM_WHITESPACE: UInt32 = 59
ROLE_SYSTEM_PAGETABLIST: UInt32 = 60
ROLE_SYSTEM_CLOCK: UInt32 = 61
ROLE_SYSTEM_SPLITBUTTON: UInt32 = 62
ROLE_SYSTEM_IPADDRESS: UInt32 = 63
ROLE_SYSTEM_OUTLINEBUTTON: UInt32 = 64
UIA_E_ELEMENTNOTENABLED: UInt32 = 2147746304
UIA_E_ELEMENTNOTAVAILABLE: UInt32 = 2147746305
UIA_E_NOCLICKABLEPOINT: UInt32 = 2147746306
UIA_E_PROXYASSEMBLYNOTLOADED: UInt32 = 2147746307
UIA_E_NOTSUPPORTED: UInt32 = 2147746308
UIA_E_INVALIDOPERATION: UInt32 = 2148734217
UIA_E_TIMEOUT: UInt32 = 2148734213
UiaAppendRuntimeId: UInt32 = 3
UiaRootObjectId: Int32 = -25
RuntimeId_Property_GUID: Guid = Guid('a39eebfa-7fba-4c89-b4-d4-b9-9e-2d-e7-d1-60')
BoundingRectangle_Property_GUID: Guid = Guid('7bbfe8b2-3bfc-48dd-b7-29-c7-94-b8-46-e9-a1')
ProcessId_Property_GUID: Guid = Guid('40499998-9c31-4245-a4-03-87-32-0e-59-ea-f6')
ControlType_Property_GUID: Guid = Guid('ca774fea-28ac-4bc2-94-ca-ac-ec-6d-6c-10-a3')
LocalizedControlType_Property_GUID: Guid = Guid('8763404f-a1bd-452a-89-c4-3f-01-d3-83-38-06')
Name_Property_GUID: Guid = Guid('c3a6921b-4a99-44f1-bc-a6-61-18-70-52-c4-31')
AcceleratorKey_Property_GUID: Guid = Guid('514865df-2557-4cb9-ae-ed-6c-ed-08-4c-e5-2c')
AccessKey_Property_GUID: Guid = Guid('06827b12-a7f9-4a15-91-7c-ff-a5-ad-3e-b0-a7')
HasKeyboardFocus_Property_GUID: Guid = Guid('cf8afd39-3f46-4800-96-56-b2-bf-12-52-99-05')
IsKeyboardFocusable_Property_GUID: Guid = Guid('f7b8552a-0859-4b37-b9-cb-51-e7-20-92-f2-9f')
IsEnabled_Property_GUID: Guid = Guid('2109427f-da60-4fed-bf-1b-26-4b-dc-e6-eb-3a')
AutomationId_Property_GUID: Guid = Guid('c82c0500-b60e-4310-a2-67-30-3c-53-1f-8e-e5')
ClassName_Property_GUID: Guid = Guid('157b7215-894f-4b65-84-e2-aa-c0-da-08-b1-6b')
HelpText_Property_GUID: Guid = Guid('08555685-0977-45c7-a7-a6-ab-af-56-84-12-1a')
ClickablePoint_Property_GUID: Guid = Guid('0196903b-b203-4818-a9-f3-f0-8e-67-5f-23-41')
Culture_Property_GUID: Guid = Guid('e2d74f27-3d79-4dc2-b8-8b-30-44-96-3a-8a-fb')
IsControlElement_Property_GUID: Guid = Guid('95f35085-abcc-4afd-a5-f4-db-b4-6c-23-0f-db')
IsContentElement_Property_GUID: Guid = Guid('4bda64a8-f5d8-480b-81-55-ef-2e-89-ad-b6-72')
LabeledBy_Property_GUID: Guid = Guid('e5b8924b-fc8a-4a35-80-31-cf-78-ac-43-e5-5e')
IsPassword_Property_GUID: Guid = Guid('e8482eb1-687c-497b-be-bc-03-be-53-ec-14-54')
NewNativeWindowHandle_Property_GUID: Guid = Guid('5196b33b-380a-4982-95-e1-91-f3-ef-60-e0-24')
ItemType_Property_GUID: Guid = Guid('cdda434d-6222-413b-a6-8a-32-5d-d1-d4-0f-39')
IsOffscreen_Property_GUID: Guid = Guid('03c3d160-db79-42db-a2-ef-1c-23-1e-ed-e5-07')
Orientation_Property_GUID: Guid = Guid('a01eee62-3884-4415-88-7e-67-8e-c2-1e-39-ba')
FrameworkId_Property_GUID: Guid = Guid('dbfd9900-7e1a-4f58-b6-1b-70-63-12-0f-77-3b')
IsRequiredForForm_Property_GUID: Guid = Guid('4f5f43cf-59fb-4bde-a2-70-60-2e-5e-11-41-e9')
ItemStatus_Property_GUID: Guid = Guid('51de0321-3973-43e7-89-13-0b-08-e8-13-c3-7f')
AriaRole_Property_GUID: Guid = Guid('dd207b95-be4a-4e0d-b7-27-63-ac-e9-4b-69-16')
AriaProperties_Property_GUID: Guid = Guid('4213678c-e025-4922-be-b5-e4-3b-a0-8e-62-21')
IsDataValidForForm_Property_GUID: Guid = Guid('445ac684-c3fc-4dd9-ac-f8-84-5a-57-92-96-ba')
ControllerFor_Property_GUID: Guid = Guid('51124c8a-a5d2-4f13-9b-e6-7f-a8-ba-9d-3a-90')
DescribedBy_Property_GUID: Guid = Guid('7c5865b8-9992-40fd-8d-b0-6b-f1-d3-17-f9-98')
FlowsTo_Property_GUID: Guid = Guid('e4f33d20-559a-47fb-a8-30-f9-cb-4f-f1-a7-0a')
ProviderDescription_Property_GUID: Guid = Guid('dca5708a-c16b-4cd9-b8-89-be-b1-6a-80-49-04')
OptimizeForVisualContent_Property_GUID: Guid = Guid('6a852250-c75a-4e5d-b8-58-e3-81-b0-f7-88-61')
IsDockPatternAvailable_Property_GUID: Guid = Guid('2600a4c4-2ff8-4c96-ae-31-8f-e6-19-a1-3c-6c')
IsExpandCollapsePatternAvailable_Property_GUID: Guid = Guid('929d3806-5287-4725-aa-16-22-2a-fc-63-d5-95')
IsGridItemPatternAvailable_Property_GUID: Guid = Guid('5a43e524-f9a2-4b12-84-c8-b4-8a-3e-fe-dd-34')
IsGridPatternAvailable_Property_GUID: Guid = Guid('5622c26c-f0ef-4f3b-97-cb-71-4c-08-68-58-8b')
IsInvokePatternAvailable_Property_GUID: Guid = Guid('4e725738-8364-4679-aa-6c-f3-f4-19-31-f7-50')
IsMultipleViewPatternAvailable_Property_GUID: Guid = Guid('ff0a31eb-8e25-469d-8d-6e-e7-71-a2-7c-1b-90')
IsRangeValuePatternAvailable_Property_GUID: Guid = Guid('fda4244a-eb4d-43ff-b5-ad-ed-36-d3-73-ec-4c')
IsScrollPatternAvailable_Property_GUID: Guid = Guid('3ebb7b4a-828a-4b57-9d-22-2f-ea-16-32-ed-0d')
IsScrollItemPatternAvailable_Property_GUID: Guid = Guid('1cad1a05-0927-4b76-97-e1-0f-cd-b2-09-b9-8a')
IsSelectionItemPatternAvailable_Property_GUID: Guid = Guid('8becd62d-0bc3-4109-be-e2-8e-67-15-29-0e-68')
IsSelectionPatternAvailable_Property_GUID: Guid = Guid('f588acbe-c769-4838-9a-60-26-86-dc-11-88-c4')
IsTablePatternAvailable_Property_GUID: Guid = Guid('cb83575f-45c2-4048-9c-76-15-97-15-a1-39-df')
IsTableItemPatternAvailable_Property_GUID: Guid = Guid('eb36b40d-8ea4-489b-a0-13-e6-0d-59-51-fe-34')
IsTextPatternAvailable_Property_GUID: Guid = Guid('fbe2d69d-aff6-4a45-82-e2-fc-92-a8-2f-59-17')
IsTogglePatternAvailable_Property_GUID: Guid = Guid('78686d53-fcd0-4b83-9b-78-58-32-ce-63-bb-5b')
IsTransformPatternAvailable_Property_GUID: Guid = Guid('a7f78804-d68b-4077-a5-c6-7a-5e-a1-ac-31-c5')
IsValuePatternAvailable_Property_GUID: Guid = Guid('0b5020a7-2119-473b-be-37-5c-eb-98-bb-fb-22')
IsWindowPatternAvailable_Property_GUID: Guid = Guid('e7a57bb1-5888-4155-98-dc-b4-22-fd-57-f2-bc')
IsLegacyIAccessiblePatternAvailable_Property_GUID: Guid = Guid('d8ebd0c7-929a-4ee7-8d-3a-d3-d9-44-13-02-7b')
IsItemContainerPatternAvailable_Property_GUID: Guid = Guid('624b5ca7-fe40-4957-a0-19-20-c4-cf-11-92-0f')
IsVirtualizedItemPatternAvailable_Property_GUID: Guid = Guid('302cb151-2ac8-45d6-97-7b-d2-b3-a5-a5-3f-20')
IsSynchronizedInputPatternAvailable_Property_GUID: Guid = Guid('75d69cc5-d2bf-4943-87-6e-b4-5b-62-a6-cc-66')
IsObjectModelPatternAvailable_Property_GUID: Guid = Guid('6b21d89b-2841-412f-8e-f2-15-ca-95-23-18-ba')
IsAnnotationPatternAvailable_Property_GUID: Guid = Guid('0b5b3238-6d5c-41b6-bc-c4-5e-80-7f-65-51-c4')
IsTextPattern2Available_Property_GUID: Guid = Guid('41cf921d-e3f1-4b22-9c-81-e1-c3-ed-33-1c-22')
IsTextEditPatternAvailable_Property_GUID: Guid = Guid('7843425c-8b32-484c-9a-b5-e3-20-05-71-ff-da')
IsCustomNavigationPatternAvailable_Property_GUID: Guid = Guid('8f8e80d4-2351-48e0-87-4a-54-aa-73-13-88-9a')
IsStylesPatternAvailable_Property_GUID: Guid = Guid('27f353d3-459c-4b59-a4-90-50-61-1d-ac-af-b5')
IsSpreadsheetPatternAvailable_Property_GUID: Guid = Guid('6ff43732-e4b4-4555-97-bc-ec-db-bc-4d-18-88')
IsSpreadsheetItemPatternAvailable_Property_GUID: Guid = Guid('9fe79b2a-2f94-43fd-99-6b-54-9e-31-6f-4a-cd')
IsTransformPattern2Available_Property_GUID: Guid = Guid('25980b4b-be04-4710-ab-4a-fd-a3-1d-bd-28-95')
IsTextChildPatternAvailable_Property_GUID: Guid = Guid('559e65df-30ff-43b5-b5-ed-5b-28-3b-80-c7-e9')
IsDragPatternAvailable_Property_GUID: Guid = Guid('e997a7b7-1d39-4ca7-be-0f-27-7f-cf-56-05-cc')
IsDropTargetPatternAvailable_Property_GUID: Guid = Guid('0686b62e-8e19-4aaf-87-3d-38-4f-6d-3b-92-be')
IsStructuredMarkupPatternAvailable_Property_GUID: Guid = Guid('b0d4c196-2c0b-489c-b1-65-a4-05-92-8c-6f-3d')
IsPeripheral_Property_GUID: Guid = Guid('da758276-7ed5-49d4-8e-68-ec-c9-a2-d3-00-dd')
PositionInSet_Property_GUID: Guid = Guid('33d1dc54-641e-4d76-a6-b1-13-f3-41-c1-f8-96')
SizeOfSet_Property_GUID: Guid = Guid('1600d33c-3b9f-4369-94-31-aa-29-3f-34-4c-f1')
Level_Property_GUID: Guid = Guid('242ac529-cd36-400f-aa-d9-78-76-ef-3a-f6-27')
AnnotationTypes_Property_GUID: Guid = Guid('64b71f76-53c4-4696-a2-19-20-e9-40-c9-a1-76')
AnnotationObjects_Property_GUID: Guid = Guid('310910c8-7c6e-4f20-be-cd-4a-af-6d-19-11-56')
LandmarkType_Property_GUID: Guid = Guid('454045f2-6f61-49f7-a4-f8-b5-f0-cf-82-da-1e')
LocalizedLandmarkType_Property_GUID: Guid = Guid('7ac81980-eafb-4fb2-bf-91-f4-85-be-f5-e8-e1')
FullDescription_Property_GUID: Guid = Guid('0d4450ff-6aef-4f33-95-dd-7b-ef-a7-2a-43-91')
Value_Value_Property_GUID: Guid = Guid('e95f5e64-269f-4a85-ba-99-40-92-c3-ea-29-86')
Value_IsReadOnly_Property_GUID: Guid = Guid('eb090f30-e24c-4799-a7-05-0d-24-7b-c0-37-f8')
RangeValue_Value_Property_GUID: Guid = Guid('131f5d98-c50c-489d-ab-e5-ae-22-08-98-c5-f7')
RangeValue_IsReadOnly_Property_GUID: Guid = Guid('25fa1055-debf-4373-a7-9e-1f-1a-19-08-d3-c4')
RangeValue_Minimum_Property_GUID: Guid = Guid('78cbd3b2-684d-4860-af-93-d1-f9-5c-b0-22-fd')
RangeValue_Maximum_Property_GUID: Guid = Guid('19319914-f979-4b35-a1-a6-d3-7e-05-43-34-73')
RangeValue_LargeChange_Property_GUID: Guid = Guid('a1f96325-3a3d-4b44-8e-1f-4a-46-d9-84-40-19')
RangeValue_SmallChange_Property_GUID: Guid = Guid('81c2c457-3941-4107-99-75-13-97-60-f7-c0-72')
Scroll_HorizontalScrollPercent_Property_GUID: Guid = Guid('c7c13c0e-eb21-47ff-ac-c4-b5-a3-35-0f-51-91')
Scroll_HorizontalViewSize_Property_GUID: Guid = Guid('70c2e5d4-fcb0-4713-a9-aa-af-92-ff-79-e4-cd')
Scroll_VerticalScrollPercent_Property_GUID: Guid = Guid('6c8d7099-b2a8-4948-bf-f7-3c-f9-05-8b-fe-fb')
Scroll_VerticalViewSize_Property_GUID: Guid = Guid('de6a2e22-d8c7-40c5-83-ba-e5-f6-81-d5-31-08')
Scroll_HorizontallyScrollable_Property_GUID: Guid = Guid('8b925147-28cd-49ae-bd-63-f4-41-18-d2-e7-19')
Scroll_VerticallyScrollable_Property_GUID: Guid = Guid('89164798-0068-4315-b8-9a-1e-7c-fb-bc-3d-fc')
Selection_Selection_Property_GUID: Guid = Guid('aa6dc2a2-0e2b-4d38-96-d5-34-e4-70-b8-18-53')
Selection_CanSelectMultiple_Property_GUID: Guid = Guid('49d73da5-c883-4500-88-3d-8f-cf-8d-af-6c-be')
Selection_IsSelectionRequired_Property_GUID: Guid = Guid('b1ae4422-63fe-44e7-a5-a5-a7-38-c8-29-b1-9a')
Grid_RowCount_Property_GUID: Guid = Guid('2a9505bf-c2eb-4fb6-b3-56-82-45-ae-53-70-3e')
Grid_ColumnCount_Property_GUID: Guid = Guid('fe96f375-44aa-4536-ac-7a-2a-75-d7-1a-3e-fc')
GridItem_Row_Property_GUID: Guid = Guid('6223972a-c945-4563-93-29-fd-c9-74-af-25-53')
GridItem_Column_Property_GUID: Guid = Guid('c774c15c-62c0-4519-8b-dc-47-be-57-3c-8a-d5')
GridItem_RowSpan_Property_GUID: Guid = Guid('4582291c-466b-4e93-8e-83-3d-17-15-ec-0c-5e')
GridItem_ColumnSpan_Property_GUID: Guid = Guid('583ea3f5-86d0-4b08-a6-ec-2c-54-63-ff-c1-09')
GridItem_Parent_Property_GUID: Guid = Guid('9d912252-b97f-4ecc-85-10-ea-0e-33-42-7c-72')
Dock_DockPosition_Property_GUID: Guid = Guid('6d67f02e-c0b0-4b10-b5-b9-18-d6-ec-f9-87-60')
ExpandCollapse_ExpandCollapseState_Property_GUID: Guid = Guid('275a4c48-85a7-4f69-ab-a0-af-15-76-10-00-2b')
MultipleView_CurrentView_Property_GUID: Guid = Guid('7a81a67a-b94f-4875-91-8b-65-c8-d2-f9-98-e5')
MultipleView_SupportedViews_Property_GUID: Guid = Guid('8d5db9fd-ce3c-4ae7-b7-88-40-0a-3c-64-55-47')
Window_CanMaximize_Property_GUID: Guid = Guid('64fff53f-635d-41c1-95-0c-cb-5a-df-be-28-e3')
Window_CanMinimize_Property_GUID: Guid = Guid('b73b4625-5988-4b97-b4-c2-a6-fe-6e-78-c8-c6')
Window_WindowVisualState_Property_GUID: Guid = Guid('4ab7905f-e860-453e-a3-0a-f6-43-1e-5d-aa-d5')
Window_WindowInteractionState_Property_GUID: Guid = Guid('4fed26a4-0455-4fa2-b2-1c-c4-da-2d-b1-ff-9c')
Window_IsModal_Property_GUID: Guid = Guid('ff4e6892-37b9-4fca-85-32-ff-e6-74-ec-fe-ed')
Window_IsTopmost_Property_GUID: Guid = Guid('ef7d85d3-0937-4962-92-41-b6-23-45-f2-40-41')
SelectionItem_IsSelected_Property_GUID: Guid = Guid('f122835f-cd5f-43df-b7-9d-4b-84-9e-9e-60-20')
SelectionItem_SelectionContainer_Property_GUID: Guid = Guid('a4365b6e-9c1e-4b63-8b-53-c2-42-1d-d1-e8-fb')
Table_RowHeaders_Property_GUID: Guid = Guid('d9e35b87-6eb8-4562-aa-c6-a8-a9-07-52-36-a8')
Table_ColumnHeaders_Property_GUID: Guid = Guid('aff1d72b-968d-42b1-b4-59-15-0b-29-9d-a6-64')
Table_RowOrColumnMajor_Property_GUID: Guid = Guid('83be75c3-29fe-4a30-85-e1-2a-62-77-fd-10-6e')
TableItem_RowHeaderItems_Property_GUID: Guid = Guid('b3f853a0-0574-4cd8-bc-d7-ed-59-23-57-2d-97')
TableItem_ColumnHeaderItems_Property_GUID: Guid = Guid('967a56a3-74b6-431e-8d-e6-99-c4-11-03-1c-58')
Toggle_ToggleState_Property_GUID: Guid = Guid('b23cdc52-22c2-4c6c-9d-ed-f5-c4-22-47-9e-de')
Transform_CanMove_Property_GUID: Guid = Guid('1b75824d-208b-4fdf-bc-cd-f1-f4-e5-74-1f-4f')
Transform_CanResize_Property_GUID: Guid = Guid('bb98dca5-4c1a-41d4-a4-f6-eb-c1-28-64-41-80')
Transform_CanRotate_Property_GUID: Guid = Guid('10079b48-3849-476f-ac-96-44-a9-5c-84-40-d9')
LegacyIAccessible_ChildId_Property_GUID: Guid = Guid('9a191b5d-9ef2-4787-a4-59-dc-de-88-5d-d4-e8')
LegacyIAccessible_Name_Property_GUID: Guid = Guid('caeb063d-40ae-4869-aa-5a-1b-8e-5d-66-67-39')
LegacyIAccessible_Value_Property_GUID: Guid = Guid('b5c5b0b6-8217-4a77-97-a5-19-0a-85-ed-01-56')
LegacyIAccessible_Description_Property_GUID: Guid = Guid('46448418-7d70-4ea9-9d-27-b7-e7-75-cf-2a-d7')
LegacyIAccessible_Role_Property_GUID: Guid = Guid('6856e59f-cbaf-4e31-93-e8-bc-bf-6f-7e-49-1c')
LegacyIAccessible_State_Property_GUID: Guid = Guid('df985854-2281-4340-ab-9c-c6-0e-2c-58-03-f6')
LegacyIAccessible_Help_Property_GUID: Guid = Guid('94402352-161c-4b77-a9-8d-a8-72-cc-33-94-7a')
LegacyIAccessible_KeyboardShortcut_Property_GUID: Guid = Guid('8f6909ac-00b8-4259-a4-1c-96-62-66-d4-3a-8a')
LegacyIAccessible_Selection_Property_GUID: Guid = Guid('8aa8b1e0-0891-40cc-8b-06-90-d7-d4-16-62-19')
LegacyIAccessible_DefaultAction_Property_GUID: Guid = Guid('3b331729-eaad-4502-b8-5f-92-61-56-22-91-3c')
Annotation_AnnotationTypeId_Property_GUID: Guid = Guid('20ae484f-69ef-4c48-8f-5b-c4-93-8b-20-6a-c7')
Annotation_AnnotationTypeName_Property_GUID: Guid = Guid('9b818892-5ac9-4af9-aa-96-f5-8a-77-b0-58-e3')
Annotation_Author_Property_GUID: Guid = Guid('7a528462-9c5c-4a03-a9-74-8b-30-7a-99-37-f2')
Annotation_DateTime_Property_GUID: Guid = Guid('99b5ca5d-1acf-414b-a4-d0-6b-35-0b-04-75-78')
Annotation_Target_Property_GUID: Guid = Guid('b71b302d-2104-44ad-9c-5c-09-2b-49-07-d7-0f')
Styles_StyleId_Property_GUID: Guid = Guid('da82852f-3817-4233-82-af-02-27-9e-72-cc-77')
Styles_StyleName_Property_GUID: Guid = Guid('1c12b035-05d1-4f55-9e-8e-14-89-f3-ff-55-0d')
Styles_FillColor_Property_GUID: Guid = Guid('63eff97a-a1c5-4b1d-84-eb-b7-65-f2-ed-d6-32')
Styles_FillPatternStyle_Property_GUID: Guid = Guid('81cf651f-482b-4451-a3-0a-e1-54-5e-55-4f-b8')
Styles_Shape_Property_GUID: Guid = Guid('c71a23f8-778c-400d-84-58-3b-54-3e-52-69-84')
Styles_FillPatternColor_Property_GUID: Guid = Guid('939a59fe-8fbd-4e75-a2-71-ac-45-95-19-51-63')
Styles_ExtendedProperties_Property_GUID: Guid = Guid('f451cda0-ba0a-4681-b0-b0-0d-bd-b5-3e-58-f3')
SpreadsheetItem_Formula_Property_GUID: Guid = Guid('e602e47d-1b47-4bea-87-cf-3b-0b-0b-5c-15-b6')
SpreadsheetItem_AnnotationObjects_Property_GUID: Guid = Guid('a3194c38-c9bc-4604-93-96-ae-3f-9f-45-7f-7b')
SpreadsheetItem_AnnotationTypes_Property_GUID: Guid = Guid('c70c51d0-d602-4b45-af-bc-b4-71-2b-96-d7-2b')
Transform2_CanZoom_Property_GUID: Guid = Guid('f357e890-a756-4359-9c-a6-86-70-2b-f8-f3-81')
LiveSetting_Property_GUID: Guid = Guid('c12bcd8e-2a8e-4950-8a-e7-36-25-11-1d-58-eb')
Drag_IsGrabbed_Property_GUID: Guid = Guid('45f206f3-75cc-4cca-a9-b9-fc-df-b9-82-d8-a2')
Drag_GrabbedItems_Property_GUID: Guid = Guid('77c1562c-7b86-4b21-9e-d7-3c-ef-da-6f-4c-43')
Drag_DropEffect_Property_GUID: Guid = Guid('646f2779-48d3-4b23-89-02-4b-f1-00-00-5d-f3')
Drag_DropEffects_Property_GUID: Guid = Guid('f5d61156-7ce6-49be-a8-36-92-69-dc-ec-92-0f')
DropTarget_DropTargetEffect_Property_GUID: Guid = Guid('8bb75975-a0ca-4981-b8-18-87-fc-66-e9-50-9d')
DropTarget_DropTargetEffects_Property_GUID: Guid = Guid('bc1dd4ed-cb89-45f1-a5-92-e0-3b-08-ae-79-0f')
Transform2_ZoomLevel_Property_GUID: Guid = Guid('eee29f1a-f4a2-4b5b-ac-65-95-cf-93-28-33-87')
Transform2_ZoomMinimum_Property_GUID: Guid = Guid('742ccc16-4ad1-4e07-96-fe-b1-22-c6-e6-b2-2b')
Transform2_ZoomMaximum_Property_GUID: Guid = Guid('42ab6b77-ceb0-4eca-b8-2a-6c-fa-5f-a1-fc-08')
FlowsFrom_Property_GUID: Guid = Guid('05c6844f-19de-48f8-95-fa-88-0d-5b-0f-d6-15')
FillColor_Property_GUID: Guid = Guid('6e0ec4d0-e2a8-4a56-9d-e7-95-33-89-93-3b-39')
OutlineColor_Property_GUID: Guid = Guid('c395d6c0-4b55-4762-a0-73-fd-30-3a-63-4f-52')
FillType_Property_GUID: Guid = Guid('c6fc74e4-8cb9-429c-a9-e1-9b-c4-ac-37-2b-62')
VisualEffects_Property_GUID: Guid = Guid('e61a8565-aad9-46d7-9e-70-4e-8a-84-20-d4-20')
OutlineThickness_Property_GUID: Guid = Guid('13e67cc7-dac2-4888-bd-d3-37-5c-62-fa-96-18')
CenterPoint_Property_GUID: Guid = Guid('0cb00c08-540c-4edb-94-45-26-35-9e-a6-97-85')
Rotation_Property_GUID: Guid = Guid('767cdc7d-aec0-4110-ad-32-30-ed-d4-03-49-2e')
Size_Property_GUID: Guid = Guid('2b5f761d-f885-4404-97-3f-9b-1d-98-e3-6d-8f')
ToolTipOpened_Event_GUID: Guid = Guid('3f4b97ff-2edc-451d-bc-a4-95-a3-18-8d-5b-03')
ToolTipClosed_Event_GUID: Guid = Guid('276d71ef-24a9-49b6-8e-97-da-98-b4-01-bb-cd')
StructureChanged_Event_GUID: Guid = Guid('59977961-3edd-4b11-b1-3b-67-6b-2a-2a-6c-a9')
MenuOpened_Event_GUID: Guid = Guid('ebe2e945-66ca-4ed1-9f-f8-2a-d7-df-0a-1b-08')
AutomationPropertyChanged_Event_GUID: Guid = Guid('2527fba1-8d7a-4630-a4-cc-e6-63-15-94-2f-52')
AutomationFocusChanged_Event_GUID: Guid = Guid('b68a1f17-f60d-41a7-a3-cc-b0-52-92-15-5f-e0')
ActiveTextPositionChanged_Event_GUID: Guid = Guid('a5c09e9c-c77d-4f25-b4-91-e5-bb-70-17-cb-d4')
AsyncContentLoaded_Event_GUID: Guid = Guid('5fdee11c-d2fa-4fb9-90-4e-5c-be-e8-94-d5-ef')
MenuClosed_Event_GUID: Guid = Guid('3cf1266e-1582-4041-ac-d7-88-a3-5a-96-52-97')
LayoutInvalidated_Event_GUID: Guid = Guid('ed7d6544-a6bd-4595-9b-ae-3d-28-94-6c-c7-15')
Invoke_Invoked_Event_GUID: Guid = Guid('dfd699f0-c915-49dd-b4-22-dd-e7-85-c3-d2-4b')
SelectionItem_ElementAddedToSelectionEvent_Event_GUID: Guid = Guid('3c822dd1-c407-4dba-91-dd-79-d4-ae-d0-ae-c6')
SelectionItem_ElementRemovedFromSelectionEvent_Event_GUID: Guid = Guid('097fa8a9-7079-41af-8b-9c-09-34-d8-30-5e-5c')
SelectionItem_ElementSelectedEvent_Event_GUID: Guid = Guid('b9c7dbfb-4ebe-4532-aa-f4-00-8c-f6-47-23-3c')
Selection_InvalidatedEvent_Event_GUID: Guid = Guid('cac14904-16b4-4b53-8e-47-4c-b1-df-26-7b-b7')
Text_TextSelectionChangedEvent_Event_GUID: Guid = Guid('918edaa1-71b3-49ae-97-41-79-be-b8-d3-58-f3')
Text_TextChangedEvent_Event_GUID: Guid = Guid('4a342082-f483-48c4-ac-11-a8-4b-43-5e-2a-84')
Window_WindowOpened_Event_GUID: Guid = Guid('d3e81d06-de45-4f2f-96-33-de-9e-02-fb-65-af')
Window_WindowClosed_Event_GUID: Guid = Guid('edf141f8-fa67-4e22-bb-f7-94-4e-05-73-5e-e2')
MenuModeStart_Event_GUID: Guid = Guid('18d7c631-166a-4ac9-ae-3b-ef-4b-54-20-e6-81')
MenuModeEnd_Event_GUID: Guid = Guid('9ecd4c9f-80dd-47b8-82-67-5a-ec-06-bb-2c-ff')
InputReachedTarget_Event_GUID: Guid = Guid('93ed549a-0549-40f0-be-db-28-e4-4f-7d-e2-a3')
InputReachedOtherElement_Event_GUID: Guid = Guid('ed201d8a-4e6c-415e-a8-74-24-60-c9-b6-6b-a8')
InputDiscarded_Event_GUID: Guid = Guid('7f36c367-7b18-417c-97-e3-9d-58-dd-c9-44-ab')
SystemAlert_Event_GUID: Guid = Guid('d271545d-7a3a-47a7-84-74-81-d2-9a-24-51-c9')
LiveRegionChanged_Event_GUID: Guid = Guid('102d5e90-e6a9-41b6-b1-c5-a9-b1-92-9d-95-10')
HostedFragmentRootsInvalidated_Event_GUID: Guid = Guid('e6bdb03e-0921-4ec5-8d-cf-ea-e8-77-b0-42-6b')
Drag_DragStart_Event_GUID: Guid = Guid('883a480b-3aa9-429d-95-e4-d9-c8-d0-11-f0-dd')
Drag_DragCancel_Event_GUID: Guid = Guid('c3ede6fa-3451-4e0f-9e-71-df-9c-28-0a-46-57')
Drag_DragComplete_Event_GUID: Guid = Guid('38e96188-ef1f-463e-91-ca-3a-77-92-c2-9c-af')
DropTarget_DragEnter_Event_GUID: Guid = Guid('aad9319b-032c-4a88-96-1d-1c-f5-79-58-1e-34')
DropTarget_DragLeave_Event_GUID: Guid = Guid('0f82eb15-24a2-4988-92-17-de-16-2a-ee-27-2b')
DropTarget_Dropped_Event_GUID: Guid = Guid('622cead8-1edb-4a3d-ab-bc-be-22-11-ff-68-b5')
StructuredMarkup_CompositionComplete_Event_GUID: Guid = Guid('c48a3c17-677a-4047-a6-8d-fc-12-57-52-8a-ef')
StructuredMarkup_Deleted_Event_GUID: Guid = Guid('f9d0a020-e1c1-4ecf-b9-aa-52-ef-de-7e-41-e1')
StructuredMarkup_SelectionChanged_Event_GUID: Guid = Guid('a7c815f7-ff9f-41c7-a3-a7-ab-6c-bf-db-49-03')
Invoke_Pattern_GUID: Guid = Guid('d976c2fc-66ea-4a6e-b2-8f-c2-4c-75-46-ad-37')
Selection_Pattern_GUID: Guid = Guid('66e3b7e8-d821-4d25-87-61-43-5d-2c-8b-25-3f')
Value_Pattern_GUID: Guid = Guid('17faad9e-c877-475b-b9-33-77-33-27-79-b6-37')
RangeValue_Pattern_GUID: Guid = Guid('18b00d87-b1c9-476a-bf-bd-5f-0b-db-92-6f-63')
Scroll_Pattern_GUID: Guid = Guid('895fa4b4-759d-4c50-8e-15-03-46-06-72-00-3c')
ExpandCollapse_Pattern_GUID: Guid = Guid('ae05efa2-f9d1-428a-83-4c-53-a5-c5-2f-9b-8b')
Grid_Pattern_GUID: Guid = Guid('260a2ccb-93a8-4e44-a4-c1-3d-f3-97-f2-b0-2b')
GridItem_Pattern_GUID: Guid = Guid('f2d5c877-a462-4957-a2-a5-2c-96-b3-03-bc-63')
MultipleView_Pattern_GUID: Guid = Guid('547a6ae4-113f-47c4-85-0f-db-4d-fa-46-6b-1d')
Window_Pattern_GUID: Guid = Guid('27901735-c760-4994-ad-11-59-19-e6-06-b1-10')
SelectionItem_Pattern_GUID: Guid = Guid('9bc64eeb-87c7-4b28-94-bb-4d-9f-a4-37-b6-ef')
Dock_Pattern_GUID: Guid = Guid('9cbaa846-83c8-428d-82-7f-7e-60-63-fe-06-20')
Table_Pattern_GUID: Guid = Guid('c415218e-a028-461e-aa-92-8f-92-5c-f7-93-51')
TableItem_Pattern_GUID: Guid = Guid('df1343bd-1888-4a29-a5-0c-b9-2e-6d-e3-7f-6f')
Text_Pattern_GUID: Guid = Guid('8615f05d-7de5-44fd-a6-79-2c-a4-b4-60-33-a8')
Toggle_Pattern_GUID: Guid = Guid('0b419760-e2f4-43ff-8c-5f-94-57-c8-2b-56-e9')
Transform_Pattern_GUID: Guid = Guid('24b46fdb-587e-49f1-9c-4a-d8-e9-8b-66-4b-7b')
ScrollItem_Pattern_GUID: Guid = Guid('4591d005-a803-4d5c-b4-d5-8d-28-00-f9-06-a7')
LegacyIAccessible_Pattern_GUID: Guid = Guid('54cc0a9f-3395-48af-ba-8d-73-f8-56-90-f3-e0')
ItemContainer_Pattern_GUID: Guid = Guid('3d13da0f-8b9a-4a99-85-fa-c5-c9-a6-9f-1e-d4')
VirtualizedItem_Pattern_GUID: Guid = Guid('f510173e-2e71-45e9-a6-e5-62-f6-ed-82-89-d5')
SynchronizedInput_Pattern_GUID: Guid = Guid('05c288a6-c47b-488b-b6-53-33-97-7a-55-1b-8b')
ObjectModel_Pattern_GUID: Guid = Guid('3e04acfe-08fc-47ec-96-bc-35-3f-a3-b3-4a-a7')
Annotation_Pattern_GUID: Guid = Guid('f6c72ad7-356c-4850-92-91-31-6f-60-8a-8c-84')
Text_Pattern2_GUID: Guid = Guid('498479a2-5b22-448d-b6-e4-64-74-90-86-06-98')
TextEdit_Pattern_GUID: Guid = Guid('69f3ff89-5af9-4c75-93-40-f2-de-29-2e-45-91')
CustomNavigation_Pattern_GUID: Guid = Guid('afea938a-621e-4054-bb-2c-2f-46-11-4d-ac-3f')
Styles_Pattern_GUID: Guid = Guid('1ae62655-da72-4d60-a1-53-e5-aa-69-88-e3-bf')
Spreadsheet_Pattern_GUID: Guid = Guid('6a5b24c9-9d1e-4b85-9e-44-c0-2e-31-69-b1-0b')
SpreadsheetItem_Pattern_GUID: Guid = Guid('32cf83ff-f1a8-4a8c-86-58-d4-7b-a7-4e-20-ba')
Tranform_Pattern2_GUID: Guid = Guid('8afcfd07-a369-44de-98-8b-2f-7f-f4-9f-b8-a8')
TextChild_Pattern_GUID: Guid = Guid('7533cab7-3bfe-41ef-9e-85-e2-63-8c-be-16-9e')
Drag_Pattern_GUID: Guid = Guid('c0bee21f-ccb3-4fed-99-5b-11-4f-6e-3d-27-28')
DropTarget_Pattern_GUID: Guid = Guid('0bcbec56-bd34-4b7b-9f-d5-26-59-90-5e-a3-dc')
StructuredMarkup_Pattern_GUID: Guid = Guid('abbd0878-8665-4f5c-94-fc-36-e7-d8-bb-70-6b')
Button_Control_GUID: Guid = Guid('5a78e369-c6a1-4f33-a9-d7-79-f2-0d-0c-78-8e')
Calendar_Control_GUID: Guid = Guid('8913eb88-00e5-46bc-8e-4e-14-a7-86-e1-65-a1')
CheckBox_Control_GUID: Guid = Guid('fb50f922-a3db-49c0-8b-c3-06-da-d5-57-78-e2')
ComboBox_Control_GUID: Guid = Guid('54cb426c-2f33-4fff-aa-a1-ae-f6-0d-ac-5d-eb')
Edit_Control_GUID: Guid = Guid('6504a5c8-2c86-4f87-ae-7b-1a-bd-dc-81-0c-f9')
Hyperlink_Control_GUID: Guid = Guid('8a56022c-b00d-4d15-8f-f0-5b-6b-26-6e-5e-02')
Image_Control_GUID: Guid = Guid('2d3736e4-6b16-4c57-a9-62-f9-32-60-a7-52-43')
ListItem_Control_GUID: Guid = Guid('7b3717f2-44d1-4a58-98-a8-f1-2a-9b-8f-78-e2')
List_Control_GUID: Guid = Guid('9b149ee1-7cca-4cfc-9a-f1-ca-c7-bd-dd-30-31')
Menu_Control_GUID: Guid = Guid('2e9b1440-0ea8-41fd-b3-74-c1-ea-6f-50-3c-d1')
MenuBar_Control_GUID: Guid = Guid('cc384250-0e7b-4ae8-95-ae-a0-8f-26-1b-52-ee')
MenuItem_Control_GUID: Guid = Guid('f45225d3-d0a0-49d8-98-34-9a-00-0d-2a-ed-dc')
ProgressBar_Control_GUID: Guid = Guid('228c9f86-c36c-47bb-9f-b6-a5-83-4b-fc-53-a4')
RadioButton_Control_GUID: Guid = Guid('3bdb49db-fe2c-4483-b3-e1-e5-7f-21-94-40-c6')
ScrollBar_Control_GUID: Guid = Guid('daf34b36-5065-4946-b2-2f-92-59-5f-c0-75-1a')
Slider_Control_GUID: Guid = Guid('b033c24b-3b35-4cea-b6-09-76-36-82-fa-66-0b')
Spinner_Control_GUID: Guid = Guid('60cc4b38-3cb1-4161-b4-42-c6-b7-26-c1-78-25')
StatusBar_Control_GUID: Guid = Guid('d45e7d1b-5873-475f-95-a4-04-33-e1-f1-b0-0a')
Tab_Control_GUID: Guid = Guid('38cd1f2d-337a-4bd2-a5-e3-ad-b4-69-e3-0b-d3')
TabItem_Control_GUID: Guid = Guid('2c6a634f-921b-4e6e-b2-6e-08-fc-b0-79-8f-4c')
Text_Control_GUID: Guid = Guid('ae9772dc-d331-4f09-be-20-7e-6d-fa-f0-7b-0a')
ToolBar_Control_GUID: Guid = Guid('8f06b751-e182-4e98-88-93-22-84-54-3a-7d-ce')
ToolTip_Control_GUID: Guid = Guid('05ddc6d1-2137-4768-98-ea-73-f5-2f-71-34-f3')
Tree_Control_GUID: Guid = Guid('7561349c-d241-43f4-99-08-b5-f0-91-be-e6-11')
TreeItem_Control_GUID: Guid = Guid('62c9feb9-8ffc-4878-a3-a4-96-b0-30-31-5c-18')
Custom_Control_GUID: Guid = Guid('f29ea0c3-adb7-430a-ba-90-e5-2c-73-13-e6-ed')
Group_Control_GUID: Guid = Guid('ad50aa1c-e8c8-4774-ae-1b-dd-86-df-0b-3b-dc')
Thumb_Control_GUID: Guid = Guid('701ca877-e310-4dd6-b6-44-79-7e-4f-ae-a2-13')
DataGrid_Control_GUID: Guid = Guid('84b783af-d103-4b0a-84-15-e7-39-42-41-0f-4b')
DataItem_Control_GUID: Guid = Guid('a0177842-d94f-42a5-81-4b-60-68-ad-dc-8d-a5')
Document_Control_GUID: Guid = Guid('3cd6bb6f-6f08-4562-b2-29-e4-e2-fc-7a-9e-b4')
SplitButton_Control_GUID: Guid = Guid('7011f01f-4ace-4901-b4-61-92-0a-6f-1c-a6-50')
Window_Control_GUID: Guid = Guid('e13a7242-f462-4f4d-ae-c1-53-b2-8d-6c-32-90')
Pane_Control_GUID: Guid = Guid('5c2b3f5b-9182-42a3-8d-ec-8c-04-c1-ee-63-4d')
Header_Control_GUID: Guid = Guid('5b90cbce-78fb-4614-82-b6-55-4d-74-71-8e-67')
HeaderItem_Control_GUID: Guid = Guid('e6bc12cb-7c8e-49cf-b1-68-4a-93-a3-2b-eb-b0')
Table_Control_GUID: Guid = Guid('773bfa0e-5bc4-4deb-92-1b-de-7b-32-06-22-9e')
TitleBar_Control_GUID: Guid = Guid('98aa55bf-3bb0-4b65-83-6e-2e-a3-0d-bc-17-1f')
Separator_Control_GUID: Guid = Guid('8767eba3-2a63-4ab0-ac-8d-aa-50-e2-3d-e9-78')
SemanticZoom_Control_GUID: Guid = Guid('5fd34a43-061e-42c8-b5-89-9d-cc-f7-4b-c4-3a')
AppBar_Control_GUID: Guid = Guid('6114908d-cc02-4d37-87-5b-b5-30-c7-13-95-54')
Text_AnimationStyle_Attribute_GUID: Guid = Guid('628209f0-7c9a-4d57-be-64-1f-18-36-57-1f-f5')
Text_BackgroundColor_Attribute_GUID: Guid = Guid('fdc49a07-583d-4f17-ad-27-77-fc-83-2a-3c-0b')
Text_BulletStyle_Attribute_GUID: Guid = Guid('c1097c90-d5c4-4237-97-81-3b-ec-8b-a5-4e-48')
Text_CapStyle_Attribute_GUID: Guid = Guid('fb059c50-92cc-49a5-ba-8f-0a-a8-72-bb-a2-f3')
Text_Culture_Attribute_GUID: Guid = Guid('c2025af9-a42d-4ced-a1-fb-c6-74-63-15-22-2e')
Text_FontName_Attribute_GUID: Guid = Guid('64e63ba8-f2e5-476e-a4-77-17-34-fe-aa-f7-26')
Text_FontSize_Attribute_GUID: Guid = Guid('dc5eeeff-0506-4673-93-f2-37-7e-4a-8e-01-f1')
Text_FontWeight_Attribute_GUID: Guid = Guid('6fc02359-b316-4f5f-b4-01-f1-ce-55-74-18-53')
Text_ForegroundColor_Attribute_GUID: Guid = Guid('72d1c95d-5e60-471a-96-b1-6c-1b-3b-77-a4-36')
Text_HorizontalTextAlignment_Attribute_GUID: Guid = Guid('04ea6161-fba3-477a-95-2a-bb-32-6d-02-6a-5b')
Text_IndentationFirstLine_Attribute_GUID: Guid = Guid('206f9ad5-c1d3-424a-81-82-6d-a9-a7-f3-d6-32')
Text_IndentationLeading_Attribute_GUID: Guid = Guid('5cf66bac-2d45-4a4b-b6-c9-f7-22-1d-28-15-b0')
Text_IndentationTrailing_Attribute_GUID: Guid = Guid('97ff6c0f-1ce4-408a-b6-7b-94-d8-3e-b6-9b-f2')
Text_IsHidden_Attribute_GUID: Guid = Guid('360182fb-bdd7-47f6-ab-69-19-e3-3f-8a-33-44')
Text_IsItalic_Attribute_GUID: Guid = Guid('fce12a56-1336-4a34-96-63-1b-ab-47-23-93-20')
Text_IsReadOnly_Attribute_GUID: Guid = Guid('a738156b-ca3e-495e-95-14-83-3c-44-0f-eb-11')
Text_IsSubscript_Attribute_GUID: Guid = Guid('f0ead858-8f53-413c-87-3f-1a-7d-7f-5e-0d-e4')
Text_IsSuperscript_Attribute_GUID: Guid = Guid('da706ee4-b3aa-4645-a4-1f-cd-25-15-7d-ea-76')
Text_MarginBottom_Attribute_GUID: Guid = Guid('7ee593c4-72b4-4cac-92-71-3e-d2-4b-0e-4d-42')
Text_MarginLeading_Attribute_GUID: Guid = Guid('9e9242d0-5ed0-4900-8e-8a-ee-cc-03-83-5a-fc')
Text_MarginTop_Attribute_GUID: Guid = Guid('683d936f-c9b9-4a9a-b3-d9-d2-0d-33-31-1e-2a')
Text_MarginTrailing_Attribute_GUID: Guid = Guid('af522f98-999d-40af-a5-b2-01-69-d0-34-20-02')
Text_OutlineStyles_Attribute_GUID: Guid = Guid('5b675b27-db89-46fe-97-0c-61-4d-52-3b-b9-7d')
Text_OverlineColor_Attribute_GUID: Guid = Guid('83ab383a-fd43-40da-ab-3e-ec-f8-16-5c-bb-6d')
Text_OverlineStyle_Attribute_GUID: Guid = Guid('0a234d66-617e-427f-87-1d-e1-ff-1e-0c-21-3f')
Text_StrikethroughColor_Attribute_GUID: Guid = Guid('bfe15a18-8c41-4c5a-9a-0b-04-af-0e-07-f4-87')
Text_StrikethroughStyle_Attribute_GUID: Guid = Guid('72913ef1-da00-4f01-89-9c-ac-5a-85-77-a3-07')
Text_Tabs_Attribute_GUID: Guid = Guid('2e68d00b-92fe-42d8-89-9a-a7-84-aa-44-54-a1')
Text_TextFlowDirections_Attribute_GUID: Guid = Guid('8bdf8739-f420-423e-af-77-20-a5-d9-73-a9-07')
Text_UnderlineColor_Attribute_GUID: Guid = Guid('bfa12c73-fde2-4473-bf-64-10-36-d6-aa-0f-45')
Text_UnderlineStyle_Attribute_GUID: Guid = Guid('5f3b21c0-ede4-44bd-9c-36-38-53-03-8c-bf-eb')
Text_AnnotationTypes_Attribute_GUID: Guid = Guid('ad2eb431-ee4e-4be1-a7-ba-55-59-15-5a-73-ef')
Text_AnnotationObjects_Attribute_GUID: Guid = Guid('ff41cf68-e7ab-40b9-8c-72-72-a8-ed-94-01-7d')
Text_StyleName_Attribute_GUID: Guid = Guid('22c9e091-4d66-45d8-a8-28-73-7b-ab-4c-98-a7')
Text_StyleId_Attribute_GUID: Guid = Guid('14c300de-c32b-449b-ab-7c-b0-e0-78-9a-ea-5d')
Text_Link_Attribute_GUID: Guid = Guid('b38ef51d-9e8d-4e46-91-44-56-eb-e1-77-32-9b')
Text_IsActive_Attribute_GUID: Guid = Guid('f5a4e533-e1b8-436b-93-5d-b5-7a-a3-f5-58-c4')
Text_SelectionActiveEnd_Attribute_GUID: Guid = Guid('1f668cc3-9bbf-416b-b0-a2-f8-9f-86-f6-61-2c')
Text_CaretPosition_Attribute_GUID: Guid = Guid('b227b131-9889-4752-a9-1b-73-3e-fd-c5-c5-a0')
Text_CaretBidiMode_Attribute_GUID: Guid = Guid('929ee7a6-51d3-4715-96-dc-b6-94-fa-24-a1-68')
Text_BeforeParagraphSpacing_Attribute_GUID: Guid = Guid('be7b0ab1-c822-4a24-85-e9-c8-f2-65-0f-c7-9c')
Text_AfterParagraphSpacing_Attribute_GUID: Guid = Guid('588cbb38-e62f-497c-b5-d1-cc-df-0e-e8-23-d8')
Text_LineSpacing_Attribute_GUID: Guid = Guid('63ff70ae-d943-4b47-8a-b7-a7-a0-33-d3-21-4b')
Text_BeforeSpacing_Attribute_GUID: Guid = Guid('be7b0ab1-c822-4a24-85-e9-c8-f2-65-0f-c7-9c')
Text_AfterSpacing_Attribute_GUID: Guid = Guid('588cbb38-e62f-497c-b5-d1-cc-df-0e-e8-23-d8')
Text_SayAsInterpretAs_Attribute_GUID: Guid = Guid('b38ad6ac-eee1-4b6e-88-cc-01-4c-ef-a9-3f-cb')
TextEdit_TextChanged_Event_GUID: Guid = Guid('120b0308-ec22-4eb8-9c-98-98-67-cd-a1-b1-65')
TextEdit_ConversionTargetChanged_Event_GUID: Guid = Guid('3388c183-ed4f-4c8b-9b-aa-36-4d-51-d8-84-7f')
Changes_Event_GUID: Guid = Guid('7df26714-614f-4e05-94-88-71-6c-5b-a1-94-36')
Annotation_Custom_GUID: Guid = Guid('9ec82750-3931-4952-85-bc-1d-bf-f7-8a-43-e3')
Annotation_SpellingError_GUID: Guid = Guid('ae85567e-9ece-423f-81-b7-96-c4-3d-53-e5-0e')
Annotation_GrammarError_GUID: Guid = Guid('757a048d-4518-41c6-85-4c-dc-00-9b-7c-fb-53')
Annotation_Comment_GUID: Guid = Guid('fd2fda30-26b3-4c06-8b-c7-98-f1-53-2e-46-fd')
Annotation_FormulaError_GUID: Guid = Guid('95611982-0cab-46d5-a2-f0-e3-0d-19-05-f8-bf')
Annotation_TrackChanges_GUID: Guid = Guid('21e6e888-dc14-4016-ac-27-19-05-53-c8-c4-70')
Annotation_Header_GUID: Guid = Guid('867b409b-b216-4472-a2-19-52-5e-31-06-81-f8')
Annotation_Footer_GUID: Guid = Guid('cceab046-1833-47aa-80-80-70-1e-d0-b0-c8-32')
Annotation_Highlighted_GUID: Guid = Guid('757c884e-8083-4081-8b-9c-e8-7f-50-72-f0-e4')
Annotation_Endnote_GUID: Guid = Guid('7565725c-2d99-4839-96-0d-33-d3-b8-66-ab-a5')
Annotation_Footnote_GUID: Guid = Guid('3de10e21-4125-42db-86-20-be-80-83-08-06-24')
Annotation_InsertionChange_GUID: Guid = Guid('0dbeb3a6-df15-4164-a3-c0-e2-1a-8c-e9-31-c4')
Annotation_DeletionChange_GUID: Guid = Guid('be3d5b05-951d-42e7-90-1d-ad-c8-c2-cf-34-d0')
Annotation_MoveChange_GUID: Guid = Guid('9da587eb-23e5-4490-b3-85-1a-22-dd-c8-b1-87')
Annotation_FormatChange_GUID: Guid = Guid('eb247345-d4f1-41ce-8e-52-f7-9b-69-63-5e-48')
Annotation_UnsyncedChange_GUID: Guid = Guid('1851116a-0e47-4b30-8c-b5-d7-da-e4-fb-cd-1b')
Annotation_EditingLockedChange_GUID: Guid = Guid('c31f3e1c-7423-4dac-83-48-41-f0-99-ff-6f-64')
Annotation_ExternalChange_GUID: Guid = Guid('75a05b31-5f11-42fd-88-7d-df-a0-10-db-23-92')
Annotation_ConflictingChange_GUID: Guid = Guid('98af8802-517c-459f-af-13-01-6d-3f-ab-87-7e')
Annotation_Author_GUID: Guid = Guid('f161d3a7-f81b-4128-b1-7f-71-f6-90-91-45-20')
Annotation_AdvancedProofingIssue_GUID: Guid = Guid('dac7b72c-c0f2-4b84-b9-0d-5f-af-c0-f0-ef-1c')
Annotation_DataValidationError_GUID: Guid = Guid('c8649fa8-9775-437e-ad-46-e7-09-d9-3c-23-43')
Annotation_CircularReferenceError_GUID: Guid = Guid('25bd9cf4-1745-4659-ba-67-72-7f-03-18-c6-16')
Annotation_Mathematics_GUID: Guid = Guid('eaab634b-26d0-40c1-80-73-57-ca-1c-63-3c-9b')
Annotation_Sensitive_GUID: Guid = Guid('37f4c04f-0f12-4464-92-9c-82-8f-d1-52-92-e3')
Changes_Summary_GUID: Guid = Guid('313d65a6-e60f-4d62-98-61-55-af-d7-28-d2-07')
StyleId_Custom_GUID: Guid = Guid('ef2edd3e-a999-4b7c-a3-78-09-bb-d5-2a-35-16')
StyleId_Heading1_GUID: Guid = Guid('7f7e8f69-6866-4621-93-0c-9a-5d-0c-a5-96-1c')
StyleId_Heading2_GUID: Guid = Guid('baa9b241-5c69-469d-85-ad-47-47-37-b5-2b-14')
StyleId_Heading3_GUID: Guid = Guid('bf8be9d2-d8b8-4ec5-8c-52-9c-fb-0d-03-59-70')
StyleId_Heading4_GUID: Guid = Guid('8436ffc0-9578-45fc-83-a4-ff-40-05-33-15-dd')
StyleId_Heading5_GUID: Guid = Guid('909f424d-0dbf-406e-97-bb-4e-77-3d-97-98-f7')
StyleId_Heading6_GUID: Guid = Guid('89d23459-5d5b-4824-a4-20-11-d3-ed-82-e4-0f')
StyleId_Heading7_GUID: Guid = Guid('a3790473-e9ae-422d-b8-e3-3b-67-5c-61-81-a4')
StyleId_Heading8_GUID: Guid = Guid('2bc14145-a40c-4881-84-ae-f2-23-56-85-38-0c')
StyleId_Heading9_GUID: Guid = Guid('c70d9133-bb2a-43d3-8a-c6-33-65-78-84-b0-f0')
StyleId_Title_GUID: Guid = Guid('15d8201a-ffcf-481f-b0-a1-30-b6-3b-e9-8f-07')
StyleId_Subtitle_GUID: Guid = Guid('b5d9fc17-5d6f-4420-b4-39-7c-b1-9a-d4-34-e2')
StyleId_Normal_GUID: Guid = Guid('cd14d429-e45e-4475-a1-c5-7f-9e-6b-e9-6e-ba')
StyleId_Emphasis_GUID: Guid = Guid('ca6e7dbe-355e-4820-95-a0-92-5f-04-1d-34-70')
StyleId_Quote_GUID: Guid = Guid('5d1c21ea-8195-4f6c-87-ea-5d-ab-ec-e6-4c-1d')
StyleId_BulletedList_GUID: Guid = Guid('5963ed64-6426-4632-8c-af-a3-2a-d4-02-d9-1a')
StyleId_NumberedList_GUID: Guid = Guid('1e96dbd5-64c3-43d0-b1-ee-b5-3b-06-e3-ed-df')
Notification_Event_GUID: Guid = Guid('72c5a2f7-9788-480f-b8-eb-4d-ee-00-f6-18-6f')
SID_IsUIAutomationObject: Guid = Guid('b96fdb85-7204-4724-84-2b-c7-05-9d-ed-b9-d0')
SID_ControlElementProvider: Guid = Guid('f4791d68-e254-4ba3-9a-53-26-a5-c5-49-79-46')
IsSelectionPattern2Available_Property_GUID: Guid = Guid('490806fb-6e89-4a47-83-19-d2-66-e5-11-f0-21')
Selection2_FirstSelectedItem_Property_GUID: Guid = Guid('cc24ea67-369c-4e55-9f-f7-38-da-69-54-0c-29')
Selection2_LastSelectedItem_Property_GUID: Guid = Guid('cf7bda90-2d83-49f8-86-0c-9c-e3-94-cf-89-b4')
Selection2_CurrentSelectedItem_Property_GUID: Guid = Guid('34257c26-83b5-41a6-93-9c-ae-84-1c-13-62-36')
Selection2_ItemCount_Property_GUID: Guid = Guid('bb49eb9f-456d-4048-b5-91-9c-20-26-b8-46-36')
Selection_Pattern2_GUID: Guid = Guid('fba25cab-ab98-49f7-a7-dc-fe-53-9d-c1-5b-e7')
HeadingLevel_Property_GUID: Guid = Guid('29084272-aaaf-4a30-87-96-3c-12-f6-2b-6b-bb')
IsDialog_Property_GUID: Guid = Guid('9d0dfb9b-8436-4501-bb-bb-e5-34-a4-fb-3b-3f')
UIA_IAFP_DEFAULT: UInt32 = 0
UIA_IAFP_UNWRAP_BRIDGE: UInt32 = 1
UIA_PFIA_DEFAULT: UInt32 = 0
UIA_PFIA_UNWRAP_BRIDGE: UInt32 = 1
UIA_ScrollPatternNoScroll: Double = -1
@winfunctype('OLEACC.dll')
def LresultFromObject(riid: POINTER(Guid), wParam: Windows.Win32.Foundation.WPARAM, punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype('OLEACC.dll')
def ObjectFromLresult(lResult: Windows.Win32.Foundation.LRESULT, riid: POINTER(Guid), wParam: Windows.Win32.Foundation.WPARAM, ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def WindowFromAccessibleObject(param0: Windows.Win32.UI.Accessibility.IAccessible_head, phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def AccessibleObjectFromWindow(hwnd: Windows.Win32.Foundation.HWND, dwId: UInt32, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def AccessibleObjectFromEvent(hwnd: Windows.Win32.Foundation.HWND, dwId: UInt32, dwChildId: UInt32, ppacc: POINTER(Windows.Win32.UI.Accessibility.IAccessible_head), pvarChild: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def AccessibleObjectFromPoint(ptScreen: Windows.Win32.Foundation.POINT, ppacc: POINTER(Windows.Win32.UI.Accessibility.IAccessible_head), pvarChild: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def AccessibleChildren(paccContainer: Windows.Win32.UI.Accessibility.IAccessible_head, iChildStart: Int32, cChildren: Int32, rgvarChildren: POINTER(Windows.Win32.System.Com.VARIANT_head), pcObtained: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def GetRoleTextA(lRole: UInt32, lpszRole: Windows.Win32.Foundation.PSTR, cchRoleMax: UInt32) -> UInt32: ...
@winfunctype('OLEACC.dll')
def GetRoleTextW(lRole: UInt32, lpszRole: Windows.Win32.Foundation.PWSTR, cchRoleMax: UInt32) -> UInt32: ...
@winfunctype('OLEACC.dll')
def GetStateTextA(lStateBit: UInt32, lpszState: Windows.Win32.Foundation.PSTR, cchState: UInt32) -> UInt32: ...
@winfunctype('OLEACC.dll')
def GetStateTextW(lStateBit: UInt32, lpszState: Windows.Win32.Foundation.PWSTR, cchState: UInt32) -> UInt32: ...
@winfunctype('OLEACC.dll')
def GetOleaccVersionInfo(pVer: POINTER(UInt32), pBuild: POINTER(UInt32)) -> Void: ...
@winfunctype('OLEACC.dll')
def CreateStdAccessibleObject(hwnd: Windows.Win32.Foundation.HWND, idObject: Int32, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def CreateStdAccessibleProxyA(hwnd: Windows.Win32.Foundation.HWND, pClassName: Windows.Win32.Foundation.PSTR, idObject: Int32, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def CreateStdAccessibleProxyW(hwnd: Windows.Win32.Foundation.HWND, pClassName: Windows.Win32.Foundation.PWSTR, idObject: Int32, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def AccSetRunningUtilityState(hwndApp: Windows.Win32.Foundation.HWND, dwUtilityStateMask: UInt32, dwUtilityState: Windows.Win32.UI.Accessibility.ACC_UTILITY_STATE_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def AccNotifyTouchInteraction(hwndApp: Windows.Win32.Foundation.HWND, hwndTarget: Windows.Win32.Foundation.HWND, ptTarget: Windows.Win32.Foundation.POINT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetErrorDescription(pDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('UIAutomationCore.dll')
def UiaHUiaNodeFromVariant(pvar: POINTER(Windows.Win32.System.Com.VARIANT_head), phnode: POINTER(Windows.Win32.UI.Accessibility.HUIANODE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaHPatternObjectFromVariant(pvar: POINTER(Windows.Win32.System.Com.VARIANT_head), phobj: POINTER(Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaHTextRangeFromVariant(pvar: POINTER(Windows.Win32.System.Com.VARIANT_head), phtextrange: POINTER(Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaNodeRelease(hnode: Windows.Win32.UI.Accessibility.HUIANODE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetPropertyValue(hnode: Windows.Win32.UI.Accessibility.HUIANODE, propertyId: Int32, pValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetPatternProvider(hnode: Windows.Win32.UI.Accessibility.HUIANODE, patternId: Int32, phobj: POINTER(Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetRuntimeId(hnode: Windows.Win32.UI.Accessibility.HUIANODE, pruntimeId: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaSetFocus(hnode: Windows.Win32.UI.Accessibility.HUIANODE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaNavigate(hnode: Windows.Win32.UI.Accessibility.HUIANODE, direction: Windows.Win32.UI.Accessibility.NavigateDirection, pCondition: POINTER(Windows.Win32.UI.Accessibility.UiaCondition_head), pRequest: POINTER(Windows.Win32.UI.Accessibility.UiaCacheRequest_head), ppRequestedData: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppTreeStructure: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetUpdatedCache(hnode: Windows.Win32.UI.Accessibility.HUIANODE, pRequest: POINTER(Windows.Win32.UI.Accessibility.UiaCacheRequest_head), normalizeState: Windows.Win32.UI.Accessibility.NormalizeState, pNormalizeCondition: POINTER(Windows.Win32.UI.Accessibility.UiaCondition_head), ppRequestedData: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppTreeStructure: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaFind(hnode: Windows.Win32.UI.Accessibility.HUIANODE, pParams: POINTER(Windows.Win32.UI.Accessibility.UiaFindParams_head), pRequest: POINTER(Windows.Win32.UI.Accessibility.UiaCacheRequest_head), ppRequestedData: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppOffsets: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppTreeStructures: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaNodeFromPoint(x: Double, y: Double, pRequest: POINTER(Windows.Win32.UI.Accessibility.UiaCacheRequest_head), ppRequestedData: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppTreeStructure: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaNodeFromFocus(pRequest: POINTER(Windows.Win32.UI.Accessibility.UiaCacheRequest_head), ppRequestedData: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), ppTreeStructure: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaNodeFromHandle(hwnd: Windows.Win32.Foundation.HWND, phnode: POINTER(Windows.Win32.UI.Accessibility.HUIANODE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaNodeFromProvider(pProvider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, phnode: POINTER(Windows.Win32.UI.Accessibility.HUIANODE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetRootNode(phnode: POINTER(Windows.Win32.UI.Accessibility.HUIANODE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRegisterProviderCallback(pCallback: POINTER(Windows.Win32.UI.Accessibility.UiaProviderCallback)) -> Void: ...
@winfunctype('UIAutomationCore.dll')
def UiaLookupId(type: Windows.Win32.UI.Accessibility.AutomationIdentifierType, pGuid: POINTER(Guid)) -> Int32: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetReservedNotSupportedValue(punkNotSupportedValue: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetReservedMixedAttributeValue(punkMixedAttributeValue: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaClientsAreListening() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseAutomationPropertyChangedEvent(pProvider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, id: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, oldValue: Windows.Win32.System.Com.VARIANT, newValue: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseAutomationEvent(pProvider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, id: Windows.Win32.UI.Accessibility.UIA_EVENT_ID) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseStructureChangedEvent(pProvider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, structureChangeType: Windows.Win32.UI.Accessibility.StructureChangeType, pRuntimeId: POINTER(Int32), cRuntimeIdLen: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseAsyncContentLoadedEvent(pProvider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, asyncContentLoadedState: Windows.Win32.UI.Accessibility.AsyncContentLoadedState, percentComplete: Double) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseTextEditTextChangedEvent(pProvider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, textEditChangeType: Windows.Win32.UI.Accessibility.TextEditChangeType, pChangedData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseChangesEvent(pProvider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, eventIdCount: Int32, pUiaChanges: POINTER(Windows.Win32.UI.Accessibility.UiaChangeInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseNotificationEvent(provider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, notificationKind: Windows.Win32.UI.Accessibility.NotificationKind, notificationProcessing: Windows.Win32.UI.Accessibility.NotificationProcessing, displayString: Windows.Win32.Foundation.BSTR, activityId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseActiveTextPositionChangedEvent(provider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, textRange: Windows.Win32.UI.Accessibility.ITextRangeProvider_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaAddEvent(hnode: Windows.Win32.UI.Accessibility.HUIANODE, eventId: Int32, pCallback: POINTER(Windows.Win32.UI.Accessibility.UiaEventCallback), scope: Windows.Win32.UI.Accessibility.TreeScope, pProperties: POINTER(Int32), cProperties: Int32, pRequest: POINTER(Windows.Win32.UI.Accessibility.UiaCacheRequest_head), phEvent: POINTER(Windows.Win32.UI.Accessibility.HUIAEVENT)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRemoveEvent(hEvent: Windows.Win32.UI.Accessibility.HUIAEVENT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaEventAddWindow(hEvent: Windows.Win32.UI.Accessibility.HUIAEVENT, hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaEventRemoveWindow(hEvent: Windows.Win32.UI.Accessibility.HUIAEVENT, hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def DockPattern_SetDockPosition(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, dockPosition: Windows.Win32.UI.Accessibility.DockPosition) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ExpandCollapsePattern_Collapse(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ExpandCollapsePattern_Expand(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def GridPattern_GetItem(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, row: Int32, column: Int32, pResult: POINTER(Windows.Win32.UI.Accessibility.HUIANODE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def InvokePattern_Invoke(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def MultipleViewPattern_GetViewName(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, viewId: Int32, ppStr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def MultipleViewPattern_SetCurrentView(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, viewId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def RangeValuePattern_SetValue(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, val: Double) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ScrollItemPattern_ScrollIntoView(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ScrollPattern_Scroll(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, horizontalAmount: Windows.Win32.UI.Accessibility.ScrollAmount, verticalAmount: Windows.Win32.UI.Accessibility.ScrollAmount) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ScrollPattern_SetScrollPercent(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, horizontalPercent: Double, verticalPercent: Double) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def SelectionItemPattern_AddToSelection(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def SelectionItemPattern_RemoveFromSelection(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def SelectionItemPattern_Select(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TogglePattern_Toggle(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TransformPattern_Move(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, x: Double, y: Double) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TransformPattern_Resize(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, width: Double, height: Double) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TransformPattern_Rotate(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, degrees: Double) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ValuePattern_SetValue(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, pVal: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def WindowPattern_Close(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def WindowPattern_SetWindowVisualState(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, state: Windows.Win32.UI.Accessibility.WindowVisualState) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def WindowPattern_WaitForInputIdle(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, milliseconds: Int32, pResult: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextPattern_GetSelection(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextPattern_GetVisibleRanges(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextPattern_RangeFromChild(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, hnodeChild: Windows.Win32.UI.Accessibility.HUIANODE, pRetVal: POINTER(Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextPattern_RangeFromPoint(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, point: Windows.Win32.UI.Accessibility.UiaPoint, pRetVal: POINTER(Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextPattern_get_DocumentRange(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, pRetVal: POINTER(Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextPattern_get_SupportedTextSelection(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, pRetVal: POINTER(Windows.Win32.UI.Accessibility.SupportedTextSelection)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_Clone(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, pRetVal: POINTER(Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_Compare(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, range: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_CompareEndpoints(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, endpoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, targetRange: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, targetEndpoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_ExpandToEnclosingUnit(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, unit: Windows.Win32.UI.Accessibility.TextUnit) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_GetAttributeValue(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, attributeId: Int32, pRetVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_FindAttribute(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, attributeId: Int32, val: Windows.Win32.System.Com.VARIANT, backward: Windows.Win32.Foundation.BOOL, pRetVal: POINTER(Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_FindText(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, text: Windows.Win32.Foundation.BSTR, backward: Windows.Win32.Foundation.BOOL, ignoreCase: Windows.Win32.Foundation.BOOL, pRetVal: POINTER(Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_GetBoundingRectangles(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_GetEnclosingElement(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, pRetVal: POINTER(Windows.Win32.UI.Accessibility.HUIANODE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_GetText(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, maxLength: Int32, pRetVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_Move(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, unit: Windows.Win32.UI.Accessibility.TextUnit, count: Int32, pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_MoveEndpointByUnit(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, endpoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, unit: Windows.Win32.UI.Accessibility.TextUnit, count: Int32, pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_MoveEndpointByRange(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, endpoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, targetRange: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, targetEndpoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_Select(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_AddToSelection(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_RemoveFromSelection(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_ScrollIntoView(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, alignToTop: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_GetChildren(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE, pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ItemContainerPattern_FindItemByProperty(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, hnodeStartAfter: Windows.Win32.UI.Accessibility.HUIANODE, propertyId: Int32, value: Windows.Win32.System.Com.VARIANT, pFound: POINTER(Windows.Win32.UI.Accessibility.HUIANODE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def LegacyIAccessiblePattern_Select(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, flagsSelect: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def LegacyIAccessiblePattern_DoDefaultAction(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def LegacyIAccessiblePattern_SetValue(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, szValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def LegacyIAccessiblePattern_GetIAccessible(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, pAccessible: POINTER(Windows.Win32.UI.Accessibility.IAccessible_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def SynchronizedInputPattern_StartListening(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, inputType: Windows.Win32.UI.Accessibility.SynchronizedInputType) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def SynchronizedInputPattern_Cancel(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def VirtualizedItemPattern_Realize(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaPatternRelease(hobj: Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('UIAutomationCore.dll')
def UiaTextRangeRelease(hobj: Windows.Win32.UI.Accessibility.HUIATEXTRANGE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('UIAutomationCore.dll')
def UiaReturnRawElementProvider(hwnd: Windows.Win32.Foundation.HWND, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, el: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaHostProviderFromHwnd(hwnd: Windows.Win32.Foundation.HWND, ppProvider: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaProviderForNonClient(hwnd: Windows.Win32.Foundation.HWND, idObject: Int32, idChild: Int32, ppProvider: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaIAccessibleFromProvider(pProvider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, dwFlags: UInt32, ppAccessible: POINTER(Windows.Win32.UI.Accessibility.IAccessible_head), pvarChild: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaProviderFromIAccessible(pAccessible: Windows.Win32.UI.Accessibility.IAccessible_head, idChild: Int32, dwFlags: UInt32, ppProvider: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaDisconnectAllProviders() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaDisconnectProvider(pProvider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaHasServerSideProvider(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def RegisterPointerInputTarget(hwnd: Windows.Win32.Foundation.HWND, pointerType: Windows.Win32.UI.WindowsAndMessaging.POINTER_INPUT_TYPE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def UnregisterPointerInputTarget(hwnd: Windows.Win32.Foundation.HWND, pointerType: Windows.Win32.UI.WindowsAndMessaging.POINTER_INPUT_TYPE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def RegisterPointerInputTargetEx(hwnd: Windows.Win32.Foundation.HWND, pointerType: Windows.Win32.UI.WindowsAndMessaging.POINTER_INPUT_TYPE, fObserve: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def UnregisterPointerInputTargetEx(hwnd: Windows.Win32.Foundation.HWND, pointerType: Windows.Win32.UI.WindowsAndMessaging.POINTER_INPUT_TYPE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def NotifyWinEvent(event: UInt32, hwnd: Windows.Win32.Foundation.HWND, idObject: Int32, idChild: Int32) -> Void: ...
@winfunctype('USER32.dll')
def SetWinEventHook(eventMin: UInt32, eventMax: UInt32, hmodWinEventProc: Windows.Win32.Foundation.HINSTANCE, pfnWinEventProc: Windows.Win32.UI.Accessibility.WINEVENTPROC, idProcess: UInt32, idThread: UInt32, dwFlags: UInt32) -> Windows.Win32.UI.Accessibility.HWINEVENTHOOK: ...
@winfunctype('USER32.dll')
def IsWinEventHookInstalled(event: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def UnhookWinEvent(hWinEventHook: Windows.Win32.UI.Accessibility.HWINEVENTHOOK) -> Windows.Win32.Foundation.BOOL: ...
AsyncContentLoadedState = Int32
AsyncContentLoadedState_Beginning: AsyncContentLoadedState = 0
AsyncContentLoadedState_Progress: AsyncContentLoadedState = 1
AsyncContentLoadedState_Completed: AsyncContentLoadedState = 2
AutomationElementMode = Int32
AutomationElementMode_None: AutomationElementMode = 0
AutomationElementMode_Full: AutomationElementMode = 1
AutomationIdentifierType = Int32
AutomationIdentifierType_Property: AutomationIdentifierType = 0
AutomationIdentifierType_Pattern: AutomationIdentifierType = 1
AutomationIdentifierType_Event: AutomationIdentifierType = 2
AutomationIdentifierType_ControlType: AutomationIdentifierType = 3
AutomationIdentifierType_TextAttribute: AutomationIdentifierType = 4
AutomationIdentifierType_LandmarkType: AutomationIdentifierType = 5
AutomationIdentifierType_Annotation: AutomationIdentifierType = 6
AutomationIdentifierType_Changes: AutomationIdentifierType = 7
AutomationIdentifierType_Style: AutomationIdentifierType = 8
BulletStyle = Int32
BulletStyle_None: BulletStyle = 0
BulletStyle_HollowRoundBullet: BulletStyle = 1
BulletStyle_FilledRoundBullet: BulletStyle = 2
BulletStyle_HollowSquareBullet: BulletStyle = 3
BulletStyle_FilledSquareBullet: BulletStyle = 4
BulletStyle_DashBullet: BulletStyle = 5
BulletStyle_Other: BulletStyle = -1
CAccPropServices = Guid('b5f8350b-0548-48b1-a6-ee-88-bd-00-b4-a5-e7')
CUIAutomation = Guid('ff48dba4-60ef-4201-aa-87-54-10-3e-ef-59-4e')
CUIAutomation8 = Guid('e22ad333-b25f-460c-83-d0-05-81-10-73-95-c9')
CUIAutomationRegistrar = Guid('6e29fabf-9977-42d1-8d-0e-ca-7e-61-ad-87-e6')
CapStyle = Int32
CapStyle_None: CapStyle = 0
CapStyle_SmallCap: CapStyle = 1
CapStyle_AllCap: CapStyle = 2
CapStyle_AllPetiteCaps: CapStyle = 3
CapStyle_PetiteCaps: CapStyle = 4
CapStyle_Unicase: CapStyle = 5
CapStyle_Titling: CapStyle = 6
CapStyle_Other: CapStyle = -1
CaretBidiMode = Int32
CaretBidiMode_LTR: CaretBidiMode = 0
CaretBidiMode_RTL: CaretBidiMode = 1
CaretPosition = Int32
CaretPosition_Unknown: CaretPosition = 0
CaretPosition_EndOfLine: CaretPosition = 1
CaretPosition_BeginningOfLine: CaretPosition = 2
CoalesceEventsOptions = Int32
CoalesceEventsOptions_Disabled: CoalesceEventsOptions = 0
CoalesceEventsOptions_Enabled: CoalesceEventsOptions = 1
ConditionType = Int32
ConditionType_True: ConditionType = 0
ConditionType_False: ConditionType = 1
ConditionType_Property: ConditionType = 2
ConditionType_And: ConditionType = 3
ConditionType_Or: ConditionType = 4
ConditionType_Not: ConditionType = 5
ConnectionRecoveryBehaviorOptions = Int32
ConnectionRecoveryBehaviorOptions_Disabled: ConnectionRecoveryBehaviorOptions = 0
ConnectionRecoveryBehaviorOptions_Enabled: ConnectionRecoveryBehaviorOptions = 1
DockPosition = Int32
DockPosition_Top: DockPosition = 0
DockPosition_Left: DockPosition = 1
DockPosition_Bottom: DockPosition = 2
DockPosition_Right: DockPosition = 3
DockPosition_Fill: DockPosition = 4
DockPosition_None: DockPosition = 5
EventArgsType = Int32
EventArgsType_Simple: EventArgsType = 0
EventArgsType_PropertyChanged: EventArgsType = 1
EventArgsType_StructureChanged: EventArgsType = 2
EventArgsType_AsyncContentLoaded: EventArgsType = 3
EventArgsType_WindowClosed: EventArgsType = 4
EventArgsType_TextEditTextChanged: EventArgsType = 5
EventArgsType_Changes: EventArgsType = 6
EventArgsType_Notification: EventArgsType = 7
EventArgsType_ActiveTextPositionChanged: EventArgsType = 8
EventArgsType_StructuredMarkup: EventArgsType = 9
ExpandCollapseState = Int32
ExpandCollapseState_Collapsed: ExpandCollapseState = 0
ExpandCollapseState_Expanded: ExpandCollapseState = 1
ExpandCollapseState_PartiallyExpanded: ExpandCollapseState = 2
ExpandCollapseState_LeafNode: ExpandCollapseState = 3
class ExtendedProperty(Structure):
    PropertyName: Windows.Win32.Foundation.BSTR
    PropertyValue: Windows.Win32.Foundation.BSTR
class FILTERKEYS(Structure):
    cbSize: UInt32
    dwFlags: UInt32
    iWaitMSec: UInt32
    iDelayMSec: UInt32
    iRepeatMSec: UInt32
    iBounceMSec: UInt32
FillType = Int32
FillType_None: FillType = 0
FillType_Color: FillType = 1
FillType_Gradient: FillType = 2
FillType_Picture: FillType = 3
FillType_Pattern: FillType = 4
FlowDirections = Int32
FlowDirections_Default: FlowDirections = 0
FlowDirections_RightToLeft: FlowDirections = 1
FlowDirections_BottomToTop: FlowDirections = 2
FlowDirections_Vertical: FlowDirections = 4
class HIGHCONTRASTA(Structure):
    cbSize: UInt32
    dwFlags: Windows.Win32.UI.Accessibility.HIGHCONTRASTW_FLAGS
    lpszDefaultScheme: Windows.Win32.Foundation.PSTR
class HIGHCONTRASTW(Structure):
    cbSize: UInt32
    dwFlags: Windows.Win32.UI.Accessibility.HIGHCONTRASTW_FLAGS
    lpszDefaultScheme: Windows.Win32.Foundation.PWSTR
HIGHCONTRASTW_FLAGS = UInt32
HCF_HIGHCONTRASTON: HIGHCONTRASTW_FLAGS = 1
HCF_AVAILABLE: HIGHCONTRASTW_FLAGS = 2
HCF_HOTKEYACTIVE: HIGHCONTRASTW_FLAGS = 4
HCF_CONFIRMHOTKEY: HIGHCONTRASTW_FLAGS = 8
HCF_HOTKEYSOUND: HIGHCONTRASTW_FLAGS = 16
HCF_INDICATOR: HIGHCONTRASTW_FLAGS = 32
HCF_HOTKEYAVAILABLE: HIGHCONTRASTW_FLAGS = 64
HCF_OPTION_NOTHEMECHANGE: HIGHCONTRASTW_FLAGS = 4096
HUIAEVENT = IntPtr
HUIANODE = IntPtr
HUIAPATTERNOBJECT = IntPtr
HUIATEXTRANGE = IntPtr
HWINEVENTHOOK = IntPtr
HorizontalTextAlignment = Int32
HorizontalTextAlignment_Left: HorizontalTextAlignment = 0
HorizontalTextAlignment_Centered: HorizontalTextAlignment = 1
HorizontalTextAlignment_Right: HorizontalTextAlignment = 2
HorizontalTextAlignment_Justified: HorizontalTextAlignment = 3
class IAccIdentity(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7852b78d-1cfd-41c1-a6-15-9c-0c-85-96-0b-5f')
    @commethod(3)
    def GetIdentityString(dwIDChild: UInt32, ppIDString: POINTER(c_char_p_no), pdwIDStringLen: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAccPropServer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('76c0dbbb-15e0-4e7b-b6-1b-20-ee-ea-20-01-e0')
    @commethod(3)
    def GetPropValue(pIDString: c_char_p_no, dwIDStringLen: UInt32, idProp: Guid, pvarValue: POINTER(Windows.Win32.System.Com.VARIANT_head), pfHasProp: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAccPropServices(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6e26e776-04f0-495d-80-e4-33-30-35-2e-31-69')
    @commethod(3)
    def SetPropValue(pIDString: c_char_p_no, dwIDStringLen: UInt32, idProp: Guid, var: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPropServer(pIDString: c_char_p_no, dwIDStringLen: UInt32, paProps: POINTER(Guid), cProps: Int32, pServer: Windows.Win32.UI.Accessibility.IAccPropServer_head, annoScope: Windows.Win32.UI.Accessibility.AnnoScope) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ClearProps(pIDString: c_char_p_no, dwIDStringLen: UInt32, paProps: POINTER(Guid), cProps: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetHwndProp(hwnd: Windows.Win32.Foundation.HWND, idObject: UInt32, idChild: UInt32, idProp: Guid, var: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetHwndPropStr(hwnd: Windows.Win32.Foundation.HWND, idObject: UInt32, idChild: UInt32, idProp: Guid, str: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetHwndPropServer(hwnd: Windows.Win32.Foundation.HWND, idObject: UInt32, idChild: UInt32, paProps: POINTER(Guid), cProps: Int32, pServer: Windows.Win32.UI.Accessibility.IAccPropServer_head, annoScope: Windows.Win32.UI.Accessibility.AnnoScope) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ClearHwndProps(hwnd: Windows.Win32.Foundation.HWND, idObject: UInt32, idChild: UInt32, paProps: POINTER(Guid), cProps: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ComposeHwndIdentityString(hwnd: Windows.Win32.Foundation.HWND, idObject: UInt32, idChild: UInt32, ppIDString: POINTER(c_char_p_no), pdwIDStringLen: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DecomposeHwndIdentityString(pIDString: c_char_p_no, dwIDStringLen: UInt32, phwnd: POINTER(Windows.Win32.Foundation.HWND), pidObject: POINTER(UInt32), pidChild: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetHmenuProp(hmenu: Windows.Win32.UI.WindowsAndMessaging.HMENU, idChild: UInt32, idProp: Guid, var: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetHmenuPropStr(hmenu: Windows.Win32.UI.WindowsAndMessaging.HMENU, idChild: UInt32, idProp: Guid, str: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetHmenuPropServer(hmenu: Windows.Win32.UI.WindowsAndMessaging.HMENU, idChild: UInt32, paProps: POINTER(Guid), cProps: Int32, pServer: Windows.Win32.UI.Accessibility.IAccPropServer_head, annoScope: Windows.Win32.UI.Accessibility.AnnoScope) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ClearHmenuProps(hmenu: Windows.Win32.UI.WindowsAndMessaging.HMENU, idChild: UInt32, paProps: POINTER(Guid), cProps: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ComposeHmenuIdentityString(hmenu: Windows.Win32.UI.WindowsAndMessaging.HMENU, idChild: UInt32, ppIDString: POINTER(c_char_p_no), pdwIDStringLen: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def DecomposeHmenuIdentityString(pIDString: c_char_p_no, dwIDStringLen: UInt32, phmenu: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU), pidChild: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAccessible(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('618736e0-3c3d-11cf-81-0c-00-aa-00-38-9b-71')
    @commethod(7)
    def get_accParent(ppdispParent: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_accChildCount(pcountChildren: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_accChild(varChild: Windows.Win32.System.Com.VARIANT, ppdispChild: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_accName(varChild: Windows.Win32.System.Com.VARIANT, pszName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_accValue(varChild: Windows.Win32.System.Com.VARIANT, pszValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_accDescription(varChild: Windows.Win32.System.Com.VARIANT, pszDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_accRole(varChild: Windows.Win32.System.Com.VARIANT, pvarRole: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_accState(varChild: Windows.Win32.System.Com.VARIANT, pvarState: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_accHelp(varChild: Windows.Win32.System.Com.VARIANT, pszHelp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_accHelpTopic(pszHelpFile: POINTER(Windows.Win32.Foundation.BSTR), varChild: Windows.Win32.System.Com.VARIANT, pidTopic: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_accKeyboardShortcut(varChild: Windows.Win32.System.Com.VARIANT, pszKeyboardShortcut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_accFocus(pvarChild: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_accSelection(pvarChildren: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_accDefaultAction(varChild: Windows.Win32.System.Com.VARIANT, pszDefaultAction: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def accSelect(flagsSelect: Int32, varChild: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def accLocation(pxLeft: POINTER(Int32), pyTop: POINTER(Int32), pcxWidth: POINTER(Int32), pcyHeight: POINTER(Int32), varChild: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def accNavigate(navDir: Int32, varStart: Windows.Win32.System.Com.VARIANT, pvarEndUpAt: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def accHitTest(xLeft: Int32, yTop: Int32, pvarChild: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def accDoDefaultAction(varChild: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_accName(varChild: Windows.Win32.System.Com.VARIANT, szName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_accValue(varChild: Windows.Win32.System.Com.VARIANT, szValue: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IAccessibleEx(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f8b80ada-2c44-48d0-89-be-5f-f2-3c-9c-d8-75')
    @commethod(3)
    def GetObjectForChild(idChild: Int32, pRetVal: POINTER(Windows.Win32.UI.Accessibility.IAccessibleEx_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIAccessiblePair(ppAcc: POINTER(Windows.Win32.UI.Accessibility.IAccessible_head), pidChild: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRuntimeId(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ConvertReturnedElement(pIn: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, ppRetValOut: POINTER(Windows.Win32.UI.Accessibility.IAccessibleEx_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAccessibleHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('03022430-abc4-11d0-bd-e2-00-aa-00-1a-19-53')
    @commethod(3)
    def AccessibleObjectFromID(hwnd: Int32, lObjectID: Int32, pIAccessible: POINTER(Windows.Win32.UI.Accessibility.IAccessible_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAccessibleHostingElementProviders(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('33ac331b-943e-4020-b2-95-db-37-78-49-74-a3')
    @commethod(3)
    def GetEmbeddedFragmentRoots(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetObjectIdForProvider(pProvider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, pidObject: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAccessibleWindowlessSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bf3abd9c-76da-4389-9e-b6-14-27-d2-5a-ba-b7')
    @commethod(3)
    def AcquireObjectIdRange(rangeSize: Int32, pRangeOwner: Windows.Win32.UI.Accessibility.IAccessibleHandler_head, pRangeBase: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseObjectIdRange(rangeBase: Int32, pRangeOwner: Windows.Win32.UI.Accessibility.IAccessibleHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryObjectIdRanges(pRangesOwner: Windows.Win32.UI.Accessibility.IAccessibleHandler_head, psaRanges: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetParentAccessible(ppParent: POINTER(Windows.Win32.UI.Accessibility.IAccessible_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAnnotationProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f95c7e80-bd63-4601-97-82-44-5e-bf-f0-11-fc')
    @commethod(3)
    def get_AnnotationTypeId(retVal: POINTER(Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_AnnotationTypeName(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Author(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_DateTime(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Target(retVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICustomNavigationProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2062a28a-8c07-4b94-8e-12-70-37-c6-22-ae-b8')
    @commethod(3)
    def Navigate(direction: Windows.Win32.UI.Accessibility.NavigateDirection, pRetVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDockProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('159bc72c-4ad3-485e-96-37-d7-05-2e-df-01-46')
    @commethod(3)
    def SetDockPosition(dockPosition: Windows.Win32.UI.Accessibility.DockPosition) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_DockPosition(pRetVal: POINTER(Windows.Win32.UI.Accessibility.DockPosition)) -> Windows.Win32.Foundation.HRESULT: ...
class IDragProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6aa7bbbb-7ff9-497d-90-4f-d2-0b-89-79-29-d8')
    @commethod(3)
    def get_IsGrabbed(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_DropEffect(pRetVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_DropEffects(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGrabbedItems(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IDropTargetProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bae82bfd-358a-481c-85-a0-d8-b4-d9-0a-5d-61')
    @commethod(3)
    def get_DropTargetEffect(pRetVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_DropTargetEffects(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IExpandCollapseProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d847d3a5-cab0-4a98-8c-32-ec-b4-5c-59-ad-24')
    @commethod(3)
    def Expand() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Collapse() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_ExpandCollapseState(pRetVal: POINTER(Windows.Win32.UI.Accessibility.ExpandCollapseState)) -> Windows.Win32.Foundation.HRESULT: ...
class IGridItemProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d02541f1-fb81-4d64-ae-32-f5-20-f8-a6-db-d1')
    @commethod(3)
    def get_Row(pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Column(pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_RowSpan(pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_ColumnSpan(pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_ContainingGrid(pRetVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGridProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b17d6187-0907-464b-a1-68-0e-f1-7a-15-72-b1')
    @commethod(3)
    def GetItem(row: Int32, column: Int32, pRetVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_RowCount(pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_ColumnCount(pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IInvokeProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('54fcb24b-e18e-47a2-b4-d3-ec-cb-e7-75-99-a2')
    @commethod(3)
    def Invoke() -> Windows.Win32.Foundation.HRESULT: ...
class IItemContainerProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e747770b-39ce-4382-ab-30-d8-fb-3f-33-6f-24')
    @commethod(3)
    def FindItemByProperty(pStartAfter: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, propertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, value: Windows.Win32.System.Com.VARIANT, pFound: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ILegacyIAccessibleProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e44c3566-915d-4070-99-c6-04-7b-ff-5a-08-f5')
    @commethod(3)
    def Select(flagsSelect: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DoDefaultAction() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(szValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIAccessible(ppAccessible: POINTER(Windows.Win32.UI.Accessibility.IAccessible_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_ChildId(pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Name(pszName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Value(pszValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Description(pszDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Role(pdwRole: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_State(pdwState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Help(pszHelp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_KeyboardShortcut(pszKeyboardShortcut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetSelection(pvarSelectedChildren: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_DefaultAction(pszDefaultAction: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IMultipleViewProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6278cab1-b556-4a1a-b4-e0-41-8a-cc-52-32-01')
    @commethod(3)
    def GetViewName(viewId: Int32, pRetVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCurrentView(viewId: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentView(pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSupportedViews(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectModelProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3ad86ebd-f5ef-483d-bb-18-b1-04-2a-47-5d-64')
    @commethod(3)
    def GetUnderlyingObjectModel(ppUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IProxyProviderWinEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('89592ad4-f4e0-43d5-a3-b6-ba-d7-e1-11-b4-35')
    @commethod(3)
    def RespondToWinEvent(idWinEvent: UInt32, hwnd: Windows.Win32.Foundation.HWND, idObject: Int32, idChild: Int32, pSink: Windows.Win32.UI.Accessibility.IProxyProviderWinEventSink_head) -> Windows.Win32.Foundation.HRESULT: ...
class IProxyProviderWinEventSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4fd82b78-a43e-46ac-98-03-0a-69-69-c7-c1-83')
    @commethod(3)
    def AddAutomationPropertyChangedEvent(pProvider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, id: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, newValue: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddAutomationEvent(pProvider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, id: Windows.Win32.UI.Accessibility.UIA_EVENT_ID) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddStructureChangedEvent(pProvider: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, structureChangeType: Windows.Win32.UI.Accessibility.StructureChangeType, runtimeId: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRangeValueProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('36dc7aef-33e6-4691-af-e1-2b-e7-27-4b-3d-33')
    @commethod(3)
    def SetValue(val: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Value(pRetVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_IsReadOnly(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Maximum(pRetVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Minimum(pRetVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LargeChange(pRetVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SmallChange(pRetVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderAdviseEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a407b27b-0f6d-4427-92-92-47-3c-7b-f9-32-58')
    @commethod(3)
    def AdviseEventAdded(eventId: Windows.Win32.UI.Accessibility.UIA_EVENT_ID, propertyIDs: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AdviseEventRemoved(eventId: Windows.Win32.UI.Accessibility.UIA_EVENT_ID, propertyIDs: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderFragment(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f7063da8-8359-439c-92-97-bb-c5-29-9a-7d-87')
    @commethod(3)
    def Navigate(direction: Windows.Win32.UI.Accessibility.NavigateDirection, pRetVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderFragment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRuntimeId(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_BoundingRectangle(pRetVal: POINTER(Windows.Win32.UI.Accessibility.UiaRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEmbeddedFragmentRoots(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFocus() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_FragmentRoot(pRetVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderFragmentRoot_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderFragmentRoot(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('620ce2a5-ab8f-40a9-86-cb-de-3c-75-59-9b-58')
    @commethod(3)
    def ElementProviderFromPoint(x: Double, y: Double, pRetVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderFragment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFocus(pRetVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderFragment_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderHostingAccessibles(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('24be0b07-d37d-487a-98-cf-a1-3e-d4-65-e9-b3')
    @commethod(3)
    def GetEmbeddedAccessibles(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderHwndOverride(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1d5df27c-8947-4425-b8-d9-79-78-7b-b4-60-b8')
    @commethod(3)
    def GetOverrideProviderForHwnd(hwnd: Windows.Win32.Foundation.HWND, pRetVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderSimple(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d6dd68d1-86fd-4332-86-66-9a-be-de-a2-d2-4c')
    @commethod(3)
    def get_ProviderOptions(pRetVal: POINTER(Windows.Win32.UI.Accessibility.ProviderOptions)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPatternProvider(patternId: Windows.Win32.UI.Accessibility.UIA_PATTERN_ID, pRetVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyValue(propertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, pRetVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_HostRawElementProvider(pRetVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderSimple2(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IRawElementProviderSimple
    Guid = Guid('a0a839a9-8da1-4a82-80-6a-8e-0d-44-e7-9f-56')
    @commethod(7)
    def ShowContextMenu() -> Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderSimple3(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IRawElementProviderSimple2
    Guid = Guid('fcf5d820-d7ec-4613-bd-f6-42-a8-4c-e7-da-af')
    @commethod(8)
    def GetMetadataValue(targetId: Int32, metadataId: Windows.Win32.UI.Accessibility.UIA_METADATA_ID, returnVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderWindowlessSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0a2a93cc-bfad-42ac-9b-2e-09-91-fb-0d-3e-a0')
    @commethod(3)
    def GetAdjacentFragment(direction: Windows.Win32.UI.Accessibility.NavigateDirection, ppParent: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderFragment_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRuntimeIdPrefix(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IRichEditUiaInformation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetBoundaryRectangle(pUiaRect: POINTER(Windows.Win32.UI.Accessibility.UiaRect_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsVisible() -> Windows.Win32.Foundation.HRESULT: ...
class IRicheditWindowlessAccessibility(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def CreateProvider(pSite: Windows.Win32.UI.Accessibility.IRawElementProviderWindowlessSite_head, ppProvider: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IScrollItemProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2360c714-4bf1-4b26-ba-65-9b-21-31-61-27-eb')
    @commethod(3)
    def ScrollIntoView() -> Windows.Win32.Foundation.HRESULT: ...
class IScrollProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b38b8077-1fc3-42a5-8c-ae-d4-0c-22-15-05-5a')
    @commethod(3)
    def Scroll(horizontalAmount: Windows.Win32.UI.Accessibility.ScrollAmount, verticalAmount: Windows.Win32.UI.Accessibility.ScrollAmount) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetScrollPercent(horizontalPercent: Double, verticalPercent: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_HorizontalScrollPercent(pRetVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_VerticalScrollPercent(pRetVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_HorizontalViewSize(pRetVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_VerticalViewSize(pRetVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_HorizontallyScrollable(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_VerticallyScrollable(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ISelectionItemProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2acad808-b2d4-452d-a4-07-91-ff-1a-d1-67-b2')
    @commethod(3)
    def Select() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddToSelection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveFromSelection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_IsSelected(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_SelectionContainer(pRetVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISelectionProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fb8b03af-3bdf-48d4-bd-36-1a-65-79-3b-e1-68')
    @commethod(3)
    def GetSelection(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CanSelectMultiple(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_IsSelectionRequired(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ISelectionProvider2(c_void_p):
    extends: Windows.Win32.UI.Accessibility.ISelectionProvider
    Guid = Guid('14f68475-ee1c-44f6-a8-69-d2-39-38-1f-0f-e7')
    @commethod(6)
    def get_FirstSelectedItem(retVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_LastSelectedItem(retVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentSelectedItem(retVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ItemCount(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpreadsheetItemProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('eaed4660-7b3d-4879-a2-e6-36-5c-e6-03-f3-d0')
    @commethod(3)
    def get_Formula(pRetVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAnnotationObjects(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAnnotationTypes(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class ISpreadsheetProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6f6b5d35-5525-4f80-b7-58-85-47-38-32-ff-c7')
    @commethod(3)
    def GetItemByName(name: Windows.Win32.Foundation.PWSTR, pRetVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IStylesProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('19b6b649-f5d7-4a6d-bd-cb-12-92-52-be-58-8a')
    @commethod(3)
    def get_StyleId(retVal: POINTER(Windows.Win32.UI.Accessibility.UIA_STYLE_ID)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_StyleName(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_FillColor(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_FillPatternStyle(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Shape(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_FillPatternColor(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ExtendedProperties(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISynchronizedInputProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('29db1a06-02ce-4cf7-9b-42-56-5d-4f-ab-20-ee')
    @commethod(3)
    def StartListening(inputType: Windows.Win32.UI.Accessibility.SynchronizedInputType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Cancel() -> Windows.Win32.Foundation.HRESULT: ...
class ITableItemProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b9734fa6-771f-4d78-9c-90-25-17-99-93-49-cd')
    @commethod(3)
    def GetRowHeaderItems(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColumnHeaderItems(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class ITableProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9c860395-97b3-490a-b5-2a-85-8c-c2-2a-f1-66')
    @commethod(3)
    def GetRowHeaders(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColumnHeaders(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_RowOrColumnMajor(pRetVal: POINTER(Windows.Win32.UI.Accessibility.RowOrColumnMajor)) -> Windows.Win32.Foundation.HRESULT: ...
class ITextChildProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4c2de2b9-c88f-4f88-a1-11-f1-d3-36-b7-d1-a9')
    @commethod(3)
    def get_TextContainer(pRetVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_TextRange(pRetVal: POINTER(Windows.Win32.UI.Accessibility.ITextRangeProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITextEditProvider(c_void_p):
    extends: Windows.Win32.UI.Accessibility.ITextProvider
    Guid = Guid('ea3605b4-3a05-400e-b5-f9-4e-91-b4-0f-61-76')
    @commethod(9)
    def GetActiveComposition(pRetVal: POINTER(Windows.Win32.UI.Accessibility.ITextRangeProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConversionTarget(pRetVal: POINTER(Windows.Win32.UI.Accessibility.ITextRangeProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITextProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3589c92c-63f3-4367-99-bb-ad-a6-53-b7-7c-f2')
    @commethod(3)
    def GetSelection(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVisibleRanges(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RangeFromChild(childElement: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, pRetVal: POINTER(Windows.Win32.UI.Accessibility.ITextRangeProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RangeFromPoint(point: Windows.Win32.UI.Accessibility.UiaPoint, pRetVal: POINTER(Windows.Win32.UI.Accessibility.ITextRangeProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_DocumentRange(pRetVal: POINTER(Windows.Win32.UI.Accessibility.ITextRangeProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SupportedTextSelection(pRetVal: POINTER(Windows.Win32.UI.Accessibility.SupportedTextSelection)) -> Windows.Win32.Foundation.HRESULT: ...
class ITextProvider2(c_void_p):
    extends: Windows.Win32.UI.Accessibility.ITextProvider
    Guid = Guid('0dc5e6ed-3e16-4bf1-8f-9a-a9-79-87-8b-c1-95')
    @commethod(9)
    def RangeFromAnnotation(annotationElement: Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head, pRetVal: POINTER(Windows.Win32.UI.Accessibility.ITextRangeProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCaretRange(isActive: POINTER(Windows.Win32.Foundation.BOOL), pRetVal: POINTER(Windows.Win32.UI.Accessibility.ITextRangeProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITextRangeProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5347ad7b-c355-46f8-af-f5-90-90-33-58-2f-63')
    @commethod(3)
    def Clone(pRetVal: POINTER(Windows.Win32.UI.Accessibility.ITextRangeProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Compare(range: Windows.Win32.UI.Accessibility.ITextRangeProvider_head, pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CompareEndpoints(endpoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, targetRange: Windows.Win32.UI.Accessibility.ITextRangeProvider_head, targetEndpoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ExpandToEnclosingUnit(unit: Windows.Win32.UI.Accessibility.TextUnit) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindAttribute(attributeId: Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID, val: Windows.Win32.System.Com.VARIANT, backward: Windows.Win32.Foundation.BOOL, pRetVal: POINTER(Windows.Win32.UI.Accessibility.ITextRangeProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindText(text: Windows.Win32.Foundation.BSTR, backward: Windows.Win32.Foundation.BOOL, ignoreCase: Windows.Win32.Foundation.BOOL, pRetVal: POINTER(Windows.Win32.UI.Accessibility.ITextRangeProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAttributeValue(attributeId: Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID, pRetVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBoundingRectangles(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetEnclosingElement(pRetVal: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetText(maxLength: Int32, pRetVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Move(unit: Windows.Win32.UI.Accessibility.TextUnit, count: Int32, pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def MoveEndpointByUnit(endpoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, unit: Windows.Win32.UI.Accessibility.TextUnit, count: Int32, pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def MoveEndpointByRange(endpoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, targetRange: Windows.Win32.UI.Accessibility.ITextRangeProvider_head, targetEndpoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Select() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AddToSelection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RemoveFromSelection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ScrollIntoView(alignToTop: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetChildren(pRetVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class ITextRangeProvider2(c_void_p):
    extends: Windows.Win32.UI.Accessibility.ITextRangeProvider
    Guid = Guid('9bbce42c-1921-4f18-89-ca-db-a1-91-0a-03-86')
    @commethod(21)
    def ShowContextMenu() -> Windows.Win32.Foundation.HRESULT: ...
class IToggleProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('56d00bd0-c4f4-433c-a8-36-1a-52-a5-7e-08-92')
    @commethod(3)
    def Toggle() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ToggleState(pRetVal: POINTER(Windows.Win32.UI.Accessibility.ToggleState)) -> Windows.Win32.Foundation.HRESULT: ...
class ITransformProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6829ddc4-4f91-4ffa-b8-6f-bd-3e-29-87-cb-4c')
    @commethod(3)
    def Move(x: Double, y: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Resize(width: Double, height: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Rotate(degrees: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CanMove(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CanResize(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CanRotate(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ITransformProvider2(c_void_p):
    extends: Windows.Win32.UI.Accessibility.ITransformProvider
    Guid = Guid('4758742f-7ac2-460c-bc-48-09-fc-09-30-8a-93')
    @commethod(9)
    def Zoom(zoom: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CanZoom(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ZoomLevel(pRetVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ZoomMinimum(pRetVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ZoomMaximum(pRetVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ZoomByUnit(zoomUnit: Windows.Win32.UI.Accessibility.ZoomUnit) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30cbe57d-d9d0-452a-ab-13-7a-c5-ac-48-25-ee')
    @commethod(3)
    def CompareElements(el1: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, el2: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, areSame: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CompareRuntimeIds(runtimeId1: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), runtimeId2: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), areSame: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRootElement(root: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ElementFromHandle(hwnd: Windows.Win32.Foundation.HWND, element: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ElementFromPoint(pt: Windows.Win32.Foundation.POINT, element: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFocusedElement(element: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRootElementBuildCache(cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, root: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ElementFromHandleBuildCache(hwnd: Windows.Win32.Foundation.HWND, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, element: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ElementFromPointBuildCache(pt: Windows.Win32.Foundation.POINT, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, element: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFocusedElementBuildCache(cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, element: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateTreeWalker(pCondition: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, walker: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTreeWalker_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ControlViewWalker(walker: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTreeWalker_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ContentViewWalker(walker: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTreeWalker_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_RawViewWalker(walker: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTreeWalker_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RawViewCondition(condition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ControlViewCondition(condition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ContentViewCondition(condition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CreateCacheRequest(cacheRequest: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CreateTrueCondition(newCondition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateFalseCondition(newCondition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreatePropertyCondition(propertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, value: Windows.Win32.System.Com.VARIANT, newCondition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def CreatePropertyConditionEx(propertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, value: Windows.Win32.System.Com.VARIANT, flags: Windows.Win32.UI.Accessibility.PropertyConditionFlags, newCondition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CreateAndCondition(condition1: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, condition2: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, newCondition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def CreateAndConditionFromArray(conditions: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), newCondition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def CreateAndConditionFromNativeArray(conditions: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head), conditionCount: Int32, newCondition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def CreateOrCondition(condition1: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, condition2: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, newCondition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def CreateOrConditionFromArray(conditions: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), newCondition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CreateOrConditionFromNativeArray(conditions: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head), conditionCount: Int32, newCondition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def CreateNotCondition(condition: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, newCondition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def AddAutomationEventHandler(eventId: Windows.Win32.UI.Accessibility.UIA_EVENT_ID, element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, scope: Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def RemoveAutomationEventHandler(eventId: Windows.Win32.UI.Accessibility.UIA_EVENT_ID, element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def AddPropertyChangedEventHandlerNativeArray(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, scope: Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head, propertyArray: POINTER(Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID), propertyCount: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def AddPropertyChangedEventHandler(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, scope: Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head, propertyArray: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def RemovePropertyChangedEventHandler(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def AddStructureChangedEventHandler(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, scope: Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationStructureChangedEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def RemoveStructureChangedEventHandler(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationStructureChangedEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def AddFocusChangedEventHandler(cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationFocusChangedEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def RemoveFocusChangedEventHandler(handler: Windows.Win32.UI.Accessibility.IUIAutomationFocusChangedEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def RemoveAllEventHandlers() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def IntNativeArrayToSafeArray(array: POINTER(Int32), arrayCount: Int32, safeArray: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def IntSafeArrayToNativeArray(intArray: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), array: POINTER(POINTER(Int32)), arrayCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def RectToVariant(rc: Windows.Win32.Foundation.RECT, var: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def VariantToRect(var: Windows.Win32.System.Com.VARIANT, rc: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def SafeArrayToRectNativeArray(rects: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), rectArray: POINTER(POINTER(Windows.Win32.Foundation.RECT_head)), rectArrayCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def CreateProxyFactoryEntry(factory: Windows.Win32.UI.Accessibility.IUIAutomationProxyFactory_head, factoryEntry: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationProxyFactoryEntry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_ProxyFactoryMapping(factoryMapping: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationProxyFactoryMapping_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def GetPropertyProgrammaticName(property: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def GetPatternProgrammaticName(pattern: Windows.Win32.UI.Accessibility.UIA_PATTERN_ID, name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def PollForPotentialSupportedPatterns(pElement: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, patternIds: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), patternNames: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def PollForPotentialSupportedProperties(pElement: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, propertyIds: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), propertyNames: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def CheckNotSupported(value: Windows.Win32.System.Com.VARIANT, isNotSupported: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def get_ReservedNotSupportedValue(notSupportedValue: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_ReservedMixedAttributeValue(mixedAttributeValue: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def ElementFromIAccessible(accessible: Windows.Win32.UI.Accessibility.IAccessible_head, childId: Int32, element: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def ElementFromIAccessibleBuildCache(accessible: Windows.Win32.UI.Accessibility.IAccessible_head, childId: Int32, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, element: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomation2(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomation
    Guid = Guid('34723aff-0c9d-49d0-98-96-7a-b5-2d-f8-cd-8a')
    @commethod(58)
    def get_AutoSetFocus(autoSetFocus: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def put_AutoSetFocus(autoSetFocus: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def get_ConnectionTimeout(timeout: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def put_ConnectionTimeout(timeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def get_TransactionTimeout(timeout: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def put_TransactionTimeout(timeout: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomation3(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomation2
    Guid = Guid('73d768da-9b51-4b89-93-6e-c2-09-29-09-73-e7')
    @commethod(64)
    def AddTextEditTextChangedEventHandler(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, scope: Windows.Win32.UI.Accessibility.TreeScope, textEditChangeType: Windows.Win32.UI.Accessibility.TextEditChangeType, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def RemoveTextEditTextChangedEventHandler(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomation4(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomation3
    Guid = Guid('1189c02a-05f8-4319-8e-21-e8-17-e3-db-28-60')
    @commethod(66)
    def AddChangesEventHandler(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, scope: Windows.Win32.UI.Accessibility.TreeScope, changeTypes: POINTER(Int32), changesCount: Int32, pCacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationChangesEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def RemoveChangesEventHandler(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationChangesEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomation5(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomation4
    Guid = Guid('25f700c8-d816-4057-a9-dc-3c-bd-ee-77-e2-56')
    @commethod(68)
    def AddNotificationEventHandler(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, scope: Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationNotificationEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def RemoveNotificationEventHandler(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationNotificationEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomation6(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomation5
    Guid = Guid('aae072da-29e3-413d-87-a7-19-2d-bf-81-ed-10')
    @commethod(70)
    def CreateEventHandlerGroup(handlerGroup: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationEventHandlerGroup_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def AddEventHandlerGroup(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, handlerGroup: Windows.Win32.UI.Accessibility.IUIAutomationEventHandlerGroup_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def RemoveEventHandlerGroup(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, handlerGroup: Windows.Win32.UI.Accessibility.IUIAutomationEventHandlerGroup_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def get_ConnectionRecoveryBehavior(connectionRecoveryBehaviorOptions: POINTER(Windows.Win32.UI.Accessibility.ConnectionRecoveryBehaviorOptions)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def put_ConnectionRecoveryBehavior(connectionRecoveryBehaviorOptions: Windows.Win32.UI.Accessibility.ConnectionRecoveryBehaviorOptions) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def get_CoalesceEvents(coalesceEventsOptions: POINTER(Windows.Win32.UI.Accessibility.CoalesceEventsOptions)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def put_CoalesceEvents(coalesceEventsOptions: Windows.Win32.UI.Accessibility.CoalesceEventsOptions) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def AddActiveTextPositionChangedEventHandler(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, scope: Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def RemoveActiveTextPositionChangedEventHandler(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationActiveTextPositionChangedEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f97933b0-8dae-4496-89-97-5b-a0-15-fe-0d-82')
    @commethod(3)
    def HandleActiveTextPositionChangedEvent(sender: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, range: Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationAndCondition(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationCondition
    Guid = Guid('a7d0af36-b912-45fe-98-55-09-1d-dc-17-4a-ec')
    @commethod(3)
    def get_ChildCount(childCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetChildrenAsNativeArray(childArray: POINTER(POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)), childArrayCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChildren(childArray: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationAnnotationPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9a175b21-339e-41b1-8e-8b-62-3f-6b-68-10-98')
    @commethod(3)
    def get_CurrentAnnotationTypeId(retVal: POINTER(Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentAnnotationTypeName(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentAuthor(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentDateTime(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentTarget(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CachedAnnotationTypeId(retVal: POINTER(Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CachedAnnotationTypeName(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CachedAuthor(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CachedDateTime(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CachedTarget(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationBoolCondition(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationCondition
    Guid = Guid('1b4e1f2e-75eb-4d0b-89-52-5a-69-98-8e-23-07')
    @commethod(3)
    def get_BooleanValue(boolVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationCacheRequest(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b32a92b5-bc25-4078-9c-08-d7-ee-95-c4-8e-03')
    @commethod(3)
    def AddProperty(propertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddPattern(patternId: Windows.Win32.UI.Accessibility.UIA_PATTERN_ID) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Clone(clonedRequest: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_TreeScope(scope: POINTER(Windows.Win32.UI.Accessibility.TreeScope)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_TreeScope(scope: Windows.Win32.UI.Accessibility.TreeScope) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_TreeFilter(filter: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_TreeFilter(filter: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AutomationElementMode(mode: POINTER(Windows.Win32.UI.Accessibility.AutomationElementMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_AutomationElementMode(mode: Windows.Win32.UI.Accessibility.AutomationElementMode) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationChangesEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('58edca55-2c3e-4980-b1-b9-56-c1-7f-27-a2-a0')
    @commethod(3)
    def HandleChangesEvent(sender: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, uiaChanges: POINTER(Windows.Win32.UI.Accessibility.UiaChangeInfo_head), changesCount: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationCondition(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('352ffba8-0973-437c-a6-1f-f6-4c-af-d8-1d-f9')
class IUIAutomationCustomNavigationPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('01ea217a-1766-47ed-a6-cc-ac-f4-92-85-4b-1f')
    @commethod(3)
    def Navigate(direction: Windows.Win32.UI.Accessibility.NavigateDirection, pRetVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationDockPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fde5ef97-1464-48f6-90-bf-43-d0-94-8e-86-ec')
    @commethod(3)
    def SetDockPosition(dockPos: Windows.Win32.UI.Accessibility.DockPosition) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentDockPosition(retVal: POINTER(Windows.Win32.UI.Accessibility.DockPosition)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CachedDockPosition(retVal: POINTER(Windows.Win32.UI.Accessibility.DockPosition)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationDragPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1dc7b570-1f54-4bad-bc-da-d3-6a-72-2f-b7-bd')
    @commethod(3)
    def get_CurrentIsGrabbed(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CachedIsGrabbed(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentDropEffect(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CachedDropEffect(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentDropEffects(retVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CachedDropEffects(retVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentGrabbedItems(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCachedGrabbedItems(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationDropTargetPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('69a095f7-eee4-430e-a4-6b-fb-73-b1-ae-39-a5')
    @commethod(3)
    def get_CurrentDropTargetEffect(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CachedDropTargetEffect(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentDropTargetEffects(retVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CachedDropTargetEffects(retVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d22108aa-8ac5-49a5-83-7b-37-bb-b3-d7-59-1e')
    @commethod(3)
    def SetFocus() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRuntimeId(runtimeId: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindFirst(scope: Windows.Win32.UI.Accessibility.TreeScope, condition: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, found: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindAll(scope: Windows.Win32.UI.Accessibility.TreeScope, condition: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, found: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindFirstBuildCache(scope: Windows.Win32.UI.Accessibility.TreeScope, condition: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, found: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindAllBuildCache(scope: Windows.Win32.UI.Accessibility.TreeScope, condition: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, found: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def BuildUpdatedCache(cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, updatedElement: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCurrentPropertyValue(propertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, retVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCurrentPropertyValueEx(propertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, ignoreDefaultValue: Windows.Win32.Foundation.BOOL, retVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCachedPropertyValue(propertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, retVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCachedPropertyValueEx(propertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, ignoreDefaultValue: Windows.Win32.Foundation.BOOL, retVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCurrentPatternAs(patternId: Windows.Win32.UI.Accessibility.UIA_PATTERN_ID, riid: POINTER(Guid), patternObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCachedPatternAs(patternId: Windows.Win32.UI.Accessibility.UIA_PATTERN_ID, riid: POINTER(Guid), patternObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCurrentPattern(patternId: Windows.Win32.UI.Accessibility.UIA_PATTERN_ID, patternObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCachedPattern(patternId: Windows.Win32.UI.Accessibility.UIA_PATTERN_ID, patternObject: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCachedParent(parent: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCachedChildren(children: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_CurrentProcessId(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_CurrentControlType(retVal: POINTER(Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CurrentLocalizedControlType(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_CurrentName(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_CurrentAcceleratorKey(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_CurrentAccessKey(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_CurrentHasKeyboardFocus(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_CurrentIsKeyboardFocusable(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_CurrentIsEnabled(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_CurrentAutomationId(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_CurrentClassName(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_CurrentHelpText(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_CurrentCulture(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_CurrentIsControlElement(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_CurrentIsContentElement(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_CurrentIsPassword(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_CurrentNativeWindowHandle(retVal: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_CurrentItemType(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_CurrentIsOffscreen(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_CurrentOrientation(retVal: POINTER(Windows.Win32.UI.Accessibility.OrientationType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_CurrentFrameworkId(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_CurrentIsRequiredForForm(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_CurrentItemStatus(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_CurrentBoundingRectangle(retVal: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_CurrentLabeledBy(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_CurrentAriaRole(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_CurrentAriaProperties(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def get_CurrentIsDataValidForForm(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_CurrentControllerFor(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_CurrentDescribedBy(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_CurrentFlowsTo(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def get_CurrentProviderDescription(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def get_CachedProcessId(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_CachedControlType(retVal: POINTER(Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def get_CachedLocalizedControlType(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_CachedName(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def get_CachedAcceleratorKey(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_CachedAccessKey(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def get_CachedHasKeyboardFocus(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_CachedIsKeyboardFocusable(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def get_CachedIsEnabled(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def get_CachedAutomationId(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def get_CachedClassName(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def get_CachedHelpText(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def get_CachedCulture(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_CachedIsControlElement(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def get_CachedIsContentElement(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def get_CachedIsPassword(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def get_CachedNativeWindowHandle(retVal: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def get_CachedItemType(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def get_CachedIsOffscreen(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def get_CachedOrientation(retVal: POINTER(Windows.Win32.UI.Accessibility.OrientationType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def get_CachedFrameworkId(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def get_CachedIsRequiredForForm(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def get_CachedItemStatus(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def get_CachedBoundingRectangle(retVal: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def get_CachedLabeledBy(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def get_CachedAriaRole(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def get_CachedAriaProperties(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def get_CachedIsDataValidForForm(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def get_CachedControllerFor(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def get_CachedDescribedBy(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def get_CachedFlowsTo(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def get_CachedProviderDescription(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def GetClickablePoint(clickable: POINTER(Windows.Win32.Foundation.POINT_head), gotClickable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement2(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationElement
    Guid = Guid('6749c683-f70d-4487-a6-98-5f-79-d5-52-90-d6')
    @commethod(85)
    def get_CurrentOptimizeForVisualContent(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def get_CachedOptimizeForVisualContent(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def get_CurrentLiveSetting(retVal: POINTER(Windows.Win32.UI.Accessibility.LiveSetting)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def get_CachedLiveSetting(retVal: POINTER(Windows.Win32.UI.Accessibility.LiveSetting)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def get_CurrentFlowsFrom(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def get_CachedFlowsFrom(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement3(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationElement2
    Guid = Guid('8471df34-aee0-4a01-a7-de-7d-b9-af-12-c2-96')
    @commethod(91)
    def ShowContextMenu() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def get_CurrentIsPeripheral(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def get_CachedIsPeripheral(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement4(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationElement3
    Guid = Guid('3b6e233c-52fb-4063-a4-c9-77-c0-75-c2-a0-6b')
    @commethod(94)
    def get_CurrentPositionInSet(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(95)
    def get_CurrentSizeOfSet(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def get_CurrentLevel(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(97)
    def get_CurrentAnnotationTypes(retVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def get_CurrentAnnotationObjects(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(99)
    def get_CachedPositionInSet(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(100)
    def get_CachedSizeOfSet(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(101)
    def get_CachedLevel(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(102)
    def get_CachedAnnotationTypes(retVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(103)
    def get_CachedAnnotationObjects(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement5(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationElement4
    Guid = Guid('98141c1d-0d0e-4175-bb-e2-6b-ff-45-58-42-a7')
    @commethod(104)
    def get_CurrentLandmarkType(retVal: POINTER(Windows.Win32.UI.Accessibility.UIA_LANDMARKTYPE_ID)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(105)
    def get_CurrentLocalizedLandmarkType(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(106)
    def get_CachedLandmarkType(retVal: POINTER(Windows.Win32.UI.Accessibility.UIA_LANDMARKTYPE_ID)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(107)
    def get_CachedLocalizedLandmarkType(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement6(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationElement5
    Guid = Guid('4780d450-8bca-4977-af-a5-a4-a5-17-f5-55-e3')
    @commethod(108)
    def get_CurrentFullDescription(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(109)
    def get_CachedFullDescription(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement7(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationElement6
    Guid = Guid('204e8572-cfc3-4c11-b0-c8-7d-a7-42-07-50-b7')
    @commethod(110)
    def FindFirstWithOptions(scope: Windows.Win32.UI.Accessibility.TreeScope, condition: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, traversalOptions: Windows.Win32.UI.Accessibility.TreeTraversalOptions, root: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, found: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(111)
    def FindAllWithOptions(scope: Windows.Win32.UI.Accessibility.TreeScope, condition: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, traversalOptions: Windows.Win32.UI.Accessibility.TreeTraversalOptions, root: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, found: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(112)
    def FindFirstWithOptionsBuildCache(scope: Windows.Win32.UI.Accessibility.TreeScope, condition: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, traversalOptions: Windows.Win32.UI.Accessibility.TreeTraversalOptions, root: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, found: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(113)
    def FindAllWithOptionsBuildCache(scope: Windows.Win32.UI.Accessibility.TreeScope, condition: Windows.Win32.UI.Accessibility.IUIAutomationCondition_head, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, traversalOptions: Windows.Win32.UI.Accessibility.TreeTraversalOptions, root: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, found: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(114)
    def GetCurrentMetadataValue(targetId: Int32, metadataId: Windows.Win32.UI.Accessibility.UIA_METADATA_ID, returnVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement8(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationElement7
    Guid = Guid('8c60217d-5411-4cde-bc-c0-1c-ed-a2-23-83-0c')
    @commethod(115)
    def get_CurrentHeadingLevel(retVal: POINTER(Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(116)
    def get_CachedHeadingLevel(retVal: POINTER(Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement9(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationElement8
    Guid = Guid('39325fac-039d-440e-a3-a3-5e-b8-1a-5c-ec-c3')
    @commethod(117)
    def get_CurrentIsDialog(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(118)
    def get_CachedIsDialog(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElementArray(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('14314595-b4bc-4055-95-f2-58-f2-e4-2c-98-55')
    @commethod(3)
    def get_Length(length: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetElement(index: Int32, element: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('146c3c17-f12e-4e22-8c-27-f8-94-b9-b7-9c-69')
    @commethod(3)
    def HandleAutomationEvent(sender: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, eventId: Windows.Win32.UI.Accessibility.UIA_EVENT_ID) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationEventHandlerGroup(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c9ee12f2-c13b-4408-99-7c-63-99-14-37-7f-4e')
    @commethod(3)
    def AddActiveTextPositionChangedEventHandler(scope: Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddAutomationEventHandler(eventId: Windows.Win32.UI.Accessibility.UIA_EVENT_ID, scope: Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddChangesEventHandler(scope: Windows.Win32.UI.Accessibility.TreeScope, changeTypes: POINTER(Int32), changesCount: Int32, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationChangesEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddNotificationEventHandler(scope: Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationNotificationEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddPropertyChangedEventHandler(scope: Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head, propertyArray: POINTER(Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID), propertyCount: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddStructureChangedEventHandler(scope: Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationStructureChangedEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddTextEditTextChangedEventHandler(scope: Windows.Win32.UI.Accessibility.TreeScope, textEditChangeType: Windows.Win32.UI.Accessibility.TextEditChangeType, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, handler: Windows.Win32.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationExpandCollapsePattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('619be086-1f4e-4ee4-ba-fa-21-01-28-73-87-30')
    @commethod(3)
    def Expand() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Collapse() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentExpandCollapseState(retVal: POINTER(Windows.Win32.UI.Accessibility.ExpandCollapseState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CachedExpandCollapseState(retVal: POINTER(Windows.Win32.UI.Accessibility.ExpandCollapseState)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationFocusChangedEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c270f6b5-5c69-4290-97-45-7a-7f-97-16-94-68')
    @commethod(3)
    def HandleFocusChangedEvent(sender: Windows.Win32.UI.Accessibility.IUIAutomationElement_head) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationGridItemPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('78f8ef57-66c3-4e09-bd-7c-e7-9b-20-04-89-4d')
    @commethod(3)
    def get_CurrentContainingGrid(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentRow(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentColumn(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentRowSpan(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentColumnSpan(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CachedContainingGrid(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CachedRow(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CachedColumn(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CachedRowSpan(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CachedColumnSpan(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationGridPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('414c3cdc-856b-4f5b-85-38-31-31-c6-30-25-50')
    @commethod(3)
    def GetItem(row: Int32, column: Int32, element: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentRowCount(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentColumnCount(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CachedRowCount(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CachedColumnCount(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationInvokePattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fb377fbe-8ea6-46d5-9c-73-64-99-64-2d-30-59')
    @commethod(3)
    def Invoke() -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationItemContainerPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c690fdb2-27a8-423c-81-2d-42-97-73-c9-08-4e')
    @commethod(3)
    def FindItemByProperty(pStartAfter: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, propertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, value: Windows.Win32.System.Com.VARIANT, pFound: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationLegacyIAccessiblePattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('828055ad-355b-4435-86-d5-3b-51-c1-4a-9b-1b')
    @commethod(3)
    def Select(flagsSelect: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DoDefaultAction() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(szValue: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentChildId(pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentName(pszName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentValue(pszValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentDescription(pszDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentRole(pdwRole: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CurrentState(pdwState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CurrentHelp(pszHelp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_CurrentKeyboardShortcut(pszKeyboardShortcut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCurrentSelection(pvarSelectedChildren: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CurrentDefaultAction(pszDefaultAction: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CachedChildId(pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_CachedName(pszName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_CachedValue(pszValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_CachedDescription(pszDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_CachedRole(pdwRole: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_CachedState(pdwState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CachedHelp(pszHelp: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_CachedKeyboardShortcut(pszKeyboardShortcut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetCachedSelection(pvarSelectedChildren: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_CachedDefaultAction(pszDefaultAction: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetIAccessible(ppAccessible: POINTER(Windows.Win32.UI.Accessibility.IAccessible_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationMultipleViewPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8d253c91-1dc5-4bb5-b1-8f-ad-e1-6f-a4-95-e8')
    @commethod(3)
    def GetViewName(view: Int32, name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCurrentView(view: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentCurrentView(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentSupportedViews(retVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CachedCurrentView(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCachedSupportedViews(retVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationNotCondition(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationCondition
    Guid = Guid('f528b657-847b-498c-88-96-d5-2b-56-54-07-a1')
    @commethod(3)
    def GetChild(condition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationNotificationEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c7cb2637-e6c2-4d0c-85-de-49-48-c0-21-75-c7')
    @commethod(3)
    def HandleNotificationEvent(sender: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, notificationKind: Windows.Win32.UI.Accessibility.NotificationKind, notificationProcessing: Windows.Win32.UI.Accessibility.NotificationProcessing, displayString: Windows.Win32.Foundation.BSTR, activityId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationObjectModelPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('71c284b3-c14d-4d14-98-1e-19-75-1b-0d-75-6d')
    @commethod(3)
    def GetUnderlyingObjectModel(retVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationOrCondition(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationCondition
    Guid = Guid('8753f032-3db1-47b5-a1-fc-6e-34-a2-66-c7-12')
    @commethod(3)
    def get_ChildCount(childCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetChildrenAsNativeArray(childArray: POINTER(POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)), childArrayCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChildren(childArray: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationPatternHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d97022f3-a947-465e-8b-2a-ac-43-15-fa-54-e8')
    @commethod(3)
    def CreateClientWrapper(pPatternInstance: Windows.Win32.UI.Accessibility.IUIAutomationPatternInstance_head, pClientWrapper: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Dispatch(pTarget: Windows.Win32.System.Com.IUnknown_head, index: UInt32, pParams: POINTER(Windows.Win32.UI.Accessibility.UIAutomationParameter_head), cParams: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationPatternInstance(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c03a7fe4-9431-409f-be-d8-ae-7c-22-99-bc-8d')
    @commethod(3)
    def GetProperty(index: UInt32, cached: Windows.Win32.Foundation.BOOL, type: Windows.Win32.UI.Accessibility.UIAutomationType, pPtr: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CallMethod(index: UInt32, pParams: POINTER(Windows.Win32.UI.Accessibility.UIAutomationParameter_head), cParams: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationPropertyChangedEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('40cd37d4-c756-4b0c-8c-6f-bd-df-ee-b1-3b-50')
    @commethod(3)
    def HandlePropertyChangedEvent(sender: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, propertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, newValue: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationPropertyCondition(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationCondition
    Guid = Guid('99ebf2cb-5578-4267-9a-d4-af-d6-ea-77-e9-4b')
    @commethod(3)
    def get_PropertyId(propertyId: POINTER(Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_PropertyValue(propertyValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_PropertyConditionFlags(flags: POINTER(Windows.Win32.UI.Accessibility.PropertyConditionFlags)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationProxyFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('85b94ecd-849d-42b6-b9-4d-d6-db-23-fd-f5-a4')
    @commethod(3)
    def CreateProvider(hwnd: Windows.Win32.Foundation.HWND, idObject: Int32, idChild: Int32, provider: POINTER(Windows.Win32.UI.Accessibility.IRawElementProviderSimple_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ProxyFactoryId(factoryId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationProxyFactoryEntry(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d50e472e-b64b-490c-bc-a1-d3-06-96-f9-f2-89')
    @commethod(3)
    def get_ProxyFactory(factory: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationProxyFactory_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ClassName(className: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_ImageName(imageName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_AllowSubstringMatch(allowSubstringMatch: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CanCheckBaseClass(canCheckBaseClass: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_NeedsAdviseEvents(adviseEvents: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_ClassName(className: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ImageName(imageName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_AllowSubstringMatch(allowSubstringMatch: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_CanCheckBaseClass(canCheckBaseClass: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_NeedsAdviseEvents(adviseEvents: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetWinEventsForAutomationEvent(eventId: Windows.Win32.UI.Accessibility.UIA_EVENT_ID, propertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, winEvents: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetWinEventsForAutomationEvent(eventId: Windows.Win32.UI.Accessibility.UIA_EVENT_ID, propertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, winEvents: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationProxyFactoryMapping(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('09e31e18-872d-4873-93-d1-1e-54-1e-c1-33-fd')
    @commethod(3)
    def get_Count(count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTable(table: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEntry(index: UInt32, entry: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationProxyFactoryEntry_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTable(factoryList: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InsertEntries(before: UInt32, factoryList: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InsertEntry(before: UInt32, factory: Windows.Win32.UI.Accessibility.IUIAutomationProxyFactoryEntry_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveEntry(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ClearTable() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RestoreDefaultTable() -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationRangeValuePattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('59213f4f-7346-49e5-b1-20-80-55-59-87-a1-48')
    @commethod(3)
    def SetValue(val: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentValue(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentIsReadOnly(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentMaximum(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentMinimum(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentLargeChange(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentSmallChange(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CachedValue(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CachedIsReadOnly(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CachedMaximum(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_CachedMinimum(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CachedLargeChange(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CachedSmallChange(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationRegistrar(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8609c4ec-4a1a-4d88-a3-57-5a-66-e0-60-e1-cf')
    @commethod(3)
    def RegisterProperty(property: POINTER(Windows.Win32.UI.Accessibility.UIAutomationPropertyInfo_head), propertyId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterEvent(event: POINTER(Windows.Win32.UI.Accessibility.UIAutomationEventInfo_head), eventId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterPattern(pattern: POINTER(Windows.Win32.UI.Accessibility.UIAutomationPatternInfo_head), pPatternId: POINTER(Int32), pPatternAvailablePropertyId: POINTER(Int32), propertyIdCount: UInt32, pPropertyIds: POINTER(Int32), eventIdCount: UInt32, pEventIds: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationScrollItemPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b488300f-d015-4f19-9c-29-bb-59-5e-36-45-ef')
    @commethod(3)
    def ScrollIntoView() -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationScrollPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('88f4d42a-e881-459d-a7-7c-73-bb-bb-7e-02-dc')
    @commethod(3)
    def Scroll(horizontalAmount: Windows.Win32.UI.Accessibility.ScrollAmount, verticalAmount: Windows.Win32.UI.Accessibility.ScrollAmount) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetScrollPercent(horizontalPercent: Double, verticalPercent: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentHorizontalScrollPercent(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentVerticalScrollPercent(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentHorizontalViewSize(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentVerticalViewSize(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentHorizontallyScrollable(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentVerticallyScrollable(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CachedHorizontalScrollPercent(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CachedVerticalScrollPercent(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_CachedHorizontalViewSize(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CachedVerticalViewSize(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CachedHorizontallyScrollable(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CachedVerticallyScrollable(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationSelectionItemPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a8efa66a-0fda-421a-91-94-38-02-1f-35-78-ea')
    @commethod(3)
    def Select() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddToSelection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveFromSelection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentIsSelected(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentSelectionContainer(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CachedIsSelected(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CachedSelectionContainer(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationSelectionPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5ed5202e-b2ac-47a6-b6-38-4b-0b-f1-40-d7-8e')
    @commethod(3)
    def GetCurrentSelection(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentCanSelectMultiple(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentIsSelectionRequired(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCachedSelection(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CachedCanSelectMultiple(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CachedIsSelectionRequired(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationSelectionPattern2(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationSelectionPattern
    Guid = Guid('0532bfae-c011-4e32-a3-43-6d-64-2d-79-85-55')
    @commethod(9)
    def get_CurrentFirstSelectedItem(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentLastSelectedItem(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CurrentCurrentSelectedItem(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CurrentItemCount(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_CachedFirstSelectedItem(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CachedLastSelectedItem(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CachedCurrentSelectedItem(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CachedItemCount(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationSpreadsheetItemPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7d4fb86c-8d34-40e1-8e-83-62-c1-52-04-e3-35')
    @commethod(3)
    def get_CurrentFormula(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentAnnotationObjects(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentAnnotationTypes(retVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CachedFormula(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCachedAnnotationObjects(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCachedAnnotationTypes(retVal: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationSpreadsheetPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7517a7c8-faae-4de9-9f-08-29-b9-1e-85-95-c1')
    @commethod(3)
    def GetItemByName(name: Windows.Win32.Foundation.BSTR, element: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationStructureChangedEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e81d1b4e-11c5-42f8-97-54-e7-03-6c-79-f0-54')
    @commethod(3)
    def HandleStructureChangedEvent(sender: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, changeType: Windows.Win32.UI.Accessibility.StructureChangeType, runtimeId: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationStylesPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('85b5f0a2-bd79-484a-ad-2b-38-8c-98-38-d5-fb')
    @commethod(3)
    def get_CurrentStyleId(retVal: POINTER(Windows.Win32.UI.Accessibility.UIA_STYLE_ID)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentStyleName(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentFillColor(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentFillPatternStyle(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentShape(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentFillPatternColor(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentExtendedProperties(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCurrentExtendedPropertiesAsArray(propertyArray: POINTER(POINTER(Windows.Win32.UI.Accessibility.ExtendedProperty_head)), propertyCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CachedStyleId(retVal: POINTER(Windows.Win32.UI.Accessibility.UIA_STYLE_ID)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CachedStyleName(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_CachedFillColor(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CachedFillPatternStyle(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CachedShape(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CachedFillPatternColor(retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_CachedExtendedProperties(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCachedExtendedPropertiesAsArray(propertyArray: POINTER(POINTER(Windows.Win32.UI.Accessibility.ExtendedProperty_head)), propertyCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationSynchronizedInputPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2233be0b-afb7-448b-9f-da-3b-37-8a-a5-ea-e1')
    @commethod(3)
    def StartListening(inputType: Windows.Win32.UI.Accessibility.SynchronizedInputType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Cancel() -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTableItemPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0b964eb3-ef2e-4464-9c-79-61-d6-17-37-a2-7e')
    @commethod(3)
    def GetCurrentRowHeaderItems(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentColumnHeaderItems(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCachedRowHeaderItems(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCachedColumnHeaderItems(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTablePattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('620e691c-ea96-4710-a8-50-75-4b-24-ce-24-17')
    @commethod(3)
    def GetCurrentRowHeaders(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentColumnHeaders(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentRowOrColumnMajor(retVal: POINTER(Windows.Win32.UI.Accessibility.RowOrColumnMajor)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCachedRowHeaders(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCachedColumnHeaders(retVal: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CachedRowOrColumnMajor(retVal: POINTER(Windows.Win32.UI.Accessibility.RowOrColumnMajor)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextChildPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6552b038-ae05-40c8-ab-fd-aa-08-35-2a-ab-86')
    @commethod(3)
    def get_TextContainer(container: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_TextRange(range: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextEditPattern(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationTextPattern
    Guid = Guid('17e21576-996c-4870-99-d9-bf-f3-23-38-0c-06')
    @commethod(9)
    def GetActiveComposition(range: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConversionTarget(range: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextEditTextChangedEventHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('92faa680-e704-4156-93-1a-e3-2d-5b-b3-8f-3f')
    @commethod(3)
    def HandleTextEditTextChangedEvent(sender: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, textEditChangeType: Windows.Win32.UI.Accessibility.TextEditChangeType, eventStrings: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('32eba289-3583-42c9-9c-59-3b-6d-9a-1e-9b-6a')
    @commethod(3)
    def RangeFromPoint(pt: Windows.Win32.Foundation.POINT, range: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RangeFromChild(child: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, range: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSelection(ranges: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRangeArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVisibleRanges(ranges: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRangeArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_DocumentRange(range: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SupportedTextSelection(supportedTextSelection: POINTER(Windows.Win32.UI.Accessibility.SupportedTextSelection)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextPattern2(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationTextPattern
    Guid = Guid('506a921a-fcc9-409f-b2-3b-37-eb-74-10-68-72')
    @commethod(9)
    def RangeFromAnnotation(annotation: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, range: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCaretRange(isActive: POINTER(Windows.Win32.Foundation.BOOL), range: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextRange(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a543cc6a-f4ae-494b-82-39-c8-14-48-11-87-a8')
    @commethod(3)
    def Clone(clonedRange: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Compare(range: Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head, areSame: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CompareEndpoints(srcEndPoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, range: Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head, targetEndPoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, compValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ExpandToEnclosingUnit(textUnit: Windows.Win32.UI.Accessibility.TextUnit) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindAttribute(attr: Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID, val: Windows.Win32.System.Com.VARIANT, backward: Windows.Win32.Foundation.BOOL, found: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindText(text: Windows.Win32.Foundation.BSTR, backward: Windows.Win32.Foundation.BOOL, ignoreCase: Windows.Win32.Foundation.BOOL, found: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAttributeValue(attr: Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID, value: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBoundingRectangles(boundingRects: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetEnclosingElement(enclosingElement: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetText(maxLength: Int32, text: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Move(unit: Windows.Win32.UI.Accessibility.TextUnit, count: Int32, moved: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def MoveEndpointByUnit(endpoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, unit: Windows.Win32.UI.Accessibility.TextUnit, count: Int32, moved: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def MoveEndpointByRange(srcEndPoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, range: Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head, targetEndPoint: Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Select() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AddToSelection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RemoveFromSelection() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ScrollIntoView(alignToTop: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetChildren(children: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextRange2(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationTextRange
    Guid = Guid('bb9b40e0-5e04-46bd-9b-e0-4b-60-1b-9a-fa-d4')
    @commethod(21)
    def ShowContextMenu() -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextRange3(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationTextRange2
    Guid = Guid('6a315d69-5512-4c2e-85-f0-53-fc-e6-dd-4b-c2')
    @commethod(22)
    def GetEnclosingElementBuildCache(cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, enclosingElement: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetChildrenBuildCache(cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, children: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElementArray_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetAttributeValues(attributeIds: POINTER(Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID), attributeIdCount: Int32, attributeValues: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextRangeArray(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ce4ae76a-e717-4c98-81-ea-47-37-1d-02-8e-b6')
    @commethod(3)
    def get_Length(length: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetElement(index: Int32, element: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationTextRange_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTogglePattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('94cf8058-9b8d-4ab9-8b-fd-4c-d0-a3-3c-8c-70')
    @commethod(3)
    def Toggle() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentToggleState(retVal: POINTER(Windows.Win32.UI.Accessibility.ToggleState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CachedToggleState(retVal: POINTER(Windows.Win32.UI.Accessibility.ToggleState)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTransformPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a9b55844-a55d-4ef0-92-6d-56-9c-16-ff-89-bb')
    @commethod(3)
    def Move(x: Double, y: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Resize(width: Double, height: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Rotate(degrees: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentCanMove(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentCanResize(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentCanRotate(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CachedCanMove(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CachedCanResize(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CachedCanRotate(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTransformPattern2(c_void_p):
    extends: Windows.Win32.UI.Accessibility.IUIAutomationTransformPattern
    Guid = Guid('6d74d017-6ecb-4381-b3-8b-3c-17-a4-8f-f1-c2')
    @commethod(12)
    def Zoom(zoomValue: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ZoomByUnit(zoomUnit: Windows.Win32.UI.Accessibility.ZoomUnit) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CurrentCanZoom(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CachedCanZoom(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CurrentZoomLevel(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_CachedZoomLevel(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_CurrentZoomMinimum(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_CachedZoomMinimum(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_CurrentZoomMaximum(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_CachedZoomMaximum(retVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTreeWalker(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4042c624-389c-4afc-a6-30-9d-f8-54-a5-41-fc')
    @commethod(3)
    def GetParentElement(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, parent: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFirstChildElement(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, first: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLastChildElement(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, last: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNextSiblingElement(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, next: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPreviousSiblingElement(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, previous: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def NormalizeElement(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, normalized: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetParentElementBuildCache(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, parent: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFirstChildElementBuildCache(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, first: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetLastChildElementBuildCache(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, last: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetNextSiblingElementBuildCache(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, next: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPreviousSiblingElementBuildCache(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, previous: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def NormalizeElementBuildCache(element: Windows.Win32.UI.Accessibility.IUIAutomationElement_head, cacheRequest: Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest_head, normalized: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationElement_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Condition(condition: POINTER(Windows.Win32.UI.Accessibility.IUIAutomationCondition_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationValuePattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a94cd8b1-0844-4cd6-9d-2d-64-05-37-ab-39-e9')
    @commethod(3)
    def SetValue(val: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentValue(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentIsReadOnly(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CachedValue(retVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CachedIsReadOnly(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationVirtualizedItemPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6ba3d7a6-04cf-4f11-87-93-a8-d1-cd-e9-96-9f')
    @commethod(3)
    def Realize() -> Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationWindowPattern(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0faef453-9208-43ef-bb-b2-3b-48-51-77-86-4f')
    @commethod(3)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WaitForInputIdle(milliseconds: Int32, success: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetWindowVisualState(state: Windows.Win32.UI.Accessibility.WindowVisualState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentCanMaximize(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentCanMinimize(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentIsModal(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentIsTopmost(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentWindowVisualState(retVal: POINTER(Windows.Win32.UI.Accessibility.WindowVisualState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CurrentWindowInteractionState(retVal: POINTER(Windows.Win32.UI.Accessibility.WindowInteractionState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CachedCanMaximize(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_CachedCanMinimize(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CachedIsModal(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CachedIsTopmost(retVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CachedWindowVisualState(retVal: POINTER(Windows.Win32.UI.Accessibility.WindowVisualState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_CachedWindowInteractionState(retVal: POINTER(Windows.Win32.UI.Accessibility.WindowInteractionState)) -> Windows.Win32.Foundation.HRESULT: ...
class IValueProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c7935180-6fb3-4201-b1-74-7d-f7-3a-db-f6-4a')
    @commethod(3)
    def SetValue(val: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Value(pRetVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_IsReadOnly(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IVirtualizedItemProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cb98b665-2d35-4fac-ad-35-f3-c6-0d-0c-0b-8b')
    @commethod(3)
    def Realize() -> Windows.Win32.Foundation.HRESULT: ...
class IWindowProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('987df77b-db06-4d77-8f-8a-86-a9-c3-bb-90-b9')
    @commethod(3)
    def SetVisualState(state: Windows.Win32.UI.Accessibility.WindowVisualState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WaitForInputIdle(milliseconds: Int32, pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CanMaximize(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CanMinimize(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IsModal(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_WindowVisualState(pRetVal: POINTER(Windows.Win32.UI.Accessibility.WindowVisualState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_WindowInteractionState(pRetVal: POINTER(Windows.Win32.UI.Accessibility.WindowInteractionState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsTopmost(pRetVal: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNACCESSIBLECHILDREN(paccContainer: Windows.Win32.UI.Accessibility.IAccessible_head, iChildStart: Int32, cChildren: Int32, rgvarChildren: POINTER(Windows.Win32.System.Com.VARIANT_head), pcObtained: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNACCESSIBLEOBJECTFROMPOINT(ptScreen: Windows.Win32.Foundation.POINT, ppacc: POINTER(Windows.Win32.UI.Accessibility.IAccessible_head), pvarChild: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNACCESSIBLEOBJECTFROMWINDOW(hwnd: Windows.Win32.Foundation.HWND, dwId: UInt32, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNCREATESTDACCESSIBLEOBJECT(hwnd: Windows.Win32.Foundation.HWND, idObject: Int32, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNLRESULTFROMOBJECT(riid: POINTER(Guid), wParam: Windows.Win32.Foundation.WPARAM, punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype_pointer
def LPFNOBJECTFROMLRESULT(lResult: Windows.Win32.Foundation.LRESULT, riid: POINTER(Guid), wParam: Windows.Win32.Foundation.WPARAM, ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
LiveSetting = Int32
LiveSetting_Off: LiveSetting = 0
LiveSetting_Polite: LiveSetting = 1
LiveSetting_Assertive: LiveSetting = 2
class MOUSEKEYS(Structure):
    cbSize: UInt32
    dwFlags: UInt32
    iMaxSpeed: UInt32
    iTimeToMaxSpeed: UInt32
    iCtrlSpeed: UInt32
    dwReserved1: UInt32
    dwReserved2: UInt32
class MSAAMENUINFO(Structure):
    dwMSAASignature: UInt32
    cchWText: UInt32
    pszWText: Windows.Win32.Foundation.PWSTR
NavigateDirection = Int32
NavigateDirection_Parent: NavigateDirection = 0
NavigateDirection_NextSibling: NavigateDirection = 1
NavigateDirection_PreviousSibling: NavigateDirection = 2
NavigateDirection_FirstChild: NavigateDirection = 3
NavigateDirection_LastChild: NavigateDirection = 4
NormalizeState = Int32
NormalizeState_None: NormalizeState = 0
NormalizeState_View: NormalizeState = 1
NormalizeState_Custom: NormalizeState = 2
NotificationKind = Int32
NotificationKind_ItemAdded: NotificationKind = 0
NotificationKind_ItemRemoved: NotificationKind = 1
NotificationKind_ActionCompleted: NotificationKind = 2
NotificationKind_ActionAborted: NotificationKind = 3
NotificationKind_Other: NotificationKind = 4
NotificationProcessing = Int32
NotificationProcessing_ImportantAll: NotificationProcessing = 0
NotificationProcessing_ImportantMostRecent: NotificationProcessing = 1
NotificationProcessing_All: NotificationProcessing = 2
NotificationProcessing_MostRecent: NotificationProcessing = 3
NotificationProcessing_CurrentThenMostRecent: NotificationProcessing = 4
OrientationType = Int32
OrientationType_None: OrientationType = 0
OrientationType_Horizontal: OrientationType = 1
OrientationType_Vertical: OrientationType = 2
OutlineStyles = Int32
OutlineStyles_None: OutlineStyles = 0
OutlineStyles_Outline: OutlineStyles = 1
OutlineStyles_Shadow: OutlineStyles = 2
OutlineStyles_Engraved: OutlineStyles = 4
OutlineStyles_Embossed: OutlineStyles = 8
PropertyConditionFlags = Int32
PropertyConditionFlags_None: PropertyConditionFlags = 0
PropertyConditionFlags_IgnoreCase: PropertyConditionFlags = 1
PropertyConditionFlags_MatchSubstring: PropertyConditionFlags = 2
ProviderOptions = Int32
ProviderOptions_ClientSideProvider: ProviderOptions = 1
ProviderOptions_ServerSideProvider: ProviderOptions = 2
ProviderOptions_NonClientAreaProvider: ProviderOptions = 4
ProviderOptions_OverrideProvider: ProviderOptions = 8
ProviderOptions_ProviderOwnsSetFocus: ProviderOptions = 16
ProviderOptions_UseComThreading: ProviderOptions = 32
ProviderOptions_RefuseNonClientSupport: ProviderOptions = 64
ProviderOptions_HasNativeIAccessible: ProviderOptions = 128
ProviderOptions_UseClientCoordinates: ProviderOptions = 256
ProviderType = Int32
ProviderType_BaseHwnd: ProviderType = 0
ProviderType_Proxy: ProviderType = 1
ProviderType_NonClientArea: ProviderType = 2
RowOrColumnMajor = Int32
RowOrColumnMajor_RowMajor: RowOrColumnMajor = 0
RowOrColumnMajor_ColumnMajor: RowOrColumnMajor = 1
RowOrColumnMajor_Indeterminate: RowOrColumnMajor = 2
class SERIALKEYSA(Structure):
    cbSize: UInt32
    dwFlags: Windows.Win32.UI.Accessibility.SERIALKEYS_FLAGS
    lpszActivePort: Windows.Win32.Foundation.PSTR
    lpszPort: Windows.Win32.Foundation.PSTR
    iBaudRate: UInt32
    iPortState: UInt32
    iActive: UInt32
class SERIALKEYSW(Structure):
    cbSize: UInt32
    dwFlags: Windows.Win32.UI.Accessibility.SERIALKEYS_FLAGS
    lpszActivePort: Windows.Win32.Foundation.PWSTR
    lpszPort: Windows.Win32.Foundation.PWSTR
    iBaudRate: UInt32
    iPortState: UInt32
    iActive: UInt32
SERIALKEYS_FLAGS = UInt32
SERKF_AVAILABLE: SERIALKEYS_FLAGS = 2
SERKF_INDICATOR: SERIALKEYS_FLAGS = 4
SERKF_SERIALKEYSON: SERIALKEYS_FLAGS = 1
class SOUNDSENTRYA(Structure):
    cbSize: UInt32
    dwFlags: Windows.Win32.UI.Accessibility.SOUNDSENTRY_FLAGS
    iFSTextEffect: Windows.Win32.UI.Accessibility.SOUNDSENTRY_TEXT_EFFECT
    iFSTextEffectMSec: UInt32
    iFSTextEffectColorBits: UInt32
    iFSGrafEffect: Windows.Win32.UI.Accessibility.SOUND_SENTRY_GRAPHICS_EFFECT
    iFSGrafEffectMSec: UInt32
    iFSGrafEffectColor: UInt32
    iWindowsEffect: Windows.Win32.UI.Accessibility.SOUNDSENTRY_WINDOWS_EFFECT
    iWindowsEffectMSec: UInt32
    lpszWindowsEffectDLL: Windows.Win32.Foundation.PSTR
    iWindowsEffectOrdinal: UInt32
class SOUNDSENTRYW(Structure):
    cbSize: UInt32
    dwFlags: Windows.Win32.UI.Accessibility.SOUNDSENTRY_FLAGS
    iFSTextEffect: Windows.Win32.UI.Accessibility.SOUNDSENTRY_TEXT_EFFECT
    iFSTextEffectMSec: UInt32
    iFSTextEffectColorBits: UInt32
    iFSGrafEffect: Windows.Win32.UI.Accessibility.SOUND_SENTRY_GRAPHICS_EFFECT
    iFSGrafEffectMSec: UInt32
    iFSGrafEffectColor: UInt32
    iWindowsEffect: Windows.Win32.UI.Accessibility.SOUNDSENTRY_WINDOWS_EFFECT
    iWindowsEffectMSec: UInt32
    lpszWindowsEffectDLL: Windows.Win32.Foundation.PWSTR
    iWindowsEffectOrdinal: UInt32
SOUNDSENTRY_FLAGS = UInt32
SSF_SOUNDSENTRYON: SOUNDSENTRY_FLAGS = 1
SSF_AVAILABLE: SOUNDSENTRY_FLAGS = 2
SSF_INDICATOR: SOUNDSENTRY_FLAGS = 4
SOUNDSENTRY_TEXT_EFFECT = UInt32
SSTF_BORDER: SOUNDSENTRY_TEXT_EFFECT = 2
SSTF_CHARS: SOUNDSENTRY_TEXT_EFFECT = 1
SSTF_DISPLAY: SOUNDSENTRY_TEXT_EFFECT = 3
SSTF_NONE: SOUNDSENTRY_TEXT_EFFECT = 0
SOUNDSENTRY_WINDOWS_EFFECT = UInt32
SSWF_CUSTOM: SOUNDSENTRY_WINDOWS_EFFECT = 4
SSWF_DISPLAY: SOUNDSENTRY_WINDOWS_EFFECT = 3
SSWF_NONE: SOUNDSENTRY_WINDOWS_EFFECT = 0
SSWF_TITLE: SOUNDSENTRY_WINDOWS_EFFECT = 1
SSWF_WINDOW: SOUNDSENTRY_WINDOWS_EFFECT = 2
SOUND_SENTRY_GRAPHICS_EFFECT = UInt32
SSGF_DISPLAY: SOUND_SENTRY_GRAPHICS_EFFECT = 3
SSGF_NONE: SOUND_SENTRY_GRAPHICS_EFFECT = 0
class STICKYKEYS(Structure):
    cbSize: UInt32
    dwFlags: Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS
STICKYKEYS_FLAGS = UInt32
SKF_STICKYKEYSON: STICKYKEYS_FLAGS = 1
SKF_AVAILABLE: STICKYKEYS_FLAGS = 2
SKF_HOTKEYACTIVE: STICKYKEYS_FLAGS = 4
SKF_CONFIRMHOTKEY: STICKYKEYS_FLAGS = 8
SKF_HOTKEYSOUND: STICKYKEYS_FLAGS = 16
SKF_INDICATOR: STICKYKEYS_FLAGS = 32
SKF_AUDIBLEFEEDBACK: STICKYKEYS_FLAGS = 64
SKF_TRISTATE: STICKYKEYS_FLAGS = 128
SKF_TWOKEYSOFF: STICKYKEYS_FLAGS = 256
SKF_LALTLATCHED: STICKYKEYS_FLAGS = 268435456
SKF_LCTLLATCHED: STICKYKEYS_FLAGS = 67108864
SKF_LSHIFTLATCHED: STICKYKEYS_FLAGS = 16777216
SKF_RALTLATCHED: STICKYKEYS_FLAGS = 536870912
SKF_RCTLLATCHED: STICKYKEYS_FLAGS = 134217728
SKF_RSHIFTLATCHED: STICKYKEYS_FLAGS = 33554432
SKF_LWINLATCHED: STICKYKEYS_FLAGS = 1073741824
SKF_RWINLATCHED: STICKYKEYS_FLAGS = 2147483648
SKF_LALTLOCKED: STICKYKEYS_FLAGS = 1048576
SKF_LCTLLOCKED: STICKYKEYS_FLAGS = 262144
SKF_LSHIFTLOCKED: STICKYKEYS_FLAGS = 65536
SKF_RALTLOCKED: STICKYKEYS_FLAGS = 2097152
SKF_RCTLLOCKED: STICKYKEYS_FLAGS = 524288
SKF_RSHIFTLOCKED: STICKYKEYS_FLAGS = 131072
SKF_LWINLOCKED: STICKYKEYS_FLAGS = 4194304
SKF_RWINLOCKED: STICKYKEYS_FLAGS = 8388608
SayAsInterpretAs = Int32
SayAsInterpretAs_None: SayAsInterpretAs = 0
SayAsInterpretAs_Spell: SayAsInterpretAs = 1
SayAsInterpretAs_Cardinal: SayAsInterpretAs = 2
SayAsInterpretAs_Ordinal: SayAsInterpretAs = 3
SayAsInterpretAs_Number: SayAsInterpretAs = 4
SayAsInterpretAs_Date: SayAsInterpretAs = 5
SayAsInterpretAs_Time: SayAsInterpretAs = 6
SayAsInterpretAs_Telephone: SayAsInterpretAs = 7
SayAsInterpretAs_Currency: SayAsInterpretAs = 8
SayAsInterpretAs_Net: SayAsInterpretAs = 9
SayAsInterpretAs_Url: SayAsInterpretAs = 10
SayAsInterpretAs_Address: SayAsInterpretAs = 11
SayAsInterpretAs_Alphanumeric: SayAsInterpretAs = 12
SayAsInterpretAs_Name: SayAsInterpretAs = 13
SayAsInterpretAs_Media: SayAsInterpretAs = 14
SayAsInterpretAs_Date_MonthDayYear: SayAsInterpretAs = 15
SayAsInterpretAs_Date_DayMonthYear: SayAsInterpretAs = 16
SayAsInterpretAs_Date_YearMonthDay: SayAsInterpretAs = 17
SayAsInterpretAs_Date_YearMonth: SayAsInterpretAs = 18
SayAsInterpretAs_Date_MonthYear: SayAsInterpretAs = 19
SayAsInterpretAs_Date_DayMonth: SayAsInterpretAs = 20
SayAsInterpretAs_Date_MonthDay: SayAsInterpretAs = 21
SayAsInterpretAs_Date_Year: SayAsInterpretAs = 22
SayAsInterpretAs_Time_HoursMinutesSeconds12: SayAsInterpretAs = 23
SayAsInterpretAs_Time_HoursMinutes12: SayAsInterpretAs = 24
SayAsInterpretAs_Time_HoursMinutesSeconds24: SayAsInterpretAs = 25
SayAsInterpretAs_Time_HoursMinutes24: SayAsInterpretAs = 26
ScrollAmount = Int32
ScrollAmount_LargeDecrement: ScrollAmount = 0
ScrollAmount_SmallDecrement: ScrollAmount = 1
ScrollAmount_NoAmount: ScrollAmount = 2
ScrollAmount_LargeIncrement: ScrollAmount = 3
ScrollAmount_SmallIncrement: ScrollAmount = 4
StructureChangeType = Int32
StructureChangeType_ChildAdded: StructureChangeType = 0
StructureChangeType_ChildRemoved: StructureChangeType = 1
StructureChangeType_ChildrenInvalidated: StructureChangeType = 2
StructureChangeType_ChildrenBulkAdded: StructureChangeType = 3
StructureChangeType_ChildrenBulkRemoved: StructureChangeType = 4
StructureChangeType_ChildrenReordered: StructureChangeType = 5
SupportedTextSelection = Int32
SupportedTextSelection_None: SupportedTextSelection = 0
SupportedTextSelection_Single: SupportedTextSelection = 1
SupportedTextSelection_Multiple: SupportedTextSelection = 2
SynchronizedInputType = Int32
SynchronizedInputType_KeyUp: SynchronizedInputType = 1
SynchronizedInputType_KeyDown: SynchronizedInputType = 2
SynchronizedInputType_LeftMouseUp: SynchronizedInputType = 4
SynchronizedInputType_LeftMouseDown: SynchronizedInputType = 8
SynchronizedInputType_RightMouseUp: SynchronizedInputType = 16
SynchronizedInputType_RightMouseDown: SynchronizedInputType = 32
class TOGGLEKEYS(Structure):
    cbSize: UInt32
    dwFlags: UInt32
TextDecorationLineStyle = Int32
TextDecorationLineStyle_None: TextDecorationLineStyle = 0
TextDecorationLineStyle_Single: TextDecorationLineStyle = 1
TextDecorationLineStyle_WordsOnly: TextDecorationLineStyle = 2
TextDecorationLineStyle_Double: TextDecorationLineStyle = 3
TextDecorationLineStyle_Dot: TextDecorationLineStyle = 4
TextDecorationLineStyle_Dash: TextDecorationLineStyle = 5
TextDecorationLineStyle_DashDot: TextDecorationLineStyle = 6
TextDecorationLineStyle_DashDotDot: TextDecorationLineStyle = 7
TextDecorationLineStyle_Wavy: TextDecorationLineStyle = 8
TextDecorationLineStyle_ThickSingle: TextDecorationLineStyle = 9
TextDecorationLineStyle_DoubleWavy: TextDecorationLineStyle = 11
TextDecorationLineStyle_ThickWavy: TextDecorationLineStyle = 12
TextDecorationLineStyle_LongDash: TextDecorationLineStyle = 13
TextDecorationLineStyle_ThickDash: TextDecorationLineStyle = 14
TextDecorationLineStyle_ThickDashDot: TextDecorationLineStyle = 15
TextDecorationLineStyle_ThickDashDotDot: TextDecorationLineStyle = 16
TextDecorationLineStyle_ThickDot: TextDecorationLineStyle = 17
TextDecorationLineStyle_ThickLongDash: TextDecorationLineStyle = 18
TextDecorationLineStyle_Other: TextDecorationLineStyle = -1
TextEditChangeType = Int32
TextEditChangeType_None: TextEditChangeType = 0
TextEditChangeType_AutoCorrect: TextEditChangeType = 1
TextEditChangeType_Composition: TextEditChangeType = 2
TextEditChangeType_CompositionFinalized: TextEditChangeType = 3
TextEditChangeType_AutoComplete: TextEditChangeType = 4
TextPatternRangeEndpoint = Int32
TextPatternRangeEndpoint_Start: TextPatternRangeEndpoint = 0
TextPatternRangeEndpoint_End: TextPatternRangeEndpoint = 1
TextUnit = Int32
TextUnit_Character: TextUnit = 0
TextUnit_Format: TextUnit = 1
TextUnit_Word: TextUnit = 2
TextUnit_Line: TextUnit = 3
TextUnit_Paragraph: TextUnit = 4
TextUnit_Page: TextUnit = 5
TextUnit_Document: TextUnit = 6
ToggleState = Int32
ToggleState_Off: ToggleState = 0
ToggleState_On: ToggleState = 1
ToggleState_Indeterminate: ToggleState = 2
TreeScope = Int32
TreeScope_None: TreeScope = 0
TreeScope_Element: TreeScope = 1
TreeScope_Children: TreeScope = 2
TreeScope_Descendants: TreeScope = 4
TreeScope_Parent: TreeScope = 8
TreeScope_Ancestors: TreeScope = 16
TreeScope_Subtree: TreeScope = 7
TreeTraversalOptions = Int32
TreeTraversalOptions_Default: TreeTraversalOptions = 0
TreeTraversalOptions_PostOrder: TreeTraversalOptions = 1
TreeTraversalOptions_LastToFirstOrder: TreeTraversalOptions = 2
UIA_ANNOTATIONTYPE = UInt32
AnnotationType_Unknown: UIA_ANNOTATIONTYPE = 60000
AnnotationType_SpellingError: UIA_ANNOTATIONTYPE = 60001
AnnotationType_GrammarError: UIA_ANNOTATIONTYPE = 60002
AnnotationType_Comment: UIA_ANNOTATIONTYPE = 60003
AnnotationType_FormulaError: UIA_ANNOTATIONTYPE = 60004
AnnotationType_TrackChanges: UIA_ANNOTATIONTYPE = 60005
AnnotationType_Header: UIA_ANNOTATIONTYPE = 60006
AnnotationType_Footer: UIA_ANNOTATIONTYPE = 60007
AnnotationType_Highlighted: UIA_ANNOTATIONTYPE = 60008
AnnotationType_Endnote: UIA_ANNOTATIONTYPE = 60009
AnnotationType_Footnote: UIA_ANNOTATIONTYPE = 60010
AnnotationType_InsertionChange: UIA_ANNOTATIONTYPE = 60011
AnnotationType_DeletionChange: UIA_ANNOTATIONTYPE = 60012
AnnotationType_MoveChange: UIA_ANNOTATIONTYPE = 60013
AnnotationType_FormatChange: UIA_ANNOTATIONTYPE = 60014
AnnotationType_UnsyncedChange: UIA_ANNOTATIONTYPE = 60015
AnnotationType_EditingLockedChange: UIA_ANNOTATIONTYPE = 60016
AnnotationType_ExternalChange: UIA_ANNOTATIONTYPE = 60017
AnnotationType_ConflictingChange: UIA_ANNOTATIONTYPE = 60018
AnnotationType_Author: UIA_ANNOTATIONTYPE = 60019
AnnotationType_AdvancedProofingIssue: UIA_ANNOTATIONTYPE = 60020
AnnotationType_DataValidationError: UIA_ANNOTATIONTYPE = 60021
AnnotationType_CircularReferenceError: UIA_ANNOTATIONTYPE = 60022
AnnotationType_Mathematics: UIA_ANNOTATIONTYPE = 60023
AnnotationType_Sensitive: UIA_ANNOTATIONTYPE = 60024
UIA_CHANGE_ID = UInt32
UIA_SummaryChangeId: UIA_CHANGE_ID = 90000
UIA_CONTROLTYPE_ID = UInt32
UIA_ButtonControlTypeId: UIA_CONTROLTYPE_ID = 50000
UIA_CalendarControlTypeId: UIA_CONTROLTYPE_ID = 50001
UIA_CheckBoxControlTypeId: UIA_CONTROLTYPE_ID = 50002
UIA_ComboBoxControlTypeId: UIA_CONTROLTYPE_ID = 50003
UIA_EditControlTypeId: UIA_CONTROLTYPE_ID = 50004
UIA_HyperlinkControlTypeId: UIA_CONTROLTYPE_ID = 50005
UIA_ImageControlTypeId: UIA_CONTROLTYPE_ID = 50006
UIA_ListItemControlTypeId: UIA_CONTROLTYPE_ID = 50007
UIA_ListControlTypeId: UIA_CONTROLTYPE_ID = 50008
UIA_MenuControlTypeId: UIA_CONTROLTYPE_ID = 50009
UIA_MenuBarControlTypeId: UIA_CONTROLTYPE_ID = 50010
UIA_MenuItemControlTypeId: UIA_CONTROLTYPE_ID = 50011
UIA_ProgressBarControlTypeId: UIA_CONTROLTYPE_ID = 50012
UIA_RadioButtonControlTypeId: UIA_CONTROLTYPE_ID = 50013
UIA_ScrollBarControlTypeId: UIA_CONTROLTYPE_ID = 50014
UIA_SliderControlTypeId: UIA_CONTROLTYPE_ID = 50015
UIA_SpinnerControlTypeId: UIA_CONTROLTYPE_ID = 50016
UIA_StatusBarControlTypeId: UIA_CONTROLTYPE_ID = 50017
UIA_TabControlTypeId: UIA_CONTROLTYPE_ID = 50018
UIA_TabItemControlTypeId: UIA_CONTROLTYPE_ID = 50019
UIA_TextControlTypeId: UIA_CONTROLTYPE_ID = 50020
UIA_ToolBarControlTypeId: UIA_CONTROLTYPE_ID = 50021
UIA_ToolTipControlTypeId: UIA_CONTROLTYPE_ID = 50022
UIA_TreeControlTypeId: UIA_CONTROLTYPE_ID = 50023
UIA_TreeItemControlTypeId: UIA_CONTROLTYPE_ID = 50024
UIA_CustomControlTypeId: UIA_CONTROLTYPE_ID = 50025
UIA_GroupControlTypeId: UIA_CONTROLTYPE_ID = 50026
UIA_ThumbControlTypeId: UIA_CONTROLTYPE_ID = 50027
UIA_DataGridControlTypeId: UIA_CONTROLTYPE_ID = 50028
UIA_DataItemControlTypeId: UIA_CONTROLTYPE_ID = 50029
UIA_DocumentControlTypeId: UIA_CONTROLTYPE_ID = 50030
UIA_SplitButtonControlTypeId: UIA_CONTROLTYPE_ID = 50031
UIA_WindowControlTypeId: UIA_CONTROLTYPE_ID = 50032
UIA_PaneControlTypeId: UIA_CONTROLTYPE_ID = 50033
UIA_HeaderControlTypeId: UIA_CONTROLTYPE_ID = 50034
UIA_HeaderItemControlTypeId: UIA_CONTROLTYPE_ID = 50035
UIA_TableControlTypeId: UIA_CONTROLTYPE_ID = 50036
UIA_TitleBarControlTypeId: UIA_CONTROLTYPE_ID = 50037
UIA_SeparatorControlTypeId: UIA_CONTROLTYPE_ID = 50038
UIA_SemanticZoomControlTypeId: UIA_CONTROLTYPE_ID = 50039
UIA_AppBarControlTypeId: UIA_CONTROLTYPE_ID = 50040
UIA_EVENT_ID = UInt32
UIA_ToolTipOpenedEventId: UIA_EVENT_ID = 20000
UIA_ToolTipClosedEventId: UIA_EVENT_ID = 20001
UIA_StructureChangedEventId: UIA_EVENT_ID = 20002
UIA_MenuOpenedEventId: UIA_EVENT_ID = 20003
UIA_AutomationPropertyChangedEventId: UIA_EVENT_ID = 20004
UIA_AutomationFocusChangedEventId: UIA_EVENT_ID = 20005
UIA_AsyncContentLoadedEventId: UIA_EVENT_ID = 20006
UIA_MenuClosedEventId: UIA_EVENT_ID = 20007
UIA_LayoutInvalidatedEventId: UIA_EVENT_ID = 20008
UIA_Invoke_InvokedEventId: UIA_EVENT_ID = 20009
UIA_SelectionItem_ElementAddedToSelectionEventId: UIA_EVENT_ID = 20010
UIA_SelectionItem_ElementRemovedFromSelectionEventId: UIA_EVENT_ID = 20011
UIA_SelectionItem_ElementSelectedEventId: UIA_EVENT_ID = 20012
UIA_Selection_InvalidatedEventId: UIA_EVENT_ID = 20013
UIA_Text_TextSelectionChangedEventId: UIA_EVENT_ID = 20014
UIA_Text_TextChangedEventId: UIA_EVENT_ID = 20015
UIA_Window_WindowOpenedEventId: UIA_EVENT_ID = 20016
UIA_Window_WindowClosedEventId: UIA_EVENT_ID = 20017
UIA_MenuModeStartEventId: UIA_EVENT_ID = 20018
UIA_MenuModeEndEventId: UIA_EVENT_ID = 20019
UIA_InputReachedTargetEventId: UIA_EVENT_ID = 20020
UIA_InputReachedOtherElementEventId: UIA_EVENT_ID = 20021
UIA_InputDiscardedEventId: UIA_EVENT_ID = 20022
UIA_SystemAlertEventId: UIA_EVENT_ID = 20023
UIA_LiveRegionChangedEventId: UIA_EVENT_ID = 20024
UIA_HostedFragmentRootsInvalidatedEventId: UIA_EVENT_ID = 20025
UIA_Drag_DragStartEventId: UIA_EVENT_ID = 20026
UIA_Drag_DragCancelEventId: UIA_EVENT_ID = 20027
UIA_Drag_DragCompleteEventId: UIA_EVENT_ID = 20028
UIA_DropTarget_DragEnterEventId: UIA_EVENT_ID = 20029
UIA_DropTarget_DragLeaveEventId: UIA_EVENT_ID = 20030
UIA_DropTarget_DroppedEventId: UIA_EVENT_ID = 20031
UIA_TextEdit_TextChangedEventId: UIA_EVENT_ID = 20032
UIA_TextEdit_ConversionTargetChangedEventId: UIA_EVENT_ID = 20033
UIA_ChangesEventId: UIA_EVENT_ID = 20034
UIA_NotificationEventId: UIA_EVENT_ID = 20035
UIA_ActiveTextPositionChangedEventId: UIA_EVENT_ID = 20036
UIA_HEADINGLEVEL_ID = UInt32
UIA_HEADINGLEVEL_ID_HeadingLevel_None: UIA_HEADINGLEVEL_ID = 80050
UIA_HEADINGLEVEL_ID_HeadingLevel1: UIA_HEADINGLEVEL_ID = 80051
UIA_HEADINGLEVEL_ID_HeadingLevel2: UIA_HEADINGLEVEL_ID = 80052
UIA_HEADINGLEVEL_ID_HeadingLevel3: UIA_HEADINGLEVEL_ID = 80053
UIA_HEADINGLEVEL_ID_HeadingLevel4: UIA_HEADINGLEVEL_ID = 80054
UIA_HEADINGLEVEL_ID_HeadingLevel5: UIA_HEADINGLEVEL_ID = 80055
UIA_HEADINGLEVEL_ID_HeadingLevel6: UIA_HEADINGLEVEL_ID = 80056
UIA_HEADINGLEVEL_ID_HeadingLevel7: UIA_HEADINGLEVEL_ID = 80057
UIA_HEADINGLEVEL_ID_HeadingLevel8: UIA_HEADINGLEVEL_ID = 80058
UIA_HEADINGLEVEL_ID_HeadingLevel9: UIA_HEADINGLEVEL_ID = 80059
UIA_LANDMARKTYPE_ID = UInt32
UIA_CustomLandmarkTypeId: UIA_LANDMARKTYPE_ID = 80000
UIA_FormLandmarkTypeId: UIA_LANDMARKTYPE_ID = 80001
UIA_MainLandmarkTypeId: UIA_LANDMARKTYPE_ID = 80002
UIA_NavigationLandmarkTypeId: UIA_LANDMARKTYPE_ID = 80003
UIA_SearchLandmarkTypeId: UIA_LANDMARKTYPE_ID = 80004
UIA_METADATA_ID = UInt32
UIA_SayAsInterpretAsMetadataId: UIA_METADATA_ID = 100000
UIA_PATTERN_ID = UInt32
UIA_InvokePatternId: UIA_PATTERN_ID = 10000
UIA_SelectionPatternId: UIA_PATTERN_ID = 10001
UIA_ValuePatternId: UIA_PATTERN_ID = 10002
UIA_RangeValuePatternId: UIA_PATTERN_ID = 10003
UIA_ScrollPatternId: UIA_PATTERN_ID = 10004
UIA_ExpandCollapsePatternId: UIA_PATTERN_ID = 10005
UIA_GridPatternId: UIA_PATTERN_ID = 10006
UIA_GridItemPatternId: UIA_PATTERN_ID = 10007
UIA_MultipleViewPatternId: UIA_PATTERN_ID = 10008
UIA_WindowPatternId: UIA_PATTERN_ID = 10009
UIA_SelectionItemPatternId: UIA_PATTERN_ID = 10010
UIA_DockPatternId: UIA_PATTERN_ID = 10011
UIA_TablePatternId: UIA_PATTERN_ID = 10012
UIA_TableItemPatternId: UIA_PATTERN_ID = 10013
UIA_TextPatternId: UIA_PATTERN_ID = 10014
UIA_TogglePatternId: UIA_PATTERN_ID = 10015
UIA_TransformPatternId: UIA_PATTERN_ID = 10016
UIA_ScrollItemPatternId: UIA_PATTERN_ID = 10017
UIA_LegacyIAccessiblePatternId: UIA_PATTERN_ID = 10018
UIA_ItemContainerPatternId: UIA_PATTERN_ID = 10019
UIA_VirtualizedItemPatternId: UIA_PATTERN_ID = 10020
UIA_SynchronizedInputPatternId: UIA_PATTERN_ID = 10021
UIA_ObjectModelPatternId: UIA_PATTERN_ID = 10022
UIA_AnnotationPatternId: UIA_PATTERN_ID = 10023
UIA_TextPattern2Id: UIA_PATTERN_ID = 10024
UIA_StylesPatternId: UIA_PATTERN_ID = 10025
UIA_SpreadsheetPatternId: UIA_PATTERN_ID = 10026
UIA_SpreadsheetItemPatternId: UIA_PATTERN_ID = 10027
UIA_TransformPattern2Id: UIA_PATTERN_ID = 10028
UIA_TextChildPatternId: UIA_PATTERN_ID = 10029
UIA_DragPatternId: UIA_PATTERN_ID = 10030
UIA_DropTargetPatternId: UIA_PATTERN_ID = 10031
UIA_TextEditPatternId: UIA_PATTERN_ID = 10032
UIA_CustomNavigationPatternId: UIA_PATTERN_ID = 10033
UIA_SelectionPattern2Id: UIA_PATTERN_ID = 10034
UIA_PROPERTY_ID = UInt32
UIA_RuntimeIdPropertyId: UIA_PROPERTY_ID = 30000
UIA_BoundingRectanglePropertyId: UIA_PROPERTY_ID = 30001
UIA_ProcessIdPropertyId: UIA_PROPERTY_ID = 30002
UIA_ControlTypePropertyId: UIA_PROPERTY_ID = 30003
UIA_LocalizedControlTypePropertyId: UIA_PROPERTY_ID = 30004
UIA_NamePropertyId: UIA_PROPERTY_ID = 30005
UIA_AcceleratorKeyPropertyId: UIA_PROPERTY_ID = 30006
UIA_AccessKeyPropertyId: UIA_PROPERTY_ID = 30007
UIA_HasKeyboardFocusPropertyId: UIA_PROPERTY_ID = 30008
UIA_IsKeyboardFocusablePropertyId: UIA_PROPERTY_ID = 30009
UIA_IsEnabledPropertyId: UIA_PROPERTY_ID = 30010
UIA_AutomationIdPropertyId: UIA_PROPERTY_ID = 30011
UIA_ClassNamePropertyId: UIA_PROPERTY_ID = 30012
UIA_HelpTextPropertyId: UIA_PROPERTY_ID = 30013
UIA_ClickablePointPropertyId: UIA_PROPERTY_ID = 30014
UIA_CulturePropertyId: UIA_PROPERTY_ID = 30015
UIA_IsControlElementPropertyId: UIA_PROPERTY_ID = 30016
UIA_IsContentElementPropertyId: UIA_PROPERTY_ID = 30017
UIA_LabeledByPropertyId: UIA_PROPERTY_ID = 30018
UIA_IsPasswordPropertyId: UIA_PROPERTY_ID = 30019
UIA_NativeWindowHandlePropertyId: UIA_PROPERTY_ID = 30020
UIA_ItemTypePropertyId: UIA_PROPERTY_ID = 30021
UIA_IsOffscreenPropertyId: UIA_PROPERTY_ID = 30022
UIA_OrientationPropertyId: UIA_PROPERTY_ID = 30023
UIA_FrameworkIdPropertyId: UIA_PROPERTY_ID = 30024
UIA_IsRequiredForFormPropertyId: UIA_PROPERTY_ID = 30025
UIA_ItemStatusPropertyId: UIA_PROPERTY_ID = 30026
UIA_IsDockPatternAvailablePropertyId: UIA_PROPERTY_ID = 30027
UIA_IsExpandCollapsePatternAvailablePropertyId: UIA_PROPERTY_ID = 30028
UIA_IsGridItemPatternAvailablePropertyId: UIA_PROPERTY_ID = 30029
UIA_IsGridPatternAvailablePropertyId: UIA_PROPERTY_ID = 30030
UIA_IsInvokePatternAvailablePropertyId: UIA_PROPERTY_ID = 30031
UIA_IsMultipleViewPatternAvailablePropertyId: UIA_PROPERTY_ID = 30032
UIA_IsRangeValuePatternAvailablePropertyId: UIA_PROPERTY_ID = 30033
UIA_IsScrollPatternAvailablePropertyId: UIA_PROPERTY_ID = 30034
UIA_IsScrollItemPatternAvailablePropertyId: UIA_PROPERTY_ID = 30035
UIA_IsSelectionItemPatternAvailablePropertyId: UIA_PROPERTY_ID = 30036
UIA_IsSelectionPatternAvailablePropertyId: UIA_PROPERTY_ID = 30037
UIA_IsTablePatternAvailablePropertyId: UIA_PROPERTY_ID = 30038
UIA_IsTableItemPatternAvailablePropertyId: UIA_PROPERTY_ID = 30039
UIA_IsTextPatternAvailablePropertyId: UIA_PROPERTY_ID = 30040
UIA_IsTogglePatternAvailablePropertyId: UIA_PROPERTY_ID = 30041
UIA_IsTransformPatternAvailablePropertyId: UIA_PROPERTY_ID = 30042
UIA_IsValuePatternAvailablePropertyId: UIA_PROPERTY_ID = 30043
UIA_IsWindowPatternAvailablePropertyId: UIA_PROPERTY_ID = 30044
UIA_ValueValuePropertyId: UIA_PROPERTY_ID = 30045
UIA_ValueIsReadOnlyPropertyId: UIA_PROPERTY_ID = 30046
UIA_RangeValueValuePropertyId: UIA_PROPERTY_ID = 30047
UIA_RangeValueIsReadOnlyPropertyId: UIA_PROPERTY_ID = 30048
UIA_RangeValueMinimumPropertyId: UIA_PROPERTY_ID = 30049
UIA_RangeValueMaximumPropertyId: UIA_PROPERTY_ID = 30050
UIA_RangeValueLargeChangePropertyId: UIA_PROPERTY_ID = 30051
UIA_RangeValueSmallChangePropertyId: UIA_PROPERTY_ID = 30052
UIA_ScrollHorizontalScrollPercentPropertyId: UIA_PROPERTY_ID = 30053
UIA_ScrollHorizontalViewSizePropertyId: UIA_PROPERTY_ID = 30054
UIA_ScrollVerticalScrollPercentPropertyId: UIA_PROPERTY_ID = 30055
UIA_ScrollVerticalViewSizePropertyId: UIA_PROPERTY_ID = 30056
UIA_ScrollHorizontallyScrollablePropertyId: UIA_PROPERTY_ID = 30057
UIA_ScrollVerticallyScrollablePropertyId: UIA_PROPERTY_ID = 30058
UIA_SelectionSelectionPropertyId: UIA_PROPERTY_ID = 30059
UIA_SelectionCanSelectMultiplePropertyId: UIA_PROPERTY_ID = 30060
UIA_SelectionIsSelectionRequiredPropertyId: UIA_PROPERTY_ID = 30061
UIA_GridRowCountPropertyId: UIA_PROPERTY_ID = 30062
UIA_GridColumnCountPropertyId: UIA_PROPERTY_ID = 30063
UIA_GridItemRowPropertyId: UIA_PROPERTY_ID = 30064
UIA_GridItemColumnPropertyId: UIA_PROPERTY_ID = 30065
UIA_GridItemRowSpanPropertyId: UIA_PROPERTY_ID = 30066
UIA_GridItemColumnSpanPropertyId: UIA_PROPERTY_ID = 30067
UIA_GridItemContainingGridPropertyId: UIA_PROPERTY_ID = 30068
UIA_DockDockPositionPropertyId: UIA_PROPERTY_ID = 30069
UIA_ExpandCollapseExpandCollapseStatePropertyId: UIA_PROPERTY_ID = 30070
UIA_MultipleViewCurrentViewPropertyId: UIA_PROPERTY_ID = 30071
UIA_MultipleViewSupportedViewsPropertyId: UIA_PROPERTY_ID = 30072
UIA_WindowCanMaximizePropertyId: UIA_PROPERTY_ID = 30073
UIA_WindowCanMinimizePropertyId: UIA_PROPERTY_ID = 30074
UIA_WindowWindowVisualStatePropertyId: UIA_PROPERTY_ID = 30075
UIA_WindowWindowInteractionStatePropertyId: UIA_PROPERTY_ID = 30076
UIA_WindowIsModalPropertyId: UIA_PROPERTY_ID = 30077
UIA_WindowIsTopmostPropertyId: UIA_PROPERTY_ID = 30078
UIA_SelectionItemIsSelectedPropertyId: UIA_PROPERTY_ID = 30079
UIA_SelectionItemSelectionContainerPropertyId: UIA_PROPERTY_ID = 30080
UIA_TableRowHeadersPropertyId: UIA_PROPERTY_ID = 30081
UIA_TableColumnHeadersPropertyId: UIA_PROPERTY_ID = 30082
UIA_TableRowOrColumnMajorPropertyId: UIA_PROPERTY_ID = 30083
UIA_TableItemRowHeaderItemsPropertyId: UIA_PROPERTY_ID = 30084
UIA_TableItemColumnHeaderItemsPropertyId: UIA_PROPERTY_ID = 30085
UIA_ToggleToggleStatePropertyId: UIA_PROPERTY_ID = 30086
UIA_TransformCanMovePropertyId: UIA_PROPERTY_ID = 30087
UIA_TransformCanResizePropertyId: UIA_PROPERTY_ID = 30088
UIA_TransformCanRotatePropertyId: UIA_PROPERTY_ID = 30089
UIA_IsLegacyIAccessiblePatternAvailablePropertyId: UIA_PROPERTY_ID = 30090
UIA_LegacyIAccessibleChildIdPropertyId: UIA_PROPERTY_ID = 30091
UIA_LegacyIAccessibleNamePropertyId: UIA_PROPERTY_ID = 30092
UIA_LegacyIAccessibleValuePropertyId: UIA_PROPERTY_ID = 30093
UIA_LegacyIAccessibleDescriptionPropertyId: UIA_PROPERTY_ID = 30094
UIA_LegacyIAccessibleRolePropertyId: UIA_PROPERTY_ID = 30095
UIA_LegacyIAccessibleStatePropertyId: UIA_PROPERTY_ID = 30096
UIA_LegacyIAccessibleHelpPropertyId: UIA_PROPERTY_ID = 30097
UIA_LegacyIAccessibleKeyboardShortcutPropertyId: UIA_PROPERTY_ID = 30098
UIA_LegacyIAccessibleSelectionPropertyId: UIA_PROPERTY_ID = 30099
UIA_LegacyIAccessibleDefaultActionPropertyId: UIA_PROPERTY_ID = 30100
UIA_AriaRolePropertyId: UIA_PROPERTY_ID = 30101
UIA_AriaPropertiesPropertyId: UIA_PROPERTY_ID = 30102
UIA_IsDataValidForFormPropertyId: UIA_PROPERTY_ID = 30103
UIA_ControllerForPropertyId: UIA_PROPERTY_ID = 30104
UIA_DescribedByPropertyId: UIA_PROPERTY_ID = 30105
UIA_FlowsToPropertyId: UIA_PROPERTY_ID = 30106
UIA_ProviderDescriptionPropertyId: UIA_PROPERTY_ID = 30107
UIA_IsItemContainerPatternAvailablePropertyId: UIA_PROPERTY_ID = 30108
UIA_IsVirtualizedItemPatternAvailablePropertyId: UIA_PROPERTY_ID = 30109
UIA_IsSynchronizedInputPatternAvailablePropertyId: UIA_PROPERTY_ID = 30110
UIA_OptimizeForVisualContentPropertyId: UIA_PROPERTY_ID = 30111
UIA_IsObjectModelPatternAvailablePropertyId: UIA_PROPERTY_ID = 30112
UIA_AnnotationAnnotationTypeIdPropertyId: UIA_PROPERTY_ID = 30113
UIA_AnnotationAnnotationTypeNamePropertyId: UIA_PROPERTY_ID = 30114
UIA_AnnotationAuthorPropertyId: UIA_PROPERTY_ID = 30115
UIA_AnnotationDateTimePropertyId: UIA_PROPERTY_ID = 30116
UIA_AnnotationTargetPropertyId: UIA_PROPERTY_ID = 30117
UIA_IsAnnotationPatternAvailablePropertyId: UIA_PROPERTY_ID = 30118
UIA_IsTextPattern2AvailablePropertyId: UIA_PROPERTY_ID = 30119
UIA_StylesStyleIdPropertyId: UIA_PROPERTY_ID = 30120
UIA_StylesStyleNamePropertyId: UIA_PROPERTY_ID = 30121
UIA_StylesFillColorPropertyId: UIA_PROPERTY_ID = 30122
UIA_StylesFillPatternStylePropertyId: UIA_PROPERTY_ID = 30123
UIA_StylesShapePropertyId: UIA_PROPERTY_ID = 30124
UIA_StylesFillPatternColorPropertyId: UIA_PROPERTY_ID = 30125
UIA_StylesExtendedPropertiesPropertyId: UIA_PROPERTY_ID = 30126
UIA_IsStylesPatternAvailablePropertyId: UIA_PROPERTY_ID = 30127
UIA_IsSpreadsheetPatternAvailablePropertyId: UIA_PROPERTY_ID = 30128
UIA_SpreadsheetItemFormulaPropertyId: UIA_PROPERTY_ID = 30129
UIA_SpreadsheetItemAnnotationObjectsPropertyId: UIA_PROPERTY_ID = 30130
UIA_SpreadsheetItemAnnotationTypesPropertyId: UIA_PROPERTY_ID = 30131
UIA_IsSpreadsheetItemPatternAvailablePropertyId: UIA_PROPERTY_ID = 30132
UIA_Transform2CanZoomPropertyId: UIA_PROPERTY_ID = 30133
UIA_IsTransformPattern2AvailablePropertyId: UIA_PROPERTY_ID = 30134
UIA_LiveSettingPropertyId: UIA_PROPERTY_ID = 30135
UIA_IsTextChildPatternAvailablePropertyId: UIA_PROPERTY_ID = 30136
UIA_IsDragPatternAvailablePropertyId: UIA_PROPERTY_ID = 30137
UIA_DragIsGrabbedPropertyId: UIA_PROPERTY_ID = 30138
UIA_DragDropEffectPropertyId: UIA_PROPERTY_ID = 30139
UIA_DragDropEffectsPropertyId: UIA_PROPERTY_ID = 30140
UIA_IsDropTargetPatternAvailablePropertyId: UIA_PROPERTY_ID = 30141
UIA_DropTargetDropTargetEffectPropertyId: UIA_PROPERTY_ID = 30142
UIA_DropTargetDropTargetEffectsPropertyId: UIA_PROPERTY_ID = 30143
UIA_DragGrabbedItemsPropertyId: UIA_PROPERTY_ID = 30144
UIA_Transform2ZoomLevelPropertyId: UIA_PROPERTY_ID = 30145
UIA_Transform2ZoomMinimumPropertyId: UIA_PROPERTY_ID = 30146
UIA_Transform2ZoomMaximumPropertyId: UIA_PROPERTY_ID = 30147
UIA_FlowsFromPropertyId: UIA_PROPERTY_ID = 30148
UIA_IsTextEditPatternAvailablePropertyId: UIA_PROPERTY_ID = 30149
UIA_IsPeripheralPropertyId: UIA_PROPERTY_ID = 30150
UIA_IsCustomNavigationPatternAvailablePropertyId: UIA_PROPERTY_ID = 30151
UIA_PositionInSetPropertyId: UIA_PROPERTY_ID = 30152
UIA_SizeOfSetPropertyId: UIA_PROPERTY_ID = 30153
UIA_LevelPropertyId: UIA_PROPERTY_ID = 30154
UIA_AnnotationTypesPropertyId: UIA_PROPERTY_ID = 30155
UIA_AnnotationObjectsPropertyId: UIA_PROPERTY_ID = 30156
UIA_LandmarkTypePropertyId: UIA_PROPERTY_ID = 30157
UIA_LocalizedLandmarkTypePropertyId: UIA_PROPERTY_ID = 30158
UIA_FullDescriptionPropertyId: UIA_PROPERTY_ID = 30159
UIA_FillColorPropertyId: UIA_PROPERTY_ID = 30160
UIA_OutlineColorPropertyId: UIA_PROPERTY_ID = 30161
UIA_FillTypePropertyId: UIA_PROPERTY_ID = 30162
UIA_VisualEffectsPropertyId: UIA_PROPERTY_ID = 30163
UIA_OutlineThicknessPropertyId: UIA_PROPERTY_ID = 30164
UIA_CenterPointPropertyId: UIA_PROPERTY_ID = 30165
UIA_RotationPropertyId: UIA_PROPERTY_ID = 30166
UIA_SizePropertyId: UIA_PROPERTY_ID = 30167
UIA_IsSelectionPattern2AvailablePropertyId: UIA_PROPERTY_ID = 30168
UIA_Selection2FirstSelectedItemPropertyId: UIA_PROPERTY_ID = 30169
UIA_Selection2LastSelectedItemPropertyId: UIA_PROPERTY_ID = 30170
UIA_Selection2CurrentSelectedItemPropertyId: UIA_PROPERTY_ID = 30171
UIA_Selection2ItemCountPropertyId: UIA_PROPERTY_ID = 30172
UIA_HeadingLevelPropertyId: UIA_PROPERTY_ID = 30173
UIA_IsDialogPropertyId: UIA_PROPERTY_ID = 30174
UIA_STYLE_ID = UInt32
StyleId_Custom: UIA_STYLE_ID = 70000
StyleId_Heading1: UIA_STYLE_ID = 70001
StyleId_Heading2: UIA_STYLE_ID = 70002
StyleId_Heading3: UIA_STYLE_ID = 70003
StyleId_Heading4: UIA_STYLE_ID = 70004
StyleId_Heading5: UIA_STYLE_ID = 70005
StyleId_Heading6: UIA_STYLE_ID = 70006
StyleId_Heading7: UIA_STYLE_ID = 70007
StyleId_Heading8: UIA_STYLE_ID = 70008
StyleId_Heading9: UIA_STYLE_ID = 70009
StyleId_Title: UIA_STYLE_ID = 70010
StyleId_Subtitle: UIA_STYLE_ID = 70011
StyleId_Normal: UIA_STYLE_ID = 70012
StyleId_Emphasis: UIA_STYLE_ID = 70013
StyleId_Quote: UIA_STYLE_ID = 70014
StyleId_BulletedList: UIA_STYLE_ID = 70015
StyleId_NumberedList: UIA_STYLE_ID = 70016
UIA_TEXTATTRIBUTE_ID = UInt32
UIA_AnimationStyleAttributeId: UIA_TEXTATTRIBUTE_ID = 40000
UIA_BackgroundColorAttributeId: UIA_TEXTATTRIBUTE_ID = 40001
UIA_BulletStyleAttributeId: UIA_TEXTATTRIBUTE_ID = 40002
UIA_CapStyleAttributeId: UIA_TEXTATTRIBUTE_ID = 40003
UIA_CultureAttributeId: UIA_TEXTATTRIBUTE_ID = 40004
UIA_FontNameAttributeId: UIA_TEXTATTRIBUTE_ID = 40005
UIA_FontSizeAttributeId: UIA_TEXTATTRIBUTE_ID = 40006
UIA_FontWeightAttributeId: UIA_TEXTATTRIBUTE_ID = 40007
UIA_ForegroundColorAttributeId: UIA_TEXTATTRIBUTE_ID = 40008
UIA_HorizontalTextAlignmentAttributeId: UIA_TEXTATTRIBUTE_ID = 40009
UIA_IndentationFirstLineAttributeId: UIA_TEXTATTRIBUTE_ID = 40010
UIA_IndentationLeadingAttributeId: UIA_TEXTATTRIBUTE_ID = 40011
UIA_IndentationTrailingAttributeId: UIA_TEXTATTRIBUTE_ID = 40012
UIA_IsHiddenAttributeId: UIA_TEXTATTRIBUTE_ID = 40013
UIA_IsItalicAttributeId: UIA_TEXTATTRIBUTE_ID = 40014
UIA_IsReadOnlyAttributeId: UIA_TEXTATTRIBUTE_ID = 40015
UIA_IsSubscriptAttributeId: UIA_TEXTATTRIBUTE_ID = 40016
UIA_IsSuperscriptAttributeId: UIA_TEXTATTRIBUTE_ID = 40017
UIA_MarginBottomAttributeId: UIA_TEXTATTRIBUTE_ID = 40018
UIA_MarginLeadingAttributeId: UIA_TEXTATTRIBUTE_ID = 40019
UIA_MarginTopAttributeId: UIA_TEXTATTRIBUTE_ID = 40020
UIA_MarginTrailingAttributeId: UIA_TEXTATTRIBUTE_ID = 40021
UIA_OutlineStylesAttributeId: UIA_TEXTATTRIBUTE_ID = 40022
UIA_OverlineColorAttributeId: UIA_TEXTATTRIBUTE_ID = 40023
UIA_OverlineStyleAttributeId: UIA_TEXTATTRIBUTE_ID = 40024
UIA_StrikethroughColorAttributeId: UIA_TEXTATTRIBUTE_ID = 40025
UIA_StrikethroughStyleAttributeId: UIA_TEXTATTRIBUTE_ID = 40026
UIA_TabsAttributeId: UIA_TEXTATTRIBUTE_ID = 40027
UIA_TextFlowDirectionsAttributeId: UIA_TEXTATTRIBUTE_ID = 40028
UIA_UnderlineColorAttributeId: UIA_TEXTATTRIBUTE_ID = 40029
UIA_UnderlineStyleAttributeId: UIA_TEXTATTRIBUTE_ID = 40030
UIA_AnnotationTypesAttributeId: UIA_TEXTATTRIBUTE_ID = 40031
UIA_AnnotationObjectsAttributeId: UIA_TEXTATTRIBUTE_ID = 40032
UIA_StyleNameAttributeId: UIA_TEXTATTRIBUTE_ID = 40033
UIA_StyleIdAttributeId: UIA_TEXTATTRIBUTE_ID = 40034
UIA_LinkAttributeId: UIA_TEXTATTRIBUTE_ID = 40035
UIA_IsActiveAttributeId: UIA_TEXTATTRIBUTE_ID = 40036
UIA_SelectionActiveEndAttributeId: UIA_TEXTATTRIBUTE_ID = 40037
UIA_CaretPositionAttributeId: UIA_TEXTATTRIBUTE_ID = 40038
UIA_CaretBidiModeAttributeId: UIA_TEXTATTRIBUTE_ID = 40039
UIA_LineSpacingAttributeId: UIA_TEXTATTRIBUTE_ID = 40040
UIA_BeforeParagraphSpacingAttributeId: UIA_TEXTATTRIBUTE_ID = 40041
UIA_AfterParagraphSpacingAttributeId: UIA_TEXTATTRIBUTE_ID = 40042
UIA_SayAsInterpretAsAttributeId: UIA_TEXTATTRIBUTE_ID = 40043
class UIAutomationEventInfo(Structure):
    guid: Guid
    pProgrammaticName: Windows.Win32.Foundation.PWSTR
class UIAutomationMethodInfo(Structure):
    pProgrammaticName: Windows.Win32.Foundation.PWSTR
    doSetFocus: Windows.Win32.Foundation.BOOL
    cInParameters: UInt32
    cOutParameters: UInt32
    pParameterTypes: POINTER(Windows.Win32.UI.Accessibility.UIAutomationType)
    pParameterNames: POINTER(Windows.Win32.Foundation.PWSTR)
class UIAutomationParameter(Structure):
    type: Windows.Win32.UI.Accessibility.UIAutomationType
    pData: c_void_p
class UIAutomationPatternInfo(Structure):
    guid: Guid
    pProgrammaticName: Windows.Win32.Foundation.PWSTR
    providerInterfaceId: Guid
    clientInterfaceId: Guid
    cProperties: UInt32
    pProperties: POINTER(Windows.Win32.UI.Accessibility.UIAutomationPropertyInfo_head)
    cMethods: UInt32
    pMethods: POINTER(Windows.Win32.UI.Accessibility.UIAutomationMethodInfo_head)
    cEvents: UInt32
    pEvents: POINTER(Windows.Win32.UI.Accessibility.UIAutomationEventInfo_head)
    pPatternHandler: Windows.Win32.UI.Accessibility.IUIAutomationPatternHandler_head
class UIAutomationPropertyInfo(Structure):
    guid: Guid
    pProgrammaticName: Windows.Win32.Foundation.PWSTR
    type: Windows.Win32.UI.Accessibility.UIAutomationType
UIAutomationType = Int32
UIAutomationType_Int: UIAutomationType = 1
UIAutomationType_Bool: UIAutomationType = 2
UIAutomationType_String: UIAutomationType = 3
UIAutomationType_Double: UIAutomationType = 4
UIAutomationType_Point: UIAutomationType = 5
UIAutomationType_Rect: UIAutomationType = 6
UIAutomationType_Element: UIAutomationType = 7
UIAutomationType_Array: UIAutomationType = 65536
UIAutomationType_Out: UIAutomationType = 131072
UIAutomationType_IntArray: UIAutomationType = 65537
UIAutomationType_BoolArray: UIAutomationType = 65538
UIAutomationType_StringArray: UIAutomationType = 65539
UIAutomationType_DoubleArray: UIAutomationType = 65540
UIAutomationType_PointArray: UIAutomationType = 65541
UIAutomationType_RectArray: UIAutomationType = 65542
UIAutomationType_ElementArray: UIAutomationType = 65543
UIAutomationType_OutInt: UIAutomationType = 131073
UIAutomationType_OutBool: UIAutomationType = 131074
UIAutomationType_OutString: UIAutomationType = 131075
UIAutomationType_OutDouble: UIAutomationType = 131076
UIAutomationType_OutPoint: UIAutomationType = 131077
UIAutomationType_OutRect: UIAutomationType = 131078
UIAutomationType_OutElement: UIAutomationType = 131079
UIAutomationType_OutIntArray: UIAutomationType = 196609
UIAutomationType_OutBoolArray: UIAutomationType = 196610
UIAutomationType_OutStringArray: UIAutomationType = 196611
UIAutomationType_OutDoubleArray: UIAutomationType = 196612
UIAutomationType_OutPointArray: UIAutomationType = 196613
UIAutomationType_OutRectArray: UIAutomationType = 196614
UIAutomationType_OutElementArray: UIAutomationType = 196615
class UiaAndOrCondition(Structure):
    ConditionType: Windows.Win32.UI.Accessibility.ConditionType
    ppConditions: POINTER(POINTER(Windows.Win32.UI.Accessibility.UiaCondition_head))
    cConditions: Int32
class UiaAsyncContentLoadedEventArgs(Structure):
    Type: Windows.Win32.UI.Accessibility.EventArgsType
    EventId: Int32
    AsyncContentLoadedState: Windows.Win32.UI.Accessibility.AsyncContentLoadedState
    PercentComplete: Double
class UiaCacheRequest(Structure):
    pViewCondition: POINTER(Windows.Win32.UI.Accessibility.UiaCondition_head)
    Scope: Windows.Win32.UI.Accessibility.TreeScope
    pProperties: POINTER(Int32)
    cProperties: Int32
    pPatterns: POINTER(Int32)
    cPatterns: Int32
    automationElementMode: Windows.Win32.UI.Accessibility.AutomationElementMode
class UiaChangeInfo(Structure):
    uiaId: Int32
    payload: Windows.Win32.System.Com.VARIANT
    extraInfo: Windows.Win32.System.Com.VARIANT
class UiaChangesEventArgs(Structure):
    Type: Windows.Win32.UI.Accessibility.EventArgsType
    EventId: Int32
    EventIdCount: Int32
    pUiaChanges: POINTER(Windows.Win32.UI.Accessibility.UiaChangeInfo_head)
class UiaCondition(Structure):
    ConditionType: Windows.Win32.UI.Accessibility.ConditionType
class UiaEventArgs(Structure):
    Type: Windows.Win32.UI.Accessibility.EventArgsType
    EventId: Int32
@winfunctype_pointer
def UiaEventCallback(pArgs: POINTER(Windows.Win32.UI.Accessibility.UiaEventArgs_head), pRequestedData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), pTreeStructure: Windows.Win32.Foundation.BSTR) -> Void: ...
class UiaFindParams(Structure):
    MaxDepth: Int32
    FindFirst: Windows.Win32.Foundation.BOOL
    ExcludeRoot: Windows.Win32.Foundation.BOOL
    pFindCondition: POINTER(Windows.Win32.UI.Accessibility.UiaCondition_head)
class UiaNotCondition(Structure):
    ConditionType: Windows.Win32.UI.Accessibility.ConditionType
    pCondition: POINTER(Windows.Win32.UI.Accessibility.UiaCondition_head)
class UiaPoint(Structure):
    x: Double
    y: Double
class UiaPropertyChangedEventArgs(Structure):
    Type: Windows.Win32.UI.Accessibility.EventArgsType
    EventId: Windows.Win32.UI.Accessibility.UIA_EVENT_ID
    PropertyId: Int32
    OldValue: Windows.Win32.System.Com.VARIANT
    NewValue: Windows.Win32.System.Com.VARIANT
class UiaPropertyCondition(Structure):
    ConditionType: Windows.Win32.UI.Accessibility.ConditionType
    PropertyId: Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID
    Value: Windows.Win32.System.Com.VARIANT
    Flags: Windows.Win32.UI.Accessibility.PropertyConditionFlags
@winfunctype_pointer
def UiaProviderCallback(hwnd: Windows.Win32.Foundation.HWND, providerType: Windows.Win32.UI.Accessibility.ProviderType) -> POINTER(Windows.Win32.System.Com.SAFEARRAY_head): ...
class UiaRect(Structure):
    left: Double
    top: Double
    width: Double
    height: Double
class UiaStructureChangedEventArgs(Structure):
    Type: Windows.Win32.UI.Accessibility.EventArgsType
    EventId: Int32
    StructureChangeType: Windows.Win32.UI.Accessibility.StructureChangeType
    pRuntimeId: POINTER(Int32)
    cRuntimeIdLen: Int32
class UiaTextEditTextChangedEventArgs(Structure):
    Type: Windows.Win32.UI.Accessibility.EventArgsType
    EventId: Int32
    TextEditChangeType: Windows.Win32.UI.Accessibility.TextEditChangeType
    pTextChange: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)
class UiaWindowClosedEventArgs(Structure):
    Type: Windows.Win32.UI.Accessibility.EventArgsType
    EventId: Int32
    pRuntimeId: POINTER(Int32)
    cRuntimeIdLen: Int32
VisualEffects = Int32
VisualEffects_None: VisualEffects = 0
VisualEffects_Shadow: VisualEffects = 1
VisualEffects_Reflection: VisualEffects = 2
VisualEffects_Glow: VisualEffects = 4
VisualEffects_SoftEdges: VisualEffects = 8
VisualEffects_Bevel: VisualEffects = 16
@winfunctype_pointer
def WINEVENTPROC(hWinEventHook: Windows.Win32.UI.Accessibility.HWINEVENTHOOK, event: UInt32, hwnd: Windows.Win32.Foundation.HWND, idObject: Int32, idChild: Int32, idEventThread: UInt32, dwmsEventTime: UInt32) -> Void: ...
WindowInteractionState = Int32
WindowInteractionState_Running: WindowInteractionState = 0
WindowInteractionState_Closing: WindowInteractionState = 1
WindowInteractionState_ReadyForUserInteraction: WindowInteractionState = 2
WindowInteractionState_BlockedByModalWindow: WindowInteractionState = 3
WindowInteractionState_NotResponding: WindowInteractionState = 4
WindowVisualState = Int32
WindowVisualState_Normal: WindowVisualState = 0
WindowVisualState_Maximized: WindowVisualState = 1
WindowVisualState_Minimized: WindowVisualState = 2
ZoomUnit = Int32
ZoomUnit_NoAmount: ZoomUnit = 0
ZoomUnit_LargeDecrement: ZoomUnit = 1
ZoomUnit_SmallDecrement: ZoomUnit = 2
ZoomUnit_LargeIncrement: ZoomUnit = 3
ZoomUnit_SmallIncrement: ZoomUnit = 4
make_head(_module, 'ACCESSTIMEOUT')
make_head(_module, 'ExtendedProperty')
make_head(_module, 'FILTERKEYS')
make_head(_module, 'HIGHCONTRASTA')
make_head(_module, 'HIGHCONTRASTW')
make_head(_module, 'IAccIdentity')
make_head(_module, 'IAccPropServer')
make_head(_module, 'IAccPropServices')
make_head(_module, 'IAccessible')
make_head(_module, 'IAccessibleEx')
make_head(_module, 'IAccessibleHandler')
make_head(_module, 'IAccessibleHostingElementProviders')
make_head(_module, 'IAccessibleWindowlessSite')
make_head(_module, 'IAnnotationProvider')
make_head(_module, 'ICustomNavigationProvider')
make_head(_module, 'IDockProvider')
make_head(_module, 'IDragProvider')
make_head(_module, 'IDropTargetProvider')
make_head(_module, 'IExpandCollapseProvider')
make_head(_module, 'IGridItemProvider')
make_head(_module, 'IGridProvider')
make_head(_module, 'IInvokeProvider')
make_head(_module, 'IItemContainerProvider')
make_head(_module, 'ILegacyIAccessibleProvider')
make_head(_module, 'IMultipleViewProvider')
make_head(_module, 'IObjectModelProvider')
make_head(_module, 'IProxyProviderWinEventHandler')
make_head(_module, 'IProxyProviderWinEventSink')
make_head(_module, 'IRangeValueProvider')
make_head(_module, 'IRawElementProviderAdviseEvents')
make_head(_module, 'IRawElementProviderFragment')
make_head(_module, 'IRawElementProviderFragmentRoot')
make_head(_module, 'IRawElementProviderHostingAccessibles')
make_head(_module, 'IRawElementProviderHwndOverride')
make_head(_module, 'IRawElementProviderSimple')
make_head(_module, 'IRawElementProviderSimple2')
make_head(_module, 'IRawElementProviderSimple3')
make_head(_module, 'IRawElementProviderWindowlessSite')
make_head(_module, 'IRichEditUiaInformation')
make_head(_module, 'IRicheditWindowlessAccessibility')
make_head(_module, 'IScrollItemProvider')
make_head(_module, 'IScrollProvider')
make_head(_module, 'ISelectionItemProvider')
make_head(_module, 'ISelectionProvider')
make_head(_module, 'ISelectionProvider2')
make_head(_module, 'ISpreadsheetItemProvider')
make_head(_module, 'ISpreadsheetProvider')
make_head(_module, 'IStylesProvider')
make_head(_module, 'ISynchronizedInputProvider')
make_head(_module, 'ITableItemProvider')
make_head(_module, 'ITableProvider')
make_head(_module, 'ITextChildProvider')
make_head(_module, 'ITextEditProvider')
make_head(_module, 'ITextProvider')
make_head(_module, 'ITextProvider2')
make_head(_module, 'ITextRangeProvider')
make_head(_module, 'ITextRangeProvider2')
make_head(_module, 'IToggleProvider')
make_head(_module, 'ITransformProvider')
make_head(_module, 'ITransformProvider2')
make_head(_module, 'IUIAutomation')
make_head(_module, 'IUIAutomation2')
make_head(_module, 'IUIAutomation3')
make_head(_module, 'IUIAutomation4')
make_head(_module, 'IUIAutomation5')
make_head(_module, 'IUIAutomation6')
make_head(_module, 'IUIAutomationActiveTextPositionChangedEventHandler')
make_head(_module, 'IUIAutomationAndCondition')
make_head(_module, 'IUIAutomationAnnotationPattern')
make_head(_module, 'IUIAutomationBoolCondition')
make_head(_module, 'IUIAutomationCacheRequest')
make_head(_module, 'IUIAutomationChangesEventHandler')
make_head(_module, 'IUIAutomationCondition')
make_head(_module, 'IUIAutomationCustomNavigationPattern')
make_head(_module, 'IUIAutomationDockPattern')
make_head(_module, 'IUIAutomationDragPattern')
make_head(_module, 'IUIAutomationDropTargetPattern')
make_head(_module, 'IUIAutomationElement')
make_head(_module, 'IUIAutomationElement2')
make_head(_module, 'IUIAutomationElement3')
make_head(_module, 'IUIAutomationElement4')
make_head(_module, 'IUIAutomationElement5')
make_head(_module, 'IUIAutomationElement6')
make_head(_module, 'IUIAutomationElement7')
make_head(_module, 'IUIAutomationElement8')
make_head(_module, 'IUIAutomationElement9')
make_head(_module, 'IUIAutomationElementArray')
make_head(_module, 'IUIAutomationEventHandler')
make_head(_module, 'IUIAutomationEventHandlerGroup')
make_head(_module, 'IUIAutomationExpandCollapsePattern')
make_head(_module, 'IUIAutomationFocusChangedEventHandler')
make_head(_module, 'IUIAutomationGridItemPattern')
make_head(_module, 'IUIAutomationGridPattern')
make_head(_module, 'IUIAutomationInvokePattern')
make_head(_module, 'IUIAutomationItemContainerPattern')
make_head(_module, 'IUIAutomationLegacyIAccessiblePattern')
make_head(_module, 'IUIAutomationMultipleViewPattern')
make_head(_module, 'IUIAutomationNotCondition')
make_head(_module, 'IUIAutomationNotificationEventHandler')
make_head(_module, 'IUIAutomationObjectModelPattern')
make_head(_module, 'IUIAutomationOrCondition')
make_head(_module, 'IUIAutomationPatternHandler')
make_head(_module, 'IUIAutomationPatternInstance')
make_head(_module, 'IUIAutomationPropertyChangedEventHandler')
make_head(_module, 'IUIAutomationPropertyCondition')
make_head(_module, 'IUIAutomationProxyFactory')
make_head(_module, 'IUIAutomationProxyFactoryEntry')
make_head(_module, 'IUIAutomationProxyFactoryMapping')
make_head(_module, 'IUIAutomationRangeValuePattern')
make_head(_module, 'IUIAutomationRegistrar')
make_head(_module, 'IUIAutomationScrollItemPattern')
make_head(_module, 'IUIAutomationScrollPattern')
make_head(_module, 'IUIAutomationSelectionItemPattern')
make_head(_module, 'IUIAutomationSelectionPattern')
make_head(_module, 'IUIAutomationSelectionPattern2')
make_head(_module, 'IUIAutomationSpreadsheetItemPattern')
make_head(_module, 'IUIAutomationSpreadsheetPattern')
make_head(_module, 'IUIAutomationStructureChangedEventHandler')
make_head(_module, 'IUIAutomationStylesPattern')
make_head(_module, 'IUIAutomationSynchronizedInputPattern')
make_head(_module, 'IUIAutomationTableItemPattern')
make_head(_module, 'IUIAutomationTablePattern')
make_head(_module, 'IUIAutomationTextChildPattern')
make_head(_module, 'IUIAutomationTextEditPattern')
make_head(_module, 'IUIAutomationTextEditTextChangedEventHandler')
make_head(_module, 'IUIAutomationTextPattern')
make_head(_module, 'IUIAutomationTextPattern2')
make_head(_module, 'IUIAutomationTextRange')
make_head(_module, 'IUIAutomationTextRange2')
make_head(_module, 'IUIAutomationTextRange3')
make_head(_module, 'IUIAutomationTextRangeArray')
make_head(_module, 'IUIAutomationTogglePattern')
make_head(_module, 'IUIAutomationTransformPattern')
make_head(_module, 'IUIAutomationTransformPattern2')
make_head(_module, 'IUIAutomationTreeWalker')
make_head(_module, 'IUIAutomationValuePattern')
make_head(_module, 'IUIAutomationVirtualizedItemPattern')
make_head(_module, 'IUIAutomationWindowPattern')
make_head(_module, 'IValueProvider')
make_head(_module, 'IVirtualizedItemProvider')
make_head(_module, 'IWindowProvider')
make_head(_module, 'LPFNACCESSIBLECHILDREN')
make_head(_module, 'LPFNACCESSIBLEOBJECTFROMPOINT')
make_head(_module, 'LPFNACCESSIBLEOBJECTFROMWINDOW')
make_head(_module, 'LPFNCREATESTDACCESSIBLEOBJECT')
make_head(_module, 'LPFNLRESULTFROMOBJECT')
make_head(_module, 'LPFNOBJECTFROMLRESULT')
make_head(_module, 'MOUSEKEYS')
make_head(_module, 'MSAAMENUINFO')
make_head(_module, 'SERIALKEYSA')
make_head(_module, 'SERIALKEYSW')
make_head(_module, 'SOUNDSENTRYA')
make_head(_module, 'SOUNDSENTRYW')
make_head(_module, 'STICKYKEYS')
make_head(_module, 'TOGGLEKEYS')
make_head(_module, 'UIAutomationEventInfo')
make_head(_module, 'UIAutomationMethodInfo')
make_head(_module, 'UIAutomationParameter')
make_head(_module, 'UIAutomationPatternInfo')
make_head(_module, 'UIAutomationPropertyInfo')
make_head(_module, 'UiaAndOrCondition')
make_head(_module, 'UiaAsyncContentLoadedEventArgs')
make_head(_module, 'UiaCacheRequest')
make_head(_module, 'UiaChangeInfo')
make_head(_module, 'UiaChangesEventArgs')
make_head(_module, 'UiaCondition')
make_head(_module, 'UiaEventArgs')
make_head(_module, 'UiaEventCallback')
make_head(_module, 'UiaFindParams')
make_head(_module, 'UiaNotCondition')
make_head(_module, 'UiaPoint')
make_head(_module, 'UiaPropertyChangedEventArgs')
make_head(_module, 'UiaPropertyCondition')
make_head(_module, 'UiaProviderCallback')
make_head(_module, 'UiaRect')
make_head(_module, 'UiaStructureChangedEventArgs')
make_head(_module, 'UiaTextEditTextChangedEventArgs')
make_head(_module, 'UiaWindowClosedEventArgs')
make_head(_module, 'WINEVENTPROC')
__all__ = [
    "ACCESSTIMEOUT",
    "ACC_UTILITY_STATE_FLAGS",
    "ANNO_CONTAINER",
    "ANNO_THIS",
    "ANRUS_ON_SCREEN_KEYBOARD_ACTIVE",
    "ANRUS_PRIORITY_AUDIO_ACTIVE",
    "ANRUS_PRIORITY_AUDIO_ACTIVE_NODUCK",
    "ANRUS_PRIORITY_AUDIO_DYNAMIC_DUCK",
    "ANRUS_TOUCH_MODIFICATION_ACTIVE",
    "AccNotifyTouchInteraction",
    "AccSetRunningUtilityState",
    "AcceleratorKey_Property_GUID",
    "AccessKey_Property_GUID",
    "AccessibleChildren",
    "AccessibleObjectFromEvent",
    "AccessibleObjectFromPoint",
    "AccessibleObjectFromWindow",
    "ActiveEnd",
    "ActiveEnd_End",
    "ActiveEnd_None",
    "ActiveEnd_Start",
    "ActiveTextPositionChanged_Event_GUID",
    "AnimationStyle",
    "AnimationStyle_BlinkingBackground",
    "AnimationStyle_LasVegasLights",
    "AnimationStyle_MarchingBlackAnts",
    "AnimationStyle_MarchingRedAnts",
    "AnimationStyle_None",
    "AnimationStyle_Other",
    "AnimationStyle_Shimmer",
    "AnimationStyle_SparkleText",
    "AnnoScope",
    "AnnotationObjects_Property_GUID",
    "AnnotationType_AdvancedProofingIssue",
    "AnnotationType_Author",
    "AnnotationType_CircularReferenceError",
    "AnnotationType_Comment",
    "AnnotationType_ConflictingChange",
    "AnnotationType_DataValidationError",
    "AnnotationType_DeletionChange",
    "AnnotationType_EditingLockedChange",
    "AnnotationType_Endnote",
    "AnnotationType_ExternalChange",
    "AnnotationType_Footer",
    "AnnotationType_Footnote",
    "AnnotationType_FormatChange",
    "AnnotationType_FormulaError",
    "AnnotationType_GrammarError",
    "AnnotationType_Header",
    "AnnotationType_Highlighted",
    "AnnotationType_InsertionChange",
    "AnnotationType_Mathematics",
    "AnnotationType_MoveChange",
    "AnnotationType_Sensitive",
    "AnnotationType_SpellingError",
    "AnnotationType_TrackChanges",
    "AnnotationType_Unknown",
    "AnnotationType_UnsyncedChange",
    "AnnotationTypes_Property_GUID",
    "Annotation_AdvancedProofingIssue_GUID",
    "Annotation_AnnotationTypeId_Property_GUID",
    "Annotation_AnnotationTypeName_Property_GUID",
    "Annotation_Author_GUID",
    "Annotation_Author_Property_GUID",
    "Annotation_CircularReferenceError_GUID",
    "Annotation_Comment_GUID",
    "Annotation_ConflictingChange_GUID",
    "Annotation_Custom_GUID",
    "Annotation_DataValidationError_GUID",
    "Annotation_DateTime_Property_GUID",
    "Annotation_DeletionChange_GUID",
    "Annotation_EditingLockedChange_GUID",
    "Annotation_Endnote_GUID",
    "Annotation_ExternalChange_GUID",
    "Annotation_Footer_GUID",
    "Annotation_Footnote_GUID",
    "Annotation_FormatChange_GUID",
    "Annotation_FormulaError_GUID",
    "Annotation_GrammarError_GUID",
    "Annotation_Header_GUID",
    "Annotation_Highlighted_GUID",
    "Annotation_InsertionChange_GUID",
    "Annotation_Mathematics_GUID",
    "Annotation_MoveChange_GUID",
    "Annotation_Pattern_GUID",
    "Annotation_Sensitive_GUID",
    "Annotation_SpellingError_GUID",
    "Annotation_Target_Property_GUID",
    "Annotation_TrackChanges_GUID",
    "Annotation_UnsyncedChange_GUID",
    "AppBar_Control_GUID",
    "AriaProperties_Property_GUID",
    "AriaRole_Property_GUID",
    "AsyncContentLoadedState",
    "AsyncContentLoadedState_Beginning",
    "AsyncContentLoadedState_Completed",
    "AsyncContentLoadedState_Progress",
    "AsyncContentLoaded_Event_GUID",
    "AutomationElementMode",
    "AutomationElementMode_Full",
    "AutomationElementMode_None",
    "AutomationFocusChanged_Event_GUID",
    "AutomationId_Property_GUID",
    "AutomationIdentifierType",
    "AutomationIdentifierType_Annotation",
    "AutomationIdentifierType_Changes",
    "AutomationIdentifierType_ControlType",
    "AutomationIdentifierType_Event",
    "AutomationIdentifierType_LandmarkType",
    "AutomationIdentifierType_Pattern",
    "AutomationIdentifierType_Property",
    "AutomationIdentifierType_Style",
    "AutomationIdentifierType_TextAttribute",
    "AutomationPropertyChanged_Event_GUID",
    "BoundingRectangle_Property_GUID",
    "BulletStyle",
    "BulletStyle_DashBullet",
    "BulletStyle_FilledRoundBullet",
    "BulletStyle_FilledSquareBullet",
    "BulletStyle_HollowRoundBullet",
    "BulletStyle_HollowSquareBullet",
    "BulletStyle_None",
    "BulletStyle_Other",
    "Button_Control_GUID",
    "CAccPropServices",
    "CLSID_AccPropServices",
    "CUIAutomation",
    "CUIAutomation8",
    "CUIAutomationRegistrar",
    "Calendar_Control_GUID",
    "CapStyle",
    "CapStyle_AllCap",
    "CapStyle_AllPetiteCaps",
    "CapStyle_None",
    "CapStyle_Other",
    "CapStyle_PetiteCaps",
    "CapStyle_SmallCap",
    "CapStyle_Titling",
    "CapStyle_Unicase",
    "CaretBidiMode",
    "CaretBidiMode_LTR",
    "CaretBidiMode_RTL",
    "CaretPosition",
    "CaretPosition_BeginningOfLine",
    "CaretPosition_EndOfLine",
    "CaretPosition_Unknown",
    "CenterPoint_Property_GUID",
    "Changes_Event_GUID",
    "Changes_Summary_GUID",
    "CheckBox_Control_GUID",
    "ClassName_Property_GUID",
    "ClickablePoint_Property_GUID",
    "CoalesceEventsOptions",
    "CoalesceEventsOptions_Disabled",
    "CoalesceEventsOptions_Enabled",
    "ComboBox_Control_GUID",
    "ConditionType",
    "ConditionType_And",
    "ConditionType_False",
    "ConditionType_Not",
    "ConditionType_Or",
    "ConditionType_Property",
    "ConditionType_True",
    "ConnectionRecoveryBehaviorOptions",
    "ConnectionRecoveryBehaviorOptions_Disabled",
    "ConnectionRecoveryBehaviorOptions_Enabled",
    "ControlType_Property_GUID",
    "ControllerFor_Property_GUID",
    "CreateStdAccessibleObject",
    "CreateStdAccessibleProxyA",
    "CreateStdAccessibleProxyW",
    "Culture_Property_GUID",
    "CustomNavigation_Pattern_GUID",
    "Custom_Control_GUID",
    "DISPID_ACC_CHILD",
    "DISPID_ACC_CHILDCOUNT",
    "DISPID_ACC_DEFAULTACTION",
    "DISPID_ACC_DESCRIPTION",
    "DISPID_ACC_DODEFAULTACTION",
    "DISPID_ACC_FOCUS",
    "DISPID_ACC_HELP",
    "DISPID_ACC_HELPTOPIC",
    "DISPID_ACC_HITTEST",
    "DISPID_ACC_KEYBOARDSHORTCUT",
    "DISPID_ACC_LOCATION",
    "DISPID_ACC_NAME",
    "DISPID_ACC_NAVIGATE",
    "DISPID_ACC_PARENT",
    "DISPID_ACC_ROLE",
    "DISPID_ACC_SELECT",
    "DISPID_ACC_SELECTION",
    "DISPID_ACC_STATE",
    "DISPID_ACC_VALUE",
    "DataGrid_Control_GUID",
    "DataItem_Control_GUID",
    "DescribedBy_Property_GUID",
    "DockPattern_SetDockPosition",
    "DockPosition",
    "DockPosition_Bottom",
    "DockPosition_Fill",
    "DockPosition_Left",
    "DockPosition_None",
    "DockPosition_Right",
    "DockPosition_Top",
    "Dock_DockPosition_Property_GUID",
    "Dock_Pattern_GUID",
    "Document_Control_GUID",
    "Drag_DragCancel_Event_GUID",
    "Drag_DragComplete_Event_GUID",
    "Drag_DragStart_Event_GUID",
    "Drag_DropEffect_Property_GUID",
    "Drag_DropEffects_Property_GUID",
    "Drag_GrabbedItems_Property_GUID",
    "Drag_IsGrabbed_Property_GUID",
    "Drag_Pattern_GUID",
    "DropTarget_DragEnter_Event_GUID",
    "DropTarget_DragLeave_Event_GUID",
    "DropTarget_DropTargetEffect_Property_GUID",
    "DropTarget_DropTargetEffects_Property_GUID",
    "DropTarget_Dropped_Event_GUID",
    "DropTarget_Pattern_GUID",
    "Edit_Control_GUID",
    "EventArgsType",
    "EventArgsType_ActiveTextPositionChanged",
    "EventArgsType_AsyncContentLoaded",
    "EventArgsType_Changes",
    "EventArgsType_Notification",
    "EventArgsType_PropertyChanged",
    "EventArgsType_Simple",
    "EventArgsType_StructureChanged",
    "EventArgsType_StructuredMarkup",
    "EventArgsType_TextEditTextChanged",
    "EventArgsType_WindowClosed",
    "ExpandCollapsePattern_Collapse",
    "ExpandCollapsePattern_Expand",
    "ExpandCollapseState",
    "ExpandCollapseState_Collapsed",
    "ExpandCollapseState_Expanded",
    "ExpandCollapseState_LeafNode",
    "ExpandCollapseState_PartiallyExpanded",
    "ExpandCollapse_ExpandCollapseState_Property_GUID",
    "ExpandCollapse_Pattern_GUID",
    "ExtendedProperty",
    "FILTERKEYS",
    "FillColor_Property_GUID",
    "FillType",
    "FillType_Color",
    "FillType_Gradient",
    "FillType_None",
    "FillType_Pattern",
    "FillType_Picture",
    "FillType_Property_GUID",
    "FlowDirections",
    "FlowDirections_BottomToTop",
    "FlowDirections_Default",
    "FlowDirections_RightToLeft",
    "FlowDirections_Vertical",
    "FlowsFrom_Property_GUID",
    "FlowsTo_Property_GUID",
    "FrameworkId_Property_GUID",
    "FullDescription_Property_GUID",
    "GetOleaccVersionInfo",
    "GetRoleTextA",
    "GetRoleTextW",
    "GetStateTextA",
    "GetStateTextW",
    "GridItem_ColumnSpan_Property_GUID",
    "GridItem_Column_Property_GUID",
    "GridItem_Parent_Property_GUID",
    "GridItem_Pattern_GUID",
    "GridItem_RowSpan_Property_GUID",
    "GridItem_Row_Property_GUID",
    "GridPattern_GetItem",
    "Grid_ColumnCount_Property_GUID",
    "Grid_Pattern_GUID",
    "Grid_RowCount_Property_GUID",
    "Group_Control_GUID",
    "HCF_AVAILABLE",
    "HCF_CONFIRMHOTKEY",
    "HCF_HIGHCONTRASTON",
    "HCF_HOTKEYACTIVE",
    "HCF_HOTKEYAVAILABLE",
    "HCF_HOTKEYSOUND",
    "HCF_INDICATOR",
    "HCF_OPTION_NOTHEMECHANGE",
    "HIGHCONTRASTA",
    "HIGHCONTRASTW",
    "HIGHCONTRASTW_FLAGS",
    "HUIAEVENT",
    "HUIANODE",
    "HUIAPATTERNOBJECT",
    "HUIATEXTRANGE",
    "HWINEVENTHOOK",
    "HasKeyboardFocus_Property_GUID",
    "HeaderItem_Control_GUID",
    "Header_Control_GUID",
    "HeadingLevel_Property_GUID",
    "HelpText_Property_GUID",
    "HorizontalTextAlignment",
    "HorizontalTextAlignment_Centered",
    "HorizontalTextAlignment_Justified",
    "HorizontalTextAlignment_Left",
    "HorizontalTextAlignment_Right",
    "HostedFragmentRootsInvalidated_Event_GUID",
    "Hyperlink_Control_GUID",
    "IAccIdentity",
    "IAccPropServer",
    "IAccPropServices",
    "IAccessible",
    "IAccessibleEx",
    "IAccessibleHandler",
    "IAccessibleHostingElementProviders",
    "IAccessibleWindowlessSite",
    "IAnnotationProvider",
    "ICustomNavigationProvider",
    "IDockProvider",
    "IDragProvider",
    "IDropTargetProvider",
    "IExpandCollapseProvider",
    "IGridItemProvider",
    "IGridProvider",
    "IIS_ControlAccessible",
    "IIS_IsOleaccProxy",
    "IInvokeProvider",
    "IItemContainerProvider",
    "ILegacyIAccessibleProvider",
    "IMultipleViewProvider",
    "IObjectModelProvider",
    "IProxyProviderWinEventHandler",
    "IProxyProviderWinEventSink",
    "IRangeValueProvider",
    "IRawElementProviderAdviseEvents",
    "IRawElementProviderFragment",
    "IRawElementProviderFragmentRoot",
    "IRawElementProviderHostingAccessibles",
    "IRawElementProviderHwndOverride",
    "IRawElementProviderSimple",
    "IRawElementProviderSimple2",
    "IRawElementProviderSimple3",
    "IRawElementProviderWindowlessSite",
    "IRichEditUiaInformation",
    "IRicheditWindowlessAccessibility",
    "IScrollItemProvider",
    "IScrollProvider",
    "ISelectionItemProvider",
    "ISelectionProvider",
    "ISelectionProvider2",
    "ISpreadsheetItemProvider",
    "ISpreadsheetProvider",
    "IStylesProvider",
    "ISynchronizedInputProvider",
    "ITableItemProvider",
    "ITableProvider",
    "ITextChildProvider",
    "ITextEditProvider",
    "ITextProvider",
    "ITextProvider2",
    "ITextRangeProvider",
    "ITextRangeProvider2",
    "IToggleProvider",
    "ITransformProvider",
    "ITransformProvider2",
    "IUIAutomation",
    "IUIAutomation2",
    "IUIAutomation3",
    "IUIAutomation4",
    "IUIAutomation5",
    "IUIAutomation6",
    "IUIAutomationActiveTextPositionChangedEventHandler",
    "IUIAutomationAndCondition",
    "IUIAutomationAnnotationPattern",
    "IUIAutomationBoolCondition",
    "IUIAutomationCacheRequest",
    "IUIAutomationChangesEventHandler",
    "IUIAutomationCondition",
    "IUIAutomationCustomNavigationPattern",
    "IUIAutomationDockPattern",
    "IUIAutomationDragPattern",
    "IUIAutomationDropTargetPattern",
    "IUIAutomationElement",
    "IUIAutomationElement2",
    "IUIAutomationElement3",
    "IUIAutomationElement4",
    "IUIAutomationElement5",
    "IUIAutomationElement6",
    "IUIAutomationElement7",
    "IUIAutomationElement8",
    "IUIAutomationElement9",
    "IUIAutomationElementArray",
    "IUIAutomationEventHandler",
    "IUIAutomationEventHandlerGroup",
    "IUIAutomationExpandCollapsePattern",
    "IUIAutomationFocusChangedEventHandler",
    "IUIAutomationGridItemPattern",
    "IUIAutomationGridPattern",
    "IUIAutomationInvokePattern",
    "IUIAutomationItemContainerPattern",
    "IUIAutomationLegacyIAccessiblePattern",
    "IUIAutomationMultipleViewPattern",
    "IUIAutomationNotCondition",
    "IUIAutomationNotificationEventHandler",
    "IUIAutomationObjectModelPattern",
    "IUIAutomationOrCondition",
    "IUIAutomationPatternHandler",
    "IUIAutomationPatternInstance",
    "IUIAutomationPropertyChangedEventHandler",
    "IUIAutomationPropertyCondition",
    "IUIAutomationProxyFactory",
    "IUIAutomationProxyFactoryEntry",
    "IUIAutomationProxyFactoryMapping",
    "IUIAutomationRangeValuePattern",
    "IUIAutomationRegistrar",
    "IUIAutomationScrollItemPattern",
    "IUIAutomationScrollPattern",
    "IUIAutomationSelectionItemPattern",
    "IUIAutomationSelectionPattern",
    "IUIAutomationSelectionPattern2",
    "IUIAutomationSpreadsheetItemPattern",
    "IUIAutomationSpreadsheetPattern",
    "IUIAutomationStructureChangedEventHandler",
    "IUIAutomationStylesPattern",
    "IUIAutomationSynchronizedInputPattern",
    "IUIAutomationTableItemPattern",
    "IUIAutomationTablePattern",
    "IUIAutomationTextChildPattern",
    "IUIAutomationTextEditPattern",
    "IUIAutomationTextEditTextChangedEventHandler",
    "IUIAutomationTextPattern",
    "IUIAutomationTextPattern2",
    "IUIAutomationTextRange",
    "IUIAutomationTextRange2",
    "IUIAutomationTextRange3",
    "IUIAutomationTextRangeArray",
    "IUIAutomationTogglePattern",
    "IUIAutomationTransformPattern",
    "IUIAutomationTransformPattern2",
    "IUIAutomationTreeWalker",
    "IUIAutomationValuePattern",
    "IUIAutomationVirtualizedItemPattern",
    "IUIAutomationWindowPattern",
    "IValueProvider",
    "IVirtualizedItemProvider",
    "IWindowProvider",
    "Image_Control_GUID",
    "InputDiscarded_Event_GUID",
    "InputReachedOtherElement_Event_GUID",
    "InputReachedTarget_Event_GUID",
    "InvokePattern_Invoke",
    "Invoke_Invoked_Event_GUID",
    "Invoke_Pattern_GUID",
    "IsAnnotationPatternAvailable_Property_GUID",
    "IsContentElement_Property_GUID",
    "IsControlElement_Property_GUID",
    "IsCustomNavigationPatternAvailable_Property_GUID",
    "IsDataValidForForm_Property_GUID",
    "IsDialog_Property_GUID",
    "IsDockPatternAvailable_Property_GUID",
    "IsDragPatternAvailable_Property_GUID",
    "IsDropTargetPatternAvailable_Property_GUID",
    "IsEnabled_Property_GUID",
    "IsExpandCollapsePatternAvailable_Property_GUID",
    "IsGridItemPatternAvailable_Property_GUID",
    "IsGridPatternAvailable_Property_GUID",
    "IsInvokePatternAvailable_Property_GUID",
    "IsItemContainerPatternAvailable_Property_GUID",
    "IsKeyboardFocusable_Property_GUID",
    "IsLegacyIAccessiblePatternAvailable_Property_GUID",
    "IsMultipleViewPatternAvailable_Property_GUID",
    "IsObjectModelPatternAvailable_Property_GUID",
    "IsOffscreen_Property_GUID",
    "IsPassword_Property_GUID",
    "IsPeripheral_Property_GUID",
    "IsRangeValuePatternAvailable_Property_GUID",
    "IsRequiredForForm_Property_GUID",
    "IsScrollItemPatternAvailable_Property_GUID",
    "IsScrollPatternAvailable_Property_GUID",
    "IsSelectionItemPatternAvailable_Property_GUID",
    "IsSelectionPattern2Available_Property_GUID",
    "IsSelectionPatternAvailable_Property_GUID",
    "IsSpreadsheetItemPatternAvailable_Property_GUID",
    "IsSpreadsheetPatternAvailable_Property_GUID",
    "IsStructuredMarkupPatternAvailable_Property_GUID",
    "IsStylesPatternAvailable_Property_GUID",
    "IsSynchronizedInputPatternAvailable_Property_GUID",
    "IsTableItemPatternAvailable_Property_GUID",
    "IsTablePatternAvailable_Property_GUID",
    "IsTextChildPatternAvailable_Property_GUID",
    "IsTextEditPatternAvailable_Property_GUID",
    "IsTextPattern2Available_Property_GUID",
    "IsTextPatternAvailable_Property_GUID",
    "IsTogglePatternAvailable_Property_GUID",
    "IsTransformPattern2Available_Property_GUID",
    "IsTransformPatternAvailable_Property_GUID",
    "IsValuePatternAvailable_Property_GUID",
    "IsVirtualizedItemPatternAvailable_Property_GUID",
    "IsWinEventHookInstalled",
    "IsWindowPatternAvailable_Property_GUID",
    "ItemContainerPattern_FindItemByProperty",
    "ItemContainer_Pattern_GUID",
    "ItemStatus_Property_GUID",
    "ItemType_Property_GUID",
    "LIBID_Accessibility",
    "LPFNACCESSIBLECHILDREN",
    "LPFNACCESSIBLEOBJECTFROMPOINT",
    "LPFNACCESSIBLEOBJECTFROMWINDOW",
    "LPFNCREATESTDACCESSIBLEOBJECT",
    "LPFNLRESULTFROMOBJECT",
    "LPFNOBJECTFROMLRESULT",
    "LabeledBy_Property_GUID",
    "LandmarkType_Property_GUID",
    "LayoutInvalidated_Event_GUID",
    "LegacyIAccessiblePattern_DoDefaultAction",
    "LegacyIAccessiblePattern_GetIAccessible",
    "LegacyIAccessiblePattern_Select",
    "LegacyIAccessiblePattern_SetValue",
    "LegacyIAccessible_ChildId_Property_GUID",
    "LegacyIAccessible_DefaultAction_Property_GUID",
    "LegacyIAccessible_Description_Property_GUID",
    "LegacyIAccessible_Help_Property_GUID",
    "LegacyIAccessible_KeyboardShortcut_Property_GUID",
    "LegacyIAccessible_Name_Property_GUID",
    "LegacyIAccessible_Pattern_GUID",
    "LegacyIAccessible_Role_Property_GUID",
    "LegacyIAccessible_Selection_Property_GUID",
    "LegacyIAccessible_State_Property_GUID",
    "LegacyIAccessible_Value_Property_GUID",
    "Level_Property_GUID",
    "ListItem_Control_GUID",
    "List_Control_GUID",
    "LiveRegionChanged_Event_GUID",
    "LiveSetting",
    "LiveSetting_Assertive",
    "LiveSetting_Off",
    "LiveSetting_Polite",
    "LiveSetting_Property_GUID",
    "LocalizedControlType_Property_GUID",
    "LocalizedLandmarkType_Property_GUID",
    "LresultFromObject",
    "MOUSEKEYS",
    "MSAAMENUINFO",
    "MSAA_MENU_SIG",
    "MenuBar_Control_GUID",
    "MenuClosed_Event_GUID",
    "MenuItem_Control_GUID",
    "MenuModeEnd_Event_GUID",
    "MenuModeStart_Event_GUID",
    "MenuOpened_Event_GUID",
    "Menu_Control_GUID",
    "MultipleViewPattern_GetViewName",
    "MultipleViewPattern_SetCurrentView",
    "MultipleView_CurrentView_Property_GUID",
    "MultipleView_Pattern_GUID",
    "MultipleView_SupportedViews_Property_GUID",
    "NAVDIR_DOWN",
    "NAVDIR_FIRSTCHILD",
    "NAVDIR_LASTCHILD",
    "NAVDIR_LEFT",
    "NAVDIR_MAX",
    "NAVDIR_MIN",
    "NAVDIR_NEXT",
    "NAVDIR_PREVIOUS",
    "NAVDIR_RIGHT",
    "NAVDIR_UP",
    "Name_Property_GUID",
    "NavigateDirection",
    "NavigateDirection_FirstChild",
    "NavigateDirection_LastChild",
    "NavigateDirection_NextSibling",
    "NavigateDirection_Parent",
    "NavigateDirection_PreviousSibling",
    "NewNativeWindowHandle_Property_GUID",
    "NormalizeState",
    "NormalizeState_Custom",
    "NormalizeState_None",
    "NormalizeState_View",
    "NotificationKind",
    "NotificationKind_ActionAborted",
    "NotificationKind_ActionCompleted",
    "NotificationKind_ItemAdded",
    "NotificationKind_ItemRemoved",
    "NotificationKind_Other",
    "NotificationProcessing",
    "NotificationProcessing_All",
    "NotificationProcessing_CurrentThenMostRecent",
    "NotificationProcessing_ImportantAll",
    "NotificationProcessing_ImportantMostRecent",
    "NotificationProcessing_MostRecent",
    "Notification_Event_GUID",
    "NotifyWinEvent",
    "ObjectFromLresult",
    "ObjectModel_Pattern_GUID",
    "OptimizeForVisualContent_Property_GUID",
    "OrientationType",
    "OrientationType_Horizontal",
    "OrientationType_None",
    "OrientationType_Vertical",
    "Orientation_Property_GUID",
    "OutlineColor_Property_GUID",
    "OutlineStyles",
    "OutlineStyles_Embossed",
    "OutlineStyles_Engraved",
    "OutlineStyles_None",
    "OutlineStyles_Outline",
    "OutlineStyles_Shadow",
    "OutlineThickness_Property_GUID",
    "PROPID_ACC_DEFAULTACTION",
    "PROPID_ACC_DESCRIPTION",
    "PROPID_ACC_DESCRIPTIONMAP",
    "PROPID_ACC_DODEFAULTACTION",
    "PROPID_ACC_FOCUS",
    "PROPID_ACC_HELP",
    "PROPID_ACC_HELPTOPIC",
    "PROPID_ACC_KEYBOARDSHORTCUT",
    "PROPID_ACC_NAME",
    "PROPID_ACC_NAV_DOWN",
    "PROPID_ACC_NAV_FIRSTCHILD",
    "PROPID_ACC_NAV_LASTCHILD",
    "PROPID_ACC_NAV_LEFT",
    "PROPID_ACC_NAV_NEXT",
    "PROPID_ACC_NAV_PREV",
    "PROPID_ACC_NAV_RIGHT",
    "PROPID_ACC_NAV_UP",
    "PROPID_ACC_PARENT",
    "PROPID_ACC_ROLE",
    "PROPID_ACC_ROLEMAP",
    "PROPID_ACC_SELECTION",
    "PROPID_ACC_STATE",
    "PROPID_ACC_STATEMAP",
    "PROPID_ACC_VALUE",
    "PROPID_ACC_VALUEMAP",
    "Pane_Control_GUID",
    "PositionInSet_Property_GUID",
    "ProcessId_Property_GUID",
    "ProgressBar_Control_GUID",
    "PropertyConditionFlags",
    "PropertyConditionFlags_IgnoreCase",
    "PropertyConditionFlags_MatchSubstring",
    "PropertyConditionFlags_None",
    "ProviderDescription_Property_GUID",
    "ProviderOptions",
    "ProviderOptions_ClientSideProvider",
    "ProviderOptions_HasNativeIAccessible",
    "ProviderOptions_NonClientAreaProvider",
    "ProviderOptions_OverrideProvider",
    "ProviderOptions_ProviderOwnsSetFocus",
    "ProviderOptions_RefuseNonClientSupport",
    "ProviderOptions_ServerSideProvider",
    "ProviderOptions_UseClientCoordinates",
    "ProviderOptions_UseComThreading",
    "ProviderType",
    "ProviderType_BaseHwnd",
    "ProviderType_NonClientArea",
    "ProviderType_Proxy",
    "ROLE_SYSTEM_ALERT",
    "ROLE_SYSTEM_ANIMATION",
    "ROLE_SYSTEM_APPLICATION",
    "ROLE_SYSTEM_BORDER",
    "ROLE_SYSTEM_BUTTONDROPDOWN",
    "ROLE_SYSTEM_BUTTONDROPDOWNGRID",
    "ROLE_SYSTEM_BUTTONMENU",
    "ROLE_SYSTEM_CARET",
    "ROLE_SYSTEM_CELL",
    "ROLE_SYSTEM_CHARACTER",
    "ROLE_SYSTEM_CHART",
    "ROLE_SYSTEM_CHECKBUTTON",
    "ROLE_SYSTEM_CLIENT",
    "ROLE_SYSTEM_CLOCK",
    "ROLE_SYSTEM_COLUMN",
    "ROLE_SYSTEM_COLUMNHEADER",
    "ROLE_SYSTEM_COMBOBOX",
    "ROLE_SYSTEM_CURSOR",
    "ROLE_SYSTEM_DIAGRAM",
    "ROLE_SYSTEM_DIAL",
    "ROLE_SYSTEM_DIALOG",
    "ROLE_SYSTEM_DOCUMENT",
    "ROLE_SYSTEM_DROPLIST",
    "ROLE_SYSTEM_EQUATION",
    "ROLE_SYSTEM_GRAPHIC",
    "ROLE_SYSTEM_GRIP",
    "ROLE_SYSTEM_GROUPING",
    "ROLE_SYSTEM_HELPBALLOON",
    "ROLE_SYSTEM_HOTKEYFIELD",
    "ROLE_SYSTEM_INDICATOR",
    "ROLE_SYSTEM_IPADDRESS",
    "ROLE_SYSTEM_LINK",
    "ROLE_SYSTEM_LIST",
    "ROLE_SYSTEM_LISTITEM",
    "ROLE_SYSTEM_MENUBAR",
    "ROLE_SYSTEM_MENUITEM",
    "ROLE_SYSTEM_MENUPOPUP",
    "ROLE_SYSTEM_OUTLINE",
    "ROLE_SYSTEM_OUTLINEBUTTON",
    "ROLE_SYSTEM_OUTLINEITEM",
    "ROLE_SYSTEM_PAGETAB",
    "ROLE_SYSTEM_PAGETABLIST",
    "ROLE_SYSTEM_PANE",
    "ROLE_SYSTEM_PROGRESSBAR",
    "ROLE_SYSTEM_PROPERTYPAGE",
    "ROLE_SYSTEM_PUSHBUTTON",
    "ROLE_SYSTEM_RADIOBUTTON",
    "ROLE_SYSTEM_ROW",
    "ROLE_SYSTEM_ROWHEADER",
    "ROLE_SYSTEM_SCROLLBAR",
    "ROLE_SYSTEM_SEPARATOR",
    "ROLE_SYSTEM_SLIDER",
    "ROLE_SYSTEM_SOUND",
    "ROLE_SYSTEM_SPINBUTTON",
    "ROLE_SYSTEM_SPLITBUTTON",
    "ROLE_SYSTEM_STATICTEXT",
    "ROLE_SYSTEM_STATUSBAR",
    "ROLE_SYSTEM_TABLE",
    "ROLE_SYSTEM_TEXT",
    "ROLE_SYSTEM_TITLEBAR",
    "ROLE_SYSTEM_TOOLBAR",
    "ROLE_SYSTEM_TOOLTIP",
    "ROLE_SYSTEM_WHITESPACE",
    "ROLE_SYSTEM_WINDOW",
    "RadioButton_Control_GUID",
    "RangeValuePattern_SetValue",
    "RangeValue_IsReadOnly_Property_GUID",
    "RangeValue_LargeChange_Property_GUID",
    "RangeValue_Maximum_Property_GUID",
    "RangeValue_Minimum_Property_GUID",
    "RangeValue_Pattern_GUID",
    "RangeValue_SmallChange_Property_GUID",
    "RangeValue_Value_Property_GUID",
    "RegisterPointerInputTarget",
    "RegisterPointerInputTargetEx",
    "Rotation_Property_GUID",
    "RowOrColumnMajor",
    "RowOrColumnMajor_ColumnMajor",
    "RowOrColumnMajor_Indeterminate",
    "RowOrColumnMajor_RowMajor",
    "RuntimeId_Property_GUID",
    "SELFLAG_ADDSELECTION",
    "SELFLAG_EXTENDSELECTION",
    "SELFLAG_NONE",
    "SELFLAG_REMOVESELECTION",
    "SELFLAG_TAKEFOCUS",
    "SELFLAG_TAKESELECTION",
    "SELFLAG_VALID",
    "SERIALKEYSA",
    "SERIALKEYSW",
    "SERIALKEYS_FLAGS",
    "SERKF_AVAILABLE",
    "SERKF_INDICATOR",
    "SERKF_SERIALKEYSON",
    "SID_ControlElementProvider",
    "SID_IsUIAutomationObject",
    "SKF_AUDIBLEFEEDBACK",
    "SKF_AVAILABLE",
    "SKF_CONFIRMHOTKEY",
    "SKF_HOTKEYACTIVE",
    "SKF_HOTKEYSOUND",
    "SKF_INDICATOR",
    "SKF_LALTLATCHED",
    "SKF_LALTLOCKED",
    "SKF_LCTLLATCHED",
    "SKF_LCTLLOCKED",
    "SKF_LSHIFTLATCHED",
    "SKF_LSHIFTLOCKED",
    "SKF_LWINLATCHED",
    "SKF_LWINLOCKED",
    "SKF_RALTLATCHED",
    "SKF_RALTLOCKED",
    "SKF_RCTLLATCHED",
    "SKF_RCTLLOCKED",
    "SKF_RSHIFTLATCHED",
    "SKF_RSHIFTLOCKED",
    "SKF_RWINLATCHED",
    "SKF_RWINLOCKED",
    "SKF_STICKYKEYSON",
    "SKF_TRISTATE",
    "SKF_TWOKEYSOFF",
    "SOUNDSENTRYA",
    "SOUNDSENTRYW",
    "SOUNDSENTRY_FLAGS",
    "SOUNDSENTRY_TEXT_EFFECT",
    "SOUNDSENTRY_WINDOWS_EFFECT",
    "SOUND_SENTRY_GRAPHICS_EFFECT",
    "SSF_AVAILABLE",
    "SSF_INDICATOR",
    "SSF_SOUNDSENTRYON",
    "SSGF_DISPLAY",
    "SSGF_NONE",
    "SSTF_BORDER",
    "SSTF_CHARS",
    "SSTF_DISPLAY",
    "SSTF_NONE",
    "SSWF_CUSTOM",
    "SSWF_DISPLAY",
    "SSWF_NONE",
    "SSWF_TITLE",
    "SSWF_WINDOW",
    "STATE_SYSTEM_HASPOPUP",
    "STATE_SYSTEM_NORMAL",
    "STICKYKEYS",
    "STICKYKEYS_FLAGS",
    "SayAsInterpretAs",
    "SayAsInterpretAs_Address",
    "SayAsInterpretAs_Alphanumeric",
    "SayAsInterpretAs_Cardinal",
    "SayAsInterpretAs_Currency",
    "SayAsInterpretAs_Date",
    "SayAsInterpretAs_Date_DayMonth",
    "SayAsInterpretAs_Date_DayMonthYear",
    "SayAsInterpretAs_Date_MonthDay",
    "SayAsInterpretAs_Date_MonthDayYear",
    "SayAsInterpretAs_Date_MonthYear",
    "SayAsInterpretAs_Date_Year",
    "SayAsInterpretAs_Date_YearMonth",
    "SayAsInterpretAs_Date_YearMonthDay",
    "SayAsInterpretAs_Media",
    "SayAsInterpretAs_Name",
    "SayAsInterpretAs_Net",
    "SayAsInterpretAs_None",
    "SayAsInterpretAs_Number",
    "SayAsInterpretAs_Ordinal",
    "SayAsInterpretAs_Spell",
    "SayAsInterpretAs_Telephone",
    "SayAsInterpretAs_Time",
    "SayAsInterpretAs_Time_HoursMinutes12",
    "SayAsInterpretAs_Time_HoursMinutes24",
    "SayAsInterpretAs_Time_HoursMinutesSeconds12",
    "SayAsInterpretAs_Time_HoursMinutesSeconds24",
    "SayAsInterpretAs_Url",
    "ScrollAmount",
    "ScrollAmount_LargeDecrement",
    "ScrollAmount_LargeIncrement",
    "ScrollAmount_NoAmount",
    "ScrollAmount_SmallDecrement",
    "ScrollAmount_SmallIncrement",
    "ScrollBar_Control_GUID",
    "ScrollItemPattern_ScrollIntoView",
    "ScrollItem_Pattern_GUID",
    "ScrollPattern_Scroll",
    "ScrollPattern_SetScrollPercent",
    "Scroll_HorizontalScrollPercent_Property_GUID",
    "Scroll_HorizontalViewSize_Property_GUID",
    "Scroll_HorizontallyScrollable_Property_GUID",
    "Scroll_Pattern_GUID",
    "Scroll_VerticalScrollPercent_Property_GUID",
    "Scroll_VerticalViewSize_Property_GUID",
    "Scroll_VerticallyScrollable_Property_GUID",
    "Selection2_CurrentSelectedItem_Property_GUID",
    "Selection2_FirstSelectedItem_Property_GUID",
    "Selection2_ItemCount_Property_GUID",
    "Selection2_LastSelectedItem_Property_GUID",
    "SelectionItemPattern_AddToSelection",
    "SelectionItemPattern_RemoveFromSelection",
    "SelectionItemPattern_Select",
    "SelectionItem_ElementAddedToSelectionEvent_Event_GUID",
    "SelectionItem_ElementRemovedFromSelectionEvent_Event_GUID",
    "SelectionItem_ElementSelectedEvent_Event_GUID",
    "SelectionItem_IsSelected_Property_GUID",
    "SelectionItem_Pattern_GUID",
    "SelectionItem_SelectionContainer_Property_GUID",
    "Selection_CanSelectMultiple_Property_GUID",
    "Selection_InvalidatedEvent_Event_GUID",
    "Selection_IsSelectionRequired_Property_GUID",
    "Selection_Pattern2_GUID",
    "Selection_Pattern_GUID",
    "Selection_Selection_Property_GUID",
    "SemanticZoom_Control_GUID",
    "Separator_Control_GUID",
    "SetWinEventHook",
    "SizeOfSet_Property_GUID",
    "Size_Property_GUID",
    "Slider_Control_GUID",
    "Spinner_Control_GUID",
    "SplitButton_Control_GUID",
    "SpreadsheetItem_AnnotationObjects_Property_GUID",
    "SpreadsheetItem_AnnotationTypes_Property_GUID",
    "SpreadsheetItem_Formula_Property_GUID",
    "SpreadsheetItem_Pattern_GUID",
    "Spreadsheet_Pattern_GUID",
    "StatusBar_Control_GUID",
    "StructureChangeType",
    "StructureChangeType_ChildAdded",
    "StructureChangeType_ChildRemoved",
    "StructureChangeType_ChildrenBulkAdded",
    "StructureChangeType_ChildrenBulkRemoved",
    "StructureChangeType_ChildrenInvalidated",
    "StructureChangeType_ChildrenReordered",
    "StructureChanged_Event_GUID",
    "StructuredMarkup_CompositionComplete_Event_GUID",
    "StructuredMarkup_Deleted_Event_GUID",
    "StructuredMarkup_Pattern_GUID",
    "StructuredMarkup_SelectionChanged_Event_GUID",
    "StyleId_BulletedList",
    "StyleId_BulletedList_GUID",
    "StyleId_Custom",
    "StyleId_Custom_GUID",
    "StyleId_Emphasis",
    "StyleId_Emphasis_GUID",
    "StyleId_Heading1",
    "StyleId_Heading1_GUID",
    "StyleId_Heading2",
    "StyleId_Heading2_GUID",
    "StyleId_Heading3",
    "StyleId_Heading3_GUID",
    "StyleId_Heading4",
    "StyleId_Heading4_GUID",
    "StyleId_Heading5",
    "StyleId_Heading5_GUID",
    "StyleId_Heading6",
    "StyleId_Heading6_GUID",
    "StyleId_Heading7",
    "StyleId_Heading7_GUID",
    "StyleId_Heading8",
    "StyleId_Heading8_GUID",
    "StyleId_Heading9",
    "StyleId_Heading9_GUID",
    "StyleId_Normal",
    "StyleId_Normal_GUID",
    "StyleId_NumberedList",
    "StyleId_NumberedList_GUID",
    "StyleId_Quote",
    "StyleId_Quote_GUID",
    "StyleId_Subtitle",
    "StyleId_Subtitle_GUID",
    "StyleId_Title",
    "StyleId_Title_GUID",
    "Styles_ExtendedProperties_Property_GUID",
    "Styles_FillColor_Property_GUID",
    "Styles_FillPatternColor_Property_GUID",
    "Styles_FillPatternStyle_Property_GUID",
    "Styles_Pattern_GUID",
    "Styles_Shape_Property_GUID",
    "Styles_StyleId_Property_GUID",
    "Styles_StyleName_Property_GUID",
    "SupportedTextSelection",
    "SupportedTextSelection_Multiple",
    "SupportedTextSelection_None",
    "SupportedTextSelection_Single",
    "SynchronizedInputPattern_Cancel",
    "SynchronizedInputPattern_StartListening",
    "SynchronizedInputType",
    "SynchronizedInputType_KeyDown",
    "SynchronizedInputType_KeyUp",
    "SynchronizedInputType_LeftMouseDown",
    "SynchronizedInputType_LeftMouseUp",
    "SynchronizedInputType_RightMouseDown",
    "SynchronizedInputType_RightMouseUp",
    "SynchronizedInput_Pattern_GUID",
    "SystemAlert_Event_GUID",
    "TOGGLEKEYS",
    "TabItem_Control_GUID",
    "Tab_Control_GUID",
    "TableItem_ColumnHeaderItems_Property_GUID",
    "TableItem_Pattern_GUID",
    "TableItem_RowHeaderItems_Property_GUID",
    "Table_ColumnHeaders_Property_GUID",
    "Table_Control_GUID",
    "Table_Pattern_GUID",
    "Table_RowHeaders_Property_GUID",
    "Table_RowOrColumnMajor_Property_GUID",
    "TextChild_Pattern_GUID",
    "TextDecorationLineStyle",
    "TextDecorationLineStyle_Dash",
    "TextDecorationLineStyle_DashDot",
    "TextDecorationLineStyle_DashDotDot",
    "TextDecorationLineStyle_Dot",
    "TextDecorationLineStyle_Double",
    "TextDecorationLineStyle_DoubleWavy",
    "TextDecorationLineStyle_LongDash",
    "TextDecorationLineStyle_None",
    "TextDecorationLineStyle_Other",
    "TextDecorationLineStyle_Single",
    "TextDecorationLineStyle_ThickDash",
    "TextDecorationLineStyle_ThickDashDot",
    "TextDecorationLineStyle_ThickDashDotDot",
    "TextDecorationLineStyle_ThickDot",
    "TextDecorationLineStyle_ThickLongDash",
    "TextDecorationLineStyle_ThickSingle",
    "TextDecorationLineStyle_ThickWavy",
    "TextDecorationLineStyle_Wavy",
    "TextDecorationLineStyle_WordsOnly",
    "TextEditChangeType",
    "TextEditChangeType_AutoComplete",
    "TextEditChangeType_AutoCorrect",
    "TextEditChangeType_Composition",
    "TextEditChangeType_CompositionFinalized",
    "TextEditChangeType_None",
    "TextEdit_ConversionTargetChanged_Event_GUID",
    "TextEdit_Pattern_GUID",
    "TextEdit_TextChanged_Event_GUID",
    "TextPatternRangeEndpoint",
    "TextPatternRangeEndpoint_End",
    "TextPatternRangeEndpoint_Start",
    "TextPattern_GetSelection",
    "TextPattern_GetVisibleRanges",
    "TextPattern_RangeFromChild",
    "TextPattern_RangeFromPoint",
    "TextPattern_get_DocumentRange",
    "TextPattern_get_SupportedTextSelection",
    "TextRange_AddToSelection",
    "TextRange_Clone",
    "TextRange_Compare",
    "TextRange_CompareEndpoints",
    "TextRange_ExpandToEnclosingUnit",
    "TextRange_FindAttribute",
    "TextRange_FindText",
    "TextRange_GetAttributeValue",
    "TextRange_GetBoundingRectangles",
    "TextRange_GetChildren",
    "TextRange_GetEnclosingElement",
    "TextRange_GetText",
    "TextRange_Move",
    "TextRange_MoveEndpointByRange",
    "TextRange_MoveEndpointByUnit",
    "TextRange_RemoveFromSelection",
    "TextRange_ScrollIntoView",
    "TextRange_Select",
    "TextUnit",
    "TextUnit_Character",
    "TextUnit_Document",
    "TextUnit_Format",
    "TextUnit_Line",
    "TextUnit_Page",
    "TextUnit_Paragraph",
    "TextUnit_Word",
    "Text_AfterParagraphSpacing_Attribute_GUID",
    "Text_AfterSpacing_Attribute_GUID",
    "Text_AnimationStyle_Attribute_GUID",
    "Text_AnnotationObjects_Attribute_GUID",
    "Text_AnnotationTypes_Attribute_GUID",
    "Text_BackgroundColor_Attribute_GUID",
    "Text_BeforeParagraphSpacing_Attribute_GUID",
    "Text_BeforeSpacing_Attribute_GUID",
    "Text_BulletStyle_Attribute_GUID",
    "Text_CapStyle_Attribute_GUID",
    "Text_CaretBidiMode_Attribute_GUID",
    "Text_CaretPosition_Attribute_GUID",
    "Text_Control_GUID",
    "Text_Culture_Attribute_GUID",
    "Text_FontName_Attribute_GUID",
    "Text_FontSize_Attribute_GUID",
    "Text_FontWeight_Attribute_GUID",
    "Text_ForegroundColor_Attribute_GUID",
    "Text_HorizontalTextAlignment_Attribute_GUID",
    "Text_IndentationFirstLine_Attribute_GUID",
    "Text_IndentationLeading_Attribute_GUID",
    "Text_IndentationTrailing_Attribute_GUID",
    "Text_IsActive_Attribute_GUID",
    "Text_IsHidden_Attribute_GUID",
    "Text_IsItalic_Attribute_GUID",
    "Text_IsReadOnly_Attribute_GUID",
    "Text_IsSubscript_Attribute_GUID",
    "Text_IsSuperscript_Attribute_GUID",
    "Text_LineSpacing_Attribute_GUID",
    "Text_Link_Attribute_GUID",
    "Text_MarginBottom_Attribute_GUID",
    "Text_MarginLeading_Attribute_GUID",
    "Text_MarginTop_Attribute_GUID",
    "Text_MarginTrailing_Attribute_GUID",
    "Text_OutlineStyles_Attribute_GUID",
    "Text_OverlineColor_Attribute_GUID",
    "Text_OverlineStyle_Attribute_GUID",
    "Text_Pattern2_GUID",
    "Text_Pattern_GUID",
    "Text_SayAsInterpretAs_Attribute_GUID",
    "Text_SelectionActiveEnd_Attribute_GUID",
    "Text_StrikethroughColor_Attribute_GUID",
    "Text_StrikethroughStyle_Attribute_GUID",
    "Text_StyleId_Attribute_GUID",
    "Text_StyleName_Attribute_GUID",
    "Text_Tabs_Attribute_GUID",
    "Text_TextChangedEvent_Event_GUID",
    "Text_TextFlowDirections_Attribute_GUID",
    "Text_TextSelectionChangedEvent_Event_GUID",
    "Text_UnderlineColor_Attribute_GUID",
    "Text_UnderlineStyle_Attribute_GUID",
    "Thumb_Control_GUID",
    "TitleBar_Control_GUID",
    "TogglePattern_Toggle",
    "ToggleState",
    "ToggleState_Indeterminate",
    "ToggleState_Off",
    "ToggleState_On",
    "Toggle_Pattern_GUID",
    "Toggle_ToggleState_Property_GUID",
    "ToolBar_Control_GUID",
    "ToolTipClosed_Event_GUID",
    "ToolTipOpened_Event_GUID",
    "ToolTip_Control_GUID",
    "Tranform_Pattern2_GUID",
    "Transform2_CanZoom_Property_GUID",
    "Transform2_ZoomLevel_Property_GUID",
    "Transform2_ZoomMaximum_Property_GUID",
    "Transform2_ZoomMinimum_Property_GUID",
    "TransformPattern_Move",
    "TransformPattern_Resize",
    "TransformPattern_Rotate",
    "Transform_CanMove_Property_GUID",
    "Transform_CanResize_Property_GUID",
    "Transform_CanRotate_Property_GUID",
    "Transform_Pattern_GUID",
    "TreeItem_Control_GUID",
    "TreeScope",
    "TreeScope_Ancestors",
    "TreeScope_Children",
    "TreeScope_Descendants",
    "TreeScope_Element",
    "TreeScope_None",
    "TreeScope_Parent",
    "TreeScope_Subtree",
    "TreeTraversalOptions",
    "TreeTraversalOptions_Default",
    "TreeTraversalOptions_LastToFirstOrder",
    "TreeTraversalOptions_PostOrder",
    "Tree_Control_GUID",
    "UIA_ANNOTATIONTYPE",
    "UIA_AcceleratorKeyPropertyId",
    "UIA_AccessKeyPropertyId",
    "UIA_ActiveTextPositionChangedEventId",
    "UIA_AfterParagraphSpacingAttributeId",
    "UIA_AnimationStyleAttributeId",
    "UIA_AnnotationAnnotationTypeIdPropertyId",
    "UIA_AnnotationAnnotationTypeNamePropertyId",
    "UIA_AnnotationAuthorPropertyId",
    "UIA_AnnotationDateTimePropertyId",
    "UIA_AnnotationObjectsAttributeId",
    "UIA_AnnotationObjectsPropertyId",
    "UIA_AnnotationPatternId",
    "UIA_AnnotationTargetPropertyId",
    "UIA_AnnotationTypesAttributeId",
    "UIA_AnnotationTypesPropertyId",
    "UIA_AppBarControlTypeId",
    "UIA_AriaPropertiesPropertyId",
    "UIA_AriaRolePropertyId",
    "UIA_AsyncContentLoadedEventId",
    "UIA_AutomationFocusChangedEventId",
    "UIA_AutomationIdPropertyId",
    "UIA_AutomationPropertyChangedEventId",
    "UIA_BackgroundColorAttributeId",
    "UIA_BeforeParagraphSpacingAttributeId",
    "UIA_BoundingRectanglePropertyId",
    "UIA_BulletStyleAttributeId",
    "UIA_ButtonControlTypeId",
    "UIA_CHANGE_ID",
    "UIA_CONTROLTYPE_ID",
    "UIA_CalendarControlTypeId",
    "UIA_CapStyleAttributeId",
    "UIA_CaretBidiModeAttributeId",
    "UIA_CaretPositionAttributeId",
    "UIA_CenterPointPropertyId",
    "UIA_ChangesEventId",
    "UIA_CheckBoxControlTypeId",
    "UIA_ClassNamePropertyId",
    "UIA_ClickablePointPropertyId",
    "UIA_ComboBoxControlTypeId",
    "UIA_ControlTypePropertyId",
    "UIA_ControllerForPropertyId",
    "UIA_CultureAttributeId",
    "UIA_CulturePropertyId",
    "UIA_CustomControlTypeId",
    "UIA_CustomLandmarkTypeId",
    "UIA_CustomNavigationPatternId",
    "UIA_DataGridControlTypeId",
    "UIA_DataItemControlTypeId",
    "UIA_DescribedByPropertyId",
    "UIA_DockDockPositionPropertyId",
    "UIA_DockPatternId",
    "UIA_DocumentControlTypeId",
    "UIA_DragDropEffectPropertyId",
    "UIA_DragDropEffectsPropertyId",
    "UIA_DragGrabbedItemsPropertyId",
    "UIA_DragIsGrabbedPropertyId",
    "UIA_DragPatternId",
    "UIA_Drag_DragCancelEventId",
    "UIA_Drag_DragCompleteEventId",
    "UIA_Drag_DragStartEventId",
    "UIA_DropTargetDropTargetEffectPropertyId",
    "UIA_DropTargetDropTargetEffectsPropertyId",
    "UIA_DropTargetPatternId",
    "UIA_DropTarget_DragEnterEventId",
    "UIA_DropTarget_DragLeaveEventId",
    "UIA_DropTarget_DroppedEventId",
    "UIA_EVENT_ID",
    "UIA_E_ELEMENTNOTAVAILABLE",
    "UIA_E_ELEMENTNOTENABLED",
    "UIA_E_INVALIDOPERATION",
    "UIA_E_NOCLICKABLEPOINT",
    "UIA_E_NOTSUPPORTED",
    "UIA_E_PROXYASSEMBLYNOTLOADED",
    "UIA_E_TIMEOUT",
    "UIA_EditControlTypeId",
    "UIA_ExpandCollapseExpandCollapseStatePropertyId",
    "UIA_ExpandCollapsePatternId",
    "UIA_FillColorPropertyId",
    "UIA_FillTypePropertyId",
    "UIA_FlowsFromPropertyId",
    "UIA_FlowsToPropertyId",
    "UIA_FontNameAttributeId",
    "UIA_FontSizeAttributeId",
    "UIA_FontWeightAttributeId",
    "UIA_ForegroundColorAttributeId",
    "UIA_FormLandmarkTypeId",
    "UIA_FrameworkIdPropertyId",
    "UIA_FullDescriptionPropertyId",
    "UIA_GridColumnCountPropertyId",
    "UIA_GridItemColumnPropertyId",
    "UIA_GridItemColumnSpanPropertyId",
    "UIA_GridItemContainingGridPropertyId",
    "UIA_GridItemPatternId",
    "UIA_GridItemRowPropertyId",
    "UIA_GridItemRowSpanPropertyId",
    "UIA_GridPatternId",
    "UIA_GridRowCountPropertyId",
    "UIA_GroupControlTypeId",
    "UIA_HEADINGLEVEL_ID",
    "UIA_HEADINGLEVEL_ID_HeadingLevel1",
    "UIA_HEADINGLEVEL_ID_HeadingLevel2",
    "UIA_HEADINGLEVEL_ID_HeadingLevel3",
    "UIA_HEADINGLEVEL_ID_HeadingLevel4",
    "UIA_HEADINGLEVEL_ID_HeadingLevel5",
    "UIA_HEADINGLEVEL_ID_HeadingLevel6",
    "UIA_HEADINGLEVEL_ID_HeadingLevel7",
    "UIA_HEADINGLEVEL_ID_HeadingLevel8",
    "UIA_HEADINGLEVEL_ID_HeadingLevel9",
    "UIA_HEADINGLEVEL_ID_HeadingLevel_None",
    "UIA_HasKeyboardFocusPropertyId",
    "UIA_HeaderControlTypeId",
    "UIA_HeaderItemControlTypeId",
    "UIA_HeadingLevelPropertyId",
    "UIA_HelpTextPropertyId",
    "UIA_HorizontalTextAlignmentAttributeId",
    "UIA_HostedFragmentRootsInvalidatedEventId",
    "UIA_HyperlinkControlTypeId",
    "UIA_IAFP_DEFAULT",
    "UIA_IAFP_UNWRAP_BRIDGE",
    "UIA_ImageControlTypeId",
    "UIA_IndentationFirstLineAttributeId",
    "UIA_IndentationLeadingAttributeId",
    "UIA_IndentationTrailingAttributeId",
    "UIA_InputDiscardedEventId",
    "UIA_InputReachedOtherElementEventId",
    "UIA_InputReachedTargetEventId",
    "UIA_InvokePatternId",
    "UIA_Invoke_InvokedEventId",
    "UIA_IsActiveAttributeId",
    "UIA_IsAnnotationPatternAvailablePropertyId",
    "UIA_IsContentElementPropertyId",
    "UIA_IsControlElementPropertyId",
    "UIA_IsCustomNavigationPatternAvailablePropertyId",
    "UIA_IsDataValidForFormPropertyId",
    "UIA_IsDialogPropertyId",
    "UIA_IsDockPatternAvailablePropertyId",
    "UIA_IsDragPatternAvailablePropertyId",
    "UIA_IsDropTargetPatternAvailablePropertyId",
    "UIA_IsEnabledPropertyId",
    "UIA_IsExpandCollapsePatternAvailablePropertyId",
    "UIA_IsGridItemPatternAvailablePropertyId",
    "UIA_IsGridPatternAvailablePropertyId",
    "UIA_IsHiddenAttributeId",
    "UIA_IsInvokePatternAvailablePropertyId",
    "UIA_IsItalicAttributeId",
    "UIA_IsItemContainerPatternAvailablePropertyId",
    "UIA_IsKeyboardFocusablePropertyId",
    "UIA_IsLegacyIAccessiblePatternAvailablePropertyId",
    "UIA_IsMultipleViewPatternAvailablePropertyId",
    "UIA_IsObjectModelPatternAvailablePropertyId",
    "UIA_IsOffscreenPropertyId",
    "UIA_IsPasswordPropertyId",
    "UIA_IsPeripheralPropertyId",
    "UIA_IsRangeValuePatternAvailablePropertyId",
    "UIA_IsReadOnlyAttributeId",
    "UIA_IsRequiredForFormPropertyId",
    "UIA_IsScrollItemPatternAvailablePropertyId",
    "UIA_IsScrollPatternAvailablePropertyId",
    "UIA_IsSelectionItemPatternAvailablePropertyId",
    "UIA_IsSelectionPattern2AvailablePropertyId",
    "UIA_IsSelectionPatternAvailablePropertyId",
    "UIA_IsSpreadsheetItemPatternAvailablePropertyId",
    "UIA_IsSpreadsheetPatternAvailablePropertyId",
    "UIA_IsStylesPatternAvailablePropertyId",
    "UIA_IsSubscriptAttributeId",
    "UIA_IsSuperscriptAttributeId",
    "UIA_IsSynchronizedInputPatternAvailablePropertyId",
    "UIA_IsTableItemPatternAvailablePropertyId",
    "UIA_IsTablePatternAvailablePropertyId",
    "UIA_IsTextChildPatternAvailablePropertyId",
    "UIA_IsTextEditPatternAvailablePropertyId",
    "UIA_IsTextPattern2AvailablePropertyId",
    "UIA_IsTextPatternAvailablePropertyId",
    "UIA_IsTogglePatternAvailablePropertyId",
    "UIA_IsTransformPattern2AvailablePropertyId",
    "UIA_IsTransformPatternAvailablePropertyId",
    "UIA_IsValuePatternAvailablePropertyId",
    "UIA_IsVirtualizedItemPatternAvailablePropertyId",
    "UIA_IsWindowPatternAvailablePropertyId",
    "UIA_ItemContainerPatternId",
    "UIA_ItemStatusPropertyId",
    "UIA_ItemTypePropertyId",
    "UIA_LANDMARKTYPE_ID",
    "UIA_LabeledByPropertyId",
    "UIA_LandmarkTypePropertyId",
    "UIA_LayoutInvalidatedEventId",
    "UIA_LegacyIAccessibleChildIdPropertyId",
    "UIA_LegacyIAccessibleDefaultActionPropertyId",
    "UIA_LegacyIAccessibleDescriptionPropertyId",
    "UIA_LegacyIAccessibleHelpPropertyId",
    "UIA_LegacyIAccessibleKeyboardShortcutPropertyId",
    "UIA_LegacyIAccessibleNamePropertyId",
    "UIA_LegacyIAccessiblePatternId",
    "UIA_LegacyIAccessibleRolePropertyId",
    "UIA_LegacyIAccessibleSelectionPropertyId",
    "UIA_LegacyIAccessibleStatePropertyId",
    "UIA_LegacyIAccessibleValuePropertyId",
    "UIA_LevelPropertyId",
    "UIA_LineSpacingAttributeId",
    "UIA_LinkAttributeId",
    "UIA_ListControlTypeId",
    "UIA_ListItemControlTypeId",
    "UIA_LiveRegionChangedEventId",
    "UIA_LiveSettingPropertyId",
    "UIA_LocalizedControlTypePropertyId",
    "UIA_LocalizedLandmarkTypePropertyId",
    "UIA_METADATA_ID",
    "UIA_MainLandmarkTypeId",
    "UIA_MarginBottomAttributeId",
    "UIA_MarginLeadingAttributeId",
    "UIA_MarginTopAttributeId",
    "UIA_MarginTrailingAttributeId",
    "UIA_MenuBarControlTypeId",
    "UIA_MenuClosedEventId",
    "UIA_MenuControlTypeId",
    "UIA_MenuItemControlTypeId",
    "UIA_MenuModeEndEventId",
    "UIA_MenuModeStartEventId",
    "UIA_MenuOpenedEventId",
    "UIA_MultipleViewCurrentViewPropertyId",
    "UIA_MultipleViewPatternId",
    "UIA_MultipleViewSupportedViewsPropertyId",
    "UIA_NamePropertyId",
    "UIA_NativeWindowHandlePropertyId",
    "UIA_NavigationLandmarkTypeId",
    "UIA_NotificationEventId",
    "UIA_ObjectModelPatternId",
    "UIA_OptimizeForVisualContentPropertyId",
    "UIA_OrientationPropertyId",
    "UIA_OutlineColorPropertyId",
    "UIA_OutlineStylesAttributeId",
    "UIA_OutlineThicknessPropertyId",
    "UIA_OverlineColorAttributeId",
    "UIA_OverlineStyleAttributeId",
    "UIA_PATTERN_ID",
    "UIA_PFIA_DEFAULT",
    "UIA_PFIA_UNWRAP_BRIDGE",
    "UIA_PROPERTY_ID",
    "UIA_PaneControlTypeId",
    "UIA_PositionInSetPropertyId",
    "UIA_ProcessIdPropertyId",
    "UIA_ProgressBarControlTypeId",
    "UIA_ProviderDescriptionPropertyId",
    "UIA_RadioButtonControlTypeId",
    "UIA_RangeValueIsReadOnlyPropertyId",
    "UIA_RangeValueLargeChangePropertyId",
    "UIA_RangeValueMaximumPropertyId",
    "UIA_RangeValueMinimumPropertyId",
    "UIA_RangeValuePatternId",
    "UIA_RangeValueSmallChangePropertyId",
    "UIA_RangeValueValuePropertyId",
    "UIA_RotationPropertyId",
    "UIA_RuntimeIdPropertyId",
    "UIA_STYLE_ID",
    "UIA_SayAsInterpretAsAttributeId",
    "UIA_SayAsInterpretAsMetadataId",
    "UIA_ScrollBarControlTypeId",
    "UIA_ScrollHorizontalScrollPercentPropertyId",
    "UIA_ScrollHorizontalViewSizePropertyId",
    "UIA_ScrollHorizontallyScrollablePropertyId",
    "UIA_ScrollItemPatternId",
    "UIA_ScrollPatternId",
    "UIA_ScrollPatternNoScroll",
    "UIA_ScrollVerticalScrollPercentPropertyId",
    "UIA_ScrollVerticalViewSizePropertyId",
    "UIA_ScrollVerticallyScrollablePropertyId",
    "UIA_SearchLandmarkTypeId",
    "UIA_Selection2CurrentSelectedItemPropertyId",
    "UIA_Selection2FirstSelectedItemPropertyId",
    "UIA_Selection2ItemCountPropertyId",
    "UIA_Selection2LastSelectedItemPropertyId",
    "UIA_SelectionActiveEndAttributeId",
    "UIA_SelectionCanSelectMultiplePropertyId",
    "UIA_SelectionIsSelectionRequiredPropertyId",
    "UIA_SelectionItemIsSelectedPropertyId",
    "UIA_SelectionItemPatternId",
    "UIA_SelectionItemSelectionContainerPropertyId",
    "UIA_SelectionItem_ElementAddedToSelectionEventId",
    "UIA_SelectionItem_ElementRemovedFromSelectionEventId",
    "UIA_SelectionItem_ElementSelectedEventId",
    "UIA_SelectionPattern2Id",
    "UIA_SelectionPatternId",
    "UIA_SelectionSelectionPropertyId",
    "UIA_Selection_InvalidatedEventId",
    "UIA_SemanticZoomControlTypeId",
    "UIA_SeparatorControlTypeId",
    "UIA_SizeOfSetPropertyId",
    "UIA_SizePropertyId",
    "UIA_SliderControlTypeId",
    "UIA_SpinnerControlTypeId",
    "UIA_SplitButtonControlTypeId",
    "UIA_SpreadsheetItemAnnotationObjectsPropertyId",
    "UIA_SpreadsheetItemAnnotationTypesPropertyId",
    "UIA_SpreadsheetItemFormulaPropertyId",
    "UIA_SpreadsheetItemPatternId",
    "UIA_SpreadsheetPatternId",
    "UIA_StatusBarControlTypeId",
    "UIA_StrikethroughColorAttributeId",
    "UIA_StrikethroughStyleAttributeId",
    "UIA_StructureChangedEventId",
    "UIA_StyleIdAttributeId",
    "UIA_StyleNameAttributeId",
    "UIA_StylesExtendedPropertiesPropertyId",
    "UIA_StylesFillColorPropertyId",
    "UIA_StylesFillPatternColorPropertyId",
    "UIA_StylesFillPatternStylePropertyId",
    "UIA_StylesPatternId",
    "UIA_StylesShapePropertyId",
    "UIA_StylesStyleIdPropertyId",
    "UIA_StylesStyleNamePropertyId",
    "UIA_SummaryChangeId",
    "UIA_SynchronizedInputPatternId",
    "UIA_SystemAlertEventId",
    "UIA_TEXTATTRIBUTE_ID",
    "UIA_TabControlTypeId",
    "UIA_TabItemControlTypeId",
    "UIA_TableColumnHeadersPropertyId",
    "UIA_TableControlTypeId",
    "UIA_TableItemColumnHeaderItemsPropertyId",
    "UIA_TableItemPatternId",
    "UIA_TableItemRowHeaderItemsPropertyId",
    "UIA_TablePatternId",
    "UIA_TableRowHeadersPropertyId",
    "UIA_TableRowOrColumnMajorPropertyId",
    "UIA_TabsAttributeId",
    "UIA_TextChildPatternId",
    "UIA_TextControlTypeId",
    "UIA_TextEditPatternId",
    "UIA_TextEdit_ConversionTargetChangedEventId",
    "UIA_TextEdit_TextChangedEventId",
    "UIA_TextFlowDirectionsAttributeId",
    "UIA_TextPattern2Id",
    "UIA_TextPatternId",
    "UIA_Text_TextChangedEventId",
    "UIA_Text_TextSelectionChangedEventId",
    "UIA_ThumbControlTypeId",
    "UIA_TitleBarControlTypeId",
    "UIA_TogglePatternId",
    "UIA_ToggleToggleStatePropertyId",
    "UIA_ToolBarControlTypeId",
    "UIA_ToolTipClosedEventId",
    "UIA_ToolTipControlTypeId",
    "UIA_ToolTipOpenedEventId",
    "UIA_Transform2CanZoomPropertyId",
    "UIA_Transform2ZoomLevelPropertyId",
    "UIA_Transform2ZoomMaximumPropertyId",
    "UIA_Transform2ZoomMinimumPropertyId",
    "UIA_TransformCanMovePropertyId",
    "UIA_TransformCanResizePropertyId",
    "UIA_TransformCanRotatePropertyId",
    "UIA_TransformPattern2Id",
    "UIA_TransformPatternId",
    "UIA_TreeControlTypeId",
    "UIA_TreeItemControlTypeId",
    "UIA_UnderlineColorAttributeId",
    "UIA_UnderlineStyleAttributeId",
    "UIA_ValueIsReadOnlyPropertyId",
    "UIA_ValuePatternId",
    "UIA_ValueValuePropertyId",
    "UIA_VirtualizedItemPatternId",
    "UIA_VisualEffectsPropertyId",
    "UIA_WindowCanMaximizePropertyId",
    "UIA_WindowCanMinimizePropertyId",
    "UIA_WindowControlTypeId",
    "UIA_WindowIsModalPropertyId",
    "UIA_WindowIsTopmostPropertyId",
    "UIA_WindowPatternId",
    "UIA_WindowWindowInteractionStatePropertyId",
    "UIA_WindowWindowVisualStatePropertyId",
    "UIA_Window_WindowClosedEventId",
    "UIA_Window_WindowOpenedEventId",
    "UIAutomationEventInfo",
    "UIAutomationMethodInfo",
    "UIAutomationParameter",
    "UIAutomationPatternInfo",
    "UIAutomationPropertyInfo",
    "UIAutomationType",
    "UIAutomationType_Array",
    "UIAutomationType_Bool",
    "UIAutomationType_BoolArray",
    "UIAutomationType_Double",
    "UIAutomationType_DoubleArray",
    "UIAutomationType_Element",
    "UIAutomationType_ElementArray",
    "UIAutomationType_Int",
    "UIAutomationType_IntArray",
    "UIAutomationType_Out",
    "UIAutomationType_OutBool",
    "UIAutomationType_OutBoolArray",
    "UIAutomationType_OutDouble",
    "UIAutomationType_OutDoubleArray",
    "UIAutomationType_OutElement",
    "UIAutomationType_OutElementArray",
    "UIAutomationType_OutInt",
    "UIAutomationType_OutIntArray",
    "UIAutomationType_OutPoint",
    "UIAutomationType_OutPointArray",
    "UIAutomationType_OutRect",
    "UIAutomationType_OutRectArray",
    "UIAutomationType_OutString",
    "UIAutomationType_OutStringArray",
    "UIAutomationType_Point",
    "UIAutomationType_PointArray",
    "UIAutomationType_Rect",
    "UIAutomationType_RectArray",
    "UIAutomationType_String",
    "UIAutomationType_StringArray",
    "UiaAddEvent",
    "UiaAndOrCondition",
    "UiaAppendRuntimeId",
    "UiaAsyncContentLoadedEventArgs",
    "UiaCacheRequest",
    "UiaChangeInfo",
    "UiaChangesEventArgs",
    "UiaClientsAreListening",
    "UiaCondition",
    "UiaDisconnectAllProviders",
    "UiaDisconnectProvider",
    "UiaEventAddWindow",
    "UiaEventArgs",
    "UiaEventCallback",
    "UiaEventRemoveWindow",
    "UiaFind",
    "UiaFindParams",
    "UiaGetErrorDescription",
    "UiaGetPatternProvider",
    "UiaGetPropertyValue",
    "UiaGetReservedMixedAttributeValue",
    "UiaGetReservedNotSupportedValue",
    "UiaGetRootNode",
    "UiaGetRuntimeId",
    "UiaGetUpdatedCache",
    "UiaHPatternObjectFromVariant",
    "UiaHTextRangeFromVariant",
    "UiaHUiaNodeFromVariant",
    "UiaHasServerSideProvider",
    "UiaHostProviderFromHwnd",
    "UiaIAccessibleFromProvider",
    "UiaLookupId",
    "UiaNavigate",
    "UiaNodeFromFocus",
    "UiaNodeFromHandle",
    "UiaNodeFromPoint",
    "UiaNodeFromProvider",
    "UiaNodeRelease",
    "UiaNotCondition",
    "UiaPatternRelease",
    "UiaPoint",
    "UiaPropertyChangedEventArgs",
    "UiaPropertyCondition",
    "UiaProviderCallback",
    "UiaProviderForNonClient",
    "UiaProviderFromIAccessible",
    "UiaRaiseActiveTextPositionChangedEvent",
    "UiaRaiseAsyncContentLoadedEvent",
    "UiaRaiseAutomationEvent",
    "UiaRaiseAutomationPropertyChangedEvent",
    "UiaRaiseChangesEvent",
    "UiaRaiseNotificationEvent",
    "UiaRaiseStructureChangedEvent",
    "UiaRaiseTextEditTextChangedEvent",
    "UiaRect",
    "UiaRegisterProviderCallback",
    "UiaRemoveEvent",
    "UiaReturnRawElementProvider",
    "UiaRootObjectId",
    "UiaSetFocus",
    "UiaStructureChangedEventArgs",
    "UiaTextEditTextChangedEventArgs",
    "UiaTextRangeRelease",
    "UiaWindowClosedEventArgs",
    "UnhookWinEvent",
    "UnregisterPointerInputTarget",
    "UnregisterPointerInputTargetEx",
    "ValuePattern_SetValue",
    "Value_IsReadOnly_Property_GUID",
    "Value_Pattern_GUID",
    "Value_Value_Property_GUID",
    "VirtualizedItemPattern_Realize",
    "VirtualizedItem_Pattern_GUID",
    "VisualEffects",
    "VisualEffects_Bevel",
    "VisualEffects_Glow",
    "VisualEffects_None",
    "VisualEffects_Property_GUID",
    "VisualEffects_Reflection",
    "VisualEffects_Shadow",
    "VisualEffects_SoftEdges",
    "WINEVENTPROC",
    "WindowFromAccessibleObject",
    "WindowInteractionState",
    "WindowInteractionState_BlockedByModalWindow",
    "WindowInteractionState_Closing",
    "WindowInteractionState_NotResponding",
    "WindowInteractionState_ReadyForUserInteraction",
    "WindowInteractionState_Running",
    "WindowPattern_Close",
    "WindowPattern_SetWindowVisualState",
    "WindowPattern_WaitForInputIdle",
    "WindowVisualState",
    "WindowVisualState_Maximized",
    "WindowVisualState_Minimized",
    "WindowVisualState_Normal",
    "Window_CanMaximize_Property_GUID",
    "Window_CanMinimize_Property_GUID",
    "Window_Control_GUID",
    "Window_IsModal_Property_GUID",
    "Window_IsTopmost_Property_GUID",
    "Window_Pattern_GUID",
    "Window_WindowClosed_Event_GUID",
    "Window_WindowInteractionState_Property_GUID",
    "Window_WindowOpened_Event_GUID",
    "Window_WindowVisualState_Property_GUID",
    "ZoomUnit",
    "ZoomUnit_LargeDecrement",
    "ZoomUnit_LargeIncrement",
    "ZoomUnit_NoAmount",
    "ZoomUnit_SmallDecrement",
    "ZoomUnit_SmallIncrement",
]
_arch_optional = [
]
