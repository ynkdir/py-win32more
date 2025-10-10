from __future__ import annotations

from ctypes import wstring_at

from ._win32 import FAILED, String, UInt32, UIntPtr, WinError
from ._win32api import HSTRING, WindowsCreateString, WindowsDeleteString, WindowsGetStringLen, WindowsGetStringRawBuffer


class hstr(HSTRING):
    def __init__(self, obj=None, own=False):
        if obj is None:
            hs = HSTRING(0)
        elif isinstance(obj, HSTRING):
            hs = obj
        elif isinstance(obj, String):
            hs = _windows_create_string(obj.value)
        elif isinstance(obj, str):
            hs = _windows_create_string(obj)
        else:
            raise ValueError(obj)
        # https://github.com/python/cpython/issues/73456
        # super().__init__(hs.value)
        self.value = hs.value
        self._own = own

    def __del__(self):
        if getattr(self, "_own", False):
            self.clear()

    def clear(self):
        if self:
            hr = WindowsDeleteString(self)
            if FAILED(hr):
                raise WinError(hr)
            self.value = 0

    def __len__(self):
        return WindowsGetStringLen(self)

    def __str__(self):
        return _windows_get_string_raw_buffer(self)

    def __int__(self):
        return UIntPtr.from_buffer(self).value

    @classmethod
    def from_param(cls, obj):
        if isinstance(obj, String):
            return cls(obj, own=True)
        elif isinstance(obj, str):
            return cls(obj, own=True)
        else:
            return cls(obj, own=False)


def _windows_create_string(s: str) -> HSTRING:
    hs = HSTRING()
    hr = WindowsCreateString(s, len(s), hs)
    if FAILED(hr):
        raise WinError(hr)
    return hs


def _windows_get_string_raw_buffer(hs: HSTRING) -> str:
    length = UInt32()
    bufaddr = WindowsGetStringRawBuffer(hs, length, _as_intptr=True)
    return wstring_at(bufaddr, length.value)
