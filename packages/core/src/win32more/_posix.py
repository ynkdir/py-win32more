"""Backend for Linux and macOS: vtable calls into shared libraries that export COM interfaces, such as DXC.

There is no COM runtime (no CoCreateInstance, apartments, error info or WinRT).
"foo.dll" is loaded as "libfoo.so" (".dylib" on macOS); windll.register_library() sets a path.
The BSTR and CoTaskMem functions follow DXC's WinAdapter: malloc/free, 4-byte byte-length
prefix, wchar_t units (UTF-32).  DXC's BOOL is 1 byte and LONG/ULONG are 8 bytes on LP64,
which the generated bindings do not account for.
"""

import platform
import sys
from ctypes import CDLL, c_size_t, c_uint32, c_void_p, c_wchar, cast, memmove, memset, sizeof, wstring_at
from functools import cache

from ._winfunctype import WINFUNCTYPE  # noqa: F401

_machine = platform.machine().lower()
if _machine in ("x86_64", "amd64"):
    ARCH = "X64"
elif _machine in ("arm64", "aarch64"):
    ARCH = "ARM64"
else:
    raise RuntimeError(f"{platform.machine()} is not supported")


class LibraryLoader:
    def __init__(self):
        self._registered = {}
        self._loaded = {}

    def register_library(self, dllname, path):
        self._loaded.pop(dllname.lower(), None)
        self._registered[dllname.lower()] = path

    def candidates(self, dllname):
        key = dllname.lower()
        if key in self._registered:
            return [self._registered[key]]
        stem = dllname[:-4] if key.endswith(".dll") else dllname
        return [f"lib{stem}.dylib", f"lib{stem}.so"] if sys.platform == "darwin" else [f"lib{stem}.so"]

    def __getitem__(self, dllname):
        key = dllname.lower()
        if key not in self._loaded:
            self._loaded[key] = self._open(self.candidates(dllname))
        return self._loaded[key]

    @staticmethod
    def _open(candidates):
        for path in candidates:
            try:
                return CDLL(path)
            except OSError as e:
                error = e
        raise error


windll = LibraryLoader()


def FormatError(code):
    return f"error 0x{code & 0xFFFFFFFF:08X}"


def WinError(code, descr=None):
    # No GetLastError() here, so code is required.
    e = OSError(code, FormatError(code) if descr is None else descr)
    e.winerror = code
    return e


@cache
def _libc():
    libc = CDLL(None if sys.platform != "win32" else "msvcrt")
    libc.malloc.restype = c_void_p
    libc.malloc.argtypes = [c_size_t]
    libc.free.restype = None
    libc.free.argtypes = [c_void_p]
    return libc


def _address(p):
    if p is None or isinstance(p, int):
        return p or 0
    return cast(p, c_void_p).value or 0


def SysAllocStringLen(strIn, ui, _as_intptr=False):
    nbytes = ui * sizeof(c_wchar)
    buf = _libc().malloc(4 + nbytes + sizeof(c_wchar))
    if not buf:
        return 0 if _as_intptr else None
    c_uint32.from_address(buf).value = nbytes
    p = buf + 4
    memset(p, 0, nbytes + sizeof(c_wchar))
    if strIn is not None:
        memmove(p, strIn, nbytes)
    return p if _as_intptr else wstring_at(p, ui)


def SysFreeString(bstrString):
    p = _address(bstrString)
    if p:
        _libc().free(p - 4)


def SysStringLen(pbstr):
    p = _address(pbstr)
    return c_uint32.from_address(p - 4).value // sizeof(c_wchar) if p else 0


def CoTaskMemAlloc(cb):
    return _libc().malloc(cb)


def CoTaskMemFree(pv):
    _libc().free(_address(pv))
