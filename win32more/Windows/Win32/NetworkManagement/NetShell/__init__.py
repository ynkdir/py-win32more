from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.NetShell
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
def MatchEnumTag(hModule: win32more.Windows.Win32.Foundation.HANDLE, pwcArg: win32more.Windows.Win32.Foundation.PWSTR, dwNumArg: UInt32, pEnumTable: POINTER(win32more.Windows.Win32.NetworkManagement.NetShell.TOKEN_VALUE), pdwValue: POINTER(UInt32)) -> UInt32: ...
@winfunctype('NETSH.dll')
def MatchToken(pwszUserToken: win32more.Windows.Win32.Foundation.PWSTR, pwszCmdToken: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('NETSH.dll')
def PreprocessCommand(hModule: win32more.Windows.Win32.Foundation.HANDLE, ppwcArguments: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwCurrentIndex: UInt32, dwArgCount: UInt32, pttTags: POINTER(win32more.Windows.Win32.NetworkManagement.NetShell.TAG_TYPE), dwTagCount: UInt32, dwMinArgs: UInt32, dwMaxArgs: UInt32, pdwTagType: POINTER(UInt32)) -> UInt32: ...
@cfunctype('NETSH.dll', variadic=True)
def PrintError(hModule: win32more.Windows.Win32.Foundation.HANDLE, dwErrId: UInt32, *__arglist) -> UInt32: ...
@cfunctype('NETSH.dll', variadic=True)
def PrintMessageFromModule(hModule: win32more.Windows.Win32.Foundation.HANDLE, dwMsgId: UInt32, *__arglist) -> UInt32: ...
@cfunctype('NETSH.dll', variadic=True)
def PrintMessage(pwszFormat: win32more.Windows.Win32.Foundation.PWSTR, *__arglist) -> UInt32: ...
@winfunctype('NETSH.dll')
def RegisterContext(pChildContext: POINTER(win32more.Windows.Win32.NetworkManagement.NetShell.NS_CONTEXT_ATTRIBUTES)) -> UInt32: ...
@winfunctype('NETSH.dll')
def RegisterHelper(pguidParentContext: POINTER(Guid), pfnRegisterSubContext: POINTER(win32more.Windows.Win32.NetworkManagement.NetShell.NS_HELPER_ATTRIBUTES)) -> UInt32: ...
class CMD_ENTRY(Structure):
    pwszCmdToken: win32more.Windows.Win32.Foundation.PWSTR
    pfnCmdHandler: win32more.Windows.Win32.NetworkManagement.NetShell.PFN_HANDLE_CMD
    dwShortCmdHelpToken: UInt32
    dwCmdHlpToken: UInt32
    dwFlags: UInt32
    pOsVersionCheck: win32more.Windows.Win32.NetworkManagement.NetShell.PNS_OSVERSIONCHECK
    pfnCustomHelpFn: win32more.Windows.Win32.NetworkManagement.NetShell.PFN_CUSTOM_HELP
class CMD_GROUP_ENTRY(Structure):
    pwszCmdGroupToken: win32more.Windows.Win32.Foundation.PWSTR
    dwShortCmdHelpToken: UInt32
    ulCmdGroupSize: UInt32
    dwFlags: UInt32
    pCmdGroup: POINTER(win32more.Windows.Win32.NetworkManagement.NetShell.CMD_ENTRY)
    pOsVersionCheck: win32more.Windows.Win32.NetworkManagement.NetShell.PNS_OSVERSIONCHECK
NS_CMD_FLAGS = Int32
CMD_FLAG_PRIVATE: win32more.Windows.Win32.NetworkManagement.NetShell.NS_CMD_FLAGS = 1
CMD_FLAG_INTERACTIVE: win32more.Windows.Win32.NetworkManagement.NetShell.NS_CMD_FLAGS = 2
CMD_FLAG_LOCAL: win32more.Windows.Win32.NetworkManagement.NetShell.NS_CMD_FLAGS = 8
CMD_FLAG_ONLINE: win32more.Windows.Win32.NetworkManagement.NetShell.NS_CMD_FLAGS = 16
CMD_FLAG_HIDDEN: win32more.Windows.Win32.NetworkManagement.NetShell.NS_CMD_FLAGS = 32
CMD_FLAG_LIMIT_MASK: win32more.Windows.Win32.NetworkManagement.NetShell.NS_CMD_FLAGS = 65535
CMD_FLAG_PRIORITY: win32more.Windows.Win32.NetworkManagement.NetShell.NS_CMD_FLAGS = -2147483648
class NS_CONTEXT_ATTRIBUTES(Structure):
    Anonymous: _Anonymous_e__Union
    pwszContext: win32more.Windows.Win32.Foundation.PWSTR
    guidHelper: Guid
    dwFlags: UInt32
    ulPriority: UInt32
    ulNumTopCmds: UInt32
    pTopCmds: POINTER(win32more.Windows.Win32.NetworkManagement.NetShell.CMD_ENTRY)
    ulNumGroups: UInt32
    pCmdGroups: POINTER(win32more.Windows.Win32.NetworkManagement.NetShell.CMD_GROUP_ENTRY)
    pfnCommitFn: win32more.Windows.Win32.NetworkManagement.NetShell.PNS_CONTEXT_COMMIT_FN
    pfnDumpFn: win32more.Windows.Win32.NetworkManagement.NetShell.PNS_CONTEXT_DUMP_FN
    pfnConnectFn: win32more.Windows.Win32.NetworkManagement.NetShell.PNS_CONTEXT_CONNECT_FN
    pReserved: VoidPtr
    pfnOsVersionCheck: win32more.Windows.Win32.NetworkManagement.NetShell.PNS_OSVERSIONCHECK
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        _ullAlign: UInt64
        class _Anonymous_e__Struct(Structure):
            dwVersion: UInt32
            dwReserved: UInt32
NS_EVENTS = Int32
NS_EVENT_LOOP: win32more.Windows.Win32.NetworkManagement.NetShell.NS_EVENTS = 65536
NS_EVENT_LAST_N: win32more.Windows.Win32.NetworkManagement.NetShell.NS_EVENTS = 1
NS_EVENT_LAST_SECS: win32more.Windows.Win32.NetworkManagement.NetShell.NS_EVENTS = 2
NS_EVENT_FROM_N: win32more.Windows.Win32.NetworkManagement.NetShell.NS_EVENTS = 4
NS_EVENT_FROM_START: win32more.Windows.Win32.NetworkManagement.NetShell.NS_EVENTS = 8
class NS_HELPER_ATTRIBUTES(Structure):
    Anonymous: _Anonymous_e__Union
    guidHelper: Guid
    pfnStart: win32more.Windows.Win32.NetworkManagement.NetShell.PNS_HELPER_START_FN
    pfnStop: win32more.Windows.Win32.NetworkManagement.NetShell.PNS_HELPER_STOP_FN
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        _ullAlign: UInt64
        class _Anonymous_e__Struct(Structure):
            dwVersion: UInt32
            dwReserved: UInt32
NS_MODE_CHANGE = Int32
NETSH_COMMIT: win32more.Windows.Win32.NetworkManagement.NetShell.NS_MODE_CHANGE = 0
NETSH_UNCOMMIT: win32more.Windows.Win32.NetworkManagement.NetShell.NS_MODE_CHANGE = 1
NETSH_FLUSH: win32more.Windows.Win32.NetworkManagement.NetShell.NS_MODE_CHANGE = 2
NETSH_COMMIT_STATE: win32more.Windows.Win32.NetworkManagement.NetShell.NS_MODE_CHANGE = 3
NETSH_SAVE: win32more.Windows.Win32.NetworkManagement.NetShell.NS_MODE_CHANGE = 4
NS_REQS = Int32
NS_REQ_ZERO: win32more.Windows.Win32.NetworkManagement.NetShell.NS_REQS = 0
NS_REQ_PRESENT: win32more.Windows.Win32.NetworkManagement.NetShell.NS_REQS = 1
NS_REQ_ALLOW_MULTIPLE: win32more.Windows.Win32.NetworkManagement.NetShell.NS_REQS = 2
NS_REQ_ONE_OR_MORE: win32more.Windows.Win32.NetworkManagement.NetShell.NS_REQS = 3
@winfunctype_pointer
def PFN_CUSTOM_HELP(hModule: win32more.Windows.Win32.Foundation.HANDLE, pwszCmdToken: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype_pointer
def PFN_HANDLE_CMD(pwszMachine: win32more.Windows.Win32.Foundation.PWSTR, ppwcArguments: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwCurrentIndex: UInt32, dwArgCount: UInt32, dwFlags: UInt32, pvData: VoidPtr, pbDone: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype_pointer
def PGET_RESOURCE_STRING_FN(dwMsgID: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, nBufferMax: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_CONTEXT_COMMIT_FN(dwAction: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_CONTEXT_CONNECT_FN(pwszMachine: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def PNS_CONTEXT_DUMP_FN(pwszRouter: win32more.Windows.Win32.Foundation.PWSTR, ppwcArguments: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwArgCount: UInt32, pvData: VoidPtr) -> UInt32: ...
@winfunctype_pointer
def PNS_DLL_INIT_FN(dwNetshVersion: UInt32, pReserved: VoidPtr) -> UInt32: ...
@winfunctype_pointer
def PNS_DLL_STOP_FN(dwReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_HELPER_START_FN(pguidParent: POINTER(Guid), dwVersion: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_HELPER_STOP_FN(dwReserved: UInt32) -> UInt32: ...
@winfunctype_pointer
def PNS_OSVERSIONCHECK(CIMOSType: UInt32, CIMOSProductSuite: UInt32, CIMOSVersion: win32more.Windows.Win32.Foundation.PWSTR, CIMOSBuildNumber: win32more.Windows.Win32.Foundation.PWSTR, CIMServicePackMajorVersion: win32more.Windows.Win32.Foundation.PWSTR, CIMServicePackMinorVersion: win32more.Windows.Win32.Foundation.PWSTR, uiReserved: UInt32, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
class TAG_TYPE(Structure):
    pwszTag: win32more.Windows.Win32.Foundation.PWSTR
    dwRequired: UInt32
    bPresent: win32more.Windows.Win32.Foundation.BOOL
class TOKEN_VALUE(Structure):
    pwszToken: win32more.Windows.Win32.Foundation.PWSTR
    dwValue: UInt32


make_ready(__name__)
