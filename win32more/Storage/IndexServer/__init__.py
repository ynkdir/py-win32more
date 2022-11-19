from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Storage.IndexServer
import win32more.System.Com
import win32more.System.Com.StructuredStorage

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
CI_VERSION_WDS30 = 258
CI_VERSION_WDS40 = 265
CI_VERSION_WIN70 = 1792
LIFF_LOAD_DEFINED_FILTER = 1
LIFF_IMPLEMENT_TEXT_FILTER_FALLBACK_POLICY = 2
LIFF_FORCE_TEXT_FILTER_FALLBACK = 3
PID_FILENAME = 100
DBPROP_CI_CATALOG_NAME = 2
DBPROP_CI_INCLUDE_SCOPES = 3
DBPROP_CI_DEPTHS = 4
DBPROP_CI_SCOPE_FLAGS = 4
DBPROP_CI_EXCLUDE_SCOPES = 5
DBPROP_CI_SECURITY_ID = 6
DBPROP_CI_QUERY_TYPE = 7
DBPROP_CI_PROVIDER = 8
CI_PROVIDER_MSSEARCH = 1
CI_PROVIDER_INDEXING_SERVICE = 2
CI_PROVIDER_ALL = 4294967295
DBPROP_DEFAULT_EQUALS_BEHAVIOR = 2
DBPROP_USECONTENTINDEX = 2
DBPROP_DEFERNONINDEXEDTRIMMING = 3
DBPROP_USEEXTENDEDDBTYPES = 4
DBPROP_IGNORENOISEONLYCLAUSES = 5
DBPROP_GENERICOPTIONS_STRING = 6
DBPROP_FIRSTROWS = 7
DBPROP_DEFERCATALOGVERIFICATION = 8
DBPROP_CATALOGLISTID = 9
DBPROP_GENERATEPARSETREE = 10
DBPROP_APPLICATION_NAME = 11
DBPROP_FREETEXTANYTERM = 12
DBPROP_FREETEXTUSESTEMMING = 13
DBPROP_IGNORESBRI = 14
DBPROP_DONOTCOMPUTEEXPENSIVEPROPS = 15
DBPROP_ENABLEROWSETEVENTS = 16
DBPROP_MACHINE = 2
DBPROP_CLIENT_CLSID = 3
MSIDXSPROP_ROWSETQUERYSTATUS = 2
MSIDXSPROP_COMMAND_LOCALE_STRING = 3
MSIDXSPROP_QUERY_RESTRICTION = 4
MSIDXSPROP_PARSE_TREE = 5
MSIDXSPROP_MAX_RANK = 6
MSIDXSPROP_RESULTS_FOUND = 7
MSIDXSPROP_WHEREID = 8
MSIDXSPROP_SERVER_VERSION = 9
MSIDXSPROP_SERVER_WINVER_MAJOR = 10
MSIDXSPROP_SERVER_WINVER_MINOR = 11
MSIDXSPROP_SERVER_NLSVERSION = 12
MSIDXSPROP_SERVER_NLSVER_DEFINED = 13
MSIDXSPROP_SAME_SORTORDER_USED = 14
STAT_BUSY = 0
STAT_ERROR = 1
STAT_DONE = 2
STAT_REFRESH = 3
STAT_PARTIAL_SCOPE = 8
STAT_NOISE_WORDS = 16
STAT_CONTENT_OUT_OF_DATE = 32
STAT_REFRESH_INCOMPLETE = 64
STAT_CONTENT_QUERY_INCOMPLETE = 128
STAT_TIME_LIMIT_EXCEEDED = 256
STAT_SHARING_VIOLATION = 512
STAT_MISSING_RELDOC = 1024
STAT_MISSING_PROP_IN_RELDOC = 2048
STAT_RELDOC_ACCESS_DENIED = 4096
STAT_COALESCE_COMP_ALL_NOISE = 8192
QUERY_SHALLOW = 0
QUERY_DEEP = 1
QUERY_PHYSICAL_PATH = 0
QUERY_VIRTUAL_PATH = 2
PROPID_QUERY_WORKID = 5
PROPID_QUERY_UNFILTERED = 7
PROPID_QUERY_VIRTUALPATH = 9
PROPID_QUERY_LASTSEENTIME = 10
CICAT_STOPPED = 1
CICAT_READONLY = 2
CICAT_WRITABLE = 4
CICAT_NO_QUERY = 8
CICAT_GET_STATE = 16
CICAT_ALL_OPENED = 32
CI_STATE_SHADOW_MERGE = 1
CI_STATE_MASTER_MERGE = 2
CI_STATE_CONTENT_SCAN_REQUIRED = 4
CI_STATE_ANNEALING_MERGE = 8
CI_STATE_SCANNING = 16
CI_STATE_RECOVERING = 32
CI_STATE_INDEX_MIGRATION_MERGE = 64
CI_STATE_LOW_MEMORY = 128
CI_STATE_HIGH_IO = 256
CI_STATE_MASTER_MERGE_PAUSED = 512
CI_STATE_READ_ONLY = 1024
CI_STATE_BATTERY_POWER = 2048
CI_STATE_USER_ACTIVE = 4096
CI_STATE_STARTING = 8192
CI_STATE_READING_USNS = 16384
CI_STATE_DELETION_MERGE = 32768
CI_STATE_LOW_DISK = 65536
CI_STATE_HIGH_CPU = 131072
CI_STATE_BATTERY_POLICY = 262144
GENERATE_METHOD_EXACT = 0
GENERATE_METHOD_PREFIX = 1
GENERATE_METHOD_INFLECT = 2
SCOPE_FLAG_MASK = 255
SCOPE_FLAG_INCLUDE = 1
SCOPE_FLAG_DEEP = 2
SCOPE_TYPE_MASK = 4294967040
SCOPE_TYPE_WINPATH = 256
SCOPE_TYPE_VPATH = 512
PROPID_QUERY_RANKVECTOR = 2
PROPID_QUERY_RANK = 3
PROPID_QUERY_HITCOUNT = 4
PROPID_QUERY_ALL = 6
PROPID_STG_CONTENTS = 19
VECTOR_RANK_MIN = 0
VECTOR_RANK_MAX = 1
VECTOR_RANK_INNER = 2
VECTOR_RANK_DICE = 3
VECTOR_RANK_JACCARD = 4
DBSETFUNC_NONE = 0
DBSETFUNC_ALL = 1
DBSETFUNC_DISTINCT = 2
PROXIMITY_UNIT_WORD = 0
PROXIMITY_UNIT_SENTENCE = 1
PROXIMITY_UNIT_PARAGRAPH = 2
PROXIMITY_UNIT_CHAPTER = 3
NOT_AN_ERROR = 524288
FILTER_E_END_OF_CHUNKS = -2147215616
FILTER_E_NO_MORE_TEXT = -2147215615
FILTER_E_NO_MORE_VALUES = -2147215614
FILTER_E_ACCESS = -2147215613
FILTER_W_MONIKER_CLIPPED = 268036
FILTER_E_NO_TEXT = -2147215611
FILTER_E_NO_VALUES = -2147215610
FILTER_E_EMBEDDING_UNAVAILABLE = -2147215609
FILTER_E_LINK_UNAVAILABLE = -2147215608
FILTER_S_LAST_TEXT = 268041
FILTER_S_LAST_VALUES = 268042
FILTER_E_PASSWORD = -2147215605
FILTER_E_UNKNOWNFORMAT = -2147215604
def _define_CI_STATE_head():
    class CI_STATE(Structure):
        pass
    return CI_STATE
def _define_CI_STATE():
    CI_STATE = win32more.Storage.IndexServer.CI_STATE_head
    CI_STATE._fields_ = [
        ("cbStruct", UInt32),
        ("cWordList", UInt32),
        ("cPersistentIndex", UInt32),
        ("cQueries", UInt32),
        ("cDocuments", UInt32),
        ("cFreshTest", UInt32),
        ("dwMergeProgress", UInt32),
        ("eState", UInt32),
        ("cFilteredDocuments", UInt32),
        ("cTotalDocuments", UInt32),
        ("cPendingScans", UInt32),
        ("dwIndexSize", UInt32),
        ("cUniqueKeys", UInt32),
        ("cSecQDocuments", UInt32),
        ("dwPropCacheSize", UInt32),
    ]
    return CI_STATE
def _define_FULLPROPSPEC_head():
    class FULLPROPSPEC(Structure):
        pass
    return FULLPROPSPEC
def _define_FULLPROPSPEC():
    FULLPROPSPEC = win32more.Storage.IndexServer.FULLPROPSPEC_head
    FULLPROPSPEC._fields_ = [
        ("guidPropSet", Guid),
        ("psProperty", win32more.System.Com.StructuredStorage.PROPSPEC),
    ]
    return FULLPROPSPEC
IFILTER_INIT = Int32
IFILTER_INIT_CANON_PARAGRAPHS = 1
IFILTER_INIT_HARD_LINE_BREAKS = 2
IFILTER_INIT_CANON_HYPHENS = 4
IFILTER_INIT_CANON_SPACES = 8
IFILTER_INIT_APPLY_INDEX_ATTRIBUTES = 16
IFILTER_INIT_APPLY_OTHER_ATTRIBUTES = 32
IFILTER_INIT_APPLY_CRAWL_ATTRIBUTES = 256
IFILTER_INIT_INDEXING_ONLY = 64
IFILTER_INIT_SEARCH_LINKS = 128
IFILTER_INIT_FILTER_OWNED_VALUE_OK = 512
IFILTER_INIT_FILTER_AGGRESSIVE_BREAK = 1024
IFILTER_INIT_DISABLE_EMBEDDED = 2048
IFILTER_INIT_EMIT_FORMATTING = 4096
IFILTER_FLAGS = Int32
IFILTER_FLAGS_OLE_PROPERTIES = 1
CHUNKSTATE = Int32
CHUNK_TEXT = 1
CHUNK_VALUE = 2
CHUNK_FILTER_OWNED_VALUE = 4
CHUNK_BREAKTYPE = Int32
CHUNK_NO_BREAK = 0
CHUNK_EOW = 1
CHUNK_EOS = 2
CHUNK_EOP = 3
CHUNK_EOC = 4
def _define_FILTERREGION_head():
    class FILTERREGION(Structure):
        pass
    return FILTERREGION
def _define_FILTERREGION():
    FILTERREGION = win32more.Storage.IndexServer.FILTERREGION_head
    FILTERREGION._fields_ = [
        ("idChunk", UInt32),
        ("cwcStart", UInt32),
        ("cwcExtent", UInt32),
    ]
    return FILTERREGION
def _define_STAT_CHUNK_head():
    class STAT_CHUNK(Structure):
        pass
    return STAT_CHUNK
def _define_STAT_CHUNK():
    STAT_CHUNK = win32more.Storage.IndexServer.STAT_CHUNK_head
    STAT_CHUNK._fields_ = [
        ("idChunk", UInt32),
        ("breakType", win32more.Storage.IndexServer.CHUNK_BREAKTYPE),
        ("flags", win32more.Storage.IndexServer.CHUNKSTATE),
        ("locale", UInt32),
        ("attribute", win32more.Storage.IndexServer.FULLPROPSPEC),
        ("idChunkSource", UInt32),
        ("cwcStartSource", UInt32),
        ("cwcLenSource", UInt32),
    ]
    return STAT_CHUNK
def _define_IFilter_head():
    class IFilter(win32more.System.Com.IUnknown_head):
        Guid = Guid('89bcb740-6119-101a-bcb7-00dd010655af')
    return IFilter
def _define_IFilter():
    IFilter = win32more.Storage.IndexServer.IFilter_head
    IFilter.Init = COMMETHOD(WINFUNCTYPE(Int32,UInt32,UInt32,POINTER(win32more.Storage.IndexServer.FULLPROPSPEC),POINTER(UInt32), use_last_error=False)(3, 'Init', ((1, 'grfFlags'),(1, 'cAttributes'),(1, 'aAttributes'),(1, 'pFlags'),)))
    IFilter.GetChunk = COMMETHOD(WINFUNCTYPE(Int32,POINTER(win32more.Storage.IndexServer.STAT_CHUNK_head), use_last_error=False)(4, 'GetChunk', ((1, 'pStat'),)))
    IFilter.GetText = COMMETHOD(WINFUNCTYPE(Int32,POINTER(UInt32),POINTER(Char), use_last_error=False)(5, 'GetText', ((1, 'pcwcBuffer'),(1, 'awcBuffer'),)))
    IFilter.GetValue = COMMETHOD(WINFUNCTYPE(Int32,POINTER(POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head)), use_last_error=False)(6, 'GetValue', ((1, 'ppPropValue'),)))
    IFilter.BindRegion = COMMETHOD(WINFUNCTYPE(Int32,win32more.Storage.IndexServer.FILTERREGION,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(7, 'BindRegion', ((1, 'origPos'),(1, 'riid'),(1, 'ppunk'),)))
    win32more.System.Com.IUnknown
    return IFilter
def _define_IPhraseSink_head():
    class IPhraseSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('cc906ff0-c058-101a-b554-08002b33b0e6')
    return IPhraseSink
def _define_IPhraseSink():
    IPhraseSink = win32more.Storage.IndexServer.IPhraseSink_head
    IPhraseSink.PutSmallPhrase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,UInt32, use_last_error=False)(3, 'PutSmallPhrase', ((1, 'pwcNoun'),(1, 'cwcNoun'),(1, 'pwcModifier'),(1, 'cwcModifier'),(1, 'ulAttachmentType'),)))
    IPhraseSink.PutPhrase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(4, 'PutPhrase', ((1, 'pwcPhrase'),(1, 'cwcPhrase'),)))
    win32more.System.Com.IUnknown
    return IPhraseSink
WORDREP_BREAK_TYPE = Int32
WORDREP_BREAK_EOW = 0
WORDREP_BREAK_EOS = 1
WORDREP_BREAK_EOP = 2
WORDREP_BREAK_EOC = 3
DBKINDENUM = Int32
DBKIND_GUID_NAME = 0
DBKIND_GUID_PROPID = 1
DBKIND_NAME = 2
DBKIND_PGUID_NAME = 3
DBKIND_PGUID_PROPID = 4
DBKIND_PROPID = 5
DBKIND_GUID = 6
def _define_DBID_head():
    class DBID(Structure):
        pass
    return DBID
def _define_DBID():
    DBID = win32more.Storage.IndexServer.DBID_head
    class DBID__uName_e__Union(Union):
        pass
    DBID__uName_e__Union._fields_ = [
        ("pwszName", win32more.Foundation.PWSTR),
        ("ulPropid", UInt32),
    ]
    class DBID__uGuid_e__Union(Union):
        pass
    DBID__uGuid_e__Union._fields_ = [
        ("guid", Guid),
        ("pguid", POINTER(Guid)),
    ]
    DBID._fields_ = [
        ("uGuid", DBID__uGuid_e__Union),
        ("eKind", UInt32),
        ("uName", DBID__uName_e__Union),
    ]
    return DBID
def _define_LoadIFilter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IUnknown_head,POINTER(c_void_p), use_last_error=False)(("LoadIFilter", windll["query"]), ((1, 'pwcsPath'),(1, 'pUnkOuter'),(1, 'ppIUnk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadIFilterEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("LoadIFilterEx", windll["query"]), ((1, 'pwcsPath'),(1, 'dwFlags'),(1, 'riid'),(1, 'ppIUnk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BindIFilterFromStorage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,win32more.System.Com.IUnknown_head,POINTER(c_void_p), use_last_error=False)(("BindIFilterFromStorage", windll["query"]), ((1, 'pStg'),(1, 'pUnkOuter'),(1, 'ppIUnk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BindIFilterFromStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.Com.IUnknown_head,POINTER(c_void_p), use_last_error=False)(("BindIFilterFromStream", windll["query"]), ((1, 'pStm'),(1, 'pUnkOuter'),(1, 'ppIUnk'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CI_VERSION_WDS30",
    "CI_VERSION_WDS40",
    "CI_VERSION_WIN70",
    "LIFF_LOAD_DEFINED_FILTER",
    "LIFF_IMPLEMENT_TEXT_FILTER_FALLBACK_POLICY",
    "LIFF_FORCE_TEXT_FILTER_FALLBACK",
    "PID_FILENAME",
    "DBPROP_CI_CATALOG_NAME",
    "DBPROP_CI_INCLUDE_SCOPES",
    "DBPROP_CI_DEPTHS",
    "DBPROP_CI_SCOPE_FLAGS",
    "DBPROP_CI_EXCLUDE_SCOPES",
    "DBPROP_CI_SECURITY_ID",
    "DBPROP_CI_QUERY_TYPE",
    "DBPROP_CI_PROVIDER",
    "CI_PROVIDER_MSSEARCH",
    "CI_PROVIDER_INDEXING_SERVICE",
    "CI_PROVIDER_ALL",
    "DBPROP_DEFAULT_EQUALS_BEHAVIOR",
    "DBPROP_USECONTENTINDEX",
    "DBPROP_DEFERNONINDEXEDTRIMMING",
    "DBPROP_USEEXTENDEDDBTYPES",
    "DBPROP_IGNORENOISEONLYCLAUSES",
    "DBPROP_GENERICOPTIONS_STRING",
    "DBPROP_FIRSTROWS",
    "DBPROP_DEFERCATALOGVERIFICATION",
    "DBPROP_CATALOGLISTID",
    "DBPROP_GENERATEPARSETREE",
    "DBPROP_APPLICATION_NAME",
    "DBPROP_FREETEXTANYTERM",
    "DBPROP_FREETEXTUSESTEMMING",
    "DBPROP_IGNORESBRI",
    "DBPROP_DONOTCOMPUTEEXPENSIVEPROPS",
    "DBPROP_ENABLEROWSETEVENTS",
    "DBPROP_MACHINE",
    "DBPROP_CLIENT_CLSID",
    "MSIDXSPROP_ROWSETQUERYSTATUS",
    "MSIDXSPROP_COMMAND_LOCALE_STRING",
    "MSIDXSPROP_QUERY_RESTRICTION",
    "MSIDXSPROP_PARSE_TREE",
    "MSIDXSPROP_MAX_RANK",
    "MSIDXSPROP_RESULTS_FOUND",
    "MSIDXSPROP_WHEREID",
    "MSIDXSPROP_SERVER_VERSION",
    "MSIDXSPROP_SERVER_WINVER_MAJOR",
    "MSIDXSPROP_SERVER_WINVER_MINOR",
    "MSIDXSPROP_SERVER_NLSVERSION",
    "MSIDXSPROP_SERVER_NLSVER_DEFINED",
    "MSIDXSPROP_SAME_SORTORDER_USED",
    "STAT_BUSY",
    "STAT_ERROR",
    "STAT_DONE",
    "STAT_REFRESH",
    "STAT_PARTIAL_SCOPE",
    "STAT_NOISE_WORDS",
    "STAT_CONTENT_OUT_OF_DATE",
    "STAT_REFRESH_INCOMPLETE",
    "STAT_CONTENT_QUERY_INCOMPLETE",
    "STAT_TIME_LIMIT_EXCEEDED",
    "STAT_SHARING_VIOLATION",
    "STAT_MISSING_RELDOC",
    "STAT_MISSING_PROP_IN_RELDOC",
    "STAT_RELDOC_ACCESS_DENIED",
    "STAT_COALESCE_COMP_ALL_NOISE",
    "QUERY_SHALLOW",
    "QUERY_DEEP",
    "QUERY_PHYSICAL_PATH",
    "QUERY_VIRTUAL_PATH",
    "PROPID_QUERY_WORKID",
    "PROPID_QUERY_UNFILTERED",
    "PROPID_QUERY_VIRTUALPATH",
    "PROPID_QUERY_LASTSEENTIME",
    "CICAT_STOPPED",
    "CICAT_READONLY",
    "CICAT_WRITABLE",
    "CICAT_NO_QUERY",
    "CICAT_GET_STATE",
    "CICAT_ALL_OPENED",
    "CI_STATE_SHADOW_MERGE",
    "CI_STATE_MASTER_MERGE",
    "CI_STATE_CONTENT_SCAN_REQUIRED",
    "CI_STATE_ANNEALING_MERGE",
    "CI_STATE_SCANNING",
    "CI_STATE_RECOVERING",
    "CI_STATE_INDEX_MIGRATION_MERGE",
    "CI_STATE_LOW_MEMORY",
    "CI_STATE_HIGH_IO",
    "CI_STATE_MASTER_MERGE_PAUSED",
    "CI_STATE_READ_ONLY",
    "CI_STATE_BATTERY_POWER",
    "CI_STATE_USER_ACTIVE",
    "CI_STATE_STARTING",
    "CI_STATE_READING_USNS",
    "CI_STATE_DELETION_MERGE",
    "CI_STATE_LOW_DISK",
    "CI_STATE_HIGH_CPU",
    "CI_STATE_BATTERY_POLICY",
    "GENERATE_METHOD_EXACT",
    "GENERATE_METHOD_PREFIX",
    "GENERATE_METHOD_INFLECT",
    "SCOPE_FLAG_MASK",
    "SCOPE_FLAG_INCLUDE",
    "SCOPE_FLAG_DEEP",
    "SCOPE_TYPE_MASK",
    "SCOPE_TYPE_WINPATH",
    "SCOPE_TYPE_VPATH",
    "PROPID_QUERY_RANKVECTOR",
    "PROPID_QUERY_RANK",
    "PROPID_QUERY_HITCOUNT",
    "PROPID_QUERY_ALL",
    "PROPID_STG_CONTENTS",
    "VECTOR_RANK_MIN",
    "VECTOR_RANK_MAX",
    "VECTOR_RANK_INNER",
    "VECTOR_RANK_DICE",
    "VECTOR_RANK_JACCARD",
    "DBSETFUNC_NONE",
    "DBSETFUNC_ALL",
    "DBSETFUNC_DISTINCT",
    "PROXIMITY_UNIT_WORD",
    "PROXIMITY_UNIT_SENTENCE",
    "PROXIMITY_UNIT_PARAGRAPH",
    "PROXIMITY_UNIT_CHAPTER",
    "NOT_AN_ERROR",
    "FILTER_E_END_OF_CHUNKS",
    "FILTER_E_NO_MORE_TEXT",
    "FILTER_E_NO_MORE_VALUES",
    "FILTER_E_ACCESS",
    "FILTER_W_MONIKER_CLIPPED",
    "FILTER_E_NO_TEXT",
    "FILTER_E_NO_VALUES",
    "FILTER_E_EMBEDDING_UNAVAILABLE",
    "FILTER_E_LINK_UNAVAILABLE",
    "FILTER_S_LAST_TEXT",
    "FILTER_S_LAST_VALUES",
    "FILTER_E_PASSWORD",
    "FILTER_E_UNKNOWNFORMAT",
    "CI_STATE",
    "FULLPROPSPEC",
    "IFILTER_INIT",
    "IFILTER_INIT_CANON_PARAGRAPHS",
    "IFILTER_INIT_HARD_LINE_BREAKS",
    "IFILTER_INIT_CANON_HYPHENS",
    "IFILTER_INIT_CANON_SPACES",
    "IFILTER_INIT_APPLY_INDEX_ATTRIBUTES",
    "IFILTER_INIT_APPLY_OTHER_ATTRIBUTES",
    "IFILTER_INIT_APPLY_CRAWL_ATTRIBUTES",
    "IFILTER_INIT_INDEXING_ONLY",
    "IFILTER_INIT_SEARCH_LINKS",
    "IFILTER_INIT_FILTER_OWNED_VALUE_OK",
    "IFILTER_INIT_FILTER_AGGRESSIVE_BREAK",
    "IFILTER_INIT_DISABLE_EMBEDDED",
    "IFILTER_INIT_EMIT_FORMATTING",
    "IFILTER_FLAGS",
    "IFILTER_FLAGS_OLE_PROPERTIES",
    "CHUNKSTATE",
    "CHUNK_TEXT",
    "CHUNK_VALUE",
    "CHUNK_FILTER_OWNED_VALUE",
    "CHUNK_BREAKTYPE",
    "CHUNK_NO_BREAK",
    "CHUNK_EOW",
    "CHUNK_EOS",
    "CHUNK_EOP",
    "CHUNK_EOC",
    "FILTERREGION",
    "STAT_CHUNK",
    "IFilter",
    "IPhraseSink",
    "WORDREP_BREAK_TYPE",
    "WORDREP_BREAK_EOW",
    "WORDREP_BREAK_EOS",
    "WORDREP_BREAK_EOP",
    "WORDREP_BREAK_EOC",
    "DBKINDENUM",
    "DBKIND_GUID_NAME",
    "DBKIND_GUID_PROPID",
    "DBKIND_NAME",
    "DBKIND_PGUID_NAME",
    "DBKIND_PGUID_PROPID",
    "DBKIND_PROPID",
    "DBKIND_GUID",
    "DBID",
    "LoadIFilter",
    "LoadIFilterEx",
    "BindIFilterFromStorage",
    "BindIFilterFromStream",
]
