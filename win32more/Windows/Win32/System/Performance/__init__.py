from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Ole
import win32more.Windows.Win32.System.Performance
import win32more.Windows.Win32.System.Variant
MAX_COUNTER_PATH: UInt32 = 256
PDH_MAX_COUNTER_NAME: UInt32 = 1024
PDH_MAX_INSTANCE_NAME: UInt32 = 1024
PDH_MAX_COUNTER_PATH: UInt32 = 2048
PDH_MAX_DATASOURCE_PATH: UInt32 = 1024
H_WBEM_DATASOURCE: Int32 = -1
PDH_MAX_SCALE: Int32 = 7
PDH_MIN_SCALE: Int32 = -7
PDH_NOEXPANDCOUNTERS: UInt32 = 1
PDH_NOEXPANDINSTANCES: UInt32 = 2
PDH_REFRESHCOUNTERS: UInt32 = 4
PDH_LOG_TYPE_RETIRED_BIN: UInt32 = 3
PDH_LOG_TYPE_TRACE_KERNEL: UInt32 = 4
PDH_LOG_TYPE_TRACE_GENERIC: UInt32 = 5
PERF_PROVIDER_USER_MODE: UInt32 = 0
PERF_PROVIDER_KERNEL_MODE: UInt32 = 1
PERF_PROVIDER_DRIVER: UInt32 = 2
PERF_COUNTERSET_FLAG_MULTIPLE: UInt32 = 2
PERF_COUNTERSET_FLAG_AGGREGATE: UInt32 = 4
PERF_COUNTERSET_FLAG_HISTORY: UInt32 = 8
PERF_COUNTERSET_FLAG_INSTANCE: UInt32 = 16
PERF_COUNTERSET_SINGLE_INSTANCE: UInt32 = 0
PERF_COUNTERSET_MULTI_INSTANCES: UInt32 = 2
PERF_COUNTERSET_SINGLE_AGGREGATE: UInt32 = 4
PERF_ATTRIB_BY_REFERENCE: UInt64 = 1
PERF_ATTRIB_NO_DISPLAYABLE: UInt64 = 2
PERF_ATTRIB_NO_GROUP_SEPARATOR: UInt64 = 4
PERF_ATTRIB_DISPLAY_AS_REAL: UInt64 = 8
PERF_ATTRIB_DISPLAY_AS_HEX: UInt64 = 16
PERF_WILDCARD_COUNTER: UInt32 = 4294967295
PERF_WILDCARD_INSTANCE: String = '*'
PERF_AGGREGATE_INSTANCE: String = '_Total'
PERF_MAX_INSTANCE_NAME: UInt32 = 1024
PERF_ADD_COUNTER: UInt32 = 1
PERF_REMOVE_COUNTER: UInt32 = 2
PERF_ENUM_INSTANCES: UInt32 = 3
PERF_COLLECT_START: UInt32 = 5
PERF_COLLECT_END: UInt32 = 6
PERF_FILTER: UInt32 = 9
PERF_DATA_VERSION: UInt32 = 1
PERF_DATA_REVISION: UInt32 = 1
PERF_NO_INSTANCES: Int32 = -1
PERF_METADATA_MULTIPLE_INSTANCES: Int32 = -2
PERF_METADATA_NO_INSTANCES: Int32 = -3
PERF_SIZE_DWORD: UInt32 = 0
PERF_SIZE_LARGE: UInt32 = 256
PERF_SIZE_ZERO: UInt32 = 512
PERF_SIZE_VARIABLE_LEN: UInt32 = 768
PERF_TYPE_NUMBER: UInt32 = 0
PERF_TYPE_COUNTER: UInt32 = 1024
PERF_TYPE_TEXT: UInt32 = 2048
PERF_TYPE_ZERO: UInt32 = 3072
PERF_NUMBER_HEX: UInt32 = 0
PERF_NUMBER_DECIMAL: UInt32 = 65536
PERF_NUMBER_DEC_1000: UInt32 = 131072
PERF_COUNTER_VALUE: UInt32 = 0
PERF_COUNTER_RATE: UInt32 = 65536
PERF_COUNTER_FRACTION: UInt32 = 131072
PERF_COUNTER_BASE: UInt32 = 196608
PERF_COUNTER_ELAPSED: UInt32 = 262144
PERF_COUNTER_QUEUELEN: UInt32 = 327680
PERF_COUNTER_HISTOGRAM: UInt32 = 393216
PERF_COUNTER_PRECISION: UInt32 = 458752
PERF_TEXT_UNICODE: UInt32 = 0
PERF_TEXT_ASCII: UInt32 = 65536
PERF_TIMER_TICK: UInt32 = 0
PERF_TIMER_100NS: UInt32 = 1048576
PERF_OBJECT_TIMER: UInt32 = 2097152
PERF_DELTA_COUNTER: UInt32 = 4194304
PERF_DELTA_BASE: UInt32 = 8388608
PERF_INVERSE_COUNTER: UInt32 = 16777216
PERF_MULTI_COUNTER: UInt32 = 33554432
PERF_DISPLAY_NO_SUFFIX: UInt32 = 0
PERF_DISPLAY_PER_SEC: UInt32 = 268435456
PERF_DISPLAY_PERCENT: UInt32 = 536870912
PERF_DISPLAY_SECONDS: UInt32 = 805306368
PERF_DISPLAY_NOSHOW: UInt32 = 1073741824
PERF_COUNTER_HISTOGRAM_TYPE: UInt32 = 2147483648
PERF_NO_UNIQUE_ID: Int32 = -1
MAX_PERF_OBJECTS_IN_QUERY_FUNCTION: Int32 = 64
WINPERF_LOG_NONE: UInt32 = 0
WINPERF_LOG_USER: UInt32 = 1
WINPERF_LOG_DEBUG: UInt32 = 2
WINPERF_LOG_VERBOSE: UInt32 = 3
LIBID_SystemMonitor: Guid = Guid('{1b773e42-2509-11cf-942f-008029004347}')
DIID_DICounterItem: Guid = Guid('{c08c4ff2-0e2e-11cf-942c-008029004347}')
DIID_DILogFileItem: Guid = Guid('{8d093ffc-f777-4917-82d1-833fbc54c58f}')
DIID_DISystemMonitor: Guid = Guid('{13d73d81-c32e-11cf-9398-00aa00a3ddea}')
DIID_DISystemMonitorInternal: Guid = Guid('{194eb242-c32c-11cf-9398-00aa00a3ddea}')
DIID_DISystemMonitorEvents: Guid = Guid('{84979930-4ab3-11cf-943a-008029004347}')
PDH_CSTATUS_VALID_DATA: UInt32 = 0
PDH_CSTATUS_NEW_DATA: UInt32 = 1
PDH_CSTATUS_NO_MACHINE: UInt32 = 2147485648
PDH_CSTATUS_NO_INSTANCE: UInt32 = 2147485649
PDH_MORE_DATA: UInt32 = 2147485650
PDH_CSTATUS_ITEM_NOT_VALIDATED: UInt32 = 2147485651
PDH_RETRY: UInt32 = 2147485652
PDH_NO_DATA: UInt32 = 2147485653
PDH_CALC_NEGATIVE_DENOMINATOR: UInt32 = 2147485654
PDH_CALC_NEGATIVE_TIMEBASE: UInt32 = 2147485655
PDH_CALC_NEGATIVE_VALUE: UInt32 = 2147485656
PDH_DIALOG_CANCELLED: UInt32 = 2147485657
PDH_END_OF_LOG_FILE: UInt32 = 2147485658
PDH_ASYNC_QUERY_TIMEOUT: UInt32 = 2147485659
PDH_CANNOT_SET_DEFAULT_REALTIME_DATASOURCE: UInt32 = 2147485660
PDH_UNABLE_MAP_NAME_FILES: UInt32 = 2147486677
PDH_PLA_VALIDATION_WARNING: UInt32 = 2147486707
PDH_CSTATUS_NO_OBJECT: UInt32 = 3221228472
PDH_CSTATUS_NO_COUNTER: UInt32 = 3221228473
PDH_CSTATUS_INVALID_DATA: UInt32 = 3221228474
PDH_MEMORY_ALLOCATION_FAILURE: UInt32 = 3221228475
PDH_INVALID_HANDLE: UInt32 = 3221228476
PDH_INVALID_ARGUMENT: UInt32 = 3221228477
PDH_FUNCTION_NOT_FOUND: UInt32 = 3221228478
PDH_CSTATUS_NO_COUNTERNAME: UInt32 = 3221228479
PDH_CSTATUS_BAD_COUNTERNAME: UInt32 = 3221228480
PDH_INVALID_BUFFER: UInt32 = 3221228481
PDH_INSUFFICIENT_BUFFER: UInt32 = 3221228482
PDH_CANNOT_CONNECT_MACHINE: UInt32 = 3221228483
PDH_INVALID_PATH: UInt32 = 3221228484
PDH_INVALID_INSTANCE: UInt32 = 3221228485
PDH_INVALID_DATA: UInt32 = 3221228486
PDH_NO_DIALOG_DATA: UInt32 = 3221228487
PDH_CANNOT_READ_NAME_STRINGS: UInt32 = 3221228488
PDH_LOG_FILE_CREATE_ERROR: UInt32 = 3221228489
PDH_LOG_FILE_OPEN_ERROR: UInt32 = 3221228490
PDH_LOG_TYPE_NOT_FOUND: UInt32 = 3221228491
PDH_NO_MORE_DATA: UInt32 = 3221228492
PDH_ENTRY_NOT_IN_LOG_FILE: UInt32 = 3221228493
PDH_DATA_SOURCE_IS_LOG_FILE: UInt32 = 3221228494
PDH_DATA_SOURCE_IS_REAL_TIME: UInt32 = 3221228495
PDH_UNABLE_READ_LOG_HEADER: UInt32 = 3221228496
PDH_FILE_NOT_FOUND: UInt32 = 3221228497
PDH_FILE_ALREADY_EXISTS: UInt32 = 3221228498
PDH_NOT_IMPLEMENTED: UInt32 = 3221228499
PDH_STRING_NOT_FOUND: UInt32 = 3221228500
PDH_UNKNOWN_LOG_FORMAT: UInt32 = 3221228502
PDH_UNKNOWN_LOGSVC_COMMAND: UInt32 = 3221228503
PDH_LOGSVC_QUERY_NOT_FOUND: UInt32 = 3221228504
PDH_LOGSVC_NOT_OPENED: UInt32 = 3221228505
PDH_WBEM_ERROR: UInt32 = 3221228506
PDH_ACCESS_DENIED: UInt32 = 3221228507
PDH_LOG_FILE_TOO_SMALL: UInt32 = 3221228508
PDH_INVALID_DATASOURCE: UInt32 = 3221228509
PDH_INVALID_SQLDB: UInt32 = 3221228510
PDH_NO_COUNTERS: UInt32 = 3221228511
PDH_SQL_ALLOC_FAILED: UInt32 = 3221228512
PDH_SQL_ALLOCCON_FAILED: UInt32 = 3221228513
PDH_SQL_EXEC_DIRECT_FAILED: UInt32 = 3221228514
PDH_SQL_FETCH_FAILED: UInt32 = 3221228515
PDH_SQL_ROWCOUNT_FAILED: UInt32 = 3221228516
PDH_SQL_MORE_RESULTS_FAILED: UInt32 = 3221228517
PDH_SQL_CONNECT_FAILED: UInt32 = 3221228518
PDH_SQL_BIND_FAILED: UInt32 = 3221228519
PDH_CANNOT_CONNECT_WMI_SERVER: UInt32 = 3221228520
PDH_PLA_COLLECTION_ALREADY_RUNNING: UInt32 = 3221228521
PDH_PLA_ERROR_SCHEDULE_OVERLAP: UInt32 = 3221228522
PDH_PLA_COLLECTION_NOT_FOUND: UInt32 = 3221228523
PDH_PLA_ERROR_SCHEDULE_ELAPSED: UInt32 = 3221228524
PDH_PLA_ERROR_NOSTART: UInt32 = 3221228525
PDH_PLA_ERROR_ALREADY_EXISTS: UInt32 = 3221228526
PDH_PLA_ERROR_TYPE_MISMATCH: UInt32 = 3221228527
PDH_PLA_ERROR_FILEPATH: UInt32 = 3221228528
PDH_PLA_SERVICE_ERROR: UInt32 = 3221228529
PDH_PLA_VALIDATION_ERROR: UInt32 = 3221228530
PDH_PLA_ERROR_NAME_TOO_LONG: UInt32 = 3221228532
PDH_INVALID_SQL_LOG_FORMAT: UInt32 = 3221228533
PDH_COUNTER_ALREADY_IN_QUERY: UInt32 = 3221228534
PDH_BINARY_LOG_CORRUPT: UInt32 = 3221228535
PDH_LOG_SAMPLE_TOO_SMALL: UInt32 = 3221228536
PDH_OS_LATER_VERSION: UInt32 = 3221228537
PDH_OS_EARLIER_VERSION: UInt32 = 3221228538
PDH_INCORRECT_APPEND_TIME: UInt32 = 3221228539
PDH_UNMATCHED_APPEND_COUNTER: UInt32 = 3221228540
PDH_SQL_ALTER_DETAIL_FAILED: UInt32 = 3221228541
PDH_QUERY_PERF_DATA_TIMEOUT: UInt32 = 3221228542
PLA_CAPABILITY_LOCAL: UInt32 = 268435456
PLA_CAPABILITY_V1_SVC: UInt32 = 1
PLA_CAPABILITY_V1_SESSION: UInt32 = 2
PLA_CAPABILITY_V1_SYSTEM: UInt32 = 4
PLA_CAPABILITY_LEGACY_SESSION: UInt32 = 8
PLA_CAPABILITY_LEGACY_SVC: UInt32 = 16
PLA_CAPABILITY_AUTOLOGGER: UInt32 = 32
PLAL_ALERT_CMD_LINE_SINGLE: UInt32 = 256
PLAL_ALERT_CMD_LINE_A_NAME: UInt32 = 512
PLAL_ALERT_CMD_LINE_C_NAME: UInt32 = 1024
PLAL_ALERT_CMD_LINE_D_TIME: UInt32 = 2048
PLAL_ALERT_CMD_LINE_L_VAL: UInt32 = 4096
PLAL_ALERT_CMD_LINE_M_VAL: UInt32 = 8192
PLAL_ALERT_CMD_LINE_U_TEXT: UInt32 = 16384
PLAL_ALERT_CMD_LINE_MASK: UInt32 = 32512
S_PDH: Guid = Guid('{04d66358-c4a1-419b-8023-23b73902de2c}')
@winfunctype('KERNEL32.dll')
def QueryPerformanceCounter(lpPerformanceCount: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryPerformanceFrequency(lpFrequency: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('loadperf.dll')
def InstallPerfDllW(szComputerName: win32more.Windows.Win32.Foundation.PWSTR, lpIniFile: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UIntPtr) -> UInt32: ...
InstallPerfDll = UnicodeAlias('InstallPerfDllW')
@winfunctype('loadperf.dll')
def InstallPerfDllA(szComputerName: win32more.Windows.Win32.Foundation.PSTR, lpIniFile: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UIntPtr) -> UInt32: ...
@winfunctype('loadperf.dll')
def LoadPerfCounterTextStringsA(lpCommandLine: win32more.Windows.Win32.Foundation.PSTR, bQuietModeArg: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('loadperf.dll')
def LoadPerfCounterTextStringsW(lpCommandLine: win32more.Windows.Win32.Foundation.PWSTR, bQuietModeArg: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
LoadPerfCounterTextStrings = UnicodeAlias('LoadPerfCounterTextStringsW')
@winfunctype('loadperf.dll')
def UnloadPerfCounterTextStringsW(lpCommandLine: win32more.Windows.Win32.Foundation.PWSTR, bQuietModeArg: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
UnloadPerfCounterTextStrings = UnicodeAlias('UnloadPerfCounterTextStringsW')
@winfunctype('loadperf.dll')
def UnloadPerfCounterTextStringsA(lpCommandLine: win32more.Windows.Win32.Foundation.PSTR, bQuietModeArg: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('loadperf.dll')
def UpdatePerfNameFilesA(szNewCtrFilePath: win32more.Windows.Win32.Foundation.PSTR, szNewHlpFilePath: win32more.Windows.Win32.Foundation.PSTR, szLanguageID: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UIntPtr) -> UInt32: ...
@winfunctype('loadperf.dll')
def UpdatePerfNameFilesW(szNewCtrFilePath: win32more.Windows.Win32.Foundation.PWSTR, szNewHlpFilePath: win32more.Windows.Win32.Foundation.PWSTR, szLanguageID: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UIntPtr) -> UInt32: ...
UpdatePerfNameFiles = UnicodeAlias('UpdatePerfNameFilesW')
@winfunctype('loadperf.dll')
def SetServiceAsTrustedA(szReserved: win32more.Windows.Win32.Foundation.PSTR, szServiceName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('loadperf.dll')
def SetServiceAsTrustedW(szReserved: win32more.Windows.Win32.Foundation.PWSTR, szServiceName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
SetServiceAsTrusted = UnicodeAlias('SetServiceAsTrustedW')
@winfunctype('loadperf.dll')
def BackupPerfRegistryToFileW(szFileName: win32more.Windows.Win32.Foundation.PWSTR, szCommentString: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('loadperf.dll')
def RestorePerfRegistryFromFileW(szFileName: win32more.Windows.Win32.Foundation.PWSTR, szLangId: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfStartProvider(ProviderGuid: POINTER(Guid), ControlCallback: win32more.Windows.Win32.System.Performance.PERFLIBREQUEST, phProvider: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfStartProviderEx(ProviderGuid: POINTER(Guid), ProviderContext: POINTER(win32more.Windows.Win32.System.Performance.PERF_PROVIDER_CONTEXT), Provider: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfStopProvider(ProviderHandle: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfSetCounterSetInfo(ProviderHandle: win32more.Windows.Win32.Foundation.HANDLE, Template: POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTERSET_INFO), TemplateSize: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfCreateInstance(ProviderHandle: win32more.Windows.Win32.Foundation.HANDLE, CounterSetGuid: POINTER(Guid), Name: win32more.Windows.Win32.Foundation.PWSTR, Id: UInt32) -> POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE): ...
@winfunctype('ADVAPI32.dll')
def PerfDeleteInstance(Provider: win32more.Windows.Win32.Foundation.HANDLE, InstanceBlock: POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfQueryInstance(ProviderHandle: win32more.Windows.Win32.Foundation.HANDLE, CounterSetGuid: POINTER(Guid), Name: win32more.Windows.Win32.Foundation.PWSTR, Id: UInt32) -> POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE): ...
@winfunctype('ADVAPI32.dll')
def PerfSetCounterRefValue(Provider: win32more.Windows.Win32.Foundation.HANDLE, Instance: POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE), CounterId: UInt32, Address: VoidPtr) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfSetULongCounterValue(Provider: win32more.Windows.Win32.Foundation.HANDLE, Instance: POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE), CounterId: UInt32, Value: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfSetULongLongCounterValue(Provider: win32more.Windows.Win32.Foundation.HANDLE, Instance: POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE), CounterId: UInt32, Value: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfIncrementULongCounterValue(Provider: win32more.Windows.Win32.Foundation.HANDLE, Instance: POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE), CounterId: UInt32, Value: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfIncrementULongLongCounterValue(Provider: win32more.Windows.Win32.Foundation.HANDLE, Instance: POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE), CounterId: UInt32, Value: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfDecrementULongCounterValue(Provider: win32more.Windows.Win32.Foundation.HANDLE, Instance: POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE), CounterId: UInt32, Value: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfDecrementULongLongCounterValue(Provider: win32more.Windows.Win32.Foundation.HANDLE, Instance: POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE), CounterId: UInt32, Value: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfEnumerateCounterSet(szMachine: win32more.Windows.Win32.Foundation.PWSTR, pCounterSetIds: POINTER(Guid), cCounterSetIds: UInt32, pcCounterSetIdsActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfEnumerateCounterSetInstances(szMachine: win32more.Windows.Win32.Foundation.PWSTR, pCounterSetId: POINTER(Guid), pInstances: POINTER(win32more.Windows.Win32.System.Performance.PERF_INSTANCE_HEADER), cbInstances: UInt32, pcbInstancesActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfQueryCounterSetRegistrationInfo(szMachine: win32more.Windows.Win32.Foundation.PWSTR, pCounterSetId: POINTER(Guid), requestCode: win32more.Windows.Win32.System.Performance.PerfRegInfoType, requestLangId: UInt32, pbRegInfo: POINTER(Byte), cbRegInfo: UInt32, pcbRegInfoActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfOpenQueryHandle(szMachine: win32more.Windows.Win32.Foundation.PWSTR, phQuery: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfCloseQueryHandle(hQuery: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfQueryCounterInfo(hQuery: win32more.Windows.Win32.Foundation.HANDLE, pCounters: POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTER_IDENTIFIER), cbCounters: UInt32, pcbCountersActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfQueryCounterData(hQuery: win32more.Windows.Win32.Foundation.HANDLE, pCounterBlock: POINTER(win32more.Windows.Win32.System.Performance.PERF_DATA_HEADER), cbCounterBlock: UInt32, pcbCounterBlockActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfAddCounters(hQuery: win32more.Windows.Win32.Foundation.HANDLE, pCounters: POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTER_IDENTIFIER), cbCounters: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfDeleteCounters(hQuery: win32more.Windows.Win32.Foundation.HANDLE, pCounters: POINTER(win32more.Windows.Win32.System.Performance.PERF_COUNTER_IDENTIFIER), cbCounters: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDllVersion(lpdwVersion: POINTER(win32more.Windows.Win32.System.Performance.PDH_DLL_VERSION)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhOpenQueryW(szDataSource: win32more.Windows.Win32.Foundation.PWSTR, dwUserData: UIntPtr, phQuery: POINTER(win32more.Windows.Win32.System.Performance.PDH_HQUERY)) -> UInt32: ...
PdhOpenQuery = UnicodeAlias('PdhOpenQueryW')
@winfunctype('pdh.dll')
def PdhOpenQueryA(szDataSource: win32more.Windows.Win32.Foundation.PSTR, dwUserData: UIntPtr, phQuery: POINTER(win32more.Windows.Win32.System.Performance.PDH_HQUERY)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhAddCounterW(hQuery: win32more.Windows.Win32.System.Performance.PDH_HQUERY, szFullCounterPath: win32more.Windows.Win32.Foundation.PWSTR, dwUserData: UIntPtr, phCounter: POINTER(win32more.Windows.Win32.System.Performance.PDH_HCOUNTER)) -> UInt32: ...
PdhAddCounter = UnicodeAlias('PdhAddCounterW')
@winfunctype('pdh.dll')
def PdhAddCounterA(hQuery: win32more.Windows.Win32.System.Performance.PDH_HQUERY, szFullCounterPath: win32more.Windows.Win32.Foundation.PSTR, dwUserData: UIntPtr, phCounter: POINTER(win32more.Windows.Win32.System.Performance.PDH_HCOUNTER)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhAddEnglishCounterW(hQuery: win32more.Windows.Win32.System.Performance.PDH_HQUERY, szFullCounterPath: win32more.Windows.Win32.Foundation.PWSTR, dwUserData: UIntPtr, phCounter: POINTER(win32more.Windows.Win32.System.Performance.PDH_HCOUNTER)) -> UInt32: ...
PdhAddEnglishCounter = UnicodeAlias('PdhAddEnglishCounterW')
@winfunctype('pdh.dll')
def PdhAddEnglishCounterA(hQuery: win32more.Windows.Win32.System.Performance.PDH_HQUERY, szFullCounterPath: win32more.Windows.Win32.Foundation.PSTR, dwUserData: UIntPtr, phCounter: POINTER(win32more.Windows.Win32.System.Performance.PDH_HCOUNTER)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCollectQueryDataWithTime(hQuery: win32more.Windows.Win32.System.Performance.PDH_HQUERY, pllTimeStamp: POINTER(Int64)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhValidatePathExW(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, szFullPathBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
PdhValidatePathEx = UnicodeAlias('PdhValidatePathExW')
@winfunctype('pdh.dll')
def PdhValidatePathExA(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, szFullPathBuffer: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhRemoveCounter(hCounter: win32more.Windows.Win32.System.Performance.PDH_HCOUNTER) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCollectQueryData(hQuery: win32more.Windows.Win32.System.Performance.PDH_HQUERY) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCloseQuery(hQuery: win32more.Windows.Win32.System.Performance.PDH_HQUERY) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetFormattedCounterValue(hCounter: win32more.Windows.Win32.System.Performance.PDH_HCOUNTER, dwFormat: win32more.Windows.Win32.System.Performance.PDH_FMT, lpdwType: POINTER(UInt32), pValue: POINTER(win32more.Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetFormattedCounterArrayA(hCounter: win32more.Windows.Win32.System.Performance.PDH_HCOUNTER, dwFormat: win32more.Windows.Win32.System.Performance.PDH_FMT, lpdwBufferSize: POINTER(UInt32), lpdwItemCount: POINTER(UInt32), ItemBuffer: POINTER(win32more.Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE_ITEM_A)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetFormattedCounterArrayW(hCounter: win32more.Windows.Win32.System.Performance.PDH_HCOUNTER, dwFormat: win32more.Windows.Win32.System.Performance.PDH_FMT, lpdwBufferSize: POINTER(UInt32), lpdwItemCount: POINTER(UInt32), ItemBuffer: POINTER(win32more.Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE_ITEM_W)) -> UInt32: ...
PdhGetFormattedCounterArray = UnicodeAlias('PdhGetFormattedCounterArrayW')
@winfunctype('pdh.dll')
def PdhGetRawCounterValue(hCounter: win32more.Windows.Win32.System.Performance.PDH_HCOUNTER, lpdwType: POINTER(UInt32), pValue: POINTER(win32more.Windows.Win32.System.Performance.PDH_RAW_COUNTER)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetRawCounterArrayA(hCounter: win32more.Windows.Win32.System.Performance.PDH_HCOUNTER, lpdwBufferSize: POINTER(UInt32), lpdwItemCount: POINTER(UInt32), ItemBuffer: POINTER(win32more.Windows.Win32.System.Performance.PDH_RAW_COUNTER_ITEM_A)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetRawCounterArrayW(hCounter: win32more.Windows.Win32.System.Performance.PDH_HCOUNTER, lpdwBufferSize: POINTER(UInt32), lpdwItemCount: POINTER(UInt32), ItemBuffer: POINTER(win32more.Windows.Win32.System.Performance.PDH_RAW_COUNTER_ITEM_W)) -> UInt32: ...
PdhGetRawCounterArray = UnicodeAlias('PdhGetRawCounterArrayW')
@winfunctype('pdh.dll')
def PdhCalculateCounterFromRawValue(hCounter: win32more.Windows.Win32.System.Performance.PDH_HCOUNTER, dwFormat: win32more.Windows.Win32.System.Performance.PDH_FMT, rawValue1: POINTER(win32more.Windows.Win32.System.Performance.PDH_RAW_COUNTER), rawValue2: POINTER(win32more.Windows.Win32.System.Performance.PDH_RAW_COUNTER), fmtValue: POINTER(win32more.Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhComputeCounterStatistics(hCounter: win32more.Windows.Win32.System.Performance.PDH_HCOUNTER, dwFormat: win32more.Windows.Win32.System.Performance.PDH_FMT, dwFirstEntry: UInt32, dwNumEntries: UInt32, lpRawValueArray: POINTER(win32more.Windows.Win32.System.Performance.PDH_RAW_COUNTER), data: POINTER(win32more.Windows.Win32.System.Performance.PDH_STATISTICS)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetCounterInfoW(hCounter: win32more.Windows.Win32.System.Performance.PDH_HCOUNTER, bRetrieveExplainText: win32more.Windows.Win32.Foundation.BOOLEAN, pdwBufferSize: POINTER(UInt32), lpBuffer: POINTER(win32more.Windows.Win32.System.Performance.PDH_COUNTER_INFO_W)) -> UInt32: ...
PdhGetCounterInfo = UnicodeAlias('PdhGetCounterInfoW')
@winfunctype('pdh.dll')
def PdhGetCounterInfoA(hCounter: win32more.Windows.Win32.System.Performance.PDH_HCOUNTER, bRetrieveExplainText: win32more.Windows.Win32.Foundation.BOOLEAN, pdwBufferSize: POINTER(UInt32), lpBuffer: POINTER(win32more.Windows.Win32.System.Performance.PDH_COUNTER_INFO_A)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSetCounterScaleFactor(hCounter: win32more.Windows.Win32.System.Performance.PDH_HCOUNTER, lFactor: Int32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhConnectMachineW(szMachineName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
PdhConnectMachine = UnicodeAlias('PdhConnectMachineW')
@winfunctype('pdh.dll')
def PdhConnectMachineA(szMachineName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumMachinesW(szDataSource: win32more.Windows.Win32.Foundation.PWSTR, mszMachineList: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
PdhEnumMachines = UnicodeAlias('PdhEnumMachinesW')
@winfunctype('pdh.dll')
def PdhEnumMachinesA(szDataSource: win32more.Windows.Win32.Foundation.PSTR, mszMachineList: win32more.Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectsW(szDataSource: win32more.Windows.Win32.Foundation.PWSTR, szMachineName: win32more.Windows.Win32.Foundation.PWSTR, mszObjectList: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32), dwDetailLevel: win32more.Windows.Win32.System.Performance.PERF_DETAIL, bRefresh: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
PdhEnumObjects = UnicodeAlias('PdhEnumObjectsW')
@winfunctype('pdh.dll')
def PdhEnumObjectsA(szDataSource: win32more.Windows.Win32.Foundation.PSTR, szMachineName: win32more.Windows.Win32.Foundation.PSTR, mszObjectList: win32more.Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32), dwDetailLevel: win32more.Windows.Win32.System.Performance.PERF_DETAIL, bRefresh: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectItemsW(szDataSource: win32more.Windows.Win32.Foundation.PWSTR, szMachineName: win32more.Windows.Win32.Foundation.PWSTR, szObjectName: win32more.Windows.Win32.Foundation.PWSTR, mszCounterList: win32more.Windows.Win32.Foundation.PWSTR, pcchCounterListLength: POINTER(UInt32), mszInstanceList: win32more.Windows.Win32.Foundation.PWSTR, pcchInstanceListLength: POINTER(UInt32), dwDetailLevel: win32more.Windows.Win32.System.Performance.PERF_DETAIL, dwFlags: UInt32) -> UInt32: ...
PdhEnumObjectItems = UnicodeAlias('PdhEnumObjectItemsW')
@winfunctype('pdh.dll')
def PdhEnumObjectItemsA(szDataSource: win32more.Windows.Win32.Foundation.PSTR, szMachineName: win32more.Windows.Win32.Foundation.PSTR, szObjectName: win32more.Windows.Win32.Foundation.PSTR, mszCounterList: win32more.Windows.Win32.Foundation.PSTR, pcchCounterListLength: POINTER(UInt32), mszInstanceList: win32more.Windows.Win32.Foundation.PSTR, pcchInstanceListLength: POINTER(UInt32), dwDetailLevel: win32more.Windows.Win32.System.Performance.PERF_DETAIL, dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhMakeCounterPathW(pCounterPathElements: POINTER(win32more.Windows.Win32.System.Performance.PDH_COUNTER_PATH_ELEMENTS_W), szFullPathBuffer: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32), dwFlags: win32more.Windows.Win32.System.Performance.PDH_PATH_FLAGS) -> UInt32: ...
PdhMakeCounterPath = UnicodeAlias('PdhMakeCounterPathW')
@winfunctype('pdh.dll')
def PdhMakeCounterPathA(pCounterPathElements: POINTER(win32more.Windows.Win32.System.Performance.PDH_COUNTER_PATH_ELEMENTS_A), szFullPathBuffer: win32more.Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32), dwFlags: win32more.Windows.Win32.System.Performance.PDH_PATH_FLAGS) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhParseCounterPathW(szFullPathBuffer: win32more.Windows.Win32.Foundation.PWSTR, pCounterPathElements: POINTER(win32more.Windows.Win32.System.Performance.PDH_COUNTER_PATH_ELEMENTS_W), pdwBufferSize: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
PdhParseCounterPath = UnicodeAlias('PdhParseCounterPathW')
@winfunctype('pdh.dll')
def PdhParseCounterPathA(szFullPathBuffer: win32more.Windows.Win32.Foundation.PSTR, pCounterPathElements: POINTER(win32more.Windows.Win32.System.Performance.PDH_COUNTER_PATH_ELEMENTS_A), pdwBufferSize: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhParseInstanceNameW(szInstanceString: win32more.Windows.Win32.Foundation.PWSTR, szInstanceName: win32more.Windows.Win32.Foundation.PWSTR, pcchInstanceNameLength: POINTER(UInt32), szParentName: win32more.Windows.Win32.Foundation.PWSTR, pcchParentNameLength: POINTER(UInt32), lpIndex: POINTER(UInt32)) -> UInt32: ...
PdhParseInstanceName = UnicodeAlias('PdhParseInstanceNameW')
@winfunctype('pdh.dll')
def PdhParseInstanceNameA(szInstanceString: win32more.Windows.Win32.Foundation.PSTR, szInstanceName: win32more.Windows.Win32.Foundation.PSTR, pcchInstanceNameLength: POINTER(UInt32), szParentName: win32more.Windows.Win32.Foundation.PSTR, pcchParentNameLength: POINTER(UInt32), lpIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhValidatePathW(szFullPathBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
PdhValidatePath = UnicodeAlias('PdhValidatePathW')
@winfunctype('pdh.dll')
def PdhValidatePathA(szFullPathBuffer: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfObjectW(szDataSource: win32more.Windows.Win32.Foundation.PWSTR, szMachineName: win32more.Windows.Win32.Foundation.PWSTR, szDefaultObjectName: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
PdhGetDefaultPerfObject = UnicodeAlias('PdhGetDefaultPerfObjectW')
@winfunctype('pdh.dll')
def PdhGetDefaultPerfObjectA(szDataSource: win32more.Windows.Win32.Foundation.PSTR, szMachineName: win32more.Windows.Win32.Foundation.PSTR, szDefaultObjectName: win32more.Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfCounterW(szDataSource: win32more.Windows.Win32.Foundation.PWSTR, szMachineName: win32more.Windows.Win32.Foundation.PWSTR, szObjectName: win32more.Windows.Win32.Foundation.PWSTR, szDefaultCounterName: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
PdhGetDefaultPerfCounter = UnicodeAlias('PdhGetDefaultPerfCounterW')
@winfunctype('pdh.dll')
def PdhGetDefaultPerfCounterA(szDataSource: win32more.Windows.Win32.Foundation.PSTR, szMachineName: win32more.Windows.Win32.Foundation.PSTR, szObjectName: win32more.Windows.Win32.Foundation.PSTR, szDefaultCounterName: win32more.Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBrowseCountersW(pBrowseDlgData: POINTER(win32more.Windows.Win32.System.Performance.PDH_BROWSE_DLG_CONFIG_W)) -> UInt32: ...
PdhBrowseCounters = UnicodeAlias('PdhBrowseCountersW')
@winfunctype('pdh.dll')
def PdhBrowseCountersA(pBrowseDlgData: POINTER(win32more.Windows.Win32.System.Performance.PDH_BROWSE_DLG_CONFIG_A)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandCounterPathW(szWildCardPath: win32more.Windows.Win32.Foundation.PWSTR, mszExpandedPathList: win32more.Windows.Win32.Foundation.PWSTR, pcchPathListLength: POINTER(UInt32)) -> UInt32: ...
PdhExpandCounterPath = UnicodeAlias('PdhExpandCounterPathW')
@winfunctype('pdh.dll')
def PdhExpandCounterPathA(szWildCardPath: win32more.Windows.Win32.Foundation.PSTR, mszExpandedPathList: win32more.Windows.Win32.Foundation.PSTR, pcchPathListLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhLookupPerfNameByIndexW(szMachineName: win32more.Windows.Win32.Foundation.PWSTR, dwNameIndex: UInt32, szNameBuffer: win32more.Windows.Win32.Foundation.PWSTR, pcchNameBufferSize: POINTER(UInt32)) -> UInt32: ...
PdhLookupPerfNameByIndex = UnicodeAlias('PdhLookupPerfNameByIndexW')
@winfunctype('pdh.dll')
def PdhLookupPerfNameByIndexA(szMachineName: win32more.Windows.Win32.Foundation.PSTR, dwNameIndex: UInt32, szNameBuffer: win32more.Windows.Win32.Foundation.PSTR, pcchNameBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhLookupPerfIndexByNameW(szMachineName: win32more.Windows.Win32.Foundation.PWSTR, szNameBuffer: win32more.Windows.Win32.Foundation.PWSTR, pdwIndex: POINTER(UInt32)) -> UInt32: ...
PdhLookupPerfIndexByName = UnicodeAlias('PdhLookupPerfIndexByNameW')
@winfunctype('pdh.dll')
def PdhLookupPerfIndexByNameA(szMachineName: win32more.Windows.Win32.Foundation.PSTR, szNameBuffer: win32more.Windows.Win32.Foundation.PSTR, pdwIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandWildCardPathA(szDataSource: win32more.Windows.Win32.Foundation.PSTR, szWildCardPath: win32more.Windows.Win32.Foundation.PSTR, mszExpandedPathList: win32more.Windows.Win32.Foundation.PSTR, pcchPathListLength: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandWildCardPathW(szDataSource: win32more.Windows.Win32.Foundation.PWSTR, szWildCardPath: win32more.Windows.Win32.Foundation.PWSTR, mszExpandedPathList: win32more.Windows.Win32.Foundation.PWSTR, pcchPathListLength: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
PdhExpandWildCardPath = UnicodeAlias('PdhExpandWildCardPathW')
@winfunctype('pdh.dll')
def PdhOpenLogW(szLogFileName: win32more.Windows.Win32.Foundation.PWSTR, dwAccessFlags: win32more.Windows.Win32.System.Performance.PDH_LOG, lpdwLogType: POINTER(win32more.Windows.Win32.System.Performance.PDH_LOG_TYPE), hQuery: win32more.Windows.Win32.System.Performance.PDH_HQUERY, dwMaxSize: UInt32, szUserCaption: win32more.Windows.Win32.Foundation.PWSTR, phLog: POINTER(win32more.Windows.Win32.System.Performance.PDH_HLOG)) -> UInt32: ...
PdhOpenLog = UnicodeAlias('PdhOpenLogW')
@winfunctype('pdh.dll')
def PdhOpenLogA(szLogFileName: win32more.Windows.Win32.Foundation.PSTR, dwAccessFlags: win32more.Windows.Win32.System.Performance.PDH_LOG, lpdwLogType: POINTER(win32more.Windows.Win32.System.Performance.PDH_LOG_TYPE), hQuery: win32more.Windows.Win32.System.Performance.PDH_HQUERY, dwMaxSize: UInt32, szUserCaption: win32more.Windows.Win32.Foundation.PSTR, phLog: POINTER(win32more.Windows.Win32.System.Performance.PDH_HLOG)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhUpdateLogW(hLog: win32more.Windows.Win32.System.Performance.PDH_HLOG, szUserString: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
PdhUpdateLog = UnicodeAlias('PdhUpdateLogW')
@winfunctype('pdh.dll')
def PdhUpdateLogA(hLog: win32more.Windows.Win32.System.Performance.PDH_HLOG, szUserString: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhUpdateLogFileCatalog(hLog: win32more.Windows.Win32.System.Performance.PDH_HLOG) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetLogFileSize(hLog: win32more.Windows.Win32.System.Performance.PDH_HLOG, llSize: POINTER(Int64)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCloseLog(hLog: win32more.Windows.Win32.System.Performance.PDH_HLOG, dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSelectDataSourceW(hWndOwner: win32more.Windows.Win32.Foundation.HWND, dwFlags: win32more.Windows.Win32.System.Performance.PDH_SELECT_DATA_SOURCE_FLAGS, szDataSource: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferLength: POINTER(UInt32)) -> UInt32: ...
PdhSelectDataSource = UnicodeAlias('PdhSelectDataSourceW')
@winfunctype('pdh.dll')
def PdhSelectDataSourceA(hWndOwner: win32more.Windows.Win32.Foundation.HWND, dwFlags: win32more.Windows.Win32.System.Performance.PDH_SELECT_DATA_SOURCE_FLAGS, szDataSource: win32more.Windows.Win32.Foundation.PSTR, pcchBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhIsRealTimeQuery(hQuery: win32more.Windows.Win32.System.Performance.PDH_HQUERY) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('pdh.dll')
def PdhSetQueryTimeRange(hQuery: win32more.Windows.Win32.System.Performance.PDH_HQUERY, pInfo: POINTER(win32more.Windows.Win32.System.Performance.PDH_TIME_INFO)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDataSourceTimeRangeW(szDataSource: win32more.Windows.Win32.Foundation.PWSTR, pdwNumEntries: POINTER(UInt32), pInfo: POINTER(win32more.Windows.Win32.System.Performance.PDH_TIME_INFO), pdwBufferSize: POINTER(UInt32)) -> UInt32: ...
PdhGetDataSourceTimeRange = UnicodeAlias('PdhGetDataSourceTimeRangeW')
@winfunctype('pdh.dll')
def PdhGetDataSourceTimeRangeA(szDataSource: win32more.Windows.Win32.Foundation.PSTR, pdwNumEntries: POINTER(UInt32), pInfo: POINTER(win32more.Windows.Win32.System.Performance.PDH_TIME_INFO), pdwBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCollectQueryDataEx(hQuery: win32more.Windows.Win32.System.Performance.PDH_HQUERY, dwIntervalTime: UInt32, hNewDataEvent: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhFormatFromRawValue(dwCounterType: UInt32, dwFormat: win32more.Windows.Win32.System.Performance.PDH_FMT, pTimeBase: POINTER(Int64), pRawValue1: POINTER(win32more.Windows.Win32.System.Performance.PDH_RAW_COUNTER), pRawValue2: POINTER(win32more.Windows.Win32.System.Performance.PDH_RAW_COUNTER), pFmtValue: POINTER(win32more.Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetCounterTimeBase(hCounter: win32more.Windows.Win32.System.Performance.PDH_HCOUNTER, pTimeBase: POINTER(Int64)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhReadRawLogRecord(hLog: win32more.Windows.Win32.System.Performance.PDH_HLOG, ftRecord: win32more.Windows.Win32.Foundation.FILETIME, pRawLogRecord: POINTER(win32more.Windows.Win32.System.Performance.PDH_RAW_LOG_RECORD), pdwBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSetDefaultRealTimeDataSource(dwDataSourceId: win32more.Windows.Win32.System.Performance.REAL_TIME_DATA_SOURCE_ID_FLAGS) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBindInputDataSourceW(phDataSource: POINTER(win32more.Windows.Win32.System.Performance.PDH_HLOG), LogFileNameList: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
PdhBindInputDataSource = UnicodeAlias('PdhBindInputDataSourceW')
@winfunctype('pdh.dll')
def PdhBindInputDataSourceA(phDataSource: POINTER(win32more.Windows.Win32.System.Performance.PDH_HLOG), LogFileNameList: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhOpenQueryH(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, dwUserData: UIntPtr, phQuery: POINTER(win32more.Windows.Win32.System.Performance.PDH_HQUERY)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumMachinesHW(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, mszMachineList: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
PdhEnumMachinesH = UnicodeAlias('PdhEnumMachinesHW')
@winfunctype('pdh.dll')
def PdhEnumMachinesHA(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, mszMachineList: win32more.Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectsHW(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, szMachineName: win32more.Windows.Win32.Foundation.PWSTR, mszObjectList: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32), dwDetailLevel: win32more.Windows.Win32.System.Performance.PERF_DETAIL, bRefresh: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
PdhEnumObjectsH = UnicodeAlias('PdhEnumObjectsHW')
@winfunctype('pdh.dll')
def PdhEnumObjectsHA(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, szMachineName: win32more.Windows.Win32.Foundation.PSTR, mszObjectList: win32more.Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32), dwDetailLevel: win32more.Windows.Win32.System.Performance.PERF_DETAIL, bRefresh: win32more.Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectItemsHW(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, szMachineName: win32more.Windows.Win32.Foundation.PWSTR, szObjectName: win32more.Windows.Win32.Foundation.PWSTR, mszCounterList: win32more.Windows.Win32.Foundation.PWSTR, pcchCounterListLength: POINTER(UInt32), mszInstanceList: win32more.Windows.Win32.Foundation.PWSTR, pcchInstanceListLength: POINTER(UInt32), dwDetailLevel: win32more.Windows.Win32.System.Performance.PERF_DETAIL, dwFlags: UInt32) -> UInt32: ...
PdhEnumObjectItemsH = UnicodeAlias('PdhEnumObjectItemsHW')
@winfunctype('pdh.dll')
def PdhEnumObjectItemsHA(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, szMachineName: win32more.Windows.Win32.Foundation.PSTR, szObjectName: win32more.Windows.Win32.Foundation.PSTR, mszCounterList: win32more.Windows.Win32.Foundation.PSTR, pcchCounterListLength: POINTER(UInt32), mszInstanceList: win32more.Windows.Win32.Foundation.PSTR, pcchInstanceListLength: POINTER(UInt32), dwDetailLevel: win32more.Windows.Win32.System.Performance.PERF_DETAIL, dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandWildCardPathHW(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, szWildCardPath: win32more.Windows.Win32.Foundation.PWSTR, mszExpandedPathList: win32more.Windows.Win32.Foundation.PWSTR, pcchPathListLength: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
PdhExpandWildCardPathH = UnicodeAlias('PdhExpandWildCardPathHW')
@winfunctype('pdh.dll')
def PdhExpandWildCardPathHA(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, szWildCardPath: win32more.Windows.Win32.Foundation.PSTR, mszExpandedPathList: win32more.Windows.Win32.Foundation.PSTR, pcchPathListLength: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDataSourceTimeRangeH(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, pdwNumEntries: POINTER(UInt32), pInfo: POINTER(win32more.Windows.Win32.System.Performance.PDH_TIME_INFO), pdwBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfObjectHW(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, szMachineName: win32more.Windows.Win32.Foundation.PWSTR, szDefaultObjectName: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
PdhGetDefaultPerfObjectH = UnicodeAlias('PdhGetDefaultPerfObjectHW')
@winfunctype('pdh.dll')
def PdhGetDefaultPerfObjectHA(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, szMachineName: win32more.Windows.Win32.Foundation.PSTR, szDefaultObjectName: win32more.Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfCounterHW(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, szMachineName: win32more.Windows.Win32.Foundation.PWSTR, szObjectName: win32more.Windows.Win32.Foundation.PWSTR, szDefaultCounterName: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
PdhGetDefaultPerfCounterH = UnicodeAlias('PdhGetDefaultPerfCounterHW')
@winfunctype('pdh.dll')
def PdhGetDefaultPerfCounterHA(hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG, szMachineName: win32more.Windows.Win32.Foundation.PSTR, szObjectName: win32more.Windows.Win32.Foundation.PSTR, szDefaultCounterName: win32more.Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBrowseCountersHW(pBrowseDlgData: POINTER(win32more.Windows.Win32.System.Performance.PDH_BROWSE_DLG_CONFIG_HW)) -> UInt32: ...
PdhBrowseCountersH = UnicodeAlias('PdhBrowseCountersHW')
@winfunctype('pdh.dll')
def PdhBrowseCountersHA(pBrowseDlgData: POINTER(win32more.Windows.Win32.System.Performance.PDH_BROWSE_DLG_CONFIG_HA)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhVerifySQLDBW(szDataSource: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
PdhVerifySQLDB = UnicodeAlias('PdhVerifySQLDBW')
@winfunctype('pdh.dll')
def PdhVerifySQLDBA(szDataSource: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCreateSQLTablesW(szDataSource: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
PdhCreateSQLTables = UnicodeAlias('PdhCreateSQLTablesW')
@winfunctype('pdh.dll')
def PdhCreateSQLTablesA(szDataSource: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumLogSetNamesW(szDataSource: win32more.Windows.Win32.Foundation.PWSTR, mszDataSetNameList: win32more.Windows.Win32.Foundation.PWSTR, pcchBufferLength: POINTER(UInt32)) -> UInt32: ...
PdhEnumLogSetNames = UnicodeAlias('PdhEnumLogSetNamesW')
@winfunctype('pdh.dll')
def PdhEnumLogSetNamesA(szDataSource: win32more.Windows.Win32.Foundation.PSTR, mszDataSetNameList: win32more.Windows.Win32.Foundation.PSTR, pcchBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetLogSetGUID(hLog: win32more.Windows.Win32.System.Performance.PDH_HLOG, pGuid: POINTER(Guid), pRunId: POINTER(Int32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSetLogSetRunID(hLog: win32more.Windows.Win32.System.Performance.PDH_HLOG, RunId: Int32) -> UInt32: ...
AppearPropPage = Guid('{e49741e9-93a8-4ab1-8e96-bf4482282e9c}')
AutoPathFormat = Int32
plaNone: win32more.Windows.Win32.System.Performance.AutoPathFormat = 0
plaPattern: win32more.Windows.Win32.System.Performance.AutoPathFormat = 1
plaComputer: win32more.Windows.Win32.System.Performance.AutoPathFormat = 2
plaMonthDayHour: win32more.Windows.Win32.System.Performance.AutoPathFormat = 256
plaSerialNumber: win32more.Windows.Win32.System.Performance.AutoPathFormat = 512
plaYearDayOfYear: win32more.Windows.Win32.System.Performance.AutoPathFormat = 1024
plaYearMonth: win32more.Windows.Win32.System.Performance.AutoPathFormat = 2048
plaYearMonthDay: win32more.Windows.Win32.System.Performance.AutoPathFormat = 4096
plaYearMonthDayHour: win32more.Windows.Win32.System.Performance.AutoPathFormat = 8192
plaMonthDayHourMinute: win32more.Windows.Win32.System.Performance.AutoPathFormat = 16384
BootTraceSession = Guid('{03837538-098b-11d8-9414-505054503030}')
BootTraceSessionCollection = Guid('{03837539-098b-11d8-9414-505054503030}')
ClockType = Int32
plaTimeStamp: win32more.Windows.Win32.System.Performance.ClockType = 0
plaPerformance: win32more.Windows.Win32.System.Performance.ClockType = 1
plaSystem: win32more.Windows.Win32.System.Performance.ClockType = 2
plaCycle: win32more.Windows.Win32.System.Performance.ClockType = 3
CommitMode = Int32
plaCreateNew: win32more.Windows.Win32.System.Performance.CommitMode = 1
plaModify: win32more.Windows.Win32.System.Performance.CommitMode = 2
plaCreateOrModify: win32more.Windows.Win32.System.Performance.CommitMode = 3
plaUpdateRunningInstance: win32more.Windows.Win32.System.Performance.CommitMode = 16
plaFlushTrace: win32more.Windows.Win32.System.Performance.CommitMode = 32
plaValidateOnly: win32more.Windows.Win32.System.Performance.CommitMode = 4096
CounterItem = Guid('{c4d2d8e0-d1dd-11ce-940f-008029004348}')
CounterItem2 = Guid('{43196c62-c31f-4ce3-a02e-79efe0f6a525}')
@winfunctype_pointer
def CounterPathCallBack(param0: UIntPtr) -> Int32: ...
CounterPropPage = Guid('{cf948561-ede8-11ce-941e-008029004347}')
Counters = Guid('{b2b066d2-2aac-11cf-942f-008029004347}')
class DICounterItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c08c4ff2-0e2e-11cf-942c-008029004347}')
class DILogFileItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8d093ffc-f777-4917-82d1-833fbc54c58f}')
class DISystemMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{13d73d81-c32e-11cf-9398-00aa00a3ddea}')
class DISystemMonitorEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{84979930-4ab3-11cf-943a-008029004347}')
class DISystemMonitorInternal(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{194eb242-c32c-11cf-9398-00aa00a3ddea}')
DataCollectorSet = Guid('{03837521-098b-11d8-9414-505054503030}')
DataCollectorSetCollection = Guid('{03837525-098b-11d8-9414-505054503030}')
DataCollectorSetStatus = Int32
plaStopped: win32more.Windows.Win32.System.Performance.DataCollectorSetStatus = 0
plaRunning: win32more.Windows.Win32.System.Performance.DataCollectorSetStatus = 1
plaCompiling: win32more.Windows.Win32.System.Performance.DataCollectorSetStatus = 2
plaPending: win32more.Windows.Win32.System.Performance.DataCollectorSetStatus = 3
plaUndefined: win32more.Windows.Win32.System.Performance.DataCollectorSetStatus = 4
DataCollectorType = Int32
plaPerformanceCounter: win32more.Windows.Win32.System.Performance.DataCollectorType = 0
plaTrace: win32more.Windows.Win32.System.Performance.DataCollectorType = 1
plaConfiguration: win32more.Windows.Win32.System.Performance.DataCollectorType = 2
plaAlert: win32more.Windows.Win32.System.Performance.DataCollectorType = 3
plaApiTrace: win32more.Windows.Win32.System.Performance.DataCollectorType = 4
DataManagerSteps = Int32
plaCreateReport: win32more.Windows.Win32.System.Performance.DataManagerSteps = 1
plaRunRules: win32more.Windows.Win32.System.Performance.DataManagerSteps = 2
plaCreateHtml: win32more.Windows.Win32.System.Performance.DataManagerSteps = 4
plaFolderActions: win32more.Windows.Win32.System.Performance.DataManagerSteps = 8
plaResourceFreeing: win32more.Windows.Win32.System.Performance.DataManagerSteps = 16
DataSourceTypeConstants = Int32
sysmonNullDataSource: win32more.Windows.Win32.System.Performance.DataSourceTypeConstants = -1
sysmonCurrentActivity: win32more.Windows.Win32.System.Performance.DataSourceTypeConstants = 1
sysmonLogFiles: win32more.Windows.Win32.System.Performance.DataSourceTypeConstants = 2
sysmonSqlLog: win32more.Windows.Win32.System.Performance.DataSourceTypeConstants = 3
DisplayTypeConstants = Int32
sysmonLineGraph: win32more.Windows.Win32.System.Performance.DisplayTypeConstants = 1
sysmonHistogram: win32more.Windows.Win32.System.Performance.DisplayTypeConstants = 2
sysmonReport: win32more.Windows.Win32.System.Performance.DisplayTypeConstants = 3
sysmonChartArea: win32more.Windows.Win32.System.Performance.DisplayTypeConstants = 4
sysmonChartStackedArea: win32more.Windows.Win32.System.Performance.DisplayTypeConstants = 5
FileFormat = Int32
plaCommaSeparated: win32more.Windows.Win32.System.Performance.FileFormat = 0
plaTabSeparated: win32more.Windows.Win32.System.Performance.FileFormat = 1
plaSql: win32more.Windows.Win32.System.Performance.FileFormat = 2
plaBinary: win32more.Windows.Win32.System.Performance.FileFormat = 3
FolderActionSteps = Int32
plaCreateCab: win32more.Windows.Win32.System.Performance.FolderActionSteps = 1
plaDeleteData: win32more.Windows.Win32.System.Performance.FolderActionSteps = 2
plaSendCab: win32more.Windows.Win32.System.Performance.FolderActionSteps = 4
plaDeleteCab: win32more.Windows.Win32.System.Performance.FolderActionSteps = 8
plaDeleteReport: win32more.Windows.Win32.System.Performance.FolderActionSteps = 16
GeneralPropPage = Guid('{c3e5d3d2-1a03-11cf-942d-008029004347}')
GraphPropPage = Guid('{c3e5d3d3-1a03-11cf-942d-008029004347}')
class IAlertDataCollector(ComPtr):
    extends: win32more.Windows.Win32.System.Performance.IDataCollector
    _iid_ = Guid('{03837516-098b-11d8-9414-505054503030}')
    @commethod(32)
    def get_AlertThresholds(self, alerts: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_AlertThresholds(self, alerts: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_EventLog(self, log: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_EventLog(self, log: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_SampleInterval(self, interval: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_SampleInterval(self, interval: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_Task(self, task: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_Task(self, task: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_TaskRunAsSelf(self, RunAsSelf: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_TaskRunAsSelf(self, RunAsSelf: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_TaskArguments(self, task: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_TaskArguments(self, task: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_TaskUserTextArguments(self, task: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_TaskUserTextArguments(self, task: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_TriggerDataCollectorSet(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_TriggerDataCollectorSet(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApiTracingDataCollector(ComPtr):
    extends: win32more.Windows.Win32.System.Performance.IDataCollector
    _iid_ = Guid('{0383751a-098b-11d8-9414-505054503030}')
    @commethod(32)
    def get_LogApiNamesOnly(self, logapinames: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_LogApiNamesOnly(self, logapinames: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_LogApisRecursively(self, logrecursively: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_LogApisRecursively(self, logrecursively: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_ExePath(self, exepath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_ExePath(self, exepath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_LogFilePath(self, logfilepath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_LogFilePath(self, logfilepath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_IncludeModules(self, includemodules: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_IncludeModules(self, includemodules: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_IncludeApis(self, includeapis: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_IncludeApis(self, includeapis: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_ExcludeApis(self, excludeapis: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_ExcludeApis(self, excludeapis: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IConfigurationDataCollector(ComPtr):
    extends: win32more.Windows.Win32.System.Performance.IDataCollector
    _iid_ = Guid('{03837514-098b-11d8-9414-505054503030}')
    @commethod(32)
    def get_FileMaxCount(self, count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_FileMaxCount(self, count: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_FileMaxRecursiveDepth(self, depth: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_FileMaxRecursiveDepth(self, depth: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_FileMaxTotalSize(self, size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_FileMaxTotalSize(self, size: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_Files(self, Files: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_Files(self, Files: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_ManagementQueries(self, Queries: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_ManagementQueries(self, Queries: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_QueryNetworkAdapters(self, network: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_QueryNetworkAdapters(self, network: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_RegistryKeys(self, query: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_RegistryKeys(self, query: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_RegistryMaxRecursiveDepth(self, depth: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_RegistryMaxRecursiveDepth(self, depth: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_SystemStateFile(self, FileName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_SystemStateFile(self, FileName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICounterItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{771a9520-ee28-11ce-941e-008029004347}')
    @commethod(3)
    def get_Value(self, pdblValue: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Color(self, Color: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Color(self, pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_Width(self, iWidth: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Width(self, piValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_LineStyle(self, iLineStyle: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LineStyle(self, piValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ScaleFactor(self, iScale: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ScaleFactor(self, piValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Path(self, pstrValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetValue(self, Value: POINTER(Double), Status: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetStatistics(self, Max: POINTER(Double), Min: POINTER(Double), Avg: POINTER(Double), Status: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICounterItem2(ComPtr):
    extends: win32more.Windows.Win32.System.Performance.ICounterItem
    _iid_ = Guid('{eefcd4e1-ea1c-4435-b7f4-e341ba03b4f9}')
    @commethod(15)
    def put_Selected(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Selected(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Visible(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Visible(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDataAt(self, iIndex: Int32, iWhich: win32more.Windows.Win32.System.Performance.SysmonDataType, pVariant: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICounters(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{79167962-28fc-11cf-942f-008029004347}')
    @commethod(7)
    def get_Count(self, pLong: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, ppIunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, index: win32more.Windows.Win32.System.Variant.VARIANT, ppI: POINTER(win32more.Windows.Win32.System.Performance.DICounterItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pathname: win32more.Windows.Win32.Foundation.BSTR, ppI: POINTER(win32more.Windows.Win32.System.Performance.DICounterItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, index: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDataCollector(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{038374ff-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_DataCollectorSet(self, group: POINTER(win32more.Windows.Win32.System.Performance.IDataCollectorSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_DataCollectorSet(self, group: win32more.Windows.Win32.System.Performance.IDataCollectorSet) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DataCollectorType(self, type: POINTER(win32more.Windows.Win32.System.Performance.DataCollectorType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_FileName(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_FileName(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_FileNameFormat(self, format: POINTER(win32more.Windows.Win32.System.Performance.AutoPathFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_FileNameFormat(self, format: win32more.Windows.Win32.System.Performance.AutoPathFormat) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_FileNameFormatPattern(self, pattern: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_FileNameFormatPattern(self, pattern: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_LatestOutputLocation(self, path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_LatestOutputLocation(self, path: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_LogAppend(self, append: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_LogAppend(self, append: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_LogCircular(self, circular: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_LogCircular(self, circular: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_LogOverwrite(self, overwrite: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_LogOverwrite(self, overwrite: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_OutputLocation(self, path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Index(self, index: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_Index(self, index: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_Xml(self, Xml: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetXml(self, Xml: win32more.Windows.Win32.Foundation.BSTR, Validation: POINTER(win32more.Windows.Win32.System.Performance.IValueMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def CreateOutputLocation(self, Latest: win32more.Windows.Win32.Foundation.VARIANT_BOOL, Location: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDataCollectorCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837502-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Count(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, index: win32more.Windows.Win32.System.Variant.VARIANT, collector: POINTER(win32more.Windows.Win32.System.Performance.IDataCollector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, retVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, collector: win32more.Windows.Win32.System.Performance.IDataCollector) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, collector: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(self, collectors: win32more.Windows.Win32.System.Performance.IDataCollectorCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateDataCollectorFromXml(self, bstrXml: win32more.Windows.Win32.Foundation.BSTR, pValidation: POINTER(win32more.Windows.Win32.System.Performance.IValueMap), pCollector: POINTER(win32more.Windows.Win32.System.Performance.IDataCollector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateDataCollector(self, Type: win32more.Windows.Win32.System.Performance.DataCollectorType, Collector: POINTER(win32more.Windows.Win32.System.Performance.IDataCollector)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDataCollectorSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837520-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_DataCollectors(self, collectors: POINTER(win32more.Windows.Win32.System.Performance.IDataCollectorCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Duration(self, seconds: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Duration(self, seconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Description(self, description: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_Description(self, description: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_DescriptionUnresolved(self, Descr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_DisplayName(self, DisplayName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_DisplayName(self, DisplayName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_DisplayNameUnresolved(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Keywords(self, keywords: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Keywords(self, keywords: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_LatestOutputLocation(self, path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_LatestOutputLocation(self, path: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Name(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_OutputLocation(self, path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_RootPath(self, folder: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_RootPath(self, folder: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Segment(self, segment: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Segment(self, segment: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_SegmentMaxDuration(self, seconds: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_SegmentMaxDuration(self, seconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_SegmentMaxSize(self, size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_SegmentMaxSize(self, size: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_SerialNumber(self, index: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_SerialNumber(self, index: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_Server(self, server: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_Status(self, status: POINTER(win32more.Windows.Win32.System.Performance.DataCollectorSetStatus)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_Subdirectory(self, folder: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_Subdirectory(self, folder: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_SubdirectoryFormat(self, format: POINTER(win32more.Windows.Win32.System.Performance.AutoPathFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_SubdirectoryFormat(self, format: win32more.Windows.Win32.System.Performance.AutoPathFormat) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_SubdirectoryFormatPattern(self, pattern: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_SubdirectoryFormatPattern(self, pattern: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_Task(self, task: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_Task(self, task: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_TaskRunAsSelf(self, RunAsSelf: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_TaskRunAsSelf(self, RunAsSelf: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_TaskArguments(self, task: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_TaskArguments(self, task: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_TaskUserTextArguments(self, UserText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_TaskUserTextArguments(self, UserText: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_Schedules(self, ppSchedules: POINTER(win32more.Windows.Win32.System.Performance.IScheduleCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_SchedulesEnabled(self, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def put_SchedulesEnabled(self, enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def get_UserAccount(self, user: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def get_Xml(self, xml: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_Security(self, pbstrSecurity: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def put_Security(self, bstrSecurity: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_StopOnCompletion(self, Stop: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def put_StopOnCompletion(self, Stop: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_DataManager(self, DataManager: POINTER(win32more.Windows.Win32.System.Performance.IDataManager)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def SetCredentials(self, user: win32more.Windows.Win32.Foundation.BSTR, password: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def Query(self, name: win32more.Windows.Win32.Foundation.BSTR, server: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def Commit(self, name: win32more.Windows.Win32.Foundation.BSTR, server: win32more.Windows.Win32.Foundation.BSTR, mode: win32more.Windows.Win32.System.Performance.CommitMode, validation: POINTER(win32more.Windows.Win32.System.Performance.IValueMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def Start(self, Synchronous: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def Stop(self, Synchronous: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def SetXml(self, xml: win32more.Windows.Win32.Foundation.BSTR, validation: POINTER(win32more.Windows.Win32.System.Performance.IValueMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def SetValue(self, key: win32more.Windows.Win32.Foundation.BSTR, value: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def GetValue(self, key: win32more.Windows.Win32.Foundation.BSTR, value: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDataCollectorSetCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837524-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Count(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, index: win32more.Windows.Win32.System.Variant.VARIANT, set: POINTER(win32more.Windows.Win32.System.Performance.IDataCollectorSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, retVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, set: win32more.Windows.Win32.System.Performance.IDataCollectorSet) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, set: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(self, sets: win32more.Windows.Win32.System.Performance.IDataCollectorSetCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDataCollectorSets(self, server: win32more.Windows.Win32.Foundation.BSTR, filter: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDataManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837541-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Enabled(self, pfEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Enabled(self, fEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CheckBeforeRunning(self, pfCheck: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_CheckBeforeRunning(self, fCheck: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_MinFreeDisk(self, MinFreeDisk: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_MinFreeDisk(self, MinFreeDisk: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_MaxSize(self, pulMaxSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_MaxSize(self, ulMaxSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MaxFolderCount(self, pulMaxFolderCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_MaxFolderCount(self, ulMaxFolderCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ResourcePolicy(self, pPolicy: POINTER(win32more.Windows.Win32.System.Performance.ResourcePolicy)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ResourcePolicy(self, Policy: win32more.Windows.Win32.System.Performance.ResourcePolicy) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_FolderActions(self, Actions: POINTER(win32more.Windows.Win32.System.Performance.IFolderActionCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_ReportSchema(self, ReportSchema: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_ReportSchema(self, ReportSchema: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_ReportFileName(self, pbstrFilename: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_ReportFileName(self, pbstrFilename: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_RuleTargetFileName(self, Filename: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_RuleTargetFileName(self, Filename: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_EventsFileName(self, pbstrFilename: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_EventsFileName(self, pbstrFilename: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Rules(self, pbstrXml: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Rules(self, bstrXml: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Run(self, Steps: win32more.Windows.Win32.System.Performance.DataManagerSteps, bstrFolder: win32more.Windows.Win32.Foundation.BSTR, Errors: POINTER(win32more.Windows.Win32.System.Performance.IValueMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def Extract(self, CabFilename: win32more.Windows.Win32.Foundation.BSTR, DestinationPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFolderAction(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837543-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Age(self, pulAge: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Age(self, ulAge: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Size(self, pulAge: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Size(self, ulAge: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Actions(self, Steps: POINTER(win32more.Windows.Win32.System.Performance.FolderActionSteps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Actions(self, Steps: win32more.Windows.Win32.System.Performance.FolderActionSteps) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_SendCabTo(self, pbstrDestination: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_SendCabTo(self, bstrDestination: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFolderActionCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837544-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Count(self, Count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, Index: win32more.Windows.Win32.System.Variant.VARIANT, Action: POINTER(win32more.Windows.Win32.System.Performance.IFolderAction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, Enum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, Action: win32more.Windows.Win32.System.Performance.IFolderAction) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, Index: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(self, Actions: win32more.Windows.Win32.System.Performance.IFolderActionCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateFolderAction(self, FolderAction: POINTER(win32more.Windows.Win32.System.Performance.IFolderAction)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILogFileItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d6b518dd-05c7-418a-89e6-4f9ce8c6841e}')
    @commethod(3)
    def get_Path(self, pstrValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILogFiles(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6a2a97e6-6851-41ea-87ad-2a8225335865}')
    @commethod(7)
    def get_Count(self, pLong: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, ppIunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, index: win32more.Windows.Win32.System.Variant.VARIANT, ppI: POINTER(win32more.Windows.Win32.System.Performance.DILogFileItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pathname: win32more.Windows.Win32.Foundation.BSTR, ppI: POINTER(win32more.Windows.Win32.System.Performance.DILogFileItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, index: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPerformanceCounterDataCollector(ComPtr):
    extends: win32more.Windows.Win32.System.Performance.IDataCollector
    _iid_ = Guid('{03837506-098b-11d8-9414-505054503030}')
    @commethod(32)
    def get_DataSourceName(self, dsn: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_DataSourceName(self, dsn: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_PerformanceCounters(self, counters: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_PerformanceCounters(self, counters: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_LogFileFormat(self, format: POINTER(win32more.Windows.Win32.System.Performance.FileFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_LogFileFormat(self, format: win32more.Windows.Win32.System.Performance.FileFormat) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_SampleInterval(self, interval: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_SampleInterval(self, interval: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_SegmentMaxRecords(self, records: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_SegmentMaxRecords(self, records: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISchedule(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0383753a-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_StartDate(self, start: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_StartDate(self, start: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_EndDate(self, end: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_EndDate(self, end: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_StartTime(self, start: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_StartTime(self, start: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Days(self, days: POINTER(win32more.Windows.Win32.System.Performance.WeekDays)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Days(self, days: win32more.Windows.Win32.System.Performance.WeekDays) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IScheduleCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0383753d-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Count(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, index: win32more.Windows.Win32.System.Variant.VARIANT, ppSchedule: POINTER(win32more.Windows.Win32.System.Performance.ISchedule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ienum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pSchedule: win32more.Windows.Win32.System.Performance.ISchedule) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, vSchedule: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(self, pSchedules: win32more.Windows.Win32.System.Performance.IScheduleCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateSchedule(self, Schedule: POINTER(win32more.Windows.Win32.System.Performance.ISchedule)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISystemMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{194eb241-c32c-11cf-9398-00aa00a3ddea}')
    @commethod(3)
    def get_Appearance(self, iAppearance: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Appearance(self, iAppearance: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_BackColor(self, pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_BackColor(self, Color: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_BorderStyle(self, iBorderStyle: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_BorderStyle(self, iBorderStyle: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ForeColor(self, pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ForeColor(self, Color: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Font(self, ppFont: POINTER(win32more.Windows.Win32.System.Ole.IFontDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def putref_Font(self, pFont: win32more.Windows.Win32.System.Ole.IFontDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Counters(self, ppICounters: POINTER(win32more.Windows.Win32.System.Performance.ICounters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_ShowVerticalGrid(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ShowVerticalGrid(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ShowHorizontalGrid(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ShowHorizontalGrid(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ShowLegend(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ShowLegend(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_ShowScaleLabels(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_ShowScaleLabels(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_ShowValueBar(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_ShowValueBar(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_MaximumScale(self, iValue: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_MaximumScale(self, piValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_MinimumScale(self, iValue: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_MinimumScale(self, piValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_UpdateInterval(self, fValue: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_UpdateInterval(self, pfValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_DisplayType(self, eDisplayType: win32more.Windows.Win32.System.Performance.DisplayTypeConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_DisplayType(self, peDisplayType: POINTER(win32more.Windows.Win32.System.Performance.DisplayTypeConstants)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_ManualUpdate(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_ManualUpdate(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_GraphTitle(self, bsTitle: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_GraphTitle(self, pbsTitle: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_YAxisLabel(self, bsTitle: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_YAxisLabel(self, pbsTitle: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def CollectSample(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def UpdateGraph(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def BrowseCounters(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def DisplayProperties(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def Counter(self, iIndex: Int32, ppICounter: POINTER(win32more.Windows.Win32.System.Performance.ICounterItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def AddCounter(self, bsPath: win32more.Windows.Win32.Foundation.BSTR, ppICounter: POINTER(win32more.Windows.Win32.System.Performance.ICounterItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def DeleteCounter(self, pCtr: win32more.Windows.Win32.System.Performance.ICounterItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_BackColorCtl(self, pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_BackColorCtl(self, Color: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_LogFileName(self, bsFileName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_LogFileName(self, bsFileName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_LogViewStart(self, StartTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_LogViewStart(self, StartTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def put_LogViewStop(self, StopTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def get_LogViewStop(self, StopTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_GridColor(self, pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def put_GridColor(self, Color: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_TimeBarColor(self, pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def put_TimeBarColor(self, Color: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_Highlight(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def put_Highlight(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_ShowToolbar(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def put_ShowToolbar(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def Paste(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def Copy(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def put_ReadOnly(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_ReadOnly(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def put_ReportValueType(self, eReportValueType: win32more.Windows.Win32.System.Performance.ReportValueTypeConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def get_ReportValueType(self, peReportValueType: POINTER(win32more.Windows.Win32.System.Performance.ReportValueTypeConstants)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def put_MonitorDuplicateInstances(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def get_MonitorDuplicateInstances(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def put_DisplayFilter(self, iValue: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def get_DisplayFilter(self, piValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def get_LogFiles(self, ppILogFiles: POINTER(win32more.Windows.Win32.System.Performance.ILogFiles)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def put_DataSourceType(self, eDataSourceType: win32more.Windows.Win32.System.Performance.DataSourceTypeConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def get_DataSourceType(self, peDataSourceType: POINTER(win32more.Windows.Win32.System.Performance.DataSourceTypeConstants)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def put_SqlDsnName(self, bsSqlDsnName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def get_SqlDsnName(self, bsSqlDsnName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def put_SqlLogSetName(self, bsSqlLogSetName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def get_SqlLogSetName(self, bsSqlLogSetName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISystemMonitor2(ComPtr):
    extends: win32more.Windows.Win32.System.Performance.ISystemMonitor
    _iid_ = Guid('{08e3206a-5fd2-4fde-a8a5-8cb3b63d2677}')
    @commethod(79)
    def put_EnableDigitGrouping(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def get_EnableDigitGrouping(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def put_EnableToolTips(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def get_EnableToolTips(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def put_ShowTimeAxisLabels(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def get_ShowTimeAxisLabels(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def put_ChartScroll(self, bScroll: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def get_ChartScroll(self, pbScroll: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def put_DataPointCount(self, iNewCount: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def get_DataPointCount(self, piDataPointCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def ScaleToFit(self, bSelectedCountersOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def SaveAs(self, bstrFileName: win32more.Windows.Win32.Foundation.BSTR, eSysmonFileType: win32more.Windows.Win32.System.Performance.SysmonFileType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(91)
    def Relog(self, bstrFileName: win32more.Windows.Win32.Foundation.BSTR, eSysmonFileType: win32more.Windows.Win32.System.Performance.SysmonFileType, iFilter: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def ClearData(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def get_LogSourceStartTime(self, pDate: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(94)
    def get_LogSourceStopTime(self, pDate: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(95)
    def SetLogViewRange(self, StartTime: Double, StopTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def GetLogViewRange(self, StartTime: POINTER(Double), StopTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(97)
    def BatchingLock(self, fLock: win32more.Windows.Win32.Foundation.VARIANT_BOOL, eBatchReason: win32more.Windows.Win32.System.Performance.SysmonBatchReason) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def LoadSettings(self, bstrSettingFileName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISystemMonitorEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ee660ea0-4abd-11cf-943a-008029004347}')
    @commethod(3)
    def OnCounterSelected(self, Index: Int32) -> Void: ...
    @commethod(4)
    def OnCounterAdded(self, Index: Int32) -> Void: ...
    @commethod(5)
    def OnCounterDeleted(self, Index: Int32) -> Void: ...
    @commethod(6)
    def OnSampleCollected(self) -> Void: ...
    @commethod(7)
    def OnDblClick(self, Index: Int32) -> Void: ...
class ITraceDataCollector(ComPtr):
    extends: win32more.Windows.Win32.System.Performance.IDataCollector
    _iid_ = Guid('{0383750b-098b-11d8-9414-505054503030}')
    @commethod(32)
    def get_BufferSize(self, size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_BufferSize(self, size: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_BuffersLost(self, buffers: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_BuffersLost(self, buffers: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_BuffersWritten(self, buffers: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_BuffersWritten(self, buffers: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_ClockType(self, clock: POINTER(win32more.Windows.Win32.System.Performance.ClockType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_ClockType(self, clock: win32more.Windows.Win32.System.Performance.ClockType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_EventsLost(self, events: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_EventsLost(self, events: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_ExtendedModes(self, mode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_ExtendedModes(self, mode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_FlushTimer(self, seconds: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_FlushTimer(self, seconds: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_FreeBuffers(self, buffers: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_FreeBuffers(self, buffers: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_Guid(self, guid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_Guid(self, guid: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_IsKernelTrace(self, kernel: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def get_MaximumBuffers(self, buffers: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def put_MaximumBuffers(self, buffers: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_MinimumBuffers(self, buffers: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def put_MinimumBuffers(self, buffers: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_NumberOfBuffers(self, buffers: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def put_NumberOfBuffers(self, buffers: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_PreallocateFile(self, allocate: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def put_PreallocateFile(self, allocate: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_ProcessMode(self, process: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def put_ProcessMode(self, process: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def get_RealTimeBuffersLost(self, buffers: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def put_RealTimeBuffersLost(self, buffers: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def get_SessionId(self, id: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def put_SessionId(self, id: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_SessionName(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def put_SessionName(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def get_SessionThreadId(self, tid: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def put_SessionThreadId(self, tid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def get_StreamMode(self, mode: POINTER(win32more.Windows.Win32.System.Performance.StreamMode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def put_StreamMode(self, mode: win32more.Windows.Win32.System.Performance.StreamMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def get_TraceDataProviders(self, providers: POINTER(win32more.Windows.Win32.System.Performance.ITraceDataProviderCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITraceDataProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837512-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_DisplayName(self, name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_DisplayName(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Guid(self, guid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Guid(self, guid: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Level(self, ppLevel: POINTER(win32more.Windows.Win32.System.Performance.IValueMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_KeywordsAny(self, ppKeywords: POINTER(win32more.Windows.Win32.System.Performance.IValueMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_KeywordsAll(self, ppKeywords: POINTER(win32more.Windows.Win32.System.Performance.IValueMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Properties(self, ppProperties: POINTER(win32more.Windows.Win32.System.Performance.IValueMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_FilterEnabled(self, FilterEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_FilterEnabled(self, FilterEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_FilterType(self, pulType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_FilterType(self, ulType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_FilterData(self, ppData: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_FilterData(self, pData: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Query(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, bstrServer: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Resolve(self, pFrom: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetSecurity(self, Sddl: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetSecurity(self, SecurityInfo: UInt32, Sddl: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetRegisteredProcesses(self, Processes: POINTER(win32more.Windows.Win32.System.Performance.IValueMap)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITraceDataProviderCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837510-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Count(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, index: win32more.Windows.Win32.System.Variant.VARIANT, ppProvider: POINTER(win32more.Windows.Win32.System.Performance.ITraceDataProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, retVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pProvider: win32more.Windows.Win32.System.Performance.ITraceDataProvider) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, vProvider: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(self, providers: win32more.Windows.Win32.System.Performance.ITraceDataProviderCollection) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateTraceDataProvider(self, Provider: POINTER(win32more.Windows.Win32.System.Performance.ITraceDataProvider)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetTraceDataProviders(self, server: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetTraceDataProvidersByProcess(self, Server: win32more.Windows.Win32.Foundation.BSTR, Pid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IValueMap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837534-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Count(self, retVal: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, index: win32more.Windows.Win32.System.Variant.VARIANT, value: POINTER(win32more.Windows.Win32.System.Performance.IValueMapItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, retVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Description(self, description: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_Description(self, description: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Value(self, Value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Value(self, Value: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ValueMapType(self, type: POINTER(win32more.Windows.Win32.System.Performance.ValueMapType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_ValueMapType(self, type: win32more.Windows.Win32.System.Performance.ValueMapType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Add(self, value: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Remove(self, value: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Clear(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def AddRange(self, map: win32more.Windows.Win32.System.Performance.IValueMap) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CreateValueMapItem(self, Item: POINTER(win32more.Windows.Win32.System.Performance.IValueMapItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IValueMapItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837533-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Description(self, description: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Description(self, description: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Enabled(self, enabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Enabled(self, enabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Key(self, key: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Key(self, key: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Value(self, Value: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Value(self, Value: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ValueMapType(self, type: POINTER(win32more.Windows.Win32.System.Performance.ValueMapType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ValueMapType(self, type: win32more.Windows.Win32.System.Performance.ValueMapType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
LegacyDataCollectorSet = Guid('{03837526-098b-11d8-9414-505054503030}')
LegacyDataCollectorSetCollection = Guid('{03837527-098b-11d8-9414-505054503030}')
LegacyTraceSession = Guid('{03837528-098b-11d8-9414-505054503030}')
LegacyTraceSessionCollection = Guid('{03837529-098b-11d8-9414-505054503030}')
LogFileItem = Guid('{16ec5be8-df93-4237-94e4-9ee918111d71}')
LogFiles = Guid('{2735d9fd-f6b9-4f19-a5d9-e2d068584bc5}')
class PDH_BROWSE_DLG_CONFIG_A(Structure):
    bIncludeInstanceIndex: Annotated[UInt32, 1]
    bSingleCounterPerAdd: Annotated[UInt32, 1]
    bSingleCounterPerDialog: Annotated[UInt32, 1]
    bLocalCountersOnly: Annotated[UInt32, 1]
    bWildCardInstances: Annotated[UInt32, 1]
    bHideDetailBox: Annotated[UInt32, 1]
    bInitializePath: Annotated[UInt32, 1]
    bDisableMachineSelection: Annotated[UInt32, 1]
    bIncludeCostlyObjects: Annotated[UInt32, 1]
    bShowObjectBrowser: Annotated[UInt32, 1]
    bReserved: Annotated[UInt32, 22]
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    szDataSource: win32more.Windows.Win32.Foundation.PSTR
    szReturnPathBuffer: win32more.Windows.Win32.Foundation.PSTR
    cchReturnPathLength: UInt32
    pCallBack: win32more.Windows.Win32.System.Performance.CounterPathCallBack
    dwCallBackArg: UIntPtr
    CallBackStatus: Int32
    dwDefaultDetailLevel: win32more.Windows.Win32.System.Performance.PERF_DETAIL
    szDialogBoxCaption: win32more.Windows.Win32.Foundation.PSTR
class PDH_BROWSE_DLG_CONFIG_HA(Structure):
    bIncludeInstanceIndex: Annotated[UInt32, 1]
    bSingleCounterPerAdd: Annotated[UInt32, 1]
    bSingleCounterPerDialog: Annotated[UInt32, 1]
    bLocalCountersOnly: Annotated[UInt32, 1]
    bWildCardInstances: Annotated[UInt32, 1]
    bHideDetailBox: Annotated[UInt32, 1]
    bInitializePath: Annotated[UInt32, 1]
    bDisableMachineSelection: Annotated[UInt32, 1]
    bIncludeCostlyObjects: Annotated[UInt32, 1]
    bShowObjectBrowser: Annotated[UInt32, 1]
    bReserved: Annotated[UInt32, 22]
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG
    szReturnPathBuffer: win32more.Windows.Win32.Foundation.PSTR
    cchReturnPathLength: UInt32
    pCallBack: win32more.Windows.Win32.System.Performance.CounterPathCallBack
    dwCallBackArg: UIntPtr
    CallBackStatus: Int32
    dwDefaultDetailLevel: win32more.Windows.Win32.System.Performance.PERF_DETAIL
    szDialogBoxCaption: win32more.Windows.Win32.Foundation.PSTR
class PDH_BROWSE_DLG_CONFIG_HW(Structure):
    bIncludeInstanceIndex: Annotated[UInt32, 1]
    bSingleCounterPerAdd: Annotated[UInt32, 1]
    bSingleCounterPerDialog: Annotated[UInt32, 1]
    bLocalCountersOnly: Annotated[UInt32, 1]
    bWildCardInstances: Annotated[UInt32, 1]
    bHideDetailBox: Annotated[UInt32, 1]
    bInitializePath: Annotated[UInt32, 1]
    bDisableMachineSelection: Annotated[UInt32, 1]
    bIncludeCostlyObjects: Annotated[UInt32, 1]
    bShowObjectBrowser: Annotated[UInt32, 1]
    bReserved: Annotated[UInt32, 22]
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    hDataSource: win32more.Windows.Win32.System.Performance.PDH_HLOG
    szReturnPathBuffer: win32more.Windows.Win32.Foundation.PWSTR
    cchReturnPathLength: UInt32
    pCallBack: win32more.Windows.Win32.System.Performance.CounterPathCallBack
    dwCallBackArg: UIntPtr
    CallBackStatus: Int32
    dwDefaultDetailLevel: win32more.Windows.Win32.System.Performance.PERF_DETAIL
    szDialogBoxCaption: win32more.Windows.Win32.Foundation.PWSTR
PDH_BROWSE_DLG_CONFIG_H = UnicodeAlias('PDH_BROWSE_DLG_CONFIG_HW')
class PDH_BROWSE_DLG_CONFIG_W(Structure):
    bIncludeInstanceIndex: Annotated[UInt32, 1]
    bSingleCounterPerAdd: Annotated[UInt32, 1]
    bSingleCounterPerDialog: Annotated[UInt32, 1]
    bLocalCountersOnly: Annotated[UInt32, 1]
    bWildCardInstances: Annotated[UInt32, 1]
    bHideDetailBox: Annotated[UInt32, 1]
    bInitializePath: Annotated[UInt32, 1]
    bDisableMachineSelection: Annotated[UInt32, 1]
    bIncludeCostlyObjects: Annotated[UInt32, 1]
    bShowObjectBrowser: Annotated[UInt32, 1]
    bReserved: Annotated[UInt32, 22]
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    szDataSource: win32more.Windows.Win32.Foundation.PWSTR
    szReturnPathBuffer: win32more.Windows.Win32.Foundation.PWSTR
    cchReturnPathLength: UInt32
    pCallBack: win32more.Windows.Win32.System.Performance.CounterPathCallBack
    dwCallBackArg: UIntPtr
    CallBackStatus: Int32
    dwDefaultDetailLevel: win32more.Windows.Win32.System.Performance.PERF_DETAIL
    szDialogBoxCaption: win32more.Windows.Win32.Foundation.PWSTR
PDH_BROWSE_DLG_CONFIG = UnicodeAlias('PDH_BROWSE_DLG_CONFIG_W')
class PDH_COUNTER_INFO_A(Structure):
    dwLength: UInt32
    dwType: UInt32
    CVersion: UInt32
    CStatus: UInt32
    lScale: Int32
    lDefaultScale: Int32
    dwUserData: UIntPtr
    dwQueryUserData: UIntPtr
    szFullPath: win32more.Windows.Win32.Foundation.PSTR
    Anonymous: _Anonymous_e__Union
    szExplainText: win32more.Windows.Win32.Foundation.PSTR
    DataBuffer: UInt32 * 1
    class _Anonymous_e__Union(Union):
        DataItemPath: win32more.Windows.Win32.System.Performance.PDH_DATA_ITEM_PATH_ELEMENTS_A
        CounterPath: win32more.Windows.Win32.System.Performance.PDH_COUNTER_PATH_ELEMENTS_A
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            szMachineName: win32more.Windows.Win32.Foundation.PSTR
            szObjectName: win32more.Windows.Win32.Foundation.PSTR
            szInstanceName: win32more.Windows.Win32.Foundation.PSTR
            szParentInstance: win32more.Windows.Win32.Foundation.PSTR
            dwInstanceIndex: UInt32
            szCounterName: win32more.Windows.Win32.Foundation.PSTR
class PDH_COUNTER_INFO_W(Structure):
    dwLength: UInt32
    dwType: UInt32
    CVersion: UInt32
    CStatus: UInt32
    lScale: Int32
    lDefaultScale: Int32
    dwUserData: UIntPtr
    dwQueryUserData: UIntPtr
    szFullPath: win32more.Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    szExplainText: win32more.Windows.Win32.Foundation.PWSTR
    DataBuffer: UInt32 * 1
    class _Anonymous_e__Union(Union):
        DataItemPath: win32more.Windows.Win32.System.Performance.PDH_DATA_ITEM_PATH_ELEMENTS_W
        CounterPath: win32more.Windows.Win32.System.Performance.PDH_COUNTER_PATH_ELEMENTS_W
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            szMachineName: win32more.Windows.Win32.Foundation.PWSTR
            szObjectName: win32more.Windows.Win32.Foundation.PWSTR
            szInstanceName: win32more.Windows.Win32.Foundation.PWSTR
            szParentInstance: win32more.Windows.Win32.Foundation.PWSTR
            dwInstanceIndex: UInt32
            szCounterName: win32more.Windows.Win32.Foundation.PWSTR
PDH_COUNTER_INFO = UnicodeAlias('PDH_COUNTER_INFO_W')
class PDH_COUNTER_PATH_ELEMENTS_A(Structure):
    szMachineName: win32more.Windows.Win32.Foundation.PSTR
    szObjectName: win32more.Windows.Win32.Foundation.PSTR
    szInstanceName: win32more.Windows.Win32.Foundation.PSTR
    szParentInstance: win32more.Windows.Win32.Foundation.PSTR
    dwInstanceIndex: UInt32
    szCounterName: win32more.Windows.Win32.Foundation.PSTR
class PDH_COUNTER_PATH_ELEMENTS_W(Structure):
    szMachineName: win32more.Windows.Win32.Foundation.PWSTR
    szObjectName: win32more.Windows.Win32.Foundation.PWSTR
    szInstanceName: win32more.Windows.Win32.Foundation.PWSTR
    szParentInstance: win32more.Windows.Win32.Foundation.PWSTR
    dwInstanceIndex: UInt32
    szCounterName: win32more.Windows.Win32.Foundation.PWSTR
PDH_COUNTER_PATH_ELEMENTS = UnicodeAlias('PDH_COUNTER_PATH_ELEMENTS_W')
class PDH_DATA_ITEM_PATH_ELEMENTS_A(Structure):
    szMachineName: win32more.Windows.Win32.Foundation.PSTR
    ObjectGUID: Guid
    dwItemId: UInt32
    szInstanceName: win32more.Windows.Win32.Foundation.PSTR
class PDH_DATA_ITEM_PATH_ELEMENTS_W(Structure):
    szMachineName: win32more.Windows.Win32.Foundation.PWSTR
    ObjectGUID: Guid
    dwItemId: UInt32
    szInstanceName: win32more.Windows.Win32.Foundation.PWSTR
PDH_DATA_ITEM_PATH_ELEMENTS = UnicodeAlias('PDH_DATA_ITEM_PATH_ELEMENTS_W')
PDH_DLL_VERSION = UInt32
PDH_CVERSION_WIN50: win32more.Windows.Win32.System.Performance.PDH_DLL_VERSION = 1280
PDH_VERSION: win32more.Windows.Win32.System.Performance.PDH_DLL_VERSION = 1283
PDH_FMT = UInt32
PDH_FMT_DOUBLE: win32more.Windows.Win32.System.Performance.PDH_FMT = 512
PDH_FMT_LARGE: win32more.Windows.Win32.System.Performance.PDH_FMT = 1024
PDH_FMT_LONG: win32more.Windows.Win32.System.Performance.PDH_FMT = 256
class PDH_FMT_COUNTERVALUE(Structure):
    CStatus: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        longValue: Int32
        doubleValue: Double
        largeValue: Int64
        AnsiStringValue: win32more.Windows.Win32.Foundation.PSTR
        WideStringValue: win32more.Windows.Win32.Foundation.PWSTR
class PDH_FMT_COUNTERVALUE_ITEM_A(Structure):
    szName: win32more.Windows.Win32.Foundation.PSTR
    FmtValue: win32more.Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE
class PDH_FMT_COUNTERVALUE_ITEM_W(Structure):
    szName: win32more.Windows.Win32.Foundation.PWSTR
    FmtValue: win32more.Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE
PDH_FMT_COUNTERVALUE_ITEM = UnicodeAlias('PDH_FMT_COUNTERVALUE_ITEM_W')
PDH_HCOUNTER = VoidPtr
PDH_HLOG = VoidPtr
PDH_HQUERY = VoidPtr
PDH_LOG = UInt32
PDH_LOG_READ_ACCESS: win32more.Windows.Win32.System.Performance.PDH_LOG = 65536
PDH_LOG_WRITE_ACCESS: win32more.Windows.Win32.System.Performance.PDH_LOG = 131072
PDH_LOG_UPDATE_ACCESS: win32more.Windows.Win32.System.Performance.PDH_LOG = 262144
class PDH_LOG_SERVICE_QUERY_INFO_A(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwLogQuota: UInt32
    szLogFileCaption: win32more.Windows.Win32.Foundation.PSTR
    szDefaultDir: win32more.Windows.Win32.Foundation.PSTR
    szBaseFileName: win32more.Windows.Win32.Foundation.PSTR
    dwFileType: UInt32
    dwReserved: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        class _Anonymous1_e__Struct(Structure):
            PdlAutoNameInterval: UInt32
            PdlAutoNameUnits: UInt32
            PdlCommandFilename: win32more.Windows.Win32.Foundation.PSTR
            PdlCounterList: win32more.Windows.Win32.Foundation.PSTR
            PdlAutoNameFormat: UInt32
            PdlSampleInterval: UInt32
            PdlLogStartTime: win32more.Windows.Win32.Foundation.FILETIME
            PdlLogEndTime: win32more.Windows.Win32.Foundation.FILETIME
        class _Anonymous2_e__Struct(Structure):
            TlNumberOfBuffers: UInt32
            TlMinimumBuffers: UInt32
            TlMaximumBuffers: UInt32
            TlFreeBuffers: UInt32
            TlBufferSize: UInt32
            TlEventsLost: UInt32
            TlLoggerThreadId: UInt32
            TlBuffersWritten: UInt32
            TlLogHandle: UInt32
            TlLogFileName: win32more.Windows.Win32.Foundation.PSTR
class PDH_LOG_SERVICE_QUERY_INFO_W(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwLogQuota: UInt32
    szLogFileCaption: win32more.Windows.Win32.Foundation.PWSTR
    szDefaultDir: win32more.Windows.Win32.Foundation.PWSTR
    szBaseFileName: win32more.Windows.Win32.Foundation.PWSTR
    dwFileType: UInt32
    dwReserved: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        class _Anonymous1_e__Struct(Structure):
            PdlAutoNameInterval: UInt32
            PdlAutoNameUnits: UInt32
            PdlCommandFilename: win32more.Windows.Win32.Foundation.PWSTR
            PdlCounterList: win32more.Windows.Win32.Foundation.PWSTR
            PdlAutoNameFormat: UInt32
            PdlSampleInterval: UInt32
            PdlLogStartTime: win32more.Windows.Win32.Foundation.FILETIME
            PdlLogEndTime: win32more.Windows.Win32.Foundation.FILETIME
        class _Anonymous2_e__Struct(Structure):
            TlNumberOfBuffers: UInt32
            TlMinimumBuffers: UInt32
            TlMaximumBuffers: UInt32
            TlFreeBuffers: UInt32
            TlBufferSize: UInt32
            TlEventsLost: UInt32
            TlLoggerThreadId: UInt32
            TlBuffersWritten: UInt32
            TlLogHandle: UInt32
            TlLogFileName: win32more.Windows.Win32.Foundation.PWSTR
PDH_LOG_SERVICE_QUERY_INFO = UnicodeAlias('PDH_LOG_SERVICE_QUERY_INFO_W')
PDH_LOG_TYPE = UInt32
PDH_LOG_TYPE_UNDEFINED: win32more.Windows.Win32.System.Performance.PDH_LOG_TYPE = 0
PDH_LOG_TYPE_CSV: win32more.Windows.Win32.System.Performance.PDH_LOG_TYPE = 1
PDH_LOG_TYPE_SQL: win32more.Windows.Win32.System.Performance.PDH_LOG_TYPE = 7
PDH_LOG_TYPE_TSV: win32more.Windows.Win32.System.Performance.PDH_LOG_TYPE = 2
PDH_LOG_TYPE_BINARY: win32more.Windows.Win32.System.Performance.PDH_LOG_TYPE = 8
PDH_LOG_TYPE_PERFMON: win32more.Windows.Win32.System.Performance.PDH_LOG_TYPE = 6
PDH_PATH_FLAGS = UInt32
PDH_PATH_WBEM_RESULT: win32more.Windows.Win32.System.Performance.PDH_PATH_FLAGS = 1
PDH_PATH_WBEM_INPUT: win32more.Windows.Win32.System.Performance.PDH_PATH_FLAGS = 2
PDH_PATH_WBEM_NONE: win32more.Windows.Win32.System.Performance.PDH_PATH_FLAGS = 0
class PDH_RAW_COUNTER(Structure):
    CStatus: UInt32
    TimeStamp: win32more.Windows.Win32.Foundation.FILETIME
    FirstValue: Int64
    SecondValue: Int64
    MultiCount: UInt32
class PDH_RAW_COUNTER_ITEM_A(Structure):
    szName: win32more.Windows.Win32.Foundation.PSTR
    RawValue: win32more.Windows.Win32.System.Performance.PDH_RAW_COUNTER
class PDH_RAW_COUNTER_ITEM_W(Structure):
    szName: win32more.Windows.Win32.Foundation.PWSTR
    RawValue: win32more.Windows.Win32.System.Performance.PDH_RAW_COUNTER
PDH_RAW_COUNTER_ITEM = UnicodeAlias('PDH_RAW_COUNTER_ITEM_W')
class PDH_RAW_LOG_RECORD(Structure):
    dwStructureSize: UInt32
    dwRecordType: win32more.Windows.Win32.System.Performance.PDH_LOG_TYPE
    dwItems: UInt32
    RawBytes: Byte * 1
PDH_SELECT_DATA_SOURCE_FLAGS = UInt32
PDH_FLAGS_FILE_BROWSER_ONLY: win32more.Windows.Win32.System.Performance.PDH_SELECT_DATA_SOURCE_FLAGS = 1
PDH_FLAGS_NONE: win32more.Windows.Win32.System.Performance.PDH_SELECT_DATA_SOURCE_FLAGS = 0
class PDH_STATISTICS(Structure):
    dwFormat: UInt32
    count: UInt32
    min: win32more.Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE
    max: win32more.Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE
    mean: win32more.Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE
class PDH_TIME_INFO(Structure):
    StartTime: Int64
    EndTime: Int64
    SampleCount: UInt32
@winfunctype_pointer
def PERFLIBREQUEST(RequestCode: UInt32, Buffer: VoidPtr, BufferSize: UInt32) -> UInt32: ...
class PERF_COUNTERSET_INFO(Structure):
    CounterSetGuid: Guid
    ProviderGuid: Guid
    NumCounters: UInt32
    InstanceType: UInt32
class PERF_COUNTERSET_INSTANCE(Structure):
    CounterSetGuid: Guid
    dwSize: UInt32
    InstanceId: UInt32
    InstanceNameOffset: UInt32
    InstanceNameSize: UInt32
class PERF_COUNTERSET_REG_INFO(Structure):
    CounterSetGuid: Guid
    CounterSetType: UInt32
    DetailLevel: UInt32
    NumCounters: UInt32
    InstanceType: UInt32
PERF_COUNTER_AGGREGATE_FUNC = UInt32
PERF_AGGREGATE_UNDEFINED: win32more.Windows.Win32.System.Performance.PERF_COUNTER_AGGREGATE_FUNC = 0
PERF_AGGREGATE_TOTAL: win32more.Windows.Win32.System.Performance.PERF_COUNTER_AGGREGATE_FUNC = 1
PERF_AGGREGATE_AVG: win32more.Windows.Win32.System.Performance.PERF_COUNTER_AGGREGATE_FUNC = 2
PERF_AGGREGATE_MIN: win32more.Windows.Win32.System.Performance.PERF_COUNTER_AGGREGATE_FUNC = 3
PERF_AGGREGATE_MAX: win32more.Windows.Win32.System.Performance.PERF_COUNTER_AGGREGATE_FUNC = 4
class PERF_COUNTER_BLOCK(Structure):
    ByteLength: UInt32
class PERF_COUNTER_DATA(Structure):
    dwDataSize: UInt32
    dwSize: UInt32
if ARCH in 'X64,ARM64':
    class PERF_COUNTER_DEFINITION(Structure):
        ByteLength: UInt32
        CounterNameTitleIndex: UInt32
        CounterNameTitle: UInt32
        CounterHelpTitleIndex: UInt32
        CounterHelpTitle: UInt32
        DefaultScale: Int32
        DetailLevel: UInt32
        CounterType: UInt32
        CounterSize: UInt32
        CounterOffset: UInt32
elif ARCH in 'X86':
    class PERF_COUNTER_DEFINITION(Structure):
        ByteLength: UInt32
        CounterNameTitleIndex: UInt32
        CounterNameTitle: win32more.Windows.Win32.Foundation.PWSTR
        CounterHelpTitleIndex: UInt32
        CounterHelpTitle: win32more.Windows.Win32.Foundation.PWSTR
        DefaultScale: Int32
        DetailLevel: UInt32
        CounterType: UInt32
        CounterSize: UInt32
        CounterOffset: UInt32
class PERF_COUNTER_HEADER(Structure):
    dwStatus: UInt32
    dwType: win32more.Windows.Win32.System.Performance.PerfCounterDataType
    dwSize: UInt32
    Reserved: UInt32
class PERF_COUNTER_IDENTIFIER(Structure):
    CounterSetGuid: Guid
    Status: UInt32
    Size: UInt32
    CounterId: UInt32
    InstanceId: UInt32
    Index: UInt32
    Reserved: UInt32
class PERF_COUNTER_IDENTITY(Structure):
    CounterSetGuid: Guid
    BufferSize: UInt32
    CounterId: UInt32
    InstanceId: UInt32
    MachineOffset: UInt32
    NameOffset: UInt32
    Reserved: UInt32
class PERF_COUNTER_INFO(Structure):
    CounterId: UInt32
    Type: UInt32
    Attrib: UInt64
    Size: UInt32
    DetailLevel: UInt32
    Scale: Int32
    Offset: UInt32
class PERF_COUNTER_REG_INFO(Structure):
    CounterId: UInt32
    Type: UInt32
    Attrib: UInt64
    DetailLevel: UInt32
    DefaultScale: Int32
    BaseCounterId: UInt32
    PerfTimeId: UInt32
    PerfFreqId: UInt32
    MultiId: UInt32
    AggregateFunc: win32more.Windows.Win32.System.Performance.PERF_COUNTER_AGGREGATE_FUNC
    Reserved: UInt32
class PERF_DATA_BLOCK(Structure):
    Signature: Char * 4
    LittleEndian: UInt32
    Version: UInt32
    Revision: UInt32
    TotalByteLength: UInt32
    HeaderLength: UInt32
    NumObjectTypes: UInt32
    DefaultObject: Int32
    SystemTime: win32more.Windows.Win32.Foundation.SYSTEMTIME
    PerfTime: Int64
    PerfFreq: Int64
    PerfTime100nSec: Int64
    SystemNameLength: UInt32
    SystemNameOffset: UInt32
class PERF_DATA_HEADER(Structure):
    dwTotalSize: UInt32
    dwNumCounters: UInt32
    PerfTimeStamp: Int64
    PerfTime100NSec: Int64
    PerfFreq: Int64
    SystemTime: win32more.Windows.Win32.Foundation.SYSTEMTIME
PERF_DETAIL = UInt32
PERF_DETAIL_NOVICE: win32more.Windows.Win32.System.Performance.PERF_DETAIL = 100
PERF_DETAIL_ADVANCED: win32more.Windows.Win32.System.Performance.PERF_DETAIL = 200
PERF_DETAIL_EXPERT: win32more.Windows.Win32.System.Performance.PERF_DETAIL = 300
PERF_DETAIL_WIZARD: win32more.Windows.Win32.System.Performance.PERF_DETAIL = 400
class PERF_INSTANCE_DEFINITION(Structure):
    ByteLength: UInt32
    ParentObjectTitleIndex: UInt32
    ParentObjectInstance: UInt32
    UniqueID: Int32
    NameOffset: UInt32
    NameLength: UInt32
class PERF_INSTANCE_HEADER(Structure):
    Size: UInt32
    InstanceId: UInt32
@winfunctype_pointer
def PERF_MEM_ALLOC(AllocSize: UIntPtr, pContext: VoidPtr) -> VoidPtr: ...
@winfunctype_pointer
def PERF_MEM_FREE(pBuffer: VoidPtr, pContext: VoidPtr) -> Void: ...
class PERF_MULTI_COUNTERS(Structure):
    dwSize: UInt32
    dwCounters: UInt32
class PERF_MULTI_INSTANCES(Structure):
    dwTotalSize: UInt32
    dwInstances: UInt32
if ARCH in 'X64,ARM64':
    class PERF_OBJECT_TYPE(Structure):
        TotalByteLength: UInt32
        DefinitionLength: UInt32
        HeaderLength: UInt32
        ObjectNameTitleIndex: UInt32
        ObjectNameTitle: UInt32
        ObjectHelpTitleIndex: UInt32
        ObjectHelpTitle: UInt32
        DetailLevel: UInt32
        NumCounters: UInt32
        DefaultCounter: Int32
        NumInstances: Int32
        CodePage: UInt32
        PerfTime: Int64
        PerfFreq: Int64
elif ARCH in 'X86':
    class PERF_OBJECT_TYPE(Structure):
        TotalByteLength: UInt32
        DefinitionLength: UInt32
        HeaderLength: UInt32
        ObjectNameTitleIndex: UInt32
        ObjectNameTitle: win32more.Windows.Win32.Foundation.PWSTR
        ObjectHelpTitleIndex: UInt32
        ObjectHelpTitle: win32more.Windows.Win32.Foundation.PWSTR
        DetailLevel: UInt32
        NumCounters: UInt32
        DefaultCounter: Int32
        NumInstances: Int32
        CodePage: UInt32
        PerfTime: Int64
        PerfFreq: Int64
class PERF_PROVIDER_CONTEXT(Structure):
    ContextSize: UInt32
    Reserved: UInt32
    ControlCallback: win32more.Windows.Win32.System.Performance.PERFLIBREQUEST
    MemAllocRoutine: win32more.Windows.Win32.System.Performance.PERF_MEM_ALLOC
    MemFreeRoutine: win32more.Windows.Win32.System.Performance.PERF_MEM_FREE
    pMemContext: VoidPtr
class PERF_STRING_BUFFER_HEADER(Structure):
    dwSize: UInt32
    dwCounters: UInt32
class PERF_STRING_COUNTER_HEADER(Structure):
    dwCounterId: UInt32
    dwOffset: UInt32
@winfunctype_pointer
def PLA_CABEXTRACT_CALLBACK(FileName: win32more.Windows.Win32.Foundation.PWSTR, Context: VoidPtr) -> Void: ...
@winfunctype_pointer
def PM_CLOSE_PROC() -> UInt32: ...
@winfunctype_pointer
def PM_COLLECT_PROC(pValueName: win32more.Windows.Win32.Foundation.PWSTR, ppData: POINTER(VoidPtr), pcbTotalBytes: POINTER(UInt32), pNumObjectTypes: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PM_OPEN_PROC(pContext: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
PerfCounterDataType = Int32
PERF_ERROR_RETURN: win32more.Windows.Win32.System.Performance.PerfCounterDataType = 0
PERF_SINGLE_COUNTER: win32more.Windows.Win32.System.Performance.PerfCounterDataType = 1
PERF_MULTIPLE_COUNTERS: win32more.Windows.Win32.System.Performance.PerfCounterDataType = 2
PERF_MULTIPLE_INSTANCES: win32more.Windows.Win32.System.Performance.PerfCounterDataType = 4
PERF_COUNTERSET: win32more.Windows.Win32.System.Performance.PerfCounterDataType = 6
PerfRegInfoType = Int32
PERF_REG_COUNTERSET_STRUCT: win32more.Windows.Win32.System.Performance.PerfRegInfoType = 1
PERF_REG_COUNTER_STRUCT: win32more.Windows.Win32.System.Performance.PerfRegInfoType = 2
PERF_REG_COUNTERSET_NAME_STRING: win32more.Windows.Win32.System.Performance.PerfRegInfoType = 3
PERF_REG_COUNTERSET_HELP_STRING: win32more.Windows.Win32.System.Performance.PerfRegInfoType = 4
PERF_REG_COUNTER_NAME_STRINGS: win32more.Windows.Win32.System.Performance.PerfRegInfoType = 5
PERF_REG_COUNTER_HELP_STRINGS: win32more.Windows.Win32.System.Performance.PerfRegInfoType = 6
PERF_REG_PROVIDER_NAME: win32more.Windows.Win32.System.Performance.PerfRegInfoType = 7
PERF_REG_PROVIDER_GUID: win32more.Windows.Win32.System.Performance.PerfRegInfoType = 8
PERF_REG_COUNTERSET_ENGLISH_NAME: win32more.Windows.Win32.System.Performance.PerfRegInfoType = 9
PERF_REG_COUNTER_ENGLISH_NAMES: win32more.Windows.Win32.System.Performance.PerfRegInfoType = 10
REAL_TIME_DATA_SOURCE_ID_FLAGS = UInt32
DATA_SOURCE_REGISTRY: win32more.Windows.Win32.System.Performance.REAL_TIME_DATA_SOURCE_ID_FLAGS = 1
DATA_SOURCE_WBEM: win32more.Windows.Win32.System.Performance.REAL_TIME_DATA_SOURCE_ID_FLAGS = 4
ReportValueTypeConstants = Int32
sysmonDefaultValue: win32more.Windows.Win32.System.Performance.ReportValueTypeConstants = 0
sysmonCurrentValue: win32more.Windows.Win32.System.Performance.ReportValueTypeConstants = 1
sysmonAverage: win32more.Windows.Win32.System.Performance.ReportValueTypeConstants = 2
sysmonMinimum: win32more.Windows.Win32.System.Performance.ReportValueTypeConstants = 3
sysmonMaximum: win32more.Windows.Win32.System.Performance.ReportValueTypeConstants = 4
ResourcePolicy = Int32
plaDeleteLargest: win32more.Windows.Win32.System.Performance.ResourcePolicy = 0
plaDeleteOldest: win32more.Windows.Win32.System.Performance.ResourcePolicy = 1
ServerDataCollectorSet = Guid('{03837531-098b-11d8-9414-505054503030}')
ServerDataCollectorSetCollection = Guid('{03837532-098b-11d8-9414-505054503030}')
SourcePropPage = Guid('{0cf32aa1-7571-11d0-93c4-00aa00a3ddea}')
StreamMode = Int32
plaFile: win32more.Windows.Win32.System.Performance.StreamMode = 1
plaRealTime: win32more.Windows.Win32.System.Performance.StreamMode = 2
plaBoth: win32more.Windows.Win32.System.Performance.StreamMode = 3
plaBuffering: win32more.Windows.Win32.System.Performance.StreamMode = 4
SysmonBatchReason = Int32
sysmonBatchNone: win32more.Windows.Win32.System.Performance.SysmonBatchReason = 0
sysmonBatchAddFiles: win32more.Windows.Win32.System.Performance.SysmonBatchReason = 1
sysmonBatchAddCounters: win32more.Windows.Win32.System.Performance.SysmonBatchReason = 2
sysmonBatchAddFilesAutoCounters: win32more.Windows.Win32.System.Performance.SysmonBatchReason = 3
SysmonDataType = Int32
sysmonDataAvg: win32more.Windows.Win32.System.Performance.SysmonDataType = 1
sysmonDataMin: win32more.Windows.Win32.System.Performance.SysmonDataType = 2
sysmonDataMax: win32more.Windows.Win32.System.Performance.SysmonDataType = 3
sysmonDataTime: win32more.Windows.Win32.System.Performance.SysmonDataType = 4
sysmonDataCount: win32more.Windows.Win32.System.Performance.SysmonDataType = 5
SysmonFileType = Int32
sysmonFileHtml: win32more.Windows.Win32.System.Performance.SysmonFileType = 1
sysmonFileReport: win32more.Windows.Win32.System.Performance.SysmonFileType = 2
sysmonFileCsv: win32more.Windows.Win32.System.Performance.SysmonFileType = 3
sysmonFileTsv: win32more.Windows.Win32.System.Performance.SysmonFileType = 4
sysmonFileBlg: win32more.Windows.Win32.System.Performance.SysmonFileType = 5
sysmonFileRetiredBlg: win32more.Windows.Win32.System.Performance.SysmonFileType = 6
sysmonFileGif: win32more.Windows.Win32.System.Performance.SysmonFileType = 7
SystemDataCollectorSet = Guid('{03837546-098b-11d8-9414-505054503030}')
SystemDataCollectorSetCollection = Guid('{03837547-098b-11d8-9414-505054503030}')
SystemMonitor = Guid('{c4d2d8e0-d1dd-11ce-940f-008029004347}')
SystemMonitor2 = Guid('{7f30578c-5f38-4612-acfe-6ed04c7b7af8}')
TraceDataProvider = Guid('{03837513-098b-11d8-9414-505054503030}')
TraceDataProviderCollection = Guid('{03837511-098b-11d8-9414-505054503030}')
TraceSession = Guid('{0383751c-098b-11d8-9414-505054503030}')
TraceSessionCollection = Guid('{03837530-098b-11d8-9414-505054503030}')
ValueMapType = Int32
plaIndex: win32more.Windows.Win32.System.Performance.ValueMapType = 1
plaFlag: win32more.Windows.Win32.System.Performance.ValueMapType = 2
plaFlagArray: win32more.Windows.Win32.System.Performance.ValueMapType = 3
plaValidation: win32more.Windows.Win32.System.Performance.ValueMapType = 4
WeekDays = Int32
plaRunOnce: win32more.Windows.Win32.System.Performance.WeekDays = 0
plaSunday: win32more.Windows.Win32.System.Performance.WeekDays = 1
plaMonday: win32more.Windows.Win32.System.Performance.WeekDays = 2
plaTuesday: win32more.Windows.Win32.System.Performance.WeekDays = 4
plaWednesday: win32more.Windows.Win32.System.Performance.WeekDays = 8
plaThursday: win32more.Windows.Win32.System.Performance.WeekDays = 16
plaFriday: win32more.Windows.Win32.System.Performance.WeekDays = 32
plaSaturday: win32more.Windows.Win32.System.Performance.WeekDays = 64
plaEveryday: win32more.Windows.Win32.System.Performance.WeekDays = 127
class _ICounterItemUnion(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{de1a6b74-9182-4c41-8e2c-24c2cd30ee83}')
    @commethod(3)
    def get_Value(self, pdblValue: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Color(self, Color: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Color(self, pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_Width(self, iWidth: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Width(self, piValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_LineStyle(self, iLineStyle: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LineStyle(self, piValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ScaleFactor(self, iScale: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ScaleFactor(self, piValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Path(self, pstrValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetValue(self, Value: POINTER(Double), Status: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetStatistics(self, Max: POINTER(Double), Min: POINTER(Double), Avg: POINTER(Double), Status: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Selected(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Selected(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Visible(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Visible(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDataAt(self, iIndex: Int32, iWhich: win32more.Windows.Win32.System.Performance.SysmonDataType, pVariant: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class _ISystemMonitorUnion(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c8a77338-265f-4de5-aa25-c7da1ce5a8f4}')
    @commethod(3)
    def get_Appearance(self, iAppearance: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Appearance(self, iAppearance: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_BackColor(self, pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_BackColor(self, Color: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_BorderStyle(self, iBorderStyle: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_BorderStyle(self, iBorderStyle: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ForeColor(self, pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ForeColor(self, Color: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Font(self, ppFont: POINTER(win32more.Windows.Win32.System.Ole.IFontDisp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def putref_Font(self, pFont: win32more.Windows.Win32.System.Ole.IFontDisp) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Counters(self, ppICounters: POINTER(win32more.Windows.Win32.System.Performance.ICounters)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_ShowVerticalGrid(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ShowVerticalGrid(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ShowHorizontalGrid(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ShowHorizontalGrid(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ShowLegend(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ShowLegend(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_ShowScaleLabels(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_ShowScaleLabels(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_ShowValueBar(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_ShowValueBar(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_MaximumScale(self, iValue: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_MaximumScale(self, piValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_MinimumScale(self, iValue: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_MinimumScale(self, piValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_UpdateInterval(self, fValue: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_UpdateInterval(self, pfValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_DisplayType(self, eDisplayType: win32more.Windows.Win32.System.Performance.DisplayTypeConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_DisplayType(self, peDisplayType: POINTER(win32more.Windows.Win32.System.Performance.DisplayTypeConstants)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_ManualUpdate(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_ManualUpdate(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_GraphTitle(self, bsTitle: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_GraphTitle(self, pbsTitle: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_YAxisLabel(self, bsTitle: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_YAxisLabel(self, pbsTitle: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def CollectSample(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def UpdateGraph(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def BrowseCounters(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def DisplayProperties(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def Counter(self, iIndex: Int32, ppICounter: POINTER(win32more.Windows.Win32.System.Performance.ICounterItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def AddCounter(self, bsPath: win32more.Windows.Win32.Foundation.BSTR, ppICounter: POINTER(win32more.Windows.Win32.System.Performance.ICounterItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def DeleteCounter(self, pCtr: win32more.Windows.Win32.System.Performance.ICounterItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_BackColorCtl(self, pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_BackColorCtl(self, Color: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_LogFileName(self, bsFileName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_LogFileName(self, bsFileName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_LogViewStart(self, StartTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_LogViewStart(self, StartTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def put_LogViewStop(self, StopTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def get_LogViewStop(self, StopTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_GridColor(self, pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def put_GridColor(self, Color: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_TimeBarColor(self, pColor: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def put_TimeBarColor(self, Color: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_Highlight(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def put_Highlight(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_ShowToolbar(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def put_ShowToolbar(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def Paste(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def Copy(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def put_ReadOnly(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_ReadOnly(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def put_ReportValueType(self, eReportValueType: win32more.Windows.Win32.System.Performance.ReportValueTypeConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def get_ReportValueType(self, peReportValueType: POINTER(win32more.Windows.Win32.System.Performance.ReportValueTypeConstants)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def put_MonitorDuplicateInstances(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def get_MonitorDuplicateInstances(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def put_DisplayFilter(self, iValue: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def get_DisplayFilter(self, piValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def get_LogFiles(self, ppILogFiles: POINTER(win32more.Windows.Win32.System.Performance.ILogFiles)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def put_DataSourceType(self, eDataSourceType: win32more.Windows.Win32.System.Performance.DataSourceTypeConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def get_DataSourceType(self, peDataSourceType: POINTER(win32more.Windows.Win32.System.Performance.DataSourceTypeConstants)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def put_SqlDsnName(self, bsSqlDsnName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def get_SqlDsnName(self, bsSqlDsnName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def put_SqlLogSetName(self, bsSqlLogSetName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def get_SqlLogSetName(self, bsSqlLogSetName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def put_EnableDigitGrouping(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def get_EnableDigitGrouping(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def put_EnableToolTips(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def get_EnableToolTips(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def put_ShowTimeAxisLabels(self, bState: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def get_ShowTimeAxisLabels(self, pbState: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def put_ChartScroll(self, bScroll: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def get_ChartScroll(self, pbScroll: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def put_DataPointCount(self, iNewCount: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def get_DataPointCount(self, piDataPointCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def ScaleToFit(self, bSelectedCountersOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def SaveAs(self, bstrFileName: win32more.Windows.Win32.Foundation.BSTR, eSysmonFileType: win32more.Windows.Win32.System.Performance.SysmonFileType) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(91)
    def Relog(self, bstrFileName: win32more.Windows.Win32.Foundation.BSTR, eSysmonFileType: win32more.Windows.Win32.System.Performance.SysmonFileType, iFilter: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def ClearData(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def get_LogSourceStartTime(self, pDate: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(94)
    def get_LogSourceStopTime(self, pDate: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(95)
    def SetLogViewRange(self, StartTime: Double, StopTime: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def GetLogViewRange(self, StartTime: POINTER(Double), StopTime: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(97)
    def BatchingLock(self, fLock: win32more.Windows.Win32.Foundation.VARIANT_BOOL, eBatchReason: win32more.Windows.Win32.System.Performance.SysmonBatchReason) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def LoadSettings(self, bstrSettingFileName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
