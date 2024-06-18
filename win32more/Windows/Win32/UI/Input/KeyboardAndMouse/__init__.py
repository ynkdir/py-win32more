from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.UI.Input.KeyboardAndMouse
ACTIVATE_KEYBOARD_LAYOUT_FLAGS = UInt32
KLF_REORDER: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 8
KLF_RESET: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 1073741824
KLF_SETFORPROCESS: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 256
KLF_SHIFTLOCK: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 65536
KLF_ACTIVATE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 1
KLF_NOTELLSHELL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 128
KLF_REPLACELANG: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 16
KLF_SUBSTITUTE_OK: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS = 2
EXTENDED_BIT: UInt32 = 16777216
DONTCARE_BIT: UInt32 = 33554432
FAKE_KEYSTROKE: UInt32 = 33554432
KBDBASE: UInt32 = 0
KBDSHIFT: UInt32 = 1
KBDCTRL: UInt32 = 2
KBDALT: UInt32 = 4
KBDKANA: UInt32 = 8
KBDROYA: UInt32 = 16
KBDLOYA: UInt32 = 32
KBDGRPSELTAP: UInt32 = 128
GRAVE: UInt32 = 768
ACUTE: UInt32 = 769
CIRCUMFLEX: UInt32 = 770
TILDE: UInt32 = 771
MACRON: UInt32 = 772
OVERSCORE: UInt32 = 773
BREVE: UInt32 = 774
DOT_ABOVE: UInt32 = 775
UMLAUT: UInt32 = 776
DIARESIS: UInt32 = 776
HOOK_ABOVE: UInt32 = 777
RING: UInt32 = 778
DOUBLE_ACUTE: UInt32 = 779
HACEK: UInt32 = 780
CEDILLA: UInt32 = 807
OGONEK: UInt32 = 808
TONOS: UInt32 = 900
DIARESIS_TONOS: UInt32 = 901
wszGRAVE: String = '\u0300'
wszACUTE: String = '\u0301'
wszCIRCUMFLEX: String = '\u0302'
wszTILDE: String = '\u0303'
wszMACRON: String = '\u0304'
wszOVERSCORE: String = '\u0305'
wszBREVE: String = '\u0306'
wszDOT_ABOVE: String = '\u0307'
wszUMLAUT: String = '\u0308'
wszHOOK_ABOVE: String = '\u0309'
wszRING: String = '\u030a'
wszDOUBLE_ACUTE: String = '\u030b'
wszHACEK: String = '\u030c'
wszCEDILLA: String = '\u0327'
wszOGONEK: String = '\u0328'
wszTONOS: String = '\u0384'
wszDIARESIS_TONOS: String = '\u0385'
SHFT_INVALID: UInt32 = 15
WCH_NONE: UInt32 = 61440
WCH_DEAD: UInt32 = 61441
WCH_LGTR: UInt32 = 61442
CAPLOK: UInt32 = 1
SGCAPS: UInt32 = 2
CAPLOKALTGR: UInt32 = 4
KANALOK: UInt32 = 8
GRPSELTAP: UInt32 = 128
DKF_DEAD: UInt32 = 1
KBD_VERSION: UInt32 = 1
KLLF_ALTGR: UInt32 = 1
KLLF_SHIFTLOCK: UInt32 = 2
KLLF_LRM_RLM: UInt32 = 4
KLLF_GLOBAL_ATTRS: UInt32 = 2
KBDTABLE_MULTI_MAX: UInt32 = 8
KEYBOARD_TYPE_GENERIC_101: UInt32 = 4
KEYBOARD_TYPE_JAPAN: UInt32 = 7
KEYBOARD_TYPE_KOREA: UInt32 = 8
KEYBOARD_TYPE_UNKNOWN: UInt32 = 81
NLSKBD_OEM_MICROSOFT: UInt32 = 0
NLSKBD_OEM_AX: UInt32 = 1
NLSKBD_OEM_EPSON: UInt32 = 4
NLSKBD_OEM_FUJITSU: UInt32 = 5
NLSKBD_OEM_IBM: UInt32 = 7
NLSKBD_OEM_MATSUSHITA: UInt32 = 10
NLSKBD_OEM_NEC: UInt32 = 13
NLSKBD_OEM_TOSHIBA: UInt32 = 18
NLSKBD_OEM_DEC: UInt32 = 24
MICROSOFT_KBD_101_TYPE: UInt32 = 0
MICROSOFT_KBD_AX_TYPE: UInt32 = 1
MICROSOFT_KBD_106_TYPE: UInt32 = 2
MICROSOFT_KBD_002_TYPE: UInt32 = 3
MICROSOFT_KBD_001_TYPE: UInt32 = 4
MICROSOFT_KBD_FUNC: UInt32 = 12
AX_KBD_DESKTOP_TYPE: UInt32 = 1
FMR_KBD_JIS_TYPE: UInt32 = 0
FMR_KBD_OASYS_TYPE: UInt32 = 1
FMV_KBD_OASYS_TYPE: UInt32 = 2
NEC_KBD_NORMAL_TYPE: UInt32 = 1
NEC_KBD_N_MODE_TYPE: UInt32 = 2
NEC_KBD_H_MODE_TYPE: UInt32 = 3
NEC_KBD_LAPTOP_TYPE: UInt32 = 4
NEC_KBD_106_TYPE: UInt32 = 5
TOSHIBA_KBD_DESKTOP_TYPE: UInt32 = 13
TOSHIBA_KBD_LAPTOP_TYPE: UInt32 = 15
DEC_KBD_ANSI_LAYOUT_TYPE: UInt32 = 1
DEC_KBD_JIS_LAYOUT_TYPE: UInt32 = 2
MICROSOFT_KBD_101A_TYPE: UInt32 = 0
MICROSOFT_KBD_101B_TYPE: UInt32 = 4
MICROSOFT_KBD_101C_TYPE: UInt32 = 5
MICROSOFT_KBD_103_TYPE: UInt32 = 6
NLSKBD_INFO_SEND_IME_NOTIFICATION: UInt32 = 1
NLSKBD_INFO_ACCESSIBILITY_KEYMAP: UInt32 = 2
NLSKBD_INFO_EMURATE_101_KEYBOARD: UInt32 = 16
NLSKBD_INFO_EMURATE_106_KEYBOARD: UInt32 = 32
KBDNLS_TYPE_NULL: UInt32 = 0
KBDNLS_TYPE_NORMAL: UInt32 = 1
KBDNLS_TYPE_TOGGLE: UInt32 = 2
KBDNLS_INDEX_NORMAL: UInt32 = 1
KBDNLS_INDEX_ALT: UInt32 = 2
KBDNLS_NULL: UInt32 = 0
KBDNLS_NOEVENT: UInt32 = 1
KBDNLS_SEND_BASE_VK: UInt32 = 2
KBDNLS_SEND_PARAM_VK: UInt32 = 3
KBDNLS_KANALOCK: UInt32 = 4
KBDNLS_ALPHANUM: UInt32 = 5
KBDNLS_HIRAGANA: UInt32 = 6
KBDNLS_KATAKANA: UInt32 = 7
KBDNLS_SBCSDBCS: UInt32 = 8
KBDNLS_ROMAN: UInt32 = 9
KBDNLS_CODEINPUT: UInt32 = 10
KBDNLS_HELP_OR_END: UInt32 = 11
KBDNLS_HOME_OR_CLEAR: UInt32 = 12
KBDNLS_NUMPAD: UInt32 = 13
KBDNLS_KANAEVENT: UInt32 = 14
KBDNLS_CONV_OR_NONCONV: UInt32 = 15
KBD_TYPE: UInt32 = 4
SCANCODE_LSHIFT: UInt32 = 42
SCANCODE_RSHIFT: UInt32 = 54
SCANCODE_CTRL: UInt32 = 29
SCANCODE_ALT: UInt32 = 56
SCANCODE_NUMPAD_FIRST: UInt32 = 71
SCANCODE_NUMPAD_LAST: UInt32 = 82
SCANCODE_LWIN: UInt32 = 91
SCANCODE_RWIN: UInt32 = 92
SCANCODE_THAI_LAYOUT_TOGGLE: UInt32 = 41
@winfunctype('COMCTL32.dll')
def _TrackMouseEvent(lpEventTrack: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def LoadKeyboardLayoutA(pwszKLID: win32more.Windows.Win32.Foundation.PSTR, Flags: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS) -> win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL: ...
@winfunctype('USER32.dll')
def LoadKeyboardLayoutW(pwszKLID: win32more.Windows.Win32.Foundation.PWSTR, Flags: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS) -> win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL: ...
LoadKeyboardLayout = UnicodeAlias('LoadKeyboardLayoutW')
@winfunctype('USER32.dll')
def ActivateKeyboardLayout(hkl: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, Flags: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.ACTIVATE_KEYBOARD_LAYOUT_FLAGS) -> win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL: ...
@winfunctype('USER32.dll')
def ToUnicodeEx(wVirtKey: UInt32, wScanCode: UInt32, lpKeyState: POINTER(Byte), pwszBuff: win32more.Windows.Win32.Foundation.PWSTR, cchBuff: Int32, wFlags: UInt32, dwhkl: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL) -> Int32: ...
@winfunctype('USER32.dll')
def UnloadKeyboardLayout(hkl: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetKeyboardLayoutNameA(pwszKLID: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetKeyboardLayoutNameW(pwszKLID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetKeyboardLayoutName = UnicodeAlias('GetKeyboardLayoutNameW')
@winfunctype('USER32.dll')
def GetKeyboardLayoutList(nBuff: Int32, lpList: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL)) -> Int32: ...
@winfunctype('USER32.dll')
def GetKeyboardLayout(idThread: UInt32) -> win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL: ...
@winfunctype('USER32.dll')
def GetMouseMovePointsEx(cbSize: UInt32, lppt: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSEMOVEPOINT), lpptBuf: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSEMOVEPOINT), nBufPoints: Int32, resolution: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.GET_MOUSE_MOVE_POINTS_EX_RESOLUTION) -> Int32: ...
@winfunctype('USER32.dll')
def TrackMouseEvent(lpEventTrack: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def RegisterHotKey(hWnd: win32more.Windows.Win32.Foundation.HWND, id: Int32, fsModifiers: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HOT_KEY_MODIFIERS, vk: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def UnregisterHotKey(hWnd: win32more.Windows.Win32.Foundation.HWND, id: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SwapMouseButton(fSwap: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetDoubleClickTime() -> UInt32: ...
@winfunctype('USER32.dll')
def SetDoubleClickTime(param0: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetFocus(hWnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def GetActiveWindow() -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def GetFocus() -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def GetKBCodePage() -> UInt32: ...
@winfunctype('USER32.dll')
def GetKeyState(nVirtKey: Int32) -> Int16: ...
@winfunctype('USER32.dll')
def GetAsyncKeyState(vKey: Int32) -> Int16: ...
@winfunctype('USER32.dll')
def GetKeyboardState(lpKeyState: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetKeyboardState(lpKeyState: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetKeyNameTextA(lParam: Int32, lpString: win32more.Windows.Win32.Foundation.PSTR, cchSize: Int32) -> Int32: ...
@winfunctype('USER32.dll')
def GetKeyNameTextW(lParam: Int32, lpString: win32more.Windows.Win32.Foundation.PWSTR, cchSize: Int32) -> Int32: ...
GetKeyNameText = UnicodeAlias('GetKeyNameTextW')
@winfunctype('USER32.dll')
def GetKeyboardType(nTypeFlag: Int32) -> Int32: ...
@winfunctype('USER32.dll')
def ToAscii(uVirtKey: UInt32, uScanCode: UInt32, lpKeyState: POINTER(Byte), lpChar: POINTER(UInt16), uFlags: UInt32) -> Int32: ...
@winfunctype('USER32.dll')
def ToAsciiEx(uVirtKey: UInt32, uScanCode: UInt32, lpKeyState: POINTER(Byte), lpChar: POINTER(UInt16), uFlags: UInt32, dwhkl: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL) -> Int32: ...
@winfunctype('USER32.dll')
def ToUnicode(wVirtKey: UInt32, wScanCode: UInt32, lpKeyState: POINTER(Byte), pwszBuff: win32more.Windows.Win32.Foundation.PWSTR, cchBuff: Int32, wFlags: UInt32) -> Int32: ...
@winfunctype('USER32.dll')
def OemKeyScan(wOemChar: UInt16) -> UInt32: ...
@winfunctype('USER32.dll')
def VkKeyScanA(ch: win32more.Windows.Win32.Foundation.CHAR) -> Int16: ...
@winfunctype('USER32.dll')
def VkKeyScanW(ch: Char) -> Int16: ...
VkKeyScan = UnicodeAlias('VkKeyScanW')
@winfunctype('USER32.dll')
def VkKeyScanExA(ch: win32more.Windows.Win32.Foundation.CHAR, dwhkl: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL) -> Int16: ...
@winfunctype('USER32.dll')
def VkKeyScanExW(ch: Char, dwhkl: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL) -> Int16: ...
VkKeyScanEx = UnicodeAlias('VkKeyScanExW')
@winfunctype('USER32.dll')
def keybd_event(bVk: Byte, bScan: Byte, dwFlags: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.KEYBD_EVENT_FLAGS, dwExtraInfo: UIntPtr) -> Void: ...
@winfunctype('USER32.dll')
def mouse_event(dwFlags: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS, dx: Int32, dy: Int32, dwData: Int32, dwExtraInfo: UIntPtr) -> Void: ...
@winfunctype('USER32.dll')
def SendInput(cInputs: UInt32, pInputs: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.INPUT), cbSize: Int32) -> UInt32: ...
@winfunctype('USER32.dll')
def GetLastInputInfo(plii: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.LASTINPUTINFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def MapVirtualKeyA(uCode: UInt32, uMapType: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MAP_VIRTUAL_KEY_TYPE) -> UInt32: ...
@winfunctype('USER32.dll')
def MapVirtualKeyW(uCode: UInt32, uMapType: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MAP_VIRTUAL_KEY_TYPE) -> UInt32: ...
MapVirtualKey = UnicodeAlias('MapVirtualKeyW')
@winfunctype('USER32.dll')
def MapVirtualKeyExA(uCode: UInt32, uMapType: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MAP_VIRTUAL_KEY_TYPE, dwhkl: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL) -> UInt32: ...
@winfunctype('USER32.dll')
def MapVirtualKeyExW(uCode: UInt32, uMapType: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MAP_VIRTUAL_KEY_TYPE, dwhkl: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL) -> UInt32: ...
MapVirtualKeyEx = UnicodeAlias('MapVirtualKeyExW')
@winfunctype('USER32.dll')
def GetCapture() -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def SetCapture(hWnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def ReleaseCapture() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def EnableWindow(hWnd: win32more.Windows.Win32.Foundation.HWND, bEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IsWindowEnabled(hWnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DragDetect(hwnd: win32more.Windows.Win32.Foundation.HWND, pt: win32more.Windows.Win32.Foundation.POINT) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetActiveWindow(hWnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def BlockInput(fBlockIt: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
class DEADKEY(Structure):
    dwBoth: UInt32
    wchComposed: Char
    uFlags: UInt16
GET_MOUSE_MOVE_POINTS_EX_RESOLUTION = UInt32
GMMP_USE_DISPLAY_POINTS: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.GET_MOUSE_MOVE_POINTS_EX_RESOLUTION = 1
GMMP_USE_HIGH_RESOLUTION_POINTS: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.GET_MOUSE_MOVE_POINTS_EX_RESOLUTION = 2
class HARDWAREINPUT(Structure):
    uMsg: UInt32
    wParamL: UInt16
    wParamH: UInt16
HKL = VoidPtr
HOT_KEY_MODIFIERS = UInt32
MOD_ALT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HOT_KEY_MODIFIERS = 1
MOD_CONTROL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HOT_KEY_MODIFIERS = 2
MOD_NOREPEAT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HOT_KEY_MODIFIERS = 16384
MOD_SHIFT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HOT_KEY_MODIFIERS = 4
MOD_WIN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HOT_KEY_MODIFIERS = 8
class INPUT(Structure):
    type: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.INPUT_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        mi: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSEINPUT
        ki: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.KEYBDINPUT
        hi: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HARDWAREINPUT
INPUT_TYPE = UInt32
INPUT_MOUSE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.INPUT_TYPE = 0
INPUT_KEYBOARD: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.INPUT_TYPE = 1
INPUT_HARDWARE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.INPUT_TYPE = 2
class KBDNLSTABLES(Structure):
    OEMIdentifier: UInt16
    LayoutInformation: UInt16
    NumOfVkToF: UInt32
    pVkToF: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VK_F)
    NumOfMouseVKey: Int32
    pusMouseVKey: POINTER(UInt16)
class KBDTABLES(Structure):
    pCharModifiers: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MODIFIERS)
    pVkToWcharTable: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VK_TO_WCHAR_TABLE)
    pDeadKey: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.DEADKEY)
    pKeyNames: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VSC_LPWSTR)
    pKeyNamesExt: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VSC_LPWSTR)
    pKeyNamesDead: POINTER(POINTER(UInt16))
    pusVSCtoVK: POINTER(UInt16)
    bMaxVSCtoVK: Byte
    pVSCtoVK_E0: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VSC_VK)
    pVSCtoVK_E1: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VSC_VK)
    fLocaleFlags: UInt32
    nLgMax: Byte
    cbLgEntry: Byte
    pLigature: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.LIGATURE1)
    dwType: UInt32
    dwSubType: UInt32
class KBDTABLE_DESC(Structure):
    wszDllName: Char * 32
    dwType: UInt32
    dwSubType: UInt32
class KBDTABLE_MULTI(Structure):
    nTables: UInt32
    aKbdTables: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.KBDTABLE_DESC * 8
class KBD_TYPE_INFO(Structure):
    dwVersion: UInt32
    dwType: UInt32
    dwSubType: UInt32
class KEYBDINPUT(Structure):
    wVk: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY
    wScan: UInt16
    dwFlags: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.KEYBD_EVENT_FLAGS
    time: UInt32
    dwExtraInfo: UIntPtr
KEYBD_EVENT_FLAGS = UInt32
KEYEVENTF_EXTENDEDKEY: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.KEYBD_EVENT_FLAGS = 1
KEYEVENTF_KEYUP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.KEYBD_EVENT_FLAGS = 2
KEYEVENTF_SCANCODE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.KEYBD_EVENT_FLAGS = 8
KEYEVENTF_UNICODE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.KEYBD_EVENT_FLAGS = 4
class LASTINPUTINFO(Structure):
    cbSize: UInt32
    dwTime: UInt32
class LIGATURE1(Structure):
    VirtualKey: Byte
    ModificationNumber: UInt16
    wch: Char * 1
class LIGATURE2(Structure):
    VirtualKey: Byte
    ModificationNumber: UInt16
    wch: Char * 2
class LIGATURE3(Structure):
    VirtualKey: Byte
    ModificationNumber: UInt16
    wch: Char * 3
class LIGATURE4(Structure):
    VirtualKey: Byte
    ModificationNumber: UInt16
    wch: Char * 4
class LIGATURE5(Structure):
    VirtualKey: Byte
    ModificationNumber: UInt16
    wch: Char * 5
MAP_VIRTUAL_KEY_TYPE = UInt32
MAPVK_VK_TO_VSC: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MAP_VIRTUAL_KEY_TYPE = 0
MAPVK_VSC_TO_VK: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MAP_VIRTUAL_KEY_TYPE = 1
MAPVK_VK_TO_CHAR: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MAP_VIRTUAL_KEY_TYPE = 2
MAPVK_VSC_TO_VK_EX: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MAP_VIRTUAL_KEY_TYPE = 3
MAPVK_VK_TO_VSC_EX: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MAP_VIRTUAL_KEY_TYPE = 4
class MODIFIERS(Structure):
    pVkToBit: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VK_TO_BIT)
    wMaxModBits: UInt16
    ModNumber: Byte * 1
class MOUSEINPUT(Structure):
    dx: Int32
    dy: Int32
    mouseData: UInt32
    dwFlags: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS
    time: UInt32
    dwExtraInfo: UIntPtr
class MOUSEMOVEPOINT(Structure):
    x: Int32
    y: Int32
    time: UInt32
    dwExtraInfo: UIntPtr
MOUSE_EVENT_FLAGS = UInt32
MOUSEEVENTF_ABSOLUTE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 32768
MOUSEEVENTF_LEFTDOWN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 2
MOUSEEVENTF_LEFTUP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 4
MOUSEEVENTF_MIDDLEDOWN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 32
MOUSEEVENTF_MIDDLEUP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 64
MOUSEEVENTF_MOVE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 1
MOUSEEVENTF_RIGHTDOWN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 8
MOUSEEVENTF_RIGHTUP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 16
MOUSEEVENTF_WHEEL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 2048
MOUSEEVENTF_XDOWN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 128
MOUSEEVENTF_XUP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 256
MOUSEEVENTF_HWHEEL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 4096
MOUSEEVENTF_MOVE_NOCOALESCE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 8192
MOUSEEVENTF_VIRTUALDESK: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.MOUSE_EVENT_FLAGS = 16384
class TRACKMOUSEEVENT(Structure):
    cbSize: UInt32
    dwFlags: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT_FLAGS
    hwndTrack: win32more.Windows.Win32.Foundation.HWND
    dwHoverTime: UInt32
TRACKMOUSEEVENT_FLAGS = UInt32
TME_CANCEL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT_FLAGS = 2147483648
TME_HOVER: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT_FLAGS = 1
TME_LEAVE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT_FLAGS = 2
TME_NONCLIENT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT_FLAGS = 16
TME_QUERY: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.TRACKMOUSEEVENT_FLAGS = 1073741824
VIRTUAL_KEY = UInt16
VK_0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 48
VK_1: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 49
VK_2: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 50
VK_3: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 51
VK_4: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 52
VK_5: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 53
VK_6: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 54
VK_7: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 55
VK_8: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 56
VK_9: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 57
VK_A: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 65
VK_B: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 66
VK_C: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 67
VK_D: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 68
VK_E: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 69
VK_F_: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 70
VK_G: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 71
VK_H: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 72
VK_I: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 73
VK_J: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 74
VK_K: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 75
VK_L: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 76
VK_M: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 77
VK_N: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 78
VK_O: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 79
VK_P: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 80
VK_Q: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 81
VK_R: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 82
VK_S: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 83
VK_T: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 84
VK_U: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 85
VK_V: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 86
VK_W: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 87
VK_X: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 88
VK_Y: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 89
VK_Z: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 90
VK_ABNT_C1: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 193
VK_ABNT_C2: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 194
VK_DBE_ALPHANUMERIC: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 240
VK_DBE_CODEINPUT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 250
VK_DBE_DBCSCHAR: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 244
VK_DBE_DETERMINESTRING: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 252
VK_DBE_ENTERDLGCONVERSIONMODE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 253
VK_DBE_ENTERIMECONFIGMODE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 248
VK_DBE_ENTERWORDREGISTERMODE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 247
VK_DBE_FLUSHSTRING: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 249
VK_DBE_HIRAGANA: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 242
VK_DBE_KATAKANA: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 241
VK_DBE_NOCODEINPUT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 251
VK_DBE_NOROMAN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 246
VK_DBE_ROMAN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 245
VK_DBE_SBCSCHAR: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 243
VK__none_: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 255
VK_LBUTTON: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 1
VK_RBUTTON: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 2
VK_CANCEL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 3
VK_MBUTTON: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 4
VK_XBUTTON1: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 5
VK_XBUTTON2: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 6
VK_BACK: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 8
VK_TAB: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 9
VK_CLEAR: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 12
VK_RETURN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 13
VK_SHIFT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 16
VK_CONTROL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 17
VK_MENU: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 18
VK_PAUSE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 19
VK_CAPITAL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 20
VK_KANA: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 21
VK_HANGEUL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 21
VK_HANGUL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 21
VK_IME_ON: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 22
VK_JUNJA: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 23
VK_FINAL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 24
VK_HANJA: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 25
VK_KANJI: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 25
VK_IME_OFF: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 26
VK_ESCAPE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 27
VK_CONVERT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 28
VK_NONCONVERT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 29
VK_ACCEPT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 30
VK_MODECHANGE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 31
VK_SPACE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 32
VK_PRIOR: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 33
VK_NEXT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 34
VK_END: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 35
VK_HOME: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 36
VK_LEFT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 37
VK_UP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 38
VK_RIGHT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 39
VK_DOWN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 40
VK_SELECT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 41
VK_PRINT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 42
VK_EXECUTE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 43
VK_SNAPSHOT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 44
VK_INSERT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 45
VK_DELETE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 46
VK_HELP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 47
VK_LWIN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 91
VK_RWIN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 92
VK_APPS: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 93
VK_SLEEP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 95
VK_NUMPAD0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 96
VK_NUMPAD1: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 97
VK_NUMPAD2: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 98
VK_NUMPAD3: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 99
VK_NUMPAD4: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 100
VK_NUMPAD5: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 101
VK_NUMPAD6: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 102
VK_NUMPAD7: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 103
VK_NUMPAD8: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 104
VK_NUMPAD9: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 105
VK_MULTIPLY: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 106
VK_ADD: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 107
VK_SEPARATOR: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 108
VK_SUBTRACT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 109
VK_DECIMAL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 110
VK_DIVIDE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 111
VK_F1: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 112
VK_F2: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 113
VK_F3: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 114
VK_F4: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 115
VK_F5: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 116
VK_F6: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 117
VK_F7: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 118
VK_F8: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 119
VK_F9: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 120
VK_F10: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 121
VK_F11: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 122
VK_F12: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 123
VK_F13: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 124
VK_F14: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 125
VK_F15: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 126
VK_F16: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 127
VK_F17: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 128
VK_F18: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 129
VK_F19: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 130
VK_F20: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 131
VK_F21: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 132
VK_F22: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 133
VK_F23: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 134
VK_F24: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 135
VK_NAVIGATION_VIEW: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 136
VK_NAVIGATION_MENU: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 137
VK_NAVIGATION_UP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 138
VK_NAVIGATION_DOWN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 139
VK_NAVIGATION_LEFT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 140
VK_NAVIGATION_RIGHT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 141
VK_NAVIGATION_ACCEPT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 142
VK_NAVIGATION_CANCEL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 143
VK_NUMLOCK: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 144
VK_SCROLL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 145
VK_OEM_NEC_EQUAL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 146
VK_OEM_FJ_JISHO: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 146
VK_OEM_FJ_MASSHOU: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 147
VK_OEM_FJ_TOUROKU: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 148
VK_OEM_FJ_LOYA: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 149
VK_OEM_FJ_ROYA: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 150
VK_LSHIFT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 160
VK_RSHIFT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 161
VK_LCONTROL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 162
VK_RCONTROL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 163
VK_LMENU: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 164
VK_RMENU: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 165
VK_BROWSER_BACK: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 166
VK_BROWSER_FORWARD: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 167
VK_BROWSER_REFRESH: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 168
VK_BROWSER_STOP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 169
VK_BROWSER_SEARCH: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 170
VK_BROWSER_FAVORITES: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 171
VK_BROWSER_HOME: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 172
VK_VOLUME_MUTE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 173
VK_VOLUME_DOWN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 174
VK_VOLUME_UP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 175
VK_MEDIA_NEXT_TRACK: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 176
VK_MEDIA_PREV_TRACK: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 177
VK_MEDIA_STOP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 178
VK_MEDIA_PLAY_PAUSE: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 179
VK_LAUNCH_MAIL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 180
VK_LAUNCH_MEDIA_SELECT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 181
VK_LAUNCH_APP1: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 182
VK_LAUNCH_APP2: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 183
VK_OEM_1: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 186
VK_OEM_PLUS: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 187
VK_OEM_COMMA: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 188
VK_OEM_MINUS: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 189
VK_OEM_PERIOD: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 190
VK_OEM_2: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 191
VK_OEM_3: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 192
VK_GAMEPAD_A: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 195
VK_GAMEPAD_B: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 196
VK_GAMEPAD_X: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 197
VK_GAMEPAD_Y: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 198
VK_GAMEPAD_RIGHT_SHOULDER: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 199
VK_GAMEPAD_LEFT_SHOULDER: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 200
VK_GAMEPAD_LEFT_TRIGGER: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 201
VK_GAMEPAD_RIGHT_TRIGGER: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 202
VK_GAMEPAD_DPAD_UP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 203
VK_GAMEPAD_DPAD_DOWN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 204
VK_GAMEPAD_DPAD_LEFT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 205
VK_GAMEPAD_DPAD_RIGHT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 206
VK_GAMEPAD_MENU: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 207
VK_GAMEPAD_VIEW: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 208
VK_GAMEPAD_LEFT_THUMBSTICK_BUTTON: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 209
VK_GAMEPAD_RIGHT_THUMBSTICK_BUTTON: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 210
VK_GAMEPAD_LEFT_THUMBSTICK_UP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 211
VK_GAMEPAD_LEFT_THUMBSTICK_DOWN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 212
VK_GAMEPAD_LEFT_THUMBSTICK_RIGHT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 213
VK_GAMEPAD_LEFT_THUMBSTICK_LEFT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 214
VK_GAMEPAD_RIGHT_THUMBSTICK_UP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 215
VK_GAMEPAD_RIGHT_THUMBSTICK_DOWN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 216
VK_GAMEPAD_RIGHT_THUMBSTICK_RIGHT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 217
VK_GAMEPAD_RIGHT_THUMBSTICK_LEFT: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 218
VK_OEM_4: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 219
VK_OEM_5: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 220
VK_OEM_6: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 221
VK_OEM_7: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 222
VK_OEM_8: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 223
VK_OEM_AX: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 225
VK_OEM_102: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 226
VK_ICO_HELP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 227
VK_ICO_00: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 228
VK_PROCESSKEY: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 229
VK_ICO_CLEAR: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 230
VK_PACKET: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 231
VK_OEM_RESET: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 233
VK_OEM_JUMP: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 234
VK_OEM_PA1: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 235
VK_OEM_PA2: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 236
VK_OEM_PA3: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 237
VK_OEM_WSCTRL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 238
VK_OEM_CUSEL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 239
VK_OEM_ATTN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 240
VK_OEM_FINISH: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 241
VK_OEM_COPY: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 242
VK_OEM_AUTO: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 243
VK_OEM_ENLW: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 244
VK_OEM_BACKTAB: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 245
VK_ATTN: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 246
VK_CRSEL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 247
VK_EXSEL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 248
VK_EREOF: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 249
VK_PLAY: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 250
VK_ZOOM: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 251
VK_NONAME: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 252
VK_PA1: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 253
VK_OEM_CLEAR: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VIRTUAL_KEY = 254
class VK_F(Structure):
    Vk: Byte
    NLSFEProcType: Byte
    NLSFEProcCurrent: Byte
    NLSFEProcSwitch: Byte
    NLSFEProc: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VK_FPARAM * 8
    NLSFEProcAlt: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VK_FPARAM * 8
class VK_FPARAM(Structure):
    NLSFEProcIndex: Byte
    NLSFEProcParam: UInt32
class VK_TO_BIT(Structure):
    Vk: Byte
    ModBits: Byte
class VK_TO_WCHARS1(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 1
class VK_TO_WCHARS10(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 10
class VK_TO_WCHARS2(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 2
class VK_TO_WCHARS3(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 3
class VK_TO_WCHARS4(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 4
class VK_TO_WCHARS5(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 5
class VK_TO_WCHARS6(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 6
class VK_TO_WCHARS7(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 7
class VK_TO_WCHARS8(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 8
class VK_TO_WCHARS9(Structure):
    VirtualKey: Byte
    Attributes: Byte
    wch: Char * 9
class VK_TO_WCHAR_TABLE(Structure):
    pVkToWchars: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.VK_TO_WCHARS1)
    nModifications: Byte
    cbSize: Byte
class VK_VSC(Structure):
    Vk: Byte
    Vsc: Byte
class VSC_LPWSTR(Structure):
    vsc: Byte
    pwsz: win32more.Windows.Win32.Foundation.PWSTR
class VSC_VK(Structure):
    Vsc: Byte
    Vk: UInt16


make_ready(__name__)
