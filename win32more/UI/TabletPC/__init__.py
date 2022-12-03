from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.System.Ole
import win32more.UI.Controls
import win32more.UI.TabletPC
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
def _define__IInkCollectorEvents_head():
    class _IInkCollectorEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('11a583f2-712d-4fea-ab-cf-ab-4a-f3-8e-a0-6b')
    return _IInkCollectorEvents
def _define__IInkCollectorEvents():
    _IInkCollectorEvents = win32more.UI.TabletPC._IInkCollectorEvents_head
    win32more.System.Com.IDispatch
    return _IInkCollectorEvents
def _define__IInkEditEvents_head():
    class _IInkEditEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('e3b0b797-a72e-46db-a0-d7-6c-9e-ba-8e-9b-bc')
    return _IInkEditEvents
def _define__IInkEditEvents():
    _IInkEditEvents = win32more.UI.TabletPC._IInkEditEvents_head
    win32more.System.Com.IDispatch
    return _IInkEditEvents
def _define__IInkEvents_head():
    class _IInkEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('427b1865-ca3f-479a-83-a9-0f-42-0f-2a-00-73')
    return _IInkEvents
def _define__IInkEvents():
    _IInkEvents = win32more.UI.TabletPC._IInkEvents_head
    win32more.System.Com.IDispatch
    return _IInkEvents
def _define__IInkOverlayEvents_head():
    class _IInkOverlayEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('31179b69-e563-489e-b1-6f-71-2f-1e-8a-06-51')
    return _IInkOverlayEvents
def _define__IInkOverlayEvents():
    _IInkOverlayEvents = win32more.UI.TabletPC._IInkOverlayEvents_head
    win32more.System.Com.IDispatch
    return _IInkOverlayEvents
def _define__IInkPictureEvents_head():
    class _IInkPictureEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('60ff4fee-22ff-4484-ac-c1-d3-08-d9-cd-7e-a3')
    return _IInkPictureEvents
def _define__IInkPictureEvents():
    _IInkPictureEvents = win32more.UI.TabletPC._IInkPictureEvents_head
    win32more.System.Com.IDispatch
    return _IInkPictureEvents
def _define__IInkRecognitionEvents_head():
    class _IInkRecognitionEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('17bce92f-2e21-47fd-9d-33-3c-6a-fb-fd-8c-59')
    return _IInkRecognitionEvents
def _define__IInkRecognitionEvents():
    _IInkRecognitionEvents = win32more.UI.TabletPC._IInkRecognitionEvents_head
    win32more.System.Com.IDispatch
    return _IInkRecognitionEvents
def _define__IInkStrokesEvents_head():
    class _IInkStrokesEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('f33053ec-5d25-430a-92-8f-76-a6-49-1d-de-15')
    return _IInkStrokesEvents
def _define__IInkStrokesEvents():
    _IInkStrokesEvents = win32more.UI.TabletPC._IInkStrokesEvents_head
    win32more.System.Com.IDispatch
    return _IInkStrokesEvents
def _define__IMathInputControlEvents_head():
    class _IMathInputControlEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('683336b5-a47d-4358-96-f9-87-5a-47-2a-e7-0a')
    return _IMathInputControlEvents
def _define__IMathInputControlEvents():
    _IMathInputControlEvents = win32more.UI.TabletPC._IMathInputControlEvents_head
    win32more.System.Com.IDispatch
    return _IMathInputControlEvents
def _define__IPenInputPanelEvents_head():
    class _IPenInputPanelEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('b7e489da-3719-439f-84-8f-e7-ac-bd-82-0f-17')
    return _IPenInputPanelEvents
def _define__IPenInputPanelEvents():
    _IPenInputPanelEvents = win32more.UI.TabletPC._IPenInputPanelEvents_head
    win32more.System.Com.IDispatch
    return _IPenInputPanelEvents
ALT_BREAKS = Int32
ALT_BREAKS_SAME = 0
ALT_BREAKS_UNIQUE = 1
ALT_BREAKS_FULL = 2
MICROSOFT_URL_EXPERIENCE_PROPERTY = 'Microsoft TIP URL Experience'
MICROSOFT_TIP_NO_INSERT_BUTTON_PROPERTY = 'Microsoft TIP No Insert Option'
MICROSOFT_TIP_COMBOBOXLIST_PROPERTY = 'Microsoft TIP ComboBox List Window Identifier'
MICROSOFT_TIP_OPENING_MSG = 'TabletInputPanelOpening'
SAFE_PARTIAL = 1
BEST_COMPLETE = 2
MAX_VENDORNAME = 32
MAX_FRIENDLYNAME = 64
MAX_LANGUAGES = 64
CAC_FULL = 0
CAC_PREFIX = 1
CAC_RANDOM = 2
ASYNC_RECO_INTERRUPTED = 1
ASYNC_RECO_PROCESS_FAILED = 2
ASYNC_RECO_ADDSTROKE_FAILED = 4
ASYNC_RECO_SETCACMODE_FAILED = 8
ASYNC_RECO_RESETCONTEXT_FAILED = 16
ASYNC_RECO_SETGUIDE_FAILED = 32
ASYNC_RECO_SETFLAGS_FAILED = 64
ASYNC_RECO_SETFACTOID_FAILED = 128
ASYNC_RECO_SETTEXTCONTEXT_FAILED = 256
ASYNC_RECO_SETWORDLIST_FAILED = 512
RF_DONTCARE = 1
RF_OBJECT = 2
RF_FREE_INPUT = 4
RF_LINED_INPUT = 8
RF_BOXED_INPUT = 16
RF_CAC_INPUT = 32
RF_RIGHT_AND_DOWN = 64
RF_LEFT_AND_DOWN = 128
RF_DOWN_AND_LEFT = 256
RF_DOWN_AND_RIGHT = 512
RF_ARBITRARY_ANGLE = 1024
RF_LATTICE = 2048
RF_ADVISEINKCHANGE = 4096
RF_STROKEREORDER = 8192
RF_PERSONALIZABLE = 16384
RF_PERFORMSLINEBREAKING = 65536
RF_REQUIRESSEGMENTATIONBREAKING = 131072
FLICK_WM_HANDLED_MASK = 1
NUM_FLICK_DIRECTIONS = 8
WM_TABLET_DEFBASE = 704
WM_TABLET_MAXOFFSET = 32
WM_TABLET_ADDED = 712
WM_TABLET_DELETED = 713
WM_TABLET_FLICK = 715
WM_TABLET_QUERYSYSTEMGESTURESTATUS = 716
TABLET_DISABLE_PRESSANDHOLD = 1
TABLET_DISABLE_PENTAPFEEDBACK = 8
TABLET_DISABLE_PENBARRELFEEDBACK = 16
TABLET_DISABLE_TOUCHUIFORCEON = 256
TABLET_DISABLE_TOUCHUIFORCEOFF = 512
TABLET_DISABLE_TOUCHSWITCH = 32768
TABLET_DISABLE_FLICKS = 65536
TABLET_ENABLE_FLICKSONCONTEXT = 131072
TABLET_ENABLE_FLICKLEARNINGMODE = 262144
TABLET_DISABLE_SMOOTHSCROLLING = 524288
TABLET_DISABLE_FLICKFALLBACKKEYS = 1048576
TABLET_ENABLE_MULTITOUCHDATA = 16777216
MAX_PACKET_PROPERTY_COUNT = 32
MAX_PACKET_BUTTON_COUNT = 32
IP_CURSOR_DOWN = 1
IP_INVERTED = 2
IP_MARGIN = 4
INK_SERIALIZED_FORMAT = 'Ink Serialized Format'
STR_GUID_X = '{598A6A8F-52C0-4BA0-93AF-AF357411A561}'
STR_GUID_Y = '{B53F9F75-04E0-4498-A7EE-C30DBB5A9011}'
STR_GUID_Z = '{735ADB30-0EBB-4788-A0E4-0F316490055D}'
STR_GUID_PAKETSTATUS = '{6E0E07BF-AFE7-4CF7-87D1-AF6446208418}'
STR_GUID_TIMERTICK = '{436510C5-FED3-45D1-8B76-71D3EA7A829D}'
STR_GUID_SERIALNUMBER = '{78A81B56-0935-4493-BAAE-00541A8A16C4}'
STR_GUID_NORMALPRESSURE = '{7307502D-F9F4-4E18-B3F2-2CE1B1A3610C}'
STR_GUID_TANGENTPRESSURE = '{6DA4488B-5244-41EC-905B-32D89AB80809}'
STR_GUID_BUTTONPRESSURE = '{8B7FEFC4-96AA-4BFE-AC26-8A5F0BE07BF5}'
STR_GUID_XTILTORIENTATION = '{A8D07B3A-8BF0-40B0-95A9-B80A6BB787BF}'
STR_GUID_YTILTORIENTATION = '{0E932389-1D77-43AF-AC00-5B950D6D4B2D}'
STR_GUID_AZIMUTHORIENTATION = '{029123B4-8828-410B-B250-A0536595E5DC}'
STR_GUID_ALTITUDEORIENTATION = '{82DEC5C7-F6BA-4906-894F-66D68DFC456C}'
STR_GUID_TWISTORIENTATION = '{0D324960-13B2-41E4-ACE6-7AE9D43D2D3B}'
STR_GUID_PITCHROTATION = '{7F7E57B7-BE37-4BE1-A356-7A84160E1893}'
STR_GUID_ROLLROTATION = '{5D5D5E56-6BA9-4C5B-9FB0-851C91714E56}'
STR_GUID_YAWROTATION = '{6A849980-7C3A-45B7-AA82-90A262950E89}'
STR_GUID_WIDTH = '{BAABE94D-2712-48F5-BE9D-8F8B5EA0711A}'
STR_GUID_HEIGHT = '{E61858D2-E447-4218-9D3F-18865C203DF4}'
STR_GUID_FINGERCONTACTCONFIDENCE = '{E706C804-57F0-4F00-8A0C-853D57789BE9}'
STR_GUID_DEVICE_CONTACT_ID = '{02585B91-049B-4750-9615-DF8948AB3C9C}'
INKRECOGNITIONPROPERTY_LINENUMBER = '{DBF29F2C-5289-4BE8-B3D8-6EF63246253E}'
INKRECOGNITIONPROPERTY_BOXNUMBER = '{2C243E3A-F733-4EB6-B1F8-B5DC5C2C4CDA}'
INKRECOGNITIONPROPERTY_SEGMENTATION = '{B3C0FE6C-FB51-4164-BA2F-844AF8F983DA}'
INKRECOGNITIONPROPERTY_HOTPOINT = '{CA6F40DC-5292-452a-91FB-2181C0BEC0DE}'
INKRECOGNITIONPROPERTY_MAXIMUMSTROKECOUNT = '{BF0EEC4E-4B7D-47a9-8CFA-234DD24BD22A}'
INKRECOGNITIONPROPERTY_POINTSPERINCH = '{7ED16B76-889C-468e-8276-0021B770187E}'
INKRECOGNITIONPROPERTY_CONFIDENCELEVEL = '{7DFE11A7-FB5D-4958-8765-154ADF0D833F}'
INKRECOGNITIONPROPERTY_LINEMETRICS = '{8CC24B27-30A9-4b96-9056-2D3A90DA0727}'
FACTOID_NONE = 'NONE'
FACTOID_DEFAULT = 'DEFAULT'
FACTOID_SYSTEMDICTIONARY = 'SYSDICT'
FACTOID_WORDLIST = 'WORDLIST'
FACTOID_EMAIL = 'EMAIL'
FACTOID_WEB = 'WEB'
FACTOID_ONECHAR = 'ONECHAR'
FACTOID_NUMBER = 'NUMBER'
FACTOID_DIGIT = 'DIGIT'
FACTOID_NUMBERSIMPLE = 'NUMSIMPLE'
FACTOID_CURRENCY = 'CURRENCY'
FACTOID_POSTALCODE = 'POSTALCODE'
FACTOID_PERCENT = 'PERCENT'
FACTOID_DATE = 'DATE'
FACTOID_TIME = 'TIME'
FACTOID_TELEPHONE = 'TELEPHONE'
FACTOID_FILENAME = 'FILENAME'
FACTOID_UPPERCHAR = 'UPPERCHAR'
FACTOID_LOWERCHAR = 'LOWERCHAR'
FACTOID_PUNCCHAR = 'PUNCCHAR'
FACTOID_JAPANESECOMMON = 'JPN_COMMON'
FACTOID_CHINESESIMPLECOMMON = 'CHS_COMMON'
FACTOID_CHINESETRADITIONALCOMMON = 'CHT_COMMON'
FACTOID_KOREANCOMMON = 'KOR_COMMON'
FACTOID_HIRAGANA = 'HIRAGANA'
FACTOID_KATAKANA = 'KATAKANA'
FACTOID_KANJICOMMON = 'KANJI_COMMON'
FACTOID_KANJIRARE = 'KANJI_RARE'
FACTOID_BOPOMOFO = 'BOPOMOFO'
FACTOID_JAMO = 'JAMO'
FACTOID_HANGULCOMMON = 'HANGUL_COMMON'
FACTOID_HANGULRARE = 'HANGUL_RARE'
MICROSOFT_PENINPUT_PANEL_PROPERTY_T = 'Microsoft PenInputPanel 1.5'
INKEDIT_CLASSW = 'INKEDIT'
INKEDIT_CLASS = 'INKEDIT'
IEC__BASE = 1536
EM_GETINKMODE = 1537
EM_SETINKMODE = 1538
EM_GETINKINSERTMODE = 1539
EM_SETINKINSERTMODE = 1540
EM_GETDRAWATTR = 1541
EM_SETDRAWATTR = 1542
EM_GETRECOTIMEOUT = 1543
EM_SETRECOTIMEOUT = 1544
EM_GETGESTURESTATUS = 1545
EM_SETGESTURESTATUS = 1546
EM_GETRECOGNIZER = 1547
EM_SETRECOGNIZER = 1548
EM_GETFACTOID = 1549
EM_SETFACTOID = 1550
EM_GETSELINK = 1551
EM_SETSELINK = 1552
EM_GETMOUSEICON = 1553
EM_SETMOUSEICON = 1554
EM_GETMOUSEPOINTER = 1555
EM_SETMOUSEPOINTER = 1556
EM_GETSTATUS = 1557
EM_RECOGNIZE = 1558
EM_GETUSEMOUSEFORINPUT = 1559
EM_SETUSEMOUSEFORINPUT = 1560
EM_SETSELINKDISPLAYMODE = 1561
EM_GETSELINKDISPLAYMODE = 1562
IECN__BASE = 2048
IECN_STROKE = 2049
IECN_GESTURE = 2050
IECN_RECOGNITIONRESULT = 2051
RECOFLAG_WORDMODE = 1
RECOFLAG_COERCE = 2
RECOFLAG_SINGLESEG = 4
RECOFLAG_PREFIXOK = 8
RECOFLAG_LINEMODE = 16
RECOFLAG_DISABLEPERSONALIZATION = 32
RECOFLAG_AUTOSPACE = 64
RECOCONF_LOWCONFIDENCE = -1
RECOCONF_MEDIUMCONFIDENCE = 0
RECOCONF_HIGHCONFIDENCE = 1
RECOCONF_NOTSET = 128
GESTURE_NULL = 61440
GESTURE_SCRATCHOUT = 61441
GESTURE_TRIANGLE = 61442
GESTURE_SQUARE = 61443
GESTURE_STAR = 61444
GESTURE_CHECK = 61445
GESTURE_INFINITY = 61446
GESTURE_CROSS = 61447
GESTURE_PARAGRAPH = 61448
GESTURE_SECTION = 61449
GESTURE_BULLET = 61450
GESTURE_BULLET_CROSS = 61451
GESTURE_SQUIGGLE = 61452
GESTURE_SWAP = 61453
GESTURE_OPENUP = 61454
GESTURE_CLOSEUP = 61455
GESTURE_CURLICUE = 61456
GESTURE_DOUBLE_CURLICUE = 61457
GESTURE_RECTANGLE = 61458
GESTURE_CIRCLE = 61472
GESTURE_DOUBLE_CIRCLE = 61473
GESTURE_CIRCLE_TAP = 61474
GESTURE_CIRCLE_CIRCLE = 61475
GESTURE_CIRCLE_CROSS = 61477
GESTURE_CIRCLE_LINE_VERT = 61478
GESTURE_CIRCLE_LINE_HORZ = 61479
GESTURE_SEMICIRCLE_LEFT = 61480
GESTURE_SEMICIRCLE_RIGHT = 61481
GESTURE_CHEVRON_UP = 61488
GESTURE_CHEVRON_DOWN = 61489
GESTURE_CHEVRON_LEFT = 61490
GESTURE_CHEVRON_RIGHT = 61491
GESTURE_ARROW_UP = 61496
GESTURE_ARROW_DOWN = 61497
GESTURE_ARROW_LEFT = 61498
GESTURE_ARROW_RIGHT = 61499
GESTURE_DOUBLE_ARROW_UP = 61500
GESTURE_DOUBLE_ARROW_DOWN = 61501
GESTURE_DOUBLE_ARROW_LEFT = 61502
GESTURE_DOUBLE_ARROW_RIGHT = 61503
GESTURE_UP_ARROW_LEFT = 61504
GESTURE_UP_ARROW_RIGHT = 61505
GESTURE_DOWN_ARROW_LEFT = 61506
GESTURE_DOWN_ARROW_RIGHT = 61507
GESTURE_LEFT_ARROW_UP = 61508
GESTURE_LEFT_ARROW_DOWN = 61509
GESTURE_RIGHT_ARROW_UP = 61510
GESTURE_RIGHT_ARROW_DOWN = 61511
GESTURE_UP = 61528
GESTURE_DOWN = 61529
GESTURE_LEFT = 61530
GESTURE_RIGHT = 61531
GESTURE_DIAGONAL_LEFTUP = 61532
GESTURE_DIAGONAL_RIGHTUP = 61533
GESTURE_DIAGONAL_LEFTDOWN = 61534
GESTURE_DIAGONAL_RIGHTDOWN = 61535
GESTURE_UP_DOWN = 61536
GESTURE_DOWN_UP = 61537
GESTURE_LEFT_RIGHT = 61538
GESTURE_RIGHT_LEFT = 61539
GESTURE_UP_LEFT_LONG = 61540
GESTURE_UP_RIGHT_LONG = 61541
GESTURE_DOWN_LEFT_LONG = 61542
GESTURE_DOWN_RIGHT_LONG = 61543
GESTURE_UP_LEFT = 61544
GESTURE_UP_RIGHT = 61545
GESTURE_DOWN_LEFT = 61546
GESTURE_DOWN_RIGHT = 61547
GESTURE_LEFT_UP = 61548
GESTURE_LEFT_DOWN = 61549
GESTURE_RIGHT_UP = 61550
GESTURE_RIGHT_DOWN = 61551
GESTURE_LETTER_A = 61568
GESTURE_LETTER_B = 61569
GESTURE_LETTER_C = 61570
GESTURE_LETTER_D = 61571
GESTURE_LETTER_E = 61572
GESTURE_LETTER_F = 61573
GESTURE_LETTER_G = 61574
GESTURE_LETTER_H = 61575
GESTURE_LETTER_I = 61576
GESTURE_LETTER_J = 61577
GESTURE_LETTER_K = 61578
GESTURE_LETTER_L = 61579
GESTURE_LETTER_M = 61580
GESTURE_LETTER_N = 61581
GESTURE_LETTER_O = 61582
GESTURE_LETTER_P = 61583
GESTURE_LETTER_Q = 61584
GESTURE_LETTER_R = 61585
GESTURE_LETTER_S = 61586
GESTURE_LETTER_T = 61587
GESTURE_LETTER_U = 61588
GESTURE_LETTER_V = 61589
GESTURE_LETTER_W = 61590
GESTURE_LETTER_X = 61591
GESTURE_LETTER_Y = 61592
GESTURE_LETTER_Z = 61593
GESTURE_DIGIT_0 = 61594
GESTURE_DIGIT_1 = 61595
GESTURE_DIGIT_2 = 61596
GESTURE_DIGIT_3 = 61597
GESTURE_DIGIT_4 = 61598
GESTURE_DIGIT_5 = 61599
GESTURE_DIGIT_6 = 61600
GESTURE_DIGIT_7 = 61601
GESTURE_DIGIT_8 = 61602
GESTURE_DIGIT_9 = 61603
GESTURE_EXCLAMATION = 61604
GESTURE_QUESTION = 61605
GESTURE_SHARP = 61606
GESTURE_DOLLAR = 61607
GESTURE_ASTERISK = 61608
GESTURE_PLUS = 61609
GESTURE_DOUBLE_UP = 61624
GESTURE_DOUBLE_DOWN = 61625
GESTURE_DOUBLE_LEFT = 61626
GESTURE_DOUBLE_RIGHT = 61627
GESTURE_TRIPLE_UP = 61628
GESTURE_TRIPLE_DOWN = 61629
GESTURE_TRIPLE_LEFT = 61630
GESTURE_TRIPLE_RIGHT = 61631
GESTURE_BRACKET_OVER = 61668
GESTURE_BRACKET_UNDER = 61669
GESTURE_BRACKET_LEFT = 61670
GESTURE_BRACKET_RIGHT = 61671
GESTURE_BRACE_OVER = 61672
GESTURE_BRACE_UNDER = 61673
GESTURE_BRACE_LEFT = 61674
GESTURE_BRACE_RIGHT = 61675
GESTURE_TAP = 61680
GESTURE_DOUBLE_TAP = 61681
GESTURE_TRIPLE_TAP = 61682
GESTURE_QUAD_TAP = 61683
FACILITY_INK = 40
def _define_GUID_PACKETPROPERTY_GUID_X():
    return Guid('598a6a8f-52c0-4ba0-93-af-af-35-74-11-a5-61')
def _define_GUID_PACKETPROPERTY_GUID_Y():
    return Guid('b53f9f75-04e0-4498-a7-ee-c3-0d-bb-5a-90-11')
def _define_GUID_PACKETPROPERTY_GUID_Z():
    return Guid('735adb30-0ebb-4788-a0-e4-0f-31-64-90-05-5d')
def _define_GUID_PACKETPROPERTY_GUID_PACKET_STATUS():
    return Guid('6e0e07bf-afe7-4cf7-87-d1-af-64-46-20-84-18')
def _define_GUID_PACKETPROPERTY_GUID_TIMER_TICK():
    return Guid('436510c5-fed3-45d1-8b-76-71-d3-ea-7a-82-9d')
def _define_GUID_PACKETPROPERTY_GUID_SERIAL_NUMBER():
    return Guid('78a81b56-0935-4493-ba-ae-00-54-1a-8a-16-c4')
def _define_GUID_PACKETPROPERTY_GUID_NORMAL_PRESSURE():
    return Guid('7307502d-f9f4-4e18-b3-f2-2c-e1-b1-a3-61-0c')
def _define_GUID_PACKETPROPERTY_GUID_TANGENT_PRESSURE():
    return Guid('6da4488b-5244-41ec-90-5b-32-d8-9a-b8-08-09')
def _define_GUID_PACKETPROPERTY_GUID_BUTTON_PRESSURE():
    return Guid('8b7fefc4-96aa-4bfe-ac-26-8a-5f-0b-e0-7b-f5')
def _define_GUID_PACKETPROPERTY_GUID_X_TILT_ORIENTATION():
    return Guid('a8d07b3a-8bf0-40b0-95-a9-b8-0a-6b-b7-87-bf')
def _define_GUID_PACKETPROPERTY_GUID_Y_TILT_ORIENTATION():
    return Guid('0e932389-1d77-43af-ac-00-5b-95-0d-6d-4b-2d')
def _define_GUID_PACKETPROPERTY_GUID_AZIMUTH_ORIENTATION():
    return Guid('029123b4-8828-410b-b2-50-a0-53-65-95-e5-dc')
def _define_GUID_PACKETPROPERTY_GUID_ALTITUDE_ORIENTATION():
    return Guid('82dec5c7-f6ba-4906-89-4f-66-d6-8d-fc-45-6c')
def _define_GUID_PACKETPROPERTY_GUID_TWIST_ORIENTATION():
    return Guid('0d324960-13b2-41e4-ac-e6-7a-e9-d4-3d-2d-3b')
def _define_GUID_PACKETPROPERTY_GUID_PITCH_ROTATION():
    return Guid('7f7e57b7-be37-4be1-a3-56-7a-84-16-0e-18-93')
def _define_GUID_PACKETPROPERTY_GUID_ROLL_ROTATION():
    return Guid('5d5d5e56-6ba9-4c5b-9f-b0-85-1c-91-71-4e-56')
def _define_GUID_PACKETPROPERTY_GUID_YAW_ROTATION():
    return Guid('6a849980-7c3a-45b7-aa-82-90-a2-62-95-0e-89')
def _define_GUID_PACKETPROPERTY_GUID_WIDTH():
    return Guid('baabe94d-2712-48f5-be-9d-8f-8b-5e-a0-71-1a')
def _define_GUID_PACKETPROPERTY_GUID_HEIGHT():
    return Guid('e61858d2-e447-4218-9d-3f-18-86-5c-20-3d-f4')
def _define_GUID_PACKETPROPERTY_GUID_FINGERCONTACTCONFIDENCE():
    return Guid('e706c804-57f0-4f00-8a-0c-85-3d-57-78-9b-e9')
def _define_GUID_PACKETPROPERTY_GUID_DEVICE_CONTACT_ID():
    return Guid('02585b91-049b-4750-96-15-df-89-48-ab-3c-9c')
InkMinTransparencyValue = 0
InkMaxTransparencyValue = 255
InkCollectorClipInkToMargin = 0
InkCollectorDefaultMargin = -2147483648
def _define_GUID_GESTURE_DATA():
    return Guid('41e4ec0f-26aa-455a-9a-a5-2c-d3-6c-f6-3f-b9')
def _define_GUID_DYNAMIC_RENDERER_CACHED_DATA():
    return Guid('bf531b92-25bf-4a95-89-ad-0e-47-6b-34-b4-f5')
def _define_CreateRecognizer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.TabletPC.HRECOGNIZER))(('CreateRecognizer', windll['inkobjcore.dll']), ((1, 'pCLSID'),(1, 'phrec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DestroyRecognizer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOGNIZER)(('DestroyRecognizer', windll['inkobjcore.dll']), ((1, 'hrec'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRecoAttributes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOGNIZER,POINTER(win32more.UI.TabletPC.RECO_ATTRS_head))(('GetRecoAttributes', windll['inkobjcore.dll']), ((1, 'hrec'),(1, 'pRecoAttrs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOGNIZER,POINTER(win32more.UI.TabletPC.HRECOCONTEXT))(('CreateContext', windll['inkobjcore.dll']), ((1, 'hrec'),(1, 'phrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DestroyContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT)(('DestroyContext', windll['inkobjcore.dll']), ((1, 'hrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetResultPropertyList():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOGNIZER,POINTER(UInt32),POINTER(Guid))(('GetResultPropertyList', windll['inkobjcore.dll']), ((1, 'hrec'),(1, 'pPropertyCount'),(1, 'pPropertyGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUnicodeRanges():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOGNIZER,POINTER(UInt32),POINTER(win32more.UI.TabletPC.CHARACTER_RANGE_head))(('GetUnicodeRanges', windll['inkobjcore.dll']), ((1, 'hrec'),(1, 'pcRanges'),(1, 'pcr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddStroke():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,POINTER(win32more.UI.TabletPC.PACKET_DESCRIPTION_head),UInt32,c_char_p_no,POINTER(win32more.Graphics.Gdi.XFORM_head))(('AddStroke', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'pPacketDesc'),(1, 'cbPacket'),(1, 'pPacket'),(1, 'pXForm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetBestResultString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,POINTER(UInt32),win32more.Foundation.PWSTR)(('GetBestResultString', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'pcSize'),(1, 'pwcBestResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetGuide():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,POINTER(win32more.UI.TabletPC.RECO_GUIDE_head),UInt32)(('SetGuide', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'pGuide'),(1, 'iIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AdviseInkChange():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,win32more.Foundation.BOOL)(('AdviseInkChange', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'bNewStroke'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EndInkInput():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT)(('EndInkInput', windll['inkobjcore.dll']), ((1, 'hrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Process():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,POINTER(win32more.Foundation.BOOL))(('Process', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'pbPartialProcessing'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFactoid():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,UInt32,win32more.Foundation.PWSTR)(('SetFactoid', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'cwcFactoid'),(1, 'pwcFactoid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFlags():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,UInt32)(('SetFlags', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLatticePtr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,POINTER(POINTER(win32more.UI.TabletPC.RECO_LATTICE_head)))(('GetLatticePtr', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'ppLattice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTextContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR)(('SetTextContext', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'cwcBefore'),(1, 'pwcBefore'),(1, 'cwcAfter'),(1, 'pwcAfter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEnabledUnicodeRanges():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,UInt32,POINTER(win32more.UI.TabletPC.CHARACTER_RANGE_head))(('SetEnabledUnicodeRanges', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'cRanges'),(1, 'pcr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsStringSupported():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,UInt32,win32more.Foundation.PWSTR)(('IsStringSupported', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'wcString'),(1, 'pwcString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetWordList():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,win32more.UI.TabletPC.HRECOWORDLIST)(('SetWordList', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'hwl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRightSeparator():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,POINTER(UInt32),win32more.Foundation.PWSTR)(('GetRightSeparator', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'pcSize'),(1, 'pwcRightSeparator'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLeftSeparator():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOCONTEXT,POINTER(UInt32),win32more.Foundation.PWSTR)(('GetLeftSeparator', windll['inkobjcore.dll']), ((1, 'hrc'),(1, 'pcSize'),(1, 'pwcLeftSeparator'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DestroyWordList():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOWORDLIST)(('DestroyWordList', windll['inkobjcore.dll']), ((1, 'hwl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddWordsToWordList():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOWORDLIST,win32more.Foundation.PWSTR)(('AddWordsToWordList', windll['inkobjcore.dll']), ((1, 'hwl'),(1, 'pwcWords'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MakeWordList():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.HRECOGNIZER,win32more.Foundation.PWSTR,POINTER(win32more.UI.TabletPC.HRECOWORDLIST))(('MakeWordList', windll['inkobjcore.dll']), ((1, 'hrec'),(1, 'pBuffer'),(1, 'phwl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAllRecognizers():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(Guid)),POINTER(UInt32))(('GetAllRecognizers', windll['inkobjcore.dll']), ((1, 'recognizerClsids'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadCachedAttributes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.UI.TabletPC.RECO_ATTRS_head))(('LoadCachedAttributes', windll['inkobjcore.dll']), ((1, 'clsid'),(1, 'pRecoAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
AppearanceConstants = Int32
AppearanceConstants_rtfFlat = 0
AppearanceConstants_rtfThreeD = 1
BorderStyleConstants = Int32
BorderStyleConstants_rtfNoBorder = 0
BorderStyleConstants_rtfFixedSingle = 1
def _define_CHARACTER_RANGE_head():
    class CHARACTER_RANGE(Structure):
        pass
    return CHARACTER_RANGE
def _define_CHARACTER_RANGE():
    CHARACTER_RANGE = win32more.UI.TabletPC.CHARACTER_RANGE_head
    CHARACTER_RANGE._fields_ = [
        ('wcLow', Char),
        ('cChars', UInt16),
    ]
    return CHARACTER_RANGE
CONFIDENCE_LEVEL = Int32
CFL_STRONG = 0
CFL_INTERMEDIATE = 1
CFL_POOR = 2
CorrectionMode = Int32
CorrectionMode_NotVisible = 0
CorrectionMode_PreInsertion = 1
CorrectionMode_PostInsertionCollapsed = 2
CorrectionMode_PostInsertionExpanded = 3
CorrectionPosition = Int32
CorrectionPosition_Auto = 0
CorrectionPosition_Bottom = 1
CorrectionPosition_Top = 2
DISPID_Ink = Int32
DISPID_IStrokes = 1
DISPID_IExtendedProperties = 2
DISPID_IGetBoundingBox = 3
DISPID_IDeleteStrokes = 4
DISPID_IDeleteStroke = 5
DISPID_IExtractStrokes = 6
DISPID_IExtractWithRectangle = 7
DISPID_IDirty = 8
DISPID_ICustomStrokes = 9
DISPID_IClone = 10
DISPID_IHitTestCircle = 11
DISPID_IHitTestWithRectangle = 12
DISPID_IHitTestWithLasso = 13
DISPID_INearestPoint = 14
DISPID_ICreateStrokes = 15
DISPID_ICreateStroke = 16
DISPID_IAddStrokesAtRectangle = 17
DISPID_IClip = 18
DISPID_ISave = 19
DISPID_ILoad = 20
DISPID_ICreateStrokeFromPoints = 21
DISPID_IClipboardCopyWithRectangle = 22
DISPID_IClipboardCopy = 23
DISPID_ICanPaste = 24
DISPID_IClipboardPaste = 25
DISPID_InkCollector = Int32
DISPID_ICEnabled = 1
DISPID_ICHwnd = 2
DISPID_ICPaint = 3
DISPID_ICText = 4
DISPID_ICDefaultDrawingAttributes = 5
DISPID_ICRenderer = 6
DISPID_ICInk = 7
DISPID_ICAutoRedraw = 8
DISPID_ICCollectingInk = 9
DISPID_ICSetEventInterest = 10
DISPID_ICGetEventInterest = 11
DISPID_IOEditingMode = 12
DISPID_IOSelection = 13
DISPID_IOAttachMode = 14
DISPID_IOHitTestSelection = 15
DISPID_IODraw = 16
DISPID_IPPicture = 17
DISPID_IPSizeMode = 18
DISPID_IPBackColor = 19
DISPID_ICCursors = 20
DISPID_ICMarginX = 21
DISPID_ICMarginY = 22
DISPID_ICSetWindowInputRectangle = 23
DISPID_ICGetWindowInputRectangle = 24
DISPID_ICTablet = 25
DISPID_ICSetAllTabletsMode = 26
DISPID_ICSetSingleTabletIntegratedMode = 27
DISPID_ICCollectionMode = 28
DISPID_ICSetGestureStatus = 29
DISPID_ICGetGestureStatus = 30
DISPID_ICDynamicRendering = 31
DISPID_ICDesiredPacketDescription = 32
DISPID_IOEraserMode = 33
DISPID_IOEraserWidth = 34
DISPID_ICMouseIcon = 35
DISPID_ICMousePointer = 36
DISPID_IPInkEnabled = 37
DISPID_ICSupportHighContrastInk = 38
DISPID_IOSupportHighContrastSelectionUI = 39
DISPID_InkCollectorEvent = Int32
DISPID_ICEStroke = 1
DISPID_ICECursorDown = 2
DISPID_ICENewPackets = 3
DISPID_ICENewInAirPackets = 4
DISPID_ICECursorButtonDown = 5
DISPID_ICECursorButtonUp = 6
DISPID_ICECursorInRange = 7
DISPID_ICECursorOutOfRange = 8
DISPID_ICESystemGesture = 9
DISPID_ICEGesture = 10
DISPID_ICETabletAdded = 11
DISPID_ICETabletRemoved = 12
DISPID_IOEPainting = 13
DISPID_IOEPainted = 14
DISPID_IOESelectionChanging = 15
DISPID_IOESelectionChanged = 16
DISPID_IOESelectionMoving = 17
DISPID_IOESelectionMoved = 18
DISPID_IOESelectionResizing = 19
DISPID_IOESelectionResized = 20
DISPID_IOEStrokesDeleting = 21
DISPID_IOEStrokesDeleted = 22
DISPID_IPEChangeUICues = 23
DISPID_IPEClick = 24
DISPID_IPEDblClick = 25
DISPID_IPEInvalidated = 26
DISPID_IPEMouseDown = 27
DISPID_IPEMouseEnter = 28
DISPID_IPEMouseHover = 29
DISPID_IPEMouseLeave = 30
DISPID_IPEMouseMove = 31
DISPID_IPEMouseUp = 32
DISPID_IPEMouseWheel = 33
DISPID_IPESizeModeChanged = 34
DISPID_IPEStyleChanged = 35
DISPID_IPESystemColorsChanged = 36
DISPID_IPEKeyDown = 37
DISPID_IPEKeyPress = 38
DISPID_IPEKeyUp = 39
DISPID_IPEResize = 40
DISPID_IPESizeChanged = 41
DISPID_InkCursor = Int32
DISPID_ICsrName = 0
DISPID_ICsrId = 1
DISPID_ICsrDrawingAttributes = 2
DISPID_ICsrButtons = 3
DISPID_ICsrInverted = 4
DISPID_ICsrTablet = 5
DISPID_InkCursorButton = Int32
DISPID_ICBName = 0
DISPID_ICBId = 1
DISPID_ICBState = 2
DISPID_InkCursorButtons = Int32
DISPID_ICBs_NewEnum = -4
DISPID_ICBsItem = 0
DISPID_ICBsCount = 1
DISPID_InkCursors = Int32
DISPID_ICs_NewEnum = -4
DISPID_ICsItem = 0
DISPID_ICsCount = 1
DISPID_InkCustomStrokes = Int32
DISPID_ICSs_NewEnum = -4
DISPID_ICSsItem = 0
DISPID_ICSsCount = 1
DISPID_ICSsAdd = 2
DISPID_ICSsRemove = 3
DISPID_ICSsClear = 4
DISPID_InkDivider = Int32
DISPID_IInkDivider_Strokes = 1
DISPID_IInkDivider_RecognizerContext = 2
DISPID_IInkDivider_LineHeight = 3
DISPID_IInkDivider_Divide = 4
DISPID_InkDivisionResult = Int32
DISPID_IInkDivisionResult_Strokes = 1
DISPID_IInkDivisionResult_ResultByType = 2
DISPID_InkDivisionUnit = Int32
DISPID_IInkDivisionUnit_Strokes = 1
DISPID_IInkDivisionUnit_DivisionType = 2
DISPID_IInkDivisionUnit_RecognizedString = 3
DISPID_IInkDivisionUnit_RotationTransform = 4
DISPID_InkDivisionUnits = Int32
DISPID_IInkDivisionUnits_NewEnum = -4
DISPID_IInkDivisionUnits_Item = 0
DISPID_IInkDivisionUnits_Count = 1
DISPID_InkDrawingAttributes = Int32
DISPID_DAHeight = 1
DISPID_DAColor = 2
DISPID_DAWidth = 3
DISPID_DAFitToCurve = 4
DISPID_DAIgnorePressure = 5
DISPID_DAAntiAliased = 6
DISPID_DATransparency = 7
DISPID_DARasterOperation = 8
DISPID_DAPenTip = 9
DISPID_DAClone = 10
DISPID_DAExtendedProperties = 11
DISPID_InkEdit = Int32
DISPID_Text = 0
DISPID_TextRTF = 1
DISPID_Hwnd = 2
DISPID_DisableNoScroll = 3
DISPID_Locked = 4
DISPID_Enabled = 5
DISPID_MaxLength = 6
DISPID_MultiLine = 7
DISPID_ScrollBars = 8
DISPID_RTSelStart = 9
DISPID_RTSelLength = 10
DISPID_RTSelText = 11
DISPID_SelAlignment = 12
DISPID_SelBold = 13
DISPID_SelCharOffset = 14
DISPID_SelColor = 15
DISPID_SelFontName = 16
DISPID_SelFontSize = 17
DISPID_SelItalic = 18
DISPID_SelRTF = 19
DISPID_SelUnderline = 20
DISPID_DragIcon = 21
DISPID_Status = 22
DISPID_UseMouseForInput = 23
DISPID_InkMode = 24
DISPID_InkInsertMode = 25
DISPID_RecoTimeout = 26
DISPID_DrawAttr = 27
DISPID_Recognizer = 28
DISPID_Factoid = 29
DISPID_SelInk = 30
DISPID_SelInksDisplayMode = 31
DISPID_Recognize = 32
DISPID_GetGestStatus = 33
DISPID_SetGestStatus = 34
DISPID_Refresh = 35
DISPID_InkEditEvents = Int32
DISPID_IeeChange = 1
DISPID_IeeSelChange = 2
DISPID_IeeKeyDown = 3
DISPID_IeeKeyUp = 4
DISPID_IeeMouseUp = 5
DISPID_IeeMouseDown = 6
DISPID_IeeKeyPress = 7
DISPID_IeeDblClick = 8
DISPID_IeeClick = 9
DISPID_IeeMouseMove = 10
DISPID_IeeCursorDown = 21
DISPID_IeeStroke = 22
DISPID_IeeGesture = 23
DISPID_IeeRecognitionResult = 24
DISPID_InkEvent = Int32
DISPID_IEInkAdded = 1
DISPID_IEInkDeleted = 2
DISPID_InkExtendedProperties = Int32
DISPID_IEPs_NewEnum = -4
DISPID_IEPsItem = 0
DISPID_IEPsCount = 1
DISPID_IEPsAdd = 2
DISPID_IEPsRemove = 3
DISPID_IEPsClear = 4
DISPID_IEPsDoesPropertyExist = 5
DISPID_InkExtendedProperty = Int32
DISPID_IEPGuid = 1
DISPID_IEPData = 2
DISPID_InkGesture = Int32
DISPID_IGId = 0
DISPID_IGGetHotPoint = 1
DISPID_IGConfidence = 2
DISPID_InkRecoAlternate = Int32
DISPID_InkRecoAlternate_String = 1
DISPID_InkRecoAlternate_LineNumber = 2
DISPID_InkRecoAlternate_Baseline = 3
DISPID_InkRecoAlternate_Midline = 4
DISPID_InkRecoAlternate_Ascender = 5
DISPID_InkRecoAlternate_Descender = 6
DISPID_InkRecoAlternate_Confidence = 7
DISPID_InkRecoAlternate_Strokes = 8
DISPID_InkRecoAlternate_GetStrokesFromStrokeRanges = 9
DISPID_InkRecoAlternate_GetStrokesFromTextRange = 10
DISPID_InkRecoAlternate_GetTextRangeFromStrokes = 11
DISPID_InkRecoAlternate_GetPropertyValue = 12
DISPID_InkRecoAlternate_LineAlternates = 13
DISPID_InkRecoAlternate_ConfidenceAlternates = 14
DISPID_InkRecoAlternate_AlternatesWithConstantPropertyValues = 15
DISPID_InkRecoContext = Int32
DISPID_IRecoCtx_Strokes = 1
DISPID_IRecoCtx_CharacterAutoCompletionMode = 2
DISPID_IRecoCtx_Factoid = 3
DISPID_IRecoCtx_WordList = 4
DISPID_IRecoCtx_Recognizer = 5
DISPID_IRecoCtx_Guide = 6
DISPID_IRecoCtx_Flags = 7
DISPID_IRecoCtx_PrefixText = 8
DISPID_IRecoCtx_SuffixText = 9
DISPID_IRecoCtx_StopRecognition = 10
DISPID_IRecoCtx_Clone = 11
DISPID_IRecoCtx_Recognize = 12
DISPID_IRecoCtx_StopBackgroundRecognition = 13
DISPID_IRecoCtx_EndInkInput = 14
DISPID_IRecoCtx_BackgroundRecognize = 15
DISPID_IRecoCtx_BackgroundRecognizeWithAlternates = 16
DISPID_IRecoCtx_IsStringSupported = 17
DISPID_InkRecoContext2 = Int32
DISPID_IRecoCtx2_EnabledUnicodeRanges = 0
DISPID_InkRecognitionAlternates = Int32
DISPID_InkRecognitionAlternates_NewEnum = -4
DISPID_InkRecognitionAlternates_Item = 0
DISPID_InkRecognitionAlternates_Count = 1
DISPID_InkRecognitionAlternates_Strokes = 2
DISPID_InkRecognitionEvent = Int32
DISPID_IRERecognitionWithAlternates = 1
DISPID_IRERecognition = 2
DISPID_InkRecognitionResult = Int32
DISPID_InkRecognitionResult_TopString = 1
DISPID_InkRecognitionResult_TopAlternate = 2
DISPID_InkRecognitionResult_Strokes = 3
DISPID_InkRecognitionResult_TopConfidence = 4
DISPID_InkRecognitionResult_AlternatesFromSelection = 5
DISPID_InkRecognitionResult_ModifyTopAlternate = 6
DISPID_InkRecognitionResult_SetResultOnStrokes = 7
DISPID_InkRecognizer = Int32
DISPID_RecoClsid = 1
DISPID_RecoName = 2
DISPID_RecoVendor = 3
DISPID_RecoCapabilities = 4
DISPID_RecoLanguageID = 5
DISPID_RecoPreferredPacketDescription = 6
DISPID_RecoCreateRecognizerContext = 7
DISPID_RecoSupportedProperties = 8
DISPID_InkRecognizer2 = Int32
DISPID_RecoId = 0
DISPID_RecoUnicodeRanges = 1
DISPID_InkRecognizerGuide = Int32
DISPID_IRGWritingBox = 1
DISPID_IRGDrawnBox = 2
DISPID_IRGRows = 3
DISPID_IRGColumns = 4
DISPID_IRGMidline = 5
DISPID_IRGGuideData = 6
DISPID_InkRecognizers = Int32
DISPID_IRecos_NewEnum = -4
DISPID_IRecosItem = 0
DISPID_IRecosCount = 1
DISPID_IRecosGetDefaultRecognizer = 2
DISPID_InkRectangle = Int32
DISPID_IRTop = 1
DISPID_IRLeft = 2
DISPID_IRBottom = 3
DISPID_IRRight = 4
DISPID_IRGetRectangle = 5
DISPID_IRSetRectangle = 6
DISPID_IRData = 7
DISPID_InkRenderer = Int32
DISPID_IRGetViewTransform = 1
DISPID_IRSetViewTransform = 2
DISPID_IRGetObjectTransform = 3
DISPID_IRSetObjectTransform = 4
DISPID_IRDraw = 5
DISPID_IRDrawStroke = 6
DISPID_IRPixelToInkSpace = 7
DISPID_IRInkSpaceToPixel = 8
DISPID_IRPixelToInkSpaceFromPoints = 9
DISPID_IRInkSpaceToPixelFromPoints = 10
DISPID_IRMeasure = 11
DISPID_IRMeasureStroke = 12
DISPID_IRMove = 13
DISPID_IRRotate = 14
DISPID_IRScale = 15
DISPID_InkStrokeDisp = Int32
DISPID_ISDInkIndex = 1
DISPID_ISDID = 2
DISPID_ISDGetBoundingBox = 3
DISPID_ISDDrawingAttributes = 4
DISPID_ISDFindIntersections = 5
DISPID_ISDGetRectangleIntersections = 6
DISPID_ISDClip = 7
DISPID_ISDHitTestCircle = 8
DISPID_ISDNearestPoint = 9
DISPID_ISDSplit = 10
DISPID_ISDExtendedProperties = 11
DISPID_ISDInk = 12
DISPID_ISDBezierPoints = 13
DISPID_ISDPolylineCusps = 14
DISPID_ISDBezierCusps = 15
DISPID_ISDSelfIntersections = 16
DISPID_ISDPacketCount = 17
DISPID_ISDPacketSize = 18
DISPID_ISDPacketDescription = 19
DISPID_ISDDeleted = 20
DISPID_ISDGetPacketDescriptionPropertyMetrics = 21
DISPID_ISDGetPoints = 22
DISPID_ISDSetPoints = 23
DISPID_ISDGetPacketData = 24
DISPID_ISDGetPacketValuesByProperty = 25
DISPID_ISDSetPacketValuesByProperty = 26
DISPID_ISDGetFlattenedBezierPoints = 27
DISPID_ISDScaleToRectangle = 28
DISPID_ISDTransform = 29
DISPID_ISDMove = 30
DISPID_ISDRotate = 31
DISPID_ISDShear = 32
DISPID_ISDScale = 33
DISPID_InkStrokes = Int32
DISPID_ISs_NewEnum = -4
DISPID_ISsItem = 0
DISPID_ISsCount = 1
DISPID_ISsValid = 2
DISPID_ISsInk = 3
DISPID_ISsAdd = 4
DISPID_ISsAddStrokes = 5
DISPID_ISsRemove = 6
DISPID_ISsRemoveStrokes = 7
DISPID_ISsToString = 8
DISPID_ISsModifyDrawingAttributes = 9
DISPID_ISsGetBoundingBox = 10
DISPID_ISsScaleToRectangle = 11
DISPID_ISsTransform = 12
DISPID_ISsMove = 13
DISPID_ISsRotate = 14
DISPID_ISsShear = 15
DISPID_ISsScale = 16
DISPID_ISsClip = 17
DISPID_ISsRecognitionResult = 18
DISPID_ISsRemoveRecognitionResult = 19
DISPID_InkTablet = Int32
DISPID_ITName = 0
DISPID_ITPlugAndPlayId = 1
DISPID_ITPropertyMetrics = 2
DISPID_ITIsPacketPropertySupported = 3
DISPID_ITMaximumInputRectangle = 4
DISPID_ITHardwareCapabilities = 5
DISPID_InkTablet2 = Int32
DISPID_IT2DeviceKind = 0
DISPID_InkTablet3 = Int32
DISPID_IT3IsMultiTouch = 0
DISPID_IT3MaximumCursors = 1
DISPID_InkTablets = Int32
DISPID_ITs_NewEnum = -4
DISPID_ITsItem = 0
DISPID_ITsDefaultTablet = 1
DISPID_ITsCount = 2
DISPID_ITsIsPacketPropertySupported = 3
DISPID_InkTransform = Int32
DISPID_ITReset = 1
DISPID_ITTranslate = 2
DISPID_ITRotate = 3
DISPID_ITReflect = 4
DISPID_ITShear = 5
DISPID_ITScale = 6
DISPID_ITeM11 = 7
DISPID_ITeM12 = 8
DISPID_ITeM21 = 9
DISPID_ITeM22 = 10
DISPID_ITeDx = 11
DISPID_ITeDy = 12
DISPID_ITGetTransform = 13
DISPID_ITSetTransform = 14
DISPID_ITData = 15
DISPID_InkWordList = Int32
DISPID_InkWordList_AddWord = 0
DISPID_InkWordList_RemoveWord = 1
DISPID_InkWordList_Merge = 2
DISPID_InkWordList2 = Int32
DISPID_InkWordList2_AddWords = 3
DISPID_MathInputControlEvents = Int32
DISPID_MICInsert = 0
DISPID_MICClose = 1
DISPID_MICPaint = 2
DISPID_MICClear = 3
DISPID_PenInputPanel = Int32
DISPID_PIPAttachedEditWindow = 0
DISPID_PIPFactoid = 1
DISPID_PIPCurrentPanel = 2
DISPID_PIPDefaultPanel = 3
DISPID_PIPVisible = 4
DISPID_PIPTop = 5
DISPID_PIPLeft = 6
DISPID_PIPWidth = 7
DISPID_PIPHeight = 8
DISPID_PIPMoveTo = 9
DISPID_PIPCommitPendingInput = 10
DISPID_PIPRefresh = 11
DISPID_PIPBusy = 12
DISPID_PIPVerticalOffset = 13
DISPID_PIPHorizontalOffset = 14
DISPID_PIPEnableTsf = 15
DISPID_PIPAutoShow = 16
DISPID_PenInputPanelEvents = Int32
DISPID_PIPEVisibleChanged = 0
DISPID_PIPEPanelChanged = 1
DISPID_PIPEInputFailed = 2
DISPID_PIPEPanelMoving = 3
DISPID_StrokeEvent = Int32
DISPID_SEStrokesAdded = 1
DISPID_SEStrokesRemoved = 2
def _define_DYNAMIC_RENDERER_CACHED_DATA_head():
    class DYNAMIC_RENDERER_CACHED_DATA(Structure):
        pass
    return DYNAMIC_RENDERER_CACHED_DATA
def _define_DYNAMIC_RENDERER_CACHED_DATA():
    DYNAMIC_RENDERER_CACHED_DATA = win32more.UI.TabletPC.DYNAMIC_RENDERER_CACHED_DATA_head
    DYNAMIC_RENDERER_CACHED_DATA._fields_ = [
        ('strokeId', Int32),
        ('dynamicRenderer', win32more.UI.TabletPC.IDynamicRenderer_head),
    ]
    return DYNAMIC_RENDERER_CACHED_DATA
DynamicRenderer = Guid('ecd32aea-746f-4dcb-bf-68-08-27-57-fa-ff-18')
EventMask = Int32
EventMask_InPlaceStateChanging = 1
EventMask_InPlaceStateChanged = 2
EventMask_InPlaceSizeChanging = 4
EventMask_InPlaceSizeChanged = 8
EventMask_InputAreaChanging = 16
EventMask_InputAreaChanged = 32
EventMask_CorrectionModeChanging = 64
EventMask_CorrectionModeChanged = 128
EventMask_InPlaceVisibilityChanging = 256
EventMask_InPlaceVisibilityChanged = 512
EventMask_TextInserting = 1024
EventMask_TextInserted = 2048
EventMask_All = 4095
def _define_FLICK_DATA_head():
    class FLICK_DATA(Structure):
        pass
    return FLICK_DATA
def _define_FLICK_DATA():
    FLICK_DATA = win32more.UI.TabletPC.FLICK_DATA_head
    FLICK_DATA._fields_ = [
        ('_bitfield', Int32),
    ]
    return FLICK_DATA
def _define_FLICK_POINT_head():
    class FLICK_POINT(Structure):
        pass
    return FLICK_POINT
def _define_FLICK_POINT():
    FLICK_POINT = win32more.UI.TabletPC.FLICK_POINT_head
    FLICK_POINT._fields_ = [
        ('_bitfield', Int32),
    ]
    return FLICK_POINT
FLICKACTION_COMMANDCODE = Int32
FLICKACTION_COMMANDCODE_NULL = 0
FLICKACTION_COMMANDCODE_SCROLL = 1
FLICKACTION_COMMANDCODE_APPCOMMAND = 2
FLICKACTION_COMMANDCODE_CUSTOMKEY = 3
FLICKACTION_COMMANDCODE_KEYMODIFIER = 4
FLICKDIRECTION = Int32
FLICKDIRECTION_MIN = 0
FLICKDIRECTION_RIGHT = 0
FLICKDIRECTION_UPRIGHT = 1
FLICKDIRECTION_UP = 2
FLICKDIRECTION_UPLEFT = 3
FLICKDIRECTION_LEFT = 4
FLICKDIRECTION_DOWNLEFT = 5
FLICKDIRECTION_DOWN = 6
FLICKDIRECTION_DOWNRIGHT = 7
FLICKDIRECTION_INVALID = 8
FLICKMODE = Int32
FLICKMODE_MIN = 0
FLICKMODE_OFF = 0
FLICKMODE_ON = 1
FLICKMODE_LEARNING = 2
FLICKMODE_MAX = 2
FLICKMODE_DEFAULT = 1
def _define_GESTURE_DATA_head():
    class GESTURE_DATA(Structure):
        pass
    return GESTURE_DATA
def _define_GESTURE_DATA():
    GESTURE_DATA = win32more.UI.TabletPC.GESTURE_DATA_head
    GESTURE_DATA._fields_ = [
        ('gestureId', Int32),
        ('recoConfidence', Int32),
        ('strokeCount', Int32),
    ]
    return GESTURE_DATA
GestureRecognizer = Guid('ea30c654-c62c-441f-ac-00-95-f9-a1-96-78-2c')
GET_DANDIDATE_FLAGS = Int32
TCF_ALLOW_RECOGNITION = 1
TCF_FORCE_RECOGNITION = 2
HandwrittenTextInsertion = Guid('9f074ee2-e6e9-4d8a-a0-47-eb-5b-5c-3c-55-da')
HRECOALT = IntPtr
HRECOCONTEXT = IntPtr
HRECOGNIZER = IntPtr
HRECOLATTICE = IntPtr
HRECOWORDLIST = IntPtr
def _define_IDynamicRenderer_head():
    class IDynamicRenderer(win32more.System.Com.IUnknown_head):
        Guid = Guid('a079468e-7165-46f9-b7-af-98-ad-01-a9-30-09')
    return IDynamicRenderer
def _define_IDynamicRenderer():
    IDynamicRenderer = win32more.UI.TabletPC.IDynamicRenderer_head
    IDynamicRenderer.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'get_Enabled', ((1, 'bEnabled'),)))
    IDynamicRenderer.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(4, 'put_Enabled', ((1, 'bEnabled'),)))
    IDynamicRenderer.get_HWND = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE_PTR))(5, 'get_HWND', ((1, 'hwnd'),)))
    IDynamicRenderer.put_HWND = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE_PTR)(6, 'put_HWND', ((1, 'hwnd'),)))
    IDynamicRenderer.get_ClipRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(7, 'get_ClipRectangle', ((1, 'prcClipRect'),)))
    IDynamicRenderer.put_ClipRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(8, 'put_ClipRectangle', ((1, 'prcClipRect'),)))
    IDynamicRenderer.get_ClipRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE_PTR))(9, 'get_ClipRegion', ((1, 'phClipRgn'),)))
    IDynamicRenderer.put_ClipRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE_PTR)(10, 'put_ClipRegion', ((1, 'hClipRgn'),)))
    IDynamicRenderer.get_DrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDrawingAttributes_head))(11, 'get_DrawingAttributes', ((1, 'ppiDA'),)))
    IDynamicRenderer.putref_DrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkDrawingAttributes_head)(12, 'putref_DrawingAttributes', ((1, 'piDA'),)))
    IDynamicRenderer.get_DataCacheEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(13, 'get_DataCacheEnabled', ((1, 'pfCacheData'),)))
    IDynamicRenderer.put_DataCacheEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(14, 'put_DataCacheEnabled', ((1, 'fCacheData'),)))
    IDynamicRenderer.ReleaseCachedData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(15, 'ReleaseCachedData', ((1, 'strokeId'),)))
    IDynamicRenderer.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'Refresh', ()))
    IDynamicRenderer.Draw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE_PTR)(17, 'Draw', ((1, 'hDC'),)))
    win32more.System.Com.IUnknown
    return IDynamicRenderer
def _define_IEC_GESTUREINFO_head():
    class IEC_GESTUREINFO(Structure):
        pass
    return IEC_GESTUREINFO
def _define_IEC_GESTUREINFO():
    IEC_GESTUREINFO = win32more.UI.TabletPC.IEC_GESTUREINFO_head
    IEC_GESTUREINFO._fields_ = [
        ('nmhdr', win32more.UI.Controls.NMHDR),
        ('Cursor', win32more.UI.TabletPC.IInkCursor_head),
        ('Strokes', win32more.UI.TabletPC.IInkStrokes_head),
        ('Gestures', win32more.System.Com.VARIANT),
    ]
    return IEC_GESTUREINFO
def _define_IEC_RECOGNITIONRESULTINFO_head():
    class IEC_RECOGNITIONRESULTINFO(Structure):
        pass
    return IEC_RECOGNITIONRESULTINFO
def _define_IEC_RECOGNITIONRESULTINFO():
    IEC_RECOGNITIONRESULTINFO = win32more.UI.TabletPC.IEC_RECOGNITIONRESULTINFO_head
    IEC_RECOGNITIONRESULTINFO._fields_ = [
        ('nmhdr', win32more.UI.Controls.NMHDR),
        ('RecognitionResult', win32more.UI.TabletPC.IInkRecognitionResult_head),
    ]
    return IEC_RECOGNITIONRESULTINFO
def _define_IEC_STROKEINFO_head():
    class IEC_STROKEINFO(Structure):
        pass
    return IEC_STROKEINFO
def _define_IEC_STROKEINFO():
    IEC_STROKEINFO = win32more.UI.TabletPC.IEC_STROKEINFO_head
    IEC_STROKEINFO._fields_ = [
        ('nmhdr', win32more.UI.Controls.NMHDR),
        ('Cursor', win32more.UI.TabletPC.IInkCursor_head),
        ('Stroke', win32more.UI.TabletPC.IInkStrokeDisp_head),
    ]
    return IEC_STROKEINFO
def _define_IGestureRecognizer_head():
    class IGestureRecognizer(win32more.System.Com.IUnknown_head):
        Guid = Guid('ae9ef86b-7054-45e3-ae-22-31-74-dc-88-11-b7')
    return IGestureRecognizer
def _define_IGestureRecognizer():
    IGestureRecognizer = win32more.UI.TabletPC.IGestureRecognizer_head
    IGestureRecognizer.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'get_Enabled', ((1, 'pfEnabled'),)))
    IGestureRecognizer.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(4, 'put_Enabled', ((1, 'fEnabled'),)))
    IGestureRecognizer.get_MaxStrokeCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(5, 'get_MaxStrokeCount', ((1, 'pcStrokes'),)))
    IGestureRecognizer.put_MaxStrokeCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(6, 'put_MaxStrokeCount', ((1, 'cStrokes'),)))
    IGestureRecognizer.EnableGestures = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Int32))(7, 'EnableGestures', ((1, 'cGestures'),(1, 'pGestures'),)))
    IGestureRecognizer.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Reset', ()))
    win32more.System.Com.IUnknown
    return IGestureRecognizer
def _define_IHandwrittenTextInsertion_head():
    class IHandwrittenTextInsertion(win32more.System.Com.IUnknown_head):
        Guid = Guid('56fdea97-ecd6-43e7-aa-3a-81-6b-e7-78-58-60')
    return IHandwrittenTextInsertion
def _define_IHandwrittenTextInsertion():
    IHandwrittenTextInsertion = win32more.UI.TabletPC.IHandwrittenTextInsertion_head
    IHandwrittenTextInsertion.InsertRecognitionResultsArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),UInt32,win32more.Foundation.BOOL)(3, 'InsertRecognitionResultsArray', ((1, 'psaAlternates'),(1, 'locale'),(1, 'fAlternateContainsAutoSpacingInformation'),)))
    IHandwrittenTextInsertion.InsertInkRecognitionResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRecognitionResult_head,UInt32,win32more.Foundation.BOOL)(4, 'InsertInkRecognitionResult', ((1, 'pIInkRecoResult'),(1, 'locale'),(1, 'fAlternateContainsAutoSpacingInformation'),)))
    win32more.System.Com.IUnknown
    return IHandwrittenTextInsertion
def _define_IInk_head():
    class IInk(win32more.System.Com.IDispatch_head):
        Guid = Guid('03f8e511-43a1-11d3-8b-b6-00-80-c7-d6-ba-d5')
    return IInk
def _define_IInk():
    IInk = win32more.UI.TabletPC.IInk_head
    win32more.System.Com.IDispatch
    return IInk
def _define_IInkCollector_head():
    class IInkCollector(win32more.System.Com.IDispatch_head):
        Guid = Guid('f0f060b5-8b1f-4a7c-89-ec-88-06-92-58-8a-4f')
    return IInkCollector
def _define_IInkCollector():
    IInkCollector = win32more.UI.TabletPC.IInkCollector_head
    IInkCollector.get_hWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(IntPtr))(7, 'get_hWnd', ((1, 'CurrentWindow'),)))
    IInkCollector.put_hWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr)(8, 'put_hWnd', ((1, 'NewWindow'),)))
    IInkCollector.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_Enabled', ((1, 'Collecting'),)))
    IInkCollector.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(10, 'put_Enabled', ((1, 'Collecting'),)))
    IInkCollector.get_DefaultDrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDrawingAttributes_head))(11, 'get_DefaultDrawingAttributes', ((1, 'CurrentAttributes'),)))
    IInkCollector.putref_DefaultDrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkDrawingAttributes_head)(12, 'putref_DefaultDrawingAttributes', ((1, 'NewAttributes'),)))
    IInkCollector.get_Renderer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRenderer_head))(13, 'get_Renderer', ((1, 'CurrentInkRenderer'),)))
    IInkCollector.putref_Renderer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRenderer_head)(14, 'putref_Renderer', ((1, 'NewInkRenderer'),)))
    IInkCollector.get_Ink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDisp_head))(15, 'get_Ink', ((1, 'Ink'),)))
    IInkCollector.putref_Ink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkDisp_head)(16, 'putref_Ink', ((1, 'NewInk'),)))
    IInkCollector.get_AutoRedraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(17, 'get_AutoRedraw', ((1, 'AutoRedraw'),)))
    IInkCollector.put_AutoRedraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(18, 'put_AutoRedraw', ((1, 'AutoRedraw'),)))
    IInkCollector.get_CollectingInk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(19, 'get_CollectingInk', ((1, 'Collecting'),)))
    IInkCollector.get_CollectionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkCollectionMode))(20, 'get_CollectionMode', ((1, 'Mode'),)))
    IInkCollector.put_CollectionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkCollectionMode)(21, 'put_CollectionMode', ((1, 'Mode'),)))
    IInkCollector.get_DynamicRendering = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(22, 'get_DynamicRendering', ((1, 'Enabled'),)))
    IInkCollector.put_DynamicRendering = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(23, 'put_DynamicRendering', ((1, 'Enabled'),)))
    IInkCollector.get_DesiredPacketDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(24, 'get_DesiredPacketDescription', ((1, 'PacketGuids'),)))
    IInkCollector.put_DesiredPacketDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(25, 'put_DesiredPacketDescription', ((1, 'PacketGuids'),)))
    IInkCollector.get_MouseIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IPictureDisp_head))(26, 'get_MouseIcon', ((1, 'MouseIcon'),)))
    IInkCollector.put_MouseIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IPictureDisp_head)(27, 'put_MouseIcon', ((1, 'MouseIcon'),)))
    IInkCollector.putref_MouseIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IPictureDisp_head)(28, 'putref_MouseIcon', ((1, 'MouseIcon'),)))
    IInkCollector.get_MousePointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkMousePointer))(29, 'get_MousePointer', ((1, 'MousePointer'),)))
    IInkCollector.put_MousePointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkMousePointer)(30, 'put_MousePointer', ((1, 'MousePointer'),)))
    IInkCollector.get_Cursors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkCursors_head))(31, 'get_Cursors', ((1, 'Cursors'),)))
    IInkCollector.get_MarginX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(32, 'get_MarginX', ((1, 'MarginX'),)))
    IInkCollector.put_MarginX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(33, 'put_MarginX', ((1, 'MarginX'),)))
    IInkCollector.get_MarginY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(34, 'get_MarginY', ((1, 'MarginY'),)))
    IInkCollector.put_MarginY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(35, 'put_MarginY', ((1, 'MarginY'),)))
    IInkCollector.get_Tablet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkTablet_head))(36, 'get_Tablet', ((1, 'SingleTablet'),)))
    IInkCollector.get_SupportHighContrastInk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(37, 'get_SupportHighContrastInk', ((1, 'Support'),)))
    IInkCollector.put_SupportHighContrastInk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(38, 'put_SupportHighContrastInk', ((1, 'Support'),)))
    IInkCollector.SetGestureStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkApplicationGesture,win32more.Foundation.VARIANT_BOOL)(39, 'SetGestureStatus', ((1, 'Gesture'),(1, 'Listen'),)))
    IInkCollector.GetGestureStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkApplicationGesture,POINTER(win32more.Foundation.VARIANT_BOOL))(40, 'GetGestureStatus', ((1, 'Gesture'),(1, 'Listening'),)))
    IInkCollector.GetWindowInputRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRectangle_head))(41, 'GetWindowInputRectangle', ((1, 'WindowInputRectangle'),)))
    IInkCollector.SetWindowInputRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head)(42, 'SetWindowInputRectangle', ((1, 'WindowInputRectangle'),)))
    IInkCollector.SetAllTabletsMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(43, 'SetAllTabletsMode', ((1, 'UseMouseForInput'),)))
    IInkCollector.SetSingleTabletIntegratedMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkTablet_head)(44, 'SetSingleTabletIntegratedMode', ((1, 'Tablet'),)))
    IInkCollector.GetEventInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkCollectorEventInterest,POINTER(win32more.Foundation.VARIANT_BOOL))(45, 'GetEventInterest', ((1, 'EventId'),(1, 'Listen'),)))
    IInkCollector.SetEventInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkCollectorEventInterest,win32more.Foundation.VARIANT_BOOL)(46, 'SetEventInterest', ((1, 'EventId'),(1, 'Listen'),)))
    win32more.System.Com.IDispatch
    return IInkCollector
def _define_IInkCursor_head():
    class IInkCursor(win32more.System.Com.IDispatch_head):
        Guid = Guid('ad30c630-40c5-4350-84-05-9c-71-01-2f-c5-58')
    return IInkCursor
def _define_IInkCursor():
    IInkCursor = win32more.UI.TabletPC.IInkCursor_head
    IInkCursor.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'Name'),)))
    IInkCursor.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(8, 'get_Id', ((1, 'Id'),)))
    IInkCursor.get_Inverted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_Inverted', ((1, 'Status'),)))
    IInkCursor.get_DrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDrawingAttributes_head))(10, 'get_DrawingAttributes', ((1, 'Attributes'),)))
    IInkCursor.putref_DrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkDrawingAttributes_head)(11, 'putref_DrawingAttributes', ((1, 'Attributes'),)))
    IInkCursor.get_Tablet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkTablet_head))(12, 'get_Tablet', ((1, 'Tablet'),)))
    IInkCursor.get_Buttons = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkCursorButtons_head))(13, 'get_Buttons', ((1, 'Buttons'),)))
    win32more.System.Com.IDispatch
    return IInkCursor
def _define_IInkCursorButton_head():
    class IInkCursorButton(win32more.System.Com.IDispatch_head):
        Guid = Guid('85ef9417-1d59-49b2-a1-3c-70-2c-85-43-08-94')
    return IInkCursorButton
def _define_IInkCursorButton():
    IInkCursorButton = win32more.UI.TabletPC.IInkCursorButton_head
    IInkCursorButton.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'Name'),)))
    IInkCursorButton.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Id', ((1, 'Id'),)))
    IInkCursorButton.get_State = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkCursorButtonState))(9, 'get_State', ((1, 'CurrentState'),)))
    win32more.System.Com.IDispatch
    return IInkCursorButton
def _define_IInkCursorButtons_head():
    class IInkCursorButtons(win32more.System.Com.IDispatch_head):
        Guid = Guid('3671cc40-b624-4671-9f-a0-db-11-9d-95-2d-54')
    return IInkCursorButtons
def _define_IInkCursorButtons():
    IInkCursorButtons = win32more.UI.TabletPC.IInkCursorButtons_head
    IInkCursorButtons.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'Count'),)))
    IInkCursorButtons.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(8, 'get__NewEnum', ((1, '_NewEnum'),)))
    IInkCursorButtons.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.UI.TabletPC.IInkCursorButton_head))(9, 'Item', ((1, 'Identifier'),(1, 'Button'),)))
    win32more.System.Com.IDispatch
    return IInkCursorButtons
def _define_IInkCursors_head():
    class IInkCursors(win32more.System.Com.IDispatch_head):
        Guid = Guid('a248c1ac-c698-4e06-9e-5c-d5-7f-77-c7-e6-47')
    return IInkCursors
def _define_IInkCursors():
    IInkCursors = win32more.UI.TabletPC.IInkCursors_head
    IInkCursors.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'Count'),)))
    IInkCursors.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(8, 'get__NewEnum', ((1, '_NewEnum'),)))
    IInkCursors.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.TabletPC.IInkCursor_head))(9, 'Item', ((1, 'Index'),(1, 'Cursor'),)))
    win32more.System.Com.IDispatch
    return IInkCursors
def _define_IInkCustomStrokes_head():
    class IInkCustomStrokes(win32more.System.Com.IDispatch_head):
        Guid = Guid('7e23a88f-c30e-420f-9b-db-28-90-25-43-f0-c1')
    return IInkCustomStrokes
def _define_IInkCustomStrokes():
    IInkCustomStrokes = win32more.UI.TabletPC.IInkCustomStrokes_head
    IInkCustomStrokes.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'Count'),)))
    IInkCustomStrokes.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(8, 'get__NewEnum', ((1, '_NewEnum'),)))
    IInkCustomStrokes.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(9, 'Item', ((1, 'Identifier'),(1, 'Strokes'),)))
    IInkCustomStrokes.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.UI.TabletPC.IInkStrokes_head)(10, 'Add', ((1, 'Name'),(1, 'Strokes'),)))
    IInkCustomStrokes.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(11, 'Remove', ((1, 'Identifier'),)))
    IInkCustomStrokes.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'Clear', ()))
    win32more.System.Com.IDispatch
    return IInkCustomStrokes
def _define_IInkDisp_head():
    class IInkDisp(win32more.System.Com.IDispatch_head):
        Guid = Guid('9d398fa0-c4e2-4fcd-99-73-97-5c-aa-f4-7e-a6')
    return IInkDisp
def _define_IInkDisp():
    IInkDisp = win32more.UI.TabletPC.IInkDisp_head
    IInkDisp.get_Strokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(7, 'get_Strokes', ((1, 'Strokes'),)))
    IInkDisp.get_ExtendedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkExtendedProperties_head))(8, 'get_ExtendedProperties', ((1, 'Properties'),)))
    IInkDisp.get_Dirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_Dirty', ((1, 'Dirty'),)))
    IInkDisp.put_Dirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(10, 'put_Dirty', ((1, 'Dirty'),)))
    IInkDisp.get_CustomStrokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkCustomStrokes_head))(11, 'get_CustomStrokes', ((1, 'ppunkInkCustomStrokes'),)))
    IInkDisp.GetBoundingBox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkBoundingBoxMode,POINTER(win32more.UI.TabletPC.IInkRectangle_head))(12, 'GetBoundingBox', ((1, 'BoundingBoxMode'),(1, 'Rectangle'),)))
    IInkDisp.DeleteStrokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head)(13, 'DeleteStrokes', ((1, 'Strokes'),)))
    IInkDisp.DeleteStroke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokeDisp_head)(14, 'DeleteStroke', ((1, 'Stroke'),)))
    IInkDisp.ExtractStrokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head,win32more.UI.TabletPC.InkExtractFlags,POINTER(win32more.UI.TabletPC.IInkDisp_head))(15, 'ExtractStrokes', ((1, 'Strokes'),(1, 'ExtractFlags'),(1, 'ExtractedInk'),)))
    IInkDisp.ExtractWithRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head,win32more.UI.TabletPC.InkExtractFlags,POINTER(win32more.UI.TabletPC.IInkDisp_head))(16, 'ExtractWithRectangle', ((1, 'Rectangle'),(1, 'extractFlags'),(1, 'ExtractedInk'),)))
    IInkDisp.Clip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head)(17, 'Clip', ((1, 'Rectangle'),)))
    IInkDisp.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDisp_head))(18, 'Clone', ((1, 'NewInk'),)))
    IInkDisp.HitTestCircle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Single,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(19, 'HitTestCircle', ((1, 'X'),(1, 'Y'),(1, 'radius'),(1, 'Strokes'),)))
    IInkDisp.HitTestWithRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head,Single,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(20, 'HitTestWithRectangle', ((1, 'SelectionRectangle'),(1, 'IntersectPercent'),(1, 'Strokes'),)))
    IInkDisp.HitTestWithLasso = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,Single,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.UI.TabletPC.IInkStrokes_head))(21, 'HitTestWithLasso', ((1, 'Points'),(1, 'IntersectPercent'),(1, 'LassoPoints'),(1, 'Strokes'),)))
    IInkDisp.NearestPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Single),POINTER(Single),POINTER(win32more.UI.TabletPC.IInkStrokeDisp_head))(22, 'NearestPoint', ((1, 'X'),(1, 'Y'),(1, 'PointOnStroke'),(1, 'DistanceFromPacket'),(1, 'Stroke'),)))
    IInkDisp.CreateStrokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(23, 'CreateStrokes', ((1, 'StrokeIds'),(1, 'Strokes'),)))
    IInkDisp.AddStrokesAtRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head,win32more.UI.TabletPC.IInkRectangle_head)(24, 'AddStrokesAtRectangle', ((1, 'SourceStrokes'),(1, 'TargetRectangle'),)))
    IInkDisp.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkPersistenceFormat,win32more.UI.TabletPC.InkPersistenceCompressionMode,POINTER(win32more.System.Com.VARIANT_head))(25, 'Save', ((1, 'PersistenceFormat'),(1, 'CompressionMode'),(1, 'Data'),)))
    IInkDisp.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(26, 'Load', ((1, 'Data'),)))
    IInkDisp.CreateStroke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,win32more.System.Com.VARIANT,POINTER(win32more.UI.TabletPC.IInkStrokeDisp_head))(27, 'CreateStroke', ((1, 'PacketData'),(1, 'PacketDescription'),(1, 'Stroke'),)))
    IInkDisp.ClipboardCopyWithRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head,win32more.UI.TabletPC.InkClipboardFormats,win32more.UI.TabletPC.InkClipboardModes,POINTER(win32more.System.Com.IDataObject_head))(28, 'ClipboardCopyWithRectangle', ((1, 'Rectangle'),(1, 'ClipboardFormats'),(1, 'ClipboardModes'),(1, 'DataObject'),)))
    IInkDisp.ClipboardCopy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head,win32more.UI.TabletPC.InkClipboardFormats,win32more.UI.TabletPC.InkClipboardModes,POINTER(win32more.System.Com.IDataObject_head))(29, 'ClipboardCopy', ((1, 'strokes'),(1, 'ClipboardFormats'),(1, 'ClipboardModes'),(1, 'DataObject'),)))
    IInkDisp.CanPaste = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,POINTER(win32more.Foundation.VARIANT_BOOL))(30, 'CanPaste', ((1, 'DataObject'),(1, 'CanPaste'),)))
    IInkDisp.ClipboardPaste = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.System.Com.IDataObject_head,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(31, 'ClipboardPaste', ((1, 'x'),(1, 'y'),(1, 'DataObject'),(1, 'Strokes'),)))
    win32more.System.Com.IDispatch
    return IInkDisp
def _define_IInkDivider_head():
    class IInkDivider(win32more.System.Com.IDispatch_head):
        Guid = Guid('5de00405-f9a4-4651-b0-c5-c3-17-de-fd-58-b9')
    return IInkDivider
def _define_IInkDivider():
    IInkDivider = win32more.UI.TabletPC.IInkDivider_head
    IInkDivider.get_Strokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(7, 'get_Strokes', ((1, 'Strokes'),)))
    IInkDivider.putref_Strokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head)(8, 'putref_Strokes', ((1, 'Strokes'),)))
    IInkDivider.get_RecognizerContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRecognizerContext_head))(9, 'get_RecognizerContext', ((1, 'RecognizerContext'),)))
    IInkDivider.putref_RecognizerContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRecognizerContext_head)(10, 'putref_RecognizerContext', ((1, 'RecognizerContext'),)))
    IInkDivider.get_LineHeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_LineHeight', ((1, 'LineHeight'),)))
    IInkDivider.put_LineHeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(12, 'put_LineHeight', ((1, 'LineHeight'),)))
    IInkDivider.Divide = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDivisionResult_head))(13, 'Divide', ((1, 'InkDivisionResult'),)))
    win32more.System.Com.IDispatch
    return IInkDivider
def _define_IInkDivisionResult_head():
    class IInkDivisionResult(win32more.System.Com.IDispatch_head):
        Guid = Guid('2dbec0a7-74c7-4b38-81-eb-aa-8e-f0-c2-49-00')
    return IInkDivisionResult
def _define_IInkDivisionResult():
    IInkDivisionResult = win32more.UI.TabletPC.IInkDivisionResult_head
    IInkDivisionResult.get_Strokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(7, 'get_Strokes', ((1, 'Strokes'),)))
    IInkDivisionResult.ResultByType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkDivisionType,POINTER(win32more.UI.TabletPC.IInkDivisionUnits_head))(8, 'ResultByType', ((1, 'divisionType'),(1, 'InkDivisionUnits'),)))
    win32more.System.Com.IDispatch
    return IInkDivisionResult
def _define_IInkDivisionUnit_head():
    class IInkDivisionUnit(win32more.System.Com.IDispatch_head):
        Guid = Guid('85aee342-48b0-4244-9d-d5-1e-d4-35-41-0f-ab')
    return IInkDivisionUnit
def _define_IInkDivisionUnit():
    IInkDivisionUnit = win32more.UI.TabletPC.IInkDivisionUnit_head
    IInkDivisionUnit.get_Strokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(7, 'get_Strokes', ((1, 'Strokes'),)))
    IInkDivisionUnit.get_DivisionType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkDivisionType))(8, 'get_DivisionType', ((1, 'divisionType'),)))
    IInkDivisionUnit.get_RecognizedString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'get_RecognizedString', ((1, 'RecoString'),)))
    IInkDivisionUnit.get_RotationTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkTransform_head))(10, 'get_RotationTransform', ((1, 'RotationTransform'),)))
    win32more.System.Com.IDispatch
    return IInkDivisionUnit
def _define_IInkDivisionUnits_head():
    class IInkDivisionUnits(win32more.System.Com.IDispatch_head):
        Guid = Guid('1bb5ddc2-31cc-4135-ab-82-2c-66-c9-f0-0c-41')
    return IInkDivisionUnits
def _define_IInkDivisionUnits():
    IInkDivisionUnits = win32more.UI.TabletPC.IInkDivisionUnits_head
    IInkDivisionUnits.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'Count'),)))
    IInkDivisionUnits.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(8, 'get__NewEnum', ((1, '_NewEnum'),)))
    IInkDivisionUnits.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.TabletPC.IInkDivisionUnit_head))(9, 'Item', ((1, 'Index'),(1, 'InkDivisionUnit'),)))
    win32more.System.Com.IDispatch
    return IInkDivisionUnits
def _define_IInkDrawingAttributes_head():
    class IInkDrawingAttributes(win32more.System.Com.IDispatch_head):
        Guid = Guid('bf519b75-0a15-4623-ad-c9-c0-0d-43-6a-80-92')
    return IInkDrawingAttributes
def _define_IInkDrawingAttributes():
    IInkDrawingAttributes = win32more.UI.TabletPC.IInkDrawingAttributes_head
    IInkDrawingAttributes.get_Color = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Color', ((1, 'CurrentColor'),)))
    IInkDrawingAttributes.put_Color = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(8, 'put_Color', ((1, 'NewColor'),)))
    IInkDrawingAttributes.get_Width = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(9, 'get_Width', ((1, 'CurrentWidth'),)))
    IInkDrawingAttributes.put_Width = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(10, 'put_Width', ((1, 'NewWidth'),)))
    IInkDrawingAttributes.get_Height = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(11, 'get_Height', ((1, 'CurrentHeight'),)))
    IInkDrawingAttributes.put_Height = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(12, 'put_Height', ((1, 'NewHeight'),)))
    IInkDrawingAttributes.get_FitToCurve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(13, 'get_FitToCurve', ((1, 'Flag'),)))
    IInkDrawingAttributes.put_FitToCurve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(14, 'put_FitToCurve', ((1, 'Flag'),)))
    IInkDrawingAttributes.get_IgnorePressure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(15, 'get_IgnorePressure', ((1, 'Flag'),)))
    IInkDrawingAttributes.put_IgnorePressure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(16, 'put_IgnorePressure', ((1, 'Flag'),)))
    IInkDrawingAttributes.get_AntiAliased = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(17, 'get_AntiAliased', ((1, 'Flag'),)))
    IInkDrawingAttributes.put_AntiAliased = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(18, 'put_AntiAliased', ((1, 'Flag'),)))
    IInkDrawingAttributes.get_Transparency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(19, 'get_Transparency', ((1, 'CurrentTransparency'),)))
    IInkDrawingAttributes.put_Transparency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(20, 'put_Transparency', ((1, 'NewTransparency'),)))
    IInkDrawingAttributes.get_RasterOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkRasterOperation))(21, 'get_RasterOperation', ((1, 'CurrentRasterOperation'),)))
    IInkDrawingAttributes.put_RasterOperation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkRasterOperation)(22, 'put_RasterOperation', ((1, 'NewRasterOperation'),)))
    IInkDrawingAttributes.get_PenTip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkPenTip))(23, 'get_PenTip', ((1, 'CurrentPenTip'),)))
    IInkDrawingAttributes.put_PenTip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkPenTip)(24, 'put_PenTip', ((1, 'NewPenTip'),)))
    IInkDrawingAttributes.get_ExtendedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkExtendedProperties_head))(25, 'get_ExtendedProperties', ((1, 'Properties'),)))
    IInkDrawingAttributes.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDrawingAttributes_head))(26, 'Clone', ((1, 'DrawingAttributes'),)))
    win32more.System.Com.IDispatch
    return IInkDrawingAttributes
def _define_IInkEdit_head():
    class IInkEdit(win32more.System.Com.IDispatch_head):
        Guid = Guid('f2127a19-fbfb-4aed-84-64-3f-36-d7-8c-fe-fb')
    return IInkEdit
def _define_IInkEdit():
    IInkEdit = win32more.UI.TabletPC.IInkEdit_head
    IInkEdit.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkEditStatus))(7, 'get_Status', ((1, 'pStatus'),)))
    IInkEdit.get_UseMouseForInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(8, 'get_UseMouseForInput', ((1, 'pVal'),)))
    IInkEdit.put_UseMouseForInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(9, 'put_UseMouseForInput', ((1, 'newVal'),)))
    IInkEdit.get_InkMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkMode))(10, 'get_InkMode', ((1, 'pVal'),)))
    IInkEdit.put_InkMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkMode)(11, 'put_InkMode', ((1, 'newVal'),)))
    IInkEdit.get_InkInsertMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkInsertMode))(12, 'get_InkInsertMode', ((1, 'pVal'),)))
    IInkEdit.put_InkInsertMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkInsertMode)(13, 'put_InkInsertMode', ((1, 'newVal'),)))
    IInkEdit.get_DrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDrawingAttributes_head))(14, 'get_DrawingAttributes', ((1, 'pVal'),)))
    IInkEdit.putref_DrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkDrawingAttributes_head)(15, 'putref_DrawingAttributes', ((1, 'newVal'),)))
    IInkEdit.get_RecognitionTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_RecognitionTimeout', ((1, 'pVal'),)))
    IInkEdit.put_RecognitionTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(17, 'put_RecognitionTimeout', ((1, 'newVal'),)))
    IInkEdit.get_Recognizer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRecognizer_head))(18, 'get_Recognizer', ((1, 'pVal'),)))
    IInkEdit.putref_Recognizer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRecognizer_head)(19, 'putref_Recognizer', ((1, 'newVal'),)))
    IInkEdit.get_Factoid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'get_Factoid', ((1, 'pVal'),)))
    IInkEdit.put_Factoid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(21, 'put_Factoid', ((1, 'newVal'),)))
    IInkEdit.get_SelInks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(22, 'get_SelInks', ((1, 'pSelInk'),)))
    IInkEdit.put_SelInks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(23, 'put_SelInks', ((1, 'SelInk'),)))
    IInkEdit.get_SelInksDisplayMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkDisplayMode))(24, 'get_SelInksDisplayMode', ((1, 'pInkDisplayMode'),)))
    IInkEdit.put_SelInksDisplayMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkDisplayMode)(25, 'put_SelInksDisplayMode', ((1, 'InkDisplayMode'),)))
    IInkEdit.Recognize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(26, 'Recognize', ()))
    IInkEdit.GetGestureStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkApplicationGesture,POINTER(win32more.Foundation.VARIANT_BOOL))(27, 'GetGestureStatus', ((1, 'Gesture'),(1, 'pListen'),)))
    IInkEdit.SetGestureStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkApplicationGesture,win32more.Foundation.VARIANT_BOOL)(28, 'SetGestureStatus', ((1, 'Gesture'),(1, 'Listen'),)))
    IInkEdit.put_BackColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(29, 'put_BackColor', ((1, 'clr'),)))
    IInkEdit.get_BackColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(30, 'get_BackColor', ((1, 'pclr'),)))
    IInkEdit.get_Appearance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.AppearanceConstants))(31, 'get_Appearance', ((1, 'pAppearance'),)))
    IInkEdit.put_Appearance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.AppearanceConstants)(32, 'put_Appearance', ((1, 'pAppearance'),)))
    IInkEdit.get_BorderStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.BorderStyleConstants))(33, 'get_BorderStyle', ((1, 'pBorderStyle'),)))
    IInkEdit.put_BorderStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.BorderStyleConstants)(34, 'put_BorderStyle', ((1, 'pBorderStyle'),)))
    IInkEdit.get_Hwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.OLE_HANDLE))(35, 'get_Hwnd', ((1, 'pohHwnd'),)))
    IInkEdit.get_Font = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IFontDisp_head))(36, 'get_Font', ((1, 'ppFont'),)))
    IInkEdit.putref_Font = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IFontDisp_head)(37, 'putref_Font', ((1, 'ppFont'),)))
    IInkEdit.get_Text = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(38, 'get_Text', ((1, 'pbstrText'),)))
    IInkEdit.put_Text = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(39, 'put_Text', ((1, 'pbstrText'),)))
    IInkEdit.get_MouseIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IPictureDisp_head))(40, 'get_MouseIcon', ((1, 'MouseIcon'),)))
    IInkEdit.put_MouseIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IPictureDisp_head)(41, 'put_MouseIcon', ((1, 'MouseIcon'),)))
    IInkEdit.putref_MouseIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IPictureDisp_head)(42, 'putref_MouseIcon', ((1, 'MouseIcon'),)))
    IInkEdit.get_MousePointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkMousePointer))(43, 'get_MousePointer', ((1, 'MousePointer'),)))
    IInkEdit.put_MousePointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkMousePointer)(44, 'put_MousePointer', ((1, 'MousePointer'),)))
    IInkEdit.get_Locked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(45, 'get_Locked', ((1, 'pVal'),)))
    IInkEdit.put_Locked = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(46, 'put_Locked', ((1, 'newVal'),)))
    IInkEdit.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(47, 'get_Enabled', ((1, 'pVal'),)))
    IInkEdit.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(48, 'put_Enabled', ((1, 'newVal'),)))
    IInkEdit.get_MaxLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(49, 'get_MaxLength', ((1, 'plMaxLength'),)))
    IInkEdit.put_MaxLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(50, 'put_MaxLength', ((1, 'lMaxLength'),)))
    IInkEdit.get_MultiLine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(51, 'get_MultiLine', ((1, 'pVal'),)))
    IInkEdit.put_MultiLine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(52, 'put_MultiLine', ((1, 'newVal'),)))
    IInkEdit.get_ScrollBars = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.ScrollBarsConstants))(53, 'get_ScrollBars', ((1, 'pVal'),)))
    IInkEdit.put_ScrollBars = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.ScrollBarsConstants)(54, 'put_ScrollBars', ((1, 'newVal'),)))
    IInkEdit.get_DisableNoScroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(55, 'get_DisableNoScroll', ((1, 'pVal'),)))
    IInkEdit.put_DisableNoScroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(56, 'put_DisableNoScroll', ((1, 'newVal'),)))
    IInkEdit.get_SelAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(57, 'get_SelAlignment', ((1, 'pvarSelAlignment'),)))
    IInkEdit.put_SelAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(58, 'put_SelAlignment', ((1, 'pvarSelAlignment'),)))
    IInkEdit.get_SelBold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(59, 'get_SelBold', ((1, 'pvarSelBold'),)))
    IInkEdit.put_SelBold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(60, 'put_SelBold', ((1, 'pvarSelBold'),)))
    IInkEdit.get_SelItalic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(61, 'get_SelItalic', ((1, 'pvarSelItalic'),)))
    IInkEdit.put_SelItalic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(62, 'put_SelItalic', ((1, 'pvarSelItalic'),)))
    IInkEdit.get_SelUnderline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(63, 'get_SelUnderline', ((1, 'pvarSelUnderline'),)))
    IInkEdit.put_SelUnderline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(64, 'put_SelUnderline', ((1, 'pvarSelUnderline'),)))
    IInkEdit.get_SelColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(65, 'get_SelColor', ((1, 'pvarSelColor'),)))
    IInkEdit.put_SelColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(66, 'put_SelColor', ((1, 'pvarSelColor'),)))
    IInkEdit.get_SelFontName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(67, 'get_SelFontName', ((1, 'pvarSelFontName'),)))
    IInkEdit.put_SelFontName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(68, 'put_SelFontName', ((1, 'pvarSelFontName'),)))
    IInkEdit.get_SelFontSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(69, 'get_SelFontSize', ((1, 'pvarSelFontSize'),)))
    IInkEdit.put_SelFontSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(70, 'put_SelFontSize', ((1, 'pvarSelFontSize'),)))
    IInkEdit.get_SelCharOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(71, 'get_SelCharOffset', ((1, 'pvarSelCharOffset'),)))
    IInkEdit.put_SelCharOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(72, 'put_SelCharOffset', ((1, 'pvarSelCharOffset'),)))
    IInkEdit.get_TextRTF = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(73, 'get_TextRTF', ((1, 'pbstrTextRTF'),)))
    IInkEdit.put_TextRTF = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(74, 'put_TextRTF', ((1, 'pbstrTextRTF'),)))
    IInkEdit.get_SelStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(75, 'get_SelStart', ((1, 'plSelStart'),)))
    IInkEdit.put_SelStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(76, 'put_SelStart', ((1, 'plSelStart'),)))
    IInkEdit.get_SelLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(77, 'get_SelLength', ((1, 'plSelLength'),)))
    IInkEdit.put_SelLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(78, 'put_SelLength', ((1, 'plSelLength'),)))
    IInkEdit.get_SelText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(79, 'get_SelText', ((1, 'pbstrSelText'),)))
    IInkEdit.put_SelText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(80, 'put_SelText', ((1, 'pbstrSelText'),)))
    IInkEdit.get_SelRTF = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(81, 'get_SelRTF', ((1, 'pbstrSelRTF'),)))
    IInkEdit.put_SelRTF = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(82, 'put_SelRTF', ((1, 'pbstrSelRTF'),)))
    IInkEdit.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(83, 'Refresh', ()))
    win32more.System.Com.IDispatch
    return IInkEdit
def _define_IInkExtendedProperties_head():
    class IInkExtendedProperties(win32more.System.Com.IDispatch_head):
        Guid = Guid('89f2a8be-95a9-4530-8b-8f-88-e9-71-e3-e2-5f')
    return IInkExtendedProperties
def _define_IInkExtendedProperties():
    IInkExtendedProperties = win32more.UI.TabletPC.IInkExtendedProperties_head
    IInkExtendedProperties.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'Count'),)))
    IInkExtendedProperties.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(8, 'get__NewEnum', ((1, '_NewEnum'),)))
    IInkExtendedProperties.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.UI.TabletPC.IInkExtendedProperty_head))(9, 'Item', ((1, 'Identifier'),(1, 'Item'),)))
    IInkExtendedProperties.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,POINTER(win32more.UI.TabletPC.IInkExtendedProperty_head))(10, 'Add', ((1, 'Guid'),(1, 'Data'),(1, 'InkExtendedProperty'),)))
    IInkExtendedProperties.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(11, 'Remove', ((1, 'Identifier'),)))
    IInkExtendedProperties.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'Clear', ()))
    IInkExtendedProperties.DoesPropertyExist = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.VARIANT_BOOL))(13, 'DoesPropertyExist', ((1, 'Guid'),(1, 'DoesPropertyExist'),)))
    win32more.System.Com.IDispatch
    return IInkExtendedProperties
def _define_IInkExtendedProperty_head():
    class IInkExtendedProperty(win32more.System.Com.IDispatch_head):
        Guid = Guid('db489209-b7c3-411d-90-f6-15-48-cf-ff-27-1e')
    return IInkExtendedProperty
def _define_IInkExtendedProperty():
    IInkExtendedProperty = win32more.UI.TabletPC.IInkExtendedProperty_head
    IInkExtendedProperty.get_Guid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Guid', ((1, 'Guid'),)))
    IInkExtendedProperty.get_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_Data', ((1, 'Data'),)))
    IInkExtendedProperty.put_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(9, 'put_Data', ((1, 'Data'),)))
    win32more.System.Com.IDispatch
    return IInkExtendedProperty
def _define_IInkGesture_head():
    class IInkGesture(win32more.System.Com.IDispatch_head):
        Guid = Guid('3bdc0a97-04e5-4e26-b8-13-18-f0-52-d4-1d-ef')
    return IInkGesture
def _define_IInkGesture():
    IInkGesture = win32more.UI.TabletPC.IInkGesture_head
    IInkGesture.get_Confidence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkRecognitionConfidence))(7, 'get_Confidence', ((1, 'Confidence'),)))
    IInkGesture.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkApplicationGesture))(8, 'get_Id', ((1, 'Id'),)))
    IInkGesture.GetHotPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32))(9, 'GetHotPoint', ((1, 'X'),(1, 'Y'),)))
    win32more.System.Com.IDispatch
    return IInkGesture
def _define_IInkLineInfo_head():
    class IInkLineInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('9c1c5ad6-f22f-4de4-b4-53-a2-cc-48-2e-7c-33')
    return IInkLineInfo
def _define_IInkLineInfo():
    IInkLineInfo = win32more.UI.TabletPC.IInkLineInfo_head
    IInkLineInfo.SetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.INKMETRIC_head))(3, 'SetFormat', ((1, 'pim'),)))
    IInkLineInfo.GetFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.INKMETRIC_head))(4, 'GetFormat', ((1, 'pim'),)))
    IInkLineInfo.GetInkExtent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.INKMETRIC_head),POINTER(UInt32))(5, 'GetInkExtent', ((1, 'pim'),(1, 'pnWidth'),)))
    IInkLineInfo.GetCandidate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),UInt32)(6, 'GetCandidate', ((1, 'nCandidateNum'),(1, 'pwcRecogWord'),(1, 'pcwcRecogWord'),(1, 'dwFlags'),)))
    IInkLineInfo.SetCandidate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR)(7, 'SetCandidate', ((1, 'nCandidateNum'),(1, 'strRecogWord'),)))
    IInkLineInfo.Recognize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Recognize', ()))
    win32more.System.Com.IUnknown
    return IInkLineInfo
def _define_IInkOverlay_head():
    class IInkOverlay(win32more.System.Com.IDispatch_head):
        Guid = Guid('b82a463b-c1c5-45a3-99-7c-de-ab-56-51-b6-7a')
    return IInkOverlay
def _define_IInkOverlay():
    IInkOverlay = win32more.UI.TabletPC.IInkOverlay_head
    IInkOverlay.get_hWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(IntPtr))(7, 'get_hWnd', ((1, 'CurrentWindow'),)))
    IInkOverlay.put_hWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr)(8, 'put_hWnd', ((1, 'NewWindow'),)))
    IInkOverlay.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'get_Enabled', ((1, 'Collecting'),)))
    IInkOverlay.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(10, 'put_Enabled', ((1, 'Collecting'),)))
    IInkOverlay.get_DefaultDrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDrawingAttributes_head))(11, 'get_DefaultDrawingAttributes', ((1, 'CurrentAttributes'),)))
    IInkOverlay.putref_DefaultDrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkDrawingAttributes_head)(12, 'putref_DefaultDrawingAttributes', ((1, 'NewAttributes'),)))
    IInkOverlay.get_Renderer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRenderer_head))(13, 'get_Renderer', ((1, 'CurrentInkRenderer'),)))
    IInkOverlay.putref_Renderer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRenderer_head)(14, 'putref_Renderer', ((1, 'NewInkRenderer'),)))
    IInkOverlay.get_Ink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDisp_head))(15, 'get_Ink', ((1, 'Ink'),)))
    IInkOverlay.putref_Ink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkDisp_head)(16, 'putref_Ink', ((1, 'NewInk'),)))
    IInkOverlay.get_AutoRedraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(17, 'get_AutoRedraw', ((1, 'AutoRedraw'),)))
    IInkOverlay.put_AutoRedraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(18, 'put_AutoRedraw', ((1, 'AutoRedraw'),)))
    IInkOverlay.get_CollectingInk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(19, 'get_CollectingInk', ((1, 'Collecting'),)))
    IInkOverlay.get_CollectionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkCollectionMode))(20, 'get_CollectionMode', ((1, 'Mode'),)))
    IInkOverlay.put_CollectionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkCollectionMode)(21, 'put_CollectionMode', ((1, 'Mode'),)))
    IInkOverlay.get_DynamicRendering = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(22, 'get_DynamicRendering', ((1, 'Enabled'),)))
    IInkOverlay.put_DynamicRendering = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(23, 'put_DynamicRendering', ((1, 'Enabled'),)))
    IInkOverlay.get_DesiredPacketDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(24, 'get_DesiredPacketDescription', ((1, 'PacketGuids'),)))
    IInkOverlay.put_DesiredPacketDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(25, 'put_DesiredPacketDescription', ((1, 'PacketGuids'),)))
    IInkOverlay.get_MouseIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IPictureDisp_head))(26, 'get_MouseIcon', ((1, 'MouseIcon'),)))
    IInkOverlay.put_MouseIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IPictureDisp_head)(27, 'put_MouseIcon', ((1, 'MouseIcon'),)))
    IInkOverlay.putref_MouseIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IPictureDisp_head)(28, 'putref_MouseIcon', ((1, 'MouseIcon'),)))
    IInkOverlay.get_MousePointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkMousePointer))(29, 'get_MousePointer', ((1, 'MousePointer'),)))
    IInkOverlay.put_MousePointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkMousePointer)(30, 'put_MousePointer', ((1, 'MousePointer'),)))
    IInkOverlay.get_EditingMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkOverlayEditingMode))(31, 'get_EditingMode', ((1, 'EditingMode'),)))
    IInkOverlay.put_EditingMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkOverlayEditingMode)(32, 'put_EditingMode', ((1, 'EditingMode'),)))
    IInkOverlay.get_Selection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(33, 'get_Selection', ((1, 'Selection'),)))
    IInkOverlay.put_Selection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head)(34, 'put_Selection', ((1, 'Selection'),)))
    IInkOverlay.get_EraserMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkOverlayEraserMode))(35, 'get_EraserMode', ((1, 'EraserMode'),)))
    IInkOverlay.put_EraserMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkOverlayEraserMode)(36, 'put_EraserMode', ((1, 'EraserMode'),)))
    IInkOverlay.get_EraserWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(37, 'get_EraserWidth', ((1, 'EraserWidth'),)))
    IInkOverlay.put_EraserWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(38, 'put_EraserWidth', ((1, 'newEraserWidth'),)))
    IInkOverlay.get_AttachMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkOverlayAttachMode))(39, 'get_AttachMode', ((1, 'AttachMode'),)))
    IInkOverlay.put_AttachMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkOverlayAttachMode)(40, 'put_AttachMode', ((1, 'AttachMode'),)))
    IInkOverlay.get_Cursors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkCursors_head))(41, 'get_Cursors', ((1, 'Cursors'),)))
    IInkOverlay.get_MarginX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(42, 'get_MarginX', ((1, 'MarginX'),)))
    IInkOverlay.put_MarginX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(43, 'put_MarginX', ((1, 'MarginX'),)))
    IInkOverlay.get_MarginY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(44, 'get_MarginY', ((1, 'MarginY'),)))
    IInkOverlay.put_MarginY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(45, 'put_MarginY', ((1, 'MarginY'),)))
    IInkOverlay.get_Tablet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkTablet_head))(46, 'get_Tablet', ((1, 'SingleTablet'),)))
    IInkOverlay.get_SupportHighContrastInk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(47, 'get_SupportHighContrastInk', ((1, 'Support'),)))
    IInkOverlay.put_SupportHighContrastInk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(48, 'put_SupportHighContrastInk', ((1, 'Support'),)))
    IInkOverlay.get_SupportHighContrastSelectionUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(49, 'get_SupportHighContrastSelectionUI', ((1, 'Support'),)))
    IInkOverlay.put_SupportHighContrastSelectionUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(50, 'put_SupportHighContrastSelectionUI', ((1, 'Support'),)))
    IInkOverlay.HitTestSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.TabletPC.SelectionHitResult))(51, 'HitTestSelection', ((1, 'x'),(1, 'y'),(1, 'SelArea'),)))
    IInkOverlay.Draw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head)(52, 'Draw', ((1, 'Rect'),)))
    IInkOverlay.SetGestureStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkApplicationGesture,win32more.Foundation.VARIANT_BOOL)(53, 'SetGestureStatus', ((1, 'Gesture'),(1, 'Listen'),)))
    IInkOverlay.GetGestureStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkApplicationGesture,POINTER(win32more.Foundation.VARIANT_BOOL))(54, 'GetGestureStatus', ((1, 'Gesture'),(1, 'Listening'),)))
    IInkOverlay.GetWindowInputRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRectangle_head))(55, 'GetWindowInputRectangle', ((1, 'WindowInputRectangle'),)))
    IInkOverlay.SetWindowInputRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head)(56, 'SetWindowInputRectangle', ((1, 'WindowInputRectangle'),)))
    IInkOverlay.SetAllTabletsMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(57, 'SetAllTabletsMode', ((1, 'UseMouseForInput'),)))
    IInkOverlay.SetSingleTabletIntegratedMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkTablet_head)(58, 'SetSingleTabletIntegratedMode', ((1, 'Tablet'),)))
    IInkOverlay.GetEventInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkCollectorEventInterest,POINTER(win32more.Foundation.VARIANT_BOOL))(59, 'GetEventInterest', ((1, 'EventId'),(1, 'Listen'),)))
    IInkOverlay.SetEventInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkCollectorEventInterest,win32more.Foundation.VARIANT_BOOL)(60, 'SetEventInterest', ((1, 'EventId'),(1, 'Listen'),)))
    win32more.System.Com.IDispatch
    return IInkOverlay
def _define_IInkPicture_head():
    class IInkPicture(win32more.System.Com.IDispatch_head):
        Guid = Guid('e85662e0-379a-40d7-9b-5c-75-7d-23-3f-99-23')
    return IInkPicture
def _define_IInkPicture():
    IInkPicture = win32more.UI.TabletPC.IInkPicture_head
    IInkPicture.get_hWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(IntPtr))(7, 'get_hWnd', ((1, 'CurrentWindow'),)))
    IInkPicture.get_DefaultDrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDrawingAttributes_head))(8, 'get_DefaultDrawingAttributes', ((1, 'CurrentAttributes'),)))
    IInkPicture.putref_DefaultDrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkDrawingAttributes_head)(9, 'putref_DefaultDrawingAttributes', ((1, 'NewAttributes'),)))
    IInkPicture.get_Renderer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRenderer_head))(10, 'get_Renderer', ((1, 'CurrentInkRenderer'),)))
    IInkPicture.putref_Renderer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRenderer_head)(11, 'putref_Renderer', ((1, 'NewInkRenderer'),)))
    IInkPicture.get_Ink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDisp_head))(12, 'get_Ink', ((1, 'Ink'),)))
    IInkPicture.putref_Ink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkDisp_head)(13, 'putref_Ink', ((1, 'NewInk'),)))
    IInkPicture.get_AutoRedraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(14, 'get_AutoRedraw', ((1, 'AutoRedraw'),)))
    IInkPicture.put_AutoRedraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(15, 'put_AutoRedraw', ((1, 'AutoRedraw'),)))
    IInkPicture.get_CollectingInk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(16, 'get_CollectingInk', ((1, 'Collecting'),)))
    IInkPicture.get_CollectionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkCollectionMode))(17, 'get_CollectionMode', ((1, 'Mode'),)))
    IInkPicture.put_CollectionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkCollectionMode)(18, 'put_CollectionMode', ((1, 'Mode'),)))
    IInkPicture.get_DynamicRendering = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(19, 'get_DynamicRendering', ((1, 'Enabled'),)))
    IInkPicture.put_DynamicRendering = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(20, 'put_DynamicRendering', ((1, 'Enabled'),)))
    IInkPicture.get_DesiredPacketDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(21, 'get_DesiredPacketDescription', ((1, 'PacketGuids'),)))
    IInkPicture.put_DesiredPacketDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(22, 'put_DesiredPacketDescription', ((1, 'PacketGuids'),)))
    IInkPicture.get_MouseIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IPictureDisp_head))(23, 'get_MouseIcon', ((1, 'MouseIcon'),)))
    IInkPicture.put_MouseIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IPictureDisp_head)(24, 'put_MouseIcon', ((1, 'MouseIcon'),)))
    IInkPicture.putref_MouseIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IPictureDisp_head)(25, 'putref_MouseIcon', ((1, 'MouseIcon'),)))
    IInkPicture.get_MousePointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkMousePointer))(26, 'get_MousePointer', ((1, 'MousePointer'),)))
    IInkPicture.put_MousePointer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkMousePointer)(27, 'put_MousePointer', ((1, 'MousePointer'),)))
    IInkPicture.get_EditingMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkOverlayEditingMode))(28, 'get_EditingMode', ((1, 'EditingMode'),)))
    IInkPicture.put_EditingMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkOverlayEditingMode)(29, 'put_EditingMode', ((1, 'EditingMode'),)))
    IInkPicture.get_Selection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(30, 'get_Selection', ((1, 'Selection'),)))
    IInkPicture.put_Selection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head)(31, 'put_Selection', ((1, 'Selection'),)))
    IInkPicture.get_EraserMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkOverlayEraserMode))(32, 'get_EraserMode', ((1, 'EraserMode'),)))
    IInkPicture.put_EraserMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkOverlayEraserMode)(33, 'put_EraserMode', ((1, 'EraserMode'),)))
    IInkPicture.get_EraserWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(34, 'get_EraserWidth', ((1, 'EraserWidth'),)))
    IInkPicture.put_EraserWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(35, 'put_EraserWidth', ((1, 'newEraserWidth'),)))
    IInkPicture.putref_Picture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IPictureDisp_head)(36, 'putref_Picture', ((1, 'pPicture'),)))
    IInkPicture.put_Picture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IPictureDisp_head)(37, 'put_Picture', ((1, 'pPicture'),)))
    IInkPicture.get_Picture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IPictureDisp_head))(38, 'get_Picture', ((1, 'ppPicture'),)))
    IInkPicture.put_SizeMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkPictureSizeMode)(39, 'put_SizeMode', ((1, 'smNewSizeMode'),)))
    IInkPicture.get_SizeMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkPictureSizeMode))(40, 'get_SizeMode', ((1, 'smSizeMode'),)))
    IInkPicture.put_BackColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(41, 'put_BackColor', ((1, 'newColor'),)))
    IInkPicture.get_BackColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(42, 'get_BackColor', ((1, 'pColor'),)))
    IInkPicture.get_Cursors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkCursors_head))(43, 'get_Cursors', ((1, 'Cursors'),)))
    IInkPicture.get_MarginX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(44, 'get_MarginX', ((1, 'MarginX'),)))
    IInkPicture.put_MarginX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(45, 'put_MarginX', ((1, 'MarginX'),)))
    IInkPicture.get_MarginY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(46, 'get_MarginY', ((1, 'MarginY'),)))
    IInkPicture.put_MarginY = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(47, 'put_MarginY', ((1, 'MarginY'),)))
    IInkPicture.get_Tablet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkTablet_head))(48, 'get_Tablet', ((1, 'SingleTablet'),)))
    IInkPicture.get_SupportHighContrastInk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(49, 'get_SupportHighContrastInk', ((1, 'Support'),)))
    IInkPicture.put_SupportHighContrastInk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(50, 'put_SupportHighContrastInk', ((1, 'Support'),)))
    IInkPicture.get_SupportHighContrastSelectionUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(51, 'get_SupportHighContrastSelectionUI', ((1, 'Support'),)))
    IInkPicture.put_SupportHighContrastSelectionUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(52, 'put_SupportHighContrastSelectionUI', ((1, 'Support'),)))
    IInkPicture.HitTestSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.TabletPC.SelectionHitResult))(53, 'HitTestSelection', ((1, 'x'),(1, 'y'),(1, 'SelArea'),)))
    IInkPicture.SetGestureStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkApplicationGesture,win32more.Foundation.VARIANT_BOOL)(54, 'SetGestureStatus', ((1, 'Gesture'),(1, 'Listen'),)))
    IInkPicture.GetGestureStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkApplicationGesture,POINTER(win32more.Foundation.VARIANT_BOOL))(55, 'GetGestureStatus', ((1, 'Gesture'),(1, 'Listening'),)))
    IInkPicture.GetWindowInputRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRectangle_head))(56, 'GetWindowInputRectangle', ((1, 'WindowInputRectangle'),)))
    IInkPicture.SetWindowInputRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head)(57, 'SetWindowInputRectangle', ((1, 'WindowInputRectangle'),)))
    IInkPicture.SetAllTabletsMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(58, 'SetAllTabletsMode', ((1, 'UseMouseForInput'),)))
    IInkPicture.SetSingleTabletIntegratedMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkTablet_head)(59, 'SetSingleTabletIntegratedMode', ((1, 'Tablet'),)))
    IInkPicture.GetEventInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkCollectorEventInterest,POINTER(win32more.Foundation.VARIANT_BOOL))(60, 'GetEventInterest', ((1, 'EventId'),(1, 'Listen'),)))
    IInkPicture.SetEventInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkCollectorEventInterest,win32more.Foundation.VARIANT_BOOL)(61, 'SetEventInterest', ((1, 'EventId'),(1, 'Listen'),)))
    IInkPicture.get_InkEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(62, 'get_InkEnabled', ((1, 'Collecting'),)))
    IInkPicture.put_InkEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(63, 'put_InkEnabled', ((1, 'Collecting'),)))
    IInkPicture.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(64, 'get_Enabled', ((1, 'pbool'),)))
    IInkPicture.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(65, 'put_Enabled', ((1, 'vbool'),)))
    win32more.System.Com.IDispatch
    return IInkPicture
def _define_IInkRecognitionAlternate_head():
    class IInkRecognitionAlternate(win32more.System.Com.IDispatch_head):
        Guid = Guid('b7e660ad-77e4-429b-ad-da-87-37-80-d1-fc-4a')
    return IInkRecognitionAlternate
def _define_IInkRecognitionAlternate():
    IInkRecognitionAlternate = win32more.UI.TabletPC.IInkRecognitionAlternate_head
    IInkRecognitionAlternate.get_String = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_String', ((1, 'RecoString'),)))
    IInkRecognitionAlternate.get_Confidence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkRecognitionConfidence))(8, 'get_Confidence', ((1, 'Confidence'),)))
    IInkRecognitionAlternate.get_Baseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(9, 'get_Baseline', ((1, 'Baseline'),)))
    IInkRecognitionAlternate.get_Midline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(10, 'get_Midline', ((1, 'Midline'),)))
    IInkRecognitionAlternate.get_Ascender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(11, 'get_Ascender', ((1, 'Ascender'),)))
    IInkRecognitionAlternate.get_Descender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(12, 'get_Descender', ((1, 'Descender'),)))
    IInkRecognitionAlternate.get_LineNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_LineNumber', ((1, 'LineNumber'),)))
    IInkRecognitionAlternate.get_Strokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(14, 'get_Strokes', ((1, 'Strokes'),)))
    IInkRecognitionAlternate.get_LineAlternates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRecognitionAlternates_head))(15, 'get_LineAlternates', ((1, 'LineAlternates'),)))
    IInkRecognitionAlternate.get_ConfidenceAlternates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRecognitionAlternates_head))(16, 'get_ConfidenceAlternates', ((1, 'ConfidenceAlternates'),)))
    IInkRecognitionAlternate.GetStrokesFromStrokeRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(17, 'GetStrokesFromStrokeRanges', ((1, 'Strokes'),(1, 'GetStrokesFromStrokeRanges'),)))
    IInkRecognitionAlternate.GetStrokesFromTextRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32),POINTER(win32more.UI.TabletPC.IInkStrokes_head))(18, 'GetStrokesFromTextRange', ((1, 'selectionStart'),(1, 'selectionLength'),(1, 'GetStrokesFromTextRange'),)))
    IInkRecognitionAlternate.GetTextRangeFromStrokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head,POINTER(Int32),POINTER(Int32))(19, 'GetTextRangeFromStrokes', ((1, 'Strokes'),(1, 'selectionStart'),(1, 'selectionLength'),)))
    IInkRecognitionAlternate.AlternatesWithConstantPropertyValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.UI.TabletPC.IInkRecognitionAlternates_head))(20, 'AlternatesWithConstantPropertyValues', ((1, 'PropertyType'),(1, 'AlternatesWithConstantPropertyValues'),)))
    IInkRecognitionAlternate.GetPropertyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head))(21, 'GetPropertyValue', ((1, 'PropertyType'),(1, 'PropertyValue'),)))
    win32more.System.Com.IDispatch
    return IInkRecognitionAlternate
def _define_IInkRecognitionAlternates_head():
    class IInkRecognitionAlternates(win32more.System.Com.IDispatch_head):
        Guid = Guid('286a167f-9f19-4c61-9d-53-4f-07-be-62-2b-84')
    return IInkRecognitionAlternates
def _define_IInkRecognitionAlternates():
    IInkRecognitionAlternates = win32more.UI.TabletPC.IInkRecognitionAlternates_head
    IInkRecognitionAlternates.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'Count'),)))
    IInkRecognitionAlternates.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(8, 'get__NewEnum', ((1, '_NewEnum'),)))
    IInkRecognitionAlternates.get_Strokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(9, 'get_Strokes', ((1, 'Strokes'),)))
    IInkRecognitionAlternates.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.TabletPC.IInkRecognitionAlternate_head))(10, 'Item', ((1, 'Index'),(1, 'InkRecoAlternate'),)))
    win32more.System.Com.IDispatch
    return IInkRecognitionAlternates
def _define_IInkRecognitionResult_head():
    class IInkRecognitionResult(win32more.System.Com.IDispatch_head):
        Guid = Guid('3bc129a8-86cd-45ad-bd-e8-e0-d3-2d-61-c1-6d')
    return IInkRecognitionResult
def _define_IInkRecognitionResult():
    IInkRecognitionResult = win32more.UI.TabletPC.IInkRecognitionResult_head
    IInkRecognitionResult.get_TopString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_TopString', ((1, 'TopString'),)))
    IInkRecognitionResult.get_TopAlternate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRecognitionAlternate_head))(8, 'get_TopAlternate', ((1, 'TopAlternate'),)))
    IInkRecognitionResult.get_TopConfidence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkRecognitionConfidence))(9, 'get_TopConfidence', ((1, 'TopConfidence'),)))
    IInkRecognitionResult.get_Strokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(10, 'get_Strokes', ((1, 'Strokes'),)))
    IInkRecognitionResult.AlternatesFromSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,POINTER(win32more.UI.TabletPC.IInkRecognitionAlternates_head))(11, 'AlternatesFromSelection', ((1, 'selectionStart'),(1, 'selectionLength'),(1, 'maximumAlternates'),(1, 'AlternatesFromSelection'),)))
    IInkRecognitionResult.ModifyTopAlternate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRecognitionAlternate_head)(12, 'ModifyTopAlternate', ((1, 'Alternate'),)))
    IInkRecognitionResult.SetResultOnStrokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(13, 'SetResultOnStrokes', ()))
    win32more.System.Com.IDispatch
    return IInkRecognitionResult
def _define_IInkRecognizer_head():
    class IInkRecognizer(win32more.System.Com.IDispatch_head):
        Guid = Guid('782bf7cf-034b-4396-8a-32-3a-18-33-cf-6b-56')
    return IInkRecognizer
def _define_IInkRecognizer():
    IInkRecognizer = win32more.UI.TabletPC.IInkRecognizer_head
    IInkRecognizer.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'Name'),)))
    IInkRecognizer.get_Vendor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Vendor', ((1, 'Vendor'),)))
    IInkRecognizer.get_Capabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkRecognizerCapabilities))(9, 'get_Capabilities', ((1, 'CapabilitiesFlags'),)))
    IInkRecognizer.get_Languages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(10, 'get_Languages', ((1, 'Languages'),)))
    IInkRecognizer.get_SupportedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(11, 'get_SupportedProperties', ((1, 'SupportedProperties'),)))
    IInkRecognizer.get_PreferredPacketDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(12, 'get_PreferredPacketDescription', ((1, 'PreferredPacketDescription'),)))
    IInkRecognizer.CreateRecognizerContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRecognizerContext_head))(13, 'CreateRecognizerContext', ((1, 'Context'),)))
    win32more.System.Com.IDispatch
    return IInkRecognizer
def _define_IInkRecognizer2_head():
    class IInkRecognizer2(win32more.System.Com.IDispatch_head):
        Guid = Guid('6110118a-3a75-4ad6-b2-aa-04-b2-b7-2b-be-65')
    return IInkRecognizer2
def _define_IInkRecognizer2():
    IInkRecognizer2 = win32more.UI.TabletPC.IInkRecognizer2_head
    IInkRecognizer2.get_Id = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Id', ((1, 'pbstrId'),)))
    IInkRecognizer2.get_UnicodeRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_UnicodeRanges', ((1, 'UnicodeRanges'),)))
    win32more.System.Com.IDispatch
    return IInkRecognizer2
def _define_IInkRecognizerContext_head():
    class IInkRecognizerContext(win32more.System.Com.IDispatch_head):
        Guid = Guid('c68f52f9-32a3-4625-90-6c-44-fc-23-b4-09-58')
    return IInkRecognizerContext
def _define_IInkRecognizerContext():
    IInkRecognizerContext = win32more.UI.TabletPC.IInkRecognizerContext_head
    IInkRecognizerContext.get_Strokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkStrokes_head))(7, 'get_Strokes', ((1, 'Strokes'),)))
    IInkRecognizerContext.putref_Strokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head)(8, 'putref_Strokes', ((1, 'Strokes'),)))
    IInkRecognizerContext.get_CharacterAutoCompletionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkRecognizerCharacterAutoCompletionMode))(9, 'get_CharacterAutoCompletionMode', ((1, 'Mode'),)))
    IInkRecognizerContext.put_CharacterAutoCompletionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkRecognizerCharacterAutoCompletionMode)(10, 'put_CharacterAutoCompletionMode', ((1, 'Mode'),)))
    IInkRecognizerContext.get_Factoid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'get_Factoid', ((1, 'Factoid'),)))
    IInkRecognizerContext.put_Factoid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'put_Factoid', ((1, 'factoid'),)))
    IInkRecognizerContext.get_Guide = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRecognizerGuide_head))(13, 'get_Guide', ((1, 'RecognizerGuide'),)))
    IInkRecognizerContext.putref_Guide = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRecognizerGuide_head)(14, 'putref_Guide', ((1, 'RecognizerGuide'),)))
    IInkRecognizerContext.get_PrefixText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'get_PrefixText', ((1, 'Prefix'),)))
    IInkRecognizerContext.put_PrefixText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(16, 'put_PrefixText', ((1, 'Prefix'),)))
    IInkRecognizerContext.get_SuffixText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(17, 'get_SuffixText', ((1, 'Suffix'),)))
    IInkRecognizerContext.put_SuffixText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(18, 'put_SuffixText', ((1, 'Suffix'),)))
    IInkRecognizerContext.get_RecognitionFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkRecognitionModes))(19, 'get_RecognitionFlags', ((1, 'Modes'),)))
    IInkRecognizerContext.put_RecognitionFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkRecognitionModes)(20, 'put_RecognitionFlags', ((1, 'Modes'),)))
    IInkRecognizerContext.get_WordList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkWordList_head))(21, 'get_WordList', ((1, 'WordList'),)))
    IInkRecognizerContext.putref_WordList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkWordList_head)(22, 'putref_WordList', ((1, 'WordList'),)))
    IInkRecognizerContext.get_Recognizer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRecognizer_head))(23, 'get_Recognizer', ((1, 'Recognizer'),)))
    IInkRecognizerContext.Recognize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkRecognitionStatus),POINTER(win32more.UI.TabletPC.IInkRecognitionResult_head))(24, 'Recognize', ((1, 'RecognitionStatus'),(1, 'RecognitionResult'),)))
    IInkRecognizerContext.StopBackgroundRecognition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(25, 'StopBackgroundRecognition', ()))
    IInkRecognizerContext.EndInkInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(26, 'EndInkInput', ()))
    IInkRecognizerContext.BackgroundRecognize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(27, 'BackgroundRecognize', ((1, 'CustomData'),)))
    IInkRecognizerContext.BackgroundRecognizeWithAlternates = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(28, 'BackgroundRecognizeWithAlternates', ((1, 'CustomData'),)))
    IInkRecognizerContext.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRecognizerContext_head))(29, 'Clone', ((1, 'RecoContext'),)))
    IInkRecognizerContext.IsStringSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.VARIANT_BOOL))(30, 'IsStringSupported', ((1, 'String'),(1, 'Supported'),)))
    win32more.System.Com.IDispatch
    return IInkRecognizerContext
def _define_IInkRecognizerContext2_head():
    class IInkRecognizerContext2(win32more.System.Com.IDispatch_head):
        Guid = Guid('d6f0e32f-73d8-408e-8e-9f-5f-ea-59-2c-36-3f')
    return IInkRecognizerContext2
def _define_IInkRecognizerContext2():
    IInkRecognizerContext2 = win32more.UI.TabletPC.IInkRecognizerContext2_head
    IInkRecognizerContext2.get_EnabledUnicodeRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(7, 'get_EnabledUnicodeRanges', ((1, 'UnicodeRanges'),)))
    IInkRecognizerContext2.put_EnabledUnicodeRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT)(8, 'put_EnabledUnicodeRanges', ((1, 'UnicodeRanges'),)))
    win32more.System.Com.IDispatch
    return IInkRecognizerContext2
def _define_IInkRecognizerGuide_head():
    class IInkRecognizerGuide(win32more.System.Com.IDispatch_head):
        Guid = Guid('d934be07-7b84-4208-91-36-83-c2-09-94-e9-05')
    return IInkRecognizerGuide
def _define_IInkRecognizerGuide():
    IInkRecognizerGuide = win32more.UI.TabletPC.IInkRecognizerGuide_head
    IInkRecognizerGuide.get_WritingBox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRectangle_head))(7, 'get_WritingBox', ((1, 'Rectangle'),)))
    IInkRecognizerGuide.put_WritingBox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head)(8, 'put_WritingBox', ((1, 'Rectangle'),)))
    IInkRecognizerGuide.get_DrawnBox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRectangle_head))(9, 'get_DrawnBox', ((1, 'Rectangle'),)))
    IInkRecognizerGuide.put_DrawnBox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head)(10, 'put_DrawnBox', ((1, 'Rectangle'),)))
    IInkRecognizerGuide.get_Rows = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_Rows', ((1, 'Units'),)))
    IInkRecognizerGuide.put_Rows = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(12, 'put_Rows', ((1, 'Units'),)))
    IInkRecognizerGuide.get_Columns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_Columns', ((1, 'Units'),)))
    IInkRecognizerGuide.put_Columns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(14, 'put_Columns', ((1, 'Units'),)))
    IInkRecognizerGuide.get_Midline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(15, 'get_Midline', ((1, 'Units'),)))
    IInkRecognizerGuide.put_Midline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(16, 'put_Midline', ((1, 'Units'),)))
    IInkRecognizerGuide.get_GuideData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InkRecoGuide_head))(17, 'get_GuideData', ((1, 'pRecoGuide'),)))
    IInkRecognizerGuide.put_GuideData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkRecoGuide)(18, 'put_GuideData', ((1, 'recoGuide'),)))
    win32more.System.Com.IDispatch
    return IInkRecognizerGuide
def _define_IInkRecognizers_head():
    class IInkRecognizers(win32more.System.Com.IDispatch_head):
        Guid = Guid('9ccc4f12-b0b7-4a8b-bf-58-4a-ec-a4-e8-ce-fd')
    return IInkRecognizers
def _define_IInkRecognizers():
    IInkRecognizers = win32more.UI.TabletPC.IInkRecognizers_head
    IInkRecognizers.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'Count'),)))
    IInkRecognizers.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(8, 'get__NewEnum', ((1, '_NewEnum'),)))
    IInkRecognizers.GetDefaultRecognizer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.TabletPC.IInkRecognizer_head))(9, 'GetDefaultRecognizer', ((1, 'lcid'),(1, 'DefaultRecognizer'),)))
    IInkRecognizers.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.TabletPC.IInkRecognizer_head))(10, 'Item', ((1, 'Index'),(1, 'InkRecognizer'),)))
    win32more.System.Com.IDispatch
    return IInkRecognizers
def _define_IInkRectangle_head():
    class IInkRectangle(win32more.System.Com.IDispatch_head):
        Guid = Guid('9794ff82-6071-4717-8a-8b-6a-c7-c6-4a-68-6e')
    return IInkRectangle
def _define_IInkRectangle():
    IInkRectangle = win32more.UI.TabletPC.IInkRectangle_head
    IInkRectangle.get_Top = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Top', ((1, 'Units'),)))
    IInkRectangle.put_Top = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(8, 'put_Top', ((1, 'Units'),)))
    IInkRectangle.get_Left = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(9, 'get_Left', ((1, 'Units'),)))
    IInkRectangle.put_Left = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(10, 'put_Left', ((1, 'Units'),)))
    IInkRectangle.get_Bottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(11, 'get_Bottom', ((1, 'Units'),)))
    IInkRectangle.put_Bottom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(12, 'put_Bottom', ((1, 'Units'),)))
    IInkRectangle.get_Right = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(13, 'get_Right', ((1, 'Units'),)))
    IInkRectangle.put_Right = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(14, 'put_Right', ((1, 'Units'),)))
    IInkRectangle.get_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(15, 'get_Data', ((1, 'Rect'),)))
    IInkRectangle.put_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.RECT)(16, 'put_Data', ((1, 'Rect'),)))
    IInkRectangle.GetRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32))(17, 'GetRectangle', ((1, 'Top'),(1, 'Left'),(1, 'Bottom'),(1, 'Right'),)))
    IInkRectangle.SetRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,Int32)(18, 'SetRectangle', ((1, 'Top'),(1, 'Left'),(1, 'Bottom'),(1, 'Right'),)))
    win32more.System.Com.IDispatch
    return IInkRectangle
def _define_IInkRenderer_head():
    class IInkRenderer(win32more.System.Com.IDispatch_head):
        Guid = Guid('e6257a9c-b511-4f4c-a8-b0-a7-db-c9-50-6b-83')
    return IInkRenderer
def _define_IInkRenderer():
    IInkRenderer = win32more.UI.TabletPC.IInkRenderer_head
    IInkRenderer.GetViewTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkTransform_head)(7, 'GetViewTransform', ((1, 'ViewTransform'),)))
    IInkRenderer.SetViewTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkTransform_head)(8, 'SetViewTransform', ((1, 'ViewTransform'),)))
    IInkRenderer.GetObjectTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkTransform_head)(9, 'GetObjectTransform', ((1, 'ObjectTransform'),)))
    IInkRenderer.SetObjectTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkTransform_head)(10, 'SetObjectTransform', ((1, 'ObjectTransform'),)))
    IInkRenderer.Draw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,win32more.UI.TabletPC.IInkStrokes_head)(11, 'Draw', ((1, 'hDC'),(1, 'Strokes'),)))
    IInkRenderer.DrawStroke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,win32more.UI.TabletPC.IInkStrokeDisp_head,win32more.UI.TabletPC.IInkDrawingAttributes_head)(12, 'DrawStroke', ((1, 'hDC'),(1, 'Stroke'),(1, 'DrawingAttributes'),)))
    IInkRenderer.PixelToInkSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(Int32),POINTER(Int32))(13, 'PixelToInkSpace', ((1, 'hDC'),(1, 'x'),(1, 'y'),)))
    IInkRenderer.InkSpaceToPixel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(Int32),POINTER(Int32))(14, 'InkSpaceToPixel', ((1, 'hdcDisplay'),(1, 'x'),(1, 'y'),)))
    IInkRenderer.PixelToInkSpaceFromPoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(win32more.System.Com.VARIANT_head))(15, 'PixelToInkSpaceFromPoints', ((1, 'hDC'),(1, 'Points'),)))
    IInkRenderer.InkSpaceToPixelFromPoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,POINTER(win32more.System.Com.VARIANT_head))(16, 'InkSpaceToPixelFromPoints', ((1, 'hDC'),(1, 'Points'),)))
    IInkRenderer.Measure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head,POINTER(win32more.UI.TabletPC.IInkRectangle_head))(17, 'Measure', ((1, 'Strokes'),(1, 'Rectangle'),)))
    IInkRenderer.MeasureStroke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokeDisp_head,win32more.UI.TabletPC.IInkDrawingAttributes_head,POINTER(win32more.UI.TabletPC.IInkRectangle_head))(18, 'MeasureStroke', ((1, 'Stroke'),(1, 'DrawingAttributes'),(1, 'Rectangle'),)))
    IInkRenderer.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single)(19, 'Move', ((1, 'HorizontalComponent'),(1, 'VerticalComponent'),)))
    IInkRenderer.Rotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single)(20, 'Rotate', ((1, 'Degrees'),(1, 'x'),(1, 'y'),)))
    IInkRenderer.ScaleTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,win32more.Foundation.VARIANT_BOOL)(21, 'ScaleTransform', ((1, 'HorizontalMultiplier'),(1, 'VerticalMultiplier'),(1, 'ApplyOnPenWidth'),)))
    win32more.System.Com.IDispatch
    return IInkRenderer
def _define_IInkStrokeDisp_head():
    class IInkStrokeDisp(win32more.System.Com.IDispatch_head):
        Guid = Guid('43242fea-91d1-4a72-96-3e-fb-b9-18-29-cf-a2')
    return IInkStrokeDisp
def _define_IInkStrokeDisp():
    IInkStrokeDisp = win32more.UI.TabletPC.IInkStrokeDisp_head
    IInkStrokeDisp.get_ID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_ID', ((1, 'ID'),)))
    IInkStrokeDisp.get_BezierPoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(8, 'get_BezierPoints', ((1, 'Points'),)))
    IInkStrokeDisp.get_DrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDrawingAttributes_head))(9, 'get_DrawingAttributes', ((1, 'DrawAttrs'),)))
    IInkStrokeDisp.putref_DrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkDrawingAttributes_head)(10, 'putref_DrawingAttributes', ((1, 'DrawAttrs'),)))
    IInkStrokeDisp.get_Ink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDisp_head))(11, 'get_Ink', ((1, 'Ink'),)))
    IInkStrokeDisp.get_ExtendedProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkExtendedProperties_head))(12, 'get_ExtendedProperties', ((1, 'Properties'),)))
    IInkStrokeDisp.get_PolylineCusps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(13, 'get_PolylineCusps', ((1, 'Cusps'),)))
    IInkStrokeDisp.get_BezierCusps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(14, 'get_BezierCusps', ((1, 'Cusps'),)))
    IInkStrokeDisp.get_SelfIntersections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(15, 'get_SelfIntersections', ((1, 'Intersections'),)))
    IInkStrokeDisp.get_PacketCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(16, 'get_PacketCount', ((1, 'plCount'),)))
    IInkStrokeDisp.get_PacketSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(17, 'get_PacketSize', ((1, 'plSize'),)))
    IInkStrokeDisp.get_PacketDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head))(18, 'get_PacketDescription', ((1, 'PacketDescription'),)))
    IInkStrokeDisp.get_Deleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(19, 'get_Deleted', ((1, 'Deleted'),)))
    IInkStrokeDisp.GetBoundingBox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkBoundingBoxMode,POINTER(win32more.UI.TabletPC.IInkRectangle_head))(20, 'GetBoundingBox', ((1, 'BoundingBoxMode'),(1, 'Rectangle'),)))
    IInkStrokeDisp.FindIntersections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head,POINTER(win32more.System.Com.VARIANT_head))(21, 'FindIntersections', ((1, 'Strokes'),(1, 'Intersections'),)))
    IInkStrokeDisp.GetRectangleIntersections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head,POINTER(win32more.System.Com.VARIANT_head))(22, 'GetRectangleIntersections', ((1, 'Rectangle'),(1, 'Intersections'),)))
    IInkStrokeDisp.Clip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head)(23, 'Clip', ((1, 'Rectangle'),)))
    IInkStrokeDisp.HitTestCircle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Single,POINTER(win32more.Foundation.VARIANT_BOOL))(24, 'HitTestCircle', ((1, 'X'),(1, 'Y'),(1, 'Radius'),(1, 'Intersects'),)))
    IInkStrokeDisp.NearestPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Single),POINTER(Single))(25, 'NearestPoint', ((1, 'X'),(1, 'Y'),(1, 'Distance'),(1, 'Point'),)))
    IInkStrokeDisp.Split = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(win32more.UI.TabletPC.IInkStrokeDisp_head))(26, 'Split', ((1, 'SplitAt'),(1, 'NewStroke'),)))
    IInkStrokeDisp.GetPacketDescriptionPropertyMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int32),POINTER(Int32),POINTER(win32more.UI.TabletPC.TabletPropertyMetricUnit),POINTER(Single))(27, 'GetPacketDescriptionPropertyMetrics', ((1, 'PropertyName'),(1, 'Minimum'),(1, 'Maximum'),(1, 'Units'),(1, 'Resolution'),)))
    IInkStrokeDisp.GetPoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head))(28, 'GetPoints', ((1, 'Index'),(1, 'Count'),(1, 'Points'),)))
    IInkStrokeDisp.SetPoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,Int32,Int32,POINTER(Int32))(29, 'SetPoints', ((1, 'Points'),(1, 'Index'),(1, 'Count'),(1, 'NumberOfPointsSet'),)))
    IInkStrokeDisp.GetPacketData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head))(30, 'GetPacketData', ((1, 'Index'),(1, 'Count'),(1, 'PacketData'),)))
    IInkStrokeDisp.GetPacketValuesByProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,POINTER(win32more.System.Com.VARIANT_head))(31, 'GetPacketValuesByProperty', ((1, 'PropertyName'),(1, 'Index'),(1, 'Count'),(1, 'PacketValues'),)))
    IInkStrokeDisp.SetPacketValuesByProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.VARIANT,Int32,Int32,POINTER(Int32))(32, 'SetPacketValuesByProperty', ((1, 'bstrPropertyName'),(1, 'PacketValues'),(1, 'Index'),(1, 'Count'),(1, 'NumberOfPacketsSet'),)))
    IInkStrokeDisp.GetFlattenedBezierPoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head))(33, 'GetFlattenedBezierPoints', ((1, 'FittingError'),(1, 'FlattenedBezierPoints'),)))
    IInkStrokeDisp.Transform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkTransform_head,win32more.Foundation.VARIANT_BOOL)(34, 'Transform', ((1, 'Transform'),(1, 'ApplyOnPenWidth'),)))
    IInkStrokeDisp.ScaleToRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head)(35, 'ScaleToRectangle', ((1, 'Rectangle'),)))
    IInkStrokeDisp.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single)(36, 'Move', ((1, 'HorizontalComponent'),(1, 'VerticalComponent'),)))
    IInkStrokeDisp.Rotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single)(37, 'Rotate', ((1, 'Degrees'),(1, 'x'),(1, 'y'),)))
    IInkStrokeDisp.Shear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single)(38, 'Shear', ((1, 'HorizontalMultiplier'),(1, 'VerticalMultiplier'),)))
    IInkStrokeDisp.ScaleTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single)(39, 'ScaleTransform', ((1, 'HorizontalMultiplier'),(1, 'VerticalMultiplier'),)))
    win32more.System.Com.IDispatch
    return IInkStrokeDisp
def _define_IInkStrokes_head():
    class IInkStrokes(win32more.System.Com.IDispatch_head):
        Guid = Guid('f1f4c9d8-590a-4963-b3-ae-19-35-67-1b-b6-f3')
    return IInkStrokes
def _define_IInkStrokes():
    IInkStrokes = win32more.UI.TabletPC.IInkStrokes_head
    IInkStrokes.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'Count'),)))
    IInkStrokes.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(8, 'get__NewEnum', ((1, '_NewEnum'),)))
    IInkStrokes.get_Ink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDisp_head))(9, 'get_Ink', ((1, 'Ink'),)))
    IInkStrokes.get_RecognitionResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRecognitionResult_head))(10, 'get_RecognitionResult', ((1, 'RecognitionResult'),)))
    IInkStrokes.ToString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'ToString', ((1, 'ToString'),)))
    IInkStrokes.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.TabletPC.IInkStrokeDisp_head))(12, 'Item', ((1, 'Index'),(1, 'Stroke'),)))
    IInkStrokes.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokeDisp_head)(13, 'Add', ((1, 'InkStroke'),)))
    IInkStrokes.AddStrokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head)(14, 'AddStrokes', ((1, 'InkStrokes'),)))
    IInkStrokes.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokeDisp_head)(15, 'Remove', ((1, 'InkStroke'),)))
    IInkStrokes.RemoveStrokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkStrokes_head)(16, 'RemoveStrokes', ((1, 'InkStrokes'),)))
    IInkStrokes.ModifyDrawingAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkDrawingAttributes_head)(17, 'ModifyDrawingAttributes', ((1, 'DrawAttrs'),)))
    IInkStrokes.GetBoundingBox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InkBoundingBoxMode,POINTER(win32more.UI.TabletPC.IInkRectangle_head))(18, 'GetBoundingBox', ((1, 'BoundingBoxMode'),(1, 'BoundingBox'),)))
    IInkStrokes.Transform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkTransform_head,win32more.Foundation.VARIANT_BOOL)(19, 'Transform', ((1, 'Transform'),(1, 'ApplyOnPenWidth'),)))
    IInkStrokes.ScaleToRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head)(20, 'ScaleToRectangle', ((1, 'Rectangle'),)))
    IInkStrokes.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single)(21, 'Move', ((1, 'HorizontalComponent'),(1, 'VerticalComponent'),)))
    IInkStrokes.Rotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single)(22, 'Rotate', ((1, 'Degrees'),(1, 'x'),(1, 'y'),)))
    IInkStrokes.Shear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single)(23, 'Shear', ((1, 'HorizontalMultiplier'),(1, 'VerticalMultiplier'),)))
    IInkStrokes.ScaleTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single)(24, 'ScaleTransform', ((1, 'HorizontalMultiplier'),(1, 'VerticalMultiplier'),)))
    IInkStrokes.Clip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkRectangle_head)(25, 'Clip', ((1, 'Rectangle'),)))
    IInkStrokes.RemoveRecognitionResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(26, 'RemoveRecognitionResult', ()))
    win32more.System.Com.IDispatch
    return IInkStrokes
def _define_IInkTablet_head():
    class IInkTablet(win32more.System.Com.IDispatch_head):
        Guid = Guid('2de25eaa-6ef8-42d5-ae-e9-18-5b-c8-1b-91-2d')
    return IInkTablet
def _define_IInkTablet():
    IInkTablet = win32more.UI.TabletPC.IInkTablet_head
    IInkTablet.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'get_Name', ((1, 'Name'),)))
    IInkTablet.get_PlugAndPlayId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_PlugAndPlayId', ((1, 'Id'),)))
    IInkTablet.get_MaximumInputRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkRectangle_head))(9, 'get_MaximumInputRectangle', ((1, 'Rectangle'),)))
    IInkTablet.get_HardwareCapabilities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.TabletHardwareCapabilities))(10, 'get_HardwareCapabilities', ((1, 'Capabilities'),)))
    IInkTablet.IsPacketPropertySupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'IsPacketPropertySupported', ((1, 'packetPropertyName'),(1, 'Supported'),)))
    IInkTablet.GetPropertyMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int32),POINTER(Int32),POINTER(win32more.UI.TabletPC.TabletPropertyMetricUnit),POINTER(Single))(12, 'GetPropertyMetrics', ((1, 'propertyName'),(1, 'Minimum'),(1, 'Maximum'),(1, 'Units'),(1, 'Resolution'),)))
    win32more.System.Com.IDispatch
    return IInkTablet
def _define_IInkTablet2_head():
    class IInkTablet2(win32more.System.Com.IDispatch_head):
        Guid = Guid('90c91ad2-fa36-49d6-95-16-ce-8d-57-0f-6f-85')
    return IInkTablet2
def _define_IInkTablet2():
    IInkTablet2 = win32more.UI.TabletPC.IInkTablet2_head
    IInkTablet2.get_DeviceKind = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.TabletDeviceKind))(7, 'get_DeviceKind', ((1, 'Kind'),)))
    win32more.System.Com.IDispatch
    return IInkTablet2
def _define_IInkTablet3_head():
    class IInkTablet3(win32more.System.Com.IDispatch_head):
        Guid = Guid('7e313997-1327-41dd-8c-a9-79-f2-4b-e1-72-50')
    return IInkTablet3
def _define_IInkTablet3():
    IInkTablet3 = win32more.UI.TabletPC.IInkTablet3_head
    IInkTablet3.get_IsMultiTouch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_IsMultiTouch', ((1, 'pIsMultiTouch'),)))
    IInkTablet3.get_MaximumCursors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'get_MaximumCursors', ((1, 'pMaximumCursors'),)))
    win32more.System.Com.IDispatch
    return IInkTablet3
def _define_IInkTablets_head():
    class IInkTablets(win32more.System.Com.IDispatch_head):
        Guid = Guid('112086d9-7779-4535-a6-99-86-2b-43-ac-18-63')
    return IInkTablets
def _define_IInkTablets():
    IInkTablets = win32more.UI.TabletPC.IInkTablets_head
    IInkTablets.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'get_Count', ((1, 'Count'),)))
    IInkTablets.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(8, 'get__NewEnum', ((1, '_NewEnum'),)))
    IInkTablets.get_DefaultTablet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkTablet_head))(9, 'get_DefaultTablet', ((1, 'DefaultTablet'),)))
    IInkTablets.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.TabletPC.IInkTablet_head))(10, 'Item', ((1, 'Index'),(1, 'Tablet'),)))
    IInkTablets.IsPacketPropertySupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.VARIANT_BOOL))(11, 'IsPacketPropertySupported', ((1, 'packetPropertyName'),(1, 'Supported'),)))
    win32more.System.Com.IDispatch
    return IInkTablets
def _define_IInkTransform_head():
    class IInkTransform(win32more.System.Com.IDispatch_head):
        Guid = Guid('615f1d43-8703-4565-88-e2-82-01-d2-ec-d7-b7')
    return IInkTransform
def _define_IInkTransform():
    IInkTransform = win32more.UI.TabletPC.IInkTransform_head
    IInkTransform.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Reset', ()))
    IInkTransform.Translate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single)(8, 'Translate', ((1, 'HorizontalComponent'),(1, 'VerticalComponent'),)))
    IInkTransform.Rotate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single)(9, 'Rotate', ((1, 'Degrees'),(1, 'x'),(1, 'y'),)))
    IInkTransform.Reflect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL,win32more.Foundation.VARIANT_BOOL)(10, 'Reflect', ((1, 'Horizontally'),(1, 'Vertically'),)))
    IInkTransform.Shear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single)(11, 'Shear', ((1, 'HorizontalComponent'),(1, 'VerticalComponent'),)))
    IInkTransform.ScaleTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single)(12, 'ScaleTransform', ((1, 'HorizontalMultiplier'),(1, 'VerticalMultiplier'),)))
    IInkTransform.GetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),POINTER(Single),POINTER(Single),POINTER(Single),POINTER(Single),POINTER(Single))(13, 'GetTransform', ((1, 'eM11'),(1, 'eM12'),(1, 'eM21'),(1, 'eM22'),(1, 'eDx'),(1, 'eDy'),)))
    IInkTransform.SetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,Single,Single,Single)(14, 'SetTransform', ((1, 'eM11'),(1, 'eM12'),(1, 'eM21'),(1, 'eM22'),(1, 'eDx'),(1, 'eDy'),)))
    IInkTransform.get_eM11 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(15, 'get_eM11', ((1, 'Value'),)))
    IInkTransform.put_eM11 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(16, 'put_eM11', ((1, 'Value'),)))
    IInkTransform.get_eM12 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(17, 'get_eM12', ((1, 'Value'),)))
    IInkTransform.put_eM12 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(18, 'put_eM12', ((1, 'Value'),)))
    IInkTransform.get_eM21 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(19, 'get_eM21', ((1, 'Value'),)))
    IInkTransform.put_eM21 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(20, 'put_eM21', ((1, 'Value'),)))
    IInkTransform.get_eM22 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(21, 'get_eM22', ((1, 'Value'),)))
    IInkTransform.put_eM22 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(22, 'put_eM22', ((1, 'Value'),)))
    IInkTransform.get_eDx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(23, 'get_eDx', ((1, 'Value'),)))
    IInkTransform.put_eDx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(24, 'put_eDx', ((1, 'Value'),)))
    IInkTransform.get_eDy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(25, 'get_eDy', ((1, 'Value'),)))
    IInkTransform.put_eDy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(26, 'put_eDy', ((1, 'Value'),)))
    IInkTransform.get_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Gdi.XFORM_head))(27, 'get_Data', ((1, 'XForm'),)))
    IInkTransform.put_Data = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.XFORM)(28, 'put_Data', ((1, 'XForm'),)))
    win32more.System.Com.IDispatch
    return IInkTransform
def _define_IInkWordList_head():
    class IInkWordList(win32more.System.Com.IDispatch_head):
        Guid = Guid('76ba3491-cb2f-406b-99-61-0e-0c-4c-da-ae-f2')
    return IInkWordList
def _define_IInkWordList():
    IInkWordList = win32more.UI.TabletPC.IInkWordList_head
    IInkWordList.AddWord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(7, 'AddWord', ((1, 'NewWord'),)))
    IInkWordList.RemoveWord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'RemoveWord', ((1, 'RemoveWord'),)))
    IInkWordList.Merge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkWordList_head)(9, 'Merge', ((1, 'MergeWordList'),)))
    win32more.System.Com.IDispatch
    return IInkWordList
def _define_IInkWordList2_head():
    class IInkWordList2(win32more.System.Com.IDispatch_head):
        Guid = Guid('14542586-11bf-4f5f-b6-e7-49-d0-74-4a-ab-6e')
    return IInkWordList2
def _define_IInkWordList2():
    IInkWordList2 = win32more.UI.TabletPC.IInkWordList2_head
    IInkWordList2.AddWords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(7, 'AddWords', ((1, 'NewWords'),)))
    win32more.System.Com.IDispatch
    return IInkWordList2
def _define_IInputPanelWindowHandle_head():
    class IInputPanelWindowHandle(win32more.System.Com.IUnknown_head):
        Guid = Guid('4af81847-fdc4-4fc3-ad-0b-42-24-79-c1-b9-35')
    return IInputPanelWindowHandle
def _define_IInputPanelWindowHandle():
    IInputPanelWindowHandle = win32more.UI.TabletPC.IInputPanelWindowHandle_head
    IInputPanelWindowHandle.get_AttachedEditWindow32 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(3, 'get_AttachedEditWindow32', ((1, 'AttachedEditWindow'),)))
    IInputPanelWindowHandle.put_AttachedEditWindow32 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(4, 'put_AttachedEditWindow32', ((1, 'AttachedEditWindow'),)))
    IInputPanelWindowHandle.get_AttachedEditWindow64 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64))(5, 'get_AttachedEditWindow64', ((1, 'AttachedEditWindow'),)))
    IInputPanelWindowHandle.put_AttachedEditWindow64 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64)(6, 'put_AttachedEditWindow64', ((1, 'AttachedEditWindow'),)))
    win32more.System.Com.IUnknown
    return IInputPanelWindowHandle
def _define_IMathInputControl_head():
    class IMathInputControl(win32more.System.Com.IDispatch_head):
        Guid = Guid('eba615aa-fac6-4738-ba-5f-ff-09-e9-fe-47-3e')
    return IMathInputControl
def _define_IMathInputControl():
    IMathInputControl = win32more.UI.TabletPC.IMathInputControl_head
    IMathInputControl.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Show', ()))
    IMathInputControl.Hide = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Hide', ()))
    IMathInputControl.IsVisible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(9, 'IsVisible', ((1, 'pvbShown'),)))
    IMathInputControl.GetPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32))(10, 'GetPosition', ((1, 'Left'),(1, 'Top'),(1, 'Right'),(1, 'Bottom'),)))
    IMathInputControl.SetPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,Int32)(11, 'SetPosition', ((1, 'Left'),(1, 'Top'),(1, 'Right'),(1, 'Bottom'),)))
    IMathInputControl.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(12, 'Clear', ()))
    IMathInputControl.SetCustomPaint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.VARIANT_BOOL)(13, 'SetCustomPaint', ((1, 'Element'),(1, 'Paint'),)))
    IMathInputControl.SetCaptionText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(14, 'SetCaptionText', ((1, 'CaptionText'),)))
    IMathInputControl.LoadInk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkDisp_head)(15, 'LoadInk', ((1, 'Ink'),)))
    IMathInputControl.SetOwnerWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr)(16, 'SetOwnerWindow', ((1, 'OwnerWindow'),)))
    IMathInputControl.EnableExtendedButtons = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(17, 'EnableExtendedButtons', ((1, 'Extended'),)))
    IMathInputControl.GetPreviewHeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(18, 'GetPreviewHeight', ((1, 'Height'),)))
    IMathInputControl.SetPreviewHeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(19, 'SetPreviewHeight', ((1, 'Height'),)))
    IMathInputControl.EnableAutoGrow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(20, 'EnableAutoGrow', ((1, 'AutoGrow'),)))
    IMathInputControl.AddFunctionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(21, 'AddFunctionName', ((1, 'FunctionName'),)))
    IMathInputControl.RemoveFunctionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(22, 'RemoveFunctionName', ((1, 'FunctionName'),)))
    IMathInputControl.GetHoverIcon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IPictureDisp_head))(23, 'GetHoverIcon', ((1, 'HoverImage'),)))
    win32more.System.Com.IDispatch
    return IMathInputControl
Ink = Guid('13de4a42-8d21-4c8e-bf-9c-8f-69-cb-06-8f-ca')
INK_METRIC_FLAGS = Int32
IMF_FONT_SELECTED_IN_HDC = 1
IMF_ITALIC = 2
IMF_BOLD = 4
InkApplicationGesture = Int32
IAG_AllGestures = 0
IAG_NoGesture = 61440
IAG_Scratchout = 61441
IAG_Triangle = 61442
IAG_Square = 61443
IAG_Star = 61444
IAG_Check = 61445
IAG_Curlicue = 61456
IAG_DoubleCurlicue = 61457
IAG_Circle = 61472
IAG_DoubleCircle = 61473
IAG_SemiCircleLeft = 61480
IAG_SemiCircleRight = 61481
IAG_ChevronUp = 61488
IAG_ChevronDown = 61489
IAG_ChevronLeft = 61490
IAG_ChevronRight = 61491
IAG_ArrowUp = 61496
IAG_ArrowDown = 61497
IAG_ArrowLeft = 61498
IAG_ArrowRight = 61499
IAG_Up = 61528
IAG_Down = 61529
IAG_Left = 61530
IAG_Right = 61531
IAG_UpDown = 61536
IAG_DownUp = 61537
IAG_LeftRight = 61538
IAG_RightLeft = 61539
IAG_UpLeftLong = 61540
IAG_UpRightLong = 61541
IAG_DownLeftLong = 61542
IAG_DownRightLong = 61543
IAG_UpLeft = 61544
IAG_UpRight = 61545
IAG_DownLeft = 61546
IAG_DownRight = 61547
IAG_LeftUp = 61548
IAG_LeftDown = 61549
IAG_RightUp = 61550
IAG_RightDown = 61551
IAG_Exclamation = 61604
IAG_Tap = 61680
IAG_DoubleTap = 61681
InkBoundingBoxMode = Int32
IBBM_Default = 0
IBBM_NoCurveFit = 1
IBBM_CurveFit = 2
IBBM_PointsOnly = 3
IBBM_Union = 4
InkClipboardFormats = Int32
ICF_None = 0
ICF_InkSerializedFormat = 1
ICF_SketchInk = 2
ICF_TextInk = 6
ICF_EnhancedMetafile = 8
ICF_Metafile = 32
ICF_Bitmap = 64
ICF_PasteMask = 7
ICF_CopyMask = 127
ICF_Default = 127
InkClipboardModes = Int32
ICB_Copy = 0
ICB_Cut = 1
ICB_ExtractOnly = 48
ICB_DelayedCopy = 32
ICB_Default = 0
InkCollectionMode = Int32
ICM_InkOnly = 0
ICM_GestureOnly = 1
ICM_InkAndGesture = 2
InkCollector = Guid('43fb1553-ad74-4ee8-88-e4-3e-6d-aa-c9-15-db')
InkCollectorEventInterest = Int32
ICEI_DefaultEvents = -1
ICEI_CursorDown = 0
ICEI_Stroke = 1
ICEI_NewPackets = 2
ICEI_NewInAirPackets = 3
ICEI_CursorButtonDown = 4
ICEI_CursorButtonUp = 5
ICEI_CursorInRange = 6
ICEI_CursorOutOfRange = 7
ICEI_SystemGesture = 8
ICEI_TabletAdded = 9
ICEI_TabletRemoved = 10
ICEI_MouseDown = 11
ICEI_MouseMove = 12
ICEI_MouseUp = 13
ICEI_MouseWheel = 14
ICEI_DblClick = 15
ICEI_AllEvents = 16
InkCursorButtonState = Int32
ICBS_Unavailable = 0
ICBS_Up = 1
ICBS_Down = 2
InkDisp = Guid('937c1a34-151d-4610-9c-a6-a8-cc-9b-db-5d-83')
InkDisplayMode = Int32
IDM_Ink = 0
IDM_Text = 1
InkDivider = Guid('8854f6a0-4683-4ae7-91-91-75-2f-e6-46-12-c3')
InkDivisionType = Int32
IDT_Segment = 0
IDT_Line = 1
IDT_Paragraph = 2
IDT_Drawing = 3
InkDrawingAttributes = Guid('d8bf32a2-05a5-44c3-b3-aa-5e-80-ac-7d-25-76')
InkEdit = Guid('e5ca59f5-57c4-4dd8-9b-d6-1d-ee-ed-d2-7a-f4')
InkEditStatus = Int32
IES_Idle = 0
IES_Collecting = 1
IES_Recognizing = 2
InkExtractFlags = Int32
IEF_CopyFromOriginal = 0
IEF_RemoveFromOriginal = 1
IEF_Default = 1
InkInsertMode = Int32
IEM_InsertText = 0
IEM_InsertInk = 1
def _define_INKMETRIC_head():
    class INKMETRIC(Structure):
        pass
    return INKMETRIC
def _define_INKMETRIC():
    INKMETRIC = win32more.UI.TabletPC.INKMETRIC_head
    INKMETRIC._fields_ = [
        ('iHeight', Int32),
        ('iFontAscent', Int32),
        ('iFontDescent', Int32),
        ('dwFlags', UInt32),
        ('color', win32more.Foundation.COLORREF),
    ]
    return INKMETRIC
InkMode = Int32
IEM_Disabled = 0
IEM_Ink = 1
IEM_InkAndGesture = 2
InkMouseButton = Int32
IMF_Left = 1
IMF_Right = 2
IMF_Middle = 4
InkMousePointer = Int32
IMP_Default = 0
IMP_Arrow = 1
IMP_Crosshair = 2
IMP_Ibeam = 3
IMP_SizeNESW = 4
IMP_SizeNS = 5
IMP_SizeNWSE = 6
IMP_SizeWE = 7
IMP_UpArrow = 8
IMP_Hourglass = 9
IMP_NoDrop = 10
IMP_ArrowHourglass = 11
IMP_ArrowQuestion = 12
IMP_SizeAll = 13
IMP_Hand = 14
IMP_Custom = 99
InkOverlay = Guid('65d00646-cde3-4a88-91-63-67-69-f0-f1-a9-7d')
InkOverlayAttachMode = Int32
IOAM_Behind = 0
IOAM_InFront = 1
InkOverlayEditingMode = Int32
IOEM_Ink = 0
IOEM_Delete = 1
IOEM_Select = 2
InkOverlayEraserMode = Int32
IOERM_StrokeErase = 0
IOERM_PointErase = 1
InkPenTip = Int32
IPT_Ball = 0
IPT_Rectangle = 1
InkPersistenceCompressionMode = Int32
IPCM_Default = 0
IPCM_MaximumCompression = 1
IPCM_NoCompression = 2
InkPersistenceFormat = Int32
IPF_InkSerializedFormat = 0
IPF_Base64InkSerializedFormat = 1
IPF_GIF = 2
IPF_Base64GIF = 3
InkPicture = Guid('04a1e553-fe36-4fde-86-5e-34-41-94-e6-94-24')
InkPictureSizeMode = Int32
IPSM_AutoSize = 0
IPSM_CenterImage = 1
IPSM_Normal = 2
IPSM_StretchImage = 3
InkRasterOperation = Int32
IRO_Black = 1
IRO_NotMergePen = 2
IRO_MaskNotPen = 3
IRO_NotCopyPen = 4
IRO_MaskPenNot = 5
IRO_Not = 6
IRO_XOrPen = 7
IRO_NotMaskPen = 8
IRO_MaskPen = 9
IRO_NotXOrPen = 10
IRO_NoOperation = 11
IRO_MergeNotPen = 12
IRO_CopyPen = 13
IRO_MergePenNot = 14
IRO_MergePen = 15
IRO_White = 16
InkRecognitionAlternatesSelection = Int32
IRAS_Start = 0
IRAS_DefaultCount = 10
IRAS_All = -1
InkRecognitionConfidence = Int32
IRC_Strong = 0
IRC_Intermediate = 1
IRC_Poor = 2
InkRecognitionModes = Int32
IRM_None = 0
IRM_WordModeOnly = 1
IRM_Coerce = 2
IRM_TopInkBreaksOnly = 4
IRM_PrefixOk = 8
IRM_LineMode = 16
IRM_DisablePersonalization = 32
IRM_AutoSpace = 64
IRM_Max = 128
InkRecognitionStatus = Int32
IRS_NoError = 0
IRS_Interrupted = 1
IRS_ProcessFailed = 2
IRS_InkAddedFailed = 4
IRS_SetAutoCompletionModeFailed = 8
IRS_SetStrokesFailed = 16
IRS_SetGuideFailed = 32
IRS_SetFlagsFailed = 64
IRS_SetFactoidFailed = 128
IRS_SetPrefixSuffixFailed = 256
IRS_SetWordListFailed = 512
InkRecognizerCapabilities = Int32
IRC_DontCare = 1
IRC_Object = 2
IRC_FreeInput = 4
IRC_LinedInput = 8
IRC_BoxedInput = 16
IRC_CharacterAutoCompletionInput = 32
IRC_RightAndDown = 64
IRC_LeftAndDown = 128
IRC_DownAndLeft = 256
IRC_DownAndRight = 512
IRC_ArbitraryAngle = 1024
IRC_Lattice = 2048
IRC_AdviseInkChange = 4096
IRC_StrokeReorder = 8192
IRC_Personalizable = 16384
IRC_PrefersArbitraryAngle = 32768
IRC_PrefersParagraphBreaking = 65536
IRC_PrefersSegmentation = 131072
IRC_Cursive = 262144
IRC_TextPrediction = 524288
IRC_Alpha = 1048576
IRC_Beta = 2097152
InkRecognizerCharacterAutoCompletionMode = Int32
IRCACM_Full = 0
IRCACM_Prefix = 1
IRCACM_Random = 2
InkRecognizerContext = Guid('aac46a37-9229-4fc0-8c-ce-44-97-56-9b-f4-d1')
InkRecognizerGuide = Guid('8770d941-a63a-4671-a3-75-28-55-a1-8e-ba-73')
InkRecognizers = Guid('9fd4e808-f6e6-4e65-98-d3-aa-39-05-4c-12-55')
def _define_InkRecoGuide_head():
    class InkRecoGuide(Structure):
        pass
    return InkRecoGuide
def _define_InkRecoGuide():
    InkRecoGuide = win32more.UI.TabletPC.InkRecoGuide_head
    InkRecoGuide._fields_ = [
        ('rectWritingBox', win32more.Foundation.RECT),
        ('rectDrawnBox', win32more.Foundation.RECT),
        ('cRows', Int32),
        ('cColumns', Int32),
        ('midline', Int32),
    ]
    return InkRecoGuide
InkRectangle = Guid('43b07326-aae0-4b62-a8-3d-5f-d7-68-b7-35-3c')
InkRenderer = Guid('9c1cc6e4-d7eb-4eeb-90-91-15-a7-c8-79-1e-d9')
InkSelectionConstants = Int32
ISC_FirstElement = 0
ISC_AllElements = -1
InkShiftKeyModifierFlags = Int32
IKM_Shift = 1
IKM_Control = 2
IKM_Alt = 4
InkStrokes = Guid('48f491bc-240e-4860-b0-79-a1-e9-4d-3d-2c-86')
InkSystemGesture = Int32
ISG_Tap = 16
ISG_DoubleTap = 17
ISG_RightTap = 18
ISG_Drag = 19
ISG_RightDrag = 20
ISG_HoldEnter = 21
ISG_HoldLeave = 22
ISG_HoverEnter = 23
ISG_HoverLeave = 24
ISG_Flick = 31
InkTablets = Guid('6e4fcb12-510a-4d40-93-04-1d-a1-0a-e9-14-7c')
InkTransform = Guid('e3d5d93c-1663-4a78-a1-a7-22-37-5d-fe-ba-ee')
InkWordList = Guid('9de85094-f71f-44f1-84-71-15-a2-fa-76-fc-f3')
InPlaceDirection = Int32
InPlaceDirection_Auto = 0
InPlaceDirection_Bottom = 1
InPlaceDirection_Top = 2
InPlaceState = Int32
InPlaceState_Auto = 0
InPlaceState_HoverTarget = 1
InPlaceState_Expanded = 2
InteractionMode = Int32
InteractionMode_InPlace = 0
InteractionMode_Floating = 1
InteractionMode_DockedTop = 2
InteractionMode_DockedBottom = 3
def _define_IPenInputPanel_head():
    class IPenInputPanel(win32more.System.Com.IDispatch_head):
        Guid = Guid('fa7a4083-5747-4040-a1-82-0b-0e-9f-d4-fa-c7')
    return IPenInputPanel
def _define_IPenInputPanel():
    IPenInputPanel = win32more.UI.TabletPC.IPenInputPanel_head
    IPenInputPanel.get_Busy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(7, 'get_Busy', ((1, 'Busy'),)))
    IPenInputPanel.get_Factoid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'get_Factoid', ((1, 'Factoid'),)))
    IPenInputPanel.put_Factoid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(9, 'put_Factoid', ((1, 'Factoid'),)))
    IPenInputPanel.get_AttachedEditWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(10, 'get_AttachedEditWindow', ((1, 'AttachedEditWindow'),)))
    IPenInputPanel.put_AttachedEditWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(11, 'put_AttachedEditWindow', ((1, 'AttachedEditWindow'),)))
    IPenInputPanel.get_CurrentPanel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.PanelType))(12, 'get_CurrentPanel', ((1, 'CurrentPanel'),)))
    IPenInputPanel.put_CurrentPanel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.PanelType)(13, 'put_CurrentPanel', ((1, 'CurrentPanel'),)))
    IPenInputPanel.get_DefaultPanel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.PanelType))(14, 'get_DefaultPanel', ((1, 'pDefaultPanel'),)))
    IPenInputPanel.put_DefaultPanel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.PanelType)(15, 'put_DefaultPanel', ((1, 'DefaultPanel'),)))
    IPenInputPanel.get_Visible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(16, 'get_Visible', ((1, 'Visible'),)))
    IPenInputPanel.put_Visible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(17, 'put_Visible', ((1, 'Visible'),)))
    IPenInputPanel.get_Top = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(18, 'get_Top', ((1, 'Top'),)))
    IPenInputPanel.get_Left = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(19, 'get_Left', ((1, 'Left'),)))
    IPenInputPanel.get_Width = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(20, 'get_Width', ((1, 'Width'),)))
    IPenInputPanel.get_Height = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(21, 'get_Height', ((1, 'Height'),)))
    IPenInputPanel.get_VerticalOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(22, 'get_VerticalOffset', ((1, 'VerticalOffset'),)))
    IPenInputPanel.put_VerticalOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(23, 'put_VerticalOffset', ((1, 'VerticalOffset'),)))
    IPenInputPanel.get_HorizontalOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(24, 'get_HorizontalOffset', ((1, 'HorizontalOffset'),)))
    IPenInputPanel.put_HorizontalOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(25, 'put_HorizontalOffset', ((1, 'HorizontalOffset'),)))
    IPenInputPanel.get_AutoShow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.VARIANT_BOOL))(26, 'get_AutoShow', ((1, 'pAutoShow'),)))
    IPenInputPanel.put_AutoShow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(27, 'put_AutoShow', ((1, 'AutoShow'),)))
    IPenInputPanel.MoveTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32)(28, 'MoveTo', ((1, 'Left'),(1, 'Top'),)))
    IPenInputPanel.CommitPendingInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(29, 'CommitPendingInput', ()))
    IPenInputPanel.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(30, 'Refresh', ()))
    IPenInputPanel.EnableTsf = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.VARIANT_BOOL)(31, 'EnableTsf', ((1, 'Enable'),)))
    win32more.System.Com.IDispatch
    return IPenInputPanel
def _define_IRealTimeStylus_head():
    class IRealTimeStylus(win32more.System.Com.IUnknown_head):
        Guid = Guid('a8bb5d22-3144-4a7b-93-cd-f3-4a-16-be-51-3a')
    return IRealTimeStylus
def _define_IRealTimeStylus():
    IRealTimeStylus = win32more.UI.TabletPC.IRealTimeStylus_head
    IRealTimeStylus.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'get_Enabled', ((1, 'pfEnable'),)))
    IRealTimeStylus.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(4, 'put_Enabled', ((1, 'fEnable'),)))
    IRealTimeStylus.get_HWND = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE_PTR))(5, 'get_HWND', ((1, 'phwnd'),)))
    IRealTimeStylus.put_HWND = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE_PTR)(6, 'put_HWND', ((1, 'hwnd'),)))
    IRealTimeStylus.get_WindowInputRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(7, 'get_WindowInputRectangle', ((1, 'prcWndInputRect'),)))
    IRealTimeStylus.put_WindowInputRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(8, 'put_WindowInputRectangle', ((1, 'prcWndInputRect'),)))
    IRealTimeStylus.AddStylusSyncPlugin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TabletPC.IStylusSyncPlugin_head)(9, 'AddStylusSyncPlugin', ((1, 'iIndex'),(1, 'piPlugin'),)))
    IRealTimeStylus.RemoveStylusSyncPlugin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TabletPC.IStylusSyncPlugin_head))(10, 'RemoveStylusSyncPlugin', ((1, 'iIndex'),(1, 'ppiPlugin'),)))
    IRealTimeStylus.RemoveAllStylusSyncPlugins = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(11, 'RemoveAllStylusSyncPlugins', ()))
    IRealTimeStylus.GetStylusSyncPlugin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TabletPC.IStylusSyncPlugin_head))(12, 'GetStylusSyncPlugin', ((1, 'iIndex'),(1, 'ppiPlugin'),)))
    IRealTimeStylus.GetStylusSyncPluginCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(13, 'GetStylusSyncPluginCount', ((1, 'pcPlugins'),)))
    IRealTimeStylus.AddStylusAsyncPlugin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.TabletPC.IStylusAsyncPlugin_head)(14, 'AddStylusAsyncPlugin', ((1, 'iIndex'),(1, 'piPlugin'),)))
    IRealTimeStylus.RemoveStylusAsyncPlugin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TabletPC.IStylusAsyncPlugin_head))(15, 'RemoveStylusAsyncPlugin', ((1, 'iIndex'),(1, 'ppiPlugin'),)))
    IRealTimeStylus.RemoveAllStylusAsyncPlugins = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'RemoveAllStylusAsyncPlugins', ()))
    IRealTimeStylus.GetStylusAsyncPlugin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TabletPC.IStylusAsyncPlugin_head))(17, 'GetStylusAsyncPlugin', ((1, 'iIndex'),(1, 'ppiPlugin'),)))
    IRealTimeStylus.GetStylusAsyncPluginCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(18, 'GetStylusAsyncPluginCount', ((1, 'pcPlugins'),)))
    IRealTimeStylus.get_ChildRealTimeStylusPlugin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IRealTimeStylus_head))(19, 'get_ChildRealTimeStylusPlugin', ((1, 'ppiRTS'),)))
    IRealTimeStylus.putref_ChildRealTimeStylusPlugin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head)(20, 'putref_ChildRealTimeStylusPlugin', ((1, 'piRTS'),)))
    IRealTimeStylus.AddCustomStylusDataToQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.StylusQueue,POINTER(Guid),UInt32,c_char_p_no)(21, 'AddCustomStylusDataToQueue', ((1, 'sq'),(1, 'pGuidId'),(1, 'cbData'),(1, 'pbData'),)))
    IRealTimeStylus.ClearStylusQueues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(22, 'ClearStylusQueues', ()))
    IRealTimeStylus.SetAllTabletsMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(23, 'SetAllTabletsMode', ((1, 'fUseMouseForInput'),)))
    IRealTimeStylus.SetSingleTabletMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkTablet_head)(24, 'SetSingleTabletMode', ((1, 'piTablet'),)))
    IRealTimeStylus.GetTablet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkTablet_head))(25, 'GetTablet', ((1, 'ppiSingleTablet'),)))
    IRealTimeStylus.GetTabletContextIdFromTablet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkTablet_head,POINTER(UInt32))(26, 'GetTabletContextIdFromTablet', ((1, 'piTablet'),(1, 'ptcid'),)))
    IRealTimeStylus.GetTabletFromTabletContextId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TabletPC.IInkTablet_head))(27, 'GetTabletFromTabletContextId', ((1, 'tcid'),(1, 'ppiTablet'),)))
    IRealTimeStylus.GetAllTabletContextIds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(UInt32)))(28, 'GetAllTabletContextIds', ((1, 'pcTcidCount'),(1, 'ppTcids'),)))
    IRealTimeStylus.GetStyluses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkCursors_head))(29, 'GetStyluses', ((1, 'ppiInkCursors'),)))
    IRealTimeStylus.GetStylusForId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.TabletPC.IInkCursor_head))(30, 'GetStylusForId', ((1, 'sid'),(1, 'ppiInkCursor'),)))
    IRealTimeStylus.SetDesiredPacketDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid))(31, 'SetDesiredPacketDescription', ((1, 'cProperties'),(1, 'pPropertyGuids'),)))
    IRealTimeStylus.GetDesiredPacketDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(Guid)))(32, 'GetDesiredPacketDescription', ((1, 'pcProperties'),(1, 'ppPropertyGuids'),)))
    IRealTimeStylus.GetPacketDescriptionData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Single),POINTER(Single),POINTER(UInt32),POINTER(POINTER(win32more.UI.TabletPC.PACKET_PROPERTY_head)))(33, 'GetPacketDescriptionData', ((1, 'tcid'),(1, 'pfInkToDeviceScaleX'),(1, 'pfInkToDeviceScaleY'),(1, 'pcPacketProperties'),(1, 'ppPacketProperties'),)))
    win32more.System.Com.IUnknown
    return IRealTimeStylus
def _define_IRealTimeStylus2_head():
    class IRealTimeStylus2(win32more.System.Com.IUnknown_head):
        Guid = Guid('b5f2a6cd-3179-4a3e-b9-c4-bb-58-65-96-2b-e2')
    return IRealTimeStylus2
def _define_IRealTimeStylus2():
    IRealTimeStylus2 = win32more.UI.TabletPC.IRealTimeStylus2_head
    IRealTimeStylus2.get_FlicksEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'get_FlicksEnabled', ((1, 'pfEnable'),)))
    IRealTimeStylus2.put_FlicksEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(4, 'put_FlicksEnabled', ((1, 'fEnable'),)))
    win32more.System.Com.IUnknown
    return IRealTimeStylus2
def _define_IRealTimeStylus3_head():
    class IRealTimeStylus3(win32more.System.Com.IUnknown_head):
        Guid = Guid('d70230a3-6986-4051-b5-7a-1c-f6-9f-4d-9d-b5')
    return IRealTimeStylus3
def _define_IRealTimeStylus3():
    IRealTimeStylus3 = win32more.UI.TabletPC.IRealTimeStylus3_head
    IRealTimeStylus3.get_MultiTouchEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'get_MultiTouchEnabled', ((1, 'pfEnable'),)))
    IRealTimeStylus3.put_MultiTouchEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(4, 'put_MultiTouchEnabled', ((1, 'fEnable'),)))
    win32more.System.Com.IUnknown
    return IRealTimeStylus3
def _define_IRealTimeStylusSynchronization_head():
    class IRealTimeStylusSynchronization(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa87eab8-ab4a-4cea-b5-cb-46-d8-4c-6a-25-09')
    return IRealTimeStylusSynchronization
def _define_IRealTimeStylusSynchronization():
    IRealTimeStylusSynchronization = win32more.UI.TabletPC.IRealTimeStylusSynchronization_head
    IRealTimeStylusSynchronization.AcquireLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.RealTimeStylusLockType)(3, 'AcquireLock', ((1, 'lock'),)))
    IRealTimeStylusSynchronization.ReleaseLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.RealTimeStylusLockType)(4, 'ReleaseLock', ((1, 'lock'),)))
    win32more.System.Com.IUnknown
    return IRealTimeStylusSynchronization
def _define_ISketchInk_head():
    class ISketchInk(win32more.System.Com.IDispatch_head):
        Guid = Guid('b4563688-98eb-4646-b2-79-44-da-14-d4-57-48')
    return ISketchInk
def _define_ISketchInk():
    ISketchInk = win32more.UI.TabletPC.ISketchInk_head
    win32more.System.Com.IDispatch
    return ISketchInk
def _define_IStrokeBuilder_head():
    class IStrokeBuilder(win32more.System.Com.IUnknown_head):
        Guid = Guid('a5fd4e2d-c44b-4092-91-77-26-09-05-eb-67-2b')
    return IStrokeBuilder
def _define_IStrokeBuilder():
    IStrokeBuilder = win32more.UI.TabletPC.IStrokeBuilder_head
    IStrokeBuilder.CreateStroke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Int32),UInt32,POINTER(win32more.UI.TabletPC.PACKET_PROPERTY_head),Single,Single,POINTER(win32more.UI.TabletPC.IInkStrokeDisp_head))(3, 'CreateStroke', ((1, 'cPktBuffLength'),(1, 'pPackets'),(1, 'cPacketProperties'),(1, 'pPacketProperties'),(1, 'fInkToDeviceScaleX'),(1, 'fInkToDeviceScaleY'),(1, 'ppIInkStroke'),)))
    IStrokeBuilder.BeginStroke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Int32),UInt32,POINTER(win32more.UI.TabletPC.PACKET_PROPERTY_head),Single,Single,POINTER(win32more.UI.TabletPC.IInkStrokeDisp_head))(4, 'BeginStroke', ((1, 'tcid'),(1, 'sid'),(1, 'pPacket'),(1, 'cPacketProperties'),(1, 'pPacketProperties'),(1, 'fInkToDeviceScaleX'),(1, 'fInkToDeviceScaleY'),(1, 'ppIInkStroke'),)))
    IStrokeBuilder.AppendPackets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(Int32))(5, 'AppendPackets', ((1, 'tcid'),(1, 'sid'),(1, 'cPktBuffLength'),(1, 'pPackets'),)))
    IStrokeBuilder.EndStroke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.UI.TabletPC.IInkStrokeDisp_head),POINTER(win32more.Foundation.RECT_head))(6, 'EndStroke', ((1, 'tcid'),(1, 'sid'),(1, 'ppIInkStroke'),(1, 'pDirtyRect'),)))
    IStrokeBuilder.get_Ink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.IInkDisp_head))(7, 'get_Ink', ((1, 'ppiInkObj'),)))
    IStrokeBuilder.putref_Ink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IInkDisp_head)(8, 'putref_Ink', ((1, 'piInkObj'),)))
    win32more.System.Com.IUnknown
    return IStrokeBuilder
def _define_IStylusAsyncPlugin_head():
    class IStylusAsyncPlugin(win32more.UI.TabletPC.IStylusPlugin_head):
        Guid = Guid('a7cca85a-31bc-4cd2-aa-dc-32-89-a3-af-11-c8')
    return IStylusAsyncPlugin
def _define_IStylusAsyncPlugin():
    IStylusAsyncPlugin = win32more.UI.TabletPC.IStylusAsyncPlugin_head
    win32more.UI.TabletPC.IStylusPlugin
    return IStylusAsyncPlugin
def _define_IStylusPlugin_head():
    class IStylusPlugin(win32more.System.Com.IUnknown_head):
        Guid = Guid('a81436d8-4757-4fd1-a1-85-13-3f-97-c6-c5-45')
    return IStylusPlugin
def _define_IStylusPlugin():
    IStylusPlugin = win32more.UI.TabletPC.IStylusPlugin_head
    IStylusPlugin.RealTimeStylusEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,UInt32,POINTER(UInt32))(3, 'RealTimeStylusEnabled', ((1, 'piRtsSrc'),(1, 'cTcidCount'),(1, 'pTcids'),)))
    IStylusPlugin.RealTimeStylusDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,UInt32,POINTER(UInt32))(4, 'RealTimeStylusDisabled', ((1, 'piRtsSrc'),(1, 'cTcidCount'),(1, 'pTcids'),)))
    IStylusPlugin.StylusInRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,UInt32,UInt32)(5, 'StylusInRange', ((1, 'piRtsSrc'),(1, 'tcid'),(1, 'sid'),)))
    IStylusPlugin.StylusOutOfRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,UInt32,UInt32)(6, 'StylusOutOfRange', ((1, 'piRtsSrc'),(1, 'tcid'),(1, 'sid'),)))
    IStylusPlugin.StylusDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,POINTER(win32more.UI.TabletPC.StylusInfo_head),UInt32,POINTER(Int32),POINTER(POINTER(Int32)))(7, 'StylusDown', ((1, 'piRtsSrc'),(1, 'pStylusInfo'),(1, 'cPropCountPerPkt'),(1, 'pPacket'),(1, 'ppInOutPkt'),)))
    IStylusPlugin.StylusUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,POINTER(win32more.UI.TabletPC.StylusInfo_head),UInt32,POINTER(Int32),POINTER(POINTER(Int32)))(8, 'StylusUp', ((1, 'piRtsSrc'),(1, 'pStylusInfo'),(1, 'cPropCountPerPkt'),(1, 'pPacket'),(1, 'ppInOutPkt'),)))
    IStylusPlugin.StylusButtonDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,UInt32,POINTER(Guid),POINTER(win32more.Foundation.POINT_head))(9, 'StylusButtonDown', ((1, 'piRtsSrc'),(1, 'sid'),(1, 'pGuidStylusButton'),(1, 'pStylusPos'),)))
    IStylusPlugin.StylusButtonUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,UInt32,POINTER(Guid),POINTER(win32more.Foundation.POINT_head))(10, 'StylusButtonUp', ((1, 'piRtsSrc'),(1, 'sid'),(1, 'pGuidStylusButton'),(1, 'pStylusPos'),)))
    IStylusPlugin.InAirPackets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,POINTER(win32more.UI.TabletPC.StylusInfo_head),UInt32,UInt32,POINTER(Int32),POINTER(UInt32),POINTER(POINTER(Int32)))(11, 'InAirPackets', ((1, 'piRtsSrc'),(1, 'pStylusInfo'),(1, 'cPktCount'),(1, 'cPktBuffLength'),(1, 'pPackets'),(1, 'pcInOutPkts'),(1, 'ppInOutPkts'),)))
    IStylusPlugin.Packets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,POINTER(win32more.UI.TabletPC.StylusInfo_head),UInt32,UInt32,POINTER(Int32),POINTER(UInt32),POINTER(POINTER(Int32)))(12, 'Packets', ((1, 'piRtsSrc'),(1, 'pStylusInfo'),(1, 'cPktCount'),(1, 'cPktBuffLength'),(1, 'pPackets'),(1, 'pcInOutPkts'),(1, 'ppInOutPkts'),)))
    IStylusPlugin.CustomStylusDataAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,POINTER(Guid),UInt32,c_char_p_no)(13, 'CustomStylusDataAdded', ((1, 'piRtsSrc'),(1, 'pGuidId'),(1, 'cbData'),(1, 'pbData'),)))
    IStylusPlugin.SystemEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,UInt32,UInt32,UInt16,win32more.UI.TabletPC.SYSTEM_EVENT_DATA)(14, 'SystemEvent', ((1, 'piRtsSrc'),(1, 'tcid'),(1, 'sid'),(1, 'event'),(1, 'eventdata'),)))
    IStylusPlugin.TabletAdded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,win32more.UI.TabletPC.IInkTablet_head)(15, 'TabletAdded', ((1, 'piRtsSrc'),(1, 'piTablet'),)))
    IStylusPlugin.TabletRemoved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,Int32)(16, 'TabletRemoved', ((1, 'piRtsSrc'),(1, 'iTabletIndex'),)))
    IStylusPlugin.Error = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head,win32more.UI.TabletPC.IStylusPlugin_head,win32more.UI.TabletPC.RealTimeStylusDataInterest,win32more.Foundation.HRESULT,POINTER(IntPtr))(17, 'Error', ((1, 'piRtsSrc'),(1, 'piPlugin'),(1, 'dataInterest'),(1, 'hrErrorCode'),(1, 'lptrKey'),)))
    IStylusPlugin.UpdateMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.IRealTimeStylus_head)(18, 'UpdateMapping', ((1, 'piRtsSrc'),)))
    IStylusPlugin.DataInterest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.RealTimeStylusDataInterest))(19, 'DataInterest', ((1, 'pDataInterest'),)))
    win32more.System.Com.IUnknown
    return IStylusPlugin
def _define_IStylusSyncPlugin_head():
    class IStylusSyncPlugin(win32more.UI.TabletPC.IStylusPlugin_head):
        Guid = Guid('a157b174-482f-4d71-a3-f6-3a-41-dd-d1-1b-e9')
    return IStylusSyncPlugin
def _define_IStylusSyncPlugin():
    IStylusSyncPlugin = win32more.UI.TabletPC.IStylusSyncPlugin_head
    win32more.UI.TabletPC.IStylusPlugin
    return IStylusSyncPlugin
def _define_ITextInputPanel_head():
    class ITextInputPanel(win32more.System.Com.IUnknown_head):
        Guid = Guid('6b6a65a5-6af3-46c2-b6-ea-56-cd-1f-80-df-71')
    return ITextInputPanel
def _define_ITextInputPanel():
    ITextInputPanel = win32more.UI.TabletPC.ITextInputPanel_head
    ITextInputPanel.get_AttachedEditWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND))(3, 'get_AttachedEditWindow', ((1, 'AttachedEditWindow'),)))
    ITextInputPanel.put_AttachedEditWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND)(4, 'put_AttachedEditWindow', ((1, 'AttachedEditWindow'),)))
    ITextInputPanel.get_CurrentInteractionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InteractionMode))(5, 'get_CurrentInteractionMode', ((1, 'CurrentInteractionMode'),)))
    ITextInputPanel.get_DefaultInPlaceState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InPlaceState))(6, 'get_DefaultInPlaceState', ((1, 'State'),)))
    ITextInputPanel.put_DefaultInPlaceState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InPlaceState)(7, 'put_DefaultInPlaceState', ((1, 'State'),)))
    ITextInputPanel.get_CurrentInPlaceState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InPlaceState))(8, 'get_CurrentInPlaceState', ((1, 'State'),)))
    ITextInputPanel.get_DefaultInputArea = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.PanelInputArea))(9, 'get_DefaultInputArea', ((1, 'Area'),)))
    ITextInputPanel.put_DefaultInputArea = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.PanelInputArea)(10, 'put_DefaultInputArea', ((1, 'Area'),)))
    ITextInputPanel.get_CurrentInputArea = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.PanelInputArea))(11, 'get_CurrentInputArea', ((1, 'Area'),)))
    ITextInputPanel.get_CurrentCorrectionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.CorrectionMode))(12, 'get_CurrentCorrectionMode', ((1, 'Mode'),)))
    ITextInputPanel.get_PreferredInPlaceDirection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.TabletPC.InPlaceDirection))(13, 'get_PreferredInPlaceDirection', ((1, 'Direction'),)))
    ITextInputPanel.put_PreferredInPlaceDirection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InPlaceDirection)(14, 'put_PreferredInPlaceDirection', ((1, 'Direction'),)))
    ITextInputPanel.get_ExpandPostInsertionCorrection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(15, 'get_ExpandPostInsertionCorrection', ((1, 'Expand'),)))
    ITextInputPanel.put_ExpandPostInsertionCorrection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(16, 'put_ExpandPostInsertionCorrection', ((1, 'Expand'),)))
    ITextInputPanel.get_InPlaceVisibleOnFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(17, 'get_InPlaceVisibleOnFocus', ((1, 'Visible'),)))
    ITextInputPanel.put_InPlaceVisibleOnFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(18, 'put_InPlaceVisibleOnFocus', ((1, 'Visible'),)))
    ITextInputPanel.get_InPlaceBoundingRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head))(19, 'get_InPlaceBoundingRectangle', ((1, 'BoundingRectangle'),)))
    ITextInputPanel.get_PopUpCorrectionHeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(20, 'get_PopUpCorrectionHeight', ((1, 'Height'),)))
    ITextInputPanel.get_PopDownCorrectionHeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(21, 'get_PopDownCorrectionHeight', ((1, 'Height'),)))
    ITextInputPanel.CommitPendingInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(22, 'CommitPendingInput', ()))
    ITextInputPanel.SetInPlaceVisibility = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(23, 'SetInPlaceVisibility', ((1, 'Visible'),)))
    ITextInputPanel.SetInPlacePosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.UI.TabletPC.CorrectionPosition)(24, 'SetInPlacePosition', ((1, 'xPosition'),(1, 'yPosition'),(1, 'position'),)))
    ITextInputPanel.SetInPlaceHoverTargetPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32)(25, 'SetInPlaceHoverTargetPosition', ((1, 'xPosition'),(1, 'yPosition'),)))
    ITextInputPanel.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.ITextInputPanelEventSink_head,UInt32)(26, 'Advise', ((1, 'EventSink'),(1, 'EventMask'),)))
    ITextInputPanel.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.ITextInputPanelEventSink_head)(27, 'Unadvise', ((1, 'EventSink'),)))
    win32more.System.Com.IUnknown
    return ITextInputPanel
def _define_ITextInputPanelEventSink_head():
    class ITextInputPanelEventSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('27560408-8e64-4fe1-80-4e-42-12-01-58-4b-31')
    return ITextInputPanelEventSink
def _define_ITextInputPanelEventSink():
    ITextInputPanelEventSink = win32more.UI.TabletPC.ITextInputPanelEventSink_head
    ITextInputPanelEventSink.InPlaceStateChanging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InPlaceState,win32more.UI.TabletPC.InPlaceState)(3, 'InPlaceStateChanging', ((1, 'oldInPlaceState'),(1, 'newInPlaceState'),)))
    ITextInputPanelEventSink.InPlaceStateChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.InPlaceState,win32more.UI.TabletPC.InPlaceState)(4, 'InPlaceStateChanged', ((1, 'oldInPlaceState'),(1, 'newInPlaceState'),)))
    ITextInputPanelEventSink.InPlaceSizeChanging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.RECT,win32more.Foundation.RECT)(5, 'InPlaceSizeChanging', ((1, 'oldBoundingRectangle'),(1, 'newBoundingRectangle'),)))
    ITextInputPanelEventSink.InPlaceSizeChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.RECT,win32more.Foundation.RECT)(6, 'InPlaceSizeChanged', ((1, 'oldBoundingRectangle'),(1, 'newBoundingRectangle'),)))
    ITextInputPanelEventSink.InputAreaChanging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.PanelInputArea,win32more.UI.TabletPC.PanelInputArea)(7, 'InputAreaChanging', ((1, 'oldInputArea'),(1, 'newInputArea'),)))
    ITextInputPanelEventSink.InputAreaChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.PanelInputArea,win32more.UI.TabletPC.PanelInputArea)(8, 'InputAreaChanged', ((1, 'oldInputArea'),(1, 'newInputArea'),)))
    ITextInputPanelEventSink.CorrectionModeChanging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.CorrectionMode,win32more.UI.TabletPC.CorrectionMode)(9, 'CorrectionModeChanging', ((1, 'oldCorrectionMode'),(1, 'newCorrectionMode'),)))
    ITextInputPanelEventSink.CorrectionModeChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TabletPC.CorrectionMode,win32more.UI.TabletPC.CorrectionMode)(10, 'CorrectionModeChanged', ((1, 'oldCorrectionMode'),(1, 'newCorrectionMode'),)))
    ITextInputPanelEventSink.InPlaceVisibilityChanging = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.BOOL)(11, 'InPlaceVisibilityChanging', ((1, 'oldVisible'),(1, 'newVisible'),)))
    ITextInputPanelEventSink.InPlaceVisibilityChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.BOOL)(12, 'InPlaceVisibilityChanged', ((1, 'oldVisible'),(1, 'newVisible'),)))
    ITextInputPanelEventSink.TextInserting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(13, 'TextInserting', ((1, 'Ink'),)))
    ITextInputPanelEventSink.TextInserted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head))(14, 'TextInserted', ((1, 'Ink'),)))
    win32more.System.Com.IUnknown
    return ITextInputPanelEventSink
def _define_ITextInputPanelRunInfo_head():
    class ITextInputPanelRunInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('9f424568-1920-48cc-98-11-a9-93-cb-f5-ad-ba')
    return ITextInputPanelRunInfo
def _define_ITextInputPanelRunInfo():
    ITextInputPanelRunInfo = win32more.UI.TabletPC.ITextInputPanelRunInfo_head
    ITextInputPanelRunInfo.IsTipRunning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(3, 'IsTipRunning', ((1, 'pfRunning'),)))
    win32more.System.Com.IUnknown
    return ITextInputPanelRunInfo
def _define_ITipAutoCompleteClient_head():
    class ITipAutoCompleteClient(win32more.System.Com.IUnknown_head):
        Guid = Guid('5e078e03-8265-4bbe-94-87-d2-42-ed-be-f9-10')
    return ITipAutoCompleteClient
def _define_ITipAutoCompleteClient():
    ITipAutoCompleteClient = win32more.UI.TabletPC.ITipAutoCompleteClient_head
    ITipAutoCompleteClient.AdviseProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.UI.TabletPC.ITipAutoCompleteProvider_head)(3, 'AdviseProvider', ((1, 'hWndField'),(1, 'pIProvider'),)))
    ITipAutoCompleteClient.UnadviseProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.UI.TabletPC.ITipAutoCompleteProvider_head)(4, 'UnadviseProvider', ((1, 'hWndField'),(1, 'pIProvider'),)))
    ITipAutoCompleteClient.UserSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'UserSelection', ()))
    ITipAutoCompleteClient.PreferredRects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.BOOL))(6, 'PreferredRects', ((1, 'prcACList'),(1, 'prcField'),(1, 'prcModifiedACList'),(1, 'pfShownAboveTip'),)))
    ITipAutoCompleteClient.RequestShowUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.BOOL))(7, 'RequestShowUI', ((1, 'hWndList'),(1, 'pfAllowShowing'),)))
    win32more.System.Com.IUnknown
    return ITipAutoCompleteClient
def _define_ITipAutoCompleteProvider_head():
    class ITipAutoCompleteProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('7c6cf46d-8404-46b9-ad-33-f5-b6-03-6d-40-07')
    return ITipAutoCompleteProvider
def _define_ITipAutoCompleteProvider():
    ITipAutoCompleteProvider = win32more.UI.TabletPC.ITipAutoCompleteProvider_head
    ITipAutoCompleteProvider.UpdatePendingText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(3, 'UpdatePendingText', ((1, 'bstrPendingText'),)))
    ITipAutoCompleteProvider.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(4, 'Show', ((1, 'fShow'),)))
    win32more.System.Com.IUnknown
    return ITipAutoCompleteProvider
KEYMODIFIER = Int32
KEYMODIFIER_CONTROL = 1
KEYMODIFIER_MENU = 2
KEYMODIFIER_SHIFT = 4
KEYMODIFIER_WIN = 8
KEYMODIFIER_ALTGR = 16
KEYMODIFIER_EXT = 32
def _define_LATTICE_METRICS_head():
    class LATTICE_METRICS(Structure):
        pass
    return LATTICE_METRICS
def _define_LATTICE_METRICS():
    LATTICE_METRICS = win32more.UI.TabletPC.LATTICE_METRICS_head
    LATTICE_METRICS._fields_ = [
        ('lsBaseline', win32more.UI.TabletPC.LINE_SEGMENT),
        ('iMidlineOffset', Int16),
    ]
    return LATTICE_METRICS
LINE_METRICS = Int32
LM_BASELINE = 0
LM_MIDLINE = 1
LM_ASCENDER = 2
LM_DESCENDER = 3
def _define_LINE_SEGMENT_head():
    class LINE_SEGMENT(Structure):
        pass
    return LINE_SEGMENT
def _define_LINE_SEGMENT():
    LINE_SEGMENT = win32more.UI.TabletPC.LINE_SEGMENT_head
    LINE_SEGMENT._fields_ = [
        ('PtA', win32more.Foundation.POINT),
        ('PtB', win32more.Foundation.POINT),
    ]
    return LINE_SEGMENT
MathInputControl = Guid('c561816c-14d8-4090-83-0c-98-d9-94-b2-1c-7b')
MICUIELEMENT = Int32
MICUIELEMENT_BUTTON_WRITE = 1
MICUIELEMENT_BUTTON_ERASE = 2
MICUIELEMENT_BUTTON_CORRECT = 4
MICUIELEMENT_BUTTON_CLEAR = 8
MICUIELEMENT_BUTTON_UNDO = 16
MICUIELEMENT_BUTTON_REDO = 32
MICUIELEMENT_BUTTON_INSERT = 64
MICUIELEMENT_BUTTON_CANCEL = 128
MICUIELEMENT_INKPANEL_BACKGROUND = 256
MICUIELEMENT_RESULTPANEL_BACKGROUND = 512
MICUIELEMENTSTATE = Int32
MICUIELEMENTSTATE_NORMAL = 1
MICUIELEMENTSTATE_HOT = 2
MICUIELEMENTSTATE_PRESSED = 3
MICUIELEMENTSTATE_DISABLED = 4
MouseButton = Int32
NO_BUTTON = 0
LEFT_BUTTON = 1
RIGHT_BUTTON = 2
MIDDLE_BUTTON = 4
def _define_PACKET_DESCRIPTION_head():
    class PACKET_DESCRIPTION(Structure):
        pass
    return PACKET_DESCRIPTION
def _define_PACKET_DESCRIPTION():
    PACKET_DESCRIPTION = win32more.UI.TabletPC.PACKET_DESCRIPTION_head
    PACKET_DESCRIPTION._fields_ = [
        ('cbPacketSize', UInt32),
        ('cPacketProperties', UInt32),
        ('pPacketProperties', POINTER(win32more.UI.TabletPC.PACKET_PROPERTY_head)),
        ('cButtons', UInt32),
        ('pguidButtons', POINTER(Guid)),
    ]
    return PACKET_DESCRIPTION
def _define_PACKET_PROPERTY_head():
    class PACKET_PROPERTY(Structure):
        pass
    return PACKET_PROPERTY
def _define_PACKET_PROPERTY():
    PACKET_PROPERTY = win32more.UI.TabletPC.PACKET_PROPERTY_head
    PACKET_PROPERTY._fields_ = [
        ('guid', Guid),
        ('PropertyMetrics', win32more.UI.TabletPC.PROPERTY_METRICS),
    ]
    return PACKET_PROPERTY
PanelInputArea = Int32
PanelInputArea_Auto = 0
PanelInputArea_Keyboard = 1
PanelInputArea_WritingPad = 2
PanelInputArea_CharacterPad = 3
PanelType = Int32
PT_Default = 0
PT_Inactive = 1
PT_Handwriting = 2
PT_Keyboard = 3
PenInputPanel = Guid('f744e496-1b5a-489e-81-dc-fb-d7-ac-62-98-a8')
PenInputPanel_Internal = Guid('802b1fb9-056b-4720-b0-cc-80-d2-3b-71-17-1e')
def _define_PfnRecoCallback():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,win32more.UI.TabletPC.HRECOCONTEXT)
def _define_PROPERTY_METRICS_head():
    class PROPERTY_METRICS(Structure):
        pass
    return PROPERTY_METRICS
def _define_PROPERTY_METRICS():
    PROPERTY_METRICS = win32more.UI.TabletPC.PROPERTY_METRICS_head
    PROPERTY_METRICS._fields_ = [
        ('nLogicalMin', Int32),
        ('nLogicalMax', Int32),
        ('Units', win32more.UI.TabletPC.PROPERTY_UNITS),
        ('fResolution', Single),
    ]
    return PROPERTY_METRICS
PROPERTY_UNITS = Int32
PROPERTY_UNITS_DEFAULT = 0
PROPERTY_UNITS_INCHES = 1
PROPERTY_UNITS_CENTIMETERS = 2
PROPERTY_UNITS_DEGREES = 3
PROPERTY_UNITS_RADIANS = 4
PROPERTY_UNITS_SECONDS = 5
PROPERTY_UNITS_POUNDS = 6
PROPERTY_UNITS_GRAMS = 7
PROPERTY_UNITS_SILINEAR = 8
PROPERTY_UNITS_SIROTATION = 9
PROPERTY_UNITS_ENGLINEAR = 10
PROPERTY_UNITS_ENGROTATION = 11
PROPERTY_UNITS_SLUGS = 12
PROPERTY_UNITS_KELVIN = 13
PROPERTY_UNITS_FAHRENHEIT = 14
PROPERTY_UNITS_AMPERE = 15
PROPERTY_UNITS_CANDELA = 16
RealTimeStylus = Guid('e26b366d-f998-43ce-83-6f-cb-6d-90-44-32-b0')
RealTimeStylusDataInterest = Int32
RTSDI_AllData = -1
RTSDI_None = 0
RTSDI_Error = 1
RTSDI_RealTimeStylusEnabled = 2
RTSDI_RealTimeStylusDisabled = 4
RTSDI_StylusNew = 8
RTSDI_StylusInRange = 16
RTSDI_InAirPackets = 32
RTSDI_StylusOutOfRange = 64
RTSDI_StylusDown = 128
RTSDI_Packets = 256
RTSDI_StylusUp = 512
RTSDI_StylusButtonUp = 1024
RTSDI_StylusButtonDown = 2048
RTSDI_SystemEvents = 4096
RTSDI_TabletAdded = 8192
RTSDI_TabletRemoved = 16384
RTSDI_CustomStylusDataAdded = 32768
RTSDI_UpdateMapping = 65536
RTSDI_DefaultEvents = 37766
RealTimeStylusLockType = Int32
RTSLT_ObjLock = 1
RTSLT_SyncEventLock = 2
RTSLT_AsyncEventLock = 4
RTSLT_ExcludeCallback = 8
RTSLT_SyncObjLock = 11
RTSLT_AsyncObjLock = 13
def _define_RECO_ATTRS_head():
    class RECO_ATTRS(Structure):
        pass
    return RECO_ATTRS
def _define_RECO_ATTRS():
    RECO_ATTRS = win32more.UI.TabletPC.RECO_ATTRS_head
    RECO_ATTRS._fields_ = [
        ('dwRecoCapabilityFlags', UInt32),
        ('awcVendorName', Char * 32),
        ('awcFriendlyName', Char * 64),
        ('awLanguageId', UInt16 * 64),
    ]
    return RECO_ATTRS
def _define_RECO_GUIDE_head():
    class RECO_GUIDE(Structure):
        pass
    return RECO_GUIDE
def _define_RECO_GUIDE():
    RECO_GUIDE = win32more.UI.TabletPC.RECO_GUIDE_head
    RECO_GUIDE._fields_ = [
        ('xOrigin', Int32),
        ('yOrigin', Int32),
        ('cxBox', Int32),
        ('cyBox', Int32),
        ('cxBase', Int32),
        ('cyBase', Int32),
        ('cHorzBox', Int32),
        ('cVertBox', Int32),
        ('cyMid', Int32),
    ]
    return RECO_GUIDE
def _define_RECO_LATTICE_head():
    class RECO_LATTICE(Structure):
        pass
    return RECO_LATTICE
def _define_RECO_LATTICE():
    RECO_LATTICE = win32more.UI.TabletPC.RECO_LATTICE_head
    RECO_LATTICE._fields_ = [
        ('ulColumnCount', UInt32),
        ('pLatticeColumns', POINTER(win32more.UI.TabletPC.RECO_LATTICE_COLUMN_head)),
        ('ulPropertyCount', UInt32),
        ('pGuidProperties', POINTER(Guid)),
        ('ulBestResultColumnCount', UInt32),
        ('pulBestResultColumns', POINTER(UInt32)),
        ('pulBestResultIndexes', POINTER(UInt32)),
    ]
    return RECO_LATTICE
def _define_RECO_LATTICE_COLUMN_head():
    class RECO_LATTICE_COLUMN(Structure):
        pass
    return RECO_LATTICE_COLUMN
def _define_RECO_LATTICE_COLUMN():
    RECO_LATTICE_COLUMN = win32more.UI.TabletPC.RECO_LATTICE_COLUMN_head
    RECO_LATTICE_COLUMN._fields_ = [
        ('key', UInt32),
        ('cpProp', win32more.UI.TabletPC.RECO_LATTICE_PROPERTIES),
        ('cStrokes', UInt32),
        ('pStrokes', POINTER(UInt32)),
        ('cLatticeElements', UInt32),
        ('pLatticeElements', POINTER(win32more.UI.TabletPC.RECO_LATTICE_ELEMENT_head)),
    ]
    return RECO_LATTICE_COLUMN
def _define_RECO_LATTICE_ELEMENT_head():
    class RECO_LATTICE_ELEMENT(Structure):
        pass
    return RECO_LATTICE_ELEMENT
def _define_RECO_LATTICE_ELEMENT():
    RECO_LATTICE_ELEMENT = win32more.UI.TabletPC.RECO_LATTICE_ELEMENT_head
    RECO_LATTICE_ELEMENT._fields_ = [
        ('score', Int32),
        ('type', UInt16),
        ('pData', c_char_p_no),
        ('ulNextColumn', UInt32),
        ('ulStrokeNumber', UInt32),
        ('epProp', win32more.UI.TabletPC.RECO_LATTICE_PROPERTIES),
    ]
    return RECO_LATTICE_ELEMENT
def _define_RECO_LATTICE_PROPERTIES_head():
    class RECO_LATTICE_PROPERTIES(Structure):
        pass
    return RECO_LATTICE_PROPERTIES
def _define_RECO_LATTICE_PROPERTIES():
    RECO_LATTICE_PROPERTIES = win32more.UI.TabletPC.RECO_LATTICE_PROPERTIES_head
    RECO_LATTICE_PROPERTIES._fields_ = [
        ('cProperties', UInt32),
        ('apProps', POINTER(POINTER(win32more.UI.TabletPC.RECO_LATTICE_PROPERTY_head))),
    ]
    return RECO_LATTICE_PROPERTIES
def _define_RECO_LATTICE_PROPERTY_head():
    class RECO_LATTICE_PROPERTY(Structure):
        pass
    return RECO_LATTICE_PROPERTY
def _define_RECO_LATTICE_PROPERTY():
    RECO_LATTICE_PROPERTY = win32more.UI.TabletPC.RECO_LATTICE_PROPERTY_head
    RECO_LATTICE_PROPERTY._fields_ = [
        ('guidProperty', Guid),
        ('cbPropertyValue', UInt16),
        ('pPropertyValue', c_char_p_no),
    ]
    return RECO_LATTICE_PROPERTY
def _define_RECO_RANGE_head():
    class RECO_RANGE(Structure):
        pass
    return RECO_RANGE
def _define_RECO_RANGE():
    RECO_RANGE = win32more.UI.TabletPC.RECO_RANGE_head
    RECO_RANGE._fields_ = [
        ('iwcBegin', UInt32),
        ('cCount', UInt32),
    ]
    return RECO_RANGE
RECO_TYPE = Int32
RECO_TYPE_WSTRING = 0
RECO_TYPE_WCHAR = 1
ScrollBarsConstants = Int32
ScrollBarsConstants_rtfNone = 0
ScrollBarsConstants_rtfHorizontal = 1
ScrollBarsConstants_rtfVertical = 2
ScrollBarsConstants_rtfBoth = 3
SCROLLDIRECTION = Int32
SCROLLDIRECTION_UP = 0
SCROLLDIRECTION_DOWN = 1
SelAlignmentConstants = Int32
SelAlignmentConstants_rtfLeft = 0
SelAlignmentConstants_rtfRight = 1
SelAlignmentConstants_rtfCenter = 2
SelectionHitResult = Int32
SHR_None = 0
SHR_NW = 1
SHR_SE = 2
SHR_NE = 3
SHR_SW = 4
SHR_E = 5
SHR_W = 6
SHR_N = 7
SHR_S = 8
SHR_Selection = 9
SketchInk = Guid('f0291081-e87c-4e07-97-da-a0-a0-37-61-e5-86')
def _define_STROKE_RANGE_head():
    class STROKE_RANGE(Structure):
        pass
    return STROKE_RANGE
def _define_STROKE_RANGE():
    STROKE_RANGE = win32more.UI.TabletPC.STROKE_RANGE_head
    STROKE_RANGE._fields_ = [
        ('iStrokeBegin', UInt32),
        ('iStrokeEnd', UInt32),
    ]
    return STROKE_RANGE
StrokeBuilder = Guid('e810cee7-6e51-4cb0-aa-3a-0b-98-5b-70-da-f7')
def _define_StylusInfo_head():
    class StylusInfo(Structure):
        pass
    return StylusInfo
def _define_StylusInfo():
    StylusInfo = win32more.UI.TabletPC.StylusInfo_head
    StylusInfo._fields_ = [
        ('tcid', UInt32),
        ('cid', UInt32),
        ('bIsInvertedCursor', win32more.Foundation.BOOL),
    ]
    return StylusInfo
StylusQueue = Int32
StylusQueue_SyncStylusQueue = 1
StylusQueue_AsyncStylusQueueImmediate = 2
StylusQueue_AsyncStylusQueue = 3
def _define_SYSTEM_EVENT_DATA_head():
    class SYSTEM_EVENT_DATA(Structure):
        pass
    return SYSTEM_EVENT_DATA
def _define_SYSTEM_EVENT_DATA():
    SYSTEM_EVENT_DATA = win32more.UI.TabletPC.SYSTEM_EVENT_DATA_head
    SYSTEM_EVENT_DATA._fields_ = [
        ('bModifier', Byte),
        ('wKey', Char),
        ('xPos', Int32),
        ('yPos', Int32),
        ('bCursorMode', Byte),
        ('dwButtonState', UInt32),
    ]
    return SYSTEM_EVENT_DATA
TabletDeviceKind = Int32
TDK_Mouse = 0
TDK_Pen = 1
TDK_Touch = 2
TabletHardwareCapabilities = Int32
THWC_Integrated = 1
THWC_CursorMustTouch = 2
THWC_HardProximity = 4
THWC_CursorsHavePhysicalIds = 8
TabletPropertyMetricUnit = Int32
TPMU_Default = 0
TPMU_Inches = 1
TPMU_Centimeters = 2
TPMU_Degrees = 3
TPMU_Radians = 4
TPMU_Seconds = 5
TPMU_Pounds = 6
TPMU_Grams = 7
TextInputPanel = Guid('f9b189d7-228b-4f2b-86-50-b9-7f-59-e0-2c-8c')
TipAutoCompleteClient = Guid('807c1e6c-1d00-453f-b9-20-b6-1b-b7-cd-d9-97')
VisualState = Int32
VisualState_InPlace = 0
VisualState_Floating = 1
VisualState_DockedTop = 2
VisualState_DockedBottom = 3
VisualState_Closed = 4
__all__ = [
    "ALT_BREAKS",
    "ALT_BREAKS_FULL",
    "ALT_BREAKS_SAME",
    "ALT_BREAKS_UNIQUE",
    "ASYNC_RECO_ADDSTROKE_FAILED",
    "ASYNC_RECO_INTERRUPTED",
    "ASYNC_RECO_PROCESS_FAILED",
    "ASYNC_RECO_RESETCONTEXT_FAILED",
    "ASYNC_RECO_SETCACMODE_FAILED",
    "ASYNC_RECO_SETFACTOID_FAILED",
    "ASYNC_RECO_SETFLAGS_FAILED",
    "ASYNC_RECO_SETGUIDE_FAILED",
    "ASYNC_RECO_SETTEXTCONTEXT_FAILED",
    "ASYNC_RECO_SETWORDLIST_FAILED",
    "AddStroke",
    "AddWordsToWordList",
    "AdviseInkChange",
    "AppearanceConstants",
    "AppearanceConstants_rtfFlat",
    "AppearanceConstants_rtfThreeD",
    "BEST_COMPLETE",
    "BorderStyleConstants",
    "BorderStyleConstants_rtfFixedSingle",
    "BorderStyleConstants_rtfNoBorder",
    "CAC_FULL",
    "CAC_PREFIX",
    "CAC_RANDOM",
    "CFL_INTERMEDIATE",
    "CFL_POOR",
    "CFL_STRONG",
    "CHARACTER_RANGE",
    "CONFIDENCE_LEVEL",
    "CorrectionMode",
    "CorrectionMode_NotVisible",
    "CorrectionMode_PostInsertionCollapsed",
    "CorrectionMode_PostInsertionExpanded",
    "CorrectionMode_PreInsertion",
    "CorrectionPosition",
    "CorrectionPosition_Auto",
    "CorrectionPosition_Bottom",
    "CorrectionPosition_Top",
    "CreateContext",
    "CreateRecognizer",
    "DISPID_DAAntiAliased",
    "DISPID_DAClone",
    "DISPID_DAColor",
    "DISPID_DAExtendedProperties",
    "DISPID_DAFitToCurve",
    "DISPID_DAHeight",
    "DISPID_DAIgnorePressure",
    "DISPID_DAPenTip",
    "DISPID_DARasterOperation",
    "DISPID_DATransparency",
    "DISPID_DAWidth",
    "DISPID_DisableNoScroll",
    "DISPID_DragIcon",
    "DISPID_DrawAttr",
    "DISPID_Enabled",
    "DISPID_Factoid",
    "DISPID_GetGestStatus",
    "DISPID_Hwnd",
    "DISPID_IAddStrokesAtRectangle",
    "DISPID_ICAutoRedraw",
    "DISPID_ICBId",
    "DISPID_ICBName",
    "DISPID_ICBState",
    "DISPID_ICBsCount",
    "DISPID_ICBsItem",
    "DISPID_ICBs_NewEnum",
    "DISPID_ICCollectingInk",
    "DISPID_ICCollectionMode",
    "DISPID_ICCursors",
    "DISPID_ICDefaultDrawingAttributes",
    "DISPID_ICDesiredPacketDescription",
    "DISPID_ICDynamicRendering",
    "DISPID_ICECursorButtonDown",
    "DISPID_ICECursorButtonUp",
    "DISPID_ICECursorDown",
    "DISPID_ICECursorInRange",
    "DISPID_ICECursorOutOfRange",
    "DISPID_ICEGesture",
    "DISPID_ICENewInAirPackets",
    "DISPID_ICENewPackets",
    "DISPID_ICEStroke",
    "DISPID_ICESystemGesture",
    "DISPID_ICETabletAdded",
    "DISPID_ICETabletRemoved",
    "DISPID_ICEnabled",
    "DISPID_ICGetEventInterest",
    "DISPID_ICGetGestureStatus",
    "DISPID_ICGetWindowInputRectangle",
    "DISPID_ICHwnd",
    "DISPID_ICInk",
    "DISPID_ICMarginX",
    "DISPID_ICMarginY",
    "DISPID_ICMouseIcon",
    "DISPID_ICMousePointer",
    "DISPID_ICPaint",
    "DISPID_ICRenderer",
    "DISPID_ICSetAllTabletsMode",
    "DISPID_ICSetEventInterest",
    "DISPID_ICSetGestureStatus",
    "DISPID_ICSetSingleTabletIntegratedMode",
    "DISPID_ICSetWindowInputRectangle",
    "DISPID_ICSsAdd",
    "DISPID_ICSsClear",
    "DISPID_ICSsCount",
    "DISPID_ICSsItem",
    "DISPID_ICSsRemove",
    "DISPID_ICSs_NewEnum",
    "DISPID_ICSupportHighContrastInk",
    "DISPID_ICTablet",
    "DISPID_ICText",
    "DISPID_ICanPaste",
    "DISPID_IClip",
    "DISPID_IClipboardCopy",
    "DISPID_IClipboardCopyWithRectangle",
    "DISPID_IClipboardPaste",
    "DISPID_IClone",
    "DISPID_ICreateStroke",
    "DISPID_ICreateStrokeFromPoints",
    "DISPID_ICreateStrokes",
    "DISPID_ICsCount",
    "DISPID_ICsItem",
    "DISPID_ICs_NewEnum",
    "DISPID_ICsrButtons",
    "DISPID_ICsrDrawingAttributes",
    "DISPID_ICsrId",
    "DISPID_ICsrInverted",
    "DISPID_ICsrName",
    "DISPID_ICsrTablet",
    "DISPID_ICustomStrokes",
    "DISPID_IDeleteStroke",
    "DISPID_IDeleteStrokes",
    "DISPID_IDirty",
    "DISPID_IEInkAdded",
    "DISPID_IEInkDeleted",
    "DISPID_IEPData",
    "DISPID_IEPGuid",
    "DISPID_IEPsAdd",
    "DISPID_IEPsClear",
    "DISPID_IEPsCount",
    "DISPID_IEPsDoesPropertyExist",
    "DISPID_IEPsItem",
    "DISPID_IEPsRemove",
    "DISPID_IEPs_NewEnum",
    "DISPID_IExtendedProperties",
    "DISPID_IExtractStrokes",
    "DISPID_IExtractWithRectangle",
    "DISPID_IGConfidence",
    "DISPID_IGGetHotPoint",
    "DISPID_IGId",
    "DISPID_IGetBoundingBox",
    "DISPID_IHitTestCircle",
    "DISPID_IHitTestWithLasso",
    "DISPID_IHitTestWithRectangle",
    "DISPID_IInkDivider_Divide",
    "DISPID_IInkDivider_LineHeight",
    "DISPID_IInkDivider_RecognizerContext",
    "DISPID_IInkDivider_Strokes",
    "DISPID_IInkDivisionResult_ResultByType",
    "DISPID_IInkDivisionResult_Strokes",
    "DISPID_IInkDivisionUnit_DivisionType",
    "DISPID_IInkDivisionUnit_RecognizedString",
    "DISPID_IInkDivisionUnit_RotationTransform",
    "DISPID_IInkDivisionUnit_Strokes",
    "DISPID_IInkDivisionUnits_Count",
    "DISPID_IInkDivisionUnits_Item",
    "DISPID_IInkDivisionUnits_NewEnum",
    "DISPID_ILoad",
    "DISPID_INearestPoint",
    "DISPID_IOAttachMode",
    "DISPID_IODraw",
    "DISPID_IOEPainted",
    "DISPID_IOEPainting",
    "DISPID_IOESelectionChanged",
    "DISPID_IOESelectionChanging",
    "DISPID_IOESelectionMoved",
    "DISPID_IOESelectionMoving",
    "DISPID_IOESelectionResized",
    "DISPID_IOESelectionResizing",
    "DISPID_IOEStrokesDeleted",
    "DISPID_IOEStrokesDeleting",
    "DISPID_IOEditingMode",
    "DISPID_IOEraserMode",
    "DISPID_IOEraserWidth",
    "DISPID_IOHitTestSelection",
    "DISPID_IOSelection",
    "DISPID_IOSupportHighContrastSelectionUI",
    "DISPID_IPBackColor",
    "DISPID_IPEChangeUICues",
    "DISPID_IPEClick",
    "DISPID_IPEDblClick",
    "DISPID_IPEInvalidated",
    "DISPID_IPEKeyDown",
    "DISPID_IPEKeyPress",
    "DISPID_IPEKeyUp",
    "DISPID_IPEMouseDown",
    "DISPID_IPEMouseEnter",
    "DISPID_IPEMouseHover",
    "DISPID_IPEMouseLeave",
    "DISPID_IPEMouseMove",
    "DISPID_IPEMouseUp",
    "DISPID_IPEMouseWheel",
    "DISPID_IPEResize",
    "DISPID_IPESizeChanged",
    "DISPID_IPESizeModeChanged",
    "DISPID_IPEStyleChanged",
    "DISPID_IPESystemColorsChanged",
    "DISPID_IPInkEnabled",
    "DISPID_IPPicture",
    "DISPID_IPSizeMode",
    "DISPID_IRBottom",
    "DISPID_IRData",
    "DISPID_IRDraw",
    "DISPID_IRDrawStroke",
    "DISPID_IRERecognition",
    "DISPID_IRERecognitionWithAlternates",
    "DISPID_IRGColumns",
    "DISPID_IRGDrawnBox",
    "DISPID_IRGGuideData",
    "DISPID_IRGMidline",
    "DISPID_IRGRows",
    "DISPID_IRGWritingBox",
    "DISPID_IRGetObjectTransform",
    "DISPID_IRGetRectangle",
    "DISPID_IRGetViewTransform",
    "DISPID_IRInkSpaceToPixel",
    "DISPID_IRInkSpaceToPixelFromPoints",
    "DISPID_IRLeft",
    "DISPID_IRMeasure",
    "DISPID_IRMeasureStroke",
    "DISPID_IRMove",
    "DISPID_IRPixelToInkSpace",
    "DISPID_IRPixelToInkSpaceFromPoints",
    "DISPID_IRRight",
    "DISPID_IRRotate",
    "DISPID_IRScale",
    "DISPID_IRSetObjectTransform",
    "DISPID_IRSetRectangle",
    "DISPID_IRSetViewTransform",
    "DISPID_IRTop",
    "DISPID_IRecoCtx2_EnabledUnicodeRanges",
    "DISPID_IRecoCtx_BackgroundRecognize",
    "DISPID_IRecoCtx_BackgroundRecognizeWithAlternates",
    "DISPID_IRecoCtx_CharacterAutoCompletionMode",
    "DISPID_IRecoCtx_Clone",
    "DISPID_IRecoCtx_EndInkInput",
    "DISPID_IRecoCtx_Factoid",
    "DISPID_IRecoCtx_Flags",
    "DISPID_IRecoCtx_Guide",
    "DISPID_IRecoCtx_IsStringSupported",
    "DISPID_IRecoCtx_PrefixText",
    "DISPID_IRecoCtx_Recognize",
    "DISPID_IRecoCtx_Recognizer",
    "DISPID_IRecoCtx_StopBackgroundRecognition",
    "DISPID_IRecoCtx_StopRecognition",
    "DISPID_IRecoCtx_Strokes",
    "DISPID_IRecoCtx_SuffixText",
    "DISPID_IRecoCtx_WordList",
    "DISPID_IRecosCount",
    "DISPID_IRecosGetDefaultRecognizer",
    "DISPID_IRecosItem",
    "DISPID_IRecos_NewEnum",
    "DISPID_ISDBezierCusps",
    "DISPID_ISDBezierPoints",
    "DISPID_ISDClip",
    "DISPID_ISDDeleted",
    "DISPID_ISDDrawingAttributes",
    "DISPID_ISDExtendedProperties",
    "DISPID_ISDFindIntersections",
    "DISPID_ISDGetBoundingBox",
    "DISPID_ISDGetFlattenedBezierPoints",
    "DISPID_ISDGetPacketData",
    "DISPID_ISDGetPacketDescriptionPropertyMetrics",
    "DISPID_ISDGetPacketValuesByProperty",
    "DISPID_ISDGetPoints",
    "DISPID_ISDGetRectangleIntersections",
    "DISPID_ISDHitTestCircle",
    "DISPID_ISDID",
    "DISPID_ISDInk",
    "DISPID_ISDInkIndex",
    "DISPID_ISDMove",
    "DISPID_ISDNearestPoint",
    "DISPID_ISDPacketCount",
    "DISPID_ISDPacketDescription",
    "DISPID_ISDPacketSize",
    "DISPID_ISDPolylineCusps",
    "DISPID_ISDRotate",
    "DISPID_ISDScale",
    "DISPID_ISDScaleToRectangle",
    "DISPID_ISDSelfIntersections",
    "DISPID_ISDSetPacketValuesByProperty",
    "DISPID_ISDSetPoints",
    "DISPID_ISDShear",
    "DISPID_ISDSplit",
    "DISPID_ISDTransform",
    "DISPID_ISave",
    "DISPID_ISsAdd",
    "DISPID_ISsAddStrokes",
    "DISPID_ISsClip",
    "DISPID_ISsCount",
    "DISPID_ISsGetBoundingBox",
    "DISPID_ISsInk",
    "DISPID_ISsItem",
    "DISPID_ISsModifyDrawingAttributes",
    "DISPID_ISsMove",
    "DISPID_ISsRecognitionResult",
    "DISPID_ISsRemove",
    "DISPID_ISsRemoveRecognitionResult",
    "DISPID_ISsRemoveStrokes",
    "DISPID_ISsRotate",
    "DISPID_ISsScale",
    "DISPID_ISsScaleToRectangle",
    "DISPID_ISsShear",
    "DISPID_ISsToString",
    "DISPID_ISsTransform",
    "DISPID_ISsValid",
    "DISPID_ISs_NewEnum",
    "DISPID_IStrokes",
    "DISPID_IT2DeviceKind",
    "DISPID_IT3IsMultiTouch",
    "DISPID_IT3MaximumCursors",
    "DISPID_ITData",
    "DISPID_ITGetTransform",
    "DISPID_ITHardwareCapabilities",
    "DISPID_ITIsPacketPropertySupported",
    "DISPID_ITMaximumInputRectangle",
    "DISPID_ITName",
    "DISPID_ITPlugAndPlayId",
    "DISPID_ITPropertyMetrics",
    "DISPID_ITReflect",
    "DISPID_ITReset",
    "DISPID_ITRotate",
    "DISPID_ITScale",
    "DISPID_ITSetTransform",
    "DISPID_ITShear",
    "DISPID_ITTranslate",
    "DISPID_ITeDx",
    "DISPID_ITeDy",
    "DISPID_ITeM11",
    "DISPID_ITeM12",
    "DISPID_ITeM21",
    "DISPID_ITeM22",
    "DISPID_ITsCount",
    "DISPID_ITsDefaultTablet",
    "DISPID_ITsIsPacketPropertySupported",
    "DISPID_ITsItem",
    "DISPID_ITs_NewEnum",
    "DISPID_IeeChange",
    "DISPID_IeeClick",
    "DISPID_IeeCursorDown",
    "DISPID_IeeDblClick",
    "DISPID_IeeGesture",
    "DISPID_IeeKeyDown",
    "DISPID_IeeKeyPress",
    "DISPID_IeeKeyUp",
    "DISPID_IeeMouseDown",
    "DISPID_IeeMouseMove",
    "DISPID_IeeMouseUp",
    "DISPID_IeeRecognitionResult",
    "DISPID_IeeSelChange",
    "DISPID_IeeStroke",
    "DISPID_Ink",
    "DISPID_InkCollector",
    "DISPID_InkCollectorEvent",
    "DISPID_InkCursor",
    "DISPID_InkCursorButton",
    "DISPID_InkCursorButtons",
    "DISPID_InkCursors",
    "DISPID_InkCustomStrokes",
    "DISPID_InkDivider",
    "DISPID_InkDivisionResult",
    "DISPID_InkDivisionUnit",
    "DISPID_InkDivisionUnits",
    "DISPID_InkDrawingAttributes",
    "DISPID_InkEdit",
    "DISPID_InkEditEvents",
    "DISPID_InkEvent",
    "DISPID_InkExtendedProperties",
    "DISPID_InkExtendedProperty",
    "DISPID_InkGesture",
    "DISPID_InkInsertMode",
    "DISPID_InkMode",
    "DISPID_InkRecoAlternate",
    "DISPID_InkRecoAlternate_AlternatesWithConstantPropertyValues",
    "DISPID_InkRecoAlternate_Ascender",
    "DISPID_InkRecoAlternate_Baseline",
    "DISPID_InkRecoAlternate_Confidence",
    "DISPID_InkRecoAlternate_ConfidenceAlternates",
    "DISPID_InkRecoAlternate_Descender",
    "DISPID_InkRecoAlternate_GetPropertyValue",
    "DISPID_InkRecoAlternate_GetStrokesFromStrokeRanges",
    "DISPID_InkRecoAlternate_GetStrokesFromTextRange",
    "DISPID_InkRecoAlternate_GetTextRangeFromStrokes",
    "DISPID_InkRecoAlternate_LineAlternates",
    "DISPID_InkRecoAlternate_LineNumber",
    "DISPID_InkRecoAlternate_Midline",
    "DISPID_InkRecoAlternate_String",
    "DISPID_InkRecoAlternate_Strokes",
    "DISPID_InkRecoContext",
    "DISPID_InkRecoContext2",
    "DISPID_InkRecognitionAlternates",
    "DISPID_InkRecognitionAlternates_Count",
    "DISPID_InkRecognitionAlternates_Item",
    "DISPID_InkRecognitionAlternates_NewEnum",
    "DISPID_InkRecognitionAlternates_Strokes",
    "DISPID_InkRecognitionEvent",
    "DISPID_InkRecognitionResult",
    "DISPID_InkRecognitionResult_AlternatesFromSelection",
    "DISPID_InkRecognitionResult_ModifyTopAlternate",
    "DISPID_InkRecognitionResult_SetResultOnStrokes",
    "DISPID_InkRecognitionResult_Strokes",
    "DISPID_InkRecognitionResult_TopAlternate",
    "DISPID_InkRecognitionResult_TopConfidence",
    "DISPID_InkRecognitionResult_TopString",
    "DISPID_InkRecognizer",
    "DISPID_InkRecognizer2",
    "DISPID_InkRecognizerGuide",
    "DISPID_InkRecognizers",
    "DISPID_InkRectangle",
    "DISPID_InkRenderer",
    "DISPID_InkStrokeDisp",
    "DISPID_InkStrokes",
    "DISPID_InkTablet",
    "DISPID_InkTablet2",
    "DISPID_InkTablet3",
    "DISPID_InkTablets",
    "DISPID_InkTransform",
    "DISPID_InkWordList",
    "DISPID_InkWordList2",
    "DISPID_InkWordList2_AddWords",
    "DISPID_InkWordList_AddWord",
    "DISPID_InkWordList_Merge",
    "DISPID_InkWordList_RemoveWord",
    "DISPID_Locked",
    "DISPID_MICClear",
    "DISPID_MICClose",
    "DISPID_MICInsert",
    "DISPID_MICPaint",
    "DISPID_MathInputControlEvents",
    "DISPID_MaxLength",
    "DISPID_MultiLine",
    "DISPID_PIPAttachedEditWindow",
    "DISPID_PIPAutoShow",
    "DISPID_PIPBusy",
    "DISPID_PIPCommitPendingInput",
    "DISPID_PIPCurrentPanel",
    "DISPID_PIPDefaultPanel",
    "DISPID_PIPEInputFailed",
    "DISPID_PIPEPanelChanged",
    "DISPID_PIPEPanelMoving",
    "DISPID_PIPEVisibleChanged",
    "DISPID_PIPEnableTsf",
    "DISPID_PIPFactoid",
    "DISPID_PIPHeight",
    "DISPID_PIPHorizontalOffset",
    "DISPID_PIPLeft",
    "DISPID_PIPMoveTo",
    "DISPID_PIPRefresh",
    "DISPID_PIPTop",
    "DISPID_PIPVerticalOffset",
    "DISPID_PIPVisible",
    "DISPID_PIPWidth",
    "DISPID_PenInputPanel",
    "DISPID_PenInputPanelEvents",
    "DISPID_RTSelLength",
    "DISPID_RTSelStart",
    "DISPID_RTSelText",
    "DISPID_RecoCapabilities",
    "DISPID_RecoClsid",
    "DISPID_RecoCreateRecognizerContext",
    "DISPID_RecoId",
    "DISPID_RecoLanguageID",
    "DISPID_RecoName",
    "DISPID_RecoPreferredPacketDescription",
    "DISPID_RecoSupportedProperties",
    "DISPID_RecoTimeout",
    "DISPID_RecoUnicodeRanges",
    "DISPID_RecoVendor",
    "DISPID_Recognize",
    "DISPID_Recognizer",
    "DISPID_Refresh",
    "DISPID_SEStrokesAdded",
    "DISPID_SEStrokesRemoved",
    "DISPID_ScrollBars",
    "DISPID_SelAlignment",
    "DISPID_SelBold",
    "DISPID_SelCharOffset",
    "DISPID_SelColor",
    "DISPID_SelFontName",
    "DISPID_SelFontSize",
    "DISPID_SelInk",
    "DISPID_SelInksDisplayMode",
    "DISPID_SelItalic",
    "DISPID_SelRTF",
    "DISPID_SelUnderline",
    "DISPID_SetGestStatus",
    "DISPID_Status",
    "DISPID_StrokeEvent",
    "DISPID_Text",
    "DISPID_TextRTF",
    "DISPID_UseMouseForInput",
    "DYNAMIC_RENDERER_CACHED_DATA",
    "DestroyContext",
    "DestroyRecognizer",
    "DestroyWordList",
    "DynamicRenderer",
    "EM_GETDRAWATTR",
    "EM_GETFACTOID",
    "EM_GETGESTURESTATUS",
    "EM_GETINKINSERTMODE",
    "EM_GETINKMODE",
    "EM_GETMOUSEICON",
    "EM_GETMOUSEPOINTER",
    "EM_GETRECOGNIZER",
    "EM_GETRECOTIMEOUT",
    "EM_GETSELINK",
    "EM_GETSELINKDISPLAYMODE",
    "EM_GETSTATUS",
    "EM_GETUSEMOUSEFORINPUT",
    "EM_RECOGNIZE",
    "EM_SETDRAWATTR",
    "EM_SETFACTOID",
    "EM_SETGESTURESTATUS",
    "EM_SETINKINSERTMODE",
    "EM_SETINKMODE",
    "EM_SETMOUSEICON",
    "EM_SETMOUSEPOINTER",
    "EM_SETRECOGNIZER",
    "EM_SETRECOTIMEOUT",
    "EM_SETSELINK",
    "EM_SETSELINKDISPLAYMODE",
    "EM_SETUSEMOUSEFORINPUT",
    "EndInkInput",
    "EventMask",
    "EventMask_All",
    "EventMask_CorrectionModeChanged",
    "EventMask_CorrectionModeChanging",
    "EventMask_InPlaceSizeChanged",
    "EventMask_InPlaceSizeChanging",
    "EventMask_InPlaceStateChanged",
    "EventMask_InPlaceStateChanging",
    "EventMask_InPlaceVisibilityChanged",
    "EventMask_InPlaceVisibilityChanging",
    "EventMask_InputAreaChanged",
    "EventMask_InputAreaChanging",
    "EventMask_TextInserted",
    "EventMask_TextInserting",
    "FACILITY_INK",
    "FACTOID_BOPOMOFO",
    "FACTOID_CHINESESIMPLECOMMON",
    "FACTOID_CHINESETRADITIONALCOMMON",
    "FACTOID_CURRENCY",
    "FACTOID_DATE",
    "FACTOID_DEFAULT",
    "FACTOID_DIGIT",
    "FACTOID_EMAIL",
    "FACTOID_FILENAME",
    "FACTOID_HANGULCOMMON",
    "FACTOID_HANGULRARE",
    "FACTOID_HIRAGANA",
    "FACTOID_JAMO",
    "FACTOID_JAPANESECOMMON",
    "FACTOID_KANJICOMMON",
    "FACTOID_KANJIRARE",
    "FACTOID_KATAKANA",
    "FACTOID_KOREANCOMMON",
    "FACTOID_LOWERCHAR",
    "FACTOID_NONE",
    "FACTOID_NUMBER",
    "FACTOID_NUMBERSIMPLE",
    "FACTOID_ONECHAR",
    "FACTOID_PERCENT",
    "FACTOID_POSTALCODE",
    "FACTOID_PUNCCHAR",
    "FACTOID_SYSTEMDICTIONARY",
    "FACTOID_TELEPHONE",
    "FACTOID_TIME",
    "FACTOID_UPPERCHAR",
    "FACTOID_WEB",
    "FACTOID_WORDLIST",
    "FLICKACTION_COMMANDCODE",
    "FLICKACTION_COMMANDCODE_APPCOMMAND",
    "FLICKACTION_COMMANDCODE_CUSTOMKEY",
    "FLICKACTION_COMMANDCODE_KEYMODIFIER",
    "FLICKACTION_COMMANDCODE_NULL",
    "FLICKACTION_COMMANDCODE_SCROLL",
    "FLICKDIRECTION",
    "FLICKDIRECTION_DOWN",
    "FLICKDIRECTION_DOWNLEFT",
    "FLICKDIRECTION_DOWNRIGHT",
    "FLICKDIRECTION_INVALID",
    "FLICKDIRECTION_LEFT",
    "FLICKDIRECTION_MIN",
    "FLICKDIRECTION_RIGHT",
    "FLICKDIRECTION_UP",
    "FLICKDIRECTION_UPLEFT",
    "FLICKDIRECTION_UPRIGHT",
    "FLICKMODE",
    "FLICKMODE_DEFAULT",
    "FLICKMODE_LEARNING",
    "FLICKMODE_MAX",
    "FLICKMODE_MIN",
    "FLICKMODE_OFF",
    "FLICKMODE_ON",
    "FLICK_DATA",
    "FLICK_POINT",
    "FLICK_WM_HANDLED_MASK",
    "GESTURE_ARROW_DOWN",
    "GESTURE_ARROW_LEFT",
    "GESTURE_ARROW_RIGHT",
    "GESTURE_ARROW_UP",
    "GESTURE_ASTERISK",
    "GESTURE_BRACE_LEFT",
    "GESTURE_BRACE_OVER",
    "GESTURE_BRACE_RIGHT",
    "GESTURE_BRACE_UNDER",
    "GESTURE_BRACKET_LEFT",
    "GESTURE_BRACKET_OVER",
    "GESTURE_BRACKET_RIGHT",
    "GESTURE_BRACKET_UNDER",
    "GESTURE_BULLET",
    "GESTURE_BULLET_CROSS",
    "GESTURE_CHECK",
    "GESTURE_CHEVRON_DOWN",
    "GESTURE_CHEVRON_LEFT",
    "GESTURE_CHEVRON_RIGHT",
    "GESTURE_CHEVRON_UP",
    "GESTURE_CIRCLE",
    "GESTURE_CIRCLE_CIRCLE",
    "GESTURE_CIRCLE_CROSS",
    "GESTURE_CIRCLE_LINE_HORZ",
    "GESTURE_CIRCLE_LINE_VERT",
    "GESTURE_CIRCLE_TAP",
    "GESTURE_CLOSEUP",
    "GESTURE_CROSS",
    "GESTURE_CURLICUE",
    "GESTURE_DATA",
    "GESTURE_DIAGONAL_LEFTDOWN",
    "GESTURE_DIAGONAL_LEFTUP",
    "GESTURE_DIAGONAL_RIGHTDOWN",
    "GESTURE_DIAGONAL_RIGHTUP",
    "GESTURE_DIGIT_0",
    "GESTURE_DIGIT_1",
    "GESTURE_DIGIT_2",
    "GESTURE_DIGIT_3",
    "GESTURE_DIGIT_4",
    "GESTURE_DIGIT_5",
    "GESTURE_DIGIT_6",
    "GESTURE_DIGIT_7",
    "GESTURE_DIGIT_8",
    "GESTURE_DIGIT_9",
    "GESTURE_DOLLAR",
    "GESTURE_DOUBLE_ARROW_DOWN",
    "GESTURE_DOUBLE_ARROW_LEFT",
    "GESTURE_DOUBLE_ARROW_RIGHT",
    "GESTURE_DOUBLE_ARROW_UP",
    "GESTURE_DOUBLE_CIRCLE",
    "GESTURE_DOUBLE_CURLICUE",
    "GESTURE_DOUBLE_DOWN",
    "GESTURE_DOUBLE_LEFT",
    "GESTURE_DOUBLE_RIGHT",
    "GESTURE_DOUBLE_TAP",
    "GESTURE_DOUBLE_UP",
    "GESTURE_DOWN",
    "GESTURE_DOWN_ARROW_LEFT",
    "GESTURE_DOWN_ARROW_RIGHT",
    "GESTURE_DOWN_LEFT",
    "GESTURE_DOWN_LEFT_LONG",
    "GESTURE_DOWN_RIGHT",
    "GESTURE_DOWN_RIGHT_LONG",
    "GESTURE_DOWN_UP",
    "GESTURE_EXCLAMATION",
    "GESTURE_INFINITY",
    "GESTURE_LEFT",
    "GESTURE_LEFT_ARROW_DOWN",
    "GESTURE_LEFT_ARROW_UP",
    "GESTURE_LEFT_DOWN",
    "GESTURE_LEFT_RIGHT",
    "GESTURE_LEFT_UP",
    "GESTURE_LETTER_A",
    "GESTURE_LETTER_B",
    "GESTURE_LETTER_C",
    "GESTURE_LETTER_D",
    "GESTURE_LETTER_E",
    "GESTURE_LETTER_F",
    "GESTURE_LETTER_G",
    "GESTURE_LETTER_H",
    "GESTURE_LETTER_I",
    "GESTURE_LETTER_J",
    "GESTURE_LETTER_K",
    "GESTURE_LETTER_L",
    "GESTURE_LETTER_M",
    "GESTURE_LETTER_N",
    "GESTURE_LETTER_O",
    "GESTURE_LETTER_P",
    "GESTURE_LETTER_Q",
    "GESTURE_LETTER_R",
    "GESTURE_LETTER_S",
    "GESTURE_LETTER_T",
    "GESTURE_LETTER_U",
    "GESTURE_LETTER_V",
    "GESTURE_LETTER_W",
    "GESTURE_LETTER_X",
    "GESTURE_LETTER_Y",
    "GESTURE_LETTER_Z",
    "GESTURE_NULL",
    "GESTURE_OPENUP",
    "GESTURE_PARAGRAPH",
    "GESTURE_PLUS",
    "GESTURE_QUAD_TAP",
    "GESTURE_QUESTION",
    "GESTURE_RECTANGLE",
    "GESTURE_RIGHT",
    "GESTURE_RIGHT_ARROW_DOWN",
    "GESTURE_RIGHT_ARROW_UP",
    "GESTURE_RIGHT_DOWN",
    "GESTURE_RIGHT_LEFT",
    "GESTURE_RIGHT_UP",
    "GESTURE_SCRATCHOUT",
    "GESTURE_SECTION",
    "GESTURE_SEMICIRCLE_LEFT",
    "GESTURE_SEMICIRCLE_RIGHT",
    "GESTURE_SHARP",
    "GESTURE_SQUARE",
    "GESTURE_SQUIGGLE",
    "GESTURE_STAR",
    "GESTURE_SWAP",
    "GESTURE_TAP",
    "GESTURE_TRIANGLE",
    "GESTURE_TRIPLE_DOWN",
    "GESTURE_TRIPLE_LEFT",
    "GESTURE_TRIPLE_RIGHT",
    "GESTURE_TRIPLE_TAP",
    "GESTURE_TRIPLE_UP",
    "GESTURE_UP",
    "GESTURE_UP_ARROW_LEFT",
    "GESTURE_UP_ARROW_RIGHT",
    "GESTURE_UP_DOWN",
    "GESTURE_UP_LEFT",
    "GESTURE_UP_LEFT_LONG",
    "GESTURE_UP_RIGHT",
    "GESTURE_UP_RIGHT_LONG",
    "GET_DANDIDATE_FLAGS",
    "GUID_DYNAMIC_RENDERER_CACHED_DATA",
    "GUID_GESTURE_DATA",
    "GUID_PACKETPROPERTY_GUID_ALTITUDE_ORIENTATION",
    "GUID_PACKETPROPERTY_GUID_AZIMUTH_ORIENTATION",
    "GUID_PACKETPROPERTY_GUID_BUTTON_PRESSURE",
    "GUID_PACKETPROPERTY_GUID_DEVICE_CONTACT_ID",
    "GUID_PACKETPROPERTY_GUID_FINGERCONTACTCONFIDENCE",
    "GUID_PACKETPROPERTY_GUID_HEIGHT",
    "GUID_PACKETPROPERTY_GUID_NORMAL_PRESSURE",
    "GUID_PACKETPROPERTY_GUID_PACKET_STATUS",
    "GUID_PACKETPROPERTY_GUID_PITCH_ROTATION",
    "GUID_PACKETPROPERTY_GUID_ROLL_ROTATION",
    "GUID_PACKETPROPERTY_GUID_SERIAL_NUMBER",
    "GUID_PACKETPROPERTY_GUID_TANGENT_PRESSURE",
    "GUID_PACKETPROPERTY_GUID_TIMER_TICK",
    "GUID_PACKETPROPERTY_GUID_TWIST_ORIENTATION",
    "GUID_PACKETPROPERTY_GUID_WIDTH",
    "GUID_PACKETPROPERTY_GUID_X",
    "GUID_PACKETPROPERTY_GUID_X_TILT_ORIENTATION",
    "GUID_PACKETPROPERTY_GUID_Y",
    "GUID_PACKETPROPERTY_GUID_YAW_ROTATION",
    "GUID_PACKETPROPERTY_GUID_Y_TILT_ORIENTATION",
    "GUID_PACKETPROPERTY_GUID_Z",
    "GestureRecognizer",
    "GetAllRecognizers",
    "GetBestResultString",
    "GetLatticePtr",
    "GetLeftSeparator",
    "GetRecoAttributes",
    "GetResultPropertyList",
    "GetRightSeparator",
    "GetUnicodeRanges",
    "HRECOALT",
    "HRECOCONTEXT",
    "HRECOGNIZER",
    "HRECOLATTICE",
    "HRECOWORDLIST",
    "HandwrittenTextInsertion",
    "IAG_AllGestures",
    "IAG_ArrowDown",
    "IAG_ArrowLeft",
    "IAG_ArrowRight",
    "IAG_ArrowUp",
    "IAG_Check",
    "IAG_ChevronDown",
    "IAG_ChevronLeft",
    "IAG_ChevronRight",
    "IAG_ChevronUp",
    "IAG_Circle",
    "IAG_Curlicue",
    "IAG_DoubleCircle",
    "IAG_DoubleCurlicue",
    "IAG_DoubleTap",
    "IAG_Down",
    "IAG_DownLeft",
    "IAG_DownLeftLong",
    "IAG_DownRight",
    "IAG_DownRightLong",
    "IAG_DownUp",
    "IAG_Exclamation",
    "IAG_Left",
    "IAG_LeftDown",
    "IAG_LeftRight",
    "IAG_LeftUp",
    "IAG_NoGesture",
    "IAG_Right",
    "IAG_RightDown",
    "IAG_RightLeft",
    "IAG_RightUp",
    "IAG_Scratchout",
    "IAG_SemiCircleLeft",
    "IAG_SemiCircleRight",
    "IAG_Square",
    "IAG_Star",
    "IAG_Tap",
    "IAG_Triangle",
    "IAG_Up",
    "IAG_UpDown",
    "IAG_UpLeft",
    "IAG_UpLeftLong",
    "IAG_UpRight",
    "IAG_UpRightLong",
    "IBBM_CurveFit",
    "IBBM_Default",
    "IBBM_NoCurveFit",
    "IBBM_PointsOnly",
    "IBBM_Union",
    "ICBS_Down",
    "ICBS_Unavailable",
    "ICBS_Up",
    "ICB_Copy",
    "ICB_Cut",
    "ICB_Default",
    "ICB_DelayedCopy",
    "ICB_ExtractOnly",
    "ICEI_AllEvents",
    "ICEI_CursorButtonDown",
    "ICEI_CursorButtonUp",
    "ICEI_CursorDown",
    "ICEI_CursorInRange",
    "ICEI_CursorOutOfRange",
    "ICEI_DblClick",
    "ICEI_DefaultEvents",
    "ICEI_MouseDown",
    "ICEI_MouseMove",
    "ICEI_MouseUp",
    "ICEI_MouseWheel",
    "ICEI_NewInAirPackets",
    "ICEI_NewPackets",
    "ICEI_Stroke",
    "ICEI_SystemGesture",
    "ICEI_TabletAdded",
    "ICEI_TabletRemoved",
    "ICF_Bitmap",
    "ICF_CopyMask",
    "ICF_Default",
    "ICF_EnhancedMetafile",
    "ICF_InkSerializedFormat",
    "ICF_Metafile",
    "ICF_None",
    "ICF_PasteMask",
    "ICF_SketchInk",
    "ICF_TextInk",
    "ICM_GestureOnly",
    "ICM_InkAndGesture",
    "ICM_InkOnly",
    "IDM_Ink",
    "IDM_Text",
    "IDT_Drawing",
    "IDT_Line",
    "IDT_Paragraph",
    "IDT_Segment",
    "IDynamicRenderer",
    "IECN_GESTURE",
    "IECN_RECOGNITIONRESULT",
    "IECN_STROKE",
    "IECN__BASE",
    "IEC_GESTUREINFO",
    "IEC_RECOGNITIONRESULTINFO",
    "IEC_STROKEINFO",
    "IEC__BASE",
    "IEF_CopyFromOriginal",
    "IEF_Default",
    "IEF_RemoveFromOriginal",
    "IEM_Disabled",
    "IEM_Ink",
    "IEM_InkAndGesture",
    "IEM_InsertInk",
    "IEM_InsertText",
    "IES_Collecting",
    "IES_Idle",
    "IES_Recognizing",
    "IGestureRecognizer",
    "IHandwrittenTextInsertion",
    "IInk",
    "IInkCollector",
    "IInkCursor",
    "IInkCursorButton",
    "IInkCursorButtons",
    "IInkCursors",
    "IInkCustomStrokes",
    "IInkDisp",
    "IInkDivider",
    "IInkDivisionResult",
    "IInkDivisionUnit",
    "IInkDivisionUnits",
    "IInkDrawingAttributes",
    "IInkEdit",
    "IInkExtendedProperties",
    "IInkExtendedProperty",
    "IInkGesture",
    "IInkLineInfo",
    "IInkOverlay",
    "IInkPicture",
    "IInkRecognitionAlternate",
    "IInkRecognitionAlternates",
    "IInkRecognitionResult",
    "IInkRecognizer",
    "IInkRecognizer2",
    "IInkRecognizerContext",
    "IInkRecognizerContext2",
    "IInkRecognizerGuide",
    "IInkRecognizers",
    "IInkRectangle",
    "IInkRenderer",
    "IInkStrokeDisp",
    "IInkStrokes",
    "IInkTablet",
    "IInkTablet2",
    "IInkTablet3",
    "IInkTablets",
    "IInkTransform",
    "IInkWordList",
    "IInkWordList2",
    "IInputPanelWindowHandle",
    "IKM_Alt",
    "IKM_Control",
    "IKM_Shift",
    "IMF_BOLD",
    "IMF_FONT_SELECTED_IN_HDC",
    "IMF_ITALIC",
    "IMF_Left",
    "IMF_Middle",
    "IMF_Right",
    "IMP_Arrow",
    "IMP_ArrowHourglass",
    "IMP_ArrowQuestion",
    "IMP_Crosshair",
    "IMP_Custom",
    "IMP_Default",
    "IMP_Hand",
    "IMP_Hourglass",
    "IMP_Ibeam",
    "IMP_NoDrop",
    "IMP_SizeAll",
    "IMP_SizeNESW",
    "IMP_SizeNS",
    "IMP_SizeNWSE",
    "IMP_SizeWE",
    "IMP_UpArrow",
    "IMathInputControl",
    "INKEDIT_CLASS",
    "INKEDIT_CLASSW",
    "INKMETRIC",
    "INKRECOGNITIONPROPERTY_BOXNUMBER",
    "INKRECOGNITIONPROPERTY_CONFIDENCELEVEL",
    "INKRECOGNITIONPROPERTY_HOTPOINT",
    "INKRECOGNITIONPROPERTY_LINEMETRICS",
    "INKRECOGNITIONPROPERTY_LINENUMBER",
    "INKRECOGNITIONPROPERTY_MAXIMUMSTROKECOUNT",
    "INKRECOGNITIONPROPERTY_POINTSPERINCH",
    "INKRECOGNITIONPROPERTY_SEGMENTATION",
    "INK_METRIC_FLAGS",
    "INK_SERIALIZED_FORMAT",
    "IOAM_Behind",
    "IOAM_InFront",
    "IOEM_Delete",
    "IOEM_Ink",
    "IOEM_Select",
    "IOERM_PointErase",
    "IOERM_StrokeErase",
    "IPCM_Default",
    "IPCM_MaximumCompression",
    "IPCM_NoCompression",
    "IPF_Base64GIF",
    "IPF_Base64InkSerializedFormat",
    "IPF_GIF",
    "IPF_InkSerializedFormat",
    "IPSM_AutoSize",
    "IPSM_CenterImage",
    "IPSM_Normal",
    "IPSM_StretchImage",
    "IPT_Ball",
    "IPT_Rectangle",
    "IP_CURSOR_DOWN",
    "IP_INVERTED",
    "IP_MARGIN",
    "IPenInputPanel",
    "IRAS_All",
    "IRAS_DefaultCount",
    "IRAS_Start",
    "IRCACM_Full",
    "IRCACM_Prefix",
    "IRCACM_Random",
    "IRC_AdviseInkChange",
    "IRC_Alpha",
    "IRC_ArbitraryAngle",
    "IRC_Beta",
    "IRC_BoxedInput",
    "IRC_CharacterAutoCompletionInput",
    "IRC_Cursive",
    "IRC_DontCare",
    "IRC_DownAndLeft",
    "IRC_DownAndRight",
    "IRC_FreeInput",
    "IRC_Intermediate",
    "IRC_Lattice",
    "IRC_LeftAndDown",
    "IRC_LinedInput",
    "IRC_Object",
    "IRC_Personalizable",
    "IRC_Poor",
    "IRC_PrefersArbitraryAngle",
    "IRC_PrefersParagraphBreaking",
    "IRC_PrefersSegmentation",
    "IRC_RightAndDown",
    "IRC_StrokeReorder",
    "IRC_Strong",
    "IRC_TextPrediction",
    "IRM_AutoSpace",
    "IRM_Coerce",
    "IRM_DisablePersonalization",
    "IRM_LineMode",
    "IRM_Max",
    "IRM_None",
    "IRM_PrefixOk",
    "IRM_TopInkBreaksOnly",
    "IRM_WordModeOnly",
    "IRO_Black",
    "IRO_CopyPen",
    "IRO_MaskNotPen",
    "IRO_MaskPen",
    "IRO_MaskPenNot",
    "IRO_MergeNotPen",
    "IRO_MergePen",
    "IRO_MergePenNot",
    "IRO_NoOperation",
    "IRO_Not",
    "IRO_NotCopyPen",
    "IRO_NotMaskPen",
    "IRO_NotMergePen",
    "IRO_NotXOrPen",
    "IRO_White",
    "IRO_XOrPen",
    "IRS_InkAddedFailed",
    "IRS_Interrupted",
    "IRS_NoError",
    "IRS_ProcessFailed",
    "IRS_SetAutoCompletionModeFailed",
    "IRS_SetFactoidFailed",
    "IRS_SetFlagsFailed",
    "IRS_SetGuideFailed",
    "IRS_SetPrefixSuffixFailed",
    "IRS_SetStrokesFailed",
    "IRS_SetWordListFailed",
    "IRealTimeStylus",
    "IRealTimeStylus2",
    "IRealTimeStylus3",
    "IRealTimeStylusSynchronization",
    "ISC_AllElements",
    "ISC_FirstElement",
    "ISG_DoubleTap",
    "ISG_Drag",
    "ISG_Flick",
    "ISG_HoldEnter",
    "ISG_HoldLeave",
    "ISG_HoverEnter",
    "ISG_HoverLeave",
    "ISG_RightDrag",
    "ISG_RightTap",
    "ISG_Tap",
    "ISketchInk",
    "IStrokeBuilder",
    "IStylusAsyncPlugin",
    "IStylusPlugin",
    "IStylusSyncPlugin",
    "ITextInputPanel",
    "ITextInputPanelEventSink",
    "ITextInputPanelRunInfo",
    "ITipAutoCompleteClient",
    "ITipAutoCompleteProvider",
    "InPlaceDirection",
    "InPlaceDirection_Auto",
    "InPlaceDirection_Bottom",
    "InPlaceDirection_Top",
    "InPlaceState",
    "InPlaceState_Auto",
    "InPlaceState_Expanded",
    "InPlaceState_HoverTarget",
    "Ink",
    "InkApplicationGesture",
    "InkBoundingBoxMode",
    "InkClipboardFormats",
    "InkClipboardModes",
    "InkCollectionMode",
    "InkCollector",
    "InkCollectorClipInkToMargin",
    "InkCollectorDefaultMargin",
    "InkCollectorEventInterest",
    "InkCursorButtonState",
    "InkDisp",
    "InkDisplayMode",
    "InkDivider",
    "InkDivisionType",
    "InkDrawingAttributes",
    "InkEdit",
    "InkEditStatus",
    "InkExtractFlags",
    "InkInsertMode",
    "InkMaxTransparencyValue",
    "InkMinTransparencyValue",
    "InkMode",
    "InkMouseButton",
    "InkMousePointer",
    "InkOverlay",
    "InkOverlayAttachMode",
    "InkOverlayEditingMode",
    "InkOverlayEraserMode",
    "InkPenTip",
    "InkPersistenceCompressionMode",
    "InkPersistenceFormat",
    "InkPicture",
    "InkPictureSizeMode",
    "InkRasterOperation",
    "InkRecoGuide",
    "InkRecognitionAlternatesSelection",
    "InkRecognitionConfidence",
    "InkRecognitionModes",
    "InkRecognitionStatus",
    "InkRecognizerCapabilities",
    "InkRecognizerCharacterAutoCompletionMode",
    "InkRecognizerContext",
    "InkRecognizerGuide",
    "InkRecognizers",
    "InkRectangle",
    "InkRenderer",
    "InkSelectionConstants",
    "InkShiftKeyModifierFlags",
    "InkStrokes",
    "InkSystemGesture",
    "InkTablets",
    "InkTransform",
    "InkWordList",
    "InteractionMode",
    "InteractionMode_DockedBottom",
    "InteractionMode_DockedTop",
    "InteractionMode_Floating",
    "InteractionMode_InPlace",
    "IsStringSupported",
    "KEYMODIFIER",
    "KEYMODIFIER_ALTGR",
    "KEYMODIFIER_CONTROL",
    "KEYMODIFIER_EXT",
    "KEYMODIFIER_MENU",
    "KEYMODIFIER_SHIFT",
    "KEYMODIFIER_WIN",
    "LATTICE_METRICS",
    "LEFT_BUTTON",
    "LINE_METRICS",
    "LINE_SEGMENT",
    "LM_ASCENDER",
    "LM_BASELINE",
    "LM_DESCENDER",
    "LM_MIDLINE",
    "LoadCachedAttributes",
    "MAX_FRIENDLYNAME",
    "MAX_LANGUAGES",
    "MAX_PACKET_BUTTON_COUNT",
    "MAX_PACKET_PROPERTY_COUNT",
    "MAX_VENDORNAME",
    "MICROSOFT_PENINPUT_PANEL_PROPERTY_T",
    "MICROSOFT_TIP_COMBOBOXLIST_PROPERTY",
    "MICROSOFT_TIP_NO_INSERT_BUTTON_PROPERTY",
    "MICROSOFT_TIP_OPENING_MSG",
    "MICROSOFT_URL_EXPERIENCE_PROPERTY",
    "MICUIELEMENT",
    "MICUIELEMENTSTATE",
    "MICUIELEMENTSTATE_DISABLED",
    "MICUIELEMENTSTATE_HOT",
    "MICUIELEMENTSTATE_NORMAL",
    "MICUIELEMENTSTATE_PRESSED",
    "MICUIELEMENT_BUTTON_CANCEL",
    "MICUIELEMENT_BUTTON_CLEAR",
    "MICUIELEMENT_BUTTON_CORRECT",
    "MICUIELEMENT_BUTTON_ERASE",
    "MICUIELEMENT_BUTTON_INSERT",
    "MICUIELEMENT_BUTTON_REDO",
    "MICUIELEMENT_BUTTON_UNDO",
    "MICUIELEMENT_BUTTON_WRITE",
    "MICUIELEMENT_INKPANEL_BACKGROUND",
    "MICUIELEMENT_RESULTPANEL_BACKGROUND",
    "MIDDLE_BUTTON",
    "MakeWordList",
    "MathInputControl",
    "MouseButton",
    "NO_BUTTON",
    "NUM_FLICK_DIRECTIONS",
    "PACKET_DESCRIPTION",
    "PACKET_PROPERTY",
    "PROPERTY_METRICS",
    "PROPERTY_UNITS",
    "PROPERTY_UNITS_AMPERE",
    "PROPERTY_UNITS_CANDELA",
    "PROPERTY_UNITS_CENTIMETERS",
    "PROPERTY_UNITS_DEFAULT",
    "PROPERTY_UNITS_DEGREES",
    "PROPERTY_UNITS_ENGLINEAR",
    "PROPERTY_UNITS_ENGROTATION",
    "PROPERTY_UNITS_FAHRENHEIT",
    "PROPERTY_UNITS_GRAMS",
    "PROPERTY_UNITS_INCHES",
    "PROPERTY_UNITS_KELVIN",
    "PROPERTY_UNITS_POUNDS",
    "PROPERTY_UNITS_RADIANS",
    "PROPERTY_UNITS_SECONDS",
    "PROPERTY_UNITS_SILINEAR",
    "PROPERTY_UNITS_SIROTATION",
    "PROPERTY_UNITS_SLUGS",
    "PT_Default",
    "PT_Handwriting",
    "PT_Inactive",
    "PT_Keyboard",
    "PanelInputArea",
    "PanelInputArea_Auto",
    "PanelInputArea_CharacterPad",
    "PanelInputArea_Keyboard",
    "PanelInputArea_WritingPad",
    "PanelType",
    "PenInputPanel",
    "PenInputPanel_Internal",
    "PfnRecoCallback",
    "Process",
    "RECOCONF_HIGHCONFIDENCE",
    "RECOCONF_LOWCONFIDENCE",
    "RECOCONF_MEDIUMCONFIDENCE",
    "RECOCONF_NOTSET",
    "RECOFLAG_AUTOSPACE",
    "RECOFLAG_COERCE",
    "RECOFLAG_DISABLEPERSONALIZATION",
    "RECOFLAG_LINEMODE",
    "RECOFLAG_PREFIXOK",
    "RECOFLAG_SINGLESEG",
    "RECOFLAG_WORDMODE",
    "RECO_ATTRS",
    "RECO_GUIDE",
    "RECO_LATTICE",
    "RECO_LATTICE_COLUMN",
    "RECO_LATTICE_ELEMENT",
    "RECO_LATTICE_PROPERTIES",
    "RECO_LATTICE_PROPERTY",
    "RECO_RANGE",
    "RECO_TYPE",
    "RECO_TYPE_WCHAR",
    "RECO_TYPE_WSTRING",
    "RF_ADVISEINKCHANGE",
    "RF_ARBITRARY_ANGLE",
    "RF_BOXED_INPUT",
    "RF_CAC_INPUT",
    "RF_DONTCARE",
    "RF_DOWN_AND_LEFT",
    "RF_DOWN_AND_RIGHT",
    "RF_FREE_INPUT",
    "RF_LATTICE",
    "RF_LEFT_AND_DOWN",
    "RF_LINED_INPUT",
    "RF_OBJECT",
    "RF_PERFORMSLINEBREAKING",
    "RF_PERSONALIZABLE",
    "RF_REQUIRESSEGMENTATIONBREAKING",
    "RF_RIGHT_AND_DOWN",
    "RF_STROKEREORDER",
    "RIGHT_BUTTON",
    "RTSDI_AllData",
    "RTSDI_CustomStylusDataAdded",
    "RTSDI_DefaultEvents",
    "RTSDI_Error",
    "RTSDI_InAirPackets",
    "RTSDI_None",
    "RTSDI_Packets",
    "RTSDI_RealTimeStylusDisabled",
    "RTSDI_RealTimeStylusEnabled",
    "RTSDI_StylusButtonDown",
    "RTSDI_StylusButtonUp",
    "RTSDI_StylusDown",
    "RTSDI_StylusInRange",
    "RTSDI_StylusNew",
    "RTSDI_StylusOutOfRange",
    "RTSDI_StylusUp",
    "RTSDI_SystemEvents",
    "RTSDI_TabletAdded",
    "RTSDI_TabletRemoved",
    "RTSDI_UpdateMapping",
    "RTSLT_AsyncEventLock",
    "RTSLT_AsyncObjLock",
    "RTSLT_ExcludeCallback",
    "RTSLT_ObjLock",
    "RTSLT_SyncEventLock",
    "RTSLT_SyncObjLock",
    "RealTimeStylus",
    "RealTimeStylusDataInterest",
    "RealTimeStylusLockType",
    "SAFE_PARTIAL",
    "SCROLLDIRECTION",
    "SCROLLDIRECTION_DOWN",
    "SCROLLDIRECTION_UP",
    "SHR_E",
    "SHR_N",
    "SHR_NE",
    "SHR_NW",
    "SHR_None",
    "SHR_S",
    "SHR_SE",
    "SHR_SW",
    "SHR_Selection",
    "SHR_W",
    "STROKE_RANGE",
    "STR_GUID_ALTITUDEORIENTATION",
    "STR_GUID_AZIMUTHORIENTATION",
    "STR_GUID_BUTTONPRESSURE",
    "STR_GUID_DEVICE_CONTACT_ID",
    "STR_GUID_FINGERCONTACTCONFIDENCE",
    "STR_GUID_HEIGHT",
    "STR_GUID_NORMALPRESSURE",
    "STR_GUID_PAKETSTATUS",
    "STR_GUID_PITCHROTATION",
    "STR_GUID_ROLLROTATION",
    "STR_GUID_SERIALNUMBER",
    "STR_GUID_TANGENTPRESSURE",
    "STR_GUID_TIMERTICK",
    "STR_GUID_TWISTORIENTATION",
    "STR_GUID_WIDTH",
    "STR_GUID_X",
    "STR_GUID_XTILTORIENTATION",
    "STR_GUID_Y",
    "STR_GUID_YAWROTATION",
    "STR_GUID_YTILTORIENTATION",
    "STR_GUID_Z",
    "SYSTEM_EVENT_DATA",
    "ScrollBarsConstants",
    "ScrollBarsConstants_rtfBoth",
    "ScrollBarsConstants_rtfHorizontal",
    "ScrollBarsConstants_rtfNone",
    "ScrollBarsConstants_rtfVertical",
    "SelAlignmentConstants",
    "SelAlignmentConstants_rtfCenter",
    "SelAlignmentConstants_rtfLeft",
    "SelAlignmentConstants_rtfRight",
    "SelectionHitResult",
    "SetEnabledUnicodeRanges",
    "SetFactoid",
    "SetFlags",
    "SetGuide",
    "SetTextContext",
    "SetWordList",
    "SketchInk",
    "StrokeBuilder",
    "StylusInfo",
    "StylusQueue",
    "StylusQueue_AsyncStylusQueue",
    "StylusQueue_AsyncStylusQueueImmediate",
    "StylusQueue_SyncStylusQueue",
    "TABLET_DISABLE_FLICKFALLBACKKEYS",
    "TABLET_DISABLE_FLICKS",
    "TABLET_DISABLE_PENBARRELFEEDBACK",
    "TABLET_DISABLE_PENTAPFEEDBACK",
    "TABLET_DISABLE_PRESSANDHOLD",
    "TABLET_DISABLE_SMOOTHSCROLLING",
    "TABLET_DISABLE_TOUCHSWITCH",
    "TABLET_DISABLE_TOUCHUIFORCEOFF",
    "TABLET_DISABLE_TOUCHUIFORCEON",
    "TABLET_ENABLE_FLICKLEARNINGMODE",
    "TABLET_ENABLE_FLICKSONCONTEXT",
    "TABLET_ENABLE_MULTITOUCHDATA",
    "TCF_ALLOW_RECOGNITION",
    "TCF_FORCE_RECOGNITION",
    "TDK_Mouse",
    "TDK_Pen",
    "TDK_Touch",
    "THWC_CursorMustTouch",
    "THWC_CursorsHavePhysicalIds",
    "THWC_HardProximity",
    "THWC_Integrated",
    "TPMU_Centimeters",
    "TPMU_Default",
    "TPMU_Degrees",
    "TPMU_Grams",
    "TPMU_Inches",
    "TPMU_Pounds",
    "TPMU_Radians",
    "TPMU_Seconds",
    "TabletDeviceKind",
    "TabletHardwareCapabilities",
    "TabletPropertyMetricUnit",
    "TextInputPanel",
    "TipAutoCompleteClient",
    "VisualState",
    "VisualState_Closed",
    "VisualState_DockedBottom",
    "VisualState_DockedTop",
    "VisualState_Floating",
    "VisualState_InPlace",
    "WM_TABLET_ADDED",
    "WM_TABLET_DEFBASE",
    "WM_TABLET_DELETED",
    "WM_TABLET_FLICK",
    "WM_TABLET_MAXOFFSET",
    "WM_TABLET_QUERYSYSTEMGESTURESTATUS",
    "_IInkCollectorEvents",
    "_IInkEditEvents",
    "_IInkEvents",
    "_IInkOverlayEvents",
    "_IInkPictureEvents",
    "_IInkRecognitionEvents",
    "_IInkStrokesEvents",
    "_IMathInputControlEvents",
    "_IPenInputPanelEvents",
]
