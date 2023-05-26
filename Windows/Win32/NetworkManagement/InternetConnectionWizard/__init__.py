from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.InternetConnectionWizard
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
def PFNSETSHELLNEXT(param0: Windows.Win32.Foundation.PSTR) -> UInt32: ...
make_head(_module, 'PFNCHECKCONNECTIONWIZARD')
make_head(_module, 'PFNSETSHELLNEXT')
