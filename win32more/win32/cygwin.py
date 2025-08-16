import platform
from ctypes import CFUNCTYPE, POINTER, c_char_p, c_uint, c_void_p, c_wchar_p, cast, cdll, pointer

if platform.machine() != "x86_64":
    raise RuntimeError(f"{platform.machine()} is not supported")

ARCH = "X64"

windll = cdll


def MAKELANGID(p, s):
    return (s << 10) | p


def FormatError(code):
    from win32more.Windows.Win32.Foundation import LocalFree
    from win32more.Windows.Win32.System.Diagnostics.Debug import (
        FORMAT_MESSAGE_ALLOCATE_BUFFER,
        FORMAT_MESSAGE_FROM_SYSTEM,
        FORMAT_MESSAGE_IGNORE_INSERTS,
        FormatMessageW,
    )
    from win32more.Windows.Win32.System.SystemServices import LANG_NEUTRAL, SUBLANG_NEUTRAL

    lpMsgBuf = c_wchar_p()
    n = FormatMessageW(
        FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS,
        None,
        code,
        MAKELANGID(LANG_NEUTRAL, SUBLANG_NEUTRAL),
        cast(pointer(lpMsgBuf), c_wchar_p),
        0,
        None,
    )
    if n == 0:
        return "<no description>"
    msg = lpMsgBuf.value.rstrip()
    LocalFree(lpMsgBuf)
    return msg


def WinError(code=None, descr=None):
    from win32more.Windows.Win32.Foundation import GetLastError

    if code is None:
        code = GetLastError()
    if descr is None:
        descr = FormatError(code).strip()
    # Cygwin version doesn't have 4th winerror argument.
    # OSError(None, descr, None, code)
    return OSError(code, descr)


def WINFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False):
    def __new__(cls, *args):
        if len(args) >= 2 and isinstance(args[0], int):
            return _ComMethod(restype, argtypes, use_errno, use_last_error, *args)
        return functype_new(cls, *args)

    functype = CFUNCTYPE(restype, *argtypes, use_errno=use_errno, use_last_error=use_last_error)
    functype_new = functype.__new__
    functype.__new__ = __new__
    return functype


class _ComMethod:
    def __init__(self, restype, argtypes, use_errno, use_last_error, vtbl_index, name, paramflags=None, iid=None):
        self._vtbl_index = vtbl_index
        self._functype = CFUNCTYPE(restype, c_void_p, *argtypes, use_errno=use_errno, use_last_error=use_last_error)

    def __call__(self, this, *args, **kwargs):
        pvtbl = cast(this, POINTER(POINTER(c_void_p)))
        func = self._functype(pvtbl[0][self._vtbl_index])
        # WORKAROUND: return_length and return are passed as kwargs.
        _args = list(args) + list(kwargs.values())
        return func(this, *_args)


CCP_POSIX_TO_WIN_W = 1

try:
    cygwin1 = cdll.LoadLibrary("cygwin1.dll")
except OSError:
    cygwin1 = cdll.LoadLibrary("msys-2.0.dll")

cygwin_create_path = cygwin1.cygwin_create_path
cygwin_create_path.restype = c_void_p
cygwin_create_path.argtypes = [c_uint, c_void_p]

free = cygwin1.free
free.restype = None
free.argtypes = [c_void_p]


def posix_to_win(posix_path: str) -> str:
    p = cygwin_create_path(CCP_POSIX_TO_WIN_W, c_char_p(posix_path.encode("utf-8")))
    win_path = c_wchar_p(p).value
    free(p)
    return win_path
