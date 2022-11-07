from win32more import *
import win32more.Foundation
import win32more.System.Com
import win32more.UI.Accessibility
import win32more.UI.WindowsAndMessaging

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
LIBID_Accessibility = '1ea4dbf0-3c3b-11cf-810c-00aa00389b71'
CLSID_AccPropServices = 'b5f8350b-0548-48b1-a6ee-88bd00b4a5e7'
IIS_IsOleaccProxy = '902697fa-80e4-4560-802a-a13f22a64709'
IIS_ControlAccessible = '38c682a6-9731-43f2-9fae-e901e641b101'
ANRUS_PRIORITY_AUDIO_DYNAMIC_DUCK = 16
MSAA_MENU_SIG = -1441927155
PROPID_ACC_NAME = '608d3df8-8128-4aa7-a428-f55e49267291'
PROPID_ACC_VALUE = '123fe443-211a-4615-9527-c45a7e93717a'
PROPID_ACC_DESCRIPTION = '4d48dfe4-bd3f-491f-a648-492d6f20c588'
PROPID_ACC_ROLE = 'cb905ff2-7bd1-4c05-b3c8-e6c241364d70'
PROPID_ACC_STATE = 'a8d4d5b0-0a21-42d0-a5c0-514e984f457b'
PROPID_ACC_HELP = 'c831e11f-44db-4a99-9768-cb8f978b7231'
PROPID_ACC_KEYBOARDSHORTCUT = '7d9bceee-7d1e-4979-9382-5180f4172c34'
PROPID_ACC_DEFAULTACTION = '180c072b-c27f-43c7-9922-f63562a4632b'
PROPID_ACC_HELPTOPIC = '787d1379-8ede-440b-8aec-11f7bf9030b3'
PROPID_ACC_FOCUS = '6eb335df-1c29-4127-b12c-dee9fd157f2b'
PROPID_ACC_SELECTION = 'b99d073c-d731-405b-9061-d95e8f842984'
PROPID_ACC_PARENT = '474c22b6-ffc2-467a-b1b5-e958b4657330'
PROPID_ACC_NAV_UP = '016e1a2b-1a4e-4767-8612-3386f66935ec'
PROPID_ACC_NAV_DOWN = '031670ed-3cdf-48d2-9613-138f2dd8a668'
PROPID_ACC_NAV_LEFT = '228086cb-82f1-4a39-8705-dcdc0fff92f5'
PROPID_ACC_NAV_RIGHT = 'cd211d9f-e1cb-4fe5-a77c-920b884d095b'
PROPID_ACC_NAV_PREV = '776d3891-c73b-4480-b3f6-076a16a15af6'
PROPID_ACC_NAV_NEXT = '1cdc5455-8cd9-4c92-a371-3939a2fe3eee'
PROPID_ACC_NAV_FIRSTCHILD = 'cfd02558-557b-4c67-84f9-2a09fce40749'
PROPID_ACC_NAV_LASTCHILD = '302ecaa5-48d5-4f8d-b671-1a8d20a77832'
PROPID_ACC_ROLEMAP = 'f79acda2-140d-4fe6-8914-208476328269'
PROPID_ACC_VALUEMAP = 'da1c3d79-fc5c-420e-b399-9d1533549e75'
PROPID_ACC_STATEMAP = '43946c5e-0ac0-4042-b525-07bbdbe17fa7'
PROPID_ACC_DESCRIPTIONMAP = '1ff1435f-8a14-477b-b226-a0abe279975d'
PROPID_ACC_DODEFAULTACTION = '1ba09523-2e3b-49a6-a059-59682a3c48fd'
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
RuntimeId_Property_GUID = 'a39eebfa-7fba-4c89-b4d4-b99e2de7d160'
BoundingRectangle_Property_GUID = '7bbfe8b2-3bfc-48dd-b729-c794b846e9a1'
ProcessId_Property_GUID = '40499998-9c31-4245-a403-87320e59eaf6'
ControlType_Property_GUID = 'ca774fea-28ac-4bc2-94ca-acec6d6c10a3'
LocalizedControlType_Property_GUID = '8763404f-a1bd-452a-89c4-3f01d3833806'
Name_Property_GUID = 'c3a6921b-4a99-44f1-bca6-61187052c431'
AcceleratorKey_Property_GUID = '514865df-2557-4cb9-aeed-6ced084ce52c'
AccessKey_Property_GUID = '06827b12-a7f9-4a15-917c-ffa5ad3eb0a7'
HasKeyboardFocus_Property_GUID = 'cf8afd39-3f46-4800-9656-b2bf12529905'
IsKeyboardFocusable_Property_GUID = 'f7b8552a-0859-4b37-b9cb-51e72092f29f'
IsEnabled_Property_GUID = '2109427f-da60-4fed-bf1b-264bdce6eb3a'
AutomationId_Property_GUID = 'c82c0500-b60e-4310-a267-303c531f8ee5'
ClassName_Property_GUID = '157b7215-894f-4b65-84e2-aac0da08b16b'
HelpText_Property_GUID = '08555685-0977-45c7-a7a6-abaf5684121a'
ClickablePoint_Property_GUID = '0196903b-b203-4818-a9f3-f08e675f2341'
Culture_Property_GUID = 'e2d74f27-3d79-4dc2-b88b-3044963a8afb'
IsControlElement_Property_GUID = '95f35085-abcc-4afd-a5f4-dbb46c230fdb'
IsContentElement_Property_GUID = '4bda64a8-f5d8-480b-8155-ef2e89adb672'
LabeledBy_Property_GUID = 'e5b8924b-fc8a-4a35-8031-cf78ac43e55e'
IsPassword_Property_GUID = 'e8482eb1-687c-497b-bebc-03be53ec1454'
NewNativeWindowHandle_Property_GUID = '5196b33b-380a-4982-95e1-91f3ef60e024'
ItemType_Property_GUID = 'cdda434d-6222-413b-a68a-325dd1d40f39'
IsOffscreen_Property_GUID = '03c3d160-db79-42db-a2ef-1c231eede507'
Orientation_Property_GUID = 'a01eee62-3884-4415-887e-678ec21e39ba'
FrameworkId_Property_GUID = 'dbfd9900-7e1a-4f58-b61b-7063120f773b'
IsRequiredForForm_Property_GUID = '4f5f43cf-59fb-4bde-a270-602e5e1141e9'
ItemStatus_Property_GUID = '51de0321-3973-43e7-8913-0b08e813c37f'
AriaRole_Property_GUID = 'dd207b95-be4a-4e0d-b727-63ace94b6916'
AriaProperties_Property_GUID = '4213678c-e025-4922-beb5-e43ba08e6221'
IsDataValidForForm_Property_GUID = '445ac684-c3fc-4dd9-acf8-845a579296ba'
ControllerFor_Property_GUID = '51124c8a-a5d2-4f13-9be6-7fa8ba9d3a90'
DescribedBy_Property_GUID = '7c5865b8-9992-40fd-8db0-6bf1d317f998'
FlowsTo_Property_GUID = 'e4f33d20-559a-47fb-a830-f9cb4ff1a70a'
ProviderDescription_Property_GUID = 'dca5708a-c16b-4cd9-b889-beb16a804904'
OptimizeForVisualContent_Property_GUID = '6a852250-c75a-4e5d-b858-e381b0f78861'
IsDockPatternAvailable_Property_GUID = '2600a4c4-2ff8-4c96-ae31-8fe619a13c6c'
IsExpandCollapsePatternAvailable_Property_GUID = '929d3806-5287-4725-aa16-222afc63d595'
IsGridItemPatternAvailable_Property_GUID = '5a43e524-f9a2-4b12-84c8-b48a3efedd34'
IsGridPatternAvailable_Property_GUID = '5622c26c-f0ef-4f3b-97cb-714c0868588b'
IsInvokePatternAvailable_Property_GUID = '4e725738-8364-4679-aa6c-f3f41931f750'
IsMultipleViewPatternAvailable_Property_GUID = 'ff0a31eb-8e25-469d-8d6e-e771a27c1b90'
IsRangeValuePatternAvailable_Property_GUID = 'fda4244a-eb4d-43ff-b5ad-ed36d373ec4c'
IsScrollPatternAvailable_Property_GUID = '3ebb7b4a-828a-4b57-9d22-2fea1632ed0d'
IsScrollItemPatternAvailable_Property_GUID = '1cad1a05-0927-4b76-97e1-0fcdb209b98a'
IsSelectionItemPatternAvailable_Property_GUID = '8becd62d-0bc3-4109-bee2-8e6715290e68'
IsSelectionPatternAvailable_Property_GUID = 'f588acbe-c769-4838-9a60-2686dc1188c4'
IsTablePatternAvailable_Property_GUID = 'cb83575f-45c2-4048-9c76-159715a139df'
IsTableItemPatternAvailable_Property_GUID = 'eb36b40d-8ea4-489b-a013-e60d5951fe34'
IsTextPatternAvailable_Property_GUID = 'fbe2d69d-aff6-4a45-82e2-fc92a82f5917'
IsTogglePatternAvailable_Property_GUID = '78686d53-fcd0-4b83-9b78-5832ce63bb5b'
IsTransformPatternAvailable_Property_GUID = 'a7f78804-d68b-4077-a5c6-7a5ea1ac31c5'
IsValuePatternAvailable_Property_GUID = '0b5020a7-2119-473b-be37-5ceb98bbfb22'
IsWindowPatternAvailable_Property_GUID = 'e7a57bb1-5888-4155-98dc-b422fd57f2bc'
IsLegacyIAccessiblePatternAvailable_Property_GUID = 'd8ebd0c7-929a-4ee7-8d3a-d3d94413027b'
IsItemContainerPatternAvailable_Property_GUID = '624b5ca7-fe40-4957-a019-20c4cf11920f'
IsVirtualizedItemPatternAvailable_Property_GUID = '302cb151-2ac8-45d6-977b-d2b3a5a53f20'
IsSynchronizedInputPatternAvailable_Property_GUID = '75d69cc5-d2bf-4943-876e-b45b62a6cc66'
IsObjectModelPatternAvailable_Property_GUID = '6b21d89b-2841-412f-8ef2-15ca952318ba'
IsAnnotationPatternAvailable_Property_GUID = '0b5b3238-6d5c-41b6-bcc4-5e807f6551c4'
IsTextPattern2Available_Property_GUID = '41cf921d-e3f1-4b22-9c81-e1c3ed331c22'
IsTextEditPatternAvailable_Property_GUID = '7843425c-8b32-484c-9ab5-e3200571ffda'
IsCustomNavigationPatternAvailable_Property_GUID = '8f8e80d4-2351-48e0-874a-54aa7313889a'
IsStylesPatternAvailable_Property_GUID = '27f353d3-459c-4b59-a490-50611dacafb5'
IsSpreadsheetPatternAvailable_Property_GUID = '6ff43732-e4b4-4555-97bc-ecdbbc4d1888'
IsSpreadsheetItemPatternAvailable_Property_GUID = '9fe79b2a-2f94-43fd-996b-549e316f4acd'
IsTransformPattern2Available_Property_GUID = '25980b4b-be04-4710-ab4a-fda31dbd2895'
IsTextChildPatternAvailable_Property_GUID = '559e65df-30ff-43b5-b5ed-5b283b80c7e9'
IsDragPatternAvailable_Property_GUID = 'e997a7b7-1d39-4ca7-be0f-277fcf5605cc'
IsDropTargetPatternAvailable_Property_GUID = '0686b62e-8e19-4aaf-873d-384f6d3b92be'
IsStructuredMarkupPatternAvailable_Property_GUID = 'b0d4c196-2c0b-489c-b165-a405928c6f3d'
IsPeripheral_Property_GUID = 'da758276-7ed5-49d4-8e68-ecc9a2d300dd'
PositionInSet_Property_GUID = '33d1dc54-641e-4d76-a6b1-13f341c1f896'
SizeOfSet_Property_GUID = '1600d33c-3b9f-4369-9431-aa293f344cf1'
Level_Property_GUID = '242ac529-cd36-400f-aad9-7876ef3af627'
AnnotationTypes_Property_GUID = '64b71f76-53c4-4696-a219-20e940c9a176'
AnnotationObjects_Property_GUID = '310910c8-7c6e-4f20-becd-4aaf6d191156'
LandmarkType_Property_GUID = '454045f2-6f61-49f7-a4f8-b5f0cf82da1e'
LocalizedLandmarkType_Property_GUID = '7ac81980-eafb-4fb2-bf91-f485bef5e8e1'
FullDescription_Property_GUID = '0d4450ff-6aef-4f33-95dd-7befa72a4391'
Value_Value_Property_GUID = 'e95f5e64-269f-4a85-ba99-4092c3ea2986'
Value_IsReadOnly_Property_GUID = 'eb090f30-e24c-4799-a705-0d247bc037f8'
RangeValue_Value_Property_GUID = '131f5d98-c50c-489d-abe5-ae220898c5f7'
RangeValue_IsReadOnly_Property_GUID = '25fa1055-debf-4373-a79e-1f1a1908d3c4'
RangeValue_Minimum_Property_GUID = '78cbd3b2-684d-4860-af93-d1f95cb022fd'
RangeValue_Maximum_Property_GUID = '19319914-f979-4b35-a1a6-d37e05433473'
RangeValue_LargeChange_Property_GUID = 'a1f96325-3a3d-4b44-8e1f-4a46d9844019'
RangeValue_SmallChange_Property_GUID = '81c2c457-3941-4107-9975-139760f7c072'
Scroll_HorizontalScrollPercent_Property_GUID = 'c7c13c0e-eb21-47ff-acc4-b5a3350f5191'
Scroll_HorizontalViewSize_Property_GUID = '70c2e5d4-fcb0-4713-a9aa-af92ff79e4cd'
Scroll_VerticalScrollPercent_Property_GUID = '6c8d7099-b2a8-4948-bff7-3cf9058bfefb'
Scroll_VerticalViewSize_Property_GUID = 'de6a2e22-d8c7-40c5-83ba-e5f681d53108'
Scroll_HorizontallyScrollable_Property_GUID = '8b925147-28cd-49ae-bd63-f44118d2e719'
Scroll_VerticallyScrollable_Property_GUID = '89164798-0068-4315-b89a-1e7cfbbc3dfc'
Selection_Selection_Property_GUID = 'aa6dc2a2-0e2b-4d38-96d5-34e470b81853'
Selection_CanSelectMultiple_Property_GUID = '49d73da5-c883-4500-883d-8fcf8daf6cbe'
Selection_IsSelectionRequired_Property_GUID = 'b1ae4422-63fe-44e7-a5a5-a738c829b19a'
Grid_RowCount_Property_GUID = '2a9505bf-c2eb-4fb6-b356-8245ae53703e'
Grid_ColumnCount_Property_GUID = 'fe96f375-44aa-4536-ac7a-2a75d71a3efc'
GridItem_Row_Property_GUID = '6223972a-c945-4563-9329-fdc974af2553'
GridItem_Column_Property_GUID = 'c774c15c-62c0-4519-8bdc-47be573c8ad5'
GridItem_RowSpan_Property_GUID = '4582291c-466b-4e93-8e83-3d1715ec0c5e'
GridItem_ColumnSpan_Property_GUID = '583ea3f5-86d0-4b08-a6ec-2c5463ffc109'
GridItem_Parent_Property_GUID = '9d912252-b97f-4ecc-8510-ea0e33427c72'
Dock_DockPosition_Property_GUID = '6d67f02e-c0b0-4b10-b5b9-18d6ecf98760'
ExpandCollapse_ExpandCollapseState_Property_GUID = '275a4c48-85a7-4f69-aba0-af157610002b'
MultipleView_CurrentView_Property_GUID = '7a81a67a-b94f-4875-918b-65c8d2f998e5'
MultipleView_SupportedViews_Property_GUID = '8d5db9fd-ce3c-4ae7-b788-400a3c645547'
Window_CanMaximize_Property_GUID = '64fff53f-635d-41c1-950c-cb5adfbe28e3'
Window_CanMinimize_Property_GUID = 'b73b4625-5988-4b97-b4c2-a6fe6e78c8c6'
Window_WindowVisualState_Property_GUID = '4ab7905f-e860-453e-a30a-f6431e5daad5'
Window_WindowInteractionState_Property_GUID = '4fed26a4-0455-4fa2-b21c-c4da2db1ff9c'
Window_IsModal_Property_GUID = 'ff4e6892-37b9-4fca-8532-ffe674ecfeed'
Window_IsTopmost_Property_GUID = 'ef7d85d3-0937-4962-9241-b62345f24041'
SelectionItem_IsSelected_Property_GUID = 'f122835f-cd5f-43df-b79d-4b849e9e6020'
SelectionItem_SelectionContainer_Property_GUID = 'a4365b6e-9c1e-4b63-8b53-c2421dd1e8fb'
Table_RowHeaders_Property_GUID = 'd9e35b87-6eb8-4562-aac6-a8a9075236a8'
Table_ColumnHeaders_Property_GUID = 'aff1d72b-968d-42b1-b459-150b299da664'
Table_RowOrColumnMajor_Property_GUID = '83be75c3-29fe-4a30-85e1-2a6277fd106e'
TableItem_RowHeaderItems_Property_GUID = 'b3f853a0-0574-4cd8-bcd7-ed5923572d97'
TableItem_ColumnHeaderItems_Property_GUID = '967a56a3-74b6-431e-8de6-99c411031c58'
Toggle_ToggleState_Property_GUID = 'b23cdc52-22c2-4c6c-9ded-f5c422479ede'
Transform_CanMove_Property_GUID = '1b75824d-208b-4fdf-bccd-f1f4e5741f4f'
Transform_CanResize_Property_GUID = 'bb98dca5-4c1a-41d4-a4f6-ebc128644180'
Transform_CanRotate_Property_GUID = '10079b48-3849-476f-ac96-44a95c8440d9'
LegacyIAccessible_ChildId_Property_GUID = '9a191b5d-9ef2-4787-a459-dcde885dd4e8'
LegacyIAccessible_Name_Property_GUID = 'caeb063d-40ae-4869-aa5a-1b8e5d666739'
LegacyIAccessible_Value_Property_GUID = 'b5c5b0b6-8217-4a77-97a5-190a85ed0156'
LegacyIAccessible_Description_Property_GUID = '46448418-7d70-4ea9-9d27-b7e775cf2ad7'
LegacyIAccessible_Role_Property_GUID = '6856e59f-cbaf-4e31-93e8-bcbf6f7e491c'
LegacyIAccessible_State_Property_GUID = 'df985854-2281-4340-ab9c-c60e2c5803f6'
LegacyIAccessible_Help_Property_GUID = '94402352-161c-4b77-a98d-a872cc33947a'
LegacyIAccessible_KeyboardShortcut_Property_GUID = '8f6909ac-00b8-4259-a41c-966266d43a8a'
LegacyIAccessible_Selection_Property_GUID = '8aa8b1e0-0891-40cc-8b06-90d7d4166219'
LegacyIAccessible_DefaultAction_Property_GUID = '3b331729-eaad-4502-b85f-92615622913c'
Annotation_AnnotationTypeId_Property_GUID = '20ae484f-69ef-4c48-8f5b-c4938b206ac7'
Annotation_AnnotationTypeName_Property_GUID = '9b818892-5ac9-4af9-aa96-f58a77b058e3'
Annotation_Author_Property_GUID = '7a528462-9c5c-4a03-a974-8b307a9937f2'
Annotation_DateTime_Property_GUID = '99b5ca5d-1acf-414b-a4d0-6b350b047578'
Annotation_Target_Property_GUID = 'b71b302d-2104-44ad-9c5c-092b4907d70f'
Styles_StyleId_Property_GUID = 'da82852f-3817-4233-82af-02279e72cc77'
Styles_StyleName_Property_GUID = '1c12b035-05d1-4f55-9e8e-1489f3ff550d'
Styles_FillColor_Property_GUID = '63eff97a-a1c5-4b1d-84eb-b765f2edd632'
Styles_FillPatternStyle_Property_GUID = '81cf651f-482b-4451-a30a-e1545e554fb8'
Styles_Shape_Property_GUID = 'c71a23f8-778c-400d-8458-3b543e526984'
Styles_FillPatternColor_Property_GUID = '939a59fe-8fbd-4e75-a271-ac4595195163'
Styles_ExtendedProperties_Property_GUID = 'f451cda0-ba0a-4681-b0b0-0dbdb53e58f3'
SpreadsheetItem_Formula_Property_GUID = 'e602e47d-1b47-4bea-87cf-3b0b0b5c15b6'
SpreadsheetItem_AnnotationObjects_Property_GUID = 'a3194c38-c9bc-4604-9396-ae3f9f457f7b'
SpreadsheetItem_AnnotationTypes_Property_GUID = 'c70c51d0-d602-4b45-afbc-b4712b96d72b'
Transform2_CanZoom_Property_GUID = 'f357e890-a756-4359-9ca6-86702bf8f381'
LiveSetting_Property_GUID = 'c12bcd8e-2a8e-4950-8ae7-3625111d58eb'
Drag_IsGrabbed_Property_GUID = '45f206f3-75cc-4cca-a9b9-fcdfb982d8a2'
Drag_GrabbedItems_Property_GUID = '77c1562c-7b86-4b21-9ed7-3cefda6f4c43'
Drag_DropEffect_Property_GUID = '646f2779-48d3-4b23-8902-4bf100005df3'
Drag_DropEffects_Property_GUID = 'f5d61156-7ce6-49be-a836-9269dcec920f'
DropTarget_DropTargetEffect_Property_GUID = '8bb75975-a0ca-4981-b818-87fc66e9509d'
DropTarget_DropTargetEffects_Property_GUID = 'bc1dd4ed-cb89-45f1-a592-e03b08ae790f'
Transform2_ZoomLevel_Property_GUID = 'eee29f1a-f4a2-4b5b-ac65-95cf93283387'
Transform2_ZoomMinimum_Property_GUID = '742ccc16-4ad1-4e07-96fe-b122c6e6b22b'
Transform2_ZoomMaximum_Property_GUID = '42ab6b77-ceb0-4eca-b82a-6cfa5fa1fc08'
FlowsFrom_Property_GUID = '05c6844f-19de-48f8-95fa-880d5b0fd615'
FillColor_Property_GUID = '6e0ec4d0-e2a8-4a56-9de7-953389933b39'
OutlineColor_Property_GUID = 'c395d6c0-4b55-4762-a073-fd303a634f52'
FillType_Property_GUID = 'c6fc74e4-8cb9-429c-a9e1-9bc4ac372b62'
VisualEffects_Property_GUID = 'e61a8565-aad9-46d7-9e70-4e8a8420d420'
OutlineThickness_Property_GUID = '13e67cc7-dac2-4888-bdd3-375c62fa9618'
CenterPoint_Property_GUID = '0cb00c08-540c-4edb-9445-26359ea69785'
Rotation_Property_GUID = '767cdc7d-aec0-4110-ad32-30edd403492e'
Size_Property_GUID = '2b5f761d-f885-4404-973f-9b1d98e36d8f'
ToolTipOpened_Event_GUID = '3f4b97ff-2edc-451d-bca4-95a3188d5b03'
ToolTipClosed_Event_GUID = '276d71ef-24a9-49b6-8e97-da98b401bbcd'
StructureChanged_Event_GUID = '59977961-3edd-4b11-b13b-676b2a2a6ca9'
MenuOpened_Event_GUID = 'ebe2e945-66ca-4ed1-9ff8-2ad7df0a1b08'
AutomationPropertyChanged_Event_GUID = '2527fba1-8d7a-4630-a4cc-e66315942f52'
AutomationFocusChanged_Event_GUID = 'b68a1f17-f60d-41a7-a3cc-b05292155fe0'
ActiveTextPositionChanged_Event_GUID = 'a5c09e9c-c77d-4f25-b491-e5bb7017cbd4'
AsyncContentLoaded_Event_GUID = '5fdee11c-d2fa-4fb9-904e-5cbee894d5ef'
MenuClosed_Event_GUID = '3cf1266e-1582-4041-acd7-88a35a965297'
LayoutInvalidated_Event_GUID = 'ed7d6544-a6bd-4595-9bae-3d28946cc715'
Invoke_Invoked_Event_GUID = 'dfd699f0-c915-49dd-b422-dde785c3d24b'
SelectionItem_ElementAddedToSelectionEvent_Event_GUID = '3c822dd1-c407-4dba-91dd-79d4aed0aec6'
SelectionItem_ElementRemovedFromSelectionEvent_Event_GUID = '097fa8a9-7079-41af-8b9c-0934d8305e5c'
SelectionItem_ElementSelectedEvent_Event_GUID = 'b9c7dbfb-4ebe-4532-aaf4-008cf647233c'
Selection_InvalidatedEvent_Event_GUID = 'cac14904-16b4-4b53-8e47-4cb1df267bb7'
Text_TextSelectionChangedEvent_Event_GUID = '918edaa1-71b3-49ae-9741-79beb8d358f3'
Text_TextChangedEvent_Event_GUID = '4a342082-f483-48c4-ac11-a84b435e2a84'
Window_WindowOpened_Event_GUID = 'd3e81d06-de45-4f2f-9633-de9e02fb65af'
Window_WindowClosed_Event_GUID = 'edf141f8-fa67-4e22-bbf7-944e05735ee2'
MenuModeStart_Event_GUID = '18d7c631-166a-4ac9-ae3b-ef4b5420e681'
MenuModeEnd_Event_GUID = '9ecd4c9f-80dd-47b8-8267-5aec06bb2cff'
InputReachedTarget_Event_GUID = '93ed549a-0549-40f0-bedb-28e44f7de2a3'
InputReachedOtherElement_Event_GUID = 'ed201d8a-4e6c-415e-a874-2460c9b66ba8'
InputDiscarded_Event_GUID = '7f36c367-7b18-417c-97e3-9d58ddc944ab'
SystemAlert_Event_GUID = 'd271545d-7a3a-47a7-8474-81d29a2451c9'
LiveRegionChanged_Event_GUID = '102d5e90-e6a9-41b6-b1c5-a9b1929d9510'
HostedFragmentRootsInvalidated_Event_GUID = 'e6bdb03e-0921-4ec5-8dcf-eae877b0426b'
Drag_DragStart_Event_GUID = '883a480b-3aa9-429d-95e4-d9c8d011f0dd'
Drag_DragCancel_Event_GUID = 'c3ede6fa-3451-4e0f-9e71-df9c280a4657'
Drag_DragComplete_Event_GUID = '38e96188-ef1f-463e-91ca-3a7792c29caf'
DropTarget_DragEnter_Event_GUID = 'aad9319b-032c-4a88-961d-1cf579581e34'
DropTarget_DragLeave_Event_GUID = '0f82eb15-24a2-4988-9217-de162aee272b'
DropTarget_Dropped_Event_GUID = '622cead8-1edb-4a3d-abbc-be2211ff68b5'
StructuredMarkup_CompositionComplete_Event_GUID = 'c48a3c17-677a-4047-a68d-fc1257528aef'
StructuredMarkup_Deleted_Event_GUID = 'f9d0a020-e1c1-4ecf-b9aa-52efde7e41e1'
StructuredMarkup_SelectionChanged_Event_GUID = 'a7c815f7-ff9f-41c7-a3a7-ab6cbfdb4903'
Invoke_Pattern_GUID = 'd976c2fc-66ea-4a6e-b28f-c24c7546ad37'
Selection_Pattern_GUID = '66e3b7e8-d821-4d25-8761-435d2c8b253f'
Value_Pattern_GUID = '17faad9e-c877-475b-b933-77332779b637'
RangeValue_Pattern_GUID = '18b00d87-b1c9-476a-bfbd-5f0bdb926f63'
Scroll_Pattern_GUID = '895fa4b4-759d-4c50-8e15-03460672003c'
ExpandCollapse_Pattern_GUID = 'ae05efa2-f9d1-428a-834c-53a5c52f9b8b'
Grid_Pattern_GUID = '260a2ccb-93a8-4e44-a4c1-3df397f2b02b'
GridItem_Pattern_GUID = 'f2d5c877-a462-4957-a2a5-2c96b303bc63'
MultipleView_Pattern_GUID = '547a6ae4-113f-47c4-850f-db4dfa466b1d'
Window_Pattern_GUID = '27901735-c760-4994-ad11-5919e606b110'
SelectionItem_Pattern_GUID = '9bc64eeb-87c7-4b28-94bb-4d9fa437b6ef'
Dock_Pattern_GUID = '9cbaa846-83c8-428d-827f-7e6063fe0620'
Table_Pattern_GUID = 'c415218e-a028-461e-aa92-8f925cf79351'
TableItem_Pattern_GUID = 'df1343bd-1888-4a29-a50c-b92e6de37f6f'
Text_Pattern_GUID = '8615f05d-7de5-44fd-a679-2ca4b46033a8'
Toggle_Pattern_GUID = '0b419760-e2f4-43ff-8c5f-9457c82b56e9'
Transform_Pattern_GUID = '24b46fdb-587e-49f1-9c4a-d8e98b664b7b'
ScrollItem_Pattern_GUID = '4591d005-a803-4d5c-b4d5-8d2800f906a7'
LegacyIAccessible_Pattern_GUID = '54cc0a9f-3395-48af-ba8d-73f85690f3e0'
ItemContainer_Pattern_GUID = '3d13da0f-8b9a-4a99-85fa-c5c9a69f1ed4'
VirtualizedItem_Pattern_GUID = 'f510173e-2e71-45e9-a6e5-62f6ed8289d5'
SynchronizedInput_Pattern_GUID = '05c288a6-c47b-488b-b653-33977a551b8b'
ObjectModel_Pattern_GUID = '3e04acfe-08fc-47ec-96bc-353fa3b34aa7'
Annotation_Pattern_GUID = 'f6c72ad7-356c-4850-9291-316f608a8c84'
Text_Pattern2_GUID = '498479a2-5b22-448d-b6e4-647490860698'
TextEdit_Pattern_GUID = '69f3ff89-5af9-4c75-9340-f2de292e4591'
CustomNavigation_Pattern_GUID = 'afea938a-621e-4054-bb2c-2f46114dac3f'
Styles_Pattern_GUID = '1ae62655-da72-4d60-a153-e5aa6988e3bf'
Spreadsheet_Pattern_GUID = '6a5b24c9-9d1e-4b85-9e44-c02e3169b10b'
SpreadsheetItem_Pattern_GUID = '32cf83ff-f1a8-4a8c-8658-d47ba74e20ba'
Tranform_Pattern2_GUID = '8afcfd07-a369-44de-988b-2f7ff49fb8a8'
TextChild_Pattern_GUID = '7533cab7-3bfe-41ef-9e85-e2638cbe169e'
Drag_Pattern_GUID = 'c0bee21f-ccb3-4fed-995b-114f6e3d2728'
DropTarget_Pattern_GUID = '0bcbec56-bd34-4b7b-9fd5-2659905ea3dc'
StructuredMarkup_Pattern_GUID = 'abbd0878-8665-4f5c-94fc-36e7d8bb706b'
Button_Control_GUID = '5a78e369-c6a1-4f33-a9d7-79f20d0c788e'
Calendar_Control_GUID = '8913eb88-00e5-46bc-8e4e-14a786e165a1'
CheckBox_Control_GUID = 'fb50f922-a3db-49c0-8bc3-06dad55778e2'
ComboBox_Control_GUID = '54cb426c-2f33-4fff-aaa1-aef60dac5deb'
Edit_Control_GUID = '6504a5c8-2c86-4f87-ae7b-1abddc810cf9'
Hyperlink_Control_GUID = '8a56022c-b00d-4d15-8ff0-5b6b266e5e02'
Image_Control_GUID = '2d3736e4-6b16-4c57-a962-f93260a75243'
ListItem_Control_GUID = '7b3717f2-44d1-4a58-98a8-f12a9b8f78e2'
List_Control_GUID = '9b149ee1-7cca-4cfc-9af1-cac7bddd3031'
Menu_Control_GUID = '2e9b1440-0ea8-41fd-b374-c1ea6f503cd1'
MenuBar_Control_GUID = 'cc384250-0e7b-4ae8-95ae-a08f261b52ee'
MenuItem_Control_GUID = 'f45225d3-d0a0-49d8-9834-9a000d2aeddc'
ProgressBar_Control_GUID = '228c9f86-c36c-47bb-9fb6-a5834bfc53a4'
RadioButton_Control_GUID = '3bdb49db-fe2c-4483-b3e1-e57f219440c6'
ScrollBar_Control_GUID = 'daf34b36-5065-4946-b22f-92595fc0751a'
Slider_Control_GUID = 'b033c24b-3b35-4cea-b609-763682fa660b'
Spinner_Control_GUID = '60cc4b38-3cb1-4161-b442-c6b726c17825'
StatusBar_Control_GUID = 'd45e7d1b-5873-475f-95a4-0433e1f1b00a'
Tab_Control_GUID = '38cd1f2d-337a-4bd2-a5e3-adb469e30bd3'
TabItem_Control_GUID = '2c6a634f-921b-4e6e-b26e-08fcb0798f4c'
Text_Control_GUID = 'ae9772dc-d331-4f09-be20-7e6dfaf07b0a'
ToolBar_Control_GUID = '8f06b751-e182-4e98-8893-2284543a7dce'
ToolTip_Control_GUID = '05ddc6d1-2137-4768-98ea-73f52f7134f3'
Tree_Control_GUID = '7561349c-d241-43f4-9908-b5f091bee611'
TreeItem_Control_GUID = '62c9feb9-8ffc-4878-a3a4-96b030315c18'
Custom_Control_GUID = 'f29ea0c3-adb7-430a-ba90-e52c7313e6ed'
Group_Control_GUID = 'ad50aa1c-e8c8-4774-ae1b-dd86df0b3bdc'
Thumb_Control_GUID = '701ca877-e310-4dd6-b644-797e4faea213'
DataGrid_Control_GUID = '84b783af-d103-4b0a-8415-e73942410f4b'
DataItem_Control_GUID = 'a0177842-d94f-42a5-814b-6068addc8da5'
Document_Control_GUID = '3cd6bb6f-6f08-4562-b229-e4e2fc7a9eb4'
SplitButton_Control_GUID = '7011f01f-4ace-4901-b461-920a6f1ca650'
Window_Control_GUID = 'e13a7242-f462-4f4d-aec1-53b28d6c3290'
Pane_Control_GUID = '5c2b3f5b-9182-42a3-8dec-8c04c1ee634d'
Header_Control_GUID = '5b90cbce-78fb-4614-82b6-554d74718e67'
HeaderItem_Control_GUID = 'e6bc12cb-7c8e-49cf-b168-4a93a32bebb0'
Table_Control_GUID = '773bfa0e-5bc4-4deb-921b-de7b3206229e'
TitleBar_Control_GUID = '98aa55bf-3bb0-4b65-836e-2ea30dbc171f'
Separator_Control_GUID = '8767eba3-2a63-4ab0-ac8d-aa50e23de978'
SemanticZoom_Control_GUID = '5fd34a43-061e-42c8-b589-9dccf74bc43a'
AppBar_Control_GUID = '6114908d-cc02-4d37-875b-b530c7139554'
Text_AnimationStyle_Attribute_GUID = '628209f0-7c9a-4d57-be64-1f1836571ff5'
Text_BackgroundColor_Attribute_GUID = 'fdc49a07-583d-4f17-ad27-77fc832a3c0b'
Text_BulletStyle_Attribute_GUID = 'c1097c90-d5c4-4237-9781-3bec8ba54e48'
Text_CapStyle_Attribute_GUID = 'fb059c50-92cc-49a5-ba8f-0aa872bba2f3'
Text_Culture_Attribute_GUID = 'c2025af9-a42d-4ced-a1fb-c6746315222e'
Text_FontName_Attribute_GUID = '64e63ba8-f2e5-476e-a477-1734feaaf726'
Text_FontSize_Attribute_GUID = 'dc5eeeff-0506-4673-93f2-377e4a8e01f1'
Text_FontWeight_Attribute_GUID = '6fc02359-b316-4f5f-b401-f1ce55741853'
Text_ForegroundColor_Attribute_GUID = '72d1c95d-5e60-471a-96b1-6c1b3b77a436'
Text_HorizontalTextAlignment_Attribute_GUID = '04ea6161-fba3-477a-952a-bb326d026a5b'
Text_IndentationFirstLine_Attribute_GUID = '206f9ad5-c1d3-424a-8182-6da9a7f3d632'
Text_IndentationLeading_Attribute_GUID = '5cf66bac-2d45-4a4b-b6c9-f7221d2815b0'
Text_IndentationTrailing_Attribute_GUID = '97ff6c0f-1ce4-408a-b67b-94d83eb69bf2'
Text_IsHidden_Attribute_GUID = '360182fb-bdd7-47f6-ab69-19e33f8a3344'
Text_IsItalic_Attribute_GUID = 'fce12a56-1336-4a34-9663-1bab47239320'
Text_IsReadOnly_Attribute_GUID = 'a738156b-ca3e-495e-9514-833c440feb11'
Text_IsSubscript_Attribute_GUID = 'f0ead858-8f53-413c-873f-1a7d7f5e0de4'
Text_IsSuperscript_Attribute_GUID = 'da706ee4-b3aa-4645-a41f-cd25157dea76'
Text_MarginBottom_Attribute_GUID = '7ee593c4-72b4-4cac-9271-3ed24b0e4d42'
Text_MarginLeading_Attribute_GUID = '9e9242d0-5ed0-4900-8e8a-eecc03835afc'
Text_MarginTop_Attribute_GUID = '683d936f-c9b9-4a9a-b3d9-d20d33311e2a'
Text_MarginTrailing_Attribute_GUID = 'af522f98-999d-40af-a5b2-0169d0342002'
Text_OutlineStyles_Attribute_GUID = '5b675b27-db89-46fe-970c-614d523bb97d'
Text_OverlineColor_Attribute_GUID = '83ab383a-fd43-40da-ab3e-ecf8165cbb6d'
Text_OverlineStyle_Attribute_GUID = '0a234d66-617e-427f-871d-e1ff1e0c213f'
Text_StrikethroughColor_Attribute_GUID = 'bfe15a18-8c41-4c5a-9a0b-04af0e07f487'
Text_StrikethroughStyle_Attribute_GUID = '72913ef1-da00-4f01-899c-ac5a8577a307'
Text_Tabs_Attribute_GUID = '2e68d00b-92fe-42d8-899a-a784aa4454a1'
Text_TextFlowDirections_Attribute_GUID = '8bdf8739-f420-423e-af77-20a5d973a907'
Text_UnderlineColor_Attribute_GUID = 'bfa12c73-fde2-4473-bf64-1036d6aa0f45'
Text_UnderlineStyle_Attribute_GUID = '5f3b21c0-ede4-44bd-9c36-3853038cbfeb'
Text_AnnotationTypes_Attribute_GUID = 'ad2eb431-ee4e-4be1-a7ba-5559155a73ef'
Text_AnnotationObjects_Attribute_GUID = 'ff41cf68-e7ab-40b9-8c72-72a8ed94017d'
Text_StyleName_Attribute_GUID = '22c9e091-4d66-45d8-a828-737bab4c98a7'
Text_StyleId_Attribute_GUID = '14c300de-c32b-449b-ab7c-b0e0789aea5d'
Text_Link_Attribute_GUID = 'b38ef51d-9e8d-4e46-9144-56ebe177329b'
Text_IsActive_Attribute_GUID = 'f5a4e533-e1b8-436b-935d-b57aa3f558c4'
Text_SelectionActiveEnd_Attribute_GUID = '1f668cc3-9bbf-416b-b0a2-f89f86f6612c'
Text_CaretPosition_Attribute_GUID = 'b227b131-9889-4752-a91b-733efdc5c5a0'
Text_CaretBidiMode_Attribute_GUID = '929ee7a6-51d3-4715-96dc-b694fa24a168'
Text_BeforeParagraphSpacing_Attribute_GUID = 'be7b0ab1-c822-4a24-85e9-c8f2650fc79c'
Text_AfterParagraphSpacing_Attribute_GUID = '588cbb38-e62f-497c-b5d1-ccdf0ee823d8'
Text_LineSpacing_Attribute_GUID = '63ff70ae-d943-4b47-8ab7-a7a033d3214b'
Text_BeforeSpacing_Attribute_GUID = 'be7b0ab1-c822-4a24-85e9-c8f2650fc79c'
Text_AfterSpacing_Attribute_GUID = '588cbb38-e62f-497c-b5d1-ccdf0ee823d8'
Text_SayAsInterpretAs_Attribute_GUID = 'b38ad6ac-eee1-4b6e-88cc-014cefa93fcb'
TextEdit_TextChanged_Event_GUID = '120b0308-ec22-4eb8-9c98-9867cda1b165'
TextEdit_ConversionTargetChanged_Event_GUID = '3388c183-ed4f-4c8b-9baa-364d51d8847f'
Changes_Event_GUID = '7df26714-614f-4e05-9488-716c5ba19436'
Annotation_Custom_GUID = '9ec82750-3931-4952-85bc-1dbff78a43e3'
Annotation_SpellingError_GUID = 'ae85567e-9ece-423f-81b7-96c43d53e50e'
Annotation_GrammarError_GUID = '757a048d-4518-41c6-854c-dc009b7cfb53'
Annotation_Comment_GUID = 'fd2fda30-26b3-4c06-8bc7-98f1532e46fd'
Annotation_FormulaError_GUID = '95611982-0cab-46d5-a2f0-e30d1905f8bf'
Annotation_TrackChanges_GUID = '21e6e888-dc14-4016-ac27-190553c8c470'
Annotation_Header_GUID = '867b409b-b216-4472-a219-525e310681f8'
Annotation_Footer_GUID = 'cceab046-1833-47aa-8080-701ed0b0c832'
Annotation_Highlighted_GUID = '757c884e-8083-4081-8b9c-e87f5072f0e4'
Annotation_Endnote_GUID = '7565725c-2d99-4839-960d-33d3b866aba5'
Annotation_Footnote_GUID = '3de10e21-4125-42db-8620-be8083080624'
Annotation_InsertionChange_GUID = '0dbeb3a6-df15-4164-a3c0-e21a8ce931c4'
Annotation_DeletionChange_GUID = 'be3d5b05-951d-42e7-901d-adc8c2cf34d0'
Annotation_MoveChange_GUID = '9da587eb-23e5-4490-b385-1a22ddc8b187'
Annotation_FormatChange_GUID = 'eb247345-d4f1-41ce-8e52-f79b69635e48'
Annotation_UnsyncedChange_GUID = '1851116a-0e47-4b30-8cb5-d7dae4fbcd1b'
Annotation_EditingLockedChange_GUID = 'c31f3e1c-7423-4dac-8348-41f099ff6f64'
Annotation_ExternalChange_GUID = '75a05b31-5f11-42fd-887d-dfa010db2392'
Annotation_ConflictingChange_GUID = '98af8802-517c-459f-af13-016d3fab877e'
Annotation_Author_GUID = 'f161d3a7-f81b-4128-b17f-71f690914520'
Annotation_AdvancedProofingIssue_GUID = 'dac7b72c-c0f2-4b84-b90d-5fafc0f0ef1c'
Annotation_DataValidationError_GUID = 'c8649fa8-9775-437e-ad46-e709d93c2343'
Annotation_CircularReferenceError_GUID = '25bd9cf4-1745-4659-ba67-727f0318c616'
Annotation_Mathematics_GUID = 'eaab634b-26d0-40c1-8073-57ca1c633c9b'
Annotation_Sensitive_GUID = '37f4c04f-0f12-4464-929c-828fd15292e3'
Changes_Summary_GUID = '313d65a6-e60f-4d62-9861-55afd728d207'
StyleId_Custom_GUID = 'ef2edd3e-a999-4b7c-a378-09bbd52a3516'
StyleId_Heading1_GUID = '7f7e8f69-6866-4621-930c-9a5d0ca5961c'
StyleId_Heading2_GUID = 'baa9b241-5c69-469d-85ad-474737b52b14'
StyleId_Heading3_GUID = 'bf8be9d2-d8b8-4ec5-8c52-9cfb0d035970'
StyleId_Heading4_GUID = '8436ffc0-9578-45fc-83a4-ff40053315dd'
StyleId_Heading5_GUID = '909f424d-0dbf-406e-97bb-4e773d9798f7'
StyleId_Heading6_GUID = '89d23459-5d5b-4824-a420-11d3ed82e40f'
StyleId_Heading7_GUID = 'a3790473-e9ae-422d-b8e3-3b675c6181a4'
StyleId_Heading8_GUID = '2bc14145-a40c-4881-84ae-f2235685380c'
StyleId_Heading9_GUID = 'c70d9133-bb2a-43d3-8ac6-33657884b0f0'
StyleId_Title_GUID = '15d8201a-ffcf-481f-b0a1-30b63be98f07'
StyleId_Subtitle_GUID = 'b5d9fc17-5d6f-4420-b439-7cb19ad434e2'
StyleId_Normal_GUID = 'cd14d429-e45e-4475-a1c5-7f9e6be96eba'
StyleId_Emphasis_GUID = 'ca6e7dbe-355e-4820-95a0-925f041d3470'
StyleId_Quote_GUID = '5d1c21ea-8195-4f6c-87ea-5dabece64c1d'
StyleId_BulletedList_GUID = '5963ed64-6426-4632-8caf-a32ad402d91a'
StyleId_NumberedList_GUID = '1e96dbd5-64c3-43d0-b1ee-b53b06e3eddf'
Notification_Event_GUID = '72c5a2f7-9788-480f-b8eb-4dee00f6186f'
SID_IsUIAutomationObject = 'b96fdb85-7204-4724-842b-c7059dedb9d0'
SID_ControlElementProvider = 'f4791d68-e254-4ba3-9a53-26a5c5497946'
IsSelectionPattern2Available_Property_GUID = '490806fb-6e89-4a47-8319-d266e511f021'
Selection2_FirstSelectedItem_Property_GUID = 'cc24ea67-369c-4e55-9ff7-38da69540c29'
Selection2_LastSelectedItem_Property_GUID = 'cf7bda90-2d83-49f8-860c-9ce394cf89b4'
Selection2_CurrentSelectedItem_Property_GUID = '34257c26-83b5-41a6-939c-ae841c136236'
Selection2_ItemCount_Property_GUID = 'bb49eb9f-456d-4048-b591-9c2026b84636'
Selection_Pattern2_GUID = 'fba25cab-ab98-49f7-a7dc-fe539dc15be7'
HeadingLevel_Property_GUID = '29084272-aaaf-4a30-8796-3c12f62b6bbb'
IsDialog_Property_GUID = '9d0dfb9b-8436-4501-bbbb-e534a4fb3b3f'
UIA_IAFP_DEFAULT = 0
UIA_IAFP_UNWRAP_BRIDGE = 1
UIA_PFIA_DEFAULT = 0
UIA_PFIA_UNWRAP_BRIDGE = 1
UIA_ScrollPatternNoScroll = -1
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
UIA_CustomLandmarkTypeId = 80000
UIA_FormLandmarkTypeId = 80001
UIA_MainLandmarkTypeId = 80002
UIA_NavigationLandmarkTypeId = 80003
UIA_SearchLandmarkTypeId = 80004
HeadingLevel_None = 80050
HeadingLevel1 = 80051
HeadingLevel2 = 80052
HeadingLevel3 = 80053
HeadingLevel4 = 80054
HeadingLevel5 = 80055
HeadingLevel6 = 80056
HeadingLevel7 = 80057
HeadingLevel8 = 80058
HeadingLevel9 = 80059
UIA_SummaryChangeId = 90000
UIA_SayAsInterpretAsMetadataId = 100000
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
SOUNDSENTRY_FLAGS = UInt32
SSF_SOUNDSENTRYON = 1
SSF_AVAILABLE = 2
SSF_INDICATOR = 4
ACC_UTILITY_STATE_FLAGS = UInt32
ANRUS_ON_SCREEN_KEYBOARD_ACTIVE = 1
ANRUS_TOUCH_MODIFICATION_ACTIVE = 2
ANRUS_PRIORITY_AUDIO_ACTIVE = 4
ANRUS_PRIORITY_AUDIO_ACTIVE_NODUCK = 8
SOUND_SENTRY_GRAPHICS_EFFECT = UInt32
SSGF_DISPLAY = 3
SSGF_NONE = 0
SERIALKEYS_FLAGS = UInt32
SERKF_AVAILABLE = 2
SERKF_INDICATOR = 4
SERKF_SERIALKEYSON = 1
HIGHCONTRASTW_FLAGS = UInt32
HCF_HIGHCONTRASTON = 1
HCF_AVAILABLE = 2
HCF_HOTKEYACTIVE = 4
HCF_CONFIRMHOTKEY = 8
HCF_HOTKEYSOUND = 16
HCF_INDICATOR = 32
HCF_HOTKEYAVAILABLE = 64
HCF_OPTION_NOTHEMECHANGE = 4096
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
HWINEVENTHOOK = IntPtr
HUIANODE = IntPtr
HUIAPATTERNOBJECT = IntPtr
HUIATEXTRANGE = IntPtr
HUIAEVENT = IntPtr
def _define_IRicheditWindowlessAccessibility_head():
    class IRicheditWindowlessAccessibility(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IRicheditWindowlessAccessibility
def _define_IRicheditWindowlessAccessibility():
    IRicheditWindowlessAccessibility = win32more.UI.Accessibility.IRicheditWindowlessAccessibility_head
    IRicheditWindowlessAccessibility.CreateProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderWindowlessSite_head,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(3, 'CreateProvider', ((1, 'pSite'),(1, 'ppProvider'),)))
    win32more.System.Com.IUnknown
    return IRicheditWindowlessAccessibility
def _define_IRichEditUiaInformation_head():
    class IRichEditUiaInformation(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IRichEditUiaInformation
def _define_IRichEditUiaInformation():
    IRichEditUiaInformation = win32more.UI.Accessibility.IRichEditUiaInformation_head
    IRichEditUiaInformation.GetBoundaryRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UiaRect_head), use_last_error=False)(3, 'GetBoundaryRectangle', ((1, 'pUiaRect'),)))
    IRichEditUiaInformation.IsVisible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'IsVisible', ()))
    win32more.System.Com.IUnknown
    return IRichEditUiaInformation
CAccPropServices = Guid('b5f8350b-0548-48b1-a6ee-88bd00b4a5e7')
def _define_LPFNLRESULTFROMOBJECT():
    return CFUNCTYPE(win32more.Foundation.LRESULT,POINTER(Guid),win32more.Foundation.WPARAM,win32more.System.Com.IUnknown_head, use_last_error=False)
def _define_LPFNOBJECTFROMLRESULT():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LRESULT,POINTER(Guid),win32more.Foundation.WPARAM,POINTER(c_void_p), use_last_error=False)
def _define_LPFNACCESSIBLEOBJECTFROMWINDOW():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)
def _define_LPFNACCESSIBLEOBJECTFROMPOINT():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,POINTER(win32more.UI.Accessibility.IAccessible_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)
def _define_LPFNCREATESTDACCESSIBLEOBJECT():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,Int32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)
def _define_LPFNACCESSIBLECHILDREN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessible_head,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32), use_last_error=False)
def _define_MSAAMENUINFO_head():
    class MSAAMENUINFO(Structure):
        pass
    return MSAAMENUINFO
def _define_MSAAMENUINFO():
    MSAAMENUINFO = win32more.UI.Accessibility.MSAAMENUINFO_head
    MSAAMENUINFO._fields_ = [
        ("dwMSAASignature", UInt32),
        ("cchWText", UInt32),
        ("pszWText", win32more.Foundation.PWSTR),
    ]
    return MSAAMENUINFO
def _define_IAccessible_head():
    class IAccessible(win32more.System.Com.IDispatch_head):
        Guid = Guid('618736e0-3c3d-11cf-810c-00aa00389b71')
    return IAccessible
def _define_IAccessible():
    IAccessible = win32more.UI.Accessibility.IAccessible_head
    IAccessible.get_accParent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(7, 'get_accParent', ((1, 'ppdispParent'),)))
    IAccessible.get_accChildCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_accChildCount', ((1, 'pcountChildren'),)))
    IAccessible.get_accChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(9, 'get_accChild', ((1, 'varChild'),(1, 'ppdispChild'),)))
    IAccessible.get_accName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_accName', ((1, 'varChild'),(1, 'pszName'),)))
    IAccessible.get_accValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_accValue', ((1, 'varChild'),(1, 'pszValue'),)))
    IAccessible.get_accDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_accDescription', ((1, 'varChild'),(1, 'pszDescription'),)))
    IAccessible.get_accRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'get_accRole', ((1, 'varChild'),(1, 'pvarRole'),)))
    IAccessible.get_accState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(14, 'get_accState', ((1, 'varChild'),(1, 'pvarState'),)))
    IAccessible.get_accHelp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_accHelp', ((1, 'varChild'),(1, 'pszHelp'),)))
    IAccessible.get_accHelpTopic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR),win32more.System.Com.VARIANT,POINTER(Int32), use_last_error=False)(16, 'get_accHelpTopic', ((1, 'pszHelpFile'),(1, 'varChild'),(1, 'pidTopic'),)))
    IAccessible.get_accKeyboardShortcut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_accKeyboardShortcut', ((1, 'varChild'),(1, 'pszKeyboardShortcut'),)))
    IAccessible.get_accFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(18, 'get_accFocus', ((1, 'pvarChild'),)))
    IAccessible.get_accSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(19, 'get_accSelection', ((1, 'pvarChildren'),)))
    IAccessible.get_accDefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_accDefaultAction', ((1, 'varChild'),(1, 'pszDefaultAction'),)))
    IAccessible.accSelect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT, use_last_error=False)(21, 'accSelect', ((1, 'flagsSelect'),(1, 'varChild'),)))
    IAccessible.accLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32),win32more.System.Com.VARIANT, use_last_error=False)(22, 'accLocation', ((1, 'pxLeft'),(1, 'pyTop'),(1, 'pcxWidth'),(1, 'pcyHeight'),(1, 'varChild'),)))
    IAccessible.accNavigate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(23, 'accNavigate', ((1, 'navDir'),(1, 'varStart'),(1, 'pvarEndUpAt'),)))
    IAccessible.accHitTest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(24, 'accHitTest', ((1, 'xLeft'),(1, 'yTop'),(1, 'pvarChild'),)))
    IAccessible.accDoDefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(25, 'accDoDefaultAction', ((1, 'varChild'),)))
    IAccessible.put_accName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,win32more.Foundation.BSTR, use_last_error=False)(26, 'put_accName', ((1, 'varChild'),(1, 'szName'),)))
    IAccessible.put_accValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,win32more.Foundation.BSTR, use_last_error=False)(27, 'put_accValue', ((1, 'varChild'),(1, 'szValue'),)))
    win32more.System.Com.IDispatch
    return IAccessible
def _define_IAccessibleHandler_head():
    class IAccessibleHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('03022430-abc4-11d0-bde2-00aa001a1953')
    return IAccessibleHandler
def _define_IAccessibleHandler():
    IAccessibleHandler = win32more.UI.Accessibility.IAccessibleHandler_head
    IAccessibleHandler.AccessibleObjectFromID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.Accessibility.IAccessible_head), use_last_error=False)(3, 'AccessibleObjectFromID', ((1, 'hwnd'),(1, 'lObjectID'),(1, 'pIAccessible'),)))
    win32more.System.Com.IUnknown
    return IAccessibleHandler
def _define_IAccessibleWindowlessSite_head():
    class IAccessibleWindowlessSite(win32more.System.Com.IUnknown_head):
        Guid = Guid('bf3abd9c-76da-4389-9eb6-1427d25abab7')
    return IAccessibleWindowlessSite
def _define_IAccessibleWindowlessSite():
    IAccessibleWindowlessSite = win32more.UI.Accessibility.IAccessibleWindowlessSite_head
    IAccessibleWindowlessSite.AcquireObjectIdRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.UI.Accessibility.IAccessibleHandler_head,POINTER(Int32), use_last_error=False)(3, 'AcquireObjectIdRange', ((1, 'rangeSize'),(1, 'pRangeOwner'),(1, 'pRangeBase'),)))
    IAccessibleWindowlessSite.ReleaseObjectIdRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.UI.Accessibility.IAccessibleHandler_head, use_last_error=False)(4, 'ReleaseObjectIdRange', ((1, 'rangeBase'),(1, 'pRangeOwner'),)))
    IAccessibleWindowlessSite.QueryObjectIdRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessibleHandler_head,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(5, 'QueryObjectIdRanges', ((1, 'pRangesOwner'),(1, 'psaRanges'),)))
    IAccessibleWindowlessSite.GetParentAccessible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IAccessible_head), use_last_error=False)(6, 'GetParentAccessible', ((1, 'ppParent'),)))
    win32more.System.Com.IUnknown
    return IAccessibleWindowlessSite
AnnoScope = Int32
ANNO_THIS = 0
ANNO_CONTAINER = 1
def _define_IAccIdentity_head():
    class IAccIdentity(win32more.System.Com.IUnknown_head):
        Guid = Guid('7852b78d-1cfd-41c1-a615-9c0c85960b5f')
    return IAccIdentity
def _define_IAccIdentity():
    IAccIdentity = win32more.UI.Accessibility.IAccIdentity_head
    IAccIdentity.GetIdentityString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(3, 'GetIdentityString', ((1, 'dwIDChild'),(1, 'ppIDString'),(1, 'pdwIDStringLen'),)))
    win32more.System.Com.IUnknown
    return IAccIdentity
def _define_IAccPropServer_head():
    class IAccPropServer(win32more.System.Com.IUnknown_head):
        Guid = Guid('76c0dbbb-15e0-4e7b-b61b-20eeea2001e0')
    return IAccPropServer
def _define_IAccPropServer():
    IAccPropServer = win32more.UI.Accessibility.IAccPropServer_head
    IAccPropServer.GetPropValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,Guid,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'GetPropValue', ((1, 'pIDString'),(1, 'dwIDStringLen'),(1, 'idProp'),(1, 'pvarValue'),(1, 'pfHasProp'),)))
    win32more.System.Com.IUnknown
    return IAccPropServer
def _define_IAccPropServices_head():
    class IAccPropServices(win32more.System.Com.IUnknown_head):
        Guid = Guid('6e26e776-04f0-495d-80e4-3330352e3169')
    return IAccPropServices
def _define_IAccPropServices():
    IAccPropServices = win32more.UI.Accessibility.IAccPropServices_head
    IAccPropServices.SetPropValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,Guid,win32more.System.Com.VARIANT, use_last_error=False)(3, 'SetPropValue', ((1, 'pIDString'),(1, 'dwIDStringLen'),(1, 'idProp'),(1, 'var'),)))
    IAccPropServices.SetPropServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(Guid),Int32,win32more.UI.Accessibility.IAccPropServer_head,win32more.UI.Accessibility.AnnoScope, use_last_error=False)(4, 'SetPropServer', ((1, 'pIDString'),(1, 'dwIDStringLen'),(1, 'paProps'),(1, 'cProps'),(1, 'pServer'),(1, 'annoScope'),)))
    IAccPropServices.ClearProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(Guid),Int32, use_last_error=False)(5, 'ClearProps', ((1, 'pIDString'),(1, 'dwIDStringLen'),(1, 'paProps'),(1, 'cProps'),)))
    IAccPropServices.SetHwndProp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,UInt32,Guid,win32more.System.Com.VARIANT, use_last_error=False)(6, 'SetHwndProp', ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'idProp'),(1, 'var'),)))
    IAccPropServices.SetHwndPropStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,UInt32,Guid,win32more.Foundation.PWSTR, use_last_error=False)(7, 'SetHwndPropStr', ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'idProp'),(1, 'str'),)))
    IAccPropServices.SetHwndPropServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,UInt32,POINTER(Guid),Int32,win32more.UI.Accessibility.IAccPropServer_head,win32more.UI.Accessibility.AnnoScope, use_last_error=False)(8, 'SetHwndPropServer', ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'paProps'),(1, 'cProps'),(1, 'pServer'),(1, 'annoScope'),)))
    IAccPropServices.ClearHwndProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,UInt32,POINTER(Guid),Int32, use_last_error=False)(9, 'ClearHwndProps', ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'paProps'),(1, 'cProps'),)))
    IAccPropServices.ComposeHwndIdentityString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,UInt32,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(10, 'ComposeHwndIdentityString', ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'ppIDString'),(1, 'pdwIDStringLen'),)))
    IAccPropServices.DecomposeHwndIdentityString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(win32more.Foundation.HWND),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(11, 'DecomposeHwndIdentityString', ((1, 'pIDString'),(1, 'dwIDStringLen'),(1, 'phwnd'),(1, 'pidObject'),(1, 'pidChild'),)))
    IAccPropServices.SetHmenuProp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HMENU,UInt32,Guid,win32more.System.Com.VARIANT, use_last_error=False)(12, 'SetHmenuProp', ((1, 'hmenu'),(1, 'idChild'),(1, 'idProp'),(1, 'var'),)))
    IAccPropServices.SetHmenuPropStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HMENU,UInt32,Guid,win32more.Foundation.PWSTR, use_last_error=False)(13, 'SetHmenuPropStr', ((1, 'hmenu'),(1, 'idChild'),(1, 'idProp'),(1, 'str'),)))
    IAccPropServices.SetHmenuPropServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HMENU,UInt32,POINTER(Guid),Int32,win32more.UI.Accessibility.IAccPropServer_head,win32more.UI.Accessibility.AnnoScope, use_last_error=False)(14, 'SetHmenuPropServer', ((1, 'hmenu'),(1, 'idChild'),(1, 'paProps'),(1, 'cProps'),(1, 'pServer'),(1, 'annoScope'),)))
    IAccPropServices.ClearHmenuProps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HMENU,UInt32,POINTER(Guid),Int32, use_last_error=False)(15, 'ClearHmenuProps', ((1, 'hmenu'),(1, 'idChild'),(1, 'paProps'),(1, 'cProps'),)))
    IAccPropServices.ComposeHmenuIdentityString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HMENU,UInt32,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(16, 'ComposeHmenuIdentityString', ((1, 'hmenu'),(1, 'idChild'),(1, 'ppIDString'),(1, 'pdwIDStringLen'),)))
    IAccPropServices.DecomposeHmenuIdentityString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(win32more.UI.WindowsAndMessaging.HMENU),POINTER(UInt32), use_last_error=False)(17, 'DecomposeHmenuIdentityString', ((1, 'pIDString'),(1, 'dwIDStringLen'),(1, 'phmenu'),(1, 'pidChild'),)))
    win32more.System.Com.IUnknown
    return IAccPropServices
CUIAutomation = Guid('ff48dba4-60ef-4201-aa87-54103eef594e')
CUIAutomation8 = Guid('e22ad333-b25f-460c-83d0-0581107395c9')
CUIAutomationRegistrar = Guid('6e29fabf-9977-42d1-8d0e-ca7e61ad87e6')
NavigateDirection = Int32
NavigateDirection_Parent = 0
NavigateDirection_NextSibling = 1
NavigateDirection_PreviousSibling = 2
NavigateDirection_FirstChild = 3
NavigateDirection_LastChild = 4
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
StructureChangeType = Int32
StructureChangeType_ChildAdded = 0
StructureChangeType_ChildRemoved = 1
StructureChangeType_ChildrenInvalidated = 2
StructureChangeType_ChildrenBulkAdded = 3
StructureChangeType_ChildrenBulkRemoved = 4
StructureChangeType_ChildrenReordered = 5
TextEditChangeType = Int32
TextEditChangeType_None = 0
TextEditChangeType_AutoCorrect = 1
TextEditChangeType_Composition = 2
TextEditChangeType_CompositionFinalized = 3
TextEditChangeType_AutoComplete = 4
OrientationType = Int32
OrientationType_None = 0
OrientationType_Horizontal = 1
OrientationType_Vertical = 2
DockPosition = Int32
DockPosition_Top = 0
DockPosition_Left = 1
DockPosition_Bottom = 2
DockPosition_Right = 3
DockPosition_Fill = 4
DockPosition_None = 5
ExpandCollapseState = Int32
ExpandCollapseState_Collapsed = 0
ExpandCollapseState_Expanded = 1
ExpandCollapseState_PartiallyExpanded = 2
ExpandCollapseState_LeafNode = 3
ScrollAmount = Int32
ScrollAmount_LargeDecrement = 0
ScrollAmount_SmallDecrement = 1
ScrollAmount_NoAmount = 2
ScrollAmount_LargeIncrement = 3
ScrollAmount_SmallIncrement = 4
RowOrColumnMajor = Int32
RowOrColumnMajor_RowMajor = 0
RowOrColumnMajor_ColumnMajor = 1
RowOrColumnMajor_Indeterminate = 2
ToggleState = Int32
ToggleState_Off = 0
ToggleState_On = 1
ToggleState_Indeterminate = 2
WindowVisualState = Int32
WindowVisualState_Normal = 0
WindowVisualState_Maximized = 1
WindowVisualState_Minimized = 2
SynchronizedInputType = Int32
SynchronizedInputType_KeyUp = 1
SynchronizedInputType_KeyDown = 2
SynchronizedInputType_LeftMouseUp = 4
SynchronizedInputType_LeftMouseDown = 8
SynchronizedInputType_RightMouseUp = 16
SynchronizedInputType_RightMouseDown = 32
WindowInteractionState = Int32
WindowInteractionState_Running = 0
WindowInteractionState_Closing = 1
WindowInteractionState_ReadyForUserInteraction = 2
WindowInteractionState_BlockedByModalWindow = 3
WindowInteractionState_NotResponding = 4
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
TextUnit = Int32
TextUnit_Character = 0
TextUnit_Format = 1
TextUnit_Word = 2
TextUnit_Line = 3
TextUnit_Paragraph = 4
TextUnit_Page = 5
TextUnit_Document = 6
TextPatternRangeEndpoint = Int32
TextPatternRangeEndpoint_Start = 0
TextPatternRangeEndpoint_End = 1
SupportedTextSelection = Int32
SupportedTextSelection_None = 0
SupportedTextSelection_Single = 1
SupportedTextSelection_Multiple = 2
LiveSetting = Int32
LiveSetting_Off = 0
LiveSetting_Polite = 1
LiveSetting_Assertive = 2
ActiveEnd = Int32
ActiveEnd_None = 0
ActiveEnd_Start = 1
ActiveEnd_End = 2
CaretPosition = Int32
CaretPosition_Unknown = 0
CaretPosition_EndOfLine = 1
CaretPosition_BeginningOfLine = 2
CaretBidiMode = Int32
CaretBidiMode_LTR = 0
CaretBidiMode_RTL = 1
ZoomUnit = Int32
ZoomUnit_NoAmount = 0
ZoomUnit_LargeDecrement = 1
ZoomUnit_SmallDecrement = 2
ZoomUnit_LargeIncrement = 3
ZoomUnit_SmallIncrement = 4
AnimationStyle = Int32
AnimationStyle_None = 0
AnimationStyle_LasVegasLights = 1
AnimationStyle_BlinkingBackground = 2
AnimationStyle_SparkleText = 3
AnimationStyle_MarchingBlackAnts = 4
AnimationStyle_MarchingRedAnts = 5
AnimationStyle_Shimmer = 6
AnimationStyle_Other = -1
BulletStyle = Int32
BulletStyle_None = 0
BulletStyle_HollowRoundBullet = 1
BulletStyle_FilledRoundBullet = 2
BulletStyle_HollowSquareBullet = 3
BulletStyle_FilledSquareBullet = 4
BulletStyle_DashBullet = 5
BulletStyle_Other = -1
CapStyle = Int32
CapStyle_None = 0
CapStyle_SmallCap = 1
CapStyle_AllCap = 2
CapStyle_AllPetiteCaps = 3
CapStyle_PetiteCaps = 4
CapStyle_Unicase = 5
CapStyle_Titling = 6
CapStyle_Other = -1
FillType = Int32
FillType_None = 0
FillType_Color = 1
FillType_Gradient = 2
FillType_Picture = 3
FillType_Pattern = 4
FlowDirections = Int32
FlowDirections_Default = 0
FlowDirections_RightToLeft = 1
FlowDirections_BottomToTop = 2
FlowDirections_Vertical = 4
HorizontalTextAlignment = Int32
HorizontalTextAlignment_Left = 0
HorizontalTextAlignment_Centered = 1
HorizontalTextAlignment_Right = 2
HorizontalTextAlignment_Justified = 3
OutlineStyles = Int32
OutlineStyles_None = 0
OutlineStyles_Outline = 1
OutlineStyles_Shadow = 2
OutlineStyles_Engraved = 4
OutlineStyles_Embossed = 8
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
VisualEffects = Int32
VisualEffects_None = 0
VisualEffects_Shadow = 1
VisualEffects_Reflection = 2
VisualEffects_Glow = 4
VisualEffects_SoftEdges = 8
VisualEffects_Bevel = 16
NotificationProcessing = Int32
NotificationProcessing_ImportantAll = 0
NotificationProcessing_ImportantMostRecent = 1
NotificationProcessing_All = 2
NotificationProcessing_MostRecent = 3
NotificationProcessing_CurrentThenMostRecent = 4
NotificationKind = Int32
NotificationKind_ItemAdded = 0
NotificationKind_ItemRemoved = 1
NotificationKind_ActionCompleted = 2
NotificationKind_ActionAborted = 3
NotificationKind_Other = 4
def _define_UiaRect_head():
    class UiaRect(Structure):
        pass
    return UiaRect
def _define_UiaRect():
    UiaRect = win32more.UI.Accessibility.UiaRect_head
    UiaRect._fields_ = [
        ("left", Double),
        ("top", Double),
        ("width", Double),
        ("height", Double),
    ]
    return UiaRect
def _define_UiaPoint_head():
    class UiaPoint(Structure):
        pass
    return UiaPoint
def _define_UiaPoint():
    UiaPoint = win32more.UI.Accessibility.UiaPoint_head
    UiaPoint._fields_ = [
        ("x", Double),
        ("y", Double),
    ]
    return UiaPoint
def _define_UiaChangeInfo_head():
    class UiaChangeInfo(Structure):
        pass
    return UiaChangeInfo
def _define_UiaChangeInfo():
    UiaChangeInfo = win32more.UI.Accessibility.UiaChangeInfo_head
    UiaChangeInfo._fields_ = [
        ("uiaId", Int32),
        ("payload", win32more.System.Com.VARIANT),
        ("extraInfo", win32more.System.Com.VARIANT),
    ]
    return UiaChangeInfo
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
def _define_UIAutomationParameter_head():
    class UIAutomationParameter(Structure):
        pass
    return UIAutomationParameter
def _define_UIAutomationParameter():
    UIAutomationParameter = win32more.UI.Accessibility.UIAutomationParameter_head
    UIAutomationParameter._fields_ = [
        ("type", win32more.UI.Accessibility.UIAutomationType),
        ("pData", c_void_p),
    ]
    return UIAutomationParameter
def _define_UIAutomationPropertyInfo_head():
    class UIAutomationPropertyInfo(Structure):
        pass
    return UIAutomationPropertyInfo
def _define_UIAutomationPropertyInfo():
    UIAutomationPropertyInfo = win32more.UI.Accessibility.UIAutomationPropertyInfo_head
    UIAutomationPropertyInfo._fields_ = [
        ("guid", Guid),
        ("pProgrammaticName", win32more.Foundation.PWSTR),
        ("type", win32more.UI.Accessibility.UIAutomationType),
    ]
    return UIAutomationPropertyInfo
def _define_UIAutomationEventInfo_head():
    class UIAutomationEventInfo(Structure):
        pass
    return UIAutomationEventInfo
def _define_UIAutomationEventInfo():
    UIAutomationEventInfo = win32more.UI.Accessibility.UIAutomationEventInfo_head
    UIAutomationEventInfo._fields_ = [
        ("guid", Guid),
        ("pProgrammaticName", win32more.Foundation.PWSTR),
    ]
    return UIAutomationEventInfo
def _define_UIAutomationMethodInfo_head():
    class UIAutomationMethodInfo(Structure):
        pass
    return UIAutomationMethodInfo
def _define_UIAutomationMethodInfo():
    UIAutomationMethodInfo = win32more.UI.Accessibility.UIAutomationMethodInfo_head
    UIAutomationMethodInfo._fields_ = [
        ("pProgrammaticName", win32more.Foundation.PWSTR),
        ("doSetFocus", win32more.Foundation.BOOL),
        ("cInParameters", UInt32),
        ("cOutParameters", UInt32),
        ("pParameterTypes", POINTER(win32more.UI.Accessibility.UIAutomationType)),
        ("pParameterNames", POINTER(win32more.Foundation.PWSTR)),
    ]
    return UIAutomationMethodInfo
def _define_UIAutomationPatternInfo_head():
    class UIAutomationPatternInfo(Structure):
        pass
    return UIAutomationPatternInfo
def _define_UIAutomationPatternInfo():
    UIAutomationPatternInfo = win32more.UI.Accessibility.UIAutomationPatternInfo_head
    UIAutomationPatternInfo._fields_ = [
        ("guid", Guid),
        ("pProgrammaticName", win32more.Foundation.PWSTR),
        ("providerInterfaceId", Guid),
        ("clientInterfaceId", Guid),
        ("cProperties", UInt32),
        ("pProperties", POINTER(win32more.UI.Accessibility.UIAutomationPropertyInfo_head)),
        ("cMethods", UInt32),
        ("pMethods", POINTER(win32more.UI.Accessibility.UIAutomationMethodInfo_head)),
        ("cEvents", UInt32),
        ("pEvents", POINTER(win32more.UI.Accessibility.UIAutomationEventInfo_head)),
        ("pPatternHandler", win32more.UI.Accessibility.IUIAutomationPatternHandler_head),
    ]
    return UIAutomationPatternInfo
def _define_IRawElementProviderSimple_head():
    class IRawElementProviderSimple(win32more.System.Com.IUnknown_head):
        Guid = Guid('d6dd68d1-86fd-4332-8666-9abedea2d24c')
    return IRawElementProviderSimple
def _define_IRawElementProviderSimple():
    IRawElementProviderSimple = win32more.UI.Accessibility.IRawElementProviderSimple_head
    IRawElementProviderSimple.get_ProviderOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ProviderOptions), use_last_error=False)(3, 'get_ProviderOptions', ((1, 'pRetVal'),)))
    IRawElementProviderSimple.GetPatternProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(4, 'GetPatternProvider', ((1, 'patternId'),(1, 'pRetVal'),)))
    IRawElementProviderSimple.GetPropertyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(5, 'GetPropertyValue', ((1, 'propertyId'),(1, 'pRetVal'),)))
    IRawElementProviderSimple.get_HostRawElementProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(6, 'get_HostRawElementProvider', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderSimple
def _define_IAccessibleEx_head():
    class IAccessibleEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('f8b80ada-2c44-48d0-89be-5ff23c9cd875')
    return IAccessibleEx
def _define_IAccessibleEx():
    IAccessibleEx = win32more.UI.Accessibility.IAccessibleEx_head
    IAccessibleEx.GetObjectForChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.Accessibility.IAccessibleEx_head), use_last_error=False)(3, 'GetObjectForChild', ((1, 'idChild'),(1, 'pRetVal'),)))
    IAccessibleEx.GetIAccessiblePair = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IAccessible_head),POINTER(Int32), use_last_error=False)(4, 'GetIAccessiblePair', ((1, 'ppAcc'),(1, 'pidChild'),)))
    IAccessibleEx.GetRuntimeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(5, 'GetRuntimeId', ((1, 'pRetVal'),)))
    IAccessibleEx.ConvertReturnedElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,POINTER(win32more.UI.Accessibility.IAccessibleEx_head), use_last_error=False)(6, 'ConvertReturnedElement', ((1, 'pIn'),(1, 'ppRetValOut'),)))
    win32more.System.Com.IUnknown
    return IAccessibleEx
def _define_IRawElementProviderSimple2_head():
    class IRawElementProviderSimple2(win32more.UI.Accessibility.IRawElementProviderSimple_head):
        Guid = Guid('a0a839a9-8da1-4a82-806a-8e0d44e79f56')
    return IRawElementProviderSimple2
def _define_IRawElementProviderSimple2():
    IRawElementProviderSimple2 = win32more.UI.Accessibility.IRawElementProviderSimple2_head
    IRawElementProviderSimple2.ShowContextMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'ShowContextMenu', ()))
    win32more.UI.Accessibility.IRawElementProviderSimple
    return IRawElementProviderSimple2
def _define_IRawElementProviderSimple3_head():
    class IRawElementProviderSimple3(win32more.UI.Accessibility.IRawElementProviderSimple2_head):
        Guid = Guid('fcf5d820-d7ec-4613-bdf6-42a84ce7daaf')
    return IRawElementProviderSimple3
def _define_IRawElementProviderSimple3():
    IRawElementProviderSimple3 = win32more.UI.Accessibility.IRawElementProviderSimple3_head
    IRawElementProviderSimple3.GetMetadataValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'GetMetadataValue', ((1, 'targetId'),(1, 'metadataId'),(1, 'returnVal'),)))
    win32more.UI.Accessibility.IRawElementProviderSimple2
    return IRawElementProviderSimple3
def _define_IRawElementProviderFragmentRoot_head():
    class IRawElementProviderFragmentRoot(win32more.System.Com.IUnknown_head):
        Guid = Guid('620ce2a5-ab8f-40a9-86cb-de3c75599b58')
    return IRawElementProviderFragmentRoot
def _define_IRawElementProviderFragmentRoot():
    IRawElementProviderFragmentRoot = win32more.UI.Accessibility.IRawElementProviderFragmentRoot_head
    IRawElementProviderFragmentRoot.ElementProviderFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,POINTER(win32more.UI.Accessibility.IRawElementProviderFragment_head), use_last_error=False)(3, 'ElementProviderFromPoint', ((1, 'x'),(1, 'y'),(1, 'pRetVal'),)))
    IRawElementProviderFragmentRoot.GetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderFragment_head), use_last_error=False)(4, 'GetFocus', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderFragmentRoot
def _define_IRawElementProviderFragment_head():
    class IRawElementProviderFragment(win32more.System.Com.IUnknown_head):
        Guid = Guid('f7063da8-8359-439c-9297-bbc5299a7d87')
    return IRawElementProviderFragment
def _define_IRawElementProviderFragment():
    IRawElementProviderFragment = win32more.UI.Accessibility.IRawElementProviderFragment_head
    IRawElementProviderFragment.Navigate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.NavigateDirection,POINTER(win32more.UI.Accessibility.IRawElementProviderFragment_head), use_last_error=False)(3, 'Navigate', ((1, 'direction'),(1, 'pRetVal'),)))
    IRawElementProviderFragment.GetRuntimeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(4, 'GetRuntimeId', ((1, 'pRetVal'),)))
    IRawElementProviderFragment.get_BoundingRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UiaRect_head), use_last_error=False)(5, 'get_BoundingRectangle', ((1, 'pRetVal'),)))
    IRawElementProviderFragment.GetEmbeddedFragmentRoots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(6, 'GetEmbeddedFragmentRoots', ((1, 'pRetVal'),)))
    IRawElementProviderFragment.SetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'SetFocus', ()))
    IRawElementProviderFragment.get_FragmentRoot = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderFragmentRoot_head), use_last_error=False)(8, 'get_FragmentRoot', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderFragment
def _define_IRawElementProviderAdviseEvents_head():
    class IRawElementProviderAdviseEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('a407b27b-0f6d-4427-9292-473c7bf93258')
    return IRawElementProviderAdviseEvents
def _define_IRawElementProviderAdviseEvents():
    IRawElementProviderAdviseEvents = win32more.UI.Accessibility.IRawElementProviderAdviseEvents_head
    IRawElementProviderAdviseEvents.AdviseEventAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(3, 'AdviseEventAdded', ((1, 'eventId'),(1, 'propertyIDs'),)))
    IRawElementProviderAdviseEvents.AdviseEventRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(4, 'AdviseEventRemoved', ((1, 'eventId'),(1, 'propertyIDs'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderAdviseEvents
def _define_IRawElementProviderHwndOverride_head():
    class IRawElementProviderHwndOverride(win32more.System.Com.IUnknown_head):
        Guid = Guid('1d5df27c-8947-4425-b8d9-79787bb460b8')
    return IRawElementProviderHwndOverride
def _define_IRawElementProviderHwndOverride():
    IRawElementProviderHwndOverride = win32more.UI.Accessibility.IRawElementProviderHwndOverride_head
    IRawElementProviderHwndOverride.GetOverrideProviderForHwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(3, 'GetOverrideProviderForHwnd', ((1, 'hwnd'),(1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderHwndOverride
def _define_IProxyProviderWinEventSink_head():
    class IProxyProviderWinEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('4fd82b78-a43e-46ac-9803-0a6969c7c183')
    return IProxyProviderWinEventSink
def _define_IProxyProviderWinEventSink():
    IProxyProviderWinEventSink = win32more.UI.Accessibility.IProxyProviderWinEventSink_head
    IProxyProviderWinEventSink.AddAutomationPropertyChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,Int32,win32more.System.Com.VARIANT, use_last_error=False)(3, 'AddAutomationPropertyChangedEvent', ((1, 'pProvider'),(1, 'id'),(1, 'newValue'),)))
    IProxyProviderWinEventSink.AddAutomationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,Int32, use_last_error=False)(4, 'AddAutomationEvent', ((1, 'pProvider'),(1, 'id'),)))
    IProxyProviderWinEventSink.AddStructureChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.StructureChangeType,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(5, 'AddStructureChangedEvent', ((1, 'pProvider'),(1, 'structureChangeType'),(1, 'runtimeId'),)))
    win32more.System.Com.IUnknown
    return IProxyProviderWinEventSink
def _define_IProxyProviderWinEventHandler_head():
    class IProxyProviderWinEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('89592ad4-f4e0-43d5-a3b6-bad7e111b435')
    return IProxyProviderWinEventHandler
def _define_IProxyProviderWinEventHandler():
    IProxyProviderWinEventHandler = win32more.UI.Accessibility.IProxyProviderWinEventHandler_head
    IProxyProviderWinEventHandler.RespondToWinEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.HWND,Int32,Int32,win32more.UI.Accessibility.IProxyProviderWinEventSink_head, use_last_error=False)(3, 'RespondToWinEvent', ((1, 'idWinEvent'),(1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'pSink'),)))
    win32more.System.Com.IUnknown
    return IProxyProviderWinEventHandler
def _define_IRawElementProviderWindowlessSite_head():
    class IRawElementProviderWindowlessSite(win32more.System.Com.IUnknown_head):
        Guid = Guid('0a2a93cc-bfad-42ac-9b2e-0991fb0d3ea0')
    return IRawElementProviderWindowlessSite
def _define_IRawElementProviderWindowlessSite():
    IRawElementProviderWindowlessSite = win32more.UI.Accessibility.IRawElementProviderWindowlessSite_head
    IRawElementProviderWindowlessSite.GetAdjacentFragment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.NavigateDirection,POINTER(win32more.UI.Accessibility.IRawElementProviderFragment_head), use_last_error=False)(3, 'GetAdjacentFragment', ((1, 'direction'),(1, 'ppParent'),)))
    IRawElementProviderWindowlessSite.GetRuntimeIdPrefix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(4, 'GetRuntimeIdPrefix', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderWindowlessSite
def _define_IAccessibleHostingElementProviders_head():
    class IAccessibleHostingElementProviders(win32more.System.Com.IUnknown_head):
        Guid = Guid('33ac331b-943e-4020-b295-db37784974a3')
    return IAccessibleHostingElementProviders
def _define_IAccessibleHostingElementProviders():
    IAccessibleHostingElementProviders = win32more.UI.Accessibility.IAccessibleHostingElementProviders_head
    IAccessibleHostingElementProviders.GetEmbeddedFragmentRoots = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(3, 'GetEmbeddedFragmentRoots', ((1, 'pRetVal'),)))
    IAccessibleHostingElementProviders.GetObjectIdForProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,POINTER(Int32), use_last_error=False)(4, 'GetObjectIdForProvider', ((1, 'pProvider'),(1, 'pidObject'),)))
    win32more.System.Com.IUnknown
    return IAccessibleHostingElementProviders
def _define_IRawElementProviderHostingAccessibles_head():
    class IRawElementProviderHostingAccessibles(win32more.System.Com.IUnknown_head):
        Guid = Guid('24be0b07-d37d-487a-98cf-a13ed465e9b3')
    return IRawElementProviderHostingAccessibles
def _define_IRawElementProviderHostingAccessibles():
    IRawElementProviderHostingAccessibles = win32more.UI.Accessibility.IRawElementProviderHostingAccessibles_head
    IRawElementProviderHostingAccessibles.GetEmbeddedAccessibles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(3, 'GetEmbeddedAccessibles', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRawElementProviderHostingAccessibles
def _define_IDockProvider_head():
    class IDockProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('159bc72c-4ad3-485e-9637-d7052edf0146')
    return IDockProvider
def _define_IDockProvider():
    IDockProvider = win32more.UI.Accessibility.IDockProvider_head
    IDockProvider.SetDockPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.DockPosition, use_last_error=False)(3, 'SetDockPosition', ((1, 'dockPosition'),)))
    IDockProvider.get_DockPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.DockPosition), use_last_error=False)(4, 'get_DockPosition', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IDockProvider
def _define_IExpandCollapseProvider_head():
    class IExpandCollapseProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('d847d3a5-cab0-4a98-8c32-ecb45c59ad24')
    return IExpandCollapseProvider
def _define_IExpandCollapseProvider():
    IExpandCollapseProvider = win32more.UI.Accessibility.IExpandCollapseProvider_head
    IExpandCollapseProvider.Expand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Expand', ()))
    IExpandCollapseProvider.Collapse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Collapse', ()))
    IExpandCollapseProvider.get_ExpandCollapseState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ExpandCollapseState), use_last_error=False)(5, 'get_ExpandCollapseState', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IExpandCollapseProvider
def _define_IGridProvider_head():
    class IGridProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('b17d6187-0907-464b-a168-0ef17a1572b1')
    return IGridProvider
def _define_IGridProvider():
    IGridProvider = win32more.UI.Accessibility.IGridProvider_head
    IGridProvider.GetItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(3, 'GetItem', ((1, 'row'),(1, 'column'),(1, 'pRetVal'),)))
    IGridProvider.get_RowCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(4, 'get_RowCount', ((1, 'pRetVal'),)))
    IGridProvider.get_ColumnCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(5, 'get_ColumnCount', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IGridProvider
def _define_IGridItemProvider_head():
    class IGridItemProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('d02541f1-fb81-4d64-ae32-f520f8a6dbd1')
    return IGridItemProvider
def _define_IGridItemProvider():
    IGridItemProvider = win32more.UI.Accessibility.IGridItemProvider_head
    IGridItemProvider.get_Row = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'get_Row', ((1, 'pRetVal'),)))
    IGridItemProvider.get_Column = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(4, 'get_Column', ((1, 'pRetVal'),)))
    IGridItemProvider.get_RowSpan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(5, 'get_RowSpan', ((1, 'pRetVal'),)))
    IGridItemProvider.get_ColumnSpan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(6, 'get_ColumnSpan', ((1, 'pRetVal'),)))
    IGridItemProvider.get_ContainingGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(7, 'get_ContainingGrid', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IGridItemProvider
def _define_IInvokeProvider_head():
    class IInvokeProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('54fcb24b-e18e-47a2-b4d3-eccbe77599a2')
    return IInvokeProvider
def _define_IInvokeProvider():
    IInvokeProvider = win32more.UI.Accessibility.IInvokeProvider_head
    IInvokeProvider.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Invoke', ()))
    win32more.System.Com.IUnknown
    return IInvokeProvider
def _define_IMultipleViewProvider_head():
    class IMultipleViewProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('6278cab1-b556-4a1a-b4e0-418acc523201')
    return IMultipleViewProvider
def _define_IMultipleViewProvider():
    IMultipleViewProvider = win32more.UI.Accessibility.IMultipleViewProvider_head
    IMultipleViewProvider.GetViewName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetViewName', ((1, 'viewId'),(1, 'pRetVal'),)))
    IMultipleViewProvider.SetCurrentView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(4, 'SetCurrentView', ((1, 'viewId'),)))
    IMultipleViewProvider.get_CurrentView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(5, 'get_CurrentView', ((1, 'pRetVal'),)))
    IMultipleViewProvider.GetSupportedViews = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(6, 'GetSupportedViews', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IMultipleViewProvider
def _define_IRangeValueProvider_head():
    class IRangeValueProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('36dc7aef-33e6-4691-afe1-2be7274b3d33')
    return IRangeValueProvider
def _define_IRangeValueProvider():
    IRangeValueProvider = win32more.UI.Accessibility.IRangeValueProvider_head
    IRangeValueProvider.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(3, 'SetValue', ((1, 'val'),)))
    IRangeValueProvider.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(4, 'get_Value', ((1, 'pRetVal'),)))
    IRangeValueProvider.get_IsReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'get_IsReadOnly', ((1, 'pRetVal'),)))
    IRangeValueProvider.get_Maximum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(6, 'get_Maximum', ((1, 'pRetVal'),)))
    IRangeValueProvider.get_Minimum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(7, 'get_Minimum', ((1, 'pRetVal'),)))
    IRangeValueProvider.get_LargeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(8, 'get_LargeChange', ((1, 'pRetVal'),)))
    IRangeValueProvider.get_SmallChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(9, 'get_SmallChange', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IRangeValueProvider
def _define_IScrollItemProvider_head():
    class IScrollItemProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('2360c714-4bf1-4b26-ba65-9b21316127eb')
    return IScrollItemProvider
def _define_IScrollItemProvider():
    IScrollItemProvider = win32more.UI.Accessibility.IScrollItemProvider_head
    IScrollItemProvider.ScrollIntoView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'ScrollIntoView', ()))
    win32more.System.Com.IUnknown
    return IScrollItemProvider
def _define_ISelectionProvider_head():
    class ISelectionProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('fb8b03af-3bdf-48d4-bd36-1a65793be168')
    return ISelectionProvider
def _define_ISelectionProvider():
    ISelectionProvider = win32more.UI.Accessibility.ISelectionProvider_head
    ISelectionProvider.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(3, 'GetSelection', ((1, 'pRetVal'),)))
    ISelectionProvider.get_CanSelectMultiple = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'get_CanSelectMultiple', ((1, 'pRetVal'),)))
    ISelectionProvider.get_IsSelectionRequired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'get_IsSelectionRequired', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ISelectionProvider
def _define_ISelectionProvider2_head():
    class ISelectionProvider2(win32more.UI.Accessibility.ISelectionProvider_head):
        Guid = Guid('14f68475-ee1c-44f6-a869-d239381f0fe7')
    return ISelectionProvider2
def _define_ISelectionProvider2():
    ISelectionProvider2 = win32more.UI.Accessibility.ISelectionProvider2_head
    ISelectionProvider2.get_FirstSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(6, 'get_FirstSelectedItem', ((1, 'retVal'),)))
    ISelectionProvider2.get_LastSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(7, 'get_LastSelectedItem', ((1, 'retVal'),)))
    ISelectionProvider2.get_CurrentSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(8, 'get_CurrentSelectedItem', ((1, 'retVal'),)))
    ISelectionProvider2.get_ItemCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_ItemCount', ((1, 'retVal'),)))
    win32more.UI.Accessibility.ISelectionProvider
    return ISelectionProvider2
def _define_IScrollProvider_head():
    class IScrollProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('b38b8077-1fc3-42a5-8cae-d40c2215055a')
    return IScrollProvider
def _define_IScrollProvider():
    IScrollProvider = win32more.UI.Accessibility.IScrollProvider_head
    IScrollProvider.Scroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.ScrollAmount,win32more.UI.Accessibility.ScrollAmount, use_last_error=False)(3, 'Scroll', ((1, 'horizontalAmount'),(1, 'verticalAmount'),)))
    IScrollProvider.SetScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double, use_last_error=False)(4, 'SetScrollPercent', ((1, 'horizontalPercent'),(1, 'verticalPercent'),)))
    IScrollProvider.get_HorizontalScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(5, 'get_HorizontalScrollPercent', ((1, 'pRetVal'),)))
    IScrollProvider.get_VerticalScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(6, 'get_VerticalScrollPercent', ((1, 'pRetVal'),)))
    IScrollProvider.get_HorizontalViewSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(7, 'get_HorizontalViewSize', ((1, 'pRetVal'),)))
    IScrollProvider.get_VerticalViewSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(8, 'get_VerticalViewSize', ((1, 'pRetVal'),)))
    IScrollProvider.get_HorizontallyScrollable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'get_HorizontallyScrollable', ((1, 'pRetVal'),)))
    IScrollProvider.get_VerticallyScrollable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(10, 'get_VerticallyScrollable', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IScrollProvider
def _define_ISelectionItemProvider_head():
    class ISelectionItemProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('2acad808-b2d4-452d-a407-91ff1ad167b2')
    return ISelectionItemProvider
def _define_ISelectionItemProvider():
    ISelectionItemProvider = win32more.UI.Accessibility.ISelectionItemProvider_head
    ISelectionItemProvider.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Select', ()))
    ISelectionItemProvider.AddToSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'AddToSelection', ()))
    ISelectionItemProvider.RemoveFromSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'RemoveFromSelection', ()))
    ISelectionItemProvider.get_IsSelected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'get_IsSelected', ((1, 'pRetVal'),)))
    ISelectionItemProvider.get_SelectionContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(7, 'get_SelectionContainer', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ISelectionItemProvider
def _define_ISynchronizedInputProvider_head():
    class ISynchronizedInputProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('29db1a06-02ce-4cf7-9b42-565d4fab20ee')
    return ISynchronizedInputProvider
def _define_ISynchronizedInputProvider():
    ISynchronizedInputProvider = win32more.UI.Accessibility.ISynchronizedInputProvider_head
    ISynchronizedInputProvider.StartListening = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.SynchronizedInputType, use_last_error=False)(3, 'StartListening', ((1, 'inputType'),)))
    ISynchronizedInputProvider.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Cancel', ()))
    win32more.System.Com.IUnknown
    return ISynchronizedInputProvider
def _define_ITableProvider_head():
    class ITableProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('9c860395-97b3-490a-b52a-858cc22af166')
    return ITableProvider
def _define_ITableProvider():
    ITableProvider = win32more.UI.Accessibility.ITableProvider_head
    ITableProvider.GetRowHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(3, 'GetRowHeaders', ((1, 'pRetVal'),)))
    ITableProvider.GetColumnHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(4, 'GetColumnHeaders', ((1, 'pRetVal'),)))
    ITableProvider.get_RowOrColumnMajor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.RowOrColumnMajor), use_last_error=False)(5, 'get_RowOrColumnMajor', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ITableProvider
def _define_ITableItemProvider_head():
    class ITableItemProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('b9734fa6-771f-4d78-9c90-2517999349cd')
    return ITableItemProvider
def _define_ITableItemProvider():
    ITableItemProvider = win32more.UI.Accessibility.ITableItemProvider_head
    ITableItemProvider.GetRowHeaderItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(3, 'GetRowHeaderItems', ((1, 'pRetVal'),)))
    ITableItemProvider.GetColumnHeaderItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(4, 'GetColumnHeaderItems', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ITableItemProvider
def _define_IToggleProvider_head():
    class IToggleProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('56d00bd0-c4f4-433c-a836-1a52a57e0892')
    return IToggleProvider
def _define_IToggleProvider():
    IToggleProvider = win32more.UI.Accessibility.IToggleProvider_head
    IToggleProvider.Toggle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Toggle', ()))
    IToggleProvider.get_ToggleState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ToggleState), use_last_error=False)(4, 'get_ToggleState', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IToggleProvider
def _define_ITransformProvider_head():
    class ITransformProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('6829ddc4-4f91-4ffa-b86f-bd3e2987cb4c')
    return ITransformProvider
def _define_ITransformProvider():
    ITransformProvider = win32more.UI.Accessibility.ITransformProvider_head
    ITransformProvider.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double, use_last_error=False)(3, 'Move', ((1, 'x'),(1, 'y'),)))
    ITransformProvider.Resize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double, use_last_error=False)(4, 'Resize', ((1, 'width'),(1, 'height'),)))
    ITransformProvider.Rotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(5, 'Rotate', ((1, 'degrees'),)))
    ITransformProvider.get_CanMove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'get_CanMove', ((1, 'pRetVal'),)))
    ITransformProvider.get_CanResize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'get_CanResize', ((1, 'pRetVal'),)))
    ITransformProvider.get_CanRotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'get_CanRotate', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ITransformProvider
def _define_IValueProvider_head():
    class IValueProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('c7935180-6fb3-4201-b174-7df73adbf64a')
    return IValueProvider
def _define_IValueProvider():
    IValueProvider = win32more.UI.Accessibility.IValueProvider_head
    IValueProvider.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'SetValue', ((1, 'val'),)))
    IValueProvider.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_Value', ((1, 'pRetVal'),)))
    IValueProvider.get_IsReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'get_IsReadOnly', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IValueProvider
def _define_IWindowProvider_head():
    class IWindowProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('987df77b-db06-4d77-8f8a-86a9c3bb90b9')
    return IWindowProvider
def _define_IWindowProvider():
    IWindowProvider = win32more.UI.Accessibility.IWindowProvider_head
    IWindowProvider.SetVisualState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.WindowVisualState, use_last_error=False)(3, 'SetVisualState', ((1, 'state'),)))
    IWindowProvider.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    IWindowProvider.WaitForInputIdle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'WaitForInputIdle', ((1, 'milliseconds'),(1, 'pRetVal'),)))
    IWindowProvider.get_CanMaximize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'get_CanMaximize', ((1, 'pRetVal'),)))
    IWindowProvider.get_CanMinimize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'get_CanMinimize', ((1, 'pRetVal'),)))
    IWindowProvider.get_IsModal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'get_IsModal', ((1, 'pRetVal'),)))
    IWindowProvider.get_WindowVisualState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.WindowVisualState), use_last_error=False)(9, 'get_WindowVisualState', ((1, 'pRetVal'),)))
    IWindowProvider.get_WindowInteractionState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.WindowInteractionState), use_last_error=False)(10, 'get_WindowInteractionState', ((1, 'pRetVal'),)))
    IWindowProvider.get_IsTopmost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'get_IsTopmost', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IWindowProvider
def _define_ILegacyIAccessibleProvider_head():
    class ILegacyIAccessibleProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('e44c3566-915d-4070-99c6-047bff5a08f5')
    return ILegacyIAccessibleProvider
def _define_ILegacyIAccessibleProvider():
    ILegacyIAccessibleProvider = win32more.UI.Accessibility.ILegacyIAccessibleProvider_head
    ILegacyIAccessibleProvider.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'Select', ((1, 'flagsSelect'),)))
    ILegacyIAccessibleProvider.DoDefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'DoDefaultAction', ()))
    ILegacyIAccessibleProvider.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SetValue', ((1, 'szValue'),)))
    ILegacyIAccessibleProvider.GetIAccessible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IAccessible_head), use_last_error=False)(6, 'GetIAccessible', ((1, 'ppAccessible'),)))
    ILegacyIAccessibleProvider.get_ChildId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_ChildId', ((1, 'pRetVal'),)))
    ILegacyIAccessibleProvider.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Name', ((1, 'pszName'),)))
    ILegacyIAccessibleProvider.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Value', ((1, 'pszValue'),)))
    ILegacyIAccessibleProvider.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Description', ((1, 'pszDescription'),)))
    ILegacyIAccessibleProvider.get_Role = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'get_Role', ((1, 'pdwRole'),)))
    ILegacyIAccessibleProvider.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'get_State', ((1, 'pdwState'),)))
    ILegacyIAccessibleProvider.get_Help = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_Help', ((1, 'pszHelp'),)))
    ILegacyIAccessibleProvider.get_KeyboardShortcut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_KeyboardShortcut', ((1, 'pszKeyboardShortcut'),)))
    ILegacyIAccessibleProvider.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(15, 'GetSelection', ((1, 'pvarSelectedChildren'),)))
    ILegacyIAccessibleProvider.get_DefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'get_DefaultAction', ((1, 'pszDefaultAction'),)))
    win32more.System.Com.IUnknown
    return ILegacyIAccessibleProvider
def _define_IItemContainerProvider_head():
    class IItemContainerProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('e747770b-39ce-4382-ab30-d8fb3f336f24')
    return IItemContainerProvider
def _define_IItemContainerProvider():
    IItemContainerProvider = win32more.UI.Accessibility.IItemContainerProvider_head
    IItemContainerProvider.FindItemByProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,Int32,win32more.System.Com.VARIANT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(3, 'FindItemByProperty', ((1, 'pStartAfter'),(1, 'propertyId'),(1, 'value'),(1, 'pFound'),)))
    win32more.System.Com.IUnknown
    return IItemContainerProvider
def _define_IVirtualizedItemProvider_head():
    class IVirtualizedItemProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('cb98b665-2d35-4fac-ad35-f3c60d0c0b8b')
    return IVirtualizedItemProvider
def _define_IVirtualizedItemProvider():
    IVirtualizedItemProvider = win32more.UI.Accessibility.IVirtualizedItemProvider_head
    IVirtualizedItemProvider.Realize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Realize', ()))
    win32more.System.Com.IUnknown
    return IVirtualizedItemProvider
def _define_IObjectModelProvider_head():
    class IObjectModelProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('3ad86ebd-f5ef-483d-bb18-b1042a475d64')
    return IObjectModelProvider
def _define_IObjectModelProvider():
    IObjectModelProvider = win32more.UI.Accessibility.IObjectModelProvider_head
    IObjectModelProvider.GetUnderlyingObjectModel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(3, 'GetUnderlyingObjectModel', ((1, 'ppUnknown'),)))
    win32more.System.Com.IUnknown
    return IObjectModelProvider
def _define_IAnnotationProvider_head():
    class IAnnotationProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('f95c7e80-bd63-4601-9782-445ebff011fc')
    return IAnnotationProvider
def _define_IAnnotationProvider():
    IAnnotationProvider = win32more.UI.Accessibility.IAnnotationProvider_head
    IAnnotationProvider.get_AnnotationTypeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'get_AnnotationTypeId', ((1, 'retVal'),)))
    IAnnotationProvider.get_AnnotationTypeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_AnnotationTypeName', ((1, 'retVal'),)))
    IAnnotationProvider.get_Author = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'get_Author', ((1, 'retVal'),)))
    IAnnotationProvider.get_DateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'get_DateTime', ((1, 'retVal'),)))
    IAnnotationProvider.get_Target = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(7, 'get_Target', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IAnnotationProvider
def _define_IStylesProvider_head():
    class IStylesProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('19b6b649-f5d7-4a6d-bdcb-129252be588a')
    return IStylesProvider
def _define_IStylesProvider():
    IStylesProvider = win32more.UI.Accessibility.IStylesProvider_head
    IStylesProvider.get_StyleId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'get_StyleId', ((1, 'retVal'),)))
    IStylesProvider.get_StyleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_StyleName', ((1, 'retVal'),)))
    IStylesProvider.get_FillColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(5, 'get_FillColor', ((1, 'retVal'),)))
    IStylesProvider.get_FillPatternStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'get_FillPatternStyle', ((1, 'retVal'),)))
    IStylesProvider.get_Shape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Shape', ((1, 'retVal'),)))
    IStylesProvider.get_FillPatternColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_FillPatternColor', ((1, 'retVal'),)))
    IStylesProvider.get_ExtendedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_ExtendedProperties', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IStylesProvider
def _define_ISpreadsheetProvider_head():
    class ISpreadsheetProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('6f6b5d35-5525-4f80-b758-85473832ffc7')
    return ISpreadsheetProvider
def _define_ISpreadsheetProvider():
    ISpreadsheetProvider = win32more.UI.Accessibility.ISpreadsheetProvider_head
    ISpreadsheetProvider.GetItemByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(3, 'GetItemByName', ((1, 'name'),(1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ISpreadsheetProvider
def _define_ISpreadsheetItemProvider_head():
    class ISpreadsheetItemProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('eaed4660-7b3d-4879-a2e6-365ce603f3d0')
    return ISpreadsheetItemProvider
def _define_ISpreadsheetItemProvider():
    ISpreadsheetItemProvider = win32more.UI.Accessibility.ISpreadsheetItemProvider_head
    ISpreadsheetItemProvider.get_Formula = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_Formula', ((1, 'pRetVal'),)))
    ISpreadsheetItemProvider.GetAnnotationObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(4, 'GetAnnotationObjects', ((1, 'pRetVal'),)))
    ISpreadsheetItemProvider.GetAnnotationTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(5, 'GetAnnotationTypes', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ISpreadsheetItemProvider
def _define_ITransformProvider2_head():
    class ITransformProvider2(win32more.UI.Accessibility.ITransformProvider_head):
        Guid = Guid('4758742f-7ac2-460c-bc48-09fc09308a93')
    return ITransformProvider2
def _define_ITransformProvider2():
    ITransformProvider2 = win32more.UI.Accessibility.ITransformProvider2_head
    ITransformProvider2.Zoom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(9, 'Zoom', ((1, 'zoom'),)))
    ITransformProvider2.get_CanZoom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(10, 'get_CanZoom', ((1, 'pRetVal'),)))
    ITransformProvider2.get_ZoomLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(11, 'get_ZoomLevel', ((1, 'pRetVal'),)))
    ITransformProvider2.get_ZoomMinimum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(12, 'get_ZoomMinimum', ((1, 'pRetVal'),)))
    ITransformProvider2.get_ZoomMaximum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(13, 'get_ZoomMaximum', ((1, 'pRetVal'),)))
    ITransformProvider2.ZoomByUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.ZoomUnit, use_last_error=False)(14, 'ZoomByUnit', ((1, 'zoomUnit'),)))
    win32more.UI.Accessibility.ITransformProvider
    return ITransformProvider2
def _define_IDragProvider_head():
    class IDragProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('6aa7bbbb-7ff9-497d-904f-d20b897929d8')
    return IDragProvider
def _define_IDragProvider():
    IDragProvider = win32more.UI.Accessibility.IDragProvider_head
    IDragProvider.get_IsGrabbed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'get_IsGrabbed', ((1, 'pRetVal'),)))
    IDragProvider.get_DropEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_DropEffect', ((1, 'pRetVal'),)))
    IDragProvider.get_DropEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(5, 'get_DropEffects', ((1, 'pRetVal'),)))
    IDragProvider.GetGrabbedItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(6, 'GetGrabbedItems', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IDragProvider
def _define_IDropTargetProvider_head():
    class IDropTargetProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('bae82bfd-358a-481c-85a0-d8b4d90a5d61')
    return IDropTargetProvider
def _define_IDropTargetProvider():
    IDropTargetProvider = win32more.UI.Accessibility.IDropTargetProvider_head
    IDropTargetProvider.get_DropTargetEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_DropTargetEffect', ((1, 'pRetVal'),)))
    IDropTargetProvider.get_DropTargetEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(4, 'get_DropTargetEffects', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IDropTargetProvider
def _define_ITextRangeProvider_head():
    class ITextRangeProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('5347ad7b-c355-46f8-aff5-909033582f63')
    return ITextRangeProvider
def _define_ITextRangeProvider():
    ITextRangeProvider = win32more.UI.Accessibility.ITextRangeProvider_head
    ITextRangeProvider.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head), use_last_error=False)(3, 'Clone', ((1, 'pRetVal'),)))
    ITextRangeProvider.Compare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.ITextRangeProvider_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'Compare', ((1, 'range'),(1, 'pRetVal'),)))
    ITextRangeProvider.CompareEndpoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.ITextRangeProvider_head,win32more.UI.Accessibility.TextPatternRangeEndpoint,POINTER(Int32), use_last_error=False)(5, 'CompareEndpoints', ((1, 'endpoint'),(1, 'targetRange'),(1, 'targetEndpoint'),(1, 'pRetVal'),)))
    ITextRangeProvider.ExpandToEnclosingUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextUnit, use_last_error=False)(6, 'ExpandToEnclosingUnit', ((1, 'unit'),)))
    ITextRangeProvider.FindAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.Foundation.BOOL,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head), use_last_error=False)(7, 'FindAttribute', ((1, 'attributeId'),(1, 'val'),(1, 'backward'),(1, 'pRetVal'),)))
    ITextRangeProvider.FindText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head), use_last_error=False)(8, 'FindText', ((1, 'text'),(1, 'backward'),(1, 'ignoreCase'),(1, 'pRetVal'),)))
    ITextRangeProvider.GetAttributeValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'GetAttributeValue', ((1, 'attributeId'),(1, 'pRetVal'),)))
    ITextRangeProvider.GetBoundingRectangles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(10, 'GetBoundingRectangles', ((1, 'pRetVal'),)))
    ITextRangeProvider.GetEnclosingElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(11, 'GetEnclosingElement', ((1, 'pRetVal'),)))
    ITextRangeProvider.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'GetText', ((1, 'maxLength'),(1, 'pRetVal'),)))
    ITextRangeProvider.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextUnit,Int32,POINTER(Int32), use_last_error=False)(13, 'Move', ((1, 'unit'),(1, 'count'),(1, 'pRetVal'),)))
    ITextRangeProvider.MoveEndpointByUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.TextUnit,Int32,POINTER(Int32), use_last_error=False)(14, 'MoveEndpointByUnit', ((1, 'endpoint'),(1, 'unit'),(1, 'count'),(1, 'pRetVal'),)))
    ITextRangeProvider.MoveEndpointByRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.ITextRangeProvider_head,win32more.UI.Accessibility.TextPatternRangeEndpoint, use_last_error=False)(15, 'MoveEndpointByRange', ((1, 'endpoint'),(1, 'targetRange'),(1, 'targetEndpoint'),)))
    ITextRangeProvider.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Select', ()))
    ITextRangeProvider.AddToSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'AddToSelection', ()))
    ITextRangeProvider.RemoveFromSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'RemoveFromSelection', ()))
    ITextRangeProvider.ScrollIntoView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(19, 'ScrollIntoView', ((1, 'alignToTop'),)))
    ITextRangeProvider.GetChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(20, 'GetChildren', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ITextRangeProvider
def _define_ITextProvider_head():
    class ITextProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('3589c92c-63f3-4367-99bb-ada653b77cf2')
    return ITextProvider
def _define_ITextProvider():
    ITextProvider = win32more.UI.Accessibility.ITextProvider_head
    ITextProvider.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(3, 'GetSelection', ((1, 'pRetVal'),)))
    ITextProvider.GetVisibleRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(4, 'GetVisibleRanges', ((1, 'pRetVal'),)))
    ITextProvider.RangeFromChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head), use_last_error=False)(5, 'RangeFromChild', ((1, 'childElement'),(1, 'pRetVal'),)))
    ITextProvider.RangeFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.UiaPoint,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head), use_last_error=False)(6, 'RangeFromPoint', ((1, 'point'),(1, 'pRetVal'),)))
    ITextProvider.get_DocumentRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head), use_last_error=False)(7, 'get_DocumentRange', ((1, 'pRetVal'),)))
    ITextProvider.get_SupportedTextSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.SupportedTextSelection), use_last_error=False)(8, 'get_SupportedTextSelection', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ITextProvider
def _define_ITextProvider2_head():
    class ITextProvider2(win32more.UI.Accessibility.ITextProvider_head):
        Guid = Guid('0dc5e6ed-3e16-4bf1-8f9a-a979878bc195')
    return ITextProvider2
def _define_ITextProvider2():
    ITextProvider2 = win32more.UI.Accessibility.ITextProvider2_head
    ITextProvider2.RangeFromAnnotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head), use_last_error=False)(9, 'RangeFromAnnotation', ((1, 'annotationElement'),(1, 'pRetVal'),)))
    ITextProvider2.GetCaretRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.UI.Accessibility.ITextRangeProvider_head), use_last_error=False)(10, 'GetCaretRange', ((1, 'isActive'),(1, 'pRetVal'),)))
    win32more.UI.Accessibility.ITextProvider
    return ITextProvider2
def _define_ITextEditProvider_head():
    class ITextEditProvider(win32more.UI.Accessibility.ITextProvider_head):
        Guid = Guid('ea3605b4-3a05-400e-b5f9-4e91b40f6176')
    return ITextEditProvider
def _define_ITextEditProvider():
    ITextEditProvider = win32more.UI.Accessibility.ITextEditProvider_head
    ITextEditProvider.GetActiveComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head), use_last_error=False)(9, 'GetActiveComposition', ((1, 'pRetVal'),)))
    ITextEditProvider.GetConversionTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head), use_last_error=False)(10, 'GetConversionTarget', ((1, 'pRetVal'),)))
    win32more.UI.Accessibility.ITextProvider
    return ITextEditProvider
def _define_ITextRangeProvider2_head():
    class ITextRangeProvider2(win32more.UI.Accessibility.ITextRangeProvider_head):
        Guid = Guid('9bbce42c-1921-4f18-89ca-dba1910a0386')
    return ITextRangeProvider2
def _define_ITextRangeProvider2():
    ITextRangeProvider2 = win32more.UI.Accessibility.ITextRangeProvider2_head
    ITextRangeProvider2.ShowContextMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'ShowContextMenu', ()))
    win32more.UI.Accessibility.ITextRangeProvider
    return ITextRangeProvider2
def _define_ITextChildProvider_head():
    class ITextChildProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('4c2de2b9-c88f-4f88-a111-f1d336b7d1a9')
    return ITextChildProvider
def _define_ITextChildProvider():
    ITextChildProvider = win32more.UI.Accessibility.ITextChildProvider_head
    ITextChildProvider.get_TextContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(3, 'get_TextContainer', ((1, 'pRetVal'),)))
    ITextChildProvider.get_TextRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ITextRangeProvider_head), use_last_error=False)(4, 'get_TextRange', ((1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ITextChildProvider
def _define_ICustomNavigationProvider_head():
    class ICustomNavigationProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('2062a28a-8c07-4b94-8e12-7037c622aeb8')
    return ICustomNavigationProvider
def _define_ICustomNavigationProvider():
    ICustomNavigationProvider = win32more.UI.Accessibility.ICustomNavigationProvider_head
    ICustomNavigationProvider.Navigate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.NavigateDirection,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(3, 'Navigate', ((1, 'direction'),(1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return ICustomNavigationProvider
def _define_IUIAutomationPatternInstance_head():
    class IUIAutomationPatternInstance(win32more.System.Com.IUnknown_head):
        Guid = Guid('c03a7fe4-9431-409f-bed8-ae7c2299bc8d')
    return IUIAutomationPatternInstance
def _define_IUIAutomationPatternInstance():
    IUIAutomationPatternInstance = win32more.UI.Accessibility.IUIAutomationPatternInstance_head
    IUIAutomationPatternInstance.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,win32more.UI.Accessibility.UIAutomationType,c_void_p, use_last_error=False)(3, 'GetProperty', ((1, 'index'),(1, 'cached'),(1, 'type'),(1, 'pPtr'),)))
    IUIAutomationPatternInstance.CallMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Accessibility.UIAutomationParameter_head),UInt32, use_last_error=False)(4, 'CallMethod', ((1, 'index'),(1, 'pParams'),(1, 'cParams'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationPatternInstance
def _define_IUIAutomationPatternHandler_head():
    class IUIAutomationPatternHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('d97022f3-a947-465e-8b2a-ac4315fa54e8')
    return IUIAutomationPatternHandler
def _define_IUIAutomationPatternHandler():
    IUIAutomationPatternHandler = win32more.UI.Accessibility.IUIAutomationPatternHandler_head
    IUIAutomationPatternHandler.CreateClientWrapper = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationPatternInstance_head,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(3, 'CreateClientWrapper', ((1, 'pPatternInstance'),(1, 'pClientWrapper'),)))
    IUIAutomationPatternHandler.Dispatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,POINTER(win32more.UI.Accessibility.UIAutomationParameter_head),UInt32, use_last_error=False)(4, 'Dispatch', ((1, 'pTarget'),(1, 'index'),(1, 'pParams'),(1, 'cParams'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationPatternHandler
def _define_IUIAutomationRegistrar_head():
    class IUIAutomationRegistrar(win32more.System.Com.IUnknown_head):
        Guid = Guid('8609c4ec-4a1a-4d88-a357-5a66e060e1cf')
    return IUIAutomationRegistrar
def _define_IUIAutomationRegistrar():
    IUIAutomationRegistrar = win32more.UI.Accessibility.IUIAutomationRegistrar_head
    IUIAutomationRegistrar.RegisterProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIAutomationPropertyInfo_head),POINTER(Int32), use_last_error=False)(3, 'RegisterProperty', ((1, 'property'),(1, 'propertyId'),)))
    IUIAutomationRegistrar.RegisterEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIAutomationEventInfo_head),POINTER(Int32), use_last_error=False)(4, 'RegisterEvent', ((1, 'event'),(1, 'eventId'),)))
    IUIAutomationRegistrar.RegisterPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UIAutomationPatternInfo_head),POINTER(Int32),POINTER(Int32),UInt32,POINTER(Int32),UInt32,POINTER(Int32), use_last_error=False)(5, 'RegisterPattern', ((1, 'pattern'),(1, 'pPatternId'),(1, 'pPatternAvailablePropertyId'),(1, 'propertyIdCount'),(1, 'pPropertyIds'),(1, 'eventIdCount'),(1, 'pEventIds'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationRegistrar
TreeScope = Int32
TreeScope_None = 0
TreeScope_Element = 1
TreeScope_Children = 2
TreeScope_Descendants = 4
TreeScope_Parent = 8
TreeScope_Ancestors = 16
TreeScope_Subtree = 7
PropertyConditionFlags = Int32
PropertyConditionFlags_None = 0
PropertyConditionFlags_IgnoreCase = 1
PropertyConditionFlags_MatchSubstring = 2
AutomationElementMode = Int32
AutomationElementMode_None = 0
AutomationElementMode_Full = 1
TreeTraversalOptions = Int32
TreeTraversalOptions_Default = 0
TreeTraversalOptions_PostOrder = 1
TreeTraversalOptions_LastToFirstOrder = 2
ConnectionRecoveryBehaviorOptions = Int32
ConnectionRecoveryBehaviorOptions_Disabled = 0
ConnectionRecoveryBehaviorOptions_Enabled = 1
CoalesceEventsOptions = Int32
CoalesceEventsOptions_Disabled = 0
CoalesceEventsOptions_Enabled = 1
def _define_ExtendedProperty_head():
    class ExtendedProperty(Structure):
        pass
    return ExtendedProperty
def _define_ExtendedProperty():
    ExtendedProperty = win32more.UI.Accessibility.ExtendedProperty_head
    ExtendedProperty._fields_ = [
        ("PropertyName", win32more.Foundation.BSTR),
        ("PropertyValue", win32more.Foundation.BSTR),
    ]
    return ExtendedProperty
def _define_IUIAutomationElement_head():
    class IUIAutomationElement(win32more.System.Com.IUnknown_head):
        Guid = Guid('d22108aa-8ac5-49a5-837b-37bbb3d7591e')
    return IUIAutomationElement
def _define_IUIAutomationElement():
    IUIAutomationElement = win32more.UI.Accessibility.IUIAutomationElement_head
    IUIAutomationElement.SetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'SetFocus', ()))
    IUIAutomationElement.GetRuntimeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(4, 'GetRuntimeId', ((1, 'runtimeId'),)))
    IUIAutomationElement.FindFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(5, 'FindFirst', ((1, 'scope'),(1, 'condition'),(1, 'found'),)))
    IUIAutomationElement.FindAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(6, 'FindAll', ((1, 'scope'),(1, 'condition'),(1, 'found'),)))
    IUIAutomationElement.FindFirstBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(7, 'FindFirstBuildCache', ((1, 'scope'),(1, 'condition'),(1, 'cacheRequest'),(1, 'found'),)))
    IUIAutomationElement.FindAllBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(8, 'FindAllBuildCache', ((1, 'scope'),(1, 'condition'),(1, 'cacheRequest'),(1, 'found'),)))
    IUIAutomationElement.BuildUpdatedCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(9, 'BuildUpdatedCache', ((1, 'cacheRequest'),(1, 'updatedElement'),)))
    IUIAutomationElement.GetCurrentPropertyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'GetCurrentPropertyValue', ((1, 'propertyId'),(1, 'retVal'),)))
    IUIAutomationElement.GetCurrentPropertyValueEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BOOL,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(11, 'GetCurrentPropertyValueEx', ((1, 'propertyId'),(1, 'ignoreDefaultValue'),(1, 'retVal'),)))
    IUIAutomationElement.GetCachedPropertyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(12, 'GetCachedPropertyValue', ((1, 'propertyId'),(1, 'retVal'),)))
    IUIAutomationElement.GetCachedPropertyValueEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BOOL,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'GetCachedPropertyValueEx', ((1, 'propertyId'),(1, 'ignoreDefaultValue'),(1, 'retVal'),)))
    IUIAutomationElement.GetCurrentPatternAs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(14, 'GetCurrentPatternAs', ((1, 'patternId'),(1, 'riid'),(1, 'patternObject'),)))
    IUIAutomationElement.GetCachedPatternAs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(15, 'GetCachedPatternAs', ((1, 'patternId'),(1, 'riid'),(1, 'patternObject'),)))
    IUIAutomationElement.GetCurrentPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(16, 'GetCurrentPattern', ((1, 'patternId'),(1, 'patternObject'),)))
    IUIAutomationElement.GetCachedPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(17, 'GetCachedPattern', ((1, 'patternId'),(1, 'patternObject'),)))
    IUIAutomationElement.GetCachedParent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(18, 'GetCachedParent', ((1, 'parent'),)))
    IUIAutomationElement.GetCachedChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(19, 'GetCachedChildren', ((1, 'children'),)))
    IUIAutomationElement.get_CurrentProcessId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'get_CurrentProcessId', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentControlType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(21, 'get_CurrentControlType', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentLocalizedControlType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_CurrentLocalizedControlType', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_CurrentName', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentAcceleratorKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'get_CurrentAcceleratorKey', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentAccessKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(25, 'get_CurrentAccessKey', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentHasKeyboardFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(26, 'get_CurrentHasKeyboardFocus', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsKeyboardFocusable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(27, 'get_CurrentIsKeyboardFocusable', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(28, 'get_CurrentIsEnabled', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentAutomationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(29, 'get_CurrentAutomationId', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(30, 'get_CurrentClassName', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentHelpText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(31, 'get_CurrentHelpText', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentCulture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(32, 'get_CurrentCulture', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsControlElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(33, 'get_CurrentIsControlElement', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsContentElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(34, 'get_CurrentIsContentElement', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(35, 'get_CurrentIsPassword', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentNativeWindowHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(36, 'get_CurrentNativeWindowHandle', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentItemType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(37, 'get_CurrentItemType', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsOffscreen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(38, 'get_CurrentIsOffscreen', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.OrientationType), use_last_error=False)(39, 'get_CurrentOrientation', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentFrameworkId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(40, 'get_CurrentFrameworkId', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsRequiredForForm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(41, 'get_CurrentIsRequiredForForm', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentItemStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(42, 'get_CurrentItemStatus', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentBoundingRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(43, 'get_CurrentBoundingRectangle', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentLabeledBy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(44, 'get_CurrentLabeledBy', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentAriaRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(45, 'get_CurrentAriaRole', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentAriaProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(46, 'get_CurrentAriaProperties', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentIsDataValidForForm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(47, 'get_CurrentIsDataValidForForm', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentControllerFor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(48, 'get_CurrentControllerFor', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentDescribedBy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(49, 'get_CurrentDescribedBy', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentFlowsTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(50, 'get_CurrentFlowsTo', ((1, 'retVal'),)))
    IUIAutomationElement.get_CurrentProviderDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(51, 'get_CurrentProviderDescription', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedProcessId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(52, 'get_CachedProcessId', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedControlType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(53, 'get_CachedControlType', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedLocalizedControlType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(54, 'get_CachedLocalizedControlType', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(55, 'get_CachedName', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedAcceleratorKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(56, 'get_CachedAcceleratorKey', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedAccessKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(57, 'get_CachedAccessKey', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedHasKeyboardFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(58, 'get_CachedHasKeyboardFocus', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsKeyboardFocusable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(59, 'get_CachedIsKeyboardFocusable', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(60, 'get_CachedIsEnabled', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedAutomationId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(61, 'get_CachedAutomationId', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(62, 'get_CachedClassName', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedHelpText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(63, 'get_CachedHelpText', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedCulture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(64, 'get_CachedCulture', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsControlElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(65, 'get_CachedIsControlElement', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsContentElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(66, 'get_CachedIsContentElement', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(67, 'get_CachedIsPassword', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedNativeWindowHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(68, 'get_CachedNativeWindowHandle', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedItemType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(69, 'get_CachedItemType', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsOffscreen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(70, 'get_CachedIsOffscreen', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.OrientationType), use_last_error=False)(71, 'get_CachedOrientation', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedFrameworkId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(72, 'get_CachedFrameworkId', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsRequiredForForm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(73, 'get_CachedIsRequiredForForm', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedItemStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(74, 'get_CachedItemStatus', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedBoundingRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(75, 'get_CachedBoundingRectangle', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedLabeledBy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(76, 'get_CachedLabeledBy', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedAriaRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(77, 'get_CachedAriaRole', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedAriaProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(78, 'get_CachedAriaProperties', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedIsDataValidForForm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(79, 'get_CachedIsDataValidForForm', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedControllerFor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(80, 'get_CachedControllerFor', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedDescribedBy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(81, 'get_CachedDescribedBy', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedFlowsTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(82, 'get_CachedFlowsTo', ((1, 'retVal'),)))
    IUIAutomationElement.get_CachedProviderDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(83, 'get_CachedProviderDescription', ((1, 'retVal'),)))
    IUIAutomationElement.GetClickablePoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.POINT_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(84, 'GetClickablePoint', ((1, 'clickable'),(1, 'gotClickable'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationElement
def _define_IUIAutomationElementArray_head():
    class IUIAutomationElementArray(win32more.System.Com.IUnknown_head):
        Guid = Guid('14314595-b4bc-4055-95f2-58f2e42c9855')
    return IUIAutomationElementArray
def _define_IUIAutomationElementArray():
    IUIAutomationElementArray = win32more.UI.Accessibility.IUIAutomationElementArray_head
    IUIAutomationElementArray.get_Length = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'get_Length', ((1, 'length'),)))
    IUIAutomationElementArray.GetElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(4, 'GetElement', ((1, 'index'),(1, 'element'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationElementArray
def _define_IUIAutomationCondition_head():
    class IUIAutomationCondition(win32more.System.Com.IUnknown_head):
        Guid = Guid('352ffba8-0973-437c-a61f-f64cafd81df9')
    return IUIAutomationCondition
def _define_IUIAutomationCondition():
    IUIAutomationCondition = win32more.UI.Accessibility.IUIAutomationCondition_head
    win32more.System.Com.IUnknown
    return IUIAutomationCondition
def _define_IUIAutomationBoolCondition_head():
    class IUIAutomationBoolCondition(win32more.UI.Accessibility.IUIAutomationCondition_head):
        Guid = Guid('1b4e1f2e-75eb-4d0b-8952-5a69988e2307')
    return IUIAutomationBoolCondition
def _define_IUIAutomationBoolCondition():
    IUIAutomationBoolCondition = win32more.UI.Accessibility.IUIAutomationBoolCondition_head
    IUIAutomationBoolCondition.get_BooleanValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'get_BooleanValue', ((1, 'boolVal'),)))
    win32more.UI.Accessibility.IUIAutomationCondition
    return IUIAutomationBoolCondition
def _define_IUIAutomationPropertyCondition_head():
    class IUIAutomationPropertyCondition(win32more.UI.Accessibility.IUIAutomationCondition_head):
        Guid = Guid('99ebf2cb-5578-4267-9ad4-afd6ea77e94b')
    return IUIAutomationPropertyCondition
def _define_IUIAutomationPropertyCondition():
    IUIAutomationPropertyCondition = win32more.UI.Accessibility.IUIAutomationPropertyCondition_head
    IUIAutomationPropertyCondition.get_PropertyId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'get_PropertyId', ((1, 'propertyId'),)))
    IUIAutomationPropertyCondition.get_PropertyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(4, 'get_PropertyValue', ((1, 'propertyValue'),)))
    IUIAutomationPropertyCondition.get_PropertyConditionFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.PropertyConditionFlags), use_last_error=False)(5, 'get_PropertyConditionFlags', ((1, 'flags'),)))
    win32more.UI.Accessibility.IUIAutomationCondition
    return IUIAutomationPropertyCondition
def _define_IUIAutomationAndCondition_head():
    class IUIAutomationAndCondition(win32more.UI.Accessibility.IUIAutomationCondition_head):
        Guid = Guid('a7d0af36-b912-45fe-9855-091ddc174aec')
    return IUIAutomationAndCondition
def _define_IUIAutomationAndCondition():
    IUIAutomationAndCondition = win32more.UI.Accessibility.IUIAutomationAndCondition_head
    IUIAutomationAndCondition.get_ChildCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'get_ChildCount', ((1, 'childCount'),)))
    IUIAutomationAndCondition.GetChildrenAsNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head)),POINTER(Int32), use_last_error=False)(4, 'GetChildrenAsNativeArray', ((1, 'childArray'),(1, 'childArrayCount'),)))
    IUIAutomationAndCondition.GetChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(5, 'GetChildren', ((1, 'childArray'),)))
    win32more.UI.Accessibility.IUIAutomationCondition
    return IUIAutomationAndCondition
def _define_IUIAutomationOrCondition_head():
    class IUIAutomationOrCondition(win32more.UI.Accessibility.IUIAutomationCondition_head):
        Guid = Guid('8753f032-3db1-47b5-a1fc-6e34a266c712')
    return IUIAutomationOrCondition
def _define_IUIAutomationOrCondition():
    IUIAutomationOrCondition = win32more.UI.Accessibility.IUIAutomationOrCondition_head
    IUIAutomationOrCondition.get_ChildCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'get_ChildCount', ((1, 'childCount'),)))
    IUIAutomationOrCondition.GetChildrenAsNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head)),POINTER(Int32), use_last_error=False)(4, 'GetChildrenAsNativeArray', ((1, 'childArray'),(1, 'childArrayCount'),)))
    IUIAutomationOrCondition.GetChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(5, 'GetChildren', ((1, 'childArray'),)))
    win32more.UI.Accessibility.IUIAutomationCondition
    return IUIAutomationOrCondition
def _define_IUIAutomationNotCondition_head():
    class IUIAutomationNotCondition(win32more.UI.Accessibility.IUIAutomationCondition_head):
        Guid = Guid('f528b657-847b-498c-8896-d52b565407a1')
    return IUIAutomationNotCondition
def _define_IUIAutomationNotCondition():
    IUIAutomationNotCondition = win32more.UI.Accessibility.IUIAutomationNotCondition_head
    IUIAutomationNotCondition.GetChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(3, 'GetChild', ((1, 'condition'),)))
    win32more.UI.Accessibility.IUIAutomationCondition
    return IUIAutomationNotCondition
def _define_IUIAutomationCacheRequest_head():
    class IUIAutomationCacheRequest(win32more.System.Com.IUnknown_head):
        Guid = Guid('b32a92b5-bc25-4078-9c08-d7ee95c48e03')
    return IUIAutomationCacheRequest
def _define_IUIAutomationCacheRequest():
    IUIAutomationCacheRequest = win32more.UI.Accessibility.IUIAutomationCacheRequest_head
    IUIAutomationCacheRequest.AddProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'AddProperty', ((1, 'propertyId'),)))
    IUIAutomationCacheRequest.AddPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(4, 'AddPattern', ((1, 'patternId'),)))
    IUIAutomationCacheRequest.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCacheRequest_head), use_last_error=False)(5, 'Clone', ((1, 'clonedRequest'),)))
    IUIAutomationCacheRequest.get_TreeScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.TreeScope), use_last_error=False)(6, 'get_TreeScope', ((1, 'scope'),)))
    IUIAutomationCacheRequest.put_TreeScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope, use_last_error=False)(7, 'put_TreeScope', ((1, 'scope'),)))
    IUIAutomationCacheRequest.get_TreeFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(8, 'get_TreeFilter', ((1, 'filter'),)))
    IUIAutomationCacheRequest.put_TreeFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCondition_head, use_last_error=False)(9, 'put_TreeFilter', ((1, 'filter'),)))
    IUIAutomationCacheRequest.get_AutomationElementMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.AutomationElementMode), use_last_error=False)(10, 'get_AutomationElementMode', ((1, 'mode'),)))
    IUIAutomationCacheRequest.put_AutomationElementMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.AutomationElementMode, use_last_error=False)(11, 'put_AutomationElementMode', ((1, 'mode'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationCacheRequest
def _define_IUIAutomationTreeWalker_head():
    class IUIAutomationTreeWalker(win32more.System.Com.IUnknown_head):
        Guid = Guid('4042c624-389c-4afc-a630-9df854a541fc')
    return IUIAutomationTreeWalker
def _define_IUIAutomationTreeWalker():
    IUIAutomationTreeWalker = win32more.UI.Accessibility.IUIAutomationTreeWalker_head
    IUIAutomationTreeWalker.GetParentElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(3, 'GetParentElement', ((1, 'element'),(1, 'parent'),)))
    IUIAutomationTreeWalker.GetFirstChildElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(4, 'GetFirstChildElement', ((1, 'element'),(1, 'first'),)))
    IUIAutomationTreeWalker.GetLastChildElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(5, 'GetLastChildElement', ((1, 'element'),(1, 'last'),)))
    IUIAutomationTreeWalker.GetNextSiblingElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(6, 'GetNextSiblingElement', ((1, 'element'),(1, 'next'),)))
    IUIAutomationTreeWalker.GetPreviousSiblingElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(7, 'GetPreviousSiblingElement', ((1, 'element'),(1, 'previous'),)))
    IUIAutomationTreeWalker.NormalizeElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(8, 'NormalizeElement', ((1, 'element'),(1, 'normalized'),)))
    IUIAutomationTreeWalker.GetParentElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(9, 'GetParentElementBuildCache', ((1, 'element'),(1, 'cacheRequest'),(1, 'parent'),)))
    IUIAutomationTreeWalker.GetFirstChildElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(10, 'GetFirstChildElementBuildCache', ((1, 'element'),(1, 'cacheRequest'),(1, 'first'),)))
    IUIAutomationTreeWalker.GetLastChildElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(11, 'GetLastChildElementBuildCache', ((1, 'element'),(1, 'cacheRequest'),(1, 'last'),)))
    IUIAutomationTreeWalker.GetNextSiblingElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(12, 'GetNextSiblingElementBuildCache', ((1, 'element'),(1, 'cacheRequest'),(1, 'next'),)))
    IUIAutomationTreeWalker.GetPreviousSiblingElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(13, 'GetPreviousSiblingElementBuildCache', ((1, 'element'),(1, 'cacheRequest'),(1, 'previous'),)))
    IUIAutomationTreeWalker.NormalizeElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(14, 'NormalizeElementBuildCache', ((1, 'element'),(1, 'cacheRequest'),(1, 'normalized'),)))
    IUIAutomationTreeWalker.get_Condition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(15, 'get_Condition', ((1, 'condition'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTreeWalker
def _define_IUIAutomationEventHandler_head():
    class IUIAutomationEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('146c3c17-f12e-4e22-8c27-f894b9b79c69')
    return IUIAutomationEventHandler
def _define_IUIAutomationEventHandler():
    IUIAutomationEventHandler = win32more.UI.Accessibility.IUIAutomationEventHandler_head
    IUIAutomationEventHandler.HandleAutomationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,Int32, use_last_error=False)(3, 'HandleAutomationEvent', ((1, 'sender'),(1, 'eventId'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationEventHandler
def _define_IUIAutomationPropertyChangedEventHandler_head():
    class IUIAutomationPropertyChangedEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('40cd37d4-c756-4b0c-8c6f-bddfeeb13b50')
    return IUIAutomationPropertyChangedEventHandler
def _define_IUIAutomationPropertyChangedEventHandler():
    IUIAutomationPropertyChangedEventHandler = win32more.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head
    IUIAutomationPropertyChangedEventHandler.HandlePropertyChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,Int32,win32more.System.Com.VARIANT, use_last_error=False)(3, 'HandlePropertyChangedEvent', ((1, 'sender'),(1, 'propertyId'),(1, 'newValue'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationPropertyChangedEventHandler
def _define_IUIAutomationStructureChangedEventHandler_head():
    class IUIAutomationStructureChangedEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('e81d1b4e-11c5-42f8-9754-e7036c79f054')
    return IUIAutomationStructureChangedEventHandler
def _define_IUIAutomationStructureChangedEventHandler():
    IUIAutomationStructureChangedEventHandler = win32more.UI.Accessibility.IUIAutomationStructureChangedEventHandler_head
    IUIAutomationStructureChangedEventHandler.HandleStructureChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.StructureChangeType,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(3, 'HandleStructureChangedEvent', ((1, 'sender'),(1, 'changeType'),(1, 'runtimeId'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationStructureChangedEventHandler
def _define_IUIAutomationFocusChangedEventHandler_head():
    class IUIAutomationFocusChangedEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('c270f6b5-5c69-4290-9745-7a7f97169468')
    return IUIAutomationFocusChangedEventHandler
def _define_IUIAutomationFocusChangedEventHandler():
    IUIAutomationFocusChangedEventHandler = win32more.UI.Accessibility.IUIAutomationFocusChangedEventHandler_head
    IUIAutomationFocusChangedEventHandler.HandleFocusChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head, use_last_error=False)(3, 'HandleFocusChangedEvent', ((1, 'sender'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationFocusChangedEventHandler
def _define_IUIAutomationTextEditTextChangedEventHandler_head():
    class IUIAutomationTextEditTextChangedEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('92faa680-e704-4156-931a-e32d5bb38f3f')
    return IUIAutomationTextEditTextChangedEventHandler
def _define_IUIAutomationTextEditTextChangedEventHandler():
    IUIAutomationTextEditTextChangedEventHandler = win32more.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler_head
    IUIAutomationTextEditTextChangedEventHandler.HandleTextEditTextChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TextEditChangeType,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(3, 'HandleTextEditTextChangedEvent', ((1, 'sender'),(1, 'textEditChangeType'),(1, 'eventStrings'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTextEditTextChangedEventHandler
def _define_IUIAutomationChangesEventHandler_head():
    class IUIAutomationChangesEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('58edca55-2c3e-4980-b1b9-56c17f27a2a0')
    return IUIAutomationChangesEventHandler
def _define_IUIAutomationChangesEventHandler():
    IUIAutomationChangesEventHandler = win32more.UI.Accessibility.IUIAutomationChangesEventHandler_head
    IUIAutomationChangesEventHandler.HandleChangesEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.UiaChangeInfo),Int32, use_last_error=False)(3, 'HandleChangesEvent', ((1, 'sender'),(1, 'uiaChanges'),(1, 'changesCount'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationChangesEventHandler
def _define_IUIAutomationNotificationEventHandler_head():
    class IUIAutomationNotificationEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('c7cb2637-e6c2-4d0c-85de-4948c02175c7')
    return IUIAutomationNotificationEventHandler
def _define_IUIAutomationNotificationEventHandler():
    IUIAutomationNotificationEventHandler = win32more.UI.Accessibility.IUIAutomationNotificationEventHandler_head
    IUIAutomationNotificationEventHandler.HandleNotificationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.NotificationKind,win32more.UI.Accessibility.NotificationProcessing,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(3, 'HandleNotificationEvent', ((1, 'sender'),(1, 'notificationKind'),(1, 'notificationProcessing'),(1, 'displayString'),(1, 'activityId'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationNotificationEventHandler
def _define_IUIAutomationInvokePattern_head():
    class IUIAutomationInvokePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('fb377fbe-8ea6-46d5-9c73-6499642d3059')
    return IUIAutomationInvokePattern
def _define_IUIAutomationInvokePattern():
    IUIAutomationInvokePattern = win32more.UI.Accessibility.IUIAutomationInvokePattern_head
    IUIAutomationInvokePattern.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Invoke', ()))
    win32more.System.Com.IUnknown
    return IUIAutomationInvokePattern
def _define_IUIAutomationDockPattern_head():
    class IUIAutomationDockPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('fde5ef97-1464-48f6-90bf-43d0948e86ec')
    return IUIAutomationDockPattern
def _define_IUIAutomationDockPattern():
    IUIAutomationDockPattern = win32more.UI.Accessibility.IUIAutomationDockPattern_head
    IUIAutomationDockPattern.SetDockPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.DockPosition, use_last_error=False)(3, 'SetDockPosition', ((1, 'dockPos'),)))
    IUIAutomationDockPattern.get_CurrentDockPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.DockPosition), use_last_error=False)(4, 'get_CurrentDockPosition', ((1, 'retVal'),)))
    IUIAutomationDockPattern.get_CachedDockPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.DockPosition), use_last_error=False)(5, 'get_CachedDockPosition', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationDockPattern
def _define_IUIAutomationExpandCollapsePattern_head():
    class IUIAutomationExpandCollapsePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('619be086-1f4e-4ee4-bafa-210128738730')
    return IUIAutomationExpandCollapsePattern
def _define_IUIAutomationExpandCollapsePattern():
    IUIAutomationExpandCollapsePattern = win32more.UI.Accessibility.IUIAutomationExpandCollapsePattern_head
    IUIAutomationExpandCollapsePattern.Expand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Expand', ()))
    IUIAutomationExpandCollapsePattern.Collapse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Collapse', ()))
    IUIAutomationExpandCollapsePattern.get_CurrentExpandCollapseState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ExpandCollapseState), use_last_error=False)(5, 'get_CurrentExpandCollapseState', ((1, 'retVal'),)))
    IUIAutomationExpandCollapsePattern.get_CachedExpandCollapseState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ExpandCollapseState), use_last_error=False)(6, 'get_CachedExpandCollapseState', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationExpandCollapsePattern
def _define_IUIAutomationGridPattern_head():
    class IUIAutomationGridPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('414c3cdc-856b-4f5b-8538-3131c6302550')
    return IUIAutomationGridPattern
def _define_IUIAutomationGridPattern():
    IUIAutomationGridPattern = win32more.UI.Accessibility.IUIAutomationGridPattern_head
    IUIAutomationGridPattern.GetItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(3, 'GetItem', ((1, 'row'),(1, 'column'),(1, 'element'),)))
    IUIAutomationGridPattern.get_CurrentRowCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(4, 'get_CurrentRowCount', ((1, 'retVal'),)))
    IUIAutomationGridPattern.get_CurrentColumnCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(5, 'get_CurrentColumnCount', ((1, 'retVal'),)))
    IUIAutomationGridPattern.get_CachedRowCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(6, 'get_CachedRowCount', ((1, 'retVal'),)))
    IUIAutomationGridPattern.get_CachedColumnCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_CachedColumnCount', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationGridPattern
def _define_IUIAutomationGridItemPattern_head():
    class IUIAutomationGridItemPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('78f8ef57-66c3-4e09-bd7c-e79b2004894d')
    return IUIAutomationGridItemPattern
def _define_IUIAutomationGridItemPattern():
    IUIAutomationGridItemPattern = win32more.UI.Accessibility.IUIAutomationGridItemPattern_head
    IUIAutomationGridItemPattern.get_CurrentContainingGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(3, 'get_CurrentContainingGrid', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CurrentRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(4, 'get_CurrentRow', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CurrentColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(5, 'get_CurrentColumn', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CurrentRowSpan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(6, 'get_CurrentRowSpan', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CurrentColumnSpan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_CurrentColumnSpan', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CachedContainingGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(8, 'get_CachedContainingGrid', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CachedRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_CachedRow', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CachedColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(10, 'get_CachedColumn', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CachedRowSpan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_CachedRowSpan', ((1, 'retVal'),)))
    IUIAutomationGridItemPattern.get_CachedColumnSpan = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_CachedColumnSpan', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationGridItemPattern
def _define_IUIAutomationMultipleViewPattern_head():
    class IUIAutomationMultipleViewPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('8d253c91-1dc5-4bb5-b18f-ade16fa495e8')
    return IUIAutomationMultipleViewPattern
def _define_IUIAutomationMultipleViewPattern():
    IUIAutomationMultipleViewPattern = win32more.UI.Accessibility.IUIAutomationMultipleViewPattern_head
    IUIAutomationMultipleViewPattern.GetViewName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetViewName', ((1, 'view'),(1, 'name'),)))
    IUIAutomationMultipleViewPattern.SetCurrentView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(4, 'SetCurrentView', ((1, 'view'),)))
    IUIAutomationMultipleViewPattern.get_CurrentCurrentView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(5, 'get_CurrentCurrentView', ((1, 'retVal'),)))
    IUIAutomationMultipleViewPattern.GetCurrentSupportedViews = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(6, 'GetCurrentSupportedViews', ((1, 'retVal'),)))
    IUIAutomationMultipleViewPattern.get_CachedCurrentView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_CachedCurrentView', ((1, 'retVal'),)))
    IUIAutomationMultipleViewPattern.GetCachedSupportedViews = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(8, 'GetCachedSupportedViews', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationMultipleViewPattern
def _define_IUIAutomationObjectModelPattern_head():
    class IUIAutomationObjectModelPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('71c284b3-c14d-4d14-981e-19751b0d756d')
    return IUIAutomationObjectModelPattern
def _define_IUIAutomationObjectModelPattern():
    IUIAutomationObjectModelPattern = win32more.UI.Accessibility.IUIAutomationObjectModelPattern_head
    IUIAutomationObjectModelPattern.GetUnderlyingObjectModel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(3, 'GetUnderlyingObjectModel', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationObjectModelPattern
def _define_IUIAutomationRangeValuePattern_head():
    class IUIAutomationRangeValuePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('59213f4f-7346-49e5-b120-80555987a148')
    return IUIAutomationRangeValuePattern
def _define_IUIAutomationRangeValuePattern():
    IUIAutomationRangeValuePattern = win32more.UI.Accessibility.IUIAutomationRangeValuePattern_head
    IUIAutomationRangeValuePattern.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(3, 'SetValue', ((1, 'val'),)))
    IUIAutomationRangeValuePattern.get_CurrentValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(4, 'get_CurrentValue', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CurrentIsReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'get_CurrentIsReadOnly', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CurrentMaximum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(6, 'get_CurrentMaximum', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CurrentMinimum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(7, 'get_CurrentMinimum', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CurrentLargeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(8, 'get_CurrentLargeChange', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CurrentSmallChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(9, 'get_CurrentSmallChange', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CachedValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(10, 'get_CachedValue', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CachedIsReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'get_CachedIsReadOnly', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CachedMaximum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(12, 'get_CachedMaximum', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CachedMinimum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(13, 'get_CachedMinimum', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CachedLargeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(14, 'get_CachedLargeChange', ((1, 'retVal'),)))
    IUIAutomationRangeValuePattern.get_CachedSmallChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(15, 'get_CachedSmallChange', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationRangeValuePattern
def _define_IUIAutomationScrollPattern_head():
    class IUIAutomationScrollPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('88f4d42a-e881-459d-a77c-73bbbb7e02dc')
    return IUIAutomationScrollPattern
def _define_IUIAutomationScrollPattern():
    IUIAutomationScrollPattern = win32more.UI.Accessibility.IUIAutomationScrollPattern_head
    IUIAutomationScrollPattern.Scroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.ScrollAmount,win32more.UI.Accessibility.ScrollAmount, use_last_error=False)(3, 'Scroll', ((1, 'horizontalAmount'),(1, 'verticalAmount'),)))
    IUIAutomationScrollPattern.SetScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double, use_last_error=False)(4, 'SetScrollPercent', ((1, 'horizontalPercent'),(1, 'verticalPercent'),)))
    IUIAutomationScrollPattern.get_CurrentHorizontalScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(5, 'get_CurrentHorizontalScrollPercent', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CurrentVerticalScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(6, 'get_CurrentVerticalScrollPercent', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CurrentHorizontalViewSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(7, 'get_CurrentHorizontalViewSize', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CurrentVerticalViewSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(8, 'get_CurrentVerticalViewSize', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CurrentHorizontallyScrollable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'get_CurrentHorizontallyScrollable', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CurrentVerticallyScrollable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(10, 'get_CurrentVerticallyScrollable', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CachedHorizontalScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(11, 'get_CachedHorizontalScrollPercent', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CachedVerticalScrollPercent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(12, 'get_CachedVerticalScrollPercent', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CachedHorizontalViewSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(13, 'get_CachedHorizontalViewSize', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CachedVerticalViewSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(14, 'get_CachedVerticalViewSize', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CachedHorizontallyScrollable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(15, 'get_CachedHorizontallyScrollable', ((1, 'retVal'),)))
    IUIAutomationScrollPattern.get_CachedVerticallyScrollable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(16, 'get_CachedVerticallyScrollable', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationScrollPattern
def _define_IUIAutomationScrollItemPattern_head():
    class IUIAutomationScrollItemPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('b488300f-d015-4f19-9c29-bb595e3645ef')
    return IUIAutomationScrollItemPattern
def _define_IUIAutomationScrollItemPattern():
    IUIAutomationScrollItemPattern = win32more.UI.Accessibility.IUIAutomationScrollItemPattern_head
    IUIAutomationScrollItemPattern.ScrollIntoView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'ScrollIntoView', ()))
    win32more.System.Com.IUnknown
    return IUIAutomationScrollItemPattern
def _define_IUIAutomationSelectionPattern_head():
    class IUIAutomationSelectionPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('5ed5202e-b2ac-47a6-b638-4b0bf140d78e')
    return IUIAutomationSelectionPattern
def _define_IUIAutomationSelectionPattern():
    IUIAutomationSelectionPattern = win32more.UI.Accessibility.IUIAutomationSelectionPattern_head
    IUIAutomationSelectionPattern.GetCurrentSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(3, 'GetCurrentSelection', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern.get_CurrentCanSelectMultiple = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'get_CurrentCanSelectMultiple', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern.get_CurrentIsSelectionRequired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'get_CurrentIsSelectionRequired', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern.GetCachedSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(6, 'GetCachedSelection', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern.get_CachedCanSelectMultiple = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'get_CachedCanSelectMultiple', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern.get_CachedIsSelectionRequired = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'get_CachedIsSelectionRequired', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationSelectionPattern
def _define_IUIAutomationSelectionPattern2_head():
    class IUIAutomationSelectionPattern2(win32more.UI.Accessibility.IUIAutomationSelectionPattern_head):
        Guid = Guid('0532bfae-c011-4e32-a343-6d642d798555')
    return IUIAutomationSelectionPattern2
def _define_IUIAutomationSelectionPattern2():
    IUIAutomationSelectionPattern2 = win32more.UI.Accessibility.IUIAutomationSelectionPattern2_head
    IUIAutomationSelectionPattern2.get_CurrentFirstSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(9, 'get_CurrentFirstSelectedItem', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CurrentLastSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(10, 'get_CurrentLastSelectedItem', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CurrentCurrentSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(11, 'get_CurrentCurrentSelectedItem', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CurrentItemCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'get_CurrentItemCount', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CachedFirstSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(13, 'get_CachedFirstSelectedItem', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CachedLastSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(14, 'get_CachedLastSelectedItem', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CachedCurrentSelectedItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(15, 'get_CachedCurrentSelectedItem', ((1, 'retVal'),)))
    IUIAutomationSelectionPattern2.get_CachedItemCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'get_CachedItemCount', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationSelectionPattern
    return IUIAutomationSelectionPattern2
def _define_IUIAutomationSelectionItemPattern_head():
    class IUIAutomationSelectionItemPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('a8efa66a-0fda-421a-9194-38021f3578ea')
    return IUIAutomationSelectionItemPattern
def _define_IUIAutomationSelectionItemPattern():
    IUIAutomationSelectionItemPattern = win32more.UI.Accessibility.IUIAutomationSelectionItemPattern_head
    IUIAutomationSelectionItemPattern.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Select', ()))
    IUIAutomationSelectionItemPattern.AddToSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'AddToSelection', ()))
    IUIAutomationSelectionItemPattern.RemoveFromSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'RemoveFromSelection', ()))
    IUIAutomationSelectionItemPattern.get_CurrentIsSelected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'get_CurrentIsSelected', ((1, 'retVal'),)))
    IUIAutomationSelectionItemPattern.get_CurrentSelectionContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(7, 'get_CurrentSelectionContainer', ((1, 'retVal'),)))
    IUIAutomationSelectionItemPattern.get_CachedIsSelected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'get_CachedIsSelected', ((1, 'retVal'),)))
    IUIAutomationSelectionItemPattern.get_CachedSelectionContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(9, 'get_CachedSelectionContainer', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationSelectionItemPattern
def _define_IUIAutomationSynchronizedInputPattern_head():
    class IUIAutomationSynchronizedInputPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('2233be0b-afb7-448b-9fda-3b378aa5eae1')
    return IUIAutomationSynchronizedInputPattern
def _define_IUIAutomationSynchronizedInputPattern():
    IUIAutomationSynchronizedInputPattern = win32more.UI.Accessibility.IUIAutomationSynchronizedInputPattern_head
    IUIAutomationSynchronizedInputPattern.StartListening = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.SynchronizedInputType, use_last_error=False)(3, 'StartListening', ((1, 'inputType'),)))
    IUIAutomationSynchronizedInputPattern.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Cancel', ()))
    win32more.System.Com.IUnknown
    return IUIAutomationSynchronizedInputPattern
def _define_IUIAutomationTablePattern_head():
    class IUIAutomationTablePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('620e691c-ea96-4710-a850-754b24ce2417')
    return IUIAutomationTablePattern
def _define_IUIAutomationTablePattern():
    IUIAutomationTablePattern = win32more.UI.Accessibility.IUIAutomationTablePattern_head
    IUIAutomationTablePattern.GetCurrentRowHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(3, 'GetCurrentRowHeaders', ((1, 'retVal'),)))
    IUIAutomationTablePattern.GetCurrentColumnHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(4, 'GetCurrentColumnHeaders', ((1, 'retVal'),)))
    IUIAutomationTablePattern.get_CurrentRowOrColumnMajor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.RowOrColumnMajor), use_last_error=False)(5, 'get_CurrentRowOrColumnMajor', ((1, 'retVal'),)))
    IUIAutomationTablePattern.GetCachedRowHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(6, 'GetCachedRowHeaders', ((1, 'retVal'),)))
    IUIAutomationTablePattern.GetCachedColumnHeaders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(7, 'GetCachedColumnHeaders', ((1, 'retVal'),)))
    IUIAutomationTablePattern.get_CachedRowOrColumnMajor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.RowOrColumnMajor), use_last_error=False)(8, 'get_CachedRowOrColumnMajor', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTablePattern
def _define_IUIAutomationTableItemPattern_head():
    class IUIAutomationTableItemPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('0b964eb3-ef2e-4464-9c79-61d61737a27e')
    return IUIAutomationTableItemPattern
def _define_IUIAutomationTableItemPattern():
    IUIAutomationTableItemPattern = win32more.UI.Accessibility.IUIAutomationTableItemPattern_head
    IUIAutomationTableItemPattern.GetCurrentRowHeaderItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(3, 'GetCurrentRowHeaderItems', ((1, 'retVal'),)))
    IUIAutomationTableItemPattern.GetCurrentColumnHeaderItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(4, 'GetCurrentColumnHeaderItems', ((1, 'retVal'),)))
    IUIAutomationTableItemPattern.GetCachedRowHeaderItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(5, 'GetCachedRowHeaderItems', ((1, 'retVal'),)))
    IUIAutomationTableItemPattern.GetCachedColumnHeaderItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(6, 'GetCachedColumnHeaderItems', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTableItemPattern
def _define_IUIAutomationTogglePattern_head():
    class IUIAutomationTogglePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('94cf8058-9b8d-4ab9-8bfd-4cd0a33c8c70')
    return IUIAutomationTogglePattern
def _define_IUIAutomationTogglePattern():
    IUIAutomationTogglePattern = win32more.UI.Accessibility.IUIAutomationTogglePattern_head
    IUIAutomationTogglePattern.Toggle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Toggle', ()))
    IUIAutomationTogglePattern.get_CurrentToggleState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ToggleState), use_last_error=False)(4, 'get_CurrentToggleState', ((1, 'retVal'),)))
    IUIAutomationTogglePattern.get_CachedToggleState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ToggleState), use_last_error=False)(5, 'get_CachedToggleState', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTogglePattern
def _define_IUIAutomationTransformPattern_head():
    class IUIAutomationTransformPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('a9b55844-a55d-4ef0-926d-569c16ff89bb')
    return IUIAutomationTransformPattern
def _define_IUIAutomationTransformPattern():
    IUIAutomationTransformPattern = win32more.UI.Accessibility.IUIAutomationTransformPattern_head
    IUIAutomationTransformPattern.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double, use_last_error=False)(3, 'Move', ((1, 'x'),(1, 'y'),)))
    IUIAutomationTransformPattern.Resize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double, use_last_error=False)(4, 'Resize', ((1, 'width'),(1, 'height'),)))
    IUIAutomationTransformPattern.Rotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(5, 'Rotate', ((1, 'degrees'),)))
    IUIAutomationTransformPattern.get_CurrentCanMove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'get_CurrentCanMove', ((1, 'retVal'),)))
    IUIAutomationTransformPattern.get_CurrentCanResize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'get_CurrentCanResize', ((1, 'retVal'),)))
    IUIAutomationTransformPattern.get_CurrentCanRotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'get_CurrentCanRotate', ((1, 'retVal'),)))
    IUIAutomationTransformPattern.get_CachedCanMove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'get_CachedCanMove', ((1, 'retVal'),)))
    IUIAutomationTransformPattern.get_CachedCanResize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(10, 'get_CachedCanResize', ((1, 'retVal'),)))
    IUIAutomationTransformPattern.get_CachedCanRotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'get_CachedCanRotate', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTransformPattern
def _define_IUIAutomationValuePattern_head():
    class IUIAutomationValuePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('a94cd8b1-0844-4cd6-9d2d-640537ab39e9')
    return IUIAutomationValuePattern
def _define_IUIAutomationValuePattern():
    IUIAutomationValuePattern = win32more.UI.Accessibility.IUIAutomationValuePattern_head
    IUIAutomationValuePattern.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(3, 'SetValue', ((1, 'val'),)))
    IUIAutomationValuePattern.get_CurrentValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_CurrentValue', ((1, 'retVal'),)))
    IUIAutomationValuePattern.get_CurrentIsReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'get_CurrentIsReadOnly', ((1, 'retVal'),)))
    IUIAutomationValuePattern.get_CachedValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'get_CachedValue', ((1, 'retVal'),)))
    IUIAutomationValuePattern.get_CachedIsReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'get_CachedIsReadOnly', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationValuePattern
def _define_IUIAutomationWindowPattern_head():
    class IUIAutomationWindowPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('0faef453-9208-43ef-bbb2-3b485177864f')
    return IUIAutomationWindowPattern
def _define_IUIAutomationWindowPattern():
    IUIAutomationWindowPattern = win32more.UI.Accessibility.IUIAutomationWindowPattern_head
    IUIAutomationWindowPattern.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Close', ()))
    IUIAutomationWindowPattern.WaitForInputIdle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'WaitForInputIdle', ((1, 'milliseconds'),(1, 'success'),)))
    IUIAutomationWindowPattern.SetWindowVisualState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.WindowVisualState, use_last_error=False)(5, 'SetWindowVisualState', ((1, 'state'),)))
    IUIAutomationWindowPattern.get_CurrentCanMaximize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'get_CurrentCanMaximize', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CurrentCanMinimize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'get_CurrentCanMinimize', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CurrentIsModal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'get_CurrentIsModal', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CurrentIsTopmost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'get_CurrentIsTopmost', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CurrentWindowVisualState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.WindowVisualState), use_last_error=False)(10, 'get_CurrentWindowVisualState', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CurrentWindowInteractionState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.WindowInteractionState), use_last_error=False)(11, 'get_CurrentWindowInteractionState', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CachedCanMaximize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'get_CachedCanMaximize', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CachedCanMinimize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'get_CachedCanMinimize', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CachedIsModal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(14, 'get_CachedIsModal', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CachedIsTopmost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(15, 'get_CachedIsTopmost', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CachedWindowVisualState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.WindowVisualState), use_last_error=False)(16, 'get_CachedWindowVisualState', ((1, 'retVal'),)))
    IUIAutomationWindowPattern.get_CachedWindowInteractionState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.WindowInteractionState), use_last_error=False)(17, 'get_CachedWindowInteractionState', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationWindowPattern
def _define_IUIAutomationTextRange_head():
    class IUIAutomationTextRange(win32more.System.Com.IUnknown_head):
        Guid = Guid('a543cc6a-f4ae-494b-8239-c814481187a8')
    return IUIAutomationTextRange
def _define_IUIAutomationTextRange():
    IUIAutomationTextRange = win32more.UI.Accessibility.IUIAutomationTextRange_head
    IUIAutomationTextRange.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head), use_last_error=False)(3, 'Clone', ((1, 'clonedRange'),)))
    IUIAutomationTextRange.Compare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationTextRange_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'Compare', ((1, 'range'),(1, 'areSame'),)))
    IUIAutomationTextRange.CompareEndpoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.IUIAutomationTextRange_head,win32more.UI.Accessibility.TextPatternRangeEndpoint,POINTER(Int32), use_last_error=False)(5, 'CompareEndpoints', ((1, 'srcEndPoint'),(1, 'range'),(1, 'targetEndPoint'),(1, 'compValue'),)))
    IUIAutomationTextRange.ExpandToEnclosingUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextUnit, use_last_error=False)(6, 'ExpandToEnclosingUnit', ((1, 'textUnit'),)))
    IUIAutomationTextRange.FindAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.Foundation.BOOL,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head), use_last_error=False)(7, 'FindAttribute', ((1, 'attr'),(1, 'val'),(1, 'backward'),(1, 'found'),)))
    IUIAutomationTextRange.FindText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head), use_last_error=False)(8, 'FindText', ((1, 'text'),(1, 'backward'),(1, 'ignoreCase'),(1, 'found'),)))
    IUIAutomationTextRange.GetAttributeValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'GetAttributeValue', ((1, 'attr'),(1, 'value'),)))
    IUIAutomationTextRange.GetBoundingRectangles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(10, 'GetBoundingRectangles', ((1, 'boundingRects'),)))
    IUIAutomationTextRange.GetEnclosingElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(11, 'GetEnclosingElement', ((1, 'enclosingElement'),)))
    IUIAutomationTextRange.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'GetText', ((1, 'maxLength'),(1, 'text'),)))
    IUIAutomationTextRange.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextUnit,Int32,POINTER(Int32), use_last_error=False)(13, 'Move', ((1, 'unit'),(1, 'count'),(1, 'moved'),)))
    IUIAutomationTextRange.MoveEndpointByUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.TextUnit,Int32,POINTER(Int32), use_last_error=False)(14, 'MoveEndpointByUnit', ((1, 'endpoint'),(1, 'unit'),(1, 'count'),(1, 'moved'),)))
    IUIAutomationTextRange.MoveEndpointByRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.IUIAutomationTextRange_head,win32more.UI.Accessibility.TextPatternRangeEndpoint, use_last_error=False)(15, 'MoveEndpointByRange', ((1, 'srcEndPoint'),(1, 'range'),(1, 'targetEndPoint'),)))
    IUIAutomationTextRange.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Select', ()))
    IUIAutomationTextRange.AddToSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'AddToSelection', ()))
    IUIAutomationTextRange.RemoveFromSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'RemoveFromSelection', ()))
    IUIAutomationTextRange.ScrollIntoView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(19, 'ScrollIntoView', ((1, 'alignToTop'),)))
    IUIAutomationTextRange.GetChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(20, 'GetChildren', ((1, 'children'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTextRange
def _define_IUIAutomationTextRange2_head():
    class IUIAutomationTextRange2(win32more.UI.Accessibility.IUIAutomationTextRange_head):
        Guid = Guid('bb9b40e0-5e04-46bd-9be0-4b601b9afad4')
    return IUIAutomationTextRange2
def _define_IUIAutomationTextRange2():
    IUIAutomationTextRange2 = win32more.UI.Accessibility.IUIAutomationTextRange2_head
    IUIAutomationTextRange2.ShowContextMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'ShowContextMenu', ()))
    win32more.UI.Accessibility.IUIAutomationTextRange
    return IUIAutomationTextRange2
def _define_IUIAutomationTextRange3_head():
    class IUIAutomationTextRange3(win32more.UI.Accessibility.IUIAutomationTextRange2_head):
        Guid = Guid('6a315d69-5512-4c2e-85f0-53fce6dd4bc2')
    return IUIAutomationTextRange3
def _define_IUIAutomationTextRange3():
    IUIAutomationTextRange3 = win32more.UI.Accessibility.IUIAutomationTextRange3_head
    IUIAutomationTextRange3.GetEnclosingElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(22, 'GetEnclosingElementBuildCache', ((1, 'cacheRequest'),(1, 'enclosingElement'),)))
    IUIAutomationTextRange3.GetChildrenBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(23, 'GetChildrenBuildCache', ((1, 'cacheRequest'),(1, 'children'),)))
    IUIAutomationTextRange3.GetAttributeValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),Int32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(24, 'GetAttributeValues', ((1, 'attributeIds'),(1, 'attributeIdCount'),(1, 'attributeValues'),)))
    win32more.UI.Accessibility.IUIAutomationTextRange2
    return IUIAutomationTextRange3
def _define_IUIAutomationTextRangeArray_head():
    class IUIAutomationTextRangeArray(win32more.System.Com.IUnknown_head):
        Guid = Guid('ce4ae76a-e717-4c98-81ea-47371d028eb6')
    return IUIAutomationTextRangeArray
def _define_IUIAutomationTextRangeArray():
    IUIAutomationTextRangeArray = win32more.UI.Accessibility.IUIAutomationTextRangeArray_head
    IUIAutomationTextRangeArray.get_Length = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'get_Length', ((1, 'length'),)))
    IUIAutomationTextRangeArray.GetElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head), use_last_error=False)(4, 'GetElement', ((1, 'index'),(1, 'element'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTextRangeArray
def _define_IUIAutomationTextPattern_head():
    class IUIAutomationTextPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('32eba289-3583-42c9-9c59-3b6d9a1e9b6a')
    return IUIAutomationTextPattern
def _define_IUIAutomationTextPattern():
    IUIAutomationTextPattern = win32more.UI.Accessibility.IUIAutomationTextPattern_head
    IUIAutomationTextPattern.RangeFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head), use_last_error=False)(3, 'RangeFromPoint', ((1, 'pt'),(1, 'range'),)))
    IUIAutomationTextPattern.RangeFromChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head), use_last_error=False)(4, 'RangeFromChild', ((1, 'child'),(1, 'range'),)))
    IUIAutomationTextPattern.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRangeArray_head), use_last_error=False)(5, 'GetSelection', ((1, 'ranges'),)))
    IUIAutomationTextPattern.GetVisibleRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRangeArray_head), use_last_error=False)(6, 'GetVisibleRanges', ((1, 'ranges'),)))
    IUIAutomationTextPattern.get_DocumentRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head), use_last_error=False)(7, 'get_DocumentRange', ((1, 'range'),)))
    IUIAutomationTextPattern.get_SupportedTextSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.SupportedTextSelection), use_last_error=False)(8, 'get_SupportedTextSelection', ((1, 'supportedTextSelection'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTextPattern
def _define_IUIAutomationTextPattern2_head():
    class IUIAutomationTextPattern2(win32more.UI.Accessibility.IUIAutomationTextPattern_head):
        Guid = Guid('506a921a-fcc9-409f-b23b-37eb74106872')
    return IUIAutomationTextPattern2
def _define_IUIAutomationTextPattern2():
    IUIAutomationTextPattern2 = win32more.UI.Accessibility.IUIAutomationTextPattern2_head
    IUIAutomationTextPattern2.RangeFromAnnotation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head), use_last_error=False)(9, 'RangeFromAnnotation', ((1, 'annotation'),(1, 'range'),)))
    IUIAutomationTextPattern2.GetCaretRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head), use_last_error=False)(10, 'GetCaretRange', ((1, 'isActive'),(1, 'range'),)))
    win32more.UI.Accessibility.IUIAutomationTextPattern
    return IUIAutomationTextPattern2
def _define_IUIAutomationTextEditPattern_head():
    class IUIAutomationTextEditPattern(win32more.UI.Accessibility.IUIAutomationTextPattern_head):
        Guid = Guid('17e21576-996c-4870-99d9-bff323380c06')
    return IUIAutomationTextEditPattern
def _define_IUIAutomationTextEditPattern():
    IUIAutomationTextEditPattern = win32more.UI.Accessibility.IUIAutomationTextEditPattern_head
    IUIAutomationTextEditPattern.GetActiveComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head), use_last_error=False)(9, 'GetActiveComposition', ((1, 'range'),)))
    IUIAutomationTextEditPattern.GetConversionTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head), use_last_error=False)(10, 'GetConversionTarget', ((1, 'range'),)))
    win32more.UI.Accessibility.IUIAutomationTextPattern
    return IUIAutomationTextEditPattern
def _define_IUIAutomationCustomNavigationPattern_head():
    class IUIAutomationCustomNavigationPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('01ea217a-1766-47ed-a6cc-acf492854b1f')
    return IUIAutomationCustomNavigationPattern
def _define_IUIAutomationCustomNavigationPattern():
    IUIAutomationCustomNavigationPattern = win32more.UI.Accessibility.IUIAutomationCustomNavigationPattern_head
    IUIAutomationCustomNavigationPattern.Navigate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.NavigateDirection,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(3, 'Navigate', ((1, 'direction'),(1, 'pRetVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationCustomNavigationPattern
def _define_IUIAutomationActiveTextPositionChangedEventHandler_head():
    class IUIAutomationActiveTextPositionChangedEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('f97933b0-8dae-4496-8997-5ba015fe0d82')
    return IUIAutomationActiveTextPositionChangedEventHandler
def _define_IUIAutomationActiveTextPositionChangedEventHandler():
    IUIAutomationActiveTextPositionChangedEventHandler = win32more.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler_head
    IUIAutomationActiveTextPositionChangedEventHandler.HandleActiveTextPositionChangedEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationTextRange_head, use_last_error=False)(3, 'HandleActiveTextPositionChangedEvent', ((1, 'sender'),(1, 'range'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationActiveTextPositionChangedEventHandler
def _define_IUIAutomationLegacyIAccessiblePattern_head():
    class IUIAutomationLegacyIAccessiblePattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('828055ad-355b-4435-86d5-3b51c14a9b1b')
    return IUIAutomationLegacyIAccessiblePattern
def _define_IUIAutomationLegacyIAccessiblePattern():
    IUIAutomationLegacyIAccessiblePattern = win32more.UI.Accessibility.IUIAutomationLegacyIAccessiblePattern_head
    IUIAutomationLegacyIAccessiblePattern.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'Select', ((1, 'flagsSelect'),)))
    IUIAutomationLegacyIAccessiblePattern.DoDefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'DoDefaultAction', ()))
    IUIAutomationLegacyIAccessiblePattern.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SetValue', ((1, 'szValue'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentChildId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(6, 'get_CurrentChildId', ((1, 'pRetVal'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_CurrentName', ((1, 'pszName'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_CurrentValue', ((1, 'pszValue'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_CurrentDescription', ((1, 'pszDescription'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'get_CurrentRole', ((1, 'pdwRole'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'get_CurrentState', ((1, 'pdwState'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentHelp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_CurrentHelp', ((1, 'pszHelp'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentKeyboardShortcut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_CurrentKeyboardShortcut', ((1, 'pszKeyboardShortcut'),)))
    IUIAutomationLegacyIAccessiblePattern.GetCurrentSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(14, 'GetCurrentSelection', ((1, 'pvarSelectedChildren'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CurrentDefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_CurrentDefaultAction', ((1, 'pszDefaultAction'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedChildId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'get_CachedChildId', ((1, 'pRetVal'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_CachedName', ((1, 'pszName'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_CachedValue', ((1, 'pszValue'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(19, 'get_CachedDescription', ((1, 'pszDescription'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedRole = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(20, 'get_CachedRole', ((1, 'pdwRole'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(21, 'get_CachedState', ((1, 'pdwState'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedHelp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_CachedHelp', ((1, 'pszHelp'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedKeyboardShortcut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(23, 'get_CachedKeyboardShortcut', ((1, 'pszKeyboardShortcut'),)))
    IUIAutomationLegacyIAccessiblePattern.GetCachedSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(24, 'GetCachedSelection', ((1, 'pvarSelectedChildren'),)))
    IUIAutomationLegacyIAccessiblePattern.get_CachedDefaultAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(25, 'get_CachedDefaultAction', ((1, 'pszDefaultAction'),)))
    IUIAutomationLegacyIAccessiblePattern.GetIAccessible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IAccessible_head), use_last_error=False)(26, 'GetIAccessible', ((1, 'ppAccessible'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationLegacyIAccessiblePattern
def _define_IUIAutomationItemContainerPattern_head():
    class IUIAutomationItemContainerPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('c690fdb2-27a8-423c-812d-429773c9084e')
    return IUIAutomationItemContainerPattern
def _define_IUIAutomationItemContainerPattern():
    IUIAutomationItemContainerPattern = win32more.UI.Accessibility.IUIAutomationItemContainerPattern_head
    IUIAutomationItemContainerPattern.FindItemByProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,Int32,win32more.System.Com.VARIANT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(3, 'FindItemByProperty', ((1, 'pStartAfter'),(1, 'propertyId'),(1, 'value'),(1, 'pFound'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationItemContainerPattern
def _define_IUIAutomationVirtualizedItemPattern_head():
    class IUIAutomationVirtualizedItemPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('6ba3d7a6-04cf-4f11-8793-a8d1cde9969f')
    return IUIAutomationVirtualizedItemPattern
def _define_IUIAutomationVirtualizedItemPattern():
    IUIAutomationVirtualizedItemPattern = win32more.UI.Accessibility.IUIAutomationVirtualizedItemPattern_head
    IUIAutomationVirtualizedItemPattern.Realize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Realize', ()))
    win32more.System.Com.IUnknown
    return IUIAutomationVirtualizedItemPattern
def _define_IUIAutomationAnnotationPattern_head():
    class IUIAutomationAnnotationPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('9a175b21-339e-41b1-8e8b-623f6b681098')
    return IUIAutomationAnnotationPattern
def _define_IUIAutomationAnnotationPattern():
    IUIAutomationAnnotationPattern = win32more.UI.Accessibility.IUIAutomationAnnotationPattern_head
    IUIAutomationAnnotationPattern.get_CurrentAnnotationTypeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'get_CurrentAnnotationTypeId', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CurrentAnnotationTypeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_CurrentAnnotationTypeName', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CurrentAuthor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'get_CurrentAuthor', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CurrentDateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'get_CurrentDateTime', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CurrentTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(7, 'get_CurrentTarget', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CachedAnnotationTypeId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_CachedAnnotationTypeId', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CachedAnnotationTypeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_CachedAnnotationTypeName', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CachedAuthor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_CachedAuthor', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CachedDateTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_CachedDateTime', ((1, 'retVal'),)))
    IUIAutomationAnnotationPattern.get_CachedTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(12, 'get_CachedTarget', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationAnnotationPattern
def _define_IUIAutomationStylesPattern_head():
    class IUIAutomationStylesPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('85b5f0a2-bd79-484a-ad2b-388c9838d5fb')
    return IUIAutomationStylesPattern
def _define_IUIAutomationStylesPattern():
    IUIAutomationStylesPattern = win32more.UI.Accessibility.IUIAutomationStylesPattern_head
    IUIAutomationStylesPattern.get_CurrentStyleId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'get_CurrentStyleId', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CurrentStyleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_CurrentStyleName', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CurrentFillColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(5, 'get_CurrentFillColor', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CurrentFillPatternStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'get_CurrentFillPatternStyle', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CurrentShape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_CurrentShape', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CurrentFillPatternColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'get_CurrentFillPatternColor', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CurrentExtendedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_CurrentExtendedProperties', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.GetCurrentExtendedPropertiesAsArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Accessibility.ExtendedProperty_head)),POINTER(Int32), use_last_error=False)(10, 'GetCurrentExtendedPropertiesAsArray', ((1, 'propertyArray'),(1, 'propertyCount'),)))
    IUIAutomationStylesPattern.get_CachedStyleId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_CachedStyleId', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CachedStyleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_CachedStyleName', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CachedFillColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_CachedFillColor', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CachedFillPatternStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_CachedFillPatternStyle', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CachedShape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_CachedShape', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CachedFillPatternColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'get_CachedFillPatternColor', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.get_CachedExtendedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'get_CachedExtendedProperties', ((1, 'retVal'),)))
    IUIAutomationStylesPattern.GetCachedExtendedPropertiesAsArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Accessibility.ExtendedProperty_head)),POINTER(Int32), use_last_error=False)(18, 'GetCachedExtendedPropertiesAsArray', ((1, 'propertyArray'),(1, 'propertyCount'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationStylesPattern
def _define_IUIAutomationSpreadsheetPattern_head():
    class IUIAutomationSpreadsheetPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('7517a7c8-faae-4de9-9f08-29b91e8595c1')
    return IUIAutomationSpreadsheetPattern
def _define_IUIAutomationSpreadsheetPattern():
    IUIAutomationSpreadsheetPattern = win32more.UI.Accessibility.IUIAutomationSpreadsheetPattern_head
    IUIAutomationSpreadsheetPattern.GetItemByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(3, 'GetItemByName', ((1, 'name'),(1, 'element'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationSpreadsheetPattern
def _define_IUIAutomationSpreadsheetItemPattern_head():
    class IUIAutomationSpreadsheetItemPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('7d4fb86c-8d34-40e1-8e83-62c15204e335')
    return IUIAutomationSpreadsheetItemPattern
def _define_IUIAutomationSpreadsheetItemPattern():
    IUIAutomationSpreadsheetItemPattern = win32more.UI.Accessibility.IUIAutomationSpreadsheetItemPattern_head
    IUIAutomationSpreadsheetItemPattern.get_CurrentFormula = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_CurrentFormula', ((1, 'retVal'),)))
    IUIAutomationSpreadsheetItemPattern.GetCurrentAnnotationObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(4, 'GetCurrentAnnotationObjects', ((1, 'retVal'),)))
    IUIAutomationSpreadsheetItemPattern.GetCurrentAnnotationTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(5, 'GetCurrentAnnotationTypes', ((1, 'retVal'),)))
    IUIAutomationSpreadsheetItemPattern.get_CachedFormula = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'get_CachedFormula', ((1, 'retVal'),)))
    IUIAutomationSpreadsheetItemPattern.GetCachedAnnotationObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(7, 'GetCachedAnnotationObjects', ((1, 'retVal'),)))
    IUIAutomationSpreadsheetItemPattern.GetCachedAnnotationTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(8, 'GetCachedAnnotationTypes', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationSpreadsheetItemPattern
def _define_IUIAutomationTransformPattern2_head():
    class IUIAutomationTransformPattern2(win32more.UI.Accessibility.IUIAutomationTransformPattern_head):
        Guid = Guid('6d74d017-6ecb-4381-b38b-3c17a48ff1c2')
    return IUIAutomationTransformPattern2
def _define_IUIAutomationTransformPattern2():
    IUIAutomationTransformPattern2 = win32more.UI.Accessibility.IUIAutomationTransformPattern2_head
    IUIAutomationTransformPattern2.Zoom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(12, 'Zoom', ((1, 'zoomValue'),)))
    IUIAutomationTransformPattern2.ZoomByUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.ZoomUnit, use_last_error=False)(13, 'ZoomByUnit', ((1, 'zoomUnit'),)))
    IUIAutomationTransformPattern2.get_CurrentCanZoom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(14, 'get_CurrentCanZoom', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CachedCanZoom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(15, 'get_CachedCanZoom', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CurrentZoomLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(16, 'get_CurrentZoomLevel', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CachedZoomLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(17, 'get_CachedZoomLevel', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CurrentZoomMinimum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(18, 'get_CurrentZoomMinimum', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CachedZoomMinimum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(19, 'get_CachedZoomMinimum', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CurrentZoomMaximum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(20, 'get_CurrentZoomMaximum', ((1, 'retVal'),)))
    IUIAutomationTransformPattern2.get_CachedZoomMaximum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(21, 'get_CachedZoomMaximum', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationTransformPattern
    return IUIAutomationTransformPattern2
def _define_IUIAutomationTextChildPattern_head():
    class IUIAutomationTextChildPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('6552b038-ae05-40c8-abfd-aa08352aab86')
    return IUIAutomationTextChildPattern
def _define_IUIAutomationTextChildPattern():
    IUIAutomationTextChildPattern = win32more.UI.Accessibility.IUIAutomationTextChildPattern_head
    IUIAutomationTextChildPattern.get_TextContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(3, 'get_TextContainer', ((1, 'container'),)))
    IUIAutomationTextChildPattern.get_TextRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTextRange_head), use_last_error=False)(4, 'get_TextRange', ((1, 'range'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationTextChildPattern
def _define_IUIAutomationDragPattern_head():
    class IUIAutomationDragPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dc7b570-1f54-4bad-bcda-d36a722fb7bd')
    return IUIAutomationDragPattern
def _define_IUIAutomationDragPattern():
    IUIAutomationDragPattern = win32more.UI.Accessibility.IUIAutomationDragPattern_head
    IUIAutomationDragPattern.get_CurrentIsGrabbed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'get_CurrentIsGrabbed', ((1, 'retVal'),)))
    IUIAutomationDragPattern.get_CachedIsGrabbed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'get_CachedIsGrabbed', ((1, 'retVal'),)))
    IUIAutomationDragPattern.get_CurrentDropEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'get_CurrentDropEffect', ((1, 'retVal'),)))
    IUIAutomationDragPattern.get_CachedDropEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'get_CachedDropEffect', ((1, 'retVal'),)))
    IUIAutomationDragPattern.get_CurrentDropEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(7, 'get_CurrentDropEffects', ((1, 'retVal'),)))
    IUIAutomationDragPattern.get_CachedDropEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(8, 'get_CachedDropEffects', ((1, 'retVal'),)))
    IUIAutomationDragPattern.GetCurrentGrabbedItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(9, 'GetCurrentGrabbedItems', ((1, 'retVal'),)))
    IUIAutomationDragPattern.GetCachedGrabbedItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(10, 'GetCachedGrabbedItems', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationDragPattern
def _define_IUIAutomationDropTargetPattern_head():
    class IUIAutomationDropTargetPattern(win32more.System.Com.IUnknown_head):
        Guid = Guid('69a095f7-eee4-430e-a46b-fb73b1ae39a5')
    return IUIAutomationDropTargetPattern
def _define_IUIAutomationDropTargetPattern():
    IUIAutomationDropTargetPattern = win32more.UI.Accessibility.IUIAutomationDropTargetPattern_head
    IUIAutomationDropTargetPattern.get_CurrentDropTargetEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_CurrentDropTargetEffect', ((1, 'retVal'),)))
    IUIAutomationDropTargetPattern.get_CachedDropTargetEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_CachedDropTargetEffect', ((1, 'retVal'),)))
    IUIAutomationDropTargetPattern.get_CurrentDropTargetEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(5, 'get_CurrentDropTargetEffects', ((1, 'retVal'),)))
    IUIAutomationDropTargetPattern.get_CachedDropTargetEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(6, 'get_CachedDropTargetEffects', ((1, 'retVal'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationDropTargetPattern
def _define_IUIAutomationElement2_head():
    class IUIAutomationElement2(win32more.UI.Accessibility.IUIAutomationElement_head):
        Guid = Guid('6749c683-f70d-4487-a698-5f79d55290d6')
    return IUIAutomationElement2
def _define_IUIAutomationElement2():
    IUIAutomationElement2 = win32more.UI.Accessibility.IUIAutomationElement2_head
    IUIAutomationElement2.get_CurrentOptimizeForVisualContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(85, 'get_CurrentOptimizeForVisualContent', ((1, 'retVal'),)))
    IUIAutomationElement2.get_CachedOptimizeForVisualContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(86, 'get_CachedOptimizeForVisualContent', ((1, 'retVal'),)))
    IUIAutomationElement2.get_CurrentLiveSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.LiveSetting), use_last_error=False)(87, 'get_CurrentLiveSetting', ((1, 'retVal'),)))
    IUIAutomationElement2.get_CachedLiveSetting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.LiveSetting), use_last_error=False)(88, 'get_CachedLiveSetting', ((1, 'retVal'),)))
    IUIAutomationElement2.get_CurrentFlowsFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(89, 'get_CurrentFlowsFrom', ((1, 'retVal'),)))
    IUIAutomationElement2.get_CachedFlowsFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(90, 'get_CachedFlowsFrom', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement
    return IUIAutomationElement2
def _define_IUIAutomationElement3_head():
    class IUIAutomationElement3(win32more.UI.Accessibility.IUIAutomationElement2_head):
        Guid = Guid('8471df34-aee0-4a01-a7de-7db9af12c296')
    return IUIAutomationElement3
def _define_IUIAutomationElement3():
    IUIAutomationElement3 = win32more.UI.Accessibility.IUIAutomationElement3_head
    IUIAutomationElement3.ShowContextMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(91, 'ShowContextMenu', ()))
    IUIAutomationElement3.get_CurrentIsPeripheral = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(92, 'get_CurrentIsPeripheral', ((1, 'retVal'),)))
    IUIAutomationElement3.get_CachedIsPeripheral = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(93, 'get_CachedIsPeripheral', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement2
    return IUIAutomationElement3
def _define_IUIAutomationElement4_head():
    class IUIAutomationElement4(win32more.UI.Accessibility.IUIAutomationElement3_head):
        Guid = Guid('3b6e233c-52fb-4063-a4c9-77c075c2a06b')
    return IUIAutomationElement4
def _define_IUIAutomationElement4():
    IUIAutomationElement4 = win32more.UI.Accessibility.IUIAutomationElement4_head
    IUIAutomationElement4.get_CurrentPositionInSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(94, 'get_CurrentPositionInSet', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CurrentSizeOfSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(95, 'get_CurrentSizeOfSet', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CurrentLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(96, 'get_CurrentLevel', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CurrentAnnotationTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(97, 'get_CurrentAnnotationTypes', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CurrentAnnotationObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(98, 'get_CurrentAnnotationObjects', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CachedPositionInSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(99, 'get_CachedPositionInSet', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CachedSizeOfSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(100, 'get_CachedSizeOfSet', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CachedLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(101, 'get_CachedLevel', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CachedAnnotationTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(102, 'get_CachedAnnotationTypes', ((1, 'retVal'),)))
    IUIAutomationElement4.get_CachedAnnotationObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(103, 'get_CachedAnnotationObjects', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement3
    return IUIAutomationElement4
def _define_IUIAutomationElement5_head():
    class IUIAutomationElement5(win32more.UI.Accessibility.IUIAutomationElement4_head):
        Guid = Guid('98141c1d-0d0e-4175-bbe2-6bff455842a7')
    return IUIAutomationElement5
def _define_IUIAutomationElement5():
    IUIAutomationElement5 = win32more.UI.Accessibility.IUIAutomationElement5_head
    IUIAutomationElement5.get_CurrentLandmarkType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(104, 'get_CurrentLandmarkType', ((1, 'retVal'),)))
    IUIAutomationElement5.get_CurrentLocalizedLandmarkType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(105, 'get_CurrentLocalizedLandmarkType', ((1, 'retVal'),)))
    IUIAutomationElement5.get_CachedLandmarkType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(106, 'get_CachedLandmarkType', ((1, 'retVal'),)))
    IUIAutomationElement5.get_CachedLocalizedLandmarkType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(107, 'get_CachedLocalizedLandmarkType', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement4
    return IUIAutomationElement5
def _define_IUIAutomationElement6_head():
    class IUIAutomationElement6(win32more.UI.Accessibility.IUIAutomationElement5_head):
        Guid = Guid('4780d450-8bca-4977-afa5-a4a517f555e3')
    return IUIAutomationElement6
def _define_IUIAutomationElement6():
    IUIAutomationElement6 = win32more.UI.Accessibility.IUIAutomationElement6_head
    IUIAutomationElement6.get_CurrentFullDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(108, 'get_CurrentFullDescription', ((1, 'retVal'),)))
    IUIAutomationElement6.get_CachedFullDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(109, 'get_CachedFullDescription', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement5
    return IUIAutomationElement6
def _define_IUIAutomationElement7_head():
    class IUIAutomationElement7(win32more.UI.Accessibility.IUIAutomationElement6_head):
        Guid = Guid('204e8572-cfc3-4c11-b0c8-7da7420750b7')
    return IUIAutomationElement7
def _define_IUIAutomationElement7():
    IUIAutomationElement7 = win32more.UI.Accessibility.IUIAutomationElement7_head
    IUIAutomationElement7.FindFirstWithOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.TreeTraversalOptions,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(110, 'FindFirstWithOptions', ((1, 'scope'),(1, 'condition'),(1, 'traversalOptions'),(1, 'root'),(1, 'found'),)))
    IUIAutomationElement7.FindAllWithOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.TreeTraversalOptions,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(111, 'FindAllWithOptions', ((1, 'scope'),(1, 'condition'),(1, 'traversalOptions'),(1, 'root'),(1, 'found'),)))
    IUIAutomationElement7.FindFirstWithOptionsBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.TreeTraversalOptions,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(112, 'FindFirstWithOptionsBuildCache', ((1, 'scope'),(1, 'condition'),(1, 'cacheRequest'),(1, 'traversalOptions'),(1, 'root'),(1, 'found'),)))
    IUIAutomationElement7.FindAllWithOptionsBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.TreeTraversalOptions,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.UI.Accessibility.IUIAutomationElementArray_head), use_last_error=False)(113, 'FindAllWithOptionsBuildCache', ((1, 'scope'),(1, 'condition'),(1, 'cacheRequest'),(1, 'traversalOptions'),(1, 'root'),(1, 'found'),)))
    IUIAutomationElement7.GetCurrentMetadataValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(114, 'GetCurrentMetadataValue', ((1, 'targetId'),(1, 'metadataId'),(1, 'returnVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement6
    return IUIAutomationElement7
def _define_IUIAutomationElement8_head():
    class IUIAutomationElement8(win32more.UI.Accessibility.IUIAutomationElement7_head):
        Guid = Guid('8c60217d-5411-4cde-bcc0-1ceda223830c')
    return IUIAutomationElement8
def _define_IUIAutomationElement8():
    IUIAutomationElement8 = win32more.UI.Accessibility.IUIAutomationElement8_head
    IUIAutomationElement8.get_CurrentHeadingLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(115, 'get_CurrentHeadingLevel', ((1, 'retVal'),)))
    IUIAutomationElement8.get_CachedHeadingLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(116, 'get_CachedHeadingLevel', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement7
    return IUIAutomationElement8
def _define_IUIAutomationElement9_head():
    class IUIAutomationElement9(win32more.UI.Accessibility.IUIAutomationElement8_head):
        Guid = Guid('39325fac-039d-440e-a3a3-5eb81a5cecc3')
    return IUIAutomationElement9
def _define_IUIAutomationElement9():
    IUIAutomationElement9 = win32more.UI.Accessibility.IUIAutomationElement9_head
    IUIAutomationElement9.get_CurrentIsDialog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(117, 'get_CurrentIsDialog', ((1, 'retVal'),)))
    IUIAutomationElement9.get_CachedIsDialog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(118, 'get_CachedIsDialog', ((1, 'retVal'),)))
    win32more.UI.Accessibility.IUIAutomationElement8
    return IUIAutomationElement9
def _define_IUIAutomationProxyFactory_head():
    class IUIAutomationProxyFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('85b94ecd-849d-42b6-b94d-d6db23fdf5a4')
    return IUIAutomationProxyFactory
def _define_IUIAutomationProxyFactory():
    IUIAutomationProxyFactory = win32more.UI.Accessibility.IUIAutomationProxyFactory_head
    IUIAutomationProxyFactory.CreateProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,Int32,Int32,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(3, 'CreateProvider', ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'provider'),)))
    IUIAutomationProxyFactory.get_ProxyFactoryId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_ProxyFactoryId', ((1, 'factoryId'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationProxyFactory
def _define_IUIAutomationProxyFactoryEntry_head():
    class IUIAutomationProxyFactoryEntry(win32more.System.Com.IUnknown_head):
        Guid = Guid('d50e472e-b64b-490c-bca1-d30696f9f289')
    return IUIAutomationProxyFactoryEntry
def _define_IUIAutomationProxyFactoryEntry():
    IUIAutomationProxyFactoryEntry = win32more.UI.Accessibility.IUIAutomationProxyFactoryEntry_head
    IUIAutomationProxyFactoryEntry.get_ProxyFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationProxyFactory_head), use_last_error=False)(3, 'get_ProxyFactory', ((1, 'factory'),)))
    IUIAutomationProxyFactoryEntry.get_ClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'get_ClassName', ((1, 'className'),)))
    IUIAutomationProxyFactoryEntry.get_ImageName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'get_ImageName', ((1, 'imageName'),)))
    IUIAutomationProxyFactoryEntry.get_AllowSubstringMatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'get_AllowSubstringMatch', ((1, 'allowSubstringMatch'),)))
    IUIAutomationProxyFactoryEntry.get_CanCheckBaseClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'get_CanCheckBaseClass', ((1, 'canCheckBaseClass'),)))
    IUIAutomationProxyFactoryEntry.get_NeedsAdviseEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'get_NeedsAdviseEvents', ((1, 'adviseEvents'),)))
    IUIAutomationProxyFactoryEntry.put_ClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(9, 'put_ClassName', ((1, 'className'),)))
    IUIAutomationProxyFactoryEntry.put_ImageName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(10, 'put_ImageName', ((1, 'imageName'),)))
    IUIAutomationProxyFactoryEntry.put_AllowSubstringMatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(11, 'put_AllowSubstringMatch', ((1, 'allowSubstringMatch'),)))
    IUIAutomationProxyFactoryEntry.put_CanCheckBaseClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(12, 'put_CanCheckBaseClass', ((1, 'canCheckBaseClass'),)))
    IUIAutomationProxyFactoryEntry.put_NeedsAdviseEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(13, 'put_NeedsAdviseEvents', ((1, 'adviseEvents'),)))
    IUIAutomationProxyFactoryEntry.SetWinEventsForAutomationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(14, 'SetWinEventsForAutomationEvent', ((1, 'eventId'),(1, 'propertyId'),(1, 'winEvents'),)))
    IUIAutomationProxyFactoryEntry.GetWinEventsForAutomationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(15, 'GetWinEventsForAutomationEvent', ((1, 'eventId'),(1, 'propertyId'),(1, 'winEvents'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationProxyFactoryEntry
def _define_IUIAutomationProxyFactoryMapping_head():
    class IUIAutomationProxyFactoryMapping(win32more.System.Com.IUnknown_head):
        Guid = Guid('09e31e18-872d-4873-93d1-1e541ec133fd')
    return IUIAutomationProxyFactoryMapping
def _define_IUIAutomationProxyFactoryMapping():
    IUIAutomationProxyFactoryMapping = win32more.UI.Accessibility.IUIAutomationProxyFactoryMapping_head
    IUIAutomationProxyFactoryMapping.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'get_Count', ((1, 'count'),)))
    IUIAutomationProxyFactoryMapping.GetTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(4, 'GetTable', ((1, 'table'),)))
    IUIAutomationProxyFactoryMapping.GetEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Accessibility.IUIAutomationProxyFactoryEntry_head), use_last_error=False)(5, 'GetEntry', ((1, 'index'),(1, 'entry'),)))
    IUIAutomationProxyFactoryMapping.SetTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(6, 'SetTable', ((1, 'factoryList'),)))
    IUIAutomationProxyFactoryMapping.InsertEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(7, 'InsertEntries', ((1, 'before'),(1, 'factoryList'),)))
    IUIAutomationProxyFactoryMapping.InsertEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.Accessibility.IUIAutomationProxyFactoryEntry_head, use_last_error=False)(8, 'InsertEntry', ((1, 'before'),(1, 'factory'),)))
    IUIAutomationProxyFactoryMapping.RemoveEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'RemoveEntry', ((1, 'index'),)))
    IUIAutomationProxyFactoryMapping.ClearTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'ClearTable', ()))
    IUIAutomationProxyFactoryMapping.RestoreDefaultTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'RestoreDefaultTable', ()))
    win32more.System.Com.IUnknown
    return IUIAutomationProxyFactoryMapping
def _define_IUIAutomationEventHandlerGroup_head():
    class IUIAutomationEventHandlerGroup(win32more.System.Com.IUnknown_head):
        Guid = Guid('c9ee12f2-c13b-4408-997c-639914377f4e')
    return IUIAutomationEventHandlerGroup
def _define_IUIAutomationEventHandlerGroup():
    IUIAutomationEventHandlerGroup = win32more.UI.Accessibility.IUIAutomationEventHandlerGroup_head
    IUIAutomationEventHandlerGroup.AddActiveTextPositionChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler_head, use_last_error=False)(3, 'AddActiveTextPositionChangedEventHandler', ((1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomationEventHandlerGroup.AddAutomationEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationEventHandler_head, use_last_error=False)(4, 'AddAutomationEventHandler', ((1, 'eventId'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomationEventHandlerGroup.AddChangesEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,POINTER(Int32),Int32,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationChangesEventHandler_head, use_last_error=False)(5, 'AddChangesEventHandler', ((1, 'scope'),(1, 'changeTypes'),(1, 'changesCount'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomationEventHandlerGroup.AddNotificationEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationNotificationEventHandler_head, use_last_error=False)(6, 'AddNotificationEventHandler', ((1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomationEventHandlerGroup.AddPropertyChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head,POINTER(Int32),Int32, use_last_error=False)(7, 'AddPropertyChangedEventHandler', ((1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),(1, 'propertyArray'),(1, 'propertyCount'),)))
    IUIAutomationEventHandlerGroup.AddStructureChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationStructureChangedEventHandler_head, use_last_error=False)(8, 'AddStructureChangedEventHandler', ((1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomationEventHandlerGroup.AddTextEditTextChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.TextEditChangeType,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler_head, use_last_error=False)(9, 'AddTextEditTextChangedEventHandler', ((1, 'scope'),(1, 'textEditChangeType'),(1, 'cacheRequest'),(1, 'handler'),)))
    win32more.System.Com.IUnknown
    return IUIAutomationEventHandlerGroup
def _define_IUIAutomation_head():
    class IUIAutomation(win32more.System.Com.IUnknown_head):
        Guid = Guid('30cbe57d-d9d0-452a-ab13-7ac5ac4825ee')
    return IUIAutomation
def _define_IUIAutomation():
    IUIAutomation = win32more.UI.Accessibility.IUIAutomation_head
    IUIAutomation.CompareElements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'CompareElements', ((1, 'el1'),(1, 'el2'),(1, 'areSame'),)))
    IUIAutomation.CompareRuntimeIds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'CompareRuntimeIds', ((1, 'runtimeId1'),(1, 'runtimeId2'),(1, 'areSame'),)))
    IUIAutomation.GetRootElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(5, 'GetRootElement', ((1, 'root'),)))
    IUIAutomation.ElementFromHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(6, 'ElementFromHandle', ((1, 'hwnd'),(1, 'element'),)))
    IUIAutomation.ElementFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(7, 'ElementFromPoint', ((1, 'pt'),(1, 'element'),)))
    IUIAutomation.GetFocusedElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(8, 'GetFocusedElement', ((1, 'element'),)))
    IUIAutomation.GetRootElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(9, 'GetRootElementBuildCache', ((1, 'cacheRequest'),(1, 'root'),)))
    IUIAutomation.ElementFromHandleBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(10, 'ElementFromHandleBuildCache', ((1, 'hwnd'),(1, 'cacheRequest'),(1, 'element'),)))
    IUIAutomation.ElementFromPointBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(11, 'ElementFromPointBuildCache', ((1, 'pt'),(1, 'cacheRequest'),(1, 'element'),)))
    IUIAutomation.GetFocusedElementBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(12, 'GetFocusedElementBuildCache', ((1, 'cacheRequest'),(1, 'element'),)))
    IUIAutomation.CreateTreeWalker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCondition_head,POINTER(win32more.UI.Accessibility.IUIAutomationTreeWalker_head), use_last_error=False)(13, 'CreateTreeWalker', ((1, 'pCondition'),(1, 'walker'),)))
    IUIAutomation.get_ControlViewWalker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTreeWalker_head), use_last_error=False)(14, 'get_ControlViewWalker', ((1, 'walker'),)))
    IUIAutomation.get_ContentViewWalker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTreeWalker_head), use_last_error=False)(15, 'get_ContentViewWalker', ((1, 'walker'),)))
    IUIAutomation.get_RawViewWalker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationTreeWalker_head), use_last_error=False)(16, 'get_RawViewWalker', ((1, 'walker'),)))
    IUIAutomation.get_RawViewCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(17, 'get_RawViewCondition', ((1, 'condition'),)))
    IUIAutomation.get_ControlViewCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(18, 'get_ControlViewCondition', ((1, 'condition'),)))
    IUIAutomation.get_ContentViewCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(19, 'get_ContentViewCondition', ((1, 'condition'),)))
    IUIAutomation.CreateCacheRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCacheRequest_head), use_last_error=False)(20, 'CreateCacheRequest', ((1, 'cacheRequest'),)))
    IUIAutomation.CreateTrueCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(21, 'CreateTrueCondition', ((1, 'newCondition'),)))
    IUIAutomation.CreateFalseCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(22, 'CreateFalseCondition', ((1, 'newCondition'),)))
    IUIAutomation.CreatePropertyCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(23, 'CreatePropertyCondition', ((1, 'propertyId'),(1, 'value'),(1, 'newCondition'),)))
    IUIAutomation.CreatePropertyConditionEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.VARIANT,win32more.UI.Accessibility.PropertyConditionFlags,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(24, 'CreatePropertyConditionEx', ((1, 'propertyId'),(1, 'value'),(1, 'flags'),(1, 'newCondition'),)))
    IUIAutomation.CreateAndCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.IUIAutomationCondition_head,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(25, 'CreateAndCondition', ((1, 'condition1'),(1, 'condition2'),(1, 'newCondition'),)))
    IUIAutomation.CreateAndConditionFromArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(26, 'CreateAndConditionFromArray', ((1, 'conditions'),(1, 'newCondition'),)))
    IUIAutomation.CreateAndConditionFromNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head),Int32,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(27, 'CreateAndConditionFromNativeArray', ((1, 'conditions'),(1, 'conditionCount'),(1, 'newCondition'),)))
    IUIAutomation.CreateOrCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCondition_head,win32more.UI.Accessibility.IUIAutomationCondition_head,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(28, 'CreateOrCondition', ((1, 'condition1'),(1, 'condition2'),(1, 'newCondition'),)))
    IUIAutomation.CreateOrConditionFromArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(29, 'CreateOrConditionFromArray', ((1, 'conditions'),(1, 'newCondition'),)))
    IUIAutomation.CreateOrConditionFromNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head),Int32,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(30, 'CreateOrConditionFromNativeArray', ((1, 'conditions'),(1, 'conditionCount'),(1, 'newCondition'),)))
    IUIAutomation.CreateNotCondition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCondition_head,POINTER(win32more.UI.Accessibility.IUIAutomationCondition_head), use_last_error=False)(31, 'CreateNotCondition', ((1, 'condition'),(1, 'newCondition'),)))
    IUIAutomation.AddAutomationEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationEventHandler_head, use_last_error=False)(32, 'AddAutomationEventHandler', ((1, 'eventId'),(1, 'element'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomation.RemoveAutomationEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationEventHandler_head, use_last_error=False)(33, 'RemoveAutomationEventHandler', ((1, 'eventId'),(1, 'element'),(1, 'handler'),)))
    IUIAutomation.AddPropertyChangedEventHandlerNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head,POINTER(Int32),Int32, use_last_error=False)(34, 'AddPropertyChangedEventHandlerNativeArray', ((1, 'element'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),(1, 'propertyArray'),(1, 'propertyCount'),)))
    IUIAutomation.AddPropertyChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(35, 'AddPropertyChangedEventHandler', ((1, 'element'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),(1, 'propertyArray'),)))
    IUIAutomation.RemovePropertyChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationPropertyChangedEventHandler_head, use_last_error=False)(36, 'RemovePropertyChangedEventHandler', ((1, 'element'),(1, 'handler'),)))
    IUIAutomation.AddStructureChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationStructureChangedEventHandler_head, use_last_error=False)(37, 'AddStructureChangedEventHandler', ((1, 'element'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomation.RemoveStructureChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationStructureChangedEventHandler_head, use_last_error=False)(38, 'RemoveStructureChangedEventHandler', ((1, 'element'),(1, 'handler'),)))
    IUIAutomation.AddFocusChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationFocusChangedEventHandler_head, use_last_error=False)(39, 'AddFocusChangedEventHandler', ((1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomation.RemoveFocusChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationFocusChangedEventHandler_head, use_last_error=False)(40, 'RemoveFocusChangedEventHandler', ((1, 'handler'),)))
    IUIAutomation.RemoveAllEventHandlers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(41, 'RemoveAllEventHandlers', ()))
    IUIAutomation.IntNativeArrayToSafeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),Int32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(42, 'IntNativeArrayToSafeArray', ((1, 'array'),(1, 'arrayCount'),(1, 'safeArray'),)))
    IUIAutomation.IntSafeArrayToNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(POINTER(Int32)),POINTER(Int32), use_last_error=False)(43, 'IntSafeArrayToNativeArray', ((1, 'intArray'),(1, 'array'),(1, 'arrayCount'),)))
    IUIAutomation.RectToVariant = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.RECT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(44, 'RectToVariant', ((1, 'rc'),(1, 'var'),)))
    IUIAutomation.VariantToRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(45, 'VariantToRect', ((1, 'var'),(1, 'rc'),)))
    IUIAutomation.SafeArrayToRectNativeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(POINTER(win32more.Foundation.RECT_head)),POINTER(Int32), use_last_error=False)(46, 'SafeArrayToRectNativeArray', ((1, 'rects'),(1, 'rectArray'),(1, 'rectArrayCount'),)))
    IUIAutomation.CreateProxyFactoryEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationProxyFactory_head,POINTER(win32more.UI.Accessibility.IUIAutomationProxyFactoryEntry_head), use_last_error=False)(47, 'CreateProxyFactoryEntry', ((1, 'factory'),(1, 'factoryEntry'),)))
    IUIAutomation.get_ProxyFactoryMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationProxyFactoryMapping_head), use_last_error=False)(48, 'get_ProxyFactoryMapping', ((1, 'factoryMapping'),)))
    IUIAutomation.GetPropertyProgrammaticName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(49, 'GetPropertyProgrammaticName', ((1, 'property'),(1, 'name'),)))
    IUIAutomation.GetPatternProgrammaticName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(50, 'GetPatternProgrammaticName', ((1, 'pattern'),(1, 'name'),)))
    IUIAutomation.PollForPotentialSupportedPatterns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(51, 'PollForPotentialSupportedPatterns', ((1, 'pElement'),(1, 'patternIds'),(1, 'patternNames'),)))
    IUIAutomation.PollForPotentialSupportedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(52, 'PollForPotentialSupportedProperties', ((1, 'pElement'),(1, 'propertyIds'),(1, 'propertyNames'),)))
    IUIAutomation.CheckNotSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(53, 'CheckNotSupported', ((1, 'value'),(1, 'isNotSupported'),)))
    IUIAutomation.get_ReservedNotSupportedValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(54, 'get_ReservedNotSupportedValue', ((1, 'notSupportedValue'),)))
    IUIAutomation.get_ReservedMixedAttributeValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(55, 'get_ReservedMixedAttributeValue', ((1, 'mixedAttributeValue'),)))
    IUIAutomation.ElementFromIAccessible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessible_head,Int32,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(56, 'ElementFromIAccessible', ((1, 'accessible'),(1, 'childId'),(1, 'element'),)))
    IUIAutomation.ElementFromIAccessibleBuildCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessible_head,Int32,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,POINTER(win32more.UI.Accessibility.IUIAutomationElement_head), use_last_error=False)(57, 'ElementFromIAccessibleBuildCache', ((1, 'accessible'),(1, 'childId'),(1, 'cacheRequest'),(1, 'element'),)))
    win32more.System.Com.IUnknown
    return IUIAutomation
def _define_IUIAutomation2_head():
    class IUIAutomation2(win32more.UI.Accessibility.IUIAutomation_head):
        Guid = Guid('34723aff-0c9d-49d0-9896-7ab52df8cd8a')
    return IUIAutomation2
def _define_IUIAutomation2():
    IUIAutomation2 = win32more.UI.Accessibility.IUIAutomation2_head
    IUIAutomation2.get_AutoSetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(58, 'get_AutoSetFocus', ((1, 'autoSetFocus'),)))
    IUIAutomation2.put_AutoSetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(59, 'put_AutoSetFocus', ((1, 'autoSetFocus'),)))
    IUIAutomation2.get_ConnectionTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(60, 'get_ConnectionTimeout', ((1, 'timeout'),)))
    IUIAutomation2.put_ConnectionTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(61, 'put_ConnectionTimeout', ((1, 'timeout'),)))
    IUIAutomation2.get_TransactionTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(62, 'get_TransactionTimeout', ((1, 'timeout'),)))
    IUIAutomation2.put_TransactionTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(63, 'put_TransactionTimeout', ((1, 'timeout'),)))
    win32more.UI.Accessibility.IUIAutomation
    return IUIAutomation2
def _define_IUIAutomation3_head():
    class IUIAutomation3(win32more.UI.Accessibility.IUIAutomation2_head):
        Guid = Guid('73d768da-9b51-4b89-936e-c209290973e7')
    return IUIAutomation3
def _define_IUIAutomation3():
    IUIAutomation3 = win32more.UI.Accessibility.IUIAutomation3_head
    IUIAutomation3.AddTextEditTextChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.TextEditChangeType,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler_head, use_last_error=False)(64, 'AddTextEditTextChangedEventHandler', ((1, 'element'),(1, 'scope'),(1, 'textEditChangeType'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomation3.RemoveTextEditTextChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationTextEditTextChangedEventHandler_head, use_last_error=False)(65, 'RemoveTextEditTextChangedEventHandler', ((1, 'element'),(1, 'handler'),)))
    win32more.UI.Accessibility.IUIAutomation2
    return IUIAutomation3
def _define_IUIAutomation4_head():
    class IUIAutomation4(win32more.UI.Accessibility.IUIAutomation3_head):
        Guid = Guid('1189c02a-05f8-4319-8e21-e817e3db2860')
    return IUIAutomation4
def _define_IUIAutomation4():
    IUIAutomation4 = win32more.UI.Accessibility.IUIAutomation4_head
    IUIAutomation4.AddChangesEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,POINTER(Int32),Int32,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationChangesEventHandler_head, use_last_error=False)(66, 'AddChangesEventHandler', ((1, 'element'),(1, 'scope'),(1, 'changeTypes'),(1, 'changesCount'),(1, 'pCacheRequest'),(1, 'handler'),)))
    IUIAutomation4.RemoveChangesEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationChangesEventHandler_head, use_last_error=False)(67, 'RemoveChangesEventHandler', ((1, 'element'),(1, 'handler'),)))
    win32more.UI.Accessibility.IUIAutomation3
    return IUIAutomation4
def _define_IUIAutomation5_head():
    class IUIAutomation5(win32more.UI.Accessibility.IUIAutomation4_head):
        Guid = Guid('25f700c8-d816-4057-a9dc-3cbdee77e256')
    return IUIAutomation5
def _define_IUIAutomation5():
    IUIAutomation5 = win32more.UI.Accessibility.IUIAutomation5_head
    IUIAutomation5.AddNotificationEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationNotificationEventHandler_head, use_last_error=False)(68, 'AddNotificationEventHandler', ((1, 'element'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomation5.RemoveNotificationEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationNotificationEventHandler_head, use_last_error=False)(69, 'RemoveNotificationEventHandler', ((1, 'element'),(1, 'handler'),)))
    win32more.UI.Accessibility.IUIAutomation4
    return IUIAutomation5
def _define_IUIAutomation6_head():
    class IUIAutomation6(win32more.UI.Accessibility.IUIAutomation5_head):
        Guid = Guid('aae072da-29e3-413d-87a7-192dbf81ed10')
    return IUIAutomation6
def _define_IUIAutomation6():
    IUIAutomation6 = win32more.UI.Accessibility.IUIAutomation6_head
    IUIAutomation6.CreateEventHandlerGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.IUIAutomationEventHandlerGroup_head), use_last_error=False)(70, 'CreateEventHandlerGroup', ((1, 'handlerGroup'),)))
    IUIAutomation6.AddEventHandlerGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationEventHandlerGroup_head, use_last_error=False)(71, 'AddEventHandlerGroup', ((1, 'element'),(1, 'handlerGroup'),)))
    IUIAutomation6.RemoveEventHandlerGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationEventHandlerGroup_head, use_last_error=False)(72, 'RemoveEventHandlerGroup', ((1, 'element'),(1, 'handlerGroup'),)))
    IUIAutomation6.get_ConnectionRecoveryBehavior = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.ConnectionRecoveryBehaviorOptions), use_last_error=False)(73, 'get_ConnectionRecoveryBehavior', ((1, 'connectionRecoveryBehaviorOptions'),)))
    IUIAutomation6.put_ConnectionRecoveryBehavior = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.ConnectionRecoveryBehaviorOptions, use_last_error=False)(74, 'put_ConnectionRecoveryBehavior', ((1, 'connectionRecoveryBehaviorOptions'),)))
    IUIAutomation6.get_CoalesceEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.CoalesceEventsOptions), use_last_error=False)(75, 'get_CoalesceEvents', ((1, 'coalesceEventsOptions'),)))
    IUIAutomation6.put_CoalesceEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.CoalesceEventsOptions, use_last_error=False)(76, 'put_CoalesceEvents', ((1, 'coalesceEventsOptions'),)))
    IUIAutomation6.AddActiveTextPositionChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.TreeScope,win32more.UI.Accessibility.IUIAutomationCacheRequest_head,win32more.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler_head, use_last_error=False)(77, 'AddActiveTextPositionChangedEventHandler', ((1, 'element'),(1, 'scope'),(1, 'cacheRequest'),(1, 'handler'),)))
    IUIAutomation6.RemoveActiveTextPositionChangedEventHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IUIAutomationElement_head,win32more.UI.Accessibility.IUIAutomationActiveTextPositionChangedEventHandler_head, use_last_error=False)(78, 'RemoveActiveTextPositionChangedEventHandler', ((1, 'element'),(1, 'handler'),)))
    win32more.UI.Accessibility.IUIAutomation5
    return IUIAutomation6
ConditionType = Int32
ConditionType_True = 0
ConditionType_False = 1
ConditionType_Property = 2
ConditionType_And = 3
ConditionType_Or = 4
ConditionType_Not = 5
def _define_UiaCondition_head():
    class UiaCondition(Structure):
        pass
    return UiaCondition
def _define_UiaCondition():
    UiaCondition = win32more.UI.Accessibility.UiaCondition_head
    UiaCondition._fields_ = [
        ("ConditionType", win32more.UI.Accessibility.ConditionType),
    ]
    return UiaCondition
def _define_UiaPropertyCondition_head():
    class UiaPropertyCondition(Structure):
        pass
    return UiaPropertyCondition
def _define_UiaPropertyCondition():
    UiaPropertyCondition = win32more.UI.Accessibility.UiaPropertyCondition_head
    UiaPropertyCondition._fields_ = [
        ("ConditionType", win32more.UI.Accessibility.ConditionType),
        ("PropertyId", Int32),
        ("Value", win32more.System.Com.VARIANT),
        ("Flags", win32more.UI.Accessibility.PropertyConditionFlags),
    ]
    return UiaPropertyCondition
def _define_UiaAndOrCondition_head():
    class UiaAndOrCondition(Structure):
        pass
    return UiaAndOrCondition
def _define_UiaAndOrCondition():
    UiaAndOrCondition = win32more.UI.Accessibility.UiaAndOrCondition_head
    UiaAndOrCondition._fields_ = [
        ("ConditionType", win32more.UI.Accessibility.ConditionType),
        ("ppConditions", POINTER(POINTER(win32more.UI.Accessibility.UiaCondition_head))),
        ("cConditions", Int32),
    ]
    return UiaAndOrCondition
def _define_UiaNotCondition_head():
    class UiaNotCondition(Structure):
        pass
    return UiaNotCondition
def _define_UiaNotCondition():
    UiaNotCondition = win32more.UI.Accessibility.UiaNotCondition_head
    UiaNotCondition._fields_ = [
        ("ConditionType", win32more.UI.Accessibility.ConditionType),
        ("pCondition", POINTER(win32more.UI.Accessibility.UiaCondition_head)),
    ]
    return UiaNotCondition
def _define_UiaCacheRequest_head():
    class UiaCacheRequest(Structure):
        pass
    return UiaCacheRequest
def _define_UiaCacheRequest():
    UiaCacheRequest = win32more.UI.Accessibility.UiaCacheRequest_head
    UiaCacheRequest._fields_ = [
        ("pViewCondition", POINTER(win32more.UI.Accessibility.UiaCondition_head)),
        ("Scope", win32more.UI.Accessibility.TreeScope),
        ("pProperties", POINTER(Int32)),
        ("cProperties", Int32),
        ("pPatterns", POINTER(Int32)),
        ("cPatterns", Int32),
        ("automationElementMode", win32more.UI.Accessibility.AutomationElementMode),
    ]
    return UiaCacheRequest
NormalizeState = Int32
NormalizeState_None = 0
NormalizeState_View = 1
NormalizeState_Custom = 2
def _define_UiaFindParams_head():
    class UiaFindParams(Structure):
        pass
    return UiaFindParams
def _define_UiaFindParams():
    UiaFindParams = win32more.UI.Accessibility.UiaFindParams_head
    UiaFindParams._fields_ = [
        ("MaxDepth", Int32),
        ("FindFirst", win32more.Foundation.BOOL),
        ("ExcludeRoot", win32more.Foundation.BOOL),
        ("pFindCondition", POINTER(win32more.UI.Accessibility.UiaCondition_head)),
    ]
    return UiaFindParams
ProviderType = Int32
ProviderType_BaseHwnd = 0
ProviderType_Proxy = 1
ProviderType_NonClientArea = 2
def _define_UiaProviderCallback():
    return CFUNCTYPE(POINTER(win32more.System.Com.SAFEARRAY_head),win32more.Foundation.HWND,win32more.UI.Accessibility.ProviderType, use_last_error=False)
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
AsyncContentLoadedState = Int32
AsyncContentLoadedState_Beginning = 0
AsyncContentLoadedState_Progress = 1
AsyncContentLoadedState_Completed = 2
def _define_UiaEventArgs_head():
    class UiaEventArgs(Structure):
        pass
    return UiaEventArgs
def _define_UiaEventArgs():
    UiaEventArgs = win32more.UI.Accessibility.UiaEventArgs_head
    UiaEventArgs._fields_ = [
        ("Type", win32more.UI.Accessibility.EventArgsType),
        ("EventId", Int32),
    ]
    return UiaEventArgs
def _define_UiaPropertyChangedEventArgs_head():
    class UiaPropertyChangedEventArgs(Structure):
        pass
    return UiaPropertyChangedEventArgs
def _define_UiaPropertyChangedEventArgs():
    UiaPropertyChangedEventArgs = win32more.UI.Accessibility.UiaPropertyChangedEventArgs_head
    UiaPropertyChangedEventArgs._fields_ = [
        ("Type", win32more.UI.Accessibility.EventArgsType),
        ("EventId", Int32),
        ("PropertyId", Int32),
        ("OldValue", win32more.System.Com.VARIANT),
        ("NewValue", win32more.System.Com.VARIANT),
    ]
    return UiaPropertyChangedEventArgs
def _define_UiaStructureChangedEventArgs_head():
    class UiaStructureChangedEventArgs(Structure):
        pass
    return UiaStructureChangedEventArgs
def _define_UiaStructureChangedEventArgs():
    UiaStructureChangedEventArgs = win32more.UI.Accessibility.UiaStructureChangedEventArgs_head
    UiaStructureChangedEventArgs._fields_ = [
        ("Type", win32more.UI.Accessibility.EventArgsType),
        ("EventId", Int32),
        ("StructureChangeType", win32more.UI.Accessibility.StructureChangeType),
        ("pRuntimeId", POINTER(Int32)),
        ("cRuntimeIdLen", Int32),
    ]
    return UiaStructureChangedEventArgs
def _define_UiaTextEditTextChangedEventArgs_head():
    class UiaTextEditTextChangedEventArgs(Structure):
        pass
    return UiaTextEditTextChangedEventArgs
def _define_UiaTextEditTextChangedEventArgs():
    UiaTextEditTextChangedEventArgs = win32more.UI.Accessibility.UiaTextEditTextChangedEventArgs_head
    UiaTextEditTextChangedEventArgs._fields_ = [
        ("Type", win32more.UI.Accessibility.EventArgsType),
        ("EventId", Int32),
        ("TextEditChangeType", win32more.UI.Accessibility.TextEditChangeType),
        ("pTextChange", POINTER(win32more.System.Com.SAFEARRAY_head)),
    ]
    return UiaTextEditTextChangedEventArgs
def _define_UiaChangesEventArgs_head():
    class UiaChangesEventArgs(Structure):
        pass
    return UiaChangesEventArgs
def _define_UiaChangesEventArgs():
    UiaChangesEventArgs = win32more.UI.Accessibility.UiaChangesEventArgs_head
    UiaChangesEventArgs._fields_ = [
        ("Type", win32more.UI.Accessibility.EventArgsType),
        ("EventId", Int32),
        ("EventIdCount", Int32),
        ("pUiaChanges", POINTER(win32more.UI.Accessibility.UiaChangeInfo_head)),
    ]
    return UiaChangesEventArgs
def _define_UiaAsyncContentLoadedEventArgs_head():
    class UiaAsyncContentLoadedEventArgs(Structure):
        pass
    return UiaAsyncContentLoadedEventArgs
def _define_UiaAsyncContentLoadedEventArgs():
    UiaAsyncContentLoadedEventArgs = win32more.UI.Accessibility.UiaAsyncContentLoadedEventArgs_head
    UiaAsyncContentLoadedEventArgs._fields_ = [
        ("Type", win32more.UI.Accessibility.EventArgsType),
        ("EventId", Int32),
        ("AsyncContentLoadedState", win32more.UI.Accessibility.AsyncContentLoadedState),
        ("PercentComplete", Double),
    ]
    return UiaAsyncContentLoadedEventArgs
def _define_UiaWindowClosedEventArgs_head():
    class UiaWindowClosedEventArgs(Structure):
        pass
    return UiaWindowClosedEventArgs
def _define_UiaWindowClosedEventArgs():
    UiaWindowClosedEventArgs = win32more.UI.Accessibility.UiaWindowClosedEventArgs_head
    UiaWindowClosedEventArgs._fields_ = [
        ("Type", win32more.UI.Accessibility.EventArgsType),
        ("EventId", Int32),
        ("pRuntimeId", POINTER(Int32)),
        ("cRuntimeIdLen", Int32),
    ]
    return UiaWindowClosedEventArgs
def _define_UiaEventCallback():
    return CFUNCTYPE(Void,POINTER(win32more.UI.Accessibility.UiaEventArgs_head),POINTER(win32more.System.Com.SAFEARRAY_head),win32more.Foundation.BSTR, use_last_error=False)
def _define_SERIALKEYSA_head():
    class SERIALKEYSA(Structure):
        pass
    return SERIALKEYSA
def _define_SERIALKEYSA():
    SERIALKEYSA = win32more.UI.Accessibility.SERIALKEYSA_head
    SERIALKEYSA._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", win32more.UI.Accessibility.SERIALKEYS_FLAGS),
        ("lpszActivePort", win32more.Foundation.PSTR),
        ("lpszPort", win32more.Foundation.PSTR),
        ("iBaudRate", UInt32),
        ("iPortState", UInt32),
        ("iActive", UInt32),
    ]
    return SERIALKEYSA
def _define_SERIALKEYSW_head():
    class SERIALKEYSW(Structure):
        pass
    return SERIALKEYSW
def _define_SERIALKEYSW():
    SERIALKEYSW = win32more.UI.Accessibility.SERIALKEYSW_head
    SERIALKEYSW._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", win32more.UI.Accessibility.SERIALKEYS_FLAGS),
        ("lpszActivePort", win32more.Foundation.PWSTR),
        ("lpszPort", win32more.Foundation.PWSTR),
        ("iBaudRate", UInt32),
        ("iPortState", UInt32),
        ("iActive", UInt32),
    ]
    return SERIALKEYSW
def _define_HIGHCONTRASTA_head():
    class HIGHCONTRASTA(Structure):
        pass
    return HIGHCONTRASTA
def _define_HIGHCONTRASTA():
    HIGHCONTRASTA = win32more.UI.Accessibility.HIGHCONTRASTA_head
    HIGHCONTRASTA._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", win32more.UI.Accessibility.HIGHCONTRASTW_FLAGS),
        ("lpszDefaultScheme", win32more.Foundation.PSTR),
    ]
    return HIGHCONTRASTA
def _define_HIGHCONTRASTW_head():
    class HIGHCONTRASTW(Structure):
        pass
    return HIGHCONTRASTW
def _define_HIGHCONTRASTW():
    HIGHCONTRASTW = win32more.UI.Accessibility.HIGHCONTRASTW_head
    HIGHCONTRASTW._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", win32more.UI.Accessibility.HIGHCONTRASTW_FLAGS),
        ("lpszDefaultScheme", win32more.Foundation.PWSTR),
    ]
    return HIGHCONTRASTW
def _define_FILTERKEYS_head():
    class FILTERKEYS(Structure):
        pass
    return FILTERKEYS
def _define_FILTERKEYS():
    FILTERKEYS = win32more.UI.Accessibility.FILTERKEYS_head
    FILTERKEYS._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", UInt32),
        ("iWaitMSec", UInt32),
        ("iDelayMSec", UInt32),
        ("iRepeatMSec", UInt32),
        ("iBounceMSec", UInt32),
    ]
    return FILTERKEYS
def _define_STICKYKEYS_head():
    class STICKYKEYS(Structure):
        pass
    return STICKYKEYS
def _define_STICKYKEYS():
    STICKYKEYS = win32more.UI.Accessibility.STICKYKEYS_head
    STICKYKEYS._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", win32more.UI.Accessibility.STICKYKEYS_FLAGS),
    ]
    return STICKYKEYS
def _define_MOUSEKEYS_head():
    class MOUSEKEYS(Structure):
        pass
    return MOUSEKEYS
def _define_MOUSEKEYS():
    MOUSEKEYS = win32more.UI.Accessibility.MOUSEKEYS_head
    MOUSEKEYS._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", UInt32),
        ("iMaxSpeed", UInt32),
        ("iTimeToMaxSpeed", UInt32),
        ("iCtrlSpeed", UInt32),
        ("dwReserved1", UInt32),
        ("dwReserved2", UInt32),
    ]
    return MOUSEKEYS
def _define_ACCESSTIMEOUT_head():
    class ACCESSTIMEOUT(Structure):
        pass
    return ACCESSTIMEOUT
def _define_ACCESSTIMEOUT():
    ACCESSTIMEOUT = win32more.UI.Accessibility.ACCESSTIMEOUT_head
    ACCESSTIMEOUT._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", UInt32),
        ("iTimeOutMSec", UInt32),
    ]
    return ACCESSTIMEOUT
def _define_SOUNDSENTRYA_head():
    class SOUNDSENTRYA(Structure):
        pass
    return SOUNDSENTRYA
def _define_SOUNDSENTRYA():
    SOUNDSENTRYA = win32more.UI.Accessibility.SOUNDSENTRYA_head
    SOUNDSENTRYA._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", win32more.UI.Accessibility.SOUNDSENTRY_FLAGS),
        ("iFSTextEffect", win32more.UI.Accessibility.SOUNDSENTRY_TEXT_EFFECT),
        ("iFSTextEffectMSec", UInt32),
        ("iFSTextEffectColorBits", UInt32),
        ("iFSGrafEffect", win32more.UI.Accessibility.SOUND_SENTRY_GRAPHICS_EFFECT),
        ("iFSGrafEffectMSec", UInt32),
        ("iFSGrafEffectColor", UInt32),
        ("iWindowsEffect", win32more.UI.Accessibility.SOUNDSENTRY_WINDOWS_EFFECT),
        ("iWindowsEffectMSec", UInt32),
        ("lpszWindowsEffectDLL", win32more.Foundation.PSTR),
        ("iWindowsEffectOrdinal", UInt32),
    ]
    return SOUNDSENTRYA
def _define_SOUNDSENTRYW_head():
    class SOUNDSENTRYW(Structure):
        pass
    return SOUNDSENTRYW
def _define_SOUNDSENTRYW():
    SOUNDSENTRYW = win32more.UI.Accessibility.SOUNDSENTRYW_head
    SOUNDSENTRYW._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", win32more.UI.Accessibility.SOUNDSENTRY_FLAGS),
        ("iFSTextEffect", win32more.UI.Accessibility.SOUNDSENTRY_TEXT_EFFECT),
        ("iFSTextEffectMSec", UInt32),
        ("iFSTextEffectColorBits", UInt32),
        ("iFSGrafEffect", win32more.UI.Accessibility.SOUND_SENTRY_GRAPHICS_EFFECT),
        ("iFSGrafEffectMSec", UInt32),
        ("iFSGrafEffectColor", UInt32),
        ("iWindowsEffect", win32more.UI.Accessibility.SOUNDSENTRY_WINDOWS_EFFECT),
        ("iWindowsEffectMSec", UInt32),
        ("lpszWindowsEffectDLL", win32more.Foundation.PWSTR),
        ("iWindowsEffectOrdinal", UInt32),
    ]
    return SOUNDSENTRYW
def _define_TOGGLEKEYS_head():
    class TOGGLEKEYS(Structure):
        pass
    return TOGGLEKEYS
def _define_TOGGLEKEYS():
    TOGGLEKEYS = win32more.UI.Accessibility.TOGGLEKEYS_head
    TOGGLEKEYS._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", UInt32),
    ]
    return TOGGLEKEYS
def _define_WINEVENTPROC():
    return CFUNCTYPE(Void,win32more.UI.Accessibility.HWINEVENTHOOK,UInt32,win32more.Foundation.HWND,Int32,Int32,UInt32,UInt32, use_last_error=False)
def _define_LresultFromObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.LRESULT,POINTER(Guid),win32more.Foundation.WPARAM,win32more.System.Com.IUnknown_head, use_last_error=False)(("LresultFromObject", windll["OLEACC"]), ((1, 'riid'),(1, 'wParam'),(1, 'punk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ObjectFromLresult():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LRESULT,POINTER(Guid),win32more.Foundation.WPARAM,POINTER(c_void_p), use_last_error=False)(("ObjectFromLresult", windll["OLEACC"]), ((1, 'lResult'),(1, 'riid'),(1, 'wParam'),(1, 'ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowFromAccessibleObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessible_head,POINTER(win32more.Foundation.HWND), use_last_error=False)(("WindowFromAccessibleObject", windll["OLEACC"]), ((1, 'param0'),(1, 'phwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessibleObjectFromWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("AccessibleObjectFromWindow", windll["OLEACC"]), ((1, 'hwnd'),(1, 'dwId'),(1, 'riid'),(1, 'ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessibleObjectFromEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,UInt32,POINTER(win32more.UI.Accessibility.IAccessible_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("AccessibleObjectFromEvent", windll["OLEACC"]), ((1, 'hwnd'),(1, 'dwId'),(1, 'dwChildId'),(1, 'ppacc'),(1, 'pvarChild'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessibleObjectFromPoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,POINTER(win32more.UI.Accessibility.IAccessible_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("AccessibleObjectFromPoint", windll["OLEACC"]), ((1, 'ptScreen'),(1, 'ppacc'),(1, 'pvarChild'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccessibleChildren():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessible_head,Int32,Int32,POINTER(win32more.System.Com.VARIANT),POINTER(Int32), use_last_error=False)(("AccessibleChildren", windll["OLEACC"]), ((1, 'paccContainer'),(1, 'iChildStart'),(1, 'cChildren'),(1, 'rgvarChildren'),(1, 'pcObtained'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRoleTextA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Byte),UInt32, use_last_error=True)(("GetRoleTextA", windll["OLEACC"]), ((1, 'lRole'),(1, 'lpszRole'),(1, 'cchRoleMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRoleTextW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Char),UInt32, use_last_error=True)(("GetRoleTextW", windll["OLEACC"]), ((1, 'lRole'),(1, 'lpszRole'),(1, 'cchRoleMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRoleText():
    return win32more.UI.Accessibility.GetRoleTextW
def _define_GetStateTextA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Byte),UInt32, use_last_error=True)(("GetStateTextA", windll["OLEACC"]), ((1, 'lStateBit'),(1, 'lpszState'),(1, 'cchState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStateTextW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(Char),UInt32, use_last_error=True)(("GetStateTextW", windll["OLEACC"]), ((1, 'lStateBit'),(1, 'lpszState'),(1, 'cchState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStateText():
    return win32more.UI.Accessibility.GetStateTextW
def _define_GetOleaccVersionInfo():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("GetOleaccVersionInfo", windll["OLEACC"]), ((1, 'pVer'),(1, 'pBuild'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateStdAccessibleObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,Int32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("CreateStdAccessibleObject", windll["OLEACC"]), ((1, 'hwnd'),(1, 'idObject'),(1, 'riid'),(1, 'ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateStdAccessibleProxyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PSTR,Int32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("CreateStdAccessibleProxyA", windll["OLEACC"]), ((1, 'hwnd'),(1, 'pClassName'),(1, 'idObject'),(1, 'riid'),(1, 'ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateStdAccessibleProxyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,Int32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("CreateStdAccessibleProxyW", windll["OLEACC"]), ((1, 'hwnd'),(1, 'pClassName'),(1, 'idObject'),(1, 'riid'),(1, 'ppvObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateStdAccessibleProxy():
    return win32more.UI.Accessibility.CreateStdAccessibleProxyW
def _define_AccSetRunningUtilityState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.UI.Accessibility.ACC_UTILITY_STATE_FLAGS, use_last_error=False)(("AccSetRunningUtilityState", windll["OLEACC"]), ((1, 'hwndApp'),(1, 'dwUtilityStateMask'),(1, 'dwUtilityState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AccNotifyTouchInteraction():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.HWND,win32more.Foundation.POINT, use_last_error=False)(("AccNotifyTouchInteraction", windll["OLEACC"]), ((1, 'hwndApp'),(1, 'hwndTarget'),(1, 'ptTarget'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetErrorDescription():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("UiaGetErrorDescription", windll["UIAutomationCore"]), ((1, 'pDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaHUiaNodeFromVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.UI.Accessibility.HUIANODE), use_last_error=False)(("UiaHUiaNodeFromVariant", windll["UIAutomationCore"]), ((1, 'pvar'),(1, 'phnode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaHPatternObjectFromVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.UI.Accessibility.HUIAPATTERNOBJECT), use_last_error=False)(("UiaHPatternObjectFromVariant", windll["UIAutomationCore"]), ((1, 'pvar'),(1, 'phobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaHTextRangeFromVariant():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.UI.Accessibility.HUIATEXTRANGE), use_last_error=False)(("UiaHTextRangeFromVariant", windll["UIAutomationCore"]), ((1, 'pvar'),(1, 'phtextrange'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaNodeRelease():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Accessibility.HUIANODE, use_last_error=False)(("UiaNodeRelease", windll["UIAutomationCore"]), ((1, 'hnode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetPropertyValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("UiaGetPropertyValue", windll["UIAutomationCore"]), ((1, 'hnode'),(1, 'propertyId'),(1, 'pValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetPatternProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,Int32,POINTER(win32more.UI.Accessibility.HUIAPATTERNOBJECT), use_last_error=False)(("UiaGetPatternProvider", windll["UIAutomationCore"]), ((1, 'hnode'),(1, 'patternId'),(1, 'phobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetRuntimeId():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("UiaGetRuntimeId", windll["UIAutomationCore"]), ((1, 'hnode'),(1, 'pruntimeId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaSetFocus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE, use_last_error=False)(("UiaSetFocus", windll["UIAutomationCore"]), ((1, 'hnode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaNavigate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,win32more.UI.Accessibility.NavigateDirection,POINTER(win32more.UI.Accessibility.UiaCondition_head),POINTER(win32more.UI.Accessibility.UiaCacheRequest_head),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(win32more.Foundation.BSTR), use_last_error=False)(("UiaNavigate", windll["UIAutomationCore"]), ((1, 'hnode'),(1, 'direction'),(1, 'pCondition'),(1, 'pRequest'),(1, 'ppRequestedData'),(1, 'ppTreeStructure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetUpdatedCache():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,POINTER(win32more.UI.Accessibility.UiaCacheRequest_head),win32more.UI.Accessibility.NormalizeState,POINTER(win32more.UI.Accessibility.UiaCondition_head),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(win32more.Foundation.BSTR), use_last_error=False)(("UiaGetUpdatedCache", windll["UIAutomationCore"]), ((1, 'hnode'),(1, 'pRequest'),(1, 'normalizeState'),(1, 'pNormalizeCondition'),(1, 'ppRequestedData'),(1, 'ppTreeStructure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaFind():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,POINTER(win32more.UI.Accessibility.UiaFindParams_head),POINTER(win32more.UI.Accessibility.UiaCacheRequest_head),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("UiaFind", windll["UIAutomationCore"]), ((1, 'hnode'),(1, 'pParams'),(1, 'pRequest'),(1, 'ppRequestedData'),(1, 'ppOffsets'),(1, 'ppTreeStructures'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaNodeFromPoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,POINTER(win32more.UI.Accessibility.UiaCacheRequest_head),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(win32more.Foundation.BSTR), use_last_error=False)(("UiaNodeFromPoint", windll["UIAutomationCore"]), ((1, 'x'),(1, 'y'),(1, 'pRequest'),(1, 'ppRequestedData'),(1, 'ppTreeStructure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaNodeFromFocus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.UiaCacheRequest_head),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(win32more.Foundation.BSTR), use_last_error=False)(("UiaNodeFromFocus", windll["UIAutomationCore"]), ((1, 'pRequest'),(1, 'ppRequestedData'),(1, 'ppTreeStructure'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaNodeFromHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.UI.Accessibility.HUIANODE), use_last_error=False)(("UiaNodeFromHandle", windll["UIAutomationCore"]), ((1, 'hwnd'),(1, 'phnode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaNodeFromProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,POINTER(win32more.UI.Accessibility.HUIANODE), use_last_error=False)(("UiaNodeFromProvider", windll["UIAutomationCore"]), ((1, 'pProvider'),(1, 'phnode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetRootNode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Accessibility.HUIANODE), use_last_error=False)(("UiaGetRootNode", windll["UIAutomationCore"]), ((1, 'phnode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRegisterProviderCallback():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.UI.Accessibility.UiaProviderCallback), use_last_error=False)(("UiaRegisterProviderCallback", windll["UIAutomationCore"]), ((1, 'pCallback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaLookupId():
    try:
        return WINFUNCTYPE(Int32,win32more.UI.Accessibility.AutomationIdentifierType,POINTER(Guid), use_last_error=False)(("UiaLookupId", windll["UIAutomationCore"]), ((1, 'type'),(1, 'pGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetReservedNotSupportedValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(("UiaGetReservedNotSupportedValue", windll["UIAutomationCore"]), ((1, 'punkNotSupportedValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaGetReservedMixedAttributeValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(("UiaGetReservedMixedAttributeValue", windll["UIAutomationCore"]), ((1, 'punkMixedAttributeValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaClientsAreListening():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(("UiaClientsAreListening", windll["UIAutomationCore"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseAutomationPropertyChangedEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,Int32,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT, use_last_error=False)(("UiaRaiseAutomationPropertyChangedEvent", windll["UIAutomationCore"]), ((1, 'pProvider'),(1, 'id'),(1, 'oldValue'),(1, 'newValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseAutomationEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,Int32, use_last_error=False)(("UiaRaiseAutomationEvent", windll["UIAutomationCore"]), ((1, 'pProvider'),(1, 'id'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseStructureChangedEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.StructureChangeType,POINTER(Int32),Int32, use_last_error=False)(("UiaRaiseStructureChangedEvent", windll["UIAutomationCore"]), ((1, 'pProvider'),(1, 'structureChangeType'),(1, 'pRuntimeId'),(1, 'cRuntimeIdLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseAsyncContentLoadedEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.AsyncContentLoadedState,Double, use_last_error=False)(("UiaRaiseAsyncContentLoadedEvent", windll["UIAutomationCore"]), ((1, 'pProvider'),(1, 'asyncContentLoadedState'),(1, 'percentComplete'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseTextEditTextChangedEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.TextEditChangeType,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(("UiaRaiseTextEditTextChangedEvent", windll["UIAutomationCore"]), ((1, 'pProvider'),(1, 'textEditChangeType'),(1, 'pChangedData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseChangesEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,Int32,POINTER(win32more.UI.Accessibility.UiaChangeInfo_head), use_last_error=False)(("UiaRaiseChangesEvent", windll["UIAutomationCore"]), ((1, 'pProvider'),(1, 'eventIdCount'),(1, 'pUiaChanges'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseNotificationEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.NotificationKind,win32more.UI.Accessibility.NotificationProcessing,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(("UiaRaiseNotificationEvent", windll["UIAutomationCore"]), ((1, 'provider'),(1, 'notificationKind'),(1, 'notificationProcessing'),(1, 'displayString'),(1, 'activityId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRaiseActiveTextPositionChangedEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,win32more.UI.Accessibility.ITextRangeProvider_head, use_last_error=False)(("UiaRaiseActiveTextPositionChangedEvent", windll["UIAutomationCore"]), ((1, 'provider'),(1, 'textRange'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaAddEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIANODE,Int32,POINTER(win32more.UI.Accessibility.UiaEventCallback),win32more.UI.Accessibility.TreeScope,POINTER(Int32),Int32,POINTER(win32more.UI.Accessibility.UiaCacheRequest_head),POINTER(win32more.UI.Accessibility.HUIAEVENT), use_last_error=False)(("UiaAddEvent", windll["UIAutomationCore"]), ((1, 'hnode'),(1, 'eventId'),(1, 'pCallback'),(1, 'scope'),(1, 'pProperties'),(1, 'cProperties'),(1, 'pRequest'),(1, 'phEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaRemoveEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAEVENT, use_last_error=False)(("UiaRemoveEvent", windll["UIAutomationCore"]), ((1, 'hEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaEventAddWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAEVENT,win32more.Foundation.HWND, use_last_error=False)(("UiaEventAddWindow", windll["UIAutomationCore"]), ((1, 'hEvent'),(1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaEventRemoveWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAEVENT,win32more.Foundation.HWND, use_last_error=False)(("UiaEventRemoveWindow", windll["UIAutomationCore"]), ((1, 'hEvent'),(1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DockPattern_SetDockPosition():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.DockPosition, use_last_error=False)(("DockPattern_SetDockPosition", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'dockPosition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExpandCollapsePattern_Collapse():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT, use_last_error=False)(("ExpandCollapsePattern_Collapse", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExpandCollapsePattern_Expand():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT, use_last_error=False)(("ExpandCollapsePattern_Expand", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GridPattern_GetItem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Int32,Int32,POINTER(win32more.UI.Accessibility.HUIANODE), use_last_error=False)(("GridPattern_GetItem", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'row'),(1, 'column'),(1, 'pResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InvokePattern_Invoke():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT, use_last_error=False)(("InvokePattern_Invoke", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MultipleViewPattern_GetViewName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("MultipleViewPattern_GetViewName", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'viewId'),(1, 'ppStr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MultipleViewPattern_SetCurrentView():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Int32, use_last_error=False)(("MultipleViewPattern_SetCurrentView", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'viewId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RangeValuePattern_SetValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Double, use_last_error=False)(("RangeValuePattern_SetValue", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'val'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScrollItemPattern_ScrollIntoView():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT, use_last_error=False)(("ScrollItemPattern_ScrollIntoView", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScrollPattern_Scroll():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.ScrollAmount,win32more.UI.Accessibility.ScrollAmount, use_last_error=False)(("ScrollPattern_Scroll", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'horizontalAmount'),(1, 'verticalAmount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScrollPattern_SetScrollPercent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Double,Double, use_last_error=False)(("ScrollPattern_SetScrollPercent", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'horizontalPercent'),(1, 'verticalPercent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SelectionItemPattern_AddToSelection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT, use_last_error=False)(("SelectionItemPattern_AddToSelection", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SelectionItemPattern_RemoveFromSelection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT, use_last_error=False)(("SelectionItemPattern_RemoveFromSelection", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SelectionItemPattern_Select():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT, use_last_error=False)(("SelectionItemPattern_Select", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TogglePattern_Toggle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT, use_last_error=False)(("TogglePattern_Toggle", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TransformPattern_Move():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Double,Double, use_last_error=False)(("TransformPattern_Move", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TransformPattern_Resize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Double,Double, use_last_error=False)(("TransformPattern_Resize", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'width'),(1, 'height'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TransformPattern_Rotate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Double, use_last_error=False)(("TransformPattern_Rotate", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'degrees'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ValuePattern_SetValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.Foundation.PWSTR, use_last_error=False)(("ValuePattern_SetValue", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'pVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowPattern_Close():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT, use_last_error=False)(("WindowPattern_Close", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowPattern_SetWindowVisualState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.WindowVisualState, use_last_error=False)(("WindowPattern_SetWindowVisualState", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'state'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowPattern_WaitForInputIdle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Int32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("WindowPattern_WaitForInputIdle", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'milliseconds'),(1, 'pResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextPattern_GetSelection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("TextPattern_GetSelection", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextPattern_GetVisibleRanges():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("TextPattern_GetVisibleRanges", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextPattern_RangeFromChild():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.HUIANODE,POINTER(win32more.UI.Accessibility.HUIATEXTRANGE), use_last_error=False)(("TextPattern_RangeFromChild", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'hnodeChild'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextPattern_RangeFromPoint():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.UiaPoint,POINTER(win32more.UI.Accessibility.HUIATEXTRANGE), use_last_error=False)(("TextPattern_RangeFromPoint", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'point'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextPattern_get_DocumentRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,POINTER(win32more.UI.Accessibility.HUIATEXTRANGE), use_last_error=False)(("TextPattern_get_DocumentRange", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextPattern_get_SupportedTextSelection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,POINTER(win32more.UI.Accessibility.SupportedTextSelection), use_last_error=False)(("TextPattern_get_SupportedTextSelection", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_Clone():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,POINTER(win32more.UI.Accessibility.HUIATEXTRANGE), use_last_error=False)(("TextRange_Clone", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_Compare():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.HUIATEXTRANGE,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("TextRange_Compare", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'range'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_CompareEndpoints():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextPatternRangeEndpoint,POINTER(Int32), use_last_error=False)(("TextRange_CompareEndpoints", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'endpoint'),(1, 'targetRange'),(1, 'targetEndpoint'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_ExpandToEnclosingUnit():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextUnit, use_last_error=False)(("TextRange_ExpandToEnclosingUnit", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'unit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_GetAttributeValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("TextRange_GetAttributeValue", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'attributeId'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_FindAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,Int32,win32more.System.Com.VARIANT,win32more.Foundation.BOOL,POINTER(win32more.UI.Accessibility.HUIATEXTRANGE), use_last_error=False)(("TextRange_FindAttribute", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'attributeId'),(1, 'val'),(1, 'backward'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_FindText():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.Foundation.BSTR,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(win32more.UI.Accessibility.HUIATEXTRANGE), use_last_error=False)(("TextRange_FindText", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'text'),(1, 'backward'),(1, 'ignoreCase'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_GetBoundingRectangles():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("TextRange_GetBoundingRectangles", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_GetEnclosingElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,POINTER(win32more.UI.Accessibility.HUIANODE), use_last_error=False)(("TextRange_GetEnclosingElement", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_GetText():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("TextRange_GetText", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'maxLength'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_Move():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextUnit,Int32,POINTER(Int32), use_last_error=False)(("TextRange_Move", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'unit'),(1, 'count'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_MoveEndpointByUnit():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.TextUnit,Int32,POINTER(Int32), use_last_error=False)(("TextRange_MoveEndpointByUnit", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'endpoint'),(1, 'unit'),(1, 'count'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_MoveEndpointByRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextPatternRangeEndpoint,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.UI.Accessibility.TextPatternRangeEndpoint, use_last_error=False)(("TextRange_MoveEndpointByRange", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'endpoint'),(1, 'targetRange'),(1, 'targetEndpoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_Select():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE, use_last_error=False)(("TextRange_Select", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_AddToSelection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE, use_last_error=False)(("TextRange_AddToSelection", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_RemoveFromSelection():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE, use_last_error=False)(("TextRange_RemoveFromSelection", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_ScrollIntoView():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,win32more.Foundation.BOOL, use_last_error=False)(("TextRange_ScrollIntoView", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'alignToTop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextRange_GetChildren():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIATEXTRANGE,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("TextRange_GetChildren", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'pRetVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ItemContainerPattern_FindItemByProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.HUIANODE,Int32,win32more.System.Com.VARIANT,POINTER(win32more.UI.Accessibility.HUIANODE), use_last_error=False)(("ItemContainerPattern_FindItemByProperty", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'hnodeStartAfter'),(1, 'propertyId'),(1, 'value'),(1, 'pFound'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LegacyIAccessiblePattern_Select():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,Int32, use_last_error=False)(("LegacyIAccessiblePattern_Select", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'flagsSelect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LegacyIAccessiblePattern_DoDefaultAction():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT, use_last_error=False)(("LegacyIAccessiblePattern_DoDefaultAction", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LegacyIAccessiblePattern_SetValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.Foundation.PWSTR, use_last_error=False)(("LegacyIAccessiblePattern_SetValue", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'szValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LegacyIAccessiblePattern_GetIAccessible():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,POINTER(win32more.UI.Accessibility.IAccessible_head), use_last_error=False)(("LegacyIAccessiblePattern_GetIAccessible", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'pAccessible'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SynchronizedInputPattern_StartListening():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT,win32more.UI.Accessibility.SynchronizedInputType, use_last_error=False)(("SynchronizedInputPattern_StartListening", windll["UIAutomationCore"]), ((1, 'hobj'),(1, 'inputType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SynchronizedInputPattern_Cancel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT, use_last_error=False)(("SynchronizedInputPattern_Cancel", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualizedItemPattern_Realize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.HUIAPATTERNOBJECT, use_last_error=False)(("VirtualizedItemPattern_Realize", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaPatternRelease():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Accessibility.HUIAPATTERNOBJECT, use_last_error=False)(("UiaPatternRelease", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaTextRangeRelease():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Accessibility.HUIATEXTRANGE, use_last_error=False)(("UiaTextRangeRelease", windll["UIAutomationCore"]), ((1, 'hobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaReturnRawElementProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.LRESULT,win32more.Foundation.HWND,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,win32more.UI.Accessibility.IRawElementProviderSimple_head, use_last_error=False)(("UiaReturnRawElementProvider", windll["UIAutomationCore"]), ((1, 'hwnd'),(1, 'wParam'),(1, 'lParam'),(1, 'el'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaHostProviderFromHwnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(("UiaHostProviderFromHwnd", windll["UIAutomationCore"]), ((1, 'hwnd'),(1, 'ppProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaProviderForNonClient():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,Int32,Int32,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(("UiaProviderForNonClient", windll["UIAutomationCore"]), ((1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),(1, 'ppProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaIAccessibleFromProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head,UInt32,POINTER(win32more.UI.Accessibility.IAccessible_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("UiaIAccessibleFromProvider", windll["UIAutomationCore"]), ((1, 'pProvider'),(1, 'dwFlags'),(1, 'ppAccessible'),(1, 'pvarChild'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaProviderFromIAccessible():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IAccessible_head,Int32,UInt32,POINTER(win32more.UI.Accessibility.IRawElementProviderSimple_head), use_last_error=False)(("UiaProviderFromIAccessible", windll["UIAutomationCore"]), ((1, 'pAccessible'),(1, 'idChild'),(1, 'dwFlags'),(1, 'ppProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaDisconnectAllProviders():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("UiaDisconnectAllProviders", windll["UIAutomationCore"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaDisconnectProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Accessibility.IRawElementProviderSimple_head, use_last_error=False)(("UiaDisconnectProvider", windll["UIAutomationCore"]), ((1, 'pProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UiaHasServerSideProvider():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND, use_last_error=False)(("UiaHasServerSideProvider", windll["UIAutomationCore"]), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterPointerInputTarget():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE, use_last_error=True)(("RegisterPointerInputTarget", windll["USER32"]), ((1, 'hwnd'),(1, 'pointerType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterPointerInputTarget():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE, use_last_error=True)(("UnregisterPointerInputTarget", windll["USER32"]), ((1, 'hwnd'),(1, 'pointerType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterPointerInputTargetEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE,win32more.Foundation.BOOL, use_last_error=False)(("RegisterPointerInputTargetEx", windll["USER32"]), ((1, 'hwnd'),(1, 'pointerType'),(1, 'fObserve'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterPointerInputTargetEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.UI.WindowsAndMessaging.POINTER_INPUT_TYPE, use_last_error=False)(("UnregisterPointerInputTargetEx", windll["USER32"]), ((1, 'hwnd'),(1, 'pointerType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NotifyWinEvent():
    try:
        return WINFUNCTYPE(Void,UInt32,win32more.Foundation.HWND,Int32,Int32, use_last_error=False)(("NotifyWinEvent", windll["USER32"]), ((1, 'event'),(1, 'hwnd'),(1, 'idObject'),(1, 'idChild'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetWinEventHook():
    try:
        return WINFUNCTYPE(win32more.UI.Accessibility.HWINEVENTHOOK,UInt32,UInt32,win32more.Foundation.HINSTANCE,win32more.UI.Accessibility.WINEVENTPROC,UInt32,UInt32,UInt32, use_last_error=False)(("SetWinEventHook", windll["USER32"]), ((1, 'eventMin'),(1, 'eventMax'),(1, 'hmodWinEventProc'),(1, 'pfnWinEventProc'),(1, 'idProcess'),(1, 'idThread'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsWinEventHookInstalled():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=False)(("IsWinEventHookInstalled", windll["USER32"]), ((1, 'event'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnhookWinEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.Accessibility.HWINEVENTHOOK, use_last_error=False)(("UnhookWinEvent", windll["USER32"]), ((1, 'hWinEventHook'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "LIBID_Accessibility",
    "CLSID_AccPropServices",
    "IIS_IsOleaccProxy",
    "IIS_ControlAccessible",
    "ANRUS_PRIORITY_AUDIO_DYNAMIC_DUCK",
    "MSAA_MENU_SIG",
    "PROPID_ACC_NAME",
    "PROPID_ACC_VALUE",
    "PROPID_ACC_DESCRIPTION",
    "PROPID_ACC_ROLE",
    "PROPID_ACC_STATE",
    "PROPID_ACC_HELP",
    "PROPID_ACC_KEYBOARDSHORTCUT",
    "PROPID_ACC_DEFAULTACTION",
    "PROPID_ACC_HELPTOPIC",
    "PROPID_ACC_FOCUS",
    "PROPID_ACC_SELECTION",
    "PROPID_ACC_PARENT",
    "PROPID_ACC_NAV_UP",
    "PROPID_ACC_NAV_DOWN",
    "PROPID_ACC_NAV_LEFT",
    "PROPID_ACC_NAV_RIGHT",
    "PROPID_ACC_NAV_PREV",
    "PROPID_ACC_NAV_NEXT",
    "PROPID_ACC_NAV_FIRSTCHILD",
    "PROPID_ACC_NAV_LASTCHILD",
    "PROPID_ACC_ROLEMAP",
    "PROPID_ACC_VALUEMAP",
    "PROPID_ACC_STATEMAP",
    "PROPID_ACC_DESCRIPTIONMAP",
    "PROPID_ACC_DODEFAULTACTION",
    "DISPID_ACC_PARENT",
    "DISPID_ACC_CHILDCOUNT",
    "DISPID_ACC_CHILD",
    "DISPID_ACC_NAME",
    "DISPID_ACC_VALUE",
    "DISPID_ACC_DESCRIPTION",
    "DISPID_ACC_ROLE",
    "DISPID_ACC_STATE",
    "DISPID_ACC_HELP",
    "DISPID_ACC_HELPTOPIC",
    "DISPID_ACC_KEYBOARDSHORTCUT",
    "DISPID_ACC_FOCUS",
    "DISPID_ACC_SELECTION",
    "DISPID_ACC_DEFAULTACTION",
    "DISPID_ACC_SELECT",
    "DISPID_ACC_LOCATION",
    "DISPID_ACC_NAVIGATE",
    "DISPID_ACC_HITTEST",
    "DISPID_ACC_DODEFAULTACTION",
    "NAVDIR_MIN",
    "NAVDIR_UP",
    "NAVDIR_DOWN",
    "NAVDIR_LEFT",
    "NAVDIR_RIGHT",
    "NAVDIR_NEXT",
    "NAVDIR_PREVIOUS",
    "NAVDIR_FIRSTCHILD",
    "NAVDIR_LASTCHILD",
    "NAVDIR_MAX",
    "SELFLAG_NONE",
    "SELFLAG_TAKEFOCUS",
    "SELFLAG_TAKESELECTION",
    "SELFLAG_EXTENDSELECTION",
    "SELFLAG_ADDSELECTION",
    "SELFLAG_REMOVESELECTION",
    "SELFLAG_VALID",
    "STATE_SYSTEM_NORMAL",
    "STATE_SYSTEM_HASPOPUP",
    "ROLE_SYSTEM_TITLEBAR",
    "ROLE_SYSTEM_MENUBAR",
    "ROLE_SYSTEM_SCROLLBAR",
    "ROLE_SYSTEM_GRIP",
    "ROLE_SYSTEM_SOUND",
    "ROLE_SYSTEM_CURSOR",
    "ROLE_SYSTEM_CARET",
    "ROLE_SYSTEM_ALERT",
    "ROLE_SYSTEM_WINDOW",
    "ROLE_SYSTEM_CLIENT",
    "ROLE_SYSTEM_MENUPOPUP",
    "ROLE_SYSTEM_MENUITEM",
    "ROLE_SYSTEM_TOOLTIP",
    "ROLE_SYSTEM_APPLICATION",
    "ROLE_SYSTEM_DOCUMENT",
    "ROLE_SYSTEM_PANE",
    "ROLE_SYSTEM_CHART",
    "ROLE_SYSTEM_DIALOG",
    "ROLE_SYSTEM_BORDER",
    "ROLE_SYSTEM_GROUPING",
    "ROLE_SYSTEM_SEPARATOR",
    "ROLE_SYSTEM_TOOLBAR",
    "ROLE_SYSTEM_STATUSBAR",
    "ROLE_SYSTEM_TABLE",
    "ROLE_SYSTEM_COLUMNHEADER",
    "ROLE_SYSTEM_ROWHEADER",
    "ROLE_SYSTEM_COLUMN",
    "ROLE_SYSTEM_ROW",
    "ROLE_SYSTEM_CELL",
    "ROLE_SYSTEM_LINK",
    "ROLE_SYSTEM_HELPBALLOON",
    "ROLE_SYSTEM_CHARACTER",
    "ROLE_SYSTEM_LIST",
    "ROLE_SYSTEM_LISTITEM",
    "ROLE_SYSTEM_OUTLINE",
    "ROLE_SYSTEM_OUTLINEITEM",
    "ROLE_SYSTEM_PAGETAB",
    "ROLE_SYSTEM_PROPERTYPAGE",
    "ROLE_SYSTEM_INDICATOR",
    "ROLE_SYSTEM_GRAPHIC",
    "ROLE_SYSTEM_STATICTEXT",
    "ROLE_SYSTEM_TEXT",
    "ROLE_SYSTEM_PUSHBUTTON",
    "ROLE_SYSTEM_CHECKBUTTON",
    "ROLE_SYSTEM_RADIOBUTTON",
    "ROLE_SYSTEM_COMBOBOX",
    "ROLE_SYSTEM_DROPLIST",
    "ROLE_SYSTEM_PROGRESSBAR",
    "ROLE_SYSTEM_DIAL",
    "ROLE_SYSTEM_HOTKEYFIELD",
    "ROLE_SYSTEM_SLIDER",
    "ROLE_SYSTEM_SPINBUTTON",
    "ROLE_SYSTEM_DIAGRAM",
    "ROLE_SYSTEM_ANIMATION",
    "ROLE_SYSTEM_EQUATION",
    "ROLE_SYSTEM_BUTTONDROPDOWN",
    "ROLE_SYSTEM_BUTTONMENU",
    "ROLE_SYSTEM_BUTTONDROPDOWNGRID",
    "ROLE_SYSTEM_WHITESPACE",
    "ROLE_SYSTEM_PAGETABLIST",
    "ROLE_SYSTEM_CLOCK",
    "ROLE_SYSTEM_SPLITBUTTON",
    "ROLE_SYSTEM_IPADDRESS",
    "ROLE_SYSTEM_OUTLINEBUTTON",
    "UIA_E_ELEMENTNOTENABLED",
    "UIA_E_ELEMENTNOTAVAILABLE",
    "UIA_E_NOCLICKABLEPOINT",
    "UIA_E_PROXYASSEMBLYNOTLOADED",
    "UIA_E_NOTSUPPORTED",
    "UIA_E_INVALIDOPERATION",
    "UIA_E_TIMEOUT",
    "UiaAppendRuntimeId",
    "UiaRootObjectId",
    "RuntimeId_Property_GUID",
    "BoundingRectangle_Property_GUID",
    "ProcessId_Property_GUID",
    "ControlType_Property_GUID",
    "LocalizedControlType_Property_GUID",
    "Name_Property_GUID",
    "AcceleratorKey_Property_GUID",
    "AccessKey_Property_GUID",
    "HasKeyboardFocus_Property_GUID",
    "IsKeyboardFocusable_Property_GUID",
    "IsEnabled_Property_GUID",
    "AutomationId_Property_GUID",
    "ClassName_Property_GUID",
    "HelpText_Property_GUID",
    "ClickablePoint_Property_GUID",
    "Culture_Property_GUID",
    "IsControlElement_Property_GUID",
    "IsContentElement_Property_GUID",
    "LabeledBy_Property_GUID",
    "IsPassword_Property_GUID",
    "NewNativeWindowHandle_Property_GUID",
    "ItemType_Property_GUID",
    "IsOffscreen_Property_GUID",
    "Orientation_Property_GUID",
    "FrameworkId_Property_GUID",
    "IsRequiredForForm_Property_GUID",
    "ItemStatus_Property_GUID",
    "AriaRole_Property_GUID",
    "AriaProperties_Property_GUID",
    "IsDataValidForForm_Property_GUID",
    "ControllerFor_Property_GUID",
    "DescribedBy_Property_GUID",
    "FlowsTo_Property_GUID",
    "ProviderDescription_Property_GUID",
    "OptimizeForVisualContent_Property_GUID",
    "IsDockPatternAvailable_Property_GUID",
    "IsExpandCollapsePatternAvailable_Property_GUID",
    "IsGridItemPatternAvailable_Property_GUID",
    "IsGridPatternAvailable_Property_GUID",
    "IsInvokePatternAvailable_Property_GUID",
    "IsMultipleViewPatternAvailable_Property_GUID",
    "IsRangeValuePatternAvailable_Property_GUID",
    "IsScrollPatternAvailable_Property_GUID",
    "IsScrollItemPatternAvailable_Property_GUID",
    "IsSelectionItemPatternAvailable_Property_GUID",
    "IsSelectionPatternAvailable_Property_GUID",
    "IsTablePatternAvailable_Property_GUID",
    "IsTableItemPatternAvailable_Property_GUID",
    "IsTextPatternAvailable_Property_GUID",
    "IsTogglePatternAvailable_Property_GUID",
    "IsTransformPatternAvailable_Property_GUID",
    "IsValuePatternAvailable_Property_GUID",
    "IsWindowPatternAvailable_Property_GUID",
    "IsLegacyIAccessiblePatternAvailable_Property_GUID",
    "IsItemContainerPatternAvailable_Property_GUID",
    "IsVirtualizedItemPatternAvailable_Property_GUID",
    "IsSynchronizedInputPatternAvailable_Property_GUID",
    "IsObjectModelPatternAvailable_Property_GUID",
    "IsAnnotationPatternAvailable_Property_GUID",
    "IsTextPattern2Available_Property_GUID",
    "IsTextEditPatternAvailable_Property_GUID",
    "IsCustomNavigationPatternAvailable_Property_GUID",
    "IsStylesPatternAvailable_Property_GUID",
    "IsSpreadsheetPatternAvailable_Property_GUID",
    "IsSpreadsheetItemPatternAvailable_Property_GUID",
    "IsTransformPattern2Available_Property_GUID",
    "IsTextChildPatternAvailable_Property_GUID",
    "IsDragPatternAvailable_Property_GUID",
    "IsDropTargetPatternAvailable_Property_GUID",
    "IsStructuredMarkupPatternAvailable_Property_GUID",
    "IsPeripheral_Property_GUID",
    "PositionInSet_Property_GUID",
    "SizeOfSet_Property_GUID",
    "Level_Property_GUID",
    "AnnotationTypes_Property_GUID",
    "AnnotationObjects_Property_GUID",
    "LandmarkType_Property_GUID",
    "LocalizedLandmarkType_Property_GUID",
    "FullDescription_Property_GUID",
    "Value_Value_Property_GUID",
    "Value_IsReadOnly_Property_GUID",
    "RangeValue_Value_Property_GUID",
    "RangeValue_IsReadOnly_Property_GUID",
    "RangeValue_Minimum_Property_GUID",
    "RangeValue_Maximum_Property_GUID",
    "RangeValue_LargeChange_Property_GUID",
    "RangeValue_SmallChange_Property_GUID",
    "Scroll_HorizontalScrollPercent_Property_GUID",
    "Scroll_HorizontalViewSize_Property_GUID",
    "Scroll_VerticalScrollPercent_Property_GUID",
    "Scroll_VerticalViewSize_Property_GUID",
    "Scroll_HorizontallyScrollable_Property_GUID",
    "Scroll_VerticallyScrollable_Property_GUID",
    "Selection_Selection_Property_GUID",
    "Selection_CanSelectMultiple_Property_GUID",
    "Selection_IsSelectionRequired_Property_GUID",
    "Grid_RowCount_Property_GUID",
    "Grid_ColumnCount_Property_GUID",
    "GridItem_Row_Property_GUID",
    "GridItem_Column_Property_GUID",
    "GridItem_RowSpan_Property_GUID",
    "GridItem_ColumnSpan_Property_GUID",
    "GridItem_Parent_Property_GUID",
    "Dock_DockPosition_Property_GUID",
    "ExpandCollapse_ExpandCollapseState_Property_GUID",
    "MultipleView_CurrentView_Property_GUID",
    "MultipleView_SupportedViews_Property_GUID",
    "Window_CanMaximize_Property_GUID",
    "Window_CanMinimize_Property_GUID",
    "Window_WindowVisualState_Property_GUID",
    "Window_WindowInteractionState_Property_GUID",
    "Window_IsModal_Property_GUID",
    "Window_IsTopmost_Property_GUID",
    "SelectionItem_IsSelected_Property_GUID",
    "SelectionItem_SelectionContainer_Property_GUID",
    "Table_RowHeaders_Property_GUID",
    "Table_ColumnHeaders_Property_GUID",
    "Table_RowOrColumnMajor_Property_GUID",
    "TableItem_RowHeaderItems_Property_GUID",
    "TableItem_ColumnHeaderItems_Property_GUID",
    "Toggle_ToggleState_Property_GUID",
    "Transform_CanMove_Property_GUID",
    "Transform_CanResize_Property_GUID",
    "Transform_CanRotate_Property_GUID",
    "LegacyIAccessible_ChildId_Property_GUID",
    "LegacyIAccessible_Name_Property_GUID",
    "LegacyIAccessible_Value_Property_GUID",
    "LegacyIAccessible_Description_Property_GUID",
    "LegacyIAccessible_Role_Property_GUID",
    "LegacyIAccessible_State_Property_GUID",
    "LegacyIAccessible_Help_Property_GUID",
    "LegacyIAccessible_KeyboardShortcut_Property_GUID",
    "LegacyIAccessible_Selection_Property_GUID",
    "LegacyIAccessible_DefaultAction_Property_GUID",
    "Annotation_AnnotationTypeId_Property_GUID",
    "Annotation_AnnotationTypeName_Property_GUID",
    "Annotation_Author_Property_GUID",
    "Annotation_DateTime_Property_GUID",
    "Annotation_Target_Property_GUID",
    "Styles_StyleId_Property_GUID",
    "Styles_StyleName_Property_GUID",
    "Styles_FillColor_Property_GUID",
    "Styles_FillPatternStyle_Property_GUID",
    "Styles_Shape_Property_GUID",
    "Styles_FillPatternColor_Property_GUID",
    "Styles_ExtendedProperties_Property_GUID",
    "SpreadsheetItem_Formula_Property_GUID",
    "SpreadsheetItem_AnnotationObjects_Property_GUID",
    "SpreadsheetItem_AnnotationTypes_Property_GUID",
    "Transform2_CanZoom_Property_GUID",
    "LiveSetting_Property_GUID",
    "Drag_IsGrabbed_Property_GUID",
    "Drag_GrabbedItems_Property_GUID",
    "Drag_DropEffect_Property_GUID",
    "Drag_DropEffects_Property_GUID",
    "DropTarget_DropTargetEffect_Property_GUID",
    "DropTarget_DropTargetEffects_Property_GUID",
    "Transform2_ZoomLevel_Property_GUID",
    "Transform2_ZoomMinimum_Property_GUID",
    "Transform2_ZoomMaximum_Property_GUID",
    "FlowsFrom_Property_GUID",
    "FillColor_Property_GUID",
    "OutlineColor_Property_GUID",
    "FillType_Property_GUID",
    "VisualEffects_Property_GUID",
    "OutlineThickness_Property_GUID",
    "CenterPoint_Property_GUID",
    "Rotation_Property_GUID",
    "Size_Property_GUID",
    "ToolTipOpened_Event_GUID",
    "ToolTipClosed_Event_GUID",
    "StructureChanged_Event_GUID",
    "MenuOpened_Event_GUID",
    "AutomationPropertyChanged_Event_GUID",
    "AutomationFocusChanged_Event_GUID",
    "ActiveTextPositionChanged_Event_GUID",
    "AsyncContentLoaded_Event_GUID",
    "MenuClosed_Event_GUID",
    "LayoutInvalidated_Event_GUID",
    "Invoke_Invoked_Event_GUID",
    "SelectionItem_ElementAddedToSelectionEvent_Event_GUID",
    "SelectionItem_ElementRemovedFromSelectionEvent_Event_GUID",
    "SelectionItem_ElementSelectedEvent_Event_GUID",
    "Selection_InvalidatedEvent_Event_GUID",
    "Text_TextSelectionChangedEvent_Event_GUID",
    "Text_TextChangedEvent_Event_GUID",
    "Window_WindowOpened_Event_GUID",
    "Window_WindowClosed_Event_GUID",
    "MenuModeStart_Event_GUID",
    "MenuModeEnd_Event_GUID",
    "InputReachedTarget_Event_GUID",
    "InputReachedOtherElement_Event_GUID",
    "InputDiscarded_Event_GUID",
    "SystemAlert_Event_GUID",
    "LiveRegionChanged_Event_GUID",
    "HostedFragmentRootsInvalidated_Event_GUID",
    "Drag_DragStart_Event_GUID",
    "Drag_DragCancel_Event_GUID",
    "Drag_DragComplete_Event_GUID",
    "DropTarget_DragEnter_Event_GUID",
    "DropTarget_DragLeave_Event_GUID",
    "DropTarget_Dropped_Event_GUID",
    "StructuredMarkup_CompositionComplete_Event_GUID",
    "StructuredMarkup_Deleted_Event_GUID",
    "StructuredMarkup_SelectionChanged_Event_GUID",
    "Invoke_Pattern_GUID",
    "Selection_Pattern_GUID",
    "Value_Pattern_GUID",
    "RangeValue_Pattern_GUID",
    "Scroll_Pattern_GUID",
    "ExpandCollapse_Pattern_GUID",
    "Grid_Pattern_GUID",
    "GridItem_Pattern_GUID",
    "MultipleView_Pattern_GUID",
    "Window_Pattern_GUID",
    "SelectionItem_Pattern_GUID",
    "Dock_Pattern_GUID",
    "Table_Pattern_GUID",
    "TableItem_Pattern_GUID",
    "Text_Pattern_GUID",
    "Toggle_Pattern_GUID",
    "Transform_Pattern_GUID",
    "ScrollItem_Pattern_GUID",
    "LegacyIAccessible_Pattern_GUID",
    "ItemContainer_Pattern_GUID",
    "VirtualizedItem_Pattern_GUID",
    "SynchronizedInput_Pattern_GUID",
    "ObjectModel_Pattern_GUID",
    "Annotation_Pattern_GUID",
    "Text_Pattern2_GUID",
    "TextEdit_Pattern_GUID",
    "CustomNavigation_Pattern_GUID",
    "Styles_Pattern_GUID",
    "Spreadsheet_Pattern_GUID",
    "SpreadsheetItem_Pattern_GUID",
    "Tranform_Pattern2_GUID",
    "TextChild_Pattern_GUID",
    "Drag_Pattern_GUID",
    "DropTarget_Pattern_GUID",
    "StructuredMarkup_Pattern_GUID",
    "Button_Control_GUID",
    "Calendar_Control_GUID",
    "CheckBox_Control_GUID",
    "ComboBox_Control_GUID",
    "Edit_Control_GUID",
    "Hyperlink_Control_GUID",
    "Image_Control_GUID",
    "ListItem_Control_GUID",
    "List_Control_GUID",
    "Menu_Control_GUID",
    "MenuBar_Control_GUID",
    "MenuItem_Control_GUID",
    "ProgressBar_Control_GUID",
    "RadioButton_Control_GUID",
    "ScrollBar_Control_GUID",
    "Slider_Control_GUID",
    "Spinner_Control_GUID",
    "StatusBar_Control_GUID",
    "Tab_Control_GUID",
    "TabItem_Control_GUID",
    "Text_Control_GUID",
    "ToolBar_Control_GUID",
    "ToolTip_Control_GUID",
    "Tree_Control_GUID",
    "TreeItem_Control_GUID",
    "Custom_Control_GUID",
    "Group_Control_GUID",
    "Thumb_Control_GUID",
    "DataGrid_Control_GUID",
    "DataItem_Control_GUID",
    "Document_Control_GUID",
    "SplitButton_Control_GUID",
    "Window_Control_GUID",
    "Pane_Control_GUID",
    "Header_Control_GUID",
    "HeaderItem_Control_GUID",
    "Table_Control_GUID",
    "TitleBar_Control_GUID",
    "Separator_Control_GUID",
    "SemanticZoom_Control_GUID",
    "AppBar_Control_GUID",
    "Text_AnimationStyle_Attribute_GUID",
    "Text_BackgroundColor_Attribute_GUID",
    "Text_BulletStyle_Attribute_GUID",
    "Text_CapStyle_Attribute_GUID",
    "Text_Culture_Attribute_GUID",
    "Text_FontName_Attribute_GUID",
    "Text_FontSize_Attribute_GUID",
    "Text_FontWeight_Attribute_GUID",
    "Text_ForegroundColor_Attribute_GUID",
    "Text_HorizontalTextAlignment_Attribute_GUID",
    "Text_IndentationFirstLine_Attribute_GUID",
    "Text_IndentationLeading_Attribute_GUID",
    "Text_IndentationTrailing_Attribute_GUID",
    "Text_IsHidden_Attribute_GUID",
    "Text_IsItalic_Attribute_GUID",
    "Text_IsReadOnly_Attribute_GUID",
    "Text_IsSubscript_Attribute_GUID",
    "Text_IsSuperscript_Attribute_GUID",
    "Text_MarginBottom_Attribute_GUID",
    "Text_MarginLeading_Attribute_GUID",
    "Text_MarginTop_Attribute_GUID",
    "Text_MarginTrailing_Attribute_GUID",
    "Text_OutlineStyles_Attribute_GUID",
    "Text_OverlineColor_Attribute_GUID",
    "Text_OverlineStyle_Attribute_GUID",
    "Text_StrikethroughColor_Attribute_GUID",
    "Text_StrikethroughStyle_Attribute_GUID",
    "Text_Tabs_Attribute_GUID",
    "Text_TextFlowDirections_Attribute_GUID",
    "Text_UnderlineColor_Attribute_GUID",
    "Text_UnderlineStyle_Attribute_GUID",
    "Text_AnnotationTypes_Attribute_GUID",
    "Text_AnnotationObjects_Attribute_GUID",
    "Text_StyleName_Attribute_GUID",
    "Text_StyleId_Attribute_GUID",
    "Text_Link_Attribute_GUID",
    "Text_IsActive_Attribute_GUID",
    "Text_SelectionActiveEnd_Attribute_GUID",
    "Text_CaretPosition_Attribute_GUID",
    "Text_CaretBidiMode_Attribute_GUID",
    "Text_BeforeParagraphSpacing_Attribute_GUID",
    "Text_AfterParagraphSpacing_Attribute_GUID",
    "Text_LineSpacing_Attribute_GUID",
    "Text_BeforeSpacing_Attribute_GUID",
    "Text_AfterSpacing_Attribute_GUID",
    "Text_SayAsInterpretAs_Attribute_GUID",
    "TextEdit_TextChanged_Event_GUID",
    "TextEdit_ConversionTargetChanged_Event_GUID",
    "Changes_Event_GUID",
    "Annotation_Custom_GUID",
    "Annotation_SpellingError_GUID",
    "Annotation_GrammarError_GUID",
    "Annotation_Comment_GUID",
    "Annotation_FormulaError_GUID",
    "Annotation_TrackChanges_GUID",
    "Annotation_Header_GUID",
    "Annotation_Footer_GUID",
    "Annotation_Highlighted_GUID",
    "Annotation_Endnote_GUID",
    "Annotation_Footnote_GUID",
    "Annotation_InsertionChange_GUID",
    "Annotation_DeletionChange_GUID",
    "Annotation_MoveChange_GUID",
    "Annotation_FormatChange_GUID",
    "Annotation_UnsyncedChange_GUID",
    "Annotation_EditingLockedChange_GUID",
    "Annotation_ExternalChange_GUID",
    "Annotation_ConflictingChange_GUID",
    "Annotation_Author_GUID",
    "Annotation_AdvancedProofingIssue_GUID",
    "Annotation_DataValidationError_GUID",
    "Annotation_CircularReferenceError_GUID",
    "Annotation_Mathematics_GUID",
    "Annotation_Sensitive_GUID",
    "Changes_Summary_GUID",
    "StyleId_Custom_GUID",
    "StyleId_Heading1_GUID",
    "StyleId_Heading2_GUID",
    "StyleId_Heading3_GUID",
    "StyleId_Heading4_GUID",
    "StyleId_Heading5_GUID",
    "StyleId_Heading6_GUID",
    "StyleId_Heading7_GUID",
    "StyleId_Heading8_GUID",
    "StyleId_Heading9_GUID",
    "StyleId_Title_GUID",
    "StyleId_Subtitle_GUID",
    "StyleId_Normal_GUID",
    "StyleId_Emphasis_GUID",
    "StyleId_Quote_GUID",
    "StyleId_BulletedList_GUID",
    "StyleId_NumberedList_GUID",
    "Notification_Event_GUID",
    "SID_IsUIAutomationObject",
    "SID_ControlElementProvider",
    "IsSelectionPattern2Available_Property_GUID",
    "Selection2_FirstSelectedItem_Property_GUID",
    "Selection2_LastSelectedItem_Property_GUID",
    "Selection2_CurrentSelectedItem_Property_GUID",
    "Selection2_ItemCount_Property_GUID",
    "Selection_Pattern2_GUID",
    "HeadingLevel_Property_GUID",
    "IsDialog_Property_GUID",
    "UIA_IAFP_DEFAULT",
    "UIA_IAFP_UNWRAP_BRIDGE",
    "UIA_PFIA_DEFAULT",
    "UIA_PFIA_UNWRAP_BRIDGE",
    "UIA_ScrollPatternNoScroll",
    "UIA_InvokePatternId",
    "UIA_SelectionPatternId",
    "UIA_ValuePatternId",
    "UIA_RangeValuePatternId",
    "UIA_ScrollPatternId",
    "UIA_ExpandCollapsePatternId",
    "UIA_GridPatternId",
    "UIA_GridItemPatternId",
    "UIA_MultipleViewPatternId",
    "UIA_WindowPatternId",
    "UIA_SelectionItemPatternId",
    "UIA_DockPatternId",
    "UIA_TablePatternId",
    "UIA_TableItemPatternId",
    "UIA_TextPatternId",
    "UIA_TogglePatternId",
    "UIA_TransformPatternId",
    "UIA_ScrollItemPatternId",
    "UIA_LegacyIAccessiblePatternId",
    "UIA_ItemContainerPatternId",
    "UIA_VirtualizedItemPatternId",
    "UIA_SynchronizedInputPatternId",
    "UIA_ObjectModelPatternId",
    "UIA_AnnotationPatternId",
    "UIA_TextPattern2Id",
    "UIA_StylesPatternId",
    "UIA_SpreadsheetPatternId",
    "UIA_SpreadsheetItemPatternId",
    "UIA_TransformPattern2Id",
    "UIA_TextChildPatternId",
    "UIA_DragPatternId",
    "UIA_DropTargetPatternId",
    "UIA_TextEditPatternId",
    "UIA_CustomNavigationPatternId",
    "UIA_SelectionPattern2Id",
    "UIA_ToolTipOpenedEventId",
    "UIA_ToolTipClosedEventId",
    "UIA_StructureChangedEventId",
    "UIA_MenuOpenedEventId",
    "UIA_AutomationPropertyChangedEventId",
    "UIA_AutomationFocusChangedEventId",
    "UIA_AsyncContentLoadedEventId",
    "UIA_MenuClosedEventId",
    "UIA_LayoutInvalidatedEventId",
    "UIA_Invoke_InvokedEventId",
    "UIA_SelectionItem_ElementAddedToSelectionEventId",
    "UIA_SelectionItem_ElementRemovedFromSelectionEventId",
    "UIA_SelectionItem_ElementSelectedEventId",
    "UIA_Selection_InvalidatedEventId",
    "UIA_Text_TextSelectionChangedEventId",
    "UIA_Text_TextChangedEventId",
    "UIA_Window_WindowOpenedEventId",
    "UIA_Window_WindowClosedEventId",
    "UIA_MenuModeStartEventId",
    "UIA_MenuModeEndEventId",
    "UIA_InputReachedTargetEventId",
    "UIA_InputReachedOtherElementEventId",
    "UIA_InputDiscardedEventId",
    "UIA_SystemAlertEventId",
    "UIA_LiveRegionChangedEventId",
    "UIA_HostedFragmentRootsInvalidatedEventId",
    "UIA_Drag_DragStartEventId",
    "UIA_Drag_DragCancelEventId",
    "UIA_Drag_DragCompleteEventId",
    "UIA_DropTarget_DragEnterEventId",
    "UIA_DropTarget_DragLeaveEventId",
    "UIA_DropTarget_DroppedEventId",
    "UIA_TextEdit_TextChangedEventId",
    "UIA_TextEdit_ConversionTargetChangedEventId",
    "UIA_ChangesEventId",
    "UIA_NotificationEventId",
    "UIA_ActiveTextPositionChangedEventId",
    "UIA_RuntimeIdPropertyId",
    "UIA_BoundingRectanglePropertyId",
    "UIA_ProcessIdPropertyId",
    "UIA_ControlTypePropertyId",
    "UIA_LocalizedControlTypePropertyId",
    "UIA_NamePropertyId",
    "UIA_AcceleratorKeyPropertyId",
    "UIA_AccessKeyPropertyId",
    "UIA_HasKeyboardFocusPropertyId",
    "UIA_IsKeyboardFocusablePropertyId",
    "UIA_IsEnabledPropertyId",
    "UIA_AutomationIdPropertyId",
    "UIA_ClassNamePropertyId",
    "UIA_HelpTextPropertyId",
    "UIA_ClickablePointPropertyId",
    "UIA_CulturePropertyId",
    "UIA_IsControlElementPropertyId",
    "UIA_IsContentElementPropertyId",
    "UIA_LabeledByPropertyId",
    "UIA_IsPasswordPropertyId",
    "UIA_NativeWindowHandlePropertyId",
    "UIA_ItemTypePropertyId",
    "UIA_IsOffscreenPropertyId",
    "UIA_OrientationPropertyId",
    "UIA_FrameworkIdPropertyId",
    "UIA_IsRequiredForFormPropertyId",
    "UIA_ItemStatusPropertyId",
    "UIA_IsDockPatternAvailablePropertyId",
    "UIA_IsExpandCollapsePatternAvailablePropertyId",
    "UIA_IsGridItemPatternAvailablePropertyId",
    "UIA_IsGridPatternAvailablePropertyId",
    "UIA_IsInvokePatternAvailablePropertyId",
    "UIA_IsMultipleViewPatternAvailablePropertyId",
    "UIA_IsRangeValuePatternAvailablePropertyId",
    "UIA_IsScrollPatternAvailablePropertyId",
    "UIA_IsScrollItemPatternAvailablePropertyId",
    "UIA_IsSelectionItemPatternAvailablePropertyId",
    "UIA_IsSelectionPatternAvailablePropertyId",
    "UIA_IsTablePatternAvailablePropertyId",
    "UIA_IsTableItemPatternAvailablePropertyId",
    "UIA_IsTextPatternAvailablePropertyId",
    "UIA_IsTogglePatternAvailablePropertyId",
    "UIA_IsTransformPatternAvailablePropertyId",
    "UIA_IsValuePatternAvailablePropertyId",
    "UIA_IsWindowPatternAvailablePropertyId",
    "UIA_ValueValuePropertyId",
    "UIA_ValueIsReadOnlyPropertyId",
    "UIA_RangeValueValuePropertyId",
    "UIA_RangeValueIsReadOnlyPropertyId",
    "UIA_RangeValueMinimumPropertyId",
    "UIA_RangeValueMaximumPropertyId",
    "UIA_RangeValueLargeChangePropertyId",
    "UIA_RangeValueSmallChangePropertyId",
    "UIA_ScrollHorizontalScrollPercentPropertyId",
    "UIA_ScrollHorizontalViewSizePropertyId",
    "UIA_ScrollVerticalScrollPercentPropertyId",
    "UIA_ScrollVerticalViewSizePropertyId",
    "UIA_ScrollHorizontallyScrollablePropertyId",
    "UIA_ScrollVerticallyScrollablePropertyId",
    "UIA_SelectionSelectionPropertyId",
    "UIA_SelectionCanSelectMultiplePropertyId",
    "UIA_SelectionIsSelectionRequiredPropertyId",
    "UIA_GridRowCountPropertyId",
    "UIA_GridColumnCountPropertyId",
    "UIA_GridItemRowPropertyId",
    "UIA_GridItemColumnPropertyId",
    "UIA_GridItemRowSpanPropertyId",
    "UIA_GridItemColumnSpanPropertyId",
    "UIA_GridItemContainingGridPropertyId",
    "UIA_DockDockPositionPropertyId",
    "UIA_ExpandCollapseExpandCollapseStatePropertyId",
    "UIA_MultipleViewCurrentViewPropertyId",
    "UIA_MultipleViewSupportedViewsPropertyId",
    "UIA_WindowCanMaximizePropertyId",
    "UIA_WindowCanMinimizePropertyId",
    "UIA_WindowWindowVisualStatePropertyId",
    "UIA_WindowWindowInteractionStatePropertyId",
    "UIA_WindowIsModalPropertyId",
    "UIA_WindowIsTopmostPropertyId",
    "UIA_SelectionItemIsSelectedPropertyId",
    "UIA_SelectionItemSelectionContainerPropertyId",
    "UIA_TableRowHeadersPropertyId",
    "UIA_TableColumnHeadersPropertyId",
    "UIA_TableRowOrColumnMajorPropertyId",
    "UIA_TableItemRowHeaderItemsPropertyId",
    "UIA_TableItemColumnHeaderItemsPropertyId",
    "UIA_ToggleToggleStatePropertyId",
    "UIA_TransformCanMovePropertyId",
    "UIA_TransformCanResizePropertyId",
    "UIA_TransformCanRotatePropertyId",
    "UIA_IsLegacyIAccessiblePatternAvailablePropertyId",
    "UIA_LegacyIAccessibleChildIdPropertyId",
    "UIA_LegacyIAccessibleNamePropertyId",
    "UIA_LegacyIAccessibleValuePropertyId",
    "UIA_LegacyIAccessibleDescriptionPropertyId",
    "UIA_LegacyIAccessibleRolePropertyId",
    "UIA_LegacyIAccessibleStatePropertyId",
    "UIA_LegacyIAccessibleHelpPropertyId",
    "UIA_LegacyIAccessibleKeyboardShortcutPropertyId",
    "UIA_LegacyIAccessibleSelectionPropertyId",
    "UIA_LegacyIAccessibleDefaultActionPropertyId",
    "UIA_AriaRolePropertyId",
    "UIA_AriaPropertiesPropertyId",
    "UIA_IsDataValidForFormPropertyId",
    "UIA_ControllerForPropertyId",
    "UIA_DescribedByPropertyId",
    "UIA_FlowsToPropertyId",
    "UIA_ProviderDescriptionPropertyId",
    "UIA_IsItemContainerPatternAvailablePropertyId",
    "UIA_IsVirtualizedItemPatternAvailablePropertyId",
    "UIA_IsSynchronizedInputPatternAvailablePropertyId",
    "UIA_OptimizeForVisualContentPropertyId",
    "UIA_IsObjectModelPatternAvailablePropertyId",
    "UIA_AnnotationAnnotationTypeIdPropertyId",
    "UIA_AnnotationAnnotationTypeNamePropertyId",
    "UIA_AnnotationAuthorPropertyId",
    "UIA_AnnotationDateTimePropertyId",
    "UIA_AnnotationTargetPropertyId",
    "UIA_IsAnnotationPatternAvailablePropertyId",
    "UIA_IsTextPattern2AvailablePropertyId",
    "UIA_StylesStyleIdPropertyId",
    "UIA_StylesStyleNamePropertyId",
    "UIA_StylesFillColorPropertyId",
    "UIA_StylesFillPatternStylePropertyId",
    "UIA_StylesShapePropertyId",
    "UIA_StylesFillPatternColorPropertyId",
    "UIA_StylesExtendedPropertiesPropertyId",
    "UIA_IsStylesPatternAvailablePropertyId",
    "UIA_IsSpreadsheetPatternAvailablePropertyId",
    "UIA_SpreadsheetItemFormulaPropertyId",
    "UIA_SpreadsheetItemAnnotationObjectsPropertyId",
    "UIA_SpreadsheetItemAnnotationTypesPropertyId",
    "UIA_IsSpreadsheetItemPatternAvailablePropertyId",
    "UIA_Transform2CanZoomPropertyId",
    "UIA_IsTransformPattern2AvailablePropertyId",
    "UIA_LiveSettingPropertyId",
    "UIA_IsTextChildPatternAvailablePropertyId",
    "UIA_IsDragPatternAvailablePropertyId",
    "UIA_DragIsGrabbedPropertyId",
    "UIA_DragDropEffectPropertyId",
    "UIA_DragDropEffectsPropertyId",
    "UIA_IsDropTargetPatternAvailablePropertyId",
    "UIA_DropTargetDropTargetEffectPropertyId",
    "UIA_DropTargetDropTargetEffectsPropertyId",
    "UIA_DragGrabbedItemsPropertyId",
    "UIA_Transform2ZoomLevelPropertyId",
    "UIA_Transform2ZoomMinimumPropertyId",
    "UIA_Transform2ZoomMaximumPropertyId",
    "UIA_FlowsFromPropertyId",
    "UIA_IsTextEditPatternAvailablePropertyId",
    "UIA_IsPeripheralPropertyId",
    "UIA_IsCustomNavigationPatternAvailablePropertyId",
    "UIA_PositionInSetPropertyId",
    "UIA_SizeOfSetPropertyId",
    "UIA_LevelPropertyId",
    "UIA_AnnotationTypesPropertyId",
    "UIA_AnnotationObjectsPropertyId",
    "UIA_LandmarkTypePropertyId",
    "UIA_LocalizedLandmarkTypePropertyId",
    "UIA_FullDescriptionPropertyId",
    "UIA_FillColorPropertyId",
    "UIA_OutlineColorPropertyId",
    "UIA_FillTypePropertyId",
    "UIA_VisualEffectsPropertyId",
    "UIA_OutlineThicknessPropertyId",
    "UIA_CenterPointPropertyId",
    "UIA_RotationPropertyId",
    "UIA_SizePropertyId",
    "UIA_IsSelectionPattern2AvailablePropertyId",
    "UIA_Selection2FirstSelectedItemPropertyId",
    "UIA_Selection2LastSelectedItemPropertyId",
    "UIA_Selection2CurrentSelectedItemPropertyId",
    "UIA_Selection2ItemCountPropertyId",
    "UIA_HeadingLevelPropertyId",
    "UIA_IsDialogPropertyId",
    "UIA_AnimationStyleAttributeId",
    "UIA_BackgroundColorAttributeId",
    "UIA_BulletStyleAttributeId",
    "UIA_CapStyleAttributeId",
    "UIA_CultureAttributeId",
    "UIA_FontNameAttributeId",
    "UIA_FontSizeAttributeId",
    "UIA_FontWeightAttributeId",
    "UIA_ForegroundColorAttributeId",
    "UIA_HorizontalTextAlignmentAttributeId",
    "UIA_IndentationFirstLineAttributeId",
    "UIA_IndentationLeadingAttributeId",
    "UIA_IndentationTrailingAttributeId",
    "UIA_IsHiddenAttributeId",
    "UIA_IsItalicAttributeId",
    "UIA_IsReadOnlyAttributeId",
    "UIA_IsSubscriptAttributeId",
    "UIA_IsSuperscriptAttributeId",
    "UIA_MarginBottomAttributeId",
    "UIA_MarginLeadingAttributeId",
    "UIA_MarginTopAttributeId",
    "UIA_MarginTrailingAttributeId",
    "UIA_OutlineStylesAttributeId",
    "UIA_OverlineColorAttributeId",
    "UIA_OverlineStyleAttributeId",
    "UIA_StrikethroughColorAttributeId",
    "UIA_StrikethroughStyleAttributeId",
    "UIA_TabsAttributeId",
    "UIA_TextFlowDirectionsAttributeId",
    "UIA_UnderlineColorAttributeId",
    "UIA_UnderlineStyleAttributeId",
    "UIA_AnnotationTypesAttributeId",
    "UIA_AnnotationObjectsAttributeId",
    "UIA_StyleNameAttributeId",
    "UIA_StyleIdAttributeId",
    "UIA_LinkAttributeId",
    "UIA_IsActiveAttributeId",
    "UIA_SelectionActiveEndAttributeId",
    "UIA_CaretPositionAttributeId",
    "UIA_CaretBidiModeAttributeId",
    "UIA_LineSpacingAttributeId",
    "UIA_BeforeParagraphSpacingAttributeId",
    "UIA_AfterParagraphSpacingAttributeId",
    "UIA_SayAsInterpretAsAttributeId",
    "UIA_ButtonControlTypeId",
    "UIA_CalendarControlTypeId",
    "UIA_CheckBoxControlTypeId",
    "UIA_ComboBoxControlTypeId",
    "UIA_EditControlTypeId",
    "UIA_HyperlinkControlTypeId",
    "UIA_ImageControlTypeId",
    "UIA_ListItemControlTypeId",
    "UIA_ListControlTypeId",
    "UIA_MenuControlTypeId",
    "UIA_MenuBarControlTypeId",
    "UIA_MenuItemControlTypeId",
    "UIA_ProgressBarControlTypeId",
    "UIA_RadioButtonControlTypeId",
    "UIA_ScrollBarControlTypeId",
    "UIA_SliderControlTypeId",
    "UIA_SpinnerControlTypeId",
    "UIA_StatusBarControlTypeId",
    "UIA_TabControlTypeId",
    "UIA_TabItemControlTypeId",
    "UIA_TextControlTypeId",
    "UIA_ToolBarControlTypeId",
    "UIA_ToolTipControlTypeId",
    "UIA_TreeControlTypeId",
    "UIA_TreeItemControlTypeId",
    "UIA_CustomControlTypeId",
    "UIA_GroupControlTypeId",
    "UIA_ThumbControlTypeId",
    "UIA_DataGridControlTypeId",
    "UIA_DataItemControlTypeId",
    "UIA_DocumentControlTypeId",
    "UIA_SplitButtonControlTypeId",
    "UIA_WindowControlTypeId",
    "UIA_PaneControlTypeId",
    "UIA_HeaderControlTypeId",
    "UIA_HeaderItemControlTypeId",
    "UIA_TableControlTypeId",
    "UIA_TitleBarControlTypeId",
    "UIA_SeparatorControlTypeId",
    "UIA_SemanticZoomControlTypeId",
    "UIA_AppBarControlTypeId",
    "AnnotationType_Unknown",
    "AnnotationType_SpellingError",
    "AnnotationType_GrammarError",
    "AnnotationType_Comment",
    "AnnotationType_FormulaError",
    "AnnotationType_TrackChanges",
    "AnnotationType_Header",
    "AnnotationType_Footer",
    "AnnotationType_Highlighted",
    "AnnotationType_Endnote",
    "AnnotationType_Footnote",
    "AnnotationType_InsertionChange",
    "AnnotationType_DeletionChange",
    "AnnotationType_MoveChange",
    "AnnotationType_FormatChange",
    "AnnotationType_UnsyncedChange",
    "AnnotationType_EditingLockedChange",
    "AnnotationType_ExternalChange",
    "AnnotationType_ConflictingChange",
    "AnnotationType_Author",
    "AnnotationType_AdvancedProofingIssue",
    "AnnotationType_DataValidationError",
    "AnnotationType_CircularReferenceError",
    "AnnotationType_Mathematics",
    "AnnotationType_Sensitive",
    "StyleId_Custom",
    "StyleId_Heading1",
    "StyleId_Heading2",
    "StyleId_Heading3",
    "StyleId_Heading4",
    "StyleId_Heading5",
    "StyleId_Heading6",
    "StyleId_Heading7",
    "StyleId_Heading8",
    "StyleId_Heading9",
    "StyleId_Title",
    "StyleId_Subtitle",
    "StyleId_Normal",
    "StyleId_Emphasis",
    "StyleId_Quote",
    "StyleId_BulletedList",
    "StyleId_NumberedList",
    "UIA_CustomLandmarkTypeId",
    "UIA_FormLandmarkTypeId",
    "UIA_MainLandmarkTypeId",
    "UIA_NavigationLandmarkTypeId",
    "UIA_SearchLandmarkTypeId",
    "HeadingLevel_None",
    "HeadingLevel1",
    "HeadingLevel2",
    "HeadingLevel3",
    "HeadingLevel4",
    "HeadingLevel5",
    "HeadingLevel6",
    "HeadingLevel7",
    "HeadingLevel8",
    "HeadingLevel9",
    "UIA_SummaryChangeId",
    "UIA_SayAsInterpretAsMetadataId",
    "STICKYKEYS_FLAGS",
    "SKF_STICKYKEYSON",
    "SKF_AVAILABLE",
    "SKF_HOTKEYACTIVE",
    "SKF_CONFIRMHOTKEY",
    "SKF_HOTKEYSOUND",
    "SKF_INDICATOR",
    "SKF_AUDIBLEFEEDBACK",
    "SKF_TRISTATE",
    "SKF_TWOKEYSOFF",
    "SKF_LALTLATCHED",
    "SKF_LCTLLATCHED",
    "SKF_LSHIFTLATCHED",
    "SKF_RALTLATCHED",
    "SKF_RCTLLATCHED",
    "SKF_RSHIFTLATCHED",
    "SKF_LWINLATCHED",
    "SKF_RWINLATCHED",
    "SKF_LALTLOCKED",
    "SKF_LCTLLOCKED",
    "SKF_LSHIFTLOCKED",
    "SKF_RALTLOCKED",
    "SKF_RCTLLOCKED",
    "SKF_RSHIFTLOCKED",
    "SKF_LWINLOCKED",
    "SKF_RWINLOCKED",
    "SOUNDSENTRY_FLAGS",
    "SSF_SOUNDSENTRYON",
    "SSF_AVAILABLE",
    "SSF_INDICATOR",
    "ACC_UTILITY_STATE_FLAGS",
    "ANRUS_ON_SCREEN_KEYBOARD_ACTIVE",
    "ANRUS_TOUCH_MODIFICATION_ACTIVE",
    "ANRUS_PRIORITY_AUDIO_ACTIVE",
    "ANRUS_PRIORITY_AUDIO_ACTIVE_NODUCK",
    "SOUND_SENTRY_GRAPHICS_EFFECT",
    "SSGF_DISPLAY",
    "SSGF_NONE",
    "SERIALKEYS_FLAGS",
    "SERKF_AVAILABLE",
    "SERKF_INDICATOR",
    "SERKF_SERIALKEYSON",
    "HIGHCONTRASTW_FLAGS",
    "HCF_HIGHCONTRASTON",
    "HCF_AVAILABLE",
    "HCF_HOTKEYACTIVE",
    "HCF_CONFIRMHOTKEY",
    "HCF_HOTKEYSOUND",
    "HCF_INDICATOR",
    "HCF_HOTKEYAVAILABLE",
    "HCF_OPTION_NOTHEMECHANGE",
    "SOUNDSENTRY_TEXT_EFFECT",
    "SSTF_BORDER",
    "SSTF_CHARS",
    "SSTF_DISPLAY",
    "SSTF_NONE",
    "SOUNDSENTRY_WINDOWS_EFFECT",
    "SSWF_CUSTOM",
    "SSWF_DISPLAY",
    "SSWF_NONE",
    "SSWF_TITLE",
    "SSWF_WINDOW",
    "HWINEVENTHOOK",
    "HUIANODE",
    "HUIAPATTERNOBJECT",
    "HUIATEXTRANGE",
    "HUIAEVENT",
    "IRicheditWindowlessAccessibility",
    "IRichEditUiaInformation",
    "CAccPropServices",
    "LPFNLRESULTFROMOBJECT",
    "LPFNOBJECTFROMLRESULT",
    "LPFNACCESSIBLEOBJECTFROMWINDOW",
    "LPFNACCESSIBLEOBJECTFROMPOINT",
    "LPFNCREATESTDACCESSIBLEOBJECT",
    "LPFNACCESSIBLECHILDREN",
    "MSAAMENUINFO",
    "IAccessible",
    "IAccessibleHandler",
    "IAccessibleWindowlessSite",
    "AnnoScope",
    "ANNO_THIS",
    "ANNO_CONTAINER",
    "IAccIdentity",
    "IAccPropServer",
    "IAccPropServices",
    "CUIAutomation",
    "CUIAutomation8",
    "CUIAutomationRegistrar",
    "NavigateDirection",
    "NavigateDirection_Parent",
    "NavigateDirection_NextSibling",
    "NavigateDirection_PreviousSibling",
    "NavigateDirection_FirstChild",
    "NavigateDirection_LastChild",
    "ProviderOptions",
    "ProviderOptions_ClientSideProvider",
    "ProviderOptions_ServerSideProvider",
    "ProviderOptions_NonClientAreaProvider",
    "ProviderOptions_OverrideProvider",
    "ProviderOptions_ProviderOwnsSetFocus",
    "ProviderOptions_UseComThreading",
    "ProviderOptions_RefuseNonClientSupport",
    "ProviderOptions_HasNativeIAccessible",
    "ProviderOptions_UseClientCoordinates",
    "StructureChangeType",
    "StructureChangeType_ChildAdded",
    "StructureChangeType_ChildRemoved",
    "StructureChangeType_ChildrenInvalidated",
    "StructureChangeType_ChildrenBulkAdded",
    "StructureChangeType_ChildrenBulkRemoved",
    "StructureChangeType_ChildrenReordered",
    "TextEditChangeType",
    "TextEditChangeType_None",
    "TextEditChangeType_AutoCorrect",
    "TextEditChangeType_Composition",
    "TextEditChangeType_CompositionFinalized",
    "TextEditChangeType_AutoComplete",
    "OrientationType",
    "OrientationType_None",
    "OrientationType_Horizontal",
    "OrientationType_Vertical",
    "DockPosition",
    "DockPosition_Top",
    "DockPosition_Left",
    "DockPosition_Bottom",
    "DockPosition_Right",
    "DockPosition_Fill",
    "DockPosition_None",
    "ExpandCollapseState",
    "ExpandCollapseState_Collapsed",
    "ExpandCollapseState_Expanded",
    "ExpandCollapseState_PartiallyExpanded",
    "ExpandCollapseState_LeafNode",
    "ScrollAmount",
    "ScrollAmount_LargeDecrement",
    "ScrollAmount_SmallDecrement",
    "ScrollAmount_NoAmount",
    "ScrollAmount_LargeIncrement",
    "ScrollAmount_SmallIncrement",
    "RowOrColumnMajor",
    "RowOrColumnMajor_RowMajor",
    "RowOrColumnMajor_ColumnMajor",
    "RowOrColumnMajor_Indeterminate",
    "ToggleState",
    "ToggleState_Off",
    "ToggleState_On",
    "ToggleState_Indeterminate",
    "WindowVisualState",
    "WindowVisualState_Normal",
    "WindowVisualState_Maximized",
    "WindowVisualState_Minimized",
    "SynchronizedInputType",
    "SynchronizedInputType_KeyUp",
    "SynchronizedInputType_KeyDown",
    "SynchronizedInputType_LeftMouseUp",
    "SynchronizedInputType_LeftMouseDown",
    "SynchronizedInputType_RightMouseUp",
    "SynchronizedInputType_RightMouseDown",
    "WindowInteractionState",
    "WindowInteractionState_Running",
    "WindowInteractionState_Closing",
    "WindowInteractionState_ReadyForUserInteraction",
    "WindowInteractionState_BlockedByModalWindow",
    "WindowInteractionState_NotResponding",
    "SayAsInterpretAs",
    "SayAsInterpretAs_None",
    "SayAsInterpretAs_Spell",
    "SayAsInterpretAs_Cardinal",
    "SayAsInterpretAs_Ordinal",
    "SayAsInterpretAs_Number",
    "SayAsInterpretAs_Date",
    "SayAsInterpretAs_Time",
    "SayAsInterpretAs_Telephone",
    "SayAsInterpretAs_Currency",
    "SayAsInterpretAs_Net",
    "SayAsInterpretAs_Url",
    "SayAsInterpretAs_Address",
    "SayAsInterpretAs_Alphanumeric",
    "SayAsInterpretAs_Name",
    "SayAsInterpretAs_Media",
    "SayAsInterpretAs_Date_MonthDayYear",
    "SayAsInterpretAs_Date_DayMonthYear",
    "SayAsInterpretAs_Date_YearMonthDay",
    "SayAsInterpretAs_Date_YearMonth",
    "SayAsInterpretAs_Date_MonthYear",
    "SayAsInterpretAs_Date_DayMonth",
    "SayAsInterpretAs_Date_MonthDay",
    "SayAsInterpretAs_Date_Year",
    "SayAsInterpretAs_Time_HoursMinutesSeconds12",
    "SayAsInterpretAs_Time_HoursMinutes12",
    "SayAsInterpretAs_Time_HoursMinutesSeconds24",
    "SayAsInterpretAs_Time_HoursMinutes24",
    "TextUnit",
    "TextUnit_Character",
    "TextUnit_Format",
    "TextUnit_Word",
    "TextUnit_Line",
    "TextUnit_Paragraph",
    "TextUnit_Page",
    "TextUnit_Document",
    "TextPatternRangeEndpoint",
    "TextPatternRangeEndpoint_Start",
    "TextPatternRangeEndpoint_End",
    "SupportedTextSelection",
    "SupportedTextSelection_None",
    "SupportedTextSelection_Single",
    "SupportedTextSelection_Multiple",
    "LiveSetting",
    "LiveSetting_Off",
    "LiveSetting_Polite",
    "LiveSetting_Assertive",
    "ActiveEnd",
    "ActiveEnd_None",
    "ActiveEnd_Start",
    "ActiveEnd_End",
    "CaretPosition",
    "CaretPosition_Unknown",
    "CaretPosition_EndOfLine",
    "CaretPosition_BeginningOfLine",
    "CaretBidiMode",
    "CaretBidiMode_LTR",
    "CaretBidiMode_RTL",
    "ZoomUnit",
    "ZoomUnit_NoAmount",
    "ZoomUnit_LargeDecrement",
    "ZoomUnit_SmallDecrement",
    "ZoomUnit_LargeIncrement",
    "ZoomUnit_SmallIncrement",
    "AnimationStyle",
    "AnimationStyle_None",
    "AnimationStyle_LasVegasLights",
    "AnimationStyle_BlinkingBackground",
    "AnimationStyle_SparkleText",
    "AnimationStyle_MarchingBlackAnts",
    "AnimationStyle_MarchingRedAnts",
    "AnimationStyle_Shimmer",
    "AnimationStyle_Other",
    "BulletStyle",
    "BulletStyle_None",
    "BulletStyle_HollowRoundBullet",
    "BulletStyle_FilledRoundBullet",
    "BulletStyle_HollowSquareBullet",
    "BulletStyle_FilledSquareBullet",
    "BulletStyle_DashBullet",
    "BulletStyle_Other",
    "CapStyle",
    "CapStyle_None",
    "CapStyle_SmallCap",
    "CapStyle_AllCap",
    "CapStyle_AllPetiteCaps",
    "CapStyle_PetiteCaps",
    "CapStyle_Unicase",
    "CapStyle_Titling",
    "CapStyle_Other",
    "FillType",
    "FillType_None",
    "FillType_Color",
    "FillType_Gradient",
    "FillType_Picture",
    "FillType_Pattern",
    "FlowDirections",
    "FlowDirections_Default",
    "FlowDirections_RightToLeft",
    "FlowDirections_BottomToTop",
    "FlowDirections_Vertical",
    "HorizontalTextAlignment",
    "HorizontalTextAlignment_Left",
    "HorizontalTextAlignment_Centered",
    "HorizontalTextAlignment_Right",
    "HorizontalTextAlignment_Justified",
    "OutlineStyles",
    "OutlineStyles_None",
    "OutlineStyles_Outline",
    "OutlineStyles_Shadow",
    "OutlineStyles_Engraved",
    "OutlineStyles_Embossed",
    "TextDecorationLineStyle",
    "TextDecorationLineStyle_None",
    "TextDecorationLineStyle_Single",
    "TextDecorationLineStyle_WordsOnly",
    "TextDecorationLineStyle_Double",
    "TextDecorationLineStyle_Dot",
    "TextDecorationLineStyle_Dash",
    "TextDecorationLineStyle_DashDot",
    "TextDecorationLineStyle_DashDotDot",
    "TextDecorationLineStyle_Wavy",
    "TextDecorationLineStyle_ThickSingle",
    "TextDecorationLineStyle_DoubleWavy",
    "TextDecorationLineStyle_ThickWavy",
    "TextDecorationLineStyle_LongDash",
    "TextDecorationLineStyle_ThickDash",
    "TextDecorationLineStyle_ThickDashDot",
    "TextDecorationLineStyle_ThickDashDotDot",
    "TextDecorationLineStyle_ThickDot",
    "TextDecorationLineStyle_ThickLongDash",
    "TextDecorationLineStyle_Other",
    "VisualEffects",
    "VisualEffects_None",
    "VisualEffects_Shadow",
    "VisualEffects_Reflection",
    "VisualEffects_Glow",
    "VisualEffects_SoftEdges",
    "VisualEffects_Bevel",
    "NotificationProcessing",
    "NotificationProcessing_ImportantAll",
    "NotificationProcessing_ImportantMostRecent",
    "NotificationProcessing_All",
    "NotificationProcessing_MostRecent",
    "NotificationProcessing_CurrentThenMostRecent",
    "NotificationKind",
    "NotificationKind_ItemAdded",
    "NotificationKind_ItemRemoved",
    "NotificationKind_ActionCompleted",
    "NotificationKind_ActionAborted",
    "NotificationKind_Other",
    "UiaRect",
    "UiaPoint",
    "UiaChangeInfo",
    "UIAutomationType",
    "UIAutomationType_Int",
    "UIAutomationType_Bool",
    "UIAutomationType_String",
    "UIAutomationType_Double",
    "UIAutomationType_Point",
    "UIAutomationType_Rect",
    "UIAutomationType_Element",
    "UIAutomationType_Array",
    "UIAutomationType_Out",
    "UIAutomationType_IntArray",
    "UIAutomationType_BoolArray",
    "UIAutomationType_StringArray",
    "UIAutomationType_DoubleArray",
    "UIAutomationType_PointArray",
    "UIAutomationType_RectArray",
    "UIAutomationType_ElementArray",
    "UIAutomationType_OutInt",
    "UIAutomationType_OutBool",
    "UIAutomationType_OutString",
    "UIAutomationType_OutDouble",
    "UIAutomationType_OutPoint",
    "UIAutomationType_OutRect",
    "UIAutomationType_OutElement",
    "UIAutomationType_OutIntArray",
    "UIAutomationType_OutBoolArray",
    "UIAutomationType_OutStringArray",
    "UIAutomationType_OutDoubleArray",
    "UIAutomationType_OutPointArray",
    "UIAutomationType_OutRectArray",
    "UIAutomationType_OutElementArray",
    "UIAutomationParameter",
    "UIAutomationPropertyInfo",
    "UIAutomationEventInfo",
    "UIAutomationMethodInfo",
    "UIAutomationPatternInfo",
    "IRawElementProviderSimple",
    "IAccessibleEx",
    "IRawElementProviderSimple2",
    "IRawElementProviderSimple3",
    "IRawElementProviderFragmentRoot",
    "IRawElementProviderFragment",
    "IRawElementProviderAdviseEvents",
    "IRawElementProviderHwndOverride",
    "IProxyProviderWinEventSink",
    "IProxyProviderWinEventHandler",
    "IRawElementProviderWindowlessSite",
    "IAccessibleHostingElementProviders",
    "IRawElementProviderHostingAccessibles",
    "IDockProvider",
    "IExpandCollapseProvider",
    "IGridProvider",
    "IGridItemProvider",
    "IInvokeProvider",
    "IMultipleViewProvider",
    "IRangeValueProvider",
    "IScrollItemProvider",
    "ISelectionProvider",
    "ISelectionProvider2",
    "IScrollProvider",
    "ISelectionItemProvider",
    "ISynchronizedInputProvider",
    "ITableProvider",
    "ITableItemProvider",
    "IToggleProvider",
    "ITransformProvider",
    "IValueProvider",
    "IWindowProvider",
    "ILegacyIAccessibleProvider",
    "IItemContainerProvider",
    "IVirtualizedItemProvider",
    "IObjectModelProvider",
    "IAnnotationProvider",
    "IStylesProvider",
    "ISpreadsheetProvider",
    "ISpreadsheetItemProvider",
    "ITransformProvider2",
    "IDragProvider",
    "IDropTargetProvider",
    "ITextRangeProvider",
    "ITextProvider",
    "ITextProvider2",
    "ITextEditProvider",
    "ITextRangeProvider2",
    "ITextChildProvider",
    "ICustomNavigationProvider",
    "IUIAutomationPatternInstance",
    "IUIAutomationPatternHandler",
    "IUIAutomationRegistrar",
    "TreeScope",
    "TreeScope_None",
    "TreeScope_Element",
    "TreeScope_Children",
    "TreeScope_Descendants",
    "TreeScope_Parent",
    "TreeScope_Ancestors",
    "TreeScope_Subtree",
    "PropertyConditionFlags",
    "PropertyConditionFlags_None",
    "PropertyConditionFlags_IgnoreCase",
    "PropertyConditionFlags_MatchSubstring",
    "AutomationElementMode",
    "AutomationElementMode_None",
    "AutomationElementMode_Full",
    "TreeTraversalOptions",
    "TreeTraversalOptions_Default",
    "TreeTraversalOptions_PostOrder",
    "TreeTraversalOptions_LastToFirstOrder",
    "ConnectionRecoveryBehaviorOptions",
    "ConnectionRecoveryBehaviorOptions_Disabled",
    "ConnectionRecoveryBehaviorOptions_Enabled",
    "CoalesceEventsOptions",
    "CoalesceEventsOptions_Disabled",
    "CoalesceEventsOptions_Enabled",
    "ExtendedProperty",
    "IUIAutomationElement",
    "IUIAutomationElementArray",
    "IUIAutomationCondition",
    "IUIAutomationBoolCondition",
    "IUIAutomationPropertyCondition",
    "IUIAutomationAndCondition",
    "IUIAutomationOrCondition",
    "IUIAutomationNotCondition",
    "IUIAutomationCacheRequest",
    "IUIAutomationTreeWalker",
    "IUIAutomationEventHandler",
    "IUIAutomationPropertyChangedEventHandler",
    "IUIAutomationStructureChangedEventHandler",
    "IUIAutomationFocusChangedEventHandler",
    "IUIAutomationTextEditTextChangedEventHandler",
    "IUIAutomationChangesEventHandler",
    "IUIAutomationNotificationEventHandler",
    "IUIAutomationInvokePattern",
    "IUIAutomationDockPattern",
    "IUIAutomationExpandCollapsePattern",
    "IUIAutomationGridPattern",
    "IUIAutomationGridItemPattern",
    "IUIAutomationMultipleViewPattern",
    "IUIAutomationObjectModelPattern",
    "IUIAutomationRangeValuePattern",
    "IUIAutomationScrollPattern",
    "IUIAutomationScrollItemPattern",
    "IUIAutomationSelectionPattern",
    "IUIAutomationSelectionPattern2",
    "IUIAutomationSelectionItemPattern",
    "IUIAutomationSynchronizedInputPattern",
    "IUIAutomationTablePattern",
    "IUIAutomationTableItemPattern",
    "IUIAutomationTogglePattern",
    "IUIAutomationTransformPattern",
    "IUIAutomationValuePattern",
    "IUIAutomationWindowPattern",
    "IUIAutomationTextRange",
    "IUIAutomationTextRange2",
    "IUIAutomationTextRange3",
    "IUIAutomationTextRangeArray",
    "IUIAutomationTextPattern",
    "IUIAutomationTextPattern2",
    "IUIAutomationTextEditPattern",
    "IUIAutomationCustomNavigationPattern",
    "IUIAutomationActiveTextPositionChangedEventHandler",
    "IUIAutomationLegacyIAccessiblePattern",
    "IUIAutomationItemContainerPattern",
    "IUIAutomationVirtualizedItemPattern",
    "IUIAutomationAnnotationPattern",
    "IUIAutomationStylesPattern",
    "IUIAutomationSpreadsheetPattern",
    "IUIAutomationSpreadsheetItemPattern",
    "IUIAutomationTransformPattern2",
    "IUIAutomationTextChildPattern",
    "IUIAutomationDragPattern",
    "IUIAutomationDropTargetPattern",
    "IUIAutomationElement2",
    "IUIAutomationElement3",
    "IUIAutomationElement4",
    "IUIAutomationElement5",
    "IUIAutomationElement6",
    "IUIAutomationElement7",
    "IUIAutomationElement8",
    "IUIAutomationElement9",
    "IUIAutomationProxyFactory",
    "IUIAutomationProxyFactoryEntry",
    "IUIAutomationProxyFactoryMapping",
    "IUIAutomationEventHandlerGroup",
    "IUIAutomation",
    "IUIAutomation2",
    "IUIAutomation3",
    "IUIAutomation4",
    "IUIAutomation5",
    "IUIAutomation6",
    "ConditionType",
    "ConditionType_True",
    "ConditionType_False",
    "ConditionType_Property",
    "ConditionType_And",
    "ConditionType_Or",
    "ConditionType_Not",
    "UiaCondition",
    "UiaPropertyCondition",
    "UiaAndOrCondition",
    "UiaNotCondition",
    "UiaCacheRequest",
    "NormalizeState",
    "NormalizeState_None",
    "NormalizeState_View",
    "NormalizeState_Custom",
    "UiaFindParams",
    "ProviderType",
    "ProviderType_BaseHwnd",
    "ProviderType_Proxy",
    "ProviderType_NonClientArea",
    "UiaProviderCallback",
    "AutomationIdentifierType",
    "AutomationIdentifierType_Property",
    "AutomationIdentifierType_Pattern",
    "AutomationIdentifierType_Event",
    "AutomationIdentifierType_ControlType",
    "AutomationIdentifierType_TextAttribute",
    "AutomationIdentifierType_LandmarkType",
    "AutomationIdentifierType_Annotation",
    "AutomationIdentifierType_Changes",
    "AutomationIdentifierType_Style",
    "EventArgsType",
    "EventArgsType_Simple",
    "EventArgsType_PropertyChanged",
    "EventArgsType_StructureChanged",
    "EventArgsType_AsyncContentLoaded",
    "EventArgsType_WindowClosed",
    "EventArgsType_TextEditTextChanged",
    "EventArgsType_Changes",
    "EventArgsType_Notification",
    "EventArgsType_ActiveTextPositionChanged",
    "EventArgsType_StructuredMarkup",
    "AsyncContentLoadedState",
    "AsyncContentLoadedState_Beginning",
    "AsyncContentLoadedState_Progress",
    "AsyncContentLoadedState_Completed",
    "UiaEventArgs",
    "UiaPropertyChangedEventArgs",
    "UiaStructureChangedEventArgs",
    "UiaTextEditTextChangedEventArgs",
    "UiaChangesEventArgs",
    "UiaAsyncContentLoadedEventArgs",
    "UiaWindowClosedEventArgs",
    "UiaEventCallback",
    "SERIALKEYSA",
    "SERIALKEYSW",
    "HIGHCONTRASTA",
    "HIGHCONTRASTW",
    "FILTERKEYS",
    "STICKYKEYS",
    "MOUSEKEYS",
    "ACCESSTIMEOUT",
    "SOUNDSENTRYA",
    "SOUNDSENTRYW",
    "TOGGLEKEYS",
    "WINEVENTPROC",
    "LresultFromObject",
    "ObjectFromLresult",
    "WindowFromAccessibleObject",
    "AccessibleObjectFromWindow",
    "AccessibleObjectFromEvent",
    "AccessibleObjectFromPoint",
    "AccessibleChildren",
    "GetRoleTextA",
    "GetRoleTextW",
    "GetRoleText",
    "GetStateTextA",
    "GetStateTextW",
    "GetStateText",
    "GetOleaccVersionInfo",
    "CreateStdAccessibleObject",
    "CreateStdAccessibleProxyA",
    "CreateStdAccessibleProxyW",
    "CreateStdAccessibleProxy",
    "AccSetRunningUtilityState",
    "AccNotifyTouchInteraction",
    "UiaGetErrorDescription",
    "UiaHUiaNodeFromVariant",
    "UiaHPatternObjectFromVariant",
    "UiaHTextRangeFromVariant",
    "UiaNodeRelease",
    "UiaGetPropertyValue",
    "UiaGetPatternProvider",
    "UiaGetRuntimeId",
    "UiaSetFocus",
    "UiaNavigate",
    "UiaGetUpdatedCache",
    "UiaFind",
    "UiaNodeFromPoint",
    "UiaNodeFromFocus",
    "UiaNodeFromHandle",
    "UiaNodeFromProvider",
    "UiaGetRootNode",
    "UiaRegisterProviderCallback",
    "UiaLookupId",
    "UiaGetReservedNotSupportedValue",
    "UiaGetReservedMixedAttributeValue",
    "UiaClientsAreListening",
    "UiaRaiseAutomationPropertyChangedEvent",
    "UiaRaiseAutomationEvent",
    "UiaRaiseStructureChangedEvent",
    "UiaRaiseAsyncContentLoadedEvent",
    "UiaRaiseTextEditTextChangedEvent",
    "UiaRaiseChangesEvent",
    "UiaRaiseNotificationEvent",
    "UiaRaiseActiveTextPositionChangedEvent",
    "UiaAddEvent",
    "UiaRemoveEvent",
    "UiaEventAddWindow",
    "UiaEventRemoveWindow",
    "DockPattern_SetDockPosition",
    "ExpandCollapsePattern_Collapse",
    "ExpandCollapsePattern_Expand",
    "GridPattern_GetItem",
    "InvokePattern_Invoke",
    "MultipleViewPattern_GetViewName",
    "MultipleViewPattern_SetCurrentView",
    "RangeValuePattern_SetValue",
    "ScrollItemPattern_ScrollIntoView",
    "ScrollPattern_Scroll",
    "ScrollPattern_SetScrollPercent",
    "SelectionItemPattern_AddToSelection",
    "SelectionItemPattern_RemoveFromSelection",
    "SelectionItemPattern_Select",
    "TogglePattern_Toggle",
    "TransformPattern_Move",
    "TransformPattern_Resize",
    "TransformPattern_Rotate",
    "ValuePattern_SetValue",
    "WindowPattern_Close",
    "WindowPattern_SetWindowVisualState",
    "WindowPattern_WaitForInputIdle",
    "TextPattern_GetSelection",
    "TextPattern_GetVisibleRanges",
    "TextPattern_RangeFromChild",
    "TextPattern_RangeFromPoint",
    "TextPattern_get_DocumentRange",
    "TextPattern_get_SupportedTextSelection",
    "TextRange_Clone",
    "TextRange_Compare",
    "TextRange_CompareEndpoints",
    "TextRange_ExpandToEnclosingUnit",
    "TextRange_GetAttributeValue",
    "TextRange_FindAttribute",
    "TextRange_FindText",
    "TextRange_GetBoundingRectangles",
    "TextRange_GetEnclosingElement",
    "TextRange_GetText",
    "TextRange_Move",
    "TextRange_MoveEndpointByUnit",
    "TextRange_MoveEndpointByRange",
    "TextRange_Select",
    "TextRange_AddToSelection",
    "TextRange_RemoveFromSelection",
    "TextRange_ScrollIntoView",
    "TextRange_GetChildren",
    "ItemContainerPattern_FindItemByProperty",
    "LegacyIAccessiblePattern_Select",
    "LegacyIAccessiblePattern_DoDefaultAction",
    "LegacyIAccessiblePattern_SetValue",
    "LegacyIAccessiblePattern_GetIAccessible",
    "SynchronizedInputPattern_StartListening",
    "SynchronizedInputPattern_Cancel",
    "VirtualizedItemPattern_Realize",
    "UiaPatternRelease",
    "UiaTextRangeRelease",
    "UiaReturnRawElementProvider",
    "UiaHostProviderFromHwnd",
    "UiaProviderForNonClient",
    "UiaIAccessibleFromProvider",
    "UiaProviderFromIAccessible",
    "UiaDisconnectAllProviders",
    "UiaDisconnectProvider",
    "UiaHasServerSideProvider",
    "RegisterPointerInputTarget",
    "UnregisterPointerInputTarget",
    "RegisterPointerInputTargetEx",
    "UnregisterPointerInputTargetEx",
    "NotifyWinEvent",
    "SetWinEventHook",
    "IsWinEventHookInstalled",
    "UnhookWinEvent",
]
