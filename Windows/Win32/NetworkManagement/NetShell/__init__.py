from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.NetShell
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
@cfunctype('NETSH.dll', variadic=True)
def PrintError(hModule: Windows.Win32.Foundation.HANDLE, dwErrId: UInt32, *__arglist) -> UInt32: ...
@cfunctype('NETSH.dll', variadic=True)
def PrintMessageFromModule(hModule: Windows.Win32.Foundation.HANDLE, dwMsgId: UInt32, *__arglist) -> UInt32: ...
@cfunctype('NETSH.dll', variadic=True)
def PrintMessage(pwszFormat: Windows.Win32.Foundation.PWSTR, *__arglist) -> UInt32: ...
@winfunctype('NETSH.dll')
def RegisterContext(pChildContext: POINTER(Windows.Win32.NetworkManagement.NetShell.NS_CONTEXT_ATTRIBUTES_head)) -> UInt32: ...
@winfunctype('NETSH.dll')
def RegisterHelper(pguidParentContext: POINTER(Guid), pfnRegisterSubContext: POINTER(Windows.Win32.NetworkManagement.NetShell.NS_HELPER_ATTRIBUTES_head)) -> UInt32: ...
class CMD_ENTRY(EasyCastStructure):
    pwszCmdToken: Windows.Win32.Foundation.PWSTR
    pfnCmdHandler: Windows.Win32.NetworkManagement.NetShell.PFN_HANDLE_CMD
    dwShortCmdHelpToken: UInt32
    dwCmdHlpToken: UInt32
    dwFlags: UInt32
    pOsVersionCheck: Windows.Win32.NetworkManagement.NetShell.PNS_OSVERSIONCHECK
    pfnCustomHelpFn: Windows.Win32.NetworkManagement.NetShell.PFN_CUSTOM_HELP
class CMD_GROUP_ENTRY(EasyCastStructure):
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
class NS_CONTEXT_ATTRIBUTES(EasyCastStructure):
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
    pReserved: VoidPtr
    pfnOsVersionCheck: Windows.Win32.NetworkManagement.NetShell.PNS_OSVERSIONCHECK
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        _ullAlign: UInt64
        class _Anonymous_e__Struct(EasyCastStructure):
            dwVersion: UInt32
            dwReserved: UInt32
NS_EVENTS = Int32
NS_EVENT_LOOP: NS_EVENTS = 65536
NS_EVENT_LAST_N: NS_EVENTS = 1
NS_EVENT_LAST_SECS: NS_EVENTS = 2
NS_EVENT_FROM_N: NS_EVENTS = 4
NS_EVENT_FROM_START: NS_EVENTS = 8
class NS_HELPER_ATTRIBUTES(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    guidHelper: Guid
    pfnStart: Windows.Win32.NetworkManagement.NetShell.PNS_HELPER_START_FN
    pfnStop: Windows.Win32.NetworkManagement.NetShell.PNS_HELPER_STOP_FN
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        _ullAlign: UInt64
        class _Anonymous_e__Struct(EasyCastStructure):
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
def PFN_CUSTOM_HELP(hModule: Windows.Win32.Foundation.HANDLE, pwszCmdToken: Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype_pointer
def PFN_HANDLE_CMD(pwszMachine: Windows.Win32.Foundation.PWSTR, ppwcArguments: POINTER(Windows.Win32.Foundation.PWSTR), dwCurrentIndex: UInt32, dwArgCount: UInt32, dwFlags: UInt32, pvData: VoidPtr, pbDone: POINTER(Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype_pointer
def PGET_RESOURCE_STRING_FN(dwMsgID: UInt32, lpBuffer: Windows.Win32.Foundation.PWSTR, nBufferMax: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_CONTEXT_COMMIT_FN(dwAction: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_CONTEXT_CONNECT_FN(pwszMachine: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def PNS_CONTEXT_DUMP_FN(pwszRouter: Windows.Win32.Foundation.PWSTR, ppwcArguments: POINTER(Windows.Win32.Foundation.PWSTR), dwArgCount: UInt32, pvData: VoidPtr) -> UInt32: ...
@winfunctype_pointer
def PNS_DLL_INIT_FN(dwNetshVersion: UInt32, pReserved: VoidPtr) -> UInt32: ...
@winfunctype_pointer
def PNS_DLL_STOP_FN(dwReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_HELPER_START_FN(pguidParent: POINTER(Guid), dwVersion: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_HELPER_STOP_FN(dwReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_OSVERSIONCHECK(CIMOSType: UInt32, CIMOSProductSuite: UInt32, CIMOSVersion: Windows.Win32.Foundation.PWSTR, CIMOSBuildNumber: Windows.Win32.Foundation.PWSTR, CIMServicePackMajorVersion: Windows.Win32.Foundation.PWSTR, CIMServicePackMinorVersion: Windows.Win32.Foundation.PWSTR, uiReserved: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.BOOL: ...
class TAG_TYPE(EasyCastStructure):
    pwszTag: Windows.Win32.Foundation.PWSTR
    dwRequired: UInt32
    bPresent: Windows.Win32.Foundation.BOOL
class TOKEN_VALUE(EasyCastStructure):
    pwszToken: Windows.Win32.Foundation.PWSTR
    dwValue: UInt32
make_head(_module, 'CMD_ENTRY')
make_head(_module, 'CMD_GROUP_ENTRY')
make_head(_module, 'NS_CONTEXT_ATTRIBUTES')
make_head(_module, 'NS_HELPER_ATTRIBUTES')
make_head(_module, 'PFN_CUSTOM_HELP')
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
