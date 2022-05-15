from win32more import *
import win32more.UI.Input.KeyboardAndMouse
import win32more.Foundation
import win32more.UI.TextServices

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.UI.Input.KeyboardAndMouse, name, globals()[f"_define_{name}"]())
    return getattr(win32more.UI.Input.KeyboardAndMouse, name)
def __dir__():
    return __all__
EXTENDED_BIT = 16777216
DONTCARE_BIT = 33554432
FAKE_KEYSTROKE = 33554432
KBDBASE = 0
KBDSHIFT = 1
KBDCTRL = 2
KBDALT = 4
KBDKANA = 8
KBDROYA = 16
KBDLOYA = 32
KBDGRPSELTAP = 128
GRAVE = 768
ACUTE = 769
CIRCUMFLEX = 770
TILDE = 771
MACRON = 772
OVERSCORE = 773
BREVE = 774
DOT_ABOVE = 775
UMLAUT = 776
DIARESIS = 776
HOOK_ABOVE = 777
RING = 778
DOUBLE_ACUTE = 779
HACEK = 780
CEDILLA = 807
OGONEK = 808
TONOS = 900
DIARESIS_TONOS = 901
SHFT_INVALID = 15
WCH_NONE = 61440
WCH_DEAD = 61441
WCH_LGTR = 61442
CAPLOK = 1
SGCAPS = 2
CAPLOKALTGR = 4
KANALOK = 8
GRPSELTAP = 128
DKF_DEAD = 1
KBD_VERSION = 1
KLLF_ALTGR = 1
KLLF_SHIFTLOCK = 2
KLLF_LRM_RLM = 4
KLLF_GLOBAL_ATTRS = 2
KBDTABLE_MULTI_MAX = 8
KEYBOARD_TYPE_GENERIC_101 = 4
KEYBOARD_TYPE_JAPAN = 7
KEYBOARD_TYPE_KOREA = 8
KEYBOARD_TYPE_UNKNOWN = 81
NLSKBD_OEM_MICROSOFT = 0
NLSKBD_OEM_AX = 1
NLSKBD_OEM_EPSON = 4
NLSKBD_OEM_FUJITSU = 5
NLSKBD_OEM_IBM = 7
NLSKBD_OEM_MATSUSHITA = 10
NLSKBD_OEM_NEC = 13
NLSKBD_OEM_TOSHIBA = 18
NLSKBD_OEM_DEC = 24
MICROSOFT_KBD_101_TYPE = 0
MICROSOFT_KBD_AX_TYPE = 1
MICROSOFT_KBD_106_TYPE = 2
MICROSOFT_KBD_002_TYPE = 3
MICROSOFT_KBD_001_TYPE = 4
MICROSOFT_KBD_FUNC = 12
AX_KBD_DESKTOP_TYPE = 1
FMR_KBD_JIS_TYPE = 0
FMR_KBD_OASYS_TYPE = 1
FMV_KBD_OASYS_TYPE = 2
NEC_KBD_NORMAL_TYPE = 1
NEC_KBD_N_MODE_TYPE = 2
NEC_KBD_H_MODE_TYPE = 3
NEC_KBD_LAPTOP_TYPE = 4
NEC_KBD_106_TYPE = 5
TOSHIBA_KBD_DESKTOP_TYPE = 13
TOSHIBA_KBD_LAPTOP_TYPE = 15
DEC_KBD_ANSI_LAYOUT_TYPE = 1
DEC_KBD_JIS_LAYOUT_TYPE = 2
MICROSOFT_KBD_101A_TYPE = 0
MICROSOFT_KBD_101B_TYPE = 4
MICROSOFT_KBD_101C_TYPE = 5
MICROSOFT_KBD_103_TYPE = 6
NLSKBD_INFO_SEND_IME_NOTIFICATION = 1
NLSKBD_INFO_ACCESSIBILITY_KEYMAP = 2
NLSKBD_INFO_EMURATE_101_KEYBOARD = 16
NLSKBD_INFO_EMURATE_106_KEYBOARD = 32
KBDNLS_TYPE_NULL = 0
KBDNLS_TYPE_NORMAL = 1
KBDNLS_TYPE_TOGGLE = 2
KBDNLS_INDEX_NORMAL = 1
KBDNLS_INDEX_ALT = 2
KBDNLS_NULL = 0
KBDNLS_NOEVENT = 1
KBDNLS_SEND_BASE_VK = 2
KBDNLS_SEND_PARAM_VK = 3
KBDNLS_KANALOCK = 4
KBDNLS_ALPHANUM = 5
KBDNLS_HIRAGANA = 6
KBDNLS_KATAKANA = 7
KBDNLS_SBCSDBCS = 8
KBDNLS_ROMAN = 9
KBDNLS_CODEINPUT = 10
KBDNLS_HELP_OR_END = 11
KBDNLS_HOME_OR_CLEAR = 12
KBDNLS_NUMPAD = 13
KBDNLS_KANAEVENT = 14
KBDNLS_CONV_OR_NONCONV = 15
KBD_TYPE = 4
VK__none_ = 255
VK_ABNT_C1 = 193
VK_ABNT_C2 = 194
SCANCODE_LSHIFT = 42
SCANCODE_RSHIFT = 54
SCANCODE_CTRL = 29
SCANCODE_ALT = 56
SCANCODE_NUMPAD_FIRST = 71
SCANCODE_NUMPAD_LAST = 82
SCANCODE_LWIN = 91
SCANCODE_RWIN = 92
SCANCODE_THAI_LAYOUT_TOGGLE = 41
VK_DBE_ALPHANUMERIC = 240
VK_DBE_KATAKANA = 241
VK_DBE_HIRAGANA = 242
VK_DBE_SBCSCHAR = 243
VK_DBE_DBCSCHAR = 244
VK_DBE_ROMAN = 245
VK_DBE_NOROMAN = 246
VK_DBE_ENTERWORDREGISTERMODE = 247
VK_DBE_ENTERIMECONFIGMODE = 248
VK_DBE_FLUSHSTRING = 249
VK_DBE_CODEINPUT = 250
VK_DBE_NOCODEINPUT = 251
VK_DBE_DETERMINESTRING = 252
VK_DBE_ENTERDLGCONVERSIONMODE = 253
HOT_KEY_MODIFIERS = UInt32
MOD_ALT = 1
MOD_CONTROL = 2
MOD_NOREPEAT = 16384
MOD_SHIFT = 4
MOD_WIN = 8
ACTIVATE_KEYBOARD_LAYOUT_FLAGS = UInt32
KLF_REORDER = 8
KLF_RESET = 1073741824
KLF_SETFORPROCESS = 256
KLF_SHIFTLOCK = 65536
KLF_ACTIVATE = 1
KLF_NOTELLSHELL = 128
KLF_REPLACELANG = 16
KLF_SUBSTITUTE_OK = 2
GET_MOUSE_MOVE_POINTS_EX_RESOLUTION = UInt32
GMMP_USE_DISPLAY_POINTS = 1
GMMP_USE_HIGH_RESOLUTION_POINTS = 2
KEYBD_EVENT_FLAGS = UInt32
KEYEVENTF_EXTENDEDKEY = 1
KEYEVENTF_KEYUP = 2
KEYEVENTF_SCANCODE = 8
KEYEVENTF_UNICODE = 4
MOUSE_EVENT_FLAGS = UInt32
MOUSEEVENTF_ABSOLUTE = 32768
MOUSEEVENTF_LEFTDOWN = 2
MOUSEEVENTF_LEFTUP = 4
MOUSEEVENTF_MIDDLEDOWN = 32
MOUSEEVENTF_MIDDLEUP = 64
MOUSEEVENTF_MOVE = 1
MOUSEEVENTF_RIGHTDOWN = 8
MOUSEEVENTF_RIGHTUP = 16
MOUSEEVENTF_WHEEL = 2048
MOUSEEVENTF_XDOWN = 128
MOUSEEVENTF_XUP = 256
MOUSEEVENTF_HWHEEL = 4096
MOUSEEVENTF_MOVE_NOCOALESCE = 8192
MOUSEEVENTF_VIRTUALDESK = 16384
INPUT_TYPE = UInt32
INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2
TRACKMOUSEEVENT_FLAGS = UInt32
TME_CANCEL = 2147483648
TME_HOVER = 1
TME_LEAVE = 2
TME_NONCLIENT = 16
TME_QUERY = 1073741824
VIRTUAL_KEY = UInt16
VK_0 = 48
VK_1 = 49
VK_2 = 50
VK_3 = 51
VK_4 = 52
VK_5 = 53
VK_6 = 54
VK_7 = 55
VK_8 = 56
VK_9 = 57
VK_A = 65
VK_B = 66
VK_C = 67
VK_D = 68
VK_E = 69
VK_F = 70
VK_G = 71
VK_H = 72
VK_I = 73
VK_J = 74
VK_K = 75
VK_L = 76
VK_M = 77
VK_N = 78
VK_O = 79
VK_P = 80
VK_Q = 81
VK_R = 82
VK_S = 83
VK_T = 84
VK_U = 85
VK_V = 86
VK_W = 87
VK_X = 88
VK_Y = 89
VK_Z = 90
VK_LBUTTON = 1
VK_RBUTTON = 2
VK_CANCEL = 3
VK_MBUTTON = 4
VK_XBUTTON1 = 5
VK_XBUTTON2 = 6
VK_BACK = 8
VK_TAB = 9
VK_CLEAR = 12
VK_RETURN = 13
VK_SHIFT = 16
VK_CONTROL = 17
VK_MENU = 18
VK_PAUSE = 19
VK_CAPITAL = 20
VK_KANA = 21
VK_HANGEUL = 21
VK_HANGUL = 21
VK_IME_ON = 22
VK_JUNJA = 23
VK_FINAL = 24
VK_HANJA = 25
VK_KANJI = 25
VK_IME_OFF = 26
VK_ESCAPE = 27
VK_CONVERT = 28
VK_NONCONVERT = 29
VK_ACCEPT = 30
VK_MODECHANGE = 31
VK_SPACE = 32
VK_PRIOR = 33
VK_NEXT = 34
VK_END = 35
VK_HOME = 36
VK_LEFT = 37
VK_UP = 38
VK_RIGHT = 39
VK_DOWN = 40
VK_SELECT = 41
VK_PRINT = 42
VK_EXECUTE = 43
VK_SNAPSHOT = 44
VK_INSERT = 45
VK_DELETE = 46
VK_HELP = 47
VK_LWIN = 91
VK_RWIN = 92
VK_APPS = 93
VK_SLEEP = 95
VK_NUMPAD0 = 96
VK_NUMPAD1 = 97
VK_NUMPAD2 = 98
VK_NUMPAD3 = 99
VK_NUMPAD4 = 100
VK_NUMPAD5 = 101
VK_NUMPAD6 = 102
VK_NUMPAD7 = 103
VK_NUMPAD8 = 104
VK_NUMPAD9 = 105
VK_MULTIPLY = 106
VK_ADD = 107
VK_SEPARATOR = 108
VK_SUBTRACT = 109
VK_DECIMAL = 110
VK_DIVIDE = 111
VK_F1 = 112
VK_F2 = 113
VK_F3 = 114
VK_F4 = 115
VK_F5 = 116
VK_F6 = 117
VK_F7 = 118
VK_F8 = 119
VK_F9 = 120
VK_F10 = 121
VK_F11 = 122
VK_F12 = 123
VK_F13 = 124
VK_F14 = 125
VK_F15 = 126
VK_F16 = 127
VK_F17 = 128
VK_F18 = 129
VK_F19 = 130
VK_F20 = 131
VK_F21 = 132
VK_F22 = 133
VK_F23 = 134
VK_F24 = 135
VK_NAVIGATION_VIEW = 136
VK_NAVIGATION_MENU = 137
VK_NAVIGATION_UP = 138
VK_NAVIGATION_DOWN = 139
VK_NAVIGATION_LEFT = 140
VK_NAVIGATION_RIGHT = 141
VK_NAVIGATION_ACCEPT = 142
VK_NAVIGATION_CANCEL = 143
VK_NUMLOCK = 144
VK_SCROLL = 145
VK_OEM_NEC_EQUAL = 146
VK_OEM_FJ_JISHO = 146
VK_OEM_FJ_MASSHOU = 147
VK_OEM_FJ_TOUROKU = 148
VK_OEM_FJ_LOYA = 149
VK_OEM_FJ_ROYA = 150
VK_LSHIFT = 160
VK_RSHIFT = 161
VK_LCONTROL = 162
VK_RCONTROL = 163
VK_LMENU = 164
VK_RMENU = 165
VK_BROWSER_BACK = 166
VK_BROWSER_FORWARD = 167
VK_BROWSER_REFRESH = 168
VK_BROWSER_STOP = 169
VK_BROWSER_SEARCH = 170
VK_BROWSER_FAVORITES = 171
VK_BROWSER_HOME = 172
VK_VOLUME_MUTE = 173
VK_VOLUME_DOWN = 174
VK_VOLUME_UP = 175
VK_MEDIA_NEXT_TRACK = 176
VK_MEDIA_PREV_TRACK = 177
VK_MEDIA_STOP = 178
VK_MEDIA_PLAY_PAUSE = 179
VK_LAUNCH_MAIL = 180
VK_LAUNCH_MEDIA_SELECT = 181
VK_LAUNCH_APP1 = 182
VK_LAUNCH_APP2 = 183
VK_OEM_1 = 186
VK_OEM_PLUS = 187
VK_OEM_COMMA = 188
VK_OEM_MINUS = 189
VK_OEM_PERIOD = 190
VK_OEM_2 = 191
VK_OEM_3 = 192
VK_GAMEPAD_A = 195
VK_GAMEPAD_B = 196
VK_GAMEPAD_X = 197
VK_GAMEPAD_Y = 198
VK_GAMEPAD_RIGHT_SHOULDER = 199
VK_GAMEPAD_LEFT_SHOULDER = 200
VK_GAMEPAD_LEFT_TRIGGER = 201
VK_GAMEPAD_RIGHT_TRIGGER = 202
VK_GAMEPAD_DPAD_UP = 203
VK_GAMEPAD_DPAD_DOWN = 204
VK_GAMEPAD_DPAD_LEFT = 205
VK_GAMEPAD_DPAD_RIGHT = 206
VK_GAMEPAD_MENU = 207
VK_GAMEPAD_VIEW = 208
VK_GAMEPAD_LEFT_THUMBSTICK_BUTTON = 209
VK_GAMEPAD_RIGHT_THUMBSTICK_BUTTON = 210
VK_GAMEPAD_LEFT_THUMBSTICK_UP = 211
VK_GAMEPAD_LEFT_THUMBSTICK_DOWN = 212
VK_GAMEPAD_LEFT_THUMBSTICK_RIGHT = 213
VK_GAMEPAD_LEFT_THUMBSTICK_LEFT = 214
VK_GAMEPAD_RIGHT_THUMBSTICK_UP = 215
VK_GAMEPAD_RIGHT_THUMBSTICK_DOWN = 216
VK_GAMEPAD_RIGHT_THUMBSTICK_RIGHT = 217
VK_GAMEPAD_RIGHT_THUMBSTICK_LEFT = 218
VK_OEM_4 = 219
VK_OEM_5 = 220
VK_OEM_6 = 221
VK_OEM_7 = 222
VK_OEM_8 = 223
VK_OEM_AX = 225
VK_OEM_102 = 226
VK_ICO_HELP = 227
VK_ICO_00 = 228
VK_PROCESSKEY = 229
VK_ICO_CLEAR = 230
VK_PACKET = 231
VK_OEM_RESET = 233
VK_OEM_JUMP = 234
VK_OEM_PA1 = 235
VK_OEM_PA2 = 236
VK_OEM_PA3 = 237
VK_OEM_WSCTRL = 238
VK_OEM_CUSEL = 239
VK_OEM_ATTN = 240
VK_OEM_FINISH = 241
VK_OEM_COPY = 242
VK_OEM_AUTO = 243
VK_OEM_ENLW = 244
VK_OEM_BACKTAB = 245
VK_ATTN = 246
VK_CRSEL = 247
VK_EXSEL = 248
VK_EREOF = 249
VK_PLAY = 250
VK_ZOOM = 251
VK_NONAME = 252
VK_PA1 = 253
VK_OEM_CLEAR = 254
def _define_VK_TO_BIT_head():
    class VK_TO_BIT(Structure):
        pass
    return VK_TO_BIT
def _define_VK_TO_BIT():
    VK_TO_BIT = win32more.UI.Input.KeyboardAndMouse.VK_TO_BIT_head
    VK_TO_BIT._fields_ = [
        ("Vk", Byte),
        ("ModBits", Byte),
    ]
    return VK_TO_BIT
def _define_MODIFIERS_head():
    class MODIFIERS(Structure):
        pass
    return MODIFIERS
def _define_MODIFIERS():
    MODIFIERS = win32more.UI.Input.KeyboardAndMouse.MODIFIERS_head
    MODIFIERS._fields_ = [
        ("pVkToBit", POINTER(win32more.UI.Input.KeyboardAndMouse.VK_TO_BIT_head)),
        ("wMaxModBits", UInt16),
        ("ModNumber", Byte * 0),
    ]
    return MODIFIERS
def _define_VSC_VK_head():
    class VSC_VK(Structure):
        pass
    return VSC_VK
def _define_VSC_VK():
    VSC_VK = win32more.UI.Input.KeyboardAndMouse.VSC_VK_head
    VSC_VK._fields_ = [
        ("Vsc", Byte),
        ("Vk", UInt16),
    ]
    return VSC_VK
def _define_VK_VSC_head():
    class VK_VSC(Structure):
        pass
    return VK_VSC
def _define_VK_VSC():
    VK_VSC = win32more.UI.Input.KeyboardAndMouse.VK_VSC_head
    VK_VSC._fields_ = [
        ("Vk", Byte),
        ("Vsc", Byte),
    ]
    return VK_VSC
def _define_VK_TO_WCHARS1_head():
    class VK_TO_WCHARS1(Structure):
        pass
    return VK_TO_WCHARS1
def _define_VK_TO_WCHARS1():
    VK_TO_WCHARS1 = win32more.UI.Input.KeyboardAndMouse.VK_TO_WCHARS1_head
    VK_TO_WCHARS1._fields_ = [
        ("VirtualKey", Byte),
        ("Attributes", Byte),
        ("wch", Char * 0),
    ]
    return VK_TO_WCHARS1
def _define_VK_TO_WCHARS2_head():
    class VK_TO_WCHARS2(Structure):
        pass
    return VK_TO_WCHARS2
def _define_VK_TO_WCHARS2():
    VK_TO_WCHARS2 = win32more.UI.Input.KeyboardAndMouse.VK_TO_WCHARS2_head
    VK_TO_WCHARS2._fields_ = [
        ("VirtualKey", Byte),
        ("Attributes", Byte),
        ("wch", Char * 2),
    ]
    return VK_TO_WCHARS2
def _define_VK_TO_WCHARS3_head():
    class VK_TO_WCHARS3(Structure):
        pass
    return VK_TO_WCHARS3
def _define_VK_TO_WCHARS3():
    VK_TO_WCHARS3 = win32more.UI.Input.KeyboardAndMouse.VK_TO_WCHARS3_head
    VK_TO_WCHARS3._fields_ = [
        ("VirtualKey", Byte),
        ("Attributes", Byte),
        ("wch", Char * 3),
    ]
    return VK_TO_WCHARS3
def _define_VK_TO_WCHARS4_head():
    class VK_TO_WCHARS4(Structure):
        pass
    return VK_TO_WCHARS4
def _define_VK_TO_WCHARS4():
    VK_TO_WCHARS4 = win32more.UI.Input.KeyboardAndMouse.VK_TO_WCHARS4_head
    VK_TO_WCHARS4._fields_ = [
        ("VirtualKey", Byte),
        ("Attributes", Byte),
        ("wch", Char * 4),
    ]
    return VK_TO_WCHARS4
def _define_VK_TO_WCHARS5_head():
    class VK_TO_WCHARS5(Structure):
        pass
    return VK_TO_WCHARS5
def _define_VK_TO_WCHARS5():
    VK_TO_WCHARS5 = win32more.UI.Input.KeyboardAndMouse.VK_TO_WCHARS5_head
    VK_TO_WCHARS5._fields_ = [
        ("VirtualKey", Byte),
        ("Attributes", Byte),
        ("wch", Char * 5),
    ]
    return VK_TO_WCHARS5
def _define_VK_TO_WCHARS6_head():
    class VK_TO_WCHARS6(Structure):
        pass
    return VK_TO_WCHARS6
def _define_VK_TO_WCHARS6():
    VK_TO_WCHARS6 = win32more.UI.Input.KeyboardAndMouse.VK_TO_WCHARS6_head
    VK_TO_WCHARS6._fields_ = [
        ("VirtualKey", Byte),
        ("Attributes", Byte),
        ("wch", Char * 6),
    ]
    return VK_TO_WCHARS6
def _define_VK_TO_WCHARS7_head():
    class VK_TO_WCHARS7(Structure):
        pass
    return VK_TO_WCHARS7
def _define_VK_TO_WCHARS7():
    VK_TO_WCHARS7 = win32more.UI.Input.KeyboardAndMouse.VK_TO_WCHARS7_head
    VK_TO_WCHARS7._fields_ = [
        ("VirtualKey", Byte),
        ("Attributes", Byte),
        ("wch", Char * 7),
    ]
    return VK_TO_WCHARS7
def _define_VK_TO_WCHARS8_head():
    class VK_TO_WCHARS8(Structure):
        pass
    return VK_TO_WCHARS8
def _define_VK_TO_WCHARS8():
    VK_TO_WCHARS8 = win32more.UI.Input.KeyboardAndMouse.VK_TO_WCHARS8_head
    VK_TO_WCHARS8._fields_ = [
        ("VirtualKey", Byte),
        ("Attributes", Byte),
        ("wch", Char * 8),
    ]
    return VK_TO_WCHARS8
def _define_VK_TO_WCHARS9_head():
    class VK_TO_WCHARS9(Structure):
        pass
    return VK_TO_WCHARS9
def _define_VK_TO_WCHARS9():
    VK_TO_WCHARS9 = win32more.UI.Input.KeyboardAndMouse.VK_TO_WCHARS9_head
    VK_TO_WCHARS9._fields_ = [
        ("VirtualKey", Byte),
        ("Attributes", Byte),
        ("wch", Char * 9),
    ]
    return VK_TO_WCHARS9
def _define_VK_TO_WCHARS10_head():
    class VK_TO_WCHARS10(Structure):
        pass
    return VK_TO_WCHARS10
def _define_VK_TO_WCHARS10():
    VK_TO_WCHARS10 = win32more.UI.Input.KeyboardAndMouse.VK_TO_WCHARS10_head
    VK_TO_WCHARS10._fields_ = [
        ("VirtualKey", Byte),
        ("Attributes", Byte),
        ("wch", Char * 10),
    ]
    return VK_TO_WCHARS10
def _define_VK_TO_WCHAR_TABLE_head():
    class VK_TO_WCHAR_TABLE(Structure):
        pass
    return VK_TO_WCHAR_TABLE
def _define_VK_TO_WCHAR_TABLE():
    VK_TO_WCHAR_TABLE = win32more.UI.Input.KeyboardAndMouse.VK_TO_WCHAR_TABLE_head
    VK_TO_WCHAR_TABLE._fields_ = [
        ("pVkToWchars", POINTER(win32more.UI.Input.KeyboardAndMouse.VK_TO_WCHARS1_head)),
        ("nModifications", Byte),
        ("cbSize", Byte),
    ]
    return VK_TO_WCHAR_TABLE
def _define_DEADKEY_head():
    class DEADKEY(Structure):
        pass
    return DEADKEY
def _define_DEADKEY():
    DEADKEY = win32more.UI.Input.KeyboardAndMouse.DEADKEY_head
    DEADKEY._fields_ = [
        ("dwBoth", UInt32),
        ("wchComposed", Char),
        ("uFlags", UInt16),
    ]
    return DEADKEY
def _define_LIGATURE1_head():
    class LIGATURE1(Structure):
        pass
    return LIGATURE1
def _define_LIGATURE1():
    LIGATURE1 = win32more.UI.Input.KeyboardAndMouse.LIGATURE1_head
    LIGATURE1._fields_ = [
        ("VirtualKey", Byte),
        ("ModificationNumber", UInt16),
        ("wch", Char * 0),
    ]
    return LIGATURE1
def _define_LIGATURE2_head():
    class LIGATURE2(Structure):
        pass
    return LIGATURE2
def _define_LIGATURE2():
    LIGATURE2 = win32more.UI.Input.KeyboardAndMouse.LIGATURE2_head
    LIGATURE2._fields_ = [
        ("VirtualKey", Byte),
        ("ModificationNumber", UInt16),
        ("wch", Char * 2),
    ]
    return LIGATURE2
def _define_LIGATURE3_head():
    class LIGATURE3(Structure):
        pass
    return LIGATURE3
def _define_LIGATURE3():
    LIGATURE3 = win32more.UI.Input.KeyboardAndMouse.LIGATURE3_head
    LIGATURE3._fields_ = [
        ("VirtualKey", Byte),
        ("ModificationNumber", UInt16),
        ("wch", Char * 3),
    ]
    return LIGATURE3
def _define_LIGATURE4_head():
    class LIGATURE4(Structure):
        pass
    return LIGATURE4
def _define_LIGATURE4():
    LIGATURE4 = win32more.UI.Input.KeyboardAndMouse.LIGATURE4_head
    LIGATURE4._fields_ = [
        ("VirtualKey", Byte),
        ("ModificationNumber", UInt16),
        ("wch", Char * 4),
    ]
    return LIGATURE4
def _define_LIGATURE5_head():
    class LIGATURE5(Structure):
        pass
    return LIGATURE5
def _define_LIGATURE5():
    LIGATURE5 = win32more.UI.Input.KeyboardAndMouse.LIGATURE5_head
    LIGATURE5._fields_ = [
        ("VirtualKey", Byte),
        ("ModificationNumber", UInt16),
        ("wch", Char * 5),
    ]
    return LIGATURE5
def _define_VSC_LPWSTR_head():
    class VSC_LPWSTR(Structure):
        pass
    return VSC_LPWSTR
def _define_VSC_LPWSTR():
    VSC_LPWSTR = win32more.UI.Input.KeyboardAndMouse.VSC_LPWSTR_head
    VSC_LPWSTR._fields_ = [
        ("vsc", Byte),
        ("pwsz", win32more.Foundation.PWSTR),
    ]
    return VSC_LPWSTR
def _define_tagKbdLayer_head():
    class tagKbdLayer(Structure):
        pass
    return tagKbdLayer
def _define_tagKbdLayer():
    tagKbdLayer = win32more.UI.Input.KeyboardAndMouse.tagKbdLayer_head
    tagKbdLayer._fields_ = [
        ("pCharModifiers", POINTER(win32more.UI.Input.KeyboardAndMouse.MODIFIERS_head)),
        ("pVkToWcharTable", POINTER(win32more.UI.Input.KeyboardAndMouse.VK_TO_WCHAR_TABLE_head)),
        ("pDeadKey", POINTER(win32more.UI.Input.KeyboardAndMouse.DEADKEY_head)),
        ("pKeyNames", POINTER(win32more.UI.Input.KeyboardAndMouse.VSC_LPWSTR_head)),
        ("pKeyNamesExt", POINTER(win32more.UI.Input.KeyboardAndMouse.VSC_LPWSTR_head)),
        ("pKeyNamesDead", POINTER(POINTER(UInt16))),
        ("pusVSCtoVK", POINTER(UInt16)),
        ("bMaxVSCtoVK", Byte),
        ("pVSCtoVK_E0", POINTER(win32more.UI.Input.KeyboardAndMouse.VSC_VK_head)),
        ("pVSCtoVK_E1", POINTER(win32more.UI.Input.KeyboardAndMouse.VSC_VK_head)),
        ("fLocaleFlags", UInt32),
        ("nLgMax", Byte),
        ("cbLgEntry", Byte),
        ("pLigature", POINTER(win32more.UI.Input.KeyboardAndMouse.LIGATURE1_head)),
        ("dwType", UInt32),
        ("dwSubType", UInt32),
    ]
    return tagKbdLayer
def _define__VK_FUNCTION_PARAM_head():
    class _VK_FUNCTION_PARAM(Structure):
        pass
    return _VK_FUNCTION_PARAM
def _define__VK_FUNCTION_PARAM():
    _VK_FUNCTION_PARAM = win32more.UI.Input.KeyboardAndMouse._VK_FUNCTION_PARAM_head
    _VK_FUNCTION_PARAM._fields_ = [
        ("NLSFEProcIndex", Byte),
        ("NLSFEProcParam", UInt32),
    ]
    return _VK_FUNCTION_PARAM
def _define__VK_TO_FUNCTION_TABLE_head():
    class _VK_TO_FUNCTION_TABLE(Structure):
        pass
    return _VK_TO_FUNCTION_TABLE
def _define__VK_TO_FUNCTION_TABLE():
    _VK_TO_FUNCTION_TABLE = win32more.UI.Input.KeyboardAndMouse._VK_TO_FUNCTION_TABLE_head
    _VK_TO_FUNCTION_TABLE._fields_ = [
        ("Vk", Byte),
        ("NLSFEProcType", Byte),
        ("NLSFEProcCurrent", Byte),
        ("NLSFEProcSwitch", Byte),
        ("NLSFEProc", win32more.UI.Input.KeyboardAndMouse._VK_FUNCTION_PARAM * 8),
        ("NLSFEProcAlt", win32more.UI.Input.KeyboardAndMouse._VK_FUNCTION_PARAM * 8),
    ]
    return _VK_TO_FUNCTION_TABLE
def _define_tagKbdNlsLayer_head():
    class tagKbdNlsLayer(Structure):
        pass
    return tagKbdNlsLayer
def _define_tagKbdNlsLayer():
    tagKbdNlsLayer = win32more.UI.Input.KeyboardAndMouse.tagKbdNlsLayer_head
    tagKbdNlsLayer._fields_ = [
        ("OEMIdentifier", UInt16),
        ("LayoutInformation", UInt16),
        ("NumOfVkToF", UInt32),
        ("pVkToF", POINTER(win32more.UI.Input.KeyboardAndMouse._VK_TO_FUNCTION_TABLE_head)),
        ("NumOfMouseVKey", Int32),
        ("pusMouseVKey", POINTER(UInt16)),
    ]
    return tagKbdNlsLayer
def _define_KBDTABLE_DESC_head():
    class KBDTABLE_DESC(Structure):
        pass
    return KBDTABLE_DESC
def _define_KBDTABLE_DESC():
    KBDTABLE_DESC = win32more.UI.Input.KeyboardAndMouse.KBDTABLE_DESC_head
    KBDTABLE_DESC._fields_ = [
        ("wszDllName", Char * 32),
        ("dwType", UInt32),
        ("dwSubType", UInt32),
    ]
    return KBDTABLE_DESC
def _define_KBDTABLE_MULTI_head():
    class KBDTABLE_MULTI(Structure):
        pass
    return KBDTABLE_MULTI
def _define_KBDTABLE_MULTI():
    KBDTABLE_MULTI = win32more.UI.Input.KeyboardAndMouse.KBDTABLE_MULTI_head
    KBDTABLE_MULTI._fields_ = [
        ("nTables", UInt32),
        ("aKbdTables", win32more.UI.Input.KeyboardAndMouse.KBDTABLE_DESC * 8),
    ]
    return KBDTABLE_MULTI
def _define_KBD_TYPE_INFO_head():
    class KBD_TYPE_INFO(Structure):
        pass
    return KBD_TYPE_INFO
def _define_KBD_TYPE_INFO():
    KBD_TYPE_INFO = win32more.UI.Input.KeyboardAndMouse.KBD_TYPE_INFO_head
    KBD_TYPE_INFO._fields_ = [
        ("dwVersion", UInt32),
        ("dwType", UInt32),
        ("dwSubType", UInt32),
    ]
    return KBD_TYPE_INFO
def _define_MOUSEMOVEPOINT_head():
    class MOUSEMOVEPOINT(Structure):
        pass
    return MOUSEMOVEPOINT
def _define_MOUSEMOVEPOINT():
    MOUSEMOVEPOINT = win32more.UI.Input.KeyboardAndMouse.MOUSEMOVEPOINT_head
    MOUSEMOVEPOINT._fields_ = [
        ("x", Int32),
        ("y", Int32),
        ("time", UInt32),
        ("dwExtraInfo", UIntPtr),
    ]
    return MOUSEMOVEPOINT
def _define_TRACKMOUSEEVENT_head():
    class TRACKMOUSEEVENT(Structure):
        pass
    return TRACKMOUSEEVENT
def _define_TRACKMOUSEEVENT():
    TRACKMOUSEEVENT = win32more.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT_head
    TRACKMOUSEEVENT._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", win32more.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT_FLAGS),
        ("hwndTrack", win32more.Foundation.HWND),
        ("dwHoverTime", UInt32),
    ]
    return TRACKMOUSEEVENT
def _define_MOUSEINPUT_head():
    class MOUSEINPUT(Structure):
        pass
    return MOUSEINPUT
def _define_MOUSEINPUT():
    MOUSEINPUT = win32more.UI.Input.KeyboardAndMouse.MOUSEINPUT_head
    MOUSEINPUT._fields_ = [
        ("dx", Int32),
        ("dy", Int32),
        ("mouseData", UInt32),
        ("dwFlags", win32more.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS),
        ("time", UInt32),
        ("dwExtraInfo", UIntPtr),
    ]
    return MOUSEINPUT
def _define_KEYBDINPUT_head():
    class KEYBDINPUT(Structure):
        pass
    return KEYBDINPUT
def _define_KEYBDINPUT():
    KEYBDINPUT = win32more.UI.Input.KeyboardAndMouse.KEYBDINPUT_head
    KEYBDINPUT._fields_ = [
        ("wVk", win32more.UI.Input.KeyboardAndMouse.VIRTUAL_KEY),
        ("wScan", UInt16),
        ("dwFlags", win32more.UI.Input.KeyboardAndMouse.KEYBD_EVENT_FLAGS),
        ("time", UInt32),
        ("dwExtraInfo", UIntPtr),
    ]
    return KEYBDINPUT
def _define_HARDWAREINPUT_head():
    class HARDWAREINPUT(Structure):
        pass
    return HARDWAREINPUT
def _define_HARDWAREINPUT():
    HARDWAREINPUT = win32more.UI.Input.KeyboardAndMouse.HARDWAREINPUT_head
    HARDWAREINPUT._fields_ = [
        ("uMsg", UInt32),
        ("wParamL", UInt16),
        ("wParamH", UInt16),
    ]
    return HARDWAREINPUT
def _define_INPUT_head():
    class INPUT(Structure):
        pass
    return INPUT
def _define_INPUT():
    INPUT = win32more.UI.Input.KeyboardAndMouse.INPUT_head
    class INPUT__Anonymous_e__Union(Union):
        pass
    INPUT__Anonymous_e__Union._fields_ = [
        ("mi", win32more.UI.Input.KeyboardAndMouse.MOUSEINPUT),
        ("ki", win32more.UI.Input.KeyboardAndMouse.KEYBDINPUT),
        ("hi", win32more.UI.Input.KeyboardAndMouse.HARDWAREINPUT),
    ]
    INPUT._anonymous_ = [
        'Anonymous',
    ]
    INPUT._fields_ = [
        ("type", win32more.UI.Input.KeyboardAndMouse.INPUT_TYPE),
        ("Anonymous", INPUT__Anonymous_e__Union),
    ]
    return INPUT
def _define_LASTINPUTINFO_head():
    class LASTINPUTINFO(Structure):
        pass
    return LASTINPUTINFO
def _define_LASTINPUTINFO():
    LASTINPUTINFO = win32more.UI.Input.KeyboardAndMouse.LASTINPUTINFO_head
    LASTINPUTINFO._fields_ = [
        ("cbSize", UInt32),
        ("dwTime", UInt32),
    ]
    return LASTINPUTINFO
def _define__TrackMouseEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT_head), use_last_error=False)(("_TrackMouseEvent", windll["COMCTL32"]), ((1, 'lpEventTrack'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadKeyboardLayoutA():
    try:
        return WINFUNCTYPE(win32more.UI.TextServices.HKL,win32more.Foundation.PSTR,win32more.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS, use_last_error=True)(("LoadKeyboardLayoutA", windll["USER32"]), ((1, 'pwszKLID'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadKeyboardLayoutW():
    try:
        return WINFUNCTYPE(win32more.UI.TextServices.HKL,win32more.Foundation.PWSTR,win32more.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS, use_last_error=True)(("LoadKeyboardLayoutW", windll["USER32"]), ((1, 'pwszKLID'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadKeyboardLayout():
    return win32more.UI.Input.KeyboardAndMouse.LoadKeyboardLayoutW
def _define_ActivateKeyboardLayout():
    try:
        return WINFUNCTYPE(win32more.UI.TextServices.HKL,win32more.UI.TextServices.HKL,win32more.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS, use_last_error=True)(("ActivateKeyboardLayout", windll["USER32"]), ((1, 'hkl'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ToUnicodeEx():
    try:
        return WINFUNCTYPE(Int32,UInt32,UInt32,POINTER(Byte),POINTER(Char),Int32,UInt32,win32more.UI.TextServices.HKL, use_last_error=False)(("ToUnicodeEx", windll["USER32"]), ((1, 'wVirtKey'),(1, 'wScanCode'),(1, 'lpKeyState'),(1, 'pwszBuff'),(1, 'cchBuff'),(1, 'wFlags'),(1, 'dwhkl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnloadKeyboardLayout():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.TextServices.HKL, use_last_error=True)(("UnloadKeyboardLayout", windll["USER32"]), ((1, 'hkl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetKeyboardLayoutNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Byte), use_last_error=True)(("GetKeyboardLayoutNameA", windll["USER32"]), ((1, 'pwszKLID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetKeyboardLayoutNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Char), use_last_error=True)(("GetKeyboardLayoutNameW", windll["USER32"]), ((1, 'pwszKLID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetKeyboardLayoutName():
    return win32more.UI.Input.KeyboardAndMouse.GetKeyboardLayoutNameW
def _define_GetKeyboardLayoutList():
    try:
        return WINFUNCTYPE(Int32,Int32,POINTER(win32more.UI.TextServices.HKL), use_last_error=True)(("GetKeyboardLayoutList", windll["USER32"]), ((1, 'nBuff'),(1, 'lpList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetKeyboardLayout():
    try:
        return WINFUNCTYPE(win32more.UI.TextServices.HKL,UInt32, use_last_error=False)(("GetKeyboardLayout", windll["USER32"]), ((1, 'idThread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMouseMovePointsEx():
    try:
        return WINFUNCTYPE(Int32,UInt32,POINTER(win32more.UI.Input.KeyboardAndMouse.MOUSEMOVEPOINT_head),POINTER(win32more.UI.Input.KeyboardAndMouse.MOUSEMOVEPOINT),Int32,win32more.UI.Input.KeyboardAndMouse.GET_MOUSE_MOVE_POINTS_EX_RESOLUTION, use_last_error=True)(("GetMouseMovePointsEx", windll["USER32"]), ((1, 'cbSize'),(1, 'lppt'),(1, 'lpptBuf'),(1, 'nBufPoints'),(1, 'resolution'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TrackMouseEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT_head), use_last_error=True)(("TrackMouseEvent", windll["USER32"]), ((1, 'lpEventTrack'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterHotKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,Int32,win32more.UI.Input.KeyboardAndMouse.HOT_KEY_MODIFIERS,UInt32, use_last_error=True)(("RegisterHotKey", windll["USER32"]), ((1, 'hWnd'),(1, 'id'),(1, 'fsModifiers'),(1, 'vk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterHotKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,Int32, use_last_error=True)(("UnregisterHotKey", windll["USER32"]), ((1, 'hWnd'),(1, 'id'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwapMouseButton():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(("SwapMouseButton", windll["USER32"]), ((1, 'fSwap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDoubleClickTime():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("GetDoubleClickTime", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDoubleClickTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=True)(("SetDoubleClickTime", windll["USER32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFocus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,win32more.Foundation.HWND, use_last_error=True)(("SetFocus", windll["USER32"]), ((1, 'hWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetActiveWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND, use_last_error=False)(("GetActiveWindow", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFocus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND, use_last_error=False)(("GetFocus", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetKBCodePage():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("GetKBCodePage", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetKeyState():
    try:
        return WINFUNCTYPE(Int16,Int32, use_last_error=False)(("GetKeyState", windll["USER32"]), ((1, 'nVirtKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAsyncKeyState():
    try:
        return WINFUNCTYPE(Int16,Int32, use_last_error=False)(("GetAsyncKeyState", windll["USER32"]), ((1, 'vKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetKeyboardState():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Byte), use_last_error=True)(("GetKeyboardState", windll["USER32"]), ((1, 'lpKeyState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetKeyboardState():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Byte), use_last_error=True)(("SetKeyboardState", windll["USER32"]), ((1, 'lpKeyState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetKeyNameTextA():
    try:
        return WINFUNCTYPE(Int32,Int32,POINTER(Byte),Int32, use_last_error=True)(("GetKeyNameTextA", windll["USER32"]), ((1, 'lParam'),(1, 'lpString'),(1, 'cchSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetKeyNameTextW():
    try:
        return WINFUNCTYPE(Int32,Int32,POINTER(Char),Int32, use_last_error=True)(("GetKeyNameTextW", windll["USER32"]), ((1, 'lParam'),(1, 'lpString'),(1, 'cchSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetKeyNameText():
    return win32more.UI.Input.KeyboardAndMouse.GetKeyNameTextW
def _define_GetKeyboardType():
    try:
        return WINFUNCTYPE(Int32,Int32, use_last_error=True)(("GetKeyboardType", windll["USER32"]), ((1, 'nTypeFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ToAscii():
    try:
        return WINFUNCTYPE(Int32,UInt32,UInt32,POINTER(Byte),POINTER(UInt16),UInt32, use_last_error=False)(("ToAscii", windll["USER32"]), ((1, 'uVirtKey'),(1, 'uScanCode'),(1, 'lpKeyState'),(1, 'lpChar'),(1, 'uFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ToAsciiEx():
    try:
        return WINFUNCTYPE(Int32,UInt32,UInt32,POINTER(Byte),POINTER(UInt16),UInt32,win32more.UI.TextServices.HKL, use_last_error=False)(("ToAsciiEx", windll["USER32"]), ((1, 'uVirtKey'),(1, 'uScanCode'),(1, 'lpKeyState'),(1, 'lpChar'),(1, 'uFlags'),(1, 'dwhkl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ToUnicode():
    try:
        return WINFUNCTYPE(Int32,UInt32,UInt32,POINTER(Byte),POINTER(Char),Int32,UInt32, use_last_error=False)(("ToUnicode", windll["USER32"]), ((1, 'wVirtKey'),(1, 'wScanCode'),(1, 'lpKeyState'),(1, 'pwszBuff'),(1, 'cchBuff'),(1, 'wFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OemKeyScan():
    try:
        return WINFUNCTYPE(UInt32,UInt16, use_last_error=False)(("OemKeyScan", windll["USER32"]), ((1, 'wOemChar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VkKeyScanA():
    try:
        return WINFUNCTYPE(Int16,win32more.Foundation.CHAR, use_last_error=False)(("VkKeyScanA", windll["USER32"]), ((1, 'ch'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VkKeyScanW():
    try:
        return WINFUNCTYPE(Int16,Char, use_last_error=False)(("VkKeyScanW", windll["USER32"]), ((1, 'ch'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VkKeyScan():
    return win32more.UI.Input.KeyboardAndMouse.VkKeyScanW
def _define_VkKeyScanExA():
    try:
        return WINFUNCTYPE(Int16,win32more.Foundation.CHAR,win32more.UI.TextServices.HKL, use_last_error=False)(("VkKeyScanExA", windll["USER32"]), ((1, 'ch'),(1, 'dwhkl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VkKeyScanExW():
    try:
        return WINFUNCTYPE(Int16,Char,win32more.UI.TextServices.HKL, use_last_error=False)(("VkKeyScanExW", windll["USER32"]), ((1, 'ch'),(1, 'dwhkl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VkKeyScanEx():
    return win32more.UI.Input.KeyboardAndMouse.VkKeyScanExW
def _define_keybd_event():
    try:
        return WINFUNCTYPE(Void,Byte,Byte,win32more.UI.Input.KeyboardAndMouse.KEYBD_EVENT_FLAGS,UIntPtr, use_last_error=False)(("keybd_event", windll["USER32"]), ((1, 'bVk'),(1, 'bScan'),(1, 'dwFlags'),(1, 'dwExtraInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_mouse_event():
    try:
        return WINFUNCTYPE(Void,win32more.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS,Int32,Int32,UInt32,UIntPtr, use_last_error=False)(("mouse_event", windll["USER32"]), ((1, 'dwFlags'),(1, 'dx'),(1, 'dy'),(1, 'dwData'),(1, 'dwExtraInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SendInput():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.UI.Input.KeyboardAndMouse.INPUT),Int32, use_last_error=True)(("SendInput", windll["USER32"]), ((1, 'cInputs'),(1, 'pInputs'),(1, 'cbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLastInputInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Input.KeyboardAndMouse.LASTINPUTINFO_head), use_last_error=False)(("GetLastInputInfo", windll["USER32"]), ((1, 'plii'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapVirtualKeyA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32, use_last_error=False)(("MapVirtualKeyA", windll["USER32"]), ((1, 'uCode'),(1, 'uMapType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapVirtualKeyW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32, use_last_error=False)(("MapVirtualKeyW", windll["USER32"]), ((1, 'uCode'),(1, 'uMapType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapVirtualKey():
    return win32more.UI.Input.KeyboardAndMouse.MapVirtualKeyW
def _define_MapVirtualKeyExA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,win32more.UI.TextServices.HKL, use_last_error=False)(("MapVirtualKeyExA", windll["USER32"]), ((1, 'uCode'),(1, 'uMapType'),(1, 'dwhkl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapVirtualKeyExW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,win32more.UI.TextServices.HKL, use_last_error=False)(("MapVirtualKeyExW", windll["USER32"]), ((1, 'uCode'),(1, 'uMapType'),(1, 'dwhkl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapVirtualKeyEx():
    return win32more.UI.Input.KeyboardAndMouse.MapVirtualKeyExW
def _define_GetCapture():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND, use_last_error=False)(("GetCapture", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCapture():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,win32more.Foundation.HWND, use_last_error=False)(("SetCapture", windll["USER32"]), ((1, 'hWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseCapture():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=True)(("ReleaseCapture", windll["USER32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnableWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.BOOL, use_last_error=False)(("EnableWindow", windll["USER32"]), ((1, 'hWnd'),(1, 'bEnable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsWindowEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND, use_last_error=False)(("IsWindowEnabled", windll["USER32"]), ((1, 'hWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DragDetect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.POINT, use_last_error=False)(("DragDetect", windll["USER32"]), ((1, 'hwnd'),(1, 'pt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetActiveWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,win32more.Foundation.HWND, use_last_error=True)(("SetActiveWindow", windll["USER32"]), ((1, 'hWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BlockInput():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=True)(("BlockInput", windll["USER32"]), ((1, 'fBlockIt'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "EXTENDED_BIT",
    "DONTCARE_BIT",
    "FAKE_KEYSTROKE",
    "KBDBASE",
    "KBDSHIFT",
    "KBDCTRL",
    "KBDALT",
    "KBDKANA",
    "KBDROYA",
    "KBDLOYA",
    "KBDGRPSELTAP",
    "GRAVE",
    "ACUTE",
    "CIRCUMFLEX",
    "TILDE",
    "MACRON",
    "OVERSCORE",
    "BREVE",
    "DOT_ABOVE",
    "UMLAUT",
    "DIARESIS",
    "HOOK_ABOVE",
    "RING",
    "DOUBLE_ACUTE",
    "HACEK",
    "CEDILLA",
    "OGONEK",
    "TONOS",
    "DIARESIS_TONOS",
    "SHFT_INVALID",
    "WCH_NONE",
    "WCH_DEAD",
    "WCH_LGTR",
    "CAPLOK",
    "SGCAPS",
    "CAPLOKALTGR",
    "KANALOK",
    "GRPSELTAP",
    "DKF_DEAD",
    "KBD_VERSION",
    "KLLF_ALTGR",
    "KLLF_SHIFTLOCK",
    "KLLF_LRM_RLM",
    "KLLF_GLOBAL_ATTRS",
    "KBDTABLE_MULTI_MAX",
    "KEYBOARD_TYPE_GENERIC_101",
    "KEYBOARD_TYPE_JAPAN",
    "KEYBOARD_TYPE_KOREA",
    "KEYBOARD_TYPE_UNKNOWN",
    "NLSKBD_OEM_MICROSOFT",
    "NLSKBD_OEM_AX",
    "NLSKBD_OEM_EPSON",
    "NLSKBD_OEM_FUJITSU",
    "NLSKBD_OEM_IBM",
    "NLSKBD_OEM_MATSUSHITA",
    "NLSKBD_OEM_NEC",
    "NLSKBD_OEM_TOSHIBA",
    "NLSKBD_OEM_DEC",
    "MICROSOFT_KBD_101_TYPE",
    "MICROSOFT_KBD_AX_TYPE",
    "MICROSOFT_KBD_106_TYPE",
    "MICROSOFT_KBD_002_TYPE",
    "MICROSOFT_KBD_001_TYPE",
    "MICROSOFT_KBD_FUNC",
    "AX_KBD_DESKTOP_TYPE",
    "FMR_KBD_JIS_TYPE",
    "FMR_KBD_OASYS_TYPE",
    "FMV_KBD_OASYS_TYPE",
    "NEC_KBD_NORMAL_TYPE",
    "NEC_KBD_N_MODE_TYPE",
    "NEC_KBD_H_MODE_TYPE",
    "NEC_KBD_LAPTOP_TYPE",
    "NEC_KBD_106_TYPE",
    "TOSHIBA_KBD_DESKTOP_TYPE",
    "TOSHIBA_KBD_LAPTOP_TYPE",
    "DEC_KBD_ANSI_LAYOUT_TYPE",
    "DEC_KBD_JIS_LAYOUT_TYPE",
    "MICROSOFT_KBD_101A_TYPE",
    "MICROSOFT_KBD_101B_TYPE",
    "MICROSOFT_KBD_101C_TYPE",
    "MICROSOFT_KBD_103_TYPE",
    "NLSKBD_INFO_SEND_IME_NOTIFICATION",
    "NLSKBD_INFO_ACCESSIBILITY_KEYMAP",
    "NLSKBD_INFO_EMURATE_101_KEYBOARD",
    "NLSKBD_INFO_EMURATE_106_KEYBOARD",
    "KBDNLS_TYPE_NULL",
    "KBDNLS_TYPE_NORMAL",
    "KBDNLS_TYPE_TOGGLE",
    "KBDNLS_INDEX_NORMAL",
    "KBDNLS_INDEX_ALT",
    "KBDNLS_NULL",
    "KBDNLS_NOEVENT",
    "KBDNLS_SEND_BASE_VK",
    "KBDNLS_SEND_PARAM_VK",
    "KBDNLS_KANALOCK",
    "KBDNLS_ALPHANUM",
    "KBDNLS_HIRAGANA",
    "KBDNLS_KATAKANA",
    "KBDNLS_SBCSDBCS",
    "KBDNLS_ROMAN",
    "KBDNLS_CODEINPUT",
    "KBDNLS_HELP_OR_END",
    "KBDNLS_HOME_OR_CLEAR",
    "KBDNLS_NUMPAD",
    "KBDNLS_KANAEVENT",
    "KBDNLS_CONV_OR_NONCONV",
    "KBD_TYPE",
    "VK__none_",
    "VK_ABNT_C1",
    "VK_ABNT_C2",
    "SCANCODE_LSHIFT",
    "SCANCODE_RSHIFT",
    "SCANCODE_CTRL",
    "SCANCODE_ALT",
    "SCANCODE_NUMPAD_FIRST",
    "SCANCODE_NUMPAD_LAST",
    "SCANCODE_LWIN",
    "SCANCODE_RWIN",
    "SCANCODE_THAI_LAYOUT_TOGGLE",
    "VK_DBE_ALPHANUMERIC",
    "VK_DBE_KATAKANA",
    "VK_DBE_HIRAGANA",
    "VK_DBE_SBCSCHAR",
    "VK_DBE_DBCSCHAR",
    "VK_DBE_ROMAN",
    "VK_DBE_NOROMAN",
    "VK_DBE_ENTERWORDREGISTERMODE",
    "VK_DBE_ENTERIMECONFIGMODE",
    "VK_DBE_FLUSHSTRING",
    "VK_DBE_CODEINPUT",
    "VK_DBE_NOCODEINPUT",
    "VK_DBE_DETERMINESTRING",
    "VK_DBE_ENTERDLGCONVERSIONMODE",
    "HOT_KEY_MODIFIERS",
    "MOD_ALT",
    "MOD_CONTROL",
    "MOD_NOREPEAT",
    "MOD_SHIFT",
    "MOD_WIN",
    "ACTIVATE_KEYBOARD_LAYOUT_FLAGS",
    "KLF_REORDER",
    "KLF_RESET",
    "KLF_SETFORPROCESS",
    "KLF_SHIFTLOCK",
    "KLF_ACTIVATE",
    "KLF_NOTELLSHELL",
    "KLF_REPLACELANG",
    "KLF_SUBSTITUTE_OK",
    "GET_MOUSE_MOVE_POINTS_EX_RESOLUTION",
    "GMMP_USE_DISPLAY_POINTS",
    "GMMP_USE_HIGH_RESOLUTION_POINTS",
    "KEYBD_EVENT_FLAGS",
    "KEYEVENTF_EXTENDEDKEY",
    "KEYEVENTF_KEYUP",
    "KEYEVENTF_SCANCODE",
    "KEYEVENTF_UNICODE",
    "MOUSE_EVENT_FLAGS",
    "MOUSEEVENTF_ABSOLUTE",
    "MOUSEEVENTF_LEFTDOWN",
    "MOUSEEVENTF_LEFTUP",
    "MOUSEEVENTF_MIDDLEDOWN",
    "MOUSEEVENTF_MIDDLEUP",
    "MOUSEEVENTF_MOVE",
    "MOUSEEVENTF_RIGHTDOWN",
    "MOUSEEVENTF_RIGHTUP",
    "MOUSEEVENTF_WHEEL",
    "MOUSEEVENTF_XDOWN",
    "MOUSEEVENTF_XUP",
    "MOUSEEVENTF_HWHEEL",
    "MOUSEEVENTF_MOVE_NOCOALESCE",
    "MOUSEEVENTF_VIRTUALDESK",
    "INPUT_TYPE",
    "INPUT_MOUSE",
    "INPUT_KEYBOARD",
    "INPUT_HARDWARE",
    "TRACKMOUSEEVENT_FLAGS",
    "TME_CANCEL",
    "TME_HOVER",
    "TME_LEAVE",
    "TME_NONCLIENT",
    "TME_QUERY",
    "VIRTUAL_KEY",
    "VK_0",
    "VK_1",
    "VK_2",
    "VK_3",
    "VK_4",
    "VK_5",
    "VK_6",
    "VK_7",
    "VK_8",
    "VK_9",
    "VK_A",
    "VK_B",
    "VK_C",
    "VK_D",
    "VK_E",
    "VK_F",
    "VK_G",
    "VK_H",
    "VK_I",
    "VK_J",
    "VK_K",
    "VK_L",
    "VK_M",
    "VK_N",
    "VK_O",
    "VK_P",
    "VK_Q",
    "VK_R",
    "VK_S",
    "VK_T",
    "VK_U",
    "VK_V",
    "VK_W",
    "VK_X",
    "VK_Y",
    "VK_Z",
    "VK_LBUTTON",
    "VK_RBUTTON",
    "VK_CANCEL",
    "VK_MBUTTON",
    "VK_XBUTTON1",
    "VK_XBUTTON2",
    "VK_BACK",
    "VK_TAB",
    "VK_CLEAR",
    "VK_RETURN",
    "VK_SHIFT",
    "VK_CONTROL",
    "VK_MENU",
    "VK_PAUSE",
    "VK_CAPITAL",
    "VK_KANA",
    "VK_HANGEUL",
    "VK_HANGUL",
    "VK_IME_ON",
    "VK_JUNJA",
    "VK_FINAL",
    "VK_HANJA",
    "VK_KANJI",
    "VK_IME_OFF",
    "VK_ESCAPE",
    "VK_CONVERT",
    "VK_NONCONVERT",
    "VK_ACCEPT",
    "VK_MODECHANGE",
    "VK_SPACE",
    "VK_PRIOR",
    "VK_NEXT",
    "VK_END",
    "VK_HOME",
    "VK_LEFT",
    "VK_UP",
    "VK_RIGHT",
    "VK_DOWN",
    "VK_SELECT",
    "VK_PRINT",
    "VK_EXECUTE",
    "VK_SNAPSHOT",
    "VK_INSERT",
    "VK_DELETE",
    "VK_HELP",
    "VK_LWIN",
    "VK_RWIN",
    "VK_APPS",
    "VK_SLEEP",
    "VK_NUMPAD0",
    "VK_NUMPAD1",
    "VK_NUMPAD2",
    "VK_NUMPAD3",
    "VK_NUMPAD4",
    "VK_NUMPAD5",
    "VK_NUMPAD6",
    "VK_NUMPAD7",
    "VK_NUMPAD8",
    "VK_NUMPAD9",
    "VK_MULTIPLY",
    "VK_ADD",
    "VK_SEPARATOR",
    "VK_SUBTRACT",
    "VK_DECIMAL",
    "VK_DIVIDE",
    "VK_F1",
    "VK_F2",
    "VK_F3",
    "VK_F4",
    "VK_F5",
    "VK_F6",
    "VK_F7",
    "VK_F8",
    "VK_F9",
    "VK_F10",
    "VK_F11",
    "VK_F12",
    "VK_F13",
    "VK_F14",
    "VK_F15",
    "VK_F16",
    "VK_F17",
    "VK_F18",
    "VK_F19",
    "VK_F20",
    "VK_F21",
    "VK_F22",
    "VK_F23",
    "VK_F24",
    "VK_NAVIGATION_VIEW",
    "VK_NAVIGATION_MENU",
    "VK_NAVIGATION_UP",
    "VK_NAVIGATION_DOWN",
    "VK_NAVIGATION_LEFT",
    "VK_NAVIGATION_RIGHT",
    "VK_NAVIGATION_ACCEPT",
    "VK_NAVIGATION_CANCEL",
    "VK_NUMLOCK",
    "VK_SCROLL",
    "VK_OEM_NEC_EQUAL",
    "VK_OEM_FJ_JISHO",
    "VK_OEM_FJ_MASSHOU",
    "VK_OEM_FJ_TOUROKU",
    "VK_OEM_FJ_LOYA",
    "VK_OEM_FJ_ROYA",
    "VK_LSHIFT",
    "VK_RSHIFT",
    "VK_LCONTROL",
    "VK_RCONTROL",
    "VK_LMENU",
    "VK_RMENU",
    "VK_BROWSER_BACK",
    "VK_BROWSER_FORWARD",
    "VK_BROWSER_REFRESH",
    "VK_BROWSER_STOP",
    "VK_BROWSER_SEARCH",
    "VK_BROWSER_FAVORITES",
    "VK_BROWSER_HOME",
    "VK_VOLUME_MUTE",
    "VK_VOLUME_DOWN",
    "VK_VOLUME_UP",
    "VK_MEDIA_NEXT_TRACK",
    "VK_MEDIA_PREV_TRACK",
    "VK_MEDIA_STOP",
    "VK_MEDIA_PLAY_PAUSE",
    "VK_LAUNCH_MAIL",
    "VK_LAUNCH_MEDIA_SELECT",
    "VK_LAUNCH_APP1",
    "VK_LAUNCH_APP2",
    "VK_OEM_1",
    "VK_OEM_PLUS",
    "VK_OEM_COMMA",
    "VK_OEM_MINUS",
    "VK_OEM_PERIOD",
    "VK_OEM_2",
    "VK_OEM_3",
    "VK_GAMEPAD_A",
    "VK_GAMEPAD_B",
    "VK_GAMEPAD_X",
    "VK_GAMEPAD_Y",
    "VK_GAMEPAD_RIGHT_SHOULDER",
    "VK_GAMEPAD_LEFT_SHOULDER",
    "VK_GAMEPAD_LEFT_TRIGGER",
    "VK_GAMEPAD_RIGHT_TRIGGER",
    "VK_GAMEPAD_DPAD_UP",
    "VK_GAMEPAD_DPAD_DOWN",
    "VK_GAMEPAD_DPAD_LEFT",
    "VK_GAMEPAD_DPAD_RIGHT",
    "VK_GAMEPAD_MENU",
    "VK_GAMEPAD_VIEW",
    "VK_GAMEPAD_LEFT_THUMBSTICK_BUTTON",
    "VK_GAMEPAD_RIGHT_THUMBSTICK_BUTTON",
    "VK_GAMEPAD_LEFT_THUMBSTICK_UP",
    "VK_GAMEPAD_LEFT_THUMBSTICK_DOWN",
    "VK_GAMEPAD_LEFT_THUMBSTICK_RIGHT",
    "VK_GAMEPAD_LEFT_THUMBSTICK_LEFT",
    "VK_GAMEPAD_RIGHT_THUMBSTICK_UP",
    "VK_GAMEPAD_RIGHT_THUMBSTICK_DOWN",
    "VK_GAMEPAD_RIGHT_THUMBSTICK_RIGHT",
    "VK_GAMEPAD_RIGHT_THUMBSTICK_LEFT",
    "VK_OEM_4",
    "VK_OEM_5",
    "VK_OEM_6",
    "VK_OEM_7",
    "VK_OEM_8",
    "VK_OEM_AX",
    "VK_OEM_102",
    "VK_ICO_HELP",
    "VK_ICO_00",
    "VK_PROCESSKEY",
    "VK_ICO_CLEAR",
    "VK_PACKET",
    "VK_OEM_RESET",
    "VK_OEM_JUMP",
    "VK_OEM_PA1",
    "VK_OEM_PA2",
    "VK_OEM_PA3",
    "VK_OEM_WSCTRL",
    "VK_OEM_CUSEL",
    "VK_OEM_ATTN",
    "VK_OEM_FINISH",
    "VK_OEM_COPY",
    "VK_OEM_AUTO",
    "VK_OEM_ENLW",
    "VK_OEM_BACKTAB",
    "VK_ATTN",
    "VK_CRSEL",
    "VK_EXSEL",
    "VK_EREOF",
    "VK_PLAY",
    "VK_ZOOM",
    "VK_NONAME",
    "VK_PA1",
    "VK_OEM_CLEAR",
    "VK_TO_BIT",
    "MODIFIERS",
    "VSC_VK",
    "VK_VSC",
    "VK_TO_WCHARS1",
    "VK_TO_WCHARS2",
    "VK_TO_WCHARS3",
    "VK_TO_WCHARS4",
    "VK_TO_WCHARS5",
    "VK_TO_WCHARS6",
    "VK_TO_WCHARS7",
    "VK_TO_WCHARS8",
    "VK_TO_WCHARS9",
    "VK_TO_WCHARS10",
    "VK_TO_WCHAR_TABLE",
    "DEADKEY",
    "LIGATURE1",
    "LIGATURE2",
    "LIGATURE3",
    "LIGATURE4",
    "LIGATURE5",
    "VSC_LPWSTR",
    "tagKbdLayer",
    "_VK_FUNCTION_PARAM",
    "_VK_TO_FUNCTION_TABLE",
    "tagKbdNlsLayer",
    "KBDTABLE_DESC",
    "KBDTABLE_MULTI",
    "KBD_TYPE_INFO",
    "MOUSEMOVEPOINT",
    "TRACKMOUSEEVENT",
    "MOUSEINPUT",
    "KEYBDINPUT",
    "HARDWAREINPUT",
    "INPUT",
    "LASTINPUTINFO",
    "_TrackMouseEvent",
    "LoadKeyboardLayoutA",
    "LoadKeyboardLayoutW",
    "LoadKeyboardLayout",
    "ActivateKeyboardLayout",
    "ToUnicodeEx",
    "UnloadKeyboardLayout",
    "GetKeyboardLayoutNameA",
    "GetKeyboardLayoutNameW",
    "GetKeyboardLayoutName",
    "GetKeyboardLayoutList",
    "GetKeyboardLayout",
    "GetMouseMovePointsEx",
    "TrackMouseEvent",
    "RegisterHotKey",
    "UnregisterHotKey",
    "SwapMouseButton",
    "GetDoubleClickTime",
    "SetDoubleClickTime",
    "SetFocus",
    "GetActiveWindow",
    "GetFocus",
    "GetKBCodePage",
    "GetKeyState",
    "GetAsyncKeyState",
    "GetKeyboardState",
    "SetKeyboardState",
    "GetKeyNameTextA",
    "GetKeyNameTextW",
    "GetKeyNameText",
    "GetKeyboardType",
    "ToAscii",
    "ToAsciiEx",
    "ToUnicode",
    "OemKeyScan",
    "VkKeyScanA",
    "VkKeyScanW",
    "VkKeyScan",
    "VkKeyScanExA",
    "VkKeyScanExW",
    "VkKeyScanEx",
    "keybd_event",
    "mouse_event",
    "SendInput",
    "GetLastInputInfo",
    "MapVirtualKeyA",
    "MapVirtualKeyW",
    "MapVirtualKey",
    "MapVirtualKeyExA",
    "MapVirtualKeyExW",
    "MapVirtualKeyEx",
    "GetCapture",
    "SetCapture",
    "ReleaseCapture",
    "EnableWindow",
    "IsWindowEnabled",
    "DragDetect",
    "SetActiveWindow",
    "BlockInput",
]
