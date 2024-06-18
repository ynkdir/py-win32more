from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.UI.Accessibility
import win32more.Windows.Win32.UI.WindowsAndMessaging
class ACCESSTIMEOUT(Structure):
    cbSize: UInt32
    dwFlags: UInt32
    iTimeOutMSec: UInt32
ACC_UTILITY_STATE_FLAGS = UInt32
ANRUS_ON_SCREEN_KEYBOARD_ACTIVE: win32more.Windows.Win32.UI.Accessibility.ACC_UTILITY_STATE_FLAGS = 1
ANRUS_TOUCH_MODIFICATION_ACTIVE: win32more.Windows.Win32.UI.Accessibility.ACC_UTILITY_STATE_FLAGS = 2
ANRUS_PRIORITY_AUDIO_ACTIVE: win32more.Windows.Win32.UI.Accessibility.ACC_UTILITY_STATE_FLAGS = 4
ANRUS_PRIORITY_AUDIO_ACTIVE_NODUCK: win32more.Windows.Win32.UI.Accessibility.ACC_UTILITY_STATE_FLAGS = 8
ActiveEnd = Int32
ActiveEnd_None: win32more.Windows.Win32.UI.Accessibility.ActiveEnd = 0
ActiveEnd_Start: win32more.Windows.Win32.UI.Accessibility.ActiveEnd = 1
ActiveEnd_End: win32more.Windows.Win32.UI.Accessibility.ActiveEnd = 2
AnimationStyle = Int32
AnimationStyle_None: win32more.Windows.Win32.UI.Accessibility.AnimationStyle = 0
AnimationStyle_LasVegasLights: win32more.Windows.Win32.UI.Accessibility.AnimationStyle = 1
AnimationStyle_BlinkingBackground: win32more.Windows.Win32.UI.Accessibility.AnimationStyle = 2
AnimationStyle_SparkleText: win32more.Windows.Win32.UI.Accessibility.AnimationStyle = 3
AnimationStyle_MarchingBlackAnts: win32more.Windows.Win32.UI.Accessibility.AnimationStyle = 4
AnimationStyle_MarchingRedAnts: win32more.Windows.Win32.UI.Accessibility.AnimationStyle = 5
AnimationStyle_Shimmer: win32more.Windows.Win32.UI.Accessibility.AnimationStyle = 6
AnimationStyle_Other: win32more.Windows.Win32.UI.Accessibility.AnimationStyle = -1
AnnoScope = Int32
ANNO_THIS: win32more.Windows.Win32.UI.Accessibility.AnnoScope = 0
ANNO_CONTAINER: win32more.Windows.Win32.UI.Accessibility.AnnoScope = 1
LIBID_Accessibility: Guid = Guid('{1ea4dbf0-3c3b-11cf-810c-00aa00389b71}')
CLSID_AccPropServices: Guid = Guid('{b5f8350b-0548-48b1-a6ee-88bd00b4a5e7}')
IIS_IsOleaccProxy: Guid = Guid('{902697fa-80e4-4560-802a-a13f22a64709}')
IIS_ControlAccessible: Guid = Guid('{38c682a6-9731-43f2-9fae-e901e641b101}')
ANRUS_PRIORITY_AUDIO_DYNAMIC_DUCK: UInt32 = 16
MSAA_MENU_SIG: Int32 = -1441927155
PROPID_ACC_NAME: Guid = Guid('{608d3df8-8128-4aa7-a428-f55e49267291}')
PROPID_ACC_VALUE: Guid = Guid('{123fe443-211a-4615-9527-c45a7e93717a}')
PROPID_ACC_DESCRIPTION: Guid = Guid('{4d48dfe4-bd3f-491f-a648-492d6f20c588}')
PROPID_ACC_ROLE: Guid = Guid('{cb905ff2-7bd1-4c05-b3c8-e6c241364d70}')
PROPID_ACC_STATE: Guid = Guid('{a8d4d5b0-0a21-42d0-a5c0-514e984f457b}')
PROPID_ACC_HELP: Guid = Guid('{c831e11f-44db-4a99-9768-cb8f978b7231}')
PROPID_ACC_KEYBOARDSHORTCUT: Guid = Guid('{7d9bceee-7d1e-4979-9382-5180f4172c34}')
PROPID_ACC_DEFAULTACTION: Guid = Guid('{180c072b-c27f-43c7-9922-f63562a4632b}')
PROPID_ACC_HELPTOPIC: Guid = Guid('{787d1379-8ede-440b-8aec-11f7bf9030b3}')
PROPID_ACC_FOCUS: Guid = Guid('{6eb335df-1c29-4127-b12c-dee9fd157f2b}')
PROPID_ACC_SELECTION: Guid = Guid('{b99d073c-d731-405b-9061-d95e8f842984}')
PROPID_ACC_PARENT: Guid = Guid('{474c22b6-ffc2-467a-b1b5-e958b4657330}')
PROPID_ACC_NAV_UP: Guid = Guid('{016e1a2b-1a4e-4767-8612-3386f66935ec}')
PROPID_ACC_NAV_DOWN: Guid = Guid('{031670ed-3cdf-48d2-9613-138f2dd8a668}')
PROPID_ACC_NAV_LEFT: Guid = Guid('{228086cb-82f1-4a39-8705-dcdc0fff92f5}')
PROPID_ACC_NAV_RIGHT: Guid = Guid('{cd211d9f-e1cb-4fe5-a77c-920b884d095b}')
PROPID_ACC_NAV_PREV: Guid = Guid('{776d3891-c73b-4480-b3f6-076a16a15af6}')
PROPID_ACC_NAV_NEXT: Guid = Guid('{1cdc5455-8cd9-4c92-a371-3939a2fe3eee}')
PROPID_ACC_NAV_FIRSTCHILD: Guid = Guid('{cfd02558-557b-4c67-84f9-2a09fce40749}')
PROPID_ACC_NAV_LASTCHILD: Guid = Guid('{302ecaa5-48d5-4f8d-b671-1a8d20a77832}')
PROPID_ACC_ROLEMAP: Guid = Guid('{f79acda2-140d-4fe6-8914-208476328269}')
PROPID_ACC_VALUEMAP: Guid = Guid('{da1c3d79-fc5c-420e-b399-9d1533549e75}')
PROPID_ACC_STATEMAP: Guid = Guid('{43946c5e-0ac0-4042-b525-07bbdbe17fa7}')
PROPID_ACC_DESCRIPTIONMAP: Guid = Guid('{1ff1435f-8a14-477b-b226-a0abe279975d}')
PROPID_ACC_DODEFAULTACTION: Guid = Guid('{1ba09523-2e3b-49a6-a059-59682a3c48fd}')
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
RuntimeId_Property_GUID: Guid = Guid('{a39eebfa-7fba-4c89-b4d4-b99e2de7d160}')
BoundingRectangle_Property_GUID: Guid = Guid('{7bbfe8b2-3bfc-48dd-b729-c794b846e9a1}')
ProcessId_Property_GUID: Guid = Guid('{40499998-9c31-4245-a403-87320e59eaf6}')
ControlType_Property_GUID: Guid = Guid('{ca774fea-28ac-4bc2-94ca-acec6d6c10a3}')
LocalizedControlType_Property_GUID: Guid = Guid('{8763404f-a1bd-452a-89c4-3f01d3833806}')
Name_Property_GUID: Guid = Guid('{c3a6921b-4a99-44f1-bca6-61187052c431}')
AcceleratorKey_Property_GUID: Guid = Guid('{514865df-2557-4cb9-aeed-6ced084ce52c}')
AccessKey_Property_GUID: Guid = Guid('{06827b12-a7f9-4a15-917c-ffa5ad3eb0a7}')
HasKeyboardFocus_Property_GUID: Guid = Guid('{cf8afd39-3f46-4800-9656-b2bf12529905}')
IsKeyboardFocusable_Property_GUID: Guid = Guid('{f7b8552a-0859-4b37-b9cb-51e72092f29f}')
IsEnabled_Property_GUID: Guid = Guid('{2109427f-da60-4fed-bf1b-264bdce6eb3a}')
AutomationId_Property_GUID: Guid = Guid('{c82c0500-b60e-4310-a267-303c531f8ee5}')
ClassName_Property_GUID: Guid = Guid('{157b7215-894f-4b65-84e2-aac0da08b16b}')
HelpText_Property_GUID: Guid = Guid('{08555685-0977-45c7-a7a6-abaf5684121a}')
ClickablePoint_Property_GUID: Guid = Guid('{0196903b-b203-4818-a9f3-f08e675f2341}')
Culture_Property_GUID: Guid = Guid('{e2d74f27-3d79-4dc2-b88b-3044963a8afb}')
IsControlElement_Property_GUID: Guid = Guid('{95f35085-abcc-4afd-a5f4-dbb46c230fdb}')
IsContentElement_Property_GUID: Guid = Guid('{4bda64a8-f5d8-480b-8155-ef2e89adb672}')
LabeledBy_Property_GUID: Guid = Guid('{e5b8924b-fc8a-4a35-8031-cf78ac43e55e}')
IsPassword_Property_GUID: Guid = Guid('{e8482eb1-687c-497b-bebc-03be53ec1454}')
NewNativeWindowHandle_Property_GUID: Guid = Guid('{5196b33b-380a-4982-95e1-91f3ef60e024}')
ItemType_Property_GUID: Guid = Guid('{cdda434d-6222-413b-a68a-325dd1d40f39}')
IsOffscreen_Property_GUID: Guid = Guid('{03c3d160-db79-42db-a2ef-1c231eede507}')
Orientation_Property_GUID: Guid = Guid('{a01eee62-3884-4415-887e-678ec21e39ba}')
FrameworkId_Property_GUID: Guid = Guid('{dbfd9900-7e1a-4f58-b61b-7063120f773b}')
IsRequiredForForm_Property_GUID: Guid = Guid('{4f5f43cf-59fb-4bde-a270-602e5e1141e9}')
ItemStatus_Property_GUID: Guid = Guid('{51de0321-3973-43e7-8913-0b08e813c37f}')
AriaRole_Property_GUID: Guid = Guid('{dd207b95-be4a-4e0d-b727-63ace94b6916}')
AriaProperties_Property_GUID: Guid = Guid('{4213678c-e025-4922-beb5-e43ba08e6221}')
IsDataValidForForm_Property_GUID: Guid = Guid('{445ac684-c3fc-4dd9-acf8-845a579296ba}')
ControllerFor_Property_GUID: Guid = Guid('{51124c8a-a5d2-4f13-9be6-7fa8ba9d3a90}')
DescribedBy_Property_GUID: Guid = Guid('{7c5865b8-9992-40fd-8db0-6bf1d317f998}')
FlowsTo_Property_GUID: Guid = Guid('{e4f33d20-559a-47fb-a830-f9cb4ff1a70a}')
ProviderDescription_Property_GUID: Guid = Guid('{dca5708a-c16b-4cd9-b889-beb16a804904}')
OptimizeForVisualContent_Property_GUID: Guid = Guid('{6a852250-c75a-4e5d-b858-e381b0f78861}')
IsDockPatternAvailable_Property_GUID: Guid = Guid('{2600a4c4-2ff8-4c96-ae31-8fe619a13c6c}')
IsExpandCollapsePatternAvailable_Property_GUID: Guid = Guid('{929d3806-5287-4725-aa16-222afc63d595}')
IsGridItemPatternAvailable_Property_GUID: Guid = Guid('{5a43e524-f9a2-4b12-84c8-b48a3efedd34}')
IsGridPatternAvailable_Property_GUID: Guid = Guid('{5622c26c-f0ef-4f3b-97cb-714c0868588b}')
IsInvokePatternAvailable_Property_GUID: Guid = Guid('{4e725738-8364-4679-aa6c-f3f41931f750}')
IsMultipleViewPatternAvailable_Property_GUID: Guid = Guid('{ff0a31eb-8e25-469d-8d6e-e771a27c1b90}')
IsRangeValuePatternAvailable_Property_GUID: Guid = Guid('{fda4244a-eb4d-43ff-b5ad-ed36d373ec4c}')
IsScrollPatternAvailable_Property_GUID: Guid = Guid('{3ebb7b4a-828a-4b57-9d22-2fea1632ed0d}')
IsScrollItemPatternAvailable_Property_GUID: Guid = Guid('{1cad1a05-0927-4b76-97e1-0fcdb209b98a}')
IsSelectionItemPatternAvailable_Property_GUID: Guid = Guid('{8becd62d-0bc3-4109-bee2-8e6715290e68}')
IsSelectionPatternAvailable_Property_GUID: Guid = Guid('{f588acbe-c769-4838-9a60-2686dc1188c4}')
IsTablePatternAvailable_Property_GUID: Guid = Guid('{cb83575f-45c2-4048-9c76-159715a139df}')
IsTableItemPatternAvailable_Property_GUID: Guid = Guid('{eb36b40d-8ea4-489b-a013-e60d5951fe34}')
IsTextPatternAvailable_Property_GUID: Guid = Guid('{fbe2d69d-aff6-4a45-82e2-fc92a82f5917}')
IsTogglePatternAvailable_Property_GUID: Guid = Guid('{78686d53-fcd0-4b83-9b78-5832ce63bb5b}')
IsTransformPatternAvailable_Property_GUID: Guid = Guid('{a7f78804-d68b-4077-a5c6-7a5ea1ac31c5}')
IsValuePatternAvailable_Property_GUID: Guid = Guid('{0b5020a7-2119-473b-be37-5ceb98bbfb22}')
IsWindowPatternAvailable_Property_GUID: Guid = Guid('{e7a57bb1-5888-4155-98dc-b422fd57f2bc}')
IsLegacyIAccessiblePatternAvailable_Property_GUID: Guid = Guid('{d8ebd0c7-929a-4ee7-8d3a-d3d94413027b}')
IsItemContainerPatternAvailable_Property_GUID: Guid = Guid('{624b5ca7-fe40-4957-a019-20c4cf11920f}')
IsVirtualizedItemPatternAvailable_Property_GUID: Guid = Guid('{302cb151-2ac8-45d6-977b-d2b3a5a53f20}')
IsSynchronizedInputPatternAvailable_Property_GUID: Guid = Guid('{75d69cc5-d2bf-4943-876e-b45b62a6cc66}')
IsObjectModelPatternAvailable_Property_GUID: Guid = Guid('{6b21d89b-2841-412f-8ef2-15ca952318ba}')
IsAnnotationPatternAvailable_Property_GUID: Guid = Guid('{0b5b3238-6d5c-41b6-bcc4-5e807f6551c4}')
IsTextPattern2Available_Property_GUID: Guid = Guid('{41cf921d-e3f1-4b22-9c81-e1c3ed331c22}')
IsTextEditPatternAvailable_Property_GUID: Guid = Guid('{7843425c-8b32-484c-9ab5-e3200571ffda}')
IsCustomNavigationPatternAvailable_Property_GUID: Guid = Guid('{8f8e80d4-2351-48e0-874a-54aa7313889a}')
IsStylesPatternAvailable_Property_GUID: Guid = Guid('{27f353d3-459c-4b59-a490-50611dacafb5}')
IsSpreadsheetPatternAvailable_Property_GUID: Guid = Guid('{6ff43732-e4b4-4555-97bc-ecdbbc4d1888}')
IsSpreadsheetItemPatternAvailable_Property_GUID: Guid = Guid('{9fe79b2a-2f94-43fd-996b-549e316f4acd}')
IsTransformPattern2Available_Property_GUID: Guid = Guid('{25980b4b-be04-4710-ab4a-fda31dbd2895}')
IsTextChildPatternAvailable_Property_GUID: Guid = Guid('{559e65df-30ff-43b5-b5ed-5b283b80c7e9}')
IsDragPatternAvailable_Property_GUID: Guid = Guid('{e997a7b7-1d39-4ca7-be0f-277fcf5605cc}')
IsDropTargetPatternAvailable_Property_GUID: Guid = Guid('{0686b62e-8e19-4aaf-873d-384f6d3b92be}')
IsStructuredMarkupPatternAvailable_Property_GUID: Guid = Guid('{b0d4c196-2c0b-489c-b165-a405928c6f3d}')
IsPeripheral_Property_GUID: Guid = Guid('{da758276-7ed5-49d4-8e68-ecc9a2d300dd}')
PositionInSet_Property_GUID: Guid = Guid('{33d1dc54-641e-4d76-a6b1-13f341c1f896}')
SizeOfSet_Property_GUID: Guid = Guid('{1600d33c-3b9f-4369-9431-aa293f344cf1}')
Level_Property_GUID: Guid = Guid('{242ac529-cd36-400f-aad9-7876ef3af627}')
AnnotationTypes_Property_GUID: Guid = Guid('{64b71f76-53c4-4696-a219-20e940c9a176}')
AnnotationObjects_Property_GUID: Guid = Guid('{310910c8-7c6e-4f20-becd-4aaf6d191156}')
LandmarkType_Property_GUID: Guid = Guid('{454045f2-6f61-49f7-a4f8-b5f0cf82da1e}')
LocalizedLandmarkType_Property_GUID: Guid = Guid('{7ac81980-eafb-4fb2-bf91-f485bef5e8e1}')
FullDescription_Property_GUID: Guid = Guid('{0d4450ff-6aef-4f33-95dd-7befa72a4391}')
Value_Value_Property_GUID: Guid = Guid('{e95f5e64-269f-4a85-ba99-4092c3ea2986}')
Value_IsReadOnly_Property_GUID: Guid = Guid('{eb090f30-e24c-4799-a705-0d247bc037f8}')
RangeValue_Value_Property_GUID: Guid = Guid('{131f5d98-c50c-489d-abe5-ae220898c5f7}')
RangeValue_IsReadOnly_Property_GUID: Guid = Guid('{25fa1055-debf-4373-a79e-1f1a1908d3c4}')
RangeValue_Minimum_Property_GUID: Guid = Guid('{78cbd3b2-684d-4860-af93-d1f95cb022fd}')
RangeValue_Maximum_Property_GUID: Guid = Guid('{19319914-f979-4b35-a1a6-d37e05433473}')
RangeValue_LargeChange_Property_GUID: Guid = Guid('{a1f96325-3a3d-4b44-8e1f-4a46d9844019}')
RangeValue_SmallChange_Property_GUID: Guid = Guid('{81c2c457-3941-4107-9975-139760f7c072}')
Scroll_HorizontalScrollPercent_Property_GUID: Guid = Guid('{c7c13c0e-eb21-47ff-acc4-b5a3350f5191}')
Scroll_HorizontalViewSize_Property_GUID: Guid = Guid('{70c2e5d4-fcb0-4713-a9aa-af92ff79e4cd}')
Scroll_VerticalScrollPercent_Property_GUID: Guid = Guid('{6c8d7099-b2a8-4948-bff7-3cf9058bfefb}')
Scroll_VerticalViewSize_Property_GUID: Guid = Guid('{de6a2e22-d8c7-40c5-83ba-e5f681d53108}')
Scroll_HorizontallyScrollable_Property_GUID: Guid = Guid('{8b925147-28cd-49ae-bd63-f44118d2e719}')
Scroll_VerticallyScrollable_Property_GUID: Guid = Guid('{89164798-0068-4315-b89a-1e7cfbbc3dfc}')
Selection_Selection_Property_GUID: Guid = Guid('{aa6dc2a2-0e2b-4d38-96d5-34e470b81853}')
Selection_CanSelectMultiple_Property_GUID: Guid = Guid('{49d73da5-c883-4500-883d-8fcf8daf6cbe}')
Selection_IsSelectionRequired_Property_GUID: Guid = Guid('{b1ae4422-63fe-44e7-a5a5-a738c829b19a}')
Grid_RowCount_Property_GUID: Guid = Guid('{2a9505bf-c2eb-4fb6-b356-8245ae53703e}')
Grid_ColumnCount_Property_GUID: Guid = Guid('{fe96f375-44aa-4536-ac7a-2a75d71a3efc}')
GridItem_Row_Property_GUID: Guid = Guid('{6223972a-c945-4563-9329-fdc974af2553}')
GridItem_Column_Property_GUID: Guid = Guid('{c774c15c-62c0-4519-8bdc-47be573c8ad5}')
GridItem_RowSpan_Property_GUID: Guid = Guid('{4582291c-466b-4e93-8e83-3d1715ec0c5e}')
GridItem_ColumnSpan_Property_GUID: Guid = Guid('{583ea3f5-86d0-4b08-a6ec-2c5463ffc109}')
GridItem_Parent_Property_GUID: Guid = Guid('{9d912252-b97f-4ecc-8510-ea0e33427c72}')
Dock_DockPosition_Property_GUID: Guid = Guid('{6d67f02e-c0b0-4b10-b5b9-18d6ecf98760}')
ExpandCollapse_ExpandCollapseState_Property_GUID: Guid = Guid('{275a4c48-85a7-4f69-aba0-af157610002b}')
MultipleView_CurrentView_Property_GUID: Guid = Guid('{7a81a67a-b94f-4875-918b-65c8d2f998e5}')
MultipleView_SupportedViews_Property_GUID: Guid = Guid('{8d5db9fd-ce3c-4ae7-b788-400a3c645547}')
Window_CanMaximize_Property_GUID: Guid = Guid('{64fff53f-635d-41c1-950c-cb5adfbe28e3}')
Window_CanMinimize_Property_GUID: Guid = Guid('{b73b4625-5988-4b97-b4c2-a6fe6e78c8c6}')
Window_WindowVisualState_Property_GUID: Guid = Guid('{4ab7905f-e860-453e-a30a-f6431e5daad5}')
Window_WindowInteractionState_Property_GUID: Guid = Guid('{4fed26a4-0455-4fa2-b21c-c4da2db1ff9c}')
Window_IsModal_Property_GUID: Guid = Guid('{ff4e6892-37b9-4fca-8532-ffe674ecfeed}')
Window_IsTopmost_Property_GUID: Guid = Guid('{ef7d85d3-0937-4962-9241-b62345f24041}')
SelectionItem_IsSelected_Property_GUID: Guid = Guid('{f122835f-cd5f-43df-b79d-4b849e9e6020}')
SelectionItem_SelectionContainer_Property_GUID: Guid = Guid('{a4365b6e-9c1e-4b63-8b53-c2421dd1e8fb}')
Table_RowHeaders_Property_GUID: Guid = Guid('{d9e35b87-6eb8-4562-aac6-a8a9075236a8}')
Table_ColumnHeaders_Property_GUID: Guid = Guid('{aff1d72b-968d-42b1-b459-150b299da664}')
Table_RowOrColumnMajor_Property_GUID: Guid = Guid('{83be75c3-29fe-4a30-85e1-2a6277fd106e}')
TableItem_RowHeaderItems_Property_GUID: Guid = Guid('{b3f853a0-0574-4cd8-bcd7-ed5923572d97}')
TableItem_ColumnHeaderItems_Property_GUID: Guid = Guid('{967a56a3-74b6-431e-8de6-99c411031c58}')
Toggle_ToggleState_Property_GUID: Guid = Guid('{b23cdc52-22c2-4c6c-9ded-f5c422479ede}')
Transform_CanMove_Property_GUID: Guid = Guid('{1b75824d-208b-4fdf-bccd-f1f4e5741f4f}')
Transform_CanResize_Property_GUID: Guid = Guid('{bb98dca5-4c1a-41d4-a4f6-ebc128644180}')
Transform_CanRotate_Property_GUID: Guid = Guid('{10079b48-3849-476f-ac96-44a95c8440d9}')
LegacyIAccessible_ChildId_Property_GUID: Guid = Guid('{9a191b5d-9ef2-4787-a459-dcde885dd4e8}')
LegacyIAccessible_Name_Property_GUID: Guid = Guid('{caeb063d-40ae-4869-aa5a-1b8e5d666739}')
LegacyIAccessible_Value_Property_GUID: Guid = Guid('{b5c5b0b6-8217-4a77-97a5-190a85ed0156}')
LegacyIAccessible_Description_Property_GUID: Guid = Guid('{46448418-7d70-4ea9-9d27-b7e775cf2ad7}')
LegacyIAccessible_Role_Property_GUID: Guid = Guid('{6856e59f-cbaf-4e31-93e8-bcbf6f7e491c}')
LegacyIAccessible_State_Property_GUID: Guid = Guid('{df985854-2281-4340-ab9c-c60e2c5803f6}')
LegacyIAccessible_Help_Property_GUID: Guid = Guid('{94402352-161c-4b77-a98d-a872cc33947a}')
LegacyIAccessible_KeyboardShortcut_Property_GUID: Guid = Guid('{8f6909ac-00b8-4259-a41c-966266d43a8a}')
LegacyIAccessible_Selection_Property_GUID: Guid = Guid('{8aa8b1e0-0891-40cc-8b06-90d7d4166219}')
LegacyIAccessible_DefaultAction_Property_GUID: Guid = Guid('{3b331729-eaad-4502-b85f-92615622913c}')
Annotation_AnnotationTypeId_Property_GUID: Guid = Guid('{20ae484f-69ef-4c48-8f5b-c4938b206ac7}')
Annotation_AnnotationTypeName_Property_GUID: Guid = Guid('{9b818892-5ac9-4af9-aa96-f58a77b058e3}')
Annotation_Author_Property_GUID: Guid = Guid('{7a528462-9c5c-4a03-a974-8b307a9937f2}')
Annotation_DateTime_Property_GUID: Guid = Guid('{99b5ca5d-1acf-414b-a4d0-6b350b047578}')
Annotation_Target_Property_GUID: Guid = Guid('{b71b302d-2104-44ad-9c5c-092b4907d70f}')
Styles_StyleId_Property_GUID: Guid = Guid('{da82852f-3817-4233-82af-02279e72cc77}')
Styles_StyleName_Property_GUID: Guid = Guid('{1c12b035-05d1-4f55-9e8e-1489f3ff550d}')
Styles_FillColor_Property_GUID: Guid = Guid('{63eff97a-a1c5-4b1d-84eb-b765f2edd632}')
Styles_FillPatternStyle_Property_GUID: Guid = Guid('{81cf651f-482b-4451-a30a-e1545e554fb8}')
Styles_Shape_Property_GUID: Guid = Guid('{c71a23f8-778c-400d-8458-3b543e526984}')
Styles_FillPatternColor_Property_GUID: Guid = Guid('{939a59fe-8fbd-4e75-a271-ac4595195163}')
Styles_ExtendedProperties_Property_GUID: Guid = Guid('{f451cda0-ba0a-4681-b0b0-0dbdb53e58f3}')
SpreadsheetItem_Formula_Property_GUID: Guid = Guid('{e602e47d-1b47-4bea-87cf-3b0b0b5c15b6}')
SpreadsheetItem_AnnotationObjects_Property_GUID: Guid = Guid('{a3194c38-c9bc-4604-9396-ae3f9f457f7b}')
SpreadsheetItem_AnnotationTypes_Property_GUID: Guid = Guid('{c70c51d0-d602-4b45-afbc-b4712b96d72b}')
Transform2_CanZoom_Property_GUID: Guid = Guid('{f357e890-a756-4359-9ca6-86702bf8f381}')
LiveSetting_Property_GUID: Guid = Guid('{c12bcd8e-2a8e-4950-8ae7-3625111d58eb}')
Drag_IsGrabbed_Property_GUID: Guid = Guid('{45f206f3-75cc-4cca-a9b9-fcdfb982d8a2}')
Drag_GrabbedItems_Property_GUID: Guid = Guid('{77c1562c-7b86-4b21-9ed7-3cefda6f4c43}')
Drag_DropEffect_Property_GUID: Guid = Guid('{646f2779-48d3-4b23-8902-4bf100005df3}')
Drag_DropEffects_Property_GUID: Guid = Guid('{f5d61156-7ce6-49be-a836-9269dcec920f}')
DropTarget_DropTargetEffect_Property_GUID: Guid = Guid('{8bb75975-a0ca-4981-b818-87fc66e9509d}')
DropTarget_DropTargetEffects_Property_GUID: Guid = Guid('{bc1dd4ed-cb89-45f1-a592-e03b08ae790f}')
Transform2_ZoomLevel_Property_GUID: Guid = Guid('{eee29f1a-f4a2-4b5b-ac65-95cf93283387}')
Transform2_ZoomMinimum_Property_GUID: Guid = Guid('{742ccc16-4ad1-4e07-96fe-b122c6e6b22b}')
Transform2_ZoomMaximum_Property_GUID: Guid = Guid('{42ab6b77-ceb0-4eca-b82a-6cfa5fa1fc08}')
FlowsFrom_Property_GUID: Guid = Guid('{05c6844f-19de-48f8-95fa-880d5b0fd615}')
FillColor_Property_GUID: Guid = Guid('{6e0ec4d0-e2a8-4a56-9de7-953389933b39}')
OutlineColor_Property_GUID: Guid = Guid('{c395d6c0-4b55-4762-a073-fd303a634f52}')
FillType_Property_GUID: Guid = Guid('{c6fc74e4-8cb9-429c-a9e1-9bc4ac372b62}')
VisualEffects_Property_GUID: Guid = Guid('{e61a8565-aad9-46d7-9e70-4e8a8420d420}')
OutlineThickness_Property_GUID: Guid = Guid('{13e67cc7-dac2-4888-bdd3-375c62fa9618}')
CenterPoint_Property_GUID: Guid = Guid('{0cb00c08-540c-4edb-9445-26359ea69785}')
Rotation_Property_GUID: Guid = Guid('{767cdc7d-aec0-4110-ad32-30edd403492e}')
Size_Property_GUID: Guid = Guid('{2b5f761d-f885-4404-973f-9b1d98e36d8f}')
ToolTipOpened_Event_GUID: Guid = Guid('{3f4b97ff-2edc-451d-bca4-95a3188d5b03}')
ToolTipClosed_Event_GUID: Guid = Guid('{276d71ef-24a9-49b6-8e97-da98b401bbcd}')
StructureChanged_Event_GUID: Guid = Guid('{59977961-3edd-4b11-b13b-676b2a2a6ca9}')
MenuOpened_Event_GUID: Guid = Guid('{ebe2e945-66ca-4ed1-9ff8-2ad7df0a1b08}')
AutomationPropertyChanged_Event_GUID: Guid = Guid('{2527fba1-8d7a-4630-a4cc-e66315942f52}')
AutomationFocusChanged_Event_GUID: Guid = Guid('{b68a1f17-f60d-41a7-a3cc-b05292155fe0}')
ActiveTextPositionChanged_Event_GUID: Guid = Guid('{a5c09e9c-c77d-4f25-b491-e5bb7017cbd4}')
AsyncContentLoaded_Event_GUID: Guid = Guid('{5fdee11c-d2fa-4fb9-904e-5cbee894d5ef}')
MenuClosed_Event_GUID: Guid = Guid('{3cf1266e-1582-4041-acd7-88a35a965297}')
LayoutInvalidated_Event_GUID: Guid = Guid('{ed7d6544-a6bd-4595-9bae-3d28946cc715}')
Invoke_Invoked_Event_GUID: Guid = Guid('{dfd699f0-c915-49dd-b422-dde785c3d24b}')
SelectionItem_ElementAddedToSelectionEvent_Event_GUID: Guid = Guid('{3c822dd1-c407-4dba-91dd-79d4aed0aec6}')
SelectionItem_ElementRemovedFromSelectionEvent_Event_GUID: Guid = Guid('{097fa8a9-7079-41af-8b9c-0934d8305e5c}')
SelectionItem_ElementSelectedEvent_Event_GUID: Guid = Guid('{b9c7dbfb-4ebe-4532-aaf4-008cf647233c}')
Selection_InvalidatedEvent_Event_GUID: Guid = Guid('{cac14904-16b4-4b53-8e47-4cb1df267bb7}')
Text_TextSelectionChangedEvent_Event_GUID: Guid = Guid('{918edaa1-71b3-49ae-9741-79beb8d358f3}')
Text_TextChangedEvent_Event_GUID: Guid = Guid('{4a342082-f483-48c4-ac11-a84b435e2a84}')
Window_WindowOpened_Event_GUID: Guid = Guid('{d3e81d06-de45-4f2f-9633-de9e02fb65af}')
Window_WindowClosed_Event_GUID: Guid = Guid('{edf141f8-fa67-4e22-bbf7-944e05735ee2}')
MenuModeStart_Event_GUID: Guid = Guid('{18d7c631-166a-4ac9-ae3b-ef4b5420e681}')
MenuModeEnd_Event_GUID: Guid = Guid('{9ecd4c9f-80dd-47b8-8267-5aec06bb2cff}')
InputReachedTarget_Event_GUID: Guid = Guid('{93ed549a-0549-40f0-bedb-28e44f7de2a3}')
InputReachedOtherElement_Event_GUID: Guid = Guid('{ed201d8a-4e6c-415e-a874-2460c9b66ba8}')
InputDiscarded_Event_GUID: Guid = Guid('{7f36c367-7b18-417c-97e3-9d58ddc944ab}')
SystemAlert_Event_GUID: Guid = Guid('{d271545d-7a3a-47a7-8474-81d29a2451c9}')
LiveRegionChanged_Event_GUID: Guid = Guid('{102d5e90-e6a9-41b6-b1c5-a9b1929d9510}')
HostedFragmentRootsInvalidated_Event_GUID: Guid = Guid('{e6bdb03e-0921-4ec5-8dcf-eae877b0426b}')
Drag_DragStart_Event_GUID: Guid = Guid('{883a480b-3aa9-429d-95e4-d9c8d011f0dd}')
Drag_DragCancel_Event_GUID: Guid = Guid('{c3ede6fa-3451-4e0f-9e71-df9c280a4657}')
Drag_DragComplete_Event_GUID: Guid = Guid('{38e96188-ef1f-463e-91ca-3a7792c29caf}')
DropTarget_DragEnter_Event_GUID: Guid = Guid('{aad9319b-032c-4a88-961d-1cf579581e34}')
DropTarget_DragLeave_Event_GUID: Guid = Guid('{0f82eb15-24a2-4988-9217-de162aee272b}')
DropTarget_Dropped_Event_GUID: Guid = Guid('{622cead8-1edb-4a3d-abbc-be2211ff68b5}')
StructuredMarkup_CompositionComplete_Event_GUID: Guid = Guid('{c48a3c17-677a-4047-a68d-fc1257528aef}')
StructuredMarkup_Deleted_Event_GUID: Guid = Guid('{f9d0a020-e1c1-4ecf-b9aa-52efde7e41e1}')
StructuredMarkup_SelectionChanged_Event_GUID: Guid = Guid('{a7c815f7-ff9f-41c7-a3a7-ab6cbfdb4903}')
Invoke_Pattern_GUID: Guid = Guid('{d976c2fc-66ea-4a6e-b28f-c24c7546ad37}')
Selection_Pattern_GUID: Guid = Guid('{66e3b7e8-d821-4d25-8761-435d2c8b253f}')
Value_Pattern_GUID: Guid = Guid('{17faad9e-c877-475b-b933-77332779b637}')
RangeValue_Pattern_GUID: Guid = Guid('{18b00d87-b1c9-476a-bfbd-5f0bdb926f63}')
Scroll_Pattern_GUID: Guid = Guid('{895fa4b4-759d-4c50-8e15-03460672003c}')
ExpandCollapse_Pattern_GUID: Guid = Guid('{ae05efa2-f9d1-428a-834c-53a5c52f9b8b}')
Grid_Pattern_GUID: Guid = Guid('{260a2ccb-93a8-4e44-a4c1-3df397f2b02b}')
GridItem_Pattern_GUID: Guid = Guid('{f2d5c877-a462-4957-a2a5-2c96b303bc63}')
MultipleView_Pattern_GUID: Guid = Guid('{547a6ae4-113f-47c4-850f-db4dfa466b1d}')
Window_Pattern_GUID: Guid = Guid('{27901735-c760-4994-ad11-5919e606b110}')
SelectionItem_Pattern_GUID: Guid = Guid('{9bc64eeb-87c7-4b28-94bb-4d9fa437b6ef}')
Dock_Pattern_GUID: Guid = Guid('{9cbaa846-83c8-428d-827f-7e6063fe0620}')
Table_Pattern_GUID: Guid = Guid('{c415218e-a028-461e-aa92-8f925cf79351}')
TableItem_Pattern_GUID: Guid = Guid('{df1343bd-1888-4a29-a50c-b92e6de37f6f}')
Text_Pattern_GUID: Guid = Guid('{8615f05d-7de5-44fd-a679-2ca4b46033a8}')
Toggle_Pattern_GUID: Guid = Guid('{0b419760-e2f4-43ff-8c5f-9457c82b56e9}')
Transform_Pattern_GUID: Guid = Guid('{24b46fdb-587e-49f1-9c4a-d8e98b664b7b}')
ScrollItem_Pattern_GUID: Guid = Guid('{4591d005-a803-4d5c-b4d5-8d2800f906a7}')
LegacyIAccessible_Pattern_GUID: Guid = Guid('{54cc0a9f-3395-48af-ba8d-73f85690f3e0}')
ItemContainer_Pattern_GUID: Guid = Guid('{3d13da0f-8b9a-4a99-85fa-c5c9a69f1ed4}')
VirtualizedItem_Pattern_GUID: Guid = Guid('{f510173e-2e71-45e9-a6e5-62f6ed8289d5}')
SynchronizedInput_Pattern_GUID: Guid = Guid('{05c288a6-c47b-488b-b653-33977a551b8b}')
ObjectModel_Pattern_GUID: Guid = Guid('{3e04acfe-08fc-47ec-96bc-353fa3b34aa7}')
Annotation_Pattern_GUID: Guid = Guid('{f6c72ad7-356c-4850-9291-316f608a8c84}')
Text_Pattern2_GUID: Guid = Guid('{498479a2-5b22-448d-b6e4-647490860698}')
TextEdit_Pattern_GUID: Guid = Guid('{69f3ff89-5af9-4c75-9340-f2de292e4591}')
CustomNavigation_Pattern_GUID: Guid = Guid('{afea938a-621e-4054-bb2c-2f46114dac3f}')
Styles_Pattern_GUID: Guid = Guid('{1ae62655-da72-4d60-a153-e5aa6988e3bf}')
Spreadsheet_Pattern_GUID: Guid = Guid('{6a5b24c9-9d1e-4b85-9e44-c02e3169b10b}')
SpreadsheetItem_Pattern_GUID: Guid = Guid('{32cf83ff-f1a8-4a8c-8658-d47ba74e20ba}')
Tranform_Pattern2_GUID: Guid = Guid('{8afcfd07-a369-44de-988b-2f7ff49fb8a8}')
TextChild_Pattern_GUID: Guid = Guid('{7533cab7-3bfe-41ef-9e85-e2638cbe169e}')
Drag_Pattern_GUID: Guid = Guid('{c0bee21f-ccb3-4fed-995b-114f6e3d2728}')
DropTarget_Pattern_GUID: Guid = Guid('{0bcbec56-bd34-4b7b-9fd5-2659905ea3dc}')
StructuredMarkup_Pattern_GUID: Guid = Guid('{abbd0878-8665-4f5c-94fc-36e7d8bb706b}')
Button_Control_GUID: Guid = Guid('{5a78e369-c6a1-4f33-a9d7-79f20d0c788e}')
Calendar_Control_GUID: Guid = Guid('{8913eb88-00e5-46bc-8e4e-14a786e165a1}')
CheckBox_Control_GUID: Guid = Guid('{fb50f922-a3db-49c0-8bc3-06dad55778e2}')
ComboBox_Control_GUID: Guid = Guid('{54cb426c-2f33-4fff-aaa1-aef60dac5deb}')
Edit_Control_GUID: Guid = Guid('{6504a5c8-2c86-4f87-ae7b-1abddc810cf9}')
Hyperlink_Control_GUID: Guid = Guid('{8a56022c-b00d-4d15-8ff0-5b6b266e5e02}')
Image_Control_GUID: Guid = Guid('{2d3736e4-6b16-4c57-a962-f93260a75243}')
ListItem_Control_GUID: Guid = Guid('{7b3717f2-44d1-4a58-98a8-f12a9b8f78e2}')
List_Control_GUID: Guid = Guid('{9b149ee1-7cca-4cfc-9af1-cac7bddd3031}')
Menu_Control_GUID: Guid = Guid('{2e9b1440-0ea8-41fd-b374-c1ea6f503cd1}')
MenuBar_Control_GUID: Guid = Guid('{cc384250-0e7b-4ae8-95ae-a08f261b52ee}')
MenuItem_Control_GUID: Guid = Guid('{f45225d3-d0a0-49d8-9834-9a000d2aeddc}')
ProgressBar_Control_GUID: Guid = Guid('{228c9f86-c36c-47bb-9fb6-a5834bfc53a4}')
RadioButton_Control_GUID: Guid = Guid('{3bdb49db-fe2c-4483-b3e1-e57f219440c6}')
ScrollBar_Control_GUID: Guid = Guid('{daf34b36-5065-4946-b22f-92595fc0751a}')
Slider_Control_GUID: Guid = Guid('{b033c24b-3b35-4cea-b609-763682fa660b}')
Spinner_Control_GUID: Guid = Guid('{60cc4b38-3cb1-4161-b442-c6b726c17825}')
StatusBar_Control_GUID: Guid = Guid('{d45e7d1b-5873-475f-95a4-0433e1f1b00a}')
Tab_Control_GUID: Guid = Guid('{38cd1f2d-337a-4bd2-a5e3-adb469e30bd3}')
TabItem_Control_GUID: Guid = Guid('{2c6a634f-921b-4e6e-b26e-08fcb0798f4c}')
Text_Control_GUID: Guid = Guid('{ae9772dc-d331-4f09-be20-7e6dfaf07b0a}')
ToolBar_Control_GUID: Guid = Guid('{8f06b751-e182-4e98-8893-2284543a7dce}')
ToolTip_Control_GUID: Guid = Guid('{05ddc6d1-2137-4768-98ea-73f52f7134f3}')
Tree_Control_GUID: Guid = Guid('{7561349c-d241-43f4-9908-b5f091bee611}')
TreeItem_Control_GUID: Guid = Guid('{62c9feb9-8ffc-4878-a3a4-96b030315c18}')
Custom_Control_GUID: Guid = Guid('{f29ea0c3-adb7-430a-ba90-e52c7313e6ed}')
Group_Control_GUID: Guid = Guid('{ad50aa1c-e8c8-4774-ae1b-dd86df0b3bdc}')
Thumb_Control_GUID: Guid = Guid('{701ca877-e310-4dd6-b644-797e4faea213}')
DataGrid_Control_GUID: Guid = Guid('{84b783af-d103-4b0a-8415-e73942410f4b}')
DataItem_Control_GUID: Guid = Guid('{a0177842-d94f-42a5-814b-6068addc8da5}')
Document_Control_GUID: Guid = Guid('{3cd6bb6f-6f08-4562-b229-e4e2fc7a9eb4}')
SplitButton_Control_GUID: Guid = Guid('{7011f01f-4ace-4901-b461-920a6f1ca650}')
Window_Control_GUID: Guid = Guid('{e13a7242-f462-4f4d-aec1-53b28d6c3290}')
Pane_Control_GUID: Guid = Guid('{5c2b3f5b-9182-42a3-8dec-8c04c1ee634d}')
Header_Control_GUID: Guid = Guid('{5b90cbce-78fb-4614-82b6-554d74718e67}')
HeaderItem_Control_GUID: Guid = Guid('{e6bc12cb-7c8e-49cf-b168-4a93a32bebb0}')
Table_Control_GUID: Guid = Guid('{773bfa0e-5bc4-4deb-921b-de7b3206229e}')
TitleBar_Control_GUID: Guid = Guid('{98aa55bf-3bb0-4b65-836e-2ea30dbc171f}')
Separator_Control_GUID: Guid = Guid('{8767eba3-2a63-4ab0-ac8d-aa50e23de978}')
SemanticZoom_Control_GUID: Guid = Guid('{5fd34a43-061e-42c8-b589-9dccf74bc43a}')
AppBar_Control_GUID: Guid = Guid('{6114908d-cc02-4d37-875b-b530c7139554}')
Text_AnimationStyle_Attribute_GUID: Guid = Guid('{628209f0-7c9a-4d57-be64-1f1836571ff5}')
Text_BackgroundColor_Attribute_GUID: Guid = Guid('{fdc49a07-583d-4f17-ad27-77fc832a3c0b}')
Text_BulletStyle_Attribute_GUID: Guid = Guid('{c1097c90-d5c4-4237-9781-3bec8ba54e48}')
Text_CapStyle_Attribute_GUID: Guid = Guid('{fb059c50-92cc-49a5-ba8f-0aa872bba2f3}')
Text_Culture_Attribute_GUID: Guid = Guid('{c2025af9-a42d-4ced-a1fb-c6746315222e}')
Text_FontName_Attribute_GUID: Guid = Guid('{64e63ba8-f2e5-476e-a477-1734feaaf726}')
Text_FontSize_Attribute_GUID: Guid = Guid('{dc5eeeff-0506-4673-93f2-377e4a8e01f1}')
Text_FontWeight_Attribute_GUID: Guid = Guid('{6fc02359-b316-4f5f-b401-f1ce55741853}')
Text_ForegroundColor_Attribute_GUID: Guid = Guid('{72d1c95d-5e60-471a-96b1-6c1b3b77a436}')
Text_HorizontalTextAlignment_Attribute_GUID: Guid = Guid('{04ea6161-fba3-477a-952a-bb326d026a5b}')
Text_IndentationFirstLine_Attribute_GUID: Guid = Guid('{206f9ad5-c1d3-424a-8182-6da9a7f3d632}')
Text_IndentationLeading_Attribute_GUID: Guid = Guid('{5cf66bac-2d45-4a4b-b6c9-f7221d2815b0}')
Text_IndentationTrailing_Attribute_GUID: Guid = Guid('{97ff6c0f-1ce4-408a-b67b-94d83eb69bf2}')
Text_IsHidden_Attribute_GUID: Guid = Guid('{360182fb-bdd7-47f6-ab69-19e33f8a3344}')
Text_IsItalic_Attribute_GUID: Guid = Guid('{fce12a56-1336-4a34-9663-1bab47239320}')
Text_IsReadOnly_Attribute_GUID: Guid = Guid('{a738156b-ca3e-495e-9514-833c440feb11}')
Text_IsSubscript_Attribute_GUID: Guid = Guid('{f0ead858-8f53-413c-873f-1a7d7f5e0de4}')
Text_IsSuperscript_Attribute_GUID: Guid = Guid('{da706ee4-b3aa-4645-a41f-cd25157dea76}')
Text_MarginBottom_Attribute_GUID: Guid = Guid('{7ee593c4-72b4-4cac-9271-3ed24b0e4d42}')
Text_MarginLeading_Attribute_GUID: Guid = Guid('{9e9242d0-5ed0-4900-8e8a-eecc03835afc}')
Text_MarginTop_Attribute_GUID: Guid = Guid('{683d936f-c9b9-4a9a-b3d9-d20d33311e2a}')
Text_MarginTrailing_Attribute_GUID: Guid = Guid('{af522f98-999d-40af-a5b2-0169d0342002}')
Text_OutlineStyles_Attribute_GUID: Guid = Guid('{5b675b27-db89-46fe-970c-614d523bb97d}')
Text_OverlineColor_Attribute_GUID: Guid = Guid('{83ab383a-fd43-40da-ab3e-ecf8165cbb6d}')
Text_OverlineStyle_Attribute_GUID: Guid = Guid('{0a234d66-617e-427f-871d-e1ff1e0c213f}')
Text_StrikethroughColor_Attribute_GUID: Guid = Guid('{bfe15a18-8c41-4c5a-9a0b-04af0e07f487}')
Text_StrikethroughStyle_Attribute_GUID: Guid = Guid('{72913ef1-da00-4f01-899c-ac5a8577a307}')
Text_Tabs_Attribute_GUID: Guid = Guid('{2e68d00b-92fe-42d8-899a-a784aa4454a1}')
Text_TextFlowDirections_Attribute_GUID: Guid = Guid('{8bdf8739-f420-423e-af77-20a5d973a907}')
Text_UnderlineColor_Attribute_GUID: Guid = Guid('{bfa12c73-fde2-4473-bf64-1036d6aa0f45}')
Text_UnderlineStyle_Attribute_GUID: Guid = Guid('{5f3b21c0-ede4-44bd-9c36-3853038cbfeb}')
Text_AnnotationTypes_Attribute_GUID: Guid = Guid('{ad2eb431-ee4e-4be1-a7ba-5559155a73ef}')
Text_AnnotationObjects_Attribute_GUID: Guid = Guid('{ff41cf68-e7ab-40b9-8c72-72a8ed94017d}')
Text_StyleName_Attribute_GUID: Guid = Guid('{22c9e091-4d66-45d8-a828-737bab4c98a7}')
Text_StyleId_Attribute_GUID: Guid = Guid('{14c300de-c32b-449b-ab7c-b0e0789aea5d}')
Text_Link_Attribute_GUID: Guid = Guid('{b38ef51d-9e8d-4e46-9144-56ebe177329b}')
Text_IsActive_Attribute_GUID: Guid = Guid('{f5a4e533-e1b8-436b-935d-b57aa3f558c4}')
Text_SelectionActiveEnd_Attribute_GUID: Guid = Guid('{1f668cc3-9bbf-416b-b0a2-f89f86f6612c}')
Text_CaretPosition_Attribute_GUID: Guid = Guid('{b227b131-9889-4752-a91b-733efdc5c5a0}')
Text_CaretBidiMode_Attribute_GUID: Guid = Guid('{929ee7a6-51d3-4715-96dc-b694fa24a168}')
Text_BeforeParagraphSpacing_Attribute_GUID: Guid = Guid('{be7b0ab1-c822-4a24-85e9-c8f2650fc79c}')
Text_AfterParagraphSpacing_Attribute_GUID: Guid = Guid('{588cbb38-e62f-497c-b5d1-ccdf0ee823d8}')
Text_LineSpacing_Attribute_GUID: Guid = Guid('{63ff70ae-d943-4b47-8ab7-a7a033d3214b}')
Text_BeforeSpacing_Attribute_GUID: Guid = Guid('{be7b0ab1-c822-4a24-85e9-c8f2650fc79c}')
Text_AfterSpacing_Attribute_GUID: Guid = Guid('{588cbb38-e62f-497c-b5d1-ccdf0ee823d8}')
Text_SayAsInterpretAs_Attribute_GUID: Guid = Guid('{b38ad6ac-eee1-4b6e-88cc-014cefa93fcb}')
TextEdit_TextChanged_Event_GUID: Guid = Guid('{120b0308-ec22-4eb8-9c98-9867cda1b165}')
TextEdit_ConversionTargetChanged_Event_GUID: Guid = Guid('{3388c183-ed4f-4c8b-9baa-364d51d8847f}')
Changes_Event_GUID: Guid = Guid('{7df26714-614f-4e05-9488-716c5ba19436}')
Annotation_Custom_GUID: Guid = Guid('{9ec82750-3931-4952-85bc-1dbff78a43e3}')
Annotation_SpellingError_GUID: Guid = Guid('{ae85567e-9ece-423f-81b7-96c43d53e50e}')
Annotation_GrammarError_GUID: Guid = Guid('{757a048d-4518-41c6-854c-dc009b7cfb53}')
Annotation_Comment_GUID: Guid = Guid('{fd2fda30-26b3-4c06-8bc7-98f1532e46fd}')
Annotation_FormulaError_GUID: Guid = Guid('{95611982-0cab-46d5-a2f0-e30d1905f8bf}')
Annotation_TrackChanges_GUID: Guid = Guid('{21e6e888-dc14-4016-ac27-190553c8c470}')
Annotation_Header_GUID: Guid = Guid('{867b409b-b216-4472-a219-525e310681f8}')
Annotation_Footer_GUID: Guid = Guid('{cceab046-1833-47aa-8080-701ed0b0c832}')
Annotation_Highlighted_GUID: Guid = Guid('{757c884e-8083-4081-8b9c-e87f5072f0e4}')
Annotation_Endnote_GUID: Guid = Guid('{7565725c-2d99-4839-960d-33d3b866aba5}')
Annotation_Footnote_GUID: Guid = Guid('{3de10e21-4125-42db-8620-be8083080624}')
Annotation_InsertionChange_GUID: Guid = Guid('{0dbeb3a6-df15-4164-a3c0-e21a8ce931c4}')
Annotation_DeletionChange_GUID: Guid = Guid('{be3d5b05-951d-42e7-901d-adc8c2cf34d0}')
Annotation_MoveChange_GUID: Guid = Guid('{9da587eb-23e5-4490-b385-1a22ddc8b187}')
Annotation_FormatChange_GUID: Guid = Guid('{eb247345-d4f1-41ce-8e52-f79b69635e48}')
Annotation_UnsyncedChange_GUID: Guid = Guid('{1851116a-0e47-4b30-8cb5-d7dae4fbcd1b}')
Annotation_EditingLockedChange_GUID: Guid = Guid('{c31f3e1c-7423-4dac-8348-41f099ff6f64}')
Annotation_ExternalChange_GUID: Guid = Guid('{75a05b31-5f11-42fd-887d-dfa010db2392}')
Annotation_ConflictingChange_GUID: Guid = Guid('{98af8802-517c-459f-af13-016d3fab877e}')
Annotation_Author_GUID: Guid = Guid('{f161d3a7-f81b-4128-b17f-71f690914520}')
Annotation_AdvancedProofingIssue_GUID: Guid = Guid('{dac7b72c-c0f2-4b84-b90d-5fafc0f0ef1c}')
Annotation_DataValidationError_GUID: Guid = Guid('{c8649fa8-9775-437e-ad46-e709d93c2343}')
Annotation_CircularReferenceError_GUID: Guid = Guid('{25bd9cf4-1745-4659-ba67-727f0318c616}')
Annotation_Mathematics_GUID: Guid = Guid('{eaab634b-26d0-40c1-8073-57ca1c633c9b}')
Annotation_Sensitive_GUID: Guid = Guid('{37f4c04f-0f12-4464-929c-828fd15292e3}')
Changes_Summary_GUID: Guid = Guid('{313d65a6-e60f-4d62-9861-55afd728d207}')
StyleId_Custom_GUID: Guid = Guid('{ef2edd3e-a999-4b7c-a378-09bbd52a3516}')
StyleId_Heading1_GUID: Guid = Guid('{7f7e8f69-6866-4621-930c-9a5d0ca5961c}')
StyleId_Heading2_GUID: Guid = Guid('{baa9b241-5c69-469d-85ad-474737b52b14}')
StyleId_Heading3_GUID: Guid = Guid('{bf8be9d2-d8b8-4ec5-8c52-9cfb0d035970}')
StyleId_Heading4_GUID: Guid = Guid('{8436ffc0-9578-45fc-83a4-ff40053315dd}')
StyleId_Heading5_GUID: Guid = Guid('{909f424d-0dbf-406e-97bb-4e773d9798f7}')
StyleId_Heading6_GUID: Guid = Guid('{89d23459-5d5b-4824-a420-11d3ed82e40f}')
StyleId_Heading7_GUID: Guid = Guid('{a3790473-e9ae-422d-b8e3-3b675c6181a4}')
StyleId_Heading8_GUID: Guid = Guid('{2bc14145-a40c-4881-84ae-f2235685380c}')
StyleId_Heading9_GUID: Guid = Guid('{c70d9133-bb2a-43d3-8ac6-33657884b0f0}')
StyleId_Title_GUID: Guid = Guid('{15d8201a-ffcf-481f-b0a1-30b63be98f07}')
StyleId_Subtitle_GUID: Guid = Guid('{b5d9fc17-5d6f-4420-b439-7cb19ad434e2}')
StyleId_Normal_GUID: Guid = Guid('{cd14d429-e45e-4475-a1c5-7f9e6be96eba}')
StyleId_Emphasis_GUID: Guid = Guid('{ca6e7dbe-355e-4820-95a0-925f041d3470}')
StyleId_Quote_GUID: Guid = Guid('{5d1c21ea-8195-4f6c-87ea-5dabece64c1d}')
StyleId_BulletedList_GUID: Guid = Guid('{5963ed64-6426-4632-8caf-a32ad402d91a}')
StyleId_NumberedList_GUID: Guid = Guid('{1e96dbd5-64c3-43d0-b1ee-b53b06e3eddf}')
Notification_Event_GUID: Guid = Guid('{72c5a2f7-9788-480f-b8eb-4dee00f6186f}')
SID_IsUIAutomationObject: Guid = Guid('{b96fdb85-7204-4724-842b-c7059dedb9d0}')
SID_ControlElementProvider: Guid = Guid('{f4791d68-e254-4ba3-9a53-26a5c5497946}')
IsSelectionPattern2Available_Property_GUID: Guid = Guid('{490806fb-6e89-4a47-8319-d266e511f021}')
Selection2_FirstSelectedItem_Property_GUID: Guid = Guid('{cc24ea67-369c-4e55-9ff7-38da69540c29}')
Selection2_LastSelectedItem_Property_GUID: Guid = Guid('{cf7bda90-2d83-49f8-860c-9ce394cf89b4}')
Selection2_CurrentSelectedItem_Property_GUID: Guid = Guid('{34257c26-83b5-41a6-939c-ae841c136236}')
Selection2_ItemCount_Property_GUID: Guid = Guid('{bb49eb9f-456d-4048-b591-9c2026b84636}')
Selection_Pattern2_GUID: Guid = Guid('{fba25cab-ab98-49f7-a7dc-fe539dc15be7}')
HeadingLevel_Property_GUID: Guid = Guid('{29084272-aaaf-4a30-8796-3c12f62b6bbb}')
IsDialog_Property_GUID: Guid = Guid('{9d0dfb9b-8436-4501-bbbb-e534a4fb3b3f}')
UIA_IAFP_DEFAULT: UInt32 = 0
UIA_IAFP_UNWRAP_BRIDGE: UInt32 = 1
UIA_PFIA_DEFAULT: UInt32 = 0
UIA_PFIA_UNWRAP_BRIDGE: UInt32 = 1
UIA_ScrollPatternNoScroll: Double = -1
@winfunctype('OLEACC.dll')
def LresultFromObject(riid: POINTER(Guid), wParam: win32more.Windows.Win32.Foundation.WPARAM, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.LRESULT: ...
@winfunctype('OLEACC.dll')
def ObjectFromLresult(lResult: win32more.Windows.Win32.Foundation.LRESULT, riid: POINTER(Guid), wParam: win32more.Windows.Win32.Foundation.WPARAM, ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def WindowFromAccessibleObject(param0: win32more.Windows.Win32.UI.Accessibility.IAccessible, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def AccessibleObjectFromWindow(hwnd: win32more.Windows.Win32.Foundation.HWND, dwId: UInt32, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def AccessibleObjectFromEvent(hwnd: win32more.Windows.Win32.Foundation.HWND, dwId: UInt32, dwChildId: UInt32, ppacc: POINTER(win32more.Windows.Win32.UI.Accessibility.IAccessible), pvarChild: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def AccessibleObjectFromPoint(ptScreen: win32more.Windows.Win32.Foundation.POINT, ppacc: POINTER(win32more.Windows.Win32.UI.Accessibility.IAccessible), pvarChild: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def AccessibleChildren(paccContainer: win32more.Windows.Win32.UI.Accessibility.IAccessible, iChildStart: Int32, cChildren: Int32, rgvarChildren: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pcObtained: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def GetRoleTextA(lRole: UInt32, lpszRole: win32more.Windows.Win32.Foundation.PSTR, cchRoleMax: UInt32) -> UInt32: ...
@winfunctype('OLEACC.dll')
def GetRoleTextW(lRole: UInt32, lpszRole: win32more.Windows.Win32.Foundation.PWSTR, cchRoleMax: UInt32) -> UInt32: ...
GetRoleText = UnicodeAlias('GetRoleTextW')
@winfunctype('OLEACC.dll')
def GetStateTextA(lStateBit: UInt32, lpszState: win32more.Windows.Win32.Foundation.PSTR, cchState: UInt32) -> UInt32: ...
@winfunctype('OLEACC.dll')
def GetStateTextW(lStateBit: UInt32, lpszState: win32more.Windows.Win32.Foundation.PWSTR, cchState: UInt32) -> UInt32: ...
GetStateText = UnicodeAlias('GetStateTextW')
@winfunctype('OLEACC.dll')
def GetOleaccVersionInfo(pVer: POINTER(UInt32), pBuild: POINTER(UInt32)) -> Void: ...
@winfunctype('OLEACC.dll')
def CreateStdAccessibleObject(hwnd: win32more.Windows.Win32.Foundation.HWND, idObject: Int32, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def CreateStdAccessibleProxyA(hwnd: win32more.Windows.Win32.Foundation.HWND, pClassName: win32more.Windows.Win32.Foundation.PSTR, idObject: Int32, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def CreateStdAccessibleProxyW(hwnd: win32more.Windows.Win32.Foundation.HWND, pClassName: win32more.Windows.Win32.Foundation.PWSTR, idObject: Int32, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
CreateStdAccessibleProxy = UnicodeAlias('CreateStdAccessibleProxyW')
@winfunctype('OLEACC.dll')
def AccSetRunningUtilityState(hwndApp: win32more.Windows.Win32.Foundation.HWND, dwUtilityStateMask: UInt32, dwUtilityState: win32more.Windows.Win32.UI.Accessibility.ACC_UTILITY_STATE_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEACC.dll')
def AccNotifyTouchInteraction(hwndApp: win32more.Windows.Win32.Foundation.HWND, hwndTarget: win32more.Windows.Win32.Foundation.HWND, ptTarget: win32more.Windows.Win32.Foundation.POINT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetErrorDescription(pDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('UIAutomationCore.dll')
def UiaHUiaNodeFromVariant(pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), phnode: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIANODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaHPatternObjectFromVariant(pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), phobj: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaHTextRangeFromVariant(pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), phtextrange: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaNodeRelease(hnode: win32more.Windows.Win32.UI.Accessibility.HUIANODE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetPropertyValue(hnode: win32more.Windows.Win32.UI.Accessibility.HUIANODE, propertyId: Int32, pValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetPatternProvider(hnode: win32more.Windows.Win32.UI.Accessibility.HUIANODE, patternId: Int32, phobj: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetRuntimeId(hnode: win32more.Windows.Win32.UI.Accessibility.HUIANODE, pruntimeId: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaSetFocus(hnode: win32more.Windows.Win32.UI.Accessibility.HUIANODE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaNavigate(hnode: win32more.Windows.Win32.UI.Accessibility.HUIANODE, direction: win32more.Windows.Win32.UI.Accessibility.NavigateDirection, pCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaCondition), pRequest: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaCacheRequest), ppRequestedData: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppTreeStructure: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetUpdatedCache(hnode: win32more.Windows.Win32.UI.Accessibility.HUIANODE, pRequest: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaCacheRequest), normalizeState: win32more.Windows.Win32.UI.Accessibility.NormalizeState, pNormalizeCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaCondition), ppRequestedData: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppTreeStructure: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaFind(hnode: win32more.Windows.Win32.UI.Accessibility.HUIANODE, pParams: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaFindParams), pRequest: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaCacheRequest), ppRequestedData: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppOffsets: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppTreeStructures: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaNodeFromPoint(x: Double, y: Double, pRequest: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaCacheRequest), ppRequestedData: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppTreeStructure: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaNodeFromFocus(pRequest: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaCacheRequest), ppRequestedData: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), ppTreeStructure: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaNodeFromHandle(hwnd: win32more.Windows.Win32.Foundation.HWND, phnode: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIANODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaNodeFromProvider(pProvider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, phnode: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIANODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetRootNode(phnode: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIANODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRegisterProviderCallback(pCallback: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaProviderCallback)) -> Void: ...
@winfunctype('UIAutomationCore.dll')
def UiaLookupId(type: win32more.Windows.Win32.UI.Accessibility.AutomationIdentifierType, pGuid: POINTER(Guid)) -> Int32: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetReservedNotSupportedValue(punkNotSupportedValue: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaGetReservedMixedAttributeValue(punkMixedAttributeValue: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaClientsAreListening() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseAutomationPropertyChangedEvent(pProvider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, id: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, oldValue: win32more.Windows.Win32.System.Variant.VARIANT, newValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseAutomationEvent(pProvider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, id: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseStructureChangedEvent(pProvider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, structureChangeType: win32more.Windows.Win32.UI.Accessibility.StructureChangeType, pRuntimeId: POINTER(Int32), cRuntimeIdLen: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseAsyncContentLoadedEvent(pProvider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, asyncContentLoadedState: win32more.Windows.Win32.UI.Accessibility.AsyncContentLoadedState, percentComplete: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseTextEditTextChangedEvent(pProvider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, textEditChangeType: win32more.Windows.Win32.UI.Accessibility.TextEditChangeType, pChangedData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseChangesEvent(pProvider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, eventIdCount: Int32, pUiaChanges: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaChangeInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseNotificationEvent(provider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, notificationKind: win32more.Windows.Win32.UI.Accessibility.NotificationKind, notificationProcessing: win32more.Windows.Win32.UI.Accessibility.NotificationProcessing, displayString: win32more.Windows.Win32.Foundation.BSTR, activityId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRaiseActiveTextPositionChangedEvent(provider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, textRange: win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaAddEvent(hnode: win32more.Windows.Win32.UI.Accessibility.HUIANODE, eventId: Int32, pCallback: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaEventCallback), scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, pProperties: POINTER(Int32), cProperties: Int32, pRequest: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaCacheRequest), phEvent: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIAEVENT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaRemoveEvent(hEvent: win32more.Windows.Win32.UI.Accessibility.HUIAEVENT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaEventAddWindow(hEvent: win32more.Windows.Win32.UI.Accessibility.HUIAEVENT, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaEventRemoveWindow(hEvent: win32more.Windows.Win32.UI.Accessibility.HUIAEVENT, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def DockPattern_SetDockPosition(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, dockPosition: win32more.Windows.Win32.UI.Accessibility.DockPosition) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ExpandCollapsePattern_Collapse(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ExpandCollapsePattern_Expand(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def GridPattern_GetItem(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, row: Int32, column: Int32, pResult: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIANODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def InvokePattern_Invoke(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def MultipleViewPattern_GetViewName(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, viewId: Int32, ppStr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def MultipleViewPattern_SetCurrentView(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, viewId: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def RangeValuePattern_SetValue(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, val: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ScrollItemPattern_ScrollIntoView(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ScrollPattern_Scroll(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, horizontalAmount: win32more.Windows.Win32.UI.Accessibility.ScrollAmount, verticalAmount: win32more.Windows.Win32.UI.Accessibility.ScrollAmount) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ScrollPattern_SetScrollPercent(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, horizontalPercent: Double, verticalPercent: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def SelectionItemPattern_AddToSelection(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def SelectionItemPattern_RemoveFromSelection(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def SelectionItemPattern_Select(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TogglePattern_Toggle(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TransformPattern_Move(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, x: Double, y: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TransformPattern_Resize(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, width: Double, height: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TransformPattern_Rotate(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, degrees: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ValuePattern_SetValue(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, pVal: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def WindowPattern_Close(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def WindowPattern_SetWindowVisualState(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, state: win32more.Windows.Win32.UI.Accessibility.WindowVisualState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def WindowPattern_WaitForInputIdle(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, milliseconds: Int32, pResult: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextPattern_GetSelection(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextPattern_GetVisibleRanges(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextPattern_RangeFromChild(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, hnodeChild: win32more.Windows.Win32.UI.Accessibility.HUIANODE, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextPattern_RangeFromPoint(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, point: win32more.Windows.Win32.UI.Accessibility.UiaPoint, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextPattern_get_DocumentRange(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextPattern_get_SupportedTextSelection(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.SupportedTextSelection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_Clone(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_Compare(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, range: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_CompareEndpoints(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, endpoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, targetRange: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, targetEndpoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_ExpandToEnclosingUnit(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, unit: win32more.Windows.Win32.UI.Accessibility.TextUnit) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_GetAttributeValue(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, attributeId: Int32, pRetVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_FindAttribute(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, attributeId: Int32, val: win32more.Windows.Win32.System.Variant.VARIANT, backward: win32more.Windows.Win32.Foundation.BOOL, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_FindText(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, text: win32more.Windows.Win32.Foundation.BSTR, backward: win32more.Windows.Win32.Foundation.BOOL, ignoreCase: win32more.Windows.Win32.Foundation.BOOL, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_GetBoundingRectangles(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_GetEnclosingElement(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIANODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_GetText(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, maxLength: Int32, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_Move(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, unit: win32more.Windows.Win32.UI.Accessibility.TextUnit, count: Int32, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_MoveEndpointByUnit(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, endpoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, unit: win32more.Windows.Win32.UI.Accessibility.TextUnit, count: Int32, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_MoveEndpointByRange(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, endpoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, targetRange: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, targetEndpoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_Select(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_AddToSelection(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_RemoveFromSelection(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_ScrollIntoView(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, alignToTop: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def TextRange_GetChildren(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def ItemContainerPattern_FindItemByProperty(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, hnodeStartAfter: win32more.Windows.Win32.UI.Accessibility.HUIANODE, propertyId: Int32, value: win32more.Windows.Win32.System.Variant.VARIANT, pFound: POINTER(win32more.Windows.Win32.UI.Accessibility.HUIANODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def LegacyIAccessiblePattern_Select(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, flagsSelect: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def LegacyIAccessiblePattern_DoDefaultAction(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def LegacyIAccessiblePattern_SetValue(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, szValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def LegacyIAccessiblePattern_GetIAccessible(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, pAccessible: POINTER(win32more.Windows.Win32.UI.Accessibility.IAccessible)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def SynchronizedInputPattern_StartListening(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT, inputType: win32more.Windows.Win32.UI.Accessibility.SynchronizedInputType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def SynchronizedInputPattern_Cancel(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def VirtualizedItemPattern_Realize(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaPatternRelease(hobj: win32more.Windows.Win32.UI.Accessibility.HUIAPATTERNOBJECT) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('UIAutomationCore.dll')
def UiaTextRangeRelease(hobj: win32more.Windows.Win32.UI.Accessibility.HUIATEXTRANGE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('UIAutomationCore.dll')
def UiaReturnRawElementProvider(hwnd: win32more.Windows.Win32.Foundation.HWND, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, el: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple) -> win32more.Windows.Win32.Foundation.LRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaHostProviderFromHwnd(hwnd: win32more.Windows.Win32.Foundation.HWND, ppProvider: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaProviderForNonClient(hwnd: win32more.Windows.Win32.Foundation.HWND, idObject: Int32, idChild: Int32, ppProvider: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaIAccessibleFromProvider(pProvider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, dwFlags: UInt32, ppAccessible: POINTER(win32more.Windows.Win32.UI.Accessibility.IAccessible), pvarChild: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaProviderFromIAccessible(pAccessible: win32more.Windows.Win32.UI.Accessibility.IAccessible, idChild: Int32, dwFlags: UInt32, ppProvider: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaDisconnectAllProviders() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaDisconnectProvider(pProvider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('UIAutomationCore.dll')
def UiaHasServerSideProvider(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def RegisterPointerInputTarget(hwnd: win32more.Windows.Win32.Foundation.HWND, pointerType: win32more.Windows.Win32.UI.WindowsAndMessaging.POINTER_INPUT_TYPE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def UnregisterPointerInputTarget(hwnd: win32more.Windows.Win32.Foundation.HWND, pointerType: win32more.Windows.Win32.UI.WindowsAndMessaging.POINTER_INPUT_TYPE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def RegisterPointerInputTargetEx(hwnd: win32more.Windows.Win32.Foundation.HWND, pointerType: win32more.Windows.Win32.UI.WindowsAndMessaging.POINTER_INPUT_TYPE, fObserve: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def UnregisterPointerInputTargetEx(hwnd: win32more.Windows.Win32.Foundation.HWND, pointerType: win32more.Windows.Win32.UI.WindowsAndMessaging.POINTER_INPUT_TYPE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def NotifyWinEvent(event: UInt32, hwnd: win32more.Windows.Win32.Foundation.HWND, idObject: Int32, idChild: Int32) -> Void: ...
@winfunctype('USER32.dll')
def SetWinEventHook(eventMin: UInt32, eventMax: UInt32, hmodWinEventProc: win32more.Windows.Win32.Foundation.HMODULE, pfnWinEventProc: win32more.Windows.Win32.UI.Accessibility.WINEVENTPROC, idProcess: UInt32, idThread: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.UI.Accessibility.HWINEVENTHOOK: ...
@winfunctype('USER32.dll')
def IsWinEventHookInstalled(event: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def UnhookWinEvent(hWinEventHook: win32more.Windows.Win32.UI.Accessibility.HWINEVENTHOOK) -> win32more.Windows.Win32.Foundation.BOOL: ...
AsyncContentLoadedState = Int32
AsyncContentLoadedState_Beginning: win32more.Windows.Win32.UI.Accessibility.AsyncContentLoadedState = 0
AsyncContentLoadedState_Progress: win32more.Windows.Win32.UI.Accessibility.AsyncContentLoadedState = 1
AsyncContentLoadedState_Completed: win32more.Windows.Win32.UI.Accessibility.AsyncContentLoadedState = 2
AutomationElementMode = Int32
AutomationElementMode_None: win32more.Windows.Win32.UI.Accessibility.AutomationElementMode = 0
AutomationElementMode_Full: win32more.Windows.Win32.UI.Accessibility.AutomationElementMode = 1
AutomationIdentifierType = Int32
AutomationIdentifierType_Property: win32more.Windows.Win32.UI.Accessibility.AutomationIdentifierType = 0
AutomationIdentifierType_Pattern: win32more.Windows.Win32.UI.Accessibility.AutomationIdentifierType = 1
AutomationIdentifierType_Event: win32more.Windows.Win32.UI.Accessibility.AutomationIdentifierType = 2
AutomationIdentifierType_ControlType: win32more.Windows.Win32.UI.Accessibility.AutomationIdentifierType = 3
AutomationIdentifierType_TextAttribute: win32more.Windows.Win32.UI.Accessibility.AutomationIdentifierType = 4
AutomationIdentifierType_LandmarkType: win32more.Windows.Win32.UI.Accessibility.AutomationIdentifierType = 5
AutomationIdentifierType_Annotation: win32more.Windows.Win32.UI.Accessibility.AutomationIdentifierType = 6
AutomationIdentifierType_Changes: win32more.Windows.Win32.UI.Accessibility.AutomationIdentifierType = 7
AutomationIdentifierType_Style: win32more.Windows.Win32.UI.Accessibility.AutomationIdentifierType = 8
BulletStyle = Int32
BulletStyle_None: win32more.Windows.Win32.UI.Accessibility.BulletStyle = 0
BulletStyle_HollowRoundBullet: win32more.Windows.Win32.UI.Accessibility.BulletStyle = 1
BulletStyle_FilledRoundBullet: win32more.Windows.Win32.UI.Accessibility.BulletStyle = 2
BulletStyle_HollowSquareBullet: win32more.Windows.Win32.UI.Accessibility.BulletStyle = 3
BulletStyle_FilledSquareBullet: win32more.Windows.Win32.UI.Accessibility.BulletStyle = 4
BulletStyle_DashBullet: win32more.Windows.Win32.UI.Accessibility.BulletStyle = 5
BulletStyle_Other: win32more.Windows.Win32.UI.Accessibility.BulletStyle = -1
CAccPropServices = Guid('{b5f8350b-0548-48b1-a6ee-88bd00b4a5e7}')
CUIAutomation = Guid('{ff48dba4-60ef-4201-aa87-54103eef594e}')
CUIAutomation8 = Guid('{e22ad333-b25f-460c-83d0-0581107395c9}')
CUIAutomationRegistrar = Guid('{6e29fabf-9977-42d1-8d0e-ca7e61ad87e6}')
CapStyle = Int32
CapStyle_None: win32more.Windows.Win32.UI.Accessibility.CapStyle = 0
CapStyle_SmallCap: win32more.Windows.Win32.UI.Accessibility.CapStyle = 1
CapStyle_AllCap: win32more.Windows.Win32.UI.Accessibility.CapStyle = 2
CapStyle_AllPetiteCaps: win32more.Windows.Win32.UI.Accessibility.CapStyle = 3
CapStyle_PetiteCaps: win32more.Windows.Win32.UI.Accessibility.CapStyle = 4
CapStyle_Unicase: win32more.Windows.Win32.UI.Accessibility.CapStyle = 5
CapStyle_Titling: win32more.Windows.Win32.UI.Accessibility.CapStyle = 6
CapStyle_Other: win32more.Windows.Win32.UI.Accessibility.CapStyle = -1
CaretBidiMode = Int32
CaretBidiMode_LTR: win32more.Windows.Win32.UI.Accessibility.CaretBidiMode = 0
CaretBidiMode_RTL: win32more.Windows.Win32.UI.Accessibility.CaretBidiMode = 1
CaretPosition = Int32
CaretPosition_Unknown: win32more.Windows.Win32.UI.Accessibility.CaretPosition = 0
CaretPosition_EndOfLine: win32more.Windows.Win32.UI.Accessibility.CaretPosition = 1
CaretPosition_BeginningOfLine: win32more.Windows.Win32.UI.Accessibility.CaretPosition = 2
CoalesceEventsOptions = Int32
CoalesceEventsOptions_Disabled: win32more.Windows.Win32.UI.Accessibility.CoalesceEventsOptions = 0
CoalesceEventsOptions_Enabled: win32more.Windows.Win32.UI.Accessibility.CoalesceEventsOptions = 1
ConditionType = Int32
ConditionType_True: win32more.Windows.Win32.UI.Accessibility.ConditionType = 0
ConditionType_False: win32more.Windows.Win32.UI.Accessibility.ConditionType = 1
ConditionType_Property: win32more.Windows.Win32.UI.Accessibility.ConditionType = 2
ConditionType_And: win32more.Windows.Win32.UI.Accessibility.ConditionType = 3
ConditionType_Or: win32more.Windows.Win32.UI.Accessibility.ConditionType = 4
ConditionType_Not: win32more.Windows.Win32.UI.Accessibility.ConditionType = 5
ConnectionRecoveryBehaviorOptions = Int32
ConnectionRecoveryBehaviorOptions_Disabled: win32more.Windows.Win32.UI.Accessibility.ConnectionRecoveryBehaviorOptions = 0
ConnectionRecoveryBehaviorOptions_Enabled: win32more.Windows.Win32.UI.Accessibility.ConnectionRecoveryBehaviorOptions = 1
DockPosition = Int32
DockPosition_Top: win32more.Windows.Win32.UI.Accessibility.DockPosition = 0
DockPosition_Left: win32more.Windows.Win32.UI.Accessibility.DockPosition = 1
DockPosition_Bottom: win32more.Windows.Win32.UI.Accessibility.DockPosition = 2
DockPosition_Right: win32more.Windows.Win32.UI.Accessibility.DockPosition = 3
DockPosition_Fill: win32more.Windows.Win32.UI.Accessibility.DockPosition = 4
DockPosition_None: win32more.Windows.Win32.UI.Accessibility.DockPosition = 5
EventArgsType = Int32
EventArgsType_Simple: win32more.Windows.Win32.UI.Accessibility.EventArgsType = 0
EventArgsType_PropertyChanged: win32more.Windows.Win32.UI.Accessibility.EventArgsType = 1
EventArgsType_StructureChanged: win32more.Windows.Win32.UI.Accessibility.EventArgsType = 2
EventArgsType_AsyncContentLoaded: win32more.Windows.Win32.UI.Accessibility.EventArgsType = 3
EventArgsType_WindowClosed: win32more.Windows.Win32.UI.Accessibility.EventArgsType = 4
EventArgsType_TextEditTextChanged: win32more.Windows.Win32.UI.Accessibility.EventArgsType = 5
EventArgsType_Changes: win32more.Windows.Win32.UI.Accessibility.EventArgsType = 6
EventArgsType_Notification: win32more.Windows.Win32.UI.Accessibility.EventArgsType = 7
EventArgsType_ActiveTextPositionChanged: win32more.Windows.Win32.UI.Accessibility.EventArgsType = 8
EventArgsType_StructuredMarkup: win32more.Windows.Win32.UI.Accessibility.EventArgsType = 9
ExpandCollapseState = Int32
ExpandCollapseState_Collapsed: win32more.Windows.Win32.UI.Accessibility.ExpandCollapseState = 0
ExpandCollapseState_Expanded: win32more.Windows.Win32.UI.Accessibility.ExpandCollapseState = 1
ExpandCollapseState_PartiallyExpanded: win32more.Windows.Win32.UI.Accessibility.ExpandCollapseState = 2
ExpandCollapseState_LeafNode: win32more.Windows.Win32.UI.Accessibility.ExpandCollapseState = 3
class ExtendedProperty(Structure):
    PropertyName: win32more.Windows.Win32.Foundation.BSTR
    PropertyValue: win32more.Windows.Win32.Foundation.BSTR
class FILTERKEYS(Structure):
    cbSize: UInt32
    dwFlags: UInt32
    iWaitMSec: UInt32
    iDelayMSec: UInt32
    iRepeatMSec: UInt32
    iBounceMSec: UInt32
FillType = Int32
FillType_None: win32more.Windows.Win32.UI.Accessibility.FillType = 0
FillType_Color: win32more.Windows.Win32.UI.Accessibility.FillType = 1
FillType_Gradient: win32more.Windows.Win32.UI.Accessibility.FillType = 2
FillType_Picture: win32more.Windows.Win32.UI.Accessibility.FillType = 3
FillType_Pattern: win32more.Windows.Win32.UI.Accessibility.FillType = 4
FlowDirections = Int32
FlowDirections_Default: win32more.Windows.Win32.UI.Accessibility.FlowDirections = 0
FlowDirections_RightToLeft: win32more.Windows.Win32.UI.Accessibility.FlowDirections = 1
FlowDirections_BottomToTop: win32more.Windows.Win32.UI.Accessibility.FlowDirections = 2
FlowDirections_Vertical: win32more.Windows.Win32.UI.Accessibility.FlowDirections = 4
class HIGHCONTRASTA(Structure):
    cbSize: UInt32
    dwFlags: win32more.Windows.Win32.UI.Accessibility.HIGHCONTRASTW_FLAGS
    lpszDefaultScheme: win32more.Windows.Win32.Foundation.PSTR
class HIGHCONTRASTW(Structure):
    cbSize: UInt32
    dwFlags: win32more.Windows.Win32.UI.Accessibility.HIGHCONTRASTW_FLAGS
    lpszDefaultScheme: win32more.Windows.Win32.Foundation.PWSTR
HIGHCONTRAST = UnicodeAlias('HIGHCONTRASTW')
HIGHCONTRASTW_FLAGS = UInt32
HCF_HIGHCONTRASTON: win32more.Windows.Win32.UI.Accessibility.HIGHCONTRASTW_FLAGS = 1
HCF_AVAILABLE: win32more.Windows.Win32.UI.Accessibility.HIGHCONTRASTW_FLAGS = 2
HCF_HOTKEYACTIVE: win32more.Windows.Win32.UI.Accessibility.HIGHCONTRASTW_FLAGS = 4
HCF_CONFIRMHOTKEY: win32more.Windows.Win32.UI.Accessibility.HIGHCONTRASTW_FLAGS = 8
HCF_HOTKEYSOUND: win32more.Windows.Win32.UI.Accessibility.HIGHCONTRASTW_FLAGS = 16
HCF_INDICATOR: win32more.Windows.Win32.UI.Accessibility.HIGHCONTRASTW_FLAGS = 32
HCF_HOTKEYAVAILABLE: win32more.Windows.Win32.UI.Accessibility.HIGHCONTRASTW_FLAGS = 64
HCF_OPTION_NOTHEMECHANGE: win32more.Windows.Win32.UI.Accessibility.HIGHCONTRASTW_FLAGS = 4096
HUIAEVENT = VoidPtr
HUIANODE = VoidPtr
HUIAPATTERNOBJECT = VoidPtr
HUIATEXTRANGE = VoidPtr
HWINEVENTHOOK = VoidPtr
HorizontalTextAlignment = Int32
HorizontalTextAlignment_Left: win32more.Windows.Win32.UI.Accessibility.HorizontalTextAlignment = 0
HorizontalTextAlignment_Centered: win32more.Windows.Win32.UI.Accessibility.HorizontalTextAlignment = 1
HorizontalTextAlignment_Right: win32more.Windows.Win32.UI.Accessibility.HorizontalTextAlignment = 2
HorizontalTextAlignment_Justified: win32more.Windows.Win32.UI.Accessibility.HorizontalTextAlignment = 3
class IAccIdentity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7852b78d-1cfd-41c1-a615-9c0c85960b5f}')
    @commethod(3)
    def GetIdentityString(self, dwIDChild: UInt32, ppIDString: POINTER(POINTER(Byte)), pdwIDStringLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAccPropServer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{76c0dbbb-15e0-4e7b-b61b-20eeea2001e0}')
    @commethod(3)
    def GetPropValue(self, pIDString: POINTER(Byte), dwIDStringLen: UInt32, idProp: Guid, pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pfHasProp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAccPropServices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6e26e776-04f0-495d-80e4-3330352e3169}')
    @commethod(3)
    def SetPropValue(self, pIDString: POINTER(Byte), dwIDStringLen: UInt32, idProp: Guid, var: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPropServer(self, pIDString: POINTER(Byte), dwIDStringLen: UInt32, paProps: POINTER(Guid), cProps: Int32, pServer: win32more.Windows.Win32.UI.Accessibility.IAccPropServer, annoScope: win32more.Windows.Win32.UI.Accessibility.AnnoScope) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ClearProps(self, pIDString: POINTER(Byte), dwIDStringLen: UInt32, paProps: POINTER(Guid), cProps: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetHwndProp(self, hwnd: win32more.Windows.Win32.Foundation.HWND, idObject: UInt32, idChild: UInt32, idProp: Guid, var: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetHwndPropStr(self, hwnd: win32more.Windows.Win32.Foundation.HWND, idObject: UInt32, idChild: UInt32, idProp: Guid, str: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetHwndPropServer(self, hwnd: win32more.Windows.Win32.Foundation.HWND, idObject: UInt32, idChild: UInt32, paProps: POINTER(Guid), cProps: Int32, pServer: win32more.Windows.Win32.UI.Accessibility.IAccPropServer, annoScope: win32more.Windows.Win32.UI.Accessibility.AnnoScope) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ClearHwndProps(self, hwnd: win32more.Windows.Win32.Foundation.HWND, idObject: UInt32, idChild: UInt32, paProps: POINTER(Guid), cProps: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ComposeHwndIdentityString(self, hwnd: win32more.Windows.Win32.Foundation.HWND, idObject: UInt32, idChild: UInt32, ppIDString: POINTER(POINTER(Byte)), pdwIDStringLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DecomposeHwndIdentityString(self, pIDString: POINTER(Byte), dwIDStringLen: UInt32, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND), pidObject: POINTER(UInt32), pidChild: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetHmenuProp(self, hmenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, idChild: UInt32, idProp: Guid, var: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetHmenuPropStr(self, hmenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, idChild: UInt32, idProp: Guid, str: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetHmenuPropServer(self, hmenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, idChild: UInt32, paProps: POINTER(Guid), cProps: Int32, pServer: win32more.Windows.Win32.UI.Accessibility.IAccPropServer, annoScope: win32more.Windows.Win32.UI.Accessibility.AnnoScope) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ClearHmenuProps(self, hmenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, idChild: UInt32, paProps: POINTER(Guid), cProps: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ComposeHmenuIdentityString(self, hmenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, idChild: UInt32, ppIDString: POINTER(POINTER(Byte)), pdwIDStringLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def DecomposeHmenuIdentityString(self, pIDString: POINTER(Byte), dwIDStringLen: UInt32, phmenu: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU), pidChild: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAccessible(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{618736e0-3c3d-11cf-810c-00aa00389b71}')
    @commethod(7)
    def get_accParent(self, ppdispParent: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_accChildCount(self, pcountChildren: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_accChild(self, varChild: win32more.Windows.Win32.System.Variant.VARIANT, ppdispChild: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_accName(self, varChild: win32more.Windows.Win32.System.Variant.VARIANT, pszName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_accValue(self, varChild: win32more.Windows.Win32.System.Variant.VARIANT, pszValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_accDescription(self, varChild: win32more.Windows.Win32.System.Variant.VARIANT, pszDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_accRole(self, varChild: win32more.Windows.Win32.System.Variant.VARIANT, pvarRole: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_accState(self, varChild: win32more.Windows.Win32.System.Variant.VARIANT, pvarState: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_accHelp(self, varChild: win32more.Windows.Win32.System.Variant.VARIANT, pszHelp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_accHelpTopic(self, pszHelpFile: POINTER(win32more.Windows.Win32.Foundation.BSTR), varChild: win32more.Windows.Win32.System.Variant.VARIANT, pidTopic: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_accKeyboardShortcut(self, varChild: win32more.Windows.Win32.System.Variant.VARIANT, pszKeyboardShortcut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_accFocus(self, pvarChild: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_accSelection(self, pvarChildren: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_accDefaultAction(self, varChild: win32more.Windows.Win32.System.Variant.VARIANT, pszDefaultAction: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def accSelect(self, flagsSelect: Int32, varChild: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def accLocation(self, pxLeft: POINTER(Int32), pyTop: POINTER(Int32), pcxWidth: POINTER(Int32), pcyHeight: POINTER(Int32), varChild: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def accNavigate(self, navDir: Int32, varStart: win32more.Windows.Win32.System.Variant.VARIANT, pvarEndUpAt: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def accHitTest(self, xLeft: Int32, yTop: Int32, pvarChild: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def accDoDefaultAction(self, varChild: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_accName(self, varChild: win32more.Windows.Win32.System.Variant.VARIANT, szName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_accValue(self, varChild: win32more.Windows.Win32.System.Variant.VARIANT, szValue: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAccessibleEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f8b80ada-2c44-48d0-89be-5ff23c9cd875}')
    @commethod(3)
    def GetObjectForChild(self, idChild: Int32, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IAccessibleEx)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIAccessiblePair(self, ppAcc: POINTER(win32more.Windows.Win32.UI.Accessibility.IAccessible), pidChild: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRuntimeId(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ConvertReturnedElement(self, pIn: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, ppRetValOut: POINTER(win32more.Windows.Win32.UI.Accessibility.IAccessibleEx)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAccessibleHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{03022430-abc4-11d0-bde2-00aa001a1953}')
    @commethod(3)
    def AccessibleObjectFromID(self, hwnd: Int32, lObjectID: Int32, pIAccessible: POINTER(win32more.Windows.Win32.UI.Accessibility.IAccessible)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAccessibleHostingElementProviders(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{33ac331b-943e-4020-b295-db37784974a3}')
    @commethod(3)
    def GetEmbeddedFragmentRoots(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetObjectIdForProvider(self, pProvider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, pidObject: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAccessibleWindowlessSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bf3abd9c-76da-4389-9eb6-1427d25abab7}')
    @commethod(3)
    def AcquireObjectIdRange(self, rangeSize: Int32, pRangeOwner: win32more.Windows.Win32.UI.Accessibility.IAccessibleHandler, pRangeBase: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseObjectIdRange(self, rangeBase: Int32, pRangeOwner: win32more.Windows.Win32.UI.Accessibility.IAccessibleHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryObjectIdRanges(self, pRangesOwner: win32more.Windows.Win32.UI.Accessibility.IAccessibleHandler, psaRanges: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetParentAccessible(self, ppParent: POINTER(win32more.Windows.Win32.UI.Accessibility.IAccessible)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAnnotationProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f95c7e80-bd63-4601-9782-445ebff011fc}')
    @commethod(3)
    def get_AnnotationTypeId(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_AnnotationTypeName(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Author(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_DateTime(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Target(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICustomNavigationProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2062a28a-8c07-4b94-8e12-7037c622aeb8}')
    @commethod(3)
    def Navigate(self, direction: win32more.Windows.Win32.UI.Accessibility.NavigateDirection, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDockProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{159bc72c-4ad3-485e-9637-d7052edf0146}')
    @commethod(3)
    def SetDockPosition(self, dockPosition: win32more.Windows.Win32.UI.Accessibility.DockPosition) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_DockPosition(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.DockPosition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDragProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6aa7bbbb-7ff9-497d-904f-d20b897929d8}')
    @commethod(3)
    def get_IsGrabbed(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_DropEffect(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_DropEffects(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGrabbedItems(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDropTargetProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bae82bfd-358a-481c-85a0-d8b4d90a5d61}')
    @commethod(3)
    def get_DropTargetEffect(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_DropTargetEffects(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExpandCollapseProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d847d3a5-cab0-4a98-8c32-ecb45c59ad24}')
    @commethod(3)
    def Expand(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Collapse(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_ExpandCollapseState(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ExpandCollapseState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGridItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d02541f1-fb81-4d64-ae32-f520f8a6dbd1}')
    @commethod(3)
    def get_Row(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Column(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_RowSpan(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_ColumnSpan(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_ContainingGrid(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGridProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b17d6187-0907-464b-a168-0ef17a1572b1}')
    @commethod(3)
    def GetItem(self, row: Int32, column: Int32, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_RowCount(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_ColumnCount(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInvokeProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{54fcb24b-e18e-47a2-b4d3-eccbe77599a2}')
    @commethod(3)
    def Invoke(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IItemContainerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e747770b-39ce-4382-ab30-d8fb3f336f24}')
    @commethod(3)
    def FindItemByProperty(self, pStartAfter: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, propertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, value: win32more.Windows.Win32.System.Variant.VARIANT, pFound: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILegacyIAccessibleProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e44c3566-915d-4070-99c6-047bff5a08f5}')
    @commethod(3)
    def Select(self, flagsSelect: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DoDefaultAction(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(self, szValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIAccessible(self, ppAccessible: POINTER(win32more.Windows.Win32.UI.Accessibility.IAccessible)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_ChildId(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Name(self, pszName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Value(self, pszValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Description(self, pszDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Role(self, pdwRole: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_State(self, pdwState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Help(self, pszHelp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_KeyboardShortcut(self, pszKeyboardShortcut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetSelection(self, pvarSelectedChildren: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_DefaultAction(self, pszDefaultAction: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMultipleViewProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6278cab1-b556-4a1a-b4e0-418acc523201}')
    @commethod(3)
    def GetViewName(self, viewId: Int32, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCurrentView(self, viewId: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentView(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSupportedViews(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectModelProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3ad86ebd-f5ef-483d-bb18-b1042a475d64}')
    @commethod(3)
    def GetUnderlyingObjectModel(self, ppUnknown: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProxyProviderWinEventHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{89592ad4-f4e0-43d5-a3b6-bad7e111b435}')
    @commethod(3)
    def RespondToWinEvent(self, idWinEvent: UInt32, hwnd: win32more.Windows.Win32.Foundation.HWND, idObject: Int32, idChild: Int32, pSink: win32more.Windows.Win32.UI.Accessibility.IProxyProviderWinEventSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProxyProviderWinEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4fd82b78-a43e-46ac-9803-0a6969c7c183}')
    @commethod(3)
    def AddAutomationPropertyChangedEvent(self, pProvider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, id: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, newValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddAutomationEvent(self, pProvider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, id: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddStructureChangedEvent(self, pProvider: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, structureChangeType: win32more.Windows.Win32.UI.Accessibility.StructureChangeType, runtimeId: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRangeValueProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{36dc7aef-33e6-4691-afe1-2be7274b3d33}')
    @commethod(3)
    def SetValue(self, val: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Value(self, pRetVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_IsReadOnly(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Maximum(self, pRetVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Minimum(self, pRetVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LargeChange(self, pRetVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SmallChange(self, pRetVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderAdviseEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a407b27b-0f6d-4427-9292-473c7bf93258}')
    @commethod(3)
    def AdviseEventAdded(self, eventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID, propertyIDs: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AdviseEventRemoved(self, eventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID, propertyIDs: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderFragment(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f7063da8-8359-439c-9297-bbc5299a7d87}')
    @commethod(3)
    def Navigate(self, direction: win32more.Windows.Win32.UI.Accessibility.NavigateDirection, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderFragment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRuntimeId(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_BoundingRectangle(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaRect)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEmbeddedFragmentRoots(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFocus(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_FragmentRoot(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderFragmentRoot)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderFragmentRoot(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{620ce2a5-ab8f-40a9-86cb-de3c75599b58}')
    @commethod(3)
    def ElementProviderFromPoint(self, x: Double, y: Double, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderFragment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFocus(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderFragment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderHostingAccessibles(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{24be0b07-d37d-487a-98cf-a13ed465e9b3}')
    @commethod(3)
    def GetEmbeddedAccessibles(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderHwndOverride(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1d5df27c-8947-4425-b8d9-79787bb460b8}')
    @commethod(3)
    def GetOverrideProviderForHwnd(self, hwnd: win32more.Windows.Win32.Foundation.HWND, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderSimple(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d6dd68d1-86fd-4332-8666-9abedea2d24c}')
    @commethod(3)
    def get_ProviderOptions(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ProviderOptions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPatternProvider(self, patternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID, pRetVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyValue(self, propertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, pRetVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_HostRawElementProvider(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderSimple2(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple
    _iid_ = Guid('{a0a839a9-8da1-4a82-806a-8e0d44e79f56}')
    @commethod(7)
    def ShowContextMenu(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderSimple3(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple2
    _iid_ = Guid('{fcf5d820-d7ec-4613-bdf6-42a84ce7daaf}')
    @commethod(8)
    def GetMetadataValue(self, targetId: Int32, metadataId: win32more.Windows.Win32.UI.Accessibility.UIA_METADATA_ID, returnVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRawElementProviderWindowlessSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0a2a93cc-bfad-42ac-9b2e-0991fb0d3ea0}')
    @commethod(3)
    def GetAdjacentFragment(self, direction: win32more.Windows.Win32.UI.Accessibility.NavigateDirection, ppParent: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderFragment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRuntimeIdPrefix(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRichEditUiaInformation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetBoundaryRectangle(self, pUiaRect: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaRect)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsVisible(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRicheditWindowlessAccessibility(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def CreateProvider(self, pSite: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderWindowlessSite, ppProvider: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IScrollItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2360c714-4bf1-4b26-ba65-9b21316127eb}')
    @commethod(3)
    def ScrollIntoView(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IScrollProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b38b8077-1fc3-42a5-8cae-d40c2215055a}')
    @commethod(3)
    def Scroll(self, horizontalAmount: win32more.Windows.Win32.UI.Accessibility.ScrollAmount, verticalAmount: win32more.Windows.Win32.UI.Accessibility.ScrollAmount) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetScrollPercent(self, horizontalPercent: Double, verticalPercent: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_HorizontalScrollPercent(self, pRetVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_VerticalScrollPercent(self, pRetVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_HorizontalViewSize(self, pRetVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_VerticalViewSize(self, pRetVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_HorizontallyScrollable(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_VerticallyScrollable(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISelectionItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2acad808-b2d4-452d-a407-91ff1ad167b2}')
    @commethod(3)
    def Select(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddToSelection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveFromSelection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_IsSelected(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_SelectionContainer(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISelectionProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fb8b03af-3bdf-48d4-bd36-1a65793be168}')
    @commethod(3)
    def GetSelection(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CanSelectMultiple(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_IsSelectionRequired(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISelectionProvider2(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.ISelectionProvider
    _iid_ = Guid('{14f68475-ee1c-44f6-a869-d239381f0fe7}')
    @commethod(6)
    def get_FirstSelectedItem(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_LastSelectedItem(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentSelectedItem(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ItemCount(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpreadsheetItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eaed4660-7b3d-4879-a2e6-365ce603f3d0}')
    @commethod(3)
    def get_Formula(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAnnotationObjects(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAnnotationTypes(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpreadsheetProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6f6b5d35-5525-4f80-b758-85473832ffc7}')
    @commethod(3)
    def GetItemByName(self, name: win32more.Windows.Win32.Foundation.PWSTR, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStylesProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{19b6b649-f5d7-4a6d-bdcb-129252be588a}')
    @commethod(3)
    def get_StyleId(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_StyleName(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_FillColor(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_FillPatternStyle(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Shape(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_FillPatternColor(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ExtendedProperties(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISynchronizedInputProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{29db1a06-02ce-4cf7-9b42-565d4fab20ee}')
    @commethod(3)
    def StartListening(self, inputType: win32more.Windows.Win32.UI.Accessibility.SynchronizedInputType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITableItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b9734fa6-771f-4d78-9c90-2517999349cd}')
    @commethod(3)
    def GetRowHeaderItems(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColumnHeaderItems(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITableProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9c860395-97b3-490a-b52a-858cc22af166}')
    @commethod(3)
    def GetRowHeaders(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColumnHeaders(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_RowOrColumnMajor(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.RowOrColumnMajor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextChildProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4c2de2b9-c88f-4f88-a111-f1d336b7d1a9}')
    @commethod(3)
    def get_TextContainer(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_TextRange(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextEditProvider(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.ITextProvider
    _iid_ = Guid('{ea3605b4-3a05-400e-b5f9-4e91b40f6176}')
    @commethod(9)
    def GetActiveComposition(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConversionTarget(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3589c92c-63f3-4367-99bb-ada653b77cf2}')
    @commethod(3)
    def GetSelection(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetVisibleRanges(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RangeFromChild(self, childElement: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RangeFromPoint(self, point: win32more.Windows.Win32.UI.Accessibility.UiaPoint, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_DocumentRange(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SupportedTextSelection(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.SupportedTextSelection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextProvider2(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.ITextProvider
    _iid_ = Guid('{0dc5e6ed-3e16-4bf1-8f9a-a979878bc195}')
    @commethod(9)
    def RangeFromAnnotation(self, annotationElement: win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCaretRange(self, isActive: POINTER(win32more.Windows.Win32.Foundation.BOOL), pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextRangeProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5347ad7b-c355-46f8-aff5-909033582f63}')
    @commethod(3)
    def Clone(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Compare(self, range: win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CompareEndpoints(self, endpoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, targetRange: win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider, targetEndpoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ExpandToEnclosingUnit(self, unit: win32more.Windows.Win32.UI.Accessibility.TextUnit) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindAttribute(self, attributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID, val: win32more.Windows.Win32.System.Variant.VARIANT, backward: win32more.Windows.Win32.Foundation.BOOL, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindText(self, text: win32more.Windows.Win32.Foundation.BSTR, backward: win32more.Windows.Win32.Foundation.BOOL, ignoreCase: win32more.Windows.Win32.Foundation.BOOL, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAttributeValue(self, attributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID, pRetVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBoundingRectangles(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetEnclosingElement(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetText(self, maxLength: Int32, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Move(self, unit: win32more.Windows.Win32.UI.Accessibility.TextUnit, count: Int32, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def MoveEndpointByUnit(self, endpoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, unit: win32more.Windows.Win32.UI.Accessibility.TextUnit, count: Int32, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def MoveEndpointByRange(self, endpoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, targetRange: win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider, targetEndpoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Select(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AddToSelection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RemoveFromSelection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ScrollIntoView(self, alignToTop: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetChildren(self, pRetVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextRangeProvider2(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.ITextRangeProvider
    _iid_ = Guid('{9bbce42c-1921-4f18-89ca-dba1910a0386}')
    @commethod(21)
    def ShowContextMenu(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IToggleProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56d00bd0-c4f4-433c-a836-1a52a57e0892}')
    @commethod(3)
    def Toggle(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ToggleState(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ToggleState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransformProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6829ddc4-4f91-4ffa-b86f-bd3e2987cb4c}')
    @commethod(3)
    def Move(self, x: Double, y: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Resize(self, width: Double, height: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Rotate(self, degrees: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CanMove(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CanResize(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CanRotate(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransformProvider2(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.ITransformProvider
    _iid_ = Guid('{4758742f-7ac2-460c-bc48-09fc09308a93}')
    @commethod(9)
    def Zoom(self, zoom: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CanZoom(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ZoomLevel(self, pRetVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ZoomMinimum(self, pRetVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ZoomMaximum(self, pRetVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ZoomByUnit(self, zoomUnit: win32more.Windows.Win32.UI.Accessibility.ZoomUnit) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30cbe57d-d9d0-452a-ab13-7ac5ac4825ee}')
    @commethod(3)
    def CompareElements(self, el1: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, el2: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, areSame: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CompareRuntimeIds(self, runtimeId1: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), runtimeId2: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), areSame: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRootElement(self, root: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ElementFromHandle(self, hwnd: win32more.Windows.Win32.Foundation.HWND, element: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ElementFromPoint(self, pt: win32more.Windows.Win32.Foundation.POINT, element: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFocusedElement(self, element: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRootElementBuildCache(self, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, root: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ElementFromHandleBuildCache(self, hwnd: win32more.Windows.Win32.Foundation.HWND, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, element: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ElementFromPointBuildCache(self, pt: win32more.Windows.Win32.Foundation.POINT, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, element: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFocusedElementBuildCache(self, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, element: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateTreeWalker(self, pCondition: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, walker: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTreeWalker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ControlViewWalker(self, walker: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTreeWalker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ContentViewWalker(self, walker: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTreeWalker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_RawViewWalker(self, walker: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTreeWalker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_RawViewCondition(self, condition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ControlViewCondition(self, condition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ContentViewCondition(self, condition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CreateCacheRequest(self, cacheRequest: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CreateTrueCondition(self, newCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateFalseCondition(self, newCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreatePropertyCondition(self, propertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, value: win32more.Windows.Win32.System.Variant.VARIANT, newCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def CreatePropertyConditionEx(self, propertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, value: win32more.Windows.Win32.System.Variant.VARIANT, flags: win32more.Windows.Win32.UI.Accessibility.PropertyConditionFlags, newCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CreateAndCondition(self, condition1: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, condition2: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, newCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def CreateAndConditionFromArray(self, conditions: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), newCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def CreateAndConditionFromNativeArray(self, conditions: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition), conditionCount: Int32, newCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def CreateOrCondition(self, condition1: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, condition2: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, newCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def CreateOrConditionFromArray(self, conditions: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), newCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CreateOrConditionFromNativeArray(self, conditions: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition), conditionCount: Int32, newCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def CreateNotCondition(self, condition: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, newCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def AddAutomationEventHandler(self, eventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def RemoveAutomationEventHandler(self, eventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def AddPropertyChangedEventHandlerNativeArray(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationPropertyChangedEventHandler, propertyArray: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID), propertyCount: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def AddPropertyChangedEventHandler(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationPropertyChangedEventHandler, propertyArray: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def RemovePropertyChangedEventHandler(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationPropertyChangedEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def AddStructureChangedEventHandler(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationStructureChangedEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def RemoveStructureChangedEventHandler(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationStructureChangedEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def AddFocusChangedEventHandler(self, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationFocusChangedEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def RemoveFocusChangedEventHandler(self, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationFocusChangedEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def RemoveAllEventHandlers(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def IntNativeArrayToSafeArray(self, array: POINTER(Int32), arrayCount: Int32, safeArray: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def IntSafeArrayToNativeArray(self, intArray: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), array: POINTER(POINTER(Int32)), arrayCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def RectToVariant(self, rc: win32more.Windows.Win32.Foundation.RECT, var: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def VariantToRect(self, var: win32more.Windows.Win32.System.Variant.VARIANT, rc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def SafeArrayToRectNativeArray(self, rects: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), rectArray: POINTER(POINTER(win32more.Windows.Win32.Foundation.RECT)), rectArrayCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def CreateProxyFactoryEntry(self, factory: win32more.Windows.Win32.UI.Accessibility.IUIAutomationProxyFactory, factoryEntry: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationProxyFactoryEntry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_ProxyFactoryMapping(self, factoryMapping: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationProxyFactoryMapping)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def GetPropertyProgrammaticName(self, property: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def GetPatternProgrammaticName(self, pattern: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def PollForPotentialSupportedPatterns(self, pElement: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, patternIds: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), patternNames: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def PollForPotentialSupportedProperties(self, pElement: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, propertyIds: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), propertyNames: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def CheckNotSupported(self, value: win32more.Windows.Win32.System.Variant.VARIANT, isNotSupported: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def get_ReservedNotSupportedValue(self, notSupportedValue: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_ReservedMixedAttributeValue(self, mixedAttributeValue: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def ElementFromIAccessible(self, accessible: win32more.Windows.Win32.UI.Accessibility.IAccessible, childId: Int32, element: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def ElementFromIAccessibleBuildCache(self, accessible: win32more.Windows.Win32.UI.Accessibility.IAccessible, childId: Int32, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, element: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomation2(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomation
    _iid_ = Guid('{34723aff-0c9d-49d0-9896-7ab52df8cd8a}')
    @commethod(58)
    def get_AutoSetFocus(self, autoSetFocus: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def put_AutoSetFocus(self, autoSetFocus: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def get_ConnectionTimeout(self, timeout: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def put_ConnectionTimeout(self, timeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def get_TransactionTimeout(self, timeout: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def put_TransactionTimeout(self, timeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomation3(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomation2
    _iid_ = Guid('{73d768da-9b51-4b89-936e-c209290973e7}')
    @commethod(64)
    def AddTextEditTextChangedEventHandler(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, textEditChangeType: win32more.Windows.Win32.UI.Accessibility.TextEditChangeType, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def RemoveTextEditTextChangedEventHandler(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomation4(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomation3
    _iid_ = Guid('{1189c02a-05f8-4319-8e21-e817e3db2860}')
    @commethod(66)
    def AddChangesEventHandler(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, changeTypes: POINTER(Int32), changesCount: Int32, pCacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationChangesEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def RemoveChangesEventHandler(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationChangesEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomation5(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomation4
    _iid_ = Guid('{25f700c8-d816-4057-a9dc-3cbdee77e256}')
    @commethod(68)
    def AddNotificationEventHandler(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationNotificationEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def RemoveNotificationEventHandler(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationNotificationEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomation6(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomation5
    _iid_ = Guid('{aae072da-29e3-413d-87a7-192dbf81ed10}')
    @commethod(70)
    def CreateEventHandlerGroup(self, handlerGroup: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationEventHandlerGroup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def AddEventHandlerGroup(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, handlerGroup: win32more.Windows.Win32.UI.Accessibility.IUIAutomationEventHandlerGroup) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def RemoveEventHandlerGroup(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, handlerGroup: win32more.Windows.Win32.UI.Accessibility.IUIAutomationEventHandlerGroup) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def get_ConnectionRecoveryBehavior(self, connectionRecoveryBehaviorOptions: POINTER(win32more.Windows.Win32.UI.Accessibility.ConnectionRecoveryBehaviorOptions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def put_ConnectionRecoveryBehavior(self, connectionRecoveryBehaviorOptions: win32more.Windows.Win32.UI.Accessibility.ConnectionRecoveryBehaviorOptions) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def get_CoalesceEvents(self, coalesceEventsOptions: POINTER(win32more.Windows.Win32.UI.Accessibility.CoalesceEventsOptions)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def put_CoalesceEvents(self, coalesceEventsOptions: win32more.Windows.Win32.UI.Accessibility.CoalesceEventsOptions) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def AddActiveTextPositionChangedEventHandler(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def RemoveActiveTextPositionChangedEventHandler(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationActiveTextPositionChangedEventHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f97933b0-8dae-4496-8997-5ba015fe0d82}')
    @commethod(3)
    def HandleActiveTextPositionChangedEvent(self, sender: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, range: win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationAndCondition(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition
    _iid_ = Guid('{a7d0af36-b912-45fe-9855-091ddc174aec}')
    @commethod(3)
    def get_ChildCount(self, childCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetChildrenAsNativeArray(self, childArray: POINTER(POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)), childArrayCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChildren(self, childArray: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationAnnotationPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9a175b21-339e-41b1-8e8b-623f6b681098}')
    @commethod(3)
    def get_CurrentAnnotationTypeId(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentAnnotationTypeName(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentAuthor(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentDateTime(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentTarget(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CachedAnnotationTypeId(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CachedAnnotationTypeName(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CachedAuthor(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CachedDateTime(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CachedTarget(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationBoolCondition(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition
    _iid_ = Guid('{1b4e1f2e-75eb-4d0b-8952-5a69988e2307}')
    @commethod(3)
    def get_BooleanValue(self, boolVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationCacheRequest(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b32a92b5-bc25-4078-9c08-d7ee95c48e03}')
    @commethod(3)
    def AddProperty(self, propertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddPattern(self, patternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Clone(self, clonedRequest: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_TreeScope(self, scope: POINTER(win32more.Windows.Win32.UI.Accessibility.TreeScope)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_TreeScope(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_TreeFilter(self, filter: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_TreeFilter(self, filter: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AutomationElementMode(self, mode: POINTER(win32more.Windows.Win32.UI.Accessibility.AutomationElementMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_AutomationElementMode(self, mode: win32more.Windows.Win32.UI.Accessibility.AutomationElementMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationChangesEventHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{58edca55-2c3e-4980-b1b9-56c17f27a2a0}')
    @commethod(3)
    def HandleChangesEvent(self, sender: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, uiaChanges: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaChangeInfo), changesCount: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationCondition(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{352ffba8-0973-437c-a61f-f64cafd81df9}')
class IUIAutomationCustomNavigationPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{01ea217a-1766-47ed-a6cc-acf492854b1f}')
    @commethod(3)
    def Navigate(self, direction: win32more.Windows.Win32.UI.Accessibility.NavigateDirection, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationDockPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fde5ef97-1464-48f6-90bf-43d0948e86ec}')
    @commethod(3)
    def SetDockPosition(self, dockPos: win32more.Windows.Win32.UI.Accessibility.DockPosition) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentDockPosition(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.DockPosition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CachedDockPosition(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.DockPosition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationDragPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dc7b570-1f54-4bad-bcda-d36a722fb7bd}')
    @commethod(3)
    def get_CurrentIsGrabbed(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CachedIsGrabbed(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentDropEffect(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CachedDropEffect(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentDropEffects(self, retVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CachedDropEffects(self, retVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCurrentGrabbedItems(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCachedGrabbedItems(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationDropTargetPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{69a095f7-eee4-430e-a46b-fb73b1ae39a5}')
    @commethod(3)
    def get_CurrentDropTargetEffect(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CachedDropTargetEffect(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentDropTargetEffects(self, retVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CachedDropTargetEffects(self, retVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d22108aa-8ac5-49a5-837b-37bbb3d7591e}')
    @commethod(3)
    def SetFocus(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRuntimeId(self, runtimeId: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindFirst(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, condition: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, found: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindAll(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, condition: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, found: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindFirstBuildCache(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, condition: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, found: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindAllBuildCache(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, condition: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, found: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def BuildUpdatedCache(self, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, updatedElement: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCurrentPropertyValue(self, propertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, retVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCurrentPropertyValueEx(self, propertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, ignoreDefaultValue: win32more.Windows.Win32.Foundation.BOOL, retVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCachedPropertyValue(self, propertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, retVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCachedPropertyValueEx(self, propertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, ignoreDefaultValue: win32more.Windows.Win32.Foundation.BOOL, retVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCurrentPatternAs(self, patternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID, riid: POINTER(Guid), patternObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCachedPatternAs(self, patternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID, riid: POINTER(Guid), patternObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCurrentPattern(self, patternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID, patternObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCachedPattern(self, patternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID, patternObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCachedParent(self, parent: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCachedChildren(self, children: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_CurrentProcessId(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_CurrentControlType(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CurrentLocalizedControlType(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_CurrentName(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_CurrentAcceleratorKey(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_CurrentAccessKey(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_CurrentHasKeyboardFocus(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_CurrentIsKeyboardFocusable(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_CurrentIsEnabled(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_CurrentAutomationId(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_CurrentClassName(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_CurrentHelpText(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_CurrentCulture(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_CurrentIsControlElement(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_CurrentIsContentElement(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_CurrentIsPassword(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_CurrentNativeWindowHandle(self, retVal: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_CurrentItemType(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_CurrentIsOffscreen(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_CurrentOrientation(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.OrientationType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_CurrentFrameworkId(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_CurrentIsRequiredForForm(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_CurrentItemStatus(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_CurrentBoundingRectangle(self, retVal: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_CurrentLabeledBy(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_CurrentAriaRole(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_CurrentAriaProperties(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def get_CurrentIsDataValidForForm(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_CurrentControllerFor(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_CurrentDescribedBy(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_CurrentFlowsTo(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def get_CurrentProviderDescription(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def get_CachedProcessId(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_CachedControlType(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def get_CachedLocalizedControlType(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_CachedName(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def get_CachedAcceleratorKey(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_CachedAccessKey(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def get_CachedHasKeyboardFocus(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_CachedIsKeyboardFocusable(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def get_CachedIsEnabled(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def get_CachedAutomationId(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def get_CachedClassName(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def get_CachedHelpText(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def get_CachedCulture(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_CachedIsControlElement(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def get_CachedIsContentElement(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def get_CachedIsPassword(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def get_CachedNativeWindowHandle(self, retVal: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def get_CachedItemType(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def get_CachedIsOffscreen(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def get_CachedOrientation(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.OrientationType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def get_CachedFrameworkId(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def get_CachedIsRequiredForForm(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def get_CachedItemStatus(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def get_CachedBoundingRectangle(self, retVal: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def get_CachedLabeledBy(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def get_CachedAriaRole(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def get_CachedAriaProperties(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def get_CachedIsDataValidForForm(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def get_CachedControllerFor(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def get_CachedDescribedBy(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def get_CachedFlowsTo(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def get_CachedProviderDescription(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def GetClickablePoint(self, clickable: POINTER(win32more.Windows.Win32.Foundation.POINT), gotClickable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement2(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement
    _iid_ = Guid('{6749c683-f70d-4487-a698-5f79d55290d6}')
    @commethod(85)
    def get_CurrentOptimizeForVisualContent(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def get_CachedOptimizeForVisualContent(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def get_CurrentLiveSetting(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.LiveSetting)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def get_CachedLiveSetting(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.LiveSetting)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def get_CurrentFlowsFrom(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def get_CachedFlowsFrom(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement3(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement2
    _iid_ = Guid('{8471df34-aee0-4a01-a7de-7db9af12c296}')
    @commethod(91)
    def ShowContextMenu(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def get_CurrentIsPeripheral(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def get_CachedIsPeripheral(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement4(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement3
    _iid_ = Guid('{3b6e233c-52fb-4063-a4c9-77c075c2a06b}')
    @commethod(94)
    def get_CurrentPositionInSet(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(95)
    def get_CurrentSizeOfSet(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def get_CurrentLevel(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(97)
    def get_CurrentAnnotationTypes(self, retVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def get_CurrentAnnotationObjects(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(99)
    def get_CachedPositionInSet(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(100)
    def get_CachedSizeOfSet(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(101)
    def get_CachedLevel(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(102)
    def get_CachedAnnotationTypes(self, retVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(103)
    def get_CachedAnnotationObjects(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement5(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement4
    _iid_ = Guid('{98141c1d-0d0e-4175-bbe2-6bff455842a7}')
    @commethod(104)
    def get_CurrentLandmarkType(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_LANDMARKTYPE_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(105)
    def get_CurrentLocalizedLandmarkType(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(106)
    def get_CachedLandmarkType(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_LANDMARKTYPE_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(107)
    def get_CachedLocalizedLandmarkType(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement6(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement5
    _iid_ = Guid('{4780d450-8bca-4977-afa5-a4a517f555e3}')
    @commethod(108)
    def get_CurrentFullDescription(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(109)
    def get_CachedFullDescription(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement7(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement6
    _iid_ = Guid('{204e8572-cfc3-4c11-b0c8-7da7420750b7}')
    @commethod(110)
    def FindFirstWithOptions(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, condition: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, traversalOptions: win32more.Windows.Win32.UI.Accessibility.TreeTraversalOptions, root: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, found: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(111)
    def FindAllWithOptions(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, condition: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, traversalOptions: win32more.Windows.Win32.UI.Accessibility.TreeTraversalOptions, root: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, found: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(112)
    def FindFirstWithOptionsBuildCache(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, condition: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, traversalOptions: win32more.Windows.Win32.UI.Accessibility.TreeTraversalOptions, root: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, found: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(113)
    def FindAllWithOptionsBuildCache(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, condition: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, traversalOptions: win32more.Windows.Win32.UI.Accessibility.TreeTraversalOptions, root: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, found: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(114)
    def GetCurrentMetadataValue(self, targetId: Int32, metadataId: win32more.Windows.Win32.UI.Accessibility.UIA_METADATA_ID, returnVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement8(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement7
    _iid_ = Guid('{8c60217d-5411-4cde-bcc0-1ceda223830c}')
    @commethod(115)
    def get_CurrentHeadingLevel(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(116)
    def get_CachedHeadingLevel(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElement9(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement8
    _iid_ = Guid('{39325fac-039d-440e-a3a3-5eb81a5cecc3}')
    @commethod(117)
    def get_CurrentIsDialog(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(118)
    def get_CachedIsDialog(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationElementArray(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{14314595-b4bc-4055-95f2-58f2e42c9855}')
    @commethod(3)
    def get_Length(self, length: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetElement(self, index: Int32, element: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationEventHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{146c3c17-f12e-4e22-8c27-f894b9b79c69}')
    @commethod(3)
    def HandleAutomationEvent(self, sender: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, eventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationEventHandlerGroup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c9ee12f2-c13b-4408-997c-639914377f4e}')
    @commethod(3)
    def AddActiveTextPositionChangedEventHandler(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddAutomationEventHandler(self, eventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddChangesEventHandler(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, changeTypes: POINTER(Int32), changesCount: Int32, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationChangesEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddNotificationEventHandler(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationNotificationEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddPropertyChangedEventHandler(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationPropertyChangedEventHandler, propertyArray: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID), propertyCount: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddStructureChangedEventHandler(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationStructureChangedEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddTextEditTextChangedEventHandler(self, scope: win32more.Windows.Win32.UI.Accessibility.TreeScope, textEditChangeType: win32more.Windows.Win32.UI.Accessibility.TextEditChangeType, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, handler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationExpandCollapsePattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{619be086-1f4e-4ee4-bafa-210128738730}')
    @commethod(3)
    def Expand(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Collapse(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentExpandCollapseState(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ExpandCollapseState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CachedExpandCollapseState(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ExpandCollapseState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationFocusChangedEventHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c270f6b5-5c69-4290-9745-7a7f97169468}')
    @commethod(3)
    def HandleFocusChangedEvent(self, sender: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationGridItemPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{78f8ef57-66c3-4e09-bd7c-e79b2004894d}')
    @commethod(3)
    def get_CurrentContainingGrid(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentRow(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentColumn(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentRowSpan(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentColumnSpan(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CachedContainingGrid(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CachedRow(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CachedColumn(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CachedRowSpan(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CachedColumnSpan(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationGridPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{414c3cdc-856b-4f5b-8538-3131c6302550}')
    @commethod(3)
    def GetItem(self, row: Int32, column: Int32, element: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentRowCount(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentColumnCount(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CachedRowCount(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CachedColumnCount(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationInvokePattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fb377fbe-8ea6-46d5-9c73-6499642d3059}')
    @commethod(3)
    def Invoke(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationItemContainerPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c690fdb2-27a8-423c-812d-429773c9084e}')
    @commethod(3)
    def FindItemByProperty(self, pStartAfter: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, propertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, value: win32more.Windows.Win32.System.Variant.VARIANT, pFound: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationLegacyIAccessiblePattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{828055ad-355b-4435-86d5-3b51c14a9b1b}')
    @commethod(3)
    def Select(self, flagsSelect: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DoDefaultAction(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(self, szValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentChildId(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentName(self, pszName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentValue(self, pszValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentDescription(self, pszDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentRole(self, pdwRole: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CurrentState(self, pdwState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CurrentHelp(self, pszHelp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_CurrentKeyboardShortcut(self, pszKeyboardShortcut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCurrentSelection(self, pvarSelectedChildren: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CurrentDefaultAction(self, pszDefaultAction: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CachedChildId(self, pRetVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_CachedName(self, pszName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_CachedValue(self, pszValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_CachedDescription(self, pszDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_CachedRole(self, pdwRole: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_CachedState(self, pdwState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_CachedHelp(self, pszHelp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_CachedKeyboardShortcut(self, pszKeyboardShortcut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetCachedSelection(self, pvarSelectedChildren: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_CachedDefaultAction(self, pszDefaultAction: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetIAccessible(self, ppAccessible: POINTER(win32more.Windows.Win32.UI.Accessibility.IAccessible)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationMultipleViewPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8d253c91-1dc5-4bb5-b18f-ade16fa495e8}')
    @commethod(3)
    def GetViewName(self, view: Int32, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCurrentView(self, view: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentCurrentView(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentSupportedViews(self, retVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CachedCurrentView(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCachedSupportedViews(self, retVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationNotCondition(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition
    _iid_ = Guid('{f528b657-847b-498c-8896-d52b565407a1}')
    @commethod(3)
    def GetChild(self, condition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationNotificationEventHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c7cb2637-e6c2-4d0c-85de-4948c02175c7}')
    @commethod(3)
    def HandleNotificationEvent(self, sender: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, notificationKind: win32more.Windows.Win32.UI.Accessibility.NotificationKind, notificationProcessing: win32more.Windows.Win32.UI.Accessibility.NotificationProcessing, displayString: win32more.Windows.Win32.Foundation.BSTR, activityId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationObjectModelPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71c284b3-c14d-4d14-981e-19751b0d756d}')
    @commethod(3)
    def GetUnderlyingObjectModel(self, retVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationOrCondition(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition
    _iid_ = Guid('{8753f032-3db1-47b5-a1fc-6e34a266c712}')
    @commethod(3)
    def get_ChildCount(self, childCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetChildrenAsNativeArray(self, childArray: POINTER(POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)), childArrayCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChildren(self, childArray: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationPatternHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d97022f3-a947-465e-8b2a-ac4315fa54e8}')
    @commethod(3)
    def CreateClientWrapper(self, pPatternInstance: win32more.Windows.Win32.UI.Accessibility.IUIAutomationPatternInstance, pClientWrapper: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Dispatch(self, pTarget: win32more.Windows.Win32.System.Com.IUnknown, index: UInt32, pParams: POINTER(win32more.Windows.Win32.UI.Accessibility.UIAutomationParameter), cParams: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationPatternInstance(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c03a7fe4-9431-409f-bed8-ae7c2299bc8d}')
    @commethod(3)
    def GetProperty(self, index: UInt32, cached: win32more.Windows.Win32.Foundation.BOOL, type: win32more.Windows.Win32.UI.Accessibility.UIAutomationType, pPtr: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CallMethod(self, index: UInt32, pParams: POINTER(win32more.Windows.Win32.UI.Accessibility.UIAutomationParameter), cParams: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationPropertyChangedEventHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{40cd37d4-c756-4b0c-8c6f-bddfeeb13b50}')
    @commethod(3)
    def HandlePropertyChangedEvent(self, sender: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, propertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, newValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationPropertyCondition(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition
    _iid_ = Guid('{99ebf2cb-5578-4267-9ad4-afd6ea77e94b}')
    @commethod(3)
    def get_PropertyId(self, propertyId: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_PropertyValue(self, propertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_PropertyConditionFlags(self, flags: POINTER(win32more.Windows.Win32.UI.Accessibility.PropertyConditionFlags)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationProxyFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{85b94ecd-849d-42b6-b94d-d6db23fdf5a4}')
    @commethod(3)
    def CreateProvider(self, hwnd: win32more.Windows.Win32.Foundation.HWND, idObject: Int32, idChild: Int32, provider: POINTER(win32more.Windows.Win32.UI.Accessibility.IRawElementProviderSimple)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ProxyFactoryId(self, factoryId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationProxyFactoryEntry(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d50e472e-b64b-490c-bca1-d30696f9f289}')
    @commethod(3)
    def get_ProxyFactory(self, factory: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationProxyFactory)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_ClassName(self, className: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_ImageName(self, imageName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_AllowSubstringMatch(self, allowSubstringMatch: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CanCheckBaseClass(self, canCheckBaseClass: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_NeedsAdviseEvents(self, adviseEvents: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_ClassName(self, className: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ImageName(self, imageName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_AllowSubstringMatch(self, allowSubstringMatch: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_CanCheckBaseClass(self, canCheckBaseClass: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_NeedsAdviseEvents(self, adviseEvents: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetWinEventsForAutomationEvent(self, eventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID, propertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, winEvents: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetWinEventsForAutomationEvent(self, eventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID, propertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID, winEvents: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationProxyFactoryMapping(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09e31e18-872d-4873-93d1-1e541ec133fd}')
    @commethod(3)
    def get_Count(self, count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTable(self, table: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEntry(self, index: UInt32, entry: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationProxyFactoryEntry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTable(self, factoryList: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InsertEntries(self, before: UInt32, factoryList: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InsertEntry(self, before: UInt32, factory: win32more.Windows.Win32.UI.Accessibility.IUIAutomationProxyFactoryEntry) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveEntry(self, index: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ClearTable(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RestoreDefaultTable(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationRangeValuePattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{59213f4f-7346-49e5-b120-80555987a148}')
    @commethod(3)
    def SetValue(self, val: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentValue(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentIsReadOnly(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentMaximum(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentMinimum(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentLargeChange(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentSmallChange(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CachedValue(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CachedIsReadOnly(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CachedMaximum(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_CachedMinimum(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CachedLargeChange(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CachedSmallChange(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationRegistrar(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8609c4ec-4a1a-4d88-a357-5a66e060e1cf}')
    @commethod(3)
    def RegisterProperty(self, property: POINTER(win32more.Windows.Win32.UI.Accessibility.UIAutomationPropertyInfo), propertyId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RegisterEvent(self, event: POINTER(win32more.Windows.Win32.UI.Accessibility.UIAutomationEventInfo), eventId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterPattern(self, pattern: POINTER(win32more.Windows.Win32.UI.Accessibility.UIAutomationPatternInfo), pPatternId: POINTER(Int32), pPatternAvailablePropertyId: POINTER(Int32), propertyIdCount: UInt32, pPropertyIds: POINTER(Int32), eventIdCount: UInt32, pEventIds: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationScrollItemPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b488300f-d015-4f19-9c29-bb595e3645ef}')
    @commethod(3)
    def ScrollIntoView(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationScrollPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{88f4d42a-e881-459d-a77c-73bbbb7e02dc}')
    @commethod(3)
    def Scroll(self, horizontalAmount: win32more.Windows.Win32.UI.Accessibility.ScrollAmount, verticalAmount: win32more.Windows.Win32.UI.Accessibility.ScrollAmount) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetScrollPercent(self, horizontalPercent: Double, verticalPercent: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentHorizontalScrollPercent(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentVerticalScrollPercent(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentHorizontalViewSize(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentVerticalViewSize(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentHorizontallyScrollable(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentVerticallyScrollable(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CachedHorizontalScrollPercent(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CachedVerticalScrollPercent(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_CachedHorizontalViewSize(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CachedVerticalViewSize(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CachedHorizontallyScrollable(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CachedVerticallyScrollable(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationSelectionItemPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a8efa66a-0fda-421a-9194-38021f3578ea}')
    @commethod(3)
    def Select(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddToSelection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveFromSelection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentIsSelected(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentSelectionContainer(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CachedIsSelected(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CachedSelectionContainer(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationSelectionPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5ed5202e-b2ac-47a6-b638-4b0bf140d78e}')
    @commethod(3)
    def GetCurrentSelection(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentCanSelectMultiple(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentIsSelectionRequired(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCachedSelection(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CachedCanSelectMultiple(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CachedIsSelectionRequired(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationSelectionPattern2(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationSelectionPattern
    _iid_ = Guid('{0532bfae-c011-4e32-a343-6d642d798555}')
    @commethod(9)
    def get_CurrentFirstSelectedItem(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentLastSelectedItem(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CurrentCurrentSelectedItem(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CurrentItemCount(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_CachedFirstSelectedItem(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CachedLastSelectedItem(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CachedCurrentSelectedItem(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CachedItemCount(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationSpreadsheetItemPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d4fb86c-8d34-40e1-8e83-62c15204e335}')
    @commethod(3)
    def get_CurrentFormula(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentAnnotationObjects(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentAnnotationTypes(self, retVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CachedFormula(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCachedAnnotationObjects(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCachedAnnotationTypes(self, retVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationSpreadsheetPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7517a7c8-faae-4de9-9f08-29b91e8595c1}')
    @commethod(3)
    def GetItemByName(self, name: win32more.Windows.Win32.Foundation.BSTR, element: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationStructureChangedEventHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e81d1b4e-11c5-42f8-9754-e7036c79f054}')
    @commethod(3)
    def HandleStructureChangedEvent(self, sender: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, changeType: win32more.Windows.Win32.UI.Accessibility.StructureChangeType, runtimeId: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationStylesPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{85b5f0a2-bd79-484a-ad2b-388c9838d5fb}')
    @commethod(3)
    def get_CurrentStyleId(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentStyleName(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentFillColor(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentFillPatternStyle(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentShape(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentFillPatternColor(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentExtendedProperties(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCurrentExtendedPropertiesAsArray(self, propertyArray: POINTER(POINTER(win32more.Windows.Win32.UI.Accessibility.ExtendedProperty)), propertyCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CachedStyleId(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CachedStyleName(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_CachedFillColor(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CachedFillPatternStyle(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CachedShape(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CachedFillPatternColor(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_CachedExtendedProperties(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCachedExtendedPropertiesAsArray(self, propertyArray: POINTER(POINTER(win32more.Windows.Win32.UI.Accessibility.ExtendedProperty)), propertyCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationSynchronizedInputPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2233be0b-afb7-448b-9fda-3b378aa5eae1}')
    @commethod(3)
    def StartListening(self, inputType: win32more.Windows.Win32.UI.Accessibility.SynchronizedInputType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTableItemPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0b964eb3-ef2e-4464-9c79-61d61737a27e}')
    @commethod(3)
    def GetCurrentRowHeaderItems(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentColumnHeaderItems(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCachedRowHeaderItems(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCachedColumnHeaderItems(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTablePattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{620e691c-ea96-4710-a850-754b24ce2417}')
    @commethod(3)
    def GetCurrentRowHeaders(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentColumnHeaders(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentRowOrColumnMajor(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.RowOrColumnMajor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCachedRowHeaders(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCachedColumnHeaders(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CachedRowOrColumnMajor(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.RowOrColumnMajor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextChildPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6552b038-ae05-40c8-abfd-aa08352aab86}')
    @commethod(3)
    def get_TextContainer(self, container: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_TextRange(self, range: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextEditPattern(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextPattern
    _iid_ = Guid('{17e21576-996c-4870-99d9-bff323380c06}')
    @commethod(9)
    def GetActiveComposition(self, range: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetConversionTarget(self, range: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextEditTextChangedEventHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{92faa680-e704-4156-931a-e32d5bb38f3f}')
    @commethod(3)
    def HandleTextEditTextChangedEvent(self, sender: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, textEditChangeType: win32more.Windows.Win32.UI.Accessibility.TextEditChangeType, eventStrings: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{32eba289-3583-42c9-9c59-3b6d9a1e9b6a}')
    @commethod(3)
    def RangeFromPoint(self, pt: win32more.Windows.Win32.Foundation.POINT, range: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RangeFromChild(self, child: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, range: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSelection(self, ranges: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRangeArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVisibleRanges(self, ranges: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRangeArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_DocumentRange(self, range: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SupportedTextSelection(self, supportedTextSelection: POINTER(win32more.Windows.Win32.UI.Accessibility.SupportedTextSelection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextPattern2(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextPattern
    _iid_ = Guid('{506a921a-fcc9-409f-b23b-37eb74106872}')
    @commethod(9)
    def RangeFromAnnotation(self, annotation: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, range: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCaretRange(self, isActive: POINTER(win32more.Windows.Win32.Foundation.BOOL), range: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextRange(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a543cc6a-f4ae-494b-8239-c814481187a8}')
    @commethod(3)
    def Clone(self, clonedRange: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Compare(self, range: win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange, areSame: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CompareEndpoints(self, srcEndPoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, range: win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange, targetEndPoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, compValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ExpandToEnclosingUnit(self, textUnit: win32more.Windows.Win32.UI.Accessibility.TextUnit) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindAttribute(self, attr: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID, val: win32more.Windows.Win32.System.Variant.VARIANT, backward: win32more.Windows.Win32.Foundation.BOOL, found: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindText(self, text: win32more.Windows.Win32.Foundation.BSTR, backward: win32more.Windows.Win32.Foundation.BOOL, ignoreCase: win32more.Windows.Win32.Foundation.BOOL, found: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAttributeValue(self, attr: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID, value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBoundingRectangles(self, boundingRects: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetEnclosingElement(self, enclosingElement: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetText(self, maxLength: Int32, text: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Move(self, unit: win32more.Windows.Win32.UI.Accessibility.TextUnit, count: Int32, moved: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def MoveEndpointByUnit(self, endpoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, unit: win32more.Windows.Win32.UI.Accessibility.TextUnit, count: Int32, moved: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def MoveEndpointByRange(self, srcEndPoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint, range: win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange, targetEndPoint: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Select(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AddToSelection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RemoveFromSelection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ScrollIntoView(self, alignToTop: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetChildren(self, children: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextRange2(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange
    _iid_ = Guid('{bb9b40e0-5e04-46bd-9be0-4b601b9afad4}')
    @commethod(21)
    def ShowContextMenu(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextRange3(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange2
    _iid_ = Guid('{6a315d69-5512-4c2e-85f0-53fce6dd4bc2}')
    @commethod(22)
    def GetEnclosingElementBuildCache(self, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, enclosingElement: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetChildrenBuildCache(self, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, children: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElementArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetAttributeValues(self, attributeIds: POINTER(win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID), attributeIdCount: Int32, attributeValues: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTextRangeArray(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ce4ae76a-e717-4c98-81ea-47371d028eb6}')
    @commethod(3)
    def get_Length(self, length: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetElement(self, index: Int32, element: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationTextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTogglePattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{94cf8058-9b8d-4ab9-8bfd-4cd0a33c8c70}')
    @commethod(3)
    def Toggle(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentToggleState(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ToggleState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CachedToggleState(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.ToggleState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTransformPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9b55844-a55d-4ef0-926d-569c16ff89bb}')
    @commethod(3)
    def Move(self, x: Double, y: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Resize(self, width: Double, height: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Rotate(self, degrees: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentCanMove(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentCanResize(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentCanRotate(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CachedCanMove(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CachedCanResize(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CachedCanRotate(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTransformPattern2(ComPtr):
    extends: win32more.Windows.Win32.UI.Accessibility.IUIAutomationTransformPattern
    _iid_ = Guid('{6d74d017-6ecb-4381-b38b-3c17a48ff1c2}')
    @commethod(12)
    def Zoom(self, zoomValue: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ZoomByUnit(self, zoomUnit: win32more.Windows.Win32.UI.Accessibility.ZoomUnit) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CurrentCanZoom(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CachedCanZoom(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CurrentZoomLevel(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_CachedZoomLevel(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_CurrentZoomMinimum(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_CachedZoomMinimum(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_CurrentZoomMaximum(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_CachedZoomMaximum(self, retVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationTreeWalker(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4042c624-389c-4afc-a630-9df854a541fc}')
    @commethod(3)
    def GetParentElement(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, parent: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFirstChildElement(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, first: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLastChildElement(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, last: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNextSiblingElement(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, next: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPreviousSiblingElement(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, previous: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def NormalizeElement(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, normalized: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetParentElementBuildCache(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, parent: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFirstChildElementBuildCache(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, first: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetLastChildElementBuildCache(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, last: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetNextSiblingElementBuildCache(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, next: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetPreviousSiblingElementBuildCache(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, previous: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def NormalizeElementBuildCache(self, element: win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement, cacheRequest: win32more.Windows.Win32.UI.Accessibility.IUIAutomationCacheRequest, normalized: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Condition(self, condition: POINTER(win32more.Windows.Win32.UI.Accessibility.IUIAutomationCondition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationValuePattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a94cd8b1-0844-4cd6-9d2d-640537ab39e9}')
    @commethod(3)
    def SetValue(self, val: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CurrentValue(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentIsReadOnly(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CachedValue(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CachedIsReadOnly(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationVirtualizedItemPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6ba3d7a6-04cf-4f11-8793-a8d1cde9969f}')
    @commethod(3)
    def Realize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIAutomationWindowPattern(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0faef453-9208-43ef-bbb2-3b485177864f}')
    @commethod(3)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WaitForInputIdle(self, milliseconds: Int32, success: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetWindowVisualState(self, state: win32more.Windows.Win32.UI.Accessibility.WindowVisualState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CurrentCanMaximize(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CurrentCanMinimize(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentIsModal(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CurrentIsTopmost(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentWindowVisualState(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.WindowVisualState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CurrentWindowInteractionState(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.WindowInteractionState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CachedCanMaximize(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_CachedCanMinimize(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CachedIsModal(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_CachedIsTopmost(self, retVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CachedWindowVisualState(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.WindowVisualState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_CachedWindowInteractionState(self, retVal: POINTER(win32more.Windows.Win32.UI.Accessibility.WindowInteractionState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IValueProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c7935180-6fb3-4201-b174-7df73adbf64a}')
    @commethod(3)
    def SetValue(self, val: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_Value(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_IsReadOnly(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVirtualizedItemProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cb98b665-2d35-4fac-ad35-f3c60d0c0b8b}')
    @commethod(3)
    def Realize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWindowProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{987df77b-db06-4d77-8f8a-86a9c3bb90b9}')
    @commethod(3)
    def SetVisualState(self, state: win32more.Windows.Win32.UI.Accessibility.WindowVisualState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WaitForInputIdle(self, milliseconds: Int32, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_CanMaximize(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_CanMinimize(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IsModal(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_WindowVisualState(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.WindowVisualState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_WindowInteractionState(self, pRetVal: POINTER(win32more.Windows.Win32.UI.Accessibility.WindowInteractionState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IsTopmost(self, pRetVal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNACCESSIBLECHILDREN(paccContainer: win32more.Windows.Win32.UI.Accessibility.IAccessible, iChildStart: Int32, cChildren: Int32, rgvarChildren: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pcObtained: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNACCESSIBLEOBJECTFROMPOINT(ptScreen: win32more.Windows.Win32.Foundation.POINT, ppacc: POINTER(win32more.Windows.Win32.UI.Accessibility.IAccessible), pvarChild: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNACCESSIBLEOBJECTFROMWINDOW(hwnd: win32more.Windows.Win32.Foundation.HWND, dwId: UInt32, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNCREATESTDACCESSIBLEOBJECT(hwnd: win32more.Windows.Win32.Foundation.HWND, idObject: Int32, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNLRESULTFROMOBJECT(riid: POINTER(Guid), wParam: win32more.Windows.Win32.Foundation.WPARAM, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.LRESULT: ...
@winfunctype_pointer
def LPFNOBJECTFROMLRESULT(lResult: win32more.Windows.Win32.Foundation.LRESULT, riid: POINTER(Guid), wParam: win32more.Windows.Win32.Foundation.WPARAM, ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
LiveSetting = Int32
Off: win32more.Windows.Win32.UI.Accessibility.LiveSetting = 0
Polite: win32more.Windows.Win32.UI.Accessibility.LiveSetting = 1
Assertive: win32more.Windows.Win32.UI.Accessibility.LiveSetting = 2
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
    pszWText: win32more.Windows.Win32.Foundation.PWSTR
NavigateDirection = Int32
NavigateDirection_Parent: win32more.Windows.Win32.UI.Accessibility.NavigateDirection = 0
NavigateDirection_NextSibling: win32more.Windows.Win32.UI.Accessibility.NavigateDirection = 1
NavigateDirection_PreviousSibling: win32more.Windows.Win32.UI.Accessibility.NavigateDirection = 2
NavigateDirection_FirstChild: win32more.Windows.Win32.UI.Accessibility.NavigateDirection = 3
NavigateDirection_LastChild: win32more.Windows.Win32.UI.Accessibility.NavigateDirection = 4
NormalizeState = Int32
NormalizeState_None: win32more.Windows.Win32.UI.Accessibility.NormalizeState = 0
NormalizeState_View: win32more.Windows.Win32.UI.Accessibility.NormalizeState = 1
NormalizeState_Custom: win32more.Windows.Win32.UI.Accessibility.NormalizeState = 2
NotificationKind = Int32
NotificationKind_ItemAdded: win32more.Windows.Win32.UI.Accessibility.NotificationKind = 0
NotificationKind_ItemRemoved: win32more.Windows.Win32.UI.Accessibility.NotificationKind = 1
NotificationKind_ActionCompleted: win32more.Windows.Win32.UI.Accessibility.NotificationKind = 2
NotificationKind_ActionAborted: win32more.Windows.Win32.UI.Accessibility.NotificationKind = 3
NotificationKind_Other: win32more.Windows.Win32.UI.Accessibility.NotificationKind = 4
NotificationProcessing = Int32
NotificationProcessing_ImportantAll: win32more.Windows.Win32.UI.Accessibility.NotificationProcessing = 0
NotificationProcessing_ImportantMostRecent: win32more.Windows.Win32.UI.Accessibility.NotificationProcessing = 1
NotificationProcessing_All: win32more.Windows.Win32.UI.Accessibility.NotificationProcessing = 2
NotificationProcessing_MostRecent: win32more.Windows.Win32.UI.Accessibility.NotificationProcessing = 3
NotificationProcessing_CurrentThenMostRecent: win32more.Windows.Win32.UI.Accessibility.NotificationProcessing = 4
OrientationType = Int32
OrientationType_None: win32more.Windows.Win32.UI.Accessibility.OrientationType = 0
OrientationType_Horizontal: win32more.Windows.Win32.UI.Accessibility.OrientationType = 1
OrientationType_Vertical: win32more.Windows.Win32.UI.Accessibility.OrientationType = 2
OutlineStyles = Int32
OutlineStyles_None: win32more.Windows.Win32.UI.Accessibility.OutlineStyles = 0
OutlineStyles_Outline: win32more.Windows.Win32.UI.Accessibility.OutlineStyles = 1
OutlineStyles_Shadow: win32more.Windows.Win32.UI.Accessibility.OutlineStyles = 2
OutlineStyles_Engraved: win32more.Windows.Win32.UI.Accessibility.OutlineStyles = 4
OutlineStyles_Embossed: win32more.Windows.Win32.UI.Accessibility.OutlineStyles = 8
PropertyConditionFlags = Int32
PropertyConditionFlags_None: win32more.Windows.Win32.UI.Accessibility.PropertyConditionFlags = 0
PropertyConditionFlags_IgnoreCase: win32more.Windows.Win32.UI.Accessibility.PropertyConditionFlags = 1
PropertyConditionFlags_MatchSubstring: win32more.Windows.Win32.UI.Accessibility.PropertyConditionFlags = 2
ProviderOptions = Int32
ProviderOptions_ClientSideProvider: win32more.Windows.Win32.UI.Accessibility.ProviderOptions = 1
ProviderOptions_ServerSideProvider: win32more.Windows.Win32.UI.Accessibility.ProviderOptions = 2
ProviderOptions_NonClientAreaProvider: win32more.Windows.Win32.UI.Accessibility.ProviderOptions = 4
ProviderOptions_OverrideProvider: win32more.Windows.Win32.UI.Accessibility.ProviderOptions = 8
ProviderOptions_ProviderOwnsSetFocus: win32more.Windows.Win32.UI.Accessibility.ProviderOptions = 16
ProviderOptions_UseComThreading: win32more.Windows.Win32.UI.Accessibility.ProviderOptions = 32
ProviderOptions_RefuseNonClientSupport: win32more.Windows.Win32.UI.Accessibility.ProviderOptions = 64
ProviderOptions_HasNativeIAccessible: win32more.Windows.Win32.UI.Accessibility.ProviderOptions = 128
ProviderOptions_UseClientCoordinates: win32more.Windows.Win32.UI.Accessibility.ProviderOptions = 256
ProviderType = Int32
ProviderType_BaseHwnd: win32more.Windows.Win32.UI.Accessibility.ProviderType = 0
ProviderType_Proxy: win32more.Windows.Win32.UI.Accessibility.ProviderType = 1
ProviderType_NonClientArea: win32more.Windows.Win32.UI.Accessibility.ProviderType = 2
RowOrColumnMajor = Int32
RowOrColumnMajor_RowMajor: win32more.Windows.Win32.UI.Accessibility.RowOrColumnMajor = 0
RowOrColumnMajor_ColumnMajor: win32more.Windows.Win32.UI.Accessibility.RowOrColumnMajor = 1
RowOrColumnMajor_Indeterminate: win32more.Windows.Win32.UI.Accessibility.RowOrColumnMajor = 2
class SERIALKEYSA(Structure):
    cbSize: UInt32
    dwFlags: win32more.Windows.Win32.UI.Accessibility.SERIALKEYS_FLAGS
    lpszActivePort: win32more.Windows.Win32.Foundation.PSTR
    lpszPort: win32more.Windows.Win32.Foundation.PSTR
    iBaudRate: UInt32
    iPortState: UInt32
    iActive: UInt32
class SERIALKEYSW(Structure):
    cbSize: UInt32
    dwFlags: win32more.Windows.Win32.UI.Accessibility.SERIALKEYS_FLAGS
    lpszActivePort: win32more.Windows.Win32.Foundation.PWSTR
    lpszPort: win32more.Windows.Win32.Foundation.PWSTR
    iBaudRate: UInt32
    iPortState: UInt32
    iActive: UInt32
SERIALKEYS = UnicodeAlias('SERIALKEYSW')
SERIALKEYS_FLAGS = UInt32
SERKF_AVAILABLE: win32more.Windows.Win32.UI.Accessibility.SERIALKEYS_FLAGS = 2
SERKF_INDICATOR: win32more.Windows.Win32.UI.Accessibility.SERIALKEYS_FLAGS = 4
SERKF_SERIALKEYSON: win32more.Windows.Win32.UI.Accessibility.SERIALKEYS_FLAGS = 1
class SOUNDSENTRYA(Structure):
    cbSize: UInt32
    dwFlags: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_FLAGS
    iFSTextEffect: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_TEXT_EFFECT
    iFSTextEffectMSec: UInt32
    iFSTextEffectColorBits: UInt32
    iFSGrafEffect: win32more.Windows.Win32.UI.Accessibility.SOUND_SENTRY_GRAPHICS_EFFECT
    iFSGrafEffectMSec: UInt32
    iFSGrafEffectColor: UInt32
    iWindowsEffect: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_WINDOWS_EFFECT
    iWindowsEffectMSec: UInt32
    lpszWindowsEffectDLL: win32more.Windows.Win32.Foundation.PSTR
    iWindowsEffectOrdinal: UInt32
class SOUNDSENTRYW(Structure):
    cbSize: UInt32
    dwFlags: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_FLAGS
    iFSTextEffect: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_TEXT_EFFECT
    iFSTextEffectMSec: UInt32
    iFSTextEffectColorBits: UInt32
    iFSGrafEffect: win32more.Windows.Win32.UI.Accessibility.SOUND_SENTRY_GRAPHICS_EFFECT
    iFSGrafEffectMSec: UInt32
    iFSGrafEffectColor: UInt32
    iWindowsEffect: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_WINDOWS_EFFECT
    iWindowsEffectMSec: UInt32
    lpszWindowsEffectDLL: win32more.Windows.Win32.Foundation.PWSTR
    iWindowsEffectOrdinal: UInt32
SOUNDSENTRY = UnicodeAlias('SOUNDSENTRYW')
SOUNDSENTRY_FLAGS = UInt32
SSF_SOUNDSENTRYON: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_FLAGS = 1
SSF_AVAILABLE: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_FLAGS = 2
SSF_INDICATOR: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_FLAGS = 4
SOUNDSENTRY_TEXT_EFFECT = UInt32
SSTF_BORDER: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_TEXT_EFFECT = 2
SSTF_CHARS: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_TEXT_EFFECT = 1
SSTF_DISPLAY: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_TEXT_EFFECT = 3
SSTF_NONE: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_TEXT_EFFECT = 0
SOUNDSENTRY_WINDOWS_EFFECT = UInt32
SSWF_CUSTOM: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_WINDOWS_EFFECT = 4
SSWF_DISPLAY: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_WINDOWS_EFFECT = 3
SSWF_NONE: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_WINDOWS_EFFECT = 0
SSWF_TITLE: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_WINDOWS_EFFECT = 1
SSWF_WINDOW: win32more.Windows.Win32.UI.Accessibility.SOUNDSENTRY_WINDOWS_EFFECT = 2
SOUND_SENTRY_GRAPHICS_EFFECT = UInt32
SSGF_DISPLAY: win32more.Windows.Win32.UI.Accessibility.SOUND_SENTRY_GRAPHICS_EFFECT = 3
SSGF_NONE: win32more.Windows.Win32.UI.Accessibility.SOUND_SENTRY_GRAPHICS_EFFECT = 0
class STICKYKEYS(Structure):
    cbSize: UInt32
    dwFlags: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS
STICKYKEYS_FLAGS = UInt32
SKF_STICKYKEYSON: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 1
SKF_AVAILABLE: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 2
SKF_HOTKEYACTIVE: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 4
SKF_CONFIRMHOTKEY: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 8
SKF_HOTKEYSOUND: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 16
SKF_INDICATOR: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 32
SKF_AUDIBLEFEEDBACK: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 64
SKF_TRISTATE: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 128
SKF_TWOKEYSOFF: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 256
SKF_LALTLATCHED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 268435456
SKF_LCTLLATCHED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 67108864
SKF_LSHIFTLATCHED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 16777216
SKF_RALTLATCHED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 536870912
SKF_RCTLLATCHED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 134217728
SKF_RSHIFTLATCHED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 33554432
SKF_LWINLATCHED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 1073741824
SKF_RWINLATCHED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 2147483648
SKF_LALTLOCKED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 1048576
SKF_LCTLLOCKED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 262144
SKF_LSHIFTLOCKED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 65536
SKF_RALTLOCKED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 2097152
SKF_RCTLLOCKED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 524288
SKF_RSHIFTLOCKED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 131072
SKF_LWINLOCKED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 4194304
SKF_RWINLOCKED: win32more.Windows.Win32.UI.Accessibility.STICKYKEYS_FLAGS = 8388608
SayAsInterpretAs = Int32
SayAsInterpretAs_None: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 0
SayAsInterpretAs_Spell: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 1
SayAsInterpretAs_Cardinal: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 2
SayAsInterpretAs_Ordinal: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 3
SayAsInterpretAs_Number: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 4
SayAsInterpretAs_Date: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 5
SayAsInterpretAs_Time: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 6
SayAsInterpretAs_Telephone: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 7
SayAsInterpretAs_Currency: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 8
SayAsInterpretAs_Net: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 9
SayAsInterpretAs_Url: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 10
SayAsInterpretAs_Address: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 11
SayAsInterpretAs_Alphanumeric: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 12
SayAsInterpretAs_Name: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 13
SayAsInterpretAs_Media: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 14
SayAsInterpretAs_Date_MonthDayYear: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 15
SayAsInterpretAs_Date_DayMonthYear: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 16
SayAsInterpretAs_Date_YearMonthDay: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 17
SayAsInterpretAs_Date_YearMonth: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 18
SayAsInterpretAs_Date_MonthYear: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 19
SayAsInterpretAs_Date_DayMonth: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 20
SayAsInterpretAs_Date_MonthDay: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 21
SayAsInterpretAs_Date_Year: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 22
SayAsInterpretAs_Time_HoursMinutesSeconds12: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 23
SayAsInterpretAs_Time_HoursMinutes12: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 24
SayAsInterpretAs_Time_HoursMinutesSeconds24: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 25
SayAsInterpretAs_Time_HoursMinutes24: win32more.Windows.Win32.UI.Accessibility.SayAsInterpretAs = 26
ScrollAmount = Int32
ScrollAmount_LargeDecrement: win32more.Windows.Win32.UI.Accessibility.ScrollAmount = 0
ScrollAmount_SmallDecrement: win32more.Windows.Win32.UI.Accessibility.ScrollAmount = 1
ScrollAmount_NoAmount: win32more.Windows.Win32.UI.Accessibility.ScrollAmount = 2
ScrollAmount_LargeIncrement: win32more.Windows.Win32.UI.Accessibility.ScrollAmount = 3
ScrollAmount_SmallIncrement: win32more.Windows.Win32.UI.Accessibility.ScrollAmount = 4
StructureChangeType = Int32
StructureChangeType_ChildAdded: win32more.Windows.Win32.UI.Accessibility.StructureChangeType = 0
StructureChangeType_ChildRemoved: win32more.Windows.Win32.UI.Accessibility.StructureChangeType = 1
StructureChangeType_ChildrenInvalidated: win32more.Windows.Win32.UI.Accessibility.StructureChangeType = 2
StructureChangeType_ChildrenBulkAdded: win32more.Windows.Win32.UI.Accessibility.StructureChangeType = 3
StructureChangeType_ChildrenBulkRemoved: win32more.Windows.Win32.UI.Accessibility.StructureChangeType = 4
StructureChangeType_ChildrenReordered: win32more.Windows.Win32.UI.Accessibility.StructureChangeType = 5
SupportedTextSelection = Int32
SupportedTextSelection_None: win32more.Windows.Win32.UI.Accessibility.SupportedTextSelection = 0
SupportedTextSelection_Single: win32more.Windows.Win32.UI.Accessibility.SupportedTextSelection = 1
SupportedTextSelection_Multiple: win32more.Windows.Win32.UI.Accessibility.SupportedTextSelection = 2
SynchronizedInputType = Int32
SynchronizedInputType_KeyUp: win32more.Windows.Win32.UI.Accessibility.SynchronizedInputType = 1
SynchronizedInputType_KeyDown: win32more.Windows.Win32.UI.Accessibility.SynchronizedInputType = 2
SynchronizedInputType_LeftMouseUp: win32more.Windows.Win32.UI.Accessibility.SynchronizedInputType = 4
SynchronizedInputType_LeftMouseDown: win32more.Windows.Win32.UI.Accessibility.SynchronizedInputType = 8
SynchronizedInputType_RightMouseUp: win32more.Windows.Win32.UI.Accessibility.SynchronizedInputType = 16
SynchronizedInputType_RightMouseDown: win32more.Windows.Win32.UI.Accessibility.SynchronizedInputType = 32
class TOGGLEKEYS(Structure):
    cbSize: UInt32
    dwFlags: UInt32
TextDecorationLineStyle = Int32
TextDecorationLineStyle_None: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 0
TextDecorationLineStyle_Single: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 1
TextDecorationLineStyle_WordsOnly: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 2
TextDecorationLineStyle_Double: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 3
TextDecorationLineStyle_Dot: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 4
TextDecorationLineStyle_Dash: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 5
TextDecorationLineStyle_DashDot: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 6
TextDecorationLineStyle_DashDotDot: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 7
TextDecorationLineStyle_Wavy: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 8
TextDecorationLineStyle_ThickSingle: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 9
TextDecorationLineStyle_DoubleWavy: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 11
TextDecorationLineStyle_ThickWavy: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 12
TextDecorationLineStyle_LongDash: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 13
TextDecorationLineStyle_ThickDash: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 14
TextDecorationLineStyle_ThickDashDot: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 15
TextDecorationLineStyle_ThickDashDotDot: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 16
TextDecorationLineStyle_ThickDot: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 17
TextDecorationLineStyle_ThickLongDash: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = 18
TextDecorationLineStyle_Other: win32more.Windows.Win32.UI.Accessibility.TextDecorationLineStyle = -1
TextEditChangeType = Int32
TextEditChangeType_None: win32more.Windows.Win32.UI.Accessibility.TextEditChangeType = 0
TextEditChangeType_AutoCorrect: win32more.Windows.Win32.UI.Accessibility.TextEditChangeType = 1
TextEditChangeType_Composition: win32more.Windows.Win32.UI.Accessibility.TextEditChangeType = 2
TextEditChangeType_CompositionFinalized: win32more.Windows.Win32.UI.Accessibility.TextEditChangeType = 3
TextEditChangeType_AutoComplete: win32more.Windows.Win32.UI.Accessibility.TextEditChangeType = 4
TextPatternRangeEndpoint = Int32
TextPatternRangeEndpoint_Start: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint = 0
TextPatternRangeEndpoint_End: win32more.Windows.Win32.UI.Accessibility.TextPatternRangeEndpoint = 1
TextUnit = Int32
TextUnit_Character: win32more.Windows.Win32.UI.Accessibility.TextUnit = 0
TextUnit_Format: win32more.Windows.Win32.UI.Accessibility.TextUnit = 1
TextUnit_Word: win32more.Windows.Win32.UI.Accessibility.TextUnit = 2
TextUnit_Line: win32more.Windows.Win32.UI.Accessibility.TextUnit = 3
TextUnit_Paragraph: win32more.Windows.Win32.UI.Accessibility.TextUnit = 4
TextUnit_Page: win32more.Windows.Win32.UI.Accessibility.TextUnit = 5
TextUnit_Document: win32more.Windows.Win32.UI.Accessibility.TextUnit = 6
ToggleState = Int32
ToggleState_Off: win32more.Windows.Win32.UI.Accessibility.ToggleState = 0
ToggleState_On: win32more.Windows.Win32.UI.Accessibility.ToggleState = 1
ToggleState_Indeterminate: win32more.Windows.Win32.UI.Accessibility.ToggleState = 2
TreeScope = Int32
TreeScope_None: win32more.Windows.Win32.UI.Accessibility.TreeScope = 0
TreeScope_Element: win32more.Windows.Win32.UI.Accessibility.TreeScope = 1
TreeScope_Children: win32more.Windows.Win32.UI.Accessibility.TreeScope = 2
TreeScope_Descendants: win32more.Windows.Win32.UI.Accessibility.TreeScope = 4
TreeScope_Parent: win32more.Windows.Win32.UI.Accessibility.TreeScope = 8
TreeScope_Ancestors: win32more.Windows.Win32.UI.Accessibility.TreeScope = 16
TreeScope_Subtree: win32more.Windows.Win32.UI.Accessibility.TreeScope = 7
TreeTraversalOptions = Int32
TreeTraversalOptions_Default: win32more.Windows.Win32.UI.Accessibility.TreeTraversalOptions = 0
TreeTraversalOptions_PostOrder: win32more.Windows.Win32.UI.Accessibility.TreeTraversalOptions = 1
TreeTraversalOptions_LastToFirstOrder: win32more.Windows.Win32.UI.Accessibility.TreeTraversalOptions = 2
UIA_ANNOTATIONTYPE = Int32
AnnotationType_Unknown: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60000
AnnotationType_SpellingError: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60001
AnnotationType_GrammarError: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60002
AnnotationType_Comment: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60003
AnnotationType_FormulaError: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60004
AnnotationType_TrackChanges: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60005
AnnotationType_Header: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60006
AnnotationType_Footer: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60007
AnnotationType_Highlighted: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60008
AnnotationType_Endnote: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60009
AnnotationType_Footnote: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60010
AnnotationType_InsertionChange: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60011
AnnotationType_DeletionChange: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60012
AnnotationType_MoveChange: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60013
AnnotationType_FormatChange: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60014
AnnotationType_UnsyncedChange: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60015
AnnotationType_EditingLockedChange: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60016
AnnotationType_ExternalChange: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60017
AnnotationType_ConflictingChange: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60018
AnnotationType_Author: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60019
AnnotationType_AdvancedProofingIssue: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60020
AnnotationType_DataValidationError: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60021
AnnotationType_CircularReferenceError: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60022
AnnotationType_Mathematics: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60023
AnnotationType_Sensitive: win32more.Windows.Win32.UI.Accessibility.UIA_ANNOTATIONTYPE = 60024
UIA_CHANGE_ID = Int32
UIA_SummaryChangeId: win32more.Windows.Win32.UI.Accessibility.UIA_CHANGE_ID = 90000
UIA_CONTROLTYPE_ID = Int32
UIA_ButtonControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50000
UIA_CalendarControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50001
UIA_CheckBoxControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50002
UIA_ComboBoxControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50003
UIA_EditControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50004
UIA_HyperlinkControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50005
UIA_ImageControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50006
UIA_ListItemControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50007
UIA_ListControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50008
UIA_MenuControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50009
UIA_MenuBarControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50010
UIA_MenuItemControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50011
UIA_ProgressBarControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50012
UIA_RadioButtonControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50013
UIA_ScrollBarControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50014
UIA_SliderControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50015
UIA_SpinnerControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50016
UIA_StatusBarControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50017
UIA_TabControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50018
UIA_TabItemControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50019
UIA_TextControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50020
UIA_ToolBarControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50021
UIA_ToolTipControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50022
UIA_TreeControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50023
UIA_TreeItemControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50024
UIA_CustomControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50025
UIA_GroupControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50026
UIA_ThumbControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50027
UIA_DataGridControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50028
UIA_DataItemControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50029
UIA_DocumentControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50030
UIA_SplitButtonControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50031
UIA_WindowControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50032
UIA_PaneControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50033
UIA_HeaderControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50034
UIA_HeaderItemControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50035
UIA_TableControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50036
UIA_TitleBarControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50037
UIA_SeparatorControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50038
UIA_SemanticZoomControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50039
UIA_AppBarControlTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_CONTROLTYPE_ID = 50040
UIA_EVENT_ID = Int32
UIA_ToolTipOpenedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20000
UIA_ToolTipClosedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20001
UIA_StructureChangedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20002
UIA_MenuOpenedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20003
UIA_AutomationPropertyChangedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20004
UIA_AutomationFocusChangedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20005
UIA_AsyncContentLoadedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20006
UIA_MenuClosedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20007
UIA_LayoutInvalidatedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20008
UIA_Invoke_InvokedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20009
UIA_SelectionItem_ElementAddedToSelectionEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20010
UIA_SelectionItem_ElementRemovedFromSelectionEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20011
UIA_SelectionItem_ElementSelectedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20012
UIA_Selection_InvalidatedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20013
UIA_Text_TextSelectionChangedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20014
UIA_Text_TextChangedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20015
UIA_Window_WindowOpenedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20016
UIA_Window_WindowClosedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20017
UIA_MenuModeStartEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20018
UIA_MenuModeEndEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20019
UIA_InputReachedTargetEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20020
UIA_InputReachedOtherElementEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20021
UIA_InputDiscardedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20022
UIA_SystemAlertEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20023
UIA_LiveRegionChangedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20024
UIA_HostedFragmentRootsInvalidatedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20025
UIA_Drag_DragStartEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20026
UIA_Drag_DragCancelEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20027
UIA_Drag_DragCompleteEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20028
UIA_DropTarget_DragEnterEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20029
UIA_DropTarget_DragLeaveEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20030
UIA_DropTarget_DroppedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20031
UIA_TextEdit_TextChangedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20032
UIA_TextEdit_ConversionTargetChangedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20033
UIA_ChangesEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20034
UIA_NotificationEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20035
UIA_ActiveTextPositionChangedEventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID = 20036
UIA_HEADINGLEVEL_ID = Int32
HeadingLevel_None: win32more.Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID = 80050
HeadingLevel1: win32more.Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID = 80051
HeadingLevel2: win32more.Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID = 80052
HeadingLevel3: win32more.Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID = 80053
HeadingLevel4: win32more.Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID = 80054
HeadingLevel5: win32more.Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID = 80055
HeadingLevel6: win32more.Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID = 80056
HeadingLevel7: win32more.Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID = 80057
HeadingLevel8: win32more.Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID = 80058
HeadingLevel9: win32more.Windows.Win32.UI.Accessibility.UIA_HEADINGLEVEL_ID = 80059
UIA_LANDMARKTYPE_ID = Int32
UIA_CustomLandmarkTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_LANDMARKTYPE_ID = 80000
UIA_FormLandmarkTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_LANDMARKTYPE_ID = 80001
UIA_MainLandmarkTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_LANDMARKTYPE_ID = 80002
UIA_NavigationLandmarkTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_LANDMARKTYPE_ID = 80003
UIA_SearchLandmarkTypeId: win32more.Windows.Win32.UI.Accessibility.UIA_LANDMARKTYPE_ID = 80004
UIA_METADATA_ID = Int32
UIA_SayAsInterpretAsMetadataId: win32more.Windows.Win32.UI.Accessibility.UIA_METADATA_ID = 100000
UIA_PATTERN_ID = Int32
UIA_InvokePatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10000
UIA_SelectionPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10001
UIA_ValuePatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10002
UIA_RangeValuePatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10003
UIA_ScrollPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10004
UIA_ExpandCollapsePatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10005
UIA_GridPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10006
UIA_GridItemPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10007
UIA_MultipleViewPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10008
UIA_WindowPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10009
UIA_SelectionItemPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10010
UIA_DockPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10011
UIA_TablePatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10012
UIA_TableItemPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10013
UIA_TextPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10014
UIA_TogglePatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10015
UIA_TransformPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10016
UIA_ScrollItemPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10017
UIA_LegacyIAccessiblePatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10018
UIA_ItemContainerPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10019
UIA_VirtualizedItemPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10020
UIA_SynchronizedInputPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10021
UIA_ObjectModelPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10022
UIA_AnnotationPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10023
UIA_TextPattern2Id: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10024
UIA_StylesPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10025
UIA_SpreadsheetPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10026
UIA_SpreadsheetItemPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10027
UIA_TransformPattern2Id: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10028
UIA_TextChildPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10029
UIA_DragPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10030
UIA_DropTargetPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10031
UIA_TextEditPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10032
UIA_CustomNavigationPatternId: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10033
UIA_SelectionPattern2Id: win32more.Windows.Win32.UI.Accessibility.UIA_PATTERN_ID = 10034
UIA_PROPERTY_ID = Int32
UIA_RuntimeIdPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30000
UIA_BoundingRectanglePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30001
UIA_ProcessIdPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30002
UIA_ControlTypePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30003
UIA_LocalizedControlTypePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30004
UIA_NamePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30005
UIA_AcceleratorKeyPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30006
UIA_AccessKeyPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30007
UIA_HasKeyboardFocusPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30008
UIA_IsKeyboardFocusablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30009
UIA_IsEnabledPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30010
UIA_AutomationIdPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30011
UIA_ClassNamePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30012
UIA_HelpTextPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30013
UIA_ClickablePointPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30014
UIA_CulturePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30015
UIA_IsControlElementPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30016
UIA_IsContentElementPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30017
UIA_LabeledByPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30018
UIA_IsPasswordPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30019
UIA_NativeWindowHandlePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30020
UIA_ItemTypePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30021
UIA_IsOffscreenPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30022
UIA_OrientationPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30023
UIA_FrameworkIdPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30024
UIA_IsRequiredForFormPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30025
UIA_ItemStatusPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30026
UIA_IsDockPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30027
UIA_IsExpandCollapsePatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30028
UIA_IsGridItemPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30029
UIA_IsGridPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30030
UIA_IsInvokePatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30031
UIA_IsMultipleViewPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30032
UIA_IsRangeValuePatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30033
UIA_IsScrollPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30034
UIA_IsScrollItemPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30035
UIA_IsSelectionItemPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30036
UIA_IsSelectionPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30037
UIA_IsTablePatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30038
UIA_IsTableItemPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30039
UIA_IsTextPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30040
UIA_IsTogglePatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30041
UIA_IsTransformPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30042
UIA_IsValuePatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30043
UIA_IsWindowPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30044
UIA_ValueValuePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30045
UIA_ValueIsReadOnlyPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30046
UIA_RangeValueValuePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30047
UIA_RangeValueIsReadOnlyPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30048
UIA_RangeValueMinimumPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30049
UIA_RangeValueMaximumPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30050
UIA_RangeValueLargeChangePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30051
UIA_RangeValueSmallChangePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30052
UIA_ScrollHorizontalScrollPercentPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30053
UIA_ScrollHorizontalViewSizePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30054
UIA_ScrollVerticalScrollPercentPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30055
UIA_ScrollVerticalViewSizePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30056
UIA_ScrollHorizontallyScrollablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30057
UIA_ScrollVerticallyScrollablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30058
UIA_SelectionSelectionPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30059
UIA_SelectionCanSelectMultiplePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30060
UIA_SelectionIsSelectionRequiredPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30061
UIA_GridRowCountPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30062
UIA_GridColumnCountPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30063
UIA_GridItemRowPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30064
UIA_GridItemColumnPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30065
UIA_GridItemRowSpanPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30066
UIA_GridItemColumnSpanPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30067
UIA_GridItemContainingGridPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30068
UIA_DockDockPositionPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30069
UIA_ExpandCollapseExpandCollapseStatePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30070
UIA_MultipleViewCurrentViewPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30071
UIA_MultipleViewSupportedViewsPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30072
UIA_WindowCanMaximizePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30073
UIA_WindowCanMinimizePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30074
UIA_WindowWindowVisualStatePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30075
UIA_WindowWindowInteractionStatePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30076
UIA_WindowIsModalPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30077
UIA_WindowIsTopmostPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30078
UIA_SelectionItemIsSelectedPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30079
UIA_SelectionItemSelectionContainerPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30080
UIA_TableRowHeadersPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30081
UIA_TableColumnHeadersPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30082
UIA_TableRowOrColumnMajorPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30083
UIA_TableItemRowHeaderItemsPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30084
UIA_TableItemColumnHeaderItemsPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30085
UIA_ToggleToggleStatePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30086
UIA_TransformCanMovePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30087
UIA_TransformCanResizePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30088
UIA_TransformCanRotatePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30089
UIA_IsLegacyIAccessiblePatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30090
UIA_LegacyIAccessibleChildIdPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30091
UIA_LegacyIAccessibleNamePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30092
UIA_LegacyIAccessibleValuePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30093
UIA_LegacyIAccessibleDescriptionPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30094
UIA_LegacyIAccessibleRolePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30095
UIA_LegacyIAccessibleStatePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30096
UIA_LegacyIAccessibleHelpPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30097
UIA_LegacyIAccessibleKeyboardShortcutPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30098
UIA_LegacyIAccessibleSelectionPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30099
UIA_LegacyIAccessibleDefaultActionPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30100
UIA_AriaRolePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30101
UIA_AriaPropertiesPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30102
UIA_IsDataValidForFormPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30103
UIA_ControllerForPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30104
UIA_DescribedByPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30105
UIA_FlowsToPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30106
UIA_ProviderDescriptionPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30107
UIA_IsItemContainerPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30108
UIA_IsVirtualizedItemPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30109
UIA_IsSynchronizedInputPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30110
UIA_OptimizeForVisualContentPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30111
UIA_IsObjectModelPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30112
UIA_AnnotationAnnotationTypeIdPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30113
UIA_AnnotationAnnotationTypeNamePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30114
UIA_AnnotationAuthorPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30115
UIA_AnnotationDateTimePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30116
UIA_AnnotationTargetPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30117
UIA_IsAnnotationPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30118
UIA_IsTextPattern2AvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30119
UIA_StylesStyleIdPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30120
UIA_StylesStyleNamePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30121
UIA_StylesFillColorPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30122
UIA_StylesFillPatternStylePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30123
UIA_StylesShapePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30124
UIA_StylesFillPatternColorPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30125
UIA_StylesExtendedPropertiesPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30126
UIA_IsStylesPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30127
UIA_IsSpreadsheetPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30128
UIA_SpreadsheetItemFormulaPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30129
UIA_SpreadsheetItemAnnotationObjectsPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30130
UIA_SpreadsheetItemAnnotationTypesPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30131
UIA_IsSpreadsheetItemPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30132
UIA_Transform2CanZoomPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30133
UIA_IsTransformPattern2AvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30134
UIA_LiveSettingPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30135
UIA_IsTextChildPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30136
UIA_IsDragPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30137
UIA_DragIsGrabbedPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30138
UIA_DragDropEffectPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30139
UIA_DragDropEffectsPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30140
UIA_IsDropTargetPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30141
UIA_DropTargetDropTargetEffectPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30142
UIA_DropTargetDropTargetEffectsPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30143
UIA_DragGrabbedItemsPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30144
UIA_Transform2ZoomLevelPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30145
UIA_Transform2ZoomMinimumPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30146
UIA_Transform2ZoomMaximumPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30147
UIA_FlowsFromPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30148
UIA_IsTextEditPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30149
UIA_IsPeripheralPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30150
UIA_IsCustomNavigationPatternAvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30151
UIA_PositionInSetPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30152
UIA_SizeOfSetPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30153
UIA_LevelPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30154
UIA_AnnotationTypesPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30155
UIA_AnnotationObjectsPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30156
UIA_LandmarkTypePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30157
UIA_LocalizedLandmarkTypePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30158
UIA_FullDescriptionPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30159
UIA_FillColorPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30160
UIA_OutlineColorPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30161
UIA_FillTypePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30162
UIA_VisualEffectsPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30163
UIA_OutlineThicknessPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30164
UIA_CenterPointPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30165
UIA_RotationPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30166
UIA_SizePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30167
UIA_IsSelectionPattern2AvailablePropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30168
UIA_Selection2FirstSelectedItemPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30169
UIA_Selection2LastSelectedItemPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30170
UIA_Selection2CurrentSelectedItemPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30171
UIA_Selection2ItemCountPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30172
UIA_HeadingLevelPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30173
UIA_IsDialogPropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID = 30174
UIA_STYLE_ID = Int32
StyleId_Custom: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70000
StyleId_Heading1: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70001
StyleId_Heading2: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70002
StyleId_Heading3: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70003
StyleId_Heading4: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70004
StyleId_Heading5: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70005
StyleId_Heading6: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70006
StyleId_Heading7: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70007
StyleId_Heading8: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70008
StyleId_Heading9: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70009
StyleId_Title: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70010
StyleId_Subtitle: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70011
StyleId_Normal: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70012
StyleId_Emphasis: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70013
StyleId_Quote: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70014
StyleId_BulletedList: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70015
StyleId_NumberedList: win32more.Windows.Win32.UI.Accessibility.UIA_STYLE_ID = 70016
UIA_TEXTATTRIBUTE_ID = Int32
UIA_AnimationStyleAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40000
UIA_BackgroundColorAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40001
UIA_BulletStyleAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40002
UIA_CapStyleAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40003
UIA_CultureAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40004
UIA_FontNameAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40005
UIA_FontSizeAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40006
UIA_FontWeightAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40007
UIA_ForegroundColorAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40008
UIA_HorizontalTextAlignmentAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40009
UIA_IndentationFirstLineAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40010
UIA_IndentationLeadingAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40011
UIA_IndentationTrailingAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40012
UIA_IsHiddenAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40013
UIA_IsItalicAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40014
UIA_IsReadOnlyAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40015
UIA_IsSubscriptAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40016
UIA_IsSuperscriptAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40017
UIA_MarginBottomAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40018
UIA_MarginLeadingAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40019
UIA_MarginTopAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40020
UIA_MarginTrailingAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40021
UIA_OutlineStylesAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40022
UIA_OverlineColorAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40023
UIA_OverlineStyleAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40024
UIA_StrikethroughColorAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40025
UIA_StrikethroughStyleAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40026
UIA_TabsAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40027
UIA_TextFlowDirectionsAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40028
UIA_UnderlineColorAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40029
UIA_UnderlineStyleAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40030
UIA_AnnotationTypesAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40031
UIA_AnnotationObjectsAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40032
UIA_StyleNameAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40033
UIA_StyleIdAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40034
UIA_LinkAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40035
UIA_IsActiveAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40036
UIA_SelectionActiveEndAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40037
UIA_CaretPositionAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40038
UIA_CaretBidiModeAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40039
UIA_LineSpacingAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40040
UIA_BeforeParagraphSpacingAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40041
UIA_AfterParagraphSpacingAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40042
UIA_SayAsInterpretAsAttributeId: win32more.Windows.Win32.UI.Accessibility.UIA_TEXTATTRIBUTE_ID = 40043
class UIAutomationEventInfo(Structure):
    guid: Guid
    pProgrammaticName: win32more.Windows.Win32.Foundation.PWSTR
class UIAutomationMethodInfo(Structure):
    pProgrammaticName: win32more.Windows.Win32.Foundation.PWSTR
    doSetFocus: win32more.Windows.Win32.Foundation.BOOL
    cInParameters: UInt32
    cOutParameters: UInt32
    pParameterTypes: POINTER(win32more.Windows.Win32.UI.Accessibility.UIAutomationType)
    pParameterNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
class UIAutomationParameter(Structure):
    type: win32more.Windows.Win32.UI.Accessibility.UIAutomationType
    pData: VoidPtr
class UIAutomationPatternInfo(Structure):
    guid: Guid
    pProgrammaticName: win32more.Windows.Win32.Foundation.PWSTR
    providerInterfaceId: Guid
    clientInterfaceId: Guid
    cProperties: UInt32
    pProperties: POINTER(win32more.Windows.Win32.UI.Accessibility.UIAutomationPropertyInfo)
    cMethods: UInt32
    pMethods: POINTER(win32more.Windows.Win32.UI.Accessibility.UIAutomationMethodInfo)
    cEvents: UInt32
    pEvents: POINTER(win32more.Windows.Win32.UI.Accessibility.UIAutomationEventInfo)
    pPatternHandler: win32more.Windows.Win32.UI.Accessibility.IUIAutomationPatternHandler
class UIAutomationPropertyInfo(Structure):
    guid: Guid
    pProgrammaticName: win32more.Windows.Win32.Foundation.PWSTR
    type: win32more.Windows.Win32.UI.Accessibility.UIAutomationType
UIAutomationType = Int32
UIAutomationType_Int: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 1
UIAutomationType_Bool: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 2
UIAutomationType_String: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 3
UIAutomationType_Double: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 4
UIAutomationType_Point: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 5
UIAutomationType_Rect: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 6
UIAutomationType_Element: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 7
UIAutomationType_Array: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 65536
UIAutomationType_Out: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 131072
UIAutomationType_IntArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 65537
UIAutomationType_BoolArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 65538
UIAutomationType_StringArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 65539
UIAutomationType_DoubleArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 65540
UIAutomationType_PointArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 65541
UIAutomationType_RectArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 65542
UIAutomationType_ElementArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 65543
UIAutomationType_OutInt: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 131073
UIAutomationType_OutBool: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 131074
UIAutomationType_OutString: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 131075
UIAutomationType_OutDouble: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 131076
UIAutomationType_OutPoint: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 131077
UIAutomationType_OutRect: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 131078
UIAutomationType_OutElement: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 131079
UIAutomationType_OutIntArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 196609
UIAutomationType_OutBoolArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 196610
UIAutomationType_OutStringArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 196611
UIAutomationType_OutDoubleArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 196612
UIAutomationType_OutPointArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 196613
UIAutomationType_OutRectArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 196614
UIAutomationType_OutElementArray: win32more.Windows.Win32.UI.Accessibility.UIAutomationType = 196615
class UiaAndOrCondition(Structure):
    ConditionType: win32more.Windows.Win32.UI.Accessibility.ConditionType
    ppConditions: POINTER(POINTER(win32more.Windows.Win32.UI.Accessibility.UiaCondition))
    cConditions: Int32
class UiaAsyncContentLoadedEventArgs(Structure):
    Type: win32more.Windows.Win32.UI.Accessibility.EventArgsType
    EventId: Int32
    AsyncContentLoadedState: win32more.Windows.Win32.UI.Accessibility.AsyncContentLoadedState
    PercentComplete: Double
class UiaCacheRequest(Structure):
    pViewCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaCondition)
    Scope: win32more.Windows.Win32.UI.Accessibility.TreeScope
    pProperties: POINTER(Int32)
    cProperties: Int32
    pPatterns: POINTER(Int32)
    cPatterns: Int32
    automationElementMode: win32more.Windows.Win32.UI.Accessibility.AutomationElementMode
class UiaChangeInfo(Structure):
    uiaId: Int32
    payload: win32more.Windows.Win32.System.Variant.VARIANT
    extraInfo: win32more.Windows.Win32.System.Variant.VARIANT
class UiaChangesEventArgs(Structure):
    Type: win32more.Windows.Win32.UI.Accessibility.EventArgsType
    EventId: Int32
    EventIdCount: Int32
    pUiaChanges: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaChangeInfo)
class UiaCondition(Structure):
    ConditionType: win32more.Windows.Win32.UI.Accessibility.ConditionType
class UiaEventArgs(Structure):
    Type: win32more.Windows.Win32.UI.Accessibility.EventArgsType
    EventId: Int32
@winfunctype_pointer
def UiaEventCallback(pArgs: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaEventArgs), pRequestedData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), pTreeStructure: win32more.Windows.Win32.Foundation.BSTR) -> Void: ...
class UiaFindParams(Structure):
    MaxDepth: Int32
    FindFirst: win32more.Windows.Win32.Foundation.BOOL
    ExcludeRoot: win32more.Windows.Win32.Foundation.BOOL
    pFindCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaCondition)
class UiaNotCondition(Structure):
    ConditionType: win32more.Windows.Win32.UI.Accessibility.ConditionType
    pCondition: POINTER(win32more.Windows.Win32.UI.Accessibility.UiaCondition)
class UiaPoint(Structure):
    x: Double
    y: Double
class UiaPropertyChangedEventArgs(Structure):
    Type: win32more.Windows.Win32.UI.Accessibility.EventArgsType
    EventId: win32more.Windows.Win32.UI.Accessibility.UIA_EVENT_ID
    PropertyId: Int32
    OldValue: win32more.Windows.Win32.System.Variant.VARIANT
    NewValue: win32more.Windows.Win32.System.Variant.VARIANT
class UiaPropertyCondition(Structure):
    ConditionType: win32more.Windows.Win32.UI.Accessibility.ConditionType
    PropertyId: win32more.Windows.Win32.UI.Accessibility.UIA_PROPERTY_ID
    Value: win32more.Windows.Win32.System.Variant.VARIANT
    Flags: win32more.Windows.Win32.UI.Accessibility.PropertyConditionFlags
@winfunctype_pointer
def UiaProviderCallback(hwnd: win32more.Windows.Win32.Foundation.HWND, providerType: win32more.Windows.Win32.UI.Accessibility.ProviderType) -> POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY): ...
class UiaRect(Structure):
    left: Double
    top: Double
    width: Double
    height: Double
class UiaStructureChangedEventArgs(Structure):
    Type: win32more.Windows.Win32.UI.Accessibility.EventArgsType
    EventId: Int32
    StructureChangeType: win32more.Windows.Win32.UI.Accessibility.StructureChangeType
    pRuntimeId: POINTER(Int32)
    cRuntimeIdLen: Int32
class UiaTextEditTextChangedEventArgs(Structure):
    Type: win32more.Windows.Win32.UI.Accessibility.EventArgsType
    EventId: Int32
    TextEditChangeType: win32more.Windows.Win32.UI.Accessibility.TextEditChangeType
    pTextChange: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)
class UiaWindowClosedEventArgs(Structure):
    Type: win32more.Windows.Win32.UI.Accessibility.EventArgsType
    EventId: Int32
    pRuntimeId: POINTER(Int32)
    cRuntimeIdLen: Int32
VisualEffects = Int32
VisualEffects_None: win32more.Windows.Win32.UI.Accessibility.VisualEffects = 0
VisualEffects_Shadow: win32more.Windows.Win32.UI.Accessibility.VisualEffects = 1
VisualEffects_Reflection: win32more.Windows.Win32.UI.Accessibility.VisualEffects = 2
VisualEffects_Glow: win32more.Windows.Win32.UI.Accessibility.VisualEffects = 4
VisualEffects_SoftEdges: win32more.Windows.Win32.UI.Accessibility.VisualEffects = 8
VisualEffects_Bevel: win32more.Windows.Win32.UI.Accessibility.VisualEffects = 16
@winfunctype_pointer
def WINEVENTPROC(hWinEventHook: win32more.Windows.Win32.UI.Accessibility.HWINEVENTHOOK, event: UInt32, hwnd: win32more.Windows.Win32.Foundation.HWND, idObject: Int32, idChild: Int32, idEventThread: UInt32, dwmsEventTime: UInt32) -> Void: ...
WindowInteractionState = Int32
WindowInteractionState_Running: win32more.Windows.Win32.UI.Accessibility.WindowInteractionState = 0
WindowInteractionState_Closing: win32more.Windows.Win32.UI.Accessibility.WindowInteractionState = 1
WindowInteractionState_ReadyForUserInteraction: win32more.Windows.Win32.UI.Accessibility.WindowInteractionState = 2
WindowInteractionState_BlockedByModalWindow: win32more.Windows.Win32.UI.Accessibility.WindowInteractionState = 3
WindowInteractionState_NotResponding: win32more.Windows.Win32.UI.Accessibility.WindowInteractionState = 4
WindowVisualState = Int32
WindowVisualState_Normal: win32more.Windows.Win32.UI.Accessibility.WindowVisualState = 0
WindowVisualState_Maximized: win32more.Windows.Win32.UI.Accessibility.WindowVisualState = 1
WindowVisualState_Minimized: win32more.Windows.Win32.UI.Accessibility.WindowVisualState = 2
ZoomUnit = Int32
ZoomUnit_NoAmount: win32more.Windows.Win32.UI.Accessibility.ZoomUnit = 0
ZoomUnit_LargeDecrement: win32more.Windows.Win32.UI.Accessibility.ZoomUnit = 1
ZoomUnit_SmallDecrement: win32more.Windows.Win32.UI.Accessibility.ZoomUnit = 2
ZoomUnit_LargeIncrement: win32more.Windows.Win32.UI.Accessibility.ZoomUnit = 3
ZoomUnit_SmallIncrement: win32more.Windows.Win32.UI.Accessibility.ZoomUnit = 4


make_ready(__name__)
