from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.NetShell
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
NETSH_ERROR_BASE: UInt32 = 15000
ERROR_NO_ENTRIES: UInt32 = 15000
ERROR_INVALID_SYNTAX: UInt32 = 15001
ERROR_PROTOCOL_NOT_IN_TRANSPORT: UInt32 = 15002
ERROR_NO_CHANGE: UInt32 = 15003
ERROR_CMD_NOT_FOUND: UInt32 = 15004
ERROR_ENTRY_PT_NOT_FOUND: UInt32 = 15005
ERROR_DLL_LOAD_FAILED: UInt32 = 15006
ERROR_INIT_DISPLAY: UInt32 = 15007
ERROR_TAG_ALREADY_PRESENT: UInt32 = 15008
ERROR_INVALID_OPTION_TAG: UInt32 = 15009
ERROR_NO_TAG: UInt32 = 15010
ERROR_MISSING_OPTION: UInt32 = 15011
ERROR_TRANSPORT_NOT_PRESENT: UInt32 = 15012
ERROR_SHOW_USAGE: UInt32 = 15013
ERROR_INVALID_OPTION_VALUE: UInt32 = 15014
ERROR_OKAY: UInt32 = 15015
ERROR_CONTINUE_IN_PARENT_CONTEXT: UInt32 = 15016
ERROR_SUPPRESS_OUTPUT: UInt32 = 15017
ERROR_HELPER_ALREADY_REGISTERED: UInt32 = 15018
ERROR_CONTEXT_ALREADY_REGISTERED: UInt32 = 15019
ERROR_PARSING_FAILURE: UInt32 = 15020
NETSH_ERROR_END: UInt32 = 15019
NS_GET_EVENT_IDS_FN_NAME: String = 'GetEventIds'
MAX_NAME_LEN: UInt32 = 48
NETSH_VERSION_50: UInt32 = 20480
NETSH_ARG_DELIMITER: String = '='
NETSH_CMD_DELIMITER: String = ' '
NETSH_MAX_TOKEN_LENGTH: UInt32 = 64
NETSH_MAX_CMD_TOKEN_LENGTH: UInt32 = 128
DEFAULT_CONTEXT_PRIORITY: UInt32 = 100
GET_RESOURCE_STRING_FN_NAME: String = 'GetResourceString'
@winfunctype('NETSH.dll')
def MatchEnumTag(hModule: Windows.Win32.Foundation.HANDLE, pwcArg: Windows.Win32.Foundation.PWSTR, dwNumArg: UInt32, pEnumTable: POINTER(Windows.Win32.NetworkManagement.NetShell.TOKEN_VALUE_head), pdwValue: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETSH.dll')
def MatchToken(pwszUserToken: Windows.Win32.Foundation.PWSTR, pwszCmdToken: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('NETSH.dll')
def PreprocessCommand(hModule: Windows.Win32.Foundation.HANDLE, ppwcArguments: POINTER(Windows.Win32.Foundation.PWSTR), dwCurrentIndex: UInt32, dwArgCount: UInt32, pttTags: POINTER(Windows.Win32.NetworkManagement.NetShell.TAG_TYPE_head), dwTagCount: UInt32, dwMinArgs: UInt32, dwMaxArgs: UInt32, pdwTagType: POINTER(UInt32)) -> UInt32: ...
@cfunctype('NETSH.dll')
def PrintError(hModule: Windows.Win32.Foundation.HANDLE, dwErrId: UInt32) -> UInt32: ...
@cfunctype('NETSH.dll')
def PrintMessageFromModule(hModule: Windows.Win32.Foundation.HANDLE, dwMsgId: UInt32) -> UInt32: ...
@cfunctype('NETSH.dll')
def PrintMessage(pwszFormat: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('NETSH.dll')
def RegisterContext(pChildContext: POINTER(Windows.Win32.NetworkManagement.NetShell.NS_CONTEXT_ATTRIBUTES_head)) -> UInt32: ...
@winfunctype('NETSH.dll')
def RegisterHelper(pguidParentContext: POINTER(Guid), pfnRegisterSubContext: POINTER(Windows.Win32.NetworkManagement.NetShell.NS_HELPER_ATTRIBUTES_head)) -> UInt32: ...
class CMD_ENTRY(Structure):
    pwszCmdToken: Windows.Win32.Foundation.PWSTR
    pfnCmdHandler: Windows.Win32.NetworkManagement.NetShell.PFN_HANDLE_CMD
    dwShortCmdHelpToken: UInt32
    dwCmdHlpToken: UInt32
    dwFlags: UInt32
    pOsVersionCheck: Windows.Win32.NetworkManagement.NetShell.PNS_OSVERSIONCHECK
class CMD_GROUP_ENTRY(Structure):
    pwszCmdGroupToken: Windows.Win32.Foundation.PWSTR
    dwShortCmdHelpToken: UInt32
    ulCmdGroupSize: UInt32
    dwFlags: UInt32
    pCmdGroup: POINTER(Windows.Win32.NetworkManagement.NetShell.CMD_ENTRY_head)
    pOsVersionCheck: Windows.Win32.NetworkManagement.NetShell.PNS_OSVERSIONCHECK
NS_CMD_FLAGS = Int32
CMD_FLAG_PRIVATE: NS_CMD_FLAGS = 1
CMD_FLAG_INTERACTIVE: NS_CMD_FLAGS = 2
CMD_FLAG_LOCAL: NS_CMD_FLAGS = 8
CMD_FLAG_ONLINE: NS_CMD_FLAGS = 16
CMD_FLAG_HIDDEN: NS_CMD_FLAGS = 32
CMD_FLAG_LIMIT_MASK: NS_CMD_FLAGS = 65535
CMD_FLAG_PRIORITY: NS_CMD_FLAGS = -2147483648
class NS_CONTEXT_ATTRIBUTES(Structure):
    Anonymous: _Anonymous_e__Union
    pwszContext: Windows.Win32.Foundation.PWSTR
    guidHelper: Guid
    dwFlags: UInt32
    ulPriority: UInt32
    ulNumTopCmds: UInt32
    pTopCmds: POINTER(Windows.Win32.NetworkManagement.NetShell.CMD_ENTRY_head)
    ulNumGroups: UInt32
    pCmdGroups: POINTER(Windows.Win32.NetworkManagement.NetShell.CMD_GROUP_ENTRY_head)
    pfnCommitFn: Windows.Win32.NetworkManagement.NetShell.PNS_CONTEXT_COMMIT_FN
    pfnDumpFn: Windows.Win32.NetworkManagement.NetShell.PNS_CONTEXT_DUMP_FN
    pfnConnectFn: Windows.Win32.NetworkManagement.NetShell.PNS_CONTEXT_CONNECT_FN
    pReserved: c_void_p
    pfnOsVersionCheck: Windows.Win32.NetworkManagement.NetShell.PNS_OSVERSIONCHECK
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        _ullAlign: UInt64
        class _Anonymous_e__Struct(Structure):
            dwVersion: UInt32
            dwReserved: UInt32
NS_EVENTS = Int32
NS_EVENT_LOOP: NS_EVENTS = 65536
NS_EVENT_LAST_N: NS_EVENTS = 1
NS_EVENT_LAST_SECS: NS_EVENTS = 2
NS_EVENT_FROM_N: NS_EVENTS = 4
NS_EVENT_FROM_START: NS_EVENTS = 8
class NS_HELPER_ATTRIBUTES(Structure):
    Anonymous: _Anonymous_e__Union
    guidHelper: Guid
    pfnStart: Windows.Win32.NetworkManagement.NetShell.PNS_HELPER_START_FN
    pfnStop: Windows.Win32.NetworkManagement.NetShell.PNS_HELPER_STOP_FN
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        _ullAlign: UInt64
        class _Anonymous_e__Struct(Structure):
            dwVersion: UInt32
            dwReserved: UInt32
NS_MODE_CHANGE = Int32
NETSH_COMMIT: NS_MODE_CHANGE = 0
NETSH_UNCOMMIT: NS_MODE_CHANGE = 1
NETSH_FLUSH: NS_MODE_CHANGE = 2
NETSH_COMMIT_STATE: NS_MODE_CHANGE = 3
NETSH_SAVE: NS_MODE_CHANGE = 4
NS_REQS = Int32
NS_REQ_ZERO: NS_REQS = 0
NS_REQ_PRESENT: NS_REQS = 1
NS_REQ_ALLOW_MULTIPLE: NS_REQS = 2
NS_REQ_ONE_OR_MORE: NS_REQS = 3
@winfunctype_pointer
def PFN_HANDLE_CMD(pwszMachine: Windows.Win32.Foundation.PWSTR, ppwcArguments: POINTER(Windows.Win32.Foundation.PWSTR), dwCurrentIndex: UInt32, dwArgCount: UInt32, dwFlags: UInt32, pvData: c_void_p, pbDone: POINTER(Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype_pointer
def PGET_RESOURCE_STRING_FN(dwMsgID: UInt32, lpBuffer: Windows.Win32.Foundation.PWSTR, nBufferMax: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_CONTEXT_COMMIT_FN(dwAction: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_CONTEXT_CONNECT_FN(pwszMachine: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def PNS_CONTEXT_DUMP_FN(pwszRouter: Windows.Win32.Foundation.PWSTR, ppwcArguments: POINTER(Windows.Win32.Foundation.PWSTR), dwArgCount: UInt32, pvData: c_void_p) -> UInt32: ...
@winfunctype_pointer
def PNS_DLL_INIT_FN(dwNetshVersion: UInt32, pReserved: c_void_p) -> UInt32: ...
@winfunctype_pointer
def PNS_DLL_STOP_FN(dwReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_HELPER_START_FN(pguidParent: POINTER(Guid), dwVersion: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_HELPER_STOP_FN(dwReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_OSVERSIONCHECK(CIMOSType: UInt32, CIMOSProductSuite: UInt32, CIMOSVersion: Windows.Win32.Foundation.PWSTR, CIMOSBuildNumber: Windows.Win32.Foundation.PWSTR, CIMServicePackMajorVersion: Windows.Win32.Foundation.PWSTR, CIMServicePackMinorVersion: Windows.Win32.Foundation.PWSTR, uiReserved: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.BOOL: ...
class TAG_TYPE(Structure):
    pwszTag: Windows.Win32.Foundation.PWSTR
    dwRequired: UInt32
    bPresent: Windows.Win32.Foundation.BOOL
class TOKEN_VALUE(Structure):
    pwszToken: Windows.Win32.Foundation.PWSTR
    dwValue: UInt32
make_head(_module, 'CMD_ENTRY')
make_head(_module, 'CMD_GROUP_ENTRY')
make_head(_module, 'NS_CONTEXT_ATTRIBUTES')
make_head(_module, 'NS_HELPER_ATTRIBUTES')
make_head(_module, 'PFN_HANDLE_CMD')
make_head(_module, 'PGET_RESOURCE_STRING_FN')
make_head(_module, 'PNS_CONTEXT_COMMIT_FN')
make_head(_module, 'PNS_CONTEXT_CONNECT_FN')
make_head(_module, 'PNS_CONTEXT_DUMP_FN')
make_head(_module, 'PNS_DLL_INIT_FN')
make_head(_module, 'PNS_DLL_STOP_FN')
make_head(_module, 'PNS_HELPER_START_FN')
make_head(_module, 'PNS_HELPER_STOP_FN')
make_head(_module, 'PNS_OSVERSIONCHECK')
make_head(_module, 'TAG_TYPE')
make_head(_module, 'TOKEN_VALUE')
__all__ = [
    "CMD_ENTRY",
    "CMD_FLAG_HIDDEN",
    "CMD_FLAG_INTERACTIVE",
    "CMD_FLAG_LIMIT_MASK",
    "CMD_FLAG_LOCAL",
    "CMD_FLAG_ONLINE",
    "CMD_FLAG_PRIORITY",
    "CMD_FLAG_PRIVATE",
    "CMD_GROUP_ENTRY",
    "DEFAULT_CONTEXT_PRIORITY",
    "ERROR_CMD_NOT_FOUND",
    "ERROR_CONTEXT_ALREADY_REGISTERED",
    "ERROR_CONTINUE_IN_PARENT_CONTEXT",
    "ERROR_DLL_LOAD_FAILED",
    "ERROR_ENTRY_PT_NOT_FOUND",
    "ERROR_HELPER_ALREADY_REGISTERED",
    "ERROR_INIT_DISPLAY",
    "ERROR_INVALID_OPTION_TAG",
    "ERROR_INVALID_OPTION_VALUE",
    "ERROR_INVALID_SYNTAX",
    "ERROR_MISSING_OPTION",
    "ERROR_NO_CHANGE",
    "ERROR_NO_ENTRIES",
    "ERROR_NO_TAG",
    "ERROR_OKAY",
    "ERROR_PARSING_FAILURE",
    "ERROR_PROTOCOL_NOT_IN_TRANSPORT",
    "ERROR_SHOW_USAGE",
    "ERROR_SUPPRESS_OUTPUT",
    "ERROR_TAG_ALREADY_PRESENT",
    "ERROR_TRANSPORT_NOT_PRESENT",
    "GET_RESOURCE_STRING_FN_NAME",
    "MAX_NAME_LEN",
    "MatchEnumTag",
    "MatchToken",
    "NETSH_ARG_DELIMITER",
    "NETSH_CMD_DELIMITER",
    "NETSH_COMMIT",
    "NETSH_COMMIT_STATE",
    "NETSH_ERROR_BASE",
    "NETSH_ERROR_END",
    "NETSH_FLUSH",
    "NETSH_MAX_CMD_TOKEN_LENGTH",
    "NETSH_MAX_TOKEN_LENGTH",
    "NETSH_SAVE",
    "NETSH_UNCOMMIT",
    "NETSH_VERSION_50",
    "NS_CMD_FLAGS",
    "NS_CONTEXT_ATTRIBUTES",
    "NS_EVENTS",
    "NS_EVENT_FROM_N",
    "NS_EVENT_FROM_START",
    "NS_EVENT_LAST_N",
    "NS_EVENT_LAST_SECS",
    "NS_EVENT_LOOP",
    "NS_GET_EVENT_IDS_FN_NAME",
    "NS_HELPER_ATTRIBUTES",
    "NS_MODE_CHANGE",
    "NS_REQS",
    "NS_REQ_ALLOW_MULTIPLE",
    "NS_REQ_ONE_OR_MORE",
    "NS_REQ_PRESENT",
    "NS_REQ_ZERO",
    "PFN_HANDLE_CMD",
    "PGET_RESOURCE_STRING_FN",
    "PNS_CONTEXT_COMMIT_FN",
    "PNS_CONTEXT_CONNECT_FN",
    "PNS_CONTEXT_DUMP_FN",
    "PNS_DLL_INIT_FN",
    "PNS_DLL_STOP_FN",
    "PNS_HELPER_START_FN",
    "PNS_HELPER_STOP_FN",
    "PNS_OSVERSIONCHECK",
    "PreprocessCommand",
    "PrintError",
    "PrintMessage",
    "PrintMessageFromModule",
    "RegisterContext",
    "RegisterHelper",
    "TAG_TYPE",
    "TOKEN_VALUE",
]
_arch_optional = [
]
