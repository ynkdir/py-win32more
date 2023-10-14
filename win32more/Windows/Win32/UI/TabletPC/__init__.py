from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, winfunctype, winfunctype_pointer, make_ready
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Ole
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.UI.Controls
import win32more.Windows.Win32.UI.TabletPC
ALT_BREAKS = Int32
ALT_BREAKS_SAME: ALT_BREAKS = 0
ALT_BREAKS_UNIQUE: ALT_BREAKS = 1
ALT_BREAKS_FULL: ALT_BREAKS = 2
MICROSOFT_URL_EXPERIENCE_PROPERTY: String = 'Microsoft TIP URL Experience'
MICROSOFT_TIP_NO_INSERT_BUTTON_PROPERTY: String = 'Microsoft TIP No Insert Option'
MICROSOFT_TIP_COMBOBOXLIST_PROPERTY: String = 'Microsoft TIP ComboBox List Window Identifier'
MICROSOFT_TIP_OPENING_MSG: String = 'TabletInputPanelOpening'
SAFE_PARTIAL: UInt32 = 1
BEST_COMPLETE: UInt32 = 2
MAX_VENDORNAME: UInt32 = 32
MAX_FRIENDLYNAME: UInt32 = 64
MAX_LANGUAGES: UInt32 = 64
CAC_FULL: UInt32 = 0
CAC_PREFIX: UInt32 = 1
CAC_RANDOM: UInt32 = 2
ASYNC_RECO_INTERRUPTED: UInt32 = 1
ASYNC_RECO_PROCESS_FAILED: UInt32 = 2
ASYNC_RECO_ADDSTROKE_FAILED: UInt32 = 4
ASYNC_RECO_SETCACMODE_FAILED: UInt32 = 8
ASYNC_RECO_RESETCONTEXT_FAILED: UInt32 = 16
ASYNC_RECO_SETGUIDE_FAILED: UInt32 = 32
ASYNC_RECO_SETFLAGS_FAILED: UInt32 = 64
ASYNC_RECO_SETFACTOID_FAILED: UInt32 = 128
ASYNC_RECO_SETTEXTCONTEXT_FAILED: UInt32 = 256
ASYNC_RECO_SETWORDLIST_FAILED: UInt32 = 512
RF_DONTCARE: Int32 = 1
RF_OBJECT: Int32 = 2
RF_FREE_INPUT: Int32 = 4
RF_LINED_INPUT: Int32 = 8
RF_BOXED_INPUT: Int32 = 16
RF_CAC_INPUT: Int32 = 32
RF_RIGHT_AND_DOWN: Int32 = 64
RF_LEFT_AND_DOWN: Int32 = 128
RF_DOWN_AND_LEFT: Int32 = 256
RF_DOWN_AND_RIGHT: Int32 = 512
RF_ARBITRARY_ANGLE: Int32 = 1024
RF_LATTICE: Int32 = 2048
RF_ADVISEINKCHANGE: Int32 = 4096
RF_STROKEREORDER: Int32 = 8192
RF_PERSONALIZABLE: Int32 = 16384
RF_PERFORMSLINEBREAKING: Int32 = 65536
RF_REQUIRESSEGMENTATIONBREAKING: Int32 = 131072
FLICK_WM_HANDLED_MASK: UInt32 = 1
NUM_FLICK_DIRECTIONS: UInt32 = 8
WM_TABLET_DEFBASE: UInt32 = 704
WM_TABLET_MAXOFFSET: UInt32 = 32
WM_TABLET_ADDED: UInt32 = 712
WM_TABLET_DELETED: UInt32 = 713
WM_TABLET_FLICK: UInt32 = 715
WM_TABLET_QUERYSYSTEMGESTURESTATUS: UInt32 = 716
TABLET_DISABLE_PRESSANDHOLD: UInt32 = 1
TABLET_DISABLE_PENTAPFEEDBACK: UInt32 = 8
TABLET_DISABLE_PENBARRELFEEDBACK: UInt32 = 16
TABLET_DISABLE_TOUCHUIFORCEON: UInt32 = 256
TABLET_DISABLE_TOUCHUIFORCEOFF: UInt32 = 512
TABLET_DISABLE_TOUCHSWITCH: UInt32 = 32768
TABLET_DISABLE_FLICKS: UInt32 = 65536
TABLET_ENABLE_FLICKSONCONTEXT: UInt32 = 131072
TABLET_ENABLE_FLICKLEARNINGMODE: UInt32 = 262144
TABLET_DISABLE_SMOOTHSCROLLING: UInt32 = 524288
TABLET_DISABLE_FLICKFALLBACKKEYS: UInt32 = 1048576
TABLET_ENABLE_MULTITOUCHDATA: UInt32 = 16777216
MAX_PACKET_PROPERTY_COUNT: UInt32 = 32
MAX_PACKET_BUTTON_COUNT: UInt32 = 32
IP_CURSOR_DOWN: UInt32 = 1
IP_INVERTED: UInt32 = 2
IP_MARGIN: UInt32 = 4
INK_SERIALIZED_FORMAT: String = 'Ink Serialized Format'
STR_GUID_X: String = '{598A6A8F-52C0-4BA0-93AF-AF357411A561}'
STR_GUID_Y: String = '{B53F9F75-04E0-4498-A7EE-C30DBB5A9011}'
STR_GUID_Z: String = '{735ADB30-0EBB-4788-A0E4-0F316490055D}'
STR_GUID_PAKETSTATUS: String = '{6E0E07BF-AFE7-4CF7-87D1-AF6446208418}'
STR_GUID_TIMERTICK: String = '{436510C5-FED3-45D1-8B76-71D3EA7A829D}'
STR_GUID_SERIALNUMBER: String = '{78A81B56-0935-4493-BAAE-00541A8A16C4}'
STR_GUID_NORMALPRESSURE: String = '{7307502D-F9F4-4E18-B3F2-2CE1B1A3610C}'
STR_GUID_TANGENTPRESSURE: String = '{6DA4488B-5244-41EC-905B-32D89AB80809}'
STR_GUID_BUTTONPRESSURE: String = '{8B7FEFC4-96AA-4BFE-AC26-8A5F0BE07BF5}'
STR_GUID_XTILTORIENTATION: String = '{A8D07B3A-8BF0-40B0-95A9-B80A6BB787BF}'
STR_GUID_YTILTORIENTATION: String = '{0E932389-1D77-43AF-AC00-5B950D6D4B2D}'
STR_GUID_AZIMUTHORIENTATION: String = '{029123B4-8828-410B-B250-A0536595E5DC}'
STR_GUID_ALTITUDEORIENTATION: String = '{82DEC5C7-F6BA-4906-894F-66D68DFC456C}'
STR_GUID_TWISTORIENTATION: String = '{0D324960-13B2-41E4-ACE6-7AE9D43D2D3B}'
STR_GUID_PITCHROTATION: String = '{7F7E57B7-BE37-4BE1-A356-7A84160E1893}'
STR_GUID_ROLLROTATION: String = '{5D5D5E56-6BA9-4C5B-9FB0-851C91714E56}'
STR_GUID_YAWROTATION: String = '{6A849980-7C3A-45B7-AA82-90A262950E89}'
STR_GUID_WIDTH: String = '{BAABE94D-2712-48F5-BE9D-8F8B5EA0711A}'
STR_GUID_HEIGHT: String = '{E61858D2-E447-4218-9D3F-18865C203DF4}'
STR_GUID_FINGERCONTACTCONFIDENCE: String = '{E706C804-57F0-4F00-8A0C-853D57789BE9}'
STR_GUID_DEVICE_CONTACT_ID: String = '{02585B91-049B-4750-9615-DF8948AB3C9C}'
INKRECOGNITIONPROPERTY_LINENUMBER: String = '{DBF29F2C-5289-4BE8-B3D8-6EF63246253E}'
INKRECOGNITIONPROPERTY_BOXNUMBER: String = '{2C243E3A-F733-4EB6-B1F8-B5DC5C2C4CDA}'
INKRECOGNITIONPROPERTY_SEGMENTATION: String = '{B3C0FE6C-FB51-4164-BA2F-844AF8F983DA}'
INKRECOGNITIONPROPERTY_HOTPOINT: String = '{CA6F40DC-5292-452a-91FB-2181C0BEC0DE}'
INKRECOGNITIONPROPERTY_MAXIMUMSTROKECOUNT: String = '{BF0EEC4E-4B7D-47a9-8CFA-234DD24BD22A}'
INKRECOGNITIONPROPERTY_POINTSPERINCH: String = '{7ED16B76-889C-468e-8276-0021B770187E}'
INKRECOGNITIONPROPERTY_CONFIDENCELEVEL: String = '{7DFE11A7-FB5D-4958-8765-154ADF0D833F}'
INKRECOGNITIONPROPERTY_LINEMETRICS: String = '{8CC24B27-30A9-4b96-9056-2D3A90DA0727}'
FACTOID_NONE: String = 'NONE'
FACTOID_DEFAULT: String = 'DEFAULT'
FACTOID_SYSTEMDICTIONARY: String = 'SYSDICT'
FACTOID_WORDLIST: String = 'WORDLIST'
FACTOID_EMAIL: String = 'EMAIL'
FACTOID_WEB: String = 'WEB'
FACTOID_ONECHAR: String = 'ONECHAR'
FACTOID_NUMBER: String = 'NUMBER'
FACTOID_DIGIT: String = 'DIGIT'
FACTOID_NUMBERSIMPLE: String = 'NUMSIMPLE'
FACTOID_CURRENCY: String = 'CURRENCY'
FACTOID_POSTALCODE: String = 'POSTALCODE'
FACTOID_PERCENT: String = 'PERCENT'
FACTOID_DATE: String = 'DATE'
FACTOID_TIME: String = 'TIME'
FACTOID_TELEPHONE: String = 'TELEPHONE'
FACTOID_FILENAME: String = 'FILENAME'
FACTOID_UPPERCHAR: String = 'UPPERCHAR'
FACTOID_LOWERCHAR: String = 'LOWERCHAR'
FACTOID_PUNCCHAR: String = 'PUNCCHAR'
FACTOID_JAPANESECOMMON: String = 'JPN_COMMON'
FACTOID_CHINESESIMPLECOMMON: String = 'CHS_COMMON'
FACTOID_CHINESETRADITIONALCOMMON: String = 'CHT_COMMON'
FACTOID_KOREANCOMMON: String = 'KOR_COMMON'
FACTOID_HIRAGANA: String = 'HIRAGANA'
FACTOID_KATAKANA: String = 'KATAKANA'
FACTOID_KANJICOMMON: String = 'KANJI_COMMON'
FACTOID_KANJIRARE: String = 'KANJI_RARE'
FACTOID_BOPOMOFO: String = 'BOPOMOFO'
FACTOID_JAMO: String = 'JAMO'
FACTOID_HANGULCOMMON: String = 'HANGUL_COMMON'
FACTOID_HANGULRARE: String = 'HANGUL_RARE'
MICROSOFT_PENINPUT_PANEL_PROPERTY_T: String = 'Microsoft PenInputPanel 1.5'
INKEDIT_CLASSW: String = 'INKEDIT'
INKEDIT_CLASS: String = 'INKEDIT'
IEC__BASE: UInt32 = 1536
EM_GETINKMODE: UInt32 = 1537
EM_SETINKMODE: UInt32 = 1538
EM_GETINKINSERTMODE: UInt32 = 1539
EM_SETINKINSERTMODE: UInt32 = 1540
EM_GETDRAWATTR: UInt32 = 1541
EM_SETDRAWATTR: UInt32 = 1542
EM_GETRECOTIMEOUT: UInt32 = 1543
EM_SETRECOTIMEOUT: UInt32 = 1544
EM_GETGESTURESTATUS: UInt32 = 1545
EM_SETGESTURESTATUS: UInt32 = 1546
EM_GETRECOGNIZER: UInt32 = 1547
EM_SETRECOGNIZER: UInt32 = 1548
EM_GETFACTOID: UInt32 = 1549
EM_SETFACTOID: UInt32 = 1550
EM_GETSELINK: UInt32 = 1551
EM_SETSELINK: UInt32 = 1552
EM_GETMOUSEICON: UInt32 = 1553
EM_SETMOUSEICON: UInt32 = 1554
EM_GETMOUSEPOINTER: UInt32 = 1555
EM_SETMOUSEPOINTER: UInt32 = 1556
EM_GETSTATUS: UInt32 = 1557
EM_RECOGNIZE: UInt32 = 1558
EM_GETUSEMOUSEFORINPUT: UInt32 = 1559
EM_SETUSEMOUSEFORINPUT: UInt32 = 1560
EM_SETSELINKDISPLAYMODE: UInt32 = 1561
EM_GETSELINKDISPLAYMODE: UInt32 = 1562
IECN__BASE: UInt32 = 2048
IECN_STROKE: UInt32 = 2049
IECN_GESTURE: UInt32 = 2050
IECN_RECOGNITIONRESULT: UInt32 = 2051
RECOFLAG_WORDMODE: UInt32 = 1
RECOFLAG_COERCE: UInt32 = 2
RECOFLAG_SINGLESEG: UInt32 = 4
RECOFLAG_PREFIXOK: UInt32 = 8
RECOFLAG_LINEMODE: UInt32 = 16
RECOFLAG_DISABLEPERSONALIZATION: UInt32 = 32
RECOFLAG_AUTOSPACE: UInt32 = 64
RECOCONF_LOWCONFIDENCE: Int32 = -1
RECOCONF_MEDIUMCONFIDENCE: UInt32 = 0
RECOCONF_HIGHCONFIDENCE: UInt32 = 1
RECOCONF_NOTSET: UInt32 = 128
GESTURE_NULL: UInt32 = 61440
GESTURE_SCRATCHOUT: UInt32 = 61441
GESTURE_TRIANGLE: UInt32 = 61442
GESTURE_SQUARE: UInt32 = 61443
GESTURE_STAR: UInt32 = 61444
GESTURE_CHECK: UInt32 = 61445
GESTURE_INFINITY: UInt32 = 61446
GESTURE_CROSS: UInt32 = 61447
GESTURE_PARAGRAPH: UInt32 = 61448
GESTURE_SECTION: UInt32 = 61449
GESTURE_BULLET: UInt32 = 61450
GESTURE_BULLET_CROSS: UInt32 = 61451
GESTURE_SQUIGGLE: UInt32 = 61452
GESTURE_SWAP: UInt32 = 61453
GESTURE_OPENUP: UInt32 = 61454
GESTURE_CLOSEUP: UInt32 = 61455
GESTURE_CURLICUE: UInt32 = 61456
GESTURE_DOUBLE_CURLICUE: UInt32 = 61457
GESTURE_RECTANGLE: UInt32 = 61458
GESTURE_CIRCLE: UInt32 = 61472
GESTURE_DOUBLE_CIRCLE: UInt32 = 61473
GESTURE_CIRCLE_TAP: UInt32 = 61474
GESTURE_CIRCLE_CIRCLE: UInt32 = 61475
GESTURE_CIRCLE_CROSS: UInt32 = 61477
GESTURE_CIRCLE_LINE_VERT: UInt32 = 61478
GESTURE_CIRCLE_LINE_HORZ: UInt32 = 61479
GESTURE_SEMICIRCLE_LEFT: UInt32 = 61480
GESTURE_SEMICIRCLE_RIGHT: UInt32 = 61481
GESTURE_CHEVRON_UP: UInt32 = 61488
GESTURE_CHEVRON_DOWN: UInt32 = 61489
GESTURE_CHEVRON_LEFT: UInt32 = 61490
GESTURE_CHEVRON_RIGHT: UInt32 = 61491
GESTURE_ARROW_UP: UInt32 = 61496
GESTURE_ARROW_DOWN: UInt32 = 61497
GESTURE_ARROW_LEFT: UInt32 = 61498
GESTURE_ARROW_RIGHT: UInt32 = 61499
GESTURE_DOUBLE_ARROW_UP: UInt32 = 61500
GESTURE_DOUBLE_ARROW_DOWN: UInt32 = 61501
GESTURE_DOUBLE_ARROW_LEFT: UInt32 = 61502
GESTURE_DOUBLE_ARROW_RIGHT: UInt32 = 61503
GESTURE_UP_ARROW_LEFT: UInt32 = 61504
GESTURE_UP_ARROW_RIGHT: UInt32 = 61505
GESTURE_DOWN_ARROW_LEFT: UInt32 = 61506
GESTURE_DOWN_ARROW_RIGHT: UInt32 = 61507
GESTURE_LEFT_ARROW_UP: UInt32 = 61508
GESTURE_LEFT_ARROW_DOWN: UInt32 = 61509
GESTURE_RIGHT_ARROW_UP: UInt32 = 61510
GESTURE_RIGHT_ARROW_DOWN: UInt32 = 61511
GESTURE_UP: UInt32 = 61528
GESTURE_DOWN: UInt32 = 61529
GESTURE_LEFT: UInt32 = 61530
GESTURE_RIGHT: UInt32 = 61531
GESTURE_DIAGONAL_LEFTUP: UInt32 = 61532
GESTURE_DIAGONAL_RIGHTUP: UInt32 = 61533
GESTURE_DIAGONAL_LEFTDOWN: UInt32 = 61534
GESTURE_DIAGONAL_RIGHTDOWN: UInt32 = 61535
GESTURE_UP_DOWN: UInt32 = 61536
GESTURE_DOWN_UP: UInt32 = 61537
GESTURE_LEFT_RIGHT: UInt32 = 61538
GESTURE_RIGHT_LEFT: UInt32 = 61539
GESTURE_UP_LEFT_LONG: UInt32 = 61540
GESTURE_UP_RIGHT_LONG: UInt32 = 61541
GESTURE_DOWN_LEFT_LONG: UInt32 = 61542
GESTURE_DOWN_RIGHT_LONG: UInt32 = 61543
GESTURE_UP_LEFT: UInt32 = 61544
GESTURE_UP_RIGHT: UInt32 = 61545
GESTURE_DOWN_LEFT: UInt32 = 61546
GESTURE_DOWN_RIGHT: UInt32 = 61547
GESTURE_LEFT_UP: UInt32 = 61548
GESTURE_LEFT_DOWN: UInt32 = 61549
GESTURE_RIGHT_UP: UInt32 = 61550
GESTURE_RIGHT_DOWN: UInt32 = 61551
GESTURE_LETTER_A: UInt32 = 61568
GESTURE_LETTER_B: UInt32 = 61569
GESTURE_LETTER_C: UInt32 = 61570
GESTURE_LETTER_D: UInt32 = 61571
GESTURE_LETTER_E: UInt32 = 61572
GESTURE_LETTER_F: UInt32 = 61573
GESTURE_LETTER_G: UInt32 = 61574
GESTURE_LETTER_H: UInt32 = 61575
GESTURE_LETTER_I: UInt32 = 61576
GESTURE_LETTER_J: UInt32 = 61577
GESTURE_LETTER_K: UInt32 = 61578
GESTURE_LETTER_L: UInt32 = 61579
GESTURE_LETTER_M: UInt32 = 61580
GESTURE_LETTER_N: UInt32 = 61581
GESTURE_LETTER_O: UInt32 = 61582
GESTURE_LETTER_P: UInt32 = 61583
GESTURE_LETTER_Q: UInt32 = 61584
GESTURE_LETTER_R: UInt32 = 61585
GESTURE_LETTER_S: UInt32 = 61586
GESTURE_LETTER_T: UInt32 = 61587
GESTURE_LETTER_U: UInt32 = 61588
GESTURE_LETTER_V: UInt32 = 61589
GESTURE_LETTER_W: UInt32 = 61590
GESTURE_LETTER_X: UInt32 = 61591
GESTURE_LETTER_Y: UInt32 = 61592
GESTURE_LETTER_Z: UInt32 = 61593
GESTURE_DIGIT_0: UInt32 = 61594
GESTURE_DIGIT_1: UInt32 = 61595
GESTURE_DIGIT_2: UInt32 = 61596
GESTURE_DIGIT_3: UInt32 = 61597
GESTURE_DIGIT_4: UInt32 = 61598
GESTURE_DIGIT_5: UInt32 = 61599
GESTURE_DIGIT_6: UInt32 = 61600
GESTURE_DIGIT_7: UInt32 = 61601
GESTURE_DIGIT_8: UInt32 = 61602
GESTURE_DIGIT_9: UInt32 = 61603
GESTURE_EXCLAMATION: UInt32 = 61604
GESTURE_QUESTION: UInt32 = 61605
GESTURE_SHARP: UInt32 = 61606
GESTURE_DOLLAR: UInt32 = 61607
GESTURE_ASTERISK: UInt32 = 61608
GESTURE_PLUS: UInt32 = 61609
GESTURE_DOUBLE_UP: UInt32 = 61624
GESTURE_DOUBLE_DOWN: UInt32 = 61625
GESTURE_DOUBLE_LEFT: UInt32 = 61626
GESTURE_DOUBLE_RIGHT: UInt32 = 61627
GESTURE_TRIPLE_UP: UInt32 = 61628
GESTURE_TRIPLE_DOWN: UInt32 = 61629
GESTURE_TRIPLE_LEFT: UInt32 = 61630
GESTURE_TRIPLE_RIGHT: UInt32 = 61631
GESTURE_BRACKET_OVER: UInt32 = 61668
GESTURE_BRACKET_UNDER: UInt32 = 61669
GESTURE_BRACKET_LEFT: UInt32 = 61670
GESTURE_BRACKET_RIGHT: UInt32 = 61671
GESTURE_BRACE_OVER: UInt32 = 61672
GESTURE_BRACE_UNDER: UInt32 = 61673
GESTURE_BRACE_LEFT: UInt32 = 61674
GESTURE_BRACE_RIGHT: UInt32 = 61675
GESTURE_TAP: UInt32 = 61680
GESTURE_DOUBLE_TAP: UInt32 = 61681
GESTURE_TRIPLE_TAP: UInt32 = 61682
GESTURE_QUAD_TAP: UInt32 = 61683
FACILITY_INK: UInt32 = 40
GUID_PACKETPROPERTY_GUID_X: Guid = Guid('{598a6a8f-52c0-4ba0-93af-af357411a561}')
GUID_PACKETPROPERTY_GUID_Y: Guid = Guid('{b53f9f75-04e0-4498-a7ee-c30dbb5a9011}')
GUID_PACKETPROPERTY_GUID_Z: Guid = Guid('{735adb30-0ebb-4788-a0e4-0f316490055d}')
GUID_PACKETPROPERTY_GUID_PACKET_STATUS: Guid = Guid('{6e0e07bf-afe7-4cf7-87d1-af6446208418}')
GUID_PACKETPROPERTY_GUID_TIMER_TICK: Guid = Guid('{436510c5-fed3-45d1-8b76-71d3ea7a829d}')
GUID_PACKETPROPERTY_GUID_SERIAL_NUMBER: Guid = Guid('{78a81b56-0935-4493-baae-00541a8a16c4}')
GUID_PACKETPROPERTY_GUID_NORMAL_PRESSURE: Guid = Guid('{7307502d-f9f4-4e18-b3f2-2ce1b1a3610c}')
GUID_PACKETPROPERTY_GUID_TANGENT_PRESSURE: Guid = Guid('{6da4488b-5244-41ec-905b-32d89ab80809}')
GUID_PACKETPROPERTY_GUID_BUTTON_PRESSURE: Guid = Guid('{8b7fefc4-96aa-4bfe-ac26-8a5f0be07bf5}')
GUID_PACKETPROPERTY_GUID_X_TILT_ORIENTATION: Guid = Guid('{a8d07b3a-8bf0-40b0-95a9-b80a6bb787bf}')
GUID_PACKETPROPERTY_GUID_Y_TILT_ORIENTATION: Guid = Guid('{0e932389-1d77-43af-ac00-5b950d6d4b2d}')
GUID_PACKETPROPERTY_GUID_AZIMUTH_ORIENTATION: Guid = Guid('{029123b4-8828-410b-b250-a0536595e5dc}')
GUID_PACKETPROPERTY_GUID_ALTITUDE_ORIENTATION: Guid = Guid('{82dec5c7-f6ba-4906-894f-66d68dfc456c}')
GUID_PACKETPROPERTY_GUID_TWIST_ORIENTATION: Guid = Guid('{0d324960-13b2-41e4-ace6-7ae9d43d2d3b}')
GUID_PACKETPROPERTY_GUID_PITCH_ROTATION: Guid = Guid('{7f7e57b7-be37-4be1-a356-7a84160e1893}')
GUID_PACKETPROPERTY_GUID_ROLL_ROTATION: Guid = Guid('{5d5d5e56-6ba9-4c5b-9fb0-851c91714e56}')
GUID_PACKETPROPERTY_GUID_YAW_ROTATION: Guid = Guid('{6a849980-7c3a-45b7-aa82-90a262950e89}')
GUID_PACKETPROPERTY_GUID_WIDTH: Guid = Guid('{baabe94d-2712-48f5-be9d-8f8b5ea0711a}')
GUID_PACKETPROPERTY_GUID_HEIGHT: Guid = Guid('{e61858d2-e447-4218-9d3f-18865c203df4}')
GUID_PACKETPROPERTY_GUID_FINGERCONTACTCONFIDENCE: Guid = Guid('{e706c804-57f0-4f00-8a0c-853d57789be9}')
GUID_PACKETPROPERTY_GUID_DEVICE_CONTACT_ID: Guid = Guid('{02585b91-049b-4750-9615-df8948ab3c9c}')
InkMinTransparencyValue: Int32 = 0
InkMaxTransparencyValue: Int32 = 255
InkCollectorClipInkToMargin: Int32 = 0
InkCollectorDefaultMargin: Int32 = -2147483648
GUID_GESTURE_DATA: Guid = Guid('{41e4ec0f-26aa-455a-9aa5-2cd36cf63fb9}')
GUID_DYNAMIC_RENDERER_CACHED_DATA: Guid = Guid('{bf531b92-25bf-4a95-89ad-0e476b34b4f5}')
@winfunctype('inkobjcore.dll')
def CreateRecognizer(pCLSID: POINTER(Guid), phrec: POINTER(win32more.Windows.Win32.UI.TabletPC.HRECOGNIZER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def DestroyRecognizer(hrec: win32more.Windows.Win32.UI.TabletPC.HRECOGNIZER) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def GetRecoAttributes(hrec: win32more.Windows.Win32.UI.TabletPC.HRECOGNIZER, pRecoAttrs: POINTER(win32more.Windows.Win32.UI.TabletPC.RECO_ATTRS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def CreateContext(hrec: win32more.Windows.Win32.UI.TabletPC.HRECOGNIZER, phrc: POINTER(win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def DestroyContext(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def GetResultPropertyList(hrec: win32more.Windows.Win32.UI.TabletPC.HRECOGNIZER, pPropertyCount: POINTER(UInt32), pPropertyGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def GetUnicodeRanges(hrec: win32more.Windows.Win32.UI.TabletPC.HRECOGNIZER, pcRanges: POINTER(UInt32), pcr: POINTER(win32more.Windows.Win32.UI.TabletPC.CHARACTER_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def AddStroke(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, pPacketDesc: POINTER(win32more.Windows.Win32.UI.TabletPC.PACKET_DESCRIPTION), cbPacket: UInt32, pPacket: POINTER(Byte), pXForm: POINTER(win32more.Windows.Win32.Graphics.Gdi.XFORM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def GetBestResultString(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, pcSize: POINTER(UInt32), pwcBestResult: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def SetGuide(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, pGuide: POINTER(win32more.Windows.Win32.UI.TabletPC.RECO_GUIDE), iIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def AdviseInkChange(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, bNewStroke: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def EndInkInput(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def Process(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, pbPartialProcessing: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def SetFactoid(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, cwcFactoid: UInt32, pwcFactoid: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def SetFlags(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def GetLatticePtr(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, ppLattice: POINTER(POINTER(win32more.Windows.Win32.UI.TabletPC.RECO_LATTICE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def SetTextContext(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, cwcBefore: UInt32, pwcBefore: win32more.Windows.Win32.Foundation.PWSTR, cwcAfter: UInt32, pwcAfter: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def SetEnabledUnicodeRanges(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, cRanges: UInt32, pcr: POINTER(win32more.Windows.Win32.UI.TabletPC.CHARACTER_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def IsStringSupported(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, wcString: UInt32, pwcString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def SetWordList(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, hwl: win32more.Windows.Win32.UI.TabletPC.HRECOWORDLIST) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def GetRightSeparator(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, pcSize: POINTER(UInt32), pwcRightSeparator: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def GetLeftSeparator(hrc: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT, pcSize: POINTER(UInt32), pwcLeftSeparator: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def DestroyWordList(hwl: win32more.Windows.Win32.UI.TabletPC.HRECOWORDLIST) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def AddWordsToWordList(hwl: win32more.Windows.Win32.UI.TabletPC.HRECOWORDLIST, pwcWords: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def MakeWordList(hrec: win32more.Windows.Win32.UI.TabletPC.HRECOGNIZER, pBuffer: win32more.Windows.Win32.Foundation.PWSTR, phwl: POINTER(win32more.Windows.Win32.UI.TabletPC.HRECOWORDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def GetAllRecognizers(recognizerClsids: POINTER(POINTER(Guid)), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('inkobjcore.dll')
def LoadCachedAttributes(clsid: Guid, pRecoAttributes: POINTER(win32more.Windows.Win32.UI.TabletPC.RECO_ATTRS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
AppearanceConstants = Int32
AppearanceConstants_rtfFlat: AppearanceConstants = 0
AppearanceConstants_rtfThreeD: AppearanceConstants = 1
BorderStyleConstants = Int32
BorderStyleConstants_rtfNoBorder: BorderStyleConstants = 0
BorderStyleConstants_rtfFixedSingle: BorderStyleConstants = 1
class CHARACTER_RANGE(EasyCastStructure):
    wcLow: Char
    cChars: UInt16
CONFIDENCE_LEVEL = Int32
CFL_STRONG: CONFIDENCE_LEVEL = 0
CFL_INTERMEDIATE: CONFIDENCE_LEVEL = 1
CFL_POOR: CONFIDENCE_LEVEL = 2
CorrectionMode = Int32
CorrectionMode_NotVisible: CorrectionMode = 0
CorrectionMode_PreInsertion: CorrectionMode = 1
CorrectionMode_PostInsertionCollapsed: CorrectionMode = 2
CorrectionMode_PostInsertionExpanded: CorrectionMode = 3
CorrectionPosition = Int32
CorrectionPosition_Auto: CorrectionPosition = 0
CorrectionPosition_Bottom: CorrectionPosition = 1
CorrectionPosition_Top: CorrectionPosition = 2
DISPID_Ink = Int32
DISPID_IStrokes: DISPID_Ink = 1
DISPID_IExtendedProperties: DISPID_Ink = 2
DISPID_IGetBoundingBox: DISPID_Ink = 3
DISPID_IDeleteStrokes: DISPID_Ink = 4
DISPID_IDeleteStroke: DISPID_Ink = 5
DISPID_IExtractStrokes: DISPID_Ink = 6
DISPID_IExtractWithRectangle: DISPID_Ink = 7
DISPID_IDirty: DISPID_Ink = 8
DISPID_ICustomStrokes: DISPID_Ink = 9
DISPID_IClone: DISPID_Ink = 10
DISPID_IHitTestCircle: DISPID_Ink = 11
DISPID_IHitTestWithRectangle: DISPID_Ink = 12
DISPID_IHitTestWithLasso: DISPID_Ink = 13
DISPID_INearestPoint: DISPID_Ink = 14
DISPID_ICreateStrokes: DISPID_Ink = 15
DISPID_ICreateStroke: DISPID_Ink = 16
DISPID_IAddStrokesAtRectangle: DISPID_Ink = 17
DISPID_IClip: DISPID_Ink = 18
DISPID_ISave: DISPID_Ink = 19
DISPID_ILoad: DISPID_Ink = 20
DISPID_ICreateStrokeFromPoints: DISPID_Ink = 21
DISPID_IClipboardCopyWithRectangle: DISPID_Ink = 22
DISPID_IClipboardCopy: DISPID_Ink = 23
DISPID_ICanPaste: DISPID_Ink = 24
DISPID_IClipboardPaste: DISPID_Ink = 25
DISPID_InkCollector = Int32
DISPID_ICEnabled: DISPID_InkCollector = 1
DISPID_ICHwnd: DISPID_InkCollector = 2
DISPID_ICPaint: DISPID_InkCollector = 3
DISPID_ICText: DISPID_InkCollector = 4
DISPID_ICDefaultDrawingAttributes: DISPID_InkCollector = 5
DISPID_ICRenderer: DISPID_InkCollector = 6
DISPID_ICInk: DISPID_InkCollector = 7
DISPID_ICAutoRedraw: DISPID_InkCollector = 8
DISPID_ICCollectingInk: DISPID_InkCollector = 9
DISPID_ICSetEventInterest: DISPID_InkCollector = 10
DISPID_ICGetEventInterest: DISPID_InkCollector = 11
DISPID_IOEditingMode: DISPID_InkCollector = 12
DISPID_IOSelection: DISPID_InkCollector = 13
DISPID_IOAttachMode: DISPID_InkCollector = 14
DISPID_IOHitTestSelection: DISPID_InkCollector = 15
DISPID_IODraw: DISPID_InkCollector = 16
DISPID_IPPicture: DISPID_InkCollector = 17
DISPID_IPSizeMode: DISPID_InkCollector = 18
DISPID_IPBackColor: DISPID_InkCollector = 19
DISPID_ICCursors: DISPID_InkCollector = 20
DISPID_ICMarginX: DISPID_InkCollector = 21
DISPID_ICMarginY: DISPID_InkCollector = 22
DISPID_ICSetWindowInputRectangle: DISPID_InkCollector = 23
DISPID_ICGetWindowInputRectangle: DISPID_InkCollector = 24
DISPID_ICTablet: DISPID_InkCollector = 25
DISPID_ICSetAllTabletsMode: DISPID_InkCollector = 26
DISPID_ICSetSingleTabletIntegratedMode: DISPID_InkCollector = 27
DISPID_ICCollectionMode: DISPID_InkCollector = 28
DISPID_ICSetGestureStatus: DISPID_InkCollector = 29
DISPID_ICGetGestureStatus: DISPID_InkCollector = 30
DISPID_ICDynamicRendering: DISPID_InkCollector = 31
DISPID_ICDesiredPacketDescription: DISPID_InkCollector = 32
DISPID_IOEraserMode: DISPID_InkCollector = 33
DISPID_IOEraserWidth: DISPID_InkCollector = 34
DISPID_ICMouseIcon: DISPID_InkCollector = 35
DISPID_ICMousePointer: DISPID_InkCollector = 36
DISPID_IPInkEnabled: DISPID_InkCollector = 37
DISPID_ICSupportHighContrastInk: DISPID_InkCollector = 38
DISPID_IOSupportHighContrastSelectionUI: DISPID_InkCollector = 39
DISPID_InkCollectorEvent = Int32
DISPID_ICEStroke: DISPID_InkCollectorEvent = 1
DISPID_ICECursorDown: DISPID_InkCollectorEvent = 2
DISPID_ICENewPackets: DISPID_InkCollectorEvent = 3
DISPID_ICENewInAirPackets: DISPID_InkCollectorEvent = 4
DISPID_ICECursorButtonDown: DISPID_InkCollectorEvent = 5
DISPID_ICECursorButtonUp: DISPID_InkCollectorEvent = 6
DISPID_ICECursorInRange: DISPID_InkCollectorEvent = 7
DISPID_ICECursorOutOfRange: DISPID_InkCollectorEvent = 8
DISPID_ICESystemGesture: DISPID_InkCollectorEvent = 9
DISPID_ICEGesture: DISPID_InkCollectorEvent = 10
DISPID_ICETabletAdded: DISPID_InkCollectorEvent = 11
DISPID_ICETabletRemoved: DISPID_InkCollectorEvent = 12
DISPID_IOEPainting: DISPID_InkCollectorEvent = 13
DISPID_IOEPainted: DISPID_InkCollectorEvent = 14
DISPID_IOESelectionChanging: DISPID_InkCollectorEvent = 15
DISPID_IOESelectionChanged: DISPID_InkCollectorEvent = 16
DISPID_IOESelectionMoving: DISPID_InkCollectorEvent = 17
DISPID_IOESelectionMoved: DISPID_InkCollectorEvent = 18
DISPID_IOESelectionResizing: DISPID_InkCollectorEvent = 19
DISPID_IOESelectionResized: DISPID_InkCollectorEvent = 20
DISPID_IOEStrokesDeleting: DISPID_InkCollectorEvent = 21
DISPID_IOEStrokesDeleted: DISPID_InkCollectorEvent = 22
DISPID_IPEChangeUICues: DISPID_InkCollectorEvent = 23
DISPID_IPEClick: DISPID_InkCollectorEvent = 24
DISPID_IPEDblClick: DISPID_InkCollectorEvent = 25
DISPID_IPEInvalidated: DISPID_InkCollectorEvent = 26
DISPID_IPEMouseDown: DISPID_InkCollectorEvent = 27
DISPID_IPEMouseEnter: DISPID_InkCollectorEvent = 28
DISPID_IPEMouseHover: DISPID_InkCollectorEvent = 29
DISPID_IPEMouseLeave: DISPID_InkCollectorEvent = 30
DISPID_IPEMouseMove: DISPID_InkCollectorEvent = 31
DISPID_IPEMouseUp: DISPID_InkCollectorEvent = 32
DISPID_IPEMouseWheel: DISPID_InkCollectorEvent = 33
DISPID_IPESizeModeChanged: DISPID_InkCollectorEvent = 34
DISPID_IPEStyleChanged: DISPID_InkCollectorEvent = 35
DISPID_IPESystemColorsChanged: DISPID_InkCollectorEvent = 36
DISPID_IPEKeyDown: DISPID_InkCollectorEvent = 37
DISPID_IPEKeyPress: DISPID_InkCollectorEvent = 38
DISPID_IPEKeyUp: DISPID_InkCollectorEvent = 39
DISPID_IPEResize: DISPID_InkCollectorEvent = 40
DISPID_IPESizeChanged: DISPID_InkCollectorEvent = 41
DISPID_InkCursor = Int32
DISPID_ICsrName: DISPID_InkCursor = 0
DISPID_ICsrId: DISPID_InkCursor = 1
DISPID_ICsrDrawingAttributes: DISPID_InkCursor = 2
DISPID_ICsrButtons: DISPID_InkCursor = 3
DISPID_ICsrInverted: DISPID_InkCursor = 4
DISPID_ICsrTablet: DISPID_InkCursor = 5
DISPID_InkCursorButton = Int32
DISPID_ICBName: DISPID_InkCursorButton = 0
DISPID_ICBId: DISPID_InkCursorButton = 1
DISPID_ICBState: DISPID_InkCursorButton = 2
DISPID_InkCursorButtons = Int32
DISPID_ICBs_NewEnum: DISPID_InkCursorButtons = -4
DISPID_ICBsItem: DISPID_InkCursorButtons = 0
DISPID_ICBsCount: DISPID_InkCursorButtons = 1
DISPID_InkCursors = Int32
DISPID_ICs_NewEnum: DISPID_InkCursors = -4
DISPID_ICsItem: DISPID_InkCursors = 0
DISPID_ICsCount: DISPID_InkCursors = 1
DISPID_InkCustomStrokes = Int32
DISPID_ICSs_NewEnum: DISPID_InkCustomStrokes = -4
DISPID_ICSsItem: DISPID_InkCustomStrokes = 0
DISPID_ICSsCount: DISPID_InkCustomStrokes = 1
DISPID_ICSsAdd: DISPID_InkCustomStrokes = 2
DISPID_ICSsRemove: DISPID_InkCustomStrokes = 3
DISPID_ICSsClear: DISPID_InkCustomStrokes = 4
DISPID_InkDivider = Int32
DISPID_IInkDivider_Strokes: DISPID_InkDivider = 1
DISPID_IInkDivider_RecognizerContext: DISPID_InkDivider = 2
DISPID_IInkDivider_LineHeight: DISPID_InkDivider = 3
DISPID_IInkDivider_Divide: DISPID_InkDivider = 4
DISPID_InkDivisionResult = Int32
DISPID_IInkDivisionResult_Strokes: DISPID_InkDivisionResult = 1
DISPID_IInkDivisionResult_ResultByType: DISPID_InkDivisionResult = 2
DISPID_InkDivisionUnit = Int32
DISPID_IInkDivisionUnit_Strokes: DISPID_InkDivisionUnit = 1
DISPID_IInkDivisionUnit_DivisionType: DISPID_InkDivisionUnit = 2
DISPID_IInkDivisionUnit_RecognizedString: DISPID_InkDivisionUnit = 3
DISPID_IInkDivisionUnit_RotationTransform: DISPID_InkDivisionUnit = 4
DISPID_InkDivisionUnits = Int32
DISPID_IInkDivisionUnits_NewEnum: DISPID_InkDivisionUnits = -4
DISPID_IInkDivisionUnits_Item: DISPID_InkDivisionUnits = 0
DISPID_IInkDivisionUnits_Count: DISPID_InkDivisionUnits = 1
DISPID_InkDrawingAttributes = Int32
DISPID_DAHeight: DISPID_InkDrawingAttributes = 1
DISPID_DAColor: DISPID_InkDrawingAttributes = 2
DISPID_DAWidth: DISPID_InkDrawingAttributes = 3
DISPID_DAFitToCurve: DISPID_InkDrawingAttributes = 4
DISPID_DAIgnorePressure: DISPID_InkDrawingAttributes = 5
DISPID_DAAntiAliased: DISPID_InkDrawingAttributes = 6
DISPID_DATransparency: DISPID_InkDrawingAttributes = 7
DISPID_DARasterOperation: DISPID_InkDrawingAttributes = 8
DISPID_DAPenTip: DISPID_InkDrawingAttributes = 9
DISPID_DAClone: DISPID_InkDrawingAttributes = 10
DISPID_DAExtendedProperties: DISPID_InkDrawingAttributes = 11
DISPID_InkEdit = Int32
DISPID_Text: DISPID_InkEdit = 0
DISPID_TextRTF: DISPID_InkEdit = 1
DISPID_Hwnd: DISPID_InkEdit = 2
DISPID_DisableNoScroll: DISPID_InkEdit = 3
DISPID_Locked: DISPID_InkEdit = 4
DISPID_Enabled: DISPID_InkEdit = 5
DISPID_MaxLength: DISPID_InkEdit = 6
DISPID_MultiLine: DISPID_InkEdit = 7
DISPID_ScrollBars: DISPID_InkEdit = 8
DISPID_RTSelStart: DISPID_InkEdit = 9
DISPID_RTSelLength: DISPID_InkEdit = 10
DISPID_RTSelText: DISPID_InkEdit = 11
DISPID_SelAlignment: DISPID_InkEdit = 12
DISPID_SelBold: DISPID_InkEdit = 13
DISPID_SelCharOffset: DISPID_InkEdit = 14
DISPID_SelColor: DISPID_InkEdit = 15
DISPID_SelFontName: DISPID_InkEdit = 16
DISPID_SelFontSize: DISPID_InkEdit = 17
DISPID_SelItalic: DISPID_InkEdit = 18
DISPID_SelRTF: DISPID_InkEdit = 19
DISPID_SelUnderline: DISPID_InkEdit = 20
DISPID_DragIcon: DISPID_InkEdit = 21
DISPID_Status: DISPID_InkEdit = 22
DISPID_UseMouseForInput: DISPID_InkEdit = 23
DISPID_InkMode: DISPID_InkEdit = 24
DISPID_InkInsertMode: DISPID_InkEdit = 25
DISPID_RecoTimeout: DISPID_InkEdit = 26
DISPID_DrawAttr: DISPID_InkEdit = 27
DISPID_Recognizer: DISPID_InkEdit = 28
DISPID_Factoid: DISPID_InkEdit = 29
DISPID_SelInk: DISPID_InkEdit = 30
DISPID_SelInksDisplayMode: DISPID_InkEdit = 31
DISPID_Recognize: DISPID_InkEdit = 32
DISPID_GetGestStatus: DISPID_InkEdit = 33
DISPID_SetGestStatus: DISPID_InkEdit = 34
DISPID_Refresh: DISPID_InkEdit = 35
DISPID_InkEditEvents = Int32
DISPID_IeeChange: DISPID_InkEditEvents = 1
DISPID_IeeSelChange: DISPID_InkEditEvents = 2
DISPID_IeeKeyDown: DISPID_InkEditEvents = 3
DISPID_IeeKeyUp: DISPID_InkEditEvents = 4
DISPID_IeeMouseUp: DISPID_InkEditEvents = 5
DISPID_IeeMouseDown: DISPID_InkEditEvents = 6
DISPID_IeeKeyPress: DISPID_InkEditEvents = 7
DISPID_IeeDblClick: DISPID_InkEditEvents = 8
DISPID_IeeClick: DISPID_InkEditEvents = 9
DISPID_IeeMouseMove: DISPID_InkEditEvents = 10
DISPID_IeeCursorDown: DISPID_InkEditEvents = 21
DISPID_IeeStroke: DISPID_InkEditEvents = 22
DISPID_IeeGesture: DISPID_InkEditEvents = 23
DISPID_IeeRecognitionResult: DISPID_InkEditEvents = 24
DISPID_InkEvent = Int32
DISPID_IEInkAdded: DISPID_InkEvent = 1
DISPID_IEInkDeleted: DISPID_InkEvent = 2
DISPID_InkExtendedProperties = Int32
DISPID_IEPs_NewEnum: DISPID_InkExtendedProperties = -4
DISPID_IEPsItem: DISPID_InkExtendedProperties = 0
DISPID_IEPsCount: DISPID_InkExtendedProperties = 1
DISPID_IEPsAdd: DISPID_InkExtendedProperties = 2
DISPID_IEPsRemove: DISPID_InkExtendedProperties = 3
DISPID_IEPsClear: DISPID_InkExtendedProperties = 4
DISPID_IEPsDoesPropertyExist: DISPID_InkExtendedProperties = 5
DISPID_InkExtendedProperty = Int32
DISPID_IEPGuid: DISPID_InkExtendedProperty = 1
DISPID_IEPData: DISPID_InkExtendedProperty = 2
DISPID_InkGesture = Int32
DISPID_IGId: DISPID_InkGesture = 0
DISPID_IGGetHotPoint: DISPID_InkGesture = 1
DISPID_IGConfidence: DISPID_InkGesture = 2
DISPID_InkRecoAlternate = Int32
DISPID_InkRecoAlternate_String: DISPID_InkRecoAlternate = 1
DISPID_InkRecoAlternate_LineNumber: DISPID_InkRecoAlternate = 2
DISPID_InkRecoAlternate_Baseline: DISPID_InkRecoAlternate = 3
DISPID_InkRecoAlternate_Midline: DISPID_InkRecoAlternate = 4
DISPID_InkRecoAlternate_Ascender: DISPID_InkRecoAlternate = 5
DISPID_InkRecoAlternate_Descender: DISPID_InkRecoAlternate = 6
DISPID_InkRecoAlternate_Confidence: DISPID_InkRecoAlternate = 7
DISPID_InkRecoAlternate_Strokes: DISPID_InkRecoAlternate = 8
DISPID_InkRecoAlternate_GetStrokesFromStrokeRanges: DISPID_InkRecoAlternate = 9
DISPID_InkRecoAlternate_GetStrokesFromTextRange: DISPID_InkRecoAlternate = 10
DISPID_InkRecoAlternate_GetTextRangeFromStrokes: DISPID_InkRecoAlternate = 11
DISPID_InkRecoAlternate_GetPropertyValue: DISPID_InkRecoAlternate = 12
DISPID_InkRecoAlternate_LineAlternates: DISPID_InkRecoAlternate = 13
DISPID_InkRecoAlternate_ConfidenceAlternates: DISPID_InkRecoAlternate = 14
DISPID_InkRecoAlternate_AlternatesWithConstantPropertyValues: DISPID_InkRecoAlternate = 15
DISPID_InkRecoContext = Int32
DISPID_IRecoCtx_Strokes: DISPID_InkRecoContext = 1
DISPID_IRecoCtx_CharacterAutoCompletionMode: DISPID_InkRecoContext = 2
DISPID_IRecoCtx_Factoid: DISPID_InkRecoContext = 3
DISPID_IRecoCtx_WordList: DISPID_InkRecoContext = 4
DISPID_IRecoCtx_Recognizer: DISPID_InkRecoContext = 5
DISPID_IRecoCtx_Guide: DISPID_InkRecoContext = 6
DISPID_IRecoCtx_Flags: DISPID_InkRecoContext = 7
DISPID_IRecoCtx_PrefixText: DISPID_InkRecoContext = 8
DISPID_IRecoCtx_SuffixText: DISPID_InkRecoContext = 9
DISPID_IRecoCtx_StopRecognition: DISPID_InkRecoContext = 10
DISPID_IRecoCtx_Clone: DISPID_InkRecoContext = 11
DISPID_IRecoCtx_Recognize: DISPID_InkRecoContext = 12
DISPID_IRecoCtx_StopBackgroundRecognition: DISPID_InkRecoContext = 13
DISPID_IRecoCtx_EndInkInput: DISPID_InkRecoContext = 14
DISPID_IRecoCtx_BackgroundRecognize: DISPID_InkRecoContext = 15
DISPID_IRecoCtx_BackgroundRecognizeWithAlternates: DISPID_InkRecoContext = 16
DISPID_IRecoCtx_IsStringSupported: DISPID_InkRecoContext = 17
DISPID_InkRecoContext2 = Int32
DISPID_IRecoCtx2_EnabledUnicodeRanges: DISPID_InkRecoContext2 = 0
DISPID_InkRecognitionAlternates = Int32
DISPID_InkRecognitionAlternates_NewEnum: DISPID_InkRecognitionAlternates = -4
DISPID_InkRecognitionAlternates_Item: DISPID_InkRecognitionAlternates = 0
DISPID_InkRecognitionAlternates_Count: DISPID_InkRecognitionAlternates = 1
DISPID_InkRecognitionAlternates_Strokes: DISPID_InkRecognitionAlternates = 2
DISPID_InkRecognitionEvent = Int32
DISPID_IRERecognitionWithAlternates: DISPID_InkRecognitionEvent = 1
DISPID_IRERecognition: DISPID_InkRecognitionEvent = 2
DISPID_InkRecognitionResult = Int32
DISPID_InkRecognitionResult_TopString: DISPID_InkRecognitionResult = 1
DISPID_InkRecognitionResult_TopAlternate: DISPID_InkRecognitionResult = 2
DISPID_InkRecognitionResult_Strokes: DISPID_InkRecognitionResult = 3
DISPID_InkRecognitionResult_TopConfidence: DISPID_InkRecognitionResult = 4
DISPID_InkRecognitionResult_AlternatesFromSelection: DISPID_InkRecognitionResult = 5
DISPID_InkRecognitionResult_ModifyTopAlternate: DISPID_InkRecognitionResult = 6
DISPID_InkRecognitionResult_SetResultOnStrokes: DISPID_InkRecognitionResult = 7
DISPID_InkRecognizer = Int32
DISPID_RecoClsid: DISPID_InkRecognizer = 1
DISPID_RecoName: DISPID_InkRecognizer = 2
DISPID_RecoVendor: DISPID_InkRecognizer = 3
DISPID_RecoCapabilities: DISPID_InkRecognizer = 4
DISPID_RecoLanguageID: DISPID_InkRecognizer = 5
DISPID_RecoPreferredPacketDescription: DISPID_InkRecognizer = 6
DISPID_RecoCreateRecognizerContext: DISPID_InkRecognizer = 7
DISPID_RecoSupportedProperties: DISPID_InkRecognizer = 8
DISPID_InkRecognizer2 = Int32
DISPID_RecoId: DISPID_InkRecognizer2 = 0
DISPID_RecoUnicodeRanges: DISPID_InkRecognizer2 = 1
DISPID_InkRecognizerGuide = Int32
DISPID_IRGWritingBox: DISPID_InkRecognizerGuide = 1
DISPID_IRGDrawnBox: DISPID_InkRecognizerGuide = 2
DISPID_IRGRows: DISPID_InkRecognizerGuide = 3
DISPID_IRGColumns: DISPID_InkRecognizerGuide = 4
DISPID_IRGMidline: DISPID_InkRecognizerGuide = 5
DISPID_IRGGuideData: DISPID_InkRecognizerGuide = 6
DISPID_InkRecognizers = Int32
DISPID_IRecos_NewEnum: DISPID_InkRecognizers = -4
DISPID_IRecosItem: DISPID_InkRecognizers = 0
DISPID_IRecosCount: DISPID_InkRecognizers = 1
DISPID_IRecosGetDefaultRecognizer: DISPID_InkRecognizers = 2
DISPID_InkRectangle = Int32
DISPID_IRTop: DISPID_InkRectangle = 1
DISPID_IRLeft: DISPID_InkRectangle = 2
DISPID_IRBottom: DISPID_InkRectangle = 3
DISPID_IRRight: DISPID_InkRectangle = 4
DISPID_IRGetRectangle: DISPID_InkRectangle = 5
DISPID_IRSetRectangle: DISPID_InkRectangle = 6
DISPID_IRData: DISPID_InkRectangle = 7
DISPID_InkRenderer = Int32
DISPID_IRGetViewTransform: DISPID_InkRenderer = 1
DISPID_IRSetViewTransform: DISPID_InkRenderer = 2
DISPID_IRGetObjectTransform: DISPID_InkRenderer = 3
DISPID_IRSetObjectTransform: DISPID_InkRenderer = 4
DISPID_IRDraw: DISPID_InkRenderer = 5
DISPID_IRDrawStroke: DISPID_InkRenderer = 6
DISPID_IRPixelToInkSpace: DISPID_InkRenderer = 7
DISPID_IRInkSpaceToPixel: DISPID_InkRenderer = 8
DISPID_IRPixelToInkSpaceFromPoints: DISPID_InkRenderer = 9
DISPID_IRInkSpaceToPixelFromPoints: DISPID_InkRenderer = 10
DISPID_IRMeasure: DISPID_InkRenderer = 11
DISPID_IRMeasureStroke: DISPID_InkRenderer = 12
DISPID_IRMove: DISPID_InkRenderer = 13
DISPID_IRRotate: DISPID_InkRenderer = 14
DISPID_IRScale: DISPID_InkRenderer = 15
DISPID_InkStrokeDisp = Int32
DISPID_ISDInkIndex: DISPID_InkStrokeDisp = 1
DISPID_ISDID: DISPID_InkStrokeDisp = 2
DISPID_ISDGetBoundingBox: DISPID_InkStrokeDisp = 3
DISPID_ISDDrawingAttributes: DISPID_InkStrokeDisp = 4
DISPID_ISDFindIntersections: DISPID_InkStrokeDisp = 5
DISPID_ISDGetRectangleIntersections: DISPID_InkStrokeDisp = 6
DISPID_ISDClip: DISPID_InkStrokeDisp = 7
DISPID_ISDHitTestCircle: DISPID_InkStrokeDisp = 8
DISPID_ISDNearestPoint: DISPID_InkStrokeDisp = 9
DISPID_ISDSplit: DISPID_InkStrokeDisp = 10
DISPID_ISDExtendedProperties: DISPID_InkStrokeDisp = 11
DISPID_ISDInk: DISPID_InkStrokeDisp = 12
DISPID_ISDBezierPoints: DISPID_InkStrokeDisp = 13
DISPID_ISDPolylineCusps: DISPID_InkStrokeDisp = 14
DISPID_ISDBezierCusps: DISPID_InkStrokeDisp = 15
DISPID_ISDSelfIntersections: DISPID_InkStrokeDisp = 16
DISPID_ISDPacketCount: DISPID_InkStrokeDisp = 17
DISPID_ISDPacketSize: DISPID_InkStrokeDisp = 18
DISPID_ISDPacketDescription: DISPID_InkStrokeDisp = 19
DISPID_ISDDeleted: DISPID_InkStrokeDisp = 20
DISPID_ISDGetPacketDescriptionPropertyMetrics: DISPID_InkStrokeDisp = 21
DISPID_ISDGetPoints: DISPID_InkStrokeDisp = 22
DISPID_ISDSetPoints: DISPID_InkStrokeDisp = 23
DISPID_ISDGetPacketData: DISPID_InkStrokeDisp = 24
DISPID_ISDGetPacketValuesByProperty: DISPID_InkStrokeDisp = 25
DISPID_ISDSetPacketValuesByProperty: DISPID_InkStrokeDisp = 26
DISPID_ISDGetFlattenedBezierPoints: DISPID_InkStrokeDisp = 27
DISPID_ISDScaleToRectangle: DISPID_InkStrokeDisp = 28
DISPID_ISDTransform: DISPID_InkStrokeDisp = 29
DISPID_ISDMove: DISPID_InkStrokeDisp = 30
DISPID_ISDRotate: DISPID_InkStrokeDisp = 31
DISPID_ISDShear: DISPID_InkStrokeDisp = 32
DISPID_ISDScale: DISPID_InkStrokeDisp = 33
DISPID_InkStrokes = Int32
DISPID_ISs_NewEnum: DISPID_InkStrokes = -4
DISPID_ISsItem: DISPID_InkStrokes = 0
DISPID_ISsCount: DISPID_InkStrokes = 1
DISPID_ISsValid: DISPID_InkStrokes = 2
DISPID_ISsInk: DISPID_InkStrokes = 3
DISPID_ISsAdd: DISPID_InkStrokes = 4
DISPID_ISsAddStrokes: DISPID_InkStrokes = 5
DISPID_ISsRemove: DISPID_InkStrokes = 6
DISPID_ISsRemoveStrokes: DISPID_InkStrokes = 7
DISPID_ISsToString: DISPID_InkStrokes = 8
DISPID_ISsModifyDrawingAttributes: DISPID_InkStrokes = 9
DISPID_ISsGetBoundingBox: DISPID_InkStrokes = 10
DISPID_ISsScaleToRectangle: DISPID_InkStrokes = 11
DISPID_ISsTransform: DISPID_InkStrokes = 12
DISPID_ISsMove: DISPID_InkStrokes = 13
DISPID_ISsRotate: DISPID_InkStrokes = 14
DISPID_ISsShear: DISPID_InkStrokes = 15
DISPID_ISsScale: DISPID_InkStrokes = 16
DISPID_ISsClip: DISPID_InkStrokes = 17
DISPID_ISsRecognitionResult: DISPID_InkStrokes = 18
DISPID_ISsRemoveRecognitionResult: DISPID_InkStrokes = 19
DISPID_InkTablet = Int32
DISPID_ITName: DISPID_InkTablet = 0
DISPID_ITPlugAndPlayId: DISPID_InkTablet = 1
DISPID_ITPropertyMetrics: DISPID_InkTablet = 2
DISPID_ITIsPacketPropertySupported: DISPID_InkTablet = 3
DISPID_ITMaximumInputRectangle: DISPID_InkTablet = 4
DISPID_ITHardwareCapabilities: DISPID_InkTablet = 5
DISPID_InkTablet2 = Int32
DISPID_IT2DeviceKind: DISPID_InkTablet2 = 0
DISPID_InkTablet3 = Int32
DISPID_IT3IsMultiTouch: DISPID_InkTablet3 = 0
DISPID_IT3MaximumCursors: DISPID_InkTablet3 = 1
DISPID_InkTablets = Int32
DISPID_ITs_NewEnum: DISPID_InkTablets = -4
DISPID_ITsItem: DISPID_InkTablets = 0
DISPID_ITsDefaultTablet: DISPID_InkTablets = 1
DISPID_ITsCount: DISPID_InkTablets = 2
DISPID_ITsIsPacketPropertySupported: DISPID_InkTablets = 3
DISPID_InkTransform = Int32
DISPID_ITReset: DISPID_InkTransform = 1
DISPID_ITTranslate: DISPID_InkTransform = 2
DISPID_ITRotate: DISPID_InkTransform = 3
DISPID_ITReflect: DISPID_InkTransform = 4
DISPID_ITShear: DISPID_InkTransform = 5
DISPID_ITScale: DISPID_InkTransform = 6
DISPID_ITeM11: DISPID_InkTransform = 7
DISPID_ITeM12: DISPID_InkTransform = 8
DISPID_ITeM21: DISPID_InkTransform = 9
DISPID_ITeM22: DISPID_InkTransform = 10
DISPID_ITeDx: DISPID_InkTransform = 11
DISPID_ITeDy: DISPID_InkTransform = 12
DISPID_ITGetTransform: DISPID_InkTransform = 13
DISPID_ITSetTransform: DISPID_InkTransform = 14
DISPID_ITData: DISPID_InkTransform = 15
DISPID_InkWordList = Int32
DISPID_InkWordList_AddWord: DISPID_InkWordList = 0
DISPID_InkWordList_RemoveWord: DISPID_InkWordList = 1
DISPID_InkWordList_Merge: DISPID_InkWordList = 2
DISPID_InkWordList2 = Int32
DISPID_InkWordList2_AddWords: DISPID_InkWordList2 = 3
DISPID_MathInputControlEvents = Int32
DISPID_MICInsert: DISPID_MathInputControlEvents = 0
DISPID_MICClose: DISPID_MathInputControlEvents = 1
DISPID_MICPaint: DISPID_MathInputControlEvents = 2
DISPID_MICClear: DISPID_MathInputControlEvents = 3
DISPID_PenInputPanel = Int32
DISPID_PIPAttachedEditWindow: DISPID_PenInputPanel = 0
DISPID_PIPFactoid: DISPID_PenInputPanel = 1
DISPID_PIPCurrentPanel: DISPID_PenInputPanel = 2
DISPID_PIPDefaultPanel: DISPID_PenInputPanel = 3
DISPID_PIPVisible: DISPID_PenInputPanel = 4
DISPID_PIPTop: DISPID_PenInputPanel = 5
DISPID_PIPLeft: DISPID_PenInputPanel = 6
DISPID_PIPWidth: DISPID_PenInputPanel = 7
DISPID_PIPHeight: DISPID_PenInputPanel = 8
DISPID_PIPMoveTo: DISPID_PenInputPanel = 9
DISPID_PIPCommitPendingInput: DISPID_PenInputPanel = 10
DISPID_PIPRefresh: DISPID_PenInputPanel = 11
DISPID_PIPBusy: DISPID_PenInputPanel = 12
DISPID_PIPVerticalOffset: DISPID_PenInputPanel = 13
DISPID_PIPHorizontalOffset: DISPID_PenInputPanel = 14
DISPID_PIPEnableTsf: DISPID_PenInputPanel = 15
DISPID_PIPAutoShow: DISPID_PenInputPanel = 16
DISPID_PenInputPanelEvents = Int32
DISPID_PIPEVisibleChanged: DISPID_PenInputPanelEvents = 0
DISPID_PIPEPanelChanged: DISPID_PenInputPanelEvents = 1
DISPID_PIPEInputFailed: DISPID_PenInputPanelEvents = 2
DISPID_PIPEPanelMoving: DISPID_PenInputPanelEvents = 3
DISPID_StrokeEvent = Int32
DISPID_SEStrokesAdded: DISPID_StrokeEvent = 1
DISPID_SEStrokesRemoved: DISPID_StrokeEvent = 2
class DYNAMIC_RENDERER_CACHED_DATA(EasyCastStructure):
    strokeId: Int32
    dynamicRenderer: win32more.Windows.Win32.UI.TabletPC.IDynamicRenderer
DynamicRenderer = Guid('{ecd32aea-746f-4dcb-bf68-082757faff18}')
EventMask = Int32
EventMask_InPlaceStateChanging: EventMask = 1
EventMask_InPlaceStateChanged: EventMask = 2
EventMask_InPlaceSizeChanging: EventMask = 4
EventMask_InPlaceSizeChanged: EventMask = 8
EventMask_InputAreaChanging: EventMask = 16
EventMask_InputAreaChanged: EventMask = 32
EventMask_CorrectionModeChanging: EventMask = 64
EventMask_CorrectionModeChanged: EventMask = 128
EventMask_InPlaceVisibilityChanging: EventMask = 256
EventMask_InPlaceVisibilityChanged: EventMask = 512
EventMask_TextInserting: EventMask = 1024
EventMask_TextInserted: EventMask = 2048
EventMask_All: EventMask = 4095
FLICKACTION_COMMANDCODE = Int32
FLICKACTION_COMMANDCODE_NULL: FLICKACTION_COMMANDCODE = 0
FLICKACTION_COMMANDCODE_SCROLL: FLICKACTION_COMMANDCODE = 1
FLICKACTION_COMMANDCODE_APPCOMMAND: FLICKACTION_COMMANDCODE = 2
FLICKACTION_COMMANDCODE_CUSTOMKEY: FLICKACTION_COMMANDCODE = 3
FLICKACTION_COMMANDCODE_KEYMODIFIER: FLICKACTION_COMMANDCODE = 4
FLICKDIRECTION = Int32
FLICKDIRECTION_MIN: FLICKDIRECTION = 0
FLICKDIRECTION_RIGHT: FLICKDIRECTION = 0
FLICKDIRECTION_UPRIGHT: FLICKDIRECTION = 1
FLICKDIRECTION_UP: FLICKDIRECTION = 2
FLICKDIRECTION_UPLEFT: FLICKDIRECTION = 3
FLICKDIRECTION_LEFT: FLICKDIRECTION = 4
FLICKDIRECTION_DOWNLEFT: FLICKDIRECTION = 5
FLICKDIRECTION_DOWN: FLICKDIRECTION = 6
FLICKDIRECTION_DOWNRIGHT: FLICKDIRECTION = 7
FLICKDIRECTION_INVALID: FLICKDIRECTION = 8
FLICKMODE = Int32
FLICKMODE_MIN: FLICKMODE = 0
FLICKMODE_OFF: FLICKMODE = 0
FLICKMODE_ON: FLICKMODE = 1
FLICKMODE_LEARNING: FLICKMODE = 2
FLICKMODE_MAX: FLICKMODE = 2
FLICKMODE_DEFAULT: FLICKMODE = 1
class FLICK_DATA(EasyCastStructure):
    _bitfield: Int32
class FLICK_POINT(EasyCastStructure):
    _bitfield: Int32
class GESTURE_DATA(EasyCastStructure):
    gestureId: Int32
    recoConfidence: Int32
    strokeCount: Int32
GET_DANDIDATE_FLAGS = Int32
TCF_ALLOW_RECOGNITION: GET_DANDIDATE_FLAGS = 1
TCF_FORCE_RECOGNITION: GET_DANDIDATE_FLAGS = 2
GestureRecognizer = Guid('{ea30c654-c62c-441f-ac00-95f9a196782c}')
HRECOALT = IntPtr
HRECOCONTEXT = IntPtr
HRECOGNIZER = IntPtr
HRECOLATTICE = IntPtr
HRECOWORDLIST = IntPtr
HandwrittenTextInsertion = Guid('{9f074ee2-e6e9-4d8a-a047-eb5b5c3c55da}')
class IDynamicRenderer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a079468e-7165-46f9-b7af-98ad01a93009}')
    @commethod(3)
    def get_Enabled(self, bEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Enabled(self, bEnabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_HWND(self, hwnd: POINTER(win32more.Windows.Win32.Foundation.HANDLE_PTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_HWND(self, hwnd: win32more.Windows.Win32.Foundation.HANDLE_PTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_ClipRectangle(self, prcClipRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_ClipRectangle(self, prcClipRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ClipRegion(self, phClipRgn: POINTER(win32more.Windows.Win32.Foundation.HANDLE_PTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ClipRegion(self, hClipRgn: win32more.Windows.Win32.Foundation.HANDLE_PTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DrawingAttributes(self, ppiDA: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def putref_DrawingAttributes(self, piDA: win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_DataCacheEnabled(self, pfCacheData: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_DataCacheEnabled(self, fCacheData: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ReleaseCachedData(self, strokeId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Draw(self, hDC: win32more.Windows.Win32.Foundation.HANDLE_PTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEC_GESTUREINFO(EasyCastStructure):
    nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
    Cursor: win32more.Windows.Win32.UI.TabletPC.IInkCursor
    Strokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes
    Gestures: win32more.Windows.Win32.System.Variant.VARIANT
class IEC_RECOGNITIONRESULTINFO(EasyCastStructure):
    nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
    RecognitionResult: win32more.Windows.Win32.UI.TabletPC.IInkRecognitionResult
class IEC_STROKEINFO(EasyCastStructure):
    nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
    Cursor: win32more.Windows.Win32.UI.TabletPC.IInkCursor
    Stroke: win32more.Windows.Win32.UI.TabletPC.IInkStrokeDisp
class IGestureRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ae9ef86b-7054-45e3-ae22-3174dc8811b7}')
    @commethod(3)
    def get_Enabled(self, pfEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Enabled(self, fEnabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_MaxStrokeCount(self, pcStrokes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_MaxStrokeCount(self, cStrokes: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnableGestures(self, cGestures: UInt32, pGestures: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHandwrittenTextInsertion(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56fdea97-ecd6-43e7-aa3a-816be7785860}')
    @commethod(3)
    def InsertRecognitionResultsArray(self, psaAlternates: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), locale: UInt32, fAlternateContainsAutoSpacingInformation: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InsertInkRecognitionResult(self, pIInkRecoResult: win32more.Windows.Win32.UI.TabletPC.IInkRecognitionResult, locale: UInt32, fAlternateContainsAutoSpacingInformation: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInk(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03f8e511-43a1-11d3-8bb6-0080c7d6bad5}')
class IInkCollector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f0f060b5-8b1f-4a7c-89ec-880692588a4f}')
    @commethod(7)
    def get_hWnd(self, CurrentWindow: POINTER(IntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_hWnd(self, NewWindow: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Enabled(self, Collecting: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Enabled(self, Collecting: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DefaultDrawingAttributes(self, CurrentAttributes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def putref_DefaultDrawingAttributes(self, NewAttributes: win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Renderer(self, CurrentInkRenderer: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRenderer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def putref_Renderer(self, NewInkRenderer: win32more.Windows.Win32.UI.TabletPC.IInkRenderer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Ink(self, Ink: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def putref_Ink(self, NewInk: win32more.Windows.Win32.UI.TabletPC.IInkDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AutoRedraw(self, AutoRedraw: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AutoRedraw(self, AutoRedraw: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_CollectingInk(self, Collecting: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_CollectionMode(self, Mode: POINTER(win32more.Windows.Win32.UI.TabletPC.InkCollectionMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_CollectionMode(self, Mode: win32more.Windows.Win32.UI.TabletPC.InkCollectionMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_DynamicRendering(self, Enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_DynamicRendering(self, Enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_DesiredPacketDescription(self, PacketGuids: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_DesiredPacketDescription(self, PacketGuids: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_MouseIcon(self, MouseIcon: POINTER(win32more.Windows.Win32.System.Ole.IPictureDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_MouseIcon(self, MouseIcon: win32more.Windows.Win32.System.Ole.IPictureDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def putref_MouseIcon(self, MouseIcon: win32more.Windows.Win32.System.Ole.IPictureDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_MousePointer(self, MousePointer: POINTER(win32more.Windows.Win32.UI.TabletPC.InkMousePointer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_MousePointer(self, MousePointer: win32more.Windows.Win32.UI.TabletPC.InkMousePointer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_Cursors(self, Cursors: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkCursors)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_MarginX(self, MarginX: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_MarginX(self, MarginX: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_MarginY(self, MarginY: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_MarginY(self, MarginY: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_Tablet(self, SingleTablet: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkTablet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_SupportHighContrastInk(self, Support: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_SupportHighContrastInk(self, Support: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetGestureStatus(self, Gesture: win32more.Windows.Win32.UI.TabletPC.InkApplicationGesture, Listen: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetGestureStatus(self, Gesture: win32more.Windows.Win32.UI.TabletPC.InkApplicationGesture, Listening: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetWindowInputRectangle(self, WindowInputRectangle: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRectangle)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def SetWindowInputRectangle(self, WindowInputRectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def SetAllTabletsMode(self, UseMouseForInput: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def SetSingleTabletIntegratedMode(self, Tablet: win32more.Windows.Win32.UI.TabletPC.IInkTablet) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def GetEventInterest(self, EventId: win32more.Windows.Win32.UI.TabletPC.InkCollectorEventInterest, Listen: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def SetEventInterest(self, EventId: win32more.Windows.Win32.UI.TabletPC.InkCollectorEventInterest, Listen: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkCursor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ad30c630-40c5-4350-8405-9c71012fc558}')
    @commethod(7)
    def get_Name(self, Name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, Id: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Inverted(self, Status: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DrawingAttributes(self, Attributes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def putref_DrawingAttributes(self, Attributes: win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Tablet(self, Tablet: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkTablet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Buttons(self, Buttons: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkCursorButtons)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkCursorButton(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{85ef9417-1d59-49b2-a13c-702c85430894}')
    @commethod(7)
    def get_Name(self, Name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, Id: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_State(self, CurrentState: POINTER(win32more.Windows.Win32.UI.TabletPC.InkCursorButtonState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkCursorButtons(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3671cc40-b624-4671-9fa0-db119d952d54}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, _NewEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Item(self, Identifier: win32more.Windows.Win32.System.Variant.VARIANT, Button: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkCursorButton)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkCursors(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a248c1ac-c698-4e06-9e5c-d57f77c7e647}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, _NewEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Item(self, Index: Int32, Cursor: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkCursor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkCustomStrokes(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7e23a88f-c30e-420f-9bdb-28902543f0c1}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, _NewEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Item(self, Identifier: win32more.Windows.Win32.System.Variant.VARIANT, Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, Name: win32more.Windows.Win32.Foundation.BSTR, Strokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, Identifier: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkDisp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9d398fa0-c4e2-4fcd-9973-975caaf47ea6}')
    @commethod(7)
    def get_Strokes(self, Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_ExtendedProperties(self, Properties: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkExtendedProperties)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Dirty(self, Dirty: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Dirty(self, Dirty: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CustomStrokes(self, ppunkInkCustomStrokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkCustomStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetBoundingBox(self, BoundingBoxMode: win32more.Windows.Win32.UI.TabletPC.InkBoundingBoxMode, Rectangle: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRectangle)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteStrokes(self, Strokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def DeleteStroke(self, Stroke: win32more.Windows.Win32.UI.TabletPC.IInkStrokeDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ExtractStrokes(self, Strokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes, ExtractFlags: win32more.Windows.Win32.UI.TabletPC.InkExtractFlags, ExtractedInk: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ExtractWithRectangle(self, Rectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle, extractFlags: win32more.Windows.Win32.UI.TabletPC.InkExtractFlags, ExtractedInk: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Clip(self, Rectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Clone(self, NewInk: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def HitTestCircle(self, X: Int32, Y: Int32, radius: Single, Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def HitTestWithRectangle(self, SelectionRectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle, IntersectPercent: Single, Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def HitTestWithLasso(self, Points: win32more.Windows.Win32.System.Variant.VARIANT, IntersectPercent: Single, LassoPoints: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def NearestPoint(self, X: Int32, Y: Int32, PointOnStroke: POINTER(Single), DistanceFromPacket: POINTER(Single), Stroke: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokeDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreateStrokes(self, StrokeIds: win32more.Windows.Win32.System.Variant.VARIANT, Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def AddStrokesAtRectangle(self, SourceStrokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes, TargetRectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Save(self, PersistenceFormat: win32more.Windows.Win32.UI.TabletPC.InkPersistenceFormat, CompressionMode: win32more.Windows.Win32.UI.TabletPC.InkPersistenceCompressionMode, Data: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Load(self, Data: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def CreateStroke(self, PacketData: win32more.Windows.Win32.System.Variant.VARIANT, PacketDescription: win32more.Windows.Win32.System.Variant.VARIANT, Stroke: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokeDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def ClipboardCopyWithRectangle(self, Rectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle, ClipboardFormats: win32more.Windows.Win32.UI.TabletPC.InkClipboardFormats, ClipboardModes: win32more.Windows.Win32.UI.TabletPC.InkClipboardModes, DataObject: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def ClipboardCopy(self, strokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes, ClipboardFormats: win32more.Windows.Win32.UI.TabletPC.InkClipboardFormats, ClipboardModes: win32more.Windows.Win32.UI.TabletPC.InkClipboardModes, DataObject: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CanPaste(self, DataObject: win32more.Windows.Win32.System.Com.IDataObject, CanPaste: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def ClipboardPaste(self, x: Int32, y: Int32, DataObject: win32more.Windows.Win32.System.Com.IDataObject, Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkDivider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{5de00405-f9a4-4651-b0c5-c317defd58b9}')
    @commethod(7)
    def get_Strokes(self, Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def putref_Strokes(self, Strokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_RecognizerContext(self, RecognizerContext: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognizerContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def putref_RecognizerContext(self, RecognizerContext: win32more.Windows.Win32.UI.TabletPC.IInkRecognizerContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_LineHeight(self, LineHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_LineHeight(self, LineHeight: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Divide(self, InkDivisionResult: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDivisionResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkDivisionResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2dbec0a7-74c7-4b38-81eb-aa8ef0c24900}')
    @commethod(7)
    def get_Strokes(self, Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResultByType(self, divisionType: win32more.Windows.Win32.UI.TabletPC.InkDivisionType, InkDivisionUnits: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDivisionUnits)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkDivisionUnit(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{85aee342-48b0-4244-9dd5-1ed435410fab}')
    @commethod(7)
    def get_Strokes(self, Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DivisionType(self, divisionType: POINTER(win32more.Windows.Win32.UI.TabletPC.InkDivisionType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_RecognizedString(self, RecoString: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_RotationTransform(self, RotationTransform: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkTransform)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkDivisionUnits(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{1bb5ddc2-31cc-4135-ab82-2c66c9f00c41}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, _NewEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Item(self, Index: Int32, InkDivisionUnit: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDivisionUnit)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkDrawingAttributes(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bf519b75-0a15-4623-adc9-c00d436a8092}')
    @commethod(7)
    def get_Color(self, CurrentColor: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Color(self, NewColor: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Width(self, CurrentWidth: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Width(self, NewWidth: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Height(self, CurrentHeight: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Height(self, NewHeight: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_FitToCurve(self, Flag: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_FitToCurve(self, Flag: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_IgnorePressure(self, Flag: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_IgnorePressure(self, Flag: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AntiAliased(self, Flag: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AntiAliased(self, Flag: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Transparency(self, CurrentTransparency: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_Transparency(self, NewTransparency: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_RasterOperation(self, CurrentRasterOperation: POINTER(win32more.Windows.Win32.UI.TabletPC.InkRasterOperation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_RasterOperation(self, NewRasterOperation: win32more.Windows.Win32.UI.TabletPC.InkRasterOperation) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_PenTip(self, CurrentPenTip: POINTER(win32more.Windows.Win32.UI.TabletPC.InkPenTip)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_PenTip(self, NewPenTip: win32more.Windows.Win32.UI.TabletPC.InkPenTip) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_ExtendedProperties(self, Properties: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkExtendedProperties)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Clone(self, DrawingAttributes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkEdit(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f2127a19-fbfb-4aed-8464-3f36d78cfefb}')
    @commethod(7)
    def get_Status(self, pStatus: POINTER(win32more.Windows.Win32.UI.TabletPC.InkEditStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_UseMouseForInput(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_UseMouseForInput(self, newVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_InkMode(self, pVal: POINTER(win32more.Windows.Win32.UI.TabletPC.InkMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_InkMode(self, newVal: win32more.Windows.Win32.UI.TabletPC.InkMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_InkInsertMode(self, pVal: POINTER(win32more.Windows.Win32.UI.TabletPC.InkInsertMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_InkInsertMode(self, newVal: win32more.Windows.Win32.UI.TabletPC.InkInsertMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_DrawingAttributes(self, pVal: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def putref_DrawingAttributes(self, newVal: win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_RecognitionTimeout(self, pVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_RecognitionTimeout(self, newVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Recognizer(self, pVal: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognizer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def putref_Recognizer(self, newVal: win32more.Windows.Win32.UI.TabletPC.IInkRecognizer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Factoid(self, pVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_Factoid(self, newVal: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_SelInks(self, pSelInk: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_SelInks(self, SelInk: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_SelInksDisplayMode(self, pInkDisplayMode: POINTER(win32more.Windows.Win32.UI.TabletPC.InkDisplayMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_SelInksDisplayMode(self, InkDisplayMode: win32more.Windows.Win32.UI.TabletPC.InkDisplayMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Recognize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetGestureStatus(self, Gesture: win32more.Windows.Win32.UI.TabletPC.InkApplicationGesture, pListen: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetGestureStatus(self, Gesture: win32more.Windows.Win32.UI.TabletPC.InkApplicationGesture, Listen: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_BackColor(self, clr: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_BackColor(self, pclr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_Appearance(self, pAppearance: POINTER(win32more.Windows.Win32.UI.TabletPC.AppearanceConstants)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_Appearance(self, pAppearance: win32more.Windows.Win32.UI.TabletPC.AppearanceConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_BorderStyle(self, pBorderStyle: POINTER(win32more.Windows.Win32.UI.TabletPC.BorderStyleConstants)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_BorderStyle(self, pBorderStyle: win32more.Windows.Win32.UI.TabletPC.BorderStyleConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_Hwnd(self, pohHwnd: POINTER(win32more.Windows.Win32.System.Ole.OLE_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_Font(self, ppFont: POINTER(win32more.Windows.Win32.System.Ole.IFontDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def putref_Font(self, ppFont: win32more.Windows.Win32.System.Ole.IFontDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_Text(self, pbstrText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_Text(self, pbstrText: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_MouseIcon(self, MouseIcon: POINTER(win32more.Windows.Win32.System.Ole.IPictureDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_MouseIcon(self, MouseIcon: win32more.Windows.Win32.System.Ole.IPictureDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def putref_MouseIcon(self, MouseIcon: win32more.Windows.Win32.System.Ole.IPictureDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_MousePointer(self, MousePointer: POINTER(win32more.Windows.Win32.UI.TabletPC.InkMousePointer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def put_MousePointer(self, MousePointer: win32more.Windows.Win32.UI.TabletPC.InkMousePointer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_Locked(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_Locked(self, newVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def get_Enabled(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def put_Enabled(self, newVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_MaxLength(self, plMaxLength: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def put_MaxLength(self, lMaxLength: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def get_MultiLine(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def put_MultiLine(self, newVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_ScrollBars(self, pVal: POINTER(win32more.Windows.Win32.UI.TabletPC.ScrollBarsConstants)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def put_ScrollBars(self, newVal: win32more.Windows.Win32.UI.TabletPC.ScrollBarsConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_DisableNoScroll(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def put_DisableNoScroll(self, newVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_SelAlignment(self, pvarSelAlignment: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def put_SelAlignment(self, pvarSelAlignment: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_SelBold(self, pvarSelBold: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def put_SelBold(self, pvarSelBold: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def get_SelItalic(self, pvarSelItalic: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def put_SelItalic(self, pvarSelItalic: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def get_SelUnderline(self, pvarSelUnderline: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def put_SelUnderline(self, pvarSelUnderline: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_SelColor(self, pvarSelColor: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def put_SelColor(self, pvarSelColor: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def get_SelFontName(self, pvarSelFontName: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def put_SelFontName(self, pvarSelFontName: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def get_SelFontSize(self, pvarSelFontSize: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def put_SelFontSize(self, pvarSelFontSize: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def get_SelCharOffset(self, pvarSelCharOffset: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def put_SelCharOffset(self, pvarSelCharOffset: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def get_TextRTF(self, pbstrTextRTF: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def put_TextRTF(self, pbstrTextRTF: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def get_SelStart(self, plSelStart: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def put_SelStart(self, plSelStart: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def get_SelLength(self, plSelLength: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def put_SelLength(self, plSelLength: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def get_SelText(self, pbstrSelText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def put_SelText(self, pbstrSelText: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def get_SelRTF(self, pbstrSelRTF: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def put_SelRTF(self, pbstrSelRTF: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkExtendedProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{89f2a8be-95a9-4530-8b8f-88e971e3e25f}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, _NewEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Item(self, Identifier: win32more.Windows.Win32.System.Variant.VARIANT, Item: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkExtendedProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, Guid: win32more.Windows.Win32.Foundation.BSTR, Data: win32more.Windows.Win32.System.Variant.VARIANT, InkExtendedProperty: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkExtendedProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, Identifier: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DoesPropertyExist(self, Guid: win32more.Windows.Win32.Foundation.BSTR, DoesPropertyExist: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkExtendedProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{db489209-b7c3-411d-90f6-1548cfff271e}')
    @commethod(7)
    def get_Guid(self, Guid: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Data(self, Data: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Data(self, Data: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkGesture(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3bdc0a97-04e5-4e26-b813-18f052d41def}')
    @commethod(7)
    def get_Confidence(self, Confidence: POINTER(win32more.Windows.Win32.UI.TabletPC.InkRecognitionConfidence)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, Id: POINTER(win32more.Windows.Win32.UI.TabletPC.InkApplicationGesture)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetHotPoint(self, X: POINTER(Int32), Y: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkLineInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9c1c5ad6-f22f-4de4-b453-a2cc482e7c33}')
    @commethod(3)
    def SetFormat(self, pim: POINTER(win32more.Windows.Win32.UI.TabletPC.INKMETRIC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFormat(self, pim: POINTER(win32more.Windows.Win32.UI.TabletPC.INKMETRIC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInkExtent(self, pim: POINTER(win32more.Windows.Win32.UI.TabletPC.INKMETRIC), pnWidth: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCandidate(self, nCandidateNum: UInt32, pwcRecogWord: win32more.Windows.Win32.Foundation.PWSTR, pcwcRecogWord: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetCandidate(self, nCandidateNum: UInt32, strRecogWord: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Recognize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkOverlay(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b82a463b-c1c5-45a3-997c-deab5651b67a}')
    @commethod(7)
    def get_hWnd(self, CurrentWindow: POINTER(IntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_hWnd(self, NewWindow: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Enabled(self, Collecting: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Enabled(self, Collecting: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_DefaultDrawingAttributes(self, CurrentAttributes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def putref_DefaultDrawingAttributes(self, NewAttributes: win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Renderer(self, CurrentInkRenderer: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRenderer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def putref_Renderer(self, NewInkRenderer: win32more.Windows.Win32.UI.TabletPC.IInkRenderer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Ink(self, Ink: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def putref_Ink(self, NewInk: win32more.Windows.Win32.UI.TabletPC.IInkDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_AutoRedraw(self, AutoRedraw: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_AutoRedraw(self, AutoRedraw: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_CollectingInk(self, Collecting: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_CollectionMode(self, Mode: POINTER(win32more.Windows.Win32.UI.TabletPC.InkCollectionMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_CollectionMode(self, Mode: win32more.Windows.Win32.UI.TabletPC.InkCollectionMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_DynamicRendering(self, Enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_DynamicRendering(self, Enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_DesiredPacketDescription(self, PacketGuids: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_DesiredPacketDescription(self, PacketGuids: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_MouseIcon(self, MouseIcon: POINTER(win32more.Windows.Win32.System.Ole.IPictureDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_MouseIcon(self, MouseIcon: win32more.Windows.Win32.System.Ole.IPictureDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def putref_MouseIcon(self, MouseIcon: win32more.Windows.Win32.System.Ole.IPictureDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_MousePointer(self, MousePointer: POINTER(win32more.Windows.Win32.UI.TabletPC.InkMousePointer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_MousePointer(self, MousePointer: win32more.Windows.Win32.UI.TabletPC.InkMousePointer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_EditingMode(self, EditingMode: POINTER(win32more.Windows.Win32.UI.TabletPC.InkOverlayEditingMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_EditingMode(self, EditingMode: win32more.Windows.Win32.UI.TabletPC.InkOverlayEditingMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_Selection(self, Selection: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_Selection(self, Selection: win32more.Windows.Win32.UI.TabletPC.IInkStrokes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_EraserMode(self, EraserMode: POINTER(win32more.Windows.Win32.UI.TabletPC.InkOverlayEraserMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_EraserMode(self, EraserMode: win32more.Windows.Win32.UI.TabletPC.InkOverlayEraserMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_EraserWidth(self, EraserWidth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_EraserWidth(self, newEraserWidth: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_AttachMode(self, AttachMode: POINTER(win32more.Windows.Win32.UI.TabletPC.InkOverlayAttachMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_AttachMode(self, AttachMode: win32more.Windows.Win32.UI.TabletPC.InkOverlayAttachMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_Cursors(self, Cursors: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkCursors)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_MarginX(self, MarginX: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_MarginX(self, MarginX: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_MarginY(self, MarginY: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_MarginY(self, MarginY: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_Tablet(self, SingleTablet: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkTablet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def get_SupportHighContrastInk(self, Support: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def put_SupportHighContrastInk(self, Support: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_SupportHighContrastSelectionUI(self, Support: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def put_SupportHighContrastSelectionUI(self, Support: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def HitTestSelection(self, x: Int32, y: Int32, SelArea: POINTER(win32more.Windows.Win32.UI.TabletPC.SelectionHitResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def Draw(self, Rect: win32more.Windows.Win32.UI.TabletPC.IInkRectangle) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def SetGestureStatus(self, Gesture: win32more.Windows.Win32.UI.TabletPC.InkApplicationGesture, Listen: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def GetGestureStatus(self, Gesture: win32more.Windows.Win32.UI.TabletPC.InkApplicationGesture, Listening: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def GetWindowInputRectangle(self, WindowInputRectangle: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRectangle)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def SetWindowInputRectangle(self, WindowInputRectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def SetAllTabletsMode(self, UseMouseForInput: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def SetSingleTabletIntegratedMode(self, Tablet: win32more.Windows.Win32.UI.TabletPC.IInkTablet) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def GetEventInterest(self, EventId: win32more.Windows.Win32.UI.TabletPC.InkCollectorEventInterest, Listen: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def SetEventInterest(self, EventId: win32more.Windows.Win32.UI.TabletPC.InkCollectorEventInterest, Listen: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkPicture(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e85662e0-379a-40d7-9b5c-757d233f9923}')
    @commethod(7)
    def get_hWnd(self, CurrentWindow: POINTER(IntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DefaultDrawingAttributes(self, CurrentAttributes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def putref_DefaultDrawingAttributes(self, NewAttributes: win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Renderer(self, CurrentInkRenderer: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRenderer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def putref_Renderer(self, NewInkRenderer: win32more.Windows.Win32.UI.TabletPC.IInkRenderer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Ink(self, Ink: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def putref_Ink(self, NewInk: win32more.Windows.Win32.UI.TabletPC.IInkDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_AutoRedraw(self, AutoRedraw: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_AutoRedraw(self, AutoRedraw: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_CollectingInk(self, Collecting: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_CollectionMode(self, Mode: POINTER(win32more.Windows.Win32.UI.TabletPC.InkCollectionMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_CollectionMode(self, Mode: win32more.Windows.Win32.UI.TabletPC.InkCollectionMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_DynamicRendering(self, Enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_DynamicRendering(self, Enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_DesiredPacketDescription(self, PacketGuids: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_DesiredPacketDescription(self, PacketGuids: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_MouseIcon(self, MouseIcon: POINTER(win32more.Windows.Win32.System.Ole.IPictureDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_MouseIcon(self, MouseIcon: win32more.Windows.Win32.System.Ole.IPictureDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def putref_MouseIcon(self, MouseIcon: win32more.Windows.Win32.System.Ole.IPictureDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_MousePointer(self, MousePointer: POINTER(win32more.Windows.Win32.UI.TabletPC.InkMousePointer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_MousePointer(self, MousePointer: win32more.Windows.Win32.UI.TabletPC.InkMousePointer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_EditingMode(self, EditingMode: POINTER(win32more.Windows.Win32.UI.TabletPC.InkOverlayEditingMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_EditingMode(self, EditingMode: win32more.Windows.Win32.UI.TabletPC.InkOverlayEditingMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Selection(self, Selection: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_Selection(self, Selection: win32more.Windows.Win32.UI.TabletPC.IInkStrokes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_EraserMode(self, EraserMode: POINTER(win32more.Windows.Win32.UI.TabletPC.InkOverlayEraserMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_EraserMode(self, EraserMode: win32more.Windows.Win32.UI.TabletPC.InkOverlayEraserMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_EraserWidth(self, EraserWidth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_EraserWidth(self, newEraserWidth: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def putref_Picture(self, pPicture: win32more.Windows.Win32.System.Ole.IPictureDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_Picture(self, pPicture: win32more.Windows.Win32.System.Ole.IPictureDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_Picture(self, ppPicture: POINTER(win32more.Windows.Win32.System.Ole.IPictureDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_SizeMode(self, smNewSizeMode: win32more.Windows.Win32.UI.TabletPC.InkPictureSizeMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_SizeMode(self, smSizeMode: POINTER(win32more.Windows.Win32.UI.TabletPC.InkPictureSizeMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_BackColor(self, newColor: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_BackColor(self, pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def get_Cursors(self, Cursors: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkCursors)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_MarginX(self, MarginX: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_MarginX(self, MarginX: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_MarginY(self, MarginY: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_MarginY(self, MarginY: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_Tablet(self, SingleTablet: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkTablet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_SupportHighContrastInk(self, Support: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def put_SupportHighContrastInk(self, Support: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def get_SupportHighContrastSelectionUI(self, Support: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def put_SupportHighContrastSelectionUI(self, Support: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def HitTestSelection(self, x: Int32, y: Int32, SelArea: POINTER(win32more.Windows.Win32.UI.TabletPC.SelectionHitResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def SetGestureStatus(self, Gesture: win32more.Windows.Win32.UI.TabletPC.InkApplicationGesture, Listen: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def GetGestureStatus(self, Gesture: win32more.Windows.Win32.UI.TabletPC.InkApplicationGesture, Listening: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def GetWindowInputRectangle(self, WindowInputRectangle: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRectangle)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def SetWindowInputRectangle(self, WindowInputRectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def SetAllTabletsMode(self, UseMouseForInput: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def SetSingleTabletIntegratedMode(self, Tablet: win32more.Windows.Win32.UI.TabletPC.IInkTablet) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def GetEventInterest(self, EventId: win32more.Windows.Win32.UI.TabletPC.InkCollectorEventInterest, Listen: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def SetEventInterest(self, EventId: win32more.Windows.Win32.UI.TabletPC.InkCollectorEventInterest, Listen: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def get_InkEnabled(self, Collecting: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def put_InkEnabled(self, Collecting: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def get_Enabled(self, pbool: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def put_Enabled(self, vbool: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkRecognitionAlternate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b7e660ad-77e4-429b-adda-873780d1fc4a}')
    @commethod(7)
    def get_String(self, RecoString: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Confidence(self, Confidence: POINTER(win32more.Windows.Win32.UI.TabletPC.InkRecognitionConfidence)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Baseline(self, Baseline: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Midline(self, Midline: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Ascender(self, Ascender: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Descender(self, Descender: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_LineNumber(self, LineNumber: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Strokes(self, Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_LineAlternates(self, LineAlternates: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognitionAlternates)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_ConfidenceAlternates(self, ConfidenceAlternates: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognitionAlternates)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetStrokesFromStrokeRanges(self, Strokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes, GetStrokesFromStrokeRanges: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetStrokesFromTextRange(self, selectionStart: POINTER(Int32), selectionLength: POINTER(Int32), GetStrokesFromTextRange: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetTextRangeFromStrokes(self, Strokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes, selectionStart: POINTER(Int32), selectionLength: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def AlternatesWithConstantPropertyValues(self, PropertyType: win32more.Windows.Win32.Foundation.BSTR, AlternatesWithConstantPropertyValues: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognitionAlternates)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetPropertyValue(self, PropertyType: win32more.Windows.Win32.Foundation.BSTR, PropertyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkRecognitionAlternates(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{286a167f-9f19-4c61-9d53-4f07be622b84}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, _NewEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Strokes(self, Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Item(self, Index: Int32, InkRecoAlternate: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognitionAlternate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkRecognitionResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3bc129a8-86cd-45ad-bde8-e0d32d61c16d}')
    @commethod(7)
    def get_TopString(self, TopString: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_TopAlternate(self, TopAlternate: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognitionAlternate)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_TopConfidence(self, TopConfidence: POINTER(win32more.Windows.Win32.UI.TabletPC.InkRecognitionConfidence)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Strokes(self, Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AlternatesFromSelection(self, selectionStart: Int32, selectionLength: Int32, maximumAlternates: Int32, AlternatesFromSelection: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognitionAlternates)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ModifyTopAlternate(self, Alternate: win32more.Windows.Win32.UI.TabletPC.IInkRecognitionAlternate) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetResultOnStrokes(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{782bf7cf-034b-4396-8a32-3a1833cf6b56}')
    @commethod(7)
    def get_Name(self, Name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Vendor(self, Vendor: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Capabilities(self, CapabilitiesFlags: POINTER(win32more.Windows.Win32.UI.TabletPC.InkRecognizerCapabilities)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Languages(self, Languages: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SupportedProperties(self, SupportedProperties: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_PreferredPacketDescription(self, PreferredPacketDescription: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateRecognizerContext(self, Context: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognizerContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkRecognizer2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6110118a-3a75-4ad6-b2aa-04b2b72bbe65}')
    @commethod(7)
    def get_Id(self, pbstrId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_UnicodeRanges(self, UnicodeRanges: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkRecognizerContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c68f52f9-32a3-4625-906c-44fc23b40958}')
    @commethod(7)
    def get_Strokes(self, Strokes: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def putref_Strokes(self, Strokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CharacterAutoCompletionMode(self, Mode: POINTER(win32more.Windows.Win32.UI.TabletPC.InkRecognizerCharacterAutoCompletionMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_CharacterAutoCompletionMode(self, Mode: win32more.Windows.Win32.UI.TabletPC.InkRecognizerCharacterAutoCompletionMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Factoid(self, Factoid: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Factoid(self, factoid: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Guide(self, RecognizerGuide: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognizerGuide)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def putref_Guide(self, RecognizerGuide: win32more.Windows.Win32.UI.TabletPC.IInkRecognizerGuide) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_PrefixText(self, Prefix: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_PrefixText(self, Prefix: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_SuffixText(self, Suffix: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_SuffixText(self, Suffix: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_RecognitionFlags(self, Modes: POINTER(win32more.Windows.Win32.UI.TabletPC.InkRecognitionModes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_RecognitionFlags(self, Modes: win32more.Windows.Win32.UI.TabletPC.InkRecognitionModes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_WordList(self, WordList: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkWordList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def putref_WordList(self, WordList: win32more.Windows.Win32.UI.TabletPC.IInkWordList) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_Recognizer(self, Recognizer: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognizer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Recognize(self, RecognitionStatus: POINTER(win32more.Windows.Win32.UI.TabletPC.InkRecognitionStatus), RecognitionResult: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognitionResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def StopBackgroundRecognition(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def EndInkInput(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def BackgroundRecognize(self, CustomData: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def BackgroundRecognizeWithAlternates(self, CustomData: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def Clone(self, RecoContext: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognizerContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def IsStringSupported(self, String: win32more.Windows.Win32.Foundation.BSTR, Supported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkRecognizerContext2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d6f0e32f-73d8-408e-8e9f-5fea592c363f}')
    @commethod(7)
    def get_EnabledUnicodeRanges(self, UnicodeRanges: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_EnabledUnicodeRanges(self, UnicodeRanges: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkRecognizerGuide(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d934be07-7b84-4208-9136-83c20994e905}')
    @commethod(7)
    def get_WritingBox(self, Rectangle: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRectangle)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_WritingBox(self, Rectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DrawnBox(self, Rectangle: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRectangle)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_DrawnBox(self, Rectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Rows(self, Units: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Rows(self, Units: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Columns(self, Units: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Columns(self, Units: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Midline(self, Units: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Midline(self, Units: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_GuideData(self, pRecoGuide: POINTER(win32more.Windows.Win32.UI.TabletPC.InkRecoGuide)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_GuideData(self, recoGuide: win32more.Windows.Win32.UI.TabletPC.InkRecoGuide) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkRecognizers(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9ccc4f12-b0b7-4a8b-bf58-4aeca4e8cefd}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, _NewEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDefaultRecognizer(self, lcid: Int32, DefaultRecognizer: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognizer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Item(self, Index: Int32, InkRecognizer: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognizer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkRectangle(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9794ff82-6071-4717-8a8b-6ac7c64a686e}')
    @commethod(7)
    def get_Top(self, Units: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Top(self, Units: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Left(self, Units: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Left(self, Units: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Bottom(self, Units: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Bottom(self, Units: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Right(self, Units: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Right(self, Units: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Data(self, Rect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Data(self, Rect: win32more.Windows.Win32.Foundation.RECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetRectangle(self, Top: POINTER(Int32), Left: POINTER(Int32), Bottom: POINTER(Int32), Right: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetRectangle(self, Top: Int32, Left: Int32, Bottom: Int32, Right: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkRenderer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e6257a9c-b511-4f4c-a8b0-a7dbc9506b83}')
    @commethod(7)
    def GetViewTransform(self, ViewTransform: win32more.Windows.Win32.UI.TabletPC.IInkTransform) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetViewTransform(self, ViewTransform: win32more.Windows.Win32.UI.TabletPC.IInkTransform) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetObjectTransform(self, ObjectTransform: win32more.Windows.Win32.UI.TabletPC.IInkTransform) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetObjectTransform(self, ObjectTransform: win32more.Windows.Win32.UI.TabletPC.IInkTransform) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Draw(self, hDC: IntPtr, Strokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DrawStroke(self, hDC: IntPtr, Stroke: win32more.Windows.Win32.UI.TabletPC.IInkStrokeDisp, DrawingAttributes: win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def PixelToInkSpace(self, hDC: IntPtr, x: POINTER(Int32), y: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def InkSpaceToPixel(self, hdcDisplay: IntPtr, x: POINTER(Int32), y: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def PixelToInkSpaceFromPoints(self, hDC: IntPtr, Points: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def InkSpaceToPixelFromPoints(self, hDC: IntPtr, Points: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Measure(self, Strokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes, Rectangle: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRectangle)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def MeasureStroke(self, Stroke: win32more.Windows.Win32.UI.TabletPC.IInkStrokeDisp, DrawingAttributes: win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes, Rectangle: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRectangle)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Move(self, HorizontalComponent: Single, VerticalComponent: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Rotate(self, Degrees: Single, x: Single, y: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ScaleTransform(self, HorizontalMultiplier: Single, VerticalMultiplier: Single, ApplyOnPenWidth: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkStrokeDisp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{43242fea-91d1-4a72-963e-fbb91829cfa2}')
    @commethod(7)
    def get_ID(self, ID: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_BezierPoints(self, Points: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DrawingAttributes(self, DrawAttrs: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def putref_DrawingAttributes(self, DrawAttrs: win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Ink(self, Ink: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_ExtendedProperties(self, Properties: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkExtendedProperties)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_PolylineCusps(self, Cusps: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_BezierCusps(self, Cusps: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_SelfIntersections(self, Intersections: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_PacketCount(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_PacketSize(self, plSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_PacketDescription(self, PacketDescription: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Deleted(self, Deleted: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetBoundingBox(self, BoundingBoxMode: win32more.Windows.Win32.UI.TabletPC.InkBoundingBoxMode, Rectangle: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRectangle)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def FindIntersections(self, Strokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes, Intersections: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetRectangleIntersections(self, Rectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle, Intersections: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Clip(self, Rectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def HitTestCircle(self, X: Int32, Y: Int32, Radius: Single, Intersects: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def NearestPoint(self, X: Int32, Y: Int32, Distance: POINTER(Single), Point: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Split(self, SplitAt: Single, NewStroke: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokeDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetPacketDescriptionPropertyMetrics(self, PropertyName: win32more.Windows.Win32.Foundation.BSTR, Minimum: POINTER(Int32), Maximum: POINTER(Int32), Units: POINTER(win32more.Windows.Win32.UI.TabletPC.TabletPropertyMetricUnit), Resolution: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetPoints(self, Index: Int32, Count: Int32, Points: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetPoints(self, Points: win32more.Windows.Win32.System.Variant.VARIANT, Index: Int32, Count: Int32, NumberOfPointsSet: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetPacketData(self, Index: Int32, Count: Int32, PacketData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetPacketValuesByProperty(self, PropertyName: win32more.Windows.Win32.Foundation.BSTR, Index: Int32, Count: Int32, PacketValues: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetPacketValuesByProperty(self, bstrPropertyName: win32more.Windows.Win32.Foundation.BSTR, PacketValues: win32more.Windows.Win32.System.Variant.VARIANT, Index: Int32, Count: Int32, NumberOfPacketsSet: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetFlattenedBezierPoints(self, FittingError: Int32, FlattenedBezierPoints: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def Transform(self, Transform: win32more.Windows.Win32.UI.TabletPC.IInkTransform, ApplyOnPenWidth: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def ScaleToRectangle(self, Rectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def Move(self, HorizontalComponent: Single, VerticalComponent: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def Rotate(self, Degrees: Single, x: Single, y: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def Shear(self, HorizontalMultiplier: Single, VerticalMultiplier: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def ScaleTransform(self, HorizontalMultiplier: Single, VerticalMultiplier: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkStrokes(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f1f4c9d8-590a-4963-b3ae-1935671bb6f3}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, _NewEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Ink(self, Ink: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_RecognitionResult(self, RecognitionResult: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRecognitionResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ToString(self, ToString: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Item(self, Index: Int32, Stroke: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokeDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Add(self, InkStroke: win32more.Windows.Win32.UI.TabletPC.IInkStrokeDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def AddStrokes(self, InkStrokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Remove(self, InkStroke: win32more.Windows.Win32.UI.TabletPC.IInkStrokeDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RemoveStrokes(self, InkStrokes: win32more.Windows.Win32.UI.TabletPC.IInkStrokes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ModifyDrawingAttributes(self, DrawAttrs: win32more.Windows.Win32.UI.TabletPC.IInkDrawingAttributes) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetBoundingBox(self, BoundingBoxMode: win32more.Windows.Win32.UI.TabletPC.InkBoundingBoxMode, BoundingBox: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRectangle)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Transform(self, Transform: win32more.Windows.Win32.UI.TabletPC.IInkTransform, ApplyOnPenWidth: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ScaleToRectangle(self, Rectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Move(self, HorizontalComponent: Single, VerticalComponent: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Rotate(self, Degrees: Single, x: Single, y: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Shear(self, HorizontalMultiplier: Single, VerticalMultiplier: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def ScaleTransform(self, HorizontalMultiplier: Single, VerticalMultiplier: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Clip(self, Rectangle: win32more.Windows.Win32.UI.TabletPC.IInkRectangle) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def RemoveRecognitionResult(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkTablet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2de25eaa-6ef8-42d5-aee9-185bc81b912d}')
    @commethod(7)
    def get_Name(self, Name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_PlugAndPlayId(self, Id: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_MaximumInputRectangle(self, Rectangle: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkRectangle)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_HardwareCapabilities(self, Capabilities: POINTER(win32more.Windows.Win32.UI.TabletPC.TabletHardwareCapabilities)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsPacketPropertySupported(self, packetPropertyName: win32more.Windows.Win32.Foundation.BSTR, Supported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetPropertyMetrics(self, propertyName: win32more.Windows.Win32.Foundation.BSTR, Minimum: POINTER(Int32), Maximum: POINTER(Int32), Units: POINTER(win32more.Windows.Win32.UI.TabletPC.TabletPropertyMetricUnit), Resolution: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkTablet2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{90c91ad2-fa36-49d6-9516-ce8d570f6f85}')
    @commethod(7)
    def get_DeviceKind(self, Kind: POINTER(win32more.Windows.Win32.UI.TabletPC.TabletDeviceKind)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkTablet3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7e313997-1327-41dd-8ca9-79f24be17250}')
    @commethod(7)
    def get_IsMultiTouch(self, pIsMultiTouch: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_MaximumCursors(self, pMaximumCursors: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkTablets(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{112086d9-7779-4535-a699-862b43ac1863}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, _NewEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DefaultTablet(self, DefaultTablet: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkTablet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Item(self, Index: Int32, Tablet: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkTablet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsPacketPropertySupported(self, packetPropertyName: win32more.Windows.Win32.Foundation.BSTR, Supported: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkTransform(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{615f1d43-8703-4565-88e2-8201d2ecd7b7}')
    @commethod(7)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Translate(self, HorizontalComponent: Single, VerticalComponent: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Rotate(self, Degrees: Single, x: Single, y: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Reflect(self, Horizontally: win32more.Windows.Win32.Foundation.VARIANT_BOOL, Vertically: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Shear(self, HorizontalComponent: Single, VerticalComponent: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ScaleTransform(self, HorizontalMultiplier: Single, VerticalMultiplier: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetTransform(self, eM11: POINTER(Single), eM12: POINTER(Single), eM21: POINTER(Single), eM22: POINTER(Single), eDx: POINTER(Single), eDy: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetTransform(self, eM11: Single, eM12: Single, eM21: Single, eM22: Single, eDx: Single, eDy: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_eM11(self, Value: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_eM11(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_eM12(self, Value: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_eM12(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_eM21(self, Value: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_eM21(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_eM22(self, Value: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_eM22(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_eDx(self, Value: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_eDx(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_eDy(self, Value: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_eDy(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Data(self, XForm: POINTER(win32more.Windows.Win32.Graphics.Gdi.XFORM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_Data(self, XForm: win32more.Windows.Win32.Graphics.Gdi.XFORM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkWordList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{76ba3491-cb2f-406b-9961-0e0c4cdaaef2}')
    @commethod(7)
    def AddWord(self, NewWord: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveWord(self, RemoveWord: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Merge(self, MergeWordList: win32more.Windows.Win32.UI.TabletPC.IInkWordList) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInkWordList2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{14542586-11bf-4f5f-b6e7-49d0744aab6e}')
    @commethod(7)
    def AddWords(self, NewWords: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInputPanelWindowHandle(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4af81847-fdc4-4fc3-ad0b-422479c1b935}')
    @commethod(3)
    def get_AttachedEditWindow32(self, AttachedEditWindow: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_AttachedEditWindow32(self, AttachedEditWindow: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_AttachedEditWindow64(self, AttachedEditWindow: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_AttachedEditWindow64(self, AttachedEditWindow: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMathInputControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{eba615aa-fac6-4738-ba5f-ff09e9fe473e}')
    @commethod(7)
    def Show(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Hide(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsVisible(self, pvbShown: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPosition(self, Left: POINTER(Int32), Top: POINTER(Int32), Right: POINTER(Int32), Bottom: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetPosition(self, Left: Int32, Top: Int32, Right: Int32, Bottom: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetCustomPaint(self, Element: Int32, Paint: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetCaptionText(self, CaptionText: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def LoadInk(self, Ink: win32more.Windows.Win32.UI.TabletPC.IInkDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetOwnerWindow(self, OwnerWindow: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnableExtendedButtons(self, Extended: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetPreviewHeight(self, Height: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetPreviewHeight(self, Height: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def EnableAutoGrow(self, AutoGrow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def AddFunctionName(self, FunctionName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def RemoveFunctionName(self, FunctionName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetHoverIcon(self, HoverImage: POINTER(win32more.Windows.Win32.System.Ole.IPictureDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INKMETRIC(EasyCastStructure):
    iHeight: Int32
    iFontAscent: Int32
    iFontDescent: Int32
    dwFlags: UInt32
    color: win32more.Windows.Win32.Foundation.COLORREF
INK_METRIC_FLAGS = Int32
IMF_FONT_SELECTED_IN_HDC: INK_METRIC_FLAGS = 1
IMF_ITALIC: INK_METRIC_FLAGS = 2
IMF_BOLD: INK_METRIC_FLAGS = 4
class IPenInputPanel(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fa7a4083-5747-4040-a182-0b0e9fd4fac7}')
    @commethod(7)
    def get_Busy(self, Busy: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Factoid(self, Factoid: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Factoid(self, Factoid: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AttachedEditWindow(self, AttachedEditWindow: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_AttachedEditWindow(self, AttachedEditWindow: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CurrentPanel(self, CurrentPanel: POINTER(win32more.Windows.Win32.UI.TabletPC.PanelType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_CurrentPanel(self, CurrentPanel: win32more.Windows.Win32.UI.TabletPC.PanelType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_DefaultPanel(self, pDefaultPanel: POINTER(win32more.Windows.Win32.UI.TabletPC.PanelType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_DefaultPanel(self, DefaultPanel: win32more.Windows.Win32.UI.TabletPC.PanelType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Visible(self, Visible: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Visible(self, Visible: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Top(self, Top: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Left(self, Left: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Width(self, Width: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Height(self, Height: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_VerticalOffset(self, VerticalOffset: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_VerticalOffset(self, VerticalOffset: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_HorizontalOffset(self, HorizontalOffset: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_HorizontalOffset(self, HorizontalOffset: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_AutoShow(self, pAutoShow: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_AutoShow(self, AutoShow: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def MoveTo(self, Left: Int32, Top: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def CommitPendingInput(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def EnableTsf(self, Enable: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRealTimeStylus(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a8bb5d22-3144-4a7b-93cd-f34a16be513a}')
    @commethod(3)
    def get_Enabled(self, pfEnable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Enabled(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_HWND(self, phwnd: POINTER(win32more.Windows.Win32.Foundation.HANDLE_PTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_HWND(self, hwnd: win32more.Windows.Win32.Foundation.HANDLE_PTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_WindowInputRectangle(self, prcWndInputRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_WindowInputRectangle(self, prcWndInputRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddStylusSyncPlugin(self, iIndex: UInt32, piPlugin: win32more.Windows.Win32.UI.TabletPC.IStylusSyncPlugin) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveStylusSyncPlugin(self, iIndex: UInt32, ppiPlugin: POINTER(win32more.Windows.Win32.UI.TabletPC.IStylusSyncPlugin)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveAllStylusSyncPlugins(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetStylusSyncPlugin(self, iIndex: UInt32, ppiPlugin: POINTER(win32more.Windows.Win32.UI.TabletPC.IStylusSyncPlugin)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetStylusSyncPluginCount(self, pcPlugins: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def AddStylusAsyncPlugin(self, iIndex: UInt32, piPlugin: win32more.Windows.Win32.UI.TabletPC.IStylusAsyncPlugin) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RemoveStylusAsyncPlugin(self, iIndex: UInt32, ppiPlugin: POINTER(win32more.Windows.Win32.UI.TabletPC.IStylusAsyncPlugin)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RemoveAllStylusAsyncPlugins(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetStylusAsyncPlugin(self, iIndex: UInt32, ppiPlugin: POINTER(win32more.Windows.Win32.UI.TabletPC.IStylusAsyncPlugin)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetStylusAsyncPluginCount(self, pcPlugins: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ChildRealTimeStylusPlugin(self, ppiRTS: POINTER(win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def putref_ChildRealTimeStylusPlugin(self, piRTS: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def AddCustomStylusDataToQueue(self, sq: win32more.Windows.Win32.UI.TabletPC.StylusQueue, pGuidId: POINTER(Guid), cbData: UInt32, pbData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ClearStylusQueues(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetAllTabletsMode(self, fUseMouseForInput: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetSingleTabletMode(self, piTablet: win32more.Windows.Win32.UI.TabletPC.IInkTablet) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetTablet(self, ppiSingleTablet: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkTablet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetTabletContextIdFromTablet(self, piTablet: win32more.Windows.Win32.UI.TabletPC.IInkTablet, ptcid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetTabletFromTabletContextId(self, tcid: UInt32, ppiTablet: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkTablet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetAllTabletContextIds(self, pcTcidCount: POINTER(UInt32), ppTcids: POINTER(POINTER(UInt32))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetStyluses(self, ppiInkCursors: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkCursors)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetStylusForId(self, sid: UInt32, ppiInkCursor: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkCursor)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetDesiredPacketDescription(self, cProperties: UInt32, pPropertyGuids: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetDesiredPacketDescription(self, pcProperties: POINTER(UInt32), ppPropertyGuids: POINTER(POINTER(Guid))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetPacketDescriptionData(self, tcid: UInt32, pfInkToDeviceScaleX: POINTER(Single), pfInkToDeviceScaleY: POINTER(Single), pcPacketProperties: POINTER(UInt32), ppPacketProperties: POINTER(POINTER(win32more.Windows.Win32.UI.TabletPC.PACKET_PROPERTY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRealTimeStylus2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b5f2a6cd-3179-4a3e-b9c4-bb5865962be2}')
    @commethod(3)
    def get_FlicksEnabled(self, pfEnable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_FlicksEnabled(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRealTimeStylus3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d70230a3-6986-4051-b57a-1cf69f4d9db5}')
    @commethod(3)
    def get_MultiTouchEnabled(self, pfEnable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_MultiTouchEnabled(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRealTimeStylusSynchronization(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aa87eab8-ab4a-4cea-b5cb-46d84c6a2509}')
    @commethod(3)
    def AcquireLock(self, lock: win32more.Windows.Win32.UI.TabletPC.RealTimeStylusLockType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseLock(self, lock: win32more.Windows.Win32.UI.TabletPC.RealTimeStylusLockType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISketchInk(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b4563688-98eb-4646-b279-44da14d45748}')
class IStrokeBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a5fd4e2d-c44b-4092-9177-260905eb672b}')
    @commethod(3)
    def CreateStroke(self, cPktBuffLength: UInt32, pPackets: POINTER(Int32), cPacketProperties: UInt32, pPacketProperties: POINTER(win32more.Windows.Win32.UI.TabletPC.PACKET_PROPERTY), fInkToDeviceScaleX: Single, fInkToDeviceScaleY: Single, ppIInkStroke: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokeDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginStroke(self, tcid: UInt32, sid: UInt32, pPacket: POINTER(Int32), cPacketProperties: UInt32, pPacketProperties: POINTER(win32more.Windows.Win32.UI.TabletPC.PACKET_PROPERTY), fInkToDeviceScaleX: Single, fInkToDeviceScaleY: Single, ppIInkStroke: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokeDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AppendPackets(self, tcid: UInt32, sid: UInt32, cPktBuffLength: UInt32, pPackets: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EndStroke(self, tcid: UInt32, sid: UInt32, ppIInkStroke: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkStrokeDisp), pDirtyRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Ink(self, ppiInkObj: POINTER(win32more.Windows.Win32.UI.TabletPC.IInkDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def putref_Ink(self, piInkObj: win32more.Windows.Win32.UI.TabletPC.IInkDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStylusAsyncPlugin(ComPtr):
    extends: win32more.Windows.Win32.UI.TabletPC.IStylusPlugin
    _iid_ = Guid('{a7cca85a-31bc-4cd2-aadc-3289a3af11c8}')
class IStylusPlugin(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a81436d8-4757-4fd1-a185-133f97c6c545}')
    @commethod(3)
    def RealTimeStylusEnabled(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, cTcidCount: UInt32, pTcids: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RealTimeStylusDisabled(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, cTcidCount: UInt32, pTcids: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StylusInRange(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, tcid: UInt32, sid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def StylusOutOfRange(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, tcid: UInt32, sid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def StylusDown(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, pStylusInfo: POINTER(win32more.Windows.Win32.UI.TabletPC.StylusInfo), cPropCountPerPkt: UInt32, pPacket: POINTER(Int32), ppInOutPkt: POINTER(POINTER(Int32))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StylusUp(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, pStylusInfo: POINTER(win32more.Windows.Win32.UI.TabletPC.StylusInfo), cPropCountPerPkt: UInt32, pPacket: POINTER(Int32), ppInOutPkt: POINTER(POINTER(Int32))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def StylusButtonDown(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, sid: UInt32, pGuidStylusButton: POINTER(Guid), pStylusPos: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def StylusButtonUp(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, sid: UInt32, pGuidStylusButton: POINTER(Guid), pStylusPos: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def InAirPackets(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, pStylusInfo: POINTER(win32more.Windows.Win32.UI.TabletPC.StylusInfo), cPktCount: UInt32, cPktBuffLength: UInt32, pPackets: POINTER(Int32), pcInOutPkts: POINTER(UInt32), ppInOutPkts: POINTER(POINTER(Int32))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Packets(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, pStylusInfo: POINTER(win32more.Windows.Win32.UI.TabletPC.StylusInfo), cPktCount: UInt32, cPktBuffLength: UInt32, pPackets: POINTER(Int32), pcInOutPkts: POINTER(UInt32), ppInOutPkts: POINTER(POINTER(Int32))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CustomStylusDataAdded(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, pGuidId: POINTER(Guid), cbData: UInt32, pbData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SystemEvent(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, tcid: UInt32, sid: UInt32, event: UInt16, eventdata: win32more.Windows.Win32.UI.TabletPC.SYSTEM_EVENT_DATA) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def TabletAdded(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, piTablet: win32more.Windows.Win32.UI.TabletPC.IInkTablet) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def TabletRemoved(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, iTabletIndex: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Error(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus, piPlugin: win32more.Windows.Win32.UI.TabletPC.IStylusPlugin, dataInterest: win32more.Windows.Win32.UI.TabletPC.RealTimeStylusDataInterest, hrErrorCode: win32more.Windows.Win32.Foundation.HRESULT, lptrKey: POINTER(IntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def UpdateMapping(self, piRtsSrc: win32more.Windows.Win32.UI.TabletPC.IRealTimeStylus) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def DataInterest(self, pDataInterest: POINTER(win32more.Windows.Win32.UI.TabletPC.RealTimeStylusDataInterest)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStylusSyncPlugin(ComPtr):
    extends: win32more.Windows.Win32.UI.TabletPC.IStylusPlugin
    _iid_ = Guid('{a157b174-482f-4d71-a3f6-3a41ddd11be9}')
class ITextInputPanel(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6b6a65a5-6af3-46c2-b6ea-56cd1f80df71}')
    @commethod(3)
    def get_AttachedEditWindow(self, AttachedEditWindow: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_AttachedEditWindow(self, AttachedEditWindow: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_CurrentInteractionMode(self, CurrentInteractionMode: POINTER(win32more.Windows.Win32.UI.TabletPC.InteractionMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_DefaultInPlaceState(self, State: POINTER(win32more.Windows.Win32.UI.TabletPC.InPlaceState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_DefaultInPlaceState(self, State: win32more.Windows.Win32.UI.TabletPC.InPlaceState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CurrentInPlaceState(self, State: POINTER(win32more.Windows.Win32.UI.TabletPC.InPlaceState)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DefaultInputArea(self, Area: POINTER(win32more.Windows.Win32.UI.TabletPC.PanelInputArea)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_DefaultInputArea(self, Area: win32more.Windows.Win32.UI.TabletPC.PanelInputArea) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_CurrentInputArea(self, Area: POINTER(win32more.Windows.Win32.UI.TabletPC.PanelInputArea)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CurrentCorrectionMode(self, Mode: POINTER(win32more.Windows.Win32.UI.TabletPC.CorrectionMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_PreferredInPlaceDirection(self, Direction: POINTER(win32more.Windows.Win32.UI.TabletPC.InPlaceDirection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_PreferredInPlaceDirection(self, Direction: win32more.Windows.Win32.UI.TabletPC.InPlaceDirection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ExpandPostInsertionCorrection(self, Expand: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ExpandPostInsertionCorrection(self, Expand: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_InPlaceVisibleOnFocus(self, Visible: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_InPlaceVisibleOnFocus(self, Visible: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_InPlaceBoundingRectangle(self, BoundingRectangle: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_PopUpCorrectionHeight(self, Height: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_PopDownCorrectionHeight(self, Height: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CommitPendingInput(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetInPlaceVisibility(self, Visible: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetInPlacePosition(self, xPosition: Int32, yPosition: Int32, position: win32more.Windows.Win32.UI.TabletPC.CorrectionPosition) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetInPlaceHoverTargetPosition(self, xPosition: Int32, yPosition: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Advise(self, EventSink: win32more.Windows.Win32.UI.TabletPC.ITextInputPanelEventSink, EventMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Unadvise(self, EventSink: win32more.Windows.Win32.UI.TabletPC.ITextInputPanelEventSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextInputPanelEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{27560408-8e64-4fe1-804e-421201584b31}')
    @commethod(3)
    def InPlaceStateChanging(self, oldInPlaceState: win32more.Windows.Win32.UI.TabletPC.InPlaceState, newInPlaceState: win32more.Windows.Win32.UI.TabletPC.InPlaceState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InPlaceStateChanged(self, oldInPlaceState: win32more.Windows.Win32.UI.TabletPC.InPlaceState, newInPlaceState: win32more.Windows.Win32.UI.TabletPC.InPlaceState) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InPlaceSizeChanging(self, oldBoundingRectangle: win32more.Windows.Win32.Foundation.RECT, newBoundingRectangle: win32more.Windows.Win32.Foundation.RECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InPlaceSizeChanged(self, oldBoundingRectangle: win32more.Windows.Win32.Foundation.RECT, newBoundingRectangle: win32more.Windows.Win32.Foundation.RECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InputAreaChanging(self, oldInputArea: win32more.Windows.Win32.UI.TabletPC.PanelInputArea, newInputArea: win32more.Windows.Win32.UI.TabletPC.PanelInputArea) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InputAreaChanged(self, oldInputArea: win32more.Windows.Win32.UI.TabletPC.PanelInputArea, newInputArea: win32more.Windows.Win32.UI.TabletPC.PanelInputArea) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CorrectionModeChanging(self, oldCorrectionMode: win32more.Windows.Win32.UI.TabletPC.CorrectionMode, newCorrectionMode: win32more.Windows.Win32.UI.TabletPC.CorrectionMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CorrectionModeChanged(self, oldCorrectionMode: win32more.Windows.Win32.UI.TabletPC.CorrectionMode, newCorrectionMode: win32more.Windows.Win32.UI.TabletPC.CorrectionMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def InPlaceVisibilityChanging(self, oldVisible: win32more.Windows.Win32.Foundation.BOOL, newVisible: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def InPlaceVisibilityChanged(self, oldVisible: win32more.Windows.Win32.Foundation.BOOL, newVisible: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def TextInserting(self, Ink: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def TextInserted(self, Ink: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextInputPanelRunInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9f424568-1920-48cc-9811-a993cbf5adba}')
    @commethod(3)
    def IsTipRunning(self, pfRunning: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITipAutoCompleteClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5e078e03-8265-4bbe-9487-d242edbef910}')
    @commethod(3)
    def AdviseProvider(self, hWndField: win32more.Windows.Win32.Foundation.HWND, pIProvider: win32more.Windows.Win32.UI.TabletPC.ITipAutoCompleteProvider) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnadviseProvider(self, hWndField: win32more.Windows.Win32.Foundation.HWND, pIProvider: win32more.Windows.Win32.UI.TabletPC.ITipAutoCompleteProvider) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UserSelection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PreferredRects(self, prcACList: POINTER(win32more.Windows.Win32.Foundation.RECT), prcField: POINTER(win32more.Windows.Win32.Foundation.RECT), prcModifiedACList: POINTER(win32more.Windows.Win32.Foundation.RECT), pfShownAboveTip: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RequestShowUI(self, hWndList: win32more.Windows.Win32.Foundation.HWND, pfAllowShowing: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITipAutoCompleteProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7c6cf46d-8404-46b9-ad33-f5b6036d4007}')
    @commethod(3)
    def UpdatePendingText(self, bstrPendingText: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Show(self, fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
InPlaceDirection = Int32
InPlaceDirection_Auto: InPlaceDirection = 0
InPlaceDirection_Bottom: InPlaceDirection = 1
InPlaceDirection_Top: InPlaceDirection = 2
InPlaceState = Int32
InPlaceState_Auto: InPlaceState = 0
InPlaceState_HoverTarget: InPlaceState = 1
InPlaceState_Expanded: InPlaceState = 2
Ink = Guid('{13de4a42-8d21-4c8e-bf9c-8f69cb068fca}')
InkApplicationGesture = Int32
IAG_AllGestures: InkApplicationGesture = 0
IAG_NoGesture: InkApplicationGesture = 61440
IAG_Scratchout: InkApplicationGesture = 61441
IAG_Triangle: InkApplicationGesture = 61442
IAG_Square: InkApplicationGesture = 61443
IAG_Star: InkApplicationGesture = 61444
IAG_Check: InkApplicationGesture = 61445
IAG_Curlicue: InkApplicationGesture = 61456
IAG_DoubleCurlicue: InkApplicationGesture = 61457
IAG_Circle: InkApplicationGesture = 61472
IAG_DoubleCircle: InkApplicationGesture = 61473
IAG_SemiCircleLeft: InkApplicationGesture = 61480
IAG_SemiCircleRight: InkApplicationGesture = 61481
IAG_ChevronUp: InkApplicationGesture = 61488
IAG_ChevronDown: InkApplicationGesture = 61489
IAG_ChevronLeft: InkApplicationGesture = 61490
IAG_ChevronRight: InkApplicationGesture = 61491
IAG_ArrowUp: InkApplicationGesture = 61496
IAG_ArrowDown: InkApplicationGesture = 61497
IAG_ArrowLeft: InkApplicationGesture = 61498
IAG_ArrowRight: InkApplicationGesture = 61499
IAG_Up: InkApplicationGesture = 61528
IAG_Down: InkApplicationGesture = 61529
IAG_Left: InkApplicationGesture = 61530
IAG_Right: InkApplicationGesture = 61531
IAG_UpDown: InkApplicationGesture = 61536
IAG_DownUp: InkApplicationGesture = 61537
IAG_LeftRight: InkApplicationGesture = 61538
IAG_RightLeft: InkApplicationGesture = 61539
IAG_UpLeftLong: InkApplicationGesture = 61540
IAG_UpRightLong: InkApplicationGesture = 61541
IAG_DownLeftLong: InkApplicationGesture = 61542
IAG_DownRightLong: InkApplicationGesture = 61543
IAG_UpLeft: InkApplicationGesture = 61544
IAG_UpRight: InkApplicationGesture = 61545
IAG_DownLeft: InkApplicationGesture = 61546
IAG_DownRight: InkApplicationGesture = 61547
IAG_LeftUp: InkApplicationGesture = 61548
IAG_LeftDown: InkApplicationGesture = 61549
IAG_RightUp: InkApplicationGesture = 61550
IAG_RightDown: InkApplicationGesture = 61551
IAG_Exclamation: InkApplicationGesture = 61604
IAG_Tap: InkApplicationGesture = 61680
IAG_DoubleTap: InkApplicationGesture = 61681
InkBoundingBoxMode = Int32
IBBM_Default: InkBoundingBoxMode = 0
IBBM_NoCurveFit: InkBoundingBoxMode = 1
IBBM_CurveFit: InkBoundingBoxMode = 2
IBBM_PointsOnly: InkBoundingBoxMode = 3
IBBM_Union: InkBoundingBoxMode = 4
InkClipboardFormats = Int32
ICF_None: InkClipboardFormats = 0
ICF_InkSerializedFormat: InkClipboardFormats = 1
ICF_SketchInk: InkClipboardFormats = 2
ICF_TextInk: InkClipboardFormats = 6
ICF_EnhancedMetafile: InkClipboardFormats = 8
ICF_Metafile: InkClipboardFormats = 32
ICF_Bitmap: InkClipboardFormats = 64
ICF_PasteMask: InkClipboardFormats = 7
ICF_CopyMask: InkClipboardFormats = 127
ICF_Default: InkClipboardFormats = 127
InkClipboardModes = Int32
ICB_Copy: InkClipboardModes = 0
ICB_Cut: InkClipboardModes = 1
ICB_ExtractOnly: InkClipboardModes = 48
ICB_DelayedCopy: InkClipboardModes = 32
ICB_Default: InkClipboardModes = 0
InkCollectionMode = Int32
ICM_InkOnly: InkCollectionMode = 0
ICM_GestureOnly: InkCollectionMode = 1
ICM_InkAndGesture: InkCollectionMode = 2
InkCollector = Guid('{43fb1553-ad74-4ee8-88e4-3e6daac915db}')
InkCollectorEventInterest = Int32
ICEI_DefaultEvents: InkCollectorEventInterest = -1
ICEI_CursorDown: InkCollectorEventInterest = 0
ICEI_Stroke: InkCollectorEventInterest = 1
ICEI_NewPackets: InkCollectorEventInterest = 2
ICEI_NewInAirPackets: InkCollectorEventInterest = 3
ICEI_CursorButtonDown: InkCollectorEventInterest = 4
ICEI_CursorButtonUp: InkCollectorEventInterest = 5
ICEI_CursorInRange: InkCollectorEventInterest = 6
ICEI_CursorOutOfRange: InkCollectorEventInterest = 7
ICEI_SystemGesture: InkCollectorEventInterest = 8
ICEI_TabletAdded: InkCollectorEventInterest = 9
ICEI_TabletRemoved: InkCollectorEventInterest = 10
ICEI_MouseDown: InkCollectorEventInterest = 11
ICEI_MouseMove: InkCollectorEventInterest = 12
ICEI_MouseUp: InkCollectorEventInterest = 13
ICEI_MouseWheel: InkCollectorEventInterest = 14
ICEI_DblClick: InkCollectorEventInterest = 15
ICEI_AllEvents: InkCollectorEventInterest = 16
InkCursorButtonState = Int32
ICBS_Unavailable: InkCursorButtonState = 0
ICBS_Up: InkCursorButtonState = 1
ICBS_Down: InkCursorButtonState = 2
InkDisp = Guid('{937c1a34-151d-4610-9ca6-a8cc9bdb5d83}')
InkDisplayMode = Int32
IDM_Ink: InkDisplayMode = 0
IDM_Text: InkDisplayMode = 1
InkDivider = Guid('{8854f6a0-4683-4ae7-9191-752fe64612c3}')
InkDivisionType = Int32
IDT_Segment: InkDivisionType = 0
IDT_Line: InkDivisionType = 1
IDT_Paragraph: InkDivisionType = 2
IDT_Drawing: InkDivisionType = 3
InkDrawingAttributes = Guid('{d8bf32a2-05a5-44c3-b3aa-5e80ac7d2576}')
InkEdit = Guid('{e5ca59f5-57c4-4dd8-9bd6-1deeedd27af4}')
InkEditStatus = Int32
IES_Idle: InkEditStatus = 0
IES_Collecting: InkEditStatus = 1
IES_Recognizing: InkEditStatus = 2
InkExtractFlags = Int32
IEF_CopyFromOriginal: InkExtractFlags = 0
IEF_RemoveFromOriginal: InkExtractFlags = 1
IEF_Default: InkExtractFlags = 1
InkInsertMode = Int32
IEM_InsertText: InkInsertMode = 0
IEM_InsertInk: InkInsertMode = 1
InkMode = Int32
IEM_Disabled: InkMode = 0
IEM_Ink: InkMode = 1
IEM_InkAndGesture: InkMode = 2
InkMouseButton = Int32
IMF_Left: InkMouseButton = 1
IMF_Right: InkMouseButton = 2
IMF_Middle: InkMouseButton = 4
InkMousePointer = Int32
IMP_Default: InkMousePointer = 0
IMP_Arrow: InkMousePointer = 1
IMP_Crosshair: InkMousePointer = 2
IMP_Ibeam: InkMousePointer = 3
IMP_SizeNESW: InkMousePointer = 4
IMP_SizeNS: InkMousePointer = 5
IMP_SizeNWSE: InkMousePointer = 6
IMP_SizeWE: InkMousePointer = 7
IMP_UpArrow: InkMousePointer = 8
IMP_Hourglass: InkMousePointer = 9
IMP_NoDrop: InkMousePointer = 10
IMP_ArrowHourglass: InkMousePointer = 11
IMP_ArrowQuestion: InkMousePointer = 12
IMP_SizeAll: InkMousePointer = 13
IMP_Hand: InkMousePointer = 14
IMP_Custom: InkMousePointer = 99
InkOverlay = Guid('{65d00646-cde3-4a88-9163-6769f0f1a97d}')
InkOverlayAttachMode = Int32
IOAM_Behind: InkOverlayAttachMode = 0
IOAM_InFront: InkOverlayAttachMode = 1
InkOverlayEditingMode = Int32
IOEM_Ink: InkOverlayEditingMode = 0
IOEM_Delete: InkOverlayEditingMode = 1
IOEM_Select: InkOverlayEditingMode = 2
InkOverlayEraserMode = Int32
IOERM_StrokeErase: InkOverlayEraserMode = 0
IOERM_PointErase: InkOverlayEraserMode = 1
InkPenTip = Int32
IPT_Ball: InkPenTip = 0
IPT_Rectangle: InkPenTip = 1
InkPersistenceCompressionMode = Int32
IPCM_Default: InkPersistenceCompressionMode = 0
IPCM_MaximumCompression: InkPersistenceCompressionMode = 1
IPCM_NoCompression: InkPersistenceCompressionMode = 2
InkPersistenceFormat = Int32
IPF_InkSerializedFormat: InkPersistenceFormat = 0
IPF_Base64InkSerializedFormat: InkPersistenceFormat = 1
IPF_GIF: InkPersistenceFormat = 2
IPF_Base64GIF: InkPersistenceFormat = 3
InkPicture = Guid('{04a1e553-fe36-4fde-865e-344194e69424}')
InkPictureSizeMode = Int32
IPSM_AutoSize: InkPictureSizeMode = 0
IPSM_CenterImage: InkPictureSizeMode = 1
IPSM_Normal: InkPictureSizeMode = 2
IPSM_StretchImage: InkPictureSizeMode = 3
InkRasterOperation = Int32
IRO_Black: InkRasterOperation = 1
IRO_NotMergePen: InkRasterOperation = 2
IRO_MaskNotPen: InkRasterOperation = 3
IRO_NotCopyPen: InkRasterOperation = 4
IRO_MaskPenNot: InkRasterOperation = 5
IRO_Not: InkRasterOperation = 6
IRO_XOrPen: InkRasterOperation = 7
IRO_NotMaskPen: InkRasterOperation = 8
IRO_MaskPen: InkRasterOperation = 9
IRO_NotXOrPen: InkRasterOperation = 10
IRO_NoOperation: InkRasterOperation = 11
IRO_MergeNotPen: InkRasterOperation = 12
IRO_CopyPen: InkRasterOperation = 13
IRO_MergePenNot: InkRasterOperation = 14
IRO_MergePen: InkRasterOperation = 15
IRO_White: InkRasterOperation = 16
class InkRecoGuide(EasyCastStructure):
    rectWritingBox: win32more.Windows.Win32.Foundation.RECT
    rectDrawnBox: win32more.Windows.Win32.Foundation.RECT
    cRows: Int32
    cColumns: Int32
    midline: Int32
InkRecognitionAlternatesSelection = Int32
IRAS_Start: InkRecognitionAlternatesSelection = 0
IRAS_DefaultCount: InkRecognitionAlternatesSelection = 10
IRAS_All: InkRecognitionAlternatesSelection = -1
InkRecognitionConfidence = Int32
IRC_Strong: InkRecognitionConfidence = 0
IRC_Intermediate: InkRecognitionConfidence = 1
IRC_Poor: InkRecognitionConfidence = 2
InkRecognitionModes = Int32
IRM_None: InkRecognitionModes = 0
IRM_WordModeOnly: InkRecognitionModes = 1
IRM_Coerce: InkRecognitionModes = 2
IRM_TopInkBreaksOnly: InkRecognitionModes = 4
IRM_PrefixOk: InkRecognitionModes = 8
IRM_LineMode: InkRecognitionModes = 16
IRM_DisablePersonalization: InkRecognitionModes = 32
IRM_AutoSpace: InkRecognitionModes = 64
IRM_Max: InkRecognitionModes = 128
InkRecognitionStatus = Int32
IRS_NoError: InkRecognitionStatus = 0
IRS_Interrupted: InkRecognitionStatus = 1
IRS_ProcessFailed: InkRecognitionStatus = 2
IRS_InkAddedFailed: InkRecognitionStatus = 4
IRS_SetAutoCompletionModeFailed: InkRecognitionStatus = 8
IRS_SetStrokesFailed: InkRecognitionStatus = 16
IRS_SetGuideFailed: InkRecognitionStatus = 32
IRS_SetFlagsFailed: InkRecognitionStatus = 64
IRS_SetFactoidFailed: InkRecognitionStatus = 128
IRS_SetPrefixSuffixFailed: InkRecognitionStatus = 256
IRS_SetWordListFailed: InkRecognitionStatus = 512
InkRecognizerCapabilities = Int32
IRC_DontCare: InkRecognizerCapabilities = 1
IRC_Object: InkRecognizerCapabilities = 2
IRC_FreeInput: InkRecognizerCapabilities = 4
IRC_LinedInput: InkRecognizerCapabilities = 8
IRC_BoxedInput: InkRecognizerCapabilities = 16
IRC_CharacterAutoCompletionInput: InkRecognizerCapabilities = 32
IRC_RightAndDown: InkRecognizerCapabilities = 64
IRC_LeftAndDown: InkRecognizerCapabilities = 128
IRC_DownAndLeft: InkRecognizerCapabilities = 256
IRC_DownAndRight: InkRecognizerCapabilities = 512
IRC_ArbitraryAngle: InkRecognizerCapabilities = 1024
IRC_Lattice: InkRecognizerCapabilities = 2048
IRC_AdviseInkChange: InkRecognizerCapabilities = 4096
IRC_StrokeReorder: InkRecognizerCapabilities = 8192
IRC_Personalizable: InkRecognizerCapabilities = 16384
IRC_PrefersArbitraryAngle: InkRecognizerCapabilities = 32768
IRC_PrefersParagraphBreaking: InkRecognizerCapabilities = 65536
IRC_PrefersSegmentation: InkRecognizerCapabilities = 131072
IRC_Cursive: InkRecognizerCapabilities = 262144
IRC_TextPrediction: InkRecognizerCapabilities = 524288
IRC_Alpha: InkRecognizerCapabilities = 1048576
IRC_Beta: InkRecognizerCapabilities = 2097152
InkRecognizerCharacterAutoCompletionMode = Int32
IRCACM_Full: InkRecognizerCharacterAutoCompletionMode = 0
IRCACM_Prefix: InkRecognizerCharacterAutoCompletionMode = 1
IRCACM_Random: InkRecognizerCharacterAutoCompletionMode = 2
InkRecognizerContext = Guid('{aac46a37-9229-4fc0-8cce-4497569bf4d1}')
InkRecognizerGuide = Guid('{8770d941-a63a-4671-a375-2855a18eba73}')
InkRecognizers = Guid('{9fd4e808-f6e6-4e65-98d3-aa39054c1255}')
InkRectangle = Guid('{43b07326-aae0-4b62-a83d-5fd768b7353c}')
InkRenderer = Guid('{9c1cc6e4-d7eb-4eeb-9091-15a7c8791ed9}')
InkSelectionConstants = Int32
ISC_FirstElement: InkSelectionConstants = 0
ISC_AllElements: InkSelectionConstants = -1
InkShiftKeyModifierFlags = Int32
IKM_Shift: InkShiftKeyModifierFlags = 1
IKM_Control: InkShiftKeyModifierFlags = 2
IKM_Alt: InkShiftKeyModifierFlags = 4
InkStrokes = Guid('{48f491bc-240e-4860-b079-a1e94d3d2c86}')
InkSystemGesture = Int32
ISG_Tap: InkSystemGesture = 16
ISG_DoubleTap: InkSystemGesture = 17
ISG_RightTap: InkSystemGesture = 18
ISG_Drag: InkSystemGesture = 19
ISG_RightDrag: InkSystemGesture = 20
ISG_HoldEnter: InkSystemGesture = 21
ISG_HoldLeave: InkSystemGesture = 22
ISG_HoverEnter: InkSystemGesture = 23
ISG_HoverLeave: InkSystemGesture = 24
ISG_Flick: InkSystemGesture = 31
InkTablets = Guid('{6e4fcb12-510a-4d40-9304-1da10ae9147c}')
InkTransform = Guid('{e3d5d93c-1663-4a78-a1a7-22375dfebaee}')
InkWordList = Guid('{9de85094-f71f-44f1-8471-15a2fa76fcf3}')
InteractionMode = Int32
InteractionMode_InPlace: InteractionMode = 0
InteractionMode_Floating: InteractionMode = 1
InteractionMode_DockedTop: InteractionMode = 2
InteractionMode_DockedBottom: InteractionMode = 3
KEYMODIFIER = Int32
KEYMODIFIER_CONTROL: KEYMODIFIER = 1
KEYMODIFIER_MENU: KEYMODIFIER = 2
KEYMODIFIER_SHIFT: KEYMODIFIER = 4
KEYMODIFIER_WIN: KEYMODIFIER = 8
KEYMODIFIER_ALTGR: KEYMODIFIER = 16
KEYMODIFIER_EXT: KEYMODIFIER = 32
class LATTICE_METRICS(EasyCastStructure):
    lsBaseline: win32more.Windows.Win32.UI.TabletPC.LINE_SEGMENT
    iMidlineOffset: Int16
LINE_METRICS = Int32
LM_BASELINE: LINE_METRICS = 0
LM_MIDLINE: LINE_METRICS = 1
LM_ASCENDER: LINE_METRICS = 2
LM_DESCENDER: LINE_METRICS = 3
class LINE_SEGMENT(EasyCastStructure):
    PtA: win32more.Windows.Win32.Foundation.POINT
    PtB: win32more.Windows.Win32.Foundation.POINT
MICUIELEMENT = Int32
MICUIELEMENT_BUTTON_WRITE: MICUIELEMENT = 1
MICUIELEMENT_BUTTON_ERASE: MICUIELEMENT = 2
MICUIELEMENT_BUTTON_CORRECT: MICUIELEMENT = 4
MICUIELEMENT_BUTTON_CLEAR: MICUIELEMENT = 8
MICUIELEMENT_BUTTON_UNDO: MICUIELEMENT = 16
MICUIELEMENT_BUTTON_REDO: MICUIELEMENT = 32
MICUIELEMENT_BUTTON_INSERT: MICUIELEMENT = 64
MICUIELEMENT_BUTTON_CANCEL: MICUIELEMENT = 128
MICUIELEMENT_INKPANEL_BACKGROUND: MICUIELEMENT = 256
MICUIELEMENT_RESULTPANEL_BACKGROUND: MICUIELEMENT = 512
MICUIELEMENTSTATE = Int32
MICUIELEMENTSTATE_NORMAL: MICUIELEMENTSTATE = 1
MICUIELEMENTSTATE_HOT: MICUIELEMENTSTATE = 2
MICUIELEMENTSTATE_PRESSED: MICUIELEMENTSTATE = 3
MICUIELEMENTSTATE_DISABLED: MICUIELEMENTSTATE = 4
MathInputControl = Guid('{c561816c-14d8-4090-830c-98d994b21c7b}')
MouseButton = Int32
NO_BUTTON: MouseButton = 0
LEFT_BUTTON: MouseButton = 1
RIGHT_BUTTON: MouseButton = 2
MIDDLE_BUTTON: MouseButton = 4
class PACKET_DESCRIPTION(EasyCastStructure):
    cbPacketSize: UInt32
    cPacketProperties: UInt32
    pPacketProperties: POINTER(win32more.Windows.Win32.UI.TabletPC.PACKET_PROPERTY)
    cButtons: UInt32
    pguidButtons: POINTER(Guid)
class PACKET_PROPERTY(EasyCastStructure):
    guid: Guid
    PropertyMetrics: win32more.Windows.Win32.UI.TabletPC.PROPERTY_METRICS
class PROPERTY_METRICS(EasyCastStructure):
    nLogicalMin: Int32
    nLogicalMax: Int32
    Units: win32more.Windows.Win32.UI.TabletPC.PROPERTY_UNITS
    fResolution: Single
PROPERTY_UNITS = Int32
PROPERTY_UNITS_DEFAULT: PROPERTY_UNITS = 0
PROPERTY_UNITS_INCHES: PROPERTY_UNITS = 1
PROPERTY_UNITS_CENTIMETERS: PROPERTY_UNITS = 2
PROPERTY_UNITS_DEGREES: PROPERTY_UNITS = 3
PROPERTY_UNITS_RADIANS: PROPERTY_UNITS = 4
PROPERTY_UNITS_SECONDS: PROPERTY_UNITS = 5
PROPERTY_UNITS_POUNDS: PROPERTY_UNITS = 6
PROPERTY_UNITS_GRAMS: PROPERTY_UNITS = 7
PROPERTY_UNITS_SILINEAR: PROPERTY_UNITS = 8
PROPERTY_UNITS_SIROTATION: PROPERTY_UNITS = 9
PROPERTY_UNITS_ENGLINEAR: PROPERTY_UNITS = 10
PROPERTY_UNITS_ENGROTATION: PROPERTY_UNITS = 11
PROPERTY_UNITS_SLUGS: PROPERTY_UNITS = 12
PROPERTY_UNITS_KELVIN: PROPERTY_UNITS = 13
PROPERTY_UNITS_FAHRENHEIT: PROPERTY_UNITS = 14
PROPERTY_UNITS_AMPERE: PROPERTY_UNITS = 15
PROPERTY_UNITS_CANDELA: PROPERTY_UNITS = 16
PanelInputArea = Int32
PanelInputArea_Auto: PanelInputArea = 0
PanelInputArea_Keyboard: PanelInputArea = 1
PanelInputArea_WritingPad: PanelInputArea = 2
PanelInputArea_CharacterPad: PanelInputArea = 3
PanelType = Int32
PT_Default: PanelType = 0
PT_Inactive: PanelType = 1
PT_Handwriting: PanelType = 2
PT_Keyboard: PanelType = 3
PenInputPanel = Guid('{f744e496-1b5a-489e-81dc-fbd7ac6298a8}')
PenInputPanel_Internal = Guid('{802b1fb9-056b-4720-b0cc-80d23b71171e}')
@winfunctype_pointer
def PfnRecoCallback(param0: UInt32, param1: POINTER(Byte), param2: win32more.Windows.Win32.UI.TabletPC.HRECOCONTEXT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class RECO_ATTRS(EasyCastStructure):
    dwRecoCapabilityFlags: UInt32
    awcVendorName: Char * 32
    awcFriendlyName: Char * 64
    awLanguageId: UInt16 * 64
class RECO_GUIDE(EasyCastStructure):
    xOrigin: Int32
    yOrigin: Int32
    cxBox: Int32
    cyBox: Int32
    cxBase: Int32
    cyBase: Int32
    cHorzBox: Int32
    cVertBox: Int32
    cyMid: Int32
class RECO_LATTICE(EasyCastStructure):
    ulColumnCount: UInt32
    pLatticeColumns: POINTER(win32more.Windows.Win32.UI.TabletPC.RECO_LATTICE_COLUMN)
    ulPropertyCount: UInt32
    pGuidProperties: POINTER(Guid)
    ulBestResultColumnCount: UInt32
    pulBestResultColumns: POINTER(UInt32)
    pulBestResultIndexes: POINTER(UInt32)
class RECO_LATTICE_COLUMN(EasyCastStructure):
    key: UInt32
    cpProp: win32more.Windows.Win32.UI.TabletPC.RECO_LATTICE_PROPERTIES
    cStrokes: UInt32
    pStrokes: POINTER(UInt32)
    cLatticeElements: UInt32
    pLatticeElements: POINTER(win32more.Windows.Win32.UI.TabletPC.RECO_LATTICE_ELEMENT)
class RECO_LATTICE_ELEMENT(EasyCastStructure):
    score: Int32
    type: UInt16
    pData: POINTER(Byte)
    ulNextColumn: UInt32
    ulStrokeNumber: UInt32
    epProp: win32more.Windows.Win32.UI.TabletPC.RECO_LATTICE_PROPERTIES
class RECO_LATTICE_PROPERTIES(EasyCastStructure):
    cProperties: UInt32
    apProps: POINTER(POINTER(win32more.Windows.Win32.UI.TabletPC.RECO_LATTICE_PROPERTY))
class RECO_LATTICE_PROPERTY(EasyCastStructure):
    guidProperty: Guid
    cbPropertyValue: UInt16
    pPropertyValue: POINTER(Byte)
class RECO_RANGE(EasyCastStructure):
    iwcBegin: UInt32
    cCount: UInt32
RECO_TYPE = Int32
RECO_TYPE_WSTRING: RECO_TYPE = 0
RECO_TYPE_WCHAR: RECO_TYPE = 1
RealTimeStylus = Guid('{e26b366d-f998-43ce-836f-cb6d904432b0}')
RealTimeStylusDataInterest = Int32
RTSDI_AllData: RealTimeStylusDataInterest = -1
RTSDI_None: RealTimeStylusDataInterest = 0
RTSDI_Error: RealTimeStylusDataInterest = 1
RTSDI_RealTimeStylusEnabled: RealTimeStylusDataInterest = 2
RTSDI_RealTimeStylusDisabled: RealTimeStylusDataInterest = 4
RTSDI_StylusNew: RealTimeStylusDataInterest = 8
RTSDI_StylusInRange: RealTimeStylusDataInterest = 16
RTSDI_InAirPackets: RealTimeStylusDataInterest = 32
RTSDI_StylusOutOfRange: RealTimeStylusDataInterest = 64
RTSDI_StylusDown: RealTimeStylusDataInterest = 128
RTSDI_Packets: RealTimeStylusDataInterest = 256
RTSDI_StylusUp: RealTimeStylusDataInterest = 512
RTSDI_StylusButtonUp: RealTimeStylusDataInterest = 1024
RTSDI_StylusButtonDown: RealTimeStylusDataInterest = 2048
RTSDI_SystemEvents: RealTimeStylusDataInterest = 4096
RTSDI_TabletAdded: RealTimeStylusDataInterest = 8192
RTSDI_TabletRemoved: RealTimeStylusDataInterest = 16384
RTSDI_CustomStylusDataAdded: RealTimeStylusDataInterest = 32768
RTSDI_UpdateMapping: RealTimeStylusDataInterest = 65536
RTSDI_DefaultEvents: RealTimeStylusDataInterest = 37766
RealTimeStylusLockType = Int32
RTSLT_ObjLock: RealTimeStylusLockType = 1
RTSLT_SyncEventLock: RealTimeStylusLockType = 2
RTSLT_AsyncEventLock: RealTimeStylusLockType = 4
RTSLT_ExcludeCallback: RealTimeStylusLockType = 8
RTSLT_SyncObjLock: RealTimeStylusLockType = 11
RTSLT_AsyncObjLock: RealTimeStylusLockType = 13
SCROLLDIRECTION = Int32
SCROLLDIRECTION_UP: SCROLLDIRECTION = 0
SCROLLDIRECTION_DOWN: SCROLLDIRECTION = 1
class STROKE_RANGE(EasyCastStructure):
    iStrokeBegin: UInt32
    iStrokeEnd: UInt32
class SYSTEM_EVENT_DATA(EasyCastStructure):
    bModifier: Byte
    wKey: Char
    xPos: Int32
    yPos: Int32
    bCursorMode: Byte
    dwButtonState: UInt32
ScrollBarsConstants = Int32
ScrollBarsConstants_rtfNone: ScrollBarsConstants = 0
ScrollBarsConstants_rtfHorizontal: ScrollBarsConstants = 1
ScrollBarsConstants_rtfVertical: ScrollBarsConstants = 2
ScrollBarsConstants_rtfBoth: ScrollBarsConstants = 3
SelAlignmentConstants = Int32
SelAlignmentConstants_rtfLeft: SelAlignmentConstants = 0
SelAlignmentConstants_rtfRight: SelAlignmentConstants = 1
SelAlignmentConstants_rtfCenter: SelAlignmentConstants = 2
SelectionHitResult = Int32
SHR_None: SelectionHitResult = 0
SHR_NW: SelectionHitResult = 1
SHR_SE: SelectionHitResult = 2
SHR_NE: SelectionHitResult = 3
SHR_SW: SelectionHitResult = 4
SHR_E: SelectionHitResult = 5
SHR_W: SelectionHitResult = 6
SHR_N: SelectionHitResult = 7
SHR_S: SelectionHitResult = 8
SHR_Selection: SelectionHitResult = 9
SketchInk = Guid('{f0291081-e87c-4e07-97da-a0a03761e586}')
StrokeBuilder = Guid('{e810cee7-6e51-4cb0-aa3a-0b985b70daf7}')
class StylusInfo(EasyCastStructure):
    tcid: UInt32
    cid: UInt32
    bIsInvertedCursor: win32more.Windows.Win32.Foundation.BOOL
StylusQueue = Int32
StylusQueue_SyncStylusQueue: StylusQueue = 1
StylusQueue_AsyncStylusQueueImmediate: StylusQueue = 2
StylusQueue_AsyncStylusQueue: StylusQueue = 3
TabletDeviceKind = Int32
TDK_Mouse: TabletDeviceKind = 0
TDK_Pen: TabletDeviceKind = 1
TDK_Touch: TabletDeviceKind = 2
TabletHardwareCapabilities = Int32
THWC_Integrated: TabletHardwareCapabilities = 1
THWC_CursorMustTouch: TabletHardwareCapabilities = 2
THWC_HardProximity: TabletHardwareCapabilities = 4
THWC_CursorsHavePhysicalIds: TabletHardwareCapabilities = 8
TabletPropertyMetricUnit = Int32
TPMU_Default: TabletPropertyMetricUnit = 0
TPMU_Inches: TabletPropertyMetricUnit = 1
TPMU_Centimeters: TabletPropertyMetricUnit = 2
TPMU_Degrees: TabletPropertyMetricUnit = 3
TPMU_Radians: TabletPropertyMetricUnit = 4
TPMU_Seconds: TabletPropertyMetricUnit = 5
TPMU_Pounds: TabletPropertyMetricUnit = 6
TPMU_Grams: TabletPropertyMetricUnit = 7
TextInputPanel = Guid('{f9b189d7-228b-4f2b-8650-b97f59e02c8c}')
TipAutoCompleteClient = Guid('{807c1e6c-1d00-453f-b920-b61bb7cdd997}')
VisualState = Int32
VisualState_InPlace: VisualState = 0
VisualState_Floating: VisualState = 1
VisualState_DockedTop: VisualState = 2
VisualState_DockedBottom: VisualState = 3
VisualState_Closed: VisualState = 4
class _IInkCollectorEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{11a583f2-712d-4fea-abcf-ab4af38ea06b}')
class _IInkEditEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e3b0b797-a72e-46db-a0d7-6c9eba8e9bbc}')
class _IInkEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{427b1865-ca3f-479a-83a9-0f420f2a0073}')
class _IInkOverlayEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{31179b69-e563-489e-b16f-712f1e8a0651}')
class _IInkPictureEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{60ff4fee-22ff-4484-acc1-d308d9cd7ea3}')
class _IInkRecognitionEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{17bce92f-2e21-47fd-9d33-3c6afbfd8c59}')
class _IInkStrokesEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f33053ec-5d25-430a-928f-76a6491dde15}')
class _IMathInputControlEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{683336b5-a47d-4358-96f9-875a472ae70a}')
class _IPenInputPanelEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b7e489da-3719-439f-848f-e7acbd820f17}')
make_ready(__name__)
