from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.System.Console

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
CONSOLE_TEXTMODE_BUFFER = 1
ATTACH_PARENT_PROCESS = 4294967295
CTRL_C_EVENT = 0
CTRL_BREAK_EVENT = 1
CTRL_CLOSE_EVENT = 2
CTRL_LOGOFF_EVENT = 5
CTRL_SHUTDOWN_EVENT = 6
PSEUDOCONSOLE_INHERIT_CURSOR = 1
FOREGROUND_BLUE = 1
FOREGROUND_GREEN = 2
FOREGROUND_RED = 4
FOREGROUND_INTENSITY = 8
BACKGROUND_BLUE = 16
BACKGROUND_GREEN = 32
BACKGROUND_RED = 64
BACKGROUND_INTENSITY = 128
COMMON_LVB_LEADING_BYTE = 256
COMMON_LVB_TRAILING_BYTE = 512
COMMON_LVB_GRID_HORIZONTAL = 1024
COMMON_LVB_GRID_LVERTICAL = 2048
COMMON_LVB_GRID_RVERTICAL = 4096
COMMON_LVB_REVERSE_VIDEO = 16384
COMMON_LVB_UNDERSCORE = 32768
COMMON_LVB_SBCSDBCS = 768
CONSOLE_NO_SELECTION = 0
CONSOLE_SELECTION_IN_PROGRESS = 1
CONSOLE_SELECTION_NOT_EMPTY = 2
CONSOLE_MOUSE_SELECTION = 4
CONSOLE_MOUSE_DOWN = 8
HISTORY_NO_DUP_FLAG = 1
CONSOLE_FULLSCREEN = 1
CONSOLE_FULLSCREEN_HARDWARE = 2
CONSOLE_FULLSCREEN_MODE = 1
CONSOLE_WINDOWED_MODE = 2
RIGHT_ALT_PRESSED = 1
LEFT_ALT_PRESSED = 2
RIGHT_CTRL_PRESSED = 4
LEFT_CTRL_PRESSED = 8
SHIFT_PRESSED = 16
NUMLOCK_ON = 32
SCROLLLOCK_ON = 64
CAPSLOCK_ON = 128
ENHANCED_KEY = 256
NLS_DBCSCHAR = 65536
NLS_ALPHANUMERIC = 0
NLS_KATAKANA = 131072
NLS_HIRAGANA = 262144
NLS_ROMAN = 4194304
NLS_IME_CONVERSION = 8388608
ALTNUMPAD_BIT = 67108864
NLS_IME_DISABLE = 536870912
FROM_LEFT_1ST_BUTTON_PRESSED = 1
RIGHTMOST_BUTTON_PRESSED = 2
FROM_LEFT_2ND_BUTTON_PRESSED = 4
FROM_LEFT_3RD_BUTTON_PRESSED = 8
FROM_LEFT_4TH_BUTTON_PRESSED = 16
MOUSE_MOVED = 1
DOUBLE_CLICK = 2
MOUSE_WHEELED = 4
MOUSE_HWHEELED = 8
KEY_EVENT = 1
MOUSE_EVENT = 2
WINDOW_BUFFER_SIZE_EVENT = 4
MENU_EVENT = 8
FOCUS_EVENT = 16
CONSOLE_MODE = UInt32
ENABLE_PROCESSED_INPUT = 1
ENABLE_LINE_INPUT = 2
ENABLE_ECHO_INPUT = 4
ENABLE_WINDOW_INPUT = 8
ENABLE_MOUSE_INPUT = 16
ENABLE_INSERT_MODE = 32
ENABLE_QUICK_EDIT_MODE = 64
ENABLE_EXTENDED_FLAGS = 128
ENABLE_AUTO_POSITION = 256
ENABLE_VIRTUAL_TERMINAL_INPUT = 512
ENABLE_PROCESSED_OUTPUT = 1
ENABLE_WRAP_AT_EOL_OUTPUT = 2
ENABLE_VIRTUAL_TERMINAL_PROCESSING = 4
DISABLE_NEWLINE_AUTO_RETURN = 8
ENABLE_LVB_GRID_WORLDWIDE = 16
STD_HANDLE = UInt32
STD_INPUT_HANDLE = 4294967286
STD_OUTPUT_HANDLE = 4294967285
STD_ERROR_HANDLE = 4294967284
HPCON = IntPtr
def _define_COORD_head():
    class COORD(Structure):
        pass
    return COORD
def _define_COORD():
    COORD = win32more.System.Console.COORD_head
    COORD._fields_ = [
        ("X", Int16),
        ("Y", Int16),
    ]
    return COORD
def _define_SMALL_RECT_head():
    class SMALL_RECT(Structure):
        pass
    return SMALL_RECT
def _define_SMALL_RECT():
    SMALL_RECT = win32more.System.Console.SMALL_RECT_head
    SMALL_RECT._fields_ = [
        ("Left", Int16),
        ("Top", Int16),
        ("Right", Int16),
        ("Bottom", Int16),
    ]
    return SMALL_RECT
def _define_KEY_EVENT_RECORD_head():
    class KEY_EVENT_RECORD(Structure):
        pass
    return KEY_EVENT_RECORD
def _define_KEY_EVENT_RECORD():
    KEY_EVENT_RECORD = win32more.System.Console.KEY_EVENT_RECORD_head
    class KEY_EVENT_RECORD__uChar_e__Union(Union):
        pass
    KEY_EVENT_RECORD__uChar_e__Union._fields_ = [
        ("UnicodeChar", Char),
        ("AsciiChar", win32more.Foundation.CHAR),
    ]
    KEY_EVENT_RECORD._fields_ = [
        ("bKeyDown", win32more.Foundation.BOOL),
        ("wRepeatCount", UInt16),
        ("wVirtualKeyCode", UInt16),
        ("wVirtualScanCode", UInt16),
        ("uChar", KEY_EVENT_RECORD__uChar_e__Union),
        ("dwControlKeyState", UInt32),
    ]
    return KEY_EVENT_RECORD
def _define_MOUSE_EVENT_RECORD_head():
    class MOUSE_EVENT_RECORD(Structure):
        pass
    return MOUSE_EVENT_RECORD
def _define_MOUSE_EVENT_RECORD():
    MOUSE_EVENT_RECORD = win32more.System.Console.MOUSE_EVENT_RECORD_head
    MOUSE_EVENT_RECORD._fields_ = [
        ("dwMousePosition", win32more.System.Console.COORD),
        ("dwButtonState", UInt32),
        ("dwControlKeyState", UInt32),
        ("dwEventFlags", UInt32),
    ]
    return MOUSE_EVENT_RECORD
def _define_WINDOW_BUFFER_SIZE_RECORD_head():
    class WINDOW_BUFFER_SIZE_RECORD(Structure):
        pass
    return WINDOW_BUFFER_SIZE_RECORD
def _define_WINDOW_BUFFER_SIZE_RECORD():
    WINDOW_BUFFER_SIZE_RECORD = win32more.System.Console.WINDOW_BUFFER_SIZE_RECORD_head
    WINDOW_BUFFER_SIZE_RECORD._fields_ = [
        ("dwSize", win32more.System.Console.COORD),
    ]
    return WINDOW_BUFFER_SIZE_RECORD
def _define_MENU_EVENT_RECORD_head():
    class MENU_EVENT_RECORD(Structure):
        pass
    return MENU_EVENT_RECORD
def _define_MENU_EVENT_RECORD():
    MENU_EVENT_RECORD = win32more.System.Console.MENU_EVENT_RECORD_head
    MENU_EVENT_RECORD._fields_ = [
        ("dwCommandId", UInt32),
    ]
    return MENU_EVENT_RECORD
def _define_FOCUS_EVENT_RECORD_head():
    class FOCUS_EVENT_RECORD(Structure):
        pass
    return FOCUS_EVENT_RECORD
def _define_FOCUS_EVENT_RECORD():
    FOCUS_EVENT_RECORD = win32more.System.Console.FOCUS_EVENT_RECORD_head
    FOCUS_EVENT_RECORD._fields_ = [
        ("bSetFocus", win32more.Foundation.BOOL),
    ]
    return FOCUS_EVENT_RECORD
def _define_INPUT_RECORD_head():
    class INPUT_RECORD(Structure):
        pass
    return INPUT_RECORD
def _define_INPUT_RECORD():
    INPUT_RECORD = win32more.System.Console.INPUT_RECORD_head
    class INPUT_RECORD__Event_e__Union(Union):
        pass
    INPUT_RECORD__Event_e__Union._fields_ = [
        ("KeyEvent", win32more.System.Console.KEY_EVENT_RECORD),
        ("MouseEvent", win32more.System.Console.MOUSE_EVENT_RECORD),
        ("WindowBufferSizeEvent", win32more.System.Console.WINDOW_BUFFER_SIZE_RECORD),
        ("MenuEvent", win32more.System.Console.MENU_EVENT_RECORD),
        ("FocusEvent", win32more.System.Console.FOCUS_EVENT_RECORD),
    ]
    INPUT_RECORD._fields_ = [
        ("EventType", UInt16),
        ("Event", INPUT_RECORD__Event_e__Union),
    ]
    return INPUT_RECORD
def _define_CHAR_INFO_head():
    class CHAR_INFO(Structure):
        pass
    return CHAR_INFO
def _define_CHAR_INFO():
    CHAR_INFO = win32more.System.Console.CHAR_INFO_head
    class CHAR_INFO__Char_e__Union(Union):
        pass
    CHAR_INFO__Char_e__Union._fields_ = [
        ("UnicodeChar", Char),
        ("AsciiChar", win32more.Foundation.CHAR),
    ]
    CHAR_INFO._fields_ = [
        ("Char", CHAR_INFO__Char_e__Union),
        ("Attributes", UInt16),
    ]
    return CHAR_INFO
def _define_CONSOLE_FONT_INFO_head():
    class CONSOLE_FONT_INFO(Structure):
        pass
    return CONSOLE_FONT_INFO
def _define_CONSOLE_FONT_INFO():
    CONSOLE_FONT_INFO = win32more.System.Console.CONSOLE_FONT_INFO_head
    CONSOLE_FONT_INFO._fields_ = [
        ("nFont", UInt32),
        ("dwFontSize", win32more.System.Console.COORD),
    ]
    return CONSOLE_FONT_INFO
def _define_CONSOLE_READCONSOLE_CONTROL_head():
    class CONSOLE_READCONSOLE_CONTROL(Structure):
        pass
    return CONSOLE_READCONSOLE_CONTROL
def _define_CONSOLE_READCONSOLE_CONTROL():
    CONSOLE_READCONSOLE_CONTROL = win32more.System.Console.CONSOLE_READCONSOLE_CONTROL_head
    CONSOLE_READCONSOLE_CONTROL._fields_ = [
        ("nLength", UInt32),
        ("nInitialChars", UInt32),
        ("dwCtrlWakeupMask", UInt32),
        ("dwControlKeyState", UInt32),
    ]
    return CONSOLE_READCONSOLE_CONTROL
def _define_PHANDLER_ROUTINE():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=False)
def _define_CONSOLE_CURSOR_INFO_head():
    class CONSOLE_CURSOR_INFO(Structure):
        pass
    return CONSOLE_CURSOR_INFO
def _define_CONSOLE_CURSOR_INFO():
    CONSOLE_CURSOR_INFO = win32more.System.Console.CONSOLE_CURSOR_INFO_head
    CONSOLE_CURSOR_INFO._fields_ = [
        ("dwSize", UInt32),
        ("bVisible", win32more.Foundation.BOOL),
    ]
    return CONSOLE_CURSOR_INFO
def _define_CONSOLE_SCREEN_BUFFER_INFO_head():
    class CONSOLE_SCREEN_BUFFER_INFO(Structure):
        pass
    return CONSOLE_SCREEN_BUFFER_INFO
def _define_CONSOLE_SCREEN_BUFFER_INFO():
    CONSOLE_SCREEN_BUFFER_INFO = win32more.System.Console.CONSOLE_SCREEN_BUFFER_INFO_head
    CONSOLE_SCREEN_BUFFER_INFO._fields_ = [
        ("dwSize", win32more.System.Console.COORD),
        ("dwCursorPosition", win32more.System.Console.COORD),
        ("wAttributes", UInt16),
        ("srWindow", win32more.System.Console.SMALL_RECT),
        ("dwMaximumWindowSize", win32more.System.Console.COORD),
    ]
    return CONSOLE_SCREEN_BUFFER_INFO
def _define_CONSOLE_SCREEN_BUFFER_INFOEX_head():
    class CONSOLE_SCREEN_BUFFER_INFOEX(Structure):
        pass
    return CONSOLE_SCREEN_BUFFER_INFOEX
def _define_CONSOLE_SCREEN_BUFFER_INFOEX():
    CONSOLE_SCREEN_BUFFER_INFOEX = win32more.System.Console.CONSOLE_SCREEN_BUFFER_INFOEX_head
    CONSOLE_SCREEN_BUFFER_INFOEX._fields_ = [
        ("cbSize", UInt32),
        ("dwSize", win32more.System.Console.COORD),
        ("dwCursorPosition", win32more.System.Console.COORD),
        ("wAttributes", UInt16),
        ("srWindow", win32more.System.Console.SMALL_RECT),
        ("dwMaximumWindowSize", win32more.System.Console.COORD),
        ("wPopupAttributes", UInt16),
        ("bFullscreenSupported", win32more.Foundation.BOOL),
        ("ColorTable", UInt32 * 16),
    ]
    return CONSOLE_SCREEN_BUFFER_INFOEX
def _define_CONSOLE_FONT_INFOEX_head():
    class CONSOLE_FONT_INFOEX(Structure):
        pass
    return CONSOLE_FONT_INFOEX
def _define_CONSOLE_FONT_INFOEX():
    CONSOLE_FONT_INFOEX = win32more.System.Console.CONSOLE_FONT_INFOEX_head
    CONSOLE_FONT_INFOEX._fields_ = [
        ("cbSize", UInt32),
        ("nFont", UInt32),
        ("dwFontSize", win32more.System.Console.COORD),
        ("FontFamily", UInt32),
        ("FontWeight", UInt32),
        ("FaceName", Char * 32),
    ]
    return CONSOLE_FONT_INFOEX
def _define_CONSOLE_SELECTION_INFO_head():
    class CONSOLE_SELECTION_INFO(Structure):
        pass
    return CONSOLE_SELECTION_INFO
def _define_CONSOLE_SELECTION_INFO():
    CONSOLE_SELECTION_INFO = win32more.System.Console.CONSOLE_SELECTION_INFO_head
    CONSOLE_SELECTION_INFO._fields_ = [
        ("dwFlags", UInt32),
        ("dwSelectionAnchor", win32more.System.Console.COORD),
        ("srSelection", win32more.System.Console.SMALL_RECT),
    ]
    return CONSOLE_SELECTION_INFO
def _define_CONSOLE_HISTORY_INFO_head():
    class CONSOLE_HISTORY_INFO(Structure):
        pass
    return CONSOLE_HISTORY_INFO
def _define_CONSOLE_HISTORY_INFO():
    CONSOLE_HISTORY_INFO = win32more.System.Console.CONSOLE_HISTORY_INFO_head
    CONSOLE_HISTORY_INFO._fields_ = [
        ("cbSize", UInt32),
        ("HistoryBufferSize", UInt32),
        ("NumberOfHistoryBuffers", UInt32),
        ("dwFlags", UInt32),
    ]
    return CONSOLE_HISTORY_INFO
def _define_AllocConsole():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(("AllocConsole", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeConsole():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(("FreeConsole", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_AttachConsole():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=False)(("AttachConsole", windll["KERNEL32"]), ((1, 'dwProcessId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleCP():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("GetConsoleCP", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleOutputCP():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("GetConsoleOutputCP", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.CONSOLE_MODE), use_last_error=False)(("GetConsoleMode", windll["KERNEL32"]), ((1, 'hConsoleHandle'),(1, 'lpMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Console.CONSOLE_MODE, use_last_error=False)(("SetConsoleMode", windll["KERNEL32"]), ((1, 'hConsoleHandle'),(1, 'dwMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumberOfConsoleInputEvents():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32), use_last_error=False)(("GetNumberOfConsoleInputEvents", windll["KERNEL32"]), ((1, 'hConsoleInput'),(1, 'lpNumberOfEvents'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadConsoleInputA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.INPUT_RECORD),UInt32,POINTER(UInt32), use_last_error=False)(("ReadConsoleInputA", windll["KERNEL32"]), ((1, 'hConsoleInput'),(1, 'lpBuffer'),(1, 'nLength'),(1, 'lpNumberOfEventsRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadConsoleInputW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.INPUT_RECORD),UInt32,POINTER(UInt32), use_last_error=False)(("ReadConsoleInputW", windll["KERNEL32"]), ((1, 'hConsoleInput'),(1, 'lpBuffer'),(1, 'nLength'),(1, 'lpNumberOfEventsRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadConsoleInput():
    return win32more.System.Console.ReadConsoleInputW
def _define_PeekConsoleInputA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.INPUT_RECORD),UInt32,POINTER(UInt32), use_last_error=False)(("PeekConsoleInputA", windll["KERNEL32"]), ((1, 'hConsoleInput'),(1, 'lpBuffer'),(1, 'nLength'),(1, 'lpNumberOfEventsRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeekConsoleInputW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.INPUT_RECORD),UInt32,POINTER(UInt32), use_last_error=False)(("PeekConsoleInputW", windll["KERNEL32"]), ((1, 'hConsoleInput'),(1, 'lpBuffer'),(1, 'nLength'),(1, 'lpNumberOfEventsRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PeekConsoleInput():
    return win32more.System.Console.PeekConsoleInputW
def _define_ReadConsoleA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.System.Console.CONSOLE_READCONSOLE_CONTROL_head), use_last_error=False)(("ReadConsoleA", windll["KERNEL32"]), ((1, 'hConsoleInput'),(1, 'lpBuffer'),(1, 'nNumberOfCharsToRead'),(1, 'lpNumberOfCharsRead'),(1, 'pInputControl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadConsoleW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.System.Console.CONSOLE_READCONSOLE_CONTROL_head), use_last_error=False)(("ReadConsoleW", windll["KERNEL32"]), ((1, 'hConsoleInput'),(1, 'lpBuffer'),(1, 'nNumberOfCharsToRead'),(1, 'lpNumberOfCharsRead'),(1, 'pInputControl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadConsole():
    return win32more.System.Console.ReadConsoleW
def _define_WriteConsoleA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(Void),UInt32,POINTER(UInt32),c_void_p, use_last_error=False)(("WriteConsoleA", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpBuffer'),(1, 'nNumberOfCharsToWrite'),(1, 'lpNumberOfCharsWritten'),(1, 'lpReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteConsoleW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(Void),UInt32,POINTER(UInt32),c_void_p, use_last_error=False)(("WriteConsoleW", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpBuffer'),(1, 'nNumberOfCharsToWrite'),(1, 'lpNumberOfCharsWritten'),(1, 'lpReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteConsole():
    return win32more.System.Console.WriteConsoleW
def _define_SetConsoleCtrlHandler():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Console.PHANDLER_ROUTINE,win32more.Foundation.BOOL, use_last_error=False)(("SetConsoleCtrlHandler", windll["KERNEL32"]), ((1, 'HandlerRoutine'),(1, 'Add'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePseudoConsole():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Console.COORD,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.System.Console.HPCON), use_last_error=False)(("CreatePseudoConsole", windll["KERNEL32"]), ((1, 'size'),(1, 'hInput'),(1, 'hOutput'),(1, 'dwFlags'),(1, 'phPC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResizePseudoConsole():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Console.HPCON,win32more.System.Console.COORD, use_last_error=False)(("ResizePseudoConsole", windll["KERNEL32"]), ((1, 'hPC'),(1, 'size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ClosePseudoConsole():
    try:
        return WINFUNCTYPE(Void,win32more.System.Console.HPCON, use_last_error=False)(("ClosePseudoConsole", windll["KERNEL32"]), ((1, 'hPC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FillConsoleOutputCharacterA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.CHAR,UInt32,win32more.System.Console.COORD,POINTER(UInt32), use_last_error=False)(("FillConsoleOutputCharacterA", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'cCharacter'),(1, 'nLength'),(1, 'dwWriteCoord'),(1, 'lpNumberOfCharsWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FillConsoleOutputCharacterW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,Char,UInt32,win32more.System.Console.COORD,POINTER(UInt32), use_last_error=False)(("FillConsoleOutputCharacterW", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'cCharacter'),(1, 'nLength'),(1, 'dwWriteCoord'),(1, 'lpNumberOfCharsWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FillConsoleOutputCharacter():
    return win32more.System.Console.FillConsoleOutputCharacterW
def _define_FillConsoleOutputAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt16,UInt32,win32more.System.Console.COORD,POINTER(UInt32), use_last_error=False)(("FillConsoleOutputAttribute", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'wAttribute'),(1, 'nLength'),(1, 'dwWriteCoord'),(1, 'lpNumberOfAttrsWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GenerateConsoleCtrlEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32, use_last_error=False)(("GenerateConsoleCtrlEvent", windll["KERNEL32"]), ((1, 'dwCtrlEvent'),(1, 'dwProcessGroupId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateConsoleScreenBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,c_void_p, use_last_error=False)(("CreateConsoleScreenBuffer", windll["KERNEL32"]), ((1, 'dwDesiredAccess'),(1, 'dwShareMode'),(1, 'lpSecurityAttributes'),(1, 'dwFlags'),(1, 'lpScreenBufferData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleActiveScreenBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=False)(("SetConsoleActiveScreenBuffer", windll["KERNEL32"]), ((1, 'hConsoleOutput'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlushConsoleInputBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=False)(("FlushConsoleInputBuffer", windll["KERNEL32"]), ((1, 'hConsoleInput'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleCP():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=False)(("SetConsoleCP", windll["KERNEL32"]), ((1, 'wCodePageID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleOutputCP():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=False)(("SetConsoleOutputCP", windll["KERNEL32"]), ((1, 'wCodePageID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleCursorInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.CONSOLE_CURSOR_INFO_head), use_last_error=False)(("GetConsoleCursorInfo", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpConsoleCursorInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleCursorInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.CONSOLE_CURSOR_INFO_head), use_last_error=False)(("SetConsoleCursorInfo", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpConsoleCursorInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleScreenBufferInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.CONSOLE_SCREEN_BUFFER_INFO_head), use_last_error=False)(("GetConsoleScreenBufferInfo", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpConsoleScreenBufferInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleScreenBufferInfoEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.CONSOLE_SCREEN_BUFFER_INFOEX_head), use_last_error=False)(("GetConsoleScreenBufferInfoEx", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpConsoleScreenBufferInfoEx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleScreenBufferInfoEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.CONSOLE_SCREEN_BUFFER_INFOEX_head), use_last_error=False)(("SetConsoleScreenBufferInfoEx", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpConsoleScreenBufferInfoEx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleScreenBufferSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Console.COORD, use_last_error=False)(("SetConsoleScreenBufferSize", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'dwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleCursorPosition():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Console.COORD, use_last_error=False)(("SetConsoleCursorPosition", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'dwCursorPosition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLargestConsoleWindowSize():
    try:
        return WINFUNCTYPE(win32more.System.Console.COORD,win32more.Foundation.HANDLE, use_last_error=False)(("GetLargestConsoleWindowSize", windll["KERNEL32"]), ((1, 'hConsoleOutput'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleTextAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt16, use_last_error=False)(("SetConsoleTextAttribute", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'wAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleWindowInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.BOOL,POINTER(win32more.System.Console.SMALL_RECT_head), use_last_error=False)(("SetConsoleWindowInfo", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'bAbsolute'),(1, 'lpConsoleWindow'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteConsoleOutputCharacterA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(Byte),UInt32,win32more.System.Console.COORD,POINTER(UInt32), use_last_error=False)(("WriteConsoleOutputCharacterA", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpCharacter'),(1, 'nLength'),(1, 'dwWriteCoord'),(1, 'lpNumberOfCharsWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteConsoleOutputCharacterW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(Char),UInt32,win32more.System.Console.COORD,POINTER(UInt32), use_last_error=False)(("WriteConsoleOutputCharacterW", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpCharacter'),(1, 'nLength'),(1, 'dwWriteCoord'),(1, 'lpNumberOfCharsWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteConsoleOutputCharacter():
    return win32more.System.Console.WriteConsoleOutputCharacterW
def _define_WriteConsoleOutputAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt16),UInt32,win32more.System.Console.COORD,POINTER(UInt32), use_last_error=False)(("WriteConsoleOutputAttribute", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpAttribute'),(1, 'nLength'),(1, 'dwWriteCoord'),(1, 'lpNumberOfAttrsWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadConsoleOutputCharacterA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(Byte),UInt32,win32more.System.Console.COORD,POINTER(UInt32), use_last_error=False)(("ReadConsoleOutputCharacterA", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpCharacter'),(1, 'nLength'),(1, 'dwReadCoord'),(1, 'lpNumberOfCharsRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadConsoleOutputCharacterW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(Char),UInt32,win32more.System.Console.COORD,POINTER(UInt32), use_last_error=False)(("ReadConsoleOutputCharacterW", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpCharacter'),(1, 'nLength'),(1, 'dwReadCoord'),(1, 'lpNumberOfCharsRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadConsoleOutputCharacter():
    return win32more.System.Console.ReadConsoleOutputCharacterW
def _define_ReadConsoleOutputAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt16),UInt32,win32more.System.Console.COORD,POINTER(UInt32), use_last_error=False)(("ReadConsoleOutputAttribute", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpAttribute'),(1, 'nLength'),(1, 'dwReadCoord'),(1, 'lpNumberOfAttrsRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteConsoleInputA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.INPUT_RECORD),UInt32,POINTER(UInt32), use_last_error=False)(("WriteConsoleInputA", windll["KERNEL32"]), ((1, 'hConsoleInput'),(1, 'lpBuffer'),(1, 'nLength'),(1, 'lpNumberOfEventsWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteConsoleInputW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.INPUT_RECORD),UInt32,POINTER(UInt32), use_last_error=False)(("WriteConsoleInputW", windll["KERNEL32"]), ((1, 'hConsoleInput'),(1, 'lpBuffer'),(1, 'nLength'),(1, 'lpNumberOfEventsWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteConsoleInput():
    return win32more.System.Console.WriteConsoleInputW
def _define_ScrollConsoleScreenBufferA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.SMALL_RECT_head),POINTER(win32more.System.Console.SMALL_RECT_head),win32more.System.Console.COORD,POINTER(win32more.System.Console.CHAR_INFO_head), use_last_error=False)(("ScrollConsoleScreenBufferA", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpScrollRectangle'),(1, 'lpClipRectangle'),(1, 'dwDestinationOrigin'),(1, 'lpFill'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScrollConsoleScreenBufferW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.SMALL_RECT_head),POINTER(win32more.System.Console.SMALL_RECT_head),win32more.System.Console.COORD,POINTER(win32more.System.Console.CHAR_INFO_head), use_last_error=False)(("ScrollConsoleScreenBufferW", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpScrollRectangle'),(1, 'lpClipRectangle'),(1, 'dwDestinationOrigin'),(1, 'lpFill'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScrollConsoleScreenBuffer():
    return win32more.System.Console.ScrollConsoleScreenBufferW
def _define_WriteConsoleOutputA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.CHAR_INFO_head),win32more.System.Console.COORD,win32more.System.Console.COORD,POINTER(win32more.System.Console.SMALL_RECT_head), use_last_error=False)(("WriteConsoleOutputA", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'dwBufferCoord'),(1, 'lpWriteRegion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteConsoleOutputW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.CHAR_INFO_head),win32more.System.Console.COORD,win32more.System.Console.COORD,POINTER(win32more.System.Console.SMALL_RECT_head), use_last_error=False)(("WriteConsoleOutputW", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'dwBufferCoord'),(1, 'lpWriteRegion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteConsoleOutput():
    return win32more.System.Console.WriteConsoleOutputW
def _define_ReadConsoleOutputA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.CHAR_INFO_head),win32more.System.Console.COORD,win32more.System.Console.COORD,POINTER(win32more.System.Console.SMALL_RECT_head), use_last_error=False)(("ReadConsoleOutputA", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'dwBufferCoord'),(1, 'lpReadRegion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadConsoleOutputW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.Console.CHAR_INFO_head),win32more.System.Console.COORD,win32more.System.Console.COORD,POINTER(win32more.System.Console.SMALL_RECT_head), use_last_error=False)(("ReadConsoleOutputW", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'lpBuffer'),(1, 'dwBufferSize'),(1, 'dwBufferCoord'),(1, 'lpReadRegion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadConsoleOutput():
    return win32more.System.Console.ReadConsoleOutputW
def _define_GetConsoleTitleA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Byte),UInt32, use_last_error=False)(("GetConsoleTitleA", windll["KERNEL32"]), ((1, 'lpConsoleTitle'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleTitleW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Char),UInt32, use_last_error=False)(("GetConsoleTitleW", windll["KERNEL32"]), ((1, 'lpConsoleTitle'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleTitle():
    return win32more.System.Console.GetConsoleTitleW
def _define_GetConsoleOriginalTitleA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Byte),UInt32, use_last_error=False)(("GetConsoleOriginalTitleA", windll["KERNEL32"]), ((1, 'lpConsoleTitle'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleOriginalTitleW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Char),UInt32, use_last_error=False)(("GetConsoleOriginalTitleW", windll["KERNEL32"]), ((1, 'lpConsoleTitle'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleOriginalTitle():
    return win32more.System.Console.GetConsoleOriginalTitleW
def _define_SetConsoleTitleA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR, use_last_error=False)(("SetConsoleTitleA", windll["KERNEL32"]), ((1, 'lpConsoleTitle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleTitleW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=False)(("SetConsoleTitleW", windll["KERNEL32"]), ((1, 'lpConsoleTitle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleTitle():
    return win32more.System.Console.SetConsoleTitleW
def _define_GetNumberOfConsoleMouseButtons():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32), use_last_error=False)(("GetNumberOfConsoleMouseButtons", windll["KERNEL32"]), ((1, 'lpNumberOfMouseButtons'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleFontSize():
    try:
        return WINFUNCTYPE(win32more.System.Console.COORD,win32more.Foundation.HANDLE,UInt32, use_last_error=False)(("GetConsoleFontSize", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'nFont'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentConsoleFont():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.BOOL,POINTER(win32more.System.Console.CONSOLE_FONT_INFO_head), use_last_error=False)(("GetCurrentConsoleFont", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'bMaximumWindow'),(1, 'lpConsoleCurrentFont'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentConsoleFontEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.BOOL,POINTER(win32more.System.Console.CONSOLE_FONT_INFOEX_head), use_last_error=False)(("GetCurrentConsoleFontEx", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'bMaximumWindow'),(1, 'lpConsoleCurrentFontEx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetCurrentConsoleFontEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.BOOL,POINTER(win32more.System.Console.CONSOLE_FONT_INFOEX_head), use_last_error=False)(("SetCurrentConsoleFontEx", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'bMaximumWindow'),(1, 'lpConsoleCurrentFontEx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleSelectionInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Console.CONSOLE_SELECTION_INFO_head), use_last_error=False)(("GetConsoleSelectionInfo", windll["KERNEL32"]), ((1, 'lpConsoleSelectionInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleHistoryInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Console.CONSOLE_HISTORY_INFO_head), use_last_error=False)(("GetConsoleHistoryInfo", windll["KERNEL32"]), ((1, 'lpConsoleHistoryInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleHistoryInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Console.CONSOLE_HISTORY_INFO_head), use_last_error=False)(("SetConsoleHistoryInfo", windll["KERNEL32"]), ((1, 'lpConsoleHistoryInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleDisplayMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32), use_last_error=False)(("GetConsoleDisplayMode", windll["KERNEL32"]), ((1, 'lpModeFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleDisplayMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.System.Console.COORD_head), use_last_error=False)(("SetConsoleDisplayMode", windll["KERNEL32"]), ((1, 'hConsoleOutput'),(1, 'dwFlags'),(1, 'lpNewScreenBufferDimensions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND, use_last_error=False)(("GetConsoleWindow", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddConsoleAliasA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("AddConsoleAliasA", windll["KERNEL32"]), ((1, 'Source'),(1, 'Target'),(1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddConsoleAliasW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("AddConsoleAliasW", windll["KERNEL32"]), ((1, 'Source'),(1, 'Target'),(1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddConsoleAlias():
    return win32more.System.Console.AddConsoleAliasW
def _define_GetConsoleAliasA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(Byte),UInt32,win32more.Foundation.PSTR, use_last_error=False)(("GetConsoleAliasA", windll["KERNEL32"]), ((1, 'Source'),(1, 'TargetBuffer'),(1, 'TargetBufferLength'),(1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleAliasW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Char),UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("GetConsoleAliasW", windll["KERNEL32"]), ((1, 'Source'),(1, 'TargetBuffer'),(1, 'TargetBufferLength'),(1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleAlias():
    return win32more.System.Console.GetConsoleAliasW
def _define_GetConsoleAliasesLengthA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("GetConsoleAliasesLengthA", windll["KERNEL32"]), ((1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleAliasesLengthW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("GetConsoleAliasesLengthW", windll["KERNEL32"]), ((1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleAliasesLength():
    return win32more.System.Console.GetConsoleAliasesLengthW
def _define_GetConsoleAliasExesLengthA():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("GetConsoleAliasExesLengthA", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleAliasExesLengthW():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("GetConsoleAliasExesLengthW", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleAliasExesLength():
    return win32more.System.Console.GetConsoleAliasExesLengthW
def _define_GetConsoleAliasesA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Byte),UInt32,win32more.Foundation.PSTR, use_last_error=False)(("GetConsoleAliasesA", windll["KERNEL32"]), ((1, 'AliasBuffer'),(1, 'AliasBufferLength'),(1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleAliasesW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Char),UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("GetConsoleAliasesW", windll["KERNEL32"]), ((1, 'AliasBuffer'),(1, 'AliasBufferLength'),(1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleAliases():
    return win32more.System.Console.GetConsoleAliasesW
def _define_GetConsoleAliasExesA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Byte),UInt32, use_last_error=False)(("GetConsoleAliasExesA", windll["KERNEL32"]), ((1, 'ExeNameBuffer'),(1, 'ExeNameBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleAliasExesW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Char),UInt32, use_last_error=False)(("GetConsoleAliasExesW", windll["KERNEL32"]), ((1, 'ExeNameBuffer'),(1, 'ExeNameBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleAliasExes():
    return win32more.System.Console.GetConsoleAliasExesW
def _define_ExpungeConsoleCommandHistoryA():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.PSTR, use_last_error=False)(("ExpungeConsoleCommandHistoryA", windll["KERNEL32"]), ((1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExpungeConsoleCommandHistoryW():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.PWSTR, use_last_error=False)(("ExpungeConsoleCommandHistoryW", windll["KERNEL32"]), ((1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExpungeConsoleCommandHistory():
    return win32more.System.Console.ExpungeConsoleCommandHistoryW
def _define_SetConsoleNumberOfCommandsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PSTR, use_last_error=False)(("SetConsoleNumberOfCommandsA", windll["KERNEL32"]), ((1, 'Number'),(1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleNumberOfCommandsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("SetConsoleNumberOfCommandsW", windll["KERNEL32"]), ((1, 'Number'),(1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetConsoleNumberOfCommands():
    return win32more.System.Console.SetConsoleNumberOfCommandsW
def _define_GetConsoleCommandHistoryLengthA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR, use_last_error=False)(("GetConsoleCommandHistoryLengthA", windll["KERNEL32"]), ((1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleCommandHistoryLengthW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("GetConsoleCommandHistoryLengthW", windll["KERNEL32"]), ((1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleCommandHistoryLength():
    return win32more.System.Console.GetConsoleCommandHistoryLengthW
def _define_GetConsoleCommandHistoryA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR, use_last_error=False)(("GetConsoleCommandHistoryA", windll["KERNEL32"]), ((1, 'Commands'),(1, 'CommandBufferLength'),(1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleCommandHistoryW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("GetConsoleCommandHistoryW", windll["KERNEL32"]), ((1, 'Commands'),(1, 'CommandBufferLength'),(1, 'ExeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetConsoleCommandHistory():
    return win32more.System.Console.GetConsoleCommandHistoryW
def _define_GetConsoleProcessList():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("GetConsoleProcessList", windll["KERNEL32"]), ((1, 'lpdwProcessList'),(1, 'dwProcessCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStdHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.System.Console.STD_HANDLE, use_last_error=False)(("GetStdHandle", windll["KERNEL32"]), ((1, 'nStdHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetStdHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Console.STD_HANDLE,win32more.Foundation.HANDLE, use_last_error=False)(("SetStdHandle", windll["KERNEL32"]), ((1, 'nStdHandle'),(1, 'hHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetStdHandleEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Console.STD_HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("SetStdHandleEx", windll["KERNEL32"]), ((1, 'nStdHandle'),(1, 'hHandle'),(1, 'phPrevValue'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CONSOLE_TEXTMODE_BUFFER",
    "ATTACH_PARENT_PROCESS",
    "CTRL_C_EVENT",
    "CTRL_BREAK_EVENT",
    "CTRL_CLOSE_EVENT",
    "CTRL_LOGOFF_EVENT",
    "CTRL_SHUTDOWN_EVENT",
    "PSEUDOCONSOLE_INHERIT_CURSOR",
    "FOREGROUND_BLUE",
    "FOREGROUND_GREEN",
    "FOREGROUND_RED",
    "FOREGROUND_INTENSITY",
    "BACKGROUND_BLUE",
    "BACKGROUND_GREEN",
    "BACKGROUND_RED",
    "BACKGROUND_INTENSITY",
    "COMMON_LVB_LEADING_BYTE",
    "COMMON_LVB_TRAILING_BYTE",
    "COMMON_LVB_GRID_HORIZONTAL",
    "COMMON_LVB_GRID_LVERTICAL",
    "COMMON_LVB_GRID_RVERTICAL",
    "COMMON_LVB_REVERSE_VIDEO",
    "COMMON_LVB_UNDERSCORE",
    "COMMON_LVB_SBCSDBCS",
    "CONSOLE_NO_SELECTION",
    "CONSOLE_SELECTION_IN_PROGRESS",
    "CONSOLE_SELECTION_NOT_EMPTY",
    "CONSOLE_MOUSE_SELECTION",
    "CONSOLE_MOUSE_DOWN",
    "HISTORY_NO_DUP_FLAG",
    "CONSOLE_FULLSCREEN",
    "CONSOLE_FULLSCREEN_HARDWARE",
    "CONSOLE_FULLSCREEN_MODE",
    "CONSOLE_WINDOWED_MODE",
    "RIGHT_ALT_PRESSED",
    "LEFT_ALT_PRESSED",
    "RIGHT_CTRL_PRESSED",
    "LEFT_CTRL_PRESSED",
    "SHIFT_PRESSED",
    "NUMLOCK_ON",
    "SCROLLLOCK_ON",
    "CAPSLOCK_ON",
    "ENHANCED_KEY",
    "NLS_DBCSCHAR",
    "NLS_ALPHANUMERIC",
    "NLS_KATAKANA",
    "NLS_HIRAGANA",
    "NLS_ROMAN",
    "NLS_IME_CONVERSION",
    "ALTNUMPAD_BIT",
    "NLS_IME_DISABLE",
    "FROM_LEFT_1ST_BUTTON_PRESSED",
    "RIGHTMOST_BUTTON_PRESSED",
    "FROM_LEFT_2ND_BUTTON_PRESSED",
    "FROM_LEFT_3RD_BUTTON_PRESSED",
    "FROM_LEFT_4TH_BUTTON_PRESSED",
    "MOUSE_MOVED",
    "DOUBLE_CLICK",
    "MOUSE_WHEELED",
    "MOUSE_HWHEELED",
    "KEY_EVENT",
    "MOUSE_EVENT",
    "WINDOW_BUFFER_SIZE_EVENT",
    "MENU_EVENT",
    "FOCUS_EVENT",
    "CONSOLE_MODE",
    "ENABLE_PROCESSED_INPUT",
    "ENABLE_LINE_INPUT",
    "ENABLE_ECHO_INPUT",
    "ENABLE_WINDOW_INPUT",
    "ENABLE_MOUSE_INPUT",
    "ENABLE_INSERT_MODE",
    "ENABLE_QUICK_EDIT_MODE",
    "ENABLE_EXTENDED_FLAGS",
    "ENABLE_AUTO_POSITION",
    "ENABLE_VIRTUAL_TERMINAL_INPUT",
    "ENABLE_PROCESSED_OUTPUT",
    "ENABLE_WRAP_AT_EOL_OUTPUT",
    "ENABLE_VIRTUAL_TERMINAL_PROCESSING",
    "DISABLE_NEWLINE_AUTO_RETURN",
    "ENABLE_LVB_GRID_WORLDWIDE",
    "STD_HANDLE",
    "STD_INPUT_HANDLE",
    "STD_OUTPUT_HANDLE",
    "STD_ERROR_HANDLE",
    "HPCON",
    "COORD",
    "SMALL_RECT",
    "KEY_EVENT_RECORD",
    "MOUSE_EVENT_RECORD",
    "WINDOW_BUFFER_SIZE_RECORD",
    "MENU_EVENT_RECORD",
    "FOCUS_EVENT_RECORD",
    "INPUT_RECORD",
    "CHAR_INFO",
    "CONSOLE_FONT_INFO",
    "CONSOLE_READCONSOLE_CONTROL",
    "PHANDLER_ROUTINE",
    "CONSOLE_CURSOR_INFO",
    "CONSOLE_SCREEN_BUFFER_INFO",
    "CONSOLE_SCREEN_BUFFER_INFOEX",
    "CONSOLE_FONT_INFOEX",
    "CONSOLE_SELECTION_INFO",
    "CONSOLE_HISTORY_INFO",
    "AllocConsole",
    "FreeConsole",
    "AttachConsole",
    "GetConsoleCP",
    "GetConsoleOutputCP",
    "GetConsoleMode",
    "SetConsoleMode",
    "GetNumberOfConsoleInputEvents",
    "ReadConsoleInputA",
    "ReadConsoleInputW",
    "ReadConsoleInput",
    "PeekConsoleInputA",
    "PeekConsoleInputW",
    "PeekConsoleInput",
    "ReadConsoleA",
    "ReadConsoleW",
    "ReadConsole",
    "WriteConsoleA",
    "WriteConsoleW",
    "WriteConsole",
    "SetConsoleCtrlHandler",
    "CreatePseudoConsole",
    "ResizePseudoConsole",
    "ClosePseudoConsole",
    "FillConsoleOutputCharacterA",
    "FillConsoleOutputCharacterW",
    "FillConsoleOutputCharacter",
    "FillConsoleOutputAttribute",
    "GenerateConsoleCtrlEvent",
    "CreateConsoleScreenBuffer",
    "SetConsoleActiveScreenBuffer",
    "FlushConsoleInputBuffer",
    "SetConsoleCP",
    "SetConsoleOutputCP",
    "GetConsoleCursorInfo",
    "SetConsoleCursorInfo",
    "GetConsoleScreenBufferInfo",
    "GetConsoleScreenBufferInfoEx",
    "SetConsoleScreenBufferInfoEx",
    "SetConsoleScreenBufferSize",
    "SetConsoleCursorPosition",
    "GetLargestConsoleWindowSize",
    "SetConsoleTextAttribute",
    "SetConsoleWindowInfo",
    "WriteConsoleOutputCharacterA",
    "WriteConsoleOutputCharacterW",
    "WriteConsoleOutputCharacter",
    "WriteConsoleOutputAttribute",
    "ReadConsoleOutputCharacterA",
    "ReadConsoleOutputCharacterW",
    "ReadConsoleOutputCharacter",
    "ReadConsoleOutputAttribute",
    "WriteConsoleInputA",
    "WriteConsoleInputW",
    "WriteConsoleInput",
    "ScrollConsoleScreenBufferA",
    "ScrollConsoleScreenBufferW",
    "ScrollConsoleScreenBuffer",
    "WriteConsoleOutputA",
    "WriteConsoleOutputW",
    "WriteConsoleOutput",
    "ReadConsoleOutputA",
    "ReadConsoleOutputW",
    "ReadConsoleOutput",
    "GetConsoleTitleA",
    "GetConsoleTitleW",
    "GetConsoleTitle",
    "GetConsoleOriginalTitleA",
    "GetConsoleOriginalTitleW",
    "GetConsoleOriginalTitle",
    "SetConsoleTitleA",
    "SetConsoleTitleW",
    "SetConsoleTitle",
    "GetNumberOfConsoleMouseButtons",
    "GetConsoleFontSize",
    "GetCurrentConsoleFont",
    "GetCurrentConsoleFontEx",
    "SetCurrentConsoleFontEx",
    "GetConsoleSelectionInfo",
    "GetConsoleHistoryInfo",
    "SetConsoleHistoryInfo",
    "GetConsoleDisplayMode",
    "SetConsoleDisplayMode",
    "GetConsoleWindow",
    "AddConsoleAliasA",
    "AddConsoleAliasW",
    "AddConsoleAlias",
    "GetConsoleAliasA",
    "GetConsoleAliasW",
    "GetConsoleAlias",
    "GetConsoleAliasesLengthA",
    "GetConsoleAliasesLengthW",
    "GetConsoleAliasesLength",
    "GetConsoleAliasExesLengthA",
    "GetConsoleAliasExesLengthW",
    "GetConsoleAliasExesLength",
    "GetConsoleAliasesA",
    "GetConsoleAliasesW",
    "GetConsoleAliases",
    "GetConsoleAliasExesA",
    "GetConsoleAliasExesW",
    "GetConsoleAliasExes",
    "ExpungeConsoleCommandHistoryA",
    "ExpungeConsoleCommandHistoryW",
    "ExpungeConsoleCommandHistory",
    "SetConsoleNumberOfCommandsA",
    "SetConsoleNumberOfCommandsW",
    "SetConsoleNumberOfCommands",
    "GetConsoleCommandHistoryLengthA",
    "GetConsoleCommandHistoryLengthW",
    "GetConsoleCommandHistoryLength",
    "GetConsoleCommandHistoryA",
    "GetConsoleCommandHistoryW",
    "GetConsoleCommandHistory",
    "GetConsoleProcessList",
    "GetStdHandle",
    "SetStdHandle",
    "SetStdHandleEx",
]
