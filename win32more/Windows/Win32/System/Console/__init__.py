from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Console
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
def AllocConsole() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FreeConsole() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AttachConsole(dwProcessId: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleCP() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleOutputCP() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleMode(hConsoleHandle: win32more.Windows.Win32.Foundation.HANDLE, lpMode: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_MODE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleMode(hConsoleHandle: win32more.Windows.Win32.Foundation.HANDLE, dwMode: win32more.Windows.Win32.System.Console.CONSOLE_MODE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetNumberOfConsoleInputEvents(hConsoleInput: win32more.Windows.Win32.Foundation.HANDLE, lpNumberOfEvents: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleInputA(hConsoleInput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(win32more.Windows.Win32.System.Console.INPUT_RECORD), nLength: UInt32, lpNumberOfEventsRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleInputW(hConsoleInput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(win32more.Windows.Win32.System.Console.INPUT_RECORD), nLength: UInt32, lpNumberOfEventsRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ReadConsoleInput = UnicodeAlias('ReadConsoleInputW')
@winfunctype('KERNEL32.dll')
def PeekConsoleInputA(hConsoleInput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(win32more.Windows.Win32.System.Console.INPUT_RECORD), nLength: UInt32, lpNumberOfEventsRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def PeekConsoleInputW(hConsoleInput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(win32more.Windows.Win32.System.Console.INPUT_RECORD), nLength: UInt32, lpNumberOfEventsRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PeekConsoleInput = UnicodeAlias('PeekConsoleInputW')
@winfunctype('KERNEL32.dll')
def ReadConsoleA(hConsoleInput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: VoidPtr, nNumberOfCharsToRead: UInt32, lpNumberOfCharsRead: POINTER(UInt32), pInputControl: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_READCONSOLE_CONTROL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleW(hConsoleInput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: VoidPtr, nNumberOfCharsToRead: UInt32, lpNumberOfCharsRead: POINTER(UInt32), pInputControl: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_READCONSOLE_CONTROL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ReadConsole = UnicodeAlias('ReadConsoleW')
@winfunctype('KERNEL32.dll')
def WriteConsoleA(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, nNumberOfCharsToWrite: UInt32, lpNumberOfCharsWritten: POINTER(UInt32), lpReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleW(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, nNumberOfCharsToWrite: UInt32, lpNumberOfCharsWritten: POINTER(UInt32), lpReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
WriteConsole = UnicodeAlias('WriteConsoleW')
@winfunctype('KERNEL32.dll')
def SetConsoleCtrlHandler(HandlerRoutine: win32more.Windows.Win32.System.Console.PHANDLER_ROUTINE, Add: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreatePseudoConsole(size: win32more.Windows.Win32.System.Console.COORD, hInput: win32more.Windows.Win32.Foundation.HANDLE, hOutput: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, phPC: POINTER(win32more.Windows.Win32.System.Console.HPCON)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ResizePseudoConsole(hPC: win32more.Windows.Win32.System.Console.HPCON, size: win32more.Windows.Win32.System.Console.COORD) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('KERNEL32.dll')
def ClosePseudoConsole(hPC: win32more.Windows.Win32.System.Console.HPCON) -> Void: ...
@winfunctype('KERNEL32.dll')
def FillConsoleOutputCharacterA(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, cCharacter: win32more.Windows.Win32.Foundation.CHAR, nLength: UInt32, dwWriteCoord: win32more.Windows.Win32.System.Console.COORD, lpNumberOfCharsWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FillConsoleOutputCharacterW(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, cCharacter: Char, nLength: UInt32, dwWriteCoord: win32more.Windows.Win32.System.Console.COORD, lpNumberOfCharsWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
FillConsoleOutputCharacter = UnicodeAlias('FillConsoleOutputCharacterW')
@winfunctype('KERNEL32.dll')
def FillConsoleOutputAttribute(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, wAttribute: UInt16, nLength: UInt32, dwWriteCoord: win32more.Windows.Win32.System.Console.COORD, lpNumberOfAttrsWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GenerateConsoleCtrlEvent(dwCtrlEvent: UInt32, dwProcessGroupId: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateConsoleScreenBuffer(dwDesiredAccess: UInt32, dwShareMode: UInt32, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), dwFlags: UInt32, lpScreenBufferData: VoidPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetConsoleActiveScreenBuffer(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlushConsoleInputBuffer(hConsoleInput: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleCP(wCodePageID: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleOutputCP(wCodePageID: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleCursorInfo(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpConsoleCursorInfo: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_CURSOR_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleCursorInfo(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpConsoleCursorInfo: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_CURSOR_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleScreenBufferInfo(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpConsoleScreenBufferInfo: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_SCREEN_BUFFER_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleScreenBufferInfoEx(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpConsoleScreenBufferInfoEx: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_SCREEN_BUFFER_INFOEX)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleScreenBufferInfoEx(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpConsoleScreenBufferInfoEx: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_SCREEN_BUFFER_INFOEX)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleScreenBufferSize(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, dwSize: win32more.Windows.Win32.System.Console.COORD) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleCursorPosition(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, dwCursorPosition: win32more.Windows.Win32.System.Console.COORD) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetLargestConsoleWindowSize(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.System.Console.COORD: ...
@winfunctype('KERNEL32.dll')
def SetConsoleTextAttribute(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, wAttributes: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleWindowInfo(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, bAbsolute: win32more.Windows.Win32.Foundation.BOOL, lpConsoleWindow: POINTER(win32more.Windows.Win32.System.Console.SMALL_RECT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleOutputCharacterA(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpCharacter: win32more.Windows.Win32.Foundation.PSTR, nLength: UInt32, dwWriteCoord: win32more.Windows.Win32.System.Console.COORD, lpNumberOfCharsWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleOutputCharacterW(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpCharacter: win32more.Windows.Win32.Foundation.PWSTR, nLength: UInt32, dwWriteCoord: win32more.Windows.Win32.System.Console.COORD, lpNumberOfCharsWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
WriteConsoleOutputCharacter = UnicodeAlias('WriteConsoleOutputCharacterW')
@winfunctype('KERNEL32.dll')
def WriteConsoleOutputAttribute(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpAttribute: POINTER(UInt16), nLength: UInt32, dwWriteCoord: win32more.Windows.Win32.System.Console.COORD, lpNumberOfAttrsWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleOutputCharacterA(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpCharacter: win32more.Windows.Win32.Foundation.PSTR, nLength: UInt32, dwReadCoord: win32more.Windows.Win32.System.Console.COORD, lpNumberOfCharsRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleOutputCharacterW(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpCharacter: win32more.Windows.Win32.Foundation.PWSTR, nLength: UInt32, dwReadCoord: win32more.Windows.Win32.System.Console.COORD, lpNumberOfCharsRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ReadConsoleOutputCharacter = UnicodeAlias('ReadConsoleOutputCharacterW')
@winfunctype('KERNEL32.dll')
def ReadConsoleOutputAttribute(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpAttribute: POINTER(UInt16), nLength: UInt32, dwReadCoord: win32more.Windows.Win32.System.Console.COORD, lpNumberOfAttrsRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleInputA(hConsoleInput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(win32more.Windows.Win32.System.Console.INPUT_RECORD), nLength: UInt32, lpNumberOfEventsWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleInputW(hConsoleInput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(win32more.Windows.Win32.System.Console.INPUT_RECORD), nLength: UInt32, lpNumberOfEventsWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
WriteConsoleInput = UnicodeAlias('WriteConsoleInputW')
@winfunctype('KERNEL32.dll')
def ScrollConsoleScreenBufferA(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpScrollRectangle: POINTER(win32more.Windows.Win32.System.Console.SMALL_RECT), lpClipRectangle: POINTER(win32more.Windows.Win32.System.Console.SMALL_RECT), dwDestinationOrigin: win32more.Windows.Win32.System.Console.COORD, lpFill: POINTER(win32more.Windows.Win32.System.Console.CHAR_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ScrollConsoleScreenBufferW(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpScrollRectangle: POINTER(win32more.Windows.Win32.System.Console.SMALL_RECT), lpClipRectangle: POINTER(win32more.Windows.Win32.System.Console.SMALL_RECT), dwDestinationOrigin: win32more.Windows.Win32.System.Console.COORD, lpFill: POINTER(win32more.Windows.Win32.System.Console.CHAR_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ScrollConsoleScreenBuffer = UnicodeAlias('ScrollConsoleScreenBufferW')
@winfunctype('KERNEL32.dll')
def WriteConsoleOutputA(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(win32more.Windows.Win32.System.Console.CHAR_INFO), dwBufferSize: win32more.Windows.Win32.System.Console.COORD, dwBufferCoord: win32more.Windows.Win32.System.Console.COORD, lpWriteRegion: POINTER(win32more.Windows.Win32.System.Console.SMALL_RECT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def WriteConsoleOutputW(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(win32more.Windows.Win32.System.Console.CHAR_INFO), dwBufferSize: win32more.Windows.Win32.System.Console.COORD, dwBufferCoord: win32more.Windows.Win32.System.Console.COORD, lpWriteRegion: POINTER(win32more.Windows.Win32.System.Console.SMALL_RECT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
WriteConsoleOutput = UnicodeAlias('WriteConsoleOutputW')
@winfunctype('KERNEL32.dll')
def ReadConsoleOutputA(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(win32more.Windows.Win32.System.Console.CHAR_INFO), dwBufferSize: win32more.Windows.Win32.System.Console.COORD, dwBufferCoord: win32more.Windows.Win32.System.Console.COORD, lpReadRegion: POINTER(win32more.Windows.Win32.System.Console.SMALL_RECT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def ReadConsoleOutputW(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, lpBuffer: POINTER(win32more.Windows.Win32.System.Console.CHAR_INFO), dwBufferSize: win32more.Windows.Win32.System.Console.COORD, dwBufferCoord: win32more.Windows.Win32.System.Console.COORD, lpReadRegion: POINTER(win32more.Windows.Win32.System.Console.SMALL_RECT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ReadConsoleOutput = UnicodeAlias('ReadConsoleOutputW')
@winfunctype('KERNEL32.dll')
def GetConsoleTitleA(lpConsoleTitle: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleTitleW(lpConsoleTitle: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
GetConsoleTitle = UnicodeAlias('GetConsoleTitleW')
@winfunctype('KERNEL32.dll')
def GetConsoleOriginalTitleA(lpConsoleTitle: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleOriginalTitleW(lpConsoleTitle: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
GetConsoleOriginalTitle = UnicodeAlias('GetConsoleOriginalTitleW')
@winfunctype('KERNEL32.dll')
def SetConsoleTitleA(lpConsoleTitle: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleTitleW(lpConsoleTitle: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetConsoleTitle = UnicodeAlias('SetConsoleTitleW')
@winfunctype('KERNEL32.dll')
def GetNumberOfConsoleMouseButtons(lpNumberOfMouseButtons: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleFontSize(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, nFont: UInt32) -> win32more.Windows.Win32.System.Console.COORD: ...
@winfunctype('KERNEL32.dll')
def GetCurrentConsoleFont(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, bMaximumWindow: win32more.Windows.Win32.Foundation.BOOL, lpConsoleCurrentFont: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_FONT_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetCurrentConsoleFontEx(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, bMaximumWindow: win32more.Windows.Win32.Foundation.BOOL, lpConsoleCurrentFontEx: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_FONT_INFOEX)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetCurrentConsoleFontEx(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, bMaximumWindow: win32more.Windows.Win32.Foundation.BOOL, lpConsoleCurrentFontEx: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_FONT_INFOEX)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleSelectionInfo(lpConsoleSelectionInfo: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_SELECTION_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleHistoryInfo(lpConsoleHistoryInfo: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_HISTORY_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleHistoryInfo(lpConsoleHistoryInfo: POINTER(win32more.Windows.Win32.System.Console.CONSOLE_HISTORY_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleDisplayMode(lpModeFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleDisplayMode(hConsoleOutput: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, lpNewScreenBufferDimensions: POINTER(win32more.Windows.Win32.System.Console.COORD)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetConsoleWindow() -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('KERNEL32.dll')
def AddConsoleAliasA(Source: win32more.Windows.Win32.Foundation.PSTR, Target: win32more.Windows.Win32.Foundation.PSTR, ExeName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AddConsoleAliasW(Source: win32more.Windows.Win32.Foundation.PWSTR, Target: win32more.Windows.Win32.Foundation.PWSTR, ExeName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
AddConsoleAlias = UnicodeAlias('AddConsoleAliasW')
@winfunctype('KERNEL32.dll')
def GetConsoleAliasA(Source: win32more.Windows.Win32.Foundation.PSTR, TargetBuffer: win32more.Windows.Win32.Foundation.PSTR, TargetBufferLength: UInt32, ExeName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasW(Source: win32more.Windows.Win32.Foundation.PWSTR, TargetBuffer: win32more.Windows.Win32.Foundation.PWSTR, TargetBufferLength: UInt32, ExeName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
GetConsoleAlias = UnicodeAlias('GetConsoleAliasW')
@winfunctype('KERNEL32.dll')
def GetConsoleAliasesLengthA(ExeName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasesLengthW(ExeName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
GetConsoleAliasesLength = UnicodeAlias('GetConsoleAliasesLengthW')
@winfunctype('KERNEL32.dll')
def GetConsoleAliasExesLengthA() -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasExesLengthW() -> UInt32: ...
GetConsoleAliasExesLength = UnicodeAlias('GetConsoleAliasExesLengthW')
@winfunctype('KERNEL32.dll')
def GetConsoleAliasesA(AliasBuffer: win32more.Windows.Win32.Foundation.PSTR, AliasBufferLength: UInt32, ExeName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasesW(AliasBuffer: win32more.Windows.Win32.Foundation.PWSTR, AliasBufferLength: UInt32, ExeName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
GetConsoleAliases = UnicodeAlias('GetConsoleAliasesW')
@winfunctype('KERNEL32.dll')
def GetConsoleAliasExesA(ExeNameBuffer: win32more.Windows.Win32.Foundation.PSTR, ExeNameBufferLength: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleAliasExesW(ExeNameBuffer: win32more.Windows.Win32.Foundation.PWSTR, ExeNameBufferLength: UInt32) -> UInt32: ...
GetConsoleAliasExes = UnicodeAlias('GetConsoleAliasExesW')
@winfunctype('KERNEL32.dll')
def ExpungeConsoleCommandHistoryA(ExeName: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('KERNEL32.dll')
def ExpungeConsoleCommandHistoryW(ExeName: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
ExpungeConsoleCommandHistory = UnicodeAlias('ExpungeConsoleCommandHistoryW')
@winfunctype('KERNEL32.dll')
def SetConsoleNumberOfCommandsA(Number: UInt32, ExeName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetConsoleNumberOfCommandsW(Number: UInt32, ExeName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetConsoleNumberOfCommands = UnicodeAlias('SetConsoleNumberOfCommandsW')
@winfunctype('KERNEL32.dll')
def GetConsoleCommandHistoryLengthA(ExeName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleCommandHistoryLengthW(ExeName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
GetConsoleCommandHistoryLength = UnicodeAlias('GetConsoleCommandHistoryLengthW')
@winfunctype('KERNEL32.dll')
def GetConsoleCommandHistoryA(Commands: win32more.Windows.Win32.Foundation.PSTR, CommandBufferLength: UInt32, ExeName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetConsoleCommandHistoryW(Commands: win32more.Windows.Win32.Foundation.PWSTR, CommandBufferLength: UInt32, ExeName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
GetConsoleCommandHistory = UnicodeAlias('GetConsoleCommandHistoryW')
@winfunctype('KERNEL32.dll')
def GetConsoleProcessList(lpdwProcessList: POINTER(UInt32), dwProcessCount: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def ConsoleControl(Command: win32more.Windows.Win32.System.Console.CONSOLECONTROL, ConsoleInformation: VoidPtr, ConsoleInformationLength: UInt32) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('KERNEL32.dll')
def GetStdHandle(nStdHandle: win32more.Windows.Win32.System.Console.STD_HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def SetStdHandle(nStdHandle: win32more.Windows.Win32.System.Console.STD_HANDLE, hHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetStdHandleEx(nStdHandle: win32more.Windows.Win32.System.Console.STD_HANDLE, hHandle: win32more.Windows.Win32.Foundation.HANDLE, phPrevValue: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class CHAR_INFO(Structure):
    Char: _Char_e__Union
    Attributes: UInt16
    class _Char_e__Union(Union):
        UnicodeChar: Char
        AsciiChar: win32more.Windows.Win32.Foundation.CHAR
CONSOLECONTROL = Int32
Reserved1: win32more.Windows.Win32.System.Console.CONSOLECONTROL = 0
ConsoleNotifyConsoleApplication: win32more.Windows.Win32.System.Console.CONSOLECONTROL = 1
Reserved2: win32more.Windows.Win32.System.Console.CONSOLECONTROL = 2
ConsoleSetCaretInfo: win32more.Windows.Win32.System.Console.CONSOLECONTROL = 3
Reserved3: win32more.Windows.Win32.System.Console.CONSOLECONTROL = 4
ConsoleSetForeground: win32more.Windows.Win32.System.Console.CONSOLECONTROL = 5
ConsoleSetWindowOwner: win32more.Windows.Win32.System.Console.CONSOLECONTROL = 6
ConsoleEndTask: win32more.Windows.Win32.System.Console.CONSOLECONTROL = 7
class CONSOLEENDTASK(Structure):
    ProcessId: win32more.Windows.Win32.Foundation.HANDLE
    hwnd: win32more.Windows.Win32.Foundation.HWND
    ConsoleEventCode: UInt32
    ConsoleFlags: UInt32
class CONSOLESETFOREGROUND(Structure):
    hProcess: win32more.Windows.Win32.Foundation.HANDLE
    bForeground: win32more.Windows.Win32.Foundation.BOOL
class CONSOLEWINDOWOWNER(Structure):
    hwnd: win32more.Windows.Win32.Foundation.HWND
    ProcessId: UInt32
    ThreadId: UInt32
class CONSOLE_CARET_INFO(Structure):
    hwnd: win32more.Windows.Win32.Foundation.HWND
    rc: win32more.Windows.Win32.Foundation.RECT
CONSOLE_CHARACTER_ATTRIBUTES = UInt16
FOREGROUND_BLUE: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 1
FOREGROUND_GREEN: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 2
FOREGROUND_RED: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 4
FOREGROUND_INTENSITY: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 8
BACKGROUND_BLUE: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 16
BACKGROUND_GREEN: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 32
BACKGROUND_RED: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 64
BACKGROUND_INTENSITY: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 128
COMMON_LVB_LEADING_BYTE: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 256
COMMON_LVB_TRAILING_BYTE: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 512
COMMON_LVB_GRID_HORIZONTAL: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 1024
COMMON_LVB_GRID_LVERTICAL: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 2048
COMMON_LVB_GRID_RVERTICAL: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 4096
COMMON_LVB_REVERSE_VIDEO: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 16384
COMMON_LVB_UNDERSCORE: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 32768
COMMON_LVB_SBCSDBCS: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES = 768
class CONSOLE_CURSOR_INFO(Structure):
    dwSize: UInt32
    bVisible: win32more.Windows.Win32.Foundation.BOOL
class CONSOLE_FONT_INFO(Structure):
    nFont: UInt32
    dwFontSize: win32more.Windows.Win32.System.Console.COORD
class CONSOLE_FONT_INFOEX(Structure):
    cbSize: UInt32
    nFont: UInt32
    dwFontSize: win32more.Windows.Win32.System.Console.COORD
    FontFamily: UInt32
    FontWeight: UInt32
    FaceName: Char * 32
class CONSOLE_HISTORY_INFO(Structure):
    cbSize: UInt32
    HistoryBufferSize: UInt32
    NumberOfHistoryBuffers: UInt32
    dwFlags: UInt32
CONSOLE_MODE = UInt32
ENABLE_PROCESSED_INPUT: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 1
ENABLE_LINE_INPUT: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 2
ENABLE_ECHO_INPUT: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 4
ENABLE_WINDOW_INPUT: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 8
ENABLE_MOUSE_INPUT: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 16
ENABLE_INSERT_MODE: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 32
ENABLE_QUICK_EDIT_MODE: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 64
ENABLE_EXTENDED_FLAGS: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 128
ENABLE_AUTO_POSITION: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 256
ENABLE_VIRTUAL_TERMINAL_INPUT: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 512
ENABLE_PROCESSED_OUTPUT: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 1
ENABLE_WRAP_AT_EOL_OUTPUT: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 2
ENABLE_VIRTUAL_TERMINAL_PROCESSING: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 4
DISABLE_NEWLINE_AUTO_RETURN: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 8
ENABLE_LVB_GRID_WORLDWIDE: win32more.Windows.Win32.System.Console.CONSOLE_MODE = 16
class CONSOLE_PROCESS_INFO(Structure):
    dwProcessID: UInt32
    dwFlags: UInt32
class CONSOLE_READCONSOLE_CONTROL(Structure):
    nLength: UInt32
    nInitialChars: UInt32
    dwCtrlWakeupMask: UInt32
    dwControlKeyState: UInt32
class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    dwSize: win32more.Windows.Win32.System.Console.COORD
    dwCursorPosition: win32more.Windows.Win32.System.Console.COORD
    wAttributes: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES
    srWindow: win32more.Windows.Win32.System.Console.SMALL_RECT
    dwMaximumWindowSize: win32more.Windows.Win32.System.Console.COORD
class CONSOLE_SCREEN_BUFFER_INFOEX(Structure):
    cbSize: UInt32
    dwSize: win32more.Windows.Win32.System.Console.COORD
    dwCursorPosition: win32more.Windows.Win32.System.Console.COORD
    wAttributes: win32more.Windows.Win32.System.Console.CONSOLE_CHARACTER_ATTRIBUTES
    srWindow: win32more.Windows.Win32.System.Console.SMALL_RECT
    dwMaximumWindowSize: win32more.Windows.Win32.System.Console.COORD
    wPopupAttributes: UInt16
    bFullscreenSupported: win32more.Windows.Win32.Foundation.BOOL
    ColorTable: win32more.Windows.Win32.Foundation.COLORREF * 16
class CONSOLE_SELECTION_INFO(Structure):
    dwFlags: UInt32
    dwSelectionAnchor: win32more.Windows.Win32.System.Console.COORD
    srSelection: win32more.Windows.Win32.System.Console.SMALL_RECT
class COORD(Structure):
    X: Int16
    Y: Int16
class FOCUS_EVENT_RECORD(Structure):
    bSetFocus: win32more.Windows.Win32.Foundation.BOOL
HPCON = IntPtr
class INPUT_RECORD(Structure):
    EventType: UInt16
    Event: _Event_e__Union
    class _Event_e__Union(Union):
        KeyEvent: win32more.Windows.Win32.System.Console.KEY_EVENT_RECORD
        MouseEvent: win32more.Windows.Win32.System.Console.MOUSE_EVENT_RECORD
        WindowBufferSizeEvent: win32more.Windows.Win32.System.Console.WINDOW_BUFFER_SIZE_RECORD
        MenuEvent: win32more.Windows.Win32.System.Console.MENU_EVENT_RECORD
        FocusEvent: win32more.Windows.Win32.System.Console.FOCUS_EVENT_RECORD
class KEY_EVENT_RECORD(Structure):
    bKeyDown: win32more.Windows.Win32.Foundation.BOOL
    wRepeatCount: UInt16
    wVirtualKeyCode: UInt16
    wVirtualScanCode: UInt16
    uChar: _uChar_e__Union
    dwControlKeyState: UInt32
    class _uChar_e__Union(Union):
        UnicodeChar: Char
        AsciiChar: win32more.Windows.Win32.Foundation.CHAR
class MENU_EVENT_RECORD(Structure):
    dwCommandId: UInt32
class MOUSE_EVENT_RECORD(Structure):
    dwMousePosition: win32more.Windows.Win32.System.Console.COORD
    dwButtonState: UInt32
    dwControlKeyState: UInt32
    dwEventFlags: UInt32
@winfunctype_pointer
def PHANDLER_ROUTINE(CtrlType: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
class SMALL_RECT(Structure):
    Left: Int16
    Top: Int16
    Right: Int16
    Bottom: Int16
STD_HANDLE = UInt32
STD_INPUT_HANDLE: win32more.Windows.Win32.System.Console.STD_HANDLE = 4294967286
STD_OUTPUT_HANDLE: win32more.Windows.Win32.System.Console.STD_HANDLE = 4294967285
STD_ERROR_HANDLE: win32more.Windows.Win32.System.Console.STD_HANDLE = 4294967284
class WINDOW_BUFFER_SIZE_RECORD(Structure):
    dwSize: win32more.Windows.Win32.System.Console.COORD


make_ready(__name__)
