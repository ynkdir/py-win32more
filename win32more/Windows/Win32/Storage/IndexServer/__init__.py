from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Storage.IndexServer
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
CI_VERSION_WDS30: UInt32 = 258
CI_VERSION_WDS40: UInt32 = 265
CI_VERSION_WIN70: UInt32 = 1792
CINULLCATALOG: String = '::_noindex_::'
CIADMIN: String = '::_nodocstore_::'
LIFF_LOAD_DEFINED_FILTER: UInt32 = 1
LIFF_IMPLEMENT_TEXT_FILTER_FALLBACK_POLICY: UInt32 = 2
LIFF_FORCE_TEXT_FILTER_FALLBACK: UInt32 = 3
CLSID_INDEX_SERVER_DSO: Guid = Guid('{f9ae8980-7e52-11d0-8964-00c04fd611d7}')
PSGUID_FILENAME: Guid = Guid('{41cf5ae0-f75a-4806-bd87-59c7d9248eb9}')
PID_FILENAME: UInt32 = 100
DBPROPSET_FSCIFRMWRK_EXT: Guid = Guid('{a9bd1526-6a80-11d0-8c9d-0020af1d740e}')
DBPROP_CI_CATALOG_NAME: UInt32 = 2
DBPROP_CI_INCLUDE_SCOPES: UInt32 = 3
DBPROP_CI_DEPTHS: UInt32 = 4
DBPROP_CI_SCOPE_FLAGS: UInt32 = 4
DBPROP_CI_EXCLUDE_SCOPES: UInt32 = 5
DBPROP_CI_SECURITY_ID: UInt32 = 6
DBPROP_CI_QUERY_TYPE: UInt32 = 7
DBPROP_CI_PROVIDER: UInt32 = 8
CI_PROVIDER_MSSEARCH: UInt32 = 1
CI_PROVIDER_INDEXING_SERVICE: UInt32 = 2
CI_PROVIDER_ALL: UInt32 = 4294967295
DBPROPSET_SESS_QUERYEXT: Guid = Guid('{63623309-2d8b-4d17-b152-6e2956c26a70}')
DBPROP_DEFAULT_EQUALS_BEHAVIOR: UInt32 = 2
DBPROPSET_QUERYEXT: Guid = Guid('{a7ac77ed-f8d7-11ce-a798-0020f8008025}')
DBPROP_USECONTENTINDEX: UInt32 = 2
DBPROP_DEFERNONINDEXEDTRIMMING: UInt32 = 3
DBPROP_USEEXTENDEDDBTYPES: UInt32 = 4
DBPROP_IGNORENOISEONLYCLAUSES: UInt32 = 5
DBPROP_GENERICOPTIONS_STRING: UInt32 = 6
DBPROP_FIRSTROWS: UInt32 = 7
DBPROP_DEFERCATALOGVERIFICATION: UInt32 = 8
DBPROP_CATALOGLISTID: UInt32 = 9
DBPROP_GENERATEPARSETREE: UInt32 = 10
DBPROP_APPLICATION_NAME: UInt32 = 11
DBPROP_FREETEXTANYTERM: UInt32 = 12
DBPROP_FREETEXTUSESTEMMING: UInt32 = 13
DBPROP_IGNORESBRI: UInt32 = 14
DBPROP_DONOTCOMPUTEEXPENSIVEPROPS: UInt32 = 15
DBPROP_ENABLEROWSETEVENTS: UInt32 = 16
DBPROPSET_CIFRMWRKCORE_EXT: Guid = Guid('{afafaca5-b5d1-11d0-8c62-00c04fc2db8d}')
DBPROP_MACHINE: UInt32 = 2
DBPROP_CLIENT_CLSID: UInt32 = 3
DBPROPSET_MSIDXS_ROWSETEXT: Guid = Guid('{aa6ee6b0-e828-11d0-b23e-00aa0047fc01}')
MSIDXSPROP_ROWSETQUERYSTATUS: UInt32 = 2
MSIDXSPROP_COMMAND_LOCALE_STRING: UInt32 = 3
MSIDXSPROP_QUERY_RESTRICTION: UInt32 = 4
MSIDXSPROP_PARSE_TREE: UInt32 = 5
MSIDXSPROP_MAX_RANK: UInt32 = 6
MSIDXSPROP_RESULTS_FOUND: UInt32 = 7
MSIDXSPROP_WHEREID: UInt32 = 8
MSIDXSPROP_SERVER_VERSION: UInt32 = 9
MSIDXSPROP_SERVER_WINVER_MAJOR: UInt32 = 10
MSIDXSPROP_SERVER_WINVER_MINOR: UInt32 = 11
MSIDXSPROP_SERVER_NLSVERSION: UInt32 = 12
MSIDXSPROP_SERVER_NLSVER_DEFINED: UInt32 = 13
MSIDXSPROP_SAME_SORTORDER_USED: UInt32 = 14
STAT_BUSY: UInt32 = 0
STAT_ERROR: UInt32 = 1
STAT_DONE: UInt32 = 2
STAT_REFRESH: UInt32 = 3
STAT_PARTIAL_SCOPE: UInt32 = 8
STAT_NOISE_WORDS: UInt32 = 16
STAT_CONTENT_OUT_OF_DATE: UInt32 = 32
STAT_REFRESH_INCOMPLETE: UInt32 = 64
STAT_CONTENT_QUERY_INCOMPLETE: UInt32 = 128
STAT_TIME_LIMIT_EXCEEDED: UInt32 = 256
STAT_SHARING_VIOLATION: UInt32 = 512
STAT_MISSING_RELDOC: UInt32 = 1024
STAT_MISSING_PROP_IN_RELDOC: UInt32 = 2048
STAT_RELDOC_ACCESS_DENIED: UInt32 = 4096
STAT_COALESCE_COMP_ALL_NOISE: UInt32 = 8192
QUERY_SHALLOW: UInt32 = 0
QUERY_DEEP: UInt32 = 1
QUERY_PHYSICAL_PATH: UInt32 = 0
QUERY_VIRTUAL_PATH: UInt32 = 2
PROPID_QUERY_WORKID: UInt32 = 5
PROPID_QUERY_UNFILTERED: UInt32 = 7
PROPID_QUERY_VIRTUALPATH: UInt32 = 9
PROPID_QUERY_LASTSEENTIME: UInt32 = 10
CICAT_STOPPED: UInt32 = 1
CICAT_READONLY: UInt32 = 2
CICAT_WRITABLE: UInt32 = 4
CICAT_NO_QUERY: UInt32 = 8
CICAT_GET_STATE: UInt32 = 16
CICAT_ALL_OPENED: UInt32 = 32
CI_STATE_SHADOW_MERGE: UInt32 = 1
CI_STATE_MASTER_MERGE: UInt32 = 2
CI_STATE_CONTENT_SCAN_REQUIRED: UInt32 = 4
CI_STATE_ANNEALING_MERGE: UInt32 = 8
CI_STATE_SCANNING: UInt32 = 16
CI_STATE_RECOVERING: UInt32 = 32
CI_STATE_INDEX_MIGRATION_MERGE: UInt32 = 64
CI_STATE_LOW_MEMORY: UInt32 = 128
CI_STATE_HIGH_IO: UInt32 = 256
CI_STATE_MASTER_MERGE_PAUSED: UInt32 = 512
CI_STATE_READ_ONLY: UInt32 = 1024
CI_STATE_BATTERY_POWER: UInt32 = 2048
CI_STATE_USER_ACTIVE: UInt32 = 4096
CI_STATE_STARTING: UInt32 = 8192
CI_STATE_READING_USNS: UInt32 = 16384
CI_STATE_DELETION_MERGE: UInt32 = 32768
CI_STATE_LOW_DISK: UInt32 = 65536
CI_STATE_HIGH_CPU: UInt32 = 131072
CI_STATE_BATTERY_POLICY: UInt32 = 262144
GENERATE_METHOD_EXACT: UInt32 = 0
GENERATE_METHOD_PREFIX: UInt32 = 1
GENERATE_METHOD_INFLECT: UInt32 = 2
SCOPE_FLAG_MASK: UInt32 = 255
SCOPE_FLAG_INCLUDE: UInt32 = 1
SCOPE_FLAG_DEEP: UInt32 = 2
SCOPE_TYPE_MASK: UInt32 = 4294967040
SCOPE_TYPE_WINPATH: UInt32 = 256
SCOPE_TYPE_VPATH: UInt32 = 512
PROPID_QUERY_RANKVECTOR: UInt32 = 2
PROPID_QUERY_RANK: UInt32 = 3
PROPID_QUERY_HITCOUNT: UInt32 = 4
PROPID_QUERY_ALL: UInt32 = 6
PROPID_STG_CONTENTS: UInt32 = 19
VECTOR_RANK_MIN: UInt32 = 0
VECTOR_RANK_MAX: UInt32 = 1
VECTOR_RANK_INNER: UInt32 = 2
VECTOR_RANK_DICE: UInt32 = 3
VECTOR_RANK_JACCARD: UInt32 = 4
DBSETFUNC_NONE: UInt32 = 0
DBSETFUNC_ALL: UInt32 = 1
DBSETFUNC_DISTINCT: UInt32 = 2
PROXIMITY_UNIT_WORD: UInt32 = 0
PROXIMITY_UNIT_SENTENCE: UInt32 = 1
PROXIMITY_UNIT_PARAGRAPH: UInt32 = 2
PROXIMITY_UNIT_CHAPTER: UInt32 = 3
NOT_AN_ERROR: win32more.Windows.Win32.Foundation.HRESULT = 524288
FILTER_E_END_OF_CHUNKS: win32more.Windows.Win32.Foundation.HRESULT = -2147215616
FILTER_E_NO_MORE_TEXT: win32more.Windows.Win32.Foundation.HRESULT = -2147215615
FILTER_E_NO_MORE_VALUES: win32more.Windows.Win32.Foundation.HRESULT = -2147215614
FILTER_E_ACCESS: win32more.Windows.Win32.Foundation.HRESULT = -2147215613
FILTER_W_MONIKER_CLIPPED: win32more.Windows.Win32.Foundation.HRESULT = 268036
FILTER_E_NO_TEXT: win32more.Windows.Win32.Foundation.HRESULT = -2147215611
FILTER_E_NO_VALUES: win32more.Windows.Win32.Foundation.HRESULT = -2147215610
FILTER_E_EMBEDDING_UNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147215609
FILTER_E_LINK_UNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147215608
FILTER_S_LAST_TEXT: win32more.Windows.Win32.Foundation.HRESULT = 268041
FILTER_S_LAST_VALUES: win32more.Windows.Win32.Foundation.HRESULT = 268042
FILTER_E_PASSWORD: win32more.Windows.Win32.Foundation.HRESULT = -2147215605
FILTER_E_UNKNOWNFORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2147215604
@winfunctype('query.dll')
def LoadIFilter(pwcsPath: win32more.Windows.Win32.Foundation.PWSTR, pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, ppIUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('query.dll')
def LoadIFilterEx(pwcsPath: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, riid: POINTER(Guid), ppIUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('query.dll')
def BindIFilterFromStorage(pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, ppIUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('query.dll')
def BindIFilterFromStream(pStm: win32more.Windows.Win32.System.Com.IStream, pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, ppIUnk: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
CHUNKSTATE = Int32
CHUNK_TEXT: win32more.Windows.Win32.Storage.IndexServer.CHUNKSTATE = 1
CHUNK_VALUE: win32more.Windows.Win32.Storage.IndexServer.CHUNKSTATE = 2
CHUNK_FILTER_OWNED_VALUE: win32more.Windows.Win32.Storage.IndexServer.CHUNKSTATE = 4
CHUNK_BREAKTYPE = Int32
CHUNK_NO_BREAK: win32more.Windows.Win32.Storage.IndexServer.CHUNK_BREAKTYPE = 0
CHUNK_EOW: win32more.Windows.Win32.Storage.IndexServer.CHUNK_BREAKTYPE = 1
CHUNK_EOS: win32more.Windows.Win32.Storage.IndexServer.CHUNK_BREAKTYPE = 2
CHUNK_EOP: win32more.Windows.Win32.Storage.IndexServer.CHUNK_BREAKTYPE = 3
CHUNK_EOC: win32more.Windows.Win32.Storage.IndexServer.CHUNK_BREAKTYPE = 4
class CI_STATE(Structure):
    cbStruct: UInt32
    cWordList: UInt32
    cPersistentIndex: UInt32
    cQueries: UInt32
    cDocuments: UInt32
    cFreshTest: UInt32
    dwMergeProgress: UInt32
    eState: UInt32
    cFilteredDocuments: UInt32
    cTotalDocuments: UInt32
    cPendingScans: UInt32
    dwIndexSize: UInt32
    cUniqueKeys: UInt32
    cSecQDocuments: UInt32
    dwPropCacheSize: UInt32
if ARCH in 'X64,ARM64':
    class DBID(Structure):
        uGuid: _uGuid_e__Union
        eKind: UInt32
        uName: _uName_e__Union
        class _uGuid_e__Union(Union):
            guid: Guid
            pguid: POINTER(Guid)
        class _uName_e__Union(Union):
            pwszName: win32more.Windows.Win32.Foundation.PWSTR
            ulPropid: UInt32
elif ARCH in 'X86':
    class DBID(Structure):
        uGuid: _uGuid_e__Union
        eKind: UInt32
        uName: _uName_e__Union
        _pack_ = 2
        class _uGuid_e__Union(Union):
            guid: Guid
            pguid: POINTER(Guid)
            _pack_ = 2
        class _uName_e__Union(Union):
            pwszName: win32more.Windows.Win32.Foundation.PWSTR
            ulPropid: UInt32
            _pack_ = 2
DBKINDENUM = Int32
DBKIND_GUID_NAME: win32more.Windows.Win32.Storage.IndexServer.DBKINDENUM = 0
DBKIND_GUID_PROPID: win32more.Windows.Win32.Storage.IndexServer.DBKINDENUM = 1
DBKIND_NAME: win32more.Windows.Win32.Storage.IndexServer.DBKINDENUM = 2
DBKIND_PGUID_NAME: win32more.Windows.Win32.Storage.IndexServer.DBKINDENUM = 3
DBKIND_PGUID_PROPID: win32more.Windows.Win32.Storage.IndexServer.DBKINDENUM = 4
DBKIND_PROPID: win32more.Windows.Win32.Storage.IndexServer.DBKINDENUM = 5
DBKIND_GUID: win32more.Windows.Win32.Storage.IndexServer.DBKINDENUM = 6
class FILTERREGION(Structure):
    idChunk: UInt32
    cwcStart: UInt32
    cwcExtent: UInt32
class FULLPROPSPEC(Structure):
    guidPropSet: Guid
    psProperty: win32more.Windows.Win32.System.Com.StructuredStorage.PROPSPEC
IFILTER_FLAGS = Int32
IFILTER_FLAGS_OLE_PROPERTIES: win32more.Windows.Win32.Storage.IndexServer.IFILTER_FLAGS = 1
IFILTER_INIT = Int32
IFILTER_INIT_CANON_PARAGRAPHS: win32more.Windows.Win32.Storage.IndexServer.IFILTER_INIT = 1
IFILTER_INIT_HARD_LINE_BREAKS: win32more.Windows.Win32.Storage.IndexServer.IFILTER_INIT = 2
IFILTER_INIT_CANON_HYPHENS: win32more.Windows.Win32.Storage.IndexServer.IFILTER_INIT = 4
IFILTER_INIT_CANON_SPACES: win32more.Windows.Win32.Storage.IndexServer.IFILTER_INIT = 8
IFILTER_INIT_APPLY_INDEX_ATTRIBUTES: win32more.Windows.Win32.Storage.IndexServer.IFILTER_INIT = 16
IFILTER_INIT_APPLY_OTHER_ATTRIBUTES: win32more.Windows.Win32.Storage.IndexServer.IFILTER_INIT = 32
IFILTER_INIT_APPLY_CRAWL_ATTRIBUTES: win32more.Windows.Win32.Storage.IndexServer.IFILTER_INIT = 256
IFILTER_INIT_INDEXING_ONLY: win32more.Windows.Win32.Storage.IndexServer.IFILTER_INIT = 64
IFILTER_INIT_SEARCH_LINKS: win32more.Windows.Win32.Storage.IndexServer.IFILTER_INIT = 128
IFILTER_INIT_FILTER_OWNED_VALUE_OK: win32more.Windows.Win32.Storage.IndexServer.IFILTER_INIT = 512
IFILTER_INIT_FILTER_AGGRESSIVE_BREAK: win32more.Windows.Win32.Storage.IndexServer.IFILTER_INIT = 1024
IFILTER_INIT_DISABLE_EMBEDDED: win32more.Windows.Win32.Storage.IndexServer.IFILTER_INIT = 2048
IFILTER_INIT_EMIT_FORMATTING: win32more.Windows.Win32.Storage.IndexServer.IFILTER_INIT = 4096
class IFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{89bcb740-6119-101a-bcb7-00dd010655af}')
    @commethod(3)
    def Init(self, grfFlags: UInt32, cAttributes: UInt32, aAttributes: POINTER(win32more.Windows.Win32.Storage.IndexServer.FULLPROPSPEC), pFlags: POINTER(UInt32)) -> Int32: ...
    @commethod(4)
    def GetChunk(self, pStat: POINTER(win32more.Windows.Win32.Storage.IndexServer.STAT_CHUNK)) -> Int32: ...
    @commethod(5)
    def GetText(self, pcwcBuffer: POINTER(UInt32), awcBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
    @commethod(6)
    def GetValue(self, ppPropValue: POINTER(POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT))) -> Int32: ...
    @commethod(7)
    def BindRegion(self, origPos: win32more.Windows.Win32.Storage.IndexServer.FILTERREGION, riid: POINTER(Guid), ppunk: POINTER(VoidPtr)) -> Int32: ...
class IPhraseSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cc906ff0-c058-101a-b554-08002b33b0e6}')
    @commethod(3)
    def PutSmallPhrase(self, pwcNoun: win32more.Windows.Win32.Foundation.PWSTR, cwcNoun: UInt32, pwcModifier: win32more.Windows.Win32.Foundation.PWSTR, cwcModifier: UInt32, ulAttachmentType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PutPhrase(self, pwcPhrase: win32more.Windows.Win32.Foundation.PWSTR, cwcPhrase: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class STAT_CHUNK(Structure):
    idChunk: UInt32
    breakType: win32more.Windows.Win32.Storage.IndexServer.CHUNK_BREAKTYPE
    flags: win32more.Windows.Win32.Storage.IndexServer.CHUNKSTATE
    locale: UInt32
    attribute: win32more.Windows.Win32.Storage.IndexServer.FULLPROPSPEC
    idChunkSource: UInt32
    cwcStartSource: UInt32
    cwcLenSource: UInt32
WORDREP_BREAK_TYPE = Int32
WORDREP_BREAK_EOW: win32more.Windows.Win32.Storage.IndexServer.WORDREP_BREAK_TYPE = 0
WORDREP_BREAK_EOS: win32more.Windows.Win32.Storage.IndexServer.WORDREP_BREAK_TYPE = 1
WORDREP_BREAK_EOP: win32more.Windows.Win32.Storage.IndexServer.WORDREP_BREAK_TYPE = 2
WORDREP_BREAK_EOC: win32more.Windows.Win32.Storage.IndexServer.WORDREP_BREAK_TYPE = 3


make_ready(__name__)
