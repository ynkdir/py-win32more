from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.UI.Input.KeyboardAndMouse
import win32more.Windows.Win32.UI.TextServices
import win32more.Windows.Win32.UI.WindowsAndMessaging
ANCHOR_CHANGE_HISTORY_FLAGS = UInt32
TS_CH_PRECEDING_DEL: win32more.Windows.Win32.UI.TextServices.ANCHOR_CHANGE_HISTORY_FLAGS = 1
TS_CH_FOLLOWING_DEL: win32more.Windows.Win32.UI.TextServices.ANCHOR_CHANGE_HISTORY_FLAGS = 2
AccClientDocMgr = Guid('{fc48cc30-4f3e-4fa1-803b-ad0e196a83b1}')
AccDictionary = Guid('{6572ee16-5fe5-4331-bb6d-76a49c56e423}')
AccServerDocMgr = Guid('{6089a37e-eb8a-482d-bd6f-f9f46904d16d}')
AccStore = Guid('{5440837f-4bff-4ae5-a1b1-7722ecc6332a}')
GUID_PROP_TEXTOWNER: Guid = Guid('{f1e2d520-0969-11d3-8df0-00105a2799b5}')
GUID_PROP_ATTRIBUTE: Guid = Guid('{34b45670-7526-11d2-a147-00105a2799b5}')
GUID_PROP_LANGID: Guid = Guid('{3280ce20-8032-11d2-b603-00105a2799b5}')
GUID_PROP_READING: Guid = Guid('{5463f7c0-8e31-11d2-bf46-00105a2799b5}')
GUID_PROP_COMPOSING: Guid = Guid('{e12ac060-af15-11d2-afc5-00105a2799b5}')
GUID_PROP_TKB_ALTERNATES: Guid = Guid('{70b2a803-968d-462e-b93b-2164c91517f7}')
GUID_SYSTEM_FUNCTIONPROVIDER: Guid = Guid('{9a698bb0-0f21-11d3-8df1-00105a2799b5}')
GUID_APP_FUNCTIONPROVIDER: Guid = Guid('{4caef01e-12af-4b0e-9db1-a6ec5b881208}')
GUID_TFCAT_CATEGORY_OF_TIP: Guid = Guid('{534c48c1-0607-4098-a521-4fc899c73e90}')
GUID_TFCAT_TIP_KEYBOARD: Guid = Guid('{34745c63-b2f0-4784-8b67-5e12c8701a31}')
GUID_TFCAT_TIP_SPEECH: Guid = Guid('{b5a73cd1-8355-426b-a161-259808f26b14}')
GUID_TFCAT_TIP_HANDWRITING: Guid = Guid('{246ecb87-c2f2-4abe-905b-c8b38add2c43}')
GUID_TFCAT_PROP_AUDIODATA: Guid = Guid('{9b7be3a9-e8ab-4d47-a8fe-254fa423436d}')
GUID_TFCAT_PROP_INKDATA: Guid = Guid('{7c6a82ae-b0d7-4f14-a745-14f28b009d61}')
GUID_COMPARTMENT_SAPI_AUDIO: Guid = Guid('{51af2086-cc6b-457d-b5aa-8b19dc290ab4}')
GUID_COMPARTMENT_KEYBOARD_DISABLED: Guid = Guid('{71a5b253-1951-466b-9fbc-9c8808fa84f2}')
GUID_COMPARTMENT_KEYBOARD_OPENCLOSE: Guid = Guid('{58273aad-01bb-4164-95c6-755ba0b5162d}')
GUID_COMPARTMENT_HANDWRITING_OPENCLOSE: Guid = Guid('{f9ae2c6b-1866-4361-af72-7aa30948890e}')
GUID_COMPARTMENT_SPEECH_DISABLED: Guid = Guid('{56c5c607-0703-4e59-8e52-cbc84e8bbe35}')
GUID_COMPARTMENT_SPEECH_OPENCLOSE: Guid = Guid('{544d6a63-e2e8-4752-bbd1-000960bca083}')
GUID_COMPARTMENT_SPEECH_GLOBALSTATE: Guid = Guid('{2a54fe8e-0d08-460c-a75d-87035ff436c5}')
GUID_COMPARTMENT_CONVERSIONMODEBIAS: Guid = Guid('{5497f516-ee91-436e-b946-aa2c05f1ac5b}')
GUID_PROP_MODEBIAS: Guid = Guid('{372e0716-974f-40ac-a088-08cdc92ebfbc}')
GUID_COMPARTMENT_KEYBOARD_INPUTMODE: Guid = Guid('{b6592511-bcee-4122-a7c4-09f4b3fa4396}')
GUID_MODEBIAS_NONE: Guid = Guid('{00000000-0000-0000-0000-000000000000}')
GUID_MODEBIAS_URLHISTORY: Guid = Guid('{8b0e54d9-63f2-4c68-84d4-79aee7a59f09}')
GUID_MODEBIAS_FILENAME: Guid = Guid('{d7f707fe-44c6-4fca-8e76-86ab50c7931b}')
GUID_MODEBIAS_READING: Guid = Guid('{e31643a3-6466-4cbf-8d8b-0bd4d8545461}')
GUID_MODEBIAS_DATETIME: Guid = Guid('{f2bdb372-7f61-4039-92ef-1c35599f0222}')
GUID_MODEBIAS_NAME: Guid = Guid('{fddc10f0-d239-49bf-b8fc-5410caaa427e}')
GUID_MODEBIAS_CONVERSATION: Guid = Guid('{0f4ec104-1790-443b-95f1-e10f939d6546}')
GUID_MODEBIAS_NUMERIC: Guid = Guid('{4021766c-e872-48fd-9cee-4ec5c75e16c3}')
GUID_MODEBIAS_HIRAGANA: Guid = Guid('{d73d316e-9b91-46f1-a280-31597f52c694}')
GUID_MODEBIAS_KATAKANA: Guid = Guid('{2e0eeddd-3a1a-499e-8543-3c7ee7949811}')
GUID_MODEBIAS_HANGUL: Guid = Guid('{76ef0541-23b3-4d77-a074-691801ccea17}')
GUID_MODEBIAS_CHINESE: Guid = Guid('{7add26de-4328-489b-83ae-6493750cad5c}')
GUID_MODEBIAS_HALFWIDTHKATAKANA: Guid = Guid('{005f6b63-78d4-41cc-8859-485ca821a795}')
GUID_MODEBIAS_FULLWIDTHALPHANUMERIC: Guid = Guid('{81489fb8-b36a-473d-8146-e4a2258b24ae}')
GUID_MODEBIAS_FULLWIDTHHANGUL: Guid = Guid('{c01ae6c9-45b5-4fd0-9cb1-9f4cebc39fea}')
GUID_TFCAT_PROPSTYLE_STATIC: Guid = Guid('{565fb8d8-6bd4-4ca1-b223-0f2ccb8f4f96}')
GUID_TFCAT_DISPLAYATTRIBUTEPROVIDER: Guid = Guid('{046b8c80-1647-40f7-9b21-b93b81aabc1b}')
GUID_TFCAT_DISPLAYATTRIBUTEPROPERTY: Guid = Guid('{b95f181b-ea4c-4af1-8056-7c321abbb091}')
GUID_COMPARTMENT_SPEECH_UI_STATUS: Guid = Guid('{d92016f0-9367-4fe7-9abf-bc59dacbe0e3}')
GUID_COMPARTMENT_EMPTYCONTEXT: Guid = Guid('{d7487dbf-804e-41c5-894d-ad96fd4eea13}')
GUID_COMPARTMENT_TIPUISTATUS: Guid = Guid('{148ca3ec-0366-401c-8d75-ed978d85fbc9}')
GUID_COMPARTMENT_SPEECH_CFGMENU: Guid = Guid('{fb6c5c2d-4e83-4bb6-91a2-e019bff6762d}')
GUID_LBI_SAPILAYR_CFGMENUBUTTON: Guid = Guid('{d02f24a1-942d-422e-8d99-b4f2addee999}')
GUID_TFCAT_TIPCAP_SECUREMODE: Guid = Guid('{49d2f9ce-1f5e-11d7-a6d3-00065b84435c}')
GUID_TFCAT_TIPCAP_UIELEMENTENABLED: Guid = Guid('{49d2f9cf-1f5e-11d7-a6d3-00065b84435c}')
GUID_TFCAT_TIPCAP_INPUTMODECOMPARTMENT: Guid = Guid('{ccf05dd7-4a87-11d7-a6e2-00065b84435c}')
GUID_TFCAT_TIPCAP_COMLESS: Guid = Guid('{364215d9-75bc-11d7-a6ef-00065b84435c}')
GUID_TFCAT_TIPCAP_WOW16: Guid = Guid('{364215da-75bc-11d7-a6ef-00065b84435c}')
GUID_TFCAT_TIPCAP_IMMERSIVESUPPORT: Guid = Guid('{13a016df-560b-46cd-947a-4c3af1e0e35d}')
GUID_TFCAT_TIPCAP_IMMERSIVEONLY: Guid = Guid('{3a4259ac-640d-4ad4-89f7-1eb67e7c4ee8}')
GUID_TFCAT_TIPCAP_LOCALSERVER: Guid = Guid('{74769ee9-4a66-4f9d-90d6-bf8b7c3eb461}')
GUID_TFCAT_TIPCAP_TSF3: Guid = Guid('{07dcb4af-98de-4548-bef7-25bd45979a1f}')
GUID_TFCAT_TIPCAP_DUALMODE: Guid = Guid('{3af314a2-d79f-4b1b-9992-15086d339b05}')
GUID_TFCAT_TIPCAP_SYSTRAYSUPPORT: Guid = Guid('{25504fb4-7bab-4bc1-9c69-cf81890f0ef5}')
GUID_COMPARTMENT_KEYBOARD_INPUTMODE_CONVERSION: Guid = Guid('{ccf05dd8-4a87-11d7-a6e2-00065b84435c}')
GUID_COMPARTMENT_KEYBOARD_INPUTMODE_SENTENCE: Guid = Guid('{ccf05dd9-4a87-11d7-a6e2-00065b84435c}')
GUID_COMPARTMENT_TRANSITORYEXTENSION: Guid = Guid('{8be347f5-c7a0-11d7-b408-00065b84435c}')
GUID_COMPARTMENT_TRANSITORYEXTENSION_DOCUMENTMANAGER: Guid = Guid('{8be347f7-c7a0-11d7-b408-00065b84435c}')
GUID_COMPARTMENT_TRANSITORYEXTENSION_PARENT: Guid = Guid('{8be347f8-c7a0-11d7-b408-00065b84435c}')
GUID_COMPARTMENT_ENABLED_PROFILES_UPDATED: Guid = Guid('{92c1fd48-a9ae-4a7c-be08-4329e4723817}')
GUID_TFCAT_TRANSITORYEXTENSIONUI: Guid = Guid('{6302de22-a5cf-4b02-bfe8-4d72b2bed3c6}')
GUID_LBI_INPUTMODE: Guid = Guid('{2c77a81e-41cc-4178-a3a7-5f8a987568e6}')
CLSID_TF_ThreadMgr: Guid = Guid('{529a9e6b-6587-4f23-ab9e-9c7d683e3c50}')
CLSID_TF_LangBarMgr: Guid = Guid('{ebb08c45-6c4a-4fdc-ae53-4eb8c4c7db8e}')
CLSID_TF_DisplayAttributeMgr: Guid = Guid('{3ce74de4-53d3-4d74-8b83-431b3828ba53}')
CLSID_TF_CategoryMgr: Guid = Guid('{a4b544a1-438d-4b41-9325-869523e2d6c7}')
CLSID_TF_InputProcessorProfiles: Guid = Guid('{33c53a50-f456-4884-b049-85fd643ecfed}')
CLSID_TF_LangBarItemMgr: Guid = Guid('{b9931692-a2b3-4fab-bf33-9ec6f9fb96ac}')
CLSID_TF_ClassicLangBar: Guid = Guid('{3318360c-1afc-4d09-a86b-9f9cb6dceb9c}')
CLSID_TF_TransitoryExtensionUIEntry: Guid = Guid('{ae6be008-07fb-400d-8beb-337a64f7051f}')
CLSID_TsfServices: Guid = Guid('{39aedc00-6b60-46db-8d31-3642be0e4373}')
TF_DEFAULT_SELECTION: UInt32 = 4294967295
TS_DEFAULT_SELECTION: UInt32 = 4294967295
GUID_TS_SERVICE_DATAOBJECT: Guid = Guid('{6086fbb5-e225-46ce-a770-c1bbd3e05d7b}')
GUID_TS_SERVICE_ACCESSIBLE: Guid = Guid('{f9786200-a5bf-4a0f-8c24-fb16f5d1aabb}')
GUID_TS_SERVICE_ACTIVEX: Guid = Guid('{ea937a50-c9a6-4b7d-894a-49d99b784834}')
TS_E_INVALIDPOS: win32more.Windows.Win32.Foundation.HRESULT = -2147220992
TS_E_NOLOCK: win32more.Windows.Win32.Foundation.HRESULT = -2147220991
TS_E_NOOBJECT: win32more.Windows.Win32.Foundation.HRESULT = -2147220990
TS_E_NOSERVICE: win32more.Windows.Win32.Foundation.HRESULT = -2147220989
TS_E_NOINTERFACE: win32more.Windows.Win32.Foundation.HRESULT = -2147220988
TS_E_NOSELECTION: win32more.Windows.Win32.Foundation.HRESULT = -2147220987
TS_E_NOLAYOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147220986
TS_E_INVALIDPOINT: win32more.Windows.Win32.Foundation.HRESULT = -2147220985
TS_E_SYNCHRONOUS: win32more.Windows.Win32.Foundation.HRESULT = -2147220984
TS_E_READONLY: win32more.Windows.Win32.Foundation.HRESULT = -2147220983
TS_E_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2147220982
TS_S_ASYNC: win32more.Windows.Win32.Foundation.HRESULT = 262912
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
TF_E_LOCKED: win32more.Windows.Win32.Foundation.HRESULT = -2147220224
TF_E_STACKFULL: win32more.Windows.Win32.Foundation.HRESULT = -2147220223
TF_E_NOTOWNEDRANGE: win32more.Windows.Win32.Foundation.HRESULT = -2147220222
TF_E_NOPROVIDER: win32more.Windows.Win32.Foundation.HRESULT = -2147220221
TF_E_DISCONNECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220220
TF_E_INVALIDVIEW: win32more.Windows.Win32.Foundation.HRESULT = -2147220219
TF_E_ALREADY_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = -2147220218
TF_E_RANGE_NOT_COVERED: win32more.Windows.Win32.Foundation.HRESULT = -2147220217
TF_E_COMPOSITION_REJECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147220216
TF_E_EMPTYCONTEXT: win32more.Windows.Win32.Foundation.HRESULT = -2147220215
TF_E_INVALIDPOS: win32more.Windows.Win32.Foundation.HRESULT = -2147220992
TF_E_NOLOCK: win32more.Windows.Win32.Foundation.HRESULT = -2147220991
TF_E_NOOBJECT: win32more.Windows.Win32.Foundation.HRESULT = -2147220990
TF_E_NOSERVICE: win32more.Windows.Win32.Foundation.HRESULT = -2147220989
TF_E_NOINTERFACE: win32more.Windows.Win32.Foundation.HRESULT = -2147220988
TF_E_NOSELECTION: win32more.Windows.Win32.Foundation.HRESULT = -2147220987
TF_E_NOLAYOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147220986
TF_E_INVALIDPOINT: win32more.Windows.Win32.Foundation.HRESULT = -2147220985
TF_E_SYNCHRONOUS: win32more.Windows.Win32.Foundation.HRESULT = -2147220984
TF_E_READONLY: win32more.Windows.Win32.Foundation.HRESULT = -2147220983
TF_E_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2147220982
TF_S_ASYNC: win32more.Windows.Win32.Foundation.HRESULT = 262912
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
TF_PROFILE_NEWPHONETIC: Guid = Guid('{b2f9c502-1742-11d4-9790-0080c882687e}')
TF_PROFILE_PHONETIC: Guid = Guid('{761309de-317a-11d4-9b5d-0080c882687e}')
TF_PROFILE_NEWCHANGJIE: Guid = Guid('{f3ba907a-6c7e-11d4-97fa-0080c882687e}')
TF_PROFILE_CHANGJIE: Guid = Guid('{4bdf9f03-c7d3-11d4-b2ab-0080c882687e}')
TF_PROFILE_NEWQUICK: Guid = Guid('{0b883ba0-c1c7-11d4-87f9-0080c882687e}')
TF_PROFILE_QUICK: Guid = Guid('{6024b45f-5c54-11d4-b921-0080c882687e}')
TF_PROFILE_CANTONESE: Guid = Guid('{0aec109c-7e96-11d4-b2ef-0080c882687e}')
TF_PROFILE_PINYIN: Guid = Guid('{f3ba9077-6c7e-11d4-97fa-0080c882687e}')
TF_PROFILE_SIMPLEFAST: Guid = Guid('{fa550b04-5ad7-411f-a5ac-ca038ec515d7}')
TF_PROFILE_WUBI: Guid = Guid('{82590c13-f4dd-44f4-ba1d-8667246fdf8e}')
TF_PROFILE_DAYI: Guid = Guid('{037b2c25-480c-4d7f-b027-d6ca6b69788a}')
TF_PROFILE_ARRAY: Guid = Guid('{d38eff65-aa46-4fd5-91a7-67845fb02f5b}')
TF_PROFILE_YI: Guid = Guid('{409c8376-007b-4357-ae8e-26316ee3fb0d}')
TF_PROFILE_TIGRINYA: Guid = Guid('{3cab88b7-cc3e-46a6-9765-b772ad7761ff}')
TF_E_NOCONVERSION: win32more.Windows.Win32.Foundation.HRESULT = -2147219968
TF_DICTATION_ON: UInt32 = 1
TF_DICTATION_ENABLED: UInt32 = 2
TF_COMMANDING_ENABLED: UInt32 = 4
TF_COMMANDING_ON: UInt32 = 8
TF_SPEECHUI_SHOWN: UInt32 = 16
TF_SHOW_BALLOON: UInt32 = 1
TF_DISABLE_BALLOON: UInt32 = 2
TF_MENUREADY: UInt32 = 1
TF_PROPUI_STATUS_SAVETOFILE: UInt32 = 1
GUID_INTEGRATIONSTYLE_SEARCHBOX: Guid = Guid('{e6d1bd11-82f7-4903-ae21-1a6397cde2eb}')
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
GUID_PROP_INPUTSCOPE: Guid = Guid('{1713dd5a-68e7-4a5b-9af6-592a595c778d}')
DCM_FLAGS_TASKENG: UInt32 = 1
DCM_FLAGS_CTFMON: UInt32 = 2
DCM_FLAGS_LOCALTHREADTSF: UInt32 = 4
ILMCM_CHECKLAYOUTANDTIPENABLED: UInt32 = 1
ILMCM_LANGUAGEBAROFF: UInt32 = 2
LIBID_MSAATEXTLib: Guid = Guid('{150e2d7a-dac1-4582-947d-2a8fd78b82cd}')
TS_STRF_START: UInt32 = 0
TS_STRF_MID: UInt32 = 1
TS_STRF_END: UInt32 = 2
TSATTRID_OTHERS: Guid = Guid('{b3c32af9-57d0-46a9-bca8-dac238a13057}')
TSATTRID_Font: Guid = Guid('{573ea825-749b-4f8a-9cfd-21c3605ca828}')
TSATTRID_Font_FaceName: Guid = Guid('{b536aeb6-053b-4eb8-b65a-50da1e81e72e}')
TSATTRID_Font_SizePts: Guid = Guid('{c8493302-a5e9-456d-af04-8005e4130f03}')
TSATTRID_Font_Style: Guid = Guid('{68b2a77f-6b0e-4f28-8177-571c2f3a42b1}')
TSATTRID_Font_Style_Bold: Guid = Guid('{48813a43-8a20-4940-8e58-97823f7b268a}')
TSATTRID_Font_Style_Italic: Guid = Guid('{8740682a-a765-48e1-acfc-d22222b2f810}')
TSATTRID_Font_Style_SmallCaps: Guid = Guid('{facb6bc6-9100-4cc6-b969-11eea45a86b4}')
TSATTRID_Font_Style_Capitalize: Guid = Guid('{7d85a3ba-b4fd-43b3-befc-6b985c843141}')
TSATTRID_Font_Style_Uppercase: Guid = Guid('{33a300e8-e340-4937-b697-8f234045cd9a}')
TSATTRID_Font_Style_Lowercase: Guid = Guid('{76d8ccb5-ca7b-4498-8ee9-d5c4f6f74c60}')
TSATTRID_Font_Style_Animation: Guid = Guid('{dcf73d22-e029-47b7-bb36-f263a3d004cc}')
TSATTRID_Font_Style_Animation_LasVegasLights: Guid = Guid('{f40423d5-0f87-4f8f-bada-e6d60c25e152}')
TSATTRID_Font_Style_Animation_BlinkingBackground: Guid = Guid('{86e5b104-0104-4b10-b585-00f2527522b5}')
TSATTRID_Font_Style_Animation_SparkleText: Guid = Guid('{533aad20-962c-4e9f-8c09-b42ea4749711}')
TSATTRID_Font_Style_Animation_MarchingBlackAnts: Guid = Guid('{7644e067-f186-4902-bfc6-ec815aa20e9d}')
TSATTRID_Font_Style_Animation_MarchingRedAnts: Guid = Guid('{78368dad-50fb-4c6f-840b-d486bb6cf781}')
TSATTRID_Font_Style_Animation_Shimmer: Guid = Guid('{2ce31b58-5293-4c36-8809-bf8bb51a27b3}')
TSATTRID_Font_Style_Animation_WipeDown: Guid = Guid('{5872e874-367b-4803-b160-c90ff62569d0}')
TSATTRID_Font_Style_Animation_WipeRight: Guid = Guid('{b855cbe3-3d2c-4600-b1e9-e1c9ce02f842}')
TSATTRID_Font_Style_Emboss: Guid = Guid('{bd8ed742-349e-4e37-82fb-437979cb53a7}')
TSATTRID_Font_Style_Engrave: Guid = Guid('{9c3371de-8332-4897-be5d-89233223179a}')
TSATTRID_Font_Style_Hidden: Guid = Guid('{b1e28770-881c-475f-863f-887a647b1090}')
TSATTRID_Font_Style_Kerning: Guid = Guid('{cc26e1b4-2f9a-47c8-8bff-bf1eb7cce0dd}')
TSATTRID_Font_Style_Outlined: Guid = Guid('{10e6db31-db0d-4ac6-a7f5-9c9cff6f2ab4}')
TSATTRID_Font_Style_Position: Guid = Guid('{15cd26ab-f2fb-4062-b5a6-9a49e1a5cc0b}')
TSATTRID_Font_Style_Protected: Guid = Guid('{1c557cb2-14cf-4554-a574-ecb2f7e7efd4}')
TSATTRID_Font_Style_Shadow: Guid = Guid('{5f686d2f-c6cd-4c56-8a1a-994a4b9766be}')
TSATTRID_Font_Style_Spacing: Guid = Guid('{98c1200d-8f06-409a-8e49-6a554bf7c153}')
TSATTRID_Font_Style_Weight: Guid = Guid('{12f3189c-8bb0-461b-b1fa-eaf907047fe0}')
TSATTRID_Font_Style_Height: Guid = Guid('{7e937477-12e6-458b-926a-1fa44ee8f391}')
TSATTRID_Font_Style_Underline: Guid = Guid('{c3c9c9f3-7902-444b-9a7b-48e70f4b50f7}')
TSATTRID_Font_Style_Underline_Single: Guid = Guid('{1b6720e5-0f73-4951-a6b3-6f19e43c9461}')
TSATTRID_Font_Style_Underline_Double: Guid = Guid('{74d24aa6-1db3-4c69-a176-31120e7586d5}')
TSATTRID_Font_Style_Strikethrough: Guid = Guid('{0c562193-2d08-4668-9601-ced41309d7af}')
TSATTRID_Font_Style_Strikethrough_Single: Guid = Guid('{75d736b6-3c8f-4b97-ab78-1877cb990d31}')
TSATTRID_Font_Style_Strikethrough_Double: Guid = Guid('{62489b31-a3e7-4f94-ac43-ebaf8fcc7a9f}')
TSATTRID_Font_Style_Overline: Guid = Guid('{e3989f4a-992b-4301-8ce1-a5b7c6d1f3c8}')
TSATTRID_Font_Style_Overline_Single: Guid = Guid('{8440d94c-51ce-47b2-8d4c-15751e5f721b}')
TSATTRID_Font_Style_Overline_Double: Guid = Guid('{dc46063a-e115-46e3-bcd8-ca6772aa95b4}')
TSATTRID_Font_Style_Blink: Guid = Guid('{bfb2c036-7acf-4532-b720-b416dd7765a8}')
TSATTRID_Font_Style_Subscript: Guid = Guid('{5774fb84-389b-43bc-a74b-1568347cf0f4}')
TSATTRID_Font_Style_Superscript: Guid = Guid('{2ea4993c-563c-49aa-9372-0bef09a9255b}')
TSATTRID_Font_Style_Color: Guid = Guid('{857a7a37-b8af-4e9a-81b4-acf700c8411b}')
TSATTRID_Font_Style_BackgroundColor: Guid = Guid('{b50eaa4e-3091-4468-81db-d79ea190c7c7}')
TSATTRID_Text: Guid = Guid('{7edb8e68-81f9-449d-a15a-87a8388faac0}')
TSATTRID_Text_VerticalWriting: Guid = Guid('{6bba8195-046f-4ea9-b311-97fd66c4274b}')
TSATTRID_Text_RightToLeft: Guid = Guid('{ca666e71-1b08-453d-bfdd-28e08c8aaf7a}')
TSATTRID_Text_Orientation: Guid = Guid('{6bab707f-8785-4c39-8b52-96f878303ffb}')
TSATTRID_Text_Language: Guid = Guid('{d8c04ef1-5753-4c25-8887-85443fe5f819}')
TSATTRID_Text_ReadOnly: Guid = Guid('{85836617-de32-4afd-a50f-a2db110e6e4d}')
TSATTRID_Text_EmbeddedObject: Guid = Guid('{7edb8e68-81f9-449d-a15a-87a8388faac0}')
TSATTRID_Text_Alignment: Guid = Guid('{139941e6-1767-456d-938e-35ba568b5cd4}')
TSATTRID_Text_Alignment_Left: Guid = Guid('{16ae95d3-6361-43a2-8495-d00f397f1693}')
TSATTRID_Text_Alignment_Right: Guid = Guid('{b36f0f98-1b9e-4360-8616-03fb08a78456}')
TSATTRID_Text_Alignment_Center: Guid = Guid('{a4a95c16-53bf-4d55-8b87-4bdd8d4275fc}')
TSATTRID_Text_Alignment_Justify: Guid = Guid('{ed350740-a0f7-42d3-8ea8-f81b6488faf0}')
TSATTRID_Text_Link: Guid = Guid('{47cd9051-3722-4cd8-b7c8-4e17ca1759f5}')
TSATTRID_Text_Hyphenation: Guid = Guid('{dadf4525-618e-49eb-b1a8-3b68bd7648e3}')
TSATTRID_Text_Para: Guid = Guid('{5edc5822-99dc-4dd6-aec3-b62baa5b2e7c}')
TSATTRID_Text_Para_FirstLineIndent: Guid = Guid('{07c97a13-7472-4dd8-90a9-91e3d7e4f29c}')
TSATTRID_Text_Para_LeftIndent: Guid = Guid('{fb2848e9-7471-41c9-b6b3-8a1450e01897}')
TSATTRID_Text_Para_RightIndent: Guid = Guid('{2c7f26f9-a5e2-48da-b98a-520cb16513bf}')
TSATTRID_Text_Para_SpaceAfter: Guid = Guid('{7b0a3f55-22dc-425f-a411-93da1d8f9baa}')
TSATTRID_Text_Para_SpaceBefore: Guid = Guid('{8df98589-194a-4601-b251-9865a3e906dd}')
TSATTRID_Text_Para_LineSpacing: Guid = Guid('{699b380d-7f8c-46d6-a73b-dfe3d1538df3}')
TSATTRID_Text_Para_LineSpacing_Single: Guid = Guid('{ed350740-a0f7-42d3-8ea8-f81b6488faf0}')
TSATTRID_Text_Para_LineSpacing_OnePtFive: Guid = Guid('{0428a021-0397-4b57-9a17-0795994cd3c5}')
TSATTRID_Text_Para_LineSpacing_Double: Guid = Guid('{82fb1805-a6c4-4231-ac12-6260af2aba28}')
TSATTRID_Text_Para_LineSpacing_AtLeast: Guid = Guid('{adfedf31-2d44-4434-a5ff-7f4c4990a905}')
TSATTRID_Text_Para_LineSpacing_Exactly: Guid = Guid('{3d45ad40-23de-48d7-a6b3-765420c620cc}')
TSATTRID_Text_Para_LineSpacing_Multiple: Guid = Guid('{910f1e3c-d6d0-4f65-8a3c-42b4b31868c5}')
TSATTRID_List: Guid = Guid('{436d673b-26f1-4aee-9e65-8f83a4ed4884}')
TSATTRID_List_LevelIndel: Guid = Guid('{7f7cc899-311f-487b-ad5d-e2a459e12d42}')
TSATTRID_List_Type: Guid = Guid('{ae3e665e-4bce-49e3-a0fe-2db47d3a17ae}')
TSATTRID_List_Type_Bullet: Guid = Guid('{bccd77c5-4c4d-4ce2-b102-559f3b2bfcea}')
TSATTRID_List_Type_Arabic: Guid = Guid('{1338c5d6-98a3-4fa3-9bd1-7a60eef8e9e0}')
TSATTRID_List_Type_LowerLetter: Guid = Guid('{96372285-f3cf-491e-a925-3832347fd237}')
TSATTRID_List_Type_UpperLetter: Guid = Guid('{7987b7cd-ce52-428b-9b95-a357f6f10c45}')
TSATTRID_List_Type_LowerRoman: Guid = Guid('{90466262-3980-4b8e-9368-918bd1218a41}')
TSATTRID_List_Type_UpperRoman: Guid = Guid('{0f6ab552-4a80-467f-b2f1-127e2aa3ba9e}')
TSATTRID_App: Guid = Guid('{a80f77df-4237-40e5-849c-b5fa51c13ac7}')
TSATTRID_App_IncorrectSpelling: Guid = Guid('{f42de43c-ef12-430d-944c-9a08970a25d2}')
TSATTRID_App_IncorrectGrammar: Guid = Guid('{bd54e398-ad03-4b74-b6b3-5edb19996388}')
@winfunctype('MsCtfMonitor.dll')
def DoMsCtfMonitor(dwFlags: UInt32, hEventForServiceStop: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('MsCtfMonitor.dll')
def InitLocalMsCtfMonitor(dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MsCtfMonitor.dll')
def UninitLocalMsCtfMonitor() -> win32more.Windows.Win32.Foundation.HRESULT: ...
DocWrap = Guid('{bf426f7e-7a5e-44d6-830c-a390ea9462a3}')
GET_TEXT_AND_PROPERTY_UPDATES_FLAGS = UInt32
TF_GTP_NONE: win32more.Windows.Win32.UI.TextServices.GET_TEXT_AND_PROPERTY_UPDATES_FLAGS = 0
TF_GTP_INCL_TEXT: win32more.Windows.Win32.UI.TextServices.GET_TEXT_AND_PROPERTY_UPDATES_FLAGS = 1
class IAccClientDocMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4c896039-7b6d-49e6-a8c1-45116a98292b}')
    @commethod(3)
    def GetDocuments(self, enumUnknown: POINTER(win32more.Windows.Win32.System.Com.IEnumUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LookupByHWND(self, hWnd: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LookupByPoint(self, pt: win32more.Windows.Win32.Foundation.POINT, riid: POINTER(Guid), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFocused(self, riid: POINTER(Guid), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAccDictionary(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1dc4cb5f-d737-474d-ade9-5ccfc9bc1cc9}')
    @commethod(3)
    def GetLocalizedString(self, Term: POINTER(Guid), lcid: UInt32, pResult: POINTER(win32more.Windows.Win32.Foundation.BSTR), plcid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetParentTerm(self, Term: POINTER(Guid), pParentTerm: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMnemonicString(self, Term: POINTER(Guid), pResult: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def LookupMnemonicTerm(self, bstrMnemonic: win32more.Windows.Win32.Foundation.BSTR, pTerm: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ConvertValueToString(self, Term: POINTER(Guid), lcid: UInt32, varValue: win32more.Windows.Win32.System.Variant.VARIANT, pbstrResult: POINTER(win32more.Windows.Win32.Foundation.BSTR), plcid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAccServerDocMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ad7c73cf-6dd5-4855-abc2-b04bad5b9153}')
    @commethod(3)
    def NewDocument(self, riid: POINTER(Guid), punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RevokeDocument(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnDocumentFocus(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAccStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e2cd4a63-2b72-4d48-b739-95e4765195ba}')
    @commethod(3)
    def Register(self, riid: POINTER(Guid), punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unregister(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDocuments(self, enumUnknown: POINTER(win32more.Windows.Win32.System.Com.IEnumUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def LookupByHWND(self, hWnd: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LookupByPoint(self, pt: win32more.Windows.Win32.Foundation.POINT, riid: POINTER(Guid), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnDocumentFocus(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFocused(self, riid: POINTER(Guid), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAnchor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0feb7e34-5a60-4356-8ef7-abdec2ff7cf8}')
    @commethod(3)
    def SetGravity(self, gravity: win32more.Windows.Win32.UI.TextServices.TsGravity) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetGravity(self, pgravity: POINTER(win32more.Windows.Win32.UI.TextServices.TsGravity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsEqual(self, paWith: win32more.Windows.Win32.UI.TextServices.IAnchor, pfEqual: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Compare(self, paWith: win32more.Windows.Win32.UI.TextServices.IAnchor, plResult: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Shift(self, dwFlags: UInt32, cchReq: Int32, pcch: POINTER(Int32), paHaltAnchor: win32more.Windows.Win32.UI.TextServices.IAnchor) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ShiftTo(self, paSite: win32more.Windows.Win32.UI.TextServices.IAnchor) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ShiftRegion(self, dwFlags: UInt32, dir: win32more.Windows.Win32.UI.TextServices.TsShiftDir, pfNoRegion: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetChangeHistoryMask(self, dwMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetChangeHistory(self, pdwHistory: POINTER(win32more.Windows.Win32.UI.TextServices.ANCHOR_CHANGE_HISTORY_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ClearChangeHistory(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Clone(self, ppaClone: POINTER(win32more.Windows.Win32.UI.TextServices.IAnchor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IClonableWrapper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b33e75ff-e84c-4dca-a25c-33b8dc003374}')
    @commethod(3)
    def CloneNewWrapper(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICoCreateLocally(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{03de00aa-f272-41e3-99cb-03c5e8114ea0}')
    @commethod(3)
    def CoCreateLocally(self, rclsid: POINTER(Guid), dwClsContext: UInt32, riid: POINTER(Guid), punk: POINTER(win32more.Windows.Win32.System.Com.IUnknown), riidParam: POINTER(Guid), punkParam: win32more.Windows.Win32.System.Com.IUnknown, varParam: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICoCreatedLocally(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0a53eb6c-1908-4742-8cff-2cee2e93f94c}')
    @commethod(3)
    def LocalInit(self, punkLocalObject: win32more.Windows.Win32.System.Com.IUnknown, riidParam: POINTER(Guid), punkParam: win32more.Windows.Win32.System.Com.IUnknown, varParam: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDocWrap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcd285fe-0be0-43bd-99c9-aaaec513c555}')
    @commethod(3)
    def SetDoc(self, riid: POINTER(Guid), punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWrappedDoc(self, riid: POINTER(Guid), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumITfCompositionView(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5efd22ba-7838-46cb-88e2-cadb14124f8f}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumITfCompositionView)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, rgCompositionView: POINTER(win32more.Windows.Win32.UI.TextServices.ITfCompositionView), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSpeechCommands(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8c5dac4f-083c-4b85-a4c9-71746048adca}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumSpeechCommands)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, pSpCmds: POINTER(POINTER(UInt16)), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfCandidates(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{defb1926-6c80-4ce8-87d4-d6b72b812bde}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfCandidates)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, ppCand: POINTER(win32more.Windows.Win32.UI.TextServices.ITfCandidateString), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfContextViews(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f0c0f8dd-cf38-44e1-bb0f-68cf0d551c78}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfContextViews)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, rgViews: POINTER(win32more.Windows.Win32.UI.TextServices.ITfContextView), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfContexts(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8f1a7ea6-1654-4502-a86e-b2902344d507}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfContexts)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, rgContext: POINTER(win32more.Windows.Win32.UI.TextServices.ITfContext), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfDisplayAttributeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7cef04d7-cb75-4e80-a7ab-5f5bc7d332de}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfDisplayAttributeInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, rgInfo: POINTER(win32more.Windows.Win32.UI.TextServices.ITfDisplayAttributeInfo), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfDocumentMgrs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa80e808-2021-11d2-93e0-0060b067b86e}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfDocumentMgrs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, rgDocumentMgr: POINTER(win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfFunctionProviders(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e4b24db0-0990-11d3-8df0-00105a2799b5}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfFunctionProviders)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, ppCmdobj: POINTER(win32more.Windows.Win32.UI.TextServices.ITfFunctionProvider), pcFetch: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfInputProcessorProfiles(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71c6e74d-0f28-11d8-a82a-00065b84435c}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfInputProcessorProfiles)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, pProfile: POINTER(win32more.Windows.Win32.UI.TextServices.TF_INPUTPROCESSORPROFILE), pcFetch: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfLangBarItems(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{583f34d0-de25-11d2-afdd-00105a2799b5}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfLangBarItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, ppItem: POINTER(win32more.Windows.Win32.UI.TextServices.ITfLangBarItem), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfLanguageProfiles(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3d61bf11-ac5f-42c8-a4cb-931bcc28c744}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfLanguageProfiles)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, pProfile: POINTER(win32more.Windows.Win32.UI.TextServices.TF_LANGUAGEPROFILE), pcFetch: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfLatticeElements(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56988052-47da-4a05-911a-e3d941f17145}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfLatticeElements)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, rgsElements: POINTER(win32more.Windows.Win32.UI.TextServices.TF_LMLATTELEMENT), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{19188cb0-aca9-11d2-afc5-00105a2799b5}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfProperties)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, ppProp: POINTER(win32more.Windows.Win32.UI.TextServices.ITfProperty), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfPropertyValue(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8ed8981b-7c10-4d7d-9fb3-ab72e9c75f72}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfPropertyValue)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, rgValues: POINTER(win32more.Windows.Win32.UI.TextServices.TF_PROPERTYVAL), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfRanges(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f99d3f40-8e32-11d2-bf46-00105a2799b5}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfRanges)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, ppRange: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRange), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTfUIElements(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{887aa91e-acba-4931-84da-3c5208cf543f}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfUIElements)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, ppElement: POINTER(win32more.Windows.Win32.UI.TextServices.ITfUIElement), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternalDocWrap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e1aa6466-9db4-40ba-be03-77c38e8e60b2}')
    @commethod(3)
    def NotifyRevoke(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
INSERT_TEXT_AT_SELECTION_FLAGS = UInt32
TF_IAS_NOQUERY: win32more.Windows.Win32.UI.TextServices.INSERT_TEXT_AT_SELECTION_FLAGS = 1
TF_IAS_QUERYONLY: win32more.Windows.Win32.UI.TextServices.INSERT_TEXT_AT_SELECTION_FLAGS = 2
TF_IAS_NO_DEFAULT_COMPOSITION: win32more.Windows.Win32.UI.TextServices.INSERT_TEXT_AT_SELECTION_FLAGS = 2147483648
class ISpeechCommandProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{38e09d4c-586d-435a-b592-c8a86691dec6}')
    @commethod(3)
    def EnumSpeechCommands(self, langid: UInt16, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumSpeechCommands)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ProcessCommand(self, pszCommand: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, langid: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStoreACP(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{28888fe3-c2a0-483a-a3ea-8cb1ce51ff3d}')
    @commethod(3)
    def AdviseSink(self, riid: POINTER(Guid), punk: win32more.Windows.Win32.System.Com.IUnknown, dwMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseSink(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RequestLock(self, dwLockFlags: UInt32, phrSession: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(self, pdcs: POINTER(win32more.Windows.Win32.UI.TextServices.TS_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def QueryInsert(self, acpTestStart: Int32, acpTestEnd: Int32, cch: UInt32, pacpResultStart: POINTER(Int32), pacpResultEnd: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSelection(self, ulIndex: UInt32, ulCount: UInt32, pSelection: POINTER(win32more.Windows.Win32.UI.TextServices.TS_SELECTION_ACP), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetSelection(self, ulCount: UInt32, pSelection: POINTER(win32more.Windows.Win32.UI.TextServices.TS_SELECTION_ACP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetText(self, acpStart: Int32, acpEnd: Int32, pchPlain: win32more.Windows.Win32.Foundation.PWSTR, cchPlainReq: UInt32, pcchPlainRet: POINTER(UInt32), prgRunInfo: POINTER(win32more.Windows.Win32.UI.TextServices.TS_RUNINFO), cRunInfoReq: UInt32, pcRunInfoRet: POINTER(UInt32), pacpNext: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetText(self, dwFlags: UInt32, acpStart: Int32, acpEnd: Int32, pchText: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, pChange: POINTER(win32more.Windows.Win32.UI.TextServices.TS_TEXTCHANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFormattedText(self, acpStart: Int32, acpEnd: Int32, ppDataObject: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetEmbedded(self, acpPos: Int32, rguidService: POINTER(Guid), riid: POINTER(Guid), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def QueryInsertEmbedded(self, pguidService: POINTER(Guid), pFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pfInsertable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def InsertEmbedded(self, dwFlags: UInt32, acpStart: Int32, acpEnd: Int32, pDataObject: win32more.Windows.Win32.System.Com.IDataObject, pChange: POINTER(win32more.Windows.Win32.UI.TextServices.TS_TEXTCHANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def InsertTextAtSelection(self, dwFlags: UInt32, pchText: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, pacpStart: POINTER(Int32), pacpEnd: POINTER(Int32), pChange: POINTER(win32more.Windows.Win32.UI.TextServices.TS_TEXTCHANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def InsertEmbeddedAtSelection(self, dwFlags: UInt32, pDataObject: win32more.Windows.Win32.System.Com.IDataObject, pacpStart: POINTER(Int32), pacpEnd: POINTER(Int32), pChange: POINTER(win32more.Windows.Win32.UI.TextServices.TS_TEXTCHANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RequestSupportedAttrs(self, dwFlags: UInt32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def RequestAttrsAtPosition(self, acpPos: Int32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def RequestAttrsTransitioningAtPosition(self, acpPos: Int32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def FindNextAttrTransition(self, acpStart: Int32, acpHalt: Int32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32, pacpNext: POINTER(Int32), pfFound: POINTER(win32more.Windows.Win32.Foundation.BOOL), plFoundOffset: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def RetrieveRequestedAttrs(self, ulCount: UInt32, paAttrVals: POINTER(win32more.Windows.Win32.UI.TextServices.TS_ATTRVAL), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetEndACP(self, pacp: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetActiveView(self, pvcView: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetACPFromPoint(self, vcView: UInt32, ptScreen: POINTER(win32more.Windows.Win32.Foundation.POINT), dwFlags: UInt32, pacp: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetTextExt(self, vcView: UInt32, acpStart: Int32, acpEnd: Int32, prc: POINTER(win32more.Windows.Win32.Foundation.RECT), pfClipped: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetScreenExt(self, vcView: UInt32, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetWnd(self, vcView: UInt32, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStoreACP2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f86ad89f-5fe4-4b8d-bb9f-ef3797a84f1f}')
    @commethod(3)
    def AdviseSink(self, riid: POINTER(Guid), punk: win32more.Windows.Win32.System.Com.IUnknown, dwMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseSink(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RequestLock(self, dwLockFlags: UInt32, phrSession: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(self, pdcs: POINTER(win32more.Windows.Win32.UI.TextServices.TS_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def QueryInsert(self, acpTestStart: Int32, acpTestEnd: Int32, cch: UInt32, pacpResultStart: POINTER(Int32), pacpResultEnd: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSelection(self, ulIndex: UInt32, ulCount: UInt32, pSelection: POINTER(win32more.Windows.Win32.UI.TextServices.TS_SELECTION_ACP), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetSelection(self, ulCount: UInt32, pSelection: POINTER(win32more.Windows.Win32.UI.TextServices.TS_SELECTION_ACP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetText(self, acpStart: Int32, acpEnd: Int32, pchPlain: win32more.Windows.Win32.Foundation.PWSTR, cchPlainReq: UInt32, pcchPlainRet: POINTER(UInt32), prgRunInfo: POINTER(win32more.Windows.Win32.UI.TextServices.TS_RUNINFO), cRunInfoReq: UInt32, pcRunInfoRet: POINTER(UInt32), pacpNext: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetText(self, dwFlags: UInt32, acpStart: Int32, acpEnd: Int32, pchText: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, pChange: POINTER(win32more.Windows.Win32.UI.TextServices.TS_TEXTCHANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFormattedText(self, acpStart: Int32, acpEnd: Int32, ppDataObject: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetEmbedded(self, acpPos: Int32, rguidService: POINTER(Guid), riid: POINTER(Guid), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def QueryInsertEmbedded(self, pguidService: POINTER(Guid), pFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pfInsertable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def InsertEmbedded(self, dwFlags: UInt32, acpStart: Int32, acpEnd: Int32, pDataObject: win32more.Windows.Win32.System.Com.IDataObject, pChange: POINTER(win32more.Windows.Win32.UI.TextServices.TS_TEXTCHANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def InsertTextAtSelection(self, dwFlags: UInt32, pchText: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, pacpStart: POINTER(Int32), pacpEnd: POINTER(Int32), pChange: POINTER(win32more.Windows.Win32.UI.TextServices.TS_TEXTCHANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def InsertEmbeddedAtSelection(self, dwFlags: UInt32, pDataObject: win32more.Windows.Win32.System.Com.IDataObject, pacpStart: POINTER(Int32), pacpEnd: POINTER(Int32), pChange: POINTER(win32more.Windows.Win32.UI.TextServices.TS_TEXTCHANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RequestSupportedAttrs(self, dwFlags: UInt32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def RequestAttrsAtPosition(self, acpPos: Int32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def RequestAttrsTransitioningAtPosition(self, acpPos: Int32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def FindNextAttrTransition(self, acpStart: Int32, acpHalt: Int32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32, pacpNext: POINTER(Int32), pfFound: POINTER(win32more.Windows.Win32.Foundation.BOOL), plFoundOffset: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def RetrieveRequestedAttrs(self, ulCount: UInt32, paAttrVals: POINTER(win32more.Windows.Win32.UI.TextServices.TS_ATTRVAL), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetEndACP(self, pacp: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetActiveView(self, pvcView: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetACPFromPoint(self, vcView: UInt32, ptScreen: POINTER(win32more.Windows.Win32.Foundation.POINT), dwFlags: UInt32, pacp: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetTextExt(self, vcView: UInt32, acpStart: Int32, acpEnd: Int32, prc: POINTER(win32more.Windows.Win32.Foundation.RECT), pfClipped: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetScreenExt(self, vcView: UInt32, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStoreACPEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a2de3bc2-3d8e-11d3-81a9-f753fbe61a00}')
    @commethod(3)
    def ScrollToRect(self, acpStart: Int32, acpEnd: Int32, rc: win32more.Windows.Win32.Foundation.RECT, dwPosition: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStoreACPServices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa80e901-2021-11d2-93e0-0060b067b86e}')
    @commethod(3)
    def Serialize(self, pProp: win32more.Windows.Win32.UI.TextServices.ITfProperty, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, pHdr: POINTER(win32more.Windows.Win32.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP), pStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unserialize(self, pProp: win32more.Windows.Win32.UI.TextServices.ITfProperty, pHdr: POINTER(win32more.Windows.Win32.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP), pStream: win32more.Windows.Win32.System.Com.IStream, pLoader: win32more.Windows.Win32.UI.TextServices.ITfPersistentPropertyLoaderACP) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ForceLoadProperty(self, pProp: win32more.Windows.Win32.UI.TextServices.ITfProperty) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateRange(self, acpStart: Int32, acpEnd: Int32, ppRange: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRangeACP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStoreACPSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{22d44c94-a419-4542-a272-ae26093ececf}')
    @commethod(3)
    def OnTextChange(self, dwFlags: win32more.Windows.Win32.UI.TextServices.TEXT_STORE_TEXT_CHANGE_FLAGS, pChange: POINTER(win32more.Windows.Win32.UI.TextServices.TS_TEXTCHANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSelectionChange(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnLayoutChange(self, lcode: win32more.Windows.Win32.UI.TextServices.TsLayoutCode, vcView: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnStatusChange(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnAttrsChange(self, acpStart: Int32, acpEnd: Int32, cAttrs: UInt32, paAttrs: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnLockGranted(self, dwLockFlags: win32more.Windows.Win32.UI.TextServices.TEXT_STORE_LOCK_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnStartEditTransaction(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnEndEditTransaction(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStoreACPSinkEx(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITextStoreACPSink
    _iid_ = Guid('{2bdf9464-41e2-43e3-950c-a6865ba25cd4}')
    @commethod(11)
    def OnDisconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStoreAnchor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9b2077b0-5f18-4dec-bee9-3cc722f5dfe0}')
    @commethod(3)
    def AdviseSink(self, riid: POINTER(Guid), punk: win32more.Windows.Win32.System.Com.IUnknown, dwMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseSink(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RequestLock(self, dwLockFlags: UInt32, phrSession: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(self, pdcs: POINTER(win32more.Windows.Win32.UI.TextServices.TS_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def QueryInsert(self, paTestStart: win32more.Windows.Win32.UI.TextServices.IAnchor, paTestEnd: win32more.Windows.Win32.UI.TextServices.IAnchor, cch: UInt32, ppaResultStart: POINTER(win32more.Windows.Win32.UI.TextServices.IAnchor), ppaResultEnd: POINTER(win32more.Windows.Win32.UI.TextServices.IAnchor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSelection(self, ulIndex: UInt32, ulCount: UInt32, pSelection: POINTER(win32more.Windows.Win32.UI.TextServices.TS_SELECTION_ANCHOR), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetSelection(self, ulCount: UInt32, pSelection: POINTER(win32more.Windows.Win32.UI.TextServices.TS_SELECTION_ANCHOR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetText(self, dwFlags: UInt32, paStart: win32more.Windows.Win32.UI.TextServices.IAnchor, paEnd: win32more.Windows.Win32.UI.TextServices.IAnchor, pchText: win32more.Windows.Win32.Foundation.PWSTR, cchReq: UInt32, pcch: POINTER(UInt32), fUpdateAnchor: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetText(self, dwFlags: UInt32, paStart: win32more.Windows.Win32.UI.TextServices.IAnchor, paEnd: win32more.Windows.Win32.UI.TextServices.IAnchor, pchText: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFormattedText(self, paStart: win32more.Windows.Win32.UI.TextServices.IAnchor, paEnd: win32more.Windows.Win32.UI.TextServices.IAnchor, ppDataObject: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetEmbedded(self, dwFlags: UInt32, paPos: win32more.Windows.Win32.UI.TextServices.IAnchor, rguidService: POINTER(Guid), riid: POINTER(Guid), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def InsertEmbedded(self, dwFlags: UInt32, paStart: win32more.Windows.Win32.UI.TextServices.IAnchor, paEnd: win32more.Windows.Win32.UI.TextServices.IAnchor, pDataObject: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RequestSupportedAttrs(self, dwFlags: UInt32, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RequestAttrsAtPosition(self, paPos: win32more.Windows.Win32.UI.TextServices.IAnchor, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RequestAttrsTransitioningAtPosition(self, paPos: win32more.Windows.Win32.UI.TextServices.IAnchor, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def FindNextAttrTransition(self, paStart: win32more.Windows.Win32.UI.TextServices.IAnchor, paHalt: win32more.Windows.Win32.UI.TextServices.IAnchor, cFilterAttrs: UInt32, paFilterAttrs: POINTER(Guid), dwFlags: UInt32, pfFound: POINTER(win32more.Windows.Win32.Foundation.BOOL), plFoundOffset: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def RetrieveRequestedAttrs(self, ulCount: UInt32, paAttrVals: POINTER(win32more.Windows.Win32.UI.TextServices.TS_ATTRVAL), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetStart(self, ppaStart: POINTER(win32more.Windows.Win32.UI.TextServices.IAnchor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetEnd(self, ppaEnd: POINTER(win32more.Windows.Win32.UI.TextServices.IAnchor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetActiveView(self, pvcView: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetAnchorFromPoint(self, vcView: UInt32, ptScreen: POINTER(win32more.Windows.Win32.Foundation.POINT), dwFlags: UInt32, ppaSite: POINTER(win32more.Windows.Win32.UI.TextServices.IAnchor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetTextExt(self, vcView: UInt32, paStart: win32more.Windows.Win32.UI.TextServices.IAnchor, paEnd: win32more.Windows.Win32.UI.TextServices.IAnchor, prc: POINTER(win32more.Windows.Win32.Foundation.RECT), pfClipped: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetScreenExt(self, vcView: UInt32, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetWnd(self, vcView: UInt32, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def QueryInsertEmbedded(self, pguidService: POINTER(Guid), pFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pfInsertable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def InsertTextAtSelection(self, dwFlags: UInt32, pchText: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, ppaStart: POINTER(win32more.Windows.Win32.UI.TextServices.IAnchor), ppaEnd: POINTER(win32more.Windows.Win32.UI.TextServices.IAnchor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def InsertEmbeddedAtSelection(self, dwFlags: UInt32, pDataObject: win32more.Windows.Win32.System.Com.IDataObject, ppaStart: POINTER(win32more.Windows.Win32.UI.TextServices.IAnchor), ppaEnd: POINTER(win32more.Windows.Win32.UI.TextServices.IAnchor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStoreAnchorEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a2de3bc1-3d8e-11d3-81a9-f753fbe61a00}')
    @commethod(3)
    def ScrollToRect(self, pStart: win32more.Windows.Win32.UI.TextServices.IAnchor, pEnd: win32more.Windows.Win32.UI.TextServices.IAnchor, rc: win32more.Windows.Win32.Foundation.RECT, dwPosition: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStoreAnchorSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa80e905-2021-11d2-93e0-0060b067b86e}')
    @commethod(3)
    def OnTextChange(self, dwFlags: win32more.Windows.Win32.UI.TextServices.TEXT_STORE_CHANGE_FLAGS, paStart: win32more.Windows.Win32.UI.TextServices.IAnchor, paEnd: win32more.Windows.Win32.UI.TextServices.IAnchor) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnSelectionChange(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnLayoutChange(self, lcode: win32more.Windows.Win32.UI.TextServices.TsLayoutCode, vcView: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnStatusChange(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnAttrsChange(self, paStart: win32more.Windows.Win32.UI.TextServices.IAnchor, paEnd: win32more.Windows.Win32.UI.TextServices.IAnchor, cAttrs: UInt32, paAttrs: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnLockGranted(self, dwLockFlags: win32more.Windows.Win32.UI.TextServices.TEXT_STORE_LOCK_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnStartEditTransaction(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnEndEditTransaction(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStoreSinkAnchorEx(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITextStoreAnchorSink
    _iid_ = Guid('{25642426-028d-4474-977b-111bb114fe3e}')
    @commethod(11)
    def OnDisconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfActiveLanguageProfileNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b246cb75-a93e-4652-bf8c-b3fe0cfd7e57}')
    @commethod(3)
    def OnActivated(self, clsid: POINTER(Guid), guidProfile: POINTER(Guid), fActivated: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfCandidateList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a3ad50fb-9bdb-49e3-a843-6c76520fbf5d}')
    @commethod(3)
    def EnumCandidates(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfCandidates)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCandidate(self, nIndex: UInt32, ppCand: POINTER(win32more.Windows.Win32.UI.TextServices.ITfCandidateString)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCandidateNum(self, pnCnt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetResult(self, nIndex: UInt32, imcr: win32more.Windows.Win32.UI.TextServices.TfCandidateResult) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfCandidateListUIElement(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfUIElement
    _iid_ = Guid('{ea1ea138-19df-11d7-a6d2-00065b84435c}')
    @commethod(7)
    def GetUpdatedFlags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDocumentMgr(self, ppdim: POINTER(win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCount(self, puCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSelection(self, puIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetString(self, uIndex: UInt32, pstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPageIndex(self, pIndex: POINTER(UInt32), uSize: UInt32, puPageCnt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetPageIndex(self, pIndex: POINTER(UInt32), uPageCnt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCurrentPage(self, puPage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfCandidateListUIElementBehavior(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfCandidateListUIElement
    _iid_ = Guid('{85fad185-58ce-497a-9460-355366b64b9a}')
    @commethod(15)
    def SetSelection(self, nIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Finalize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Abort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfCandidateString(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{581f317e-fd9d-443f-b972-ed00467c5d40}')
    @commethod(3)
    def GetString(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIndex(self, pnIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfCategoryMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c3acefb5-f69d-4905-938f-fcadcf4be830}')
    @commethod(3)
    def RegisterCategory(self, rclsid: POINTER(Guid), rcatid: POINTER(Guid), rguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterCategory(self, rclsid: POINTER(Guid), rcatid: POINTER(Guid), rguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumCategoriesInItem(self, rguid: POINTER(Guid), ppEnum: POINTER(win32more.Windows.Win32.System.Com.IEnumGUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumItemsInCategory(self, rcatid: POINTER(Guid), ppEnum: POINTER(win32more.Windows.Win32.System.Com.IEnumGUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindClosestCategory(self, rguid: POINTER(Guid), pcatid: POINTER(Guid), ppcatidList: POINTER(POINTER(Guid)), ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterGUIDDescription(self, rclsid: POINTER(Guid), rguid: POINTER(Guid), pchDesc: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnregisterGUIDDescription(self, rclsid: POINTER(Guid), rguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetGUIDDescription(self, rguid: POINTER(Guid), pbstrDesc: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RegisterGUIDDWORD(self, rclsid: POINTER(Guid), rguid: POINTER(Guid), dw: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UnregisterGUIDDWORD(self, rclsid: POINTER(Guid), rguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetGUIDDWORD(self, rguid: POINTER(Guid), pdw: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RegisterGUID(self, rguid: POINTER(Guid), pguidatom: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetGUID(self, guidatom: UInt32, pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def IsEqualTfGuidAtom(self, guidatom: UInt32, rguid: POINTER(Guid), pfEqual: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfCleanupContextDurationSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{45c35144-154e-4797-bed8-d33ae7bf8794}')
    @commethod(3)
    def OnStartCleanupContext(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnEndCleanupContext(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfCleanupContextSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{01689689-7acb-4e9b-ab7c-7ea46b12b522}')
    @commethod(3)
    def OnCleanupContext(self, ecWrite: UInt32, pic: win32more.Windows.Win32.UI.TextServices.ITfContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfClientId(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d60a7b49-1b9f-4be2-b702-47e9dc05dec3}')
    @commethod(3)
    def GetClientId(self, rclsid: POINTER(Guid), ptid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfCompartment(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb08f7a9-607a-4384-8623-056892b64371}')
    @commethod(3)
    def SetValue(self, tid: UInt32, pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(self, pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfCompartmentEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{743abd5f-f26d-48df-8cc5-238492419b64}')
    @commethod(3)
    def OnChange(self, rguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfCompartmentMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7dcf57ac-18ad-438b-824d-979bffb74b7c}')
    @commethod(3)
    def GetCompartment(self, rguid: POINTER(Guid), ppcomp: POINTER(win32more.Windows.Win32.UI.TextServices.ITfCompartment)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ClearCompartment(self, tid: UInt32, rguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumCompartments(self, ppEnum: POINTER(win32more.Windows.Win32.System.Com.IEnumGUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfComposition(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{20168d64-5a8f-4a5a-b7bd-cfa29f4d0fd9}')
    @commethod(3)
    def GetRange(self, ppRange: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShiftStart(self, ecWrite: UInt32, pNewStart: win32more.Windows.Win32.UI.TextServices.ITfRange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ShiftEnd(self, ecWrite: UInt32, pNewEnd: win32more.Windows.Win32.UI.TextServices.ITfRange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndComposition(self, ecWrite: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfCompositionSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a781718c-579a-4b15-a280-32b8577acc5e}')
    @commethod(3)
    def OnCompositionTerminated(self, ecWrite: UInt32, pComposition: win32more.Windows.Win32.UI.TextServices.ITfComposition) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfCompositionView(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d7540241-f9a1-4364-befc-dbcd2c4395b7}')
    @commethod(3)
    def GetOwnerClsid(self, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRange(self, ppRange: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfConfigureSystemKeystrokeFeed(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0d2c969a-bc9c-437c-84ee-951c49b1a764}')
    @commethod(3)
    def DisableSystemKeystrokeFeed(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnableSystemKeystrokeFeed(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa80e7fd-2021-11d2-93e0-0060b067b86e}')
    @commethod(3)
    def RequestEditSession(self, tid: UInt32, pes: win32more.Windows.Win32.UI.TextServices.ITfEditSession, dwFlags: win32more.Windows.Win32.UI.TextServices.TF_CONTEXT_EDIT_CONTEXT_FLAGS, phrSession: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InWriteSession(self, tid: UInt32, pfWriteSession: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSelection(self, ec: UInt32, ulIndex: UInt32, ulCount: UInt32, pSelection: POINTER(win32more.Windows.Win32.UI.TextServices.TF_SELECTION), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetSelection(self, ec: UInt32, ulCount: UInt32, pSelection: POINTER(win32more.Windows.Win32.UI.TextServices.TF_SELECTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStart(self, ec: UInt32, ppStart: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetEnd(self, ec: UInt32, ppEnd: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetActiveView(self, ppView: POINTER(win32more.Windows.Win32.UI.TextServices.ITfContextView)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumViews(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfContextViews)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetStatus(self, pdcs: POINTER(win32more.Windows.Win32.UI.TextServices.TS_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetProperty(self, guidProp: POINTER(Guid), ppProp: POINTER(win32more.Windows.Win32.UI.TextServices.ITfProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetAppProperty(self, guidProp: POINTER(Guid), ppProp: POINTER(win32more.Windows.Win32.UI.TextServices.ITfReadOnlyProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def TrackProperties(self, prgProp: POINTER(POINTER(Guid)), cProp: UInt32, prgAppProp: POINTER(POINTER(Guid)), cAppProp: UInt32, ppProperty: POINTER(win32more.Windows.Win32.UI.TextServices.ITfReadOnlyProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def EnumProperties(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfProperties)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetDocumentMgr(self, ppDm: POINTER(win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateRangeBackup(self, ec: UInt32, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, ppBackup: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRangeBackup)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfContextComposition(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d40c8aae-ac92-4fc7-9a11-0ee0e23aa39b}')
    @commethod(3)
    def StartComposition(self, ecWrite: UInt32, pCompositionRange: win32more.Windows.Win32.UI.TextServices.ITfRange, pSink: win32more.Windows.Win32.UI.TextServices.ITfCompositionSink, ppComposition: POINTER(win32more.Windows.Win32.UI.TextServices.ITfComposition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumCompositions(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumITfCompositionView)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindComposition(self, ecRead: UInt32, pTestRange: win32more.Windows.Win32.UI.TextServices.ITfRange, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumITfCompositionView)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TakeOwnership(self, ecWrite: UInt32, pComposition: win32more.Windows.Win32.UI.TextServices.ITfCompositionView, pSink: win32more.Windows.Win32.UI.TextServices.ITfCompositionSink, ppComposition: POINTER(win32more.Windows.Win32.UI.TextServices.ITfComposition)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfContextKeyEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0552ba5d-c835-4934-bf50-846aaa67432f}')
    @commethod(3)
    def OnKeyDown(self, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnKeyUp(self, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnTestKeyDown(self, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnTestKeyUp(self, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfContextOwner(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa80e80c-2021-11d2-93e0-0060b067b86e}')
    @commethod(3)
    def GetACPFromPoint(self, ptScreen: POINTER(win32more.Windows.Win32.Foundation.POINT), dwFlags: UInt32, pacp: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTextExt(self, acpStart: Int32, acpEnd: Int32, prc: POINTER(win32more.Windows.Win32.Foundation.RECT), pfClipped: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetScreenExt(self, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStatus(self, pdcs: POINTER(win32more.Windows.Win32.UI.TextServices.TS_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetWnd(self, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAttribute(self, rguidAttribute: POINTER(Guid), pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfContextOwnerCompositionServices(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfContextComposition
    _iid_ = Guid('{86462810-593b-4916-9764-19c08e9ce110}')
    @commethod(7)
    def TerminateComposition(self, pComposition: win32more.Windows.Win32.UI.TextServices.ITfCompositionView) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfContextOwnerCompositionSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5f20aa40-b57a-4f34-96ab-3576f377cc79}')
    @commethod(3)
    def OnStartComposition(self, pComposition: win32more.Windows.Win32.UI.TextServices.ITfCompositionView, pfOk: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnUpdateComposition(self, pComposition: win32more.Windows.Win32.UI.TextServices.ITfCompositionView, pRangeNew: win32more.Windows.Win32.UI.TextServices.ITfRange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnEndComposition(self, pComposition: win32more.Windows.Win32.UI.TextServices.ITfCompositionView) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfContextOwnerServices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b23eb630-3e1c-11d3-a745-0050040ab407}')
    @commethod(3)
    def OnLayoutChange(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnStatusChange(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnAttributeChange(self, rguidAttribute: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Serialize(self, pProp: win32more.Windows.Win32.UI.TextServices.ITfProperty, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, pHdr: POINTER(win32more.Windows.Win32.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP), pStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Unserialize(self, pProp: win32more.Windows.Win32.UI.TextServices.ITfProperty, pHdr: POINTER(win32more.Windows.Win32.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP), pStream: win32more.Windows.Win32.System.Com.IStream, pLoader: win32more.Windows.Win32.UI.TextServices.ITfPersistentPropertyLoaderACP) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ForceLoadProperty(self, pProp: win32more.Windows.Win32.UI.TextServices.ITfProperty) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateRange(self, acpStart: Int32, acpEnd: Int32, ppRange: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRangeACP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfContextView(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2433bf8e-0f9b-435c-ba2c-180611978c30}')
    @commethod(3)
    def GetRangeFromPoint(self, ec: UInt32, ppt: POINTER(win32more.Windows.Win32.Foundation.POINT), dwFlags: UInt32, ppRange: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTextExt(self, ec: UInt32, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, prc: POINTER(win32more.Windows.Win32.Foundation.RECT), pfClipped: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetScreenExt(self, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetWnd(self, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfCreatePropertyStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2463fbf0-b0af-11d2-afc5-00105a2799b5}')
    @commethod(3)
    def IsStoreSerializable(self, guidProp: POINTER(Guid), pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, pPropStore: win32more.Windows.Win32.UI.TextServices.ITfPropertyStore, pfSerializable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreatePropertyStore(self, guidProp: POINTER(Guid), pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, cb: UInt32, pStream: win32more.Windows.Win32.System.Com.IStream, ppStore: POINTER(win32more.Windows.Win32.UI.TextServices.ITfPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfDisplayAttributeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{70528852-2f26-4aea-8c96-215150578932}')
    @commethod(3)
    def GetGUID(self, pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(self, pbstrDesc: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAttributeInfo(self, pda: POINTER(win32more.Windows.Win32.UI.TextServices.TF_DISPLAYATTRIBUTE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAttributeInfo(self, pda: POINTER(win32more.Windows.Win32.UI.TextServices.TF_DISPLAYATTRIBUTE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfDisplayAttributeMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8ded7393-5db1-475c-9e71-a39111b0ff67}')
    @commethod(3)
    def OnUpdateInfo(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumDisplayAttributeInfo(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfDisplayAttributeInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDisplayAttributeInfo(self, guid: POINTER(Guid), ppInfo: POINTER(win32more.Windows.Win32.UI.TextServices.ITfDisplayAttributeInfo), pclsidOwner: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfDisplayAttributeNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ad56f402-e162-4f25-908f-7d577cf9bda9}')
    @commethod(3)
    def OnUpdateInfo(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfDisplayAttributeProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fee47777-163c-4769-996a-6e9c50ad8f54}')
    @commethod(3)
    def EnumDisplayAttributeInfo(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfDisplayAttributeInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDisplayAttributeInfo(self, guid: POINTER(Guid), ppInfo: POINTER(win32more.Windows.Win32.UI.TextServices.ITfDisplayAttributeInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfDocumentMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa80e7f4-2021-11d2-93e0-0060b067b86e}')
    @commethod(3)
    def CreateContext(self, tidOwner: UInt32, dwFlags: UInt32, punk: win32more.Windows.Win32.System.Com.IUnknown, ppic: POINTER(win32more.Windows.Win32.UI.TextServices.ITfContext), pecTextStore: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Push(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Pop(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTop(self, ppic: POINTER(win32more.Windows.Win32.UI.TextServices.ITfContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetBase(self, ppic: POINTER(win32more.Windows.Win32.UI.TextServices.ITfContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumContexts(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfContexts)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfEditRecord(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{42d4d099-7c1a-4a89-b836-6c6f22160df0}')
    @commethod(3)
    def GetSelectionStatus(self, pfChanged: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTextAndPropertyUpdates(self, dwFlags: win32more.Windows.Win32.UI.TextServices.GET_TEXT_AND_PROPERTY_UPDATES_FLAGS, prgProperties: POINTER(POINTER(Guid)), cProperties: UInt32, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfRanges)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfEditSession(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa80e803-2021-11d2-93e0-0060b067b86e}')
    @commethod(3)
    def DoEditSession(self, ec: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfEditTransactionSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{708fbf70-b520-416b-b06c-2c41ab44f8ba}')
    @commethod(3)
    def OnStartEditTransaction(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnEndEditTransaction(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnAdviseText(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{3527268b-7d53-4dd9-92b7-7296ae461249}')
    @commethod(4)
    def OnTextUpdate(self, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, pchText: win32more.Windows.Win32.Foundation.PWSTR, cch: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnLatticeUpdate(self, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, pLattice: win32more.Windows.Win32.UI.TextServices.ITfLMLattice) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnBalloon(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3bab89e4-5fbe-45f4-a5bc-dca36ad225a8}')
    @commethod(3)
    def UpdateBalloon(self, style: win32more.Windows.Win32.UI.TextServices.TfLBBalloonStyle, pch: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnConfigure(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{88f567c6-1757-49f8-a1b2-89234c1eeff9}')
    @commethod(4)
    def Show(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, langid: UInt16, rguidProfile: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnConfigureRegisterEudc(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{b5e26ff5-d7ad-4304-913f-21a2ed95a1b0}')
    @commethod(4)
    def Show(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, langid: UInt16, rguidProfile: POINTER(Guid), bstrRegistered: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnConfigureRegisterWord(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{bb95808a-6d8f-4bca-8400-5390b586aedf}')
    @commethod(4)
    def Show(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, langid: UInt16, rguidProfile: POINTER(Guid), bstrRegistered: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnCustomSpeechCommand(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{fca6c349-a12f-43a3-8dd6-5a5a4282577b}')
    @commethod(4)
    def SetSpeechCommandProvider(self, pspcmdProvider: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnGetLinguisticAlternates(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{ea163ce2-7a65-4506-82a3-c528215da64e}')
    @commethod(4)
    def GetAlternates(self, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, ppCandidateList: POINTER(win32more.Windows.Win32.UI.TextServices.ITfCandidateList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnGetPreferredTouchKeyboardLayout(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{5f309a41-590a-4acc-a97f-d8efff13fdfc}')
    @commethod(4)
    def GetLayout(self, pTKBLayoutType: POINTER(win32more.Windows.Win32.UI.TextServices.TKBLayoutType), pwPreferredLayoutId: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnGetSAPIObject(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{5c0ab7ea-167d-4f59-bfb5-4693755e90ca}')
    @commethod(4)
    def Get(self, sObj: win32more.Windows.Win32.UI.TextServices.TfSapiObject, ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnLMInternal(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFnLMProcessor
    _iid_ = Guid('{04b825b1-ac9a-4f7b-b5ad-c7168f1ee445}')
    @commethod(11)
    def ProcessLattice(self, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnLMProcessor(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{7afbf8e7-ac4b-4082-b058-890899d3a010}')
    @commethod(4)
    def QueryRange(self, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, ppNewRange: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRange), pfAccepted: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryLangID(self, langid: UInt16, pfAccepted: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetReconversion(self, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, ppCandList: POINTER(win32more.Windows.Win32.UI.TextServices.ITfCandidateList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Reconvert(self, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def QueryKey(self, fUp: win32more.Windows.Win32.Foundation.BOOL, vKey: win32more.Windows.Win32.Foundation.WPARAM, lparamKeydata: win32more.Windows.Win32.Foundation.LPARAM, pfInterested: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def InvokeKey(self, fUp: win32more.Windows.Win32.Foundation.BOOL, vKey: win32more.Windows.Win32.Foundation.WPARAM, lparamKeyData: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def InvokeFunc(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext, refguidFunc: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnLangProfileUtil(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{a87a8574-a6c1-4e15-99f0-3d3965f548eb}')
    @commethod(4)
    def RegisterActiveProfiles(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsProfileAvailableForLang(self, langid: UInt16, pfAvailable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnPlayBack(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{a3a416a4-0f64-11d3-b5b7-00c04fc324a1}')
    @commethod(4)
    def QueryRange(self, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, ppNewRange: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRange), pfPlayable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Play(self, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnPropertyUIStatus(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{2338ac6e-2b9d-44c0-a75e-ee64f256b3bd}')
    @commethod(4)
    def GetStatus(self, refguidProp: POINTER(Guid), pdw: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetStatus(self, refguidProp: POINTER(Guid), dw: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnReconversion(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{4cea93c0-0a58-11d3-8df0-00105a2799b5}')
    @commethod(4)
    def QueryRange(self, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, ppNewRange: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRange), pfConvertable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetReconversion(self, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, ppCandList: POINTER(win32more.Windows.Win32.UI.TextServices.ITfCandidateList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Reconvert(self, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnSearchCandidateProvider(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{87a2ad8f-f27b-4920-8501-67602280175d}')
    @commethod(4)
    def GetSearchCandidates(self, bstrQuery: win32more.Windows.Win32.Foundation.BSTR, bstrApplicationId: win32more.Windows.Win32.Foundation.BSTR, pplist: POINTER(win32more.Windows.Win32.UI.TextServices.ITfCandidateList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetResult(self, bstrQuery: win32more.Windows.Win32.Foundation.BSTR, bstrApplicationID: win32more.Windows.Win32.Foundation.BSTR, bstrResult: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFnShowHelp(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfFunction
    _iid_ = Guid('{5ab1d30c-094d-4c29-8ea5-0bf59be87bf3}')
    @commethod(4)
    def Show(self, hwndParent: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFunction(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{db593490-098f-11d3-8df0-00105a2799b5}')
    @commethod(3)
    def GetDisplayName(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfFunctionProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{101d6610-0990-11d3-8df0-00105a2799b5}')
    @commethod(3)
    def GetType(self, pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(self, pbstrDesc: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFunction(self, rguid: POINTER(Guid), riid: POINTER(Guid), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfInputProcessorProfileActivationSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71c6e74e-0f28-11d8-a82a-00065b84435c}')
    @commethod(3)
    def OnActivated(self, dwProfileType: UInt32, langid: UInt16, clsid: POINTER(Guid), catid: POINTER(Guid), guidProfile: POINTER(Guid), hkl: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfInputProcessorProfileMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71c6e74c-0f28-11d8-a82a-00065b84435c}')
    @commethod(3)
    def ActivateProfile(self, dwProfileType: UInt32, langid: UInt16, clsid: POINTER(Guid), guidProfile: POINTER(Guid), hkl: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeactivateProfile(self, dwProfileType: UInt32, langid: UInt16, clsid: POINTER(Guid), guidProfile: POINTER(Guid), hkl: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProfile(self, dwProfileType: UInt32, langid: UInt16, clsid: POINTER(Guid), guidProfile: POINTER(Guid), hkl: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, pProfile: POINTER(win32more.Windows.Win32.UI.TextServices.TF_INPUTPROCESSORPROFILE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumProfiles(self, langid: UInt16, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfInputProcessorProfiles)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ReleaseInputProcessor(self, rclsid: POINTER(Guid), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterProfile(self, rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), pchDesc: win32more.Windows.Win32.Foundation.PWSTR, cchDesc: UInt32, pchIconFile: win32more.Windows.Win32.Foundation.PWSTR, cchFile: UInt32, uIconIndex: UInt32, hklsubstitute: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, dwPreferredLayout: UInt32, bEnabledByDefault: win32more.Windows.Win32.Foundation.BOOL, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnregisterProfile(self, rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetActiveProfile(self, catid: POINTER(Guid), pProfile: POINTER(win32more.Windows.Win32.UI.TextServices.TF_INPUTPROCESSORPROFILE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfInputProcessorProfileSubstituteLayout(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4fd67194-1002-4513-bff2-c0ddf6258552}')
    @commethod(3)
    def GetSubstituteKeyboardLayout(self, rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), phKL: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfInputProcessorProfiles(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1f02b6c5-7842-4ee6-8a0b-9a24183a95ca}')
    @commethod(3)
    def Register(self, rclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unregister(self, rclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddLanguageProfile(self, rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), pchDesc: win32more.Windows.Win32.Foundation.PWSTR, cchDesc: UInt32, pchIconFile: win32more.Windows.Win32.Foundation.PWSTR, cchFile: UInt32, uIconIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveLanguageProfile(self, rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumInputProcessorInfo(self, ppEnum: POINTER(win32more.Windows.Win32.System.Com.IEnumGUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDefaultLanguageProfile(self, langid: UInt16, catid: POINTER(Guid), pclsid: POINTER(Guid), pguidProfile: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetDefaultLanguageProfile(self, langid: UInt16, rclsid: POINTER(Guid), guidProfiles: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ActivateLanguageProfile(self, rclsid: POINTER(Guid), langid: UInt16, guidProfiles: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetActiveLanguageProfile(self, rclsid: POINTER(Guid), plangid: POINTER(UInt16), pguidProfile: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLanguageProfileDescription(self, rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), pbstrProfile: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCurrentLanguage(self, plangid: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ChangeCurrentLanguage(self, langid: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetLanguageList(self, ppLangId: POINTER(POINTER(UInt16)), pulCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EnumLanguageProfiles(self, langid: UInt16, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfLanguageProfiles)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnableLanguageProfile(self, rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def IsEnabledLanguageProfile(self, rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), pfEnable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def EnableLanguageProfileByDefault(self, rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SubstituteKeyboardLayout(self, rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfInputProcessorProfilesEx(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfInputProcessorProfiles
    _iid_ = Guid('{892f230f-fe00-4a41-a98e-fcd6de0d35ef}')
    @commethod(21)
    def SetLanguageProfileDisplayName(self, rclsid: POINTER(Guid), langid: UInt16, guidProfile: POINTER(Guid), pchFile: win32more.Windows.Win32.Foundation.PWSTR, cchFile: UInt32, uResId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfInputScope(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fde1eaee-6924-4cdf-91e7-da38cff5559d}')
    @commethod(3)
    def GetInputScopes(self, pprgInputScopes: POINTER(POINTER(win32more.Windows.Win32.UI.TextServices.InputScope)), pcCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPhrase(self, ppbstrPhrases: POINTER(POINTER(win32more.Windows.Win32.Foundation.BSTR)), pcCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetRegularExpression(self, pbstrRegExp: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSRGS(self, pbstrSRGS: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetXML(self, pbstrXML: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfInputScope2(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfInputScope
    _iid_ = Guid('{5731eaa0-6bc2-4681-a532-92fbb74d7c41}')
    @commethod(8)
    def EnumWordList(self, ppEnumString: POINTER(win32more.Windows.Win32.System.Com.IEnumString)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfInsertAtSelection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{55ce16ba-3014-41c1-9ceb-fade1446ac6c}')
    @commethod(3)
    def InsertTextAtSelection(self, ec: UInt32, dwFlags: win32more.Windows.Win32.UI.TextServices.INSERT_TEXT_AT_SELECTION_FLAGS, pchText: win32more.Windows.Win32.Foundation.PWSTR, cch: Int32, ppRange: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InsertEmbeddedAtSelection(self, ec: UInt32, dwFlags: UInt32, pDataObject: win32more.Windows.Win32.System.Com.IDataObject, ppRange: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfIntegratableCandidateListUIElement(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c7a6f54f-b180-416f-b2bf-7bf2e4683d7b}')
    @commethod(3)
    def SetIntegrationStyle(self, guidIntegrationStyle: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSelectionStyle(self, ptfSelectionStyle: POINTER(win32more.Windows.Win32.UI.TextServices.TfIntegratableCandidateListSelectionStyle)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnKeyDown(self, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ShowCandidateNumbers(self, pfShow: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FinalizeExactCompositionString(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfKeyEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa80e7f5-2021-11d2-93e0-0060b067b86e}')
    @commethod(3)
    def OnSetFocus(self, fForeground: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnTestKeyDown(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnTestKeyUp(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnKeyDown(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnKeyUp(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnPreservedKey(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext, rguid: POINTER(Guid), pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfKeyTraceEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1cd4c13b-1c36-4191-a70a-7f3e611f367d}')
    @commethod(3)
    def OnKeyTraceDown(self, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnKeyTraceUp(self, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfKeystrokeMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa80e7f0-2021-11d2-93e0-0060b067b86e}')
    @commethod(3)
    def AdviseKeyEventSink(self, tid: UInt32, pSink: win32more.Windows.Win32.UI.TextServices.ITfKeyEventSink, fForeground: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseKeyEventSink(self, tid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetForeground(self, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TestKeyDown(self, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def TestKeyUp(self, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def KeyDown(self, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def KeyUp(self, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPreservedKey(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext, pprekey: POINTER(win32more.Windows.Win32.UI.TextServices.TF_PRESERVEDKEY), pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsPreservedKey(self, rguid: POINTER(Guid), pprekey: POINTER(win32more.Windows.Win32.UI.TextServices.TF_PRESERVEDKEY), pfRegistered: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def PreserveKey(self, tid: UInt32, rguid: POINTER(Guid), prekey: POINTER(win32more.Windows.Win32.UI.TextServices.TF_PRESERVEDKEY), pchDesc: win32more.Windows.Win32.Foundation.PWSTR, cchDesc: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def UnpreserveKey(self, rguid: POINTER(Guid), pprekey: POINTER(win32more.Windows.Win32.UI.TextServices.TF_PRESERVEDKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetPreservedKeyDescription(self, rguid: POINTER(Guid), pchDesc: win32more.Windows.Win32.Foundation.PWSTR, cchDesc: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetPreservedKeyDescription(self, rguid: POINTER(Guid), pbstrDesc: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SimulatePreservedKey(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext, rguid: POINTER(Guid), pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfLMLattice(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d4236675-a5bf-4570-9d42-5d6d7b02d59b}')
    @commethod(3)
    def QueryType(self, rguidType: POINTER(Guid), pfSupported: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumLatticeElements(self, dwFrameStart: UInt32, rguidType: POINTER(Guid), ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfLatticeElements)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfLangBarEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{18a4e900-e0ae-11d2-afdd-00105a2799b5}')
    @commethod(3)
    def OnSetFocus(self, dwThreadId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnThreadTerminate(self, dwThreadId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnThreadItemChange(self, dwThreadId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnModalInput(self, dwThreadId: UInt32, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowFloating(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetItemFloatingRect(self, dwThreadId: UInt32, rguid: POINTER(Guid), prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfLangBarItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{73540d69-edeb-4ee9-96c9-23aa30b25916}')
    @commethod(3)
    def GetInfo(self, pInfo: POINTER(win32more.Windows.Win32.UI.TextServices.TF_LANGBARITEMINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetStatus(self, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Show(self, fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTooltipString(self, pbstrToolTip: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfLangBarItemBalloon(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfLangBarItem
    _iid_ = Guid('{01c2d285-d3c7-4b7b-b5b5-d97411d0c283}')
    @commethod(7)
    def OnClick(self, click: win32more.Windows.Win32.UI.TextServices.TfLBIClick, pt: win32more.Windows.Win32.Foundation.POINT, prcArea: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPreferredSize(self, pszDefault: POINTER(win32more.Windows.Win32.Foundation.SIZE), psz: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetBalloonInfo(self, pInfo: POINTER(win32more.Windows.Win32.UI.TextServices.TF_LBBALLOONINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfLangBarItemBitmap(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfLangBarItem
    _iid_ = Guid('{73830352-d722-4179-ada5-f045c98df355}')
    @commethod(7)
    def OnClick(self, click: win32more.Windows.Win32.UI.TextServices.TfLBIClick, pt: win32more.Windows.Win32.Foundation.POINT, prcArea: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPreferredSize(self, pszDefault: POINTER(win32more.Windows.Win32.Foundation.SIZE), psz: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DrawBitmap(self, bmWidth: Int32, bmHeight: Int32, dwFlags: UInt32, phbmp: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP), phbmpMask: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfLangBarItemBitmapButton(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfLangBarItem
    _iid_ = Guid('{a26a0525-3fae-4fa0-89ee-88a964f9f1b5}')
    @commethod(7)
    def OnClick(self, click: win32more.Windows.Win32.UI.TextServices.TfLBIClick, pt: win32more.Windows.Win32.Foundation.POINT, prcArea: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InitMenu(self, pMenu: win32more.Windows.Win32.UI.TextServices.ITfMenu) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnMenuSelect(self, wID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPreferredSize(self, pszDefault: POINTER(win32more.Windows.Win32.Foundation.SIZE), psz: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DrawBitmap(self, bmWidth: Int32, bmHeight: Int32, dwFlags: UInt32, phbmp: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP), phbmpMask: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetText(self, pbstrText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfLangBarItemButton(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfLangBarItem
    _iid_ = Guid('{28c7f1d0-de25-11d2-afdd-00105a2799b5}')
    @commethod(7)
    def OnClick(self, click: win32more.Windows.Win32.UI.TextServices.TfLBIClick, pt: win32more.Windows.Win32.Foundation.POINT, prcArea: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InitMenu(self, pMenu: win32more.Windows.Win32.UI.TextServices.ITfMenu) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnMenuSelect(self, wID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetIcon(self, phIcon: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetText(self, pbstrText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfLangBarItemMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ba468c55-9956-4fb1-a59d-52a7dd7cc6aa}')
    @commethod(3)
    def EnumItems(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfLangBarItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(self, rguid: POINTER(Guid), ppItem: POINTER(win32more.Windows.Win32.UI.TextServices.ITfLangBarItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddItem(self, punk: win32more.Windows.Win32.UI.TextServices.ITfLangBarItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveItem(self, punk: win32more.Windows.Win32.UI.TextServices.ITfLangBarItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AdviseItemSink(self, punk: win32more.Windows.Win32.UI.TextServices.ITfLangBarItemSink, pdwCookie: POINTER(UInt32), rguidItem: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UnadviseItemSink(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetItemFloatingRect(self, dwThreadId: UInt32, rguid: POINTER(Guid), prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetItemsStatus(self, ulCount: UInt32, prgguid: POINTER(Guid), pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetItemNum(self, pulCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetItems(self, ulCount: UInt32, ppItem: POINTER(win32more.Windows.Win32.UI.TextServices.ITfLangBarItem), pInfo: POINTER(win32more.Windows.Win32.UI.TextServices.TF_LANGBARITEMINFO), pdwStatus: POINTER(UInt32), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AdviseItemsSink(self, ulCount: UInt32, ppunk: POINTER(win32more.Windows.Win32.UI.TextServices.ITfLangBarItemSink), pguidItem: POINTER(Guid), pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UnadviseItemsSink(self, ulCount: UInt32, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfLangBarItemSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{57dbe1a0-de25-11d2-afdd-00105a2799b5}')
    @commethod(3)
    def OnUpdate(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfLangBarMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{87955690-e627-11d2-8ddb-00105a2799b5}')
    @commethod(3)
    def AdviseEventSink(self, pSink: win32more.Windows.Win32.UI.TextServices.ITfLangBarEventSink, hwnd: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseEventSink(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetThreadMarshalInterface(self, dwThreadId: UInt32, dwType: UInt32, riid: POINTER(Guid), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetThreadLangBarItemMgr(self, dwThreadId: UInt32, pplbi: POINTER(win32more.Windows.Win32.UI.TextServices.ITfLangBarItemMgr), pdwThreadid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetInputProcessorProfiles(self, dwThreadId: UInt32, ppaip: POINTER(win32more.Windows.Win32.UI.TextServices.ITfInputProcessorProfiles), pdwThreadid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RestoreLastFocus(self, pdwThreadId: POINTER(UInt32), fPrev: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetModalInput(self, pSink: win32more.Windows.Win32.UI.TextServices.ITfLangBarEventSink, dwThreadId: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ShowFloating(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetShowFloatingStatus(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfLanguageProfileNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{43c9fe15-f494-4c17-9de2-b8a4ac350aa8}')
    @commethod(3)
    def OnLanguageChange(self, langid: UInt16, pfAccept: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnLanguageChanged(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfMSAAControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b5f8fb3b-393f-4f7c-84cb-504924c2705a}')
    @commethod(3)
    def SystemEnableMSAA(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SystemDisableMSAA(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfMenu(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6f8a98e4-aaa0-4f15-8c5b-07e0df0a3dd8}')
    @commethod(3)
    def AddMenuItem(self, uId: UInt32, dwFlags: UInt32, hbmp: win32more.Windows.Win32.Graphics.Gdi.HBITMAP, hbmpMask: win32more.Windows.Win32.Graphics.Gdi.HBITMAP, pch: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, ppMenu: POINTER(win32more.Windows.Win32.UI.TextServices.ITfMenu)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfMessagePump(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8f1b8ad8-0b6b-4874-90c5-bd76011e8f7c}')
    @commethod(3)
    def PeekMessageA(self, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG), hwnd: win32more.Windows.Win32.Foundation.HWND, wMsgFilterMin: UInt32, wMsgFilterMax: UInt32, wRemoveMsg: UInt32, pfResult: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMessageA(self, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG), hwnd: win32more.Windows.Win32.Foundation.HWND, wMsgFilterMin: UInt32, wMsgFilterMax: UInt32, pfResult: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PeekMessageW(self, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG), hwnd: win32more.Windows.Win32.Foundation.HWND, wMsgFilterMin: UInt32, wMsgFilterMax: UInt32, wRemoveMsg: UInt32, pfResult: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMessageW(self, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG), hwnd: win32more.Windows.Win32.Foundation.HWND, wMsgFilterMin: UInt32, wMsgFilterMax: UInt32, pfResult: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfMouseSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a1adaaa2-3a24-449d-ac96-5183e7f5c217}')
    @commethod(3)
    def OnMouseEvent(self, uEdge: UInt32, uQuadrant: UInt32, dwBtnStatus: UInt32, pfEaten: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfMouseTracker(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09d146cd-a544-4132-925b-7afa8ef322d0}')
    @commethod(3)
    def AdviseMouseSink(self, range: win32more.Windows.Win32.UI.TextServices.ITfRange, pSink: win32more.Windows.Win32.UI.TextServices.ITfMouseSink, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseMouseSink(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfMouseTrackerACP(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3bdd78e2-c16e-47fd-b883-ce6facc1a208}')
    @commethod(3)
    def AdviseMouseSink(self, range: win32more.Windows.Win32.UI.TextServices.ITfRangeACP, pSink: win32more.Windows.Win32.UI.TextServices.ITfMouseSink, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseMouseSink(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfPersistentPropertyLoaderACP(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ef89150-0807-11d3-8df0-00105a2799b5}')
    @commethod(3)
    def LoadProperty(self, pHdr: POINTER(win32more.Windows.Win32.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP), ppStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfPreservedKeyNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6f77c993-d2b1-446e-853e-5912efc8a286}')
    @commethod(3)
    def OnUpdated(self, pprekey: POINTER(win32more.Windows.Win32.UI.TextServices.TF_PRESERVEDKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfProperty(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfReadOnlyProperty
    _iid_ = Guid('{e2449660-9542-11d2-bf46-00105a2799b5}')
    @commethod(7)
    def FindRange(self, ec: UInt32, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, ppRange: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRange), aPos: win32more.Windows.Win32.UI.TextServices.TfAnchor) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetValueStore(self, ec: UInt32, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, pPropStore: win32more.Windows.Win32.UI.TextServices.ITfPropertyStore) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetValue(self, ec: UInt32, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Clear(self, ec: UInt32, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfPropertyStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6834b120-88cb-11d2-bf45-00105a2799b5}')
    @commethod(3)
    def GetType(self, pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataType(self, pdwReserved: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetData(self, pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnTextUpdated(self, dwFlags: UInt32, pRangeNew: win32more.Windows.Win32.UI.TextServices.ITfRange, pfAccept: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Shrink(self, pRangeNew: win32more.Windows.Win32.UI.TextServices.ITfRange, pfFree: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Divide(self, pRangeThis: win32more.Windows.Win32.UI.TextServices.ITfRange, pRangeNew: win32more.Windows.Win32.UI.TextServices.ITfRange, ppPropStore: POINTER(win32more.Windows.Win32.UI.TextServices.ITfPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Clone(self, pPropStore: POINTER(win32more.Windows.Win32.UI.TextServices.ITfPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPropertyRangeCreator(self, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Serialize(self, pStream: win32more.Windows.Win32.System.Com.IStream, pcb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfQueryEmbedded(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0fab9bdb-d250-4169-84e5-6be118fdd7a8}')
    @commethod(3)
    def QueryInsertEmbedded(self, pguidService: POINTER(Guid), pFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pfInsertable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfRange(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa80e7ff-2021-11d2-93e0-0060b067b86e}')
    @commethod(3)
    def GetText(self, ec: UInt32, dwFlags: UInt32, pchText: win32more.Windows.Win32.Foundation.PWSTR, cchMax: UInt32, pcch: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetText(self, ec: UInt32, dwFlags: UInt32, pchText: win32more.Windows.Win32.Foundation.PWSTR, cch: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFormattedText(self, ec: UInt32, ppDataObject: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetEmbedded(self, ec: UInt32, rguidService: POINTER(Guid), riid: POINTER(Guid), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InsertEmbedded(self, ec: UInt32, dwFlags: UInt32, pDataObject: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ShiftStart(self, ec: UInt32, cchReq: Int32, pcch: POINTER(Int32), pHalt: POINTER(win32more.Windows.Win32.UI.TextServices.TF_HALTCOND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ShiftEnd(self, ec: UInt32, cchReq: Int32, pcch: POINTER(Int32), pHalt: POINTER(win32more.Windows.Win32.UI.TextServices.TF_HALTCOND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ShiftStartToRange(self, ec: UInt32, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, aPos: win32more.Windows.Win32.UI.TextServices.TfAnchor) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ShiftEndToRange(self, ec: UInt32, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, aPos: win32more.Windows.Win32.UI.TextServices.TfAnchor) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ShiftStartRegion(self, ec: UInt32, dir: win32more.Windows.Win32.UI.TextServices.TfShiftDir, pfNoRegion: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ShiftEndRegion(self, ec: UInt32, dir: win32more.Windows.Win32.UI.TextServices.TfShiftDir, pfNoRegion: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsEmpty(self, ec: UInt32, pfEmpty: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Collapse(self, ec: UInt32, aPos: win32more.Windows.Win32.UI.TextServices.TfAnchor) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def IsEqualStart(self, ec: UInt32, pWith: win32more.Windows.Win32.UI.TextServices.ITfRange, aPos: win32more.Windows.Win32.UI.TextServices.TfAnchor, pfEqual: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def IsEqualEnd(self, ec: UInt32, pWith: win32more.Windows.Win32.UI.TextServices.ITfRange, aPos: win32more.Windows.Win32.UI.TextServices.TfAnchor, pfEqual: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CompareStart(self, ec: UInt32, pWith: win32more.Windows.Win32.UI.TextServices.ITfRange, aPos: win32more.Windows.Win32.UI.TextServices.TfAnchor, plResult: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def CompareEnd(self, ec: UInt32, pWith: win32more.Windows.Win32.UI.TextServices.ITfRange, aPos: win32more.Windows.Win32.UI.TextServices.TfAnchor, plResult: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def AdjustForInsert(self, ec: UInt32, cchInsert: UInt32, pfInsertOk: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetGravity(self, pgStart: POINTER(win32more.Windows.Win32.UI.TextServices.TfGravity), pgEnd: POINTER(win32more.Windows.Win32.UI.TextServices.TfGravity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetGravity(self, ec: UInt32, gStart: win32more.Windows.Win32.UI.TextServices.TfGravity, gEnd: win32more.Windows.Win32.UI.TextServices.TfGravity) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Clone(self, ppClone: POINTER(win32more.Windows.Win32.UI.TextServices.ITfRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetContext(self, ppContext: POINTER(win32more.Windows.Win32.UI.TextServices.ITfContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfRangeACP(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfRange
    _iid_ = Guid('{057a6296-029b-4154-b79a-0d461d4ea94c}')
    @commethod(25)
    def GetExtent(self, pacpAnchor: POINTER(Int32), pcch: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetExtent(self, acpAnchor: Int32, cch: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfRangeBackup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{463a506d-6992-49d2-9b88-93d55e70bb16}')
    @commethod(3)
    def Restore(self, ec: UInt32, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfReadOnlyProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{17d49a3d-f8b8-4b2f-b254-52319dd64c53}')
    @commethod(3)
    def GetType(self, pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumRanges(self, ec: UInt32, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfRanges), pTargetRange: win32more.Windows.Win32.UI.TextServices.ITfRange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetValue(self, ec: UInt32, pRange: win32more.Windows.Win32.UI.TextServices.ITfRange, pvarValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetContext(self, ppContext: POINTER(win32more.Windows.Win32.UI.TextServices.ITfContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfReadingInformationUIElement(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfUIElement
    _iid_ = Guid('{ea1ea139-19df-11d7-a6d2-00065b84435c}')
    @commethod(7)
    def GetUpdatedFlags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetContext(self, ppic: POINTER(win32more.Windows.Win32.UI.TextServices.ITfContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetString(self, pstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMaxReadingStringLength(self, pcchMax: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetErrorIndex(self, pErrorIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsVerticalOrderPreferred(self, pfVertical: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfReverseConversion(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a415e162-157d-417d-8a8c-0ab26c7d2781}')
    @commethod(3)
    def DoReverseConversion(self, lpstr: win32more.Windows.Win32.Foundation.PWSTR, ppList: POINTER(win32more.Windows.Win32.UI.TextServices.ITfReverseConversionList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfReverseConversionList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{151d69f0-86f4-4674-b721-56911e797f47}')
    @commethod(3)
    def GetLength(self, puIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetString(self, uIndex: UInt32, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfReverseConversionMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b643c236-c493-41b6-abb3-692412775cc4}')
    @commethod(3)
    def GetReverseConversion(self, langid: UInt16, guidProfile: POINTER(Guid), dwflag: UInt32, ppReverseConversion: POINTER(win32more.Windows.Win32.UI.TextServices.ITfReverseConversion)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfSource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ea48a35-60ae-446f-8fd6-e6a8d82459f7}')
    @commethod(3)
    def AdviseSink(self, riid: POINTER(Guid), punk: win32more.Windows.Win32.System.Com.IUnknown, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseSink(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfSourceSingle(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{73131f9c-56a9-49dd-b0ee-d046633f7528}')
    @commethod(3)
    def AdviseSingleSink(self, tid: UInt32, riid: POINTER(Guid), punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseSingleSink(self, tid: UInt32, riid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfSpeechUIServer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{90e9a944-9244-489f-a78f-de67afc013a7}')
    @commethod(3)
    def Initialize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShowUI(self, fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateBalloon(self, style: win32more.Windows.Win32.UI.TextServices.TfLBBalloonStyle, pch: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfStatusSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6b7d8d73-b267-4f69-b32e-1ca321ce4f45}')
    @commethod(3)
    def OnStatusChange(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfSystemDeviceTypeLangBarItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{45672eb9-9059-46a2-838d-4530355f6a77}')
    @commethod(3)
    def SetIconMode(self, dwFlags: win32more.Windows.Win32.UI.TextServices.LANG_BAR_ITEM_ICON_MODE_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIconMode(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfSystemLangBarItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1e13e9ec-6b33-4d4a-b5eb-8a92f029f356}')
    @commethod(3)
    def SetIcon(self, hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTooltipString(self, pchToolTip: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfSystemLangBarItemSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1449d9ab-13cf-4687-aa3e-8d8b18574396}')
    @commethod(3)
    def InitMenu(self, pMenu: win32more.Windows.Win32.UI.TextServices.ITfMenu) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnMenuSelect(self, wID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfSystemLangBarItemText(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5c4ce0e5-ba49-4b52-ac6b-3b397b4f701f}')
    @commethod(3)
    def SetItemText(self, pch: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItemText(self, pbstrText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfTextEditSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8127d409-ccd3-4683-967a-b43d5b482bf7}')
    @commethod(3)
    def OnEndEdit(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext, ecReadOnly: UInt32, pEditRecord: win32more.Windows.Win32.UI.TextServices.ITfEditRecord) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfTextInputProcessor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa80e7f7-2021-11d2-93e0-0060b067b86e}')
    @commethod(3)
    def Activate(self, ptim: win32more.Windows.Win32.UI.TextServices.ITfThreadMgr, tid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deactivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfTextInputProcessorEx(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfTextInputProcessor
    _iid_ = Guid('{6e4e2102-f9cd-433d-b496-303ce03a6507}')
    @commethod(5)
    def ActivateEx(self, ptim: win32more.Windows.Win32.UI.TextServices.ITfThreadMgr, tid: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfTextLayoutSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2af2d06a-dd5b-4927-a0b4-54f19c91fade}')
    @commethod(3)
    def OnLayoutChange(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext, lcode: win32more.Windows.Win32.UI.TextServices.TfLayoutCode, pView: win32more.Windows.Win32.UI.TextServices.ITfContextView) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfThreadFocusSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0f1db0c-3a20-405c-a303-96b6010a885f}')
    @commethod(3)
    def OnSetThreadFocus(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnKillThreadFocus(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfThreadMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa80e801-2021-11d2-93e0-0060b067b86e}')
    @commethod(3)
    def Activate(self, ptid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deactivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateDocumentMgr(self, ppdim: POINTER(win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumDocumentMgrs(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfDocumentMgrs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFocus(self, ppdimFocus: POINTER(win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetFocus(self, pdimFocus: win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AssociateFocus(self, hwnd: win32more.Windows.Win32.Foundation.HWND, pdimNew: win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr, ppdimPrev: POINTER(win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsThreadFocus(self, pfThreadFocus: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFunctionProvider(self, clsid: POINTER(Guid), ppFuncProv: POINTER(win32more.Windows.Win32.UI.TextServices.ITfFunctionProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnumFunctionProviders(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfFunctionProviders)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetGlobalCompartment(self, ppCompMgr: POINTER(win32more.Windows.Win32.UI.TextServices.ITfCompartmentMgr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfThreadMgr2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0ab198ef-6477-4ee8-8812-6780edb82d5e}')
    @commethod(3)
    def Activate(self, ptid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Deactivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateDocumentMgr(self, ppdim: POINTER(win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumDocumentMgrs(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfDocumentMgrs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFocus(self, ppdimFocus: POINTER(win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetFocus(self, pdimFocus: win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsThreadFocus(self, pfThreadFocus: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFunctionProvider(self, clsid: POINTER(Guid), ppFuncProv: POINTER(win32more.Windows.Win32.UI.TextServices.ITfFunctionProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumFunctionProviders(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfFunctionProviders)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetGlobalCompartment(self, ppCompMgr: POINTER(win32more.Windows.Win32.UI.TextServices.ITfCompartmentMgr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ActivateEx(self, ptid: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetActiveFlags(self, lpdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SuspendKeystrokeHandling(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ResumeKeystrokeHandling(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfThreadMgrEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa80e80e-2021-11d2-93e0-0060b067b86e}')
    @commethod(3)
    def OnInitDocumentMgr(self, pdim: win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnUninitDocumentMgr(self, pdim: win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnSetFocus(self, pdimFocus: win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr, pdimPrevFocus: win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnPushContext(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnPopContext(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfThreadMgrEx(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfThreadMgr
    _iid_ = Guid('{3e90ade3-7594-4cb0-bb58-69628f5f458c}')
    @commethod(14)
    def ActivateEx(self, ptid: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetActiveFlags(self, lpdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfToolTipUIElement(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfUIElement
    _iid_ = Guid('{52b18b5c-555d-46b2-b00a-fa680144fbdb}')
    @commethod(7)
    def GetString(self, pstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfTransitoryExtensionSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a615096f-1c57-4813-8a15-55ee6e5a839c}')
    @commethod(3)
    def OnTransitoryExtensionUpdated(self, pic: win32more.Windows.Win32.UI.TextServices.ITfContext, ecReadOnly: UInt32, pResultRange: win32more.Windows.Win32.UI.TextServices.ITfRange, pCompositionRange: win32more.Windows.Win32.UI.TextServices.ITfRange, pfDeleteResultRange: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfTransitoryExtensionUIElement(ComPtr):
    extends: win32more.Windows.Win32.UI.TextServices.ITfUIElement
    _iid_ = Guid('{858f956a-972f-42a2-a2f2-0321e1abe209}')
    @commethod(7)
    def GetDocumentMgr(self, ppdim: POINTER(win32more.Windows.Win32.UI.TextServices.ITfDocumentMgr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfUIElement(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ea1ea137-19df-11d7-a6d2-00065b84435c}')
    @commethod(3)
    def GetDescription(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetGUID(self, pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Show(self, bShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsShown(self, pbShow: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfUIElementMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ea1ea135-19df-11d7-a6d2-00065b84435c}')
    @commethod(3)
    def BeginUIElement(self, pElement: win32more.Windows.Win32.UI.TextServices.ITfUIElement, pbShow: POINTER(win32more.Windows.Win32.Foundation.BOOL), pdwUIElementId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateUIElement(self, dwUIElementId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndUIElement(self, dwUIElementId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetUIElement(self, dwUIELementId: UInt32, ppElement: POINTER(win32more.Windows.Win32.UI.TextServices.ITfUIElement)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumUIElements(self, ppEnum: POINTER(win32more.Windows.Win32.UI.TextServices.IEnumTfUIElements)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITfUIElementSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ea1ea136-19df-11d7-a6d2-00065b84435c}')
    @commethod(3)
    def BeginUIElement(self, dwUIElementId: UInt32, pbShow: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateUIElement(self, dwUIElementId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EndUIElement(self, dwUIElementId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIManagerEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cd91d690-a7e8-4265-9b38-8bb3bbaba7de}')
    @commethod(3)
    def OnWindowOpening(self, prcBounds: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnWindowOpened(self, prcBounds: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnWindowUpdating(self, prcUpdatedBounds: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnWindowUpdated(self, prcUpdatedBounds: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnWindowClosing(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnWindowClosed(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVersionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{401518ec-db00-4611-9b29-2a0e4b9afa85}')
    @commethod(3)
    def GetSubcomponentCount(self, ulSub: UInt32, ulCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetImplementationID(self, ulSub: UInt32, implid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBuildVersion(self, ulSub: UInt32, pdwMajor: POINTER(UInt32), pdwMinor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetComponentDescription(self, ulSub: UInt32, pImplStr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetInstanceDescription(self, ulSub: UInt32, pImplStr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
InputScope = Int32
IS_DEFAULT: win32more.Windows.Win32.UI.TextServices.InputScope = 0
IS_URL: win32more.Windows.Win32.UI.TextServices.InputScope = 1
IS_FILE_FULLFILEPATH: win32more.Windows.Win32.UI.TextServices.InputScope = 2
IS_FILE_FILENAME: win32more.Windows.Win32.UI.TextServices.InputScope = 3
IS_EMAIL_USERNAME: win32more.Windows.Win32.UI.TextServices.InputScope = 4
IS_EMAIL_SMTPEMAILADDRESS: win32more.Windows.Win32.UI.TextServices.InputScope = 5
IS_LOGINNAME: win32more.Windows.Win32.UI.TextServices.InputScope = 6
IS_PERSONALNAME_FULLNAME: win32more.Windows.Win32.UI.TextServices.InputScope = 7
IS_PERSONALNAME_PREFIX: win32more.Windows.Win32.UI.TextServices.InputScope = 8
IS_PERSONALNAME_GIVENNAME: win32more.Windows.Win32.UI.TextServices.InputScope = 9
IS_PERSONALNAME_MIDDLENAME: win32more.Windows.Win32.UI.TextServices.InputScope = 10
IS_PERSONALNAME_SURNAME: win32more.Windows.Win32.UI.TextServices.InputScope = 11
IS_PERSONALNAME_SUFFIX: win32more.Windows.Win32.UI.TextServices.InputScope = 12
IS_ADDRESS_FULLPOSTALADDRESS: win32more.Windows.Win32.UI.TextServices.InputScope = 13
IS_ADDRESS_POSTALCODE: win32more.Windows.Win32.UI.TextServices.InputScope = 14
IS_ADDRESS_STREET: win32more.Windows.Win32.UI.TextServices.InputScope = 15
IS_ADDRESS_STATEORPROVINCE: win32more.Windows.Win32.UI.TextServices.InputScope = 16
IS_ADDRESS_CITY: win32more.Windows.Win32.UI.TextServices.InputScope = 17
IS_ADDRESS_COUNTRYNAME: win32more.Windows.Win32.UI.TextServices.InputScope = 18
IS_ADDRESS_COUNTRYSHORTNAME: win32more.Windows.Win32.UI.TextServices.InputScope = 19
IS_CURRENCY_AMOUNTANDSYMBOL: win32more.Windows.Win32.UI.TextServices.InputScope = 20
IS_CURRENCY_AMOUNT: win32more.Windows.Win32.UI.TextServices.InputScope = 21
IS_DATE_FULLDATE: win32more.Windows.Win32.UI.TextServices.InputScope = 22
IS_DATE_MONTH: win32more.Windows.Win32.UI.TextServices.InputScope = 23
IS_DATE_DAY: win32more.Windows.Win32.UI.TextServices.InputScope = 24
IS_DATE_YEAR: win32more.Windows.Win32.UI.TextServices.InputScope = 25
IS_DATE_MONTHNAME: win32more.Windows.Win32.UI.TextServices.InputScope = 26
IS_DATE_DAYNAME: win32more.Windows.Win32.UI.TextServices.InputScope = 27
IS_DIGITS: win32more.Windows.Win32.UI.TextServices.InputScope = 28
IS_NUMBER: win32more.Windows.Win32.UI.TextServices.InputScope = 29
IS_ONECHAR: win32more.Windows.Win32.UI.TextServices.InputScope = 30
IS_PASSWORD: win32more.Windows.Win32.UI.TextServices.InputScope = 31
IS_TELEPHONE_FULLTELEPHONENUMBER: win32more.Windows.Win32.UI.TextServices.InputScope = 32
IS_TELEPHONE_COUNTRYCODE: win32more.Windows.Win32.UI.TextServices.InputScope = 33
IS_TELEPHONE_AREACODE: win32more.Windows.Win32.UI.TextServices.InputScope = 34
IS_TELEPHONE_LOCALNUMBER: win32more.Windows.Win32.UI.TextServices.InputScope = 35
IS_TIME_FULLTIME: win32more.Windows.Win32.UI.TextServices.InputScope = 36
IS_TIME_HOUR: win32more.Windows.Win32.UI.TextServices.InputScope = 37
IS_TIME_MINORSEC: win32more.Windows.Win32.UI.TextServices.InputScope = 38
IS_NUMBER_FULLWIDTH: win32more.Windows.Win32.UI.TextServices.InputScope = 39
IS_ALPHANUMERIC_HALFWIDTH: win32more.Windows.Win32.UI.TextServices.InputScope = 40
IS_ALPHANUMERIC_FULLWIDTH: win32more.Windows.Win32.UI.TextServices.InputScope = 41
IS_CURRENCY_CHINESE: win32more.Windows.Win32.UI.TextServices.InputScope = 42
IS_BOPOMOFO: win32more.Windows.Win32.UI.TextServices.InputScope = 43
IS_HIRAGANA: win32more.Windows.Win32.UI.TextServices.InputScope = 44
IS_KATAKANA_HALFWIDTH: win32more.Windows.Win32.UI.TextServices.InputScope = 45
IS_KATAKANA_FULLWIDTH: win32more.Windows.Win32.UI.TextServices.InputScope = 46
IS_HANJA: win32more.Windows.Win32.UI.TextServices.InputScope = 47
IS_HANGUL_HALFWIDTH: win32more.Windows.Win32.UI.TextServices.InputScope = 48
IS_HANGUL_FULLWIDTH: win32more.Windows.Win32.UI.TextServices.InputScope = 49
IS_SEARCH: win32more.Windows.Win32.UI.TextServices.InputScope = 50
IS_FORMULA: win32more.Windows.Win32.UI.TextServices.InputScope = 51
IS_SEARCH_INCREMENTAL: win32more.Windows.Win32.UI.TextServices.InputScope = 52
IS_CHINESE_HALFWIDTH: win32more.Windows.Win32.UI.TextServices.InputScope = 53
IS_CHINESE_FULLWIDTH: win32more.Windows.Win32.UI.TextServices.InputScope = 54
IS_NATIVE_SCRIPT: win32more.Windows.Win32.UI.TextServices.InputScope = 55
IS_YOMI: win32more.Windows.Win32.UI.TextServices.InputScope = 56
IS_TEXT: win32more.Windows.Win32.UI.TextServices.InputScope = 57
IS_CHAT: win32more.Windows.Win32.UI.TextServices.InputScope = 58
IS_NAME_OR_PHONENUMBER: win32more.Windows.Win32.UI.TextServices.InputScope = 59
IS_EMAILNAME_OR_ADDRESS: win32more.Windows.Win32.UI.TextServices.InputScope = 60
IS_PRIVATE: win32more.Windows.Win32.UI.TextServices.InputScope = 61
IS_MAPS: win32more.Windows.Win32.UI.TextServices.InputScope = 62
IS_NUMERIC_PASSWORD: win32more.Windows.Win32.UI.TextServices.InputScope = 63
IS_NUMERIC_PIN: win32more.Windows.Win32.UI.TextServices.InputScope = 64
IS_ALPHANUMERIC_PIN: win32more.Windows.Win32.UI.TextServices.InputScope = 65
IS_ALPHANUMERIC_PIN_SET: win32more.Windows.Win32.UI.TextServices.InputScope = 66
IS_FORMULA_NUMBER: win32more.Windows.Win32.UI.TextServices.InputScope = 67
IS_CHAT_WITHOUT_EMOJI: win32more.Windows.Win32.UI.TextServices.InputScope = 68
IS_PHRASELIST: win32more.Windows.Win32.UI.TextServices.InputScope = -1
IS_REGULAREXPRESSION: win32more.Windows.Win32.UI.TextServices.InputScope = -2
IS_SRGS: win32more.Windows.Win32.UI.TextServices.InputScope = -3
IS_XML: win32more.Windows.Win32.UI.TextServices.InputScope = -4
IS_ENUMSTRING: win32more.Windows.Win32.UI.TextServices.InputScope = -5
LANG_BAR_ITEM_ICON_MODE_FLAGS = UInt32
TF_DTLBI_NONE: win32more.Windows.Win32.UI.TextServices.LANG_BAR_ITEM_ICON_MODE_FLAGS = 0
TF_DTLBI_USEPROFILEICON: win32more.Windows.Win32.UI.TextServices.LANG_BAR_ITEM_ICON_MODE_FLAGS = 1
MSAAControl = Guid('{08cd963f-7a3e-4f5c-9bd8-d692bb043c5b}')
TEXT_STORE_CHANGE_FLAGS = UInt32
TS_TC_NONE: win32more.Windows.Win32.UI.TextServices.TEXT_STORE_CHANGE_FLAGS = 0
TS_TC_CORRECTION: win32more.Windows.Win32.UI.TextServices.TEXT_STORE_CHANGE_FLAGS = 1
TEXT_STORE_LOCK_FLAGS = UInt32
TS_LF_READ: win32more.Windows.Win32.UI.TextServices.TEXT_STORE_LOCK_FLAGS = 2
TS_LF_READWRITE: win32more.Windows.Win32.UI.TextServices.TEXT_STORE_LOCK_FLAGS = 6
TEXT_STORE_TEXT_CHANGE_FLAGS = UInt32
TS_ST_NONE: win32more.Windows.Win32.UI.TextServices.TEXT_STORE_TEXT_CHANGE_FLAGS = 0
TS_ST_CORRECTION: win32more.Windows.Win32.UI.TextServices.TEXT_STORE_TEXT_CHANGE_FLAGS = 1
TF_CONTEXT_EDIT_CONTEXT_FLAGS = UInt32
TF_ES_ASYNCDONTCARE: win32more.Windows.Win32.UI.TextServices.TF_CONTEXT_EDIT_CONTEXT_FLAGS = 0
TF_ES_SYNC: win32more.Windows.Win32.UI.TextServices.TF_CONTEXT_EDIT_CONTEXT_FLAGS = 1
TF_ES_READ: win32more.Windows.Win32.UI.TextServices.TF_CONTEXT_EDIT_CONTEXT_FLAGS = 2
TF_ES_READWRITE: win32more.Windows.Win32.UI.TextServices.TF_CONTEXT_EDIT_CONTEXT_FLAGS = 6
TF_ES_ASYNC: win32more.Windows.Win32.UI.TextServices.TF_CONTEXT_EDIT_CONTEXT_FLAGS = 8
TF_DA_ATTR_INFO = Int32
TF_ATTR_INPUT: win32more.Windows.Win32.UI.TextServices.TF_DA_ATTR_INFO = 0
TF_ATTR_TARGET_CONVERTED: win32more.Windows.Win32.UI.TextServices.TF_DA_ATTR_INFO = 1
TF_ATTR_CONVERTED: win32more.Windows.Win32.UI.TextServices.TF_DA_ATTR_INFO = 2
TF_ATTR_TARGET_NOTCONVERTED: win32more.Windows.Win32.UI.TextServices.TF_DA_ATTR_INFO = 3
TF_ATTR_INPUT_ERROR: win32more.Windows.Win32.UI.TextServices.TF_DA_ATTR_INFO = 4
TF_ATTR_FIXEDCONVERTED: win32more.Windows.Win32.UI.TextServices.TF_DA_ATTR_INFO = 5
TF_ATTR_OTHER: win32more.Windows.Win32.UI.TextServices.TF_DA_ATTR_INFO = -1
class TF_DA_COLOR(Structure):
    type: win32more.Windows.Win32.UI.TextServices.TF_DA_COLORTYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        nIndex: Int32
        cr: win32more.Windows.Win32.Foundation.COLORREF
TF_DA_COLORTYPE = Int32
TF_CT_NONE: win32more.Windows.Win32.UI.TextServices.TF_DA_COLORTYPE = 0
TF_CT_SYSCOLOR: win32more.Windows.Win32.UI.TextServices.TF_DA_COLORTYPE = 1
TF_CT_COLORREF: win32more.Windows.Win32.UI.TextServices.TF_DA_COLORTYPE = 2
TF_DA_LINESTYLE = Int32
TF_LS_NONE: win32more.Windows.Win32.UI.TextServices.TF_DA_LINESTYLE = 0
TF_LS_SOLID: win32more.Windows.Win32.UI.TextServices.TF_DA_LINESTYLE = 1
TF_LS_DOT: win32more.Windows.Win32.UI.TextServices.TF_DA_LINESTYLE = 2
TF_LS_DASH: win32more.Windows.Win32.UI.TextServices.TF_DA_LINESTYLE = 3
TF_LS_SQUIGGLE: win32more.Windows.Win32.UI.TextServices.TF_DA_LINESTYLE = 4
class TF_DISPLAYATTRIBUTE(Structure):
    crText: win32more.Windows.Win32.UI.TextServices.TF_DA_COLOR
    crBk: win32more.Windows.Win32.UI.TextServices.TF_DA_COLOR
    lsStyle: win32more.Windows.Win32.UI.TextServices.TF_DA_LINESTYLE
    fBoldLine: win32more.Windows.Win32.Foundation.BOOL
    crLine: win32more.Windows.Win32.UI.TextServices.TF_DA_COLOR
    bAttr: win32more.Windows.Win32.UI.TextServices.TF_DA_ATTR_INFO
class TF_HALTCOND(Structure):
    pHaltRange: win32more.Windows.Win32.UI.TextServices.ITfRange
    aHaltPos: win32more.Windows.Win32.UI.TextServices.TfAnchor
    dwFlags: UInt32
class TF_INPUTPROCESSORPROFILE(Structure):
    dwProfileType: UInt32
    langid: UInt16
    clsid: Guid
    guidProfile: Guid
    catid: Guid
    hklSubstitute: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL
    dwCaps: UInt32
    hkl: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL
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
    fActive: win32more.Windows.Win32.Foundation.BOOL
    guidProfile: Guid
class TF_LBBALLOONINFO(Structure):
    style: win32more.Windows.Win32.UI.TextServices.TfLBBalloonStyle
    bstrText: win32more.Windows.Win32.Foundation.BSTR
class TF_LMLATTELEMENT(Structure):
    dwFrameStart: UInt32
    dwFrameLen: UInt32
    dwFlags: UInt32
    Anonymous: _Anonymous_e__Union
    bstrText: win32more.Windows.Win32.Foundation.BSTR
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
    varValue: win32more.Windows.Win32.System.Variant.VARIANT
class TF_SELECTION(Structure):
    range: win32more.Windows.Win32.UI.TextServices.ITfRange
    style: win32more.Windows.Win32.UI.TextServices.TF_SELECTIONSTYLE
class TF_SELECTIONSTYLE(Structure):
    ase: win32more.Windows.Win32.UI.TextServices.TfActiveSelEnd
    fInterimChar: win32more.Windows.Win32.Foundation.BOOL
TKBLayoutType = Int32
TKBLT_UNDEFINED: win32more.Windows.Win32.UI.TextServices.TKBLayoutType = 0
TKBLT_CLASSIC: win32more.Windows.Win32.UI.TextServices.TKBLayoutType = 1
TKBLT_OPTIMIZED: win32more.Windows.Win32.UI.TextServices.TKBLayoutType = 2
class TS_ATTRVAL(Structure):
    idAttr: Guid
    dwOverlapId: UInt32
    varValue: win32more.Windows.Win32.System.Variant.VARIANT
class TS_RUNINFO(Structure):
    uCount: UInt32
    type: win32more.Windows.Win32.UI.TextServices.TsRunType
class TS_SELECTIONSTYLE(Structure):
    ase: win32more.Windows.Win32.UI.TextServices.TsActiveSelEnd
    fInterimChar: win32more.Windows.Win32.Foundation.BOOL
class TS_SELECTION_ACP(Structure):
    acpStart: Int32
    acpEnd: Int32
    style: win32more.Windows.Win32.UI.TextServices.TS_SELECTIONSTYLE
class TS_SELECTION_ANCHOR(Structure):
    paStart: win32more.Windows.Win32.UI.TextServices.IAnchor
    paEnd: win32more.Windows.Win32.UI.TextServices.IAnchor
    style: win32more.Windows.Win32.UI.TextServices.TS_SELECTIONSTYLE
class TS_STATUS(Structure):
    dwDynamicFlags: UInt32
    dwStaticFlags: UInt32
class TS_TEXTCHANGE(Structure):
    acpStart: Int32
    acpOldEnd: Int32
    acpNewEnd: Int32
TfActiveSelEnd = Int32
TF_AE_NONE: win32more.Windows.Win32.UI.TextServices.TfActiveSelEnd = 0
TF_AE_START: win32more.Windows.Win32.UI.TextServices.TfActiveSelEnd = 1
TF_AE_END: win32more.Windows.Win32.UI.TextServices.TfActiveSelEnd = 2
TfAnchor = Int32
TF_ANCHOR_START: win32more.Windows.Win32.UI.TextServices.TfAnchor = 0
TF_ANCHOR_END: win32more.Windows.Win32.UI.TextServices.TfAnchor = 1
TfCandidateResult = Int32
CAND_FINALIZED: win32more.Windows.Win32.UI.TextServices.TfCandidateResult = 0
CAND_SELECTED: win32more.Windows.Win32.UI.TextServices.TfCandidateResult = 1
CAND_CANCELED: win32more.Windows.Win32.UI.TextServices.TfCandidateResult = 2
TfGravity = Int32
TF_GRAVITY_BACKWARD: win32more.Windows.Win32.UI.TextServices.TfGravity = 0
TF_GRAVITY_FORWARD: win32more.Windows.Win32.UI.TextServices.TfGravity = 1
TfIntegratableCandidateListSelectionStyle = Int32
STYLE_ACTIVE_SELECTION: win32more.Windows.Win32.UI.TextServices.TfIntegratableCandidateListSelectionStyle = 0
STYLE_IMPLIED_SELECTION: win32more.Windows.Win32.UI.TextServices.TfIntegratableCandidateListSelectionStyle = 1
TfLBBalloonStyle = Int32
TF_LB_BALLOON_RECO: win32more.Windows.Win32.UI.TextServices.TfLBBalloonStyle = 0
TF_LB_BALLOON_SHOW: win32more.Windows.Win32.UI.TextServices.TfLBBalloonStyle = 1
TF_LB_BALLOON_MISS: win32more.Windows.Win32.UI.TextServices.TfLBBalloonStyle = 2
TfLBIClick = Int32
TF_LBI_CLK_RIGHT: win32more.Windows.Win32.UI.TextServices.TfLBIClick = 1
TF_LBI_CLK_LEFT: win32more.Windows.Win32.UI.TextServices.TfLBIClick = 2
TfLayoutCode = Int32
TF_LC_CREATE: win32more.Windows.Win32.UI.TextServices.TfLayoutCode = 0
TF_LC_CHANGE: win32more.Windows.Win32.UI.TextServices.TfLayoutCode = 1
TF_LC_DESTROY: win32more.Windows.Win32.UI.TextServices.TfLayoutCode = 2
TfSapiObject = Int32
GETIF_RESMGR: win32more.Windows.Win32.UI.TextServices.TfSapiObject = 0
GETIF_RECOCONTEXT: win32more.Windows.Win32.UI.TextServices.TfSapiObject = 1
GETIF_RECOGNIZER: win32more.Windows.Win32.UI.TextServices.TfSapiObject = 2
GETIF_VOICE: win32more.Windows.Win32.UI.TextServices.TfSapiObject = 3
GETIF_DICTGRAM: win32more.Windows.Win32.UI.TextServices.TfSapiObject = 4
GETIF_RECOGNIZERNOINIT: win32more.Windows.Win32.UI.TextServices.TfSapiObject = 5
TfShiftDir = Int32
TF_SD_BACKWARD: win32more.Windows.Win32.UI.TextServices.TfShiftDir = 0
TF_SD_FORWARD: win32more.Windows.Win32.UI.TextServices.TfShiftDir = 1
TsActiveSelEnd = Int32
TS_AE_NONE: win32more.Windows.Win32.UI.TextServices.TsActiveSelEnd = 0
TS_AE_START: win32more.Windows.Win32.UI.TextServices.TsActiveSelEnd = 1
TS_AE_END: win32more.Windows.Win32.UI.TextServices.TsActiveSelEnd = 2
TsGravity = Int32
TS_GR_BACKWARD: win32more.Windows.Win32.UI.TextServices.TsGravity = 0
TS_GR_FORWARD: win32more.Windows.Win32.UI.TextServices.TsGravity = 1
TsLayoutCode = Int32
TS_LC_CREATE: win32more.Windows.Win32.UI.TextServices.TsLayoutCode = 0
TS_LC_CHANGE: win32more.Windows.Win32.UI.TextServices.TsLayoutCode = 1
TS_LC_DESTROY: win32more.Windows.Win32.UI.TextServices.TsLayoutCode = 2
TsRunType = Int32
TS_RT_PLAIN: win32more.Windows.Win32.UI.TextServices.TsRunType = 0
TS_RT_HIDDEN: win32more.Windows.Win32.UI.TextServices.TsRunType = 1
TS_RT_OPAQUE: win32more.Windows.Win32.UI.TextServices.TsRunType = 2
TsShiftDir = Int32
TS_SD_BACKWARD: win32more.Windows.Win32.UI.TextServices.TsShiftDir = 0
TS_SD_FORWARD: win32more.Windows.Win32.UI.TextServices.TsShiftDir = 1


make_ready(__name__)
