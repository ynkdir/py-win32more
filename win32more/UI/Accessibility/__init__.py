from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.UI.Accessibility
import win32more.UI.WindowsAndMessaging
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
ACC_UTILITY_STATE_FLAGS = UInt32
ANRUS_ON_SCREEN_KEYBOARD_ACTIVE = 1
ANRUS_TOUCH_MODIFICATION_ACTIVE = 2
ANRUS_PRIORITY_AUDIO_ACTIVE = 4
ANRUS_PRIORITY_AUDIO_ACTIVE_NODUCK = 8
def _define_ACCESSTIMEOUT_head():
    class ACCESSTIMEOUT(Structure):
        pass
    return ACCESSTIMEOUT
def _define_ACCESSTIMEOUT():
    ACCESSTIMEOUT = win32more.UI.Accessibility.ACCESSTIMEOUT_head
    ACCESSTIMEOUT._fields_ = [
        ('cbSize', UInt32),
        ('dwFlags', UInt32),
        ('iTimeOutMSec', UInt32),
    ]
    return ACCESSTIMEOUT
ActiveEnd = Int32
ActiveEnd_None = 0
ActiveEnd_Start = 1
ActiveEnd_End = 2
AnimationStyle = Int32
AnimationStyle_None = 0
AnimationStyle_LasVegasLights = 1
AnimationStyle_BlinkingBackground = 2
AnimationStyle_SparkleText = 3
AnimationStyle_MarchingBlackAnts = 4
AnimationStyle_MarchingRedAnts = 5
AnimationStyle_Shimmer = 6
AnimationStyle_Other = -1
AnnoScope = Int32
ANNO_THIS = 0
ANNO_CONTAINER = 1
def _define_LIBID_Accessibility():
    return Guid('1ea4dbf0-3c3b-11cf-81-0c-00-aa-00-38-9b-71')
def _define_CLSID_AccPropServices():
    return Guid('b5f8350b-0548-48b1-a6-ee-88-bd-00-b4-a5-e7')
def _define_IIS_IsOleaccProxy():
    return Guid('902697fa-80e4-4560-80-2a-a1-3f-22-a6-47-09')
def _define_IIS_ControlAccessible():
    return Guid('38c682a6-9731-43f2-9f-ae-e9-01-e6-41-b1-01')
ANRUS_PRIORITY_AUDIO_DYNAMIC_DUCK = 16
MSAA_MENU_SIG = -1441927155
def _define_PROPID_ACC_NAME():
    return Guid('608d3df8-8128-4aa7-a4-28-f5-5e-49-26-72-91')
def _define_PROPID_ACC_VALUE():
    return Guid('123fe443-211a-4615-95-27-c4-5a-7e-93-71-7a')
def _define_PROPID_ACC_DESCRIPTION():
    return Guid('4d48dfe4-bd3f-491f-a6-48-49-2d-6f-20-c5-88')
def _define_PROPID_ACC_ROLE():
    return Guid('cb905ff2-7bd1-4c05-b3-c8-e6-c2-41-36-4d-70')
def _define_PROPID_ACC_STATE():
    return Guid('a8d4d5b0-0a21-42d0-a5-c0-51-4e-98-4f-45-7b')
def _define_PROPID_ACC_HELP():
    return Guid('c831e11f-44db-4a99-97-68-cb-8f-97-8b-72-31')
def _define_PROPID_ACC_KEYBOARDSHORTCUT():
    return Guid('7d9bceee-7d1e-4979-93-82-51-80-f4-17-2c-34')
def _define_PROPID_ACC_DEFAULTACTION():
    return Guid('180c072b-c27f-43c7-99-22-f6-35-62-a4-63-2b')
def _define_PROPID_ACC_HELPTOPIC():
    return Guid('787d1379-8ede-440b-8a-ec-11-f7-bf-90-30-b3')
def _define_PROPID_ACC_FOCUS():
    return Guid('6eb335df-1c29-4127-b1-2c-de-e9-fd-15-7f-2b')
def _define_PROPID_ACC_SELECTION():
    return Guid('b99d073c-d731-405b-90-61-d9-5e-8f-84-29-84')
def _define_PROPID_ACC_PARENT():
    return Guid('474c22b6-ffc2-467a-b1-b5-e9-58-b4-65-73-30')
def _define_PROPID_ACC_NAV_UP():
    return Guid('016e1a2b-1a4e-4767-86-12-33-86-f6-69-35-ec')
def _define_PROPID_ACC_NAV_DOWN():
    return Guid('031670ed-3cdf-48d2-96-13-13-8f-2d-d8-a6-68')
def _define_PROPID_ACC_NAV_LEFT():
    return Guid('228086cb-82f1-4a39-87-05-dc-dc-0f-ff-92-f5')
def _define_PROPID_ACC_NAV_RIGHT():
    return Guid('cd211d9f-e1cb-4fe5-a7-7c-92-0b-88-4d-09-5b')
def _define_PROPID_ACC_NAV_PREV():
    return Guid('776d3891-c73b-4480-b3-f6-07-6a-16-a1-5a-f6')
def _define_PROPID_ACC_NAV_NEXT():
    return Guid('1cdc5455-8cd9-4c92-a3-71-39-39-a2-fe-3e-ee')
def _define_PROPID_ACC_NAV_FIRSTCHILD():
    return Guid('cfd02558-557b-4c67-84-f9-2a-09-fc-e4-07-49')
def _define_PROPID_ACC_NAV_LASTCHILD():
    return Guid('302ecaa5-48d5-4f8d-b6-71-1a-8d-20-a7-78-32')
def _define_PROPID_ACC_ROLEMAP():
    return Guid('f79acda2-140d-4fe6-89-14-20-84-76-32-82-69')
def _define_PROPID_ACC_VALUEMAP():
    return Guid('da1c3d79-fc5c-420e-b3-99-9d-15-33-54-9e-75')
def _define_PROPID_ACC_STATEMAP():
    return Guid('43946c5e-0ac0-4042-b5-25-07-bb-db-e1-7f-a7')
def _define_PROPID_ACC_DESCRIPTIONMAP():
    return Guid('1ff1435f-8a14-477b-b2-26-a0-ab-e2-79-97-5d')
def _define_PROPID_ACC_DODEFAULTACTION():
    return Guid('1ba09523-2e3b-49a6-a0-59-59-68-2a-3c-48-fd')
DISPID_ACC_PARENT = -5000
DISPID_ACC_CHILDCOUNT = -5001
DISPID_ACC_CHILD = -5002
DISPID_ACC_NAME = -5003
DISPID_ACC_VALUE = -5004
DISPID_ACC_DESCRIPTION = -5005
DISPID_ACC_ROLE = -5006
DISPID_ACC_STATE = -5007
DISPID_ACC_HELP = -5008
DISPID_ACC_HELPTOPIC = -5009
DISPID_ACC_KEYBOARDSHORTCUT = -5010
DISPID_ACC_FOCUS = -5011
DISPID_ACC_SELECTION = -5012
DISPID_ACC_DEFAULTACTION = -5013
DISPID_ACC_SELECT = -5014
DISPID_ACC_LOCATION = -5015
DISPID_ACC_NAVIGATE = -5016
DISPID_ACC_HITTEST = -5017
DISPID_ACC_DODEFAULTACTION = -5018
NAVDIR_MIN = 0
NAVDIR_UP = 1
NAVDIR_DOWN = 2
NAVDIR_LEFT = 3
NAVDIR_RIGHT = 4
NAVDIR_NEXT = 5
NAVDIR_PREVIOUS = 6
NAVDIR_FIRSTCHILD = 7
NAVDIR_LASTCHILD = 8
NAVDIR_MAX = 9
SELFLAG_NONE = 0
SELFLAG_TAKEFOCUS = 1
SELFLAG_TAKESELECTION = 2
SELFLAG_EXTENDSELECTION = 4
SELFLAG_ADDSELECTION = 8
SELFLAG_REMOVESELECTION = 16
SELFLAG_VALID = 31
STATE_SYSTEM_NORMAL = 0
STATE_SYSTEM_HASPOPUP = 1073741824
ROLE_SYSTEM_TITLEBAR = 1
ROLE_SYSTEM_MENUBAR = 2
ROLE_SYSTEM_SCROLLBAR = 3
ROLE_SYSTEM_GRIP = 4
ROLE_SYSTEM_SOUND = 5
ROLE_SYSTEM_CURSOR = 6
ROLE_SYSTEM_CARET = 7
ROLE_SYSTEM_ALERT = 8
ROLE_SYSTEM_WINDOW = 9
ROLE_SYSTEM_CLIENT = 10
ROLE_SYSTEM_MENUPOPUP = 11
ROLE_SYSTEM_MENUITEM = 12
ROLE_SYSTEM_TOOLTIP = 13
ROLE_SYSTEM_APPLICATION = 14
ROLE_SYSTEM_DOCUMENT = 15
ROLE_SYSTEM_PANE = 16
ROLE_SYSTEM_CHART = 17
ROLE_SYSTEM_DIALOG = 18
ROLE_SYSTEM_BORDER = 19
ROLE_SYSTEM_GROUPING = 20
ROLE_SYSTEM_SEPARATOR = 21
ROLE_SYSTEM_TOOLBAR = 22
ROLE_SYSTEM_STATUSBAR = 23
ROLE_SYSTEM_TABLE = 24
ROLE_SYSTEM_COLUMNHEADER = 25
ROLE_SYSTEM_ROWHEADER = 26
ROLE_SYSTEM_COLUMN = 27
ROLE_SYSTEM_ROW = 28
ROLE_SYSTEM_CELL = 29
ROLE_SYSTEM_LINK = 30
ROLE_SYSTEM_HELPBALLOON = 31
ROLE_SYSTEM_CHARACTER = 32
ROLE_SYSTEM_LIST = 33
ROLE_SYSTEM_LISTITEM = 34
ROLE_SYSTEM_OUTLINE = 35
ROLE_SYSTEM_OUTLINEITEM = 36
ROLE_SYSTEM_PAGETAB = 37
ROLE_SYSTEM_PROPERTYPAGE = 38
ROLE_SYSTEM_INDICATOR = 39
ROLE_SYSTEM_GRAPHIC = 40
ROLE_SYSTEM_STATICTEXT = 41
ROLE_SYSTEM_TEXT = 42
ROLE_SYSTEM_PUSHBUTTON = 43
ROLE_SYSTEM_CHECKBUTTON = 44
ROLE_SYSTEM_RADIOBUTTON = 45
ROLE_SYSTEM_COMBOBOX = 46
ROLE_SYSTEM_DROPLIST = 47
ROLE_SYSTEM_PROGRESSBAR = 48
ROLE_SYSTEM_DIAL = 49
ROLE_SYSTEM_HOTKEYFIELD = 50
ROLE_SYSTEM_SLIDER = 51
ROLE_SYSTEM_SPINBUTTON = 52
ROLE_SYSTEM_DIAGRAM = 53
ROLE_SYSTEM_ANIMATION = 54
ROLE_SYSTEM_EQUATION = 55
ROLE_SYSTEM_BUTTONDROPDOWN = 56
ROLE_SYSTEM_BUTTONMENU = 57
ROLE_SYSTEM_BUTTONDROPDOWNGRID = 58
ROLE_SYSTEM_WHITESPACE = 59
ROLE_SYSTEM_PAGETABLIST = 60
ROLE_SYSTEM_CLOCK = 61
ROLE_SYSTEM_SPLITBUTTON = 62
ROLE_SYSTEM_IPADDRESS = 63
ROLE_SYSTEM_OUTLINEBUTTON = 64
UIA_E_ELEMENTNOTENABLED = 2147746304
UIA_E_ELEMENTNOTAVAILABLE = 2147746305
UIA_E_NOCLICKABLEPOINT = 2147746306
UIA_E_PROXYASSEMBLYNOTLOADED = 2147746307
UIA_E_NOTSUPPORTED = 2147746308
UIA_E_INVALIDOPERATION = 2148734217
UIA_E_TIMEOUT = 2148734213
UiaAppendRuntimeId = 3
UiaRootObjectId = -25
def _define_RuntimeId_Property_GUID():
    return Guid('a39eebfa-7fba-4c89-b4-d4-b9-9e-2d-e7-d1-60')
def _define_BoundingRectangle_Property_GUID():
    return Guid('7bbfe8b2-3bfc-48dd-b7-29-c7-94-b8-46-e9-a1')
def _define_ProcessId_Property_GUID():
    return Guid('40499998-9c31-4245-a4-03-87-32-0e-59-ea-f6')
def _define_ControlType_Property_GUID():
    return Guid('ca774fea-28ac-4bc2-94-ca-ac-ec-6d-6c-10-a3')
def _define_LocalizedControlType_Property_GUID():
    return Guid('8763404f-a1bd-452a-89-c4-3f-01-d3-83-38-06')
def _define_Name_Property_GUID():
    return Guid('c3a6921b-4a99-44f1-bc-a6-61-18-70-52-c4-31')
def _define_AcceleratorKey_Property_GUID():
    return Guid('514865df-2557-4cb9-ae-ed-6c-ed-08-4c-e5-2c')
def _define_AccessKey_Property_GUID():
    return Guid('06827b12-a7f9-4a15-91-7c-ff-a5-ad-3e-b0-a7')
def _define_HasKeyboardFocus_Property_GUID():
    return Guid('cf8afd39-3f46-4800-96-56-b2-bf-12-52-99-05')
def _define_IsKeyboardFocusable_Property_GUID():
    return Guid('f7b8552a-0859-4b37-b9-cb-51-e7-20-92-f2-9f')
def _define_IsEnabled_Property_GUID():
    return Guid('2109427f-da60-4fed-bf-1b-26-4b-dc-e6-eb-3a')
def _define_AutomationId_Property_GUID():
    return Guid('c82c0500-b60e-4310-a2-67-30-3c-53-1f-8e-e5')
def _define_ClassName_Property_GUID():
    return Guid('157b7215-894f-4b65-84-e2-aa-c0-da-08-b1-6b')
def _define_HelpText_Property_GUID():
    return Guid('08555685-0977-45c7-a7-a6-ab-af-56-84-12-1a')
def _define_ClickablePoint_Property_GUID():
    return Guid('0196903b-b203-4818-a9-f3-f0-8e-67-5f-23-41')
def _define_Culture_Property_GUID():
    return Guid('e2d74f27-3d79-4dc2-b8-8b-30-44-96-3a-8a-fb')
def _define_IsControlElement_Property_GUID():
    return Guid('95f35085-abcc-4afd-a5-f4-db-b4-6c-23-0f-db')
def _define_IsContentElement_Property_GUID():
    return Guid('4bda64a8-f5d8-480b-81-55-ef-2e-89-ad-b6-72')
def _define_LabeledBy_Property_GUID():
    return Guid('e5b8924b-fc8a-4a35-80-31-cf-78-ac-43-e5-5e')
def _define_IsPassword_Property_GUID():
    return Guid('e8482eb1-687c-497b-be-bc-03-be-53-ec-14-54')
def _define_NewNativeWindowHandle_Property_GUID():
    return Guid('5196b33b-380a-4982-95-e1-91-f3-ef-60-e0-24')
def _define_ItemType_Property_GUID():
    return Guid('cdda434d-6222-413b-a6-8a-32-5d-d1-d4-0f-39')
def _define_IsOffscreen_Property_GUID():
    return Guid('03c3d160-db79-42db-a2-ef-1c-23-1e-ed-e5-07')
def _define_Orientation_Property_GUID():
    return Guid('a01eee62-3884-4415-88-7e-67-8e-c2-1e-39-ba')
def _define_FrameworkId_Property_GUID():
    return Guid('dbfd9900-7e1a-4f58-b6-1b-70-63-12-0f-77-3b')
def _define_IsRequiredForForm_Property_GUID():
    return Guid('4f5f43cf-59fb-4bde-a2-70-60-2e-5e-11-41-e9')
def _define_ItemStatus_Property_GUID():
    return Guid('51de0321-3973-43e7-89-13-0b-08-e8-13-c3-7f')
def _define_AriaRole_Property_GUID():
    return Guid('dd207b95-be4a-4e0d-b7-27-63-ac-e9-4b-69-16')
def _define_AriaProperties_Property_GUID():
    return Guid('4213678c-e025-4922-be-b5-e4-3b-a0-8e-62-21')
def _define_IsDataValidForForm_Property_GUID():
    return Guid('445ac684-c3fc-4dd9-ac-f8-84-5a-57-92-96-ba')
def _define_ControllerFor_Property_GUID():
    return Guid('51124c8a-a5d2-4f13-9b-e6-7f-a8-ba-9d-3a-90')
def _define_DescribedBy_Property_GUID():
    return Guid('7c5865b8-9992-40fd-8d-b0-6b-f1-d3-17-f9-98')
def _define_FlowsTo_Property_GUID():
    return Guid('e4f33d20-559a-47fb-a8-30-f9-cb-4f-f1-a7-0a')
def _define_ProviderDescription_Property_GUID():
    return Guid('dca5708a-c16b-4cd9-b8-89-be-b1-6a-80-49-04')
def _define_OptimizeForVisualContent_Property_GUID():
    return Guid('6a852250-c75a-4e5d-b8-58-e3-81-b0-f7-88-61')
def _define_IsDockPatternAvailable_Property_GUID():
    return Guid('2600a4c4-2ff8-4c96-ae-31-8f-e6-19-a1-3c-6c')
def _define_IsExpandCollapsePatternAvailable_Property_GUID():
    return Guid('929d3806-5287-4725-aa-16-22-2a-fc-63-d5-95')
def _define_IsGridItemPatternAvailable_Property_GUID():
    return Guid('5a43e524-f9a2-4b12-84-c8-b4-8a-3e-fe-dd-34')
def _define_IsGridPatternAvailable_Property_GUID():
    return Guid('5622c26c-f0ef-4f3b-97-cb-71-4c-08-68-58-8b')
def _define_IsInvokePatternAvailable_Property_GUID():
    return Guid('4e725738-8364-4679-aa-6c-f3-f4-19-31-f7-50')
def _define_IsMultipleViewPatternAvailable_Property_GUID():
    return Guid('ff0a31eb-8e25-469d-8d-6e-e7-71-a2-7c-1b-90')
def _define_IsRangeValuePatternAvailable_Property_GUID():
    return Guid('fda4244a-eb4d-43ff-b5-ad-ed-36-d3-73-ec-4c')
def _define_IsScrollPatternAvailable_Property_GUID():
    return Guid('3ebb7b4a-828a-4b57-9d-22-2f-ea-16-32-ed-0d')
def _define_IsScrollItemPatternAvailable_Property_GUID():
    return Guid('1cad1a05-0927-4b76-97-e1-0f-cd-b2-09-b9-8a')
def _define_IsSelectionItemPatternAvailable_Property_GUID():
    return Guid('8becd62d-0bc3-4109-be-e2-8e-67-15-29-0e-68')
def _define_IsSelectionPatternAvailable_Property_GUID():
    return Guid('f588acbe-c769-4838-9a-60-26-86-dc-11-88-c4')
def _define_IsTablePatternAvailable_Property_GUID():
    return Guid('cb83575f-45c2-4048-9c-76-15-97-15-a1-39-df')
def _define_IsTableItemPatternAvailable_Property_GUID():
    return Guid('eb36b40d-8ea4-489b-a0-13-e6-0d-59-51-fe-34')
def _define_IsTextPatternAvailable_Property_GUID():
    return Guid('fbe2d69d-aff6-4a45-82-e2-fc-92-a8-2f-59-17')
def _define_IsTogglePatternAvailable_Property_GUID():
    return Guid('78686d53-fcd0-4b83-9b-78-58-32-ce-63-bb-5b')
def _define_IsTransformPatternAvailable_Property_GUID():
    return Guid('a7f78804-d68b-4077-a5-c6-7a-5e-a1-ac-31-c5')
def _define_IsValuePatternAvailable_Property_GUID():
    return Guid('0b5020a7-2119-473b-be-37-5c-eb-98-bb-fb-22')
def _define_IsWindowPatternAvailable_Property_GUID():
    return Guid('e7a57bb1-5888-4155-98-dc-b4-22-fd-57-f2-bc')
def _define_IsLegacyIAccessiblePatternAvailable_Property_GUID():
    return Guid('d8ebd0c7-929a-4ee7-8d-3a-d3-d9-44-13-02-7b')
def _define_IsItemContainerPatternAvailable_Property_GUID():
    return Guid('624b5ca7-fe40-4957-a0-19-20-c4-cf-11-92-0f')
def _define_IsVirtualizedItemPatternAvailable_Property_GUID():
    return Guid('302cb151-2ac8-45d6-97-7b-d2-b3-a5-a5-3f-20')
def _define_IsSynchronizedInputPatternAvailable_Property_GUID():
    return Guid('75d69cc5-d2bf-4943-87-6e-b4-5b-62-a6-cc-66')
def _define_IsObjectModelPatternAvailable_Property_GUID():
    return Guid('6b21d89b-2841-412f-8e-f2-15-ca-95-23-18-ba')
def _define_IsAnnotationPatternAvailable_Property_GUID():
    return Guid('0b5b3238-6d5c-41b6-bc-c4-5e-80-7f-65-51-c4')
def _define_IsTextPattern2Available_Property_GUID():
    return Guid('41cf921d-e3f1-4b22-9c-81-e1-c3-ed-33-1c-22')
def _define_IsTextEditPatternAvailable_Property_GUID():
    return Guid('7843425c-8b32-484c-9a-b5-e3-20-05-71-ff-da')
def _define_IsCustomNavigationPatternAvailable_Property_GUID():
    return Guid('8f8e80d4-2351-48e0-87-4a-54-aa-73-13-88-9a')
def _define_IsStylesPatternAvailable_Property_GUID():
    return Guid('27f353d3-459c-4b59-a4-90-50-61-1d-ac-af-b5')
def _define_IsSpreadsheetPatternAvailable_Property_GUID():
    return Guid('6ff43732-e4b4-4555-97-bc-ec-db-bc-4d-18-88')
def _define_IsSpreadsheetItemPatternAvailable_Property_GUID():
    return Guid('9fe79b2a-2f94-43fd-99-6b-54-9e-31-6f-4a-cd')
def _define_IsTransformPattern2Available_Property_GUID():
    return Guid('25980b4b-be04-4710-ab-4a-fd-a3-1d-bd-28-95')
def _define_IsTextChildPatternAvailable_Property_GUID():
    return Guid('559e65df-30ff-43b5-b5-ed-5b-28-3b-80-c7-e9')
def _define_IsDragPatternAvailable_Property_GUID():
    return Guid('e997a7b7-1d39-4ca7-be-0f-27-7f-cf-56-05-cc')
def _define_IsDropTargetPatternAvailable_Property_GUID():
    return Guid('0686b62e-8e19-4aaf-87-3d-38-4f-6d-3b-92-be')
def _define_IsStructuredMarkupPatternAvailable_Property_GUID():
    return Guid('b0d4c196-2c0b-489c-b1-65-a4-05-92-8c-6f-3d')
def _define_IsPeripheral_Property_GUID():
    return Guid('da758276-7ed5-49d4-8e-68-ec-c9-a2-d3-00-dd')
def _define_PositionInSet_Property_GUID():
    return Guid('33d1dc54-641e-4d76-a6-b1-13-f3-41-c1-f8-96')
def _define_SizeOfSet_Property_GUID():
    return Guid('1600d33c-3b9f-4369-94-31-aa-29-3f-34-4c-f1')
def _define_Level_Property_GUID():
    return Guid('242ac529-cd36-400f-aa-d9-78-76-ef-3a-f6-27')
def _define_AnnotationTypes_Property_GUID():
    return Guid('64b71f76-53c4-4696-a2-19-20-e9-40-c9-a1-76')
def _define_AnnotationObjects_Property_GUID():
    return Guid('310910c8-7c6e-4f20-be-cd-4a-af-6d-19-11-56')
def _define_LandmarkType_Property_GUID():
    return Guid('454045f2-6f61-49f7-a4-f8-b5-f0-cf-82-da-1e')
def _define_LocalizedLandmarkType_Property_GUID():
    return Guid('7ac81980-eafb-4fb2-bf-91-f4-85-be-f5-e8-e1')
def _define_FullDescription_Property_GUID():
    return Guid('0d4450ff-6aef-4f33-95-dd-7b-ef-a7-2a-43-91')
def _define_Value_Value_Property_GUID():
    return Guid('e95f5e64-269f-4a85-ba-99-40-92-c3-ea-29-86')
def _define_Value_IsReadOnly_Property_GUID():
    return Guid('eb090f30-e24c-4799-a7-05-0d-24-7b-c0-37-f8')
def _define_RangeValue_Value_Property_GUID():
    return Guid('131f5d98-c50c-489d-ab-e5-ae-22-08-98-c5-f7')
def _define_RangeValue_IsReadOnly_Property_GUID():
    return Guid('25fa1055-debf-4373-a7-9e-1f-1a-19-08-d3-c4')
def _define_RangeValue_Minimum_Property_GUID():
    return Guid('78cbd3b2-684d-4860-af-93-d1-f9-5c-b0-22-fd')
def _define_RangeValue_Maximum_Property_GUID():
    return Guid('19319914-f979-4b35-a1-a6-d3-7e-05-43-34-73')
def _define_RangeValue_LargeChange_Property_GUID():
    return Guid('a1f96325-3a3d-4b44-8e-1f-4a-46-d9-84-40-19')
def _define_RangeValue_SmallChange_Property_GUID():
    return Guid('81c2c457-3941-4107-99-75-13-97-60-f7-c0-72')
def _define_Scroll_HorizontalScrollPercent_Property_GUID():
    return Guid('c7c13c0e-eb21-47ff-ac-c4-b5-a3-35-0f-51-91')
def _define_Scroll_HorizontalViewSize_Property_GUID():
    return Guid('70c2e5d4-fcb0-4713-a9-aa-af-92-ff-79-e4-cd')
def _define_Scroll_VerticalScrollPercent_Property_GUID():
    return Guid('6c8d7099-b2a8-4948-bf-f7-3c-f9-05-8b-fe-fb')
def _define_Scroll_VerticalViewSize_Property_GUID():
    return Guid('de6a2e22-d8c7-40c5-83-ba-e5-f6-81-d5-31-08')
def _define_Scroll_HorizontallyScrollable_Property_GUID():
    return Guid('8b925147-28cd-49ae-bd-63-f4-41-18-d2-e7-19')
def _define_Scroll_VerticallyScrollable_Property_GUID():
    return Guid('89164798-0068-4315-b8-9a-1e-7c-fb-bc-3d-fc')
def _define_Selection_Selection_Property_GUID():
    return Guid('aa6dc2a2-0e2b-4d38-96-d5-34-e4-70-b8-18-53')
def _define_Selection_CanSelectMultiple_Property_GUID():
    return Guid('49d73da5-c883-4500-88-3d-8f-cf-8d-af-6c-be')
def _define_Selection_IsSelectionRequired_Property_GUID():
    return Guid('b1ae4422-63fe-44e7-a5-a5-a7-38-c8-29-b1-9a')
def _define_Grid_RowCount_Property_GUID():
    return Guid('2a9505bf-c2eb-4fb6-b3-56-82-45-ae-53-70-3e')
def _define_Grid_ColumnCount_Property_GUID():
    return Guid('fe96f375-44aa-4536-ac-7a-2a-75-d7-1a-3e-fc')
def _define_GridItem_Row_Property_GUID():
    return Guid('6223972a-c945-4563-93-29-fd-c9-74-af-25-53')
def _define_GridItem_Column_Property_GUID():
    return Guid('c774c15c-62c0-4519-8b-dc-47-be-57-3c-8a-d5')
def _define_GridItem_RowSpan_Property_GUID():
    return Guid('4582291c-466b-4e93-8e-83-3d-17-15-ec-0c-5e')
def _define_GridItem_ColumnSpan_Property_GUID():
    return Guid('583ea3f5-86d0-4b08-a6-ec-2c-54-63-ff-c1-09')
def _define_GridItem_Parent_Property_GUID():
    return Guid('9d912252-b97f-4ecc-85-10-ea-0e-33-42-7c-72')
def _define_Dock_DockPosition_Property_GUID():
    return Guid('6d67f02e-c0b0-4b10-b5-b9-18-d6-ec-f9-87-60')
def _define_ExpandCollapse_ExpandCollapseState_Property_GUID():
    return Guid('275a4c48-85a7-4f69-ab-a0-af-15-76-10-00-2b')
def _define_MultipleView_CurrentView_Property_GUID():
    return Guid('7a81a67a-b94f-4875-91-8b-65-c8-d2-f9-98-e5')
def _define_MultipleView_SupportedViews_Property_GUID():
    return Guid('8d5db9fd-ce3c-4ae7-b7-88-40-0a-3c-64-55-47')
def _define_Window_CanMaximize_Property_GUID():
    return Guid('64fff53f-635d-41c1-95-0c-cb-5a-df-be-28-e3')
def _define_Window_CanMinimize_Property_GUID():
    return Guid('b73b4625-5988-4b97-b4-c2-a6-fe-6e-78-c8-c6')
def _define_Window_WindowVisualState_Property_GUID():
    return Guid('4ab7905f-e860-453e-a3-0a-f6-43-1e-5d-aa-d5')
def _define_Window_WindowInteractionState_Property_GUID():
    return Guid('4fed26a4-0455-4fa2-b2-1c-c4-da-2d-b1-ff-9c')
def _define_Window_IsModal_Property_GUID():
    return Guid('ff4e6892-37b9-4fca-85-32-ff-e6-74-ec-fe-ed')
def _define_Window_IsTopmost_Property_GUID():
    return Guid('ef7d85d3-0937-4962-92-41-b6-23-45-f2-40-41')
def _define_SelectionItem_IsSelected_Property_GUID():
    return Guid('f122835f-cd5f-43df-b7-9d-4b-84-9e-9e-60-20')
def _define_SelectionItem_SelectionContainer_Property_GUID():
    return Guid('a4365b6e-9c1e-4b63-8b-53-c2-42-1d-d1-e8-fb')
def _define_Table_RowHeaders_Property_GUID():
    return Guid('d9e35b87-6eb8-4562-aa-c6-a8-a9-07-52-36-a8')
def _define_Table_ColumnHeaders_Property_GUID():
    return Guid('aff1d72b-968d-42b1-b4-59-15-0b-29-9d-a6-64')
def _define_Table_RowOrColumnMajor_Property_GUID():
    return Guid('83be75c3-29fe-4a30-85-e1-2a-62-77-fd-10-6e')
def _define_TableItem_RowHeaderItems_Property_GUID():
    return Guid('b3f853a0-0574-4cd8-bc-d7-ed-59-23-57-2d-97')
def _define_TableItem_ColumnHeaderItems_Property_GUID():
    return Guid('967a56a3-74b6-431e-8d-e6-99-c4-11-03-1c-58')
def _define_Toggle_ToggleState_Property_GUID():
    return Guid('b23cdc52-22c2-4c6c-9d-ed-f5-c4-22-47-9e-de')
def _define_Transform_CanMove_Property_GUID():
    return Guid('1b75824d-208b-4fdf-bc-cd-f1-f4-e5-74-1f-4f')
def _define_Transform_CanResize_Property_GUID():
    return Guid('bb98dca5-4c1a-41d4-a4-f6-eb-c1-28-64-41-80')
def _define_Transform_CanRotate_Property_GUID():
    return Guid('10079b48-3849-476f-ac-96-44-a9-5c-84-40-d9')
def _define_LegacyIAccessible_ChildId_Property_GUID():
    return Guid('9a191b5d-9ef2-4787-a4-59-dc-de-88-5d-d4-e8')
def _define_LegacyIAccessible_Name_Property_GUID():
    return Guid('caeb063d-40ae-4869-aa-5a-1b-8e-5d-66-67-39')
def _define_LegacyIAccessible_Value_Property_GUID():
    return Guid('b5c5b0b6-8217-4a77-97-a5-19-0a-85-ed-01-56')
def _define_LegacyIAccessible_Description_Property_GUID():
    return Guid('46448418-7d70-4ea9-9d-27-b7-e7-75-cf-2a-d7')
def _define_LegacyIAccessible_Role_Property_GUID():
    return Guid('6856e59f-cbaf-4e31-93-e8-bc-bf-6f-7e-49-1c')
def _define_LegacyIAccessible_State_Property_GUID():
    return Guid('df985854-2281-4340-ab-9c-c6-0e-2c-58-03-f6')
def _define_LegacyIAccessible_Help_Property_GUID():
    return Guid('94402352-161c-4b77-a9-8d-a8-72-cc-33-94-7a')
def _define_LegacyIAccessible_KeyboardShortcut_Property_GUID():
    return Guid('8f6909ac-00b8-4259-a4-1c-96-62-66-d4-3a-8a')
def _define_LegacyIAccessible_Selection_Property_GUID():
    return Guid('8aa8b1e0-0891-40cc-8b-06-90-d7-d4-16-62-19')
def _define_LegacyIAccessible_DefaultAction_Property_GUID():
    return Guid('3b331729-eaad-4502-b8-5f-92-61-56-22-91-3c')
def _define_Annotation_AnnotationTypeId_Property_GUID():
    return Guid('20ae484f-69ef-4c48-8f-5b-c4-93-8b-20-6a-c7')
def _define_Annotation_AnnotationTypeName_Property_GUID():
    return Guid('9b818892-5ac9-4af9-aa-96-f5-8a-77-b0-58-e3')
def _define_Annotation_Author_Property_GUID():
    return Guid('7a528462-9c5c-4a03-a9-74-8b-30-7a-99-37-f2')
def _define_Annotation_DateTime_Property_GUID():
    return Guid('99b5ca5d-1acf-414b-a4-d0-6b-35-0b-04-75-78')
def _define_Annotation_Target_Property_GUID():
    return Guid('b71b302d-2104-44ad-9c-5c-09-2b-49-07-d7-0f')
def _define_Styles_StyleId_Property_GUID():
    return Guid('da82852f-3817-4233-82-af-02-27-9e-72-cc-77')
def _define_Styles_StyleName_Property_GUID():
    return Guid('1c12b035-05d1-4f55-9e-8e-14-89-f3-ff-55-0d')
def _define_Styles_FillColor_Property_GUID():
    return Guid('63eff97a-a1c5-4b1d-84-eb-b7-65-f2-ed-d6-32')
def _define_Styles_FillPatternStyle_Property_GUID():
    return Guid('81cf651f-482b-4451-a3-0a-e1-54-5e-55-4f-b8')
def _define_Styles_Shape_Property_GUID():
    return Guid('c71a23f8-778c-400d-84-58-3b-54-3e-52-69-84')
def _define_Styles_FillPatternColor_Property_GUID():
    return Guid('939a59fe-8fbd-4e75-a2-71-ac-45-95-19-51-63')
def _define_Styles_ExtendedProperties_Property_GUID():
    return Guid('f451cda0-ba0a-4681-b0-b0-0d-bd-b5-3e-58-f3')
def _define_SpreadsheetItem_Formula_Property_GUID():
    return Guid('e602e47d-1b47-4bea-87-cf-3b-0b-0b-5c-15-b6')
def _define_SpreadsheetItem_AnnotationObjects_Property_GUID():
    return Guid('a3194c38-c9bc-4604-93-96-ae-3f-9f-45-7f-7b')
def _define_SpreadsheetItem_AnnotationTypes_Property_GUID():
    return Guid('c70c51d0-d602-4b45-af-bc-b4-71-2b-96-d7-2b')
def _define_Transform2_CanZoom_Property_GUID():
    return Guid('f357e890-a756-4359-9c-a6-86-70-2b-f8-f3-81')
def _define_LiveSetting_Property_GUID():
    return Guid('c12bcd8e-2a8e-4950-8a-e7-36-25-11-1d-58-eb')
def _define_Drag_IsGrabbed_Property_GUID():
    return Guid('45f206f3-75cc-4cca-a9-b9-fc-df-b9-82-d8-a2')
def _define_Drag_GrabbedItems_Property_GUID():
    return Guid('77c1562c-7b86-4b21-9e-d7-3c-ef-da-6f-4c-43')
def _define_Drag_DropEffect_Property_GUID():
    return Guid('646f2779-48d3-4b23-89-02-4b-f1-00-00-5d-f3')
def _define_Drag_DropEffects_Property_GUID():
    return Guid('f5d61156-7ce6-49be-a8-36-92-69-dc-ec-92-0f')
def _define_DropTarget_DropTargetEffect_Property_GUID():
    return Guid('8bb75975-a0ca-4981-b8-18-87-fc-66-e9-50-9d')
def _define_DropTarget_DropTargetEffects_Property_GUID():
    return Guid('bc1dd4ed-cb89-45f1-a5-92-e0-3b-08-ae-79-0f')
def _define_Transform2_ZoomLevel_Property_GUID():
    return Guid('eee29f1a-f4a2-4b5b-ac-65-95-cf-93-28-33-87')
def _define_Transform2_ZoomMinimum_Property_GUID():
    return Guid('742ccc16-4ad1-4e07-96-fe-b1-22-c6-e6-b2-2b')
def _define_Transform2_ZoomMaximum_Property_GUID():
    return Guid('42ab6b77-ceb0-4eca-b8-2a-6c-fa-5f-a1-fc-08')
def _define_FlowsFrom_Property_GUID():
    return Guid('05c6844f-19de-48f8-95-fa-88-0d-5b-0f-d6-15')
def _define_FillColor_Property_GUID():
    return Guid('6e0ec4d0-e2a8-4a56-9d-e7-95-33-89-93-3b-39')
def _define_OutlineColor_Property_GUID():
    return Guid('c395d6c0-4b55-4762-a0-73-fd-30-3a-63-4f-52')
def _define_FillType_Property_GUID():
    return Guid('c6fc74e4-8cb9-429c-a9-e1-9b-c4-ac-37-2b-62')
def _define_VisualEffects_Property_GUID():
    return Guid('e61a8565-aad9-46d7-9e-70-4e-8a-84-20-d4-20')
def _define_OutlineThickness_Property_GUID():
    return Guid('13e67cc7-dac2-4888-bd-d3-37-5c-62-fa-96-18')
def _define_CenterPoint_Property_GUID():
    return Guid('0cb00c08-540c-4edb-94-45-26-35-9e-a6-97-85')
def _define_Rotation_Property_GUID():
    return Guid('767cdc7d-aec0-4110-ad-32-30-ed-d4-03-49-2e')
def _define_Size_Property_GUID():
    return Guid('2b5f761d-f885-4404-97-3f-9b-1d-98-e3-6d-8f')
def _define_ToolTipOpened_Event_GUID():
    return Guid('3f4b97ff-2edc-451d-bc-a4-95-a3-18-8d-5b-03')
def _define_ToolTipClosed_Event_GUID():
    return Guid('276d71ef-24a9-49b6-8e-97-da-98-b4-01-bb-cd')
def _define_StructureChanged_Event_GUID():
    return Guid('59977961-3edd-4b11-b1-3b-67-6b-2a-2a-6c-a9')
def _define_MenuOpened_Event_GUID():
    return Guid('ebe2e945-66ca-4ed1-9f-f8-2a-d7-df-0a-1b-08')
def _define_AutomationPropertyChanged_Event_GUID():
    return Guid('2527fba1-8d7a-4630-a4-cc-e6-63-15-94-2f-52')
def _define_AutomationFocusChanged_Event_GUID():
    return Guid('b68a1f17-f60d-41a7-a3-cc-b0-52-92-15-5f-e0')
def _define_ActiveTextPositionChanged_Event_GUID():
    return Guid('a5c09e9c-c77d-4f25-b4-91-e5-bb-70-17-cb-d4')
def _define_AsyncContentLoaded_Event_GUID():
    return Guid('5fdee11c-d2fa-4fb9-90-4e-5c-be-e8-94-d5-ef')
def _define_MenuClosed_Event_GUID():
    return Guid('3cf1266e-1582-4041-ac-d7-88-a3-5a-96-52-97')
def _define_LayoutInvalidated_Event_GUID():
    return Guid('ed7d6544-a6bd-4595-9b-ae-3d-28-94-6c-c7-15')
def _define_Invoke_Invoked_Event_GUID():
    return Guid('dfd699f0-c915-49dd-b4-22-dd-e7-85-c3-d2-4b')
def _define_SelectionItem_ElementAddedToSelectionEvent_Event_GUID():
    return Guid('3c822dd1-c407-4dba-91-dd-79-d4-ae-d0-ae-c6')
def _define_SelectionItem_ElementRemovedFromSelectionEvent_Event_GUID():
    return Guid('097fa8a9-7079-41af-8b-9c-09-34-d8-30-5e-5c')
def _define_SelectionItem_ElementSelectedEvent_Event_GUID():
    return Guid('b9c7dbfb-4ebe-4532-aa-f4-00-8c-f6-47-23-3c')
def _define_Selection_InvalidatedEvent_Event_GUID():
    return Guid('cac14904-16b4-4b53-8e-47-4c-b1-df-26-7b-b7')
def _define_Text_TextSelectionChangedEvent_Event_GUID():
    return Guid('918edaa1-71b3-49ae-97-41-79-be-b8-d3-58-f3')
def _define_Text_TextChangedEvent_Event_GUID():
    return Guid('4a342082-f483-48c4-ac-11-a8-4b-43-5e-2a-84')
def _define_Window_WindowOpened_Event_GUID():
    return Guid('d3e81d06-de45-4f2f-96-33-de-9e-02-fb-65-af')
def _define_Window_WindowClosed_Event_GUID():
    return Guid('edf141f8-fa67-4e22-bb-f7-94-4e-05-73-5e-e2')
def _define_MenuModeStart_Event_GUID():
    return Guid('18d7c631-166a-4ac9-ae-3b-ef-4b-54-20-e6-81')
def _define_MenuModeEnd_Event_GUID():
    return Guid('9ecd4c9f-80dd-47b8-82-67-5a-ec-06-bb-2c-ff')
def _define_InputReachedTarget_Event_GUID():
    return Guid('93ed549a-0549-40f0-be-db-28-e4-4f-7d-e2-a3')
def _define_InputReachedOtherElement_Event_GUID():
    return Guid('ed201d8a-4e6c-415e-a8-74-24-60-c9-b6-6b-a8')
def _define_InputDiscarded_Event_GUID():
    return Guid('7f36c367-7b18-417c-97-e3-9d-58-dd-c9-44-ab')
def _define_SystemAlert_Event_GUID():
    return Guid('d271545d-7a3a-47a7-84-74-81-d2-9a-24-51-c9')
def _define_LiveRegionChanged_Event_GUID():
    return Guid('102d5e90-e6a9-41b6-b1-c5-a9-b1-92-9d-95-10')
def _define_HostedFragmentRootsInvalidated_Event_GUID():
    return Guid('e6bdb03e-0921-4ec5-8d-cf-ea-e8-77-b0-42-6b')
def _define_Drag_DragStart_Event_GUID():
    return Guid('883a480b-3aa9-429d-95-e4-d9-c8-d0-11-f0-dd')
def _define_Drag_DragCancel_Event_GUID():
    return Guid('c3ede6fa-3451-4e0f-9e-71-df-9c-28-0a-46-57')
def _define_Drag_DragComplete_Event_GUID():
    return Guid('38e96188-ef1f-463e-91-ca-3a-77-92-c2-9c-af')
def _define_DropTarget_DragEnter_Event_GUID():
    return Guid('aad9319b-032c-4a88-96-1d-1c-f5-79-58-1e-34')
def _define_DropTarget_DragLeave_Event_GUID():
    return Guid('0f82eb15-24a2-4988-92-17-de-16-2a-ee-27-2b')
def _define_DropTarget_Dropped_Event_GUID():
    return Guid('622cead8-1edb-4a3d-ab-bc-be-22-11-ff-68-b5')
def _define_StructuredMarkup_CompositionComplete_Event_GUID():
    return Guid('c48a3c17-677a-4047-a6-8d-fc-12-57-52-8a-ef')
def _define_StructuredMarkup_Deleted_Event_GUID():
    return Guid('f9d0a020-e1c1-4ecf-b9-aa-52-ef-de-7e-41-e1')
def _define_StructuredMarkup_SelectionChanged_Event_GUID():
    return Guid('a7c815f7-ff9f-41c7-a3-a7-ab-6c-bf-db-49-03')
def _define_Invoke_Pattern_GUID():
    return Guid('d976c2fc-66ea-4a6e-b2-8f-c2-4c-75-46-ad-37')
def _define_Selection_Pattern_GUID():
    return Guid('66e3b7e8-d821-4d25-87-61-43-5d-2c-8b-25-3f')
def _define_Value_Pattern_GUID():
    return Guid('17faad9e-c877-475b-b9-33-77-33-27-79-b6-37')
def _define_RangeValue_Pattern_GUID():
    return Guid('18b00d87-b1c9-476a-bf-bd-5f-0b-db-92-6f-63')
def _define_Scroll_Pattern_GUID():
    return Guid('895fa4b4-759d-4c50-8e-15-03-46-06-72-00-3c')
def _define_ExpandCollapse_Pattern_GUID():
    return Guid('ae05efa2-f9d1-428a-83-4c-53-a5-c5-2f-9b-8b')
def _define_Grid_Pattern_GUID():
    return Guid('260a2ccb-93a8-4e44-a4-c1-3d-f3-97-f2-b0-2b')
def _define_GridItem_Pattern_GUID():
    return Guid('f2d5c877-a462-4957-a2-a5-2c-96-b3-03-bc-63')
def _define_MultipleView_Pattern_GUID():
    return Guid('547a6ae4-113f-47c4-85-0f-db-4d-fa-46-6b-1d')
def _define_Window_Pattern_GUID():
    return Guid('27901735-c760-4994-ad-11-59-19-e6-06-b1-10')
def _define_SelectionItem_Pattern_GUID():
    return Guid('9bc64eeb-87c7-4b28-94-bb-4d-9f-a4-37-b6-ef')
def _define_Dock_Pattern_GUID():
    return Guid('9cbaa846-83c8-428d-82-7f-7e-60-63-fe-06-20')
def _define_Table_Pattern_GUID():
    return Guid('c415218e-a028-461e-aa-92-8f-92-5c-f7-93-51')
def _define_TableItem_Pattern_GUID():
    return Guid('df1343bd-1888-4a29-a5-0c-b9-2e-6d-e3-7f-6f')
def _define_Text_Pattern_GUID():
    return Guid('8615f05d-7de5-44fd-a6-79-2c-a4-b4-60-33-a8')
def _define_Toggle_Pattern_GUID():
    return Guid('0b419760-e2f4-43ff-8c-5f-94-57-c8-2b-56-e9')
def _define_Transform_Pattern_GUID():
    return Guid('24b46fdb-587e-49f1-9c-4a-d8-e9-8b-66-4b-7b')
def _define_ScrollItem_Pattern_GUID():
    return Guid('4591d005-a803-4d5c-b4-d5-8d-28-00-f9-06-a7')
def _define_LegacyIAccessible_Pattern_GUID():
    return Guid('54cc0a9f-3395-48af-ba-8d-73-f8-56-90-f3-e0')
def _define_ItemContainer_Pattern_GUID():
    return Guid('3d13da0f-8b9a-4a99-85-fa-c5-c9-a6-9f-1e-d4')
def _define_VirtualizedItem_Pattern_GUID():
    return Guid('f510173e-2e71-45e9-a6-e5-62-f6-ed-82-89-d5')
def _define_SynchronizedInput_Pattern_GUID():
    return Guid('05c288a6-c47b-488b-b6-53-33-97-7a-55-1b-8b')
def _define_ObjectModel_Pattern_GUID():
    return Guid('3e04acfe-08fc-47ec-96-bc-35-3f-a3-b3-4a-a7')
def _define_Annotation_Pattern_GUID():
    return Guid('f6c72ad7-356c-4850-92-91-31-6f-60-8a-8c-84')
def _define_Text_Pattern2_GUID():
    return Guid('498479a2-5b22-448d-b6-e4-64-74-90-86-06-98')
def _define_TextEdit_Pattern_GUID():
    return Guid('69f3ff89-5af9-4c75-93-40-f2-de-29-2e-45-91')
def _define_CustomNavigation_Pattern_GUID():
    return Guid('afea938a-621e-4054-bb-2c-2f-46-11-4d-ac-3f')
def _define_Styles_Pattern_GUID():
    return Guid('1ae62655-da72-4d60-a1-53-e5-aa-69-88-e3-bf')
def _define_Spreadsheet_Pattern_GUID():
    return Guid('6a5b24c9-9d1e-4b85-9e-44-c0-2e-31-69-b1-0b')
def _define_SpreadsheetItem_Pattern_GUID():
    return Guid('32cf83ff-f1a8-4a8c-86-58-d4-7b-a7-4e-20-ba')
def _define_Tranform_Pattern2_GUID():
    return Guid('8afcfd07-a369-44de-98-8b-2f-7f-f4-9f-b8-a8')
def _define_TextChild_Pattern_GUID():
    return Guid('7533cab7-3bfe-41ef-9e-85-e2-63-8c-be-16-9e')
def _define_Drag_Pattern_GUID():
    return Guid('c0bee21f-ccb3-4fed-99-5b-11-4f-6e-3d-27-28')
def _define_DropTarget_Pattern_GUID():
    return Guid('0bcbec56-bd34-4b7b-9f-d5-26-59-90-5e-a3-dc')
def _define_StructuredMarkup_Pattern_GUID():
    return Guid('abbd0878-8665-4f5c-94-fc-36-e7-d8-bb-70-6b')
def _define_Button_Control_GUID():
    return Guid('5a78e369-c6a1-4f33-a9-d7-79-f2-0d-0c-78-8e')
def _define_Calendar_Control_GUID():
    return Guid('8913eb88-00e5-46bc-8e-4e-14-a7-86-e1-65-a1')
def _define_CheckBox_Control_GUID():
    return Guid('fb50f922-a3db-49c0-8b-c3-06-da-d5-57-78-e2')
def _define_ComboBox_Control_GUID():
    return Guid('54cb426c-2f33-4fff-aa-a1-ae-f6-0d-ac-5d-eb')
def _define_Edit_Control_GUID():
    return Guid('6504a5c8-2c86-4f87-ae-7b-1a-bd-dc-81-0c-f9')
def _define_Hyperlink_Control_GUID():
    return Guid('8a56022c-b00d-4d15-8f-f0-5b-6b-26-6e-5e-02')
def _define_Image_Control_GUID():
    return Guid('2d3736e4-6b16-4c57-a9-62-f9-32-60-a7-52-43')
def _define_ListItem_Control_GUID():
    return Guid('7b3717f2-44d1-4a58-98-a8-f1-2a-9b-8f-78-e2')
def _define_List_Control_GUID():
    return Guid('9b149ee1-7cca-4cfc-9a-f1-ca-c7-bd-dd-30-31')
def _define_Menu_Control_GUID():
    return Guid('2e9b1440-0ea8-41fd-b3-74-c1-ea-6f-50-3c-d1')
def _define_MenuBar_Control_GUID():
    return Guid('cc384250-0e7b-4ae8-95-ae-a0-8f-26-1b-52-ee')
def _define_MenuItem_Control_GUID():
    return Guid('f45225d3-d0a0-49d8-98-34-9a-00-0d-2a-ed-dc')
def _define_ProgressBar_Control_GUID():
    return Guid('228c9f86-c36c-47bb-9f-b6-a5-83-4b-fc-53-a4')
def _define_RadioButton_Control_GUID():
    return Guid('3bdb49db-fe2c-4483-b3-e1-e5-7f-21-94-40-c6')
def _define_ScrollBar_Control_GUID():
    return Guid('daf34b36-5065-4946-b2-2f-92-59-5f-c0-75-1a')
def _define_Slider_Control_GUID():
    return Guid('b033c24b-3b35-4cea-b6-09-76-36-82-fa-66-0b')
def _define_Spinner_Control_GUID():
    return Guid('60cc4b38-3cb1-4161-b4-42-c6-b7-26-c1-78-25')
def _define_StatusBar_Control_GUID():
    return Guid('d45e7d1b-5873-475f-95-a4-04-33-e1-f1-b0-0a')
def _define_Tab_Control_GUID():
    return Guid('38cd1f2d-337a-4bd2-a5-e3-ad-b4-69-e3-0b-d3')
def _define_TabItem_Control_GUID():
    return Guid('2c6a634f-921b-4e6e-b2-6e-08-fc-b0-79-8f-4c')
def _define_Text_Control_GUID():
    return Guid('ae9772dc-d331-4f09-be-20-7e-6d-fa-f0-7b-0a')
def _define_ToolBar_Control_GUID():
    return Guid('8f06b751-e182-4e98-88-93-22-84-54-3a-7d-ce')
def _define_ToolTip_Control_GUID():
    return Guid('05ddc6d1-2137-4768-98-ea-73-f5-2f-71-34-f3')
def _define_Tree_Control_GUID():
    return Guid('7561349c-d241-43f4-99-08-b5-f0-91-be-e6-11')
def _define_TreeItem_Control_GUID():
    return Guid('62c9feb9-8ffc-4878-a3-a4-96-b0-30-31-5c-18')
def _define_Custom_Control_GUID():
    return Guid('f29ea0c3-adb7-430a-ba-90-e5-2c-73-13-e6-ed')
def _define_Group_Control_GUID():
    return Guid('ad50aa1c-e8c8-4774-ae-1b-dd-86-df-0b-3b-dc')
def _define_Thumb_Control_GUID():
    return Guid('701ca877-e310-4dd6-b6-44-79-7e-4f-ae-a2-13')
def _define_DataGrid_Control_GUID():
    return Guid('84b783af-d103-4b0a-84-15-e7-39-42-41-0f-4b')
def _define_DataItem_Control_GUID():
    return Guid('a0177842-d94f-42a5-81-4b-60-68-ad-dc-8d-a5')
def _define_Document_Control_GUID():
    return Guid('3cd6bb6f-6f08-4562-b2-29-e4-e2-fc-7a-9e-b4')
def _define_SplitButton_Control_GUID():
    return Guid('7011f01f-4ace-4901-b4-61-92-0a-6f-1c-a6-50')
def _define_Window_Control_GUID():
    return Guid('e13a7242-f462-4f4d-ae-c1-53-b2-8d-6c-32-90')
def _define_Pane_Control_GUID():
    return Guid('5c2b3f5b-9182-42a3-8d-ec-8c-04-c1-ee-63-4d')
def _define_Header_Control_GUID():
    return Guid('5b90cbce-78fb-4614-82-b6-55-4d-74-71-8e-67')
def _define_HeaderItem_Control_GUID():
    return Guid('e6bc12cb-7c8e-49cf-b1-68-4a-93-a3-2b-eb-b0')
def _define_Table_Control_GUID():
    return Guid('773bfa0e-5bc4-4deb-92-1b-de-7b-32-06-22-9e')
def _define_TitleBar_Control_GUID():
    return Guid('98aa55bf-3bb0-4b65-83-6e-2e-a3-0d-bc-17-1f')
def _define_Separator_Control_GUID():
    return Guid('8767eba3-2a63-4ab0-ac-8d-aa-50-e2-3d-e9-78')
def _define_SemanticZoom_Control_GUID():
    return Guid('5fd34a43-061e-42c8-b5-89-9d-cc-f7-4b-c4-3a')
def _define_AppBar_Control_GUID():
    return Guid('6114908d-cc02-4d37-87-5b-b5-30-c7-13-95-54')
def _define_Text_AnimationStyle_Attribute_GUID():
    return Guid('628209f0-7c9a-4d57-be-64-1f-18-36-57-1f-f5')
def _define_Text_BackgroundColor_Attribute_GUID():
    return Guid('fdc49a07-583d-4f17-ad-27-77-fc-83-2a-3c-0b')
def _define_Text_BulletStyle_Attribute_GUID():
    return Guid('c1097c90-d5c4-4237-97-81-3b-ec-8b-a5-4e-48')
def _define_Text_CapStyle_Attribute_GUID():
    return Guid('fb059c50-92cc-49a5-ba-8f-0a-a8-72-bb-a2-f3')
def _define_Text_Culture_Attribute_GUID():
    return Guid('c2025af9-a42d-4ced-a1-fb-c6-74-63-15-22-2e')
def _define_Text_FontName_Attribute_GUID():
    return Guid('64e63ba8-f2e5-476e-a4-77-17-34-fe-aa-f7-26')
def _define_Text_FontSize_Attribute_GUID():
    return Guid('dc5eeeff-0506-4673-93-f2-37-7e-4a-8e-01-f1')
def _define_Text_FontWeight_Attribute_GUID():
    return Guid('6fc02359-b316-4f5f-b4-01-f1-ce-55-74-18-53')
def _define_Text_ForegroundColor_Attribute_GUID():
    return Guid('72d1c95d-5e60-471a-96-b1-6c-1b-3b-77-a4-36')
def _define_Text_HorizontalTextAlignment_Attribute_GUID():
    return Guid('04ea6161-fba3-477a-95-2a-bb-32-6d-02-6a-5b')
def _define_Text_IndentationFirstLine_Attribute_GUID():
    return Guid('206f9ad5-c1d3-424a-81-82-6d-a9-a7-f3-d6-32')
def _define_Text_IndentationLeading_Attribute_GUID():
    return Guid('5cf66bac-2d45-4a4b-b6-c9-f7-22-1d-28-15-b0')
def _define_Text_IndentationTrailing_Attribute_GUID():
    return Guid('97ff6c0f-1ce4-408a-b6-7b-94-d8-3e-b6-9b-f2')
def _define_Text_IsHidden_Attribute_GUID():
    return Guid('360182fb-bdd7-47f6-ab-69-19-e3-3f-8a-33-44')
def _define_Text_IsItalic_Attribute_GUID():
    return Guid('fce12a56-1336-4a34-96-63-1b-ab-47-23-93-20')
def _define_Text_IsReadOnly_Attribute_GUID():
    return Guid('a738156b-ca3e-495e-95-14-83-3c-44-0f-eb-11')
def _define_Text_IsSubscript_Attribute_GUID():
    return Guid('f0ead858-8f53-413c-87-3f-1a-7d-7f-5e-0d-e4')
def _define_Text_IsSuperscript_Attribute_GUID():
    return Guid('da706ee4-b3aa-4645-a4-1f-cd-25-15-7d-ea-76')
def _define_Text_MarginBottom_Attribute_GUID():
    return Guid('7ee593c4-72b4-4cac-92-71-3e-d2-4b-0e-4d-42')
def _define_Text_MarginLeading_Attribute_GUID():
    return Guid('9e9242d0-5ed0-4900-8e-8a-ee-cc-03-83-5a-fc')
def _define_Text_MarginTop_Attribute_GUID():
    return Guid('683d936f-c9b9-4a9a-b3-d9-d2-0d-33-31-1e-2a')
def _define_Text_MarginTrailing_Attribute_GUID():
    return Guid('af522f98-999d-40af-a5-b2-01-69-d0-34-20-02')
def _define_Text_OutlineStyles_Attribute_GUID():
    return Guid('5b675b27-db89-46fe-97-0c-61-4d-52-3b-b9-7d')
def _define_Text_OverlineColor_Attribute_GUID():
    return Guid('83ab383a-fd43-40da-ab-3e-ec-f8-16-5c-bb-6d')
def _define_Text_OverlineStyle_Attribute_GUID():
    return Guid('0a234d66-617e-427f-87-1d-e1-ff-1e-0c-21-3f')
def _define_Text_StrikethroughColor_Attribute_GUID():
    return Guid('bfe15a18-8c41-4c5a-9a-0b-04-af-0e-07-f4-87')
def _define_Text_StrikethroughStyle_Attribute_GUID():
    return Guid('72913ef1-da00-4f01-89-9c-ac-5a-85-77-a3-07')
def _define_Text_Tabs_Attribute_GUID():
    return Guid('2e68d00b-92fe-42d8-89-9a-a7-84-aa-44-54-a1')
def _define_Text_TextFlowDirections_Attribute_GUID():
    return Guid('8bdf8739-f420-423e-af-77-20-a5-d9-73-a9-07')
def _define_Text_UnderlineColor_Attribute_GUID():
    return Guid('bfa12c73-fde2-4473-bf-64-10-36-d6-aa-0f-45')
def _define_Text_UnderlineStyle_Attribute_GUID():
    return Guid('5f3b21c0-ede4-44bd-9c-36-38-53-03-8c-bf-eb')
def _define_Text_AnnotationTypes_Attribute_GUID():
    return Guid('ad2eb431-ee4e-4be1-a7-ba-55-59-15-5a-73-ef')
def _define_Text_AnnotationObjects_Attribute_GUID():
    return Guid('ff41cf68-e7ab-40b9-8c-72-72-a8-ed-94-01-7d')
def _define_Text_StyleName_Attribute_GUID():
    return Guid('22c9e091-4d66-45d8-a8-28-73-7b-ab-4c-98-a7')
def _define_Text_StyleId_Attribute_GUID():
    return Guid('14c300de-c32b-449b-ab-7c-b0-e0-78-9a-ea-5d')
def _define_Text_Link_Attribute_GUID():
    return Guid('b38ef51d-9e8d-4e46-91-44-56-eb-e1-77-32-9b')
def _define_Text_IsActive_Attribute_GUID():
    return Guid('f5a4e533-e1b8-436b-93-5d-b5-7a-a3-f5-58-c4')
def _define_Text_SelectionActiveEnd_Attribute_GUID():
    return Guid('1f668cc3-9bbf-416b-b0-a2-f8-9f-86-f6-61-2c')
def _define_Text_CaretPosition_Attribute_GUID():
    return Guid('b227b131-9889-4752-a9-1b-73-3e-fd-c5-c5-a0')
def _define_Text_CaretBidiMode_Attribute_GUID():
    return Guid('929ee7a6-51d3-4715-96-dc-b6-94-fa-24-a1-68')
def _define_Text_BeforeParagraphSpacing_Attribute_GUID():
    return Guid('be7b0ab1-c822-4a24-85-e9-c8-f2-65-0f-c7-9c')
def _define_Text_AfterParagraphSpacing_Attribute_GUID():
    return Guid('588cbb38-e62f-497c-b5-d1-cc-df-0e-e8-23-d8')
def _define_Text_LineSpacing_Attribute_GUID():
    return Guid('63ff70ae-d943-4b47-8a-b7-a7-a0-33-d3-21-4b')
def _define_Text_BeforeSpacing_Attribute_GUID():
    return Guid('be7b0ab1-c822-4a24-85-e9-c8-f2-65-0f-c7-9c')
def _define_Text_AfterSpacing_Attribute_GUID():
    return Guid('588cbb38-e62f-497c-b5-d1-cc-df-0e-e8-23-d8')
def _define_Text_SayAsInterpretAs_Attribute_GUID():
    return Guid('b38ad6ac-eee1-4b6e-88-cc-01-4c-ef-a9-3f-cb')
def _define_TextEdit_TextChanged_Event_GUID():
    return Guid('120b0308-ec22-4eb8-9c-98-98-67-cd-a1-b1-65')
def _define_TextEdit_ConversionTargetChanged_Event_GUID():
    return Guid('3388c183-ed4f-4c8b-9b-aa-36-4d-51-d8-84-7f')
def _define_Changes_Event_GUID():
    return Guid('7df26714-614f-4e05-94-88-71-6c-5b-a1-94-36')
def _define_Annotation_Custom_GUID():
    return Guid('9ec82750-3931-4952-85-bc-1d-bf-f7-8a-43-e3')
def _define_Annotation_SpellingError_GUID():
    return Guid('ae85567e-9ece-423f-81-b7-96-c4-3d-53-e5-0e')
def _define_Annotation_GrammarError_GUID():
    return Guid('757a048d-4518-41c6-85-4c-dc-00-9b-7c-fb-53')
def _define_Annotation_Comment_GUID():
    return Guid('fd2fda30-26b3-4c06-8b-c7-98-f1-53-2e-46-fd')
def _define_Annotation_FormulaError_GUID():
    return Guid('95611982-0cab-46d5-a2-f0-e3-0d-19-05-f8-bf')
def _define_Annotation_TrackChanges_GUID():
    return Guid('21e6e888-dc14-4016-ac-27-19-05-53-c8-c4-70')
def _define_Annotation_Header_GUID():
    return Guid('867b409b-b216-4472-a2-19-52-5e-31-06-81-f8')
def _define_Annotation_Footer_GUID():
    return Guid('cceab046-1833-47aa-80-80-70-1e-d0-b0-c8-32')
def _define_Annotation_Highlighted_GUID():
    return Guid('757c884e-8083-4081-8b-9c-e8-7f-50-72-f0-e4')
def _define_Annotation_Endnote_GUID():
    return Guid('7565725c-2d99-4839-96-0d-33-d3-b8-66-ab-a5')
def _define_Annotation_Footnote_GUID():
    return Guid('3de10e21-4125-42db-86-20-be-80-83-08-06-24')
def _define_Annotation_InsertionChange_GUID():
    return Guid('0dbeb3a6-df15-4164-a3-c0-e2-1a-8c-e9-31-c4')
def _define_Annotation_DeletionChange_GUID():
    return Guid('be3d5b05-951d-42e7-90-1d-ad-c8-c2-cf-34-d0')
def _define_Annotation_MoveChange_GUID():
    return Guid('9da587eb-23e5-4490-b3-85-1a-22-dd-c8-b1-87')
def _define_Annotation_FormatChange_GUID():
    return Guid('eb247345-d4f1-41ce-8e-52-f7-9b-69-63-5e-48')
def _define_Annotation_UnsyncedChange_GUID():
    return Guid('1851116a-0e47-4b30-8c-b5-d7-da-e4-fb-cd-1b')
def _define_Annotation_EditingLockedChange_GUID():
    return Guid('c31f3e1c-7423-4dac-83-48-41-f0-99-ff-6f-64')
def _define_Annotation_ExternalChange_GUID():
    return Guid('75a05b31-5f11-42fd-88-7d-df-a0-10-db-23-92')
def _define_Annotation_ConflictingChange_GUID():
    return Guid('98af8802-517c-459f-af-13-01-6d-3f-ab-87-7e')
def _define_Annotation_Author_GUID():
    return Guid('f161d3a7-f81b-4128-b1-7f-71-f6-90-91-45-20')
def _define_Annotation_AdvancedProofingIssue_GUID():
    return Guid('dac7b72c-c0f2-4b84-b9-0d-5f-af-c0-f0-ef-1c')
def _define_Annotation_DataValidationError_GUID():
    return Guid('c8649fa8-9775-437e-ad-46-e7-09-d9-3c-23-43')
def _define_Annotation_CircularReferenceError_GUID():
    return Guid('25bd9cf4-1745-4659-ba-67-72-7f-03-18-c6-16')
def _define_Annotation_Mathematics_GUID():
    return Guid('eaab634b-26d0-40c1-80-73-57-ca-1c-63-3c-9b')
def _define_Annotation_Sensitive_GUID():
    return Guid('37f4c04f-0f12-4464-92-9c-82-8f-d1-52-92-e3')
def _define_Changes_Summary_GUID():
    return Guid('313d65a6-e60f-4d62-98-61-55-af-d7-28-d2-07')
def _define_StyleId_Custom_GUID():
    return Guid('ef2edd3e-a999-4b7c-a3-78-09-bb-d5-2a-35-16')
def _define_StyleId_Heading1_GUID():
    return Guid('7f7e8f69-6866-4621-93-0c-9a-5d-0c-a5-96-1c')
def _define_StyleId_Heading2_GUID():
    return Guid('baa9b241-5c69-469d-85-ad-47-47-37-b5-2b-14')
def _define_StyleId_Heading3_GUID():
    return Guid('bf8be9d2-d8b8-4ec5-8c-52-9c-fb-0d-03-59-70')
def _define_StyleId_Heading4_GUID():
    return Guid('8436ffc0-9578-45fc-83-a4-ff-40-05-33-15-dd')
def _define_StyleId_Heading5_GUID():
    return Guid('909f424d-0dbf-406e-97-bb-4e-77-3d-97-98-f7')
def _define_StyleId_Heading6_GUID():
    return Guid('89d23459-5d5b-4824-a4-20-11-d3-ed-82-e4-0f')
def _define_StyleId_Heading7_GUID():
    return Guid('a3790473-e9ae-422d-b8-e3-3b-67-5c-61-81-a4')
def _define_StyleId_Heading8_GUID():
    return Guid('2bc14145-a40c-4881-84-ae-f2-23-56-85-38-0c')
def _define_StyleId_Heading9_GUID():
    return Guid('c70d9133-bb2a-43d3-8a-c6-33-65-78-84-b0-f0')
def _define_StyleId_Title_GUID():
    return Guid('15d8201a-ffcf-481f-b0-a1-30-b6-3b-e9-8f-07')
def _define_StyleId_Subtitle_GUID():
    return Guid('b5d9fc17-5d6f-4420-b4-39-7c-b1-9a-d4-34-e2')
def _define_StyleId_Normal_GUID():
    return Guid('cd14d429-e45e-4475-a1-c5-7f-9e-6b-e9-6e-ba')
def _define_StyleId_Emphasis_GUID():
    return Guid('ca6e7dbe-355e-4820-95-a0-92-5f-04-1d-34-70')
def _define_StyleId_Quote_GUID():
    return Guid('5d1c21ea-8195-4f6c-87-ea-5d-ab-ec-e6-4c-1d')
def _define_StyleId_BulletedList_GUID():
    return Guid('5963ed64-6426-4632-8c-af-a3-2a-d4-02-d9-1a')
def _define_StyleId_NumberedList_GUID():
    return Guid('1e96dbd5-64c3-43d0-b1-ee-b5-3b-06-e3-ed-df')
def _define_Notification_Event_GUID():
    return Guid('72c5a2f7-9788-480f-b8-eb-4d-ee-00-f6-18-6f')
def _define_SID_IsUIAutomationObject():
    return Guid('b96fdb85-7204-4724-84-2b-c7-05-9d-ed-b9-d0')
def _define_SID_ControlElementProvider():
    return Guid('f4791d68-e254-4ba3-9a-53-26-a5-c5-49-79-46')
def _define_IsSelectionPattern2Available_Property_GUID():
    return Guid('490806fb-6e89-4a47-83-19-d2-66-e5-11-f0-21')
def _define_Selection2_FirstSelectedItem_Property_GUID():
    return Guid('cc24ea67-369c-4e55-9f-f7-38-da-69-54-0c-29')
def _define_Selection2_LastSelectedItem_Property_GUID():
    return Guid('cf7bda90-2d83-49f8-86-0c-9c-e3-94-cf-89-b4')
def _define_Selection2_CurrentSelectedItem_Property_GUID():
    return Guid('34257c26-83b5-41a6-93-9c-ae-84-1c-13-62-36')
def _define_Selection2_ItemCount_Property_GUID():
    return Guid('bb49eb9f-456d-4048-b5-91-9c-20-26-b8-46-36')
def _define_Selection_Pattern2_GUID():
    return Guid('fba25cab-ab98-49f7-a7-dc-fe-53-9d-c1-5b-e7')
def _define_HeadingLevel_Property_GUID():
    return Guid('29084272-aaaf-4a30-87-96-3c-12-f6-2b-6b-bb')
def _define_IsDialog_Property_GUID():
    return Guid('9d0dfb9b-8436-4501-bb-bb-e5-34-a4-fb-3b-3f')
UIA_IAFP_DEFAULT = 0
UIA_IAFP_UNWRAP_BRIDGE = 1
UIA_PFIA_DEFAULT = 0
UIA_PFIA_UNWRAP_BRIDGE = 1
UIA_ScrollPatternNoScroll = -1
def _define_LresultFromObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.LRESULT,POINTER(Guid),win32more.Foundation.WPARAM,win32more.System.Com.IUnknown_head)(('LresultFromObject', windll['OLEACC.dll']), ((1, 'riid'),(1, 'wParam'),(1, 'punk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ObjectFromLresult():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LRESULT,POINTER(Guid),win32more.Foundation.WPARAM,POINTER(c_void_p))(('ObjectFromLresult', windll['OLEACC.dll']), ((1, 'lResult'),(1, 'riid'),(1, 'wParam'),(1, 'ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowFromAccessibleObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessible_head,POINTER(win32more.Foundation.HWND))(('WindowFromAccessibleObject', windll['OLEACC.dll']), ((1, 'param0'),(1, 'phwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessibleObjectFromWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,POINTER(Guid),POINTER(c_void_p))(('AccessibleObjectFromWindow', windll['OLEACC.dll']), ((1, 'hwnd'),(1, 'dwId'),(1, 'riid'),(1, 'ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessibleObjectFromEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,UInt32,POINTER(win32more.UI.Accessibility.IAccessible_head),POINTER(win32more.System.Com.VARIANT_head))(('AccessibleObjectFromEvent', windll['OLEACC.dll']), ((1, 'hwnd'),(1, 'dwId'),(1, 'dwChildId'),(1, 'ppacc'),(1, 'pvarChild'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessibleObjectFromPoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,POINTER(win32more.UI.Accessibility.IAccessible_head),POINTER(win32more.System.Com.VARIANT_head))(('AccessibleObjectFromPoint', windll['OLEACC.dll']), ((1, 'ptScreen'),(1, 'ppacc'),(1, 'pvarChild'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessibleChildren():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessible_head,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32))(('AccessibleChildren', windll['OLEACC.dll']), ((1, 'paccContainer'),(1, 'iChildStart'),(1, 'cChildren'),(1, 'rgvarChildren'),(1, 'pcObtained'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRoleTextA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PSTR,UInt32)(('GetRoleTextA', windll['OLEACC.dll']), ((1, 'lRole'),(1, 'lpszRole'),(1, 'cchRoleMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRoleTextW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR,UInt32)(('GetRoleTextW', windll['OLEACC.dll']), ((1, 'lRole'),(1, 'lpszRole'),(1, 'cchRoleMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStateTextA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PSTR,UInt32)(('GetStateTextA', windll['OLEACC.dll']), ((1, 'lStateBit'),(1, 'lpszState'),(1, 'cchState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStateTextW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR,UInt32)(('GetStateTextW', windll['OLEACC.dll']), ((1, 'lStateBit'),(1, 'lpszState'),(1, 'cchState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOleaccVersionInfo():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(UInt32))(('GetOleaccVersionInfo', windll['OLEACC.dll']), ((1, 'pVer'),(1, 'pBuild'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateStdAccessibleObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,Int32,POINTER(Guid),POINTER(c_void_p))(('CreateStdAccessibleObject', windll['OLEACC.dll']), ((1, 'hwnd'),(1, 'idObject'),(1, 'riid'),(1, 'ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateStdAccessibleProxyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PSTR,Int32,POINTER(Guid),POINTER(c_void_p))(('CreateStdAccessibleProxyA', windll['OLEACC.dll']), ((1, 'hwnd'),(1, 'pClassName'),(1, 'idObject'),(1, 'riid'),(1, 'ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateStdAccessibleProxyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,Int32,POINTER(Guid),POINTER(c_void_p))(('CreateStdAccessibleProxyW', windll['OLEACC.dll']), ((1, 'hwnd'),(1, 'pClassName'),(1, 'idObject'),(1, 'riid'),(1, 'ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccSetRunningUtilityState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.UI.Accessibility.ACC_UTILITY_STATE_FLAGS)(('AccSetRunningUtilityState', windll['OLEACC.dll']), ((1, 'hwndApp'),(1, 'dwUtilityStateMask'),(1, 'dwUtilityState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccNotifyTouchInteraction():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.HWND,win32more.Foundation.POINT)(('AccNotifyTouchInteraction', windll['OLEACC.dll']), ((1, 'hwndApp'),(1, 'hwndTarget'),(1, 'ptTarget'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetErrorDescription():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.BSTR))(('UiaGetErrorDescription', windll['UIAutomationCore.dll']), ((1, 'pDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaHUiaNodeFromVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.UI.Accessibility.HUIANODE))(('UiaHUiaNodeFromVariant', windll['UIAutomationCore.dll']), ((1, 'pvar'),(1, 'phnode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaHPatternObjectFromVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.UI.Accessibility.HUIAPATTERNOBJECT))(('UiaHPatternObjectFromVariant', windll['UIAutomationCore.dll']), ((1, 'pvar'),(1, 'phobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaHTextRangeFromVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.UI.Accessibility.HUIATEXTRANGE))(('UiaHTextRangeFromVariant', windll['UIAutomationCore.dll']), ((1, 'pvar'),(1, 'phtextrange'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaNodeRelease():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Accessibility.HUIANODE)(('UiaNodeRelease', windll['UIAutomationCore.dll']), ((1, 'hnode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetPropertyValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,Int32,POINTER(win32more.System.Com.VARIANT_head))(('UiaGetPropertyValue', windll['UIAutomationCore.dll']), ((1, 'hnode'),(1, 'propertyId'),(1, 'pValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetPatternProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,Int32,POINTER(win32more.UI.Accessibility.HUIAPATTERNOBJECT))(('UiaGetPatternProvider', windll['UIAutomationCore.dll']), ((1, 'hnode'),(1, 'patternId'),(1, 'phobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetRuntimeId():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('UiaGetRuntimeId', windll['UIAutomationCore.dll']), ((1, 'hnode'),(1, 'pruntimeId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaSetFocus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE)(('UiaSetFocus', windll['UIAutomationCore.dll']), ((1, 'hnode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaNavigate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,win32more.UI.Accessibility.NavigateDirection,POINTER(win32more.UI.Accessibility.UiaCondition_head),POINTER(win32more.UI.Accessibility.UiaCacheRequest_head),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(win32more.Foundation.BSTR))(('UiaNavigate', windll['UIAutomationCore.dll']), ((1, 'hnode'),(1, 'direction'),(1, 'pCondition'),(1, 'pRequest'),(1, 'ppRequestedData'),(1, 'ppTreeStructure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetUpdatedCache():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,POINTER(win32more.UI.Accessibility.UiaCacheRequest_head),win32more.UI.Accessibility.NormalizeState,POINTER(win32more.UI.Accessibility.UiaCondition_head),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(win32more.Foundation.BSTR))(('UiaGetUpdatedCache', windll['UIAutomationCore.dll']), ((1, 'hnode'),(1, 'pRequest'),(1, 'normalizeState'),(1, 'pNormalizeCondition'),(1, 'ppRequestedData'),(1, 'ppTreeStructure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaFind():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,POINTER(win32more.UI.Accessibility.UiaFindParams_head),POINTER(win32more.UI.Accessibility.UiaCacheRequest_head),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('UiaFind', windll['UIAutomationCore.dll']), ((1, 'hnode'),(1, 'pParams'),(1, 'pRequest'),(1, 'ppRequestedData'),(1, 'ppOffsets'),(1, 'ppTreeStructures'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaNodeFromPoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,POINTER(win32more.UI.Accessibility.UiaCacheRequest_head),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(win32more.Foundation.BSTR))(('UiaNodeFromPoint', windll['UIAutomationCore.dll']), ((1, 'x'),(1, 'y'),(1, 'pRequest'),(1, 'ppRequestedData'),(1, 'ppTreeStructure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaNodeFromFocus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UiaCacheRequest_head),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(win32more.Foundation.BSTR))(('UiaNodeFromFocus', windll['UIAutomationCore.dll']), ((1, 'pRequest'),(1, 'ppRequestedData'),(1, 'ppTreeStructure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaNodeFromHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.UI.Accessibility.HUIANODE))(('UiaNodeFromHandle', windll['UIAutomationCore.dll']), ((1, 'hwnd'),(1, 'phnode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaNodeFromProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,POINTER(win32more.UI.Accessibility.HUIANODE))(('UiaNodeFromProvider', windll['UIAutomationCore.dll']), ((1, 'pProvider'),(1, 'phnode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetRootNode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.HUIANODE))(('UiaGetRootNode', windll['UIAutomationCore.dll']), ((1, 'phnode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRegisterProviderCallback():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.UI.Accessibility.UiaProviderCallback))(('UiaRegisterProviderCallback', windll['UIAutomationCore.dll']), ((1, 'pCallback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaLookupId():
    try:
        return WINFUNCTYPE(Int32,win32more.UI.Accessibility.AutomationIdentifierType,POINTER(Guid))(('UiaLookupId', windll['UIAutomationCore.dll']), ((1, 'type'),(1, 'pGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetReservedNotSupportedValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(('UiaGetReservedNotSupportedValue', windll['UIAutomationCore.dll']), ((1, 'punkNotSupportedValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetReservedMixedAttributeValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(('UiaGetReservedMixedAttributeValue', windll['UIAutomationCore.dll']), ((1, 'punkMixedAttributeValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaClientsAreListening():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('UiaClientsAreListening', windll['UIAutomationCore.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseAutomationPropertyChangedEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.UIA_PROPERTY_ID,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT)(('UiaRaiseAutomationPropertyChangedEvent', windll['UIAutomationCore.dll']), ((1, 'pProvider'),(1, 'id'),(1, 'oldValue'),(1, 'newValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseAutomationEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.UIA_EVENT_ID)(('UiaRaiseAutomationEvent', windll['UIAutomationCore.dll']), ((1, 'pProvider'),(1, 'id'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseStructureChangedEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.StructureChangeType,POINTER(Int32),Int32)(('UiaRaiseStructureChangedEvent', windll['UIAutomationCore.dll']), ((1, 'pProvider'),(1, 'structureChangeType'),(1, 'pRuntimeId'),(1, 'cRuntimeIdLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseAsyncContentLoadedEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.AsyncContentLoadedState,Double)(('UiaRaiseAsyncContentLoadedEvent', windll['UIAutomationCore.dll']), ((1, 'pProvider'),(1, 'asyncContentLoadedState'),(1, 'percentComplete'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseTextEditTextChangedEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.TextEditChangeType,POINTER(win32more.System.Com.SAFEARRAY_head))(('UiaRaiseTextEditTextChangedEvent', windll['UIAutomationCore.dll']), ((1, 'pProvider'),(1, 'textEditChangeType'),(1, 'pChangedData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseChangesEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,Int32,POINTER(win32more.UI.Accessibility.UiaChangeInfo_head))(('UiaRaiseChangesEvent', windll['UIAutomationCore.dll']), ((1, 'pProvider'),(1, 'eventIdCount'),(1, 'pUiaChanges'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseNotificationEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.NotificationKind,win32more.UI.Accessibility.NotificationProcessing,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(('UiaRaiseNotificationEvent', windll['UIAutomationCore.dll']), ((1, 'provider'),(1, 'notificationKind'),(1, 'notificationProcessing'),(1, 'displayString'),(1, 'activityId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseActiveTextPositionChangedEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.ITextRangeProvider_head)(('UiaRaiseActiveTextPositionChangedEvent', windll['UIAutomationCore.dll']), ((1, 'provider'),(1, 'textRange'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaAddEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,Int32,POINTER(win32more.UI.Accessibility.UiaEventCallback),win32more.UI.Accessibility.TreeScope,POINTER(Int32),Int32,POINTER(win32more.UI.Accessibility.UiaCacheRequest_head),POINTER(win32more.UI.Accessibility.HUIAEVENT))(('UiaAddEvent', windll['UIAutomationCore.dll']), ((1, 'hnode'),(1, 'eventId'),(1, 'pCallback'),(1, 'scope'),(1, 'pProperties'),(1, 'cProperties'),(1, 'pRequest'),(1, 'phEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRemoveEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAEVENT)(('UiaRemoveEvent', windll['UIAutomationCore.dll']), ((1, 'hEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaEventAddWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAEVENT,win32more.Foundation.HWND)(('UiaEventAddWindow', windll['UIAutomationCore.dll']), ((1, 'hEvent'),(1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaEventRemoveWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAEVENT,win32more.Foundation.HWND)(('UiaEventRemoveWindow', windll['UIAutomationCore.dll']), ((1, 'hEvent'),(1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DockPattern_SetDockPosition():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.DockPosition)(('DockPattern_SetDockPosition', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'dockPosition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExpandCollapsePattern_Collapse():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT)(('ExpandCollapsePattern_Collapse', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExpandCollapsePattern_Expand():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT)(('ExpandCollapsePattern_Expand', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GridPattern_GetItem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Int32,Int32,POINTER(win32more.UI.Accessibility.HUIANODE))(('GridPattern_GetItem', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'row'),(1, 'column'),(1, 'pResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InvokePattern_Invoke():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT)(('InvokePattern_Invoke', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MultipleViewPattern_GetViewName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Int32,POINTER(win32more.Foundation.BSTR))(('MultipleViewPattern_GetViewName', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'viewId'),(1, 'ppStr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MultipleViewPattern_SetCurrentView():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Int32)(('MultipleViewPattern_SetCurrentView', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'viewId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RangeValuePattern_SetValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Double)(('RangeValuePattern_SetValue', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'val'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScrollItemPattern_ScrollIntoView():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT)(('ScrollItemPattern_ScrollIntoView', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScrollPattern_Scroll():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.ScrollAmount,win32more.UI.Accessibility.ScrollAmount)(('ScrollPattern_Scroll', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'horizontalAmount'),(1, 'verticalAmount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScrollPattern_SetScrollPercent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Double,Double)(('ScrollPattern_SetScrollPercent', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'horizontalPercent'),(1, 'verticalPercent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SelectionItemPattern_AddToSelection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT)(('SelectionItemPattern_AddToSelection', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SelectionItemPattern_RemoveFromSelection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT)(('SelectionItemPattern_RemoveFromSelection', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SelectionItemPattern_Select():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT)(('SelectionItemPattern_Select', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TogglePattern_Toggle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT)(('TogglePattern_Toggle', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TransformPattern_Move():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Double,Double)(('TransformPattern_Move', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TransformPattern_Resize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Double,Double)(('TransformPattern_Resize', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'width'),(1, 'height'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TransformPattern_Rotate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Double)(('TransformPattern_Rotate', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'degrees'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ValuePattern_SetValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.Foundation.PWSTR)(('ValuePattern_SetValue', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'pVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowPattern_Close():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT)(('WindowPattern_Close', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowPattern_SetWindowVisualState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.WindowVisualState)(('WindowPattern_SetWindowVisualState', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'state'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowPattern_WaitForInputIdle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Int32,POINTER(win32more.Foundation.BOOL))(('WindowPattern_WaitForInputIdle', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'milliseconds'),(1, 'pResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextPattern_GetSelection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('TextPattern_GetSelection', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextPattern_GetVisibleRanges():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('TextPattern_GetVisibleRanges', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextPattern_RangeFromChild():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.HUIANODE,POINTER(win32more.UI.Accessibility.HUIATEXTRANGE))(('TextPattern_RangeFromChild', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'hnodeChild'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextPattern_RangeFromPoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.UiaPoint,POINTER(win32more.UI.Accessibility.HUIATEXTRANGE))(('TextPattern_RangeFromPoint', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'point'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextPattern_get_DocumentRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,POINTER(win32more.UI.Accessibility.HUIATEXTRANGE))(('TextPattern_get_DocumentRange', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextPattern_get_SupportedTextSelection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,POINTER(win32more.UI.Accessibility.SupportedTextSelection))(('TextPattern_get_SupportedTextSelection', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_Clone():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,POINTER(win32more.UI.Accessibility.HUIATEXTRANGE))(('TextRange_Clone', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_Compare():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.HUIATEXTRANGE,POINTER(win32more.Foundation.BOOL))(('TextRange_Compare', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'range'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_CompareEndpoints():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextPatternRangeEndpoint,POINTER(Int32))(('TextRange_CompareEndpoints', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'endpoint'),(1, 'targetRange'),(1, 'targetEndpoint'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_ExpandToEnclosingUnit():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextUnit)(('TextRange_ExpandToEnclosingUnit', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'unit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_GetAttributeValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,Int32,POINTER(win32more.System.Com.VARIANT_head))(('TextRange_GetAttributeValue', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'attributeId'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_FindAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,Int32,win32more.System.Com.VARIANT,win32more.Foundation.BOOL,POINTER(win32more.UI.Accessibility.HUIATEXTRANGE))(('TextRange_FindAttribute', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'attributeId'),(1, 'val'),(1, 'backward'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_FindText():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.Foundation.BSTR,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(win32more.UI.Accessibility.HUIATEXTRANGE))(('TextRange_FindText', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'text'),(1, 'backward'),(1, 'ignoreCase'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_GetBoundingRectangles():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('TextRange_GetBoundingRectangles', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_GetEnclosingElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,POINTER(win32more.UI.Accessibility.HUIANODE))(('TextRange_GetEnclosingElement', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_GetText():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,Int32,POINTER(win32more.Foundation.BSTR))(('TextRange_GetText', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'maxLength'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_Move():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextUnit,Int32,POINTER(Int32))(('TextRange_Move', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'unit'),(1, 'count'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_MoveEndpointByUnit():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.TextUnit,Int32,POINTER(Int32))(('TextRange_MoveEndpointByUnit', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'endpoint'),(1, 'unit'),(1, 'count'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_MoveEndpointByRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextPatternRangeEndpoint)(('TextRange_MoveEndpointByRange', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'endpoint'),(1, 'targetRange'),(1, 'targetEndpoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_Select():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE)(('TextRange_Select', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_AddToSelection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE)(('TextRange_AddToSelection', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_RemoveFromSelection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE)(('TextRange_RemoveFromSelection', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_ScrollIntoView():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.Foundation.BOOL)(('TextRange_ScrollIntoView', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'alignToTop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_GetChildren():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(('TextRange_GetChildren', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ItemContainerPattern_FindItemByProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.HUIANODE,Int32,win32more.System.Com.VARIANT,POINTER(win32more.UI.Accessibility.HUIANODE))(('ItemContainerPattern_FindItemByProperty', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'hnodeStartAfter'),(1, 'propertyId'),(1, 'value'),(1, 'pFound'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LegacyIAccessiblePattern_Select():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Int32)(('LegacyIAccessiblePattern_Select', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'flagsSelect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LegacyIAccessiblePattern_DoDefaultAction():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT)(('LegacyIAccessiblePattern_DoDefaultAction', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LegacyIAccessiblePattern_SetValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.Foundation.PWSTR)(('LegacyIAccessiblePattern_SetValue', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'szValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LegacyIAccessiblePattern_GetIAccessible():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,POINTER(win32more.UI.Accessibility.IAccessible_head))(('LegacyIAccessiblePattern_GetIAccessible', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'pAccessible'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SynchronizedInputPattern_StartListening():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.SynchronizedInputType)(('SynchronizedInputPattern_StartListening', windll['UIAutomationCore.dll']), ((1, 'hobj'),(1, 'inputType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SynchronizedInputPattern_Cancel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT)(('SynchronizedInputPattern_Cancel', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualizedItemPattern_Realize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT)(('VirtualizedItemPattern_Realize', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaPatternRelease():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Accessibility.HUIAPATTERNOBJECT)(('UiaPatternRelease', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaTextRangeRelease():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Accessibility.HUIATEXTRANGE)(('UiaTextRangeRelease', windll['UIAutomationCore.dll']), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaReturnRawElementProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.LRESULT,win32more.Foundation.HWND,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,win32more.UI.Accessibility.IRawElementProviderSimple_head)(('UiaReturnRawElementProvider', windll['UIAutomationCore.dll']), ((1, 'hwnd'),(1, 'wParam'),(1, 'lParam'),(1, 'el'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaHostProviderFromHwnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(('UiaHostProviderFromHwnd', windll['UIAutomationCore.dll']), ((1, 'hwnd'),(1, 'ppProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaProviderForNonClient():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,Int32,Int32,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(('UiaProviderForNonClient', windll['UIAutomationCore.dll']), ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'ppProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaIAccessibleFromProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,UInt32,POINTER(win32more.UI.Accessibility.IAccessible_head),POINTER(win32more.System.Com.VARIANT_head))(('UiaIAccessibleFromProvider', windll['UIAutomationCore.dll']), ((1, 'pProvider'),(1, 'dwFlags'),(1, 'ppAccessible'),(1, 'pvarChild'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaProviderFromIAccessible():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessible_head,Int32,UInt32,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(('UiaProviderFromIAccessible', windll['UIAutomationCore.dll']), ((1, 'pAccessible'),(1, 'idChild'),(1, 'dwFlags'),(1, 'ppProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaDisconnectAllProviders():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('UiaDisconnectAllProviders', windll['UIAutomationCore.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaDisconnectProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head)(('UiaDisconnectProvider', windll['UIAutomationCore.dll']), ((1, 'pProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaHasServerSideProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND)(('UiaHasServerSideProvider', windll['UIAutomationCore.dll']), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterPointerInputTarget():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE)(('RegisterPointerInputTarget', windll['USER32.dll']), ((1, 'hwnd'),(1, 'pointerType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterPointerInputTarget():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE)(('UnregisterPointerInputTarget', windll['USER32.dll']), ((1, 'hwnd'),(1, 'pointerType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterPointerInputTargetEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE,win32more.Foundation.BOOL)(('RegisterPointerInputTargetEx', windll['USER32.dll']), ((1, 'hwnd'),(1, 'pointerType'),(1, 'fObserve'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterPointerInputTargetEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE)(('UnregisterPointerInputTargetEx', windll['USER32.dll']), ((1, 'hwnd'),(1, 'pointerType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyWinEvent():
    try:
        return WINFUNCTYPE(Void,UInt32,win32more.Foundation.HWND,Int32,Int32)(('NotifyWinEvent', windll['USER32.dll']), ((1, 'event'),(1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetWinEventHook():
    try:
        return WINFUNCTYPE(win32more.UI.Accessibility.HWINEVENTHOOK,UInt32,UInt32,win32more.Foundation.HINSTANCE,win32more.UI.Accessibility.WINEVENTPROC,UInt32,UInt32,UInt32)(('SetWinEventHook', windll['USER32.dll']), ((1, 'eventMin'),(1, 'eventMax'),(1, 'hmodWinEventProc'),(1, 'pfnWinEventProc'),(1, 'idProcess'),(1, 'idThread'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsWinEventHookInstalled():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32)(('IsWinEventHookInstalled', windll['USER32.dll']), ((1, 'event'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnhookWinEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Accessibility.HWINEVENTHOOK)(('UnhookWinEvent', windll['USER32.dll']), ((1, 'hWinEventHook'),))
    except (FileNotFoundError, AttributeError):
        return None
AsyncContentLoadedState = Int32
AsyncContentLoadedState_Beginning = 0
AsyncContentLoadedState_Progress = 1
AsyncContentLoadedState_Completed = 2
AutomationElementMode = Int32
AutomationElementMode_None = 0
AutomationElementMode_Full = 1
AutomationIdentifierType = Int32
AutomationIdentifierType_Property = 0
AutomationIdentifierType_Pattern = 1
AutomationIdentifierType_Event = 2
AutomationIdentifierType_ControlType = 3
AutomationIdentifierType_TextAttribute = 4
AutomationIdentifierType_LandmarkType = 5
AutomationIdentifierType_Annotation = 6
AutomationIdentifierType_Changes = 7
AutomationIdentifierType_Style = 8
BulletStyle = Int32
BulletStyle_None = 0
BulletStyle_HollowRoundBullet = 1
BulletStyle_FilledRoundBullet = 2
BulletStyle_HollowSquareBullet = 3
BulletStyle_FilledSquareBullet = 4
BulletStyle_DashBullet = 5
BulletStyle_Other = -1
CAccPropServices = Guid('b5f8350b-0548-48b1-a6-ee-88-bd-00-b4-a5-e7')
CapStyle = Int32
CapStyle_None = 0
CapStyle_SmallCap = 1
CapStyle_AllCap = 2
CapStyle_AllPetiteCaps = 3
CapStyle_PetiteCaps = 4
CapStyle_Unicase = 5
CapStyle_Titling = 6
CapStyle_Other = -1
CaretBidiMode = Int32
CaretBidiMode_LTR = 0
CaretBidiMode_RTL = 1
CaretPosition = Int32
CaretPosition_Unknown = 0
CaretPosition_EndOfLine = 1
CaretPosition_BeginningOfLine = 2
CoalesceEventsOptions = Int32
CoalesceEventsOptions_Disabled = 0
CoalesceEventsOptions_Enabled = 1
ConditionType = Int32
ConditionType_True = 0
ConditionType_False = 1
ConditionType_Property = 2
ConditionType_And = 3
ConditionType_Or = 4
ConditionType_Not = 5
ConnectionRecoveryBehaviorOptions = Int32
ConnectionRecoveryBehaviorOptions_Disabled = 0
ConnectionRecoveryBehaviorOptions_Enabled = 1
CUIAutomation = Guid('ff48dba4-60ef-4201-aa-87-54-10-3e-ef-59-4e')
CUIAutomation8 = Guid('e22ad333-b25f-460c-83-d0-05-81-10-73-95-c9')
CUIAutomationRegistrar = Guid('6e29fabf-9977-42d1-8d-0e-ca-7e-61-ad-87-e6')
DockPosition = Int32
DockPosition_Top = 0
DockPosition_Left = 1
DockPosition_Bottom = 2
DockPosition_Right = 3
DockPosition_Fill = 4
DockPosition_None = 5
EventArgsType = Int32
EventArgsType_Simple = 0
EventArgsType_PropertyChanged = 1
EventArgsType_StructureChanged = 2
EventArgsType_AsyncContentLoaded = 3
EventArgsType_WindowClosed = 4
EventArgsType_TextEditTextChanged = 5
EventArgsType_Changes = 6
EventArgsType_Notification = 7
EventArgsType_ActiveTextPositionChanged = 8
EventArgsType_StructuredMarkup = 9
ExpandCollapseState = Int32
ExpandCollapseState_Collapsed = 0
ExpandCollapseState_Expanded = 1
ExpandCollapseState_PartiallyExpanded = 2
ExpandCollapseState_LeafNode = 3
def _define_ExtendedProperty_head():
    class ExtendedProperty(Structure):
        pass
    return ExtendedProperty
def _define_ExtendedProperty():
    ExtendedProperty = win32more.UI.Accessibility.ExtendedProperty_head
    ExtendedProperty._fields_ = [
        ('PropertyName', win32more.Foundation.BSTR),
        ('PropertyValue', win32more.Foundation.BSTR),
    ]
    return ExtendedProperty
FillType = Int32
FillType_None = 0
FillType_Color = 1
FillType_Gradient = 2
FillType_Picture = 3
FillType_Pattern = 4
def _define_FILTERKEYS_head():
    class FILTERKEYS(Structure):
        pass
    return FILTERKEYS
def _define_FILTERKEYS():
    FILTERKEYS = win32more.UI.Accessibility.FILTERKEYS_head
    FILTERKEYS._fields_ = [
        ('cbSize', UInt32),
        ('dwFlags', UInt32),
        ('iWaitMSec', UInt32),
        ('iDelayMSec', UInt32),
        ('iRepeatMSec', UInt32),
        ('iBounceMSec', UInt32),
    ]
    return FILTERKEYS
FlowDirections = Int32
FlowDirections_Default = 0
FlowDirections_RightToLeft = 1
FlowDirections_BottomToTop = 2
FlowDirections_Vertical = 4
def _define_HIGHCONTRASTA_head():
    class HIGHCONTRASTA(Structure):
        pass
    return HIGHCONTRASTA
def _define_HIGHCONTRASTA():
    HIGHCONTRASTA = win32more.UI.Accessibility.HIGHCONTRASTA_head
    HIGHCONTRASTA._fields_ = [
        ('cbSize', UInt32),
        ('dwFlags', win32more.UI.Accessibility.HIGHCONTRASTW_FLAGS),
        ('lpszDefaultScheme', win32more.Foundation.PSTR),
    ]
    return HIGHCONTRASTA
def _define_HIGHCONTRASTW_head():
    class HIGHCONTRASTW(Structure):
        pass
    return HIGHCONTRASTW
def _define_HIGHCONTRASTW():
    HIGHCONTRASTW = win32more.UI.Accessibility.HIGHCONTRASTW_head
    HIGHCONTRASTW._fields_ = [
        ('cbSize', UInt32),
        ('dwFlags', win32more.UI.Accessibility.HIGHCONTRASTW_FLAGS),
        ('lpszDefaultScheme', win32more.Foundation.PWSTR),
    ]
    return HIGHCONTRASTW
HIGHCONTRASTW_FLAGS = UInt32
HCF_HIGHCONTRASTON = 1
HCF_AVAILABLE = 2
HCF_HOTKEYACTIVE = 4
HCF_CONFIRMHOTKEY = 8
HCF_HOTKEYSOUND = 16
HCF_INDICATOR = 32
HCF_HOTKEYAVAILABLE = 64
HCF_OPTION_NOTHEMECHANGE = 4096
HorizontalTextAlignment = Int32
HorizontalTextAlignment_Left = 0
HorizontalTextAlignment_Centered = 1
HorizontalTextAlignment_Right = 2
HorizontalTextAlignment_Justified = 3
HUIAEVENT = IntPtr
HUIANODE = IntPtr
HUIAPATTERNOBJECT = IntPtr
HUIATEXTRANGE = IntPtr
HWINEVENTHOOK = IntPtr
def _define_IAccessible_head():
    class IAccessible(win32more.System.Com.IDispatch_head):
        Guid = Guid('618736e0-3c3d-11cf-81-0c-00-aa-00-38-9b-71')
    return IAccessible
def _define_IAccessible():
    IAccessible = win32more.UI.Accessibility.IAccessible_head
    IAccessible.get_accParent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head))(7, 'get_accParent', ((1, 'ppdispParent'),)))
    IAccessible.get_accChildCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_accChildCount', ((1, 'pcountChildren'),)))
    IAccessible.get_accChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.IDispatch_head))(9, 'get_accChild', ((1, 'varChild'),(1, 'ppdispChild'),)))
    IAccessible.get_accName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR))(10, 'get_accName', ((1, 'varChild'),(1, 'pszName'),)))
    IAccessible.get_accValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR))(11, 'get_accValue', ((1, 'varChild'),(1, 'pszValue'),)))
    IAccessible.get_accDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR))(12, 'get_accDescription', ((1, 'varChild'),(1, 'pszDescription'),)))
    IAccessible.get_accRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head))(13, 'get_accRole', ((1, 'varChild'),(1, 'pvarRole'),)))
    IAccessible.get_accState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head))(14, 'get_accState', ((1, 'varChild'),(1, 'pvarState'),)))
    IAccessible.get_accHelp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR))(15, 'get_accHelp', ((1, 'varChild'),(1, 'pszHelp'),)))
    IAccessible.get_accHelpTopic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR),win32more.System.Com.VARIANT,POINTER(Int32))(16, 'get_accHelpTopic', ((1, 'pszHelpFile'),(1, 'varChild'),(1, 'pidTopic'),)))
    IAccessible.get_accKeyboardShortcut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR))(17, 'get_accKeyboardShortcut', ((1, 'varChild'),(1, 'pszKeyboardShortcut'),)))
    IAccessible.get_accFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(18, 'get_accFocus', ((1, 'pvarChild'),)))
    IAccessible.get_accSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(19, 'get_accSelection', ((1, 'pvarChildren'),)))
    IAccessible.get_accDefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR))(20, 'get_accDefaultAction', ((1, 'varChild'),(1, 'pszDefaultAction'),)))
    IAccessible.accSelect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT)(21, 'accSelect', ((1, 'flagsSelect'),(1, 'varChild'),)))
    IAccessible.accLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32),win32more.System.Com.VARIANT)(22, 'accLocation', ((1, 'pxLeft'),(1, 'pyTop'),(1, 'pcxWidth'),(1, 'pcyHeight'),(1, 'varChild'),)))
    IAccessible.accNavigate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head))(23, 'accNavigate', ((1, 'navDir'),(1, 'varStart'),(1, 'pvarEndUpAt'),)))
    IAccessible.accHitTest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head))(24, 'accHitTest', ((1, 'xLeft'),(1, 'yTop'),(1, 'pvarChild'),)))
    IAccessible.accDoDefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(25, 'accDoDefaultAction', ((1, 'varChild'),)))
    IAccessible.put_accName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,win32more.Foundation.BSTR)(26, 'put_accName', ((1, 'varChild'),(1, 'szName'),)))
    IAccessible.put_accValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,win32more.Foundation.BSTR)(27, 'put_accValue', ((1, 'varChild'),(1, 'szValue'),)))
    win32more.System.Com.IDispatch
    return IAccessible
def _define_IAccessibleEx_head():
    class IAccessibleEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('f8b80ada-2c44-48d0-89-be-5f-f2-3c-9c-d8-75')
    return IAccessibleEx
def _define_IAccessibleEx():
    IAccessibleEx = win32more.UI.Accessibility.IAccessibleEx_head
    IAccessibleEx.GetObjectForChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.Accessibility.IAccessibleEx_head))(3, 'GetObjectForChild', ((1, 'idChild'),(1, 'pRetVal'),)))
    IAccessibleEx.GetIAccessiblePair = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IAccessible_head),POINTER(Int32))(4, 'GetIAccessiblePair', ((1, 'ppAcc'),(1, 'pidChild'),)))
    IAccessibleEx.GetRuntimeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(5, 'GetRuntimeId', ((1, 'pRetVal'),)))
    IAccessibleEx.ConvertReturnedElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,POINTER(win32more.UI.Accessibility.IAccessibleEx_head))(6, 'ConvertReturnedElement', ((1, 'pIn'),(1, 'ppRetValOut'),)))
    win32more.System.Com.IUnknown
    return IAccessibleEx
def _define_IAccessibleHandler_head():
    class IAccessibleHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('03022430-abc4-11d0-bd-e2-00-aa-00-1a-19-53')
    return IAccessibleHandler
def _define_IAccessibleHandler():
    IAccessibleHandler = win32more.UI.Accessibility.IAccessibleHandler_head
    IAccessibleHandler.AccessibleObjectFromID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.Accessibility.IAccessible_head))(3, 'AccessibleObjectFromID', ((1, 'hwnd'),(1, 'lObjectID'),(1, 'pIAccessible'),)))
    win32more.System.Com.IUnknown
    return IAccessibleHandler
def _define_IAccessibleHostingElementProviders_head():
    class IAccessibleHostingElementProviders(win32more.System.Com.IUnknown_head):
        Guid = Guid('33ac331b-943e-4020-b2-95-db-37-78-49-74-a3')
    return IAccessibleHostingElementProviders
def _define_IAccessibleHostingElementProviders():
    IAccessibleHostingElementProviders = win32more.UI.Accessibility.IAccessibleHostingElementProviders_head
    IAccessibleHostingElementProviders.GetEmbeddedFragmentRoots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(3, 'GetEmbeddedFragmentRoots', ((1, 'pRetVal'),)))
    IAccessibleHostingElementProviders.GetObjectIdForProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,POINTER(Int32))(4, 'GetObjectIdForProvider', ((1, 'pProvider'),(1, 'pidObject'),)))
    win32more.System.Com.IUnknown
    return IAccessibleHostingElementProviders
def _define_IAccessibleWindowlessSite_head():
    class IAccessibleWindowlessSite(win32more.System.Com.IUnknown_head):
        Guid = Guid('bf3abd9c-76da-4389-9e-b6-14-27-d2-5a-ba-b7')
    return IAccessibleWindowlessSite
def _define_IAccessibleWindowlessSite():
    IAccessibleWindowlessSite = win32more.UI.Accessibility.IAccessibleWindowlessSite_head
    IAccessibleWindowlessSite.AcquireObjectIdRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.UI.Accessibility.IAccessibleHandler_head,POINTER(Int32))(3, 'AcquireObjectIdRange', ((1, 'rangeSize'),(1, 'pRangeOwner'),(1, 'pRangeBase'),)))
    IAccessibleWindowlessSite.ReleaseObjectIdRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.UI.Accessibility.IAccessibleHandler_head)(4, 'ReleaseObjectIdRange', ((1, 'rangeBase'),(1, 'pRangeOwner'),)))
    IAccessibleWindowlessSite.QueryObjectIdRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessibleHandler_head,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(5, 'QueryObjectIdRanges', ((1, 'pRangesOwner'),(1, 'psaRanges'),)))
    IAccessibleWindowlessSite.GetParentAccessible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IAccessible_head))(6, 'GetParentAccessible', ((1, 'ppParent'),)))
    win32more.System.Com.IUnknown
    return IAccessibleWindowlessSite
def _define_IAccIdentity_head():
    class IAccIdentity(win32more.System.Com.IUnknown_head):
        Guid = Guid('7852b78d-1cfd-41c1-a6-15-9c-0c-85-96-0b-5f')
    return IAccIdentity
def _define_IAccIdentity():
    IAccIdentity = win32more.UI.Accessibility.IAccIdentity_head
    IAccIdentity.GetIdentityString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(c_char_p_no),POINTER(UInt32))(3, 'GetIdentityString', ((1, 'dwIDChild'),(1, 'ppIDString'),(1, 'pdwIDStringLen'),)))
    win32more.System.Com.IUnknown
    return IAccIdentity
def _define_IAccPropServer_head():
    class IAccPropServer(win32more.System.Com.IUnknown_head):
        Guid = Guid('76c0dbbb-15e0-4e7b-b6-1b-20-ee-ea-20-01-e0')
    return IAccPropServer
def _define_IAccPropServer():
    IAccPropServer = win32more.UI.Accessibility.IAccPropServer_head
    IAccPropServer.GetPropValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,Guid,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.BOOL))(3, 'GetPropValue', ((1, 'pIDString'),(1, 'dwIDStringLen'),(1, 'idProp'),(1, 'pvarValue'),(1, 'pfHasProp'),)))
    win32more.System.Com.IUnknown
    return IAccPropServer
def _define_IAccPropServices_head():
    class IAccPropServices(win32more.System.Com.IUnknown_head):
        Guid = Guid('6e26e776-04f0-495d-80-e4-33-30-35-2e-31-69')
    return IAccPropServices
def _define_IAccPropServices():
    IAccPropServices = win32more.UI.Accessibility.IAccPropServices_head
    IAccPropServices.SetPropValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,Guid,win32more.System.Com.VARIANT)(3, 'SetPropValue', ((1, 'pIDString'),(1, 'dwIDStringLen'),(1, 'idProp'),(1, 'var'),)))
    IAccPropServices.SetPropServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(Guid),Int32,win32more.UI.Accessibility.IAccPropServer_head,win32more.UI.Accessibility.AnnoScope)(4, 'SetPropServer', ((1, 'pIDString'),(1, 'dwIDStringLen'),(1, 'paProps'),(1, 'cProps'),(1, 'pServer'),(1, 'annoScope'),)))
    IAccPropServices.ClearProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(Guid),Int32)(5, 'ClearProps', ((1, 'pIDString'),(1, 'dwIDStringLen'),(1, 'paProps'),(1, 'cProps'),)))
    IAccPropServices.SetHwndProp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,UInt32,Guid,win32more.System.Com.VARIANT)(6, 'SetHwndProp', ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'idProp'),(1, 'var'),)))
    IAccPropServices.SetHwndPropStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,UInt32,Guid,win32more.Foundation.PWSTR)(7, 'SetHwndPropStr', ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'idProp'),(1, 'str'),)))
    IAccPropServices.SetHwndPropServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,UInt32,POINTER(Guid),Int32,win32more.UI.Accessibility.IAccPropServer_head,win32more.UI.Accessibility.AnnoScope)(8, 'SetHwndPropServer', ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'paProps'),(1, 'cProps'),(1, 'pServer'),(1, 'annoScope'),)))
    IAccPropServices.ClearHwndProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,UInt32,POINTER(Guid),Int32)(9, 'ClearHwndProps', ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'paProps'),(1, 'cProps'),)))
    IAccPropServices.ComposeHwndIdentityString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,UInt32,POINTER(c_char_p_no),POINTER(UInt32))(10, 'ComposeHwndIdentityString', ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'ppIDString'),(1, 'pdwIDStringLen'),)))
    IAccPropServices.DecomposeHwndIdentityString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(win32more.Foundation.HWND),POINTER(UInt32),POINTER(UInt32))(11, 'DecomposeHwndIdentityString', ((1, 'pIDString'),(1, 'dwIDStringLen'),(1, 'phwnd'),(1, 'pidObject'),(1, 'pidChild'),)))
    IAccPropServices.SetHmenuProp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HMENU,UInt32,Guid,win32more.System.Com.VARIANT)(12, 'SetHmenuProp', ((1, 'hmenu'),(1, 'idChild'),(1, 'idProp'),(1, 'var'),)))
    IAccPropServices.SetHmenuPropStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HMENU,UInt32,Guid,win32more.Foundation.PWSTR)(13, 'SetHmenuPropStr', ((1, 'hmenu'),(1, 'idChild'),(1, 'idProp'),(1, 'str'),)))
    IAccPropServices.SetHmenuPropServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HMENU,UInt32,POINTER(Guid),Int32,win32more.UI.Accessibility.IAccPropServer_head,win32more.UI.Accessibility.AnnoScope)(14, 'SetHmenuPropServer', ((1, 'hmenu'),(1, 'idChild'),(1, 'paProps'),(1, 'cProps'),(1, 'pServer'),(1, 'annoScope'),)))
    IAccPropServices.ClearHmenuProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HMENU,UInt32,POINTER(Guid),Int32)(15, 'ClearHmenuProps', ((1, 'hmenu'),(1, 'idChild'),(1, 'paProps'),(1, 'cProps'),)))
    IAccPropServices.ComposeHmenuIdentityString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HMENU,UInt32,POINTER(c_char_p_no),POINTER(UInt32))(16, 'ComposeHmenuIdentityString', ((1, 'hmenu'),(1, 'idChild'),(1, 'ppIDString'),(1, 'pdwIDStringLen'),)))
    IAccPropServices.DecomposeHmenuIdentityString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(win32more.UI.WindowsAndMessaging.HMENU),POINTER(UInt32))(17, 'DecomposeHmenuIdentityString', ((1, 'pIDString'),(1, 'dwIDStringLen'),(1, 'phmenu'),(1, 'pidChild'),)))
    win32more.System.Com.IUnknown
    return IAccPropServices
def _define_IAnnotationProvider_head():
    class IAnnotationProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('f95c7e80-bd63-4601-97-82-44-5e-bf-f0-11-fc')
    return IAnnotationProvider
def _define_IAnnotationProvider():
    IAnnotationProvider = win32more.UI.Accessibility.IAnnotationProvider_head
    IAnnotationProvider.get_AnnotationTypeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_ANNOTATIONTYPE))(3, 'get_AnnotationTypeId', ((1, 'retVal'),)))
    IAnnotationProvider.get_AnnotationTypeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'get_AnnotationTypeName', ((1, 'retVal'),)))
    IAnnotationProvider.get_Author = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(5, 'get_Author', ((1, 'retVal'),)))
    IAnnotationProvider.get_DateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(6, 'get_DateTime', ((1, 'retVal'),)))
    IAnnotationProvider.get_Target = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(7, 'get_Target', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IAnnotationProvider
def _define_ICustomNavigationProvider_head():
    class ICustomNavigationProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('2062a28a-8c07-4b94-8e-12-70-37-c6-22-ae-b8')
    return ICustomNavigationProvider
def _define_ICustomNavigationProvider():
    ICustomNavigationProvider = win32more.UI.Accessibility.ICustomNavigationProvider_head
    ICustomNavigationProvider.Navigate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.NavigateDirection,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(3, 'Navigate', ((1, 'direction'),(1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ICustomNavigationProvider
def _define_IDockProvider_head():
    class IDockProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('159bc72c-4ad3-485e-96-37-d7-05-2e-df-01-46')
    return IDockProvider
def _define_IDockProvider():
    IDockProvider = win32more.UI.Accessibility.IDockProvider_head
    IDockProvider.SetDockPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.DockPosition)(3, 'SetDockPosition', ((1, 'dockPosition'),)))
    IDockProvider.get_DockPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.DockPosition))(4, 'get_DockPosition', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IDockProvider
def _define_IDragProvider_head():
    class IDragProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('6aa7bbbb-7ff9-497d-90-4f-d2-0b-89-79-29-d8')
    return IDragProvider
def _define_IDragProvider():
    IDragProvider = win32more.UI.Accessibility.IDragProvider_head
    IDragProvider.get_IsGrabbed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'get_IsGrabbed', ((1, 'pRetVal'),)))
    IDragProvider.get_DropEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'get_DropEffect', ((1, 'pRetVal'),)))
    IDragProvider.get_DropEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(5, 'get_DropEffects', ((1, 'pRetVal'),)))
    IDragProvider.GetGrabbedItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(6, 'GetGrabbedItems', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IDragProvider
def _define_IDropTargetProvider_head():
    class IDropTargetProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('bae82bfd-358a-481c-85-a0-d8-b4-d9-0a-5d-61')
    return IDropTargetProvider
def _define_IDropTargetProvider():
    IDropTargetProvider = win32more.UI.Accessibility.IDropTargetProvider_head
    IDropTargetProvider.get_DropTargetEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(3, 'get_DropTargetEffect', ((1, 'pRetVal'),)))
    IDropTargetProvider.get_DropTargetEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(4, 'get_DropTargetEffects', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IDropTargetProvider
def _define_IExpandCollapseProvider_head():
    class IExpandCollapseProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('d847d3a5-cab0-4a98-8c-32-ec-b4-5c-59-ad-24')
    return IExpandCollapseProvider
def _define_IExpandCollapseProvider():
    IExpandCollapseProvider = win32more.UI.Accessibility.IExpandCollapseProvider_head
    IExpandCollapseProvider.Expand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Expand', ()))
    IExpandCollapseProvider.Collapse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Collapse', ()))
    IExpandCollapseProvider.get_ExpandCollapseState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ExpandCollapseState))(5, 'get_ExpandCollapseState', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IExpandCollapseProvider
def _define_IGridItemProvider_head():
    class IGridItemProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('d02541f1-fb81-4d64-ae-32-f5-20-f8-a6-db-d1')
    return IGridItemProvider
def _define_IGridItemProvider():
    IGridItemProvider = win32more.UI.Accessibility.IGridItemProvider_head
    IGridItemProvider.get_Row = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(3, 'get_Row', ((1, 'pRetVal'),)))
    IGridItemProvider.get_Column = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(4, 'get_Column', ((1, 'pRetVal'),)))
    IGridItemProvider.get_RowSpan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(5, 'get_RowSpan', ((1, 'pRetVal'),)))
    IGridItemProvider.get_ColumnSpan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(6, 'get_ColumnSpan', ((1, 'pRetVal'),)))
    IGridItemProvider.get_ContainingGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(7, 'get_ContainingGrid', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IGridItemProvider
def _define_IGridProvider_head():
    class IGridProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('b17d6187-0907-464b-a1-68-0e-f1-7a-15-72-b1')
    return IGridProvider
def _define_IGridProvider():
    IGridProvider = win32more.UI.Accessibility.IGridProvider_head
    IGridProvider.GetItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(3, 'GetItem', ((1, 'row'),(1, 'column'),(1, 'pRetVal'),)))
    IGridProvider.get_RowCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(4, 'get_RowCount', ((1, 'pRetVal'),)))
    IGridProvider.get_ColumnCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(5, 'get_ColumnCount', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IGridProvider
def _define_IInvokeProvider_head():
    class IInvokeProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('54fcb24b-e18e-47a2-b4-d3-ec-cb-e7-75-99-a2')
    return IInvokeProvider
def _define_IInvokeProvider():
    IInvokeProvider = win32more.UI.Accessibility.IInvokeProvider_head
    IInvokeProvider.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Invoke', ()))
    win32more.System.Com.IUnknown
    return IInvokeProvider
def _define_IItemContainerProvider_head():
    class IItemContainerProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('e747770b-39ce-4382-ab-30-d8-fb-3f-33-6f-24')
    return IItemContainerProvider
def _define_IItemContainerProvider():
    IItemContainerProvider = win32more.UI.Accessibility.IItemContainerProvider_head
    IItemContainerProvider.FindItemByProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.UIA_PROPERTY_ID,win32more.System.Com.VARIANT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(3, 'FindItemByProperty', ((1, 'pStartAfter'),(1, 'propertyId'),(1, 'value'),(1, 'pFound'),)))
    win32more.System.Com.IUnknown
    return IItemContainerProvider
def _define_ILegacyIAccessibleProvider_head():
    class ILegacyIAccessibleProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('e44c3566-915d-4070-99-c6-04-7b-ff-5a-08-f5')
    return ILegacyIAccessibleProvider
def _define_ILegacyIAccessibleProvider():
    ILegacyIAccessibleProvider = win32more.UI.Accessibility.ILegacyIAccessibleProvider_head
    ILegacyIAccessibleProvider.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(3, 'Select', ((1, 'flagsSelect'),)))
    ILegacyIAccessibleProvider.DoDefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'DoDefaultAction', ()))
    ILegacyIAccessibleProvider.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(5, 'SetValue', ((1, 'szValue'),)))
    ILegacyIAccessibleProvider.GetIAccessible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IAccessible_head))(6, 'GetIAccessible', ((1, 'ppAccessible'),)))
    ILegacyIAccessibleProvider.get_ChildId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_ChildId', ((1, 'pRetVal'),)))
    ILegacyIAccessibleProvider.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Name', ((1, 'pszName'),)))
    ILegacyIAccessibleProvider.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_Value', ((1, 'pszValue'),)))
    ILegacyIAccessibleProvider.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_Description', ((1, 'pszDescription'),)))
    ILegacyIAccessibleProvider.get_Role = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(11, 'get_Role', ((1, 'pdwRole'),)))
    ILegacyIAccessibleProvider.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'get_State', ((1, 'pdwState'),)))
    ILegacyIAccessibleProvider.get_Help = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_Help', ((1, 'pszHelp'),)))
    ILegacyIAccessibleProvider.get_KeyboardShortcut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_KeyboardShortcut', ((1, 'pszKeyboardShortcut'),)))
    ILegacyIAccessibleProvider.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(15, 'GetSelection', ((1, 'pvarSelectedChildren'),)))
    ILegacyIAccessibleProvider.get_DefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(16, 'get_DefaultAction', ((1, 'pszDefaultAction'),)))
    win32more.System.Com.IUnknown
    return ILegacyIAccessibleProvider
def _define_IMultipleViewProvider_head():
    class IMultipleViewProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('6278cab1-b556-4a1a-b4-e0-41-8a-cc-52-32-01')
    return IMultipleViewProvider
def _define_IMultipleViewProvider():
    IMultipleViewProvider = win32more.UI.Accessibility.IMultipleViewProvider_head
    IMultipleViewProvider.GetViewName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR))(3, 'GetViewName', ((1, 'viewId'),(1, 'pRetVal'),)))
    IMultipleViewProvider.SetCurrentView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(4, 'SetCurrentView', ((1, 'viewId'),)))
    IMultipleViewProvider.get_CurrentView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(5, 'get_CurrentView', ((1, 'pRetVal'),)))
    IMultipleViewProvider.GetSupportedViews = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(6, 'GetSupportedViews', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IMultipleViewProvider
def _define_IObjectModelProvider_head():
    class IObjectModelProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('3ad86ebd-f5ef-483d-bb-18-b1-04-2a-47-5d-64')
    return IObjectModelProvider
def _define_IObjectModelProvider():
    IObjectModelProvider = win32more.UI.Accessibility.IObjectModelProvider_head
    IObjectModelProvider.GetUnderlyingObjectModel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(3, 'GetUnderlyingObjectModel', ((1, 'ppUnknown'),)))
    win32more.System.Com.IUnknown
    return IObjectModelProvider
def _define_IProxyProviderWinEventHandler_head():
    class IProxyProviderWinEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('89592ad4-f4e0-43d5-a3-b6-ba-d7-e1-11-b4-35')
    return IProxyProviderWinEventHandler
def _define_IProxyProviderWinEventHandler():
    IProxyProviderWinEventHandler = win32more.UI.Accessibility.IProxyProviderWinEventHandler_head
    IProxyProviderWinEventHandler.RespondToWinEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.HWND,Int32,Int32,win32more.UI.Accessibility.IProxyProviderWinEventSink_head)(3, 'RespondToWinEvent', ((1, 'idWinEvent'),(1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'pSink'),)))
    win32more.System.Com.IUnknown
    return IProxyProviderWinEventHandler
def _define_IProxyProviderWinEventSink_head():
    class IProxyProviderWinEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('4fd82b78-a43e-46ac-98-03-0a-69-69-c7-c1-83')
    return IProxyProviderWinEventSink
def _define_IProxyProviderWinEventSink():
    IProxyProviderWinEventSink = win32more.UI.Accessibility.IProxyProviderWinEventSink_head
    IProxyProviderWinEventSink.AddAutomationPropertyChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.UIA_PROPERTY_ID,win32more.System.Com.VARIANT)(3, 'AddAutomationPropertyChangedEvent', ((1, 'pProvider'),(1, 'id'),(1, 'newValue'),)))
    IProxyProviderWinEventSink.AddAutomationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.UIA_EVENT_ID)(4, 'AddAutomationEvent', ((1, 'pProvider'),(1, 'id'),)))
    IProxyProviderWinEventSink.AddStructureChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.StructureChangeType,POINTER(win32more.System.Com.SAFEARRAY_head))(5, 'AddStructureChangedEvent', ((1, 'pProvider'),(1, 'structureChangeType'),(1, 'runtimeId'),)))
    win32more.System.Com.IUnknown
    return IProxyProviderWinEventSink
def _define_IRangeValueProvider_head():
    class IRangeValueProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('36dc7aef-33e6-4691-af-e1-2b-e7-27-4b-3d-33')
    return IRangeValueProvider
def _define_IRangeValueProvider():
    IRangeValueProvider = win32more.UI.Accessibility.IRangeValueProvider_head
    IRangeValueProvider.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(3, 'SetValue', ((1, 'val'),)))
    IRangeValueProvider.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(4, 'get_Value', ((1, 'pRetVal'),)))
    IRangeValueProvider.get_IsReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(5, 'get_IsReadOnly', ((1, 'pRetVal'),)))
    IRangeValueProvider.get_Maximum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(6, 'get_Maximum', ((1, 'pRetVal'),)))
    IRangeValueProvider.get_Minimum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(7, 'get_Minimum', ((1, 'pRetVal'),)))
    IRangeValueProvider.get_LargeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(8, 'get_LargeChange', ((1, 'pRetVal'),)))
    IRangeValueProvider.get_SmallChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(9, 'get_SmallChange', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRangeValueProvider
def _define_IRawElementProviderAdviseEvents_head():
    class IRawElementProviderAdviseEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('a407b27b-0f6d-4427-92-92-47-3c-7b-f9-32-58')
    return IRawElementProviderAdviseEvents
def _define_IRawElementProviderAdviseEvents():
    IRawElementProviderAdviseEvents = win32more.UI.Accessibility.IRawElementProviderAdviseEvents_head
    IRawElementProviderAdviseEvents.AdviseEventAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_EVENT_ID,POINTER(win32more.System.Com.SAFEARRAY_head))(3, 'AdviseEventAdded', ((1, 'eventId'),(1, 'propertyIDs'),)))
    IRawElementProviderAdviseEvents.AdviseEventRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_EVENT_ID,POINTER(win32more.System.Com.SAFEARRAY_head))(4, 'AdviseEventRemoved', ((1, 'eventId'),(1, 'propertyIDs'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderAdviseEvents
def _define_IRawElementProviderFragment_head():
    class IRawElementProviderFragment(win32more.System.Com.IUnknown_head):
        Guid = Guid('f7063da8-8359-439c-92-97-bb-c5-29-9a-7d-87')
    return IRawElementProviderFragment
def _define_IRawElementProviderFragment():
    IRawElementProviderFragment = win32more.UI.Accessibility.IRawElementProviderFragment_head
    IRawElementProviderFragment.Navigate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.NavigateDirection,POINTER(win32more.UI.Accessibility.IRawElementProviderFragment_head))(3, 'Navigate', ((1, 'direction'),(1, 'pRetVal'),)))
    IRawElementProviderFragment.GetRuntimeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(4, 'GetRuntimeId', ((1, 'pRetVal'),)))
    IRawElementProviderFragment.get_BoundingRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UiaRect_head))(5, 'get_BoundingRectangle', ((1, 'pRetVal'),)))
    IRawElementProviderFragment.GetEmbeddedFragmentRoots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(6, 'GetEmbeddedFragmentRoots', ((1, 'pRetVal'),)))
    IRawElementProviderFragment.SetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'SetFocus', ()))
    IRawElementProviderFragment.get_FragmentRoot = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderFragmentRoot_head))(8, 'get_FragmentRoot', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderFragment
def _define_IRawElementProviderFragmentRoot_head():
    class IRawElementProviderFragmentRoot(win32more.System.Com.IUnknown_head):
        Guid = Guid('620ce2a5-ab8f-40a9-86-cb-de-3c-75-59-9b-58')
    return IRawElementProviderFragmentRoot
def _define_IRawElementProviderFragmentRoot():
    IRawElementProviderFragmentRoot = win32more.UI.Accessibility.IRawElementProviderFragmentRoot_head
    IRawElementProviderFragmentRoot.ElementProviderFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,POINTER(win32more.UI.Accessibility.IRawElementProviderFragment_head))(3, 'ElementProviderFromPoint', ((1, 'x'),(1, 'y'),(1, 'pRetVal'),)))
    IRawElementProviderFragmentRoot.GetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderFragment_head))(4, 'GetFocus', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderFragmentRoot
def _define_IRawElementProviderHostingAccessibles_head():
    class IRawElementProviderHostingAccessibles(win32more.System.Com.IUnknown_head):
        Guid = Guid('24be0b07-d37d-487a-98-cf-a1-3e-d4-65-e9-b3')
    return IRawElementProviderHostingAccessibles
def _define_IRawElementProviderHostingAccessibles():
    IRawElementProviderHostingAccessibles = win32more.UI.Accessibility.IRawElementProviderHostingAccessibles_head
    IRawElementProviderHostingAccessibles.GetEmbeddedAccessibles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(3, 'GetEmbeddedAccessibles', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderHostingAccessibles
def _define_IRawElementProviderHwndOverride_head():
    class IRawElementProviderHwndOverride(win32more.System.Com.IUnknown_head):
        Guid = Guid('1d5df27c-8947-4425-b8-d9-79-78-7b-b4-60-b8')
    return IRawElementProviderHwndOverride
def _define_IRawElementProviderHwndOverride():
    IRawElementProviderHwndOverride = win32more.UI.Accessibility.IRawElementProviderHwndOverride_head
    IRawElementProviderHwndOverride.GetOverrideProviderForHwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(3, 'GetOverrideProviderForHwnd', ((1, 'hwnd'),(1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderHwndOverride
def _define_IRawElementProviderSimple_head():
    class IRawElementProviderSimple(win32more.System.Com.IUnknown_head):
        Guid = Guid('d6dd68d1-86fd-4332-86-66-9a-be-de-a2-d2-4c')
    return IRawElementProviderSimple
def _define_IRawElementProviderSimple():
    IRawElementProviderSimple = win32more.UI.Accessibility.IRawElementProviderSimple_head
    IRawElementProviderSimple.get_ProviderOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ProviderOptions))(3, 'get_ProviderOptions', ((1, 'pRetVal'),)))
    IRawElementProviderSimple.GetPatternProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PATTERN_ID,POINTER(win32more.System.Com.IUnknown_head))(4, 'GetPatternProvider', ((1, 'patternId'),(1, 'pRetVal'),)))
    IRawElementProviderSimple.GetPropertyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PROPERTY_ID,POINTER(win32more.System.Com.VARIANT_head))(5, 'GetPropertyValue', ((1, 'propertyId'),(1, 'pRetVal'),)))
    IRawElementProviderSimple.get_HostRawElementProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(6, 'get_HostRawElementProvider', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderSimple
def _define_IRawElementProviderSimple2_head():
    class IRawElementProviderSimple2(win32more.UI.Accessibility.IRawElementProviderSimple_head):
        Guid = Guid('a0a839a9-8da1-4a82-80-6a-8e-0d-44-e7-9f-56')
    return IRawElementProviderSimple2
def _define_IRawElementProviderSimple2():
    IRawElementProviderSimple2 = win32more.UI.Accessibility.IRawElementProviderSimple2_head
    IRawElementProviderSimple2.ShowContextMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'ShowContextMenu', ()))
    win32more.UI.Accessibility.IRawElementProviderSimple
    return IRawElementProviderSimple2
def _define_IRawElementProviderSimple3_head():
    class IRawElementProviderSimple3(win32more.UI.Accessibility.IRawElementProviderSimple2_head):
        Guid = Guid('fcf5d820-d7ec-4613-bd-f6-42-a8-4c-e7-da-af')
    return IRawElementProviderSimple3
def _define_IRawElementProviderSimple3():
    IRawElementProviderSimple3 = win32more.UI.Accessibility.IRawElementProviderSimple3_head
    IRawElementProviderSimple3.GetMetadataValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.UI.Accessibility.UIA_METADATA_ID,POINTER(win32more.System.Com.VARIANT_head))(8, 'GetMetadataValue', ((1, 'targetId'),(1, 'metadataId'),(1, 'returnVal'),)))
    win32more.UI.Accessibility.IRawElementProviderSimple2
    return IRawElementProviderSimple3
def _define_IRawElementProviderWindowlessSite_head():
    class IRawElementProviderWindowlessSite(win32more.System.Com.IUnknown_head):
        Guid = Guid('0a2a93cc-bfad-42ac-9b-2e-09-91-fb-0d-3e-a0')
    return IRawElementProviderWindowlessSite
def _define_IRawElementProviderWindowlessSite():
    IRawElementProviderWindowlessSite = win32more.UI.Accessibility.IRawElementProviderWindowlessSite_head
    IRawElementProviderWindowlessSite.GetAdjacentFragment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.NavigateDirection,POINTER(win32more.UI.Accessibility.IRawElementProviderFragment_head))(3, 'GetAdjacentFragment', ((1, 'direction'),(1, 'ppParent'),)))
    IRawElementProviderWindowlessSite.GetRuntimeIdPrefix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(4, 'GetRuntimeIdPrefix', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderWindowlessSite
def _define_IRichEditUiaInformation_head():
    class IRichEditUiaInformation(win32more.System.Com.IUnknown_head):
        pass
    return IRichEditUiaInformation
def _define_IRichEditUiaInformation():
    IRichEditUiaInformation = win32more.UI.Accessibility.IRichEditUiaInformation_head
    IRichEditUiaInformation.GetBoundaryRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UiaRect_head))(3, 'GetBoundaryRectangle', ((1, 'pUiaRect'),)))
    IRichEditUiaInformation.IsVisible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'IsVisible', ()))
    win32more.System.Com.IUnknown
    return IRichEditUiaInformation
def _define_IRicheditWindowlessAccessibility_head():
    class IRicheditWindowlessAccessibility(win32more.System.Com.IUnknown_head):
        pass
    return IRicheditWindowlessAccessibility
def _define_IRicheditWindowlessAccessibility():
    IRicheditWindowlessAccessibility = win32more.UI.Accessibility.IRicheditWindowlessAccessibility_head
    IRicheditWindowlessAccessibility.CreateProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderWindowlessSite_head,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(3, 'CreateProvider', ((1, 'pSite'),(1, 'ppProvider'),)))
    win32more.System.Com.IUnknown
    return IRicheditWindowlessAccessibility
def _define_IScrollItemProvider_head():
    class IScrollItemProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('2360c714-4bf1-4b26-ba-65-9b-21-31-61-27-eb')
    return IScrollItemProvider
def _define_IScrollItemProvider():
    IScrollItemProvider = win32more.UI.Accessibility.IScrollItemProvider_head
    IScrollItemProvider.ScrollIntoView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'ScrollIntoView', ()))
    win32more.System.Com.IUnknown
    return IScrollItemProvider
def _define_IScrollProvider_head():
    class IScrollProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('b38b8077-1fc3-42a5-8c-ae-d4-0c-22-15-05-5a')
    return IScrollProvider
def _define_IScrollProvider():
    IScrollProvider = win32more.UI.Accessibility.IScrollProvider_head
    IScrollProvider.Scroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.ScrollAmount,win32more.UI.Accessibility.ScrollAmount)(3, 'Scroll', ((1, 'horizontalAmount'),(1, 'verticalAmount'),)))
    IScrollProvider.SetScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double)(4, 'SetScrollPercent', ((1, 'horizontalPercent'),(1, 'verticalPercent'),)))
    IScrollProvider.get_HorizontalScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(5, 'get_HorizontalScrollPercent', ((1, 'pRetVal'),)))
    IScrollProvider.get_VerticalScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(6, 'get_VerticalScrollPercent', ((1, 'pRetVal'),)))
    IScrollProvider.get_HorizontalViewSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(7, 'get_HorizontalViewSize', ((1, 'pRetVal'),)))
    IScrollProvider.get_VerticalViewSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(8, 'get_VerticalViewSize', ((1, 'pRetVal'),)))
    IScrollProvider.get_HorizontallyScrollable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(9, 'get_HorizontallyScrollable', ((1, 'pRetVal'),)))
    IScrollProvider.get_VerticallyScrollable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(10, 'get_VerticallyScrollable', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IScrollProvider
def _define_ISelectionItemProvider_head():
    class ISelectionItemProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('2acad808-b2d4-452d-a4-07-91-ff-1a-d1-67-b2')
    return ISelectionItemProvider
def _define_ISelectionItemProvider():
    ISelectionItemProvider = win32more.UI.Accessibility.ISelectionItemProvider_head
    ISelectionItemProvider.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Select', ()))
    ISelectionItemProvider.AddToSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'AddToSelection', ()))
    ISelectionItemProvider.RemoveFromSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'RemoveFromSelection', ()))
    ISelectionItemProvider.get_IsSelected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(6, 'get_IsSelected', ((1, 'pRetVal'),)))
    ISelectionItemProvider.get_SelectionContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(7, 'get_SelectionContainer', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ISelectionItemProvider
def _define_ISelectionProvider_head():
    class ISelectionProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('fb8b03af-3bdf-48d4-bd-36-1a-65-79-3b-e1-68')
    return ISelectionProvider
def _define_ISelectionProvider():
    ISelectionProvider = win32more.UI.Accessibility.ISelectionProvider_head
    ISelectionProvider.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(3, 'GetSelection', ((1, 'pRetVal'),)))
    ISelectionProvider.get_CanSelectMultiple = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(4, 'get_CanSelectMultiple', ((1, 'pRetVal'),)))
    ISelectionProvider.get_IsSelectionRequired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(5, 'get_IsSelectionRequired', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ISelectionProvider
def _define_ISelectionProvider2_head():
    class ISelectionProvider2(win32more.UI.Accessibility.ISelectionProvider_head):
        Guid = Guid('14f68475-ee1c-44f6-a8-69-d2-39-38-1f-0f-e7')
    return ISelectionProvider2
def _define_ISelectionProvider2():
    ISelectionProvider2 = win32more.UI.Accessibility.ISelectionProvider2_head
    ISelectionProvider2.get_FirstSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(6, 'get_FirstSelectedItem', ((1, 'retVal'),)))
    ISelectionProvider2.get_LastSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(7, 'get_LastSelectedItem', ((1, 'retVal'),)))
    ISelectionProvider2.get_CurrentSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(8, 'get_CurrentSelectedItem', ((1, 'retVal'),)))
    ISelectionProvider2.get_ItemCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_ItemCount', ((1, 'retVal'),)))
    win32more.UI.Accessibility.ISelectionProvider
    return ISelectionProvider2
def _define_ISpreadsheetItemProvider_head():
    class ISpreadsheetItemProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('eaed4660-7b3d-4879-a2-e6-36-5c-e6-03-f3-d0')
    return ISpreadsheetItemProvider
def _define_ISpreadsheetItemProvider():
    ISpreadsheetItemProvider = win32more.UI.Accessibility.ISpreadsheetItemProvider_head
    ISpreadsheetItemProvider.get_Formula = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(3, 'get_Formula', ((1, 'pRetVal'),)))
    ISpreadsheetItemProvider.GetAnnotationObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(4, 'GetAnnotationObjects', ((1, 'pRetVal'),)))
    ISpreadsheetItemProvider.GetAnnotationTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(5, 'GetAnnotationTypes', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ISpreadsheetItemProvider
def _define_ISpreadsheetProvider_head():
    class ISpreadsheetProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('6f6b5d35-5525-4f80-b7-58-85-47-38-32-ff-c7')
    return ISpreadsheetProvider
def _define_ISpreadsheetProvider():
    ISpreadsheetProvider = win32more.UI.Accessibility.ISpreadsheetProvider_head
    ISpreadsheetProvider.GetItemByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(3, 'GetItemByName', ((1, 'name'),(1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ISpreadsheetProvider
def _define_IStylesProvider_head():
    class IStylesProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('19b6b649-f5d7-4a6d-bd-cb-12-92-52-be-58-8a')
    return IStylesProvider
def _define_IStylesProvider():
    IStylesProvider = win32more.UI.Accessibility.IStylesProvider_head
    IStylesProvider.get_StyleId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_STYLE_ID))(3, 'get_StyleId', ((1, 'retVal'),)))
    IStylesProvider.get_StyleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'get_StyleName', ((1, 'retVal'),)))
    IStylesProvider.get_FillColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(5, 'get_FillColor', ((1, 'retVal'),)))
    IStylesProvider.get_FillPatternStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(6, 'get_FillPatternStyle', ((1, 'retVal'),)))
    IStylesProvider.get_Shape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Shape', ((1, 'retVal'),)))
    IStylesProvider.get_FillPatternColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_FillPatternColor', ((1, 'retVal'),)))
    IStylesProvider.get_ExtendedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_ExtendedProperties', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IStylesProvider
def _define_ISynchronizedInputProvider_head():
    class ISynchronizedInputProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('29db1a06-02ce-4cf7-9b-42-56-5d-4f-ab-20-ee')
    return ISynchronizedInputProvider
def _define_ISynchronizedInputProvider():
    ISynchronizedInputProvider = win32more.UI.Accessibility.ISynchronizedInputProvider_head
    ISynchronizedInputProvider.StartListening = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.SynchronizedInputType)(3, 'StartListening', ((1, 'inputType'),)))
    ISynchronizedInputProvider.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Cancel', ()))
    win32more.System.Com.IUnknown
    return ISynchronizedInputProvider
def _define_ITableItemProvider_head():
    class ITableItemProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('b9734fa6-771f-4d78-9c-90-25-17-99-93-49-cd')
    return ITableItemProvider
def _define_ITableItemProvider():
    ITableItemProvider = win32more.UI.Accessibility.ITableItemProvider_head
    ITableItemProvider.GetRowHeaderItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(3, 'GetRowHeaderItems', ((1, 'pRetVal'),)))
    ITableItemProvider.GetColumnHeaderItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(4, 'GetColumnHeaderItems', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ITableItemProvider
def _define_ITableProvider_head():
    class ITableProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('9c860395-97b3-490a-b5-2a-85-8c-c2-2a-f1-66')
    return ITableProvider
def _define_ITableProvider():
    ITableProvider = win32more.UI.Accessibility.ITableProvider_head
    ITableProvider.GetRowHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(3, 'GetRowHeaders', ((1, 'pRetVal'),)))
    ITableProvider.GetColumnHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(4, 'GetColumnHeaders', ((1, 'pRetVal'),)))
    ITableProvider.get_RowOrColumnMajor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.RowOrColumnMajor))(5, 'get_RowOrColumnMajor', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ITableProvider
def _define_ITextChildProvider_head():
    class ITextChildProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('4c2de2b9-c88f-4f88-a1-11-f1-d3-36-b7-d1-a9')
    return ITextChildProvider
def _define_ITextChildProvider():
    ITextChildProvider = win32more.UI.Accessibility.ITextChildProvider_head
    ITextChildProvider.get_TextContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(3, 'get_TextContainer', ((1, 'pRetVal'),)))
    ITextChildProvider.get_TextRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head))(4, 'get_TextRange', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ITextChildProvider
def _define_ITextEditProvider_head():
    class ITextEditProvider(win32more.UI.Accessibility.ITextProvider_head):
        Guid = Guid('ea3605b4-3a05-400e-b5-f9-4e-91-b4-0f-61-76')
    return ITextEditProvider
def _define_ITextEditProvider():
    ITextEditProvider = win32more.UI.Accessibility.ITextEditProvider_head
    ITextEditProvider.GetActiveComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head))(9, 'GetActiveComposition', ((1, 'pRetVal'),)))
    ITextEditProvider.GetConversionTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head))(10, 'GetConversionTarget', ((1, 'pRetVal'),)))
    win32more.UI.Accessibility.ITextProvider
    return ITextEditProvider
def _define_ITextProvider_head():
    class ITextProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('3589c92c-63f3-4367-99-bb-ad-a6-53-b7-7c-f2')
    return ITextProvider
def _define_ITextProvider():
    ITextProvider = win32more.UI.Accessibility.ITextProvider_head
    ITextProvider.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(3, 'GetSelection', ((1, 'pRetVal'),)))
    ITextProvider.GetVisibleRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(4, 'GetVisibleRanges', ((1, 'pRetVal'),)))
    ITextProvider.RangeFromChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head))(5, 'RangeFromChild', ((1, 'childElement'),(1, 'pRetVal'),)))
    ITextProvider.RangeFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UiaPoint,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head))(6, 'RangeFromPoint', ((1, 'point'),(1, 'pRetVal'),)))
    ITextProvider.get_DocumentRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head))(7, 'get_DocumentRange', ((1, 'pRetVal'),)))
    ITextProvider.get_SupportedTextSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.SupportedTextSelection))(8, 'get_SupportedTextSelection', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ITextProvider
def _define_ITextProvider2_head():
    class ITextProvider2(win32more.UI.Accessibility.ITextProvider_head):
        Guid = Guid('0dc5e6ed-3e16-4bf1-8f-9a-a9-79-87-8b-c1-95')
    return ITextProvider2
def _define_ITextProvider2():
    ITextProvider2 = win32more.UI.Accessibility.ITextProvider2_head
    ITextProvider2.RangeFromAnnotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head))(9, 'RangeFromAnnotation', ((1, 'annotationElement'),(1, 'pRetVal'),)))
    ITextProvider2.GetCaretRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.UI.Accessibility.ITextRangeProvider_head))(10, 'GetCaretRange', ((1, 'isActive'),(1, 'pRetVal'),)))
    win32more.UI.Accessibility.ITextProvider
    return ITextProvider2
def _define_ITextRangeProvider_head():
    class ITextRangeProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('5347ad7b-c355-46f8-af-f5-90-90-33-58-2f-63')
    return ITextRangeProvider
def _define_ITextRangeProvider():
    ITextRangeProvider = win32more.UI.Accessibility.ITextRangeProvider_head
    ITextRangeProvider.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head))(3, 'Clone', ((1, 'pRetVal'),)))
    ITextRangeProvider.Compare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.ITextRangeProvider_head,POINTER(win32more.Foundation.BOOL))(4, 'Compare', ((1, 'range'),(1, 'pRetVal'),)))
    ITextRangeProvider.CompareEndpoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.ITextRangeProvider_head,win32more.UI.Accessibility.TextPatternRangeEndpoint,POINTER(Int32))(5, 'CompareEndpoints', ((1, 'endpoint'),(1, 'targetRange'),(1, 'targetEndpoint'),(1, 'pRetVal'),)))
    ITextRangeProvider.ExpandToEnclosingUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextUnit)(6, 'ExpandToEnclosingUnit', ((1, 'unit'),)))
    ITextRangeProvider.FindAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_TEXTATTRIBUTE_ID,win32more.System.Com.VARIANT,win32more.Foundation.BOOL,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head))(7, 'FindAttribute', ((1, 'attributeId'),(1, 'val'),(1, 'backward'),(1, 'pRetVal'),)))
    ITextRangeProvider.FindText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head))(8, 'FindText', ((1, 'text'),(1, 'backward'),(1, 'ignoreCase'),(1, 'pRetVal'),)))
    ITextRangeProvider.GetAttributeValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_TEXTATTRIBUTE_ID,POINTER(win32more.System.Com.VARIANT_head))(9, 'GetAttributeValue', ((1, 'attributeId'),(1, 'pRetVal'),)))
    ITextRangeProvider.GetBoundingRectangles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(10, 'GetBoundingRectangles', ((1, 'pRetVal'),)))
    ITextRangeProvider.GetEnclosingElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(11, 'GetEnclosingElement', ((1, 'pRetVal'),)))
    ITextRangeProvider.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR))(12, 'GetText', ((1, 'maxLength'),(1, 'pRetVal'),)))
    ITextRangeProvider.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextUnit,Int32,POINTER(Int32))(13, 'Move', ((1, 'unit'),(1, 'count'),(1, 'pRetVal'),)))
    ITextRangeProvider.MoveEndpointByUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.TextUnit,Int32,POINTER(Int32))(14, 'MoveEndpointByUnit', ((1, 'endpoint'),(1, 'unit'),(1, 'count'),(1, 'pRetVal'),)))
    ITextRangeProvider.MoveEndpointByRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.ITextRangeProvider_head,win32more.UI.Accessibility.TextPatternRangeEndpoint)(15, 'MoveEndpointByRange', ((1, 'endpoint'),(1, 'targetRange'),(1, 'targetEndpoint'),)))
    ITextRangeProvider.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'Select', ()))
    ITextRangeProvider.AddToSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(17, 'AddToSelection', ()))
    ITextRangeProvider.RemoveFromSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(18, 'RemoveFromSelection', ()))
    ITextRangeProvider.ScrollIntoView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(19, 'ScrollIntoView', ((1, 'alignToTop'),)))
    ITextRangeProvider.GetChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(20, 'GetChildren', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ITextRangeProvider
def _define_ITextRangeProvider2_head():
    class ITextRangeProvider2(win32more.UI.Accessibility.ITextRangeProvider_head):
        Guid = Guid('9bbce42c-1921-4f18-89-ca-db-a1-91-0a-03-86')
    return ITextRangeProvider2
def _define_ITextRangeProvider2():
    ITextRangeProvider2 = win32more.UI.Accessibility.ITextRangeProvider2_head
    ITextRangeProvider2.ShowContextMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(21, 'ShowContextMenu', ()))
    win32more.UI.Accessibility.ITextRangeProvider
    return ITextRangeProvider2
def _define_IToggleProvider_head():
    class IToggleProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('56d00bd0-c4f4-433c-a8-36-1a-52-a5-7e-08-92')
    return IToggleProvider
def _define_IToggleProvider():
    IToggleProvider = win32more.UI.Accessibility.IToggleProvider_head
    IToggleProvider.Toggle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Toggle', ()))
    IToggleProvider.get_ToggleState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ToggleState))(4, 'get_ToggleState', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IToggleProvider
def _define_ITransformProvider_head():
    class ITransformProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('6829ddc4-4f91-4ffa-b8-6f-bd-3e-29-87-cb-4c')
    return ITransformProvider
def _define_ITransformProvider():
    ITransformProvider = win32more.UI.Accessibility.ITransformProvider_head
    ITransformProvider.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double)(3, 'Move', ((1, 'x'),(1, 'y'),)))
    ITransformProvider.Resize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double)(4, 'Resize', ((1, 'width'),(1, 'height'),)))
    ITransformProvider.Rotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(5, 'Rotate', ((1, 'degrees'),)))
    ITransformProvider.get_CanMove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(6, 'get_CanMove', ((1, 'pRetVal'),)))
    ITransformProvider.get_CanResize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(7, 'get_CanResize', ((1, 'pRetVal'),)))
    ITransformProvider.get_CanRotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(8, 'get_CanRotate', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ITransformProvider
def _define_ITransformProvider2_head():
    class ITransformProvider2(win32more.UI.Accessibility.ITransformProvider_head):
        Guid = Guid('4758742f-7ac2-460c-bc-48-09-fc-09-30-8a-93')
    return ITransformProvider2
def _define_ITransformProvider2():
    ITransformProvider2 = win32more.UI.Accessibility.ITransformProvider2_head
    ITransformProvider2.Zoom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(9, 'Zoom', ((1, 'zoom'),)))
    ITransformProvider2.get_CanZoom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(10, 'get_CanZoom', ((1, 'pRetVal'),)))
    ITransformProvider2.get_ZoomLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(11, 'get_ZoomLevel', ((1, 'pRetVal'),)))
    ITransformProvider2.get_ZoomMinimum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(12, 'get_ZoomMinimum', ((1, 'pRetVal'),)))
    ITransformProvider2.get_ZoomMaximum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(13, 'get_ZoomMaximum', ((1, 'pRetVal'),)))
    ITransformProvider2.ZoomByUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.ZoomUnit)(14, 'ZoomByUnit', ((1, 'zoomUnit'),)))
    win32more.UI.Accessibility.ITransformProvider
    return ITransformProvider2
def _define_IUIAutomation_head():
    class IUIAutomation(win32more.System.Com.IUnknown_head):
        Guid = Guid('30cbe57d-d9d0-452a-ab-13-7a-c5-ac-48-25-ee')
    return IUIAutomation
def _define_IUIAutomation():
    IUIAutomation = win32more.UI.Accessibility.IUIAutomation_head
    IUIAutomation.CompareElements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.Foundation.BOOL))(3, 'CompareElements', ((1, 'el1'),(1, 'el2'),(1, 'areSame'),)))
    IUIAutomation.CompareRuntimeIds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.Foundation.BOOL))(4, 'CompareRuntimeIds', ((1, 'runtimeId1'),(1, 'runtimeId2'),(1, 'areSame'),)))
    IUIAutomation.GetRootElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(5, 'GetRootElement', ((1, 'root'),)))
    IUIAutomation.ElementFromHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(6, 'ElementFromHandle', ((1, 'hwnd'),(1, 'element'),)))
    IUIAutomation.ElementFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(7, 'ElementFromPoint', ((1, 'pt'),(1, 'element'),)))
    IUIAutomation.GetFocusedElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(8, 'GetFocusedElement', ((1, 'element'),)))
    IUIAutomation.GetRootElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(9, 'GetRootElementBuildCache', ((1, 'cacheRequest'),(1, 'root'),)))
    IUIAutomation.ElementFromHandleBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(10, 'ElementFromHandleBuildCache', ((1, 'hwnd'),(1, 'cacheRequest'),(1, 'element'),)))
    IUIAutomation.ElementFromPointBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(11, 'ElementFromPointBuildCache', ((1, 'pt'),(1, 'cacheRequest'),(1, 'element'),)))
    IUIAutomation.GetFocusedElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(12, 'GetFocusedElementBuildCache', ((1, 'cacheRequest'),(1, 'element'),)))
    IUIAutomation.CreateTreeWalker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCondition_head,POINTER(win32more.UI.Accessibility.IUIAutomationTreeWalker_head))(13, 'CreateTreeWalker', ((1, 'pCondition'),(1, 'walker'),)))
    IUIAutomation.get_ControlViewWalker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTreeWalker_head))(14, 'get_ControlViewWalker', ((1, 'walker'),)))
    IUIAutomation.get_ContentViewWalker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTreeWalker_head))(15, 'get_ContentViewWalker', ((1, 'walker'),)))
    IUIAutomation.get_RawViewWalker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTreeWalker_head))(16, 'get_RawViewWalker', ((1, 'walker'),)))
    IUIAutomation.get_RawViewCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(17, 'get_RawViewCondition', ((1, 'condition'),)))
    IUIAutomation.get_ControlViewCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(18, 'get_ControlViewCondition', ((1, 'condition'),)))
    IUIAutomation.get_ContentViewCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(19, 'get_ContentViewCondition', ((1, 'condition'),)))
    IUIAutomation.CreateCacheRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCacheRequest_head))(20, 'CreateCacheRequest', ((1, 'cacheRequest'),)))
    IUIAutomation.CreateTrueCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(21, 'CreateTrueCondition', ((1, 'newCondition'),)))
    IUIAutomation.CreateFalseCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(22, 'CreateFalseCondition', ((1, 'newCondition'),)))
    IUIAutomation.CreatePropertyCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PROPERTY_ID,win32more.System.Com.VARIANT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(23, 'CreatePropertyCondition', ((1, 'propertyId'),(1, 'value'),(1, 'newCondition'),)))
    IUIAutomation.CreatePropertyConditionEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PROPERTY_ID,win32more.System.Com.VARIANT,win32more.UI.Accessibility.PropertyConditionFlags,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(24, 'CreatePropertyConditionEx', ((1, 'propertyId'),(1, 'value'),(1, 'flags'),(1, 'newCondition'),)))
    IUIAutomation.CreateAndCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.IUIAutomationCondition_head,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(25, 'CreateAndCondition', ((1, 'condition1'),(1, 'condition2'),(1, 'newCondition'),)))
    IUIAutomation.CreateAndConditionFromArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(26, 'CreateAndConditionFromArray', ((1, 'conditions'),(1, 'newCondition'),)))
    IUIAutomation.CreateAndConditionFromNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head),Int32,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(27, 'CreateAndConditionFromNativeArray', ((1, 'conditions'),(1, 'conditionCount'),(1, 'newCondition'),)))
    IUIAutomation.CreateOrCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.IUIAutomationCondition_head,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(28, 'CreateOrCondition', ((1, 'condition1'),(1, 'condition2'),(1, 'newCondition'),)))
    IUIAutomation.CreateOrConditionFromArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(29, 'CreateOrConditionFromArray', ((1, 'conditions'),(1, 'newCondition'),)))
    IUIAutomation.CreateOrConditionFromNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head),Int32,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(30, 'CreateOrConditionFromNativeArray', ((1, 'conditions'),(1, 'conditionCount'),(1, 'newCondition'),)))
    IUIAutomation.CreateNotCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCondition_head,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(31, 'CreateNotCondition', ((1, 'condition'),(1, 'newCondition'),)))
    IUIAutomation.AddAutomationEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_EVENT_ID,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationEventHandler_head)(32, 'AddAutomationEventHandler', ((1, 'eventId'),(1, 'element'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomation.RemoveAutomationEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_EVENT_ID,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationEventHandler_head)(33, 'RemoveAutomationEventHandler', ((1, 'eventId'),(1, 'element'),(1, 'handler'),)))
    IUIAutomation.AddPropertyChangedEventHandlerNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head,POINTER(win32more.UI.Accessibility.UIA_PROPERTY_ID),Int32)(34, 'AddPropertyChangedEventHandlerNativeArray', ((1, 'element'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),(1, 'propertyArray'),(1, 'propertyCount'),)))
    IUIAutomation.AddPropertyChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head,POINTER(win32more.System.Com.SAFEARRAY_head))(35, 'AddPropertyChangedEventHandler', ((1, 'element'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),(1, 'propertyArray'),)))
    IUIAutomation.RemovePropertyChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head)(36, 'RemovePropertyChangedEventHandler', ((1, 'element'),(1, 'handler'),)))
    IUIAutomation.AddStructureChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationStructureChangedEventHandler_head)(37, 'AddStructureChangedEventHandler', ((1, 'element'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomation.RemoveStructureChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationStructureChangedEventHandler_head)(38, 'RemoveStructureChangedEventHandler', ((1, 'element'),(1, 'handler'),)))
    IUIAutomation.AddFocusChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationFocusChangedEventHandler_head)(39, 'AddFocusChangedEventHandler', ((1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomation.RemoveFocusChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationFocusChangedEventHandler_head)(40, 'RemoveFocusChangedEventHandler', ((1, 'handler'),)))
    IUIAutomation.RemoveAllEventHandlers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(41, 'RemoveAllEventHandlers', ()))
    IUIAutomation.IntNativeArrayToSafeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),Int32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(42, 'IntNativeArrayToSafeArray', ((1, 'array'),(1, 'arrayCount'),(1, 'safeArray'),)))
    IUIAutomation.IntSafeArrayToNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(POINTER(Int32)),POINTER(Int32))(43, 'IntSafeArrayToNativeArray', ((1, 'intArray'),(1, 'array'),(1, 'arrayCount'),)))
    IUIAutomation.RectToVariant = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.RECT,POINTER(win32more.System.Com.VARIANT_head))(44, 'RectToVariant', ((1, 'rc'),(1, 'var'),)))
    IUIAutomation.VariantToRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.RECT_head))(45, 'VariantToRect', ((1, 'var'),(1, 'rc'),)))
    IUIAutomation.SafeArrayToRectNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(POINTER(win32more.Foundation.RECT_head)),POINTER(Int32))(46, 'SafeArrayToRectNativeArray', ((1, 'rects'),(1, 'rectArray'),(1, 'rectArrayCount'),)))
    IUIAutomation.CreateProxyFactoryEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationProxyFactory_head,POINTER(win32more.UI.Accessibility.IUIAutomationProxyFactoryEntry_head))(47, 'CreateProxyFactoryEntry', ((1, 'factory'),(1, 'factoryEntry'),)))
    IUIAutomation.get_ProxyFactoryMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationProxyFactoryMapping_head))(48, 'get_ProxyFactoryMapping', ((1, 'factoryMapping'),)))
    IUIAutomation.GetPropertyProgrammaticName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PROPERTY_ID,POINTER(win32more.Foundation.BSTR))(49, 'GetPropertyProgrammaticName', ((1, 'property'),(1, 'name'),)))
    IUIAutomation.GetPatternProgrammaticName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PATTERN_ID,POINTER(win32more.Foundation.BSTR))(50, 'GetPatternProgrammaticName', ((1, 'pattern'),(1, 'name'),)))
    IUIAutomation.PollForPotentialSupportedPatterns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(51, 'PollForPotentialSupportedPatterns', ((1, 'pElement'),(1, 'patternIds'),(1, 'patternNames'),)))
    IUIAutomation.PollForPotentialSupportedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(52, 'PollForPotentialSupportedProperties', ((1, 'pElement'),(1, 'propertyIds'),(1, 'propertyNames'),)))
    IUIAutomation.CheckNotSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BOOL))(53, 'CheckNotSupported', ((1, 'value'),(1, 'isNotSupported'),)))
    IUIAutomation.get_ReservedNotSupportedValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(54, 'get_ReservedNotSupportedValue', ((1, 'notSupportedValue'),)))
    IUIAutomation.get_ReservedMixedAttributeValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(55, 'get_ReservedMixedAttributeValue', ((1, 'mixedAttributeValue'),)))
    IUIAutomation.ElementFromIAccessible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessible_head,Int32,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(56, 'ElementFromIAccessible', ((1, 'accessible'),(1, 'childId'),(1, 'element'),)))
    IUIAutomation.ElementFromIAccessibleBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessible_head,Int32,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(57, 'ElementFromIAccessibleBuildCache', ((1, 'accessible'),(1, 'childId'),(1, 'cacheRequest'),(1, 'element'),)))
    win32more.System.Com.IUnknown
    return IUIAutomation
def _define_IUIAutomation2_head():
    class IUIAutomation2(win32more.UI.Accessibility.IUIAutomation_head):
        Guid = Guid('34723aff-0c9d-49d0-98-96-7a-b5-2d-f8-cd-8a')
    return IUIAutomation2
def _define_IUIAutomation2():
    IUIAutomation2 = win32more.UI.Accessibility.IUIAutomation2_head
    IUIAutomation2.get_AutoSetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(58, 'get_AutoSetFocus', ((1, 'autoSetFocus'),)))
    IUIAutomation2.put_AutoSetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(59, 'put_AutoSetFocus', ((1, 'autoSetFocus'),)))
    IUIAutomation2.get_ConnectionTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(60, 'get_ConnectionTimeout', ((1, 'timeout'),)))
    IUIAutomation2.put_ConnectionTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(61, 'put_ConnectionTimeout', ((1, 'timeout'),)))
    IUIAutomation2.get_TransactionTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(62, 'get_TransactionTimeout', ((1, 'timeout'),)))
    IUIAutomation2.put_TransactionTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(63, 'put_TransactionTimeout', ((1, 'timeout'),)))
    win32more.UI.Accessibility.IUIAutomation
    return IUIAutomation2
def _define_IUIAutomation3_head():
    class IUIAutomation3(win32more.UI.Accessibility.IUIAutomation2_head):
        Guid = Guid('73d768da-9b51-4b89-93-6e-c2-09-29-09-73-e7')
    return IUIAutomation3
def _define_IUIAutomation3():
    IUIAutomation3 = win32more.UI.Accessibility.IUIAutomation3_head
    IUIAutomation3.AddTextEditTextChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.TextEditChangeType,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler_head)(64, 'AddTextEditTextChangedEventHandler', ((1, 'element'),(1, 'scope'),(1, 'textEditChangeType'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomation3.RemoveTextEditTextChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler_head)(65, 'RemoveTextEditTextChangedEventHandler', ((1, 'element'),(1, 'handler'),)))
    win32more.UI.Accessibility.IUIAutomation2
    return IUIAutomation3
def _define_IUIAutomation4_head():
    class IUIAutomation4(win32more.UI.Accessibility.IUIAutomation3_head):
        Guid = Guid('1189c02a-05f8-4319-8e-21-e8-17-e3-db-28-60')
    return IUIAutomation4
def _define_IUIAutomation4():
    IUIAutomation4 = win32more.UI.Accessibility.IUIAutomation4_head
    IUIAutomation4.AddChangesEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,POINTER(Int32),Int32,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationChangesEventHandler_head)(66, 'AddChangesEventHandler', ((1, 'element'),(1, 'scope'),(1, 'changeTypes'),(1, 'changesCount'),(1, 'pCacheRequest'),(1, 'handler'),)))
    IUIAutomation4.RemoveChangesEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationChangesEventHandler_head)(67, 'RemoveChangesEventHandler', ((1, 'element'),(1, 'handler'),)))
    win32more.UI.Accessibility.IUIAutomation3
    return IUIAutomation4
def _define_IUIAutomation5_head():
    class IUIAutomation5(win32more.UI.Accessibility.IUIAutomation4_head):
        Guid = Guid('25f700c8-d816-4057-a9-dc-3c-bd-ee-77-e2-56')
    return IUIAutomation5
def _define_IUIAutomation5():
    IUIAutomation5 = win32more.UI.Accessibility.IUIAutomation5_head
    IUIAutomation5.AddNotificationEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationNotificationEventHandler_head)(68, 'AddNotificationEventHandler', ((1, 'element'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomation5.RemoveNotificationEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationNotificationEventHandler_head)(69, 'RemoveNotificationEventHandler', ((1, 'element'),(1, 'handler'),)))
    win32more.UI.Accessibility.IUIAutomation4
    return IUIAutomation5
def _define_IUIAutomation6_head():
    class IUIAutomation6(win32more.UI.Accessibility.IUIAutomation5_head):
        Guid = Guid('aae072da-29e3-413d-87-a7-19-2d-bf-81-ed-10')
    return IUIAutomation6
def _define_IUIAutomation6():
    IUIAutomation6 = win32more.UI.Accessibility.IUIAutomation6_head
    IUIAutomation6.CreateEventHandlerGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationEventHandlerGroup_head))(70, 'CreateEventHandlerGroup', ((1, 'handlerGroup'),)))
    IUIAutomation6.AddEventHandlerGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationEventHandlerGroup_head)(71, 'AddEventHandlerGroup', ((1, 'element'),(1, 'handlerGroup'),)))
    IUIAutomation6.RemoveEventHandlerGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationEventHandlerGroup_head)(72, 'RemoveEventHandlerGroup', ((1, 'element'),(1, 'handlerGroup'),)))
    IUIAutomation6.get_ConnectionRecoveryBehavior = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ConnectionRecoveryBehaviorOptions))(73, 'get_ConnectionRecoveryBehavior', ((1, 'connectionRecoveryBehaviorOptions'),)))
    IUIAutomation6.put_ConnectionRecoveryBehavior = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.ConnectionRecoveryBehaviorOptions)(74, 'put_ConnectionRecoveryBehavior', ((1, 'connectionRecoveryBehaviorOptions'),)))
    IUIAutomation6.get_CoalesceEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.CoalesceEventsOptions))(75, 'get_CoalesceEvents', ((1, 'coalesceEventsOptions'),)))
    IUIAutomation6.put_CoalesceEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.CoalesceEventsOptions)(76, 'put_CoalesceEvents', ((1, 'coalesceEventsOptions'),)))
    IUIAutomation6.AddActiveTextPositionChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler_head)(77, 'AddActiveTextPositionChangedEventHandler', ((1, 'element'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomation6.RemoveActiveTextPositionChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler_head)(78, 'RemoveActiveTextPositionChangedEventHandler', ((1, 'element'),(1, 'handler'),)))
    win32more.UI.Accessibility.IUIAutomation5
    return IUIAutomation6
def _define_IUIAutomationActiveTextPositionChangedEventHandler_head():
    class IUIAutomationActiveTextPositionChangedEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('f97933b0-8dae-4496-89-97-5b-a0-15-fe-0d-82')
    return IUIAutomationActiveTextPositionChangedEventHandler
def _define_IUIAutomationActiveTextPositionChangedEventHandler():
    IUIAutomationActiveTextPositionChangedEventHandler = win32more.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler_head
    IUIAutomationActiveTextPositionChangedEventHandler.HandleActiveTextPositionChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationTextRange_head)(3, 'HandleActiveTextPositionChangedEvent', ((1, 'sender'),(1, 'range'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationActiveTextPositionChangedEventHandler
def _define_IUIAutomationAndCondition_head():
    class IUIAutomationAndCondition(win32more.UI.Accessibility.IUIAutomationCondition_head):
        Guid = Guid('a7d0af36-b912-45fe-98-55-09-1d-dc-17-4a-ec')
    return IUIAutomationAndCondition
def _define_IUIAutomationAndCondition():
    IUIAutomationAndCondition = win32more.UI.Accessibility.IUIAutomationAndCondition_head
    IUIAutomationAndCondition.get_ChildCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(3, 'get_ChildCount', ((1, 'childCount'),)))
    IUIAutomationAndCondition.GetChildrenAsNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head)),POINTER(Int32))(4, 'GetChildrenAsNativeArray', ((1, 'childArray'),(1, 'childArrayCount'),)))
    IUIAutomationAndCondition.GetChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(5, 'GetChildren', ((1, 'childArray'),)))
    win32more.UI.Accessibility.IUIAutomationCondition
    return IUIAutomationAndCondition
def _define_IUIAutomationAnnotationPattern_head():
    class IUIAutomationAnnotationPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('9a175b21-339e-41b1-8e-8b-62-3f-6b-68-10-98')
    return IUIAutomationAnnotationPattern
def _define_IUIAutomationAnnotationPattern():
    IUIAutomationAnnotationPattern = win32more.UI.Accessibility.IUIAutomationAnnotationPattern_head
    IUIAutomationAnnotationPattern.get_CurrentAnnotationTypeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_ANNOTATIONTYPE))(3, 'get_CurrentAnnotationTypeId', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CurrentAnnotationTypeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'get_CurrentAnnotationTypeName', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CurrentAuthor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(5, 'get_CurrentAuthor', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CurrentDateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(6, 'get_CurrentDateTime', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CurrentTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(7, 'get_CurrentTarget', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CachedAnnotationTypeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_ANNOTATIONTYPE))(8, 'get_CachedAnnotationTypeId', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CachedAnnotationTypeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_CachedAnnotationTypeName', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CachedAuthor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'get_CachedAuthor', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CachedDateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_CachedDateTime', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CachedTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(12, 'get_CachedTarget', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationAnnotationPattern
def _define_IUIAutomationBoolCondition_head():
    class IUIAutomationBoolCondition(win32more.UI.Accessibility.IUIAutomationCondition_head):
        Guid = Guid('1b4e1f2e-75eb-4d0b-89-52-5a-69-98-8e-23-07')
    return IUIAutomationBoolCondition
def _define_IUIAutomationBoolCondition():
    IUIAutomationBoolCondition = win32more.UI.Accessibility.IUIAutomationBoolCondition_head
    IUIAutomationBoolCondition.get_BooleanValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'get_BooleanValue', ((1, 'boolVal'),)))
    win32more.UI.Accessibility.IUIAutomationCondition
    return IUIAutomationBoolCondition
def _define_IUIAutomationCacheRequest_head():
    class IUIAutomationCacheRequest(win32more.System.Com.IUnknown_head):
        Guid = Guid('b32a92b5-bc25-4078-9c-08-d7-ee-95-c4-8e-03')
    return IUIAutomationCacheRequest
def _define_IUIAutomationCacheRequest():
    IUIAutomationCacheRequest = win32more.UI.Accessibility.IUIAutomationCacheRequest_head
    IUIAutomationCacheRequest.AddProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PROPERTY_ID)(3, 'AddProperty', ((1, 'propertyId'),)))
    IUIAutomationCacheRequest.AddPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PATTERN_ID)(4, 'AddPattern', ((1, 'patternId'),)))
    IUIAutomationCacheRequest.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCacheRequest_head))(5, 'Clone', ((1, 'clonedRequest'),)))
    IUIAutomationCacheRequest.get_TreeScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.TreeScope))(6, 'get_TreeScope', ((1, 'scope'),)))
    IUIAutomationCacheRequest.put_TreeScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope)(7, 'put_TreeScope', ((1, 'scope'),)))
    IUIAutomationCacheRequest.get_TreeFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(8, 'get_TreeFilter', ((1, 'filter'),)))
    IUIAutomationCacheRequest.put_TreeFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCondition_head)(9, 'put_TreeFilter', ((1, 'filter'),)))
    IUIAutomationCacheRequest.get_AutomationElementMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.AutomationElementMode))(10, 'get_AutomationElementMode', ((1, 'mode'),)))
    IUIAutomationCacheRequest.put_AutomationElementMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.AutomationElementMode)(11, 'put_AutomationElementMode', ((1, 'mode'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationCacheRequest
def _define_IUIAutomationChangesEventHandler_head():
    class IUIAutomationChangesEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('58edca55-2c3e-4980-b1-b9-56-c1-7f-27-a2-a0')
    return IUIAutomationChangesEventHandler
def _define_IUIAutomationChangesEventHandler():
    IUIAutomationChangesEventHandler = win32more.UI.Accessibility.IUIAutomationChangesEventHandler_head
    IUIAutomationChangesEventHandler.HandleChangesEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.UiaChangeInfo_head),Int32)(3, 'HandleChangesEvent', ((1, 'sender'),(1, 'uiaChanges'),(1, 'changesCount'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationChangesEventHandler
def _define_IUIAutomationCondition_head():
    class IUIAutomationCondition(win32more.System.Com.IUnknown_head):
        Guid = Guid('352ffba8-0973-437c-a6-1f-f6-4c-af-d8-1d-f9')
    return IUIAutomationCondition
def _define_IUIAutomationCondition():
    IUIAutomationCondition = win32more.UI.Accessibility.IUIAutomationCondition_head
    win32more.System.Com.IUnknown
    return IUIAutomationCondition
def _define_IUIAutomationCustomNavigationPattern_head():
    class IUIAutomationCustomNavigationPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('01ea217a-1766-47ed-a6-cc-ac-f4-92-85-4b-1f')
    return IUIAutomationCustomNavigationPattern
def _define_IUIAutomationCustomNavigationPattern():
    IUIAutomationCustomNavigationPattern = win32more.UI.Accessibility.IUIAutomationCustomNavigationPattern_head
    IUIAutomationCustomNavigationPattern.Navigate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.NavigateDirection,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(3, 'Navigate', ((1, 'direction'),(1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationCustomNavigationPattern
def _define_IUIAutomationDockPattern_head():
    class IUIAutomationDockPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('fde5ef97-1464-48f6-90-bf-43-d0-94-8e-86-ec')
    return IUIAutomationDockPattern
def _define_IUIAutomationDockPattern():
    IUIAutomationDockPattern = win32more.UI.Accessibility.IUIAutomationDockPattern_head
    IUIAutomationDockPattern.SetDockPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.DockPosition)(3, 'SetDockPosition', ((1, 'dockPos'),)))
    IUIAutomationDockPattern.get_CurrentDockPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.DockPosition))(4, 'get_CurrentDockPosition', ((1, 'retVal'),)))
    IUIAutomationDockPattern.get_CachedDockPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.DockPosition))(5, 'get_CachedDockPosition', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationDockPattern
def _define_IUIAutomationDragPattern_head():
    class IUIAutomationDragPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dc7b570-1f54-4bad-bc-da-d3-6a-72-2f-b7-bd')
    return IUIAutomationDragPattern
def _define_IUIAutomationDragPattern():
    IUIAutomationDragPattern = win32more.UI.Accessibility.IUIAutomationDragPattern_head
    IUIAutomationDragPattern.get_CurrentIsGrabbed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'get_CurrentIsGrabbed', ((1, 'retVal'),)))
    IUIAutomationDragPattern.get_CachedIsGrabbed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(4, 'get_CachedIsGrabbed', ((1, 'retVal'),)))
    IUIAutomationDragPattern.get_CurrentDropEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(5, 'get_CurrentDropEffect', ((1, 'retVal'),)))
    IUIAutomationDragPattern.get_CachedDropEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(6, 'get_CachedDropEffect', ((1, 'retVal'),)))
    IUIAutomationDragPattern.get_CurrentDropEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(7, 'get_CurrentDropEffects', ((1, 'retVal'),)))
    IUIAutomationDragPattern.get_CachedDropEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(8, 'get_CachedDropEffects', ((1, 'retVal'),)))
    IUIAutomationDragPattern.GetCurrentGrabbedItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(9, 'GetCurrentGrabbedItems', ((1, 'retVal'),)))
    IUIAutomationDragPattern.GetCachedGrabbedItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(10, 'GetCachedGrabbedItems', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationDragPattern
def _define_IUIAutomationDropTargetPattern_head():
    class IUIAutomationDropTargetPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('69a095f7-eee4-430e-a4-6b-fb-73-b1-ae-39-a5')
    return IUIAutomationDropTargetPattern
def _define_IUIAutomationDropTargetPattern():
    IUIAutomationDropTargetPattern = win32more.UI.Accessibility.IUIAutomationDropTargetPattern_head
    IUIAutomationDropTargetPattern.get_CurrentDropTargetEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(3, 'get_CurrentDropTargetEffect', ((1, 'retVal'),)))
    IUIAutomationDropTargetPattern.get_CachedDropTargetEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'get_CachedDropTargetEffect', ((1, 'retVal'),)))
    IUIAutomationDropTargetPattern.get_CurrentDropTargetEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(5, 'get_CurrentDropTargetEffects', ((1, 'retVal'),)))
    IUIAutomationDropTargetPattern.get_CachedDropTargetEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(6, 'get_CachedDropTargetEffects', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationDropTargetPattern
def _define_IUIAutomationElement_head():
    class IUIAutomationElement(win32more.System.Com.IUnknown_head):
        Guid = Guid('d22108aa-8ac5-49a5-83-7b-37-bb-b3-d7-59-1e')
    return IUIAutomationElement
def _define_IUIAutomationElement():
    IUIAutomationElement = win32more.UI.Accessibility.IUIAutomationElement_head
    IUIAutomationElement.SetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'SetFocus', ()))
    IUIAutomationElement.GetRuntimeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(4, 'GetRuntimeId', ((1, 'runtimeId'),)))
    IUIAutomationElement.FindFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(5, 'FindFirst', ((1, 'scope'),(1, 'condition'),(1, 'found'),)))
    IUIAutomationElement.FindAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(6, 'FindAll', ((1, 'scope'),(1, 'condition'),(1, 'found'),)))
    IUIAutomationElement.FindFirstBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(7, 'FindFirstBuildCache', ((1, 'scope'),(1, 'condition'),(1, 'cacheRequest'),(1, 'found'),)))
    IUIAutomationElement.FindAllBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(8, 'FindAllBuildCache', ((1, 'scope'),(1, 'condition'),(1, 'cacheRequest'),(1, 'found'),)))
    IUIAutomationElement.BuildUpdatedCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(9, 'BuildUpdatedCache', ((1, 'cacheRequest'),(1, 'updatedElement'),)))
    IUIAutomationElement.GetCurrentPropertyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PROPERTY_ID,POINTER(win32more.System.Com.VARIANT_head))(10, 'GetCurrentPropertyValue', ((1, 'propertyId'),(1, 'retVal'),)))
    IUIAutomationElement.GetCurrentPropertyValueEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PROPERTY_ID,win32more.Foundation.BOOL,POINTER(win32more.System.Com.VARIANT_head))(11, 'GetCurrentPropertyValueEx', ((1, 'propertyId'),(1, 'ignoreDefaultValue'),(1, 'retVal'),)))
    IUIAutomationElement.GetCachedPropertyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PROPERTY_ID,POINTER(win32more.System.Com.VARIANT_head))(12, 'GetCachedPropertyValue', ((1, 'propertyId'),(1, 'retVal'),)))
    IUIAutomationElement.GetCachedPropertyValueEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PROPERTY_ID,win32more.Foundation.BOOL,POINTER(win32more.System.Com.VARIANT_head))(13, 'GetCachedPropertyValueEx', ((1, 'propertyId'),(1, 'ignoreDefaultValue'),(1, 'retVal'),)))
    IUIAutomationElement.GetCurrentPatternAs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PATTERN_ID,POINTER(Guid),POINTER(c_void_p))(14, 'GetCurrentPatternAs', ((1, 'patternId'),(1, 'riid'),(1, 'patternObject'),)))
    IUIAutomationElement.GetCachedPatternAs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PATTERN_ID,POINTER(Guid),POINTER(c_void_p))(15, 'GetCachedPatternAs', ((1, 'patternId'),(1, 'riid'),(1, 'patternObject'),)))
    IUIAutomationElement.GetCurrentPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PATTERN_ID,POINTER(win32more.System.Com.IUnknown_head))(16, 'GetCurrentPattern', ((1, 'patternId'),(1, 'patternObject'),)))
    IUIAutomationElement.GetCachedPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_PATTERN_ID,POINTER(win32more.System.Com.IUnknown_head))(17, 'GetCachedPattern', ((1, 'patternId'),(1, 'patternObject'),)))
    IUIAutomationElement.GetCachedParent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(18, 'GetCachedParent', ((1, 'parent'),)))
    IUIAutomationElement.GetCachedChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(19, 'GetCachedChildren', ((1, 'children'),)))
    IUIAutomationElement.get_CurrentProcessId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(20, 'get_CurrentProcessId', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentControlType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_CONTROLTYPE_ID))(21, 'get_CurrentControlType', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentLocalizedControlType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_CurrentLocalizedControlType', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(23, 'get_CurrentName', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentAcceleratorKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(24, 'get_CurrentAcceleratorKey', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentAccessKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(25, 'get_CurrentAccessKey', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentHasKeyboardFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(26, 'get_CurrentHasKeyboardFocus', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsKeyboardFocusable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(27, 'get_CurrentIsKeyboardFocusable', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(28, 'get_CurrentIsEnabled', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentAutomationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(29, 'get_CurrentAutomationId', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(30, 'get_CurrentClassName', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentHelpText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(31, 'get_CurrentHelpText', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentCulture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(32, 'get_CurrentCulture', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsControlElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(33, 'get_CurrentIsControlElement', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsContentElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(34, 'get_CurrentIsContentElement', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(35, 'get_CurrentIsPassword', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentNativeWindowHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND))(36, 'get_CurrentNativeWindowHandle', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentItemType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(37, 'get_CurrentItemType', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsOffscreen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(38, 'get_CurrentIsOffscreen', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.OrientationType))(39, 'get_CurrentOrientation', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentFrameworkId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(40, 'get_CurrentFrameworkId', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsRequiredForForm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(41, 'get_CurrentIsRequiredForForm', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentItemStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(42, 'get_CurrentItemStatus', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentBoundingRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(43, 'get_CurrentBoundingRectangle', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentLabeledBy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(44, 'get_CurrentLabeledBy', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentAriaRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(45, 'get_CurrentAriaRole', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentAriaProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(46, 'get_CurrentAriaProperties', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsDataValidForForm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(47, 'get_CurrentIsDataValidForForm', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentControllerFor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(48, 'get_CurrentControllerFor', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentDescribedBy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(49, 'get_CurrentDescribedBy', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentFlowsTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(50, 'get_CurrentFlowsTo', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentProviderDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(51, 'get_CurrentProviderDescription', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedProcessId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(52, 'get_CachedProcessId', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedControlType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_CONTROLTYPE_ID))(53, 'get_CachedControlType', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedLocalizedControlType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(54, 'get_CachedLocalizedControlType', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(55, 'get_CachedName', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedAcceleratorKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(56, 'get_CachedAcceleratorKey', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedAccessKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(57, 'get_CachedAccessKey', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedHasKeyboardFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(58, 'get_CachedHasKeyboardFocus', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsKeyboardFocusable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(59, 'get_CachedIsKeyboardFocusable', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(60, 'get_CachedIsEnabled', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedAutomationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(61, 'get_CachedAutomationId', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(62, 'get_CachedClassName', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedHelpText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(63, 'get_CachedHelpText', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedCulture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(64, 'get_CachedCulture', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsControlElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(65, 'get_CachedIsControlElement', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsContentElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(66, 'get_CachedIsContentElement', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(67, 'get_CachedIsPassword', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedNativeWindowHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND))(68, 'get_CachedNativeWindowHandle', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedItemType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(69, 'get_CachedItemType', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsOffscreen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(70, 'get_CachedIsOffscreen', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.OrientationType))(71, 'get_CachedOrientation', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedFrameworkId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(72, 'get_CachedFrameworkId', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsRequiredForForm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(73, 'get_CachedIsRequiredForForm', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedItemStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(74, 'get_CachedItemStatus', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedBoundingRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(75, 'get_CachedBoundingRectangle', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedLabeledBy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(76, 'get_CachedLabeledBy', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedAriaRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(77, 'get_CachedAriaRole', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedAriaProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(78, 'get_CachedAriaProperties', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsDataValidForForm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(79, 'get_CachedIsDataValidForForm', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedControllerFor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(80, 'get_CachedControllerFor', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedDescribedBy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(81, 'get_CachedDescribedBy', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedFlowsTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(82, 'get_CachedFlowsTo', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedProviderDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(83, 'get_CachedProviderDescription', ((1, 'retVal'),)))
    IUIAutomationElement.GetClickablePoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.POINT_head),POINTER(win32more.Foundation.BOOL))(84, 'GetClickablePoint', ((1, 'clickable'),(1, 'gotClickable'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationElement
def _define_IUIAutomationElement2_head():
    class IUIAutomationElement2(win32more.UI.Accessibility.IUIAutomationElement_head):
        Guid = Guid('6749c683-f70d-4487-a6-98-5f-79-d5-52-90-d6')
    return IUIAutomationElement2
def _define_IUIAutomationElement2():
    IUIAutomationElement2 = win32more.UI.Accessibility.IUIAutomationElement2_head
    IUIAutomationElement2.get_CurrentOptimizeForVisualContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(85, 'get_CurrentOptimizeForVisualContent', ((1, 'retVal'),)))
    IUIAutomationElement2.get_CachedOptimizeForVisualContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(86, 'get_CachedOptimizeForVisualContent', ((1, 'retVal'),)))
    IUIAutomationElement2.get_CurrentLiveSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.LiveSetting))(87, 'get_CurrentLiveSetting', ((1, 'retVal'),)))
    IUIAutomationElement2.get_CachedLiveSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.LiveSetting))(88, 'get_CachedLiveSetting', ((1, 'retVal'),)))
    IUIAutomationElement2.get_CurrentFlowsFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(89, 'get_CurrentFlowsFrom', ((1, 'retVal'),)))
    IUIAutomationElement2.get_CachedFlowsFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(90, 'get_CachedFlowsFrom', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement
    return IUIAutomationElement2
def _define_IUIAutomationElement3_head():
    class IUIAutomationElement3(win32more.UI.Accessibility.IUIAutomationElement2_head):
        Guid = Guid('8471df34-aee0-4a01-a7-de-7d-b9-af-12-c2-96')
    return IUIAutomationElement3
def _define_IUIAutomationElement3():
    IUIAutomationElement3 = win32more.UI.Accessibility.IUIAutomationElement3_head
    IUIAutomationElement3.ShowContextMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(91, 'ShowContextMenu', ()))
    IUIAutomationElement3.get_CurrentIsPeripheral = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(92, 'get_CurrentIsPeripheral', ((1, 'retVal'),)))
    IUIAutomationElement3.get_CachedIsPeripheral = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(93, 'get_CachedIsPeripheral', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement2
    return IUIAutomationElement3
def _define_IUIAutomationElement4_head():
    class IUIAutomationElement4(win32more.UI.Accessibility.IUIAutomationElement3_head):
        Guid = Guid('3b6e233c-52fb-4063-a4-c9-77-c0-75-c2-a0-6b')
    return IUIAutomationElement4
def _define_IUIAutomationElement4():
    IUIAutomationElement4 = win32more.UI.Accessibility.IUIAutomationElement4_head
    IUIAutomationElement4.get_CurrentPositionInSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(94, 'get_CurrentPositionInSet', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CurrentSizeOfSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(95, 'get_CurrentSizeOfSet', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CurrentLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(96, 'get_CurrentLevel', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CurrentAnnotationTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(97, 'get_CurrentAnnotationTypes', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CurrentAnnotationObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(98, 'get_CurrentAnnotationObjects', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CachedPositionInSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(99, 'get_CachedPositionInSet', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CachedSizeOfSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(100, 'get_CachedSizeOfSet', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CachedLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(101, 'get_CachedLevel', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CachedAnnotationTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(102, 'get_CachedAnnotationTypes', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CachedAnnotationObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(103, 'get_CachedAnnotationObjects', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement3
    return IUIAutomationElement4
def _define_IUIAutomationElement5_head():
    class IUIAutomationElement5(win32more.UI.Accessibility.IUIAutomationElement4_head):
        Guid = Guid('98141c1d-0d0e-4175-bb-e2-6b-ff-45-58-42-a7')
    return IUIAutomationElement5
def _define_IUIAutomationElement5():
    IUIAutomationElement5 = win32more.UI.Accessibility.IUIAutomationElement5_head
    IUIAutomationElement5.get_CurrentLandmarkType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_LANDMARKTYPE_ID))(104, 'get_CurrentLandmarkType', ((1, 'retVal'),)))
    IUIAutomationElement5.get_CurrentLocalizedLandmarkType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(105, 'get_CurrentLocalizedLandmarkType', ((1, 'retVal'),)))
    IUIAutomationElement5.get_CachedLandmarkType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_LANDMARKTYPE_ID))(106, 'get_CachedLandmarkType', ((1, 'retVal'),)))
    IUIAutomationElement5.get_CachedLocalizedLandmarkType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(107, 'get_CachedLocalizedLandmarkType', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement4
    return IUIAutomationElement5
def _define_IUIAutomationElement6_head():
    class IUIAutomationElement6(win32more.UI.Accessibility.IUIAutomationElement5_head):
        Guid = Guid('4780d450-8bca-4977-af-a5-a4-a5-17-f5-55-e3')
    return IUIAutomationElement6
def _define_IUIAutomationElement6():
    IUIAutomationElement6 = win32more.UI.Accessibility.IUIAutomationElement6_head
    IUIAutomationElement6.get_CurrentFullDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(108, 'get_CurrentFullDescription', ((1, 'retVal'),)))
    IUIAutomationElement6.get_CachedFullDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(109, 'get_CachedFullDescription', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement5
    return IUIAutomationElement6
def _define_IUIAutomationElement7_head():
    class IUIAutomationElement7(win32more.UI.Accessibility.IUIAutomationElement6_head):
        Guid = Guid('204e8572-cfc3-4c11-b0-c8-7d-a7-42-07-50-b7')
    return IUIAutomationElement7
def _define_IUIAutomationElement7():
    IUIAutomationElement7 = win32more.UI.Accessibility.IUIAutomationElement7_head
    IUIAutomationElement7.FindFirstWithOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.TreeTraversalOptions,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(110, 'FindFirstWithOptions', ((1, 'scope'),(1, 'condition'),(1, 'traversalOptions'),(1, 'root'),(1, 'found'),)))
    IUIAutomationElement7.FindAllWithOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.TreeTraversalOptions,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(111, 'FindAllWithOptions', ((1, 'scope'),(1, 'condition'),(1, 'traversalOptions'),(1, 'root'),(1, 'found'),)))
    IUIAutomationElement7.FindFirstWithOptionsBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.TreeTraversalOptions,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(112, 'FindFirstWithOptionsBuildCache', ((1, 'scope'),(1, 'condition'),(1, 'cacheRequest'),(1, 'traversalOptions'),(1, 'root'),(1, 'found'),)))
    IUIAutomationElement7.FindAllWithOptionsBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.TreeTraversalOptions,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(113, 'FindAllWithOptionsBuildCache', ((1, 'scope'),(1, 'condition'),(1, 'cacheRequest'),(1, 'traversalOptions'),(1, 'root'),(1, 'found'),)))
    IUIAutomationElement7.GetCurrentMetadataValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.UI.Accessibility.UIA_METADATA_ID,POINTER(win32more.System.Com.VARIANT_head))(114, 'GetCurrentMetadataValue', ((1, 'targetId'),(1, 'metadataId'),(1, 'returnVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement6
    return IUIAutomationElement7
def _define_IUIAutomationElement8_head():
    class IUIAutomationElement8(win32more.UI.Accessibility.IUIAutomationElement7_head):
        Guid = Guid('8c60217d-5411-4cde-bc-c0-1c-ed-a2-23-83-0c')
    return IUIAutomationElement8
def _define_IUIAutomationElement8():
    IUIAutomationElement8 = win32more.UI.Accessibility.IUIAutomationElement8_head
    IUIAutomationElement8.get_CurrentHeadingLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_HEADINGLEVEL_ID))(115, 'get_CurrentHeadingLevel', ((1, 'retVal'),)))
    IUIAutomationElement8.get_CachedHeadingLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_HEADINGLEVEL_ID))(116, 'get_CachedHeadingLevel', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement7
    return IUIAutomationElement8
def _define_IUIAutomationElement9_head():
    class IUIAutomationElement9(win32more.UI.Accessibility.IUIAutomationElement8_head):
        Guid = Guid('39325fac-039d-440e-a3-a3-5e-b8-1a-5c-ec-c3')
    return IUIAutomationElement9
def _define_IUIAutomationElement9():
    IUIAutomationElement9 = win32more.UI.Accessibility.IUIAutomationElement9_head
    IUIAutomationElement9.get_CurrentIsDialog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(117, 'get_CurrentIsDialog', ((1, 'retVal'),)))
    IUIAutomationElement9.get_CachedIsDialog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(118, 'get_CachedIsDialog', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement8
    return IUIAutomationElement9
def _define_IUIAutomationElementArray_head():
    class IUIAutomationElementArray(win32more.System.Com.IUnknown_head):
        Guid = Guid('14314595-b4bc-4055-95-f2-58-f2-e4-2c-98-55')
    return IUIAutomationElementArray
def _define_IUIAutomationElementArray():
    IUIAutomationElementArray = win32more.UI.Accessibility.IUIAutomationElementArray_head
    IUIAutomationElementArray.get_Length = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(3, 'get_Length', ((1, 'length'),)))
    IUIAutomationElementArray.GetElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(4, 'GetElement', ((1, 'index'),(1, 'element'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationElementArray
def _define_IUIAutomationEventHandler_head():
    class IUIAutomationEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('146c3c17-f12e-4e22-8c-27-f8-94-b9-b7-9c-69')
    return IUIAutomationEventHandler
def _define_IUIAutomationEventHandler():
    IUIAutomationEventHandler = win32more.UI.Accessibility.IUIAutomationEventHandler_head
    IUIAutomationEventHandler.HandleAutomationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.UIA_EVENT_ID)(3, 'HandleAutomationEvent', ((1, 'sender'),(1, 'eventId'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationEventHandler
def _define_IUIAutomationEventHandlerGroup_head():
    class IUIAutomationEventHandlerGroup(win32more.System.Com.IUnknown_head):
        Guid = Guid('c9ee12f2-c13b-4408-99-7c-63-99-14-37-7f-4e')
    return IUIAutomationEventHandlerGroup
def _define_IUIAutomationEventHandlerGroup():
    IUIAutomationEventHandlerGroup = win32more.UI.Accessibility.IUIAutomationEventHandlerGroup_head
    IUIAutomationEventHandlerGroup.AddActiveTextPositionChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler_head)(3, 'AddActiveTextPositionChangedEventHandler', ((1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomationEventHandlerGroup.AddAutomationEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_EVENT_ID,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationEventHandler_head)(4, 'AddAutomationEventHandler', ((1, 'eventId'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomationEventHandlerGroup.AddChangesEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,POINTER(Int32),Int32,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationChangesEventHandler_head)(5, 'AddChangesEventHandler', ((1, 'scope'),(1, 'changeTypes'),(1, 'changesCount'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomationEventHandlerGroup.AddNotificationEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationNotificationEventHandler_head)(6, 'AddNotificationEventHandler', ((1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomationEventHandlerGroup.AddPropertyChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head,POINTER(win32more.UI.Accessibility.UIA_PROPERTY_ID),Int32)(7, 'AddPropertyChangedEventHandler', ((1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),(1, 'propertyArray'),(1, 'propertyCount'),)))
    IUIAutomationEventHandlerGroup.AddStructureChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationStructureChangedEventHandler_head)(8, 'AddStructureChangedEventHandler', ((1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomationEventHandlerGroup.AddTextEditTextChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.TextEditChangeType,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler_head)(9, 'AddTextEditTextChangedEventHandler', ((1, 'scope'),(1, 'textEditChangeType'),(1, 'cacheRequest'),(1, 'handler'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationEventHandlerGroup
def _define_IUIAutomationExpandCollapsePattern_head():
    class IUIAutomationExpandCollapsePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('619be086-1f4e-4ee4-ba-fa-21-01-28-73-87-30')
    return IUIAutomationExpandCollapsePattern
def _define_IUIAutomationExpandCollapsePattern():
    IUIAutomationExpandCollapsePattern = win32more.UI.Accessibility.IUIAutomationExpandCollapsePattern_head
    IUIAutomationExpandCollapsePattern.Expand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Expand', ()))
    IUIAutomationExpandCollapsePattern.Collapse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Collapse', ()))
    IUIAutomationExpandCollapsePattern.get_CurrentExpandCollapseState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ExpandCollapseState))(5, 'get_CurrentExpandCollapseState', ((1, 'retVal'),)))
    IUIAutomationExpandCollapsePattern.get_CachedExpandCollapseState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ExpandCollapseState))(6, 'get_CachedExpandCollapseState', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationExpandCollapsePattern
def _define_IUIAutomationFocusChangedEventHandler_head():
    class IUIAutomationFocusChangedEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('c270f6b5-5c69-4290-97-45-7a-7f-97-16-94-68')
    return IUIAutomationFocusChangedEventHandler
def _define_IUIAutomationFocusChangedEventHandler():
    IUIAutomationFocusChangedEventHandler = win32more.UI.Accessibility.IUIAutomationFocusChangedEventHandler_head
    IUIAutomationFocusChangedEventHandler.HandleFocusChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head)(3, 'HandleFocusChangedEvent', ((1, 'sender'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationFocusChangedEventHandler
def _define_IUIAutomationGridItemPattern_head():
    class IUIAutomationGridItemPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('78f8ef57-66c3-4e09-bd-7c-e7-9b-20-04-89-4d')
    return IUIAutomationGridItemPattern
def _define_IUIAutomationGridItemPattern():
    IUIAutomationGridItemPattern = win32more.UI.Accessibility.IUIAutomationGridItemPattern_head
    IUIAutomationGridItemPattern.get_CurrentContainingGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(3, 'get_CurrentContainingGrid', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CurrentRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(4, 'get_CurrentRow', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CurrentColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(5, 'get_CurrentColumn', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CurrentRowSpan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(6, 'get_CurrentRowSpan', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CurrentColumnSpan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_CurrentColumnSpan', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CachedContainingGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(8, 'get_CachedContainingGrid', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CachedRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_CachedRow', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CachedColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_CachedColumn', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CachedRowSpan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_CachedRowSpan', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CachedColumnSpan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(12, 'get_CachedColumnSpan', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationGridItemPattern
def _define_IUIAutomationGridPattern_head():
    class IUIAutomationGridPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('414c3cdc-856b-4f5b-85-38-31-31-c6-30-25-50')
    return IUIAutomationGridPattern
def _define_IUIAutomationGridPattern():
    IUIAutomationGridPattern = win32more.UI.Accessibility.IUIAutomationGridPattern_head
    IUIAutomationGridPattern.GetItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(3, 'GetItem', ((1, 'row'),(1, 'column'),(1, 'element'),)))
    IUIAutomationGridPattern.get_CurrentRowCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(4, 'get_CurrentRowCount', ((1, 'retVal'),)))
    IUIAutomationGridPattern.get_CurrentColumnCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(5, 'get_CurrentColumnCount', ((1, 'retVal'),)))
    IUIAutomationGridPattern.get_CachedRowCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(6, 'get_CachedRowCount', ((1, 'retVal'),)))
    IUIAutomationGridPattern.get_CachedColumnCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_CachedColumnCount', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationGridPattern
def _define_IUIAutomationInvokePattern_head():
    class IUIAutomationInvokePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('fb377fbe-8ea6-46d5-9c-73-64-99-64-2d-30-59')
    return IUIAutomationInvokePattern
def _define_IUIAutomationInvokePattern():
    IUIAutomationInvokePattern = win32more.UI.Accessibility.IUIAutomationInvokePattern_head
    IUIAutomationInvokePattern.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Invoke', ()))
    win32more.System.Com.IUnknown
    return IUIAutomationInvokePattern
def _define_IUIAutomationItemContainerPattern_head():
    class IUIAutomationItemContainerPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('c690fdb2-27a8-423c-81-2d-42-97-73-c9-08-4e')
    return IUIAutomationItemContainerPattern
def _define_IUIAutomationItemContainerPattern():
    IUIAutomationItemContainerPattern = win32more.UI.Accessibility.IUIAutomationItemContainerPattern_head
    IUIAutomationItemContainerPattern.FindItemByProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.UIA_PROPERTY_ID,win32more.System.Com.VARIANT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(3, 'FindItemByProperty', ((1, 'pStartAfter'),(1, 'propertyId'),(1, 'value'),(1, 'pFound'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationItemContainerPattern
def _define_IUIAutomationLegacyIAccessiblePattern_head():
    class IUIAutomationLegacyIAccessiblePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('828055ad-355b-4435-86-d5-3b-51-c1-4a-9b-1b')
    return IUIAutomationLegacyIAccessiblePattern
def _define_IUIAutomationLegacyIAccessiblePattern():
    IUIAutomationLegacyIAccessiblePattern = win32more.UI.Accessibility.IUIAutomationLegacyIAccessiblePattern_head
    IUIAutomationLegacyIAccessiblePattern.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(3, 'Select', ((1, 'flagsSelect'),)))
    IUIAutomationLegacyIAccessiblePattern.DoDefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'DoDefaultAction', ()))
    IUIAutomationLegacyIAccessiblePattern.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(5, 'SetValue', ((1, 'szValue'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentChildId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(6, 'get_CurrentChildId', ((1, 'pRetVal'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_CurrentName', ((1, 'pszName'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_CurrentValue', ((1, 'pszValue'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_CurrentDescription', ((1, 'pszDescription'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(10, 'get_CurrentRole', ((1, 'pdwRole'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(11, 'get_CurrentState', ((1, 'pdwState'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentHelp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_CurrentHelp', ((1, 'pszHelp'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentKeyboardShortcut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'get_CurrentKeyboardShortcut', ((1, 'pszKeyboardShortcut'),)))
    IUIAutomationLegacyIAccessiblePattern.GetCurrentSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(14, 'GetCurrentSelection', ((1, 'pvarSelectedChildren'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentDefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_CurrentDefaultAction', ((1, 'pszDefaultAction'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedChildId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_CachedChildId', ((1, 'pRetVal'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(17, 'get_CachedName', ((1, 'pszName'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'get_CachedValue', ((1, 'pszValue'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(19, 'get_CachedDescription', ((1, 'pszDescription'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(20, 'get_CachedRole', ((1, 'pdwRole'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(21, 'get_CachedState', ((1, 'pdwState'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedHelp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(22, 'get_CachedHelp', ((1, 'pszHelp'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedKeyboardShortcut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(23, 'get_CachedKeyboardShortcut', ((1, 'pszKeyboardShortcut'),)))
    IUIAutomationLegacyIAccessiblePattern.GetCachedSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(24, 'GetCachedSelection', ((1, 'pvarSelectedChildren'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedDefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(25, 'get_CachedDefaultAction', ((1, 'pszDefaultAction'),)))
    IUIAutomationLegacyIAccessiblePattern.GetIAccessible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IAccessible_head))(26, 'GetIAccessible', ((1, 'ppAccessible'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationLegacyIAccessiblePattern
def _define_IUIAutomationMultipleViewPattern_head():
    class IUIAutomationMultipleViewPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('8d253c91-1dc5-4bb5-b1-8f-ad-e1-6f-a4-95-e8')
    return IUIAutomationMultipleViewPattern
def _define_IUIAutomationMultipleViewPattern():
    IUIAutomationMultipleViewPattern = win32more.UI.Accessibility.IUIAutomationMultipleViewPattern_head
    IUIAutomationMultipleViewPattern.GetViewName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR))(3, 'GetViewName', ((1, 'view'),(1, 'name'),)))
    IUIAutomationMultipleViewPattern.SetCurrentView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(4, 'SetCurrentView', ((1, 'view'),)))
    IUIAutomationMultipleViewPattern.get_CurrentCurrentView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(5, 'get_CurrentCurrentView', ((1, 'retVal'),)))
    IUIAutomationMultipleViewPattern.GetCurrentSupportedViews = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(6, 'GetCurrentSupportedViews', ((1, 'retVal'),)))
    IUIAutomationMultipleViewPattern.get_CachedCurrentView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_CachedCurrentView', ((1, 'retVal'),)))
    IUIAutomationMultipleViewPattern.GetCachedSupportedViews = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(8, 'GetCachedSupportedViews', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationMultipleViewPattern
def _define_IUIAutomationNotCondition_head():
    class IUIAutomationNotCondition(win32more.UI.Accessibility.IUIAutomationCondition_head):
        Guid = Guid('f528b657-847b-498c-88-96-d5-2b-56-54-07-a1')
    return IUIAutomationNotCondition
def _define_IUIAutomationNotCondition():
    IUIAutomationNotCondition = win32more.UI.Accessibility.IUIAutomationNotCondition_head
    IUIAutomationNotCondition.GetChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(3, 'GetChild', ((1, 'condition'),)))
    win32more.UI.Accessibility.IUIAutomationCondition
    return IUIAutomationNotCondition
def _define_IUIAutomationNotificationEventHandler_head():
    class IUIAutomationNotificationEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('c7cb2637-e6c2-4d0c-85-de-49-48-c0-21-75-c7')
    return IUIAutomationNotificationEventHandler
def _define_IUIAutomationNotificationEventHandler():
    IUIAutomationNotificationEventHandler = win32more.UI.Accessibility.IUIAutomationNotificationEventHandler_head
    IUIAutomationNotificationEventHandler.HandleNotificationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.NotificationKind,win32more.UI.Accessibility.NotificationProcessing,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(3, 'HandleNotificationEvent', ((1, 'sender'),(1, 'notificationKind'),(1, 'notificationProcessing'),(1, 'displayString'),(1, 'activityId'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationNotificationEventHandler
def _define_IUIAutomationObjectModelPattern_head():
    class IUIAutomationObjectModelPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('71c284b3-c14d-4d14-98-1e-19-75-1b-0d-75-6d')
    return IUIAutomationObjectModelPattern
def _define_IUIAutomationObjectModelPattern():
    IUIAutomationObjectModelPattern = win32more.UI.Accessibility.IUIAutomationObjectModelPattern_head
    IUIAutomationObjectModelPattern.GetUnderlyingObjectModel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(3, 'GetUnderlyingObjectModel', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationObjectModelPattern
def _define_IUIAutomationOrCondition_head():
    class IUIAutomationOrCondition(win32more.UI.Accessibility.IUIAutomationCondition_head):
        Guid = Guid('8753f032-3db1-47b5-a1-fc-6e-34-a2-66-c7-12')
    return IUIAutomationOrCondition
def _define_IUIAutomationOrCondition():
    IUIAutomationOrCondition = win32more.UI.Accessibility.IUIAutomationOrCondition_head
    IUIAutomationOrCondition.get_ChildCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(3, 'get_ChildCount', ((1, 'childCount'),)))
    IUIAutomationOrCondition.GetChildrenAsNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head)),POINTER(Int32))(4, 'GetChildrenAsNativeArray', ((1, 'childArray'),(1, 'childArrayCount'),)))
    IUIAutomationOrCondition.GetChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(5, 'GetChildren', ((1, 'childArray'),)))
    win32more.UI.Accessibility.IUIAutomationCondition
    return IUIAutomationOrCondition
def _define_IUIAutomationPatternHandler_head():
    class IUIAutomationPatternHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('d97022f3-a947-465e-8b-2a-ac-43-15-fa-54-e8')
    return IUIAutomationPatternHandler
def _define_IUIAutomationPatternHandler():
    IUIAutomationPatternHandler = win32more.UI.Accessibility.IUIAutomationPatternHandler_head
    IUIAutomationPatternHandler.CreateClientWrapper = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationPatternInstance_head,POINTER(win32more.System.Com.IUnknown_head))(3, 'CreateClientWrapper', ((1, 'pPatternInstance'),(1, 'pClientWrapper'),)))
    IUIAutomationPatternHandler.Dispatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(win32more.UI.Accessibility.UIAutomationParameter_head),UInt32)(4, 'Dispatch', ((1, 'pTarget'),(1, 'index'),(1, 'pParams'),(1, 'cParams'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationPatternHandler
def _define_IUIAutomationPatternInstance_head():
    class IUIAutomationPatternInstance(win32more.System.Com.IUnknown_head):
        Guid = Guid('c03a7fe4-9431-409f-be-d8-ae-7c-22-99-bc-8d')
    return IUIAutomationPatternInstance
def _define_IUIAutomationPatternInstance():
    IUIAutomationPatternInstance = win32more.UI.Accessibility.IUIAutomationPatternInstance_head
    IUIAutomationPatternInstance.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,win32more.UI.Accessibility.UIAutomationType,c_void_p)(3, 'GetProperty', ((1, 'index'),(1, 'cached'),(1, 'type'),(1, 'pPtr'),)))
    IUIAutomationPatternInstance.CallMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Accessibility.UIAutomationParameter_head),UInt32)(4, 'CallMethod', ((1, 'index'),(1, 'pParams'),(1, 'cParams'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationPatternInstance
def _define_IUIAutomationPropertyChangedEventHandler_head():
    class IUIAutomationPropertyChangedEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('40cd37d4-c756-4b0c-8c-6f-bd-df-ee-b1-3b-50')
    return IUIAutomationPropertyChangedEventHandler
def _define_IUIAutomationPropertyChangedEventHandler():
    IUIAutomationPropertyChangedEventHandler = win32more.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head
    IUIAutomationPropertyChangedEventHandler.HandlePropertyChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.UIA_PROPERTY_ID,win32more.System.Com.VARIANT)(3, 'HandlePropertyChangedEvent', ((1, 'sender'),(1, 'propertyId'),(1, 'newValue'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationPropertyChangedEventHandler
def _define_IUIAutomationPropertyCondition_head():
    class IUIAutomationPropertyCondition(win32more.UI.Accessibility.IUIAutomationCondition_head):
        Guid = Guid('99ebf2cb-5578-4267-9a-d4-af-d6-ea-77-e9-4b')
    return IUIAutomationPropertyCondition
def _define_IUIAutomationPropertyCondition():
    IUIAutomationPropertyCondition = win32more.UI.Accessibility.IUIAutomationPropertyCondition_head
    IUIAutomationPropertyCondition.get_PropertyId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_PROPERTY_ID))(3, 'get_PropertyId', ((1, 'propertyId'),)))
    IUIAutomationPropertyCondition.get_PropertyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(4, 'get_PropertyValue', ((1, 'propertyValue'),)))
    IUIAutomationPropertyCondition.get_PropertyConditionFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.PropertyConditionFlags))(5, 'get_PropertyConditionFlags', ((1, 'flags'),)))
    win32more.UI.Accessibility.IUIAutomationCondition
    return IUIAutomationPropertyCondition
def _define_IUIAutomationProxyFactory_head():
    class IUIAutomationProxyFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('85b94ecd-849d-42b6-b9-4d-d6-db-23-fd-f5-a4')
    return IUIAutomationProxyFactory
def _define_IUIAutomationProxyFactory():
    IUIAutomationProxyFactory = win32more.UI.Accessibility.IUIAutomationProxyFactory_head
    IUIAutomationProxyFactory.CreateProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,Int32,Int32,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head))(3, 'CreateProvider', ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'provider'),)))
    IUIAutomationProxyFactory.get_ProxyFactoryId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'get_ProxyFactoryId', ((1, 'factoryId'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationProxyFactory
def _define_IUIAutomationProxyFactoryEntry_head():
    class IUIAutomationProxyFactoryEntry(win32more.System.Com.IUnknown_head):
        Guid = Guid('d50e472e-b64b-490c-bc-a1-d3-06-96-f9-f2-89')
    return IUIAutomationProxyFactoryEntry
def _define_IUIAutomationProxyFactoryEntry():
    IUIAutomationProxyFactoryEntry = win32more.UI.Accessibility.IUIAutomationProxyFactoryEntry_head
    IUIAutomationProxyFactoryEntry.get_ProxyFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationProxyFactory_head))(3, 'get_ProxyFactory', ((1, 'factory'),)))
    IUIAutomationProxyFactoryEntry.get_ClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'get_ClassName', ((1, 'className'),)))
    IUIAutomationProxyFactoryEntry.get_ImageName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(5, 'get_ImageName', ((1, 'imageName'),)))
    IUIAutomationProxyFactoryEntry.get_AllowSubstringMatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(6, 'get_AllowSubstringMatch', ((1, 'allowSubstringMatch'),)))
    IUIAutomationProxyFactoryEntry.get_CanCheckBaseClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(7, 'get_CanCheckBaseClass', ((1, 'canCheckBaseClass'),)))
    IUIAutomationProxyFactoryEntry.get_NeedsAdviseEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(8, 'get_NeedsAdviseEvents', ((1, 'adviseEvents'),)))
    IUIAutomationProxyFactoryEntry.put_ClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(9, 'put_ClassName', ((1, 'className'),)))
    IUIAutomationProxyFactoryEntry.put_ImageName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(10, 'put_ImageName', ((1, 'imageName'),)))
    IUIAutomationProxyFactoryEntry.put_AllowSubstringMatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(11, 'put_AllowSubstringMatch', ((1, 'allowSubstringMatch'),)))
    IUIAutomationProxyFactoryEntry.put_CanCheckBaseClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(12, 'put_CanCheckBaseClass', ((1, 'canCheckBaseClass'),)))
    IUIAutomationProxyFactoryEntry.put_NeedsAdviseEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(13, 'put_NeedsAdviseEvents', ((1, 'adviseEvents'),)))
    IUIAutomationProxyFactoryEntry.SetWinEventsForAutomationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_EVENT_ID,win32more.UI.Accessibility.UIA_PROPERTY_ID,POINTER(win32more.System.Com.SAFEARRAY_head))(14, 'SetWinEventsForAutomationEvent', ((1, 'eventId'),(1, 'propertyId'),(1, 'winEvents'),)))
    IUIAutomationProxyFactoryEntry.GetWinEventsForAutomationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_EVENT_ID,win32more.UI.Accessibility.UIA_PROPERTY_ID,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(15, 'GetWinEventsForAutomationEvent', ((1, 'eventId'),(1, 'propertyId'),(1, 'winEvents'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationProxyFactoryEntry
def _define_IUIAutomationProxyFactoryMapping_head():
    class IUIAutomationProxyFactoryMapping(win32more.System.Com.IUnknown_head):
        Guid = Guid('09e31e18-872d-4873-93-d1-1e-54-1e-c1-33-fd')
    return IUIAutomationProxyFactoryMapping
def _define_IUIAutomationProxyFactoryMapping():
    IUIAutomationProxyFactoryMapping = win32more.UI.Accessibility.IUIAutomationProxyFactoryMapping_head
    IUIAutomationProxyFactoryMapping.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'get_Count', ((1, 'count'),)))
    IUIAutomationProxyFactoryMapping.GetTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(4, 'GetTable', ((1, 'table'),)))
    IUIAutomationProxyFactoryMapping.GetEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Accessibility.IUIAutomationProxyFactoryEntry_head))(5, 'GetEntry', ((1, 'index'),(1, 'entry'),)))
    IUIAutomationProxyFactoryMapping.SetTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(6, 'SetTable', ((1, 'factoryList'),)))
    IUIAutomationProxyFactoryMapping.InsertEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.SAFEARRAY_head))(7, 'InsertEntries', ((1, 'before'),(1, 'factoryList'),)))
    IUIAutomationProxyFactoryMapping.InsertEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.Accessibility.IUIAutomationProxyFactoryEntry_head)(8, 'InsertEntry', ((1, 'before'),(1, 'factory'),)))
    IUIAutomationProxyFactoryMapping.RemoveEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(9, 'RemoveEntry', ((1, 'index'),)))
    IUIAutomationProxyFactoryMapping.ClearTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'ClearTable', ()))
    IUIAutomationProxyFactoryMapping.RestoreDefaultTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'RestoreDefaultTable', ()))
    win32more.System.Com.IUnknown
    return IUIAutomationProxyFactoryMapping
def _define_IUIAutomationRangeValuePattern_head():
    class IUIAutomationRangeValuePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('59213f4f-7346-49e5-b1-20-80-55-59-87-a1-48')
    return IUIAutomationRangeValuePattern
def _define_IUIAutomationRangeValuePattern():
    IUIAutomationRangeValuePattern = win32more.UI.Accessibility.IUIAutomationRangeValuePattern_head
    IUIAutomationRangeValuePattern.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(3, 'SetValue', ((1, 'val'),)))
    IUIAutomationRangeValuePattern.get_CurrentValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(4, 'get_CurrentValue', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CurrentIsReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(5, 'get_CurrentIsReadOnly', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CurrentMaximum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(6, 'get_CurrentMaximum', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CurrentMinimum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(7, 'get_CurrentMinimum', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CurrentLargeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(8, 'get_CurrentLargeChange', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CurrentSmallChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(9, 'get_CurrentSmallChange', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CachedValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(10, 'get_CachedValue', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CachedIsReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(11, 'get_CachedIsReadOnly', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CachedMaximum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(12, 'get_CachedMaximum', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CachedMinimum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(13, 'get_CachedMinimum', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CachedLargeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(14, 'get_CachedLargeChange', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CachedSmallChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(15, 'get_CachedSmallChange', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationRangeValuePattern
def _define_IUIAutomationRegistrar_head():
    class IUIAutomationRegistrar(win32more.System.Com.IUnknown_head):
        Guid = Guid('8609c4ec-4a1a-4d88-a3-57-5a-66-e0-60-e1-cf')
    return IUIAutomationRegistrar
def _define_IUIAutomationRegistrar():
    IUIAutomationRegistrar = win32more.UI.Accessibility.IUIAutomationRegistrar_head
    IUIAutomationRegistrar.RegisterProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIAutomationPropertyInfo_head),POINTER(Int32))(3, 'RegisterProperty', ((1, 'property'),(1, 'propertyId'),)))
    IUIAutomationRegistrar.RegisterEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIAutomationEventInfo_head),POINTER(Int32))(4, 'RegisterEvent', ((1, 'event'),(1, 'eventId'),)))
    IUIAutomationRegistrar.RegisterPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIAutomationPatternInfo_head),POINTER(Int32),POINTER(Int32),UInt32,POINTER(Int32),UInt32,POINTER(Int32))(5, 'RegisterPattern', ((1, 'pattern'),(1, 'pPatternId'),(1, 'pPatternAvailablePropertyId'),(1, 'propertyIdCount'),(1, 'pPropertyIds'),(1, 'eventIdCount'),(1, 'pEventIds'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationRegistrar
def _define_IUIAutomationScrollItemPattern_head():
    class IUIAutomationScrollItemPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('b488300f-d015-4f19-9c-29-bb-59-5e-36-45-ef')
    return IUIAutomationScrollItemPattern
def _define_IUIAutomationScrollItemPattern():
    IUIAutomationScrollItemPattern = win32more.UI.Accessibility.IUIAutomationScrollItemPattern_head
    IUIAutomationScrollItemPattern.ScrollIntoView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'ScrollIntoView', ()))
    win32more.System.Com.IUnknown
    return IUIAutomationScrollItemPattern
def _define_IUIAutomationScrollPattern_head():
    class IUIAutomationScrollPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('88f4d42a-e881-459d-a7-7c-73-bb-bb-7e-02-dc')
    return IUIAutomationScrollPattern
def _define_IUIAutomationScrollPattern():
    IUIAutomationScrollPattern = win32more.UI.Accessibility.IUIAutomationScrollPattern_head
    IUIAutomationScrollPattern.Scroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.ScrollAmount,win32more.UI.Accessibility.ScrollAmount)(3, 'Scroll', ((1, 'horizontalAmount'),(1, 'verticalAmount'),)))
    IUIAutomationScrollPattern.SetScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double)(4, 'SetScrollPercent', ((1, 'horizontalPercent'),(1, 'verticalPercent'),)))
    IUIAutomationScrollPattern.get_CurrentHorizontalScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(5, 'get_CurrentHorizontalScrollPercent', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CurrentVerticalScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(6, 'get_CurrentVerticalScrollPercent', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CurrentHorizontalViewSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(7, 'get_CurrentHorizontalViewSize', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CurrentVerticalViewSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(8, 'get_CurrentVerticalViewSize', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CurrentHorizontallyScrollable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(9, 'get_CurrentHorizontallyScrollable', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CurrentVerticallyScrollable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(10, 'get_CurrentVerticallyScrollable', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CachedHorizontalScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(11, 'get_CachedHorizontalScrollPercent', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CachedVerticalScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(12, 'get_CachedVerticalScrollPercent', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CachedHorizontalViewSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(13, 'get_CachedHorizontalViewSize', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CachedVerticalViewSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(14, 'get_CachedVerticalViewSize', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CachedHorizontallyScrollable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(15, 'get_CachedHorizontallyScrollable', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CachedVerticallyScrollable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(16, 'get_CachedVerticallyScrollable', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationScrollPattern
def _define_IUIAutomationSelectionItemPattern_head():
    class IUIAutomationSelectionItemPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('a8efa66a-0fda-421a-91-94-38-02-1f-35-78-ea')
    return IUIAutomationSelectionItemPattern
def _define_IUIAutomationSelectionItemPattern():
    IUIAutomationSelectionItemPattern = win32more.UI.Accessibility.IUIAutomationSelectionItemPattern_head
    IUIAutomationSelectionItemPattern.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Select', ()))
    IUIAutomationSelectionItemPattern.AddToSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'AddToSelection', ()))
    IUIAutomationSelectionItemPattern.RemoveFromSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'RemoveFromSelection', ()))
    IUIAutomationSelectionItemPattern.get_CurrentIsSelected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(6, 'get_CurrentIsSelected', ((1, 'retVal'),)))
    IUIAutomationSelectionItemPattern.get_CurrentSelectionContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(7, 'get_CurrentSelectionContainer', ((1, 'retVal'),)))
    IUIAutomationSelectionItemPattern.get_CachedIsSelected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(8, 'get_CachedIsSelected', ((1, 'retVal'),)))
    IUIAutomationSelectionItemPattern.get_CachedSelectionContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(9, 'get_CachedSelectionContainer', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationSelectionItemPattern
def _define_IUIAutomationSelectionPattern_head():
    class IUIAutomationSelectionPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('5ed5202e-b2ac-47a6-b6-38-4b-0b-f1-40-d7-8e')
    return IUIAutomationSelectionPattern
def _define_IUIAutomationSelectionPattern():
    IUIAutomationSelectionPattern = win32more.UI.Accessibility.IUIAutomationSelectionPattern_head
    IUIAutomationSelectionPattern.GetCurrentSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(3, 'GetCurrentSelection', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern.get_CurrentCanSelectMultiple = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(4, 'get_CurrentCanSelectMultiple', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern.get_CurrentIsSelectionRequired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(5, 'get_CurrentIsSelectionRequired', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern.GetCachedSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(6, 'GetCachedSelection', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern.get_CachedCanSelectMultiple = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(7, 'get_CachedCanSelectMultiple', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern.get_CachedIsSelectionRequired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(8, 'get_CachedIsSelectionRequired', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationSelectionPattern
def _define_IUIAutomationSelectionPattern2_head():
    class IUIAutomationSelectionPattern2(win32more.UI.Accessibility.IUIAutomationSelectionPattern_head):
        Guid = Guid('0532bfae-c011-4e32-a3-43-6d-64-2d-79-85-55')
    return IUIAutomationSelectionPattern2
def _define_IUIAutomationSelectionPattern2():
    IUIAutomationSelectionPattern2 = win32more.UI.Accessibility.IUIAutomationSelectionPattern2_head
    IUIAutomationSelectionPattern2.get_CurrentFirstSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(9, 'get_CurrentFirstSelectedItem', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CurrentLastSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(10, 'get_CurrentLastSelectedItem', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CurrentCurrentSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(11, 'get_CurrentCurrentSelectedItem', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CurrentItemCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(12, 'get_CurrentItemCount', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CachedFirstSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(13, 'get_CachedFirstSelectedItem', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CachedLastSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(14, 'get_CachedLastSelectedItem', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CachedCurrentSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(15, 'get_CachedCurrentSelectedItem', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CachedItemCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_CachedItemCount', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationSelectionPattern
    return IUIAutomationSelectionPattern2
def _define_IUIAutomationSpreadsheetItemPattern_head():
    class IUIAutomationSpreadsheetItemPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('7d4fb86c-8d34-40e1-8e-83-62-c1-52-04-e3-35')
    return IUIAutomationSpreadsheetItemPattern
def _define_IUIAutomationSpreadsheetItemPattern():
    IUIAutomationSpreadsheetItemPattern = win32more.UI.Accessibility.IUIAutomationSpreadsheetItemPattern_head
    IUIAutomationSpreadsheetItemPattern.get_CurrentFormula = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(3, 'get_CurrentFormula', ((1, 'retVal'),)))
    IUIAutomationSpreadsheetItemPattern.GetCurrentAnnotationObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(4, 'GetCurrentAnnotationObjects', ((1, 'retVal'),)))
    IUIAutomationSpreadsheetItemPattern.GetCurrentAnnotationTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(5, 'GetCurrentAnnotationTypes', ((1, 'retVal'),)))
    IUIAutomationSpreadsheetItemPattern.get_CachedFormula = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(6, 'get_CachedFormula', ((1, 'retVal'),)))
    IUIAutomationSpreadsheetItemPattern.GetCachedAnnotationObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(7, 'GetCachedAnnotationObjects', ((1, 'retVal'),)))
    IUIAutomationSpreadsheetItemPattern.GetCachedAnnotationTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(8, 'GetCachedAnnotationTypes', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationSpreadsheetItemPattern
def _define_IUIAutomationSpreadsheetPattern_head():
    class IUIAutomationSpreadsheetPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('7517a7c8-faae-4de9-9f-08-29-b9-1e-85-95-c1')
    return IUIAutomationSpreadsheetPattern
def _define_IUIAutomationSpreadsheetPattern():
    IUIAutomationSpreadsheetPattern = win32more.UI.Accessibility.IUIAutomationSpreadsheetPattern_head
    IUIAutomationSpreadsheetPattern.GetItemByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(3, 'GetItemByName', ((1, 'name'),(1, 'element'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationSpreadsheetPattern
def _define_IUIAutomationStructureChangedEventHandler_head():
    class IUIAutomationStructureChangedEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('e81d1b4e-11c5-42f8-97-54-e7-03-6c-79-f0-54')
    return IUIAutomationStructureChangedEventHandler
def _define_IUIAutomationStructureChangedEventHandler():
    IUIAutomationStructureChangedEventHandler = win32more.UI.Accessibility.IUIAutomationStructureChangedEventHandler_head
    IUIAutomationStructureChangedEventHandler.HandleStructureChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.StructureChangeType,POINTER(win32more.System.Com.SAFEARRAY_head))(3, 'HandleStructureChangedEvent', ((1, 'sender'),(1, 'changeType'),(1, 'runtimeId'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationStructureChangedEventHandler
def _define_IUIAutomationStylesPattern_head():
    class IUIAutomationStylesPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('85b5f0a2-bd79-484a-ad-2b-38-8c-98-38-d5-fb')
    return IUIAutomationStylesPattern
def _define_IUIAutomationStylesPattern():
    IUIAutomationStylesPattern = win32more.UI.Accessibility.IUIAutomationStylesPattern_head
    IUIAutomationStylesPattern.get_CurrentStyleId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_STYLE_ID))(3, 'get_CurrentStyleId', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CurrentStyleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'get_CurrentStyleName', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CurrentFillColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(5, 'get_CurrentFillColor', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CurrentFillPatternStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(6, 'get_CurrentFillPatternStyle', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CurrentShape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_CurrentShape', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CurrentFillPatternColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_CurrentFillPatternColor', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CurrentExtendedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_CurrentExtendedProperties', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.GetCurrentExtendedPropertiesAsArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Accessibility.ExtendedProperty_head)),POINTER(Int32))(10, 'GetCurrentExtendedPropertiesAsArray', ((1, 'propertyArray'),(1, 'propertyCount'),)))
    IUIAutomationStylesPattern.get_CachedStyleId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_STYLE_ID))(11, 'get_CachedStyleId', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CachedStyleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'get_CachedStyleName', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CachedFillColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_CachedFillColor', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CachedFillPatternStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'get_CachedFillPatternStyle', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CachedShape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_CachedShape', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CachedFillPatternColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_CachedFillPatternColor', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CachedExtendedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(17, 'get_CachedExtendedProperties', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.GetCachedExtendedPropertiesAsArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Accessibility.ExtendedProperty_head)),POINTER(Int32))(18, 'GetCachedExtendedPropertiesAsArray', ((1, 'propertyArray'),(1, 'propertyCount'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationStylesPattern
def _define_IUIAutomationSynchronizedInputPattern_head():
    class IUIAutomationSynchronizedInputPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('2233be0b-afb7-448b-9f-da-3b-37-8a-a5-ea-e1')
    return IUIAutomationSynchronizedInputPattern
def _define_IUIAutomationSynchronizedInputPattern():
    IUIAutomationSynchronizedInputPattern = win32more.UI.Accessibility.IUIAutomationSynchronizedInputPattern_head
    IUIAutomationSynchronizedInputPattern.StartListening = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.SynchronizedInputType)(3, 'StartListening', ((1, 'inputType'),)))
    IUIAutomationSynchronizedInputPattern.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Cancel', ()))
    win32more.System.Com.IUnknown
    return IUIAutomationSynchronizedInputPattern
def _define_IUIAutomationTableItemPattern_head():
    class IUIAutomationTableItemPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('0b964eb3-ef2e-4464-9c-79-61-d6-17-37-a2-7e')
    return IUIAutomationTableItemPattern
def _define_IUIAutomationTableItemPattern():
    IUIAutomationTableItemPattern = win32more.UI.Accessibility.IUIAutomationTableItemPattern_head
    IUIAutomationTableItemPattern.GetCurrentRowHeaderItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(3, 'GetCurrentRowHeaderItems', ((1, 'retVal'),)))
    IUIAutomationTableItemPattern.GetCurrentColumnHeaderItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(4, 'GetCurrentColumnHeaderItems', ((1, 'retVal'),)))
    IUIAutomationTableItemPattern.GetCachedRowHeaderItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(5, 'GetCachedRowHeaderItems', ((1, 'retVal'),)))
    IUIAutomationTableItemPattern.GetCachedColumnHeaderItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(6, 'GetCachedColumnHeaderItems', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTableItemPattern
def _define_IUIAutomationTablePattern_head():
    class IUIAutomationTablePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('620e691c-ea96-4710-a8-50-75-4b-24-ce-24-17')
    return IUIAutomationTablePattern
def _define_IUIAutomationTablePattern():
    IUIAutomationTablePattern = win32more.UI.Accessibility.IUIAutomationTablePattern_head
    IUIAutomationTablePattern.GetCurrentRowHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(3, 'GetCurrentRowHeaders', ((1, 'retVal'),)))
    IUIAutomationTablePattern.GetCurrentColumnHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(4, 'GetCurrentColumnHeaders', ((1, 'retVal'),)))
    IUIAutomationTablePattern.get_CurrentRowOrColumnMajor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.RowOrColumnMajor))(5, 'get_CurrentRowOrColumnMajor', ((1, 'retVal'),)))
    IUIAutomationTablePattern.GetCachedRowHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(6, 'GetCachedRowHeaders', ((1, 'retVal'),)))
    IUIAutomationTablePattern.GetCachedColumnHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(7, 'GetCachedColumnHeaders', ((1, 'retVal'),)))
    IUIAutomationTablePattern.get_CachedRowOrColumnMajor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.RowOrColumnMajor))(8, 'get_CachedRowOrColumnMajor', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTablePattern
def _define_IUIAutomationTextChildPattern_head():
    class IUIAutomationTextChildPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('6552b038-ae05-40c8-ab-fd-aa-08-35-2a-ab-86')
    return IUIAutomationTextChildPattern
def _define_IUIAutomationTextChildPattern():
    IUIAutomationTextChildPattern = win32more.UI.Accessibility.IUIAutomationTextChildPattern_head
    IUIAutomationTextChildPattern.get_TextContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(3, 'get_TextContainer', ((1, 'container'),)))
    IUIAutomationTextChildPattern.get_TextRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head))(4, 'get_TextRange', ((1, 'range'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTextChildPattern
def _define_IUIAutomationTextEditPattern_head():
    class IUIAutomationTextEditPattern(win32more.UI.Accessibility.IUIAutomationTextPattern_head):
        Guid = Guid('17e21576-996c-4870-99-d9-bf-f3-23-38-0c-06')
    return IUIAutomationTextEditPattern
def _define_IUIAutomationTextEditPattern():
    IUIAutomationTextEditPattern = win32more.UI.Accessibility.IUIAutomationTextEditPattern_head
    IUIAutomationTextEditPattern.GetActiveComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head))(9, 'GetActiveComposition', ((1, 'range'),)))
    IUIAutomationTextEditPattern.GetConversionTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head))(10, 'GetConversionTarget', ((1, 'range'),)))
    win32more.UI.Accessibility.IUIAutomationTextPattern
    return IUIAutomationTextEditPattern
def _define_IUIAutomationTextEditTextChangedEventHandler_head():
    class IUIAutomationTextEditTextChangedEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('92faa680-e704-4156-93-1a-e3-2d-5b-b3-8f-3f')
    return IUIAutomationTextEditTextChangedEventHandler
def _define_IUIAutomationTextEditTextChangedEventHandler():
    IUIAutomationTextEditTextChangedEventHandler = win32more.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler_head
    IUIAutomationTextEditTextChangedEventHandler.HandleTextEditTextChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TextEditChangeType,POINTER(win32more.System.Com.SAFEARRAY_head))(3, 'HandleTextEditTextChangedEvent', ((1, 'sender'),(1, 'textEditChangeType'),(1, 'eventStrings'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTextEditTextChangedEventHandler
def _define_IUIAutomationTextPattern_head():
    class IUIAutomationTextPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('32eba289-3583-42c9-9c-59-3b-6d-9a-1e-9b-6a')
    return IUIAutomationTextPattern
def _define_IUIAutomationTextPattern():
    IUIAutomationTextPattern = win32more.UI.Accessibility.IUIAutomationTextPattern_head
    IUIAutomationTextPattern.RangeFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head))(3, 'RangeFromPoint', ((1, 'pt'),(1, 'range'),)))
    IUIAutomationTextPattern.RangeFromChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head))(4, 'RangeFromChild', ((1, 'child'),(1, 'range'),)))
    IUIAutomationTextPattern.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRangeArray_head))(5, 'GetSelection', ((1, 'ranges'),)))
    IUIAutomationTextPattern.GetVisibleRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRangeArray_head))(6, 'GetVisibleRanges', ((1, 'ranges'),)))
    IUIAutomationTextPattern.get_DocumentRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head))(7, 'get_DocumentRange', ((1, 'range'),)))
    IUIAutomationTextPattern.get_SupportedTextSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.SupportedTextSelection))(8, 'get_SupportedTextSelection', ((1, 'supportedTextSelection'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTextPattern
def _define_IUIAutomationTextPattern2_head():
    class IUIAutomationTextPattern2(win32more.UI.Accessibility.IUIAutomationTextPattern_head):
        Guid = Guid('506a921a-fcc9-409f-b2-3b-37-eb-74-10-68-72')
    return IUIAutomationTextPattern2
def _define_IUIAutomationTextPattern2():
    IUIAutomationTextPattern2 = win32more.UI.Accessibility.IUIAutomationTextPattern2_head
    IUIAutomationTextPattern2.RangeFromAnnotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head))(9, 'RangeFromAnnotation', ((1, 'annotation'),(1, 'range'),)))
    IUIAutomationTextPattern2.GetCaretRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head))(10, 'GetCaretRange', ((1, 'isActive'),(1, 'range'),)))
    win32more.UI.Accessibility.IUIAutomationTextPattern
    return IUIAutomationTextPattern2
def _define_IUIAutomationTextRange_head():
    class IUIAutomationTextRange(win32more.System.Com.IUnknown_head):
        Guid = Guid('a543cc6a-f4ae-494b-82-39-c8-14-48-11-87-a8')
    return IUIAutomationTextRange
def _define_IUIAutomationTextRange():
    IUIAutomationTextRange = win32more.UI.Accessibility.IUIAutomationTextRange_head
    IUIAutomationTextRange.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head))(3, 'Clone', ((1, 'clonedRange'),)))
    IUIAutomationTextRange.Compare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationTextRange_head,POINTER(win32more.Foundation.BOOL))(4, 'Compare', ((1, 'range'),(1, 'areSame'),)))
    IUIAutomationTextRange.CompareEndpoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.IUIAutomationTextRange_head,win32more.UI.Accessibility.TextPatternRangeEndpoint,POINTER(Int32))(5, 'CompareEndpoints', ((1, 'srcEndPoint'),(1, 'range'),(1, 'targetEndPoint'),(1, 'compValue'),)))
    IUIAutomationTextRange.ExpandToEnclosingUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextUnit)(6, 'ExpandToEnclosingUnit', ((1, 'textUnit'),)))
    IUIAutomationTextRange.FindAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_TEXTATTRIBUTE_ID,win32more.System.Com.VARIANT,win32more.Foundation.BOOL,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head))(7, 'FindAttribute', ((1, 'attr'),(1, 'val'),(1, 'backward'),(1, 'found'),)))
    IUIAutomationTextRange.FindText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head))(8, 'FindText', ((1, 'text'),(1, 'backward'),(1, 'ignoreCase'),(1, 'found'),)))
    IUIAutomationTextRange.GetAttributeValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UIA_TEXTATTRIBUTE_ID,POINTER(win32more.System.Com.VARIANT_head))(9, 'GetAttributeValue', ((1, 'attr'),(1, 'value'),)))
    IUIAutomationTextRange.GetBoundingRectangles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(10, 'GetBoundingRectangles', ((1, 'boundingRects'),)))
    IUIAutomationTextRange.GetEnclosingElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(11, 'GetEnclosingElement', ((1, 'enclosingElement'),)))
    IUIAutomationTextRange.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR))(12, 'GetText', ((1, 'maxLength'),(1, 'text'),)))
    IUIAutomationTextRange.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextUnit,Int32,POINTER(Int32))(13, 'Move', ((1, 'unit'),(1, 'count'),(1, 'moved'),)))
    IUIAutomationTextRange.MoveEndpointByUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.TextUnit,Int32,POINTER(Int32))(14, 'MoveEndpointByUnit', ((1, 'endpoint'),(1, 'unit'),(1, 'count'),(1, 'moved'),)))
    IUIAutomationTextRange.MoveEndpointByRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.IUIAutomationTextRange_head,win32more.UI.Accessibility.TextPatternRangeEndpoint)(15, 'MoveEndpointByRange', ((1, 'srcEndPoint'),(1, 'range'),(1, 'targetEndPoint'),)))
    IUIAutomationTextRange.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'Select', ()))
    IUIAutomationTextRange.AddToSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(17, 'AddToSelection', ()))
    IUIAutomationTextRange.RemoveFromSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(18, 'RemoveFromSelection', ()))
    IUIAutomationTextRange.ScrollIntoView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(19, 'ScrollIntoView', ((1, 'alignToTop'),)))
    IUIAutomationTextRange.GetChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(20, 'GetChildren', ((1, 'children'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTextRange
def _define_IUIAutomationTextRange2_head():
    class IUIAutomationTextRange2(win32more.UI.Accessibility.IUIAutomationTextRange_head):
        Guid = Guid('bb9b40e0-5e04-46bd-9b-e0-4b-60-1b-9a-fa-d4')
    return IUIAutomationTextRange2
def _define_IUIAutomationTextRange2():
    IUIAutomationTextRange2 = win32more.UI.Accessibility.IUIAutomationTextRange2_head
    IUIAutomationTextRange2.ShowContextMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(21, 'ShowContextMenu', ()))
    win32more.UI.Accessibility.IUIAutomationTextRange
    return IUIAutomationTextRange2
def _define_IUIAutomationTextRange3_head():
    class IUIAutomationTextRange3(win32more.UI.Accessibility.IUIAutomationTextRange2_head):
        Guid = Guid('6a315d69-5512-4c2e-85-f0-53-fc-e6-dd-4b-c2')
    return IUIAutomationTextRange3
def _define_IUIAutomationTextRange3():
    IUIAutomationTextRange3 = win32more.UI.Accessibility.IUIAutomationTextRange3_head
    IUIAutomationTextRange3.GetEnclosingElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(22, 'GetEnclosingElementBuildCache', ((1, 'cacheRequest'),(1, 'enclosingElement'),)))
    IUIAutomationTextRange3.GetChildrenBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head))(23, 'GetChildrenBuildCache', ((1, 'cacheRequest'),(1, 'children'),)))
    IUIAutomationTextRange3.GetAttributeValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIA_TEXTATTRIBUTE_ID),Int32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)))(24, 'GetAttributeValues', ((1, 'attributeIds'),(1, 'attributeIdCount'),(1, 'attributeValues'),)))
    win32more.UI.Accessibility.IUIAutomationTextRange2
    return IUIAutomationTextRange3
def _define_IUIAutomationTextRangeArray_head():
    class IUIAutomationTextRangeArray(win32more.System.Com.IUnknown_head):
        Guid = Guid('ce4ae76a-e717-4c98-81-ea-47-37-1d-02-8e-b6')
    return IUIAutomationTextRangeArray
def _define_IUIAutomationTextRangeArray():
    IUIAutomationTextRangeArray = win32more.UI.Accessibility.IUIAutomationTextRangeArray_head
    IUIAutomationTextRangeArray.get_Length = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(3, 'get_Length', ((1, 'length'),)))
    IUIAutomationTextRangeArray.GetElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head))(4, 'GetElement', ((1, 'index'),(1, 'element'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTextRangeArray
def _define_IUIAutomationTogglePattern_head():
    class IUIAutomationTogglePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('94cf8058-9b8d-4ab9-8b-fd-4c-d0-a3-3c-8c-70')
    return IUIAutomationTogglePattern
def _define_IUIAutomationTogglePattern():
    IUIAutomationTogglePattern = win32more.UI.Accessibility.IUIAutomationTogglePattern_head
    IUIAutomationTogglePattern.Toggle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Toggle', ()))
    IUIAutomationTogglePattern.get_CurrentToggleState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ToggleState))(4, 'get_CurrentToggleState', ((1, 'retVal'),)))
    IUIAutomationTogglePattern.get_CachedToggleState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ToggleState))(5, 'get_CachedToggleState', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTogglePattern
def _define_IUIAutomationTransformPattern_head():
    class IUIAutomationTransformPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('a9b55844-a55d-4ef0-92-6d-56-9c-16-ff-89-bb')
    return IUIAutomationTransformPattern
def _define_IUIAutomationTransformPattern():
    IUIAutomationTransformPattern = win32more.UI.Accessibility.IUIAutomationTransformPattern_head
    IUIAutomationTransformPattern.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double)(3, 'Move', ((1, 'x'),(1, 'y'),)))
    IUIAutomationTransformPattern.Resize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double)(4, 'Resize', ((1, 'width'),(1, 'height'),)))
    IUIAutomationTransformPattern.Rotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(5, 'Rotate', ((1, 'degrees'),)))
    IUIAutomationTransformPattern.get_CurrentCanMove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(6, 'get_CurrentCanMove', ((1, 'retVal'),)))
    IUIAutomationTransformPattern.get_CurrentCanResize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(7, 'get_CurrentCanResize', ((1, 'retVal'),)))
    IUIAutomationTransformPattern.get_CurrentCanRotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(8, 'get_CurrentCanRotate', ((1, 'retVal'),)))
    IUIAutomationTransformPattern.get_CachedCanMove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(9, 'get_CachedCanMove', ((1, 'retVal'),)))
    IUIAutomationTransformPattern.get_CachedCanResize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(10, 'get_CachedCanResize', ((1, 'retVal'),)))
    IUIAutomationTransformPattern.get_CachedCanRotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(11, 'get_CachedCanRotate', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTransformPattern
def _define_IUIAutomationTransformPattern2_head():
    class IUIAutomationTransformPattern2(win32more.UI.Accessibility.IUIAutomationTransformPattern_head):
        Guid = Guid('6d74d017-6ecb-4381-b3-8b-3c-17-a4-8f-f1-c2')
    return IUIAutomationTransformPattern2
def _define_IUIAutomationTransformPattern2():
    IUIAutomationTransformPattern2 = win32more.UI.Accessibility.IUIAutomationTransformPattern2_head
    IUIAutomationTransformPattern2.Zoom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double)(12, 'Zoom', ((1, 'zoomValue'),)))
    IUIAutomationTransformPattern2.ZoomByUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.ZoomUnit)(13, 'ZoomByUnit', ((1, 'zoomUnit'),)))
    IUIAutomationTransformPattern2.get_CurrentCanZoom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(14, 'get_CurrentCanZoom', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CachedCanZoom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(15, 'get_CachedCanZoom', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CurrentZoomLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(16, 'get_CurrentZoomLevel', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CachedZoomLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(17, 'get_CachedZoomLevel', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CurrentZoomMinimum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(18, 'get_CurrentZoomMinimum', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CachedZoomMinimum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(19, 'get_CachedZoomMinimum', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CurrentZoomMaximum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(20, 'get_CurrentZoomMaximum', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CachedZoomMaximum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double))(21, 'get_CachedZoomMaximum', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationTransformPattern
    return IUIAutomationTransformPattern2
def _define_IUIAutomationTreeWalker_head():
    class IUIAutomationTreeWalker(win32more.System.Com.IUnknown_head):
        Guid = Guid('4042c624-389c-4afc-a6-30-9d-f8-54-a5-41-fc')
    return IUIAutomationTreeWalker
def _define_IUIAutomationTreeWalker():
    IUIAutomationTreeWalker = win32more.UI.Accessibility.IUIAutomationTreeWalker_head
    IUIAutomationTreeWalker.GetParentElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(3, 'GetParentElement', ((1, 'element'),(1, 'parent'),)))
    IUIAutomationTreeWalker.GetFirstChildElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(4, 'GetFirstChildElement', ((1, 'element'),(1, 'first'),)))
    IUIAutomationTreeWalker.GetLastChildElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(5, 'GetLastChildElement', ((1, 'element'),(1, 'last'),)))
    IUIAutomationTreeWalker.GetNextSiblingElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(6, 'GetNextSiblingElement', ((1, 'element'),(1, 'next'),)))
    IUIAutomationTreeWalker.GetPreviousSiblingElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(7, 'GetPreviousSiblingElement', ((1, 'element'),(1, 'previous'),)))
    IUIAutomationTreeWalker.NormalizeElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(8, 'NormalizeElement', ((1, 'element'),(1, 'normalized'),)))
    IUIAutomationTreeWalker.GetParentElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(9, 'GetParentElementBuildCache', ((1, 'element'),(1, 'cacheRequest'),(1, 'parent'),)))
    IUIAutomationTreeWalker.GetFirstChildElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(10, 'GetFirstChildElementBuildCache', ((1, 'element'),(1, 'cacheRequest'),(1, 'first'),)))
    IUIAutomationTreeWalker.GetLastChildElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(11, 'GetLastChildElementBuildCache', ((1, 'element'),(1, 'cacheRequest'),(1, 'last'),)))
    IUIAutomationTreeWalker.GetNextSiblingElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(12, 'GetNextSiblingElementBuildCache', ((1, 'element'),(1, 'cacheRequest'),(1, 'next'),)))
    IUIAutomationTreeWalker.GetPreviousSiblingElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(13, 'GetPreviousSiblingElementBuildCache', ((1, 'element'),(1, 'cacheRequest'),(1, 'previous'),)))
    IUIAutomationTreeWalker.NormalizeElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head))(14, 'NormalizeElementBuildCache', ((1, 'element'),(1, 'cacheRequest'),(1, 'normalized'),)))
    IUIAutomationTreeWalker.get_Condition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head))(15, 'get_Condition', ((1, 'condition'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTreeWalker
def _define_IUIAutomationValuePattern_head():
    class IUIAutomationValuePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('a94cd8b1-0844-4cd6-9d-2d-64-05-37-ab-39-e9')
    return IUIAutomationValuePattern
def _define_IUIAutomationValuePattern():
    IUIAutomationValuePattern = win32more.UI.Accessibility.IUIAutomationValuePattern_head
    IUIAutomationValuePattern.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(3, 'SetValue', ((1, 'val'),)))
    IUIAutomationValuePattern.get_CurrentValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'get_CurrentValue', ((1, 'retVal'),)))
    IUIAutomationValuePattern.get_CurrentIsReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(5, 'get_CurrentIsReadOnly', ((1, 'retVal'),)))
    IUIAutomationValuePattern.get_CachedValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(6, 'get_CachedValue', ((1, 'retVal'),)))
    IUIAutomationValuePattern.get_CachedIsReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(7, 'get_CachedIsReadOnly', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationValuePattern
def _define_IUIAutomationVirtualizedItemPattern_head():
    class IUIAutomationVirtualizedItemPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('6ba3d7a6-04cf-4f11-87-93-a8-d1-cd-e9-96-9f')
    return IUIAutomationVirtualizedItemPattern
def _define_IUIAutomationVirtualizedItemPattern():
    IUIAutomationVirtualizedItemPattern = win32more.UI.Accessibility.IUIAutomationVirtualizedItemPattern_head
    IUIAutomationVirtualizedItemPattern.Realize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Realize', ()))
    win32more.System.Com.IUnknown
    return IUIAutomationVirtualizedItemPattern
def _define_IUIAutomationWindowPattern_head():
    class IUIAutomationWindowPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('0faef453-9208-43ef-bb-b2-3b-48-51-77-86-4f')
    return IUIAutomationWindowPattern
def _define_IUIAutomationWindowPattern():
    IUIAutomationWindowPattern = win32more.UI.Accessibility.IUIAutomationWindowPattern_head
    IUIAutomationWindowPattern.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Close', ()))
    IUIAutomationWindowPattern.WaitForInputIdle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BOOL))(4, 'WaitForInputIdle', ((1, 'milliseconds'),(1, 'success'),)))
    IUIAutomationWindowPattern.SetWindowVisualState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.WindowVisualState)(5, 'SetWindowVisualState', ((1, 'state'),)))
    IUIAutomationWindowPattern.get_CurrentCanMaximize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(6, 'get_CurrentCanMaximize', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CurrentCanMinimize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(7, 'get_CurrentCanMinimize', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CurrentIsModal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(8, 'get_CurrentIsModal', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CurrentIsTopmost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(9, 'get_CurrentIsTopmost', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CurrentWindowVisualState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.WindowVisualState))(10, 'get_CurrentWindowVisualState', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CurrentWindowInteractionState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.WindowInteractionState))(11, 'get_CurrentWindowInteractionState', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CachedCanMaximize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(12, 'get_CachedCanMaximize', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CachedCanMinimize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(13, 'get_CachedCanMinimize', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CachedIsModal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(14, 'get_CachedIsModal', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CachedIsTopmost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(15, 'get_CachedIsTopmost', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CachedWindowVisualState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.WindowVisualState))(16, 'get_CachedWindowVisualState', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CachedWindowInteractionState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.WindowInteractionState))(17, 'get_CachedWindowInteractionState', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationWindowPattern
def _define_IValueProvider_head():
    class IValueProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('c7935180-6fb3-4201-b1-74-7d-f7-3a-db-f6-4a')
    return IValueProvider
def _define_IValueProvider():
    IValueProvider = win32more.UI.Accessibility.IValueProvider_head
    IValueProvider.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(3, 'SetValue', ((1, 'val'),)))
    IValueProvider.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'get_Value', ((1, 'pRetVal'),)))
    IValueProvider.get_IsReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(5, 'get_IsReadOnly', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IValueProvider
def _define_IVirtualizedItemProvider_head():
    class IVirtualizedItemProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('cb98b665-2d35-4fac-ad-35-f3-c6-0d-0c-0b-8b')
    return IVirtualizedItemProvider
def _define_IVirtualizedItemProvider():
    IVirtualizedItemProvider = win32more.UI.Accessibility.IVirtualizedItemProvider_head
    IVirtualizedItemProvider.Realize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Realize', ()))
    win32more.System.Com.IUnknown
    return IVirtualizedItemProvider
def _define_IWindowProvider_head():
    class IWindowProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('987df77b-db06-4d77-8f-8a-86-a9-c3-bb-90-b9')
    return IWindowProvider
def _define_IWindowProvider():
    IWindowProvider = win32more.UI.Accessibility.IWindowProvider_head
    IWindowProvider.SetVisualState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.WindowVisualState)(3, 'SetVisualState', ((1, 'state'),)))
    IWindowProvider.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Close', ()))
    IWindowProvider.WaitForInputIdle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BOOL))(5, 'WaitForInputIdle', ((1, 'milliseconds'),(1, 'pRetVal'),)))
    IWindowProvider.get_CanMaximize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(6, 'get_CanMaximize', ((1, 'pRetVal'),)))
    IWindowProvider.get_CanMinimize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(7, 'get_CanMinimize', ((1, 'pRetVal'),)))
    IWindowProvider.get_IsModal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(8, 'get_IsModal', ((1, 'pRetVal'),)))
    IWindowProvider.get_WindowVisualState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.WindowVisualState))(9, 'get_WindowVisualState', ((1, 'pRetVal'),)))
    IWindowProvider.get_WindowInteractionState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.WindowInteractionState))(10, 'get_WindowInteractionState', ((1, 'pRetVal'),)))
    IWindowProvider.get_IsTopmost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(11, 'get_IsTopmost', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IWindowProvider
LiveSetting = Int32
LiveSetting_Off = 0
LiveSetting_Polite = 1
LiveSetting_Assertive = 2
def _define_LPFNACCESSIBLECHILDREN():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessible_head,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32))
def _define_LPFNACCESSIBLEOBJECTFROMPOINT():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,POINTER(win32more.UI.Accessibility.IAccessible_head),POINTER(win32more.System.Com.VARIANT_head))
def _define_LPFNACCESSIBLEOBJECTFROMWINDOW():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,POINTER(Guid),POINTER(c_void_p))
def _define_LPFNCREATESTDACCESSIBLEOBJECT():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,Int32,POINTER(Guid),POINTER(c_void_p))
def _define_LPFNLRESULTFROMOBJECT():
    return WINFUNCTYPE(win32more.Foundation.LRESULT,POINTER(Guid),win32more.Foundation.WPARAM,win32more.System.Com.IUnknown_head)
def _define_LPFNOBJECTFROMLRESULT():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LRESULT,POINTER(Guid),win32more.Foundation.WPARAM,POINTER(c_void_p))
def _define_MOUSEKEYS_head():
    class MOUSEKEYS(Structure):
        pass
    return MOUSEKEYS
def _define_MOUSEKEYS():
    MOUSEKEYS = win32more.UI.Accessibility.MOUSEKEYS_head
    MOUSEKEYS._fields_ = [
        ('cbSize', UInt32),
        ('dwFlags', UInt32),
        ('iMaxSpeed', UInt32),
        ('iTimeToMaxSpeed', UInt32),
        ('iCtrlSpeed', UInt32),
        ('dwReserved1', UInt32),
        ('dwReserved2', UInt32),
    ]
    return MOUSEKEYS
def _define_MSAAMENUINFO_head():
    class MSAAMENUINFO(Structure):
        pass
    return MSAAMENUINFO
def _define_MSAAMENUINFO():
    MSAAMENUINFO = win32more.UI.Accessibility.MSAAMENUINFO_head
    MSAAMENUINFO._fields_ = [
        ('dwMSAASignature', UInt32),
        ('cchWText', UInt32),
        ('pszWText', win32more.Foundation.PWSTR),
    ]
    return MSAAMENUINFO
NavigateDirection = Int32
NavigateDirection_Parent = 0
NavigateDirection_NextSibling = 1
NavigateDirection_PreviousSibling = 2
NavigateDirection_FirstChild = 3
NavigateDirection_LastChild = 4
NormalizeState = Int32
NormalizeState_None = 0
NormalizeState_View = 1
NormalizeState_Custom = 2
NotificationKind = Int32
NotificationKind_ItemAdded = 0
NotificationKind_ItemRemoved = 1
NotificationKind_ActionCompleted = 2
NotificationKind_ActionAborted = 3
NotificationKind_Other = 4
NotificationProcessing = Int32
NotificationProcessing_ImportantAll = 0
NotificationProcessing_ImportantMostRecent = 1
NotificationProcessing_All = 2
NotificationProcessing_MostRecent = 3
NotificationProcessing_CurrentThenMostRecent = 4
OrientationType = Int32
OrientationType_None = 0
OrientationType_Horizontal = 1
OrientationType_Vertical = 2
OutlineStyles = Int32
OutlineStyles_None = 0
OutlineStyles_Outline = 1
OutlineStyles_Shadow = 2
OutlineStyles_Engraved = 4
OutlineStyles_Embossed = 8
PropertyConditionFlags = Int32
PropertyConditionFlags_None = 0
PropertyConditionFlags_IgnoreCase = 1
PropertyConditionFlags_MatchSubstring = 2
ProviderOptions = Int32
ProviderOptions_ClientSideProvider = 1
ProviderOptions_ServerSideProvider = 2
ProviderOptions_NonClientAreaProvider = 4
ProviderOptions_OverrideProvider = 8
ProviderOptions_ProviderOwnsSetFocus = 16
ProviderOptions_UseComThreading = 32
ProviderOptions_RefuseNonClientSupport = 64
ProviderOptions_HasNativeIAccessible = 128
ProviderOptions_UseClientCoordinates = 256
ProviderType = Int32
ProviderType_BaseHwnd = 0
ProviderType_Proxy = 1
ProviderType_NonClientArea = 2
RowOrColumnMajor = Int32
RowOrColumnMajor_RowMajor = 0
RowOrColumnMajor_ColumnMajor = 1
RowOrColumnMajor_Indeterminate = 2
SayAsInterpretAs = Int32
SayAsInterpretAs_None = 0
SayAsInterpretAs_Spell = 1
SayAsInterpretAs_Cardinal = 2
SayAsInterpretAs_Ordinal = 3
SayAsInterpretAs_Number = 4
SayAsInterpretAs_Date = 5
SayAsInterpretAs_Time = 6
SayAsInterpretAs_Telephone = 7
SayAsInterpretAs_Currency = 8
SayAsInterpretAs_Net = 9
SayAsInterpretAs_Url = 10
SayAsInterpretAs_Address = 11
SayAsInterpretAs_Alphanumeric = 12
SayAsInterpretAs_Name = 13
SayAsInterpretAs_Media = 14
SayAsInterpretAs_Date_MonthDayYear = 15
SayAsInterpretAs_Date_DayMonthYear = 16
SayAsInterpretAs_Date_YearMonthDay = 17
SayAsInterpretAs_Date_YearMonth = 18
SayAsInterpretAs_Date_MonthYear = 19
SayAsInterpretAs_Date_DayMonth = 20
SayAsInterpretAs_Date_MonthDay = 21
SayAsInterpretAs_Date_Year = 22
SayAsInterpretAs_Time_HoursMinutesSeconds12 = 23
SayAsInterpretAs_Time_HoursMinutes12 = 24
SayAsInterpretAs_Time_HoursMinutesSeconds24 = 25
SayAsInterpretAs_Time_HoursMinutes24 = 26
ScrollAmount = Int32
ScrollAmount_LargeDecrement = 0
ScrollAmount_SmallDecrement = 1
ScrollAmount_NoAmount = 2
ScrollAmount_LargeIncrement = 3
ScrollAmount_SmallIncrement = 4
SERIALKEYS_FLAGS = UInt32
SERKF_AVAILABLE = 2
SERKF_INDICATOR = 4
SERKF_SERIALKEYSON = 1
def _define_SERIALKEYSA_head():
    class SERIALKEYSA(Structure):
        pass
    return SERIALKEYSA
def _define_SERIALKEYSA():
    SERIALKEYSA = win32more.UI.Accessibility.SERIALKEYSA_head
    SERIALKEYSA._fields_ = [
        ('cbSize', UInt32),
        ('dwFlags', win32more.UI.Accessibility.SERIALKEYS_FLAGS),
        ('lpszActivePort', win32more.Foundation.PSTR),
        ('lpszPort', win32more.Foundation.PSTR),
        ('iBaudRate', UInt32),
        ('iPortState', UInt32),
        ('iActive', UInt32),
    ]
    return SERIALKEYSA
def _define_SERIALKEYSW_head():
    class SERIALKEYSW(Structure):
        pass
    return SERIALKEYSW
def _define_SERIALKEYSW():
    SERIALKEYSW = win32more.UI.Accessibility.SERIALKEYSW_head
    SERIALKEYSW._fields_ = [
        ('cbSize', UInt32),
        ('dwFlags', win32more.UI.Accessibility.SERIALKEYS_FLAGS),
        ('lpszActivePort', win32more.Foundation.PWSTR),
        ('lpszPort', win32more.Foundation.PWSTR),
        ('iBaudRate', UInt32),
        ('iPortState', UInt32),
        ('iActive', UInt32),
    ]
    return SERIALKEYSW
SOUND_SENTRY_GRAPHICS_EFFECT = UInt32
SSGF_DISPLAY = 3
SSGF_NONE = 0
SOUNDSENTRY_FLAGS = UInt32
SSF_SOUNDSENTRYON = 1
SSF_AVAILABLE = 2
SSF_INDICATOR = 4
SOUNDSENTRY_TEXT_EFFECT = UInt32
SSTF_BORDER = 2
SSTF_CHARS = 1
SSTF_DISPLAY = 3
SSTF_NONE = 0
SOUNDSENTRY_WINDOWS_EFFECT = UInt32
SSWF_CUSTOM = 4
SSWF_DISPLAY = 3
SSWF_NONE = 0
SSWF_TITLE = 1
SSWF_WINDOW = 2
def _define_SOUNDSENTRYA_head():
    class SOUNDSENTRYA(Structure):
        pass
    return SOUNDSENTRYA
def _define_SOUNDSENTRYA():
    SOUNDSENTRYA = win32more.UI.Accessibility.SOUNDSENTRYA_head
    SOUNDSENTRYA._fields_ = [
        ('cbSize', UInt32),
        ('dwFlags', win32more.UI.Accessibility.SOUNDSENTRY_FLAGS),
        ('iFSTextEffect', win32more.UI.Accessibility.SOUNDSENTRY_TEXT_EFFECT),
        ('iFSTextEffectMSec', UInt32),
        ('iFSTextEffectColorBits', UInt32),
        ('iFSGrafEffect', win32more.UI.Accessibility.SOUND_SENTRY_GRAPHICS_EFFECT),
        ('iFSGrafEffectMSec', UInt32),
        ('iFSGrafEffectColor', UInt32),
        ('iWindowsEffect', win32more.UI.Accessibility.SOUNDSENTRY_WINDOWS_EFFECT),
        ('iWindowsEffectMSec', UInt32),
        ('lpszWindowsEffectDLL', win32more.Foundation.PSTR),
        ('iWindowsEffectOrdinal', UInt32),
    ]
    return SOUNDSENTRYA
def _define_SOUNDSENTRYW_head():
    class SOUNDSENTRYW(Structure):
        pass
    return SOUNDSENTRYW
def _define_SOUNDSENTRYW():
    SOUNDSENTRYW = win32more.UI.Accessibility.SOUNDSENTRYW_head
    SOUNDSENTRYW._fields_ = [
        ('cbSize', UInt32),
        ('dwFlags', win32more.UI.Accessibility.SOUNDSENTRY_FLAGS),
        ('iFSTextEffect', win32more.UI.Accessibility.SOUNDSENTRY_TEXT_EFFECT),
        ('iFSTextEffectMSec', UInt32),
        ('iFSTextEffectColorBits', UInt32),
        ('iFSGrafEffect', win32more.UI.Accessibility.SOUND_SENTRY_GRAPHICS_EFFECT),
        ('iFSGrafEffectMSec', UInt32),
        ('iFSGrafEffectColor', UInt32),
        ('iWindowsEffect', win32more.UI.Accessibility.SOUNDSENTRY_WINDOWS_EFFECT),
        ('iWindowsEffectMSec', UInt32),
        ('lpszWindowsEffectDLL', win32more.Foundation.PWSTR),
        ('iWindowsEffectOrdinal', UInt32),
    ]
    return SOUNDSENTRYW
def _define_STICKYKEYS_head():
    class STICKYKEYS(Structure):
        pass
    return STICKYKEYS
def _define_STICKYKEYS():
    STICKYKEYS = win32more.UI.Accessibility.STICKYKEYS_head
    STICKYKEYS._fields_ = [
        ('cbSize', UInt32),
        ('dwFlags', win32more.UI.Accessibility.STICKYKEYS_FLAGS),
    ]
    return STICKYKEYS
STICKYKEYS_FLAGS = UInt32
SKF_STICKYKEYSON = 1
SKF_AVAILABLE = 2
SKF_HOTKEYACTIVE = 4
SKF_CONFIRMHOTKEY = 8
SKF_HOTKEYSOUND = 16
SKF_INDICATOR = 32
SKF_AUDIBLEFEEDBACK = 64
SKF_TRISTATE = 128
SKF_TWOKEYSOFF = 256
SKF_LALTLATCHED = 268435456
SKF_LCTLLATCHED = 67108864
SKF_LSHIFTLATCHED = 16777216
SKF_RALTLATCHED = 536870912
SKF_RCTLLATCHED = 134217728
SKF_RSHIFTLATCHED = 33554432
SKF_LWINLATCHED = 1073741824
SKF_RWINLATCHED = 2147483648
SKF_LALTLOCKED = 1048576
SKF_LCTLLOCKED = 262144
SKF_LSHIFTLOCKED = 65536
SKF_RALTLOCKED = 2097152
SKF_RCTLLOCKED = 524288
SKF_RSHIFTLOCKED = 131072
SKF_LWINLOCKED = 4194304
SKF_RWINLOCKED = 8388608
StructureChangeType = Int32
StructureChangeType_ChildAdded = 0
StructureChangeType_ChildRemoved = 1
StructureChangeType_ChildrenInvalidated = 2
StructureChangeType_ChildrenBulkAdded = 3
StructureChangeType_ChildrenBulkRemoved = 4
StructureChangeType_ChildrenReordered = 5
SupportedTextSelection = Int32
SupportedTextSelection_None = 0
SupportedTextSelection_Single = 1
SupportedTextSelection_Multiple = 2
SynchronizedInputType = Int32
SynchronizedInputType_KeyUp = 1
SynchronizedInputType_KeyDown = 2
SynchronizedInputType_LeftMouseUp = 4
SynchronizedInputType_LeftMouseDown = 8
SynchronizedInputType_RightMouseUp = 16
SynchronizedInputType_RightMouseDown = 32
TextDecorationLineStyle = Int32
TextDecorationLineStyle_None = 0
TextDecorationLineStyle_Single = 1
TextDecorationLineStyle_WordsOnly = 2
TextDecorationLineStyle_Double = 3
TextDecorationLineStyle_Dot = 4
TextDecorationLineStyle_Dash = 5
TextDecorationLineStyle_DashDot = 6
TextDecorationLineStyle_DashDotDot = 7
TextDecorationLineStyle_Wavy = 8
TextDecorationLineStyle_ThickSingle = 9
TextDecorationLineStyle_DoubleWavy = 11
TextDecorationLineStyle_ThickWavy = 12
TextDecorationLineStyle_LongDash = 13
TextDecorationLineStyle_ThickDash = 14
TextDecorationLineStyle_ThickDashDot = 15
TextDecorationLineStyle_ThickDashDotDot = 16
TextDecorationLineStyle_ThickDot = 17
TextDecorationLineStyle_ThickLongDash = 18
TextDecorationLineStyle_Other = -1
TextEditChangeType = Int32
TextEditChangeType_None = 0
TextEditChangeType_AutoCorrect = 1
TextEditChangeType_Composition = 2
TextEditChangeType_CompositionFinalized = 3
TextEditChangeType_AutoComplete = 4
TextPatternRangeEndpoint = Int32
TextPatternRangeEndpoint_Start = 0
TextPatternRangeEndpoint_End = 1
TextUnit = Int32
TextUnit_Character = 0
TextUnit_Format = 1
TextUnit_Word = 2
TextUnit_Line = 3
TextUnit_Paragraph = 4
TextUnit_Page = 5
TextUnit_Document = 6
def _define_TOGGLEKEYS_head():
    class TOGGLEKEYS(Structure):
        pass
    return TOGGLEKEYS
def _define_TOGGLEKEYS():
    TOGGLEKEYS = win32more.UI.Accessibility.TOGGLEKEYS_head
    TOGGLEKEYS._fields_ = [
        ('cbSize', UInt32),
        ('dwFlags', UInt32),
    ]
    return TOGGLEKEYS
ToggleState = Int32
ToggleState_Off = 0
ToggleState_On = 1
ToggleState_Indeterminate = 2
TreeScope = Int32
TreeScope_None = 0
TreeScope_Element = 1
TreeScope_Children = 2
TreeScope_Descendants = 4
TreeScope_Parent = 8
TreeScope_Ancestors = 16
TreeScope_Subtree = 7
TreeTraversalOptions = Int32
TreeTraversalOptions_Default = 0
TreeTraversalOptions_PostOrder = 1
TreeTraversalOptions_LastToFirstOrder = 2
UIA_ANNOTATIONTYPE = UInt32
AnnotationType_Unknown = 60000
AnnotationType_SpellingError = 60001
AnnotationType_GrammarError = 60002
AnnotationType_Comment = 60003
AnnotationType_FormulaError = 60004
AnnotationType_TrackChanges = 60005
AnnotationType_Header = 60006
AnnotationType_Footer = 60007
AnnotationType_Highlighted = 60008
AnnotationType_Endnote = 60009
AnnotationType_Footnote = 60010
AnnotationType_InsertionChange = 60011
AnnotationType_DeletionChange = 60012
AnnotationType_MoveChange = 60013
AnnotationType_FormatChange = 60014
AnnotationType_UnsyncedChange = 60015
AnnotationType_EditingLockedChange = 60016
AnnotationType_ExternalChange = 60017
AnnotationType_ConflictingChange = 60018
AnnotationType_Author = 60019
AnnotationType_AdvancedProofingIssue = 60020
AnnotationType_DataValidationError = 60021
AnnotationType_CircularReferenceError = 60022
AnnotationType_Mathematics = 60023
AnnotationType_Sensitive = 60024
UIA_CHANGE_ID = UInt32
UIA_SummaryChangeId = 90000
UIA_CONTROLTYPE_ID = UInt32
UIA_ButtonControlTypeId = 50000
UIA_CalendarControlTypeId = 50001
UIA_CheckBoxControlTypeId = 50002
UIA_ComboBoxControlTypeId = 50003
UIA_EditControlTypeId = 50004
UIA_HyperlinkControlTypeId = 50005
UIA_ImageControlTypeId = 50006
UIA_ListItemControlTypeId = 50007
UIA_ListControlTypeId = 50008
UIA_MenuControlTypeId = 50009
UIA_MenuBarControlTypeId = 50010
UIA_MenuItemControlTypeId = 50011
UIA_ProgressBarControlTypeId = 50012
UIA_RadioButtonControlTypeId = 50013
UIA_ScrollBarControlTypeId = 50014
UIA_SliderControlTypeId = 50015
UIA_SpinnerControlTypeId = 50016
UIA_StatusBarControlTypeId = 50017
UIA_TabControlTypeId = 50018
UIA_TabItemControlTypeId = 50019
UIA_TextControlTypeId = 50020
UIA_ToolBarControlTypeId = 50021
UIA_ToolTipControlTypeId = 50022
UIA_TreeControlTypeId = 50023
UIA_TreeItemControlTypeId = 50024
UIA_CustomControlTypeId = 50025
UIA_GroupControlTypeId = 50026
UIA_ThumbControlTypeId = 50027
UIA_DataGridControlTypeId = 50028
UIA_DataItemControlTypeId = 50029
UIA_DocumentControlTypeId = 50030
UIA_SplitButtonControlTypeId = 50031
UIA_WindowControlTypeId = 50032
UIA_PaneControlTypeId = 50033
UIA_HeaderControlTypeId = 50034
UIA_HeaderItemControlTypeId = 50035
UIA_TableControlTypeId = 50036
UIA_TitleBarControlTypeId = 50037
UIA_SeparatorControlTypeId = 50038
UIA_SemanticZoomControlTypeId = 50039
UIA_AppBarControlTypeId = 50040
UIA_EVENT_ID = UInt32
UIA_ToolTipOpenedEventId = 20000
UIA_ToolTipClosedEventId = 20001
UIA_StructureChangedEventId = 20002
UIA_MenuOpenedEventId = 20003
UIA_AutomationPropertyChangedEventId = 20004
UIA_AutomationFocusChangedEventId = 20005
UIA_AsyncContentLoadedEventId = 20006
UIA_MenuClosedEventId = 20007
UIA_LayoutInvalidatedEventId = 20008
UIA_Invoke_InvokedEventId = 20009
UIA_SelectionItem_ElementAddedToSelectionEventId = 20010
UIA_SelectionItem_ElementRemovedFromSelectionEventId = 20011
UIA_SelectionItem_ElementSelectedEventId = 20012
UIA_Selection_InvalidatedEventId = 20013
UIA_Text_TextSelectionChangedEventId = 20014
UIA_Text_TextChangedEventId = 20015
UIA_Window_WindowOpenedEventId = 20016
UIA_Window_WindowClosedEventId = 20017
UIA_MenuModeStartEventId = 20018
UIA_MenuModeEndEventId = 20019
UIA_InputReachedTargetEventId = 20020
UIA_InputReachedOtherElementEventId = 20021
UIA_InputDiscardedEventId = 20022
UIA_SystemAlertEventId = 20023
UIA_LiveRegionChangedEventId = 20024
UIA_HostedFragmentRootsInvalidatedEventId = 20025
UIA_Drag_DragStartEventId = 20026
UIA_Drag_DragCancelEventId = 20027
UIA_Drag_DragCompleteEventId = 20028
UIA_DropTarget_DragEnterEventId = 20029
UIA_DropTarget_DragLeaveEventId = 20030
UIA_DropTarget_DroppedEventId = 20031
UIA_TextEdit_TextChangedEventId = 20032
UIA_TextEdit_ConversionTargetChangedEventId = 20033
UIA_ChangesEventId = 20034
UIA_NotificationEventId = 20035
UIA_ActiveTextPositionChangedEventId = 20036
UIA_HEADINGLEVEL_ID = UInt32
UIA_HEADINGLEVEL_ID_HeadingLevel_None = 80050
UIA_HEADINGLEVEL_ID_HeadingLevel1 = 80051
UIA_HEADINGLEVEL_ID_HeadingLevel2 = 80052
UIA_HEADINGLEVEL_ID_HeadingLevel3 = 80053
UIA_HEADINGLEVEL_ID_HeadingLevel4 = 80054
UIA_HEADINGLEVEL_ID_HeadingLevel5 = 80055
UIA_HEADINGLEVEL_ID_HeadingLevel6 = 80056
UIA_HEADINGLEVEL_ID_HeadingLevel7 = 80057
UIA_HEADINGLEVEL_ID_HeadingLevel8 = 80058
UIA_HEADINGLEVEL_ID_HeadingLevel9 = 80059
UIA_LANDMARKTYPE_ID = UInt32
UIA_CustomLandmarkTypeId = 80000
UIA_FormLandmarkTypeId = 80001
UIA_MainLandmarkTypeId = 80002
UIA_NavigationLandmarkTypeId = 80003
UIA_SearchLandmarkTypeId = 80004
UIA_METADATA_ID = UInt32
UIA_SayAsInterpretAsMetadataId = 100000
UIA_PATTERN_ID = UInt32
UIA_InvokePatternId = 10000
UIA_SelectionPatternId = 10001
UIA_ValuePatternId = 10002
UIA_RangeValuePatternId = 10003
UIA_ScrollPatternId = 10004
UIA_ExpandCollapsePatternId = 10005
UIA_GridPatternId = 10006
UIA_GridItemPatternId = 10007
UIA_MultipleViewPatternId = 10008
UIA_WindowPatternId = 10009
UIA_SelectionItemPatternId = 10010
UIA_DockPatternId = 10011
UIA_TablePatternId = 10012
UIA_TableItemPatternId = 10013
UIA_TextPatternId = 10014
UIA_TogglePatternId = 10015
UIA_TransformPatternId = 10016
UIA_ScrollItemPatternId = 10017
UIA_LegacyIAccessiblePatternId = 10018
UIA_ItemContainerPatternId = 10019
UIA_VirtualizedItemPatternId = 10020
UIA_SynchronizedInputPatternId = 10021
UIA_ObjectModelPatternId = 10022
UIA_AnnotationPatternId = 10023
UIA_TextPattern2Id = 10024
UIA_StylesPatternId = 10025
UIA_SpreadsheetPatternId = 10026
UIA_SpreadsheetItemPatternId = 10027
UIA_TransformPattern2Id = 10028
UIA_TextChildPatternId = 10029
UIA_DragPatternId = 10030
UIA_DropTargetPatternId = 10031
UIA_TextEditPatternId = 10032
UIA_CustomNavigationPatternId = 10033
UIA_SelectionPattern2Id = 10034
UIA_PROPERTY_ID = UInt32
UIA_RuntimeIdPropertyId = 30000
UIA_BoundingRectanglePropertyId = 30001
UIA_ProcessIdPropertyId = 30002
UIA_ControlTypePropertyId = 30003
UIA_LocalizedControlTypePropertyId = 30004
UIA_NamePropertyId = 30005
UIA_AcceleratorKeyPropertyId = 30006
UIA_AccessKeyPropertyId = 30007
UIA_HasKeyboardFocusPropertyId = 30008
UIA_IsKeyboardFocusablePropertyId = 30009
UIA_IsEnabledPropertyId = 30010
UIA_AutomationIdPropertyId = 30011
UIA_ClassNamePropertyId = 30012
UIA_HelpTextPropertyId = 30013
UIA_ClickablePointPropertyId = 30014
UIA_CulturePropertyId = 30015
UIA_IsControlElementPropertyId = 30016
UIA_IsContentElementPropertyId = 30017
UIA_LabeledByPropertyId = 30018
UIA_IsPasswordPropertyId = 30019
UIA_NativeWindowHandlePropertyId = 30020
UIA_ItemTypePropertyId = 30021
UIA_IsOffscreenPropertyId = 30022
UIA_OrientationPropertyId = 30023
UIA_FrameworkIdPropertyId = 30024
UIA_IsRequiredForFormPropertyId = 30025
UIA_ItemStatusPropertyId = 30026
UIA_IsDockPatternAvailablePropertyId = 30027
UIA_IsExpandCollapsePatternAvailablePropertyId = 30028
UIA_IsGridItemPatternAvailablePropertyId = 30029
UIA_IsGridPatternAvailablePropertyId = 30030
UIA_IsInvokePatternAvailablePropertyId = 30031
UIA_IsMultipleViewPatternAvailablePropertyId = 30032
UIA_IsRangeValuePatternAvailablePropertyId = 30033
UIA_IsScrollPatternAvailablePropertyId = 30034
UIA_IsScrollItemPatternAvailablePropertyId = 30035
UIA_IsSelectionItemPatternAvailablePropertyId = 30036
UIA_IsSelectionPatternAvailablePropertyId = 30037
UIA_IsTablePatternAvailablePropertyId = 30038
UIA_IsTableItemPatternAvailablePropertyId = 30039
UIA_IsTextPatternAvailablePropertyId = 30040
UIA_IsTogglePatternAvailablePropertyId = 30041
UIA_IsTransformPatternAvailablePropertyId = 30042
UIA_IsValuePatternAvailablePropertyId = 30043
UIA_IsWindowPatternAvailablePropertyId = 30044
UIA_ValueValuePropertyId = 30045
UIA_ValueIsReadOnlyPropertyId = 30046
UIA_RangeValueValuePropertyId = 30047
UIA_RangeValueIsReadOnlyPropertyId = 30048
UIA_RangeValueMinimumPropertyId = 30049
UIA_RangeValueMaximumPropertyId = 30050
UIA_RangeValueLargeChangePropertyId = 30051
UIA_RangeValueSmallChangePropertyId = 30052
UIA_ScrollHorizontalScrollPercentPropertyId = 30053
UIA_ScrollHorizontalViewSizePropertyId = 30054
UIA_ScrollVerticalScrollPercentPropertyId = 30055
UIA_ScrollVerticalViewSizePropertyId = 30056
UIA_ScrollHorizontallyScrollablePropertyId = 30057
UIA_ScrollVerticallyScrollablePropertyId = 30058
UIA_SelectionSelectionPropertyId = 30059
UIA_SelectionCanSelectMultiplePropertyId = 30060
UIA_SelectionIsSelectionRequiredPropertyId = 30061
UIA_GridRowCountPropertyId = 30062
UIA_GridColumnCountPropertyId = 30063
UIA_GridItemRowPropertyId = 30064
UIA_GridItemColumnPropertyId = 30065
UIA_GridItemRowSpanPropertyId = 30066
UIA_GridItemColumnSpanPropertyId = 30067
UIA_GridItemContainingGridPropertyId = 30068
UIA_DockDockPositionPropertyId = 30069
UIA_ExpandCollapseExpandCollapseStatePropertyId = 30070
UIA_MultipleViewCurrentViewPropertyId = 30071
UIA_MultipleViewSupportedViewsPropertyId = 30072
UIA_WindowCanMaximizePropertyId = 30073
UIA_WindowCanMinimizePropertyId = 30074
UIA_WindowWindowVisualStatePropertyId = 30075
UIA_WindowWindowInteractionStatePropertyId = 30076
UIA_WindowIsModalPropertyId = 30077
UIA_WindowIsTopmostPropertyId = 30078
UIA_SelectionItemIsSelectedPropertyId = 30079
UIA_SelectionItemSelectionContainerPropertyId = 30080
UIA_TableRowHeadersPropertyId = 30081
UIA_TableColumnHeadersPropertyId = 30082
UIA_TableRowOrColumnMajorPropertyId = 30083
UIA_TableItemRowHeaderItemsPropertyId = 30084
UIA_TableItemColumnHeaderItemsPropertyId = 30085
UIA_ToggleToggleStatePropertyId = 30086
UIA_TransformCanMovePropertyId = 30087
UIA_TransformCanResizePropertyId = 30088
UIA_TransformCanRotatePropertyId = 30089
UIA_IsLegacyIAccessiblePatternAvailablePropertyId = 30090
UIA_LegacyIAccessibleChildIdPropertyId = 30091
UIA_LegacyIAccessibleNamePropertyId = 30092
UIA_LegacyIAccessibleValuePropertyId = 30093
UIA_LegacyIAccessibleDescriptionPropertyId = 30094
UIA_LegacyIAccessibleRolePropertyId = 30095
UIA_LegacyIAccessibleStatePropertyId = 30096
UIA_LegacyIAccessibleHelpPropertyId = 30097
UIA_LegacyIAccessibleKeyboardShortcutPropertyId = 30098
UIA_LegacyIAccessibleSelectionPropertyId = 30099
UIA_LegacyIAccessibleDefaultActionPropertyId = 30100
UIA_AriaRolePropertyId = 30101
UIA_AriaPropertiesPropertyId = 30102
UIA_IsDataValidForFormPropertyId = 30103
UIA_ControllerForPropertyId = 30104
UIA_DescribedByPropertyId = 30105
UIA_FlowsToPropertyId = 30106
UIA_ProviderDescriptionPropertyId = 30107
UIA_IsItemContainerPatternAvailablePropertyId = 30108
UIA_IsVirtualizedItemPatternAvailablePropertyId = 30109
UIA_IsSynchronizedInputPatternAvailablePropertyId = 30110
UIA_OptimizeForVisualContentPropertyId = 30111
UIA_IsObjectModelPatternAvailablePropertyId = 30112
UIA_AnnotationAnnotationTypeIdPropertyId = 30113
UIA_AnnotationAnnotationTypeNamePropertyId = 30114
UIA_AnnotationAuthorPropertyId = 30115
UIA_AnnotationDateTimePropertyId = 30116
UIA_AnnotationTargetPropertyId = 30117
UIA_IsAnnotationPatternAvailablePropertyId = 30118
UIA_IsTextPattern2AvailablePropertyId = 30119
UIA_StylesStyleIdPropertyId = 30120
UIA_StylesStyleNamePropertyId = 30121
UIA_StylesFillColorPropertyId = 30122
UIA_StylesFillPatternStylePropertyId = 30123
UIA_StylesShapePropertyId = 30124
UIA_StylesFillPatternColorPropertyId = 30125
UIA_StylesExtendedPropertiesPropertyId = 30126
UIA_IsStylesPatternAvailablePropertyId = 30127
UIA_IsSpreadsheetPatternAvailablePropertyId = 30128
UIA_SpreadsheetItemFormulaPropertyId = 30129
UIA_SpreadsheetItemAnnotationObjectsPropertyId = 30130
UIA_SpreadsheetItemAnnotationTypesPropertyId = 30131
UIA_IsSpreadsheetItemPatternAvailablePropertyId = 30132
UIA_Transform2CanZoomPropertyId = 30133
UIA_IsTransformPattern2AvailablePropertyId = 30134
UIA_LiveSettingPropertyId = 30135
UIA_IsTextChildPatternAvailablePropertyId = 30136
UIA_IsDragPatternAvailablePropertyId = 30137
UIA_DragIsGrabbedPropertyId = 30138
UIA_DragDropEffectPropertyId = 30139
UIA_DragDropEffectsPropertyId = 30140
UIA_IsDropTargetPatternAvailablePropertyId = 30141
UIA_DropTargetDropTargetEffectPropertyId = 30142
UIA_DropTargetDropTargetEffectsPropertyId = 30143
UIA_DragGrabbedItemsPropertyId = 30144
UIA_Transform2ZoomLevelPropertyId = 30145
UIA_Transform2ZoomMinimumPropertyId = 30146
UIA_Transform2ZoomMaximumPropertyId = 30147
UIA_FlowsFromPropertyId = 30148
UIA_IsTextEditPatternAvailablePropertyId = 30149
UIA_IsPeripheralPropertyId = 30150
UIA_IsCustomNavigationPatternAvailablePropertyId = 30151
UIA_PositionInSetPropertyId = 30152
UIA_SizeOfSetPropertyId = 30153
UIA_LevelPropertyId = 30154
UIA_AnnotationTypesPropertyId = 30155
UIA_AnnotationObjectsPropertyId = 30156
UIA_LandmarkTypePropertyId = 30157
UIA_LocalizedLandmarkTypePropertyId = 30158
UIA_FullDescriptionPropertyId = 30159
UIA_FillColorPropertyId = 30160
UIA_OutlineColorPropertyId = 30161
UIA_FillTypePropertyId = 30162
UIA_VisualEffectsPropertyId = 30163
UIA_OutlineThicknessPropertyId = 30164
UIA_CenterPointPropertyId = 30165
UIA_RotationPropertyId = 30166
UIA_SizePropertyId = 30167
UIA_IsSelectionPattern2AvailablePropertyId = 30168
UIA_Selection2FirstSelectedItemPropertyId = 30169
UIA_Selection2LastSelectedItemPropertyId = 30170
UIA_Selection2CurrentSelectedItemPropertyId = 30171
UIA_Selection2ItemCountPropertyId = 30172
UIA_HeadingLevelPropertyId = 30173
UIA_IsDialogPropertyId = 30174
UIA_STYLE_ID = UInt32
StyleId_Custom = 70000
StyleId_Heading1 = 70001
StyleId_Heading2 = 70002
StyleId_Heading3 = 70003
StyleId_Heading4 = 70004
StyleId_Heading5 = 70005
StyleId_Heading6 = 70006
StyleId_Heading7 = 70007
StyleId_Heading8 = 70008
StyleId_Heading9 = 70009
StyleId_Title = 70010
StyleId_Subtitle = 70011
StyleId_Normal = 70012
StyleId_Emphasis = 70013
StyleId_Quote = 70014
StyleId_BulletedList = 70015
StyleId_NumberedList = 70016
UIA_TEXTATTRIBUTE_ID = UInt32
UIA_AnimationStyleAttributeId = 40000
UIA_BackgroundColorAttributeId = 40001
UIA_BulletStyleAttributeId = 40002
UIA_CapStyleAttributeId = 40003
UIA_CultureAttributeId = 40004
UIA_FontNameAttributeId = 40005
UIA_FontSizeAttributeId = 40006
UIA_FontWeightAttributeId = 40007
UIA_ForegroundColorAttributeId = 40008
UIA_HorizontalTextAlignmentAttributeId = 40009
UIA_IndentationFirstLineAttributeId = 40010
UIA_IndentationLeadingAttributeId = 40011
UIA_IndentationTrailingAttributeId = 40012
UIA_IsHiddenAttributeId = 40013
UIA_IsItalicAttributeId = 40014
UIA_IsReadOnlyAttributeId = 40015
UIA_IsSubscriptAttributeId = 40016
UIA_IsSuperscriptAttributeId = 40017
UIA_MarginBottomAttributeId = 40018
UIA_MarginLeadingAttributeId = 40019
UIA_MarginTopAttributeId = 40020
UIA_MarginTrailingAttributeId = 40021
UIA_OutlineStylesAttributeId = 40022
UIA_OverlineColorAttributeId = 40023
UIA_OverlineStyleAttributeId = 40024
UIA_StrikethroughColorAttributeId = 40025
UIA_StrikethroughStyleAttributeId = 40026
UIA_TabsAttributeId = 40027
UIA_TextFlowDirectionsAttributeId = 40028
UIA_UnderlineColorAttributeId = 40029
UIA_UnderlineStyleAttributeId = 40030
UIA_AnnotationTypesAttributeId = 40031
UIA_AnnotationObjectsAttributeId = 40032
UIA_StyleNameAttributeId = 40033
UIA_StyleIdAttributeId = 40034
UIA_LinkAttributeId = 40035
UIA_IsActiveAttributeId = 40036
UIA_SelectionActiveEndAttributeId = 40037
UIA_CaretPositionAttributeId = 40038
UIA_CaretBidiModeAttributeId = 40039
UIA_LineSpacingAttributeId = 40040
UIA_BeforeParagraphSpacingAttributeId = 40041
UIA_AfterParagraphSpacingAttributeId = 40042
UIA_SayAsInterpretAsAttributeId = 40043
def _define_UiaAndOrCondition_head():
    class UiaAndOrCondition(Structure):
        pass
    return UiaAndOrCondition
def _define_UiaAndOrCondition():
    UiaAndOrCondition = win32more.UI.Accessibility.UiaAndOrCondition_head
    UiaAndOrCondition._fields_ = [
        ('ConditionType', win32more.UI.Accessibility.ConditionType),
        ('ppConditions', POINTER(POINTER(win32more.UI.Accessibility.UiaCondition_head))),
        ('cConditions', Int32),
    ]
    return UiaAndOrCondition
def _define_UiaAsyncContentLoadedEventArgs_head():
    class UiaAsyncContentLoadedEventArgs(Structure):
        pass
    return UiaAsyncContentLoadedEventArgs
def _define_UiaAsyncContentLoadedEventArgs():
    UiaAsyncContentLoadedEventArgs = win32more.UI.Accessibility.UiaAsyncContentLoadedEventArgs_head
    UiaAsyncContentLoadedEventArgs._fields_ = [
        ('Type', win32more.UI.Accessibility.EventArgsType),
        ('EventId', Int32),
        ('AsyncContentLoadedState', win32more.UI.Accessibility.AsyncContentLoadedState),
        ('PercentComplete', Double),
    ]
    return UiaAsyncContentLoadedEventArgs
def _define_UiaCacheRequest_head():
    class UiaCacheRequest(Structure):
        pass
    return UiaCacheRequest
def _define_UiaCacheRequest():
    UiaCacheRequest = win32more.UI.Accessibility.UiaCacheRequest_head
    UiaCacheRequest._fields_ = [
        ('pViewCondition', POINTER(win32more.UI.Accessibility.UiaCondition_head)),
        ('Scope', win32more.UI.Accessibility.TreeScope),
        ('pProperties', POINTER(Int32)),
        ('cProperties', Int32),
        ('pPatterns', POINTER(Int32)),
        ('cPatterns', Int32),
        ('automationElementMode', win32more.UI.Accessibility.AutomationElementMode),
    ]
    return UiaCacheRequest
def _define_UiaChangeInfo_head():
    class UiaChangeInfo(Structure):
        pass
    return UiaChangeInfo
def _define_UiaChangeInfo():
    UiaChangeInfo = win32more.UI.Accessibility.UiaChangeInfo_head
    UiaChangeInfo._fields_ = [
        ('uiaId', Int32),
        ('payload', win32more.System.Com.VARIANT),
        ('extraInfo', win32more.System.Com.VARIANT),
    ]
    return UiaChangeInfo
def _define_UiaChangesEventArgs_head():
    class UiaChangesEventArgs(Structure):
        pass
    return UiaChangesEventArgs
def _define_UiaChangesEventArgs():
    UiaChangesEventArgs = win32more.UI.Accessibility.UiaChangesEventArgs_head
    UiaChangesEventArgs._fields_ = [
        ('Type', win32more.UI.Accessibility.EventArgsType),
        ('EventId', Int32),
        ('EventIdCount', Int32),
        ('pUiaChanges', POINTER(win32more.UI.Accessibility.UiaChangeInfo_head)),
    ]
    return UiaChangesEventArgs
def _define_UiaCondition_head():
    class UiaCondition(Structure):
        pass
    return UiaCondition
def _define_UiaCondition():
    UiaCondition = win32more.UI.Accessibility.UiaCondition_head
    UiaCondition._fields_ = [
        ('ConditionType', win32more.UI.Accessibility.ConditionType),
    ]
    return UiaCondition
def _define_UiaEventArgs_head():
    class UiaEventArgs(Structure):
        pass
    return UiaEventArgs
def _define_UiaEventArgs():
    UiaEventArgs = win32more.UI.Accessibility.UiaEventArgs_head
    UiaEventArgs._fields_ = [
        ('Type', win32more.UI.Accessibility.EventArgsType),
        ('EventId', Int32),
    ]
    return UiaEventArgs
def _define_UiaEventCallback():
    return WINFUNCTYPE(Void,POINTER(win32more.UI.Accessibility.UiaEventArgs_head),POINTER(win32more.System.Com.SAFEARRAY_head),win32more.Foundation.BSTR)
def _define_UiaFindParams_head():
    class UiaFindParams(Structure):
        pass
    return UiaFindParams
def _define_UiaFindParams():
    UiaFindParams = win32more.UI.Accessibility.UiaFindParams_head
    UiaFindParams._fields_ = [
        ('MaxDepth', Int32),
        ('FindFirst', win32more.Foundation.BOOL),
        ('ExcludeRoot', win32more.Foundation.BOOL),
        ('pFindCondition', POINTER(win32more.UI.Accessibility.UiaCondition_head)),
    ]
    return UiaFindParams
def _define_UiaNotCondition_head():
    class UiaNotCondition(Structure):
        pass
    return UiaNotCondition
def _define_UiaNotCondition():
    UiaNotCondition = win32more.UI.Accessibility.UiaNotCondition_head
    UiaNotCondition._fields_ = [
        ('ConditionType', win32more.UI.Accessibility.ConditionType),
        ('pCondition', POINTER(win32more.UI.Accessibility.UiaCondition_head)),
    ]
    return UiaNotCondition
def _define_UiaPoint_head():
    class UiaPoint(Structure):
        pass
    return UiaPoint
def _define_UiaPoint():
    UiaPoint = win32more.UI.Accessibility.UiaPoint_head
    UiaPoint._fields_ = [
        ('x', Double),
        ('y', Double),
    ]
    return UiaPoint
def _define_UiaPropertyChangedEventArgs_head():
    class UiaPropertyChangedEventArgs(Structure):
        pass
    return UiaPropertyChangedEventArgs
def _define_UiaPropertyChangedEventArgs():
    UiaPropertyChangedEventArgs = win32more.UI.Accessibility.UiaPropertyChangedEventArgs_head
    UiaPropertyChangedEventArgs._fields_ = [
        ('Type', win32more.UI.Accessibility.EventArgsType),
        ('EventId', win32more.UI.Accessibility.UIA_EVENT_ID),
        ('PropertyId', Int32),
        ('OldValue', win32more.System.Com.VARIANT),
        ('NewValue', win32more.System.Com.VARIANT),
    ]
    return UiaPropertyChangedEventArgs
def _define_UiaPropertyCondition_head():
    class UiaPropertyCondition(Structure):
        pass
    return UiaPropertyCondition
def _define_UiaPropertyCondition():
    UiaPropertyCondition = win32more.UI.Accessibility.UiaPropertyCondition_head
    UiaPropertyCondition._fields_ = [
        ('ConditionType', win32more.UI.Accessibility.ConditionType),
        ('PropertyId', win32more.UI.Accessibility.UIA_PROPERTY_ID),
        ('Value', win32more.System.Com.VARIANT),
        ('Flags', win32more.UI.Accessibility.PropertyConditionFlags),
    ]
    return UiaPropertyCondition
def _define_UiaProviderCallback():
    return WINFUNCTYPE(POINTER(win32more.System.Com.SAFEARRAY_head),win32more.Foundation.HWND,win32more.UI.Accessibility.ProviderType)
def _define_UiaRect_head():
    class UiaRect(Structure):
        pass
    return UiaRect
def _define_UiaRect():
    UiaRect = win32more.UI.Accessibility.UiaRect_head
    UiaRect._fields_ = [
        ('left', Double),
        ('top', Double),
        ('width', Double),
        ('height', Double),
    ]
    return UiaRect
def _define_UiaStructureChangedEventArgs_head():
    class UiaStructureChangedEventArgs(Structure):
        pass
    return UiaStructureChangedEventArgs
def _define_UiaStructureChangedEventArgs():
    UiaStructureChangedEventArgs = win32more.UI.Accessibility.UiaStructureChangedEventArgs_head
    UiaStructureChangedEventArgs._fields_ = [
        ('Type', win32more.UI.Accessibility.EventArgsType),
        ('EventId', Int32),
        ('StructureChangeType', win32more.UI.Accessibility.StructureChangeType),
        ('pRuntimeId', POINTER(Int32)),
        ('cRuntimeIdLen', Int32),
    ]
    return UiaStructureChangedEventArgs
def _define_UiaTextEditTextChangedEventArgs_head():
    class UiaTextEditTextChangedEventArgs(Structure):
        pass
    return UiaTextEditTextChangedEventArgs
def _define_UiaTextEditTextChangedEventArgs():
    UiaTextEditTextChangedEventArgs = win32more.UI.Accessibility.UiaTextEditTextChangedEventArgs_head
    UiaTextEditTextChangedEventArgs._fields_ = [
        ('Type', win32more.UI.Accessibility.EventArgsType),
        ('EventId', Int32),
        ('TextEditChangeType', win32more.UI.Accessibility.TextEditChangeType),
        ('pTextChange', POINTER(win32more.System.Com.SAFEARRAY_head)),
    ]
    return UiaTextEditTextChangedEventArgs
def _define_UIAutomationEventInfo_head():
    class UIAutomationEventInfo(Structure):
        pass
    return UIAutomationEventInfo
def _define_UIAutomationEventInfo():
    UIAutomationEventInfo = win32more.UI.Accessibility.UIAutomationEventInfo_head
    UIAutomationEventInfo._fields_ = [
        ('guid', Guid),
        ('pProgrammaticName', win32more.Foundation.PWSTR),
    ]
    return UIAutomationEventInfo
def _define_UIAutomationMethodInfo_head():
    class UIAutomationMethodInfo(Structure):
        pass
    return UIAutomationMethodInfo
def _define_UIAutomationMethodInfo():
    UIAutomationMethodInfo = win32more.UI.Accessibility.UIAutomationMethodInfo_head
    UIAutomationMethodInfo._fields_ = [
        ('pProgrammaticName', win32more.Foundation.PWSTR),
        ('doSetFocus', win32more.Foundation.BOOL),
        ('cInParameters', UInt32),
        ('cOutParameters', UInt32),
        ('pParameterTypes', POINTER(win32more.UI.Accessibility.UIAutomationType)),
        ('pParameterNames', POINTER(win32more.Foundation.PWSTR)),
    ]
    return UIAutomationMethodInfo
def _define_UIAutomationParameter_head():
    class UIAutomationParameter(Structure):
        pass
    return UIAutomationParameter
def _define_UIAutomationParameter():
    UIAutomationParameter = win32more.UI.Accessibility.UIAutomationParameter_head
    UIAutomationParameter._fields_ = [
        ('type', win32more.UI.Accessibility.UIAutomationType),
        ('pData', c_void_p),
    ]
    return UIAutomationParameter
def _define_UIAutomationPatternInfo_head():
    class UIAutomationPatternInfo(Structure):
        pass
    return UIAutomationPatternInfo
def _define_UIAutomationPatternInfo():
    UIAutomationPatternInfo = win32more.UI.Accessibility.UIAutomationPatternInfo_head
    UIAutomationPatternInfo._fields_ = [
        ('guid', Guid),
        ('pProgrammaticName', win32more.Foundation.PWSTR),
        ('providerInterfaceId', Guid),
        ('clientInterfaceId', Guid),
        ('cProperties', UInt32),
        ('pProperties', POINTER(win32more.UI.Accessibility.UIAutomationPropertyInfo_head)),
        ('cMethods', UInt32),
        ('pMethods', POINTER(win32more.UI.Accessibility.UIAutomationMethodInfo_head)),
        ('cEvents', UInt32),
        ('pEvents', POINTER(win32more.UI.Accessibility.UIAutomationEventInfo_head)),
        ('pPatternHandler', win32more.UI.Accessibility.IUIAutomationPatternHandler_head),
    ]
    return UIAutomationPatternInfo
def _define_UIAutomationPropertyInfo_head():
    class UIAutomationPropertyInfo(Structure):
        pass
    return UIAutomationPropertyInfo
def _define_UIAutomationPropertyInfo():
    UIAutomationPropertyInfo = win32more.UI.Accessibility.UIAutomationPropertyInfo_head
    UIAutomationPropertyInfo._fields_ = [
        ('guid', Guid),
        ('pProgrammaticName', win32more.Foundation.PWSTR),
        ('type', win32more.UI.Accessibility.UIAutomationType),
    ]
    return UIAutomationPropertyInfo
UIAutomationType = Int32
UIAutomationType_Int = 1
UIAutomationType_Bool = 2
UIAutomationType_String = 3
UIAutomationType_Double = 4
UIAutomationType_Point = 5
UIAutomationType_Rect = 6
UIAutomationType_Element = 7
UIAutomationType_Array = 65536
UIAutomationType_Out = 131072
UIAutomationType_IntArray = 65537
UIAutomationType_BoolArray = 65538
UIAutomationType_StringArray = 65539
UIAutomationType_DoubleArray = 65540
UIAutomationType_PointArray = 65541
UIAutomationType_RectArray = 65542
UIAutomationType_ElementArray = 65543
UIAutomationType_OutInt = 131073
UIAutomationType_OutBool = 131074
UIAutomationType_OutString = 131075
UIAutomationType_OutDouble = 131076
UIAutomationType_OutPoint = 131077
UIAutomationType_OutRect = 131078
UIAutomationType_OutElement = 131079
UIAutomationType_OutIntArray = 196609
UIAutomationType_OutBoolArray = 196610
UIAutomationType_OutStringArray = 196611
UIAutomationType_OutDoubleArray = 196612
UIAutomationType_OutPointArray = 196613
UIAutomationType_OutRectArray = 196614
UIAutomationType_OutElementArray = 196615
def _define_UiaWindowClosedEventArgs_head():
    class UiaWindowClosedEventArgs(Structure):
        pass
    return UiaWindowClosedEventArgs
def _define_UiaWindowClosedEventArgs():
    UiaWindowClosedEventArgs = win32more.UI.Accessibility.UiaWindowClosedEventArgs_head
    UiaWindowClosedEventArgs._fields_ = [
        ('Type', win32more.UI.Accessibility.EventArgsType),
        ('EventId', Int32),
        ('pRuntimeId', POINTER(Int32)),
        ('cRuntimeIdLen', Int32),
    ]
    return UiaWindowClosedEventArgs
VisualEffects = Int32
VisualEffects_None = 0
VisualEffects_Shadow = 1
VisualEffects_Reflection = 2
VisualEffects_Glow = 4
VisualEffects_SoftEdges = 8
VisualEffects_Bevel = 16
WindowInteractionState = Int32
WindowInteractionState_Running = 0
WindowInteractionState_Closing = 1
WindowInteractionState_ReadyForUserInteraction = 2
WindowInteractionState_BlockedByModalWindow = 3
WindowInteractionState_NotResponding = 4
WindowVisualState = Int32
WindowVisualState_Normal = 0
WindowVisualState_Maximized = 1
WindowVisualState_Minimized = 2
def _define_WINEVENTPROC():
    return WINFUNCTYPE(Void,win32more.UI.Accessibility.HWINEVENTHOOK,UInt32,win32more.Foundation.HWND,Int32,Int32,UInt32,UInt32)
ZoomUnit = Int32
ZoomUnit_NoAmount = 0
ZoomUnit_LargeDecrement = 1
ZoomUnit_SmallDecrement = 2
ZoomUnit_LargeIncrement = 3
ZoomUnit_SmallIncrement = 4
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
