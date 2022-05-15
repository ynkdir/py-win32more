from win32more import *
import win32more.UI.TextServices
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.UI.WindowsAndMessaging

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.UI.TextServices, name, globals()[f"_define_{name}"]())
    return getattr(win32more.UI.TextServices, name)
def __dir__():
    return __all__
GUID_PROP_TEXTOWNER = 'f1e2d520-0969-11d3-8df0-00105a2799b5'
GUID_PROP_ATTRIBUTE = '34b45670-7526-11d2-a147-00105a2799b5'
GUID_PROP_LANGID = '3280ce20-8032-11d2-b603-00105a2799b5'
GUID_PROP_READING = '5463f7c0-8e31-11d2-bf46-00105a2799b5'
GUID_PROP_COMPOSING = 'e12ac060-af15-11d2-afc5-00105a2799b5'
GUID_PROP_TKB_ALTERNATES = '70b2a803-968d-462e-b93b-2164c91517f7'
GUID_SYSTEM_FUNCTIONPROVIDER = '9a698bb0-0f21-11d3-8df1-00105a2799b5'
GUID_APP_FUNCTIONPROVIDER = '4caef01e-12af-4b0e-9db1-a6ec5b881208'
GUID_TFCAT_CATEGORY_OF_TIP = '534c48c1-0607-4098-a521-4fc899c73e90'
GUID_TFCAT_TIP_KEYBOARD = '34745c63-b2f0-4784-8b67-5e12c8701a31'
GUID_TFCAT_TIP_SPEECH = 'b5a73cd1-8355-426b-a161-259808f26b14'
GUID_TFCAT_TIP_HANDWRITING = '246ecb87-c2f2-4abe-905b-c8b38add2c43'
GUID_TFCAT_PROP_AUDIODATA = '9b7be3a9-e8ab-4d47-a8fe-254fa423436d'
GUID_TFCAT_PROP_INKDATA = '7c6a82ae-b0d7-4f14-a745-14f28b009d61'
GUID_COMPARTMENT_SAPI_AUDIO = '51af2086-cc6b-457d-b5aa-8b19dc290ab4'
GUID_COMPARTMENT_KEYBOARD_DISABLED = '71a5b253-1951-466b-9fbc-9c8808fa84f2'
GUID_COMPARTMENT_KEYBOARD_OPENCLOSE = '58273aad-01bb-4164-95c6-755ba0b5162d'
GUID_COMPARTMENT_HANDWRITING_OPENCLOSE = 'f9ae2c6b-1866-4361-af72-7aa30948890e'
GUID_COMPARTMENT_SPEECH_DISABLED = '56c5c607-0703-4e59-8e52-cbc84e8bbe35'
GUID_COMPARTMENT_SPEECH_OPENCLOSE = '544d6a63-e2e8-4752-bbd1-000960bca083'
GUID_COMPARTMENT_SPEECH_GLOBALSTATE = '2a54fe8e-0d08-460c-a75d-87035ff436c5'
GUID_COMPARTMENT_CONVERSIONMODEBIAS = '5497f516-ee91-436e-b946-aa2c05f1ac5b'
GUID_PROP_MODEBIAS = '372e0716-974f-40ac-a088-08cdc92ebfbc'
GUID_COMPARTMENT_KEYBOARD_INPUTMODE = 'b6592511-bcee-4122-a7c4-09f4b3fa4396'
GUID_MODEBIAS_NONE = '00000000-0000-0000-0000-000000000000'
GUID_MODEBIAS_URLHISTORY = '8b0e54d9-63f2-4c68-84d4-79aee7a59f09'
GUID_MODEBIAS_FILENAME = 'd7f707fe-44c6-4fca-8e76-86ab50c7931b'
GUID_MODEBIAS_READING = 'e31643a3-6466-4cbf-8d8b-0bd4d8545461'
GUID_MODEBIAS_DATETIME = 'f2bdb372-7f61-4039-92ef-1c35599f0222'
GUID_MODEBIAS_NAME = 'fddc10f0-d239-49bf-b8fc-5410caaa427e'
GUID_MODEBIAS_CONVERSATION = '0f4ec104-1790-443b-95f1-e10f939d6546'
GUID_MODEBIAS_NUMERIC = '4021766c-e872-48fd-9cee-4ec5c75e16c3'
GUID_MODEBIAS_HIRAGANA = 'd73d316e-9b91-46f1-a280-31597f52c694'
GUID_MODEBIAS_KATAKANA = '2e0eeddd-3a1a-499e-8543-3c7ee7949811'
GUID_MODEBIAS_HANGUL = '76ef0541-23b3-4d77-a074-691801ccea17'
GUID_MODEBIAS_CHINESE = '7add26de-4328-489b-83ae-6493750cad5c'
GUID_MODEBIAS_HALFWIDTHKATAKANA = '005f6b63-78d4-41cc-8859-485ca821a795'
GUID_MODEBIAS_FULLWIDTHALPHANUMERIC = '81489fb8-b36a-473d-8146-e4a2258b24ae'
GUID_MODEBIAS_FULLWIDTHHANGUL = 'c01ae6c9-45b5-4fd0-9cb1-9f4cebc39fea'
GUID_TFCAT_PROPSTYLE_STATIC = '565fb8d8-6bd4-4ca1-b223-0f2ccb8f4f96'
GUID_TFCAT_DISPLAYATTRIBUTEPROVIDER = '046b8c80-1647-40f7-9b21-b93b81aabc1b'
GUID_TFCAT_DISPLAYATTRIBUTEPROPERTY = 'b95f181b-ea4c-4af1-8056-7c321abbb091'
GUID_COMPARTMENT_SPEECH_UI_STATUS = 'd92016f0-9367-4fe7-9abf-bc59dacbe0e3'
GUID_COMPARTMENT_EMPTYCONTEXT = 'd7487dbf-804e-41c5-894d-ad96fd4eea13'
GUID_COMPARTMENT_TIPUISTATUS = '148ca3ec-0366-401c-8d75-ed978d85fbc9'
GUID_COMPARTMENT_SPEECH_CFGMENU = 'fb6c5c2d-4e83-4bb6-91a2-e019bff6762d'
GUID_LBI_SAPILAYR_CFGMENUBUTTON = 'd02f24a1-942d-422e-8d99-b4f2addee999'
GUID_TFCAT_TIPCAP_SECUREMODE = '49d2f9ce-1f5e-11d7-a6d3-00065b84435c'
GUID_TFCAT_TIPCAP_UIELEMENTENABLED = '49d2f9cf-1f5e-11d7-a6d3-00065b84435c'
GUID_TFCAT_TIPCAP_INPUTMODECOMPARTMENT = 'ccf05dd7-4a87-11d7-a6e2-00065b84435c'
GUID_TFCAT_TIPCAP_COMLESS = '364215d9-75bc-11d7-a6ef-00065b84435c'
GUID_TFCAT_TIPCAP_WOW16 = '364215da-75bc-11d7-a6ef-00065b84435c'
GUID_TFCAT_TIPCAP_IMMERSIVESUPPORT = '13a016df-560b-46cd-947a-4c3af1e0e35d'
GUID_TFCAT_TIPCAP_IMMERSIVEONLY = '3a4259ac-640d-4ad4-89f7-1eb67e7c4ee8'
GUID_TFCAT_TIPCAP_LOCALSERVER = '74769ee9-4a66-4f9d-90d6-bf8b7c3eb461'
GUID_TFCAT_TIPCAP_TSF3 = '07dcb4af-98de-4548-bef7-25bd45979a1f'
GUID_TFCAT_TIPCAP_DUALMODE = '3af314a2-d79f-4b1b-9992-15086d339b05'
GUID_TFCAT_TIPCAP_SYSTRAYSUPPORT = '25504fb4-7bab-4bc1-9c69-cf81890f0ef5'
GUID_COMPARTMENT_KEYBOARD_INPUTMODE_CONVERSION = 'ccf05dd8-4a87-11d7-a6e2-00065b84435c'
GUID_COMPARTMENT_KEYBOARD_INPUTMODE_SENTENCE = 'ccf05dd9-4a87-11d7-a6e2-00065b84435c'
GUID_COMPARTMENT_TRANSITORYEXTENSION = '8be347f5-c7a0-11d7-b408-00065b84435c'
GUID_COMPARTMENT_TRANSITORYEXTENSION_DOCUMENTMANAGER = '8be347f7-c7a0-11d7-b408-00065b84435c'
GUID_COMPARTMENT_TRANSITORYEXTENSION_PARENT = '8be347f8-c7a0-11d7-b408-00065b84435c'
GUID_COMPARTMENT_ENABLED_PROFILES_UPDATED = '92c1fd48-a9ae-4a7c-be08-4329e4723817'
GUID_TFCAT_TRANSITORYEXTENSIONUI = '6302de22-a5cf-4b02-bfe8-4d72b2bed3c6'
GUID_LBI_INPUTMODE = '2c77a81e-41cc-4178-a3a7-5f8a987568e6'
CLSID_TF_ThreadMgr = '529a9e6b-6587-4f23-ab9e-9c7d683e3c50'
CLSID_TF_LangBarMgr = 'ebb08c45-6c4a-4fdc-ae53-4eb8c4c7db8e'
CLSID_TF_DisplayAttributeMgr = '3ce74de4-53d3-4d74-8b83-431b3828ba53'
CLSID_TF_CategoryMgr = 'a4b544a1-438d-4b41-9325-869523e2d6c7'
CLSID_TF_InputProcessorProfiles = '33c53a50-f456-4884-b049-85fd643ecfed'
CLSID_TF_LangBarItemMgr = 'b9931692-a2b3-4fab-bf33-9ec6f9fb96ac'
CLSID_TF_ClassicLangBar = '3318360c-1afc-4d09-a86b-9f9cb6dceb9c'
CLSID_TF_TransitoryExtensionUIEntry = 'ae6be008-07fb-400d-8beb-337a64f7051f'
CLSID_TsfServices = '39aedc00-6b60-46db-8d31-3642be0e4373'
GUID_TS_SERVICE_DATAOBJECT = '6086fbb5-e225-46ce-a770-c1bbd3e05d7b'
GUID_TS_SERVICE_ACCESSIBLE = 'f9786200-a5bf-4a0f-8c24-fb16f5d1aabb'
GUID_TS_SERVICE_ACTIVEX = 'ea937a50-c9a6-4b7d-894a-49d99b784834'
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
TF_PROFILE_NEWPHONETIC = 'b2f9c502-1742-11d4-9790-0080c882687e'
TF_PROFILE_PHONETIC = '761309de-317a-11d4-9b5d-0080c882687e'
TF_PROFILE_NEWCHANGJIE = 'f3ba907a-6c7e-11d4-97fa-0080c882687e'
TF_PROFILE_CHANGJIE = '4bdf9f03-c7d3-11d4-b2ab-0080c882687e'
TF_PROFILE_NEWQUICK = '0b883ba0-c1c7-11d4-87f9-0080c882687e'
TF_PROFILE_QUICK = '6024b45f-5c54-11d4-b921-0080c882687e'
TF_PROFILE_CANTONESE = '0aec109c-7e96-11d4-b2ef-0080c882687e'
TF_PROFILE_PINYIN = 'f3ba9077-6c7e-11d4-97fa-0080c882687e'
TF_PROFILE_SIMPLEFAST = 'fa550b04-5ad7-411f-a5ac-ca038ec515d7'
TF_PROFILE_WUBI = '82590c13-f4dd-44f4-ba1d-8667246fdf8e'
TF_PROFILE_DAYI = '037b2c25-480c-4d7f-b027-d6ca6b69788a'
TF_PROFILE_ARRAY = 'd38eff65-aa46-4fd5-91a7-67845fb02f5b'
TF_PROFILE_YI = '409c8376-007b-4357-ae8e-26316ee3fb0d'
TF_PROFILE_TIGRINYA = '3cab88b7-cc3e-46a6-9765-b772ad7761ff'
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
GUID_INTEGRATIONSTYLE_SEARCHBOX = 'e6d1bd11-82f7-4903-ae21-1a6397cde2eb'
TKBL_UNDEFINED = 0
TKBL_CLASSIC_TRADITIONAL_CHINESE_PHONETIC = 1028
TKBL_CLASSIC_TRADITIONAL_CHINESE_CHANGJIE = 61506
TKBL_CLASSIC_TRADITIONAL_CHINESE_DAYI = 61507
TKBL_OPT_JAPANESE_ABC = 1041
TKBL_OPT_KOREAN_HANGUL_2_BULSIK = 1042
TKBL_OPT_SIMPLIFIED_CHINESE_PINYIN = 2052
TKBL_OPT_TRADITIONAL_CHINESE_PHONETIC = 1028
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
GUID_PROP_INPUTSCOPE = '1713dd5a-68e7-4a5b-9af6-592a595c778d'
DCM_FLAGS_TASKENG = 1
DCM_FLAGS_CTFMON = 2
DCM_FLAGS_LOCALTHREADTSF = 4
ILMCM_CHECKLAYOUTANDTIPENABLED = 1
ILMCM_LANGUAGEBAROFF = 2
LIBID_MSAATEXTLib = '150e2d7a-dac1-4582-947d-2a8fd78b82cd'
TS_STRF_START = 0
TS_STRF_MID = 1
TS_STRF_END = 2
TSATTRID_OTHERS = 'b3c32af9-57d0-46a9-bca8-dac238a13057'
TSATTRID_Font = '573ea825-749b-4f8a-9cfd-21c3605ca828'
TSATTRID_Font_FaceName = 'b536aeb6-053b-4eb8-b65a-50da1e81e72e'
TSATTRID_Font_SizePts = 'c8493302-a5e9-456d-af04-8005e4130f03'
TSATTRID_Font_Style = '68b2a77f-6b0e-4f28-8177-571c2f3a42b1'
TSATTRID_Font_Style_Bold = '48813a43-8a20-4940-8e58-97823f7b268a'
TSATTRID_Font_Style_Italic = '8740682a-a765-48e1-acfc-d22222b2f810'
TSATTRID_Font_Style_SmallCaps = 'facb6bc6-9100-4cc6-b969-11eea45a86b4'
TSATTRID_Font_Style_Capitalize = '7d85a3ba-b4fd-43b3-befc-6b985c843141'
TSATTRID_Font_Style_Uppercase = '33a300e8-e340-4937-b697-8f234045cd9a'
TSATTRID_Font_Style_Lowercase = '76d8ccb5-ca7b-4498-8ee9-d5c4f6f74c60'
TSATTRID_Font_Style_Animation = 'dcf73d22-e029-47b7-bb36-f263a3d004cc'
TSATTRID_Font_Style_Animation_LasVegasLights = 'f40423d5-0f87-4f8f-bada-e6d60c25e152'
TSATTRID_Font_Style_Animation_BlinkingBackground = '86e5b104-0104-4b10-b585-00f2527522b5'
TSATTRID_Font_Style_Animation_SparkleText = '533aad20-962c-4e9f-8c09-b42ea4749711'
TSATTRID_Font_Style_Animation_MarchingBlackAnts = '7644e067-f186-4902-bfc6-ec815aa20e9d'
TSATTRID_Font_Style_Animation_MarchingRedAnts = '78368dad-50fb-4c6f-840b-d486bb6cf781'
TSATTRID_Font_Style_Animation_Shimmer = '2ce31b58-5293-4c36-8809-bf8bb51a27b3'
TSATTRID_Font_Style_Animation_WipeDown = '5872e874-367b-4803-b160-c90ff62569d0'
TSATTRID_Font_Style_Animation_WipeRight = 'b855cbe3-3d2c-4600-b1e9-e1c9ce02f842'
TSATTRID_Font_Style_Emboss = 'bd8ed742-349e-4e37-82fb-437979cb53a7'
TSATTRID_Font_Style_Engrave = '9c3371de-8332-4897-be5d-89233223179a'
TSATTRID_Font_Style_Hidden = 'b1e28770-881c-475f-863f-887a647b1090'
TSATTRID_Font_Style_Kerning = 'cc26e1b4-2f9a-47c8-8bff-bf1eb7cce0dd'
TSATTRID_Font_Style_Outlined = '10e6db31-db0d-4ac6-a7f5-9c9cff6f2ab4'
TSATTRID_Font_Style_Position = '15cd26ab-f2fb-4062-b5a6-9a49e1a5cc0b'
TSATTRID_Font_Style_Protected = '1c557cb2-14cf-4554-a574-ecb2f7e7efd4'
TSATTRID_Font_Style_Shadow = '5f686d2f-c6cd-4c56-8a1a-994a4b9766be'
TSATTRID_Font_Style_Spacing = '98c1200d-8f06-409a-8e49-6a554bf7c153'
TSATTRID_Font_Style_Weight = '12f3189c-8bb0-461b-b1fa-eaf907047fe0'
TSATTRID_Font_Style_Height = '7e937477-12e6-458b-926a-1fa44ee8f391'
TSATTRID_Font_Style_Underline = 'c3c9c9f3-7902-444b-9a7b-48e70f4b50f7'
TSATTRID_Font_Style_Underline_Single = '1b6720e5-0f73-4951-a6b3-6f19e43c9461'
TSATTRID_Font_Style_Underline_Double = '74d24aa6-1db3-4c69-a176-31120e7586d5'
TSATTRID_Font_Style_Strikethrough = '0c562193-2d08-4668-9601-ced41309d7af'
TSATTRID_Font_Style_Strikethrough_Single = '75d736b6-3c8f-4b97-ab78-1877cb990d31'
TSATTRID_Font_Style_Strikethrough_Double = '62489b31-a3e7-4f94-ac43-ebaf8fcc7a9f'
TSATTRID_Font_Style_Overline = 'e3989f4a-992b-4301-8ce1-a5b7c6d1f3c8'
TSATTRID_Font_Style_Overline_Single = '8440d94c-51ce-47b2-8d4c-15751e5f721b'
TSATTRID_Font_Style_Overline_Double = 'dc46063a-e115-46e3-bcd8-ca6772aa95b4'
TSATTRID_Font_Style_Blink = 'bfb2c036-7acf-4532-b720-b416dd7765a8'
TSATTRID_Font_Style_Subscript = '5774fb84-389b-43bc-a74b-1568347cf0f4'
TSATTRID_Font_Style_Superscript = '2ea4993c-563c-49aa-9372-0bef09a9255b'
TSATTRID_Font_Style_Color = '857a7a37-b8af-4e9a-81b4-acf700c8411b'
TSATTRID_Font_Style_BackgroundColor = 'b50eaa4e-3091-4468-81db-d79ea190c7c7'
TSATTRID_Text = '7edb8e68-81f9-449d-a15a-87a8388faac0'
TSATTRID_Text_VerticalWriting = '6bba8195-046f-4ea9-b311-97fd66c4274b'
TSATTRID_Text_RightToLeft = 'ca666e71-1b08-453d-bfdd-28e08c8aaf7a'
TSATTRID_Text_Orientation = '6bab707f-8785-4c39-8b52-96f878303ffb'
TSATTRID_Text_Language = 'd8c04ef1-5753-4c25-8887-85443fe5f819'
TSATTRID_Text_ReadOnly = '85836617-de32-4afd-a50f-a2db110e6e4d'
TSATTRID_Text_EmbeddedObject = '7edb8e68-81f9-449d-a15a-87a8388faac0'
TSATTRID_Text_Alignment = '139941e6-1767-456d-938e-35ba568b5cd4'
TSATTRID_Text_Alignment_Left = '16ae95d3-6361-43a2-8495-d00f397f1693'
TSATTRID_Text_Alignment_Right = 'b36f0f98-1b9e-4360-8616-03fb08a78456'
TSATTRID_Text_Alignment_Center = 'a4a95c16-53bf-4d55-8b87-4bdd8d4275fc'
TSATTRID_Text_Alignment_Justify = 'ed350740-a0f7-42d3-8ea8-f81b6488faf0'
TSATTRID_Text_Link = '47cd9051-3722-4cd8-b7c8-4e17ca1759f5'
TSATTRID_Text_Hyphenation = 'dadf4525-618e-49eb-b1a8-3b68bd7648e3'
TSATTRID_Text_Para = '5edc5822-99dc-4dd6-aec3-b62baa5b2e7c'
TSATTRID_Text_Para_FirstLineIndent = '07c97a13-7472-4dd8-90a9-91e3d7e4f29c'
TSATTRID_Text_Para_LeftIndent = 'fb2848e9-7471-41c9-b6b3-8a1450e01897'
TSATTRID_Text_Para_RightIndent = '2c7f26f9-a5e2-48da-b98a-520cb16513bf'
TSATTRID_Text_Para_SpaceAfter = '7b0a3f55-22dc-425f-a411-93da1d8f9baa'
TSATTRID_Text_Para_SpaceBefore = '8df98589-194a-4601-b251-9865a3e906dd'
TSATTRID_Text_Para_LineSpacing = '699b380d-7f8c-46d6-a73b-dfe3d1538df3'
TSATTRID_Text_Para_LineSpacing_Single = 'ed350740-a0f7-42d3-8ea8-f81b6488faf0'
TSATTRID_Text_Para_LineSpacing_OnePtFive = '0428a021-0397-4b57-9a17-0795994cd3c5'
TSATTRID_Text_Para_LineSpacing_Double = '82fb1805-a6c4-4231-ac12-6260af2aba28'
TSATTRID_Text_Para_LineSpacing_AtLeast = 'adfedf31-2d44-4434-a5ff-7f4c4990a905'
TSATTRID_Text_Para_LineSpacing_Exactly = '3d45ad40-23de-48d7-a6b3-765420c620cc'
TSATTRID_Text_Para_LineSpacing_Multiple = '910f1e3c-d6d0-4f65-8a3c-42b4b31868c5'
TSATTRID_List = '436d673b-26f1-4aee-9e65-8f83a4ed4884'
TSATTRID_List_LevelIndel = '7f7cc899-311f-487b-ad5d-e2a459e12d42'
TSATTRID_List_Type = 'ae3e665e-4bce-49e3-a0fe-2db47d3a17ae'
TSATTRID_List_Type_Bullet = 'bccd77c5-4c4d-4ce2-b102-559f3b2bfcea'
TSATTRID_List_Type_Arabic = '1338c5d6-98a3-4fa3-9bd1-7a60eef8e9e0'
TSATTRID_List_Type_LowerLetter = '96372285-f3cf-491e-a925-3832347fd237'
TSATTRID_List_Type_UpperLetter = '7987b7cd-ce52-428b-9b95-a357f6f10c45'
TSATTRID_List_Type_LowerRoman = '90466262-3980-4b8e-9368-918bd1218a41'
TSATTRID_List_Type_UpperRoman = '0f6ab552-4a80-467f-b2f1-127e2aa3ba9e'
TSATTRID_App = 'a80f77df-4237-40e5-849c-b5fa51c13ac7'
TSATTRID_App_IncorrectSpelling = 'f42de43c-ef12-430d-944c-9a08970a25d2'
TSATTRID_App_IncorrectGrammar = 'bd54e398-ad03-4b74-b6b3-5edb19996388'
LANG_BAR_ITEM_ICON_MODE_FLAGS = UInt32
TF_DTLBI_NONE = 0
TF_DTLBI_USEPROFILEICON = 1
TEXT_STORE_TEXT_CHANGE_FLAGS = UInt32
TS_ST_NONE = 0
TS_ST_CORRECTION = 1
TEXT_STORE_CHANGE_FLAGS = UInt32
TS_TC_NONE = 0
TS_TC_CORRECTION = 1
INSERT_TEXT_AT_SELECTION_FLAGS = UInt32
TF_IAS_NOQUERY = 1
TF_IAS_QUERYONLY = 2
TF_IAS_NO_DEFAULT_COMPOSITION = 2147483648
ANCHOR_CHANGE_HISTORY_FLAGS = UInt32
TS_CH_PRECEDING_DEL = 1
TS_CH_FOLLOWING_DEL = 2
TEXT_STORE_LOCK_FLAGS = UInt32
TS_LF_READ = 2
TS_LF_READWRITE = 6
GET_TEXT_AND_PROPERTY_UPDATES_FLAGS = UInt32
TF_GTP_NONE = 0
TF_GTP_INCL_TEXT = 1
TF_CONTEXT_EDIT_CONTEXT_FLAGS = UInt32
TF_ES_ASYNCDONTCARE = 0
TF_ES_SYNC = 1
TF_ES_READ = 2
TF_ES_READWRITE = 6
TF_ES_ASYNC = 8
HKL = IntPtr
def _define_TS_STATUS_head():
    class TS_STATUS(Structure):
        pass
    return TS_STATUS
def _define_TS_STATUS():
    TS_STATUS = win32more.UI.TextServices.TS_STATUS_head
    TS_STATUS._fields_ = [
        ("dwDynamicFlags", UInt32),
        ("dwStaticFlags", UInt32),
    ]
    return TS_STATUS
def _define_TS_TEXTCHANGE_head():
    class TS_TEXTCHANGE(Structure):
        pass
    return TS_TEXTCHANGE
def _define_TS_TEXTCHANGE():
    TS_TEXTCHANGE = win32more.UI.TextServices.TS_TEXTCHANGE_head
    TS_TEXTCHANGE._fields_ = [
        ("acpStart", Int32),
        ("acpOldEnd", Int32),
        ("acpNewEnd", Int32),
    ]
    return TS_TEXTCHANGE
TsActiveSelEnd = Int32
TS_AE_NONE = 0
TS_AE_START = 1
TS_AE_END = 2
def _define_TS_SELECTIONSTYLE_head():
    class TS_SELECTIONSTYLE(Structure):
        pass
    return TS_SELECTIONSTYLE
def _define_TS_SELECTIONSTYLE():
    TS_SELECTIONSTYLE = win32more.UI.TextServices.TS_SELECTIONSTYLE_head
    TS_SELECTIONSTYLE._fields_ = [
        ("ase", win32more.UI.TextServices.TsActiveSelEnd),
        ("fInterimChar", win32more.Foundation.BOOL),
    ]
    return TS_SELECTIONSTYLE
def _define_TS_SELECTION_ACP_head():
    class TS_SELECTION_ACP(Structure):
        pass
    return TS_SELECTION_ACP
def _define_TS_SELECTION_ACP():
    TS_SELECTION_ACP = win32more.UI.TextServices.TS_SELECTION_ACP_head
    TS_SELECTION_ACP._fields_ = [
        ("acpStart", Int32),
        ("acpEnd", Int32),
        ("style", win32more.UI.TextServices.TS_SELECTIONSTYLE),
    ]
    return TS_SELECTION_ACP
def _define_TS_SELECTION_ANCHOR_head():
    class TS_SELECTION_ANCHOR(Structure):
        pass
    return TS_SELECTION_ANCHOR
def _define_TS_SELECTION_ANCHOR():
    TS_SELECTION_ANCHOR = win32more.UI.TextServices.TS_SELECTION_ANCHOR_head
    TS_SELECTION_ANCHOR._fields_ = [
        ("paStart", win32more.UI.TextServices.IAnchor_head),
        ("paEnd", win32more.UI.TextServices.IAnchor_head),
        ("style", win32more.UI.TextServices.TS_SELECTIONSTYLE),
    ]
    return TS_SELECTION_ANCHOR
def _define_TS_ATTRVAL_head():
    class TS_ATTRVAL(Structure):
        pass
    return TS_ATTRVAL
def _define_TS_ATTRVAL():
    TS_ATTRVAL = win32more.UI.TextServices.TS_ATTRVAL_head
    TS_ATTRVAL._fields_ = [
        ("idAttr", Guid),
        ("dwOverlapId", UInt32),
        ("varValue", win32more.System.Com.VARIANT),
    ]
    return TS_ATTRVAL
TsLayoutCode = Int32
TS_LC_CREATE = 0
TS_LC_CHANGE = 1
TS_LC_DESTROY = 2
TsRunType = Int32
TS_RT_PLAIN = 0
TS_RT_HIDDEN = 1
TS_RT_OPAQUE = 2
def _define_TS_RUNINFO_head():
    class TS_RUNINFO(Structure):
        pass
    return TS_RUNINFO
def _define_TS_RUNINFO():
    TS_RUNINFO = win32more.UI.TextServices.TS_RUNINFO_head
    TS_RUNINFO._fields_ = [
        ("uCount", UInt32),
        ("type", win32more.UI.TextServices.TsRunType),
    ]
    return TS_RUNINFO
def _define_ITextStoreACP_head():
    class ITextStoreACP(win32more.System.Com.IUnknown_head):
        Guid = Guid('28888fe3-c2a0-483a-a3ea-8cb1ce51ff3d')
    return ITextStoreACP
def _define_ITextStoreACP():
    ITextStoreACP = win32more.UI.TextServices.ITextStoreACP_head
    ITextStoreACP.AdviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,UInt32, use_last_error=False)(3, 'AdviseSink', ((1, 'riid'),(1, 'punk'),(1, 'dwMask'),)))
    ITextStoreACP.UnadviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(4, 'UnadviseSink', ((1, 'punk'),)))
    ITextStoreACP.RequestLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(5, 'RequestLock', ((1, 'dwLockFlags'),(1, 'phrSession'),)))
    ITextStoreACP.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TS_STATUS_head), use_last_error=False)(6, 'GetStatus', ((1, 'pdcs'),)))
    ITextStoreACP.QueryInsert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(Int32),POINTER(Int32), use_last_error=False)(7, 'QueryInsert', ((1, 'acpTestStart'),(1, 'acpTestEnd'),(1, 'cch'),(1, 'pacpResultStart'),(1, 'pacpResultEnd'),)))
    ITextStoreACP.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.UI.TextServices.TS_SELECTION_ACP),POINTER(UInt32), use_last_error=False)(8, 'GetSelection', ((1, 'ulIndex'),(1, 'ulCount'),(1, 'pSelection'),(1, 'pcFetched'),)))
    ITextStoreACP.SetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TS_SELECTION_ACP), use_last_error=False)(9, 'SetSelection', ((1, 'ulCount'),(1, 'pSelection'),)))
    ITextStoreACP.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Char),UInt32,POINTER(UInt32),POINTER(win32more.UI.TextServices.TS_RUNINFO),UInt32,POINTER(UInt32),POINTER(Int32), use_last_error=False)(10, 'GetText', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'pchPlain'),(1, 'cchPlainReq'),(1, 'pcchPlainRet'),(1, 'prgRunInfo'),(1, 'cRunInfoReq'),(1, 'pcRunInfoRet'),(1, 'pacpNext'),)))
    ITextStoreACP.SetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,Int32,POINTER(Char),UInt32,POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head), use_last_error=False)(11, 'SetText', ((1, 'dwFlags'),(1, 'acpStart'),(1, 'acpEnd'),(1, 'pchText'),(1, 'cch'),(1, 'pChange'),)))
    ITextStoreACP.GetFormattedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.Com.IDataObject_head), use_last_error=False)(12, 'GetFormattedText', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'ppDataObject'),)))
    ITextStoreACP.GetEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(13, 'GetEmbedded', ((1, 'acpPos'),(1, 'rguidService'),(1, 'riid'),(1, 'ppunk'),)))
    ITextStoreACP.QueryInsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(14, 'QueryInsertEmbedded', ((1, 'pguidService'),(1, 'pFormatEtc'),(1, 'pfInsertable'),)))
    ITextStoreACP.InsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,Int32,win32more.System.Com.IDataObject_head,POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head), use_last_error=False)(15, 'InsertEmbedded', ((1, 'dwFlags'),(1, 'acpStart'),(1, 'acpEnd'),(1, 'pDataObject'),(1, 'pChange'),)))
    ITextStoreACP.InsertTextAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),UInt32,POINTER(Int32),POINTER(Int32),POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head), use_last_error=False)(16, 'InsertTextAtSelection', ((1, 'dwFlags'),(1, 'pchText'),(1, 'cch'),(1, 'pacpStart'),(1, 'pacpEnd'),(1, 'pChange'),)))
    ITextStoreACP.InsertEmbeddedAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IDataObject_head,POINTER(Int32),POINTER(Int32),POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head), use_last_error=False)(17, 'InsertEmbeddedAtSelection', ((1, 'dwFlags'),(1, 'pDataObject'),(1, 'pacpStart'),(1, 'pacpEnd'),(1, 'pChange'),)))
    ITextStoreACP.RequestSupportedAttrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid), use_last_error=False)(18, 'RequestSupportedAttrs', ((1, 'dwFlags'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),)))
    ITextStoreACP.RequestAttrsAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(Guid),UInt32, use_last_error=False)(19, 'RequestAttrsAtPosition', ((1, 'acpPos'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),)))
    ITextStoreACP.RequestAttrsTransitioningAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(Guid),UInt32, use_last_error=False)(20, 'RequestAttrsTransitioningAtPosition', ((1, 'acpPos'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),)))
    ITextStoreACP.FindNextAttrTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(Guid),UInt32,POINTER(Int32),POINTER(win32more.Foundation.BOOL),POINTER(Int32), use_last_error=False)(21, 'FindNextAttrTransition', ((1, 'acpStart'),(1, 'acpHalt'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),(1, 'pacpNext'),(1, 'pfFound'),(1, 'plFoundOffset'),)))
    ITextStoreACP.RetrieveRequestedAttrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TS_ATTRVAL),POINTER(UInt32), use_last_error=False)(22, 'RetrieveRequestedAttrs', ((1, 'ulCount'),(1, 'paAttrVals'),(1, 'pcFetched'),)))
    ITextStoreACP.GetEndACP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'GetEndACP', ((1, 'pacp'),)))
    ITextStoreACP.GetActiveView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(24, 'GetActiveView', ((1, 'pvcView'),)))
    ITextStoreACP.GetACPFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.POINT_head),UInt32,POINTER(Int32), use_last_error=False)(25, 'GetACPFromPoint', ((1, 'vcView'),(1, 'ptScreen'),(1, 'dwFlags'),(1, 'pacp'),)))
    ITextStoreACP.GetTextExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,Int32,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(26, 'GetTextExt', ((1, 'vcView'),(1, 'acpStart'),(1, 'acpEnd'),(1, 'prc'),(1, 'pfClipped'),)))
    ITextStoreACP.GetScreenExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(27, 'GetScreenExt', ((1, 'vcView'),(1, 'prc'),)))
    ITextStoreACP.GetWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.HWND), use_last_error=False)(28, 'GetWnd', ((1, 'vcView'),(1, 'phwnd'),)))
    return ITextStoreACP
def _define_ITextStoreACP2_head():
    class ITextStoreACP2(win32more.System.Com.IUnknown_head):
        Guid = Guid('f86ad89f-5fe4-4b8d-bb9f-ef3797a84f1f')
    return ITextStoreACP2
def _define_ITextStoreACP2():
    ITextStoreACP2 = win32more.UI.TextServices.ITextStoreACP2_head
    ITextStoreACP2.AdviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,UInt32, use_last_error=False)(3, 'AdviseSink', ((1, 'riid'),(1, 'punk'),(1, 'dwMask'),)))
    ITextStoreACP2.UnadviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(4, 'UnadviseSink', ((1, 'punk'),)))
    ITextStoreACP2.RequestLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(5, 'RequestLock', ((1, 'dwLockFlags'),(1, 'phrSession'),)))
    ITextStoreACP2.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TS_STATUS_head), use_last_error=False)(6, 'GetStatus', ((1, 'pdcs'),)))
    ITextStoreACP2.QueryInsert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(Int32),POINTER(Int32), use_last_error=False)(7, 'QueryInsert', ((1, 'acpTestStart'),(1, 'acpTestEnd'),(1, 'cch'),(1, 'pacpResultStart'),(1, 'pacpResultEnd'),)))
    ITextStoreACP2.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.UI.TextServices.TS_SELECTION_ACP),POINTER(UInt32), use_last_error=False)(8, 'GetSelection', ((1, 'ulIndex'),(1, 'ulCount'),(1, 'pSelection'),(1, 'pcFetched'),)))
    ITextStoreACP2.SetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TS_SELECTION_ACP), use_last_error=False)(9, 'SetSelection', ((1, 'ulCount'),(1, 'pSelection'),)))
    ITextStoreACP2.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Char),UInt32,POINTER(UInt32),POINTER(win32more.UI.TextServices.TS_RUNINFO),UInt32,POINTER(UInt32),POINTER(Int32), use_last_error=False)(10, 'GetText', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'pchPlain'),(1, 'cchPlainReq'),(1, 'pcchPlainRet'),(1, 'prgRunInfo'),(1, 'cRunInfoReq'),(1, 'pcRunInfoRet'),(1, 'pacpNext'),)))
    ITextStoreACP2.SetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,Int32,POINTER(Char),UInt32,POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head), use_last_error=False)(11, 'SetText', ((1, 'dwFlags'),(1, 'acpStart'),(1, 'acpEnd'),(1, 'pchText'),(1, 'cch'),(1, 'pChange'),)))
    ITextStoreACP2.GetFormattedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.Com.IDataObject_head), use_last_error=False)(12, 'GetFormattedText', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'ppDataObject'),)))
    ITextStoreACP2.GetEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(13, 'GetEmbedded', ((1, 'acpPos'),(1, 'rguidService'),(1, 'riid'),(1, 'ppunk'),)))
    ITextStoreACP2.QueryInsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(14, 'QueryInsertEmbedded', ((1, 'pguidService'),(1, 'pFormatEtc'),(1, 'pfInsertable'),)))
    ITextStoreACP2.InsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,Int32,win32more.System.Com.IDataObject_head,POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head), use_last_error=False)(15, 'InsertEmbedded', ((1, 'dwFlags'),(1, 'acpStart'),(1, 'acpEnd'),(1, 'pDataObject'),(1, 'pChange'),)))
    ITextStoreACP2.InsertTextAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),UInt32,POINTER(Int32),POINTER(Int32),POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head), use_last_error=False)(16, 'InsertTextAtSelection', ((1, 'dwFlags'),(1, 'pchText'),(1, 'cch'),(1, 'pacpStart'),(1, 'pacpEnd'),(1, 'pChange'),)))
    ITextStoreACP2.InsertEmbeddedAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IDataObject_head,POINTER(Int32),POINTER(Int32),POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head), use_last_error=False)(17, 'InsertEmbeddedAtSelection', ((1, 'dwFlags'),(1, 'pDataObject'),(1, 'pacpStart'),(1, 'pacpEnd'),(1, 'pChange'),)))
    ITextStoreACP2.RequestSupportedAttrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid), use_last_error=False)(18, 'RequestSupportedAttrs', ((1, 'dwFlags'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),)))
    ITextStoreACP2.RequestAttrsAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(Guid),UInt32, use_last_error=False)(19, 'RequestAttrsAtPosition', ((1, 'acpPos'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),)))
    ITextStoreACP2.RequestAttrsTransitioningAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(Guid),UInt32, use_last_error=False)(20, 'RequestAttrsTransitioningAtPosition', ((1, 'acpPos'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),)))
    ITextStoreACP2.FindNextAttrTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(Guid),UInt32,POINTER(Int32),POINTER(win32more.Foundation.BOOL),POINTER(Int32), use_last_error=False)(21, 'FindNextAttrTransition', ((1, 'acpStart'),(1, 'acpHalt'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),(1, 'pacpNext'),(1, 'pfFound'),(1, 'plFoundOffset'),)))
    ITextStoreACP2.RetrieveRequestedAttrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TS_ATTRVAL),POINTER(UInt32), use_last_error=False)(22, 'RetrieveRequestedAttrs', ((1, 'ulCount'),(1, 'paAttrVals'),(1, 'pcFetched'),)))
    ITextStoreACP2.GetEndACP = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'GetEndACP', ((1, 'pacp'),)))
    ITextStoreACP2.GetActiveView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(24, 'GetActiveView', ((1, 'pvcView'),)))
    ITextStoreACP2.GetACPFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.POINT_head),UInt32,POINTER(Int32), use_last_error=False)(25, 'GetACPFromPoint', ((1, 'vcView'),(1, 'ptScreen'),(1, 'dwFlags'),(1, 'pacp'),)))
    ITextStoreACP2.GetTextExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,Int32,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(26, 'GetTextExt', ((1, 'vcView'),(1, 'acpStart'),(1, 'acpEnd'),(1, 'prc'),(1, 'pfClipped'),)))
    ITextStoreACP2.GetScreenExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(27, 'GetScreenExt', ((1, 'vcView'),(1, 'prc'),)))
    return ITextStoreACP2
def _define_ITextStoreACPSink_head():
    class ITextStoreACPSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('22d44c94-a419-4542-a272-ae26093ececf')
    return ITextStoreACPSink
def _define_ITextStoreACPSink():
    ITextStoreACPSink = win32more.UI.TextServices.ITextStoreACPSink_head
    ITextStoreACPSink.OnTextChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TEXT_STORE_TEXT_CHANGE_FLAGS,POINTER(win32more.UI.TextServices.TS_TEXTCHANGE_head), use_last_error=False)(3, 'OnTextChange', ((1, 'dwFlags'),(1, 'pChange'),)))
    ITextStoreACPSink.OnSelectionChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnSelectionChange', ()))
    ITextStoreACPSink.OnLayoutChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TsLayoutCode,UInt32, use_last_error=False)(5, 'OnLayoutChange', ((1, 'lcode'),(1, 'vcView'),)))
    ITextStoreACPSink.OnStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'OnStatusChange', ((1, 'dwFlags'),)))
    ITextStoreACPSink.OnAttrsChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(Guid), use_last_error=False)(7, 'OnAttrsChange', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'cAttrs'),(1, 'paAttrs'),)))
    ITextStoreACPSink.OnLockGranted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TEXT_STORE_LOCK_FLAGS, use_last_error=False)(8, 'OnLockGranted', ((1, 'dwLockFlags'),)))
    ITextStoreACPSink.OnStartEditTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'OnStartEditTransaction', ()))
    ITextStoreACPSink.OnEndEditTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'OnEndEditTransaction', ()))
    return ITextStoreACPSink
TsGravity = Int32
TS_GR_BACKWARD = 0
TS_GR_FORWARD = 1
TsShiftDir = Int32
TS_SD_BACKWARD = 0
TS_SD_FORWARD = 1
def _define_IAnchor_head():
    class IAnchor(win32more.System.Com.IUnknown_head):
        Guid = Guid('0feb7e34-5a60-4356-8ef7-abdec2ff7cf8')
    return IAnchor
def _define_IAnchor():
    IAnchor = win32more.UI.TextServices.IAnchor_head
    IAnchor.SetGravity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TsGravity, use_last_error=False)(3, 'SetGravity', ((1, 'gravity'),)))
    IAnchor.GetGravity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TsGravity), use_last_error=False)(4, 'GetGravity', ((1, 'pgravity'),)))
    IAnchor.IsEqual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'IsEqual', ((1, 'paWith'),(1, 'pfEqual'),)))
    IAnchor.Compare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,POINTER(Int32), use_last_error=False)(6, 'Compare', ((1, 'paWith'),(1, 'plResult'),)))
    IAnchor.Shift = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,POINTER(Int32),win32more.UI.TextServices.IAnchor_head, use_last_error=False)(7, 'Shift', ((1, 'dwFlags'),(1, 'cchReq'),(1, 'pcch'),(1, 'paHaltAnchor'),)))
    IAnchor.ShiftTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head, use_last_error=False)(8, 'ShiftTo', ((1, 'paSite'),)))
    IAnchor.ShiftRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.TsShiftDir,POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'ShiftRegion', ((1, 'dwFlags'),(1, 'dir'),(1, 'pfNoRegion'),)))
    IAnchor.SetChangeHistoryMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'SetChangeHistoryMask', ((1, 'dwMask'),)))
    IAnchor.GetChangeHistory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ANCHOR_CHANGE_HISTORY_FLAGS), use_last_error=False)(11, 'GetChangeHistory', ((1, 'pdwHistory'),)))
    IAnchor.ClearChangeHistory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'ClearChangeHistory', ()))
    IAnchor.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IAnchor_head), use_last_error=False)(13, 'Clone', ((1, 'ppaClone'),)))
    return IAnchor
def _define_ITextStoreAnchor_head():
    class ITextStoreAnchor(win32more.System.Com.IUnknown_head):
        Guid = Guid('9b2077b0-5f18-4dec-bee9-3cc722f5dfe0')
    return ITextStoreAnchor
def _define_ITextStoreAnchor():
    ITextStoreAnchor = win32more.UI.TextServices.ITextStoreAnchor_head
    ITextStoreAnchor.AdviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,UInt32, use_last_error=False)(3, 'AdviseSink', ((1, 'riid'),(1, 'punk'),(1, 'dwMask'),)))
    ITextStoreAnchor.UnadviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(4, 'UnadviseSink', ((1, 'punk'),)))
    ITextStoreAnchor.RequestLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(5, 'RequestLock', ((1, 'dwLockFlags'),(1, 'phrSession'),)))
    ITextStoreAnchor.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TS_STATUS_head), use_last_error=False)(6, 'GetStatus', ((1, 'pdcs'),)))
    ITextStoreAnchor.QueryInsert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,UInt32,POINTER(win32more.UI.TextServices.IAnchor_head),POINTER(win32more.UI.TextServices.IAnchor_head), use_last_error=False)(7, 'QueryInsert', ((1, 'paTestStart'),(1, 'paTestEnd'),(1, 'cch'),(1, 'ppaResultStart'),(1, 'ppaResultEnd'),)))
    ITextStoreAnchor.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.UI.TextServices.TS_SELECTION_ANCHOR),POINTER(UInt32), use_last_error=False)(8, 'GetSelection', ((1, 'ulIndex'),(1, 'ulCount'),(1, 'pSelection'),(1, 'pcFetched'),)))
    ITextStoreAnchor.SetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TS_SELECTION_ANCHOR), use_last_error=False)(9, 'SetSelection', ((1, 'ulCount'),(1, 'pSelection'),)))
    ITextStoreAnchor.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,POINTER(Char),UInt32,POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(10, 'GetText', ((1, 'dwFlags'),(1, 'paStart'),(1, 'paEnd'),(1, 'pchText'),(1, 'cchReq'),(1, 'pcch'),(1, 'fUpdateAnchor'),)))
    ITextStoreAnchor.SetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,POINTER(Char),UInt32, use_last_error=False)(11, 'SetText', ((1, 'dwFlags'),(1, 'paStart'),(1, 'paEnd'),(1, 'pchText'),(1, 'cch'),)))
    ITextStoreAnchor.GetFormattedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,POINTER(win32more.System.Com.IDataObject_head), use_last_error=False)(12, 'GetFormattedText', ((1, 'paStart'),(1, 'paEnd'),(1, 'ppDataObject'),)))
    ITextStoreAnchor.GetEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.IAnchor_head,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(13, 'GetEmbedded', ((1, 'dwFlags'),(1, 'paPos'),(1, 'rguidService'),(1, 'riid'),(1, 'ppunk'),)))
    ITextStoreAnchor.InsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,win32more.System.Com.IDataObject_head, use_last_error=False)(14, 'InsertEmbedded', ((1, 'dwFlags'),(1, 'paStart'),(1, 'paEnd'),(1, 'pDataObject'),)))
    ITextStoreAnchor.RequestSupportedAttrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid), use_last_error=False)(15, 'RequestSupportedAttrs', ((1, 'dwFlags'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),)))
    ITextStoreAnchor.RequestAttrsAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,UInt32,POINTER(Guid),UInt32, use_last_error=False)(16, 'RequestAttrsAtPosition', ((1, 'paPos'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),)))
    ITextStoreAnchor.RequestAttrsTransitioningAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,UInt32,POINTER(Guid),UInt32, use_last_error=False)(17, 'RequestAttrsTransitioningAtPosition', ((1, 'paPos'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),)))
    ITextStoreAnchor.FindNextAttrTransition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,UInt32,POINTER(Guid),UInt32,POINTER(win32more.Foundation.BOOL),POINTER(Int32), use_last_error=False)(18, 'FindNextAttrTransition', ((1, 'paStart'),(1, 'paHalt'),(1, 'cFilterAttrs'),(1, 'paFilterAttrs'),(1, 'dwFlags'),(1, 'pfFound'),(1, 'plFoundOffset'),)))
    ITextStoreAnchor.RetrieveRequestedAttrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TS_ATTRVAL),POINTER(UInt32), use_last_error=False)(19, 'RetrieveRequestedAttrs', ((1, 'ulCount'),(1, 'paAttrVals'),(1, 'pcFetched'),)))
    ITextStoreAnchor.GetStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IAnchor_head), use_last_error=False)(20, 'GetStart', ((1, 'ppaStart'),)))
    ITextStoreAnchor.GetEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IAnchor_head), use_last_error=False)(21, 'GetEnd', ((1, 'ppaEnd'),)))
    ITextStoreAnchor.GetActiveView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(22, 'GetActiveView', ((1, 'pvcView'),)))
    ITextStoreAnchor.GetAnchorFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.POINT_head),UInt32,POINTER(win32more.UI.TextServices.IAnchor_head), use_last_error=False)(23, 'GetAnchorFromPoint', ((1, 'vcView'),(1, 'ptScreen'),(1, 'dwFlags'),(1, 'ppaSite'),)))
    ITextStoreAnchor.GetTextExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(24, 'GetTextExt', ((1, 'vcView'),(1, 'paStart'),(1, 'paEnd'),(1, 'prc'),(1, 'pfClipped'),)))
    ITextStoreAnchor.GetScreenExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(25, 'GetScreenExt', ((1, 'vcView'),(1, 'prc'),)))
    ITextStoreAnchor.GetWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.HWND), use_last_error=False)(26, 'GetWnd', ((1, 'vcView'),(1, 'phwnd'),)))
    ITextStoreAnchor.QueryInsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(27, 'QueryInsertEmbedded', ((1, 'pguidService'),(1, 'pFormatEtc'),(1, 'pfInsertable'),)))
    ITextStoreAnchor.InsertTextAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),UInt32,POINTER(win32more.UI.TextServices.IAnchor_head),POINTER(win32more.UI.TextServices.IAnchor_head), use_last_error=False)(28, 'InsertTextAtSelection', ((1, 'dwFlags'),(1, 'pchText'),(1, 'cch'),(1, 'ppaStart'),(1, 'ppaEnd'),)))
    ITextStoreAnchor.InsertEmbeddedAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IDataObject_head,POINTER(win32more.UI.TextServices.IAnchor_head),POINTER(win32more.UI.TextServices.IAnchor_head), use_last_error=False)(29, 'InsertEmbeddedAtSelection', ((1, 'dwFlags'),(1, 'pDataObject'),(1, 'ppaStart'),(1, 'ppaEnd'),)))
    return ITextStoreAnchor
def _define_ITextStoreAnchorSink_head():
    class ITextStoreAnchorSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e905-2021-11d2-93e0-0060b067b86e')
    return ITextStoreAnchorSink
def _define_ITextStoreAnchorSink():
    ITextStoreAnchorSink = win32more.UI.TextServices.ITextStoreAnchorSink_head
    ITextStoreAnchorSink.OnTextChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TEXT_STORE_CHANGE_FLAGS,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head, use_last_error=False)(3, 'OnTextChange', ((1, 'dwFlags'),(1, 'paStart'),(1, 'paEnd'),)))
    ITextStoreAnchorSink.OnSelectionChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnSelectionChange', ()))
    ITextStoreAnchorSink.OnLayoutChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TsLayoutCode,UInt32, use_last_error=False)(5, 'OnLayoutChange', ((1, 'lcode'),(1, 'vcView'),)))
    ITextStoreAnchorSink.OnStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'OnStatusChange', ((1, 'dwFlags'),)))
    ITextStoreAnchorSink.OnAttrsChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,UInt32,POINTER(Guid), use_last_error=False)(7, 'OnAttrsChange', ((1, 'paStart'),(1, 'paEnd'),(1, 'cAttrs'),(1, 'paAttrs'),)))
    ITextStoreAnchorSink.OnLockGranted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TEXT_STORE_LOCK_FLAGS, use_last_error=False)(8, 'OnLockGranted', ((1, 'dwLockFlags'),)))
    ITextStoreAnchorSink.OnStartEditTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'OnStartEditTransaction', ()))
    ITextStoreAnchorSink.OnEndEditTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'OnEndEditTransaction', ()))
    return ITextStoreAnchorSink
def _define_ITfLangBarMgr_head():
    class ITfLangBarMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('87955690-e627-11d2-8ddb-00105a2799b5')
    return ITfLangBarMgr
def _define_ITfLangBarMgr():
    ITfLangBarMgr = win32more.UI.TextServices.ITfLangBarMgr_head
    ITfLangBarMgr.AdviseEventSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfLangBarEventSink_head,win32more.Foundation.HWND,UInt32,POINTER(UInt32), use_last_error=False)(3, 'AdviseEventSink', ((1, 'pSink'),(1, 'hwnd'),(1, 'dwFlags'),(1, 'pdwCookie'),)))
    ITfLangBarMgr.UnadviseEventSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'UnadviseEventSink', ((1, 'dwCookie'),)))
    ITfLangBarMgr.GetThreadMarshalInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(5, 'GetThreadMarshalInterface', ((1, 'dwThreadId'),(1, 'dwType'),(1, 'riid'),(1, 'ppunk'),)))
    ITfLangBarMgr.GetThreadLangBarItemMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfLangBarItemMgr_head),POINTER(UInt32), use_last_error=False)(6, 'GetThreadLangBarItemMgr', ((1, 'dwThreadId'),(1, 'pplbi'),(1, 'pdwThreadid'),)))
    ITfLangBarMgr.GetInputProcessorProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfInputProcessorProfiles_head),POINTER(UInt32), use_last_error=False)(7, 'GetInputProcessorProfiles', ((1, 'dwThreadId'),(1, 'ppaip'),(1, 'pdwThreadid'),)))
    ITfLangBarMgr.RestoreLastFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(8, 'RestoreLastFocus', ((1, 'pdwThreadId'),(1, 'fPrev'),)))
    ITfLangBarMgr.SetModalInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfLangBarEventSink_head,UInt32,UInt32, use_last_error=False)(9, 'SetModalInput', ((1, 'pSink'),(1, 'dwThreadId'),(1, 'dwFlags'),)))
    ITfLangBarMgr.ShowFloating = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'ShowFloating', ((1, 'dwFlags'),)))
    ITfLangBarMgr.GetShowFloatingStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'GetShowFloatingStatus', ((1, 'pdwFlags'),)))
    return ITfLangBarMgr
def _define_ITfLangBarEventSink_head():
    class ITfLangBarEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('18a4e900-e0ae-11d2-afdd-00105a2799b5')
    return ITfLangBarEventSink
def _define_ITfLangBarEventSink():
    ITfLangBarEventSink = win32more.UI.TextServices.ITfLangBarEventSink_head
    ITfLangBarEventSink.OnSetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'OnSetFocus', ((1, 'dwThreadId'),)))
    ITfLangBarEventSink.OnThreadTerminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'OnThreadTerminate', ((1, 'dwThreadId'),)))
    ITfLangBarEventSink.OnThreadItemChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'OnThreadItemChange', ((1, 'dwThreadId'),)))
    ITfLangBarEventSink.OnModalInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(6, 'OnModalInput', ((1, 'dwThreadId'),(1, 'uMsg'),(1, 'wParam'),(1, 'lParam'),)))
    ITfLangBarEventSink.ShowFloating = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(7, 'ShowFloating', ((1, 'dwFlags'),)))
    ITfLangBarEventSink.GetItemFloatingRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.Foundation.RECT_head), use_last_error=False)(8, 'GetItemFloatingRect', ((1, 'dwThreadId'),(1, 'rguid'),(1, 'prc'),)))
    return ITfLangBarEventSink
def _define_ITfLangBarItemSink_head():
    class ITfLangBarItemSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('57dbe1a0-de25-11d2-afdd-00105a2799b5')
    return ITfLangBarItemSink
def _define_ITfLangBarItemSink():
    ITfLangBarItemSink = win32more.UI.TextServices.ITfLangBarItemSink_head
    ITfLangBarItemSink.OnUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'OnUpdate', ((1, 'dwFlags'),)))
    return ITfLangBarItemSink
def _define_IEnumTfLangBarItems_head():
    class IEnumTfLangBarItems(win32more.System.Com.IUnknown_head):
        Guid = Guid('583f34d0-de25-11d2-afdd-00105a2799b5')
    return IEnumTfLangBarItems
def _define_IEnumTfLangBarItems():
    IEnumTfLangBarItems = win32more.UI.TextServices.IEnumTfLangBarItems_head
    IEnumTfLangBarItems.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfLangBarItems_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfLangBarItems.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfLangBarItem_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'ppItem'),(1, 'pcFetched'),)))
    IEnumTfLangBarItems.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfLangBarItems.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfLangBarItems
def _define_TF_LANGBARITEMINFO_head():
    class TF_LANGBARITEMINFO(Structure):
        pass
    return TF_LANGBARITEMINFO
def _define_TF_LANGBARITEMINFO():
    TF_LANGBARITEMINFO = win32more.UI.TextServices.TF_LANGBARITEMINFO_head
    TF_LANGBARITEMINFO._fields_ = [
        ("clsidService", Guid),
        ("guidItem", Guid),
        ("dwStyle", UInt32),
        ("ulSort", UInt32),
        ("szDescription", Char * 32),
    ]
    return TF_LANGBARITEMINFO
def _define_ITfLangBarItemMgr_head():
    class ITfLangBarItemMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('ba468c55-9956-4fb1-a59d-52a7dd7cc6aa')
    return ITfLangBarItemMgr
def _define_ITfLangBarItemMgr():
    ITfLangBarItemMgr = win32more.UI.TextServices.ITfLangBarItemMgr_head
    ITfLangBarItemMgr.EnumItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfLangBarItems_head), use_last_error=False)(3, 'EnumItems', ((1, 'ppEnum'),)))
    ITfLangBarItemMgr.GetItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfLangBarItem_head), use_last_error=False)(4, 'GetItem', ((1, 'rguid'),(1, 'ppItem'),)))
    ITfLangBarItemMgr.AddItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfLangBarItem_head, use_last_error=False)(5, 'AddItem', ((1, 'punk'),)))
    ITfLangBarItemMgr.RemoveItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfLangBarItem_head, use_last_error=False)(6, 'RemoveItem', ((1, 'punk'),)))
    ITfLangBarItemMgr.AdviseItemSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfLangBarItemSink_head,POINTER(UInt32),POINTER(Guid), use_last_error=False)(7, 'AdviseItemSink', ((1, 'punk'),(1, 'pdwCookie'),(1, 'rguidItem'),)))
    ITfLangBarItemMgr.UnadviseItemSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'UnadviseItemSink', ((1, 'dwCookie'),)))
    ITfLangBarItemMgr.GetItemFloatingRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.Foundation.RECT_head), use_last_error=False)(9, 'GetItemFloatingRect', ((1, 'dwThreadId'),(1, 'rguid'),(1, 'prc'),)))
    ITfLangBarItemMgr.GetItemsStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt32), use_last_error=False)(10, 'GetItemsStatus', ((1, 'ulCount'),(1, 'prgguid'),(1, 'pdwStatus'),)))
    ITfLangBarItemMgr.GetItemNum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'GetItemNum', ((1, 'pulCount'),)))
    ITfLangBarItemMgr.GetItems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfLangBarItem_head),POINTER(win32more.UI.TextServices.TF_LANGBARITEMINFO),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(12, 'GetItems', ((1, 'ulCount'),(1, 'ppItem'),(1, 'pInfo'),(1, 'pdwStatus'),(1, 'pcFetched'),)))
    ITfLangBarItemMgr.AdviseItemsSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfLangBarItemSink_head),POINTER(Guid),POINTER(UInt32), use_last_error=False)(13, 'AdviseItemsSink', ((1, 'ulCount'),(1, 'ppunk'),(1, 'pguidItem'),(1, 'pdwCookie'),)))
    ITfLangBarItemMgr.UnadviseItemsSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(14, 'UnadviseItemsSink', ((1, 'ulCount'),(1, 'pdwCookie'),)))
    return ITfLangBarItemMgr
def _define_ITfLangBarItem_head():
    class ITfLangBarItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('73540d69-edeb-4ee9-96c9-23aa30b25916')
    return ITfLangBarItem
def _define_ITfLangBarItem():
    ITfLangBarItem = win32more.UI.TextServices.ITfLangBarItem_head
    ITfLangBarItem.GetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TF_LANGBARITEMINFO_head), use_last_error=False)(3, 'GetInfo', ((1, 'pInfo'),)))
    ITfLangBarItem.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetStatus', ((1, 'pdwStatus'),)))
    ITfLangBarItem.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(5, 'Show', ((1, 'fShow'),)))
    ITfLangBarItem.GetTooltipString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'GetTooltipString', ((1, 'pbstrToolTip'),)))
    return ITfLangBarItem
def _define_ITfSystemLangBarItemSink_head():
    class ITfSystemLangBarItemSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('1449d9ab-13cf-4687-aa3e-8d8b18574396')
    return ITfSystemLangBarItemSink
def _define_ITfSystemLangBarItemSink():
    ITfSystemLangBarItemSink = win32more.UI.TextServices.ITfSystemLangBarItemSink_head
    ITfSystemLangBarItemSink.InitMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfMenu_head, use_last_error=False)(3, 'InitMenu', ((1, 'pMenu'),)))
    ITfSystemLangBarItemSink.OnMenuSelect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'OnMenuSelect', ((1, 'wID'),)))
    return ITfSystemLangBarItemSink
def _define_ITfSystemLangBarItem_head():
    class ITfSystemLangBarItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('1e13e9ec-6b33-4d4a-b5eb-8a92f029f356')
    return ITfSystemLangBarItem
def _define_ITfSystemLangBarItem():
    ITfSystemLangBarItem = win32more.UI.TextServices.ITfSystemLangBarItem_head
    ITfSystemLangBarItem.SetIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HICON, use_last_error=False)(3, 'SetIcon', ((1, 'hIcon'),)))
    ITfSystemLangBarItem.SetTooltipString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(4, 'SetTooltipString', ((1, 'pchToolTip'),(1, 'cch'),)))
    return ITfSystemLangBarItem
def _define_ITfSystemLangBarItemText_head():
    class ITfSystemLangBarItemText(win32more.System.Com.IUnknown_head):
        Guid = Guid('5c4ce0e5-ba49-4b52-ac6b-3b397b4f701f')
    return ITfSystemLangBarItemText
def _define_ITfSystemLangBarItemText():
    ITfSystemLangBarItemText = win32more.UI.TextServices.ITfSystemLangBarItemText_head
    ITfSystemLangBarItemText.SetItemText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(3, 'SetItemText', ((1, 'pch'),(1, 'cch'),)))
    ITfSystemLangBarItemText.GetItemText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetItemText', ((1, 'pbstrText'),)))
    return ITfSystemLangBarItemText
def _define_ITfSystemDeviceTypeLangBarItem_head():
    class ITfSystemDeviceTypeLangBarItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('45672eb9-9059-46a2-838d-4530355f6a77')
    return ITfSystemDeviceTypeLangBarItem
def _define_ITfSystemDeviceTypeLangBarItem():
    ITfSystemDeviceTypeLangBarItem = win32more.UI.TextServices.ITfSystemDeviceTypeLangBarItem_head
    ITfSystemDeviceTypeLangBarItem.SetIconMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.LANG_BAR_ITEM_ICON_MODE_FLAGS, use_last_error=False)(3, 'SetIconMode', ((1, 'dwFlags'),)))
    ITfSystemDeviceTypeLangBarItem.GetIconMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetIconMode', ((1, 'pdwFlags'),)))
    return ITfSystemDeviceTypeLangBarItem
TfLBIClick = Int32
TF_LBI_CLK_RIGHT = 1
TF_LBI_CLK_LEFT = 2
def _define_ITfLangBarItemButton_head():
    class ITfLangBarItemButton(win32more.UI.TextServices.ITfLangBarItem_head):
        Guid = Guid('28c7f1d0-de25-11d2-afdd-00105a2799b5')
    return ITfLangBarItemButton
def _define_ITfLangBarItemButton():
    ITfLangBarItemButton = win32more.UI.TextServices.ITfLangBarItemButton_head
    ITfLangBarItemButton.OnClick = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfLBIClick,win32more.Foundation.POINT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(7, 'OnClick', ((1, 'click'),(1, 'pt'),(1, 'prcArea'),)))
    ITfLangBarItemButton.InitMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfMenu_head, use_last_error=False)(8, 'InitMenu', ((1, 'pMenu'),)))
    ITfLangBarItemButton.OnMenuSelect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'OnMenuSelect', ((1, 'wID'),)))
    ITfLangBarItemButton.GetIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.HICON), use_last_error=False)(10, 'GetIcon', ((1, 'phIcon'),)))
    ITfLangBarItemButton.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'GetText', ((1, 'pbstrText'),)))
    return ITfLangBarItemButton
def _define_ITfLangBarItemBitmapButton_head():
    class ITfLangBarItemBitmapButton(win32more.UI.TextServices.ITfLangBarItem_head):
        Guid = Guid('a26a0525-3fae-4fa0-89ee-88a964f9f1b5')
    return ITfLangBarItemBitmapButton
def _define_ITfLangBarItemBitmapButton():
    ITfLangBarItemBitmapButton = win32more.UI.TextServices.ITfLangBarItemBitmapButton_head
    ITfLangBarItemBitmapButton.OnClick = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfLBIClick,win32more.Foundation.POINT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(7, 'OnClick', ((1, 'click'),(1, 'pt'),(1, 'prcArea'),)))
    ITfLangBarItemBitmapButton.InitMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfMenu_head, use_last_error=False)(8, 'InitMenu', ((1, 'pMenu'),)))
    ITfLangBarItemBitmapButton.OnMenuSelect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'OnMenuSelect', ((1, 'wID'),)))
    ITfLangBarItemBitmapButton.GetPreferredSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SIZE_head),POINTER(win32more.Foundation.SIZE_head), use_last_error=False)(10, 'GetPreferredSize', ((1, 'pszDefault'),(1, 'psz'),)))
    ITfLangBarItemBitmapButton.DrawBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(win32more.Graphics.Gdi.HBITMAP),POINTER(win32more.Graphics.Gdi.HBITMAP), use_last_error=False)(11, 'DrawBitmap', ((1, 'bmWidth'),(1, 'bmHeight'),(1, 'dwFlags'),(1, 'phbmp'),(1, 'phbmpMask'),)))
    ITfLangBarItemBitmapButton.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'GetText', ((1, 'pbstrText'),)))
    return ITfLangBarItemBitmapButton
def _define_ITfLangBarItemBitmap_head():
    class ITfLangBarItemBitmap(win32more.UI.TextServices.ITfLangBarItem_head):
        Guid = Guid('73830352-d722-4179-ada5-f045c98df355')
    return ITfLangBarItemBitmap
def _define_ITfLangBarItemBitmap():
    ITfLangBarItemBitmap = win32more.UI.TextServices.ITfLangBarItemBitmap_head
    ITfLangBarItemBitmap.OnClick = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfLBIClick,win32more.Foundation.POINT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(7, 'OnClick', ((1, 'click'),(1, 'pt'),(1, 'prcArea'),)))
    ITfLangBarItemBitmap.GetPreferredSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SIZE_head),POINTER(win32more.Foundation.SIZE_head), use_last_error=False)(8, 'GetPreferredSize', ((1, 'pszDefault'),(1, 'psz'),)))
    ITfLangBarItemBitmap.DrawBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(win32more.Graphics.Gdi.HBITMAP),POINTER(win32more.Graphics.Gdi.HBITMAP), use_last_error=False)(9, 'DrawBitmap', ((1, 'bmWidth'),(1, 'bmHeight'),(1, 'dwFlags'),(1, 'phbmp'),(1, 'phbmpMask'),)))
    return ITfLangBarItemBitmap
TfLBBalloonStyle = Int32
TF_LB_BALLOON_RECO = 0
TF_LB_BALLOON_SHOW = 1
TF_LB_BALLOON_MISS = 2
def _define_TF_LBBALLOONINFO_head():
    class TF_LBBALLOONINFO(Structure):
        pass
    return TF_LBBALLOONINFO
def _define_TF_LBBALLOONINFO():
    TF_LBBALLOONINFO = win32more.UI.TextServices.TF_LBBALLOONINFO_head
    TF_LBBALLOONINFO._fields_ = [
        ("style", win32more.UI.TextServices.TfLBBalloonStyle),
        ("bstrText", win32more.Foundation.BSTR),
    ]
    return TF_LBBALLOONINFO
def _define_ITfLangBarItemBalloon_head():
    class ITfLangBarItemBalloon(win32more.UI.TextServices.ITfLangBarItem_head):
        Guid = Guid('01c2d285-d3c7-4b7b-b5b5-d97411d0c283')
    return ITfLangBarItemBalloon
def _define_ITfLangBarItemBalloon():
    ITfLangBarItemBalloon = win32more.UI.TextServices.ITfLangBarItemBalloon_head
    ITfLangBarItemBalloon.OnClick = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfLBIClick,win32more.Foundation.POINT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(7, 'OnClick', ((1, 'click'),(1, 'pt'),(1, 'prcArea'),)))
    ITfLangBarItemBalloon.GetPreferredSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SIZE_head),POINTER(win32more.Foundation.SIZE_head), use_last_error=False)(8, 'GetPreferredSize', ((1, 'pszDefault'),(1, 'psz'),)))
    ITfLangBarItemBalloon.GetBalloonInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TF_LBBALLOONINFO_head), use_last_error=False)(9, 'GetBalloonInfo', ((1, 'pInfo'),)))
    return ITfLangBarItemBalloon
def _define_ITfMenu_head():
    class ITfMenu(win32more.System.Com.IUnknown_head):
        Guid = Guid('6f8a98e4-aaa0-4f15-8c5b-07e0df0a3dd8')
    return ITfMenu
def _define_ITfMenu():
    ITfMenu = win32more.UI.TextServices.ITfMenu_head
    ITfMenu.AddMenuItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Graphics.Gdi.HBITMAP,win32more.Graphics.Gdi.HBITMAP,POINTER(Char),UInt32,POINTER(win32more.UI.TextServices.ITfMenu_head), use_last_error=False)(3, 'AddMenuItem', ((1, 'uId'),(1, 'dwFlags'),(1, 'hbmp'),(1, 'hbmpMask'),(1, 'pch'),(1, 'cch'),(1, 'ppMenu'),)))
    return ITfMenu
def _define_TF_PERSISTENT_PROPERTY_HEADER_ACP_head():
    class TF_PERSISTENT_PROPERTY_HEADER_ACP(Structure):
        pass
    return TF_PERSISTENT_PROPERTY_HEADER_ACP
def _define_TF_PERSISTENT_PROPERTY_HEADER_ACP():
    TF_PERSISTENT_PROPERTY_HEADER_ACP = win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head
    TF_PERSISTENT_PROPERTY_HEADER_ACP._fields_ = [
        ("guidType", Guid),
        ("ichStart", Int32),
        ("cch", Int32),
        ("cb", UInt32),
        ("dwPrivate", UInt32),
        ("clsidTIP", Guid),
    ]
    return TF_PERSISTENT_PROPERTY_HEADER_ACP
def _define_TF_LANGUAGEPROFILE_head():
    class TF_LANGUAGEPROFILE(Structure):
        pass
    return TF_LANGUAGEPROFILE
def _define_TF_LANGUAGEPROFILE():
    TF_LANGUAGEPROFILE = win32more.UI.TextServices.TF_LANGUAGEPROFILE_head
    TF_LANGUAGEPROFILE._fields_ = [
        ("clsid", Guid),
        ("langid", UInt16),
        ("catid", Guid),
        ("fActive", win32more.Foundation.BOOL),
        ("guidProfile", Guid),
    ]
    return TF_LANGUAGEPROFILE
TfAnchor = Int32
TF_ANCHOR_START = 0
TF_ANCHOR_END = 1
def _define_ITfThreadMgr_head():
    class ITfThreadMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e801-2021-11d2-93e0-0060b067b86e')
    return ITfThreadMgr
def _define_ITfThreadMgr():
    ITfThreadMgr = win32more.UI.TextServices.ITfThreadMgr_head
    ITfThreadMgr.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'Activate', ((1, 'ptid'),)))
    ITfThreadMgr.Deactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Deactivate', ()))
    ITfThreadMgr.CreateDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head), use_last_error=False)(5, 'CreateDocumentMgr', ((1, 'ppdim'),)))
    ITfThreadMgr.EnumDocumentMgrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfDocumentMgrs_head), use_last_error=False)(6, 'EnumDocumentMgrs', ((1, 'ppEnum'),)))
    ITfThreadMgr.GetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head), use_last_error=False)(7, 'GetFocus', ((1, 'ppdimFocus'),)))
    ITfThreadMgr.SetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfDocumentMgr_head, use_last_error=False)(8, 'SetFocus', ((1, 'pdimFocus'),)))
    ITfThreadMgr.AssociateFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.UI.TextServices.ITfDocumentMgr_head,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head), use_last_error=False)(9, 'AssociateFocus', ((1, 'hwnd'),(1, 'pdimNew'),(1, 'ppdimPrev'),)))
    ITfThreadMgr.IsThreadFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(10, 'IsThreadFocus', ((1, 'pfThreadFocus'),)))
    ITfThreadMgr.GetFunctionProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfFunctionProvider_head), use_last_error=False)(11, 'GetFunctionProvider', ((1, 'clsid'),(1, 'ppFuncProv'),)))
    ITfThreadMgr.EnumFunctionProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfFunctionProviders_head), use_last_error=False)(12, 'EnumFunctionProviders', ((1, 'ppEnum'),)))
    ITfThreadMgr.GetGlobalCompartment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfCompartmentMgr_head), use_last_error=False)(13, 'GetGlobalCompartment', ((1, 'ppCompMgr'),)))
    return ITfThreadMgr
def _define_ITfThreadMgrEx_head():
    class ITfThreadMgrEx(win32more.UI.TextServices.ITfThreadMgr_head):
        Guid = Guid('3e90ade3-7594-4cb0-bb58-69628f5f458c')
    return ITfThreadMgrEx
def _define_ITfThreadMgrEx():
    ITfThreadMgrEx = win32more.UI.TextServices.ITfThreadMgrEx_head
    ITfThreadMgrEx.ActivateEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32, use_last_error=False)(14, 'ActivateEx', ((1, 'ptid'),(1, 'dwFlags'),)))
    ITfThreadMgrEx.GetActiveFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(15, 'GetActiveFlags', ((1, 'lpdwFlags'),)))
    return ITfThreadMgrEx
def _define_ITfThreadMgr2_head():
    class ITfThreadMgr2(win32more.System.Com.IUnknown_head):
        Guid = Guid('0ab198ef-6477-4ee8-8812-6780edb82d5e')
    return ITfThreadMgr2
def _define_ITfThreadMgr2():
    ITfThreadMgr2 = win32more.UI.TextServices.ITfThreadMgr2_head
    ITfThreadMgr2.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'Activate', ((1, 'ptid'),)))
    ITfThreadMgr2.Deactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Deactivate', ()))
    ITfThreadMgr2.CreateDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head), use_last_error=False)(5, 'CreateDocumentMgr', ((1, 'ppdim'),)))
    ITfThreadMgr2.EnumDocumentMgrs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfDocumentMgrs_head), use_last_error=False)(6, 'EnumDocumentMgrs', ((1, 'ppEnum'),)))
    ITfThreadMgr2.GetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head), use_last_error=False)(7, 'GetFocus', ((1, 'ppdimFocus'),)))
    ITfThreadMgr2.SetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfDocumentMgr_head, use_last_error=False)(8, 'SetFocus', ((1, 'pdimFocus'),)))
    ITfThreadMgr2.IsThreadFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'IsThreadFocus', ((1, 'pfThreadFocus'),)))
    ITfThreadMgr2.GetFunctionProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfFunctionProvider_head), use_last_error=False)(10, 'GetFunctionProvider', ((1, 'clsid'),(1, 'ppFuncProv'),)))
    ITfThreadMgr2.EnumFunctionProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfFunctionProviders_head), use_last_error=False)(11, 'EnumFunctionProviders', ((1, 'ppEnum'),)))
    ITfThreadMgr2.GetGlobalCompartment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfCompartmentMgr_head), use_last_error=False)(12, 'GetGlobalCompartment', ((1, 'ppCompMgr'),)))
    ITfThreadMgr2.ActivateEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32, use_last_error=False)(13, 'ActivateEx', ((1, 'ptid'),(1, 'dwFlags'),)))
    ITfThreadMgr2.GetActiveFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(14, 'GetActiveFlags', ((1, 'lpdwFlags'),)))
    ITfThreadMgr2.SuspendKeystrokeHandling = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'SuspendKeystrokeHandling', ()))
    ITfThreadMgr2.ResumeKeystrokeHandling = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'ResumeKeystrokeHandling', ()))
    return ITfThreadMgr2
def _define_ITfThreadMgrEventSink_head():
    class ITfThreadMgrEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e80e-2021-11d2-93e0-0060b067b86e')
    return ITfThreadMgrEventSink
def _define_ITfThreadMgrEventSink():
    ITfThreadMgrEventSink = win32more.UI.TextServices.ITfThreadMgrEventSink_head
    ITfThreadMgrEventSink.OnInitDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfDocumentMgr_head, use_last_error=False)(3, 'OnInitDocumentMgr', ((1, 'pdim'),)))
    ITfThreadMgrEventSink.OnUninitDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfDocumentMgr_head, use_last_error=False)(4, 'OnUninitDocumentMgr', ((1, 'pdim'),)))
    ITfThreadMgrEventSink.OnSetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfDocumentMgr_head,win32more.UI.TextServices.ITfDocumentMgr_head, use_last_error=False)(5, 'OnSetFocus', ((1, 'pdimFocus'),(1, 'pdimPrevFocus'),)))
    ITfThreadMgrEventSink.OnPushContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head, use_last_error=False)(6, 'OnPushContext', ((1, 'pic'),)))
    ITfThreadMgrEventSink.OnPopContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head, use_last_error=False)(7, 'OnPopContext', ((1, 'pic'),)))
    return ITfThreadMgrEventSink
def _define_ITfConfigureSystemKeystrokeFeed_head():
    class ITfConfigureSystemKeystrokeFeed(win32more.System.Com.IUnknown_head):
        Guid = Guid('0d2c969a-bc9c-437c-84ee-951c49b1a764')
    return ITfConfigureSystemKeystrokeFeed
def _define_ITfConfigureSystemKeystrokeFeed():
    ITfConfigureSystemKeystrokeFeed = win32more.UI.TextServices.ITfConfigureSystemKeystrokeFeed_head
    ITfConfigureSystemKeystrokeFeed.DisableSystemKeystrokeFeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'DisableSystemKeystrokeFeed', ()))
    ITfConfigureSystemKeystrokeFeed.EnableSystemKeystrokeFeed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'EnableSystemKeystrokeFeed', ()))
    return ITfConfigureSystemKeystrokeFeed
def _define_IEnumTfDocumentMgrs_head():
    class IEnumTfDocumentMgrs(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e808-2021-11d2-93e0-0060b067b86e')
    return IEnumTfDocumentMgrs
def _define_IEnumTfDocumentMgrs():
    IEnumTfDocumentMgrs = win32more.UI.TextServices.IEnumTfDocumentMgrs_head
    IEnumTfDocumentMgrs.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfDocumentMgrs_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfDocumentMgrs.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'rgDocumentMgr'),(1, 'pcFetched'),)))
    IEnumTfDocumentMgrs.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfDocumentMgrs.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfDocumentMgrs
def _define_ITfDocumentMgr_head():
    class ITfDocumentMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e7f4-2021-11d2-93e0-0060b067b86e')
    return ITfDocumentMgr
def _define_ITfDocumentMgr():
    ITfDocumentMgr = win32more.UI.TextServices.ITfDocumentMgr_head
    ITfDocumentMgr.CreateContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.System.Com.IUnknown_head,POINTER(win32more.UI.TextServices.ITfContext_head),POINTER(UInt32), use_last_error=False)(3, 'CreateContext', ((1, 'tidOwner'),(1, 'dwFlags'),(1, 'punk'),(1, 'ppic'),(1, 'pecTextStore'),)))
    ITfDocumentMgr.Push = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head, use_last_error=False)(4, 'Push', ((1, 'pic'),)))
    ITfDocumentMgr.Pop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'Pop', ((1, 'dwFlags'),)))
    ITfDocumentMgr.GetTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfContext_head), use_last_error=False)(6, 'GetTop', ((1, 'ppic'),)))
    ITfDocumentMgr.GetBase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfContext_head), use_last_error=False)(7, 'GetBase', ((1, 'ppic'),)))
    ITfDocumentMgr.EnumContexts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfContexts_head), use_last_error=False)(8, 'EnumContexts', ((1, 'ppEnum'),)))
    return ITfDocumentMgr
def _define_IEnumTfContexts_head():
    class IEnumTfContexts(win32more.System.Com.IUnknown_head):
        Guid = Guid('8f1a7ea6-1654-4502-a86e-b2902344d507')
    return IEnumTfContexts
def _define_IEnumTfContexts():
    IEnumTfContexts = win32more.UI.TextServices.IEnumTfContexts_head
    IEnumTfContexts.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfContexts_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfContexts.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfContext_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'rgContext'),(1, 'pcFetched'),)))
    IEnumTfContexts.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfContexts.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfContexts
def _define_ITfCompositionView_head():
    class ITfCompositionView(win32more.System.Com.IUnknown_head):
        Guid = Guid('d7540241-f9a1-4364-befc-dbcd2c4395b7')
    return ITfCompositionView
def _define_ITfCompositionView():
    ITfCompositionView = win32more.UI.TextServices.ITfCompositionView_head
    ITfCompositionView.GetOwnerClsid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetOwnerClsid', ((1, 'pclsid'),)))
    ITfCompositionView.GetRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfRange_head), use_last_error=False)(4, 'GetRange', ((1, 'ppRange'),)))
    return ITfCompositionView
def _define_IEnumITfCompositionView_head():
    class IEnumITfCompositionView(win32more.System.Com.IUnknown_head):
        Guid = Guid('5efd22ba-7838-46cb-88e2-cadb14124f8f')
    return IEnumITfCompositionView
def _define_IEnumITfCompositionView():
    IEnumITfCompositionView = win32more.UI.TextServices.IEnumITfCompositionView_head
    IEnumITfCompositionView.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumITfCompositionView_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumITfCompositionView.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfCompositionView_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'rgCompositionView'),(1, 'pcFetched'),)))
    IEnumITfCompositionView.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumITfCompositionView.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumITfCompositionView
def _define_ITfComposition_head():
    class ITfComposition(win32more.System.Com.IUnknown_head):
        Guid = Guid('20168d64-5a8f-4a5a-b7bd-cfa29f4d0fd9')
    return ITfComposition
def _define_ITfComposition():
    ITfComposition = win32more.UI.TextServices.ITfComposition_head
    ITfComposition.GetRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfRange_head), use_last_error=False)(3, 'GetRange', ((1, 'ppRange'),)))
    ITfComposition.ShiftStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head, use_last_error=False)(4, 'ShiftStart', ((1, 'ecWrite'),(1, 'pNewStart'),)))
    ITfComposition.ShiftEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head, use_last_error=False)(5, 'ShiftEnd', ((1, 'ecWrite'),(1, 'pNewEnd'),)))
    ITfComposition.EndComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'EndComposition', ((1, 'ecWrite'),)))
    return ITfComposition
def _define_ITfCompositionSink_head():
    class ITfCompositionSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('a781718c-579a-4b15-a280-32b8577acc5e')
    return ITfCompositionSink
def _define_ITfCompositionSink():
    ITfCompositionSink = win32more.UI.TextServices.ITfCompositionSink_head
    ITfCompositionSink.OnCompositionTerminated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfComposition_head, use_last_error=False)(3, 'OnCompositionTerminated', ((1, 'ecWrite'),(1, 'pComposition'),)))
    return ITfCompositionSink
def _define_ITfContextComposition_head():
    class ITfContextComposition(win32more.System.Com.IUnknown_head):
        Guid = Guid('d40c8aae-ac92-4fc7-9a11-0ee0e23aa39b')
    return ITfContextComposition
def _define_ITfContextComposition():
    ITfContextComposition = win32more.UI.TextServices.ITfContextComposition_head
    ITfContextComposition.StartComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfCompositionSink_head,POINTER(win32more.UI.TextServices.ITfComposition_head), use_last_error=False)(3, 'StartComposition', ((1, 'ecWrite'),(1, 'pCompositionRange'),(1, 'pSink'),(1, 'ppComposition'),)))
    ITfContextComposition.EnumCompositions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumITfCompositionView_head), use_last_error=False)(4, 'EnumCompositions', ((1, 'ppEnum'),)))
    ITfContextComposition.FindComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.IEnumITfCompositionView_head), use_last_error=False)(5, 'FindComposition', ((1, 'ecRead'),(1, 'pTestRange'),(1, 'ppEnum'),)))
    ITfContextComposition.TakeOwnership = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfCompositionView_head,win32more.UI.TextServices.ITfCompositionSink_head,POINTER(win32more.UI.TextServices.ITfComposition_head), use_last_error=False)(6, 'TakeOwnership', ((1, 'ecWrite'),(1, 'pComposition'),(1, 'pSink'),(1, 'ppComposition'),)))
    return ITfContextComposition
def _define_ITfContextOwnerCompositionServices_head():
    class ITfContextOwnerCompositionServices(win32more.UI.TextServices.ITfContextComposition_head):
        Guid = Guid('86462810-593b-4916-9764-19c08e9ce110')
    return ITfContextOwnerCompositionServices
def _define_ITfContextOwnerCompositionServices():
    ITfContextOwnerCompositionServices = win32more.UI.TextServices.ITfContextOwnerCompositionServices_head
    ITfContextOwnerCompositionServices.TerminateComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfCompositionView_head, use_last_error=False)(7, 'TerminateComposition', ((1, 'pComposition'),)))
    return ITfContextOwnerCompositionServices
def _define_ITfContextOwnerCompositionSink_head():
    class ITfContextOwnerCompositionSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('5f20aa40-b57a-4f34-96ab-3576f377cc79')
    return ITfContextOwnerCompositionSink
def _define_ITfContextOwnerCompositionSink():
    ITfContextOwnerCompositionSink = win32more.UI.TextServices.ITfContextOwnerCompositionSink_head
    ITfContextOwnerCompositionSink.OnStartComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfCompositionView_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'OnStartComposition', ((1, 'pComposition'),(1, 'pfOk'),)))
    ITfContextOwnerCompositionSink.OnUpdateComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfCompositionView_head,win32more.UI.TextServices.ITfRange_head, use_last_error=False)(4, 'OnUpdateComposition', ((1, 'pComposition'),(1, 'pRangeNew'),)))
    ITfContextOwnerCompositionSink.OnEndComposition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfCompositionView_head, use_last_error=False)(5, 'OnEndComposition', ((1, 'pComposition'),)))
    return ITfContextOwnerCompositionSink
def _define_ITfContextView_head():
    class ITfContextView(win32more.System.Com.IUnknown_head):
        Guid = Guid('2433bf8e-0f9b-435c-ba2c-180611978c30')
    return ITfContextView
def _define_ITfContextView():
    ITfContextView = win32more.UI.TextServices.ITfContextView_head
    ITfContextView.GetRangeFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.POINT_head),UInt32,POINTER(win32more.UI.TextServices.ITfRange_head), use_last_error=False)(3, 'GetRangeFromPoint', ((1, 'ec'),(1, 'ppt'),(1, 'dwFlags'),(1, 'ppRange'),)))
    ITfContextView.GetTextExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetTextExt', ((1, 'ec'),(1, 'pRange'),(1, 'prc'),(1, 'pfClipped'),)))
    ITfContextView.GetScreenExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(5, 'GetScreenExt', ((1, 'prc'),)))
    ITfContextView.GetWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND), use_last_error=False)(6, 'GetWnd', ((1, 'phwnd'),)))
    return ITfContextView
def _define_IEnumTfContextViews_head():
    class IEnumTfContextViews(win32more.System.Com.IUnknown_head):
        Guid = Guid('f0c0f8dd-cf38-44e1-bb0f-68cf0d551c78')
    return IEnumTfContextViews
def _define_IEnumTfContextViews():
    IEnumTfContextViews = win32more.UI.TextServices.IEnumTfContextViews_head
    IEnumTfContextViews.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfContextViews_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfContextViews.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfContextView_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'rgViews'),(1, 'pcFetched'),)))
    IEnumTfContextViews.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfContextViews.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfContextViews
TfActiveSelEnd = Int32
TF_AE_NONE = 0
TF_AE_START = 1
TF_AE_END = 2
def _define_TF_SELECTIONSTYLE_head():
    class TF_SELECTIONSTYLE(Structure):
        pass
    return TF_SELECTIONSTYLE
def _define_TF_SELECTIONSTYLE():
    TF_SELECTIONSTYLE = win32more.UI.TextServices.TF_SELECTIONSTYLE_head
    TF_SELECTIONSTYLE._fields_ = [
        ("ase", win32more.UI.TextServices.TfActiveSelEnd),
        ("fInterimChar", win32more.Foundation.BOOL),
    ]
    return TF_SELECTIONSTYLE
def _define_TF_SELECTION_head():
    class TF_SELECTION(Structure):
        pass
    return TF_SELECTION
def _define_TF_SELECTION():
    TF_SELECTION = win32more.UI.TextServices.TF_SELECTION_head
    TF_SELECTION._fields_ = [
        ("range", win32more.UI.TextServices.ITfRange_head),
        ("style", win32more.UI.TextServices.TF_SELECTIONSTYLE),
    ]
    return TF_SELECTION
def _define_ITfContext_head():
    class ITfContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e7fd-2021-11d2-93e0-0060b067b86e')
    return ITfContext
def _define_ITfContext():
    ITfContext = win32more.UI.TextServices.ITfContext_head
    ITfContext.RequestEditSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfEditSession_head,win32more.UI.TextServices.TF_CONTEXT_EDIT_CONTEXT_FLAGS,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(3, 'RequestEditSession', ((1, 'tid'),(1, 'pes'),(1, 'dwFlags'),(1, 'phrSession'),)))
    ITfContext.InWriteSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'InWriteSession', ((1, 'tid'),(1, 'pfWriteSession'),)))
    ITfContext.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.UI.TextServices.TF_SELECTION),POINTER(UInt32), use_last_error=False)(5, 'GetSelection', ((1, 'ec'),(1, 'ulIndex'),(1, 'ulCount'),(1, 'pSelection'),(1, 'pcFetched'),)))
    ITfContext.SetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.UI.TextServices.TF_SELECTION), use_last_error=False)(6, 'SetSelection', ((1, 'ec'),(1, 'ulCount'),(1, 'pSelection'),)))
    ITfContext.GetStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfRange_head), use_last_error=False)(7, 'GetStart', ((1, 'ec'),(1, 'ppStart'),)))
    ITfContext.GetEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfRange_head), use_last_error=False)(8, 'GetEnd', ((1, 'ec'),(1, 'ppEnd'),)))
    ITfContext.GetActiveView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfContextView_head), use_last_error=False)(9, 'GetActiveView', ((1, 'ppView'),)))
    ITfContext.EnumViews = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfContextViews_head), use_last_error=False)(10, 'EnumViews', ((1, 'ppEnum'),)))
    ITfContext.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TS_STATUS_head), use_last_error=False)(11, 'GetStatus', ((1, 'pdcs'),)))
    ITfContext.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfProperty_head), use_last_error=False)(12, 'GetProperty', ((1, 'guidProp'),(1, 'ppProp'),)))
    ITfContext.GetAppProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfReadOnlyProperty_head), use_last_error=False)(13, 'GetAppProperty', ((1, 'guidProp'),(1, 'ppProp'),)))
    ITfContext.TrackProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(Guid)),UInt32,POINTER(POINTER(Guid)),UInt32,POINTER(win32more.UI.TextServices.ITfReadOnlyProperty_head), use_last_error=False)(14, 'TrackProperties', ((1, 'prgProp'),(1, 'cProp'),(1, 'prgAppProp'),(1, 'cAppProp'),(1, 'ppProperty'),)))
    ITfContext.EnumProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfProperties_head), use_last_error=False)(15, 'EnumProperties', ((1, 'ppEnum'),)))
    ITfContext.GetDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head), use_last_error=False)(16, 'GetDocumentMgr', ((1, 'ppDm'),)))
    ITfContext.CreateRangeBackup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfRangeBackup_head), use_last_error=False)(17, 'CreateRangeBackup', ((1, 'ec'),(1, 'pRange'),(1, 'ppBackup'),)))
    return ITfContext
def _define_ITfQueryEmbedded_head():
    class ITfQueryEmbedded(win32more.System.Com.IUnknown_head):
        Guid = Guid('0fab9bdb-d250-4169-84e5-6be118fdd7a8')
    return ITfQueryEmbedded
def _define_ITfQueryEmbedded():
    ITfQueryEmbedded = win32more.UI.TextServices.ITfQueryEmbedded_head
    ITfQueryEmbedded.QueryInsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'QueryInsertEmbedded', ((1, 'pguidService'),(1, 'pFormatEtc'),(1, 'pfInsertable'),)))
    return ITfQueryEmbedded
def _define_ITfInsertAtSelection_head():
    class ITfInsertAtSelection(win32more.System.Com.IUnknown_head):
        Guid = Guid('55ce16ba-3014-41c1-9ceb-fade1446ac6c')
    return ITfInsertAtSelection
def _define_ITfInsertAtSelection():
    ITfInsertAtSelection = win32more.UI.TextServices.ITfInsertAtSelection_head
    ITfInsertAtSelection.InsertTextAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.INSERT_TEXT_AT_SELECTION_FLAGS,POINTER(Char),Int32,POINTER(win32more.UI.TextServices.ITfRange_head), use_last_error=False)(3, 'InsertTextAtSelection', ((1, 'ec'),(1, 'dwFlags'),(1, 'pchText'),(1, 'cch'),(1, 'ppRange'),)))
    ITfInsertAtSelection.InsertEmbeddedAtSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.System.Com.IDataObject_head,POINTER(win32more.UI.TextServices.ITfRange_head), use_last_error=False)(4, 'InsertEmbeddedAtSelection', ((1, 'ec'),(1, 'dwFlags'),(1, 'pDataObject'),(1, 'ppRange'),)))
    return ITfInsertAtSelection
def _define_ITfCleanupContextSink_head():
    class ITfCleanupContextSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('01689689-7acb-4e9b-ab7c-7ea46b12b522')
    return ITfCleanupContextSink
def _define_ITfCleanupContextSink():
    ITfCleanupContextSink = win32more.UI.TextServices.ITfCleanupContextSink_head
    ITfCleanupContextSink.OnCleanupContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfContext_head, use_last_error=False)(3, 'OnCleanupContext', ((1, 'ecWrite'),(1, 'pic'),)))
    return ITfCleanupContextSink
def _define_ITfCleanupContextDurationSink_head():
    class ITfCleanupContextDurationSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('45c35144-154e-4797-bed8-d33ae7bf8794')
    return ITfCleanupContextDurationSink
def _define_ITfCleanupContextDurationSink():
    ITfCleanupContextDurationSink = win32more.UI.TextServices.ITfCleanupContextDurationSink_head
    ITfCleanupContextDurationSink.OnStartCleanupContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnStartCleanupContext', ()))
    ITfCleanupContextDurationSink.OnEndCleanupContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnEndCleanupContext', ()))
    return ITfCleanupContextDurationSink
def _define_ITfReadOnlyProperty_head():
    class ITfReadOnlyProperty(win32more.System.Com.IUnknown_head):
        Guid = Guid('17d49a3d-f8b8-4b2f-b254-52319dd64c53')
    return ITfReadOnlyProperty
def _define_ITfReadOnlyProperty():
    ITfReadOnlyProperty = win32more.UI.TextServices.ITfReadOnlyProperty_head
    ITfReadOnlyProperty.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetType', ((1, 'pguid'),)))
    ITfReadOnlyProperty.EnumRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.IEnumTfRanges_head),win32more.UI.TextServices.ITfRange_head, use_last_error=False)(4, 'EnumRanges', ((1, 'ec'),(1, 'ppEnum'),(1, 'pTargetRange'),)))
    ITfReadOnlyProperty.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(5, 'GetValue', ((1, 'ec'),(1, 'pRange'),(1, 'pvarValue'),)))
    ITfReadOnlyProperty.GetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfContext_head), use_last_error=False)(6, 'GetContext', ((1, 'ppContext'),)))
    return ITfReadOnlyProperty
def _define_TF_PROPERTYVAL_head():
    class TF_PROPERTYVAL(Structure):
        pass
    return TF_PROPERTYVAL
def _define_TF_PROPERTYVAL():
    TF_PROPERTYVAL = win32more.UI.TextServices.TF_PROPERTYVAL_head
    TF_PROPERTYVAL._fields_ = [
        ("guidId", Guid),
        ("varValue", win32more.System.Com.VARIANT),
    ]
    return TF_PROPERTYVAL
def _define_IEnumTfPropertyValue_head():
    class IEnumTfPropertyValue(win32more.System.Com.IUnknown_head):
        Guid = Guid('8ed8981b-7c10-4d7d-9fb3-ab72e9c75f72')
    return IEnumTfPropertyValue
def _define_IEnumTfPropertyValue():
    IEnumTfPropertyValue = win32more.UI.TextServices.IEnumTfPropertyValue_head
    IEnumTfPropertyValue.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfPropertyValue_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfPropertyValue.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TF_PROPERTYVAL),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'rgValues'),(1, 'pcFetched'),)))
    IEnumTfPropertyValue.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfPropertyValue.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfPropertyValue
def _define_ITfMouseTracker_head():
    class ITfMouseTracker(win32more.System.Com.IUnknown_head):
        Guid = Guid('09d146cd-a544-4132-925b-7afa8ef322d0')
    return ITfMouseTracker
def _define_ITfMouseTracker():
    ITfMouseTracker = win32more.UI.TextServices.ITfMouseTracker_head
    ITfMouseTracker.AdviseMouseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfMouseSink_head,POINTER(UInt32), use_last_error=False)(3, 'AdviseMouseSink', ((1, 'range'),(1, 'pSink'),(1, 'pdwCookie'),)))
    ITfMouseTracker.UnadviseMouseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'UnadviseMouseSink', ((1, 'dwCookie'),)))
    return ITfMouseTracker
def _define_ITfMouseTrackerACP_head():
    class ITfMouseTrackerACP(win32more.System.Com.IUnknown_head):
        Guid = Guid('3bdd78e2-c16e-47fd-b883-ce6facc1a208')
    return ITfMouseTrackerACP
def _define_ITfMouseTrackerACP():
    ITfMouseTrackerACP = win32more.UI.TextServices.ITfMouseTrackerACP_head
    ITfMouseTrackerACP.AdviseMouseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRangeACP_head,win32more.UI.TextServices.ITfMouseSink_head,POINTER(UInt32), use_last_error=False)(3, 'AdviseMouseSink', ((1, 'range'),(1, 'pSink'),(1, 'pdwCookie'),)))
    ITfMouseTrackerACP.UnadviseMouseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'UnadviseMouseSink', ((1, 'dwCookie'),)))
    return ITfMouseTrackerACP
def _define_ITfMouseSink_head():
    class ITfMouseSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('a1adaaa2-3a24-449d-ac96-5183e7f5c217')
    return ITfMouseSink
def _define_ITfMouseSink():
    ITfMouseSink = win32more.UI.TextServices.ITfMouseSink_head
    ITfMouseSink.OnMouseEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'OnMouseEvent', ((1, 'uEdge'),(1, 'uQuadrant'),(1, 'dwBtnStatus'),(1, 'pfEaten'),)))
    return ITfMouseSink
def _define_ITfEditRecord_head():
    class ITfEditRecord(win32more.System.Com.IUnknown_head):
        Guid = Guid('42d4d099-7c1a-4a89-b836-6c6f22160df0')
    return ITfEditRecord
def _define_ITfEditRecord():
    ITfEditRecord = win32more.UI.TextServices.ITfEditRecord_head
    ITfEditRecord.GetSelectionStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'GetSelectionStatus', ((1, 'pfChanged'),)))
    ITfEditRecord.GetTextAndPropertyUpdates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.GET_TEXT_AND_PROPERTY_UPDATES_FLAGS,POINTER(POINTER(Guid)),UInt32,POINTER(win32more.UI.TextServices.IEnumTfRanges_head), use_last_error=False)(4, 'GetTextAndPropertyUpdates', ((1, 'dwFlags'),(1, 'prgProperties'),(1, 'cProperties'),(1, 'ppEnum'),)))
    return ITfEditRecord
def _define_ITfTextEditSink_head():
    class ITfTextEditSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('8127d409-ccd3-4683-967a-b43d5b482bf7')
    return ITfTextEditSink
def _define_ITfTextEditSink():
    ITfTextEditSink = win32more.UI.TextServices.ITfTextEditSink_head
    ITfTextEditSink.OnEndEdit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,UInt32,win32more.UI.TextServices.ITfEditRecord_head, use_last_error=False)(3, 'OnEndEdit', ((1, 'pic'),(1, 'ecReadOnly'),(1, 'pEditRecord'),)))
    return ITfTextEditSink
TfLayoutCode = Int32
TF_LC_CREATE = 0
TF_LC_CHANGE = 1
TF_LC_DESTROY = 2
def _define_ITfTextLayoutSink_head():
    class ITfTextLayoutSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('2af2d06a-dd5b-4927-a0b4-54f19c91fade')
    return ITfTextLayoutSink
def _define_ITfTextLayoutSink():
    ITfTextLayoutSink = win32more.UI.TextServices.ITfTextLayoutSink_head
    ITfTextLayoutSink.OnLayoutChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,win32more.UI.TextServices.TfLayoutCode,win32more.UI.TextServices.ITfContextView_head, use_last_error=False)(3, 'OnLayoutChange', ((1, 'pic'),(1, 'lcode'),(1, 'pView'),)))
    return ITfTextLayoutSink
def _define_ITfStatusSink_head():
    class ITfStatusSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('6b7d8d73-b267-4f69-b32e-1ca321ce4f45')
    return ITfStatusSink
def _define_ITfStatusSink():
    ITfStatusSink = win32more.UI.TextServices.ITfStatusSink_head
    ITfStatusSink.OnStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,UInt32, use_last_error=False)(3, 'OnStatusChange', ((1, 'pic'),(1, 'dwFlags'),)))
    return ITfStatusSink
def _define_ITfEditTransactionSink_head():
    class ITfEditTransactionSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('708fbf70-b520-416b-b06c-2c41ab44f8ba')
    return ITfEditTransactionSink
def _define_ITfEditTransactionSink():
    ITfEditTransactionSink = win32more.UI.TextServices.ITfEditTransactionSink_head
    ITfEditTransactionSink.OnStartEditTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head, use_last_error=False)(3, 'OnStartEditTransaction', ((1, 'pic'),)))
    ITfEditTransactionSink.OnEndEditTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head, use_last_error=False)(4, 'OnEndEditTransaction', ((1, 'pic'),)))
    return ITfEditTransactionSink
def _define_ITfContextOwner_head():
    class ITfContextOwner(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e80c-2021-11d2-93e0-0060b067b86e')
    return ITfContextOwner
def _define_ITfContextOwner():
    ITfContextOwner = win32more.UI.TextServices.ITfContextOwner_head
    ITfContextOwner.GetACPFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.POINT_head),UInt32,POINTER(Int32), use_last_error=False)(3, 'GetACPFromPoint', ((1, 'ptScreen'),(1, 'dwFlags'),(1, 'pacp'),)))
    ITfContextOwner.GetTextExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetTextExt', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'prc'),(1, 'pfClipped'),)))
    ITfContextOwner.GetScreenExt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(5, 'GetScreenExt', ((1, 'prc'),)))
    ITfContextOwner.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TS_STATUS_head), use_last_error=False)(6, 'GetStatus', ((1, 'pdcs'),)))
    ITfContextOwner.GetWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND), use_last_error=False)(7, 'GetWnd', ((1, 'phwnd'),)))
    ITfContextOwner.GetAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'GetAttribute', ((1, 'rguidAttribute'),(1, 'pvarValue'),)))
    return ITfContextOwner
def _define_ITfContextOwnerServices_head():
    class ITfContextOwnerServices(win32more.System.Com.IUnknown_head):
        Guid = Guid('b23eb630-3e1c-11d3-a745-0050040ab407')
    return ITfContextOwnerServices
def _define_ITfContextOwnerServices():
    ITfContextOwnerServices = win32more.UI.TextServices.ITfContextOwnerServices_head
    ITfContextOwnerServices.OnLayoutChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnLayoutChange', ()))
    ITfContextOwnerServices.OnStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'OnStatusChange', ((1, 'dwFlags'),)))
    ITfContextOwnerServices.OnAttributeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(5, 'OnAttributeChange', ((1, 'rguidAttribute'),)))
    ITfContextOwnerServices.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfProperty_head,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head),win32more.System.Com.IStream_head, use_last_error=False)(6, 'Serialize', ((1, 'pProp'),(1, 'pRange'),(1, 'pHdr'),(1, 'pStream'),)))
    ITfContextOwnerServices.Unserialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfProperty_head,POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head),win32more.System.Com.IStream_head,win32more.UI.TextServices.ITfPersistentPropertyLoaderACP_head, use_last_error=False)(7, 'Unserialize', ((1, 'pProp'),(1, 'pHdr'),(1, 'pStream'),(1, 'pLoader'),)))
    ITfContextOwnerServices.ForceLoadProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfProperty_head, use_last_error=False)(8, 'ForceLoadProperty', ((1, 'pProp'),)))
    ITfContextOwnerServices.CreateRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.TextServices.ITfRangeACP_head), use_last_error=False)(9, 'CreateRange', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'ppRange'),)))
    return ITfContextOwnerServices
def _define_ITfContextKeyEventSink_head():
    class ITfContextKeyEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('0552ba5d-c835-4934-bf50-846aaa67432f')
    return ITfContextKeyEventSink
def _define_ITfContextKeyEventSink():
    ITfContextKeyEventSink = win32more.UI.TextServices.ITfContextKeyEventSink_head
    ITfContextKeyEventSink.OnKeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'OnKeyDown', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfContextKeyEventSink.OnKeyUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'OnKeyUp', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfContextKeyEventSink.OnTestKeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'OnTestKeyDown', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfContextKeyEventSink.OnTestKeyUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'OnTestKeyUp', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    return ITfContextKeyEventSink
def _define_ITfEditSession_head():
    class ITfEditSession(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e803-2021-11d2-93e0-0060b067b86e')
    return ITfEditSession
def _define_ITfEditSession():
    ITfEditSession = win32more.UI.TextServices.ITfEditSession_head
    ITfEditSession.DoEditSession = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'DoEditSession', ((1, 'ec'),)))
    return ITfEditSession
TfGravity = Int32
TF_GRAVITY_BACKWARD = 0
TF_GRAVITY_FORWARD = 1
TfShiftDir = Int32
TF_SD_BACKWARD = 0
TF_SD_FORWARD = 1
def _define_TF_HALTCOND_head():
    class TF_HALTCOND(Structure):
        pass
    return TF_HALTCOND
def _define_TF_HALTCOND():
    TF_HALTCOND = win32more.UI.TextServices.TF_HALTCOND_head
    TF_HALTCOND._fields_ = [
        ("pHaltRange", win32more.UI.TextServices.ITfRange_head),
        ("aHaltPos", win32more.UI.TextServices.TfAnchor),
        ("dwFlags", UInt32),
    ]
    return TF_HALTCOND
def _define_ITfRange_head():
    class ITfRange(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e7ff-2021-11d2-93e0-0060b067b86e')
    return ITfRange
def _define_ITfRange():
    ITfRange = win32more.UI.TextServices.ITfRange_head
    ITfRange.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Char),UInt32,POINTER(UInt32), use_last_error=False)(3, 'GetText', ((1, 'ec'),(1, 'dwFlags'),(1, 'pchText'),(1, 'cchMax'),(1, 'pcch'),)))
    ITfRange.SetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Char),Int32, use_last_error=False)(4, 'SetText', ((1, 'ec'),(1, 'dwFlags'),(1, 'pchText'),(1, 'cch'),)))
    ITfRange.GetFormattedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IDataObject_head), use_last_error=False)(5, 'GetFormattedText', ((1, 'ec'),(1, 'ppDataObject'),)))
    ITfRange.GetEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(6, 'GetEmbedded', ((1, 'ec'),(1, 'rguidService'),(1, 'riid'),(1, 'ppunk'),)))
    ITfRange.InsertEmbedded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.System.Com.IDataObject_head, use_last_error=False)(7, 'InsertEmbedded', ((1, 'ec'),(1, 'dwFlags'),(1, 'pDataObject'),)))
    ITfRange.ShiftStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,POINTER(Int32),POINTER(win32more.UI.TextServices.TF_HALTCOND_head), use_last_error=False)(8, 'ShiftStart', ((1, 'ec'),(1, 'cchReq'),(1, 'pcch'),(1, 'pHalt'),)))
    ITfRange.ShiftEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,POINTER(Int32),POINTER(win32more.UI.TextServices.TF_HALTCOND_head), use_last_error=False)(9, 'ShiftEnd', ((1, 'ec'),(1, 'cchReq'),(1, 'pcch'),(1, 'pHalt'),)))
    ITfRange.ShiftStartToRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.TfAnchor, use_last_error=False)(10, 'ShiftStartToRange', ((1, 'ec'),(1, 'pRange'),(1, 'aPos'),)))
    ITfRange.ShiftEndToRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.TfAnchor, use_last_error=False)(11, 'ShiftEndToRange', ((1, 'ec'),(1, 'pRange'),(1, 'aPos'),)))
    ITfRange.ShiftStartRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.TfShiftDir,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'ShiftStartRegion', ((1, 'ec'),(1, 'dir'),(1, 'pfNoRegion'),)))
    ITfRange.ShiftEndRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.TfShiftDir,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'ShiftEndRegion', ((1, 'ec'),(1, 'dir'),(1, 'pfNoRegion'),)))
    ITfRange.IsEmpty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(14, 'IsEmpty', ((1, 'ec'),(1, 'pfEmpty'),)))
    ITfRange.Collapse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.TfAnchor, use_last_error=False)(15, 'Collapse', ((1, 'ec'),(1, 'aPos'),)))
    ITfRange.IsEqualStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.TfAnchor,POINTER(win32more.Foundation.BOOL), use_last_error=False)(16, 'IsEqualStart', ((1, 'ec'),(1, 'pWith'),(1, 'aPos'),(1, 'pfEqual'),)))
    ITfRange.IsEqualEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.TfAnchor,POINTER(win32more.Foundation.BOOL), use_last_error=False)(17, 'IsEqualEnd', ((1, 'ec'),(1, 'pWith'),(1, 'aPos'),(1, 'pfEqual'),)))
    ITfRange.CompareStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.TfAnchor,POINTER(Int32), use_last_error=False)(18, 'CompareStart', ((1, 'ec'),(1, 'pWith'),(1, 'aPos'),(1, 'plResult'),)))
    ITfRange.CompareEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.TfAnchor,POINTER(Int32), use_last_error=False)(19, 'CompareEnd', ((1, 'ec'),(1, 'pWith'),(1, 'aPos'),(1, 'plResult'),)))
    ITfRange.AdjustForInsert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(20, 'AdjustForInsert', ((1, 'ec'),(1, 'cchInsert'),(1, 'pfInsertOk'),)))
    ITfRange.GetGravity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TfGravity),POINTER(win32more.UI.TextServices.TfGravity), use_last_error=False)(21, 'GetGravity', ((1, 'pgStart'),(1, 'pgEnd'),)))
    ITfRange.SetGravity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.TfGravity,win32more.UI.TextServices.TfGravity, use_last_error=False)(22, 'SetGravity', ((1, 'ec'),(1, 'gStart'),(1, 'gEnd'),)))
    ITfRange.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfRange_head), use_last_error=False)(23, 'Clone', ((1, 'ppClone'),)))
    ITfRange.GetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfContext_head), use_last_error=False)(24, 'GetContext', ((1, 'ppContext'),)))
    return ITfRange
def _define_ITfRangeACP_head():
    class ITfRangeACP(win32more.UI.TextServices.ITfRange_head):
        Guid = Guid('057a6296-029b-4154-b79a-0d461d4ea94c')
    return ITfRangeACP
def _define_ITfRangeACP():
    ITfRangeACP = win32more.UI.TextServices.ITfRangeACP_head
    ITfRangeACP.GetExtent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32), use_last_error=False)(25, 'GetExtent', ((1, 'pacpAnchor'),(1, 'pcch'),)))
    ITfRangeACP.SetExtent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(26, 'SetExtent', ((1, 'acpAnchor'),(1, 'cch'),)))
    return ITfRangeACP
def _define_ITextStoreACPServices_head():
    class ITextStoreACPServices(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e901-2021-11d2-93e0-0060b067b86e')
    return ITextStoreACPServices
def _define_ITextStoreACPServices():
    ITextStoreACPServices = win32more.UI.TextServices.ITextStoreACPServices_head
    ITextStoreACPServices.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfProperty_head,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head),win32more.System.Com.IStream_head, use_last_error=False)(3, 'Serialize', ((1, 'pProp'),(1, 'pRange'),(1, 'pHdr'),(1, 'pStream'),)))
    ITextStoreACPServices.Unserialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfProperty_head,POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head),win32more.System.Com.IStream_head,win32more.UI.TextServices.ITfPersistentPropertyLoaderACP_head, use_last_error=False)(4, 'Unserialize', ((1, 'pProp'),(1, 'pHdr'),(1, 'pStream'),(1, 'pLoader'),)))
    ITextStoreACPServices.ForceLoadProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfProperty_head, use_last_error=False)(5, 'ForceLoadProperty', ((1, 'pProp'),)))
    ITextStoreACPServices.CreateRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.TextServices.ITfRangeACP_head), use_last_error=False)(6, 'CreateRange', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'ppRange'),)))
    return ITextStoreACPServices
def _define_ITfRangeBackup_head():
    class ITfRangeBackup(win32more.System.Com.IUnknown_head):
        Guid = Guid('463a506d-6992-49d2-9b88-93d55e70bb16')
    return ITfRangeBackup
def _define_ITfRangeBackup():
    ITfRangeBackup = win32more.UI.TextServices.ITfRangeBackup_head
    ITfRangeBackup.Restore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head, use_last_error=False)(3, 'Restore', ((1, 'ec'),(1, 'pRange'),)))
    return ITfRangeBackup
def _define_ITfPropertyStore_head():
    class ITfPropertyStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('6834b120-88cb-11d2-bf45-00105a2799b5')
    return ITfPropertyStore
def _define_ITfPropertyStore():
    ITfPropertyStore = win32more.UI.TextServices.ITfPropertyStore_head
    ITfPropertyStore.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetType', ((1, 'pguid'),)))
    ITfPropertyStore.GetDataType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetDataType', ((1, 'pdwReserved'),)))
    ITfPropertyStore.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(5, 'GetData', ((1, 'pvarValue'),)))
    ITfPropertyStore.OnTextUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'OnTextUpdated', ((1, 'dwFlags'),(1, 'pRangeNew'),(1, 'pfAccept'),)))
    ITfPropertyStore.Shrink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'Shrink', ((1, 'pRangeNew'),(1, 'pfFree'),)))
    ITfPropertyStore.Divide = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfPropertyStore_head), use_last_error=False)(8, 'Divide', ((1, 'pRangeThis'),(1, 'pRangeNew'),(1, 'ppPropStore'),)))
    ITfPropertyStore.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfPropertyStore_head), use_last_error=False)(9, 'Clone', ((1, 'pPropStore'),)))
    ITfPropertyStore.GetPropertyRangeCreator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(10, 'GetPropertyRangeCreator', ((1, 'pclsid'),)))
    ITfPropertyStore.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(UInt32), use_last_error=False)(11, 'Serialize', ((1, 'pStream'),(1, 'pcb'),)))
    return ITfPropertyStore
def _define_IEnumTfRanges_head():
    class IEnumTfRanges(win32more.System.Com.IUnknown_head):
        Guid = Guid('f99d3f40-8e32-11d2-bf46-00105a2799b5')
    return IEnumTfRanges
def _define_IEnumTfRanges():
    IEnumTfRanges = win32more.UI.TextServices.IEnumTfRanges_head
    IEnumTfRanges.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfRanges_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfRanges.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfRange_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'ppRange'),(1, 'pcFetched'),)))
    IEnumTfRanges.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfRanges.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfRanges
def _define_ITfCreatePropertyStore_head():
    class ITfCreatePropertyStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('2463fbf0-b0af-11d2-afc5-00105a2799b5')
    return ITfCreatePropertyStore
def _define_ITfCreatePropertyStore():
    ITfCreatePropertyStore = win32more.UI.TextServices.ITfCreatePropertyStore_head
    ITfCreatePropertyStore.IsStoreSerializable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfPropertyStore_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'IsStoreSerializable', ((1, 'guidProp'),(1, 'pRange'),(1, 'pPropStore'),(1, 'pfSerializable'),)))
    ITfCreatePropertyStore.CreatePropertyStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.UI.TextServices.ITfRange_head,UInt32,win32more.System.Com.IStream_head,POINTER(win32more.UI.TextServices.ITfPropertyStore_head), use_last_error=False)(4, 'CreatePropertyStore', ((1, 'guidProp'),(1, 'pRange'),(1, 'cb'),(1, 'pStream'),(1, 'ppStore'),)))
    return ITfCreatePropertyStore
def _define_ITfPersistentPropertyLoaderACP_head():
    class ITfPersistentPropertyLoaderACP(win32more.System.Com.IUnknown_head):
        Guid = Guid('4ef89150-0807-11d3-8df0-00105a2799b5')
    return ITfPersistentPropertyLoaderACP
def _define_ITfPersistentPropertyLoaderACP():
    ITfPersistentPropertyLoaderACP = win32more.UI.TextServices.ITfPersistentPropertyLoaderACP_head
    ITfPersistentPropertyLoaderACP.LoadProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TF_PERSISTENT_PROPERTY_HEADER_ACP_head),POINTER(win32more.System.Com.IStream_head), use_last_error=False)(3, 'LoadProperty', ((1, 'pHdr'),(1, 'ppStream'),)))
    return ITfPersistentPropertyLoaderACP
def _define_ITfProperty_head():
    class ITfProperty(win32more.UI.TextServices.ITfReadOnlyProperty_head):
        Guid = Guid('e2449660-9542-11d2-bf46-00105a2799b5')
    return ITfProperty
def _define_ITfProperty():
    ITfProperty = win32more.UI.TextServices.ITfProperty_head
    ITfProperty.FindRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfRange_head),win32more.UI.TextServices.TfAnchor, use_last_error=False)(7, 'FindRange', ((1, 'ec'),(1, 'pRange'),(1, 'ppRange'),(1, 'aPos'),)))
    ITfProperty.SetValueStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfPropertyStore_head, use_last_error=False)(8, 'SetValueStore', ((1, 'ec'),(1, 'pRange'),(1, 'pPropStore'),)))
    ITfProperty.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'SetValue', ((1, 'ec'),(1, 'pRange'),(1, 'pvarValue'),)))
    ITfProperty.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfRange_head, use_last_error=False)(10, 'Clear', ((1, 'ec'),(1, 'pRange'),)))
    return ITfProperty
def _define_IEnumTfProperties_head():
    class IEnumTfProperties(win32more.System.Com.IUnknown_head):
        Guid = Guid('19188cb0-aca9-11d2-afc5-00105a2799b5')
    return IEnumTfProperties
def _define_IEnumTfProperties():
    IEnumTfProperties = win32more.UI.TextServices.IEnumTfProperties_head
    IEnumTfProperties.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfProperties_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfProperties.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfProperty_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'ppProp'),(1, 'pcFetched'),)))
    IEnumTfProperties.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfProperties.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfProperties
def _define_ITfCompartment_head():
    class ITfCompartment(win32more.System.Com.IUnknown_head):
        Guid = Guid('bb08f7a9-607a-4384-8623-056892b64371')
    return ITfCompartment
def _define_ITfCompartment():
    ITfCompartment = win32more.UI.TextServices.ITfCompartment_head
    ITfCompartment.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(3, 'SetValue', ((1, 'tid'),(1, 'pvarValue'),)))
    ITfCompartment.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(4, 'GetValue', ((1, 'pvarValue'),)))
    return ITfCompartment
def _define_ITfCompartmentEventSink_head():
    class ITfCompartmentEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('743abd5f-f26d-48df-8cc5-238492419b64')
    return ITfCompartmentEventSink
def _define_ITfCompartmentEventSink():
    ITfCompartmentEventSink = win32more.UI.TextServices.ITfCompartmentEventSink_head
    ITfCompartmentEventSink.OnChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'OnChange', ((1, 'rguid'),)))
    return ITfCompartmentEventSink
def _define_ITfCompartmentMgr_head():
    class ITfCompartmentMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('7dcf57ac-18ad-438b-824d-979bffb74b7c')
    return ITfCompartmentMgr
def _define_ITfCompartmentMgr():
    ITfCompartmentMgr = win32more.UI.TextServices.ITfCompartmentMgr_head
    ITfCompartmentMgr.GetCompartment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfCompartment_head), use_last_error=False)(3, 'GetCompartment', ((1, 'rguid'),(1, 'ppcomp'),)))
    ITfCompartmentMgr.ClearCompartment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid), use_last_error=False)(4, 'ClearCompartment', ((1, 'tid'),(1, 'rguid'),)))
    ITfCompartmentMgr.EnumCompartments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumGUID_head), use_last_error=False)(5, 'EnumCompartments', ((1, 'ppEnum'),)))
    return ITfCompartmentMgr
def _define_ITfFunction_head():
    class ITfFunction(win32more.System.Com.IUnknown_head):
        Guid = Guid('db593490-098f-11d3-8df0-00105a2799b5')
    return ITfFunction
def _define_ITfFunction():
    ITfFunction = win32more.UI.TextServices.ITfFunction_head
    ITfFunction.GetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetDisplayName', ((1, 'pbstrName'),)))
    return ITfFunction
def _define_ITfFunctionProvider_head():
    class ITfFunctionProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('101d6610-0990-11d3-8df0-00105a2799b5')
    return ITfFunctionProvider
def _define_ITfFunctionProvider():
    ITfFunctionProvider = win32more.UI.TextServices.ITfFunctionProvider_head
    ITfFunctionProvider.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetType', ((1, 'pguid'),)))
    ITfFunctionProvider.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetDescription', ((1, 'pbstrDesc'),)))
    ITfFunctionProvider.GetFunction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(5, 'GetFunction', ((1, 'rguid'),(1, 'riid'),(1, 'ppunk'),)))
    return ITfFunctionProvider
def _define_IEnumTfFunctionProviders_head():
    class IEnumTfFunctionProviders(win32more.System.Com.IUnknown_head):
        Guid = Guid('e4b24db0-0990-11d3-8df0-00105a2799b5')
    return IEnumTfFunctionProviders
def _define_IEnumTfFunctionProviders():
    IEnumTfFunctionProviders = win32more.UI.TextServices.IEnumTfFunctionProviders_head
    IEnumTfFunctionProviders.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfFunctionProviders_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfFunctionProviders.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfFunctionProvider_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'ppCmdobj'),(1, 'pcFetch'),)))
    IEnumTfFunctionProviders.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfFunctionProviders.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfFunctionProviders
def _define_ITfInputProcessorProfiles_head():
    class ITfInputProcessorProfiles(win32more.System.Com.IUnknown_head):
        Guid = Guid('1f02b6c5-7842-4ee6-8a0b-9a24183a95ca')
    return ITfInputProcessorProfiles
def _define_ITfInputProcessorProfiles():
    ITfInputProcessorProfiles = win32more.UI.TextServices.ITfInputProcessorProfiles_head
    ITfInputProcessorProfiles.Register = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'Register', ((1, 'rclsid'),)))
    ITfInputProcessorProfiles.Unregister = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'Unregister', ((1, 'rclsid'),)))
    ITfInputProcessorProfiles.AddLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),POINTER(Char),UInt32,POINTER(Char),UInt32,UInt32, use_last_error=False)(5, 'AddLanguageProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'pchDesc'),(1, 'cchDesc'),(1, 'pchIconFile'),(1, 'cchFile'),(1, 'uIconIndex'),)))
    ITfInputProcessorProfiles.RemoveLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid), use_last_error=False)(6, 'RemoveLanguageProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),)))
    ITfInputProcessorProfiles.EnumInputProcessorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumGUID_head), use_last_error=False)(7, 'EnumInputProcessorInfo', ((1, 'ppEnum'),)))
    ITfInputProcessorProfiles.GetDefaultLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Guid),POINTER(Guid),POINTER(Guid), use_last_error=False)(8, 'GetDefaultLanguageProfile', ((1, 'langid'),(1, 'catid'),(1, 'pclsid'),(1, 'pguidProfile'),)))
    ITfInputProcessorProfiles.SetDefaultLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Guid),POINTER(Guid), use_last_error=False)(9, 'SetDefaultLanguageProfile', ((1, 'langid'),(1, 'rclsid'),(1, 'guidProfiles'),)))
    ITfInputProcessorProfiles.ActivateLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid), use_last_error=False)(10, 'ActivateLanguageProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfiles'),)))
    ITfInputProcessorProfiles.GetActiveLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt16),POINTER(Guid), use_last_error=False)(11, 'GetActiveLanguageProfile', ((1, 'rclsid'),(1, 'plangid'),(1, 'pguidProfile'),)))
    ITfInputProcessorProfiles.GetLanguageProfileDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'GetLanguageProfileDescription', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'pbstrProfile'),)))
    ITfInputProcessorProfiles.GetCurrentLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(13, 'GetCurrentLanguage', ((1, 'plangid'),)))
    ITfInputProcessorProfiles.ChangeCurrentLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(14, 'ChangeCurrentLanguage', ((1, 'langid'),)))
    ITfInputProcessorProfiles.GetLanguageList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(UInt16)),POINTER(UInt32), use_last_error=False)(15, 'GetLanguageList', ((1, 'ppLangId'),(1, 'pulCount'),)))
    ITfInputProcessorProfiles.EnumLanguageProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.UI.TextServices.IEnumTfLanguageProfiles_head), use_last_error=False)(16, 'EnumLanguageProfiles', ((1, 'langid'),(1, 'ppEnum'),)))
    ITfInputProcessorProfiles.EnableLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),win32more.Foundation.BOOL, use_last_error=False)(17, 'EnableLanguageProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'fEnable'),)))
    ITfInputProcessorProfiles.IsEnabledLanguageProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),POINTER(win32more.Foundation.BOOL), use_last_error=False)(18, 'IsEnabledLanguageProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'pfEnable'),)))
    ITfInputProcessorProfiles.EnableLanguageProfileByDefault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),win32more.Foundation.BOOL, use_last_error=False)(19, 'EnableLanguageProfileByDefault', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'fEnable'),)))
    ITfInputProcessorProfiles.SubstituteKeyboardLayout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),win32more.UI.TextServices.HKL, use_last_error=False)(20, 'SubstituteKeyboardLayout', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'hKL'),)))
    return ITfInputProcessorProfiles
def _define_ITfInputProcessorProfilesEx_head():
    class ITfInputProcessorProfilesEx(win32more.UI.TextServices.ITfInputProcessorProfiles_head):
        Guid = Guid('892f230f-fe00-4a41-a98e-fcd6de0d35ef')
    return ITfInputProcessorProfilesEx
def _define_ITfInputProcessorProfilesEx():
    ITfInputProcessorProfilesEx = win32more.UI.TextServices.ITfInputProcessorProfilesEx_head
    ITfInputProcessorProfilesEx.SetLanguageProfileDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),POINTER(Char),UInt32,UInt32, use_last_error=False)(21, 'SetLanguageProfileDisplayName', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'pchFile'),(1, 'cchFile'),(1, 'uResId'),)))
    return ITfInputProcessorProfilesEx
def _define_ITfInputProcessorProfileSubstituteLayout_head():
    class ITfInputProcessorProfileSubstituteLayout(win32more.System.Com.IUnknown_head):
        Guid = Guid('4fd67194-1002-4513-bff2-c0ddf6258552')
    return ITfInputProcessorProfileSubstituteLayout
def _define_ITfInputProcessorProfileSubstituteLayout():
    ITfInputProcessorProfileSubstituteLayout = win32more.UI.TextServices.ITfInputProcessorProfileSubstituteLayout_head
    ITfInputProcessorProfileSubstituteLayout.GetSubstituteKeyboardLayout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),POINTER(win32more.UI.TextServices.HKL), use_last_error=False)(3, 'GetSubstituteKeyboardLayout', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'phKL'),)))
    return ITfInputProcessorProfileSubstituteLayout
def _define_ITfActiveLanguageProfileNotifySink_head():
    class ITfActiveLanguageProfileNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('b246cb75-a93e-4652-bf8c-b3fe0cfd7e57')
    return ITfActiveLanguageProfileNotifySink
def _define_ITfActiveLanguageProfileNotifySink():
    ITfActiveLanguageProfileNotifySink = win32more.UI.TextServices.ITfActiveLanguageProfileNotifySink_head
    ITfActiveLanguageProfileNotifySink.OnActivated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),win32more.Foundation.BOOL, use_last_error=False)(3, 'OnActivated', ((1, 'clsid'),(1, 'guidProfile'),(1, 'fActivated'),)))
    return ITfActiveLanguageProfileNotifySink
def _define_IEnumTfLanguageProfiles_head():
    class IEnumTfLanguageProfiles(win32more.System.Com.IUnknown_head):
        Guid = Guid('3d61bf11-ac5f-42c8-a4cb-931bcc28c744')
    return IEnumTfLanguageProfiles
def _define_IEnumTfLanguageProfiles():
    IEnumTfLanguageProfiles = win32more.UI.TextServices.IEnumTfLanguageProfiles_head
    IEnumTfLanguageProfiles.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfLanguageProfiles_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfLanguageProfiles.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TF_LANGUAGEPROFILE),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'pProfile'),(1, 'pcFetch'),)))
    IEnumTfLanguageProfiles.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfLanguageProfiles.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfLanguageProfiles
def _define_ITfLanguageProfileNotifySink_head():
    class ITfLanguageProfileNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('43c9fe15-f494-4c17-9de2-b8a4ac350aa8')
    return ITfLanguageProfileNotifySink
def _define_ITfLanguageProfileNotifySink():
    ITfLanguageProfileNotifySink = win32more.UI.TextServices.ITfLanguageProfileNotifySink_head
    ITfLanguageProfileNotifySink.OnLanguageChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'OnLanguageChange', ((1, 'langid'),(1, 'pfAccept'),)))
    ITfLanguageProfileNotifySink.OnLanguageChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnLanguageChanged', ()))
    return ITfLanguageProfileNotifySink
def _define_TF_INPUTPROCESSORPROFILE_head():
    class TF_INPUTPROCESSORPROFILE(Structure):
        pass
    return TF_INPUTPROCESSORPROFILE
def _define_TF_INPUTPROCESSORPROFILE():
    TF_INPUTPROCESSORPROFILE = win32more.UI.TextServices.TF_INPUTPROCESSORPROFILE_head
    TF_INPUTPROCESSORPROFILE._fields_ = [
        ("dwProfileType", UInt32),
        ("langid", UInt16),
        ("clsid", Guid),
        ("guidProfile", Guid),
        ("catid", Guid),
        ("hklSubstitute", win32more.UI.TextServices.HKL),
        ("dwCaps", UInt32),
        ("hkl", win32more.UI.TextServices.HKL),
        ("dwFlags", UInt32),
    ]
    return TF_INPUTPROCESSORPROFILE
def _define_ITfInputProcessorProfileMgr_head():
    class ITfInputProcessorProfileMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('71c6e74c-0f28-11d8-a82a-00065b84435c')
    return ITfInputProcessorProfileMgr
def _define_ITfInputProcessorProfileMgr():
    ITfInputProcessorProfileMgr = win32more.UI.TextServices.ITfInputProcessorProfileMgr_head
    ITfInputProcessorProfileMgr.ActivateProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt16,POINTER(Guid),POINTER(Guid),win32more.UI.TextServices.HKL,UInt32, use_last_error=False)(3, 'ActivateProfile', ((1, 'dwProfileType'),(1, 'langid'),(1, 'clsid'),(1, 'guidProfile'),(1, 'hkl'),(1, 'dwFlags'),)))
    ITfInputProcessorProfileMgr.DeactivateProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt16,POINTER(Guid),POINTER(Guid),win32more.UI.TextServices.HKL,UInt32, use_last_error=False)(4, 'DeactivateProfile', ((1, 'dwProfileType'),(1, 'langid'),(1, 'clsid'),(1, 'guidProfile'),(1, 'hkl'),(1, 'dwFlags'),)))
    ITfInputProcessorProfileMgr.GetProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt16,POINTER(Guid),POINTER(Guid),win32more.UI.TextServices.HKL,POINTER(win32more.UI.TextServices.TF_INPUTPROCESSORPROFILE_head), use_last_error=False)(5, 'GetProfile', ((1, 'dwProfileType'),(1, 'langid'),(1, 'clsid'),(1, 'guidProfile'),(1, 'hkl'),(1, 'pProfile'),)))
    ITfInputProcessorProfileMgr.EnumProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.UI.TextServices.IEnumTfInputProcessorProfiles_head), use_last_error=False)(6, 'EnumProfiles', ((1, 'langid'),(1, 'ppEnum'),)))
    ITfInputProcessorProfileMgr.ReleaseInputProcessor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32, use_last_error=False)(7, 'ReleaseInputProcessor', ((1, 'rclsid'),(1, 'dwFlags'),)))
    ITfInputProcessorProfileMgr.RegisterProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),POINTER(Char),UInt32,POINTER(Char),UInt32,UInt32,win32more.UI.TextServices.HKL,UInt32,win32more.Foundation.BOOL,UInt32, use_last_error=False)(8, 'RegisterProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'pchDesc'),(1, 'cchDesc'),(1, 'pchIconFile'),(1, 'cchFile'),(1, 'uIconIndex'),(1, 'hklsubstitute'),(1, 'dwPreferredLayout'),(1, 'bEnabledByDefault'),(1, 'dwFlags'),)))
    ITfInputProcessorProfileMgr.UnregisterProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,POINTER(Guid),UInt32, use_last_error=False)(9, 'UnregisterProfile', ((1, 'rclsid'),(1, 'langid'),(1, 'guidProfile'),(1, 'dwFlags'),)))
    ITfInputProcessorProfileMgr.GetActiveProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.TF_INPUTPROCESSORPROFILE_head), use_last_error=False)(10, 'GetActiveProfile', ((1, 'catid'),(1, 'pProfile'),)))
    return ITfInputProcessorProfileMgr
def _define_IEnumTfInputProcessorProfiles_head():
    class IEnumTfInputProcessorProfiles(win32more.System.Com.IUnknown_head):
        Guid = Guid('71c6e74d-0f28-11d8-a82a-00065b84435c')
    return IEnumTfInputProcessorProfiles
def _define_IEnumTfInputProcessorProfiles():
    IEnumTfInputProcessorProfiles = win32more.UI.TextServices.IEnumTfInputProcessorProfiles_head
    IEnumTfInputProcessorProfiles.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfInputProcessorProfiles_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfInputProcessorProfiles.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TF_INPUTPROCESSORPROFILE),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'pProfile'),(1, 'pcFetch'),)))
    IEnumTfInputProcessorProfiles.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfInputProcessorProfiles.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfInputProcessorProfiles
def _define_ITfInputProcessorProfileActivationSink_head():
    class ITfInputProcessorProfileActivationSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('71c6e74e-0f28-11d8-a82a-00065b84435c')
    return ITfInputProcessorProfileActivationSink
def _define_ITfInputProcessorProfileActivationSink():
    ITfInputProcessorProfileActivationSink = win32more.UI.TextServices.ITfInputProcessorProfileActivationSink_head
    ITfInputProcessorProfileActivationSink.OnActivated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt16,POINTER(Guid),POINTER(Guid),POINTER(Guid),win32more.UI.TextServices.HKL,UInt32, use_last_error=False)(3, 'OnActivated', ((1, 'dwProfileType'),(1, 'langid'),(1, 'clsid'),(1, 'catid'),(1, 'guidProfile'),(1, 'hkl'),(1, 'dwFlags'),)))
    return ITfInputProcessorProfileActivationSink
def _define_TF_PRESERVEDKEY_head():
    class TF_PRESERVEDKEY(Structure):
        pass
    return TF_PRESERVEDKEY
def _define_TF_PRESERVEDKEY():
    TF_PRESERVEDKEY = win32more.UI.TextServices.TF_PRESERVEDKEY_head
    TF_PRESERVEDKEY._fields_ = [
        ("uVKey", UInt32),
        ("uModifiers", UInt32),
    ]
    return TF_PRESERVEDKEY
def _define_ITfKeystrokeMgr_head():
    class ITfKeystrokeMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e7f0-2021-11d2-93e0-0060b067b86e')
    return ITfKeystrokeMgr
def _define_ITfKeystrokeMgr():
    ITfKeystrokeMgr = win32more.UI.TextServices.ITfKeystrokeMgr_head
    ITfKeystrokeMgr.AdviseKeyEventSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.ITfKeyEventSink_head,win32more.Foundation.BOOL, use_last_error=False)(3, 'AdviseKeyEventSink', ((1, 'tid'),(1, 'pSink'),(1, 'fForeground'),)))
    ITfKeystrokeMgr.UnadviseKeyEventSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'UnadviseKeyEventSink', ((1, 'tid'),)))
    ITfKeystrokeMgr.GetForeground = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(5, 'GetForeground', ((1, 'pclsid'),)))
    ITfKeystrokeMgr.TestKeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'TestKeyDown', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeystrokeMgr.TestKeyUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'TestKeyUp', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeystrokeMgr.KeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'KeyDown', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeystrokeMgr.KeyUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'KeyUp', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeystrokeMgr.GetPreservedKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head),POINTER(Guid), use_last_error=False)(10, 'GetPreservedKey', ((1, 'pic'),(1, 'pprekey'),(1, 'pguid'),)))
    ITfKeystrokeMgr.IsPreservedKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'IsPreservedKey', ((1, 'rguid'),(1, 'pprekey'),(1, 'pfRegistered'),)))
    ITfKeystrokeMgr.PreserveKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head),POINTER(Char),UInt32, use_last_error=False)(12, 'PreserveKey', ((1, 'tid'),(1, 'rguid'),(1, 'prekey'),(1, 'pchDesc'),(1, 'cchDesc'),)))
    ITfKeystrokeMgr.UnpreserveKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head), use_last_error=False)(13, 'UnpreserveKey', ((1, 'rguid'),(1, 'pprekey'),)))
    ITfKeystrokeMgr.SetPreservedKeyDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Char),UInt32, use_last_error=False)(14, 'SetPreservedKeyDescription', ((1, 'rguid'),(1, 'pchDesc'),(1, 'cchDesc'),)))
    ITfKeystrokeMgr.GetPreservedKeyDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'GetPreservedKeyDescription', ((1, 'rguid'),(1, 'pbstrDesc'),)))
    ITfKeystrokeMgr.SimulatePreservedKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,POINTER(Guid),POINTER(win32more.Foundation.BOOL), use_last_error=False)(16, 'SimulatePreservedKey', ((1, 'pic'),(1, 'rguid'),(1, 'pfEaten'),)))
    return ITfKeystrokeMgr
def _define_ITfKeyEventSink_head():
    class ITfKeyEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e7f5-2021-11d2-93e0-0060b067b86e')
    return ITfKeyEventSink
def _define_ITfKeyEventSink():
    ITfKeyEventSink = win32more.UI.TextServices.ITfKeyEventSink_head
    ITfKeyEventSink.OnSetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(3, 'OnSetFocus', ((1, 'fForeground'),)))
    ITfKeyEventSink.OnTestKeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'OnTestKeyDown', ((1, 'pic'),(1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeyEventSink.OnTestKeyUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'OnTestKeyUp', ((1, 'pic'),(1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeyEventSink.OnKeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'OnKeyDown', ((1, 'pic'),(1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeyEventSink.OnKeyUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'OnKeyUp', ((1, 'pic'),(1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfKeyEventSink.OnPreservedKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,POINTER(Guid),POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'OnPreservedKey', ((1, 'pic'),(1, 'rguid'),(1, 'pfEaten'),)))
    return ITfKeyEventSink
def _define_ITfKeyTraceEventSink_head():
    class ITfKeyTraceEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('1cd4c13b-1c36-4191-a70a-7f3e611f367d')
    return ITfKeyTraceEventSink
def _define_ITfKeyTraceEventSink():
    ITfKeyTraceEventSink = win32more.UI.TextServices.ITfKeyTraceEventSink_head
    ITfKeyTraceEventSink.OnKeyTraceDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(3, 'OnKeyTraceDown', ((1, 'wParam'),(1, 'lParam'),)))
    ITfKeyTraceEventSink.OnKeyTraceUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(4, 'OnKeyTraceUp', ((1, 'wParam'),(1, 'lParam'),)))
    return ITfKeyTraceEventSink
def _define_ITfPreservedKeyNotifySink_head():
    class ITfPreservedKeyNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('6f77c993-d2b1-446e-853e-5912efc8a286')
    return ITfPreservedKeyNotifySink
def _define_ITfPreservedKeyNotifySink():
    ITfPreservedKeyNotifySink = win32more.UI.TextServices.ITfPreservedKeyNotifySink_head
    ITfPreservedKeyNotifySink.OnUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TF_PRESERVEDKEY_head), use_last_error=False)(3, 'OnUpdated', ((1, 'pprekey'),)))
    return ITfPreservedKeyNotifySink
def _define_ITfMessagePump_head():
    class ITfMessagePump(win32more.System.Com.IUnknown_head):
        Guid = Guid('8f1b8ad8-0b6b-4874-90c5-bd76011e8f7c')
    return ITfMessagePump
def _define_ITfMessagePump():
    ITfMessagePump = win32more.UI.TextServices.ITfMessagePump_head
    ITfMessagePump.PeekMessageA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),win32more.Foundation.HWND,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'PeekMessageA', ((1, 'pMsg'),(1, 'hwnd'),(1, 'wMsgFilterMin'),(1, 'wMsgFilterMax'),(1, 'wRemoveMsg'),(1, 'pfResult'),)))
    ITfMessagePump.GetMessageA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),win32more.Foundation.HWND,UInt32,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'GetMessageA', ((1, 'pMsg'),(1, 'hwnd'),(1, 'wMsgFilterMin'),(1, 'wMsgFilterMax'),(1, 'pfResult'),)))
    ITfMessagePump.PeekMessageW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),win32more.Foundation.HWND,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'PeekMessageW', ((1, 'pMsg'),(1, 'hwnd'),(1, 'wMsgFilterMin'),(1, 'wMsgFilterMax'),(1, 'wRemoveMsg'),(1, 'pfResult'),)))
    ITfMessagePump.GetMessageW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),win32more.Foundation.HWND,UInt32,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'GetMessageW', ((1, 'pMsg'),(1, 'hwnd'),(1, 'wMsgFilterMin'),(1, 'wMsgFilterMax'),(1, 'pfResult'),)))
    return ITfMessagePump
def _define_ITfThreadFocusSink_head():
    class ITfThreadFocusSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('c0f1db0c-3a20-405c-a303-96b6010a885f')
    return ITfThreadFocusSink
def _define_ITfThreadFocusSink():
    ITfThreadFocusSink = win32more.UI.TextServices.ITfThreadFocusSink_head
    ITfThreadFocusSink.OnSetThreadFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnSetThreadFocus', ()))
    ITfThreadFocusSink.OnKillThreadFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnKillThreadFocus', ()))
    return ITfThreadFocusSink
def _define_ITfTextInputProcessor_head():
    class ITfTextInputProcessor(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa80e7f7-2021-11d2-93e0-0060b067b86e')
    return ITfTextInputProcessor
def _define_ITfTextInputProcessor():
    ITfTextInputProcessor = win32more.UI.TextServices.ITfTextInputProcessor_head
    ITfTextInputProcessor.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfThreadMgr_head,UInt32, use_last_error=False)(3, 'Activate', ((1, 'ptim'),(1, 'tid'),)))
    ITfTextInputProcessor.Deactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Deactivate', ()))
    return ITfTextInputProcessor
def _define_ITfTextInputProcessorEx_head():
    class ITfTextInputProcessorEx(win32more.UI.TextServices.ITfTextInputProcessor_head):
        Guid = Guid('6e4e2102-f9cd-433d-b496-303ce03a6507')
    return ITfTextInputProcessorEx
def _define_ITfTextInputProcessorEx():
    ITfTextInputProcessorEx = win32more.UI.TextServices.ITfTextInputProcessorEx_head
    ITfTextInputProcessorEx.ActivateEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfThreadMgr_head,UInt32,UInt32, use_last_error=False)(5, 'ActivateEx', ((1, 'ptim'),(1, 'tid'),(1, 'dwFlags'),)))
    return ITfTextInputProcessorEx
def _define_ITfClientId_head():
    class ITfClientId(win32more.System.Com.IUnknown_head):
        Guid = Guid('d60a7b49-1b9f-4be2-b702-47e9dc05dec3')
    return ITfClientId
def _define_ITfClientId():
    ITfClientId = win32more.UI.TextServices.ITfClientId_head
    ITfClientId.GetClientId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32), use_last_error=False)(3, 'GetClientId', ((1, 'rclsid'),(1, 'ptid'),)))
    return ITfClientId
TF_DA_LINESTYLE = Int32
TF_LS_NONE = 0
TF_LS_SOLID = 1
TF_LS_DOT = 2
TF_LS_DASH = 3
TF_LS_SQUIGGLE = 4
TF_DA_COLORTYPE = Int32
TF_CT_NONE = 0
TF_CT_SYSCOLOR = 1
TF_CT_COLORREF = 2
def _define_TF_DA_COLOR_head():
    class TF_DA_COLOR(Structure):
        pass
    return TF_DA_COLOR
def _define_TF_DA_COLOR():
    TF_DA_COLOR = win32more.UI.TextServices.TF_DA_COLOR_head
    class TF_DA_COLOR__Anonymous_e__Union(Union):
        pass
    TF_DA_COLOR__Anonymous_e__Union._fields_ = [
        ("nIndex", Int32),
        ("cr", UInt32),
    ]
    TF_DA_COLOR._anonymous_ = [
        'Anonymous',
    ]
    TF_DA_COLOR._fields_ = [
        ("type", win32more.UI.TextServices.TF_DA_COLORTYPE),
        ("Anonymous", TF_DA_COLOR__Anonymous_e__Union),
    ]
    return TF_DA_COLOR
TF_DA_ATTR_INFO = Int32
TF_ATTR_INPUT = 0
TF_ATTR_TARGET_CONVERTED = 1
TF_ATTR_CONVERTED = 2
TF_ATTR_TARGET_NOTCONVERTED = 3
TF_ATTR_INPUT_ERROR = 4
TF_ATTR_FIXEDCONVERTED = 5
TF_ATTR_OTHER = -1
def _define_TF_DISPLAYATTRIBUTE_head():
    class TF_DISPLAYATTRIBUTE(Structure):
        pass
    return TF_DISPLAYATTRIBUTE
def _define_TF_DISPLAYATTRIBUTE():
    TF_DISPLAYATTRIBUTE = win32more.UI.TextServices.TF_DISPLAYATTRIBUTE_head
    TF_DISPLAYATTRIBUTE._fields_ = [
        ("crText", win32more.UI.TextServices.TF_DA_COLOR),
        ("crBk", win32more.UI.TextServices.TF_DA_COLOR),
        ("lsStyle", win32more.UI.TextServices.TF_DA_LINESTYLE),
        ("fBoldLine", win32more.Foundation.BOOL),
        ("crLine", win32more.UI.TextServices.TF_DA_COLOR),
        ("bAttr", win32more.UI.TextServices.TF_DA_ATTR_INFO),
    ]
    return TF_DISPLAYATTRIBUTE
def _define_ITfDisplayAttributeInfo_head():
    class ITfDisplayAttributeInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('70528852-2f26-4aea-8c96-215150578932')
    return ITfDisplayAttributeInfo
def _define_ITfDisplayAttributeInfo():
    ITfDisplayAttributeInfo = win32more.UI.TextServices.ITfDisplayAttributeInfo_head
    ITfDisplayAttributeInfo.GetGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetGUID', ((1, 'pguid'),)))
    ITfDisplayAttributeInfo.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetDescription', ((1, 'pbstrDesc'),)))
    ITfDisplayAttributeInfo.GetAttributeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TF_DISPLAYATTRIBUTE_head), use_last_error=False)(5, 'GetAttributeInfo', ((1, 'pda'),)))
    ITfDisplayAttributeInfo.SetAttributeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TF_DISPLAYATTRIBUTE_head), use_last_error=False)(6, 'SetAttributeInfo', ((1, 'pda'),)))
    ITfDisplayAttributeInfo.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Reset', ()))
    return ITfDisplayAttributeInfo
def _define_IEnumTfDisplayAttributeInfo_head():
    class IEnumTfDisplayAttributeInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('7cef04d7-cb75-4e80-a7ab-5f5bc7d332de')
    return IEnumTfDisplayAttributeInfo
def _define_IEnumTfDisplayAttributeInfo():
    IEnumTfDisplayAttributeInfo = win32more.UI.TextServices.IEnumTfDisplayAttributeInfo_head
    IEnumTfDisplayAttributeInfo.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfDisplayAttributeInfo_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfDisplayAttributeInfo.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfDisplayAttributeInfo_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'rgInfo'),(1, 'pcFetched'),)))
    IEnumTfDisplayAttributeInfo.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfDisplayAttributeInfo.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfDisplayAttributeInfo
def _define_ITfDisplayAttributeProvider_head():
    class ITfDisplayAttributeProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('fee47777-163c-4769-996a-6e9c50ad8f54')
    return ITfDisplayAttributeProvider
def _define_ITfDisplayAttributeProvider():
    ITfDisplayAttributeProvider = win32more.UI.TextServices.ITfDisplayAttributeProvider_head
    ITfDisplayAttributeProvider.EnumDisplayAttributeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfDisplayAttributeInfo_head), use_last_error=False)(3, 'EnumDisplayAttributeInfo', ((1, 'ppEnum'),)))
    ITfDisplayAttributeProvider.GetDisplayAttributeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfDisplayAttributeInfo_head), use_last_error=False)(4, 'GetDisplayAttributeInfo', ((1, 'guid'),(1, 'ppInfo'),)))
    return ITfDisplayAttributeProvider
def _define_ITfDisplayAttributeMgr_head():
    class ITfDisplayAttributeMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('8ded7393-5db1-475c-9e71-a39111b0ff67')
    return ITfDisplayAttributeMgr
def _define_ITfDisplayAttributeMgr():
    ITfDisplayAttributeMgr = win32more.UI.TextServices.ITfDisplayAttributeMgr_head
    ITfDisplayAttributeMgr.OnUpdateInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnUpdateInfo', ()))
    ITfDisplayAttributeMgr.EnumDisplayAttributeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfDisplayAttributeInfo_head), use_last_error=False)(4, 'EnumDisplayAttributeInfo', ((1, 'ppEnum'),)))
    ITfDisplayAttributeMgr.GetDisplayAttributeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TextServices.ITfDisplayAttributeInfo_head),POINTER(Guid), use_last_error=False)(5, 'GetDisplayAttributeInfo', ((1, 'guid'),(1, 'ppInfo'),(1, 'pclsidOwner'),)))
    return ITfDisplayAttributeMgr
def _define_ITfDisplayAttributeNotifySink_head():
    class ITfDisplayAttributeNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('ad56f402-e162-4f25-908f-7d577cf9bda9')
    return ITfDisplayAttributeNotifySink
def _define_ITfDisplayAttributeNotifySink():
    ITfDisplayAttributeNotifySink = win32more.UI.TextServices.ITfDisplayAttributeNotifySink_head
    ITfDisplayAttributeNotifySink.OnUpdateInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnUpdateInfo', ()))
    return ITfDisplayAttributeNotifySink
def _define_ITfCategoryMgr_head():
    class ITfCategoryMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('c3acefb5-f69d-4905-938f-fcadcf4be830')
    return ITfCategoryMgr
def _define_ITfCategoryMgr():
    ITfCategoryMgr = win32more.UI.TextServices.ITfCategoryMgr_head
    ITfCategoryMgr.RegisterCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(Guid), use_last_error=False)(3, 'RegisterCategory', ((1, 'rclsid'),(1, 'rcatid'),(1, 'rguid'),)))
    ITfCategoryMgr.UnregisterCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(Guid), use_last_error=False)(4, 'UnregisterCategory', ((1, 'rclsid'),(1, 'rcatid'),(1, 'rguid'),)))
    ITfCategoryMgr.EnumCategoriesInItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IEnumGUID_head), use_last_error=False)(5, 'EnumCategoriesInItem', ((1, 'rguid'),(1, 'ppEnum'),)))
    ITfCategoryMgr.EnumItemsInCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IEnumGUID_head), use_last_error=False)(6, 'EnumItemsInCategory', ((1, 'rcatid'),(1, 'ppEnum'),)))
    ITfCategoryMgr.FindClosestCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(POINTER(Guid)),UInt32, use_last_error=False)(7, 'FindClosestCategory', ((1, 'rguid'),(1, 'pcatid'),(1, 'ppcatidList'),(1, 'ulCount'),)))
    ITfCategoryMgr.RegisterGUIDDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(Char),UInt32, use_last_error=False)(8, 'RegisterGUIDDescription', ((1, 'rclsid'),(1, 'rguid'),(1, 'pchDesc'),(1, 'cch'),)))
    ITfCategoryMgr.UnregisterGUIDDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid), use_last_error=False)(9, 'UnregisterGUIDDescription', ((1, 'rclsid'),(1, 'rguid'),)))
    ITfCategoryMgr.GetGUIDDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'GetGUIDDescription', ((1, 'rguid'),(1, 'pbstrDesc'),)))
    ITfCategoryMgr.RegisterGUIDDWORD = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),UInt32, use_last_error=False)(11, 'RegisterGUIDDWORD', ((1, 'rclsid'),(1, 'rguid'),(1, 'dw'),)))
    ITfCategoryMgr.UnregisterGUIDDWORD = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid), use_last_error=False)(12, 'UnregisterGUIDDWORD', ((1, 'rclsid'),(1, 'rguid'),)))
    ITfCategoryMgr.GetGUIDDWORD = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32), use_last_error=False)(13, 'GetGUIDDWORD', ((1, 'rguid'),(1, 'pdw'),)))
    ITfCategoryMgr.RegisterGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32), use_last_error=False)(14, 'RegisterGUID', ((1, 'rguid'),(1, 'pguidatom'),)))
    ITfCategoryMgr.GetGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid), use_last_error=False)(15, 'GetGUID', ((1, 'guidatom'),(1, 'pguid'),)))
    ITfCategoryMgr.IsEqualTfGuidAtom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.Foundation.BOOL), use_last_error=False)(16, 'IsEqualTfGuidAtom', ((1, 'guidatom'),(1, 'rguid'),(1, 'pfEqual'),)))
    return ITfCategoryMgr
def _define_ITfSource_head():
    class ITfSource(win32more.System.Com.IUnknown_head):
        Guid = Guid('4ea48a35-60ae-446f-8fd6-e6a8d82459f7')
    return ITfSource
def _define_ITfSource():
    ITfSource = win32more.UI.TextServices.ITfSource_head
    ITfSource.AdviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(UInt32), use_last_error=False)(3, 'AdviseSink', ((1, 'riid'),(1, 'punk'),(1, 'pdwCookie'),)))
    ITfSource.UnadviseSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'UnadviseSink', ((1, 'dwCookie'),)))
    return ITfSource
def _define_ITfSourceSingle_head():
    class ITfSourceSingle(win32more.System.Com.IUnknown_head):
        Guid = Guid('73131f9c-56a9-49dd-b0ee-d046633f7528')
    return ITfSourceSingle
def _define_ITfSourceSingle():
    ITfSourceSingle = win32more.UI.TextServices.ITfSourceSingle_head
    ITfSourceSingle.AdviseSingleSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'AdviseSingleSink', ((1, 'tid'),(1, 'riid'),(1, 'punk'),)))
    ITfSourceSingle.UnadviseSingleSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid), use_last_error=False)(4, 'UnadviseSingleSink', ((1, 'tid'),(1, 'riid'),)))
    return ITfSourceSingle
def _define_ITfUIElementMgr_head():
    class ITfUIElementMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('ea1ea135-19df-11d7-a6d2-00065b84435c')
    return ITfUIElementMgr
def _define_ITfUIElementMgr():
    ITfUIElementMgr = win32more.UI.TextServices.ITfUIElementMgr_head
    ITfUIElementMgr.BeginUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfUIElement_head,POINTER(win32more.Foundation.BOOL),POINTER(UInt32), use_last_error=False)(3, 'BeginUIElement', ((1, 'pElement'),(1, 'pbShow'),(1, 'pdwUIElementId'),)))
    ITfUIElementMgr.UpdateUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'UpdateUIElement', ((1, 'dwUIElementId'),)))
    ITfUIElementMgr.EndUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'EndUIElement', ((1, 'dwUIElementId'),)))
    ITfUIElementMgr.GetUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfUIElement_head), use_last_error=False)(6, 'GetUIElement', ((1, 'dwUIELementId'),(1, 'ppElement'),)))
    ITfUIElementMgr.EnumUIElements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfUIElements_head), use_last_error=False)(7, 'EnumUIElements', ((1, 'ppEnum'),)))
    return ITfUIElementMgr
def _define_IEnumTfUIElements_head():
    class IEnumTfUIElements(win32more.System.Com.IUnknown_head):
        Guid = Guid('887aa91e-acba-4931-84da-3c5208cf543f')
    return IEnumTfUIElements
def _define_IEnumTfUIElements():
    IEnumTfUIElements = win32more.UI.TextServices.IEnumTfUIElements_head
    IEnumTfUIElements.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfUIElements_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfUIElements.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfUIElement_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'ppElement'),(1, 'pcFetched'),)))
    IEnumTfUIElements.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfUIElements.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfUIElements
def _define_ITfUIElementSink_head():
    class ITfUIElementSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('ea1ea136-19df-11d7-a6d2-00065b84435c')
    return ITfUIElementSink
def _define_ITfUIElementSink():
    ITfUIElementSink = win32more.UI.TextServices.ITfUIElementSink_head
    ITfUIElementSink.BeginUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'BeginUIElement', ((1, 'dwUIElementId'),(1, 'pbShow'),)))
    ITfUIElementSink.UpdateUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'UpdateUIElement', ((1, 'dwUIElementId'),)))
    ITfUIElementSink.EndUIElement = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'EndUIElement', ((1, 'dwUIElementId'),)))
    return ITfUIElementSink
def _define_ITfUIElement_head():
    class ITfUIElement(win32more.System.Com.IUnknown_head):
        Guid = Guid('ea1ea137-19df-11d7-a6d2-00065b84435c')
    return ITfUIElement
def _define_ITfUIElement():
    ITfUIElement = win32more.UI.TextServices.ITfUIElement_head
    ITfUIElement.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetDescription', ((1, 'pbstrDescription'),)))
    ITfUIElement.GetGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'GetGUID', ((1, 'pguid'),)))
    ITfUIElement.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(5, 'Show', ((1, 'bShow'),)))
    ITfUIElement.IsShown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'IsShown', ((1, 'pbShow'),)))
    return ITfUIElement
def _define_ITfCandidateListUIElement_head():
    class ITfCandidateListUIElement(win32more.UI.TextServices.ITfUIElement_head):
        Guid = Guid('ea1ea138-19df-11d7-a6d2-00065b84435c')
    return ITfCandidateListUIElement
def _define_ITfCandidateListUIElement():
    ITfCandidateListUIElement = win32more.UI.TextServices.ITfCandidateListUIElement_head
    ITfCandidateListUIElement.GetUpdatedFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetUpdatedFlags', ((1, 'pdwFlags'),)))
    ITfCandidateListUIElement.GetDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head), use_last_error=False)(8, 'GetDocumentMgr', ((1, 'ppdim'),)))
    ITfCandidateListUIElement.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetCount', ((1, 'puCount'),)))
    ITfCandidateListUIElement.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'GetSelection', ((1, 'puIndex'),)))
    ITfCandidateListUIElement.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'GetString', ((1, 'uIndex'),(1, 'pstr'),)))
    ITfCandidateListUIElement.GetPageIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32,POINTER(UInt32), use_last_error=False)(12, 'GetPageIndex', ((1, 'pIndex'),(1, 'uSize'),(1, 'puPageCnt'),)))
    ITfCandidateListUIElement.SetPageIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32, use_last_error=False)(13, 'SetPageIndex', ((1, 'pIndex'),(1, 'uPageCnt'),)))
    ITfCandidateListUIElement.GetCurrentPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(14, 'GetCurrentPage', ((1, 'puPage'),)))
    return ITfCandidateListUIElement
def _define_ITfCandidateListUIElementBehavior_head():
    class ITfCandidateListUIElementBehavior(win32more.UI.TextServices.ITfCandidateListUIElement_head):
        Guid = Guid('85fad185-58ce-497a-9460-355366b64b9a')
    return ITfCandidateListUIElementBehavior
def _define_ITfCandidateListUIElementBehavior():
    ITfCandidateListUIElementBehavior = win32more.UI.TextServices.ITfCandidateListUIElementBehavior_head
    ITfCandidateListUIElementBehavior.SetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(15, 'SetSelection', ((1, 'nIndex'),)))
    ITfCandidateListUIElementBehavior.Finalize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'Finalize', ()))
    ITfCandidateListUIElementBehavior.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'Abort', ()))
    return ITfCandidateListUIElementBehavior
def _define_ITfReadingInformationUIElement_head():
    class ITfReadingInformationUIElement(win32more.UI.TextServices.ITfUIElement_head):
        Guid = Guid('ea1ea139-19df-11d7-a6d2-00065b84435c')
    return ITfReadingInformationUIElement
def _define_ITfReadingInformationUIElement():
    ITfReadingInformationUIElement = win32more.UI.TextServices.ITfReadingInformationUIElement_head
    ITfReadingInformationUIElement.GetUpdatedFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'GetUpdatedFlags', ((1, 'pdwFlags'),)))
    ITfReadingInformationUIElement.GetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfContext_head), use_last_error=False)(8, 'GetContext', ((1, 'ppic'),)))
    ITfReadingInformationUIElement.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetString', ((1, 'pstr'),)))
    ITfReadingInformationUIElement.GetMaxReadingStringLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'GetMaxReadingStringLength', ((1, 'pcchMax'),)))
    ITfReadingInformationUIElement.GetErrorIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'GetErrorIndex', ((1, 'pErrorIndex'),)))
    ITfReadingInformationUIElement.IsVerticalOrderPreferred = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'IsVerticalOrderPreferred', ((1, 'pfVertical'),)))
    return ITfReadingInformationUIElement
def _define_ITfTransitoryExtensionUIElement_head():
    class ITfTransitoryExtensionUIElement(win32more.UI.TextServices.ITfUIElement_head):
        Guid = Guid('858f956a-972f-42a2-a2f2-0321e1abe209')
    return ITfTransitoryExtensionUIElement
def _define_ITfTransitoryExtensionUIElement():
    ITfTransitoryExtensionUIElement = win32more.UI.TextServices.ITfTransitoryExtensionUIElement_head
    ITfTransitoryExtensionUIElement.GetDocumentMgr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.ITfDocumentMgr_head), use_last_error=False)(7, 'GetDocumentMgr', ((1, 'ppdim'),)))
    return ITfTransitoryExtensionUIElement
def _define_ITfTransitoryExtensionSink_head():
    class ITfTransitoryExtensionSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('a615096f-1c57-4813-8a15-55ee6e5a839c')
    return ITfTransitoryExtensionSink
def _define_ITfTransitoryExtensionSink():
    ITfTransitoryExtensionSink = win32more.UI.TextServices.ITfTransitoryExtensionSink_head
    ITfTransitoryExtensionSink.OnTransitoryExtensionUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,UInt32,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'OnTransitoryExtensionUpdated', ((1, 'pic'),(1, 'ecReadOnly'),(1, 'pResultRange'),(1, 'pCompositionRange'),(1, 'pfDeleteResultRange'),)))
    return ITfTransitoryExtensionSink
def _define_ITfToolTipUIElement_head():
    class ITfToolTipUIElement(win32more.UI.TextServices.ITfUIElement_head):
        Guid = Guid('52b18b5c-555d-46b2-b00a-fa680144fbdb')
    return ITfToolTipUIElement
def _define_ITfToolTipUIElement():
    ITfToolTipUIElement = win32more.UI.TextServices.ITfToolTipUIElement_head
    ITfToolTipUIElement.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetString', ((1, 'pstr'),)))
    return ITfToolTipUIElement
def _define_ITfReverseConversionList_head():
    class ITfReverseConversionList(win32more.System.Com.IUnknown_head):
        Guid = Guid('151d69f0-86f4-4674-b721-56911e797f47')
    return ITfReverseConversionList
def _define_ITfReverseConversionList():
    ITfReverseConversionList = win32more.UI.TextServices.ITfReverseConversionList_head
    ITfReverseConversionList.GetLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetLength', ((1, 'puIndex'),)))
    ITfReverseConversionList.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetString', ((1, 'uIndex'),(1, 'pbstr'),)))
    return ITfReverseConversionList
def _define_ITfReverseConversion_head():
    class ITfReverseConversion(win32more.System.Com.IUnknown_head):
        Guid = Guid('a415e162-157d-417d-8a8c-0ab26c7d2781')
    return ITfReverseConversion
def _define_ITfReverseConversion():
    ITfReverseConversion = win32more.UI.TextServices.ITfReverseConversion_head
    ITfReverseConversion.DoReverseConversion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.UI.TextServices.ITfReverseConversionList_head), use_last_error=False)(3, 'DoReverseConversion', ((1, 'lpstr'),(1, 'ppList'),)))
    return ITfReverseConversion
def _define_ITfReverseConversionMgr_head():
    class ITfReverseConversionMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('b643c236-c493-41b6-abb3-692412775cc4')
    return ITfReverseConversionMgr
def _define_ITfReverseConversionMgr():
    ITfReverseConversionMgr = win32more.UI.TextServices.ITfReverseConversionMgr_head
    ITfReverseConversionMgr.GetReverseConversion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Guid),UInt32,POINTER(win32more.UI.TextServices.ITfReverseConversion_head), use_last_error=False)(3, 'GetReverseConversion', ((1, 'langid'),(1, 'guidProfile'),(1, 'dwflag'),(1, 'ppReverseConversion'),)))
    return ITfReverseConversionMgr
def _define_ITfCandidateString_head():
    class ITfCandidateString(win32more.System.Com.IUnknown_head):
        Guid = Guid('581f317e-fd9d-443f-b972-ed00467c5d40')
    return ITfCandidateString
def _define_ITfCandidateString():
    ITfCandidateString = win32more.UI.TextServices.ITfCandidateString_head
    ITfCandidateString.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetString', ((1, 'pbstr'),)))
    ITfCandidateString.GetIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetIndex', ((1, 'pnIndex'),)))
    return ITfCandidateString
def _define_IEnumTfCandidates_head():
    class IEnumTfCandidates(win32more.System.Com.IUnknown_head):
        Guid = Guid('defb1926-6c80-4ce8-87d4-d6b72b812bde')
    return IEnumTfCandidates
def _define_IEnumTfCandidates():
    IEnumTfCandidates = win32more.UI.TextServices.IEnumTfCandidates_head
    IEnumTfCandidates.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfCandidates_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfCandidates.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfCandidateString_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'ppCand'),(1, 'pcFetched'),)))
    IEnumTfCandidates.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfCandidates.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfCandidates
TfCandidateResult = Int32
CAND_FINALIZED = 0
CAND_SELECTED = 1
CAND_CANCELED = 2
def _define_ITfCandidateList_head():
    class ITfCandidateList(win32more.System.Com.IUnknown_head):
        Guid = Guid('a3ad50fb-9bdb-49e3-a843-6c76520fbf5d')
    return ITfCandidateList
def _define_ITfCandidateList():
    ITfCandidateList = win32more.UI.TextServices.ITfCandidateList_head
    ITfCandidateList.EnumCandidates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfCandidates_head), use_last_error=False)(3, 'EnumCandidates', ((1, 'ppEnum'),)))
    ITfCandidateList.GetCandidate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.ITfCandidateString_head), use_last_error=False)(4, 'GetCandidate', ((1, 'nIndex'),(1, 'ppCand'),)))
    ITfCandidateList.GetCandidateNum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetCandidateNum', ((1, 'pnCnt'),)))
    ITfCandidateList.SetResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TextServices.TfCandidateResult, use_last_error=False)(6, 'SetResult', ((1, 'nIndex'),(1, 'imcr'),)))
    return ITfCandidateList
def _define_ITfFnReconversion_head():
    class ITfFnReconversion(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('4cea93c0-0a58-11d3-8df0-00105a2799b5')
    return ITfFnReconversion
def _define_ITfFnReconversion():
    ITfFnReconversion = win32more.UI.TextServices.ITfFnReconversion_head
    ITfFnReconversion.QueryRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfRange_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'QueryRange', ((1, 'pRange'),(1, 'ppNewRange'),(1, 'pfConvertable'),)))
    ITfFnReconversion.GetReconversion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfCandidateList_head), use_last_error=False)(5, 'GetReconversion', ((1, 'pRange'),(1, 'ppCandList'),)))
    ITfFnReconversion.Reconvert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head, use_last_error=False)(6, 'Reconvert', ((1, 'pRange'),)))
    return ITfFnReconversion
def _define_ITfFnPlayBack_head():
    class ITfFnPlayBack(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('a3a416a4-0f64-11d3-b5b7-00c04fc324a1')
    return ITfFnPlayBack
def _define_ITfFnPlayBack():
    ITfFnPlayBack = win32more.UI.TextServices.ITfFnPlayBack_head
    ITfFnPlayBack.QueryRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfRange_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'QueryRange', ((1, 'pRange'),(1, 'ppNewRange'),(1, 'pfPlayable'),)))
    ITfFnPlayBack.Play = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head, use_last_error=False)(5, 'Play', ((1, 'pRange'),)))
    return ITfFnPlayBack
def _define_ITfFnLangProfileUtil_head():
    class ITfFnLangProfileUtil(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('a87a8574-a6c1-4e15-99f0-3d3965f548eb')
    return ITfFnLangProfileUtil
def _define_ITfFnLangProfileUtil():
    ITfFnLangProfileUtil = win32more.UI.TextServices.ITfFnLangProfileUtil_head
    ITfFnLangProfileUtil.RegisterActiveProfiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'RegisterActiveProfiles', ()))
    ITfFnLangProfileUtil.IsProfileAvailableForLang = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'IsProfileAvailableForLang', ((1, 'langid'),(1, 'pfAvailable'),)))
    return ITfFnLangProfileUtil
def _define_ITfFnConfigure_head():
    class ITfFnConfigure(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('88f567c6-1757-49f8-a1b2-89234c1eeff9')
    return ITfFnConfigure
def _define_ITfFnConfigure():
    ITfFnConfigure = win32more.UI.TextServices.ITfFnConfigure_head
    ITfFnConfigure.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt16,POINTER(Guid), use_last_error=False)(4, 'Show', ((1, 'hwndParent'),(1, 'langid'),(1, 'rguidProfile'),)))
    return ITfFnConfigure
def _define_ITfFnConfigureRegisterWord_head():
    class ITfFnConfigureRegisterWord(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('bb95808a-6d8f-4bca-8400-5390b586aedf')
    return ITfFnConfigureRegisterWord
def _define_ITfFnConfigureRegisterWord():
    ITfFnConfigureRegisterWord = win32more.UI.TextServices.ITfFnConfigureRegisterWord_head
    ITfFnConfigureRegisterWord.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt16,POINTER(Guid),win32more.Foundation.BSTR, use_last_error=False)(4, 'Show', ((1, 'hwndParent'),(1, 'langid'),(1, 'rguidProfile'),(1, 'bstrRegistered'),)))
    return ITfFnConfigureRegisterWord
def _define_ITfFnConfigureRegisterEudc_head():
    class ITfFnConfigureRegisterEudc(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('b5e26ff5-d7ad-4304-913f-21a2ed95a1b0')
    return ITfFnConfigureRegisterEudc
def _define_ITfFnConfigureRegisterEudc():
    ITfFnConfigureRegisterEudc = win32more.UI.TextServices.ITfFnConfigureRegisterEudc_head
    ITfFnConfigureRegisterEudc.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt16,POINTER(Guid),win32more.Foundation.BSTR, use_last_error=False)(4, 'Show', ((1, 'hwndParent'),(1, 'langid'),(1, 'rguidProfile'),(1, 'bstrRegistered'),)))
    return ITfFnConfigureRegisterEudc
def _define_ITfFnShowHelp_head():
    class ITfFnShowHelp(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('5ab1d30c-094d-4c29-8ea5-0bf59be87bf3')
    return ITfFnShowHelp
def _define_ITfFnShowHelp():
    ITfFnShowHelp = win32more.UI.TextServices.ITfFnShowHelp_head
    ITfFnShowHelp.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(4, 'Show', ((1, 'hwndParent'),)))
    return ITfFnShowHelp
def _define_ITfFnBalloon_head():
    class ITfFnBalloon(win32more.System.Com.IUnknown_head):
        Guid = Guid('3bab89e4-5fbe-45f4-a5bc-dca36ad225a8')
    return ITfFnBalloon
def _define_ITfFnBalloon():
    ITfFnBalloon = win32more.UI.TextServices.ITfFnBalloon_head
    ITfFnBalloon.UpdateBalloon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfLBBalloonStyle,POINTER(Char),UInt32, use_last_error=False)(3, 'UpdateBalloon', ((1, 'style'),(1, 'pch'),(1, 'cch'),)))
    return ITfFnBalloon
TfSapiObject = Int32
GETIF_RESMGR = 0
GETIF_RECOCONTEXT = 1
GETIF_RECOGNIZER = 2
GETIF_VOICE = 3
GETIF_DICTGRAM = 4
GETIF_RECOGNIZERNOINIT = 5
def _define_ITfFnGetSAPIObject_head():
    class ITfFnGetSAPIObject(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('5c0ab7ea-167d-4f59-bfb5-4693755e90ca')
    return ITfFnGetSAPIObject
def _define_ITfFnGetSAPIObject():
    ITfFnGetSAPIObject = win32more.UI.TextServices.ITfFnGetSAPIObject_head
    ITfFnGetSAPIObject.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfSapiObject,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(4, 'Get', ((1, 'sObj'),(1, 'ppunk'),)))
    return ITfFnGetSAPIObject
def _define_ITfFnPropertyUIStatus_head():
    class ITfFnPropertyUIStatus(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('2338ac6e-2b9d-44c0-a75e-ee64f256b3bd')
    return ITfFnPropertyUIStatus
def _define_ITfFnPropertyUIStatus():
    ITfFnPropertyUIStatus = win32more.UI.TextServices.ITfFnPropertyUIStatus_head
    ITfFnPropertyUIStatus.GetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32), use_last_error=False)(4, 'GetStatus', ((1, 'refguidProp'),(1, 'pdw'),)))
    ITfFnPropertyUIStatus.SetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32, use_last_error=False)(5, 'SetStatus', ((1, 'refguidProp'),(1, 'dw'),)))
    return ITfFnPropertyUIStatus
def _define_IEnumSpeechCommands_head():
    class IEnumSpeechCommands(win32more.System.Com.IUnknown_head):
        Guid = Guid('8c5dac4f-083c-4b85-a4c9-71746048adca')
    return IEnumSpeechCommands
def _define_IEnumSpeechCommands():
    IEnumSpeechCommands = win32more.UI.TextServices.IEnumSpeechCommands_head
    IEnumSpeechCommands.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumSpeechCommands_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumSpeechCommands.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(UInt16)),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'pSpCmds'),(1, 'pcFetched'),)))
    IEnumSpeechCommands.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumSpeechCommands.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumSpeechCommands
def _define_ISpeechCommandProvider_head():
    class ISpeechCommandProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('38e09d4c-586d-435a-b592-c8a86691dec6')
    return ISpeechCommandProvider
def _define_ISpeechCommandProvider():
    ISpeechCommandProvider = win32more.UI.TextServices.ISpeechCommandProvider_head
    ISpeechCommandProvider.EnumSpeechCommands = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.UI.TextServices.IEnumSpeechCommands_head), use_last_error=False)(3, 'EnumSpeechCommands', ((1, 'langid'),(1, 'ppEnum'),)))
    ISpeechCommandProvider.ProcessCommand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32,UInt16, use_last_error=False)(4, 'ProcessCommand', ((1, 'pszCommand'),(1, 'cch'),(1, 'langid'),)))
    return ISpeechCommandProvider
def _define_ITfFnCustomSpeechCommand_head():
    class ITfFnCustomSpeechCommand(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('fca6c349-a12f-43a3-8dd6-5a5a4282577b')
    return ITfFnCustomSpeechCommand
def _define_ITfFnCustomSpeechCommand():
    ITfFnCustomSpeechCommand = win32more.UI.TextServices.ITfFnCustomSpeechCommand_head
    ITfFnCustomSpeechCommand.SetSpeechCommandProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(4, 'SetSpeechCommandProvider', ((1, 'pspcmdProvider'),)))
    return ITfFnCustomSpeechCommand
def _define_ITfFnLMProcessor_head():
    class ITfFnLMProcessor(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('7afbf8e7-ac4b-4082-b058-890899d3a010')
    return ITfFnLMProcessor
def _define_ITfFnLMProcessor():
    ITfFnLMProcessor = win32more.UI.TextServices.ITfFnLMProcessor_head
    ITfFnLMProcessor.QueryRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfRange_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'QueryRange', ((1, 'pRange'),(1, 'ppNewRange'),(1, 'pfAccepted'),)))
    ITfFnLMProcessor.QueryLangID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'QueryLangID', ((1, 'langid'),(1, 'pfAccepted'),)))
    ITfFnLMProcessor.GetReconversion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfCandidateList_head), use_last_error=False)(6, 'GetReconversion', ((1, 'pRange'),(1, 'ppCandList'),)))
    ITfFnLMProcessor.Reconvert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head, use_last_error=False)(7, 'Reconvert', ((1, 'pRange'),)))
    ITfFnLMProcessor.QueryKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(8, 'QueryKey', ((1, 'fUp'),(1, 'vKey'),(1, 'lparamKeydata'),(1, 'pfInterested'),)))
    ITfFnLMProcessor.InvokeKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(9, 'InvokeKey', ((1, 'fUp'),(1, 'vKey'),(1, 'lparamKeyData'),)))
    ITfFnLMProcessor.InvokeFunc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfContext_head,POINTER(Guid), use_last_error=False)(10, 'InvokeFunc', ((1, 'pic'),(1, 'refguidFunc'),)))
    return ITfFnLMProcessor
def _define_ITfFnLMInternal_head():
    class ITfFnLMInternal(win32more.UI.TextServices.ITfFnLMProcessor_head):
        Guid = Guid('04b825b1-ac9a-4f7b-b5ad-c7168f1ee445')
    return ITfFnLMInternal
def _define_ITfFnLMInternal():
    ITfFnLMInternal = win32more.UI.TextServices.ITfFnLMInternal_head
    ITfFnLMInternal.ProcessLattice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head, use_last_error=False)(11, 'ProcessLattice', ((1, 'pRange'),)))
    return ITfFnLMInternal
def _define_TF_LMLATTELEMENT_head():
    class TF_LMLATTELEMENT(Structure):
        pass
    return TF_LMLATTELEMENT
def _define_TF_LMLATTELEMENT():
    TF_LMLATTELEMENT = win32more.UI.TextServices.TF_LMLATTELEMENT_head
    class TF_LMLATTELEMENT__Anonymous_e__Union(Union):
        pass
    TF_LMLATTELEMENT__Anonymous_e__Union._fields_ = [
        ("iCost", Int32),
    ]
    TF_LMLATTELEMENT._anonymous_ = [
        'Anonymous',
    ]
    TF_LMLATTELEMENT._fields_ = [
        ("dwFrameStart", UInt32),
        ("dwFrameLen", UInt32),
        ("dwFlags", UInt32),
        ("Anonymous", TF_LMLATTELEMENT__Anonymous_e__Union),
        ("bstrText", win32more.Foundation.BSTR),
    ]
    return TF_LMLATTELEMENT
def _define_IEnumTfLatticeElements_head():
    class IEnumTfLatticeElements(win32more.System.Com.IUnknown_head):
        Guid = Guid('56988052-47da-4a05-911a-e3d941f17145')
    return IEnumTfLatticeElements
def _define_IEnumTfLatticeElements():
    IEnumTfLatticeElements = win32more.UI.TextServices.IEnumTfLatticeElements_head
    IEnumTfLatticeElements.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.IEnumTfLatticeElements_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumTfLatticeElements.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TextServices.TF_LMLATTELEMENT),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'rgsElements'),(1, 'pcFetched'),)))
    IEnumTfLatticeElements.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumTfLatticeElements.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumTfLatticeElements
def _define_ITfLMLattice_head():
    class ITfLMLattice(win32more.System.Com.IUnknown_head):
        Guid = Guid('d4236675-a5bf-4570-9d42-5d6d7b02d59b')
    return ITfLMLattice
def _define_ITfLMLattice():
    ITfLMLattice = win32more.UI.TextServices.ITfLMLattice_head
    ITfLMLattice.QueryType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'QueryType', ((1, 'rguidType'),(1, 'pfSupported'),)))
    ITfLMLattice.EnumLatticeElements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.UI.TextServices.IEnumTfLatticeElements_head), use_last_error=False)(4, 'EnumLatticeElements', ((1, 'dwFrameStart'),(1, 'rguidType'),(1, 'ppEnum'),)))
    return ITfLMLattice
def _define_ITfFnAdviseText_head():
    class ITfFnAdviseText(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('3527268b-7d53-4dd9-92b7-7296ae461249')
    return ITfFnAdviseText
def _define_ITfFnAdviseText():
    ITfFnAdviseText = win32more.UI.TextServices.ITfFnAdviseText_head
    ITfFnAdviseText.OnTextUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(Char),Int32, use_last_error=False)(4, 'OnTextUpdate', ((1, 'pRange'),(1, 'pchText'),(1, 'cch'),)))
    ITfFnAdviseText.OnLatticeUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,win32more.UI.TextServices.ITfLMLattice_head, use_last_error=False)(5, 'OnLatticeUpdate', ((1, 'pRange'),(1, 'pLattice'),)))
    return ITfFnAdviseText
def _define_ITfFnSearchCandidateProvider_head():
    class ITfFnSearchCandidateProvider(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('87a2ad8f-f27b-4920-8501-67602280175d')
    return ITfFnSearchCandidateProvider
def _define_ITfFnSearchCandidateProvider():
    ITfFnSearchCandidateProvider = win32more.UI.TextServices.ITfFnSearchCandidateProvider_head
    ITfFnSearchCandidateProvider.GetSearchCandidates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.UI.TextServices.ITfCandidateList_head), use_last_error=False)(4, 'GetSearchCandidates', ((1, 'bstrQuery'),(1, 'bstrApplicationId'),(1, 'pplist'),)))
    ITfFnSearchCandidateProvider.SetResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(5, 'SetResult', ((1, 'bstrQuery'),(1, 'bstrApplicationID'),(1, 'bstrResult'),)))
    return ITfFnSearchCandidateProvider
TfIntegratableCandidateListSelectionStyle = Int32
STYLE_ACTIVE_SELECTION = 0
STYLE_IMPLIED_SELECTION = 1
def _define_ITfIntegratableCandidateListUIElement_head():
    class ITfIntegratableCandidateListUIElement(win32more.System.Com.IUnknown_head):
        Guid = Guid('c7a6f54f-b180-416f-b2bf-7bf2e4683d7b')
    return ITfIntegratableCandidateListUIElement
def _define_ITfIntegratableCandidateListUIElement():
    ITfIntegratableCandidateListUIElement = win32more.UI.TextServices.ITfIntegratableCandidateListUIElement_head
    ITfIntegratableCandidateListUIElement.SetIntegrationStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(3, 'SetIntegrationStyle', ((1, 'guidIntegrationStyle'),)))
    ITfIntegratableCandidateListUIElement.GetSelectionStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TfIntegratableCandidateListSelectionStyle), use_last_error=False)(4, 'GetSelectionStyle', ((1, 'ptfSelectionStyle'),)))
    ITfIntegratableCandidateListUIElement.OnKeyDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'OnKeyDown', ((1, 'wParam'),(1, 'lParam'),(1, 'pfEaten'),)))
    ITfIntegratableCandidateListUIElement.ShowCandidateNumbers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'ShowCandidateNumbers', ((1, 'pfShow'),)))
    ITfIntegratableCandidateListUIElement.FinalizeExactCompositionString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'FinalizeExactCompositionString', ()))
    return ITfIntegratableCandidateListUIElement
TKBLayoutType = Int32
TKBLT_UNDEFINED = 0
TKBLT_CLASSIC = 1
TKBLT_OPTIMIZED = 2
def _define_ITfFnGetPreferredTouchKeyboardLayout_head():
    class ITfFnGetPreferredTouchKeyboardLayout(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('5f309a41-590a-4acc-a97f-d8efff13fdfc')
    return ITfFnGetPreferredTouchKeyboardLayout
def _define_ITfFnGetPreferredTouchKeyboardLayout():
    ITfFnGetPreferredTouchKeyboardLayout = win32more.UI.TextServices.ITfFnGetPreferredTouchKeyboardLayout_head
    ITfFnGetPreferredTouchKeyboardLayout.GetLayout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TextServices.TKBLayoutType),POINTER(UInt16), use_last_error=False)(4, 'GetLayout', ((1, 'pTKBLayoutType'),(1, 'pwPreferredLayoutId'),)))
    return ITfFnGetPreferredTouchKeyboardLayout
def _define_ITfFnGetLinguisticAlternates_head():
    class ITfFnGetLinguisticAlternates(win32more.UI.TextServices.ITfFunction_head):
        Guid = Guid('ea163ce2-7a65-4506-82a3-c528215da64e')
    return ITfFnGetLinguisticAlternates
def _define_ITfFnGetLinguisticAlternates():
    ITfFnGetLinguisticAlternates = win32more.UI.TextServices.ITfFnGetLinguisticAlternates_head
    ITfFnGetLinguisticAlternates.GetAlternates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.ITfRange_head,POINTER(win32more.UI.TextServices.ITfCandidateList_head), use_last_error=False)(4, 'GetAlternates', ((1, 'pRange'),(1, 'ppCandidateList'),)))
    return ITfFnGetLinguisticAlternates
def _define_IUIManagerEventSink_head():
    class IUIManagerEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('cd91d690-a7e8-4265-9b38-8bb3bbaba7de')
    return IUIManagerEventSink
def _define_IUIManagerEventSink():
    IUIManagerEventSink = win32more.UI.TextServices.IUIManagerEventSink_head
    IUIManagerEventSink.OnWindowOpening = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(3, 'OnWindowOpening', ((1, 'prcBounds'),)))
    IUIManagerEventSink.OnWindowOpened = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(4, 'OnWindowOpened', ((1, 'prcBounds'),)))
    IUIManagerEventSink.OnWindowUpdating = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(5, 'OnWindowUpdating', ((1, 'prcUpdatedBounds'),)))
    IUIManagerEventSink.OnWindowUpdated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(6, 'OnWindowUpdated', ((1, 'prcUpdatedBounds'),)))
    IUIManagerEventSink.OnWindowClosing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'OnWindowClosing', ()))
    IUIManagerEventSink.OnWindowClosed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'OnWindowClosed', ()))
    return IUIManagerEventSink
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
def _define_ITfInputScope_head():
    class ITfInputScope(win32more.System.Com.IUnknown_head):
        Guid = Guid('fde1eaee-6924-4cdf-91e7-da38cff5559d')
    return ITfInputScope
def _define_ITfInputScope():
    ITfInputScope = win32more.UI.TextServices.ITfInputScope_head
    ITfInputScope.GetInputScopes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.TextServices.InputScope)),POINTER(UInt32), use_last_error=False)(3, 'GetInputScopes', ((1, 'pprgInputScopes'),(1, 'pcCount'),)))
    ITfInputScope.GetPhrase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Foundation.BSTR)),POINTER(UInt32), use_last_error=False)(4, 'GetPhrase', ((1, 'ppbstrPhrases'),(1, 'pcCount'),)))
    ITfInputScope.GetRegularExpression = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'GetRegularExpression', ((1, 'pbstrRegExp'),)))
    ITfInputScope.GetSRGS = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'GetSRGS', ((1, 'pbstrSRGS'),)))
    ITfInputScope.GetXML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetXML', ((1, 'pbstrXML'),)))
    return ITfInputScope
def _define_ITfInputScope2_head():
    class ITfInputScope2(win32more.UI.TextServices.ITfInputScope_head):
        Guid = Guid('5731eaa0-6bc2-4681-a532-92fbb74d7c41')
    return ITfInputScope2
def _define_ITfInputScope2():
    ITfInputScope2 = win32more.UI.TextServices.ITfInputScope2_head
    ITfInputScope2.EnumWordList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumString_head), use_last_error=False)(8, 'EnumWordList', ((1, 'ppEnumString'),)))
    return ITfInputScope2
MSAAControl = Guid('08cd963f-7a3e-4f5c-9bd8-d692bb043c5b')
AccStore = Guid('5440837f-4bff-4ae5-a1b1-7722ecc6332a')
AccDictionary = Guid('6572ee16-5fe5-4331-bb6d-76a49c56e423')
AccServerDocMgr = Guid('6089a37e-eb8a-482d-bd6f-f9f46904d16d')
AccClientDocMgr = Guid('fc48cc30-4f3e-4fa1-803b-ad0e196a83b1')
DocWrap = Guid('bf426f7e-7a5e-44d6-830c-a390ea9462a3')
def _define_ITfMSAAControl_head():
    class ITfMSAAControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('b5f8fb3b-393f-4f7c-84cb-504924c2705a')
    return ITfMSAAControl
def _define_ITfMSAAControl():
    ITfMSAAControl = win32more.UI.TextServices.ITfMSAAControl_head
    ITfMSAAControl.SystemEnableMSAA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'SystemEnableMSAA', ()))
    ITfMSAAControl.SystemDisableMSAA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'SystemDisableMSAA', ()))
    return ITfMSAAControl
def _define_IInternalDocWrap_head():
    class IInternalDocWrap(win32more.System.Com.IUnknown_head):
        Guid = Guid('e1aa6466-9db4-40ba-be03-77c38e8e60b2')
    return IInternalDocWrap
def _define_IInternalDocWrap():
    IInternalDocWrap = win32more.UI.TextServices.IInternalDocWrap_head
    IInternalDocWrap.NotifyRevoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'NotifyRevoke', ()))
    return IInternalDocWrap
def _define_ITextStoreACPEx_head():
    class ITextStoreACPEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('a2de3bc2-3d8e-11d3-81a9-f753fbe61a00')
    return ITextStoreACPEx
def _define_ITextStoreACPEx():
    ITextStoreACPEx = win32more.UI.TextServices.ITextStoreACPEx_head
    ITextStoreACPEx.ScrollToRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Foundation.RECT,UInt32, use_last_error=False)(3, 'ScrollToRect', ((1, 'acpStart'),(1, 'acpEnd'),(1, 'rc'),(1, 'dwPosition'),)))
    return ITextStoreACPEx
def _define_ITextStoreAnchorEx_head():
    class ITextStoreAnchorEx(win32more.System.Com.IUnknown_head):
        Guid = Guid('a2de3bc1-3d8e-11d3-81a9-f753fbe61a00')
    return ITextStoreAnchorEx
def _define_ITextStoreAnchorEx():
    ITextStoreAnchorEx = win32more.UI.TextServices.ITextStoreAnchorEx_head
    ITextStoreAnchorEx.ScrollToRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.IAnchor_head,win32more.UI.TextServices.IAnchor_head,win32more.Foundation.RECT,UInt32, use_last_error=False)(3, 'ScrollToRect', ((1, 'pStart'),(1, 'pEnd'),(1, 'rc'),(1, 'dwPosition'),)))
    return ITextStoreAnchorEx
def _define_ITextStoreACPSinkEx_head():
    class ITextStoreACPSinkEx(win32more.UI.TextServices.ITextStoreACPSink_head):
        Guid = Guid('2bdf9464-41e2-43e3-950c-a6865ba25cd4')
    return ITextStoreACPSinkEx
def _define_ITextStoreACPSinkEx():
    ITextStoreACPSinkEx = win32more.UI.TextServices.ITextStoreACPSinkEx_head
    ITextStoreACPSinkEx.OnDisconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'OnDisconnect', ()))
    return ITextStoreACPSinkEx
def _define_ITextStoreSinkAnchorEx_head():
    class ITextStoreSinkAnchorEx(win32more.UI.TextServices.ITextStoreAnchorSink_head):
        Guid = Guid('25642426-028d-4474-977b-111bb114fe3e')
    return ITextStoreSinkAnchorEx
def _define_ITextStoreSinkAnchorEx():
    ITextStoreSinkAnchorEx = win32more.UI.TextServices.ITextStoreSinkAnchorEx_head
    ITextStoreSinkAnchorEx.OnDisconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'OnDisconnect', ()))
    return ITextStoreSinkAnchorEx
def _define_IAccDictionary_head():
    class IAccDictionary(win32more.System.Com.IUnknown_head):
        Guid = Guid('1dc4cb5f-d737-474d-ade9-5ccfc9bc1cc9')
    return IAccDictionary
def _define_IAccDictionary():
    IAccDictionary = win32more.UI.TextServices.IAccDictionary_head
    IAccDictionary.GetLocalizedString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.Foundation.BSTR),POINTER(UInt32), use_last_error=False)(3, 'GetLocalizedString', ((1, 'Term'),(1, 'lcid'),(1, 'pResult'),(1, 'plcid'),)))
    IAccDictionary.GetParentTerm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid), use_last_error=False)(4, 'GetParentTerm', ((1, 'Term'),(1, 'pParentTerm'),)))
    IAccDictionary.GetMnemonicString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.BSTR), use_last_error=False)(5, 'GetMnemonicString', ((1, 'Term'),(1, 'pResult'),)))
    IAccDictionary.LookupMnemonicTerm = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Guid), use_last_error=False)(6, 'LookupMnemonicTerm', ((1, 'bstrMnemonic'),(1, 'pTerm'),)))
    IAccDictionary.ConvertValueToString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,win32more.System.Com.VARIANT,POINTER(win32more.Foundation.BSTR),POINTER(UInt32), use_last_error=False)(7, 'ConvertValueToString', ((1, 'Term'),(1, 'lcid'),(1, 'varValue'),(1, 'pbstrResult'),(1, 'plcid'),)))
    return IAccDictionary
def _define_IVersionInfo_head():
    class IVersionInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('401518ec-db00-4611-9b29-2a0e4b9afa85')
    return IVersionInfo
def _define_IVersionInfo():
    IVersionInfo = win32more.UI.TextServices.IVersionInfo_head
    IVersionInfo.GetSubcomponentCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(3, 'GetSubcomponentCount', ((1, 'ulSub'),(1, 'ulCount'),)))
    IVersionInfo.GetImplementationID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid), use_last_error=False)(4, 'GetImplementationID', ((1, 'ulSub'),(1, 'implid'),)))
    IVersionInfo.GetBuildVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(5, 'GetBuildVersion', ((1, 'ulSub'),(1, 'pdwMajor'),(1, 'pdwMinor'),)))
    IVersionInfo.GetComponentDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'GetComponentDescription', ((1, 'ulSub'),(1, 'pImplStr'),)))
    IVersionInfo.GetInstanceDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetInstanceDescription', ((1, 'ulSub'),(1, 'pImplStr'),)))
    return IVersionInfo
def _define_ICoCreateLocally_head():
    class ICoCreateLocally(win32more.System.Com.IUnknown_head):
        Guid = Guid('03de00aa-f272-41e3-99cb-03c5e8114ea0')
    return ICoCreateLocally
def _define_ICoCreateLocally():
    ICoCreateLocally = win32more.UI.TextServices.ICoCreateLocally_head
    ICoCreateLocally.CoCreateLocally = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head),POINTER(Guid),win32more.System.Com.IUnknown_head,win32more.System.Com.VARIANT, use_last_error=False)(3, 'CoCreateLocally', ((1, 'rclsid'),(1, 'dwClsContext'),(1, 'riid'),(1, 'punk'),(1, 'riidParam'),(1, 'punkParam'),(1, 'varParam'),)))
    return ICoCreateLocally
def _define_ICoCreatedLocally_head():
    class ICoCreatedLocally(win32more.System.Com.IUnknown_head):
        Guid = Guid('0a53eb6c-1908-4742-8cff-2cee2e93f94c')
    return ICoCreatedLocally
def _define_ICoCreatedLocally():
    ICoCreatedLocally = win32more.UI.TextServices.ICoCreatedLocally_head
    ICoCreatedLocally.LocalInit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),win32more.System.Com.IUnknown_head,win32more.System.Com.VARIANT, use_last_error=False)(3, 'LocalInit', ((1, 'punkLocalObject'),(1, 'riidParam'),(1, 'punkParam'),(1, 'varParam'),)))
    return ICoCreatedLocally
def _define_IAccStore_head():
    class IAccStore(win32more.System.Com.IUnknown_head):
        Guid = Guid('e2cd4a63-2b72-4d48-b739-95e4765195ba')
    return IAccStore
def _define_IAccStore():
    IAccStore = win32more.UI.TextServices.IAccStore_head
    IAccStore.Register = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'Register', ((1, 'riid'),(1, 'punk'),)))
    IAccStore.Unregister = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(4, 'Unregister', ((1, 'punk'),)))
    IAccStore.GetDocuments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumUnknown_head), use_last_error=False)(5, 'GetDocuments', ((1, 'enumUnknown'),)))
    IAccStore.LookupByHWND = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(6, 'LookupByHWND', ((1, 'hWnd'),(1, 'riid'),(1, 'ppunk'),)))
    IAccStore.LookupByPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'LookupByPoint', ((1, 'pt'),(1, 'riid'),(1, 'ppunk'),)))
    IAccStore.OnDocumentFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(8, 'OnDocumentFocus', ((1, 'punk'),)))
    IAccStore.GetFocused = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'GetFocused', ((1, 'riid'),(1, 'ppunk'),)))
    return IAccStore
def _define_IAccServerDocMgr_head():
    class IAccServerDocMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('ad7c73cf-6dd5-4855-abc2-b04bad5b9153')
    return IAccServerDocMgr
def _define_IAccServerDocMgr():
    IAccServerDocMgr = win32more.UI.TextServices.IAccServerDocMgr_head
    IAccServerDocMgr.NewDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'NewDocument', ((1, 'riid'),(1, 'punk'),)))
    IAccServerDocMgr.RevokeDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(4, 'RevokeDocument', ((1, 'punk'),)))
    IAccServerDocMgr.OnDocumentFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(5, 'OnDocumentFocus', ((1, 'punk'),)))
    return IAccServerDocMgr
def _define_IAccClientDocMgr_head():
    class IAccClientDocMgr(win32more.System.Com.IUnknown_head):
        Guid = Guid('4c896039-7b6d-49e6-a8c1-45116a98292b')
    return IAccClientDocMgr
def _define_IAccClientDocMgr():
    IAccClientDocMgr = win32more.UI.TextServices.IAccClientDocMgr_head
    IAccClientDocMgr.GetDocuments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumUnknown_head), use_last_error=False)(3, 'GetDocuments', ((1, 'enumUnknown'),)))
    IAccClientDocMgr.LookupByHWND = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(4, 'LookupByHWND', ((1, 'hWnd'),(1, 'riid'),(1, 'ppunk'),)))
    IAccClientDocMgr.LookupByPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(5, 'LookupByPoint', ((1, 'pt'),(1, 'riid'),(1, 'ppunk'),)))
    IAccClientDocMgr.GetFocused = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(6, 'GetFocused', ((1, 'riid'),(1, 'ppunk'),)))
    return IAccClientDocMgr
def _define_IDocWrap_head():
    class IDocWrap(win32more.System.Com.IUnknown_head):
        Guid = Guid('dcd285fe-0be0-43bd-99c9-aaaec513c555')
    return IDocWrap
def _define_IDocWrap():
    IDocWrap = win32more.UI.TextServices.IDocWrap_head
    IDocWrap.SetDoc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'SetDoc', ((1, 'riid'),(1, 'punk'),)))
    IDocWrap.GetWrappedDoc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(4, 'GetWrappedDoc', ((1, 'riid'),(1, 'ppunk'),)))
    return IDocWrap
def _define_IClonableWrapper_head():
    class IClonableWrapper(win32more.System.Com.IUnknown_head):
        Guid = Guid('b33e75ff-e84c-4dca-a25c-33b8dc003374')
    return IClonableWrapper
def _define_IClonableWrapper():
    IClonableWrapper = win32more.UI.TextServices.IClonableWrapper_head
    IClonableWrapper.CloneNewWrapper = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'CloneNewWrapper', ((1, 'riid'),(1, 'ppv'),)))
    return IClonableWrapper
def _define_ITfSpeechUIServer_head():
    class ITfSpeechUIServer(win32more.System.Com.IUnknown_head):
        Guid = Guid('90e9a944-9244-489f-a78f-de67afc013a7')
    return ITfSpeechUIServer
def _define_ITfSpeechUIServer():
    ITfSpeechUIServer = win32more.UI.TextServices.ITfSpeechUIServer_head
    ITfSpeechUIServer.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Initialize', ()))
    ITfSpeechUIServer.ShowUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(4, 'ShowUI', ((1, 'fShow'),)))
    ITfSpeechUIServer.UpdateBalloon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.TfLBBalloonStyle,POINTER(Char),UInt32, use_last_error=False)(5, 'UpdateBalloon', ((1, 'style'),(1, 'pch'),(1, 'cch'),)))
    return ITfSpeechUIServer
def _define_DoMsCtfMonitor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("DoMsCtfMonitor", windll["MsCtfMonitor"]), ((1, 'dwFlags'),(1, 'hEventForServiceStop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitLocalMsCtfMonitor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("InitLocalMsCtfMonitor", windll["MsCtfMonitor"]), ((1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UninitLocalMsCtfMonitor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("UninitLocalMsCtfMonitor", windll["MsCtfMonitor"]), ())
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "GUID_PROP_TEXTOWNER",
    "GUID_PROP_ATTRIBUTE",
    "GUID_PROP_LANGID",
    "GUID_PROP_READING",
    "GUID_PROP_COMPOSING",
    "GUID_PROP_TKB_ALTERNATES",
    "GUID_SYSTEM_FUNCTIONPROVIDER",
    "GUID_APP_FUNCTIONPROVIDER",
    "GUID_TFCAT_CATEGORY_OF_TIP",
    "GUID_TFCAT_TIP_KEYBOARD",
    "GUID_TFCAT_TIP_SPEECH",
    "GUID_TFCAT_TIP_HANDWRITING",
    "GUID_TFCAT_PROP_AUDIODATA",
    "GUID_TFCAT_PROP_INKDATA",
    "GUID_COMPARTMENT_SAPI_AUDIO",
    "GUID_COMPARTMENT_KEYBOARD_DISABLED",
    "GUID_COMPARTMENT_KEYBOARD_OPENCLOSE",
    "GUID_COMPARTMENT_HANDWRITING_OPENCLOSE",
    "GUID_COMPARTMENT_SPEECH_DISABLED",
    "GUID_COMPARTMENT_SPEECH_OPENCLOSE",
    "GUID_COMPARTMENT_SPEECH_GLOBALSTATE",
    "GUID_COMPARTMENT_CONVERSIONMODEBIAS",
    "GUID_PROP_MODEBIAS",
    "GUID_COMPARTMENT_KEYBOARD_INPUTMODE",
    "GUID_MODEBIAS_NONE",
    "GUID_MODEBIAS_URLHISTORY",
    "GUID_MODEBIAS_FILENAME",
    "GUID_MODEBIAS_READING",
    "GUID_MODEBIAS_DATETIME",
    "GUID_MODEBIAS_NAME",
    "GUID_MODEBIAS_CONVERSATION",
    "GUID_MODEBIAS_NUMERIC",
    "GUID_MODEBIAS_HIRAGANA",
    "GUID_MODEBIAS_KATAKANA",
    "GUID_MODEBIAS_HANGUL",
    "GUID_MODEBIAS_CHINESE",
    "GUID_MODEBIAS_HALFWIDTHKATAKANA",
    "GUID_MODEBIAS_FULLWIDTHALPHANUMERIC",
    "GUID_MODEBIAS_FULLWIDTHHANGUL",
    "GUID_TFCAT_PROPSTYLE_STATIC",
    "GUID_TFCAT_DISPLAYATTRIBUTEPROVIDER",
    "GUID_TFCAT_DISPLAYATTRIBUTEPROPERTY",
    "GUID_COMPARTMENT_SPEECH_UI_STATUS",
    "GUID_COMPARTMENT_EMPTYCONTEXT",
    "GUID_COMPARTMENT_TIPUISTATUS",
    "GUID_COMPARTMENT_SPEECH_CFGMENU",
    "GUID_LBI_SAPILAYR_CFGMENUBUTTON",
    "GUID_TFCAT_TIPCAP_SECUREMODE",
    "GUID_TFCAT_TIPCAP_UIELEMENTENABLED",
    "GUID_TFCAT_TIPCAP_INPUTMODECOMPARTMENT",
    "GUID_TFCAT_TIPCAP_COMLESS",
    "GUID_TFCAT_TIPCAP_WOW16",
    "GUID_TFCAT_TIPCAP_IMMERSIVESUPPORT",
    "GUID_TFCAT_TIPCAP_IMMERSIVEONLY",
    "GUID_TFCAT_TIPCAP_LOCALSERVER",
    "GUID_TFCAT_TIPCAP_TSF3",
    "GUID_TFCAT_TIPCAP_DUALMODE",
    "GUID_TFCAT_TIPCAP_SYSTRAYSUPPORT",
    "GUID_COMPARTMENT_KEYBOARD_INPUTMODE_CONVERSION",
    "GUID_COMPARTMENT_KEYBOARD_INPUTMODE_SENTENCE",
    "GUID_COMPARTMENT_TRANSITORYEXTENSION",
    "GUID_COMPARTMENT_TRANSITORYEXTENSION_DOCUMENTMANAGER",
    "GUID_COMPARTMENT_TRANSITORYEXTENSION_PARENT",
    "GUID_COMPARTMENT_ENABLED_PROFILES_UPDATED",
    "GUID_TFCAT_TRANSITORYEXTENSIONUI",
    "GUID_LBI_INPUTMODE",
    "CLSID_TF_ThreadMgr",
    "CLSID_TF_LangBarMgr",
    "CLSID_TF_DisplayAttributeMgr",
    "CLSID_TF_CategoryMgr",
    "CLSID_TF_InputProcessorProfiles",
    "CLSID_TF_LangBarItemMgr",
    "CLSID_TF_ClassicLangBar",
    "CLSID_TF_TransitoryExtensionUIEntry",
    "CLSID_TsfServices",
    "GUID_TS_SERVICE_DATAOBJECT",
    "GUID_TS_SERVICE_ACCESSIBLE",
    "GUID_TS_SERVICE_ACTIVEX",
    "TS_E_INVALIDPOS",
    "TS_E_NOLOCK",
    "TS_E_NOOBJECT",
    "TS_E_NOSERVICE",
    "TS_E_NOINTERFACE",
    "TS_E_NOSELECTION",
    "TS_E_NOLAYOUT",
    "TS_E_INVALIDPOINT",
    "TS_E_SYNCHRONOUS",
    "TS_E_READONLY",
    "TS_E_FORMAT",
    "TS_S_ASYNC",
    "TS_AS_TEXT_CHANGE",
    "TS_AS_SEL_CHANGE",
    "TS_AS_LAYOUT_CHANGE",
    "TS_AS_ATTR_CHANGE",
    "TS_AS_STATUS_CHANGE",
    "TS_LF_SYNC",
    "TS_SD_READONLY",
    "TS_SD_LOADING",
    "TS_SD_RESERVED",
    "TS_SD_TKBAUTOCORRECTENABLE",
    "TS_SD_TKBPREDICTIONENABLE",
    "TS_SD_UIINTEGRATIONENABLE",
    "TS_SD_INPUTPANEMANUALDISPLAYENABLE",
    "TS_SD_EMBEDDEDHANDWRITINGVIEW_ENABLED",
    "TS_SD_EMBEDDEDHANDWRITINGVIEW_VISIBLE",
    "TS_SS_DISJOINTSEL",
    "TS_SS_REGIONS",
    "TS_SS_TRANSITORY",
    "TS_SS_NOHIDDENTEXT",
    "TS_SS_TKBAUTOCORRECTENABLE",
    "TS_SS_TKBPREDICTIONENABLE",
    "TS_SS_UWPCONTROL",
    "TS_IE_CORRECTION",
    "TS_IE_COMPOSITION",
    "TS_IAS_NOQUERY",
    "TS_IAS_QUERYONLY",
    "GXFPF_ROUND_NEAREST",
    "GXFPF_NEAREST",
    "TS_CHAR_EMBEDDED",
    "TS_CHAR_REGION",
    "TS_CHAR_REPLACEMENT",
    "TS_ATTR_FIND_BACKWARDS",
    "TS_ATTR_FIND_WANT_OFFSET",
    "TS_ATTR_FIND_UPDATESTART",
    "TS_ATTR_FIND_WANT_VALUE",
    "TS_ATTR_FIND_WANT_END",
    "TS_ATTR_FIND_HIDDEN",
    "TS_VCOOKIE_NUL",
    "TS_SHIFT_COUNT_HIDDEN",
    "TS_SHIFT_HALT_HIDDEN",
    "TS_SHIFT_HALT_VISIBLE",
    "TS_SHIFT_COUNT_ONLY",
    "TS_GTA_HIDDEN",
    "TS_GEA_HIDDEN",
    "TF_E_LOCKED",
    "TF_E_STACKFULL",
    "TF_E_NOTOWNEDRANGE",
    "TF_E_NOPROVIDER",
    "TF_E_DISCONNECTED",
    "TF_E_INVALIDVIEW",
    "TF_E_ALREADY_EXISTS",
    "TF_E_RANGE_NOT_COVERED",
    "TF_E_COMPOSITION_REJECTED",
    "TF_E_EMPTYCONTEXT",
    "TF_E_INVALIDPOS",
    "TF_E_NOLOCK",
    "TF_E_NOOBJECT",
    "TF_E_NOSERVICE",
    "TF_E_NOINTERFACE",
    "TF_E_NOSELECTION",
    "TF_E_NOLAYOUT",
    "TF_E_INVALIDPOINT",
    "TF_E_SYNCHRONOUS",
    "TF_E_READONLY",
    "TF_E_FORMAT",
    "TF_S_ASYNC",
    "TF_RCM_COMLESS",
    "TF_RCM_VKEY",
    "TF_RCM_HINT_READING_LENGTH",
    "TF_RCM_HINT_COLLISION",
    "TKB_ALTERNATES_STANDARD",
    "TKB_ALTERNATES_FOR_AUTOCORRECTION",
    "TKB_ALTERNATES_FOR_PREDICTION",
    "TKB_ALTERNATES_AUTOCORRECTION_APPLIED",
    "TF_TMAE_NOACTIVATETIP",
    "TF_TMAE_SECUREMODE",
    "TF_TMAE_UIELEMENTENABLEDONLY",
    "TF_TMAE_COMLESS",
    "TF_TMAE_WOW16",
    "TF_TMAE_NOACTIVATEKEYBOARDLAYOUT",
    "TF_TMAE_CONSOLE",
    "TF_TMF_NOACTIVATETIP",
    "TF_TMF_SECUREMODE",
    "TF_TMF_UIELEMENTENABLEDONLY",
    "TF_TMF_COMLESS",
    "TF_TMF_WOW16",
    "TF_TMF_CONSOLE",
    "TF_TMF_IMMERSIVEMODE",
    "TF_TMF_ACTIVATED",
    "TF_MOD_ALT",
    "TF_MOD_CONTROL",
    "TF_MOD_SHIFT",
    "TF_MOD_RALT",
    "TF_MOD_RCONTROL",
    "TF_MOD_RSHIFT",
    "TF_MOD_LALT",
    "TF_MOD_LCONTROL",
    "TF_MOD_LSHIFT",
    "TF_MOD_ON_KEYUP",
    "TF_MOD_IGNORE_ALL_MODIFIER",
    "TF_US_HIDETIPUI",
    "TF_DISABLE_SPEECH",
    "TF_DISABLE_DICTATION",
    "TF_DISABLE_COMMANDING",
    "TF_CLUIE_DOCUMENTMGR",
    "TF_CLUIE_COUNT",
    "TF_CLUIE_SELECTION",
    "TF_CLUIE_STRING",
    "TF_CLUIE_PAGEINDEX",
    "TF_CLUIE_CURRENTPAGE",
    "TF_RIUIE_CONTEXT",
    "TF_RIUIE_STRING",
    "TF_RIUIE_MAXREADINGSTRINGLENGTH",
    "TF_RIUIE_ERRORINDEX",
    "TF_RIUIE_VERTICALORDER",
    "TF_CONVERSIONMODE_ALPHANUMERIC",
    "TF_CONVERSIONMODE_NATIVE",
    "TF_CONVERSIONMODE_KATAKANA",
    "TF_CONVERSIONMODE_FULLSHAPE",
    "TF_CONVERSIONMODE_ROMAN",
    "TF_CONVERSIONMODE_CHARCODE",
    "TF_CONVERSIONMODE_SOFTKEYBOARD",
    "TF_CONVERSIONMODE_NOCONVERSION",
    "TF_CONVERSIONMODE_EUDC",
    "TF_CONVERSIONMODE_SYMBOL",
    "TF_CONVERSIONMODE_FIXED",
    "TF_SENTENCEMODE_NONE",
    "TF_SENTENCEMODE_PLAURALCLAUSE",
    "TF_SENTENCEMODE_SINGLECONVERT",
    "TF_SENTENCEMODE_AUTOMATIC",
    "TF_SENTENCEMODE_PHRASEPREDICT",
    "TF_SENTENCEMODE_CONVERSATION",
    "TF_TRANSITORYEXTENSION_NONE",
    "TF_TRANSITORYEXTENSION_FLOATING",
    "TF_TRANSITORYEXTENSION_ATSELECTION",
    "TF_PROFILETYPE_INPUTPROCESSOR",
    "TF_PROFILETYPE_KEYBOARDLAYOUT",
    "TF_RIP_FLAG_FREEUNUSEDLIBRARIES",
    "TF_IPP_FLAG_ACTIVE",
    "TF_IPP_FLAG_ENABLED",
    "TF_IPP_FLAG_SUBSTITUTEDBYINPUTPROCESSOR",
    "TF_IPP_CAPS_DISABLEONTRANSITORY",
    "TF_IPP_CAPS_SECUREMODESUPPORT",
    "TF_IPP_CAPS_UIELEMENTENABLED",
    "TF_IPP_CAPS_COMLESSSUPPORT",
    "TF_IPP_CAPS_WOW16SUPPORT",
    "TF_IPP_CAPS_IMMERSIVESUPPORT",
    "TF_IPP_CAPS_SYSTRAYSUPPORT",
    "TF_IPPMF_FORPROCESS",
    "TF_IPPMF_FORSESSION",
    "TF_IPPMF_FORSYSTEMALL",
    "TF_IPPMF_ENABLEPROFILE",
    "TF_IPPMF_DISABLEPROFILE",
    "TF_IPPMF_DONTCARECURRENTINPUTLANGUAGE",
    "TF_RP_HIDDENINSETTINGUI",
    "TF_RP_LOCALPROCESS",
    "TF_RP_LOCALTHREAD",
    "TF_RP_SUBITEMINSETTINGUI",
    "TF_URP_ALLPROFILES",
    "TF_URP_LOCALPROCESS",
    "TF_URP_LOCALTHREAD",
    "TF_IPSINK_FLAG_ACTIVE",
    "TF_INVALID_EDIT_COOKIE",
    "TF_POPF_ALL",
    "TF_SD_READONLY",
    "TF_SD_LOADING",
    "TF_SS_DISJOINTSEL",
    "TF_SS_REGIONS",
    "TF_SS_TRANSITORY",
    "TF_SS_TKBAUTOCORRECTENABLE",
    "TF_SS_TKBPREDICTIONENABLE",
    "TF_CHAR_EMBEDDED",
    "TF_HF_OBJECT",
    "TF_TF_MOVESTART",
    "TF_TF_IGNOREEND",
    "TF_ST_CORRECTION",
    "TF_IE_CORRECTION",
    "TF_TU_CORRECTION",
    "TF_INVALID_COOKIE",
    "TF_PROFILE_NEWPHONETIC",
    "TF_PROFILE_PHONETIC",
    "TF_PROFILE_NEWCHANGJIE",
    "TF_PROFILE_CHANGJIE",
    "TF_PROFILE_NEWQUICK",
    "TF_PROFILE_QUICK",
    "TF_PROFILE_CANTONESE",
    "TF_PROFILE_PINYIN",
    "TF_PROFILE_SIMPLEFAST",
    "TF_PROFILE_WUBI",
    "TF_PROFILE_DAYI",
    "TF_PROFILE_ARRAY",
    "TF_PROFILE_YI",
    "TF_PROFILE_TIGRINYA",
    "TF_E_NOCONVERSION",
    "TF_DICTATION_ON",
    "TF_DICTATION_ENABLED",
    "TF_COMMANDING_ENABLED",
    "TF_COMMANDING_ON",
    "TF_SPEECHUI_SHOWN",
    "TF_SHOW_BALLOON",
    "TF_DISABLE_BALLOON",
    "TF_MENUREADY",
    "TF_PROPUI_STATUS_SAVETOFILE",
    "GUID_INTEGRATIONSTYLE_SEARCHBOX",
    "TKBL_UNDEFINED",
    "TKBL_CLASSIC_TRADITIONAL_CHINESE_PHONETIC",
    "TKBL_CLASSIC_TRADITIONAL_CHINESE_CHANGJIE",
    "TKBL_CLASSIC_TRADITIONAL_CHINESE_DAYI",
    "TKBL_OPT_JAPANESE_ABC",
    "TKBL_OPT_KOREAN_HANGUL_2_BULSIK",
    "TKBL_OPT_SIMPLIFIED_CHINESE_PINYIN",
    "TKBL_OPT_TRADITIONAL_CHINESE_PHONETIC",
    "TF_LBI_ICON",
    "TF_LBI_TEXT",
    "TF_LBI_TOOLTIP",
    "TF_LBI_BITMAP",
    "TF_LBI_BALLOON",
    "TF_LBI_CUSTOMUI",
    "TF_LBI_STATUS",
    "TF_LBI_STYLE_HIDDENSTATUSCONTROL",
    "TF_LBI_STYLE_SHOWNINTRAY",
    "TF_LBI_STYLE_HIDEONNOOTHERITEMS",
    "TF_LBI_STYLE_SHOWNINTRAYONLY",
    "TF_LBI_STYLE_HIDDENBYDEFAULT",
    "TF_LBI_STYLE_TEXTCOLORICON",
    "TF_LBI_STYLE_BTN_BUTTON",
    "TF_LBI_STYLE_BTN_MENU",
    "TF_LBI_STYLE_BTN_TOGGLE",
    "TF_LBI_STATUS_HIDDEN",
    "TF_LBI_STATUS_DISABLED",
    "TF_LBI_STATUS_BTN_TOGGLED",
    "TF_LBI_BMPF_VERTICAL",
    "TF_SFT_SHOWNORMAL",
    "TF_SFT_DOCK",
    "TF_SFT_MINIMIZED",
    "TF_SFT_HIDDEN",
    "TF_SFT_NOTRANSPARENCY",
    "TF_SFT_LOWTRANSPARENCY",
    "TF_SFT_HIGHTRANSPARENCY",
    "TF_SFT_LABELS",
    "TF_SFT_NOLABELS",
    "TF_SFT_EXTRAICONSONMINIMIZED",
    "TF_SFT_NOEXTRAICONSONMINIMIZED",
    "TF_SFT_DESKBAND",
    "TF_LBI_DESC_MAXLEN",
    "TF_LBMENUF_CHECKED",
    "TF_LBMENUF_SUBMENU",
    "TF_LBMENUF_SEPARATOR",
    "TF_LBMENUF_RADIOCHECKED",
    "TF_LBMENUF_GRAYED",
    "GUID_PROP_INPUTSCOPE",
    "DCM_FLAGS_TASKENG",
    "DCM_FLAGS_CTFMON",
    "DCM_FLAGS_LOCALTHREADTSF",
    "ILMCM_CHECKLAYOUTANDTIPENABLED",
    "ILMCM_LANGUAGEBAROFF",
    "LIBID_MSAATEXTLib",
    "TS_STRF_START",
    "TS_STRF_MID",
    "TS_STRF_END",
    "TSATTRID_OTHERS",
    "TSATTRID_Font",
    "TSATTRID_Font_FaceName",
    "TSATTRID_Font_SizePts",
    "TSATTRID_Font_Style",
    "TSATTRID_Font_Style_Bold",
    "TSATTRID_Font_Style_Italic",
    "TSATTRID_Font_Style_SmallCaps",
    "TSATTRID_Font_Style_Capitalize",
    "TSATTRID_Font_Style_Uppercase",
    "TSATTRID_Font_Style_Lowercase",
    "TSATTRID_Font_Style_Animation",
    "TSATTRID_Font_Style_Animation_LasVegasLights",
    "TSATTRID_Font_Style_Animation_BlinkingBackground",
    "TSATTRID_Font_Style_Animation_SparkleText",
    "TSATTRID_Font_Style_Animation_MarchingBlackAnts",
    "TSATTRID_Font_Style_Animation_MarchingRedAnts",
    "TSATTRID_Font_Style_Animation_Shimmer",
    "TSATTRID_Font_Style_Animation_WipeDown",
    "TSATTRID_Font_Style_Animation_WipeRight",
    "TSATTRID_Font_Style_Emboss",
    "TSATTRID_Font_Style_Engrave",
    "TSATTRID_Font_Style_Hidden",
    "TSATTRID_Font_Style_Kerning",
    "TSATTRID_Font_Style_Outlined",
    "TSATTRID_Font_Style_Position",
    "TSATTRID_Font_Style_Protected",
    "TSATTRID_Font_Style_Shadow",
    "TSATTRID_Font_Style_Spacing",
    "TSATTRID_Font_Style_Weight",
    "TSATTRID_Font_Style_Height",
    "TSATTRID_Font_Style_Underline",
    "TSATTRID_Font_Style_Underline_Single",
    "TSATTRID_Font_Style_Underline_Double",
    "TSATTRID_Font_Style_Strikethrough",
    "TSATTRID_Font_Style_Strikethrough_Single",
    "TSATTRID_Font_Style_Strikethrough_Double",
    "TSATTRID_Font_Style_Overline",
    "TSATTRID_Font_Style_Overline_Single",
    "TSATTRID_Font_Style_Overline_Double",
    "TSATTRID_Font_Style_Blink",
    "TSATTRID_Font_Style_Subscript",
    "TSATTRID_Font_Style_Superscript",
    "TSATTRID_Font_Style_Color",
    "TSATTRID_Font_Style_BackgroundColor",
    "TSATTRID_Text",
    "TSATTRID_Text_VerticalWriting",
    "TSATTRID_Text_RightToLeft",
    "TSATTRID_Text_Orientation",
    "TSATTRID_Text_Language",
    "TSATTRID_Text_ReadOnly",
    "TSATTRID_Text_EmbeddedObject",
    "TSATTRID_Text_Alignment",
    "TSATTRID_Text_Alignment_Left",
    "TSATTRID_Text_Alignment_Right",
    "TSATTRID_Text_Alignment_Center",
    "TSATTRID_Text_Alignment_Justify",
    "TSATTRID_Text_Link",
    "TSATTRID_Text_Hyphenation",
    "TSATTRID_Text_Para",
    "TSATTRID_Text_Para_FirstLineIndent",
    "TSATTRID_Text_Para_LeftIndent",
    "TSATTRID_Text_Para_RightIndent",
    "TSATTRID_Text_Para_SpaceAfter",
    "TSATTRID_Text_Para_SpaceBefore",
    "TSATTRID_Text_Para_LineSpacing",
    "TSATTRID_Text_Para_LineSpacing_Single",
    "TSATTRID_Text_Para_LineSpacing_OnePtFive",
    "TSATTRID_Text_Para_LineSpacing_Double",
    "TSATTRID_Text_Para_LineSpacing_AtLeast",
    "TSATTRID_Text_Para_LineSpacing_Exactly",
    "TSATTRID_Text_Para_LineSpacing_Multiple",
    "TSATTRID_List",
    "TSATTRID_List_LevelIndel",
    "TSATTRID_List_Type",
    "TSATTRID_List_Type_Bullet",
    "TSATTRID_List_Type_Arabic",
    "TSATTRID_List_Type_LowerLetter",
    "TSATTRID_List_Type_UpperLetter",
    "TSATTRID_List_Type_LowerRoman",
    "TSATTRID_List_Type_UpperRoman",
    "TSATTRID_App",
    "TSATTRID_App_IncorrectSpelling",
    "TSATTRID_App_IncorrectGrammar",
    "LANG_BAR_ITEM_ICON_MODE_FLAGS",
    "TF_DTLBI_NONE",
    "TF_DTLBI_USEPROFILEICON",
    "TEXT_STORE_TEXT_CHANGE_FLAGS",
    "TS_ST_NONE",
    "TS_ST_CORRECTION",
    "TEXT_STORE_CHANGE_FLAGS",
    "TS_TC_NONE",
    "TS_TC_CORRECTION",
    "INSERT_TEXT_AT_SELECTION_FLAGS",
    "TF_IAS_NOQUERY",
    "TF_IAS_QUERYONLY",
    "TF_IAS_NO_DEFAULT_COMPOSITION",
    "ANCHOR_CHANGE_HISTORY_FLAGS",
    "TS_CH_PRECEDING_DEL",
    "TS_CH_FOLLOWING_DEL",
    "TEXT_STORE_LOCK_FLAGS",
    "TS_LF_READ",
    "TS_LF_READWRITE",
    "GET_TEXT_AND_PROPERTY_UPDATES_FLAGS",
    "TF_GTP_NONE",
    "TF_GTP_INCL_TEXT",
    "TF_CONTEXT_EDIT_CONTEXT_FLAGS",
    "TF_ES_ASYNCDONTCARE",
    "TF_ES_SYNC",
    "TF_ES_READ",
    "TF_ES_READWRITE",
    "TF_ES_ASYNC",
    "HKL",
    "TS_STATUS",
    "TS_TEXTCHANGE",
    "TsActiveSelEnd",
    "TS_AE_NONE",
    "TS_AE_START",
    "TS_AE_END",
    "TS_SELECTIONSTYLE",
    "TS_SELECTION_ACP",
    "TS_SELECTION_ANCHOR",
    "TS_ATTRVAL",
    "TsLayoutCode",
    "TS_LC_CREATE",
    "TS_LC_CHANGE",
    "TS_LC_DESTROY",
    "TsRunType",
    "TS_RT_PLAIN",
    "TS_RT_HIDDEN",
    "TS_RT_OPAQUE",
    "TS_RUNINFO",
    "ITextStoreACP",
    "ITextStoreACP2",
    "ITextStoreACPSink",
    "TsGravity",
    "TS_GR_BACKWARD",
    "TS_GR_FORWARD",
    "TsShiftDir",
    "TS_SD_BACKWARD",
    "TS_SD_FORWARD",
    "IAnchor",
    "ITextStoreAnchor",
    "ITextStoreAnchorSink",
    "ITfLangBarMgr",
    "ITfLangBarEventSink",
    "ITfLangBarItemSink",
    "IEnumTfLangBarItems",
    "TF_LANGBARITEMINFO",
    "ITfLangBarItemMgr",
    "ITfLangBarItem",
    "ITfSystemLangBarItemSink",
    "ITfSystemLangBarItem",
    "ITfSystemLangBarItemText",
    "ITfSystemDeviceTypeLangBarItem",
    "TfLBIClick",
    "TF_LBI_CLK_RIGHT",
    "TF_LBI_CLK_LEFT",
    "ITfLangBarItemButton",
    "ITfLangBarItemBitmapButton",
    "ITfLangBarItemBitmap",
    "TfLBBalloonStyle",
    "TF_LB_BALLOON_RECO",
    "TF_LB_BALLOON_SHOW",
    "TF_LB_BALLOON_MISS",
    "TF_LBBALLOONINFO",
    "ITfLangBarItemBalloon",
    "ITfMenu",
    "TF_PERSISTENT_PROPERTY_HEADER_ACP",
    "TF_LANGUAGEPROFILE",
    "TfAnchor",
    "TF_ANCHOR_START",
    "TF_ANCHOR_END",
    "ITfThreadMgr",
    "ITfThreadMgrEx",
    "ITfThreadMgr2",
    "ITfThreadMgrEventSink",
    "ITfConfigureSystemKeystrokeFeed",
    "IEnumTfDocumentMgrs",
    "ITfDocumentMgr",
    "IEnumTfContexts",
    "ITfCompositionView",
    "IEnumITfCompositionView",
    "ITfComposition",
    "ITfCompositionSink",
    "ITfContextComposition",
    "ITfContextOwnerCompositionServices",
    "ITfContextOwnerCompositionSink",
    "ITfContextView",
    "IEnumTfContextViews",
    "TfActiveSelEnd",
    "TF_AE_NONE",
    "TF_AE_START",
    "TF_AE_END",
    "TF_SELECTIONSTYLE",
    "TF_SELECTION",
    "ITfContext",
    "ITfQueryEmbedded",
    "ITfInsertAtSelection",
    "ITfCleanupContextSink",
    "ITfCleanupContextDurationSink",
    "ITfReadOnlyProperty",
    "TF_PROPERTYVAL",
    "IEnumTfPropertyValue",
    "ITfMouseTracker",
    "ITfMouseTrackerACP",
    "ITfMouseSink",
    "ITfEditRecord",
    "ITfTextEditSink",
    "TfLayoutCode",
    "TF_LC_CREATE",
    "TF_LC_CHANGE",
    "TF_LC_DESTROY",
    "ITfTextLayoutSink",
    "ITfStatusSink",
    "ITfEditTransactionSink",
    "ITfContextOwner",
    "ITfContextOwnerServices",
    "ITfContextKeyEventSink",
    "ITfEditSession",
    "TfGravity",
    "TF_GRAVITY_BACKWARD",
    "TF_GRAVITY_FORWARD",
    "TfShiftDir",
    "TF_SD_BACKWARD",
    "TF_SD_FORWARD",
    "TF_HALTCOND",
    "ITfRange",
    "ITfRangeACP",
    "ITextStoreACPServices",
    "ITfRangeBackup",
    "ITfPropertyStore",
    "IEnumTfRanges",
    "ITfCreatePropertyStore",
    "ITfPersistentPropertyLoaderACP",
    "ITfProperty",
    "IEnumTfProperties",
    "ITfCompartment",
    "ITfCompartmentEventSink",
    "ITfCompartmentMgr",
    "ITfFunction",
    "ITfFunctionProvider",
    "IEnumTfFunctionProviders",
    "ITfInputProcessorProfiles",
    "ITfInputProcessorProfilesEx",
    "ITfInputProcessorProfileSubstituteLayout",
    "ITfActiveLanguageProfileNotifySink",
    "IEnumTfLanguageProfiles",
    "ITfLanguageProfileNotifySink",
    "TF_INPUTPROCESSORPROFILE",
    "ITfInputProcessorProfileMgr",
    "IEnumTfInputProcessorProfiles",
    "ITfInputProcessorProfileActivationSink",
    "TF_PRESERVEDKEY",
    "ITfKeystrokeMgr",
    "ITfKeyEventSink",
    "ITfKeyTraceEventSink",
    "ITfPreservedKeyNotifySink",
    "ITfMessagePump",
    "ITfThreadFocusSink",
    "ITfTextInputProcessor",
    "ITfTextInputProcessorEx",
    "ITfClientId",
    "TF_DA_LINESTYLE",
    "TF_LS_NONE",
    "TF_LS_SOLID",
    "TF_LS_DOT",
    "TF_LS_DASH",
    "TF_LS_SQUIGGLE",
    "TF_DA_COLORTYPE",
    "TF_CT_NONE",
    "TF_CT_SYSCOLOR",
    "TF_CT_COLORREF",
    "TF_DA_COLOR",
    "TF_DA_ATTR_INFO",
    "TF_ATTR_INPUT",
    "TF_ATTR_TARGET_CONVERTED",
    "TF_ATTR_CONVERTED",
    "TF_ATTR_TARGET_NOTCONVERTED",
    "TF_ATTR_INPUT_ERROR",
    "TF_ATTR_FIXEDCONVERTED",
    "TF_ATTR_OTHER",
    "TF_DISPLAYATTRIBUTE",
    "ITfDisplayAttributeInfo",
    "IEnumTfDisplayAttributeInfo",
    "ITfDisplayAttributeProvider",
    "ITfDisplayAttributeMgr",
    "ITfDisplayAttributeNotifySink",
    "ITfCategoryMgr",
    "ITfSource",
    "ITfSourceSingle",
    "ITfUIElementMgr",
    "IEnumTfUIElements",
    "ITfUIElementSink",
    "ITfUIElement",
    "ITfCandidateListUIElement",
    "ITfCandidateListUIElementBehavior",
    "ITfReadingInformationUIElement",
    "ITfTransitoryExtensionUIElement",
    "ITfTransitoryExtensionSink",
    "ITfToolTipUIElement",
    "ITfReverseConversionList",
    "ITfReverseConversion",
    "ITfReverseConversionMgr",
    "ITfCandidateString",
    "IEnumTfCandidates",
    "TfCandidateResult",
    "CAND_FINALIZED",
    "CAND_SELECTED",
    "CAND_CANCELED",
    "ITfCandidateList",
    "ITfFnReconversion",
    "ITfFnPlayBack",
    "ITfFnLangProfileUtil",
    "ITfFnConfigure",
    "ITfFnConfigureRegisterWord",
    "ITfFnConfigureRegisterEudc",
    "ITfFnShowHelp",
    "ITfFnBalloon",
    "TfSapiObject",
    "GETIF_RESMGR",
    "GETIF_RECOCONTEXT",
    "GETIF_RECOGNIZER",
    "GETIF_VOICE",
    "GETIF_DICTGRAM",
    "GETIF_RECOGNIZERNOINIT",
    "ITfFnGetSAPIObject",
    "ITfFnPropertyUIStatus",
    "IEnumSpeechCommands",
    "ISpeechCommandProvider",
    "ITfFnCustomSpeechCommand",
    "ITfFnLMProcessor",
    "ITfFnLMInternal",
    "TF_LMLATTELEMENT",
    "IEnumTfLatticeElements",
    "ITfLMLattice",
    "ITfFnAdviseText",
    "ITfFnSearchCandidateProvider",
    "TfIntegratableCandidateListSelectionStyle",
    "STYLE_ACTIVE_SELECTION",
    "STYLE_IMPLIED_SELECTION",
    "ITfIntegratableCandidateListUIElement",
    "TKBLayoutType",
    "TKBLT_UNDEFINED",
    "TKBLT_CLASSIC",
    "TKBLT_OPTIMIZED",
    "ITfFnGetPreferredTouchKeyboardLayout",
    "ITfFnGetLinguisticAlternates",
    "IUIManagerEventSink",
    "InputScope",
    "IS_DEFAULT",
    "IS_URL",
    "IS_FILE_FULLFILEPATH",
    "IS_FILE_FILENAME",
    "IS_EMAIL_USERNAME",
    "IS_EMAIL_SMTPEMAILADDRESS",
    "IS_LOGINNAME",
    "IS_PERSONALNAME_FULLNAME",
    "IS_PERSONALNAME_PREFIX",
    "IS_PERSONALNAME_GIVENNAME",
    "IS_PERSONALNAME_MIDDLENAME",
    "IS_PERSONALNAME_SURNAME",
    "IS_PERSONALNAME_SUFFIX",
    "IS_ADDRESS_FULLPOSTALADDRESS",
    "IS_ADDRESS_POSTALCODE",
    "IS_ADDRESS_STREET",
    "IS_ADDRESS_STATEORPROVINCE",
    "IS_ADDRESS_CITY",
    "IS_ADDRESS_COUNTRYNAME",
    "IS_ADDRESS_COUNTRYSHORTNAME",
    "IS_CURRENCY_AMOUNTANDSYMBOL",
    "IS_CURRENCY_AMOUNT",
    "IS_DATE_FULLDATE",
    "IS_DATE_MONTH",
    "IS_DATE_DAY",
    "IS_DATE_YEAR",
    "IS_DATE_MONTHNAME",
    "IS_DATE_DAYNAME",
    "IS_DIGITS",
    "IS_NUMBER",
    "IS_ONECHAR",
    "IS_PASSWORD",
    "IS_TELEPHONE_FULLTELEPHONENUMBER",
    "IS_TELEPHONE_COUNTRYCODE",
    "IS_TELEPHONE_AREACODE",
    "IS_TELEPHONE_LOCALNUMBER",
    "IS_TIME_FULLTIME",
    "IS_TIME_HOUR",
    "IS_TIME_MINORSEC",
    "IS_NUMBER_FULLWIDTH",
    "IS_ALPHANUMERIC_HALFWIDTH",
    "IS_ALPHANUMERIC_FULLWIDTH",
    "IS_CURRENCY_CHINESE",
    "IS_BOPOMOFO",
    "IS_HIRAGANA",
    "IS_KATAKANA_HALFWIDTH",
    "IS_KATAKANA_FULLWIDTH",
    "IS_HANJA",
    "IS_HANGUL_HALFWIDTH",
    "IS_HANGUL_FULLWIDTH",
    "IS_SEARCH",
    "IS_FORMULA",
    "IS_SEARCH_INCREMENTAL",
    "IS_CHINESE_HALFWIDTH",
    "IS_CHINESE_FULLWIDTH",
    "IS_NATIVE_SCRIPT",
    "IS_YOMI",
    "IS_TEXT",
    "IS_CHAT",
    "IS_NAME_OR_PHONENUMBER",
    "IS_EMAILNAME_OR_ADDRESS",
    "IS_PRIVATE",
    "IS_MAPS",
    "IS_NUMERIC_PASSWORD",
    "IS_NUMERIC_PIN",
    "IS_ALPHANUMERIC_PIN",
    "IS_ALPHANUMERIC_PIN_SET",
    "IS_FORMULA_NUMBER",
    "IS_CHAT_WITHOUT_EMOJI",
    "IS_PHRASELIST",
    "IS_REGULAREXPRESSION",
    "IS_SRGS",
    "IS_XML",
    "IS_ENUMSTRING",
    "ITfInputScope",
    "ITfInputScope2",
    "MSAAControl",
    "AccStore",
    "AccDictionary",
    "AccServerDocMgr",
    "AccClientDocMgr",
    "DocWrap",
    "ITfMSAAControl",
    "IInternalDocWrap",
    "ITextStoreACPEx",
    "ITextStoreAnchorEx",
    "ITextStoreACPSinkEx",
    "ITextStoreSinkAnchorEx",
    "IAccDictionary",
    "IVersionInfo",
    "ICoCreateLocally",
    "ICoCreatedLocally",
    "IAccStore",
    "IAccServerDocMgr",
    "IAccClientDocMgr",
    "IDocWrap",
    "IClonableWrapper",
    "ITfSpeechUIServer",
    "DoMsCtfMonitor",
    "InitLocalMsCtfMonitor",
    "UninitLocalMsCtfMonitor",
]
