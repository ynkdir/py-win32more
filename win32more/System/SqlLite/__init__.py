from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.SqlLite

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
SQLITE_VERSION_NUMBER = 3029000
SQLITE_OK = 0
SQLITE_ERROR = 1
SQLITE_INTERNAL = 2
SQLITE_PERM = 3
SQLITE_ABORT = 4
SQLITE_BUSY = 5
SQLITE_LOCKED = 6
SQLITE_NOMEM = 7
SQLITE_READONLY = 8
SQLITE_INTERRUPT = 9
SQLITE_IOERR = 10
SQLITE_CORRUPT = 11
SQLITE_NOTFOUND = 12
SQLITE_FULL = 13
SQLITE_CANTOPEN = 14
SQLITE_PROTOCOL = 15
SQLITE_EMPTY = 16
SQLITE_SCHEMA = 17
SQLITE_TOOBIG = 18
SQLITE_CONSTRAINT = 19
SQLITE_MISMATCH = 20
SQLITE_MISUSE = 21
SQLITE_NOLFS = 22
SQLITE_AUTH = 23
SQLITE_FORMAT = 24
SQLITE_RANGE = 25
SQLITE_NOTADB = 26
SQLITE_NOTICE = 27
SQLITE_WARNING = 28
SQLITE_ROW = 100
SQLITE_DONE = 101
SQLITE_OPEN_READONLY = 1
SQLITE_OPEN_READWRITE = 2
SQLITE_OPEN_CREATE = 4
SQLITE_OPEN_DELETEONCLOSE = 8
SQLITE_OPEN_EXCLUSIVE = 16
SQLITE_OPEN_AUTOPROXY = 32
SQLITE_OPEN_URI = 64
SQLITE_OPEN_MEMORY = 128
SQLITE_OPEN_MAIN_DB = 256
SQLITE_OPEN_TEMP_DB = 512
SQLITE_OPEN_TRANSIENT_DB = 1024
SQLITE_OPEN_MAIN_JOURNAL = 2048
SQLITE_OPEN_TEMP_JOURNAL = 4096
SQLITE_OPEN_SUBJOURNAL = 8192
SQLITE_OPEN_SUPER_JOURNAL = 16384
SQLITE_OPEN_NOMUTEX = 32768
SQLITE_OPEN_FULLMUTEX = 65536
SQLITE_OPEN_SHAREDCACHE = 131072
SQLITE_OPEN_PRIVATECACHE = 262144
SQLITE_OPEN_WAL = 524288
SQLITE_OPEN_NOFOLLOW = 16777216
SQLITE_OPEN_MASTER_JOURNAL = 16384
SQLITE_IOCAP_ATOMIC = 1
SQLITE_IOCAP_ATOMIC512 = 2
SQLITE_IOCAP_ATOMIC1K = 4
SQLITE_IOCAP_ATOMIC2K = 8
SQLITE_IOCAP_ATOMIC4K = 16
SQLITE_IOCAP_ATOMIC8K = 32
SQLITE_IOCAP_ATOMIC16K = 64
SQLITE_IOCAP_ATOMIC32K = 128
SQLITE_IOCAP_ATOMIC64K = 256
SQLITE_IOCAP_SAFE_APPEND = 512
SQLITE_IOCAP_SEQUENTIAL = 1024
SQLITE_IOCAP_UNDELETABLE_WHEN_OPEN = 2048
SQLITE_IOCAP_POWERSAFE_OVERWRITE = 4096
SQLITE_IOCAP_IMMUTABLE = 8192
SQLITE_IOCAP_BATCH_ATOMIC = 16384
SQLITE_LOCK_NONE = 0
SQLITE_LOCK_SHARED = 1
SQLITE_LOCK_RESERVED = 2
SQLITE_LOCK_PENDING = 3
SQLITE_LOCK_EXCLUSIVE = 4
SQLITE_SYNC_NORMAL = 2
SQLITE_SYNC_FULL = 3
SQLITE_SYNC_DATAONLY = 16
SQLITE_FCNTL_LOCKSTATE = 1
SQLITE_FCNTL_GET_LOCKPROXYFILE = 2
SQLITE_FCNTL_SET_LOCKPROXYFILE = 3
SQLITE_FCNTL_LAST_ERRNO = 4
SQLITE_FCNTL_SIZE_HINT = 5
SQLITE_FCNTL_CHUNK_SIZE = 6
SQLITE_FCNTL_FILE_POINTER = 7
SQLITE_FCNTL_SYNC_OMITTED = 8
SQLITE_FCNTL_WIN32_AV_RETRY = 9
SQLITE_FCNTL_PERSIST_WAL = 10
SQLITE_FCNTL_OVERWRITE = 11
SQLITE_FCNTL_VFSNAME = 12
SQLITE_FCNTL_POWERSAFE_OVERWRITE = 13
SQLITE_FCNTL_PRAGMA = 14
SQLITE_FCNTL_BUSYHANDLER = 15
SQLITE_FCNTL_TEMPFILENAME = 16
SQLITE_FCNTL_MMAP_SIZE = 18
SQLITE_FCNTL_TRACE = 19
SQLITE_FCNTL_HAS_MOVED = 20
SQLITE_FCNTL_SYNC = 21
SQLITE_FCNTL_COMMIT_PHASETWO = 22
SQLITE_FCNTL_WIN32_SET_HANDLE = 23
SQLITE_FCNTL_WAL_BLOCK = 24
SQLITE_FCNTL_ZIPVFS = 25
SQLITE_FCNTL_RBU = 26
SQLITE_FCNTL_VFS_POINTER = 27
SQLITE_FCNTL_JOURNAL_POINTER = 28
SQLITE_FCNTL_WIN32_GET_HANDLE = 29
SQLITE_FCNTL_PDB = 30
SQLITE_FCNTL_BEGIN_ATOMIC_WRITE = 31
SQLITE_FCNTL_COMMIT_ATOMIC_WRITE = 32
SQLITE_FCNTL_ROLLBACK_ATOMIC_WRITE = 33
SQLITE_FCNTL_LOCK_TIMEOUT = 34
SQLITE_FCNTL_DATA_VERSION = 35
SQLITE_FCNTL_SIZE_LIMIT = 36
SQLITE_FCNTL_CKPT_DONE = 37
SQLITE_FCNTL_RESERVE_BYTES = 38
SQLITE_FCNTL_CKPT_START = 39
SQLITE_GET_LOCKPROXYFILE = 2
SQLITE_SET_LOCKPROXYFILE = 3
SQLITE_LAST_ERRNO = 4
SQLITE_ACCESS_EXISTS = 0
SQLITE_ACCESS_READWRITE = 1
SQLITE_ACCESS_READ = 2
SQLITE_SHM_UNLOCK = 1
SQLITE_SHM_LOCK = 2
SQLITE_SHM_SHARED = 4
SQLITE_SHM_EXCLUSIVE = 8
SQLITE_SHM_NLOCK = 8
SQLITE_CONFIG_SINGLETHREAD = 1
SQLITE_CONFIG_MULTITHREAD = 2
SQLITE_CONFIG_SERIALIZED = 3
SQLITE_CONFIG_MALLOC = 4
SQLITE_CONFIG_GETMALLOC = 5
SQLITE_CONFIG_SCRATCH = 6
SQLITE_CONFIG_PAGECACHE = 7
SQLITE_CONFIG_HEAP = 8
SQLITE_CONFIG_MEMSTATUS = 9
SQLITE_CONFIG_MUTEX = 10
SQLITE_CONFIG_GETMUTEX = 11
SQLITE_CONFIG_LOOKASIDE = 13
SQLITE_CONFIG_PCACHE = 14
SQLITE_CONFIG_GETPCACHE = 15
SQLITE_CONFIG_LOG = 16
SQLITE_CONFIG_URI = 17
SQLITE_CONFIG_PCACHE2 = 18
SQLITE_CONFIG_GETPCACHE2 = 19
SQLITE_CONFIG_COVERING_INDEX_SCAN = 20
SQLITE_CONFIG_SQLLOG = 21
SQLITE_CONFIG_MMAP_SIZE = 22
SQLITE_CONFIG_WIN32_HEAPSIZE = 23
SQLITE_CONFIG_PCACHE_HDRSZ = 24
SQLITE_CONFIG_PMASZ = 25
SQLITE_CONFIG_STMTJRNL_SPILL = 26
SQLITE_CONFIG_SMALL_MALLOC = 27
SQLITE_CONFIG_SORTERREF_SIZE = 28
SQLITE_CONFIG_MEMDB_MAXSIZE = 29
SQLITE_DBCONFIG_MAINDBNAME = 1000
SQLITE_DBCONFIG_LOOKASIDE = 1001
SQLITE_DBCONFIG_ENABLE_FKEY = 1002
SQLITE_DBCONFIG_ENABLE_TRIGGER = 1003
SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER = 1004
SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION = 1005
SQLITE_DBCONFIG_NO_CKPT_ON_CLOSE = 1006
SQLITE_DBCONFIG_ENABLE_QPSG = 1007
SQLITE_DBCONFIG_TRIGGER_EQP = 1008
SQLITE_DBCONFIG_RESET_DATABASE = 1009
SQLITE_DBCONFIG_DEFENSIVE = 1010
SQLITE_DBCONFIG_WRITABLE_SCHEMA = 1011
SQLITE_DBCONFIG_LEGACY_ALTER_TABLE = 1012
SQLITE_DBCONFIG_DQS_DML = 1013
SQLITE_DBCONFIG_DQS_DDL = 1014
SQLITE_DBCONFIG_ENABLE_VIEW = 1015
SQLITE_DBCONFIG_LEGACY_FILE_FORMAT = 1016
SQLITE_DBCONFIG_TRUSTED_SCHEMA = 1017
SQLITE_DBCONFIG_MAX = 1017
SQLITE_DENY = 1
SQLITE_IGNORE = 2
SQLITE_CREATE_INDEX = 1
SQLITE_CREATE_TABLE = 2
SQLITE_CREATE_TEMP_INDEX = 3
SQLITE_CREATE_TEMP_TABLE = 4
SQLITE_CREATE_TEMP_TRIGGER = 5
SQLITE_CREATE_TEMP_VIEW = 6
SQLITE_CREATE_TRIGGER = 7
SQLITE_CREATE_VIEW = 8
SQLITE_DELETE = 9
SQLITE_DROP_INDEX = 10
SQLITE_DROP_TABLE = 11
SQLITE_DROP_TEMP_INDEX = 12
SQLITE_DROP_TEMP_TABLE = 13
SQLITE_DROP_TEMP_TRIGGER = 14
SQLITE_DROP_TEMP_VIEW = 15
SQLITE_DROP_TRIGGER = 16
SQLITE_DROP_VIEW = 17
SQLITE_INSERT = 18
SQLITE_PRAGMA = 19
SQLITE_READ = 20
SQLITE_SELECT = 21
SQLITE_TRANSACTION = 22
SQLITE_UPDATE = 23
SQLITE_ATTACH = 24
SQLITE_DETACH = 25
SQLITE_ALTER_TABLE = 26
SQLITE_REINDEX = 27
SQLITE_ANALYZE = 28
SQLITE_CREATE_VTABLE = 29
SQLITE_DROP_VTABLE = 30
SQLITE_FUNCTION = 31
SQLITE_SAVEPOINT = 32
SQLITE_COPY = 0
SQLITE_RECURSIVE = 33
SQLITE_TRACE_STMT = 1
SQLITE_TRACE_PROFILE = 2
SQLITE_TRACE_ROW = 4
SQLITE_TRACE_CLOSE = 8
SQLITE_LIMIT_LENGTH = 0
SQLITE_LIMIT_SQL_LENGTH = 1
SQLITE_LIMIT_COLUMN = 2
SQLITE_LIMIT_EXPR_DEPTH = 3
SQLITE_LIMIT_COMPOUND_SELECT = 4
SQLITE_LIMIT_VDBE_OP = 5
SQLITE_LIMIT_FUNCTION_ARG = 6
SQLITE_LIMIT_ATTACHED = 7
SQLITE_LIMIT_LIKE_PATTERN_LENGTH = 8
SQLITE_LIMIT_VARIABLE_NUMBER = 9
SQLITE_LIMIT_TRIGGER_DEPTH = 10
SQLITE_LIMIT_WORKER_THREADS = 11
SQLITE_PREPARE_PERSISTENT = 1
SQLITE_PREPARE_NORMALIZE = 2
SQLITE_PREPARE_NO_VTAB = 4
SQLITE_INTEGER = 1
SQLITE_FLOAT = 2
SQLITE_BLOB = 4
SQLITE_NULL = 5
SQLITE3_TEXT = 3
SQLITE_UTF8 = 1
SQLITE_UTF16LE = 2
SQLITE_UTF16BE = 3
SQLITE_UTF16 = 4
SQLITE_ANY = 5
SQLITE_UTF16_ALIGNED = 8
SQLITE_DETERMINISTIC = 2048
SQLITE_DIRECTONLY = 524288
SQLITE_SUBTYPE = 1048576
SQLITE_INNOCUOUS = 2097152
SQLITE_WIN32_DATA_DIRECTORY_TYPE = 1
SQLITE_WIN32_TEMP_DIRECTORY_TYPE = 2
SQLITE_TXN_NONE = 0
SQLITE_TXN_READ = 1
SQLITE_TXN_WRITE = 2
SQLITE_INDEX_SCAN_UNIQUE = 1
SQLITE_INDEX_CONSTRAINT_EQ = 2
SQLITE_INDEX_CONSTRAINT_GT = 4
SQLITE_INDEX_CONSTRAINT_LE = 8
SQLITE_INDEX_CONSTRAINT_LT = 16
SQLITE_INDEX_CONSTRAINT_GE = 32
SQLITE_INDEX_CONSTRAINT_MATCH = 64
SQLITE_INDEX_CONSTRAINT_LIKE = 65
SQLITE_INDEX_CONSTRAINT_GLOB = 66
SQLITE_INDEX_CONSTRAINT_REGEXP = 67
SQLITE_INDEX_CONSTRAINT_NE = 68
SQLITE_INDEX_CONSTRAINT_ISNOT = 69
SQLITE_INDEX_CONSTRAINT_ISNOTNULL = 70
SQLITE_INDEX_CONSTRAINT_ISNULL = 71
SQLITE_INDEX_CONSTRAINT_IS = 72
SQLITE_INDEX_CONSTRAINT_FUNCTION = 150
SQLITE_MUTEX_FAST = 0
SQLITE_MUTEX_RECURSIVE = 1
SQLITE_MUTEX_STATIC_MAIN = 2
SQLITE_MUTEX_STATIC_MEM = 3
SQLITE_MUTEX_STATIC_MEM2 = 4
SQLITE_MUTEX_STATIC_OPEN = 4
SQLITE_MUTEX_STATIC_PRNG = 5
SQLITE_MUTEX_STATIC_LRU = 6
SQLITE_MUTEX_STATIC_LRU2 = 7
SQLITE_MUTEX_STATIC_PMEM = 7
SQLITE_MUTEX_STATIC_APP1 = 8
SQLITE_MUTEX_STATIC_APP2 = 9
SQLITE_MUTEX_STATIC_APP3 = 10
SQLITE_MUTEX_STATIC_VFS1 = 11
SQLITE_MUTEX_STATIC_VFS2 = 12
SQLITE_MUTEX_STATIC_VFS3 = 13
SQLITE_MUTEX_STATIC_MASTER = 2
SQLITE_TESTCTRL_FIRST = 5
SQLITE_TESTCTRL_PRNG_SAVE = 5
SQLITE_TESTCTRL_PRNG_RESTORE = 6
SQLITE_TESTCTRL_PRNG_RESET = 7
SQLITE_TESTCTRL_BITVEC_TEST = 8
SQLITE_TESTCTRL_FAULT_INSTALL = 9
SQLITE_TESTCTRL_BENIGN_MALLOC_HOOKS = 10
SQLITE_TESTCTRL_PENDING_BYTE = 11
SQLITE_TESTCTRL_ASSERT = 12
SQLITE_TESTCTRL_ALWAYS = 13
SQLITE_TESTCTRL_RESERVE = 14
SQLITE_TESTCTRL_OPTIMIZATIONS = 15
SQLITE_TESTCTRL_ISKEYWORD = 16
SQLITE_TESTCTRL_SCRATCHMALLOC = 17
SQLITE_TESTCTRL_INTERNAL_FUNCTIONS = 17
SQLITE_TESTCTRL_LOCALTIME_FAULT = 18
SQLITE_TESTCTRL_EXPLAIN_STMT = 19
SQLITE_TESTCTRL_ONCE_RESET_THRESHOLD = 19
SQLITE_TESTCTRL_NEVER_CORRUPT = 20
SQLITE_TESTCTRL_VDBE_COVERAGE = 21
SQLITE_TESTCTRL_BYTEORDER = 22
SQLITE_TESTCTRL_ISINIT = 23
SQLITE_TESTCTRL_SORTER_MMAP = 24
SQLITE_TESTCTRL_IMPOSTER = 25
SQLITE_TESTCTRL_PARSER_COVERAGE = 26
SQLITE_TESTCTRL_RESULT_INTREAL = 27
SQLITE_TESTCTRL_PRNG_SEED = 28
SQLITE_TESTCTRL_EXTRA_SCHEMA_CHECKS = 29
SQLITE_TESTCTRL_SEEK_COUNT = 30
SQLITE_TESTCTRL_LAST = 30
SQLITE_STATUS_MEMORY_USED = 0
SQLITE_STATUS_PAGECACHE_USED = 1
SQLITE_STATUS_PAGECACHE_OVERFLOW = 2
SQLITE_STATUS_SCRATCH_USED = 3
SQLITE_STATUS_SCRATCH_OVERFLOW = 4
SQLITE_STATUS_MALLOC_SIZE = 5
SQLITE_STATUS_PARSER_STACK = 6
SQLITE_STATUS_PAGECACHE_SIZE = 7
SQLITE_STATUS_SCRATCH_SIZE = 8
SQLITE_STATUS_MALLOC_COUNT = 9
SQLITE_DBSTATUS_LOOKASIDE_USED = 0
SQLITE_DBSTATUS_CACHE_USED = 1
SQLITE_DBSTATUS_SCHEMA_USED = 2
SQLITE_DBSTATUS_STMT_USED = 3
SQLITE_DBSTATUS_LOOKASIDE_HIT = 4
SQLITE_DBSTATUS_LOOKASIDE_MISS_SIZE = 5
SQLITE_DBSTATUS_LOOKASIDE_MISS_FULL = 6
SQLITE_DBSTATUS_CACHE_HIT = 7
SQLITE_DBSTATUS_CACHE_MISS = 8
SQLITE_DBSTATUS_CACHE_WRITE = 9
SQLITE_DBSTATUS_DEFERRED_FKS = 10
SQLITE_DBSTATUS_CACHE_USED_SHARED = 11
SQLITE_DBSTATUS_CACHE_SPILL = 12
SQLITE_DBSTATUS_MAX = 12
SQLITE_STMTSTATUS_FULLSCAN_STEP = 1
SQLITE_STMTSTATUS_SORT = 2
SQLITE_STMTSTATUS_AUTOINDEX = 3
SQLITE_STMTSTATUS_VM_STEP = 4
SQLITE_STMTSTATUS_REPREPARE = 5
SQLITE_STMTSTATUS_RUN = 6
SQLITE_STMTSTATUS_MEMUSED = 99
SQLITE_CHECKPOINT_PASSIVE = 0
SQLITE_CHECKPOINT_FULL = 1
SQLITE_CHECKPOINT_RESTART = 2
SQLITE_CHECKPOINT_TRUNCATE = 3
SQLITE_VTAB_CONSTRAINT_SUPPORT = 1
SQLITE_VTAB_INNOCUOUS = 2
SQLITE_VTAB_DIRECTONLY = 3
SQLITE_ROLLBACK = 1
SQLITE_FAIL = 3
SQLITE_REPLACE = 5
SQLITE_SCANSTAT_NLOOP = 0
SQLITE_SCANSTAT_NVISIT = 1
SQLITE_SCANSTAT_EST = 2
SQLITE_SCANSTAT_NAME = 3
SQLITE_SCANSTAT_EXPLAIN = 4
SQLITE_SCANSTAT_SELECTID = 5
SQLITE_SERIALIZE_NOCOPY = 1
SQLITE_DESERIALIZE_FREEONCLOSE = 1
SQLITE_DESERIALIZE_RESIZEABLE = 2
SQLITE_DESERIALIZE_READONLY = 4
NOT_WITHIN = 0
PARTLY_WITHIN = 1
FULLY_WITHIN = 2
__SQLITESESSION_H_ = 1
SQLITE_CHANGESETSTART_INVERT = 2
SQLITE_CHANGESETAPPLY_NOSAVEPOINT = 1
SQLITE_CHANGESETAPPLY_INVERT = 2
SQLITE_CHANGESET_DATA = 1
SQLITE_CHANGESET_NOTFOUND = 2
SQLITE_CHANGESET_CONFLICT = 3
SQLITE_CHANGESET_CONSTRAINT = 4
SQLITE_CHANGESET_FOREIGN_KEY = 5
SQLITE_CHANGESET_OMIT = 0
SQLITE_CHANGESET_REPLACE = 1
SQLITE_CHANGESET_ABORT = 2
SQLITE_SESSION_CONFIG_STRMSIZE = 1
FTS5_TOKENIZE_QUERY = 1
FTS5_TOKENIZE_PREFIX = 2
FTS5_TOKENIZE_DOCUMENT = 4
FTS5_TOKENIZE_AUX = 8
FTS5_TOKEN_COLOCATED = 1
def _define_sqlite3_head():
    class sqlite3(Structure):
        pass
    return sqlite3
def _define_sqlite3():
    sqlite3 = win32more.System.SqlLite.sqlite3_head
    return sqlite3
def _define_sqlite3_mutex_head():
    class sqlite3_mutex(Structure):
        pass
    return sqlite3_mutex
def _define_sqlite3_mutex():
    sqlite3_mutex = win32more.System.SqlLite.sqlite3_mutex_head
    return sqlite3_mutex
def _define_sqlite3_stmt_head():
    class sqlite3_stmt(Structure):
        pass
    return sqlite3_stmt
def _define_sqlite3_stmt():
    sqlite3_stmt = win32more.System.SqlLite.sqlite3_stmt_head
    return sqlite3_stmt
def _define_sqlite3_value_head():
    class sqlite3_value(Structure):
        pass
    return sqlite3_value
def _define_sqlite3_value():
    sqlite3_value = win32more.System.SqlLite.sqlite3_value_head
    return sqlite3_value
def _define_sqlite3_context_head():
    class sqlite3_context(Structure):
        pass
    return sqlite3_context
def _define_sqlite3_context():
    sqlite3_context = win32more.System.SqlLite.sqlite3_context_head
    return sqlite3_context
def _define_sqlite3_blob_head():
    class sqlite3_blob(Structure):
        pass
    return sqlite3_blob
def _define_sqlite3_blob():
    sqlite3_blob = win32more.System.SqlLite.sqlite3_blob_head
    return sqlite3_blob
def _define_sqlite3_str_head():
    class sqlite3_str(Structure):
        pass
    return sqlite3_str
def _define_sqlite3_str():
    sqlite3_str = win32more.System.SqlLite.sqlite3_str_head
    return sqlite3_str
def _define_sqlite3_pcache_head():
    class sqlite3_pcache(Structure):
        pass
    return sqlite3_pcache
def _define_sqlite3_pcache():
    sqlite3_pcache = win32more.System.SqlLite.sqlite3_pcache_head
    return sqlite3_pcache
def _define_sqlite3_backup_head():
    class sqlite3_backup(Structure):
        pass
    return sqlite3_backup
def _define_sqlite3_backup():
    sqlite3_backup = win32more.System.SqlLite.sqlite3_backup_head
    return sqlite3_backup
def _define_Fts5Context_head():
    class Fts5Context(Structure):
        pass
    return Fts5Context
def _define_Fts5Context():
    Fts5Context = win32more.System.SqlLite.Fts5Context_head
    return Fts5Context
def _define_Fts5Tokenizer_head():
    class Fts5Tokenizer(Structure):
        pass
    return Fts5Tokenizer
def _define_Fts5Tokenizer():
    Fts5Tokenizer = win32more.System.SqlLite.Fts5Tokenizer_head
    return Fts5Tokenizer
def _define_sqlite3_callback():
    return CFUNCTYPE(Int32,c_void_p,Int32,POINTER(POINTER(SByte)),POINTER(POINTER(SByte)), use_last_error=False)
def _define_sqlite3_file_head():
    class sqlite3_file(Structure):
        pass
    return sqlite3_file
def _define_sqlite3_file():
    sqlite3_file = win32more.System.SqlLite.sqlite3_file_head
    sqlite3_file._fields_ = [
        ("pMethods", POINTER(win32more.System.SqlLite.sqlite3_io_methods_head)),
    ]
    return sqlite3_file
def _define_sqlite3_io_methods_head():
    class sqlite3_io_methods(Structure):
        pass
    return sqlite3_io_methods
def _define_sqlite3_io_methods():
    sqlite3_io_methods = win32more.System.SqlLite.sqlite3_io_methods_head
    sqlite3_io_methods._fields_ = [
        ("iVersion", Int32),
        ("xClose", IntPtr),
        ("xRead", IntPtr),
        ("xWrite", IntPtr),
        ("xTruncate", IntPtr),
        ("xSync", IntPtr),
        ("xFileSize", IntPtr),
        ("xLock", IntPtr),
        ("xUnlock", IntPtr),
        ("xCheckReservedLock", IntPtr),
        ("xFileControl", IntPtr),
        ("xSectorSize", IntPtr),
        ("xDeviceCharacteristics", IntPtr),
        ("xShmMap", IntPtr),
        ("xShmLock", IntPtr),
        ("xShmBarrier", IntPtr),
        ("xShmUnmap", IntPtr),
        ("xFetch", IntPtr),
        ("xUnfetch", IntPtr),
    ]
    return sqlite3_io_methods
def _define_sqlite3_syscall_ptr():
    return CFUNCTYPE(Void, use_last_error=False)
def _define_sqlite3_vfs_head():
    class sqlite3_vfs(Structure):
        pass
    return sqlite3_vfs
def _define_sqlite3_vfs():
    sqlite3_vfs = win32more.System.SqlLite.sqlite3_vfs_head
    sqlite3_vfs._fields_ = [
        ("iVersion", Int32),
        ("szOsFile", Int32),
        ("mxPathname", Int32),
        ("pNext", POINTER(win32more.System.SqlLite.sqlite3_vfs_head)),
        ("zName", win32more.Foundation.PSTR),
        ("pAppData", c_void_p),
        ("xOpen", IntPtr),
        ("xDelete", IntPtr),
        ("xAccess", IntPtr),
        ("xFullPathname", IntPtr),
        ("xDlOpen", IntPtr),
        ("xDlError", IntPtr),
        ("xDlSym", IntPtr),
        ("xDlClose", IntPtr),
        ("xRandomness", IntPtr),
        ("xSleep", IntPtr),
        ("xCurrentTime", IntPtr),
        ("xGetLastError", IntPtr),
        ("xCurrentTimeInt64", IntPtr),
        ("xSetSystemCall", IntPtr),
        ("xGetSystemCall", IntPtr),
        ("xNextSystemCall", IntPtr),
    ]
    return sqlite3_vfs
def _define_sqlite3_mem_methods_head():
    class sqlite3_mem_methods(Structure):
        pass
    return sqlite3_mem_methods
def _define_sqlite3_mem_methods():
    sqlite3_mem_methods = win32more.System.SqlLite.sqlite3_mem_methods_head
    sqlite3_mem_methods._fields_ = [
        ("xMalloc", IntPtr),
        ("xFree", IntPtr),
        ("xRealloc", IntPtr),
        ("xSize", IntPtr),
        ("xRoundup", IntPtr),
        ("xInit", IntPtr),
        ("xShutdown", IntPtr),
        ("pAppData", c_void_p),
    ]
    return sqlite3_mem_methods
def _define_sqlite3_destructor_type():
    return CFUNCTYPE(Void,c_void_p, use_last_error=False)
def _define_sqlite3_module_head():
    class sqlite3_module(Structure):
        pass
    return sqlite3_module
def _define_sqlite3_module():
    sqlite3_module = win32more.System.SqlLite.sqlite3_module_head
    sqlite3_module._fields_ = [
        ("iVersion", Int32),
        ("xCreate", IntPtr),
        ("xConnect", IntPtr),
        ("xBestIndex", IntPtr),
        ("xDisconnect", IntPtr),
        ("xDestroy", IntPtr),
        ("xOpen", IntPtr),
        ("xClose", IntPtr),
        ("xFilter", IntPtr),
        ("xNext", IntPtr),
        ("xEof", IntPtr),
        ("xColumn", IntPtr),
        ("xRowid", IntPtr),
        ("xUpdate", IntPtr),
        ("xBegin", IntPtr),
        ("xSync", IntPtr),
        ("xCommit", IntPtr),
        ("xRollback", IntPtr),
        ("xFindFunction", IntPtr),
        ("xRename", IntPtr),
        ("xSavepoint", IntPtr),
        ("xRelease", IntPtr),
        ("xRollbackTo", IntPtr),
        ("xShadowName", IntPtr),
    ]
    return sqlite3_module
def _define_sqlite3_index_info_head():
    class sqlite3_index_info(Structure):
        pass
    return sqlite3_index_info
def _define_sqlite3_index_info():
    sqlite3_index_info = win32more.System.SqlLite.sqlite3_index_info_head
    class sqlite3_index_info_sqlite3_index_orderby(Structure):
        pass
    sqlite3_index_info_sqlite3_index_orderby._fields_ = [
        ("iColumn", Int32),
        ("desc", Byte),
    ]
    class sqlite3_index_info_sqlite3_index_constraint_usage(Structure):
        pass
    sqlite3_index_info_sqlite3_index_constraint_usage._fields_ = [
        ("argvIndex", Int32),
        ("omit", Byte),
    ]
    class sqlite3_index_info_sqlite3_index_constraint(Structure):
        pass
    sqlite3_index_info_sqlite3_index_constraint._fields_ = [
        ("iColumn", Int32),
        ("op", Byte),
        ("usable", Byte),
        ("iTermOffset", Int32),
    ]
    sqlite3_index_info._fields_ = [
        ("nConstraint", Int32),
        ("aConstraint", POINTER(sqlite3_index_info_sqlite3_index_constraint)),
        ("nOrderBy", Int32),
        ("aOrderBy", POINTER(sqlite3_index_info_sqlite3_index_orderby)),
        ("aConstraintUsage", POINTER(sqlite3_index_info_sqlite3_index_constraint_usage)),
        ("idxNum", Int32),
        ("idxStr", win32more.Foundation.PSTR),
        ("needToFreeIdxStr", Int32),
        ("orderByConsumed", Int32),
        ("estimatedCost", Double),
        ("estimatedRows", Int64),
        ("idxFlags", Int32),
        ("colUsed", UInt64),
    ]
    return sqlite3_index_info
def _define_sqlite3_vtab_head():
    class sqlite3_vtab(Structure):
        pass
    return sqlite3_vtab
def _define_sqlite3_vtab():
    sqlite3_vtab = win32more.System.SqlLite.sqlite3_vtab_head
    sqlite3_vtab._fields_ = [
        ("pModule", POINTER(win32more.System.SqlLite.sqlite3_module_head)),
        ("nRef", Int32),
        ("zErrMsg", win32more.Foundation.PSTR),
    ]
    return sqlite3_vtab
def _define_sqlite3_vtab_cursor_head():
    class sqlite3_vtab_cursor(Structure):
        pass
    return sqlite3_vtab_cursor
def _define_sqlite3_vtab_cursor():
    sqlite3_vtab_cursor = win32more.System.SqlLite.sqlite3_vtab_cursor_head
    sqlite3_vtab_cursor._fields_ = [
        ("pVtab", POINTER(win32more.System.SqlLite.sqlite3_vtab_head)),
    ]
    return sqlite3_vtab_cursor
def _define_sqlite3_mutex_methods_head():
    class sqlite3_mutex_methods(Structure):
        pass
    return sqlite3_mutex_methods
def _define_sqlite3_mutex_methods():
    sqlite3_mutex_methods = win32more.System.SqlLite.sqlite3_mutex_methods_head
    sqlite3_mutex_methods._fields_ = [
        ("xMutexInit", IntPtr),
        ("xMutexEnd", IntPtr),
        ("xMutexAlloc", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_mutex_head)))))))))),
        ("xMutexFree", IntPtr),
        ("xMutexEnter", IntPtr),
        ("xMutexTry", IntPtr),
        ("xMutexLeave", IntPtr),
        ("xMutexHeld", IntPtr),
        ("xMutexNotheld", IntPtr),
    ]
    return sqlite3_mutex_methods
def _define_sqlite3_pcache_page_head():
    class sqlite3_pcache_page(Structure):
        pass
    return sqlite3_pcache_page
def _define_sqlite3_pcache_page():
    sqlite3_pcache_page = win32more.System.SqlLite.sqlite3_pcache_page_head
    sqlite3_pcache_page._fields_ = [
        ("pBuf", c_void_p),
        ("pExtra", c_void_p),
    ]
    return sqlite3_pcache_page
def _define_sqlite3_pcache_methods2_head():
    class sqlite3_pcache_methods2(Structure):
        pass
    return sqlite3_pcache_methods2
def _define_sqlite3_pcache_methods2():
    sqlite3_pcache_methods2 = win32more.System.SqlLite.sqlite3_pcache_methods2_head
    sqlite3_pcache_methods2._fields_ = [
        ("iVersion", Int32),
        ("pArg", c_void_p),
        ("xInit", IntPtr),
        ("xShutdown", IntPtr),
        ("xCreate", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_pcache_head)))))))))),
        ("xCachesize", IntPtr),
        ("xPagecount", IntPtr),
        ("xFetch", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_pcache_page_head)))))))))))))))))))),
        ("xUnpin", IntPtr),
        ("xRekey", IntPtr),
        ("xTruncate", IntPtr),
        ("xDestroy", IntPtr),
        ("xShrink", IntPtr),
    ]
    return sqlite3_pcache_methods2
def _define_sqlite3_pcache_methods_head():
    class sqlite3_pcache_methods(Structure):
        pass
    return sqlite3_pcache_methods
def _define_sqlite3_pcache_methods():
    sqlite3_pcache_methods = win32more.System.SqlLite.sqlite3_pcache_methods_head
    sqlite3_pcache_methods._fields_ = [
        ("pArg", c_void_p),
        ("xInit", IntPtr),
        ("xShutdown", IntPtr),
        ("xCreate", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_pcache_head)))))))))),
        ("xCachesize", IntPtr),
        ("xPagecount", IntPtr),
        ("xFetch", IntPtr),
        ("xUnpin", IntPtr),
        ("xRekey", IntPtr),
        ("xTruncate", IntPtr),
        ("xDestroy", IntPtr),
    ]
    return sqlite3_pcache_methods
def _define_sqlite3_snapshot_head():
    class sqlite3_snapshot(Structure):
        pass
    return sqlite3_snapshot
def _define_sqlite3_snapshot():
    sqlite3_snapshot = win32more.System.SqlLite.sqlite3_snapshot_head
    sqlite3_snapshot._fields_ = [
        ("hidden", Byte * 48),
    ]
    return sqlite3_snapshot
def _define_sqlite3_rtree_geometry_head():
    class sqlite3_rtree_geometry(Structure):
        pass
    return sqlite3_rtree_geometry
def _define_sqlite3_rtree_geometry():
    sqlite3_rtree_geometry = win32more.System.SqlLite.sqlite3_rtree_geometry_head
    sqlite3_rtree_geometry._fields_ = [
        ("pContext", c_void_p),
        ("nParam", Int32),
        ("aParam", POINTER(Double)),
        ("pUser", c_void_p),
        ("xDelUser", IntPtr),
    ]
    return sqlite3_rtree_geometry
def _define_sqlite3_rtree_query_info_head():
    class sqlite3_rtree_query_info(Structure):
        pass
    return sqlite3_rtree_query_info
def _define_sqlite3_rtree_query_info():
    sqlite3_rtree_query_info = win32more.System.SqlLite.sqlite3_rtree_query_info_head
    sqlite3_rtree_query_info._fields_ = [
        ("pContext", c_void_p),
        ("nParam", Int32),
        ("aParam", POINTER(Double)),
        ("pUser", c_void_p),
        ("xDelUser", IntPtr),
        ("aCoord", POINTER(Double)),
        ("anQueue", POINTER(UInt32)),
        ("nCoord", Int32),
        ("iLevel", Int32),
        ("mxLevel", Int32),
        ("iRowid", Int64),
        ("rParentScore", Double),
        ("eParentWithin", Int32),
        ("eWithin", Int32),
        ("rScore", Double),
        ("apSqlParam", POINTER(POINTER(win32more.System.SqlLite.sqlite3_value_head))),
    ]
    return sqlite3_rtree_query_info
def _define_fts5_extension_function():
    return CFUNCTYPE(Void,POINTER(win32more.System.SqlLite.Fts5ExtensionApi_head),POINTER(win32more.System.SqlLite.Fts5Context_head),POINTER(win32more.System.SqlLite.sqlite3_context_head),Int32,POINTER(POINTER(win32more.System.SqlLite.sqlite3_value_head)), use_last_error=False)
def _define_Fts5PhraseIter_head():
    class Fts5PhraseIter(Structure):
        pass
    return Fts5PhraseIter
def _define_Fts5PhraseIter():
    Fts5PhraseIter = win32more.System.SqlLite.Fts5PhraseIter_head
    Fts5PhraseIter._fields_ = [
        ("a", c_char_p_no),
        ("b", c_char_p_no),
    ]
    return Fts5PhraseIter
def _define_Fts5ExtensionApi_head():
    class Fts5ExtensionApi(Structure):
        pass
    return Fts5ExtensionApi
def _define_Fts5ExtensionApi():
    Fts5ExtensionApi = win32more.System.SqlLite.Fts5ExtensionApi_head
    Fts5ExtensionApi._fields_ = [
        ("iVersion", Int32),
        ("xUserData", IntPtr),
        ("xColumnCount", IntPtr),
        ("xRowCount", IntPtr),
        ("xColumnTotalSize", IntPtr),
        ("xTokenize", IntPtr),
        ("xPhraseCount", IntPtr),
        ("xPhraseSize", IntPtr),
        ("xInstCount", IntPtr),
        ("xInst", IntPtr),
        ("xRowid", IntPtr),
        ("xColumnText", IntPtr),
        ("xColumnSize", IntPtr),
        ("xQueryPhrase", IntPtr),
        ("xSetAuxdata", IntPtr),
        ("xGetAuxdata", IntPtr),
        ("xPhraseFirst", IntPtr),
        ("xPhraseNext", IntPtr),
        ("xPhraseFirstColumn", IntPtr),
        ("xPhraseNextColumn", IntPtr),
    ]
    return Fts5ExtensionApi
def _define_fts5_tokenizer_head():
    class fts5_tokenizer(Structure):
        pass
    return fts5_tokenizer
def _define_fts5_tokenizer():
    fts5_tokenizer = win32more.System.SqlLite.fts5_tokenizer_head
    fts5_tokenizer._fields_ = [
        ("xCreate", IntPtr),
        ("xDelete", IntPtr),
        ("xTokenize", IntPtr),
    ]
    return fts5_tokenizer
def _define_fts5_api_head():
    class fts5_api(Structure):
        pass
    return fts5_api
def _define_fts5_api():
    fts5_api = win32more.System.SqlLite.fts5_api_head
    fts5_api._fields_ = [
        ("iVersion", Int32),
        ("xCreateTokenizer", IntPtr),
        ("xFindTokenizer", IntPtr),
        ("xCreateFunction", IntPtr),
    ]
    return fts5_api
def _define_sqlite3_api_routines_head():
    class sqlite3_api_routines(Structure):
        pass
    return sqlite3_api_routines
def _define_sqlite3_api_routines():
    sqlite3_api_routines = win32more.System.SqlLite.sqlite3_api_routines_head
    sqlite3_api_routines._fields_ = [
        ("aggregate_context", IntPtr),
        ("aggregate_count", IntPtr),
        ("bind_blob", IntPtr),
        ("bind_double", IntPtr),
        ("bind_int", IntPtr),
        ("bind_int64", IntPtr),
        ("bind_null", IntPtr),
        ("bind_parameter_count", IntPtr),
        ("bind_parameter_index", IntPtr),
        ("bind_parameter_name", IntPtr),
        ("bind_text", IntPtr),
        ("bind_text16", IntPtr),
        ("bind_value", IntPtr),
        ("busy_handler", IntPtr),
        ("busy_timeout", IntPtr),
        ("changes", IntPtr),
        ("close", IntPtr),
        ("collation_needed", IntPtr),
        ("collation_needed16", IntPtr),
        ("column_blob", IntPtr),
        ("column_bytes", IntPtr),
        ("column_bytes16", IntPtr),
        ("column_count", IntPtr),
        ("column_database_name", IntPtr),
        ("column_database_name16", IntPtr),
        ("column_decltype", IntPtr),
        ("column_decltype16", IntPtr),
        ("column_double", IntPtr),
        ("column_int", IntPtr),
        ("column_int64", IntPtr),
        ("column_name", IntPtr),
        ("column_name16", IntPtr),
        ("column_origin_name", IntPtr),
        ("column_origin_name16", IntPtr),
        ("column_table_name", IntPtr),
        ("column_table_name16", IntPtr),
        ("column_text", IntPtr),
        ("column_text16", IntPtr),
        ("column_type", IntPtr),
        ("column_value", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_value_head)))))))))))))))))),
        ("commit_hook", IntPtr),
        ("complete", IntPtr),
        ("complete16", IntPtr),
        ("create_collation", IntPtr),
        ("create_collation16", IntPtr),
        ("create_function", IntPtr),
        ("create_function16", IntPtr),
        ("create_module", IntPtr),
        ("data_count", IntPtr),
        ("db_handle", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_head)))))))))))))))))),
        ("declare_vtab", IntPtr),
        ("enable_shared_cache", IntPtr),
        ("errcode", IntPtr),
        ("errmsg", IntPtr),
        ("errmsg16", IntPtr),
        ("exec", IntPtr),
        ("expired", IntPtr),
        ("finalize", IntPtr),
        ("free", IntPtr),
        ("free_table", IntPtr),
        ("get_autocommit", IntPtr),
        ("get_auxdata", IntPtr),
        ("get_table", IntPtr),
        ("global_recover", IntPtr),
        ("interruptx", IntPtr),
        ("last_insert_rowid", IntPtr),
        ("libversion", IntPtr),
        ("libversion_number", IntPtr),
        ("malloc", IntPtr),
        ("mprintf", IntPtr),
        ("open", IntPtr),
        ("open16", IntPtr),
        ("prepare", IntPtr),
        ("prepare16", IntPtr),
        ("profile", IntPtr),
        ("progress_handler", IntPtr),
        ("realloc", IntPtr),
        ("reset", IntPtr),
        ("result_blob", IntPtr),
        ("result_double", IntPtr),
        ("result_error", IntPtr),
        ("result_error16", IntPtr),
        ("result_int", IntPtr),
        ("result_int64", IntPtr),
        ("result_null", IntPtr),
        ("result_text", IntPtr),
        ("result_text16", IntPtr),
        ("result_text16be", IntPtr),
        ("result_text16le", IntPtr),
        ("result_value", IntPtr),
        ("rollback_hook", IntPtr),
        ("set_authorizer", IntPtr),
        ("set_auxdata", IntPtr),
        ("xsnprintf", IntPtr),
        ("step", IntPtr),
        ("table_column_metadata", IntPtr),
        ("thread_cleanup", IntPtr),
        ("total_changes", IntPtr),
        ("trace", IntPtr),
        ("transfer_bindings", IntPtr),
        ("update_hook", IntPtr),
        ("user_data", IntPtr),
        ("value_blob", IntPtr),
        ("value_bytes", IntPtr),
        ("value_bytes16", IntPtr),
        ("value_double", IntPtr),
        ("value_int", IntPtr),
        ("value_int64", IntPtr),
        ("value_numeric_type", IntPtr),
        ("value_text", IntPtr),
        ("value_text16", IntPtr),
        ("value_text16be", IntPtr),
        ("value_text16le", IntPtr),
        ("value_type", IntPtr),
        ("vmprintf", IntPtr),
        ("overload_function", IntPtr),
        ("prepare_v2", IntPtr),
        ("prepare16_v2", IntPtr),
        ("clear_bindings", IntPtr),
        ("create_module_v2", IntPtr),
        ("bind_zeroblob", IntPtr),
        ("blob_bytes", IntPtr),
        ("blob_close", IntPtr),
        ("blob_open", IntPtr),
        ("blob_read", IntPtr),
        ("blob_write", IntPtr),
        ("create_collation_v2", IntPtr),
        ("file_control", IntPtr),
        ("memory_highwater", IntPtr),
        ("memory_used", IntPtr),
        ("mutex_alloc", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_mutex_head)))))))))),
        ("mutex_enter", IntPtr),
        ("mutex_free", IntPtr),
        ("mutex_leave", IntPtr),
        ("mutex_try", IntPtr),
        ("open_v2", IntPtr),
        ("release_memory", IntPtr),
        ("result_error_nomem", IntPtr),
        ("result_error_toobig", IntPtr),
        ("sleep", IntPtr),
        ("soft_heap_limit", IntPtr),
        ("vfs_find", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_vfs_head))))))))))),
        ("vfs_register", IntPtr),
        ("vfs_unregister", IntPtr),
        ("xthreadsafe", IntPtr),
        ("result_zeroblob", IntPtr),
        ("result_error_code", IntPtr),
        ("test_control", IntPtr),
        ("randomness", IntPtr),
        ("context_db_handle", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_head))))))))))))))))))))),
        ("extended_result_codes", IntPtr),
        ("limit", IntPtr),
        ("next_stmt", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_stmt_head))))))))))))),
        ("sql", IntPtr),
        ("status", IntPtr),
        ("backup_finish", IntPtr),
        ("backup_init", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_backup_head))))))))))))),
        ("backup_pagecount", IntPtr),
        ("backup_remaining", IntPtr),
        ("backup_step", IntPtr),
        ("compileoption_get", IntPtr),
        ("compileoption_used", IntPtr),
        ("create_function_v2", IntPtr),
        ("db_config", IntPtr),
        ("db_mutex", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_mutex_head))))))))))))),
        ("db_status", IntPtr),
        ("extended_errcode", IntPtr),
        ("log", IntPtr),
        ("soft_heap_limit64", IntPtr),
        ("sourceid", IntPtr),
        ("stmt_status", IntPtr),
        ("strnicmp", IntPtr),
        ("unlock_notify", IntPtr),
        ("wal_autocheckpoint", IntPtr),
        ("wal_checkpoint", IntPtr),
        ("wal_hook", IntPtr),
        ("blob_reopen", IntPtr),
        ("vtab_config", IntPtr),
        ("vtab_on_conflict", IntPtr),
        ("close_v2", IntPtr),
        ("db_filename", IntPtr),
        ("db_readonly", IntPtr),
        ("db_release_memory", IntPtr),
        ("errstr", IntPtr),
        ("stmt_busy", IntPtr),
        ("stmt_readonly", IntPtr),
        ("stricmp", IntPtr),
        ("uri_boolean", IntPtr),
        ("uri_int64", IntPtr),
        ("uri_parameter", IntPtr),
        ("xvsnprintf", IntPtr),
        ("wal_checkpoint_v2", IntPtr),
        ("auto_extension", IntPtr),
        ("bind_blob64", IntPtr),
        ("bind_text64", IntPtr),
        ("cancel_auto_extension", IntPtr),
        ("load_extension", IntPtr),
        ("malloc64", IntPtr),
        ("msize", IntPtr),
        ("realloc64", IntPtr),
        ("reset_auto_extension", IntPtr),
        ("result_blob64", IntPtr),
        ("result_text64", IntPtr),
        ("strglob", IntPtr),
        ("value_dup", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_value_head))))))))))),
        ("value_free", IntPtr),
        ("result_zeroblob64", IntPtr),
        ("bind_zeroblob64", IntPtr),
        ("value_subtype", IntPtr),
        ("result_subtype", IntPtr),
        ("status64", IntPtr),
        ("strlike", IntPtr),
        ("db_cacheflush", IntPtr),
        ("system_errno", IntPtr),
        ("trace_v2", IntPtr),
        ("expanded_sql", IntPtr),
        ("set_last_insert_rowid", IntPtr),
        ("prepare_v3", IntPtr),
        ("prepare16_v3", IntPtr),
        ("bind_pointer", IntPtr),
        ("result_pointer", IntPtr),
        ("value_pointer", IntPtr),
        ("vtab_nochange", IntPtr),
        ("value_nochange", IntPtr),
        ("vtab_collation", IntPtr),
        ("keyword_count", IntPtr),
        ("keyword_name", IntPtr),
        ("keyword_check", IntPtr),
        ("str_new", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_str_head))))))))))))),
        ("str_finish", IntPtr),
        ("str_appendf", IntPtr),
        ("str_vappendf", IntPtr),
        ("str_append", IntPtr),
        ("str_appendall", IntPtr),
        ("str_appendchar", IntPtr),
        ("str_reset", IntPtr),
        ("str_errcode", IntPtr),
        ("str_length", IntPtr),
        ("str_value", IntPtr),
        ("create_window_function", IntPtr),
        ("normalized_sql", IntPtr),
        ("stmt_isexplain", IntPtr),
        ("value_frombind", IntPtr),
        ("drop_modules", IntPtr),
        ("hard_heap_limit64", IntPtr),
        ("uri_key", IntPtr),
        ("filename_database", IntPtr),
        ("filename_journal", IntPtr),
        ("filename_wal", IntPtr),
        ("create_filename", IntPtr),
        ("free_filename", IntPtr),
        ("database_file_object", POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(POINTER(win32more.System.SqlLite.sqlite3_file_head))))))))))),
        ("txn_state", IntPtr),
    ]
    return sqlite3_api_routines
def _define_sqlite3_loadext_entry():
    return CFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),POINTER(POINTER(SByte)),POINTER(win32more.System.SqlLite.sqlite3_api_routines_head), use_last_error=False)
def _define_sqlite3_libversion():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_libversion", windll["winsqlite3"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_sourceid():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_sourceid", windll["winsqlite3"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_libversion_number():
    try:
        return WINFUNCTYPE(Int32, use_last_error=False)(("sqlite3_libversion_number", windll["winsqlite3"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_compileoption_used():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_compileoption_used", windll["winsqlite3"]), ((1, 'zOptName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_compileoption_get():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,Int32, use_last_error=False)(("sqlite3_compileoption_get", windll["winsqlite3"]), ((1, 'N'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_threadsafe():
    try:
        return WINFUNCTYPE(Int32, use_last_error=False)(("sqlite3_threadsafe", windll["winsqlite3"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_close():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_close", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_close_v2():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_close_v2", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_exec():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,IntPtr,c_void_p,POINTER(POINTER(SByte)), use_last_error=False)(("sqlite3_exec", windll["winsqlite3"]), ((1, 'param0'),(1, 'sql'),(1, 'callback'),(1, 'param3'),(1, 'errmsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_initialize():
    try:
        return WINFUNCTYPE(Int32, use_last_error=False)(("sqlite3_initialize", windll["winsqlite3"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_shutdown():
    try:
        return WINFUNCTYPE(Int32, use_last_error=False)(("sqlite3_shutdown", windll["winsqlite3"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_os_init():
    try:
        return WINFUNCTYPE(Int32, use_last_error=False)(("sqlite3_os_init", windll["winsqlite3"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_os_end():
    try:
        return WINFUNCTYPE(Int32, use_last_error=False)(("sqlite3_os_end", windll["winsqlite3"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_config():
    try:
        return WINFUNCTYPE(Int32,Int32, use_last_error=False)(("sqlite3_config", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_db_config():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),Int32, use_last_error=False)(("sqlite3_db_config", windll["winsqlite3"]), ((1, 'param0'),(1, 'op'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_extended_result_codes():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),Int32, use_last_error=False)(("sqlite3_extended_result_codes", windll["winsqlite3"]), ((1, 'param0'),(1, 'onoff'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_last_insert_rowid():
    try:
        return WINFUNCTYPE(Int64,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_last_insert_rowid", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_set_last_insert_rowid():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_head),Int64, use_last_error=False)(("sqlite3_set_last_insert_rowid", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_changes():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_changes", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_total_changes():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_total_changes", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_interrupt():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_interrupt", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_complete():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_complete", windll["winsqlite3"]), ((1, 'sql'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_complete16():
    try:
        return WINFUNCTYPE(Int32,c_void_p, use_last_error=False)(("sqlite3_complete16", windll["winsqlite3"]), ((1, 'sql'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_busy_handler():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),IntPtr,c_void_p, use_last_error=False)(("sqlite3_busy_handler", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_busy_timeout():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),Int32, use_last_error=False)(("sqlite3_busy_timeout", windll["winsqlite3"]), ((1, 'param0'),(1, 'ms'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_get_table():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,POINTER(POINTER(POINTER(SByte))),POINTER(Int32),POINTER(Int32),POINTER(POINTER(SByte)), use_last_error=False)(("sqlite3_get_table", windll["winsqlite3"]), ((1, 'db'),(1, 'zSql'),(1, 'pazResult'),(1, 'pnRow'),(1, 'pnColumn'),(1, 'pzErrmsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_free_table():
    try:
        return WINFUNCTYPE(Void,POINTER(POINTER(SByte)), use_last_error=False)(("sqlite3_free_table", windll["winsqlite3"]), ((1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_mprintf():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_mprintf", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_vmprintf():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(SByte), use_last_error=False)(("sqlite3_vmprintf", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_snprintf():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_snprintf", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_vsnprintf():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(SByte), use_last_error=False)(("sqlite3_vsnprintf", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_malloc():
    try:
        return WINFUNCTYPE(c_void_p,Int32, use_last_error=False)(("sqlite3_malloc", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_malloc64():
    try:
        return WINFUNCTYPE(c_void_p,UInt64, use_last_error=False)(("sqlite3_malloc64", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_realloc():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p,Int32, use_last_error=False)(("sqlite3_realloc", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_realloc64():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p,UInt64, use_last_error=False)(("sqlite3_realloc64", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_free():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("sqlite3_free", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_msize():
    try:
        return WINFUNCTYPE(UInt64,c_void_p, use_last_error=False)(("sqlite3_msize", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_memory_used():
    try:
        return WINFUNCTYPE(Int64, use_last_error=False)(("sqlite3_memory_used", windll["winsqlite3"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_memory_highwater():
    try:
        return WINFUNCTYPE(Int64,Int32, use_last_error=False)(("sqlite3_memory_highwater", windll["winsqlite3"]), ((1, 'resetFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_randomness():
    try:
        return WINFUNCTYPE(Void,Int32,c_void_p, use_last_error=False)(("sqlite3_randomness", windll["winsqlite3"]), ((1, 'N'),(1, 'P'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_set_authorizer():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),IntPtr,c_void_p, use_last_error=False)(("sqlite3_set_authorizer", windll["winsqlite3"]), ((1, 'param0'),(1, 'xAuth'),(1, 'pUserData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_trace():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_head),IntPtr,c_void_p, use_last_error=False)(("sqlite3_trace", windll["winsqlite3"]), ((1, 'param0'),(1, 'xTrace'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_profile():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_head),IntPtr,c_void_p, use_last_error=False)(("sqlite3_profile", windll["winsqlite3"]), ((1, 'param0'),(1, 'xProfile'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_trace_v2():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),UInt32,IntPtr,c_void_p, use_last_error=False)(("sqlite3_trace_v2", windll["winsqlite3"]), ((1, 'param0'),(1, 'uMask'),(1, 'xCallback'),(1, 'pCtx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_progress_handler():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_head),Int32,IntPtr,c_void_p, use_last_error=False)(("sqlite3_progress_handler", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_open():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,POINTER(POINTER(win32more.System.SqlLite.sqlite3_head)), use_last_error=False)(("sqlite3_open", windll["winsqlite3"]), ((1, 'filename'),(1, 'ppDb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_open16():
    try:
        return WINFUNCTYPE(Int32,c_void_p,POINTER(POINTER(win32more.System.SqlLite.sqlite3_head)), use_last_error=False)(("sqlite3_open16", windll["winsqlite3"]), ((1, 'filename'),(1, 'ppDb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_open_v2():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,POINTER(POINTER(win32more.System.SqlLite.sqlite3_head)),Int32,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_open_v2", windll["winsqlite3"]), ((1, 'filename'),(1, 'ppDb'),(1, 'flags'),(1, 'zVfs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_uri_parameter():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_uri_parameter", windll["winsqlite3"]), ((1, 'zFilename'),(1, 'zParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_uri_boolean():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32, use_last_error=False)(("sqlite3_uri_boolean", windll["winsqlite3"]), ((1, 'zFile'),(1, 'zParam'),(1, 'bDefault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_uri_int64():
    try:
        return WINFUNCTYPE(Int64,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int64, use_last_error=False)(("sqlite3_uri_int64", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_uri_key():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32, use_last_error=False)(("sqlite3_uri_key", windll["winsqlite3"]), ((1, 'zFilename'),(1, 'N'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_filename_database():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_filename_database", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_filename_journal():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_filename_journal", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_filename_wal():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_filename_wal", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_database_file_object():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.SqlLite.sqlite3_file_head),win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_database_file_object", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_create_filename():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32,POINTER(POINTER(SByte)), use_last_error=False)(("sqlite3_create_filename", windll["winsqlite3"]), ((1, 'zDatabase'),(1, 'zJournal'),(1, 'zWal'),(1, 'nParam'),(1, 'azParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_free_filename():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_free_filename", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_errcode():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_errcode", windll["winsqlite3"]), ((1, 'db'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_extended_errcode():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_extended_errcode", windll["winsqlite3"]), ((1, 'db'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_errmsg():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_errmsg", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_errmsg16():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_errmsg16", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_errstr():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,Int32, use_last_error=False)(("sqlite3_errstr", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_limit():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),Int32,Int32, use_last_error=False)(("sqlite3_limit", windll["winsqlite3"]), ((1, 'param0'),(1, 'id'),(1, 'newVal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_prepare():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,Int32,POINTER(POINTER(win32more.System.SqlLite.sqlite3_stmt_head)),POINTER(POINTER(SByte)), use_last_error=False)(("sqlite3_prepare", windll["winsqlite3"]), ((1, 'db'),(1, 'zSql'),(1, 'nByte'),(1, 'ppStmt'),(1, 'pzTail'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_prepare_v2():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,Int32,POINTER(POINTER(win32more.System.SqlLite.sqlite3_stmt_head)),POINTER(POINTER(SByte)), use_last_error=False)(("sqlite3_prepare_v2", windll["winsqlite3"]), ((1, 'db'),(1, 'zSql'),(1, 'nByte'),(1, 'ppStmt'),(1, 'pzTail'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_prepare_v3():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,Int32,UInt32,POINTER(POINTER(win32more.System.SqlLite.sqlite3_stmt_head)),POINTER(POINTER(SByte)), use_last_error=False)(("sqlite3_prepare_v3", windll["winsqlite3"]), ((1, 'db'),(1, 'zSql'),(1, 'nByte'),(1, 'prepFlags'),(1, 'ppStmt'),(1, 'pzTail'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_prepare16():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),c_void_p,Int32,POINTER(POINTER(win32more.System.SqlLite.sqlite3_stmt_head)),POINTER(c_void_p), use_last_error=False)(("sqlite3_prepare16", windll["winsqlite3"]), ((1, 'db'),(1, 'zSql'),(1, 'nByte'),(1, 'ppStmt'),(1, 'pzTail'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_prepare16_v2():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),c_void_p,Int32,POINTER(POINTER(win32more.System.SqlLite.sqlite3_stmt_head)),POINTER(c_void_p), use_last_error=False)(("sqlite3_prepare16_v2", windll["winsqlite3"]), ((1, 'db'),(1, 'zSql'),(1, 'nByte'),(1, 'ppStmt'),(1, 'pzTail'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_prepare16_v3():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),c_void_p,Int32,UInt32,POINTER(POINTER(win32more.System.SqlLite.sqlite3_stmt_head)),POINTER(c_void_p), use_last_error=False)(("sqlite3_prepare16_v3", windll["winsqlite3"]), ((1, 'db'),(1, 'zSql'),(1, 'nByte'),(1, 'prepFlags'),(1, 'ppStmt'),(1, 'pzTail'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_sql():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_sql", windll["winsqlite3"]), ((1, 'pStmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_expanded_sql():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_expanded_sql", windll["winsqlite3"]), ((1, 'pStmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_stmt_readonly():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_stmt_readonly", windll["winsqlite3"]), ((1, 'pStmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_stmt_isexplain():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_stmt_isexplain", windll["winsqlite3"]), ((1, 'pStmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_stmt_busy():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_stmt_busy", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_blob():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32,c_void_p,Int32,IntPtr, use_last_error=False)(("sqlite3_bind_blob", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'n'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_blob64():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32,c_void_p,UInt64,IntPtr, use_last_error=False)(("sqlite3_bind_blob64", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_double():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32,Double, use_last_error=False)(("sqlite3_bind_double", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_int():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32,Int32, use_last_error=False)(("sqlite3_bind_int", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_int64():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32,Int64, use_last_error=False)(("sqlite3_bind_int64", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_null():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_bind_null", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_text():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32,win32more.Foundation.PSTR,Int32,IntPtr, use_last_error=False)(("sqlite3_bind_text", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_text16():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32,c_void_p,Int32,IntPtr, use_last_error=False)(("sqlite3_bind_text16", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_text64():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32,win32more.Foundation.PSTR,UInt64,IntPtr,Byte, use_last_error=False)(("sqlite3_bind_text64", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),(1, 'encoding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_value():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_bind_value", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_pointer():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32,c_void_p,win32more.Foundation.PSTR,IntPtr, use_last_error=False)(("sqlite3_bind_pointer", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_zeroblob():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32,Int32, use_last_error=False)(("sqlite3_bind_zeroblob", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'n'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_zeroblob64():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32,UInt64, use_last_error=False)(("sqlite3_bind_zeroblob64", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_parameter_count():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_bind_parameter_count", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_parameter_name():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_bind_parameter_name", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_bind_parameter_index():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_bind_parameter_index", windll["winsqlite3"]), ((1, 'param0'),(1, 'zName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_clear_bindings():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_clear_bindings", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_count():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_column_count", windll["winsqlite3"]), ((1, 'pStmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_name():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_name", windll["winsqlite3"]), ((1, 'param0'),(1, 'N'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_name16():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_name16", windll["winsqlite3"]), ((1, 'param0'),(1, 'N'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_database_name():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_database_name", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_database_name16():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_database_name16", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_table_name():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_table_name", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_table_name16():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_table_name16", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_origin_name():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_origin_name", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_origin_name16():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_origin_name16", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_decltype():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_decltype", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_decltype16():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_decltype16", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_step():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_step", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_data_count():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_data_count", windll["winsqlite3"]), ((1, 'pStmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_blob():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_blob", windll["winsqlite3"]), ((1, 'param0'),(1, 'iCol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_double():
    try:
        return WINFUNCTYPE(Double,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_double", windll["winsqlite3"]), ((1, 'param0'),(1, 'iCol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_int():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_int", windll["winsqlite3"]), ((1, 'param0'),(1, 'iCol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_int64():
    try:
        return WINFUNCTYPE(Int64,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_int64", windll["winsqlite3"]), ((1, 'param0'),(1, 'iCol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_text():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_text", windll["winsqlite3"]), ((1, 'param0'),(1, 'iCol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_text16():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_text16", windll["winsqlite3"]), ((1, 'param0'),(1, 'iCol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_value():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.SqlLite.sqlite3_value_head),POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_value", windll["winsqlite3"]), ((1, 'param0'),(1, 'iCol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_bytes():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_bytes", windll["winsqlite3"]), ((1, 'param0'),(1, 'iCol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_bytes16():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_bytes16", windll["winsqlite3"]), ((1, 'param0'),(1, 'iCol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_column_type():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32, use_last_error=False)(("sqlite3_column_type", windll["winsqlite3"]), ((1, 'param0'),(1, 'iCol'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_finalize():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_finalize", windll["winsqlite3"]), ((1, 'pStmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_reset():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_reset", windll["winsqlite3"]), ((1, 'pStmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_create_function():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,Int32,Int32,c_void_p,IntPtr,IntPtr,IntPtr, use_last_error=False)(("sqlite3_create_function", windll["winsqlite3"]), ((1, 'db'),(1, 'zFunctionName'),(1, 'nArg'),(1, 'eTextRep'),(1, 'pApp'),(1, 'xFunc'),(1, 'xStep'),(1, 'xFinal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_create_function16():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),c_void_p,Int32,Int32,c_void_p,IntPtr,IntPtr,IntPtr, use_last_error=False)(("sqlite3_create_function16", windll["winsqlite3"]), ((1, 'db'),(1, 'zFunctionName'),(1, 'nArg'),(1, 'eTextRep'),(1, 'pApp'),(1, 'xFunc'),(1, 'xStep'),(1, 'xFinal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_create_function_v2():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,Int32,Int32,c_void_p,IntPtr,IntPtr,IntPtr,IntPtr, use_last_error=False)(("sqlite3_create_function_v2", windll["winsqlite3"]), ((1, 'db'),(1, 'zFunctionName'),(1, 'nArg'),(1, 'eTextRep'),(1, 'pApp'),(1, 'xFunc'),(1, 'xStep'),(1, 'xFinal'),(1, 'xDestroy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_create_window_function():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,Int32,Int32,c_void_p,IntPtr,IntPtr,IntPtr,IntPtr,IntPtr, use_last_error=False)(("sqlite3_create_window_function", windll["winsqlite3"]), ((1, 'db'),(1, 'zFunctionName'),(1, 'nArg'),(1, 'eTextRep'),(1, 'pApp'),(1, 'xStep'),(1, 'xFinal'),(1, 'xValue'),(1, 'xInverse'),(1, 'xDestroy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_aggregate_count():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_context_head), use_last_error=False)(("sqlite3_aggregate_count", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_expired():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_expired", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_transfer_bindings():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_transfer_bindings", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_global_recover():
    try:
        return WINFUNCTYPE(Int32, use_last_error=False)(("sqlite3_global_recover", windll["winsqlite3"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_thread_cleanup():
    try:
        return WINFUNCTYPE(Void, use_last_error=False)(("sqlite3_thread_cleanup", windll["winsqlite3"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_memory_alarm():
    try:
        return WINFUNCTYPE(Int32,IntPtr,c_void_p,Int64, use_last_error=False)(("sqlite3_memory_alarm", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_blob():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_blob", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_double():
    try:
        return WINFUNCTYPE(Double,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_double", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_int():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_int", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_int64():
    try:
        return WINFUNCTYPE(Int64,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_int64", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_pointer():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_value_head),win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_value_pointer", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_text():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_text", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_text16():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_text16", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_text16le():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_text16le", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_text16be():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_text16be", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_bytes():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_bytes", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_bytes16():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_bytes16", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_type():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_type", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_numeric_type():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_numeric_type", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_nochange():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_nochange", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_frombind():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_frombind", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_subtype():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_subtype", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_dup():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.SqlLite.sqlite3_value_head),POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_dup", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_value_free():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_value_free", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_aggregate_context():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_context_head),Int32, use_last_error=False)(("sqlite3_aggregate_context", windll["winsqlite3"]), ((1, 'param0'),(1, 'nBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_user_data():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_context_head), use_last_error=False)(("sqlite3_user_data", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_context_db_handle():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.SqlLite.sqlite3_head),POINTER(win32more.System.SqlLite.sqlite3_context_head), use_last_error=False)(("sqlite3_context_db_handle", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_get_auxdata():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_context_head),Int32, use_last_error=False)(("sqlite3_get_auxdata", windll["winsqlite3"]), ((1, 'param0'),(1, 'N'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_set_auxdata():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),Int32,c_void_p,IntPtr, use_last_error=False)(("sqlite3_set_auxdata", windll["winsqlite3"]), ((1, 'param0'),(1, 'N'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_blob():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),c_void_p,Int32,IntPtr, use_last_error=False)(("sqlite3_result_blob", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_blob64():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),c_void_p,UInt64,IntPtr, use_last_error=False)(("sqlite3_result_blob64", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_double():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),Double, use_last_error=False)(("sqlite3_result_double", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_error():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),win32more.Foundation.PSTR,Int32, use_last_error=False)(("sqlite3_result_error", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_error16():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),c_void_p,Int32, use_last_error=False)(("sqlite3_result_error16", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_error_toobig():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head), use_last_error=False)(("sqlite3_result_error_toobig", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_error_nomem():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head), use_last_error=False)(("sqlite3_result_error_nomem", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_error_code():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),Int32, use_last_error=False)(("sqlite3_result_error_code", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_int():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),Int32, use_last_error=False)(("sqlite3_result_int", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_int64():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),Int64, use_last_error=False)(("sqlite3_result_int64", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_null():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head), use_last_error=False)(("sqlite3_result_null", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_text():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),win32more.Foundation.PSTR,Int32,IntPtr, use_last_error=False)(("sqlite3_result_text", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_text64():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),win32more.Foundation.PSTR,UInt64,IntPtr,Byte, use_last_error=False)(("sqlite3_result_text64", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'encoding'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_text16():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),c_void_p,Int32,IntPtr, use_last_error=False)(("sqlite3_result_text16", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_text16le():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),c_void_p,Int32,IntPtr, use_last_error=False)(("sqlite3_result_text16le", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_text16be():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),c_void_p,Int32,IntPtr, use_last_error=False)(("sqlite3_result_text16be", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_value():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),POINTER(win32more.System.SqlLite.sqlite3_value_head), use_last_error=False)(("sqlite3_result_value", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_pointer():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),c_void_p,win32more.Foundation.PSTR,IntPtr, use_last_error=False)(("sqlite3_result_pointer", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_zeroblob():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),Int32, use_last_error=False)(("sqlite3_result_zeroblob", windll["winsqlite3"]), ((1, 'param0'),(1, 'n'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_zeroblob64():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_context_head),UInt64, use_last_error=False)(("sqlite3_result_zeroblob64", windll["winsqlite3"]), ((1, 'param0'),(1, 'n'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_result_subtype():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_context_head),UInt32, use_last_error=False)(("sqlite3_result_subtype", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_create_collation():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,Int32,c_void_p,IntPtr, use_last_error=False)(("sqlite3_create_collation", windll["winsqlite3"]), ((1, 'param0'),(1, 'zName'),(1, 'eTextRep'),(1, 'pArg'),(1, 'xCompare'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_create_collation_v2():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,Int32,c_void_p,IntPtr,IntPtr, use_last_error=False)(("sqlite3_create_collation_v2", windll["winsqlite3"]), ((1, 'param0'),(1, 'zName'),(1, 'eTextRep'),(1, 'pArg'),(1, 'xCompare'),(1, 'xDestroy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_create_collation16():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),c_void_p,Int32,c_void_p,IntPtr, use_last_error=False)(("sqlite3_create_collation16", windll["winsqlite3"]), ((1, 'param0'),(1, 'zName'),(1, 'eTextRep'),(1, 'pArg'),(1, 'xCompare'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_collation_needed():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),c_void_p,IntPtr, use_last_error=False)(("sqlite3_collation_needed", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_collation_needed16():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),c_void_p,IntPtr, use_last_error=False)(("sqlite3_collation_needed16", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_sleep():
    try:
        return WINFUNCTYPE(Int32,Int32, use_last_error=False)(("sqlite3_sleep", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_win32_set_directory():
    try:
        return WINFUNCTYPE(Int32,UInt32,c_void_p, use_last_error=False)(("sqlite3_win32_set_directory", windll["winsqlite3"]), ((1, 'type'),(1, 'zValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_win32_set_directory8():
    try:
        return WINFUNCTYPE(Int32,UInt32,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_win32_set_directory8", windll["winsqlite3"]), ((1, 'type'),(1, 'zValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_win32_set_directory16():
    try:
        return WINFUNCTYPE(Int32,UInt32,c_void_p, use_last_error=False)(("sqlite3_win32_set_directory16", windll["winsqlite3"]), ((1, 'type'),(1, 'zValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_get_autocommit():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_get_autocommit", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_db_handle():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.SqlLite.sqlite3_head),POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_db_handle", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_db_filename():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_db_filename", windll["winsqlite3"]), ((1, 'db'),(1, 'zDbName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_db_readonly():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_db_readonly", windll["winsqlite3"]), ((1, 'db'),(1, 'zDbName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_txn_state():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_txn_state", windll["winsqlite3"]), ((1, 'param0'),(1, 'zSchema'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_next_stmt():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.SqlLite.sqlite3_stmt_head),POINTER(win32more.System.SqlLite.sqlite3_head),POINTER(win32more.System.SqlLite.sqlite3_stmt_head), use_last_error=False)(("sqlite3_next_stmt", windll["winsqlite3"]), ((1, 'pDb'),(1, 'pStmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_commit_hook():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_head),IntPtr,c_void_p, use_last_error=False)(("sqlite3_commit_hook", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_rollback_hook():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_head),IntPtr,c_void_p, use_last_error=False)(("sqlite3_rollback_hook", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_update_hook():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_head),IntPtr,c_void_p, use_last_error=False)(("sqlite3_update_hook", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_enable_shared_cache():
    try:
        return WINFUNCTYPE(Int32,Int32, use_last_error=False)(("sqlite3_enable_shared_cache", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_release_memory():
    try:
        return WINFUNCTYPE(Int32,Int32, use_last_error=False)(("sqlite3_release_memory", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_db_release_memory():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_db_release_memory", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_soft_heap_limit64():
    try:
        return WINFUNCTYPE(Int64,Int64, use_last_error=False)(("sqlite3_soft_heap_limit64", windll["winsqlite3"]), ((1, 'N'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_hard_heap_limit64():
    try:
        return WINFUNCTYPE(Int64,Int64, use_last_error=False)(("sqlite3_hard_heap_limit64", windll["winsqlite3"]), ((1, 'N'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_soft_heap_limit():
    try:
        return WINFUNCTYPE(Void,Int32, use_last_error=False)(("sqlite3_soft_heap_limit", windll["winsqlite3"]), ((1, 'N'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_table_column_metadata():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(POINTER(SByte)),POINTER(POINTER(SByte)),POINTER(Int32),POINTER(Int32),POINTER(Int32), use_last_error=False)(("sqlite3_table_column_metadata", windll["winsqlite3"]), ((1, 'db'),(1, 'zDbName'),(1, 'zTableName'),(1, 'zColumnName'),(1, 'pzDataType'),(1, 'pzCollSeq'),(1, 'pNotNull'),(1, 'pPrimaryKey'),(1, 'pAutoinc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_load_extension():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(POINTER(SByte)), use_last_error=False)(("sqlite3_load_extension", windll["winsqlite3"]), ((1, 'db'),(1, 'zFile'),(1, 'zProc'),(1, 'pzErrMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_enable_load_extension():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),Int32, use_last_error=False)(("sqlite3_enable_load_extension", windll["winsqlite3"]), ((1, 'db'),(1, 'onoff'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_auto_extension():
    try:
        return WINFUNCTYPE(Int32,IntPtr, use_last_error=False)(("sqlite3_auto_extension", windll["winsqlite3"]), ((1, 'xEntryPoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_cancel_auto_extension():
    try:
        return WINFUNCTYPE(Int32,IntPtr, use_last_error=False)(("sqlite3_cancel_auto_extension", windll["winsqlite3"]), ((1, 'xEntryPoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_reset_auto_extension():
    try:
        return WINFUNCTYPE(Void, use_last_error=False)(("sqlite3_reset_auto_extension", windll["winsqlite3"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_create_module():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_module_head),c_void_p, use_last_error=False)(("sqlite3_create_module", windll["winsqlite3"]), ((1, 'db'),(1, 'zName'),(1, 'p'),(1, 'pClientData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_create_module_v2():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_module_head),c_void_p,IntPtr, use_last_error=False)(("sqlite3_create_module_v2", windll["winsqlite3"]), ((1, 'db'),(1, 'zName'),(1, 'p'),(1, 'pClientData'),(1, 'xDestroy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_drop_modules():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),POINTER(POINTER(SByte)), use_last_error=False)(("sqlite3_drop_modules", windll["winsqlite3"]), ((1, 'db'),(1, 'azKeep'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_declare_vtab():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_declare_vtab", windll["winsqlite3"]), ((1, 'param0'),(1, 'zSQL'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_overload_function():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,Int32, use_last_error=False)(("sqlite3_overload_function", windll["winsqlite3"]), ((1, 'param0'),(1, 'zFuncName'),(1, 'nArg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_blob_open():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int64,Int32,POINTER(POINTER(win32more.System.SqlLite.sqlite3_blob_head)), use_last_error=False)(("sqlite3_blob_open", windll["winsqlite3"]), ((1, 'param0'),(1, 'zDb'),(1, 'zTable'),(1, 'zColumn'),(1, 'iRow'),(1, 'flags'),(1, 'ppBlob'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_blob_reopen():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_blob_head),Int64, use_last_error=False)(("sqlite3_blob_reopen", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_blob_close():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_blob_head), use_last_error=False)(("sqlite3_blob_close", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_blob_bytes():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_blob_head), use_last_error=False)(("sqlite3_blob_bytes", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_blob_read():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_blob_head),c_void_p,Int32,Int32, use_last_error=False)(("sqlite3_blob_read", windll["winsqlite3"]), ((1, 'param0'),(1, 'Z'),(1, 'N'),(1, 'iOffset'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_blob_write():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_blob_head),c_void_p,Int32,Int32, use_last_error=False)(("sqlite3_blob_write", windll["winsqlite3"]), ((1, 'param0'),(1, 'z'),(1, 'n'),(1, 'iOffset'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_vfs_find():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.SqlLite.sqlite3_vfs_head),win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_vfs_find", windll["winsqlite3"]), ((1, 'zVfsName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_vfs_register():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_vfs_head),Int32, use_last_error=False)(("sqlite3_vfs_register", windll["winsqlite3"]), ((1, 'param0'),(1, 'makeDflt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_vfs_unregister():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_vfs_head), use_last_error=False)(("sqlite3_vfs_unregister", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_mutex_alloc():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.SqlLite.sqlite3_mutex_head),Int32, use_last_error=False)(("sqlite3_mutex_alloc", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_mutex_free():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_mutex_head), use_last_error=False)(("sqlite3_mutex_free", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_mutex_enter():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_mutex_head), use_last_error=False)(("sqlite3_mutex_enter", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_mutex_try():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_mutex_head), use_last_error=False)(("sqlite3_mutex_try", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_mutex_leave():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_mutex_head), use_last_error=False)(("sqlite3_mutex_leave", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_db_mutex():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.SqlLite.sqlite3_mutex_head),POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_db_mutex", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_file_control():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,Int32,c_void_p, use_last_error=False)(("sqlite3_file_control", windll["winsqlite3"]), ((1, 'param0'),(1, 'zDbName'),(1, 'op'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_test_control():
    try:
        return WINFUNCTYPE(Int32,Int32, use_last_error=False)(("sqlite3_test_control", windll["winsqlite3"]), ((1, 'op'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_keyword_count():
    try:
        return WINFUNCTYPE(Int32, use_last_error=False)(("sqlite3_keyword_count", windll["winsqlite3"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_keyword_name():
    try:
        return WINFUNCTYPE(Int32,Int32,POINTER(POINTER(SByte)),POINTER(Int32), use_last_error=False)(("sqlite3_keyword_name", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_keyword_check():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,Int32, use_last_error=False)(("sqlite3_keyword_check", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_str_new():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.SqlLite.sqlite3_str_head),POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_str_new", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_str_finish():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_str_head), use_last_error=False)(("sqlite3_str_finish", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_str_appendf():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_str_head),win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_str_appendf", windll["winsqlite3"]), ((1, 'param0'),(1, 'zFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_str_vappendf():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_str_head),win32more.Foundation.PSTR,POINTER(SByte), use_last_error=False)(("sqlite3_str_vappendf", windll["winsqlite3"]), ((1, 'param0'),(1, 'zFormat'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_str_append():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_str_head),win32more.Foundation.PSTR,Int32, use_last_error=False)(("sqlite3_str_append", windll["winsqlite3"]), ((1, 'param0'),(1, 'zIn'),(1, 'N'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_str_appendall():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_str_head),win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_str_appendall", windll["winsqlite3"]), ((1, 'param0'),(1, 'zIn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_str_appendchar():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_str_head),Int32,win32more.Foundation.CHAR, use_last_error=False)(("sqlite3_str_appendchar", windll["winsqlite3"]), ((1, 'param0'),(1, 'N'),(1, 'C'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_str_reset():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.SqlLite.sqlite3_str_head), use_last_error=False)(("sqlite3_str_reset", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_str_errcode():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_str_head), use_last_error=False)(("sqlite3_str_errcode", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_str_length():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_str_head), use_last_error=False)(("sqlite3_str_length", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_str_value():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_str_head), use_last_error=False)(("sqlite3_str_value", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_status():
    try:
        return WINFUNCTYPE(Int32,Int32,POINTER(Int32),POINTER(Int32),Int32, use_last_error=False)(("sqlite3_status", windll["winsqlite3"]), ((1, 'op'),(1, 'pCurrent'),(1, 'pHighwater'),(1, 'resetFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_status64():
    try:
        return WINFUNCTYPE(Int32,Int32,POINTER(Int64),POINTER(Int64),Int32, use_last_error=False)(("sqlite3_status64", windll["winsqlite3"]), ((1, 'op'),(1, 'pCurrent'),(1, 'pHighwater'),(1, 'resetFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_db_status():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),Int32,POINTER(Int32),POINTER(Int32),Int32, use_last_error=False)(("sqlite3_db_status", windll["winsqlite3"]), ((1, 'param0'),(1, 'op'),(1, 'pCur'),(1, 'pHiwtr'),(1, 'resetFlg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_stmt_status():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_stmt_head),Int32,Int32, use_last_error=False)(("sqlite3_stmt_status", windll["winsqlite3"]), ((1, 'param0'),(1, 'op'),(1, 'resetFlg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_backup_init():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.SqlLite.sqlite3_backup_head),POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_backup_init", windll["winsqlite3"]), ((1, 'pDest'),(1, 'zDestName'),(1, 'pSource'),(1, 'zSourceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_backup_step():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_backup_head),Int32, use_last_error=False)(("sqlite3_backup_step", windll["winsqlite3"]), ((1, 'p'),(1, 'nPage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_backup_finish():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_backup_head), use_last_error=False)(("sqlite3_backup_finish", windll["winsqlite3"]), ((1, 'p'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_backup_remaining():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_backup_head), use_last_error=False)(("sqlite3_backup_remaining", windll["winsqlite3"]), ((1, 'p'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_backup_pagecount():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_backup_head), use_last_error=False)(("sqlite3_backup_pagecount", windll["winsqlite3"]), ((1, 'p'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_stricmp():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_stricmp", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_strnicmp():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32, use_last_error=False)(("sqlite3_strnicmp", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_strglob():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_strglob", windll["winsqlite3"]), ((1, 'zGlob'),(1, 'zStr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_strlike():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("sqlite3_strlike", windll["winsqlite3"]), ((1, 'zGlob'),(1, 'zStr'),(1, 'cEsc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_log():
    try:
        return WINFUNCTYPE(Void,Int32,win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_log", windll["winsqlite3"]), ((1, 'iErrCode'),(1, 'zFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_wal_hook():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.System.SqlLite.sqlite3_head),IntPtr,c_void_p, use_last_error=False)(("sqlite3_wal_hook", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_wal_autocheckpoint():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),Int32, use_last_error=False)(("sqlite3_wal_autocheckpoint", windll["winsqlite3"]), ((1, 'db'),(1, 'N'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_wal_checkpoint():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR, use_last_error=False)(("sqlite3_wal_checkpoint", windll["winsqlite3"]), ((1, 'db'),(1, 'zDb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_wal_checkpoint_v2():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,Int32,POINTER(Int32),POINTER(Int32), use_last_error=False)(("sqlite3_wal_checkpoint_v2", windll["winsqlite3"]), ((1, 'db'),(1, 'zDb'),(1, 'eMode'),(1, 'pnLog'),(1, 'pnCkpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_vtab_config():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),Int32, use_last_error=False)(("sqlite3_vtab_config", windll["winsqlite3"]), ((1, 'param0'),(1, 'op'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_vtab_on_conflict():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_vtab_on_conflict", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_vtab_nochange():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_context_head), use_last_error=False)(("sqlite3_vtab_nochange", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_vtab_collation():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.System.SqlLite.sqlite3_index_info_head),Int32, use_last_error=False)(("sqlite3_vtab_collation", windll["winsqlite3"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_db_cacheflush():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_db_cacheflush", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_system_errno():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head), use_last_error=False)(("sqlite3_system_errno", windll["winsqlite3"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_serialize():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,POINTER(Int64),UInt32, use_last_error=False)(("sqlite3_serialize", windll["winsqlite3"]), ((1, 'db'),(1, 'zSchema'),(1, 'piSize'),(1, 'mFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_deserialize():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,c_char_p_no,Int64,Int64,UInt32, use_last_error=False)(("sqlite3_deserialize", windll["winsqlite3"]), ((1, 'db'),(1, 'zSchema'),(1, 'pData'),(1, 'szDb'),(1, 'szBuf'),(1, 'mFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_rtree_geometry_callback():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,IntPtr,c_void_p, use_last_error=False)(("sqlite3_rtree_geometry_callback", windll["winsqlite3"]), ((1, 'db'),(1, 'zGeom'),(1, 'xGeom'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_sqlite3_rtree_query_callback():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.SqlLite.sqlite3_head),win32more.Foundation.PSTR,IntPtr,c_void_p,IntPtr, use_last_error=False)(("sqlite3_rtree_query_callback", windll["winsqlite3"]), ((1, 'db'),(1, 'zQueryFunc'),(1, 'xQueryFunc'),(1, 'pContext'),(1, 'xDestructor'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "SQLITE_VERSION_NUMBER",
    "SQLITE_OK",
    "SQLITE_ERROR",
    "SQLITE_INTERNAL",
    "SQLITE_PERM",
    "SQLITE_ABORT",
    "SQLITE_BUSY",
    "SQLITE_LOCKED",
    "SQLITE_NOMEM",
    "SQLITE_READONLY",
    "SQLITE_INTERRUPT",
    "SQLITE_IOERR",
    "SQLITE_CORRUPT",
    "SQLITE_NOTFOUND",
    "SQLITE_FULL",
    "SQLITE_CANTOPEN",
    "SQLITE_PROTOCOL",
    "SQLITE_EMPTY",
    "SQLITE_SCHEMA",
    "SQLITE_TOOBIG",
    "SQLITE_CONSTRAINT",
    "SQLITE_MISMATCH",
    "SQLITE_MISUSE",
    "SQLITE_NOLFS",
    "SQLITE_AUTH",
    "SQLITE_FORMAT",
    "SQLITE_RANGE",
    "SQLITE_NOTADB",
    "SQLITE_NOTICE",
    "SQLITE_WARNING",
    "SQLITE_ROW",
    "SQLITE_DONE",
    "SQLITE_OPEN_READONLY",
    "SQLITE_OPEN_READWRITE",
    "SQLITE_OPEN_CREATE",
    "SQLITE_OPEN_DELETEONCLOSE",
    "SQLITE_OPEN_EXCLUSIVE",
    "SQLITE_OPEN_AUTOPROXY",
    "SQLITE_OPEN_URI",
    "SQLITE_OPEN_MEMORY",
    "SQLITE_OPEN_MAIN_DB",
    "SQLITE_OPEN_TEMP_DB",
    "SQLITE_OPEN_TRANSIENT_DB",
    "SQLITE_OPEN_MAIN_JOURNAL",
    "SQLITE_OPEN_TEMP_JOURNAL",
    "SQLITE_OPEN_SUBJOURNAL",
    "SQLITE_OPEN_SUPER_JOURNAL",
    "SQLITE_OPEN_NOMUTEX",
    "SQLITE_OPEN_FULLMUTEX",
    "SQLITE_OPEN_SHAREDCACHE",
    "SQLITE_OPEN_PRIVATECACHE",
    "SQLITE_OPEN_WAL",
    "SQLITE_OPEN_NOFOLLOW",
    "SQLITE_OPEN_MASTER_JOURNAL",
    "SQLITE_IOCAP_ATOMIC",
    "SQLITE_IOCAP_ATOMIC512",
    "SQLITE_IOCAP_ATOMIC1K",
    "SQLITE_IOCAP_ATOMIC2K",
    "SQLITE_IOCAP_ATOMIC4K",
    "SQLITE_IOCAP_ATOMIC8K",
    "SQLITE_IOCAP_ATOMIC16K",
    "SQLITE_IOCAP_ATOMIC32K",
    "SQLITE_IOCAP_ATOMIC64K",
    "SQLITE_IOCAP_SAFE_APPEND",
    "SQLITE_IOCAP_SEQUENTIAL",
    "SQLITE_IOCAP_UNDELETABLE_WHEN_OPEN",
    "SQLITE_IOCAP_POWERSAFE_OVERWRITE",
    "SQLITE_IOCAP_IMMUTABLE",
    "SQLITE_IOCAP_BATCH_ATOMIC",
    "SQLITE_LOCK_NONE",
    "SQLITE_LOCK_SHARED",
    "SQLITE_LOCK_RESERVED",
    "SQLITE_LOCK_PENDING",
    "SQLITE_LOCK_EXCLUSIVE",
    "SQLITE_SYNC_NORMAL",
    "SQLITE_SYNC_FULL",
    "SQLITE_SYNC_DATAONLY",
    "SQLITE_FCNTL_LOCKSTATE",
    "SQLITE_FCNTL_GET_LOCKPROXYFILE",
    "SQLITE_FCNTL_SET_LOCKPROXYFILE",
    "SQLITE_FCNTL_LAST_ERRNO",
    "SQLITE_FCNTL_SIZE_HINT",
    "SQLITE_FCNTL_CHUNK_SIZE",
    "SQLITE_FCNTL_FILE_POINTER",
    "SQLITE_FCNTL_SYNC_OMITTED",
    "SQLITE_FCNTL_WIN32_AV_RETRY",
    "SQLITE_FCNTL_PERSIST_WAL",
    "SQLITE_FCNTL_OVERWRITE",
    "SQLITE_FCNTL_VFSNAME",
    "SQLITE_FCNTL_POWERSAFE_OVERWRITE",
    "SQLITE_FCNTL_PRAGMA",
    "SQLITE_FCNTL_BUSYHANDLER",
    "SQLITE_FCNTL_TEMPFILENAME",
    "SQLITE_FCNTL_MMAP_SIZE",
    "SQLITE_FCNTL_TRACE",
    "SQLITE_FCNTL_HAS_MOVED",
    "SQLITE_FCNTL_SYNC",
    "SQLITE_FCNTL_COMMIT_PHASETWO",
    "SQLITE_FCNTL_WIN32_SET_HANDLE",
    "SQLITE_FCNTL_WAL_BLOCK",
    "SQLITE_FCNTL_ZIPVFS",
    "SQLITE_FCNTL_RBU",
    "SQLITE_FCNTL_VFS_POINTER",
    "SQLITE_FCNTL_JOURNAL_POINTER",
    "SQLITE_FCNTL_WIN32_GET_HANDLE",
    "SQLITE_FCNTL_PDB",
    "SQLITE_FCNTL_BEGIN_ATOMIC_WRITE",
    "SQLITE_FCNTL_COMMIT_ATOMIC_WRITE",
    "SQLITE_FCNTL_ROLLBACK_ATOMIC_WRITE",
    "SQLITE_FCNTL_LOCK_TIMEOUT",
    "SQLITE_FCNTL_DATA_VERSION",
    "SQLITE_FCNTL_SIZE_LIMIT",
    "SQLITE_FCNTL_CKPT_DONE",
    "SQLITE_FCNTL_RESERVE_BYTES",
    "SQLITE_FCNTL_CKPT_START",
    "SQLITE_GET_LOCKPROXYFILE",
    "SQLITE_SET_LOCKPROXYFILE",
    "SQLITE_LAST_ERRNO",
    "SQLITE_ACCESS_EXISTS",
    "SQLITE_ACCESS_READWRITE",
    "SQLITE_ACCESS_READ",
    "SQLITE_SHM_UNLOCK",
    "SQLITE_SHM_LOCK",
    "SQLITE_SHM_SHARED",
    "SQLITE_SHM_EXCLUSIVE",
    "SQLITE_SHM_NLOCK",
    "SQLITE_CONFIG_SINGLETHREAD",
    "SQLITE_CONFIG_MULTITHREAD",
    "SQLITE_CONFIG_SERIALIZED",
    "SQLITE_CONFIG_MALLOC",
    "SQLITE_CONFIG_GETMALLOC",
    "SQLITE_CONFIG_SCRATCH",
    "SQLITE_CONFIG_PAGECACHE",
    "SQLITE_CONFIG_HEAP",
    "SQLITE_CONFIG_MEMSTATUS",
    "SQLITE_CONFIG_MUTEX",
    "SQLITE_CONFIG_GETMUTEX",
    "SQLITE_CONFIG_LOOKASIDE",
    "SQLITE_CONFIG_PCACHE",
    "SQLITE_CONFIG_GETPCACHE",
    "SQLITE_CONFIG_LOG",
    "SQLITE_CONFIG_URI",
    "SQLITE_CONFIG_PCACHE2",
    "SQLITE_CONFIG_GETPCACHE2",
    "SQLITE_CONFIG_COVERING_INDEX_SCAN",
    "SQLITE_CONFIG_SQLLOG",
    "SQLITE_CONFIG_MMAP_SIZE",
    "SQLITE_CONFIG_WIN32_HEAPSIZE",
    "SQLITE_CONFIG_PCACHE_HDRSZ",
    "SQLITE_CONFIG_PMASZ",
    "SQLITE_CONFIG_STMTJRNL_SPILL",
    "SQLITE_CONFIG_SMALL_MALLOC",
    "SQLITE_CONFIG_SORTERREF_SIZE",
    "SQLITE_CONFIG_MEMDB_MAXSIZE",
    "SQLITE_DBCONFIG_MAINDBNAME",
    "SQLITE_DBCONFIG_LOOKASIDE",
    "SQLITE_DBCONFIG_ENABLE_FKEY",
    "SQLITE_DBCONFIG_ENABLE_TRIGGER",
    "SQLITE_DBCONFIG_ENABLE_FTS3_TOKENIZER",
    "SQLITE_DBCONFIG_ENABLE_LOAD_EXTENSION",
    "SQLITE_DBCONFIG_NO_CKPT_ON_CLOSE",
    "SQLITE_DBCONFIG_ENABLE_QPSG",
    "SQLITE_DBCONFIG_TRIGGER_EQP",
    "SQLITE_DBCONFIG_RESET_DATABASE",
    "SQLITE_DBCONFIG_DEFENSIVE",
    "SQLITE_DBCONFIG_WRITABLE_SCHEMA",
    "SQLITE_DBCONFIG_LEGACY_ALTER_TABLE",
    "SQLITE_DBCONFIG_DQS_DML",
    "SQLITE_DBCONFIG_DQS_DDL",
    "SQLITE_DBCONFIG_ENABLE_VIEW",
    "SQLITE_DBCONFIG_LEGACY_FILE_FORMAT",
    "SQLITE_DBCONFIG_TRUSTED_SCHEMA",
    "SQLITE_DBCONFIG_MAX",
    "SQLITE_DENY",
    "SQLITE_IGNORE",
    "SQLITE_CREATE_INDEX",
    "SQLITE_CREATE_TABLE",
    "SQLITE_CREATE_TEMP_INDEX",
    "SQLITE_CREATE_TEMP_TABLE",
    "SQLITE_CREATE_TEMP_TRIGGER",
    "SQLITE_CREATE_TEMP_VIEW",
    "SQLITE_CREATE_TRIGGER",
    "SQLITE_CREATE_VIEW",
    "SQLITE_DELETE",
    "SQLITE_DROP_INDEX",
    "SQLITE_DROP_TABLE",
    "SQLITE_DROP_TEMP_INDEX",
    "SQLITE_DROP_TEMP_TABLE",
    "SQLITE_DROP_TEMP_TRIGGER",
    "SQLITE_DROP_TEMP_VIEW",
    "SQLITE_DROP_TRIGGER",
    "SQLITE_DROP_VIEW",
    "SQLITE_INSERT",
    "SQLITE_PRAGMA",
    "SQLITE_READ",
    "SQLITE_SELECT",
    "SQLITE_TRANSACTION",
    "SQLITE_UPDATE",
    "SQLITE_ATTACH",
    "SQLITE_DETACH",
    "SQLITE_ALTER_TABLE",
    "SQLITE_REINDEX",
    "SQLITE_ANALYZE",
    "SQLITE_CREATE_VTABLE",
    "SQLITE_DROP_VTABLE",
    "SQLITE_FUNCTION",
    "SQLITE_SAVEPOINT",
    "SQLITE_COPY",
    "SQLITE_RECURSIVE",
    "SQLITE_TRACE_STMT",
    "SQLITE_TRACE_PROFILE",
    "SQLITE_TRACE_ROW",
    "SQLITE_TRACE_CLOSE",
    "SQLITE_LIMIT_LENGTH",
    "SQLITE_LIMIT_SQL_LENGTH",
    "SQLITE_LIMIT_COLUMN",
    "SQLITE_LIMIT_EXPR_DEPTH",
    "SQLITE_LIMIT_COMPOUND_SELECT",
    "SQLITE_LIMIT_VDBE_OP",
    "SQLITE_LIMIT_FUNCTION_ARG",
    "SQLITE_LIMIT_ATTACHED",
    "SQLITE_LIMIT_LIKE_PATTERN_LENGTH",
    "SQLITE_LIMIT_VARIABLE_NUMBER",
    "SQLITE_LIMIT_TRIGGER_DEPTH",
    "SQLITE_LIMIT_WORKER_THREADS",
    "SQLITE_PREPARE_PERSISTENT",
    "SQLITE_PREPARE_NORMALIZE",
    "SQLITE_PREPARE_NO_VTAB",
    "SQLITE_INTEGER",
    "SQLITE_FLOAT",
    "SQLITE_BLOB",
    "SQLITE_NULL",
    "SQLITE3_TEXT",
    "SQLITE_UTF8",
    "SQLITE_UTF16LE",
    "SQLITE_UTF16BE",
    "SQLITE_UTF16",
    "SQLITE_ANY",
    "SQLITE_UTF16_ALIGNED",
    "SQLITE_DETERMINISTIC",
    "SQLITE_DIRECTONLY",
    "SQLITE_SUBTYPE",
    "SQLITE_INNOCUOUS",
    "SQLITE_WIN32_DATA_DIRECTORY_TYPE",
    "SQLITE_WIN32_TEMP_DIRECTORY_TYPE",
    "SQLITE_TXN_NONE",
    "SQLITE_TXN_READ",
    "SQLITE_TXN_WRITE",
    "SQLITE_INDEX_SCAN_UNIQUE",
    "SQLITE_INDEX_CONSTRAINT_EQ",
    "SQLITE_INDEX_CONSTRAINT_GT",
    "SQLITE_INDEX_CONSTRAINT_LE",
    "SQLITE_INDEX_CONSTRAINT_LT",
    "SQLITE_INDEX_CONSTRAINT_GE",
    "SQLITE_INDEX_CONSTRAINT_MATCH",
    "SQLITE_INDEX_CONSTRAINT_LIKE",
    "SQLITE_INDEX_CONSTRAINT_GLOB",
    "SQLITE_INDEX_CONSTRAINT_REGEXP",
    "SQLITE_INDEX_CONSTRAINT_NE",
    "SQLITE_INDEX_CONSTRAINT_ISNOT",
    "SQLITE_INDEX_CONSTRAINT_ISNOTNULL",
    "SQLITE_INDEX_CONSTRAINT_ISNULL",
    "SQLITE_INDEX_CONSTRAINT_IS",
    "SQLITE_INDEX_CONSTRAINT_FUNCTION",
    "SQLITE_MUTEX_FAST",
    "SQLITE_MUTEX_RECURSIVE",
    "SQLITE_MUTEX_STATIC_MAIN",
    "SQLITE_MUTEX_STATIC_MEM",
    "SQLITE_MUTEX_STATIC_MEM2",
    "SQLITE_MUTEX_STATIC_OPEN",
    "SQLITE_MUTEX_STATIC_PRNG",
    "SQLITE_MUTEX_STATIC_LRU",
    "SQLITE_MUTEX_STATIC_LRU2",
    "SQLITE_MUTEX_STATIC_PMEM",
    "SQLITE_MUTEX_STATIC_APP1",
    "SQLITE_MUTEX_STATIC_APP2",
    "SQLITE_MUTEX_STATIC_APP3",
    "SQLITE_MUTEX_STATIC_VFS1",
    "SQLITE_MUTEX_STATIC_VFS2",
    "SQLITE_MUTEX_STATIC_VFS3",
    "SQLITE_MUTEX_STATIC_MASTER",
    "SQLITE_TESTCTRL_FIRST",
    "SQLITE_TESTCTRL_PRNG_SAVE",
    "SQLITE_TESTCTRL_PRNG_RESTORE",
    "SQLITE_TESTCTRL_PRNG_RESET",
    "SQLITE_TESTCTRL_BITVEC_TEST",
    "SQLITE_TESTCTRL_FAULT_INSTALL",
    "SQLITE_TESTCTRL_BENIGN_MALLOC_HOOKS",
    "SQLITE_TESTCTRL_PENDING_BYTE",
    "SQLITE_TESTCTRL_ASSERT",
    "SQLITE_TESTCTRL_ALWAYS",
    "SQLITE_TESTCTRL_RESERVE",
    "SQLITE_TESTCTRL_OPTIMIZATIONS",
    "SQLITE_TESTCTRL_ISKEYWORD",
    "SQLITE_TESTCTRL_SCRATCHMALLOC",
    "SQLITE_TESTCTRL_INTERNAL_FUNCTIONS",
    "SQLITE_TESTCTRL_LOCALTIME_FAULT",
    "SQLITE_TESTCTRL_EXPLAIN_STMT",
    "SQLITE_TESTCTRL_ONCE_RESET_THRESHOLD",
    "SQLITE_TESTCTRL_NEVER_CORRUPT",
    "SQLITE_TESTCTRL_VDBE_COVERAGE",
    "SQLITE_TESTCTRL_BYTEORDER",
    "SQLITE_TESTCTRL_ISINIT",
    "SQLITE_TESTCTRL_SORTER_MMAP",
    "SQLITE_TESTCTRL_IMPOSTER",
    "SQLITE_TESTCTRL_PARSER_COVERAGE",
    "SQLITE_TESTCTRL_RESULT_INTREAL",
    "SQLITE_TESTCTRL_PRNG_SEED",
    "SQLITE_TESTCTRL_EXTRA_SCHEMA_CHECKS",
    "SQLITE_TESTCTRL_SEEK_COUNT",
    "SQLITE_TESTCTRL_LAST",
    "SQLITE_STATUS_MEMORY_USED",
    "SQLITE_STATUS_PAGECACHE_USED",
    "SQLITE_STATUS_PAGECACHE_OVERFLOW",
    "SQLITE_STATUS_SCRATCH_USED",
    "SQLITE_STATUS_SCRATCH_OVERFLOW",
    "SQLITE_STATUS_MALLOC_SIZE",
    "SQLITE_STATUS_PARSER_STACK",
    "SQLITE_STATUS_PAGECACHE_SIZE",
    "SQLITE_STATUS_SCRATCH_SIZE",
    "SQLITE_STATUS_MALLOC_COUNT",
    "SQLITE_DBSTATUS_LOOKASIDE_USED",
    "SQLITE_DBSTATUS_CACHE_USED",
    "SQLITE_DBSTATUS_SCHEMA_USED",
    "SQLITE_DBSTATUS_STMT_USED",
    "SQLITE_DBSTATUS_LOOKASIDE_HIT",
    "SQLITE_DBSTATUS_LOOKASIDE_MISS_SIZE",
    "SQLITE_DBSTATUS_LOOKASIDE_MISS_FULL",
    "SQLITE_DBSTATUS_CACHE_HIT",
    "SQLITE_DBSTATUS_CACHE_MISS",
    "SQLITE_DBSTATUS_CACHE_WRITE",
    "SQLITE_DBSTATUS_DEFERRED_FKS",
    "SQLITE_DBSTATUS_CACHE_USED_SHARED",
    "SQLITE_DBSTATUS_CACHE_SPILL",
    "SQLITE_DBSTATUS_MAX",
    "SQLITE_STMTSTATUS_FULLSCAN_STEP",
    "SQLITE_STMTSTATUS_SORT",
    "SQLITE_STMTSTATUS_AUTOINDEX",
    "SQLITE_STMTSTATUS_VM_STEP",
    "SQLITE_STMTSTATUS_REPREPARE",
    "SQLITE_STMTSTATUS_RUN",
    "SQLITE_STMTSTATUS_MEMUSED",
    "SQLITE_CHECKPOINT_PASSIVE",
    "SQLITE_CHECKPOINT_FULL",
    "SQLITE_CHECKPOINT_RESTART",
    "SQLITE_CHECKPOINT_TRUNCATE",
    "SQLITE_VTAB_CONSTRAINT_SUPPORT",
    "SQLITE_VTAB_INNOCUOUS",
    "SQLITE_VTAB_DIRECTONLY",
    "SQLITE_ROLLBACK",
    "SQLITE_FAIL",
    "SQLITE_REPLACE",
    "SQLITE_SCANSTAT_NLOOP",
    "SQLITE_SCANSTAT_NVISIT",
    "SQLITE_SCANSTAT_EST",
    "SQLITE_SCANSTAT_NAME",
    "SQLITE_SCANSTAT_EXPLAIN",
    "SQLITE_SCANSTAT_SELECTID",
    "SQLITE_SERIALIZE_NOCOPY",
    "SQLITE_DESERIALIZE_FREEONCLOSE",
    "SQLITE_DESERIALIZE_RESIZEABLE",
    "SQLITE_DESERIALIZE_READONLY",
    "NOT_WITHIN",
    "PARTLY_WITHIN",
    "FULLY_WITHIN",
    "__SQLITESESSION_H_",
    "SQLITE_CHANGESETSTART_INVERT",
    "SQLITE_CHANGESETAPPLY_NOSAVEPOINT",
    "SQLITE_CHANGESETAPPLY_INVERT",
    "SQLITE_CHANGESET_DATA",
    "SQLITE_CHANGESET_NOTFOUND",
    "SQLITE_CHANGESET_CONFLICT",
    "SQLITE_CHANGESET_CONSTRAINT",
    "SQLITE_CHANGESET_FOREIGN_KEY",
    "SQLITE_CHANGESET_OMIT",
    "SQLITE_CHANGESET_REPLACE",
    "SQLITE_CHANGESET_ABORT",
    "SQLITE_SESSION_CONFIG_STRMSIZE",
    "FTS5_TOKENIZE_QUERY",
    "FTS5_TOKENIZE_PREFIX",
    "FTS5_TOKENIZE_DOCUMENT",
    "FTS5_TOKENIZE_AUX",
    "FTS5_TOKEN_COLOCATED",
    "sqlite3",
    "sqlite3_mutex",
    "sqlite3_stmt",
    "sqlite3_value",
    "sqlite3_context",
    "sqlite3_blob",
    "sqlite3_str",
    "sqlite3_pcache",
    "sqlite3_backup",
    "Fts5Context",
    "Fts5Tokenizer",
    "sqlite3_callback",
    "sqlite3_file",
    "sqlite3_io_methods",
    "sqlite3_syscall_ptr",
    "sqlite3_vfs",
    "sqlite3_mem_methods",
    "sqlite3_destructor_type",
    "sqlite3_module",
    "sqlite3_index_info",
    "sqlite3_vtab",
    "sqlite3_vtab_cursor",
    "sqlite3_mutex_methods",
    "sqlite3_pcache_page",
    "sqlite3_pcache_methods2",
    "sqlite3_pcache_methods",
    "sqlite3_snapshot",
    "sqlite3_rtree_geometry",
    "sqlite3_rtree_query_info",
    "fts5_extension_function",
    "Fts5PhraseIter",
    "Fts5ExtensionApi",
    "fts5_tokenizer",
    "fts5_api",
    "sqlite3_api_routines",
    "sqlite3_loadext_entry",
    "sqlite3_libversion",
    "sqlite3_sourceid",
    "sqlite3_libversion_number",
    "sqlite3_compileoption_used",
    "sqlite3_compileoption_get",
    "sqlite3_threadsafe",
    "sqlite3_close",
    "sqlite3_close_v2",
    "sqlite3_exec",
    "sqlite3_initialize",
    "sqlite3_shutdown",
    "sqlite3_os_init",
    "sqlite3_os_end",
    "sqlite3_config",
    "sqlite3_db_config",
    "sqlite3_extended_result_codes",
    "sqlite3_last_insert_rowid",
    "sqlite3_set_last_insert_rowid",
    "sqlite3_changes",
    "sqlite3_total_changes",
    "sqlite3_interrupt",
    "sqlite3_complete",
    "sqlite3_complete16",
    "sqlite3_busy_handler",
    "sqlite3_busy_timeout",
    "sqlite3_get_table",
    "sqlite3_free_table",
    "sqlite3_mprintf",
    "sqlite3_vmprintf",
    "sqlite3_snprintf",
    "sqlite3_vsnprintf",
    "sqlite3_malloc",
    "sqlite3_malloc64",
    "sqlite3_realloc",
    "sqlite3_realloc64",
    "sqlite3_free",
    "sqlite3_msize",
    "sqlite3_memory_used",
    "sqlite3_memory_highwater",
    "sqlite3_randomness",
    "sqlite3_set_authorizer",
    "sqlite3_trace",
    "sqlite3_profile",
    "sqlite3_trace_v2",
    "sqlite3_progress_handler",
    "sqlite3_open",
    "sqlite3_open16",
    "sqlite3_open_v2",
    "sqlite3_uri_parameter",
    "sqlite3_uri_boolean",
    "sqlite3_uri_int64",
    "sqlite3_uri_key",
    "sqlite3_filename_database",
    "sqlite3_filename_journal",
    "sqlite3_filename_wal",
    "sqlite3_database_file_object",
    "sqlite3_create_filename",
    "sqlite3_free_filename",
    "sqlite3_errcode",
    "sqlite3_extended_errcode",
    "sqlite3_errmsg",
    "sqlite3_errmsg16",
    "sqlite3_errstr",
    "sqlite3_limit",
    "sqlite3_prepare",
    "sqlite3_prepare_v2",
    "sqlite3_prepare_v3",
    "sqlite3_prepare16",
    "sqlite3_prepare16_v2",
    "sqlite3_prepare16_v3",
    "sqlite3_sql",
    "sqlite3_expanded_sql",
    "sqlite3_stmt_readonly",
    "sqlite3_stmt_isexplain",
    "sqlite3_stmt_busy",
    "sqlite3_bind_blob",
    "sqlite3_bind_blob64",
    "sqlite3_bind_double",
    "sqlite3_bind_int",
    "sqlite3_bind_int64",
    "sqlite3_bind_null",
    "sqlite3_bind_text",
    "sqlite3_bind_text16",
    "sqlite3_bind_text64",
    "sqlite3_bind_value",
    "sqlite3_bind_pointer",
    "sqlite3_bind_zeroblob",
    "sqlite3_bind_zeroblob64",
    "sqlite3_bind_parameter_count",
    "sqlite3_bind_parameter_name",
    "sqlite3_bind_parameter_index",
    "sqlite3_clear_bindings",
    "sqlite3_column_count",
    "sqlite3_column_name",
    "sqlite3_column_name16",
    "sqlite3_column_database_name",
    "sqlite3_column_database_name16",
    "sqlite3_column_table_name",
    "sqlite3_column_table_name16",
    "sqlite3_column_origin_name",
    "sqlite3_column_origin_name16",
    "sqlite3_column_decltype",
    "sqlite3_column_decltype16",
    "sqlite3_step",
    "sqlite3_data_count",
    "sqlite3_column_blob",
    "sqlite3_column_double",
    "sqlite3_column_int",
    "sqlite3_column_int64",
    "sqlite3_column_text",
    "sqlite3_column_text16",
    "sqlite3_column_value",
    "sqlite3_column_bytes",
    "sqlite3_column_bytes16",
    "sqlite3_column_type",
    "sqlite3_finalize",
    "sqlite3_reset",
    "sqlite3_create_function",
    "sqlite3_create_function16",
    "sqlite3_create_function_v2",
    "sqlite3_create_window_function",
    "sqlite3_aggregate_count",
    "sqlite3_expired",
    "sqlite3_transfer_bindings",
    "sqlite3_global_recover",
    "sqlite3_thread_cleanup",
    "sqlite3_memory_alarm",
    "sqlite3_value_blob",
    "sqlite3_value_double",
    "sqlite3_value_int",
    "sqlite3_value_int64",
    "sqlite3_value_pointer",
    "sqlite3_value_text",
    "sqlite3_value_text16",
    "sqlite3_value_text16le",
    "sqlite3_value_text16be",
    "sqlite3_value_bytes",
    "sqlite3_value_bytes16",
    "sqlite3_value_type",
    "sqlite3_value_numeric_type",
    "sqlite3_value_nochange",
    "sqlite3_value_frombind",
    "sqlite3_value_subtype",
    "sqlite3_value_dup",
    "sqlite3_value_free",
    "sqlite3_aggregate_context",
    "sqlite3_user_data",
    "sqlite3_context_db_handle",
    "sqlite3_get_auxdata",
    "sqlite3_set_auxdata",
    "sqlite3_result_blob",
    "sqlite3_result_blob64",
    "sqlite3_result_double",
    "sqlite3_result_error",
    "sqlite3_result_error16",
    "sqlite3_result_error_toobig",
    "sqlite3_result_error_nomem",
    "sqlite3_result_error_code",
    "sqlite3_result_int",
    "sqlite3_result_int64",
    "sqlite3_result_null",
    "sqlite3_result_text",
    "sqlite3_result_text64",
    "sqlite3_result_text16",
    "sqlite3_result_text16le",
    "sqlite3_result_text16be",
    "sqlite3_result_value",
    "sqlite3_result_pointer",
    "sqlite3_result_zeroblob",
    "sqlite3_result_zeroblob64",
    "sqlite3_result_subtype",
    "sqlite3_create_collation",
    "sqlite3_create_collation_v2",
    "sqlite3_create_collation16",
    "sqlite3_collation_needed",
    "sqlite3_collation_needed16",
    "sqlite3_sleep",
    "sqlite3_win32_set_directory",
    "sqlite3_win32_set_directory8",
    "sqlite3_win32_set_directory16",
    "sqlite3_get_autocommit",
    "sqlite3_db_handle",
    "sqlite3_db_filename",
    "sqlite3_db_readonly",
    "sqlite3_txn_state",
    "sqlite3_next_stmt",
    "sqlite3_commit_hook",
    "sqlite3_rollback_hook",
    "sqlite3_update_hook",
    "sqlite3_enable_shared_cache",
    "sqlite3_release_memory",
    "sqlite3_db_release_memory",
    "sqlite3_soft_heap_limit64",
    "sqlite3_hard_heap_limit64",
    "sqlite3_soft_heap_limit",
    "sqlite3_table_column_metadata",
    "sqlite3_load_extension",
    "sqlite3_enable_load_extension",
    "sqlite3_auto_extension",
    "sqlite3_cancel_auto_extension",
    "sqlite3_reset_auto_extension",
    "sqlite3_create_module",
    "sqlite3_create_module_v2",
    "sqlite3_drop_modules",
    "sqlite3_declare_vtab",
    "sqlite3_overload_function",
    "sqlite3_blob_open",
    "sqlite3_blob_reopen",
    "sqlite3_blob_close",
    "sqlite3_blob_bytes",
    "sqlite3_blob_read",
    "sqlite3_blob_write",
    "sqlite3_vfs_find",
    "sqlite3_vfs_register",
    "sqlite3_vfs_unregister",
    "sqlite3_mutex_alloc",
    "sqlite3_mutex_free",
    "sqlite3_mutex_enter",
    "sqlite3_mutex_try",
    "sqlite3_mutex_leave",
    "sqlite3_db_mutex",
    "sqlite3_file_control",
    "sqlite3_test_control",
    "sqlite3_keyword_count",
    "sqlite3_keyword_name",
    "sqlite3_keyword_check",
    "sqlite3_str_new",
    "sqlite3_str_finish",
    "sqlite3_str_appendf",
    "sqlite3_str_vappendf",
    "sqlite3_str_append",
    "sqlite3_str_appendall",
    "sqlite3_str_appendchar",
    "sqlite3_str_reset",
    "sqlite3_str_errcode",
    "sqlite3_str_length",
    "sqlite3_str_value",
    "sqlite3_status",
    "sqlite3_status64",
    "sqlite3_db_status",
    "sqlite3_stmt_status",
    "sqlite3_backup_init",
    "sqlite3_backup_step",
    "sqlite3_backup_finish",
    "sqlite3_backup_remaining",
    "sqlite3_backup_pagecount",
    "sqlite3_stricmp",
    "sqlite3_strnicmp",
    "sqlite3_strglob",
    "sqlite3_strlike",
    "sqlite3_log",
    "sqlite3_wal_hook",
    "sqlite3_wal_autocheckpoint",
    "sqlite3_wal_checkpoint",
    "sqlite3_wal_checkpoint_v2",
    "sqlite3_vtab_config",
    "sqlite3_vtab_on_conflict",
    "sqlite3_vtab_nochange",
    "sqlite3_vtab_collation",
    "sqlite3_db_cacheflush",
    "sqlite3_system_errno",
    "sqlite3_serialize",
    "sqlite3_deserialize",
    "sqlite3_rtree_geometry_callback",
    "sqlite3_rtree_query_callback",
]
