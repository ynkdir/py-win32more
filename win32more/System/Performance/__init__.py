from win32more.base import *
import win32more.Foundation
import win32more.System.Com
import win32more.System.Ole
import win32more.System.Performance

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
MAX_COUNTER_PATH = 256
PDH_MAX_COUNTER_NAME = 1024
PDH_MAX_INSTANCE_NAME = 1024
PDH_MAX_COUNTER_PATH = 2048
PDH_MAX_DATASOURCE_PATH = 1024
H_WBEM_DATASOURCE = -1
PDH_MAX_SCALE = 7
PDH_MIN_SCALE = -7
PDH_NOEXPANDCOUNTERS = 1
PDH_NOEXPANDINSTANCES = 2
PDH_REFRESHCOUNTERS = 4
PDH_LOG_TYPE_RETIRED_BIN = 3
PDH_LOG_TYPE_TRACE_KERNEL = 4
PDH_LOG_TYPE_TRACE_GENERIC = 5
PERF_PROVIDER_USER_MODE = 0
PERF_PROVIDER_KERNEL_MODE = 1
PERF_PROVIDER_DRIVER = 2
PERF_COUNTERSET_FLAG_MULTIPLE = 2
PERF_COUNTERSET_FLAG_AGGREGATE = 4
PERF_COUNTERSET_FLAG_HISTORY = 8
PERF_COUNTERSET_FLAG_INSTANCE = 16
PERF_COUNTERSET_SINGLE_INSTANCE = 0
PERF_COUNTERSET_MULTI_INSTANCES = 2
PERF_COUNTERSET_SINGLE_AGGREGATE = 4
PERF_AGGREGATE_MAX = 4
PERF_ATTRIB_BY_REFERENCE = 1
PERF_ATTRIB_NO_DISPLAYABLE = 2
PERF_ATTRIB_NO_GROUP_SEPARATOR = 4
PERF_ATTRIB_DISPLAY_AS_REAL = 8
PERF_ATTRIB_DISPLAY_AS_HEX = 16
PERF_WILDCARD_COUNTER = 4294967295
PERF_MAX_INSTANCE_NAME = 1024
PERF_ADD_COUNTER = 1
PERF_REMOVE_COUNTER = 2
PERF_ENUM_INSTANCES = 3
PERF_COLLECT_START = 5
PERF_COLLECT_END = 6
PERF_FILTER = 9
PERF_DATA_VERSION = 1
PERF_DATA_REVISION = 1
PERF_NO_INSTANCES = -1
PERF_METADATA_MULTIPLE_INSTANCES = -2
PERF_METADATA_NO_INSTANCES = -3
PERF_SIZE_DWORD = 0
PERF_SIZE_LARGE = 256
PERF_SIZE_ZERO = 512
PERF_SIZE_VARIABLE_LEN = 768
PERF_TYPE_NUMBER = 0
PERF_TYPE_COUNTER = 1024
PERF_TYPE_TEXT = 2048
PERF_TYPE_ZERO = 3072
PERF_NUMBER_HEX = 0
PERF_NUMBER_DECIMAL = 65536
PERF_NUMBER_DEC_1000 = 131072
PERF_COUNTER_VALUE = 0
PERF_COUNTER_RATE = 65536
PERF_COUNTER_FRACTION = 131072
PERF_COUNTER_BASE = 196608
PERF_COUNTER_ELAPSED = 262144
PERF_COUNTER_QUEUELEN = 327680
PERF_COUNTER_HISTOGRAM = 393216
PERF_COUNTER_PRECISION = 458752
PERF_TEXT_UNICODE = 0
PERF_TEXT_ASCII = 65536
PERF_TIMER_TICK = 0
PERF_TIMER_100NS = 1048576
PERF_OBJECT_TIMER = 2097152
PERF_DELTA_COUNTER = 4194304
PERF_DELTA_BASE = 8388608
PERF_INVERSE_COUNTER = 16777216
PERF_MULTI_COUNTER = 33554432
PERF_DISPLAY_NO_SUFFIX = 0
PERF_DISPLAY_PER_SEC = 268435456
PERF_DISPLAY_PERCENT = 536870912
PERF_DISPLAY_SECONDS = 805306368
PERF_DISPLAY_NOSHOW = 1073741824
PERF_COUNTER_HISTOGRAM_TYPE = 2147483648
PERF_NO_UNIQUE_ID = -1
MAX_PERF_OBJECTS_IN_QUERY_FUNCTION = 64
WINPERF_LOG_NONE = 0
WINPERF_LOG_USER = 1
WINPERF_LOG_DEBUG = 2
WINPERF_LOG_VERBOSE = 3
LIBID_SystemMonitor = '1b773e42-2509-11cf-942f-008029004347'
DIID_DICounterItem = 'c08c4ff2-0e2e-11cf-942c-008029004347'
DIID_DILogFileItem = '8d093ffc-f777-4917-82d1-833fbc54c58f'
DIID_DISystemMonitor = '13d73d81-c32e-11cf-9398-00aa00a3ddea'
DIID_DISystemMonitorInternal = '194eb242-c32c-11cf-9398-00aa00a3ddea'
DIID_DISystemMonitorEvents = '84979930-4ab3-11cf-943a-008029004347'
PDH_CSTATUS_VALID_DATA = 0
PDH_CSTATUS_NEW_DATA = 1
PDH_CSTATUS_NO_MACHINE = -2147481648
PDH_CSTATUS_NO_INSTANCE = -2147481647
PDH_MORE_DATA = -2147481646
PDH_CSTATUS_ITEM_NOT_VALIDATED = -2147481645
PDH_RETRY = -2147481644
PDH_NO_DATA = -2147481643
PDH_CALC_NEGATIVE_DENOMINATOR = -2147481642
PDH_CALC_NEGATIVE_TIMEBASE = -2147481641
PDH_CALC_NEGATIVE_VALUE = -2147481640
PDH_DIALOG_CANCELLED = -2147481639
PDH_END_OF_LOG_FILE = -2147481638
PDH_ASYNC_QUERY_TIMEOUT = -2147481637
PDH_CANNOT_SET_DEFAULT_REALTIME_DATASOURCE = -2147481636
PDH_UNABLE_MAP_NAME_FILES = -2147480619
PDH_PLA_VALIDATION_WARNING = -2147480589
PDH_CSTATUS_NO_OBJECT = -1073738824
PDH_CSTATUS_NO_COUNTER = -1073738823
PDH_CSTATUS_INVALID_DATA = -1073738822
PDH_MEMORY_ALLOCATION_FAILURE = -1073738821
PDH_INVALID_HANDLE = -1073738820
PDH_INVALID_ARGUMENT = -1073738819
PDH_FUNCTION_NOT_FOUND = -1073738818
PDH_CSTATUS_NO_COUNTERNAME = -1073738817
PDH_CSTATUS_BAD_COUNTERNAME = -1073738816
PDH_INVALID_BUFFER = -1073738815
PDH_INSUFFICIENT_BUFFER = -1073738814
PDH_CANNOT_CONNECT_MACHINE = -1073738813
PDH_INVALID_PATH = -1073738812
PDH_INVALID_INSTANCE = -1073738811
PDH_INVALID_DATA = -1073738810
PDH_NO_DIALOG_DATA = -1073738809
PDH_CANNOT_READ_NAME_STRINGS = -1073738808
PDH_LOG_FILE_CREATE_ERROR = -1073738807
PDH_LOG_FILE_OPEN_ERROR = -1073738806
PDH_LOG_TYPE_NOT_FOUND = -1073738805
PDH_NO_MORE_DATA = -1073738804
PDH_ENTRY_NOT_IN_LOG_FILE = -1073738803
PDH_DATA_SOURCE_IS_LOG_FILE = -1073738802
PDH_DATA_SOURCE_IS_REAL_TIME = -1073738801
PDH_UNABLE_READ_LOG_HEADER = -1073738800
PDH_FILE_NOT_FOUND = -1073738799
PDH_FILE_ALREADY_EXISTS = -1073738798
PDH_NOT_IMPLEMENTED = -1073738797
PDH_STRING_NOT_FOUND = -1073738796
PDH_UNKNOWN_LOG_FORMAT = -1073738794
PDH_UNKNOWN_LOGSVC_COMMAND = -1073738793
PDH_LOGSVC_QUERY_NOT_FOUND = -1073738792
PDH_LOGSVC_NOT_OPENED = -1073738791
PDH_WBEM_ERROR = -1073738790
PDH_ACCESS_DENIED = -1073738789
PDH_LOG_FILE_TOO_SMALL = -1073738788
PDH_INVALID_DATASOURCE = -1073738787
PDH_INVALID_SQLDB = -1073738786
PDH_NO_COUNTERS = -1073738785
PDH_SQL_ALLOC_FAILED = -1073738784
PDH_SQL_ALLOCCON_FAILED = -1073738783
PDH_SQL_EXEC_DIRECT_FAILED = -1073738782
PDH_SQL_FETCH_FAILED = -1073738781
PDH_SQL_ROWCOUNT_FAILED = -1073738780
PDH_SQL_MORE_RESULTS_FAILED = -1073738779
PDH_SQL_CONNECT_FAILED = -1073738778
PDH_SQL_BIND_FAILED = -1073738777
PDH_CANNOT_CONNECT_WMI_SERVER = -1073738776
PDH_PLA_COLLECTION_ALREADY_RUNNING = -1073738775
PDH_PLA_ERROR_SCHEDULE_OVERLAP = -1073738774
PDH_PLA_COLLECTION_NOT_FOUND = -1073738773
PDH_PLA_ERROR_SCHEDULE_ELAPSED = -1073738772
PDH_PLA_ERROR_NOSTART = -1073738771
PDH_PLA_ERROR_ALREADY_EXISTS = -1073738770
PDH_PLA_ERROR_TYPE_MISMATCH = -1073738769
PDH_PLA_ERROR_FILEPATH = -1073738768
PDH_PLA_SERVICE_ERROR = -1073738767
PDH_PLA_VALIDATION_ERROR = -1073738766
PDH_PLA_ERROR_NAME_TOO_LONG = -1073738764
PDH_INVALID_SQL_LOG_FORMAT = -1073738763
PDH_COUNTER_ALREADY_IN_QUERY = -1073738762
PDH_BINARY_LOG_CORRUPT = -1073738761
PDH_LOG_SAMPLE_TOO_SMALL = -1073738760
PDH_OS_LATER_VERSION = -1073738759
PDH_OS_EARLIER_VERSION = -1073738758
PDH_INCORRECT_APPEND_TIME = -1073738757
PDH_UNMATCHED_APPEND_COUNTER = -1073738756
PDH_SQL_ALTER_DETAIL_FAILED = -1073738755
PDH_QUERY_PERF_DATA_TIMEOUT = -1073738754
PLA_CAPABILITY_LOCAL = 268435456
PLA_CAPABILITY_V1_SVC = 1
PLA_CAPABILITY_V1_SESSION = 2
PLA_CAPABILITY_V1_SYSTEM = 4
PLA_CAPABILITY_LEGACY_SESSION = 8
PLA_CAPABILITY_LEGACY_SVC = 16
PLA_CAPABILITY_AUTOLOGGER = 32
S_PDH = '04d66358-c4a1-419b-8023-23b73902de2c'
PERF_DETAIL = UInt32
PERF_DETAIL_NOVICE = 100
PERF_DETAIL_ADVANCED = 200
PERF_DETAIL_EXPERT = 300
PERF_DETAIL_WIZARD = 400
REAL_TIME_DATA_SOURCE_ID_FLAGS = UInt32
DATA_SOURCE_REGISTRY = 1
DATA_SOURCE_WBEM = 4
PDH_PATH_FLAGS = UInt32
PDH_PATH_WBEM_RESULT = 1
PDH_PATH_WBEM_INPUT = 2
PDH_PATH_WBEM_NONE = 0
PDH_FMT = UInt32
PDH_FMT_DOUBLE = 512
PDH_FMT_LARGE = 1024
PDH_FMT_LONG = 256
PDH_LOG_TYPE = UInt32
PDH_LOG_TYPE_UNDEFINED = 0
PDH_LOG_TYPE_CSV = 1
PDH_LOG_TYPE_SQL = 7
PDH_LOG_TYPE_TSV = 2
PDH_LOG_TYPE_BINARY = 8
PDH_LOG_TYPE_PERFMON = 6
PDH_LOG = UInt32
PDH_LOG_READ_ACCESS = 65536
PDH_LOG_WRITE_ACCESS = 131072
PDH_LOG_UPDATE_ACCESS = 262144
PDH_SELECT_DATA_SOURCE_FLAGS = UInt32
PDH_FLAGS_FILE_BROWSER_ONLY = 1
PDH_FLAGS_NONE = 0
PDH_DLL_VERSION = UInt32
PDH_CVERSION_WIN50 = 1280
PDH_VERSION = 1283
PERF_COUNTER_AGGREGATE_FUNC = UInt32
PERF_AGGREGATE_UNDEFINED = 0
PERF_AGGREGATE_TOTAL = 1
PERF_AGGREGATE_AVG = 2
PERF_AGGREGATE_MIN = 3
PerfProviderHandle = IntPtr
PerfQueryHandle = IntPtr
DataCollectorSet = Guid('03837521-098b-11d8-9414-505054503030')
TraceSession = Guid('0383751c-098b-11d8-9414-505054503030')
TraceSessionCollection = Guid('03837530-098b-11d8-9414-505054503030')
TraceDataProvider = Guid('03837513-098b-11d8-9414-505054503030')
TraceDataProviderCollection = Guid('03837511-098b-11d8-9414-505054503030')
DataCollectorSetCollection = Guid('03837525-098b-11d8-9414-505054503030')
LegacyDataCollectorSet = Guid('03837526-098b-11d8-9414-505054503030')
LegacyDataCollectorSetCollection = Guid('03837527-098b-11d8-9414-505054503030')
LegacyTraceSession = Guid('03837528-098b-11d8-9414-505054503030')
LegacyTraceSessionCollection = Guid('03837529-098b-11d8-9414-505054503030')
ServerDataCollectorSet = Guid('03837531-098b-11d8-9414-505054503030')
ServerDataCollectorSetCollection = Guid('03837532-098b-11d8-9414-505054503030')
SystemDataCollectorSet = Guid('03837546-098b-11d8-9414-505054503030')
SystemDataCollectorSetCollection = Guid('03837547-098b-11d8-9414-505054503030')
BootTraceSession = Guid('03837538-098b-11d8-9414-505054503030')
BootTraceSessionCollection = Guid('03837539-098b-11d8-9414-505054503030')
DataCollectorType = Int32
DataCollectorType_plaPerformanceCounter = 0
DataCollectorType_plaTrace = 1
DataCollectorType_plaConfiguration = 2
DataCollectorType_plaAlert = 3
DataCollectorType_plaApiTrace = 4
FileFormat = Int32
FileFormat_plaCommaSeparated = 0
FileFormat_plaTabSeparated = 1
FileFormat_plaSql = 2
FileFormat_plaBinary = 3
AutoPathFormat = Int32
AutoPathFormat_plaNone = 0
AutoPathFormat_plaPattern = 1
AutoPathFormat_plaComputer = 2
AutoPathFormat_plaMonthDayHour = 256
AutoPathFormat_plaSerialNumber = 512
AutoPathFormat_plaYearDayOfYear = 1024
AutoPathFormat_plaYearMonth = 2048
AutoPathFormat_plaYearMonthDay = 4096
AutoPathFormat_plaYearMonthDayHour = 8192
AutoPathFormat_plaMonthDayHourMinute = 16384
DataCollectorSetStatus = Int32
DataCollectorSetStatus_plaStopped = 0
DataCollectorSetStatus_plaRunning = 1
DataCollectorSetStatus_plaCompiling = 2
DataCollectorSetStatus_plaPending = 3
DataCollectorSetStatus_plaUndefined = 4
ClockType = Int32
ClockType_plaTimeStamp = 0
ClockType_plaPerformance = 1
ClockType_plaSystem = 2
ClockType_plaCycle = 3
StreamMode = Int32
StreamMode_plaFile = 1
StreamMode_plaRealTime = 2
StreamMode_plaBoth = 3
StreamMode_plaBuffering = 4
CommitMode = Int32
CommitMode_plaCreateNew = 1
CommitMode_plaModify = 2
CommitMode_plaCreateOrModify = 3
CommitMode_plaUpdateRunningInstance = 16
CommitMode_plaFlushTrace = 32
CommitMode_plaValidateOnly = 4096
ValueMapType = Int32
ValueMapType_plaIndex = 1
ValueMapType_plaFlag = 2
ValueMapType_plaFlagArray = 3
ValueMapType_plaValidation = 4
WeekDays = Int32
WeekDays_plaRunOnce = 0
WeekDays_plaSunday = 1
WeekDays_plaMonday = 2
WeekDays_plaTuesday = 4
WeekDays_plaWednesday = 8
WeekDays_plaThursday = 16
WeekDays_plaFriday = 32
WeekDays_plaSaturday = 64
WeekDays_plaEveryday = 127
ResourcePolicy = Int32
ResourcePolicy_plaDeleteLargest = 0
ResourcePolicy_plaDeleteOldest = 1
DataManagerSteps = Int32
DataManagerSteps_plaCreateReport = 1
DataManagerSteps_plaRunRules = 2
DataManagerSteps_plaCreateHtml = 4
DataManagerSteps_plaFolderActions = 8
DataManagerSteps_plaResourceFreeing = 16
FolderActionSteps = Int32
FolderActionSteps_plaCreateCab = 1
FolderActionSteps_plaDeleteData = 2
FolderActionSteps_plaSendCab = 4
FolderActionSteps_plaDeleteCab = 8
FolderActionSteps_plaDeleteReport = 16
def _define_PLA_CABEXTRACT_CALLBACK():
    return CFUNCTYPE(Void,win32more.Foundation.PWSTR,c_void_p, use_last_error=False)
def _define_IDataCollectorSet_head():
    class IDataCollectorSet(win32more.System.Com.IDispatch_head):
        Guid = Guid('03837520-098b-11d8-9414-505054503030')
    return IDataCollectorSet
def _define_IDataCollectorSet():
    IDataCollectorSet = win32more.System.Performance.IDataCollectorSet_head
    IDataCollectorSet.get_DataCollectors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.IDataCollectorCollection_head), use_last_error=False)(7, 'get_DataCollectors', ((1, 'collectors'),)))
    IDataCollectorSet.get_Duration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'get_Duration', ((1, 'seconds'),)))
    IDataCollectorSet.put_Duration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'put_Duration', ((1, 'seconds'),)))
    IDataCollectorSet.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Description', ((1, 'description'),)))
    IDataCollectorSet.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(11, 'put_Description', ((1, 'description'),)))
    IDataCollectorSet.get_DescriptionUnresolved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_DescriptionUnresolved', ((1, 'Descr'),)))
    IDataCollectorSet.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_DisplayName', ((1, 'DisplayName'),)))
    IDataCollectorSet.put_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'put_DisplayName', ((1, 'DisplayName'),)))
    IDataCollectorSet.get_DisplayNameUnresolved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_DisplayNameUnresolved', ((1, 'name'),)))
    IDataCollectorSet.get_Keywords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(16, 'get_Keywords', ((1, 'keywords'),)))
    IDataCollectorSet.put_Keywords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(17, 'put_Keywords', ((1, 'keywords'),)))
    IDataCollectorSet.get_LatestOutputLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_LatestOutputLocation', ((1, 'path'),)))
    IDataCollectorSet.put_LatestOutputLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(19, 'put_LatestOutputLocation', ((1, 'path'),)))
    IDataCollectorSet.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_Name', ((1, 'name'),)))
    IDataCollectorSet.get_OutputLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(21, 'get_OutputLocation', ((1, 'path'),)))
    IDataCollectorSet.get_RootPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_RootPath', ((1, 'folder'),)))
    IDataCollectorSet.put_RootPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(23, 'put_RootPath', ((1, 'folder'),)))
    IDataCollectorSet.get_Segment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(24, 'get_Segment', ((1, 'segment'),)))
    IDataCollectorSet.put_Segment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(25, 'put_Segment', ((1, 'segment'),)))
    IDataCollectorSet.get_SegmentMaxDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(26, 'get_SegmentMaxDuration', ((1, 'seconds'),)))
    IDataCollectorSet.put_SegmentMaxDuration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(27, 'put_SegmentMaxDuration', ((1, 'seconds'),)))
    IDataCollectorSet.get_SegmentMaxSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(28, 'get_SegmentMaxSize', ((1, 'size'),)))
    IDataCollectorSet.put_SegmentMaxSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(29, 'put_SegmentMaxSize', ((1, 'size'),)))
    IDataCollectorSet.get_SerialNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(30, 'get_SerialNumber', ((1, 'index'),)))
    IDataCollectorSet.put_SerialNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(31, 'put_SerialNumber', ((1, 'index'),)))
    IDataCollectorSet.get_Server = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(32, 'get_Server', ((1, 'server'),)))
    IDataCollectorSet.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.DataCollectorSetStatus), use_last_error=False)(33, 'get_Status', ((1, 'status'),)))
    IDataCollectorSet.get_Subdirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(34, 'get_Subdirectory', ((1, 'folder'),)))
    IDataCollectorSet.put_Subdirectory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(35, 'put_Subdirectory', ((1, 'folder'),)))
    IDataCollectorSet.get_SubdirectoryFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.AutoPathFormat), use_last_error=False)(36, 'get_SubdirectoryFormat', ((1, 'format'),)))
    IDataCollectorSet.put_SubdirectoryFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.AutoPathFormat, use_last_error=False)(37, 'put_SubdirectoryFormat', ((1, 'format'),)))
    IDataCollectorSet.get_SubdirectoryFormatPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(38, 'get_SubdirectoryFormatPattern', ((1, 'pattern'),)))
    IDataCollectorSet.put_SubdirectoryFormatPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(39, 'put_SubdirectoryFormatPattern', ((1, 'pattern'),)))
    IDataCollectorSet.get_Task = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(40, 'get_Task', ((1, 'task'),)))
    IDataCollectorSet.put_Task = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(41, 'put_Task', ((1, 'task'),)))
    IDataCollectorSet.get_TaskRunAsSelf = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(42, 'get_TaskRunAsSelf', ((1, 'RunAsSelf'),)))
    IDataCollectorSet.put_TaskRunAsSelf = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(43, 'put_TaskRunAsSelf', ((1, 'RunAsSelf'),)))
    IDataCollectorSet.get_TaskArguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(44, 'get_TaskArguments', ((1, 'task'),)))
    IDataCollectorSet.put_TaskArguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(45, 'put_TaskArguments', ((1, 'task'),)))
    IDataCollectorSet.get_TaskUserTextArguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(46, 'get_TaskUserTextArguments', ((1, 'UserText'),)))
    IDataCollectorSet.put_TaskUserTextArguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(47, 'put_TaskUserTextArguments', ((1, 'UserText'),)))
    IDataCollectorSet.get_Schedules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.IScheduleCollection_head), use_last_error=False)(48, 'get_Schedules', ((1, 'ppSchedules'),)))
    IDataCollectorSet.get_SchedulesEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(49, 'get_SchedulesEnabled', ((1, 'enabled'),)))
    IDataCollectorSet.put_SchedulesEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(50, 'put_SchedulesEnabled', ((1, 'enabled'),)))
    IDataCollectorSet.get_UserAccount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(51, 'get_UserAccount', ((1, 'user'),)))
    IDataCollectorSet.get_Xml = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(52, 'get_Xml', ((1, 'xml'),)))
    IDataCollectorSet.get_Security = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(53, 'get_Security', ((1, 'pbstrSecurity'),)))
    IDataCollectorSet.put_Security = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(54, 'put_Security', ((1, 'bstrSecurity'),)))
    IDataCollectorSet.get_StopOnCompletion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(55, 'get_StopOnCompletion', ((1, 'Stop'),)))
    IDataCollectorSet.put_StopOnCompletion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(56, 'put_StopOnCompletion', ((1, 'Stop'),)))
    IDataCollectorSet.get_DataManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.IDataManager_head), use_last_error=False)(57, 'get_DataManager', ((1, 'DataManager'),)))
    IDataCollectorSet.SetCredentials = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(58, 'SetCredentials', ((1, 'user'),(1, 'password'),)))
    IDataCollectorSet.Query = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(59, 'Query', ((1, 'name'),(1, 'server'),)))
    IDataCollectorSet.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.Performance.CommitMode,POINTER(win32more.System.Performance.IValueMap_head), use_last_error=False)(60, 'Commit', ((1, 'name'),(1, 'server'),(1, 'mode'),(1, 'validation'),)))
    IDataCollectorSet.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(61, 'Delete', ()))
    IDataCollectorSet.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(62, 'Start', ((1, 'Synchronous'),)))
    IDataCollectorSet.Stop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(63, 'Stop', ((1, 'Synchronous'),)))
    IDataCollectorSet.SetXml = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Performance.IValueMap_head), use_last_error=False)(64, 'SetXml', ((1, 'xml'),(1, 'validation'),)))
    IDataCollectorSet.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(65, 'SetValue', ((1, 'key'),(1, 'value'),)))
    IDataCollectorSet.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(66, 'GetValue', ((1, 'key'),(1, 'value'),)))
    win32more.System.Com.IDispatch
    return IDataCollectorSet
def _define_IDataManager_head():
    class IDataManager(win32more.System.Com.IDispatch_head):
        Guid = Guid('03837541-098b-11d8-9414-505054503030')
    return IDataManager
def _define_IDataManager():
    IDataManager = win32more.System.Performance.IDataManager_head
    IDataManager.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_Enabled', ((1, 'pfEnabled'),)))
    IDataManager.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(8, 'put_Enabled', ((1, 'fEnabled'),)))
    IDataManager.get_CheckBeforeRunning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_CheckBeforeRunning', ((1, 'pfCheck'),)))
    IDataManager.put_CheckBeforeRunning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(10, 'put_CheckBeforeRunning', ((1, 'fCheck'),)))
    IDataManager.get_MinFreeDisk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'get_MinFreeDisk', ((1, 'MinFreeDisk'),)))
    IDataManager.put_MinFreeDisk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(12, 'put_MinFreeDisk', ((1, 'MinFreeDisk'),)))
    IDataManager.get_MaxSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(13, 'get_MaxSize', ((1, 'pulMaxSize'),)))
    IDataManager.put_MaxSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(14, 'put_MaxSize', ((1, 'ulMaxSize'),)))
    IDataManager.get_MaxFolderCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(15, 'get_MaxFolderCount', ((1, 'pulMaxFolderCount'),)))
    IDataManager.put_MaxFolderCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(16, 'put_MaxFolderCount', ((1, 'ulMaxFolderCount'),)))
    IDataManager.get_ResourcePolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.ResourcePolicy), use_last_error=False)(17, 'get_ResourcePolicy', ((1, 'pPolicy'),)))
    IDataManager.put_ResourcePolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.ResourcePolicy, use_last_error=False)(18, 'put_ResourcePolicy', ((1, 'Policy'),)))
    IDataManager.get_FolderActions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.IFolderActionCollection_head), use_last_error=False)(19, 'get_FolderActions', ((1, 'Actions'),)))
    IDataManager.get_ReportSchema = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(20, 'get_ReportSchema', ((1, 'ReportSchema'),)))
    IDataManager.put_ReportSchema = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(21, 'put_ReportSchema', ((1, 'ReportSchema'),)))
    IDataManager.get_ReportFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'get_ReportFileName', ((1, 'pbstrFilename'),)))
    IDataManager.put_ReportFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(23, 'put_ReportFileName', ((1, 'pbstrFilename'),)))
    IDataManager.get_RuleTargetFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'get_RuleTargetFileName', ((1, 'Filename'),)))
    IDataManager.put_RuleTargetFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'put_RuleTargetFileName', ((1, 'Filename'),)))
    IDataManager.get_EventsFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(26, 'get_EventsFileName', ((1, 'pbstrFilename'),)))
    IDataManager.put_EventsFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(27, 'put_EventsFileName', ((1, 'pbstrFilename'),)))
    IDataManager.get_Rules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(28, 'get_Rules', ((1, 'pbstrXml'),)))
    IDataManager.put_Rules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(29, 'put_Rules', ((1, 'bstrXml'),)))
    IDataManager.Run = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.DataManagerSteps,win32more.Foundation.BSTR,POINTER(win32more.System.Performance.IValueMap_head), use_last_error=False)(30, 'Run', ((1, 'Steps'),(1, 'bstrFolder'),(1, 'Errors'),)))
    IDataManager.Extract = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(31, 'Extract', ((1, 'CabFilename'),(1, 'DestinationPath'),)))
    win32more.System.Com.IDispatch
    return IDataManager
def _define_IFolderAction_head():
    class IFolderAction(win32more.System.Com.IDispatch_head):
        Guid = Guid('03837543-098b-11d8-9414-505054503030')
    return IFolderAction
def _define_IFolderAction():
    IFolderAction = win32more.System.Performance.IFolderAction_head
    IFolderAction.get_Age = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'get_Age', ((1, 'pulAge'),)))
    IFolderAction.put_Age = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'put_Age', ((1, 'ulAge'),)))
    IFolderAction.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'get_Size', ((1, 'pulAge'),)))
    IFolderAction.put_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'put_Size', ((1, 'ulAge'),)))
    IFolderAction.get_Actions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.FolderActionSteps), use_last_error=False)(11, 'get_Actions', ((1, 'Steps'),)))
    IFolderAction.put_Actions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.FolderActionSteps, use_last_error=False)(12, 'put_Actions', ((1, 'Steps'),)))
    IFolderAction.get_SendCabTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_SendCabTo', ((1, 'pbstrDestination'),)))
    IFolderAction.put_SendCabTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'put_SendCabTo', ((1, 'bstrDestination'),)))
    win32more.System.Com.IDispatch
    return IFolderAction
def _define_IFolderActionCollection_head():
    class IFolderActionCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('03837544-098b-11d8-9414-505054503030')
    return IFolderActionCollection
def _define_IFolderActionCollection():
    IFolderActionCollection = win32more.System.Performance.IFolderActionCollection_head
    IFolderActionCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(7, 'get_Count', ((1, 'Count'),)))
    IFolderActionCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Performance.IFolderAction_head), use_last_error=False)(8, 'get_Item', ((1, 'Index'),(1, 'Action'),)))
    IFolderActionCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'Enum'),)))
    IFolderActionCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.IFolderAction_head, use_last_error=False)(10, 'Add', ((1, 'Action'),)))
    IFolderActionCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(11, 'Remove', ((1, 'Index'),)))
    IFolderActionCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    IFolderActionCollection.AddRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.IFolderActionCollection_head, use_last_error=False)(13, 'AddRange', ((1, 'Actions'),)))
    IFolderActionCollection.CreateFolderAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.IFolderAction_head), use_last_error=False)(14, 'CreateFolderAction', ((1, 'FolderAction'),)))
    win32more.System.Com.IDispatch
    return IFolderActionCollection
def _define_IDataCollector_head():
    class IDataCollector(win32more.System.Com.IDispatch_head):
        Guid = Guid('038374ff-098b-11d8-9414-505054503030')
    return IDataCollector
def _define_IDataCollector():
    IDataCollector = win32more.System.Performance.IDataCollector_head
    IDataCollector.get_DataCollectorSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.IDataCollectorSet_head), use_last_error=False)(7, 'get_DataCollectorSet', ((1, 'group'),)))
    IDataCollector.put_DataCollectorSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.IDataCollectorSet_head, use_last_error=False)(8, 'put_DataCollectorSet', ((1, 'group'),)))
    IDataCollector.get_DataCollectorType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.DataCollectorType), use_last_error=False)(9, 'get_DataCollectorType', ((1, 'type'),)))
    IDataCollector.get_FileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_FileName', ((1, 'name'),)))
    IDataCollector.put_FileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(11, 'put_FileName', ((1, 'name'),)))
    IDataCollector.get_FileNameFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.AutoPathFormat), use_last_error=False)(12, 'get_FileNameFormat', ((1, 'format'),)))
    IDataCollector.put_FileNameFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.AutoPathFormat, use_last_error=False)(13, 'put_FileNameFormat', ((1, 'format'),)))
    IDataCollector.get_FileNameFormatPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'get_FileNameFormatPattern', ((1, 'pattern'),)))
    IDataCollector.put_FileNameFormatPattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'put_FileNameFormatPattern', ((1, 'pattern'),)))
    IDataCollector.get_LatestOutputLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'get_LatestOutputLocation', ((1, 'path'),)))
    IDataCollector.put_LatestOutputLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(17, 'put_LatestOutputLocation', ((1, 'path'),)))
    IDataCollector.get_LogAppend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(18, 'get_LogAppend', ((1, 'append'),)))
    IDataCollector.put_LogAppend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(19, 'put_LogAppend', ((1, 'append'),)))
    IDataCollector.get_LogCircular = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(20, 'get_LogCircular', ((1, 'circular'),)))
    IDataCollector.put_LogCircular = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(21, 'put_LogCircular', ((1, 'circular'),)))
    IDataCollector.get_LogOverwrite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(22, 'get_LogOverwrite', ((1, 'overwrite'),)))
    IDataCollector.put_LogOverwrite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(23, 'put_LogOverwrite', ((1, 'overwrite'),)))
    IDataCollector.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'get_Name', ((1, 'name'),)))
    IDataCollector.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(25, 'put_Name', ((1, 'name'),)))
    IDataCollector.get_OutputLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(26, 'get_OutputLocation', ((1, 'path'),)))
    IDataCollector.get_Index = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(27, 'get_Index', ((1, 'index'),)))
    IDataCollector.put_Index = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(28, 'put_Index', ((1, 'index'),)))
    IDataCollector.get_Xml = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(29, 'get_Xml', ((1, 'Xml'),)))
    IDataCollector.SetXml = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Performance.IValueMap_head), use_last_error=False)(30, 'SetXml', ((1, 'Xml'),(1, 'Validation'),)))
    IDataCollector.CreateOutputLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(win32more.Foundation.BSTR), use_last_error=False)(31, 'CreateOutputLocation', ((1, 'Latest'),(1, 'Location'),)))
    win32more.System.Com.IDispatch
    return IDataCollector
def _define_IPerformanceCounterDataCollector_head():
    class IPerformanceCounterDataCollector(win32more.System.Performance.IDataCollector_head):
        Guid = Guid('03837506-098b-11d8-9414-505054503030')
    return IPerformanceCounterDataCollector
def _define_IPerformanceCounterDataCollector():
    IPerformanceCounterDataCollector = win32more.System.Performance.IPerformanceCounterDataCollector_head
    IPerformanceCounterDataCollector.get_DataSourceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(32, 'get_DataSourceName', ((1, 'dsn'),)))
    IPerformanceCounterDataCollector.put_DataSourceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(33, 'put_DataSourceName', ((1, 'dsn'),)))
    IPerformanceCounterDataCollector.get_PerformanceCounters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(34, 'get_PerformanceCounters', ((1, 'counters'),)))
    IPerformanceCounterDataCollector.put_PerformanceCounters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(35, 'put_PerformanceCounters', ((1, 'counters'),)))
    IPerformanceCounterDataCollector.get_LogFileFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.FileFormat), use_last_error=False)(36, 'get_LogFileFormat', ((1, 'format'),)))
    IPerformanceCounterDataCollector.put_LogFileFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.FileFormat, use_last_error=False)(37, 'put_LogFileFormat', ((1, 'format'),)))
    IPerformanceCounterDataCollector.get_SampleInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(38, 'get_SampleInterval', ((1, 'interval'),)))
    IPerformanceCounterDataCollector.put_SampleInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(39, 'put_SampleInterval', ((1, 'interval'),)))
    IPerformanceCounterDataCollector.get_SegmentMaxRecords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(40, 'get_SegmentMaxRecords', ((1, 'records'),)))
    IPerformanceCounterDataCollector.put_SegmentMaxRecords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(41, 'put_SegmentMaxRecords', ((1, 'records'),)))
    win32more.System.Performance.IDataCollector
    return IPerformanceCounterDataCollector
def _define_ITraceDataCollector_head():
    class ITraceDataCollector(win32more.System.Performance.IDataCollector_head):
        Guid = Guid('0383750b-098b-11d8-9414-505054503030')
    return ITraceDataCollector
def _define_ITraceDataCollector():
    ITraceDataCollector = win32more.System.Performance.ITraceDataCollector_head
    ITraceDataCollector.get_BufferSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(32, 'get_BufferSize', ((1, 'size'),)))
    ITraceDataCollector.put_BufferSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(33, 'put_BufferSize', ((1, 'size'),)))
    ITraceDataCollector.get_BuffersLost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(34, 'get_BuffersLost', ((1, 'buffers'),)))
    ITraceDataCollector.put_BuffersLost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(35, 'put_BuffersLost', ((1, 'buffers'),)))
    ITraceDataCollector.get_BuffersWritten = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(36, 'get_BuffersWritten', ((1, 'buffers'),)))
    ITraceDataCollector.put_BuffersWritten = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(37, 'put_BuffersWritten', ((1, 'buffers'),)))
    ITraceDataCollector.get_ClockType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.ClockType), use_last_error=False)(38, 'get_ClockType', ((1, 'clock'),)))
    ITraceDataCollector.put_ClockType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.ClockType, use_last_error=False)(39, 'put_ClockType', ((1, 'clock'),)))
    ITraceDataCollector.get_EventsLost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(40, 'get_EventsLost', ((1, 'events'),)))
    ITraceDataCollector.put_EventsLost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(41, 'put_EventsLost', ((1, 'events'),)))
    ITraceDataCollector.get_ExtendedModes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(42, 'get_ExtendedModes', ((1, 'mode'),)))
    ITraceDataCollector.put_ExtendedModes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(43, 'put_ExtendedModes', ((1, 'mode'),)))
    ITraceDataCollector.get_FlushTimer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(44, 'get_FlushTimer', ((1, 'seconds'),)))
    ITraceDataCollector.put_FlushTimer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(45, 'put_FlushTimer', ((1, 'seconds'),)))
    ITraceDataCollector.get_FreeBuffers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(46, 'get_FreeBuffers', ((1, 'buffers'),)))
    ITraceDataCollector.put_FreeBuffers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(47, 'put_FreeBuffers', ((1, 'buffers'),)))
    ITraceDataCollector.get_Guid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(48, 'get_Guid', ((1, 'guid'),)))
    ITraceDataCollector.put_Guid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(49, 'put_Guid', ((1, 'guid'),)))
    ITraceDataCollector.get_IsKernelTrace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(50, 'get_IsKernelTrace', ((1, 'kernel'),)))
    ITraceDataCollector.get_MaximumBuffers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(51, 'get_MaximumBuffers', ((1, 'buffers'),)))
    ITraceDataCollector.put_MaximumBuffers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(52, 'put_MaximumBuffers', ((1, 'buffers'),)))
    ITraceDataCollector.get_MinimumBuffers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(53, 'get_MinimumBuffers', ((1, 'buffers'),)))
    ITraceDataCollector.put_MinimumBuffers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(54, 'put_MinimumBuffers', ((1, 'buffers'),)))
    ITraceDataCollector.get_NumberOfBuffers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(55, 'get_NumberOfBuffers', ((1, 'buffers'),)))
    ITraceDataCollector.put_NumberOfBuffers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(56, 'put_NumberOfBuffers', ((1, 'buffers'),)))
    ITraceDataCollector.get_PreallocateFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(57, 'get_PreallocateFile', ((1, 'allocate'),)))
    ITraceDataCollector.put_PreallocateFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(58, 'put_PreallocateFile', ((1, 'allocate'),)))
    ITraceDataCollector.get_ProcessMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(59, 'get_ProcessMode', ((1, 'process'),)))
    ITraceDataCollector.put_ProcessMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(60, 'put_ProcessMode', ((1, 'process'),)))
    ITraceDataCollector.get_RealTimeBuffersLost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(61, 'get_RealTimeBuffersLost', ((1, 'buffers'),)))
    ITraceDataCollector.put_RealTimeBuffersLost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(62, 'put_RealTimeBuffersLost', ((1, 'buffers'),)))
    ITraceDataCollector.get_SessionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(63, 'get_SessionId', ((1, 'id'),)))
    ITraceDataCollector.put_SessionId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64, use_last_error=False)(64, 'put_SessionId', ((1, 'id'),)))
    ITraceDataCollector.get_SessionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(65, 'get_SessionName', ((1, 'name'),)))
    ITraceDataCollector.put_SessionName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(66, 'put_SessionName', ((1, 'name'),)))
    ITraceDataCollector.get_SessionThreadId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(67, 'get_SessionThreadId', ((1, 'tid'),)))
    ITraceDataCollector.put_SessionThreadId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(68, 'put_SessionThreadId', ((1, 'tid'),)))
    ITraceDataCollector.get_StreamMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.StreamMode), use_last_error=False)(69, 'get_StreamMode', ((1, 'mode'),)))
    ITraceDataCollector.put_StreamMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.StreamMode, use_last_error=False)(70, 'put_StreamMode', ((1, 'mode'),)))
    ITraceDataCollector.get_TraceDataProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.ITraceDataProviderCollection_head), use_last_error=False)(71, 'get_TraceDataProviders', ((1, 'providers'),)))
    win32more.System.Performance.IDataCollector
    return ITraceDataCollector
def _define_IConfigurationDataCollector_head():
    class IConfigurationDataCollector(win32more.System.Performance.IDataCollector_head):
        Guid = Guid('03837514-098b-11d8-9414-505054503030')
    return IConfigurationDataCollector
def _define_IConfigurationDataCollector():
    IConfigurationDataCollector = win32more.System.Performance.IConfigurationDataCollector_head
    IConfigurationDataCollector.get_FileMaxCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(32, 'get_FileMaxCount', ((1, 'count'),)))
    IConfigurationDataCollector.put_FileMaxCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(33, 'put_FileMaxCount', ((1, 'count'),)))
    IConfigurationDataCollector.get_FileMaxRecursiveDepth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(34, 'get_FileMaxRecursiveDepth', ((1, 'depth'),)))
    IConfigurationDataCollector.put_FileMaxRecursiveDepth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(35, 'put_FileMaxRecursiveDepth', ((1, 'depth'),)))
    IConfigurationDataCollector.get_FileMaxTotalSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(36, 'get_FileMaxTotalSize', ((1, 'size'),)))
    IConfigurationDataCollector.put_FileMaxTotalSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(37, 'put_FileMaxTotalSize', ((1, 'size'),)))
    IConfigurationDataCollector.get_Files = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(38, 'get_Files', ((1, 'Files'),)))
    IConfigurationDataCollector.put_Files = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(39, 'put_Files', ((1, 'Files'),)))
    IConfigurationDataCollector.get_ManagementQueries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(40, 'get_ManagementQueries', ((1, 'Queries'),)))
    IConfigurationDataCollector.put_ManagementQueries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(41, 'put_ManagementQueries', ((1, 'Queries'),)))
    IConfigurationDataCollector.get_QueryNetworkAdapters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(42, 'get_QueryNetworkAdapters', ((1, 'network'),)))
    IConfigurationDataCollector.put_QueryNetworkAdapters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(43, 'put_QueryNetworkAdapters', ((1, 'network'),)))
    IConfigurationDataCollector.get_RegistryKeys = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(44, 'get_RegistryKeys', ((1, 'query'),)))
    IConfigurationDataCollector.put_RegistryKeys = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(45, 'put_RegistryKeys', ((1, 'query'),)))
    IConfigurationDataCollector.get_RegistryMaxRecursiveDepth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(46, 'get_RegistryMaxRecursiveDepth', ((1, 'depth'),)))
    IConfigurationDataCollector.put_RegistryMaxRecursiveDepth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(47, 'put_RegistryMaxRecursiveDepth', ((1, 'depth'),)))
    IConfigurationDataCollector.get_SystemStateFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(48, 'get_SystemStateFile', ((1, 'FileName'),)))
    IConfigurationDataCollector.put_SystemStateFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(49, 'put_SystemStateFile', ((1, 'FileName'),)))
    win32more.System.Performance.IDataCollector
    return IConfigurationDataCollector
def _define_IAlertDataCollector_head():
    class IAlertDataCollector(win32more.System.Performance.IDataCollector_head):
        Guid = Guid('03837516-098b-11d8-9414-505054503030')
    return IAlertDataCollector
def _define_IAlertDataCollector():
    IAlertDataCollector = win32more.System.Performance.IAlertDataCollector_head
    IAlertDataCollector.get_AlertThresholds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(32, 'get_AlertThresholds', ((1, 'alerts'),)))
    IAlertDataCollector.put_AlertThresholds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(33, 'put_AlertThresholds', ((1, 'alerts'),)))
    IAlertDataCollector.get_EventLog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(34, 'get_EventLog', ((1, 'log'),)))
    IAlertDataCollector.put_EventLog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(35, 'put_EventLog', ((1, 'log'),)))
    IAlertDataCollector.get_SampleInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(36, 'get_SampleInterval', ((1, 'interval'),)))
    IAlertDataCollector.put_SampleInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(37, 'put_SampleInterval', ((1, 'interval'),)))
    IAlertDataCollector.get_Task = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(38, 'get_Task', ((1, 'task'),)))
    IAlertDataCollector.put_Task = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(39, 'put_Task', ((1, 'task'),)))
    IAlertDataCollector.get_TaskRunAsSelf = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(40, 'get_TaskRunAsSelf', ((1, 'RunAsSelf'),)))
    IAlertDataCollector.put_TaskRunAsSelf = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(41, 'put_TaskRunAsSelf', ((1, 'RunAsSelf'),)))
    IAlertDataCollector.get_TaskArguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(42, 'get_TaskArguments', ((1, 'task'),)))
    IAlertDataCollector.put_TaskArguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(43, 'put_TaskArguments', ((1, 'task'),)))
    IAlertDataCollector.get_TaskUserTextArguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(44, 'get_TaskUserTextArguments', ((1, 'task'),)))
    IAlertDataCollector.put_TaskUserTextArguments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(45, 'put_TaskUserTextArguments', ((1, 'task'),)))
    IAlertDataCollector.get_TriggerDataCollectorSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(46, 'get_TriggerDataCollectorSet', ((1, 'name'),)))
    IAlertDataCollector.put_TriggerDataCollectorSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(47, 'put_TriggerDataCollectorSet', ((1, 'name'),)))
    win32more.System.Performance.IDataCollector
    return IAlertDataCollector
def _define_IApiTracingDataCollector_head():
    class IApiTracingDataCollector(win32more.System.Performance.IDataCollector_head):
        Guid = Guid('0383751a-098b-11d8-9414-505054503030')
    return IApiTracingDataCollector
def _define_IApiTracingDataCollector():
    IApiTracingDataCollector = win32more.System.Performance.IApiTracingDataCollector_head
    IApiTracingDataCollector.get_LogApiNamesOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(32, 'get_LogApiNamesOnly', ((1, 'logapinames'),)))
    IApiTracingDataCollector.put_LogApiNamesOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(33, 'put_LogApiNamesOnly', ((1, 'logapinames'),)))
    IApiTracingDataCollector.get_LogApisRecursively = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(34, 'get_LogApisRecursively', ((1, 'logrecursively'),)))
    IApiTracingDataCollector.put_LogApisRecursively = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(35, 'put_LogApisRecursively', ((1, 'logrecursively'),)))
    IApiTracingDataCollector.get_ExePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(36, 'get_ExePath', ((1, 'exepath'),)))
    IApiTracingDataCollector.put_ExePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(37, 'put_ExePath', ((1, 'exepath'),)))
    IApiTracingDataCollector.get_LogFilePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(38, 'get_LogFilePath', ((1, 'logfilepath'),)))
    IApiTracingDataCollector.put_LogFilePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(39, 'put_LogFilePath', ((1, 'logfilepath'),)))
    IApiTracingDataCollector.get_IncludeModules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(40, 'get_IncludeModules', ((1, 'includemodules'),)))
    IApiTracingDataCollector.put_IncludeModules = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(41, 'put_IncludeModules', ((1, 'includemodules'),)))
    IApiTracingDataCollector.get_IncludeApis = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(42, 'get_IncludeApis', ((1, 'includeapis'),)))
    IApiTracingDataCollector.put_IncludeApis = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(43, 'put_IncludeApis', ((1, 'includeapis'),)))
    IApiTracingDataCollector.get_ExcludeApis = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(44, 'get_ExcludeApis', ((1, 'excludeapis'),)))
    IApiTracingDataCollector.put_ExcludeApis = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(45, 'put_ExcludeApis', ((1, 'excludeapis'),)))
    win32more.System.Performance.IDataCollector
    return IApiTracingDataCollector
def _define_IDataCollectorCollection_head():
    class IDataCollectorCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('03837502-098b-11d8-9414-505054503030')
    return IDataCollectorCollection
def _define_IDataCollectorCollection():
    IDataCollectorCollection = win32more.System.Performance.IDataCollectorCollection_head
    IDataCollectorCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'retVal'),)))
    IDataCollectorCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Performance.IDataCollector_head), use_last_error=False)(8, 'get_Item', ((1, 'index'),(1, 'collector'),)))
    IDataCollectorCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'retVal'),)))
    IDataCollectorCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.IDataCollector_head, use_last_error=False)(10, 'Add', ((1, 'collector'),)))
    IDataCollectorCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(11, 'Remove', ((1, 'collector'),)))
    IDataCollectorCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    IDataCollectorCollection.AddRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.IDataCollectorCollection_head, use_last_error=False)(13, 'AddRange', ((1, 'collectors'),)))
    IDataCollectorCollection.CreateDataCollectorFromXml = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Performance.IValueMap_head),POINTER(win32more.System.Performance.IDataCollector_head), use_last_error=False)(14, 'CreateDataCollectorFromXml', ((1, 'bstrXml'),(1, 'pValidation'),(1, 'pCollector'),)))
    IDataCollectorCollection.CreateDataCollector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.DataCollectorType,POINTER(win32more.System.Performance.IDataCollector_head), use_last_error=False)(15, 'CreateDataCollector', ((1, 'Type'),(1, 'Collector'),)))
    win32more.System.Com.IDispatch
    return IDataCollectorCollection
def _define_IDataCollectorSetCollection_head():
    class IDataCollectorSetCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('03837524-098b-11d8-9414-505054503030')
    return IDataCollectorSetCollection
def _define_IDataCollectorSetCollection():
    IDataCollectorSetCollection = win32more.System.Performance.IDataCollectorSetCollection_head
    IDataCollectorSetCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'retVal'),)))
    IDataCollectorSetCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Performance.IDataCollectorSet_head), use_last_error=False)(8, 'get_Item', ((1, 'index'),(1, 'set'),)))
    IDataCollectorSetCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'retVal'),)))
    IDataCollectorSetCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.IDataCollectorSet_head, use_last_error=False)(10, 'Add', ((1, 'set'),)))
    IDataCollectorSetCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(11, 'Remove', ((1, 'set'),)))
    IDataCollectorSetCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    IDataCollectorSetCollection.AddRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.IDataCollectorSetCollection_head, use_last_error=False)(13, 'AddRange', ((1, 'sets'),)))
    IDataCollectorSetCollection.GetDataCollectorSets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(14, 'GetDataCollectorSets', ((1, 'server'),(1, 'filter'),)))
    win32more.System.Com.IDispatch
    return IDataCollectorSetCollection
def _define_ITraceDataProvider_head():
    class ITraceDataProvider(win32more.System.Com.IDispatch_head):
        Guid = Guid('03837512-098b-11d8-9414-505054503030')
    return ITraceDataProvider
def _define_ITraceDataProvider():
    ITraceDataProvider = win32more.System.Performance.ITraceDataProvider_head
    ITraceDataProvider.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_DisplayName', ((1, 'name'),)))
    ITraceDataProvider.put_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_DisplayName', ((1, 'name'),)))
    ITraceDataProvider.get_Guid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(9, 'get_Guid', ((1, 'guid'),)))
    ITraceDataProvider.put_Guid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid, use_last_error=False)(10, 'put_Guid', ((1, 'guid'),)))
    ITraceDataProvider.get_Level = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.IValueMap_head), use_last_error=False)(11, 'get_Level', ((1, 'ppLevel'),)))
    ITraceDataProvider.get_KeywordsAny = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.IValueMap_head), use_last_error=False)(12, 'get_KeywordsAny', ((1, 'ppKeywords'),)))
    ITraceDataProvider.get_KeywordsAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.IValueMap_head), use_last_error=False)(13, 'get_KeywordsAll', ((1, 'ppKeywords'),)))
    ITraceDataProvider.get_Properties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.IValueMap_head), use_last_error=False)(14, 'get_Properties', ((1, 'ppProperties'),)))
    ITraceDataProvider.get_FilterEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_FilterEnabled', ((1, 'FilterEnabled'),)))
    ITraceDataProvider.put_FilterEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(16, 'put_FilterEnabled', ((1, 'FilterEnabled'),)))
    ITraceDataProvider.get_FilterType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(17, 'get_FilterType', ((1, 'pulType'),)))
    ITraceDataProvider.put_FilterType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(18, 'put_FilterType', ((1, 'ulType'),)))
    ITraceDataProvider.get_FilterData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(19, 'get_FilterData', ((1, 'ppData'),)))
    ITraceDataProvider.put_FilterData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(20, 'put_FilterData', ((1, 'pData'),)))
    ITraceDataProvider.Query = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR, use_last_error=False)(21, 'Query', ((1, 'bstrName'),(1, 'bstrServer'),)))
    ITraceDataProvider.Resolve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head, use_last_error=False)(22, 'Resolve', ((1, 'pFrom'),)))
    ITraceDataProvider.SetSecurity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(23, 'SetSecurity', ((1, 'Sddl'),)))
    ITraceDataProvider.GetSecurity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(24, 'GetSecurity', ((1, 'SecurityInfo'),(1, 'Sddl'),)))
    ITraceDataProvider.GetRegisteredProcesses = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.IValueMap_head), use_last_error=False)(25, 'GetRegisteredProcesses', ((1, 'Processes'),)))
    win32more.System.Com.IDispatch
    return ITraceDataProvider
def _define_ITraceDataProviderCollection_head():
    class ITraceDataProviderCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('03837510-098b-11d8-9414-505054503030')
    return ITraceDataProviderCollection
def _define_ITraceDataProviderCollection():
    ITraceDataProviderCollection = win32more.System.Performance.ITraceDataProviderCollection_head
    ITraceDataProviderCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'retVal'),)))
    ITraceDataProviderCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Performance.ITraceDataProvider_head), use_last_error=False)(8, 'get_Item', ((1, 'index'),(1, 'ppProvider'),)))
    ITraceDataProviderCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'retVal'),)))
    ITraceDataProviderCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.ITraceDataProvider_head, use_last_error=False)(10, 'Add', ((1, 'pProvider'),)))
    ITraceDataProviderCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(11, 'Remove', ((1, 'vProvider'),)))
    ITraceDataProviderCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    ITraceDataProviderCollection.AddRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.ITraceDataProviderCollection_head, use_last_error=False)(13, 'AddRange', ((1, 'providers'),)))
    ITraceDataProviderCollection.CreateTraceDataProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.ITraceDataProvider_head), use_last_error=False)(14, 'CreateTraceDataProvider', ((1, 'Provider'),)))
    ITraceDataProviderCollection.GetTraceDataProviders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(15, 'GetTraceDataProviders', ((1, 'server'),)))
    ITraceDataProviderCollection.GetTraceDataProvidersByProcess = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32, use_last_error=False)(16, 'GetTraceDataProvidersByProcess', ((1, 'Server'),(1, 'Pid'),)))
    win32more.System.Com.IDispatch
    return ITraceDataProviderCollection
def _define_ISchedule_head():
    class ISchedule(win32more.System.Com.IDispatch_head):
        Guid = Guid('0383753a-098b-11d8-9414-505054503030')
    return ISchedule
def _define_ISchedule():
    ISchedule = win32more.System.Performance.ISchedule_head
    ISchedule.get_StartDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_StartDate', ((1, 'start'),)))
    ISchedule.put_StartDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(8, 'put_StartDate', ((1, 'start'),)))
    ISchedule.get_EndDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'get_EndDate', ((1, 'end'),)))
    ISchedule.put_EndDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(10, 'put_EndDate', ((1, 'end'),)))
    ISchedule.get_StartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(11, 'get_StartTime', ((1, 'start'),)))
    ISchedule.put_StartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(12, 'put_StartTime', ((1, 'start'),)))
    ISchedule.get_Days = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.WeekDays), use_last_error=False)(13, 'get_Days', ((1, 'days'),)))
    ISchedule.put_Days = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.WeekDays, use_last_error=False)(14, 'put_Days', ((1, 'days'),)))
    win32more.System.Com.IDispatch
    return ISchedule
def _define_IScheduleCollection_head():
    class IScheduleCollection(win32more.System.Com.IDispatch_head):
        Guid = Guid('0383753d-098b-11d8-9414-505054503030')
    return IScheduleCollection
def _define_IScheduleCollection():
    IScheduleCollection = win32more.System.Performance.IScheduleCollection_head
    IScheduleCollection.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'retVal'),)))
    IScheduleCollection.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Performance.ISchedule_head), use_last_error=False)(8, 'get_Item', ((1, 'index'),(1, 'ppSchedule'),)))
    IScheduleCollection.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'ienum'),)))
    IScheduleCollection.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.ISchedule_head, use_last_error=False)(10, 'Add', ((1, 'pSchedule'),)))
    IScheduleCollection.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(11, 'Remove', ((1, 'vSchedule'),)))
    IScheduleCollection.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'Clear', ()))
    IScheduleCollection.AddRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.IScheduleCollection_head, use_last_error=False)(13, 'AddRange', ((1, 'pSchedules'),)))
    IScheduleCollection.CreateSchedule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.ISchedule_head), use_last_error=False)(14, 'CreateSchedule', ((1, 'Schedule'),)))
    win32more.System.Com.IDispatch
    return IScheduleCollection
def _define_IValueMapItem_head():
    class IValueMapItem(win32more.System.Com.IDispatch_head):
        Guid = Guid('03837533-098b-11d8-9414-505054503030')
    return IValueMapItem
def _define_IValueMapItem():
    IValueMapItem = win32more.System.Performance.IValueMapItem_head
    IValueMapItem.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Description', ((1, 'description'),)))
    IValueMapItem.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Description', ((1, 'description'),)))
    IValueMapItem.get_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_Enabled', ((1, 'enabled'),)))
    IValueMapItem.put_Enabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(10, 'put_Enabled', ((1, 'enabled'),)))
    IValueMapItem.get_Key = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_Key', ((1, 'key'),)))
    IValueMapItem.put_Key = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_Key', ((1, 'key'),)))
    IValueMapItem.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'get_Value', ((1, 'Value'),)))
    IValueMapItem.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(14, 'put_Value', ((1, 'Value'),)))
    IValueMapItem.get_ValueMapType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.ValueMapType), use_last_error=False)(15, 'get_ValueMapType', ((1, 'type'),)))
    IValueMapItem.put_ValueMapType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.ValueMapType, use_last_error=False)(16, 'put_ValueMapType', ((1, 'type'),)))
    win32more.System.Com.IDispatch
    return IValueMapItem
def _define_IValueMap_head():
    class IValueMap(win32more.System.Com.IDispatch_head):
        Guid = Guid('03837534-098b-11d8-9414-505054503030')
    return IValueMap
def _define_IValueMap():
    IValueMap = win32more.System.Performance.IValueMap_head
    IValueMap.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'retVal'),)))
    IValueMap.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Performance.IValueMapItem_head), use_last_error=False)(8, 'get_Item', ((1, 'index'),(1, 'value'),)))
    IValueMap.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(9, 'get__NewEnum', ((1, 'retVal'),)))
    IValueMap.get_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_Description', ((1, 'description'),)))
    IValueMap.put_Description = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(11, 'put_Description', ((1, 'description'),)))
    IValueMap.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(12, 'get_Value', ((1, 'Value'),)))
    IValueMap.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(13, 'put_Value', ((1, 'Value'),)))
    IValueMap.get_ValueMapType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.ValueMapType), use_last_error=False)(14, 'get_ValueMapType', ((1, 'type'),)))
    IValueMap.put_ValueMapType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.ValueMapType, use_last_error=False)(15, 'put_ValueMapType', ((1, 'type'),)))
    IValueMap.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(16, 'Add', ((1, 'value'),)))
    IValueMap.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(17, 'Remove', ((1, 'value'),)))
    IValueMap.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'Clear', ()))
    IValueMap.AddRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.IValueMap_head, use_last_error=False)(19, 'AddRange', ((1, 'map'),)))
    IValueMap.CreateValueMapItem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.IValueMapItem_head), use_last_error=False)(20, 'CreateValueMapItem', ((1, 'Item'),)))
    win32more.System.Com.IDispatch
    return IValueMap
def _define_PERF_COUNTERSET_INFO_head():
    class PERF_COUNTERSET_INFO(Structure):
        pass
    return PERF_COUNTERSET_INFO
def _define_PERF_COUNTERSET_INFO():
    PERF_COUNTERSET_INFO = win32more.System.Performance.PERF_COUNTERSET_INFO_head
    PERF_COUNTERSET_INFO._fields_ = [
        ("CounterSetGuid", Guid),
        ("ProviderGuid", Guid),
        ("NumCounters", UInt32),
        ("InstanceType", UInt32),
    ]
    return PERF_COUNTERSET_INFO
def _define_PERF_COUNTER_INFO_head():
    class PERF_COUNTER_INFO(Structure):
        pass
    return PERF_COUNTER_INFO
def _define_PERF_COUNTER_INFO():
    PERF_COUNTER_INFO = win32more.System.Performance.PERF_COUNTER_INFO_head
    PERF_COUNTER_INFO._fields_ = [
        ("CounterId", UInt32),
        ("Type", UInt32),
        ("Attrib", UInt64),
        ("Size", UInt32),
        ("DetailLevel", UInt32),
        ("Scale", Int32),
        ("Offset", UInt32),
    ]
    return PERF_COUNTER_INFO
def _define_PERF_COUNTERSET_INSTANCE_head():
    class PERF_COUNTERSET_INSTANCE(Structure):
        pass
    return PERF_COUNTERSET_INSTANCE
def _define_PERF_COUNTERSET_INSTANCE():
    PERF_COUNTERSET_INSTANCE = win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head
    PERF_COUNTERSET_INSTANCE._fields_ = [
        ("CounterSetGuid", Guid),
        ("dwSize", UInt32),
        ("InstanceId", UInt32),
        ("InstanceNameOffset", UInt32),
        ("InstanceNameSize", UInt32),
    ]
    return PERF_COUNTERSET_INSTANCE
def _define_PERF_COUNTER_IDENTITY_head():
    class PERF_COUNTER_IDENTITY(Structure):
        pass
    return PERF_COUNTER_IDENTITY
def _define_PERF_COUNTER_IDENTITY():
    PERF_COUNTER_IDENTITY = win32more.System.Performance.PERF_COUNTER_IDENTITY_head
    PERF_COUNTER_IDENTITY._fields_ = [
        ("CounterSetGuid", Guid),
        ("BufferSize", UInt32),
        ("CounterId", UInt32),
        ("InstanceId", UInt32),
        ("MachineOffset", UInt32),
        ("NameOffset", UInt32),
        ("Reserved", UInt32),
    ]
    return PERF_COUNTER_IDENTITY
def _define_PERFLIBREQUEST():
    return CFUNCTYPE(UInt32,UInt32,c_void_p,UInt32, use_last_error=False)
def _define_PERF_MEM_ALLOC():
    return CFUNCTYPE(c_void_p,UIntPtr,c_void_p, use_last_error=False)
def _define_PERF_MEM_FREE():
    return CFUNCTYPE(Void,c_void_p,c_void_p, use_last_error=False)
def _define_PERF_PROVIDER_CONTEXT_head():
    class PERF_PROVIDER_CONTEXT(Structure):
        pass
    return PERF_PROVIDER_CONTEXT
def _define_PERF_PROVIDER_CONTEXT():
    PERF_PROVIDER_CONTEXT = win32more.System.Performance.PERF_PROVIDER_CONTEXT_head
    PERF_PROVIDER_CONTEXT._fields_ = [
        ("ContextSize", UInt32),
        ("Reserved", UInt32),
        ("ControlCallback", win32more.System.Performance.PERFLIBREQUEST),
        ("MemAllocRoutine", win32more.System.Performance.PERF_MEM_ALLOC),
        ("MemFreeRoutine", win32more.System.Performance.PERF_MEM_FREE),
        ("pMemContext", c_void_p),
    ]
    return PERF_PROVIDER_CONTEXT
def _define_PERF_INSTANCE_HEADER_head():
    class PERF_INSTANCE_HEADER(Structure):
        pass
    return PERF_INSTANCE_HEADER
def _define_PERF_INSTANCE_HEADER():
    PERF_INSTANCE_HEADER = win32more.System.Performance.PERF_INSTANCE_HEADER_head
    PERF_INSTANCE_HEADER._fields_ = [
        ("Size", UInt32),
        ("InstanceId", UInt32),
    ]
    return PERF_INSTANCE_HEADER
PerfRegInfoType = Int32
PERF_REG_COUNTERSET_STRUCT = 1
PERF_REG_COUNTER_STRUCT = 2
PERF_REG_COUNTERSET_NAME_STRING = 3
PERF_REG_COUNTERSET_HELP_STRING = 4
PERF_REG_COUNTER_NAME_STRINGS = 5
PERF_REG_COUNTER_HELP_STRINGS = 6
PERF_REG_PROVIDER_NAME = 7
PERF_REG_PROVIDER_GUID = 8
PERF_REG_COUNTERSET_ENGLISH_NAME = 9
PERF_REG_COUNTER_ENGLISH_NAMES = 10
def _define_PERF_COUNTERSET_REG_INFO_head():
    class PERF_COUNTERSET_REG_INFO(Structure):
        pass
    return PERF_COUNTERSET_REG_INFO
def _define_PERF_COUNTERSET_REG_INFO():
    PERF_COUNTERSET_REG_INFO = win32more.System.Performance.PERF_COUNTERSET_REG_INFO_head
    PERF_COUNTERSET_REG_INFO._fields_ = [
        ("CounterSetGuid", Guid),
        ("CounterSetType", UInt32),
        ("DetailLevel", UInt32),
        ("NumCounters", UInt32),
        ("InstanceType", UInt32),
    ]
    return PERF_COUNTERSET_REG_INFO
def _define_PERF_COUNTER_REG_INFO_head():
    class PERF_COUNTER_REG_INFO(Structure):
        pass
    return PERF_COUNTER_REG_INFO
def _define_PERF_COUNTER_REG_INFO():
    PERF_COUNTER_REG_INFO = win32more.System.Performance.PERF_COUNTER_REG_INFO_head
    PERF_COUNTER_REG_INFO._fields_ = [
        ("CounterId", UInt32),
        ("Type", UInt32),
        ("Attrib", UInt64),
        ("DetailLevel", UInt32),
        ("DefaultScale", Int32),
        ("BaseCounterId", UInt32),
        ("PerfTimeId", UInt32),
        ("PerfFreqId", UInt32),
        ("MultiId", UInt32),
        ("AggregateFunc", win32more.System.Performance.PERF_COUNTER_AGGREGATE_FUNC),
        ("Reserved", UInt32),
    ]
    return PERF_COUNTER_REG_INFO
def _define_PERF_STRING_BUFFER_HEADER_head():
    class PERF_STRING_BUFFER_HEADER(Structure):
        pass
    return PERF_STRING_BUFFER_HEADER
def _define_PERF_STRING_BUFFER_HEADER():
    PERF_STRING_BUFFER_HEADER = win32more.System.Performance.PERF_STRING_BUFFER_HEADER_head
    PERF_STRING_BUFFER_HEADER._fields_ = [
        ("dwSize", UInt32),
        ("dwCounters", UInt32),
    ]
    return PERF_STRING_BUFFER_HEADER
def _define_PERF_STRING_COUNTER_HEADER_head():
    class PERF_STRING_COUNTER_HEADER(Structure):
        pass
    return PERF_STRING_COUNTER_HEADER
def _define_PERF_STRING_COUNTER_HEADER():
    PERF_STRING_COUNTER_HEADER = win32more.System.Performance.PERF_STRING_COUNTER_HEADER_head
    PERF_STRING_COUNTER_HEADER._fields_ = [
        ("dwCounterId", UInt32),
        ("dwOffset", UInt32),
    ]
    return PERF_STRING_COUNTER_HEADER
def _define_PERF_COUNTER_IDENTIFIER_head():
    class PERF_COUNTER_IDENTIFIER(Structure):
        pass
    return PERF_COUNTER_IDENTIFIER
def _define_PERF_COUNTER_IDENTIFIER():
    PERF_COUNTER_IDENTIFIER = win32more.System.Performance.PERF_COUNTER_IDENTIFIER_head
    PERF_COUNTER_IDENTIFIER._fields_ = [
        ("CounterSetGuid", Guid),
        ("Status", UInt32),
        ("Size", UInt32),
        ("CounterId", UInt32),
        ("InstanceId", UInt32),
        ("Index", UInt32),
        ("Reserved", UInt32),
    ]
    return PERF_COUNTER_IDENTIFIER
def _define_PERF_DATA_HEADER_head():
    class PERF_DATA_HEADER(Structure):
        pass
    return PERF_DATA_HEADER
def _define_PERF_DATA_HEADER():
    PERF_DATA_HEADER = win32more.System.Performance.PERF_DATA_HEADER_head
    PERF_DATA_HEADER._fields_ = [
        ("dwTotalSize", UInt32),
        ("dwNumCounters", UInt32),
        ("PerfTimeStamp", Int64),
        ("PerfTime100NSec", Int64),
        ("PerfFreq", Int64),
        ("SystemTime", win32more.Foundation.SYSTEMTIME),
    ]
    return PERF_DATA_HEADER
PerfCounterDataType = Int32
PERF_ERROR_RETURN = 0
PERF_SINGLE_COUNTER = 1
PERF_MULTIPLE_COUNTERS = 2
PERF_MULTIPLE_INSTANCES = 4
PERF_COUNTERSET = 6
def _define_PERF_COUNTER_HEADER_head():
    class PERF_COUNTER_HEADER(Structure):
        pass
    return PERF_COUNTER_HEADER
def _define_PERF_COUNTER_HEADER():
    PERF_COUNTER_HEADER = win32more.System.Performance.PERF_COUNTER_HEADER_head
    PERF_COUNTER_HEADER._fields_ = [
        ("dwStatus", UInt32),
        ("dwType", win32more.System.Performance.PerfCounterDataType),
        ("dwSize", UInt32),
        ("Reserved", UInt32),
    ]
    return PERF_COUNTER_HEADER
def _define_PERF_MULTI_INSTANCES_head():
    class PERF_MULTI_INSTANCES(Structure):
        pass
    return PERF_MULTI_INSTANCES
def _define_PERF_MULTI_INSTANCES():
    PERF_MULTI_INSTANCES = win32more.System.Performance.PERF_MULTI_INSTANCES_head
    PERF_MULTI_INSTANCES._fields_ = [
        ("dwTotalSize", UInt32),
        ("dwInstances", UInt32),
    ]
    return PERF_MULTI_INSTANCES
def _define_PERF_MULTI_COUNTERS_head():
    class PERF_MULTI_COUNTERS(Structure):
        pass
    return PERF_MULTI_COUNTERS
def _define_PERF_MULTI_COUNTERS():
    PERF_MULTI_COUNTERS = win32more.System.Performance.PERF_MULTI_COUNTERS_head
    PERF_MULTI_COUNTERS._fields_ = [
        ("dwSize", UInt32),
        ("dwCounters", UInt32),
    ]
    return PERF_MULTI_COUNTERS
def _define_PERF_COUNTER_DATA_head():
    class PERF_COUNTER_DATA(Structure):
        pass
    return PERF_COUNTER_DATA
def _define_PERF_COUNTER_DATA():
    PERF_COUNTER_DATA = win32more.System.Performance.PERF_COUNTER_DATA_head
    PERF_COUNTER_DATA._fields_ = [
        ("dwDataSize", UInt32),
        ("dwSize", UInt32),
    ]
    return PERF_COUNTER_DATA
def _define_PERF_DATA_BLOCK_head():
    class PERF_DATA_BLOCK(Structure):
        pass
    return PERF_DATA_BLOCK
def _define_PERF_DATA_BLOCK():
    PERF_DATA_BLOCK = win32more.System.Performance.PERF_DATA_BLOCK_head
    PERF_DATA_BLOCK._fields_ = [
        ("Signature", Char * 4),
        ("LittleEndian", UInt32),
        ("Version", UInt32),
        ("Revision", UInt32),
        ("TotalByteLength", UInt32),
        ("HeaderLength", UInt32),
        ("NumObjectTypes", UInt32),
        ("DefaultObject", Int32),
        ("SystemTime", win32more.Foundation.SYSTEMTIME),
        ("PerfTime", win32more.Foundation.LARGE_INTEGER),
        ("PerfFreq", win32more.Foundation.LARGE_INTEGER),
        ("PerfTime100nSec", win32more.Foundation.LARGE_INTEGER),
        ("SystemNameLength", UInt32),
        ("SystemNameOffset", UInt32),
    ]
    return PERF_DATA_BLOCK
def _define_PERF_OBJECT_TYPE_head():
    class PERF_OBJECT_TYPE(Structure):
        pass
    return PERF_OBJECT_TYPE
def _define_PERF_OBJECT_TYPE():
    PERF_OBJECT_TYPE = win32more.System.Performance.PERF_OBJECT_TYPE_head
    PERF_OBJECT_TYPE._fields_ = [
        ("TotalByteLength", UInt32),
        ("DefinitionLength", UInt32),
        ("HeaderLength", UInt32),
        ("ObjectNameTitleIndex", UInt32),
        ("ObjectNameTitle", UInt32),
        ("ObjectHelpTitleIndex", UInt32),
        ("ObjectHelpTitle", UInt32),
        ("DetailLevel", UInt32),
        ("NumCounters", UInt32),
        ("DefaultCounter", Int32),
        ("NumInstances", Int32),
        ("CodePage", UInt32),
        ("PerfTime", win32more.Foundation.LARGE_INTEGER),
        ("PerfFreq", win32more.Foundation.LARGE_INTEGER),
    ]
    return PERF_OBJECT_TYPE
def _define_PERF_COUNTER_DEFINITION_head():
    class PERF_COUNTER_DEFINITION(Structure):
        pass
    return PERF_COUNTER_DEFINITION
def _define_PERF_COUNTER_DEFINITION():
    PERF_COUNTER_DEFINITION = win32more.System.Performance.PERF_COUNTER_DEFINITION_head
    PERF_COUNTER_DEFINITION._fields_ = [
        ("ByteLength", UInt32),
        ("CounterNameTitleIndex", UInt32),
        ("CounterNameTitle", UInt32),
        ("CounterHelpTitleIndex", UInt32),
        ("CounterHelpTitle", UInt32),
        ("DefaultScale", Int32),
        ("DetailLevel", UInt32),
        ("CounterType", UInt32),
        ("CounterSize", UInt32),
        ("CounterOffset", UInt32),
    ]
    return PERF_COUNTER_DEFINITION
def _define_PERF_INSTANCE_DEFINITION_head():
    class PERF_INSTANCE_DEFINITION(Structure):
        pass
    return PERF_INSTANCE_DEFINITION
def _define_PERF_INSTANCE_DEFINITION():
    PERF_INSTANCE_DEFINITION = win32more.System.Performance.PERF_INSTANCE_DEFINITION_head
    PERF_INSTANCE_DEFINITION._fields_ = [
        ("ByteLength", UInt32),
        ("ParentObjectTitleIndex", UInt32),
        ("ParentObjectInstance", UInt32),
        ("UniqueID", Int32),
        ("NameOffset", UInt32),
        ("NameLength", UInt32),
    ]
    return PERF_INSTANCE_DEFINITION
def _define_PERF_COUNTER_BLOCK_head():
    class PERF_COUNTER_BLOCK(Structure):
        pass
    return PERF_COUNTER_BLOCK
def _define_PERF_COUNTER_BLOCK():
    PERF_COUNTER_BLOCK = win32more.System.Performance.PERF_COUNTER_BLOCK_head
    PERF_COUNTER_BLOCK._fields_ = [
        ("ByteLength", UInt32),
    ]
    return PERF_COUNTER_BLOCK
def _define_PM_OPEN_PROC():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)
def _define_PM_COLLECT_PROC():
    return CFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(c_void_p),POINTER(UInt32),POINTER(UInt32), use_last_error=False)
def _define_PM_CLOSE_PROC():
    return CFUNCTYPE(UInt32, use_last_error=False)
def _define_PDH_RAW_COUNTER_head():
    class PDH_RAW_COUNTER(Structure):
        pass
    return PDH_RAW_COUNTER
def _define_PDH_RAW_COUNTER():
    PDH_RAW_COUNTER = win32more.System.Performance.PDH_RAW_COUNTER_head
    PDH_RAW_COUNTER._fields_ = [
        ("CStatus", UInt32),
        ("TimeStamp", win32more.Foundation.FILETIME),
        ("FirstValue", Int64),
        ("SecondValue", Int64),
        ("MultiCount", UInt32),
    ]
    return PDH_RAW_COUNTER
def _define_PDH_RAW_COUNTER_ITEM_A_head():
    class PDH_RAW_COUNTER_ITEM_A(Structure):
        pass
    return PDH_RAW_COUNTER_ITEM_A
def _define_PDH_RAW_COUNTER_ITEM_A():
    PDH_RAW_COUNTER_ITEM_A = win32more.System.Performance.PDH_RAW_COUNTER_ITEM_A_head
    PDH_RAW_COUNTER_ITEM_A._fields_ = [
        ("szName", win32more.Foundation.PSTR),
        ("RawValue", win32more.System.Performance.PDH_RAW_COUNTER),
    ]
    return PDH_RAW_COUNTER_ITEM_A
def _define_PDH_RAW_COUNTER_ITEM_W_head():
    class PDH_RAW_COUNTER_ITEM_W(Structure):
        pass
    return PDH_RAW_COUNTER_ITEM_W
def _define_PDH_RAW_COUNTER_ITEM_W():
    PDH_RAW_COUNTER_ITEM_W = win32more.System.Performance.PDH_RAW_COUNTER_ITEM_W_head
    PDH_RAW_COUNTER_ITEM_W._fields_ = [
        ("szName", win32more.Foundation.PWSTR),
        ("RawValue", win32more.System.Performance.PDH_RAW_COUNTER),
    ]
    return PDH_RAW_COUNTER_ITEM_W
def _define_PDH_FMT_COUNTERVALUE_head():
    class PDH_FMT_COUNTERVALUE(Structure):
        pass
    return PDH_FMT_COUNTERVALUE
def _define_PDH_FMT_COUNTERVALUE():
    PDH_FMT_COUNTERVALUE = win32more.System.Performance.PDH_FMT_COUNTERVALUE_head
    class PDH_FMT_COUNTERVALUE__Anonymous_e__Union(Union):
        pass
    PDH_FMT_COUNTERVALUE__Anonymous_e__Union._fields_ = [
        ("longValue", Int32),
        ("doubleValue", Double),
        ("largeValue", Int64),
        ("AnsiStringValue", win32more.Foundation.PSTR),
        ("WideStringValue", win32more.Foundation.PWSTR),
    ]
    PDH_FMT_COUNTERVALUE._anonymous_ = [
        'Anonymous',
    ]
    PDH_FMT_COUNTERVALUE._fields_ = [
        ("CStatus", UInt32),
        ("Anonymous", PDH_FMT_COUNTERVALUE__Anonymous_e__Union),
    ]
    return PDH_FMT_COUNTERVALUE
def _define_PDH_FMT_COUNTERVALUE_ITEM_A_head():
    class PDH_FMT_COUNTERVALUE_ITEM_A(Structure):
        pass
    return PDH_FMT_COUNTERVALUE_ITEM_A
def _define_PDH_FMT_COUNTERVALUE_ITEM_A():
    PDH_FMT_COUNTERVALUE_ITEM_A = win32more.System.Performance.PDH_FMT_COUNTERVALUE_ITEM_A_head
    PDH_FMT_COUNTERVALUE_ITEM_A._fields_ = [
        ("szName", win32more.Foundation.PSTR),
        ("FmtValue", win32more.System.Performance.PDH_FMT_COUNTERVALUE),
    ]
    return PDH_FMT_COUNTERVALUE_ITEM_A
def _define_PDH_FMT_COUNTERVALUE_ITEM_W_head():
    class PDH_FMT_COUNTERVALUE_ITEM_W(Structure):
        pass
    return PDH_FMT_COUNTERVALUE_ITEM_W
def _define_PDH_FMT_COUNTERVALUE_ITEM_W():
    PDH_FMT_COUNTERVALUE_ITEM_W = win32more.System.Performance.PDH_FMT_COUNTERVALUE_ITEM_W_head
    PDH_FMT_COUNTERVALUE_ITEM_W._fields_ = [
        ("szName", win32more.Foundation.PWSTR),
        ("FmtValue", win32more.System.Performance.PDH_FMT_COUNTERVALUE),
    ]
    return PDH_FMT_COUNTERVALUE_ITEM_W
def _define_PDH_STATISTICS_head():
    class PDH_STATISTICS(Structure):
        pass
    return PDH_STATISTICS
def _define_PDH_STATISTICS():
    PDH_STATISTICS = win32more.System.Performance.PDH_STATISTICS_head
    PDH_STATISTICS._fields_ = [
        ("dwFormat", UInt32),
        ("count", UInt32),
        ("min", win32more.System.Performance.PDH_FMT_COUNTERVALUE),
        ("max", win32more.System.Performance.PDH_FMT_COUNTERVALUE),
        ("mean", win32more.System.Performance.PDH_FMT_COUNTERVALUE),
    ]
    return PDH_STATISTICS
def _define_PDH_COUNTER_PATH_ELEMENTS_A_head():
    class PDH_COUNTER_PATH_ELEMENTS_A(Structure):
        pass
    return PDH_COUNTER_PATH_ELEMENTS_A
def _define_PDH_COUNTER_PATH_ELEMENTS_A():
    PDH_COUNTER_PATH_ELEMENTS_A = win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_A_head
    PDH_COUNTER_PATH_ELEMENTS_A._fields_ = [
        ("szMachineName", win32more.Foundation.PSTR),
        ("szObjectName", win32more.Foundation.PSTR),
        ("szInstanceName", win32more.Foundation.PSTR),
        ("szParentInstance", win32more.Foundation.PSTR),
        ("dwInstanceIndex", UInt32),
        ("szCounterName", win32more.Foundation.PSTR),
    ]
    return PDH_COUNTER_PATH_ELEMENTS_A
def _define_PDH_COUNTER_PATH_ELEMENTS_W_head():
    class PDH_COUNTER_PATH_ELEMENTS_W(Structure):
        pass
    return PDH_COUNTER_PATH_ELEMENTS_W
def _define_PDH_COUNTER_PATH_ELEMENTS_W():
    PDH_COUNTER_PATH_ELEMENTS_W = win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_W_head
    PDH_COUNTER_PATH_ELEMENTS_W._fields_ = [
        ("szMachineName", win32more.Foundation.PWSTR),
        ("szObjectName", win32more.Foundation.PWSTR),
        ("szInstanceName", win32more.Foundation.PWSTR),
        ("szParentInstance", win32more.Foundation.PWSTR),
        ("dwInstanceIndex", UInt32),
        ("szCounterName", win32more.Foundation.PWSTR),
    ]
    return PDH_COUNTER_PATH_ELEMENTS_W
def _define_PDH_DATA_ITEM_PATH_ELEMENTS_A_head():
    class PDH_DATA_ITEM_PATH_ELEMENTS_A(Structure):
        pass
    return PDH_DATA_ITEM_PATH_ELEMENTS_A
def _define_PDH_DATA_ITEM_PATH_ELEMENTS_A():
    PDH_DATA_ITEM_PATH_ELEMENTS_A = win32more.System.Performance.PDH_DATA_ITEM_PATH_ELEMENTS_A_head
    PDH_DATA_ITEM_PATH_ELEMENTS_A._fields_ = [
        ("szMachineName", win32more.Foundation.PSTR),
        ("ObjectGUID", Guid),
        ("dwItemId", UInt32),
        ("szInstanceName", win32more.Foundation.PSTR),
    ]
    return PDH_DATA_ITEM_PATH_ELEMENTS_A
def _define_PDH_DATA_ITEM_PATH_ELEMENTS_W_head():
    class PDH_DATA_ITEM_PATH_ELEMENTS_W(Structure):
        pass
    return PDH_DATA_ITEM_PATH_ELEMENTS_W
def _define_PDH_DATA_ITEM_PATH_ELEMENTS_W():
    PDH_DATA_ITEM_PATH_ELEMENTS_W = win32more.System.Performance.PDH_DATA_ITEM_PATH_ELEMENTS_W_head
    PDH_DATA_ITEM_PATH_ELEMENTS_W._fields_ = [
        ("szMachineName", win32more.Foundation.PWSTR),
        ("ObjectGUID", Guid),
        ("dwItemId", UInt32),
        ("szInstanceName", win32more.Foundation.PWSTR),
    ]
    return PDH_DATA_ITEM_PATH_ELEMENTS_W
def _define_PDH_COUNTER_INFO_A_head():
    class PDH_COUNTER_INFO_A(Structure):
        pass
    return PDH_COUNTER_INFO_A
def _define_PDH_COUNTER_INFO_A():
    PDH_COUNTER_INFO_A = win32more.System.Performance.PDH_COUNTER_INFO_A_head
    class PDH_COUNTER_INFO_A__Anonymous_e__Union(Union):
        pass
    class PDH_COUNTER_INFO_A__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    PDH_COUNTER_INFO_A__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("szMachineName", win32more.Foundation.PSTR),
        ("szObjectName", win32more.Foundation.PSTR),
        ("szInstanceName", win32more.Foundation.PSTR),
        ("szParentInstance", win32more.Foundation.PSTR),
        ("dwInstanceIndex", UInt32),
        ("szCounterName", win32more.Foundation.PSTR),
    ]
    PDH_COUNTER_INFO_A__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    PDH_COUNTER_INFO_A__Anonymous_e__Union._fields_ = [
        ("DataItemPath", win32more.System.Performance.PDH_DATA_ITEM_PATH_ELEMENTS_A),
        ("CounterPath", win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_A),
        ("Anonymous", PDH_COUNTER_INFO_A__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    PDH_COUNTER_INFO_A._anonymous_ = [
        'Anonymous',
    ]
    PDH_COUNTER_INFO_A._fields_ = [
        ("dwLength", UInt32),
        ("dwType", UInt32),
        ("CVersion", UInt32),
        ("CStatus", UInt32),
        ("lScale", Int32),
        ("lDefaultScale", Int32),
        ("dwUserData", UIntPtr),
        ("dwQueryUserData", UIntPtr),
        ("szFullPath", win32more.Foundation.PSTR),
        ("Anonymous", PDH_COUNTER_INFO_A__Anonymous_e__Union),
        ("szExplainText", win32more.Foundation.PSTR),
        ("DataBuffer", UInt32 * 0),
    ]
    return PDH_COUNTER_INFO_A
def _define_PDH_COUNTER_INFO_W_head():
    class PDH_COUNTER_INFO_W(Structure):
        pass
    return PDH_COUNTER_INFO_W
def _define_PDH_COUNTER_INFO_W():
    PDH_COUNTER_INFO_W = win32more.System.Performance.PDH_COUNTER_INFO_W_head
    class PDH_COUNTER_INFO_W__Anonymous_e__Union(Union):
        pass
    class PDH_COUNTER_INFO_W__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    PDH_COUNTER_INFO_W__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("szMachineName", win32more.Foundation.PWSTR),
        ("szObjectName", win32more.Foundation.PWSTR),
        ("szInstanceName", win32more.Foundation.PWSTR),
        ("szParentInstance", win32more.Foundation.PWSTR),
        ("dwInstanceIndex", UInt32),
        ("szCounterName", win32more.Foundation.PWSTR),
    ]
    PDH_COUNTER_INFO_W__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    PDH_COUNTER_INFO_W__Anonymous_e__Union._fields_ = [
        ("DataItemPath", win32more.System.Performance.PDH_DATA_ITEM_PATH_ELEMENTS_W),
        ("CounterPath", win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_W),
        ("Anonymous", PDH_COUNTER_INFO_W__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    PDH_COUNTER_INFO_W._anonymous_ = [
        'Anonymous',
    ]
    PDH_COUNTER_INFO_W._fields_ = [
        ("dwLength", UInt32),
        ("dwType", UInt32),
        ("CVersion", UInt32),
        ("CStatus", UInt32),
        ("lScale", Int32),
        ("lDefaultScale", Int32),
        ("dwUserData", UIntPtr),
        ("dwQueryUserData", UIntPtr),
        ("szFullPath", win32more.Foundation.PWSTR),
        ("Anonymous", PDH_COUNTER_INFO_W__Anonymous_e__Union),
        ("szExplainText", win32more.Foundation.PWSTR),
        ("DataBuffer", UInt32 * 0),
    ]
    return PDH_COUNTER_INFO_W
def _define_PDH_TIME_INFO_head():
    class PDH_TIME_INFO(Structure):
        pass
    return PDH_TIME_INFO
def _define_PDH_TIME_INFO():
    PDH_TIME_INFO = win32more.System.Performance.PDH_TIME_INFO_head
    PDH_TIME_INFO._fields_ = [
        ("StartTime", Int64),
        ("EndTime", Int64),
        ("SampleCount", UInt32),
    ]
    return PDH_TIME_INFO
def _define_PDH_RAW_LOG_RECORD_head():
    class PDH_RAW_LOG_RECORD(Structure):
        pass
    return PDH_RAW_LOG_RECORD
def _define_PDH_RAW_LOG_RECORD():
    PDH_RAW_LOG_RECORD = win32more.System.Performance.PDH_RAW_LOG_RECORD_head
    PDH_RAW_LOG_RECORD._fields_ = [
        ("dwStructureSize", UInt32),
        ("dwRecordType", win32more.System.Performance.PDH_LOG_TYPE),
        ("dwItems", UInt32),
        ("RawBytes", Byte * 0),
    ]
    return PDH_RAW_LOG_RECORD
def _define_PDH_LOG_SERVICE_QUERY_INFO_A_head():
    class PDH_LOG_SERVICE_QUERY_INFO_A(Structure):
        pass
    return PDH_LOG_SERVICE_QUERY_INFO_A
def _define_PDH_LOG_SERVICE_QUERY_INFO_A():
    PDH_LOG_SERVICE_QUERY_INFO_A = win32more.System.Performance.PDH_LOG_SERVICE_QUERY_INFO_A_head
    class PDH_LOG_SERVICE_QUERY_INFO_A__Anonymous_e__Union(Union):
        pass
    class PDH_LOG_SERVICE_QUERY_INFO_A__Anonymous_e__Union__Anonymous1_e__Struct(Structure):
        pass
    PDH_LOG_SERVICE_QUERY_INFO_A__Anonymous_e__Union__Anonymous1_e__Struct._fields_ = [
        ("PdlAutoNameInterval", UInt32),
        ("PdlAutoNameUnits", UInt32),
        ("PdlCommandFilename", win32more.Foundation.PSTR),
        ("PdlCounterList", win32more.Foundation.PSTR),
        ("PdlAutoNameFormat", UInt32),
        ("PdlSampleInterval", UInt32),
        ("PdlLogStartTime", win32more.Foundation.FILETIME),
        ("PdlLogEndTime", win32more.Foundation.FILETIME),
    ]
    class PDH_LOG_SERVICE_QUERY_INFO_A__Anonymous_e__Union__Anonymous2_e__Struct(Structure):
        pass
    PDH_LOG_SERVICE_QUERY_INFO_A__Anonymous_e__Union__Anonymous2_e__Struct._fields_ = [
        ("TlNumberOfBuffers", UInt32),
        ("TlMinimumBuffers", UInt32),
        ("TlMaximumBuffers", UInt32),
        ("TlFreeBuffers", UInt32),
        ("TlBufferSize", UInt32),
        ("TlEventsLost", UInt32),
        ("TlLoggerThreadId", UInt32),
        ("TlBuffersWritten", UInt32),
        ("TlLogHandle", UInt32),
        ("TlLogFileName", win32more.Foundation.PSTR),
    ]
    PDH_LOG_SERVICE_QUERY_INFO_A__Anonymous_e__Union._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    PDH_LOG_SERVICE_QUERY_INFO_A__Anonymous_e__Union._fields_ = [
        ("Anonymous1", PDH_LOG_SERVICE_QUERY_INFO_A__Anonymous_e__Union__Anonymous1_e__Struct),
        ("Anonymous2", PDH_LOG_SERVICE_QUERY_INFO_A__Anonymous_e__Union__Anonymous2_e__Struct),
    ]
    PDH_LOG_SERVICE_QUERY_INFO_A._anonymous_ = [
        'Anonymous',
    ]
    PDH_LOG_SERVICE_QUERY_INFO_A._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwLogQuota", UInt32),
        ("szLogFileCaption", win32more.Foundation.PSTR),
        ("szDefaultDir", win32more.Foundation.PSTR),
        ("szBaseFileName", win32more.Foundation.PSTR),
        ("dwFileType", UInt32),
        ("dwReserved", UInt32),
        ("Anonymous", PDH_LOG_SERVICE_QUERY_INFO_A__Anonymous_e__Union),
    ]
    return PDH_LOG_SERVICE_QUERY_INFO_A
def _define_PDH_LOG_SERVICE_QUERY_INFO_W_head():
    class PDH_LOG_SERVICE_QUERY_INFO_W(Structure):
        pass
    return PDH_LOG_SERVICE_QUERY_INFO_W
def _define_PDH_LOG_SERVICE_QUERY_INFO_W():
    PDH_LOG_SERVICE_QUERY_INFO_W = win32more.System.Performance.PDH_LOG_SERVICE_QUERY_INFO_W_head
    class PDH_LOG_SERVICE_QUERY_INFO_W__Anonymous_e__Union(Union):
        pass
    class PDH_LOG_SERVICE_QUERY_INFO_W__Anonymous_e__Union__Anonymous1_e__Struct(Structure):
        pass
    PDH_LOG_SERVICE_QUERY_INFO_W__Anonymous_e__Union__Anonymous1_e__Struct._fields_ = [
        ("PdlAutoNameInterval", UInt32),
        ("PdlAutoNameUnits", UInt32),
        ("PdlCommandFilename", win32more.Foundation.PWSTR),
        ("PdlCounterList", win32more.Foundation.PWSTR),
        ("PdlAutoNameFormat", UInt32),
        ("PdlSampleInterval", UInt32),
        ("PdlLogStartTime", win32more.Foundation.FILETIME),
        ("PdlLogEndTime", win32more.Foundation.FILETIME),
    ]
    class PDH_LOG_SERVICE_QUERY_INFO_W__Anonymous_e__Union__Anonymous2_e__Struct(Structure):
        pass
    PDH_LOG_SERVICE_QUERY_INFO_W__Anonymous_e__Union__Anonymous2_e__Struct._fields_ = [
        ("TlNumberOfBuffers", UInt32),
        ("TlMinimumBuffers", UInt32),
        ("TlMaximumBuffers", UInt32),
        ("TlFreeBuffers", UInt32),
        ("TlBufferSize", UInt32),
        ("TlEventsLost", UInt32),
        ("TlLoggerThreadId", UInt32),
        ("TlBuffersWritten", UInt32),
        ("TlLogHandle", UInt32),
        ("TlLogFileName", win32more.Foundation.PWSTR),
    ]
    PDH_LOG_SERVICE_QUERY_INFO_W__Anonymous_e__Union._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    PDH_LOG_SERVICE_QUERY_INFO_W__Anonymous_e__Union._fields_ = [
        ("Anonymous1", PDH_LOG_SERVICE_QUERY_INFO_W__Anonymous_e__Union__Anonymous1_e__Struct),
        ("Anonymous2", PDH_LOG_SERVICE_QUERY_INFO_W__Anonymous_e__Union__Anonymous2_e__Struct),
    ]
    PDH_LOG_SERVICE_QUERY_INFO_W._anonymous_ = [
        'Anonymous',
    ]
    PDH_LOG_SERVICE_QUERY_INFO_W._fields_ = [
        ("dwSize", UInt32),
        ("dwFlags", UInt32),
        ("dwLogQuota", UInt32),
        ("szLogFileCaption", win32more.Foundation.PWSTR),
        ("szDefaultDir", win32more.Foundation.PWSTR),
        ("szBaseFileName", win32more.Foundation.PWSTR),
        ("dwFileType", UInt32),
        ("dwReserved", UInt32),
        ("Anonymous", PDH_LOG_SERVICE_QUERY_INFO_W__Anonymous_e__Union),
    ]
    return PDH_LOG_SERVICE_QUERY_INFO_W
def _define_CounterPathCallBack():
    return CFUNCTYPE(Int32,UIntPtr, use_last_error=False)
def _define_PDH_BROWSE_DLG_CONFIG_HW_head():
    class PDH_BROWSE_DLG_CONFIG_HW(Structure):
        pass
    return PDH_BROWSE_DLG_CONFIG_HW
def _define_PDH_BROWSE_DLG_CONFIG_HW():
    PDH_BROWSE_DLG_CONFIG_HW = win32more.System.Performance.PDH_BROWSE_DLG_CONFIG_HW_head
    PDH_BROWSE_DLG_CONFIG_HW._fields_ = [
        ("_bitfield", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("hDataSource", IntPtr),
        ("szReturnPathBuffer", win32more.Foundation.PWSTR),
        ("cchReturnPathLength", UInt32),
        ("pCallBack", win32more.System.Performance.CounterPathCallBack),
        ("dwCallBackArg", UIntPtr),
        ("CallBackStatus", Int32),
        ("dwDefaultDetailLevel", win32more.System.Performance.PERF_DETAIL),
        ("szDialogBoxCaption", win32more.Foundation.PWSTR),
    ]
    return PDH_BROWSE_DLG_CONFIG_HW
def _define_PDH_BROWSE_DLG_CONFIG_HA_head():
    class PDH_BROWSE_DLG_CONFIG_HA(Structure):
        pass
    return PDH_BROWSE_DLG_CONFIG_HA
def _define_PDH_BROWSE_DLG_CONFIG_HA():
    PDH_BROWSE_DLG_CONFIG_HA = win32more.System.Performance.PDH_BROWSE_DLG_CONFIG_HA_head
    PDH_BROWSE_DLG_CONFIG_HA._fields_ = [
        ("_bitfield", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("hDataSource", IntPtr),
        ("szReturnPathBuffer", win32more.Foundation.PSTR),
        ("cchReturnPathLength", UInt32),
        ("pCallBack", win32more.System.Performance.CounterPathCallBack),
        ("dwCallBackArg", UIntPtr),
        ("CallBackStatus", Int32),
        ("dwDefaultDetailLevel", win32more.System.Performance.PERF_DETAIL),
        ("szDialogBoxCaption", win32more.Foundation.PSTR),
    ]
    return PDH_BROWSE_DLG_CONFIG_HA
def _define_PDH_BROWSE_DLG_CONFIG_W_head():
    class PDH_BROWSE_DLG_CONFIG_W(Structure):
        pass
    return PDH_BROWSE_DLG_CONFIG_W
def _define_PDH_BROWSE_DLG_CONFIG_W():
    PDH_BROWSE_DLG_CONFIG_W = win32more.System.Performance.PDH_BROWSE_DLG_CONFIG_W_head
    PDH_BROWSE_DLG_CONFIG_W._fields_ = [
        ("_bitfield", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("szDataSource", win32more.Foundation.PWSTR),
        ("szReturnPathBuffer", win32more.Foundation.PWSTR),
        ("cchReturnPathLength", UInt32),
        ("pCallBack", win32more.System.Performance.CounterPathCallBack),
        ("dwCallBackArg", UIntPtr),
        ("CallBackStatus", Int32),
        ("dwDefaultDetailLevel", win32more.System.Performance.PERF_DETAIL),
        ("szDialogBoxCaption", win32more.Foundation.PWSTR),
    ]
    return PDH_BROWSE_DLG_CONFIG_W
def _define_PDH_BROWSE_DLG_CONFIG_A_head():
    class PDH_BROWSE_DLG_CONFIG_A(Structure):
        pass
    return PDH_BROWSE_DLG_CONFIG_A
def _define_PDH_BROWSE_DLG_CONFIG_A():
    PDH_BROWSE_DLG_CONFIG_A = win32more.System.Performance.PDH_BROWSE_DLG_CONFIG_A_head
    PDH_BROWSE_DLG_CONFIG_A._fields_ = [
        ("_bitfield", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("szDataSource", win32more.Foundation.PSTR),
        ("szReturnPathBuffer", win32more.Foundation.PSTR),
        ("cchReturnPathLength", UInt32),
        ("pCallBack", win32more.System.Performance.CounterPathCallBack),
        ("dwCallBackArg", UIntPtr),
        ("CallBackStatus", Int32),
        ("dwDefaultDetailLevel", win32more.System.Performance.PERF_DETAIL),
        ("szDialogBoxCaption", win32more.Foundation.PSTR),
    ]
    return PDH_BROWSE_DLG_CONFIG_A
SystemMonitor = Guid('c4d2d8e0-d1dd-11ce-940f-008029004347')
CounterItem = Guid('c4d2d8e0-d1dd-11ce-940f-008029004348')
Counters = Guid('b2b066d2-2aac-11cf-942f-008029004347')
LogFileItem = Guid('16ec5be8-df93-4237-94e4-9ee918111d71')
LogFiles = Guid('2735d9fd-f6b9-4f19-a5d9-e2d068584bc5')
CounterItem2 = Guid('43196c62-c31f-4ce3-a02e-79efe0f6a525')
SystemMonitor2 = Guid('7f30578c-5f38-4612-acfe-6ed04c7b7af8')
AppearPropPage = Guid('e49741e9-93a8-4ab1-8e96-bf4482282e9c')
GeneralPropPage = Guid('c3e5d3d2-1a03-11cf-942d-008029004347')
GraphPropPage = Guid('c3e5d3d3-1a03-11cf-942d-008029004347')
SourcePropPage = Guid('0cf32aa1-7571-11d0-93c4-00aa00a3ddea')
CounterPropPage = Guid('cf948561-ede8-11ce-941e-008029004347')
DisplayTypeConstants = Int32
DisplayTypeConstants_sysmonLineGraph = 1
DisplayTypeConstants_sysmonHistogram = 2
DisplayTypeConstants_sysmonReport = 3
DisplayTypeConstants_sysmonChartArea = 4
DisplayTypeConstants_sysmonChartStackedArea = 5
ReportValueTypeConstants = Int32
ReportValueTypeConstants_sysmonDefaultValue = 0
ReportValueTypeConstants_sysmonCurrentValue = 1
ReportValueTypeConstants_sysmonAverage = 2
ReportValueTypeConstants_sysmonMinimum = 3
ReportValueTypeConstants_sysmonMaximum = 4
DataSourceTypeConstants = Int32
DataSourceTypeConstants_sysmonNullDataSource = -1
DataSourceTypeConstants_sysmonCurrentActivity = 1
DataSourceTypeConstants_sysmonLogFiles = 2
DataSourceTypeConstants_sysmonSqlLog = 3
SysmonFileType = Int32
SysmonFileType_sysmonFileHtml = 1
SysmonFileType_sysmonFileReport = 2
SysmonFileType_sysmonFileCsv = 3
SysmonFileType_sysmonFileTsv = 4
SysmonFileType_sysmonFileBlg = 5
SysmonFileType_sysmonFileRetiredBlg = 6
SysmonFileType_sysmonFileGif = 7
SysmonDataType = Int32
SysmonDataType_sysmonDataAvg = 1
SysmonDataType_sysmonDataMin = 2
SysmonDataType_sysmonDataMax = 3
SysmonDataType_sysmonDataTime = 4
SysmonDataType_sysmonDataCount = 5
SysmonBatchReason = Int32
SysmonBatchReason_sysmonBatchNone = 0
SysmonBatchReason_sysmonBatchAddFiles = 1
SysmonBatchReason_sysmonBatchAddCounters = 2
SysmonBatchReason_sysmonBatchAddFilesAutoCounters = 3
def _define_ICounterItem_head():
    class ICounterItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('771a9520-ee28-11ce-941e-008029004347')
    return ICounterItem
def _define_ICounterItem():
    ICounterItem = win32more.System.Performance.ICounterItem_head
    ICounterItem.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(3, 'get_Value', ((1, 'pdblValue'),)))
    ICounterItem.put_Color = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'put_Color', ((1, 'Color'),)))
    ICounterItem.get_Color = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'get_Color', ((1, 'pColor'),)))
    ICounterItem.put_Width = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(6, 'put_Width', ((1, 'iWidth'),)))
    ICounterItem.get_Width = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Width', ((1, 'piValue'),)))
    ICounterItem.put_LineStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_LineStyle', ((1, 'iLineStyle'),)))
    ICounterItem.get_LineStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_LineStyle', ((1, 'piValue'),)))
    ICounterItem.put_ScaleFactor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_ScaleFactor', ((1, 'iScale'),)))
    ICounterItem.get_ScaleFactor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_ScaleFactor', ((1, 'piValue'),)))
    ICounterItem.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_Path', ((1, 'pstrValue'),)))
    ICounterItem.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),POINTER(Int32), use_last_error=False)(13, 'GetValue', ((1, 'Value'),(1, 'Status'),)))
    ICounterItem.GetStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),POINTER(Double),POINTER(Double),POINTER(Int32), use_last_error=False)(14, 'GetStatistics', ((1, 'Max'),(1, 'Min'),(1, 'Avg'),(1, 'Status'),)))
    win32more.System.Com.IUnknown
    return ICounterItem
def _define_ICounterItem2_head():
    class ICounterItem2(win32more.System.Performance.ICounterItem_head):
        Guid = Guid('eefcd4e1-ea1c-4435-b7f4-e341ba03b4f9')
    return ICounterItem2
def _define_ICounterItem2():
    ICounterItem2 = win32more.System.Performance.ICounterItem2_head
    ICounterItem2.put_Selected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(15, 'put_Selected', ((1, 'bState'),)))
    ICounterItem2.get_Selected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_Selected', ((1, 'pbState'),)))
    ICounterItem2.put_Visible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(17, 'put_Visible', ((1, 'bState'),)))
    ICounterItem2.get_Visible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(18, 'get_Visible', ((1, 'pbState'),)))
    ICounterItem2.GetDataAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Performance.SysmonDataType,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(19, 'GetDataAt', ((1, 'iIndex'),(1, 'iWhich'),(1, 'pVariant'),)))
    win32more.System.Performance.ICounterItem
    return ICounterItem2
def _define__ICounterItemUnion_head():
    class _ICounterItemUnion(win32more.System.Com.IUnknown_head):
        Guid = Guid('de1a6b74-9182-4c41-8e2c-24c2cd30ee83')
    return _ICounterItemUnion
def _define__ICounterItemUnion():
    _ICounterItemUnion = win32more.System.Performance._ICounterItemUnion_head
    _ICounterItemUnion.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(3, 'get_Value', ((1, 'pdblValue'),)))
    _ICounterItemUnion.put_Color = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'put_Color', ((1, 'Color'),)))
    _ICounterItemUnion.get_Color = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'get_Color', ((1, 'pColor'),)))
    _ICounterItemUnion.put_Width = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(6, 'put_Width', ((1, 'iWidth'),)))
    _ICounterItemUnion.get_Width = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Width', ((1, 'piValue'),)))
    _ICounterItemUnion.put_LineStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_LineStyle', ((1, 'iLineStyle'),)))
    _ICounterItemUnion.get_LineStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_LineStyle', ((1, 'piValue'),)))
    _ICounterItemUnion.put_ScaleFactor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_ScaleFactor', ((1, 'iScale'),)))
    _ICounterItemUnion.get_ScaleFactor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'get_ScaleFactor', ((1, 'piValue'),)))
    _ICounterItemUnion.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_Path', ((1, 'pstrValue'),)))
    _ICounterItemUnion.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),POINTER(Int32), use_last_error=False)(13, 'GetValue', ((1, 'Value'),(1, 'Status'),)))
    _ICounterItemUnion.GetStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),POINTER(Double),POINTER(Double),POINTER(Int32), use_last_error=False)(14, 'GetStatistics', ((1, 'Max'),(1, 'Min'),(1, 'Avg'),(1, 'Status'),)))
    _ICounterItemUnion.put_Selected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(15, 'put_Selected', ((1, 'bState'),)))
    _ICounterItemUnion.get_Selected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(16, 'get_Selected', ((1, 'pbState'),)))
    _ICounterItemUnion.put_Visible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(17, 'put_Visible', ((1, 'bState'),)))
    _ICounterItemUnion.get_Visible = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(18, 'get_Visible', ((1, 'pbState'),)))
    _ICounterItemUnion.GetDataAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Performance.SysmonDataType,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(19, 'GetDataAt', ((1, 'iIndex'),(1, 'iWhich'),(1, 'pVariant'),)))
    win32more.System.Com.IUnknown
    return _ICounterItemUnion
def _define_DICounterItem_head():
    class DICounterItem(win32more.System.Com.IDispatch_head):
        Guid = Guid('c08c4ff2-0e2e-11cf-942c-008029004347')
    return DICounterItem
def _define_DICounterItem():
    DICounterItem = win32more.System.Performance.DICounterItem_head
    win32more.System.Com.IDispatch
    return DICounterItem
def _define_ICounters_head():
    class ICounters(win32more.System.Com.IDispatch_head):
        Guid = Guid('79167962-28fc-11cf-942f-008029004347')
    return ICounters
def _define_ICounters():
    ICounters = win32more.System.Performance.ICounters_head
    ICounters.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'pLong'),)))
    ICounters.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'get__NewEnum', ((1, 'ppIunk'),)))
    ICounters.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Performance.DICounterItem_head), use_last_error=False)(9, 'get_Item', ((1, 'index'),(1, 'ppI'),)))
    ICounters.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Performance.DICounterItem_head), use_last_error=False)(10, 'Add', ((1, 'pathname'),(1, 'ppI'),)))
    ICounters.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(11, 'Remove', ((1, 'index'),)))
    win32more.System.Com.IDispatch
    return ICounters
def _define_ILogFileItem_head():
    class ILogFileItem(win32more.System.Com.IUnknown_head):
        Guid = Guid('d6b518dd-05c7-418a-89e6-4f9ce8c6841e')
    return ILogFileItem
def _define_ILogFileItem():
    ILogFileItem = win32more.System.Performance.ILogFileItem_head
    ILogFileItem.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_Path', ((1, 'pstrValue'),)))
    win32more.System.Com.IUnknown
    return ILogFileItem
def _define_DILogFileItem_head():
    class DILogFileItem(win32more.System.Com.IDispatch_head):
        Guid = Guid('8d093ffc-f777-4917-82d1-833fbc54c58f')
    return DILogFileItem
def _define_DILogFileItem():
    DILogFileItem = win32more.System.Performance.DILogFileItem_head
    win32more.System.Com.IDispatch
    return DILogFileItem
def _define_ILogFiles_head():
    class ILogFiles(win32more.System.Com.IDispatch_head):
        Guid = Guid('6a2a97e6-6851-41ea-87ad-2a8225335865')
    return ILogFiles
def _define_ILogFiles():
    ILogFiles = win32more.System.Performance.ILogFiles_head
    ILogFiles.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Count', ((1, 'pLong'),)))
    ILogFiles.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(8, 'get__NewEnum', ((1, 'ppIunk'),)))
    ILogFiles.get_Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Performance.DILogFileItem_head), use_last_error=False)(9, 'get_Item', ((1, 'index'),(1, 'ppI'),)))
    ILogFiles.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Performance.DILogFileItem_head), use_last_error=False)(10, 'Add', ((1, 'pathname'),(1, 'ppI'),)))
    ILogFiles.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT, use_last_error=False)(11, 'Remove', ((1, 'index'),)))
    win32more.System.Com.IDispatch
    return ILogFiles
def _define_ISystemMonitor_head():
    class ISystemMonitor(win32more.System.Com.IUnknown_head):
        Guid = Guid('194eb241-c32c-11cf-9398-00aa00a3ddea')
    return ISystemMonitor
def _define_ISystemMonitor():
    ISystemMonitor = win32more.System.Performance.ISystemMonitor_head
    ISystemMonitor.get_Appearance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'get_Appearance', ((1, 'iAppearance'),)))
    ISystemMonitor.put_Appearance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(4, 'put_Appearance', ((1, 'iAppearance'),)))
    ISystemMonitor.get_BackColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'get_BackColor', ((1, 'pColor'),)))
    ISystemMonitor.put_BackColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'put_BackColor', ((1, 'Color'),)))
    ISystemMonitor.get_BorderStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_BorderStyle', ((1, 'iBorderStyle'),)))
    ISystemMonitor.put_BorderStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_BorderStyle', ((1, 'iBorderStyle'),)))
    ISystemMonitor.get_ForeColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'get_ForeColor', ((1, 'pColor'),)))
    ISystemMonitor.put_ForeColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'put_ForeColor', ((1, 'Color'),)))
    ISystemMonitor.get_Font = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IFontDisp_head), use_last_error=False)(11, 'get_Font', ((1, 'ppFont'),)))
    ISystemMonitor.putref_Font = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IFontDisp_head, use_last_error=False)(12, 'putref_Font', ((1, 'pFont'),)))
    ISystemMonitor.get_Counters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.ICounters_head), use_last_error=False)(13, 'get_Counters', ((1, 'ppICounters'),)))
    ISystemMonitor.put_ShowVerticalGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(14, 'put_ShowVerticalGrid', ((1, 'bState'),)))
    ISystemMonitor.get_ShowVerticalGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_ShowVerticalGrid', ((1, 'pbState'),)))
    ISystemMonitor.put_ShowHorizontalGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(16, 'put_ShowHorizontalGrid', ((1, 'bState'),)))
    ISystemMonitor.get_ShowHorizontalGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(17, 'get_ShowHorizontalGrid', ((1, 'pbState'),)))
    ISystemMonitor.put_ShowLegend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(18, 'put_ShowLegend', ((1, 'bState'),)))
    ISystemMonitor.get_ShowLegend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(19, 'get_ShowLegend', ((1, 'pbState'),)))
    ISystemMonitor.put_ShowScaleLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(20, 'put_ShowScaleLabels', ((1, 'bState'),)))
    ISystemMonitor.get_ShowScaleLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(21, 'get_ShowScaleLabels', ((1, 'pbState'),)))
    ISystemMonitor.put_ShowValueBar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(22, 'put_ShowValueBar', ((1, 'bState'),)))
    ISystemMonitor.get_ShowValueBar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(23, 'get_ShowValueBar', ((1, 'pbState'),)))
    ISystemMonitor.put_MaximumScale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_MaximumScale', ((1, 'iValue'),)))
    ISystemMonitor.get_MaximumScale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(25, 'get_MaximumScale', ((1, 'piValue'),)))
    ISystemMonitor.put_MinimumScale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(26, 'put_MinimumScale', ((1, 'iValue'),)))
    ISystemMonitor.get_MinimumScale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(27, 'get_MinimumScale', ((1, 'piValue'),)))
    ISystemMonitor.put_UpdateInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(28, 'put_UpdateInterval', ((1, 'fValue'),)))
    ISystemMonitor.get_UpdateInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(29, 'get_UpdateInterval', ((1, 'pfValue'),)))
    ISystemMonitor.put_DisplayType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.DisplayTypeConstants, use_last_error=False)(30, 'put_DisplayType', ((1, 'eDisplayType'),)))
    ISystemMonitor.get_DisplayType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.DisplayTypeConstants), use_last_error=False)(31, 'get_DisplayType', ((1, 'peDisplayType'),)))
    ISystemMonitor.put_ManualUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(32, 'put_ManualUpdate', ((1, 'bState'),)))
    ISystemMonitor.get_ManualUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(33, 'get_ManualUpdate', ((1, 'pbState'),)))
    ISystemMonitor.put_GraphTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(34, 'put_GraphTitle', ((1, 'bsTitle'),)))
    ISystemMonitor.get_GraphTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(35, 'get_GraphTitle', ((1, 'pbsTitle'),)))
    ISystemMonitor.put_YAxisLabel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(36, 'put_YAxisLabel', ((1, 'bsTitle'),)))
    ISystemMonitor.get_YAxisLabel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(37, 'get_YAxisLabel', ((1, 'pbsTitle'),)))
    ISystemMonitor.CollectSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(38, 'CollectSample', ()))
    ISystemMonitor.UpdateGraph = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(39, 'UpdateGraph', ()))
    ISystemMonitor.BrowseCounters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(40, 'BrowseCounters', ()))
    ISystemMonitor.DisplayProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(41, 'DisplayProperties', ()))
    ISystemMonitor.Counter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Performance.ICounterItem_head), use_last_error=False)(42, 'Counter', ((1, 'iIndex'),(1, 'ppICounter'),)))
    ISystemMonitor.AddCounter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Performance.ICounterItem_head), use_last_error=False)(43, 'AddCounter', ((1, 'bsPath'),(1, 'ppICounter'),)))
    ISystemMonitor.DeleteCounter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.ICounterItem_head, use_last_error=False)(44, 'DeleteCounter', ((1, 'pCtr'),)))
    ISystemMonitor.get_BackColorCtl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(45, 'get_BackColorCtl', ((1, 'pColor'),)))
    ISystemMonitor.put_BackColorCtl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(46, 'put_BackColorCtl', ((1, 'Color'),)))
    ISystemMonitor.put_LogFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(47, 'put_LogFileName', ((1, 'bsFileName'),)))
    ISystemMonitor.get_LogFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(48, 'get_LogFileName', ((1, 'bsFileName'),)))
    ISystemMonitor.put_LogViewStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(49, 'put_LogViewStart', ((1, 'StartTime'),)))
    ISystemMonitor.get_LogViewStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(50, 'get_LogViewStart', ((1, 'StartTime'),)))
    ISystemMonitor.put_LogViewStop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(51, 'put_LogViewStop', ((1, 'StopTime'),)))
    ISystemMonitor.get_LogViewStop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(52, 'get_LogViewStop', ((1, 'StopTime'),)))
    ISystemMonitor.get_GridColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(53, 'get_GridColor', ((1, 'pColor'),)))
    ISystemMonitor.put_GridColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(54, 'put_GridColor', ((1, 'Color'),)))
    ISystemMonitor.get_TimeBarColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(55, 'get_TimeBarColor', ((1, 'pColor'),)))
    ISystemMonitor.put_TimeBarColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(56, 'put_TimeBarColor', ((1, 'Color'),)))
    ISystemMonitor.get_Highlight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(57, 'get_Highlight', ((1, 'pbState'),)))
    ISystemMonitor.put_Highlight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(58, 'put_Highlight', ((1, 'bState'),)))
    ISystemMonitor.get_ShowToolbar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(59, 'get_ShowToolbar', ((1, 'pbState'),)))
    ISystemMonitor.put_ShowToolbar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(60, 'put_ShowToolbar', ((1, 'bState'),)))
    ISystemMonitor.Paste = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(61, 'Paste', ()))
    ISystemMonitor.Copy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(62, 'Copy', ()))
    ISystemMonitor.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(63, 'Reset', ()))
    ISystemMonitor.put_ReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(64, 'put_ReadOnly', ((1, 'bState'),)))
    ISystemMonitor.get_ReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(65, 'get_ReadOnly', ((1, 'pbState'),)))
    ISystemMonitor.put_ReportValueType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.ReportValueTypeConstants, use_last_error=False)(66, 'put_ReportValueType', ((1, 'eReportValueType'),)))
    ISystemMonitor.get_ReportValueType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.ReportValueTypeConstants), use_last_error=False)(67, 'get_ReportValueType', ((1, 'peReportValueType'),)))
    ISystemMonitor.put_MonitorDuplicateInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(68, 'put_MonitorDuplicateInstances', ((1, 'bState'),)))
    ISystemMonitor.get_MonitorDuplicateInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(69, 'get_MonitorDuplicateInstances', ((1, 'pbState'),)))
    ISystemMonitor.put_DisplayFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(70, 'put_DisplayFilter', ((1, 'iValue'),)))
    ISystemMonitor.get_DisplayFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(71, 'get_DisplayFilter', ((1, 'piValue'),)))
    ISystemMonitor.get_LogFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.ILogFiles_head), use_last_error=False)(72, 'get_LogFiles', ((1, 'ppILogFiles'),)))
    ISystemMonitor.put_DataSourceType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.DataSourceTypeConstants, use_last_error=False)(73, 'put_DataSourceType', ((1, 'eDataSourceType'),)))
    ISystemMonitor.get_DataSourceType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.DataSourceTypeConstants), use_last_error=False)(74, 'get_DataSourceType', ((1, 'peDataSourceType'),)))
    ISystemMonitor.put_SqlDsnName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(75, 'put_SqlDsnName', ((1, 'bsSqlDsnName'),)))
    ISystemMonitor.get_SqlDsnName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(76, 'get_SqlDsnName', ((1, 'bsSqlDsnName'),)))
    ISystemMonitor.put_SqlLogSetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(77, 'put_SqlLogSetName', ((1, 'bsSqlLogSetName'),)))
    ISystemMonitor.get_SqlLogSetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(78, 'get_SqlLogSetName', ((1, 'bsSqlLogSetName'),)))
    win32more.System.Com.IUnknown
    return ISystemMonitor
def _define_ISystemMonitor2_head():
    class ISystemMonitor2(win32more.System.Performance.ISystemMonitor_head):
        Guid = Guid('08e3206a-5fd2-4fde-a8a5-8cb3b63d2677')
    return ISystemMonitor2
def _define_ISystemMonitor2():
    ISystemMonitor2 = win32more.System.Performance.ISystemMonitor2_head
    ISystemMonitor2.put_EnableDigitGrouping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(79, 'put_EnableDigitGrouping', ((1, 'bState'),)))
    ISystemMonitor2.get_EnableDigitGrouping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(80, 'get_EnableDigitGrouping', ((1, 'pbState'),)))
    ISystemMonitor2.put_EnableToolTips = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(81, 'put_EnableToolTips', ((1, 'bState'),)))
    ISystemMonitor2.get_EnableToolTips = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(82, 'get_EnableToolTips', ((1, 'pbState'),)))
    ISystemMonitor2.put_ShowTimeAxisLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(83, 'put_ShowTimeAxisLabels', ((1, 'bState'),)))
    ISystemMonitor2.get_ShowTimeAxisLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(84, 'get_ShowTimeAxisLabels', ((1, 'pbState'),)))
    ISystemMonitor2.put_ChartScroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(85, 'put_ChartScroll', ((1, 'bScroll'),)))
    ISystemMonitor2.get_ChartScroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(86, 'get_ChartScroll', ((1, 'pbScroll'),)))
    ISystemMonitor2.put_DataPointCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(87, 'put_DataPointCount', ((1, 'iNewCount'),)))
    ISystemMonitor2.get_DataPointCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(88, 'get_DataPointCount', ((1, 'piDataPointCount'),)))
    ISystemMonitor2.ScaleToFit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(89, 'ScaleToFit', ((1, 'bSelectedCountersOnly'),)))
    ISystemMonitor2.SaveAs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Performance.SysmonFileType, use_last_error=False)(90, 'SaveAs', ((1, 'bstrFileName'),(1, 'eSysmonFileType'),)))
    ISystemMonitor2.Relog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Performance.SysmonFileType,Int32, use_last_error=False)(91, 'Relog', ((1, 'bstrFileName'),(1, 'eSysmonFileType'),(1, 'iFilter'),)))
    ISystemMonitor2.ClearData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(92, 'ClearData', ()))
    ISystemMonitor2.get_LogSourceStartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(93, 'get_LogSourceStartTime', ((1, 'pDate'),)))
    ISystemMonitor2.get_LogSourceStopTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(94, 'get_LogSourceStopTime', ((1, 'pDate'),)))
    ISystemMonitor2.SetLogViewRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double, use_last_error=False)(95, 'SetLogViewRange', ((1, 'StartTime'),(1, 'StopTime'),)))
    ISystemMonitor2.GetLogViewRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),POINTER(Double), use_last_error=False)(96, 'GetLogViewRange', ((1, 'StartTime'),(1, 'StopTime'),)))
    ISystemMonitor2.BatchingLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.System.Performance.SysmonBatchReason, use_last_error=False)(97, 'BatchingLock', ((1, 'fLock'),(1, 'eBatchReason'),)))
    ISystemMonitor2.LoadSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(98, 'LoadSettings', ((1, 'bstrSettingFileName'),)))
    win32more.System.Performance.ISystemMonitor
    return ISystemMonitor2
def _define__ISystemMonitorUnion_head():
    class _ISystemMonitorUnion(win32more.System.Com.IUnknown_head):
        Guid = Guid('c8a77338-265f-4de5-aa25-c7da1ce5a8f4')
    return _ISystemMonitorUnion
def _define__ISystemMonitorUnion():
    _ISystemMonitorUnion = win32more.System.Performance._ISystemMonitorUnion_head
    _ISystemMonitorUnion.get_Appearance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'get_Appearance', ((1, 'iAppearance'),)))
    _ISystemMonitorUnion.put_Appearance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(4, 'put_Appearance', ((1, 'iAppearance'),)))
    _ISystemMonitorUnion.get_BackColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'get_BackColor', ((1, 'pColor'),)))
    _ISystemMonitorUnion.put_BackColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'put_BackColor', ((1, 'Color'),)))
    _ISystemMonitorUnion.get_BorderStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_BorderStyle', ((1, 'iBorderStyle'),)))
    _ISystemMonitorUnion.put_BorderStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'put_BorderStyle', ((1, 'iBorderStyle'),)))
    _ISystemMonitorUnion.get_ForeColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'get_ForeColor', ((1, 'pColor'),)))
    _ISystemMonitorUnion.put_ForeColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'put_ForeColor', ((1, 'Color'),)))
    _ISystemMonitorUnion.get_Font = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IFontDisp_head), use_last_error=False)(11, 'get_Font', ((1, 'ppFont'),)))
    _ISystemMonitorUnion.putref_Font = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IFontDisp_head, use_last_error=False)(12, 'putref_Font', ((1, 'pFont'),)))
    _ISystemMonitorUnion.get_Counters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.ICounters_head), use_last_error=False)(13, 'get_Counters', ((1, 'ppICounters'),)))
    _ISystemMonitorUnion.put_ShowVerticalGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(14, 'put_ShowVerticalGrid', ((1, 'bState'),)))
    _ISystemMonitorUnion.get_ShowVerticalGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_ShowVerticalGrid', ((1, 'pbState'),)))
    _ISystemMonitorUnion.put_ShowHorizontalGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(16, 'put_ShowHorizontalGrid', ((1, 'bState'),)))
    _ISystemMonitorUnion.get_ShowHorizontalGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(17, 'get_ShowHorizontalGrid', ((1, 'pbState'),)))
    _ISystemMonitorUnion.put_ShowLegend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(18, 'put_ShowLegend', ((1, 'bState'),)))
    _ISystemMonitorUnion.get_ShowLegend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(19, 'get_ShowLegend', ((1, 'pbState'),)))
    _ISystemMonitorUnion.put_ShowScaleLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(20, 'put_ShowScaleLabels', ((1, 'bState'),)))
    _ISystemMonitorUnion.get_ShowScaleLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(21, 'get_ShowScaleLabels', ((1, 'pbState'),)))
    _ISystemMonitorUnion.put_ShowValueBar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(22, 'put_ShowValueBar', ((1, 'bState'),)))
    _ISystemMonitorUnion.get_ShowValueBar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(23, 'get_ShowValueBar', ((1, 'pbState'),)))
    _ISystemMonitorUnion.put_MaximumScale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'put_MaximumScale', ((1, 'iValue'),)))
    _ISystemMonitorUnion.get_MaximumScale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(25, 'get_MaximumScale', ((1, 'piValue'),)))
    _ISystemMonitorUnion.put_MinimumScale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(26, 'put_MinimumScale', ((1, 'iValue'),)))
    _ISystemMonitorUnion.get_MinimumScale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(27, 'get_MinimumScale', ((1, 'piValue'),)))
    _ISystemMonitorUnion.put_UpdateInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(28, 'put_UpdateInterval', ((1, 'fValue'),)))
    _ISystemMonitorUnion.get_UpdateInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(29, 'get_UpdateInterval', ((1, 'pfValue'),)))
    _ISystemMonitorUnion.put_DisplayType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.DisplayTypeConstants, use_last_error=False)(30, 'put_DisplayType', ((1, 'eDisplayType'),)))
    _ISystemMonitorUnion.get_DisplayType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.DisplayTypeConstants), use_last_error=False)(31, 'get_DisplayType', ((1, 'peDisplayType'),)))
    _ISystemMonitorUnion.put_ManualUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(32, 'put_ManualUpdate', ((1, 'bState'),)))
    _ISystemMonitorUnion.get_ManualUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(33, 'get_ManualUpdate', ((1, 'pbState'),)))
    _ISystemMonitorUnion.put_GraphTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(34, 'put_GraphTitle', ((1, 'bsTitle'),)))
    _ISystemMonitorUnion.get_GraphTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(35, 'get_GraphTitle', ((1, 'pbsTitle'),)))
    _ISystemMonitorUnion.put_YAxisLabel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(36, 'put_YAxisLabel', ((1, 'bsTitle'),)))
    _ISystemMonitorUnion.get_YAxisLabel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(37, 'get_YAxisLabel', ((1, 'pbsTitle'),)))
    _ISystemMonitorUnion.CollectSample = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(38, 'CollectSample', ()))
    _ISystemMonitorUnion.UpdateGraph = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(39, 'UpdateGraph', ()))
    _ISystemMonitorUnion.BrowseCounters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(40, 'BrowseCounters', ()))
    _ISystemMonitorUnion.DisplayProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(41, 'DisplayProperties', ()))
    _ISystemMonitorUnion.Counter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Performance.ICounterItem_head), use_last_error=False)(42, 'Counter', ((1, 'iIndex'),(1, 'ppICounter'),)))
    _ISystemMonitorUnion.AddCounter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Performance.ICounterItem_head), use_last_error=False)(43, 'AddCounter', ((1, 'bsPath'),(1, 'ppICounter'),)))
    _ISystemMonitorUnion.DeleteCounter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.ICounterItem_head, use_last_error=False)(44, 'DeleteCounter', ((1, 'pCtr'),)))
    _ISystemMonitorUnion.get_BackColorCtl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(45, 'get_BackColorCtl', ((1, 'pColor'),)))
    _ISystemMonitorUnion.put_BackColorCtl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(46, 'put_BackColorCtl', ((1, 'Color'),)))
    _ISystemMonitorUnion.put_LogFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(47, 'put_LogFileName', ((1, 'bsFileName'),)))
    _ISystemMonitorUnion.get_LogFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(48, 'get_LogFileName', ((1, 'bsFileName'),)))
    _ISystemMonitorUnion.put_LogViewStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(49, 'put_LogViewStart', ((1, 'StartTime'),)))
    _ISystemMonitorUnion.get_LogViewStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(50, 'get_LogViewStart', ((1, 'StartTime'),)))
    _ISystemMonitorUnion.put_LogViewStop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double, use_last_error=False)(51, 'put_LogViewStop', ((1, 'StopTime'),)))
    _ISystemMonitorUnion.get_LogViewStop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(52, 'get_LogViewStop', ((1, 'StopTime'),)))
    _ISystemMonitorUnion.get_GridColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(53, 'get_GridColor', ((1, 'pColor'),)))
    _ISystemMonitorUnion.put_GridColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(54, 'put_GridColor', ((1, 'Color'),)))
    _ISystemMonitorUnion.get_TimeBarColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(55, 'get_TimeBarColor', ((1, 'pColor'),)))
    _ISystemMonitorUnion.put_TimeBarColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(56, 'put_TimeBarColor', ((1, 'Color'),)))
    _ISystemMonitorUnion.get_Highlight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(57, 'get_Highlight', ((1, 'pbState'),)))
    _ISystemMonitorUnion.put_Highlight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(58, 'put_Highlight', ((1, 'bState'),)))
    _ISystemMonitorUnion.get_ShowToolbar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(59, 'get_ShowToolbar', ((1, 'pbState'),)))
    _ISystemMonitorUnion.put_ShowToolbar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(60, 'put_ShowToolbar', ((1, 'bState'),)))
    _ISystemMonitorUnion.Paste = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(61, 'Paste', ()))
    _ISystemMonitorUnion.Copy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(62, 'Copy', ()))
    _ISystemMonitorUnion.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(63, 'Reset', ()))
    _ISystemMonitorUnion.put_ReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(64, 'put_ReadOnly', ((1, 'bState'),)))
    _ISystemMonitorUnion.get_ReadOnly = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(65, 'get_ReadOnly', ((1, 'pbState'),)))
    _ISystemMonitorUnion.put_ReportValueType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.ReportValueTypeConstants, use_last_error=False)(66, 'put_ReportValueType', ((1, 'eReportValueType'),)))
    _ISystemMonitorUnion.get_ReportValueType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.ReportValueTypeConstants), use_last_error=False)(67, 'get_ReportValueType', ((1, 'peReportValueType'),)))
    _ISystemMonitorUnion.put_MonitorDuplicateInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(68, 'put_MonitorDuplicateInstances', ((1, 'bState'),)))
    _ISystemMonitorUnion.get_MonitorDuplicateInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(69, 'get_MonitorDuplicateInstances', ((1, 'pbState'),)))
    _ISystemMonitorUnion.put_DisplayFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(70, 'put_DisplayFilter', ((1, 'iValue'),)))
    _ISystemMonitorUnion.get_DisplayFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(71, 'get_DisplayFilter', ((1, 'piValue'),)))
    _ISystemMonitorUnion.get_LogFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.ILogFiles_head), use_last_error=False)(72, 'get_LogFiles', ((1, 'ppILogFiles'),)))
    _ISystemMonitorUnion.put_DataSourceType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Performance.DataSourceTypeConstants, use_last_error=False)(73, 'put_DataSourceType', ((1, 'eDataSourceType'),)))
    _ISystemMonitorUnion.get_DataSourceType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Performance.DataSourceTypeConstants), use_last_error=False)(74, 'get_DataSourceType', ((1, 'peDataSourceType'),)))
    _ISystemMonitorUnion.put_SqlDsnName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(75, 'put_SqlDsnName', ((1, 'bsSqlDsnName'),)))
    _ISystemMonitorUnion.get_SqlDsnName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(76, 'get_SqlDsnName', ((1, 'bsSqlDsnName'),)))
    _ISystemMonitorUnion.put_SqlLogSetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(77, 'put_SqlLogSetName', ((1, 'bsSqlLogSetName'),)))
    _ISystemMonitorUnion.get_SqlLogSetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(78, 'get_SqlLogSetName', ((1, 'bsSqlLogSetName'),)))
    _ISystemMonitorUnion.put_EnableDigitGrouping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(79, 'put_EnableDigitGrouping', ((1, 'bState'),)))
    _ISystemMonitorUnion.get_EnableDigitGrouping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(80, 'get_EnableDigitGrouping', ((1, 'pbState'),)))
    _ISystemMonitorUnion.put_EnableToolTips = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(81, 'put_EnableToolTips', ((1, 'bState'),)))
    _ISystemMonitorUnion.get_EnableToolTips = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(82, 'get_EnableToolTips', ((1, 'pbState'),)))
    _ISystemMonitorUnion.put_ShowTimeAxisLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(83, 'put_ShowTimeAxisLabels', ((1, 'bState'),)))
    _ISystemMonitorUnion.get_ShowTimeAxisLabels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(84, 'get_ShowTimeAxisLabels', ((1, 'pbState'),)))
    _ISystemMonitorUnion.put_ChartScroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(85, 'put_ChartScroll', ((1, 'bScroll'),)))
    _ISystemMonitorUnion.get_ChartScroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(86, 'get_ChartScroll', ((1, 'pbScroll'),)))
    _ISystemMonitorUnion.put_DataPointCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(87, 'put_DataPointCount', ((1, 'iNewCount'),)))
    _ISystemMonitorUnion.get_DataPointCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(88, 'get_DataPointCount', ((1, 'piDataPointCount'),)))
    _ISystemMonitorUnion.ScaleToFit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(89, 'ScaleToFit', ((1, 'bSelectedCountersOnly'),)))
    _ISystemMonitorUnion.SaveAs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Performance.SysmonFileType, use_last_error=False)(90, 'SaveAs', ((1, 'bstrFileName'),(1, 'eSysmonFileType'),)))
    _ISystemMonitorUnion.Relog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Performance.SysmonFileType,Int32, use_last_error=False)(91, 'Relog', ((1, 'bstrFileName'),(1, 'eSysmonFileType'),(1, 'iFilter'),)))
    _ISystemMonitorUnion.ClearData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(92, 'ClearData', ()))
    _ISystemMonitorUnion.get_LogSourceStartTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(93, 'get_LogSourceStartTime', ((1, 'pDate'),)))
    _ISystemMonitorUnion.get_LogSourceStopTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(94, 'get_LogSourceStopTime', ((1, 'pDate'),)))
    _ISystemMonitorUnion.SetLogViewRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double, use_last_error=False)(95, 'SetLogViewRange', ((1, 'StartTime'),(1, 'StopTime'),)))
    _ISystemMonitorUnion.GetLogViewRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),POINTER(Double), use_last_error=False)(96, 'GetLogViewRange', ((1, 'StartTime'),(1, 'StopTime'),)))
    _ISystemMonitorUnion.BatchingLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.System.Performance.SysmonBatchReason, use_last_error=False)(97, 'BatchingLock', ((1, 'fLock'),(1, 'eBatchReason'),)))
    _ISystemMonitorUnion.LoadSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(98, 'LoadSettings', ((1, 'bstrSettingFileName'),)))
    win32more.System.Com.IUnknown
    return _ISystemMonitorUnion
def _define_DISystemMonitor_head():
    class DISystemMonitor(win32more.System.Com.IDispatch_head):
        Guid = Guid('13d73d81-c32e-11cf-9398-00aa00a3ddea')
    return DISystemMonitor
def _define_DISystemMonitor():
    DISystemMonitor = win32more.System.Performance.DISystemMonitor_head
    win32more.System.Com.IDispatch
    return DISystemMonitor
def _define_DISystemMonitorInternal_head():
    class DISystemMonitorInternal(win32more.System.Com.IDispatch_head):
        Guid = Guid('194eb242-c32c-11cf-9398-00aa00a3ddea')
    return DISystemMonitorInternal
def _define_DISystemMonitorInternal():
    DISystemMonitorInternal = win32more.System.Performance.DISystemMonitorInternal_head
    win32more.System.Com.IDispatch
    return DISystemMonitorInternal
def _define_ISystemMonitorEvents_head():
    class ISystemMonitorEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('ee660ea0-4abd-11cf-943a-008029004347')
    return ISystemMonitorEvents
def _define_ISystemMonitorEvents():
    ISystemMonitorEvents = win32more.System.Performance.ISystemMonitorEvents_head
    ISystemMonitorEvents.OnCounterSelected = COMMETHOD(WINFUNCTYPE(Void,Int32, use_last_error=False)(3, 'OnCounterSelected', ((1, 'Index'),)))
    ISystemMonitorEvents.OnCounterAdded = COMMETHOD(WINFUNCTYPE(Void,Int32, use_last_error=False)(4, 'OnCounterAdded', ((1, 'Index'),)))
    ISystemMonitorEvents.OnCounterDeleted = COMMETHOD(WINFUNCTYPE(Void,Int32, use_last_error=False)(5, 'OnCounterDeleted', ((1, 'Index'),)))
    ISystemMonitorEvents.OnSampleCollected = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(6, 'OnSampleCollected', ()))
    ISystemMonitorEvents.OnDblClick = COMMETHOD(WINFUNCTYPE(Void,Int32, use_last_error=False)(7, 'OnDblClick', ((1, 'Index'),)))
    win32more.System.Com.IUnknown
    return ISystemMonitorEvents
def _define_DISystemMonitorEvents_head():
    class DISystemMonitorEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('84979930-4ab3-11cf-943a-008029004347')
    return DISystemMonitorEvents
def _define_DISystemMonitorEvents():
    DISystemMonitorEvents = win32more.System.Performance.DISystemMonitorEvents_head
    win32more.System.Com.IDispatch
    return DISystemMonitorEvents
def _define_QueryPerformanceCounter():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.LARGE_INTEGER_head), use_last_error=True)(("QueryPerformanceCounter", windll["KERNEL32"]), ((1, 'lpPerformanceCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryPerformanceFrequency():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.LARGE_INTEGER_head), use_last_error=True)(("QueryPerformanceFrequency", windll["KERNEL32"]), ((1, 'lpFrequency'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InstallPerfDllW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UIntPtr, use_last_error=False)(("InstallPerfDllW", windll["loadperf"]), ((1, 'szComputerName'),(1, 'lpIniFile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InstallPerfDll():
    return win32more.System.Performance.InstallPerfDllW
def _define_InstallPerfDllA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UIntPtr, use_last_error=False)(("InstallPerfDllA", windll["loadperf"]), ((1, 'szComputerName'),(1, 'lpIniFile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadPerfCounterTextStringsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.BOOL, use_last_error=False)(("LoadPerfCounterTextStringsA", windll["loadperf"]), ((1, 'lpCommandLine'),(1, 'bQuietModeArg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadPerfCounterTextStringsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("LoadPerfCounterTextStringsW", windll["loadperf"]), ((1, 'lpCommandLine'),(1, 'bQuietModeArg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadPerfCounterTextStrings():
    return win32more.System.Performance.LoadPerfCounterTextStringsW
def _define_UnloadPerfCounterTextStringsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("UnloadPerfCounterTextStringsW", windll["loadperf"]), ((1, 'lpCommandLine'),(1, 'bQuietModeArg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnloadPerfCounterTextStrings():
    return win32more.System.Performance.UnloadPerfCounterTextStringsW
def _define_UnloadPerfCounterTextStringsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.BOOL, use_last_error=False)(("UnloadPerfCounterTextStringsA", windll["loadperf"]), ((1, 'lpCommandLine'),(1, 'bQuietModeArg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdatePerfNameFilesA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UIntPtr, use_last_error=False)(("UpdatePerfNameFilesA", windll["loadperf"]), ((1, 'szNewCtrFilePath'),(1, 'szNewHlpFilePath'),(1, 'szLanguageID'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdatePerfNameFilesW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UIntPtr, use_last_error=False)(("UpdatePerfNameFilesW", windll["loadperf"]), ((1, 'szNewCtrFilePath'),(1, 'szNewHlpFilePath'),(1, 'szLanguageID'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdatePerfNameFiles():
    return win32more.System.Performance.UpdatePerfNameFilesW
def _define_SetServiceAsTrustedA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("SetServiceAsTrustedA", windll["loadperf"]), ((1, 'szReserved'),(1, 'szServiceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetServiceAsTrustedW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("SetServiceAsTrustedW", windll["loadperf"]), ((1, 'szReserved'),(1, 'szServiceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetServiceAsTrusted():
    return win32more.System.Performance.SetServiceAsTrustedW
def _define_BackupPerfRegistryToFileW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("BackupPerfRegistryToFileW", windll["loadperf"]), ((1, 'szFileName'),(1, 'szCommentString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RestorePerfRegistryFromFileW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("RestorePerfRegistryFromFileW", windll["loadperf"]), ((1, 'szFileName'),(1, 'szLangId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfStartProvider():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),win32more.System.Performance.PERFLIBREQUEST,POINTER(win32more.System.Performance.PerfProviderHandle), use_last_error=False)(("PerfStartProvider", windll["ADVAPI32"]), ((1, 'ProviderGuid'),(1, 'ControlCallback'),(1, 'phProvider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfStartProviderEx():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),POINTER(win32more.System.Performance.PERF_PROVIDER_CONTEXT_head),POINTER(win32more.System.Performance.PerfProviderHandle), use_last_error=False)(("PerfStartProviderEx", windll["ADVAPI32"]), ((1, 'ProviderGuid'),(1, 'ProviderContext'),(1, 'Provider'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfStopProvider():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Performance.PerfProviderHandle, use_last_error=False)(("PerfStopProvider", windll["ADVAPI32"]), ((1, 'ProviderHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfSetCounterSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.System.Performance.PERF_COUNTERSET_INFO_head),UInt32, use_last_error=False)(("PerfSetCounterSetInfo", windll["ADVAPI32"]), ((1, 'ProviderHandle'),(1, 'Template'),(1, 'TemplateSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfCreateInstance():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head),win32more.System.Performance.PerfProviderHandle,POINTER(Guid),win32more.Foundation.PWSTR,UInt32, use_last_error=True)(("PerfCreateInstance", windll["ADVAPI32"]), ((1, 'ProviderHandle'),(1, 'CounterSetGuid'),(1, 'Name'),(1, 'Id'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfDeleteInstance():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Performance.PerfProviderHandle,POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head), use_last_error=False)(("PerfDeleteInstance", windll["ADVAPI32"]), ((1, 'Provider'),(1, 'InstanceBlock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfQueryInstance():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head),win32more.Foundation.HANDLE,POINTER(Guid),win32more.Foundation.PWSTR,UInt32, use_last_error=True)(("PerfQueryInstance", windll["ADVAPI32"]), ((1, 'ProviderHandle'),(1, 'CounterSetGuid'),(1, 'Name'),(1, 'Id'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfSetCounterRefValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head),UInt32,c_void_p, use_last_error=False)(("PerfSetCounterRefValue", windll["ADVAPI32"]), ((1, 'Provider'),(1, 'Instance'),(1, 'CounterId'),(1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfSetULongCounterValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head),UInt32,UInt32, use_last_error=False)(("PerfSetULongCounterValue", windll["ADVAPI32"]), ((1, 'Provider'),(1, 'Instance'),(1, 'CounterId'),(1, 'Value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfSetULongLongCounterValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head),UInt32,UInt64, use_last_error=False)(("PerfSetULongLongCounterValue", windll["ADVAPI32"]), ((1, 'Provider'),(1, 'Instance'),(1, 'CounterId'),(1, 'Value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfIncrementULongCounterValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head),UInt32,UInt32, use_last_error=False)(("PerfIncrementULongCounterValue", windll["ADVAPI32"]), ((1, 'Provider'),(1, 'Instance'),(1, 'CounterId'),(1, 'Value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfIncrementULongLongCounterValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head),UInt32,UInt64, use_last_error=False)(("PerfIncrementULongLongCounterValue", windll["ADVAPI32"]), ((1, 'Provider'),(1, 'Instance'),(1, 'CounterId'),(1, 'Value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfDecrementULongCounterValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head),UInt32,UInt32, use_last_error=False)(("PerfDecrementULongCounterValue", windll["ADVAPI32"]), ((1, 'Provider'),(1, 'Instance'),(1, 'CounterId'),(1, 'Value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfDecrementULongLongCounterValue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.System.Performance.PERF_COUNTERSET_INSTANCE_head),UInt32,UInt64, use_last_error=False)(("PerfDecrementULongLongCounterValue", windll["ADVAPI32"]), ((1, 'Provider'),(1, 'Instance'),(1, 'CounterId'),(1, 'Value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfEnumerateCounterSet():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Guid),UInt32,POINTER(UInt32), use_last_error=False)(("PerfEnumerateCounterSet", windll["ADVAPI32"]), ((1, 'szMachine'),(1, 'pCounterSetIds'),(1, 'cCounterSetIds'),(1, 'pcCounterSetIdsActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfEnumerateCounterSetInstances():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(win32more.System.Performance.PERF_INSTANCE_HEADER_head),UInt32,POINTER(UInt32), use_last_error=False)(("PerfEnumerateCounterSetInstances", windll["ADVAPI32"]), ((1, 'szMachine'),(1, 'pCounterSetId'),(1, 'pInstances'),(1, 'cbInstances'),(1, 'pcbInstancesActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfQueryCounterSetRegistrationInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(Guid),win32more.System.Performance.PerfRegInfoType,UInt32,c_char_p_no,UInt32,POINTER(UInt32), use_last_error=False)(("PerfQueryCounterSetRegistrationInfo", windll["ADVAPI32"]), ((1, 'szMachine'),(1, 'pCounterSetId'),(1, 'requestCode'),(1, 'requestLangId'),(1, 'pbRegInfo'),(1, 'cbRegInfo'),(1, 'pcbRegInfoActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfOpenQueryHandle():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.System.Performance.PerfQueryHandle), use_last_error=False)(("PerfOpenQueryHandle", windll["ADVAPI32"]), ((1, 'szMachine'),(1, 'phQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfCloseQueryHandle():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("PerfCloseQueryHandle", windll["ADVAPI32"]), ((1, 'hQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfQueryCounterInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Performance.PerfQueryHandle,POINTER(win32more.System.Performance.PERF_COUNTER_IDENTIFIER_head),UInt32,POINTER(UInt32), use_last_error=False)(("PerfQueryCounterInfo", windll["ADVAPI32"]), ((1, 'hQuery'),(1, 'pCounters'),(1, 'cbCounters'),(1, 'pcbCountersActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfQueryCounterData():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Performance.PerfQueryHandle,POINTER(win32more.System.Performance.PERF_DATA_HEADER_head),UInt32,POINTER(UInt32), use_last_error=False)(("PerfQueryCounterData", windll["ADVAPI32"]), ((1, 'hQuery'),(1, 'pCounterBlock'),(1, 'cbCounterBlock'),(1, 'pcbCounterBlockActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfAddCounters():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Performance.PerfQueryHandle,POINTER(win32more.System.Performance.PERF_COUNTER_IDENTIFIER_head),UInt32, use_last_error=False)(("PerfAddCounters", windll["ADVAPI32"]), ((1, 'hQuery'),(1, 'pCounters'),(1, 'cbCounters'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PerfDeleteCounters():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Performance.PerfQueryHandle,POINTER(win32more.System.Performance.PERF_COUNTER_IDENTIFIER_head),UInt32, use_last_error=False)(("PerfDeleteCounters", windll["ADVAPI32"]), ((1, 'hQuery'),(1, 'pCounters'),(1, 'cbCounters'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetDllVersion():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Performance.PDH_DLL_VERSION), use_last_error=False)(("PdhGetDllVersion", windll["pdh"]), ((1, 'lpdwVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhOpenQueryW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,UIntPtr,POINTER(IntPtr), use_last_error=False)(("PdhOpenQueryW", windll["pdh"]), ((1, 'szDataSource'),(1, 'dwUserData'),(1, 'phQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhOpenQuery():
    return win32more.System.Performance.PdhOpenQueryW
def _define_PdhOpenQueryA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,UIntPtr,POINTER(IntPtr), use_last_error=False)(("PdhOpenQueryA", windll["pdh"]), ((1, 'szDataSource'),(1, 'dwUserData'),(1, 'phQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhAddCounterW():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PWSTR,UIntPtr,POINTER(IntPtr), use_last_error=False)(("PdhAddCounterW", windll["pdh"]), ((1, 'hQuery'),(1, 'szFullCounterPath'),(1, 'dwUserData'),(1, 'phCounter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhAddCounter():
    return win32more.System.Performance.PdhAddCounterW
def _define_PdhAddCounterA():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PSTR,UIntPtr,POINTER(IntPtr), use_last_error=False)(("PdhAddCounterA", windll["pdh"]), ((1, 'hQuery'),(1, 'szFullCounterPath'),(1, 'dwUserData'),(1, 'phCounter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhAddEnglishCounterW():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PWSTR,UIntPtr,POINTER(IntPtr), use_last_error=False)(("PdhAddEnglishCounterW", windll["pdh"]), ((1, 'hQuery'),(1, 'szFullCounterPath'),(1, 'dwUserData'),(1, 'phCounter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhAddEnglishCounter():
    return win32more.System.Performance.PdhAddEnglishCounterW
def _define_PdhAddEnglishCounterA():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PSTR,UIntPtr,POINTER(IntPtr), use_last_error=False)(("PdhAddEnglishCounterA", windll["pdh"]), ((1, 'hQuery'),(1, 'szFullCounterPath'),(1, 'dwUserData'),(1, 'phCounter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhCollectQueryDataWithTime():
    try:
        return WINFUNCTYPE(Int32,IntPtr,POINTER(Int64), use_last_error=False)(("PdhCollectQueryDataWithTime", windll["pdh"]), ((1, 'hQuery'),(1, 'pllTimeStamp'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhValidatePathExW():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PWSTR, use_last_error=False)(("PdhValidatePathExW", windll["pdh"]), ((1, 'hDataSource'),(1, 'szFullPathBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhValidatePathEx():
    return win32more.System.Performance.PdhValidatePathExW
def _define_PdhValidatePathExA():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PSTR, use_last_error=False)(("PdhValidatePathExA", windll["pdh"]), ((1, 'hDataSource'),(1, 'szFullPathBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhRemoveCounter():
    try:
        return WINFUNCTYPE(Int32,IntPtr, use_last_error=False)(("PdhRemoveCounter", windll["pdh"]), ((1, 'hCounter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhCollectQueryData():
    try:
        return WINFUNCTYPE(Int32,IntPtr, use_last_error=False)(("PdhCollectQueryData", windll["pdh"]), ((1, 'hQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhCloseQuery():
    try:
        return WINFUNCTYPE(Int32,IntPtr, use_last_error=False)(("PdhCloseQuery", windll["pdh"]), ((1, 'hQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetFormattedCounterValue():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.System.Performance.PDH_FMT,POINTER(UInt32),POINTER(win32more.System.Performance.PDH_FMT_COUNTERVALUE_head), use_last_error=False)(("PdhGetFormattedCounterValue", windll["pdh"]), ((1, 'hCounter'),(1, 'dwFormat'),(1, 'lpdwType'),(1, 'pValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetFormattedCounterArrayA():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.System.Performance.PDH_FMT,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.System.Performance.PDH_FMT_COUNTERVALUE_ITEM_A_head), use_last_error=False)(("PdhGetFormattedCounterArrayA", windll["pdh"]), ((1, 'hCounter'),(1, 'dwFormat'),(1, 'lpdwBufferSize'),(1, 'lpdwItemCount'),(1, 'ItemBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetFormattedCounterArrayW():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.System.Performance.PDH_FMT,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.System.Performance.PDH_FMT_COUNTERVALUE_ITEM_W_head), use_last_error=False)(("PdhGetFormattedCounterArrayW", windll["pdh"]), ((1, 'hCounter'),(1, 'dwFormat'),(1, 'lpdwBufferSize'),(1, 'lpdwItemCount'),(1, 'ItemBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetFormattedCounterArray():
    return win32more.System.Performance.PdhGetFormattedCounterArrayW
def _define_PdhGetRawCounterValue():
    try:
        return WINFUNCTYPE(Int32,IntPtr,POINTER(UInt32),POINTER(win32more.System.Performance.PDH_RAW_COUNTER_head), use_last_error=False)(("PdhGetRawCounterValue", windll["pdh"]), ((1, 'hCounter'),(1, 'lpdwType'),(1, 'pValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetRawCounterArrayA():
    try:
        return WINFUNCTYPE(Int32,IntPtr,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.System.Performance.PDH_RAW_COUNTER_ITEM_A_head), use_last_error=False)(("PdhGetRawCounterArrayA", windll["pdh"]), ((1, 'hCounter'),(1, 'lpdwBufferSize'),(1, 'lpdwItemCount'),(1, 'ItemBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetRawCounterArrayW():
    try:
        return WINFUNCTYPE(Int32,IntPtr,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.System.Performance.PDH_RAW_COUNTER_ITEM_W_head), use_last_error=False)(("PdhGetRawCounterArrayW", windll["pdh"]), ((1, 'hCounter'),(1, 'lpdwBufferSize'),(1, 'lpdwItemCount'),(1, 'ItemBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetRawCounterArray():
    return win32more.System.Performance.PdhGetRawCounterArrayW
def _define_PdhCalculateCounterFromRawValue():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.System.Performance.PDH_FMT,POINTER(win32more.System.Performance.PDH_RAW_COUNTER_head),POINTER(win32more.System.Performance.PDH_RAW_COUNTER_head),POINTER(win32more.System.Performance.PDH_FMT_COUNTERVALUE_head), use_last_error=False)(("PdhCalculateCounterFromRawValue", windll["pdh"]), ((1, 'hCounter'),(1, 'dwFormat'),(1, 'rawValue1'),(1, 'rawValue2'),(1, 'fmtValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhComputeCounterStatistics():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.System.Performance.PDH_FMT,UInt32,UInt32,POINTER(win32more.System.Performance.PDH_RAW_COUNTER_head),POINTER(win32more.System.Performance.PDH_STATISTICS_head), use_last_error=False)(("PdhComputeCounterStatistics", windll["pdh"]), ((1, 'hCounter'),(1, 'dwFormat'),(1, 'dwFirstEntry'),(1, 'dwNumEntries'),(1, 'lpRawValueArray'),(1, 'data'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetCounterInfoW():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.BOOLEAN,POINTER(UInt32),POINTER(win32more.System.Performance.PDH_COUNTER_INFO_W_head), use_last_error=False)(("PdhGetCounterInfoW", windll["pdh"]), ((1, 'hCounter'),(1, 'bRetrieveExplainText'),(1, 'pdwBufferSize'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetCounterInfo():
    return win32more.System.Performance.PdhGetCounterInfoW
def _define_PdhGetCounterInfoA():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.BOOLEAN,POINTER(UInt32),POINTER(win32more.System.Performance.PDH_COUNTER_INFO_A_head), use_last_error=False)(("PdhGetCounterInfoA", windll["pdh"]), ((1, 'hCounter'),(1, 'bRetrieveExplainText'),(1, 'pdwBufferSize'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhSetCounterScaleFactor():
    try:
        return WINFUNCTYPE(Int32,IntPtr,Int32, use_last_error=False)(("PdhSetCounterScaleFactor", windll["pdh"]), ((1, 'hCounter'),(1, 'lFactor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhConnectMachineW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR, use_last_error=False)(("PdhConnectMachineW", windll["pdh"]), ((1, 'szMachineName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhConnectMachine():
    return win32more.System.Performance.PdhConnectMachineW
def _define_PdhConnectMachineA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR, use_last_error=False)(("PdhConnectMachineA", windll["pdh"]), ((1, 'szMachineName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumMachinesW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("PdhEnumMachinesW", windll["pdh"]), ((1, 'szDataSource'),(1, 'mszMachineList'),(1, 'pcchBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumMachines():
    return win32more.System.Performance.PdhEnumMachinesW
def _define_PdhEnumMachinesA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("PdhEnumMachinesA", windll["pdh"]), ((1, 'szDataSource'),(1, 'mszMachineList'),(1, 'pcchBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumObjectsW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.System.Performance.PERF_DETAIL,win32more.Foundation.BOOL, use_last_error=False)(("PdhEnumObjectsW", windll["pdh"]), ((1, 'szDataSource'),(1, 'szMachineName'),(1, 'mszObjectList'),(1, 'pcchBufferSize'),(1, 'dwDetailLevel'),(1, 'bRefresh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumObjects():
    return win32more.System.Performance.PdhEnumObjectsW
def _define_PdhEnumObjectsA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32),win32more.System.Performance.PERF_DETAIL,win32more.Foundation.BOOL, use_last_error=False)(("PdhEnumObjectsA", windll["pdh"]), ((1, 'szDataSource'),(1, 'szMachineName'),(1, 'mszObjectList'),(1, 'pcchBufferSize'),(1, 'dwDetailLevel'),(1, 'bRefresh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumObjectItemsW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.System.Performance.PERF_DETAIL,UInt32, use_last_error=False)(("PdhEnumObjectItemsW", windll["pdh"]), ((1, 'szDataSource'),(1, 'szMachineName'),(1, 'szObjectName'),(1, 'mszCounterList'),(1, 'pcchCounterListLength'),(1, 'mszInstanceList'),(1, 'pcchInstanceListLength'),(1, 'dwDetailLevel'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumObjectItems():
    return win32more.System.Performance.PdhEnumObjectItemsW
def _define_PdhEnumObjectItemsA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32),win32more.Foundation.PSTR,POINTER(UInt32),win32more.System.Performance.PERF_DETAIL,UInt32, use_last_error=False)(("PdhEnumObjectItemsA", windll["pdh"]), ((1, 'szDataSource'),(1, 'szMachineName'),(1, 'szObjectName'),(1, 'mszCounterList'),(1, 'pcchCounterListLength'),(1, 'mszInstanceList'),(1, 'pcchInstanceListLength'),(1, 'dwDetailLevel'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhMakeCounterPathW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_W_head),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.System.Performance.PDH_PATH_FLAGS, use_last_error=False)(("PdhMakeCounterPathW", windll["pdh"]), ((1, 'pCounterPathElements'),(1, 'szFullPathBuffer'),(1, 'pcchBufferSize'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhMakeCounterPath():
    return win32more.System.Performance.PdhMakeCounterPathW
def _define_PdhMakeCounterPathA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_A_head),win32more.Foundation.PSTR,POINTER(UInt32),win32more.System.Performance.PDH_PATH_FLAGS, use_last_error=False)(("PdhMakeCounterPathA", windll["pdh"]), ((1, 'pCounterPathElements'),(1, 'szFullPathBuffer'),(1, 'pcchBufferSize'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhParseCounterPathW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,POINTER(win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_W_head),POINTER(UInt32),UInt32, use_last_error=False)(("PdhParseCounterPathW", windll["pdh"]), ((1, 'szFullPathBuffer'),(1, 'pCounterPathElements'),(1, 'pdwBufferSize'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhParseCounterPath():
    return win32more.System.Performance.PdhParseCounterPathW
def _define_PdhParseCounterPathA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,POINTER(win32more.System.Performance.PDH_COUNTER_PATH_ELEMENTS_A_head),POINTER(UInt32),UInt32, use_last_error=False)(("PdhParseCounterPathA", windll["pdh"]), ((1, 'szFullPathBuffer'),(1, 'pCounterPathElements'),(1, 'pdwBufferSize'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhParseInstanceNameW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("PdhParseInstanceNameW", windll["pdh"]), ((1, 'szInstanceString'),(1, 'szInstanceName'),(1, 'pcchInstanceNameLength'),(1, 'szParentName'),(1, 'pcchParentNameLength'),(1, 'lpIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhParseInstanceName():
    return win32more.System.Performance.PdhParseInstanceNameW
def _define_PdhParseInstanceNameA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32),win32more.Foundation.PSTR,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("PdhParseInstanceNameA", windll["pdh"]), ((1, 'szInstanceString'),(1, 'szInstanceName'),(1, 'pcchInstanceNameLength'),(1, 'szParentName'),(1, 'pcchParentNameLength'),(1, 'lpIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhValidatePathW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR, use_last_error=False)(("PdhValidatePathW", windll["pdh"]), ((1, 'szFullPathBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhValidatePath():
    return win32more.System.Performance.PdhValidatePathW
def _define_PdhValidatePathA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR, use_last_error=False)(("PdhValidatePathA", windll["pdh"]), ((1, 'szFullPathBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetDefaultPerfObjectW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("PdhGetDefaultPerfObjectW", windll["pdh"]), ((1, 'szDataSource'),(1, 'szMachineName'),(1, 'szDefaultObjectName'),(1, 'pcchBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetDefaultPerfObject():
    return win32more.System.Performance.PdhGetDefaultPerfObjectW
def _define_PdhGetDefaultPerfObjectA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("PdhGetDefaultPerfObjectA", windll["pdh"]), ((1, 'szDataSource'),(1, 'szMachineName'),(1, 'szDefaultObjectName'),(1, 'pcchBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetDefaultPerfCounterW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("PdhGetDefaultPerfCounterW", windll["pdh"]), ((1, 'szDataSource'),(1, 'szMachineName'),(1, 'szObjectName'),(1, 'szDefaultCounterName'),(1, 'pcchBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetDefaultPerfCounter():
    return win32more.System.Performance.PdhGetDefaultPerfCounterW
def _define_PdhGetDefaultPerfCounterA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("PdhGetDefaultPerfCounterA", windll["pdh"]), ((1, 'szDataSource'),(1, 'szMachineName'),(1, 'szObjectName'),(1, 'szDefaultCounterName'),(1, 'pcchBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhBrowseCountersW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Performance.PDH_BROWSE_DLG_CONFIG_W_head), use_last_error=False)(("PdhBrowseCountersW", windll["pdh"]), ((1, 'pBrowseDlgData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhBrowseCounters():
    return win32more.System.Performance.PdhBrowseCountersW
def _define_PdhBrowseCountersA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Performance.PDH_BROWSE_DLG_CONFIG_A_head), use_last_error=False)(("PdhBrowseCountersA", windll["pdh"]), ((1, 'pBrowseDlgData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhExpandCounterPathW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("PdhExpandCounterPathW", windll["pdh"]), ((1, 'szWildCardPath'),(1, 'mszExpandedPathList'),(1, 'pcchPathListLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhExpandCounterPath():
    return win32more.System.Performance.PdhExpandCounterPathW
def _define_PdhExpandCounterPathA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("PdhExpandCounterPathA", windll["pdh"]), ((1, 'szWildCardPath'),(1, 'mszExpandedPathList'),(1, 'pcchPathListLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhLookupPerfNameByIndexW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("PdhLookupPerfNameByIndexW", windll["pdh"]), ((1, 'szMachineName'),(1, 'dwNameIndex'),(1, 'szNameBuffer'),(1, 'pcchNameBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhLookupPerfNameByIndex():
    return win32more.System.Performance.PdhLookupPerfNameByIndexW
def _define_PdhLookupPerfNameByIndexA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("PdhLookupPerfNameByIndexA", windll["pdh"]), ((1, 'szMachineName'),(1, 'dwNameIndex'),(1, 'szNameBuffer'),(1, 'pcchNameBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhLookupPerfIndexByNameW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("PdhLookupPerfIndexByNameW", windll["pdh"]), ((1, 'szMachineName'),(1, 'szNameBuffer'),(1, 'pdwIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhLookupPerfIndexByName():
    return win32more.System.Performance.PdhLookupPerfIndexByNameW
def _define_PdhLookupPerfIndexByNameA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("PdhLookupPerfIndexByNameA", windll["pdh"]), ((1, 'szMachineName'),(1, 'szNameBuffer'),(1, 'pdwIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhExpandWildCardPathA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32),UInt32, use_last_error=False)(("PdhExpandWildCardPathA", windll["pdh"]), ((1, 'szDataSource'),(1, 'szWildCardPath'),(1, 'mszExpandedPathList'),(1, 'pcchPathListLength'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhExpandWildCardPathW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),UInt32, use_last_error=False)(("PdhExpandWildCardPathW", windll["pdh"]), ((1, 'szDataSource'),(1, 'szWildCardPath'),(1, 'mszExpandedPathList'),(1, 'pcchPathListLength'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhExpandWildCardPath():
    return win32more.System.Performance.PdhExpandWildCardPathW
def _define_PdhOpenLogW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.System.Performance.PDH_LOG,POINTER(win32more.System.Performance.PDH_LOG_TYPE),IntPtr,UInt32,win32more.Foundation.PWSTR,POINTER(IntPtr), use_last_error=False)(("PdhOpenLogW", windll["pdh"]), ((1, 'szLogFileName'),(1, 'dwAccessFlags'),(1, 'lpdwLogType'),(1, 'hQuery'),(1, 'dwMaxSize'),(1, 'szUserCaption'),(1, 'phLog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhOpenLog():
    return win32more.System.Performance.PdhOpenLogW
def _define_PdhOpenLogA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.System.Performance.PDH_LOG,POINTER(win32more.System.Performance.PDH_LOG_TYPE),IntPtr,UInt32,win32more.Foundation.PSTR,POINTER(IntPtr), use_last_error=False)(("PdhOpenLogA", windll["pdh"]), ((1, 'szLogFileName'),(1, 'dwAccessFlags'),(1, 'lpdwLogType'),(1, 'hQuery'),(1, 'dwMaxSize'),(1, 'szUserCaption'),(1, 'phLog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhUpdateLogW():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PWSTR, use_last_error=False)(("PdhUpdateLogW", windll["pdh"]), ((1, 'hLog'),(1, 'szUserString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhUpdateLog():
    return win32more.System.Performance.PdhUpdateLogW
def _define_PdhUpdateLogA():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PSTR, use_last_error=False)(("PdhUpdateLogA", windll["pdh"]), ((1, 'hLog'),(1, 'szUserString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhUpdateLogFileCatalog():
    try:
        return WINFUNCTYPE(Int32,IntPtr, use_last_error=False)(("PdhUpdateLogFileCatalog", windll["pdh"]), ((1, 'hLog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetLogFileSize():
    try:
        return WINFUNCTYPE(Int32,IntPtr,POINTER(Int64), use_last_error=False)(("PdhGetLogFileSize", windll["pdh"]), ((1, 'hLog'),(1, 'llSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhCloseLog():
    try:
        return WINFUNCTYPE(Int32,IntPtr,UInt32, use_last_error=False)(("PdhCloseLog", windll["pdh"]), ((1, 'hLog'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhSelectDataSourceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HWND,win32more.System.Performance.PDH_SELECT_DATA_SOURCE_FLAGS,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("PdhSelectDataSourceW", windll["pdh"]), ((1, 'hWndOwner'),(1, 'dwFlags'),(1, 'szDataSource'),(1, 'pcchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhSelectDataSource():
    return win32more.System.Performance.PdhSelectDataSourceW
def _define_PdhSelectDataSourceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HWND,win32more.System.Performance.PDH_SELECT_DATA_SOURCE_FLAGS,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("PdhSelectDataSourceA", windll["pdh"]), ((1, 'hWndOwner'),(1, 'dwFlags'),(1, 'szDataSource'),(1, 'pcchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhIsRealTimeQuery():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr, use_last_error=False)(("PdhIsRealTimeQuery", windll["pdh"]), ((1, 'hQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhSetQueryTimeRange():
    try:
        return WINFUNCTYPE(Int32,IntPtr,POINTER(win32more.System.Performance.PDH_TIME_INFO_head), use_last_error=False)(("PdhSetQueryTimeRange", windll["pdh"]), ((1, 'hQuery'),(1, 'pInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetDataSourceTimeRangeW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.System.Performance.PDH_TIME_INFO_head),POINTER(UInt32), use_last_error=False)(("PdhGetDataSourceTimeRangeW", windll["pdh"]), ((1, 'szDataSource'),(1, 'pdwNumEntries'),(1, 'pInfo'),(1, 'pdwBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetDataSourceTimeRange():
    return win32more.System.Performance.PdhGetDataSourceTimeRangeW
def _define_PdhGetDataSourceTimeRangeA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,POINTER(UInt32),POINTER(win32more.System.Performance.PDH_TIME_INFO_head),POINTER(UInt32), use_last_error=False)(("PdhGetDataSourceTimeRangeA", windll["pdh"]), ((1, 'szDataSource'),(1, 'pdwNumEntries'),(1, 'pInfo'),(1, 'pdwBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhCollectQueryDataEx():
    try:
        return WINFUNCTYPE(Int32,IntPtr,UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("PdhCollectQueryDataEx", windll["pdh"]), ((1, 'hQuery'),(1, 'dwIntervalTime'),(1, 'hNewDataEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhFormatFromRawValue():
    try:
        return WINFUNCTYPE(Int32,UInt32,win32more.System.Performance.PDH_FMT,POINTER(Int64),POINTER(win32more.System.Performance.PDH_RAW_COUNTER_head),POINTER(win32more.System.Performance.PDH_RAW_COUNTER_head),POINTER(win32more.System.Performance.PDH_FMT_COUNTERVALUE_head), use_last_error=False)(("PdhFormatFromRawValue", windll["pdh"]), ((1, 'dwCounterType'),(1, 'dwFormat'),(1, 'pTimeBase'),(1, 'pRawValue1'),(1, 'pRawValue2'),(1, 'pFmtValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetCounterTimeBase():
    try:
        return WINFUNCTYPE(Int32,IntPtr,POINTER(Int64), use_last_error=False)(("PdhGetCounterTimeBase", windll["pdh"]), ((1, 'hCounter'),(1, 'pTimeBase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhReadRawLogRecord():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.FILETIME,POINTER(win32more.System.Performance.PDH_RAW_LOG_RECORD_head),POINTER(UInt32), use_last_error=False)(("PdhReadRawLogRecord", windll["pdh"]), ((1, 'hLog'),(1, 'ftRecord'),(1, 'pRawLogRecord'),(1, 'pdwBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhSetDefaultRealTimeDataSource():
    try:
        return WINFUNCTYPE(Int32,win32more.System.Performance.REAL_TIME_DATA_SOURCE_ID_FLAGS, use_last_error=False)(("PdhSetDefaultRealTimeDataSource", windll["pdh"]), ((1, 'dwDataSourceId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhBindInputDataSourceW():
    try:
        return WINFUNCTYPE(Int32,POINTER(IntPtr),win32more.Foundation.PWSTR, use_last_error=False)(("PdhBindInputDataSourceW", windll["pdh"]), ((1, 'phDataSource'),(1, 'LogFileNameList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhBindInputDataSource():
    return win32more.System.Performance.PdhBindInputDataSourceW
def _define_PdhBindInputDataSourceA():
    try:
        return WINFUNCTYPE(Int32,POINTER(IntPtr),win32more.Foundation.PSTR, use_last_error=False)(("PdhBindInputDataSourceA", windll["pdh"]), ((1, 'phDataSource'),(1, 'LogFileNameList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhOpenQueryH():
    try:
        return WINFUNCTYPE(Int32,IntPtr,UIntPtr,POINTER(IntPtr), use_last_error=False)(("PdhOpenQueryH", windll["pdh"]), ((1, 'hDataSource'),(1, 'dwUserData'),(1, 'phQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumMachinesHW():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("PdhEnumMachinesHW", windll["pdh"]), ((1, 'hDataSource'),(1, 'mszMachineList'),(1, 'pcchBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumMachinesH():
    return win32more.System.Performance.PdhEnumMachinesHW
def _define_PdhEnumMachinesHA():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("PdhEnumMachinesHA", windll["pdh"]), ((1, 'hDataSource'),(1, 'mszMachineList'),(1, 'pcchBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumObjectsHW():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.System.Performance.PERF_DETAIL,win32more.Foundation.BOOL, use_last_error=False)(("PdhEnumObjectsHW", windll["pdh"]), ((1, 'hDataSource'),(1, 'szMachineName'),(1, 'mszObjectList'),(1, 'pcchBufferSize'),(1, 'dwDetailLevel'),(1, 'bRefresh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumObjectsH():
    return win32more.System.Performance.PdhEnumObjectsHW
def _define_PdhEnumObjectsHA():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32),win32more.System.Performance.PERF_DETAIL,win32more.Foundation.BOOL, use_last_error=False)(("PdhEnumObjectsHA", windll["pdh"]), ((1, 'hDataSource'),(1, 'szMachineName'),(1, 'mszObjectList'),(1, 'pcchBufferSize'),(1, 'dwDetailLevel'),(1, 'bRefresh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumObjectItemsHW():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32),win32more.System.Performance.PERF_DETAIL,UInt32, use_last_error=False)(("PdhEnumObjectItemsHW", windll["pdh"]), ((1, 'hDataSource'),(1, 'szMachineName'),(1, 'szObjectName'),(1, 'mszCounterList'),(1, 'pcchCounterListLength'),(1, 'mszInstanceList'),(1, 'pcchInstanceListLength'),(1, 'dwDetailLevel'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumObjectItemsH():
    return win32more.System.Performance.PdhEnumObjectItemsHW
def _define_PdhEnumObjectItemsHA():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32),win32more.Foundation.PSTR,POINTER(UInt32),win32more.System.Performance.PERF_DETAIL,UInt32, use_last_error=False)(("PdhEnumObjectItemsHA", windll["pdh"]), ((1, 'hDataSource'),(1, 'szMachineName'),(1, 'szObjectName'),(1, 'mszCounterList'),(1, 'pcchCounterListLength'),(1, 'mszInstanceList'),(1, 'pcchInstanceListLength'),(1, 'dwDetailLevel'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhExpandWildCardPathHW():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),UInt32, use_last_error=False)(("PdhExpandWildCardPathHW", windll["pdh"]), ((1, 'hDataSource'),(1, 'szWildCardPath'),(1, 'mszExpandedPathList'),(1, 'pcchPathListLength'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhExpandWildCardPathH():
    return win32more.System.Performance.PdhExpandWildCardPathHW
def _define_PdhExpandWildCardPathHA():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32),UInt32, use_last_error=False)(("PdhExpandWildCardPathHA", windll["pdh"]), ((1, 'hDataSource'),(1, 'szWildCardPath'),(1, 'mszExpandedPathList'),(1, 'pcchPathListLength'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetDataSourceTimeRangeH():
    try:
        return WINFUNCTYPE(Int32,IntPtr,POINTER(UInt32),POINTER(win32more.System.Performance.PDH_TIME_INFO_head),POINTER(UInt32), use_last_error=False)(("PdhGetDataSourceTimeRangeH", windll["pdh"]), ((1, 'hDataSource'),(1, 'pdwNumEntries'),(1, 'pInfo'),(1, 'pdwBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetDefaultPerfObjectHW():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("PdhGetDefaultPerfObjectHW", windll["pdh"]), ((1, 'hDataSource'),(1, 'szMachineName'),(1, 'szDefaultObjectName'),(1, 'pcchBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetDefaultPerfObjectH():
    return win32more.System.Performance.PdhGetDefaultPerfObjectHW
def _define_PdhGetDefaultPerfObjectHA():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("PdhGetDefaultPerfObjectHA", windll["pdh"]), ((1, 'hDataSource'),(1, 'szMachineName'),(1, 'szDefaultObjectName'),(1, 'pcchBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetDefaultPerfCounterHW():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("PdhGetDefaultPerfCounterHW", windll["pdh"]), ((1, 'hDataSource'),(1, 'szMachineName'),(1, 'szObjectName'),(1, 'szDefaultCounterName'),(1, 'pcchBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetDefaultPerfCounterH():
    return win32more.System.Performance.PdhGetDefaultPerfCounterHW
def _define_PdhGetDefaultPerfCounterHA():
    try:
        return WINFUNCTYPE(Int32,IntPtr,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("PdhGetDefaultPerfCounterHA", windll["pdh"]), ((1, 'hDataSource'),(1, 'szMachineName'),(1, 'szObjectName'),(1, 'szDefaultCounterName'),(1, 'pcchBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhBrowseCountersHW():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Performance.PDH_BROWSE_DLG_CONFIG_HW_head), use_last_error=False)(("PdhBrowseCountersHW", windll["pdh"]), ((1, 'pBrowseDlgData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhBrowseCountersH():
    return win32more.System.Performance.PdhBrowseCountersHW
def _define_PdhBrowseCountersHA():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.System.Performance.PDH_BROWSE_DLG_CONFIG_HA_head), use_last_error=False)(("PdhBrowseCountersHA", windll["pdh"]), ((1, 'pBrowseDlgData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhVerifySQLDBW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR, use_last_error=False)(("PdhVerifySQLDBW", windll["pdh"]), ((1, 'szDataSource'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhVerifySQLDB():
    return win32more.System.Performance.PdhVerifySQLDBW
def _define_PdhVerifySQLDBA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR, use_last_error=False)(("PdhVerifySQLDBA", windll["pdh"]), ((1, 'szDataSource'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhCreateSQLTablesW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR, use_last_error=False)(("PdhCreateSQLTablesW", windll["pdh"]), ((1, 'szDataSource'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhCreateSQLTables():
    return win32more.System.Performance.PdhCreateSQLTablesW
def _define_PdhCreateSQLTablesA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR, use_last_error=False)(("PdhCreateSQLTablesA", windll["pdh"]), ((1, 'szDataSource'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumLogSetNamesW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("PdhEnumLogSetNamesW", windll["pdh"]), ((1, 'szDataSource'),(1, 'mszDataSetNameList'),(1, 'pcchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhEnumLogSetNames():
    return win32more.System.Performance.PdhEnumLogSetNamesW
def _define_PdhEnumLogSetNamesA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("PdhEnumLogSetNamesA", windll["pdh"]), ((1, 'szDataSource'),(1, 'mszDataSetNameList'),(1, 'pcchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhGetLogSetGUID():
    try:
        return WINFUNCTYPE(Int32,IntPtr,POINTER(Guid),POINTER(Int32), use_last_error=False)(("PdhGetLogSetGUID", windll["pdh"]), ((1, 'hLog'),(1, 'pGuid'),(1, 'pRunId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PdhSetLogSetRunID():
    try:
        return WINFUNCTYPE(Int32,IntPtr,Int32, use_last_error=False)(("PdhSetLogSetRunID", windll["pdh"]), ((1, 'hLog'),(1, 'RunId'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "MAX_COUNTER_PATH",
    "PDH_MAX_COUNTER_NAME",
    "PDH_MAX_INSTANCE_NAME",
    "PDH_MAX_COUNTER_PATH",
    "PDH_MAX_DATASOURCE_PATH",
    "H_WBEM_DATASOURCE",
    "PDH_MAX_SCALE",
    "PDH_MIN_SCALE",
    "PDH_NOEXPANDCOUNTERS",
    "PDH_NOEXPANDINSTANCES",
    "PDH_REFRESHCOUNTERS",
    "PDH_LOG_TYPE_RETIRED_BIN",
    "PDH_LOG_TYPE_TRACE_KERNEL",
    "PDH_LOG_TYPE_TRACE_GENERIC",
    "PERF_PROVIDER_USER_MODE",
    "PERF_PROVIDER_KERNEL_MODE",
    "PERF_PROVIDER_DRIVER",
    "PERF_COUNTERSET_FLAG_MULTIPLE",
    "PERF_COUNTERSET_FLAG_AGGREGATE",
    "PERF_COUNTERSET_FLAG_HISTORY",
    "PERF_COUNTERSET_FLAG_INSTANCE",
    "PERF_COUNTERSET_SINGLE_INSTANCE",
    "PERF_COUNTERSET_MULTI_INSTANCES",
    "PERF_COUNTERSET_SINGLE_AGGREGATE",
    "PERF_AGGREGATE_MAX",
    "PERF_ATTRIB_BY_REFERENCE",
    "PERF_ATTRIB_NO_DISPLAYABLE",
    "PERF_ATTRIB_NO_GROUP_SEPARATOR",
    "PERF_ATTRIB_DISPLAY_AS_REAL",
    "PERF_ATTRIB_DISPLAY_AS_HEX",
    "PERF_WILDCARD_COUNTER",
    "PERF_MAX_INSTANCE_NAME",
    "PERF_ADD_COUNTER",
    "PERF_REMOVE_COUNTER",
    "PERF_ENUM_INSTANCES",
    "PERF_COLLECT_START",
    "PERF_COLLECT_END",
    "PERF_FILTER",
    "PERF_DATA_VERSION",
    "PERF_DATA_REVISION",
    "PERF_NO_INSTANCES",
    "PERF_METADATA_MULTIPLE_INSTANCES",
    "PERF_METADATA_NO_INSTANCES",
    "PERF_SIZE_DWORD",
    "PERF_SIZE_LARGE",
    "PERF_SIZE_ZERO",
    "PERF_SIZE_VARIABLE_LEN",
    "PERF_TYPE_NUMBER",
    "PERF_TYPE_COUNTER",
    "PERF_TYPE_TEXT",
    "PERF_TYPE_ZERO",
    "PERF_NUMBER_HEX",
    "PERF_NUMBER_DECIMAL",
    "PERF_NUMBER_DEC_1000",
    "PERF_COUNTER_VALUE",
    "PERF_COUNTER_RATE",
    "PERF_COUNTER_FRACTION",
    "PERF_COUNTER_BASE",
    "PERF_COUNTER_ELAPSED",
    "PERF_COUNTER_QUEUELEN",
    "PERF_COUNTER_HISTOGRAM",
    "PERF_COUNTER_PRECISION",
    "PERF_TEXT_UNICODE",
    "PERF_TEXT_ASCII",
    "PERF_TIMER_TICK",
    "PERF_TIMER_100NS",
    "PERF_OBJECT_TIMER",
    "PERF_DELTA_COUNTER",
    "PERF_DELTA_BASE",
    "PERF_INVERSE_COUNTER",
    "PERF_MULTI_COUNTER",
    "PERF_DISPLAY_NO_SUFFIX",
    "PERF_DISPLAY_PER_SEC",
    "PERF_DISPLAY_PERCENT",
    "PERF_DISPLAY_SECONDS",
    "PERF_DISPLAY_NOSHOW",
    "PERF_COUNTER_HISTOGRAM_TYPE",
    "PERF_NO_UNIQUE_ID",
    "MAX_PERF_OBJECTS_IN_QUERY_FUNCTION",
    "WINPERF_LOG_NONE",
    "WINPERF_LOG_USER",
    "WINPERF_LOG_DEBUG",
    "WINPERF_LOG_VERBOSE",
    "LIBID_SystemMonitor",
    "DIID_DICounterItem",
    "DIID_DILogFileItem",
    "DIID_DISystemMonitor",
    "DIID_DISystemMonitorInternal",
    "DIID_DISystemMonitorEvents",
    "PDH_CSTATUS_VALID_DATA",
    "PDH_CSTATUS_NEW_DATA",
    "PDH_CSTATUS_NO_MACHINE",
    "PDH_CSTATUS_NO_INSTANCE",
    "PDH_MORE_DATA",
    "PDH_CSTATUS_ITEM_NOT_VALIDATED",
    "PDH_RETRY",
    "PDH_NO_DATA",
    "PDH_CALC_NEGATIVE_DENOMINATOR",
    "PDH_CALC_NEGATIVE_TIMEBASE",
    "PDH_CALC_NEGATIVE_VALUE",
    "PDH_DIALOG_CANCELLED",
    "PDH_END_OF_LOG_FILE",
    "PDH_ASYNC_QUERY_TIMEOUT",
    "PDH_CANNOT_SET_DEFAULT_REALTIME_DATASOURCE",
    "PDH_UNABLE_MAP_NAME_FILES",
    "PDH_PLA_VALIDATION_WARNING",
    "PDH_CSTATUS_NO_OBJECT",
    "PDH_CSTATUS_NO_COUNTER",
    "PDH_CSTATUS_INVALID_DATA",
    "PDH_MEMORY_ALLOCATION_FAILURE",
    "PDH_INVALID_HANDLE",
    "PDH_INVALID_ARGUMENT",
    "PDH_FUNCTION_NOT_FOUND",
    "PDH_CSTATUS_NO_COUNTERNAME",
    "PDH_CSTATUS_BAD_COUNTERNAME",
    "PDH_INVALID_BUFFER",
    "PDH_INSUFFICIENT_BUFFER",
    "PDH_CANNOT_CONNECT_MACHINE",
    "PDH_INVALID_PATH",
    "PDH_INVALID_INSTANCE",
    "PDH_INVALID_DATA",
    "PDH_NO_DIALOG_DATA",
    "PDH_CANNOT_READ_NAME_STRINGS",
    "PDH_LOG_FILE_CREATE_ERROR",
    "PDH_LOG_FILE_OPEN_ERROR",
    "PDH_LOG_TYPE_NOT_FOUND",
    "PDH_NO_MORE_DATA",
    "PDH_ENTRY_NOT_IN_LOG_FILE",
    "PDH_DATA_SOURCE_IS_LOG_FILE",
    "PDH_DATA_SOURCE_IS_REAL_TIME",
    "PDH_UNABLE_READ_LOG_HEADER",
    "PDH_FILE_NOT_FOUND",
    "PDH_FILE_ALREADY_EXISTS",
    "PDH_NOT_IMPLEMENTED",
    "PDH_STRING_NOT_FOUND",
    "PDH_UNKNOWN_LOG_FORMAT",
    "PDH_UNKNOWN_LOGSVC_COMMAND",
    "PDH_LOGSVC_QUERY_NOT_FOUND",
    "PDH_LOGSVC_NOT_OPENED",
    "PDH_WBEM_ERROR",
    "PDH_ACCESS_DENIED",
    "PDH_LOG_FILE_TOO_SMALL",
    "PDH_INVALID_DATASOURCE",
    "PDH_INVALID_SQLDB",
    "PDH_NO_COUNTERS",
    "PDH_SQL_ALLOC_FAILED",
    "PDH_SQL_ALLOCCON_FAILED",
    "PDH_SQL_EXEC_DIRECT_FAILED",
    "PDH_SQL_FETCH_FAILED",
    "PDH_SQL_ROWCOUNT_FAILED",
    "PDH_SQL_MORE_RESULTS_FAILED",
    "PDH_SQL_CONNECT_FAILED",
    "PDH_SQL_BIND_FAILED",
    "PDH_CANNOT_CONNECT_WMI_SERVER",
    "PDH_PLA_COLLECTION_ALREADY_RUNNING",
    "PDH_PLA_ERROR_SCHEDULE_OVERLAP",
    "PDH_PLA_COLLECTION_NOT_FOUND",
    "PDH_PLA_ERROR_SCHEDULE_ELAPSED",
    "PDH_PLA_ERROR_NOSTART",
    "PDH_PLA_ERROR_ALREADY_EXISTS",
    "PDH_PLA_ERROR_TYPE_MISMATCH",
    "PDH_PLA_ERROR_FILEPATH",
    "PDH_PLA_SERVICE_ERROR",
    "PDH_PLA_VALIDATION_ERROR",
    "PDH_PLA_ERROR_NAME_TOO_LONG",
    "PDH_INVALID_SQL_LOG_FORMAT",
    "PDH_COUNTER_ALREADY_IN_QUERY",
    "PDH_BINARY_LOG_CORRUPT",
    "PDH_LOG_SAMPLE_TOO_SMALL",
    "PDH_OS_LATER_VERSION",
    "PDH_OS_EARLIER_VERSION",
    "PDH_INCORRECT_APPEND_TIME",
    "PDH_UNMATCHED_APPEND_COUNTER",
    "PDH_SQL_ALTER_DETAIL_FAILED",
    "PDH_QUERY_PERF_DATA_TIMEOUT",
    "PLA_CAPABILITY_LOCAL",
    "PLA_CAPABILITY_V1_SVC",
    "PLA_CAPABILITY_V1_SESSION",
    "PLA_CAPABILITY_V1_SYSTEM",
    "PLA_CAPABILITY_LEGACY_SESSION",
    "PLA_CAPABILITY_LEGACY_SVC",
    "PLA_CAPABILITY_AUTOLOGGER",
    "S_PDH",
    "PERF_DETAIL",
    "PERF_DETAIL_NOVICE",
    "PERF_DETAIL_ADVANCED",
    "PERF_DETAIL_EXPERT",
    "PERF_DETAIL_WIZARD",
    "REAL_TIME_DATA_SOURCE_ID_FLAGS",
    "DATA_SOURCE_REGISTRY",
    "DATA_SOURCE_WBEM",
    "PDH_PATH_FLAGS",
    "PDH_PATH_WBEM_RESULT",
    "PDH_PATH_WBEM_INPUT",
    "PDH_PATH_WBEM_NONE",
    "PDH_FMT",
    "PDH_FMT_DOUBLE",
    "PDH_FMT_LARGE",
    "PDH_FMT_LONG",
    "PDH_LOG_TYPE",
    "PDH_LOG_TYPE_UNDEFINED",
    "PDH_LOG_TYPE_CSV",
    "PDH_LOG_TYPE_SQL",
    "PDH_LOG_TYPE_TSV",
    "PDH_LOG_TYPE_BINARY",
    "PDH_LOG_TYPE_PERFMON",
    "PDH_LOG",
    "PDH_LOG_READ_ACCESS",
    "PDH_LOG_WRITE_ACCESS",
    "PDH_LOG_UPDATE_ACCESS",
    "PDH_SELECT_DATA_SOURCE_FLAGS",
    "PDH_FLAGS_FILE_BROWSER_ONLY",
    "PDH_FLAGS_NONE",
    "PDH_DLL_VERSION",
    "PDH_CVERSION_WIN50",
    "PDH_VERSION",
    "PERF_COUNTER_AGGREGATE_FUNC",
    "PERF_AGGREGATE_UNDEFINED",
    "PERF_AGGREGATE_TOTAL",
    "PERF_AGGREGATE_AVG",
    "PERF_AGGREGATE_MIN",
    "PerfProviderHandle",
    "PerfQueryHandle",
    "DataCollectorSet",
    "TraceSession",
    "TraceSessionCollection",
    "TraceDataProvider",
    "TraceDataProviderCollection",
    "DataCollectorSetCollection",
    "LegacyDataCollectorSet",
    "LegacyDataCollectorSetCollection",
    "LegacyTraceSession",
    "LegacyTraceSessionCollection",
    "ServerDataCollectorSet",
    "ServerDataCollectorSetCollection",
    "SystemDataCollectorSet",
    "SystemDataCollectorSetCollection",
    "BootTraceSession",
    "BootTraceSessionCollection",
    "DataCollectorType",
    "DataCollectorType_plaPerformanceCounter",
    "DataCollectorType_plaTrace",
    "DataCollectorType_plaConfiguration",
    "DataCollectorType_plaAlert",
    "DataCollectorType_plaApiTrace",
    "FileFormat",
    "FileFormat_plaCommaSeparated",
    "FileFormat_plaTabSeparated",
    "FileFormat_plaSql",
    "FileFormat_plaBinary",
    "AutoPathFormat",
    "AutoPathFormat_plaNone",
    "AutoPathFormat_plaPattern",
    "AutoPathFormat_plaComputer",
    "AutoPathFormat_plaMonthDayHour",
    "AutoPathFormat_plaSerialNumber",
    "AutoPathFormat_plaYearDayOfYear",
    "AutoPathFormat_plaYearMonth",
    "AutoPathFormat_plaYearMonthDay",
    "AutoPathFormat_plaYearMonthDayHour",
    "AutoPathFormat_plaMonthDayHourMinute",
    "DataCollectorSetStatus",
    "DataCollectorSetStatus_plaStopped",
    "DataCollectorSetStatus_plaRunning",
    "DataCollectorSetStatus_plaCompiling",
    "DataCollectorSetStatus_plaPending",
    "DataCollectorSetStatus_plaUndefined",
    "ClockType",
    "ClockType_plaTimeStamp",
    "ClockType_plaPerformance",
    "ClockType_plaSystem",
    "ClockType_plaCycle",
    "StreamMode",
    "StreamMode_plaFile",
    "StreamMode_plaRealTime",
    "StreamMode_plaBoth",
    "StreamMode_plaBuffering",
    "CommitMode",
    "CommitMode_plaCreateNew",
    "CommitMode_plaModify",
    "CommitMode_plaCreateOrModify",
    "CommitMode_plaUpdateRunningInstance",
    "CommitMode_plaFlushTrace",
    "CommitMode_plaValidateOnly",
    "ValueMapType",
    "ValueMapType_plaIndex",
    "ValueMapType_plaFlag",
    "ValueMapType_plaFlagArray",
    "ValueMapType_plaValidation",
    "WeekDays",
    "WeekDays_plaRunOnce",
    "WeekDays_plaSunday",
    "WeekDays_plaMonday",
    "WeekDays_plaTuesday",
    "WeekDays_plaWednesday",
    "WeekDays_plaThursday",
    "WeekDays_plaFriday",
    "WeekDays_plaSaturday",
    "WeekDays_plaEveryday",
    "ResourcePolicy",
    "ResourcePolicy_plaDeleteLargest",
    "ResourcePolicy_plaDeleteOldest",
    "DataManagerSteps",
    "DataManagerSteps_plaCreateReport",
    "DataManagerSteps_plaRunRules",
    "DataManagerSteps_plaCreateHtml",
    "DataManagerSteps_plaFolderActions",
    "DataManagerSteps_plaResourceFreeing",
    "FolderActionSteps",
    "FolderActionSteps_plaCreateCab",
    "FolderActionSteps_plaDeleteData",
    "FolderActionSteps_plaSendCab",
    "FolderActionSteps_plaDeleteCab",
    "FolderActionSteps_plaDeleteReport",
    "PLA_CABEXTRACT_CALLBACK",
    "IDataCollectorSet",
    "IDataManager",
    "IFolderAction",
    "IFolderActionCollection",
    "IDataCollector",
    "IPerformanceCounterDataCollector",
    "ITraceDataCollector",
    "IConfigurationDataCollector",
    "IAlertDataCollector",
    "IApiTracingDataCollector",
    "IDataCollectorCollection",
    "IDataCollectorSetCollection",
    "ITraceDataProvider",
    "ITraceDataProviderCollection",
    "ISchedule",
    "IScheduleCollection",
    "IValueMapItem",
    "IValueMap",
    "PERF_COUNTERSET_INFO",
    "PERF_COUNTER_INFO",
    "PERF_COUNTERSET_INSTANCE",
    "PERF_COUNTER_IDENTITY",
    "PERFLIBREQUEST",
    "PERF_MEM_ALLOC",
    "PERF_MEM_FREE",
    "PERF_PROVIDER_CONTEXT",
    "PERF_INSTANCE_HEADER",
    "PerfRegInfoType",
    "PERF_REG_COUNTERSET_STRUCT",
    "PERF_REG_COUNTER_STRUCT",
    "PERF_REG_COUNTERSET_NAME_STRING",
    "PERF_REG_COUNTERSET_HELP_STRING",
    "PERF_REG_COUNTER_NAME_STRINGS",
    "PERF_REG_COUNTER_HELP_STRINGS",
    "PERF_REG_PROVIDER_NAME",
    "PERF_REG_PROVIDER_GUID",
    "PERF_REG_COUNTERSET_ENGLISH_NAME",
    "PERF_REG_COUNTER_ENGLISH_NAMES",
    "PERF_COUNTERSET_REG_INFO",
    "PERF_COUNTER_REG_INFO",
    "PERF_STRING_BUFFER_HEADER",
    "PERF_STRING_COUNTER_HEADER",
    "PERF_COUNTER_IDENTIFIER",
    "PERF_DATA_HEADER",
    "PerfCounterDataType",
    "PERF_ERROR_RETURN",
    "PERF_SINGLE_COUNTER",
    "PERF_MULTIPLE_COUNTERS",
    "PERF_MULTIPLE_INSTANCES",
    "PERF_COUNTERSET",
    "PERF_COUNTER_HEADER",
    "PERF_MULTI_INSTANCES",
    "PERF_MULTI_COUNTERS",
    "PERF_COUNTER_DATA",
    "PERF_DATA_BLOCK",
    "PERF_OBJECT_TYPE",
    "PERF_COUNTER_DEFINITION",
    "PERF_INSTANCE_DEFINITION",
    "PERF_COUNTER_BLOCK",
    "PM_OPEN_PROC",
    "PM_COLLECT_PROC",
    "PM_CLOSE_PROC",
    "PDH_RAW_COUNTER",
    "PDH_RAW_COUNTER_ITEM_A",
    "PDH_RAW_COUNTER_ITEM_W",
    "PDH_FMT_COUNTERVALUE",
    "PDH_FMT_COUNTERVALUE_ITEM_A",
    "PDH_FMT_COUNTERVALUE_ITEM_W",
    "PDH_STATISTICS",
    "PDH_COUNTER_PATH_ELEMENTS_A",
    "PDH_COUNTER_PATH_ELEMENTS_W",
    "PDH_DATA_ITEM_PATH_ELEMENTS_A",
    "PDH_DATA_ITEM_PATH_ELEMENTS_W",
    "PDH_COUNTER_INFO_A",
    "PDH_COUNTER_INFO_W",
    "PDH_TIME_INFO",
    "PDH_RAW_LOG_RECORD",
    "PDH_LOG_SERVICE_QUERY_INFO_A",
    "PDH_LOG_SERVICE_QUERY_INFO_W",
    "CounterPathCallBack",
    "PDH_BROWSE_DLG_CONFIG_HW",
    "PDH_BROWSE_DLG_CONFIG_HA",
    "PDH_BROWSE_DLG_CONFIG_W",
    "PDH_BROWSE_DLG_CONFIG_A",
    "SystemMonitor",
    "CounterItem",
    "Counters",
    "LogFileItem",
    "LogFiles",
    "CounterItem2",
    "SystemMonitor2",
    "AppearPropPage",
    "GeneralPropPage",
    "GraphPropPage",
    "SourcePropPage",
    "CounterPropPage",
    "DisplayTypeConstants",
    "DisplayTypeConstants_sysmonLineGraph",
    "DisplayTypeConstants_sysmonHistogram",
    "DisplayTypeConstants_sysmonReport",
    "DisplayTypeConstants_sysmonChartArea",
    "DisplayTypeConstants_sysmonChartStackedArea",
    "ReportValueTypeConstants",
    "ReportValueTypeConstants_sysmonDefaultValue",
    "ReportValueTypeConstants_sysmonCurrentValue",
    "ReportValueTypeConstants_sysmonAverage",
    "ReportValueTypeConstants_sysmonMinimum",
    "ReportValueTypeConstants_sysmonMaximum",
    "DataSourceTypeConstants",
    "DataSourceTypeConstants_sysmonNullDataSource",
    "DataSourceTypeConstants_sysmonCurrentActivity",
    "DataSourceTypeConstants_sysmonLogFiles",
    "DataSourceTypeConstants_sysmonSqlLog",
    "SysmonFileType",
    "SysmonFileType_sysmonFileHtml",
    "SysmonFileType_sysmonFileReport",
    "SysmonFileType_sysmonFileCsv",
    "SysmonFileType_sysmonFileTsv",
    "SysmonFileType_sysmonFileBlg",
    "SysmonFileType_sysmonFileRetiredBlg",
    "SysmonFileType_sysmonFileGif",
    "SysmonDataType",
    "SysmonDataType_sysmonDataAvg",
    "SysmonDataType_sysmonDataMin",
    "SysmonDataType_sysmonDataMax",
    "SysmonDataType_sysmonDataTime",
    "SysmonDataType_sysmonDataCount",
    "SysmonBatchReason",
    "SysmonBatchReason_sysmonBatchNone",
    "SysmonBatchReason_sysmonBatchAddFiles",
    "SysmonBatchReason_sysmonBatchAddCounters",
    "SysmonBatchReason_sysmonBatchAddFilesAutoCounters",
    "ICounterItem",
    "ICounterItem2",
    "_ICounterItemUnion",
    "DICounterItem",
    "ICounters",
    "ILogFileItem",
    "DILogFileItem",
    "ILogFiles",
    "ISystemMonitor",
    "ISystemMonitor2",
    "_ISystemMonitorUnion",
    "DISystemMonitor",
    "DISystemMonitorInternal",
    "ISystemMonitorEvents",
    "DISystemMonitorEvents",
    "QueryPerformanceCounter",
    "QueryPerformanceFrequency",
    "InstallPerfDllW",
    "InstallPerfDll",
    "InstallPerfDllA",
    "LoadPerfCounterTextStringsA",
    "LoadPerfCounterTextStringsW",
    "LoadPerfCounterTextStrings",
    "UnloadPerfCounterTextStringsW",
    "UnloadPerfCounterTextStrings",
    "UnloadPerfCounterTextStringsA",
    "UpdatePerfNameFilesA",
    "UpdatePerfNameFilesW",
    "UpdatePerfNameFiles",
    "SetServiceAsTrustedA",
    "SetServiceAsTrustedW",
    "SetServiceAsTrusted",
    "BackupPerfRegistryToFileW",
    "RestorePerfRegistryFromFileW",
    "PerfStartProvider",
    "PerfStartProviderEx",
    "PerfStopProvider",
    "PerfSetCounterSetInfo",
    "PerfCreateInstance",
    "PerfDeleteInstance",
    "PerfQueryInstance",
    "PerfSetCounterRefValue",
    "PerfSetULongCounterValue",
    "PerfSetULongLongCounterValue",
    "PerfIncrementULongCounterValue",
    "PerfIncrementULongLongCounterValue",
    "PerfDecrementULongCounterValue",
    "PerfDecrementULongLongCounterValue",
    "PerfEnumerateCounterSet",
    "PerfEnumerateCounterSetInstances",
    "PerfQueryCounterSetRegistrationInfo",
    "PerfOpenQueryHandle",
    "PerfCloseQueryHandle",
    "PerfQueryCounterInfo",
    "PerfQueryCounterData",
    "PerfAddCounters",
    "PerfDeleteCounters",
    "PdhGetDllVersion",
    "PdhOpenQueryW",
    "PdhOpenQuery",
    "PdhOpenQueryA",
    "PdhAddCounterW",
    "PdhAddCounter",
    "PdhAddCounterA",
    "PdhAddEnglishCounterW",
    "PdhAddEnglishCounter",
    "PdhAddEnglishCounterA",
    "PdhCollectQueryDataWithTime",
    "PdhValidatePathExW",
    "PdhValidatePathEx",
    "PdhValidatePathExA",
    "PdhRemoveCounter",
    "PdhCollectQueryData",
    "PdhCloseQuery",
    "PdhGetFormattedCounterValue",
    "PdhGetFormattedCounterArrayA",
    "PdhGetFormattedCounterArrayW",
    "PdhGetFormattedCounterArray",
    "PdhGetRawCounterValue",
    "PdhGetRawCounterArrayA",
    "PdhGetRawCounterArrayW",
    "PdhGetRawCounterArray",
    "PdhCalculateCounterFromRawValue",
    "PdhComputeCounterStatistics",
    "PdhGetCounterInfoW",
    "PdhGetCounterInfo",
    "PdhGetCounterInfoA",
    "PdhSetCounterScaleFactor",
    "PdhConnectMachineW",
    "PdhConnectMachine",
    "PdhConnectMachineA",
    "PdhEnumMachinesW",
    "PdhEnumMachines",
    "PdhEnumMachinesA",
    "PdhEnumObjectsW",
    "PdhEnumObjects",
    "PdhEnumObjectsA",
    "PdhEnumObjectItemsW",
    "PdhEnumObjectItems",
    "PdhEnumObjectItemsA",
    "PdhMakeCounterPathW",
    "PdhMakeCounterPath",
    "PdhMakeCounterPathA",
    "PdhParseCounterPathW",
    "PdhParseCounterPath",
    "PdhParseCounterPathA",
    "PdhParseInstanceNameW",
    "PdhParseInstanceName",
    "PdhParseInstanceNameA",
    "PdhValidatePathW",
    "PdhValidatePath",
    "PdhValidatePathA",
    "PdhGetDefaultPerfObjectW",
    "PdhGetDefaultPerfObject",
    "PdhGetDefaultPerfObjectA",
    "PdhGetDefaultPerfCounterW",
    "PdhGetDefaultPerfCounter",
    "PdhGetDefaultPerfCounterA",
    "PdhBrowseCountersW",
    "PdhBrowseCounters",
    "PdhBrowseCountersA",
    "PdhExpandCounterPathW",
    "PdhExpandCounterPath",
    "PdhExpandCounterPathA",
    "PdhLookupPerfNameByIndexW",
    "PdhLookupPerfNameByIndex",
    "PdhLookupPerfNameByIndexA",
    "PdhLookupPerfIndexByNameW",
    "PdhLookupPerfIndexByName",
    "PdhLookupPerfIndexByNameA",
    "PdhExpandWildCardPathA",
    "PdhExpandWildCardPathW",
    "PdhExpandWildCardPath",
    "PdhOpenLogW",
    "PdhOpenLog",
    "PdhOpenLogA",
    "PdhUpdateLogW",
    "PdhUpdateLog",
    "PdhUpdateLogA",
    "PdhUpdateLogFileCatalog",
    "PdhGetLogFileSize",
    "PdhCloseLog",
    "PdhSelectDataSourceW",
    "PdhSelectDataSource",
    "PdhSelectDataSourceA",
    "PdhIsRealTimeQuery",
    "PdhSetQueryTimeRange",
    "PdhGetDataSourceTimeRangeW",
    "PdhGetDataSourceTimeRange",
    "PdhGetDataSourceTimeRangeA",
    "PdhCollectQueryDataEx",
    "PdhFormatFromRawValue",
    "PdhGetCounterTimeBase",
    "PdhReadRawLogRecord",
    "PdhSetDefaultRealTimeDataSource",
    "PdhBindInputDataSourceW",
    "PdhBindInputDataSource",
    "PdhBindInputDataSourceA",
    "PdhOpenQueryH",
    "PdhEnumMachinesHW",
    "PdhEnumMachinesH",
    "PdhEnumMachinesHA",
    "PdhEnumObjectsHW",
    "PdhEnumObjectsH",
    "PdhEnumObjectsHA",
    "PdhEnumObjectItemsHW",
    "PdhEnumObjectItemsH",
    "PdhEnumObjectItemsHA",
    "PdhExpandWildCardPathHW",
    "PdhExpandWildCardPathH",
    "PdhExpandWildCardPathHA",
    "PdhGetDataSourceTimeRangeH",
    "PdhGetDefaultPerfObjectHW",
    "PdhGetDefaultPerfObjectH",
    "PdhGetDefaultPerfObjectHA",
    "PdhGetDefaultPerfCounterHW",
    "PdhGetDefaultPerfCounterH",
    "PdhGetDefaultPerfCounterHA",
    "PdhBrowseCountersHW",
    "PdhBrowseCountersH",
    "PdhBrowseCountersHA",
    "PdhVerifySQLDBW",
    "PdhVerifySQLDB",
    "PdhVerifySQLDBA",
    "PdhCreateSQLTablesW",
    "PdhCreateSQLTables",
    "PdhCreateSQLTablesA",
    "PdhEnumLogSetNamesW",
    "PdhEnumLogSetNames",
    "PdhEnumLogSetNamesA",
    "PdhGetLogSetGUID",
    "PdhSetLogSetRunID",
]
