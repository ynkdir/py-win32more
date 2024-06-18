from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.InternetConnectionWizard
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
def PFNSETSHELLNEXT(param0: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...


make_ready(__name__)
