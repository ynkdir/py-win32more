from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.NetworkManagement.NetShell

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
NETSH_ERROR_BASE = 15000
ERROR_NO_ENTRIES = 15000
ERROR_INVALID_SYNTAX = 15001
ERROR_PROTOCOL_NOT_IN_TRANSPORT = 15002
ERROR_NO_CHANGE = 15003
ERROR_CMD_NOT_FOUND = 15004
ERROR_ENTRY_PT_NOT_FOUND = 15005
ERROR_DLL_LOAD_FAILED = 15006
ERROR_INIT_DISPLAY = 15007
ERROR_TAG_ALREADY_PRESENT = 15008
ERROR_INVALID_OPTION_TAG = 15009
ERROR_NO_TAG = 15010
ERROR_MISSING_OPTION = 15011
ERROR_TRANSPORT_NOT_PRESENT = 15012
ERROR_SHOW_USAGE = 15013
ERROR_INVALID_OPTION_VALUE = 15014
ERROR_OKAY = 15015
ERROR_CONTINUE_IN_PARENT_CONTEXT = 15016
ERROR_SUPPRESS_OUTPUT = 15017
ERROR_HELPER_ALREADY_REGISTERED = 15018
ERROR_CONTEXT_ALREADY_REGISTERED = 15019
ERROR_PARSING_FAILURE = 15020
NETSH_ERROR_END = 15019
MAX_NAME_LEN = 48
NETSH_VERSION_50 = 20480
NETSH_MAX_TOKEN_LENGTH = 64
NETSH_MAX_CMD_TOKEN_LENGTH = 128
DEFAULT_CONTEXT_PRIORITY = 100
NS_CMD_FLAGS = Int32
CMD_FLAG_PRIVATE = 1
CMD_FLAG_INTERACTIVE = 2
CMD_FLAG_LOCAL = 8
CMD_FLAG_ONLINE = 16
CMD_FLAG_HIDDEN = 32
CMD_FLAG_LIMIT_MASK = 65535
CMD_FLAG_PRIORITY = -2147483648
NS_REQS = Int32
NS_REQ_ZERO = 0
NS_REQ_PRESENT = 1
NS_REQ_ALLOW_MULTIPLE = 2
NS_REQ_ONE_OR_MORE = 3
NS_EVENTS = Int32
NS_EVENT_LOOP = 65536
NS_EVENT_LAST_N = 1
NS_EVENT_LAST_SECS = 2
NS_EVENT_FROM_N = 4
NS_EVENT_FROM_START = 8
NS_MODE_CHANGE = Int32
NETSH_COMMIT = 0
NETSH_UNCOMMIT = 1
NETSH_FLUSH = 2
NETSH_COMMIT_STATE = 3
NETSH_SAVE = 4
def _define_TOKEN_VALUE_head():
    class TOKEN_VALUE(Structure):
        pass
    return TOKEN_VALUE
def _define_TOKEN_VALUE():
    TOKEN_VALUE = win32more.NetworkManagement.NetShell.TOKEN_VALUE_head
    TOKEN_VALUE._fields_ = [
        ("pwszToken", win32more.Foundation.PWSTR),
        ("dwValue", UInt32),
    ]
    return TOKEN_VALUE
def _define_PGET_RESOURCE_STRING_FN():
    return CFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR,UInt32, use_last_error=False)
def _define_PNS_CONTEXT_COMMIT_FN():
    return CFUNCTYPE(UInt32,UInt32, use_last_error=False)
def _define_PNS_CONTEXT_CONNECT_FN():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)
def _define_PNS_CONTEXT_DUMP_FN():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),UInt32,c_void_p, use_last_error=False)
def _define_PNS_DLL_STOP_FN():
    return CFUNCTYPE(UInt32,UInt32, use_last_error=False)
def _define_PNS_HELPER_START_FN():
    return CFUNCTYPE(UInt32,POINTER(Guid),UInt32, use_last_error=False)
def _define_PNS_HELPER_STOP_FN():
    return CFUNCTYPE(UInt32,UInt32, use_last_error=False)
def _define_PFN_HANDLE_CMD():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),UInt32,UInt32,UInt32,c_void_p,POINTER(win32more.Foundation.BOOL), use_last_error=False)
def _define_PNS_OSVERSIONCHECK():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32, use_last_error=False)
def _define_NS_HELPER_ATTRIBUTES_head():
    class NS_HELPER_ATTRIBUTES(Structure):
        pass
    return NS_HELPER_ATTRIBUTES
def _define_NS_HELPER_ATTRIBUTES():
    NS_HELPER_ATTRIBUTES = win32more.NetworkManagement.NetShell.NS_HELPER_ATTRIBUTES_head
    class NS_HELPER_ATTRIBUTES__Anonymous_e__Union(Union):
        pass
    class NS_HELPER_ATTRIBUTES__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    NS_HELPER_ATTRIBUTES__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("dwVersion", UInt32),
        ("dwReserved", UInt32),
    ]
    NS_HELPER_ATTRIBUTES__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    NS_HELPER_ATTRIBUTES__Anonymous_e__Union._fields_ = [
        ("Anonymous", NS_HELPER_ATTRIBUTES__Anonymous_e__Union__Anonymous_e__Struct),
        ("_ullAlign", UInt64),
    ]
    NS_HELPER_ATTRIBUTES._anonymous_ = [
        'Anonymous',
    ]
    NS_HELPER_ATTRIBUTES._fields_ = [
        ("Anonymous", NS_HELPER_ATTRIBUTES__Anonymous_e__Union),
        ("guidHelper", Guid),
        ("pfnStart", win32more.NetworkManagement.NetShell.PNS_HELPER_START_FN),
        ("pfnStop", win32more.NetworkManagement.NetShell.PNS_HELPER_STOP_FN),
    ]
    return NS_HELPER_ATTRIBUTES
def _define_CMD_ENTRY_head():
    class CMD_ENTRY(Structure):
        pass
    return CMD_ENTRY
def _define_CMD_ENTRY():
    CMD_ENTRY = win32more.NetworkManagement.NetShell.CMD_ENTRY_head
    CMD_ENTRY._fields_ = [
        ("pwszCmdToken", win32more.Foundation.PWSTR),
        ("pfnCmdHandler", win32more.NetworkManagement.NetShell.PFN_HANDLE_CMD),
        ("dwShortCmdHelpToken", UInt32),
        ("dwCmdHlpToken", UInt32),
        ("dwFlags", UInt32),
        ("pOsVersionCheck", win32more.NetworkManagement.NetShell.PNS_OSVERSIONCHECK),
    ]
    return CMD_ENTRY
def _define_CMD_GROUP_ENTRY_head():
    class CMD_GROUP_ENTRY(Structure):
        pass
    return CMD_GROUP_ENTRY
def _define_CMD_GROUP_ENTRY():
    CMD_GROUP_ENTRY = win32more.NetworkManagement.NetShell.CMD_GROUP_ENTRY_head
    CMD_GROUP_ENTRY._fields_ = [
        ("pwszCmdGroupToken", win32more.Foundation.PWSTR),
        ("dwShortCmdHelpToken", UInt32),
        ("ulCmdGroupSize", UInt32),
        ("dwFlags", UInt32),
        ("pCmdGroup", POINTER(win32more.NetworkManagement.NetShell.CMD_ENTRY_head)),
        ("pOsVersionCheck", win32more.NetworkManagement.NetShell.PNS_OSVERSIONCHECK),
    ]
    return CMD_GROUP_ENTRY
def _define_NS_CONTEXT_ATTRIBUTES_head():
    class NS_CONTEXT_ATTRIBUTES(Structure):
        pass
    return NS_CONTEXT_ATTRIBUTES
def _define_NS_CONTEXT_ATTRIBUTES():
    NS_CONTEXT_ATTRIBUTES = win32more.NetworkManagement.NetShell.NS_CONTEXT_ATTRIBUTES_head
    class NS_CONTEXT_ATTRIBUTES__Anonymous_e__Union(Union):
        pass
    class NS_CONTEXT_ATTRIBUTES__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    NS_CONTEXT_ATTRIBUTES__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("dwVersion", UInt32),
        ("dwReserved", UInt32),
    ]
    NS_CONTEXT_ATTRIBUTES__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    NS_CONTEXT_ATTRIBUTES__Anonymous_e__Union._fields_ = [
        ("Anonymous", NS_CONTEXT_ATTRIBUTES__Anonymous_e__Union__Anonymous_e__Struct),
        ("_ullAlign", UInt64),
    ]
    NS_CONTEXT_ATTRIBUTES._anonymous_ = [
        'Anonymous',
    ]
    NS_CONTEXT_ATTRIBUTES._fields_ = [
        ("Anonymous", NS_CONTEXT_ATTRIBUTES__Anonymous_e__Union),
        ("pwszContext", win32more.Foundation.PWSTR),
        ("guidHelper", Guid),
        ("dwFlags", UInt32),
        ("ulPriority", UInt32),
        ("ulNumTopCmds", UInt32),
        ("pTopCmds", POINTER(win32more.NetworkManagement.NetShell.CMD_ENTRY_head)),
        ("ulNumGroups", UInt32),
        ("pCmdGroups", POINTER(win32more.NetworkManagement.NetShell.CMD_GROUP_ENTRY_head)),
        ("pfnCommitFn", win32more.NetworkManagement.NetShell.PNS_CONTEXT_COMMIT_FN),
        ("pfnDumpFn", win32more.NetworkManagement.NetShell.PNS_CONTEXT_DUMP_FN),
        ("pfnConnectFn", win32more.NetworkManagement.NetShell.PNS_CONTEXT_CONNECT_FN),
        ("pReserved", c_void_p),
        ("pfnOsVersionCheck", win32more.NetworkManagement.NetShell.PNS_OSVERSIONCHECK),
    ]
    return NS_CONTEXT_ATTRIBUTES
def _define_TAG_TYPE_head():
    class TAG_TYPE(Structure):
        pass
    return TAG_TYPE
def _define_TAG_TYPE():
    TAG_TYPE = win32more.NetworkManagement.NetShell.TAG_TYPE_head
    TAG_TYPE._fields_ = [
        ("pwszTag", win32more.Foundation.PWSTR),
        ("dwRequired", UInt32),
        ("bPresent", win32more.Foundation.BOOL),
    ]
    return TAG_TYPE
def _define_PNS_DLL_INIT_FN():
    return CFUNCTYPE(UInt32,UInt32,c_void_p, use_last_error=False)
def _define_MatchEnumTag():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.NetworkManagement.NetShell.TOKEN_VALUE_head),POINTER(UInt32), use_last_error=False)(("MatchEnumTag", windll["NETSH"]), ((1, 'hModule'),(1, 'pwcArg'),(1, 'dwNumArg'),(1, 'pEnumTable'),(1, 'pdwValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MatchToken():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("MatchToken", windll["NETSH"]), ((1, 'pwszUserToken'),(1, 'pwszCmdToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PreprocessCommand():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.PWSTR),UInt32,UInt32,POINTER(win32more.NetworkManagement.NetShell.TAG_TYPE),UInt32,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(("PreprocessCommand", windll["NETSH"]), ((1, 'hModule'),(1, 'ppwcArguments'),(1, 'dwCurrentIndex'),(1, 'dwArgCount'),(1, 'pttTags'),(1, 'dwTagCount'),(1, 'dwMinArgs'),(1, 'dwMaxArgs'),(1, 'pdwTagType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrintError():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32, use_last_error=False)(("PrintError", windll["NETSH"]), ((1, 'hModule'),(1, 'dwErrId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrintMessageFromModule():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32, use_last_error=False)(("PrintMessageFromModule", windll["NETSH"]), ((1, 'hModule'),(1, 'dwMsgId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrintMessage():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("PrintMessage", windll["NETSH"]), ((1, 'pwszFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterContext():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.NetShell.NS_CONTEXT_ATTRIBUTES_head), use_last_error=False)(("RegisterContext", windll["NETSH"]), ((1, 'pChildContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterHelper():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),POINTER(win32more.NetworkManagement.NetShell.NS_HELPER_ATTRIBUTES_head), use_last_error=False)(("RegisterHelper", windll["NETSH"]), ((1, 'pguidParentContext'),(1, 'pfnRegisterSubContext'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "NETSH_ERROR_BASE",
    "ERROR_NO_ENTRIES",
    "ERROR_INVALID_SYNTAX",
    "ERROR_PROTOCOL_NOT_IN_TRANSPORT",
    "ERROR_NO_CHANGE",
    "ERROR_CMD_NOT_FOUND",
    "ERROR_ENTRY_PT_NOT_FOUND",
    "ERROR_DLL_LOAD_FAILED",
    "ERROR_INIT_DISPLAY",
    "ERROR_TAG_ALREADY_PRESENT",
    "ERROR_INVALID_OPTION_TAG",
    "ERROR_NO_TAG",
    "ERROR_MISSING_OPTION",
    "ERROR_TRANSPORT_NOT_PRESENT",
    "ERROR_SHOW_USAGE",
    "ERROR_INVALID_OPTION_VALUE",
    "ERROR_OKAY",
    "ERROR_CONTINUE_IN_PARENT_CONTEXT",
    "ERROR_SUPPRESS_OUTPUT",
    "ERROR_HELPER_ALREADY_REGISTERED",
    "ERROR_CONTEXT_ALREADY_REGISTERED",
    "ERROR_PARSING_FAILURE",
    "NETSH_ERROR_END",
    "MAX_NAME_LEN",
    "NETSH_VERSION_50",
    "NETSH_MAX_TOKEN_LENGTH",
    "NETSH_MAX_CMD_TOKEN_LENGTH",
    "DEFAULT_CONTEXT_PRIORITY",
    "NS_CMD_FLAGS",
    "CMD_FLAG_PRIVATE",
    "CMD_FLAG_INTERACTIVE",
    "CMD_FLAG_LOCAL",
    "CMD_FLAG_ONLINE",
    "CMD_FLAG_HIDDEN",
    "CMD_FLAG_LIMIT_MASK",
    "CMD_FLAG_PRIORITY",
    "NS_REQS",
    "NS_REQ_ZERO",
    "NS_REQ_PRESENT",
    "NS_REQ_ALLOW_MULTIPLE",
    "NS_REQ_ONE_OR_MORE",
    "NS_EVENTS",
    "NS_EVENT_LOOP",
    "NS_EVENT_LAST_N",
    "NS_EVENT_LAST_SECS",
    "NS_EVENT_FROM_N",
    "NS_EVENT_FROM_START",
    "NS_MODE_CHANGE",
    "NETSH_COMMIT",
    "NETSH_UNCOMMIT",
    "NETSH_FLUSH",
    "NETSH_COMMIT_STATE",
    "NETSH_SAVE",
    "TOKEN_VALUE",
    "PGET_RESOURCE_STRING_FN",
    "PNS_CONTEXT_COMMIT_FN",
    "PNS_CONTEXT_CONNECT_FN",
    "PNS_CONTEXT_DUMP_FN",
    "PNS_DLL_STOP_FN",
    "PNS_HELPER_START_FN",
    "PNS_HELPER_STOP_FN",
    "PFN_HANDLE_CMD",
    "PNS_OSVERSIONCHECK",
    "NS_HELPER_ATTRIBUTES",
    "CMD_ENTRY",
    "CMD_GROUP_ENTRY",
    "NS_CONTEXT_ATTRIBUTES",
    "TAG_TYPE",
    "PNS_DLL_INIT_FN",
    "MatchEnumTag",
    "MatchToken",
    "PreprocessCommand",
    "PrintError",
    "PrintMessageFromModule",
    "PrintMessage",
    "RegisterContext",
    "RegisterHelper",
]
