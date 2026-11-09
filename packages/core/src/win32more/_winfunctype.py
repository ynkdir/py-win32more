"""WINFUNCTYPE() with the COM method prototype form functype(vtbl_index, name, ...) for non-Windows ctypes."""

from ctypes import CFUNCTYPE, POINTER, c_void_p, cast


def WINFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False):
    def __new__(cls, *args):
        if len(args) >= 2 and isinstance(args[0], int):
            return ComMethod(restype, argtypes, use_errno, use_last_error, *args)
        return functype_new(cls, *args)

    functype = CFUNCTYPE(restype, *argtypes, use_errno=use_errno, use_last_error=use_last_error)
    if functype.__new__.__module__ != __name__:
        functype_new = functype.__new__
        functype.__new__ = __new__
    return functype


class ComMethod:
    def __init__(self, restype, argtypes, use_errno, use_last_error, vtbl_index, name, paramflags=None, iid=None):
        self._vtbl_index = vtbl_index
        self._functype = CFUNCTYPE(restype, c_void_p, *argtypes, use_errno=use_errno, use_last_error=use_last_error)

    def __call__(self, this, *args, **kwargs):
        pvtbl = cast(this, POINTER(POINTER(c_void_p)))
        func = self._functype(pvtbl[0][self._vtbl_index])
        # WORKAROUND: return_length and return are passed as kwargs.
        _args = list(args) + list(kwargs.values())
        return func(this, *_args)
