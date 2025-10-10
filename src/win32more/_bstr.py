from __future__ import annotations

from ctypes import wstring_at

from ._win32 import UIntPtr
from ._win32api import BSTR, SysAllocStringLen, SysFreeString, SysStringLen


class bstr(BSTR):
    def __init__(self, obj=None, own=False):
        if obj is None:
            bs = 0
        elif isinstance(obj, str):
            bs = SysAllocStringLen(obj, len(obj), _as_intptr=True)
        else:
            raise ValueError(obj)
        self.value = bs
        self._own = own

    def __del__(self):
        if getattr(self, "_own", False):
            self.clear()

    def clear(self):
        if self.value:
            SysFreeString(self)
            self.value = 0

    def __len__(self):
        return SysStringLen(self)

    def __str__(self):
        return wstring_at(self, len(self))

    def __int__(self):
        return UIntPtr.from_buffer(self).value
