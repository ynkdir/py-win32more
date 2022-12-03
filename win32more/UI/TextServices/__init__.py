from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.UI.TextServices
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
AccClientDocMgr = Guid('fc48cc30-4f3e-4fa1-80-3b-ad-0e-19-6a-83-b1')
AccDictionary = Guid('6572ee16-5fe5-4331-bb-6d-76-a4-9c-56-e4-23')
AccServerDocMgr = Guid('6089a37e-eb8a-482d-bd-6f-f9-f4-69-04-d1-6d')
AccStore = Guid('5440837f-4bff-4ae5-a1-b1-77-22-ec-c6-33-2a')
ANCHOR_CHANGE_HISTORY_FLAGS = UInt32
TS_CH_PRECEDING_DEL = 1
TS_CH_FOLLOWING_DEL = 2
def _define_GUID_PROP_TEXTOWNER():
    return Guid('f1e2d520-0969-11d3-8d-f0-00-10-5a-27-99-b5')
def _define_GUID_PROP_ATTRIBUTE():
    return Guid('34b45670-7526-11d2-a1-47-00-10-5a-27-99-b5')
def _define_GUID_PROP_LANGID():
    return Guid('3280ce20-8032-11d2-b6-03-00-10-5a-27-99-b5')
def _define_GUID_PROP_READING():
    return Guid('5463f7c0-8e31-11d2-bf-46-00-10-5a-27-99-b5')
def _define_GUID_PROP_COMPOSING():
    return Guid('e12ac060-af15-11d2-af-c5-00-10-5a-27-99-b5')
def _define_GUID_PROP_TKB_ALTERNATES():
    return Guid('70b2a803-968d-462e-b9-3b-21-64-c9-15-17-f7')
def _define_GUID_SYSTEM_FUNCTIONPROVIDER():
    return Guid('9a698bb0-0f21-11d3-8d-f1-00-10-5a-27-99-b5')
def _define_GUID_APP_FUNCTIONPROVIDER():
    return Guid('4caef01e-12af-4b0e-9d-b1-a6-ec-5b-88-12-08')
def _define_GUID_TFCAT_CATEGORY_OF_TIP():
    return Guid('534c48c1-0607-4098-a5-21-4f-c8-99-c7-3e-90')
def _define_GUID_TFCAT_TIP_KEYBOARD():
    return Guid('34745c63-b2f0-4784-8b-67-5e-12-c8-70-1a-31')
def _define_GUID_TFCAT_TIP_SPEECH():
    return Guid('b5a73cd1-8355-426b-a1-61-25-98-08-f2-6b-14')
def _define_GUID_TFCAT_TIP_HANDWRITING():
    return Guid('246ecb87-c2f2-4abe-90-5b-c8-b3-8a-dd-2c-43')
def _define_GUID_TFCAT_PROP_AUDIODATA():
    return Guid('9b7be3a9-e8ab-4d47-a8-fe-25-4f-a4-23-43-6d')
def _define_GUID_TFCAT_PROP_INKDATA():
    return Guid('7c6a82ae-b0d7-4f14-a7-45-14-f2-8b-00-9d-61')
def _define_GUID_COMPARTMENT_SAPI_AUDIO():
    return Guid('51af2086-cc6b-457d-b5-aa-8b-19-dc-29-0a-b4')
def _define_GUID_COMPARTMENT_KEYBOARD_DISABLED():
    return Guid('71a5b253-1951-466b-9f-bc-9c-88-08-fa-84-f2')
def _define_GUID_COMPARTMENT_KEYBOARD_OPENCLOSE():
    return Guid('58273aad-01bb-4164-95-c6-75-5b-a0-b5-16-2d')
def _define_GUID_COMPARTMENT_HANDWRITING_OPENCLOSE():
    return Guid('f9ae2c6b-1866-4361-af-72-7a-a3-09-48-89-0e')
def _define_GUID_COMPARTMENT_SPEECH_DISABLED():
    return Guid('56c5c607-0703-4e59-8e-52-cb-c8-4e-8b-be-35')
def _define_GUID_COMPARTMENT_SPEECH_OPENCLOSE():
    return Guid('544d6a63-e2e8-4752-bb-d1-00-09-60-bc-a0-83')
def _define_GUID_COMPARTMENT_SPEECH_GLOBALSTATE():
    return Guid('2a54fe8e-0d08-460c-a7-5d-87-03-5f-f4-36-c5')
def _define_GUID_COMPARTMENT_CONVERSIONMODEBIAS():
    return Guid('5497f516-ee91-436e-b9-46-aa-2c-05-f1-ac-5b')
def _define_GUID_PROP_MODEBIAS():
    return Guid('372e0716-974f-40ac-a0-88-08-cd-c9-2e-bf-bc')
def _define_GUID_COMPARTMENT_KEYBOARD_INPUTMODE():
    return Guid('b6592511-bcee-4122-a7-c4-09-f4-b3-fa-43-96')
def _define_GUID_MODEBIAS_NONE():
    return Guid('00000000-0000-0000-00-00-00-00-00-00-00-00')
def _define_GUID_MODEBIAS_URLHISTORY():
    return Guid('8b0e54d9-63f2-4c68-84-d4-79-ae-e7-a5-9f-09')
def _define_GUID_MODEBIAS_FILENAME():
    return Guid('d7f707fe-44c6-4fca-8e-76-86-ab-50-c7-93-1b')
def _define_GUID_MODEBIAS_READING():
    return Guid('e31643a3-6466-4cbf-8d-8b-0b-d4-d8-54-54-61')
def _define_GUID_MODEBIAS_DATETIME():
    return Guid('f2bdb372-7f61-4039-92-ef-1c-35-59-9f-02-22')
def _define_GUID_MODEBIAS_NAME():
    return Guid('fddc10f0-d239-49bf-b8-fc-54-10-ca-aa-42-7e')
def _define_GUID_MODEBIAS_CONVERSATION():
    return Guid('0f4ec104-1790-443b-95-f1-e1-0f-93-9d-65-46')
def _define_GUID_MODEBIAS_NUMERIC():
    return Guid('4021766c-e872-48fd-9c-ee-4e-c5-c7-5e-16-c3')
def _define_GUID_MODEBIAS_HIRAGANA():
    return Guid('d73d316e-9b91-46f1-a2-80-31-59-7f-52-c6-94')
def _define_GUID_MODEBIAS_KATAKANA():
    return Guid('2e0eeddd-3a1a-499e-85-43-3c-7e-e7-94-98-11')
def _define_GUID_MODEBIAS_HANGUL():
    return Guid('76ef0541-23b3-4d77-a0-74-69-18-01-cc-ea-17')
def _define_GUID_MODEBIAS_CHINESE():
    return Guid('7add26de-4328-489b-83-ae-64-93-75-0c-ad-5c')
def _define_GUID_MODEBIAS_HALFWIDTHKATAKANA():
    return Guid('005f6b63-78d4-41cc-88-59-48-5c-a8-21-a7-95')
def _define_GUID_MODEBIAS_FULLWIDTHALPHANUMERIC():
    return Guid('81489fb8-b36a-473d-81-46-e4-a2-25-8b-24-ae')
def _define_GUID_MODEBIAS_FULLWIDTHHANGUL():
    return Guid('c01ae6c9-45b5-4fd0-9c-b1-9f-4c-eb-c3-9f-ea')
def _define_GUID_TFCAT_PROPSTYLE_STATIC():
    return Guid('565fb8d8-6bd4-4ca1-b2-23-0f-2c-cb-8f-4f-96')
def _define_GUID_TFCAT_DISPLAYATTRIBUTEPROVIDER():
    return Guid('046b8c80-1647-40f7-9b-21-b9-3b-81-aa-bc-1b')
def _define_GUID_TFCAT_DISPLAYATTRIBUTEPROPERTY():
    return Guid('b95f181b-ea4c-4af1-80-56-7c-32-1a-bb-b0-91')
def _define_GUID_COMPARTMENT_SPEECH_UI_STATUS():
    return Guid('d92016f0-9367-4fe7-9a-bf-bc-59-da-cb-e0-e3')
def _define_GUID_COMPARTMENT_EMPTYCONTEXT():
    return Guid('d7487dbf-804e-41c5-89-4d-ad-96-fd-4e-ea-13')
def _define_GUID_COMPARTMENT_TIPUISTATUS():
    return Guid('148ca3ec-0366-401c-8d-75-ed-97-8d-85-fb-c9')
def _define_GUID_COMPARTMENT_SPEECH_CFGMENU():
    return Guid('fb6c5c2d-4e83-4bb6-91-a2-e0-19-bf-f6-76-2d')
def _define_GUID_LBI_SAPILAYR_CFGMENUBUTTON():
    return Guid('d02f24a1-942d-422e-8d-99-b4-f2-ad-de-e9-99')
def _define_GUID_TFCAT_TIPCAP_SECUREMODE():
    return Guid('49d2f9ce-1f5e-11d7-a6-d3-00-06-5b-84-43-5c')
def _define_GUID_TFCAT_TIPCAP_UIELEMENTENABLED():
    return Guid('49d2f9cf-1f5e-11d7-a6-d3-00-06-5b-84-43-5c')
def _define_GUID_TFCAT_TIPCAP_INPUTMODECOMPARTMENT():
    return Guid('ccf05dd7-4a87-11d7-a6-e2-00-06-5b-84-43-5c')
def _define_GUID_TFCAT_TIPCAP_COMLESS():
    return Guid('364215d9-75bc-11d7-a6-ef-00-06-5b-84-43-5c')
def _define_GUID_TFCAT_TIPCAP_WOW16():
    return Guid('364215da-75bc-11d7-a6-ef-00-06-5b-84-43-5c')
def _define_GUID_TFCAT_TIPCAP_IMMERSIVESUPPORT():
    return Guid('13a016df-560b-46cd-94-7a-4c-3a-f1-e0-e3-5d')
def _define_GUID_TFCAT_TIPCAP_IMMERSIVEONLY():
    return Guid('3a4259ac-640d-4ad4-89-f7-1e-b6-7e-7c-4e-e8')
def _define_GUID_TFCAT_TIPCAP_LOCALSERVER():
    return Guid('74769ee9-4a66-4f9d-90-d6-bf-8b-7c-3e-b4-61')
def _define_GUID_TFCAT_TIPCAP_TSF3():
    return Guid('07dcb4af-98de-4548-be-f7-25-bd-45-97-9a-1f')
def _define_GUID_TFCAT_TIPCAP_DUALMODE():
    return Guid('3af314a2-d79f-4b1b-99-92-15-08-6d-33-9b-05')
def _define_GUID_TFCAT_TIPCAP_SYSTRAYSUPPORT():
    return Guid('25504fb4-7bab-4bc1-9c-69-cf-81-89-0f-0e-f5')
def _define_GUID_COMPARTMENT_KEYBOARD_INPUTMODE_CONVERSION():
    return Guid('ccf05dd8-4a87-11d7-a6-e2-00-06-5b-84-43-5c')
def _define_GUID_COMPARTMENT_KEYBOARD_INPUTMODE_SENTENCE():
    return Guid('ccf05dd9-4a87-11d7-a6-e2-00-06-5b-84-43-5c')
def _define_GUID_COMPARTMENT_TRANSITORYEXTENSION():
    return Guid('8be347f5-c7a0-11d7-b4-08-00-06-5b-84-43-5c')
def _define_GUID_COMPARTMENT_TRANSITORYEXTENSION_DOCUMENTMANAGER():
    return Guid('8be347f7-c7a0-11d7-b4-08-00-06-5b-84-43-5c')
def _define_GUID_COMPARTMENT_TRANSITORYEXTENSION_PARENT():
    return Guid('8be347f8-c7a0-11d7-b4-08-00-06-5b-84-43-5c')
def _define_GUID_COMPARTMENT_ENABLED_PROFILES_UPDATED():
    return Guid('92c1fd48-a9ae-4a7c-be-08-43-29-e4-72-38-17')
def _define_GUID_TFCAT_TRANSITORYEXTENSIONUI():
    return Guid('6302de22-a5cf-4b02-bf-e8-4d-72-b2-be-d3-c6')
def _define_GUID_LBI_INPUTMODE():
    return Guid('2c77a81e-41cc-4178-a3-a7-5f-8a-98-75-68-e6')
def _define_CLSID_TF_ThreadMgr():
    return Guid('529a9e6b-6587-4f23-ab-9e-9c-7d-68-3e-3c-50')
def _define_CLSID_TF_LangBarMgr():
    return Guid('ebb08c45-6c4a-4fdc-ae-53-4e-b8-c4-c7-db-8e')
def _define_CLSID_TF_DisplayAttributeMgr():
    return Guid('3ce74de4-53d3-4d74-8b-83-43-1b-38-28-ba-53')
def _define_CLSID_TF_CategoryMgr():
    return Guid('a4b544a1-438d-4b41-93-25-86-95-23-e2-d6-c7')
def _define_CLSID_TF_InputProcessorProfiles():
    return Guid('33c53a50-f456-4884-b0-49-85-fd-64-3e-cf-ed')
def _define_CLSID_TF_LangBarItemMgr():
    return Guid('b9931692-a2b3-4fab-bf-33-9e-c6-f9-fb-96-ac')
def _define_CLSID_TF_ClassicLangBar():
    return Guid('3318360c-1afc-4d09-a8-6b-9f-9c-b6-dc-eb-9c')
def _define_CLSID_TF_TransitoryExtensionUIEntry():
    return Guid('ae6be008-07fb-400d-8b-eb-33-7a-64-f7-05-1f')
def _define_CLSID_TsfServices():
    return Guid('39aedc00-6b60-46db-8d-31-36-42-be-0e-43-73')
TF_DEFAULT_SELECTION = 18446744073709551615
TS_DEFAULT_SELECTION = 18446744073709551615
def _define_GUID_TS_SERVICE_DATAOBJECT():
    return Guid('6086fbb5-e225-46ce-a7-70-c1-bb-d3-e0-5d-7b')
def _define_GUID_TS_SERVICE_ACCESSIBLE():
    return Guid('f9786200-a5bf-4a0f-8c-24-fb-16-f5-d1-aa-bb')
def _define_GUID_TS_SERVICE_ACTIVEX():
    return Guid('ea937a50-c9a6-4b7d-89-4a-49-d9-9b-78-48-34')
TS_E_INVALIDPOS = -2147220992
TS_E_NOLOCK = -2147220991
TS_E_NOOBJECT = -2147220990
TS_E_NOSERVICE = -2147220989
TS_E_NOINTERFACE = -2147220988
TS_E_NOSELECTION = -2147220987
TS_E_NOLAYOUT = -2147220986
TS_E_INVALIDPOINT = -2147220985
TS_E_SYNCHRONOUS = -2147220984
TS_E_READONLY = -2147220983
TS_E_FORMAT = -2147220982
TS_S_ASYNC = 262912
TS_AS_TEXT_CHANGE = 1
TS_AS_SEL_CHANGE = 2
TS_AS_LAYOUT_CHANGE = 4
TS_AS_ATTR_CHANGE = 8
TS_AS_STATUS_CHANGE = 16
TS_LF_SYNC = 1
TS_SD_READONLY = 1
TS_SD_LOADING = 2
TS_SD_RESERVED = 4
TS_SD_TKBAUTOCORRECTENABLE = 8
TS_SD_TKBPREDICTIONENABLE = 16
TS_SD_UIINTEGRATIONENABLE = 32
TS_SD_INPUTPANEMANUALDISPLAYENABLE = 64
TS_SD_EMBEDDEDHANDWRITINGVIEW_ENABLED = 128
TS_SD_EMBEDDEDHANDWRITINGVIEW_VISIBLE = 256
TS_SS_DISJOINTSEL = 1
TS_SS_REGIONS = 2
TS_SS_TRANSITORY = 4
TS_SS_NOHIDDENTEXT = 8
TS_SS_TKBAUTOCORRECTENABLE = 16
TS_SS_TKBPREDICTIONENABLE = 32
TS_SS_UWPCONTROL = 64
TS_IE_CORRECTION = 1
TS_IE_COMPOSITION = 2
TS_IAS_NOQUERY = 1
TS_IAS_QUERYONLY = 2
GXFPF_ROUND_NEAREST = 1
GXFPF_NEAREST = 2
TS_CHAR_EMBEDDED = 65532
TS_CHAR_REGION = 0
TS_CHAR_REPLACEMENT = 65533
TS_ATTR_FIND_BACKWARDS = 1
TS_ATTR_FIND_WANT_OFFSET = 2
TS_ATTR_FIND_UPDATESTART = 4
TS_ATTR_FIND_WANT_VALUE = 8
TS_ATTR_FIND_WANT_END = 16
TS_ATTR_FIND_HIDDEN = 32
TS_VCOOKIE_NUL = 4294967295
TS_SHIFT_COUNT_HIDDEN = 1
TS_SHIFT_HALT_HIDDEN = 2
TS_SHIFT_HALT_VISIBLE = 4
TS_SHIFT_COUNT_ONLY = 8
TS_GTA_HIDDEN = 1
TS_GEA_HIDDEN = 1
TF_E_LOCKED = -2147220224
TF_E_STACKFULL = -2147220223
TF_E_NOTOWNEDRANGE = -2147220222
TF_E_NOPROVIDER = -2147220221
TF_E_DISCONNECTED = -2147220220
TF_E_INVALIDVIEW = -2147220219
TF_E_ALREADY_EXISTS = -2147220218
TF_E_RANGE_NOT_COVERED = -2147220217
TF_E_COMPOSITION_REJECTED = -2147220216
TF_E_EMPTYCONTEXT = -2147220215
TF_E_INVALIDPOS = -2147220992
TF_E_NOLOCK = -2147220991
TF_E_NOOBJECT = -2147220990
TF_E_NOSERVICE = -2147220989
TF_E_NOINTERFACE = -2147220988
TF_E_NOSELECTION = -2147220987
TF_E_NOLAYOUT = -2147220986
TF_E_INVALIDPOINT = -2147220985
TF_E_SYNCHRONOUS = -2147220984
TF_E_READONLY = -2147220983
TF_E_FORMAT = -2147220982
TF_S_ASYNC = 262912
TF_RCM_COMLESS = 1
TF_RCM_VKEY = 2
TF_RCM_HINT_READING_LENGTH = 4
TF_RCM_HINT_COLLISION = 8
TKB_ALTERNATES_STANDARD = 1
TKB_ALTERNATES_FOR_AUTOCORRECTION = 2
TKB_ALTERNATES_FOR_PREDICTION = 3
TKB_ALTERNATES_AUTOCORRECTION_APPLIED = 4
TF_TMAE_NOACTIVATETIP = 1
TF_TMAE_SECUREMODE = 2
TF_TMAE_UIELEMENTENABLEDONLY = 4
TF_TMAE_COMLESS = 8
TF_TMAE_WOW16 = 16
TF_TMAE_NOACTIVATEKEYBOARDLAYOUT = 32
TF_TMAE_CONSOLE = 64
TF_TMF_NOACTIVATETIP = 1
TF_TMF_SECUREMODE = 2
TF_TMF_UIELEMENTENABLEDONLY = 4
TF_TMF_COMLESS = 8
TF_TMF_WOW16 = 16
TF_TMF_CONSOLE = 64
TF_TMF_IMMERSIVEMODE = 1073741824
TF_TMF_ACTIVATED = 2147483648
TF_MOD_ALT = 1
TF_MOD_CONTROL = 2
TF_MOD_SHIFT = 4
TF_MOD_RALT = 8
TF_MOD_RCONTROL = 16
TF_MOD_RSHIFT = 32
TF_MOD_LALT = 64
TF_MOD_LCONTROL = 128
TF_MOD_LSHIFT = 256
TF_MOD_ON_KEYUP = 512
TF_MOD_IGNORE_ALL_MODIFIER = 1024
TF_US_HIDETIPUI = 1
TF_DISABLE_SPEECH = 1
TF_DISABLE_DICTATION = 2
TF_DISABLE_COMMANDING = 4
TF_PROCESS_ATOM = '_CTF_PROCESS_ATOM_'
TF_ENABLE_PROCESS_ATOM = '_CTF_ENABLE_PROCESS_ATOM_'
TF_CLUIE_DOCUMENTMGR = 1
TF_CLUIE_COUNT = 2
TF_CLUIE_SELECTION = 4
TF_CLUIE_STRING = 8
TF_CLUIE_PAGEINDEX = 16
TF_CLUIE_CURRENTPAGE = 32
TF_RIUIE_CONTEXT = 1
TF_RIUIE_STRING = 2
TF_RIUIE_MAXREADINGSTRINGLENGTH = 4
TF_RIUIE_ERRORINDEX = 8
TF_RIUIE_VERTICALORDER = 16
TF_CONVERSIONMODE_ALPHANUMERIC = 0
TF_CONVERSIONMODE_NATIVE = 1
TF_CONVERSIONMODE_KATAKANA = 2
TF_CONVERSIONMODE_FULLSHAPE = 8
TF_CONVERSIONMODE_ROMAN = 16
TF_CONVERSIONMODE_CHARCODE = 32
TF_CONVERSIONMODE_SOFTKEYBOARD = 128
TF_CONVERSIONMODE_NOCONVERSION = 256
TF_CONVERSIONMODE_EUDC = 512
TF_CONVERSIONMODE_SYMBOL = 1024
TF_CONVERSIONMODE_FIXED = 2048
TF_SENTENCEMODE_NONE = 0
TF_SENTENCEMODE_PLAURALCLAUSE = 1
TF_SENTENCEMODE_SINGLECONVERT = 2
TF_SENTENCEMODE_AUTOMATIC = 4
TF_SENTENCEMODE_PHRASEPREDICT = 8
TF_SENTENCEMODE_CONVERSATION = 16
TF_TRANSITORYEXTENSION_NONE = 0
TF_TRANSITORYEXTENSION_FLOATING = 1
TF_TRANSITORYEXTENSION_ATSELECTION = 2
TF_PROFILETYPE_INPUTPROCESSOR = 1
TF_PROFILETYPE_KEYBOARDLAYOUT = 2
TF_RIP_FLAG_FREEUNUSEDLIBRARIES = 1
TF_IPP_FLAG_ACTIVE = 1
TF_IPP_FLAG_ENABLED = 2
TF_IPP_FLAG_SUBSTITUTEDBYINPUTPROCESSOR = 4
TF_IPP_CAPS_DISABLEONTRANSITORY = 1
TF_IPP_CAPS_SECUREMODESUPPORT = 2
TF_IPP_CAPS_UIELEMENTENABLED = 4
TF_IPP_CAPS_COMLESSSUPPORT = 8
TF_IPP_CAPS_WOW16SUPPORT = 16
TF_IPP_CAPS_IMMERSIVESUPPORT = 65536
TF_IPP_CAPS_SYSTRAYSUPPORT = 131072
TF_IPPMF_FORPROCESS = 268435456
TF_IPPMF_FORSESSION = 536870912
TF_IPPMF_FORSYSTEMALL = 1073741824
TF_IPPMF_ENABLEPROFILE = 1
TF_IPPMF_DISABLEPROFILE = 2
TF_IPPMF_DONTCARECURRENTINPUTLANGUAGE = 4
TF_RP_HIDDENINSETTINGUI = 2
TF_RP_LOCALPROCESS = 4
TF_RP_LOCALTHREAD = 8
TF_RP_SUBITEMINSETTINGUI = 16
TF_URP_ALLPROFILES = 2
TF_URP_LOCALPROCESS = 4
TF_URP_LOCALTHREAD = 8
TF_IPSINK_FLAG_ACTIVE = 1
TF_INVALID_EDIT_COOKIE = 0
TF_POPF_ALL = 1
TF_SD_READONLY = 1
TF_SD_LOADING = 2
TF_SS_DISJOINTSEL = 1
TF_SS_REGIONS = 2
TF_SS_TRANSITORY = 4
TF_SS_TKBAUTOCORRECTENABLE = 16
TF_SS_TKBPREDICTIONENABLE = 32
TF_CHAR_EMBEDDED = 65532
TF_HF_OBJECT = 1
TF_TF_MOVESTART = 1
TF_TF_IGNOREEND = 2
TF_ST_CORRECTION = 1
TF_IE_CORRECTION = 1
TF_TU_CORRECTION = 1
TF_INVALID_COOKIE = 4294967295
def _define_TF_PROFILE_NEWPHONETIC():
    return Guid('b2f9c502-1742-11d4-97-90-00-80-c8-82-68-7e')
def _define_TF_PROFILE_PHONETIC():
    return Guid('761309de-317a-11d4-9b-5d-00-80-c8-82-68-7e')
def _define_TF_PROFILE_NEWCHANGJIE():
    return Guid('f3ba907a-6c7e-11d4-97-fa-00-80-c8-82-68-7e')
def _define_TF_PROFILE_CHANGJIE():
    return Guid('4bdf9f03-c7d3-11d4-b2-ab-00-80-c8-82-68-7e')
def _define_TF_PROFILE_NEWQUICK():
    return Guid('0b883ba0-c1c7-11d4-87-f9-00-80-c8-82-68-7e')
def _define_TF_PROFILE_QUICK():
    return Guid('6024b45f-5c54-11d4-b9-21-00-80-c8-82-68-7e')
def _define_TF_PROFILE_CANTONESE():
    return Guid('0aec109c-7e96-11d4-b2-ef-00-80-c8-82-68-7e')
def _define_TF_PROFILE_PINYIN():
    return Guid('f3ba9077-6c7e-11d4-97-fa-00-80-c8-82-68-7e')
def _define_TF_PROFILE_SIMPLEFAST():
    return Guid('fa550b04-5ad7-411f-a5-ac-ca-03-8e-c5-15-d7')
def _define_TF_PROFILE_WUBI():
    return Guid('82590c13-f4dd-44f4-ba-1d-86-67-24-6f-df-8e')
def _define_TF_PROFILE_DAYI():
    return Guid('037b2c25-480c-4d7f-b0-27-d6-ca-6b-69-78-8a')
def _define_TF_PROFILE_ARRAY():
    return Guid('d38eff65-aa46-4fd5-91-a7-67-84-5f-b0-2f-5b')
def _define_TF_PROFILE_YI():
    return Guid('409c8376-007b-4357-ae-8e-26-31-6e-e3-fb-0d')
def _define_TF_PROFILE_TIGRINYA():
    return Guid('3cab88b7-cc3e-46a6-97-65-b7-72-ad-77-61-ff')
TF_E_NOCONVERSION = -2147219968
TF_DICTATION_ON = 1
TF_DICTATION_ENABLED = 2
TF_COMMANDING_ENABLED = 4
TF_COMMANDING_ON = 8
TF_SPEECHUI_SHOWN = 16
TF_SHOW_BALLOON = 1
TF_DISABLE_BALLOON = 2
TF_MENUREADY = 1
TF_PROPUI_STATUS_SAVETOFILE = 1
def _define_GUID_INTEGRATIONSTYLE_SEARCHBOX():
    return Guid('e6d1bd11-82f7-4903-ae-21-1a-63-97-cd-e2-eb')
TKBL_UNDEFINED = 0
TKBL_CLASSIC_TRADITIONAL_CHINESE_PHONETIC = 1028
TKBL_CLASSIC_TRADITIONAL_CHINESE_CHANGJIE = 61506
TKBL_CLASSIC_TRADITIONAL_CHINESE_DAYI = 61507
TKBL_OPT_JAPANESE_ABC = 1041
TKBL_OPT_KOREAN_HANGUL_2_BULSIK = 1042
TKBL_OPT_SIMPLIFIED_CHINESE_PINYIN = 2052
TKBL_OPT_TRADITIONAL_CHINESE_PHONETIC = 1028
TF_FLOATINGLANGBAR_WNDTITLEW = 'TF_FloatingLangBar_WndTitle'
TF_FLOATINGLANGBAR_WNDTITLEA = 'TF_FloatingLangBar_WndTitle'
TF_FLOATINGLANGBAR_WNDTITLE = 'TF_FloatingLangBar_WndTitle'
TF_LBI_ICON = 1
TF_LBI_TEXT = 2
TF_LBI_TOOLTIP = 4
TF_LBI_BITMAP = 8
TF_LBI_BALLOON = 16
TF_LBI_CUSTOMUI = 32
TF_LBI_STATUS = 65536
TF_LBI_STYLE_HIDDENSTATUSCONTROL = 1
TF_LBI_STYLE_SHOWNINTRAY = 2
TF_LBI_STYLE_HIDEONNOOTHERITEMS = 4
TF_LBI_STYLE_SHOWNINTRAYONLY = 8
TF_LBI_STYLE_HIDDENBYDEFAULT = 16
TF_LBI_STYLE_TEXTCOLORICON = 32
TF_LBI_STYLE_BTN_BUTTON = 65536
TF_LBI_STYLE_BTN_MENU = 131072
TF_LBI_STYLE_BTN_TOGGLE = 262144
TF_LBI_STATUS_HIDDEN = 1
TF_LBI_STATUS_DISABLED = 2
TF_LBI_STATUS_BTN_TOGGLED = 65536
TF_LBI_BMPF_VERTICAL = 1
TF_SFT_SHOWNORMAL = 1
TF_SFT_DOCK = 2
TF_SFT_MINIMIZED = 4
TF_SFT_HIDDEN = 8
TF_SFT_NOTRANSPARENCY = 16
TF_SFT_LOWTRANSPARENCY = 32
TF_SFT_HIGHTRANSPARENCY = 64
TF_SFT_LABELS = 128
TF_SFT_NOLABELS = 256
TF_SFT_EXTRAICONSONMINIMIZED = 512
TF_SFT_NOEXTRAICONSONMINIMIZED = 1024
TF_SFT_DESKBAND = 2048
TF_LBI_DESC_MAXLEN = 32
TF_LBMENUF_CHECKED = 1
TF_LBMENUF_SUBMENU = 2
TF_LBMENUF_SEPARATOR = 4
TF_LBMENUF_RADIOCHECKED = 8
TF_LBMENUF_GRAYED = 16
def _define_GUID_PROP_INPUTSCOPE():
    return Guid('1713dd5a-68e7-4a5b-9a-f6-59-2a-59-5c-77-8d')
DCM_FLAGS_TASKENG = 1
DCM_FLAGS_CTFMON = 2
DCM_FLAGS_LOCALTHREADTSF = 4
ILMCM_CHECKLAYOUTANDTIPENABLED = 1
ILMCM_LANGUAGEBAROFF = 2
def _define_LIBID_MSAATEXTLib():
    return Guid('150e2d7a-dac1-4582-94-7d-2a-8f-d7-8b-82-cd')
TS_STRF_START = 0
TS_STRF_MID = 1
TS_STRF_END = 2
def _define_TSATTRID_OTHERS():
    return Guid('b3c32af9-57d0-46a9-bc-a8-da-c2-38-a1-30-57')
def _define_TSATTRID_Font():
    return Guid('573ea825-749b-4f8a-9c-fd-21-c3-60-5c-a8-28')
def _define_TSATTRID_Font_FaceName():
    return Guid('b536aeb6-053b-4eb8-b6-5a-50-da-1e-81-e7-2e')
def _define_TSATTRID_Font_SizePts():
    return Guid('c8493302-a5e9-456d-af-04-80-05-e4-13-0f-03')
def _define_TSATTRID_Font_Style():
    return Guid('68b2a77f-6b0e-4f28-81-77-57-1c-2f-3a-42-b1')
def _define_TSATTRID_Font_Style_Bold():
    return Guid('48813a43-8a20-4940-8e-58-97-82-3f-7b-26-8a')
def _define_TSATTRID_Font_Style_Italic():
    return Guid('8740682a-a765-48e1-ac-fc-d2-22-22-b2-f8-10')
def _define_TSATTRID_Font_Style_SmallCaps():
    return Guid('facb6bc6-9100-4cc6-b9-69-11-ee-a4-5a-86-b4')
def _define_TSATTRID_Font_Style_Capitalize():
    return Guid('7d85a3ba-b4fd-43b3-be-fc-6b-98-5c-84-31-41')
def _define_TSATTRID_Font_Style_Uppercase():
    return Guid('33a300e8-e340-4937-b6-97-8f-23-40-45-cd-9a')
def _define_TSATTRID_Font_Style_Lowercase():
    return Guid('76d8ccb5-ca7b-4498-8e-e9-d5-c4-f6-f7-4c-60')
def _define_TSATTRID_Font_Style_Animation():
    return Guid('dcf73d22-e029-47b7-bb-36-f2-63-a3-d0-04-cc')
def _define_TSATTRID_Font_Style_Animation_LasVegasLights():
    return Guid('f40423d5-0f87-4f8f-ba-da-e6-d6-0c-25-e1-52')
def _define_TSATTRID_Font_Style_Animation_BlinkingBackground():
    return Guid('86e5b104-0104-4b10-b5-85-00-f2-52-75-22-b5')
def _define_TSATTRID_Font_Style_Animation_SparkleText():
    return Guid('533aad20-962c-4e9f-8c-09-b4-2e-a4-74-97-11')
def _define_TSATTRID_Font_Style_Animation_MarchingBlackAnts():
    return Guid('7644e067-f186-4902-bf-c6-ec-81-5a-a2-0e-9d')
def _define_TSATTRID_Font_Style_Animation_MarchingRedAnts():
    return Guid('78368dad-50fb-4c6f-84-0b-d4-86-bb-6c-f7-81')
def _define_TSATTRID_Font_Style_Animation_Shimmer():
    return Guid('2ce31b58-5293-4c36-88-09-bf-8b-b5-1a-27-b3')
def _define_TSATTRID_Font_Style_Animation_WipeDown():
    return Guid('5872e874-367b-4803-b1-60-c9-0f-f6-25-69-d0')
def _define_TSATTRID_Font_Style_Animation_WipeRight():
    return Guid('b855cbe3-3d2c-4600-b1-e9-e1-c9-ce-02-f8-42')
def _define_TSATTRID_Font_Style_Emboss():
    return Guid('bd8ed742-349e-4e37-82-fb-43-79-79-cb-53-a7')
def _define_TSATTRID_Font_Style_Engrave():
    return Guid('9c3371de-8332-4897-be-5d-89-23-32-23-17-9a')
def _define_TSATTRID_Font_Style_Hidden():
    return Guid('b1e28770-881c-475f-86-3f-88-7a-64-7b-10-90')
def _define_TSATTRID_Font_Style_Kerning():
    return Guid('cc26e1b4-2f9a-47c8-8b-ff-bf-1e-b7-cc-e0-dd')
def _define_TSATTRID_Font_Style_Outlined():
    return Guid('10e6db31-db0d-4ac6-a7-f5-9c-9c-ff-6f-2a-b4')
def _define_TSATTRID_Font_Style_Position():
    return Guid('15cd26ab-f2fb-4062-b5-a6-9a-49-e1-a5-cc-0b')
def _define_TSATTRID_Font_Style_Protected():
    return Guid('1c557cb2-14cf-4554-a5-74-ec-b2-f7-e7-ef-d4')
def _define_TSATTRID_Font_Style_Shadow():
    return Guid('5f686d2f-c6cd-4c56-8a-1a-99-4a-4b-97-66-be')
def _define_TSATTRID_Font_Style_Spacing():
    return Guid('98c1200d-8f06-409a-8e-49-6a-55-4b-f7-c1-53')
def _define_TSATTRID_Font_Style_Weight():
    return Guid('12f3189c-8bb0-461b-b1-fa-ea-f9-07-04-7f-e0')
def _define_TSATTRID_Font_Style_Height():
    return Guid('7e937477-12e6-458b-92-6a-1f-a4-4e-e8-f3-91')
def _define_TSATTRID_Font_Style_Underline():
    return Guid('c3c9c9f3-7902-444b-9a-7b-48-e7-0f-4b-50-f7')
def _define_TSATTRID_Font_Style_Underline_Single():
    return Guid('1b6720e5-0f73-4951-a6-b3-6f-19-e4-3c-94-61')
def _define_TSATTRID_Font_Style_Underline_Double():
    return Guid('74d24aa6-1db3-4c69-a1-76-31-12-0e-75-86-d5')
def _define_TSATTRID_Font_Style_Strikethrough():
    return Guid('0c562193-2d08-4668-96-01-ce-d4-13-09-d7-af')
def _define_TSATTRID_Font_Style_Strikethrough_Single():
    return Guid('75d736b6-3c8f-4b97-ab-78-18-77-cb-99-0d-31')
def _define_TSATTRID_Font_Style_Strikethrough_Double():
    return Guid('62489b31-a3e7-4f94-ac-43-eb-af-8f-cc-7a-9f')
def _define_TSATTRID_Font_Style_Overline():
    return Guid('e3989f4a-992b-4301-8c-e1-a5-b7-c6-d1-f3-c8')
def _define_TSATTRID_Font_Style_Overline_Single():
    return Guid('8440d94c-51ce-47b2-8d-4c-15-75-1e-5f-72-1b')
def _define_TSATTRID_Font_Style_Overline_Double():
    return Guid('dc46063a-e115-46e3-bc-d8-ca-67-72-aa-95-b4')
def _define_TSATTRID_Font_Style_Blink():
    return Guid('bfb2c036-7acf-4532-b7-20-b4-16-dd-77-65-a8')
def _define_TSATTRID_Font_Style_Subscript():
    return Guid('5774fb84-389b-43bc-a7-4b-15-68-34-7c-f0-f4')
def _define_TSATTRID_Font_Style_Superscript():
    return Guid('2ea4993c-563c-49aa-93-72-0b-ef-09-a9-25-5b')
def _define_TSATTRID_Font_Style_Color():
    return Guid('857a7a37-b8af-4e9a-81-b4-ac-f7-00-c8-41-1b')
def _define_TSATTRID_Font_Style_BackgroundColor():
    return Guid('b50eaa4e-3091-4468-81-db-d7-9e-a1-90-c7-c7')
def _define_TSATTRID_Text():
    return Guid('7edb8e68-81f9-449d-a1-5a-87-a8-38-8f-aa-c0')
def _define_TSATTRID_Text_VerticalWriting():
    return Guid('6bba8195-046f-4ea9-b3-11-97-fd-66-c4-27-4b')
def _define_TSATTRID_Text_RightToLeft():
    return Guid('ca666e71-1b08-453d-bf-dd-28-e0-8c-8a-af-7a')
def _define_TSATTRID_Text_Orientation():
    return Guid('6bab707f-8785-4c39-8b-52-96-f8-78-30-3f-fb')
def _define_TSATTRID_Text_Language():
    return Guid('d8c04ef1-5753-4c25-88-87-85-44-3f-e5-f8-19')
def _define_TSATTRID_Text_ReadOnly():
    return Guid('85836617-de32-4afd-a5-0f-a2-db-11-0e-6e-4d')
def _define_TSATTRID_Text_EmbeddedObject():
    return Guid('7edb8e68-81f9-449d-a1-5a-87-a8-38-8f-aa-c0')
def _define_TSATTRID_Text_Alignment():
    return Guid('139941e6-1767-456d-93-8e-35-ba-56-8b-5c-d4')
def _define_TSATTRID_Text_Alignment_Left():
    return Guid('16ae95d3-6361-43a2-84-95-d0-0f-39-7f-16-93')
def _define_TSATTRID_Text_Alignment_Right():
    return Guid('b36f0f98-1b9e-4360-86-16-03-fb-08-a7-84-56')
def _define_TSATTRID_Text_Alignment_Center():
    return Guid('a4a95c16-53bf-4d55-8b-87-4b-dd-8d-42-75-fc')
def _define_TSATTRID_Text_Alignment_Justify():
    return Guid('ed350740-a0f7-42d3-8e-a8-f8-1b-64-88-fa-f0')
def _define_TSATTRID_Text_Link():
    return Guid('47cd9051-3722-4cd8-b7-c8-4e-17-ca-17-59-f5')
def _define_TSATTRID_Text_Hyphenation():
    return Guid('dadf4525-618e-49eb-b1-a8-3b-68-bd-76-48-e3')
def _define_TSATTRID_Text_Para():
    return Guid('5edc5822-99dc-4dd6-ae-c3-b6-2b-aa-5b-2e-7c')
def _define_TSATTRID_Text_Para_FirstLineIndent():
    return Guid('07c97a13-7472-4dd8-90-a9-91-e3-d7-e4-f2-9c')
def _define_TSATTRID_Text_Para_LeftIndent():
    return Guid('fb2848e9-7471-41c9-b6-b3-8a-14-50-e0-18-97')
def _define_TSATTRID_Text_Para_RightIndent():
    return Guid('2c7f26f9-a5e2-48da-b9-8a-52-0c-b1-65-13-bf')
def _define_TSATTRID_Text_Para_SpaceAfter():
    return Guid('7b0a3f55-22dc-425f-a4-11-93-da-1d-8f-9b-aa')
def _define_TSATTRID_Text_Para_SpaceBefore():
    return Guid('8df98589-194a-4601-b2-51-98-65-a3-e9-06-dd')
def _define_TSATTRID_Text_Para_LineSpacing():
    return Guid('699b380d-7f8c-46d6-a7-3b-df-e3-d1-53-8d-f3')
def _define_TSATTRID_Text_Para_LineSpacing_Single():
    return Guid('ed350740-a0f7-42d3-8e-a8-f8-1b-64-88-fa-f0')
def _define_TSATTRID_Text_Para_LineSpacing_OnePtFive():
    return Guid('0428a021-0397-4b57-9a-17-07-95-99-4c-d3-c5')
def _define_TSATTRID_Text_Para_LineSpacing_Double():
    return Guid('82fb1805-a6c4-4231-ac-12-62-60-af-2a-ba-28')
def _define_TSATTRID_Text_Para_LineSpacing_AtLeast():
    return Guid('adfedf31-2d44-4434-a5-ff-7f-4c-49-90-a9-05')
def _define_TSATTRID_Text_Para_LineSpacing_Exactly():
    return Guid('3d45ad40-23de-48d7-a6-b3-76-54-20-c6-20-cc')
def _define_TSATTRID_Text_Para_LineSpacing_Multiple():
    return Guid('910f1e3c-d6d0-4f65-8a-3c-42-b4-b3-18-68-c5')
def _define_TSATTRID_List():
    return Guid('436d673b-26f1-4aee-9e-65-8f-83-a4-ed-48-84')
def _define_TSATTRID_List_LevelIndel():
    return Guid('7f7cc899-311f-487b-ad-5d-e2-a4-59-e1-2d-42')
def _define_TSATTRID_List_Type():
    return Guid('ae3e665e-4bce-49e3-a0-fe-2d-b4-7d-3a-17-ae')
def _define_TSATTRID_List_Type_Bullet():
    return Guid('bccd77c5-4c4d-4ce2-b1-02-55-9f-3b-2b-fc-ea')
def _define_TSATTRID_List_Type_Arabic():
    return Guid('1338c5d6-98a3-4fa3-9b-d1-7a-60-ee-f8-e9-e0')
def _define_TSATTRID_List_Type_LowerLetter():
    return Guid('96372285-f3cf-491e-a9-25-38-32-34-7f-d2-37')
def _define_TSATTRID_List_Type_UpperLetter():
    return Guid('7987b7cd-ce52-428b-9b-95-a3-57-f6-f1-0c-45')
def _define_TSATTRID_List_Type_LowerRoman():
    return Guid('90466262-3980-4b8e-93-68-91-8b-d1-21-8a-41')
def _define_TSATTRID_List_Type_UpperRoman():
    return Guid('0f6ab552-4a80-467f-b2-f1-12-7e-2a-a3-ba-9e')
def _define_TSATTRID_App():
    return Guid('a80f77df-4237-40e5-84-9c-b5-fa-51-c1-3a-c7')
def _define_TSATTRID_App_IncorrectSpelling():
    return Guid('f42de43c-ef12-430d-94-4c-9a-08-97-0a-25-d2')
def _define_TSATTRID_App_IncorrectGrammar():
    return Guid('bd54e398-ad03-4b74-b6-b3-5e-db-19-99-63-88')
def _define_DoMsCtfMonitor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.HANDLE)(('DoMsCtfMonitor', windll['MsCtfMonitor.dll']), ((1, 'dwFlags'),(1, 'hEventForServiceStop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitLocalMsCtfMonitor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(('InitLocalMsCtfMonitor', windll['MsCtfMonitor.dll']), ((1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UninitLocalMsCtfMonitor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('UninitLocalMsCtfMonitor', windll['MsCtfMonitor.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
DocWrap = Guid('bf426f7e-7a5e-44d6-83-0c-a3-90-ea-94-62-a3')
GET_TEXT_AND_PROPERTY_UPDATES_FLAGS = UInt32
TF_GTP_NONE = 0
TF_GTP_INCL_TEXT = 1
HKL = IntPtr
def _define_IAccClientDocMgr_head():
    class IAccClientDocMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('4c896039-7b6d-49e6-a8-c1-45-11-6a-98-29-2b')
    return IAccClientDocMgr
def _define_IAccClientDocMgr():
    IAccClientDocMgr = win32more.UI.TextServices.IAccClientDocMgr_head
    IAccClientDocMgr.GetDocuments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumUnknown_head))(3, 'GetDocuments', ((1, 'enumUnknown'),)))
    IAccClientDocMgr.LookupByHWND = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(4, 'LookupByHWND', ((1, 'hWnd'),(1, 'riid'),(1, 'ppunk'),)))
    IAccClientDocMgr.LookupByPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(5, 'LookupByPoint', ((1, 'pt'),(1, 'riid'),(1, 'ppunk'),)))
    IAccClientDocMgr.GetFocused = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(6, 'GetFocused', ((1, 'riid'),(1, 'ppunk'),)))
    win32more.System.Com.IUnknown
    return IAccClientDocMgr
def _define_IAccDictionary_head():
    class IAccDictionary(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dc4cb5f-d737-474d-ad-e9-5c-cf-c9-bc-1c-c9')
    return IAccDictionary
def _define_IAccDictionary():
    IAccDictionary = win32more.UI.TextServices.IAccDictionary_head
    IAccDictionary.GetLocalizedString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.Foundation.BSTR),POINTER(UInt32))(3, 'GetLocalizedString', ((1, 'Term'),(1, 'lcid'),(1, 'pResult'),(1, 'plcid'),)))
    IAccDictionary.GetParentTerm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid))(4, 'GetParentTerm', ((1, 'Term'),(1, 'pParentTerm'),)))
    IAccDictionary.GetMnemonicString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.BSTR))(5, 'GetMnemonicString', ((1, 'Term'),(1, 'pResult'),)))
    IAccDictionary.LookupMnemonicTerm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Guid))(6, 'LookupMnemonicTerm', ((1, 'bstrMnemonic'),(1, 'pTerm'),)))
    IAccDictionary.ConvertValueToString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR),POINTER(UInt32))(7, 'ConvertValueToString', ((1, 'Term'),(1, 'lcid'),(1, 'varValue'),(1, 'pbstrResult'),(1, 'plcid'),)))
    win32more.System.Com.IUnknown
    return IAccDictionary
def _define_IAccServerDocMgr_head():
    class IAccServerDocMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('ad7c73cf-6dd5-4855-ab-c2-b0-4b-ad-5b-91-53')
    return IAccServerDocMgr
def _define_IAccServerDocMgr():
    IAccServerDocMgr = win32more.UI.TextServices.IAccServerDocMgr_head
    IAccServerDocMgr.NewDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head)(3, 'NewDocument', ((1, 'riid'),(1, 'punk'),)))
    IAccServerDocMgr.RevokeDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(4, 'RevokeDocument', ((1, 'punk'),)))
    IAccServerDocMgr.OnDocumentFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(5, 'OnDocumentFocus', ((1, 'punk'),)))
    win32more.System.Com.IUnknown
    return IAccServerDocMgr
def _define_IAccStore_head():
    class IAccStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('e2cd4a63-2b72-4d48-b7-39-95-e4-76-51-95-ba')
    return IAccStore
def _define_IAccStore():
    IAccStore = win32more.UI.TextServices.IAccStore_head
    IAccStore.Register = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head)(3, 'Register', ((1, 'riid'),(1, 'punk'),)))
    IAccStore.Unregister = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(4, 'Unregister', ((1, 'punk'),)))
    IAccStore.GetDocuments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumUnknown_head))(5, 'GetDocuments', ((1, 'enumUnknown'),)))
    IAccStore.LookupByHWND = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(6, 'LookupByHWND', ((1, 'hWnd'),(1, 'riid'),(1, 'ppunk'),)))
    IAccStore.LookupByPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(7, 'LookupByPoint', ((1, 'pt'),(1, 'riid'),(1, 'ppunk'),)))
    IAccStore.OnDocumentFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(8, 'OnDocumentFocus', ((1, 'punk'),)))
    IAccStore.GetFocused = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(9, 'GetFocused', ((1, 'riid'),(1, 'ppunk'),)))
    win32more.System.Com.IUnknown
    return IAccStore
def _define_IAnchor_head():
    class IAnchor(win32more.System.Com.IUnknown_head):
        Guid = Guid('0feb7e34-5a60-4356-8e-f7-ab-de-c2-ff-7c-f8')
    return IAnchor
def _define_IAnchor():
    IAnchor = win32more.UI.TextServices.IAnchor_head
    IAnchor.SetGravity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TsGravity)(3, 'SetGravity', ((1, 'gravity'),)))
    IAnchor.GetGravity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TsGravity))(4, 'GetGravity', ((1, 'pgravity'),)))
    IAnchor.IsEqual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,POINTER(win32more.Foundation.BOOL))(5, 'IsEqual', ((1, 'paWith'),(1, 'pfEqual'),)))
    IAnchor.Compare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,POINTER(Int32))(6, 'Compare', ((1, 'paWith'),(1, 'plResult'),)))
    IAnchor.Shift = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,POINTER(Int32),win32more.UI.TextServices.IAnchor_head)(7, 'Shift', ((1, 'dwFlags'),(1, 'cchReq'),(1, 'pcch'),(1, 'paHaltAnchor'),)))
    IAnchor.ShiftTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head)(8, 'ShiftTo', ((1, 'paSite'),)))
    IAnchor.ShiftRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.TsShiftDir,POINTER(win32more.Foundation.BOOL))(9, 'ShiftRegion', ((1, 'dwFlags'),(1, 'dir'),(1, 'pfNoRegion'),)))
    IAnchor.SetChangeHistoryMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(10, 'SetChangeHistoryMask', ((1, 'dwMask'),)))
    IAnchor.GetChangeHistory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ANCHOR_CHANGE_HISTORY_FLAGS))(11, 'GetChangeHistory', ((1, 'pdwHistory'),)))
    IAnchor.ClearChangeHistory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'ClearChangeHistory', ()))
    IAnchor.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IAnchor_head))(13, 'Clone', ((1, 'ppaClone'),)))
    win32more.System.Com.IUnknown
    return IAnchor
def _define_IClonableWrapper_head():
    class IClonableWrapper(win32more.System.Com.IUnknown_head):
        Guid = Guid('b33e75ff-e84c-4dca-a2-5c-33-b8-dc-00-33-74')
    return IClonableWrapper
def _define_IClonableWrapper():
    IClonableWrapper = win32more.UI.TextServices.IClonableWrapper_head
    IClonableWrapper.CloneNewWrapper = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(3, 'CloneNewWrapper', ((1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return IClonableWrapper
def _define_ICoCreatedLocally_head():
    class ICoCreatedLocally(win32more.System.Com.IUnknown_head):
        Guid = Guid('0a53eb6c-1908-4742-8c-ff-2c-ee-2e-93-f9-4c')
    return ICoCreatedLocally
def _define_ICoCreatedLocally():
    ICoCreatedLocally = win32more.UI.TextServices.ICoCreatedLocally_head
    ICoCreatedLocally.LocalInit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),win32more.System.Com.IUnknown_head,win32more.System.Com.VARIANT)(3, 'LocalInit', ((1, 'punkLocalObject'),(1, 'riidParam'),(1, 'punkParam'),(1, 'varParam'),)))
    win32more.System.Com.IUnknown
    return ICoCreatedLocally
def _define_ICoCreateLocally_head():
    class ICoCreateLocally(win32more.System.Com.IUnknown_head):
        Guid = Guid('03de00aa-f272-41e3-99-cb-03-c5-e8-11-4e-a0')
    return ICoCreateLocally
def _define_ICoCreateLocally():
    ICoCreateLocally = win32more.UI.TextServices.ICoCreateLocally_head
    ICoCreateLocally.CoCreateLocally = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head),POINTER(Guid),win32more.System.Com.IUnknown_head,win32more.System.Com.VARIANT)(3, 'CoCreateLocally', ((1, 'rclsid'),(1, 'dwClsContext'),(1, 'riid'),(1, 'punk'),(1, 'riidParam'),(1, 'punkParam'),(1, 'varParam'),)))
    win32more.System.Com.IUnknown
    return ICoCreateLocally
def _define_IDocWrap_head():
    class IDocWrap(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcd285fe-0be0-43bd-99-c9-aa-ae-c5-13-c5-55')
    return IDocWrap
def _define_IDocWrap():
    IDocWrap = win32more.UI.TextServices.IDocWrap_head
    IDocWrap.SetDoc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head)(3, 'SetDoc', ((1, 'riid'),(1, 'punk'),)))
    IDocWrap.GetWrappedDoc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(4, 'GetWrappedDoc', ((1, 'riid'),(1, 'ppunk'),)))
    win32more.System.Com.IUnknown
    return IDocWrap
def _define_IEnumITfCompositionView_head():
    class IEnumITfCompositionView(win32more.System.Com.IUnknown_head):
        Guid = Guid('5efd22ba-7838-46cb-88-e2-ca-db-14-12-4f-8f')
    return IEnumITfCompositionView
def _define_IEnumITfCompositionView():
    IEnumITfCompositionView = win32more.UI.TextServices.IEnumITfCompositionView_head
    IEnumITfCompositionView.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumITfCompositionView_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumITfCompositionView.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfCompositionView_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'rgCompositionView'),(1, 'pcFetched'),)))
    IEnumITfCompositionView.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumITfCompositionView.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumITfCompositionView
def _define_IEnumSpeechCommands_head():
    class IEnumSpeechCommands(win32more.System.Com.IUnknown_head):
        Guid = Guid('8c5dac4f-083c-4b85-a4-c9-71-74-60-48-ad-ca')
    return IEnumSpeechCommands
def _define_IEnumSpeechCommands():
    IEnumSpeechCommands = win32more.UI.TextServices.IEnumSpeechCommands_head
    IEnumSpeechCommands.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumSpeechCommands_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumSpeechCommands.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(UInt16)),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'pSpCmds'),(1, 'pcFetched'),)))
    IEnumSpeechCommands.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumSpeechCommands.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumSpeechCommands
def _define_IEnumTfCandidates_head():
    class IEnumTfCandidates(win32more.System.Com.IUnknown_head):
        Guid = Guid('defb1926-6c80-4ce8-87-d4-d6-b7-2b-81-2b-de')
    return IEnumTfCandidates
def _define_IEnumTfCandidates():
    IEnumTfCandidates = win32more.UI.TextServices.IEnumTfCandidates_head
    IEnumTfCandidates.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfCandidates_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfCandidates.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfCandidateString_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'ppCand'),(1, 'pcFetched'),)))
    IEnumTfCandidates.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfCandidates.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfCandidates
def _define_IEnumTfContexts_head():
    class IEnumTfContexts(win32more.System.Com.IUnknown_head):
        Guid = Guid('8f1a7ea6-1654-4502-a8-6e-b2-90-23-44-d5-07')
    return IEnumTfContexts
def _define_IEnumTfContexts():
    IEnumTfContexts = win32more.UI.TextServices.IEnumTfContexts_head
    IEnumTfContexts.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfContexts_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfContexts.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfContext_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'rgContext'),(1, 'pcFetched'),)))
    IEnumTfContexts.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfContexts.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfContexts
def _define_IEnumTfContextViews_head():
    class IEnumTfContextViews(win32more.System.Com.IUnknown_head):
        Guid = Guid('f0c0f8dd-cf38-44e1-bb-0f-68-cf-0d-55-1c-78')
    return IEnumTfContextViews
def _define_IEnumTfContextViews():
    IEnumTfContextViews = win32more.UI.TextServices.IEnumTfContextViews_head
    IEnumTfContextViews.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfContextViews_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfContextViews.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfContextView_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'rgViews'),(1, 'pcFetched'),)))
    IEnumTfContextViews.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfContextViews.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfContextViews
def _define_IEnumTfDisplayAttributeInfo_head():
    class IEnumTfDisplayAttributeInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('7cef04d7-cb75-4e80-a7-ab-5f-5b-c7-d3-32-de')
    return IEnumTfDisplayAttributeInfo
def _define_IEnumTfDisplayAttributeInfo():
    IEnumTfDisplayAttributeInfo = win32more.UI.TextServices.IEnumTfDisplayAttributeInfo_head
    IEnumTfDisplayAttributeInfo.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfDisplayAttributeInfo_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfDisplayAttributeInfo.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfDisplayAttributeInfo_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'rgInfo'),(1, 'pcFetched'),)))
    IEnumTfDisplayAttributeInfo.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfDisplayAttributeInfo.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfDisplayAttributeInfo
def _define_IEnumTfDocumentMgrs_head():
    class IEnumTfDocumentMgrs(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e808-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    return IEnumTfDocumentMgrs
def _define_IEnumTfDocumentMgrs():
    IEnumTfDocumentMgrs = win32more.UI.TextServices.IEnumTfDocumentMgrs_head
    IEnumTfDocumentMgrs.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfDocumentMgrs_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfDocumentMgrs.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'rgDocumentMgr'),(1, 'pcFetched'),)))
    IEnumTfDocumentMgrs.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfDocumentMgrs.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfDocumentMgrs
def _define_IEnumTfFunctionProviders_head():
    class IEnumTfFunctionProviders(win32more.System.Com.IUnknown_head):
        Guid = Guid('e4b24db0-0990-11d3-8d-f0-00-10-5a-27-99-b5')
    return IEnumTfFunctionProviders
def _define_IEnumTfFunctionProviders():
    IEnumTfFunctionProviders = win32more.UI.TextServices.IEnumTfFunctionProviders_head
    IEnumTfFunctionProviders.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfFunctionProviders_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfFunctionProviders.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfFunctionProvider_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'ppCmdobj'),(1, 'pcFetch'),)))
    IEnumTfFunctionProviders.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfFunctionProviders.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfFunctionProviders
def _define_IEnumTfInputProcessorProfiles_head():
    class IEnumTfInputProcessorProfiles(win32more.System.Com.IUnknown_head):
        Guid = Guid('71c6e74d-0f28-11d8-a8-2a-00-06-5b-84-43-5c')
    return IEnumTfInputProcessorProfiles
def _define_IEnumTfInputProcessorProfiles():
    IEnumTfInputProcessorProfiles = win32more.UI.TextServices.IEnumTfInputProcessorProfiles_head
    IEnumTfInputProcessorProfiles.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfInputProcessorProfiles_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfInputProcessorProfiles.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TF_INPUTPROCESSORPROFILE_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'pProfile'),(1, 'pcFetch'),)))
    IEnumTfInputProcessorProfiles.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfInputProcessorProfiles.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfInputProcessorProfiles
def _define_IEnumTfLangBarItems_head():
    class IEnumTfLangBarItems(win32more.System.Com.IUnknown_head):
        Guid = Guid('583f34d0-de25-11d2-af-dd-00-10-5a-27-99-b5')
    return IEnumTfLangBarItems
def _define_IEnumTfLangBarItems():
    IEnumTfLangBarItems = win32more.UI.TextServices.IEnumTfLangBarItems_head
    IEnumTfLangBarItems.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfLangBarItems_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfLangBarItems.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfLangBarItem_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'ppItem'),(1, 'pcFetched'),)))
    IEnumTfLangBarItems.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfLangBarItems.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfLangBarItems
def _define_IEnumTfLanguageProfiles_head():
    class IEnumTfLanguageProfiles(win32more.System.Com.IUnknown_head):
        Guid = Guid('3d61bf11-ac5f-42c8-a4-cb-93-1b-cc-28-c7-44')
    return IEnumTfLanguageProfiles
def _define_IEnumTfLanguageProfiles():
    IEnumTfLanguageProfiles = win32more.UI.TextServices.IEnumTfLanguageProfiles_head
    IEnumTfLanguageProfiles.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfLanguageProfiles_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfLanguageProfiles.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TF_LANGUAGEPROFILE_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'pProfile'),(1, 'pcFetch'),)))
    IEnumTfLanguageProfiles.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfLanguageProfiles.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfLanguageProfiles
def _define_IEnumTfLatticeElements_head():
    class IEnumTfLatticeElements(win32more.System.Com.IUnknown_head):
        Guid = Guid('56988052-47da-4a05-91-1a-e3-d9-41-f1-71-45')
    return IEnumTfLatticeElements
def _define_IEnumTfLatticeElements():
    IEnumTfLatticeElements = win32more.UI.TextServices.IEnumTfLatticeElements_head
    IEnumTfLatticeElements.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfLatticeElements_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfLatticeElements.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TF_LMLATTELEMENT_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'rgsElements'),(1, 'pcFetched'),)))
    IEnumTfLatticeElements.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfLatticeElements.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfLatticeElements
def _define_IEnumTfProperties_head():
    class IEnumTfProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('19188cb0-aca9-11d2-af-c5-00-10-5a-27-99-b5')
    return IEnumTfProperties
def _define_IEnumTfProperties():
    IEnumTfProperties = win32more.UI.TextServices.IEnumTfProperties_head
    IEnumTfProperties.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfProperties_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfProperties.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfProperty_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'ppProp'),(1, 'pcFetched'),)))
    IEnumTfProperties.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfProperties.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfProperties
def _define_IEnumTfPropertyValue_head():
    class IEnumTfPropertyValue(win32more.System.Com.IUnknown_head):
        Guid = Guid('8ed8981b-7c10-4d7d-9f-b3-ab-72-e9-c7-5f-72')
    return IEnumTfPropertyValue
def _define_IEnumTfPropertyValue():
    IEnumTfPropertyValue = win32more.UI.TextServices.IEnumTfPropertyValue_head
    IEnumTfPropertyValue.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfPropertyValue_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfPropertyValue.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TF_PROPERTYVAL_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'rgValues'),(1, 'pcFetched'),)))
    IEnumTfPropertyValue.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfPropertyValue.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfPropertyValue
def _define_IEnumTfRanges_head():
    class IEnumTfRanges(win32more.System.Com.IUnknown_head):
        Guid = Guid('f99d3f40-8e32-11d2-bf-46-00-10-5a-27-99-b5')
    return IEnumTfRanges
def _define_IEnumTfRanges():
    IEnumTfRanges = win32more.UI.TextServices.IEnumTfRanges_head
    IEnumTfRanges.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfRanges_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfRanges.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfRange_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'ppRange'),(1, 'pcFetched'),)))
    IEnumTfRanges.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfRanges.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfRanges
def _define_IEnumTfUIElements_head():
    class IEnumTfUIElements(win32more.System.Com.IUnknown_head):
        Guid = Guid('887aa91e-acba-4931-84-da-3c-52-08-cf-54-3f')
    return IEnumTfUIElements
def _define_IEnumTfUIElements():
    IEnumTfUIElements = win32more.UI.TextServices.IEnumTfUIElements_head
    IEnumTfUIElements.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfUIElements_head))(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfUIElements.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfUIElement_head),POINTER(UInt32))(4, 'Next', ((1, 'ulCount'),(1, 'ppElement'),(1, 'pcFetched'),)))
    IEnumTfUIElements.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumTfUIElements.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Skip', ((1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IEnumTfUIElements
def _define_IInternalDocWrap_head():
    class IInternalDocWrap(win32more.System.Com.IUnknown_head):
        Guid = Guid('e1aa6466-9db4-40ba-be-03-77-c3-8e-8e-60-b2')
    return IInternalDocWrap
def _define_IInternalDocWrap():
    IInternalDocWrap = win32more.UI.TextServices.IInternalDocWrap_head
    IInternalDocWrap.NotifyRevoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'NotifyRevoke', ()))
    win32more.System.Com.IUnknown
    return IInternalDocWrap
InputScope = Int32
IS_DEFAULT = 0
IS_URL = 1
IS_FILE_FULLFILEPATH = 2
IS_FILE_FILENAME = 3
IS_EMAIL_USERNAME = 4
IS_EMAIL_SMTPEMAILADDRESS = 5
IS_LOGINNAME = 6
IS_PERSONALNAME_FULLNAME = 7
IS_PERSONALNAME_PREFIX = 8
IS_PERSONALNAME_GIVENNAME = 9
IS_PERSONALNAME_MIDDLENAME = 10
IS_PERSONALNAME_SURNAME = 11
IS_PERSONALNAME_SUFFIX = 12
IS_ADDRESS_FULLPOSTALADDRESS = 13
IS_ADDRESS_POSTALCODE = 14
IS_ADDRESS_STREET = 15
IS_ADDRESS_STATEORPROVINCE = 16
IS_ADDRESS_CITY = 17
IS_ADDRESS_COUNTRYNAME = 18
IS_ADDRESS_COUNTRYSHORTNAME = 19
IS_CURRENCY_AMOUNTANDSYMBOL = 20
IS_CURRENCY_AMOUNT = 21
IS_DATE_FULLDATE = 22
IS_DATE_MONTH = 23
IS_DATE_DAY = 24
IS_DATE_YEAR = 25
IS_DATE_MONTHNAME = 26
IS_DATE_DAYNAME = 27
IS_DIGITS = 28
IS_NUMBER = 29
IS_ONECHAR = 30
IS_PASSWORD = 31
IS_TELEPHONE_FULLTELEPHONENUMBER = 32
IS_TELEPHONE_COUNTRYCODE = 33
IS_TELEPHONE_AREACODE = 34
IS_TELEPHONE_LOCALNUMBER = 35
IS_TIME_FULLTIME = 36
IS_TIME_HOUR = 37
IS_TIME_MINORSEC = 38
IS_NUMBER_FULLWIDTH = 39
IS_ALPHANUMERIC_HALFWIDTH = 40
IS_ALPHANUMERIC_FULLWIDTH = 41
IS_CURRENCY_CHINESE = 42
IS_BOPOMOFO = 43
IS_HIRAGANA = 44
IS_KATAKANA_HALFWIDTH = 45
IS_KATAKANA_FULLWIDTH = 46
IS_HANJA = 47
IS_HANGUL_HALFWIDTH = 48
IS_HANGUL_FULLWIDTH = 49
IS_SEARCH = 50
IS_FORMULA = 51
IS_SEARCH_INCREMENTAL = 52
IS_CHINESE_HALFWIDTH = 53
IS_CHINESE_FULLWIDTH = 54
IS_NATIVE_SCRIPT = 55
IS_YOMI = 56
IS_TEXT = 57
IS_CHAT = 58
IS_NAME_OR_PHONENUMBER = 59
IS_EMAILNAME_OR_ADDRESS = 60
IS_PRIVATE = 61
IS_MAPS = 62
IS_NUMERIC_PASSWORD = 63
IS_NUMERIC_PIN = 64
IS_ALPHANUMERIC_PIN = 65
IS_ALPHANUMERIC_PIN_SET = 66
IS_FORMULA_NUMBER = 67
IS_CHAT_WITHOUT_EMOJI = 68
IS_PHRASELIST = -1
IS_REGULAREXPRESSION = -2
IS_SRGS = -3
IS_XML = -4
IS_ENUMSTRING = -5
INSERT_TEXT_AT_SELECTION_FLAGS = UInt32
TF_IAS_NOQUERY = 1
TF_IAS_QUERYONLY = 2
TF_IAS_NO_DEFAULT_COMPOSITION = 2147483648
def _define_ISpeechCommandProvider_head():
    class ISpeechCommandProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('38e09d4c-586d-435a-b5-92-c8-a8-66-91-de-c6')
    return ISpeechCommandProvider
def _define_ISpeechCommandProvider():
    ISpeechCommandProvider = win32more.UI.TextServices.ISpeechCommandProvider_head
    ISpeechCommandProvider.EnumSpeechCommands = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.UI.TextServices.IEnumSpeechCommands_head))(3, 'EnumSpeechCommands', ((1, 'langid'),(1, 'ppEnum'),)))
    ISpeechCommandProvider.ProcessCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt16)(4, 'ProcessCommand', ((1, 'pszCommand'),(1, 'cch'),(1, 'langid'),)))
    win32more.System.Com.IUnknown
    return ISpeechCommandProvider
def _define_ITextStoreACP_head():
    class ITextStoreACP(win32more.System.Com.IUnknown_head):
        Guid = Guid('28888fe3-c2a0-483a-a3-ea-8c-b1-ce-51-ff-3d')
    return ITextStoreACP
def _define_ITextStoreACP():
    ITextStoreACP = win32more.UI.TextServices.ITextStoreACP_head
    ITextStoreACP.AdviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,UInt32)(3, 'AdviseSink', ((1, 'riid'),(1, 'punk'),(1, 'dwMask'),)))
    ITextStoreACP.UnadviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(4, 'UnadviseSink', ((1, 'punk'),)))
    ITextStoreACP.RequestLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.HRESULT))(5, 'RequestLock', ((1, 'dwLockFlags'),(1, 'phrSession'),)))
    ITextStoreACP.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TS_STATUS_head))(6, 'GetStatus', ((1, 'pdcs'),)))
    ITextStoreACP.QueryInsert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(Int32),POINTER(Int32))(7, 'QueryInsert', ((1, 'acpTestStart'),(1, 'acpTestEnd'),(1, 'cch'),(1, 'pacpResultStart'),(1, 'pacpResultEnd'),)))
    ITextStoreACP.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.UI.TextServices.TS_SELECTION_ACP_head),POINTER(UInt32))(8, 'GetSelection', ((1, 'ulIndex'),(1, 'ulCount'),(1, 'pSelection'),(1, 'pcFetched'),)))
    ITextStoreACP.SetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TS_SELECTION_ACP_head))(9, 'SetSelection', ((1, 'ulCount'),(1, 'pSelection'),)))
    ITextStoreACP.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(win32more.UI.TextServices.TS_RUNINFO_head),UInt32,POINTER(UInt32),POINTER(Int32))(10, 'GetText', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'pchPlain'),(1, 'cchPlainReq'),(1, 'pcchPlainRet'),(1, 'prgRunInfo'),(1, 'cRunInfoReq'),(1, 'pcRunInfoRet'),(1, 'pacpNext'),)))
    ITextStoreACP.SetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,Int32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head))(11, 'SetText', ((1, 'dwFlags'),(1, 'acpStart'),(1, 'acpEnd'),(1, 'pchText'),(1, 'cch'),(1, 'pChange'),)))
    ITextStoreACP.GetFormattedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.Com.IDataObject_head))(12, 'GetFormattedText', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'ppDataObject'),)))
    ITextStoreACP.GetEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(13, 'GetEmbedded', ((1, 'acpPos'),(1, 'rguidService'),(1, 'riid'),(1, 'ppunk'),)))
    ITextStoreACP.QueryInsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.Foundation.BOOL))(14, 'QueryInsertEmbedded', ((1, 'pguidService'),(1, 'pFormatEtc'),(1, 'pfInsertable'),)))
    ITextStoreACP.InsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,Int32,win32more.System.Com.IDataObject_head,POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head))(15, 'InsertEmbedded', ((1, 'dwFlags'),(1, 'acpStart'),(1, 'acpEnd'),(1, 'pDataObject'),(1, 'pChange'),)))
    ITextStoreACP.InsertTextAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(Int32),POINTER(Int32),POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head))(16, 'InsertTextAtSelection', ((1, 'dwFlags'),(1, 'pchText'),(1, 'cch'),(1, 'pacpStart'),(1, 'pacpEnd'),(1, 'pChange'),)))
    ITextStoreACP.InsertEmbeddedAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IDataObject_head,POINTER(Int32),POINTER(Int32),POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head))(17, 'InsertEmbeddedAtSelection', ((1, 'dwFlags'),(1, 'pDataObject'),(1, 'pacpStart'),(1, 'pacpEnd'),(1, 'pChange'),)))
    ITextStoreACP.RequestSupportedAttrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid))(18, 'RequestSupportedAttrs', ((1, 'dwFlags'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),)))
    ITextStoreACP.RequestAttrsAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(Guid),UInt32)(19, 'RequestAttrsAtPosition', ((1, 'acpPos'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),)))
    ITextStoreACP.RequestAttrsTransitioningAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(Guid),UInt32)(20, 'RequestAttrsTransitioningAtPosition', ((1, 'acpPos'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),)))
    ITextStoreACP.FindNextAttrTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(Guid),UInt32,POINTER(Int32),POINTER(win32more.Foundation.BOOL),POINTER(Int32))(21, 'FindNextAttrTransition', ((1, 'acpStart'),(1, 'acpHalt'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),(1, 'pacpNext'),(1, 'pfFound'),(1, 'plFoundOffset'),)))
    ITextStoreACP.RetrieveRequestedAttrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TS_ATTRVAL_head),POINTER(UInt32))(22, 'RetrieveRequestedAttrs', ((1, 'ulCount'),(1, 'paAttrVals'),(1, 'pcFetched'),)))
    ITextStoreACP.GetEndACP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(23, 'GetEndACP', ((1, 'pacp'),)))
    ITextStoreACP.GetActiveView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(24, 'GetActiveView', ((1, 'pvcView'),)))
    ITextStoreACP.GetACPFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.POINT_head),UInt32,POINTER(Int32))(25, 'GetACPFromPoint', ((1, 'vcView'),(1, 'ptScreen'),(1, 'dwFlags'),(1, 'pacp'),)))
    ITextStoreACP.GetTextExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,Int32,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.BOOL))(26, 'GetTextExt', ((1, 'vcView'),(1, 'acpStart'),(1, 'acpEnd'),(1, 'prc'),(1, 'pfClipped'),)))
    ITextStoreACP.GetScreenExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.RECT_head))(27, 'GetScreenExt', ((1, 'vcView'),(1, 'prc'),)))
    ITextStoreACP.GetWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.HWND))(28, 'GetWnd', ((1, 'vcView'),(1, 'phwnd'),)))
    win32more.System.Com.IUnknown
    return ITextStoreACP
def _define_ITextStoreACP2_head():
    class ITextStoreACP2(win32more.System.Com.IUnknown_head):
        Guid = Guid('f86ad89f-5fe4-4b8d-bb-9f-ef-37-97-a8-4f-1f')
    return ITextStoreACP2
def _define_ITextStoreACP2():
    ITextStoreACP2 = win32more.UI.TextServices.ITextStoreACP2_head
    ITextStoreACP2.AdviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,UInt32)(3, 'AdviseSink', ((1, 'riid'),(1, 'punk'),(1, 'dwMask'),)))
    ITextStoreACP2.UnadviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(4, 'UnadviseSink', ((1, 'punk'),)))
    ITextStoreACP2.RequestLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.HRESULT))(5, 'RequestLock', ((1, 'dwLockFlags'),(1, 'phrSession'),)))
    ITextStoreACP2.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TS_STATUS_head))(6, 'GetStatus', ((1, 'pdcs'),)))
    ITextStoreACP2.QueryInsert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(Int32),POINTER(Int32))(7, 'QueryInsert', ((1, 'acpTestStart'),(1, 'acpTestEnd'),(1, 'cch'),(1, 'pacpResultStart'),(1, 'pacpResultEnd'),)))
    ITextStoreACP2.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.UI.TextServices.TS_SELECTION_ACP_head),POINTER(UInt32))(8, 'GetSelection', ((1, 'ulIndex'),(1, 'ulCount'),(1, 'pSelection'),(1, 'pcFetched'),)))
    ITextStoreACP2.SetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TS_SELECTION_ACP_head))(9, 'SetSelection', ((1, 'ulCount'),(1, 'pSelection'),)))
    ITextStoreACP2.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(win32more.UI.TextServices.TS_RUNINFO_head),UInt32,POINTER(UInt32),POINTER(Int32))(10, 'GetText', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'pchPlain'),(1, 'cchPlainReq'),(1, 'pcchPlainRet'),(1, 'prgRunInfo'),(1, 'cRunInfoReq'),(1, 'pcRunInfoRet'),(1, 'pacpNext'),)))
    ITextStoreACP2.SetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,Int32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head))(11, 'SetText', ((1, 'dwFlags'),(1, 'acpStart'),(1, 'acpEnd'),(1, 'pchText'),(1, 'cch'),(1, 'pChange'),)))
    ITextStoreACP2.GetFormattedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.Com.IDataObject_head))(12, 'GetFormattedText', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'ppDataObject'),)))
    ITextStoreACP2.GetEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(13, 'GetEmbedded', ((1, 'acpPos'),(1, 'rguidService'),(1, 'riid'),(1, 'ppunk'),)))
    ITextStoreACP2.QueryInsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.Foundation.BOOL))(14, 'QueryInsertEmbedded', ((1, 'pguidService'),(1, 'pFormatEtc'),(1, 'pfInsertable'),)))
    ITextStoreACP2.InsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,Int32,win32more.System.Com.IDataObject_head,POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head))(15, 'InsertEmbedded', ((1, 'dwFlags'),(1, 'acpStart'),(1, 'acpEnd'),(1, 'pDataObject'),(1, 'pChange'),)))
    ITextStoreACP2.InsertTextAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(Int32),POINTER(Int32),POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head))(16, 'InsertTextAtSelection', ((1, 'dwFlags'),(1, 'pchText'),(1, 'cch'),(1, 'pacpStart'),(1, 'pacpEnd'),(1, 'pChange'),)))
    ITextStoreACP2.InsertEmbeddedAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IDataObject_head,POINTER(Int32),POINTER(Int32),POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head))(17, 'InsertEmbeddedAtSelection', ((1, 'dwFlags'),(1, 'pDataObject'),(1, 'pacpStart'),(1, 'pacpEnd'),(1, 'pChange'),)))
    ITextStoreACP2.RequestSupportedAttrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid))(18, 'RequestSupportedAttrs', ((1, 'dwFlags'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),)))
    ITextStoreACP2.RequestAttrsAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(Guid),UInt32)(19, 'RequestAttrsAtPosition', ((1, 'acpPos'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),)))
    ITextStoreACP2.RequestAttrsTransitioningAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(Guid),UInt32)(20, 'RequestAttrsTransitioningAtPosition', ((1, 'acpPos'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),)))
    ITextStoreACP2.FindNextAttrTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(Guid),UInt32,POINTER(Int32),POINTER(win32more.Foundation.BOOL),POINTER(Int32))(21, 'FindNextAttrTransition', ((1, 'acpStart'),(1, 'acpHalt'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),(1, 'pacpNext'),(1, 'pfFound'),(1, 'plFoundOffset'),)))
    ITextStoreACP2.RetrieveRequestedAttrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TS_ATTRVAL_head),POINTER(UInt32))(22, 'RetrieveRequestedAttrs', ((1, 'ulCount'),(1, 'paAttrVals'),(1, 'pcFetched'),)))
    ITextStoreACP2.GetEndACP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(23, 'GetEndACP', ((1, 'pacp'),)))
    ITextStoreACP2.GetActiveView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(24, 'GetActiveView', ((1, 'pvcView'),)))
    ITextStoreACP2.GetACPFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.POINT_head),UInt32,POINTER(Int32))(25, 'GetACPFromPoint', ((1, 'vcView'),(1, 'ptScreen'),(1, 'dwFlags'),(1, 'pacp'),)))
    ITextStoreACP2.GetTextExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,Int32,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.BOOL))(26, 'GetTextExt', ((1, 'vcView'),(1, 'acpStart'),(1, 'acpEnd'),(1, 'prc'),(1, 'pfClipped'),)))
    ITextStoreACP2.GetScreenExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.RECT_head))(27, 'GetScreenExt', ((1, 'vcView'),(1, 'prc'),)))
    win32more.System.Com.IUnknown
    return ITextStoreACP2
def _define_ITextStoreACPEx_head():
    class ITextStoreACPEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('a2de3bc2-3d8e-11d3-81-a9-f7-53-fb-e6-1a-00')
    return ITextStoreACPEx
def _define_ITextStoreACPEx():
    ITextStoreACPEx = win32more.UI.TextServices.ITextStoreACPEx_head
    ITextStoreACPEx.ScrollToRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Foundation.RECT,UInt32)(3, 'ScrollToRect', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'rc'),(1, 'dwPosition'),)))
    win32more.System.Com.IUnknown
    return ITextStoreACPEx
def _define_ITextStoreACPServices_head():
    class ITextStoreACPServices(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e901-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    return ITextStoreACPServices
def _define_ITextStoreACPServices():
    ITextStoreACPServices = win32more.UI.TextServices.ITextStoreACPServices_head
    ITextStoreACPServices.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfProperty_head,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head),win32more.System.Com.IStream_head)(3, 'Serialize', ((1, 'pProp'),(1, 'pRange'),(1, 'pHdr'),(1, 'pStream'),)))
    ITextStoreACPServices.Unserialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfProperty_head,POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head),win32more.System.Com.IStream_head,win32more.UI.TextServices.ITfPersistentPropertyLoaderACP_head)(4, 'Unserialize', ((1, 'pProp'),(1, 'pHdr'),(1, 'pStream'),(1, 'pLoader'),)))
    ITextStoreACPServices.ForceLoadProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfProperty_head)(5, 'ForceLoadProperty', ((1, 'pProp'),)))
    ITextStoreACPServices.CreateRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.TextServices.ITfRangeACP_head))(6, 'CreateRange', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'ppRange'),)))
    win32more.System.Com.IUnknown
    return ITextStoreACPServices
def _define_ITextStoreACPSink_head():
    class ITextStoreACPSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('22d44c94-a419-4542-a2-72-ae-26-09-3e-ce-cf')
    return ITextStoreACPSink
def _define_ITextStoreACPSink():
    ITextStoreACPSink = win32more.UI.TextServices.ITextStoreACPSink_head
    ITextStoreACPSink.OnTextChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TEXT_STORE_TEXT_CHANGE_FLAGS,POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head))(3, 'OnTextChange', ((1, 'dwFlags'),(1, 'pChange'),)))
    ITextStoreACPSink.OnSelectionChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'OnSelectionChange', ()))
    ITextStoreACPSink.OnLayoutChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TsLayoutCode,UInt32)(5, 'OnLayoutChange', ((1, 'lcode'),(1, 'vcView'),)))
    ITextStoreACPSink.OnStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'OnStatusChange', ((1, 'dwFlags'),)))
    ITextStoreACPSink.OnAttrsChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(Guid))(7, 'OnAttrsChange', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'cAttrs'),(1, 'paAttrs'),)))
    ITextStoreACPSink.OnLockGranted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TEXT_STORE_LOCK_FLAGS)(8, 'OnLockGranted', ((1, 'dwLockFlags'),)))
    ITextStoreACPSink.OnStartEditTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'OnStartEditTransaction', ()))
    ITextStoreACPSink.OnEndEditTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'OnEndEditTransaction', ()))
    win32more.System.Com.IUnknown
    return ITextStoreACPSink
def _define_ITextStoreACPSinkEx_head():
    class ITextStoreACPSinkEx(win32more.UI.TextServices.ITextStoreACPSink_head):
        Guid = Guid('2bdf9464-41e2-43e3-95-0c-a6-86-5b-a2-5c-d4')
    return ITextStoreACPSinkEx
def _define_ITextStoreACPSinkEx():
    ITextStoreACPSinkEx = win32more.UI.TextServices.ITextStoreACPSinkEx_head
    ITextStoreACPSinkEx.OnDisconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'OnDisconnect', ()))
    win32more.UI.TextServices.ITextStoreACPSink
    return ITextStoreACPSinkEx
def _define_ITextStoreAnchor_head():
    class ITextStoreAnchor(win32more.System.Com.IUnknown_head):
        Guid = Guid('9b2077b0-5f18-4dec-be-e9-3c-c7-22-f5-df-e0')
    return ITextStoreAnchor
def _define_ITextStoreAnchor():
    ITextStoreAnchor = win32more.UI.TextServices.ITextStoreAnchor_head
    ITextStoreAnchor.AdviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,UInt32)(3, 'AdviseSink', ((1, 'riid'),(1, 'punk'),(1, 'dwMask'),)))
    ITextStoreAnchor.UnadviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(4, 'UnadviseSink', ((1, 'punk'),)))
    ITextStoreAnchor.RequestLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.HRESULT))(5, 'RequestLock', ((1, 'dwLockFlags'),(1, 'phrSession'),)))
    ITextStoreAnchor.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TS_STATUS_head))(6, 'GetStatus', ((1, 'pdcs'),)))
    ITextStoreAnchor.QueryInsert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,UInt32,POINTER(win32more.UI.TextServices.IAnchor_head),POINTER(win32more.UI.TextServices.IAnchor_head))(7, 'QueryInsert', ((1, 'paTestStart'),(1, 'paTestEnd'),(1, 'cch'),(1, 'ppaResultStart'),(1, 'ppaResultEnd'),)))
    ITextStoreAnchor.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.UI.TextServices.TS_SELECTION_ANCHOR_head),POINTER(UInt32))(8, 'GetSelection', ((1, 'ulIndex'),(1, 'ulCount'),(1, 'pSelection'),(1, 'pcFetched'),)))
    ITextStoreAnchor.SetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TS_SELECTION_ANCHOR_head))(9, 'SetSelection', ((1, 'ulCount'),(1, 'pSelection'),)))
    ITextStoreAnchor.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),win32more.Foundation.BOOL)(10, 'GetText', ((1, 'dwFlags'),(1, 'paStart'),(1, 'paEnd'),(1, 'pchText'),(1, 'cchReq'),(1, 'pcch'),(1, 'fUpdateAnchor'),)))
    ITextStoreAnchor.SetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,win32more.Foundation.PWSTR,UInt32)(11, 'SetText', ((1, 'dwFlags'),(1, 'paStart'),(1, 'paEnd'),(1, 'pchText'),(1, 'cch'),)))
    ITextStoreAnchor.GetFormattedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,POINTER(win32more.System.Com.IDataObject_head))(12, 'GetFormattedText', ((1, 'paStart'),(1, 'paEnd'),(1, 'ppDataObject'),)))
    ITextStoreAnchor.GetEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.IAnchor_head,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(13, 'GetEmbedded', ((1, 'dwFlags'),(1, 'paPos'),(1, 'rguidService'),(1, 'riid'),(1, 'ppunk'),)))
    ITextStoreAnchor.InsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,win32more.System.Com.IDataObject_head)(14, 'InsertEmbedded', ((1, 'dwFlags'),(1, 'paStart'),(1, 'paEnd'),(1, 'pDataObject'),)))
    ITextStoreAnchor.RequestSupportedAttrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid))(15, 'RequestSupportedAttrs', ((1, 'dwFlags'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),)))
    ITextStoreAnchor.RequestAttrsAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,UInt32,POINTER(Guid),UInt32)(16, 'RequestAttrsAtPosition', ((1, 'paPos'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),)))
    ITextStoreAnchor.RequestAttrsTransitioningAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,UInt32,POINTER(Guid),UInt32)(17, 'RequestAttrsTransitioningAtPosition', ((1, 'paPos'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),)))
    ITextStoreAnchor.FindNextAttrTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,UInt32,POINTER(Guid),UInt32,POINTER(win32more.Foundation.BOOL),POINTER(Int32))(18, 'FindNextAttrTransition', ((1, 'paStart'),(1, 'paHalt'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),(1, 'pfFound'),(1, 'plFoundOffset'),)))
    ITextStoreAnchor.RetrieveRequestedAttrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TS_ATTRVAL_head),POINTER(UInt32))(19, 'RetrieveRequestedAttrs', ((1, 'ulCount'),(1, 'paAttrVals'),(1, 'pcFetched'),)))
    ITextStoreAnchor.GetStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IAnchor_head))(20, 'GetStart', ((1, 'ppaStart'),)))
    ITextStoreAnchor.GetEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IAnchor_head))(21, 'GetEnd', ((1, 'ppaEnd'),)))
    ITextStoreAnchor.GetActiveView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(22, 'GetActiveView', ((1, 'pvcView'),)))
    ITextStoreAnchor.GetAnchorFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.POINT_head),UInt32,POINTER(win32more.UI.TextServices.IAnchor_head))(23, 'GetAnchorFromPoint', ((1, 'vcView'),(1, 'ptScreen'),(1, 'dwFlags'),(1, 'ppaSite'),)))
    ITextStoreAnchor.GetTextExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.BOOL))(24, 'GetTextExt', ((1, 'vcView'),(1, 'paStart'),(1, 'paEnd'),(1, 'prc'),(1, 'pfClipped'),)))
    ITextStoreAnchor.GetScreenExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.RECT_head))(25, 'GetScreenExt', ((1, 'vcView'),(1, 'prc'),)))
    ITextStoreAnchor.GetWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.HWND))(26, 'GetWnd', ((1, 'vcView'),(1, 'phwnd'),)))
    ITextStoreAnchor.QueryInsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.Foundation.BOOL))(27, 'QueryInsertEmbedded', ((1, 'pguidService'),(1, 'pFormatEtc'),(1, 'pfInsertable'),)))
    ITextStoreAnchor.InsertTextAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.UI.TextServices.IAnchor_head),POINTER(win32more.UI.TextServices.IAnchor_head))(28, 'InsertTextAtSelection', ((1, 'dwFlags'),(1, 'pchText'),(1, 'cch'),(1, 'ppaStart'),(1, 'ppaEnd'),)))
    ITextStoreAnchor.InsertEmbeddedAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IDataObject_head,POINTER(win32more.UI.TextServices.IAnchor_head),POINTER(win32more.UI.TextServices.IAnchor_head))(29, 'InsertEmbeddedAtSelection', ((1, 'dwFlags'),(1, 'pDataObject'),(1, 'ppaStart'),(1, 'ppaEnd'),)))
    win32more.System.Com.IUnknown
    return ITextStoreAnchor
def _define_ITextStoreAnchorEx_head():
    class ITextStoreAnchorEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('a2de3bc1-3d8e-11d3-81-a9-f7-53-fb-e6-1a-00')
    return ITextStoreAnchorEx
def _define_ITextStoreAnchorEx():
    ITextStoreAnchorEx = win32more.UI.TextServices.ITextStoreAnchorEx_head
    ITextStoreAnchorEx.ScrollToRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,win32more.Foundation.RECT,UInt32)(3, 'ScrollToRect', ((1, 'pStart'),(1, 'pEnd'),(1, 'rc'),(1, 'dwPosition'),)))
    win32more.System.Com.IUnknown
    return ITextStoreAnchorEx
def _define_ITextStoreAnchorSink_head():
    class ITextStoreAnchorSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e905-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    return ITextStoreAnchorSink
def _define_ITextStoreAnchorSink():
    ITextStoreAnchorSink = win32more.UI.TextServices.ITextStoreAnchorSink_head
    ITextStoreAnchorSink.OnTextChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TEXT_STORE_CHANGE_FLAGS,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head)(3, 'OnTextChange', ((1, 'dwFlags'),(1, 'paStart'),(1, 'paEnd'),)))
    ITextStoreAnchorSink.OnSelectionChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'OnSelectionChange', ()))
    ITextStoreAnchorSink.OnLayoutChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TsLayoutCode,UInt32)(5, 'OnLayoutChange', ((1, 'lcode'),(1, 'vcView'),)))
    ITextStoreAnchorSink.OnStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'OnStatusChange', ((1, 'dwFlags'),)))
    ITextStoreAnchorSink.OnAttrsChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,UInt32,POINTER(Guid))(7, 'OnAttrsChange', ((1, 'paStart'),(1, 'paEnd'),(1, 'cAttrs'),(1, 'paAttrs'),)))
    ITextStoreAnchorSink.OnLockGranted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TEXT_STORE_LOCK_FLAGS)(8, 'OnLockGranted', ((1, 'dwLockFlags'),)))
    ITextStoreAnchorSink.OnStartEditTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'OnStartEditTransaction', ()))
    ITextStoreAnchorSink.OnEndEditTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(10, 'OnEndEditTransaction', ()))
    win32more.System.Com.IUnknown
    return ITextStoreAnchorSink
def _define_ITextStoreSinkAnchorEx_head():
    class ITextStoreSinkAnchorEx(win32more.UI.TextServices.ITextStoreAnchorSink_head):
        Guid = Guid('25642426-028d-4474-97-7b-11-1b-b1-14-fe-3e')
    return ITextStoreSinkAnchorEx
def _define_ITextStoreSinkAnchorEx():
    ITextStoreSinkAnchorEx = win32more.UI.TextServices.ITextStoreSinkAnchorEx_head
    ITextStoreSinkAnchorEx.OnDisconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'OnDisconnect', ()))
    win32more.UI.TextServices.ITextStoreAnchorSink
    return ITextStoreSinkAnchorEx
def _define_ITfActiveLanguageProfileNotifySink_head():
    class ITfActiveLanguageProfileNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('b246cb75-a93e-4652-bf-8c-b3-fe-0c-fd-7e-57')
    return ITfActiveLanguageProfileNotifySink
def _define_ITfActiveLanguageProfileNotifySink():
    ITfActiveLanguageProfileNotifySink = win32more.UI.TextServices.ITfActiveLanguageProfileNotifySink_head
    ITfActiveLanguageProfileNotifySink.OnActivated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),win32more.Foundation.BOOL)(3, 'OnActivated', ((1, 'clsid'),(1, 'guidProfile'),(1, 'fActivated'),)))
    win32more.System.Com.IUnknown
    return ITfActiveLanguageProfileNotifySink
def _define_ITfCandidateList_head():
    class ITfCandidateList(win32more.System.Com.IUnknown_head):
        Guid = Guid('a3ad50fb-9bdb-49e3-a8-43-6c-76-52-0f-bf-5d')
    return ITfCandidateList
def _define_ITfCandidateList():
    ITfCandidateList = win32more.UI.TextServices.ITfCandidateList_head
    ITfCandidateList.EnumCandidates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfCandidates_head))(3, 'EnumCandidates', ((1, 'ppEnum'),)))
    ITfCandidateList.GetCandidate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfCandidateString_head))(4, 'GetCandidate', ((1, 'nIndex'),(1, 'ppCand'),)))
    ITfCandidateList.GetCandidateNum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(5, 'GetCandidateNum', ((1, 'pnCnt'),)))
    ITfCandidateList.SetResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.TfCandidateResult)(6, 'SetResult', ((1, 'nIndex'),(1, 'imcr'),)))
    win32more.System.Com.IUnknown
    return ITfCandidateList
def _define_ITfCandidateListUIElement_head():
    class ITfCandidateListUIElement(win32more.UI.TextServices.ITfUIElement_head):
        Guid = Guid('ea1ea138-19df-11d7-a6-d2-00-06-5b-84-43-5c')
    return ITfCandidateListUIElement
def _define_ITfCandidateListUIElement():
    ITfCandidateListUIElement = win32more.UI.TextServices.ITfCandidateListUIElement_head
    ITfCandidateListUIElement.GetUpdatedFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(7, 'GetUpdatedFlags', ((1, 'pdwFlags'),)))
    ITfCandidateListUIElement.GetDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head))(8, 'GetDocumentMgr', ((1, 'ppdim'),)))
    ITfCandidateListUIElement.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'GetCount', ((1, 'puCount'),)))
    ITfCandidateListUIElement.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(10, 'GetSelection', ((1, 'puIndex'),)))
    ITfCandidateListUIElement.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR))(11, 'GetString', ((1, 'uIndex'),(1, 'pstr'),)))
    ITfCandidateListUIElement.GetPageIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32,POINTER(UInt32))(12, 'GetPageIndex', ((1, 'pIndex'),(1, 'uSize'),(1, 'puPageCnt'),)))
    ITfCandidateListUIElement.SetPageIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32)(13, 'SetPageIndex', ((1, 'pIndex'),(1, 'uPageCnt'),)))
    ITfCandidateListUIElement.GetCurrentPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(14, 'GetCurrentPage', ((1, 'puPage'),)))
    win32more.UI.TextServices.ITfUIElement
    return ITfCandidateListUIElement
def _define_ITfCandidateListUIElementBehavior_head():
    class ITfCandidateListUIElementBehavior(win32more.UI.TextServices.ITfCandidateListUIElement_head):
        Guid = Guid('85fad185-58ce-497a-94-60-35-53-66-b6-4b-9a')
    return ITfCandidateListUIElementBehavior
def _define_ITfCandidateListUIElementBehavior():
    ITfCandidateListUIElementBehavior = win32more.UI.TextServices.ITfCandidateListUIElementBehavior_head
    ITfCandidateListUIElementBehavior.SetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(15, 'SetSelection', ((1, 'nIndex'),)))
    ITfCandidateListUIElementBehavior.Finalize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'Finalize', ()))
    ITfCandidateListUIElementBehavior.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(17, 'Abort', ()))
    win32more.UI.TextServices.ITfCandidateListUIElement
    return ITfCandidateListUIElementBehavior
def _define_ITfCandidateString_head():
    class ITfCandidateString(win32more.System.Com.IUnknown_head):
        Guid = Guid('581f317e-fd9d-443f-b9-72-ed-00-46-7c-5d-40')
    return ITfCandidateString
def _define_ITfCandidateString():
    ITfCandidateString = win32more.UI.TextServices.ITfCandidateString_head
    ITfCandidateString.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(3, 'GetString', ((1, 'pbstr'),)))
    ITfCandidateString.GetIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetIndex', ((1, 'pnIndex'),)))
    win32more.System.Com.IUnknown
    return ITfCandidateString
def _define_ITfCategoryMgr_head():
    class ITfCategoryMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('c3acefb5-f69d-4905-93-8f-fc-ad-cf-4b-e8-30')
    return ITfCategoryMgr
def _define_ITfCategoryMgr():
    ITfCategoryMgr = win32more.UI.TextServices.ITfCategoryMgr_head
    ITfCategoryMgr.RegisterCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(Guid))(3, 'RegisterCategory', ((1, 'rclsid'),(1, 'rcatid'),(1, 'rguid'),)))
    ITfCategoryMgr.UnregisterCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(Guid))(4, 'UnregisterCategory', ((1, 'rclsid'),(1, 'rcatid'),(1, 'rguid'),)))
    ITfCategoryMgr.EnumCategoriesInItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IEnumGUID_head))(5, 'EnumCategoriesInItem', ((1, 'rguid'),(1, 'ppEnum'),)))
    ITfCategoryMgr.EnumItemsInCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IEnumGUID_head))(6, 'EnumItemsInCategory', ((1, 'rcatid'),(1, 'ppEnum'),)))
    ITfCategoryMgr.FindClosestCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(POINTER(Guid)),UInt32)(7, 'FindClosestCategory', ((1, 'rguid'),(1, 'pcatid'),(1, 'ppcatidList'),(1, 'ulCount'),)))
    ITfCategoryMgr.RegisterGUIDDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),win32more.Foundation.PWSTR,UInt32)(8, 'RegisterGUIDDescription', ((1, 'rclsid'),(1, 'rguid'),(1, 'pchDesc'),(1, 'cch'),)))
    ITfCategoryMgr.UnregisterGUIDDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid))(9, 'UnregisterGUIDDescription', ((1, 'rclsid'),(1, 'rguid'),)))
    ITfCategoryMgr.GetGUIDDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.BSTR))(10, 'GetGUIDDescription', ((1, 'rguid'),(1, 'pbstrDesc'),)))
    ITfCategoryMgr.RegisterGUIDDWORD = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),UInt32)(11, 'RegisterGUIDDWORD', ((1, 'rclsid'),(1, 'rguid'),(1, 'dw'),)))
    ITfCategoryMgr.UnregisterGUIDDWORD = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid))(12, 'UnregisterGUIDDWORD', ((1, 'rclsid'),(1, 'rguid'),)))
    ITfCategoryMgr.GetGUIDDWORD = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32))(13, 'GetGUIDDWORD', ((1, 'rguid'),(1, 'pdw'),)))
    ITfCategoryMgr.RegisterGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32))(14, 'RegisterGUID', ((1, 'rguid'),(1, 'pguidatom'),)))
    ITfCategoryMgr.GetGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid))(15, 'GetGUID', ((1, 'guidatom'),(1, 'pguid'),)))
    ITfCategoryMgr.IsEqualTfGuidAtom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.Foundation.BOOL))(16, 'IsEqualTfGuidAtom', ((1, 'guidatom'),(1, 'rguid'),(1, 'pfEqual'),)))
    win32more.System.Com.IUnknown
    return ITfCategoryMgr
def _define_ITfCleanupContextDurationSink_head():
    class ITfCleanupContextDurationSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('45c35144-154e-4797-be-d8-d3-3a-e7-bf-87-94')
    return ITfCleanupContextDurationSink
def _define_ITfCleanupContextDurationSink():
    ITfCleanupContextDurationSink = win32more.UI.TextServices.ITfCleanupContextDurationSink_head
    ITfCleanupContextDurationSink.OnStartCleanupContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'OnStartCleanupContext', ()))
    ITfCleanupContextDurationSink.OnEndCleanupContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'OnEndCleanupContext', ()))
    win32more.System.Com.IUnknown
    return ITfCleanupContextDurationSink
def _define_ITfCleanupContextSink_head():
    class ITfCleanupContextSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('01689689-7acb-4e9b-ab-7c-7e-a4-6b-12-b5-22')
    return ITfCleanupContextSink
def _define_ITfCleanupContextSink():
    ITfCleanupContextSink = win32more.UI.TextServices.ITfCleanupContextSink_head
    ITfCleanupContextSink.OnCleanupContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfContext_head)(3, 'OnCleanupContext', ((1, 'ecWrite'),(1, 'pic'),)))
    win32more.System.Com.IUnknown
    return ITfCleanupContextSink
def _define_ITfClientId_head():
    class ITfClientId(win32more.System.Com.IUnknown_head):
        Guid = Guid('d60a7b49-1b9f-4be2-b7-02-47-e9-dc-05-de-c3')
    return ITfClientId
def _define_ITfClientId():
    ITfClientId = win32more.UI.TextServices.ITfClientId_head
    ITfClientId.GetClientId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32))(3, 'GetClientId', ((1, 'rclsid'),(1, 'ptid'),)))
    win32more.System.Com.IUnknown
    return ITfClientId
def _define_ITfCompartment_head():
    class ITfCompartment(win32more.System.Com.IUnknown_head):
        Guid = Guid('bb08f7a9-607a-4384-86-23-05-68-92-b6-43-71')
    return ITfCompartment
def _define_ITfCompartment():
    ITfCompartment = win32more.UI.TextServices.ITfCompartment_head
    ITfCompartment.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARIANT_head))(3, 'SetValue', ((1, 'tid'),(1, 'pvarValue'),)))
    ITfCompartment.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(4, 'GetValue', ((1, 'pvarValue'),)))
    win32more.System.Com.IUnknown
    return ITfCompartment
def _define_ITfCompartmentEventSink_head():
    class ITfCompartmentEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('743abd5f-f26d-48df-8c-c5-23-84-92-41-9b-64')
    return ITfCompartmentEventSink
def _define_ITfCompartmentEventSink():
    ITfCompartmentEventSink = win32more.UI.TextServices.ITfCompartmentEventSink_head
    ITfCompartmentEventSink.OnChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'OnChange', ((1, 'rguid'),)))
    win32more.System.Com.IUnknown
    return ITfCompartmentEventSink
def _define_ITfCompartmentMgr_head():
    class ITfCompartmentMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('7dcf57ac-18ad-438b-82-4d-97-9b-ff-b7-4b-7c')
    return ITfCompartmentMgr
def _define_ITfCompartmentMgr():
    ITfCompartmentMgr = win32more.UI.TextServices.ITfCompartmentMgr_head
    ITfCompartmentMgr.GetCompartment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfCompartment_head))(3, 'GetCompartment', ((1, 'rguid'),(1, 'ppcomp'),)))
    ITfCompartmentMgr.ClearCompartment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid))(4, 'ClearCompartment', ((1, 'tid'),(1, 'rguid'),)))
    ITfCompartmentMgr.EnumCompartments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumGUID_head))(5, 'EnumCompartments', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return ITfCompartmentMgr
def _define_ITfComposition_head():
    class ITfComposition(win32more.System.Com.IUnknown_head):
        Guid = Guid('20168d64-5a8f-4a5a-b7-bd-cf-a2-9f-4d-0f-d9')
    return ITfComposition
def _define_ITfComposition():
    ITfComposition = win32more.UI.TextServices.ITfComposition_head
    ITfComposition.GetRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfRange_head))(3, 'GetRange', ((1, 'ppRange'),)))
    ITfComposition.ShiftStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head)(4, 'ShiftStart', ((1, 'ecWrite'),(1, 'pNewStart'),)))
    ITfComposition.ShiftEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head)(5, 'ShiftEnd', ((1, 'ecWrite'),(1, 'pNewEnd'),)))
    ITfComposition.EndComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'EndComposition', ((1, 'ecWrite'),)))
    win32more.System.Com.IUnknown
    return ITfComposition
def _define_ITfCompositionSink_head():
    class ITfCompositionSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('a781718c-579a-4b15-a2-80-32-b8-57-7a-cc-5e')
    return ITfCompositionSink
def _define_ITfCompositionSink():
    ITfCompositionSink = win32more.UI.TextServices.ITfCompositionSink_head
    ITfCompositionSink.OnCompositionTerminated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfComposition_head)(3, 'OnCompositionTerminated', ((1, 'ecWrite'),(1, 'pComposition'),)))
    win32more.System.Com.IUnknown
    return ITfCompositionSink
def _define_ITfCompositionView_head():
    class ITfCompositionView(win32more.System.Com.IUnknown_head):
        Guid = Guid('d7540241-f9a1-4364-be-fc-db-cd-2c-43-95-b7')
    return ITfCompositionView
def _define_ITfCompositionView():
    ITfCompositionView = win32more.UI.TextServices.ITfCompositionView_head
    ITfCompositionView.GetOwnerClsid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetOwnerClsid', ((1, 'pclsid'),)))
    ITfCompositionView.GetRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfRange_head))(4, 'GetRange', ((1, 'ppRange'),)))
    win32more.System.Com.IUnknown
    return ITfCompositionView
def _define_ITfConfigureSystemKeystrokeFeed_head():
    class ITfConfigureSystemKeystrokeFeed(win32more.System.Com.IUnknown_head):
        Guid = Guid('0d2c969a-bc9c-437c-84-ee-95-1c-49-b1-a7-64')
    return ITfConfigureSystemKeystrokeFeed
def _define_ITfConfigureSystemKeystrokeFeed():
    ITfConfigureSystemKeystrokeFeed = win32more.UI.TextServices.ITfConfigureSystemKeystrokeFeed_head
    ITfConfigureSystemKeystrokeFeed.DisableSystemKeystrokeFeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'DisableSystemKeystrokeFeed', ()))
    ITfConfigureSystemKeystrokeFeed.EnableSystemKeystrokeFeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'EnableSystemKeystrokeFeed', ()))
    win32more.System.Com.IUnknown
    return ITfConfigureSystemKeystrokeFeed
def _define_ITfContext_head():
    class ITfContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e7fd-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    return ITfContext
def _define_ITfContext():
    ITfContext = win32more.UI.TextServices.ITfContext_head
    ITfContext.RequestEditSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfEditSession_head,win32more.UI.TextServices.TF_CONTEXT_EDIT_CONTEXT_FLAGS,POINTER(win32more.Foundation.HRESULT))(3, 'RequestEditSession', ((1, 'tid'),(1, 'pes'),(1, 'dwFlags'),(1, 'phrSession'),)))
    ITfContext.InWriteSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL))(4, 'InWriteSession', ((1, 'tid'),(1, 'pfWriteSession'),)))
    ITfContext.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.UI.TextServices.TF_SELECTION_head),POINTER(UInt32))(5, 'GetSelection', ((1, 'ec'),(1, 'ulIndex'),(1, 'ulCount'),(1, 'pSelection'),(1, 'pcFetched'),)))
    ITfContext.SetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.UI.TextServices.TF_SELECTION_head))(6, 'SetSelection', ((1, 'ec'),(1, 'ulCount'),(1, 'pSelection'),)))
    ITfContext.GetStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfRange_head))(7, 'GetStart', ((1, 'ec'),(1, 'ppStart'),)))
    ITfContext.GetEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfRange_head))(8, 'GetEnd', ((1, 'ec'),(1, 'ppEnd'),)))
    ITfContext.GetActiveView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfContextView_head))(9, 'GetActiveView', ((1, 'ppView'),)))
    ITfContext.EnumViews = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfContextViews_head))(10, 'EnumViews', ((1, 'ppEnum'),)))
    ITfContext.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TS_STATUS_head))(11, 'GetStatus', ((1, 'pdcs'),)))
    ITfContext.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfProperty_head))(12, 'GetProperty', ((1, 'guidProp'),(1, 'ppProp'),)))
    ITfContext.GetAppProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfReadOnlyProperty_head))(13, 'GetAppProperty', ((1, 'guidProp'),(1, 'ppProp'),)))
    ITfContext.TrackProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(Guid)),UInt32,POINTER(POINTER(Guid)),UInt32,POINTER(win32more.UI.TextServices.ITfReadOnlyProperty_head))(14, 'TrackProperties', ((1, 'prgProp'),(1, 'cProp'),(1, 'prgAppProp'),(1, 'cAppProp'),(1, 'ppProperty'),)))
    ITfContext.EnumProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfProperties_head))(15, 'EnumProperties', ((1, 'ppEnum'),)))
    ITfContext.GetDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head))(16, 'GetDocumentMgr', ((1, 'ppDm'),)))
    ITfContext.CreateRangeBackup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfRangeBackup_head))(17, 'CreateRangeBackup', ((1, 'ec'),(1, 'pRange'),(1, 'ppBackup'),)))
    win32more.System.Com.IUnknown
    return ITfContext
def _define_ITfContextComposition_head():
    class ITfContextComposition(win32more.System.Com.IUnknown_head):
        Guid = Guid('d40c8aae-ac92-4fc7-9a-11-0e-e0-e2-3a-a3-9b')
    return ITfContextComposition
def _define_ITfContextComposition():
    ITfContextComposition = win32more.UI.TextServices.ITfContextComposition_head
    ITfContextComposition.StartComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfCompositionSink_head,POINTER(win32more.UI.TextServices.ITfComposition_head))(3, 'StartComposition', ((1, 'ecWrite'),(1, 'pCompositionRange'),(1, 'pSink'),(1, 'ppComposition'),)))
    ITfContextComposition.EnumCompositions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumITfCompositionView_head))(4, 'EnumCompositions', ((1, 'ppEnum'),)))
    ITfContextComposition.FindComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.IEnumITfCompositionView_head))(5, 'FindComposition', ((1, 'ecRead'),(1, 'pTestRange'),(1, 'ppEnum'),)))
    ITfContextComposition.TakeOwnership = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfCompositionView_head,win32more.UI.TextServices.ITfCompositionSink_head,POINTER(win32more.UI.TextServices.ITfComposition_head))(6, 'TakeOwnership', ((1, 'ecWrite'),(1, 'pComposition'),(1, 'pSink'),(1, 'ppComposition'),)))
    win32more.System.Com.IUnknown
    return ITfContextComposition
def _define_ITfContextKeyEventSink_head():
    class ITfContextKeyEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('0552ba5d-c835-4934-bf-50-84-6a-aa-67-43-2f')
    return ITfContextKeyEventSink
def _define_ITfContextKeyEventSink():
    ITfContextKeyEventSink = win32more.UI.TextServices.ITfContextKeyEventSink_head
    ITfContextKeyEventSink.OnKeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(3, 'OnKeyDown', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfContextKeyEventSink.OnKeyUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(4, 'OnKeyUp', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfContextKeyEventSink.OnTestKeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(5, 'OnTestKeyDown', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfContextKeyEventSink.OnTestKeyUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(6, 'OnTestKeyUp', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    win32more.System.Com.IUnknown
    return ITfContextKeyEventSink
def _define_ITfContextOwner_head():
    class ITfContextOwner(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e80c-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    return ITfContextOwner
def _define_ITfContextOwner():
    ITfContextOwner = win32more.UI.TextServices.ITfContextOwner_head
    ITfContextOwner.GetACPFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.POINT_head),UInt32,POINTER(Int32))(3, 'GetACPFromPoint', ((1, 'ptScreen'),(1, 'dwFlags'),(1, 'pacp'),)))
    ITfContextOwner.GetTextExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.BOOL))(4, 'GetTextExt', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'prc'),(1, 'pfClipped'),)))
    ITfContextOwner.GetScreenExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(5, 'GetScreenExt', ((1, 'prc'),)))
    ITfContextOwner.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TS_STATUS_head))(6, 'GetStatus', ((1, 'pdcs'),)))
    ITfContextOwner.GetWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND))(7, 'GetWnd', ((1, 'phwnd'),)))
    ITfContextOwner.GetAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head))(8, 'GetAttribute', ((1, 'rguidAttribute'),(1, 'pvarValue'),)))
    win32more.System.Com.IUnknown
    return ITfContextOwner
def _define_ITfContextOwnerCompositionServices_head():
    class ITfContextOwnerCompositionServices(win32more.UI.TextServices.ITfContextComposition_head):
        Guid = Guid('86462810-593b-4916-97-64-19-c0-8e-9c-e1-10')
    return ITfContextOwnerCompositionServices
def _define_ITfContextOwnerCompositionServices():
    ITfContextOwnerCompositionServices = win32more.UI.TextServices.ITfContextOwnerCompositionServices_head
    ITfContextOwnerCompositionServices.TerminateComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfCompositionView_head)(7, 'TerminateComposition', ((1, 'pComposition'),)))
    win32more.UI.TextServices.ITfContextComposition
    return ITfContextOwnerCompositionServices
def _define_ITfContextOwnerCompositionSink_head():
    class ITfContextOwnerCompositionSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('5f20aa40-b57a-4f34-96-ab-35-76-f3-77-cc-79')
    return ITfContextOwnerCompositionSink
def _define_ITfContextOwnerCompositionSink():
    ITfContextOwnerCompositionSink = win32more.UI.TextServices.ITfContextOwnerCompositionSink_head
    ITfContextOwnerCompositionSink.OnStartComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfCompositionView_head,POINTER(win32more.Foundation.BOOL))(3, 'OnStartComposition', ((1, 'pComposition'),(1, 'pfOk'),)))
    ITfContextOwnerCompositionSink.OnUpdateComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfCompositionView_head,win32more.UI.TextServices.ITfRange_head)(4, 'OnUpdateComposition', ((1, 'pComposition'),(1, 'pRangeNew'),)))
    ITfContextOwnerCompositionSink.OnEndComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfCompositionView_head)(5, 'OnEndComposition', ((1, 'pComposition'),)))
    win32more.System.Com.IUnknown
    return ITfContextOwnerCompositionSink
def _define_ITfContextOwnerServices_head():
    class ITfContextOwnerServices(win32more.System.Com.IUnknown_head):
        Guid = Guid('b23eb630-3e1c-11d3-a7-45-00-50-04-0a-b4-07')
    return ITfContextOwnerServices
def _define_ITfContextOwnerServices():
    ITfContextOwnerServices = win32more.UI.TextServices.ITfContextOwnerServices_head
    ITfContextOwnerServices.OnLayoutChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'OnLayoutChange', ()))
    ITfContextOwnerServices.OnStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'OnStatusChange', ((1, 'dwFlags'),)))
    ITfContextOwnerServices.OnAttributeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(5, 'OnAttributeChange', ((1, 'rguidAttribute'),)))
    ITfContextOwnerServices.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfProperty_head,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head),win32more.System.Com.IStream_head)(6, 'Serialize', ((1, 'pProp'),(1, 'pRange'),(1, 'pHdr'),(1, 'pStream'),)))
    ITfContextOwnerServices.Unserialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfProperty_head,POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head),win32more.System.Com.IStream_head,win32more.UI.TextServices.ITfPersistentPropertyLoaderACP_head)(7, 'Unserialize', ((1, 'pProp'),(1, 'pHdr'),(1, 'pStream'),(1, 'pLoader'),)))
    ITfContextOwnerServices.ForceLoadProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfProperty_head)(8, 'ForceLoadProperty', ((1, 'pProp'),)))
    ITfContextOwnerServices.CreateRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.TextServices.ITfRangeACP_head))(9, 'CreateRange', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'ppRange'),)))
    win32more.System.Com.IUnknown
    return ITfContextOwnerServices
def _define_ITfContextView_head():
    class ITfContextView(win32more.System.Com.IUnknown_head):
        Guid = Guid('2433bf8e-0f9b-435c-ba-2c-18-06-11-97-8c-30')
    return ITfContextView
def _define_ITfContextView():
    ITfContextView = win32more.UI.TextServices.ITfContextView_head
    ITfContextView.GetRangeFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.POINT_head),UInt32,POINTER(win32more.UI.TextServices.ITfRange_head))(3, 'GetRangeFromPoint', ((1, 'ec'),(1, 'ppt'),(1, 'dwFlags'),(1, 'ppRange'),)))
    ITfContextView.GetTextExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.BOOL))(4, 'GetTextExt', ((1, 'ec'),(1, 'pRange'),(1, 'prc'),(1, 'pfClipped'),)))
    ITfContextView.GetScreenExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(5, 'GetScreenExt', ((1, 'prc'),)))
    ITfContextView.GetWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND))(6, 'GetWnd', ((1, 'phwnd'),)))
    win32more.System.Com.IUnknown
    return ITfContextView
def _define_ITfCreatePropertyStore_head():
    class ITfCreatePropertyStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('2463fbf0-b0af-11d2-af-c5-00-10-5a-27-99-b5')
    return ITfCreatePropertyStore
def _define_ITfCreatePropertyStore():
    ITfCreatePropertyStore = win32more.UI.TextServices.ITfCreatePropertyStore_head
    ITfCreatePropertyStore.IsStoreSerializable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfPropertyStore_head,POINTER(win32more.Foundation.BOOL))(3, 'IsStoreSerializable', ((1, 'guidProp'),(1, 'pRange'),(1, 'pPropStore'),(1, 'pfSerializable'),)))
    ITfCreatePropertyStore.CreatePropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.UI.TextServices.ITfRange_head,UInt32,win32more.System.Com.IStream_head,POINTER(win32more.UI.TextServices.ITfPropertyStore_head))(4, 'CreatePropertyStore', ((1, 'guidProp'),(1, 'pRange'),(1, 'cb'),(1, 'pStream'),(1, 'ppStore'),)))
    win32more.System.Com.IUnknown
    return ITfCreatePropertyStore
def _define_ITfDisplayAttributeInfo_head():
    class ITfDisplayAttributeInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('70528852-2f26-4aea-8c-96-21-51-50-57-89-32')
    return ITfDisplayAttributeInfo
def _define_ITfDisplayAttributeInfo():
    ITfDisplayAttributeInfo = win32more.UI.TextServices.ITfDisplayAttributeInfo_head
    ITfDisplayAttributeInfo.GetGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetGUID', ((1, 'pguid'),)))
    ITfDisplayAttributeInfo.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'GetDescription', ((1, 'pbstrDesc'),)))
    ITfDisplayAttributeInfo.GetAttributeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TF_DISPLAYATTRIBUTE_head))(5, 'GetAttributeInfo', ((1, 'pda'),)))
    ITfDisplayAttributeInfo.SetAttributeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TF_DISPLAYATTRIBUTE_head))(6, 'SetAttributeInfo', ((1, 'pda'),)))
    ITfDisplayAttributeInfo.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Reset', ()))
    win32more.System.Com.IUnknown
    return ITfDisplayAttributeInfo
def _define_ITfDisplayAttributeMgr_head():
    class ITfDisplayAttributeMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('8ded7393-5db1-475c-9e-71-a3-91-11-b0-ff-67')
    return ITfDisplayAttributeMgr
def _define_ITfDisplayAttributeMgr():
    ITfDisplayAttributeMgr = win32more.UI.TextServices.ITfDisplayAttributeMgr_head
    ITfDisplayAttributeMgr.OnUpdateInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'OnUpdateInfo', ()))
    ITfDisplayAttributeMgr.EnumDisplayAttributeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfDisplayAttributeInfo_head))(4, 'EnumDisplayAttributeInfo', ((1, 'ppEnum'),)))
    ITfDisplayAttributeMgr.GetDisplayAttributeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfDisplayAttributeInfo_head),POINTER(Guid))(5, 'GetDisplayAttributeInfo', ((1, 'guid'),(1, 'ppInfo'),(1, 'pclsidOwner'),)))
    win32more.System.Com.IUnknown
    return ITfDisplayAttributeMgr
def _define_ITfDisplayAttributeNotifySink_head():
    class ITfDisplayAttributeNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('ad56f402-e162-4f25-90-8f-7d-57-7c-f9-bd-a9')
    return ITfDisplayAttributeNotifySink
def _define_ITfDisplayAttributeNotifySink():
    ITfDisplayAttributeNotifySink = win32more.UI.TextServices.ITfDisplayAttributeNotifySink_head
    ITfDisplayAttributeNotifySink.OnUpdateInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'OnUpdateInfo', ()))
    win32more.System.Com.IUnknown
    return ITfDisplayAttributeNotifySink
def _define_ITfDisplayAttributeProvider_head():
    class ITfDisplayAttributeProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('fee47777-163c-4769-99-6a-6e-9c-50-ad-8f-54')
    return ITfDisplayAttributeProvider
def _define_ITfDisplayAttributeProvider():
    ITfDisplayAttributeProvider = win32more.UI.TextServices.ITfDisplayAttributeProvider_head
    ITfDisplayAttributeProvider.EnumDisplayAttributeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfDisplayAttributeInfo_head))(3, 'EnumDisplayAttributeInfo', ((1, 'ppEnum'),)))
    ITfDisplayAttributeProvider.GetDisplayAttributeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfDisplayAttributeInfo_head))(4, 'GetDisplayAttributeInfo', ((1, 'guid'),(1, 'ppInfo'),)))
    win32more.System.Com.IUnknown
    return ITfDisplayAttributeProvider
def _define_ITfDocumentMgr_head():
    class ITfDocumentMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e7f4-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    return ITfDocumentMgr
def _define_ITfDocumentMgr():
    ITfDocumentMgr = win32more.UI.TextServices.ITfDocumentMgr_head
    ITfDocumentMgr.CreateContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.System.Com.IUnknown_head,POINTER(win32more.UI.TextServices.ITfContext_head),POINTER(UInt32))(3, 'CreateContext', ((1, 'tidOwner'),(1, 'dwFlags'),(1, 'punk'),(1, 'ppic'),(1, 'pecTextStore'),)))
    ITfDocumentMgr.Push = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head)(4, 'Push', ((1, 'pic'),)))
    ITfDocumentMgr.Pop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'Pop', ((1, 'dwFlags'),)))
    ITfDocumentMgr.GetTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfContext_head))(6, 'GetTop', ((1, 'ppic'),)))
    ITfDocumentMgr.GetBase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfContext_head))(7, 'GetBase', ((1, 'ppic'),)))
    ITfDocumentMgr.EnumContexts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfContexts_head))(8, 'EnumContexts', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return ITfDocumentMgr
def _define_ITfEditRecord_head():
    class ITfEditRecord(win32more.System.Com.IUnknown_head):
        Guid = Guid('42d4d099-7c1a-4a89-b8-36-6c-6f-22-16-0d-f0')
    return ITfEditRecord
def _define_ITfEditRecord():
    ITfEditRecord = win32more.UI.TextServices.ITfEditRecord_head
    ITfEditRecord.GetSelectionStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'GetSelectionStatus', ((1, 'pfChanged'),)))
    ITfEditRecord.GetTextAndPropertyUpdates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.GET_TEXT_AND_PROPERTY_UPDATES_FLAGS,POINTER(POINTER(Guid)),UInt32,POINTER(win32more.UI.TextServices.IEnumTfRanges_head))(4, 'GetTextAndPropertyUpdates', ((1, 'dwFlags'),(1, 'prgProperties'),(1, 'cProperties'),(1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return ITfEditRecord
def _define_ITfEditSession_head():
    class ITfEditSession(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e803-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    return ITfEditSession
def _define_ITfEditSession():
    ITfEditSession = win32more.UI.TextServices.ITfEditSession_head
    ITfEditSession.DoEditSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'DoEditSession', ((1, 'ec'),)))
    win32more.System.Com.IUnknown
    return ITfEditSession
def _define_ITfEditTransactionSink_head():
    class ITfEditTransactionSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('708fbf70-b520-416b-b0-6c-2c-41-ab-44-f8-ba')
    return ITfEditTransactionSink
def _define_ITfEditTransactionSink():
    ITfEditTransactionSink = win32more.UI.TextServices.ITfEditTransactionSink_head
    ITfEditTransactionSink.OnStartEditTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head)(3, 'OnStartEditTransaction', ((1, 'pic'),)))
    ITfEditTransactionSink.OnEndEditTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head)(4, 'OnEndEditTransaction', ((1, 'pic'),)))
    win32more.System.Com.IUnknown
    return ITfEditTransactionSink
def _define_ITfFnAdviseText_head():
    class ITfFnAdviseText(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('3527268b-7d53-4dd9-92-b7-72-96-ae-46-12-49')
    return ITfFnAdviseText
def _define_ITfFnAdviseText():
    ITfFnAdviseText = win32more.UI.TextServices.ITfFnAdviseText_head
    ITfFnAdviseText.OnTextUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,win32more.Foundation.PWSTR,Int32)(4, 'OnTextUpdate', ((1, 'pRange'),(1, 'pchText'),(1, 'cch'),)))
    ITfFnAdviseText.OnLatticeUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfLMLattice_head)(5, 'OnLatticeUpdate', ((1, 'pRange'),(1, 'pLattice'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnAdviseText
def _define_ITfFnBalloon_head():
    class ITfFnBalloon(win32more.System.Com.IUnknown_head):
        Guid = Guid('3bab89e4-5fbe-45f4-a5-bc-dc-a3-6a-d2-25-a8')
    return ITfFnBalloon
def _define_ITfFnBalloon():
    ITfFnBalloon = win32more.UI.TextServices.ITfFnBalloon_head
    ITfFnBalloon.UpdateBalloon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfLBBalloonStyle,win32more.Foundation.PWSTR,UInt32)(3, 'UpdateBalloon', ((1, 'style'),(1, 'pch'),(1, 'cch'),)))
    win32more.System.Com.IUnknown
    return ITfFnBalloon
def _define_ITfFnConfigure_head():
    class ITfFnConfigure(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('88f567c6-1757-49f8-a1-b2-89-23-4c-1e-ef-f9')
    return ITfFnConfigure
def _define_ITfFnConfigure():
    ITfFnConfigure = win32more.UI.TextServices.ITfFnConfigure_head
    ITfFnConfigure.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt16,POINTER(Guid))(4, 'Show', ((1, 'hwndParent'),(1, 'langid'),(1, 'rguidProfile'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnConfigure
def _define_ITfFnConfigureRegisterEudc_head():
    class ITfFnConfigureRegisterEudc(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('b5e26ff5-d7ad-4304-91-3f-21-a2-ed-95-a1-b0')
    return ITfFnConfigureRegisterEudc
def _define_ITfFnConfigureRegisterEudc():
    ITfFnConfigureRegisterEudc = win32more.UI.TextServices.ITfFnConfigureRegisterEudc_head
    ITfFnConfigureRegisterEudc.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt16,POINTER(Guid),win32more.Foundation.BSTR)(4, 'Show', ((1, 'hwndParent'),(1, 'langid'),(1, 'rguidProfile'),(1, 'bstrRegistered'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnConfigureRegisterEudc
def _define_ITfFnConfigureRegisterWord_head():
    class ITfFnConfigureRegisterWord(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('bb95808a-6d8f-4bca-84-00-53-90-b5-86-ae-df')
    return ITfFnConfigureRegisterWord
def _define_ITfFnConfigureRegisterWord():
    ITfFnConfigureRegisterWord = win32more.UI.TextServices.ITfFnConfigureRegisterWord_head
    ITfFnConfigureRegisterWord.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt16,POINTER(Guid),win32more.Foundation.BSTR)(4, 'Show', ((1, 'hwndParent'),(1, 'langid'),(1, 'rguidProfile'),(1, 'bstrRegistered'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnConfigureRegisterWord
def _define_ITfFnCustomSpeechCommand_head():
    class ITfFnCustomSpeechCommand(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('fca6c349-a12f-43a3-8d-d6-5a-5a-42-82-57-7b')
    return ITfFnCustomSpeechCommand
def _define_ITfFnCustomSpeechCommand():
    ITfFnCustomSpeechCommand = win32more.UI.TextServices.ITfFnCustomSpeechCommand_head
    ITfFnCustomSpeechCommand.SetSpeechCommandProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(4, 'SetSpeechCommandProvider', ((1, 'pspcmdProvider'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnCustomSpeechCommand
def _define_ITfFnGetLinguisticAlternates_head():
    class ITfFnGetLinguisticAlternates(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('ea163ce2-7a65-4506-82-a3-c5-28-21-5d-a6-4e')
    return ITfFnGetLinguisticAlternates
def _define_ITfFnGetLinguisticAlternates():
    ITfFnGetLinguisticAlternates = win32more.UI.TextServices.ITfFnGetLinguisticAlternates_head
    ITfFnGetLinguisticAlternates.GetAlternates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfCandidateList_head))(4, 'GetAlternates', ((1, 'pRange'),(1, 'ppCandidateList'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnGetLinguisticAlternates
def _define_ITfFnGetPreferredTouchKeyboardLayout_head():
    class ITfFnGetPreferredTouchKeyboardLayout(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('5f309a41-590a-4acc-a9-7f-d8-ef-ff-13-fd-fc')
    return ITfFnGetPreferredTouchKeyboardLayout
def _define_ITfFnGetPreferredTouchKeyboardLayout():
    ITfFnGetPreferredTouchKeyboardLayout = win32more.UI.TextServices.ITfFnGetPreferredTouchKeyboardLayout_head
    ITfFnGetPreferredTouchKeyboardLayout.GetLayout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TKBLayoutType),POINTER(UInt16))(4, 'GetLayout', ((1, 'pTKBLayoutType'),(1, 'pwPreferredLayoutId'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnGetPreferredTouchKeyboardLayout
def _define_ITfFnGetSAPIObject_head():
    class ITfFnGetSAPIObject(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('5c0ab7ea-167d-4f59-bf-b5-46-93-75-5e-90-ca')
    return ITfFnGetSAPIObject
def _define_ITfFnGetSAPIObject():
    ITfFnGetSAPIObject = win32more.UI.TextServices.ITfFnGetSAPIObject_head
    ITfFnGetSAPIObject.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfSapiObject,POINTER(win32more.System.Com.IUnknown_head))(4, 'Get', ((1, 'sObj'),(1, 'ppunk'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnGetSAPIObject
def _define_ITfFnLangProfileUtil_head():
    class ITfFnLangProfileUtil(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('a87a8574-a6c1-4e15-99-f0-3d-39-65-f5-48-eb')
    return ITfFnLangProfileUtil
def _define_ITfFnLangProfileUtil():
    ITfFnLangProfileUtil = win32more.UI.TextServices.ITfFnLangProfileUtil_head
    ITfFnLangProfileUtil.RegisterActiveProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'RegisterActiveProfiles', ()))
    ITfFnLangProfileUtil.IsProfileAvailableForLang = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.BOOL))(5, 'IsProfileAvailableForLang', ((1, 'langid'),(1, 'pfAvailable'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnLangProfileUtil
def _define_ITfFnLMInternal_head():
    class ITfFnLMInternal(win32more.UI.TextServices.ITfFnLMProcessor_head):
        Guid = Guid('04b825b1-ac9a-4f7b-b5-ad-c7-16-8f-1e-e4-45')
    return ITfFnLMInternal
def _define_ITfFnLMInternal():
    ITfFnLMInternal = win32more.UI.TextServices.ITfFnLMInternal_head
    ITfFnLMInternal.ProcessLattice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head)(11, 'ProcessLattice', ((1, 'pRange'),)))
    win32more.UI.TextServices.ITfFnLMProcessor
    return ITfFnLMInternal
def _define_ITfFnLMProcessor_head():
    class ITfFnLMProcessor(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('7afbf8e7-ac4b-4082-b0-58-89-08-99-d3-a0-10')
    return ITfFnLMProcessor
def _define_ITfFnLMProcessor():
    ITfFnLMProcessor = win32more.UI.TextServices.ITfFnLMProcessor_head
    ITfFnLMProcessor.QueryRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfRange_head),POINTER(win32more.Foundation.BOOL))(4, 'QueryRange', ((1, 'pRange'),(1, 'ppNewRange'),(1, 'pfAccepted'),)))
    ITfFnLMProcessor.QueryLangID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.BOOL))(5, 'QueryLangID', ((1, 'langid'),(1, 'pfAccepted'),)))
    ITfFnLMProcessor.GetReconversion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfCandidateList_head))(6, 'GetReconversion', ((1, 'pRange'),(1, 'ppCandList'),)))
    ITfFnLMProcessor.Reconvert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head)(7, 'Reconvert', ((1, 'pRange'),)))
    ITfFnLMProcessor.QueryKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(8, 'QueryKey', ((1, 'fUp'),(1, 'vKey'),(1, 'lparamKeydata'),(1, 'pfInterested'),)))
    ITfFnLMProcessor.InvokeKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)(9, 'InvokeKey', ((1, 'fUp'),(1, 'vKey'),(1, 'lparamKeyData'),)))
    ITfFnLMProcessor.InvokeFunc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,POINTER(Guid))(10, 'InvokeFunc', ((1, 'pic'),(1, 'refguidFunc'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnLMProcessor
def _define_ITfFnPlayBack_head():
    class ITfFnPlayBack(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('a3a416a4-0f64-11d3-b5-b7-00-c0-4f-c3-24-a1')
    return ITfFnPlayBack
def _define_ITfFnPlayBack():
    ITfFnPlayBack = win32more.UI.TextServices.ITfFnPlayBack_head
    ITfFnPlayBack.QueryRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfRange_head),POINTER(win32more.Foundation.BOOL))(4, 'QueryRange', ((1, 'pRange'),(1, 'ppNewRange'),(1, 'pfPlayable'),)))
    ITfFnPlayBack.Play = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head)(5, 'Play', ((1, 'pRange'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnPlayBack
def _define_ITfFnPropertyUIStatus_head():
    class ITfFnPropertyUIStatus(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('2338ac6e-2b9d-44c0-a7-5e-ee-64-f2-56-b3-bd')
    return ITfFnPropertyUIStatus
def _define_ITfFnPropertyUIStatus():
    ITfFnPropertyUIStatus = win32more.UI.TextServices.ITfFnPropertyUIStatus_head
    ITfFnPropertyUIStatus.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32))(4, 'GetStatus', ((1, 'refguidProp'),(1, 'pdw'),)))
    ITfFnPropertyUIStatus.SetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32)(5, 'SetStatus', ((1, 'refguidProp'),(1, 'dw'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnPropertyUIStatus
def _define_ITfFnReconversion_head():
    class ITfFnReconversion(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('4cea93c0-0a58-11d3-8d-f0-00-10-5a-27-99-b5')
    return ITfFnReconversion
def _define_ITfFnReconversion():
    ITfFnReconversion = win32more.UI.TextServices.ITfFnReconversion_head
    ITfFnReconversion.QueryRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfRange_head),POINTER(win32more.Foundation.BOOL))(4, 'QueryRange', ((1, 'pRange'),(1, 'ppNewRange'),(1, 'pfConvertable'),)))
    ITfFnReconversion.GetReconversion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfCandidateList_head))(5, 'GetReconversion', ((1, 'pRange'),(1, 'ppCandList'),)))
    ITfFnReconversion.Reconvert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head)(6, 'Reconvert', ((1, 'pRange'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnReconversion
def _define_ITfFnSearchCandidateProvider_head():
    class ITfFnSearchCandidateProvider(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('87a2ad8f-f27b-4920-85-01-67-60-22-80-17-5d')
    return ITfFnSearchCandidateProvider
def _define_ITfFnSearchCandidateProvider():
    ITfFnSearchCandidateProvider = win32more.UI.TextServices.ITfFnSearchCandidateProvider_head
    ITfFnSearchCandidateProvider.GetSearchCandidates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.UI.TextServices.ITfCandidateList_head))(4, 'GetSearchCandidates', ((1, 'bstrQuery'),(1, 'bstrApplicationId'),(1, 'pplist'),)))
    ITfFnSearchCandidateProvider.SetResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR)(5, 'SetResult', ((1, 'bstrQuery'),(1, 'bstrApplicationID'),(1, 'bstrResult'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnSearchCandidateProvider
def _define_ITfFnShowHelp_head():
    class ITfFnShowHelp(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('5ab1d30c-094d-4c29-8e-a5-0b-f5-9b-e8-7b-f3')
    return ITfFnShowHelp
def _define_ITfFnShowHelp():
    ITfFnShowHelp = win32more.UI.TextServices.ITfFnShowHelp_head
    ITfFnShowHelp.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND)(4, 'Show', ((1, 'hwndParent'),)))
    win32more.UI.TextServices.ITfFunction
    return ITfFnShowHelp
def _define_ITfFunction_head():
    class ITfFunction(win32more.System.Com.IUnknown_head):
        Guid = Guid('db593490-098f-11d3-8d-f0-00-10-5a-27-99-b5')
    return ITfFunction
def _define_ITfFunction():
    ITfFunction = win32more.UI.TextServices.ITfFunction_head
    ITfFunction.GetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(3, 'GetDisplayName', ((1, 'pbstrName'),)))
    win32more.System.Com.IUnknown
    return ITfFunction
def _define_ITfFunctionProvider_head():
    class ITfFunctionProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('101d6610-0990-11d3-8d-f0-00-10-5a-27-99-b5')
    return ITfFunctionProvider
def _define_ITfFunctionProvider():
    ITfFunctionProvider = win32more.UI.TextServices.ITfFunctionProvider_head
    ITfFunctionProvider.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetType', ((1, 'pguid'),)))
    ITfFunctionProvider.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'GetDescription', ((1, 'pbstrDesc'),)))
    ITfFunctionProvider.GetFunction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(5, 'GetFunction', ((1, 'rguid'),(1, 'riid'),(1, 'ppunk'),)))
    win32more.System.Com.IUnknown
    return ITfFunctionProvider
def _define_ITfInputProcessorProfileActivationSink_head():
    class ITfInputProcessorProfileActivationSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('71c6e74e-0f28-11d8-a8-2a-00-06-5b-84-43-5c')
    return ITfInputProcessorProfileActivationSink
def _define_ITfInputProcessorProfileActivationSink():
    ITfInputProcessorProfileActivationSink = win32more.UI.TextServices.ITfInputProcessorProfileActivationSink_head
    ITfInputProcessorProfileActivationSink.OnActivated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt16,POINTER(Guid),POINTER(Guid),POINTER(Guid),win32more.UI.TextServices.HKL,UInt32)(3, 'OnActivated', ((1, 'dwProfileType'),(1, 'langid'),(1, 'clsid'),(1, 'catid'),(1, 'guidProfile'),(1, 'hkl'),(1, 'dwFlags'),)))
    win32more.System.Com.IUnknown
    return ITfInputProcessorProfileActivationSink
def _define_ITfInputProcessorProfileMgr_head():
    class ITfInputProcessorProfileMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('71c6e74c-0f28-11d8-a8-2a-00-06-5b-84-43-5c')
    return ITfInputProcessorProfileMgr
def _define_ITfInputProcessorProfileMgr():
    ITfInputProcessorProfileMgr = win32more.UI.TextServices.ITfInputProcessorProfileMgr_head
    ITfInputProcessorProfileMgr.ActivateProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt16,POINTER(Guid),POINTER(Guid),win32more.UI.TextServices.HKL,UInt32)(3, 'ActivateProfile', ((1, 'dwProfileType'),(1, 'langid'),(1, 'clsid'),(1, 'guidProfile'),(1, 'hkl'),(1, 'dwFlags'),)))
    ITfInputProcessorProfileMgr.DeactivateProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt16,POINTER(Guid),POINTER(Guid),win32more.UI.TextServices.HKL,UInt32)(4, 'DeactivateProfile', ((1, 'dwProfileType'),(1, 'langid'),(1, 'clsid'),(1, 'guidProfile'),(1, 'hkl'),(1, 'dwFlags'),)))
    ITfInputProcessorProfileMgr.GetProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt16,POINTER(Guid),POINTER(Guid),win32more.UI.TextServices.HKL,POINTER(win32more.UI.TextServices.TF_INPUTPROCESSORPROFILE_head))(5, 'GetProfile', ((1, 'dwProfileType'),(1, 'langid'),(1, 'clsid'),(1, 'guidProfile'),(1, 'hkl'),(1, 'pProfile'),)))
    ITfInputProcessorProfileMgr.EnumProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.UI.TextServices.IEnumTfInputProcessorProfiles_head))(6, 'EnumProfiles', ((1, 'langid'),(1, 'ppEnum'),)))
    ITfInputProcessorProfileMgr.ReleaseInputProcessor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32)(7, 'ReleaseInputProcessor', ((1, 'rclsid'),(1, 'dwFlags'),)))
    ITfInputProcessorProfileMgr.RegisterProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.UI.TextServices.HKL,UInt32,win32more.Foundation.BOOL,UInt32)(8, 'RegisterProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'pchDesc'),(1, 'cchDesc'),(1, 'pchIconFile'),(1, 'cchFile'),(1, 'uIconIndex'),(1, 'hklsubstitute'),(1, 'dwPreferredLayout'),(1, 'bEnabledByDefault'),(1, 'dwFlags'),)))
    ITfInputProcessorProfileMgr.UnregisterProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),UInt32)(9, 'UnregisterProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'dwFlags'),)))
    ITfInputProcessorProfileMgr.GetActiveProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.TF_INPUTPROCESSORPROFILE_head))(10, 'GetActiveProfile', ((1, 'catid'),(1, 'pProfile'),)))
    win32more.System.Com.IUnknown
    return ITfInputProcessorProfileMgr
def _define_ITfInputProcessorProfiles_head():
    class ITfInputProcessorProfiles(win32more.System.Com.IUnknown_head):
        Guid = Guid('1f02b6c5-7842-4ee6-8a-0b-9a-24-18-3a-95-ca')
    return ITfInputProcessorProfiles
def _define_ITfInputProcessorProfiles():
    ITfInputProcessorProfiles = win32more.UI.TextServices.ITfInputProcessorProfiles_head
    ITfInputProcessorProfiles.Register = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'Register', ((1, 'rclsid'),)))
    ITfInputProcessorProfiles.Unregister = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(4, 'Unregister', ((1, 'rclsid'),)))
    ITfInputProcessorProfiles.AddLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,UInt32)(5, 'AddLanguageProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'pchDesc'),(1, 'cchDesc'),(1, 'pchIconFile'),(1, 'cchFile'),(1, 'uIconIndex'),)))
    ITfInputProcessorProfiles.RemoveLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid))(6, 'RemoveLanguageProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),)))
    ITfInputProcessorProfiles.EnumInputProcessorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumGUID_head))(7, 'EnumInputProcessorInfo', ((1, 'ppEnum'),)))
    ITfInputProcessorProfiles.GetDefaultLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Guid),POINTER(Guid),POINTER(Guid))(8, 'GetDefaultLanguageProfile', ((1, 'langid'),(1, 'catid'),(1, 'pclsid'),(1, 'pguidProfile'),)))
    ITfInputProcessorProfiles.SetDefaultLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Guid),POINTER(Guid))(9, 'SetDefaultLanguageProfile', ((1, 'langid'),(1, 'rclsid'),(1, 'guidProfiles'),)))
    ITfInputProcessorProfiles.ActivateLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid))(10, 'ActivateLanguageProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfiles'),)))
    ITfInputProcessorProfiles.GetActiveLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt16),POINTER(Guid))(11, 'GetActiveLanguageProfile', ((1, 'rclsid'),(1, 'plangid'),(1, 'pguidProfile'),)))
    ITfInputProcessorProfiles.GetLanguageProfileDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),POINTER(win32more.Foundation.BSTR))(12, 'GetLanguageProfileDescription', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'pbstrProfile'),)))
    ITfInputProcessorProfiles.GetCurrentLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16))(13, 'GetCurrentLanguage', ((1, 'plangid'),)))
    ITfInputProcessorProfiles.ChangeCurrentLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16)(14, 'ChangeCurrentLanguage', ((1, 'langid'),)))
    ITfInputProcessorProfiles.GetLanguageList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)),POINTER(UInt32))(15, 'GetLanguageList', ((1, 'ppLangId'),(1, 'pulCount'),)))
    ITfInputProcessorProfiles.EnumLanguageProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.UI.TextServices.IEnumTfLanguageProfiles_head))(16, 'EnumLanguageProfiles', ((1, 'langid'),(1, 'ppEnum'),)))
    ITfInputProcessorProfiles.EnableLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),win32more.Foundation.BOOL)(17, 'EnableLanguageProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'fEnable'),)))
    ITfInputProcessorProfiles.IsEnabledLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),POINTER(win32more.Foundation.BOOL))(18, 'IsEnabledLanguageProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'pfEnable'),)))
    ITfInputProcessorProfiles.EnableLanguageProfileByDefault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),win32more.Foundation.BOOL)(19, 'EnableLanguageProfileByDefault', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'fEnable'),)))
    ITfInputProcessorProfiles.SubstituteKeyboardLayout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),win32more.UI.TextServices.HKL)(20, 'SubstituteKeyboardLayout', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'hKL'),)))
    win32more.System.Com.IUnknown
    return ITfInputProcessorProfiles
def _define_ITfInputProcessorProfilesEx_head():
    class ITfInputProcessorProfilesEx(win32more.UI.TextServices.ITfInputProcessorProfiles_head):
        Guid = Guid('892f230f-fe00-4a41-a9-8e-fc-d6-de-0d-35-ef')
    return ITfInputProcessorProfilesEx
def _define_ITfInputProcessorProfilesEx():
    ITfInputProcessorProfilesEx = win32more.UI.TextServices.ITfInputProcessorProfilesEx_head
    ITfInputProcessorProfilesEx.SetLanguageProfileDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),win32more.Foundation.PWSTR,UInt32,UInt32)(21, 'SetLanguageProfileDisplayName', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'pchFile'),(1, 'cchFile'),(1, 'uResId'),)))
    win32more.UI.TextServices.ITfInputProcessorProfiles
    return ITfInputProcessorProfilesEx
def _define_ITfInputProcessorProfileSubstituteLayout_head():
    class ITfInputProcessorProfileSubstituteLayout(win32more.System.Com.IUnknown_head):
        Guid = Guid('4fd67194-1002-4513-bf-f2-c0-dd-f6-25-85-52')
    return ITfInputProcessorProfileSubstituteLayout
def _define_ITfInputProcessorProfileSubstituteLayout():
    ITfInputProcessorProfileSubstituteLayout = win32more.UI.TextServices.ITfInputProcessorProfileSubstituteLayout_head
    ITfInputProcessorProfileSubstituteLayout.GetSubstituteKeyboardLayout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),POINTER(win32more.UI.TextServices.HKL))(3, 'GetSubstituteKeyboardLayout', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'phKL'),)))
    win32more.System.Com.IUnknown
    return ITfInputProcessorProfileSubstituteLayout
def _define_ITfInputScope_head():
    class ITfInputScope(win32more.System.Com.IUnknown_head):
        Guid = Guid('fde1eaee-6924-4cdf-91-e7-da-38-cf-f5-55-9d')
    return ITfInputScope
def _define_ITfInputScope():
    ITfInputScope = win32more.UI.TextServices.ITfInputScope_head
    ITfInputScope.GetInputScopes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.TextServices.InputScope)),POINTER(UInt32))(3, 'GetInputScopes', ((1, 'pprgInputScopes'),(1, 'pcCount'),)))
    ITfInputScope.GetPhrase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Foundation.BSTR)),POINTER(UInt32))(4, 'GetPhrase', ((1, 'ppbstrPhrases'),(1, 'pcCount'),)))
    ITfInputScope.GetRegularExpression = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(5, 'GetRegularExpression', ((1, 'pbstrRegExp'),)))
    ITfInputScope.GetSRGS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(6, 'GetSRGS', ((1, 'pbstrSRGS'),)))
    ITfInputScope.GetXML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'GetXML', ((1, 'pbstrXML'),)))
    win32more.System.Com.IUnknown
    return ITfInputScope
def _define_ITfInputScope2_head():
    class ITfInputScope2(win32more.UI.TextServices.ITfInputScope_head):
        Guid = Guid('5731eaa0-6bc2-4681-a5-32-92-fb-b7-4d-7c-41')
    return ITfInputScope2
def _define_ITfInputScope2():
    ITfInputScope2 = win32more.UI.TextServices.ITfInputScope2_head
    ITfInputScope2.EnumWordList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumString_head))(8, 'EnumWordList', ((1, 'ppEnumString'),)))
    win32more.UI.TextServices.ITfInputScope
    return ITfInputScope2
def _define_ITfInsertAtSelection_head():
    class ITfInsertAtSelection(win32more.System.Com.IUnknown_head):
        Guid = Guid('55ce16ba-3014-41c1-9c-eb-fa-de-14-46-ac-6c')
    return ITfInsertAtSelection
def _define_ITfInsertAtSelection():
    ITfInsertAtSelection = win32more.UI.TextServices.ITfInsertAtSelection_head
    ITfInsertAtSelection.InsertTextAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.INSERT_TEXT_AT_SELECTION_FLAGS,win32more.Foundation.PWSTR,Int32,POINTER(win32more.UI.TextServices.ITfRange_head))(3, 'InsertTextAtSelection', ((1, 'ec'),(1, 'dwFlags'),(1, 'pchText'),(1, 'cch'),(1, 'ppRange'),)))
    ITfInsertAtSelection.InsertEmbeddedAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.System.Com.IDataObject_head,POINTER(win32more.UI.TextServices.ITfRange_head))(4, 'InsertEmbeddedAtSelection', ((1, 'ec'),(1, 'dwFlags'),(1, 'pDataObject'),(1, 'ppRange'),)))
    win32more.System.Com.IUnknown
    return ITfInsertAtSelection
def _define_ITfIntegratableCandidateListUIElement_head():
    class ITfIntegratableCandidateListUIElement(win32more.System.Com.IUnknown_head):
        Guid = Guid('c7a6f54f-b180-416f-b2-bf-7b-f2-e4-68-3d-7b')
    return ITfIntegratableCandidateListUIElement
def _define_ITfIntegratableCandidateListUIElement():
    ITfIntegratableCandidateListUIElement = win32more.UI.TextServices.ITfIntegratableCandidateListUIElement_head
    ITfIntegratableCandidateListUIElement.SetIntegrationStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid)(3, 'SetIntegrationStyle', ((1, 'guidIntegrationStyle'),)))
    ITfIntegratableCandidateListUIElement.GetSelectionStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TfIntegratableCandidateListSelectionStyle))(4, 'GetSelectionStyle', ((1, 'ptfSelectionStyle'),)))
    ITfIntegratableCandidateListUIElement.OnKeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(5, 'OnKeyDown', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfIntegratableCandidateListUIElement.ShowCandidateNumbers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(6, 'ShowCandidateNumbers', ((1, 'pfShow'),)))
    ITfIntegratableCandidateListUIElement.FinalizeExactCompositionString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'FinalizeExactCompositionString', ()))
    win32more.System.Com.IUnknown
    return ITfIntegratableCandidateListUIElement
def _define_ITfKeyEventSink_head():
    class ITfKeyEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e7f5-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    return ITfKeyEventSink
def _define_ITfKeyEventSink():
    ITfKeyEventSink = win32more.UI.TextServices.ITfKeyEventSink_head
    ITfKeyEventSink.OnSetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(3, 'OnSetFocus', ((1, 'fForeground'),)))
    ITfKeyEventSink.OnTestKeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(4, 'OnTestKeyDown', ((1, 'pic'),(1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeyEventSink.OnTestKeyUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(5, 'OnTestKeyUp', ((1, 'pic'),(1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeyEventSink.OnKeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(6, 'OnKeyDown', ((1, 'pic'),(1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeyEventSink.OnKeyUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(7, 'OnKeyUp', ((1, 'pic'),(1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeyEventSink.OnPreservedKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,POINTER(Guid),POINTER(win32more.Foundation.BOOL))(8, 'OnPreservedKey', ((1, 'pic'),(1, 'rguid'),(1, 'pfEaten'),)))
    win32more.System.Com.IUnknown
    return ITfKeyEventSink
def _define_ITfKeystrokeMgr_head():
    class ITfKeystrokeMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e7f0-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    return ITfKeystrokeMgr
def _define_ITfKeystrokeMgr():
    ITfKeystrokeMgr = win32more.UI.TextServices.ITfKeystrokeMgr_head
    ITfKeystrokeMgr.AdviseKeyEventSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfKeyEventSink_head,win32more.Foundation.BOOL)(3, 'AdviseKeyEventSink', ((1, 'tid'),(1, 'pSink'),(1, 'fForeground'),)))
    ITfKeystrokeMgr.UnadviseKeyEventSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'UnadviseKeyEventSink', ((1, 'tid'),)))
    ITfKeystrokeMgr.GetForeground = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(5, 'GetForeground', ((1, 'pclsid'),)))
    ITfKeystrokeMgr.TestKeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(6, 'TestKeyDown', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeystrokeMgr.TestKeyUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(7, 'TestKeyUp', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeystrokeMgr.KeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(8, 'KeyDown', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeystrokeMgr.KeyUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL))(9, 'KeyUp', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeystrokeMgr.GetPreservedKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head),POINTER(Guid))(10, 'GetPreservedKey', ((1, 'pic'),(1, 'pprekey'),(1, 'pguid'),)))
    ITfKeystrokeMgr.IsPreservedKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head),POINTER(win32more.Foundation.BOOL))(11, 'IsPreservedKey', ((1, 'rguid'),(1, 'pprekey'),(1, 'pfRegistered'),)))
    ITfKeystrokeMgr.PreserveKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head),win32more.Foundation.PWSTR,UInt32)(12, 'PreserveKey', ((1, 'tid'),(1, 'rguid'),(1, 'prekey'),(1, 'pchDesc'),(1, 'cchDesc'),)))
    ITfKeystrokeMgr.UnpreserveKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head))(13, 'UnpreserveKey', ((1, 'rguid'),(1, 'pprekey'),)))
    ITfKeystrokeMgr.SetPreservedKeyDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,UInt32)(14, 'SetPreservedKeyDescription', ((1, 'rguid'),(1, 'pchDesc'),(1, 'cchDesc'),)))
    ITfKeystrokeMgr.GetPreservedKeyDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.BSTR))(15, 'GetPreservedKeyDescription', ((1, 'rguid'),(1, 'pbstrDesc'),)))
    ITfKeystrokeMgr.SimulatePreservedKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,POINTER(Guid),POINTER(win32more.Foundation.BOOL))(16, 'SimulatePreservedKey', ((1, 'pic'),(1, 'rguid'),(1, 'pfEaten'),)))
    win32more.System.Com.IUnknown
    return ITfKeystrokeMgr
def _define_ITfKeyTraceEventSink_head():
    class ITfKeyTraceEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('1cd4c13b-1c36-4191-a7-0a-7f-3e-61-1f-36-7d')
    return ITfKeyTraceEventSink
def _define_ITfKeyTraceEventSink():
    ITfKeyTraceEventSink = win32more.UI.TextServices.ITfKeyTraceEventSink_head
    ITfKeyTraceEventSink.OnKeyTraceDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)(3, 'OnKeyTraceDown', ((1, 'wParam'),(1, 'lParam'),)))
    ITfKeyTraceEventSink.OnKeyTraceUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)(4, 'OnKeyTraceUp', ((1, 'wParam'),(1, 'lParam'),)))
    win32more.System.Com.IUnknown
    return ITfKeyTraceEventSink
def _define_ITfLangBarEventSink_head():
    class ITfLangBarEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('18a4e900-e0ae-11d2-af-dd-00-10-5a-27-99-b5')
    return ITfLangBarEventSink
def _define_ITfLangBarEventSink():
    ITfLangBarEventSink = win32more.UI.TextServices.ITfLangBarEventSink_head
    ITfLangBarEventSink.OnSetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'OnSetFocus', ((1, 'dwThreadId'),)))
    ITfLangBarEventSink.OnThreadTerminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'OnThreadTerminate', ((1, 'dwThreadId'),)))
    ITfLangBarEventSink.OnThreadItemChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'OnThreadItemChange', ((1, 'dwThreadId'),)))
    ITfLangBarEventSink.OnModalInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)(6, 'OnModalInput', ((1, 'dwThreadId'),(1, 'uMsg'),(1, 'wParam'),(1, 'lParam'),)))
    ITfLangBarEventSink.ShowFloating = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'ShowFloating', ((1, 'dwFlags'),)))
    ITfLangBarEventSink.GetItemFloatingRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.Foundation.RECT_head))(8, 'GetItemFloatingRect', ((1, 'dwThreadId'),(1, 'rguid'),(1, 'prc'),)))
    win32more.System.Com.IUnknown
    return ITfLangBarEventSink
def _define_ITfLangBarItem_head():
    class ITfLangBarItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('73540d69-edeb-4ee9-96-c9-23-aa-30-b2-59-16')
    return ITfLangBarItem
def _define_ITfLangBarItem():
    ITfLangBarItem = win32more.UI.TextServices.ITfLangBarItem_head
    ITfLangBarItem.GetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TF_LANGBARITEMINFO_head))(3, 'GetInfo', ((1, 'pInfo'),)))
    ITfLangBarItem.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetStatus', ((1, 'pdwStatus'),)))
    ITfLangBarItem.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(5, 'Show', ((1, 'fShow'),)))
    ITfLangBarItem.GetTooltipString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(6, 'GetTooltipString', ((1, 'pbstrToolTip'),)))
    win32more.System.Com.IUnknown
    return ITfLangBarItem
def _define_ITfLangBarItemBalloon_head():
    class ITfLangBarItemBalloon(win32more.UI.TextServices.ITfLangBarItem_head):
        Guid = Guid('01c2d285-d3c7-4b7b-b5-b5-d9-74-11-d0-c2-83')
    return ITfLangBarItemBalloon
def _define_ITfLangBarItemBalloon():
    ITfLangBarItemBalloon = win32more.UI.TextServices.ITfLangBarItemBalloon_head
    ITfLangBarItemBalloon.OnClick = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfLBIClick,win32more.Foundation.POINT,POINTER(win32more.Foundation.RECT_head))(7, 'OnClick', ((1, 'click'),(1, 'pt'),(1, 'prcArea'),)))
    ITfLangBarItemBalloon.GetPreferredSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SIZE_head),POINTER(win32more.Foundation.SIZE_head))(8, 'GetPreferredSize', ((1, 'pszDefault'),(1, 'psz'),)))
    ITfLangBarItemBalloon.GetBalloonInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TF_LBBALLOONINFO_head))(9, 'GetBalloonInfo', ((1, 'pInfo'),)))
    win32more.UI.TextServices.ITfLangBarItem
    return ITfLangBarItemBalloon
def _define_ITfLangBarItemBitmap_head():
    class ITfLangBarItemBitmap(win32more.UI.TextServices.ITfLangBarItem_head):
        Guid = Guid('73830352-d722-4179-ad-a5-f0-45-c9-8d-f3-55')
    return ITfLangBarItemBitmap
def _define_ITfLangBarItemBitmap():
    ITfLangBarItemBitmap = win32more.UI.TextServices.ITfLangBarItemBitmap_head
    ITfLangBarItemBitmap.OnClick = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfLBIClick,win32more.Foundation.POINT,POINTER(win32more.Foundation.RECT_head))(7, 'OnClick', ((1, 'click'),(1, 'pt'),(1, 'prcArea'),)))
    ITfLangBarItemBitmap.GetPreferredSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SIZE_head),POINTER(win32more.Foundation.SIZE_head))(8, 'GetPreferredSize', ((1, 'pszDefault'),(1, 'psz'),)))
    ITfLangBarItemBitmap.DrawBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(win32more.Graphics.Gdi.HBITMAP),POINTER(win32more.Graphics.Gdi.HBITMAP))(9, 'DrawBitmap', ((1, 'bmWidth'),(1, 'bmHeight'),(1, 'dwFlags'),(1, 'phbmp'),(1, 'phbmpMask'),)))
    win32more.UI.TextServices.ITfLangBarItem
    return ITfLangBarItemBitmap
def _define_ITfLangBarItemBitmapButton_head():
    class ITfLangBarItemBitmapButton(win32more.UI.TextServices.ITfLangBarItem_head):
        Guid = Guid('a26a0525-3fae-4fa0-89-ee-88-a9-64-f9-f1-b5')
    return ITfLangBarItemBitmapButton
def _define_ITfLangBarItemBitmapButton():
    ITfLangBarItemBitmapButton = win32more.UI.TextServices.ITfLangBarItemBitmapButton_head
    ITfLangBarItemBitmapButton.OnClick = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfLBIClick,win32more.Foundation.POINT,POINTER(win32more.Foundation.RECT_head))(7, 'OnClick', ((1, 'click'),(1, 'pt'),(1, 'prcArea'),)))
    ITfLangBarItemBitmapButton.InitMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfMenu_head)(8, 'InitMenu', ((1, 'pMenu'),)))
    ITfLangBarItemBitmapButton.OnMenuSelect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(9, 'OnMenuSelect', ((1, 'wID'),)))
    ITfLangBarItemBitmapButton.GetPreferredSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SIZE_head),POINTER(win32more.Foundation.SIZE_head))(10, 'GetPreferredSize', ((1, 'pszDefault'),(1, 'psz'),)))
    ITfLangBarItemBitmapButton.DrawBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(win32more.Graphics.Gdi.HBITMAP),POINTER(win32more.Graphics.Gdi.HBITMAP))(11, 'DrawBitmap', ((1, 'bmWidth'),(1, 'bmHeight'),(1, 'dwFlags'),(1, 'phbmp'),(1, 'phbmpMask'),)))
    ITfLangBarItemBitmapButton.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'GetText', ((1, 'pbstrText'),)))
    win32more.UI.TextServices.ITfLangBarItem
    return ITfLangBarItemBitmapButton
def _define_ITfLangBarItemButton_head():
    class ITfLangBarItemButton(win32more.UI.TextServices.ITfLangBarItem_head):
        Guid = Guid('28c7f1d0-de25-11d2-af-dd-00-10-5a-27-99-b5')
    return ITfLangBarItemButton
def _define_ITfLangBarItemButton():
    ITfLangBarItemButton = win32more.UI.TextServices.ITfLangBarItemButton_head
    ITfLangBarItemButton.OnClick = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfLBIClick,win32more.Foundation.POINT,POINTER(win32more.Foundation.RECT_head))(7, 'OnClick', ((1, 'click'),(1, 'pt'),(1, 'prcArea'),)))
    ITfLangBarItemButton.InitMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfMenu_head)(8, 'InitMenu', ((1, 'pMenu'),)))
    ITfLangBarItemButton.OnMenuSelect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(9, 'OnMenuSelect', ((1, 'wID'),)))
    ITfLangBarItemButton.GetIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.HICON))(10, 'GetIcon', ((1, 'phIcon'),)))
    ITfLangBarItemButton.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'GetText', ((1, 'pbstrText'),)))
    win32more.UI.TextServices.ITfLangBarItem
    return ITfLangBarItemButton
def _define_ITfLangBarItemMgr_head():
    class ITfLangBarItemMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('ba468c55-9956-4fb1-a5-9d-52-a7-dd-7c-c6-aa')
    return ITfLangBarItemMgr
def _define_ITfLangBarItemMgr():
    ITfLangBarItemMgr = win32more.UI.TextServices.ITfLangBarItemMgr_head
    ITfLangBarItemMgr.EnumItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfLangBarItems_head))(3, 'EnumItems', ((1, 'ppEnum'),)))
    ITfLangBarItemMgr.GetItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfLangBarItem_head))(4, 'GetItem', ((1, 'rguid'),(1, 'ppItem'),)))
    ITfLangBarItemMgr.AddItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfLangBarItem_head)(5, 'AddItem', ((1, 'punk'),)))
    ITfLangBarItemMgr.RemoveItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfLangBarItem_head)(6, 'RemoveItem', ((1, 'punk'),)))
    ITfLangBarItemMgr.AdviseItemSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfLangBarItemSink_head,POINTER(UInt32),POINTER(Guid))(7, 'AdviseItemSink', ((1, 'punk'),(1, 'pdwCookie'),(1, 'rguidItem'),)))
    ITfLangBarItemMgr.UnadviseItemSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(8, 'UnadviseItemSink', ((1, 'dwCookie'),)))
    ITfLangBarItemMgr.GetItemFloatingRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.Foundation.RECT_head))(9, 'GetItemFloatingRect', ((1, 'dwThreadId'),(1, 'rguid'),(1, 'prc'),)))
    ITfLangBarItemMgr.GetItemsStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt32))(10, 'GetItemsStatus', ((1, 'ulCount'),(1, 'prgguid'),(1, 'pdwStatus'),)))
    ITfLangBarItemMgr.GetItemNum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(11, 'GetItemNum', ((1, 'pulCount'),)))
    ITfLangBarItemMgr.GetItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfLangBarItem_head),POINTER(win32more.UI.TextServices.TF_LANGBARITEMINFO_head),POINTER(UInt32),POINTER(UInt32))(12, 'GetItems', ((1, 'ulCount'),(1, 'ppItem'),(1, 'pInfo'),(1, 'pdwStatus'),(1, 'pcFetched'),)))
    ITfLangBarItemMgr.AdviseItemsSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfLangBarItemSink_head),POINTER(Guid),POINTER(UInt32))(13, 'AdviseItemsSink', ((1, 'ulCount'),(1, 'ppunk'),(1, 'pguidItem'),(1, 'pdwCookie'),)))
    ITfLangBarItemMgr.UnadviseItemsSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(14, 'UnadviseItemsSink', ((1, 'ulCount'),(1, 'pdwCookie'),)))
    win32more.System.Com.IUnknown
    return ITfLangBarItemMgr
def _define_ITfLangBarItemSink_head():
    class ITfLangBarItemSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('57dbe1a0-de25-11d2-af-dd-00-10-5a-27-99-b5')
    return ITfLangBarItemSink
def _define_ITfLangBarItemSink():
    ITfLangBarItemSink = win32more.UI.TextServices.ITfLangBarItemSink_head
    ITfLangBarItemSink.OnUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'OnUpdate', ((1, 'dwFlags'),)))
    win32more.System.Com.IUnknown
    return ITfLangBarItemSink
def _define_ITfLangBarMgr_head():
    class ITfLangBarMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('87955690-e627-11d2-8d-db-00-10-5a-27-99-b5')
    return ITfLangBarMgr
def _define_ITfLangBarMgr():
    ITfLangBarMgr = win32more.UI.TextServices.ITfLangBarMgr_head
    ITfLangBarMgr.AdviseEventSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfLangBarEventSink_head,win32more.Foundation.HWND,UInt32,POINTER(UInt32))(3, 'AdviseEventSink', ((1, 'pSink'),(1, 'hwnd'),(1, 'dwFlags'),(1, 'pdwCookie'),)))
    ITfLangBarMgr.UnadviseEventSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'UnadviseEventSink', ((1, 'dwCookie'),)))
    ITfLangBarMgr.GetThreadMarshalInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(5, 'GetThreadMarshalInterface', ((1, 'dwThreadId'),(1, 'dwType'),(1, 'riid'),(1, 'ppunk'),)))
    ITfLangBarMgr.GetThreadLangBarItemMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfLangBarItemMgr_head),POINTER(UInt32))(6, 'GetThreadLangBarItemMgr', ((1, 'dwThreadId'),(1, 'pplbi'),(1, 'pdwThreadid'),)))
    ITfLangBarMgr.GetInputProcessorProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfInputProcessorProfiles_head),POINTER(UInt32))(7, 'GetInputProcessorProfiles', ((1, 'dwThreadId'),(1, 'ppaip'),(1, 'pdwThreadid'),)))
    ITfLangBarMgr.RestoreLastFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),win32more.Foundation.BOOL)(8, 'RestoreLastFocus', ((1, 'pdwThreadId'),(1, 'fPrev'),)))
    ITfLangBarMgr.SetModalInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfLangBarEventSink_head,UInt32,UInt32)(9, 'SetModalInput', ((1, 'pSink'),(1, 'dwThreadId'),(1, 'dwFlags'),)))
    ITfLangBarMgr.ShowFloating = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(10, 'ShowFloating', ((1, 'dwFlags'),)))
    ITfLangBarMgr.GetShowFloatingStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(11, 'GetShowFloatingStatus', ((1, 'pdwFlags'),)))
    win32more.System.Com.IUnknown
    return ITfLangBarMgr
def _define_ITfLanguageProfileNotifySink_head():
    class ITfLanguageProfileNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('43c9fe15-f494-4c17-9d-e2-b8-a4-ac-35-0a-a8')
    return ITfLanguageProfileNotifySink
def _define_ITfLanguageProfileNotifySink():
    ITfLanguageProfileNotifySink = win32more.UI.TextServices.ITfLanguageProfileNotifySink_head
    ITfLanguageProfileNotifySink.OnLanguageChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.BOOL))(3, 'OnLanguageChange', ((1, 'langid'),(1, 'pfAccept'),)))
    ITfLanguageProfileNotifySink.OnLanguageChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'OnLanguageChanged', ()))
    win32more.System.Com.IUnknown
    return ITfLanguageProfileNotifySink
def _define_ITfLMLattice_head():
    class ITfLMLattice(win32more.System.Com.IUnknown_head):
        Guid = Guid('d4236675-a5bf-4570-9d-42-5d-6d-7b-02-d5-9b')
    return ITfLMLattice
def _define_ITfLMLattice():
    ITfLMLattice = win32more.UI.TextServices.ITfLMLattice_head
    ITfLMLattice.QueryType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.BOOL))(3, 'QueryType', ((1, 'rguidType'),(1, 'pfSupported'),)))
    ITfLMLattice.EnumLatticeElements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.UI.TextServices.IEnumTfLatticeElements_head))(4, 'EnumLatticeElements', ((1, 'dwFrameStart'),(1, 'rguidType'),(1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return ITfLMLattice
def _define_ITfMenu_head():
    class ITfMenu(win32more.System.Com.IUnknown_head):
        Guid = Guid('6f8a98e4-aaa0-4f15-8c-5b-07-e0-df-0a-3d-d8')
    return ITfMenu
def _define_ITfMenu():
    ITfMenu = win32more.UI.TextServices.ITfMenu_head
    ITfMenu.AddMenuItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Graphics.Gdi.HBITMAP,win32more.Graphics.Gdi.HBITMAP,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.UI.TextServices.ITfMenu_head))(3, 'AddMenuItem', ((1, 'uId'),(1, 'dwFlags'),(1, 'hbmp'),(1, 'hbmpMask'),(1, 'pch'),(1, 'cch'),(1, 'ppMenu'),)))
    win32more.System.Com.IUnknown
    return ITfMenu
def _define_ITfMessagePump_head():
    class ITfMessagePump(win32more.System.Com.IUnknown_head):
        Guid = Guid('8f1b8ad8-0b6b-4874-90-c5-bd-76-01-1e-8f-7c')
    return ITfMessagePump
def _define_ITfMessagePump():
    ITfMessagePump = win32more.UI.TextServices.ITfMessagePump_head
    ITfMessagePump.PeekMessageA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),win32more.Foundation.HWND,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.BOOL))(3, 'PeekMessageA', ((1, 'pMsg'),(1, 'hwnd'),(1, 'wMsgFilterMin'),(1, 'wMsgFilterMax'),(1, 'wRemoveMsg'),(1, 'pfResult'),)))
    ITfMessagePump.GetMessageA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),win32more.Foundation.HWND,UInt32,UInt32,POINTER(win32more.Foundation.BOOL))(4, 'GetMessageA', ((1, 'pMsg'),(1, 'hwnd'),(1, 'wMsgFilterMin'),(1, 'wMsgFilterMax'),(1, 'pfResult'),)))
    ITfMessagePump.PeekMessageW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),win32more.Foundation.HWND,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.BOOL))(5, 'PeekMessageW', ((1, 'pMsg'),(1, 'hwnd'),(1, 'wMsgFilterMin'),(1, 'wMsgFilterMax'),(1, 'wRemoveMsg'),(1, 'pfResult'),)))
    ITfMessagePump.GetMessageW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),win32more.Foundation.HWND,UInt32,UInt32,POINTER(win32more.Foundation.BOOL))(6, 'GetMessageW', ((1, 'pMsg'),(1, 'hwnd'),(1, 'wMsgFilterMin'),(1, 'wMsgFilterMax'),(1, 'pfResult'),)))
    win32more.System.Com.IUnknown
    return ITfMessagePump
def _define_ITfMouseSink_head():
    class ITfMouseSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('a1adaaa2-3a24-449d-ac-96-51-83-e7-f5-c2-17')
    return ITfMouseSink
def _define_ITfMouseSink():
    ITfMouseSink = win32more.UI.TextServices.ITfMouseSink_head
    ITfMouseSink.OnMouseEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.BOOL))(3, 'OnMouseEvent', ((1, 'uEdge'),(1, 'uQuadrant'),(1, 'dwBtnStatus'),(1, 'pfEaten'),)))
    win32more.System.Com.IUnknown
    return ITfMouseSink
def _define_ITfMouseTracker_head():
    class ITfMouseTracker(win32more.System.Com.IUnknown_head):
        Guid = Guid('09d146cd-a544-4132-92-5b-7a-fa-8e-f3-22-d0')
    return ITfMouseTracker
def _define_ITfMouseTracker():
    ITfMouseTracker = win32more.UI.TextServices.ITfMouseTracker_head
    ITfMouseTracker.AdviseMouseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfMouseSink_head,POINTER(UInt32))(3, 'AdviseMouseSink', ((1, 'range'),(1, 'pSink'),(1, 'pdwCookie'),)))
    ITfMouseTracker.UnadviseMouseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'UnadviseMouseSink', ((1, 'dwCookie'),)))
    win32more.System.Com.IUnknown
    return ITfMouseTracker
def _define_ITfMouseTrackerACP_head():
    class ITfMouseTrackerACP(win32more.System.Com.IUnknown_head):
        Guid = Guid('3bdd78e2-c16e-47fd-b8-83-ce-6f-ac-c1-a2-08')
    return ITfMouseTrackerACP
def _define_ITfMouseTrackerACP():
    ITfMouseTrackerACP = win32more.UI.TextServices.ITfMouseTrackerACP_head
    ITfMouseTrackerACP.AdviseMouseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRangeACP_head,win32more.UI.TextServices.ITfMouseSink_head,POINTER(UInt32))(3, 'AdviseMouseSink', ((1, 'range'),(1, 'pSink'),(1, 'pdwCookie'),)))
    ITfMouseTrackerACP.UnadviseMouseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'UnadviseMouseSink', ((1, 'dwCookie'),)))
    win32more.System.Com.IUnknown
    return ITfMouseTrackerACP
def _define_ITfMSAAControl_head():
    class ITfMSAAControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('b5f8fb3b-393f-4f7c-84-cb-50-49-24-c2-70-5a')
    return ITfMSAAControl
def _define_ITfMSAAControl():
    ITfMSAAControl = win32more.UI.TextServices.ITfMSAAControl_head
    ITfMSAAControl.SystemEnableMSAA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'SystemEnableMSAA', ()))
    ITfMSAAControl.SystemDisableMSAA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'SystemDisableMSAA', ()))
    win32more.System.Com.IUnknown
    return ITfMSAAControl
def _define_ITfPersistentPropertyLoaderACP_head():
    class ITfPersistentPropertyLoaderACP(win32more.System.Com.IUnknown_head):
        Guid = Guid('4ef89150-0807-11d3-8d-f0-00-10-5a-27-99-b5')
    return ITfPersistentPropertyLoaderACP
def _define_ITfPersistentPropertyLoaderACP():
    ITfPersistentPropertyLoaderACP = win32more.UI.TextServices.ITfPersistentPropertyLoaderACP_head
    ITfPersistentPropertyLoaderACP.LoadProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head),POINTER(win32more.System.Com.IStream_head))(3, 'LoadProperty', ((1, 'pHdr'),(1, 'ppStream'),)))
    win32more.System.Com.IUnknown
    return ITfPersistentPropertyLoaderACP
def _define_ITfPreservedKeyNotifySink_head():
    class ITfPreservedKeyNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('6f77c993-d2b1-446e-85-3e-59-12-ef-c8-a2-86')
    return ITfPreservedKeyNotifySink
def _define_ITfPreservedKeyNotifySink():
    ITfPreservedKeyNotifySink = win32more.UI.TextServices.ITfPreservedKeyNotifySink_head
    ITfPreservedKeyNotifySink.OnUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head))(3, 'OnUpdated', ((1, 'pprekey'),)))
    win32more.System.Com.IUnknown
    return ITfPreservedKeyNotifySink
def _define_ITfProperty_head():
    class ITfProperty(win32more.UI.TextServices.ITfReadOnlyProperty_head):
        Guid = Guid('e2449660-9542-11d2-bf-46-00-10-5a-27-99-b5')
    return ITfProperty
def _define_ITfProperty():
    ITfProperty = win32more.UI.TextServices.ITfProperty_head
    ITfProperty.FindRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfRange_head),win32more.UI.TextServices.TfAnchor)(7, 'FindRange', ((1, 'ec'),(1, 'pRange'),(1, 'ppRange'),(1, 'aPos'),)))
    ITfProperty.SetValueStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfPropertyStore_head)(8, 'SetValueStore', ((1, 'ec'),(1, 'pRange'),(1, 'pPropStore'),)))
    ITfProperty.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.System.Com.VARIANT_head))(9, 'SetValue', ((1, 'ec'),(1, 'pRange'),(1, 'pvarValue'),)))
    ITfProperty.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head)(10, 'Clear', ((1, 'ec'),(1, 'pRange'),)))
    win32more.UI.TextServices.ITfReadOnlyProperty
    return ITfProperty
def _define_ITfPropertyStore_head():
    class ITfPropertyStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('6834b120-88cb-11d2-bf-45-00-10-5a-27-99-b5')
    return ITfPropertyStore
def _define_ITfPropertyStore():
    ITfPropertyStore = win32more.UI.TextServices.ITfPropertyStore_head
    ITfPropertyStore.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetType', ((1, 'pguid'),)))
    ITfPropertyStore.GetDataType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetDataType', ((1, 'pdwReserved'),)))
    ITfPropertyStore.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(5, 'GetData', ((1, 'pvarValue'),)))
    ITfPropertyStore.OnTextUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.Foundation.BOOL))(6, 'OnTextUpdated', ((1, 'dwFlags'),(1, 'pRangeNew'),(1, 'pfAccept'),)))
    ITfPropertyStore.Shrink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.Foundation.BOOL))(7, 'Shrink', ((1, 'pRangeNew'),(1, 'pfFree'),)))
    ITfPropertyStore.Divide = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfPropertyStore_head))(8, 'Divide', ((1, 'pRangeThis'),(1, 'pRangeNew'),(1, 'ppPropStore'),)))
    ITfPropertyStore.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfPropertyStore_head))(9, 'Clone', ((1, 'pPropStore'),)))
    ITfPropertyStore.GetPropertyRangeCreator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(10, 'GetPropertyRangeCreator', ((1, 'pclsid'),)))
    ITfPropertyStore.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(UInt32))(11, 'Serialize', ((1, 'pStream'),(1, 'pcb'),)))
    win32more.System.Com.IUnknown
    return ITfPropertyStore
def _define_ITfQueryEmbedded_head():
    class ITfQueryEmbedded(win32more.System.Com.IUnknown_head):
        Guid = Guid('0fab9bdb-d250-4169-84-e5-6b-e1-18-fd-d7-a8')
    return ITfQueryEmbedded
def _define_ITfQueryEmbedded():
    ITfQueryEmbedded = win32more.UI.TextServices.ITfQueryEmbedded_head
    ITfQueryEmbedded.QueryInsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.Foundation.BOOL))(3, 'QueryInsertEmbedded', ((1, 'pguidService'),(1, 'pFormatEtc'),(1, 'pfInsertable'),)))
    win32more.System.Com.IUnknown
    return ITfQueryEmbedded
def _define_ITfRange_head():
    class ITfRange(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e7ff-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    return ITfRange
def _define_ITfRange():
    ITfRange = win32more.UI.TextServices.ITfRange_head
    ITfRange.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(3, 'GetText', ((1, 'ec'),(1, 'dwFlags'),(1, 'pchText'),(1, 'cchMax'),(1, 'pcch'),)))
    ITfRange.SetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.PWSTR,Int32)(4, 'SetText', ((1, 'ec'),(1, 'dwFlags'),(1, 'pchText'),(1, 'cch'),)))
    ITfRange.GetFormattedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IDataObject_head))(5, 'GetFormattedText', ((1, 'ec'),(1, 'ppDataObject'),)))
    ITfRange.GetEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(6, 'GetEmbedded', ((1, 'ec'),(1, 'rguidService'),(1, 'riid'),(1, 'ppunk'),)))
    ITfRange.InsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.System.Com.IDataObject_head)(7, 'InsertEmbedded', ((1, 'ec'),(1, 'dwFlags'),(1, 'pDataObject'),)))
    ITfRange.ShiftStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,POINTER(Int32),POINTER(win32more.UI.TextServices.TF_HALTCOND_head))(8, 'ShiftStart', ((1, 'ec'),(1, 'cchReq'),(1, 'pcch'),(1, 'pHalt'),)))
    ITfRange.ShiftEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,POINTER(Int32),POINTER(win32more.UI.TextServices.TF_HALTCOND_head))(9, 'ShiftEnd', ((1, 'ec'),(1, 'cchReq'),(1, 'pcch'),(1, 'pHalt'),)))
    ITfRange.ShiftStartToRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.TfAnchor)(10, 'ShiftStartToRange', ((1, 'ec'),(1, 'pRange'),(1, 'aPos'),)))
    ITfRange.ShiftEndToRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.TfAnchor)(11, 'ShiftEndToRange', ((1, 'ec'),(1, 'pRange'),(1, 'aPos'),)))
    ITfRange.ShiftStartRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.TfShiftDir,POINTER(win32more.Foundation.BOOL))(12, 'ShiftStartRegion', ((1, 'ec'),(1, 'dir'),(1, 'pfNoRegion'),)))
    ITfRange.ShiftEndRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.TfShiftDir,POINTER(win32more.Foundation.BOOL))(13, 'ShiftEndRegion', ((1, 'ec'),(1, 'dir'),(1, 'pfNoRegion'),)))
    ITfRange.IsEmpty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL))(14, 'IsEmpty', ((1, 'ec'),(1, 'pfEmpty'),)))
    ITfRange.Collapse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.TfAnchor)(15, 'Collapse', ((1, 'ec'),(1, 'aPos'),)))
    ITfRange.IsEqualStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.TfAnchor,POINTER(win32more.Foundation.BOOL))(16, 'IsEqualStart', ((1, 'ec'),(1, 'pWith'),(1, 'aPos'),(1, 'pfEqual'),)))
    ITfRange.IsEqualEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.TfAnchor,POINTER(win32more.Foundation.BOOL))(17, 'IsEqualEnd', ((1, 'ec'),(1, 'pWith'),(1, 'aPos'),(1, 'pfEqual'),)))
    ITfRange.CompareStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.TfAnchor,POINTER(Int32))(18, 'CompareStart', ((1, 'ec'),(1, 'pWith'),(1, 'aPos'),(1, 'plResult'),)))
    ITfRange.CompareEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.TfAnchor,POINTER(Int32))(19, 'CompareEnd', ((1, 'ec'),(1, 'pWith'),(1, 'aPos'),(1, 'plResult'),)))
    ITfRange.AdjustForInsert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Foundation.BOOL))(20, 'AdjustForInsert', ((1, 'ec'),(1, 'cchInsert'),(1, 'pfInsertOk'),)))
    ITfRange.GetGravity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TfGravity),POINTER(win32more.UI.TextServices.TfGravity))(21, 'GetGravity', ((1, 'pgStart'),(1, 'pgEnd'),)))
    ITfRange.SetGravity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.TfGravity,win32more.UI.TextServices.TfGravity)(22, 'SetGravity', ((1, 'ec'),(1, 'gStart'),(1, 'gEnd'),)))
    ITfRange.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfRange_head))(23, 'Clone', ((1, 'ppClone'),)))
    ITfRange.GetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfContext_head))(24, 'GetContext', ((1, 'ppContext'),)))
    win32more.System.Com.IUnknown
    return ITfRange
def _define_ITfRangeACP_head():
    class ITfRangeACP(win32more.UI.TextServices.ITfRange_head):
        Guid = Guid('057a6296-029b-4154-b7-9a-0d-46-1d-4e-a9-4c')
    return ITfRangeACP
def _define_ITfRangeACP():
    ITfRangeACP = win32more.UI.TextServices.ITfRangeACP_head
    ITfRangeACP.GetExtent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32))(25, 'GetExtent', ((1, 'pacpAnchor'),(1, 'pcch'),)))
    ITfRangeACP.SetExtent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32)(26, 'SetExtent', ((1, 'acpAnchor'),(1, 'cch'),)))
    win32more.UI.TextServices.ITfRange
    return ITfRangeACP
def _define_ITfRangeBackup_head():
    class ITfRangeBackup(win32more.System.Com.IUnknown_head):
        Guid = Guid('463a506d-6992-49d2-9b-88-93-d5-5e-70-bb-16')
    return ITfRangeBackup
def _define_ITfRangeBackup():
    ITfRangeBackup = win32more.UI.TextServices.ITfRangeBackup_head
    ITfRangeBackup.Restore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head)(3, 'Restore', ((1, 'ec'),(1, 'pRange'),)))
    win32more.System.Com.IUnknown
    return ITfRangeBackup
def _define_ITfReadingInformationUIElement_head():
    class ITfReadingInformationUIElement(win32more.UI.TextServices.ITfUIElement_head):
        Guid = Guid('ea1ea139-19df-11d7-a6-d2-00-06-5b-84-43-5c')
    return ITfReadingInformationUIElement
def _define_ITfReadingInformationUIElement():
    ITfReadingInformationUIElement = win32more.UI.TextServices.ITfReadingInformationUIElement_head
    ITfReadingInformationUIElement.GetUpdatedFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(7, 'GetUpdatedFlags', ((1, 'pdwFlags'),)))
    ITfReadingInformationUIElement.GetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfContext_head))(8, 'GetContext', ((1, 'ppic'),)))
    ITfReadingInformationUIElement.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'GetString', ((1, 'pstr'),)))
    ITfReadingInformationUIElement.GetMaxReadingStringLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(10, 'GetMaxReadingStringLength', ((1, 'pcchMax'),)))
    ITfReadingInformationUIElement.GetErrorIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(11, 'GetErrorIndex', ((1, 'pErrorIndex'),)))
    ITfReadingInformationUIElement.IsVerticalOrderPreferred = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(12, 'IsVerticalOrderPreferred', ((1, 'pfVertical'),)))
    win32more.UI.TextServices.ITfUIElement
    return ITfReadingInformationUIElement
def _define_ITfReadOnlyProperty_head():
    class ITfReadOnlyProperty(win32more.System.Com.IUnknown_head):
        Guid = Guid('17d49a3d-f8b8-4b2f-b2-54-52-31-9d-d6-4c-53')
    return ITfReadOnlyProperty
def _define_ITfReadOnlyProperty():
    ITfReadOnlyProperty = win32more.UI.TextServices.ITfReadOnlyProperty_head
    ITfReadOnlyProperty.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetType', ((1, 'pguid'),)))
    ITfReadOnlyProperty.EnumRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.IEnumTfRanges_head),win32more.UI.TextServices.ITfRange_head)(4, 'EnumRanges', ((1, 'ec'),(1, 'ppEnum'),(1, 'pTargetRange'),)))
    ITfReadOnlyProperty.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.System.Com.VARIANT_head))(5, 'GetValue', ((1, 'ec'),(1, 'pRange'),(1, 'pvarValue'),)))
    ITfReadOnlyProperty.GetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfContext_head))(6, 'GetContext', ((1, 'ppContext'),)))
    win32more.System.Com.IUnknown
    return ITfReadOnlyProperty
def _define_ITfReverseConversion_head():
    class ITfReverseConversion(win32more.System.Com.IUnknown_head):
        Guid = Guid('a415e162-157d-417d-8a-8c-0a-b2-6c-7d-27-81')
    return ITfReverseConversion
def _define_ITfReverseConversion():
    ITfReverseConversion = win32more.UI.TextServices.ITfReverseConversion_head
    ITfReverseConversion.DoReverseConversion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.TextServices.ITfReverseConversionList_head))(3, 'DoReverseConversion', ((1, 'lpstr'),(1, 'ppList'),)))
    win32more.System.Com.IUnknown
    return ITfReverseConversion
def _define_ITfReverseConversionList_head():
    class ITfReverseConversionList(win32more.System.Com.IUnknown_head):
        Guid = Guid('151d69f0-86f4-4674-b7-21-56-91-1e-79-7f-47')
    return ITfReverseConversionList
def _define_ITfReverseConversionList():
    ITfReverseConversionList = win32more.UI.TextServices.ITfReverseConversionList_head
    ITfReverseConversionList.GetLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetLength', ((1, 'puIndex'),)))
    ITfReverseConversionList.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR))(4, 'GetString', ((1, 'uIndex'),(1, 'pbstr'),)))
    win32more.System.Com.IUnknown
    return ITfReverseConversionList
def _define_ITfReverseConversionMgr_head():
    class ITfReverseConversionMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('b643c236-c493-41b6-ab-b3-69-24-12-77-5c-c4')
    return ITfReverseConversionMgr
def _define_ITfReverseConversionMgr():
    ITfReverseConversionMgr = win32more.UI.TextServices.ITfReverseConversionMgr_head
    ITfReverseConversionMgr.GetReverseConversion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Guid),UInt32,POINTER(win32more.UI.TextServices.ITfReverseConversion_head))(3, 'GetReverseConversion', ((1, 'langid'),(1, 'guidProfile'),(1, 'dwflag'),(1, 'ppReverseConversion'),)))
    win32more.System.Com.IUnknown
    return ITfReverseConversionMgr
def _define_ITfSource_head():
    class ITfSource(win32more.System.Com.IUnknown_head):
        Guid = Guid('4ea48a35-60ae-446f-8f-d6-e6-a8-d8-24-59-f7')
    return ITfSource
def _define_ITfSource():
    ITfSource = win32more.UI.TextServices.ITfSource_head
    ITfSource.AdviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(UInt32))(3, 'AdviseSink', ((1, 'riid'),(1, 'punk'),(1, 'pdwCookie'),)))
    ITfSource.UnadviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'UnadviseSink', ((1, 'dwCookie'),)))
    win32more.System.Com.IUnknown
    return ITfSource
def _define_ITfSourceSingle_head():
    class ITfSourceSingle(win32more.System.Com.IUnknown_head):
        Guid = Guid('73131f9c-56a9-49dd-b0-ee-d0-46-63-3f-75-28')
    return ITfSourceSingle
def _define_ITfSourceSingle():
    ITfSourceSingle = win32more.UI.TextServices.ITfSourceSingle_head
    ITfSourceSingle.AdviseSingleSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),win32more.System.Com.IUnknown_head)(3, 'AdviseSingleSink', ((1, 'tid'),(1, 'riid'),(1, 'punk'),)))
    ITfSourceSingle.UnadviseSingleSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid))(4, 'UnadviseSingleSink', ((1, 'tid'),(1, 'riid'),)))
    win32more.System.Com.IUnknown
    return ITfSourceSingle
def _define_ITfSpeechUIServer_head():
    class ITfSpeechUIServer(win32more.System.Com.IUnknown_head):
        Guid = Guid('90e9a944-9244-489f-a7-8f-de-67-af-c0-13-a7')
    return ITfSpeechUIServer
def _define_ITfSpeechUIServer():
    ITfSpeechUIServer = win32more.UI.TextServices.ITfSpeechUIServer_head
    ITfSpeechUIServer.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Initialize', ()))
    ITfSpeechUIServer.ShowUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(4, 'ShowUI', ((1, 'fShow'),)))
    ITfSpeechUIServer.UpdateBalloon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfLBBalloonStyle,win32more.Foundation.PWSTR,UInt32)(5, 'UpdateBalloon', ((1, 'style'),(1, 'pch'),(1, 'cch'),)))
    win32more.System.Com.IUnknown
    return ITfSpeechUIServer
def _define_ITfStatusSink_head():
    class ITfStatusSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('6b7d8d73-b267-4f69-b3-2e-1c-a3-21-ce-4f-45')
    return ITfStatusSink
def _define_ITfStatusSink():
    ITfStatusSink = win32more.UI.TextServices.ITfStatusSink_head
    ITfStatusSink.OnStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,UInt32)(3, 'OnStatusChange', ((1, 'pic'),(1, 'dwFlags'),)))
    win32more.System.Com.IUnknown
    return ITfStatusSink
def _define_ITfSystemDeviceTypeLangBarItem_head():
    class ITfSystemDeviceTypeLangBarItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('45672eb9-9059-46a2-83-8d-45-30-35-5f-6a-77')
    return ITfSystemDeviceTypeLangBarItem
def _define_ITfSystemDeviceTypeLangBarItem():
    ITfSystemDeviceTypeLangBarItem = win32more.UI.TextServices.ITfSystemDeviceTypeLangBarItem_head
    ITfSystemDeviceTypeLangBarItem.SetIconMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.LANG_BAR_ITEM_ICON_MODE_FLAGS)(3, 'SetIconMode', ((1, 'dwFlags'),)))
    ITfSystemDeviceTypeLangBarItem.GetIconMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetIconMode', ((1, 'pdwFlags'),)))
    win32more.System.Com.IUnknown
    return ITfSystemDeviceTypeLangBarItem
def _define_ITfSystemLangBarItem_head():
    class ITfSystemLangBarItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('1e13e9ec-6b33-4d4a-b5-eb-8a-92-f0-29-f3-56')
    return ITfSystemLangBarItem
def _define_ITfSystemLangBarItem():
    ITfSystemLangBarItem = win32more.UI.TextServices.ITfSystemLangBarItem_head
    ITfSystemLangBarItem.SetIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HICON)(3, 'SetIcon', ((1, 'hIcon'),)))
    ITfSystemLangBarItem.SetTooltipString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(4, 'SetTooltipString', ((1, 'pchToolTip'),(1, 'cch'),)))
    win32more.System.Com.IUnknown
    return ITfSystemLangBarItem
def _define_ITfSystemLangBarItemSink_head():
    class ITfSystemLangBarItemSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('1449d9ab-13cf-4687-aa-3e-8d-8b-18-57-43-96')
    return ITfSystemLangBarItemSink
def _define_ITfSystemLangBarItemSink():
    ITfSystemLangBarItemSink = win32more.UI.TextServices.ITfSystemLangBarItemSink_head
    ITfSystemLangBarItemSink.InitMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfMenu_head)(3, 'InitMenu', ((1, 'pMenu'),)))
    ITfSystemLangBarItemSink.OnMenuSelect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'OnMenuSelect', ((1, 'wID'),)))
    win32more.System.Com.IUnknown
    return ITfSystemLangBarItemSink
def _define_ITfSystemLangBarItemText_head():
    class ITfSystemLangBarItemText(win32more.System.Com.IUnknown_head):
        Guid = Guid('5c4ce0e5-ba49-4b52-ac-6b-3b-39-7b-4f-70-1f')
    return ITfSystemLangBarItemText
def _define_ITfSystemLangBarItemText():
    ITfSystemLangBarItemText = win32more.UI.TextServices.ITfSystemLangBarItemText_head
    ITfSystemLangBarItemText.SetItemText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(3, 'SetItemText', ((1, 'pch'),(1, 'cch'),)))
    ITfSystemLangBarItemText.GetItemText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'GetItemText', ((1, 'pbstrText'),)))
    win32more.System.Com.IUnknown
    return ITfSystemLangBarItemText
def _define_ITfTextEditSink_head():
    class ITfTextEditSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('8127d409-ccd3-4683-96-7a-b4-3d-5b-48-2b-f7')
    return ITfTextEditSink
def _define_ITfTextEditSink():
    ITfTextEditSink = win32more.UI.TextServices.ITfTextEditSink_head
    ITfTextEditSink.OnEndEdit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,UInt32,win32more.UI.TextServices.ITfEditRecord_head)(3, 'OnEndEdit', ((1, 'pic'),(1, 'ecReadOnly'),(1, 'pEditRecord'),)))
    win32more.System.Com.IUnknown
    return ITfTextEditSink
def _define_ITfTextInputProcessor_head():
    class ITfTextInputProcessor(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e7f7-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    return ITfTextInputProcessor
def _define_ITfTextInputProcessor():
    ITfTextInputProcessor = win32more.UI.TextServices.ITfTextInputProcessor_head
    ITfTextInputProcessor.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfThreadMgr_head,UInt32)(3, 'Activate', ((1, 'ptim'),(1, 'tid'),)))
    ITfTextInputProcessor.Deactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Deactivate', ()))
    win32more.System.Com.IUnknown
    return ITfTextInputProcessor
def _define_ITfTextInputProcessorEx_head():
    class ITfTextInputProcessorEx(win32more.UI.TextServices.ITfTextInputProcessor_head):
        Guid = Guid('6e4e2102-f9cd-433d-b4-96-30-3c-e0-3a-65-07')
    return ITfTextInputProcessorEx
def _define_ITfTextInputProcessorEx():
    ITfTextInputProcessorEx = win32more.UI.TextServices.ITfTextInputProcessorEx_head
    ITfTextInputProcessorEx.ActivateEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfThreadMgr_head,UInt32,UInt32)(5, 'ActivateEx', ((1, 'ptim'),(1, 'tid'),(1, 'dwFlags'),)))
    win32more.UI.TextServices.ITfTextInputProcessor
    return ITfTextInputProcessorEx
def _define_ITfTextLayoutSink_head():
    class ITfTextLayoutSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('2af2d06a-dd5b-4927-a0-b4-54-f1-9c-91-fa-de')
    return ITfTextLayoutSink
def _define_ITfTextLayoutSink():
    ITfTextLayoutSink = win32more.UI.TextServices.ITfTextLayoutSink_head
    ITfTextLayoutSink.OnLayoutChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,win32more.UI.TextServices.TfLayoutCode,win32more.UI.TextServices.ITfContextView_head)(3, 'OnLayoutChange', ((1, 'pic'),(1, 'lcode'),(1, 'pView'),)))
    win32more.System.Com.IUnknown
    return ITfTextLayoutSink
def _define_ITfThreadFocusSink_head():
    class ITfThreadFocusSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0f1db0c-3a20-405c-a3-03-96-b6-01-0a-88-5f')
    return ITfThreadFocusSink
def _define_ITfThreadFocusSink():
    ITfThreadFocusSink = win32more.UI.TextServices.ITfThreadFocusSink_head
    ITfThreadFocusSink.OnSetThreadFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'OnSetThreadFocus', ()))
    ITfThreadFocusSink.OnKillThreadFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'OnKillThreadFocus', ()))
    win32more.System.Com.IUnknown
    return ITfThreadFocusSink
def _define_ITfThreadMgr_head():
    class ITfThreadMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e801-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    return ITfThreadMgr
def _define_ITfThreadMgr():
    ITfThreadMgr = win32more.UI.TextServices.ITfThreadMgr_head
    ITfThreadMgr.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'Activate', ((1, 'ptid'),)))
    ITfThreadMgr.Deactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Deactivate', ()))
    ITfThreadMgr.CreateDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head))(5, 'CreateDocumentMgr', ((1, 'ppdim'),)))
    ITfThreadMgr.EnumDocumentMgrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfDocumentMgrs_head))(6, 'EnumDocumentMgrs', ((1, 'ppEnum'),)))
    ITfThreadMgr.GetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head))(7, 'GetFocus', ((1, 'ppdimFocus'),)))
    ITfThreadMgr.SetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfDocumentMgr_head)(8, 'SetFocus', ((1, 'pdimFocus'),)))
    ITfThreadMgr.AssociateFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.UI.TextServices.ITfDocumentMgr_head,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head))(9, 'AssociateFocus', ((1, 'hwnd'),(1, 'pdimNew'),(1, 'ppdimPrev'),)))
    ITfThreadMgr.IsThreadFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(10, 'IsThreadFocus', ((1, 'pfThreadFocus'),)))
    ITfThreadMgr.GetFunctionProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfFunctionProvider_head))(11, 'GetFunctionProvider', ((1, 'clsid'),(1, 'ppFuncProv'),)))
    ITfThreadMgr.EnumFunctionProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfFunctionProviders_head))(12, 'EnumFunctionProviders', ((1, 'ppEnum'),)))
    ITfThreadMgr.GetGlobalCompartment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfCompartmentMgr_head))(13, 'GetGlobalCompartment', ((1, 'ppCompMgr'),)))
    win32more.System.Com.IUnknown
    return ITfThreadMgr
def _define_ITfThreadMgr2_head():
    class ITfThreadMgr2(win32more.System.Com.IUnknown_head):
        Guid = Guid('0ab198ef-6477-4ee8-88-12-67-80-ed-b8-2d-5e')
    return ITfThreadMgr2
def _define_ITfThreadMgr2():
    ITfThreadMgr2 = win32more.UI.TextServices.ITfThreadMgr2_head
    ITfThreadMgr2.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'Activate', ((1, 'ptid'),)))
    ITfThreadMgr2.Deactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Deactivate', ()))
    ITfThreadMgr2.CreateDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head))(5, 'CreateDocumentMgr', ((1, 'ppdim'),)))
    ITfThreadMgr2.EnumDocumentMgrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfDocumentMgrs_head))(6, 'EnumDocumentMgrs', ((1, 'ppEnum'),)))
    ITfThreadMgr2.GetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head))(7, 'GetFocus', ((1, 'ppdimFocus'),)))
    ITfThreadMgr2.SetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfDocumentMgr_head)(8, 'SetFocus', ((1, 'pdimFocus'),)))
    ITfThreadMgr2.IsThreadFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(9, 'IsThreadFocus', ((1, 'pfThreadFocus'),)))
    ITfThreadMgr2.GetFunctionProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfFunctionProvider_head))(10, 'GetFunctionProvider', ((1, 'clsid'),(1, 'ppFuncProv'),)))
    ITfThreadMgr2.EnumFunctionProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfFunctionProviders_head))(11, 'EnumFunctionProviders', ((1, 'ppEnum'),)))
    ITfThreadMgr2.GetGlobalCompartment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfCompartmentMgr_head))(12, 'GetGlobalCompartment', ((1, 'ppCompMgr'),)))
    ITfThreadMgr2.ActivateEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32)(13, 'ActivateEx', ((1, 'ptid'),(1, 'dwFlags'),)))
    ITfThreadMgr2.GetActiveFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(14, 'GetActiveFlags', ((1, 'lpdwFlags'),)))
    ITfThreadMgr2.SuspendKeystrokeHandling = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'SuspendKeystrokeHandling', ()))
    ITfThreadMgr2.ResumeKeystrokeHandling = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'ResumeKeystrokeHandling', ()))
    win32more.System.Com.IUnknown
    return ITfThreadMgr2
def _define_ITfThreadMgrEventSink_head():
    class ITfThreadMgrEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e80e-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    return ITfThreadMgrEventSink
def _define_ITfThreadMgrEventSink():
    ITfThreadMgrEventSink = win32more.UI.TextServices.ITfThreadMgrEventSink_head
    ITfThreadMgrEventSink.OnInitDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfDocumentMgr_head)(3, 'OnInitDocumentMgr', ((1, 'pdim'),)))
    ITfThreadMgrEventSink.OnUninitDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfDocumentMgr_head)(4, 'OnUninitDocumentMgr', ((1, 'pdim'),)))
    ITfThreadMgrEventSink.OnSetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfDocumentMgr_head,win32more.UI.TextServices.ITfDocumentMgr_head)(5, 'OnSetFocus', ((1, 'pdimFocus'),(1, 'pdimPrevFocus'),)))
    ITfThreadMgrEventSink.OnPushContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head)(6, 'OnPushContext', ((1, 'pic'),)))
    ITfThreadMgrEventSink.OnPopContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head)(7, 'OnPopContext', ((1, 'pic'),)))
    win32more.System.Com.IUnknown
    return ITfThreadMgrEventSink
def _define_ITfThreadMgrEx_head():
    class ITfThreadMgrEx(win32more.UI.TextServices.ITfThreadMgr_head):
        Guid = Guid('3e90ade3-7594-4cb0-bb-58-69-62-8f-5f-45-8c')
    return ITfThreadMgrEx
def _define_ITfThreadMgrEx():
    ITfThreadMgrEx = win32more.UI.TextServices.ITfThreadMgrEx_head
    ITfThreadMgrEx.ActivateEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32)(14, 'ActivateEx', ((1, 'ptid'),(1, 'dwFlags'),)))
    ITfThreadMgrEx.GetActiveFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(15, 'GetActiveFlags', ((1, 'lpdwFlags'),)))
    win32more.UI.TextServices.ITfThreadMgr
    return ITfThreadMgrEx
def _define_ITfToolTipUIElement_head():
    class ITfToolTipUIElement(win32more.UI.TextServices.ITfUIElement_head):
        Guid = Guid('52b18b5c-555d-46b2-b0-0a-fa-68-01-44-fb-db')
    return ITfToolTipUIElement
def _define_ITfToolTipUIElement():
    ITfToolTipUIElement = win32more.UI.TextServices.ITfToolTipUIElement_head
    ITfToolTipUIElement.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'GetString', ((1, 'pstr'),)))
    win32more.UI.TextServices.ITfUIElement
    return ITfToolTipUIElement
def _define_ITfTransitoryExtensionSink_head():
    class ITfTransitoryExtensionSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('a615096f-1c57-4813-8a-15-55-ee-6e-5a-83-9c')
    return ITfTransitoryExtensionSink
def _define_ITfTransitoryExtensionSink():
    ITfTransitoryExtensionSink = win32more.UI.TextServices.ITfTransitoryExtensionSink_head
    ITfTransitoryExtensionSink.OnTransitoryExtensionUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.Foundation.BOOL))(3, 'OnTransitoryExtensionUpdated', ((1, 'pic'),(1, 'ecReadOnly'),(1, 'pResultRange'),(1, 'pCompositionRange'),(1, 'pfDeleteResultRange'),)))
    win32more.System.Com.IUnknown
    return ITfTransitoryExtensionSink
def _define_ITfTransitoryExtensionUIElement_head():
    class ITfTransitoryExtensionUIElement(win32more.UI.TextServices.ITfUIElement_head):
        Guid = Guid('858f956a-972f-42a2-a2-f2-03-21-e1-ab-e2-09')
    return ITfTransitoryExtensionUIElement
def _define_ITfTransitoryExtensionUIElement():
    ITfTransitoryExtensionUIElement = win32more.UI.TextServices.ITfTransitoryExtensionUIElement_head
    ITfTransitoryExtensionUIElement.GetDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head))(7, 'GetDocumentMgr', ((1, 'ppdim'),)))
    win32more.UI.TextServices.ITfUIElement
    return ITfTransitoryExtensionUIElement
def _define_ITfUIElement_head():
    class ITfUIElement(win32more.System.Com.IUnknown_head):
        Guid = Guid('ea1ea137-19df-11d7-a6-d2-00-06-5b-84-43-5c')
    return ITfUIElement
def _define_ITfUIElement():
    ITfUIElement = win32more.UI.TextServices.ITfUIElement_head
    ITfUIElement.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(3, 'GetDescription', ((1, 'pbstrDescription'),)))
    ITfUIElement.GetGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(4, 'GetGUID', ((1, 'pguid'),)))
    ITfUIElement.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(5, 'Show', ((1, 'bShow'),)))
    ITfUIElement.IsShown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(6, 'IsShown', ((1, 'pbShow'),)))
    win32more.System.Com.IUnknown
    return ITfUIElement
def _define_ITfUIElementMgr_head():
    class ITfUIElementMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('ea1ea135-19df-11d7-a6-d2-00-06-5b-84-43-5c')
    return ITfUIElementMgr
def _define_ITfUIElementMgr():
    ITfUIElementMgr = win32more.UI.TextServices.ITfUIElementMgr_head
    ITfUIElementMgr.BeginUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfUIElement_head,POINTER(win32more.Foundation.BOOL),POINTER(UInt32))(3, 'BeginUIElement', ((1, 'pElement'),(1, 'pbShow'),(1, 'pdwUIElementId'),)))
    ITfUIElementMgr.UpdateUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'UpdateUIElement', ((1, 'dwUIElementId'),)))
    ITfUIElementMgr.EndUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'EndUIElement', ((1, 'dwUIElementId'),)))
    ITfUIElementMgr.GetUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfUIElement_head))(6, 'GetUIElement', ((1, 'dwUIELementId'),(1, 'ppElement'),)))
    ITfUIElementMgr.EnumUIElements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfUIElements_head))(7, 'EnumUIElements', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return ITfUIElementMgr
def _define_ITfUIElementSink_head():
    class ITfUIElementSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('ea1ea136-19df-11d7-a6-d2-00-06-5b-84-43-5c')
    return ITfUIElementSink
def _define_ITfUIElementSink():
    ITfUIElementSink = win32more.UI.TextServices.ITfUIElementSink_head
    ITfUIElementSink.BeginUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL))(3, 'BeginUIElement', ((1, 'dwUIElementId'),(1, 'pbShow'),)))
    ITfUIElementSink.UpdateUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'UpdateUIElement', ((1, 'dwUIElementId'),)))
    ITfUIElementSink.EndUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'EndUIElement', ((1, 'dwUIElementId'),)))
    win32more.System.Com.IUnknown
    return ITfUIElementSink
def _define_IUIManagerEventSink_head():
    class IUIManagerEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('cd91d690-a7e8-4265-9b-38-8b-b3-bb-ab-a7-de')
    return IUIManagerEventSink
def _define_IUIManagerEventSink():
    IUIManagerEventSink = win32more.UI.TextServices.IUIManagerEventSink_head
    IUIManagerEventSink.OnWindowOpening = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(3, 'OnWindowOpening', ((1, 'prcBounds'),)))
    IUIManagerEventSink.OnWindowOpened = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(4, 'OnWindowOpened', ((1, 'prcBounds'),)))
    IUIManagerEventSink.OnWindowUpdating = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(5, 'OnWindowUpdating', ((1, 'prcUpdatedBounds'),)))
    IUIManagerEventSink.OnWindowUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(6, 'OnWindowUpdated', ((1, 'prcUpdatedBounds'),)))
    IUIManagerEventSink.OnWindowClosing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'OnWindowClosing', ()))
    IUIManagerEventSink.OnWindowClosed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'OnWindowClosed', ()))
    win32more.System.Com.IUnknown
    return IUIManagerEventSink
def _define_IVersionInfo_head():
    class IVersionInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('401518ec-db00-4611-9b-29-2a-0e-4b-9a-fa-85')
    return IVersionInfo
def _define_IVersionInfo():
    IVersionInfo = win32more.UI.TextServices.IVersionInfo_head
    IVersionInfo.GetSubcomponentCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(3, 'GetSubcomponentCount', ((1, 'ulSub'),(1, 'ulCount'),)))
    IVersionInfo.GetImplementationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid))(4, 'GetImplementationID', ((1, 'ulSub'),(1, 'implid'),)))
    IVersionInfo.GetBuildVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(UInt32))(5, 'GetBuildVersion', ((1, 'ulSub'),(1, 'pdwMajor'),(1, 'pdwMinor'),)))
    IVersionInfo.GetComponentDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR))(6, 'GetComponentDescription', ((1, 'ulSub'),(1, 'pImplStr'),)))
    IVersionInfo.GetInstanceDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR))(7, 'GetInstanceDescription', ((1, 'ulSub'),(1, 'pImplStr'),)))
    win32more.System.Com.IUnknown
    return IVersionInfo
LANG_BAR_ITEM_ICON_MODE_FLAGS = UInt32
TF_DTLBI_NONE = 0
TF_DTLBI_USEPROFILEICON = 1
MSAAControl = Guid('08cd963f-7a3e-4f5c-9b-d8-d6-92-bb-04-3c-5b')
TEXT_STORE_CHANGE_FLAGS = UInt32
TS_TC_NONE = 0
TS_TC_CORRECTION = 1
TEXT_STORE_LOCK_FLAGS = UInt32
TS_LF_READ = 2
TS_LF_READWRITE = 6
TEXT_STORE_TEXT_CHANGE_FLAGS = UInt32
TS_ST_NONE = 0
TS_ST_CORRECTION = 1
TF_CONTEXT_EDIT_CONTEXT_FLAGS = UInt32
TF_ES_ASYNCDONTCARE = 0
TF_ES_SYNC = 1
TF_ES_READ = 2
TF_ES_READWRITE = 6
TF_ES_ASYNC = 8
TF_DA_ATTR_INFO = Int32
TF_ATTR_INPUT = 0
TF_ATTR_TARGET_CONVERTED = 1
TF_ATTR_CONVERTED = 2
TF_ATTR_TARGET_NOTCONVERTED = 3
TF_ATTR_INPUT_ERROR = 4
TF_ATTR_FIXEDCONVERTED = 5
TF_ATTR_OTHER = -1
def _define_TF_DA_COLOR_head():
    class TF_DA_COLOR(Structure):
        pass
    return TF_DA_COLOR
def _define_TF_DA_COLOR():
    TF_DA_COLOR = win32more.UI.TextServices.TF_DA_COLOR_head
    class TF_DA_COLOR__Anonymous_e__Union(Union):
        pass
    TF_DA_COLOR__Anonymous_e__Union._fields_ = [
        ('nIndex', Int32),
        ('cr', win32more.Foundation.COLORREF),
    ]
    TF_DA_COLOR._anonymous_ = [
        'Anonymous',
    ]
    TF_DA_COLOR._fields_ = [
        ('type', win32more.UI.TextServices.TF_DA_COLORTYPE),
        ('Anonymous', TF_DA_COLOR__Anonymous_e__Union),
    ]
    return TF_DA_COLOR
TF_DA_COLORTYPE = Int32
TF_CT_NONE = 0
TF_CT_SYSCOLOR = 1
TF_CT_COLORREF = 2
TF_DA_LINESTYLE = Int32
TF_LS_NONE = 0
TF_LS_SOLID = 1
TF_LS_DOT = 2
TF_LS_DASH = 3
TF_LS_SQUIGGLE = 4
def _define_TF_DISPLAYATTRIBUTE_head():
    class TF_DISPLAYATTRIBUTE(Structure):
        pass
    return TF_DISPLAYATTRIBUTE
def _define_TF_DISPLAYATTRIBUTE():
    TF_DISPLAYATTRIBUTE = win32more.UI.TextServices.TF_DISPLAYATTRIBUTE_head
    TF_DISPLAYATTRIBUTE._fields_ = [
        ('crText', win32more.UI.TextServices.TF_DA_COLOR),
        ('crBk', win32more.UI.TextServices.TF_DA_COLOR),
        ('lsStyle', win32more.UI.TextServices.TF_DA_LINESTYLE),
        ('fBoldLine', win32more.Foundation.BOOL),
        ('crLine', win32more.UI.TextServices.TF_DA_COLOR),
        ('bAttr', win32more.UI.TextServices.TF_DA_ATTR_INFO),
    ]
    return TF_DISPLAYATTRIBUTE
def _define_TF_HALTCOND_head():
    class TF_HALTCOND(Structure):
        pass
    return TF_HALTCOND
def _define_TF_HALTCOND():
    TF_HALTCOND = win32more.UI.TextServices.TF_HALTCOND_head
    TF_HALTCOND._fields_ = [
        ('pHaltRange', win32more.UI.TextServices.ITfRange_head),
        ('aHaltPos', win32more.UI.TextServices.TfAnchor),
        ('dwFlags', UInt32),
    ]
    return TF_HALTCOND
def _define_TF_INPUTPROCESSORPROFILE_head():
    class TF_INPUTPROCESSORPROFILE(Structure):
        pass
    return TF_INPUTPROCESSORPROFILE
def _define_TF_INPUTPROCESSORPROFILE():
    TF_INPUTPROCESSORPROFILE = win32more.UI.TextServices.TF_INPUTPROCESSORPROFILE_head
    TF_INPUTPROCESSORPROFILE._fields_ = [
        ('dwProfileType', UInt32),
        ('langid', UInt16),
        ('clsid', Guid),
        ('guidProfile', Guid),
        ('catid', Guid),
        ('hklSubstitute', win32more.UI.TextServices.HKL),
        ('dwCaps', UInt32),
        ('hkl', win32more.UI.TextServices.HKL),
        ('dwFlags', UInt32),
    ]
    return TF_INPUTPROCESSORPROFILE
def _define_TF_LANGBARITEMINFO_head():
    class TF_LANGBARITEMINFO(Structure):
        pass
    return TF_LANGBARITEMINFO
def _define_TF_LANGBARITEMINFO():
    TF_LANGBARITEMINFO = win32more.UI.TextServices.TF_LANGBARITEMINFO_head
    TF_LANGBARITEMINFO._fields_ = [
        ('clsidService', Guid),
        ('guidItem', Guid),
        ('dwStyle', UInt32),
        ('ulSort', UInt32),
        ('szDescription', Char * 32),
    ]
    return TF_LANGBARITEMINFO
def _define_TF_LANGUAGEPROFILE_head():
    class TF_LANGUAGEPROFILE(Structure):
        pass
    return TF_LANGUAGEPROFILE
def _define_TF_LANGUAGEPROFILE():
    TF_LANGUAGEPROFILE = win32more.UI.TextServices.TF_LANGUAGEPROFILE_head
    TF_LANGUAGEPROFILE._fields_ = [
        ('clsid', Guid),
        ('langid', UInt16),
        ('catid', Guid),
        ('fActive', win32more.Foundation.BOOL),
        ('guidProfile', Guid),
    ]
    return TF_LANGUAGEPROFILE
def _define_TF_LBBALLOONINFO_head():
    class TF_LBBALLOONINFO(Structure):
        pass
    return TF_LBBALLOONINFO
def _define_TF_LBBALLOONINFO():
    TF_LBBALLOONINFO = win32more.UI.TextServices.TF_LBBALLOONINFO_head
    TF_LBBALLOONINFO._fields_ = [
        ('style', win32more.UI.TextServices.TfLBBalloonStyle),
        ('bstrText', win32more.Foundation.BSTR),
    ]
    return TF_LBBALLOONINFO
def _define_TF_LMLATTELEMENT_head():
    class TF_LMLATTELEMENT(Structure):
        pass
    return TF_LMLATTELEMENT
def _define_TF_LMLATTELEMENT():
    TF_LMLATTELEMENT = win32more.UI.TextServices.TF_LMLATTELEMENT_head
    class TF_LMLATTELEMENT__Anonymous_e__Union(Union):
        pass
    TF_LMLATTELEMENT__Anonymous_e__Union._fields_ = [
        ('iCost', Int32),
    ]
    TF_LMLATTELEMENT._anonymous_ = [
        'Anonymous',
    ]
    TF_LMLATTELEMENT._fields_ = [
        ('dwFrameStart', UInt32),
        ('dwFrameLen', UInt32),
        ('dwFlags', UInt32),
        ('Anonymous', TF_LMLATTELEMENT__Anonymous_e__Union),
        ('bstrText', win32more.Foundation.BSTR),
    ]
    return TF_LMLATTELEMENT
def _define_TF_PERSISTENT_PROPERTY_HEADER_ACP_head():
    class TF_PERSISTENT_PROPERTY_HEADER_ACP(Structure):
        pass
    return TF_PERSISTENT_PROPERTY_HEADER_ACP
def _define_TF_PERSISTENT_PROPERTY_HEADER_ACP():
    TF_PERSISTENT_PROPERTY_HEADER_ACP = win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head
    TF_PERSISTENT_PROPERTY_HEADER_ACP._fields_ = [
        ('guidType', Guid),
        ('ichStart', Int32),
        ('cch', Int32),
        ('cb', UInt32),
        ('dwPrivate', UInt32),
        ('clsidTIP', Guid),
    ]
    return TF_PERSISTENT_PROPERTY_HEADER_ACP
def _define_TF_PRESERVEDKEY_head():
    class TF_PRESERVEDKEY(Structure):
        pass
    return TF_PRESERVEDKEY
def _define_TF_PRESERVEDKEY():
    TF_PRESERVEDKEY = win32more.UI.TextServices.TF_PRESERVEDKEY_head
    TF_PRESERVEDKEY._fields_ = [
        ('uVKey', UInt32),
        ('uModifiers', UInt32),
    ]
    return TF_PRESERVEDKEY
def _define_TF_PROPERTYVAL_head():
    class TF_PROPERTYVAL(Structure):
        pass
    return TF_PROPERTYVAL
def _define_TF_PROPERTYVAL():
    TF_PROPERTYVAL = win32more.UI.TextServices.TF_PROPERTYVAL_head
    TF_PROPERTYVAL._fields_ = [
        ('guidId', Guid),
        ('varValue', win32more.System.Com.VARIANT),
    ]
    return TF_PROPERTYVAL
def _define_TF_SELECTION_head():
    class TF_SELECTION(Structure):
        pass
    return TF_SELECTION
def _define_TF_SELECTION():
    TF_SELECTION = win32more.UI.TextServices.TF_SELECTION_head
    TF_SELECTION._fields_ = [
        ('range', win32more.UI.TextServices.ITfRange_head),
        ('style', win32more.UI.TextServices.TF_SELECTIONSTYLE),
    ]
    return TF_SELECTION
def _define_TF_SELECTIONSTYLE_head():
    class TF_SELECTIONSTYLE(Structure):
        pass
    return TF_SELECTIONSTYLE
def _define_TF_SELECTIONSTYLE():
    TF_SELECTIONSTYLE = win32more.UI.TextServices.TF_SELECTIONSTYLE_head
    TF_SELECTIONSTYLE._fields_ = [
        ('ase', win32more.UI.TextServices.TfActiveSelEnd),
        ('fInterimChar', win32more.Foundation.BOOL),
    ]
    return TF_SELECTIONSTYLE
TfActiveSelEnd = Int32
TF_AE_NONE = 0
TF_AE_START = 1
TF_AE_END = 2
TfAnchor = Int32
TF_ANCHOR_START = 0
TF_ANCHOR_END = 1
TfCandidateResult = Int32
CAND_FINALIZED = 0
CAND_SELECTED = 1
CAND_CANCELED = 2
TfGravity = Int32
TF_GRAVITY_BACKWARD = 0
TF_GRAVITY_FORWARD = 1
TfIntegratableCandidateListSelectionStyle = Int32
STYLE_ACTIVE_SELECTION = 0
STYLE_IMPLIED_SELECTION = 1
TfLayoutCode = Int32
TF_LC_CREATE = 0
TF_LC_CHANGE = 1
TF_LC_DESTROY = 2
TfLBBalloonStyle = Int32
TF_LB_BALLOON_RECO = 0
TF_LB_BALLOON_SHOW = 1
TF_LB_BALLOON_MISS = 2
TfLBIClick = Int32
TF_LBI_CLK_RIGHT = 1
TF_LBI_CLK_LEFT = 2
TfSapiObject = Int32
GETIF_RESMGR = 0
GETIF_RECOCONTEXT = 1
GETIF_RECOGNIZER = 2
GETIF_VOICE = 3
GETIF_DICTGRAM = 4
GETIF_RECOGNIZERNOINIT = 5
TfShiftDir = Int32
TF_SD_BACKWARD = 0
TF_SD_FORWARD = 1
TKBLayoutType = Int32
TKBLT_UNDEFINED = 0
TKBLT_CLASSIC = 1
TKBLT_OPTIMIZED = 2
def _define_TS_ATTRVAL_head():
    class TS_ATTRVAL(Structure):
        pass
    return TS_ATTRVAL
def _define_TS_ATTRVAL():
    TS_ATTRVAL = win32more.UI.TextServices.TS_ATTRVAL_head
    TS_ATTRVAL._fields_ = [
        ('idAttr', Guid),
        ('dwOverlapId', UInt32),
        ('varValue', win32more.System.Com.VARIANT),
    ]
    return TS_ATTRVAL
def _define_TS_RUNINFO_head():
    class TS_RUNINFO(Structure):
        pass
    return TS_RUNINFO
def _define_TS_RUNINFO():
    TS_RUNINFO = win32more.UI.TextServices.TS_RUNINFO_head
    TS_RUNINFO._fields_ = [
        ('uCount', UInt32),
        ('type', win32more.UI.TextServices.TsRunType),
    ]
    return TS_RUNINFO
def _define_TS_SELECTION_ACP_head():
    class TS_SELECTION_ACP(Structure):
        pass
    return TS_SELECTION_ACP
def _define_TS_SELECTION_ACP():
    TS_SELECTION_ACP = win32more.UI.TextServices.TS_SELECTION_ACP_head
    TS_SELECTION_ACP._fields_ = [
        ('acpStart', Int32),
        ('acpEnd', Int32),
        ('style', win32more.UI.TextServices.TS_SELECTIONSTYLE),
    ]
    return TS_SELECTION_ACP
def _define_TS_SELECTION_ANCHOR_head():
    class TS_SELECTION_ANCHOR(Structure):
        pass
    return TS_SELECTION_ANCHOR
def _define_TS_SELECTION_ANCHOR():
    TS_SELECTION_ANCHOR = win32more.UI.TextServices.TS_SELECTION_ANCHOR_head
    TS_SELECTION_ANCHOR._fields_ = [
        ('paStart', win32more.UI.TextServices.IAnchor_head),
        ('paEnd', win32more.UI.TextServices.IAnchor_head),
        ('style', win32more.UI.TextServices.TS_SELECTIONSTYLE),
    ]
    return TS_SELECTION_ANCHOR
def _define_TS_SELECTIONSTYLE_head():
    class TS_SELECTIONSTYLE(Structure):
        pass
    return TS_SELECTIONSTYLE
def _define_TS_SELECTIONSTYLE():
    TS_SELECTIONSTYLE = win32more.UI.TextServices.TS_SELECTIONSTYLE_head
    TS_SELECTIONSTYLE._fields_ = [
        ('ase', win32more.UI.TextServices.TsActiveSelEnd),
        ('fInterimChar', win32more.Foundation.BOOL),
    ]
    return TS_SELECTIONSTYLE
def _define_TS_STATUS_head():
    class TS_STATUS(Structure):
        pass
    return TS_STATUS
def _define_TS_STATUS():
    TS_STATUS = win32more.UI.TextServices.TS_STATUS_head
    TS_STATUS._fields_ = [
        ('dwDynamicFlags', UInt32),
        ('dwStaticFlags', UInt32),
    ]
    return TS_STATUS
def _define_TS_TEXTCHANGE_head():
    class TS_TEXTCHANGE(Structure):
        pass
    return TS_TEXTCHANGE
def _define_TS_TEXTCHANGE():
    TS_TEXTCHANGE = win32more.UI.TextServices.TS_TEXTCHANGE_head
    TS_TEXTCHANGE._fields_ = [
        ('acpStart', Int32),
        ('acpOldEnd', Int32),
        ('acpNewEnd', Int32),
    ]
    return TS_TEXTCHANGE
TsActiveSelEnd = Int32
TS_AE_NONE = 0
TS_AE_START = 1
TS_AE_END = 2
TsGravity = Int32
TS_GR_BACKWARD = 0
TS_GR_FORWARD = 1
TsLayoutCode = Int32
TS_LC_CREATE = 0
TS_LC_CHANGE = 1
TS_LC_DESTROY = 2
TsRunType = Int32
TS_RT_PLAIN = 0
TS_RT_HIDDEN = 1
TS_RT_OPAQUE = 2
TsShiftDir = Int32
TS_SD_BACKWARD = 0
TS_SD_FORWARD = 1
__all__ = [
    "ANCHOR_CHANGE_HISTORY_FLAGS",
    "AccClientDocMgr",
    "AccDictionary",
    "AccServerDocMgr",
    "AccStore",
    "CAND_CANCELED",
    "CAND_FINALIZED",
    "CAND_SELECTED",
    "CLSID_TF_CategoryMgr",
    "CLSID_TF_ClassicLangBar",
    "CLSID_TF_DisplayAttributeMgr",
    "CLSID_TF_InputProcessorProfiles",
    "CLSID_TF_LangBarItemMgr",
    "CLSID_TF_LangBarMgr",
    "CLSID_TF_ThreadMgr",
    "CLSID_TF_TransitoryExtensionUIEntry",
    "CLSID_TsfServices",
    "DCM_FLAGS_CTFMON",
    "DCM_FLAGS_LOCALTHREADTSF",
    "DCM_FLAGS_TASKENG",
    "DoMsCtfMonitor",
    "DocWrap",
    "GETIF_DICTGRAM",
    "GETIF_RECOCONTEXT",
    "GETIF_RECOGNIZER",
    "GETIF_RECOGNIZERNOINIT",
    "GETIF_RESMGR",
    "GETIF_VOICE",
    "GET_TEXT_AND_PROPERTY_UPDATES_FLAGS",
    "GUID_APP_FUNCTIONPROVIDER",
    "GUID_COMPARTMENT_CONVERSIONMODEBIAS",
    "GUID_COMPARTMENT_EMPTYCONTEXT",
    "GUID_COMPARTMENT_ENABLED_PROFILES_UPDATED",
    "GUID_COMPARTMENT_HANDWRITING_OPENCLOSE",
    "GUID_COMPARTMENT_KEYBOARD_DISABLED",
    "GUID_COMPARTMENT_KEYBOARD_INPUTMODE",
    "GUID_COMPARTMENT_KEYBOARD_INPUTMODE_CONVERSION",
    "GUID_COMPARTMENT_KEYBOARD_INPUTMODE_SENTENCE",
    "GUID_COMPARTMENT_KEYBOARD_OPENCLOSE",
    "GUID_COMPARTMENT_SAPI_AUDIO",
    "GUID_COMPARTMENT_SPEECH_CFGMENU",
    "GUID_COMPARTMENT_SPEECH_DISABLED",
    "GUID_COMPARTMENT_SPEECH_GLOBALSTATE",
    "GUID_COMPARTMENT_SPEECH_OPENCLOSE",
    "GUID_COMPARTMENT_SPEECH_UI_STATUS",
    "GUID_COMPARTMENT_TIPUISTATUS",
    "GUID_COMPARTMENT_TRANSITORYEXTENSION",
    "GUID_COMPARTMENT_TRANSITORYEXTENSION_DOCUMENTMANAGER",
    "GUID_COMPARTMENT_TRANSITORYEXTENSION_PARENT",
    "GUID_INTEGRATIONSTYLE_SEARCHBOX",
    "GUID_LBI_INPUTMODE",
    "GUID_LBI_SAPILAYR_CFGMENUBUTTON",
    "GUID_MODEBIAS_CHINESE",
    "GUID_MODEBIAS_CONVERSATION",
    "GUID_MODEBIAS_DATETIME",
    "GUID_MODEBIAS_FILENAME",
    "GUID_MODEBIAS_FULLWIDTHALPHANUMERIC",
    "GUID_MODEBIAS_FULLWIDTHHANGUL",
    "GUID_MODEBIAS_HALFWIDTHKATAKANA",
    "GUID_MODEBIAS_HANGUL",
    "GUID_MODEBIAS_HIRAGANA",
    "GUID_MODEBIAS_KATAKANA",
    "GUID_MODEBIAS_NAME",
    "GUID_MODEBIAS_NONE",
    "GUID_MODEBIAS_NUMERIC",
    "GUID_MODEBIAS_READING",
    "GUID_MODEBIAS_URLHISTORY",
    "GUID_PROP_ATTRIBUTE",
    "GUID_PROP_COMPOSING",
    "GUID_PROP_INPUTSCOPE",
    "GUID_PROP_LANGID",
    "GUID_PROP_MODEBIAS",
    "GUID_PROP_READING",
    "GUID_PROP_TEXTOWNER",
    "GUID_PROP_TKB_ALTERNATES",
    "GUID_SYSTEM_FUNCTIONPROVIDER",
    "GUID_TFCAT_CATEGORY_OF_TIP",
    "GUID_TFCAT_DISPLAYATTRIBUTEPROPERTY",
    "GUID_TFCAT_DISPLAYATTRIBUTEPROVIDER",
    "GUID_TFCAT_PROPSTYLE_STATIC",
    "GUID_TFCAT_PROP_AUDIODATA",
    "GUID_TFCAT_PROP_INKDATA",
    "GUID_TFCAT_TIPCAP_COMLESS",
    "GUID_TFCAT_TIPCAP_DUALMODE",
    "GUID_TFCAT_TIPCAP_IMMERSIVEONLY",
    "GUID_TFCAT_TIPCAP_IMMERSIVESUPPORT",
    "GUID_TFCAT_TIPCAP_INPUTMODECOMPARTMENT",
    "GUID_TFCAT_TIPCAP_LOCALSERVER",
    "GUID_TFCAT_TIPCAP_SECUREMODE",
    "GUID_TFCAT_TIPCAP_SYSTRAYSUPPORT",
    "GUID_TFCAT_TIPCAP_TSF3",
    "GUID_TFCAT_TIPCAP_UIELEMENTENABLED",
    "GUID_TFCAT_TIPCAP_WOW16",
    "GUID_TFCAT_TIP_HANDWRITING",
    "GUID_TFCAT_TIP_KEYBOARD",
    "GUID_TFCAT_TIP_SPEECH",
    "GUID_TFCAT_TRANSITORYEXTENSIONUI",
    "GUID_TS_SERVICE_ACCESSIBLE",
    "GUID_TS_SERVICE_ACTIVEX",
    "GUID_TS_SERVICE_DATAOBJECT",
    "GXFPF_NEAREST",
    "GXFPF_ROUND_NEAREST",
    "HKL",
    "IAccClientDocMgr",
    "IAccDictionary",
    "IAccServerDocMgr",
    "IAccStore",
    "IAnchor",
    "IClonableWrapper",
    "ICoCreateLocally",
    "ICoCreatedLocally",
    "IDocWrap",
    "IEnumITfCompositionView",
    "IEnumSpeechCommands",
    "IEnumTfCandidates",
    "IEnumTfContextViews",
    "IEnumTfContexts",
    "IEnumTfDisplayAttributeInfo",
    "IEnumTfDocumentMgrs",
    "IEnumTfFunctionProviders",
    "IEnumTfInputProcessorProfiles",
    "IEnumTfLangBarItems",
    "IEnumTfLanguageProfiles",
    "IEnumTfLatticeElements",
    "IEnumTfProperties",
    "IEnumTfPropertyValue",
    "IEnumTfRanges",
    "IEnumTfUIElements",
    "IInternalDocWrap",
    "ILMCM_CHECKLAYOUTANDTIPENABLED",
    "ILMCM_LANGUAGEBAROFF",
    "INSERT_TEXT_AT_SELECTION_FLAGS",
    "IS_ADDRESS_CITY",
    "IS_ADDRESS_COUNTRYNAME",
    "IS_ADDRESS_COUNTRYSHORTNAME",
    "IS_ADDRESS_FULLPOSTALADDRESS",
    "IS_ADDRESS_POSTALCODE",
    "IS_ADDRESS_STATEORPROVINCE",
    "IS_ADDRESS_STREET",
    "IS_ALPHANUMERIC_FULLWIDTH",
    "IS_ALPHANUMERIC_HALFWIDTH",
    "IS_ALPHANUMERIC_PIN",
    "IS_ALPHANUMERIC_PIN_SET",
    "IS_BOPOMOFO",
    "IS_CHAT",
    "IS_CHAT_WITHOUT_EMOJI",
    "IS_CHINESE_FULLWIDTH",
    "IS_CHINESE_HALFWIDTH",
    "IS_CURRENCY_AMOUNT",
    "IS_CURRENCY_AMOUNTANDSYMBOL",
    "IS_CURRENCY_CHINESE",
    "IS_DATE_DAY",
    "IS_DATE_DAYNAME",
    "IS_DATE_FULLDATE",
    "IS_DATE_MONTH",
    "IS_DATE_MONTHNAME",
    "IS_DATE_YEAR",
    "IS_DEFAULT",
    "IS_DIGITS",
    "IS_EMAILNAME_OR_ADDRESS",
    "IS_EMAIL_SMTPEMAILADDRESS",
    "IS_EMAIL_USERNAME",
    "IS_ENUMSTRING",
    "IS_FILE_FILENAME",
    "IS_FILE_FULLFILEPATH",
    "IS_FORMULA",
    "IS_FORMULA_NUMBER",
    "IS_HANGUL_FULLWIDTH",
    "IS_HANGUL_HALFWIDTH",
    "IS_HANJA",
    "IS_HIRAGANA",
    "IS_KATAKANA_FULLWIDTH",
    "IS_KATAKANA_HALFWIDTH",
    "IS_LOGINNAME",
    "IS_MAPS",
    "IS_NAME_OR_PHONENUMBER",
    "IS_NATIVE_SCRIPT",
    "IS_NUMBER",
    "IS_NUMBER_FULLWIDTH",
    "IS_NUMERIC_PASSWORD",
    "IS_NUMERIC_PIN",
    "IS_ONECHAR",
    "IS_PASSWORD",
    "IS_PERSONALNAME_FULLNAME",
    "IS_PERSONALNAME_GIVENNAME",
    "IS_PERSONALNAME_MIDDLENAME",
    "IS_PERSONALNAME_PREFIX",
    "IS_PERSONALNAME_SUFFIX",
    "IS_PERSONALNAME_SURNAME",
    "IS_PHRASELIST",
    "IS_PRIVATE",
    "IS_REGULAREXPRESSION",
    "IS_SEARCH",
    "IS_SEARCH_INCREMENTAL",
    "IS_SRGS",
    "IS_TELEPHONE_AREACODE",
    "IS_TELEPHONE_COUNTRYCODE",
    "IS_TELEPHONE_FULLTELEPHONENUMBER",
    "IS_TELEPHONE_LOCALNUMBER",
    "IS_TEXT",
    "IS_TIME_FULLTIME",
    "IS_TIME_HOUR",
    "IS_TIME_MINORSEC",
    "IS_URL",
    "IS_XML",
    "IS_YOMI",
    "ISpeechCommandProvider",
    "ITextStoreACP",
    "ITextStoreACP2",
    "ITextStoreACPEx",
    "ITextStoreACPServices",
    "ITextStoreACPSink",
    "ITextStoreACPSinkEx",
    "ITextStoreAnchor",
    "ITextStoreAnchorEx",
    "ITextStoreAnchorSink",
    "ITextStoreSinkAnchorEx",
    "ITfActiveLanguageProfileNotifySink",
    "ITfCandidateList",
    "ITfCandidateListUIElement",
    "ITfCandidateListUIElementBehavior",
    "ITfCandidateString",
    "ITfCategoryMgr",
    "ITfCleanupContextDurationSink",
    "ITfCleanupContextSink",
    "ITfClientId",
    "ITfCompartment",
    "ITfCompartmentEventSink",
    "ITfCompartmentMgr",
    "ITfComposition",
    "ITfCompositionSink",
    "ITfCompositionView",
    "ITfConfigureSystemKeystrokeFeed",
    "ITfContext",
    "ITfContextComposition",
    "ITfContextKeyEventSink",
    "ITfContextOwner",
    "ITfContextOwnerCompositionServices",
    "ITfContextOwnerCompositionSink",
    "ITfContextOwnerServices",
    "ITfContextView",
    "ITfCreatePropertyStore",
    "ITfDisplayAttributeInfo",
    "ITfDisplayAttributeMgr",
    "ITfDisplayAttributeNotifySink",
    "ITfDisplayAttributeProvider",
    "ITfDocumentMgr",
    "ITfEditRecord",
    "ITfEditSession",
    "ITfEditTransactionSink",
    "ITfFnAdviseText",
    "ITfFnBalloon",
    "ITfFnConfigure",
    "ITfFnConfigureRegisterEudc",
    "ITfFnConfigureRegisterWord",
    "ITfFnCustomSpeechCommand",
    "ITfFnGetLinguisticAlternates",
    "ITfFnGetPreferredTouchKeyboardLayout",
    "ITfFnGetSAPIObject",
    "ITfFnLMInternal",
    "ITfFnLMProcessor",
    "ITfFnLangProfileUtil",
    "ITfFnPlayBack",
    "ITfFnPropertyUIStatus",
    "ITfFnReconversion",
    "ITfFnSearchCandidateProvider",
    "ITfFnShowHelp",
    "ITfFunction",
    "ITfFunctionProvider",
    "ITfInputProcessorProfileActivationSink",
    "ITfInputProcessorProfileMgr",
    "ITfInputProcessorProfileSubstituteLayout",
    "ITfInputProcessorProfiles",
    "ITfInputProcessorProfilesEx",
    "ITfInputScope",
    "ITfInputScope2",
    "ITfInsertAtSelection",
    "ITfIntegratableCandidateListUIElement",
    "ITfKeyEventSink",
    "ITfKeyTraceEventSink",
    "ITfKeystrokeMgr",
    "ITfLMLattice",
    "ITfLangBarEventSink",
    "ITfLangBarItem",
    "ITfLangBarItemBalloon",
    "ITfLangBarItemBitmap",
    "ITfLangBarItemBitmapButton",
    "ITfLangBarItemButton",
    "ITfLangBarItemMgr",
    "ITfLangBarItemSink",
    "ITfLangBarMgr",
    "ITfLanguageProfileNotifySink",
    "ITfMSAAControl",
    "ITfMenu",
    "ITfMessagePump",
    "ITfMouseSink",
    "ITfMouseTracker",
    "ITfMouseTrackerACP",
    "ITfPersistentPropertyLoaderACP",
    "ITfPreservedKeyNotifySink",
    "ITfProperty",
    "ITfPropertyStore",
    "ITfQueryEmbedded",
    "ITfRange",
    "ITfRangeACP",
    "ITfRangeBackup",
    "ITfReadOnlyProperty",
    "ITfReadingInformationUIElement",
    "ITfReverseConversion",
    "ITfReverseConversionList",
    "ITfReverseConversionMgr",
    "ITfSource",
    "ITfSourceSingle",
    "ITfSpeechUIServer",
    "ITfStatusSink",
    "ITfSystemDeviceTypeLangBarItem",
    "ITfSystemLangBarItem",
    "ITfSystemLangBarItemSink",
    "ITfSystemLangBarItemText",
    "ITfTextEditSink",
    "ITfTextInputProcessor",
    "ITfTextInputProcessorEx",
    "ITfTextLayoutSink",
    "ITfThreadFocusSink",
    "ITfThreadMgr",
    "ITfThreadMgr2",
    "ITfThreadMgrEventSink",
    "ITfThreadMgrEx",
    "ITfToolTipUIElement",
    "ITfTransitoryExtensionSink",
    "ITfTransitoryExtensionUIElement",
    "ITfUIElement",
    "ITfUIElementMgr",
    "ITfUIElementSink",
    "IUIManagerEventSink",
    "IVersionInfo",
    "InitLocalMsCtfMonitor",
    "InputScope",
    "LANG_BAR_ITEM_ICON_MODE_FLAGS",
    "LIBID_MSAATEXTLib",
    "MSAAControl",
    "STYLE_ACTIVE_SELECTION",
    "STYLE_IMPLIED_SELECTION",
    "TEXT_STORE_CHANGE_FLAGS",
    "TEXT_STORE_LOCK_FLAGS",
    "TEXT_STORE_TEXT_CHANGE_FLAGS",
    "TF_AE_END",
    "TF_AE_NONE",
    "TF_AE_START",
    "TF_ANCHOR_END",
    "TF_ANCHOR_START",
    "TF_ATTR_CONVERTED",
    "TF_ATTR_FIXEDCONVERTED",
    "TF_ATTR_INPUT",
    "TF_ATTR_INPUT_ERROR",
    "TF_ATTR_OTHER",
    "TF_ATTR_TARGET_CONVERTED",
    "TF_ATTR_TARGET_NOTCONVERTED",
    "TF_CHAR_EMBEDDED",
    "TF_CLUIE_COUNT",
    "TF_CLUIE_CURRENTPAGE",
    "TF_CLUIE_DOCUMENTMGR",
    "TF_CLUIE_PAGEINDEX",
    "TF_CLUIE_SELECTION",
    "TF_CLUIE_STRING",
    "TF_COMMANDING_ENABLED",
    "TF_COMMANDING_ON",
    "TF_CONTEXT_EDIT_CONTEXT_FLAGS",
    "TF_CONVERSIONMODE_ALPHANUMERIC",
    "TF_CONVERSIONMODE_CHARCODE",
    "TF_CONVERSIONMODE_EUDC",
    "TF_CONVERSIONMODE_FIXED",
    "TF_CONVERSIONMODE_FULLSHAPE",
    "TF_CONVERSIONMODE_KATAKANA",
    "TF_CONVERSIONMODE_NATIVE",
    "TF_CONVERSIONMODE_NOCONVERSION",
    "TF_CONVERSIONMODE_ROMAN",
    "TF_CONVERSIONMODE_SOFTKEYBOARD",
    "TF_CONVERSIONMODE_SYMBOL",
    "TF_CT_COLORREF",
    "TF_CT_NONE",
    "TF_CT_SYSCOLOR",
    "TF_DA_ATTR_INFO",
    "TF_DA_COLOR",
    "TF_DA_COLORTYPE",
    "TF_DA_LINESTYLE",
    "TF_DEFAULT_SELECTION",
    "TF_DICTATION_ENABLED",
    "TF_DICTATION_ON",
    "TF_DISABLE_BALLOON",
    "TF_DISABLE_COMMANDING",
    "TF_DISABLE_DICTATION",
    "TF_DISABLE_SPEECH",
    "TF_DISPLAYATTRIBUTE",
    "TF_DTLBI_NONE",
    "TF_DTLBI_USEPROFILEICON",
    "TF_ENABLE_PROCESS_ATOM",
    "TF_ES_ASYNC",
    "TF_ES_ASYNCDONTCARE",
    "TF_ES_READ",
    "TF_ES_READWRITE",
    "TF_ES_SYNC",
    "TF_E_ALREADY_EXISTS",
    "TF_E_COMPOSITION_REJECTED",
    "TF_E_DISCONNECTED",
    "TF_E_EMPTYCONTEXT",
    "TF_E_FORMAT",
    "TF_E_INVALIDPOINT",
    "TF_E_INVALIDPOS",
    "TF_E_INVALIDVIEW",
    "TF_E_LOCKED",
    "TF_E_NOCONVERSION",
    "TF_E_NOINTERFACE",
    "TF_E_NOLAYOUT",
    "TF_E_NOLOCK",
    "TF_E_NOOBJECT",
    "TF_E_NOPROVIDER",
    "TF_E_NOSELECTION",
    "TF_E_NOSERVICE",
    "TF_E_NOTOWNEDRANGE",
    "TF_E_RANGE_NOT_COVERED",
    "TF_E_READONLY",
    "TF_E_STACKFULL",
    "TF_E_SYNCHRONOUS",
    "TF_FLOATINGLANGBAR_WNDTITLE",
    "TF_FLOATINGLANGBAR_WNDTITLEA",
    "TF_FLOATINGLANGBAR_WNDTITLEW",
    "TF_GRAVITY_BACKWARD",
    "TF_GRAVITY_FORWARD",
    "TF_GTP_INCL_TEXT",
    "TF_GTP_NONE",
    "TF_HALTCOND",
    "TF_HF_OBJECT",
    "TF_IAS_NOQUERY",
    "TF_IAS_NO_DEFAULT_COMPOSITION",
    "TF_IAS_QUERYONLY",
    "TF_IE_CORRECTION",
    "TF_INPUTPROCESSORPROFILE",
    "TF_INVALID_COOKIE",
    "TF_INVALID_EDIT_COOKIE",
    "TF_IPPMF_DISABLEPROFILE",
    "TF_IPPMF_DONTCARECURRENTINPUTLANGUAGE",
    "TF_IPPMF_ENABLEPROFILE",
    "TF_IPPMF_FORPROCESS",
    "TF_IPPMF_FORSESSION",
    "TF_IPPMF_FORSYSTEMALL",
    "TF_IPP_CAPS_COMLESSSUPPORT",
    "TF_IPP_CAPS_DISABLEONTRANSITORY",
    "TF_IPP_CAPS_IMMERSIVESUPPORT",
    "TF_IPP_CAPS_SECUREMODESUPPORT",
    "TF_IPP_CAPS_SYSTRAYSUPPORT",
    "TF_IPP_CAPS_UIELEMENTENABLED",
    "TF_IPP_CAPS_WOW16SUPPORT",
    "TF_IPP_FLAG_ACTIVE",
    "TF_IPP_FLAG_ENABLED",
    "TF_IPP_FLAG_SUBSTITUTEDBYINPUTPROCESSOR",
    "TF_IPSINK_FLAG_ACTIVE",
    "TF_LANGBARITEMINFO",
    "TF_LANGUAGEPROFILE",
    "TF_LBBALLOONINFO",
    "TF_LBI_BALLOON",
    "TF_LBI_BITMAP",
    "TF_LBI_BMPF_VERTICAL",
    "TF_LBI_CLK_LEFT",
    "TF_LBI_CLK_RIGHT",
    "TF_LBI_CUSTOMUI",
    "TF_LBI_DESC_MAXLEN",
    "TF_LBI_ICON",
    "TF_LBI_STATUS",
    "TF_LBI_STATUS_BTN_TOGGLED",
    "TF_LBI_STATUS_DISABLED",
    "TF_LBI_STATUS_HIDDEN",
    "TF_LBI_STYLE_BTN_BUTTON",
    "TF_LBI_STYLE_BTN_MENU",
    "TF_LBI_STYLE_BTN_TOGGLE",
    "TF_LBI_STYLE_HIDDENBYDEFAULT",
    "TF_LBI_STYLE_HIDDENSTATUSCONTROL",
    "TF_LBI_STYLE_HIDEONNOOTHERITEMS",
    "TF_LBI_STYLE_SHOWNINTRAY",
    "TF_LBI_STYLE_SHOWNINTRAYONLY",
    "TF_LBI_STYLE_TEXTCOLORICON",
    "TF_LBI_TEXT",
    "TF_LBI_TOOLTIP",
    "TF_LBMENUF_CHECKED",
    "TF_LBMENUF_GRAYED",
    "TF_LBMENUF_RADIOCHECKED",
    "TF_LBMENUF_SEPARATOR",
    "TF_LBMENUF_SUBMENU",
    "TF_LB_BALLOON_MISS",
    "TF_LB_BALLOON_RECO",
    "TF_LB_BALLOON_SHOW",
    "TF_LC_CHANGE",
    "TF_LC_CREATE",
    "TF_LC_DESTROY",
    "TF_LMLATTELEMENT",
    "TF_LS_DASH",
    "TF_LS_DOT",
    "TF_LS_NONE",
    "TF_LS_SOLID",
    "TF_LS_SQUIGGLE",
    "TF_MENUREADY",
    "TF_MOD_ALT",
    "TF_MOD_CONTROL",
    "TF_MOD_IGNORE_ALL_MODIFIER",
    "TF_MOD_LALT",
    "TF_MOD_LCONTROL",
    "TF_MOD_LSHIFT",
    "TF_MOD_ON_KEYUP",
    "TF_MOD_RALT",
    "TF_MOD_RCONTROL",
    "TF_MOD_RSHIFT",
    "TF_MOD_SHIFT",
    "TF_PERSISTENT_PROPERTY_HEADER_ACP",
    "TF_POPF_ALL",
    "TF_PRESERVEDKEY",
    "TF_PROCESS_ATOM",
    "TF_PROFILETYPE_INPUTPROCESSOR",
    "TF_PROFILETYPE_KEYBOARDLAYOUT",
    "TF_PROFILE_ARRAY",
    "TF_PROFILE_CANTONESE",
    "TF_PROFILE_CHANGJIE",
    "TF_PROFILE_DAYI",
    "TF_PROFILE_NEWCHANGJIE",
    "TF_PROFILE_NEWPHONETIC",
    "TF_PROFILE_NEWQUICK",
    "TF_PROFILE_PHONETIC",
    "TF_PROFILE_PINYIN",
    "TF_PROFILE_QUICK",
    "TF_PROFILE_SIMPLEFAST",
    "TF_PROFILE_TIGRINYA",
    "TF_PROFILE_WUBI",
    "TF_PROFILE_YI",
    "TF_PROPERTYVAL",
    "TF_PROPUI_STATUS_SAVETOFILE",
    "TF_RCM_COMLESS",
    "TF_RCM_HINT_COLLISION",
    "TF_RCM_HINT_READING_LENGTH",
    "TF_RCM_VKEY",
    "TF_RIP_FLAG_FREEUNUSEDLIBRARIES",
    "TF_RIUIE_CONTEXT",
    "TF_RIUIE_ERRORINDEX",
    "TF_RIUIE_MAXREADINGSTRINGLENGTH",
    "TF_RIUIE_STRING",
    "TF_RIUIE_VERTICALORDER",
    "TF_RP_HIDDENINSETTINGUI",
    "TF_RP_LOCALPROCESS",
    "TF_RP_LOCALTHREAD",
    "TF_RP_SUBITEMINSETTINGUI",
    "TF_SD_BACKWARD",
    "TF_SD_FORWARD",
    "TF_SD_LOADING",
    "TF_SD_READONLY",
    "TF_SELECTION",
    "TF_SELECTIONSTYLE",
    "TF_SENTENCEMODE_AUTOMATIC",
    "TF_SENTENCEMODE_CONVERSATION",
    "TF_SENTENCEMODE_NONE",
    "TF_SENTENCEMODE_PHRASEPREDICT",
    "TF_SENTENCEMODE_PLAURALCLAUSE",
    "TF_SENTENCEMODE_SINGLECONVERT",
    "TF_SFT_DESKBAND",
    "TF_SFT_DOCK",
    "TF_SFT_EXTRAICONSONMINIMIZED",
    "TF_SFT_HIDDEN",
    "TF_SFT_HIGHTRANSPARENCY",
    "TF_SFT_LABELS",
    "TF_SFT_LOWTRANSPARENCY",
    "TF_SFT_MINIMIZED",
    "TF_SFT_NOEXTRAICONSONMINIMIZED",
    "TF_SFT_NOLABELS",
    "TF_SFT_NOTRANSPARENCY",
    "TF_SFT_SHOWNORMAL",
    "TF_SHOW_BALLOON",
    "TF_SPEECHUI_SHOWN",
    "TF_SS_DISJOINTSEL",
    "TF_SS_REGIONS",
    "TF_SS_TKBAUTOCORRECTENABLE",
    "TF_SS_TKBPREDICTIONENABLE",
    "TF_SS_TRANSITORY",
    "TF_ST_CORRECTION",
    "TF_S_ASYNC",
    "TF_TF_IGNOREEND",
    "TF_TF_MOVESTART",
    "TF_TMAE_COMLESS",
    "TF_TMAE_CONSOLE",
    "TF_TMAE_NOACTIVATEKEYBOARDLAYOUT",
    "TF_TMAE_NOACTIVATETIP",
    "TF_TMAE_SECUREMODE",
    "TF_TMAE_UIELEMENTENABLEDONLY",
    "TF_TMAE_WOW16",
    "TF_TMF_ACTIVATED",
    "TF_TMF_COMLESS",
    "TF_TMF_CONSOLE",
    "TF_TMF_IMMERSIVEMODE",
    "TF_TMF_NOACTIVATETIP",
    "TF_TMF_SECUREMODE",
    "TF_TMF_UIELEMENTENABLEDONLY",
    "TF_TMF_WOW16",
    "TF_TRANSITORYEXTENSION_ATSELECTION",
    "TF_TRANSITORYEXTENSION_FLOATING",
    "TF_TRANSITORYEXTENSION_NONE",
    "TF_TU_CORRECTION",
    "TF_URP_ALLPROFILES",
    "TF_URP_LOCALPROCESS",
    "TF_URP_LOCALTHREAD",
    "TF_US_HIDETIPUI",
    "TKBLT_CLASSIC",
    "TKBLT_OPTIMIZED",
    "TKBLT_UNDEFINED",
    "TKBL_CLASSIC_TRADITIONAL_CHINESE_CHANGJIE",
    "TKBL_CLASSIC_TRADITIONAL_CHINESE_DAYI",
    "TKBL_CLASSIC_TRADITIONAL_CHINESE_PHONETIC",
    "TKBL_OPT_JAPANESE_ABC",
    "TKBL_OPT_KOREAN_HANGUL_2_BULSIK",
    "TKBL_OPT_SIMPLIFIED_CHINESE_PINYIN",
    "TKBL_OPT_TRADITIONAL_CHINESE_PHONETIC",
    "TKBL_UNDEFINED",
    "TKBLayoutType",
    "TKB_ALTERNATES_AUTOCORRECTION_APPLIED",
    "TKB_ALTERNATES_FOR_AUTOCORRECTION",
    "TKB_ALTERNATES_FOR_PREDICTION",
    "TKB_ALTERNATES_STANDARD",
    "TSATTRID_App",
    "TSATTRID_App_IncorrectGrammar",
    "TSATTRID_App_IncorrectSpelling",
    "TSATTRID_Font",
    "TSATTRID_Font_FaceName",
    "TSATTRID_Font_SizePts",
    "TSATTRID_Font_Style",
    "TSATTRID_Font_Style_Animation",
    "TSATTRID_Font_Style_Animation_BlinkingBackground",
    "TSATTRID_Font_Style_Animation_LasVegasLights",
    "TSATTRID_Font_Style_Animation_MarchingBlackAnts",
    "TSATTRID_Font_Style_Animation_MarchingRedAnts",
    "TSATTRID_Font_Style_Animation_Shimmer",
    "TSATTRID_Font_Style_Animation_SparkleText",
    "TSATTRID_Font_Style_Animation_WipeDown",
    "TSATTRID_Font_Style_Animation_WipeRight",
    "TSATTRID_Font_Style_BackgroundColor",
    "TSATTRID_Font_Style_Blink",
    "TSATTRID_Font_Style_Bold",
    "TSATTRID_Font_Style_Capitalize",
    "TSATTRID_Font_Style_Color",
    "TSATTRID_Font_Style_Emboss",
    "TSATTRID_Font_Style_Engrave",
    "TSATTRID_Font_Style_Height",
    "TSATTRID_Font_Style_Hidden",
    "TSATTRID_Font_Style_Italic",
    "TSATTRID_Font_Style_Kerning",
    "TSATTRID_Font_Style_Lowercase",
    "TSATTRID_Font_Style_Outlined",
    "TSATTRID_Font_Style_Overline",
    "TSATTRID_Font_Style_Overline_Double",
    "TSATTRID_Font_Style_Overline_Single",
    "TSATTRID_Font_Style_Position",
    "TSATTRID_Font_Style_Protected",
    "TSATTRID_Font_Style_Shadow",
    "TSATTRID_Font_Style_SmallCaps",
    "TSATTRID_Font_Style_Spacing",
    "TSATTRID_Font_Style_Strikethrough",
    "TSATTRID_Font_Style_Strikethrough_Double",
    "TSATTRID_Font_Style_Strikethrough_Single",
    "TSATTRID_Font_Style_Subscript",
    "TSATTRID_Font_Style_Superscript",
    "TSATTRID_Font_Style_Underline",
    "TSATTRID_Font_Style_Underline_Double",
    "TSATTRID_Font_Style_Underline_Single",
    "TSATTRID_Font_Style_Uppercase",
    "TSATTRID_Font_Style_Weight",
    "TSATTRID_List",
    "TSATTRID_List_LevelIndel",
    "TSATTRID_List_Type",
    "TSATTRID_List_Type_Arabic",
    "TSATTRID_List_Type_Bullet",
    "TSATTRID_List_Type_LowerLetter",
    "TSATTRID_List_Type_LowerRoman",
    "TSATTRID_List_Type_UpperLetter",
    "TSATTRID_List_Type_UpperRoman",
    "TSATTRID_OTHERS",
    "TSATTRID_Text",
    "TSATTRID_Text_Alignment",
    "TSATTRID_Text_Alignment_Center",
    "TSATTRID_Text_Alignment_Justify",
    "TSATTRID_Text_Alignment_Left",
    "TSATTRID_Text_Alignment_Right",
    "TSATTRID_Text_EmbeddedObject",
    "TSATTRID_Text_Hyphenation",
    "TSATTRID_Text_Language",
    "TSATTRID_Text_Link",
    "TSATTRID_Text_Orientation",
    "TSATTRID_Text_Para",
    "TSATTRID_Text_Para_FirstLineIndent",
    "TSATTRID_Text_Para_LeftIndent",
    "TSATTRID_Text_Para_LineSpacing",
    "TSATTRID_Text_Para_LineSpacing_AtLeast",
    "TSATTRID_Text_Para_LineSpacing_Double",
    "TSATTRID_Text_Para_LineSpacing_Exactly",
    "TSATTRID_Text_Para_LineSpacing_Multiple",
    "TSATTRID_Text_Para_LineSpacing_OnePtFive",
    "TSATTRID_Text_Para_LineSpacing_Single",
    "TSATTRID_Text_Para_RightIndent",
    "TSATTRID_Text_Para_SpaceAfter",
    "TSATTRID_Text_Para_SpaceBefore",
    "TSATTRID_Text_ReadOnly",
    "TSATTRID_Text_RightToLeft",
    "TSATTRID_Text_VerticalWriting",
    "TS_AE_END",
    "TS_AE_NONE",
    "TS_AE_START",
    "TS_AS_ATTR_CHANGE",
    "TS_AS_LAYOUT_CHANGE",
    "TS_AS_SEL_CHANGE",
    "TS_AS_STATUS_CHANGE",
    "TS_AS_TEXT_CHANGE",
    "TS_ATTRVAL",
    "TS_ATTR_FIND_BACKWARDS",
    "TS_ATTR_FIND_HIDDEN",
    "TS_ATTR_FIND_UPDATESTART",
    "TS_ATTR_FIND_WANT_END",
    "TS_ATTR_FIND_WANT_OFFSET",
    "TS_ATTR_FIND_WANT_VALUE",
    "TS_CHAR_EMBEDDED",
    "TS_CHAR_REGION",
    "TS_CHAR_REPLACEMENT",
    "TS_CH_FOLLOWING_DEL",
    "TS_CH_PRECEDING_DEL",
    "TS_DEFAULT_SELECTION",
    "TS_E_FORMAT",
    "TS_E_INVALIDPOINT",
    "TS_E_INVALIDPOS",
    "TS_E_NOINTERFACE",
    "TS_E_NOLAYOUT",
    "TS_E_NOLOCK",
    "TS_E_NOOBJECT",
    "TS_E_NOSELECTION",
    "TS_E_NOSERVICE",
    "TS_E_READONLY",
    "TS_E_SYNCHRONOUS",
    "TS_GEA_HIDDEN",
    "TS_GR_BACKWARD",
    "TS_GR_FORWARD",
    "TS_GTA_HIDDEN",
    "TS_IAS_NOQUERY",
    "TS_IAS_QUERYONLY",
    "TS_IE_COMPOSITION",
    "TS_IE_CORRECTION",
    "TS_LC_CHANGE",
    "TS_LC_CREATE",
    "TS_LC_DESTROY",
    "TS_LF_READ",
    "TS_LF_READWRITE",
    "TS_LF_SYNC",
    "TS_RT_HIDDEN",
    "TS_RT_OPAQUE",
    "TS_RT_PLAIN",
    "TS_RUNINFO",
    "TS_SD_BACKWARD",
    "TS_SD_EMBEDDEDHANDWRITINGVIEW_ENABLED",
    "TS_SD_EMBEDDEDHANDWRITINGVIEW_VISIBLE",
    "TS_SD_FORWARD",
    "TS_SD_INPUTPANEMANUALDISPLAYENABLE",
    "TS_SD_LOADING",
    "TS_SD_READONLY",
    "TS_SD_RESERVED",
    "TS_SD_TKBAUTOCORRECTENABLE",
    "TS_SD_TKBPREDICTIONENABLE",
    "TS_SD_UIINTEGRATIONENABLE",
    "TS_SELECTIONSTYLE",
    "TS_SELECTION_ACP",
    "TS_SELECTION_ANCHOR",
    "TS_SHIFT_COUNT_HIDDEN",
    "TS_SHIFT_COUNT_ONLY",
    "TS_SHIFT_HALT_HIDDEN",
    "TS_SHIFT_HALT_VISIBLE",
    "TS_SS_DISJOINTSEL",
    "TS_SS_NOHIDDENTEXT",
    "TS_SS_REGIONS",
    "TS_SS_TKBAUTOCORRECTENABLE",
    "TS_SS_TKBPREDICTIONENABLE",
    "TS_SS_TRANSITORY",
    "TS_SS_UWPCONTROL",
    "TS_STATUS",
    "TS_STRF_END",
    "TS_STRF_MID",
    "TS_STRF_START",
    "TS_ST_CORRECTION",
    "TS_ST_NONE",
    "TS_S_ASYNC",
    "TS_TC_CORRECTION",
    "TS_TC_NONE",
    "TS_TEXTCHANGE",
    "TS_VCOOKIE_NUL",
    "TfActiveSelEnd",
    "TfAnchor",
    "TfCandidateResult",
    "TfGravity",
    "TfIntegratableCandidateListSelectionStyle",
    "TfLBBalloonStyle",
    "TfLBIClick",
    "TfLayoutCode",
    "TfSapiObject",
    "TfShiftDir",
    "TsActiveSelEnd",
    "TsGravity",
    "TsLayoutCode",
    "TsRunType",
    "TsShiftDir",
    "UninitLocalMsCtfMonitor",
]
