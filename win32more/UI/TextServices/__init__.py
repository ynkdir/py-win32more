from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.UI.TextServices
import win32more.UI.WindowsAndMessaging
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
ANCHOR_CHANGE_HISTORY_FLAGS = UInt32
TS_CH_PRECEDING_DEL: ANCHOR_CHANGE_HISTORY_FLAGS = 1
TS_CH_FOLLOWING_DEL: ANCHOR_CHANGE_HISTORY_FLAGS = 2
AccClientDocMgr = Guid('fc48cc30-4f3e-4fa1-80-3b-ad-0e-19-6a-83-b1')
AccDictionary = Guid('6572ee16-5fe5-4331-bb-6d-76-a4-9c-56-e4-23')
AccServerDocMgr = Guid('6089a37e-eb8a-482d-bd-6f-f9-f4-69-04-d1-6d')
AccStore = Guid('5440837f-4bff-4ae5-a1-b1-77-22-ec-c6-33-2a')
GUID_PROP_TEXTOWNER: Guid = Guid('f1e2d520-0969-11d3-8d-f0-00-10-5a-27-99-b5')
GUID_PROP_ATTRIBUTE: Guid = Guid('34b45670-7526-11d2-a1-47-00-10-5a-27-99-b5')
GUID_PROP_LANGID: Guid = Guid('3280ce20-8032-11d2-b6-03-00-10-5a-27-99-b5')
GUID_PROP_READING: Guid = Guid('5463f7c0-8e31-11d2-bf-46-00-10-5a-27-99-b5')
GUID_PROP_COMPOSING: Guid = Guid('e12ac060-af15-11d2-af-c5-00-10-5a-27-99-b5')
GUID_PROP_TKB_ALTERNATES: Guid = Guid('70b2a803-968d-462e-b9-3b-21-64-c9-15-17-f7')
GUID_SYSTEM_FUNCTIONPROVIDER: Guid = Guid('9a698bb0-0f21-11d3-8d-f1-00-10-5a-27-99-b5')
GUID_APP_FUNCTIONPROVIDER: Guid = Guid('4caef01e-12af-4b0e-9d-b1-a6-ec-5b-88-12-08')
GUID_TFCAT_CATEGORY_OF_TIP: Guid = Guid('534c48c1-0607-4098-a5-21-4f-c8-99-c7-3e-90')
GUID_TFCAT_TIP_KEYBOARD: Guid = Guid('34745c63-b2f0-4784-8b-67-5e-12-c8-70-1a-31')
GUID_TFCAT_TIP_SPEECH: Guid = Guid('b5a73cd1-8355-426b-a1-61-25-98-08-f2-6b-14')
GUID_TFCAT_TIP_HANDWRITING: Guid = Guid('246ecb87-c2f2-4abe-90-5b-c8-b3-8a-dd-2c-43')
GUID_TFCAT_PROP_AUDIODATA: Guid = Guid('9b7be3a9-e8ab-4d47-a8-fe-25-4f-a4-23-43-6d')
GUID_TFCAT_PROP_INKDATA: Guid = Guid('7c6a82ae-b0d7-4f14-a7-45-14-f2-8b-00-9d-61')
GUID_COMPARTMENT_SAPI_AUDIO: Guid = Guid('51af2086-cc6b-457d-b5-aa-8b-19-dc-29-0a-b4')
GUID_COMPARTMENT_KEYBOARD_DISABLED: Guid = Guid('71a5b253-1951-466b-9f-bc-9c-88-08-fa-84-f2')
GUID_COMPARTMENT_KEYBOARD_OPENCLOSE: Guid = Guid('58273aad-01bb-4164-95-c6-75-5b-a0-b5-16-2d')
GUID_COMPARTMENT_HANDWRITING_OPENCLOSE: Guid = Guid('f9ae2c6b-1866-4361-af-72-7a-a3-09-48-89-0e')
GUID_COMPARTMENT_SPEECH_DISABLED: Guid = Guid('56c5c607-0703-4e59-8e-52-cb-c8-4e-8b-be-35')
GUID_COMPARTMENT_SPEECH_OPENCLOSE: Guid = Guid('544d6a63-e2e8-4752-bb-d1-00-09-60-bc-a0-83')
GUID_COMPARTMENT_SPEECH_GLOBALSTATE: Guid = Guid('2a54fe8e-0d08-460c-a7-5d-87-03-5f-f4-36-c5')
GUID_COMPARTMENT_CONVERSIONMODEBIAS: Guid = Guid('5497f516-ee91-436e-b9-46-aa-2c-05-f1-ac-5b')
GUID_PROP_MODEBIAS: Guid = Guid('372e0716-974f-40ac-a0-88-08-cd-c9-2e-bf-bc')
GUID_COMPARTMENT_KEYBOARD_INPUTMODE: Guid = Guid('b6592511-bcee-4122-a7-c4-09-f4-b3-fa-43-96')
GUID_MODEBIAS_NONE: Guid = Guid('00000000-0000-0000-00-00-00-00-00-00-00-00')
GUID_MODEBIAS_URLHISTORY: Guid = Guid('8b0e54d9-63f2-4c68-84-d4-79-ae-e7-a5-9f-09')
GUID_MODEBIAS_FILENAME: Guid = Guid('d7f707fe-44c6-4fca-8e-76-86-ab-50-c7-93-1b')
GUID_MODEBIAS_READING: Guid = Guid('e31643a3-6466-4cbf-8d-8b-0b-d4-d8-54-54-61')
GUID_MODEBIAS_DATETIME: Guid = Guid('f2bdb372-7f61-4039-92-ef-1c-35-59-9f-02-22')
GUID_MODEBIAS_NAME: Guid = Guid('fddc10f0-d239-49bf-b8-fc-54-10-ca-aa-42-7e')
GUID_MODEBIAS_CONVERSATION: Guid = Guid('0f4ec104-1790-443b-95-f1-e1-0f-93-9d-65-46')
GUID_MODEBIAS_NUMERIC: Guid = Guid('4021766c-e872-48fd-9c-ee-4e-c5-c7-5e-16-c3')
GUID_MODEBIAS_HIRAGANA: Guid = Guid('d73d316e-9b91-46f1-a2-80-31-59-7f-52-c6-94')
GUID_MODEBIAS_KATAKANA: Guid = Guid('2e0eeddd-3a1a-499e-85-43-3c-7e-e7-94-98-11')
GUID_MODEBIAS_HANGUL: Guid = Guid('76ef0541-23b3-4d77-a0-74-69-18-01-cc-ea-17')
GUID_MODEBIAS_CHINESE: Guid = Guid('7add26de-4328-489b-83-ae-64-93-75-0c-ad-5c')
GUID_MODEBIAS_HALFWIDTHKATAKANA: Guid = Guid('005f6b63-78d4-41cc-88-59-48-5c-a8-21-a7-95')
GUID_MODEBIAS_FULLWIDTHALPHANUMERIC: Guid = Guid('81489fb8-b36a-473d-81-46-e4-a2-25-8b-24-ae')
GUID_MODEBIAS_FULLWIDTHHANGUL: Guid = Guid('c01ae6c9-45b5-4fd0-9c-b1-9f-4c-eb-c3-9f-ea')
GUID_TFCAT_PROPSTYLE_STATIC: Guid = Guid('565fb8d8-6bd4-4ca1-b2-23-0f-2c-cb-8f-4f-96')
GUID_TFCAT_DISPLAYATTRIBUTEPROVIDER: Guid = Guid('046b8c80-1647-40f7-9b-21-b9-3b-81-aa-bc-1b')
GUID_TFCAT_DISPLAYATTRIBUTEPROPERTY: Guid = Guid('b95f181b-ea4c-4af1-80-56-7c-32-1a-bb-b0-91')
GUID_COMPARTMENT_SPEECH_UI_STATUS: Guid = Guid('d92016f0-9367-4fe7-9a-bf-bc-59-da-cb-e0-e3')
GUID_COMPARTMENT_EMPTYCONTEXT: Guid = Guid('d7487dbf-804e-41c5-89-4d-ad-96-fd-4e-ea-13')
GUID_COMPARTMENT_TIPUISTATUS: Guid = Guid('148ca3ec-0366-401c-8d-75-ed-97-8d-85-fb-c9')
GUID_COMPARTMENT_SPEECH_CFGMENU: Guid = Guid('fb6c5c2d-4e83-4bb6-91-a2-e0-19-bf-f6-76-2d')
GUID_LBI_SAPILAYR_CFGMENUBUTTON: Guid = Guid('d02f24a1-942d-422e-8d-99-b4-f2-ad-de-e9-99')
GUID_TFCAT_TIPCAP_SECUREMODE: Guid = Guid('49d2f9ce-1f5e-11d7-a6-d3-00-06-5b-84-43-5c')
GUID_TFCAT_TIPCAP_UIELEMENTENABLED: Guid = Guid('49d2f9cf-1f5e-11d7-a6-d3-00-06-5b-84-43-5c')
GUID_TFCAT_TIPCAP_INPUTMODECOMPARTMENT: Guid = Guid('ccf05dd7-4a87-11d7-a6-e2-00-06-5b-84-43-5c')
GUID_TFCAT_TIPCAP_COMLESS: Guid = Guid('364215d9-75bc-11d7-a6-ef-00-06-5b-84-43-5c')
GUID_TFCAT_TIPCAP_WOW16: Guid = Guid('364215da-75bc-11d7-a6-ef-00-06-5b-84-43-5c')
GUID_TFCAT_TIPCAP_IMMERSIVESUPPORT: Guid = Guid('13a016df-560b-46cd-94-7a-4c-3a-f1-e0-e3-5d')
GUID_TFCAT_TIPCAP_IMMERSIVEONLY: Guid = Guid('3a4259ac-640d-4ad4-89-f7-1e-b6-7e-7c-4e-e8')
GUID_TFCAT_TIPCAP_LOCALSERVER: Guid = Guid('74769ee9-4a66-4f9d-90-d6-bf-8b-7c-3e-b4-61')
GUID_TFCAT_TIPCAP_TSF3: Guid = Guid('07dcb4af-98de-4548-be-f7-25-bd-45-97-9a-1f')
GUID_TFCAT_TIPCAP_DUALMODE: Guid = Guid('3af314a2-d79f-4b1b-99-92-15-08-6d-33-9b-05')
GUID_TFCAT_TIPCAP_SYSTRAYSUPPORT: Guid = Guid('25504fb4-7bab-4bc1-9c-69-cf-81-89-0f-0e-f5')
GUID_COMPARTMENT_KEYBOARD_INPUTMODE_CONVERSION: Guid = Guid('ccf05dd8-4a87-11d7-a6-e2-00-06-5b-84-43-5c')
GUID_COMPARTMENT_KEYBOARD_INPUTMODE_SENTENCE: Guid = Guid('ccf05dd9-4a87-11d7-a6-e2-00-06-5b-84-43-5c')
GUID_COMPARTMENT_TRANSITORYEXTENSION: Guid = Guid('8be347f5-c7a0-11d7-b4-08-00-06-5b-84-43-5c')
GUID_COMPARTMENT_TRANSITORYEXTENSION_DOCUMENTMANAGER: Guid = Guid('8be347f7-c7a0-11d7-b4-08-00-06-5b-84-43-5c')
GUID_COMPARTMENT_TRANSITORYEXTENSION_PARENT: Guid = Guid('8be347f8-c7a0-11d7-b4-08-00-06-5b-84-43-5c')
GUID_COMPARTMENT_ENABLED_PROFILES_UPDATED: Guid = Guid('92c1fd48-a9ae-4a7c-be-08-43-29-e4-72-38-17')
GUID_TFCAT_TRANSITORYEXTENSIONUI: Guid = Guid('6302de22-a5cf-4b02-bf-e8-4d-72-b2-be-d3-c6')
GUID_LBI_INPUTMODE: Guid = Guid('2c77a81e-41cc-4178-a3-a7-5f-8a-98-75-68-e6')
CLSID_TF_ThreadMgr: Guid = Guid('529a9e6b-6587-4f23-ab-9e-9c-7d-68-3e-3c-50')
CLSID_TF_LangBarMgr: Guid = Guid('ebb08c45-6c4a-4fdc-ae-53-4e-b8-c4-c7-db-8e')
CLSID_TF_DisplayAttributeMgr: Guid = Guid('3ce74de4-53d3-4d74-8b-83-43-1b-38-28-ba-53')
CLSID_TF_CategoryMgr: Guid = Guid('a4b544a1-438d-4b41-93-25-86-95-23-e2-d6-c7')
CLSID_TF_InputProcessorProfiles: Guid = Guid('33c53a50-f456-4884-b0-49-85-fd-64-3e-cf-ed')
CLSID_TF_LangBarItemMgr: Guid = Guid('b9931692-a2b3-4fab-bf-33-9e-c6-f9-fb-96-ac')
CLSID_TF_ClassicLangBar: Guid = Guid('3318360c-1afc-4d09-a8-6b-9f-9c-b6-dc-eb-9c')
CLSID_TF_TransitoryExtensionUIEntry: Guid = Guid('ae6be008-07fb-400d-8b-eb-33-7a-64-f7-05-1f')
CLSID_TsfServices: Guid = Guid('39aedc00-6b60-46db-8d-31-36-42-be-0e-43-73')
TF_DEFAULT_SELECTION: UInt64 = 18446744073709551615
TS_DEFAULT_SELECTION: UInt64 = 18446744073709551615
GUID_TS_SERVICE_DATAOBJECT: Guid = Guid('6086fbb5-e225-46ce-a7-70-c1-bb-d3-e0-5d-7b')
GUID_TS_SERVICE_ACCESSIBLE: Guid = Guid('f9786200-a5bf-4a0f-8c-24-fb-16-f5-d1-aa-bb')
GUID_TS_SERVICE_ACTIVEX: Guid = Guid('ea937a50-c9a6-4b7d-89-4a-49-d9-9b-78-48-34')
TS_E_INVALIDPOS: win32more.Foundation.HRESULT = -2147220992
TS_E_NOLOCK: win32more.Foundation.HRESULT = -2147220991
TS_E_NOOBJECT: win32more.Foundation.HRESULT = -2147220990
TS_E_NOSERVICE: win32more.Foundation.HRESULT = -2147220989
TS_E_NOINTERFACE: win32more.Foundation.HRESULT = -2147220988
TS_E_NOSELECTION: win32more.Foundation.HRESULT = -2147220987
TS_E_NOLAYOUT: win32more.Foundation.HRESULT = -2147220986
TS_E_INVALIDPOINT: win32more.Foundation.HRESULT = -2147220985
TS_E_SYNCHRONOUS: win32more.Foundation.HRESULT = -2147220984
TS_E_READONLY: win32more.Foundation.HRESULT = -2147220983
TS_E_FORMAT: win32more.Foundation.HRESULT = -2147220982
TS_S_ASYNC: win32more.Foundation.HRESULT = 262912
TS_AS_TEXT_CHANGE: UInt32 = 1
TS_AS_SEL_CHANGE: UInt32 = 2
TS_AS_LAYOUT_CHANGE: UInt32 = 4
TS_AS_ATTR_CHANGE: UInt32 = 8
TS_AS_STATUS_CHANGE: UInt32 = 16
TS_LF_SYNC: UInt32 = 1
TS_SD_READONLY: UInt32 = 1
TS_SD_LOADING: UInt32 = 2
TS_SD_RESERVED: UInt32 = 4
TS_SD_TKBAUTOCORRECTENABLE: UInt32 = 8
TS_SD_TKBPREDICTIONENABLE: UInt32 = 16
TS_SD_UIINTEGRATIONENABLE: UInt32 = 32
TS_SD_INPUTPANEMANUALDISPLAYENABLE: UInt32 = 64
TS_SD_EMBEDDEDHANDWRITINGVIEW_ENABLED: UInt32 = 128
TS_SD_EMBEDDEDHANDWRITINGVIEW_VISIBLE: UInt32 = 256
TS_SS_DISJOINTSEL: UInt32 = 1
TS_SS_REGIONS: UInt32 = 2
TS_SS_TRANSITORY: UInt32 = 4
TS_SS_NOHIDDENTEXT: UInt32 = 8
TS_SS_TKBAUTOCORRECTENABLE: UInt32 = 16
TS_SS_TKBPREDICTIONENABLE: UInt32 = 32
TS_SS_UWPCONTROL: UInt32 = 64
TS_IE_CORRECTION: UInt32 = 1
TS_IE_COMPOSITION: UInt32 = 2
TS_IAS_NOQUERY: UInt32 = 1
TS_IAS_QUERYONLY: UInt32 = 2
GXFPF_ROUND_NEAREST: UInt32 = 1
GXFPF_NEAREST: UInt32 = 2
TS_CHAR_EMBEDDED: UInt32 = 65532
TS_CHAR_REGION: UInt32 = 0
TS_CHAR_REPLACEMENT: UInt32 = 65533
TS_ATTR_FIND_BACKWARDS: UInt32 = 1
TS_ATTR_FIND_WANT_OFFSET: UInt32 = 2
TS_ATTR_FIND_UPDATESTART: UInt32 = 4
TS_ATTR_FIND_WANT_VALUE: UInt32 = 8
TS_ATTR_FIND_WANT_END: UInt32 = 16
TS_ATTR_FIND_HIDDEN: UInt32 = 32
TS_VCOOKIE_NUL: UInt32 = 4294967295
TS_SHIFT_COUNT_HIDDEN: UInt32 = 1
TS_SHIFT_HALT_HIDDEN: UInt32 = 2
TS_SHIFT_HALT_VISIBLE: UInt32 = 4
TS_SHIFT_COUNT_ONLY: UInt32 = 8
TS_GTA_HIDDEN: UInt32 = 1
TS_GEA_HIDDEN: UInt32 = 1
TF_E_LOCKED: win32more.Foundation.HRESULT = -2147220224
TF_E_STACKFULL: win32more.Foundation.HRESULT = -2147220223
TF_E_NOTOWNEDRANGE: win32more.Foundation.HRESULT = -2147220222
TF_E_NOPROVIDER: win32more.Foundation.HRESULT = -2147220221
TF_E_DISCONNECTED: win32more.Foundation.HRESULT = -2147220220
TF_E_INVALIDVIEW: win32more.Foundation.HRESULT = -2147220219
TF_E_ALREADY_EXISTS: win32more.Foundation.HRESULT = -2147220218
TF_E_RANGE_NOT_COVERED: win32more.Foundation.HRESULT = -2147220217
TF_E_COMPOSITION_REJECTED: win32more.Foundation.HRESULT = -2147220216
TF_E_EMPTYCONTEXT: win32more.Foundation.HRESULT = -2147220215
TF_E_INVALIDPOS: win32more.Foundation.HRESULT = -2147220992
TF_E_NOLOCK: win32more.Foundation.HRESULT = -2147220991
TF_E_NOOBJECT: win32more.Foundation.HRESULT = -2147220990
TF_E_NOSERVICE: win32more.Foundation.HRESULT = -2147220989
TF_E_NOINTERFACE: win32more.Foundation.HRESULT = -2147220988
TF_E_NOSELECTION: win32more.Foundation.HRESULT = -2147220987
TF_E_NOLAYOUT: win32more.Foundation.HRESULT = -2147220986
TF_E_INVALIDPOINT: win32more.Foundation.HRESULT = -2147220985
TF_E_SYNCHRONOUS: win32more.Foundation.HRESULT = -2147220984
TF_E_READONLY: win32more.Foundation.HRESULT = -2147220983
TF_E_FORMAT: win32more.Foundation.HRESULT = -2147220982
TF_S_ASYNC: win32more.Foundation.HRESULT = 262912
TF_RCM_COMLESS: UInt32 = 1
TF_RCM_VKEY: UInt32 = 2
TF_RCM_HINT_READING_LENGTH: UInt32 = 4
TF_RCM_HINT_COLLISION: UInt32 = 8
TKB_ALTERNATES_STANDARD: UInt32 = 1
TKB_ALTERNATES_FOR_AUTOCORRECTION: UInt32 = 2
TKB_ALTERNATES_FOR_PREDICTION: UInt32 = 3
TKB_ALTERNATES_AUTOCORRECTION_APPLIED: UInt32 = 4
TF_TMAE_NOACTIVATETIP: UInt32 = 1
TF_TMAE_SECUREMODE: UInt32 = 2
TF_TMAE_UIELEMENTENABLEDONLY: UInt32 = 4
TF_TMAE_COMLESS: UInt32 = 8
TF_TMAE_WOW16: UInt32 = 16
TF_TMAE_NOACTIVATEKEYBOARDLAYOUT: UInt32 = 32
TF_TMAE_CONSOLE: UInt32 = 64
TF_TMF_NOACTIVATETIP: UInt32 = 1
TF_TMF_SECUREMODE: UInt32 = 2
TF_TMF_UIELEMENTENABLEDONLY: UInt32 = 4
TF_TMF_COMLESS: UInt32 = 8
TF_TMF_WOW16: UInt32 = 16
TF_TMF_CONSOLE: UInt32 = 64
TF_TMF_IMMERSIVEMODE: UInt32 = 1073741824
TF_TMF_ACTIVATED: UInt32 = 2147483648
TF_MOD_ALT: UInt32 = 1
TF_MOD_CONTROL: UInt32 = 2
TF_MOD_SHIFT: UInt32 = 4
TF_MOD_RALT: UInt32 = 8
TF_MOD_RCONTROL: UInt32 = 16
TF_MOD_RSHIFT: UInt32 = 32
TF_MOD_LALT: UInt32 = 64
TF_MOD_LCONTROL: UInt32 = 128
TF_MOD_LSHIFT: UInt32 = 256
TF_MOD_ON_KEYUP: UInt32 = 512
TF_MOD_IGNORE_ALL_MODIFIER: UInt32 = 1024
TF_US_HIDETIPUI: UInt32 = 1
TF_DISABLE_SPEECH: UInt32 = 1
TF_DISABLE_DICTATION: UInt32 = 2
TF_DISABLE_COMMANDING: UInt32 = 4
TF_PROCESS_ATOM: String = '_CTF_PROCESS_ATOM_'
TF_ENABLE_PROCESS_ATOM: String = '_CTF_ENABLE_PROCESS_ATOM_'
TF_CLUIE_DOCUMENTMGR: UInt32 = 1
TF_CLUIE_COUNT: UInt32 = 2
TF_CLUIE_SELECTION: UInt32 = 4
TF_CLUIE_STRING: UInt32 = 8
TF_CLUIE_PAGEINDEX: UInt32 = 16
TF_CLUIE_CURRENTPAGE: UInt32 = 32
TF_RIUIE_CONTEXT: UInt32 = 1
TF_RIUIE_STRING: UInt32 = 2
TF_RIUIE_MAXREADINGSTRINGLENGTH: UInt32 = 4
TF_RIUIE_ERRORINDEX: UInt32 = 8
TF_RIUIE_VERTICALORDER: UInt32 = 16
TF_CONVERSIONMODE_ALPHANUMERIC: UInt32 = 0
TF_CONVERSIONMODE_NATIVE: UInt32 = 1
TF_CONVERSIONMODE_KATAKANA: UInt32 = 2
TF_CONVERSIONMODE_FULLSHAPE: UInt32 = 8
TF_CONVERSIONMODE_ROMAN: UInt32 = 16
TF_CONVERSIONMODE_CHARCODE: UInt32 = 32
TF_CONVERSIONMODE_SOFTKEYBOARD: UInt32 = 128
TF_CONVERSIONMODE_NOCONVERSION: UInt32 = 256
TF_CONVERSIONMODE_EUDC: UInt32 = 512
TF_CONVERSIONMODE_SYMBOL: UInt32 = 1024
TF_CONVERSIONMODE_FIXED: UInt32 = 2048
TF_SENTENCEMODE_NONE: UInt32 = 0
TF_SENTENCEMODE_PLAURALCLAUSE: UInt32 = 1
TF_SENTENCEMODE_SINGLECONVERT: UInt32 = 2
TF_SENTENCEMODE_AUTOMATIC: UInt32 = 4
TF_SENTENCEMODE_PHRASEPREDICT: UInt32 = 8
TF_SENTENCEMODE_CONVERSATION: UInt32 = 16
TF_TRANSITORYEXTENSION_NONE: UInt32 = 0
TF_TRANSITORYEXTENSION_FLOATING: UInt32 = 1
TF_TRANSITORYEXTENSION_ATSELECTION: UInt32 = 2
TF_PROFILETYPE_INPUTPROCESSOR: UInt32 = 1
TF_PROFILETYPE_KEYBOARDLAYOUT: UInt32 = 2
TF_RIP_FLAG_FREEUNUSEDLIBRARIES: UInt32 = 1
TF_IPP_FLAG_ACTIVE: UInt32 = 1
TF_IPP_FLAG_ENABLED: UInt32 = 2
TF_IPP_FLAG_SUBSTITUTEDBYINPUTPROCESSOR: UInt32 = 4
TF_IPP_CAPS_DISABLEONTRANSITORY: UInt32 = 1
TF_IPP_CAPS_SECUREMODESUPPORT: UInt32 = 2
TF_IPP_CAPS_UIELEMENTENABLED: UInt32 = 4
TF_IPP_CAPS_COMLESSSUPPORT: UInt32 = 8
TF_IPP_CAPS_WOW16SUPPORT: UInt32 = 16
TF_IPP_CAPS_IMMERSIVESUPPORT: UInt32 = 65536
TF_IPP_CAPS_SYSTRAYSUPPORT: UInt32 = 131072
TF_IPPMF_FORPROCESS: UInt32 = 268435456
TF_IPPMF_FORSESSION: UInt32 = 536870912
TF_IPPMF_FORSYSTEMALL: UInt32 = 1073741824
TF_IPPMF_ENABLEPROFILE: UInt32 = 1
TF_IPPMF_DISABLEPROFILE: UInt32 = 2
TF_IPPMF_DONTCARECURRENTINPUTLANGUAGE: UInt32 = 4
TF_RP_HIDDENINSETTINGUI: UInt32 = 2
TF_RP_LOCALPROCESS: UInt32 = 4
TF_RP_LOCALTHREAD: UInt32 = 8
TF_RP_SUBITEMINSETTINGUI: UInt32 = 16
TF_URP_ALLPROFILES: UInt32 = 2
TF_URP_LOCALPROCESS: UInt32 = 4
TF_URP_LOCALTHREAD: UInt32 = 8
TF_IPSINK_FLAG_ACTIVE: UInt32 = 1
TF_INVALID_EDIT_COOKIE: UInt32 = 0
TF_POPF_ALL: UInt32 = 1
TF_SD_READONLY: UInt32 = 1
TF_SD_LOADING: UInt32 = 2
TF_SS_DISJOINTSEL: UInt32 = 1
TF_SS_REGIONS: UInt32 = 2
TF_SS_TRANSITORY: UInt32 = 4
TF_SS_TKBAUTOCORRECTENABLE: UInt32 = 16
TF_SS_TKBPREDICTIONENABLE: UInt32 = 32
TF_CHAR_EMBEDDED: UInt32 = 65532
TF_HF_OBJECT: UInt32 = 1
TF_TF_MOVESTART: UInt32 = 1
TF_TF_IGNOREEND: UInt32 = 2
TF_ST_CORRECTION: UInt32 = 1
TF_IE_CORRECTION: UInt32 = 1
TF_TU_CORRECTION: UInt32 = 1
TF_INVALID_COOKIE: UInt32 = 4294967295
TF_PROFILE_NEWPHONETIC: Guid = Guid('b2f9c502-1742-11d4-97-90-00-80-c8-82-68-7e')
TF_PROFILE_PHONETIC: Guid = Guid('761309de-317a-11d4-9b-5d-00-80-c8-82-68-7e')
TF_PROFILE_NEWCHANGJIE: Guid = Guid('f3ba907a-6c7e-11d4-97-fa-00-80-c8-82-68-7e')
TF_PROFILE_CHANGJIE: Guid = Guid('4bdf9f03-c7d3-11d4-b2-ab-00-80-c8-82-68-7e')
TF_PROFILE_NEWQUICK: Guid = Guid('0b883ba0-c1c7-11d4-87-f9-00-80-c8-82-68-7e')
TF_PROFILE_QUICK: Guid = Guid('6024b45f-5c54-11d4-b9-21-00-80-c8-82-68-7e')
TF_PROFILE_CANTONESE: Guid = Guid('0aec109c-7e96-11d4-b2-ef-00-80-c8-82-68-7e')
TF_PROFILE_PINYIN: Guid = Guid('f3ba9077-6c7e-11d4-97-fa-00-80-c8-82-68-7e')
TF_PROFILE_SIMPLEFAST: Guid = Guid('fa550b04-5ad7-411f-a5-ac-ca-03-8e-c5-15-d7')
TF_PROFILE_WUBI: Guid = Guid('82590c13-f4dd-44f4-ba-1d-86-67-24-6f-df-8e')
TF_PROFILE_DAYI: Guid = Guid('037b2c25-480c-4d7f-b0-27-d6-ca-6b-69-78-8a')
TF_PROFILE_ARRAY: Guid = Guid('d38eff65-aa46-4fd5-91-a7-67-84-5f-b0-2f-5b')
TF_PROFILE_YI: Guid = Guid('409c8376-007b-4357-ae-8e-26-31-6e-e3-fb-0d')
TF_PROFILE_TIGRINYA: Guid = Guid('3cab88b7-cc3e-46a6-97-65-b7-72-ad-77-61-ff')
TF_E_NOCONVERSION: win32more.Foundation.HRESULT = -2147219968
TF_DICTATION_ON: UInt32 = 1
TF_DICTATION_ENABLED: UInt32 = 2
TF_COMMANDING_ENABLED: UInt32 = 4
TF_COMMANDING_ON: UInt32 = 8
TF_SPEECHUI_SHOWN: UInt32 = 16
TF_SHOW_BALLOON: UInt32 = 1
TF_DISABLE_BALLOON: UInt32 = 2
TF_MENUREADY: UInt32 = 1
TF_PROPUI_STATUS_SAVETOFILE: UInt32 = 1
GUID_INTEGRATIONSTYLE_SEARCHBOX: Guid = Guid('e6d1bd11-82f7-4903-ae-21-1a-63-97-cd-e2-eb')
TKBL_UNDEFINED: UInt32 = 0
TKBL_CLASSIC_TRADITIONAL_CHINESE_PHONETIC: UInt32 = 1028
TKBL_CLASSIC_TRADITIONAL_CHINESE_CHANGJIE: UInt32 = 61506
TKBL_CLASSIC_TRADITIONAL_CHINESE_DAYI: UInt32 = 61507
TKBL_OPT_JAPANESE_ABC: UInt32 = 1041
TKBL_OPT_KOREAN_HANGUL_2_BULSIK: UInt32 = 1042
TKBL_OPT_SIMPLIFIED_CHINESE_PINYIN: UInt32 = 2052
TKBL_OPT_TRADITIONAL_CHINESE_PHONETIC: UInt32 = 1028
TF_FLOATINGLANGBAR_WNDTITLEW: String = 'TF_FloatingLangBar_WndTitle'
TF_FLOATINGLANGBAR_WNDTITLEA: String = 'TF_FloatingLangBar_WndTitle'
TF_FLOATINGLANGBAR_WNDTITLE: String = 'TF_FloatingLangBar_WndTitle'
TF_LBI_ICON: UInt32 = 1
TF_LBI_TEXT: UInt32 = 2
TF_LBI_TOOLTIP: UInt32 = 4
TF_LBI_BITMAP: UInt32 = 8
TF_LBI_BALLOON: UInt32 = 16
TF_LBI_CUSTOMUI: UInt32 = 32
TF_LBI_STATUS: UInt32 = 65536
TF_LBI_STYLE_HIDDENSTATUSCONTROL: UInt32 = 1
TF_LBI_STYLE_SHOWNINTRAY: UInt32 = 2
TF_LBI_STYLE_HIDEONNOOTHERITEMS: UInt32 = 4
TF_LBI_STYLE_SHOWNINTRAYONLY: UInt32 = 8
TF_LBI_STYLE_HIDDENBYDEFAULT: UInt32 = 16
TF_LBI_STYLE_TEXTCOLORICON: UInt32 = 32
TF_LBI_STYLE_BTN_BUTTON: UInt32 = 65536
TF_LBI_STYLE_BTN_MENU: UInt32 = 131072
TF_LBI_STYLE_BTN_TOGGLE: UInt32 = 262144
TF_LBI_STATUS_HIDDEN: UInt32 = 1
TF_LBI_STATUS_DISABLED: UInt32 = 2
TF_LBI_STATUS_BTN_TOGGLED: UInt32 = 65536
TF_LBI_BMPF_VERTICAL: UInt32 = 1
TF_SFT_SHOWNORMAL: UInt32 = 1
TF_SFT_DOCK: UInt32 = 2
TF_SFT_MINIMIZED: UInt32 = 4
TF_SFT_HIDDEN: UInt32 = 8
TF_SFT_NOTRANSPARENCY: UInt32 = 16
TF_SFT_LOWTRANSPARENCY: UInt32 = 32
TF_SFT_HIGHTRANSPARENCY: UInt32 = 64
TF_SFT_LABELS: UInt32 = 128
TF_SFT_NOLABELS: UInt32 = 256
TF_SFT_EXTRAICONSONMINIMIZED: UInt32 = 512
TF_SFT_NOEXTRAICONSONMINIMIZED: UInt32 = 1024
TF_SFT_DESKBAND: UInt32 = 2048
TF_LBI_DESC_MAXLEN: UInt32 = 32
TF_LBMENUF_CHECKED: UInt32 = 1
TF_LBMENUF_SUBMENU: UInt32 = 2
TF_LBMENUF_SEPARATOR: UInt32 = 4
TF_LBMENUF_RADIOCHECKED: UInt32 = 8
TF_LBMENUF_GRAYED: UInt32 = 16
GUID_PROP_INPUTSCOPE: Guid = Guid('1713dd5a-68e7-4a5b-9a-f6-59-2a-59-5c-77-8d')
DCM_FLAGS_TASKENG: UInt32 = 1
DCM_FLAGS_CTFMON: UInt32 = 2
DCM_FLAGS_LOCALTHREADTSF: UInt32 = 4
ILMCM_CHECKLAYOUTANDTIPENABLED: UInt32 = 1
ILMCM_LANGUAGEBAROFF: UInt32 = 2
LIBID_MSAATEXTLib: Guid = Guid('150e2d7a-dac1-4582-94-7d-2a-8f-d7-8b-82-cd')
TS_STRF_START: UInt32 = 0
TS_STRF_MID: UInt32 = 1
TS_STRF_END: UInt32 = 2
TSATTRID_OTHERS: Guid = Guid('b3c32af9-57d0-46a9-bc-a8-da-c2-38-a1-30-57')
TSATTRID_Font: Guid = Guid('573ea825-749b-4f8a-9c-fd-21-c3-60-5c-a8-28')
TSATTRID_Font_FaceName: Guid = Guid('b536aeb6-053b-4eb8-b6-5a-50-da-1e-81-e7-2e')
TSATTRID_Font_SizePts: Guid = Guid('c8493302-a5e9-456d-af-04-80-05-e4-13-0f-03')
TSATTRID_Font_Style: Guid = Guid('68b2a77f-6b0e-4f28-81-77-57-1c-2f-3a-42-b1')
TSATTRID_Font_Style_Bold: Guid = Guid('48813a43-8a20-4940-8e-58-97-82-3f-7b-26-8a')
TSATTRID_Font_Style_Italic: Guid = Guid('8740682a-a765-48e1-ac-fc-d2-22-22-b2-f8-10')
TSATTRID_Font_Style_SmallCaps: Guid = Guid('facb6bc6-9100-4cc6-b9-69-11-ee-a4-5a-86-b4')
TSATTRID_Font_Style_Capitalize: Guid = Guid('7d85a3ba-b4fd-43b3-be-fc-6b-98-5c-84-31-41')
TSATTRID_Font_Style_Uppercase: Guid = Guid('33a300e8-e340-4937-b6-97-8f-23-40-45-cd-9a')
TSATTRID_Font_Style_Lowercase: Guid = Guid('76d8ccb5-ca7b-4498-8e-e9-d5-c4-f6-f7-4c-60')
TSATTRID_Font_Style_Animation: Guid = Guid('dcf73d22-e029-47b7-bb-36-f2-63-a3-d0-04-cc')
TSATTRID_Font_Style_Animation_LasVegasLights: Guid = Guid('f40423d5-0f87-4f8f-ba-da-e6-d6-0c-25-e1-52')
TSATTRID_Font_Style_Animation_BlinkingBackground: Guid = Guid('86e5b104-0104-4b10-b5-85-00-f2-52-75-22-b5')
TSATTRID_Font_Style_Animation_SparkleText: Guid = Guid('533aad20-962c-4e9f-8c-09-b4-2e-a4-74-97-11')
TSATTRID_Font_Style_Animation_MarchingBlackAnts: Guid = Guid('7644e067-f186-4902-bf-c6-ec-81-5a-a2-0e-9d')
TSATTRID_Font_Style_Animation_MarchingRedAnts: Guid = Guid('78368dad-50fb-4c6f-84-0b-d4-86-bb-6c-f7-81')
TSATTRID_Font_Style_Animation_Shimmer: Guid = Guid('2ce31b58-5293-4c36-88-09-bf-8b-b5-1a-27-b3')
TSATTRID_Font_Style_Animation_WipeDown: Guid = Guid('5872e874-367b-4803-b1-60-c9-0f-f6-25-69-d0')
TSATTRID_Font_Style_Animation_WipeRight: Guid = Guid('b855cbe3-3d2c-4600-b1-e9-e1-c9-ce-02-f8-42')
TSATTRID_Font_Style_Emboss: Guid = Guid('bd8ed742-349e-4e37-82-fb-43-79-79-cb-53-a7')
TSATTRID_Font_Style_Engrave: Guid = Guid('9c3371de-8332-4897-be-5d-89-23-32-23-17-9a')
TSATTRID_Font_Style_Hidden: Guid = Guid('b1e28770-881c-475f-86-3f-88-7a-64-7b-10-90')
TSATTRID_Font_Style_Kerning: Guid = Guid('cc26e1b4-2f9a-47c8-8b-ff-bf-1e-b7-cc-e0-dd')
TSATTRID_Font_Style_Outlined: Guid = Guid('10e6db31-db0d-4ac6-a7-f5-9c-9c-ff-6f-2a-b4')
TSATTRID_Font_Style_Position: Guid = Guid('15cd26ab-f2fb-4062-b5-a6-9a-49-e1-a5-cc-0b')
TSATTRID_Font_Style_Protected: Guid = Guid('1c557cb2-14cf-4554-a5-74-ec-b2-f7-e7-ef-d4')
TSATTRID_Font_Style_Shadow: Guid = Guid('5f686d2f-c6cd-4c56-8a-1a-99-4a-4b-97-66-be')
TSATTRID_Font_Style_Spacing: Guid = Guid('98c1200d-8f06-409a-8e-49-6a-55-4b-f7-c1-53')
TSATTRID_Font_Style_Weight: Guid = Guid('12f3189c-8bb0-461b-b1-fa-ea-f9-07-04-7f-e0')
TSATTRID_Font_Style_Height: Guid = Guid('7e937477-12e6-458b-92-6a-1f-a4-4e-e8-f3-91')
TSATTRID_Font_Style_Underline: Guid = Guid('c3c9c9f3-7902-444b-9a-7b-48-e7-0f-4b-50-f7')
TSATTRID_Font_Style_Underline_Single: Guid = Guid('1b6720e5-0f73-4951-a6-b3-6f-19-e4-3c-94-61')
TSATTRID_Font_Style_Underline_Double: Guid = Guid('74d24aa6-1db3-4c69-a1-76-31-12-0e-75-86-d5')
TSATTRID_Font_Style_Strikethrough: Guid = Guid('0c562193-2d08-4668-96-01-ce-d4-13-09-d7-af')
TSATTRID_Font_Style_Strikethrough_Single: Guid = Guid('75d736b6-3c8f-4b97-ab-78-18-77-cb-99-0d-31')
TSATTRID_Font_Style_Strikethrough_Double: Guid = Guid('62489b31-a3e7-4f94-ac-43-eb-af-8f-cc-7a-9f')
TSATTRID_Font_Style_Overline: Guid = Guid('e3989f4a-992b-4301-8c-e1-a5-b7-c6-d1-f3-c8')
TSATTRID_Font_Style_Overline_Single: Guid = Guid('8440d94c-51ce-47b2-8d-4c-15-75-1e-5f-72-1b')
TSATTRID_Font_Style_Overline_Double: Guid = Guid('dc46063a-e115-46e3-bc-d8-ca-67-72-aa-95-b4')
TSATTRID_Font_Style_Blink: Guid = Guid('bfb2c036-7acf-4532-b7-20-b4-16-dd-77-65-a8')
TSATTRID_Font_Style_Subscript: Guid = Guid('5774fb84-389b-43bc-a7-4b-15-68-34-7c-f0-f4')
TSATTRID_Font_Style_Superscript: Guid = Guid('2ea4993c-563c-49aa-93-72-0b-ef-09-a9-25-5b')
TSATTRID_Font_Style_Color: Guid = Guid('857a7a37-b8af-4e9a-81-b4-ac-f7-00-c8-41-1b')
TSATTRID_Font_Style_BackgroundColor: Guid = Guid('b50eaa4e-3091-4468-81-db-d7-9e-a1-90-c7-c7')
TSATTRID_Text: Guid = Guid('7edb8e68-81f9-449d-a1-5a-87-a8-38-8f-aa-c0')
TSATTRID_Text_VerticalWriting: Guid = Guid('6bba8195-046f-4ea9-b3-11-97-fd-66-c4-27-4b')
TSATTRID_Text_RightToLeft: Guid = Guid('ca666e71-1b08-453d-bf-dd-28-e0-8c-8a-af-7a')
TSATTRID_Text_Orientation: Guid = Guid('6bab707f-8785-4c39-8b-52-96-f8-78-30-3f-fb')
TSATTRID_Text_Language: Guid = Guid('d8c04ef1-5753-4c25-88-87-85-44-3f-e5-f8-19')
TSATTRID_Text_ReadOnly: Guid = Guid('85836617-de32-4afd-a5-0f-a2-db-11-0e-6e-4d')
TSATTRID_Text_EmbeddedObject: Guid = Guid('7edb8e68-81f9-449d-a1-5a-87-a8-38-8f-aa-c0')
TSATTRID_Text_Alignment: Guid = Guid('139941e6-1767-456d-93-8e-35-ba-56-8b-5c-d4')
TSATTRID_Text_Alignment_Left: Guid = Guid('16ae95d3-6361-43a2-84-95-d0-0f-39-7f-16-93')
TSATTRID_Text_Alignment_Right: Guid = Guid('b36f0f98-1b9e-4360-86-16-03-fb-08-a7-84-56')
TSATTRID_Text_Alignment_Center: Guid = Guid('a4a95c16-53bf-4d55-8b-87-4b-dd-8d-42-75-fc')
TSATTRID_Text_Alignment_Justify: Guid = Guid('ed350740-a0f7-42d3-8e-a8-f8-1b-64-88-fa-f0')
TSATTRID_Text_Link: Guid = Guid('47cd9051-3722-4cd8-b7-c8-4e-17-ca-17-59-f5')
TSATTRID_Text_Hyphenation: Guid = Guid('dadf4525-618e-49eb-b1-a8-3b-68-bd-76-48-e3')
TSATTRID_Text_Para: Guid = Guid('5edc5822-99dc-4dd6-ae-c3-b6-2b-aa-5b-2e-7c')
TSATTRID_Text_Para_FirstLineIndent: Guid = Guid('07c97a13-7472-4dd8-90-a9-91-e3-d7-e4-f2-9c')
TSATTRID_Text_Para_LeftIndent: Guid = Guid('fb2848e9-7471-41c9-b6-b3-8a-14-50-e0-18-97')
TSATTRID_Text_Para_RightIndent: Guid = Guid('2c7f26f9-a5e2-48da-b9-8a-52-0c-b1-65-13-bf')
TSATTRID_Text_Para_SpaceAfter: Guid = Guid('7b0a3f55-22dc-425f-a4-11-93-da-1d-8f-9b-aa')
TSATTRID_Text_Para_SpaceBefore: Guid = Guid('8df98589-194a-4601-b2-51-98-65-a3-e9-06-dd')
TSATTRID_Text_Para_LineSpacing: Guid = Guid('699b380d-7f8c-46d6-a7-3b-df-e3-d1-53-8d-f3')
TSATTRID_Text_Para_LineSpacing_Single: Guid = Guid('ed350740-a0f7-42d3-8e-a8-f8-1b-64-88-fa-f0')
TSATTRID_Text_Para_LineSpacing_OnePtFive: Guid = Guid('0428a021-0397-4b57-9a-17-07-95-99-4c-d3-c5')
TSATTRID_Text_Para_LineSpacing_Double: Guid = Guid('82fb1805-a6c4-4231-ac-12-62-60-af-2a-ba-28')
TSATTRID_Text_Para_LineSpacing_AtLeast: Guid = Guid('adfedf31-2d44-4434-a5-ff-7f-4c-49-90-a9-05')
TSATTRID_Text_Para_LineSpacing_Exactly: Guid = Guid('3d45ad40-23de-48d7-a6-b3-76-54-20-c6-20-cc')
TSATTRID_Text_Para_LineSpacing_Multiple: Guid = Guid('910f1e3c-d6d0-4f65-8a-3c-42-b4-b3-18-68-c5')
TSATTRID_List: Guid = Guid('436d673b-26f1-4aee-9e-65-8f-83-a4-ed-48-84')
TSATTRID_List_LevelIndel: Guid = Guid('7f7cc899-311f-487b-ad-5d-e2-a4-59-e1-2d-42')
TSATTRID_List_Type: Guid = Guid('ae3e665e-4bce-49e3-a0-fe-2d-b4-7d-3a-17-ae')
TSATTRID_List_Type_Bullet: Guid = Guid('bccd77c5-4c4d-4ce2-b1-02-55-9f-3b-2b-fc-ea')
TSATTRID_List_Type_Arabic: Guid = Guid('1338c5d6-98a3-4fa3-9b-d1-7a-60-ee-f8-e9-e0')
TSATTRID_List_Type_LowerLetter: Guid = Guid('96372285-f3cf-491e-a9-25-38-32-34-7f-d2-37')
TSATTRID_List_Type_UpperLetter: Guid = Guid('7987b7cd-ce52-428b-9b-95-a3-57-f6-f1-0c-45')
TSATTRID_List_Type_LowerRoman: Guid = Guid('90466262-3980-4b8e-93-68-91-8b-d1-21-8a-41')
TSATTRID_List_Type_UpperRoman: Guid = Guid('0f6ab552-4a80-467f-b2-f1-12-7e-2a-a3-ba-9e')
TSATTRID_App: Guid = Guid('a80f77df-4237-40e5-84-9c-b5-fa-51-c1-3a-c7')
TSATTRID_App_IncorrectSpelling: Guid = Guid('f42de43c-ef12-430d-94-4c-9a-08-97-0a-25-d2')
TSATTRID_App_IncorrectGrammar: Guid = Guid('bd54e398-ad03-4b74-b6-b3-5e-db-19-99-63-88')
@winfunctype('MsCtfMonitor.dll')
def DoMsCtfMonitor(dwFlags: UInt32, hEventForServiceStop: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('MsCtfMonitor.dll')
def InitLocalMsCtfMonitor(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('MsCtfMonitor.dll')
def UninitLocalMsCtfMonitor() -> win32more.Foundation.HRESULT: ...
DocWrap = Guid('bf426f7e-7a5e-44d6-83-0c-a3-90-ea-94-62-a3')
GET_TEXT_AND_PROPERTY_UPDATES_FLAGS = UInt32
TF_GTP_NONE: GET_TEXT_AND_PROPERTY_UPDATES_FLAGS = 0
TF_GTP_INCL_TEXT: GET_TEXT_AND_PROPERTY_UPDATES_FLAGS = 1
HKL = IntPtr
class IAccClientDocMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4c896039-7b6d-49e6-a8-c1-45-11-6a-98-29-2b')
    @commethod(3)
    def GetDocuments(enumUnknown: POINTER(win32more.System.Com.IEnumUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def LookupByHWND(hWnd: win32more.Foundation.HWND, riid: POINTER(Guid), ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def LookupByPoint(pt: win32more.Foundation.POINT, riid: POINTER(Guid), ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetFocused(riid: POINTER(Guid), ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IAccDictionary(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1dc4cb5f-d737-474d-ad-e9-5c-cf-c9-bc-1c-c9')
    @commethod(3)
    def GetLocalizedString(Term: POINTER(Guid), lcid: UInt32, pResult: POINTER(win32more.Foundation.BSTR), plcid: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetParentTerm(Term: POINTER(Guid), pParentTerm: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetMnemonicString(Term: POINTER(Guid), pResult: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def LookupMnemonicTerm(bstrMnemonic: win32more.Foundation.BSTR, pTerm: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ConvertValueToString(Term: POINTER(Guid), lcid: UInt32, varValue: win32more.System.Com.VARIANT, pbstrResult: POINTER(win32more.Foundation.BSTR), plcid: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IAccServerDocMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ad7c73cf-6dd5-4855-ab-c2-b0-4b-ad-5b-91-53')
    @commethod(3)
    def NewDocument(riid: POINTER(Guid), punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RevokeDocument(punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnDocumentFocus(punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class IAccStore(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e2cd4a63-2b72-4d48-b7-39-95-e4-76-51-95-ba')
    @commethod(3)
    def Register(riid: POINTER(Guid), punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Unregister(punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDocuments(enumUnknown: POINTER(win32more.System.Com.IEnumUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def LookupByHWND(hWnd: win32more.Foundation.HWND, riid: POINTER(Guid), ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def LookupByPoint(pt: win32more.Foundation.POINT, riid: POINTER(Guid), ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def OnDocumentFocus(punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetFocused(riid: POINTER(Guid), ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IAnchor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0feb7e34-5a60-4356-8e-f7-ab-de-c2-ff-7c-f8')
    @commethod(3)
    def SetGravity(gravity: win32more.UI.TextServices.TsGravity) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetGravity(pgravity: POINTER(win32more.UI.TextServices.TsGravity)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def IsEqual(paWith: win32more.UI.TextServices.IAnchor_head, pfEqual: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Compare(paWith: win32more.UI.TextServices.IAnchor_head, plResult: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Shift(dwFlags: UInt32, cchReq: Int32, pcch: POINTER(Int32), paHaltAnchor: win32more.UI.TextServices.IAnchor_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ShiftTo(paSite: win32more.UI.TextServices.IAnchor_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def ShiftRegion(dwFlags: UInt32, dir: win32more.UI.TextServices.TsShiftDir, pfNoRegion: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetChangeHistoryMask(dwMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetChangeHistory(pdwHistory: POINTER(win32more.UI.TextServices.ANCHOR_CHANGE_HISTORY_FLAGS)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def ClearChangeHistory() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Clone(ppaClone: POINTER(win32more.UI.TextServices.IAnchor_head)) -> win32more.Foundation.HRESULT: ...
class IClonableWrapper(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b33e75ff-e84c-4dca-a2-5c-33-b8-dc-00-33-74')
    @commethod(3)
    def CloneNewWrapper(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class ICoCreateLocally(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('03de00aa-f272-41e3-99-cb-03-c5-e8-11-4e-a0')
    @commethod(3)
    def CoCreateLocally(rclsid: POINTER(Guid), dwClsContext: UInt32, riid: POINTER(Guid), punk: POINTER(win32more.System.Com.IUnknown_head), riidParam: POINTER(Guid), punkParam: win32more.System.Com.IUnknown_head, varParam: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class ICoCreatedLocally(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0a53eb6c-1908-4742-8c-ff-2c-ee-2e-93-f9-4c')
    @commethod(3)
    def LocalInit(punkLocalObject: win32more.System.Com.IUnknown_head, riidParam: POINTER(Guid), punkParam: win32more.System.Com.IUnknown_head, varParam: win32more.System.Com.VARIANT) -> win32more.Foundation.HRESULT: ...
class IDocWrap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dcd285fe-0be0-43bd-99-c9-aa-ae-c5-13-c5-55')
    @commethod(3)
    def SetDoc(riid: POINTER(Guid), punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetWrappedDoc(riid: POINTER(Guid), ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IEnumITfCompositionView(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5efd22ba-7838-46cb-88-e2-ca-db-14-12-4f-8f')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumITfCompositionView_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, rgCompositionView: POINTER(win32more.UI.TextServices.ITfCompositionView_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumSpeechCommands(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8c5dac4f-083c-4b85-a4-c9-71-74-60-48-ad-ca')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumSpeechCommands_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, pSpCmds: POINTER(POINTER(UInt16)), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfCandidates(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('defb1926-6c80-4ce8-87-d4-d6-b7-2b-81-2b-de')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfCandidates_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, ppCand: POINTER(win32more.UI.TextServices.ITfCandidateString_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfContextViews(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f0c0f8dd-cf38-44e1-bb-0f-68-cf-0d-55-1c-78')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfContextViews_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, rgViews: POINTER(win32more.UI.TextServices.ITfContextView_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfContexts(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8f1a7ea6-1654-4502-a8-6e-b2-90-23-44-d5-07')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfContexts_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, rgContext: POINTER(win32more.UI.TextServices.ITfContext_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfDisplayAttributeInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7cef04d7-cb75-4e80-a7-ab-5f-5b-c7-d3-32-de')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfDisplayAttributeInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, rgInfo: POINTER(win32more.UI.TextServices.ITfDisplayAttributeInfo_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfDocumentMgrs(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aa80e808-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfDocumentMgrs_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, rgDocumentMgr: POINTER(win32more.UI.TextServices.ITfDocumentMgr_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfFunctionProviders(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e4b24db0-0990-11d3-8d-f0-00-10-5a-27-99-b5')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfFunctionProviders_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, ppCmdobj: POINTER(win32more.UI.TextServices.ITfFunctionProvider_head), pcFetch: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfInputProcessorProfiles(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('71c6e74d-0f28-11d8-a8-2a-00-06-5b-84-43-5c')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfInputProcessorProfiles_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, pProfile: POINTER(win32more.UI.TextServices.TF_INPUTPROCESSORPROFILE_head), pcFetch: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfLangBarItems(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('583f34d0-de25-11d2-af-dd-00-10-5a-27-99-b5')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfLangBarItems_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, ppItem: POINTER(win32more.UI.TextServices.ITfLangBarItem_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfLanguageProfiles(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3d61bf11-ac5f-42c8-a4-cb-93-1b-cc-28-c7-44')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfLanguageProfiles_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, pProfile: POINTER(win32more.UI.TextServices.TF_LANGUAGEPROFILE_head), pcFetch: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfLatticeElements(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('56988052-47da-4a05-91-1a-e3-d9-41-f1-71-45')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfLatticeElements_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, rgsElements: POINTER(win32more.UI.TextServices.TF_LMLATTELEMENT_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfProperties(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('19188cb0-aca9-11d2-af-c5-00-10-5a-27-99-b5')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfProperties_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, ppProp: POINTER(win32more.UI.TextServices.ITfProperty_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfPropertyValue(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8ed8981b-7c10-4d7d-9f-b3-ab-72-e9-c7-5f-72')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfPropertyValue_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, rgValues: POINTER(win32more.UI.TextServices.TF_PROPERTYVAL_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfRanges(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f99d3f40-8e32-11d2-bf-46-00-10-5a-27-99-b5')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfRanges_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, ppRange: POINTER(win32more.UI.TextServices.ITfRange_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IEnumTfUIElements(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('887aa91e-acba-4931-84-da-3c-52-08-cf-54-3f')
    @commethod(3)
    def Clone(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfUIElements_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, ppElement: POINTER(win32more.UI.TextServices.ITfUIElement_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IInternalDocWrap(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e1aa6466-9db4-40ba-be-03-77-c3-8e-8e-60-b2')
    @commethod(3)
    def NotifyRevoke() -> win32more.Foundation.HRESULT: ...
INSERT_TEXT_AT_SELECTION_FLAGS = UInt32
TF_IAS_NOQUERY: INSERT_TEXT_AT_SELECTION_FLAGS = 1
TF_IAS_QUERYONLY: INSERT_TEXT_AT_SELECTION_FLAGS = 2
TF_IAS_NO_DEFAULT_COMPOSITION: INSERT_TEXT_AT_SELECTION_FLAGS = 2147483648
class ISpeechCommandProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('38e09d4c-586d-435a-b5-92-c8-a8-66-91-de-c6')
    @commethod(3)
    def EnumSpeechCommands(langid: UInt16, ppEnum: POINTER(win32more.UI.TextServices.IEnumSpeechCommands_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ProcessCommand(pszCommand: win32more.Foundation.PWSTR, cch: UInt32, langid: UInt16) -> win32more.Foundation.HRESULT: ...
class ITextStoreACP(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('28888fe3-c2a0-483a-a3-ea-8c-b1-ce-51-ff-3d')
    @commethod(3)
    def AdviseSink(riid: POINTER(Guid), punk: win32more.System.Com.IUnknown_head, dwMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseSink(punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RequestLock(dwLockFlags: UInt32, phrSession: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(pdcs: POINTER(win32more.UI.TextServices.TS_STATUS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def QueryInsert(acpTestStart: Int32, acpTestEnd: Int32, cch: UInt32, pacpResultStart: POINTER(Int32), pacpResultEnd: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSelection(ulIndex: UInt32, ulCount: UInt32, pSelection: POINTER(win32more.UI.TextServices.TS_SELECTION_ACP_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetSelection(ulCount: UInt32, pSelection: POINTER(win32more.UI.TextServices.TS_SELECTION_ACP_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetText(acpStart: Int32, acpEnd: Int32, pchPlain: win32more.Foundation.PWSTR, cchPlainReq: UInt32, pcchPlainRet: POINTER(UInt32), prgRunInfo: POINTER(win32more.UI.TextServices.TS_RUNINFO_head), cRunInfoReq: UInt32, pcRunInfoRet: POINTER(UInt32), pacpNext: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetText(dwFlags: UInt32, acpStart: Int32, acpEnd: Int32, pchText: win32more.Foundation.PWSTR, cch: UInt32, pChange: POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetFormattedText(acpStart: Int32, acpEnd: Int32, ppDataObject: POINTER(win32more.System.Com.IDataObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetEmbedded(acpPos: Int32, rguidService: POINTER(Guid), riid: POINTER(Guid), ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def QueryInsertEmbedded(pguidService: POINTER(Guid), pFormatEtc: POINTER(win32more.System.Com.FORMATETC_head), pfInsertable: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def InsertEmbedded(dwFlags: UInt32, acpStart: Int32, acpEnd: Int32, pDataObject: win32more.System.Com.IDataObject_head, pChange: POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def InsertTextAtSelection(dwFlags: UInt32, pchText: win32more.Foundation.PWSTR, cch: UInt32, pacpStart: POINTER(Int32), pacpEnd: POINTER(Int32), pChange: POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def InsertEmbeddedAtSelection(dwFlags: UInt32, pDataObject: win32more.System.Com.IDataObject_head, pacpStart: POINTER(Int32), pacpEnd: POINTER(Int32), pChange: POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def RequestSupportedAttrs(dwFlags: UInt32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def RequestAttrsAtPosition(acpPos: Int32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def RequestAttrsTransitioningAtPosition(acpPos: Int32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def FindNextAttrTransition(acpStart: Int32, acpHalt: Int32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32, pacpNext: POINTER(Int32), pfFound: POINTER(win32more.Foundation.BOOL), plFoundOffset: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def RetrieveRequestedAttrs(ulCount: UInt32, paAttrVals: POINTER(win32more.UI.TextServices.TS_ATTRVAL_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetEndACP(pacp: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetActiveView(pvcView: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetACPFromPoint(vcView: UInt32, ptScreen: POINTER(win32more.Foundation.POINT_head), dwFlags: UInt32, pacp: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetTextExt(vcView: UInt32, acpStart: Int32, acpEnd: Int32, prc: POINTER(win32more.Foundation.RECT_head), pfClipped: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def GetScreenExt(vcView: UInt32, prc: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetWnd(vcView: UInt32, phwnd: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
class ITextStoreACP2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f86ad89f-5fe4-4b8d-bb-9f-ef-37-97-a8-4f-1f')
    @commethod(3)
    def AdviseSink(riid: POINTER(Guid), punk: win32more.System.Com.IUnknown_head, dwMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseSink(punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RequestLock(dwLockFlags: UInt32, phrSession: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(pdcs: POINTER(win32more.UI.TextServices.TS_STATUS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def QueryInsert(acpTestStart: Int32, acpTestEnd: Int32, cch: UInt32, pacpResultStart: POINTER(Int32), pacpResultEnd: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSelection(ulIndex: UInt32, ulCount: UInt32, pSelection: POINTER(win32more.UI.TextServices.TS_SELECTION_ACP_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetSelection(ulCount: UInt32, pSelection: POINTER(win32more.UI.TextServices.TS_SELECTION_ACP_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetText(acpStart: Int32, acpEnd: Int32, pchPlain: win32more.Foundation.PWSTR, cchPlainReq: UInt32, pcchPlainRet: POINTER(UInt32), prgRunInfo: POINTER(win32more.UI.TextServices.TS_RUNINFO_head), cRunInfoReq: UInt32, pcRunInfoRet: POINTER(UInt32), pacpNext: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetText(dwFlags: UInt32, acpStart: Int32, acpEnd: Int32, pchText: win32more.Foundation.PWSTR, cch: UInt32, pChange: POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetFormattedText(acpStart: Int32, acpEnd: Int32, ppDataObject: POINTER(win32more.System.Com.IDataObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetEmbedded(acpPos: Int32, rguidService: POINTER(Guid), riid: POINTER(Guid), ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def QueryInsertEmbedded(pguidService: POINTER(Guid), pFormatEtc: POINTER(win32more.System.Com.FORMATETC_head), pfInsertable: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def InsertEmbedded(dwFlags: UInt32, acpStart: Int32, acpEnd: Int32, pDataObject: win32more.System.Com.IDataObject_head, pChange: POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def InsertTextAtSelection(dwFlags: UInt32, pchText: win32more.Foundation.PWSTR, cch: UInt32, pacpStart: POINTER(Int32), pacpEnd: POINTER(Int32), pChange: POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def InsertEmbeddedAtSelection(dwFlags: UInt32, pDataObject: win32more.System.Com.IDataObject_head, pacpStart: POINTER(Int32), pacpEnd: POINTER(Int32), pChange: POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def RequestSupportedAttrs(dwFlags: UInt32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def RequestAttrsAtPosition(acpPos: Int32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def RequestAttrsTransitioningAtPosition(acpPos: Int32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def FindNextAttrTransition(acpStart: Int32, acpHalt: Int32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32, pacpNext: POINTER(Int32), pfFound: POINTER(win32more.Foundation.BOOL), plFoundOffset: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def RetrieveRequestedAttrs(ulCount: UInt32, paAttrVals: POINTER(win32more.UI.TextServices.TS_ATTRVAL_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetEndACP(pacp: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetActiveView(pvcView: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetACPFromPoint(vcView: UInt32, ptScreen: POINTER(win32more.Foundation.POINT_head), dwFlags: UInt32, pacp: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetTextExt(vcView: UInt32, acpStart: Int32, acpEnd: Int32, prc: POINTER(win32more.Foundation.RECT_head), pfClipped: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def GetScreenExt(vcView: UInt32, prc: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
class ITextStoreACPEx(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a2de3bc2-3d8e-11d3-81-a9-f7-53-fb-e6-1a-00')
    @commethod(3)
    def ScrollToRect(acpStart: Int32, acpEnd: Int32, rc: win32more.Foundation.RECT, dwPosition: UInt32) -> win32more.Foundation.HRESULT: ...
class ITextStoreACPServices(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aa80e901-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    @commethod(3)
    def Serialize(pProp: win32more.UI.TextServices.ITfProperty_head, pRange: win32more.UI.TextServices.ITfRange_head, pHdr: POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head), pStream: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Unserialize(pProp: win32more.UI.TextServices.ITfProperty_head, pHdr: POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head), pStream: win32more.System.Com.IStream_head, pLoader: win32more.UI.TextServices.ITfPersistentPropertyLoaderACP_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ForceLoadProperty(pProp: win32more.UI.TextServices.ITfProperty_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CreateRange(acpStart: Int32, acpEnd: Int32, ppRange: POINTER(win32more.UI.TextServices.ITfRangeACP_head)) -> win32more.Foundation.HRESULT: ...
class ITextStoreACPSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('22d44c94-a419-4542-a2-72-ae-26-09-3e-ce-cf')
    @commethod(3)
    def OnTextChange(dwFlags: win32more.UI.TextServices.TEXT_STORE_TEXT_CHANGE_FLAGS, pChange: POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnSelectionChange() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnLayoutChange(lcode: win32more.UI.TextServices.TsLayoutCode, vcView: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnStatusChange(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnAttrsChange(acpStart: Int32, acpEnd: Int32, cAttrs: UInt32, paAttrs: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def OnLockGranted(dwLockFlags: win32more.UI.TextServices.TEXT_STORE_LOCK_FLAGS) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def OnStartEditTransaction() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def OnEndEditTransaction() -> win32more.Foundation.HRESULT: ...
class ITextStoreACPSinkEx(c_void_p):
    extends: win32more.UI.TextServices.ITextStoreACPSink
    Guid = Guid('2bdf9464-41e2-43e3-95-0c-a6-86-5b-a2-5c-d4')
    @commethod(11)
    def OnDisconnect() -> win32more.Foundation.HRESULT: ...
class ITextStoreAnchor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9b2077b0-5f18-4dec-be-e9-3c-c7-22-f5-df-e0')
    @commethod(3)
    def AdviseSink(riid: POINTER(Guid), punk: win32more.System.Com.IUnknown_head, dwMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseSink(punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RequestLock(dwLockFlags: UInt32, phrSession: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(pdcs: POINTER(win32more.UI.TextServices.TS_STATUS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def QueryInsert(paTestStart: win32more.UI.TextServices.IAnchor_head, paTestEnd: win32more.UI.TextServices.IAnchor_head, cch: UInt32, ppaResultStart: POINTER(win32more.UI.TextServices.IAnchor_head), ppaResultEnd: POINTER(win32more.UI.TextServices.IAnchor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSelection(ulIndex: UInt32, ulCount: UInt32, pSelection: POINTER(win32more.UI.TextServices.TS_SELECTION_ANCHOR_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetSelection(ulCount: UInt32, pSelection: POINTER(win32more.UI.TextServices.TS_SELECTION_ANCHOR_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetText(dwFlags: UInt32, paStart: win32more.UI.TextServices.IAnchor_head, paEnd: win32more.UI.TextServices.IAnchor_head, pchText: win32more.Foundation.PWSTR, cchReq: UInt32, pcch: POINTER(UInt32), fUpdateAnchor: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetText(dwFlags: UInt32, paStart: win32more.UI.TextServices.IAnchor_head, paEnd: win32more.UI.TextServices.IAnchor_head, pchText: win32more.Foundation.PWSTR, cch: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetFormattedText(paStart: win32more.UI.TextServices.IAnchor_head, paEnd: win32more.UI.TextServices.IAnchor_head, ppDataObject: POINTER(win32more.System.Com.IDataObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetEmbedded(dwFlags: UInt32, paPos: win32more.UI.TextServices.IAnchor_head, rguidService: POINTER(Guid), riid: POINTER(Guid), ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def InsertEmbedded(dwFlags: UInt32, paStart: win32more.UI.TextServices.IAnchor_head, paEnd: win32more.UI.TextServices.IAnchor_head, pDataObject: win32more.System.Com.IDataObject_head) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def RequestSupportedAttrs(dwFlags: UInt32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def RequestAttrsAtPosition(paPos: win32more.UI.TextServices.IAnchor_head, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def RequestAttrsTransitioningAtPosition(paPos: win32more.UI.TextServices.IAnchor_head, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def FindNextAttrTransition(paStart: win32more.UI.TextServices.IAnchor_head, paHalt: win32more.UI.TextServices.IAnchor_head, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32, pfFound: POINTER(win32more.Foundation.BOOL), plFoundOffset: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def RetrieveRequestedAttrs(ulCount: UInt32, paAttrVals: POINTER(win32more.UI.TextServices.TS_ATTRVAL_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetStart(ppaStart: POINTER(win32more.UI.TextServices.IAnchor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetEnd(ppaEnd: POINTER(win32more.UI.TextServices.IAnchor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetActiveView(pvcView: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetAnchorFromPoint(vcView: UInt32, ptScreen: POINTER(win32more.Foundation.POINT_head), dwFlags: UInt32, ppaSite: POINTER(win32more.UI.TextServices.IAnchor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetTextExt(vcView: UInt32, paStart: win32more.UI.TextServices.IAnchor_head, paEnd: win32more.UI.TextServices.IAnchor_head, prc: POINTER(win32more.Foundation.RECT_head), pfClipped: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetScreenExt(vcView: UInt32, prc: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetWnd(vcView: UInt32, phwnd: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def QueryInsertEmbedded(pguidService: POINTER(Guid), pFormatEtc: POINTER(win32more.System.Com.FORMATETC_head), pfInsertable: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def InsertTextAtSelection(dwFlags: UInt32, pchText: win32more.Foundation.PWSTR, cch: UInt32, ppaStart: POINTER(win32more.UI.TextServices.IAnchor_head), ppaEnd: POINTER(win32more.UI.TextServices.IAnchor_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def InsertEmbeddedAtSelection(dwFlags: UInt32, pDataObject: win32more.System.Com.IDataObject_head, ppaStart: POINTER(win32more.UI.TextServices.IAnchor_head), ppaEnd: POINTER(win32more.UI.TextServices.IAnchor_head)) -> win32more.Foundation.HRESULT: ...
class ITextStoreAnchorEx(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a2de3bc1-3d8e-11d3-81-a9-f7-53-fb-e6-1a-00')
    @commethod(3)
    def ScrollToRect(pStart: win32more.UI.TextServices.IAnchor_head, pEnd: win32more.UI.TextServices.IAnchor_head, rc: win32more.Foundation.RECT, dwPosition: UInt32) -> win32more.Foundation.HRESULT: ...
class ITextStoreAnchorSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aa80e905-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    @commethod(3)
    def OnTextChange(dwFlags: win32more.UI.TextServices.TEXT_STORE_CHANGE_FLAGS, paStart: win32more.UI.TextServices.IAnchor_head, paEnd: win32more.UI.TextServices.IAnchor_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnSelectionChange() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnLayoutChange(lcode: win32more.UI.TextServices.TsLayoutCode, vcView: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnStatusChange(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnAttrsChange(paStart: win32more.UI.TextServices.IAnchor_head, paEnd: win32more.UI.TextServices.IAnchor_head, cAttrs: UInt32, paAttrs: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def OnLockGranted(dwLockFlags: win32more.UI.TextServices.TEXT_STORE_LOCK_FLAGS) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def OnStartEditTransaction() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def OnEndEditTransaction() -> win32more.Foundation.HRESULT: ...
class ITextStoreSinkAnchorEx(c_void_p):
    extends: win32more.UI.TextServices.ITextStoreAnchorSink
    Guid = Guid('25642426-028d-4474-97-7b-11-1b-b1-14-fe-3e')
    @commethod(11)
    def OnDisconnect() -> win32more.Foundation.HRESULT: ...
class ITfActiveLanguageProfileNotifySink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b246cb75-a93e-4652-bf-8c-b3-fe-0c-fd-7e-57')
    @commethod(3)
    def OnActivated(clsid: POINTER(Guid), guidProfile: POINTER(Guid), fActivated: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class ITfCandidateList(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a3ad50fb-9bdb-49e3-a8-43-6c-76-52-0f-bf-5d')
    @commethod(3)
    def EnumCandidates(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfCandidates_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCandidate(nIndex: UInt32, ppCand: POINTER(win32more.UI.TextServices.ITfCandidateString_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCandidateNum(pnCnt: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetResult(nIndex: UInt32, imcr: win32more.UI.TextServices.TfCandidateResult) -> win32more.Foundation.HRESULT: ...
class ITfCandidateListUIElement(c_void_p):
    extends: win32more.UI.TextServices.ITfUIElement
    Guid = Guid('ea1ea138-19df-11d7-a6-d2-00-06-5b-84-43-5c')
    @commethod(7)
    def GetUpdatedFlags(pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetDocumentMgr(ppdim: POINTER(win32more.UI.TextServices.ITfDocumentMgr_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCount(puCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetSelection(puIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetString(uIndex: UInt32, pstr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetPageIndex(pIndex: POINTER(UInt32), uSize: UInt32, puPageCnt: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetPageIndex(pIndex: POINTER(UInt32), uPageCnt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetCurrentPage(puPage: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITfCandidateListUIElementBehavior(c_void_p):
    extends: win32more.UI.TextServices.ITfCandidateListUIElement
    Guid = Guid('85fad185-58ce-497a-94-60-35-53-66-b6-4b-9a')
    @commethod(15)
    def SetSelection(nIndex: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Finalize() -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Abort() -> win32more.Foundation.HRESULT: ...
class ITfCandidateString(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('581f317e-fd9d-443f-b9-72-ed-00-46-7c-5d-40')
    @commethod(3)
    def GetString(pbstr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetIndex(pnIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITfCategoryMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c3acefb5-f69d-4905-93-8f-fc-ad-cf-4b-e8-30')
    @commethod(3)
    def RegisterCategory(rclsid: POINTER(Guid), rcatid: POINTER(Guid), rguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterCategory(rclsid: POINTER(Guid), rcatid: POINTER(Guid), rguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumCategoriesInItem(rguid: POINTER(Guid), ppEnum: POINTER(win32more.System.Com.IEnumGUID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EnumItemsInCategory(rcatid: POINTER(Guid), ppEnum: POINTER(win32more.System.Com.IEnumGUID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def FindClosestCategory(rguid: POINTER(Guid), pcatid: POINTER(Guid), ppcatidList: POINTER(POINTER(Guid)), ulCount: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterGUIDDescription(rclsid: POINTER(Guid), rguid: POINTER(Guid), pchDesc: win32more.Foundation.PWSTR, cch: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def UnregisterGUIDDescription(rclsid: POINTER(Guid), rguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetGUIDDescription(rguid: POINTER(Guid), pbstrDesc: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def RegisterGUIDDWORD(rclsid: POINTER(Guid), rguid: POINTER(Guid), dw: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def UnregisterGUIDDWORD(rclsid: POINTER(Guid), rguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetGUIDDWORD(rguid: POINTER(Guid), pdw: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def RegisterGUID(rguid: POINTER(Guid), pguidatom: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetGUID(guidatom: UInt32, pguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def IsEqualTfGuidAtom(guidatom: UInt32, rguid: POINTER(Guid), pfEqual: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITfCleanupContextDurationSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('45c35144-154e-4797-be-d8-d3-3a-e7-bf-87-94')
    @commethod(3)
    def OnStartCleanupContext() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnEndCleanupContext() -> win32more.Foundation.HRESULT: ...
class ITfCleanupContextSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('01689689-7acb-4e9b-ab-7c-7e-a4-6b-12-b5-22')
    @commethod(3)
    def OnCleanupContext(ecWrite: UInt32, pic: win32more.UI.TextServices.ITfContext_head) -> win32more.Foundation.HRESULT: ...
class ITfClientId(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d60a7b49-1b9f-4be2-b7-02-47-e9-dc-05-de-c3')
    @commethod(3)
    def GetClientId(rclsid: POINTER(Guid), ptid: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITfCompartment(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bb08f7a9-607a-4384-86-23-05-68-92-b6-43-71')
    @commethod(3)
    def SetValue(tid: UInt32, pvarValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(pvarValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class ITfCompartmentEventSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('743abd5f-f26d-48df-8c-c5-23-84-92-41-9b-64')
    @commethod(3)
    def OnChange(rguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class ITfCompartmentMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7dcf57ac-18ad-438b-82-4d-97-9b-ff-b7-4b-7c')
    @commethod(3)
    def GetCompartment(rguid: POINTER(Guid), ppcomp: POINTER(win32more.UI.TextServices.ITfCompartment_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ClearCompartment(tid: UInt32, rguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumCompartments(ppEnum: POINTER(win32more.System.Com.IEnumGUID_head)) -> win32more.Foundation.HRESULT: ...
class ITfComposition(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('20168d64-5a8f-4a5a-b7-bd-cf-a2-9f-4d-0f-d9')
    @commethod(3)
    def GetRange(ppRange: POINTER(win32more.UI.TextServices.ITfRange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ShiftStart(ecWrite: UInt32, pNewStart: win32more.UI.TextServices.ITfRange_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ShiftEnd(ecWrite: UInt32, pNewEnd: win32more.UI.TextServices.ITfRange_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EndComposition(ecWrite: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfCompositionSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a781718c-579a-4b15-a2-80-32-b8-57-7a-cc-5e')
    @commethod(3)
    def OnCompositionTerminated(ecWrite: UInt32, pComposition: win32more.UI.TextServices.ITfComposition_head) -> win32more.Foundation.HRESULT: ...
class ITfCompositionView(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d7540241-f9a1-4364-be-fc-db-cd-2c-43-95-b7')
    @commethod(3)
    def GetOwnerClsid(pclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetRange(ppRange: POINTER(win32more.UI.TextServices.ITfRange_head)) -> win32more.Foundation.HRESULT: ...
class ITfConfigureSystemKeystrokeFeed(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0d2c969a-bc9c-437c-84-ee-95-1c-49-b1-a7-64')
    @commethod(3)
    def DisableSystemKeystrokeFeed() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def EnableSystemKeystrokeFeed() -> win32more.Foundation.HRESULT: ...
class ITfContext(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aa80e7fd-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    @commethod(3)
    def RequestEditSession(tid: UInt32, pes: win32more.UI.TextServices.ITfEditSession_head, dwFlags: win32more.UI.TextServices.TF_CONTEXT_EDIT_CONTEXT_FLAGS, phrSession: POINTER(win32more.Foundation.HRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def InWriteSession(tid: UInt32, pfWriteSession: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetSelection(ec: UInt32, ulIndex: UInt32, ulCount: UInt32, pSelection: POINTER(win32more.UI.TextServices.TF_SELECTION_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetSelection(ec: UInt32, ulCount: UInt32, pSelection: POINTER(win32more.UI.TextServices.TF_SELECTION_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetStart(ec: UInt32, ppStart: POINTER(win32more.UI.TextServices.ITfRange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetEnd(ec: UInt32, ppEnd: POINTER(win32more.UI.TextServices.ITfRange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetActiveView(ppView: POINTER(win32more.UI.TextServices.ITfContextView_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def EnumViews(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfContextViews_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetStatus(pdcs: POINTER(win32more.UI.TextServices.TS_STATUS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetProperty(guidProp: POINTER(Guid), ppProp: POINTER(win32more.UI.TextServices.ITfProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetAppProperty(guidProp: POINTER(Guid), ppProp: POINTER(win32more.UI.TextServices.ITfReadOnlyProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def TrackProperties(prgProp: POINTER(POINTER(Guid)), cProp: UInt32, prgAppProp: POINTER(POINTER(Guid)), cAppProp: UInt32, ppProperty: POINTER(win32more.UI.TextServices.ITfReadOnlyProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def EnumProperties(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfProperties_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetDocumentMgr(ppDm: POINTER(win32more.UI.TextServices.ITfDocumentMgr_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def CreateRangeBackup(ec: UInt32, pRange: win32more.UI.TextServices.ITfRange_head, ppBackup: POINTER(win32more.UI.TextServices.ITfRangeBackup_head)) -> win32more.Foundation.HRESULT: ...
class ITfContextComposition(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d40c8aae-ac92-4fc7-9a-11-0e-e0-e2-3a-a3-9b')
    @commethod(3)
    def StartComposition(ecWrite: UInt32, pCompositionRange: win32more.UI.TextServices.ITfRange_head, pSink: win32more.UI.TextServices.ITfCompositionSink_head, ppComposition: POINTER(win32more.UI.TextServices.ITfComposition_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def EnumCompositions(ppEnum: POINTER(win32more.UI.TextServices.IEnumITfCompositionView_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def FindComposition(ecRead: UInt32, pTestRange: win32more.UI.TextServices.ITfRange_head, ppEnum: POINTER(win32more.UI.TextServices.IEnumITfCompositionView_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def TakeOwnership(ecWrite: UInt32, pComposition: win32more.UI.TextServices.ITfCompositionView_head, pSink: win32more.UI.TextServices.ITfCompositionSink_head, ppComposition: POINTER(win32more.UI.TextServices.ITfComposition_head)) -> win32more.Foundation.HRESULT: ...
class ITfContextKeyEventSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0552ba5d-c835-4934-bf-50-84-6a-aa-67-43-2f')
    @commethod(3)
    def OnKeyDown(wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnKeyUp(wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnTestKeyDown(wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnTestKeyUp(wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITfContextOwner(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aa80e80c-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    @commethod(3)
    def GetACPFromPoint(ptScreen: POINTER(win32more.Foundation.POINT_head), dwFlags: UInt32, pacp: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTextExt(acpStart: Int32, acpEnd: Int32, prc: POINTER(win32more.Foundation.RECT_head), pfClipped: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetScreenExt(prc: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(pdcs: POINTER(win32more.UI.TextServices.TS_STATUS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetWnd(phwnd: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetAttribute(rguidAttribute: POINTER(Guid), pvarValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class ITfContextOwnerCompositionServices(c_void_p):
    extends: win32more.UI.TextServices.ITfContextComposition
    Guid = Guid('86462810-593b-4916-97-64-19-c0-8e-9c-e1-10')
    @commethod(7)
    def TerminateComposition(pComposition: win32more.UI.TextServices.ITfCompositionView_head) -> win32more.Foundation.HRESULT: ...
class ITfContextOwnerCompositionSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5f20aa40-b57a-4f34-96-ab-35-76-f3-77-cc-79')
    @commethod(3)
    def OnStartComposition(pComposition: win32more.UI.TextServices.ITfCompositionView_head, pfOk: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnUpdateComposition(pComposition: win32more.UI.TextServices.ITfCompositionView_head, pRangeNew: win32more.UI.TextServices.ITfRange_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnEndComposition(pComposition: win32more.UI.TextServices.ITfCompositionView_head) -> win32more.Foundation.HRESULT: ...
class ITfContextOwnerServices(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b23eb630-3e1c-11d3-a7-45-00-50-04-0a-b4-07')
    @commethod(3)
    def OnLayoutChange() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnStatusChange(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnAttributeChange(rguidAttribute: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Serialize(pProp: win32more.UI.TextServices.ITfProperty_head, pRange: win32more.UI.TextServices.ITfRange_head, pHdr: POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head), pStream: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Unserialize(pProp: win32more.UI.TextServices.ITfProperty_head, pHdr: POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head), pStream: win32more.System.Com.IStream_head, pLoader: win32more.UI.TextServices.ITfPersistentPropertyLoaderACP_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ForceLoadProperty(pProp: win32more.UI.TextServices.ITfProperty_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CreateRange(acpStart: Int32, acpEnd: Int32, ppRange: POINTER(win32more.UI.TextServices.ITfRangeACP_head)) -> win32more.Foundation.HRESULT: ...
class ITfContextView(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2433bf8e-0f9b-435c-ba-2c-18-06-11-97-8c-30')
    @commethod(3)
    def GetRangeFromPoint(ec: UInt32, ppt: POINTER(win32more.Foundation.POINT_head), dwFlags: UInt32, ppRange: POINTER(win32more.UI.TextServices.ITfRange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTextExt(ec: UInt32, pRange: win32more.UI.TextServices.ITfRange_head, prc: POINTER(win32more.Foundation.RECT_head), pfClipped: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetScreenExt(prc: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetWnd(phwnd: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
class ITfCreatePropertyStore(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2463fbf0-b0af-11d2-af-c5-00-10-5a-27-99-b5')
    @commethod(3)
    def IsStoreSerializable(guidProp: POINTER(Guid), pRange: win32more.UI.TextServices.ITfRange_head, pPropStore: win32more.UI.TextServices.ITfPropertyStore_head, pfSerializable: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePropertyStore(guidProp: POINTER(Guid), pRange: win32more.UI.TextServices.ITfRange_head, cb: UInt32, pStream: win32more.System.Com.IStream_head, ppStore: POINTER(win32more.UI.TextServices.ITfPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
class ITfDisplayAttributeInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('70528852-2f26-4aea-8c-96-21-51-50-57-89-32')
    @commethod(3)
    def GetGUID(pguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(pbstrDesc: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttributeInfo(pda: POINTER(win32more.UI.TextServices.TF_DISPLAYATTRIBUTE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetAttributeInfo(pda: POINTER(win32more.UI.TextServices.TF_DISPLAYATTRIBUTE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Reset() -> win32more.Foundation.HRESULT: ...
class ITfDisplayAttributeMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8ded7393-5db1-475c-9e-71-a3-91-11-b0-ff-67')
    @commethod(3)
    def OnUpdateInfo() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def EnumDisplayAttributeInfo(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfDisplayAttributeInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDisplayAttributeInfo(guid: POINTER(Guid), ppInfo: POINTER(win32more.UI.TextServices.ITfDisplayAttributeInfo_head), pclsidOwner: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class ITfDisplayAttributeNotifySink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ad56f402-e162-4f25-90-8f-7d-57-7c-f9-bd-a9')
    @commethod(3)
    def OnUpdateInfo() -> win32more.Foundation.HRESULT: ...
class ITfDisplayAttributeProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fee47777-163c-4769-99-6a-6e-9c-50-ad-8f-54')
    @commethod(3)
    def EnumDisplayAttributeInfo(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfDisplayAttributeInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDisplayAttributeInfo(guid: POINTER(Guid), ppInfo: POINTER(win32more.UI.TextServices.ITfDisplayAttributeInfo_head)) -> win32more.Foundation.HRESULT: ...
class ITfDocumentMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aa80e7f4-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    @commethod(3)
    def CreateContext(tidOwner: UInt32, dwFlags: UInt32, punk: win32more.System.Com.IUnknown_head, ppic: POINTER(win32more.UI.TextServices.ITfContext_head), pecTextStore: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Push(pic: win32more.UI.TextServices.ITfContext_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Pop(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTop(ppic: POINTER(win32more.UI.TextServices.ITfContext_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetBase(ppic: POINTER(win32more.UI.TextServices.ITfContext_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def EnumContexts(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfContexts_head)) -> win32more.Foundation.HRESULT: ...
class ITfEditRecord(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('42d4d099-7c1a-4a89-b8-36-6c-6f-22-16-0d-f0')
    @commethod(3)
    def GetSelectionStatus(pfChanged: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTextAndPropertyUpdates(dwFlags: win32more.UI.TextServices.GET_TEXT_AND_PROPERTY_UPDATES_FLAGS, prgProperties: POINTER(POINTER(Guid)), cProperties: UInt32, ppEnum: POINTER(win32more.UI.TextServices.IEnumTfRanges_head)) -> win32more.Foundation.HRESULT: ...
class ITfEditSession(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aa80e803-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    @commethod(3)
    def DoEditSession(ec: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfEditTransactionSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('708fbf70-b520-416b-b0-6c-2c-41-ab-44-f8-ba')
    @commethod(3)
    def OnStartEditTransaction(pic: win32more.UI.TextServices.ITfContext_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnEndEditTransaction(pic: win32more.UI.TextServices.ITfContext_head) -> win32more.Foundation.HRESULT: ...
class ITfFnAdviseText(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('3527268b-7d53-4dd9-92-b7-72-96-ae-46-12-49')
    @commethod(4)
    def OnTextUpdate(pRange: win32more.UI.TextServices.ITfRange_head, pchText: win32more.Foundation.PWSTR, cch: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnLatticeUpdate(pRange: win32more.UI.TextServices.ITfRange_head, pLattice: win32more.UI.TextServices.ITfLMLattice_head) -> win32more.Foundation.HRESULT: ...
class ITfFnBalloon(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3bab89e4-5fbe-45f4-a5-bc-dc-a3-6a-d2-25-a8')
    @commethod(3)
    def UpdateBalloon(style: win32more.UI.TextServices.TfLBBalloonStyle, pch: win32more.Foundation.PWSTR, cch: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfFnConfigure(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('88f567c6-1757-49f8-a1-b2-89-23-4c-1e-ef-f9')
    @commethod(4)
    def Show(hwndParent: win32more.Foundation.HWND, langid: UInt16, rguidProfile: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class ITfFnConfigureRegisterEudc(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('b5e26ff5-d7ad-4304-91-3f-21-a2-ed-95-a1-b0')
    @commethod(4)
    def Show(hwndParent: win32more.Foundation.HWND, langid: UInt16, rguidProfile: POINTER(Guid), bstrRegistered: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class ITfFnConfigureRegisterWord(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('bb95808a-6d8f-4bca-84-00-53-90-b5-86-ae-df')
    @commethod(4)
    def Show(hwndParent: win32more.Foundation.HWND, langid: UInt16, rguidProfile: POINTER(Guid), bstrRegistered: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class ITfFnCustomSpeechCommand(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('fca6c349-a12f-43a3-8d-d6-5a-5a-42-82-57-7b')
    @commethod(4)
    def SetSpeechCommandProvider(pspcmdProvider: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class ITfFnGetLinguisticAlternates(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('ea163ce2-7a65-4506-82-a3-c5-28-21-5d-a6-4e')
    @commethod(4)
    def GetAlternates(pRange: win32more.UI.TextServices.ITfRange_head, ppCandidateList: POINTER(win32more.UI.TextServices.ITfCandidateList_head)) -> win32more.Foundation.HRESULT: ...
class ITfFnGetPreferredTouchKeyboardLayout(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('5f309a41-590a-4acc-a9-7f-d8-ef-ff-13-fd-fc')
    @commethod(4)
    def GetLayout(pTKBLayoutType: POINTER(win32more.UI.TextServices.TKBLayoutType), pwPreferredLayoutId: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
class ITfFnGetSAPIObject(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('5c0ab7ea-167d-4f59-bf-b5-46-93-75-5e-90-ca')
    @commethod(4)
    def Get(sObj: win32more.UI.TextServices.TfSapiObject, ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ITfFnLMInternal(c_void_p):
    extends: win32more.UI.TextServices.ITfFnLMProcessor
    Guid = Guid('04b825b1-ac9a-4f7b-b5-ad-c7-16-8f-1e-e4-45')
    @commethod(11)
    def ProcessLattice(pRange: win32more.UI.TextServices.ITfRange_head) -> win32more.Foundation.HRESULT: ...
class ITfFnLMProcessor(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('7afbf8e7-ac4b-4082-b0-58-89-08-99-d3-a0-10')
    @commethod(4)
    def QueryRange(pRange: win32more.UI.TextServices.ITfRange_head, ppNewRange: POINTER(win32more.UI.TextServices.ITfRange_head), pfAccepted: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def QueryLangID(langid: UInt16, pfAccepted: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetReconversion(pRange: win32more.UI.TextServices.ITfRange_head, ppCandList: POINTER(win32more.UI.TextServices.ITfCandidateList_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Reconvert(pRange: win32more.UI.TextServices.ITfRange_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def QueryKey(fUp: win32more.Foundation.BOOL, vKey: win32more.Foundation.WPARAM, lparamKeydata: win32more.Foundation.LPARAM, pfInterested: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def InvokeKey(fUp: win32more.Foundation.BOOL, vKey: win32more.Foundation.WPARAM, lparamKeyData: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def InvokeFunc(pic: win32more.UI.TextServices.ITfContext_head, refguidFunc: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class ITfFnLangProfileUtil(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('a87a8574-a6c1-4e15-99-f0-3d-39-65-f5-48-eb')
    @commethod(4)
    def RegisterActiveProfiles() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def IsProfileAvailableForLang(langid: UInt16, pfAvailable: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITfFnPlayBack(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('a3a416a4-0f64-11d3-b5-b7-00-c0-4f-c3-24-a1')
    @commethod(4)
    def QueryRange(pRange: win32more.UI.TextServices.ITfRange_head, ppNewRange: POINTER(win32more.UI.TextServices.ITfRange_head), pfPlayable: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Play(pRange: win32more.UI.TextServices.ITfRange_head) -> win32more.Foundation.HRESULT: ...
class ITfFnPropertyUIStatus(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('2338ac6e-2b9d-44c0-a7-5e-ee-64-f2-56-b3-bd')
    @commethod(4)
    def GetStatus(refguidProp: POINTER(Guid), pdw: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetStatus(refguidProp: POINTER(Guid), dw: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfFnReconversion(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('4cea93c0-0a58-11d3-8d-f0-00-10-5a-27-99-b5')
    @commethod(4)
    def QueryRange(pRange: win32more.UI.TextServices.ITfRange_head, ppNewRange: POINTER(win32more.UI.TextServices.ITfRange_head), pfConvertable: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetReconversion(pRange: win32more.UI.TextServices.ITfRange_head, ppCandList: POINTER(win32more.UI.TextServices.ITfCandidateList_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Reconvert(pRange: win32more.UI.TextServices.ITfRange_head) -> win32more.Foundation.HRESULT: ...
class ITfFnSearchCandidateProvider(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('87a2ad8f-f27b-4920-85-01-67-60-22-80-17-5d')
    @commethod(4)
    def GetSearchCandidates(bstrQuery: win32more.Foundation.BSTR, bstrApplicationId: win32more.Foundation.BSTR, pplist: POINTER(win32more.UI.TextServices.ITfCandidateList_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetResult(bstrQuery: win32more.Foundation.BSTR, bstrApplicationID: win32more.Foundation.BSTR, bstrResult: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class ITfFnShowHelp(c_void_p):
    extends: win32more.UI.TextServices.ITfFunction
    Guid = Guid('5ab1d30c-094d-4c29-8e-a5-0b-f5-9b-e8-7b-f3')
    @commethod(4)
    def Show(hwndParent: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
class ITfFunction(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('db593490-098f-11d3-8d-f0-00-10-5a-27-99-b5')
    @commethod(3)
    def GetDisplayName(pbstrName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ITfFunctionProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('101d6610-0990-11d3-8d-f0-00-10-5a-27-99-b5')
    @commethod(3)
    def GetType(pguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(pbstrDesc: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetFunction(rguid: POINTER(Guid), riid: POINTER(Guid), ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ITfInputProcessorProfileActivationSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('71c6e74e-0f28-11d8-a8-2a-00-06-5b-84-43-5c')
    @commethod(3)
    def OnActivated(dwProfileType: UInt32, langid: UInt16, clsid: POINTER(Guid), catid: POINTER(Guid), guidProfile: POINTER(Guid), hkl: win32more.UI.TextServices.HKL, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfInputProcessorProfileMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('71c6e74c-0f28-11d8-a8-2a-00-06-5b-84-43-5c')
    @commethod(3)
    def ActivateProfile(dwProfileType: UInt32, langid: UInt16, clsid: POINTER(Guid), guidProfile: POINTER(Guid), hkl: win32more.UI.TextServices.HKL, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def DeactivateProfile(dwProfileType: UInt32, langid: UInt16, clsid: POINTER(Guid), guidProfile: POINTER(Guid), hkl: win32more.UI.TextServices.HKL, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetProfile(dwProfileType: UInt32, langid: UInt16, clsid: POINTER(Guid), guidProfile: POINTER(Guid), hkl: win32more.UI.TextServices.HKL, pProfile: POINTER(win32more.UI.TextServices.TF_INPUTPROCESSORPROFILE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EnumProfiles(langid: UInt16, ppEnum: POINTER(win32more.UI.TextServices.IEnumTfInputProcessorProfiles_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ReleaseInputProcessor(rclsid: POINTER(Guid), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterProfile(rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), pchDesc: win32more.Foundation.PWSTR, cchDesc: UInt32, pchIconFile: win32more.Foundation.PWSTR, cchFile: UInt32, uIconIndex: UInt32, hklsubstitute: win32more.UI.TextServices.HKL, dwPreferredLayout: UInt32, bEnabledByDefault: win32more.Foundation.BOOL, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def UnregisterProfile(rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetActiveProfile(catid: POINTER(Guid), pProfile: POINTER(win32more.UI.TextServices.TF_INPUTPROCESSORPROFILE_head)) -> win32more.Foundation.HRESULT: ...
class ITfInputProcessorProfileSubstituteLayout(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4fd67194-1002-4513-bf-f2-c0-dd-f6-25-85-52')
    @commethod(3)
    def GetSubstituteKeyboardLayout(rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), phKL: POINTER(win32more.UI.TextServices.HKL)) -> win32more.Foundation.HRESULT: ...
class ITfInputProcessorProfiles(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1f02b6c5-7842-4ee6-8a-0b-9a-24-18-3a-95-ca')
    @commethod(3)
    def Register(rclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Unregister(rclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddLanguageProfile(rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), pchDesc: win32more.Foundation.PWSTR, cchDesc: UInt32, pchIconFile: win32more.Foundation.PWSTR, cchFile: UInt32, uIconIndex: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveLanguageProfile(rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def EnumInputProcessorInfo(ppEnum: POINTER(win32more.System.Com.IEnumGUID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetDefaultLanguageProfile(langid: UInt16, catid: POINTER(Guid), pclsid: POINTER(Guid), pguidProfile: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetDefaultLanguageProfile(langid: UInt16, rclsid: POINTER(Guid), guidProfiles: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ActivateLanguageProfile(rclsid: POINTER(Guid), langid: UInt16, guidProfiles: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetActiveLanguageProfile(rclsid: POINTER(Guid), plangid: POINTER(UInt16), pguidProfile: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetLanguageProfileDescription(rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), pbstrProfile: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetCurrentLanguage(plangid: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def ChangeCurrentLanguage(langid: UInt16) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetLanguageList(ppLangId: POINTER(POINTER(UInt16)), pulCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def EnumLanguageProfiles(langid: UInt16, ppEnum: POINTER(win32more.UI.TextServices.IEnumTfLanguageProfiles_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def EnableLanguageProfile(rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), fEnable: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def IsEnabledLanguageProfile(rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), pfEnable: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def EnableLanguageProfileByDefault(rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), fEnable: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SubstituteKeyboardLayout(rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), hKL: win32more.UI.TextServices.HKL) -> win32more.Foundation.HRESULT: ...
class ITfInputProcessorProfilesEx(c_void_p):
    extends: win32more.UI.TextServices.ITfInputProcessorProfiles
    Guid = Guid('892f230f-fe00-4a41-a9-8e-fc-d6-de-0d-35-ef')
    @commethod(21)
    def SetLanguageProfileDisplayName(rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), pchFile: win32more.Foundation.PWSTR, cchFile: UInt32, uResId: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfInputScope(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fde1eaee-6924-4cdf-91-e7-da-38-cf-f5-55-9d')
    @commethod(3)
    def GetInputScopes(pprgInputScopes: POINTER(POINTER(win32more.UI.TextServices.InputScope)), pcCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPhrase(ppbstrPhrases: POINTER(POINTER(win32more.Foundation.BSTR)), pcCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetRegularExpression(pbstrRegExp: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSRGS(pbstrSRGS: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetXML(pbstrXML: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ITfInputScope2(c_void_p):
    extends: win32more.UI.TextServices.ITfInputScope
    Guid = Guid('5731eaa0-6bc2-4681-a5-32-92-fb-b7-4d-7c-41')
    @commethod(8)
    def EnumWordList(ppEnumString: POINTER(win32more.System.Com.IEnumString_head)) -> win32more.Foundation.HRESULT: ...
class ITfInsertAtSelection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('55ce16ba-3014-41c1-9c-eb-fa-de-14-46-ac-6c')
    @commethod(3)
    def InsertTextAtSelection(ec: UInt32, dwFlags: win32more.UI.TextServices.INSERT_TEXT_AT_SELECTION_FLAGS, pchText: win32more.Foundation.PWSTR, cch: Int32, ppRange: POINTER(win32more.UI.TextServices.ITfRange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def InsertEmbeddedAtSelection(ec: UInt32, dwFlags: UInt32, pDataObject: win32more.System.Com.IDataObject_head, ppRange: POINTER(win32more.UI.TextServices.ITfRange_head)) -> win32more.Foundation.HRESULT: ...
class ITfIntegratableCandidateListUIElement(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c7a6f54f-b180-416f-b2-bf-7b-f2-e4-68-3d-7b')
    @commethod(3)
    def SetIntegrationStyle(guidIntegrationStyle: Guid) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSelectionStyle(ptfSelectionStyle: POINTER(win32more.UI.TextServices.TfIntegratableCandidateListSelectionStyle)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnKeyDown(wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ShowCandidateNumbers(pfShow: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def FinalizeExactCompositionString() -> win32more.Foundation.HRESULT: ...
class ITfKeyEventSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aa80e7f5-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    @commethod(3)
    def OnSetFocus(fForeground: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnTestKeyDown(pic: win32more.UI.TextServices.ITfContext_head, wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnTestKeyUp(pic: win32more.UI.TextServices.ITfContext_head, wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnKeyDown(pic: win32more.UI.TextServices.ITfContext_head, wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnKeyUp(pic: win32more.UI.TextServices.ITfContext_head, wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def OnPreservedKey(pic: win32more.UI.TextServices.ITfContext_head, rguid: POINTER(Guid), pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITfKeyTraceEventSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1cd4c13b-1c36-4191-a7-0a-7f-3e-61-1f-36-7d')
    @commethod(3)
    def OnKeyTraceDown(wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnKeyTraceUp(wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
class ITfKeystrokeMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aa80e7f0-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    @commethod(3)
    def AdviseKeyEventSink(tid: UInt32, pSink: win32more.UI.TextServices.ITfKeyEventSink_head, fForeground: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseKeyEventSink(tid: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetForeground(pclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def TestKeyDown(wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def TestKeyUp(wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def KeyDown(wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def KeyUp(wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetPreservedKey(pic: win32more.UI.TextServices.ITfContext_head, pprekey: POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head), pguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def IsPreservedKey(rguid: POINTER(Guid), pprekey: POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head), pfRegistered: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def PreserveKey(tid: UInt32, rguid: POINTER(Guid), prekey: POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head), pchDesc: win32more.Foundation.PWSTR, cchDesc: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def UnpreserveKey(rguid: POINTER(Guid), pprekey: POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetPreservedKeyDescription(rguid: POINTER(Guid), pchDesc: win32more.Foundation.PWSTR, cchDesc: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetPreservedKeyDescription(rguid: POINTER(Guid), pbstrDesc: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SimulatePreservedKey(pic: win32more.UI.TextServices.ITfContext_head, rguid: POINTER(Guid), pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITfLMLattice(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d4236675-a5bf-4570-9d-42-5d-6d-7b-02-d5-9b')
    @commethod(3)
    def QueryType(rguidType: POINTER(Guid), pfSupported: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def EnumLatticeElements(dwFrameStart: UInt32, rguidType: POINTER(Guid), ppEnum: POINTER(win32more.UI.TextServices.IEnumTfLatticeElements_head)) -> win32more.Foundation.HRESULT: ...
class ITfLangBarEventSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('18a4e900-e0ae-11d2-af-dd-00-10-5a-27-99-b5')
    @commethod(3)
    def OnSetFocus(dwThreadId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnThreadTerminate(dwThreadId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnThreadItemChange(dwThreadId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnModalInput(dwThreadId: UInt32, uMsg: UInt32, wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ShowFloating(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetItemFloatingRect(dwThreadId: UInt32, rguid: POINTER(Guid), prc: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
class ITfLangBarItem(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('73540d69-edeb-4ee9-96-c9-23-aa-30-b2-59-16')
    @commethod(3)
    def GetInfo(pInfo: POINTER(win32more.UI.TextServices.TF_LANGBARITEMINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetStatus(pdwStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Show(fShow: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTooltipString(pbstrToolTip: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ITfLangBarItemBalloon(c_void_p):
    extends: win32more.UI.TextServices.ITfLangBarItem
    Guid = Guid('01c2d285-d3c7-4b7b-b5-b5-d9-74-11-d0-c2-83')
    @commethod(7)
    def OnClick(click: win32more.UI.TextServices.TfLBIClick, pt: win32more.Foundation.POINT, prcArea: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetPreferredSize(pszDefault: POINTER(win32more.Foundation.SIZE_head), psz: POINTER(win32more.Foundation.SIZE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetBalloonInfo(pInfo: POINTER(win32more.UI.TextServices.TF_LBBALLOONINFO_head)) -> win32more.Foundation.HRESULT: ...
class ITfLangBarItemBitmap(c_void_p):
    extends: win32more.UI.TextServices.ITfLangBarItem
    Guid = Guid('73830352-d722-4179-ad-a5-f0-45-c9-8d-f3-55')
    @commethod(7)
    def OnClick(click: win32more.UI.TextServices.TfLBIClick, pt: win32more.Foundation.POINT, prcArea: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetPreferredSize(pszDefault: POINTER(win32more.Foundation.SIZE_head), psz: POINTER(win32more.Foundation.SIZE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def DrawBitmap(bmWidth: Int32, bmHeight: Int32, dwFlags: UInt32, phbmp: POINTER(win32more.Graphics.Gdi.HBITMAP), phbmpMask: POINTER(win32more.Graphics.Gdi.HBITMAP)) -> win32more.Foundation.HRESULT: ...
class ITfLangBarItemBitmapButton(c_void_p):
    extends: win32more.UI.TextServices.ITfLangBarItem
    Guid = Guid('a26a0525-3fae-4fa0-89-ee-88-a9-64-f9-f1-b5')
    @commethod(7)
    def OnClick(click: win32more.UI.TextServices.TfLBIClick, pt: win32more.Foundation.POINT, prcArea: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def InitMenu(pMenu: win32more.UI.TextServices.ITfMenu_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def OnMenuSelect(wID: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetPreferredSize(pszDefault: POINTER(win32more.Foundation.SIZE_head), psz: POINTER(win32more.Foundation.SIZE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def DrawBitmap(bmWidth: Int32, bmHeight: Int32, dwFlags: UInt32, phbmp: POINTER(win32more.Graphics.Gdi.HBITMAP), phbmpMask: POINTER(win32more.Graphics.Gdi.HBITMAP)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetText(pbstrText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ITfLangBarItemButton(c_void_p):
    extends: win32more.UI.TextServices.ITfLangBarItem
    Guid = Guid('28c7f1d0-de25-11d2-af-dd-00-10-5a-27-99-b5')
    @commethod(7)
    def OnClick(click: win32more.UI.TextServices.TfLBIClick, pt: win32more.Foundation.POINT, prcArea: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def InitMenu(pMenu: win32more.UI.TextServices.ITfMenu_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def OnMenuSelect(wID: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetIcon(phIcon: POINTER(win32more.UI.WindowsAndMessaging.HICON)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetText(pbstrText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ITfLangBarItemMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ba468c55-9956-4fb1-a5-9d-52-a7-dd-7c-c6-aa')
    @commethod(3)
    def EnumItems(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfLangBarItems_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(rguid: POINTER(Guid), ppItem: POINTER(win32more.UI.TextServices.ITfLangBarItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddItem(punk: win32more.UI.TextServices.ITfLangBarItem_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveItem(punk: win32more.UI.TextServices.ITfLangBarItem_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def AdviseItemSink(punk: win32more.UI.TextServices.ITfLangBarItemSink_head, pdwCookie: POINTER(UInt32), rguidItem: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def UnadviseItemSink(dwCookie: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetItemFloatingRect(dwThreadId: UInt32, rguid: POINTER(Guid), prc: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetItemsStatus(ulCount: UInt32, prgguid: POINTER(Guid), pdwStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetItemNum(pulCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetItems(ulCount: UInt32, ppItem: POINTER(win32more.UI.TextServices.ITfLangBarItem_head), pInfo: POINTER(win32more.UI.TextServices.TF_LANGBARITEMINFO_head), pdwStatus: POINTER(UInt32), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def AdviseItemsSink(ulCount: UInt32, ppunk: POINTER(win32more.UI.TextServices.ITfLangBarItemSink_head), pguidItem: POINTER(Guid), pdwCookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def UnadviseItemsSink(ulCount: UInt32, pdwCookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITfLangBarItemSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('57dbe1a0-de25-11d2-af-dd-00-10-5a-27-99-b5')
    @commethod(3)
    def OnUpdate(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfLangBarMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('87955690-e627-11d2-8d-db-00-10-5a-27-99-b5')
    @commethod(3)
    def AdviseEventSink(pSink: win32more.UI.TextServices.ITfLangBarEventSink_head, hwnd: win32more.Foundation.HWND, dwFlags: UInt32, pdwCookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseEventSink(dwCookie: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetThreadMarshalInterface(dwThreadId: UInt32, dwType: UInt32, riid: POINTER(Guid), ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetThreadLangBarItemMgr(dwThreadId: UInt32, pplbi: POINTER(win32more.UI.TextServices.ITfLangBarItemMgr_head), pdwThreadid: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetInputProcessorProfiles(dwThreadId: UInt32, ppaip: POINTER(win32more.UI.TextServices.ITfInputProcessorProfiles_head), pdwThreadid: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RestoreLastFocus(pdwThreadId: POINTER(UInt32), fPrev: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetModalInput(pSink: win32more.UI.TextServices.ITfLangBarEventSink_head, dwThreadId: UInt32, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ShowFloating(dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetShowFloatingStatus(pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITfLanguageProfileNotifySink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('43c9fe15-f494-4c17-9d-e2-b8-a4-ac-35-0a-a8')
    @commethod(3)
    def OnLanguageChange(langid: UInt16, pfAccept: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnLanguageChanged() -> win32more.Foundation.HRESULT: ...
class ITfMSAAControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b5f8fb3b-393f-4f7c-84-cb-50-49-24-c2-70-5a')
    @commethod(3)
    def SystemEnableMSAA() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SystemDisableMSAA() -> win32more.Foundation.HRESULT: ...
class ITfMenu(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6f8a98e4-aaa0-4f15-8c-5b-07-e0-df-0a-3d-d8')
    @commethod(3)
    def AddMenuItem(uId: UInt32, dwFlags: UInt32, hbmp: win32more.Graphics.Gdi.HBITMAP, hbmpMask: win32more.Graphics.Gdi.HBITMAP, pch: win32more.Foundation.PWSTR, cch: UInt32, ppMenu: POINTER(win32more.UI.TextServices.ITfMenu_head)) -> win32more.Foundation.HRESULT: ...
class ITfMessagePump(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8f1b8ad8-0b6b-4874-90-c5-bd-76-01-1e-8f-7c')
    @commethod(3)
    def PeekMessageA(pMsg: POINTER(win32more.UI.WindowsAndMessaging.MSG_head), hwnd: win32more.Foundation.HWND, wMsgFilterMin: UInt32, wMsgFilterMax: UInt32, wRemoveMsg: UInt32, pfResult: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetMessageA(pMsg: POINTER(win32more.UI.WindowsAndMessaging.MSG_head), hwnd: win32more.Foundation.HWND, wMsgFilterMin: UInt32, wMsgFilterMax: UInt32, pfResult: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def PeekMessageW(pMsg: POINTER(win32more.UI.WindowsAndMessaging.MSG_head), hwnd: win32more.Foundation.HWND, wMsgFilterMin: UInt32, wMsgFilterMax: UInt32, wRemoveMsg: UInt32, pfResult: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetMessageW(pMsg: POINTER(win32more.UI.WindowsAndMessaging.MSG_head), hwnd: win32more.Foundation.HWND, wMsgFilterMin: UInt32, wMsgFilterMax: UInt32, pfResult: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITfMouseSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a1adaaa2-3a24-449d-ac-96-51-83-e7-f5-c2-17')
    @commethod(3)
    def OnMouseEvent(uEdge: UInt32, uQuadrant: UInt32, dwBtnStatus: UInt32, pfEaten: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITfMouseTracker(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('09d146cd-a544-4132-92-5b-7a-fa-8e-f3-22-d0')
    @commethod(3)
    def AdviseMouseSink(range: win32more.UI.TextServices.ITfRange_head, pSink: win32more.UI.TextServices.ITfMouseSink_head, pdwCookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseMouseSink(dwCookie: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfMouseTrackerACP(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3bdd78e2-c16e-47fd-b8-83-ce-6f-ac-c1-a2-08')
    @commethod(3)
    def AdviseMouseSink(range: win32more.UI.TextServices.ITfRangeACP_head, pSink: win32more.UI.TextServices.ITfMouseSink_head, pdwCookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseMouseSink(dwCookie: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfPersistentPropertyLoaderACP(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4ef89150-0807-11d3-8d-f0-00-10-5a-27-99-b5')
    @commethod(3)
    def LoadProperty(pHdr: POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head), ppStream: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
class ITfPreservedKeyNotifySink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6f77c993-d2b1-446e-85-3e-59-12-ef-c8-a2-86')
    @commethod(3)
    def OnUpdated(pprekey: POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head)) -> win32more.Foundation.HRESULT: ...
class ITfProperty(c_void_p):
    extends: win32more.UI.TextServices.ITfReadOnlyProperty
    Guid = Guid('e2449660-9542-11d2-bf-46-00-10-5a-27-99-b5')
    @commethod(7)
    def FindRange(ec: UInt32, pRange: win32more.UI.TextServices.ITfRange_head, ppRange: POINTER(win32more.UI.TextServices.ITfRange_head), aPos: win32more.UI.TextServices.TfAnchor) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetValueStore(ec: UInt32, pRange: win32more.UI.TextServices.ITfRange_head, pPropStore: win32more.UI.TextServices.ITfPropertyStore_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetValue(ec: UInt32, pRange: win32more.UI.TextServices.ITfRange_head, pvarValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Clear(ec: UInt32, pRange: win32more.UI.TextServices.ITfRange_head) -> win32more.Foundation.HRESULT: ...
class ITfPropertyStore(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6834b120-88cb-11d2-bf-45-00-10-5a-27-99-b5')
    @commethod(3)
    def GetType(pguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataType(pdwReserved: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetData(pvarValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnTextUpdated(dwFlags: UInt32, pRangeNew: win32more.UI.TextServices.ITfRange_head, pfAccept: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Shrink(pRangeNew: win32more.UI.TextServices.ITfRange_head, pfFree: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Divide(pRangeThis: win32more.UI.TextServices.ITfRange_head, pRangeNew: win32more.UI.TextServices.ITfRange_head, ppPropStore: POINTER(win32more.UI.TextServices.ITfPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Clone(pPropStore: POINTER(win32more.UI.TextServices.ITfPropertyStore_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetPropertyRangeCreator(pclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Serialize(pStream: win32more.System.Com.IStream_head, pcb: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITfQueryEmbedded(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0fab9bdb-d250-4169-84-e5-6b-e1-18-fd-d7-a8')
    @commethod(3)
    def QueryInsertEmbedded(pguidService: POINTER(Guid), pFormatEtc: POINTER(win32more.System.Com.FORMATETC_head), pfInsertable: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITfRange(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aa80e7ff-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    @commethod(3)
    def GetText(ec: UInt32, dwFlags: UInt32, pchText: win32more.Foundation.PWSTR, cchMax: UInt32, pcch: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetText(ec: UInt32, dwFlags: UInt32, pchText: win32more.Foundation.PWSTR, cch: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetFormattedText(ec: UInt32, ppDataObject: POINTER(win32more.System.Com.IDataObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetEmbedded(ec: UInt32, rguidService: POINTER(Guid), riid: POINTER(Guid), ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def InsertEmbedded(ec: UInt32, dwFlags: UInt32, pDataObject: win32more.System.Com.IDataObject_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ShiftStart(ec: UInt32, cchReq: Int32, pcch: POINTER(Int32), pHalt: POINTER(win32more.UI.TextServices.TF_HALTCOND_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def ShiftEnd(ec: UInt32, cchReq: Int32, pcch: POINTER(Int32), pHalt: POINTER(win32more.UI.TextServices.TF_HALTCOND_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def ShiftStartToRange(ec: UInt32, pRange: win32more.UI.TextServices.ITfRange_head, aPos: win32more.UI.TextServices.TfAnchor) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ShiftEndToRange(ec: UInt32, pRange: win32more.UI.TextServices.ITfRange_head, aPos: win32more.UI.TextServices.TfAnchor) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def ShiftStartRegion(ec: UInt32, dir: win32more.UI.TextServices.TfShiftDir, pfNoRegion: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def ShiftEndRegion(ec: UInt32, dir: win32more.UI.TextServices.TfShiftDir, pfNoRegion: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def IsEmpty(ec: UInt32, pfEmpty: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Collapse(ec: UInt32, aPos: win32more.UI.TextServices.TfAnchor) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def IsEqualStart(ec: UInt32, pWith: win32more.UI.TextServices.ITfRange_head, aPos: win32more.UI.TextServices.TfAnchor, pfEqual: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def IsEqualEnd(ec: UInt32, pWith: win32more.UI.TextServices.ITfRange_head, aPos: win32more.UI.TextServices.TfAnchor, pfEqual: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def CompareStart(ec: UInt32, pWith: win32more.UI.TextServices.ITfRange_head, aPos: win32more.UI.TextServices.TfAnchor, plResult: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def CompareEnd(ec: UInt32, pWith: win32more.UI.TextServices.ITfRange_head, aPos: win32more.UI.TextServices.TfAnchor, plResult: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def AdjustForInsert(ec: UInt32, cchInsert: UInt32, pfInsertOk: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetGravity(pgStart: POINTER(win32more.UI.TextServices.TfGravity), pgEnd: POINTER(win32more.UI.TextServices.TfGravity)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SetGravity(ec: UInt32, gStart: win32more.UI.TextServices.TfGravity, gEnd: win32more.UI.TextServices.TfGravity) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def Clone(ppClone: POINTER(win32more.UI.TextServices.ITfRange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetContext(ppContext: POINTER(win32more.UI.TextServices.ITfContext_head)) -> win32more.Foundation.HRESULT: ...
class ITfRangeACP(c_void_p):
    extends: win32more.UI.TextServices.ITfRange
    Guid = Guid('057a6296-029b-4154-b7-9a-0d-46-1d-4e-a9-4c')
    @commethod(25)
    def GetExtent(pacpAnchor: POINTER(Int32), pcch: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def SetExtent(acpAnchor: Int32, cch: Int32) -> win32more.Foundation.HRESULT: ...
class ITfRangeBackup(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('463a506d-6992-49d2-9b-88-93-d5-5e-70-bb-16')
    @commethod(3)
    def Restore(ec: UInt32, pRange: win32more.UI.TextServices.ITfRange_head) -> win32more.Foundation.HRESULT: ...
class ITfReadOnlyProperty(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('17d49a3d-f8b8-4b2f-b2-54-52-31-9d-d6-4c-53')
    @commethod(3)
    def GetType(pguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def EnumRanges(ec: UInt32, ppEnum: POINTER(win32more.UI.TextServices.IEnumTfRanges_head), pTargetRange: win32more.UI.TextServices.ITfRange_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetValue(ec: UInt32, pRange: win32more.UI.TextServices.ITfRange_head, pvarValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetContext(ppContext: POINTER(win32more.UI.TextServices.ITfContext_head)) -> win32more.Foundation.HRESULT: ...
class ITfReadingInformationUIElement(c_void_p):
    extends: win32more.UI.TextServices.ITfUIElement
    Guid = Guid('ea1ea139-19df-11d7-a6-d2-00-06-5b-84-43-5c')
    @commethod(7)
    def GetUpdatedFlags(pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetContext(ppic: POINTER(win32more.UI.TextServices.ITfContext_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetString(pstr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetMaxReadingStringLength(pcchMax: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetErrorIndex(pErrorIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def IsVerticalOrderPreferred(pfVertical: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITfReverseConversion(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a415e162-157d-417d-8a-8c-0a-b2-6c-7d-27-81')
    @commethod(3)
    def DoReverseConversion(lpstr: win32more.Foundation.PWSTR, ppList: POINTER(win32more.UI.TextServices.ITfReverseConversionList_head)) -> win32more.Foundation.HRESULT: ...
class ITfReverseConversionList(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('151d69f0-86f4-4674-b7-21-56-91-1e-79-7f-47')
    @commethod(3)
    def GetLength(puIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetString(uIndex: UInt32, pbstr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ITfReverseConversionMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b643c236-c493-41b6-ab-b3-69-24-12-77-5c-c4')
    @commethod(3)
    def GetReverseConversion(langid: UInt16, guidProfile: POINTER(Guid), dwflag: UInt32, ppReverseConversion: POINTER(win32more.UI.TextServices.ITfReverseConversion_head)) -> win32more.Foundation.HRESULT: ...
class ITfSource(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4ea48a35-60ae-446f-8f-d6-e6-a8-d8-24-59-f7')
    @commethod(3)
    def AdviseSink(riid: POINTER(Guid), punk: win32more.System.Com.IUnknown_head, pdwCookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseSink(dwCookie: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfSourceSingle(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('73131f9c-56a9-49dd-b0-ee-d0-46-63-3f-75-28')
    @commethod(3)
    def AdviseSingleSink(tid: UInt32, riid: POINTER(Guid), punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseSingleSink(tid: UInt32, riid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class ITfSpeechUIServer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('90e9a944-9244-489f-a7-8f-de-67-af-c0-13-a7')
    @commethod(3)
    def Initialize() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ShowUI(fShow: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateBalloon(style: win32more.UI.TextServices.TfLBBalloonStyle, pch: win32more.Foundation.PWSTR, cch: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfStatusSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6b7d8d73-b267-4f69-b3-2e-1c-a3-21-ce-4f-45')
    @commethod(3)
    def OnStatusChange(pic: win32more.UI.TextServices.ITfContext_head, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfSystemDeviceTypeLangBarItem(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('45672eb9-9059-46a2-83-8d-45-30-35-5f-6a-77')
    @commethod(3)
    def SetIconMode(dwFlags: win32more.UI.TextServices.LANG_BAR_ITEM_ICON_MODE_FLAGS) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetIconMode(pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITfSystemLangBarItem(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1e13e9ec-6b33-4d4a-b5-eb-8a-92-f0-29-f3-56')
    @commethod(3)
    def SetIcon(hIcon: win32more.UI.WindowsAndMessaging.HICON) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetTooltipString(pchToolTip: win32more.Foundation.PWSTR, cch: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfSystemLangBarItemSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1449d9ab-13cf-4687-aa-3e-8d-8b-18-57-43-96')
    @commethod(3)
    def InitMenu(pMenu: win32more.UI.TextServices.ITfMenu_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnMenuSelect(wID: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfSystemLangBarItemText(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5c4ce0e5-ba49-4b52-ac-6b-3b-39-7b-4f-70-1f')
    @commethod(3)
    def SetItemText(pch: win32more.Foundation.PWSTR, cch: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetItemText(pbstrText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ITfTextEditSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8127d409-ccd3-4683-96-7a-b4-3d-5b-48-2b-f7')
    @commethod(3)
    def OnEndEdit(pic: win32more.UI.TextServices.ITfContext_head, ecReadOnly: UInt32, pEditRecord: win32more.UI.TextServices.ITfEditRecord_head) -> win32more.Foundation.HRESULT: ...
class ITfTextInputProcessor(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aa80e7f7-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    @commethod(3)
    def Activate(ptim: win32more.UI.TextServices.ITfThreadMgr_head, tid: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Deactivate() -> win32more.Foundation.HRESULT: ...
class ITfTextInputProcessorEx(c_void_p):
    extends: win32more.UI.TextServices.ITfTextInputProcessor
    Guid = Guid('6e4e2102-f9cd-433d-b4-96-30-3c-e0-3a-65-07')
    @commethod(5)
    def ActivateEx(ptim: win32more.UI.TextServices.ITfThreadMgr_head, tid: UInt32, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class ITfTextLayoutSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2af2d06a-dd5b-4927-a0-b4-54-f1-9c-91-fa-de')
    @commethod(3)
    def OnLayoutChange(pic: win32more.UI.TextServices.ITfContext_head, lcode: win32more.UI.TextServices.TfLayoutCode, pView: win32more.UI.TextServices.ITfContextView_head) -> win32more.Foundation.HRESULT: ...
class ITfThreadFocusSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c0f1db0c-3a20-405c-a3-03-96-b6-01-0a-88-5f')
    @commethod(3)
    def OnSetThreadFocus() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnKillThreadFocus() -> win32more.Foundation.HRESULT: ...
class ITfThreadMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aa80e801-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    @commethod(3)
    def Activate(ptid: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Deactivate() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateDocumentMgr(ppdim: POINTER(win32more.UI.TextServices.ITfDocumentMgr_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EnumDocumentMgrs(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfDocumentMgrs_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetFocus(ppdimFocus: POINTER(win32more.UI.TextServices.ITfDocumentMgr_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetFocus(pdimFocus: win32more.UI.TextServices.ITfDocumentMgr_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def AssociateFocus(hwnd: win32more.Foundation.HWND, pdimNew: win32more.UI.TextServices.ITfDocumentMgr_head, ppdimPrev: POINTER(win32more.UI.TextServices.ITfDocumentMgr_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def IsThreadFocus(pfThreadFocus: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetFunctionProvider(clsid: POINTER(Guid), ppFuncProv: POINTER(win32more.UI.TextServices.ITfFunctionProvider_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def EnumFunctionProviders(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfFunctionProviders_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetGlobalCompartment(ppCompMgr: POINTER(win32more.UI.TextServices.ITfCompartmentMgr_head)) -> win32more.Foundation.HRESULT: ...
class ITfThreadMgr2(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0ab198ef-6477-4ee8-88-12-67-80-ed-b8-2d-5e')
    @commethod(3)
    def Activate(ptid: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Deactivate() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateDocumentMgr(ppdim: POINTER(win32more.UI.TextServices.ITfDocumentMgr_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def EnumDocumentMgrs(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfDocumentMgrs_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetFocus(ppdimFocus: POINTER(win32more.UI.TextServices.ITfDocumentMgr_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetFocus(pdimFocus: win32more.UI.TextServices.ITfDocumentMgr_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def IsThreadFocus(pfThreadFocus: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetFunctionProvider(clsid: POINTER(Guid), ppFuncProv: POINTER(win32more.UI.TextServices.ITfFunctionProvider_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def EnumFunctionProviders(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfFunctionProviders_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetGlobalCompartment(ppCompMgr: POINTER(win32more.UI.TextServices.ITfCompartmentMgr_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def ActivateEx(ptid: POINTER(UInt32), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetActiveFlags(lpdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SuspendKeystrokeHandling() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def ResumeKeystrokeHandling() -> win32more.Foundation.HRESULT: ...
class ITfThreadMgrEventSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('aa80e80e-2021-11d2-93-e0-00-60-b0-67-b8-6e')
    @commethod(3)
    def OnInitDocumentMgr(pdim: win32more.UI.TextServices.ITfDocumentMgr_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnUninitDocumentMgr(pdim: win32more.UI.TextServices.ITfDocumentMgr_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnSetFocus(pdimFocus: win32more.UI.TextServices.ITfDocumentMgr_head, pdimPrevFocus: win32more.UI.TextServices.ITfDocumentMgr_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnPushContext(pic: win32more.UI.TextServices.ITfContext_head) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnPopContext(pic: win32more.UI.TextServices.ITfContext_head) -> win32more.Foundation.HRESULT: ...
class ITfThreadMgrEx(c_void_p):
    extends: win32more.UI.TextServices.ITfThreadMgr
    Guid = Guid('3e90ade3-7594-4cb0-bb-58-69-62-8f-5f-45-8c')
    @commethod(14)
    def ActivateEx(ptid: POINTER(UInt32), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetActiveFlags(lpdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITfToolTipUIElement(c_void_p):
    extends: win32more.UI.TextServices.ITfUIElement
    Guid = Guid('52b18b5c-555d-46b2-b0-0a-fa-68-01-44-fb-db')
    @commethod(7)
    def GetString(pstr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ITfTransitoryExtensionSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a615096f-1c57-4813-8a-15-55-ee-6e-5a-83-9c')
    @commethod(3)
    def OnTransitoryExtensionUpdated(pic: win32more.UI.TextServices.ITfContext_head, ecReadOnly: UInt32, pResultRange: win32more.UI.TextServices.ITfRange_head, pCompositionRange: win32more.UI.TextServices.ITfRange_head, pfDeleteResultRange: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITfTransitoryExtensionUIElement(c_void_p):
    extends: win32more.UI.TextServices.ITfUIElement
    Guid = Guid('858f956a-972f-42a2-a2-f2-03-21-e1-ab-e2-09')
    @commethod(7)
    def GetDocumentMgr(ppdim: POINTER(win32more.UI.TextServices.ITfDocumentMgr_head)) -> win32more.Foundation.HRESULT: ...
class ITfUIElement(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ea1ea137-19df-11d7-a6-d2-00-06-5b-84-43-5c')
    @commethod(3)
    def GetDescription(pbstrDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetGUID(pguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Show(bShow: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def IsShown(pbShow: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class ITfUIElementMgr(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ea1ea135-19df-11d7-a6-d2-00-06-5b-84-43-5c')
    @commethod(3)
    def BeginUIElement(pElement: win32more.UI.TextServices.ITfUIElement_head, pbShow: POINTER(win32more.Foundation.BOOL), pdwUIElementId: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateUIElement(dwUIElementId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EndUIElement(dwUIElementId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetUIElement(dwUIELementId: UInt32, ppElement: POINTER(win32more.UI.TextServices.ITfUIElement_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def EnumUIElements(ppEnum: POINTER(win32more.UI.TextServices.IEnumTfUIElements_head)) -> win32more.Foundation.HRESULT: ...
class ITfUIElementSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ea1ea136-19df-11d7-a6-d2-00-06-5b-84-43-5c')
    @commethod(3)
    def BeginUIElement(dwUIElementId: UInt32, pbShow: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateUIElement(dwUIElementId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EndUIElement(dwUIElementId: UInt32) -> win32more.Foundation.HRESULT: ...
class IUIManagerEventSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('cd91d690-a7e8-4265-9b-38-8b-b3-bb-ab-a7-de')
    @commethod(3)
    def OnWindowOpening(prcBounds: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OnWindowOpened(prcBounds: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnWindowUpdating(prcUpdatedBounds: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnWindowUpdated(prcUpdatedBounds: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnWindowClosing() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def OnWindowClosed() -> win32more.Foundation.HRESULT: ...
class IVersionInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('401518ec-db00-4611-9b-29-2a-0e-4b-9a-fa-85')
    @commethod(3)
    def GetSubcomponentCount(ulSub: UInt32, ulCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetImplementationID(ulSub: UInt32, implid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetBuildVersion(ulSub: UInt32, pdwMajor: POINTER(UInt32), pdwMinor: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetComponentDescription(ulSub: UInt32, pImplStr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetInstanceDescription(ulSub: UInt32, pImplStr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
InputScope = Int32
IS_DEFAULT: InputScope = 0
IS_URL: InputScope = 1
IS_FILE_FULLFILEPATH: InputScope = 2
IS_FILE_FILENAME: InputScope = 3
IS_EMAIL_USERNAME: InputScope = 4
IS_EMAIL_SMTPEMAILADDRESS: InputScope = 5
IS_LOGINNAME: InputScope = 6
IS_PERSONALNAME_FULLNAME: InputScope = 7
IS_PERSONALNAME_PREFIX: InputScope = 8
IS_PERSONALNAME_GIVENNAME: InputScope = 9
IS_PERSONALNAME_MIDDLENAME: InputScope = 10
IS_PERSONALNAME_SURNAME: InputScope = 11
IS_PERSONALNAME_SUFFIX: InputScope = 12
IS_ADDRESS_FULLPOSTALADDRESS: InputScope = 13
IS_ADDRESS_POSTALCODE: InputScope = 14
IS_ADDRESS_STREET: InputScope = 15
IS_ADDRESS_STATEORPROVINCE: InputScope = 16
IS_ADDRESS_CITY: InputScope = 17
IS_ADDRESS_COUNTRYNAME: InputScope = 18
IS_ADDRESS_COUNTRYSHORTNAME: InputScope = 19
IS_CURRENCY_AMOUNTANDSYMBOL: InputScope = 20
IS_CURRENCY_AMOUNT: InputScope = 21
IS_DATE_FULLDATE: InputScope = 22
IS_DATE_MONTH: InputScope = 23
IS_DATE_DAY: InputScope = 24
IS_DATE_YEAR: InputScope = 25
IS_DATE_MONTHNAME: InputScope = 26
IS_DATE_DAYNAME: InputScope = 27
IS_DIGITS: InputScope = 28
IS_NUMBER: InputScope = 29
IS_ONECHAR: InputScope = 30
IS_PASSWORD: InputScope = 31
IS_TELEPHONE_FULLTELEPHONENUMBER: InputScope = 32
IS_TELEPHONE_COUNTRYCODE: InputScope = 33
IS_TELEPHONE_AREACODE: InputScope = 34
IS_TELEPHONE_LOCALNUMBER: InputScope = 35
IS_TIME_FULLTIME: InputScope = 36
IS_TIME_HOUR: InputScope = 37
IS_TIME_MINORSEC: InputScope = 38
IS_NUMBER_FULLWIDTH: InputScope = 39
IS_ALPHANUMERIC_HALFWIDTH: InputScope = 40
IS_ALPHANUMERIC_FULLWIDTH: InputScope = 41
IS_CURRENCY_CHINESE: InputScope = 42
IS_BOPOMOFO: InputScope = 43
IS_HIRAGANA: InputScope = 44
IS_KATAKANA_HALFWIDTH: InputScope = 45
IS_KATAKANA_FULLWIDTH: InputScope = 46
IS_HANJA: InputScope = 47
IS_HANGUL_HALFWIDTH: InputScope = 48
IS_HANGUL_FULLWIDTH: InputScope = 49
IS_SEARCH: InputScope = 50
IS_FORMULA: InputScope = 51
IS_SEARCH_INCREMENTAL: InputScope = 52
IS_CHINESE_HALFWIDTH: InputScope = 53
IS_CHINESE_FULLWIDTH: InputScope = 54
IS_NATIVE_SCRIPT: InputScope = 55
IS_YOMI: InputScope = 56
IS_TEXT: InputScope = 57
IS_CHAT: InputScope = 58
IS_NAME_OR_PHONENUMBER: InputScope = 59
IS_EMAILNAME_OR_ADDRESS: InputScope = 60
IS_PRIVATE: InputScope = 61
IS_MAPS: InputScope = 62
IS_NUMERIC_PASSWORD: InputScope = 63
IS_NUMERIC_PIN: InputScope = 64
IS_ALPHANUMERIC_PIN: InputScope = 65
IS_ALPHANUMERIC_PIN_SET: InputScope = 66
IS_FORMULA_NUMBER: InputScope = 67
IS_CHAT_WITHOUT_EMOJI: InputScope = 68
IS_PHRASELIST: InputScope = -1
IS_REGULAREXPRESSION: InputScope = -2
IS_SRGS: InputScope = -3
IS_XML: InputScope = -4
IS_ENUMSTRING: InputScope = -5
LANG_BAR_ITEM_ICON_MODE_FLAGS = UInt32
TF_DTLBI_NONE: LANG_BAR_ITEM_ICON_MODE_FLAGS = 0
TF_DTLBI_USEPROFILEICON: LANG_BAR_ITEM_ICON_MODE_FLAGS = 1
MSAAControl = Guid('08cd963f-7a3e-4f5c-9b-d8-d6-92-bb-04-3c-5b')
TEXT_STORE_CHANGE_FLAGS = UInt32
TS_TC_NONE: TEXT_STORE_CHANGE_FLAGS = 0
TS_TC_CORRECTION: TEXT_STORE_CHANGE_FLAGS = 1
TEXT_STORE_LOCK_FLAGS = UInt32
TS_LF_READ: TEXT_STORE_LOCK_FLAGS = 2
TS_LF_READWRITE: TEXT_STORE_LOCK_FLAGS = 6
TEXT_STORE_TEXT_CHANGE_FLAGS = UInt32
TS_ST_NONE: TEXT_STORE_TEXT_CHANGE_FLAGS = 0
TS_ST_CORRECTION: TEXT_STORE_TEXT_CHANGE_FLAGS = 1
TF_CONTEXT_EDIT_CONTEXT_FLAGS = UInt32
TF_ES_ASYNCDONTCARE: TF_CONTEXT_EDIT_CONTEXT_FLAGS = 0
TF_ES_SYNC: TF_CONTEXT_EDIT_CONTEXT_FLAGS = 1
TF_ES_READ: TF_CONTEXT_EDIT_CONTEXT_FLAGS = 2
TF_ES_READWRITE: TF_CONTEXT_EDIT_CONTEXT_FLAGS = 6
TF_ES_ASYNC: TF_CONTEXT_EDIT_CONTEXT_FLAGS = 8
TF_DA_ATTR_INFO = Int32
TF_ATTR_INPUT: TF_DA_ATTR_INFO = 0
TF_ATTR_TARGET_CONVERTED: TF_DA_ATTR_INFO = 1
TF_ATTR_CONVERTED: TF_DA_ATTR_INFO = 2
TF_ATTR_TARGET_NOTCONVERTED: TF_DA_ATTR_INFO = 3
TF_ATTR_INPUT_ERROR: TF_DA_ATTR_INFO = 4
TF_ATTR_FIXEDCONVERTED: TF_DA_ATTR_INFO = 5
TF_ATTR_OTHER: TF_DA_ATTR_INFO = -1
class TF_DA_COLOR(Structure):
    type: win32more.UI.TextServices.TF_DA_COLORTYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        nIndex: Int32
        cr: win32more.Foundation.COLORREF
TF_DA_COLORTYPE = Int32
TF_CT_NONE: TF_DA_COLORTYPE = 0
TF_CT_SYSCOLOR: TF_DA_COLORTYPE = 1
TF_CT_COLORREF: TF_DA_COLORTYPE = 2
TF_DA_LINESTYLE = Int32
TF_LS_NONE: TF_DA_LINESTYLE = 0
TF_LS_SOLID: TF_DA_LINESTYLE = 1
TF_LS_DOT: TF_DA_LINESTYLE = 2
TF_LS_DASH: TF_DA_LINESTYLE = 3
TF_LS_SQUIGGLE: TF_DA_LINESTYLE = 4
class TF_DISPLAYATTRIBUTE(Structure):
    crText: win32more.UI.TextServices.TF_DA_COLOR
    crBk: win32more.UI.TextServices.TF_DA_COLOR
    lsStyle: win32more.UI.TextServices.TF_DA_LINESTYLE
    fBoldLine: win32more.Foundation.BOOL
    crLine: win32more.UI.TextServices.TF_DA_COLOR
    bAttr: win32more.UI.TextServices.TF_DA_ATTR_INFO
class TF_HALTCOND(Structure):
    pHaltRange: win32more.UI.TextServices.ITfRange_head
    aHaltPos: win32more.UI.TextServices.TfAnchor
    dwFlags: UInt32
class TF_INPUTPROCESSORPROFILE(Structure):
    dwProfileType: UInt32
    langid: UInt16
    clsid: Guid
    guidProfile: Guid
    catid: Guid
    hklSubstitute: win32more.UI.TextServices.HKL
    dwCaps: UInt32
    hkl: win32more.UI.TextServices.HKL
    dwFlags: UInt32
class TF_LANGBARITEMINFO(Structure):
    clsidService: Guid
    guidItem: Guid
    dwStyle: UInt32
    ulSort: UInt32
    szDescription: Char * 32
class TF_LANGUAGEPROFILE(Structure):
    clsid: Guid
    langid: UInt16
    catid: Guid
    fActive: win32more.Foundation.BOOL
    guidProfile: Guid
class TF_LBBALLOONINFO(Structure):
    style: win32more.UI.TextServices.TfLBBalloonStyle
    bstrText: win32more.Foundation.BSTR
class TF_LMLATTELEMENT(Structure):
    dwFrameStart: UInt32
    dwFrameLen: UInt32
    dwFlags: UInt32
    Anonymous: _Anonymous_e__Union
    bstrText: win32more.Foundation.BSTR
    class _Anonymous_e__Union(Union):
        iCost: Int32
class TF_PERSISTENT_PROPERTY_HEADER_ACP(Structure):
    guidType: Guid
    ichStart: Int32
    cch: Int32
    cb: UInt32
    dwPrivate: UInt32
    clsidTIP: Guid
class TF_PRESERVEDKEY(Structure):
    uVKey: UInt32
    uModifiers: UInt32
class TF_PROPERTYVAL(Structure):
    guidId: Guid
    varValue: win32more.System.Com.VARIANT
class TF_SELECTION(Structure):
    range: win32more.UI.TextServices.ITfRange_head
    style: win32more.UI.TextServices.TF_SELECTIONSTYLE
class TF_SELECTIONSTYLE(Structure):
    ase: win32more.UI.TextServices.TfActiveSelEnd
    fInterimChar: win32more.Foundation.BOOL
TKBLayoutType = Int32
TKBLT_UNDEFINED: TKBLayoutType = 0
TKBLT_CLASSIC: TKBLayoutType = 1
TKBLT_OPTIMIZED: TKBLayoutType = 2
class TS_ATTRVAL(Structure):
    idAttr: Guid
    dwOverlapId: UInt32
    varValue: win32more.System.Com.VARIANT
class TS_RUNINFO(Structure):
    uCount: UInt32
    type: win32more.UI.TextServices.TsRunType
class TS_SELECTIONSTYLE(Structure):
    ase: win32more.UI.TextServices.TsActiveSelEnd
    fInterimChar: win32more.Foundation.BOOL
class TS_SELECTION_ACP(Structure):
    acpStart: Int32
    acpEnd: Int32
    style: win32more.UI.TextServices.TS_SELECTIONSTYLE
class TS_SELECTION_ANCHOR(Structure):
    paStart: win32more.UI.TextServices.IAnchor_head
    paEnd: win32more.UI.TextServices.IAnchor_head
    style: win32more.UI.TextServices.TS_SELECTIONSTYLE
class TS_STATUS(Structure):
    dwDynamicFlags: UInt32
    dwStaticFlags: UInt32
class TS_TEXTCHANGE(Structure):
    acpStart: Int32
    acpOldEnd: Int32
    acpNewEnd: Int32
TfActiveSelEnd = Int32
TF_AE_NONE: TfActiveSelEnd = 0
TF_AE_START: TfActiveSelEnd = 1
TF_AE_END: TfActiveSelEnd = 2
TfAnchor = Int32
TF_ANCHOR_START: TfAnchor = 0
TF_ANCHOR_END: TfAnchor = 1
TfCandidateResult = Int32
CAND_FINALIZED: TfCandidateResult = 0
CAND_SELECTED: TfCandidateResult = 1
CAND_CANCELED: TfCandidateResult = 2
TfGravity = Int32
TF_GRAVITY_BACKWARD: TfGravity = 0
TF_GRAVITY_FORWARD: TfGravity = 1
TfIntegratableCandidateListSelectionStyle = Int32
STYLE_ACTIVE_SELECTION: TfIntegratableCandidateListSelectionStyle = 0
STYLE_IMPLIED_SELECTION: TfIntegratableCandidateListSelectionStyle = 1
TfLBBalloonStyle = Int32
TF_LB_BALLOON_RECO: TfLBBalloonStyle = 0
TF_LB_BALLOON_SHOW: TfLBBalloonStyle = 1
TF_LB_BALLOON_MISS: TfLBBalloonStyle = 2
TfLBIClick = Int32
TF_LBI_CLK_RIGHT: TfLBIClick = 1
TF_LBI_CLK_LEFT: TfLBIClick = 2
TfLayoutCode = Int32
TF_LC_CREATE: TfLayoutCode = 0
TF_LC_CHANGE: TfLayoutCode = 1
TF_LC_DESTROY: TfLayoutCode = 2
TfSapiObject = Int32
GETIF_RESMGR: TfSapiObject = 0
GETIF_RECOCONTEXT: TfSapiObject = 1
GETIF_RECOGNIZER: TfSapiObject = 2
GETIF_VOICE: TfSapiObject = 3
GETIF_DICTGRAM: TfSapiObject = 4
GETIF_RECOGNIZERNOINIT: TfSapiObject = 5
TfShiftDir = Int32
TF_SD_BACKWARD: TfShiftDir = 0
TF_SD_FORWARD: TfShiftDir = 1
TsActiveSelEnd = Int32
TS_AE_NONE: TsActiveSelEnd = 0
TS_AE_START: TsActiveSelEnd = 1
TS_AE_END: TsActiveSelEnd = 2
TsGravity = Int32
TS_GR_BACKWARD: TsGravity = 0
TS_GR_FORWARD: TsGravity = 1
TsLayoutCode = Int32
TS_LC_CREATE: TsLayoutCode = 0
TS_LC_CHANGE: TsLayoutCode = 1
TS_LC_DESTROY: TsLayoutCode = 2
TsRunType = Int32
TS_RT_PLAIN: TsRunType = 0
TS_RT_HIDDEN: TsRunType = 1
TS_RT_OPAQUE: TsRunType = 2
TsShiftDir = Int32
TS_SD_BACKWARD: TsShiftDir = 0
TS_SD_FORWARD: TsShiftDir = 1
make_head(_module, 'IAccClientDocMgr')
make_head(_module, 'IAccDictionary')
make_head(_module, 'IAccServerDocMgr')
make_head(_module, 'IAccStore')
make_head(_module, 'IAnchor')
make_head(_module, 'IClonableWrapper')
make_head(_module, 'ICoCreateLocally')
make_head(_module, 'ICoCreatedLocally')
make_head(_module, 'IDocWrap')
make_head(_module, 'IEnumITfCompositionView')
make_head(_module, 'IEnumSpeechCommands')
make_head(_module, 'IEnumTfCandidates')
make_head(_module, 'IEnumTfContextViews')
make_head(_module, 'IEnumTfContexts')
make_head(_module, 'IEnumTfDisplayAttributeInfo')
make_head(_module, 'IEnumTfDocumentMgrs')
make_head(_module, 'IEnumTfFunctionProviders')
make_head(_module, 'IEnumTfInputProcessorProfiles')
make_head(_module, 'IEnumTfLangBarItems')
make_head(_module, 'IEnumTfLanguageProfiles')
make_head(_module, 'IEnumTfLatticeElements')
make_head(_module, 'IEnumTfProperties')
make_head(_module, 'IEnumTfPropertyValue')
make_head(_module, 'IEnumTfRanges')
make_head(_module, 'IEnumTfUIElements')
make_head(_module, 'IInternalDocWrap')
make_head(_module, 'ISpeechCommandProvider')
make_head(_module, 'ITextStoreACP')
make_head(_module, 'ITextStoreACP2')
make_head(_module, 'ITextStoreACPEx')
make_head(_module, 'ITextStoreACPServices')
make_head(_module, 'ITextStoreACPSink')
make_head(_module, 'ITextStoreACPSinkEx')
make_head(_module, 'ITextStoreAnchor')
make_head(_module, 'ITextStoreAnchorEx')
make_head(_module, 'ITextStoreAnchorSink')
make_head(_module, 'ITextStoreSinkAnchorEx')
make_head(_module, 'ITfActiveLanguageProfileNotifySink')
make_head(_module, 'ITfCandidateList')
make_head(_module, 'ITfCandidateListUIElement')
make_head(_module, 'ITfCandidateListUIElementBehavior')
make_head(_module, 'ITfCandidateString')
make_head(_module, 'ITfCategoryMgr')
make_head(_module, 'ITfCleanupContextDurationSink')
make_head(_module, 'ITfCleanupContextSink')
make_head(_module, 'ITfClientId')
make_head(_module, 'ITfCompartment')
make_head(_module, 'ITfCompartmentEventSink')
make_head(_module, 'ITfCompartmentMgr')
make_head(_module, 'ITfComposition')
make_head(_module, 'ITfCompositionSink')
make_head(_module, 'ITfCompositionView')
make_head(_module, 'ITfConfigureSystemKeystrokeFeed')
make_head(_module, 'ITfContext')
make_head(_module, 'ITfContextComposition')
make_head(_module, 'ITfContextKeyEventSink')
make_head(_module, 'ITfContextOwner')
make_head(_module, 'ITfContextOwnerCompositionServices')
make_head(_module, 'ITfContextOwnerCompositionSink')
make_head(_module, 'ITfContextOwnerServices')
make_head(_module, 'ITfContextView')
make_head(_module, 'ITfCreatePropertyStore')
make_head(_module, 'ITfDisplayAttributeInfo')
make_head(_module, 'ITfDisplayAttributeMgr')
make_head(_module, 'ITfDisplayAttributeNotifySink')
make_head(_module, 'ITfDisplayAttributeProvider')
make_head(_module, 'ITfDocumentMgr')
make_head(_module, 'ITfEditRecord')
make_head(_module, 'ITfEditSession')
make_head(_module, 'ITfEditTransactionSink')
make_head(_module, 'ITfFnAdviseText')
make_head(_module, 'ITfFnBalloon')
make_head(_module, 'ITfFnConfigure')
make_head(_module, 'ITfFnConfigureRegisterEudc')
make_head(_module, 'ITfFnConfigureRegisterWord')
make_head(_module, 'ITfFnCustomSpeechCommand')
make_head(_module, 'ITfFnGetLinguisticAlternates')
make_head(_module, 'ITfFnGetPreferredTouchKeyboardLayout')
make_head(_module, 'ITfFnGetSAPIObject')
make_head(_module, 'ITfFnLMInternal')
make_head(_module, 'ITfFnLMProcessor')
make_head(_module, 'ITfFnLangProfileUtil')
make_head(_module, 'ITfFnPlayBack')
make_head(_module, 'ITfFnPropertyUIStatus')
make_head(_module, 'ITfFnReconversion')
make_head(_module, 'ITfFnSearchCandidateProvider')
make_head(_module, 'ITfFnShowHelp')
make_head(_module, 'ITfFunction')
make_head(_module, 'ITfFunctionProvider')
make_head(_module, 'ITfInputProcessorProfileActivationSink')
make_head(_module, 'ITfInputProcessorProfileMgr')
make_head(_module, 'ITfInputProcessorProfileSubstituteLayout')
make_head(_module, 'ITfInputProcessorProfiles')
make_head(_module, 'ITfInputProcessorProfilesEx')
make_head(_module, 'ITfInputScope')
make_head(_module, 'ITfInputScope2')
make_head(_module, 'ITfInsertAtSelection')
make_head(_module, 'ITfIntegratableCandidateListUIElement')
make_head(_module, 'ITfKeyEventSink')
make_head(_module, 'ITfKeyTraceEventSink')
make_head(_module, 'ITfKeystrokeMgr')
make_head(_module, 'ITfLMLattice')
make_head(_module, 'ITfLangBarEventSink')
make_head(_module, 'ITfLangBarItem')
make_head(_module, 'ITfLangBarItemBalloon')
make_head(_module, 'ITfLangBarItemBitmap')
make_head(_module, 'ITfLangBarItemBitmapButton')
make_head(_module, 'ITfLangBarItemButton')
make_head(_module, 'ITfLangBarItemMgr')
make_head(_module, 'ITfLangBarItemSink')
make_head(_module, 'ITfLangBarMgr')
make_head(_module, 'ITfLanguageProfileNotifySink')
make_head(_module, 'ITfMSAAControl')
make_head(_module, 'ITfMenu')
make_head(_module, 'ITfMessagePump')
make_head(_module, 'ITfMouseSink')
make_head(_module, 'ITfMouseTracker')
make_head(_module, 'ITfMouseTrackerACP')
make_head(_module, 'ITfPersistentPropertyLoaderACP')
make_head(_module, 'ITfPreservedKeyNotifySink')
make_head(_module, 'ITfProperty')
make_head(_module, 'ITfPropertyStore')
make_head(_module, 'ITfQueryEmbedded')
make_head(_module, 'ITfRange')
make_head(_module, 'ITfRangeACP')
make_head(_module, 'ITfRangeBackup')
make_head(_module, 'ITfReadOnlyProperty')
make_head(_module, 'ITfReadingInformationUIElement')
make_head(_module, 'ITfReverseConversion')
make_head(_module, 'ITfReverseConversionList')
make_head(_module, 'ITfReverseConversionMgr')
make_head(_module, 'ITfSource')
make_head(_module, 'ITfSourceSingle')
make_head(_module, 'ITfSpeechUIServer')
make_head(_module, 'ITfStatusSink')
make_head(_module, 'ITfSystemDeviceTypeLangBarItem')
make_head(_module, 'ITfSystemLangBarItem')
make_head(_module, 'ITfSystemLangBarItemSink')
make_head(_module, 'ITfSystemLangBarItemText')
make_head(_module, 'ITfTextEditSink')
make_head(_module, 'ITfTextInputProcessor')
make_head(_module, 'ITfTextInputProcessorEx')
make_head(_module, 'ITfTextLayoutSink')
make_head(_module, 'ITfThreadFocusSink')
make_head(_module, 'ITfThreadMgr')
make_head(_module, 'ITfThreadMgr2')
make_head(_module, 'ITfThreadMgrEventSink')
make_head(_module, 'ITfThreadMgrEx')
make_head(_module, 'ITfToolTipUIElement')
make_head(_module, 'ITfTransitoryExtensionSink')
make_head(_module, 'ITfTransitoryExtensionUIElement')
make_head(_module, 'ITfUIElement')
make_head(_module, 'ITfUIElementMgr')
make_head(_module, 'ITfUIElementSink')
make_head(_module, 'IUIManagerEventSink')
make_head(_module, 'IVersionInfo')
make_head(_module, 'TF_DA_COLOR')
make_head(_module, 'TF_DISPLAYATTRIBUTE')
make_head(_module, 'TF_HALTCOND')
make_head(_module, 'TF_INPUTPROCESSORPROFILE')
make_head(_module, 'TF_LANGBARITEMINFO')
make_head(_module, 'TF_LANGUAGEPROFILE')
make_head(_module, 'TF_LBBALLOONINFO')
make_head(_module, 'TF_LMLATTELEMENT')
make_head(_module, 'TF_PERSISTENT_PROPERTY_HEADER_ACP')
make_head(_module, 'TF_PRESERVEDKEY')
make_head(_module, 'TF_PROPERTYVAL')
make_head(_module, 'TF_SELECTION')
make_head(_module, 'TF_SELECTIONSTYLE')
make_head(_module, 'TS_ATTRVAL')
make_head(_module, 'TS_RUNINFO')
make_head(_module, 'TS_SELECTIONSTYLE')
make_head(_module, 'TS_SELECTION_ACP')
make_head(_module, 'TS_SELECTION_ANCHOR')
make_head(_module, 'TS_STATUS')
make_head(_module, 'TS_TEXTCHANGE')
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
_arch_optional = [
]
