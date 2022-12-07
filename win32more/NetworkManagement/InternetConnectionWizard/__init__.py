from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.NetworkManagement.InternetConnectionWizard
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
ICW_REGPATHSETTINGS: String = 'Software\\Microsoft\\Internet Connection Wizard'
ICW_REGKEYCOMPLETED: String = 'Completed'
ICW_MAX_ACCTNAME: UInt32 = 256
ICW_MAX_PASSWORD: UInt32 = 256
ICW_MAX_LOGONNAME: UInt32 = 256
ICW_MAX_SERVERNAME: UInt32 = 64
ICW_MAX_RASNAME: UInt32 = 256
ICW_MAX_EMAILNAME: UInt32 = 64
ICW_MAX_EMAILADDR: UInt32 = 128
ICW_CHECKSTATUS: UInt32 = 1
ICW_LAUNCHFULL: UInt32 = 256
ICW_LAUNCHMANUAL: UInt32 = 512
ICW_USE_SHELLNEXT: UInt32 = 1024
ICW_FULL_SMARTSTART: UInt32 = 2048
ICW_FULLPRESENT: UInt32 = 1
ICW_MANUALPRESENT: UInt32 = 2
ICW_ALREADYRUN: UInt32 = 4
ICW_LAUNCHEDFULL: UInt32 = 256
ICW_LAUNCHEDMANUAL: UInt32 = 512
ICW_USEDEFAULTS: UInt32 = 1
@winfunctype_pointer
def PFNCHECKCONNECTIONWIZARD(param0: UInt32, param1: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PFNSETSHELLNEXT(param0: win32more.Foundation.PSTR) -> UInt32: ...
make_head(_module, 'PFNCHECKCONNECTIONWIZARD')
make_head(_module, 'PFNSETSHELLNEXT')
__all__ = [
    "ICW_ALREADYRUN",
    "ICW_CHECKSTATUS",
    "ICW_FULLPRESENT",
    "ICW_FULL_SMARTSTART",
    "ICW_LAUNCHEDFULL",
    "ICW_LAUNCHEDMANUAL",
    "ICW_LAUNCHFULL",
    "ICW_LAUNCHMANUAL",
    "ICW_MANUALPRESENT",
    "ICW_MAX_ACCTNAME",
    "ICW_MAX_EMAILADDR",
    "ICW_MAX_EMAILNAME",
    "ICW_MAX_LOGONNAME",
    "ICW_MAX_PASSWORD",
    "ICW_MAX_RASNAME",
    "ICW_MAX_SERVERNAME",
    "ICW_REGKEYCOMPLETED",
    "ICW_REGPATHSETTINGS",
    "ICW_USEDEFAULTS",
    "ICW_USE_SHELLNEXT",
    "PFNCHECKCONNECTIONWIZARD",
    "PFNSETSHELLNEXT",
]
