from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Ole
import Windows.Win32.System.Performance
import Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
PERF_AGGREGATE_MAX: UInt32 = 4
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
def QueryPerformanceCounter(lpPerformanceCount: POINTER(Int64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def QueryPerformanceFrequency(lpFrequency: POINTER(Int64)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('loadperf.dll')
def InstallPerfDllW(szComputerName: Windows.Win32.Foundation.PWSTR, lpIniFile: Windows.Win32.Foundation.PWSTR, dwFlags: UIntPtr) -> UInt32: ...
@winfunctype('loadperf.dll')
def InstallPerfDllA(szComputerName: Windows.Win32.Foundation.PSTR, lpIniFile: Windows.Win32.Foundation.PSTR, dwFlags: UIntPtr) -> UInt32: ...
@winfunctype('loadperf.dll')
def LoadPerfCounterTextStringsA(lpCommandLine: Windows.Win32.Foundation.PSTR, bQuietModeArg: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('loadperf.dll')
def LoadPerfCounterTextStringsW(lpCommandLine: Windows.Win32.Foundation.PWSTR, bQuietModeArg: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('loadperf.dll')
def UnloadPerfCounterTextStringsW(lpCommandLine: Windows.Win32.Foundation.PWSTR, bQuietModeArg: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('loadperf.dll')
def UnloadPerfCounterTextStringsA(lpCommandLine: Windows.Win32.Foundation.PSTR, bQuietModeArg: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('loadperf.dll')
def UpdatePerfNameFilesA(szNewCtrFilePath: Windows.Win32.Foundation.PSTR, szNewHlpFilePath: Windows.Win32.Foundation.PSTR, szLanguageID: Windows.Win32.Foundation.PSTR, dwFlags: UIntPtr) -> UInt32: ...
@winfunctype('loadperf.dll')
def UpdatePerfNameFilesW(szNewCtrFilePath: Windows.Win32.Foundation.PWSTR, szNewHlpFilePath: Windows.Win32.Foundation.PWSTR, szLanguageID: Windows.Win32.Foundation.PWSTR, dwFlags: UIntPtr) -> UInt32: ...
@winfunctype('loadperf.dll')
def SetServiceAsTrustedA(szReserved: Windows.Win32.Foundation.PSTR, szServiceName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('loadperf.dll')
def SetServiceAsTrustedW(szReserved: Windows.Win32.Foundation.PWSTR, szServiceName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('loadperf.dll')
def BackupPerfRegistryToFileW(szFileName: Windows.Win32.Foundation.PWSTR, szCommentString: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('loadperf.dll')
def RestorePerfRegistryFromFileW(szFileName: Windows.Win32.Foundation.PWSTR, szLangId: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfStartProvider(ProviderGuid: POINTER(Guid), ControlCallback: Windows.Win32.System.Performance.PERFLIBREQUEST, phProvider: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfStartProviderEx(ProviderGuid: POINTER(Guid), ProviderContext: POINTER(Windows.Win32.System.Performance.PERF_PROVIDER_CONTEXT_head), Provider: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfStopProvider(ProviderHandle: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfSetCounterSetInfo(ProviderHandle: Windows.Win32.Foundation.HANDLE, Template: POINTER(Windows.Win32.System.Performance.PERF_COUNTERSET_INFO_head), TemplateSize: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfCreateInstance(ProviderHandle: Windows.Win32.Foundation.HANDLE, CounterSetGuid: POINTER(Guid), Name: Windows.Win32.Foundation.PWSTR, Id: UInt32) -> POINTER(Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE_head): ...
@winfunctype('ADVAPI32.dll')
def PerfDeleteInstance(Provider: Windows.Win32.Foundation.HANDLE, InstanceBlock: POINTER(Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE_head)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfQueryInstance(ProviderHandle: Windows.Win32.Foundation.HANDLE, CounterSetGuid: POINTER(Guid), Name: Windows.Win32.Foundation.PWSTR, Id: UInt32) -> POINTER(Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE_head): ...
@winfunctype('ADVAPI32.dll')
def PerfSetCounterRefValue(Provider: Windows.Win32.Foundation.HANDLE, Instance: POINTER(Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Address: VoidPtr) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfSetULongCounterValue(Provider: Windows.Win32.Foundation.HANDLE, Instance: POINTER(Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Value: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfSetULongLongCounterValue(Provider: Windows.Win32.Foundation.HANDLE, Instance: POINTER(Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Value: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfIncrementULongCounterValue(Provider: Windows.Win32.Foundation.HANDLE, Instance: POINTER(Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Value: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfIncrementULongLongCounterValue(Provider: Windows.Win32.Foundation.HANDLE, Instance: POINTER(Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Value: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfDecrementULongCounterValue(Provider: Windows.Win32.Foundation.HANDLE, Instance: POINTER(Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Value: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfDecrementULongLongCounterValue(Provider: Windows.Win32.Foundation.HANDLE, Instance: POINTER(Windows.Win32.System.Performance.PERF_COUNTERSET_INSTANCE_head), CounterId: UInt32, Value: UInt64) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfEnumerateCounterSet(szMachine: Windows.Win32.Foundation.PWSTR, pCounterSetIds: POINTER(Guid), cCounterSetIds: UInt32, pcCounterSetIdsActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfEnumerateCounterSetInstances(szMachine: Windows.Win32.Foundation.PWSTR, pCounterSetId: POINTER(Guid), pInstances: POINTER(Windows.Win32.System.Performance.PERF_INSTANCE_HEADER_head), cbInstances: UInt32, pcbInstancesActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfQueryCounterSetRegistrationInfo(szMachine: Windows.Win32.Foundation.PWSTR, pCounterSetId: POINTER(Guid), requestCode: Windows.Win32.System.Performance.PerfRegInfoType, requestLangId: UInt32, pbRegInfo: POINTER(Byte), cbRegInfo: UInt32, pcbRegInfoActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfOpenQueryHandle(szMachine: Windows.Win32.Foundation.PWSTR, phQuery: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfCloseQueryHandle(hQuery: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfQueryCounterInfo(hQuery: Windows.Win32.Foundation.HANDLE, pCounters: POINTER(Windows.Win32.System.Performance.PERF_COUNTER_IDENTIFIER_head), cbCounters: UInt32, pcbCountersActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfQueryCounterData(hQuery: Windows.Win32.Foundation.HANDLE, pCounterBlock: POINTER(Windows.Win32.System.Performance.PERF_DATA_HEADER_head), cbCounterBlock: UInt32, pcbCounterBlockActual: POINTER(UInt32)) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfAddCounters(hQuery: Windows.Win32.Foundation.HANDLE, pCounters: POINTER(Windows.Win32.System.Performance.PERF_COUNTER_IDENTIFIER_head), cbCounters: UInt32) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def PerfDeleteCounters(hQuery: Windows.Win32.Foundation.HANDLE, pCounters: POINTER(Windows.Win32.System.Performance.PERF_COUNTER_IDENTIFIER_head), cbCounters: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDllVersion(lpdwVersion: POINTER(Windows.Win32.System.Performance.PDH_DLL_VERSION)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhOpenQueryW(szDataSource: Windows.Win32.Foundation.PWSTR, dwUserData: UIntPtr, phQuery: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhOpenQueryA(szDataSource: Windows.Win32.Foundation.PSTR, dwUserData: UIntPtr, phQuery: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhAddCounterW(hQuery: IntPtr, szFullCounterPath: Windows.Win32.Foundation.PWSTR, dwUserData: UIntPtr, phCounter: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhAddCounterA(hQuery: IntPtr, szFullCounterPath: Windows.Win32.Foundation.PSTR, dwUserData: UIntPtr, phCounter: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhAddEnglishCounterW(hQuery: IntPtr, szFullCounterPath: Windows.Win32.Foundation.PWSTR, dwUserData: UIntPtr, phCounter: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhAddEnglishCounterA(hQuery: IntPtr, szFullCounterPath: Windows.Win32.Foundation.PSTR, dwUserData: UIntPtr, phCounter: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCollectQueryDataWithTime(hQuery: IntPtr, pllTimeStamp: POINTER(Int64)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhValidatePathExW(hDataSource: IntPtr, szFullPathBuffer: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhValidatePathExA(hDataSource: IntPtr, szFullPathBuffer: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhRemoveCounter(hCounter: IntPtr) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCollectQueryData(hQuery: IntPtr) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCloseQuery(hQuery: IntPtr) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetFormattedCounterValue(hCounter: IntPtr, dwFormat: Windows.Win32.System.Performance.PDH_FMT, lpdwType: POINTER(UInt32), pValue: POINTER(Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetFormattedCounterArrayA(hCounter: IntPtr, dwFormat: Windows.Win32.System.Performance.PDH_FMT, lpdwBufferSize: POINTER(UInt32), lpdwItemCount: POINTER(UInt32), ItemBuffer: POINTER(Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE_ITEM_A_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetFormattedCounterArrayW(hCounter: IntPtr, dwFormat: Windows.Win32.System.Performance.PDH_FMT, lpdwBufferSize: POINTER(UInt32), lpdwItemCount: POINTER(UInt32), ItemBuffer: POINTER(Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE_ITEM_W_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetRawCounterValue(hCounter: IntPtr, lpdwType: POINTER(UInt32), pValue: POINTER(Windows.Win32.System.Performance.PDH_RAW_COUNTER_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetRawCounterArrayA(hCounter: IntPtr, lpdwBufferSize: POINTER(UInt32), lpdwItemCount: POINTER(UInt32), ItemBuffer: POINTER(Windows.Win32.System.Performance.PDH_RAW_COUNTER_ITEM_A_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetRawCounterArrayW(hCounter: IntPtr, lpdwBufferSize: POINTER(UInt32), lpdwItemCount: POINTER(UInt32), ItemBuffer: POINTER(Windows.Win32.System.Performance.PDH_RAW_COUNTER_ITEM_W_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCalculateCounterFromRawValue(hCounter: IntPtr, dwFormat: Windows.Win32.System.Performance.PDH_FMT, rawValue1: POINTER(Windows.Win32.System.Performance.PDH_RAW_COUNTER_head), rawValue2: POINTER(Windows.Win32.System.Performance.PDH_RAW_COUNTER_head), fmtValue: POINTER(Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhComputeCounterStatistics(hCounter: IntPtr, dwFormat: Windows.Win32.System.Performance.PDH_FMT, dwFirstEntry: UInt32, dwNumEntries: UInt32, lpRawValueArray: POINTER(Windows.Win32.System.Performance.PDH_RAW_COUNTER_head), data: POINTER(Windows.Win32.System.Performance.PDH_STATISTICS_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetCounterInfoW(hCounter: IntPtr, bRetrieveExplainText: Windows.Win32.Foundation.BOOLEAN, pdwBufferSize: POINTER(UInt32), lpBuffer: POINTER(Windows.Win32.System.Performance.PDH_COUNTER_INFO_W_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetCounterInfoA(hCounter: IntPtr, bRetrieveExplainText: Windows.Win32.Foundation.BOOLEAN, pdwBufferSize: POINTER(UInt32), lpBuffer: POINTER(Windows.Win32.System.Performance.PDH_COUNTER_INFO_A_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSetCounterScaleFactor(hCounter: IntPtr, lFactor: Int32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhConnectMachineW(szMachineName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhConnectMachineA(szMachineName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumMachinesW(szDataSource: Windows.Win32.Foundation.PWSTR, mszMachineList: Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumMachinesA(szDataSource: Windows.Win32.Foundation.PSTR, mszMachineList: Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectsW(szDataSource: Windows.Win32.Foundation.PWSTR, szMachineName: Windows.Win32.Foundation.PWSTR, mszObjectList: Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32), dwDetailLevel: Windows.Win32.System.Performance.PERF_DETAIL, bRefresh: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectsA(szDataSource: Windows.Win32.Foundation.PSTR, szMachineName: Windows.Win32.Foundation.PSTR, mszObjectList: Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32), dwDetailLevel: Windows.Win32.System.Performance.PERF_DETAIL, bRefresh: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectItemsW(szDataSource: Windows.Win32.Foundation.PWSTR, szMachineName: Windows.Win32.Foundation.PWSTR, szObjectName: Windows.Win32.Foundation.PWSTR, mszCounterList: Windows.Win32.Foundation.PWSTR, pcchCounterListLength: POINTER(UInt32), mszInstanceList: Windows.Win32.Foundation.PWSTR, pcchInstanceListLength: POINTER(UInt32), dwDetailLevel: Windows.Win32.System.Performance.PERF_DETAIL, dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectItemsA(szDataSource: Windows.Win32.Foundation.PSTR, szMachineName: Windows.Win32.Foundation.PSTR, szObjectName: Windows.Win32.Foundation.PSTR, mszCounterList: Windows.Win32.Foundation.PSTR, pcchCounterListLength: POINTER(UInt32), mszInstanceList: Windows.Win32.Foundation.PSTR, pcchInstanceListLength: POINTER(UInt32), dwDetailLevel: Windows.Win32.System.Performance.PERF_DETAIL, dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhMakeCounterPathW(pCounterPathElements: POINTER(Windows.Win32.System.Performance.PDH_COUNTER_PATH_ELEMENTS_W_head), szFullPathBuffer: Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32), dwFlags: Windows.Win32.System.Performance.PDH_PATH_FLAGS) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhMakeCounterPathA(pCounterPathElements: POINTER(Windows.Win32.System.Performance.PDH_COUNTER_PATH_ELEMENTS_A_head), szFullPathBuffer: Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32), dwFlags: Windows.Win32.System.Performance.PDH_PATH_FLAGS) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhParseCounterPathW(szFullPathBuffer: Windows.Win32.Foundation.PWSTR, pCounterPathElements: POINTER(Windows.Win32.System.Performance.PDH_COUNTER_PATH_ELEMENTS_W_head), pdwBufferSize: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhParseCounterPathA(szFullPathBuffer: Windows.Win32.Foundation.PSTR, pCounterPathElements: POINTER(Windows.Win32.System.Performance.PDH_COUNTER_PATH_ELEMENTS_A_head), pdwBufferSize: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhParseInstanceNameW(szInstanceString: Windows.Win32.Foundation.PWSTR, szInstanceName: Windows.Win32.Foundation.PWSTR, pcchInstanceNameLength: POINTER(UInt32), szParentName: Windows.Win32.Foundation.PWSTR, pcchParentNameLength: POINTER(UInt32), lpIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhParseInstanceNameA(szInstanceString: Windows.Win32.Foundation.PSTR, szInstanceName: Windows.Win32.Foundation.PSTR, pcchInstanceNameLength: POINTER(UInt32), szParentName: Windows.Win32.Foundation.PSTR, pcchParentNameLength: POINTER(UInt32), lpIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhValidatePathW(szFullPathBuffer: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhValidatePathA(szFullPathBuffer: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfObjectW(szDataSource: Windows.Win32.Foundation.PWSTR, szMachineName: Windows.Win32.Foundation.PWSTR, szDefaultObjectName: Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfObjectA(szDataSource: Windows.Win32.Foundation.PSTR, szMachineName: Windows.Win32.Foundation.PSTR, szDefaultObjectName: Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfCounterW(szDataSource: Windows.Win32.Foundation.PWSTR, szMachineName: Windows.Win32.Foundation.PWSTR, szObjectName: Windows.Win32.Foundation.PWSTR, szDefaultCounterName: Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfCounterA(szDataSource: Windows.Win32.Foundation.PSTR, szMachineName: Windows.Win32.Foundation.PSTR, szObjectName: Windows.Win32.Foundation.PSTR, szDefaultCounterName: Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBrowseCountersW(pBrowseDlgData: POINTER(Windows.Win32.System.Performance.PDH_BROWSE_DLG_CONFIG_W_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBrowseCountersA(pBrowseDlgData: POINTER(Windows.Win32.System.Performance.PDH_BROWSE_DLG_CONFIG_A_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandCounterPathW(szWildCardPath: Windows.Win32.Foundation.PWSTR, mszExpandedPathList: Windows.Win32.Foundation.PWSTR, pcchPathListLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandCounterPathA(szWildCardPath: Windows.Win32.Foundation.PSTR, mszExpandedPathList: Windows.Win32.Foundation.PSTR, pcchPathListLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhLookupPerfNameByIndexW(szMachineName: Windows.Win32.Foundation.PWSTR, dwNameIndex: UInt32, szNameBuffer: Windows.Win32.Foundation.PWSTR, pcchNameBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhLookupPerfNameByIndexA(szMachineName: Windows.Win32.Foundation.PSTR, dwNameIndex: UInt32, szNameBuffer: Windows.Win32.Foundation.PSTR, pcchNameBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhLookupPerfIndexByNameW(szMachineName: Windows.Win32.Foundation.PWSTR, szNameBuffer: Windows.Win32.Foundation.PWSTR, pdwIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhLookupPerfIndexByNameA(szMachineName: Windows.Win32.Foundation.PSTR, szNameBuffer: Windows.Win32.Foundation.PSTR, pdwIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandWildCardPathA(szDataSource: Windows.Win32.Foundation.PSTR, szWildCardPath: Windows.Win32.Foundation.PSTR, mszExpandedPathList: Windows.Win32.Foundation.PSTR, pcchPathListLength: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandWildCardPathW(szDataSource: Windows.Win32.Foundation.PWSTR, szWildCardPath: Windows.Win32.Foundation.PWSTR, mszExpandedPathList: Windows.Win32.Foundation.PWSTR, pcchPathListLength: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhOpenLogW(szLogFileName: Windows.Win32.Foundation.PWSTR, dwAccessFlags: Windows.Win32.System.Performance.PDH_LOG, lpdwLogType: POINTER(Windows.Win32.System.Performance.PDH_LOG_TYPE), hQuery: IntPtr, dwMaxSize: UInt32, szUserCaption: Windows.Win32.Foundation.PWSTR, phLog: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhOpenLogA(szLogFileName: Windows.Win32.Foundation.PSTR, dwAccessFlags: Windows.Win32.System.Performance.PDH_LOG, lpdwLogType: POINTER(Windows.Win32.System.Performance.PDH_LOG_TYPE), hQuery: IntPtr, dwMaxSize: UInt32, szUserCaption: Windows.Win32.Foundation.PSTR, phLog: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhUpdateLogW(hLog: IntPtr, szUserString: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhUpdateLogA(hLog: IntPtr, szUserString: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhUpdateLogFileCatalog(hLog: IntPtr) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetLogFileSize(hLog: IntPtr, llSize: POINTER(Int64)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCloseLog(hLog: IntPtr, dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSelectDataSourceW(hWndOwner: Windows.Win32.Foundation.HWND, dwFlags: Windows.Win32.System.Performance.PDH_SELECT_DATA_SOURCE_FLAGS, szDataSource: Windows.Win32.Foundation.PWSTR, pcchBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSelectDataSourceA(hWndOwner: Windows.Win32.Foundation.HWND, dwFlags: Windows.Win32.System.Performance.PDH_SELECT_DATA_SOURCE_FLAGS, szDataSource: Windows.Win32.Foundation.PSTR, pcchBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhIsRealTimeQuery(hQuery: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('pdh.dll')
def PdhSetQueryTimeRange(hQuery: IntPtr, pInfo: POINTER(Windows.Win32.System.Performance.PDH_TIME_INFO_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDataSourceTimeRangeW(szDataSource: Windows.Win32.Foundation.PWSTR, pdwNumEntries: POINTER(UInt32), pInfo: POINTER(Windows.Win32.System.Performance.PDH_TIME_INFO_head), pdwBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDataSourceTimeRangeA(szDataSource: Windows.Win32.Foundation.PSTR, pdwNumEntries: POINTER(UInt32), pInfo: POINTER(Windows.Win32.System.Performance.PDH_TIME_INFO_head), pdwBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCollectQueryDataEx(hQuery: IntPtr, dwIntervalTime: UInt32, hNewDataEvent: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhFormatFromRawValue(dwCounterType: UInt32, dwFormat: Windows.Win32.System.Performance.PDH_FMT, pTimeBase: POINTER(Int64), pRawValue1: POINTER(Windows.Win32.System.Performance.PDH_RAW_COUNTER_head), pRawValue2: POINTER(Windows.Win32.System.Performance.PDH_RAW_COUNTER_head), pFmtValue: POINTER(Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetCounterTimeBase(hCounter: IntPtr, pTimeBase: POINTER(Int64)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhReadRawLogRecord(hLog: IntPtr, ftRecord: Windows.Win32.Foundation.FILETIME, pRawLogRecord: POINTER(Windows.Win32.System.Performance.PDH_RAW_LOG_RECORD_head), pdwBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSetDefaultRealTimeDataSource(dwDataSourceId: Windows.Win32.System.Performance.REAL_TIME_DATA_SOURCE_ID_FLAGS) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBindInputDataSourceW(phDataSource: POINTER(IntPtr), LogFileNameList: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBindInputDataSourceA(phDataSource: POINTER(IntPtr), LogFileNameList: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhOpenQueryH(hDataSource: IntPtr, dwUserData: UIntPtr, phQuery: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumMachinesHW(hDataSource: IntPtr, mszMachineList: Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumMachinesHA(hDataSource: IntPtr, mszMachineList: Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectsHW(hDataSource: IntPtr, szMachineName: Windows.Win32.Foundation.PWSTR, mszObjectList: Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32), dwDetailLevel: Windows.Win32.System.Performance.PERF_DETAIL, bRefresh: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectsHA(hDataSource: IntPtr, szMachineName: Windows.Win32.Foundation.PSTR, mszObjectList: Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32), dwDetailLevel: Windows.Win32.System.Performance.PERF_DETAIL, bRefresh: Windows.Win32.Foundation.BOOL) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectItemsHW(hDataSource: IntPtr, szMachineName: Windows.Win32.Foundation.PWSTR, szObjectName: Windows.Win32.Foundation.PWSTR, mszCounterList: Windows.Win32.Foundation.PWSTR, pcchCounterListLength: POINTER(UInt32), mszInstanceList: Windows.Win32.Foundation.PWSTR, pcchInstanceListLength: POINTER(UInt32), dwDetailLevel: Windows.Win32.System.Performance.PERF_DETAIL, dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumObjectItemsHA(hDataSource: IntPtr, szMachineName: Windows.Win32.Foundation.PSTR, szObjectName: Windows.Win32.Foundation.PSTR, mszCounterList: Windows.Win32.Foundation.PSTR, pcchCounterListLength: POINTER(UInt32), mszInstanceList: Windows.Win32.Foundation.PSTR, pcchInstanceListLength: POINTER(UInt32), dwDetailLevel: Windows.Win32.System.Performance.PERF_DETAIL, dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandWildCardPathHW(hDataSource: IntPtr, szWildCardPath: Windows.Win32.Foundation.PWSTR, mszExpandedPathList: Windows.Win32.Foundation.PWSTR, pcchPathListLength: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhExpandWildCardPathHA(hDataSource: IntPtr, szWildCardPath: Windows.Win32.Foundation.PSTR, mszExpandedPathList: Windows.Win32.Foundation.PSTR, pcchPathListLength: POINTER(UInt32), dwFlags: UInt32) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDataSourceTimeRangeH(hDataSource: IntPtr, pdwNumEntries: POINTER(UInt32), pInfo: POINTER(Windows.Win32.System.Performance.PDH_TIME_INFO_head), pdwBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfObjectHW(hDataSource: IntPtr, szMachineName: Windows.Win32.Foundation.PWSTR, szDefaultObjectName: Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfObjectHA(hDataSource: IntPtr, szMachineName: Windows.Win32.Foundation.PSTR, szDefaultObjectName: Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfCounterHW(hDataSource: IntPtr, szMachineName: Windows.Win32.Foundation.PWSTR, szObjectName: Windows.Win32.Foundation.PWSTR, szDefaultCounterName: Windows.Win32.Foundation.PWSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetDefaultPerfCounterHA(hDataSource: IntPtr, szMachineName: Windows.Win32.Foundation.PSTR, szObjectName: Windows.Win32.Foundation.PSTR, szDefaultCounterName: Windows.Win32.Foundation.PSTR, pcchBufferSize: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBrowseCountersHW(pBrowseDlgData: POINTER(Windows.Win32.System.Performance.PDH_BROWSE_DLG_CONFIG_HW_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhBrowseCountersHA(pBrowseDlgData: POINTER(Windows.Win32.System.Performance.PDH_BROWSE_DLG_CONFIG_HA_head)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhVerifySQLDBW(szDataSource: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhVerifySQLDBA(szDataSource: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCreateSQLTablesW(szDataSource: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhCreateSQLTablesA(szDataSource: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumLogSetNamesW(szDataSource: Windows.Win32.Foundation.PWSTR, mszDataSetNameList: Windows.Win32.Foundation.PWSTR, pcchBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhEnumLogSetNamesA(szDataSource: Windows.Win32.Foundation.PSTR, mszDataSetNameList: Windows.Win32.Foundation.PSTR, pcchBufferLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhGetLogSetGUID(hLog: IntPtr, pGuid: POINTER(Guid), pRunId: POINTER(Int32)) -> UInt32: ...
@winfunctype('pdh.dll')
def PdhSetLogSetRunID(hLog: IntPtr, RunId: Int32) -> UInt32: ...
AppearPropPage = Guid('{e49741e9-93a8-4ab1-8e96-bf4482282e9c}')
AutoPathFormat = Int32
AutoPathFormat_plaNone: AutoPathFormat = 0
AutoPathFormat_plaPattern: AutoPathFormat = 1
AutoPathFormat_plaComputer: AutoPathFormat = 2
AutoPathFormat_plaMonthDayHour: AutoPathFormat = 256
AutoPathFormat_plaSerialNumber: AutoPathFormat = 512
AutoPathFormat_plaYearDayOfYear: AutoPathFormat = 1024
AutoPathFormat_plaYearMonth: AutoPathFormat = 2048
AutoPathFormat_plaYearMonthDay: AutoPathFormat = 4096
AutoPathFormat_plaYearMonthDayHour: AutoPathFormat = 8192
AutoPathFormat_plaMonthDayHourMinute: AutoPathFormat = 16384
BootTraceSession = Guid('{03837538-098b-11d8-9414-505054503030}')
BootTraceSessionCollection = Guid('{03837539-098b-11d8-9414-505054503030}')
ClockType = Int32
ClockType_plaTimeStamp: ClockType = 0
ClockType_plaPerformance: ClockType = 1
ClockType_plaSystem: ClockType = 2
ClockType_plaCycle: ClockType = 3
CommitMode = Int32
CommitMode_plaCreateNew: CommitMode = 1
CommitMode_plaModify: CommitMode = 2
CommitMode_plaCreateOrModify: CommitMode = 3
CommitMode_plaUpdateRunningInstance: CommitMode = 16
CommitMode_plaFlushTrace: CommitMode = 32
CommitMode_plaValidateOnly: CommitMode = 4096
CounterItem = Guid('{c4d2d8e0-d1dd-11ce-940f-008029004348}')
CounterItem2 = Guid('{43196c62-c31f-4ce3-a02e-79efe0f6a525}')
@winfunctype_pointer
def CounterPathCallBack(param0: UIntPtr) -> Int32: ...
CounterPropPage = Guid('{cf948561-ede8-11ce-941e-008029004347}')
Counters = Guid('{b2b066d2-2aac-11cf-942f-008029004347}')
class DICounterItem(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c08c4ff2-0e2e-11cf-942c-008029004347}')
class DILogFileItem(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8d093ffc-f777-4917-82d1-833fbc54c58f}')
class DISystemMonitor(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{13d73d81-c32e-11cf-9398-00aa00a3ddea}')
class DISystemMonitorEvents(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{84979930-4ab3-11cf-943a-008029004347}')
class DISystemMonitorInternal(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{194eb242-c32c-11cf-9398-00aa00a3ddea}')
DataCollectorSet = Guid('{03837521-098b-11d8-9414-505054503030}')
DataCollectorSetCollection = Guid('{03837525-098b-11d8-9414-505054503030}')
DataCollectorSetStatus = Int32
DataCollectorSetStatus_plaStopped: DataCollectorSetStatus = 0
DataCollectorSetStatus_plaRunning: DataCollectorSetStatus = 1
DataCollectorSetStatus_plaCompiling: DataCollectorSetStatus = 2
DataCollectorSetStatus_plaPending: DataCollectorSetStatus = 3
DataCollectorSetStatus_plaUndefined: DataCollectorSetStatus = 4
DataCollectorType = Int32
DataCollectorType_plaPerformanceCounter: DataCollectorType = 0
DataCollectorType_plaTrace: DataCollectorType = 1
DataCollectorType_plaConfiguration: DataCollectorType = 2
DataCollectorType_plaAlert: DataCollectorType = 3
DataCollectorType_plaApiTrace: DataCollectorType = 4
DataManagerSteps = Int32
DataManagerSteps_plaCreateReport: DataManagerSteps = 1
DataManagerSteps_plaRunRules: DataManagerSteps = 2
DataManagerSteps_plaCreateHtml: DataManagerSteps = 4
DataManagerSteps_plaFolderActions: DataManagerSteps = 8
DataManagerSteps_plaResourceFreeing: DataManagerSteps = 16
DataSourceTypeConstants = Int32
DataSourceTypeConstants_sysmonNullDataSource: DataSourceTypeConstants = -1
DataSourceTypeConstants_sysmonCurrentActivity: DataSourceTypeConstants = 1
DataSourceTypeConstants_sysmonLogFiles: DataSourceTypeConstants = 2
DataSourceTypeConstants_sysmonSqlLog: DataSourceTypeConstants = 3
DisplayTypeConstants = Int32
DisplayTypeConstants_sysmonLineGraph: DisplayTypeConstants = 1
DisplayTypeConstants_sysmonHistogram: DisplayTypeConstants = 2
DisplayTypeConstants_sysmonReport: DisplayTypeConstants = 3
DisplayTypeConstants_sysmonChartArea: DisplayTypeConstants = 4
DisplayTypeConstants_sysmonChartStackedArea: DisplayTypeConstants = 5
FileFormat = Int32
FileFormat_plaCommaSeparated: FileFormat = 0
FileFormat_plaTabSeparated: FileFormat = 1
FileFormat_plaSql: FileFormat = 2
FileFormat_plaBinary: FileFormat = 3
FolderActionSteps = Int32
FolderActionSteps_plaCreateCab: FolderActionSteps = 1
FolderActionSteps_plaDeleteData: FolderActionSteps = 2
FolderActionSteps_plaSendCab: FolderActionSteps = 4
FolderActionSteps_plaDeleteCab: FolderActionSteps = 8
FolderActionSteps_plaDeleteReport: FolderActionSteps = 16
GeneralPropPage = Guid('{c3e5d3d2-1a03-11cf-942d-008029004347}')
GraphPropPage = Guid('{c3e5d3d3-1a03-11cf-942d-008029004347}')
class IAlertDataCollector(ComPtr):
    extends: Windows.Win32.System.Performance.IDataCollector
    _iid_ = Guid('{03837516-098b-11d8-9414-505054503030}')
    @commethod(32)
    def get_AlertThresholds(self, alerts: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_AlertThresholds(self, alerts: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_EventLog(self, log: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_EventLog(self, log: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_SampleInterval(self, interval: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_SampleInterval(self, interval: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_Task(self, task: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_Task(self, task: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_TaskRunAsSelf(self, RunAsSelf: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_TaskRunAsSelf(self, RunAsSelf: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_TaskArguments(self, task: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_TaskArguments(self, task: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_TaskUserTextArguments(self, task: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_TaskUserTextArguments(self, task: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_TriggerDataCollectorSet(self, name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_TriggerDataCollectorSet(self, name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IApiTracingDataCollector(ComPtr):
    extends: Windows.Win32.System.Performance.IDataCollector
    _iid_ = Guid('{0383751a-098b-11d8-9414-505054503030}')
    @commethod(32)
    def get_LogApiNamesOnly(self, logapinames: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_LogApiNamesOnly(self, logapinames: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_LogApisRecursively(self, logrecursively: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_LogApisRecursively(self, logrecursively: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_ExePath(self, exepath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_ExePath(self, exepath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_LogFilePath(self, logfilepath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_LogFilePath(self, logfilepath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_IncludeModules(self, includemodules: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_IncludeModules(self, includemodules: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_IncludeApis(self, includeapis: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_IncludeApis(self, includeapis: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_ExcludeApis(self, excludeapis: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_ExcludeApis(self, excludeapis: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IConfigurationDataCollector(ComPtr):
    extends: Windows.Win32.System.Performance.IDataCollector
    _iid_ = Guid('{03837514-098b-11d8-9414-505054503030}')
    @commethod(32)
    def get_FileMaxCount(self, count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_FileMaxCount(self, count: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_FileMaxRecursiveDepth(self, depth: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_FileMaxRecursiveDepth(self, depth: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_FileMaxTotalSize(self, size: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_FileMaxTotalSize(self, size: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_Files(self, Files: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_Files(self, Files: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_ManagementQueries(self, Queries: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_ManagementQueries(self, Queries: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_QueryNetworkAdapters(self, network: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_QueryNetworkAdapters(self, network: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_RegistryKeys(self, query: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_RegistryKeys(self, query: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_RegistryMaxRecursiveDepth(self, depth: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_RegistryMaxRecursiveDepth(self, depth: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_SystemStateFile(self, FileName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_SystemStateFile(self, FileName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ICounterItem(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{771a9520-ee28-11ce-941e-008029004347}')
    @commethod(3)
    def get_Value(self, pdblValue: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Color(self, Color: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Color(self, pColor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_Width(self, iWidth: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Width(self, piValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_LineStyle(self, iLineStyle: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LineStyle(self, piValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ScaleFactor(self, iScale: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ScaleFactor(self, piValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Path(self, pstrValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetValue(self, Value: POINTER(Double), Status: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetStatistics(self, Max: POINTER(Double), Min: POINTER(Double), Avg: POINTER(Double), Status: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class ICounterItem2(ComPtr):
    extends: Windows.Win32.System.Performance.ICounterItem
    _iid_ = Guid('{eefcd4e1-ea1c-4435-b7f4-e341ba03b4f9}')
    @commethod(15)
    def put_Selected(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Selected(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Visible(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Visible(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDataAt(self, iIndex: Int32, iWhich: Windows.Win32.System.Performance.SysmonDataType, pVariant: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICounters(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{79167962-28fc-11cf-942f-008029004347}')
    @commethod(7)
    def get_Count(self, pLong: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, ppIunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, index: Windows.Win32.System.Variant.VARIANT, ppI: POINTER(Windows.Win32.System.Performance.DICounterItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pathname: Windows.Win32.Foundation.BSTR, ppI: POINTER(Windows.Win32.System.Performance.DICounterItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, index: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IDataCollector(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{038374ff-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_DataCollectorSet(self, group: POINTER(Windows.Win32.System.Performance.IDataCollectorSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_DataCollectorSet(self, group: Windows.Win32.System.Performance.IDataCollectorSet_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_DataCollectorType(self, type: POINTER(Windows.Win32.System.Performance.DataCollectorType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_FileName(self, name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_FileName(self, name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_FileNameFormat(self, format: POINTER(Windows.Win32.System.Performance.AutoPathFormat)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_FileNameFormat(self, format: Windows.Win32.System.Performance.AutoPathFormat) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_FileNameFormatPattern(self, pattern: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_FileNameFormatPattern(self, pattern: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_LatestOutputLocation(self, path: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_LatestOutputLocation(self, path: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_LogAppend(self, append: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_LogAppend(self, append: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_LogCircular(self, circular: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_LogCircular(self, circular: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_LogOverwrite(self, overwrite: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_LogOverwrite(self, overwrite: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Name(self, name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Name(self, name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_OutputLocation(self, path: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Index(self, index: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_Index(self, index: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_Xml(self, Xml: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetXml(self, Xml: Windows.Win32.Foundation.BSTR, Validation: POINTER(Windows.Win32.System.Performance.IValueMap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def CreateOutputLocation(self, Latest: Windows.Win32.Foundation.VARIANT_BOOL, Location: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IDataCollectorCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837502-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Count(self, retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, index: Windows.Win32.System.Variant.VARIANT, collector: POINTER(Windows.Win32.System.Performance.IDataCollector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, retVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, collector: Windows.Win32.System.Performance.IDataCollector_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, collector: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(self, collectors: Windows.Win32.System.Performance.IDataCollectorCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateDataCollectorFromXml(self, bstrXml: Windows.Win32.Foundation.BSTR, pValidation: POINTER(Windows.Win32.System.Performance.IValueMap_head), pCollector: POINTER(Windows.Win32.System.Performance.IDataCollector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateDataCollector(self, Type: Windows.Win32.System.Performance.DataCollectorType, Collector: POINTER(Windows.Win32.System.Performance.IDataCollector_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDataCollectorSet(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837520-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_DataCollectors(self, collectors: POINTER(Windows.Win32.System.Performance.IDataCollectorCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Duration(self, seconds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_Duration(self, seconds: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Description(self, description: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_Description(self, description: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_DescriptionUnresolved(self, Descr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_DisplayName(self, DisplayName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_DisplayName(self, DisplayName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_DisplayNameUnresolved(self, name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Keywords(self, keywords: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Keywords(self, keywords: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_LatestOutputLocation(self, path: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_LatestOutputLocation(self, path: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Name(self, name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_OutputLocation(self, path: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_RootPath(self, folder: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_RootPath(self, folder: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Segment(self, segment: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Segment(self, segment: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_SegmentMaxDuration(self, seconds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_SegmentMaxDuration(self, seconds: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_SegmentMaxSize(self, size: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_SegmentMaxSize(self, size: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_SerialNumber(self, index: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_SerialNumber(self, index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def get_Server(self, server: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_Status(self, status: POINTER(Windows.Win32.System.Performance.DataCollectorSetStatus)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_Subdirectory(self, folder: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_Subdirectory(self, folder: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_SubdirectoryFormat(self, format: POINTER(Windows.Win32.System.Performance.AutoPathFormat)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_SubdirectoryFormat(self, format: Windows.Win32.System.Performance.AutoPathFormat) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_SubdirectoryFormatPattern(self, pattern: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_SubdirectoryFormatPattern(self, pattern: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_Task(self, task: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_Task(self, task: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_TaskRunAsSelf(self, RunAsSelf: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_TaskRunAsSelf(self, RunAsSelf: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_TaskArguments(self, task: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_TaskArguments(self, task: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_TaskUserTextArguments(self, UserText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_TaskUserTextArguments(self, UserText: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_Schedules(self, ppSchedules: POINTER(Windows.Win32.System.Performance.IScheduleCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def get_SchedulesEnabled(self, enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def put_SchedulesEnabled(self, enabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def get_UserAccount(self, user: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def get_Xml(self, xml: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_Security(self, pbstrSecurity: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def put_Security(self, bstrSecurity: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_StopOnCompletion(self, Stop: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def put_StopOnCompletion(self, Stop: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_DataManager(self, DataManager: POINTER(Windows.Win32.System.Performance.IDataManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def SetCredentials(self, user: Windows.Win32.Foundation.BSTR, password: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def Query(self, name: Windows.Win32.Foundation.BSTR, server: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def Commit(self, name: Windows.Win32.Foundation.BSTR, server: Windows.Win32.Foundation.BSTR, mode: Windows.Win32.System.Performance.CommitMode, validation: POINTER(Windows.Win32.System.Performance.IValueMap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def Delete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def Start(self, Synchronous: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def Stop(self, Synchronous: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def SetXml(self, xml: Windows.Win32.Foundation.BSTR, validation: POINTER(Windows.Win32.System.Performance.IValueMap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def SetValue(self, key: Windows.Win32.Foundation.BSTR, value: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def GetValue(self, key: Windows.Win32.Foundation.BSTR, value: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IDataCollectorSetCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837524-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Count(self, retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, index: Windows.Win32.System.Variant.VARIANT, set: POINTER(Windows.Win32.System.Performance.IDataCollectorSet_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, retVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, set: Windows.Win32.System.Performance.IDataCollectorSet_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, set: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(self, sets: Windows.Win32.System.Performance.IDataCollectorSetCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDataCollectorSets(self, server: Windows.Win32.Foundation.BSTR, filter: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IDataManager(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837541-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Enabled(self, pfEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Enabled(self, fEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_CheckBeforeRunning(self, pfCheck: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_CheckBeforeRunning(self, fCheck: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_MinFreeDisk(self, MinFreeDisk: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_MinFreeDisk(self, MinFreeDisk: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_MaxSize(self, pulMaxSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_MaxSize(self, ulMaxSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MaxFolderCount(self, pulMaxFolderCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_MaxFolderCount(self, ulMaxFolderCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ResourcePolicy(self, pPolicy: POINTER(Windows.Win32.System.Performance.ResourcePolicy)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ResourcePolicy(self, Policy: Windows.Win32.System.Performance.ResourcePolicy) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_FolderActions(self, Actions: POINTER(Windows.Win32.System.Performance.IFolderActionCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_ReportSchema(self, ReportSchema: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_ReportSchema(self, ReportSchema: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_ReportFileName(self, pbstrFilename: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_ReportFileName(self, pbstrFilename: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_RuleTargetFileName(self, Filename: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_RuleTargetFileName(self, Filename: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_EventsFileName(self, pbstrFilename: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_EventsFileName(self, pbstrFilename: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Rules(self, pbstrXml: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Rules(self, bstrXml: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Run(self, Steps: Windows.Win32.System.Performance.DataManagerSteps, bstrFolder: Windows.Win32.Foundation.BSTR, Errors: POINTER(Windows.Win32.System.Performance.IValueMap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def Extract(self, CabFilename: Windows.Win32.Foundation.BSTR, DestinationPath: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IFolderAction(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837543-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Age(self, pulAge: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Age(self, ulAge: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Size(self, pulAge: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Size(self, ulAge: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Actions(self, Steps: POINTER(Windows.Win32.System.Performance.FolderActionSteps)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Actions(self, Steps: Windows.Win32.System.Performance.FolderActionSteps) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_SendCabTo(self, pbstrDestination: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_SendCabTo(self, bstrDestination: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IFolderActionCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837544-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Count(self, Count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, Index: Windows.Win32.System.Variant.VARIANT, Action: POINTER(Windows.Win32.System.Performance.IFolderAction_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, Enum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, Action: Windows.Win32.System.Performance.IFolderAction_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, Index: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(self, Actions: Windows.Win32.System.Performance.IFolderActionCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateFolderAction(self, FolderAction: POINTER(Windows.Win32.System.Performance.IFolderAction_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ILogFileItem(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d6b518dd-05c7-418a-89e6-4f9ce8c6841e}')
    @commethod(3)
    def get_Path(self, pstrValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ILogFiles(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{6a2a97e6-6851-41ea-87ad-2a8225335865}')
    @commethod(7)
    def get_Count(self, pLong: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get__NewEnum(self, ppIunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Item(self, index: Windows.Win32.System.Variant.VARIANT, ppI: POINTER(Windows.Win32.System.Performance.DILogFileItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pathname: Windows.Win32.Foundation.BSTR, ppI: POINTER(Windows.Win32.System.Performance.DILogFileItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, index: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IPerformanceCounterDataCollector(ComPtr):
    extends: Windows.Win32.System.Performance.IDataCollector
    _iid_ = Guid('{03837506-098b-11d8-9414-505054503030}')
    @commethod(32)
    def get_DataSourceName(self, dsn: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_DataSourceName(self, dsn: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_PerformanceCounters(self, counters: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_PerformanceCounters(self, counters: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_LogFileFormat(self, format: POINTER(Windows.Win32.System.Performance.FileFormat)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_LogFileFormat(self, format: Windows.Win32.System.Performance.FileFormat) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_SampleInterval(self, interval: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_SampleInterval(self, interval: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_SegmentMaxRecords(self, records: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_SegmentMaxRecords(self, records: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISchedule(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0383753a-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_StartDate(self, start: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_StartDate(self, start: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_EndDate(self, end: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_EndDate(self, end: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_StartTime(self, start: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_StartTime(self, start: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Days(self, days: POINTER(Windows.Win32.System.Performance.WeekDays)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Days(self, days: Windows.Win32.System.Performance.WeekDays) -> Windows.Win32.Foundation.HRESULT: ...
class IScheduleCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{0383753d-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Count(self, retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, index: Windows.Win32.System.Variant.VARIANT, ppSchedule: POINTER(Windows.Win32.System.Performance.ISchedule_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ienum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pSchedule: Windows.Win32.System.Performance.ISchedule_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, vSchedule: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(self, pSchedules: Windows.Win32.System.Performance.IScheduleCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateSchedule(self, Schedule: POINTER(Windows.Win32.System.Performance.ISchedule_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISystemMonitor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{194eb241-c32c-11cf-9398-00aa00a3ddea}')
    @commethod(3)
    def get_Appearance(self, iAppearance: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Appearance(self, iAppearance: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_BackColor(self, pColor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_BackColor(self, Color: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_BorderStyle(self, iBorderStyle: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_BorderStyle(self, iBorderStyle: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ForeColor(self, pColor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ForeColor(self, Color: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Font(self, ppFont: POINTER(Windows.Win32.System.Ole.IFontDisp_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def putref_Font(self, pFont: Windows.Win32.System.Ole.IFontDisp_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Counters(self, ppICounters: POINTER(Windows.Win32.System.Performance.ICounters_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_ShowVerticalGrid(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ShowVerticalGrid(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ShowHorizontalGrid(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ShowHorizontalGrid(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ShowLegend(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ShowLegend(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_ShowScaleLabels(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_ShowScaleLabels(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_ShowValueBar(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_ShowValueBar(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_MaximumScale(self, iValue: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_MaximumScale(self, piValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_MinimumScale(self, iValue: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_MinimumScale(self, piValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_UpdateInterval(self, fValue: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_UpdateInterval(self, pfValue: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_DisplayType(self, eDisplayType: Windows.Win32.System.Performance.DisplayTypeConstants) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_DisplayType(self, peDisplayType: POINTER(Windows.Win32.System.Performance.DisplayTypeConstants)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_ManualUpdate(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_ManualUpdate(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_GraphTitle(self, bsTitle: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_GraphTitle(self, pbsTitle: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_YAxisLabel(self, bsTitle: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_YAxisLabel(self, pbsTitle: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def CollectSample(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def UpdateGraph(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def BrowseCounters(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def DisplayProperties(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def Counter(self, iIndex: Int32, ppICounter: POINTER(Windows.Win32.System.Performance.ICounterItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def AddCounter(self, bsPath: Windows.Win32.Foundation.BSTR, ppICounter: POINTER(Windows.Win32.System.Performance.ICounterItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def DeleteCounter(self, pCtr: Windows.Win32.System.Performance.ICounterItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_BackColorCtl(self, pColor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_BackColorCtl(self, Color: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_LogFileName(self, bsFileName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_LogFileName(self, bsFileName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_LogViewStart(self, StartTime: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_LogViewStart(self, StartTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def put_LogViewStop(self, StopTime: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def get_LogViewStop(self, StopTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_GridColor(self, pColor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def put_GridColor(self, Color: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_TimeBarColor(self, pColor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def put_TimeBarColor(self, Color: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_Highlight(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def put_Highlight(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_ShowToolbar(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def put_ShowToolbar(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def Paste(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def Copy(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def put_ReadOnly(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_ReadOnly(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def put_ReportValueType(self, eReportValueType: Windows.Win32.System.Performance.ReportValueTypeConstants) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def get_ReportValueType(self, peReportValueType: POINTER(Windows.Win32.System.Performance.ReportValueTypeConstants)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def put_MonitorDuplicateInstances(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def get_MonitorDuplicateInstances(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def put_DisplayFilter(self, iValue: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def get_DisplayFilter(self, piValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def get_LogFiles(self, ppILogFiles: POINTER(Windows.Win32.System.Performance.ILogFiles_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def put_DataSourceType(self, eDataSourceType: Windows.Win32.System.Performance.DataSourceTypeConstants) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def get_DataSourceType(self, peDataSourceType: POINTER(Windows.Win32.System.Performance.DataSourceTypeConstants)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def put_SqlDsnName(self, bsSqlDsnName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def get_SqlDsnName(self, bsSqlDsnName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def put_SqlLogSetName(self, bsSqlLogSetName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def get_SqlLogSetName(self, bsSqlLogSetName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ISystemMonitor2(ComPtr):
    extends: Windows.Win32.System.Performance.ISystemMonitor
    _iid_ = Guid('{08e3206a-5fd2-4fde-a8a5-8cb3b63d2677}')
    @commethod(79)
    def put_EnableDigitGrouping(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def get_EnableDigitGrouping(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def put_EnableToolTips(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def get_EnableToolTips(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def put_ShowTimeAxisLabels(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def get_ShowTimeAxisLabels(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def put_ChartScroll(self, bScroll: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def get_ChartScroll(self, pbScroll: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def put_DataPointCount(self, iNewCount: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def get_DataPointCount(self, piDataPointCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def ScaleToFit(self, bSelectedCountersOnly: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def SaveAs(self, bstrFileName: Windows.Win32.Foundation.BSTR, eSysmonFileType: Windows.Win32.System.Performance.SysmonFileType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(91)
    def Relog(self, bstrFileName: Windows.Win32.Foundation.BSTR, eSysmonFileType: Windows.Win32.System.Performance.SysmonFileType, iFilter: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def ClearData(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def get_LogSourceStartTime(self, pDate: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(94)
    def get_LogSourceStopTime(self, pDate: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(95)
    def SetLogViewRange(self, StartTime: Double, StopTime: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def GetLogViewRange(self, StartTime: POINTER(Double), StopTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(97)
    def BatchingLock(self, fLock: Windows.Win32.Foundation.VARIANT_BOOL, eBatchReason: Windows.Win32.System.Performance.SysmonBatchReason) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def LoadSettings(self, bstrSettingFileName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISystemMonitorEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
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
    extends: Windows.Win32.System.Performance.IDataCollector
    _iid_ = Guid('{0383750b-098b-11d8-9414-505054503030}')
    @commethod(32)
    def get_BufferSize(self, size: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def put_BufferSize(self, size: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_BuffersLost(self, buffers: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_BuffersLost(self, buffers: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_BuffersWritten(self, buffers: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def put_BuffersWritten(self, buffers: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_ClockType(self, clock: POINTER(Windows.Win32.System.Performance.ClockType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def put_ClockType(self, clock: Windows.Win32.System.Performance.ClockType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_EventsLost(self, events: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_EventsLost(self, events: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_ExtendedModes(self, mode: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_ExtendedModes(self, mode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_FlushTimer(self, seconds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_FlushTimer(self, seconds: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_FreeBuffers(self, buffers: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_FreeBuffers(self, buffers: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_Guid(self, guid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_Guid(self, guid: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_IsKernelTrace(self, kernel: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def get_MaximumBuffers(self, buffers: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def put_MaximumBuffers(self, buffers: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_MinimumBuffers(self, buffers: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def put_MinimumBuffers(self, buffers: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_NumberOfBuffers(self, buffers: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def put_NumberOfBuffers(self, buffers: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_PreallocateFile(self, allocate: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def put_PreallocateFile(self, allocate: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_ProcessMode(self, process: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def put_ProcessMode(self, process: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def get_RealTimeBuffersLost(self, buffers: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def put_RealTimeBuffersLost(self, buffers: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def get_SessionId(self, id: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def put_SessionId(self, id: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_SessionName(self, name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def put_SessionName(self, name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def get_SessionThreadId(self, tid: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def put_SessionThreadId(self, tid: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def get_StreamMode(self, mode: POINTER(Windows.Win32.System.Performance.StreamMode)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def put_StreamMode(self, mode: Windows.Win32.System.Performance.StreamMode) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def get_TraceDataProviders(self, providers: POINTER(Windows.Win32.System.Performance.ITraceDataProviderCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITraceDataProvider(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837512-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_DisplayName(self, name: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_DisplayName(self, name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Guid(self, guid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Guid(self, guid: Guid) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Level(self, ppLevel: POINTER(Windows.Win32.System.Performance.IValueMap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_KeywordsAny(self, ppKeywords: POINTER(Windows.Win32.System.Performance.IValueMap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_KeywordsAll(self, ppKeywords: POINTER(Windows.Win32.System.Performance.IValueMap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Properties(self, ppProperties: POINTER(Windows.Win32.System.Performance.IValueMap_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_FilterEnabled(self, FilterEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_FilterEnabled(self, FilterEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_FilterType(self, pulType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_FilterType(self, ulType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_FilterData(self, ppData: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_FilterData(self, pData: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Query(self, bstrName: Windows.Win32.Foundation.BSTR, bstrServer: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Resolve(self, pFrom: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetSecurity(self, Sddl: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetSecurity(self, SecurityInfo: UInt32, Sddl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetRegisteredProcesses(self, Processes: POINTER(Windows.Win32.System.Performance.IValueMap_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITraceDataProviderCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837510-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Count(self, retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, index: Windows.Win32.System.Variant.VARIANT, ppProvider: POINTER(Windows.Win32.System.Performance.ITraceDataProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, retVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, pProvider: Windows.Win32.System.Performance.ITraceDataProvider_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, vProvider: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddRange(self, providers: Windows.Win32.System.Performance.ITraceDataProviderCollection_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateTraceDataProvider(self, Provider: POINTER(Windows.Win32.System.Performance.ITraceDataProvider_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetTraceDataProviders(self, server: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetTraceDataProvidersByProcess(self, Server: Windows.Win32.Foundation.BSTR, Pid: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IValueMap(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837534-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Count(self, retVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, index: Windows.Win32.System.Variant.VARIANT, value: POINTER(Windows.Win32.System.Performance.IValueMapItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, retVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Description(self, description: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_Description(self, description: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Value(self, Value: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Value(self, Value: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ValueMapType(self, type: POINTER(Windows.Win32.System.Performance.ValueMapType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_ValueMapType(self, type: Windows.Win32.System.Performance.ValueMapType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Add(self, value: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Remove(self, value: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def AddRange(self, map: Windows.Win32.System.Performance.IValueMap_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CreateValueMapItem(self, Item: POINTER(Windows.Win32.System.Performance.IValueMapItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IValueMapItem(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{03837533-098b-11d8-9414-505054503030}')
    @commethod(7)
    def get_Description(self, description: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Description(self, description: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Enabled(self, enabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Enabled(self, enabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Key(self, key: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Key(self, key: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Value(self, Value: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Value(self, Value: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ValueMapType(self, type: POINTER(Windows.Win32.System.Performance.ValueMapType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ValueMapType(self, type: Windows.Win32.System.Performance.ValueMapType) -> Windows.Win32.Foundation.HRESULT: ...
LegacyDataCollectorSet = Guid('{03837526-098b-11d8-9414-505054503030}')
LegacyDataCollectorSetCollection = Guid('{03837527-098b-11d8-9414-505054503030}')
LegacyTraceSession = Guid('{03837528-098b-11d8-9414-505054503030}')
LegacyTraceSessionCollection = Guid('{03837529-098b-11d8-9414-505054503030}')
LogFileItem = Guid('{16ec5be8-df93-4237-94e4-9ee918111d71}')
LogFiles = Guid('{2735d9fd-f6b9-4f19-a5d9-e2d068584bc5}')
class PDH_BROWSE_DLG_CONFIG_A(EasyCastStructure):
    _bitfield: UInt32
    hWndOwner: Windows.Win32.Foundation.HWND
    szDataSource: Windows.Win32.Foundation.PSTR
    szReturnPathBuffer: Windows.Win32.Foundation.PSTR
    cchReturnPathLength: UInt32
    pCallBack: Windows.Win32.System.Performance.CounterPathCallBack
    dwCallBackArg: UIntPtr
    CallBackStatus: Int32
    dwDefaultDetailLevel: Windows.Win32.System.Performance.PERF_DETAIL
    szDialogBoxCaption: Windows.Win32.Foundation.PSTR
class PDH_BROWSE_DLG_CONFIG_HA(EasyCastStructure):
    _bitfield: UInt32
    hWndOwner: Windows.Win32.Foundation.HWND
    hDataSource: IntPtr
    szReturnPathBuffer: Windows.Win32.Foundation.PSTR
    cchReturnPathLength: UInt32
    pCallBack: Windows.Win32.System.Performance.CounterPathCallBack
    dwCallBackArg: UIntPtr
    CallBackStatus: Int32
    dwDefaultDetailLevel: Windows.Win32.System.Performance.PERF_DETAIL
    szDialogBoxCaption: Windows.Win32.Foundation.PSTR
class PDH_BROWSE_DLG_CONFIG_HW(EasyCastStructure):
    _bitfield: UInt32
    hWndOwner: Windows.Win32.Foundation.HWND
    hDataSource: IntPtr
    szReturnPathBuffer: Windows.Win32.Foundation.PWSTR
    cchReturnPathLength: UInt32
    pCallBack: Windows.Win32.System.Performance.CounterPathCallBack
    dwCallBackArg: UIntPtr
    CallBackStatus: Int32
    dwDefaultDetailLevel: Windows.Win32.System.Performance.PERF_DETAIL
    szDialogBoxCaption: Windows.Win32.Foundation.PWSTR
class PDH_BROWSE_DLG_CONFIG_W(EasyCastStructure):
    _bitfield: UInt32
    hWndOwner: Windows.Win32.Foundation.HWND
    szDataSource: Windows.Win32.Foundation.PWSTR
    szReturnPathBuffer: Windows.Win32.Foundation.PWSTR
    cchReturnPathLength: UInt32
    pCallBack: Windows.Win32.System.Performance.CounterPathCallBack
    dwCallBackArg: UIntPtr
    CallBackStatus: Int32
    dwDefaultDetailLevel: Windows.Win32.System.Performance.PERF_DETAIL
    szDialogBoxCaption: Windows.Win32.Foundation.PWSTR
class PDH_COUNTER_INFO_A(EasyCastStructure):
    dwLength: UInt32
    dwType: UInt32
    CVersion: UInt32
    CStatus: UInt32
    lScale: Int32
    lDefaultScale: Int32
    dwUserData: UIntPtr
    dwQueryUserData: UIntPtr
    szFullPath: Windows.Win32.Foundation.PSTR
    Anonymous: _Anonymous_e__Union
    szExplainText: Windows.Win32.Foundation.PSTR
    DataBuffer: UInt32 * 1
    class _Anonymous_e__Union(EasyCastUnion):
        DataItemPath: Windows.Win32.System.Performance.PDH_DATA_ITEM_PATH_ELEMENTS_A
        CounterPath: Windows.Win32.System.Performance.PDH_COUNTER_PATH_ELEMENTS_A
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            szMachineName: Windows.Win32.Foundation.PSTR
            szObjectName: Windows.Win32.Foundation.PSTR
            szInstanceName: Windows.Win32.Foundation.PSTR
            szParentInstance: Windows.Win32.Foundation.PSTR
            dwInstanceIndex: UInt32
            szCounterName: Windows.Win32.Foundation.PSTR
class PDH_COUNTER_INFO_W(EasyCastStructure):
    dwLength: UInt32
    dwType: UInt32
    CVersion: UInt32
    CStatus: UInt32
    lScale: Int32
    lDefaultScale: Int32
    dwUserData: UIntPtr
    dwQueryUserData: UIntPtr
    szFullPath: Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    szExplainText: Windows.Win32.Foundation.PWSTR
    DataBuffer: UInt32 * 1
    class _Anonymous_e__Union(EasyCastUnion):
        DataItemPath: Windows.Win32.System.Performance.PDH_DATA_ITEM_PATH_ELEMENTS_W
        CounterPath: Windows.Win32.System.Performance.PDH_COUNTER_PATH_ELEMENTS_W
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            szMachineName: Windows.Win32.Foundation.PWSTR
            szObjectName: Windows.Win32.Foundation.PWSTR
            szInstanceName: Windows.Win32.Foundation.PWSTR
            szParentInstance: Windows.Win32.Foundation.PWSTR
            dwInstanceIndex: UInt32
            szCounterName: Windows.Win32.Foundation.PWSTR
class PDH_COUNTER_PATH_ELEMENTS_A(EasyCastStructure):
    szMachineName: Windows.Win32.Foundation.PSTR
    szObjectName: Windows.Win32.Foundation.PSTR
    szInstanceName: Windows.Win32.Foundation.PSTR
    szParentInstance: Windows.Win32.Foundation.PSTR
    dwInstanceIndex: UInt32
    szCounterName: Windows.Win32.Foundation.PSTR
class PDH_COUNTER_PATH_ELEMENTS_W(EasyCastStructure):
    szMachineName: Windows.Win32.Foundation.PWSTR
    szObjectName: Windows.Win32.Foundation.PWSTR
    szInstanceName: Windows.Win32.Foundation.PWSTR
    szParentInstance: Windows.Win32.Foundation.PWSTR
    dwInstanceIndex: UInt32
    szCounterName: Windows.Win32.Foundation.PWSTR
class PDH_DATA_ITEM_PATH_ELEMENTS_A(EasyCastStructure):
    szMachineName: Windows.Win32.Foundation.PSTR
    ObjectGUID: Guid
    dwItemId: UInt32
    szInstanceName: Windows.Win32.Foundation.PSTR
class PDH_DATA_ITEM_PATH_ELEMENTS_W(EasyCastStructure):
    szMachineName: Windows.Win32.Foundation.PWSTR
    ObjectGUID: Guid
    dwItemId: UInt32
    szInstanceName: Windows.Win32.Foundation.PWSTR
PDH_DLL_VERSION = UInt32
PDH_CVERSION_WIN50: PDH_DLL_VERSION = 1280
PDH_VERSION: PDH_DLL_VERSION = 1283
PDH_FMT = UInt32
PDH_FMT_DOUBLE: PDH_FMT = 512
PDH_FMT_LARGE: PDH_FMT = 1024
PDH_FMT_LONG: PDH_FMT = 256
class PDH_FMT_COUNTERVALUE(EasyCastStructure):
    CStatus: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        longValue: Int32
        doubleValue: Double
        largeValue: Int64
        AnsiStringValue: Windows.Win32.Foundation.PSTR
        WideStringValue: Windows.Win32.Foundation.PWSTR
class PDH_FMT_COUNTERVALUE_ITEM_A(EasyCastStructure):
    szName: Windows.Win32.Foundation.PSTR
    FmtValue: Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE
class PDH_FMT_COUNTERVALUE_ITEM_W(EasyCastStructure):
    szName: Windows.Win32.Foundation.PWSTR
    FmtValue: Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE
PDH_LOG = UInt32
PDH_LOG_READ_ACCESS: PDH_LOG = 65536
PDH_LOG_WRITE_ACCESS: PDH_LOG = 131072
PDH_LOG_UPDATE_ACCESS: PDH_LOG = 262144
class PDH_LOG_SERVICE_QUERY_INFO_A(EasyCastStructure):
    dwSize: UInt32
    dwFlags: UInt32
    dwLogQuota: UInt32
    szLogFileCaption: Windows.Win32.Foundation.PSTR
    szDefaultDir: Windows.Win32.Foundation.PSTR
    szBaseFileName: Windows.Win32.Foundation.PSTR
    dwFileType: UInt32
    dwReserved: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        class _Anonymous1_e__Struct(EasyCastStructure):
            PdlAutoNameInterval: UInt32
            PdlAutoNameUnits: UInt32
            PdlCommandFilename: Windows.Win32.Foundation.PSTR
            PdlCounterList: Windows.Win32.Foundation.PSTR
            PdlAutoNameFormat: UInt32
            PdlSampleInterval: UInt32
            PdlLogStartTime: Windows.Win32.Foundation.FILETIME
            PdlLogEndTime: Windows.Win32.Foundation.FILETIME
        class _Anonymous2_e__Struct(EasyCastStructure):
            TlNumberOfBuffers: UInt32
            TlMinimumBuffers: UInt32
            TlMaximumBuffers: UInt32
            TlFreeBuffers: UInt32
            TlBufferSize: UInt32
            TlEventsLost: UInt32
            TlLoggerThreadId: UInt32
            TlBuffersWritten: UInt32
            TlLogHandle: UInt32
            TlLogFileName: Windows.Win32.Foundation.PSTR
class PDH_LOG_SERVICE_QUERY_INFO_W(EasyCastStructure):
    dwSize: UInt32
    dwFlags: UInt32
    dwLogQuota: UInt32
    szLogFileCaption: Windows.Win32.Foundation.PWSTR
    szDefaultDir: Windows.Win32.Foundation.PWSTR
    szBaseFileName: Windows.Win32.Foundation.PWSTR
    dwFileType: UInt32
    dwReserved: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        class _Anonymous1_e__Struct(EasyCastStructure):
            PdlAutoNameInterval: UInt32
            PdlAutoNameUnits: UInt32
            PdlCommandFilename: Windows.Win32.Foundation.PWSTR
            PdlCounterList: Windows.Win32.Foundation.PWSTR
            PdlAutoNameFormat: UInt32
            PdlSampleInterval: UInt32
            PdlLogStartTime: Windows.Win32.Foundation.FILETIME
            PdlLogEndTime: Windows.Win32.Foundation.FILETIME
        class _Anonymous2_e__Struct(EasyCastStructure):
            TlNumberOfBuffers: UInt32
            TlMinimumBuffers: UInt32
            TlMaximumBuffers: UInt32
            TlFreeBuffers: UInt32
            TlBufferSize: UInt32
            TlEventsLost: UInt32
            TlLoggerThreadId: UInt32
            TlBuffersWritten: UInt32
            TlLogHandle: UInt32
            TlLogFileName: Windows.Win32.Foundation.PWSTR
PDH_LOG_TYPE = UInt32
PDH_LOG_TYPE_UNDEFINED: PDH_LOG_TYPE = 0
PDH_LOG_TYPE_CSV: PDH_LOG_TYPE = 1
PDH_LOG_TYPE_SQL: PDH_LOG_TYPE = 7
PDH_LOG_TYPE_TSV: PDH_LOG_TYPE = 2
PDH_LOG_TYPE_BINARY: PDH_LOG_TYPE = 8
PDH_LOG_TYPE_PERFMON: PDH_LOG_TYPE = 6
PDH_PATH_FLAGS = UInt32
PDH_PATH_WBEM_RESULT: PDH_PATH_FLAGS = 1
PDH_PATH_WBEM_INPUT: PDH_PATH_FLAGS = 2
PDH_PATH_WBEM_NONE: PDH_PATH_FLAGS = 0
class PDH_RAW_COUNTER(EasyCastStructure):
    CStatus: UInt32
    TimeStamp: Windows.Win32.Foundation.FILETIME
    FirstValue: Int64
    SecondValue: Int64
    MultiCount: UInt32
class PDH_RAW_COUNTER_ITEM_A(EasyCastStructure):
    szName: Windows.Win32.Foundation.PSTR
    RawValue: Windows.Win32.System.Performance.PDH_RAW_COUNTER
class PDH_RAW_COUNTER_ITEM_W(EasyCastStructure):
    szName: Windows.Win32.Foundation.PWSTR
    RawValue: Windows.Win32.System.Performance.PDH_RAW_COUNTER
class PDH_RAW_LOG_RECORD(EasyCastStructure):
    dwStructureSize: UInt32
    dwRecordType: Windows.Win32.System.Performance.PDH_LOG_TYPE
    dwItems: UInt32
    RawBytes: Byte * 1
PDH_SELECT_DATA_SOURCE_FLAGS = UInt32
PDH_FLAGS_FILE_BROWSER_ONLY: PDH_SELECT_DATA_SOURCE_FLAGS = 1
PDH_FLAGS_NONE: PDH_SELECT_DATA_SOURCE_FLAGS = 0
class PDH_STATISTICS(EasyCastStructure):
    dwFormat: UInt32
    count: UInt32
    min: Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE
    max: Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE
    mean: Windows.Win32.System.Performance.PDH_FMT_COUNTERVALUE
class PDH_TIME_INFO(EasyCastStructure):
    StartTime: Int64
    EndTime: Int64
    SampleCount: UInt32
@winfunctype_pointer
def PERFLIBREQUEST(RequestCode: UInt32, Buffer: VoidPtr, BufferSize: UInt32) -> UInt32: ...
class PERF_COUNTERSET_INFO(EasyCastStructure):
    CounterSetGuid: Guid
    ProviderGuid: Guid
    NumCounters: UInt32
    InstanceType: UInt32
class PERF_COUNTERSET_INSTANCE(EasyCastStructure):
    CounterSetGuid: Guid
    dwSize: UInt32
    InstanceId: UInt32
    InstanceNameOffset: UInt32
    InstanceNameSize: UInt32
class PERF_COUNTERSET_REG_INFO(EasyCastStructure):
    CounterSetGuid: Guid
    CounterSetType: UInt32
    DetailLevel: UInt32
    NumCounters: UInt32
    InstanceType: UInt32
PERF_COUNTER_AGGREGATE_FUNC = UInt32
PERF_AGGREGATE_UNDEFINED: PERF_COUNTER_AGGREGATE_FUNC = 0
PERF_AGGREGATE_TOTAL: PERF_COUNTER_AGGREGATE_FUNC = 1
PERF_AGGREGATE_AVG: PERF_COUNTER_AGGREGATE_FUNC = 2
PERF_AGGREGATE_MIN: PERF_COUNTER_AGGREGATE_FUNC = 3
class PERF_COUNTER_BLOCK(EasyCastStructure):
    ByteLength: UInt32
class PERF_COUNTER_DATA(EasyCastStructure):
    dwDataSize: UInt32
    dwSize: UInt32
if ARCH in 'X64,ARM64':
    class PERF_COUNTER_DEFINITION(EasyCastStructure):
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
if ARCH in 'X86':
    class PERF_COUNTER_DEFINITION(EasyCastStructure):
        ByteLength: UInt32
        CounterNameTitleIndex: UInt32
        CounterNameTitle: Windows.Win32.Foundation.PWSTR
        CounterHelpTitleIndex: UInt32
        CounterHelpTitle: Windows.Win32.Foundation.PWSTR
        DefaultScale: Int32
        DetailLevel: UInt32
        CounterType: UInt32
        CounterSize: UInt32
        CounterOffset: UInt32
class PERF_COUNTER_HEADER(EasyCastStructure):
    dwStatus: UInt32
    dwType: Windows.Win32.System.Performance.PerfCounterDataType
    dwSize: UInt32
    Reserved: UInt32
class PERF_COUNTER_IDENTIFIER(EasyCastStructure):
    CounterSetGuid: Guid
    Status: UInt32
    Size: UInt32
    CounterId: UInt32
    InstanceId: UInt32
    Index: UInt32
    Reserved: UInt32
class PERF_COUNTER_IDENTITY(EasyCastStructure):
    CounterSetGuid: Guid
    BufferSize: UInt32
    CounterId: UInt32
    InstanceId: UInt32
    MachineOffset: UInt32
    NameOffset: UInt32
    Reserved: UInt32
class PERF_COUNTER_INFO(EasyCastStructure):
    CounterId: UInt32
    Type: UInt32
    Attrib: UInt64
    Size: UInt32
    DetailLevel: UInt32
    Scale: Int32
    Offset: UInt32
class PERF_COUNTER_REG_INFO(EasyCastStructure):
    CounterId: UInt32
    Type: UInt32
    Attrib: UInt64
    DetailLevel: UInt32
    DefaultScale: Int32
    BaseCounterId: UInt32
    PerfTimeId: UInt32
    PerfFreqId: UInt32
    MultiId: UInt32
    AggregateFunc: Windows.Win32.System.Performance.PERF_COUNTER_AGGREGATE_FUNC
    Reserved: UInt32
class PERF_DATA_BLOCK(EasyCastStructure):
    Signature: Char * 4
    LittleEndian: UInt32
    Version: UInt32
    Revision: UInt32
    TotalByteLength: UInt32
    HeaderLength: UInt32
    NumObjectTypes: UInt32
    DefaultObject: Int32
    SystemTime: Windows.Win32.Foundation.SYSTEMTIME
    PerfTime: Int64
    PerfFreq: Int64
    PerfTime100nSec: Int64
    SystemNameLength: UInt32
    SystemNameOffset: UInt32
class PERF_DATA_HEADER(EasyCastStructure):
    dwTotalSize: UInt32
    dwNumCounters: UInt32
    PerfTimeStamp: Int64
    PerfTime100NSec: Int64
    PerfFreq: Int64
    SystemTime: Windows.Win32.Foundation.SYSTEMTIME
PERF_DETAIL = UInt32
PERF_DETAIL_NOVICE: PERF_DETAIL = 100
PERF_DETAIL_ADVANCED: PERF_DETAIL = 200
PERF_DETAIL_EXPERT: PERF_DETAIL = 300
PERF_DETAIL_WIZARD: PERF_DETAIL = 400
class PERF_INSTANCE_DEFINITION(EasyCastStructure):
    ByteLength: UInt32
    ParentObjectTitleIndex: UInt32
    ParentObjectInstance: UInt32
    UniqueID: Int32
    NameOffset: UInt32
    NameLength: UInt32
class PERF_INSTANCE_HEADER(EasyCastStructure):
    Size: UInt32
    InstanceId: UInt32
@winfunctype_pointer
def PERF_MEM_ALLOC(AllocSize: UIntPtr, pContext: VoidPtr) -> VoidPtr: ...
@winfunctype_pointer
def PERF_MEM_FREE(pBuffer: VoidPtr, pContext: VoidPtr) -> Void: ...
class PERF_MULTI_COUNTERS(EasyCastStructure):
    dwSize: UInt32
    dwCounters: UInt32
class PERF_MULTI_INSTANCES(EasyCastStructure):
    dwTotalSize: UInt32
    dwInstances: UInt32
if ARCH in 'X64,ARM64':
    class PERF_OBJECT_TYPE(EasyCastStructure):
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
if ARCH in 'X86':
    class PERF_OBJECT_TYPE(EasyCastStructure):
        TotalByteLength: UInt32
        DefinitionLength: UInt32
        HeaderLength: UInt32
        ObjectNameTitleIndex: UInt32
        ObjectNameTitle: Windows.Win32.Foundation.PWSTR
        ObjectHelpTitleIndex: UInt32
        ObjectHelpTitle: Windows.Win32.Foundation.PWSTR
        DetailLevel: UInt32
        NumCounters: UInt32
        DefaultCounter: Int32
        NumInstances: Int32
        CodePage: UInt32
        PerfTime: Int64
        PerfFreq: Int64
class PERF_PROVIDER_CONTEXT(EasyCastStructure):
    ContextSize: UInt32
    Reserved: UInt32
    ControlCallback: Windows.Win32.System.Performance.PERFLIBREQUEST
    MemAllocRoutine: Windows.Win32.System.Performance.PERF_MEM_ALLOC
    MemFreeRoutine: Windows.Win32.System.Performance.PERF_MEM_FREE
    pMemContext: VoidPtr
class PERF_STRING_BUFFER_HEADER(EasyCastStructure):
    dwSize: UInt32
    dwCounters: UInt32
class PERF_STRING_COUNTER_HEADER(EasyCastStructure):
    dwCounterId: UInt32
    dwOffset: UInt32
@winfunctype_pointer
def PLA_CABEXTRACT_CALLBACK(FileName: Windows.Win32.Foundation.PWSTR, Context: VoidPtr) -> Void: ...
@winfunctype_pointer
def PM_CLOSE_PROC() -> UInt32: ...
@winfunctype_pointer
def PM_COLLECT_PROC(pValueName: Windows.Win32.Foundation.PWSTR, ppData: POINTER(VoidPtr), pcbTotalBytes: POINTER(UInt32), pNumObjectTypes: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def PM_OPEN_PROC(pContext: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
PerfCounterDataType = Int32
PERF_ERROR_RETURN: PerfCounterDataType = 0
PERF_SINGLE_COUNTER: PerfCounterDataType = 1
PERF_MULTIPLE_COUNTERS: PerfCounterDataType = 2
PERF_MULTIPLE_INSTANCES: PerfCounterDataType = 4
PERF_COUNTERSET: PerfCounterDataType = 6
PerfRegInfoType = Int32
PERF_REG_COUNTERSET_STRUCT: PerfRegInfoType = 1
PERF_REG_COUNTER_STRUCT: PerfRegInfoType = 2
PERF_REG_COUNTERSET_NAME_STRING: PerfRegInfoType = 3
PERF_REG_COUNTERSET_HELP_STRING: PerfRegInfoType = 4
PERF_REG_COUNTER_NAME_STRINGS: PerfRegInfoType = 5
PERF_REG_COUNTER_HELP_STRINGS: PerfRegInfoType = 6
PERF_REG_PROVIDER_NAME: PerfRegInfoType = 7
PERF_REG_PROVIDER_GUID: PerfRegInfoType = 8
PERF_REG_COUNTERSET_ENGLISH_NAME: PerfRegInfoType = 9
PERF_REG_COUNTER_ENGLISH_NAMES: PerfRegInfoType = 10
REAL_TIME_DATA_SOURCE_ID_FLAGS = UInt32
DATA_SOURCE_REGISTRY: REAL_TIME_DATA_SOURCE_ID_FLAGS = 1
DATA_SOURCE_WBEM: REAL_TIME_DATA_SOURCE_ID_FLAGS = 4
ReportValueTypeConstants = Int32
ReportValueTypeConstants_sysmonDefaultValue: ReportValueTypeConstants = 0
ReportValueTypeConstants_sysmonCurrentValue: ReportValueTypeConstants = 1
ReportValueTypeConstants_sysmonAverage: ReportValueTypeConstants = 2
ReportValueTypeConstants_sysmonMinimum: ReportValueTypeConstants = 3
ReportValueTypeConstants_sysmonMaximum: ReportValueTypeConstants = 4
ResourcePolicy = Int32
ResourcePolicy_plaDeleteLargest: ResourcePolicy = 0
ResourcePolicy_plaDeleteOldest: ResourcePolicy = 1
ServerDataCollectorSet = Guid('{03837531-098b-11d8-9414-505054503030}')
ServerDataCollectorSetCollection = Guid('{03837532-098b-11d8-9414-505054503030}')
SourcePropPage = Guid('{0cf32aa1-7571-11d0-93c4-00aa00a3ddea}')
StreamMode = Int32
StreamMode_plaFile: StreamMode = 1
StreamMode_plaRealTime: StreamMode = 2
StreamMode_plaBoth: StreamMode = 3
StreamMode_plaBuffering: StreamMode = 4
SysmonBatchReason = Int32
SysmonBatchReason_sysmonBatchNone: SysmonBatchReason = 0
SysmonBatchReason_sysmonBatchAddFiles: SysmonBatchReason = 1
SysmonBatchReason_sysmonBatchAddCounters: SysmonBatchReason = 2
SysmonBatchReason_sysmonBatchAddFilesAutoCounters: SysmonBatchReason = 3
SysmonDataType = Int32
SysmonDataType_sysmonDataAvg: SysmonDataType = 1
SysmonDataType_sysmonDataMin: SysmonDataType = 2
SysmonDataType_sysmonDataMax: SysmonDataType = 3
SysmonDataType_sysmonDataTime: SysmonDataType = 4
SysmonDataType_sysmonDataCount: SysmonDataType = 5
SysmonFileType = Int32
SysmonFileType_sysmonFileHtml: SysmonFileType = 1
SysmonFileType_sysmonFileReport: SysmonFileType = 2
SysmonFileType_sysmonFileCsv: SysmonFileType = 3
SysmonFileType_sysmonFileTsv: SysmonFileType = 4
SysmonFileType_sysmonFileBlg: SysmonFileType = 5
SysmonFileType_sysmonFileRetiredBlg: SysmonFileType = 6
SysmonFileType_sysmonFileGif: SysmonFileType = 7
SystemDataCollectorSet = Guid('{03837546-098b-11d8-9414-505054503030}')
SystemDataCollectorSetCollection = Guid('{03837547-098b-11d8-9414-505054503030}')
SystemMonitor = Guid('{c4d2d8e0-d1dd-11ce-940f-008029004347}')
SystemMonitor2 = Guid('{7f30578c-5f38-4612-acfe-6ed04c7b7af8}')
TraceDataProvider = Guid('{03837513-098b-11d8-9414-505054503030}')
TraceDataProviderCollection = Guid('{03837511-098b-11d8-9414-505054503030}')
TraceSession = Guid('{0383751c-098b-11d8-9414-505054503030}')
TraceSessionCollection = Guid('{03837530-098b-11d8-9414-505054503030}')
ValueMapType = Int32
ValueMapType_plaIndex: ValueMapType = 1
ValueMapType_plaFlag: ValueMapType = 2
ValueMapType_plaFlagArray: ValueMapType = 3
ValueMapType_plaValidation: ValueMapType = 4
WeekDays = Int32
WeekDays_plaRunOnce: WeekDays = 0
WeekDays_plaSunday: WeekDays = 1
WeekDays_plaMonday: WeekDays = 2
WeekDays_plaTuesday: WeekDays = 4
WeekDays_plaWednesday: WeekDays = 8
WeekDays_plaThursday: WeekDays = 16
WeekDays_plaFriday: WeekDays = 32
WeekDays_plaSaturday: WeekDays = 64
WeekDays_plaEveryday: WeekDays = 127
class _ICounterItemUnion(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{de1a6b74-9182-4c41-8e2c-24c2cd30ee83}')
    @commethod(3)
    def get_Value(self, pdblValue: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Color(self, Color: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Color(self, pColor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_Width(self, iWidth: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Width(self, piValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_LineStyle(self, iLineStyle: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LineStyle(self, piValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ScaleFactor(self, iScale: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ScaleFactor(self, piValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Path(self, pstrValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetValue(self, Value: POINTER(Double), Status: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetStatistics(self, Max: POINTER(Double), Min: POINTER(Double), Avg: POINTER(Double), Status: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_Selected(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Selected(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_Visible(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Visible(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDataAt(self, iIndex: Int32, iWhich: Windows.Win32.System.Performance.SysmonDataType, pVariant: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class _ISystemMonitorUnion(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c8a77338-265f-4de5-aa25-c7da1ce5a8f4}')
    @commethod(3)
    def get_Appearance(self, iAppearance: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Appearance(self, iAppearance: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_BackColor(self, pColor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_BackColor(self, Color: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_BorderStyle(self, iBorderStyle: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_BorderStyle(self, iBorderStyle: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ForeColor(self, pColor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ForeColor(self, Color: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Font(self, ppFont: POINTER(Windows.Win32.System.Ole.IFontDisp_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def putref_Font(self, pFont: Windows.Win32.System.Ole.IFontDisp_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Counters(self, ppICounters: POINTER(Windows.Win32.System.Performance.ICounters_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_ShowVerticalGrid(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ShowVerticalGrid(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ShowHorizontalGrid(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ShowHorizontalGrid(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ShowLegend(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_ShowLegend(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_ShowScaleLabels(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_ShowScaleLabels(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_ShowValueBar(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_ShowValueBar(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_MaximumScale(self, iValue: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_MaximumScale(self, piValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_MinimumScale(self, iValue: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_MinimumScale(self, piValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_UpdateInterval(self, fValue: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_UpdateInterval(self, pfValue: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_DisplayType(self, eDisplayType: Windows.Win32.System.Performance.DisplayTypeConstants) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_DisplayType(self, peDisplayType: POINTER(Windows.Win32.System.Performance.DisplayTypeConstants)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_ManualUpdate(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_ManualUpdate(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_GraphTitle(self, bsTitle: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_GraphTitle(self, pbsTitle: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_YAxisLabel(self, bsTitle: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_YAxisLabel(self, pbsTitle: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def CollectSample(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def UpdateGraph(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def BrowseCounters(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def DisplayProperties(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def Counter(self, iIndex: Int32, ppICounter: POINTER(Windows.Win32.System.Performance.ICounterItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def AddCounter(self, bsPath: Windows.Win32.Foundation.BSTR, ppICounter: POINTER(Windows.Win32.System.Performance.ICounterItem_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def DeleteCounter(self, pCtr: Windows.Win32.System.Performance.ICounterItem_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def get_BackColorCtl(self, pColor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def put_BackColorCtl(self, Color: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_LogFileName(self, bsFileName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_LogFileName(self, bsFileName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_LogViewStart(self, StartTime: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_LogViewStart(self, StartTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def put_LogViewStop(self, StopTime: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def get_LogViewStop(self, StopTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def get_GridColor(self, pColor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def put_GridColor(self, Color: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def get_TimeBarColor(self, pColor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def put_TimeBarColor(self, Color: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_Highlight(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def put_Highlight(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_ShowToolbar(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def put_ShowToolbar(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def Paste(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def Copy(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def put_ReadOnly(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_ReadOnly(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def put_ReportValueType(self, eReportValueType: Windows.Win32.System.Performance.ReportValueTypeConstants) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def get_ReportValueType(self, peReportValueType: POINTER(Windows.Win32.System.Performance.ReportValueTypeConstants)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def put_MonitorDuplicateInstances(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def get_MonitorDuplicateInstances(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def put_DisplayFilter(self, iValue: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def get_DisplayFilter(self, piValue: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def get_LogFiles(self, ppILogFiles: POINTER(Windows.Win32.System.Performance.ILogFiles_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def put_DataSourceType(self, eDataSourceType: Windows.Win32.System.Performance.DataSourceTypeConstants) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def get_DataSourceType(self, peDataSourceType: POINTER(Windows.Win32.System.Performance.DataSourceTypeConstants)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def put_SqlDsnName(self, bsSqlDsnName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def get_SqlDsnName(self, bsSqlDsnName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def put_SqlLogSetName(self, bsSqlLogSetName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def get_SqlLogSetName(self, bsSqlLogSetName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def put_EnableDigitGrouping(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def get_EnableDigitGrouping(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def put_EnableToolTips(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def get_EnableToolTips(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def put_ShowTimeAxisLabels(self, bState: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def get_ShowTimeAxisLabels(self, pbState: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def put_ChartScroll(self, bScroll: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def get_ChartScroll(self, pbScroll: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def put_DataPointCount(self, iNewCount: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def get_DataPointCount(self, piDataPointCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def ScaleToFit(self, bSelectedCountersOnly: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def SaveAs(self, bstrFileName: Windows.Win32.Foundation.BSTR, eSysmonFileType: Windows.Win32.System.Performance.SysmonFileType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(91)
    def Relog(self, bstrFileName: Windows.Win32.Foundation.BSTR, eSysmonFileType: Windows.Win32.System.Performance.SysmonFileType, iFilter: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def ClearData(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def get_LogSourceStartTime(self, pDate: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(94)
    def get_LogSourceStopTime(self, pDate: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(95)
    def SetLogViewRange(self, StartTime: Double, StopTime: Double) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def GetLogViewRange(self, StartTime: POINTER(Double), StopTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(97)
    def BatchingLock(self, fLock: Windows.Win32.Foundation.VARIANT_BOOL, eBatchReason: Windows.Win32.System.Performance.SysmonBatchReason) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def LoadSettings(self, bstrSettingFileName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'CounterPathCallBack')
make_head(_module, 'DICounterItem')
make_head(_module, 'DILogFileItem')
make_head(_module, 'DISystemMonitor')
make_head(_module, 'DISystemMonitorEvents')
make_head(_module, 'DISystemMonitorInternal')
make_head(_module, 'IAlertDataCollector')
make_head(_module, 'IApiTracingDataCollector')
make_head(_module, 'IConfigurationDataCollector')
make_head(_module, 'ICounterItem')
make_head(_module, 'ICounterItem2')
make_head(_module, 'ICounters')
make_head(_module, 'IDataCollector')
make_head(_module, 'IDataCollectorCollection')
make_head(_module, 'IDataCollectorSet')
make_head(_module, 'IDataCollectorSetCollection')
make_head(_module, 'IDataManager')
make_head(_module, 'IFolderAction')
make_head(_module, 'IFolderActionCollection')
make_head(_module, 'ILogFileItem')
make_head(_module, 'ILogFiles')
make_head(_module, 'IPerformanceCounterDataCollector')
make_head(_module, 'ISchedule')
make_head(_module, 'IScheduleCollection')
make_head(_module, 'ISystemMonitor')
make_head(_module, 'ISystemMonitor2')
make_head(_module, 'ISystemMonitorEvents')
make_head(_module, 'ITraceDataCollector')
make_head(_module, 'ITraceDataProvider')
make_head(_module, 'ITraceDataProviderCollection')
make_head(_module, 'IValueMap')
make_head(_module, 'IValueMapItem')
make_head(_module, 'PDH_BROWSE_DLG_CONFIG_A')
make_head(_module, 'PDH_BROWSE_DLG_CONFIG_HA')
make_head(_module, 'PDH_BROWSE_DLG_CONFIG_HW')
make_head(_module, 'PDH_BROWSE_DLG_CONFIG_W')
make_head(_module, 'PDH_COUNTER_INFO_A')
make_head(_module, 'PDH_COUNTER_INFO_W')
make_head(_module, 'PDH_COUNTER_PATH_ELEMENTS_A')
make_head(_module, 'PDH_COUNTER_PATH_ELEMENTS_W')
make_head(_module, 'PDH_DATA_ITEM_PATH_ELEMENTS_A')
make_head(_module, 'PDH_DATA_ITEM_PATH_ELEMENTS_W')
make_head(_module, 'PDH_FMT_COUNTERVALUE')
make_head(_module, 'PDH_FMT_COUNTERVALUE_ITEM_A')
make_head(_module, 'PDH_FMT_COUNTERVALUE_ITEM_W')
make_head(_module, 'PDH_LOG_SERVICE_QUERY_INFO_A')
make_head(_module, 'PDH_LOG_SERVICE_QUERY_INFO_W')
make_head(_module, 'PDH_RAW_COUNTER')
make_head(_module, 'PDH_RAW_COUNTER_ITEM_A')
make_head(_module, 'PDH_RAW_COUNTER_ITEM_W')
make_head(_module, 'PDH_RAW_LOG_RECORD')
make_head(_module, 'PDH_STATISTICS')
make_head(_module, 'PDH_TIME_INFO')
make_head(_module, 'PERFLIBREQUEST')
make_head(_module, 'PERF_COUNTERSET_INFO')
make_head(_module, 'PERF_COUNTERSET_INSTANCE')
make_head(_module, 'PERF_COUNTERSET_REG_INFO')
make_head(_module, 'PERF_COUNTER_BLOCK')
make_head(_module, 'PERF_COUNTER_DATA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'PERF_COUNTER_DEFINITION')
if ARCH in 'X86':
    make_head(_module, 'PERF_COUNTER_DEFINITION')
make_head(_module, 'PERF_COUNTER_HEADER')
make_head(_module, 'PERF_COUNTER_IDENTIFIER')
make_head(_module, 'PERF_COUNTER_IDENTITY')
make_head(_module, 'PERF_COUNTER_INFO')
make_head(_module, 'PERF_COUNTER_REG_INFO')
make_head(_module, 'PERF_DATA_BLOCK')
make_head(_module, 'PERF_DATA_HEADER')
make_head(_module, 'PERF_INSTANCE_DEFINITION')
make_head(_module, 'PERF_INSTANCE_HEADER')
make_head(_module, 'PERF_MEM_ALLOC')
make_head(_module, 'PERF_MEM_FREE')
make_head(_module, 'PERF_MULTI_COUNTERS')
make_head(_module, 'PERF_MULTI_INSTANCES')
if ARCH in 'X64,ARM64':
    make_head(_module, 'PERF_OBJECT_TYPE')
if ARCH in 'X86':
    make_head(_module, 'PERF_OBJECT_TYPE')
make_head(_module, 'PERF_PROVIDER_CONTEXT')
make_head(_module, 'PERF_STRING_BUFFER_HEADER')
make_head(_module, 'PERF_STRING_COUNTER_HEADER')
make_head(_module, 'PLA_CABEXTRACT_CALLBACK')
make_head(_module, 'PM_CLOSE_PROC')
make_head(_module, 'PM_COLLECT_PROC')
make_head(_module, 'PM_OPEN_PROC')
make_head(_module, '_ICounterItemUnion')
make_head(_module, '_ISystemMonitorUnion')
