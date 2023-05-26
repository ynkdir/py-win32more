from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.System.Console
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
CONSOLE_TEXTMODE_BUFFER: UInt32 = 1
ATTACH_PARENT_PROCESS: UInt32 = 4294967295
CTRL_C_EVENT: UInt32 = 0
CTRL_BREAK_EVENT: UInt32 = 1
CTRL_CLOSE_EVENT: UInt32 = 2
CTRL_LOGOFF_EVENT: UInt32 = 5
CTRL_SHUTDOWN_EVENT: UInt32 = 6
PSEUDOCONSOLE_INHERIT_CURSOR: UInt32 = 1
CONSOLE_NO_SELECTION: UInt32 = 0
CONSOLE_SELECTION_IN_PROGRESS: UInt32 = 1
CONSOLE_SELECTION_NOT_EMPTY: UInt32 = 2
CONSOLE_MOUSE_SELECTION: UInt32 = 4
CONSOLE_MOUSE_DOWN: UInt32 = 8
HISTORY_NO_DUP_FLAG: UInt32 = 1
CONSOLE_FULLSCREEN: UInt32 = 1
CONSOLE_FULLSCREEN_HARDWARE: UInt32 = 2
CONSOLE_FULLSCREEN_MODE: UInt32 = 1
CONSOLE_WINDOWED_MODE: UInt32 = 2
RIGHT_ALT_PRESSED: UInt32 = 1
LEFT_ALT_PRESSED: UInt32 = 2
RIGHT_CTRL_PRESSED: UInt32 = 4
LEFT_CTRL_PRESSED: UInt32 = 8
SHIFT_PRESSED: UInt32 = 16
NUMLOCK_ON: UInt32 = 32
SCROLLLOCK_ON: UInt32 = 64
CAPSLOCK_ON: UInt32 = 128
ENHANCED_KEY: UInt32 = 256
NLS_DBCSCHAR: UInt32 = 65536
NLS_ALPHANUMERIC: UInt32 = 0
NLS_KATAKANA: UInt32 = 131072
NLS_HIRAGANA: UInt32 = 262144
NLS_ROMAN: UInt32 = 4194304
NLS_IME_CONVERSION: UInt32 = 8388608
ALTNUMPAD_BIT: UInt32 = 67108864
NLS_IME_DISABLE: UInt32 = 536870912
FROM_LEFT_1ST_BUTTON_PRESSED: UInt32 = 1
RIGHTMOST_BUTTON_PRESSED: UInt32 = 2
FROM_LEFT_2ND_BUTTON_PRESSED: UInt32 = 4
FROM_LEFT_3RD_BUTTON_PRESSED: UInt32 = 8
FROM_LEFT_4TH_BUTTON_PRESSED: UInt32 = 16
MOUSE_MOVED: UInt32 = 1
DOUBLE_CLICK: UInt32 = 2
MOUSE_WHEELED: UInt32 = 4
MOUSE_HWHEELED: UInt32 = 8
KEY_EVENT: UInt32 = 1
MOUSE_EVENT: UInt32 = 2
WINDOW_BUFFER_SIZE_EVENT: UInt32 = 4
MENU_EVENT: UInt32 = 8
FOCUS_EVENT: UInt32 = 16
@winfunctype('KERNEL32.dll')
def AllocConsole() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FreeConsole() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AttachConsole(dwProcessId: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleCP() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleOutputCP() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleMode(hConsoleHandle: Windows.Win32.Foundation.HANDLE, lpMode: POINTER(Windows.Win32.System.Console.CONSOLE_MODE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleMode(hConsoleHandle: Windows.Win32.Foundation.HANDLE, dwMode: Windows.Win32.System.Console.CONSOLE_MODE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumberOfConsoleInputEvents(hConsoleInput: Windows.Win32.Foundation.HANDLE, lpNumberOfEvents: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleInputA(hConsoleInput: Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Windows.Win32.System.Console.INPUT_RECORD_head), nLength: UInt32, lpNumberOfEventsRead: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleInputW(hConsoleInput: Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Windows.Win32.System.Console.INPUT_RECORD_head), nLength: UInt32, lpNumberOfEventsRead: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PeekConsoleInputA(hConsoleInput: Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Windows.Win32.System.Console.INPUT_RECORD_head), nLength: UInt32, lpNumberOfEventsRead: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PeekConsoleInputW(hConsoleInput: Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Windows.Win32.System.Console.INPUT_RECORD_head), nLength: UInt32, lpNumberOfEventsRead: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleA(hConsoleInput: Windows.Win32.Foundation.HANDLE, lpBuffer: VoidPtr, nNumberOfCharsToRead: UInt32, lpNumberOfCharsRead: POINTER(UInt32), pInputControl: POINTER(Windows.Win32.System.Console.CONSOLE_READCONSOLE_CONTROL_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleW(hConsoleInput: Windows.Win32.Foundation.HANDLE, lpBuffer: VoidPtr, nNumberOfCharsToRead: UInt32, lpNumberOfCharsRead: POINTER(UInt32), pInputControl: POINTER(Windows.Win32.System.Console.CONSOLE_READCONSOLE_CONTROL_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleA(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpBuffer: VoidPtr, nNumberOfCharsToWrite: UInt32, lpNumberOfCharsWritten: POINTER(UInt32), lpReserved: VoidPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleW(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpBuffer: VoidPtr, nNumberOfCharsToWrite: UInt32, lpNumberOfCharsWritten: POINTER(UInt32), lpReserved: VoidPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleCtrlHandler(HandlerRoutine: Windows.Win32.System.Console.PHANDLER_ROUTINE, Add: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreatePseudoConsole(size: Windows.Win32.System.Console.COORD, hInput: Windows.Win32.Foundation.HANDLE, hOutput: Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, phPC: POINTER(Windows.Win32.System.Console.HPCON)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ResizePseudoConsole(hPC: Windows.Win32.System.Console.HPCON, size: Windows.Win32.System.Console.COORD) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ClosePseudoConsole(hPC: Windows.Win32.System.Console.HPCON) -> Void: ...
@winfunctype('KERNEL32.dll')
def FillConsoleOutputCharacterA(hConsoleOutput: Windows.Win32.Foundation.HANDLE, cCharacter: Windows.Win32.Foundation.CHAR, nLength: UInt32, dwWriteCoord: Windows.Win32.System.Console.COORD, lpNumberOfCharsWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FillConsoleOutputCharacterW(hConsoleOutput: Windows.Win32.Foundation.HANDLE, cCharacter: Char, nLength: UInt32, dwWriteCoord: Windows.Win32.System.Console.COORD, lpNumberOfCharsWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FillConsoleOutputAttribute(hConsoleOutput: Windows.Win32.Foundation.HANDLE, wAttribute: UInt16, nLength: UInt32, dwWriteCoord: Windows.Win32.System.Console.COORD, lpNumberOfAttrsWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GenerateConsoleCtrlEvent(dwCtrlEvent: UInt32, dwProcessGroupId: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateConsoleScreenBuffer(dwDesiredAccess: UInt32, dwShareMode: UInt32, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwFlags: UInt32, lpScreenBufferData: VoidPtr) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetConsoleActiveScreenBuffer(hConsoleOutput: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlushConsoleInputBuffer(hConsoleInput: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleCP(wCodePageID: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleOutputCP(wCodePageID: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleCursorInfo(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpConsoleCursorInfo: POINTER(Windows.Win32.System.Console.CONSOLE_CURSOR_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleCursorInfo(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpConsoleCursorInfo: POINTER(Windows.Win32.System.Console.CONSOLE_CURSOR_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleScreenBufferInfo(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpConsoleScreenBufferInfo: POINTER(Windows.Win32.System.Console.CONSOLE_SCREEN_BUFFER_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleScreenBufferInfoEx(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpConsoleScreenBufferInfoEx: POINTER(Windows.Win32.System.Console.CONSOLE_SCREEN_BUFFER_INFOEX_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleScreenBufferInfoEx(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpConsoleScreenBufferInfoEx: POINTER(Windows.Win32.System.Console.CONSOLE_SCREEN_BUFFER_INFOEX_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleScreenBufferSize(hConsoleOutput: Windows.Win32.Foundation.HANDLE, dwSize: Windows.Win32.System.Console.COORD) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleCursorPosition(hConsoleOutput: Windows.Win32.Foundation.HANDLE, dwCursorPosition: Windows.Win32.System.Console.COORD) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetLargestConsoleWindowSize(hConsoleOutput: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.System.Console.COORD: ...
@winfunctype('KERNEL32.dll')
def SetConsoleTextAttribute(hConsoleOutput: Windows.Win32.Foundation.HANDLE, wAttributes: Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleWindowInfo(hConsoleOutput: Windows.Win32.Foundation.HANDLE, bAbsolute: Windows.Win32.Foundation.BOOL, lpConsoleWindow: POINTER(Windows.Win32.System.Console.SMALL_RECT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleOutputCharacterA(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpCharacter: Windows.Win32.Foundation.PSTR, nLength: UInt32, dwWriteCoord: Windows.Win32.System.Console.COORD, lpNumberOfCharsWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleOutputCharacterW(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpCharacter: Windows.Win32.Foundation.PWSTR, nLength: UInt32, dwWriteCoord: Windows.Win32.System.Console.COORD, lpNumberOfCharsWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleOutputAttribute(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpAttribute: POINTER(UInt16), nLength: UInt32, dwWriteCoord: Windows.Win32.System.Console.COORD, lpNumberOfAttrsWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleOutputCharacterA(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpCharacter: Windows.Win32.Foundation.PSTR, nLength: UInt32, dwReadCoord: Windows.Win32.System.Console.COORD, lpNumberOfCharsRead: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleOutputCharacterW(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpCharacter: Windows.Win32.Foundation.PWSTR, nLength: UInt32, dwReadCoord: Windows.Win32.System.Console.COORD, lpNumberOfCharsRead: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleOutputAttribute(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpAttribute: POINTER(UInt16), nLength: UInt32, dwReadCoord: Windows.Win32.System.Console.COORD, lpNumberOfAttrsRead: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleInputA(hConsoleInput: Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Windows.Win32.System.Console.INPUT_RECORD_head), nLength: UInt32, lpNumberOfEventsWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleInputW(hConsoleInput: Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Windows.Win32.System.Console.INPUT_RECORD_head), nLength: UInt32, lpNumberOfEventsWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ScrollConsoleScreenBufferA(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpScrollRectangle: POINTER(Windows.Win32.System.Console.SMALL_RECT_head), lpClipRectangle: POINTER(Windows.Win32.System.Console.SMALL_RECT_head), dwDestinationOrigin: Windows.Win32.System.Console.COORD, lpFill: POINTER(Windows.Win32.System.Console.CHAR_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ScrollConsoleScreenBufferW(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpScrollRectangle: POINTER(Windows.Win32.System.Console.SMALL_RECT_head), lpClipRectangle: POINTER(Windows.Win32.System.Console.SMALL_RECT_head), dwDestinationOrigin: Windows.Win32.System.Console.COORD, lpFill: POINTER(Windows.Win32.System.Console.CHAR_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleOutputA(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Windows.Win32.System.Console.CHAR_INFO_head), dwBufferSize: Windows.Win32.System.Console.COORD, dwBufferCoord: Windows.Win32.System.Console.COORD, lpWriteRegion: POINTER(Windows.Win32.System.Console.SMALL_RECT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleOutputW(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Windows.Win32.System.Console.CHAR_INFO_head), dwBufferSize: Windows.Win32.System.Console.COORD, dwBufferCoord: Windows.Win32.System.Console.COORD, lpWriteRegion: POINTER(Windows.Win32.System.Console.SMALL_RECT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleOutputA(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Windows.Win32.System.Console.CHAR_INFO_head), dwBufferSize: Windows.Win32.System.Console.COORD, dwBufferCoord: Windows.Win32.System.Console.COORD, lpReadRegion: POINTER(Windows.Win32.System.Console.SMALL_RECT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleOutputW(hConsoleOutput: Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(Windows.Win32.System.Console.CHAR_INFO_head), dwBufferSize: Windows.Win32.System.Console.COORD, dwBufferCoord: Windows.Win32.System.Console.COORD, lpReadRegion: POINTER(Windows.Win32.System.Console.SMALL_RECT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleTitleA(lpConsoleTitle: Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleTitleW(lpConsoleTitle: Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleOriginalTitleA(lpConsoleTitle: Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleOriginalTitleW(lpConsoleTitle: Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def SetConsoleTitleA(lpConsoleTitle: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleTitleW(lpConsoleTitle: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumberOfConsoleMouseButtons(lpNumberOfMouseButtons: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleFontSize(hConsoleOutput: Windows.Win32.Foundation.HANDLE, nFont: UInt32) -> Windows.Win32.System.Console.COORD: ...
@winfunctype('KERNEL32.dll')
def GetCurrentConsoleFont(hConsoleOutput: Windows.Win32.Foundation.HANDLE, bMaximumWindow: Windows.Win32.Foundation.BOOL, lpConsoleCurrentFont: POINTER(Windows.Win32.System.Console.CONSOLE_FONT_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCurrentConsoleFontEx(hConsoleOutput: Windows.Win32.Foundation.HANDLE, bMaximumWindow: Windows.Win32.Foundation.BOOL, lpConsoleCurrentFontEx: POINTER(Windows.Win32.System.Console.CONSOLE_FONT_INFOEX_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCurrentConsoleFontEx(hConsoleOutput: Windows.Win32.Foundation.HANDLE, bMaximumWindow: Windows.Win32.Foundation.BOOL, lpConsoleCurrentFontEx: POINTER(Windows.Win32.System.Console.CONSOLE_FONT_INFOEX_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleSelectionInfo(lpConsoleSelectionInfo: POINTER(Windows.Win32.System.Console.CONSOLE_SELECTION_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleHistoryInfo(lpConsoleHistoryInfo: POINTER(Windows.Win32.System.Console.CONSOLE_HISTORY_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleHistoryInfo(lpConsoleHistoryInfo: POINTER(Windows.Win32.System.Console.CONSOLE_HISTORY_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleDisplayMode(lpModeFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleDisplayMode(hConsoleOutput: Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, lpNewScreenBufferDimensions: POINTER(Windows.Win32.System.Console.COORD_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleWindow() -> Windows.Win32.Foundation.HWND: ...
@winfunctype('KERNEL32.dll')
def AddConsoleAliasA(Source: Windows.Win32.Foundation.PSTR, Target: Windows.Win32.Foundation.PSTR, ExeName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AddConsoleAliasW(Source: Windows.Win32.Foundation.PWSTR, Target: Windows.Win32.Foundation.PWSTR, ExeName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasA(Source: Windows.Win32.Foundation.PSTR, TargetBuffer: Windows.Win32.Foundation.PSTR, TargetBufferLength: UInt32, ExeName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasW(Source: Windows.Win32.Foundation.PWSTR, TargetBuffer: Windows.Win32.Foundation.PWSTR, TargetBufferLength: UInt32, ExeName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasesLengthA(ExeName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasesLengthW(ExeName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasExesLengthA() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasExesLengthW() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasesA(AliasBuffer: Windows.Win32.Foundation.PSTR, AliasBufferLength: UInt32, ExeName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasesW(AliasBuffer: Windows.Win32.Foundation.PWSTR, AliasBufferLength: UInt32, ExeName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasExesA(ExeNameBuffer: Windows.Win32.Foundation.PSTR, ExeNameBufferLength: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasExesW(ExeNameBuffer: Windows.Win32.Foundation.PWSTR, ExeNameBufferLength: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ExpungeConsoleCommandHistoryA(ExeName: Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('KERNEL32.dll')
def ExpungeConsoleCommandHistoryW(ExeName: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('KERNEL32.dll')
def SetConsoleNumberOfCommandsA(Number: UInt32, ExeName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleNumberOfCommandsW(Number: UInt32, ExeName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleCommandHistoryLengthA(ExeName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleCommandHistoryLengthW(ExeName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleCommandHistoryA(Commands: Windows.Win32.Foundation.PSTR, CommandBufferLength: UInt32, ExeName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleCommandHistoryW(Commands: Windows.Win32.Foundation.PWSTR, CommandBufferLength: UInt32, ExeName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleProcessList(lpdwProcessList: POINTER(UInt32), dwProcessCount: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetStdHandle(nStdHandle: Windows.Win32.System.Console.STD_HANDLE) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetStdHandle(nStdHandle: Windows.Win32.System.Console.STD_HANDLE, hHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetStdHandleEx(nStdHandle: Windows.Win32.System.Console.STD_HANDLE, hHandle: Windows.Win32.Foundation.HANDLE, phPrevValue: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
class CHAR_INFO(EasyCastStructure):
    Char: _Char_e__Union
    Attributes: UInt16
    class _Char_e__Union(EasyCastUnion):
        UnicodeChar: Char
        AsciiChar: Windows.Win32.Foundation.CHAR
CONSOLE_CHARACTER_ATTRIBUTES = UInt16
FOREGROUND_BLUE: CONSOLE_CHARACTER_ATTRIBUTES = 1
FOREGROUND_GREEN: CONSOLE_CHARACTER_ATTRIBUTES = 2
FOREGROUND_RED: CONSOLE_CHARACTER_ATTRIBUTES = 4
FOREGROUND_INTENSITY: CONSOLE_CHARACTER_ATTRIBUTES = 8
BACKGROUND_BLUE: CONSOLE_CHARACTER_ATTRIBUTES = 16
BACKGROUND_GREEN: CONSOLE_CHARACTER_ATTRIBUTES = 32
BACKGROUND_RED: CONSOLE_CHARACTER_ATTRIBUTES = 64
BACKGROUND_INTENSITY: CONSOLE_CHARACTER_ATTRIBUTES = 128
COMMON_LVB_LEADING_BYTE: CONSOLE_CHARACTER_ATTRIBUTES = 256
COMMON_LVB_TRAILING_BYTE: CONSOLE_CHARACTER_ATTRIBUTES = 512
COMMON_LVB_GRID_HORIZONTAL: CONSOLE_CHARACTER_ATTRIBUTES = 1024
COMMON_LVB_GRID_LVERTICAL: CONSOLE_CHARACTER_ATTRIBUTES = 2048
COMMON_LVB_GRID_RVERTICAL: CONSOLE_CHARACTER_ATTRIBUTES = 4096
COMMON_LVB_REVERSE_VIDEO: CONSOLE_CHARACTER_ATTRIBUTES = 16384
COMMON_LVB_UNDERSCORE: CONSOLE_CHARACTER_ATTRIBUTES = 32768
COMMON_LVB_SBCSDBCS: CONSOLE_CHARACTER_ATTRIBUTES = 768
class CONSOLE_CURSOR_INFO(EasyCastStructure):
    dwSize: UInt32
    bVisible: Windows.Win32.Foundation.BOOL
class CONSOLE_FONT_INFO(EasyCastStructure):
    nFont: UInt32
    dwFontSize: Windows.Win32.System.Console.COORD
class CONSOLE_FONT_INFOEX(EasyCastStructure):
    cbSize: UInt32
    nFont: UInt32
    dwFontSize: Windows.Win32.System.Console.COORD
    FontFamily: UInt32
    FontWeight: UInt32
    FaceName: Char * 32
class CONSOLE_HISTORY_INFO(EasyCastStructure):
    cbSize: UInt32
    HistoryBufferSize: UInt32
    NumberOfHistoryBuffers: UInt32
    dwFlags: UInt32
CONSOLE_MODE = UInt32
ENABLE_PROCESSED_INPUT: CONSOLE_MODE = 1
ENABLE_LINE_INPUT: CONSOLE_MODE = 2
ENABLE_ECHO_INPUT: CONSOLE_MODE = 4
ENABLE_WINDOW_INPUT: CONSOLE_MODE = 8
ENABLE_MOUSE_INPUT: CONSOLE_MODE = 16
ENABLE_INSERT_MODE: CONSOLE_MODE = 32
ENABLE_QUICK_EDIT_MODE: CONSOLE_MODE = 64
ENABLE_EXTENDED_FLAGS: CONSOLE_MODE = 128
ENABLE_AUTO_POSITION: CONSOLE_MODE = 256
ENABLE_VIRTUAL_TERMINAL_INPUT: CONSOLE_MODE = 512
ENABLE_PROCESSED_OUTPUT: CONSOLE_MODE = 1
ENABLE_WRAP_AT_EOL_OUTPUT: CONSOLE_MODE = 2
ENABLE_VIRTUAL_TERMINAL_PROCESSING: CONSOLE_MODE = 4
DISABLE_NEWLINE_AUTO_RETURN: CONSOLE_MODE = 8
ENABLE_LVB_GRID_WORLDWIDE: CONSOLE_MODE = 16
class CONSOLE_READCONSOLE_CONTROL(EasyCastStructure):
    nLength: UInt32
    nInitialChars: UInt32
    dwCtrlWakeupMask: UInt32
    dwControlKeyState: UInt32
class CONSOLE_SCREEN_BUFFER_INFO(EasyCastStructure):
    dwSize: Windows.Win32.System.Console.COORD
    dwCursorPosition: Windows.Win32.System.Console.COORD
    wAttributes: Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES
    srWindow: Windows.Win32.System.Console.SMALL_RECT
    dwMaximumWindowSize: Windows.Win32.System.Console.COORD
class CONSOLE_SCREEN_BUFFER_INFOEX(EasyCastStructure):
    cbSize: UInt32
    dwSize: Windows.Win32.System.Console.COORD
    dwCursorPosition: Windows.Win32.System.Console.COORD
    wAttributes: Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES
    srWindow: Windows.Win32.System.Console.SMALL_RECT
    dwMaximumWindowSize: Windows.Win32.System.Console.COORD
    wPopupAttributes: UInt16
    bFullscreenSupported: Windows.Win32.Foundation.BOOL
    ColorTable: Windows.Win32.Foundation.COLORREF * 16
class CONSOLE_SELECTION_INFO(EasyCastStructure):
    dwFlags: UInt32
    dwSelectionAnchor: Windows.Win32.System.Console.COORD
    srSelection: Windows.Win32.System.Console.SMALL_RECT
class COORD(EasyCastStructure):
    X: Int16
    Y: Int16
class FOCUS_EVENT_RECORD(EasyCastStructure):
    bSetFocus: Windows.Win32.Foundation.BOOL
HPCON = IntPtr
class INPUT_RECORD(EasyCastStructure):
    EventType: UInt16
    Event: _Event_e__Union
    class _Event_e__Union(EasyCastUnion):
        KeyEvent: Windows.Win32.System.Console.KEY_EVENT_RECORD
        MouseEvent: Windows.Win32.System.Console.MOUSE_EVENT_RECORD
        WindowBufferSizeEvent: Windows.Win32.System.Console.WINDOW_BUFFER_SIZE_RECORD
        MenuEvent: Windows.Win32.System.Console.MENU_EVENT_RECORD
        FocusEvent: Windows.Win32.System.Console.FOCUS_EVENT_RECORD
class KEY_EVENT_RECORD(EasyCastStructure):
    bKeyDown: Windows.Win32.Foundation.BOOL
    wRepeatCount: UInt16
    wVirtualKeyCode: UInt16
    wVirtualScanCode: UInt16
    uChar: _uChar_e__Union
    dwControlKeyState: UInt32
    class _uChar_e__Union(EasyCastUnion):
        UnicodeChar: Char
        AsciiChar: Windows.Win32.Foundation.CHAR
class MENU_EVENT_RECORD(EasyCastStructure):
    dwCommandId: UInt32
class MOUSE_EVENT_RECORD(EasyCastStructure):
    dwMousePosition: Windows.Win32.System.Console.COORD
    dwButtonState: UInt32
    dwControlKeyState: UInt32
    dwEventFlags: UInt32
@winfunctype_pointer
def PHANDLER_ROUTINE(CtrlType: UInt32) -> Windows.Win32.Foundation.BOOL: ...
class SMALL_RECT(EasyCastStructure):
    Left: Int16
    Top: Int16
    Right: Int16
    Bottom: Int16
STD_HANDLE = UInt32
STD_INPUT_HANDLE: STD_HANDLE = 4294967286
STD_OUTPUT_HANDLE: STD_HANDLE = 4294967285
STD_ERROR_HANDLE: STD_HANDLE = 4294967284
class WINDOW_BUFFER_SIZE_RECORD(EasyCastStructure):
    dwSize: Windows.Win32.System.Console.COORD
make_head(_module, 'CHAR_INFO')
make_head(_module, 'CONSOLE_CURSOR_INFO')
make_head(_module, 'CONSOLE_FONT_INFO')
make_head(_module, 'CONSOLE_FONT_INFOEX')
make_head(_module, 'CONSOLE_HISTORY_INFO')
make_head(_module, 'CONSOLE_READCONSOLE_CONTROL')
make_head(_module, 'CONSOLE_SCREEN_BUFFER_INFO')
make_head(_module, 'CONSOLE_SCREEN_BUFFER_INFOEX')
make_head(_module, 'CONSOLE_SELECTION_INFO')
make_head(_module, 'COORD')
make_head(_module, 'FOCUS_EVENT_RECORD')
make_head(_module, 'INPUT_RECORD')
make_head(_module, 'KEY_EVENT_RECORD')
make_head(_module, 'MENU_EVENT_RECORD')
make_head(_module, 'MOUSE_EVENT_RECORD')
make_head(_module, 'PHANDLER_ROUTINE')
make_head(_module, 'SMALL_RECT')
make_head(_module, 'WINDOW_BUFFER_SIZE_RECORD')
